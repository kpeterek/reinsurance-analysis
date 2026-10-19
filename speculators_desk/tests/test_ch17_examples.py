"""Reproduces every number in Chapter 17 text, problems, and solutions.

Where possible each number is checked by an independent route (closed form,
reverse calculation, numerical integration, or a different library function).
"""

import math

import pytest

from sdesk import fixed_income as fi
from sdesk import markets, tvm
from sdesk import x_capital_structure as xcs
from sdesk import x_credit as xc
from sdesk import x_rates

R = pytest.approx


# --------------------------------------------------------------------------
# Library unit and boundary tests
# --------------------------------------------------------------------------

def test_hazard_roundtrip_and_boundaries():
    for pd in (0.0, 0.01, 0.3, 0.9):
        lam = xc.hazard_from_cum_pd(pd, 4)
        assert xc.cum_pd_from_hazard(lam, 4) == R(pd)
    assert xc.hazard_from_cum_pd(0.0, 5) == 0.0
    with pytest.raises(ValueError):
        xc.hazard_from_cum_pd(1.0, 5)
    # triangle agrees with the existing x_rates helper
    assert xc.triangle_hazard(0.045, 0.4) == R(x_rates.credit_triangle_hazard(0.045, 0.4))


def test_triangle_exact_for_continuous_premium():
    # Numerically integrate both legs with continuous premium: par spread = lambda (1-R).
    lam, rec, r, T, n = 0.08, 0.35, 0.03, 5.0, 200_000
    dt = T / n
    prem = sum(math.exp(-(r + lam) * (k + 0.5) * dt) * dt for k in range(n))
    prot = sum((1 - rec) * lam * math.exp(-(r + lam) * (k + 0.5) * dt) * dt for k in range(n))
    assert prot / prem == R(xc.triangle_spread(lam, rec), rel=1e-9)
    # closed-form protection leg in cds_flat matches the integral
    assert xc.cds_flat(lam, rec, r, T)["protection"] == R(prot, rel=1e-6)


def test_apr_waterfall_boundaries():
    cls = [("S", 100), [("U1", 50), ("U2", 50)], ("J", 20)]
    zero = xc.apr_waterfall(0, cls)
    assert all(r["paid"] == 0 for r in zero["rows"]) and zero["fulcrum"] == "S"
    full = xc.apr_waterfall(500, cls)
    assert full["fulcrum"] is None and full["residual"] == R(280)
    # value exactly exhausting a class: next class is the fulcrum at zero recovery
    edge = xc.apr_waterfall(100, cls)
    assert edge["by_name"]["S"]["recovery"] == 1.0 and edge["fulcrum"] == ["U1", "U2"]


def test_tranche_loss_boundaries():
    assert xc.tranche_loss(0.0, 0.05, 0.10) == 0.0
    assert xc.tranche_loss(1.0, 0.05, 0.10) == 1.0  # 100% pool loss wipes every tranche
    assert xc.tranche_loss(0.05, 0.05, 0.10) == 0.0
    with pytest.raises(ValueError):
        xc.tranche_loss(0.1, 0.1, 0.1)


def test_merton_boundaries():
    # zero leverage limit: tiny face -> debt riskless, equity ~ V - F e^{-rT}
    m = xc.merton(100, 1e-6, 3, 0.04, 0.2)
    assert m["equity"] == R(100, abs=1e-5) and m["spread"] == R(0, abs=1e-6)
    # higher volatility always raises equity and spread
    lo, hi = xc.merton(80, 80, 3, 0.04, 0.15), xc.merton(80, 80, 3, 0.04, 0.20)
    assert hi["equity"] > lo["equity"] and hi["spread"] > lo["spread"]


def test_bond_ytm_roundtrip():
    y = xc.bond_ytm(96.5, 0.0675, 5)
    assert fi.bond_price(y, 0.0675, 5) == R(96.5, abs=1e-9)
    assert xc.bond_ytm(100, 0.05, 7) == R(0.05, abs=1e-10)  # par bond yields its coupon


# --------------------------------------------------------------------------
# Worked examples
# --------------------------------------------------------------------------

