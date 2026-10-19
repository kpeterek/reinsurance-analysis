"""Reproduces every number in Chapter 2 text, problems, and solutions.

Where possible each figure is computed twice: once with
``sdesk.x_microstructure`` and once by an explicit formula or an independent
route (reverse calculation, re-smoothing, brute-force schedule).
"""

import math

import pytest

from sdesk import stats
from sdesk import x_microstructure as xm

R = pytest.approx


# ------------------------------------------------------------ library tests

def test_auction_rule_matches_brute_force():
    buys = [(10.2, 5), (10.1, 5), (10.0, 10)]
    sells = [(9.9, 4), (10.0, 8), (10.1, 10)]
    # brute force over a fine grid of prices restricted to book prices
    best = None
    for p in [9.9, 10.0, 10.1, 10.2]:
        d = sum(q for lim, q in buys if lim >= p)
        s = sum(q for lim, q in sells if lim <= p)
        key = (min(d, s), -abs(d - s))
        if best is None or key > best[0]:
            best = (key, p)
    assert xm.call_auction_clearing(buys, sells)["price"] == best[1]


def test_auction_tie_takes_mean():
    buys = [(10.1, 10)]
    sells = [(10.0, 10)]
    out = xm.call_auction_clearing(buys, sells)
    assert out["ties"] == 2 and out["price"] == R(10.05)


def test_english_auction_edge_cases():
    assert xm.english_auction_price([5.0], 0.0)["price"] == 0.0  # single bidder pays reserve
    assert xm.english_auction_price([5.0, 4.0], 6.0)["trade"] is False
    assert xm.english_auction_price([], 1.0)["trade"] is False


def test_roll_undefined_when_autocov_positive():
    # accelerating prices: successive changes positively autocorrelated
    assert math.isnan(xm.roll_spread([0, 1, 3, 6, 10, 15, 21, 28]))
    assert math.isnan(xm.roll_spread_from_autocov(0.0012))
    assert xm.roll_spread_from_autocov(-0.0025) == R(0.10)


def test_roll_recovers_spread_in_long_sample():
    # deterministic pseudo-random bounce, long sample: estimate converges to S
    import random
    rng = random.Random(7)
    s = 0.10
    prices = [20 + s / 2 * (1 if rng.random() < 0.5 else -1) for _ in range(20_000)]
    assert xm.roll_spread(prices) == R(s, rel=0.03)


def test_smoothing_round_trip_and_zero_a():
    true = [0.01, -0.02, 0.03, -0.01]
    sm = xm.smooth(true, 0.6, 0.005)
    back = xm.geltner_unsmooth([0.005] + sm, 0.6)
    assert back == [R(x) for x in true]
    assert xm.geltner_unsmooth([0.0, 0.01, 0.02], 0.0) == [R(0.01), R(0.02)]
    with pytest.raises(ValueError):
        xm.geltner_unsmooth([0.0, 0.01], 1.0)


def test_vol_ratio_and_lag_against_series():
    a = 0.6
    # weights (1-a)a^k: mean lag and variance ratio by direct summation
    w = [(1 - a) * a ** k for k in range(400)]
    assert sum(w) == R(1.0)
    assert sum(k * wk for k, wk in enumerate(w)) == R(xm.smoothing_mean_lag(a))
    assert math.sqrt(sum(wk * wk for wk in w)) == R(xm.smoothing_vol_ratio(a))


def test_round_trip_zero_costs():
    assert xm.round_trip_cost(0.0, 0.0) == 0.0
    assert xm.annualized_cost_drag(0.0, 5) == 0.0


# ------------------------------------------------------------ Example 2.1

BUYS = [(50.40, 20), (50.30, 30), (50.20, 40), (50.10, 50), (50.00, 60)]
SELLS = [(49.90, 30), (50.00, 40), (50.10, 40), (50.20, 50), (50.30, 60)]


