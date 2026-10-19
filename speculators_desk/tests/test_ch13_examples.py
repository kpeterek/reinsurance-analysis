"""Reproduces every number in Chapter 13 text, problems, and solutions,
and tests the new real-option helper sdesk.x_options_real."""

import math

import pytest

from sdesk import cre, fixed_income as fi, markets as mk, risk, stats, tvm
from sdesk import x_options_real as ro

R = pytest.approx


def _bisect(f, lo, hi, n=200):
    """Root of a decreasing-or-increasing f on [lo, hi] with a sign change."""
    flo = f(lo)
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        if (f(mid) > 0) == (flo > 0):
            lo, flo = mid, f(mid)
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------- Example 13.1
MF = dict(noi1=2_200_000, g=0.03, bid=44_000_000, sell=0.015, loan=24_000_000, rate=0.0425, tsy=0.0375)


def _ym():
    return MF["loan"] * (MF["rate"] - MF["tsy"]) * tvm.annuity_factor(MF["tsy"], 5)


def _em():
    return MF["bid"] * (1 - MF["sell"]) - MF["loan"] - _ym()


def _hold_flows(exit_cap):
    nois = [MF["noi1"] * (1 + MF["g"]) ** t for t in range(6)]
    cf = [-_em()] + [nois[t] - MF["loan"] * MF["rate"] for t in range(5)]
    cf[-1] += nois[5] / exit_cap * (1 - MF["sell"]) - MF["loan"]
    return cf


def _alt_flows():
    em = _em()
    p = em / (1 + 0.015 - 0.55)
    d = 0.55 * p
    n = [p * 0.0625 * 1.025 ** t for t in range(6)]
    cf = [-em] + [n[t] - d * 0.06 for t in range(5)]
    cf[-1] += n[5] / 0.065 * 0.985 - d
    return p, d, cf


def test_example_13_1():
    assert round(tvm.annuity_factor(0.0375, 5), 4) == 4.4833
    assert round(_ym()) == 537_991
    assert round(_em()) == 18_802_009
    assert MF["noi1"] / MF["bid"] == R(0.05)
    nois = [round(MF["noi1"] * 1.03 ** t) for t in range(6)]
    assert nois == [2_200_000, 2_266_000, 2_333_980, 2_403_999, 2_476_119, 2_550_403]
    cf = _hold_flows(0.0525)
    assert [round(x) for x in cf] == [-18_802_009, 1_180_000, 1_246_000, 1_313_980, 1_383_999, 25_306_537]
    gross = MF["noi1"] * 1.03 ** 5 / 0.0525
    assert round(gross) == 48_579_104
    assert round(gross * 0.985 - 24_000_000) == 23_850_418
    irr_hold = tvm.irr(cf)
    assert round(irr_hold, 4) == 0.1121
    p, d, acf = _alt_flows()
    assert (round(p), round(d)) == (40_434_427, 22_238_935)
    assert round(p * 0.0625) == 2_527_152 and round(d * 0.06) == 1_334_336
    assert [round(x) for x in acf] == [-18_802_009, 1_192_816, 1_255_994, 1_320_753, 1_387_130, 22_544_717]
    irr_alt = tvm.irr(acf)
    assert round(irr_alt, 4) == 0.0901
    be = _bisect(lambda c: tvm.irr(_hold_flows(c)) - irr_alt, 0.04, 0.08)
    assert round(be, 4) == 0.0557
    # unlevered
    nn = [MF["noi1"] * 1.03 ** t for t in range(6)]
    u = [-44e6 * 0.985] + nn[:5]
    u[-1] += nn[5] / 0.0525 * 0.985
    assert round(tvm.irr(u), 4) == 0.0717
    n2 = [p * 0.0625 * 1.025 ** t for t in range(6)]
    u2 = [-p * 1.015] + n2[:5]
    u2[-1] += n2[5] / 0.065 * 0.985
    assert round(tvm.irr(u2), 4) == 0.0741
    assert round(d / p, 3) == 0.55 and round(24 / 44, 3) == 0.545


