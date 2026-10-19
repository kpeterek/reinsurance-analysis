"""Reproduces every number in Chapter 3 text, problems, and solutions."""

import math
import random

import pytest

from sdesk import cre, stats, tvm
from sdesk import x_dynamics as xd

R = pytest.approx


# ------------------------------------------------------------- opening problem / §3.6

def test_opening_problem_and_covenant_buffers():
    value = 320.0
    debt0, debt1 = 0.55 * value, 0.65 * value
    assert (debt0, value - debt0, debt1, debt1 - debt0) == (R(176), R(144), R(208), R(32))
    assert round(1 - 0.65 / 0.70, 4) == 0.0714
    assert round(1 - 0.55 / 0.70, 4) == 0.2143


def test_section_3_6_loop_both_directions():
    m_up = xd.reflexive_loop_gain(0.65, 0.5, 4000, 0.0004)
    m_dn = xd.reflexive_loop_gain(0.65, 0.8, 4000, 0.0004)
    assert m_up == R(0.52)
    assert m_dn == R(0.832)
    assert round(1 / (1 - m_up), 2) == 2.08
    assert round(1 / (1 - m_dn), 2) == 5.95
    assert round(0.05 / (1 - m_dn), 3) == 0.298
    assert round(0.05 / (1 - m_up), 3) == 0.104
    mult = 1 / (1 - m_dn)
    assert round((1 - 0.65 / 0.70) / mult, 3) == 0.012
    assert round((1 - 0.55 / 0.70) / mult, 3) == 0.036
    assert round(((1 - 0.55 / 0.70) / mult) / ((1 - 0.65 / 0.70) / mult)) == 3


def test_section_3_4_10_cobweb():
    path = [0.10]
    for _ in range(3):
        path.append(-0.8 * path[-1])
    assert path == [R(0.10), R(-0.08), R(0.064), R(-0.0512)]


# ------------------------------------------------------------- worked examples

def test_example_3_1_hurdle():
    h = xd.risk_matched_hurdle(0.07, 0.055, 0.16, 0.08)
    assert h == R(0.085)
    deal, alt = 10 * 1.11 ** 5, 10 * 1.085 ** 5
    assert round(1.11 ** 5, 5) == 1.68506 and round(1.085 ** 5, 5) == 1.50366
    assert round(deal, 2) == 16.85 and round(alt, 2) == 15.04
    assert round(deal - alt, 2) == 1.81
    assert round((deal - alt) / 1.085 ** 5, 2) == 1.21
    assert (0.07 - 0.055) / 0.08 == R(0.1875)
    assert round((0.11 - 0.055) / 0.16, 3) == 0.344
    assert round((0.08 - 0.055) / 0.16, 3) == 0.156
    # boundary: equal risk -> hurdle equals the alternative
    assert xd.risk_matched_hurdle(0.07, 0.055, 0.08, 0.08) == R(0.07)


def test_example_3_2_reflexive_loop():
    m = xd.reflexive_loop_gain(0.70, 0.60, 100, 0.015)
    assert m == R(0.63)
    p = xd.reflexive_path(0.05, m, 5)
    assert [round(x, 5) for x in p["increments"]] == [0.05, 0.0315, 0.01985, 0.0125, 0.00788]
    cums = [sum(p["increments"][: k + 1]) for k in range(5)]
    assert [round(c, 5) for c in cums] == [0.05, 0.0815, 0.10135, 0.11385, 0.12172]
    assert round(p["total"], 4) == 0.1351
    assert round(p["multiplier"], 2) == 2.70
    assert p["cumulative"] == R(0.05 * (1 - m ** 5) / (1 - m))
    assert xd.reflexive_loop_gain(0.85, 0.80, 100, 0.015) == R(1.02)
    assert xd.reflexive_path(0.05, 1.02, 3)["total"] == math.inf


