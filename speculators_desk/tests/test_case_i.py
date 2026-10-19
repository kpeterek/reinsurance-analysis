"""Case I numbers as stated in case_I.md and case_I_rubric.md."""

import importlib.util
import math
from pathlib import Path

import pytest

from sdesk import cre
from sdesk import x_options_real as ro

R = pytest.approx
_P = Path(__file__).resolve().parents[1] / "cases/hypothetical/case_I_development_land_option/case_i_model.py"
_spec = importlib.util.spec_from_file_location("case_i_model", _P)
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)


def test_residual_land_values():
    a = m.rlv("by_right_240")
    assert (a["gdv"], a["net_value"]) == (R(72_000_000), R(70_560_000))
    assert (a["hard"], a["soft"], round(a["fin"])) == (R(46_800_000), R(5_616_000), 3_144_960)
    assert round(a["non_land_cost"]) == 55_560_960
    assert round(a["net_value"] / 1.15) == 61_356_522
    assert round(a["land_value"]) == 5_795_562
    assert (round(a["land_value"] / 240), round(a["land_value"] / 12)) == (24_148, 482_963)
    b = m.rlv("pd_330")
    assert (b["gdv"], b["net_value"]) == (R(99_000_000), R(97_020_000))
    assert (b["hard"], round(b["soft"]), round(b["fin"])) == (R(63_360_000), 7_603_200, 4_257_792)
    assert round(b["non_land_cost"]) == 75_220_992
    assert round(b["net_value"] / 1.15) == 84_365_217
    assert round(b["land_value"]) == 9_144_225
    assert (round(b["land_value"] / 330), round(b["land_value"] / 12)) == (27_710, 762_019)
    # independent check of the residual identity: N = (L + H + S + F)(1 + m)
    assert (a["land_value"] + a["non_land_cost"]) * 1.15 == R(a["net_value"])
    assert round(5_400_000 / a["land_value"], 2) == 0.93
    assert round((b["land_value"] - a["land_value"]) / 1e6, 2) == 3.35


def test_tree_and_leverage():
    q = m.q_neutral()
    assert round(q, 4) == 0.4273
    assert round((1 + 0.045 - (1 / 1.2)) / (1.2 - 1 / 1.2), 3) == 0.577  # the no-yield error in the rubric
    up = m.rlv("by_right_240", 1.2, 1)["land_value"]
    dn = m.rlv("by_right_240", 1 / 1.2, 1)["land_value"]
    assert (round(up), round(dn)) == (15_844_428, -6_652_964)
    assert round(up / m.rlv("by_right_240")["land_value"] - 1, 3) == 1.734
    assert m.gdv(240, 1.2) == R(86_400_000) and m.gdv(240, 1 / 1.2) == R(60_000_000)
    pu = m.rlv("pd_330", 1.2, 1)["land_value"]
    pd = m.rlv("pd_330", 1 / 1.2, 1)["land_value"]
    assert (round(pu), round(pd)) == (23_008_429, -7_925_484)


def test_alternatives():
    s = m.sell_now()
    assert s["pv"] == R(5_238_000)
    b = m.build_now()
    assert b["fee"] == R(1_404_000)
    assert round(b["pv"]) == 4_391_562
    w = m.wait_one_year()
    assert round(w["pv"]) == 7_024_032
    # hand formula
    q = w["q"]
    hand = ((q * 15_844_427.686956532 + (1 - q) * 1_500_000) * 0.97 - 60_000) / 1.045
    assert hand == R(w["pv"])
    e = m.entitle_and_sell()
    assert round(e["node_up"]) == 20_142_829
    assert round(e["pv"]) == 8_278_809
    assert round(m.entitlement_breakeven_p(), 3) == 0.158
    assert round(m.entitle_and_sell(p=0.25)["pv"]) == 7_284_356
    summ = m.summary()
    assert max(summ, key=summ.get) == "entitle"
    assert round(e["pv"] / 0.97) == 8_534_854


def test_jv():
    j = m.jv()
    assert round(j["total_cost"]) == 61_560_960
    assert round(j["loan"]) == 36_936_576
    assert round(j["equity"]) == 24_624_384
    assert round(j["developer_cash"]) == 18_624_384
    assert round(j["owner_share"], 4) == 0.2437
    exp = [(23_039_424, 23_039_424, 0, 5_613_807, -0.0327), (33_623_424, 32_152_961, 1_470_463, 7_834_420, 0.1685),
           (44_207_424, 39_561_761, 4_645_663, 9_639_655, 0.3399)]
    for row, (pr, inv, prom, own, irr) in zip(j["rows"], exp):
        assert (round(row["proceeds"]), round(row["investors"]), round(row["promote"]), round(row["owner"]),
                round(row["project_irr"], 4)) == (pr, inv, prom, own, irr)
    # waterfall check on the base case: capital + 8% pref, then 70/30
    pref = 24_624_384 * 1.08 ** 2
    assert pref + 0.7 * (33_623_424 - pref) == R(32_152_961, abs=1)
    assert round(j["e_owner_t2"]) == 7_730_576
    assert round(j["pv"]) == 6_162_768
    assert round(j["owner_irr_on_credit"], 4) == 0.1351
    assert round(sum(r["p"] * r["promote"] for r in j["rows"]) / 1e6, 2) == 1.90


def test_uncertainty_and_naive():
    t = m.uncertainty_table()
    exp = [(1.10, 4_564_200, 5_262_072, -1_057_495), (1.20, 7_024_032, 8_278_809, 1_402_337),
           (1.30, 9_242_077, 10_984_650, 3_620_382)]
    for row, (u, w, e, v) in zip(t, exp):
        assert (row["u"], round(row["wait"]), round(row["entitle"]), round(row["value_of_waiting"])) == (u, w, e, v)
    assert round(5_795_562 * 0.97) == 5_621_695
    assert round(m.naive_wait()) == 7_592_770
    assert round((m.naive_wait() - m.wait_one_year()["pv"]) / 1e6, 2) == 0.57
    assert round(math.log(1.2), 3) == 0.182


def test_rubric_numbers():
    assert round(23_008_429 * 0.97 / 1e6, 1) == 22.3
    assert round(15_844_428 * 0.97 / 1e6, 1) == 15.4
    assert round(0.04 * m.non_land_costs("by_right_240")["total"]) == 2_222_438
    tc = m.rlv("by_right_240")["total_cost"]
    assert round(tc / 1e6, 1) == 61.4 and round(0.4 * tc / 1e6, 1) == 24.5
    assert 450_000 + 1.5 * 60_000 == 540_000


def test_library_consistency():
    # case uses the same q as the generic helper
    assert m.q_neutral() == R(ro.risk_neutral_prob(1.2, 1 / 1.2, 0.045, 0.055))
    r0 = cre.residual_land_value(72e6, 46.8e6, 5.616e6, 3_144_960, 0.15, 0.02)
    assert round(r0["land_value"]) == 5_795_562
