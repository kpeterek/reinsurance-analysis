"""Case J numbers as stated in case_J.md and case_J_rubric.md.

Where possible each figure is checked by an independent route (closed form,
reverse calculation, or hand-built cash flows) rather than by calling the
model function a second time.
"""

import csv
import importlib.util
from pathlib import Path

import pytest

from sdesk import cre, hotel, tvm

R = pytest.approx
ROOT = Path(__file__).resolve().parents[1]
_P = ROOT / "cases/hypothetical/case_J_credit_crunch_hotel/case_j_model.py"
_spec = importlib.util.spec_from_file_location("case_j_model", _P)
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)

N = 1_889_561.2


# ------------------------------------------------------------------ B.1 operating profile
def test_operating_statement():
    o = m.operating_statement()
    assert o["rooms_revenue"] == R(40_790 * 154.00)
    assert o["total_revenue"] == 6_801_660
    assert o["gop"] == 3_231_660
    assert round(o["gop_margin"], 3) == 0.475
    assert round(o["mgmt_fee"]) == 204_050
    assert round(o["franchise_fee"]) == 690_983
    assert round(o["ebitda_before_tax"]) == 2_161_628
    assert round(o["ffe_reserve"]) == 272_066
    assert round(o["noi_before_tax"]) == 1_889_561
    assert round(o["occupancy"], 4) == 0.7450
    assert round(o["revpar"], 2) == 114.73
    # NOI-vs-EBITDA trap: the reserve is 4% of TOTAL revenue, not rooms revenue
    assert o["ebitda_before_tax"] - o["noi_before_tax"] == R(0.04 * 6_801_660)
    assert round(m.N_PRE_CRUNCH - o["noi_before_tax"]) == 45_439
    assert round(o["noi_before_tax"] / m.N_PRE_CRUNCH - 1, 4) == -0.0235
    assert m.T_TAX == R(0.0168)


# ------------------------------------------------------------------ B.2 durability
def test_penetration_and_dataset():
    rows = list(csv.DictReader((ROOT / "cases/datasets/case_j_str_comp.csv").open()))
    assert len(rows) == len(m.STR)
    for r, (label, so, sa, co, ca) in zip(rows, m.STR):
        assert r["period"] == label
        assert (float(r["subject_occ"]), float(r["subject_adr"]), float(r["comp_occ"]), float(r["comp_adr"])) == (so, sa, co, ca)
    h = m.penetration_history()
    assert [round(x["rgi"], 1) for x in h] == [110.3, 111.9, 114.0]
    assert [round(x["mpi"], 1) for x in h] == [106.5, 108.2, 109.6]
    assert [round(x["ari"], 1) for x in h] == [103.5, 103.4, 104.1]
    assert [round(x["subject_revpar"], 2) for x in h] == [107.31, 114.30, 114.73]
    assert abs(h[1]["comp_revpar"] - 102.17) < 0.006       # 102.165 exactly
    assert round(h[2]["comp_revpar"], 2) == 100.64
    assert round(h[2]["subject_revpar"] / h[1]["subject_revpar"] - 1, 4) == 0.0037
    assert round(h[2]["comp_revpar"] / h[1]["comp_revpar"] - 1, 4) == -0.0149
    # independent: RGI = MPI x ARI / 100
    for x in h:
        assert x["rgi"] == R(x["mpi"] * x["ari"] / 100)


def test_supply():
    s = m.supply_test()
    assert s["market_rooms"] == 1_090
    assert round(s["supply_growth"], 4) == 0.0881
    assert round(s["demand_cum"], 4) == 0.0506
    assert round(s["occ_factor"], 4) == 0.9656
    assert round(s["lost_rooms_revenue"]) == 216_197
    assert round(s["noi_hit"]) == 129_718
    assert round(s["noi_hit_pct"], 4) == 0.0686
    assert round(s["supply_growth_all"], 4) == 0.1982
    assert round(s["occ_factor_all"], 4) == 0.8769
    assert round(s["noi_hit_all"]) == 464_108
    assert round(s["noi_hit_all_pct"], 4) == 0.2456


# ------------------------------------------------------------------ B.3 marginal buyers
def test_loan_constants():
    exp = {0.065: 0.081025, 0.07: 0.084814, 0.0825: 0.094614, 0.0975: 0.106936}
    for r, k in exp.items():
        assert round(tvm.loan_constant(r, 25), 6) == k
    # independent: 12 x PMT on $1
    i = 0.0825 / 12
    assert 12 * i / (1 - (1 + i) ** -300) == R(0.0946140, abs=1e-6)


