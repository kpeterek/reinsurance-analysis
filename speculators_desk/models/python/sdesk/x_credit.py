"""Credit and financial-distress helpers for Chapter 17 (new module; does not modify other modules).

Conventions follow the notation guide: rates and probabilities are decimals,
money in dollars (or "per 100 of face" where stated), time in years.

Functions
---------
Default probabilities
* hazard_from_cum_pd / cum_pd_from_hazard -- constant-hazard conversions
* annual_pd_from_hazard -- one-year PD implied by a constant hazard
* forward_hazard -- average hazard between two horizons from two cumulative PDs
* conditional_pd -- probability of default in (t1, t2] given survival to t1
* triangle_spread / triangle_hazard -- the credit triangle s = lambda * LGD

Spreads
* bond_ytm -- yield to maturity of a level-coupon bond (bisection on fixed_income.bond_price)
* spread_decomposition -- expected loss, liquidity, and residual risk premium

Capital structure and bankruptcy
* apr_waterfall -- absolute-priority distribution across ordered (possibly pari passu) classes
* holdco_opco -- structural subordination of holding-company creditors

Credit derivatives
* cds_flat -- protection leg, risky annuity (RPV01), par spread and upfront under a flat hazard

Structured credit
* tranche_loss -- loss to a tranche [attach, detach] for a pool loss (all as fractions of pool)
* tranche_table -- loss allocation across a whole CMBS stack
* credit_enhancement_after_paydown -- subordination after sequential principal paydown

Structural (Merton) model
* merton -- equity as a call on asset value; risky debt value, yield, spread, risk-neutral PD
"""

from __future__ import annotations

import math
from typing import Sequence

from . import fixed_income, markets


# --------------------------------------------------------------------------
# Default probabilities and hazard rates
# --------------------------------------------------------------------------

def hazard_from_cum_pd(cum_pd: float, t: float) -> float:
    """Constant hazard lambda (per year, continuous) with survival exp(-lambda t) = 1 - cum_pd."""
    if not 0 <= cum_pd < 1:
        raise ValueError("cumulative PD must be in [0, 1)")
    return -math.log(1.0 - cum_pd) / t


def cum_pd_from_hazard(hazard: float, t: float) -> float:
    """Cumulative default probability to horizon t under a constant hazard: 1 - exp(-lambda t)."""
    return 1.0 - math.exp(-hazard * t)


def annual_pd_from_hazard(hazard: float) -> float:
    """One-year default probability implied by a constant hazard (not equal to lambda)."""
    return cum_pd_from_hazard(hazard, 1.0)


def forward_hazard(cum_pd_1: float, t1: float, cum_pd_2: float, t2: float) -> float:
    """Average hazard over (t1, t2]: [ln S(t1) - ln S(t2)] / (t2 - t1), S = 1 - cum PD."""
    return (math.log(1 - cum_pd_1) - math.log(1 - cum_pd_2)) / (t2 - t1)


def conditional_pd(cum_pd_1: float, cum_pd_2: float) -> float:
    """P(default in (t1, t2] | survived to t1) = (PD2 - PD1) / (1 - PD1)."""
    return (cum_pd_2 - cum_pd_1) / (1 - cum_pd_1)


def triangle_spread(hazard: float, recovery: float) -> float:
    """Credit triangle: spread = lambda * (1 - R). Exact for a continuously paid premium,
    flat hazard, recovery of par paid at default; an approximation otherwise."""
    return hazard * (1.0 - recovery)


def triangle_hazard(spread: float, recovery: float) -> float:
    """Inverse credit triangle: lambda = s / (1 - R). Risk-neutral, not a real-world default rate."""
    return spread / (1.0 - recovery)


# --------------------------------------------------------------------------
# Bond yields and spread decomposition
# --------------------------------------------------------------------------

def bond_ytm(price: float, coupon_rate: float, years: float, freq: int = 2,
             face: float = 100.0) -> float:
    """Yield to maturity (bond-equivalent, compounded ``freq`` times a year) of a level-coupon bond.

    Excel equivalent: =YIELD(settle, maturity, coupon, price, 100, freq) on a coupon date.
    """
    lo, hi = -0.5, 2.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if fixed_income.bond_price(mid, coupon_rate, years, face, freq) > price:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def spread_decomposition(spread: float, real_world_pd: float, recovery: float,
                         liquidity: float) -> dict:
    """Split a credit spread (decimal per year) into expected loss, liquidity and a residual.

    expected_loss = PD * (1 - R) per year (real-world PD, annual).
    risk_premium = spread - expected_loss - liquidity (the residual: default-risk premium
    plus anything not modeled, such as taxes or optionality).
    Also returns the risk-neutral hazard implied by the spread net of liquidity and the
    ratio of that hazard to the real-world annual PD.
    """
    el = real_world_pd * (1 - recovery)
    rp = spread - el - liquidity
    q = (spread - liquidity) / (1 - recovery)
    return {"expected_loss": el, "liquidity": liquidity, "risk_premium": rp,
            "rn_hazard": q, "rn_to_physical": q / real_world_pd if real_world_pd else math.inf}


# --------------------------------------------------------------------------
# Absolute priority and structural subordination
# --------------------------------------------------------------------------

