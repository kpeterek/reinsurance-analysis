"""Case C — Cap Rate Expansion and Equity Destruction. Reproducible model.

Run:  python3 cases/hypothetical/case_C_cap_rate_expansion/case_c_model.py
Every input is hypothetical [HYPOTHESIS]. Every number quoted in case_C.md and
case_C_rubric.md is produced here and asserted in tests/test_case_c.py.

Timing conventions (notation guide section 3):
* t = 0 is acquisition. The shock is observed at the end of year 3 (month 36).
* The loan is interest-only for 24 months, then amortizes monthly on a 30-year
  schedule. Balances are computed after the stated number of amortizing payments.
* Values are forward NOI / cap rate. Debt-service tests use annual debt service
  on the amortizing payment (the payment actually due at the test date).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "models" / "python"))

from sdesk import cre, tvm  # noqa: E402

# ----------------------------------------------------------------- inputs
PRICE = 20_000_000
GOING_IN_CAP = 0.06                     # [HYPOTHESIS] chosen for the case
NOI0 = PRICE * GOING_IN_CAP             # forward NOI at acquisition, after reserves
BUYER_CLOSING_PCT = 0.015
RSF = 78_000                             # rentable square feet (medical office)

# Acquisition loan [HYPOTHESIS]
LTV0 = 0.70
LOAN = LTV0 * PRICE
RATE = 0.05                              # fixed, nominal annual, monthly pay
IO_MONTHS = 24
AMORT_YEARS = 30
TERM_YEARS = 5
LTV_COVENANT = 0.75                      # maintenance test on lender appraisal
DSCR_COVENANT = 1.15                     # financial covenant (event of default)
CASH_MGMT_DSCR = 1.25                    # cash-management (sweep) trigger
CASH_MGMT_DY = 0.08                      # cash-management (sweep) trigger

# The shock (given in the assignment)
NOI_SHOCK = -0.10
CAP_SHOCK = 0.015
SHOCK_MONTH = 36

# Market after the shock [HYPOTHESIS]
NOI_GROWTH_AFTER = 0.02                  # from the shocked level
SELLING_COST_PCT = 0.02
REFI = dict(rate=0.0675, amort=30, ltv=0.60, dscr=1.30, debt_yield=0.095)

# Forced-sale buyer underwriting [HYPOTHESIS]
BUYER_IRR = 0.11                         # opportunistic unlevered target
BUYER_GROWTH = 0.025
BUYER_CAPEX_PCT_NOI = 0.08               # TI/LC and building capital, share of NOI
BUYER_EXIT_CAP = 0.08
BUYER_HOLD = 5

# Sponsor option analysis at maturity (end of year 5) [HYPOTHESIS]
MATURITY_SCENARIOS = [  # (probability, asset value at maturity)
    (0.25, 17_500_000),
    (0.50, 15_000_000),
    (0.25, 12_000_000),
]
SPONSOR_DISCOUNT = 0.12
PREF_RATE = 0.13                          # rescue preferred equity, accrues and compounds

# Lender recovery analysis [HYPOTHESIS]
FORECLOSURE_MONTHS = 15
FORECLOSURE_COST_PCT = 0.05               # legal, receiver, leasing disruption, of sale price
LENDER_DISCOUNT = 0.08
NOTE_SALE_PRICE_PCT_OF_BALANCE = 0.80


# ----------------------------------------------------------------- loan mechanics
def amortizing_debt_service() -> float:
    return tvm.annual_debt_service(LOAN, RATE, AMORT_YEARS)


def io_debt_service() -> float:
    return tvm.annual_debt_service(LOAN, RATE, None, interest_only=True)


def balance_at(month: int) -> float:
    """Balance after ``month`` months, with IO for the first IO_MONTHS months."""
    amort_payments = max(0, month - IO_MONTHS)
    return tvm.loan_balance(LOAN, RATE, AMORT_YEARS, amort_payments)


# ----------------------------------------------------------------- origination
def origination() -> dict:
    ds_io, ds_am = io_debt_service(), amortizing_debt_service()
    equity_cash = PRICE * (1 + BUYER_CLOSING_PCT) - LOAN
    return {"noi": NOI0, "loan": LOAN, "equity_cash": equity_cash, "equity_mark": PRICE - LOAN,
            "ds_io": ds_io, "ds_amort": ds_am, "loan_constant": ds_am / LOAN,
            "dscr_io": NOI0 / ds_io, "dscr_amort": NOI0 / ds_am,
            "debt_yield": NOI0 / LOAN, "ltv": LOAN / PRICE,
            "cash_on_cash_io": (NOI0 - ds_io) / equity_cash,
            "cash_on_cash_amort": (NOI0 - ds_am) / equity_cash,
            "per_sf": PRICE / RSF}


# ----------------------------------------------------------------- the shock
def shock() -> dict:
    noi1 = NOI0 * (1 + NOI_SHOCK)
    cap1 = GOING_IN_CAP + CAP_SHOCK
    v1 = cre.direct_cap_value(noi1, cap1)
    bal = balance_at(SHOCK_MONTH)
    e_pre = PRICE - bal
    e_post = v1 - bal
    dd_equity = 1 - e_post / e_pre
    dd_asset = 1 - v1 / PRICE
    # attribution of the value loss
    v_noi_only = cre.direct_cap_value(noi1, GOING_IN_CAP)
    v_cap_only = cre.direct_cap_value(NOI0, cap1)
    return {"noi1": noi1, "cap1": cap1, "value1": v1, "per_sf1": v1 / RSF, "balance": bal,
            "amortized": LOAN - bal, "equity_pre": e_pre, "equity_post": e_post,
            "asset_drawdown": dd_asset, "equity_drawdown": dd_equity,
            "equity_vs_cash_invested": e_post / origination()["equity_cash"] - 1,
            "loss_from_noi_alone": PRICE - v_noi_only, "loss_from_cap_alone": PRICE - v_cap_only,
            "interaction": (PRICE - v1) - (PRICE - v_noi_only) - (PRICE - v_cap_only),
            "value_loss": PRICE - v1,
            "multiplier": dd_equity / dd_asset}


def covenants() -> dict:
    s = shock()
    ds = amortizing_debt_service()
    ltv1 = s["balance"] / s["value1"]
    dscr1 = s["noi1"] / ds
    dy1 = s["noi1"] / s["balance"]
    paydown_to_cure_ltv = s["balance"] - LTV_COVENANT * s["value1"]
    # NOI that just meets each test at the shocked value
    noi_dscr_cov = DSCR_COVENANT * ds
    noi_sweep_dscr = CASH_MGMT_DSCR * ds
    noi_sweep_dy = CASH_MGMT_DY * s["balance"]
    # paydown that cures the debt-yield sweep trigger
    paydown_to_cure_dy = s["balance"] - s["noi1"] / CASH_MGMT_DY
    # cap rate at which LTV covenant breaks with shocked NOI
    cap_ltv_break = s["noi1"] / (s["balance"] / LTV_COVENANT)
    return {"ltv": ltv1, "dscr": dscr1, "debt_yield": dy1,
            "ltv_breach": ltv1 > LTV_COVENANT, "dscr_default": dscr1 < DSCR_COVENANT,
            "sweep_dscr": dscr1 < CASH_MGMT_DSCR, "sweep_dy": dy1 < CASH_MGMT_DY,
            "paydown_ltv": paydown_to_cure_ltv, "paydown_dy": paydown_to_cure_dy,
            "noi_for_dscr_cov": noi_dscr_cov, "noi_for_sweep_dscr": noi_sweep_dscr,
            "noi_for_sweep_dy": noi_sweep_dy, "cap_at_ltv_break": cap_ltv_break,
            "cash_flow_after_ds": s["noi1"] - ds}


def recovery() -> dict:
    s = shock()
    asset_gain = cre.recovery_return_required(s["asset_drawdown"])
    equity_gain = cre.recovery_return_required(s["equity_drawdown"])
    # years of NOI growth to restore $20m at the new cap rate
    noi_needed = PRICE * s["cap1"]
    import math
    years_at_3 = math.log(noi_needed / s["noi1"]) / math.log(1.03)
    cap_needed_now = s["noi1"] / PRICE
    # equity: value needed to restore pre-shock equity mark with the same balance
    value_needed_equity = s["equity_pre"] + s["balance"]
    return {"asset_gain": asset_gain, "equity_gain": equity_gain, "noi_needed": noi_needed,
            "years_at_3pct": years_at_3, "cap_needed_now": cap_needed_now,
            "value_needed_for_equity": value_needed_equity}


def maturity_refi() -> dict:
    s = shock()
    noi_fwd = s["noi1"] * (1 + NOI_GROWTH_AFTER) ** 2      # forward NOI at end of year 5
    value = cre.direct_cap_value(noi_fwd, s["cap1"])
    bal = balance_at(TERM_YEARS * 12)
    sized = cre.max_loan(noi=noi_fwd, value=value, annual_rate=REFI["rate"], amort_years=REFI["amort"],
                         ltv_max=REFI["ltv"], dscr_min=REFI["dscr"], debt_yield_min=REFI["debt_yield"])
    gap = cre.refinance_gap(bal, sized["max_loan"])
    return {"noi_fwd": noi_fwd, "value": value, "balance": bal, **{f"refi_{k}": v for k, v in sized.items()},
            "gap": gap, "ltv_at_maturity": bal / value}


def forced_sale() -> dict:
    """Price an opportunistic buyer pays now, from its own DCF."""
    s = shock()
    noi = [s["noi1"] * (1 + BUYER_GROWTH) ** t for t in range(BUYER_HOLD + 1)]
    cfs = [n * (1 - BUYER_CAPEX_PCT_NOI) for n in noi[:BUYER_HOLD]]
    d = cre.dcf_value(cfs, noi[BUYER_HOLD], BUYER_EXIT_CAP, BUYER_IRR, SELLING_COST_PCT)
    price = d["value"]
    net_to_seller = price * (1 - SELLING_COST_PCT)
    shortfall = s["balance"] - net_to_seller
    return {"noi_path": noi, "cash_flows": cfs, **d, "price": price, "implied_cap": s["noi1"] / price,
            "discount_to_mark": 1 - price / s["value1"], "net_to_seller": net_to_seller,
            "shortfall": shortfall, "lender_recovery_pct": net_to_seller / s["balance"],
            "per_sf": price / RSF}


def lender_options() -> dict:
    """PV of recovery to the lender under three paths (per $ of balance at month 36)."""
    s, fs = shock(), forced_sale()
    bal = s["balance"]
    # 1. Consensual short sale now
    short_sale = min(fs["net_to_seller"], bal)
    # 2. Foreclose, then sell at the same forced-sale price after FORECLOSURE_MONTHS,
    #    receiving NOI less debt-service-free carry? Lender collects net cash flow in the
    #    interim only if a receiver is appointed; assume interim NOI after capex accrues
    #    to the lender and is received with the sale.
    t = FORECLOSURE_MONTHS / 12
    interim = fs["cash_flows"][0] * t
    gross = fs["price"] * (1 - SELLING_COST_PCT - FORECLOSURE_COST_PCT) + interim
    foreclose_pv = min(gross, bal) / (1 + LENDER_DISCOUNT) ** t
    # 3. Note sale at a percentage of balance, now
    note_sale = NOTE_SALE_PRICE_PCT_OF_BALANCE * bal
    return {"short_sale": short_sale, "foreclose_pv": foreclose_pv, "note_sale": note_sale,
            "short_sale_pct": short_sale / bal, "foreclose_pct": foreclose_pv / bal,
            "note_sale_pct": note_sale / bal}


def sponsor_options() -> dict:
    """Expected PV to the sponsor of (a) keys back, (b) cure the LTV and hold, (c) rescue pref.

    Sale at maturity (end of year 5) at the scenario value less selling costs.
    Between month 36 and 60 the property's cash flow after debt service is trapped
    by the cash-management sweep and applied to principal; it is ignored here as a
    conservative simplification (the sweep accrues to the lender's benefit).
    """
    s, c = shock(), covenants()
    paydown = c["paydown_ltv"]
    bal60 = balance_at(TERM_YEARS * 12)
    # paying down principal at month 36 reduces the month-60 balance by the paydown
    # grown at the loan rate less the reduction in scheduled amortization: with the
    # payment held constant, the balance falls by paydown*(1+i)^24.
    i = RATE / 12
    bal60_cured = bal60 - paydown * (1 + i) ** 24
    rows = []
    ev_cure = ev_none = ev_pref = ev_pref_inv = ev_value = 0.0
    pref = paydown
    pref_due = pref * (1 + PREF_RATE) ** 2
    for p, v in MATURITY_SCENARIOS:
        net = v * (1 - SELLING_COST_PCT)
        cure = max(net - bal60_cured, 0.0)
        no_cure = max(net - bal60, 0.0)     # if the lender waived the LTV breach
        pref_res = max(net - bal60_cured - pref_due, 0.0)
        pref_paid = min(max(net - bal60_cured, 0.0), pref_due)
        rows.append({"p": p, "value": v, "net": net, "cure_payoff": cure,
                     "no_cure_payoff": no_cure, "pref_residual": pref_res, "pref_paid": pref_paid})
        ev_pref_inv += p * pref_paid
        ev_value += p * v
        ev_cure += p * cure
        ev_none += p * no_cure
        ev_pref += p * pref_res
    d2 = (1 + SPONSOR_DISCOUNT) ** 2
    return {"paydown": paydown, "bal60": bal60, "bal60_cured": bal60_cured, "rows": rows,
            "ev_cure": ev_cure, "pv_cure": ev_cure / d2, "npv_cure": ev_cure / d2 - paydown,
            "ev_waiver": ev_none, "pv_waiver": ev_none / d2,
            "pref_due": pref_due, "ev_pref": ev_pref, "pv_pref": ev_pref / d2,
            "ev_pref_investor": ev_pref_inv,
            "pref_investor_expected_irr": (ev_pref_inv / pref) ** 0.5 - 1,
            "ev_value": ev_value}


def cure_breakeven_recovery_probability() -> float:
    """Probability of the recovery scenario at which the cure has zero NPV.

    The base scenario's probability is held at its stated value; probability moves
    between the recovery and further-decline scenarios.
    """
    so = sponsor_options()
    (p_up, _), (p_base, _), (p_dn, _) = MATURITY_SCENARIOS
    up, base, dn = (r["cure_payoff"] for r in so["rows"])
    required_ev = so["paydown"] * (1 + SPONSOR_DISCOUNT) ** 2
    rest = 1.0 - p_base
    # EV(q) = q*up + p_base*base + (rest - q)*dn
    return (required_ev - p_base * base - rest * dn) / (up - dn)


def leverage_table(ltvs=(0.0, 0.5, 0.6, 0.7, 0.75)) -> list[dict]:
    """Equity drawdown for the same asset shock at different initial LTVs (IO debt, no amortization)."""
    v1 = shock()["value1"]
    out = []
    for lam in ltvs:
        debt = lam * PRICE
        e0, e1 = PRICE - debt, v1 - debt
        out.append({"ltv": lam, "equity0": e0, "equity1": e1, "drawdown": 1 - e1 / e0,
                    "ltv_after": debt / v1})
    return out


def shock_grid(noi_shocks=(0.0, -0.05, -0.10, -0.15), cap_shocks=(0.005, 0.010, 0.015, 0.020)) -> dict:
    """LTV and equity drawdown (vs pre-shock mark) at month 36 for combinations of shocks."""
    bal = balance_at(SHOCK_MONTH)
    e_pre = PRICE - bal
    out = {}
    for dn in noi_shocks:
        for dc in cap_shocks:
            v = cre.direct_cap_value(NOI0 * (1 + dn), GOING_IN_CAP + dc)
            out[(dn, dc)] = {"value": v, "ltv": bal / v, "equity_drawdown": 1 - (v - bal) / e_pre}
    return out


def report() -> str:
    o, s, c, r = origination(), shock(), covenants(), recovery()
    m, f, lo, so = maturity_refi(), forced_sale(), lender_options(), sponsor_options()
    L = [f"Origination: NOI {o['noi']:,.0f} loan {o['loan']:,.0f} equity cash {o['equity_cash']:,.0f}",
         f"  DS IO {o['ds_io']:,.0f} amort {o['ds_amort']:,.0f} (K {o['loan_constant']:.4%}); "
         f"DSCR {o['dscr_io']:.2f}x/{o['dscr_amort']:.2f}x DY {o['debt_yield']:.2%}",
         f"Shock: NOI {s['noi1']:,.0f} cap {s['cap1']:.2%} value {s['value1']:,.0f} balance {s['balance']:,.0f}",
         f"  equity {s['equity_pre']:,.0f} -> {s['equity_post']:,.0f}; asset dd {s['asset_drawdown']:.2%} "
         f"equity dd {s['equity_drawdown']:.2%}",
         f"  loss NOI-only {s['loss_from_noi_alone']:,.0f} cap-only {s['loss_from_cap_alone']:,.0f} "
         f"interaction {s['interaction']:,.0f}",
         f"Covenants: LTV {c['ltv']:.2%} DSCR {c['dscr']:.3f}x DY {c['debt_yield']:.2%}; paydown LTV "
         f"{c['paydown_ltv']:,.0f} DY {c['paydown_dy']:,.0f}",
         f"Recovery: asset {r['asset_gain']:.2%} equity {r['equity_gain']:.2%} years@3% {r['years_at_3pct']:.2f}",
         f"Maturity: NOI {m['noi_fwd']:,.0f} value {m['value']:,.0f} bal {m['balance']:,.0f} "
         f"new loan {m['refi_max_loan']:,.0f} ({m['refi_binding']}) gap {m['gap']:,.0f}",
         f"Forced sale: price {f['price']:,.0f} cap {f['implied_cap']:.2%} disc {f['discount_to_mark']:.2%} "
         f"net {f['net_to_seller']:,.0f} shortfall {f['shortfall']:,.0f}",
         f"Lender: short {lo['short_sale_pct']:.2%} foreclose {lo['foreclose_pct']:.2%} note {lo['note_sale_pct']:.2%}",
         f"Sponsor: paydown {so['paydown']:,.0f} PV cure {so['pv_cure']:,.0f} NPV {so['npv_cure']:,.0f} "
         f"PV waiver {so['pv_waiver']:,.0f} PV pref {so['pv_pref']:,.0f}"]
    for row in leverage_table():
        L.append(f"  LTV {row['ltv']:.0%}: equity dd {row['drawdown']:.2%} LTV after {row['ltv_after']:.2%}")
    return "\n".join(L)


if __name__ == "__main__":
    print(report())
