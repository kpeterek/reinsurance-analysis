"""Equities and equity index futures (Chapter 14).

Conventions
-----------
* Rates and yields in decimals. Money in dollars. Time in years.
* Index futures: notional = F x multiplier x contracts. CME E-mini S&P 500
  multiplier = $50 per index point; Micro E-mini = $5 (Chapter 14, ch14-S01/S02).
* Beta hedge: N = beta x V / (F x multiplier). A positive N is the number of
  contracts to SELL to remove the beta exposure of a long position.
* Cost of carry in ``futures_fair_value_simple`` uses simple interest and a
  dividend amount: F = S(1 + r t) - D. ``sdesk.markets.futures_fair_value``
  is the continuous-compounding version.
* Betas: debt beta is assumed zero unless given. Asset beta =
  equity beta x E/(D+E) + debt beta x D/(D+E).
"""

from __future__ import annotations

import math
from typing import Sequence


# --------------------------------------------------------------------------
# Earnings and multiples
# --------------------------------------------------------------------------

def income_bridge(ebitda: float, da: float, interest: float, tax_rate: float, shares: float) -> dict:
    """EBITDA -> EBIT -> EBT -> net income -> EPS (tax on positive EBT only)."""
    ebit = ebitda - da
    ebt = ebit - interest
    tax = max(ebt, 0.0) * tax_rate
    ni = ebt - tax
    return {"ebit": ebit, "ebt": ebt, "tax": tax, "net_income": ni, "eps": ni / shares}


def enterprise_value(market_cap: float, debt: float, cash: float, preferred: float = 0.0,
                     minority: float = 0.0) -> float:
    """EV = equity market value + debt + preferred + minority interest - cash."""
    return market_cap + debt + preferred + minority - cash


def implied_cap_from_ev(ebitda: float, maintenance_capex: float, ev: float) -> float:
    """Cap-rate equivalent of a listed company: (EBITDA - maintenance capex) / EV.

    For a hotel company, maintenance capex is the FF&E reserve, so the numerator
    is NOI after reserve in the sense of the notation guide.
    """
    return (ebitda - maintenance_capex) / ev


def implied_cap_from_multiple(ev_ebitda: float, ebitda_margin: float, reserve_pct_revenue: float) -> float:
    """(1/multiple) x (1 - reserve/margin): the cap rate implied by an EV/EBITDA multiple."""
    return (1.0 / ev_ebitda) * (1.0 - reserve_pct_revenue / ebitda_margin)


# --------------------------------------------------------------------------
# Implied equity returns and risk premiums
# --------------------------------------------------------------------------

def gordon_implied_return(cash_yield_next: float, growth: float) -> float:
    """k = D1/P + g (constant-growth model; D1 = next-year cash distributions)."""
    return cash_yield_next + growth


def two_stage_pv(k: float, cf1: float, g1: float, n: int, g2: float) -> float:
    """PV of CF_t = cf1 (1+g1)^(t-1), t = 1..n, plus a Gordon terminal value at n
    on CF_{n+1} = CF_n (1+g2). Requires k > g2."""
    if k <= g2:
        raise ValueError("k must exceed terminal growth")
    pv = 0.0
    cf = cf1
    for t in range(1, n + 1):
        pv += cf / (1 + k) ** t
        if t < n:
            cf *= 1 + g1
    tv = cf * (1 + g2) / (k - g2)
    return pv + tv / (1 + k) ** n


def two_stage_implied_return(price: float, cf1: float, g1: float, n: int, g2: float,
                             lo: float | None = None, hi: float = 1.0, tol: float = 1e-12) -> float:
    """Solve two_stage_pv(k) = price for k by bisection (PV is decreasing in k)."""
    lo = g2 + 1e-9 if lo is None else lo
    if two_stage_pv(hi, cf1, g1, n, g2) > price:
        raise ValueError("no root below hi")
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if two_stage_pv(mid, cf1, g1, n, g2) > price:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return 0.5 * (lo + hi)


