"""Reproduces every number in Chapter 9 text, problems, and solutions."""

import math

import pytest

from sdesk import cre, tvm

R = pytest.approx


def _bisect(f, lo, hi, n=200):
    """Root of a decreasing-or-increasing f on [lo, hi] with a sign change."""
    flo = f(lo)
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if flo * fm <= 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


# --------------------------------------------------------------- Example 9.1

def test_example_9_1():
    vals = [cre.direct_cap_value(n, 0.055) for n in (2_610_000, 2_880_000, 3_060_000)]
    assert [round(v) for v in vals] == [47_454_545, 52_363_636, 55_636_364]
    assert round(vals[2] - 385_000) == 55_251_364
    assert 310_000 + 75_000 == 385_000
    assert round(vals[2] - vals[0], -4) == 8_180_000
    assert round((vals[2] - vals[0]) / vals[2], 3) == 0.147
    # discounting the stabilization cost over 9 months at 7% changes it by ~ $19k
    assert round(385_000 - 385_000 / 1.07 ** 0.75, -3) == 19_000
    assert 3_060_000 / vals[2] == R(0.055)


# --------------------------------------------------------------- Example 9.2

def test_example_9_2():
    assert 0.02 * 26_000_000 == R(520_000)
    n = 3_060_000 + 520_000
    t = 0.02 * 0.90
    assert t == R(0.018)
    v = cre.loaded_cap_value(n, 0.055, t)
    assert round(v) == 49_041_096
    # independent route: V = (N - tV)/c solved by fixed-point iteration
    x = 40_000_000.0
    for _ in range(200):          # contraction with factor t/c = 0.327
        x = (n - t * x) / 0.055
    assert x == R(v)
    assert round(t * v) == 882_740
    assert round(n - t * v) == 2_697_260
    assert (n - t * v) / v == R(0.055)
    err = cre.direct_cap_value(3_060_000, 0.055) - v
    assert round(err) == 6_595_268
    assert round(err / v, 3) == 0.134


# --------------------------------------------------------------- Example 9.3

NOI_93 = [3_400_000, 2_300_000, 2_850_000, 3_300_000, 3_400_000, 3_500_000]
CAP_93 = [250_000, 3_550_000, 450_000, 300_000, 350_000]
CF_93 = [n - c for n, c in zip(NOI_93[:5], CAP_93)]


def test_example_9_3():
    assert CF_93 == [3_150_000, -1_250_000, 2_400_000, 3_000_000, 3_050_000]
    d = cre.dcf_value(CF_93, NOI_93[5], 0.0825, 0.09, 0.02)
    assert round(d["gross_reversion"]) == 42_424_242
    assert round(d["net_reversion"]) == 41_575_758
    assert round(d["pv_reversion"]) == 27_021_390
    assert round(d["value"]) == 34_820_005
    assert round(d["reversion_share"], 3) == 0.776
    assert round(d["value"] - d["pv_reversion"]) == 7_798_615
    # discount factors and PVs table
    dfs = [round(1 / 1.09 ** t, 6) for t in range(1, 6)]
    assert dfs == [0.917431, 0.84168, 0.772183, 0.708425, 0.649931]
    pvs = [round(c / 1.09 ** t) for t, c in enumerate(CF_93, 1)]
    assert pvs == [2_889_908, -1_052_100, 1_853_240, 2_125_276, 1_982_291]
    assert sum(pvs) + 27_021_390 == R(34_820_005, abs=2)
    # TI check: $55/sf on 49,500 sf
    assert 55 * 49_500 == 2_722_500
    assert round(NOI_93[0] / d["value"], 4) == 0.0976
    assert round(d["value"] / 165_000) == 211
    ask = 3_400_000 / 0.07
    assert round(ask) == 48_571_429
    flows = [-ask] + CF_93[:4] + [CF_93[4] + d["net_reversion"]]
    assert round(tvm.irr(flows), 4) == 0.0144
    c_ask = _bisect(lambda c: cre.dcf_value(CF_93, NOI_93[5], c, 0.09, 0.02)["value"] - ask, 0.03, 0.12)
    assert round(c_ask, 4) == 0.0547
    d5 = cre.dcf_value(CF_93, NOI_93[4], 0.0825, 0.09, 0.02)
    assert round(d5["value"]) == 34_047_965
    assert round(d["value"] - d5["value"]) == 772_040
    assert round(NOI_93[5] / NOI_93[4] - 1, 3) == 0.029
    assert round(1 - d["value"] / ask, 2) == 0.28


