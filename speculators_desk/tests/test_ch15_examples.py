"""Reproduces every number in Chapter 15 (Foreign Exchange) text, problems, and solutions.

Quote convention throughout: BASE/QUOTE at S means 1 BASE = S QUOTE (sdesk.markets).
Where possible, results are checked by an independent route (replication, inversion, telescoping).
"""

import math

import pytest

from sdesk import markets as mk
from sdesk import tvm

R = pytest.approx


def _sd(h, s_l, s_x, rho):
    return math.sqrt(s_l ** 2 + (1 - h) ** 2 * s_x ** 2 + 2 * (1 - h) * rho * s_l * s_x)


def _cip(spot, r_q, tau_q, r_b, tau_b):
    """CIP with separate day counts, written out independently of the library."""
    return spot * (1 + r_q * tau_q) / (1 + r_b * tau_b)


# --------------------------------------------------------------------------
# Section 15.1 opening problem
# --------------------------------------------------------------------------

def test_opening_problem():
    equity_gbp = 50_000_000 - 27_500_000
    assert equity_gbp == 22_500_000
    assert mk.convert(equity_gbp, 1.27, "GBP", "GBP/USD") == R(28_575_000)
    assert 3_500_000 / 50_000_000 == R(0.07)
    assert 0.18 * 28_575_000 == R(5_143_500)  # "about $5.1 million"


# --------------------------------------------------------------------------
# Equations section
# --------------------------------------------------------------------------

def test_inverse_percentage_asymmetry():
    # "A 5% rise in EUR/USD is a 4.76% fall in the dollar measured in euros."
    assert round(1 / 1.05 - 1, 4) == -0.0476


def test_hedging_transports_spread_section_15_4_6_and_15_6():
    y_us, r_usd, r_jpy = 0.075, 0.0425, 0.005
    assert round((1 + y_us) / (1 + r_usd), 4) == 1.0312
    hedged = (1 + y_us) * (1 + r_jpy) / (1 + r_usd) - 1
    assert round(hedged, 4) == 0.0363
    # identity: (1 + R_h)/(1 + r_home) = (1 + y)/(1 + r_foreign)
    assert (1 + hedged) / (1 + r_jpy) == R((1 + y_us) / (1 + r_usd))
    assert round(1.04 / 1.005, 4) == 1.0348
    us_buyer_tokyo = 1.04 * 1.0425 / 1.005 - 1
    assert round(us_buyer_tokyo, 4) == 0.0788
    # hedged equals unhedged evaluated at S_T = F (CIP check), JPY investor; USD/JPY 150
    f = mk.covered_interest_forward(150.0, r_jpy, r_usd, 1.0)
    usd0 = 1_000_000_000 / 150.0
    assert usd0 * (1 + y_us) * f / 1_000_000_000 - 1 == R(hedged)


# --------------------------------------------------------------------------
# Worked examples
# --------------------------------------------------------------------------

def test_example_15_1():
    assert round(1.0920 / 1.0850 - 1, 5) == 0.00645
    assert round(1.0850 / 1.0920 - 1, 5) == -0.00641
    assert round(147.50 / 150.00 - 1, 5) == -0.01667
    assert round(150.00 / 147.50 - 1, 5) == 0.01695
    assert round((1.0920 - 1.0850) / 0.0001) == 70
    assert mk.fx_pnl(10_000_000, 1.0850, 1.0920) == R(70_000)
    assert round((147.50 - 150.00) / 0.01) == -250
    pnl_jpy = mk.fx_pnl(10_000_000, 150.00, 147.50)
    assert pnl_jpy == R(-25_000_000)
    pnl_usd = mk.convert(pnl_jpy, 147.50, "JPY", "USD/JPY")
    assert round(pnl_usd) == -169_492
    assert 10_000_000 * 0.0001 == R(1_000)
    assert 10_000_000 * 0.01 == R(100_000)
    assert round(100_000 / 150, 2) == 666.67
    # independent check: short JPY 1.5bn
    assert round(1_500_000_000 / 147.50) == 10_169_492


