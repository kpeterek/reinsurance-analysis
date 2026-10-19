"""Reproduces every number in Chapter 18 text, problems, and solutions.

Library: sdesk.markets (Black-Scholes), sdesk.x_derivatives (new for Ch 18),
sdesk.x_capital_structure (Bachelier caps, reused from Ch 10).
"""

import math
import statistics

import pytest

from sdesk import markets as m
from sdesk import x_capital_structure as xc
from sdesk import x_derivatives as xd

R = pytest.approx


# --------------------------------------------------------------------------
# Library checks (independent routes and boundary cases)
# --------------------------------------------------------------------------

def test_theta_matches_finite_difference_and_pde():
    s, k, t, r, sig, q = 100, 95, 0.4, 0.03, 0.25, 0.01
    for kind in ("call", "put"):
        h = 1e-5
        fd = -(m.bs_price(s, k, t + h, r, sig, kind, q) - m.bs_price(s, k, t - h, r, sig, kind, q)) / (2 * h)
        assert xd.bs_theta(s, k, t, r, sig, kind, q) == R(fd, rel=1e-6)
        v = m.bs_price(s, k, t, r, sig, kind, q)
        lhs = (xd.bs_theta(s, k, t, r, sig, kind, q) + (r - q) * s * m.bs_delta(s, k, t, r, sig, kind, q)
               + 0.5 * sig ** 2 * s ** 2 * m.bs_gamma(s, k, t, r, sig, q))
        assert lhs == R(r * v, abs=1e-10)


def test_vega_gamma_identity():
    s, k, t, r, sig = 100, 110, 0.75, 0.04, 0.3
    assert m.bs_vega(s, k, t, r, sig) == R(sig * t * s * s * m.bs_gamma(s, k, t, r, sig))


def test_implied_vol_roundtrip_and_bounds():
    p = m.bs_price(100, 105, 0.5, 0.03, 0.27, "put")
    assert xd.bs_implied_vol(p, 100, 105, 0.5, 0.03, "put") == R(0.27, abs=1e-8)
    with pytest.raises(ValueError):
        xd.bs_implied_vol(0.0001, 100, 100, 0.5, 0.03)   # below intrinsic-of-forward bound


def test_black_and_bachelier_caplet_limits():
    # zero time: both equal intrinsic
    assert xd.black_caplet(0.05, 0.04, 0.3, 0.0, 0.25, 0.99, 1e6) == R(1e6 * 0.25 * 0.99 * 0.01)
    assert xc.bachelier_caplet(0.05, 0.04, 0.01, 0.0, 0.25, 0.99, 1e6) == R(1e6 * 0.25 * 0.99 * 0.01)
    # ATM, short expiry: Black ~ Bachelier with sigma_N = sigma_LN * F
    b = xd.black_caplet(0.04, 0.04, 0.25, 0.25, 0.25, 1.0)
    n = xc.bachelier_caplet(0.04, 0.04, 0.01, 0.25, 0.25, 1.0)
    assert b == R(n, rel=2e-3)


def test_swap_floating_leg_telescopes():
    dfs = xd.discount_factors_from_zero([0.03, 0.035, 0.04, 0.042], [1, 2, 3, 4], 1)
    fwd = [1 / dfs[0] - 1] + [dfs[i - 1] / dfs[i] - 1 for i in range(1, 4)]
    assert sum(f * d for f, d in zip(fwd, dfs)) == R(1 - dfs[-1])
    k = xd.par_swap_rate(dfs, [1, 1, 1, 1])
    assert xd.swap_value(1e6, k, dfs, [1, 1, 1, 1])["value_pay_fixed"] == R(0, abs=1e-6)


def test_merton_parity_and_zero_vol_limit():
    res = xd.merton_claims(50e6, 40e6, 2, 0.03, 0.2)
    assert res["equity"] + res["debt"] == R(50e6)
    assert res["equity"] - res["put"] == R(50e6 - 40e6 * math.exp(-0.06))
    low = xd.merton_claims(50e6, 40e6, 2, 0.03, 1e-4)
    assert low["spread"] == R(0, abs=1e-8)


