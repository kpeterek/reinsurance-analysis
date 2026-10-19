"""Reproduces every number in Chapter 4 (The Business Cycle): text, problems, solutions.

Historical figures quoted in §4.9 are checked for internal arithmetic consistency
(e.g. STR occupancy x ADR ~ RevPAR) -- the figures themselves come from the sources
in references/sources_ch04.md, not from this file.
"""

import datetime as dt

import pytest

from sdesk import cre, fixed_income as fi, stats, tvm
from sdesk import x_business_cycle as bc

R = pytest.approx


# --------------------------------------------------------------------------
# Library unit tests (new module x_business_cycle)
# --------------------------------------------------------------------------

def test_annualization_round_trip_and_bounds():
    for q in (-0.03, -0.004, 0.0, 0.006, 0.02):
        a = bc.annualize_quarterly(q)
        assert bc.quarterly_from_annualized(a) == R(q)
        # compounding: 4q understates positive, overstates (in magnitude... less negative) negative
        assert a >= bc.simple_annualized(q) - 1e-15
    assert bc.annualize_quarterly(0.0) == 0.0
    assert bc.annualize_quarterly(0.01) == R(tvm.annualize_periodic(0.01, 4))


def test_contributions_sum_to_growth():
    r = bc.contributions({"a": 50, "b": 30, "c": 20}, {"a": 51, "b": 27, "c": 21})
    assert r["a"] + r["b"] + r["c"] == R(r["gdp_growth"])


def test_sahm_needs_full_window_and_flat_series_is_zero():
    s = bc.sahm_indicator([4.0] * 20)
    assert s[:14] == [None] * 14
    assert all(v == R(0.0) for v in s[14:])
    assert bc.sahm_first_trigger(s) is None


def test_net_percentage_bounds():
    assert bc.net_percentage(10, 0, 0, 0, 10) == 1.0
    assert bc.net_percentage(0, 0, 0, 10, 10) == -1.0
    assert bc.net_percentage(0, 0, 0, 0, 10) == 0.0


def test_lease_rollover_no_roll_no_change():
    r = bc.lease_rollover_noi(1_000_000, 400_000, 0.0, -0.2, 0.5, 6)
    assert r["noi1"] == R(600_000) and r["pct_change"] == R(0.0)


# --------------------------------------------------------------------------
# Worked examples
# --------------------------------------------------------------------------

EX41_PREV = {"C": 15_000, "I": 3_600, "G": 3_900, "NX": -700}
EX41_CURR = {"C": 15_075, "I": 3_168, "G": 3_958.5, "NX": -600}


def test_example_4_1():
    assert sum(EX41_PREV.values()) == 21_800
    shares = {k: v / 21_800 for k, v in EX41_PREV.items()}
    assert round(100 * shares["C"], 2) == 68.81
    assert round(100 * shares["I"], 2) == 16.51
    assert round(100 * shares["G"], 2) == 17.89
    assert round(100 * shares["NX"], 2) == -3.21
    assert EX41_CURR["C"] == R(15_000 * 1.005)
    assert EX41_CURR["I"] == R(3_600 * 0.88)
    assert EX41_CURR["G"] == R(3_900 * 1.015)
    r = bc.contributions(EX41_PREV, EX41_CURR)
    assert r["gdp1"] == R(21_601.5)
    assert round(100 * r["gdp_growth"], 2) == -0.91
    assert round(100 * r["C"], 2) == 0.34
    assert round(100 * r["I"], 2) == -1.98
    assert round(100 * r["G"], 2) == 0.27
    assert round(100 * r["NX"], 2) == 0.46
    # investment's contribution is more than twice the size of the GDP decline
    assert abs(r["I"]) / abs(r["gdp_growth"]) == R(2.176, abs=0.001)
    # imports fell: NX rose by 100 although exports may have been flat
    assert EX41_CURR["NX"] - EX41_PREV["NX"] == 100


EX42 = [22_000, 22_110, 22_143, 22_121, 22_066]


