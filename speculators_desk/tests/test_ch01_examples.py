"""Reproduces every number in Chapter 1 text, problems, and solutions."""

import math

import pytest

from sdesk import cre, risk, tvm

R = pytest.approx


def _scenarios(basis, scen, sell=0.03):
    out = []
    for p, n1, n2, gross in scen:
        net = gross * (1 - sell)
        out.append({"p": p, "net": net, "profit": n1 + n2 + net - basis,
                    "irr": tvm.irr([-basis, n1, n2 + net]),
                    "mult": (n1 + n2 + net) / basis, "n1": n1, "n2": n2})
    return out


EX11 = [(0.55, 780_000, 850_000, 9_400_000), (0.30, 760_000, 800_000, 8_600_000),
        (0.15, 650_000, 560_000, 6_400_000)]


def test_example_1_1():
    basis = 7_800_000 * 1.015
    assert basis == R(7_917_000)
    s = _scenarios(basis, EX11)
    assert [x["net"] for x in s] == [R(9_118_000), R(8_342_000), R(6_208_000)]
    assert [x["profit"] for x in s] == [R(2_831_000), R(1_985_000), R(-499_000)]
    assert [round(x["irr"], 4) for x in s] == [0.1724, 0.1237, -0.0334]
    assert [round(x["mult"], 3) for x in s] == [1.358, 1.251, 0.937]
    summ = cre.scenario_summary([x["profit"] for x in s], [x["p"] for x in s])
    assert summ["ev"] == R(2_077_700)
    assert summ["sd"] == R(1_144_810, abs=1)
    assert summ["p_loss"] == R(0.15)
    assert summ["expected_loss"] == R(-74_850)
    e_irr = sum(x["p"] * x["irr"] for x in s)
    assert round(e_irr, 4) == 0.1269
    e1 = sum(x["p"] * x["n1"] for x in s)
    e_n2 = sum(x["p"] * x["n2"] for x in s)
    e_sale = sum(x["p"] * x["net"] for x in s)
    assert (e1, e_n2, e_sale) == (R(754_500), R(791_500), R(8_448_700))
    assert round(tvm.irr([-basis, e1, e_n2 + e_sale]), 4) == 0.1290


def _q_star(profits, rel_good, rel_base):
    gbar = (rel_good * profits[0] + rel_base * profits[1]) / (rel_good + rel_base)
    return gbar, gbar / (gbar - profits[2])


def test_example_1_2():
    prof = [2_831_000, 1_985_000, -499_000]
    assert round(cre.breakeven_probability(prof[0], -prof[2]), 3) == 0.850
    gbar, q = _q_star(prof, 55, 30)
    assert gbar == R(2_532_412, abs=1)
    assert round(q, 3) == 0.835
    pip = [x - 1_500_000 for x in prof]
    assert 0.55 * pip[0] + 0.30 * pip[1] + 0.15 * pip[2] == R(577_700)
    gbar2, q2 = _q_star(pip, 55, 30)
    assert gbar2 == R(1_032_412, abs=1)
    assert round(q2, 3) == 0.341


def test_example_1_3():
    n0 = 7_800_000 * 0.99
    assert n0 == R(7_722_000)
    gross = 0.8 * 9_000_000 + 0.2 * 8_400_000
    net = gross * 0.97 - 250_000
    assert net == R(8_363_600)
    tau = 0.8 * 0.5 + 0.2 * 0.75
    assert tau == R(0.55)
    r = (net / n0) ** (1 / tau) - 1
    assert round(r, 4) == 0.1562
    assert round(math.log(net / n0) / tau, 4) == 0.1451


def test_example_1_4():
    assert 0.05 - 0.20 * 0.40 == R(-0.03)
    assert 0.20 * 0.40 == R(0.08)


def test_example_1_5():
    assert risk.expected_value([35, -1], [1 / 38, 37 / 38]) == R(-2 / 38)
    assert risk.expected_value([0.6, -0.5], [0.5, 0.5]) == R(0.05)
    f_star = risk.kelly_general_binary(0.5, 0.6, 0.5)
    assert f_star == R(1 / 6)
    table = {0.10: (0.003488, 0.0035, 1.035), f_star: (0.004149, 0.0042, 1.042),
             0.25: (0.003115, 0.0031, 1.032), 0.50: (-0.012659, -0.0126, 0.881),
             1.00: (-0.111572, -0.1056, 0.328), 1.50: (-0.372220, -0.3108, 0.024)}
    for f, (g_log, g_pct, w10) in table.items():
        g = risk.expected_log_growth([0.6, -0.5], [0.5, 0.5], f)
        assert round(g, 6) == g_log
        assert round(math.exp(g) - 1, 4) == g_pct
        assert round(math.exp(10 * g), 3) == w10
    assert 1.6 ** 5 * 0.5 ** 5 == R(0.32768)