def test_example_3_3_mean_reversion():
    h = xd.ar1_half_life(0.90)
    assert round(h, 2) == 6.58 and round(h / 4, 2) == 1.64
    assert round(0.90 ** h, 3) == 0.5
    s4, s8 = xd.ar1_forecast(2.0, 3.0, 0.90, 4), xd.ar1_forecast(2.0, 3.0, 0.90, 8)
    assert round(s4, 3) == 2.344 and round(4.5 + s4, 3) == 6.844
    assert round(0.90 ** 8, 5) == 0.43047
    assert round(s8, 3) == 2.570 and round(4.5 + s8, 3) == 7.070
    assert round(6.5 / (4.5 + s8), 4) == 0.9194
    assert round(6.5 / (4.5 + s8) - 1, 4) == -0.0806
    assert round(xd.ar1_half_life(0.97), 2) == 22.76
    s8b = xd.ar1_forecast(2.0, 3.0, 0.97, 8)
    assert round(s8b, 3) == 2.216 and round(4.5 + s8b, 3) == 6.716
    assert round(6.5 / (4.5 + s8b) - 1, 4) == -0.0322
    assert round(xd.ar1_rescale(0.90, 4), 3) == 0.656
    assert round(xd.ar1_half_life(0.95), 1) == 13.5
    with pytest.raises(ValueError):
        xd.ar1_half_life(1.0)


def test_example_3_3_small_sample_bias_simulation():
    rng = random.Random(3)
    ests = []
    for _ in range(4000):
        x = [3.0]
        for _ in range(80):
            x.append(3.0 + 0.9 * (x[-1] - 3.0) + rng.gauss(0, 0.2))
        ests.append(xd.ar1_phi_ols(x[1:])["phi"])
    avg = sum(ests) / len(ests)
    assert 0.83 < avg < 0.87
    assert round(avg, 2) == 0.85


def test_example_3_4_momentum():
    r = [0.063, -0.039, 0.102, 0.024, -0.081, 0.045, 0.036, -0.012, 0.078, 0.027, -0.054, 0.033]
    sd_m = stats.stdev(r)
    vol = sd_m * math.sqrt(12)
    assert round(sd_m, 5) == 0.05494
    assert round(vol, 4) == 0.1903
    pos = xd.tsmom_position(r, vol, 0.10)
    assert round(pos["trailing"], 4) == 0.2259
    assert round(sum(r), 3) == 0.222
    assert pos["signal"] == 1
    assert round(pos["weight"], 4) == 0.5254
    assert round(pos["weight"] * 10, 2) == 5.25
    assert pos["weight"] * vol == R(0.10)
    neg = xd.tsmom_position([-x for x in r], vol, 0.10)
    assert round(neg["trailing"], 4) == -0.2143 and neg["signal"] == -1


def _exp_growth(p11, p22, g1, g2, start, quarters=4):
    out, con = 0.0, 0.0
    for k in range(1, quarters + 1):
        m = xd.markov2_nstep(p11, p22, k)[start]
        out += (m[0] * g1 + m[1] * g2) / 4
        con += m[1] / quarters
    return out, con


def test_example_3_5_regimes():
    assert xd.markov_expected_duration(0.95) == R(20)
    assert xd.markov_expected_duration(0.80) == R(5)
    pi1, pi2 = xd.markov2_stationary(0.95, 0.80)
    assert (pi1, pi2) == (R(0.80), R(0.20))
    from_exp = [round(xd.markov2_nstep(0.95, 0.80, k)[0][1], 4) for k in range(1, 5)]
    from_con = [round(xd.markov2_nstep(0.95, 0.80, k)[1][1], 4) for k in range(1, 5)]
    assert from_exp == [0.05, 0.0875, 0.1156, 0.1367]
    assert from_con == [0.80, 0.65, 0.5375, 0.4531]
    g_e, c_e = _exp_growth(0.95, 0.80, 0.04, -0.10, 0)
    g_c, c_c = _exp_growth(0.95, 0.80, 0.04, -0.10, 1)
    assert round(c_e, 4) == 0.0975 and round(g_e, 4) == 0.0264
    assert round(c_c, 4) == 0.6102 and round(g_c, 4) == -0.0454
    assert round(g_e - g_c, 3) == 0.072
    assert round(0.80 ** 8, 3) == 0.168
    assert round(0.95 ** 20, 3) == 0.358
    assert pi1 * 0.05 == R(pi2 * 0.20)