def test_example_4_2():
    q = [EX42[t] / EX42[t - 1] - 1 for t in range(1, 5)]
    assert [round(100 * x, 2) for x in q] == [0.50, 0.15, -0.10, -0.25]
    ann = [bc.annualize_quarterly(x) for x in q]
    assert [round(100 * x, 2) for x in ann] == [2.02, 0.60, -0.40, -0.99]
    simple = [bc.simple_annualized(x) for x in q]
    assert round(100 * simple[0], 2) == 2.00
    assert round(100 * simple[3], 2) == -0.99  # -0.9945 displays as -0.99
    assert round(100 * (ann[0] - simple[0]), 3) == 0.015
    assert round(100 * bc.yoy_growth(EX42, 4), 2) == 0.30
    # YoY equals the compound of the four quarterly rates
    prod = 1.0
    for x in q:
        prod *= 1 + x
    assert prod - 1 == R(bc.yoy_growth(EX42, 4))
    # two consecutive negative quarters while YoY is still positive
    assert q[2] < 0 and q[3] < 0 and bc.yoy_growth(EX42, 4) > 0


def test_example_4_3():
    prod = 1.024 / 1.009 - 1
    assert round(100 * prod, 2) == 1.49
    ulc = 1.045 / (1 + prod) - 1
    assert round(100 * ulc, 2) == 2.97
    assert round(100 * (0.045 - prod), 2) == 3.01  # additive approximation
    lab = 0.36 * 1.045 / 1.01 / 1.025
    assert round(100 * lab, 2) == 36.34
    assert round(100 * (lab - 0.36), 2) == 0.34


EX44 = [3.6, 3.5, 3.5, 3.5, 3.6, 3.5, 3.6, 3.6, 3.7, 3.7, 3.8, 3.8,
        3.9, 3.9, 4.0, 4.1, 4.1, 4.2, 4.3, 4.4]


def test_example_4_5():
    ma = bc.moving_average(EX44)
    assert ma[2] == R(3.5333, abs=1e-4)
    assert ma[3] == R(3.5)
    assert ma[14] == R(3.9333, abs=1e-4)
    assert ma[15] == R(4.0)
    s = bc.sahm_indicator(EX44)
    assert s[13] is None
    assert s[14] == R(0.4333, abs=1e-4)
    assert s[15] == R(0.50)
    assert s[16] == R(0.5333, abs=1e-4)
    assert s[19] == R(0.7333, abs=1e-4)
    assert bc.sahm_first_trigger(s) == 15        # month 16
    # the minimum used at month 16 is month 4's average (window months 4..15)
    assert min(ma[3:15]) == R(3.5)
    # revision: month 4 revised from 3.5 to 3.6 delays the trigger one month
    rev = list(EX44)
    rev[3] = 3.6
    s2 = bc.sahm_indicator(rev)
    assert s2[15] == R(0.4667, abs=1e-4)
    assert s2[16] == R(0.50)
    assert bc.sahm_first_trigger(s2) == 16       # month 17
    # including the current month in the minimum makes no difference while rising
    s3 = bc.sahm_indicator(EX44, include_current=True)
    assert bc.sahm_first_trigger(s3) == 15


def test_example_4_6():
    assert round(stats.bayes_posterior(0.15, 0.90, 0.10), 3) == 0.614
    assert round(stats.bayes_posterior(0.15, 0.90, 0.20), 3) == 0.443
    assert round(stats.bayes_posterior(0.30, 0.90, 0.10), 3) == 0.794
    assert round(stats.bayes_posterior(0.05, 0.90, 0.10), 3) == 0.321
    # odds form agrees
    assert stats.likelihood_ratio_update(0.15, 9.0) == R(stats.bayes_posterior(0.15, 0.90, 0.10))
    # joint probabilities used in the 1,000-quarters table
    assert 1000 * 0.15 * 0.90 == R(135)
    assert 1000 * 0.85 * 0.10 == R(85)
    assert 135 / (135 + 85) == R(0.6136, abs=1e-4)


