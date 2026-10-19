"""Reproduces every number in Chapter 19 text, problems, and solutions.

Where possible, numbers are checked by a second route (hand formula, identity,
or simulation-free enumeration check) in addition to the x_alt_assets library.
"""

import math

import pytest

from sdesk import cre, stats, tvm
from sdesk import x_alt_assets as aa
from sdesk import x_microstructure as ms

R = pytest.approx

# --------------------------------------------------------------------------
# Example 19.1 — VC power law
# --------------------------------------------------------------------------
VC_M = [0, 1, 3, 10, 50]
VC_P = [0.45, 0.30, 0.15, 0.08, 0.02]


@pytest.fixture(scope="module")
def vc20():
    return aa.portfolio_multiple_distribution(VC_M, VC_P, 20)


def test_example_19_1_deal_level():
    mu = sum(m * p for m, p in zip(VC_M, VC_P))
    assert mu == R(2.55)
    assert round(0.02 * 50 / mu, 3) == 0.392


def test_example_19_1_fund_distribution(vc20):
    assert sum(p for _, p in vc20) == R(1.0)
    assert aa.distribution_mean(vc20) == R(2.55)
    assert aa.distribution_quantile(vc20, 0.25) == R(1.35)
    assert aa.distribution_quantile(vc20, 0.50) == R(1.95)
    assert aa.distribution_quantile(vc20, 0.75) == R(3.65)
    assert aa.distribution_quantile(vc20, 0.90) == R(4.65)
    assert round(aa.prob_below(vc20, 1.0), 3) == 0.106
    assert round(aa.prob_below(vc20, 2.55), 3) == 0.619
    # number of compositions enumerated: C(24, 4)
    assert math.comb(24, 4) == 10_626


def test_example_19_1_tail_and_annualized():
    assert round(0.98 ** 20, 3) == 0.668
    assert round((2.55 - 1.0) / 0.98, 2) == 1.58
    assert round(2.55 ** (1 / 8) - 1, 4) == 0.1241
    assert round(1.95 ** (1 / 8) - 1, 4) == 0.0871


def test_example_19_1_median_rises_with_n():
    meds = {n: aa.distribution_quantile(aa.portfolio_multiple_distribution(VC_M, VC_P, n), 0.5)
            for n in (5, 10, 40)}
    assert meds[5] == R(1.40)
    assert meds[10] == R(1.70)
    assert meds[40] == R(2.425)


def test_enumeration_matches_binomial_tail(vc20):
    """Independent route: P(fund multiple < 2.5) must exceed P(no 50x) only partly;
    check P(no 50x) by summing enumerated outcomes conditional structure."""
    # Every fund with at least one 50x has multiple >= 50/20 = 2.5
    p_ge = sum(p for x, p in vc20 if x >= 2.5 - 1e-12)
    assert p_ge >= 1 - 0.98 ** 20 - 1e-12


# --------------------------------------------------------------------------
# Example 19.2 — J-curve, multiples, IRR
# --------------------------------------------------------------------------
C = [25, 25, 20, 15, 5, 0, 0, 0, 0]
D = [0, 0, 0, 5, 15, 30, 40, 45, 25]
IDX = [100, 112, 105, 120, 135, 128, 150, 165, 160]


def test_example_19_2():
    nf = aa.net_flows(C, D)
    assert nf == [-25, -25, -20, -10, 10, 30, 40, 45, 25]
    cum, s = [], 0
    for x in nf:
        s += x
        cum.append(s)
    assert cum == [-25, -50, -70, -80, -70, -40, 0, 45, 70]
    m2 = aa.fund_multiples(C[:3], D[:3], 62)
    assert (m2["dpi"], round(m2["rvpi"], 3), round(m2["tvpi"], 3)) == (0.0, 0.886, 0.886)
    assert round(tvm.irr(aa.net_flows(C[:3], D[:3], 62)), 4) == -0.1108
    m4 = aa.fund_multiples(C[:5], D[:5], 95)
    assert round(m4["dpi"], 3) == 0.222 and round(m4["rvpi"], 3) == 1.056 and round(m4["tvpi"], 3) == 1.278
    assert round(m4["rvpi"] / m4["tvpi"], 2) == 0.83
    assert round(tvm.irr(aa.net_flows(C[:5], D[:5], 95)), 4) == 0.0997
    mf = aa.fund_multiples(C, D)
    assert round(mf["tvpi"], 3) == 1.778 and mf["dpi"] == mf["tvpi"]
    assert round(tvm.irr(nf), 4) == 0.1314
    # netting calls and distributions within a year overstates the multiple
    assert tvm.equity_multiple(nf) == R(150 / 80)
    assert round(tvm.equity_multiple(nf), 3) == 1.875


