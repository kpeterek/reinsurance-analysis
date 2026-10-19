"""Price formation and market microstructure helpers (Chapter 2).

Contents
--------
* Call-auction clearing from limit-order schedules.
* Standardized surprise and the price response to a data release.
* Clearing price of a single asset from a set of reservation prices
  (ascending / English auction) and financed-buyer reservation prices.
* Roll (1984) effective-spread estimator and round-trip cost arithmetic.
* Appraisal smoothing (first-order partial adjustment) and the Geltner
  unsmoothing filter.
* Selection-bias and time-adjustment arithmetic for comparable sales.

Conventions follow the package docstring: rates and returns in decimals,
money in dollars, periods are the periods of the input series (a quarterly
series gives quarterly returns). Nothing here annualizes silently.
"""

from __future__ import annotations

import math
from typing import Sequence

from . import stats


# --------------------------------------------------------------------------
# Call auctions
# --------------------------------------------------------------------------

def auction_schedules(buys: Sequence[tuple[float, float]], sells: Sequence[tuple[float, float]],
                      market_buy: float = 0.0, market_sell: float = 0.0) -> list[dict]:
    """Cumulative demand and supply at every limit price in the book.

    ``buys`` and ``sells`` are (limit price, quantity) pairs. A buy order with
    limit L is willing to trade at any price p <= L; a sell order with limit L
    at any p >= L. Market orders are willing to trade at any price.

    Returns one row per candidate price (ascending) with demand D(p), supply
    S(p), executable volume min(D, S) and imbalance D - S.
    """
    prices = sorted({p for p, _ in buys} | {p for p, _ in sells})
    rows = []
    for p in prices:
        d = market_buy + sum(q for lim, q in buys if lim >= p)
        s = market_sell + sum(q for lim, q in sells if lim <= p)
        rows.append({"price": p, "demand": d, "supply": s, "volume": min(d, s), "imbalance": d - s})
    return rows


def call_auction_clearing(buys: Sequence[tuple[float, float]], sells: Sequence[tuple[float, float]],
                          market_buy: float = 0.0, market_sell: float = 0.0) -> dict:
    """Uncross a call auction.

    Rule (the common exchange rule, simplified): (1) maximize executed volume;
    (2) among ties, minimize |imbalance|; (3) if still tied, take the mean of
    the tied prices. Returns the clearing price, volume, and imbalance
    (positive = unfilled buy interest at the clearing price).
    """
    rows = auction_schedules(buys, sells, market_buy, market_sell)
    vmax = max(r["volume"] for r in rows)
    cand = [r for r in rows if r["volume"] == vmax]
    imin = min(abs(r["imbalance"]) for r in cand)
    cand = [r for r in cand if abs(r["imbalance"]) == imin]
    price = sum(r["price"] for r in cand) / len(cand)
    return {"price": price, "volume": vmax, "imbalance": cand[0]["imbalance"], "ties": len(cand)}


def walk_the_book(bids: Sequence[tuple[float, float]], quantity: float) -> dict:
    """Average execution price of a market sell of ``quantity`` against
    resting bids (price, qty), best price first. Raises if depth is short."""
    remaining, proceeds = quantity, 0.0
    for p, q in sorted(bids, key=lambda x: -x[0]):
        take = min(q, remaining)
        proceeds += take * p
        remaining -= take
        if remaining <= 0:
            break
    if remaining > 1e-12:
        raise ValueError("insufficient depth")
    return {"avg_price": proceeds / quantity, "proceeds": proceeds}


# --------------------------------------------------------------------------
# Expectations and surprise
# --------------------------------------------------------------------------

def standardized_surprise(actual: float, consensus: float, surprise_sd: float) -> float:
    """z = (actual - consensus) / sd(historical surprises)."""
    if surprise_sd <= 0:
        raise ValueError("surprise sd must be positive")
    return (actual - consensus) / surprise_sd


def yield_change_from_surprise(z: float, bp_per_sd: float) -> float:
    """Yield change in decimals for a sensitivity quoted in bp per 1 sd."""
    return z * bp_per_sd / 10_000.0


def price_change_from_yield(mod_duration: float, dy: float, convexity: float = 0.0) -> float:
    """dP/P = -D_mod dy + 0.5 C dy^2 (decimal)."""
    return -mod_duration * dy + 0.5 * convexity * dy * dy


# --------------------------------------------------------------------------
# Reservation prices and the marginal buyer
# --------------------------------------------------------------------------

def english_auction_price(buyer_reservations: Sequence[float], seller_reserve: float = 0.0) -> dict:
    """Single-asset ascending auction with private values.

    The highest-value buyer wins and pays (approximately) the second-highest
    reservation price, or the seller's reserve if that is higher. If the top
    reservation is below the seller's reserve, there is no trade.
    """
    r = sorted(buyer_reservations, reverse=True)
    if not r or r[0] < seller_reserve:
        return {"trade": False, "price": None, "winner_value": r[0] if r else None}
    second = r[1] if len(r) > 1 else seller_reserve
    return {"trade": True, "price": max(second, seller_reserve), "winner_value": r[0]}


