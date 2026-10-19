"""Case B — The Refinancing Cliff. Reproducible model.

Run:  python3 cases/hypothetical/case_B_refinancing_cliff/case_b_model.py
All inputs are hypothetical [HYPOTHESIS]. Every number quoted in case_B.md and
case_B_rubric.md is produced here and asserted in tests/test_case_b.py.

Timeline: t = -5 origination of the maturing loan; t = 0 maturity (decision date);
t = 1..3 the three-year horizon over which every strategy is evaluated. Annual
cash flows at year-end. Property value at t = 3 is forward NOI / exit cap.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "models" / "python"))

from sdesk import cre, tvm  # noqa: E402

# ----------------------------------------------------------------- inputs
RSF = 185_000
PURCHASE_PRICE = 46_000_000
PURCHASE_CLOSING_PCT = 0.02
NOI_AT_PURCHASE = 2_990_000            # after replacement reserves; 6.50% going-in cap
OLD_LOAN = 30_000_000                  # 5-year fixed, interest-only
OLD_RATE = 0.0340
LP_SHARE, GP_SHARE = 0.90, 0.10
HIST_DISTRIBUTIONS = [1_450_000, 1_400_000, 1_100_000, 700_000, 350_000]   # t = -4 .. 0

# Today (t = 0)
OCCUPANCY_NOW = 0.82
OCCUPANCY_AT_PURCHASE = 0.93
NOI_NOW = 2_350_000                    # after replacement reserves
TILC_PER_SF = 2.00                     # normalized leasing capital the lender deducts
MARKET_CAP = 0.0825                    # on NOI
SELL_COST = 0.02

# New senior loan market (hypothetical quotes)
NEW = dict(rate=0.0675, amort=30, ltv=0.60, dscr=1.35, debt_yield=0.10)
REFI_COST_PCT = 0.015

# Strategy parameters
EXT = dict(paydown=3_000_000, fee_pct=0.005, rate=0.0575, years=3)
DPO_PRICE = 24_000_000
DPO_LEGAL = 250_000
DIL_LEGAL = 150_000
LENDER_FORECLOSURE_COST = 0.07         # legal, carry, broker on an REO exit (fraction of value)
LENDER_RATE = 0.0675                   # lender's opportunity rate (new-loan rate)
EQUITY_RATE = 0.15                     # sponsor/LP required return on new equity
NOTE_BUYER_RATE = 0.12
REO_BUYER_RATE = 0.10                  # distressed buyer's unlevered target return
AM_FEE = 0.01                          # GP asset-management fee on contributed equity, per year
HURDLES, SPLITS = [0.08, 0.12], [1.0, 0.8, 0.7]

# Three-year property states (NCF after all leasing capital, by year; forward NOI at t=3; exit cap)
STATES = {
    "Recovery": dict(p=0.30, ncf=[1_550_000, 1_850_000, 2_350_000], noi_fwd=2_900_000, cap=0.0750),
    "Base": dict(p=0.45, ncf=[1_700_000, 1_800_000, 1_950_000], noi_fwd=2_500_000, cap=0.0800),
    "Downside": dict(p=0.25, ncf=[1_450_000, 1_250_000, 1_100_000], noi_fwd=1_950_000, cap=0.0900),
}


# ----------------------------------------------------------------- building blocks
def equity_at_purchase() -> float:
    return PURCHASE_PRICE * (1 + PURCHASE_CLOSING_PCT) - OLD_LOAN


def current_position() -> dict:
    ncf = NOI_NOW - TILC_PER_SF * RSF
    value = cre.direct_cap_value(NOI_NOW, MARKET_CAP)
    old_ds = tvm.annual_debt_service(OLD_LOAN, OLD_RATE, None)
    new_k = tvm.loan_constant(NEW["rate"], NEW["amort"])
    return {"ncf": ncf, "tilc": TILC_PER_SF * RSF, "value": value, "value_psf": value / RSF,
            "ltv": OLD_LOAN / value, "equity_mark": value - OLD_LOAN,
            "net_sale": value * (1 - SELL_COST), "short_sale_gap": OLD_LOAN - value * (1 - SELL_COST),
            "old_ds": old_ds, "old_dscr": ncf / old_ds, "old_dy": ncf / OLD_LOAN,
            "dscr_old_balance_new_terms": ncf / (OLD_LOAN * new_k), "new_k": new_k,
            "value_at_purchase_psf": PURCHASE_PRICE / RSF}


def new_loan() -> dict:
    c = current_position()
    sized = cre.max_loan(noi=c["ncf"], value=c["value"], annual_rate=NEW["rate"], amort_years=NEW["amort"],
                         ltv_max=NEW["ltv"], dscr_min=NEW["dscr"], debt_yield_min=NEW["debt_yield"])
    L = sized["max_loan"]
    ds = tvm.annual_debt_service(L, NEW["rate"], NEW["amort"])
    return {**sized, "loan": L, "ds": ds, "dscr_actual": c["ncf"] / ds, "dy_actual": c["ncf"] / L,
            "costs": REFI_COST_PCT * L,
            "equity_to_refi": cre.refinance_gap(OLD_LOAN, L, REFI_COST_PCT * L),
            "balance_t3": tvm.loan_balance(L, NEW["rate"], NEW["amort"], 36)}


def gap_attribution() -> list[tuple[str, float]]:
    """Walk from the original loan to today's proceeds, one change at a time (LTV-constrained path)."""
    v0 = PURCHASE_PRICE
    v_noi = NOI_NOW / (NOI_AT_PURCHASE / PURCHASE_PRICE)    # NOI decline at the original cap
    v_now = current_position()["value"]
    steps = [("Original loan", OLD_LOAN),
             ("65% of original value", 0.65 * v0),
             ("NOI decline at original 6.50% cap (65% LTV)", 0.65 * v_noi),
             ("Cap rate 6.50% -> 8.25% (65% LTV)", 0.65 * v_now),
             ("LTV limit 65% -> 60%", NEW["ltv"] * v_now)]
    return steps


