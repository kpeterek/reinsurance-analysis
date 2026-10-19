"""Reproduces every number in Chapter 7 text, problems, and solutions."""

import math

import pytest

from sdesk import cre, fixed_income as fi, markets as mk, tvm

R = pytest.approx


# --------------------------------------------------------------------------
# helpers (explicit formulas, independent of the library where possible)
# --------------------------------------------------------------------------

def debt_path(d0, rates, g, pb):
    """d_{t+1} = d_t (1+r_t)/(1+g) - pb; ``rates`` is one effective rate per year."""
    out = [d0]
    for r in rates:
        out.append(out[-1] * (1 + r) / (1 + g) - pb)
    return out


def pb_star(d, r, g):
    return d * (r - g) / (1 + g)


def hedged_return(y, r_home, r_foreign):
    """(1+y)(1+r_home)/(1+r_foreign) - 1 for t = 1."""
    return (1 + y) * (1 + r_home) / (1 + r_foreign) - 1


# --------------------------------------------------------------------------
# Example 7.1
# --------------------------------------------------------------------------

def test_example_7_1():
    d1 = 1.0 * 1.035 / 1.04 + 0.025
    assert 1.035 / 1.04 == R(0.995192, abs=1e-6)
    assert round(d1, 4) == 1.0202
    assert pb_star(1.0, 0.035, 0.04) == R(-0.004808, abs=1e-6)
    p1 = debt_path(1.0, [0.035] * 10, 0.04, -0.025)
    assert [round(p1[i], 4) for i in (1, 5, 10)] == [1.0202, 1.1000, 1.1976]
    p2 = debt_path(1.0, [0.05] * 10, 0.04, -0.025)
    assert [round(p2[i], 4) for i in (1, 5, 10)] == [1.0346, 1.1764, 1.3615]
    assert pb_star(1.0, 0.05, 0.04) == R(0.009615, abs=1e-6)
    assert pb_star(1.0, 0.05, 0.04) + 0.025 == R(0.034615, abs=1e-6)
    assert round(pb_star(p2[10], 0.05, 0.04), 4) == 0.0131
    # steady state when r < g
    d_star = 0.025 * 1.04 / 0.005
    assert d_star == R(5.2)
    assert d_star * 1.035 / 1.04 + 0.025 == R(d_star)  # it is a fixed point
    # check by the change formula
    assert 1.0 * (0.035 - 0.04) / 1.04 + 0.025 == R(0.020192, abs=1e-6)


# --------------------------------------------------------------------------
# Example 7.2
# --------------------------------------------------------------------------

def test_example_7_2():
    s = 0.056 - 0.024
    assert s == R(0.032)
    lam40, lam25 = s / 0.6, s / 0.75
    assert round(lam40, 4) == 0.0533 and round(lam25, 4) == 0.0427
    assert round(1 - math.exp(-lam40 * 5), 3) == 0.234
    assert round(1 - math.exp(-lam40 * 10), 3) == 0.413
    assert round(1 - math.exp(-lam25 * 5), 3) == 0.192
    assert round(1 - math.exp(-lam25 * 10), 3) == 0.347
    assert 1 - 1.024 / 1.056 == R(0.030303, abs=1e-6)
    p = (1 - 1.024 / 1.056) / 0.6
    assert round(p, 4) == 0.0505
    # the exact p reprices the bond at par
    assert ((1 - p) * 1.056 + p * 0.4 * 1.056) / 1.024 == R(1.0)
    el = 0.015 * 0.6
    assert el == R(0.009)
    assert s - el == R(0.023)
    assert round((s - el) / s, 2) == 0.72  # "about 70%"
    assert 0.028 - s == R(-0.004)  # basis -40 bp
    assert round(math.exp(-lam40 * 5), 3) == 0.766
    assert round(1 - math.exp(-0.015 * 5), 3) == 0.072  # "about 7%"


# --------------------------------------------------------------------------
# Example 7.3
# --------------------------------------------------------------------------

