"""Case H numbers as stated in case_H.md and case_H_rubric.md."""

import importlib.util
from pathlib import Path

import pytest

from sdesk import cre, fixed_income as fi, markets as mk, tvm

R = pytest.approx
_P = Path(__file__).resolve().parents[1] / "cases/hypothetical/case_H_cross_asset_macro_shock/case_h_model.py"
_spec = importlib.util.spec_from_file_location("case_h_model", _P)
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)


def test_treasuries():
    t = m.treasuries()
    t10, t2 = t["t10"], t["t2"]
    assert round(t10["dv01"]) == 48_468 and round(t2["dv01"]) == 7_625
    assert round(t10["pnl"]) == -864_928 and round(t2["pnl"]) == -190_040
    assert round(t10["dv01_approx_pnl"]) == -872_418 and round(t2["dv01_approx_pnl"]) == -190_618
    assert round(t10["dv01_approx_pnl"] - t10["pnl"]) == -7_490
    assert t2["pnl"] - t2["dv01_approx_pnl"] == R(577, abs=1)
    assert (round(t10["mod_duration"], 3), round(t2["mod_duration"], 3)) == (8.078, 1.906)
    assert round(t["total"]) == -1_054_969 and round(t["dv01_total"]) == 56_092
    assert t10["dv01"] / t["dv01_total"] == R(0.864, abs=1e-3)
    assert t10["dv01"] / t2["dv01"] > 6
    # independent check: DV01 ~ D_mod x P x 0.0001 for a par bond
    assert t10["dv01"] == R(t10["mod_duration"] * 60e6 * 1e-4, rel=1e-4)
    # convexity term reproduces the gap between duration estimate and reprice
    approx = fi.price_change_approx(60e6, t10["mod_duration"], t10["convexity"], 0.0018)
    assert approx["total"] == R(t10["pnl"], abs=50)


def test_es_futures():
    e = m.equity_futures()
    assert e["notional"] == R(15_000_000)
    assert e["pnl"] == R(-375_000)
    assert e["pct"] == R(-0.025)
    assert e["pnl_if_250_multiplier"] == R(-1_875_000)
    assert e["pnl_if_250_multiplier"] - e["pnl"] == R(-1_500_000)
    assert mk.futures_pnl_ticks(-600, 12.50, 50) == R(-375_000)   # 150 points = 600 ticks of $12.50


def test_fx_translation():
    f = m.fx_translation()
    assert f["usd0"] == R(27_500_000) and f["usd1"] == R(26_680_500)
    assert f["pnl"] == R(-819_500)
    assert f["local_effect"] == R(-550_000) and f["fx_effect"] == R(-269_500)
    assert f["local_effect"] + f["fx_effect"] == R(f["pnl"])
    assert f["usd_return"] == R(-0.0298)
    assert f["hedge_pnl"] == R(275_000) and f["hedged_pnl"] == R(-544_500)
    assert f["hedged_pnl"] - f["local_effect"] == R(5_500)
    assert f["wrong_usd0"] == R(22_727_273, abs=1)
    assert f["usd0"] - f["wrong_usd0"] == R(4_772_727, abs=1)


def test_credit():
    c = m.credit()
    ig, hy = c["ig"], c["hy"]
    assert (round(ig["mod_duration"], 3), round(hy["mod_duration"], 3)) == (6.502, 4.106)
    assert (round(ig["rate_loss"]), round(ig["spread_loss"]), round(ig["full_reprice"])) == (-500_667, -273_091, -763_638)
    assert (round(hy["rate_loss"]), round(hy["spread_loss"]), round(hy["full_reprice"])) == (-135_511, -246_384, -376_033)
    assert round(ig["duration_total"]) == -773_759 and round(hy["duration_total"]) == -381_895
    assert round(c["total"]) == -1_139_671 and round(c["spread_only"]) == -519_475


def test_day_one():
    d = m.day_one()
    assert round(d["total"]) == -3_389_139
    assert d["pct_nav"] == R(-0.0085, abs=5e-5)
    assert all(v < 0 for v in d["lines"].values())


