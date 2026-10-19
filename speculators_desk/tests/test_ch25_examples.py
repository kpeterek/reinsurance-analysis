"""Reproduces every number in Chapter 25 text, problems, solutions, and the two worked desk documents."""

import math

import pytest

from sdesk import cre, markets as mk, stats, tvm
from sdesk import fixed_income as fi

R = pytest.approx

# ------------------------------------------------------------------ shared book (section 25.1)
TY_DV01 = 85
TY_N = 40
CAPITAL = 40_000_000


def _poisson_cdf(k, lam):
    return sum(math.exp(-lam) * lam ** j / math.factorial(j) for j in range(k + 1))


def test_example_25_1():
    v_err = 60_000 / 0.065
    assert v_err == R(923_076.92, abs=0.01)
    assert 0.10 * v_err == R(92_307.69, abs=0.01)
    audit_hr = 0.10 * v_err / 4
    assert round(audit_hr) == 23_077
    notes_hr = 0.02 * (0.005 * 5_000_000)
    assert notes_hr == R(500)
    assert round(audit_hr / notes_hr) == 46
    assert round(audit_hr / 10) == 2_308  # robustness: audit probability overstated tenfold
    assert (audit_hr * 4 / 0.10) * 0.065 == R(60_000)  # reverse check: hours value -> value error -> NOI error


def test_example_25_2():
    rates = TY_N * TY_DV01 * 12
    assert rates == 40_800
    es = mk.futures_pnl(5800, 5713, 10, 50, side=1)
    assert es == R(-43_500)
    assert 5800 * (1 - 0.015) == R(5713)
    reit = 2_000_000 * -0.032
    sys_ = 2_000_000 * 1.1 * -0.015
    idio = reit - sys_
    assert (reit, sys_, idio) == (R(-64_000), R(-33_000), R(-31_000))
    total = rates + es + reit + 9_600 - 2_150
    assert total == R(-59_250)
    factors = rates + (es + sys_) + idio + 9_600 - 2_150
    assert es + sys_ == R(-76_500)
    assert factors == R(total)
    assert -idio / 2_000_000 == R(0.0155)
    assert 0.02 * 2_000_000 == R(40_000)


def test_example_25_3():
    prior = 0.40
    assert prior / (1 - prior) == R(0.6667, abs=1e-4)
    lr_ind = 0.7 * 2.0 * 0.9 * 1.5
    assert lr_ind == R(1.89)
    p_ind = stats.likelihood_ratio_update(prior, lr_ind)
    assert round(p_ind, 4) == 0.5575
    assert prior / (1 - prior) * lr_ind == R(1.26)
    lr_cor = 0.7 * 2.0 * 0.9
    p_cor = stats.likelihood_ratio_update(prior, lr_cor)
    assert round(p_cor, 4) == 0.4565
    assert prior / (1 - prior) * lr_cor == R(0.84)
    assert p_cor < 0.5 < p_ind
    # independent route: Bayes with explicit likelihoods equals the odds form
    assert stats.bayes_posterior(prior, 1.89, 1.0) == R(p_ind)


def test_trade_ticket_section_25_7_5():
    dv = TY_N * TY_DV01
    assert dv == 3_400
    assert dv * 15 == 51_000
    assert 51_000 / CAPITAL == R(0.001275)
    assert dv * 30 == 102_000
    assert 102_000 / CAPITAL == R(0.00255)
    assert 0.0025 * CAPITAL == R(100_000)
    assert 39 * 85 * 30 == 99_450
    assert math.floor(100_000 / (85 * 30)) == 39


def _book_dv01():
    d5 = fi.dv01(0.04, 0.04, 5)
    return d5, TY_N * TY_DV01 - d5 * 100_000 + d5 * 150_000


