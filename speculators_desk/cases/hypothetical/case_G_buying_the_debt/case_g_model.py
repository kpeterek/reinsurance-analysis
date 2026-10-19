"""Case G — Buying the Debt Instead of the Property. Reproducible model.

Run:  python3 cases/hypothetical/case_G_buying_the_debt/case_g_model.py
All inputs are hypothetical [HYPOTHESIS]. Every number in case_G.md and
case_G_rubric.md is produced here and asserted in tests/test_case_g.py.

Conventions
-----------
* Monthly cash-flow vectors, month 0 = today, flows at month-end.
* Monthly IRR is annualized as (1 + IRR_m)^12 - 1 (style guide §3.5).
* Investor outflows negative. Unlevered (no note-on-note financing).
* Property NOI is after replacement reserves. Capex is separate.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "models" / "python"))

from sdesk import cre, tvm  # noqa: E402

# ----------------------------------------------------------------- the loan
UPB = 48_000_000
CONTRACT_RATE = 0.0775          # note rate (floating; held constant here)
ACCRUED_INTEREST = 1_200_000    # unpaid contract interest at purchase
NOTE_PRICE = 33_000_000         # offered by the selling bank
NOTE_CLOSING = 150_000          # buyer legal/diligence on the note purchase

# ----------------------------------------------------------------- the collateral
UNITS = 312
AS_IS_NOI = 2_340_000           # current NOI after reserves
AS_IS_CAP = 0.065
STABILIZED_NOI = 3_100_000      # after a $4.0m capex program and 24 months of operation
STABILIZED_CAP = 0.0625
CAPEX = 4_000_000               # spread evenly over the first 24 months of ownership
PLAN_MONTHS = 24                # months from taking title to sale
SALE_COST = 0.02
PROTECTIVE_ADVANCES_M = 75_000  # taxes + insurance per month paid by the lender while the borrower does not
DEED_TRANSFER_TAX = 0.0         # Texas has no state deed-transfer tax [verify for the county/city]

# ----------------------------------------------------------------- resolution scenarios
# months: month of resolution; for title scenarios, the month the noteholder takes title.
SCENARIOS = {
    "Cure / refinance at par": dict(p=0.10, months=6, kind="cash", legal=100_000, advances_months=0),
    "Discounted payoff": dict(p=0.20, months=4, kind="cash", legal=150_000, advances_months=0,
                              payoff=40_000_000),
    "Deed-in-lieu": dict(p=0.30, months=4, kind="title", legal=250_000, advances_months=0,
                         cash_for_keys=500_000, noi_start=AS_IS_NOI),
    "Contested foreclosure": dict(p=0.25, months=10, kind="title", legal=600_000, advances_months=8,
                                  cash_for_keys=0, noi_start=2_200_000),
    "Bankruptcy, stay lifted": dict(p=0.10, months=20, kind="title", legal=1_500_000, advances_months=0,
                                    cash_for_keys=0, noi_start=2_050_000,
                                    adequate_protection=1_200_000),
    "Bankruptcy, cramdown": dict(p=0.05, months=14, kind="cramdown", legal=1_200_000, advances_months=0,
                                 cram_value=36_000_000, cram_rate=0.07, cram_years=5),
}

# ----------------------------------------------------------------- REO alternative
REO_MONTH = 12                  # lender completes foreclosure and markets the REO
REO_PRICE = 37_500_000          # expected clearing price in a competitive REO sale
REO_CLOSING = 0.015
REO_NOI_START = 2_200_000
REO_WIN_PROB = 0.35             # probability our bid wins the marketed REO sale

DISCOUNT_RATE = 0.15            # required annual return for a distressed-debt position


def monthly_to_annual(r_m: float) -> float:
    return (1 + r_m) ** 12 - 1


def stabilized_sale_net() -> float:
    return STABILIZED_NOI / STABILIZED_CAP * (1 - SALE_COST)


def ownership_flows(noi_start: float, months: int = PLAN_MONTHS) -> list[float]:
    """Monthly flows for months 1..months after taking title.

    NOI ramps linearly from ``noi_start`` to STABILIZED_NOI (annual rates) over the
    plan; capex is spent evenly; the asset is sold at the end of the plan at
    STABILIZED_NOI / STABILIZED_CAP (forward NOI = stabilized), less SALE_COST.
    """
    flows = []
    for k in range(1, months + 1):
        noi_annual = noi_start + (STABILIZED_NOI - noi_start) * (k - 0.5) / months
        flows.append(noi_annual / 12 - CAPEX / months)
    flows[-1] += stabilized_sale_net()
    return flows


def note_flows(name: str, price: float = NOTE_PRICE) -> list[float]:
    """Monthly cash flows to the note buyer in one resolution scenario."""
    s = SCENARIOS[name]
    m = s["months"]
    horizon = m + (PLAN_MONTHS if s["kind"] == "title" else 0) + (12 * s.get("cram_years", 0))
    f = [0.0] * (horizon + 1)
    f[0] = -(price + NOTE_CLOSING)
    for k in range(1, s["advances_months"] + 1):
        f[k] -= PROTECTIVE_ADVANCES_M
    if s["kind"] == "cash":
        if "payoff" in s:
            f[m] += s["payoff"]
        else:
            f[m] += UPB + ACCRUED_INTEREST + UPB * CONTRACT_RATE * m / 12
        f[m] -= s["legal"]
    elif s["kind"] == "title":
        f[m] -= s["legal"] + s.get("cash_for_keys", 0.0)
        ap = s.get("adequate_protection", 0.0)
        if ap:
            for k in range(1, m + 1):
                f[k] += ap / m
        for j, cf in enumerate(ownership_flows(s["noi_start"]), start=1):
            f[m + j] += cf
    elif s["kind"] == "cramdown":
        f[m] -= s["legal"]
        n = 12 * s["cram_years"]
        pmt = s["cram_value"] * s["cram_rate"] / 12      # interest-only new note
        for j in range(1, n + 1):
            f[m + j] += pmt
        f[m + n] += s["cram_value"]
    return f


def note_scenarios(price: float = NOTE_PRICE) -> dict:
    out = {}
    for name, s in SCENARIOS.items():
        f = note_flows(name, price)
        irr_m = tvm.irr(f)
        out[name] = {"p": s["p"], "flows": f, "months": len(f) - 1, "irr": monthly_to_annual(irr_m),
                     "profit": sum(f), "multiple": tvm.equity_multiple(f),
                     "npv": tvm.npv((1 + DISCOUNT_RATE) ** (1 / 12) - 1, f)}
    return out


def note_summary(price: float = NOTE_PRICE) -> dict:
    sc = note_scenarios(price)
    names = list(sc)
    probs = [sc[n]["p"] for n in names]
    n = max(sc[x]["months"] for x in names)
    padded = [sc[x]["flows"] + [0.0] * (n - sc[x]["months"]) for x in names]
    exp = [sum(p * f[t] for p, f in zip(probs, padded)) for t in range(n + 1)]
    summ = cre.scenario_summary([sc[x]["profit"] for x in names], probs)
    return {"scenarios": sc, "expected_flows": exp,
            "irr_of_expected": monthly_to_annual(tvm.irr(exp)),
            "mean_irr": sum(p * sc[x]["irr"] for p, x in zip(probs, names)),
            "expected_npv": sum(p * sc[x]["npv"] for p, x in zip(probs, names)),
            "expected_profit": summ["ev"], "sd_profit": summ["sd"], "p_loss": summ["p_loss"],
            "min_irr": min(sc[x]["irr"] for x in names), "p_title": sum(
                SCENARIOS[x]["p"] for x in names if SCENARIOS[x]["kind"] == "title")}


def max_note_price(rate: float = DISCOUNT_RATE) -> float:
    """Price at which expected NPV at ``rate`` is zero (closing cost included in flows)."""
    rm = (1 + rate) ** (1 / 12) - 1
    pv_inflows = 0.0
    for name, s in SCENARIOS.items():
        f = note_flows(name, 0.0)
        pv_inflows += s["p"] * tvm.npv(rm, f)       # f[0] = -NOTE_CLOSING only
    return pv_inflows


def reo_flows() -> list[float]:
    """Buy the REO at month REO_MONTH, execute the same plan, sell PLAN_MONTHS later.

    Measured from the REO closing (month 0 = REO closing), so the IRR is the
    return on capital actually deployed. The waiting period is analyzed separately.
    """
    f = [0.0] * (PLAN_MONTHS + 1)
    f[0] = -REO_PRICE * (1 + REO_CLOSING)
    for j, cf in enumerate(ownership_flows(REO_NOI_START), start=1):
        f[j] += cf
    return f


def reo_summary() -> dict:
    f = reo_flows()
    irr = monthly_to_annual(tvm.irr(f))
    return {"flows": f, "irr": irr, "profit": sum(f), "multiple": tvm.equity_multiple(f),
            "basis": REO_PRICE * (1 + REO_CLOSING),
            "expected_profit_incl_losing": REO_WIN_PROB * sum(f)}


def loss_given_title_value(value_drop: float) -> dict:
    """Stress: stabilized value falls by ``value_drop`` in every title/cramdown scenario.

    Implemented by scaling the sale price; returns the note IRR of expected flows.
    """
    global STABILIZED_NOI
    old = STABILIZED_NOI
    try:
        STABILIZED_NOI = old * (1 - value_drop)
        s = note_summary()
        r = reo_summary()
    finally:
        STABILIZED_NOI = old
    return {"note_irr_of_expected": s["irr_of_expected"], "note_p_loss": s["p_loss"],
            "reo_irr": r["irr"]}


def credit_bid_capacity(months_default: int = 10) -> float:
    """Debt the noteholder may credit-bid at a foreclosure sale: UPB + accrued contract
    interest + default interest (5% over contract) + protective advances + legal.
    Shown only to illustrate why third-party cash bids rarely exceed it."""
    default_rate = CONTRACT_RATE + 0.05
    return (UPB + ACCRUED_INTEREST + UPB * default_rate * months_default / 12
            + PROTECTIVE_ADVANCES_M * 8 + 600_000)


def report() -> str:
    s = note_summary()
    lines = [f"Note: UPB {UPB:,.0f} price {NOTE_PRICE:,.0f} ({NOTE_PRICE / UPB:.2%} of UPB); "
             f"as-is value {AS_IS_NOI / AS_IS_CAP:,.0f}; stabilized net sale {stabilized_sale_net():,.0f}",
             f"Price per unit: note {NOTE_PRICE / UNITS:,.0f}; REO {REO_PRICE / UNITS:,.0f}"]
    for n, x in s["scenarios"].items():
        lines.append(f"  {n:<26s} p {x['p']:.2f} months {x['months']:3d} IRR {x['irr']:8.2%} "
                     f"profit {x['profit']:14,.0f} multiple {x['multiple']:.2f}x NPV@15% {x['npv']:13,.0f}")
    lines.append(f"Note: IRR of expected flows {s['irr_of_expected']:.2%}; mean IRR {s['mean_irr']:.2%}; "
                 f"E[profit] {s['expected_profit']:,.0f}; sd {s['sd_profit']:,.0f}; P(loss) {s['p_loss']:.0%}; "
                 f"E[NPV@15%] {s['expected_npv']:,.0f}; P(title) {s['p_title']:.2f}")
    lines.append(f"Max note price at 15%: {max_note_price():,.0f} ({max_note_price() / UPB:.2%} of UPB)")
    r = reo_summary()
    lines.append(f"REO: basis {r['basis']:,.0f} IRR {r['irr']:.2%} profit {r['profit']:,.0f} multiple {r['multiple']:.2f}x; "
                 f"x win prob {REO_WIN_PROB:.0%} -> {r['expected_profit_incl_losing']:,.0f}")
    for d in (0.10, 0.20):
        x = loss_given_title_value(d)
        lines.append(f"Stabilized value -{d:.0%}: note IRR(E) {x['note_irr_of_expected']:.2%} P(loss) {x['note_p_loss']:.0%}; "
                     f"REO IRR {x['reo_irr']:.2%}")
    lines.append(f"Credit-bid capacity after 10 months: {credit_bid_capacity():,.0f}")
    return "\n".join(lines)


if __name__ == "__main__":
    print(report())