def test_hotel_floating():
    h = m.hotel_floating()
    assert round(h["value"]) == 65_714_286 and round(h["ltv"], 3) == 0.730
    assert (round(h["interest0"]), round(h["interest1"]), round(h["interest_at_cap"])) == (3_528_333, 3_650_000, 3_844_667)
    assert (round(h["dscr0"], 3), round(h["dscr1"], 3), round(h["dscr_at_cap"], 3)) == (1.304, 1.260, 1.196)
    assert round(h["delta_interest"]) == 121_667
    assert round(h["per_bp_annual"]) == 4_867
    assert h["sofr_trap"] == R(0.044767, abs=1e-6)
    assert h["sofr_trap"] < m.HOTEL["cap_strike"]
    assert h["noi_trap"] == R(4_380_000) and h["noi_cushion_pct"] == R(0.0478, abs=1e-4)
    assert h["wrong_360_interest1"] == R(3_600_000)
    assert h["interest1"] - h["wrong_360_interest1"] == R(50_000)
    # independent: interest at the trap SOFR gives exactly 1.20x
    i_trap = m.HOTEL["loan"] * (h["sofr_trap"] + m.HOTEL["spread"]) * 365 / 360
    assert m.HOTEL["noi"] / i_trap == R(1.20)


def test_mf_refi():
    r = m.mf_refi()
    assert (r["r0"], r["r1"]) == (R(0.059), R(0.0623))
    assert (round(r["k0"], 6), round(r["k1"], 6)) == (0.071176, 0.07373)
    s0, s1 = r["sized0"], r["sized1"]
    assert s0["binding"] == s1["binding"] == "dscr"
    assert (s0["ltv"], s0["debt_yield"]) == (R(39_000_000), R(44_000_000))
    assert (round(s0["max_loan"]), round(s1["max_loan"])) == (37_090_956, 35_806_299)
    assert round(r["proceeds_change"]) == -1_284_656
    assert (round(r["gap0"]), round(r["gap1"])) == (5_329_044, 6_613_701)
    assert r["gap1"] / r["gap0"] - 1 == R(0.241, abs=1e-3)
    assert round(r["dscr_full_balance_r1"], 3) == 1.066
    assert round(r["proceeds_loss_10y_part"]) == 709_491
    assert round(r["proceeds_loss_spread_part"]) == 575_165
    assert round(r["proceeds_per_bp"]) == 40_014
    assert r["hedge_face"] == R(49_534_842, abs=1)
    assert round(r["hedge_pnl"]) == 714_068
    # independent check: DS at max loan is exactly NOI/1.25
    ds = tvm.annual_debt_service(s1["max_loan"], r["r1"], 30)
    assert m.MF["noi"] / ds == R(1.25)


def test_private_value_path():
    p = m.private_value_path()
    assert p["c1"] == R(0.0565)
    assert round(p["v1"]) == 58_407_080 and p["pct"] == R(-0.02655, abs=1e-5)
    assert [round(a) for a in p["appraisal_path"]] == [59_442_478, 59_080_088, 58_844_535, 58_691_426]
    decline = p["v0"] - p["v1"]
    shares = [(p["v0"] - a) / decline for a in p["appraisal_path"]]
    assert [100 * s for s in shares] == [R(35.0, abs=0.05), R(57.75, abs=0.05), R(72.5, abs=0.05), R(82.1, abs=0.05)]  # 1-(0.65)^n
    assert p["remaining_after_4q"] == R(0.1785, abs=1e-4)
    assert p["appraisal_path"][0] / p["v0"] - 1 == R(-0.0093, abs=1e-4)
    assert p["appraisal_path"][-1] / p["v0"] - 1 == R(-0.0218, abs=1e-4)
    assert p["bid_ask_gap_pct"] == R(0.0273, abs=1e-4)
    # closed form: unrecognized share after n quarters = (1 - alpha)^n
    assert p["remaining_after_4q"] == R((1 - m.APPRAISAL_ALPHA) ** 4)
    # negative leverage: going-in yield below shocked coupon
    assert p["c1"] < m.mf_refi()["r1"]


def test_rubric_sensitivity():
    # pass-through 1.0: cap 5.50% + 18 bp + 6 bp = 5.74%
    assert cre.cap_rate_shock_pct(0.055, 0.0574) == R(-0.0418, abs=1e-4)
    assert m.mf_refi()["gap1"] / m.NAV == R(0.0165, abs=1e-4)