def test_example_17_1():
    lam = xc.hazard_from_cum_pd(0.10, 5)
    assert round(lam, 6) == 0.021072
    assert round(100 * xc.annual_pd_from_hazard(lam), 3) == 2.085
    assert round(1e4 * xc.triangle_spread(lam, 0.40), 1) == 126.4
    lam2 = xc.triangle_hazard(0.045, 0.40)
    assert lam2 == R(0.075)
    assert round(math.exp(-0.375), 6) == 0.687289
    assert round(100 * xc.cum_pd_from_hazard(lam2, 5), 2) == 31.27
    assert round(100 * xc.annual_pd_from_hazard(lam2), 2) == 7.23
    assert round(100 * (1 - (1 - 0.075) ** 5), 2) == 32.28
    assert -math.log(1 - 0.312711) / 5 == R(0.075, abs=1e-6)


def test_example_17_2():
    y = xc.bond_ytm(96.50, 0.0675, 5)
    assert round(100 * y, 3) == 7.605
    # independent route: RATE on semiannual flows
    ys = tvm.irr([-96.5] + [3.375] * 9 + [103.375])
    assert 2 * ys == R(y, abs=1e-8)
    s = y - 0.041
    assert round(1e4 * s, 1) == 350.5
    d = xc.spread_decomposition(s, 0.012, 0.45, 0.006)
    assert round(1e4 * d["expected_loss"], 1) == 66.0
    assert round(1e4 * d["risk_premium"], 1) == 224.5
    assert round(100 * d["rn_hazard"], 2) == 5.28
    assert round(d["rn_to_physical"], 2) == 4.40
    assert d["expected_loss"] + d["liquidity"] + d["risk_premium"] == R(s)
    dm = fi.modified_duration(y, 0.0675, 5)
    assert round(dm, 3) == 4.153
    bp_per_point = 1 / (96.5 * dm)
    assert round(1e4 * bp_per_point, 1) == 24.9
    assert round(1e4 * bp_per_point / 2, 1) == 12.5


CLS_17_3 = [("Admin", 20), ("1L", 350), ("2L", 150), [("SrNotes", 200), ("Trade", 40)], ("Sub", 80)]


def test_example_17_3():
    w = xc.apr_waterfall(620, CLS_17_3)["by_name"]
    assert w["SrNotes"]["recovery"] == R(100 / 240)
    assert round(100 * w["SrNotes"]["recovery"], 2) == 41.67
    assert (round(w["SrNotes"]["paid"], 2), round(w["Trade"]["paid"], 2)) == (83.33, 16.67)
    assert w["Sub"]["paid"] == 0
    assert xc.apr_waterfall(620, CLS_17_3)["fulcrum"] == ["SrNotes", "Trade"]
    w2 = xc.apr_waterfall(470, CLS_17_3)
    assert round(100 * w2["by_name"]["2L"]["recovery"], 2) == 66.67
    assert w2["fulcrum"] == "2L"
    assert w2["by_name"]["SrNotes"]["paid"] == 0
    assert sum(r["paid"] for r in w2["rows"]) == R(470)
    assert 150 - w2["by_name"]["2L"]["paid"] == R(50)  # deficiency claim
    assert round(100 * 150 / 620) == 24


OPCO = [("OpBank", 250), [("OpNotes", 100), ("OpTrade", 30)]]
HOLD = [("HoldNotes", 200)]


def _holdco_rec(v):
    return xc.holdco_opco(v, OPCO, HOLD)["holdco"]["by_name"]["HoldNotes"]["recovery"]


