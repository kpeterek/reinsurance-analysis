"""Alternative and emerging speculative assets (Chapter 19).

Private-fund multiples and the Kaplan-Schoar PME, power-law portfolio
distributions, tiered auction premiums, repeat-sales indices, stale-NAV
correction, and resale-only valuation.

Conventions
-----------
* Cash flows are annual, at period ends t = 0, 1, ..., T, unless stated.
* Contributions and distributions are passed as **positive** amounts in
  separate vectors; the LP net flow is D_t - C_t (investor outflows negative).
* Rates and returns are decimals.
"""

from __future__ import annotations

import math
from itertools import product
from typing import Sequence


# --------------------------------------------------------------------------
# Private-fund multiples
# --------------------------------------------------------------------------

def fund_multiples(contributions: Sequence[float], distributions: Sequence[float],
                   nav: float = 0.0) -> dict:
    """DPI, RVPI and TVPI from cumulative paid-in capital, distributions and residual NAV.

    DPI = sum D / sum C; RVPI = NAV / sum C; TVPI = DPI + RVPI.
    Multiples ignore timing: the same TVPI over 4 or 12 years is a different return.
    """
    paid_in = float(sum(contributions))
    dist = float(sum(distributions))
    if paid_in <= 0:
        raise ValueError("paid-in capital must be positive")
    dpi, rvpi = dist / paid_in, nav / paid_in
    return {"paid_in": paid_in, "distributed": dist, "nav": nav,
            "dpi": dpi, "rvpi": rvpi, "tvpi": dpi + rvpi}


def net_flows(contributions: Sequence[float], distributions: Sequence[float],
              nav: float = 0.0) -> list[float]:
    """LP net cash-flow vector D_t - C_t, with residual NAV added to the last period
    (treated as if realizable at NAV: the convention behind an *interim* IRR)."""
    if len(contributions) != len(distributions):
        raise ValueError("vectors must have equal length")
    out = [d - c for c, d in zip(contributions, distributions)]
    out[-1] += nav
    return out


def ks_pme(contributions: Sequence[float], distributions: Sequence[float],
           index_levels: Sequence[float], nav: float = 0.0) -> float:
    """Kaplan-Schoar (2005) public market equivalent.

    KS-PME = [sum_t D_t / I_t + NAV_T / I_T] / [sum_t C_t / I_t].

    Dividing by the index level discounts each flow at the realized index return,
    so the ratio is the fund's multiple measured in "index units". KS-PME > 1 means
    the LP did better than investing the same calls in the index and withdrawing the
    same distributions. It is unchanged if every flow is instead compounded forward
    to T at the index return (multiply numerator and denominator by I_T).
    """
    if not (len(contributions) == len(distributions) == len(index_levels)):
        raise ValueError("vectors must have equal length")
    num = sum(d / i for d, i in zip(distributions, index_levels)) + nav / index_levels[-1]
    den = sum(c / i for c, i in zip(contributions, index_levels))
    return num / den


def pme_terminal_value(contributions: Sequence[float], distributions: Sequence[float],
                       index_levels: Sequence[float]) -> float:
    """Value at T of a mirror index account that receives each call and pays each
    distribution (Long-Nickels style). Negative means the mirror account was
    overdrawn, i.e. the fund distributed more than an index investment could fund."""
    bal = 0.0
    for t, (c, d) in enumerate(zip(contributions, distributions)):
        if t > 0:
            bal *= index_levels[t] / index_levels[t - 1]
        bal += c - d
    return bal


# --------------------------------------------------------------------------
# Power-law portfolios
# --------------------------------------------------------------------------

def _compositions(n: int, k: int):
    """All k-tuples of non-negative integers summing to n."""
    if k == 1:
        yield (n,)
        return
    for first in range(n + 1):
        for rest in _compositions(n - first, k - 1):
            yield (first,) + rest


def portfolio_multiple_distribution(multiples: Sequence[float], probs: Sequence[float],
                                    n: int) -> list[tuple[float, float]]:
    """Exact distribution of the equal-weighted portfolio multiple (mean of n i.i.d.
    deal multiples drawn from a discrete distribution), by multinomial enumeration.

    Returns sorted (portfolio_multiple, probability) pairs with duplicates merged.
    """
    if abs(sum(probs) - 1.0) > 1e-9:
        raise ValueError("probabilities must sum to 1")
    k = len(multiples)
    lgn = math.lgamma(n + 1)
    acc: dict[float, float] = {}
    for counts in _compositions(n, k):
        logp = lgn
        ok = True
        for c, p in zip(counts, probs):
            if c:
                if p == 0:
                    ok = False
                    break
                logp += c * math.log(p) - math.lgamma(c + 1)
        if not ok:
            continue
        m = round(sum(c * x for c, x in zip(counts, multiples)) / n, 12)
        acc[m] = acc.get(m, 0.0) + math.exp(logp)
    return sorted(acc.items())


