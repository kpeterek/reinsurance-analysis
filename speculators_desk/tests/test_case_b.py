"""Case B numbers as stated in case_B.md and case_B_rubric.md."""

import importlib.util
from pathlib import Path

import pytest

from sdesk import cre, tvm

R = pytest.approx
_P = Path(__file__).resolve().parents[1] / "cases/hypothetical/case_B_refinancing_cliff/case_b_model.py"
_spec = importlib.util.spec_from_file_location("case_b_model", _P)
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)


def test_facts():
    assert m.NOI_AT_PURCHASE / m.PURCHASE_PRICE == R(0.065)
    assert round(m.PURCHASE_PRICE / m.RSF) == 249
    assert m.equity_at_purchase() == R(16_920_000)
    assert m.AM_FEE * m.equity_at_purchase() == R(169_200)
    assert sum(s["p"] for s in m.STATES.values()) == R(1.0)
    assert m.report()  # model runs end to end


def test_cliff():
    c = m.current_position()
    assert c["ncf"] == R(1_980_000) and c["tilc"] == R(370_000)
    assert round(c["value"]) == 28_484_848 and round(c["value_psf"]) == 154
    assert round(c["ltv"], 3) == 1.053
    assert round(c["equity_mark"]) == -1_515_152
    assert c["old_ds"] == R(1_020_000)
    assert (round(c["old_dscr"], 2), round(c["old_dy"], 4)) == (1.94, 0.066)
    assert round(c["new_k"], 6) == 0.077832
    assert round(m.OLD_LOAN * c["new_k"]) == 2_334_953
    assert round(c["dscr_old_balance_new_terms"], 2) == 0.85


def test_new_loan():
    nl = m.new_loan()
    assert (round(nl["ltv"]), round(nl["dscr"]), round(nl["debt_yield"])) == (17_090_909, 18_844_061, 19_800_000)
    assert nl["binding"] == "ltv"
    assert round(nl["ds"]) == 1_330_216
    assert (round(nl["dscr_actual"], 2), round(nl["dy_actual"], 4)) == (1.49, 0.1159)
    assert round(nl["costs"]) == 256_364
    assert round(nl["equity_to_refi"]) == 13_165_455
    assert round(nl["equity_to_refi"] / m.equity_at_purchase(), 3) == 0.778
    assert round(nl["balance_t3"]) == 16_505_541
    # independent: retrospective balance formula
    i = m.NEW["rate"] / 12
    pmt = tvm.payment(nl["loan"], m.NEW["rate"], 30)
    assert nl["loan"] * (1 + i) ** 36 - pmt * ((1 + i) ** 36 - 1) / i == R(nl["balance_t3"])


def test_gap_attribution():
    g = dict(m.gap_attribution())
    vals = list(g.values())
    assert [round(v) for v in vals] == [30_000_000, 29_900_000, 23_500_000, 18_515_152, 17_090_909]
    diffs = [round(b - a) for a, b in zip(vals, vals[1:])]
    assert diffs == [-100_000, -6_400_000, -4_984_848, -1_424_242]
    total = vals[0] - vals[-1]
    assert round(total, -5) == 12_900_000
    assert [round(-d / total, 2) for d in diffs] == [0.01, 0.50, 0.39, 0.11]


def test_states():
    exp = {"Recovery": (38_666_667, 37_893_333), "Base": (31_250_000, 30_625_000),
           "Downside": (21_666_667, 21_233_333)}
    for k, (g, n) in exp.items():
        sv = m.state_value(m.STATES[k])
        assert (round(sv["gross"]), round(sv["net"])) == (g, n)


def test_strategies():
    ref = m.strategy_refinance()
    assert [round(v["npv"]) for v in ref["states"].values()] == [2_152_039, -2_797_387, -10_164_719]
    assert round(ref["enpv"]) == -3_154_392
    dpo = m.strategy_refinance(dpo=True)
    assert round(dpo["equity_in"]) == 7_415_455
    assert [round(v["npv"]) for v in dpo["states"].values()] == [7_902_039, 2_952_613, -4_414_719]
    assert round(dpo["enpv"]) == 2_595_608
    # DPO equity is refinance equity less (par - DPO) plus legal: NPVs differ by exactly that
    assert ref["enpv"] - dpo["enpv"] == R(-(30e6 - 24e6 - 250_000))
    ext = m.strategy_extension()
    assert ext["fee"] == R(135_000) and ext["equity_in"] == R(3_135_000)
    assert round(ext["enpv"]) == 395_066
    assert [round(v["npv"]) for v in ext["states"].values()] == [4_756_597, -209_591, -3_750_390]
    assert [round(v["lender_pv"]) for v in ext["states"].values()] == [29_425_631, 29_427_797, 23_792_168]
    assert round(ext["lender_pv"]) == 28_018_240
    s = ext["states"]
    assert [round(x) for x in s["Recovery"]["sponsor_flows"]] == [-3_135_000, -2_500, 0, 12_005_440]
    assert [round(x) for x in s["Base"]["sponsor_flows"]] == [-3_135_000, 0, 0, 4_449_181]
    assert [round(x) for x in s["Downside"]["sponsor_flows"]] == [-3_135_000, -102_500, -302_500, -452_500]
    assert [round(x) for x in s["Recovery"]["lender_flows"]] == [3_135_000, 1_552_500, 1_850_000, 28_237_894]
    assert [round(x) for x in s["Base"]["lender_flows"]] == [3_135_000, 1_700_000, 1_800_000, 28_125_819]
    assert [round(x) for x in s["Downside"]["lender_flows"]] == [3_135_000, 1_552_500, 1_552_500, 21_702_500]
    assert [round(v["balance_t3"]) for v in s.values()] == [25_887_894, 26_175_819, 27_000_000]
    assert [v["keys_at_t3"] for v in s.values()] == [False, False, True]
    # conservation in non-keys states: sponsor + lender flows = property flows
    for k in ("Recovery", "Base"):
        prop = [0] + m.STATES[k]["ncf"]
        prop[-1] += m.state_value(m.STATES[k])["net"]
        tot = [a + b for a, b in zip(s[k]["sponsor_flows"], s[k]["lender_flows"])]
        assert tot == [R(x) for x in prop]
    keys = m.strategy_keys()
    assert keys["e_ncf1"] == R(1_592_500)
    assert round(keys["lender_pv"]) == 26_307_643
    sale = m.strategy_sale()
    assert round(sale["net_sale"]) == 27_915_152 and round(sale["sponsor_check"]) == 2_084_848


