"""Reproduces every number in Chapter 14 text, problems, and solutions.

Library: sdesk.x_equities (new for this chapter), sdesk.markets,
sdesk.x_cre_distress (REIT implied cap), sdesk.x_dynamics (momentum),
sdesk.x_microstructure (SUE). Independent routes (closed forms, reverse
calculations, simple-interest carry) check the library where possible.
"""

import math

import pytest

from sdesk import markets as mk
from sdesk import x_cre_distress as xd
from sdesk import x_dynamics as xdyn
from sdesk import x_equities as xe
from sdesk import x_microstructure as xm

R = pytest.approx
ES, MES = 50, 5
F143 = 6_000 * math.exp((0.043 - 0.013) * 0.25)


# ------------------------------------------------------------- library unit tests

def test_library_boundaries():
    # zero leverage: asset beta = equity beta; relever inverts unlever
    assert xe.unlever_beta(1.3, 0.0) == R(1.3)
    assert xe.relever_beta(xe.unlever_beta(1.3, 0.4), 0.4) == R(1.3)
    # perfect hedge leaves only residual vol; zero residual -> zero vol
    assert xe.hedged_volatility(1.0, 0.2, 0.0, 1.0)["hedged"] == R(0.0, abs=1e-12)
    # two-stage with g1 = g2 collapses to Gordon
    k = xe.two_stage_implied_return(100, 4.0, 0.03, 5, 0.03)
    assert k == R(0.07, abs=1e-9)
    with pytest.raises(ValueError):
        xe.two_stage_pv(0.03, 4.0, 0.03, 5, 0.03)
    # no margin buffer -> call immediately
    assert xe.margin_call_points(10_000, 10_000, 50) == 0
    # ES and MES: ten micros = one E-mini
    assert 10 * mk.futures_notional(6_000, MES) == mk.futures_notional(6_000, ES)
    assert 0.25 * ES == R(12.50) and 0.25 * MES == R(1.25)


# ------------------------------------------------------------- Example 14.1

def test_example_14_1():
    mcap = 48 * 200e6
    ev = xe.enterprise_value(mcap, 4.2e9, 0.3e9)
    assert (mcap, ev) == (R(9.6e9), R(13.5e9))
    b = xe.income_bridge(1.2e9, 0.45e9, 0.24e9, 0.21, 200e6)
    assert (b["ebit"], b["ebt"], b["net_income"]) == (R(0.75e9), R(0.51e9), R(402.9e6))
    assert b["eps"] == R(2.0145)
    assert round(48 / b["eps"], 2) == 23.83
    assert round(b["eps"] / 48, 4) == 0.0420
    assert ev / 1.2e9 == R(11.25)
    assert round(1.2e9 / ev, 4) == 0.0889
    capex = 0.04 * 4.0e9
    c = xe.implied_cap_from_ev(1.2e9, capex, ev)
    assert round(c, 4) == 0.0770
    # bridge table
    assert round((1.04e9 - 0.24e9) / mcap, 4) == 0.0833
    assert round(0.8e9 * 0.79 / mcap, 4) == 0.0658
    assert round(0.24e9 / 4.2e9, 4) == 0.0571
    assert (0.45e9 - 0.16e9) * 0.79 == R(229.1e6)
    assert 0.8e9 * 0.79 - 229.1e6 == R(402.9e6)
    # check via net debt identity
    rd = 0.24e9 / 3.9e9
    assert round(rd, 5) == 0.06154
    assert c + (3.9 / 9.6) * (c - rd) == R((1.04e9 - 0.24e9) / mcap)
    assert round((3.9 / 9.6) * (c - rd), 4) == 0.0063


# ------------------------------------------------------------- Example 14.2

def test_example_14_2():
    k = xe.gordon_implied_return(0.03, 0.045)
    assert k == R(0.075) and k - 0.0425 == R(0.0325)
    cf5 = 180 * 1.06 ** 4
    assert round(cf5, 2) == 227.25
    k2 = xe.two_stage_implied_return(6_000, 180, 0.06, 5, 0.04)
    assert round(k2, 4) == 0.0722 and round(k2 - 0.0425, 4) == 0.0297
    assert xe.two_stage_pv(k2, 180, 0.06, 5, 0.04) == R(6_000)
    assert 0.07 < k2 < 0.09
    assert round(6_000 / 280, 2) == 21.43
    assert round(280 / 6_000, 4) == 0.0467
    assert round(xe.earnings_yield_gap(6_000 / 280, 0.02), 4) == 0.0267
    assert round(280 / 6_000 - 0.0425, 4) == 0.0042
    assert round(1.0425 / 1.02 - 1, 4) == 0.0221
    real_k = 1.075 / (1.0425 / 1.02) - 1
    assert 0.051 < real_k < 0.0525 and 0.075 - 0.0225 == R(0.0525)
    assert 0.07 + 0.03 - 0.0425 == R(0.0575)


