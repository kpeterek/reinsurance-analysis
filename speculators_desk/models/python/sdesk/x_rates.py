"""Rates-desk helpers used in Chapter 6 (Fixed Income and the Cost of Capital).

Extends ``sdesk.fixed_income`` without duplicating it. Conventions:

* Yields and rates are decimals (0.045 means 4.50%).
* Treasury note/bond yields are semiannual bond-equivalent yields (freq=2).
* Prices are per 100 face unless ``face`` is given. Pricing is on a coupon date
  (no accrued interest), as in ``fixed_income``.
* Treasury bills: the *discount rate* uses actual/360 and face value in the
  denominator; the *bond-equivalent yield* (investment rate) uses actual/365 and
  price in the denominator. This is the Treasury's published convention.
* Horizon (carry and roll-down) analysis keeps coupons uninvested and charges
  financing as simple interest, ``price x repo x horizon``. That is the desk
  approximation; it is stated in each docstring.
"""

from __future__ import annotations

import math
from typing import Sequence

from . import cre, fixed_income as fi


# --------------------------------------------------------------------------
# Treasury bills and quoting conventions
# --------------------------------------------------------------------------

def bill_price_from_discount(discount_rate: float, days: int, face: float = 100.0) -> float:
    """Price = face x (1 - d x days/360).  Excel: =face*(1-d*days/360)  (or =TBILLPRICE)."""
    return face * (1.0 - discount_rate * days / 360.0)


def bill_discount_from_price(price: float, days: int, face: float = 100.0) -> float:
    """Bank-discount rate d = (face - P)/face x 360/days."""
    return (face - price) / face * 360.0 / days


def bill_bey(price: float, days: int, face: float = 100.0) -> float:
    """Treasury bond-equivalent yield ("investment rate") of a bill.

    days <= 182: (face - P)/P x 365/days  (Excel: =TBILLEQ for the same case).
    days  > 182: the Treasury quadratic, which credits a hypothetical
    semiannual coupon reinvested at the same rate:
        BEY = [-2t + 2 sqrt(t^2 - (2t - 1)(1 - face/P))] / (2t - 1),  t = days/365.
    """
    if days <= 182:
        return (face - price) / price * 365.0 / days
    t = days / 365.0
    a = 2.0 * t - 1.0
    return (-2.0 * t + 2.0 * math.sqrt(t * t - a * (1.0 - face / price))) / a


def bill_money_market_yield(price: float, days: int, face: float = 100.0) -> float:
    """CD-equivalent yield: (face - P)/P x 360/days (comparable with SOFR/LIBOR-style quotes)."""
    return (face - price) / price * 360.0 / days


def bill_effective_annual(price: float, days: int, face: float = 100.0) -> float:
    """Effective annual yield with compounding over a 365-day year: (face/P)^(365/days) - 1."""
    return (face / price) ** (365.0 / days) - 1.0


def parse_32nds(quote: str) -> float:
    """Convert a Treasury price quote in 32nds to decimal.

    '99-16' -> 99.5; '99-16+' -> 99 + 16.5/32; '99-162' -> 99 + 16.25/32
    (the trailing digit is eighths of a 32nd, so 2 = 1/4, 4 = 1/2, 6 = 3/4).
    """
    handle, frac = quote.split("-")
    h = float(handle)
    if frac.endswith("+"):
        ticks = float(frac[:-1]) + 0.5
    elif len(frac) == 3:
        ticks = float(frac[:2]) + float(frac[2]) / 8.0
    else:
        ticks = float(frac)
    return h + ticks / 32.0


def tips_breakeven(nominal_yield: float, real_yield: float, exact: bool = True) -> float:
    """Breakeven inflation. Exact (Fisher): (1+n)/(1+r) - 1. Approximate: n - r.

    Breakeven inflation is NOT expected inflation: it also contains an inflation
    risk premium (positive) and a TIPS liquidity premium (which lowers it).
    """
    if exact:
        return (1.0 + nominal_yield) / (1.0 + real_yield) - 1.0
    return nominal_yield - real_yield