def test_bargaining():
    s = m.summary()
    walk_s, walk_l = s["Hand back the keys"]["sponsor_enpv"], s["Hand back the keys"]["lender_pv"]
    both = [k for k, v in s.items() if v["sponsor_enpv"] > walk_s and v["lender_pv"] > walk_l]
    # extension and short sale beat both walk-aways; extension dominates the short sale
    assert set(both) == {"Extension / modification", "Short sale (lender consents)"}
    e, ss = s["Extension / modification"], s["Short sale (lender consents)"]
    assert e["sponsor_enpv"] > ss["sponsor_enpv"] and e["lender_pv"] > ss["lender_pv"]
    d = m.dpo_range()
    assert (round(d["sponsor_max_dpo"]), round(d["lender_min_dpo"]), d["zone_exists"]) == (26_595_608, 28_018_240, False)
    # sponsor's refinance-after-DPO NPV at its max price is zero
    old = m.DPO_PRICE
    try:
        m.DPO_PRICE = d["sponsor_max_dpo"]
        assert m.strategy_refinance(dpo=True)["enpv"] == R(0, abs=1e-6)
    finally:
        m.DPO_PRICE = old
    lp = m.lender_extension_pv_by_paydown()
    assert {k: round(v) for k, v in lp.items()} == {0: 27_335_392, 1_000_000: 27_562_877, 2_000_000: 27_790_558,
                                                   3_000_000: 28_018_240, 4_000_000: 28_246_210}
    assert lp[0] > walk_l
    bp = m.extension_breakeven_paydown()
    assert round(bp) == 4_042_682
    assert m.strategy_extension(paydown=bp)["enpv"] == R(0, abs=1e-3)
    n = m.negotiation_tree()
    assert (round(n["sponsor_ev"]), round(n["lender_ev"])) == (478_854, 27_188_767)


def test_option_and_incentives():
    ext = m.strategy_extension()
    assert round(ext["option_value_t0"]) == 3_684_565
    pr = m.promote_by_strategy()
    assert all(v["promote"] == 0 for strat in pr.values() for v in strat.values())
    assert round(pr["dpo"]["Recovery"]["deal_irr"], 4) == 0.0270
    assert pr["extension"]["Downside"]["deal_irr"] is None
    # library issue documented in the case: waterfall raises when investor flows have no IRR
    hist = m.history_flows()
    fl = ext["states"]["Downside"]["sponsor_flows"]
    life = hist[:-1] + [hist[-1] + fl[0]] + fl[1:]
    w = cre.irr_hurdle_waterfall(life, m.HURDLES, m.SPLITS)
    assert w["investor_irr"] is None
    assert sum(w["promote"]) == pytest.approx(0.0, abs=1e-6)
    assert round(m.irr_to_date_if_keys(), 4) == -0.3553
    g = m.gp_economics()
    assert round(g["am_fee_pv"]) == 386_322
    assert (round(g["lp_ref"]), round(g["gp_ref"])) == (-2_838_953, 70_882)
    assert (round(g["lp_ext"]), round(g["gp_ext"])) == (355_559, 425_828)
    assert (round(g["lp_dpo"]), round(g["gp_dpo"])) == (2_336_047, 645_882)
    assert round(3_135_000 / m.equity_at_purchase(), 3) == 0.185


def test_distressed_values():
    d = m.distressed_property_value()
    assert [round(x) for x in d["e_ncf"]] == [1_592_500, 1_677_500, 1_857_500]
    assert round(d["e_net_sale"]) == 30_457_583
    assert round(d["value"]) == 27_112_891 and round(d["psf"]) == 147
    assert round(d["discount_to_market"], 3) == -0.048
    n = m.note_value()
    assert (round(n["pv_ext"]), round(n["pv_dpo"]), round(n["pv_keys"])) == (24_878_341, 22_677_868, 25_074_472)
    assert round(n["value"]) == 24_506_892 and round(n["price_pct_par"], 3) == 0.817
    assert round(30e6 - n["value"], -5) == 5_500_000