def test_example_3_6_option_to_wait():
    b = xd.binomial_wait(42.0, 40.0, 1.25, 0.80, 0.04, 0.06, 0.03)
    assert b["npv_now"] == R(2.0)
    assert (b["vu"], b["vd"], b["payout"], b["cost1"]) == (R(52.5), R(33.6), R(2.52), R(41.2))
    assert b["q"] == R(0.40)
    assert (b["fu"], b["fd"]) == (R(11.3), R(0.0))
    assert round(b["wait_value"], 3) == 4.346
    assert round(b["option_premium"], 3) == 2.346
    assert round(b["delta"], 5) == 0.59788
    assert round(b["bond"], 3) == -20.765
    assert b["replication_value"] == R(b["wait_value"])
    assert round(b["delta"] * 42.0, 3) == 25.111
    assert b["decision"] == "wait"


def test_example_3_7_forced_sale():
    assert round(7000 / 9200, 4) == 0.7609
    f0 = xd.forced_sale(100, 7000, 92, 0.75, 0.0)
    assert round(f0["units"], 2) == 4.35
    f = xd.forced_sale(100, 7000, 92, 0.75, 0.15)
    assert round(f["units"], 3) == 8.755
    assert round(f["price"], 3) == 90.687
    assert round(f["equity"], 1) == 2068.7
    assert round(2200 - f["equity"], 1) == 131.3
    assert round((2200 - f["equity"]) / 2200, 2) == 0.06
    assert round(math.sqrt(11.75 ** 2 - 4 * 0.0375 * 100), 4) == 11.0934
    assert round(f["critical_impact"], 4) == 0.3067
    bdag = (3550 - math.sqrt(700_000)) / 11_250
    assert round(bdag, 4) == 0.2412
    # the quadratic in b is the feasibility boundary: just below feasible, just above not
    assert xd.forced_sale(100, 7000, 92, 0.75, bdag - 1e-4)["feasible"]
    assert not xd.forced_sale(100, 7000, 92, 0.75, bdag + 1e-4)["feasible"]
    assert not xd.forced_sale(100, 7000, 92, 0.75, 0.30)["feasible"]
    # check: post-sale LTV = 75%
    s, p = f["units"], f["price"]
    debt_after, val_after = 7000 - s * p, (100 - s) * p
    assert round(debt_after, 1) == 6206.0 and round(val_after, 1) == 8274.7
    assert debt_after / val_after == R(0.75)
    # boundary: no breach -> no sale
    assert xd.forced_sale(100, 7000, 100, 0.75, 0.15)["units"] == 0.0


def test_example_3_8_crowding():
    assert xd.days_to_exit(60, 40, 0.20) == R(7.5)
    assert xd.days_to_exit(720, 40, 0.20) == R(90)
    assert xd.max_position(40, 0.20, 5) == R(40)
    assert round(40 / 12, 2) == 3.33
    assert round(200 / (0.25 * 450), 2) == 1.78
    assert xd.days_to_exit(60, 40 / 12, 0.20) == R(90)


def test_example_3_9_second_order():
    assert round(2_400_000 / (0.04 * 31_200_000), 2) == 1.92
    assert 0.65 * 48_000_000 == R(31_200_000)
    v = 2_400_000 / 0.0625
    assert v == R(38_400_000)
    k = tvm.loan_constant(0.065, 30)
    assert round(k, 6) == 0.075848
    ml = cre.max_loan(2_400_000, v, 0.065, 30, ltv_max=0.65, dscr_min=1.35, debt_yield_min=0.09)
    assert ml["ltv"] == R(24_960_000)
    assert round(ml["dscr"] / 1e6, 2) == 23.44
    assert round(ml["debt_yield"] / 1e6, 2) == 26.67
    assert ml["binding"] == "dscr"
    gap = cre.refinance_gap(31_200_000, ml["max_loan"])
    assert round(gap / 1e6, 2) == 7.76
    ratio = gap / 31_200_000
    assert round(ratio, 4) == 0.2488
    agg = ratio * 500
    assert round(agg, 1) == 124.4
    assert round(0.6 * agg, 1) == 74.6
    loss = 0.15 * 200
    assert loss == R(30) and loss / 0.10 == R(300)
    assert 300 / 0.60 == R(500)
    ds = ml["max_loan"] * k
    assert round(ds / 1e6, 3) == 1.778
    assert 2_400_000 / ds == R(1.35)


