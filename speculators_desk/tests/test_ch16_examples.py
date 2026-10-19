"""Reproduces every number in Chapter 16 text, problems, and solutions (Commodities).

Where possible each result is checked by an independent route as well as by
``sdesk.x_commodities``: explicit arithmetic, identities, or reverse calculation.
"""

import math

import pytest

from sdesk import hotel, markets, tvm
from sdesk import x_commodities as xc

R = pytest.approx


# --------------------------------------------------------------------------
# Library: contract specs, boundary cases
# --------------------------------------------------------------------------

def test_contract_specs():
    spec = {k: v["multiplier"] for k, v in xc.CONTRACT_SPECS.items()}
    assert spec == {"CL": 1_000, "NG": 10_000, "GC": 100, "SI": 5_000, "HG": 25_000, "ZC": 5_000}
    assert xc.dollar_multiplier("ZC") == R(50)          # cents quote: $50 per 1 cent
    assert xc.dollar_multiplier("NG") == 10_000
    # library agrees with markets.futures_pnl for a dollar-quoted contract
    assert xc.contract_pnl("CL", 70, 71, 2) == markets.futures_pnl(70, 71, 2, 1_000)


def test_library_boundaries():
    # zero storage, zero convenience: full carry equals markets.futures_fair_value with q = 0
    assert xc.full_carry_forward(50, 0.05, 1.0) == R(markets.futures_fair_value(50, 0.05, 0.0, 1.0))
    # a futures price at full carry implies zero convenience yield
    f = xc.full_carry_forward(70, 0.045, 0.5, 2.40)
    assert xc.implied_convenience_yield(70, f, 0.045, 0.5, 2.40) == R(0, abs=1e-12)
    # flat curve, zero rates -> all components zero
    d = xc.roll_decomposition([10, 10, 10], [10, 10], [0, 0])
    assert d["compound_total"] == R(0) and d["log_roll"] == R(0)
    with pytest.raises(ValueError):
        xc.storage_cost_fill(1.0, 0.03, 0.005)
    with pytest.raises(ValueError):
        xc.roll_decomposition([1, 2], [1, 2], [0, 0])


# --------------------------------------------------------------------------
# Example 16.1 — multipliers
# --------------------------------------------------------------------------

BOOK = [("CL", 72.40, 68.15, 3, 1), ("NG", 3.250, 3.610, 2, -1), ("GC", 2400.0, 2452.3, 4, 1),
        ("SI", 30.10, 29.45, 1, -1), ("HG", 4.250, 4.115, 2, 1), ("ZC", 452.25, 468.50, 5, 1)]


def test_example_16_1():
    pnl = [xc.contract_pnl(c, e, x, n, s) for c, e, x, n, s in BOOK]
    assert pnl == [R(-12_750), R(-7_200), R(20_920), R(3_250), R(-6_750), R(4_062.50)]
    assert sum(pnl) == R(1_532.50)
    notional = [xc.contract_notional(c, e, n) for c, e, x, n, s in BOOK]
    assert notional == [R(217_200), R(65_000), R(960_000), R(150_500), R(212_500), R(113_062.50)]
    assert sum(notional) == R(1_718_262.50)
    # independent route for corn: 16.25 cents x $50 x 5
    assert 16.25 * 50 * 5 == R(4_062.50)
    # the trap: reading cents as dollars
    assert 5 * (468.50 - 452.25) * 5_000 == R(406_250)
    # shares of gross notional quoted in the decision consequence
    assert round(960_000 / sum(notional), 2) == 0.56
    assert round(65_000 / sum(notional), 2) == 0.04


# --------------------------------------------------------------------------
# Example 16.2 — cost of carry
# --------------------------------------------------------------------------