def test_example_15_2():
    eb, ea, jb, ja, gb, ga = 1.0848, 1.0852, 149.98, 150.02, 1.2698, 1.2702
    assert round(eb * jb, 3) == 162.698
    assert round(ea * ja, 3) == 162.802
    assert round(eb / ga, 5) == 0.85404
    assert round(ea / gb, 5) == 0.85462
    profit = 1_000_000 * (162.90 - ea * ja)
    assert round(profit) == 98_296
    assert round(profit / 150) == 655
    assert (ea * ja - eb * jb) / 0.01 == R(10.34, abs=0.01)


def test_example_15_3_desk_1987():
    s, d = 1.60, 182
    usd = 1 + 0.07 * d / 360
    gbp = 1 + 0.095 * d / 365
    dem = 1 + 0.04 * d / 360
    assert round(usd, 7) == 1.0353889
    assert round(gbp, 7) == 1.0473699
    assert round(dem, 7) == 1.0202222
    f = _cip(s, 0.07, d / 360, 0.095, d / 365)
    assert round(f, 6) == 1.581697
    # library route, folding ACT/365 into the rate
    assert mk.covered_interest_forward(s, 0.07, 0.095 * 360 / 365, d / 360) == R(f, rel=1e-12)
    assert round((f - s) / 0.0001, 1) == -183.0
    assert s * 1.80 == R(2.88)
    f_usddem = mk.covered_interest_forward(1.80, 0.04, 0.07, d / 360)
    assert round(f_usddem, 6) == 1.773633
    assert round((f_usddem - 1.80) / 0.0001, 1) == -263.7
    f_gbpdem = f * f_usddem
    assert round(f_gbpdem, 6) == 2.805351
    # route 2: direct CIP on GBP and DEM
    assert _cip(2.88, 0.04, d / 360, 0.095, d / 365) == R(f_gbpdem, rel=1e-12)
    assert round(5_000_000 * f) == 7_908_487
    assert 5_000_000 * 1.52 == R(7_600_000)
    hedge = mk.fx_pnl(5_000_000, f, 1.52, side=-1)
    assert round(hedge) == 308_487
    assert round(mk.fx_pnl(5_000_000, f, 1.68, side=-1)) == -491_513
    # (d) day-count error
    f_wrong = _cip(s, 0.07, d / 360, 0.095, d / 360)
    assert round(1 + 0.095 * d / 360, 7) == 1.0480278
    assert round(f_wrong, 6) == 1.580704
    assert round((f - f_wrong) / 0.0001, 1) == 9.9
    assert round(5_000_000 * (f - f_wrong)) == 4_965
    approx = s * (0.07 * d / 360 - 0.095 * d / 365) / 0.0001
    assert round(approx, 1) == -191.7


def _carry(n, s0, st, ri, rf, tau=1.0):
    pnl = n * ((1 + ri * tau) * st / s0 - (1 + rf * tau))
    s = st / s0 - 1
    return pnl, n * (ri - rf) * tau, n * s, n * ri * tau * s


def test_example_15_4():
    n, margin = 1_500_000_000, 150_000_000
    assert mk.convert(n, 150.0, "JPY", "USD/JPY") == R(10_000_000)
    expected = {150.0: (56_250_000, 0, 0, 0.375),
                147.0: (24_975_000, -30_000_000, -1_275_000, 0.1665),
                135.0: (-100_125_000, -150_000_000, -6_375_000, -0.6675)}
    for st, (tot, spot, cross, rom) in expected.items():
        pnl, carry, sp, cr = _carry(n, 150.0, st, 0.0425, 0.005)
        assert pnl == R(tot)
        assert carry == R(56_250_000)
        assert sp == R(spot, abs=1e-6)
        assert cr == R(cross, abs=1e-6)
        assert carry + sp + cr == R(pnl)
        assert pnl / margin == R(rom)
    f = mk.covered_interest_forward(150.0, 0.005, 0.0425, 1.0)
    assert round(f, 3) == 144.604
    assert round(f / 150 - 1, 4) == -0.0360
    assert _carry(n, 150.0, f, 0.0425, 0.005)[0] == R(0, abs=1e-3)


