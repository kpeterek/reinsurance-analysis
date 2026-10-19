"""Bond pricing and interest-rate risk.

All yields are decimals with the stated compounding frequency (U.S. Treasuries:
semiannual, freq=2). Prices are per 100 face unless ``face`` is given.
Pricing is on a coupon date (no accrued interest) unless stated otherwise.
"""

from __future__ import annotations


def bond_cashflows(face: float, coupon_rate: float, years: float, freq: int = 2) -> list[tuple[float, float]]:
    """List of (time in years, cash flow)."""
    n = int(round(years * freq))
    c = face * coupon_rate / freq
    return [((k / freq), c + (face if k == n else 0.0)) for k in range(1, n + 1)]


def bond_price(ytm: float, coupon_rate: float, years: float, face: float = 100.0, freq: int = 2) -> float:
    """Price = sum CF_k / (1 + y/f)^k.   Excel: =PRICE(...) or =PV(y/f, n, -c, -face)"""
    y = ytm / freq
    return sum(cf / (1 + y) ** (t * freq) for t, cf in bond_cashflows(face, coupon_rate, years, freq))


def macaulay_duration(ytm: float, coupon_rate: float, years: float, freq: int = 2) -> float:
    """PV-weighted average time to cash flow, in years."""
    y = ytm / freq
    flows = bond_cashflows(100.0, coupon_rate, years, freq)
    p = sum(cf / (1 + y) ** (t * freq) for t, cf in flows)
    return sum(t * cf / (1 + y) ** (t * freq) for t, cf in flows) / p


def modified_duration(ytm: float, coupon_rate: float, years: float, freq: int = 2) -> float:
    """D_mod = D_mac / (1 + y/f).  -dP/P per unit change in yield (decimal)."""
    return macaulay_duration(ytm, coupon_rate, years, freq) / (1 + ytm / freq)


def convexity(ytm: float, coupon_rate: float, years: float, freq: int = 2) -> float:
    """Annualized convexity: (1/P) d2P/dy2, in years^2."""
    y = ytm / freq
    flows = bond_cashflows(100.0, coupon_rate, years, freq)
    p = sum(cf / (1 + y) ** (t * freq) for t, cf in flows)
    s = sum(cf * (t * freq) * (t * freq + 1) / (1 + y) ** (t * freq + 2) for t, cf in flows)
    return s / (p * freq ** 2)


def dv01(ytm: float, coupon_rate: float, years: float, face: float = 100.0, freq: int = 2) -> float:
    """Dollar value of one basis point (positive number), via central difference."""
    h = 0.0001
    up = bond_price(ytm + h, coupon_rate, years, face, freq)
    dn = bond_price(ytm - h, coupon_rate, years, face, freq)
    return (dn - up) / 2.0


def price_change_approx(price: float, mod_duration: float, convex: float, dy: float) -> dict:
    """Second-order approximation: dP ~= P(-D dy + 0.5 C dy^2). dy in decimals."""
    first = -mod_duration * dy * price
    second = 0.5 * convex * dy ** 2 * price
    return {"duration_term": first, "convexity_term": second, "total": first + second}


def zero_price(rate: float, t: float, freq: int = 1) -> float:
    """Discount factor for a zero-coupon bond paying 1 at t."""
    return 1.0 / (1 + rate / freq) ** (t * freq)


def forward_rate(r1: float, t1: float, r2: float, t2: float) -> float:
    """Annually compounded forward rate between t1 and t2 implied by spot rates."""
    return ((1 + r2) ** t2 / (1 + r1) ** t1) ** (1 / (t2 - t1)) - 1


def hedge_ratio_dv01(dv01_exposure: float, dv01_hedge_per_unit: float) -> float:
    """Units of hedge instrument to neutralize a DV01 exposure."""
    return dv01_exposure / dv01_hedge_per_unit


def bond_equivalent_to_annual(y_bey: float) -> float:
    """Convert a semiannual bond-equivalent yield to an annual effective yield."""
    return (1 + y_bey / 2) ** 2 - 1