def test_regime_table():
    rt = m.regime_table()
    exp_n = {"Lodging REIT": 19_001_990, "Owner-operator": 18_911_969, "Opportunity fund": 18_254_036,
             "Family-office cash buyer": 14_778_325}
    exp_c = {"Lodging REIT": 18_555_774, "Owner-operator": 17_142_561, "Opportunity fund": 15_981_461,
             "Family-office cash buyer": 14_778_325}
    for name, v in exp_n.items():
        assert round(rt["normal"]["rows"][name]["max_price"]) == v
    for name, v in exp_c.items():
        assert round(rt["crunch"]["rows"][name]["max_price"]) == v
    assert round(rt["normal"]["clearing"]) == 18_911_969 and rt["normal"]["marginal_buyer"] == "Owner-operator"
    assert round(rt["crunch"]["clearing"]) == 15_981_461 and rt["crunch"]["marginal_buyer"] == "Opportunity fund"
    assert rt["crunch"]["top"][0] == "Owner-operator"
    assert round(rt["normal"]["rows"]["Owner-operator"]["per_key"]) == 126_080
    assert round(rt["crunch"]["rows"]["Opportunity fund"]["per_key"]) == 106_543
    oo_n, oo_c = rt["normal"]["rows"]["Owner-operator"], rt["crunch"]["rows"]["Owner-operator"]
    assert round(oo_n["loan"]) == 12_292_780 and round(oo_n["equity"]) == 6_902_869
    assert round(oo_c["loan"]) == 7_714_152 and round(oo_c["equity"]) == 9_685_547
    assert round(oo_c["equity"] / oo_n["equity"] - 1, 2) == 0.40
    f_n, f_c = rt["normal"]["rows"]["Opportunity fund"], rt["crunch"]["rows"]["Opportunity fund"]
    assert round(f_n["loan"]) == 12_777_825 and round(f_n["equity"]) == 5_750_021
    assert round(f_c["loan"]) == 7_990_730 and round(f_c["equity"]) == 8_230_452
    assert round(rt["normal"]["rows"]["Lodging REIT"]["equity"]) == 19_287_020
    for regime in ("normal", "crunch"):
        for name in ("Owner-operator", "Opportunity fund"):
            assert rt[regime]["rows"][name]["binding"] == "ltv"
    caps = {(r, n): round(rt[r]["rows"][n]["going_in_cap"], 4) for r in ("normal", "crunch") for n in exp_n}
    assert caps[("normal", "Owner-operator")] == 0.0855 and caps[("normal", "Opportunity fund")] == 0.0892
    assert caps[("normal", "Lodging REIT")] == 0.0850 and caps[("normal", "Family-office cash buyer")] == 0.1141
    assert caps[("crunch", "Owner-operator")] == 0.0934 and caps[("crunch", "Opportunity fund")] == 0.1014
    assert caps[("crunch", "Family-office cash buyer")] == 0.1111
    # capacity: $15.0m / 1.015
    fo = rt["crunch"]["rows"]["Family-office cash buyer"]
    assert fo["capacity_binds"] and fo["max_price"] == R(15_000_000 / 1.015, abs=1)
    assert round(fo["price_return"], -4) == 17_560_000


def test_band_of_investment_closed_form_and_k_minus_y():
    b = m.BUYERS["Owner-operator"]
    # closed form equals the bisection price (LTV binding)
    p_n = m.N_PRE_CRUNCH / (0.0168 + 0.65 * tvm.loan_constant(0.065, 25) + 0.09 * (1.015 - 0.65))
    assert round(p_n) == 18_911_969
    assert m.coc_price_closed_form(N, 0.09, b["crunch"]) == R(17_142_561, abs=1)
    # reverse check: cash-on-cash at that price is exactly 9%
    cf = m.buyer_cash_flows(17_142_561.034, N, b["crunch"])
    assert cf["coc"] == R(0.09, abs=1e-8)
    # at crunch rates, 65% LTV supports LESS than 45% LTV (K > y)
    p65 = m.coc_price_closed_form(N, 0.09, {**b["crunch"], "ltv": 0.65})
    assert round(p65) == 17_000_237
    assert p65 < 17_142_561
    # at normal rates, cutting LTV lowers the price (K < y)
    assert m.coc_price_closed_form(N, 0.09, {**b["crunch"], "rate": 0.065}) == R(18_149_454, abs=1)
    lc = m.leverage_check()
    assert round(lc["normal"]["spread"], 4) == 0.0045
    assert round(lc["crunch"]["spread"], 4) == -0.0012