# --------------------------------------------------------------- Example 9.4

def test_example_9_4():
    rows = [(0.09, 0.07, 0.15, 0.0595, 0.0305), (0.075, 0.0525, 0.05, 0.0499, 0.0251),
            (0.0725, 0.055, 0.08, 0.0506, 0.0219)]
    for k, c, kap, net, g in rows:
        assert round(c * (1 - kap), 4) == net
        gi = k - c * (1 - kap)
        assert round(gi, 4) == g
        # reverse: the gordon cap rate grossed up for capex reproduces the market cap
        assert cre.gordon_cap_rate(k, gi) / (1 - kap) == R(c)
    assert round(0.07 * 0.85 + 0.01, 4) == 0.0695
    assert round((0.09 - 0.01) / 0.85, 4) == 0.0941


# --------------------------------------------------------------- Example 9.5

def test_example_9_5():
    c0 = cre.gordon_cap_rate(0.08, 0.025) / 0.90
    c10 = cre.gordon_cap_rate(0.08, 0.02) / 0.85
    assert round(c0, 4) == 0.0611
    assert round(c10, 4) == 0.0706
    assert round((c10 - c0) * 1e4) == 95


# --------------------------------------------------------------- Example 9.6

COMPS_96 = {"A": (142, [-0.02, 0, 0.05, 0, 0]), "B": (165, [-0.14, -0.05, -0.05, 0, 0]),
            "C": (128, [-0.01, 0.05, 0.10, 0.08, 0]), "D": (150, [-0.06, 0, 0, 0, -0.07])}


def _grid(comps):
    adj, w = {}, {}
    for k, (p, a) in comps.items():
        f = math.prod(1 + x for x in a)
        adj[k] = (f, p * f)
        w[k] = 1 / sum(abs(x) for x in a)
    tot = sum(w.values())
    return adj, {k: v / tot for k, v in w.items()}


def test_example_9_6():
    adj, w = _grid(COMPS_96)
    assert {k: round(v[0], 4) for k, v in adj.items()} == {"A": 1.029, "B": 0.7761, "C": 1.2349, "D": 0.8742}
    assert {k: round(v[1], 2) for k, v in adj.items()} == {"A": 146.12, "B": 128.06, "C": 158.07, "D": 131.13}
    assert {k: round(v, 3) for k, v in w.items()} == {"A": 0.471, "B": 0.137, "C": 0.137, "D": 0.254}
    ind = sum(adj[k][1] * w[k] for k in adj)
    assert round(ind, 2) == 141.48
    assert round(ind * 120_000) == 16_977_094
    assert round(sum(v[1] for v in adj.values()) / 4, 2) == 140.85
    assert round(165 * 0.95 * 0.95, 2) == 148.91
    assert round(148.91 / 128.06 - 1, 2) == 0.16
    assert round(128.06 * 120_000 / 1e6, 1) == 15.4
    assert round(158.07 * 120_000 / 1e6, 1) == 19.0


# --------------------------------------------------------------- Example 9.7