def test_example_4_7():
    z_head = bc.standardized_surprise(40, 180, 75)
    assert round(z_head, 2) == -1.87
    z = bc.standardized_surprise(40 - 60, 180, 75)
    assert round(z, 3) == -2.667
    moves = {k: b * z for k, b in {"2y": 5.0, "5y": 4.5, "10y": 3.5}.items()}
    assert round(moves["2y"], 1) == -13.3
    assert round(moves["5y"], 1) == -12.0
    assert round(moves["10y"], 1) == -9.3
    assert round(moves["10y"] - moves["2y"], 1) == 4.0          # bull steepening
    p = fi.bond_price(0.042, 0.04, 10)
    assert round(p, 2) == 98.38
    md = fi.modified_duration(0.042, 0.04, 10)
    assert round(md, 2) == 8.15
    dy = moves["10y"] / 10_000
    approx = fi.price_change_approx(p, md, fi.convexity(0.042, 0.04, 10), dy)["total"]
    exact = fi.bond_price(0.042 + dy, 0.04, 10) - p
    assert round(exact, 2) == 0.75 and approx == R(exact, abs=1e-3)
    assert 25_000_000 * 4.5 * abs(z) / 10_000 == R(30_000)


def test_example_4_4():
    assert bc.net_percentage(6, 20, 4, 0, 64) == R(0.34375)
    noi = 2_000_000
    v0 = noi / 0.07
    a = cre.max_loan(noi, v0, 0.065, 30, ltv_max=0.65, dscr_min=1.25, debt_yield_min=0.085)
    assert round(v0) == 28_571_429
    assert round(a["ltv"]) == 18_571_429
    assert round(a["dscr"]) == 21_094_776
    assert round(a["debt_yield"]) == 23_529_412
    assert a["binding"] == "ltv"
    assert round(tvm.loan_constant(0.065, 30), 4) == 0.0758
    assert round(tvm.loan_constant(0.0725, 30), 4) == 0.0819
    noi2 = noi * 0.95
    v1 = noi2 / 0.0775
    assert round(v1) == 24_516_129
    b = cre.max_loan(noi2, v1, 0.0725, 30, ltv_max=0.60, dscr_min=1.40, debt_yield_min=0.10)
    assert round(b["ltv"]) == 14_709_677
    assert round(b["dscr"]) == 16_578_594
    assert round(b["debt_yield"]) == 19_000_000
    assert b["binding"] == "ltv"
    assert round(cre.refinance_gap(18_000_000, a["max_loan"])) == -571_429
    assert round(cre.refinance_gap(18_000_000, b["max_loan"])) == 3_290_323
    # proceeds decline
    assert round(100 * (b["max_loan"] / a["max_loan"] - 1), 1) == -20.8


def test_example_4_8():
    h = cre.operating_leverage(10_000_000, 3_600_000, 0.34, -0.17)
    assert h["noi0"] == R(3_000_000)
    assert h["noi1"] == R(1_878_000)
    assert round(100 * h["pct_change"], 1) == -37.4
    assert round(h["dol"], 2) == 2.20
    cut = 8_300_000 * 0.66 - 3_600_000 * 0.92
    assert cut == R(2_166_000)
    assert round(100 * (cut / 3_000_000 - 1), 1) == -27.8
    apt = bc.lease_rollover_noi(5_000_000, 2_000_000, 0.5, -0.06, 0.55, 1, -0.02)
    assert apt["rev1"] == R(4_661_875)
    assert round(100 * apt["pct_change"], 1) == -11.3
    off = bc.lease_rollover_noi(8_000_000, 3_200_000, 0.12, -0.15, 0.5, 9, 0.0)
    assert off["rev1"] == R(7_550_000)
    assert round(100 * off["pct_change"], 1) == -9.4
    ind = bc.lease_rollover_noi(4_000_000, 600_000, 0.15, -0.05, 0.7, 4, 0.0)
    assert ind["rev1"] == R(3_913_000)
    assert round(100 * ind["pct_change"], 1) == -2.6
    # office: once all leases have rolled (renewal 50%, 9 months downtime once), the
    # steady-state revenue loss is the full 15% market-rent decline
    steady = 8_000_000 * 0.85 - 3_200_000
    assert round(100 * (steady / 4_800_000 - 1), 1) == -25.0
    # ordering: hotel first and largest
    assert h["pct_change"] < apt["pct_change"] < off["pct_change"] < ind["pct_change"]