def test_example_25_4():
    d5, net = _book_dv01()
    assert round(d5, 6) == 0.044913
    assert round(d5 * 100_000) == 4_491
    assert round(d5 * 150_000) == 6_737
    assert round(net) == 5_646
    eqd = 10 * 50 * 5713 + 1.1 * 2_000_000
    assert eqd == R(5_056_500)
    assert 0.01 * eqd == R(50_565)
    h = cre.value_change_from_cap_and_noi(2_550_000, 0.085, -0.10, 0.0925)
    assert h["noi1"] == R(2_295_000)
    assert round(h["v1"]) == 24_810_811
    hotel_ear = 30_000_000 - h["v1"]
    assert round(hotel_ear) == 5_189_189
    assert round(h["v1"] - 18_000_000, -4) == 6_810_000
    assert round((h["v1"] - 18e6) / 12e6 - 1, 3) == -0.432
    assert round(h["pct_change"], 4) == -0.1730
    assert 0.9 * 8.5 / 9.25 == R(0.82703, abs=1e-5)
    assert 30 / 12 * h["pct_change"] == R((h["v1"] - 18e6) / 12e6 - 1)
    i = cre.value_change_from_cap_and_noi(1_500_000, 0.0625, 0.0, 0.0675)
    ind_ear = 24_000_000 - i["v1"]
    assert round(i["v1"]) == 22_222_222
    assert round(ind_ear) == 1_777_778
    assert round((i["v1"] - 14.4e6) / 9.6e6 - 1, 3) == -0.185
    assert round(i["v1"] - 14.4e6, -4) == 7_820_000
    cre_ear = hotel_ear + ind_ear
    assert round(cre_ear) == 6_966_967
    assert round(cre_ear / CAPITAL, 3) == 0.174
    rates = 50 * net
    eq = -0.10 * eqd
    total = rates + eq - cre_ear
    assert round(rates) == 282_282
    assert eq == R(-505_650)
    assert round(total) == -7_190_335
    assert round(total / CAPITAL, 4) == -0.1798
    assert round(hotel_ear / -total, 2) == 0.72
    assert round(rates + eq) == -223_368
    assert round((rates + eq) / total, 2) == 0.03


def test_example_25_5():
    counts = {"units": 14, "data": 12, "timing": 11, "arithmetic": 9, "judgment": 8, "concept": 6}
    assert sum(counts.values()) == 60 == 26 + 19 + 15
    assert 60 / 400 == R(0.15)
    top3 = 14 + 12 + 11
    assert top3 == 37
    assert round(top3 / 60, 3) == 0.617
    assert (26 + 19 + 15) / 3 == 20
    p = _poisson_cdf(15, 20)
    assert round(p, 4) == 0.1565
    z = (15.5 - 20) / math.sqrt(20)
    assert round(z, 3) == -1.006
    assert round(mk.norm_cdf(z), 3) == 0.157
    assert 60 - 8 == 52
    assert round(1 - 15 / 26, 2) == 0.42


F6 = [0.9] * 5 + [0.7] * 6 + [0.5] * 4 + [0.3] * 5
O6 = [1, 1, 1, 0, 0] + [1, 1, 1, 1, 0, 0] + [1, 1, 0, 0] + [1, 0, 0, 0, 0]


def _murphy(forecasts, outcomes):
    bins = {}
    for f, o in zip(forecasts, outcomes):
        bins.setdefault(f, []).append(o)
    n = len(forecasts)
    obar = sum(outcomes) / n
    rel = sum(len(v) * (f - sum(v) / len(v)) ** 2 for f, v in bins.items()) / n
    res = sum(len(v) * (sum(v) / len(v) - obar) ** 2 for v in bins.values()) / n
    return rel, res, obar * (1 - obar)