def test_example_9_7():
    exp = {0.0525: (30_476_190, 30_019_048, 3_563_520), 0.0575: (27_826_087, 27_408_696, 1_293_648),
           0.0625: (25_600_000, 25_216_000, -613_043)}
    for c, (gdv, net, land) in exp.items():
        g = 1_600_000 / c
        r = cre.residual_land_value(g, 18_000_000, 3_240_000, 1_300_000, 0.15, 0.015)
        assert (round(g), round(r["net_value"]), round(r["land_value"])) == (gdv, net, land)
        # independent check: margin on total cost is exactly 15% at the residual land price
        assert r["net_value"] / r["total_cost"] - 1 == R(0.15)
    assert 0.18 * 18_000_000 == R(3_240_000)
    r = cre.residual_land_value(1_600_000 / 0.0575, 18_000_000, 3_240_000, 1_300_000, 0.15, 0.015)
    assert round(r["net_value"] / 1.15) == 23_833_648
    cost = 22_540_000 + 2_500_000
    assert cost == 25_040_000 and cost / 200_000 == R(125.20)
    assert round(r["net_value"] / cost - 1, 4) == 0.0946
    assert round(1_600_000 / cost, 4) == 0.0639
    assert round((1_600_000 / 0.0575) / cost, 2) == 1.11
    assert round(1.15 / 0.985, 2) == 1.17
    assert round(1_600_000 / 0.0525 - 1_600_000 / 0.0625) == 4_876_190
    assert round((1_600_000 / 0.0525 - 1_600_000 / 0.0625) / (1_600_000 / 0.0575), 3) == 0.175
    assert round(1.15 * cost) == 28_796_000
    assert round(1.15 * cost / r["net_value"] - 1, 3) == 0.051


# --------------------------------------------------------------- Examples 9.8 and 9.9

def _ind(g=0.03, exit_cap=0.06, rate=0.0625):
    noi = [1_400_000 * (1 + g) ** t for t in range(6)]
    cf = [n * 0.95 for n in noi[:5]]
    gross = noi[5] / exit_cap
    net = gross * 0.985
    prop = [-25_000_000 * 1.01] + cf[:4] + [cf[4] + net]
    loan = 15_000_000
    ds = tvm.annual_debt_service(loan, rate, 30)
    bal = tvm.loan_balance(loan, rate, 30, 60)
    eq = [prop[0] + loan] + [c - ds for c in cf[:4]] + [cf[4] - ds + net - bal]
    return {"noi": noi, "cf": cf, "gross": gross, "net": net, "prop": prop, "ds": ds, "bal": bal, "eq": eq}


def test_example_9_8():
    x = _ind()
    assert [round(n) for n in x["noi"]] == [1_400_000, 1_442_000, 1_485_260, 1_529_818, 1_575_712, 1_622_984]
    assert [round(c) for c in x["cf"]] == [1_330_000, 1_369_900, 1_410_997, 1_453_327, 1_496_927]
    assert round(x["gross"]) == 27_049_728 and round(x["net"]) == 26_643_982
    assert round(x["prop"][-1]) == 28_140_909
    assert round(tvm.irr(x["prop"]), 4) == 0.0654
    assert round(tvm.equity_multiple(x["prop"]), 2) == 1.33
    assert round(x["ds"]) == 1_108_291
    assert round(x["ds"] / 15_000_000, 4) == 0.0739
    assert round(x["bal"]) == 14_000_586
    # independent balance check: PV of the remaining 300 payments at the loan rate
    pmt = tvm.payment(15_000_000, 0.0625, 30)
    assert pmt * tvm.annuity_factor(0.0625 / 12, 300) == R(x["bal"], abs=0.01)
    assert round(1_400_000 / x["ds"], 2) == 1.26
    assert round(1_400_000 / 15_000_000, 4) == 0.0933
    assert [round(e) for e in x["eq"]] == [-10_250_000, 221_709, 261_609, 302_706, 345_036, 13_032_032]
    assert round(tvm.irr(x["eq"]), 4) == 0.0697
    assert round(tvm.equity_multiple(x["eq"]), 2) == 1.38
    assert round(x["eq"][1] / 10_250_000, 4) == 0.0216
    assert round(1_330_000 / 25_250_000, 4) == 0.0527
    assert round((tvm.irr(x["eq"]) - tvm.irr(x["prop"])) * 1e4) == 43
    y = _ind(rate=0.05)
    assert round(y["ds"] / 15_000_000, 4) == 0.0644
    assert round(tvm.irr(y["eq"]), 4) == 0.0859