def test_example_17_4():
    assert [_holdco_rec(v) for v in (400, 500, 600)] == [R(0.10), R(0.60), R(1.0)]
    h600 = xc.holdco_opco(600, OPCO, HOLD)
    assert h600["holdco"]["residual"] == R(20)
    assert all(r["recovery"] == 1 for r in h600["opco"]["rows"])
    # independent route: holdco value = V - 380
    assert [max(v - 380, 0) for v in (400, 500, 600)] == [20, 120, 220]
    g = lambda v: xc.apr_waterfall(v, [("OpBank", 250), [("OpNotes", 100), ("OpTrade", 30),
                                                       ("HoldNotes", 200)]])["by_name"]
    assert round(100 * g(400)["HoldNotes"]["recovery"], 2) == 45.45
    assert round(g(400)["HoldNotes"]["paid"], 1) == 90.9
    assert round(g(400)["OpNotes"]["paid"], 1) == 45.5
    assert round(100 * g(500)["HoldNotes"]["recovery"], 2) == 75.76
    assert round(g(500)["HoldNotes"]["paid"], 1) == 151.5
    assert round(g(500)["OpNotes"]["paid"], 1) == 75.8
    assert round(g(500)["OpTrade"]["paid"], 2) == 22.73
    assert g(600)["HoldNotes"]["recovery"] == 1.0
    gain = g(500)["HoldNotes"]["paid"] - 120
    assert round(gain, 1) == 31.5 and round(100 * gain / 200, 1) == 15.8
    assert round(100 - 100 * g(500)["OpNotes"]["recovery"], 1) == 24.2


def test_example_17_5():
    rec = [100 * _holdco_rec(v) for v in (400, 500, 600)]
    p = [0.30, 0.50, 0.20]
    er = sum(a * b for a, b in zip(p, rec))
    assert er == R(53.0)
    assert round(er / 38, 3) == 1.395
    assert round(100 * ((er / 38) ** (1 / 1.5) - 1), 2) == 24.83
    assert [round(100 * ((x / 38) ** (1 / 1.5) - 1), 2) for x in rec] == [-58.93, 35.60, 90.61]
    gbar = (5 * 60 + 2 * 100) / 7
    assert round(gbar, 2) == 71.43
    q = (gbar - 38) / (gbar - 10)
    assert round(100 * q, 1) == 54.4
    pmax = er / 1.2 ** 1.5
    assert round(1.2 ** 1.5, 5) == 1.31453
    assert round(pmax, 2) == 40.32
    assert (er / pmax) ** (1 / 1.5) == R(1.2)
    # IRR via tvm on a 1.5-year single flow as an independent check (semiannual periods)
    irr_half = tvm.irr([-38, 0, 0, er])
    assert (1 + irr_half) ** 2 - 1 == R(0.248326, abs=1e-6)
    assert round(100 * (1 - 10 / 38)) == 74


def test_example_17_6():
    u = xc.cds_upfront_triangle(0.065, 0.05, 0.40, 0.04, 5)
    assert round(100 * u["hazard"], 3) == 10.833
    assert round(u["rpv01"], 4) == 3.4654
    assert round(100 * u["upfront"], 2) == 5.20
    assert round(u["upfront"] * 1e7) == 519_806
    assert 0.05 * 1e7 == 500_000 and 0.05 * 1e7 / 4 == 125_000
    w = xc.cds_upfront_triangle(0.09, 0.05, 0.40, 0.04, 5)
    assert w["hazard"] == R(0.15)
    assert round(w["rpv01"], 4) == 3.1516
    assert round(100 * w["upfront"], 2) == 12.61
    assert round(w["upfront"] * 1e7) == 1_260_651
    mtm = w["upfront"] - u["upfront"]
    assert round(100 * mtm, 2) == 7.41
    assert round(mtm * 1e7) == 740_845
    assert round(100 * 0.025 * u["rpv01"], 2) == 8.66
    ex = xc.cds_flat(u["hazard"], 0.40, 0.04, 5, coupon=0.05)
    assert round(ex["protection"], 5) == 0.22948
    assert round(1e4 * ex["par_spread"], 1) == 662.2
    assert round(100 * ex["upfront"], 2) == 5.62
    # independent route for RPV01: geometric series
    x = math.exp(-(0.04 + 0.065 / 0.6) / 4)
    assert 0.25 * x * (1 - x ** 20) / (1 - x) == R(u["rpv01"])
    riskless = sum(0.25 * math.exp(-0.04 * i / 4) for i in range(1, 21))
    assert round(riskless, 4) == 4.5091
    assert 100 - 38 == 62


STACK = [("A", 0.30, 1.0), ("AS", 0.22, 0.30), ("B", 0.16, 0.22), ("C", 0.11, 0.16),
         ("D", 0.065, 0.11), ("E", 0.04, 0.065), ("F", 0.0, 0.04)]


