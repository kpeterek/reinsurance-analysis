"""Case D numbers as stated in case_D.md and case_D_rubric.md (The Hotel PIP Negotiation)."""

import csv
import importlib.util
from pathlib import Path

import pytest

from sdesk import hotel, tvm

R = pytest.approx
ROOT = Path(__file__).resolve().parents[1]
_P = ROOT / "cases/hypothetical/case_D_hotel_pip_negotiation/case_d_model.py"
_spec = importlib.util.spec_from_file_location("case_d_model", _P)
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)


def test_datasets_match_model():
    rows = list(csv.DictReader((ROOT / "cases/datasets/case_d_pip_items.csv").open()))
    pip = [r for r in rows if r["category"] == "PIP"]
    deferred = [r for r in rows if r["category"] != "PIP"]
    assert [int(r["amount_usd"]) for r in pip] == [int(a) for _, _, a in m.PIP_ITEMS]
    assert sum(int(r["amount_usd"]) for r in deferred) == 410_000
    dem = list(csv.DictReader((ROOT / "cases/datasets/case_d_monthly_demand.csv").open()))
    assert [float(r["t12_occupancy"]) for r in dem] == m.MONTH_OCC
    avg = sum(float(r["t12_occupancy"]) * int(r["days"]) for r in dem) / 365
    assert round(avg, 3) == 0.735   # monthly profile is consistent with the T-12 occupancy


def test_t12_statement_and_indices():
    t = m.t12()
    assert round(t["rooms_sold"], 2) == 31_656.45
    assert round(t["revpar"], 2) == 107.31
    assert round(t["rooms_revenue"]) == 4_621_842
    assert round(t["total_revenue"]) == 4_760_497
    assert round(t["gop"]) == 2_299_889
    assert round(t["gop_margin"], 3) == 0.483
    assert round(t["franchise_fee"]) == 554_621
    assert round(t["ebitda"]) == 1_299_453
    assert round(t["ffe_reserve"]) == 190_420
    assert round(t["noi"]) == 1_109_033
    assert (round(t["mpi"], 1), round(t["ari"], 1), round(t["rgi"], 1)) == (102.1, 100.7, 102.8)
    assert round(t["owner_value"]) == 13_047_450
    assert round(t["owner_value_9_25"]) == 11_989_549
    assert sum(m.RGI_BY_QUARTER) / 4 == R(102.75)


def test_pip_budget():
    b = m.pip_budget()
    assert b["hard"] == 3_292_200 and b["hard_per_key"] == R(27_900)
    assert round(b["soft"]) == 263_376
    assert round(b["base"]) == 3_555_576 and round(b["per_key"]) == 30_132
    assert round(b["contingency"]) == 426_669
    assert round(b["all_in"]) == 3_982_245
    assert b["deferred"] == 410_000


def test_displacement_by_month():
    d = m.displacement(10)
    assert round(d["contrib_per_rn"], 2) == 90.09
    assert [r["month"] for r in d["rows"]] == ["Nov", "Dec", "Jan", "Feb", "Mar", "Apr"]
    assert [round(r["lost_rn"]) for r in d["rows"]] == [0, 0, 0, 0, 187, 158]
    assert [round(r["lost_noi"]) for r in d["rows"]] == [15_018, 12_895, 13_988, 14_214, 33_219, 29_979]
    assert round(d["lost_rn"]) == 345
    assert round(d["total"]) == 119_314
    d2 = m.displacement(2)
    assert [r["month"] for r in d2["rows"]] == ["Mar", "Apr", "May", "Jun", "Jul", "Aug"]
    assert [round(r["lost_rn"]) for r in d2["rows"]] == [187, 158, 139, 88, 43, 0]
    assert round(d2["lost_rn"]) == 615
    assert round(d2["total"]) == 150_707
    # hand check, March: weekday demand 0.80*1.15*118 = 108.56 vs 98 rooms open
    lost_mar = 31 * 4 / 7 * (0.80 * 1.15 * 118 - 98)
    assert lost_mar == R(d["rows"][4]["lost_rn"])