PROP_GRID = {0.01: [6.14, 5.34, 4.58, 3.86, 3.18], 0.02: [7.14, 6.33, 5.56, 4.83, 4.14],
             0.03: [8.14, 7.32, 6.54, 5.81, 5.11], 0.04: [9.14, 8.31, 7.52, 6.78, 6.07]}
EQ_GRID = {0.01: [6.04, 4.13, 2.24, 0.37, -1.50], 0.02: [8.32, 6.48, 4.67, 2.88, 1.11],
           0.03: [10.50, 8.72, 6.97, 5.26, 3.56], 0.04: [12.60, 10.87, 9.18, 7.52, 5.89]}
CAPS = [0.055, 0.0575, 0.06, 0.0625, 0.065]


def test_example_9_9():
    for g in PROP_GRID:
        assert [round(100 * tvm.irr(_ind(g, c)["prop"]), 2) for c in CAPS] == PROP_GRID[g]
        assert [round(100 * tvm.irr(_ind(g, c)["eq"]), 2) for c in CAPS] == EQ_GRID[g]
    be = _bisect(lambda c: tvm.irr(_ind(0.03, c)["prop"]) - 0.07, 0.04, 0.09)
    assert round(be, 4) == 0.0585
    assert round((0.06 - be) * 1e4) == 15
    # one cell toward the lower right
    assert round(PROP_GRID[0.03][2] - PROP_GRID[0.02][3], 2) == 1.71
    assert round(EQ_GRID[0.03][2] - EQ_GRID[0.02][3], 2) == 4.09
    assert round(EQ_GRID[0.03][1] - EQ_GRID[0.02][2], 2) == 4.05
    # rule of thumb in the reference sheet: 100 bp exit cap ~ 300 bp property IRR
    assert round(PROP_GRID[0.03][0] - PROP_GRID[0.03][4], 2) == 3.03


# --------------------------------------------------------------- Example 9.10

def _va(g, va, exit_cap, price=40_000_000, n1=2_000_000, uplift=450_000, capex=3_000_000,
        uplift_year=2, capex_year=1):
    noi = []
    for t in range(1, 7):
        base = n1 * (1 + g) ** (t - 1)
        up = uplift * (1 + g) ** (t - uplift_year) if (va and t >= uplift_year) else 0.0
        noi.append(base + up)
    cf = list(noi[:5])
    if va:
        cf[capex_year - 1] -= capex
    rev = noi[5] / exit_cap
    return [-price] + cf[:4] + [cf[4] + rev], noi, rev


def test_example_9_10():
    steps = [(0.0, False, 0.05, 2_000_000, 40_000_000, 0.0500),
             (0.03, False, 0.05, 2_318_548, 46_370_963, 0.0800),
             (0.03, True, 0.05, 2_825_027, 56_500_542, 0.1096),
             (0.03, True, 0.0475, 2_825_027, 59_474_255, 0.1197)]
    irrs = []
    for g, va, c, n6, rev, irr in steps:
        f, noi, rv = _va(g, va, c)
        assert round(noi[5]) == n6 and round(rv) == rev
        irrs.append(tvm.irr(f))
        assert round(irrs[-1], 4) == irr
    inc = [round(100 * (b - a), 2) for a, b in zip([0.0] + irrs[:-1], irrs)]
    assert inc == [5.00, 3.00, 2.96, 1.00]
    # identity IRR = c + g (section 9.4.5), for several hold periods implicitly via n=5
    assert irrs[1] == R(0.08, abs=1e-9)
    assert 450_000 / 3_000_000 == R(0.15)
    assert 450_000 / 0.05 - 3_000_000 == R(6_000_000)
    f, _, _ = _va(0.03, False, 0.0475)
    assert round(tvm.irr(f), 4) == 0.0897
    assert round(100 * (tvm.irr(f) - 0.08), 2) == 0.97


