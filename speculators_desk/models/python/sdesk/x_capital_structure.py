"""Capital-structure helpers for Chapter 10 and Case B (new module; does not modify cre/tvm).

Conventions follow the notation guide: rates are decimals, money in dollars,
payments monthly in arrears for mortgages, annual periods for waterfalls.

Functions
---------
* io_then_amort_balance  -- balloon on a loan with an interest-only period
* bachelier_caplet / cap_premium -- interest-rate cap cost under the normal
  (Bachelier) model, the market convention for USD caps since rates neared zero
* tranche_losses -- loss allocation across an ordered capital stack
* catchup_waterfall_terminal -- pref + GP catch-up + carry on a single terminal
  distribution (whole-of-deal, "European" style)
* capital_call_dilution -- ownership after a capital call that one partner skips
* lender_pv -- present value of a lender's recovery path
"""

from __future__ import annotations

import math
from typing import Sequence

from . import markets, tvm


# --------------------------------------------------------------------------
# Loans
# --------------------------------------------------------------------------

def io_then_amort_balance(principal: float, annual_rate: float, amort_years: float,
                          io_months: int, term_months: int) -> float:
    """Balance at the end of ``term_months`` for a loan that is interest-only for
    ``io_months`` and then amortizes on an ``amort_years`` schedule.

    During IO the balance is unchanged. Amortization then runs for
    ``term_months - io_months`` payments on the original principal.
    Excel: =-FV(r/12, term-io, PMT(r/12, amort*12, -L), L)
    """
    k = max(term_months - io_months, 0)
    if k == 0:
        return principal
    return tvm.loan_balance(principal, annual_rate, amort_years, k)


# --------------------------------------------------------------------------
# Interest-rate caps (normal model)
# --------------------------------------------------------------------------

def bachelier_caplet(forward: float, strike: float, normal_vol: float, t_expiry: float,
                     accrual: float, discount_factor: float, notional: float = 1.0) -> float:
    """Caplet value under the Bachelier (normal) model.

    caplet = N * tau * DF * [(F - K) Phi(d) + sigma_N sqrt(T) phi(d)],  d = (F-K)/(sigma_N sqrt T)

    ``forward`` and ``strike`` are decimal rates; ``normal_vol`` is the annual
    normal volatility in decimal (0.01 = 100 bp). ``t_expiry`` is the fixing time
    in years, ``accrual`` the period length (0.25 quarterly), ``discount_factor``
    to the payment date. At t_expiry = 0 the caplet is its intrinsic value.
    """
    intrinsic = max(forward - strike, 0.0)
    if t_expiry <= 0 or normal_vol <= 0:
        return notional * accrual * discount_factor * intrinsic
    s = normal_vol * math.sqrt(t_expiry)
    d = (forward - strike) / s
    return notional * accrual * discount_factor * ((forward - strike) * markets.norm_cdf(d)
                                                   + s * markets.norm_pdf(d))


def cap_premium(notional: float, strike: float, forward: float, normal_vol: float,
                years: float, freq: int = 4, skip_first: bool = True) -> dict:
    """Upfront premium of a cap with a flat forward curve.

    Discounting uses the same flat forward compounded ``freq`` times a year.
    Caplet j covers (t_{j-1}, t_j], fixes at t_{j-1}, pays at t_j. When
    ``skip_first`` the first period (already fixed at trade date) is excluded, as
    is standard for spot-starting caps.
    """
    n = int(round(years * freq))
    tau = 1.0 / freq
    total = 0.0
    annuity = 0.0
    caplets = []
    for j in range(1, n + 1):
        t_fix = (j - 1) * tau
        df = (1.0 + forward * tau) ** (-j)
        annuity += tau * df
        if skip_first and j == 1:
            continue
        c = bachelier_caplet(forward, strike, normal_vol, t_fix, tau, df, notional)
        caplets.append(c)
        total += c
    return {"premium": total, "pct_notional": total / notional,
            "annual_bp_equivalent": total / notional / annuity * 1e4, "annuity": annuity,
            "caplets": caplets}


# --------------------------------------------------------------------------
# Capital stack
# --------------------------------------------------------------------------

