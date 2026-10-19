"""Reproduces every number in Chapter 5 text, problems, and solutions.

Independent routes are used where possible: closed forms are checked against
library functions, futures probabilities against zero-expected-P&L, and loan
sizing against reconstructed debt service.
"""

import pytest

from sdesk import cre, fixed_income as fi, tvm

R = pytest.approx
ACT360 = 365 / 360
FF_BP_VALUE = 41.67   # $ per bp per 30-Day Fed Funds contract ($4,167 per index point)


def taylor(rstar, pi, gap, a=0.5, b=0.5, target=2.0):
    return rstar + pi + a * (pi - target) + b * gap


def post_meeting_rate(price, n_days, pre_days, r0):
    avg = 100 - price
    return avg, (n_days * avg - pre_days * r0) / (n_days - pre_days)


def float_interest(loan, rate):
    return loan * rate * ACT360


# ------------------------------------------------------------------ text examples
def test_example_5_1():
    daily = 1e9 * (0.0390 - 0.0386) / 360
    assert daily == R(1_111.11, abs=0.01)
    assert daily * 365 == R(405_556, abs=1)
    # corridor settings (16 Sep 2026): IORB 15 bp above bottom, ON RRP at bottom, SRF at top
    lo, hi, iorb, onrrp, srf = 3.75, 4.00, 3.90, 3.75, 4.00
    assert round(iorb - lo, 2) == 0.15 and onrrp == lo and srf == hi
    assert 0.0388 + 0.03 == R(0.0688)


def test_example_5_2():
    assert taylor(2.0, 3.0, -0.5) == R(5.25)
    assert taylor(0.75, 3.0, -0.5) == R(4.00)
    assert taylor(2.0, 3.0, -0.5, b=1.0) == R(5.00)
    assert taylor(0.75, 3.0, -0.5, b=1.0) == R(3.75)
    assert 0.85 * 3.875 + 0.15 * 4.00 == R(3.89375)
    assert 0.85 * 3.875 + 0.15 * 5.25 == R(4.08125)
    # band width and step size
    assert 5.25 - 3.75 == R(1.50)
    assert 0.15 * (5.25 - 3.875) == R(0.20625)


def test_example_5_3():
    assert 0.043 - 0.019 == R(0.024)
    assert 1.043 / 1.019 - 1 == R(0.023553, abs=1e-6)
    k = 0.06 + 0.024
    real_k = (1 + k) / 1.024 - 1
    assert real_k == R(0.0585938, abs=1e-7)
    prem = real_k - 0.019
    assert prem == R(0.0395938, abs=1e-7)
    assert 1.019 * (1 + prem) * 1.024 == R(1.0848, abs=1e-4)
    # 1-point NOI growth shortfall -> premium falls ~1 point
    k2 = 0.06 + 0.014
    assert (1 + k2) / 1.024 - 1 - 0.019 == R(0.0298, abs=1e-4)


def test_example_5_4():
    avg, r1 = post_meeting_rate(96.040, 30, 16, 3.88)
    assert avg == R(3.96)
    assert r1 == R(4.05143, abs=1e-5)
    p = (r1 - 3.88) / 0.25
    assert p == R(0.685714, abs=1e-6)
    assert (avg - 3.88) / 0.25 == R(0.32)
    assert (100 - 95.950 - 3.88) / 0.25 == R(0.68)
    settle_hike = 100 - (16 * 3.88 + 14 * 4.13) / 30
    assert settle_hike == R(96.00333, abs=1e-5)
    gain = (96.040 - settle_hike) * 100 * FF_BP_VALUE * 100
    loss = (96.040 - (100 - 3.88)) * 100 * FF_BP_VALUE * 100
    assert gain == R(15_279, abs=1)
    assert loss == R(-33_336, abs=1)
    assert p * gain + (1 - p) * loss == R(0, abs=1)   # zero EV at market-implied probability


def test_example_5_5():
    f = fi.forward_rate(0.038, 1, 0.036, 2)
    assert f == R(0.034004, abs=1e-6)
    assert f - 0.001 == R(0.033004, abs=1e-6)
    assert 1.038 * (1 + f) == R(1.036 ** 2)