def test_irr_identity_other_holds():
    """Section 9.4.5: IRR = c + g for any hold with flat cap, no capex, no costs."""
    for n, c, g in [(3, 0.06, 0.02), (10, 0.045, 0.035), (7, 0.08, 0.0)]:
        flows = [-1.0 / c] + [(1 + g) ** (t - 1) for t in range(1, n)] + [(1 + g) ** (n - 1) + (1 + g) ** n / c]
        assert tvm.irr(flows) == R(c + g, abs=1e-9)


# --------------------------------------------------------------- Example 9.11

def test_example_9_11():
    assert round(2_418_000 / 62_000_000, 4) == 0.039
    v = cre.direct_cap_value(2_650_000, 0.056)
    assert round(v) == 47_321_429
    assert round(62_000_000 - v) == 14_678_571
    assert round(1 - v / 62_000_000, 3) == 0.237
    assert 62_000_000 - 40_300_000 == 21_700_000
    assert round(v - 40_300_000) == 7_021_429
    assert round(v * 0.98 - 40_300_000) == 6_075_000
    n6 = 62_000_000 * 0.056
    assert n6 == R(3_472_000)
    assert round((n6 / 2_650_000) ** 0.2 - 1, 4) == 0.0555
    n6b = 2_650_000 * 1.03 ** 5
    assert round(n6b) == 3_072_076
    assert round(n6b / 62_000_000, 4) == 0.0495
    f = [-v] + [2_650_000 * 1.03 ** t for t in range(4)] + [2_650_000 * 1.03 ** 4 + n6b / 0.056]
    assert tvm.irr(f) == R(0.086, abs=1e-9)
    intr = 0.065 * 40_300_000
    assert intr == R(2_619_500)
    eq = [-(v * 0.98 - 40_300_000)] + [2_650_000 * 1.03 ** t - intr for t in range(4)] + \
         [2_650_000 * 1.03 ** 4 - intr + n6b / 0.056 * 0.98 - 40_300_000]
    assert [round(x) for x in eq] == [-6_075_000, 30_500, 110_000, 191_885, 276_227, 13_824_434]
    assert round(tvm.irr(eq), 4) == 0.1929
    assert round(40_300_000 / v, 2) == 0.85


# --------------------------------------------------------------- Example 9.12

def test_example_9_12():
    a = 3_510_000 / 0.0675
    assert a == R(52_000_000)
    b = 3_400_000 / 0.0675
    c = 3_400_000 / 0.08
    d = cre.dcf_value(CF_93, NOI_93[5], 0.0825, 0.09, 0.02)["value"]
    assert (round(b), round(c)) == (50_370_370, 42_500_000)
    assert (round(a - b), round(b - c), round(c - d)) == (1_629_630, 7_870_370, 7_679_995)
    assert round(a - d) == 17_179_995
    assert round((a - d) / a, 3) == 0.330
    assert (a - b) / (a - d) < 0.10


# --------------------------------------------------------------- Example 9.13

def test_example_9_13():
    v = 1_710_000 / 0.0775
    assert round(v) == 22_064_516
    assert round(v / 95_000, 2) == 232.26
    rc = 310 * 95_000
    assert rc == 29_450_000
    assert round(1 - v / rc, 3) == 0.251
    need = rc * 1.15
    assert need == R(33_867_500)
    assert round(need * 0.0775) == 2_624_731
    assert round(need * 0.0775 / 95_000, 2) == 27.63
    assert round(need * 0.0775 / 1_710_000 - 1, 3) == 0.535
    assert 1_710_000 / 95_000 == R(18.0)
    assert 2026 - 1998 == 28


# --------------------------------------------------------------- Example 9.14

def test_example_9_14():
    alpha, a = 0.6, [100.0]
    for _ in range(4):
        a.append(alpha * a[-1] + (1 - alpha) * 75.0)
    assert [round(x, 2) for x in a] == [100.0, 90.0, 84.0, 80.4, 78.24]
    chg = [round(100 * (a[t] / a[t - 1] - 1), 1) for t in range(1, 5)]
    assert chg == [-10.0, -6.7, -4.3, -2.7]
    unsm = [(a[t] - alpha * a[t - 1]) / (1 - alpha) for t in range(1, 5)]
    assert unsm == [R(75.0)] * 4
    assert round((100 - a[3]) / 25, 3) == 0.784
    assert round((100 - a[4]) / 25, 3) == 0.870