def test_hedge_simulation_reproducible():
    a = xd.delta_hedge_simulation(100, 100, 0.25, 0.04, 0.2, 0.25, 63, seed=18)
    b = xd.delta_hedge_simulation(100, 100, 0.25, 0.04, 0.2, 0.25, 63, seed=18)
    assert a["pnl"] == b["pnl"] and a["path"] == b["path"]


# --------------------------------------------------------------------------
# Worked examples
# --------------------------------------------------------------------------

def test_example_18_1():
    s, k, t, r, q = 5000, 5000, 0.5, 0.04, 0.015
    assert s * math.exp(-q * t) == R(4962.64, abs=0.005)
    assert k * math.exp(-r * t) == R(4900.99, abs=0.005)
    par = s * math.exp(-q * t) - k * math.exp(-r * t)
    assert par == R(61.65, abs=0.005)
    assert s * math.exp((r - q) * t) == R(5062.89, abs=0.005)
    assert m.put_call_parity_gap(280, 230, s, k, t, r, q) == R(-11.65, abs=0.005)
    assert par - (281 - 229) == R(9.65, abs=0.005)
    c = m.bs_price(s, k, t, r, 0.18, "call", q)
    p = m.bs_price(s, k, t, r, 0.18, "put", q)
    assert (round(c, 2), round(p, 2)) == (282.28, 220.64)
    assert c - p == R(par)


def test_example_18_2():
    s, k, t, r, sig = 100, 90, 0.25, 0.04, 0.22
    d1, d2 = m._d1_d2(s, k, t, r, sig)
    assert (round(d1, 4), round(d2, 4)) == (1.1037, 0.9937)
    p = m.bs_price(s, k, t, r, sig, "put")
    d = m.bs_delta(s, k, t, r, sig, "put")
    g = m.bs_gamma(s, k, t, r, sig)
    v = m.bs_vega(s, k, t, r, sig)
    th = xd.bs_theta(s, k, t, r, sig, "put")
    assert round(p, 4) == 0.7870
    assert round(d, 4) == -0.1349
    assert round(g, 5) == 0.01972
    assert round(v / 100, 4) == 0.1085
    assert round(th / 365, 5) == -0.01151
    # PDE terms as displayed
    assert (round(th, 4), round(r * s * d, 4), round(0.5 * sig ** 2 * s ** 2 * g, 4), round(r * p, 4)) == \
        (-4.2022, -0.5394, 4.7731, 0.0315)
    assert th + r * s * d + 0.5 * sig ** 2 * s ** 2 * g - r * p == R(0, abs=1e-10)
    rows = {"a": (-10, 0.0), "b": (-10, 0.08), "c": (-5, 0.0), "d": (5, 0.0)}
    full = {key: m.bs_price(s + ds, k, t, r, sig + dv, "put") for key, (ds, dv) in rows.items()}
    assert [round(full[x], 4) for x in "abcd"] == [3.4963, 4.9180, 1.7549, 0.3170]
    assert [round(full[x] - p, 4) for x in "abcd"] == [2.7094, 4.1310, 0.9679, -0.4700]
    assert round(d * -10, 4) == 1.3485 and round(d * -5, 4) == 0.6743
    assert round(m.delta_gamma_pnl(d, g, -10), 4) == 2.3347
    assert round(m.delta_gamma_pnl(d, g, -5), 4) == 0.9208
    assert round(m.delta_gamma_pnl(d, g, 5), 4) == -0.4277
    assert round(v, 3) == 10.848 and round(v * 0.08, 4) == 0.8678
    assert round(m.delta_gamma_pnl(d, g, -10) + v * 0.08, 4) == 3.2026
    assert round(full["a"] - p - m.delta_gamma_pnl(d, g, -10), 2) == 0.37


