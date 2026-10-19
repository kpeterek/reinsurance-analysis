"""Case F numbers as stated in case_F.md and case_F_rubric.md."""

import importlib.util
from pathlib import Path

import pytest

from sdesk import fixed_income as fi, tvm

R = pytest.approx
_P = Path(__file__).resolve().parents[1] / "cases/hypothetical/case_F_hotel_vs_treasury/case_f_model.py"


def _load():
    spec = importlib.util.spec_from_file_location("case_f_model", _P)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


m = _load()


def test_tax_rates_and_jurisdiction():
    r = m.rates()
    assert (r["ordinary"], r["ltcg"], r["unrecap_1250"]) == (R(0.408), R(0.238), R(0.288))
    assert m.STATE == 0.0  # Texas resident


def test_financing_and_basis():
    ln = m.loan()
    assert ln["amount"] == R(9_900_000)
    assert round(ln["monthly"], 2) == 69_971.14
    assert round(ln["annual_ds"]) == 839_654
    assert round(ln["balance_end"]) == 9_025_053
    assert ln["balance_end"] == R(ln["balance_check"])  # schedule vs closed form
    assert round(ln["annual_ds"] / 9.9e6, 4) == round(1.4e6 / 16.5e6, 4) == 0.0848
    b = m.basis()
    assert b["total"] == R(16_830_000)
    assert (b["land"], b["building"], b["ffe"]) == (R(2_524_500), R(12_622_500), R(1_683_000))
    assert (round(b["dep_building"]), round(b["dep_ffe"]), round(b["dep_total"])) == (323_654, 240_429, 564_082)
    assert m.equity() == R(6_930_000)
    assert round(m.hotel()["dscr1"], 2) == 1.67


def test_base_case():
    h = m.hotel()
    ln = m.loan()
    assert [round(x) for x in ln["interest"]] == [688_202, 677_254, 665_514, 652_925, 639_427]
    taxable = [h["nois"][t] - ln["interest"][t] - m.basis()["dep_total"] for t in range(5)]
    assert [round(x) for x in taxable] == [147_715, 200_664, 255_664, 312_810, 372_203]
    assert [round(x) for x in h["taxes"]] == [60_268, 81_871, 104_311, 127_627, 151_859]
    assert [round(x) for x in h["flows_pre"]] == [-6_930_000, 560_346, 602_346, 645_606, 690_164, 9_203_163]
    assert [round(x) for x in h["flows_post"]] == [-6_930_000, 500_078, 520_475, 541_295, 562_538, 8_141_539]
    assert round(h["nois"][5]) == 1_622_984
    assert (round(h["gross_sale"]), round(h["net_sale"])) == (18_033_152, 17_492_158)
    assert round(h["adj_basis"]) == 14_009_588
    assert (round(h["gain"]), round(h["unrecap_1250"]), round(h["cap_gain"])) == (3_482_570, 1_618_269, 1_864_301)
    assert round(h["sale_tax"]) == 909_765
    assert round(0.288 * 1_618_269.23 + 0.238 * 1_864_300.56) == 909_765
    assert (round(h["irr_pre"], 4), round(h["irr_post"], 4)) == (0.1263, 0.0927)
    assert round(h["multiple_post"], 2) == 1.48
    assert round(1 - h["irr_post"] / h["irr_pre"], 3) == 0.266
    assert round(h["irr_post"] / h["irr_pre"], 2) == 0.73
    # no-tax switch reproduces pre-tax IRR
    assert m.hotel(tax=False)["irr_post"] == R(h["irr_pre"])


def test_treasury():
    t = m.treasury()
    assert t["irr_pre"] == R(0.04, abs=1e-9)
    assert t["irr_post"] == R(0.02368, abs=1e-9)
    assert t["after_tax_yield"] == R(0.02368)
    h = m.hotel()
    assert round((h["irr_post"] - t["irr_post"]) * 1e4) == 690
    assert round((h["irr_pre"] - t["irr_pre"]) * 1e4) == 863
    assert round(690 / 863, 2) == 0.80
    assert round(6.93 / 8.0, 2) == 0.87
    assert round(sum(t["post"])) == 820_512