def test_example_7_3():
    d10 = fi.modified_duration(0.0425, 0.0425, 10)
    d30 = fi.modified_duration(0.0475, 0.0475, 30)
    assert round(d10, 3) == 8.078 and round(d30, 3) == 15.904
    assert fi.bond_price(0.0425, 0.0425, 10) == R(100.0)
    v10, v30 = fi.dv01(0.0425, 0.0425, 10), fi.dv01(0.0475, 0.0475, 30)
    assert round(v10, 5) == 0.08078 and round(v30, 5) == 0.15904
    assert 42e9 / 100 * v10 == R(33.93e6, rel=1e-3)
    assert 25e9 / 100 * v30 == R(39.76e6, rel=1e-3)
    assert round(25 * v30 / v10, 1) == 49.2
    # first-order check: D_mod x 1bp x 100
    assert round(0.0001 * d10 * 100, 4) == round(v10, 4)
    # term-premium scenarios
    for bp_per_point, dy, cap1, dv in ((25, 37.5, 0.061875, -0.0303), (10, 15.0, 0.06075, -0.0123)):
        assert 1.5 * bp_per_point == R(dy)
        assert 0.06 + 0.5 * dy / 10_000 == R(cap1)
        assert round(cre.cap_rate_shock_pct(0.06, cap1), 4) == dv


# --------------------------------------------------------------------------
# Example 7.4
# --------------------------------------------------------------------------

def test_example_7_4():
    ca = (0.215 - 0.210) + (-0.044)
    assert ca == R(-0.039)
    assert ca * 29.0 == R(-1.131)
    assert 0.01 * 29.0 == R(0.29)
    # BEA cross-check: $1.13tn at 3.9% of GDP implies GDP of about $29tn
    assert round(1.13 / 0.039, 1) == 29.0


# --------------------------------------------------------------------------
# Example 7.5
# --------------------------------------------------------------------------

def test_example_7_5():
    f_eur = mk.covered_interest_forward(1.10, 0.04, 0.02, 1)
    f_jpy = mk.covered_interest_forward(150.0, 0.005, 0.04, 1)
    assert round(f_eur, 6) == 1.121569
    assert round(f_jpy, 4) == 144.9519
    usd = mk.convert(10e6, 1.10, "EUR", "EUR/USD")
    assert usd == R(11e6)
    term = usd * 1.043
    assert term == R(11_473_000)
    eur = mk.convert(term, f_eur, "USD", "EUR/USD")
    assert round(eur) == 10_229_423
    h = eur / 10e6 - 1
    assert round(h, 5) == 0.02294
    assert h == R(hedged_return(0.043, 0.02, 0.04))
    assert round(h - 0.026, 4) == -0.0031
    assert 0.043 - (0.04 - 0.02) == R(0.023)
    # yen
    usd_j = mk.convert(1.5e9, 150.0, "JPY", "USD/JPY")
    assert usd_j == R(10e6)
    jpy = usd_j * 1.043 * f_jpy
    assert round(jpy) == 1_511_848_558
    assert round(jpy / 1.5e9 - 1, 5) == 0.00790
    assert round(jpy / 1.5e9 - 1 - 0.016, 4) == -0.0081
    # unhedged euro at 1.15
    x = 1.10 / 1.15 - 1
    assert round(x, 5) == -0.04348
    un = mk.unhedged_foreign_return(0.043, x)
    assert round(un, 5) == -0.00235
    assert round(term / 1.15) == 9_976_522
    # break-evens
    be_eur = term / (10e6 * 1.026)
    assert round(be_eur, 4) == 1.1182
    assert round(be_eur / 1.10 - 1, 3) == 0.017  # dollar can weaken ~1.6-1.7%
    be_jpy = 1.5e9 * 1.016 / (usd_j * 1.043)
    assert round(be_jpy, 2) == 146.12
    assert round(1 - be_jpy / 150, 4) == 0.0259
    # Fed cut
    cut = hedged_return(0.043, 0.02, 0.03)
    assert round(cut, 5) == 0.03287
    assert round(cut - 0.026, 4) == 0.0069
    assert round(cut - 0.026 - (h - 0.026), 2) == 0.01
    # spreads quoted in the decision consequence
    assert 0.043 - 0.026 == R(0.017) and 0.043 - 0.016 == R(0.027)
    # check: hedged equals unhedged at S_T = F
    assert term / f_eur == R(eur)


# --------------------------------------------------------------------------
# Example 7.6
# --------------------------------------------------------------------------