def test_example_18_3():
    iv = xd.bs_implied_vol(2.60, 100, 100, 1 / 12, 0.04)
    assert round(iv, 4) == 0.2114
    assert round(iv / math.sqrt(252), 5) == 0.01332
    rets = [0.012, -0.008, 0.004, -0.015, 0.009, 0.002, -0.011, 0.006, -0.003, 0.010]
    lr = [math.log(1 + x) for x in rets]
    zero_mean = math.sqrt(252 / len(lr) * sum(x * x for x in lr))
    assert round(zero_mean, 4) == 0.1421
    assert round(statistics.stdev(lr) * math.sqrt(252), 4) == 0.1495
    assert sum(abs(x) > iv / math.sqrt(252) for x in rets) == 1
    assert round((0.2114 / 0.1421) ** 2, 1) == 2.2
    assert round(math.sqrt(2 / 10), 2) == 0.45


def _sim(sr, n, seed):
    return xd.delta_hedge_simulation(100, 100, 0.25, 0.04, 0.20, sr, n, seed=seed)


def test_example_18_4_seed_18():
    assert round(m.bs_price(100, 100, 0.25, 0.04, 0.20), 4) == 4.4852
    v = m.bs_vega(100, 100, 0.25, 0.04, 0.20)
    assert round(v, 3) == 19.724
    expected = {0.25: (0.2403, 1.0289, 0.9914, 1.7223),
                0.20: (0.1922, -0.4736, -0.4956, 0.0),
                0.15: (0.1441, -1.7954, -1.7731, -1.4722)}
    for sr, (rv, pnl, gp, th) in expected.items():
        res = _sim(sr, 63, 18)
        assert round(res["realized_vol"], 4) == rv
        assert round(res["pnl"], 4) == pnl
        assert round(res["gamma_pnl"], 4) == gp
        assert round(res["theory_pnl"], 4) == R(th, abs=1e-12)
    r25 = _sim(0.25, 63, 18)
    assert abs(r25["pnl"] - r25["gamma_pnl"]) < 0.04
    assert round(v * 0.05, 3) == 0.986
    assert round(v * (0.25 ** 2 - 0.2 ** 2) / (2 * 0.2), 3) == 1.109


EX184_TABLE = {
    (0.25, 13): (1.0595, 1.2978, 1.0094), (0.25, 63): (1.0468, 0.6768, 1.0214),
    (0.25, 252): (1.0255, 0.5248, 1.0135),
    (0.20, 13): (0.0360, 0.9795, 0.0), (0.20, 63): (0.0188, 0.4433, 0.0),
    (0.20, 252): (0.0067, 0.2251, 0.0),
    (0.15, 13): (-0.9860, 0.7907, -0.9906), (0.15, 63): (-0.9998, 0.4685, -1.0091),
    (0.15, 252): (-1.0015, 0.3727, -1.0035),
}


@pytest.mark.parametrize("key", list(EX184_TABLE), ids=lambda k: f"sr{k[0]}_n{k[1]}")
def test_example_18_4_many_seeds(key):
    sr, n = key
    runs = [_sim(sr, n, s) for s in range(1, 401)]
    pnl = [x["pnl"] for x in runs]
    th = [x["theory_pnl"] for x in runs]
    mean, sd, mth = EX184_TABLE[key]
    assert round(statistics.mean(pnl), 4) == mean
    assert round(statistics.stdev(pnl), 4) == sd
    assert round(statistics.mean(th), 4) == R(mth, abs=1e-12)
    if sr == 0.20 and n == 252:
        assert round(sd / math.sqrt(400), 3) == 0.011