def test_example_15_5():
    c = (1 + 0.0425 / 12) - (1 + 0.005 / 12)
    loss = (1 + 0.0425 / 12) * 0.92 - (1 + 0.005 / 12)
    assert round(c, 6) == 0.003125
    assert round(loss, 5) == -0.07716
    p_star = c / (c - loss)
    assert round(p_star, 4) == 0.0389
    ev = 0.97 * c + 0.03 * loss
    assert round(0.97 * c, 6) == 0.003031
    assert round(0.03 * loss, 6) == -0.002315
    assert round(ev, 6) == 0.000717
    assert round(ev * 12, 4) == 0.0086
    assert round(0.97 ** 12, 3) == 0.694
    assert round(10 * loss, 3) == -0.772
    assert round(-loss / c, 1) == 24.7
    assert round(2 * loss, 3) == -0.154
    assert (1 - p_star) * c + p_star * loss == R(0, abs=1e-12)
    assert round(1 - 0.97 ** 12, 2) == 0.31  # "roughly a 30% chance"


def test_example_15_6():
    s, tau = 1.0850, 365 / 360
    f_cip = mk.covered_interest_forward(s, 0.0425, 0.025, tau)
    assert round(f_cip, 6) == 1.103775
    assert round((f_cip - s) / 0.0001, 1) == 187.8
    f_mkt = f_cip + 0.0020
    assert round(f_mkt, 6) == 1.105775
    b = (s * (1 + 0.0425 * tau) / f_mkt - 1) / tau - 0.025
    assert round(b * 10_000, 1) == -18.3
    # check: plugging b back reproduces the market forward
    assert s * (1 + 0.0425 * tau) / (1 + (0.025 + b) * tau) == R(f_mkt, rel=1e-12)
    usd0 = mk.convert(20_000_000, s, "EUR", "EUR/USD")
    assert usd0 == R(21_700_000)
    t_cip = 21_000_000 * f_cip
    t_mkt = 21_000_000 * f_mkt
    assert round(t_cip) == 23_179_282
    assert round(t_mkt) == 23_221_282
    assert round(t_cip / usd0 - 1, 5) == 0.06817
    assert round(t_mkt / usd0 - 1, 5) == 0.07011
    assert t_mkt - t_cip == R(42_000)
    assert 20_000_000 * 0.0020 == R(40_000)
    assert 1.05 * (1 + 0.0425 * tau) / (1 + 0.025 * tau) - 1 == R(t_cip / usd0 - 1)


def _attack_time(r0, mu, alpha):
    return (r0 - alpha * mu) / mu


def test_example_15_7():
    assert 40 / 2 == 20
    assert _attack_time(40, 2, 5) == R(15)
    assert 5 * 2 == 10
    assert _attack_time(40, 2, 8) == R(12)
    assert 40 - 15 * 2 == 10


def _one_way(di, tau, d, u):
    c = di * tau
    return c, (u + c) / (d + u)


def test_example_15_8():
    c, p_bounce = _one_way(0.06, 7 / 365, 0.10, 0.01)
    assert round(c, 6) == 0.001151
    assert round(c / 0.10, 4) == 0.0115
    assert round(p_bounce, 4) == 0.1014
    req = 0.5 * 0.10 - 0.5 * 0.01
    assert req == R(0.045)
    assert round(req * 365 / 7, 3) == 2.346
    received = 15 / 2.7780
    cost = 15 / 2.55
    assert round(received, 4) == 5.3996
    assert round(cost, 4) == 5.8824
    assert round(cost - received, 4) == 0.4828
    # check: EV at p* is zero
    assert p_bounce * (0.10 - c) - (1 - p_bounce) * (0.01 + c) == R(0, abs=1e-12)