def state_value(s: dict) -> dict:
    gross = s["noi_fwd"] / s["cap"]
    return {"gross": gross, "net": gross * (1 - SELL_COST)}


# ----------------------------------------------------------------- strategies
def strategy_refinance(dpo: bool = False) -> dict:
    """Pay off (or DPO) the old loan with the new senior loan plus fresh equity."""
    nl = new_loan()
    L, ds = nl["loan"], nl["ds"]
    payoff = DPO_PRICE if dpo else OLD_LOAN
    legal = DPO_LEGAL if dpo else 0.0
    eq_in = payoff + nl["costs"] + legal - L
    out = {"equity_in": eq_in, "states": {}}
    for name, s in STATES.items():
        sv = state_value(s)
        flows = [-eq_in] + [n - ds for n in s["ncf"]]
        terminal = max(sv["net"] - nl["balance_t3"], 0.0)
        flows[-1] += terminal
        out["states"][name] = {"flows": flows, "terminal_equity": terminal,
                               "npv": tvm.npv(EQUITY_RATE, flows), "net_sale": sv["net"]}
    out["enpv"] = sum(STATES[k]["p"] * v["npv"] for k, v in out["states"].items())
    out["lender_pv"] = payoff
    return out


def strategy_extension(paydown: float | None = None, rate: float | None = None) -> dict:
    """Three-year extension: paydown at t=0, fee, IO at the modified rate, full cash sweep to principal.

    Sponsor funds any interest shortfall. At t=3 the loan is repaid from a sale or refinance if
    net value exceeds the balance; otherwise the sponsor hands back the keys and the lender
    recovers value net of LENDER_FORECLOSURE_COST.
    """
    pd = EXT["paydown"] if paydown is None else paydown
    r = EXT["rate"] if rate is None else rate
    bal0 = OLD_LOAN - pd
    fee = EXT["fee_pct"] * bal0
    out = {"balance_after_paydown": bal0, "fee": fee, "equity_in": pd + fee, "states": {}}
    for name, s in STATES.items():
        bal = bal0
        spons = [-(pd + fee)]
        lend = [pd + fee]
        for ncf in s["ncf"]:
            interest = bal * r
            excess = ncf - interest
            if excess >= 0:
                sweep = min(excess, bal)
                bal -= sweep
                spons.append(excess - sweep)
                lend.append(interest + sweep)
            else:
                spons.append(excess)           # sponsor funds the shortfall
                lend.append(interest)
        sv = state_value(s)
        if sv["net"] >= bal:
            spons[-1] += sv["net"] - bal
            lend[-1] += bal
            keys = False
        else:
            lend[-1] += sv["gross"] * (1 - LENDER_FORECLOSURE_COST)
            keys = True
        out["states"][name] = {"sponsor_flows": spons, "lender_flows": lend, "balance_t3": bal,
                               "keys_at_t3": keys, "npv": tvm.npv(EQUITY_RATE, spons),
                               "lender_pv": tvm.npv(LENDER_RATE, lend)}
    out["enpv"] = sum(STATES[k]["p"] * v["npv"] for k, v in out["states"].items())
    out["lender_pv"] = sum(STATES[k]["p"] * v["lender_pv"] for k, v in out["states"].items())
    out["option_value_t0"] = sum(STATES[k]["p"] * max(state_value(STATES[k])["net"] - v["balance_t3"], 0)
                                 for k, v in out["states"].items()) / (1 + EQUITY_RATE) ** 3
    return out