def test_example_17_7():
    sizes = {n: (d - a) * 1000 for n, a, d in STACK}
    assert [round(sizes[n], 6) for n in "A AS B C D E F".split()] == [700, 80, 60, 50, 45, 25, 40]
    assert sum(sizes.values()) == R(1000)
    L1 = 0.25 * 0.45
    assert L1 == R(0.1125)
    t1 = {r["name"]: r for r in xc.tranche_table(1000, L1, STACK)}
    assert [round(t1[n]["loss"], 6) for n in "F E D C B AS A".split()] == [40, 25, 45, 2.5, 0, 0, 0]
    assert t1["C"]["loss_pct"] == R(0.05) and t1["D"]["loss_pct"] == R(1.0)
    assert sum(r["loss"] for r in t1.values()) == R(112.5)
    # independent route: Chapter 10 capital-stack function
    tl = {r["name"]: r["loss"] for r in xcs.tranche_losses(1000, 1000 - 112.5,
                                                            [(n, sizes[n]) for n, _, _ in STACK])}
    assert all(tl[n] == R(t1[n]["loss"]) for n in tl)
    L2 = 0.15 * 0.40
    assert L2 == R(0.06)
    t2 = {r["name"]: r for r in xc.tranche_table(1000, L2, STACK)}
    assert t2["F"]["loss"] == R(40) and t2["E"]["loss"] == R(20) and t2["E"]["loss_pct"] == R(0.80)
    assert t2["D"]["loss"] == 0
    assert round(100 * 0.065 / 0.45, 2) == 14.44
    assert round(100 * 0.11 / 0.45, 2) == 24.44
    assert xc.tranche_loss(0.065 / 0.45 * 0.45, 0.065, 0.11) == R(0, abs=1e-12)
    assert xc.credit_enhancement_after_paydown(300, 800) == R(0.375)
    assert xc.credit_enhancement_after_paydown(65, 800) == R(0.08125)


def test_example_17_8():
    m = xc.merton(100, 80, 3, 0.04, 0.15)
    assert round(math.log(100 / 80), 6) == 0.223144
    assert round(m["d1"], 4) == 1.4507 and round(m["d2"], 4) == 1.1909
    assert round(m["equity"], 2) == 29.99 and round(m["debt"], 2) == 70.01
    pv_face = 80 * math.exp(-0.12)
    assert round(pv_face, 2) == 70.95
    put = pv_face - m["debt"]
    assert round(put, 2) == 0.95
    # independent: put via Black-Scholes put price equals riskless PV minus risky debt
    assert markets.bs_price(100, 80, 3, 0.04, 0.15, "put") == R(put)
    assert round(100 * m["debt_yield"], 3) == 4.448
    assert round(1e4 * m["spread"], 1) == 44.8
    assert round(100 * m["rn_pd"], 2) == 11.69
    assert round(m["equity"] - (100 - pv_face), 2) == 0.95
    assert round(100 - pv_face, 2) == 29.05
    s = xc.merton(80, 80, 3, 0.04, 0.20)
    assert round(s["d1"], 4) == 0.5196 and round(s["d2"], 4) == 0.1732
    assert round(s["equity"], 2) == 15.51 and round(s["debt"], 2) == 64.49
    assert round(100 * s["debt_yield"], 3) == 7.185
    assert round(1e4 * s["spread"], 1) == 318.5
    assert round(100 * s["rn_pd"], 1) == 43.1
    lo = xc.merton(80, 80, 3, 0.04, 0.15)
    assert round(lo["equity"], 2) == 13.14 and round(lo["debt"], 2) == 66.86
    assert round(s["equity"] - lo["equity"], 2) == 2.38
    assert round(100 * s["equity"] / 80) == 19


# --------------------------------------------------------------------------
# Problems
# --------------------------------------------------------------------------

def test_problem_17_1():
    assert xc.triangle_hazard(0.018, 0.4) == R(0.03)