def test_example_7_6():
    f = mk.covered_interest_forward(1.10, 0.04, 0.02, 1)
    eq = mk.convert(60e6, 1.10, "USD", "EUR/USD")
    assert round(eq) == 54_545_455
    end_usd = 60e6 * (1 + 0.055)
    assert end_usd == R(63.3e6)
    hedged = mk.convert(end_usd, f, "USD", "EUR/USD")
    assert round(hedged) == 56_438_811
    assert round(hedged / eq - 1, 5) == 0.03471
    assert hedged / eq - 1 == R(hedged_return(0.055, 0.02, 0.04))
    assert round(hedged / eq - 1 - 0.045, 4) == -0.0103
    loss = end_usd / 1.00 - hedged
    assert round(loss) == 6_861_189
    assert round(loss / eq, 4) == 0.1258
    assert mk.unhedged_foreign_return(0.055, 1.10 / 1.00 - 1) == R(0.1605)
    eq_l = mk.convert(30e6, 1.10, "USD", "EUR/USD")
    assert round(eq_l) == 27_272_727
    end_l = 30e6 + 3.3e6 - 30e6 * 0.06
    assert end_l == R(31.5e6)
    h_l = mk.convert(end_l, f, "USD", "EUR/USD")
    assert round(h_l) == 28_085_664
    assert round(h_l / eq_l - 1, 5) == 0.02981
    # hedge cost on equity ~1.9%
    assert round(1 - 1.02 / 1.04, 4) == 0.0192


# --------------------------------------------------------------------------
# Example 7.7
# --------------------------------------------------------------------------

def test_example_7_7():
    loss = 12 * 5.0 * 0.025
    assert loss == R(1.5)
    e1, a1 = 6.0 - loss, 100 - loss
    assert (e1, a1) == (R(4.5), R(98.5))
    assert round(e1 / a1, 4) == 0.0457
    a_max = e1 / 0.06
    assert a_max == R(75.0)
    shrink = a1 - a_max
    assert shrink == R(23.5)
    assert round(shrink / a1, 3) == 0.239
    nonsov = a1 - (12 - loss)
    assert nonsov == R(88.0)
    assert round(15 / nonsov, 4) == 0.1705
    cre_cut = shrink * 15 / nonsov
    assert round(cre_cut, 2) == 4.01
    assert round(cre_cut / 15, 3) == 0.267
    assert round(shrink / nonsov, 3) == 0.267
    assert 0.5 * 250 == 125
    assert 10 * (0.05 - 0.01) == R(0.40)
    assert round(loss / 6.0, 2) == 0.25 and round(1 / 0.06, 1) == 16.7


# --------------------------------------------------------------------------
# Example 7.8
# --------------------------------------------------------------------------

def test_example_7_8():
    r = cre.value_change_from_cap_and_noi(4.0e6, 0.05, -0.05, 0.06)
    assert r["v0"] == R(80e6) and r["noi1"] == R(3.8e6)
    assert round(r["v1"]) == 63_333_333
    assert round(r["pct_change"], 4) == -0.2083
    lv = cre.levered_equity_change(r["v0"], r["v1"], 52e6)
    assert lv["e0"] == R(28e6) and round(lv["e1"]) == 11_333_333
    assert round(lv["pct_change"], 4) == -0.5952
    assert round(lv["ltv1"], 3) == 0.821
    k = tvm.loan_constant(0.07, 25)
    assert round(k, 6) == 0.084814
    ml = cre.max_loan(r["noi1"], r["v1"], 0.07, 25, ltv_max=0.60, dscr_min=1.30, debt_yield_min=0.09)
    assert ml["ltv"] == R(38e6)
    assert round(ml["debt_yield"]) == 42_222_222
    assert round(ml["dscr"]) == 34_464_759
    assert ml["binding"] == "dscr"
    gap = cre.refinance_gap(52e6, ml["max_loan"], 0.01 * ml["max_loan"])
    assert round(gap) == 17_879_889
    ds = ml["max_loan"] * k
    assert round(ds) == 2_923_077
    assert cre.dscr(r["noi1"], ds) == R(1.30)


# --------------------------------------------------------------------------
# CRE application table (Section 7.6)
# --------------------------------------------------------------------------