def strategy_keys() -> dict:
    """Deed-in-lieu now. Lender owns for one year, collects expected NCF, sells at today's value net of costs."""
    c = current_position()
    e_ncf1 = sum(s["p"] * s["ncf"][0] for s in STATES.values())
    lender_cash_t1 = e_ncf1 + c["value"] * (1 - LENDER_FORECLOSURE_COST)
    return {"sponsor_npv": -DIL_LEGAL, "e_ncf1": e_ncf1, "lender_cash_t1": lender_cash_t1,
            "lender_pv": lender_cash_t1 / (1 + LENDER_RATE)}


def strategy_sale() -> dict:
    """Sale now at market value. Sponsor must fund the shortfall unless the lender accepts a short payoff."""
    c = current_position()
    return {"net_sale": c["net_sale"], "sponsor_check": c["short_sale_gap"],
            "sponsor_npv_full_payoff": -c["short_sale_gap"], "lender_pv_short_sale": c["net_sale"]}


def summary() -> dict:
    ref = strategy_refinance()
    dpo = strategy_refinance(dpo=True)
    ext = strategy_extension()
    keys = strategy_keys()
    sale = strategy_sale()
    return {
        "Refinance with fresh equity": {"sponsor_enpv": ref["enpv"], "equity_in": ref["equity_in"],
                                        "lender_pv": ref["lender_pv"]},
        "Extension / modification": {"sponsor_enpv": ext["enpv"], "equity_in": ext["equity_in"],
                                     "lender_pv": ext["lender_pv"]},
        "Discounted payoff": {"sponsor_enpv": dpo["enpv"], "equity_in": dpo["equity_in"],
                              "lender_pv": dpo["lender_pv"]},
        "Hand back the keys": {"sponsor_enpv": keys["sponsor_npv"], "equity_in": DIL_LEGAL,
                               "lender_pv": keys["lender_pv"]},
        "Sale (pay shortfall)": {"sponsor_enpv": sale["sponsor_npv_full_payoff"],
                                 "equity_in": sale["sponsor_check"], "lender_pv": OLD_LOAN},
        "Short sale (lender consents)": {"sponsor_enpv": 0.0, "equity_in": 0.0,
                                         "lender_pv": sale["lender_pv_short_sale"]},
    }


# ----------------------------------------------------------------- bargaining
def dpo_range() -> dict:
    """DPO prices acceptable to both sides.

    Sponsor: refinance-after-DPO NPV >= 0 (its alternative, keys, is about zero).
    Lender: DPO >= PV of its best alternative (keys or extension).
    """
    ref = strategy_refinance(dpo=True)
    # NPV is linear in the DPO price with slope -1 (equity in rises dollar for dollar)
    sponsor_max = DPO_PRICE + ref["enpv"]
    lender_min = max(strategy_keys()["lender_pv"], strategy_extension()["lender_pv"])
    return {"sponsor_max_dpo": sponsor_max, "lender_min_dpo": lender_min,
            "zone_exists": sponsor_max >= lender_min}