def test_example_18_5():
    pr = xd.put_roll_cost(100, 0.90, 0.25, 0.04, 0.24, 0.015)
    assert round(pr["premium"], 4) == 1.0730
    assert round(pr["annual_cost_pct"], 5) == 0.04292
    n = 50e6
    assert round(pr["annual_cost_pct"] * n) == 2_146_067
    assert round((1 - pr["annual_cost_pct"]) ** 10, 3) == 0.645
    assert round(1 - (1 - pr["annual_cost_pct"]) ** 10, 3) == 0.355
    assert n * (0.90 - 0.70) == R(10e6)
    freq = pr["annual_cost_pct"] * n / 10e6
    assert round(freq, 3) == 0.215 and round(1 / freq, 1) == 4.7
    assert round(1 / (pr["annual_cost_pct"] * n / 5e6), 1) == 2.3
    p75 = m.bs_price(100, 75, 0.25, 0.04, 0.30, "put", 0.015)
    assert round(p75, 4) == 0.1217
    assert round(pr["premium"] - p75, 4) == 0.9513
    spread_annual = (pr["premium"] - p75) * 4 / 100
    assert round(spread_annual, 5) == 0.03805
    assert round(pr["annual_cost_pct"] - spread_annual, 4) == 0.0049
    assert round((pr["annual_cost_pct"] - spread_annual) / pr["annual_cost_pct"], 2) == 0.11
    assert n * 0.15 == R(7.5e6)
    hi = xd.put_roll_cost(100, 0.90, 0.25, 0.04, 0.30, 0.015)
    assert round(hi["premium"], 4) == 1.8698
    assert round(hi["annual_cost_pct"], 5) == 0.07479
    assert round(hi["annual_cost_pct"] / pr["annual_cost_pct"] - 1, 2) == 0.74
    atm_vol = m.bs_price(100, 90, 0.25, 0.04, 0.18, "put", 0.015)
    assert round(atm_vol, 4) == 0.4376
    assert round(pr["premium"] / atm_vol, 1) == 2.5


def test_example_18_6():
    h = xd.min_variance_hedge(0.75, 0.24, 0.17, 40e6, 5000, 50)
    assert round(h["hedge_ratio"], 4) == 1.0588
    assert round(h["contracts"], 1) == 169.4
    assert 169 * 5000 * 50 == 42_250_000
    assert h["effectiveness"] == R(0.5625)
    assert round(h["residual_vol"], 4) == 0.1587
    vm = 169 * 50 * 300
    assert vm == 2_535_000
    total = -0.02 * 40e6 - vm
    assert total == R(-3_335_000)
    assert total < -3_000_000
    assert 169 * 50 * 500 == 4_225_000


def test_example_18_7():
    z = [0.040, 0.038, 0.037]
    t = [1, 2, 3]
    acc = [1, 1, 1]
    dfs = xd.discount_factors_from_zero(z, t, 1)
    assert [round(x, 6) for x in dfs] == [0.961538, 0.928122, 0.896734]
    a = sum(dfs)
    assert round(a, 6) == 2.786395
    k = xd.par_swap_rate(dfs, acc)
    assert round(k, 6) == 0.037061
    dn = xd.discount_factors_from_zero([x - 0.01 for x in z], t, 1)
    s = xd.swap_value(45e6, k, dn, acc)
    assert round(s["annuity"], 6) == 2.840326
    assert round(s["par_rate"], 6) == 0.027044
    assert round(s["floating_leg"]) == 3_456_682
    assert round(s["fixed_leg"]) == 4_736_903
    assert round(s["value_pay_fixed"]) == -1_280_221
    assert 45e6 * s["annuity"] * (s["par_rate"] - k) == R(s["value_pay_fixed"])
    up1 = xd.swap_value(45e6, k, xd.discount_factors_from_zero([x + 0.0001 for x in z], t, 1), acc)
    assert round(up1["value_pay_fixed"]) == 12_557
    assert round(45e6 * a * 1e-4) == 12_539
    up100 = xd.swap_value(45e6, k, xd.discount_factors_from_zero([x + 0.01 for x in z], t, 1), acc)
    assert round(up100["value_pay_fixed"]) == 1_232_353
    assert xd.swap_value(45e6, k, dfs, acc)["value_pay_fixed"] == R(0, abs=0.005)