# --------------------------------------------------------------------------
# Example 19.3 — KS-PME
# --------------------------------------------------------------------------

def test_example_19_3():
    pv_c = sum(c * 100 / i for c, i in zip(C, IDX))
    pv_d = sum(d * 100 / i for d, i in zip(D, IDX))
    assert round(pv_c, 3) == 82.573
    assert round(pv_d, 3) == 108.280
    ks = aa.ks_pme(C, D, IDX)
    assert round(ks, 3) == 1.311
    # forward-compounding route gives the same ratio
    fv_c = sum(c * IDX[-1] / i for c, i in zip(C, IDX))
    fv_d = sum(d * IDX[-1] / i for d, i in zip(D, IDX))
    assert fv_d / fv_c == R(ks)
    assert round((160 / 100) ** (1 / 8) - 1, 4) == 0.0605
    assert round(aa.pme_terminal_value(C, D, IDX), 1) == -41.1
    alt = [100, 115, 130, 140, 160, 175, 190, 205, 215]
    assert round(aa.ks_pme(C, D, alt), 3) == 1.115


def test_ks_pme_flat_index_equals_tvpi():
    assert aa.ks_pme(C, D, [100] * 9) == R(aa.fund_multiples(C, D)["tvpi"])


# --------------------------------------------------------------------------
# Example 19.4 — Unsmoothing, stale NAV, liquidity adjustment
# --------------------------------------------------------------------------
RS = [0.09, 0.11, 0.10, 0.06, -0.01, 0.02, 0.08]


def test_example_19_4():
    u = ms.geltner_unsmooth(RS, 0.5)
    assert [round(x, 4) for x in u] == [0.13, 0.09, 0.02, -0.08, 0.05, 0.14]
    obs = RS[1:]
    assert stats.mean(obs) == R(0.06)
    assert round(stats.stdev(obs), 4) == 0.0469
    assert round(stats.mean(u), 4) == 0.0583
    assert round(stats.stdev(u), 4) == 0.0818
    sh_rep = (stats.mean(obs) - 0.03) / stats.stdev(obs)
    sh_un = (stats.mean(u) - 0.03) / stats.stdev(u)
    assert round(sh_rep, 2) == 0.64 and round(sh_un, 2) == 0.35
    assert round(stats.stdev(u) / stats.stdev(obs), 2) == 1.74
    assert round(1 / ms.smoothing_vol_ratio(0.5), 2) == 1.73
    # end-point identity
    assert sum(obs) == R(0.36)
    assert sum(u) == R(0.35)
    assert sum(u) == R(sum(obs) + 0.5 / 0.5 * (RS[-1] - RS[0]))
    assert round(ms.cumulative_return(obs), 3) == 0.411
    assert round(ms.cumulative_return(u), 3) == 0.384
    # re-smoothing recovers the reported series (independent route)
    assert ms.smooth(u, 0.5, RS[0]) == R(obs)
    v = aa.stale_nav_correction(100, 1.2, -0.20)
    assert v == R(76.0)
    assert round(85 / v - 1, 3) == 0.118
    la = aa.liquidity_adjusted_return(0.09, 0.25, 0.20, 5)
    assert round(0.95 ** 0.2, 5) == 0.98979
    assert round(la, 4) == 0.0789
    assert round(0.09 - la, 3) == 0.011