def _rolling(path, h, n, s0, k, dist, sale_eq):
    f = s0 * k
    fwds, sett, unh = [f], [], [-n * s0]
    for i, s in enumerate(path):
        sett.append(mk.fx_pnl(h * n, f, s, side=-1))
        gbp = dist + (sale_eq if i == len(path) - 1 else 0)
        unh.append(gbp * s)
        f = s * k
        fwds.append(f)
    hed = [unh[0]] + [a + b for a, b in zip(unh[1:], sett)]
    return fwds, sett, unh, hed


def test_example_15_9():
    n, s0 = 22_500_000, 1.27
    dist = 3_500_000 - 0.06 * 27_500_000
    assert dist == R(1_850_000)
    sale_eq = 53_000_000 * 0.98 - 27_500_000
    assert sale_eq == R(24_440_000)
    k = 1.0425 / 1.0475
    assert round(k, 6) == 0.995227
    fwds, sett, unh, hed = _rolling([1.15, 1.22, 1.32], 1.0, n, s0, k, dist, sale_eq)
    assert [round(x, 6) for x in fwds[:3]] == [1.263938, 1.144511, 1.214177]
    assert [round(x) for x in sett] == [2_563_604, -1_698_508, -2_381_026]
    assert round(sum(sett)) == -1_515_931
    assert [round(x) for x in unh] == [-28_575_000, 2_127_500, 2_257_000, 34_702_800]
    assert [round(x) for x in hed] == [-28_575_000, 4_691_104, 558_492, 32_321_774]
    assert round(tvm.irr(unh), 4) == 0.1175
    assert round(tvm.irr(hed), 4) == 0.1062
    assert round(tvm.irr([-n, dist, dist, dist + sale_eq]), 4) == 0.1081
    # (d) telescoping identity
    tele = n * ((s0 - 1.32) + (k - 1) * (s0 + 1.15 + 1.22))
    assert tele == R(sum(sett))
    assert round(k - 1, 6) == -0.004773
    assert round((k - 1) * (s0 + 1.15 + 1.22), 6) == -0.017375
    assert round(n * (s0 - 1.32)) == -1_125_000
    assert round(n * (k - 1) * (s0 + 1.15 + 1.22)) == -390_931
    # check: on-forward path gives zero settlements and IRR 10.28%
    path_f = [s0 * k, s0 * k ** 2, s0 * k ** 3]
    _, sett_f, unh_f, _ = _rolling(path_f, 1.0, n, s0, k, dist, sale_eq)
    assert all(abs(x) < 1e-6 for x in sett_f)
    assert round(tvm.irr(unh_f), 4) == 0.1028
    # by year 3 equity worth 24.44m vs 22.5m hedged: ~8% unhedged
    assert round(1 - n / sale_eq, 2) == 0.08


def test_example_15_10():
    s_l, s_x, rho = 0.12, 0.09, -0.25
    h_star = 1 + rho * s_l / s_x
    assert round(h_star, 3) == 0.667
    n_usd = 28_575_000
    h_liq = 2_000_000 / (2 * s_x * n_usd)
    assert round(h_liq, 3) == 0.389
    vols = [round(_sd(h, s_l, s_x, rho), 4) for h in (0, h_liq, h_star, 1.0)]
    assert vols == [0.1308, 0.1188, 0.1162, 0.1200]
    reserve = h_star * 2 * s_x * n_usd
    assert round(reserve) == 3_429_000
    assert round(reserve - 2_000_000, -4) == 1_430_000
    assert round((reserve - 2_000_000) / n_usd, 2) == 0.05
    assert round((_sd(h_liq, s_l, s_x, rho) - _sd(h_star, s_l, s_x, rho)) * 10_000) == 27
    assert round(_sd(h_liq, s_l, s_x, rho), 5) == 0.11885
    assert round(_sd(h_star, s_l, s_x, rho), 5) == 0.11619
    # h* minimizes variance: numeric check
    grid = [i / 1000 for i in range(0, 1501)]
    best = min(grid, key=lambda h: _sd(h, s_l, s_x, rho))
    assert best == R(h_star, abs=1e-3)
    # with rho = 0, h* = 1
    assert 1 + 0 * s_l / s_x == 1