# ---------------------------------------------------------------- Example 13.2
def test_example_13_2():
    ml = cre.max_loan(2_200_000, 44e6, 0.06, None, ltv_max=0.65, dscr_min=1.25,
                      debt_yield_min=0.08, interest_only=True)
    assert ml["ltv"] == R(28_600_000)
    assert ml["dscr"] == R(29_333_333, abs=1)
    assert ml["debt_yield"] == R(27_500_000)
    assert ml["binding"] == "debt_yield"
    new = ml["max_loan"]
    cash = new - 24e6 - _ym() - 0.01 * new
    assert round(cash) == 2_687_009
    inc = new * 0.06 - 24e6 * 0.0425
    assert inc == R(630_000)
    lender = [-cash] + [inc] * 5
    lender[-1] += new - 24e6
    assert round(tvm.irr(lender), 4) == 0.2699
    assert 630_000 / 3_500_000 == R(0.18)


# ---------------------------------------------------------------- Example 13.3
V3 = [44.0, 28.8, 30.0]
W3 = [v / sum(V3) for v in V3]
S3 = [0.12, 0.09, 0.20]
C_TX = [[1, 0.6, 0.5], [0.6, 1, 0.55], [0.5, 0.55, 1]]
C_DIV = [[1, 0.25, 0.5], [0.25, 1, 0.30], [0.5, 0.30, 1]]


def _shares(w, s, c):
    sp = risk.portfolio_volatility(w, s, c)
    rc = [w[i] * sum(c[i][j] * s[i] * s[j] * w[j] for j in range(3)) / sp for i in range(3)]
    assert sum(rc) == R(sp)  # Euler decomposition
    return sp, [x / sp for x in rc]


def test_example_13_3():
    assert [round(w, 4) for w in W3] == [0.4280, 0.2802, 0.2918]
    sp, sh = _shares(W3, S3, C_TX)
    assert round(sp, 4) == 0.1134
    assert [round(x, 3) for x in sh] == [0.382, 0.173, 0.445]
    sp2, sh2 = _shares(W3, S3, C_DIV)
    assert round(sp2, 4) == 0.1059
    assert [round(x, 3) for x in sh2] == [0.398, 0.125, 0.477]
    st = risk.portfolio_volatility(W3, S3, [[1, .9, .9], [.9, 1, .9], [.9, .9, 1]])
    assert round(st, 4) == 0.1306
    one = risk.portfolio_volatility(W3, S3, [[1] * 3] * 3)
    wavg = sum(a * b for a, b in zip(W3, S3))
    assert one == R(wavg) and round(wavg, 4) == 0.1349
    assert round(wavg / sp, 2) == 1.19 and round(wavg / sp2, 2) == 1.27
    var = mk.norm_ppf(0.99) * sp * 102.8
    assert round(mk.norm_ppf(0.99), 4) == 2.3263
    assert round(var, 1) == 27.1
    assert round(var / 41.8, 2) == 0.65
    assert round(sp - sp2, 4) == 0.0075 and round(one - st, 4) == 0.0043


# ---------------------------------------------------------------- Example 13.4
SPREADS = [250, 240, 235, 245, 260, 290, 390, 320, 265, 255]


def test_example_13_4():
    m, sd = stats.mean(SPREADS), stats.stdev(SPREADS)
    assert m == R(275) and round(sd, 1) == 47.8
    assert round((325 - m) / sd, 2) == 1.05
    ex = [x for x in SPREADS if x != 390]
    m2, sd2 = stats.mean(ex), stats.stdev(ex)
    assert round(m2, 1) == 262.2 and round(sd2, 1) == 27.1
    assert round((325 - m2) / sd2, 2) == 2.32
    # c_H - c_MF = dk - dg  => g_MF - g_H = 3.25% - 2.50%
    assert round(0.0325 - 0.0250, 4) == 0.0075
    assert round(cre.cap_rate_shock_pct(0.085, 0.08), 4) == 0.0625
    assert round(cre.cap_rate_shock_pct(0.0525, 0.0575), 4) == -0.0870