def lender_extension_pv_by_paydown(paydowns=(0, 1_000_000, 2_000_000, 3_000_000, 4_000_000)) -> dict:
    return {pd: strategy_extension(paydown=pd)["lender_pv"] for pd in paydowns}


def negotiation_tree(p_ext: float = 0.65, p_dpo: float = 0.10, p_foreclose: float = 0.25) -> dict:
    """Sponsor's expected NPV if it opens with a DPO request and falls back to the extension or keys."""
    ev = (p_ext * strategy_extension()["enpv"] + p_dpo * strategy_refinance(dpo=True)["enpv"]
          + p_foreclose * strategy_keys()["sponsor_npv"])
    lender = (p_ext * strategy_extension()["lender_pv"] + p_dpo * DPO_PRICE
              + p_foreclose * strategy_keys()["lender_pv"])
    return {"sponsor_ev": ev, "lender_ev": lender}


def extension_breakeven_paydown(lo: float = 0.0, hi: float = 10_000_000.0) -> float:
    """Paydown at which the sponsor's extension NPV is zero (bisection)."""
    f = lambda x: strategy_extension(paydown=x)["enpv"]
    if f(lo) < 0:
        return 0.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ----------------------------------------------------------------- sponsor incentives
def history_flows() -> list[float]:
    return [-equity_at_purchase()] + HIST_DISTRIBUTIONS


def promote_by_strategy() -> dict:
    """GP promote over the whole life of the deal if the strategy is followed, per state.

    Life-of-deal equity flows: t=-5 contribution, t=-4..0 distributions, t=0 new money, t=1..3.
    """
    hist = history_flows()
    out = {}
    for label, strat in (("refinance", strategy_refinance()), ("extension", strategy_extension()),
                         ("dpo", strategy_refinance(dpo=True))):
        per = {}
        for name, s in strat["states"].items():
            fl = s.get("flows") or s.get("sponsor_flows")
            life = hist[:-1] + [hist[-1] + fl[0]] + fl[1:]
            try:
                w = cre.irr_hurdle_waterfall(life, HURDLES, SPLITS)
                promote = sum(w["promote"])
            except ValueError:
                # cre.irr_hurdle_waterfall computes the promote, then raises when the
                # investor flows have no IRR on its search interval (here: the final flow
                # is negative and total distributions are below contributions). With
                # cumulative cash below capital no hurdle can be met, so the promote is 0.
                assert sum(life) < 0
                promote = 0.0
            try:
                irr = tvm.irr(life)
            except ValueError:
                irr = None
            per[name] = {"promote": promote, "deal_irr": irr}
        out[label] = per
    return out


def irr_to_date_if_keys() -> float:
    """Life-of-deal equity IRR if the keys are handed back today (no terminal equity)."""
    return tvm.irr(history_flows())


def gp_economics() -> dict:
    """GP's private payoff: 10% co-invest share of NPV plus PV of AM fees if the asset is retained."""
    fee = AM_FEE * equity_at_purchase()
    fee_pv = fee * tvm.annuity_factor(EQUITY_RATE, 3)
    ext, ref, dpo = strategy_extension(), strategy_refinance(), strategy_refinance(dpo=True)
    return {"am_fee": fee, "am_fee_pv": fee_pv,
            "gp_ext": GP_SHARE * ext["enpv"] + fee_pv, "lp_ext": LP_SHARE * ext["enpv"],
            "gp_ref": GP_SHARE * ref["enpv"] + fee_pv, "lp_ref": LP_SHARE * ref["enpv"],
            "gp_dpo": GP_SHARE * dpo["enpv"] + fee_pv, "lp_dpo": LP_SHARE * dpo["enpv"]}