# ------------------------------------------------------------- Example 14.3

def test_example_14_3():
    f = mk.futures_fair_value(6_000, 0.043, 0.013, 0.25)
    assert f == R(F143)
    assert round(math.exp(0.0075), 7) == 1.0075282
    assert round(f, 2) == 6045.17 and round(f - 6_000, 2) == 45.17
    assert round(mk.futures_notional(f, ES)) == 302_258
    assert round(mk.futures_notional(f, MES)) == 30_226
    simple = xe.futures_fair_value_simple(6_000, 0.043, 0.25, 6_000 * 0.013 * 0.25)
    assert simple == R(6_045.00)
    assert 6_000 * (1 + 0.043 * 0.25) == R(6_064.50)
    assert round(f - simple, 2) == 0.17 and (f - simple) < 0.25
    assert round((f - simple) * ES, 1) == 8.5


# ------------------------------------------------------------- Example 14.4

def test_example_14_4():
    notional = mk.futures_notional(6_045.0, ES, 10)
    assert notional == R(3_022_500)
    im = 10 * 24_000
    assert round(notional / im, 1) == 12.6
    pts = xe.margin_call_points(24_000, 21_800, ES)
    assert pts == R(44) and round(pts / 6_045, 4) == 0.0073
    loss = mk.futures_pnl(6_045.0, 6_045.0 * 0.95, 10, ES)
    assert loss == R(-151_125)
    assert round(-loss / im, 2) == 0.63
    assert -loss / notional == R(0.05)


# ------------------------------------------------------------- Example 14.5

def test_example_14_5():
    n = xe.beta_hedge_contracts(1.10, 40e6, F143, ES)
    assert round(n, 2) == 145.57
    assert round((n - 145) * 10, 1) == 5.7
    assert round(146 * F143 * ES / 40e6, 3) == 1.103
    assert round(F143 * 0.10, 3) == 604.517
    gain = mk.futures_pnl(F143, F143 * 0.9, 146, ES, side=-1)
    assert round(gain) == 4_412_973
    sleeve = 40e6 * (1.10 * -0.10 - 0.03)
    assert sleeve == R(-5_600_000)
    assert round(sleeve + gain) == -1_187_027
    assert round(-0.03 * 40e6 + (146 - n) * ES * F143 * 0.10) == -1_187_027
    assert round((146 - n) * ES * F143 * 0.10) == 12_973


# ------------------------------------------------------------- Example 14.6

def test_example_14_6():
    d = xd.reit_implied_cap_rate(17.5, 210e6, 2.40e9, 0.15e9, 0.20e9, 0.05e9, 0.47e9)
    assert d["market_cap"] == R(3.675e9) and d["implied_re_value"] == R(5.975e9)
    assert round(d["implied_cap"], 4) == 0.0787
    nv = xd.reit_nav_per_share(0.47e9, 0.07, 2.40e9, 0.15e9, 0.20e9, 0.05e9, 210e6)
    assert round(nv["gross_asset_value"] / 1e9, 3) == 6.714
    assert round(nv["nav"] / 1e9, 3) == 4.414
    assert round(nv["nav_per_share"], 2) == 21.02
    assert round(17.5 / nv["nav_per_share"] - 1, 3) == -0.167
    assert round(nv["gross_asset_value"] / nv["nav"], 2) == 1.52
    assert round((d["implied_cap"] - 0.07) * 1e4) == 87
    # check: NAV at the implied cap equals the share price
    nv2 = xd.reit_nav_per_share(0.47e9, d["implied_cap"], 2.40e9, 0.15e9, 0.20e9, 0.05e9, 210e6)
    assert nv2["nav_per_share"] == R(17.5)
    # own portfolio at the implied cap
    v = 120e6 * 0.07 / d["implied_cap"]
    assert round(v / 1e6, 1) == 106.8 and round((v - 72e6) / 1e6, 1) == 34.8
    assert round((v - 72e6) / 48e6 - 1, 3) == -0.275


# ------------------------------------------------------------- Example 14.7