def test_example_5_6():
    L, noi = 30e6, 2.4e6
    i_lo = float_interest(L, 0.0005 + 0.03)
    i_hi = float_interest(L, 0.053 + 0.03)
    i_cap = float_interest(L, 0.03 + 0.03)
    assert (round(i_lo), round(i_hi), round(i_cap)) == (927_708, 2_524_583, 1_825_000)
    assert (round(noi / i_lo, 2), round(noi / i_hi, 2), round(noi / i_cap, 2)) == (2.59, 0.95, 1.32)
    assert noi / (L * ACT360) - 0.03 == R(0.048904, abs=1e-6)
    assert L * 0.083 == R(2_490_000)
    assert i_hi - L * 0.083 == R(34_583, abs=1)
    assert i_hi / (L * 0.083) == R(365 / 360)


def test_example_5_7():
    noi = 2.4e6
    k_lo, k_hi = tvm.loan_constant(0.0325, 30), tvm.loan_constant(0.065, 30)
    assert (round(k_lo, 6), round(k_hi, 6)) == (0.052225, 0.075848)
    lo = cre.max_loan(noi, noi / 0.05, 0.0325, 30, ltv_max=0.65, dscr_min=1.25, debt_yield_min=0.08)
    hi = cre.max_loan(noi, noi / 0.06, 0.065, 30, ltv_max=0.65, dscr_min=1.25, debt_yield_min=0.08)
    assert (lo["ltv"], round(lo["dscr"]), lo["debt_yield"]) == (R(31_200_000), 36_764_172, R(30_000_000))
    assert lo["binding"] == "debt_yield" and lo["max_loan"] == R(30_000_000)
    assert (hi["ltv"], round(hi["dscr"])) == (R(26_000_000), 25_313_731)
    assert hi["binding"] == "dscr"
    assert 1 - hi["dscr"] / lo["dscr"] == R(0.311, abs=5e-4)
    assert 1 - hi["max_loan"] / lo["max_loan"] == R(0.156, abs=5e-4)
    gap = cre.refinance_gap(30e6, hi["max_loan"], 0.01 * 30e6)
    assert round(gap) == 4_986_269
    assert gap / 30e6 == R(0.166, abs=1e-3)
    # independent check: DS at max loan gives exactly 1.25x
    ds = tvm.annual_debt_service(hi["max_loan"], 0.065, 30)
    assert ds == R(1_920_000, abs=0.5) and noi / ds == R(1.25)
    assert k_hi / k_lo - 1 == R(0.452, abs=5e-4)


def test_constant_elasticities_section_5_4_6():
    def el(c, h=1e-6):
        dk = (tvm.loan_constant(c + h, 30) - tvm.loan_constant(c - h, 30)) / (2 * h)
        return dk * c / tvm.loan_constant(c, 30)
    assert (round(el(0.06), 2), round(el(0.065), 2), round(el(0.07), 2)) == (0.64, 0.68, 0.71)
    assert round(el(0.065), 3) == 0.676
    # 10% proportional coupon rise -> ~6.8% fewer DSCR proceeds
    p0 = 1 / tvm.loan_constant(0.065, 30)
    p1 = 1 / tvm.loan_constant(0.0715, 30)
    assert 1 - p1 / p0 == R(0.0657, abs=2e-3)


def test_example_5_8():
    assert 0.043 - 0.034 == R(0.009)
    d = fi.dv01(0.043, 0.043, 10, 100)
    assert d == R(0.08059, abs=1e-5)
    assert -d * 20 == R(-1.612, abs=1e-3)
    full = fi.bond_price(0.045, 0.043, 10) - 100
    assert full == R(-1.596, abs=1e-3)
    assert full - (-d * 20) == R(0.016, abs=1e-3)
    assert cre.cap_rate_shock_pct(0.06, 0.061) == R(-0.016393, abs=1e-6)


# ------------------------------------------------------------------ problems
def test_problem_5_2():
    assert 100 - 96.18 == R(3.82)
    assert (3.88 - 3.82) / 0.25 == R(0.24)
    assert 4167 / 100 == R(41.67)


def test_problem_5_3():
    assert 0.045 - 0.023 == R(0.022)
    assert 1.045 / 1.023 - 1 == R(0.021505, abs=1e-6)