def test_stabilized_independent_and_ld():
    st = m.stabilized()
    assert round(st["adr"], 2) == 152.64 and round(st["revpar"], 2) == 114.48
    assert round(st["total_revenue"]) == 5_078_573
    assert round(st["noi"]) == 1_330_702
    assert round(st["value"]) == 15_208_026
    ind = m.independent()
    assert round(ind["adr"], 2) == 139.76 and round(ind["revpar"], 2) == 95.04
    assert round(ind["noi"]) == 826_048
    assert round(ind["value"]) == 8_472_290
    assert ind["capex"] == 1_058_000
    assert round(ind["net_value"]) == 7_004_290
    assert round(m.liquidated_damages()) == 785_713


def test_return_on_renovation():
    r = m.return_on_renovation()
    assert round(r["ft_noi"], 4) == 0.7869
    assert round(r["target_noi_gain"]) == 398_225
    assert round(r["d_revpar_needed"], 2) == 11.75
    assert round(r["revpar_needed"], 2) == 119.06
    assert round(r["pct_lift_needed"], 4) == 0.1095
    assert round(r["projected_lift"], 2) == 7.17
    assert round(r["projected_noi_gain"]) == 221_669
    assert round(r["yield_vs_t12"], 4) == 0.0557
    assert round(r["incr_capital_vs_independent"]) == 2_924_245
    assert round(r["incr_noi_vs_independent"]) == 504_654
    assert round(r["yield_vs_independent"], 4) == 0.1726
    # independent route for the needed lift: NOI gain / (rooms x 365 x flow-through)
    assert 0.10 * 3_982_245.12 / (118 * 365 * r["ft_noi"]) == R(r["d_revpar_needed"])


def test_price_bids_and_walk_away():
    p = m.price()
    assert round(p["pip_all_in"]) == 3_982_245
    assert round(p["required_profit"]) == 597_337
    assert round(p["displacement"]) == 119_314
    assert p["carry_soft_deferred"] == 560_000
    assert round(p["price"]) == 9_949_131
    assert round(p["price_per_key"]) == 84_315
    assert round(p["gap_to_ask"]) == 3_550_869
    assert round(p["implied_cap_t12"], 4) == 0.1115
    # independent check of the library function
    manual = 15_208_026.1161 - 3_982_245.12 - 119_313.7042 - 560_000 - 0.15 * 3_982_245.12
    assert p["price"] == R(manual, abs=1)
    w = m.walk_away_price()
    assert round(w["all_in"]) == 14_809_672 and round(w["yoc"], 4) == 0.0899
    assert round(w["spread_bp"], 1) == 23.5
    ob = m.opening_bid()
    assert round(ob["price"]) == 9_162_582 and round(ob["per_key"]) == 77_649
    assert round(ob["all_in"]) == 14_007_392 and ob["yoc"] == R(0.095)
    ask = m.yield_on_cost(m.OWNER_ASK)
    assert round(ask["all_in"]) == 18_431_559 and round(ask["yoc"], 4) == 0.0722
    assert round(ask["spread_bp"]) == -153
    assert ob["price"] < w["price"] < m.OWNER_ASK


def test_financing_structures():
    f = m.financing(m.price()["price"])
    assert round(f["total_cost"]) == 14_540_358
    assert round(f["ltc_loan"]) == 9_451_233
    assert round(f["dy_loan"]) == 10_562_222
    assert round(f["dscr_loan"]) == 11_018_274
    assert f["binding"] == "LTC"
    assert round(f["k"], 4) == 0.0895
    assert round(f["pip_loan"]) == 2_986_684
    assert round(f["s1_equity_close"]) == 5_089_125
    assert round(f["s1_reserve_carry"]) == 75_663
    assert round(f["s2_initial"]) == 6_464_549
    assert round(f["s2_equity_close"]) == 4_093_564
    assert round(f["s2_equity_pip"]) == 995_561
    assert f["s2_equity_total"] == R(f["s1_equity_close"])
    assert round(f["ltv_stab"], 4) == 0.6215
    assert round(f["dscr_asis"], 3) == 1.312 and round(f["dscr_stab"], 3) == 1.574
    assert f["k"] == R(tvm.loan_constant(0.076, 25))


