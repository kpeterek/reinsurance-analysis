"""Reproduces every number in Chapter 12 text, problems, and solutions.

Library: sdesk.x_cre_distress (new module for this chapter) and
sdesk.cre.distressed_loan_recovery. Where possible a second, independent route
(closed form, identity, or reverse calculation) checks the library.
"""

import datetime as dt
import math

import pytest

from sdesk import cre, tvm
from sdesk import x_cre_distress as xd

R = pytest.approx

# ---------------------------------------------------------------- Example 12.1
G121 = [0.03] * 4 + [-0.03, 0.0] + [0.015] * 14


def _sim(lag, years=16):
    return xd.stock_flow_simulation(100.0, 92.0, 30.0, years, G121[:years], 0.10, 0.5, 33.0, 0.35, lag, 0.01)


EX121_TABLE = [  # year, stock, demand, vacancy %, rent, completions, starts
    (0, 100.00, 92.00, 8.00, 30.00, 0.00, 0.00), (1, 99.00, 94.76, 4.28, 30.86, 0.00, 0.00),
    (2, 98.01, 97.60, 0.42, 32.34, 0.00, 0.00), (3, 97.03, 100.53, 0.00, 33.95, 0.00, 0.98),
    (4, 96.06, 103.55, 0.00, 35.65, 0.00, 2.70), (5, 95.10, 100.44, 0.00, 37.43, 0.00, 4.47),
    (6, 95.13, 100.44, 0.00, 39.31, 0.98, 6.36), (7, 96.88, 101.95, 0.00, 41.27, 2.70, 8.50),
    (8, 100.38, 103.48, 0.00, 43.33, 4.47, 11.00), (9, 105.74, 105.03, 0.67, 45.35, 6.36, 13.86),
    (10, 113.18, 106.60, 5.81, 46.31, 8.50, 15.97), (11, 123.05, 108.20, 12.07, 45.83, 11.00, 16.74),
    (12, 135.67, 109.83, 19.05, 43.75, 13.86, 15.47), (13, 150.29, 111.47, 25.83, 40.29, 15.97, 11.62),
    (14, 165.53, 113.15, 31.65, 35.93, 16.74, 5.14), (15, 179.34, 114.84, 35.97, 31.27, 15.47, 0.00),
    (16, 189.17, 116.57, 38.38, 26.83, 11.62, 0.00),
]


def test_example_12_1_table():
    rows = _sim(3)
    for (y, s, d, v, r, c, n), row in zip(EX121_TABLE, rows):
        assert row["year"] == y
        assert (round(row["stock"], 2), round(row["demand"], 2), round(100 * row["vacancy"], 2),
                round(row["rent"], 2), round(row["completions"], 2), round(row["starts"], 2)) == (s, d, v, r, c, n)
    # hand calculation of years 1 and 3
    assert 92 * 1.03 == R(94.76)
    assert 30 * (1 + 0.5 * (0.10 - (1 - 94.76 / 99.0))) == R(rows[1]["rent"])
    assert 0.35 * (rows[3]["rent"] / 33 - 1) * rows[3]["stock"] == R(rows[3]["starts"])
    # completions = starts three years earlier
    for t in range(4, 17):
        assert rows[t]["completions"] == R(rows[t - 3]["starts"])
    # peak rent year 10, starts peak year 11
    assert max(rows, key=lambda r: r["rent"])["year"] == 10
    assert max(rows, key=lambda r: r["starts"])["year"] == 11
    # committed pipeline at end of year 10 and later starts
    assert round(sum(rows[t]["starts"] for t in (8, 9, 10)), 2) == 40.83
    assert round(sum(rows[t]["starts"] for t in (8, 9, 10)) / rows[10]["stock"], 2) == 0.36
    assert round(sum(rows[t]["starts"] for t in (11, 12, 13, 14)), 2) == 48.98


def test_example_12_1_lag_comparison():
    r3, r1 = _sim(3, 20), _sim(1, 20)
    pv3, pv1 = max(r3, key=lambda r: r["vacancy"]), max(r1, key=lambda r: r["vacancy"])
    assert (pv3["year"], round(pv3["vacancy"], 4)) == (17, 0.3851)
    assert (pv1["year"], round(pv1["vacancy"], 4)) == (12, 0.1962)
    pr1 = max(r1, key=lambda r: r["rent"])
    assert (pr1["year"], round(pr1["rent"], 2)) == (8, 39.87)
    assert round(sum(r["completions"] for r in r3), 2) == 112.82
    assert round(sum(r["completions"] for r in r1), 2) == 51.51
    # identity once the pipeline is empty: stock decays at 1%
    assert r3[18]["completions"] == 0 and r3[19]["completions"] == 0
    assert r3[19]["stock"] == R(0.99 * r3[18]["stock"])
    # starts stop in year 15
    assert r3[15]["starts"] == 0 and r3[14]["starts"] > 0