def test_example_3_10_bayes():
    seq = xd.bayes_sequence(0.20, [3.0, 1.5, 0.5])
    assert [round(x, 4) for x in seq] == [0.4286, 0.5294, 0.36]
    assert stats.bayes_posterior(0.20, 0.60, 0.20) == R(seq[0])
    assert stats.likelihood_ratio_update(0.20, 3.0 * 1.5 * 0.5) == R(0.36)
    for order in ([0.5, 3.0, 1.5], [1.5, 0.5, 3.0]):
        assert xd.bayes_sequence(0.20, order)[-1] == R(0.36)
    over = xd.bayes_sequence(0.20, [3.0, 1.5, 0.5], weight=2)
    under = xd.bayes_sequence(0.20, [3.0, 1.5, 0.5], weight=0.5)
    assert [round(x, 3) for x in over] == [0.692, 0.835, 0.559]
    assert [round(x, 3) for x in under] == [0.302, 0.347, 0.273]
    rows = {}
    for name, p in (("bayes", seq[-1]), ("over", over[-1]), ("under", under[-1])):
        ev = 24.0 - 6.0 * p
        rows[name] = (round(ev, 2), round(ev / 1.05, 2))
    assert rows == {"bayes": (21.84, 20.80), "over": (20.65, 19.67), "under": (22.36, 21.30)}
    assert rows["under"][1] > 21.0 > rows["bayes"][1]
    assert round(rows["bayes"][1] - rows["over"][1], 2) == 1.13
    # dependence: use only the larger of LR1, LR2
    assert round(stats.likelihood_ratio_update(0.20, 3.0 * 0.5), 3) == 0.273


def test_section_3_9_japan_arithmetic():
    assert round(1 - 14_309 / 38_915.87, 3) == 0.632


# ------------------------------------------------------------- problems

def test_problem_3_2():
    assert round(-0.693 / -0.223, 1) == 3.1
    assert round(xd.ar1_half_life(0.80), 3) == 3.106
    assert round(xd.ar1_half_life(0.95), 2) == 13.51
    assert round(xd.ar1_half_life(0.95) / 4, 2) == 3.38
    assert round(0.95 ** 4, 4) == 0.8145


def test_problem_3_3():
    seq = xd.bayes_sequence(0.30, [4, 0.5])
    assert [round(x, 3) for x in seq] == [0.632, 0.462]
    assert round(0.3 / 0.7 * 4, 3) == 1.714


def test_problem_3_4():
    m6 = xd.reflexive_loop_gain(0.60, 0.8, 110, 0.015)
    m7 = xd.reflexive_loop_gain(0.70, 0.8, 110, 0.015)
    assert (round(m6, 3), round(m7, 3)) == (0.792, 0.924)
    p6, p7 = xd.reflexive_path(-0.04, m6, 3), xd.reflexive_path(-0.04, m7, 3)
    assert (round(p6["multiplier"], 2), round(p7["multiplier"], 2)) == (4.81, 13.16)
    assert (round(p6["total"], 3), round(p7["total"], 3)) == (-0.192, -0.526)
    assert round(p6["cumulative"], 4) == -0.0968
    assert round((1 - m6 ** 3) / (1 - m6), 3) == 2.419
    assert round(1 / (0.8 * 110 * 0.015), 3) == 0.758


def test_problem_3_5():
    assert (xd.markov_expected_duration(0.90), xd.markov_expected_duration(0.75)) == (R(10), R(4))
    pi = xd.markov2_stationary(0.90, 0.75)
    assert (round(pi[0], 3), round(pi[1], 3)) == (0.714, 0.286)
    assert xd.markov2_nstep(0.90, 0.75, 2)[0][1] == R(0.165)
    assert round(xd.markov2_nstep(0.90, 0.75, 8)[0][1], 3) == 0.277
    assert round(0.75 ** 3, 3) == 0.422