def test_example_18_8():
    n, f, noi, sp = 45e6, 0.036, 5.2e6, 0.0375
    kmax = noi / (1.40 * n) - sp
    assert round(kmax, 5) == 0.04504
    assert round(noi / (n * (0.045 + sp)), 4) == 1.4007
    c = xc.cap_premium(n, 0.045, f, 0.010, 3)
    assert round(c["premium"]) == 183_583
    assert round(c["pct_notional"], 5) == 0.00408
    assert round(c["annuity"], 4) == 2.8316
    assert round(c["annual_bp_equivalent"], 1) == 14.4
    assert len(c["caplets"]) == 11
    assert (round(c["caplets"][0]), round(c["caplets"][-1])) == (789, 30_984)
    grid = xd.bachelier_cap_grid(n, f, 3, [0.035, 0.040, 0.045, 0.050], [0.007, 0.010, 0.013])
    expected = {0.035: (438_698, 599_445, 760_636), 0.040: (194_604, 342_061, 495_787),
                0.045: (76_738, 183_583, 311_046), 0.050: (27_110, 93_525, 189_122)}
    for k, vals in expected.items():
        assert tuple(round(grid[(k, v)]) for v in (0.007, 0.010, 0.013)) == vals
    assert [round(xc.cap_premium(n, k, f, 0.010, 3)["annual_bp_equivalent"], 1)
            for k in (0.035, 0.040, 0.045, 0.050)] == [47.0, 26.8, 14.4, 7.3]
    bump = xc.cap_premium(n, 0.045, f, 0.011, 3)["premium"] - c["premium"]
    assert round(bump) == 40_808
    assert round(bump / c["premium"], 2) == 0.22
    sl = 0.010 / f
    assert round(sl, 4) == 0.2778
    for k, bach, black in [(0.035, 599_445, 589_046), (0.045, 183_583, 230_168), (0.055, 45_115, 95_497)]:
        assert round(xc.cap_premium(n, k, f, 0.010, 3)["premium"]) == bach
        assert round(xd.black_cap_premium(n, k, f, sl, 3)["premium"]) == black
    assert [round(b / a, 2) for a, b in [(599_445, 589_046), (183_583, 230_168), (45_115, 95_497)]] == [0.98, 1.25, 2.12]
    repl = xc.cap_premium(n, 0.045, 0.0475, 0.010, 3)["premium"]
    assert round(repl) == 683_477
    assert round(repl / c["premium"], 1) == 3.7
    # intrinsic check for the 3.50% strike
    ann_2_12 = sum(0.25 * (1 + f * 0.25) ** (-j) for j in range(2, 13))
    assert round(n * 0.001 * ann_2_12) == 116_274
    assert round(116_274 / 599_445, 2) == 0.19
    assert round(0.010 * math.sqrt(2.75) * 1e4) == 166
    assert round(noi / (n * (0.06 + sp)), 2) == 1.19
    assert 342_061 - 183_583 == 158_478
    assert n * 0.005 == R(225_000)
    assert round(311_046 / 183_583 - 1, 2) == 0.69


def test_example_18_9():
    assert round(45e6 * math.exp(-0.12)) == 39_911_420
    rows = {(60e6, 0.12): (20_183_873, 95_292, 39_816_127, 0.0316, 8.0),
            (60e6, 0.18): (20_766_248, 677_668, 39_233_752, 0.1247, 57.1),
            (60e6, 0.25): (22_031_108, 1_942_527, 37_968_892, 0.2342, 166.3),
            (48e6, 0.12): (9_019_661, 931_080, 38_980_339, 0.2165, 78.7),
            (48e6, 0.18): (10_405_572, 2_316_991, 37_594_428, 0.3314, 199.4),
            (48e6, 0.25): (12_239_830, 4_151_250, 35_760_170, 0.4170, 366.1)}
    for (v, sg), (e, p, d, pd, spr) in rows.items():
        res = xd.merton_claims(v, 45e6, 3, 0.04, sg)
        assert (round(res["equity"]), round(res["put"]), round(res["debt"])) == (e, p, d)
        assert round(res["pd_rn"], 4) == pd
        assert round(res["spread"] * 1e4, 1) == spr
        assert res["equity"] + res["debt"] == R(v)
    assert 20_183_873 - 95_292 == R(60e6 - 39_911_420, abs=1)
    assert round((22_031_108 - 20_183_873) / 1e6, 2) == 1.85
    assert round((12_239_830 - 9_019_661) / 1e6, 2) == 3.22