# --------------------------------------------------------------- Section 9.9 arithmetic

def test_episode_arithmetic():
    assert round(5.53 - (-24.9), 2) == 30.43
    unlev = 0.65 * (-0.249) + 0.35 * 0.04
    assert round(unlev, 3) == -0.148
    assert round(100 * (0.0553 - unlev), 1) == 20.3
    assert round((0.0553 - unlev) / (0.0553 + 0.249), 2) == 0.67
    # NPI Q4 2022 components
    assert 0.95 - 4.45 == R(-3.50)
    assert 1.11 - 4.13 == R(-3.02)


# --------------------------------------------------------------- problems

def test_problem_9_2():
    assert 1_800_000 / 0.06 == R(30_000_000)
    v1 = 1_710_000 / 0.0675
    assert round(v1 / 1e6, 2) == 25.33
    assert round(0.95 * 6 / 6.75 - 1, 3) == -0.156
    v = cre.loaded_cap_value(2_200_000, 0.06, 0.015)
    assert round(v / 1e6, 2) == 29.33
    assert round(2_200_000 / 0.06 / 1e6, 2) == 36.67
    assert round((2_200_000 / 0.06 - v) / 1e6, 2) == 7.33
    assert round((2_200_000 / 0.06 - v) / v, 2) == 0.25


def test_problem_9_3():
    assert round(0.075 - 0.0525 * 0.9, 5) == 0.02775
    assert round(0.0525 * 0.9 + 0.02, 5) == 0.06725
    assert round(cre.gordon_cap_rate(0.075, 0.02) / 0.9, 4) == 0.0611


def test_problem_9_4():
    noi = [1_000_000 * 1.025 ** t for t in range(6)]
    cap = [0.03 * n for n in noi[:5]]
    cap[2] += 400_000
    cf = [n - c for n, c in zip(noi[:5], cap)]
    assert [round(n) for n in noi] == [1_000_000, 1_025_000, 1_050_625, 1_076_891, 1_103_813, 1_131_408]
    assert [round(c) for c in cap] == [30_000, 30_750, 431_519, 32_307, 33_114]
    assert [round(c) for c in cf] == [970_000, 994_250, 619_106, 1_044_584, 1_070_699]
    d = cre.dcf_value(cf, noi[5], 0.07, 0.085, 0.02)
    assert (round(d["gross_reversion"]), round(d["net_reversion"]), round(d["pv_reversion"])) == \
        (16_162_974, 15_839_715, 10_534_130)
    assert round(d["value"]) == 14_223_221
    assert round(d["reversion_share"], 3) == 0.741
    assert round(noi[0] / d["value"], 4) == 0.0703
    d5 = cre.dcf_value(cf, noi[4], 0.07, 0.085, 0.02)
    assert round(d5["value"]) == 13_966_291
    assert round(d["value"] - d5["value"]) == 256_930
    assert round((d["value"] - d5["value"]) / d["value"], 3) == 0.018
    roof = 400_000 / 1.085 ** 3
    assert round(roof) == 313_163
    assert round(roof / d["value"], 3) == 0.022


def test_problem_9_5():
    exp = {0.05: (84_000_000, 82_740_000, 6_447_826, 25_791), 0.0525: (80_000_000, 78_800_000, 3_021_739, 12_087),
           0.055: (76_363_636, 75_218_182, -92_885, -372)}
    for c, (gdv, net, land, pu) in exp.items():
        r = cre.residual_land_value(4_200_000 / c, 52e6, 9.5e6, 4.0e6, 0.15, 0.015)
        assert (round(4_200_000 / c), round(r["net_value"]), round(r["land_value"]), round(r["land_value"] / 250)) == \
            (gdv, net, land, pu)
    assert 52e6 + 9.5e6 + 4.0e6 + 6.0e6 == R(71_500_000)
    assert round(78_800_000 / 71_500_000 - 1, 3) == 0.102
    assert round(4_200_000 / 71_500_000, 4) == 0.0587
    assert round(80_000_000 / 76_363_636 - 1, 3) == 0.048