def test_problem_3_6():
    a = xd.binomial_wait(30, 28, 1.30, 0.75, 0.04, 0.07, 0.02)
    assert a["q"] == R(0.40) and a["cost1"] == R(28.56) and a["fu"] == R(10.44)
    assert round(a["wait_value"], 3) == 4.015 and round(a["option_premium"], 3) == 2.015
    assert round(a["delta"], 5) == 0.63273 and round(a["bond"], 3) == -14.966
    assert a["replication_value"] == R(a["wait_value"])
    lo, hi = 0.0, 0.3
    for _ in range(100):
        mid = (lo + hi) / 2
        r = xd.binomial_wait(30, 28, 1.30, 0.75, 0.04, mid, 0.02)
        lo, hi = (mid, hi) if r["wait_value"] > r["npv_now"] else (lo, mid)
    assert round(lo, 3) == 0.180
    assert round((8.7 - 16.5 * 0.19923) / 30, 4) == 0.1804
    c = xd.binomial_wait(30, 28, 1.10, 0.90, 0.04, 0.07, 0.02)
    assert c["q"] == R(0.35) and round(c["wait_value"], 3) == 1.494
    assert c["decision"] == "build"


def test_problem_3_7():
    assert round(1800 / (50 * 46), 3) == 0.783
    assert round(xd.forced_sale(50, 1800, 46, 0.75, 0.0)["units"], 2) == 6.52
    f = xd.forced_sale(50, 1800, 46, 0.75, 0.20)
    assert f["units"] == R(30) and f["price"] == R(40) and f["equity"] == R(200)
    assert round(f["critical_impact"], 4) == 0.3067
    a, b, c = 1406.25, -937.5, 132.25
    bdag = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    assert round(bdag, 4) == 0.2027
    assert (11.5 + 37.5 * bdag) ** 2 == R(1800 * bdag)
    assert not xd.forced_sale(50, 1800, 46, 0.75, 0.21)["feasible"]


def test_problem_3_8():
    assert xd.days_to_exit(45, 25, 0.15) == R(12)
    assert xd.days_to_exit(300, 25, 0.15) == R(80)
    assert round(xd.max_position(25, 0.15, 10) / 8, 2) == 4.69
    assert xd.days_to_exit(30, 25, 0.15) == R(8)
    assert xd.days_to_exit(30, 25 / 8, 0.15) == R(64)
    assert round(xd.max_position(25, 0.15, 21) / 8, 1) == 9.8


def test_problem_3_9():
    v0 = 1_900_000 / 0.06
    assert round(v0 / 1e6, 2) == 31.67
    assert round(20e6 / v0, 3) == 0.632
    assert round(1.9e6 / (0.0375 * 20e6), 2) == 2.53
    v1 = 1_900_000 / 0.075
    assert round(v1 / 1e6, 2) == 25.33
    assert round(tvm.loan_constant(0.07, 25), 6) == 0.084814
    ml = cre.max_loan(1_900_000, v1, 0.07, 25, ltv_max=0.60, dscr_min=1.40, debt_yield_min=0.10)
    assert round(ml["ltv"] / 1e6, 2) == 15.20
    assert round(ml["dscr"] / 1e6, 2) == 16.00
    assert round(ml["debt_yield"] / 1e6, 2) == 19.00
    assert ml["binding"] == "ltv"
    gap = cre.refinance_gap(20e6, ml["max_loan"])
    assert gap == R(4.8e6) and gap / 20e6 == R(0.24)
    assert 0.20 * 400 == R(80)
    assert round(80 / 0.09) == 889


def test_problem_3_10():
    assert round(1 - 0.50 / 0.65, 3) == 0.231
    assert round(1 - 0.60 / 0.65, 3) == 0.077
    assert round(1 - 0.55 / 0.65, 3) == 0.154