# --------------------------------------------------------------------------
# Section 4.9 historical episode: arithmetic checks on sourced figures
# --------------------------------------------------------------------------

def test_history_gdp_revisions():
    # Q4 2008: advance -3.8% SAAR; 2011 annual revision -8.9% SAAR
    assert round(100 * bc.quarterly_from_annualized(-0.038), 2) == -0.96
    assert round(100 * bc.quarterly_from_annualized(-0.089), 2) == -2.30
    assert round(-8.9 - (-3.8), 1) == -5.1
    # Q3 2008 advance -0.3%, preliminary -0.5%
    assert round(100 * bc.quarterly_from_annualized(-0.003), 3) == -0.075
    # Q3 2001 advance -0.4% -> final -1.3%
    assert round(-1.3 - (-0.4), 1) == -0.9
    assert round(100 * bc.quarterly_from_annualized(-0.013), 2) == -0.33


def test_history_payroll_benchmark():
    assert round(100 * 902 / (131_175 + 902), 1) == 0.7
    assert round(902 - 824) == 78


def test_history_str_2009():
    # STR year-end 2009: occupancy 55.1% (-8.7%), ADR $97.51 (-8.8%), RevPAR $53.71 (-16.7%)
    assert round(0.551 * 97.51, 2) == 53.73                    # ~ 53.71 reported
    assert round(100 * ((1 - 0.087) * (1 - 0.088) - 1), 1) == -16.7
    assert round(100 * 0.551 / (1 - 0.087), 1) == 60.4          # implied 2008 occupancy
    assert round(97.51 / (1 - 0.088), 2) == 106.92               # implied 2008 ADR
    assert round(53.71 / (1 - 0.167), 2) == 64.48                # implied 2008 RevPAR


def _months(a, b):
    return (b.year - a.year) * 12 + (b.month - a.month)


def test_history_nber_announcement_lags():
    assert _months(dt.date(2007, 12, 1), dt.date(2008, 12, 1)) == 12
    assert _months(dt.date(2009, 6, 1), dt.date(2010, 9, 20)) == 15
    assert _months(dt.date(2001, 3, 1), dt.date(2001, 11, 26)) == 8
    assert _months(dt.date(2001, 11, 1), dt.date(2003, 7, 17)) == 20
    # recession lengths (peak to trough, months)
    assert _months(dt.date(2007, 12, 1), dt.date(2009, 6, 1)) == 18
    assert _months(dt.date(2001, 3, 1), dt.date(2001, 11, 1)) == 8


# --------------------------------------------------------------------------
# Problems
# --------------------------------------------------------------------------

def test_problem_4_2():
    assert round(100 * bc.annualize_quarterly(0.008), 2) == 3.24
    assert round(100 * bc.annualize_quarterly(-0.004), 2) == -1.59
    assert round(100 * bc.quarterly_from_annualized(0.024), 2) == 0.59
    ql = bc.quarterly_from_annualized(-0.02)
    assert round(100 * ql, 2) == -0.50
    assert round(100 * (1.01 / (1 + ql) - 1), 2) == 1.51


def test_problem_4_3():
    r = bc.contributions({"C": 68, "I": 17, "G": 17, "NX": -2},
                         {"C": 68 * 1.01, "I": 17 * 0.91, "G": 17 * 1.02, "NX": -2})
    assert round(100 * r["C"], 2) == 0.68
    assert round(100 * r["I"], 2) == -1.53
    assert round(100 * r["G"], 2) == 0.34
    assert round(100 * r["gdp_growth"], 2) == -0.51
    # break-even investment decline for zero GDP growth
    assert round(100 * (0.68 + 0.34) / 17, 1) == 6.0


P44 = [4.0, 3.9, 3.9, 3.8, 3.9, 3.9, 3.9, 4.0, 4.0, 4.1, 4.1, 4.2, 4.2, 4.3, 4.4, 4.4, 4.5, 4.6]