def test_example_16_2():
    s, r, t, u_dollar = 70.0, 0.045, 0.5, 2.40
    assert 0.40 * 6 == R(u_dollar)
    assert s * math.exp(r * t) == R(71.5929, abs=1e-4)
    assert math.exp(0.0225) == R(1.022755, abs=1e-6)
    fstar = xc.full_carry_forward(s, r, t, u_dollar)
    assert fstar == R(73.9929, abs=1e-4)
    u = xc.storage_yield_from_dollars(s, r, t, u_dollar)
    assert round(u, 5) == 0.06595
    assert s * math.exp((r + u) * t) == R(fstar)            # yield form reproduces dollar form
    out = {}
    for f in (68.50, 73.50, 75.00):
        y = xc.implied_convenience_yield(s, f, r, t, u_dollar)
        assert y == R(2 * math.log(fstar / f))              # identity y = ln(F*/F)/T
        out[f] = (round(math.log(f / s) / t, 4), round(y, 4))
    assert out == {68.50: (-0.0433, 0.1543), 73.50: (0.0976, 0.0134), 75.00: (0.1380, -0.0270)}
    # check line: r + u + 0.04332
    assert 0.045 + 0.06595 + 0.04332 == R(0.15427, abs=1e-5)
    assert 75.00 - fstar == R(1.0071, abs=1e-4)
    assert (75.00 - fstar) * 1_000 == R(1_007, abs=0.5)


# --------------------------------------------------------------------------
# Example 16.3 — roll decomposition
# --------------------------------------------------------------------------

SPOT = [70.00, 71.00, 69.50, 70.50, 70.00]
F_CONT = [71.40, 72.20, 71.00, 71.60]
F_BACK = [68.60, 69.80, 68.10, 69.40]


def test_example_16_3_contango():
    d = xc.roll_decomposition(SPOT, F_CONT, [0.004] * 4)
    rows = [(round(x["spot"] * 100, 4), round(x["roll"] * 100, 4), round(x["total"] * 100, 4)) for x in d["rows"]]
    assert rows == [(1.4006, -1.9608, -0.1602), (-2.0776, -1.6620, -3.3396),
                    (1.4085, -2.1127, -0.3042), (-0.6983, -1.5363, -1.8346)]
    assert round(d["sum_spot"] * 100, 4) == 0.0331
    assert round(d["sum_roll"] * 100, 4) == -7.2718
    assert d["sum_collateral"] == R(0.016)
    assert round(d["compound_total"] * 100, 3) == -5.553
    assert round(d["compound_excess"] * 100, 3) == -7.077
    assert d["spot_change"] == R(0)
    assert round(d["log_roll"] * 100, 3) == -7.340
    # independent: exp(log excess) - 1 equals compounded excess
    assert math.exp(d["log_excess"]) - 1 == R(d["compound_excess"])
    # independent route: wealth recursion F_t(1+i) + S_{t+1} - F_t
    w = 1.0
    for t in range(4):
        w *= (F_CONT[t] * 1.004 + SPOT[t + 1] - F_CONT[t]) / F_CONT[t]
    assert w - 1 == R(d["compound_total"])


def test_example_16_3_backwardation():
    d = xc.roll_decomposition(SPOT, F_BACK, [0.004] * 4)
    rows = [(round(x["spot"] * 100, 4), round(x["roll"] * 100, 4), round(x["total"] * 100, 4)) for x in d["rows"]]
    assert rows == [(1.4577, 2.0408, 3.8985), (-2.1490, 1.7192, -0.0298),
                    (1.4684, 2.0558, 3.9242), (-0.7205, 1.5850, 1.2646)]
    assert round(d["compound_total"] * 100, 3) == 9.309
    assert round(d["compound_excess"] * 100, 3) == 7.608
    assert round(d["log_roll"] * 100, 3) == 7.332


# --------------------------------------------------------------------------
# Example 16.4 — Working curve and calendar spread
# --------------------------------------------------------------------------

def _slope(x, f, r=0.045, u0=0.03, k=0.005, theta=0.06):
    return xc.carry_slope(r, xc.storage_cost_fill(f, u0, k), xc.convenience_yield_inventory(x, theta))


def _spread(slope, f_near=70.0):
    return f_near * (math.exp(slope / 12) - 1)


def test_example_16_4a():
    table = {}
    for name, x, f in [("tight", 0.60, 0.35), ("normal", 1.00, 0.55), ("glut", 1.50, 0.80), ("tank", 1.90, 0.97)]:
        y = 0.06 / x
        u = 0.03 + 0.005 * f / (1 - f)
        s = _slope(x, f)
        assert s == R(0.045 + u - y)
        table[name] = (round(y * 100, 3), round(u * 100, 3), round(s * 100, 3), round(_spread(s), 3))
    assert table == {"tight": (10.0, 3.269, -2.231, -0.130), "normal": (6.0, 3.611, 2.111, 0.123),
                     "glut": (4.0, 5.0, 5.5, 0.322), "tank": (3.158, 19.167, 20.509, 1.207)}
    # tank-tops slope exceeds normal full carry r + u0 = 7.5% by about 13 points
    assert round((_slope(1.90, 0.97) - 0.075) * 100) == 13