def test_problem_17_2():
    lam = xc.triangle_hazard(0.03, 0.40)
    assert lam == R(0.05)
    assert round(100 * xc.cum_pd_from_hazard(lam, 5), 2) == 22.12
    assert round(math.exp(-0.25), 2) == 0.78
    assert round(100 * xc.annual_pd_from_hazard(lam), 3) == 4.877
    assert round(100 * (0.05 - 0.00125), 2) == 4.88


def test_problem_17_3():
    assert xc.tranche_loss(0.20 * 0.35, 0.08, 0.12) == 0.0
    assert 0.20 * 0.50 == R(0.10)
    assert xc.tranche_loss(0.20 * 0.50, 0.08, 0.12) == R(0.50)
    assert 0.08 / 0.50 == R(0.16)


def test_problem_17_4():
    l3 = xc.hazard_from_cum_pd(0.075, 3)
    l5 = xc.hazard_from_cum_pd(0.13, 5)
    assert round(-math.log(0.925), 6) == 0.077962 and round(-math.log(0.87), 6) == 0.139262
    assert round(100 * l3, 3) == 2.599 and round(100 * l5, 3) == 2.785
    assert round(100 * xc.hazard_from_cum_pd(0.02, 1), 3) == 2.020
    f13 = xc.forward_hazard(0.02, 1, 0.075, 3)
    f35 = xc.forward_hazard(0.075, 3, 0.13, 5)
    assert round(100 * f13, 3) == 2.888 and round(100 * f35, 3) == 3.065
    c = xc.conditional_pd(0.075, 0.13)
    assert round(100 * c, 2) == 5.95
    assert 1 - math.exp(-2 * f35) == R(c)
    assert round(1e4 * xc.triangle_spread(l3, 0.35)) == 169
    assert round(1e4 * xc.triangle_spread(l5, 0.35)) == 181


CLS_17_5 = [("Admin", 15), ("1L", 160), ("2L", 90), [("Unsec", 120), ("Trade", 30)], ("Sub", 50)]


def test_problem_17_5():
    a = xc.apr_waterfall(300, CLS_17_5)
    assert round(100 * a["by_name"]["Unsec"]["recovery"], 2) == 23.33
    assert a["by_name"]["Unsec"]["paid"] == R(28.0) and a["by_name"]["Trade"]["paid"] == R(7.0)
    assert a["fulcrum"] == ["Unsec", "Trade"]
    b = xc.apr_waterfall(380, CLS_17_5)
    assert round(100 * b["by_name"]["Unsec"]["recovery"], 2) == 76.67
    assert b["by_name"]["Unsec"]["paid"] == R(92.0) and b["by_name"]["Trade"]["paid"] == R(23.0)
    assert b["by_name"]["Sub"]["paid"] == 0
    assert 15 + 160 + 90 + 150 == 415
    c = xc.apr_waterfall(240, CLS_17_5)
    assert round(100 * c["by_name"]["2L"]["recovery"], 2) == 72.22
    assert c["fulcrum"] == "2L"
    assert 90 - c["by_name"]["2L"]["paid"] == R(25)


def test_problem_17_6():
    a = xc.cds_upfront_triangle(0.032, 0.01, 0.40, 0.03, 5)
    assert round(100 * a["hazard"], 3) == 5.333
    assert round(a["rpv01"], 4) == 4.0467
    assert round(100 * a["upfront"], 2) == 8.90
    assert round(a["upfront"] * 1e7) == 890_266
    b = xc.cds_upfront_triangle(0.025, 0.01, 0.40, 0.03, 5)
    assert round(100 * b["hazard"], 4) == 4.1667
    assert round(b["rpv01"], 4) == 4.1647
    assert round(100 * b["upfront"], 2) == 6.25
    assert round(b["upfront"] * 1e7) == 624_705
    mtm = b["upfront"] - a["upfront"]
    assert round(100 * mtm, 2) == -2.66
    assert round(mtm * 1e7) == -265_562
    lin = -0.007 * a["rpv01"]
    assert round(100 * lin, 2) == -2.83 and round(lin * 1e7) == -283_267