def test_section_7_6_table():
    eur = hedged_return(0.055, 0.02, 0.04)
    jpy = hedged_return(0.055, 0.005, 0.04)
    assert round(eur, 4) == 0.0347 and round(jpy, 4) == 0.0195
    assert round(eur - 0.045, 4) == -0.0103
    assert round(jpy - 0.035, 4) == -0.0155
    assert round(1 - 1.02 / 1.04, 3) == 0.019
    assert round(1 - 1.005 / 1.04, 3) == 0.034


# --------------------------------------------------------------------------
# Problems
# --------------------------------------------------------------------------

def test_problem_7_1():
    assert round(pb_star(1.30, 0.025, 0.040), 5) == -0.01875
    assert round(pb_star(0.60, 0.070, 0.030), 5) == 0.02330
    assert round(1.30 / 1.04, 2) == 1.25


def test_problem_7_3():
    assert round(pb_star(0.90, 0.045, 0.035), 5) == 0.00870
    assert round(0.90 * 1.045 / 1.035, 4) == 0.9087
    assert round(0.90 * 1.045 / 1.035 + 0.02, 4) == 0.9287


def test_problem_7_4():
    assert 0.03 / 0.60 == R(0.05)
    assert round(1 - math.exp(-0.25), 4) == 0.2212
    assert 0.03 / 0.75 == R(0.04)
    assert round(1 - math.exp(-0.20), 4) == 0.1813


def test_problem_7_5():
    f = mk.covered_interest_forward(0.88, 0.0025, 0.04, 1)
    assert round(f, 6) == 0.848269
    h = 1.043 * f / 0.88 - 1
    assert round(h, 5) == 0.00539
    assert round(h - 0.007, 4) == -0.0016
    be = 0.88 * 1.007 / 1.043
    assert round(be, 6) == 0.849626
    assert round(1 - be / 0.88, 4) == 0.0345
    r_usd = 1.043 * 1.0025 / 1.007 - 1
    assert round(r_usd, 5) == 0.03834
    f3 = mk.covered_interest_forward(0.88, 0.0025, 0.04, 0.25)
    assert round(f3, 6) == 0.871832
    assert round(f3 / 0.88 - 1, 6) == -0.009282
    assert round((f3 / 0.88) ** 4 - 1, 5) == -0.03661
    assert round(f / 0.88 - 1, 5) == -0.03606
    assert round(((f / 0.88 - 1) - ((f3 / 0.88) ** 4 - 1)) * 1e4, 1) == 5.6


def test_problem_7_6():
    rates, r = [], 0.025
    for _ in range(5):
        r = r + 0.2 * (0.05 - r)
        rates.append(r)
    assert [round(x, 5) for x in rates] == [0.03, 0.034, 0.0372, 0.03976, 0.04181]
    grad = debt_path(1.2, rates, 0.035, -0.01)
    inst = debt_path(1.2, [0.05] * 5, 0.035, -0.01)
    none = debt_path(1.2, [0.025] * 5, 0.035, -0.01)
    assert [round(x, 4) for x in grad] == [1.2, 1.2042, 1.2130, 1.2256, 1.2413, 1.2594]
    assert [round(x, 4) for x in inst] == [1.2, 1.2274, 1.2552, 1.2834, 1.3120, 1.3410]
    assert [round(x, 4) for x in none] == [1.2, 1.1984, 1.1968, 1.1953, 1.1937, 1.1922]
    assert round((grad[5] - none[5]) * 100, 1) == 6.7
    assert round((inst[5] - grad[5]) * 100, 1) == 8.2
    assert round((rates[-1] - 0.025) / 0.025, 2) == 0.67
    assert round(pb_star(1.2, 0.03, 0.035), 5) == -0.00580
    assert round(pb_star(1.2, 0.05, 0.035), 5) == 0.01739


def test_problem_7_7():
    assert (0.03 - 0.01) * 2000 == R(40.0)
    assert (0.23 - 0.22) + (-0.05) == R(-0.04)
    assert 0.0 - (-0.05) == R(0.05)  # S_p - I must reach +5% for CA = 0