def test_section_18_8_and_episode_arithmetic():
    # two-day round trip
    x = 0.05
    for lev, mult in [(-1, 1), (2, 4)]:
        prod = (1 + lev * x) * (1 - lev * x)
        assert 1 - prod == R(mult * x * x)
    # rebalancing trade L(L-1)Ax, and direct check
    a = 1000.0
    for lev in (-1, 2):
        xx = 0.5
        need = lev * a * (1 + lev * xx) - lev * a * (1 + xx)
        assert need == R(lev * (lev - 1) * a * xx)
        assert need == R(2 * a * xx)
    assert 2 * 1000 * 0.50 == 1000
    assert 1000 * (1 - 0.50) == 500 and 1000 * (1 + 0.50) == 1500
    assert 1 - 0.96 == R(0.04)            # -1x daily product after a +96% day
    assert 1 - 0.80 == R(0.20)            # acceleration threshold


# --------------------------------------------------------------------------
# Problems
# --------------------------------------------------------------------------

def test_problem_18_2():
    assert round(100 - 100 * math.exp(-0.05), 3) == 4.877
    assert round(0.16 / math.sqrt(252), 5) == 0.01008
    assert round(100 * math.exp(0.03), 2) == 103.05


def test_problem_18_3():
    per = m.delta_gamma_pnl(0.55, 0.03, 4)
    assert per == R(2.44)
    assert per * 1000 == R(2440)
    assert 0.5 * 0.03 * 16 * 1000 == R(240)


def test_problem_18_4():
    s, k, t, r, sig = 50, 52, 0.5, 0.045, 0.30
    d1, d2 = m._d1_d2(s, k, t, r, sig)
    assert (round(d1, 6), round(d2, 6)) == (0.027244, -0.184888)
    assert (round(m.norm_cdf(d1), 6), round(m.norm_cdf(d2), 6)) == (0.510867, 0.426658)
    c = m.bs_price(s, k, t, r, sig)
    p = m.bs_price(s, k, t, r, sig, "put")
    assert (round(c, 4), round(p, 4)) == (3.8508, 4.6938)
    assert round(c - p, 4) == -0.8431
    assert round(s - k * math.exp(-r * t), 4) == -0.8431
    assert m.put_call_parity_gap(c, p, s, k, t, r) == R(0, abs=1e-12)
    assert round(m.bs_delta(s, k, t, r, sig), 4) == 0.5109
    assert round(m.bs_delta(s, k, t, r, sig, "put"), 4) == -0.4891
    assert round(m.bs_gamma(s, k, t, r, sig), 5) == 0.03760
    assert round(m.bs_vega(s, k, t, r, sig) / 100, 4) == 0.1410
    assert round(xd.bs_theta(s, k, t, r, sig) / 365, 5) == -0.01426
    assert round(xd.bs_theta(s, k, t, r, sig, "put") / 365, 5) == -0.00799


def test_problem_18_5():
    iv = xd.bs_implied_vol(4.10, 80, 80, 0.25, 0.04)
    assert round(iv, 4) == 0.2324
    v = m.bs_vega(80, 80, 0.25, 0.04, iv)
    assert round(v, 3) == 15.793
    assert round(v * (0.22 - iv), 4) == -0.1961
    assert round(v * (0.22 - iv) * 5000) == -981


