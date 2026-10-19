"""Case F — The Hotel versus Treasury Trade. Reproducible model.

Run:  python3 cases/hypothetical/case_F_hotel_vs_treasury/case_f_model.py
All market and property inputs are hypothetical [HYPOTHESIS]. Tax rates are the
federal statutory rates verified for this project (references/sources_ch13.md,
ch13-S13 to S16) applied in a deliberately SIMPLIFIED way. This is a teaching
model, not tax advice.

Simplifications (each is stated in case_F.md):
* Investor: Texas resident, married filing jointly, in the top federal bracket
  for every dollar of income from either alternative. Texas levies no personal
  income tax, so the state exemption of Treasury interest (31 U.S.C. 3124) is moot.
* Hotel net income and Treasury interest are both taxed at 37% + 3.8% NIIT.
  Taxable losses are assumed usable against other passive income in the same
  year (the passive-activity rules can defer them; see case text).
* Depreciation: full-year straight-line from year 1 (no mid-month convention, no
  cost segregation, no bonus depreciation). Building 39 years; FF&E 7 years.
* The FF&E reserve in NOI is treated as a deductible expense (in practice
  replacements are capitalized and depreciated).
* On sale, FF&E is assumed to be sold at its remaining tax basis (no s.1245
  recapture). Gain up to building depreciation taken is unrecaptured s.1250 gain
  at 25% + 3.8%; the remainder is long-term capital gain at 20% + 3.8%.
  If the sale produces a loss, it is assumed usable at 23.8% (a simplification).
* Treasury: 5-year note bought at par, coupons aggregated annually for
  comparability with annual hotel flows, held to maturity.
* Annual cash flows at year-end; mortgage monthly in arrears at r/12.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "models" / "python"))

from sdesk import cre, fixed_income as fi, tvm  # noqa: E402

# ----------------------------------------------------------------- inputs
ROOMS = 110
PRICE = 16_500_000
NOI1 = 1_400_000                 # year-1 NOI after a 4% FF&E reserve
CLOSING = 0.02                   # buyer closing costs, capitalized into basis
LTV, RATE, AMORT = 0.60, 0.07, 25
SELL = 0.03
HOLD = 5
ALLOC = {"land": 0.15, "building": 0.75, "ffe": 0.10}
LIFE = {"building": 39, "ffe": 7}

T_ORD = 0.37
NIIT = 0.038
T_LTCG = 0.20
T_1250 = 0.25
STATE = 0.0                      # Texas

TSY_YIELD = 0.04                 # 5-year Treasury, hypothetical; replace with a live quote
CPI = 0.025                      # base-case inflation, hypothetical

# Scenarios: name -> (probability, NOI path multipliers vs base path for years 1..6, base growth, exit cap)
SCENARIOS = {
    "Upside": (0.20, [1, 1, 1, 1, 1, 1], 0.05, 0.085),
    "Base": (0.45, [1, 1, 1, 1, 1, 1], 0.03, 0.090),
    "Downside": (0.25, [1, 0.75, 0.85, 0.95, 0.95, 0.95], 0.03, 0.100),
    "Severe": (0.10, [0.35, 0.65, 0.80, 0.85, 0.90, 0.90], 0.03, 0.110),
}
INFLATION_CASE = ([1] * 6, 0.05, 0.100, 0.05)  # NOI growth 5%, exit cap 10%, CPI 5%

HYPO_STATE_RATE = 0.06           # illustration only: a hypothetical state with a 6% income tax


# ----------------------------------------------------------------- building blocks
def rates() -> dict:
    return {"ordinary": T_ORD + NIIT + STATE, "ltcg": T_LTCG + NIIT + STATE,
            "unrecap_1250": T_1250 + NIIT + STATE, "interest": T_ORD + NIIT + STATE}


def basis() -> dict:
    total = PRICE * (1 + CLOSING)
    parts = {k: total * v for k, v in ALLOC.items()}
    dep = {k: parts[k] / LIFE[k] for k in LIFE}
    return {"total": total, **parts, "dep_building": dep["building"], "dep_ffe": dep["ffe"],
            "dep_total": dep["building"] + dep["ffe"]}


def loan() -> dict:
    amt = LTV * PRICE
    pmt = tvm.payment(amt, RATE, AMORT)
    sched = tvm.amortization_schedule(amt, RATE, AMORT, periods=12 * HOLD)
    interest = [sum(r["interest"] for r in sched[12 * y:12 * (y + 1)]) for y in range(HOLD)]
    return {"amount": amt, "monthly": pmt, "annual_ds": 12 * pmt, "interest": interest,
            "balance_end": sched[-1]["end"], "balance_check": tvm.loan_balance(amt, RATE, AMORT, 12 * HOLD)}


def equity() -> float:
    return PRICE * (1 + CLOSING) - loan()["amount"]


def noi_path(mults, g) -> list[float]:
    return [NOI1 * (1 + g) ** t * mults[t] for t in range(HOLD + 1)]


def hotel(mults=None, g=0.03, exit_cap=0.09, tax=True) -> dict:
    mults = mults or [1] * 6
    rt = rates()
    b = basis()
    ln = loan()
    e0 = equity()
    nois = noi_path(mults, g)
    flows_pre = [-e0]
    flows_post = [-e0]
    taxes = []
    for t in range(HOLD):
        cf = nois[t] - ln["annual_ds"]
        dep = b["dep_total"]
        ti = nois[t] - ln["interest"][t] - dep
        tx = rt["ordinary"] * ti if tax else 0.0
        taxes.append(tx)
        flows_pre.append(cf)
        flows_post.append(cf - tx)
    gross = nois[HOLD] / exit_cap
    net_sale = gross * (1 - SELL)
    dep_taken = HOLD * b["dep_total"]
    dep_bldg = HOLD * b["dep_building"]
    adj_basis = b["total"] - dep_taken
    gain = net_sale - adj_basis
    if gain >= 0:
        unrecap = min(gain, dep_bldg)
        cg = gain - unrecap
        sale_tax = rt["unrecap_1250"] * unrecap + rt["ltcg"] * cg
    else:
        unrecap, cg = 0.0, gain
        sale_tax = rt["ltcg"] * gain
    if not tax:
        sale_tax = 0.0
    reversion_pre = net_sale - ln["balance_end"]
    flows_pre[-1] += reversion_pre
    flows_post[-1] += reversion_pre - sale_tax
    min_cf = min(flows_pre[1:HOLD]) if HOLD > 1 else 0.0
    cum, run = 0.0, 0.0
    for f in flows_pre[1:HOLD]:
        run += f
        cum = min(cum, run)
    return {"nois": nois, "flows_pre": flows_pre, "flows_post": flows_post, "taxes": taxes,
            "gross_sale": gross, "net_sale": net_sale, "adj_basis": adj_basis, "gain": gain,
            "unrecap_1250": unrecap, "cap_gain": cg, "sale_tax": sale_tax,
            "irr_pre": tvm.irr(flows_pre), "irr_post": tvm.irr(flows_post),
            "multiple_post": tvm.equity_multiple(flows_post), "max_cum_shortfall": -cum,
            "dscr1": nois[0] / ln["annual_ds"], "min_cf": min_cf}


def treasury(amount=None, y=TSY_YIELD, state_rate=0.0) -> dict:
    amount = equity() if amount is None else amount
    t = T_ORD + NIIT + state_rate
    pre = [-amount] + [amount * y] * HOLD
    pre[-1] += amount
    post = [-amount] + [amount * y * (1 - t)] * HOLD
    post[-1] += amount
    return {"pre": pre, "post": post, "irr_pre": tvm.irr(pre), "irr_post": tvm.irr(post),
            "after_tax_yield": y * (1 - t)}


def scenario_table() -> dict:
    out = {}
    for k, (p, mults, g, xc) in SCENARIOS.items():
        h = hotel(mults, g, xc)
        out[k] = {"p": p, **h}
    exp_irr = sum(v["p"] * v["irr_post"] for v in out.values())
    exp_flows = [sum(v["p"] * v["flows_post"][t] for v in out.values()) for t in range(HOLD + 1)]
    exp_pre = sum(v["p"] * v["irr_pre"] for v in out.values())
    return {"rows": out, "expected_irr_post": exp_irr, "irr_of_expected_post": tvm.irr(exp_flows),
            "expected_irr_pre": exp_pre, "p_loss": sum(v["p"] for v in out.values() if v["irr_post"] < 0),
            "expected_flows_post": exp_flows}


def inflation_case() -> dict:
    mults, g, xc, cpi = INFLATION_CASE
    h = hotel(mults, g, xc)
    tr = treasury()
    real = lambda r: (1 + r) / (1 + cpi) - 1  # noqa: E731
    return {"hotel_post": h["irr_post"], "hotel_real": real(h["irr_post"]),
            "tsy_post": tr["irr_post"], "tsy_real": real(tr["irr_post"]),
            "tsy_real_base_cpi": (1 + tr["irr_post"]) / (1 + CPI) - 1}


def duration_comparison() -> dict:
    d_t = fi.modified_duration(TSY_YIELD, TSY_YIELD, 5, freq=2)
    c0 = NOI1 / PRICE
    v1 = cre.direct_cap_value(NOI1, c0 + 0.01)
    e0 = PRICE - loan()["amount"]
    e1 = v1 - loan()["amount"]
    return {"tsy_mod_duration": d_t, "tsy_change_100bp": -d_t * 0.01, "going_in_cap": c0,
            "value_after": v1, "asset_change": v1 / PRICE - 1, "equity_change": e1 / e0 - 1}


def state_tax_illustration(corp_yield=0.046) -> dict:
    """Why the Treasury state exemption matters outside Texas (hypothetical 6% state rate)."""
    fed = T_ORD + NIIT
    tsy_tx = TSY_YIELD * (1 - fed)                       # Texas, or any state: Treasury exempt from state tax
    corp_tx = corp_yield * (1 - fed)                    # Texas: no state tax on either
    tsy_other = TSY_YIELD * (1 - fed)                   # exempt from the 6% state tax
    corp_other = corp_yield * (1 - fed - HYPO_STATE_RATE)  # ignores federal deductibility of state tax (SALT cap)
    be_corp = TSY_YIELD * (1 - fed) / (1 - fed - HYPO_STATE_RATE)
    return {"tx_tsy": tsy_tx, "tx_corp": corp_tx, "other_tsy": tsy_other, "other_corp": corp_other,
            "breakeven_corp_yield_other": be_corp}


def breakeven_exit_cap(target_post_irr: float) -> float:
    """Base-case exit cap at which the hotel's after-tax IRR equals ``target_post_irr``."""
    lo, hi = 0.06, 0.16
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if hotel(exit_cap=mid)["irr_post"] > target_post_irr:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def summary() -> dict:
    base = hotel()
    tr = treasury()
    st = scenario_table()
    return {"equity": equity(), "base_pre": base["irr_pre"], "base_post": base["irr_post"],
            "tsy_pre": tr["irr_pre"], "tsy_post": tr["irr_post"],
            "expected_post": st["expected_irr_post"], "irr_expected_flows": st["irr_of_expected_post"]}


if __name__ == "__main__":
    print(rates())
    print(basis())
    ln = loan()
    print({k: v for k, v in ln.items()})
    print("equity", equity())
    h = hotel()
    for k, v in h.items():
        print(k, v)
    print(treasury())
    st = scenario_table()
    for k, v in st["rows"].items():
        print(k, round(v["irr_pre"], 4), round(v["irr_post"], 4), round(v["gain"]), round(v["sale_tax"]),
              round(v["max_cum_shortfall"]), [round(x) for x in v["flows_post"]])
    print({k: v for k, v in st.items() if k != "rows"})
    print(inflation_case())
    print(duration_comparison())
    print(state_tax_illustration())
    print(hotel(tax=False)["irr_post"])
    print("be cap", breakeven_exit_cap(treasury()["irr_post"] + 0.04), breakeven_exit_cap(treasury()["irr_post"]))
    print(summary())