def test_example_25_6():
    assert len(F6) == 20 and sum(O6) == 10
    bin_sums = [3 * 0.01 + 2 * 0.81, 4 * 0.09 + 2 * 0.49, 4 * 0.25, 0.49 + 4 * 0.09]
    assert bin_sums == [R(1.65), R(1.34), R(1.00), R(0.85)]
    assert sum(bin_sums) == R(4.84)
    bs = stats.brier_score(F6, O6)
    assert bs == R(0.242)
    assert 1 - bs / 0.25 == R(0.032)
    rel, res, unc = _murphy(F6, O6)
    assert rel == R(0.025333, abs=1e-6)
    assert res == R(0.033333, abs=1e-6)
    assert unc == R(0.25)
    assert rel - res + unc == R(bs)
    assert 5 * 0.3 ** 2 == R(0.45)
    assert rel * 20 == R(0.50667, abs=1e-5)
    p_le3 = 1 - math.comb(5, 4) * 0.9 ** 4 * 0.1 - 0.9 ** 5
    assert (math.comb(5, 4) * 0.9 ** 4 * 0.1, 0.9 ** 5) == (R(0.32805), R(0.59049))
    assert round(p_le3, 4) == 0.0815


def test_example_25_7():
    dmod = fi.modified_duration(0.09, 0.09, 30)
    cvx = fi.convexity(0.09, 0.09, 30)
    assert round(dmod, 3) == 10.319
    assert round(cvx, 2) == 183.83
    approx = fi.price_change_approx(100, dmod, cvx, 0.005)
    assert round(approx["duration_term"], 3) == -5.160
    assert round(approx["convexity_term"], 3) == 0.230
    assert round(approx["total"], 3) == -4.930
    exact = fi.bond_price(0.095, 0.09, 30)
    assert round(exact, 3) == 95.062
    assert round(exact - 100, 3) == -4.938
    assert abs((exact - 100) - approx["total"]) < 0.01
    assert round(-5.160 - (exact - 100), 2) == -0.22
    assert round(0.222 / 4.938, 3) == 0.045
    assert round(0.995 ** 100, 4) == 0.6058
    assert round(1 - 0.995 ** 100, 3) == 0.394
    assert round(1 - (1 - 0.005 * 0.1) ** 100, 3) == 0.049
    assert round(1 - math.exp(-0.5), 3) == 0.393


# ------------------------------------------------------------------ section 25.11 and the IC memo

NOIS = [1_500_000 * 1.03 ** t for t in range(5)]
SCEN = [(0.3, 0.0625), (0.5, 0.0675), (0.2, 0.075)]


def _irrs(price):
    basis = price * 1.02
    fwd = 1_500_000 * 1.03 ** 5
    out = []
    for p, c in SCEN:
        sale = fwd / c * 0.98
        out.append((p, sale, tvm.irr([-basis] + NOIS[:4] + [NOIS[4] + sale])))
    e_irr = sum(p * r for p, _, r in out)
    e_sale = sum(p * s for p, s, _ in out)
    irr_ecf = tvm.irr([-basis] + NOIS[:4] + [NOIS[4] + e_sale])
    return basis, out, e_irr, irr_ecf


def test_section_25_11_and_ic_memo():
    fwd = 1_500_000 * 1.03 ** 5
    assert round(fwd) == 1_738_911
    b24, s24, e24, ecf24 = _irrs(24_000_000)
    b23, s23, e23, ecf23 = _irrs(23_000_000)
    assert (b24, b23) == (R(24_480_000), R(23_460_000))
    assert [round(s) for _, s, _ in s24] == [27_266_126, 25_246_413, 22_721_772]
    assert [round(r, 4) for _, _, r in s24] == [0.0840, 0.0702, 0.0519]
    assert [round(r, 4) for _, _, r in s23] == [0.0944, 0.0805, 0.0621]
    assert (round(e24, 4), round(e23, 4)) == (0.0707, 0.0810)
    assert (round(ecf24, 4), round(ecf23, 4)) == (0.0709, 0.0813)
    lo, hi = 20e6, 26e6
    for _ in range(200):
        m = 0.5 * (lo + hi)
        lo, hi = (m, hi) if _irrs(m)[2] > 0.08 else (lo, m)
    assert round(lo) == 23_095_880
    assert round(1_500_000 / lo, 4) == 0.0649
    assert round(1_500_000 / 23_000_000, 4) == 0.0652
    assert 1_500_000 / 24_000_000 == R(0.0625)
    assert (24_000_000 / 240_000, round(23_000_000 / 240_000, 2)) == (100.0, 95.83)
    loan = 0.6 * 24_000_000
    ds = tvm.annual_debt_service(loan, 0.065, 30)
    assert round(ds) == 1_092_214
    assert round(cre.dscr(1_500_000, ds), 2) == 1.37
    assert round(cre.debt_yield(1_500_000, loan), 4) == 0.1042
    assert round(cre.cash_on_cash(1_500_000 - ds, 24_000_000 - loan), 4) == 0.0425
    assert round(e23 - 0.08, 4) == 0.0010
    # bad-scenario principal check at the bid
    assert s23[2][1] + sum(NOIS) > b23