# --------------------------------------------------------------------------
# Example 19.5 — Art transaction-cost hurdle
# --------------------------------------------------------------------------
TIERS = [(1_000_000, 0.27), (8_000_000, 0.22), (math.inf, 0.15)]


def test_example_19_5():
    h0 = 2_000_000
    bp = aa.tiered_premium(h0, TIERS)
    assert bp == R(490_000)
    paid = h0 + bp
    assert paid == R(2_490_000)
    assert bp / h0 == R(0.245)
    rt = 1 - h0 * 0.89 / paid
    assert round(rt, 3) == 0.285
    assert ms.round_trip_cost(0.245, 0.11) == R(rt)
    m = 0.006 * paid
    assert m == R(14_940)
    h_be = (paid + 5 * m) / 0.89
    assert round(h_be) == 2_881_685
    assert round((h_be / h0) ** 0.2 - 1, 4) == 0.0758
    fv_paid = paid * 1.07 ** 5
    fv_m = sum(m * 1.07 ** (5 - t) for t in range(1, 6))
    assert round(fv_paid) == 3_492_354
    assert round(fv_m) == 85_916
    h_k = (fv_paid + fv_m) / 0.89
    assert round(h_k) == 4_020_528
    assert round((h_k / h0) ** 0.2 - 1, 4) == 0.1499
    h5 = h0 * 1.05 ** 5
    assert round(h5) == 2_552_563
    assert round(h5 * 0.89) == 2_271_781
    flows = [-paid] + [-m] * 4 + [h5 * 0.89 - m]
    assert round(tvm.irr(flows), 4) == -0.0244
    # NPV at 7% of the k-hurdle flows is zero (independent check)
    flows_k = [-paid] + [-m] * 4 + [h_k * 0.89 - m]
    assert tvm.npv(0.07, flows_k) == R(0.0, abs=1e-6)


def test_tiered_premium_boundaries():
    assert aa.tiered_premium(0, TIERS) == 0
    assert aa.tiered_premium(1_000_000, TIERS) == R(270_000)
    assert aa.tiered_premium(10_000_000, TIERS) == R(270_000 + 0.22 * 7_000_000 + 0.15 * 2_000_000)


# --------------------------------------------------------------------------
# Example 19.6 — Repeat sales and selection
# --------------------------------------------------------------------------

def test_example_19_6():
    pairs = [(0, 1, 0.10), (0, 2, 0.25), (1, 2, 0.12), (0, 1, 0.06), (1, 2, 0.20), (0, 2, 0.15)]
    r = aa.repeat_sales_3period(pairs)
    assert round(r["beta"][1], 4) == 0.0667
    assert round(r["beta"][2], 4) == 0.2133
    assert [round(x, 1) for x in r["index"]] == [100.0, 106.9, 123.8]
    # residuals orthogonal to regressors (independent OLS check)
    b = r["beta"]
    res = [(s, bu, y - (b[s] - b[bu])) for bu, s, y in pairs]
    for k in (1, 2):
        assert sum(((1 if s == k else 0) - (1 if bu == k else 0)) * e for s, bu, e in res) == R(0, abs=1e-12)
    pop = [-0.30, -0.20, -0.10, 0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40]
    mask = [True, False, False, False, False, True, True, True, True, True]
    sb = ms.selection_bias(pop, mask)
    assert sb["population_mean"] == R(0.06)
    assert round(sb["traded_mean"], 3) == 0.142
    assert round(sb["bias"], 3) == 0.082


# --------------------------------------------------------------------------
# Example 19.7 — Resale-only valuation
# --------------------------------------------------------------------------