def test_problem_4_4():
    ma = bc.moving_average(P44)
    assert ma[3] == R(3.8667, abs=1e-4)
    assert ma[14] == R(4.3)
    assert ma[15] == R(4.3667, abs=1e-4)
    s = bc.sahm_indicator(P44)
    assert s[14] == R(0.4333, abs=1e-4)
    assert s[15] == R(0.50)
    assert s[17] == R(0.6333, abs=1e-4)
    assert bc.sahm_first_trigger(s) == 15        # month 16
    rev = list(P44)
    rev[3] = 3.9
    s2 = bc.sahm_indicator(rev)
    assert s2[15] == R(0.4667, abs=1e-4)
    assert s2[16] == R(0.5333, abs=1e-4)
    assert bc.sahm_first_trigger(s2) == 16       # month 17


def test_problem_4_5():
    prod = 1.012 / 1.015 - 1
    assert round(100 * prod, 2) == -0.30
    assert round(100 * (1.04 / (1 + prod) - 1), 2) == 4.31
    noi1 = 20_200_000 - 6_800_000 * 1.04 - 7_600_000
    assert noi1 == R(5_528_000)
    assert round(100 * (noi1 / 5_600_000 - 1), 2) == -1.29
    assert round(100 * 6_800_000 * 1.04 / 20_200_000, 2) == 35.01
    assert round(100 * noi1 / 20_200_000, 2) == 27.37


def test_problem_4_6():
    p1 = stats.bayes_posterior(0.12, 0.85, 0.15)
    assert round(p1, 3) == 0.436
    p2 = stats.bayes_posterior(p1, 0.80, 0.05)
    assert round(p2, 3) == 0.925
    assert round(0.85 / 0.15, 2) == 5.67 and 0.80 / 0.05 == R(16)
    # false-positive count over 40 non-recession years at a 15% annual false-positive rate
    assert 40 * 0.15 == R(6.0)


def test_problem_4_7():
    z = bc.standardized_surprise(0.4, 0.3, 0.08)
    assert round(z, 2) == 1.25
    assert round(5 * z, 2) == 6.25
    assert 40_000_000 * 5 * z / 10_000 == R(25_000)
    k0 = tvm.loan_constant(0.06, 30)
    k1 = tvm.loan_constant(0.060625, 30)
    assert round(k0, 5) == 0.07195
    assert round(k1, 5) == 0.07243
    l0 = 3_200_000 / 1.30 / k0
    l1 = 3_200_000 / 1.30 / k1
    assert round(l0) == 34_213_664
    assert round(l1 - l0) == -228_109


def test_problem_4_8():
    h = cre.operating_leverage(14_000_000, 5_000_000, 0.33, -0.15)
    assert h["noi0"] == R(4_380_000)
    assert h["noi1"] == R(2_973_000)
    assert round(100 * h["pct_change"], 1) == -32.1
    assert round(h["dol"], 2) == 2.14
    assert round(4_380_000 / 2_900_000, 2) == 1.51
    assert round(h["noi1"] / 2_900_000, 3) == 1.025
    # NOI at which the 1.20x covenant is just met
    assert 1.20 * 2_900_000 == R(3_480_000)
    apt = bc.lease_rollover_noi(6_000_000, 2_400_000, 0.5, -0.05, 0.55, 1, -0.015)
    off = bc.lease_rollover_noi(9_000_000, 3_600_000, 0.10, -0.12, 0.5, 9, 0.0)
    ind = bc.lease_rollover_noi(5_000_000, 750_000, 0.125, -0.04, 0.7, 4, 0.0)
    assert apt["noi1"] == R(3_253_125) and round(100 * apt["pct_change"], 1) == -9.6
    assert off["noi1"] == R(4_995_000) and round(100 * off["pct_change"], 1) == -7.5
    assert ind["noi1"] == R(4_165_000) and round(100 * ind["pct_change"], 1) == -2.0
    tot0 = 4_380_000 + 3_600_000 + 5_400_000 + 4_250_000
    tot1 = h["noi1"] + apt["noi1"] + off["noi1"] + ind["noi1"]
    assert tot0 == 17_630_000
    assert round(tot1) == 15_386_125
    assert round(100 * (tot1 / tot0 - 1), 1) == -12.7
    # hotel share of the portfolio NOI decline
    assert round(100 * (4_380_000 - h["noi1"]) / (tot0 - tot1), 1) == 62.7


