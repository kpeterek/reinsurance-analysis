"""Reproduces every number in Chapter 21 text, problems, and solutions."""

import math

import pytest

from sdesk import markets as mk
from sdesk import risk
from sdesk import x_dynamics as xd
from sdesk import x_microstructure as xm
from sdesk import x_risk_mgmt as xr

R = pytest.approx
Z99 = mk.norm_ppf(0.99)


def _binom_tail(n, p, k):
    return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))


# ---------------------------------------------------------------- library checks

def test_constants_and_library_identities():
    assert round(Z99, 4) == 2.3263
    assert round(mk.norm_pdf(Z99) / 0.01, 4) == 2.6652
    # ES/VaR via library equals the multipliers
    assert risk.parametric_es(1, 0, 1, 0.99) == R(mk.norm_pdf(Z99) / 0.01)
    # liquidation factor: closed form equals the explicit sum
    for t in (1, 4, 16, 20):
        s = sum(((t - j + 1) / t) ** 2 for j in range(1, t + 1))
        assert xr.liquidation_variance_factor(t) == R(s)
    assert xr.liquidation_variance_factor(1) == R(1.0)
    # gambler's ruin satisfies its recursion and boundaries
    p, n = 0.53, 40
    pr = [xr.gamblers_ruin(p, k, n) for k in range(n + 1)]
    assert pr[0] == R(1.0) and pr[-1] == R(0.0, abs=1e-12)
    for k in range(1, n):
        assert pr[k] == R(p * pr[k + 1] + (1 - p) * pr[k - 1])
    # first-passage: finite horizon converges to infinite-horizon value
    assert xr.prob_below_within(0.5, 0.05, 0.2, 2000) == R(xr.prob_ever_below(0.5, 0.05, 0.2), rel=1e-6)
    assert xr.prob_ever_below(0.5, -0.01, 0.2) == 1.0
    # Kelly estimation penalty equals 1/(2T) when s = sigma/sqrt(T)
    for t in (5, 20, 50):
        pen = xr.kelly_growth(risk.kelly_continuous(0.06, 0, 0.16), 0.06, 0.16) - \
            xr.kelly_growth_with_estimation(1, 0.06, 0.16, 0.16 / math.sqrt(t))
        assert pen == R(1 / (2 * t))
    # discrete VaR/ES on a continuous-like boundary
    assert xr.discrete_var_es([0, 1], [0.5, 0.5], 0.5)["var"] == 0


# ---------------------------------------------------------------- examples

def test_example_21_1():
    nav = 60e6
    assert risk.position_size_by_stop(nav, 0.005, 5000, 4850, 50) == R(40)
    assert 5000 * 50 * 0.012 == R(3000)
    assert xr.size_by_volatility(0.0025 * nav, 5000, 50, 0.012) == R(50)
    assert Z99 * 3000 == R(6979, abs=1)
    n = xr.size_by_var_budget(0.01 * nav * 0.40, 5000, 50, 0.012)
    assert round(n, 2) == 34.39 and math.floor(n) == 34
    # check: stop is 2.5 daily sigma
    assert (150 / 5000) / 0.012 == R(2.5)
    assert 40 * 2.5 * 3000 == R(300_000)


def test_example_21_2_1987():
    n = risk.position_size_by_stop(10e6, 0.01, 280.0, 280.0 * 0.97, 500)
    assert 280 * 0.97 == R(271.60)
    assert 8.40 * 500 == R(4200)
    assert round(n, 2) == 23.81 and math.floor(n) == 23
    notional = 23 * 280 * 500
    assert notional == 3_220_000
    sd = 0.15 / math.sqrt(252)
    assert round(math.sqrt(252), 3) == 15.875
    assert round(sd, 5) == 0.00945
    var = risk.parametric_var(notional, 0.0, sd, 0.99)
    es = risk.parametric_es(notional, 0.0, sd, 0.99)
    assert round(var, 2) == 70781.79
    assert round(es, 2) == 81092.18
    assert round(Z99 * sd * 140_000) == 3077
    assert 23 * 4200 == 96_600
    loss = 0.2047 * notional
    assert loss == R(659_134)
    assert round(loss / 10e6, 4) == 0.0659
    assert round(loss / 96_600, 1) == 6.8
    zmove = 0.2047 / sd
    assert round(zmove, 1) == 21.7
    p = 0.5 * math.erfc(zmove / math.sqrt(2))
    assert round(math.log10(p)) == -104
    assert round(notional / 10e6, 3) == 0.322
    assert round(0.2047 * 25e6 / 10e6, 2) == 0.51