# ---------------------------------------------------------------- Example 13.5
def test_example_13_5():
    dv = fi.dv01(0.06, 0.06, 10, face=60_000_000, freq=12)
    assert round(dv) == 45_037
    approx = 60e6 * 0.0001 * tvm.annuity_factor(0.06, 10)
    assert round(tvm.annuity_factor(0.06, 10), 4) == 7.3601
    assert round(approx) == 44_161
    assert abs(dv / approx - 1) < 0.02
    n = fi.hedge_ratio_dv01(dv, 85.0)
    assert round(n, 1) == 529.8
    N = round(n)
    assert N == 530
    out = []
    for dy, ds, closes in [(50, 0, True), (-40, 60, True), (-40, 0, False)]:
        loan = -dv * (dy + ds) if closes else 0.0
        hedge = mk.futures_pnl(0, dy, N, 85.0, side=1)  # short futures gains when yields rise
        out.append((round(loan), round(hedge), round(loan + hedge)))
    assert out == [(-2_251_837, 2_252_500, 663), (-900_735, -1_802_000, -2_702_735), (0, -1_802_000, -1_802_000)]
    assert round(2_702_735 / 900_735, 1) == 3.0


# ---------------------------------------------------------------- Example 13.6
def _reserve():
    mf = [2.2 * 0.92] * 2
    ind = [1.8 * 0.95, 1.8 * 0.85]
    ho = [2.4 * 0.45, 2.4 * 0.70]
    ds = [1.02, 0.90, 1.65]
    pip = [1.2, 0.0]
    x = [mf[t] - ds[0] + ind[t] - ds[1] + ho[t] - ds[2] - pip[t] for t in range(2)]
    hv = ho[1] / 0.095
    gap = 22.0 - 0.55 * hv
    cum, run = [], 0.0
    for t, m in zip(range(2), [0.0, gap]):
        run += x[t] - m
        cum.append(run)
    return mf, ind, ho, x, hv, gap, cum, max(0.0, -min(cum))


def test_example_13_6():
    mf, ind, ho, x, hv, gap, cum, r = _reserve()
    assert [round(v, 3) for v in mf + ind + ho] == [2.024, 2.024, 1.710, 1.530, 1.080, 1.680]
    assert [round(v, 3) for v in x] == [0.044, 1.664]
    assert round(hv, 2) == 17.68 and round(0.55 * hv, 2) == 9.73
    assert round(gap, 3) == 12.274
    assert round(cum[1], 2) == -10.57
    assert round(r, 2) == 10.57
    alone = (1.65 - 1.08) + 1.2 - (1.68 - 1.65) + gap
    assert round(alone, 2) == 14.01
    assert round(gap / alone, 3) > 0.85
    assert round(0.57 + 1.2 - 0.03, 2) == 1.74
    drag = r * (0.11 - 0.04)
    assert round(drag, 2) == 0.74
    assert round(drag / 41.8, 4) == 0.0177


# ---------------------------------------------------------------- Example 13.7
def _p_fail(ltv, sig, T=3, max_ltv=0.75):
    return mk.norm_cdf((math.log(ltv / max_ltv) + 0.5 * sig ** 2 * T) / (sig * math.sqrt(T)))


def test_example_13_7():
    sp = risk.portfolio_volatility([0.5, 0.5], [0.10, 0.20], [[1, 0.5], [0.5, 1]])
    assert round(sp, 4) == 0.1323
    assert round(sp * 100 / 50, 4) == 0.2646
    table = {"A": (0.5, 0.5, 0.0121, 0.1593, 0.171), "B": (0.7, 0.3, 0.3776, 0.0067, 0.384),
             "C": (0.3, 0.7, 0.0000, 0.4896, 0.490)}
    for lm, lh, pm, ph, e in table.values():
        a, b = _p_fail(lm, 0.10), _p_fail(lh, 0.20)
        assert (round(a, 4), round(b, 4), round(a + b, 3)) == (pm, ph, e)
    z = lambda l, s: (math.log(l / 0.75) + 0.5 * s * s * 3) / (s * math.sqrt(3))  # noqa: E731
    lm = _bisect(lambda m: z(m, 0.10) - z(1 - m, 0.20), 0.3, 0.99)
    assert round(lm, 3) == 0.574 and round(1 - lm, 3) == 0.426
    assert round(_p_fail(lm, 0.10), 4) == 0.0723 == round(_p_fail(1 - lm, 0.20), 4)
    assert round(2 * _p_fail(lm, 0.10), 3) == 0.145
    assert round(0.7 / 0.75, 3) == 0.933


# ---------------------------------------------------------------- Example 13.8
def _dev(sig):
    u, d = ro.crr_factors(sig)
    return ro.american_real_option(30e6, u, d, 0.04, 2, lambda V, t: V - 27e6 * 1.03 ** t, delta=0.055)