def test_problem_9_6():
    comps = {"X": (310_000, [-0.10, 0.0, 0.05]), "Y": (265_000, [-0.02, 0.08, 0.0]),
             "Z": (290_000, [-0.04, -0.03, -0.05])}
    adj, w = _grid(comps)
    assert {k: round(v[0], 4) for k, v in adj.items()} == {"X": 0.945, "Y": 1.0584, "Z": 0.8846}
    assert {k: round(v[1]) for k, v in adj.items()} == {"X": 292_950, "Y": 280_476, "Z": 256_546}
    ind = sum(adj[k][1] * w[k] for k in adj)
    assert round(ind) == 275_826
    assert round(ind * 120) == 33_099_072
    assert round(310_000 * 1.05) == 325_500
    assert round(325_500 / 292_950 - 1, 2) == 0.11


def _p97(exit_cap=0.07):
    n = [1_170_000 * 1.02 ** t for t in range(6)]
    c = [x * 0.94 for x in n[:5]]
    gross = n[5] / exit_cap
    net = gross * 0.98
    prop = [-18_000_000 * 1.01] + c[:4] + [c[4] + net]
    loan = 0.65 * 18_000_000
    ds = tvm.annual_debt_service(loan, 0.06, 25)
    bal = tvm.loan_balance(loan, 0.06, 25, 60)
    eq = [prop[0] + loan] + [x - ds for x in c[:4]] + [c[4] - ds + net - bal]
    return n, c, gross, net, prop, loan, ds, bal, eq


def test_problem_9_7():
    n, c, gross, net, prop, loan, ds, bal, eq = _p97()
    assert [round(x) for x in n] == [1_170_000, 1_193_400, 1_217_268, 1_241_613, 1_266_446, 1_291_775]
    assert [round(x) for x in c] == [1_099_800, 1_121_796, 1_144_232, 1_167_117, 1_190_459]
    assert (round(gross), round(net)) == (18_453_922, 18_084_844)
    assert round(-prop[0]) == 18_180_000
    assert round(tvm.irr(prop), 4) == 0.0619
    assert loan == R(11_700_000)
    assert round(ds / loan, 4) == 0.0773
    assert round(ds) == 904_599
    assert round(1_170_000 / ds, 2) == 1.29
    assert round(1_170_000 / loan, 3) == 0.100
    assert round(bal) == 10_522_054
    assert [round(x) for x in eq] == [-6_480_000, 195_201, 217_197, 239_633, 262_517, 7_848_649]
    assert round(tvm.irr(eq), 4) == 0.0659
    assert round(eq[1] / 6_480_000, 4) == 0.0301
    assert round(c[0] / 18_180_000, 4) == 0.0605
    assert round((tvm.irr(eq) - tvm.irr(prop)) * 1e4) == 40
    _, _, _, _, prop2, _, _, _, eq2 = _p97(0.0725)
    assert (round(tvm.irr(prop2), 4), round(tvm.irr(eq2), 4)) == (0.0558, 0.0495)


def test_problem_9_8():
    kw = dict(price=30_000_000, n1=1_800_000, uplift=300_000, capex=1_200_000, uplift_year=3, capex_year=2)
    steps = [(0.0, False, 0.06, 0.0600), (0.02, False, 0.06, 0.0800), (0.02, True, 0.06, 0.1046),
             (0.02, True, 0.0575, 0.1126)]
    irrs = []
    for g, va, c, irr in steps:
        f, noi, _ = _va(g, va, c, **kw)
        irrs.append(tvm.irr(f))
        assert round(irrs[-1], 4) == irr
    inc = [round(100 * (b - a), 2) for a, b in zip([0.0] + irrs[:-1], irrs)]
    assert inc == [6.00, 2.00, 2.46, 0.81]
    assert round(inc[1] + inc[3], 2) == 2.81
    f, noi, _ = _va(0.02, True, 0.06, **kw)
    assert [round(x) for x in noi] == [1_800_000, 1_836_000, 2_172_720, 2_216_174, 2_260_498, 2_305_708]
    f, _, _ = _va(0.0, True, 0.06, **kw)
    assert round(tvm.irr(f), 4) == 0.0850
    f, _, _ = _va(0.0, True, 0.065, **kw)
    assert round(tvm.irr(f), 4) == 0.0704