def test_opportunity_fund_irr_reverse():
    cf = m.buyer_cash_flows(18_254_036.4041, m.N_PRE_CRUNCH, m.BUYERS["Opportunity fund"]["normal"])
    assert tvm.irr(cf["flows"]) == R(0.16, abs=1e-7)
    # independent reversion: year-6 NOI before tax / (exit cap + t) x (1 - 2%)
    shock = -m.supply_test()["noi_hit_pct"]
    n6 = m.N_PRE_CRUNCH * 1.03 ** 5 * (1 + shock)
    assert cf["reversion"] == R(n6 / (0.085 + 0.0168) * 0.98)


# ------------------------------------------------------------------ B.4 decomposition
def test_decomposition():
    d = m.decomposition()
    a = d["order_a"]
    assert (round(a["fundamentals"]), round(a["proceeds"]), round(a["rate"]), round(a["universe"])) == \
        (-444_102, -318_413, -1_006_893, -1_161_100)
    steps = d["steps"]
    assert [round(v) for v in steps.values()] == [18_911_969, 18_467_867, 18_149_454, 17_142_561, 15_981_461]
    assert round(d["total"]) == -2_930_508
    assert round(d["total_pct"], 3) == -0.155
    assert round(d["order_b"]["financing"]) == -2_546_197
    assert round(d["order_b"]["fundamentals"]) == -384_311
    assert round(d["fundamentals_share_a"], 3) == 0.152
    assert round(d["fundamentals_share_b"], 3) == 0.131
    shares = [round(a[k] / d["total"], 3) for k in ("fundamentals", "proceeds", "rate", "universe")]
    assert shares == [0.152, 0.109, 0.344, 0.396]
    assert sum(a[k] for k in ("fundamentals", "proceeds", "rate", "universe")) == R(d["total"])


# ------------------------------------------------------------------ B.5 seller certainty
def test_seller_certainty_equivalent():
    s = m.seller_certainty_equivalent()
    assert round(s["fallback_pv"]) == 15_378_168
    assert s["fallback_pv"] == R(15_981_461 / 1.08 ** 0.5, abs=1)
    assert round(s["ev_financed"]) == 16_525_023
    assert round(s["discount_vs_financed"]) == 617_538


# ------------------------------------------------------------------ B.6 all-cash with refinance
def test_client_all_cash():
    ca = m.client_analysis()
    sc = ca["scenarios"]
    exp = {"Credit returns in 1 year": (0.1721, 1.46, 7_698_442, 1_390_813, 12_025_056),
           "Credit returns in 2 years": (0.1504, 1.50, 8_359_398, 851_149, 12_385_808),
           "Credit returns in 4 years": (0.1274, 1.59, 9_859_301, -142_861, 13_140_104),
           "Credit shut through exit": (0.1017, 1.52, 8_690_580, -1_695_074, None),
           "Impairment": (0.0790, 1.39, 6_500_331, -2_958_274, None)}
    for k, (irr, em, prof, npv, loan) in exp.items():
        v = sc[k]
        assert (round(v["irr"], 4), round(v["multiple"], 2), round(v["profit"]), round(v["npv_at_target"])) == \
            (irr, em, prof, npv)
        if loan:
            assert round(v["refi"]["loan"]) == loan and v["refi"]["binding"] == "ltv"
            assert round(v["refi"]["dscr"], 2) == 1.57
    assert sum(v["p"] for v in sc.values()) == R(1.0)
    r1 = sc["Credit returns in 1 year"]["refi"]
    assert round(r1["appraised"]) == 18_500_087
    assert round(r1["debt_service"]) == 974_329
    assert round(r1["net_proceeds"]) == 11_904_806
    # independent: appraisal = year-2 NOI after the UNREASSESSED tax bill / 8.25%
    shock = -m.supply_test()["noi_hit_pct"]
    noi2 = N * 1.03 * (1 + shock) - 0.0168 * 16_550_000 * 1.03
    assert r1["appraised"] == R(noi2 / 0.0825)
    assert sc["Credit returns in 1 year"]["flows"][0] == R(-16_798_250)
    assert round(0.0168 * 16_550_000) == 278_040
    assert round((N - 278_040) / 16_550_000, 4) == 0.0974
    assert round(ca["expected_irr"], 4) == 0.1379
    flows = [sum(v["p"] * v["flows"][i] for v in sc.values()) for i in range(6)]
    assert round(tvm.irr(flows), 4) == 0.1308
    assert round(ca["expected_npv"]) == 37_911
    assert tvm.npv(0.13, flows) == R(ca["expected_npv"])       # linearity of NPV
    assert ca["p_loss"] == 0
    assert round(ca["timing_cost_irr"], 4) == 0.0447
    assert round(ca["timing_cost_npv"]) == 1_533_674
    assert round(ca["timing_cost_profit"]) == -2_160_859