def test_example_13_8():
    u, d = ro.crr_factors(0.20)
    assert (round(u, 4), round(d, 4)) == (1.2214, 0.8187)
    res = _dev(0.20)
    assert round(res["q"], 4) == 0.4129
    lat = res["lattice"]
    assert [round(v / 1e6, 2) for v in lat[2]] == [20.11, 30.00, 44.75]
    assert [round(v / 1e6, 2) for v in lat[1]] == [24.56, 36.64]
    assert [round(27 * 1.03 ** t, 2) for t in (1, 2)] == [27.81, 28.64]
    opt = res["option"]
    assert [round(v / 1e6, 2) for v in opt[2]] == [0.0, 1.36, 16.11]
    assert [round(v / 1e6, 2) for v in opt[1]] == [0.54, 8.83]
    assert res["exercise"][1] == [False, True] and res["exercise"][2] == [False, True, True]
    assert round(res["option_value"]) == 3_810_482
    assert res["immediate"] == R(3_000_000)
    assert round(res["value_of_waiting"]) == 810_482
    assert not res["exercise_now"]
    # hand recursion
    q = res["q"]
    down = q * (30e6 - 27e6 * 1.03 ** 2) / 1.04
    assert round(down) == round(opt[1][0])
    assert round((q * (lat[1][1] - 27e6 * 1.03) + (1 - q) * down) / 1.04) == 3_810_482
    sens = {0.10: (3.00, 0.00, True), 0.15: (3.10, 0.10, False), 0.20: (3.81, 0.81, False), 0.25: (4.51, 1.51, False)}
    for s, (ov, vw, now) in sens.items():
        r = _dev(s)
        assert (round(r["option_value"] / 1e6, 2), round(r["value_of_waiting"] / 1e6, 2), r["exercise_now"]) == (ov, vw, now)
    hurdles = {0.10: 1.22, 0.20: 1.65, 0.25: 1.92}
    for s, h in hurdles.items():
        assert round(ro.perpetual_option_threshold(0.04, 0.055, s)["hurdle_multiple"], 2) == h
    assert round(30 / 27, 2) == 1.11
    assert round(0.810482 / 3.0, 2) == 0.27
    assert round(_dev(0.20)["value_of_waiting"] / _dev(0.15)["value_of_waiting"], 1) == 8.1


# ---------------------------------------------------------------- Example 13.9
def test_example_13_9():
    v0 = (0.65 * 33e6 + 0.35 * 24e6 + 1.6e6) / 1.08
    assert round(v0) == 29_120_370
    assert round(v0 - 27e6) == 2_120_370
    k1 = 27e6 * 1.03
    assert round(k1) == 27_810_000 and round(33e6 - k1) == 5_190_000
    rw = ro.decision_tree_ev([33e6 - k1, 0.0], [0.65, 0.35], 0.08)
    assert round(rw) == 3_123_611
    q = (1.04 * v0 - 1.6e6 - 24e6) / (33e6 - 24e6)
    assert round(q, 4) == 0.5206
    rn = q * (33e6 - k1) / 1.04
    assert round(rn) == 2_597_875
    assert round((rw - (v0 - 27e6)) / 1e6, 2) == 1.00
    assert round((rn - (v0 - 27e6)) / 1e6, 2) == 0.48
    # risk-neutral q from the library agrees when cast as u, d with delta = NOI / V0
    q2 = ro.risk_neutral_prob(33e6 / v0, 24e6 / v0, 0.04, 1.6e6 / v0)
    assert q2 == R(q)
    need = (v0 - 27e6) * 1.04 / q
    assert round(need / 1e6, 3) == 4.236
    assert round((33e6 - need) / 27e6 - 1, 4) == 0.0653


# ---------------------------------------------------------------- Example 13.10
def test_example_13_10():
    cost = 0.6 + 0.2 + 0.6 + 0.2
    f = cost / 20.0
    assert f == R(0.08)
    exp = {3: (0.1207, 307), 5: (0.1083, 183), 10: (0.0991, 91)}
    for T, (r, bp) in exp.items():
        ra = 1.09 / (1 - f) ** (1 / T) - 1
        assert round(ra, 4) == r
        assert round((ra - 0.09) * 1e4) == bp
    assert [round(f / T * 1e4) for T in (3, 5, 10)] == [267, 160, 80]


