"""CRE cycles and distressed-opportunity mathematics (Chapter 12, Cases E and G).

New module (``x_`` prefix per the authoring brief). It does not change any
existing ``sdesk`` function. Conventions follow the package docstring: rates in
decimals, money in dollars, time in years unless a name says otherwise, cash
flows at the END of each period.

Contents
--------
* ``stock_flow_simulation``     development cycle with a construction lag
* ``texas_earliest_sale_date``  first-Tuesday sale under Tex. Prop. Code 51.002
* ``foreclosure_recovery``      net, discounted recovery after carry and legal costs
* ``appraisal_reduction_amount`` generic CMBS ARA (deal documents govern)
* ``cre_concentration_screens`` 2006 interagency 100% / 300% supervisory screens
* ``sale_needed_for_ratio``      loan sales that bring CRE/capital to a target when
                                 losses on sale reduce capital (forced-selling loop)
* ``reit_implied_cap_rate``     cap rate implied by a REIT's enterprise value
* ``reit_nav_per_share``        NAV per share at a private-market cap rate
* ``required_gross_rent``       rent that delivers a target yield on a given basis
* ``scenario_irrs``             IRR per cash-flow scenario and IRR of expected flows
"""

from __future__ import annotations

import datetime as _dt
from typing import Sequence

from . import tvm


# --------------------------------------------------------------------------
# Development cycle: stock-flow model with a construction lag
# --------------------------------------------------------------------------

def stock_flow_simulation(stock0: float, demand0: float, rent0: float, years: int,
                          demand_growth: Sequence[float], natural_vacancy: float,
                          rent_sensitivity: float, feasibility_rent: float,
                          start_sensitivity: float, lag: int, depreciation: float,
                          pipeline0: Sequence[float] = ()) -> list[dict]:
    """Annual stock-flow model of a space market (DiPasquale-Wheaton style, discretized).

    Timing within year t (t = 1..years), all quantities in square feet (or units):

    1. Demand:      D_t = D_{t-1} * (1 + g_t)               (``demand_growth[t-1]``)
    2. Completions: C_t = starts decided in year t - lag     (``pipeline0`` supplies the
                    completions for years 1..lag that were started before year 1)
    3. Stock:       S_t = S_{t-1} * (1 - depreciation) + C_t
    4. Occupied:    O_t = min(D_t, S_t); vacancy v_t = 1 - O_t / S_t. Demand D_t is
                    latent demand: when the market is full, excess demand waits
                    (it is not destroyed) and shows up as rent growth.
    5. Rent:        R_t = R_{t-1} * (1 + rent_sensitivity * (natural_vacancy - v_t))
    6. Starts:      N_t = start_sensitivity * max(0, R_t / feasibility_rent - 1) * S_t

    Starts respond to the *current* rent, but space arrives ``lag`` years later.
    That is the mechanism of overbuilding: developers extrapolate today's rent
    into a market that will contain all the space already started.

    Returns one dict per year (index 0 is the starting state, year 0).
    """
    if len(demand_growth) < years:
        raise ValueError("demand_growth must have one entry per year")
    pipeline = list(pipeline0) + [0.0] * lag
    starts_hist: list[float] = []
    s, d, r = stock0, demand0, rent0
    rows = [{"year": 0, "stock": s, "demand": d, "occupied": min(d, s), "vacancy": 1 - min(d, s) / s, "rent": r,
             "completions": 0.0, "starts": 0.0}]
    for t in range(1, years + 1):
        d = d * (1 + demand_growth[t - 1])
        if t <= lag:
            c = pipeline[t - 1] if t - 1 < len(pipeline0) else 0.0
        else:
            c = starts_hist[t - 1 - lag]
        s = s * (1 - depreciation) + c
        occ = min(d, s)
        v = 1 - occ / s
        r = r * (1 + rent_sensitivity * (natural_vacancy - v))
        n = start_sensitivity * max(0.0, r / feasibility_rent - 1) * s
        starts_hist.append(n)
        rows.append({"year": t, "stock": s, "demand": d, "occupied": occ, "vacancy": v, "rent": r,
                     "completions": c, "starts": n})
    return rows


# --------------------------------------------------------------------------
# Foreclosure timing and economics
# --------------------------------------------------------------------------