def test_stock_flow_boundaries():
    # no rent premium -> no starts; zero growth, stock at demand -> vacancy 0, rent rises at alpha*v*
    rows = xd.stock_flow_simulation(100, 100, 30, 2, [0, 0], 0.10, 0.5, 50, 0.35, 2, 0.0)
    assert all(r["starts"] == 0 for r in rows)
    assert rows[1]["vacancy"] == 0 and rows[1]["rent"] == R(30 * 1.05)
    with pytest.raises(ValueError):
        xd.stock_flow_simulation(100, 90, 30, 3, [0.0], 0.1, 0.5, 30, 0.3, 2, 0.0)


# ---------------------------------------------------------------- §12.4.2 and Example 12.2
def test_section_12_4_2_factor():
    k = tvm.loan_constant(0.0625, 30)
    assert round(k, 5) == 0.07389
    assert round(0.036 / k, 3) == 0.487


def test_example_12_2():
    k = tvm.loan_constant(0.0625, 30)
    assert round(4_500_000 / (60_000_000 * 0.036), 2) == 2.08
    assert round(60_000_000 * k) == 4_433_164
    # State 1
    v1 = 4_800_000 / 0.0575
    assert round(v1) == 83_478_261
    s1 = cre.max_loan(4_800_000, v1, 0.0625, 30, ltv_max=0.65, dscr_min=1.25, debt_yield_min=0.08)
    assert (round(s1["ltv"]), round(s1["dscr"]), round(s1["debt_yield"]), s1["binding"]) == \
        (54_260_870, 51_971_912, 60_000_000, "dscr")
    assert round(4_800_000 / (60_000_000 * k), 2) == 1.08
    assert round(4_800_000 / (60_000_000 * 0.036), 2) == 2.22
    gap1 = cre.refinance_gap(60_000_000, s1["max_loan"], 0.01 * s1["max_loan"])
    assert round(gap1) == 8_547_807
    assert round(v1 - 60_000_000) == 23_478_261
    assert round(v1 * 0.98 - 60_000_000) == 21_808_696
    assert round(4.8e6 / s1["max_loan"], 4) == 0.0924
    assert round(s1["max_loan"] / v1, 3) == 0.623
    # State 2
    v2 = 3_900_000 / 0.065
    s2 = cre.max_loan(3_900_000, v2, 0.0625, 30, ltv_max=0.65, dscr_min=1.25, debt_yield_min=0.08)
    assert v2 == R(60_000_000)
    assert (round(s2["ltv"]), round(s2["dscr"]), round(s2["debt_yield"]), s2["binding"]) == \
        (39_000_000, 42_227_178, 48_750_000, "ltv")
    assert round(cre.refinance_gap(60e6, s2["max_loan"], 0.01 * s2["max_loan"])) == 21_390_000
    assert round(v2 * 0.98 - 60e6) == -1_200_000
    assert round(3.9e6 / (39e6 * k), 2) == 1.35


# ---------------------------------------------------------------- Example 12.3
EX123 = [dict(p=0.10, recovery=42_400_000, costs=150_000, years=1.0),
         dict(p=0.25, recovery=34_000_000, costs=250_000, years=0.5),
         dict(p=0.30, recovery=31_000_000 * 0.98, costs=1_000_000, years=1.25),
         dict(p=0.20, recovery=29_500_000 * 0.98, costs=2_200_000, years=2.0),
         dict(p=0.15, recovery=29_000_000 * 0.98, costs=3_500_000, years=3.0)]


def _irr_expected(scen, price):
    lo, hi = -0.5, 2.0
    f = lambda k: sum(s["p"] * (s["recovery"] - s["costs"]) / (1 + k) ** s["years"] for s in scen) - price  # noqa: E731
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if f(mid) > 0 else (lo, mid)
    return 0.5 * (lo + hi)