def test_client_prices_and_breakeven():
    p_npv = m.client_max_price()
    p_irr = m.client_max_price("irr")
    assert round(p_npv) == 16_584_807
    assert round(p_irr) == 16_857_793
    assert round(p_irr - p_npv) == 272_986
    naive = m.naive_max_price()
    assert round(naive) == 17_815_454
    assert round(naive - p_npv, -4) == 1_230_000
    q = m.breakeven_impairment_probability()
    assert round(q, 3) == 0.264
    # reverse check: rescale scenarios with impairment prob q -> expected IRR = 13%
    sc = m.client_analysis()["scenarios"]
    others = {k: v for k, v in sc.items() if k != "Impairment"}
    w = sum(v["p"] for v in others.values())
    e = q * sc["Impairment"]["irr"] + (1 - q) * sum(v["p"] * v["irr"] for v in others.values()) / w
    assert e == R(0.13)
    assert round(16_550_000 - 16_525_023) == 24_977
    assert round(p_npv - 16_550_000) == 34_807
    # Mode B: shifting 10 points from "1 year" to "shut" lowers the maximum to $16.30m
    old = dict(m.SCENARIOS)
    try:
        m.SCENARIOS["Credit returns in 1 year"] = (0.20, 1, m.UC_SHOCK, "normal")
        m.SCENARIOS["Credit shut through exit"] = (0.20, None, m.UC_SHOCK, "crunch")
        assert round(m.client_max_price(), -4) == 16_300_000
    finally:
        m.SCENARIOS.clear()
        m.SCENARIOS.update(old)


# ------------------------------------------------------------------ B.7 seller financing
def test_seller_financing():
    s = m.seller_financing()
    assert round(s["price"]) == 18_129_408
    assert round(s["bank_loan"]) == 8_158_233
    assert round(s["note"]) == 3_625_882
    assert round(s["equity"]) == 6_617_234
    assert round(s["noi1"]) == 1_584_987
    assert round(s["bank_ds"]) == 771_883
    assert round(s["note_interest"]) == 217_553
    assert round(s["dscr_total"], 2) == 1.60
    assert s["coc"] == R(0.09)
    assert s["bank_binding"] == "ltv"
    # independent note PV: 5-year annuity + balloon at 11%
    note = s["note"]
    pv = 0.06 * note * (1 - 1.11 ** -5) / 0.11 + note / 1.11 ** 5
    assert pv == R(s["pv_note"])
    assert round(s["pv_note"]) == 2_955_837
    assert round(s["note_discount"]) == 670_044
    assert round(s["seller_cash_equivalent"]) == 17_459_363


# ------------------------------------------------------------------ B.8 assumable debt
def test_assumable_debt():
    a = m.assumable_debt()
    assert round(a["balance"]) == 11_686_551
    assert round(a["monthly_payment"], 2) == 73_073.76
    assert round(a["annual_ds"]) == 876_885
    assert a["remaining_months"] == 84
    assert round(a["balloon"]) == 9_240_559
    assert round(a["pv_at_market"]) == 9_848_087
    assert round(a["mtm_gain"]) == 1_838_464
    assert round(a["fee"]) == 116_866
    # independent: balance = PV of remaining payments at the CONTRACT rate (rate-as-loan identity)
    i = 0.05 / 12
    pv_contract = a["monthly_payment"] * (1 - (1 + i) ** -84) / i + a["balloon"] / (1 + i) ** 84
    assert pv_contract == R(a["balance"])
    # schedule cross-check
    sched = tvm.amortization_schedule(12_500_000, 0.05, 25, periods=120)
    assert sched[35]["end"] == R(a["balance"])
    assert sched[119]["end"] == R(a["balloon"])
    # owner-operator price with assumption (rubric Mode D context)
    assert round(a["price"]) == 18_991_658
    assert round(a["ltv"], 3) == 0.615
    assert round(a["dscr"], 2) == 1.79
    assert round(a["debt_yield"], 3) == 0.134