def test_example_blotter():
    assert round((4.18 - 4.12) * 100) == 6
    assert round((4.35 - 4.31) * 100) == 4
    assert round((4.35 - 4.18) * 100) == 17 and round((4.31 - 4.12) * 100) == 19
    assert round((1.95 - 1.92) * 100) == 3
    assert round((4.16 - 4.10) * 100) == 6
    assert round(5771 / 5800 - 1, 4) == -0.0050
    assert round(1.0817 / 1.0850 - 1, 4) == -0.0030
    assert round(73.12 / 72.40 - 1, 4) == 0.0099
    assert round(2398 / 2410 - 1, 4) == -0.0050
    assert round(1240 / 1250 - 1, 4) == -0.0080
    assert round((1240 / 1250 - 1) / (5771 / 5800 - 1), 1) == 1.6
    assert round((4.35 - 4.20) * 100) * 3_400 == 51_000
    assert round((4.35 - 4.05) * 100) == 30 and 30 * 3_400 == 102_000
    assert mk.futures_pnl(5850, 5771, 10, 50) == R(-39_500)
    assert 5771 - 5650 == 121 and mk.futures_pnl(5771, 5650, 10, 50) == R(-60_500)


# ------------------------------------------------------------------ problems

def test_problem_25_2():
    net = 182_400 - 96_900
    assert net == 85_500
    assert net - 71_200 == 14_300
    assert round(net / 612_000, 4) == 0.1397
    import datetime as dt
    tue = dt.date(2026, 10, 20)  # a Tuesday (calendar arithmetic only)
    assert tue.weekday() == 1
    mon = tue + dt.timedelta(days=6)
    assert mon.weekday() == 0 and (mon - tue).days == 6


def test_problem_25_3():
    assert (0.8 - 1) ** 2 == R(0.04)
    assert 0.8 ** 2 == R(0.64)
    assert stats.brier_score([0.5, 0.5], [0, 1]) == R(0.25)
    o = [1] * 8 + [0] * 2
    assert stats.brier_score([0.95] * 10, o) == R(0.1825)
    assert stats.brier_score([0.8] * 10, o) == R(0.16)


def test_problem_25_4():
    rates = -20 * 82 * -8
    assert rates == 13_120
    es = mk.futures_pnl(5900, 5841, 6, 50, side=-1)
    assert es == R(17_700)
    assert round(5841 / 5900 - 1, 4) == -0.0100
    reit = 1_500_000 * -0.004
    sys_ = 1_500_000 * 1.2 * -0.01
    assert (reit, sys_, reit - sys_) == (R(-6_000), R(-18_000), R(12_000))
    fx = mk.fx_pnl(1_000_000, 1.0850, 1.0790)
    assert fx == R(-6_000)
    total = rates + es + reit + fx - 1_100
    assert total == R(17_720)
    assert es + sys_ == R(-300)
    assert rates + (es + sys_) + (reit - sys_) + fx - 1_100 == R(total)