def texas_earliest_sale_date(notice_date: _dt.date, min_days: int = 21) -> _dt.date:
    """Earliest foreclosure sale date under Tex. Prop. Code sec. 51.002.

    Statute (as verified for Chapter 12; see references/sources_ch12.md): the sale is
    held between 10 a.m. and 4 p.m. on the first Tuesday of a month, and notice of
    sale must be given at least 21 days before the sale date. If the first Tuesday
    falls on January 1 or July 4 the sale is held on the first Wednesday.

    This computes only the statutory minimum from the date notice is given. It
    ignores loan-document notice and cure periods, acceleration, the residential
    20-day cure notice of sec. 51.002(d), and any injunction or bankruptcy stay.
    """
    earliest = notice_date + _dt.timedelta(days=min_days)
    y, m = earliest.year, earliest.month
    while True:
        first = _dt.date(y, m, 1)
        tuesday = first + _dt.timedelta(days=(1 - first.weekday()) % 7)
        sale = tuesday
        if (m, tuesday.day) in ((1, 1), (7, 4)):
            sale = tuesday + _dt.timedelta(days=1)
        if sale >= earliest:
            return sale
        m += 1
        if m == 13:
            y, m = y + 1, 1


def foreclosure_recovery(value_now: float, months: float, annual_value_drift: float,
                         carry_per_year: float, legal_costs: float, selling_cost_pct: float,
                         discount_rate: float, resale_months: float = 0.0) -> dict:
    """Net recovery to a lender who forecloses, takes title, and resells.

    * Value at resale = value_now * (1 + drift)^((months + resale_months)/12).
    * Carry (taxes, insurance, receiver, protective advances, net of any property
      cash flow) accrues for ``months + resale_months`` at ``carry_per_year``.
    * Legal costs are paid at resolution (a simplification).
    * Net = value_at_resale * (1 - selling_cost_pct) - carry - legal, received at
      the resale date and discounted at ``discount_rate`` (annual effective).
    """
    t = (months + resale_months) / 12.0
    v = value_now * (1 + annual_value_drift) ** t
    carry = carry_per_year * t
    net = v * (1 - selling_cost_pct) - carry - legal_costs
    pv = net / (1 + discount_rate) ** t
    return {"years": t, "value_at_resale": v, "carry": carry, "legal": legal_costs,
            "net": net, "pv": pv}


# --------------------------------------------------------------------------
# CMBS special servicing
# --------------------------------------------------------------------------

def appraisal_reduction_amount(principal: float, accrued_unpaid_interest: float,
                               unreimbursed_advances: float, other_amounts: float,
                               appraised_value: float, haircut: float = 0.10,
                               reserves: float = 0.0) -> float:
    """Generic CMBS appraisal reduction amount (ARA).

    ARA = max(0, principal + accrued unpaid interest + unreimbursed advances
                 + other amounts due (taxes, insurance, fees)
                 - [(1 - haircut) * appraised value + reserves held])

    The 10% haircut (i.e. 90% of appraised value) is the common form; the
    governing definition is the one in each deal's pooling and servicing
    agreement, which may differ in the items included.
    """
    claim = principal + accrued_unpaid_interest + unreimbursed_advances + other_amounts
    return max(0.0, claim - ((1 - haircut) * appraised_value + reserves))


# --------------------------------------------------------------------------
# Bank balance sheets: the 2006 interagency CRE concentration screens
# --------------------------------------------------------------------------

def cre_concentration_screens(cld_loans: float, total_cre_loans: float,
                              total_risk_based_capital: float,
                              total_cre_36m_ago: float) -> dict:
    """The two supervisory screens of the 2006 interagency CRE concentration guidance.

    * Screen 1: construction, land development and other land loans >= 100% of
      total risk-based capital.
    * Screen 2: total non-owner-occupied CRE loans (including CLD) >= 300% of total
      risk-based capital AND that portfolio grew >= 50% over the prior 36 months.

    Meeting a screen is not a lending limit. It identifies a bank the supervisors
    expect to have heightened risk management and may examine further.
    """
    cld_ratio = cld_loans / total_risk_based_capital
    cre_ratio = total_cre_loans / total_risk_based_capital
    growth = total_cre_loans / total_cre_36m_ago - 1
    return {"cld_ratio": cld_ratio, "cre_ratio": cre_ratio, "cre_growth_36m": growth,
            "screen_1": cld_ratio >= 1.0, "screen_2": cre_ratio >= 3.0 and growth >= 0.50}