def test_example_14_7():
    ba = xe.unlever_beta(1.30, 0.40)
    be = xe.relever_beta(ba, 0.60)
    assert (ba, be) == (R(0.78), R(1.95))
    assert be * 48e6 == R(93.6e6) and ba * 120e6 == R(93.6e6)
    n = xe.beta_hedge_contracts(be, 48e6, F143, ES)
    assert round(n, 2) == 309.67
    hb = 310 * F143 * ES / 48e6
    assert round(hb, 3) == 1.952
    h = xe.hedged_volatility(be, 0.18, 0.30, hb)
    assert round(h["unhedged"], 4) == 0.4617
    assert round(h["rho"], 3) == 0.760
    assert round(h["hedged"], 4) == 0.3000
    assert round(h["variance_reduction"], 3) == 0.578
    assert round((1.95 * 0.18) ** 2, 4) == 0.1232
    assert be * 48e6 * 0.0325 * 0.5 == R(1_521_000)
    vm = 310 * F143 * ES * 0.15
    assert round(vm) == 14_055_018
    assert round(vm / 48e6, 2) == 0.29
    h2 = xe.hedged_volatility(1.40, 0.18, 0.30, hb)
    assert round(h2["unhedged"], 4) == 0.3918 and round(h2["hedged"], 4) == 0.3160
    assert round(hb - 1.40, 3) == 0.552


# ------------------------------------------------------------- Example 14.8

def test_example_14_8():
    q, p0, fee = 20_000, 50.0, 0.06 * 1_000_000
    pl = [q * (p0 - p) - fee for p in (35, 50, 80)]
    assert pl == [R(240_000), R(-60_000), R(-660_000)]
    probs = [0.5, 0.3, 0.2]
    assert sum(a * b for a, b in zip(pl, probs)) == R(-30_000)
    assert sum(p * w for p, w in zip((35, 50, 80), probs)) == R(48.5)
    pstar = xe.short_margin_call_price(50, 0.5, 0.30)
    assert round(pstar, 2) == 57.69 and round(pstar / 50 - 1, 3) == 0.154
    # independent: equity = 1.5m - 20,000 P = 0.3 x 20,000 P
    assert 1.5e6 - q * pstar == R(0.3 * q * pstar)
    assert 1.5e6 - q * 80 == R(-100_000)


def test_section_14_4_margin_rules():
    assert xe.long_margin_call_price(1.0, 0.5, 0.25) == R(2 / 3)
    p = xe.long_margin_call_price(50, 0.5, 0.25)
    assert (p - 25) / p == R(0.25)  # equity/value at the trigger equals maintenance
    assert xe.short_margin_call_price(1.0, 0.5, 0.30) == R(1.5 / 1.3)
    assert xe.implied_cap_from_multiple(12.5, 0.30, 0.04) == R(0.0693333, abs=1e-6)
    assert round(0.04 / 0.30, 3) == 0.133


# ------------------------------------------------------------- Section 14.9 (history)

def test_section_14_9_history():
    assert round(1_114.11 / 5_048.62 - 1, 3) == -0.779
    assert round(5_048.62 / 1_114.11 - 1, 2) == 3.53
    assert 2015 - 2000 == 15
    assert round(776.76 / 1_527.46 - 1, 2) == -0.49
    assert round(1 / 44.2, 4) == 0.0226
    assert round(1 / 44.2 - 0.043, 4) == -0.0204
    assert round(81.81 - 145, 0) == -63
    assert 27_454 / 10_000 == R(2.7454)
    assert round(2.7454 ** 0.1 - 1, 3) == 0.106
    assert round(0.909 ** 0.1 - 1, 4) == -0.0095


# ------------------------------------------------------------- problems

def test_problem_14_2():
    assert mk.futures_pnl(5_900.00, 5_860.25, 3, MES, side=-1) == R(596.25)
    assert mk.futures_pnl(5_900.00, 5_860.25, 3, ES, side=-1) == R(5_962.50)
    ticks = (5_900.00 - 5_860.25) / 0.25
    assert ticks == R(159)
    assert mk.futures_pnl_ticks(ticks, 1.25, 3, side=1) == R(596.25)
    assert mk.futures_notional(5_900, MES, 3) == R(88_500)


def test_problem_14_3():
    c = xe.implied_cap_from_multiple(12.5, 0.30, 0.04)
    assert round(c, 4) == 0.0693 and c < 0.075
    assert round(1 - 0.04 / 0.30, 4) == 0.8667


def test_problem_14_4():
    f = mk.futures_fair_value(5_500, 0.04, 0.015, 0.5)
    assert round(f, 2) == 5569.18
    lo, hi = xe.no_arbitrage_band(f, 4)
    assert 5_585 > hi and 5_560 < lo
    assert round(5_585 - f, 2) == 15.82
    assert round((5_585 - f - 4) * ES, 2) == 590.93
    assert round(f - 5_560, 2) == 9.18
    assert round((f - 5_560 - 4) * ES, 2) == 259.07