def test_example_12_3():
    assert 40_000_000 * 1.06 == R(42_400_000)
    r = cre.distressed_loan_recovery(24_000_000, EX123, 0.16)
    nets = [round(d["net"]) for d in r["detail"]]
    assert nets == [42_250_000, 33_750_000, 29_380_000, 26_710_000, 24_920_000]
    pvs = [round(d["pv"]) for d in r["detail"]]
    assert pvs == [36_422_414, 31_336_088, 24_405_028, 19_849_881, 15_965_189]
    assert [round(s["p"] * d["pv"]) for s, d in zip(EX123, r["detail"])] == \
        [3_642_241, 7_834_022, 7_321_508, 3_969_976, 2_394_778]
    assert round(r["expected_pv"]) == 25_162_526
    assert round(r["expected_pv"] / 40e6, 3) == 0.629
    assert round(r["npv"]) == 1_162_526
    anns = [round(d["annualized_return"], 4) for d in r["detail"]]
    assert anns == [0.7604, 0.9775, 0.1756, 0.0549, 0.0126]
    assert [round(d["net"] - 24e6) for d in r["detail"]] == [18_250_000, 9_750_000, 5_380_000, 2_710_000, 920_000]
    assert sum(s["p"] * (d["net"] - 24e6) for s, d in zip(EX123, r["detail"])) == R(6_556_500)
    mean_irr = sum(s["p"] * d["annualized_return"] for s, d in zip(EX123, r["detail"]))
    assert round(mean_irr, 4) == 0.3860
    assert round(_irr_expected(EX123, 24e6), 4) == 0.2046
    # check: averaging time understates
    e_net = sum(s["p"] * d["net"] for s, d in zip(EX123, r["detail"]))
    e_t = sum(s["p"] * s["years"] for s in EX123)
    assert (e_net, e_t) == (R(30_556_500), R(1.45))
    assert round((e_net / 24e6) ** (1 / e_t) - 1, 3) == 0.181
    # fast consensual share and the shift to contested
    assert sum(s["p"] for s in EX123[:3]) == R(0.65)
    shift = 0.15 * (r["detail"][1]["pv"] - r["detail"][3]["pv"])
    assert round(shift) == 1_722_931
    assert round((r["expected_pv"] - shift) / 1e6, 2) == 23.44


# ---------------------------------------------------------------- Example 12.4
def test_example_12_4_recovery():
    tx = xd.foreclosure_recovery(20e6, 3, -0.04, 600e3, 150e3, 0.02, 0.12, resale_months=6)
    jd = xd.foreclosure_recovery(20e6, 24, -0.04, 600e3, 600e3, 0.02, 0.12, resale_months=6)
    assert (tx["years"], jd["years"]) == (R(0.75), R(2.5))
    assert (round(tx["value_at_resale"]), round(tx["carry"]), round(tx["net"]), round(tx["pv"])) == \
        (19_396_949, 450_000, 18_409_010, 16_908_961)
    assert (round(jd["value_at_resale"]), round(jd["carry"]), round(jd["net"]), round(jd["pv"])) == \
        (18_059_598, 1_500_000, 15_598_406, 11_749_927)
    # independent closed form
    assert 20e6 * 0.96 ** 0.75 == R(tx["value_at_resale"])
    assert (20e6 * 0.96 ** 2.5 * 0.98 - 2.1e6) / 1.12 ** 2.5 == R(jd["pv"])
    assert round(tx["pv"] / 20e6, 3) == 0.845 and round(jd["pv"] / 20e6, 3) == 0.587
    diff = tx["pv"] - jd["pv"]
    assert round(diff / 1e6, 2) == 5.16 and round(diff / 20e6, 3) == 0.258
    assert round((tx["value_at_resale"] - jd["value_at_resale"]) * 0.98 / 1e6, 2) == 1.31
    assert round(((jd["carry"] + jd["legal"]) - (tx["carry"] + tx["legal"])) / 1e6, 2) == 1.50


def test_example_12_4_texas_dates():
    d1, d2 = dt.date(2026, 3, 11), dt.date(2026, 3, 18)
    assert d1.weekday() == 2 and d2.weekday() == 2           # Wednesdays
    s1, s2 = xd.texas_earliest_sale_date(d1), xd.texas_earliest_sale_date(d2)
    assert s1 == dt.date(2026, 4, 7) and s1.weekday() == 1
    assert s2 == dt.date(2026, 5, 5) and s2.weekday() == 1
    assert ((s1 - d1).days, (s2 - d2).days) == (27, 48)
    assert d1 + dt.timedelta(days=21) == dt.date(2026, 4, 1)
    assert d2 + dt.timedelta(days=21) == dt.date(2026, 4, 8)