# ---------------------------------------------------------------- §13.6 and §13.9
def test_section_text_numbers():
    assert round(7.0 / 5.5 - 1, 2) == 0.27
    assert round(5.365e9 / 23_262) == 230_634
    assert 33 + 18 + 10 + 8 + 3 == 72
    assert 8.00 + 3.00 == 11.00
    assert round(30.0 / 102.8, 2) == 0.29
    assert round(250_000 / 22_000_000 / 2, 4) == 0.0057  # cap premium, annualized (section 13.4.6)


# ---------------------------------------------------------------- Problems
def test_problem_13_2():
    assert round(0.08 - 0.0525, 4) == 0.0275
    assert round(0.50 / 5.25, 3) == 0.095
    assert round(cre.cap_rate_shock_pct(0.0525, 0.0475), 4) == 0.1053
    assert round(0.08 - 0.0475, 4) == 0.0325


def test_problem_13_3():
    n = fi.hedge_ratio_dv01(36_000, 80)
    assert n == 450
    assert mk.futures_pnl(0, 20, 450, 80) == 720_000
    assert -36_000 * 20 == -720_000
    assert -36_000 * 35 + 720_000 == -540_000


def _p4_flows(xc):
    em = 18e6 * 0.98 - 9e6
    n = [1e6 * 1.025 ** t for t in range(5)]
    cf = [-em] + [n[t] - 9e6 * 0.05 for t in range(4)]
    cf[-1] += n[4] / xc * 0.98 - 9e6
    return cf


def test_problem_13_4():
    cf = _p4_flows(0.06)
    assert [round(x) for x in cf] == [-8_640_000, 550_000, 575_000, 600_625, 9_655_835]
    assert [round(1e6 * 1.025 ** t) for t in range(5)] == [1_000_000, 1_025_000, 1_050_625, 1_076_891, 1_103_813]
    assert round(1e6 * 1.025 ** 4 / 0.06) == 18_396_882
    assert round(1e6 * 1.025 ** 4 / 0.06 * 0.98 - 9e6) == 9_028_944
    assert round(tvm.irr(cf), 4) == 0.0778
    be = _bisect(lambda c: tvm.irr(_p4_flows(c)) - 0.085, 0.04, 0.10)
    assert round(be, 4) == 0.0591
    assert round(1e6 / 18e6, 4) == 0.0556
    assert round((be - 1e6 / 18e6) * 1e4) == 35
    assert round((0.06 - be) * 1e4) == 9


def test_problem_13_5():
    exp = {0.3: 0.1067, 0.8: 0.1253, 1.0: 0.1320}
    eq = {0.3: 0.2666, 0.8: 0.3132, 1.0: 0.3300}
    for rho, v in exp.items():
        s = risk.portfolio_volatility([0.6, 0.4], [0.10, 0.18], [[1, rho], [rho, 1]])
        assert round(s, 4) == v
        assert round(s / 0.4, 4) == eq[rho]


def test_problem_13_6():
    q = ro.risk_neutral_prob(1.25, 0.80, 0.05, 0.06)
    assert round(q, 4) == 0.4222
    res = ro.american_real_option(20e6, 1.25, 0.80, 0.05, 1, lambda V, t: V - 18.5e6, delta=0.06)
    assert round(res["option_value"] / 1e6, 3) == 2.614
    assert round(res["value_of_waiting"] / 1e6, 3) == 1.114
    qs = 1.5 * 1.05 / 6.5
    assert round(qs, 4) == 0.2423
    d_star = 1 + 0.05 - 0.80 - qs * 0.45
    assert round(d_star, 4) == 0.1410
    # at delta*, the value of waiting is zero
    r2 = ro.american_real_option(20e6, 1.25, 0.80, 0.05, 1, lambda V, t: V - 18.5e6, delta=d_star)
    assert r2["option_value"] == R(1.5e6, rel=1e-9)


def test_problem_13_7():
    y1 = (3.0 * 0.8 - 2.4) + (1.5 * 0.95 - 1.0)
    y2 = (3.0 * 0.65 - 2.4 - 1.5) + (1.5 * 0.95 - 1.0)
    assert (round(y1, 3), round(y2, 3)) == (0.425, -1.525)
    v = 3.0 * 0.65 / 0.09
    assert round(v, 2) == 21.67 and round(0.5 * v, 2) == 10.83
    gap = 25 - 0.5 * v
    assert round(gap, 2) == 14.17
    r = -(y1 + y2 - gap)
    assert round(r, 2) == 15.27
    assert round(r * (0.10 - 0.045), 2) == 0.84