def test_problem_9_9():
    assert 1_260_000 / 0.045 == R(28_000_000)
    v = 1_200_000 / 0.06
    assert v == R(20_000_000)
    assert round(28_000_000 / v - 1, 2) == 0.40
    s = cre.max_loan(noi=1_200_000, value=v, annual_rate=0.0675, amort_years=30,
                     ltv_max=0.60, dscr_min=1.25, debt_yield_min=0.09)
    assert s["binding"] == "ltv"
    assert (round(s["ltv"]), round(s["dscr"]), round(s["debt_yield"])) == (12_000_000, 12_334_295, 13_333_333)
    assert round(cre.refinance_gap(17_000_000, s["max_loan"], 0.01 * s["max_loan"])) == 5_120_000
    assert round(17_000_000 / 0.98) == 17_346_939
    assert round(19_500_000 * 0.98 - 17_000_000) == 2_110_000
    assert round(17_000_000 / v, 2) == 0.85
    assert round(1_200_000 / 17_000_000, 4) == 0.0706


def test_problem_9_10():
    ga = 100 / 0.70
    assert round(ga, 2) == 142.86 and round(ga - 100, 2) == 42.86
    out = {}
    for off in (0.20, 0.30):
        dec = 0.40 * off + 0.35 * 0.05 + 0.25 * 0.08
        nav = 100 - ga * dec
        out[off] = (round(dec, 4), round(ga * dec, 2), round(nav, 2), round(78 / nav - 1, 3))
    assert out[0.20] == (0.1175, 16.79, 83.21, -0.063)
    assert out[0.30] == (0.1575, 22.50, 77.50, 0.006)
    x = ((100 - 78) / ga - 0.0375) / 0.40
    assert round(x, 3) == 0.291
    assert round(77.5 * 0.9, 2) == 69.75


# --------------------------------------------------------------- drill text figures (judgment parts)

def test_drill_text_figures():
    # D037 check line
    v = cre.loaded_cap_value(1_500_000, 0.07, 0.022 * 0.8)
    assert round(0.0176 * v) == 301_370
    # D040 LTV after
    assert round(0.65 / (0.95 * 5.5 / 6.5), 3) == 0.809
    # D042 reversion per $1 of NOI
    assert round(1 / 0.0525, 3) == 19.048 and round(1.025 ** 5 / 0.0575, 3) == 19.677
    # D043 hotel figures
    assert round(1_050_000 / 0.09 / 1e6, 1) == 11.7 and round(1_050_000 / 0.105 / 1e6, 1) == 10.0
    assert round(1 - 1_050_000 / 0.09 / 16_500_000, 2) == 0.29
    assert round(1 - 1_050_000 / 0.105 / 16_500_000, 2) == 0.39
    assert round(11_800_000 / 0.98 / 1e6, 2) == 12.04 and round(11_800_000 / 0.97 / 1e6, 2) == 12.16
    assert 165_000 * 120 == 19_800_000
    # D045 unlevered IRR at the 7.00% exit
    assert round(tvm.irr([-10e6] + [650e3] * 4 + [650e3 + 650e3 / 0.07]), 4) == 0.0521


def test_opening_problem_figures():
    assert round(3_400_000 / 48_600_000, 4) == 0.07
    assert 400 * 165_000 == 66_000_000
    assert round(1 - 48_600_000 / 66_000_000, 2) == 0.26
    assert 49_500 / 165_000 == R(0.30)
    # reconciliation table
    assert 3_400_000 / 0.08 == R(42_500_000)