def test_example_16_4b():
    s0, s1 = _slope(0.95, 0.55), _slope(1.10, 0.62)
    assert round(0.06 / 0.95 * 100, 3) == 6.316
    assert round((0.03 + 0.005 * 0.62 / 0.38) * 100, 3) == 3.816
    assert round(0.06 / 1.10 * 100, 3) == 5.455
    assert (round(s0 * 100, 3), round(s1 * 100, 3)) == (1.795, 2.861)
    sp0, sp1 = _spread(s0), _spread(s1)
    assert (round(sp0, 4), round(sp1, 4)) == (0.1048, 0.1671)
    assert round(sp1 - sp0, 4) == 0.0623
    assert (sp1 - sp0) * 1_000 * 10 == R(623, abs=0.5)
    # 15% inventory move relative to normal
    assert 1.10 - 0.95 == R(0.15)


# --------------------------------------------------------------------------
# Example 16.5 — seasonal gas storage
# --------------------------------------------------------------------------

def test_example_16_5():
    m = xc.storage_intrinsic_margin(2.90, 3.95, 0.02, 0.04, 0.04, 0.30, 0.05, 6)
    assert round(m["purchase"], 4) == 2.9592
    assert round(m["finance"], 4) == 0.0740
    assert round(m["margin"], 4) == 0.5368
    # independent arithmetic
    p = 2.90 / 0.98
    assert 3.95 - p - 0.08 - 0.30 - p * 0.025 == R(m["margin"])
    assert m["margin"] * 2_000_000 == R(1_073_673, abs=1)
    assert 2_000_000 / 0.98 == R(2_040_816, abs=1)
    assert round(2_000_000 / 0.98 / 10_000, 2) == 204.08
    assert 2_000_000 / 10_000 == 200
    m2 = xc.storage_intrinsic_margin(2.90, 3.55, 0.02, 0.04, 0.04, 0.30, 0.05, 6)
    assert round(m2["margin"], 4) == 0.1368
    assert m2["margin"] * 2_000_000 == R(273_673, abs=1)
    assert round(1.05 - m["margin"], 3) == 0.513
    assert round((1.05 - m["margin"]) / 1.05, 2) == 0.49
    assert round(1 - m2["margin"] / m["margin"], 2) == 0.75


# --------------------------------------------------------------------------
# Example 16.6 — oil to RevPAR to value; hedge
# --------------------------------------------------------------------------

KW66 = dict(other_revenue_pct_of_rooms=0.08, rooms_expense_per_occupied_room=32,
            other_dept_expense_ratio=0.75, undistributed_fixed=1_100_000,
            undistributed_pct_of_revenue=0.06, mgmt_fee_pct=0.03, franchise_fee_pct_of_rooms=0.11,
            property_tax=260_000, insurance=140_000, ffe_reserve_pct=0.04)


def _ex66():
    t = xc.oil_to_revpar(-0.45, 1.0, 0.50, 0.8, 0.04, 0.80, 160.0, 0.5)
    a = hotel.operating_statement(120, 0.80, 160.0, **KW66)
    b = hotel.operating_statement(120, t["occ1"], t["adr1"], **KW66)
    return t, a, b


def test_example_16_6_transmission():
    t, a, b = _ex66()
    assert (t["rigs"], t["energy_demand"], t["demand"]) == (R(-0.45), R(-0.36), R(-0.18))
    assert round(t["occ1"], 4) == 0.6308
    assert 0.80 * 0.82 / 1.04 == R(t["occ1"])
    assert round(t["occ_change"] * 100, 2) == -21.15
    assert round(t["adr1"], 2) == 143.08
    assert t["revpar0"] == R(128.0)
    assert round(t["revpar1"], 2) == 90.25
    assert round(t["revpar_change"] * 100, 1) == -29.5