def test_problem_18_6():
    dfs = [0.9800, 0.9420, 0.9050]
    sw = xd.swap_value(30e6, 0.035, dfs, [1, 1, 1], next_float_fixing=0.042)
    assert sw["annuity"] == R(2.8270)
    assert sw["fixed_leg"] == R(2_968_350)
    assert 30e6 * 1.042 * 0.98 == R(30_634_800)
    assert sw["floating_leg"] == R(3_484_800)
    assert sw["value_pay_fixed"] == R(516_450)
    assert round(0.98 / 0.942 - 1, 4) == 0.0403
    assert round(0.942 / 0.905 - 1, 4) == 0.0409


def test_problem_18_7():
    a = xc.cap_premium(25e6, 0.04, 0.038, 0.009, 2)
    b = xc.cap_premium(25e6, 0.04, 0.038, 0.012, 2)
    c = xc.cap_premium(25e6, 0.05, 0.038, 0.009, 2)
    assert len(a["caplets"]) == 7
    assert round(a["annuity"], 4) == 1.9171
    assert (round(a["premium"]), round(a["pct_notional"], 5), round(a["annual_bp_equivalent"], 1)) == \
        (106_007, 0.00424, 22.1)
    assert (round(b["premium"]), round(b["pct_notional"], 5), round(b["annual_bp_equivalent"], 1)) == \
        (152_792, 0.00611, 31.9)
    assert (round(c["premium"]), round(c["pct_notional"], 5), round(c["annual_bp_equivalent"], 1)) == \
        (17_578, 0.00070, 3.7)
    assert round(b["premium"] - a["premium"]) == 46_785
    assert round(b["premium"] / a["premium"] - 1, 2) == 0.44


def test_problem_18_8():
    i = xd.put_roll_cost(100, 0.95, 0.25, 0.04, 0.20, 0.015)
    ii = xd.put_roll_cost(100, 0.80, 0.25, 0.04, 0.28, 0.015)
    assert (round(i["premium"], 4), round(i["annual_cost_pct"], 5)) == (1.6978, 0.06791)
    assert (round(ii["premium"], 4), round(ii["annual_cost_pct"], 5)) == (0.2633, 0.01053)
    assert round((1 - i["annual_cost_pct"]) ** 10, 3) == 0.495
    assert round(i["annual_cost_pct"] / 0.30, 3) == 0.226
    assert round(0.30 / i["annual_cost_pct"], 1) == 4.4
    assert round(ii["annual_cost_pct"] / 0.15, 4) == 0.0702
    assert round(0.15 / ii["annual_cost_pct"], 1) == 14.2


def test_problem_18_9():
    assert round(30e6 * math.exp(-0.08)) == 27_693_490
    rows = {(30e6, 0.15): (3_760_436, 1_453_926, 26_239_564, 270, 0.393),
            (30e6, 0.30): (6_083_954, 3_777_444, 23_916_046, 733, 0.509),
            (36e6, 0.15): (8_653_607, 347_097, 27_346_393, 63, 0.129),
            (36e6, 0.30): (10_472_955, 2_166_445, 25_527_045, 407, 0.342)}
    for (v, sg), (e, p, d, spr, pd) in rows.items():
        res = xd.merton_claims(v, 30e6, 2, 0.04, sg)
        assert (round(res["equity"]), round(res["put"]), round(res["debt"])) == (e, p, d)
        assert round(res["spread"] * 1e4) == spr
        assert round(res["pd_rn"], 3) == pd
    assert 6_083_954 - 3_760_436 == 2_323_518
    assert 10_472_955 - 8_653_607 == 1_819_348


def test_problem_18_10():
    pp = m.bs_price(100, 90, 1 / 12, 0.04, 0.20, "put", 0.015)
    assert round(pp, 4) == 0.0668
    monthly = 5 * pp / 100
    assert round(monthly, 5) == 0.00334
    assert round((1 + monthly) ** 12 - 1, 4) == 0.0408
    lev = 0.01 / (pp / 100)
    assert round(lev, 1) == 15.0
    assert round(5 * 0.15 - monthly, 4) == 0.7467
    assert round(15 * 0.15 - 0.01, 2) == 2.24