def test_texas_holiday_exception():
    # first Tuesday of July 2028 is July 4 -> sale on Wednesday July 5
    assert dt.date(2028, 7, 4).weekday() == 1
    assert xd.texas_earliest_sale_date(dt.date(2028, 6, 1)) == dt.date(2028, 7, 5)
    # first Tuesday of January 2030 is January 1 -> Wednesday January 2
    assert xd.texas_earliest_sale_date(dt.date(2029, 12, 3)) == dt.date(2030, 1, 2)


# ---------------------------------------------------------------- Example 12.5
def test_example_12_5():
    ara = xd.appraisal_reduction_amount(50e6, 1.5e6, 0.6e6, 0.0, 38e6, 0.10, 0.4e6)
    assert ara == R(17.5e6)
    full = 50e6 * 0.05 / 12
    assert round(full) == 208_333
    assert round(full * (1 - ara / 50e6)) == 135_417
    assert (40e6 - ara) / 40e6 == R(0.5625)
    ara2 = xd.appraisal_reduction_amount(50e6, 1.5e6, 0.6e6, 0.0, 24e6, 0.10, 0.4e6)
    assert ara2 == R(30.1e6)
    assert (40e6 - ara2) / 40e6 == R(0.2475)
    mod = 0.0025 * 50e6 * 1 + 0.01 * (50e6 + 3 * 0.05 * 50e6)
    liq = 0.0025 * 50e6 * 1.5 + 0.01 * 30e6
    assert (mod, liq) == (R(700_000), R(487_500))
    # boundary: appraisal high enough -> ARA = 0
    assert xd.appraisal_reduction_amount(50e6, 1.5e6, 0.6e6, 0.0, 100e6) == 0.0


# ---------------------------------------------------------------- Example 12.6
def test_example_12_6():
    s = xd.cre_concentration_screens(280e6, 820e6, 250e6, 520e6)
    assert (s["cld_ratio"], s["cre_ratio"]) == (R(1.12), R(3.28))
    assert round(s["cre_growth_36m"], 3) == 0.577
    assert s["screen_1"] and s["screen_2"]
    a = xd.sale_needed_for_ratio(820e6, 250e6, 3.0, 0.88)
    assert (a["naive_sale"], a["sale_par"], a["loss"], a["capital_after"], a["cre_after"]) == \
        (R(70e6), R(109.375e6), R(13.125e6), R(236.875e6), R(710.625e6))
    assert a["cre_after"] / a["capital_after"] == R(3.0)
    b = xd.sale_needed_for_ratio(820e6, 250e6, 3.0, 0.88, 0.21)
    assert round(b["sale_par"] / 1e6, 2) == 97.82 and round(b["loss"] / 1e6, 2) == 9.27
    assert 1 - 3 * 0.12 * 0.79 == R(0.7156)
    c = xd.sale_needed_for_ratio(820e6, 250e6, 3.0, 0.60)
    assert not c["feasible"]
    assert 1 - 3 * 0.40 == R(-0.20)
    # boundary: price 2/3 with no tax is exactly infeasible; already compliant needs no sale
    assert not xd.sale_needed_for_ratio(820e6, 250e6, 3.0, 2 / 3)["feasible"]
    assert xd.sale_needed_for_ratio(700e6, 250e6, 3.0, 0.9)["sale_par"] == 0.0


# ---------------------------------------------------------------- Example 12.7
def test_example_12_7():
    r = xd.reit_implied_cap_rate(42, 100e6, 3.2e9, 0.3e9, 0.1e9, 0.2e9, 480e6)
    assert r["market_cap"] == R(4.2e9) and r["implied_re_value"] == R(7.4e9)
    assert round(r["implied_cap"], 4) == 0.0649
    n = xd.reit_nav_per_share(480e6, 0.055, 3.2e9, 0.3e9, 0.1e9, 0.2e9, 100e6)
    assert round(n["gross_asset_value"] / 1e9, 3) == 8.727
    assert round(n["nav"] / 1e9, 3) == 5.527
    assert round(n["nav_per_share"], 2) == 55.27
    assert round(42 / n["nav_per_share"] - 1, 3) == -0.240
    assert round(n["gross_asset_value"] / n["nav"], 2) == 1.58
    assert round((3.2e9 + 0.3e9) / n["gross_asset_value"], 2) == 0.40
    assert round((r["implied_cap"] - 0.055) * 1e4) == 99
    # check: at the implied cap, NAV per share equals the price
    chk = xd.reit_nav_per_share(480e6, r["implied_cap"], 3.2e9, 0.3e9, 0.1e9, 0.2e9, 100e6)
    assert chk["nav_per_share"] == R(42.0)