def earnings_yield_gap(pe: float, real_yield: float) -> float:
    """E/P minus the real (TIPS) yield. A crude real ERP proxy; see Chapter 14 caveats."""
    return 1.0 / pe - real_yield


# --------------------------------------------------------------------------
# Index futures
# --------------------------------------------------------------------------

def futures_fair_value_simple(spot: float, r: float, t: float, dividends_points: float) -> float:
    """F = S (1 + r t) - D, simple interest, D = dividends (index points) paid before expiry,
    ignoring interest on dividends."""
    return spot * (1 + r * t) - dividends_points


def no_arbitrage_band(fair: float, cost_points: float) -> tuple[float, float]:
    """(lower, upper) futures prices inside which neither cash-and-carry nor reverse
    cash-and-carry earns money after round-trip costs of ``cost_points``."""
    return fair - cost_points, fair + cost_points


def beta_hedge_contracts(beta: float, value: float, futures_price: float, multiplier: float) -> float:
    """N = beta x V / (F x multiplier). Unrounded; sell N to hedge a long."""
    return beta * value / (futures_price * multiplier)


def margin_call_points(initial_margin: float, maintenance_margin: float, multiplier: float) -> float:
    """Adverse index-point move per contract that exhausts IM - MM and triggers a call."""
    return (initial_margin - maintenance_margin) / multiplier


# --------------------------------------------------------------------------
# Leverage, shorting, beta algebra
# --------------------------------------------------------------------------

def long_margin_call_price(p0: float, initial_margin: float, maintenance: float) -> float:
    """Price at which a long bought on margin hits maintenance.

    Loan = (1 - m0) P0 per share; equity/value = 1 - loan/P = mm  =>  P* = (1-m0)P0/(1-mm).
    """
    return (1 - initial_margin) * p0 / (1 - maintenance)


def short_margin_call_price(p0: float, initial_margin: float, maintenance: float) -> float:
    """Price at which a short hits maintenance.

    Collateral = (1 + m0) P0 per share (proceeds plus margin). Equity = (1+m0)P0 - P.
    Call when equity < mm x P  =>  P* = (1 + m0) P0 / (1 + mm).
    """
    return (1 + initial_margin) * p0 / (1 + maintenance)


def unlever_beta(equity_beta: float, debt_to_value: float, debt_beta: float = 0.0) -> float:
    """Asset beta = beta_E (1 - D/V) + beta_D D/V."""
    return equity_beta * (1 - debt_to_value) + debt_beta * debt_to_value


def relever_beta(asset_beta: float, debt_to_value: float, debt_beta: float = 0.0) -> float:
    """Equity beta = (beta_A - beta_D D/V) / (1 - D/V)."""
    return (asset_beta - debt_beta * debt_to_value) / (1 - debt_to_value)


def hedged_volatility(beta: float, sigma_m: float, sigma_resid: float, hedge_beta: float) -> dict:
    """Vol before and after selling ``hedge_beta`` of market exposure.

    r = beta r_m + e;  hedged r = (beta - hedge_beta) r_m + e.
    """
    unhedged = math.sqrt((beta * sigma_m) ** 2 + sigma_resid ** 2)
    hedged = math.sqrt(((beta - hedge_beta) * sigma_m) ** 2 + sigma_resid ** 2)
    rho = beta * sigma_m / unhedged
    return {"unhedged": unhedged, "hedged": hedged, "rho": rho,
            "variance_reduction": 1 - hedged ** 2 / unhedged ** 2}


# --------------------------------------------------------------------------
# Breadth
# --------------------------------------------------------------------------

def breadth(caps: Sequence[float], returns: Sequence[float]) -> dict:
    """Cap-weighted and equal-weighted returns, advancers/decliners, contributions."""
    total = sum(caps)
    contrib = [c * r / total for c, r in zip(caps, returns)]
    return {"cap_weighted": sum(contrib), "equal_weighted": sum(returns) / len(returns),
            "advancers": sum(1 for r in returns if r > 0),
            "decliners": sum(1 for r in returns if r < 0),
            "contributions": contrib}