def test_example_16_6_statement_value_hedge():
    t, a, b = _ex66()
    assert [round(a[k]) for k in ("rooms_revenue", "total_revenue", "gop", "ebitda", "ffe_reserve", "noi")] == \
        [5_606_400, 6_054_912, 3_133_953, 1_935_602, 242_196, 1_693_405]
    assert [round(b[k]) for k in ("rooms_revenue", "total_revenue", "gop", "ebitda", "ffe_reserve", "noi")] == \
        [3_952_885, 4_269_116, 1_791_710, 828_819, 170_765, 658_054]
    assert (round(a["noi_margin"] * 100, 1), round(b["noi_margin"] * 100, 1)) == (28.0, 15.4)
    assert round((b["noi"] / a["noi"] - 1) * 100, 1) == -61.1
    dn, drev = a["noi"] - b["noi"], a["total_revenue"] - b["total_revenue"]
    assert round(dn) == 1_035_351 and round(drev) == 1_785_796
    assert round(dn / drev * 100, 1) == 58.0
    # check: revenue change equals RevPAR change
    assert b["total_revenue"] / a["total_revenue"] - 1 == R(t["revpar_change"])
    v0, v1 = a["noi"] / 0.095, b["noi"] / 0.105
    assert (round(v0 / 1e6, 2), round(v1 / 1e6, 2)) == (17.83, 6.27)
    assert round((v1 / v0 - 1) * 100, 1) == -64.8
    assert round((b["noi"] / a["noi"] - 1) / t["revpar_change"], 1) == 2.1
    assert round((v0 - v1) / 1e6, 1) == 11.6
    loan = 0.65 * v0
    assert round(loan / 1e6, 2) == 11.59
    ds = tvm.annual_debt_service(loan, 0.07, 25)
    assert round(ds) == 982_688
    assert (round(a["noi"] / ds, 2), round(b["noi"] / ds, 2)) == (1.72, 0.67)
    assert loan > v1
    beta = dn / (80 - 44)
    assert round(beta) == 28_760
    assert round(beta / 1_000, 1) == 28.8
    assert xc.contract_pnl("CL", 74, 44, 29, -1) == R(870_000)
    assert round(870_000 / dn * 100) == 84
    assert xc.contract_pnl("CL", 74, 100, 29, -1) == R(-754_000)


# --------------------------------------------------------------------------
# Example 16.7 — replacement cost and copper hedge
# --------------------------------------------------------------------------

def test_example_16_7():
    hard = 27_000_000
    dh = xc.hard_cost_shock(hard, [0.08, 0.05, 0.02], [0.60, 0.25, 0.30])
    assert 0.08 * 0.60 + 0.05 * 0.25 + 0.02 * 0.30 == R(0.0665)
    assert dh == R(1_795_500)
    rc0 = xc.replacement_cost(2_500_000, hard, 0.18)
    rc1 = xc.replacement_cost(2_500_000, hard + dh, 0.18)
    assert rc0 == R(34_360_000) and rc1 == R(36_478_690)
    assert (round(rc0 / 150), round(rc1 / 150)) == (229_067, 243_191)
    assert round((rc1 / rc0 - 1) * 100, 2) == 6.17
    cu = 0.02 * hard
    assert cu == R(540_000)
    assert round(cu / 4.25) == 127_059
    assert round(cu / 4.25 / 25_000, 2) == 5.08
    assert xc.contract_pnl("HG", 4.25, 4.25 * 1.30, 5) == R(159_375)
    assert cu * 0.30 == R(162_000)
    assert round(162_000 / dh * 100) == 9
    assert hard * 0.08 * 0.60 == R(1_296_000)
    assert round(1_296_000 / dh * 100) == 72


# --------------------------------------------------------------------------
# §16.6.2 — multifamily transmission
# --------------------------------------------------------------------------

def test_multifamily_transmission():
    emp = -0.25 * 0.30 * 1.5
    assert emp == R(-0.1125)
    occ1 = 0.95 * (1 + emp) / 1.03
    assert round(occ1 * 100, 2) == 81.86
    occ_chg = occ1 / 0.95 - 1
    assert round(occ_chg * 100, 2) == -13.83
    rent = 0.5 * occ_chg
    assert round(rent * 100, 2) == -6.92
    assert round(((occ1 * (1 + rent)) / 0.95 - 1) * 100, 1) == -19.8