def test_section_15_9_erm_band_arithmetic():
    assert round(2.95 * 1.0618, 3) == 3.132
    assert round(2.95 / 1.0618, 3) == 2.778
    # symmetric under inversion: the same ratio band applies to DEM/GBP
    lo, hi = 2.95 / 1.0618, 2.95 * 1.0618
    assert (1 / lo) / (1 / 2.95) == R(1.0618)
    assert (1 / 2.95) / (1 / hi) == R(1.0618)


# --------------------------------------------------------------------------
# Problems
# --------------------------------------------------------------------------

def test_problem_15_1():
    assert round(150 / 155 - 1, 4) == -0.0323
    assert round(155 / 150 - 1, 4) == 0.0333
    assert round(1 / 1.05 - 1, 4) == -0.0476


def test_problem_15_2():
    assert round(1.20 / 1.25 - 1, 4) == -0.04
    assert round(1.25 / 1.20 - 1, 4) == 0.0417
    assert round((1.20 - 1.25) / 0.0001) == -500
    assert mk.fx_pnl(5_000_000, 1.25, 1.20, side=-1) == R(250_000)


def test_problem_15_3():
    assert round(0.6600 * 150.00, 3) == 99.000
    assert round(0.6604 * 150.04, 3) == 99.086
    assert round(1.0850 * 0.8800, 5) == 0.95480
    assert round(1.0854 * 0.8804, 5) == 0.95559


def test_problem_15_4():
    f = _cip(150.0, 0.004, 90 / 365, 0.043, 90 / 360)
    assert f == R(mk.covered_interest_forward(150.0, 0.004 * 360 / 365, 0.043, 0.25), rel=1e-12)
    assert round(f, 3) == 148.551
    assert round(1 + 0.004 * 90 / 365, 6) == 1.000986
    assert round(1 + 0.043 * 0.25, 6) == 1.010750
    assert round((f - 150) / 0.01, 1) == -144.9
    assert round((f / 150 - 1) * 360 / 90, 4) == -0.0386
    # leg-by-leg replication
    usd_now = 10_000_000 / 1.01075
    assert round(usd_now) == 9_893_643
    yen_borrowed = usd_now * 150
    assert yen_borrowed == R(1_484_046_500, abs=1)
    yen_repay = yen_borrowed * (1 + 0.004 * 90 / 365)
    assert round(yen_repay) == 1_485_510_217
    assert 10_000_000 * 148.80 == R(1_488_000_000)
    profit = 1_488_000_000 - yen_repay
    assert round(profit) == 2_489_783
    assert 10_000_000 * (148.80 - f) == R(profit)


def test_problem_15_5():
    n = 10_000_000 * 99.0
    assert n == R(990_000_000)
    pnl, carry, spot, cross = _carry(n, 99.0, 92.0, 0.041, 0.005, 0.5)
    assert round(92 / 99 - 1, 4) == -0.0707
    assert pnl == R(-53_615_000)
    assert carry == R(17_820_000)
    assert spot == R(-70_000_000)
    assert cross == R(-1_435_000)
    assert round(pnl / (0.1 * n), 4) == -0.5416
    f = mk.covered_interest_forward(99.0, 0.005, 0.041, 0.5)
    assert round(f, 3) == 97.254
    assert _carry(n, 99.0, 99.0, 0.041, 0.005, 0.5)[0] == R(17_820_000)
    assert round(17_820_000 / 99_000_000, 3) == 0.180


def test_problem_15_6():
    assert 24 / 1.5 == R(16)
    assert _attack_time(24, 1.5, 4) == R(12)
    assert 4 * 1.5 == R(6)
    assert _attack_time(30, 1.5, 4) == R(16)
    assert _attack_time(24, 1.5, 8) == R(8)


