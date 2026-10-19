"""Commercial real estate valuation, financing, and capital-structure mathematics."""

from __future__ import annotations

from typing import Sequence

from . import tvm


# --------------------------------------------------------------------------
# Valuation
# --------------------------------------------------------------------------

def direct_cap_value(noi: float, cap_rate: float) -> float:
    """V = NOI / cap rate. Excel: =NOI/cap"""
    if cap_rate <= 0:
        raise ValueError("cap rate must be positive")
    return noi / cap_rate


def implied_cap_rate(noi: float, value: float) -> float:
    """Cap rate implied by a price: NOI / V."""
    return noi / value


def gordon_cap_rate(discount_rate: float, noi_growth: float) -> float:
    """Cap rate consistent with a constant-growth perpetuity: k - g.

    Valid only when NOI grows at a constant rate forever and k > g; capex must be
    netted out of NOI (i.e., use NOI after reserves).
    """
    if discount_rate <= noi_growth:
        raise ValueError("discount rate must exceed growth")
    return discount_rate - noi_growth


def value_change_from_cap_and_noi(noi0: float, cap0: float, noi_change: float, cap1: float) -> dict:
    """Value before and after an NOI change (decimal, e.g. -0.10) and cap-rate move."""
    v0 = direct_cap_value(noi0, cap0)
    noi1 = noi0 * (1.0 + noi_change)
    v1 = direct_cap_value(noi1, cap1)
    return {"v0": v0, "noi1": noi1, "v1": v1, "pct_change": v1 / v0 - 1.0}


def cap_rate_shock_pct(cap0: float, cap1: float) -> float:
    """Percentage value change from a cap-rate move with NOI unchanged: cap0/cap1 - 1."""
    return cap0 / cap1 - 1.0


def loaded_cap_value(noi_before_tax: float, cap_rate: float, effective_tax_rate_on_value: float) -> float:
    """Value when property tax is reassessed at the purchase price.

    If tax = t * V (t = tax rate x assessment ratio), then
        V = (NOI_pre_tax - t V) / c   =>   V = NOI_pre_tax / (c + t).
    ``noi_before_tax`` is NOI before real estate taxes.
    """
    return noi_before_tax / (cap_rate + effective_tax_rate_on_value)


def dcf_value(cash_flows: Sequence[float], terminal_noi: float, exit_cap: float,
              discount_rate: float, selling_cost_pct: float = 0.0) -> dict:
    """Unlevered DCF: annual cash flows for years 1..n, reversion at end of year n.

    ``cash_flows`` are property cash flows after capex for years 1..n.
    Reversion = terminal_noi / exit_cap * (1 - selling_cost_pct), where
    ``terminal_noi`` is normally year n+1 NOI (forward NOI capitalized at exit).
    """
    n = len(cash_flows)
    gross_rev = terminal_noi / exit_cap
    net_rev = gross_rev * (1.0 - selling_cost_pct)
    flows = [0.0] + list(cash_flows)
    flows[-1] += net_rev
    pv_total = tvm.npv(discount_rate, flows)
    pv_rev = net_rev / (1.0 + discount_rate) ** n
    return {"value": pv_total, "gross_reversion": gross_rev, "net_reversion": net_rev,
            "pv_reversion": pv_rev, "reversion_share": pv_rev / pv_total}


# --------------------------------------------------------------------------
# Debt sizing
# --------------------------------------------------------------------------

def dscr(noi: float, debt_service: float) -> float:
    """Debt service coverage ratio. Lenders often use underwritten NCF, not NOI."""
    return noi / debt_service


def debt_yield(noi: float, loan: float) -> float:
    """NOI / loan amount."""
    return noi / loan


def ltv(loan: float, value: float) -> float:
    return loan / value