def financed_reservation_price(equity: float, noi: float, max_ltv: float, min_dscr: float,
                               loan_constant: float) -> float:
    """Highest price a buyer with fixed equity can pay when the loan is the
    lesser of LTV and DSCR proceeds.

    LTV-bound price:  P = E / (1 - LTV)
    DSCR-bound loan:  L = NOI / (DSCR x K), price = E + L
    The binding constraint gives the lower price.
    """
    p_ltv = equity / (1.0 - max_ltv)
    loan_dscr = noi / (min_dscr * loan_constant)
    p_dscr = equity + loan_dscr
    return min(p_ltv, p_dscr)


# --------------------------------------------------------------------------
# Spreads
# --------------------------------------------------------------------------

def first_differences(prices: Sequence[float]) -> list[float]:
    return [prices[i] - prices[i - 1] for i in range(1, len(prices))]


def roll_spread(prices: Sequence[float]) -> float:
    """Roll (1984) estimator S = 2 sqrt(-cov(dp_t, dp_{t-1})).

    Covariance is the sample covariance (n - 1 divisor) between the vectors
    (dp_2..dp_N) and (dp_1..dp_{N-1}). Returns NaN when the autocovariance is
    non-negative (the estimator is undefined; the model is rejected).
    Units: same as prices.
    """
    dp = first_differences(prices)
    c = stats.covariance(dp[1:], dp[:-1])
    return 2.0 * math.sqrt(-c) if c < 0 else float("nan")


def roll_spread_from_autocov(autocov: float) -> float:
    return 2.0 * math.sqrt(-autocov) if autocov < 0 else float("nan")


def round_trip_cost(buy_cost: float, sell_cost: float) -> float:
    """Round-trip cost as a fraction of value: buy at V(1+b), sell at V(1-s).

    Cost per dollar of entry = 1 - (1-s)/(1+b). For small b, s this is ~b+s.
    """
    return 1.0 - (1.0 - sell_cost) / (1.0 + buy_cost)


def annualized_cost_drag(round_trip: float, years: float) -> float:
    """Geometric annual return drag from a one-time round-trip cost over a hold."""
    return 1.0 - (1.0 - round_trip) ** (1.0 / years)


# --------------------------------------------------------------------------
# Appraisal smoothing
# --------------------------------------------------------------------------

def smooth(true_returns: Sequence[float], a: float, r_star_prev: float = 0.0) -> list[float]:
    """First-order partial adjustment: r*_t = (1 - a) r_t + a r*_{t-1}."""
    out, prev = [], r_star_prev
    for r in true_returns:
        prev = (1.0 - a) * r + a * prev
        out.append(prev)
    return out


def geltner_unsmooth(appraisal_returns: Sequence[float], a: float) -> list[float]:
    """Geltner filter r_t = (r*_t - a r*_{t-1}) / (1 - a).

    ``appraisal_returns`` includes the initial observation r*_0, so the output
    has one fewer element (r_1 ... r_N). 0 <= a < 1.
    """
    if not 0.0 <= a < 1.0:
        raise ValueError("a must be in [0, 1)")
    s = appraisal_returns
    return [(s[t] - a * s[t - 1]) / (1.0 - a) for t in range(1, len(s))]


def cumulative_return(returns: Sequence[float]) -> float:
    g = 1.0
    for r in returns:
        g *= 1.0 + r
    return g - 1.0


def smoothing_vol_ratio(a: float) -> float:
    """sd(r*)/sd(r) for i.i.d. true returns: sqrt((1 - a)/(1 + a))."""
    return math.sqrt((1.0 - a) / (1.0 + a))


def smoothing_mean_lag(a: float) -> float:
    """Mean lag (periods) of the geometric weights (1-a)a^k: a/(1-a)."""
    return a / (1.0 - a)


# --------------------------------------------------------------------------
# Comparable sales
# --------------------------------------------------------------------------

def time_adjust_cap(cap_at_sale: float, index_at_sale: float, index_now: float) -> float:
    """Cap rate restated to today with a value index: c_now = c_sale x I_sale / I_now
    (value moves inversely to the cap rate at constant NOI)."""
    return cap_at_sale * index_at_sale / index_now


def selection_bias(all_changes: Sequence[float], traded_mask: Sequence[bool]) -> dict:
    """Mean change of traded assets versus the full population."""
    traded = [c for c, t in zip(all_changes, traded_mask) if t]
    pop = stats.mean(all_changes)
    tr = stats.mean(traded)
    return {"population_mean": pop, "traded_mean": tr, "bias": tr - pop, "n_traded": len(traded)}