# --------------------------------------------------------------------------
# §16.8 — historical arithmetic (April 2020)
# --------------------------------------------------------------------------

def test_april_2020_arithmetic():
    pnl = xc.contract_pnl("CL", 17.73, -37.63, 1)
    assert pnl == R(-55_360)
    assert round(-pnl / (17.73 * 1_000), 2) == 3.12
    # EIA figures: 60m total, ~2m in transit, 76m working capacity
    assert round((60 - 2) / 76 * 100) == 76


# --------------------------------------------------------------------------
# Problems
# --------------------------------------------------------------------------

def test_problem_16_2():
    p = [xc.contract_pnl("SI", 28.40, 29.15, 2), xc.contract_pnl("HG", 4.380, 4.215, 3, -1),
         xc.contract_pnl("ZC", 437.0, 425.5, 4), xc.contract_pnl("NG", 2.875, 3.140, 1)]
    assert p == [R(7_500), R(12_375), R(-2_300), R(2_650)]
    assert sum(p) == R(20_225)
    assert 4 * (425.5 - 437.0) * 5_000 == R(-230_000)    # the cents-as-dollars error


def test_problem_16_3():
    f = 2_000 * math.exp(0.040 - 0.005)
    assert round(f, 2) == 2_071.24
    assert round(2_000 * math.exp(0.04), 2) == 2_081.62
    assert round(xc.contract_notional("GC", f, 10)) == 2_071_239


def test_problem_16_4():
    s, r, t, u_d = 60.0, 0.05, 0.25, 3 * 0.45
    assert round(s * math.exp(r * t), 4) == 60.7547
    fstar = xc.full_carry_forward(s, r, t, u_d)
    assert round(fstar, 4) == 62.1047
    assert round(xc.storage_yield_from_dollars(s, r, t, u_d) * 100, 2) == 8.79
    assert round(63.20 - fstar, 4) == 1.0953
    assert round((63.20 - fstar) * 1_000 * 20) == 21_906
    assert round(xc.implied_convenience_yield(s, 63.20, r, t, u_d) * 100, 2) == -6.99
    assert round(xc.implied_convenience_yield(s, 58.80, r, t, u_d) * 100, 2) == 21.87


def test_problem_16_5():
    d = xc.roll_decomposition([80, 78, 81, 77], [79.00, 77.20, 80.10], [0.0035] * 3)
    rows = [(round(x["spot"] * 100, 4), round(x["roll"] * 100, 4), round(x["total"] * 100, 4)) for x in d["rows"]]
    assert rows == [(-2.5316, 1.2658, -0.9158), (3.8860, 1.0363, 5.2723), (-4.9938, 1.1236, -3.5202)]
    assert round(d["compound_total"] * 100, 3) == 0.636
    assert round(d["compound_excess"] * 100, 3) == -0.415
    assert d["spot_change"] == R(-0.0375)
    assert round(d["log_spot"] * 100, 4) == -3.8221
    assert round(d["log_roll"] * 100, 4) == 3.4061
    assert round(d["log_excess"] * 100, 4) == -0.4160
    assert math.exp(d["log_excess"]) - 1 == R(d["compound_excess"])


def test_problem_16_6():
    m = xc.storage_intrinsic_margin(2.60, 3.40, 0.015, 0.03, 0.03, 0.25, 0.06, 7)
    assert round(m["purchase"], 4) == 2.6396
    assert round(m["finance"], 4) == 0.0924
    assert round(m["margin"], 4) == 0.3580
    assert round(m["margin"] * 5_000_000) == 1_790_102
    assert round(5_000_000 / 0.985) == 5_076_142
    assert round(5_000_000 / 0.985 / 10_000, 1) == 507.6
    be = m["purchase"] + 0.03 + 0.03 + 0.25 + m["finance"]
    assert round(be, 4) == 3.0420
    assert xc.storage_intrinsic_margin(2.60, be, 0.015, 0.03, 0.03, 0.25, 0.06, 7)["margin"] == R(0, abs=1e-12)


KW167 = dict(other_revenue_pct_of_rooms=0.04, rooms_expense_per_occupied_room=28,
             other_dept_expense_ratio=0.70, undistributed_fixed=800_000,
             undistributed_pct_of_revenue=0.07, mgmt_fee_pct=0.03, franchise_fee_pct_of_rooms=0.10,
             property_tax=150_000, insurance=90_000, ffe_reserve_pct=0.04)