def max_loan(noi: float, value: float, annual_rate: float, amort_years: float | None,
             ltv_max: float | None = None, dscr_min: float | None = None,
             debt_yield_min: float | None = None, periods_per_year: int = 12,
             interest_only: bool = False, dscr_rate: float | None = None) -> dict:
    """Maximum loan as the minimum of LTV, DSCR, and debt-yield constraints.

    ``dscr_rate`` lets a lender size the DSCR test at a stressed rate (e.g.,
    floating-rate loans sized at the cap strike). Returns each constraint and the
    binding one.
    """
    out: dict = {}
    if ltv_max is not None:
        out["ltv"] = value * ltv_max
    if dscr_min is not None:
        r = annual_rate if dscr_rate is None else dscr_rate
        k = r if (interest_only or amort_years is None) else tvm.loan_constant(r, amort_years, periods_per_year)
        out["dscr"] = noi / dscr_min / k
    if debt_yield_min is not None:
        out["debt_yield"] = noi / debt_yield_min
    if not out:
        raise ValueError("at least one constraint is required")
    binding = min(out, key=out.get)
    out["max_loan"] = out[binding]
    out["binding"] = binding
    return out


def refinance_gap(existing_balance: float, new_loan: float, closing_costs: float = 0.0) -> float:
    """Equity required to refinance (positive) or cash-out available (negative)."""
    return existing_balance + closing_costs - new_loan


# --------------------------------------------------------------------------
# Returns and leverage
# --------------------------------------------------------------------------

def cash_on_cash(before_tax_cash_flow: float, equity: float) -> float:
    return before_tax_cash_flow / equity


def equity_value(asset_value: float, debt: float) -> float:
    """Book-to-market equity; may be negative (debt exceeds value)."""
    return asset_value - debt


def levered_equity_change(v0: float, v1: float, debt: float) -> dict:
    """Equity before/after an asset value change with constant debt."""
    e0, e1 = v0 - debt, v1 - debt
    return {"e0": e0, "e1": e1, "pct_change": e1 / e0 - 1.0, "ltv1": debt / v1}


def recovery_return_required(drawdown: float) -> float:
    """Gain required to recover from a fractional loss d: 1/(1-d) - 1."""
    if drawdown >= 1.0:
        return float("inf")
    return 1.0 / (1.0 - drawdown) - 1.0


def breakeven_occupancy(operating_expenses: float, debt_service: float,
                        potential_gross_income: float) -> float:
    """(OpEx + debt service) / PGI -- the conventional apartment/office measure.

    Assumes expenses do not vary with occupancy. For hotels use
    ``hotel.breakeven_occupancy`` which handles variable costs.
    """
    return (operating_expenses + debt_service) / potential_gross_income


def operating_leverage(revenue: float, fixed_costs: float, variable_cost_ratio: float,
                       revenue_change: float) -> dict:
    """Percentage change in NOI for a percentage change in revenue.

    NOI = R(1-v) - F. DOL = R(1-v)/NOI.
    """
    noi0 = revenue * (1 - variable_cost_ratio) - fixed_costs
    r1 = revenue * (1 + revenue_change)
    noi1 = r1 * (1 - variable_cost_ratio) - fixed_costs
    return {"noi0": noi0, "noi1": noi1, "pct_change": noi1 / noi0 - 1.0,
            "dol": revenue * (1 - variable_cost_ratio) / noi0}


# --------------------------------------------------------------------------
# Equity waterfall
# --------------------------------------------------------------------------

def irr_hurdle_waterfall(equity_flows: Sequence[float], hurdles: Sequence[float],
                         investor_splits: Sequence[float]) -> dict:
    """IRR-hurdle distribution waterfall (annual periods, pooled equity).

    ``equity_flows``: total project equity flows; negative = capital contributed
    (by investors), positive = distributable cash.
    ``hurdles``: ascending IRR hurdles, e.g. [0.08, 0.12, 0.15].
    ``investor_splits``: investor share of each tier; length len(hurdles)+1.
    E.g. [1.0, 0.8, 0.7, 0.6] -> 100% to investors until 8%, 80/20 to 12%,
    70/30 to 15%, 60/40 thereafter.

    Mechanics: for each hurdle h a balance accrues at h on contributions net of
    investor distributions. The balance equals the amount investors still need
    to reach an IRR of h. Balances are not floored, which preserves the exact IRR
    interpretation (investor IRR >= h iff final balance <= 0).
    """
    if len(investor_splits) != len(hurdles) + 1:
        raise ValueError("investor_splits must have len(hurdles)+1 entries")
    balances = [0.0] * len(hurdles)
    inv_flows, promote_flows = [], []
    for t, cf in enumerate(equity_flows):
        if t > 0:
            balances = [b * (1.0 + h) for b, h in zip(balances, hurdles)]
        if cf <= 0:
            balances = [b - cf for b in balances]
            inv_flows.append(cf)
            promote_flows.append(0.0)
            continue
        remaining = cf
        inv_total = prom_total = 0.0
        for k, h in enumerate(hurdles):
            need = max(balances[k], 0.0)
            if need <= 0 or remaining <= 0:
                continue
            s = investor_splits[k]
            gross = min(remaining, need / s)
            inv = gross * s
            inv_total += inv
            prom_total += gross - inv
            remaining -= gross
            balances = [b - inv for b in balances]
        if remaining > 0:
            s = investor_splits[-1]
            inv_total += remaining * s
            prom_total += remaining * (1 - s)
            balances = [b - remaining * s for b in balances]
        inv_flows.append(inv_total)
        promote_flows.append(prom_total)
    try:
        inv_irr = tvm.irr(inv_flows) if any(f > 0 for f in inv_flows) else None
    except ValueError:  # flows with no sign change on the search interval have no IRR
        inv_irr = None
    return {"investor": inv_flows, "promote": promote_flows, "investor_irr": inv_irr}


