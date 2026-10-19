"""Case E numbers as stated in case_E.md and case_E_rubric.md."""

import importlib.util
from pathlib import Path

import pytest

from sdesk import tvm

R = pytest.approx
_P = Path(__file__).resolve().parents[1] / "cases/hypothetical/case_E_distressed_office/case_e_model.py"
_spec = importlib.util.spec_from_file_location("case_e_model", _P)
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)

TABLES = {
    "Recovery": [
        (6_894_400, 894_200, 5_408_000, 592_200, 3_072_000, 666_264, 7_800_000, -10_946_064),
        (8_384_108, 1_813_452, 5_564_000, 1_006_656, 5_954_000, 1_335_733, 5_200_000, -11_483_077),
        (10_718_431, 1_786_096, 5_792_800, 3_139_535, 5_678_800, 1_313_129, 0, -3_852_394),
        (13_143_523, 1_521_713, 6_011_200, 5_610_610, 4_670_000, 1_114_024, 0, -173_415),
        (15_442_207, 1_335_210, 6_198_400, 7_908_597, 3_994_000, 980_293, 0, 2_934_304),
        (17_216_611, 478_239, 6_323_200, 10_415_172, 1_352_000, 344_332, 0, 8_718_840),
        (18_366_435, 246_293, 6_385_600, 11_734_542, 676_000, 177_331, 0, 10_881_211)],
    "Grind": [
        (6_540_800, 481_667, 5_366_400, 692_733, 1_720_000, 369_240, 7_800_000, -9_196_507),
        (7_028_800, 1_141_833, 5_418_400, 468_567, 3_926_000, 851_292, 5_200_000, -9_508_725),
        (8_138_400, 1_271_033, 5_543_200, 1_324_167, 4_326_800, 940_726, 0, -3_943_359),
        (9_413_800, 1_083_183, 5_688_800, 2_641_817, 3_656_000, 796_722, 0, -1_810_905),
        (10_593_000, 980_050, 5_824_000, 3_788_950, 3_318_000, 722_466, 0, -251_516),
        (11_580_400, 515_667, 5_938_400, 5_126_333, 1_690_000, 371_280, 0, 3_065_053),
        (12_199_200, 206_267, 6_011_200, 5_981_733, 676_000, 148_512, 0, 5_157_221)],
    "Structural": [
        (6_187_200, 124_667, 5_324_800, 737_733, 550_000, 112_200, 7_800_000, -7_724_467),
        (5_747_748, 507_342, 5_272_800, -32_394, 1_898_000, 393_583, 5_200_000, -7_523_978),
        (5_770_518, 718_052, 5_283_200, -230_734, 2_636_800, 541_315, 0, -3_408_849),
        (6_164_994, 637_520, 5_335_200, 192_274, 2_304_000, 475_013, 0, -2_586_739),
        (6_648_804, 637_520, 5_397_600, 613_684, 2_304_000, 475_013, 0, -2_165_329),
        (7_142_808, 294_116, 5_460_000, 1_388_693, 1_014_000, 211_763, 0, 162_929),
        (7_562_974, 196_077, 5_512_000, 1_854_897, 676_000, 141_176, 0, 1_037_721)],
}


def test_replacement_cost_and_rent():
    assert m.REPLACEMENT_COST_PSF * m.RSF == 249_600_000
    assert m.ASK / m.RSF == R(100.0)
    assert round(m.replacement_cost_rent(), 2) == 64.00
    opex = 6.5 * 520_000 + 4.0 * 468_000 + 0.02 * 249_600_000 + 0.3 * 520_000
    assert opex == R(10_400_000)
    assert (0.07 * 249_600_000 + opex + 2_080_000) / 468_000 == R(64.0)
    assert round(34 / 64, 2) == 0.53


def test_annual_tables():
    for name, rows in TABLES.items():
        out = m.scenario_cash_flows(name)["rows"]
        for exp, row in zip(rows, out):
            got = (row["revenue"], row["free_rent"], row["opex"] + row["reserve"], row["noi"], row["ti"],
                   row["lc"], row["capex"], row["cash_flow"])
            assert tuple(round(x) for x in got) == exp, (name, row["year"])


def test_year1_hand_check():
    r = m.scenario_cash_flows("Recovery")["rows"][0]
    assert (197_600 + 157_600) / 2 == 177_600
    assert 177_600 * 33 + 30_400 * 34 == R(r["revenue"])
    assert r["new_sf"] == R(38_800) and r["renewal_sf"] == R(22_000)
    assert 38_800 * 65 + 22_000 * 25 == R(r["ti"])
    assert m.ASK * 1.015 == R(52_780_000)
    assert 0.02 * m.ASK == R(1_040_000)


def test_exits_and_returns():
    pf = m.portfolio()
    exp = {"Recovery": (12_728_470, 154_284_479, 151_198_790, 0.1310, 94_498_194, 2.19),
           "Grind": (6_344_000, 66_778_947, 65_443_368, -0.0080, -3_825_369, 0.95),
           "Structural": (2_198_240, 17_985_597, 17_625_885, -0.2062, -57_362_825, 0.25)}
    for n, (enoi, gx, nx, irr, prof, mult) in exp.items():
        s = pf["by_scenario"][n]
        assert (round(s["exit_noi"]), round(s["gross_exit"]), round(s["net_exit"])) == (enoi, gx, nx)
        assert round(s["irr"], 4) == irr and round(s["profit"]) == prof and round(s["multiple"], 2) == mult
    assert round(pf["expected_profit"]) == 22_119_692
    assert round(pf["sd_profit"]) == 62_533_414
    assert pf["p_loss"] == R(0.60)
    assert round(pf["mean_irr"], 4) == -0.0019
    assert round(pf["irr_of_expected"], 4) == 0.0403