def _two_asset(rho):
    tsy = 25e6 * 8 * 0.0007
    es = 34 * 5000 * 50 * 0.012
    return tsy, es, risk.portfolio_volatility([1, 1], [tsy, es], [[1, rho], [rho, 1]])


def test_example_21_3():
    tsy, es, sp = _two_asset(-0.3)
    assert (tsy, es) == (R(140_000), R(102_000))
    assert round(Z99 * tsy) == 325_689 and round(Z99 * es) == 237_287
    assert round(Z99 * (tsy + es)) == 562_976
    assert round(sp) == 146_410
    assert round(Z99 * sp) == 340_601
    c_t = Z99 * (tsy ** 2 - 0.3 * tsy * es) / sp
    c_e = Z99 * (es ** 2 - 0.3 * tsy * es) / sp
    assert round(c_t) == 243_359
    assert round(c_e) == 97_242
    assert c_t + c_e == R(Z99 * sp)
    assert round(c_t / (Z99 * sp), 2) == 0.71
    table = {-0.3: (146_410, 340_601, 1_077_076), 0.0: (173_217, 402_962, 1_274_278),
             0.5: (210_438, 489_551, 1_548_097), 1.0: (242_000, 562_976, 1_780_287)}
    for rho, (s, v, v10) in table.items():
        _, _, spr = _two_asset(rho)
        assert round(spr) == s
        assert round(Z99 * spr) == v
        assert round(Z99 * spr * math.sqrt(10)) == v10
    assert round(489_551 / 340_601 - 1, 2) == 0.44
    # three CRE-linked positions
    w, v = [10e6, 9e6, 6e6], [0.25, 0.30, 0.15]
    tot = sum(a * b for a, b in zip(w, v))
    assert tot == R(6.10e6)
    out = {}
    for rho in (0.4, 0.9, 1.0):
        c = [[1 if i == j else rho for j in range(3)] for i in range(3)]
        out[rho] = risk.portfolio_volatility(w, v, c)
    assert round(out[0.4] / 1e6, 2) == 4.85 and round(out[0.4] / tot, 3) == 0.795
    assert round(out[0.9] / 1e6, 2) == 5.91 and round(out[0.9] / tot, 3) == 0.969
    assert out[1.0] == R(6.10e6)


def test_example_21_4():
    worst = [-620, -540, -505, -470, -455, -430, -410, -395]
    pnl = worst + [50.0] * 492
    assert len(pnl) == 500
    var = risk.historical_var(pnl, 0.99)
    es = risk.historical_es(pnl, 0.99)
    assert var == 430
    assert es == R(503.3333, abs=1e-3)
    assert sorted(pnl)[4] == -455
    assert round(455 / 430 - 1, 3) == 0.058
    _, _, sp = _two_asset(-0.3)
    pes = risk.parametric_es(sp, 0, 1, 0.99)
    assert round(pes) == 390_215
    assert round(430_000 / (Z99 * sp), 2) == 1.26
    assert round(503_333.33 / pes, 2) == 1.29