def test_problem_13_8():
    cash = 18.0 - 15.0 - 0.40 - 0.18
    assert round(cash, 2) == 2.42
    inc = 18.0 * 0.0625 - 15.0 * 0.039
    assert round(inc, 3) == 0.540
    fl = [-cash] + [inc] * 4
    fl[-1] += 3.0
    assert round(tvm.irr(fl), 4) == 0.2639


def test_problem_13_9():
    d = [180, 170, 200, 320, 310, 300]
    m, s = stats.mean(d), stats.stdev(d)
    assert round(m, 1) == 246.7 and round(s, 1) == 70.3
    assert round((330 - m) / s, 2) == 1.18
    m2, s2 = stats.mean(d[3:]), stats.stdev(d[3:])
    assert (m2, round(s2, 1)) == (R(310), 10.0)
    assert round((330 - m2) / s2, 2) == 2.00


def test_problem_13_10():
    dv = fi.dv01(0.0625, 0.0625, 7, face=40_000_000, freq=12)
    assert round(dv) == 22_632
    full = dv / 80
    assert round(full, 1) == 282.9 and round(full) == 283
    assert round(0.7 * full, 1) == 198.0
    rows = []
    for n in (283, 198):
        for dy in (40, -40):
            close = -dv * dy + n * 80 * dy
            fail = n * 80 * dy
            rows.append((n, dy, round(close), fail, round(0.7 * close + 0.3 * fail)))
    assert rows == [(283, 40, 338, 905_600, 271_916), (283, -40, -338, -905_600, -271_916),
                    (198, 40, -271_662, 633_600, -84), (198, -40, 271_662, -633_600, 84)]
    assert round(dv * 40) == 905_262


# ---------------------------------------------------------------- library: x_options_real
def test_ro_rejects_arbitrage_tree():
    with pytest.raises(ValueError):
        ro.risk_neutral_prob(1.1, 0.9, 0.30, 0.0)  # r above u - 1: q > 1
    with pytest.raises(ValueError):
        ro.risk_neutral_prob(0.9, 1.1, 0.05)
    with pytest.raises(ValueError):
        ro.perpetual_option_threshold(0.04, 0.0, 0.2)
    with pytest.raises(ValueError):
        ro.decision_tree_ev([1, 2], [0.5, 0.6], 0.1)


def test_ro_american_equals_european_without_yield():
    # With no cash yield and a constant strike, early exercise of a call is never optimal.
    u, d = ro.crr_factors(0.25)
    am = ro.american_real_option(100, u, d, 0.05, 5, lambda V, t: V - 100, delta=0.0)
    eu = ro.european_real_option(100, u, d, 0.05, 5, lambda V: V - 100, delta=0.0)
    assert am["option_value"] == R(eu)
    assert not any(any(row) for row in am["exercise"][:-1])


def test_ro_deep_in_money_with_high_yield_exercises_now():
    u, d = ro.crr_factors(0.10)
    res = ro.american_real_option(100, u, d, 0.03, 3, lambda V, t: V - 50, delta=0.09)
    assert res["exercise_now"] and res["value_of_waiting"] == R(0.0)


def test_ro_perpetual_limits():
    # As sigma -> 0 with delta > r, the hurdle multiple tends to 1 (the NPV rule).
    assert ro.perpetual_option_threshold(0.04, 0.06, 0.001)["hurdle_multiple"] == R(1.0, abs=1e-3)
    # beta solves the fundamental quadratic
    b = ro.perpetual_option_threshold(0.05, 0.04, 0.3)["beta"]
    assert 0.5 * 0.09 * b * (b - 1) + (0.05 - 0.04) * b - 0.05 == R(0.0, abs=1e-12)


def test_ro_zero_volatility_limit_one_step():
    # u = d is rejected; a nearly riskless tree prices the option at intrinsic forward value.
    u, d = 1.0001, 0.9999
    q = ro.risk_neutral_prob(u, d, 0.0, 0.0)
    assert q == R(0.5)