def test_example_19_7():
    e = 0.5 * 150 + 0.35 * 60 + 0.15 * 5
    assert e == R(96.75)
    assert 1.15 ** 3 == R(1.520875)
    v = aa.resale_only_value([150, 60, 5], [0.5, 0.35, 0.15], 0.15, 3)
    assert round(v, 2) == 63.61
    v25 = aa.resale_only_value([150, 60, 5], [0.5, 0.35, 0.15], 0.25, 3)
    assert round(v25, 2) == 49.54
    assert round(v25 / v - 1, 2) == -0.22
    vs = aa.resale_only_value([150, 60, 5], [0.40, 0.35, 0.25], 0.15, 3)
    assert round(vs, 2) == 54.08
    assert round(vs / v - 1, 2) == -0.15
    assert [round(aa.required_price_path(80, 0.15, t), 2) for t in (3, 10, 20)] == [121.67, 323.64, 1309.32]
    assert cre.direct_cap_value(6.0, 0.06) == R(100.0)
    assert round(cre.direct_cap_value(6.0, 0.065), 2) == 92.31
    assert round(cre.cap_rate_shock_pct(0.06, 0.065), 3) == -0.077


# --------------------------------------------------------------------------
# Example 19.8 — Development land
# --------------------------------------------------------------------------

def test_example_19_8():
    r = cre.residual_land_value(60e6, 38e6, 6e6, 3e6, 0.15, 0.02)
    assert r["net_value"] == R(58.8e6)
    assert round(r["land_value"] / 1e6, 3) == 4.130
    r2 = cre.residual_land_value(57e6, 38e6, 6e6, 3e6, 0.15, 0.02)
    assert round(r2["land_value"] / 1e6, 3) == 1.574
    assert round(r2["land_value"] / r["land_value"] - 1, 3) == -0.619
    assert round((r2["land_value"] / r["land_value"] - 1) / -0.05, 1) == 12.4
    ev = 0.6 * r["land_value"] + 0.4 * 1.5e6
    assert round(ev / 1e6, 3) == 3.078
    ann = sum(1 / 1.12 ** t for t in (1, 2, 3))
    assert round(ev / 1.12 ** 3 / 1e6, 3) == 2.191
    assert round(37_500 * ann / 1e6, 3) == 0.090
    pv = ev / 1.12 ** 3 - 37_500 * ann
    assert round(pv / 1e6, 3) == 2.101
    fv_carry = sum(37_500 * 1.12 ** (3 - t) for t in (1, 2, 3))
    assert round(fv_carry / 1e6, 3) == 0.127
    assert round(2.5 * 1.12 ** 3, 3) == 3.512
    p_star = (2.5e6 * 1.12 ** 3 + fv_carry - 1.5e6) / (r["land_value"] - 1.5e6)
    assert round(p_star, 3) == 0.813
    ev2 = 0.6 * r2["land_value"] + 0.4 * 1.5e6
    assert round((ev2 / 1.12 ** 3 - 37_500 * ann) / 1e6, 3) == 1.009


# --------------------------------------------------------------------------
# Example 19.9 — Scored framework
# --------------------------------------------------------------------------
SCORES = {
    "Core CRE": [4, 4, 5, 2, 5, 3, 3, 3, 3],
    "Development land": [1, 3, 2, 1, 5, 2, 2, 2, 2],
    "PE buyout LP interest": [3, 3, 2, 1, 4, 2, 2, 3, 3],
    "VC LP interest": [1, 2, 1, 1, 4, 1, 2, 2, 2],
    "Bitcoin": [1, 1, 3, 5, 3, 3, 5, 1, 1],
    "Other tokens and NFTs": [1, 1, 1, 2, 2, 2, 3, 1, 1],
    "Fine art": [1, 2, 2, 1, 4, 1, 1, 3, 2],
    "Compliance allowances": [1, 3, 3, 4, 4, 4, 4, 3, 2],
    "Voluntary offsets": [1, 1, 1, 2, 2, 1, 2, 2, 1],
}
EXPECTED = {  # composite, weakest, L1 from CRE, anchor sub-score
    "Core CRE": (32, 2, 0, 14),
    "Compliance allowances": (28, 1, 12, 9),
    "PE buyout LP interest": (23, 1, 9, 12),
    "Bitcoin": (23, 1, 19, 4),
    "Development land": (20, 1, 12, 8),
    "Fine art": (17, 1, 15, 8),
    "VC LP interest": (16, 1, 16, 7),
    "Other tokens and NFTs": (14, 1, 18, 4),
    "Voluntary offsets": (13, 1, 19, 5),
}