def test_example_21_5():
    single = xr.discrete_var_es([0, 5], [0.96, 0.04], 0.95)
    assert single["var"] == 0
    assert single["es"] == R(4.0)
    p = 0.04
    probs = [(1 - p) ** 2, 2 * p * (1 - p), p * p]
    assert probs[1] == R(0.0768) and probs[2] == R(0.0016) and probs[0] == R(0.9216)
    assert 1 - probs[0] == R(0.0784)
    pair = xr.discrete_var_es([0, 5, 10], probs, 0.95)
    assert pair["var"] == 5
    assert pair["es"] == R(5.16)
    assert pair["var"] > 2 * single["var"]
    assert pair["es"] <= 2 * single["es"]


def _put_book():
    s0, k, t, r, sig, h = 5000, 4750, 21 / 252, 0.04, 0.18, 10 / 252
    p0 = mk.bs_price(s0, k, t, r, sig, "put")

    def reval(x, volfn=lambda x: sig):
        return -40 * 50 * (mk.bs_price(s0 * math.exp(x), k, t - h, r, volfn(x), "put") - p0)
    return p0, reval, sig * math.sqrt(h)


def test_example_21_6():
    p0, reval, sh = _put_book()
    assert round(p0, 2) == 19.08
    assert round(40 * 50 * p0) == 38_161
    d = mk.bs_delta(5000, 4750, 21 / 252, 0.04, 0.18, "put")
    assert round(d, 4) == -0.1407
    pos_delta = -40 * 50 * d
    assert round(pos_delta, 1) == 281.4
    assert round(pos_delta / 50, 1) == 5.6
    assert round(sh, 5) == 0.03586
    var_dn = Z99 * pos_delta * 5000 * sh
    assert round(var_dn) == 117_349
    mc = xr.mc_var_es(reval, sh, 20000, 0.99, seed=21)
    assert round(mc["var"]) == 292_336
    assert round(mc["es"]) == 378_887
    mc2 = xr.mc_var_es(lambda x: reval(x, lambda x: max(0.18, 0.18 - 1.5 * x)), sh, 20000, 0.99, seed=21)
    assert round(mc2["var"]) == 372_800
    assert round(mc2["es"]) == 456_374
    ds = 5000 * (math.exp(-Z99 * sh) - 1)
    assert round(ds) == -400
    assert round(-reval(-Z99 * sh)) == 287_227
    g = mk.bs_gamma(5000, 4750, 21 / 252, 0.04, 0.18)
    dg = -(pos_delta * ds + 0.5 * (-40 * 50 * g) * ds ** 2)
    assert round(dg) == 250_218
    assert round(mc["var"] / var_dn, 1) == 2.5 and round(mc2["var"] / var_dn, 1) == 3.2


def test_example_21_7():
    f = risk.kelly_continuous(0.06, 0, 0.16)
    assert f == R(2.34375)
    g_star = xr.kelly_growth(f, 0.06, 0.16)
    assert round(g_star, 4) == 0.0703
    rows = {0.25: (0.586, 0.0308, 0.4375, 0.094), 0.5: (1.172, 0.0527, 0.75, 0.1875),
            0.75: (1.758, 0.0659, 0.9375, 0.281), 1.0: (2.344, 0.0703, 1.0, 0.375),
            1.5: (3.516, 0.0527, 0.75, 0.5625), 2.0: (4.688, 0.0, 0.0, 0.75)}
    for c, (ff, g, share, vol) in rows.items():
        assert round(c * f, 3) == ff
        gc = xr.kelly_growth(c * f, 0.06, 0.16)
        assert round(gc, 4) == R(g, abs=1e-12)
        assert gc / g_star == R(share, abs=1e-12)
        assert gc == R(g_star * c * (2 - c))
        assert round(c * f * 0.16, 4 if vol in (0.1875, 0.5625) else 3) == vol
    se = 0.16 / math.sqrt(20)
    assert round(se, 4) == 0.0358 and se ** 2 == R(0.00128)
    assert 0.5 * se ** 2 / 0.16 ** 2 == R(0.025)
    assert round(xr.kelly_growth_with_estimation(1, 0.06, 0.16, se), 4) == 0.0453
    assert round(xr.kelly_growth_with_estimation(0.5, 0.06, 0.16, se), 4) == 0.0465
    k = xr.kelly_optimal_shrink(0.06, se)
    assert round(k, 3) == 0.738
    assert round(xr.kelly_growth_with_estimation(k, 0.06, 0.16, se), 4) == 0.0519
    assert xr.kelly_growth(f, 0.03, 0.16) == R(0.0, abs=1e-15)