def apr_waterfall(value: float, classes: Sequence) -> dict:
    """Distribute ``value`` by absolute priority.

    ``classes`` is ordered senior -> junior. Each element is either (name, claim) or a
    list of (name, claim) tuples that rank pari passu (shared pro rata by claim).
    Returns {"rows": [{name, claim, paid, recovery}], "residual": value left for equity,
    "fulcrum": name(s) of the most senior class not paid in full (None if all paid)}.
    The residual goes to the old equity only if every class is paid in full.
    """
    remaining = max(value, 0.0)
    rows = []
    fulcrum = None
    for group in classes:
        members = group if isinstance(group, list) else [group]
        total = sum(c for _, c in members)
        pay = min(remaining, total)
        frac = pay / total if total else 1.0
        for name, claim in members:
            rows.append({"name": name, "claim": claim, "paid": claim * frac, "recovery": frac})
        if frac < 1.0 - 1e-12 and fulcrum is None:
            fulcrum = [n for n, _ in members] if len(members) > 1 else members[0][0]
        remaining -= pay
    return {"rows": rows, "residual": remaining, "fulcrum": fulcrum,
            "by_name": {r["name"]: r for r in rows}}


def holdco_opco(opco_value: float, opco_classes: Sequence, holdco_classes: Sequence,
                holdco_other_assets: float = 0.0) -> dict:
    """Structural subordination: holdco creditors are paid only from opco's residual equity
    (plus any other holdco assets). Returns both waterfalls."""
    op = apr_waterfall(opco_value, opco_classes)
    hold_value = op["residual"] + holdco_other_assets
    hc = apr_waterfall(hold_value, holdco_classes)
    return {"opco": op, "holdco_value": hold_value, "holdco": hc}


# --------------------------------------------------------------------------
# Credit default swaps
# --------------------------------------------------------------------------

def cds_flat(hazard: float, recovery: float, r: float, maturity: float,
             coupon: float | None = None, freq: int = 4) -> dict:
    """Simplified CDS valuation with a flat hazard and a flat continuously compounded rate.

    Protection leg (per 1 notional): (1-R) * lambda/(r+lambda) * (1 - exp(-(r+lambda) T)),
    i.e. loss paid at the moment of default.
    Risky annuity RPV01: sum over payment dates t_i = i/freq of (1/freq) * exp(-(r+lambda) t_i)
    (premium paid in arrears; accrued premium on default ignored, which makes the par
    spread slightly higher than lambda*(1-R)).
    Par spread = protection / RPV01. Upfront paid by the protection buyer for a running
    coupon c: (par - c) * RPV01 = protection - c * RPV01 (fraction of notional).
    """
    k = r + hazard
    prot = (1 - recovery) * hazard / k * (1 - math.exp(-k * maturity))
    n = int(round(maturity * freq))
    rpv01 = sum((1 / freq) * math.exp(-k * i / freq) for i in range(1, n + 1))
    par = prot / rpv01
    out = {"protection": prot, "rpv01": rpv01, "par_spread": par}
    if coupon is not None:
        out["upfront"] = prot - coupon * rpv01
    return out


def cds_upfront_triangle(spread: float, coupon: float, recovery: float, r: float,
                         maturity: float, freq: int = 4) -> dict:
    """Upfront for a quoted (par) spread using the credit-triangle hazard lambda = s/(1-R)
    to build the risky annuity: upfront = (s - c) * RPV01(lambda).

    This is the desk approximation of the ISDA standard model (which calibrates a flat
    hazard and includes accrued-on-default). Positive upfront = paid by the protection buyer.
    """
    lam = triangle_hazard(spread, recovery)
    k = r + lam
    n = int(round(maturity * freq))
    rpv01 = sum((1 / freq) * math.exp(-k * i / freq) for i in range(1, n + 1))
    return {"hazard": lam, "rpv01": rpv01, "upfront": (spread - coupon) * rpv01}


# --------------------------------------------------------------------------
# Structured credit (CMBS tranches)
# --------------------------------------------------------------------------

def tranche_loss(pool_loss: float, attach: float, detach: float) -> float:
    """Fractional loss of a tranche [attach, detach] for a pool loss L (all fractions of pool).

    loss = min(max(L - a, 0), d - a) / (d - a).
    """
    if detach <= attach:
        raise ValueError("detach must exceed attach")
    return min(max(pool_loss - attach, 0.0), detach - attach) / (detach - attach)


def tranche_table(pool_balance: float, pool_loss: float,
                  stack: Sequence[tuple[str, float, float]]) -> list[dict]:
    """Loss allocation across a stack [(name, attach, detach), ...] for pool loss L (fraction)."""
    out = []
    for name, a, d in stack:
        f = tranche_loss(pool_loss, a, d)
        size = (d - a) * pool_balance
        out.append({"name": name, "attach": a, "detach": d, "size": size,
                    "loss_pct": f, "loss": f * size})
    return out


def credit_enhancement_after_paydown(subordinate_balance: float, pool_balance_now: float) -> float:
    """Credit enhancement (subordination) of a class = balance of all classes junior to it
    divided by the current pool balance. Sequential pay to seniors raises it."""
    return subordinate_balance / pool_balance_now


# --------------------------------------------------------------------------
# Merton structural model
# --------------------------------------------------------------------------

def merton(v: float, face: float, t: float, r: float, sigma: float, q: float = 0.0) -> dict:
    """Equity = European call on asset value V struck at the face of zero-coupon debt.

    r is continuously compounded; q is a continuous payout yield on the asset.
    Debt = V e^{-qT} - E. Debt yield y = ln(face/D)/T (continuous); spread = y - r.
    Risk-neutral PD = N(-d2). Distance to default (risk-neutral drift) = d2.
    """
    e = markets.bs_price(v, face, t, r, sigma, "call", q)
    d = v * math.exp(-q * t) - e
    y = math.log(face / d) / t
    d1 = (math.log(v / face) + (r - q + 0.5 * sigma ** 2) * t) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)
    return {"equity": e, "debt": d, "debt_yield": y, "spread": y - r,
            "rn_pd": markets.norm_cdf(-d2), "d1": d1, "d2": d2,
            "delta": math.exp(-q * t) * markets.norm_cdf(d1),
            "intrinsic": max(v - face, 0.0)}