def test_problem_5_4():
    assert taylor(1.0, 2.6, 0.5) == R(4.15)
    assert taylor(1.0, 2.6, 0.5, b=1.0) == R(4.40)
    assert taylor(1.0, 3.2, 0.5) == R(5.05)
    assert 0.8 * 3.875 + 0.2 * 4.15 == R(3.93)


def test_problem_5_5():
    avg, r1 = post_meeting_rate(96.07, 31, 17, 3.88)
    assert avg == R(3.93)
    assert r1 == R(3.99071, abs=1e-5)
    assert (r1 - 3.88) / 0.25 == R(0.4429, abs=1e-4)
    assert (avg - 3.88) / 0.25 == R(0.20)
    assert (r1 - 3.88) / 0.50 == R(0.2214, abs=1e-4)


def test_problem_5_6():
    L, noi = 45e6, 4e6
    a = float_interest(L, 0.0385 + 0.035)
    b = float_interest(L, 0.0435 + 0.035)
    c = float_interest(L, 0.0425 + 0.035)
    assert (a, b, c) == (R(3_353_438, abs=1), R(3_581_563, abs=1), R(3_535_938, abs=1))
    assert (round(noi / a, 3), round(noi / b, 3), round(noi / c, 3)) == (1.193, 1.117, 1.131)
    assert float_interest(L, 0.0435 - 0.0425) == R(45_625)


def test_problem_5_7():
    noi = 1.8e6
    v = noi / 0.0625
    assert v == R(28_800_000)
    a = cre.max_loan(noi, v, 0.061, 30, ltv_max=0.6, dscr_min=1.3, debt_yield_min=0.09)
    b = cre.max_loan(noi, v, 0.0675, 30, ltv_max=0.6, dscr_min=1.3, debt_yield_min=0.09)
    assert round(tvm.loan_constant(0.061, 30), 6) == 0.072719
    assert round(tvm.loan_constant(0.0675, 30), 6) == 0.077832
    assert (a["ltv"], round(a["dscr"]), a["debt_yield"], a["binding"]) == (R(17_280_000), 19_040_529, R(20_000_000), "ltv")
    assert (round(b["dscr"]), b["max_loan"], b["binding"]) == (17_789_848, R(17_280_000), "ltv")
    assert a["dscr"] - a["ltv"] == R(1_760_529, abs=1)
    assert b["dscr"] - b["ltv"] == R(509_848, abs=1)
    c = cre.max_loan(noi, noi / 0.0675, 0.0675, 30, ltv_max=0.6, dscr_min=1.3, debt_yield_min=0.09)
    assert noi / 0.0675 == R(26_666_667, abs=1)
    assert c["max_loan"] == R(16_000_000) and c["binding"] == "ltv"
    assert 1 - c["max_loan"] / a["max_loan"] == R(0.074, abs=5e-4)


def test_problem_5_8():
    vals = [2e6 / c for c in (0.055, 0.05625, 0.0575)]
    assert [round(v) for v in vals] == [36_363_636, 35_555_556, 34_782_609]
    assert cre.cap_rate_shock_pct(0.055, 0.05625) == R(-0.0222, abs=1e-4)
    assert cre.cap_rate_shock_pct(0.055, 0.0575) == R(-0.0435, abs=1e-4)
    assert all(v < 36_000_000 for v in vals[1:])


def test_problem_5_9():
    L, noi = 25e6, 2.2e6
    out = {s: float_interest(L, s + 0.03) for s in (0.036, 0.0335, 0.0388)}
    assert [round(out[s]) for s in (0.036, 0.0335, 0.0388)] == [1_672_917, 1_609_549, 1_743_889]
    assert [round(noi / out[s], 3) for s in (0.036, 0.0335, 0.0388)] == [1.315, 1.367, 1.262]
    trig = noi / (1.15 * L * ACT360) - 0.03
    assert trig == R(0.04547, abs=1e-5)
    assert trig - 0.0388 == R(0.0067, abs=1e-4)


def test_decision_exercise_numbers():
    L, noi = 30e6, 2.4e6
    a = float_interest(L, 0.0388 + 0.035)
    b = float_interest(L, 0.0488 + 0.035)
    assert round(a) == 2_244_750 and round(noi / a, 3) == 1.069
    assert round(b) == 2_548_917 and round(noi / b, 3) == 0.942
    assert noi / (L * ACT360) - 0.035 == R(0.04390, abs=1e-5)