def test_problem_25_5():
    d10 = fi.dv01(0.042, 0.042, 10)
    assert round(d10, 6) == 0.080974
    note = -d10 * 80_000
    assert round(note) == -6_478
    net = note + 30 * 85
    assert round(net) == -3_928
    eqd = 4 * 50 * 5800 + 1.2 * 3_000_000
    assert eqd == R(4_760_000)
    noi = 0.055 * 40_000_000
    assert noi == R(2_200_000)
    v1 = noi / 0.0625
    assert v1 == R(35_200_000)
    ear = 40_000_000 - v1
    assert ear == R(4_800_000)
    assert round((v1 - 26e6) / 14e6 - 1, 3) == -0.343
    assert round(40 / 14, 3) == 2.857 and round(v1 / 40e6 - 1, 3) == -0.12
    total = 40 * net - 0.12 * eqd - ear
    assert round(40 * net) == -157_116
    assert -0.12 * eqd == R(-571_200)
    assert round(total) == -5_528_316
    assert round(total / 50e6, 4) == -0.1106
    assert round(ear / -total, 3) == 0.868


def test_problem_25_6():
    f = [0.8] * 10 + [0.6] * 10 + [0.2] * 10
    o = [1] * 6 + [0] * 4 + [1] * 6 + [0] * 4 + [1] * 3 + [0] * 7
    assert (2.80, 2.40, 2.20) == (R(6 * 0.04 + 4 * 0.64), R(6 * 0.16 + 4 * 0.36), R(3 * 0.64 + 7 * 0.04))
    bs = stats.brier_score(f, o)
    assert round(bs, 4) == 0.2467
    assert round(1 - bs / 0.25, 4) == 0.0133
    rel, res, unc = _murphy(f, o)
    assert round(rel, 5) == 0.01667
    assert res == R(0.02)
    assert rel - res + unc == R(bs)


def test_problem_25_7():
    v = {"A": 0.01 * 40_000, "B": 0.05 * 150_000, "C": 0.08 * 120_000, "D": 0.005 * 60_000}
    assert v == {"A": R(400), "B": R(7_500), "C": R(9_600), "D": R(300)}
    now = {"A": 5, "B": 3, "C": 6, "D": 10}
    new = {"A": 3, "B": 7, "C": 12, "D": 2}
    assert sum(now.values()) == sum(new.values()) == 24
    w_now = sum(v[k] * now[k] for k in v)
    w_new = sum(v[k] * new[k] for k in v)
    assert (w_now, w_new, w_new - w_now) == (R(85_100), R(169_500), R(84_400))
    c_dim = 8 * 9_600 + 4 * 4_800
    assert c_dim == 96_000
    w_dim = w_new - 12 * 9_600 + c_dim
    assert (w_dim, w_dim - w_now) == (R(150_300), R(65_200))


def test_problem_25_8():
    assert round(0.35 / 0.65, 5) == 0.53846
    assert 1.8 * 0.8 * 1.6 * 1.4 == R(3.2256)
    p1 = stats.likelihood_ratio_update(0.35, 1.8 * 0.8 * 1.6 * 1.4)
    p2 = stats.likelihood_ratio_update(0.35, 1.8 * 0.8 * 1.6)
    assert round(0.35 / 0.65 * 3.2256, 5) == 1.73686
    assert round(0.35 / 0.65 * 2.304, 5) == 1.24062
    assert (round(p1, 4), round(p2, 4)) == (0.6346, 0.5537)
    assert min(p1, p2) > 0.45


def test_problem_25_9():
    assert 0.7 * 2.0 + 0.3 * -1.5 == R(0.95)
    assert round(cre.breakeven_probability(2.0, 1.5), 4) == 0.5714
    assert 0.7 * 2.0 + 0.3 * -1.8 == R(0.86)
    assert round(cre.breakeven_probability(2.0, 1.8), 4) == 0.5263
    assert stats.brier_score([0.7], [0]) == R(0.49)


def test_problem_25_10():
    dv = 60 * 85
    assert dv == 5_100
    assert dv * 12 == 61_200
    assert dv * 25 == 127_500 > 100_000
    assert math.floor(100_000 / (85 * 25)) == 47
    assert round(100_000 / (85 * 25), 2) == 47.06
    lr = 1.2 * 0.8 * 1.3
    assert lr == R(1.248)
    p = stats.likelihood_ratio_update(0.5, lr)
    assert round(p, 4) == 0.5552
    assert round(25 / 45, 4) == 0.5556
    assert round(p * 20 - (1 - p) * 25, 2) == -0.02