def test_problem_14_5():
    k = xe.two_stage_implied_return(5_000, 170, 0.08, 5, 0.035)
    assert round(k, 4) == 0.0747 and round(k - 0.04, 4) == 0.0347
    g = xe.gordon_implied_return(0.034, 0.035)
    assert g == R(0.069) and g - 0.04 == R(0.029)
    assert round((k - g) * 1e4) == 57
    k_hi = xe.two_stage_implied_return(5_000, 170, 0.08, 5, 0.040)
    assert 0.0040 < k_hi - k < 0.0050  # +50 bp on g2 moves k by nearly 50 bp


def test_problem_14_6():
    assert xm.standardized_surprise(1.32, 1.20, 0.05) == R(2.4)
    assert 60 / 2.40 == R(25.0)
    eps1 = 2.40 * 1.04
    assert eps1 == R(2.496)
    p1 = eps1 * 23
    assert round(p1, 2) == 57.41 and round(p1 / 60 - 1, 3) == -0.043
    assert 23 / 25 - 1 == R(-0.08)


def test_problem_14_7():
    b = xe.breadth([3_000, 2_500, 800, 400, 300], [0.25, 0.18, -0.06, -0.10, -0.12])
    assert round(b["cap_weighted"], 4) == 0.1537
    assert b["equal_weighted"] == R(0.03)
    assert (b["advancers"], b["decliners"]) == (2, 3)
    assert [round(x, 4) for x in b["contributions"]] == [0.1071, 0.0643, -0.0069, -0.0057, -0.0051]
    assert round(sum(b["contributions"][:2]), 4) == 0.1714
    mom = [0.02, -0.01, 0.03, 0.01, -0.04, 0.02, 0.015, -0.02, 0.01, 0.03, -0.015, 0.01]
    t = xdyn.tsmom_position(mom, 0.20, 0.10)
    assert round(t["trailing"], 4) == 0.0589
    assert t["signal"] == 1 and t["weight"] == R(0.5)


def test_problem_14_8():
    fee = 0.25 * 0.5 * 1_500_000
    assert fee == R(187_500)
    pl = [50_000 * 30 * 0.4 - fee, -fee, -50_000 * 30 * 0.6 - fee]
    assert pl == [R(412_500), R(-187_500), R(-1_087_500)]
    probs = [0.45, 0.25, 0.30]
    assert [round(a * b) for a, b in zip(pl, probs)] == [185_625, -46_875, -326_250]
    assert sum(a * b for a, b in zip(pl, probs)) == R(-187_500)
    assert 0.45 * -0.4 + 0.30 * 0.6 == R(0.0, abs=1e-12)
    pstar = xe.short_margin_call_price(30, 0.5, 0.30)
    assert round(pstar, 2) == 34.62 and round(pstar / 30 - 1, 3) == 0.154


def test_problem_14_9():
    n = xe.beta_hedge_contracts(0.85, 25e6, 5_600, ES)
    assert round(n, 2) == 75.89
    assert 0.85 * 25e6 == R(21.25e6) and 5_600 * ES == 280_000
    assert 21.25e6 * 0.03 * 4 / 12 == R(212_500)
    assert mk.futures_pnl(5_600, 5_600 * 1.10, 76, ES, side=-1) == R(-2_128_000)


def test_problem_14_10():
    d = xd.reit_implied_cap_rate(11, 150e6, 1.9e9, 0, 0.1e9, 0, 0.27e9)
    assert d["market_cap"] == R(1.65e9) and d["implied_re_value"] == R(3.45e9)
    assert round(d["implied_cap"], 4) == 0.0783
    nv = xd.reit_nav_per_share(0.27e9, 0.07, 1.9e9, 0, 0.1e9, 0, 150e6)
    assert round(nv["gross_asset_value"] / 1e9, 3) == 3.857
    assert round(nv["nav"] / 1e9, 3) == 2.057
    assert round(nv["nav_per_share"], 2) == 13.71
    assert round(11 / nv["nav_per_share"] - 1, 3) == -0.198
    v0, v1 = 18e6 / 0.07, 18e6 / d["implied_cap"]
    debt = 0.55 * v0
    assert round(v0 / 1e6, 1) == 257.1 and round(debt / 1e6, 1) == 141.4
    assert round((v0 - debt) / 1e6, 1) == 115.7
    assert round(v1 / 1e6, 1) == 230.0 and round(v1 / v0 - 1, 3) == -0.106
    assert round((v1 - debt) / 1e6, 1) == 88.6
    assert round((v1 - debt) / (v0 - debt) - 1, 3) == -0.235
    assert round((d["implied_cap"] - 0.07) * 1e4) == 83