# --------------------------------------------------------------------------
# Horizon analysis: carry and roll-down
# --------------------------------------------------------------------------

def carry_rolldown(coupon_rate: float, years: float, y_now: float, y_rolled: float,
                   horizon: float, repo_rate: float = 0.0, freq: int = 2) -> dict:
    """Horizon P&L per 100 face of a financed (or unfinanced, repo=0) coupon bond.

    * ``y_now``: today's yield of the bond (maturity ``years``).
    * ``y_rolled``: today's yield at maturity ``years - horizon`` on the curve,
      i.e. the bond's yield at the horizon *if the curve does not move*.
    * Coupons received during the horizon are not reinvested.
    * Financing = price0 x repo x horizon (simple interest).

    Returns price0, coupon_income, financing, carry (= coupons - financing),
    pull_to_par (price change from ageing at an unchanged yield), rolldown
    (additional price change from the lower yield at the shorter maturity),
    total, dv01_h (DV01 per 100 of the bond at the horizon), and breakeven_bp:
    the parallel rise in yields at the horizon that wipes out the total.
    """
    n_h = horizon * freq
    if abs(n_h - round(n_h)) > 1e-9:
        raise ValueError("horizon must be a whole number of coupon periods")
    p0 = fi.bond_price(y_now, coupon_rate, years, freq=freq)
    rem = years - horizon
    p_same_y = fi.bond_price(y_now, coupon_rate, rem, freq=freq)
    p_rolled = fi.bond_price(y_rolled, coupon_rate, rem, freq=freq)
    coupons = 100.0 * coupon_rate * horizon
    financing = p0 * repo_rate * horizon
    carry = coupons - financing
    pull = p_same_y - p0
    roll = p_rolled - p_same_y
    total = carry + pull + roll
    dv01_h = fi.dv01(y_rolled, coupon_rate, rem, freq=freq)
    return {"price0": p0, "price_h_same_yield": p_same_y, "price_h_rolled": p_rolled,
            "coupon_income": coupons, "financing": financing, "carry": carry,
            "pull_to_par": pull, "rolldown": roll, "total": total,
            "dv01_h": dv01_h, "breakeven_bp": total / dv01_h}


# --------------------------------------------------------------------------
# Curve trades
# --------------------------------------------------------------------------

def curve_trade_pnl(legs: Sequence[dict], freq: int = 2) -> dict:
    """Full-revaluation P&L of a multi-leg Treasury position (instantaneous shock).

    Each leg: {"face": $ face, "coupon": c, "years": T, "y0": yield, "dy": change
    in yield (decimal), "side": +1 long / -1 short}. Returns per-leg P&L, total,
    and the position DV01 (dollars per bp; positive = gains when yields fall).
    """
    out = {"legs": [], "total": 0.0, "dv01": 0.0}
    for leg in legs:
        p0 = fi.bond_price(leg["y0"], leg["coupon"], leg["years"], freq=freq)
        p1 = fi.bond_price(leg["y0"] + leg["dy"], leg["coupon"], leg["years"], freq=freq)
        pnl = leg["side"] * (p1 - p0) / 100.0 * leg["face"]
        d = leg["side"] * fi.dv01(leg["y0"], leg["coupon"], leg["years"], freq=freq) / 100.0 * leg["face"]
        out["legs"].append(pnl)
        out["total"] += pnl
        out["dv01"] += d
    return out


# --------------------------------------------------------------------------
# Term structure and term premium
# --------------------------------------------------------------------------

def forward_rates_from_spots(spots: Sequence[float]) -> list[float]:
    """One-year forward rates f_{t-1,t} from annually compounded spot rates s_1..s_n."""
    out = [spots[0]]
    for t in range(2, len(spots) + 1):
        out.append(fi.forward_rate(spots[t - 2], t - 1, spots[t - 1], t))
    return out


def expectations_yield(expected_short_rates: Sequence[float]) -> float:
    """Yield on an n-year zero under the pure expectations hypothesis, given the
    expected one-year rates for years 1..n (annual compounding, convexity ignored)."""
    prod = 1.0
    for r in expected_short_rates:
        prod *= 1.0 + r
    return prod ** (1.0 / len(expected_short_rates)) - 1.0