def test_example_21_8():
    f = risk.kelly_continuous(0.06, 0, 0.16)
    res = {}
    for c in (1.0, 2 / 3, 0.5):
        ff = c * f
        m, s = xr.kelly_growth(ff, 0.06, 0.16), ff * 0.16
        res[c] = (m, s, 2 * m / s ** 2, xr.prob_ever_below(0.5, m, s), xr.prob_ever_below(0.3, m, s),
                  xr.prob_below_within(0.5, m, s, 10))
    assert res[1.0][0] == R(0.0703125) and res[1.0][1] == R(0.375)
    assert res[0.5][0] == R(0.052734375) and res[0.5][1] == R(0.1875)
    assert [round(res[c][2], 6) for c in (1.0, 2 / 3, 0.5)] == [1, 2, 3]
    assert [round(res[c][3], 4) for c in (1.0, 2 / 3, 0.5)] == [0.5, 0.25, 0.125]
    assert [round(res[c][4], 3) for c in (1.0, 2 / 3, 0.5)] == [0.7, 0.49, 0.343]
    assert [round(res[c][5], 3) for c in (1.0, 2 / 3, 0.5)] == [0.371, 0.164, 0.069]
    for c, (p_mdd, med) in {1.0: (0.86875, 0.653), 0.5: (0.1865, 0.384)}.items():
        m, s = res[c][0], res[c][1]
        mdd = xr.simulate_max_drawdowns(m, s, 10, 52, 4000, seed=21)
        assert sum(x >= 0.5 for x in mdd) / len(mdd) == R(p_mdd, abs=0.0006)
        assert round(sorted(mdd)[len(mdd) // 2], 3) == med
    # (b) gambler's ruin
    rho = 0.47 / 0.53
    assert round(rho, 4) == 0.8868
    assert round(xr.gamblers_ruin(0.53, 10), 3) == 0.301
    assert round(xr.gamblers_ruin(0.53, 20), 4) == 0.0905
    assert round(xr.gamblers_ruin(0.53, 10, 20), 3) == 0.231
    assert round(xr.gamblers_ruin(0.53, 20, 40), 3) == 0.083
    assert xr.gamblers_ruin(0.5, 20, 40) == R(0.5)
    assert xr.gamblers_ruin(0.53, 20) == R(xr.gamblers_ruin(0.53, 10) ** 2)
    # (c) simulate_fixed_fraction on Chapter 1's bet
    exp = {1 / 6: (0.00415, 1.514, 0.271), 1 / 3: (0.0, 1.000, 0.6795), 0.5: (-0.01266, 0.282, 0.853),
           1.0: (-0.11157, None, 0.9965)}
    for fr, (g, med, ruin) in exp.items():
        assert round(risk.expected_log_growth([0.6, -0.5], [0.5, 0.5], fr), 5) == R(g, abs=1e-12)
        sim = risk.simulate_fixed_fraction([0.6, -0.5], [0.5, 0.5], fr, 100, 4000, seed=7, ruin_level=0.5)
        if med is not None:
            assert round(sim["median"], 3) == med
        else:
            assert sim["median"] < 2e-5
        assert sim["ruin_prob"] == R(ruin)
    assert math.exp(100 * risk.expected_log_growth([0.6, -0.5], [0.5, 0.5], 1 / 6)) == R(1.514, abs=5e-4)


def test_example_21_9():
    t = xd.days_to_exit(1_000_000, 250_000, 0.20)
    assert t == R(20)
    v1 = risk.parametric_var(20e6, 0, 0.02, 0.99)
    assert round(v1) == 930_539
    fac = xr.liquidation_variance_factor(20)
    assert fac == R(7.175)
    assert round(math.sqrt(fac), 3) == 2.679
    assert round(v1 * math.sqrt(fac)) == 2_492_560
    assert round(v1 * math.sqrt(20)) == 4_161_498
    assert round(xr.liquidity_adjusted_var(v1 * math.sqrt(fac), 20e6, 0.01)) == 2_592_560
    assert round(xr.liquidity_adjusted_var(v1, 20e6, 0.002)) == 950_539
    assert xd.days_to_exit(200_000, 250_000, 0.2) == R(4)
    assert xd.max_position(250_000, 0.2, 5) == R(250_000)
    assert round(2_592_560 / 60e6, 3) == 0.043
    assert 20 / 3 < fac


def test_example_21_10():
    mc = xr.futures_margin_call(1_000_000, 34, 50, 24_000, 22_000)
    assert round(mc["trigger_points"], 1) == 148.2
    assert round(mc["trigger_points"] / 5000, 4) == 0.0296
    assert mc["call_at_trigger"] == 68_000
    loss = 34 * 500 * 50
    assert loss == 850_000
    assert 34 * 24_000 - (1_000_000 - loss) == 666_000
    cov = xr.ltv_covenant(21e6, 30e6, 0.75)
    assert round(cov["breach_decline"], 4) == 0.0667
    assert cov["cure"](25.5e6) == R(1_875_000)
    assert cov["cure"](19.5e6) == R(6_375_000)
    v_b = 30e6 * (1 - cov["breach_decline"])
    assert v_b == R(28e6) and 21e6 / v_b == R(0.75)


def test_example_21_11():
    g = xr.gap_loss(5000, 4850, 4700, 34, 50)
    assert g["planned"] == 255_000 and g["realized"] == 510_000 and g["ratio"] == R(2.0)
    put = mk.bs_price(5000, 4850, 1 / 12, 0.04, 0.18, "put")
    assert round(put, 2) == 39.66
    cost = 34 * 50 * put
    assert round(cost) == 67_424
    assert round(cost / 8.5e6, 4) == 0.0079
    assert round(12 * cost / 8.5e6, 3) == 0.095
    assert round(255_000 + cost) == 322_424


def test_example_21_12():
    assert 20 * 0.0005 == R(0.01)
    assert (0.05 - 0.01) / 0.10 == R(0.40)
    assert 8 * 0.006 == R(0.048)
    assert (0.05 - 0.048) / 0.10 == R(0.02)
    rt = xm.round_trip_cost(0.02, 0.03)
    assert round(rt, 4) == 0.0490
    assert round(xm.annualized_cost_drag(rt, 3), 4) == 0.0166
    assert round(xm.annualized_cost_drag(rt, 7), 4) == 0.0072


def _stress(dy, des, dv, dl):
    tsy = 25e6 * (-8 * dy + 0.5 * 75 * dy * dy)
    es = 34 * 5000 * 50 * des
    hotel = max(30e6 * (1 + dv) - 21e6, 0) - 9e6
    loan = 15e6 * dl
    return [tsy, es, hotel, loan]


def test_example_21_13():
    a = _stress(-0.015, -0.40, -0.35, -0.12)
    b = _stress(0.02, -0.20, -0.15, -0.05)
    assert round(-8 * -0.015 + 0.5 * 75 * 0.015 ** 2, 5) == 0.12844
    assert a == [R(3_210_937.5), R(-3_400_000), R(-9_000_000), R(-1_800_000)]
    assert [round(x) for x in b] == [-3_625_000, -1_700_000, -4_500_000, -750_000]
    assert round(sum(a)) == -10_989_062 or round(sum(a)) == -10_989_063
    assert round(sum(b)) == -10_575_000
    assert round(sum(a) / 60e6, 3) == -0.183
    assert round(sum(b) / 60e6, 3) == -0.176
    ha = xr.herfindahl([x for x in a if x < 0])
    hb = xr.herfindahl([x for x in b if x < 0])
    assert round(ha["effective_n"], 2) == 2.10
    assert round(hb["effective_n"], 2) == 3.04
    assert round(ha["shares"][1], 2) == 0.63
    assert round(xr.herfindahl([25, 8.5, 30, 15])["effective_n"], 2) == 3.38
    _, _, sp = _two_asset(-0.3)
    assert round(-sum(a) / (Z99 * sp)) == 32
    assert round((a[0] - b[0]) / 1e6, 1) == 6.8
    cov = xr.ltv_covenant(21e6, 30e6, 0.75)
    assert cov["cure"](19.5e6) == R(6.375e6) and cov["cure"](25.5e6) == R(1.875e6)


def test_cre_application_table():
    v1 = 30e6 * 0.65
    assert v1 == R(19.5e6)
    rows = {0.50: (0.769, 375_000, 4.5e6), 0.60: (0.923, 3_375_000, 1.5e6), 0.70: (1.077, 6_375_000, -1.5e6)}
    for ltv0, (post, cure, eq) in rows.items():
        loan = ltv0 * 30e6
        assert round(loan / v1, 3) == post
        assert xr.ltv_covenant(loan, 30e6, 0.75)["cure"](v1) == R(cure)
        assert v1 - loan == R(eq)
    assert 0.75 * 0.65 == R(0.4875)
    assert 12e6 + 3.375e6 == R(15.375e6)


def test_episode_arithmetic():
    assert 66 / 132 == R(0.5)
    assert round(_binom_tail(60, 0.01, 5), 5) == 0.00035
    assert round(_binom_tail(60, 0.01, 5) * 100, 3) == 0.035


# ---------------------------------------------------------------- problems

def test_problem_21_2():
    assert risk.position_size_by_stop(20e6, 0.0075, 80, 76, 1000) == R(37.5)
    assert xr.size_by_volatility(0.003 * 20e6, 80, 1000, 0.025) == R(30)
    g = xr.gap_loss(80, 76, 72, 30, 1000)
    assert g["realized"] == R(240_000) and g["planned"] == R(120_000) and g["ratio"] == R(2.0)
    assert 240_000 / 20e6 == R(0.012)


def test_problem_21_3():
    f = risk.kelly_continuous(0.05, 0, 0.20)
    assert f == R(1.25)
    g = xr.kelly_growth(f, 0.05, 0.20)
    assert g == R(0.03125)
    vals = [xr.kelly_growth(c * f, 0.05, 0.20) for c in (0.5, 1.5, 2, 3)]
    assert vals == [R(0.0234375), R(0.0234375), R(0.0, abs=1e-15), R(-0.09375)]


def test_problem_21_4():
    w = [-2150, -1630, -1410, -1220, -1180, -990, -940]
    pnl = w + [100.0] * 243
    assert len(pnl) == 250
    assert risk.historical_var(pnl, 0.99) == 1410
    assert risk.historical_es(pnl, 0.99) == R(1730)
    assert risk.historical_var(pnl, 0.975) == 940
    assert risk.historical_es(pnl, 0.975) == R(1360)
    assert sum(1 for x in pnl if x < -1000) == 5
    assert round(_binom_tail(250, 0.01, 5), 3) == 0.108


def test_problem_21_5():
    assert round(0.48 / 0.52, 4) == 0.9231
    assert round(xr.gamblers_ruin(0.52, 15), 3) == 0.301
    assert round(xr.gamblers_ruin(0.52, 15, 30), 3) == 0.231
    f = risk.kelly_continuous(0.04, 0, 0.15)
    assert round(f, 3) == 1.778
    exp = {1.0: (0.03556, 0.2667, 0.600, 0.297), 0.5: (0.02667, 0.1333, 0.216, 0.0376)}
    for c, (m_, s_, pe, pw) in exp.items():
        ff = c * f
        m, s = xr.kelly_growth(ff, 0.04, 0.15), ff * 0.15
        assert round(m, 5) == m_ and round(s, 4) == s_
        assert round(xr.prob_ever_below(0.4, m, s), 3) == pe
        assert round(xr.prob_below_within(0.4, m, s, 5), 4 if c == 0.5 else 3) == pw
    assert round(-math.log(0.6), 4) == 0.5108


def test_problem_21_6():
    assert xd.days_to_exit(600_000, 150_000, 0.25) == R(16)
    v = risk.parametric_var(21e6, 0, 0.022, 0.99)
    assert round(v) == 1_074_773
    fac = xr.liquidation_variance_factor(16)
    assert fac == R(5.84375) and round(math.sqrt(fac), 4) == 2.4174
    assert round(v * math.sqrt(fac)) == 2_598_139
    assert round(xr.liquidity_adjusted_var(v * math.sqrt(fac), 21e6, 0.008)) == 2_682_139
    assert xd.max_position(150_000, 0.25, 5) == R(187_500)
    assert 187_500 * 35 == R(6_562_500)


def test_problem_21_7():
    mc = xr.futures_margin_call(200_000, 20, 1000, 7000, 6000)
    assert mc["trigger_points"] == R(4.0) and mc["call_at_trigger"] == 20_000
    assert 20 * 7000 - (200_000 - 8 * 20 * 1000) == 100_000
    cov = xr.ltv_covenant(26e6, 40e6, 0.70)
    assert round(cov["breach_decline"], 4) == 0.0714
    assert cov["cure"](32e6) == R(3.6e6)


def test_problem_21_8():
    f = risk.kelly_continuous(0.05, 0, 0.10)
    assert f == R(5.0)
    se = 0.10 / math.sqrt(8)
    assert round(se, 4) == 0.0354 and se ** 2 == R(0.00125)
    assert xr.kelly_growth_with_estimation(1, 0.05, 0.10, se) == R(0.0625)
    assert xr.kelly_growth_with_estimation(0.5, 0.05, 0.10, se) == R(0.078125)
    k = xr.kelly_optimal_shrink(0.05, se)
    assert k == R(2 / 3)
    assert round(k * f, 2) == 3.33
    assert xr.kelly_growth_with_estimation(k, 0.05, 0.10, se) == R(1 / 12)
    assert xr.kelly_growth(5, 0.025, 0.10) == R(0.0, abs=1e-15)
    assert xr.kelly_growth(2, 0.025, 0.10) == R(0.03)
    assert xr.kelly_growth(2, 0.05, 0.10) == R(0.08)
    assert 5 * 0.10 == R(0.5) and 5 * 0.02 == R(0.10)


def test_problem_21_9():
    def legs(dy, de, dv, dm):
        return [15e6 * (-8.5 * dy + 0.5 * 85 * dy * dy), -20 * 5000 * 50 * de,
                max(20e6 * (1 + dv) - 14e6, 0) - 6e6, 5e6 * dm]
    a = legs(-0.01, -0.30, -0.30, -0.40)
    b = legs(0.015, -0.15, -0.10, -0.10)
    assert [round(x) for x in a] == [1_338_750, 1_500_000, -6_000_000, -2_000_000]
    assert [round(x) for x in b] == [-1_769_062, 750_000, -2_000_000, -500_000] or \
        [round(x) for x in b] == [-1_769_063, 750_000, -2_000_000, -500_000]
    assert round(sum(a)) == -5_161_250 and round(sum(a) / 40e6, 3) == -0.129
    assert round(sum(b) / 1e3, 1) == R(-3519.1, abs=0.06) and round(sum(b) / 40e6, 3) == -0.088
    assert round((a[0] + a[1]) / 1e6, 1) == 2.8
    assert round((a[0] + a[1]) / -(a[2] + a[3]), 2) == 0.35


def test_problem_21_10():
    assert round(1 - 62 / 118, 3) == 0.475
    assert 60 * 0.01 == R(0.6)
    assert round(_binom_tail(60, 0.01, 5) * 100, 3) == 0.035