def test_client_assumption():
    aa = m.client_assumption_analysis(17_600_000)
    sc = aa["scenarios"]
    for k in ("Credit returns in 1 year", "Credit returns in 2 years", "Credit returns in 4 years"):
        assert round(sc[k]["irr"], 4) == 0.1840
        assert round(sc[k]["npv_at_target"]) == 1_381_898
    assert round(sc["Credit shut through exit"]["irr"], 4) == 0.1392
    assert round(sc["Credit shut through exit"]["npv_at_target"]) == 216_136
    assert round(sc["Impairment"]["irr"], 4) == 0.0815
    assert round(sc["Impairment"]["npv_at_target"]) == -1_047_064
    assert round(sc["Impairment"]["equity"]) == 6_294_314
    assert round(sc["Impairment"]["dscr_y1"], 2) == 1.82
    assert round(aa["expected_irr"], 4) == 0.1641
    assert round(aa["expected_npv"]) == 900_978
    assert round(m.client_assumption_max_price()) == 18_436_335
    assert round(m.client_assumption_max_price(0.15)) == 17_957_636
    assert m.CLIENT_TARGET_IRR == 0.13          # restored after the 15% run
    assert round(11_686_551 / 17_600_000, 2) == 0.66


def test_seller_options_and_rubric():
    so = m.seller_options()
    assert round(so["financed_bid_ce"]) == 16_525_023
    assert round(so["seller_note_ce"]) == 17_459_363
    assert round(so["assumption_ce"]) == 17_442_500
    assert round(so["assumption_ce"] - so["financed_bid_ce"]) == 917_477
    # rubric Mode D
    s = m.supply_test()
    x = m.client_scenario(16_550_000, 1, -s["noi_hit_all_pct"], "normal")
    assert round(x["irr"], 4) == 0.0707
    assert round(x["npv_at_target"]) == -2_011_932
    a17 = m.client_analysis(17_200_000)
    assert round(a17["expected_npv"]) == -670_054
    assert round(a17["expected_irr"], 4) == 0.1215
    se = m.seller_certainty_equivalent()
    assert round(0.65 * so["seller_note_ce"] + 0.35 * se["fallback_pv"]) == 16_730_945
    assert round(0.70 * 17_600_000 + 0.30 * 16_550_000) == 17_285_000
    assert round(16_798_250 - 11_904_806) == 4_893_444
    assert round(16_798_250 / 25_000_000, 2) == 0.67


def test_boundaries():
    # zero leverage: the band-of-investment price collapses to N / (t + y(1+c))
    p0 = m.coc_price_closed_form(N, 0.09, {"rate": 0.065, "ltv": 0.0})
    assert p0 == R(N / (0.0168 + 0.09 * 1.015))
    # if K == y, LTV has no effect on the cash-on-cash price
    k = tvm.loan_constant(0.0825, 25)
    a = N / (0.0168 + 0.45 * k + k * (1.015 - 0.45))
    b = N / (0.0168 + 0.65 * k + k * (1.015 - 0.65))
    assert a == R(b)
    # hotel.indices fair share
    assert hotel.indices(0.7, 150, 0.7, 150)["rgi"] == R(100)
    # cre.max_loan agrees with the LTV binding used for the owner-operator
    ml = cre.max_loan(noi=N - 0.0168 * 17_142_561, value=17_142_561, annual_rate=0.0825, amort_years=25,
                      ltv_max=0.45, dscr_min=1.5, debt_yield_min=0.13)
    assert ml["binding"] == "ltv" and ml["max_loan"] == R(0.45 * 17_142_561)


def test_drill_prose_numbers():
    """Numbers stated in the solution text of D131-D135 that are not graded parts."""
    e = [-10e6, 7.6e6, 0.3e6, 0.3e6, 0.3e6, 5.1e6]
    late = [-10e6, 0.9e6, 0.9e6, 0.9e6, 7.3e6, 5.0e6]
    ne, nl = tvm.npv(0.12, e), tvm.npv(0.12, late)
    assert round(ne) == 322_939 and round(nl) == -361_936
    assert round(ne - nl, -3) == 685_000
    assert round(0.6 * tvm.irr(e) + 0.4 * tvm.irr(late), 4) == 0.1254
    assert round(-nl / (ne - nl), 3) == 0.528
    assert (sum(e), sum(late)) == (3.6e6, 5.0e6)
    k_n, k_c = tvm.loan_constant(0.065, 25), tvm.loan_constant(0.0825, 25)
    assert round(0.65 * k_n + 0.35 * 0.09, 4) == 0.0842
    assert round(0.45 * k_c + 0.55 * 0.09, 4) == 0.0921