def distribution_quantile(dist: Sequence[tuple[float, float]], q: float) -> float:
    """Smallest value x with P(X <= x) >= q for a sorted discrete distribution."""
    cum = 0.0
    for x, p in dist:
        cum += p
        if cum >= q - 1e-12:
            return x
    return dist[-1][0]


def distribution_mean(dist: Sequence[tuple[float, float]]) -> float:
    return sum(x * p for x, p in dist)


def prob_below(dist: Sequence[tuple[float, float]], threshold: float) -> float:
    """P(X < threshold)."""
    return sum(p for x, p in dist if x < threshold - 1e-12)


# --------------------------------------------------------------------------
# Auction costs
# --------------------------------------------------------------------------

def tiered_premium(hammer: float, tiers: Sequence[tuple[float, float]]) -> float:
    """Buyer's premium on a hammer price under a marginal (tiered) schedule.

    ``tiers`` is a list of (upper_bound, rate) with the last upper bound = inf.
    Each rate applies only to the slice of hammer price within its band, like
    marginal income-tax brackets.
    """
    prem, lower = 0.0, 0.0
    for upper, rate in tiers:
        if hammer <= lower:
            break
        prem += (min(hammer, upper) - lower) * rate
        lower = upper
    return prem


# --------------------------------------------------------------------------
# Repeat-sales index (Bailey-Muth-Nourse) for three periods
# --------------------------------------------------------------------------

def repeat_sales_3period(pairs: Sequence[tuple[int, int, float]]) -> dict:
    """OLS repeat-sales log index for periods 0, 1, 2 with beta_0 = 0.

    ``pairs``: (buy_period, sell_period, log_price_relative). The regression is
    y = beta_sell - beta_buy + e. Solved from the 2x2 normal equations.
    Returns log levels and index levels (base 100).
    """
    s11 = s22 = s12 = b1 = b2 = 0.0
    for buy, sell, y in pairs:
        x1 = (1 if sell == 1 else 0) - (1 if buy == 1 else 0)
        x2 = (1 if sell == 2 else 0) - (1 if buy == 2 else 0)
        s11 += x1 * x1
        s22 += x2 * x2
        s12 += x1 * x2
        b1 += x1 * y
        b2 += x2 * y
    det = s11 * s22 - s12 * s12
    if abs(det) < 1e-15:
        raise ValueError("pairs do not identify both period effects")
    beta1 = (b1 * s22 - b2 * s12) / det
    beta2 = (s11 * b2 - s12 * b1) / det
    return {"beta": [0.0, beta1, beta2],
            "index": [100.0, 100.0 * math.exp(beta1), 100.0 * math.exp(beta2)]}


# --------------------------------------------------------------------------
# Stale NAV and resale-only valuation
# --------------------------------------------------------------------------

def stale_nav_correction(stale_nav: float, beta: float, public_return_since_mark: float) -> float:
    """Best estimate of current value from a stale mark: NAV x (1 + beta x public move)."""
    return stale_nav * (1.0 + beta * public_return_since_mark)


def liquidity_adjusted_return(gross_annual: float, p_forced: float, haircut: float,
                              years: float) -> float:
    """Annual return after an expected forced-sale haircut spread over the hold:
    (1 + r)(1 - p x h)^(1/T) - 1. Uses the expected exit factor (risk-neutral in
    the haircut; it understates the cost to a holder who is forced in bad states)."""
    return (1.0 + gross_annual) * (1.0 - p_forced * haircut) ** (1.0 / years) - 1.0


def resale_only_value(resale_prices: Sequence[float], probs: Sequence[float],
                      required_return: float, years: float) -> float:
    """Value of a claim with no interim cash flow: E[P_T] / (1 + k)^T."""
    e = sum(p * x for p, x in zip(probs, resale_prices))
    return e / (1.0 + required_return) ** years


def required_price_path(p0: float, required_return: float, years: float) -> float:
    """Price a later buyer must pay for a no-cash-flow asset bought at p0 to earn k."""
    return p0 * (1.0 + required_return) ** years