def test_example_2_1():
    rows = xm.auction_schedules(BUYS, SELLS)
    assert [r["demand"] for r in rows] == [200, 200, 140, 90, 50, 20]
    assert [r["supply"] for r in rows] == [30, 70, 110, 160, 220, 220]
    assert [r["volume"] for r in rows] == [30, 70, 110, 90, 50, 20]
    assert [r["imbalance"] for r in rows] == [170, 130, 30, -70, -170, -200]
    out = xm.call_auction_clearing(BUYS, SELLS)
    assert (out["price"], out["volume"], out["imbalance"]) == (R(50.10), 110, 30)
    rows2 = xm.auction_schedules(BUYS, SELLS, market_sell=100)
    assert [r["supply"] for r in rows2] == [130, 170, 210, 260, 320, 320]
    assert [r["volume"] for r in rows2] == [130, 170, 140, 90, 50, 20]
    out2 = xm.call_auction_clearing(BUYS, SELLS, market_sell=100)
    assert (out2["price"], out2["volume"], out2["imbalance"]) == (R(50.00), 170, 30)
    assert (out2["price"] - out["price"]) / 100 == R(-0.001)
    assert out2["price"] / out["price"] - 1 == R(-0.0020, abs=5e-5)
    assert 100 + 30 + 40 == 170
    assert 0.10 * 100_000 == R(10_000)


# ------------------------------------------------------------ Example 2.2

def test_example_2_2():
    z = xm.standardized_surprise(0.5, 0.3, 0.1)
    assert z == R(2.0)
    dy = xm.yield_change_from_surprise(z, 6)
    assert dy == R(0.0012)
    assert xm.price_change_from_yield(8.5, dy) == R(-0.0102)
    assert 0.5 * 85 * dy ** 2 == R(0.0000612)
    assert xm.price_change_from_yield(8.5, dy, 85) == R(-0.0101388)
    assert round(100 * xm.price_change_from_yield(8.5, dy, 85), 3) == -1.014
    dc = 0.5 * dy
    assert 0.055 / (0.055 + dc) - 1 == R(-0.010791, abs=1e-6)
    z2 = xm.standardized_surprise(0.5, 0.4, 0.1)
    assert z2 == R(1.0)
    dy2 = xm.yield_change_from_surprise(z2, 6)
    assert -8.5 * dy2 == R(-0.0051)
    assert 0.055 / 0.0553 - 1 == R(-0.005425, abs=1e-6)
    assert 0.0102 / 8.5 == R(0.0012)


# ------------------------------------------------------------ Example 2.3

def test_example_2_3():
    noi = 3_000_000
    a, c, d, e = noi / 0.0475, noi / 0.054, noi / 0.0525, noi / 0.056
    assert (round(a), round(c), round(d), round(e)) == (63_157_895, 55_555_556, 57_142_857, 53_571_429)
    b0 = xm.financed_reservation_price(21_000_000, noi, 0.65, 1.25, 0.045)
    assert b0 == R(60_000_000)
    assert noi / (1.25 * 0.045) == R(53_333_333.33)
    assert 21_000_000 + noi / (1.25 * 0.045) == R(74_333_333.33)
    b1 = xm.financed_reservation_price(21_000_000, noi, 0.65, 1.25, 0.0625)
    assert b1 == R(59_400_000)
    assert noi / (1.25 * 0.0625) == R(38_400_000)
    before = xm.english_auction_price([a, b0, c, d, e])
    after = xm.english_auction_price([b1, c, d, e])
    assert before["price"] == R(60_000_000) and before["winner_value"] == R(a)
    assert after["price"] == R(d) and after["winner_value"] == R(b1)
    assert noi / before["price"] == R(0.05)
    assert noi / after["price"] == R(0.0525)
    assert after["price"] / before["price"] - 1 == R(-0.047619, abs=1e-6)
    # with the seller's reserve
    assert xm.english_auction_price([a, b0, c, d, e], 60_000_000)["price"] == R(60_000_000)
    assert xm.english_auction_price([b1, c, d, e], 60_000_000)["trade"] is False
    # independent DSCR / LTV check at $59.4m
    assert noi / (38_400_000 * 0.0625) == R(1.25)
    assert round(38.4 / 59.4, 3) == 0.646


# ------------------------------------------------------------ Example 2.4

EX24 = [20.05, 19.95, 20.05, 20.05, 19.95, 19.95, 20.05, 19.95, 20.05, 19.95, 19.95, 20.05]