def test_seller_position():
    s = m.seller_refi()
    assert round(s["dy_loan"]) == 10_562_222 and round(s["dscr_loan"]) == 9_182_845
    assert round(s["loan"]) == 9_182_845
    assert round(s["cash_out"]) == 1_645_102
    assert round(s["owner_check"]) == 2_337_143
    assert round(m.seller_net(m.price()["price"])) == 2_250_657
    assert round(m.seller_net(m.opening_bid()["price"])) == 1_487_705
    occs = m.held_occupancies()
    assert [round(o, 4) for o in occs] == [0.6936, 0.6793]
    h = m.owner_hold()
    assert [round(x) for x in h["nois"]] == [963_091, 912_656]
    assert round(h["y3"]) == -3_180_857
    assert round(h["sale"]) == 15_194_339
    assert round(h["pv"]) == 10_138_426
    d = m.owner_deflag()
    assert round(d["sale"]) == 8_464_664 and round(d["pv"]) == 7_155_519
    i = m.owner_indifference()
    assert round(i["sell"]) == 9_650_657
    assert round(i["p_star"], 3) == 0.836
    assert round(i["hold_gross_equivalent"]) == 10_451_986
    assert i["p_star"] * i["hold"] + (1 - i["p_star"]) * i["deflag"] == R(i["sell"])


def test_breakeven_occupancy_at_walk_away():
    """Mode D question: break-even occupancy at the walk-away price with the structure-1 loan."""
    f = m.financing(m.price()["price"])
    ds = f["loan"] * f["k"]
    o = m.OPEX
    fixed = o["undist_fixed"] + o["tax"] + o["ins"]
    var_pct = o["mgmt_pct"] + o["undist_pct"] + o["reserve_pct"] + o["franchise_pct"] / (1 + o["other_pct"])
    # other revenue carries its own departmental cost; fold it into an effective CPOR
    cpor = o["cpor"] + m.T12["adr"] * o["other_pct"] * o["other_dept_ratio"]
    be = hotel.breakeven_occupancy(m.ROOMS, m.T12["adr"], fixed, ds, cpor, var_pct,
                                   other_revenue_pct_of_rooms=o["other_pct"])
    be0 = hotel.breakeven_occupancy(m.ROOMS, m.T12["adr"], fixed, 0.0, cpor, var_pct,
                                    other_revenue_pct_of_rooms=o["other_pct"])
    assert round(ds) == 845_516
    assert round(be, 4) == 0.6603 and round(be0, 4) == 0.4205
    # check: the T-12 occupancy reproduces T-12 NOI under this linearization
    contrib = m.T12["adr"] * (1 + o["other_pct"]) * (1 - var_pct) - cpor
    noi = contrib * m.ROOMS * 365 * m.T12["occ"] - fixed
    assert noi == R(m.t12()["noi"], abs=1)
    assert round(var_pct, 4) == 0.2215 and round(cpor, 2) == 35.19 and round(contrib, 2) == 81.88


def test_mode_d_sensitivities():
    x = m.sensitivities()
    assert round(x["base"]) == 9_949_131
    assert round(x["exit_cap_plus_50bp"]) == 9_127_075 and round(x["d_exit"]) == -822_055
    assert round(x["pip_plus_20"]) == 9_033_214 and round(x["d_pip"]) == -915_916
    # independent: a 20% PIP increase costs 0.20 x base x 1.12 x 1.15
    assert x["d_pip"] == R(-0.20 * 3_555_576 * 1.12 * 1.15)
    assert round(x["rgi_102_noi"]) == 1_184_299 and round(x["rgi_102"]) == 8_275_951
    assert round(x["d_rgi"]) == -1_673_179
    assert round(x["schedule_saving"]) == 31_393
    assert round(x["ask_cap_t12"], 4) == 0.0822
    assert round(x["stab_value_per_key"]) == 128_882
    f = m.financing(x["base"])
    assert round(f["s1_equity_close"] / f["total_cost"], 4) == 0.35


def test_case_text_cross_checks():
    assert m.ROOMS * 365 == 43_070
    assert round(m.OWNER_ASK / m.ROOMS) == 114_407
    st, b = m.stabilized(), m.pip_budget()
    assert round(st["value"] - b["all_in"] - b["deferred"]) == 10_815_781
    assert round(0.80 * 1.15 * 118, 1) == 108.6 and round(0.80 * 0.80 * 118, 1) == 75.5
    assert round(m.price()["price"] + 410_000) == 10_359_131
    assert round(9_150_000 / 118) == 77_542
    assert round(0.735 - 0.6603, 3) == 0.075


def test_rubric_numbers():
    st = m.stabilized()
    assert round(st["noi"] / 0.0925) == 14_385_971
    assert round(m.owner_hold()["pv"] / 1e6, 2) == 10.14 and round(m.owner_deflag()["pv"] / 1e6, 2) == 7.16