# ---------------------------------------------------------------- Example 12.8
def test_example_12_8():
    r1 = xd.required_gross_rent(140e6, 0.07, 4.8e6, 400_000, 0.88, 1.6e6)
    r2 = xd.required_gross_rent(70e6, 0.09, 4.8e6, 400_000, 0.88, 1.6e6)
    assert (round(r1, 2), round(r2, 2)) == (46.02, 36.08)
    assert round(r1 - r2, 2) == 9.94
    assert (9.8e6 - 6.3e6) / 352_000 == R(r1 - r2)
    noi = 40 * 352_000 - 6.4e6
    assert noi == R(7_680_000)
    assert (round(noi / 140e6, 4), round(noi / 70e6, 4)) == (0.0549, 0.1097)


# ---------------------------------------------------------------- Problems
def test_problem_12_2():
    assert 2e6 / (25e6 * 0.04) == R(2.0)
    assert round(2e6 / (25e6 * 0.065), 2) == 1.23
    k = tvm.loan_constant(0.065, 30)
    assert round(k, 6) == 0.075848
    assert round(25e6 * k) == 1_896_204
    assert round(2e6 / (25e6 * k), 2) == 1.05
    assert round(2e6 / (1.25 * k) / 1e6, 2) == 21.09


def test_problem_12_3():
    d = dt.date(2027, 1, 14)
    assert d.weekday() == 3
    s = xd.texas_earliest_sale_date(d)
    assert s == dt.date(2027, 3, 2) and (s - d).days == 47
    assert dt.date(2027, 2, 2).weekday() == 1
    c = xd.cre_concentration_screens(70e6, 250e6, 80e6, 150e6)
    assert (c["cld_ratio"], c["cre_ratio"]) == (R(0.875), R(3.125))
    assert round(c["cre_growth_36m"], 3) == 0.667
    assert (c["screen_1"], c["screen_2"]) == (False, True)


def test_problem_12_4():
    rows = xd.stock_flow_simulation(50, 46, 20, 3, [0.04, 0.04, 0.0], 0.08, 1.0, 20, 0.5, 2, 0.0, pipeline0=[0.0, 1.0])
    exp = [(50.00, 47.84, 4.32, 20.74, 0.00, 0.92), (51.00, 49.75, 2.44, 21.89, 1.00, 2.41),
           (51.92, 49.75, 4.17, 22.73, 0.92, 3.54)]
    for row, (s, d, v, r, c, n) in zip(rows[1:], exp):
        assert (round(row["stock"], 2), round(row["demand"], 2), round(100 * row["vacancy"], 2),
                round(row["rent"], 2), round(row["completions"], 2), round(row["starts"], 2)) == (s, d, v, r, c, n)
    assert rows[1]["rent"] == R(20.736)
    assert round(rows[2]["starts"], 3) == 2.407 and round(rows[3]["starts"], 3) == 3.538
    s5 = rows[3]["stock"] + rows[2]["starts"] + rows[3]["starts"]
    assert round(s5, 1) == 57.9
    assert round(1 - rows[3]["demand"] / s5, 2) == 0.14


def test_problem_12_5():
    sc = [dict(p=0.15, recovery=21.0e6, costs=0.1e6, years=1.0), dict(p=0.25, recovery=16.5e6, costs=0.1e6, years=0.5),
          dict(p=0.45, recovery=15.0e6, costs=1.2e6, years=1.5), dict(p=0.15, recovery=14.0e6, costs=2.0e6, years=3.0)]
    r = cre.distressed_loan_recovery(13e6, sc, 0.15)
    assert [round(d["pv"]) for d in r["detail"]] == [18_173_913, 15_293_079, 11_190_058, 7_890_195]
    assert [round(s["p"] * d["pv"]) for s, d in zip(sc, r["detail"])] == [2_726_087, 3_823_270, 5_035_526, 1_183_529]
    assert round(r["expected_pv"]) == 12_768_412
    assert round(r["npv"]) == -231_588
    assert [round(d["annualized_return"], 4) for d in r["detail"]] == [0.6077, 0.5915, 0.0406, -0.0263]
    assert round(sum(s["p"] * d["annualized_return"] for s, d in zip(sc, r["detail"])), 3) == 0.253