def test_example_2_4():
    dp = xm.first_differences(EX24)
    assert [round(x, 2) for x in dp] == [-0.1, 0.1, 0.0, -0.1, 0.0, 0.1, -0.1, 0.1, -0.1, 0.0, 0.1]
    cov = stats.covariance(dp[1:], dp[:-1])
    assert cov == R(-0.0043333, abs=1e-7)
    # independent covariance computation
    x, y = dp[1:], dp[:-1]
    mx, my = sum(x) / len(x), sum(y) / len(y)
    cov2 = sum((u - mx) * (v - my) for u, v in zip(x, y)) / (len(x) - 1)
    assert cov2 == R(cov)
    s = xm.roll_spread(EX24)
    assert s == R(0.1317, abs=5e-5)
    assert math.sqrt(-cov) == R(0.065828, abs=1e-6)
    assert s / 20.0 == R(0.00658, abs=5e-6)
    assert s / 0.10 - 1 == R(0.32, abs=0.01)
    k_reit = xm.round_trip_cost(0.0025, 0.0025)
    k_cre = xm.round_trip_cost(0.015, 0.025)
    assert 1 - (1 - 0.0025) / 1.0025 == R(k_reit)
    assert round(100 * k_reit, 3) == 0.499
    assert round(100 * k_cre, 3) == 3.941
    assert 0.975 / 1.015 == R(0.960591, abs=1e-6)
    drags = {1: (0.499, 3.941), 3: (0.167, 1.331), 7: (0.071, 0.573)}
    for t, (dr, dc) in drags.items():
        assert round(100 * xm.annualized_cost_drag(k_reit, t), 3) == dr
        assert round(100 * xm.annualized_cost_drag(k_cre, t), 3) == dc


# ------------------------------------------------------------ Example 2.5

EX25 = [0.020, 0.015, 0.005, -0.010, -0.020, -0.022, -0.020, -0.015, -0.010]


def test_example_2_5():
    r = xm.geltner_unsmooth(EX25, 0.6)
    assert [round(100 * x, 4) for x in r] == [0.75, -1.0, -3.25, -3.5, -2.5, -1.7, -0.75, -0.25]
    # explicit formula, independent of the library
    r2 = [(EX25[t] - 0.6 * EX25[t - 1]) / 0.4 for t in range(1, 9)]
    assert r2 == [R(x) for x in r]
    sm = math.prod(1 + x for x in EX25[1:]) - 1
    un = math.prod(1 + x for x in r) - 1
    assert round(100 * sm, 2) == -7.50
    assert round(100 * un, 2) == -11.64
    assert round(sm / un, 2) == 0.64
    assert xm.smoothing_mean_lag(0.6) == R(1.5)
    assert xm.smoothing_vol_ratio(0.6) == R(0.5)
    assert xm.smooth(r, 0.6, EX25[0]) == [R(x) for x in EX25[1:]]
    assert round(100 * stats.stdev(EX25[1:]), 2) == 1.32
    assert round(100 * stats.stdev(r), 2) == 1.49
    # sensitivity at a = 0.75
    r75 = xm.geltner_unsmooth(EX25, 0.75)
    assert round(100 * xm.cumulative_return(r75), 2) == -15.69
    assert round(100 * min(r75), 2) == -5.50 and r75.index(min(r75)) == 2  # quarter 3
    assert round(100 * r75[-1], 2) == 0.50


# ------------------------------------------------------------ Example 2.6

COMPS = [(4.70, 100), (4.80, 98), (5.10, 92), (5.20, 91)]


def test_example_2_6():
    naive = sum(c for c, _ in COMPS) / 4
    assert naive == R(4.95)
    assert round(3_000_000 / (naive / 100)) == 60_606_061
    adj = [xm.time_adjust_cap(c, i, 90) for c, i in COMPS]
    assert [round(x, 4) for x in adj] == [5.2222, 5.2267, 5.2133, 5.2578]
    avg = sum(adj) / 4
    assert avg == R(5.23)
    assert round(3_000_000 / (avg / 100)) == 57_361_377
    subj = 3_000_000 / ((avg + 0.30) / 100)
    assert round(subj) == 54_249_548
    assert round(subj / (3_000_000 / (naive / 100)) - 1, 3) == -0.105
    assert round((max(adj) - min(adj)) * 100, 1) == 4.4  # within 4.5 bp
    sb = xm.selection_bias([-0.04, -0.06, -0.09, -0.12, -0.15, -0.18, -0.22, -0.30],
                           [True, True, True, False, False, False, False, False])
    assert sb["population_mean"] == R(-0.145)
    assert sb["traded_mean"] == R(-0.063333, abs=1e-6)
    assert sb["bias"] == R(0.081667, abs=1e-6)
    assert round(subj * 0.0553) == 3_000_000


# ------------------------------------------------------------ Example 2.7 and §2.4.2

def test_example_2_7_and_gs():
    assert round(100 * (4.30 / 5.60 - 1), 2) == -23.21
    assert round(100 * (4.30 / 5.25 - 1), 2) == -18.10
    assert round(100 * (4.30 / 5.53 - 1), 2) == -22.24
    assert 1 - 0.0075 / 0.02 == R(0.625)
    assert 1_500_000 / 200_000_000 == R(0.0075)