def test_problem_4_9():
    assert round(100 * bc.net_percentage(9, 25, 2, 0, 68), 1) == 47.1
    noi1 = 3_000_000 * 0.92
    v1 = noi1 / 0.085
    a = cre.max_loan(noi1, v1, 0.0725, 30, ltv_max=0.60, dscr_min=1.35, debt_yield_min=0.10)
    assert round(v1) == 32_470_588
    assert round(a["ltv"]) == 19_482_353
    assert round(a["dscr"]) == 24_974_537
    assert round(a["debt_yield"]) == 27_600_000
    assert a["binding"] == "ltv"
    assert round(cre.refinance_gap(32_000_000, a["max_loan"])) == 12_517_647
    b = cre.max_loan(3_000_000, 3_000_000 / 0.065, 0.06, 30, ltv_max=0.65, dscr_min=1.25,
                     debt_yield_min=0.09)
    assert round(3_000_000 / 0.065) == 46_153_846
    assert round(b["max_loan"]) == 30_000_000
    # current LTV against the new value: the loan exceeds 98% of value
    assert round(100 * 32_000_000 / v1, 1) == 98.6
    # extension economics: paydown to reach 60% LTV at the new value
    assert round(32_000_000 - a["max_loan"]) == 12_517_647


# --------------------------------------------------------------------------
# Additional numbers quoted in the chapter prose
# --------------------------------------------------------------------------

def test_chapter_prose_numbers():
    # §4.1 opening problem: going-in cap on trailing NOI
    assert round(100 * 2_430_000 / 29_500_000, 2) == 8.24
    # §4.4.2 compounding gap 6q^2 + 4q^3 + q^4 at q = 0.5% is about 1.5 bp
    q = 0.005
    gap = bc.annualize_quarterly(q) - 4 * q
    assert gap == R(6 * q**2 + 4 * q**3 + q**4)
    assert round(gap * 10_000, 1) == 1.5
    # Example 4.1: other components offset more than half of the investment drag
    r = bc.contributions(EX41_PREV, EX41_CURR)
    assert round((r["C"] + r["G"] + r["NX"]) / -r["I"], 2) == 0.54
    # Example 4.3: ADR growth that holds the labor ratio; NOI effect at a 30% margin
    assert round(100 * (1.045 / 1.01 - 1), 2) == 3.47
    lab_change = 0.36 * 1.045 / 1.01 / 1.025 - 0.36
    assert round(100 * lab_change / 0.30, 1) == 1.1
    # Example 4.4: value decline and compounded proceeds decline
    v0, v1 = 2_000_000 / 0.07, 1_900_000 / 0.0775
    assert round(100 * (v1 / v0 - 1), 1) == -14.2
    assert round(100 * (0.60 / 0.65 * v1 / v0 - 1), 1) == -20.8
    # Example 4.6: odds-form check
    assert round(0.15 / 0.85, 4) == 0.1765
    assert round(0.15 / 0.85 * 9, 3) == 1.588
    # Example 4.7: headline vs effective surprise; duration and convexity terms
    z_h = bc.standardized_surprise(40, 180, 75)
    z_e = bc.standardized_surprise(-20, 180, 75)
    assert round(100 * (z_e / z_h - 1)) == 43
    assert round(100 * (1 - z_h / z_e)) == 30
    p = fi.bond_price(0.042, 0.04, 10)
    dy = 3.5 * z_e / 10_000
    pc = fi.price_change_approx(p, fi.modified_duration(0.042, 0.04, 10), fi.convexity(0.042, 0.04, 10), dy)
    assert round(pc["duration_term"], 3) == 0.748
    assert round(pc["total"], 3) == 0.752
    # Example 4.8: a 1.50x DSCR after a 37.4% NOI decline
    assert round(1.50 * (1 - 0.374), 2) == 0.94
    # hotel decline vs apartment decline (about four times)
    assert round(37.4 / 11.3, 1) == 3.3
    # §4.9: preliminary benchmark captured 91% of the final
    assert round(100 * 824 / 902) == 91
    # Sahm three-month average step size
    assert round(0.1 / 3, 4) == 0.0333