def test_peak_capital():
    def peak(n):
        cum, lo = 0.0, 0.0
        for f in m.scenario_cash_flows(n)["flows"]:
            cum += f
            lo = min(lo, cum)
        return lo
    assert round(peak("Recovery")) == -79_234_950
    assert round(-peak("Grind") / 1e6, 1) == 77.5 and round(-peak("Structural") / 1e6, 1) == 76.2


def test_max_price_and_sensitivities():
    mp = m.max_price()
    assert round(mp) == 29_175_730 and round(mp / m.RSF, 2) == 56.11
    pf = m.portfolio(mp)
    assert pf["irr_of_expected"] == R(0.12, abs=1e-6)
    assert [round(pf["by_scenario"][n]["irr"], 4) for n in m.SCENARIOS] == [0.2135, 0.0704, -0.1228]
    assert pf["p_loss"] == R(0.25)
    p0 = {"Recovery": 40 / 75, "Grind": 35 / 75, "Structural": 0.0}
    p5 = {"Recovery": 0.5 * 40 / 75, "Grind": 0.5 * 35 / 75, "Structural": 0.5}
    assert round(m.with_probs(p0, m.max_price) / 1e6, 2) == 38.99
    assert round(m.with_probs(p5, m.max_price) / 1e6, 2) == 19.24
    assert round(m.with_globals({"TI_NEW": 85.0}, m.max_price) / 1e6, 2) == 26.21
    assert round(m.with_globals({"TI_NEW": 85.0}, lambda: m.portfolio()["irr_of_expected"]), 4) == 0.0306
    assert round(m.with_globals({"FIXED_OPEX_PSF": 7.5}, m.max_price) / 1e6, 2) == 25.17
    assert round(m.with_exit_cap_shift(0.01, m.max_price) / 1e6, 2) == 25.55
    assert round(m.with_exit_cap_shift(0.01, lambda: m.portfolio()["irr_of_expected"]), 4) == 0.0248
    # inputs restored
    assert m.TI_NEW == 65.0 and m.SCENARIOS["Grind"]["exit_cap"] == 0.095


def test_structural_breakeven():
    npv = m.npv_by_scenario()
    assert round(npv["Recovery"] / 1e6, 2) == 4.84 and round(npv["Grind"] / 1e6, 2) == -39.18
    assert m.structural_breakeven_probability() == 0.0
    q = m.structural_breakeven_probability(30e6)
    assert round(q, 3) == 0.229
    assert round(m.portfolio(30e6)["irr_of_expected"], 4) == 0.1164
    # independent check of the break-even: EV at q is zero
    n30 = m.npv_by_scenario(30e6)
    gbar = (0.40 * n30["Recovery"] + 0.35 * n30["Grind"]) / 0.75
    assert (1 - q) * gbar + q * n30["Structural"] == R(0.0, abs=1e-3)


def test_bridge_loan():
    b = m.bridge_loan_test()
    assert round(b["loan"]) == 28_600_000 and round(b["annual_interest"]) == 2_359_500
    exp = {"Recovery": (3_139_535, 34_883_722, 0), "Grind": (1_324_167, 14_712_963, 13_887_037),
           "Structural": (-230_734, 0, 28_600_000)}
    for n, (noi3, sup, pay) in exp.items():
        assert (round(b[n]["noi3"]), round(b[n]["supportable"]), round(b[n]["paydown"])) == (noi3, sup, pay)
    assert round(-m.carry_through_year3("Grind")["unlevered"] / 1e6, 1) == 22.6
    assert round(-m.carry_through_year3("Structural")["unlevered"] / 1e6, 1) == 18.7
    assert round(-m.carry_through_year3("Recovery")["unlevered"] / 1e6, 1) == 26.3
    assert round(3 * b["annual_interest"] / 1e6, 1) == 7.1


def test_conversion():
    c = m.conversion_feasibility()
    assert c["nrsf"] == R(313_600) and round(c["units"]) == 402
    assert (round(c["gpr"]), round(c["egi"]), round(c["noi"]), round(c["gdv"])) == \
        (9_219_840, 8_574_451, 5_316_160, 88_602_662)
    assert round(c["net_value"]) == 86_830_609
    assert (c["hard"], round(c["soft"])) == (R(134_400_000), 24_192_000)
    assert round(c["non_land_cost"]) == 170_592_000
    assert round(c["land_value"]) == -95_087_122
    assert c["net_value"] / 1.15 - 170_592_000 == R(c["land_value"])
    assert round(m.conversion_feasibility(hard_psf=150.0)["land_value"] / 1e6, 1) == -35.6
    assert round(m.conversion_breakeven_rent(0.0), 2) == 5.54
    assert round(m.conversion_breakeven_rent(), 2) == 7.22
    assert round(7.22 / 2.45, 1) == 2.9
    assert round(c["gdv"] / (c["non_land_cost"]), 2) == 0.52


def test_irr_matches_library_on_flows():
    f = m.scenario_cash_flows("Recovery")["flows"]
    assert tvm.npv(m.scenario_cash_flows("Recovery")["irr"], f) == R(0.0, abs=1e-3)
    assert len(f) == 8