# ------------------------------------------------------------ §2.9 historical arithmetic

def test_section_2_9_inferences():
    # Nareit Q4 2021 -> Q1 2023 cap-rate levels and changes (ch02-S01)
    assert round(100 * (4.05 / 5.43 - 1), 1) == -25.4
    assert round(100 * (4.05 / 5.85 - 1), 1) == -30.8
    assert round(5.85 - 4.05, 2) == 1.80  # 180 bp gap reported by Nareit
    # NFI-ODCE appreciation chaining (ch02-S04, S06)
    assert round(100 * ((1 - 0.0028) * (1 - 0.1519) - 1), 2) == -15.43
    # NCREIF Q3 2023 one-year components: income + appreciation ~ total (not additive exactly)
    assert 3.46 - 15.19 == R(-11.73)


# ------------------------------------------------------------ problems

def test_problem_2_2():
    assert xm.geltner_unsmooth([0.01, -0.01], 0.5)[0] == R(-0.03)
    assert xm.geltner_unsmooth([0.01, -0.01], 0.8)[0] == R(-0.09)


def test_problem_2_3():
    z = xm.standardized_surprise(120_000, 180_000, 75_000)
    assert z == R(-0.8)
    dy = xm.yield_change_from_surprise(z, 5)
    assert dy == R(-0.0004)
    assert xm.price_change_from_yield(8.0, dy) == R(0.0032)
    z2 = xm.standardized_surprise(120_000, 100_000, 75_000)
    assert round(z2, 3) == 0.267
    dy2 = xm.yield_change_from_surprise(z2, 5)
    assert round(dy2 * 1e4, 2) == 1.33
    assert round(100 * xm.price_change_from_yield(8.0, dy2), 3) == -0.107


P24B = [(25.30, 15), (25.25, 25), (25.20, 30), (25.15, 40), (25.10, 50)]
P24S = [(25.05, 20), (25.10, 30), (25.15, 35), (25.20, 40), (25.25, 50)]


def test_problem_2_4():
    rows = xm.auction_schedules(P24B, P24S)
    assert [r["demand"] for r in rows] == [160, 160, 110, 70, 40, 15]
    assert [r["supply"] for r in rows] == [20, 50, 85, 125, 175, 175]
    out = xm.call_auction_clearing(P24B, P24S)
    assert (out["price"], out["volume"], out["imbalance"]) == (R(25.15), 85, 25)
    rows2 = xm.auction_schedules(P24B, P24S, market_buy=60)
    assert [r["demand"] for r in rows2] == [220, 220, 170, 130, 100, 75]
    assert [r["volume"] for r in rows2] == [20, 50, 85, 125, 100, 75]
    out2 = xm.call_auction_clearing(P24B, P24S, market_buy=60)
    assert (out2["price"], out2["volume"], out2["imbalance"]) == (R(25.20), 125, 5)
    assert (out2["price"] - out["price"]) / 60 == R(0.000833, abs=1e-6)
    assert round(100 * 0.05 / 25.15, 2) == 0.20


P25 = [41.10, 41.30, 41.10, 41.30, 41.30, 41.10, 41.30, 41.10, 41.10, 41.30]


def test_problem_2_5():
    dp = xm.first_differences(P25)
    assert [round(x, 2) for x in dp] == [0.2, -0.2, 0.2, 0.0, -0.2, 0.2, -0.2, 0.0, 0.2]
    cov = stats.covariance(dp[1:], dp[:-1])
    assert cov == R(-0.022857, abs=1e-6)
    s = xm.roll_spread(P25)
    assert round(s, 4) == 0.3024
    assert round(100 * s / 41.20, 3) == 0.734
    assert round(s / 0.20 - 1, 1) == 0.5
    k = xm.round_trip_cost(0.02, 0.03)
    assert round(100 * k, 3) == 4.902
    assert 0.97 / 1.02 == R(0.950980, abs=1e-6)
    assert round(100 * xm.annualized_cost_drag(k, 5), 3) == 1.000
    assert math.isnan(xm.roll_spread_from_autocov(0.0012))


P26 = [0.015, 0.010, 0.0, -0.010, -0.015, -0.015, -0.012]