# --------------------------------------------------------------------------
# Development and land
# --------------------------------------------------------------------------

def residual_land_value(gross_development_value: float, hard_costs: float, soft_costs: float,
                        financing_costs: float, developer_margin_on_cost: float,
                        selling_cost_pct: float = 0.0) -> dict:
    """Residual land value with a required developer margin on total cost.

    Net value N = GDV (1 - selling costs). Total cost C = L + H + S + F.
    Require N = C (1 + m)  =>  L = N/(1+m) - (H + S + F).
    Financing on land is assumed to be included in ``financing_costs``.
    """
    net = gross_development_value * (1.0 - selling_cost_pct)
    non_land = hard_costs + soft_costs + financing_costs
    land = net / (1.0 + developer_margin_on_cost) - non_land
    return {"net_value": net, "non_land_cost": non_land, "land_value": land,
            "total_cost": non_land + land, "profit": net - (non_land + land)}


# --------------------------------------------------------------------------
# Scenario analysis
# --------------------------------------------------------------------------

def scenario_summary(outcomes: Sequence[float], probs: Sequence[float]) -> dict:
    """Expected value, standard deviation, and probability of loss for discrete scenarios.

    Outcomes are profits (negative = loss). Probabilities must sum to 1.
    """
    if abs(sum(probs) - 1.0) > 1e-9:
        raise ValueError("probabilities must sum to 1")
    ev = sum(o * p for o, p in zip(outcomes, probs))
    var = sum(p * (o - ev) ** 2 for o, p in zip(outcomes, probs))
    p_loss = sum(p for o, p in zip(outcomes, probs) if o < 0)
    exp_loss = sum(p * o for o, p in zip(outcomes, probs) if o < 0)
    return {"ev": ev, "sd": var ** 0.5, "p_loss": p_loss, "expected_loss": exp_loss}


def breakeven_probability(gain_if_good: float, loss_if_bad: float) -> float:
    """Probability of the bad state at which a two-outcome bet has zero EV.

    EV = (1-p) G - p L = 0  =>  p* = G / (G + L). ``loss_if_bad`` is positive.
    """
    return gain_if_good / (gain_if_good + loss_if_bad)


def distressed_loan_recovery(purchase_price: float, scenarios: Sequence[dict],
                             discount_rate: float) -> dict:
    """Expected PV recovery for a loan purchase.

    Each scenario: {"p": prob, "recovery": gross cash, "costs": legal/carry costs,
    "years": time to resolution}. Net cash = recovery - costs received at ``years``.
    Returns expected PV, expected profit, and per-scenario annualized returns.
    """
    exp_pv = 0.0
    detail = []
    for s in scenarios:
        net = s["recovery"] - s.get("costs", 0.0)
        pv_net = net / (1 + discount_rate) ** s["years"]
        exp_pv += s["p"] * pv_net
        ann = (net / purchase_price) ** (1 / s["years"]) - 1 if net > 0 else -1.0
        detail.append({**s, "net": net, "pv": pv_net, "annualized_return": ann})
    return {"expected_pv": exp_pv, "npv": exp_pv - purchase_price, "detail": detail}