def _l1(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))


def test_example_19_9():
    cre_s = SCORES["Core CRE"]
    for k, v in SCORES.items():
        assert len(v) == 9 and all(1 <= s <= 5 for s in v)
        anchor = v[0] + v[1] + v[7] + v[8]
        assert (sum(v), min(v), _l1(v, cre_s), anchor) == EXPECTED[k], k
    assert _l1(SCORES["PE buyout LP interest"], SCORES["Bitcoin"]) == 18
    # ranking order in the solution table is by composite (ties allowed)
    comps = [EXPECTED[k][0] for k in EXPECTED]
    assert comps == sorted(comps, reverse=True)


# --------------------------------------------------------------------------
# §19.9 historical arithmetic
# --------------------------------------------------------------------------

def test_section_19_9():
    assert round(15_800 / 69_000 - 1, 3) == -0.771
    assert 3.66 + 2.16 == R(5.82)


# --------------------------------------------------------------------------
# Problems
# --------------------------------------------------------------------------

def test_problem_19_2():
    m = aa.fund_multiples([60], [18], 66)
    assert (round(m["dpi"], 2), round(m["rvpi"], 2), round(m["tvpi"], 2)) == (0.30, 1.10, 1.40)
    assert round(m["rvpi"] / m["tvpi"], 3) == 0.786


def test_problem_19_3():
    rt = ms.round_trip_cost(0.27, 0.10)
    assert rt == R(1 - 450_000 / 635_000)
    assert round(rt, 4) == 0.2913
    assert round(ms.annualized_cost_drag(rt, 4), 4) == 0.0825


def test_problem_19_4():
    c = [40, 30, 30, 0, 0, 0]
    d = [0, 0, 20, 50, 40, 30]
    idx = [100, 90, 95, 110, 120, 130]
    m = aa.fund_multiples(c, d)
    assert m["tvpi"] == R(1.40)
    assert aa.net_flows(c, d) == [-40, -30, -10, 50, 40, 30]
    assert round(tvm.irr(aa.net_flows(c, d)), 4) == 0.1352
    assert round(sum(x * 100 / i for x, i in zip(c, idx)), 3) == 104.912
    assert round(sum(x * 100 / i for x, i in zip(d, idx)), 3) == 122.917
    assert round(aa.ks_pme(c, d, idx), 3) == 1.172
    assert aa.ks_pme(c, d, [100] * 6) == R(1.40)
    assert round((130 / 100) ** 0.2 - 1, 4) == 0.0539
    assert round(aa.pme_terminal_value(c, d, idx), 1) == -23.4


def test_problem_19_5():
    rs = [0.04, 0.07, 0.06, 0.01, -0.03, 0.02]
    u = ms.geltner_unsmooth(rs, 0.6)
    assert [round(x, 4) for x in u] == [0.115, 0.045, -0.065, -0.09, 0.095]
    assert round(stats.stdev(rs[1:]), 4) == 0.0404
    assert round(stats.stdev(u), 4) == 0.0930
    assert ms.smoothing_vol_ratio(0.6) == R(0.5)
    assert round(stats.stdev(u) / stats.stdev(rs[1:]), 2) == 2.30
    assert sum(rs[1:]) == R(0.13) and sum(u) == R(0.10)
    assert sum(u) == R(sum(rs[1:]) + 0.6 / 0.4 * (rs[-1] - rs[0]))
    assert round(ms.cumulative_return(rs[1:]), 4) == 0.1334
    assert round(ms.cumulative_return(u), 4) == 0.0856
    v = aa.stale_nav_correction(50, 1.3, -0.15)
    assert v == R(40.25)
    assert round(0.88 * 50 / v - 1, 3) == 0.093