def test_example_1_6():
    basis = 5_000_000 * 1.015
    close = 5_400_000 * 0.98 - basis
    walk = 4_900_000 * 0.98 + 150_000 - basis
    assert (close, walk) == (R(217_000), R(-123_000))
    assert 0.7 * close + 0.3 * walk == R(115_000)
    assert round(-walk / (close - walk), 3) == 0.362
    walk2 = 4_600_000 * 0.98 + 150_000 - basis
    assert walk2 == R(-417_000)
    assert 0.7 * close + 0.3 * walk2 == R(26_800)


def test_example_1_7():
    assert 0.6 * 10.0 + 0.4 * 8.5 == R(9.4)
    assert 10.0 - 9.8 - 0.04 == R(0.16)


def test_section_1_6_leverage():
    loan = 0.6 * 14_000_000
    pmt = tvm.payment(loan, 0.065, 30)
    assert round(pmt) == 53_094
    ds = 12 * pmt
    assert round(ds) == 637_125
    assert round(875_000 - ds) == 237_875
    assert round((875_000 - ds) / 5_600_000, 4) == 0.0425
    assert (0.0625 - 0.6 * 0.065) / 0.4 == R(0.05875)
    assert 875_000 / 14_000_000 == R(0.0625)


# ------------------------------------------------------------- problems

def test_problem_1_3():
    assert math.sqrt(1.4 * 0.7) - 1 == R(-0.01005, abs=1e-5)


def test_problem_1_4():
    assert cre.breakeven_probability(1.2, 2.0) == R(0.375)


def test_problem_1_5():
    basis = 5_200_000 * 1.02
    assert basis == R(5_304_000)
    sc = [(0.5, 420_000, 450_000, 6_000_000), (0.35, 400_000, 410_000, 5_400_000),
          (0.15, 330_000, 300_000, 4_300_000)]
    s = _scenarios(basis, sc)
    assert [x["profit"] for x in s] == [R(1_386_000), R(744_000), R(-503_000)]
    assert [round(x["irr"], 4) for x in s] == [0.1276, 0.0703, -0.0502]
    summ = cre.scenario_summary([x["profit"] for x in s], [x["p"] for x in s])
    assert summ["ev"] == R(877_950)
    assert round(summ["sd"]) == 649_146
    assert round(sum(x["p"] * x["irr"] for x in s), 4) == 0.0809
    e1 = sum(x["p"] * x["n1"] for x in s)
    e_n2 = sum(x["p"] * x["n2"] for x in s)
    e_sale = sum(x["p"] * x["net"] for x in s)
    assert (e1, e_n2, e_sale) == (R(399_500), R(413_500), R(5_368_950))
    assert round(tvm.irr([-basis, e1, e_n2 + e_sale]), 4) == 0.0825
    gbar, q = _q_star([x["profit"] for x in s], 50, 35)
    assert round(gbar) == 1_121_647
    assert round(q, 3) == 0.690


def test_problem_1_6():
    net = 5_100_000 * 0.97 - 90_000
    assert net == R(4_857_000)
    assert round((net / 4_600_000) ** 1.5 - 1, 4) == 0.0850
    n1 = 9_000_000 * 0.97 - 250_000
    n2 = 8_400_000 * 0.97 - 250_000
    lo, hi = 0.0, 1.0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        v = 0.8 * n1 / (1 + m) ** 0.5 + 0.2 * n2 / (1 + m) ** 0.75 - 7_722_000
        lo, hi = (m, hi) if v > 0 else (lo, m)
    assert round(lo, 4) == 0.1572


def test_problem_1_7():
    assert 0.06 - 0.15 * 0.60 == R(-0.03)
    assert 2 * 0.15 * 0.60 == R(0.18)
    assert 2 * 0.30 * 0.60 == R(0.36)


def test_problem_1_8():
    basis = 3_200_000 * 1.015
    close = 3_450_000 * 0.98 - basis
    walk = 3_150_000 * 0.98 + 60_000 - basis
    assert (close, walk) == (R(133_000), R(-101_000))
    assert 0.65 * close + 0.35 * walk == R(51_100)
    assert round(-walk / (close - walk), 3) == 0.432
    assert 0.65 * close == R(86_450)


def test_problem_1_9():
    rs, ps = [0.16, -0.04, -0.25], [0.6, 0.3, 0.1]
    expected = {0.0: (0.0590, 0.04804), 0.5: (0.0680, 0.02178), 0.65: (0.0757, -0.04784),
                0.75: (0.1010, None), 0.85: (0.2050, None)}
    for lam, (ev, lg) in expected.items():
        eq = [max((r - lam * 0.05) / (1 - lam), -1.0) for r in rs]
        assert round(sum(p * e for p, e in zip(ps, eq)), 4) == ev
        if lg is None:
            assert min(eq) == -1.0
        else:
            assert round(sum(p * math.log(1 + e) for p, e in zip(ps, eq)), 5) == lg