def test_problem_16_7():
    t = xc.oil_to_revpar(-0.35, 1.2, 0.60, 0.85, 0.05, 0.76, 135.0, 0.6)
    assert (t["rigs"], round(t["energy_demand"], 4), round(t["demand"], 4)) == (R(-0.42), -0.357, -0.2142)
    assert round(t["occ1"] * 100, 2) == 56.88
    assert round(t["occ_change"] * 100, 2) == -25.16
    assert round(t["adr1"], 2) == 114.62
    assert (round(t["revpar0"], 2), round(t["revpar1"], 2)) == (102.60, 65.19)
    assert round(t["revpar_change"] * 100, 1) == -36.5
    a = hotel.operating_statement(90, 0.76, 135.0, **KW167)
    b = hotel.operating_statement(90, t["occ1"], t["adr1"], **KW167)
    assert [round(a[k]) for k in ("rooms_revenue", "total_revenue", "gop", "ebitda", "noi")] == \
        [3_370_410, 3_505_226, 1_666_441, 984_243, 844_034]
    assert [round(b[k]) for k in ("rooms_revenue", "total_revenue", "gop", "ebitda", "noi")] == \
        [2_141_548, 2_227_210, 688_187, 167_216, 78_128]
    assert round((b["noi"] / a["noi"] - 1) * 100, 1) == -90.7
    dn = a["noi"] - b["noi"]
    assert round(dn) == 765_906
    assert 75 * 0.65 == R(48.75)
    beta = dn / 26.25
    assert round(beta) == 29_177
    assert round(beta / 1_000, 1) == 29.2
    hedge = xc.contract_pnl("CL", 71, 48.75, 29, -1)
    assert hedge == R(645_250)
    assert round(hedge / dn * 100, 1) == 84.2
    assert xc.contract_pnl("CL", 71, 96, 29, -1) == R(-725_000)


def test_problem_16_8():
    hard = 42_000_000
    dh = xc.hard_cost_shock(hard, [0.06, 0.09, 0.025], [-0.20, 0.30, 0.40])
    assert dh == R(1_050_000)
    rc0 = xc.replacement_cost(6_000_000, hard, 0.20)
    rc1 = xc.replacement_cost(6_000_000, hard + dh, 0.20)
    assert (rc0, rc1) == (R(56_400_000), R(57_660_000))
    assert round((rc1 / rc0 - 1) * 100, 2) == 2.23
    cu = 0.025 * hard
    assert cu == R(1_050_000)
    assert round(cu / 4.50) == 233_333
    assert round(cu / 4.50 / 25_000, 2) == 9.33
    assert xc.contract_pnl("HG", 4.50, 4.50 * 1.40, 9) == R(405_000)
    assert cu * 0.40 == R(420_000)
    assert 0.015 * hard == R(630_000)
    assert hard * (0.06 + 0.09 + 0.025) == R(7_350_000)


def test_problem_16_9():
    assert xc.contract_pnl("CL", 17.73, -37.63, 1) == R(-55_360)
    assert 2_000 * 1_000 * 1.0 == 2_000_000          # $1 widening on 2,000 contracts


def test_problem_16_10():
    price = 205_000 * 220
    assert price == 45_100_000
    assert price * 0.0625 == R(2_818_750)
    assert price * 0.0625 / 220 == R(12_812.50)


def test_decision_exercise():
    _, a, b = _ex66()
    k = tvm.loan_constant(0.07, 25)
    assert round(k * 100, 4) == 8.4814
    max_ds = b["noi"] / 1.20
    assert round(max_ds) == 548_379
    max_loan = max_ds / k
    assert round(max_loan) == 6_465_699
    assert round(max_loan / 0.55 / 1e6, 2) == 11.76
    assert round((1 - max_loan / 0.55 / 17.8e6) * 100) == 34
    # Item 2: margin of projected value over replacement cost per unit
    rc1 = xc.replacement_cost(2_500_000, 27_000_000 + 1_795_500, 0.18) / 150
    assert round((255_000 / rc1 - 1) * 100, 1) == 4.9