def test_scenarios():
    st = m.scenario_table()
    exp = {"Upside": (0.1867, 0.1433, 6_380_887, 1_599_565, 0),
           "Base": (0.1263, 0.0927, 3_482_570, 909_765, 0),
           "Downside": (0.0450, 0.0308, 946_207, 272_508, 0),
           "Severe": (-0.0639, -0.0446, -1_128_999, -268_702, 349_654)}
    for k, (pre, post, gain, tax, inj) in exp.items():
        v = st["rows"][k]
        assert (round(v["irr_pre"], 4), round(v["irr_post"], 4), round(v["gain"]), round(v["sale_tax"]),
                round(v["max_cum_shortfall"])) == (pre, post, gain, tax, inj)
    assert round(st["expected_irr_post"], 4) == 0.0736
    assert round(st["irr_of_expected_post"], 4) == 0.0779
    assert round(st["expected_irr_pre"], 4) == 0.0990
    assert st["p_loss"] == R(0.10)
    sev = st["rows"]["Severe"]
    assert round(sev["nois"][0]) == 490_000
    assert round(sev["nois"][0] / m.loan()["annual_ds"], 2) == 0.58
    assert round((0.0308 - 0.0237) * 1e4) == 71
    assert sum(v["p"] for v in st["rows"].values()) == R(1.0)
    profits = {k: sum(v["flows_post"]) for k, v in st["rows"].items()}
    assert round(profits["Severe"]) == -1_339_663 and round(profits["Downside"]) == 999_590
    tp = sum(m.treasury()["post"])
    shortfall = sum(v["p"] * max(0.0, tp - profits[k]) for k, v in st["rows"].items())
    assert round(shortfall) == 216_017


def test_breakevens():
    t = m.treasury()["irr_post"]
    assert round(m.breakeven_exit_cap(t), 4) == 0.1127
    assert round(m.breakeven_exit_cap(t + 0.04), 4) == 0.0988


def test_duration_and_inflation():
    d = m.duration_comparison()
    assert round(d["tsy_mod_duration"], 2) == 4.49
    assert d["tsy_mod_duration"] == R(fi.macaulay_duration(0.04, 0.04, 5) / 1.02)
    assert round(d["asset_change"], 4) == -0.1054
    assert round(d["equity_change"], 4) == -0.2636
    inf = m.inflation_case()
    assert (round(inf["hotel_post"], 4), round(inf["hotel_real"], 4)) == (0.0944, 0.0423)
    assert round(inf["tsy_real"], 4) == -0.0251
    assert round(inf["tsy_real_base_cpi"], 4) == -0.0013


def test_state_tax_illustration():
    s = m.state_tax_illustration()
    assert (round(s["tx_tsy"], 4), round(s["tx_corp"], 4)) == (0.0237, 0.0272)
    assert round(s["other_corp"], 4) == 0.0245
    assert round(s["breakeven_corp_yield_other"], 4) == 0.0445


def test_lower_leverage_variant():
    mod = _load()
    mod.LTV = 0.50
    assert mod.equity() == R(8_580_000)
    assert round(mod.hotel()["irr_post"], 4) == 0.0833
    assert round(mod.scenario_table()["expected_irr_post"], 4) == 0.0682
    sev = mod.SCENARIOS["Severe"]
    assert round(mod.hotel(sev[1], sev[2], sev[3])["max_cum_shortfall"], -4) == 210_000
    assert round(0.26 * 0.0736 + 0.74 * 0.0237, 3) == 0.037
    assert round(1 - 0.408, 2) == 0.59


def test_irr_boundary():
    # an all-Treasury allocation with zero yield returns zero
    assert tvm.irr([-100, 0, 0, 0, 0, 100]) == R(0.0, abs=1e-9)