def sale_needed_for_ratio(cre_loans: float, capital: float, target_ratio: float,
                          price_pct_of_par: float, tax_rate: float = 0.0) -> dict:
    """Par amount X of CRE loans a bank must sell so that CRE / capital <= target.

    Selling X at price p (fraction of carrying value) books an after-tax loss of
    (1 - p)(1 - tax) X, which reduces capital. Solve
        cre - X = target * (capital - (1 - p)(1 - tax) X)
    =>  X = (cre - target * capital) / (1 - target * (1 - p)(1 - tax)).
    The denominator falls as the discount widens: deep discounts force more
    selling, and if target*(1-p)(1-tax) >= 1 no amount of selling works.
    """
    loss_rate = (1 - price_pct_of_par) * (1 - tax_rate)
    denom = 1 - target_ratio * loss_rate
    excess = cre_loans - target_ratio * capital
    if excess <= 0:
        return {"sale_par": 0.0, "loss": 0.0, "capital_after": capital, "feasible": True}
    if denom <= 0:
        return {"sale_par": float("inf"), "loss": float("inf"), "capital_after": float("-inf"),
                "feasible": False}
    x = excess / denom
    loss = loss_rate * x
    return {"sale_par": x, "loss": loss, "capital_after": capital - loss,
            "cre_after": cre_loans - x, "naive_sale": excess, "feasible": True}


# --------------------------------------------------------------------------
# REIT valuation signals
# --------------------------------------------------------------------------

def reit_implied_cap_rate(share_price: float, shares: float, debt: float, preferred: float,
                          cash: float, other_assets: float, forward_cash_noi: float) -> dict:
    """Cap rate implied by a REIT's public market enterprise value.

    Implied real estate value = equity market cap + debt + preferred - cash
                                - non-real-estate assets (at estimated value).
    Implied cap = forward cash NOI / implied real estate value.
    Use cash (not straight-line GAAP) NOI and the same NOI definition as the
    private-market cap rate you compare with.
    """
    mcap = share_price * shares
    ev_re = mcap + debt + preferred - cash - other_assets
    return {"market_cap": mcap, "implied_re_value": ev_re,
            "implied_cap": forward_cash_noi / ev_re}


def reit_nav_per_share(forward_cash_noi: float, private_cap: float, debt: float,
                       preferred: float, cash: float, other_assets: float,
                       shares: float) -> dict:
    """Net asset value per share at a private-market cap rate."""
    gav = forward_cash_noi / private_cap
    nav = gav - debt - preferred + cash + other_assets
    return {"gross_asset_value": gav, "nav": nav, "nav_per_share": nav / shares}


# --------------------------------------------------------------------------
# Basis resets
# --------------------------------------------------------------------------

def required_gross_rent(basis: float, target_yield: float, operating_expenses: float,
                        rentable_sf: float, occupancy: float,
                        annual_leasing_capex: float = 0.0) -> float:
    """Gross rent per occupied sf that yields ``target_yield`` on ``basis``.

    Required NOI after leasing capital = basis * y. Gross revenue must cover that
    plus operating expenses and recurring leasing capital (TI/LC reserve):
        rent = (basis*y + opex + leasing capex) / (rentable_sf * occupancy).
    """
    return (basis * target_yield + operating_expenses + annual_leasing_capex) / (rentable_sf * occupancy)


# --------------------------------------------------------------------------
# Scenario IRRs
# --------------------------------------------------------------------------

def scenario_irrs(flows_by_scenario: Sequence[Sequence[float]], probs: Sequence[float]) -> dict:
    """IRR per scenario, probability-weighted mean IRR, and IRR of expected flows.

    All scenario vectors must have the same length (pad with zeros). A scenario
    whose IRR is undefined (no sign change) raises ValueError from ``tvm.irr``.
    """
    if abs(sum(probs) - 1) > 1e-9:
        raise ValueError("probabilities must sum to 1")
    n = max(len(f) for f in flows_by_scenario)
    padded = [list(f) + [0.0] * (n - len(f)) for f in flows_by_scenario]
    irrs = [tvm.irr(f) for f in padded]
    exp_flows = [sum(p * f[t] for p, f in zip(probs, padded)) for t in range(n)]
    profits = [sum(f) for f in padded]
    return {"irrs": irrs, "mean_irr": sum(p * i for p, i in zip(probs, irrs)),
            "expected_flows": exp_flows, "irr_of_expected": tvm.irr(exp_flows),
            "profits": profits, "expected_profit": sum(p * x for p, x in zip(probs, profits))}