def test_problem_15_7():
    f0 = mk.covered_interest_forward(1.10, 0.04, 0.02, 1.0)
    assert round(f0, 6) == 1.121569
    f1 = mk.covered_interest_forward(1.00, 0.04, 0.02, 1.0)
    assert round(f1, 6) == 1.019608
    n = 66_000_000
    s1 = n * (1 / f0 - 1 / 1.00)
    s2 = n * (1 / f1 - 1 / 1.05)
    assert round(n / f0) == 58_846_154
    assert round(s1) == -7_153_846
    assert round(n / f1) == 64_730_769
    assert round(n / 1.05) == 62_857_143
    assert round(s2) == 1_873_626
    eq = mk.convert(n, 1.10, "USD", "EUR/USD")
    assert eq == R(60_000_000)
    assert round(-s1 / eq, 4) == 0.1192
    noi_eur = mk.convert(3_630_000, 1.00, "USD", "EUR/USD")
    assert round(noi_eur / -s1, 2) == 0.51
    assert round(-s1 - noi_eur) == 3_523_846
    assert n / 1.00 - n / 1.10 == R(6_000_000)
    assert 3_630_000 / 66_000_000 == R(0.055)


def test_problem_15_8():
    s_l, s_x, rho = 0.15, 0.10, 0.30
    h_star = 1 + rho * s_l / s_x
    assert h_star == R(1.45)
    h_liq = 1_500_000 / (2 * s_x * 20_000_000)
    assert h_liq == R(0.375)
    vols = [round(_sd(h, s_l, s_x, rho), 4) for h in (0, h_liq, 1.0, h_star)]
    assert vols == [0.2037, 0.1790, 0.1500, 0.1431]
    assert 2 * s_x * 20_000_000 == R(4_000_000)
    assert round(_sd(h_liq, s_l, s_x, rho) - _sd(1.0, s_l, s_x, rho), 3) == 0.029


def test_problem_15_9():
    c, p = _one_way(0.15, 1 / 12, 0.15, 0.005)
    assert c == R(0.0125)
    assert round(p, 4) == 0.1129
    req = 0.40 * 0.15 - 0.60 * 0.005
    assert req == R(0.057)
    assert req * 12 == R(0.684)
    assert 0.05 + req * 12 == R(0.734)
    assert 20e9 * 25 == R(500e9)
    assert 20e9 * 40 == R(800e9)
    loss_lc = 20e9 * (40 - 25)
    assert loss_lc == R(300e9)
    assert loss_lc / 40 == R(7.5e9)


def test_problem_15_10():
    hedged = 1.11 / 1.09 - 1
    assert round(hedged, 4) == 0.0183
    assert hedged < 0.0425
    ev = 1.11 * (1 - 0.30 * 0.35) - 1
    assert round(1 - 0.30 * 0.35, 3) == 0.895
    assert ev == R(-0.00655)
    p = (1 - 1.0425 / 1.11) / 0.35
    assert round(p, 3) == 0.174
    assert 1.11 * (1 - 0.35 * p) == R(1.0425)


def test_drill_d148_hedged_yield():
    assert round(1.12 / 1.10 - 1, 3) == 0.018


def test_section_15_9_and_15_4_9_text_figures():
    # "even a five-point rise in the overnight rate costs a speculator about a tenth of a percent" (one week)
    assert round(0.05 * 7 / 365, 4) == 0.0010
    # "a 6-point rate differential costs only about 0.12%" (one week)
    assert round(0.06 * 7 / 365, 4) == 0.0012
    # "the speculator risks 1.1% to make 9.9%"
    c = 0.06 * 7 / 365
    assert round(0.01 + c, 3) == 0.011
    assert round(0.10 - c, 3) == 0.099
    # forward discount on sterling in the opening problem: about 0.48%
    assert round(1.0425 / 1.0475 - 1, 4) == -0.0048