def test_problem_17_7():
    a = xc.merton(50, 35, 2, 0.04, 0.18)
    assert round(math.log(50 / 35), 6) == 0.356675
    assert round(a["d1"], 4) == 1.8427 and round(a["d2"], 4) == 1.5881
    assert round(a["equity"], 2) == 17.87 and round(a["debt"], 2) == 32.13
    assert round(100 * a["debt_yield"], 3) == 4.278
    assert round(1e4 * a["spread"], 1) == 27.8
    assert round(100 * a["rn_pd"], 2) == 5.61
    b = xc.merton(40, 35, 2, 0.04, 0.18)
    assert round(b["equity"], 2) == 8.71 and round(b["debt"], 2) == 31.29
    assert round(100 * b["debt_yield"], 3) == 5.607
    assert round(1e4 * b["spread"], 1) == 160.7
    assert round(100 * b["rn_pd"], 2) == 23.84
    de = a["equity"] - b["equity"]
    assert round(de, 2) == 9.16 and round(de / 10, 3) == 0.916
    assert round(a["delta"], 3) == 0.967 and round(b["delta"], 3) == 0.833
    assert round(10 - de, 2) == 0.84


def _p8(opco_classes):
    out = []
    for v in (260, 320, 400):
        h = xc.holdco_opco(v, opco_classes, [("H", 150)])
        out.append(100 * h["holdco"]["by_name"]["H"]["recovery"])
    return out


def test_problem_17_8():
    rec = _p8([("S", 180), ("U", 60)])
    assert [round(x, 2) for x in rec] == [13.33, 53.33, 100.0]
    assert xc.holdco_opco(400, [("S", 180), ("U", 60)], [("H", 150)])["holdco"]["residual"] == R(10)
    er = sum(p * x for p, x in zip((0.35, 0.45, 0.20), rec))
    assert round(er, 2) == 48.67
    assert round(er / 30, 3) == 1.622
    assert round(100 * ((er / 30) ** 0.5 - 1), 2) == 27.37
    rec2 = _p8([("Prime", 40), ("S", 180), ("U", 60)])
    assert [round(x, 2) for x in rec2] == [0.0, 26.67, 80.0]
    er2 = sum(p * x for p, x in zip((0.35, 0.45, 0.20), rec2))
    assert er2 == R(28.0)
    assert round(100 * ((er2 / 30) ** 0.5 - 1), 2) == -3.39


def test_problem_17_9():
    losses = [xc.tranche_loss(L, 0.065, 0.11) for L in (0.04, 0.08, 0.12)]
    assert losses == [0.0, R(1 / 3), 1.0]
    prin = [100 * (1 - x) for x in losses]
    cash = [16 + x for x in prin]
    assert [round(x, 2) for x in cash] == [116.0, 82.67, 16.0]
    p = (0.40, 0.35, 0.25)
    ep = sum(a * b for a, b in zip(p, prin))
    assert round(ep, 2) == 63.33
    assert round(sum(a * b for a, b in zip(p, cash)), 2) == 79.33
    assert round(100 * tvm.irr([-72, 4, 4, 4, 4 + ep]), 2) == 2.66
    assert [round(100 * tvm.irr([-72, 4, 4, 4, 4 + x]), 2) for x in prin] == [13.51, 3.81, -41.33]
    gbar = (40 * cash[0] + 35 * cash[1]) / 75
    assert round(gbar, 2) == 100.44
    q = (gbar - 72) / (gbar - 16)
    assert round(gbar - 72, 2) == 28.44 and round(gbar - 16, 2) == 84.44
    assert round(100 * q, 1) == 33.7
    assert round(100 * xc.credit_enhancement_after_paydown(65, 700), 2) == 9.29


def test_problem_17_10():
    cls = [("Admin", 15), ("1L", 300), ("2L", 200)]
    rec = [100 * xc.apr_waterfall(v, cls)["by_name"]["2L"]["recovery"] for v in (380, 450, 520)]
    assert rec == [R(32.5), R(67.5), R(100.0)]
    assert xc.apr_waterfall(520, cls)["residual"] == R(5)
    v_star = 15 + 300 + 0.55 * 200
    assert v_star == R(425)
    assert 100 * xc.apr_waterfall(v_star, cls)["by_name"]["2L"]["recovery"] == R(55)