def test_problem_7_8():
    loss = 9 * 4.0 * 0.03
    assert loss == R(1.08)
    e1, a1 = 3.6 - loss, 60 - loss
    assert (e1, a1) == (R(2.52), R(58.92))
    assert round(e1 / a1, 4) == 0.0428
    assert e1 / 0.06 == R(42.0)
    shrink = a1 - e1 / 0.06
    assert shrink == R(16.92)
    nonsov = a1 - (9 - loss)
    assert nonsov == R(51.0)
    assert round(shrink / nonsov, 3) == 0.332
    assert round(10 * shrink / nonsov, 2) == 3.32
    assert round(0.06 * a1 - e1, 4) == 1.0152
    assert 0.05 + 0.4 * 0.03 == R(0.062)
    k0, k1 = tvm.loan_constant(0.05, 25), tvm.loan_constant(0.062, 25)
    assert round(k0, 6) == 0.070151 and round(k1, 6) == 0.078790
    l0 = cre.max_loan(1e6, 1e9, 0.05, 25, dscr_min=1.25)["max_loan"]
    l1 = cre.max_loan(1e6, 1e9, 0.062, 25, dscr_min=1.25)["max_loan"]
    assert round(l0) == 11_404_003 and round(l1) == 10_153_592
    assert round(l1 / l0 - 1, 4) == -0.1096


def test_problem_7_9():
    f = mk.covered_interest_forward(150.0, 0.005, 0.04, 1)
    eq = mk.convert(40e6, 150.0, "USD", "USD/JPY")
    assert eq == R(6e9)
    h = 1.08 * f / 150 - 1
    assert round(h, 5) == 0.04365
    end = 43.2e6
    assert round(end * 165 / 1e6) == 7128
    assert round(end * f / 1e6, 1) == 6261.9
    loss = end * (165 - f)
    assert round(loss) == 866_076_923
    assert round(loss / eq, 4) == 0.1443
    un = mk.unhedged_foreign_return(0.08, 165 / 150 - 1)
    assert un == R(0.188)
    assert round(0.5 * h + 0.5 * un, 4) == 0.1158
    assert round(0.5 * loss / eq, 4) == 0.0722
    assert mk.unhedged_foreign_return(0.08, 135 / 150 - 1) == R(-0.028)
    assert round(end * (f - 135) / eq, 4) == 0.0717
    # hedge cost "about 3.4%"
    assert round(1 - 1.005 / 1.04, 3) == 0.034


def test_problem_7_10():
    price = 0.72 * 45e6
    assert price == R(32.4e6)
    assert round(4.1 / 45, 4) == 0.0911
    assert round(4.1 / 32.4, 4) == 0.1265
    assert round(45 / 58, 3) == 0.776
    assert round(4.1e6 / 0.09 / 1e6, 1) == 45.6
    assert round(4.1e6 / 0.11 / 1e6, 1) == 37.3


def test_decision_exercise_grid():
    grid = {c: (3.8e6 / c, 3.42e6 / c) for c in (0.06, 0.065, 0.07)}
    assert [round(v[0] / 1e6, 2) for v in grid.values()] == [63.33, 58.46, 54.29]
    assert [round(v[1] / 1e6, 2) for v in grid.values()] == [57.00, 52.62, 48.86]
    assert 3.8e6 * 0.9 == R(3.42e6)
    loan_px = 0.65 * 52e6
    assert loan_px == R(33.8e6)
    assert round(loan_px / grid[0.07][1], 3) == 0.692


# --------------------------------------------------------------------------
# Boundary cases for the library functions used
# --------------------------------------------------------------------------

def test_boundaries():
    # equal rates: forward = spot, hedged = local return
    assert mk.covered_interest_forward(1.10, 0.03, 0.03, 1) == R(1.10)
    assert hedged_return(0.043, 0.03, 0.03) == R(0.043)
    # zero time: forward = spot
    assert mk.covered_interest_forward(150.0, 0.005, 0.04, 0) == R(150.0)
    # FX quote direction: converting there and back returns the original amount
    assert mk.convert(mk.convert(1e6, 1.10, "EUR", "EUR/USD"), 1.10, "USD", "EUR/USD") == R(1e6)
    # r = g: debt ratio rises exactly by the primary deficit
    assert debt_path(1.0, [0.04], 0.04, -0.02)[1] == R(1.02)
    assert pb_star(1.0, 0.04, 0.04) == 0
    # unhedged with no FX move equals local return
    assert mk.unhedged_foreign_return(0.05, 0.0) == R(0.05)
    with pytest.raises(ValueError):
        mk.convert(1.0, 1.10, "JPY", "EUR/USD")