def test_solution_extras():
    # 4.2(a) mental-math correction term
    assert round(100 * 6 * 0.008**2, 2) == 0.04
    # 4.4(d) revised averages
    rev = list(P44)
    rev[3] = 3.9
    ma = bc.moving_average(rev)
    assert ma[2] == R(3.9333, abs=1e-4)
    assert ma[3] == R(3.9) and ma[4] == R(3.9) and ma[5] == R(3.9)
    assert min(ma[3:15]) == R(3.9)
    # 4.4(b) the original minimum is 3.8667 in every window used
    ma0 = bc.moving_average(P44)
    for t in (14, 15, 16, 17):
        assert min(ma0[t - 12:t]) == R(3.8667, abs=1e-4)
    # 4.5(a) intermediate
    assert round(1.012 / 1.015, 5) == 0.99704
    # 4.8 extras
    h = cre.operating_leverage(14_000_000, 5_000_000, 0.33, -0.15)
    assert round(14_000_000 * 0.67 / 1e6, 2) == 9.38
    assert round(100 * 4_380_000 / 17_630_000, 1) == 24.8
    assert round(100 * (1 - 3_480_000 / 4_380_000), 1) == 20.5
    assert round((4_380_000 - h["noi1"]) / 1e6, 3) == 1.407
    assert round(9.0 * 0.88 - 3.6, 2) == 4.32
    assert round(100 * (4.32 / 5.4 - 1), 1) == -20.0
    apt_parts = (3.0 * 0.55 * 0.95, 3.0 * 0.45 * 0.95 * 11 / 12)
    assert apt_parts == (R(1.5675), R(1.175625))
    # 4.9 extras
    assert round(100 * 32_000_000 / (3_000_000 / 0.065), 1) == 69.3
    assert round(tvm.loan_constant(0.0725, 30), 5) == 0.08186
    assert round(100 * 12_517_647 / 32_470_588) == 39
    b = cre.max_loan(3_000_000, 3_000_000 / 0.065, 0.06, 30, ltv_max=0.65, dscr_min=1.25,
                     debt_yield_min=0.09)
    assert round(b["dscr"] / 1e6, 2) == 33.36 and round(b["debt_yield"] / 1e6, 2) == 33.33
    # 4.10 illustrative posterior
    lr = 1.5 * 1.3 * 2 * 2 * 0.8 * 1.5
    assert lr == R(9.36)
    assert round(0.15 / 0.85 * lr, 3) == 1.652
    assert round(100 * stats.likelihood_ratio_update(0.15, lr), 1) == 62.3
    assert round(lr ** 0.5, 2) == 3.06
    assert round(100 * stats.likelihood_ratio_update(0.15, lr ** 0.5), 1) == 35.1


def test_decision_exercise():
    rev = 2_430_000 / 0.30
    assert rev == R(8_100_000)
    fixed = rev * 0.66 - 2_430_000
    assert fixed == R(2_916_000)
    h = cre.operating_leverage(rev, fixed, 0.34, -0.15)
    assert h["noi1"] == R(1_628_100)
    assert round(100 * h["pct_change"], 1) == -33.0
    assert round(h["dol"], 2) == 2.20
    loan = 0.65 * 29_500_000
    assert loan == R(19_175_000)
    ds = loan * 0.0775
    assert round(ds) == 1_486_063 or round(ds) == 1_486_062
    assert round(2_430_000 / ds, 2) == 1.64
    assert round(h["noi1"] / ds, 2) == 1.10
    assert round(100 * 2_430_000 / loan, 1) == 12.7
    assert round(100 * h["noi1"] / loan, 1) == 8.5
    assert round(100 * (1.04**2 - 1), 2) == 8.16
    assert round(100 * stats.likelihood_ratio_update(0.15, 9 * 2), 1) == 76.1
    assert round(100 * stats.likelihood_ratio_update(0.15, 4.5 * 2), 1) == 61.4
    # effective payroll surprise on the dashboard
    assert (95_000 - 150_000) + (-70_000) == -125_000