def test_problem_19_6():
    m = [0, 1, 4, 20, 100]
    p = [0.5, 0.3, 0.15, 0.04, 0.01]
    mu = sum(a * b for a, b in zip(m, p))
    assert mu == R(2.70)
    assert round(1.0 / mu, 3) == 0.370
    assert round(0.99 ** 25, 3) == 0.778
    assert round((mu - 1.0) / 0.99, 2) == 1.72
    d25 = aa.portfolio_multiple_distribution(m, p, 25)
    assert aa.distribution_mean(d25) == R(2.70)
    assert aa.distribution_quantile(d25, 0.5) == R(1.88)
    assert round(aa.prob_below(d25, 1.0), 3) == 0.157
    assert round(0.99 ** 100, 3) == 0.366


def test_problem_19_6_n100():
    d100 = aa.portfolio_multiple_distribution([0, 1, 4, 20, 100], [0.5, 0.3, 0.15, 0.04, 0.01], 100)
    assert aa.distribution_quantile(d100, 0.5) == R(2.56)


def test_problem_19_7():
    pairs = [(0, 1, 0.05), (0, 1, 0.09), (1, 2, -0.04), (0, 2, 0.02), (1, 2, 0.00), (0, 2, 0.08)]
    r = aa.repeat_sales_3period(pairs)
    assert r["beta"][1] == R(0.07) and r["beta"][2] == R(0.05)
    assert [round(x, 2) for x in r["index"]] == [100.0, 107.25, 105.13]
    sb = ms.selection_bias([-0.25, -0.15, -0.05, 0.0, 0.05, 0.10, 0.20, 0.35],
                           [False, False, False, False, True, True, True, True])
    assert sb["population_mean"] == R(0.03125)
    assert sb["traded_mean"] == R(0.175)
    assert round(sb["bias"], 3) == 0.144


def test_problem_19_8():
    call2 = 25 * 1.07 ** 2 + 25 * 1.07
    assert call2 == R(55.3725)
    c1 = [0, 0, 20 + call2, 15, 5, 0, 0, 0, 0]
    m = aa.fund_multiples(c1, D)
    assert round(m["paid_in"], 2) == 95.37
    assert round(m["tvpi"], 3) == 1.678
    irr1 = tvm.irr(aa.net_flows(c1, D))
    assert round(irr1, 4) == 0.1475
    irr0 = tvm.irr(aa.net_flows(C, D))
    assert round((irr1 - irr0) * 1e4) == 161  # "about 160 bp"
    assert round(sum(D) - sum(c1), 2) == 64.63
    assert round((sum(D) - sum(C)) - (sum(D) - sum(c1)), 2) == 5.37


def test_problem_19_9():
    v = aa.resale_only_value([150, 60, 5], [0.5, 0.35, 0.15], 0.15, 3)
    assert round((96.75 / 80) ** (1 / 3) - 1, 4) == 0.0654
    assert round(80 / v - 1, 2) == 0.26


def test_problem_19_10():
    assets = 40 * (1 - 0.30) + 25 * (1 - 0.80) + 35
    assert assets == R(68.0)
    assert 100 - assets == R(32.0)


# --------------------------------------------------------------------------
# Library boundary cases
# --------------------------------------------------------------------------

def test_library_boundaries():
    with pytest.raises(ValueError):
        aa.fund_multiples([0], [10])
    with pytest.raises(ValueError):
        aa.portfolio_multiple_distribution([0, 1], [0.5, 0.6], 3)
    # single deal: distribution equals the deal distribution
    d1 = aa.portfolio_multiple_distribution(VC_M, VC_P, 1)
    assert [x for x, _ in d1] == VC_M and [p for _, p in d1] == R(VC_P)
    # zero haircut: no liquidity adjustment
    assert aa.liquidity_adjusted_return(0.08, 0.3, 0.0, 5) == R(0.08)
    # 100% forced sale at 100% haircut: total loss
    assert aa.liquidity_adjusted_return(0.08, 1.0, 1.0, 5) == R(-1.0)
    with pytest.raises(ValueError):
        aa.repeat_sales_3period([(0, 1, 0.1), (0, 1, 0.2)])