def term_premium(yield_n: float, expected_short_rates: Sequence[float]) -> float:
    """Model-dependent term premium: observed n-year zero yield minus the
    expectations-hypothesis yield implied by a *chosen* expected short-rate path."""
    return yield_n - expectations_yield(expected_short_rates)


# --------------------------------------------------------------------------
# Credit spreads
# --------------------------------------------------------------------------

def credit_triangle_hazard(spread: float, recovery: float) -> float:
    """Risk-neutral default intensity from the credit triangle: lambda = s / (1 - R).
    This contains the default risk premium; it is not a real-world default rate."""
    return spread / (1.0 - recovery)


# --------------------------------------------------------------------------
# Cap rates versus Treasury yields
# --------------------------------------------------------------------------

def cap_spread_decomposition(cap_rate: float, treasury_yield: float, noi_growth: float) -> dict:
    """Gordon decomposition c = r_f + RP - g, so spread = c - r_f = RP - g.

    Returns the spread and the implied property risk premium RP = c + g - r_f.
    Valid for NOI after reserves growing at a constant expected rate g.
    """
    spread = cap_rate - treasury_yield
    return {"spread": spread, "risk_premium": cap_rate + noi_growth - treasury_yield,
            "required_return": cap_rate + noi_growth}


def implied_cap_rate(treasury_yield: float, risk_premium: float, noi_growth: float) -> float:
    """c = r_f + RP - g (constant-growth perpetuity)."""
    return cre.gordon_cap_rate(treasury_yield + risk_premium, noi_growth)


# --------------------------------------------------------------------------
# Interest-rate sensitivity of levered CRE equity
# --------------------------------------------------------------------------

def levered_rate_shock(noi: float, cap0: float, debt: float, dy: float,
                       passthrough: float = 1.0, noi_change: float = 0.0,
                       debt_mod_duration: float = 0.0) -> dict:
    """Instantaneous effect of a Treasury-yield change ``dy`` on a levered property.

    Cap rate after the shock: c1 = c0 + passthrough x dy. NOI may change by
    ``noi_change`` (decimal). Value V = NOI / c.

    * Book equity = V - debt at par (what a refinancing or sale sees).
    * Economic equity = V - market value of fixed-rate debt, with the debt
      repriced by ``debt_mod_duration`` (first order). Floating-rate debt: 0.

    Effective durations are -(dX/X)/dy, finite-difference (dy must be non-zero).
    """
    v0 = noi / cap0
    cap1 = cap0 + passthrough * dy
    noi1 = noi * (1.0 + noi_change)
    v1 = noi1 / cap1
    e0 = v0 - debt
    e1_book = v1 - debt
    debt_mv1 = debt * (1.0 - debt_mod_duration * dy)
    e1_econ = v1 - debt_mv1
    return {"v0": v0, "cap1": cap1, "v1": v1, "property_pct": v1 / v0 - 1.0,
            "equity0": e0, "equity1_book": e1_book, "equity_pct_book": e1_book / e0 - 1.0,
            "equity1_econ": e1_econ, "equity_pct_econ": e1_econ / e0 - 1.0,
            "property_eff_duration": -(v1 / v0 - 1.0) / dy,
            "equity_eff_duration_book": -(e1_book / e0 - 1.0) / dy,
            "equity_eff_duration_econ": -(e1_econ / e0 - 1.0) / dy}


def property_duration_first_order(cap_rate: float, passthrough: float = 1.0) -> float:
    """First-order effective duration of an unlevered property to Treasury yields,
    NOI held fixed: D_V = passthrough / c  (from V = NOI/c, dV/V = -dc/c)."""
    return passthrough / cap_rate


def equity_duration_first_order(property_duration: float, ltv: float,
                                debt_mod_duration: float = 0.0) -> float:
    """D_E = (D_V - LTV x D_debt) / (1 - LTV): balance-sheet duration identity."""
    return (property_duration - ltv * debt_mod_duration) / (1.0 - ltv)