def test_problem_12_6():
    ara = xd.appraisal_reduction_amount(30e6, 0.9e6, 0.3e6, 0.2e6, 20e6, 0.10, 0.1e6)
    assert ara == R(13.3e6)
    assert 30e6 * 0.045 / 12 == R(112_500)
    assert round(1 - ara / 30e6, 5) == 0.55667
    assert round(112_500 * (1 - ara / 30e6)) == 62_625
    assert (20e6 - ara) / 20e6 == R(0.335)
    v_star = (31.3e6 - 15e6) / 0.9
    assert round(v_star / 1e6, 2) == 18.11
    assert xd.appraisal_reduction_amount(30e6, 0.9e6, 0.3e6, 0.2e6, v_star, 0.10, 0.1e6) == R(15e6)
    assert round(v_star / 20e6 - 1, 3) == -0.094


def test_problem_12_7():
    r = xd.reit_implied_cap_rate(18, 250e6, 6.0e9, 0.0, 0.2e9, 0.5e9, 720e6)
    assert r["implied_re_value"] == R(9.8e9)
    assert round(r["implied_cap"], 4) == 0.0735
    n = xd.reit_nav_per_share(720e6, 0.0625, 6.0e9, 0.0, 0.2e9, 0.5e9, 250e6)
    assert n["gross_asset_value"] == R(11.52e9) and n["nav"] == R(6.22e9)
    assert round(n["nav_per_share"], 2) == 24.88
    assert round(18 / n["nav_per_share"] - 1, 3) == -0.277
    assert round(9.8 / 11.52 - 1, 3) == -0.149
    assert round((r["implied_cap"] - 0.0625) * 1e4) == 110
    assert round(n["gross_asset_value"] / n["nav"], 2) == 1.85


def test_problem_12_8():
    exp = {0.85: (0.6445, 93.1, 11.0, 109.0), 0.70: (0.2890, 207.6, 49.2, 70.8), 0.65: (0.1705, 351.9, 97.3, 22.7)}
    for p, (den, par, loss, cap) in exp.items():
        assert round(1 - 3 * (1 - p) * 0.79, 4) == den
        r = xd.sale_needed_for_ratio(420e6, 120e6, 3.0, p, 0.21)
        assert (round(r["sale_par"] / 1e6, 1), round(r["loss"] / 1e6, 1), round(r["capital_after"] / 1e6, 1)) == \
            (par, loss, cap)
        assert r["cre_after"] / r["capital_after"] == R(3.0)
    assert round(207.6 / 420, 2) == 0.49 and round(351.9 / 420, 2) == 0.84
    assert 420e6 / 3 - 120e6 == R(20e6)


def test_problem_12_9():
    assert round(xd.required_gross_rent(95e6, 0.065, 2.75e6, 250_000, 0.85, 0.875e6), 2) == 46.12
    assert round(xd.required_gross_rent(40e6, 0.10, 2.75e6, 250_000, 0.85, 0.875e6), 2) == 35.88
    assert round((70e6 * 0.06 + 3.625e6) / 212_500, 2) == 36.82
    for rent, noi, dscr, y in ((40, 4_875_000, 1.16, 0.0513), (36, 4_025_000, 0.96, 0.0424)):
        n = rent * 212_500 - 3.625e6
        assert n == R(noi)
        assert round(n / 4.2e6, 2) == dscr and round(n / 95e6, 4) == y


def test_decision_exercise_numbers():
    # Case E figures quoted in the solutions' model answer are asserted in tests/test_case_e.py;
    # here: the NPL withdrawal threshold (combined contested + bankruptcy probability 50%)
    assert 0.20 + 0.15 + 0.15 == R(0.50)


def test_rules_of_thumb():
    # 2/3 price threshold at 3x with no tax
    assert 1 - 3 * (1 - 2 / 3) == R(0.0, abs=1e-12)
    # peak vacancy ratio lag 3 vs lag 1
    r3, r1 = _sim(3, 20), _sim(1, 20)
    ratio = max(r["vacancy"] for r in r3) / max(r["vacancy"] for r in r1)
    assert 1.9 < ratio < 2.0
    assert math.isclose(0.036 / tvm.loan_constant(0.0625, 30), 0.487, abs_tol=5e-4)
