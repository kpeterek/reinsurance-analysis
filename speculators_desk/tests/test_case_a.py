"""Case A numbers as stated in case_A.md and case_A_rubric.md."""

import importlib.util
from pathlib import Path

import pytest

from sdesk import cre

R = pytest.approx
_P = Path(__file__).resolve().parents[1] / "cases/hypothetical/case_A_overpriced_hotel_owner/case_a_model.py"
_spec = importlib.util.spec_from_file_location("case_a_model", _P)
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)


def test_owner_statement():
    o = m.owner_statement()
    assert o["total_revenue"] == 2_555_818
    assert o["gop"] == 1_190_318
    assert o["ebitda"] == 811_535
    assert round(o["occupancy"], 4) == 0.7000
    assert o["adr"] == R(118.00)
    assert round(o["revpar"], 2) == 82.60
    assert round(o["owner_cap_value_8_5"]) == 9_547_471
    assert round(o["gop"] / o["total_revenue"], 3) == 0.466
    # data exhibit agrees with model inputs
    csv = (Path(__file__).resolve().parents[1] / "cases/datasets/case_a_owner_t12.csv").read_text()
    for key in ("rooms_revenue", "franchise_fees", "property_tax"):
        assert f"{key},{m.OWNER_PL[key]}" in csv


def test_bridge_and_normalized():
    n = m.normalized_statement()
    assert n["pipeline_rev_removed"] == R(119_140)
    assert n["lost_room_nights"] == R(1_110)
    bridge = dict(m.noi_bridge())
    assert bridge["Variable rooms cost saved on lost room-nights"] == R(15_540)
    assert round(bridge["Franchise fees saved on removed revenue"]) == 12_510
    assert round(n["mgmt_fee"]) == 71_450
    assert round(n["ffe_reserve"]) == 95_267
    assert round(n["noi_before_property_tax"]) == 607_927
    assert n["rooms_sold"] == R(19_841)
    assert round(n["occupancy"], 4) == 0.6629
    assert round(n["adr"], 2) == 118.60
    assert round(n["revpar"], 2) == 78.62
    assert n["total_revenue"] == R(2_381_678)
    assert n["gop"] == R(1_089_718)
    assert round(n["rooms_expense"]) == 656_460


def test_scenarios():
    s = m.scenario_values()
    exp = {"Upside": (626_165, 5_849_277, 114_353, 511_812, 5_067_677, 61_801),
           "Base": (607_927, 5_307_091, 103_754, 504_174, 4_525_491, 55_189),
           "Downside": (559_293, 4_490_510, 87_789, 471_504, 3_708_910, 45_231)}
    for k, (npt, v, tax, noi, asis, pk) in exp.items():
        x = s[k]
        assert (round(x["noi_before_tax"]), round(x["stabilized_value"]), round(x["property_tax"]),
                round(x["noi"]), round(x["as_is_value"]), round(x["per_key"])) == (npt, v, tax, noi, asis, pk)
    assert s["Base"]["noi"] / s["Base"]["stabilized_value"] == R(0.095)
    assert s["Base"]["pip_all_in"] == R(721_600)
    e = m.unloaded_value_error()
    assert round(e["wrong"]) == 5_576_076
    assert round(e["overstatement"]) == 268_986
    assert m.REPLACEMENT_COST_PER_KEY * m.ROOMS == 11_070_000


def test_owner_ask_yields():
    n = m.normalized_statement()["noi_before_property_tax"]
    p = 8_000_000
    noi = n - m.EFFECTIVE_TAX_ON_PRICE * p
    assert round(noi) == 451_527
    assert round(noi / p, 4) == 0.0564
    allin = p * 1.02 + 721_600 + 60_000
    assert round(noi / allin, 4) == 0.0505


def test_bids_and_financing():
    n = m.normalized_statement()["noi_before_property_tax"]
    exp = {0.095: (4_582_870, 2_978_866, 270_003, 1.92, 2_477_262, 0.1002),
           0.10: (4_358_431, 2_832_980, 256_780, 2.04, 2_394_219, 0.1111),
           0.105: (4_152_067, 2_698_843, 244_622, 2.15, 2_317_865, 0.1217)}
    for y, (p, loan, ds, dscr, eq, coc) in exp.items():
        price = m.bid_price(y, n)
        noi = n - m.EFFECTIVE_TAX_ON_PRICE * price
        f = m.financing(price, noi)
        assert round(price) == p
        assert noi / f["all_in_basis"] == R(y)
        assert (round(f["max_loan"]), round(f["debt_service"]), round(f["dscr_actual"], 2),
                round(f["equity"]), round(f["cash_on_cash"], 4)) == (loan, ds, dscr, eq, coc)
        assert f["binding"] == "ltv"


def test_seller_position():
    sp = m.seller_position()
    assert round(sp["noi_refi"]) == 529_727
    assert round(sp["appraised"]) == 5_576_076
    assert round(sp["refi_max_loan"]) == 3_624_450
    assert round(sp["refi_dscr"]) == 4_174_524
    assert round(sp["refi_debt_yield"]) == 4_815_702
    assert round(sp["refi_gap"]) == 729_917
    assert round(sp["payoff_price"]) == 4_432_990


def test_rubric_numbers():
    base_n = m.normalized_statement()["noi_before_property_tax"]
    old = m.BACKFILL_SHARE
    try:
        m.BACKFILL_SHARE = 0.70
        n70 = m.normalized_statement()["noi_before_property_tax"]
    finally:
        m.BACKFILL_SHARE = old
    assert round(n70 - base_n) == 46_717
    assert round(n70) == 654_644
    dv = cre.loaded_cap_value(n70, 0.095, m.EFFECTIVE_TAX_ON_PRICE) - cre.loaded_cap_value(base_n, 0.095, m.EFFECTIVE_TAX_ON_PRICE)
    assert round(dv) == 407_832
    assert round(10_000 / (0.095 + m.EFFECTIVE_TAX_ON_PRICE), -3) == 87_000
    assert round(0.095 / 0.105 - 1, 4) == -0.0952
    be = m.breakeven_occupancy_at_price(4_350_000)
    assert round(be["debt_service"]) == 256_283
    assert round(be["breakeven_occupancy"], 3) == 0.556
    assert round(m.breakeven_occupancy_at_price(4_350_000, False)["breakeven_occupancy"], 3) == 0.454