def tranche_losses(original_value: float, new_value: float,
                   tranches: Sequence[tuple[str, float]]) -> list[dict]:
    """Allocate a value decline across tranches ordered senior -> junior.

    ``tranches`` = [(name, amount), ...] senior first, summing to original value
    (the last tranche is common equity). Losses hit the most junior tranche first.
    Returns attachment and detachment points (as fractions of original value),
    the dollar loss and the fractional loss of each tranche.
    """
    total = sum(a for _, a in tranches)
    if abs(total - original_value) > 1e-6 * original_value:
        raise ValueError("tranches must sum to the original value")
    loss = max(original_value - new_value, 0.0)
    out = []
    attach = 0.0
    for name, amt in tranches:
        out.append({"name": name, "amount": amt, "attach": attach / original_value,
                    "detach": (attach + amt) / original_value})
        attach += amt
    remaining = loss
    for row in reversed(out):
        hit = min(remaining, row["amount"])
        row["loss"] = hit
        row["loss_pct"] = hit / row["amount"] if row["amount"] else 0.0
        remaining -= hit
    return out


# --------------------------------------------------------------------------
# Waterfalls
# --------------------------------------------------------------------------

def catchup_waterfall_terminal(contributed: float, distributed: float, pref_rate: float,
                               years: float, carry: float, catchup_to_gp: float = 1.0) -> dict:
    """Single contribution at t=0, single distribution at t=years.

    Tiers: (1) return of capital; (2) compounding pref at ``pref_rate``;
    (3) catch-up: ``catchup_to_gp`` share of each dollar to the GP until the GP
    holds ``carry`` of total profit; (4) split (1-carry)/carry.
    Returns investor and GP (promote) dollars and investor multiple.
    """
    profit = distributed - contributed
    pref = contributed * ((1 + pref_rate) ** years - 1)
    to_inv = min(distributed, contributed)
    rem = distributed - to_inv
    p = min(rem, pref)
    to_inv += p
    rem -= p
    gp = 0.0
    if rem > 0:
        # catch-up: GP gets c per dollar until gp = carry * (pref + gp_catchup_total ... )
        # target: gp = carry * (p + x) where x dollars flow through catch-up
        # gp = c x  =>  c x = carry (p + x)  =>  x = carry p / (c - carry)
        c = catchup_to_gp
        x_needed = carry * p / (c - carry) if c > carry else float("inf")
        x = min(rem, x_needed)
        gp += c * x
        to_inv += (1 - c) * x
        rem -= x
    if rem > 0:
        gp += carry * rem
        to_inv += (1 - carry) * rem
    return {"profit": profit, "pref_amount": pref, "investor": to_inv, "gp": gp,
            "gp_share_of_profit": gp / profit if profit > 0 else 0.0,
            "investor_irr": (to_inv / contributed) ** (1 / years) - 1 if to_inv > 0 else -1.0}


def capital_call_dilution(units_a: float, units_b: float, value_pre: float, call: float,
                          a_share_of_call: float, a_funds: bool, b_funds: bool,
                          penalty_multiple: float = 1.0) -> dict:
    """Ownership after a capital call.

    Pre-call equity value ``value_pre`` (may be well below contributed capital).
    Each partner is asked for its pro-rata share of ``call``. A partner that funds
    receives new units at the pre-money value per unit, multiplied by
    ``penalty_multiple`` when it also funds the defaulting partner's share
    (a "punitive dilution" credit, e.g. 1.5 = 150% credit).
    """
    units = units_a + units_b
    price = value_pre / units if units else 0.0
    a_call, b_call = call * a_share_of_call, call * (1 - a_share_of_call)
    new_a = new_b = 0.0
    if a_funds:
        new_a += a_call / price
    if b_funds:
        new_b += b_call / price
    if a_funds and not b_funds:
        new_a += b_call * penalty_multiple / price
    if b_funds and not a_funds:
        new_b += a_call * penalty_multiple / price
    ua, ub = units_a + new_a, units_b + new_b
    return {"price_per_unit": price, "units_a": ua, "units_b": ub,
            "share_a": ua / (ua + ub), "share_b": ub / (ua + ub)}


# --------------------------------------------------------------------------
# Lender view
# --------------------------------------------------------------------------

def lender_pv(cashflows: Sequence[float], rate: float) -> float:
    """PV of a lender's recovery cash flows (annual, t=0 first, not discounted)."""
    return tvm.npv(rate, cashflows)