def test_problem_2_6():
    r = xm.geltner_unsmooth(P26, 0.7)
    assert [round(100 * x, 3) for x in r] == [-0.167, -2.333, -3.333, -2.667, -1.5, -0.5]
    assert round(100 * xm.cumulative_return(P26[1:]), 2) == -4.15
    assert round(100 * xm.cumulative_return(r), 2) == -10.09
    assert round(xm.smoothing_mean_lag(0.7), 2) == 2.33
    assert round(xm.smoothing_vol_ratio(0.7), 3) == 0.420
    r5 = xm.geltner_unsmooth(P26, 0.5)
    assert [round(100 * x, 2) for x in r5] == [0.5, -1.0, -2.0, -2.0, -1.5, -0.9]
    assert round(100 * xm.cumulative_return(r5), 2) == -6.73


def test_problem_2_7():
    noi = 4_000_000
    f1b = xm.financed_reservation_price(30e6, noi, 0.60, 1.35, 0.0475)
    assert f1b == R(75e6)
    assert round(noi / (1.35 * 0.0475) / 1e6, 2) == 62.38
    assert round((30e6 + noi / (1.35 * 0.0475)) / 1e6, 2) == 92.38
    f2, f3, f4, f5 = 18.5e6 / 0.25, noi / 0.055, noi / 0.0575, noi / 0.06
    assert (f2, round(f3 / 1e6, 2), round(f4 / 1e6, 2), round(f5 / 1e6, 2)) == (R(74e6), 72.73, 69.57, 66.67)
    a = xm.english_auction_price([f1b, f2, f3, f4, f5])
    assert a["price"] == R(74e6)
    assert round(100 * noi / a["price"], 2) == 5.41
    f1a = xm.financed_reservation_price(30e6, noi, 0.60, 1.35, 0.0725)
    assert round(f1a / 1e6, 2) == 70.87
    assert round(noi / (1.35 * 0.0725) / 1e6, 2) == 40.87
    b = xm.english_auction_price([f1a, f3, f4, f5])
    assert b["price"] == R(f1a) and b["winner_value"] == R(f3)
    assert round(100 * (b["price"] / a["price"] - 1), 2) == -4.23
    assert round(100 * noi / b["price"], 2) == 5.64
    c = xm.english_auction_price([f1a, f3, f4, f5], 72e6)
    assert c["trade"] and c["price"] == R(72e6)
    assert round(100 * noi / 72e6, 2) == 5.56
    d = xm.english_auction_price([f1a, noi / 0.0575, f4, f5], 72e6)
    assert d["trade"] is False


def test_problem_2_8():
    assert (88 - 12) / 0.88 == R(86.3636, abs=1e-4)
    assert round(100 * ((88 - 12) / 0.88 / 88 - 1), 2) == -1.86
    assert round(100 * (100 / 88 - 1), 2) == 13.64
    assert (88 - 0.12 * 85) / 0.88 == R(88.409, abs=1e-3)
    assert 25e6 * 0.85 == R(21.25e6)


P29 = [(4.60, 102), (4.85, 99), (6.10, 95), (5.40, 92), (5.60, 90.5)]


def test_problem_2_9():
    naive = sum(c for c, _ in P29) / 5
    assert naive == R(5.31)
    assert round(2.4e6 / (naive / 100) / 1e6, 2) == 45.20
    adj = [xm.time_adjust_cap(c, i, 90) for c, i in P29]
    assert [round(x, 3) for x in adj] == [5.213, 5.335, 6.439, 5.520, 5.631]
    class_b = [adj[0] + 0.30, adj[1] + 0.30, adj[3] + 0.30, adj[4]]
    assert [round(x, 3) for x in class_b] == [5.513, 5.635, 5.820, 5.631]
    avg = sum(class_b) / 4
    assert round(avg, 3) == 5.650
    assert round(2.4e6 / (avg / 100) / 1e6, 2) == 42.48
    assert round(2.4e6 / (min(class_b) / 100) / 1e6, 2) == 43.53
    assert round(2.4e6 / (max(class_b) / 100) / 1e6, 2) == 41.24
    naive_v, v = 2.4e6 / (naive / 100), 2.4e6 / (avg / 100)
    assert round(naive_v / v - 1, 3) == 0.064
    assert round((naive_v - v) / 1e6, 1) == 2.7


def test_problem_2_10():
    assert round(100 * 1.62 / 19.5, 2) == 8.31
    assert round(1.62 / 0.079, 2) == 20.51
    assert 1.62 / 0.096 == R(16.875)
    assert round(100 * (16.875 / 19.5 - 1), 1) == -13.5
    assert 132 * 8_000 == 1_056_000