# ----------------------------------------------------------------- distressed values
def distressed_property_value() -> dict:
    """Unlevered value to an REO buyer at REO_BUYER_RATE, on expected NCF and expected net sale at t=3."""
    e_ncf = [sum(s["p"] * s["ncf"][t] for s in STATES.values()) for t in range(3)]
    e_sale = sum(s["p"] * state_value(s)["net"] for s in STATES.values())
    flows = [0.0] + e_ncf
    flows[-1] += e_sale
    v = tvm.npv(REO_BUYER_RATE, flows)
    return {"e_ncf": e_ncf, "e_net_sale": e_sale, "value": v, "psf": v / RSF,
            "discount_to_market": v / current_position()["value"] - 1}


def note_value(p_ext: float = 0.45, p_dpo: float = 0.20, p_keys: float = 0.35) -> dict:
    """Value of the defaulted senior note to a buyer at NOTE_BUYER_RATE, mixing resolution paths."""
    ext = strategy_extension()
    pv_ext = sum(STATES[k]["p"] * tvm.npv(NOTE_BUYER_RATE, v["lender_flows"]) for k, v in ext["states"].items())
    pv_dpo = DPO_PRICE / (1 + NOTE_BUYER_RATE) ** 0.5     # six months to negotiate and close
    k = strategy_keys()
    pv_keys = k["lender_cash_t1"] / (1 + NOTE_BUYER_RATE) ** 1
    v = p_ext * pv_ext + p_dpo * pv_dpo + p_keys * pv_keys
    return {"pv_ext": pv_ext, "pv_dpo": pv_dpo, "pv_keys": pv_keys, "value": v, "price_pct_par": v / OLD_LOAN}


def report() -> str:
    c, nl = current_position(), new_loan()
    L = ["Current: NCF {:,.0f} value {:,.0f} ({:,.0f}/sf) LTV {:.1%} equity mark {:,.0f}".format(
        c["ncf"], c["value"], c["value_psf"], c["ltv"], c["equity_mark"]),
        "Old DS {:,.0f} DSCR {:.2f} DY {:.2%}; old balance on new terms DSCR {:.2f}".format(
        c["old_ds"], c["old_dscr"], c["old_dy"], c["dscr_old_balance_new_terms"]),
        "New loan: LTV {:,.0f} DSCR {:,.0f} DY {:,.0f} -> {:,.0f} ({}) DS {:,.0f} DSCR {:.2f}; equity to refi {:,.0f}; bal t3 {:,.0f}".format(
        nl["ltv"], nl["dscr"], nl["debt_yield"], nl["loan"], nl["binding"], nl["ds"], c["ncf"] / nl["ds"],
        nl["equity_to_refi"], nl["balance_t3"])]
    for lab, v in gap_attribution():
        L.append(f"  {lab:<48s}{v:>14,.0f}")
    for k, s in STATES.items():
        sv = state_value(s)
        L.append(f"  {k:<9s} gross {sv['gross']:,.0f} net {sv['net']:,.0f}")
    for k, v in summary().items():
        L.append("{:<30s} sponsor E[NPV] {:>12,.0f} equity in {:>12,.0f} lender PV {:>12,.0f}".format(
            k, v["sponsor_enpv"], v["equity_in"], v["lender_pv"]))
    ext = strategy_extension()
    for k, v in ext["states"].items():
        L.append(f"  ext {k}: sponsor {[round(x) for x in v['sponsor_flows']]} lender {[round(x) for x in v['lender_flows']]} bal3 {v['balance_t3']:,.0f} keys {v['keys_at_t3']}")
    L.append("Extension option value at t0: {:,.0f}".format(ext["option_value_t0"]))
    L.append(str(dpo_range()))
    L.append(str({k: round(v) for k, v in lender_extension_pv_by_paydown().items()}))
    L.append(str(negotiation_tree()))
    L.append("Breakeven paydown: {:,.0f}".format(extension_breakeven_paydown()))
    L.append(str(promote_by_strategy()))
    L.append("IRR to date if keys: {:.2%}".format(irr_to_date_if_keys()))
    L.append(str(gp_economics()))
    L.append(str(distressed_property_value()))
    L.append(str(note_value()))
    return "\n".join(L)


if __name__ == "__main__":
    print(report())
