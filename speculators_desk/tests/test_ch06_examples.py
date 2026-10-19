"""Reproduces every number in Chapter 6 text, problems, and solutions,
and tests the new helpers in ``sdesk.x_rates``."""

import math

import pytest

from sdesk import cre, fixed_income as fi, tvm, x_rates as xr

R = pytest.approx


# --------------------------------------------------------------------------
# Library tests for x_rates (independent routes and boundary cases)
# --------------------------------------------------------------------------

def test_bill_helpers_roundtrip_and_bounds():
    p = xr.bill_price_from_discount(0.05, 182)
    assert xr.bill_discount_from_price(p, 182) == R(0.05)
    # zero discount rate -> par, zero yields
    assert xr.bill_price_from_discount(0.0, 91) == R(100.0)
    assert xr.bill_bey(100.0, 91) == R(0.0)
    assert xr.bill_bey(100.0, 300) == R(0.0, abs=1e-12)
    # ordering: discount < MMY < BEY for a short bill
    assert 0.05 < xr.bill_money_market_yield(p, 182) < xr.bill_bey(p, 182)


def test_bill_bey_quadratic_satisfies_defining_equation():
    p = xr.bill_price_from_discount(0.048, 364)
    y = xr.bill_bey(p, 364)
    t = 364 / 365
    assert p * (1 + y / 2) * (1 + (t - 0.5) * y) == R(100.0)


def test_parse_32nds():
    assert xr.parse_32nds("98-17") == R(98.53125)
    assert xr.parse_32nds("98-17+") == R(98.546875)
    assert xr.parse_32nds("98-172") == R(98.5390625)
    assert 10_000_000 / 32 / 100 == R(3_125)  # one 32nd on $10m face


def test_dv01_identity_and_zero_coupon_duration():
    p = fi.bond_price(0.045, 0.04, 10)
    assert fi.dv01(0.045, 0.04, 10) == R(p * fi.modified_duration(0.045, 0.04, 10) * 1e-4, abs=2e-8)
    # zero-coupon: Macaulay duration equals maturity
    assert fi.macaulay_duration(0.05, 0.0, 7) == R(7.0)


def test_carry_rolldown_flat_curve_zero_repo_equals_yield():
    # par bond, flat curve, no financing: total over 1y = coupon
    r = xr.carry_rolldown(0.05, 5, 0.05, 0.05, 1.0, repo_rate=0.0)
    assert r["total"] == R(5.0)
    assert r["rolldown"] == R(0.0, abs=1e-10)
    with pytest.raises(ValueError):
        xr.carry_rolldown(0.05, 5, 0.05, 0.05, 0.3)


def test_expectations_yield_flat_path():
    assert xr.expectations_yield([0.04] * 10) == R(0.04)
    assert xr.term_premium(0.04, [0.04] * 10) == R(0.0, abs=1e-12)


def test_forward_rates_reprice_spot_curve():
    spots = [0.04, 0.042, 0.0435, 0.0445, 0.045]
    f = xr.forward_rates_from_spots(spots)
    grow = 1.0
    for t, ft in enumerate(f, start=1):
        grow *= 1 + ft
        assert grow == R((1 + spots[t - 1]) ** t)


def test_levered_shock_zero_leverage_and_identity():
    r = xr.levered_rate_shock(1_000_000, 0.05, 0.0, 0.01, passthrough=1.0)
    assert r["equity_pct_book"] == R(r["property_pct"])
    assert xr.equity_duration_first_order(10, 0.0) == R(10)
    assert xr.equity_duration_first_order(10, 0.5, 4.0) == R(16.0)


def test_cap_decomposition_roundtrip():
    d = xr.cap_spread_decomposition(0.06, 0.04, 0.03)
    assert xr.implied_cap_rate(0.04, d["risk_premium"], 0.03) == R(0.06)


# --------------------------------------------------------------------------
# Section 6.2 / 6.3 / 6.5 text numbers
# --------------------------------------------------------------------------

def test_intuition_and_reference_sheet_numbers():
    assert 1 / 0.06 == R(16.67, abs=0.01)                     # ~17 years at full pass-through
    assert xr.property_duration_first_order(0.06, 0.6) == R(10.0)
    assert xr.equity_duration_first_order(10, 0.65) == R(28.57, abs=0.01)
    assert 1 / 0.35 == R(2.857, abs=0.001)
    assert fi.dv01(0.045, 0.04, 10) / 100 * 1e6 == R(779, abs=1)
    assert fi.dv01(0.042, 0.04, 2) / 100 * 1e6 == R(189, abs=1)
    assert fi.bond_equivalent_to_annual(0.045) == R(0.045506, abs=1e-6)
    assert tvm.effective_annual_rate(0.065, 12) == R(0.066972, abs=1e-6)


# --------------------------------------------------------------------------
# Worked examples
# --------------------------------------------------------------------------

def test_example_6_1():
    p = xr.bill_price_from_discount(0.05, 182)
    assert round(p, 4) == 97.4722
    assert round(100 * xr.bill_bey(p, 182), 4) == 5.2009
    assert round(100 * xr.bill_money_market_yield(p, 182), 4) == 5.1297
    assert round(100 * xr.bill_effective_annual(p, 182), 4) == 5.2687
    assert round(10000 * (xr.bill_bey(p, 182) - 0.05)) == 20
    p52 = xr.bill_price_from_discount(0.048, 364)
    assert round(p52, 4) == 95.1467
    bey = xr.bill_bey(p52, 364)
    assert round(100 * bey, 4) == 5.0513
    assert round(100 * (100 - p52) / p52 * 365 / 364, 4) == 5.1149
    assert round(100 * xr.bill_effective_annual(p52, 364), 4) == 5.1153
    assert round(100 * fi.bond_equivalent_to_annual(bey), 4) == 5.1151
    assert round(100 * xr.tips_breakeven(0.043, 0.0195, exact=False), 2) == 2.35
    assert round(100 * xr.tips_breakeven(0.043, 0.0195), 3) == 2.305
    assert round(10000 * (0.0235 - xr.tips_breakeven(0.043, 0.0195)), 1) == 4.5
    assert round(100 * fi.bond_equivalent_to_annual(0.045), 4) == 4.5506
    assert round(100 * tvm.effective_annual_rate(0.065, 12), 4) == 6.6972


def test_example_6_2():
    c, T, y = 0.04, 10, 0.045
    p = fi.bond_price(y, c, T)
    assert round(p, 4) == 96.0091
    assert round(fi.macaulay_duration(y, c, T), 4) == 8.2978
    dmod = fi.modified_duration(y, c, T)
    assert round(dmod, 4) == 8.1152
    cx = fi.convexity(y, c, T)
    assert round(cx, 3) == 78.005
    dv = fi.dv01(y, c, T)
    assert round(dv, 6) == 0.077913
    assert round(dv / 100 * 10_000_000) == 7_791
    rows = {0.01: (-7.7913, 0.3745, -7.4169, -7.4295, -7.74),
            -0.01: (7.7913, 0.3745, 8.1658, 8.1791, 8.52),
            0.03: (-23.3740, 3.3701, -20.0039, -20.3274, -21.17),
            -0.03: (23.3740, 3.3701, 26.7441, 27.1260, 28.25)}
    for dy, (d_term, c_term, tot, exact, pct) in rows.items():
        a = fi.price_change_approx(p, dmod, cx, dy)
        ex = fi.bond_price(y + dy, c, T) - p
        assert round(a["duration_term"], 4) == d_term
        assert round(a["convexity_term"], 4) == c_term
        assert round(a["total"], 4) == tot
        assert round(ex, 4) == exact
        assert round(100 * ex / p, 2) == pct
    loss = (fi.bond_price(y + 0.01, c, T) - p) / 100 * 10_000_000
    assert round(loss) == -742_951
    # decision-consequence statements
    e100 = -(fi.bond_price(y + 0.01, c, T) - p)
    assert round(dmod * p * 0.01 - e100, 2) == 0.36
    assert round((dmod * p * 0.01 - e100) / e100, 3) == 0.049
    e300 = -(fi.bond_price(y + 0.03, c, T) - p)
    assert round(dmod * p * 0.03 - e300, 1) == 3.0
    g300 = fi.bond_price(y - 0.03, c, T) - p
    assert round(g300 - dmod * p * 0.03, 1) == 3.8
    a300 = fi.price_change_approx(p, dmod, cx, 0.03)["total"]
    assert round(e300 + a300, 2) == 0.32


def test_example_6_3_1987_desk():
    c, T, y = 0.09, 10, 0.10
    p = fi.bond_price(y, c, T)
    assert round(p, 4) == 93.7689
    # TVM-key route: n=20, i=5, PMT=4.5, FV=100
    pv_tvm = 4.5 * tvm.annuity_factor(0.05, 20) + 100 * 1.05 ** -20
    assert pv_tvm == R(p)
    pu, pd = fi.bond_price(0.101, c, T), fi.bond_price(0.099, c, T)
    assert round(pu, 4) == 93.1747
    assert round(pd, 4) == 94.3682
    assert round((pd - pu) / 20, 5) == 0.05967
    assert round((pd - pu) / (2 * p * 0.001), 4) == 6.3635
    assert round((pu + pd - 2 * p) / (p * 0.001 ** 2), 2) == 54.54
    table = {0.08: 106.80, 0.09: 100.00, 0.10: 93.77, 0.11: 88.05, 0.12: 82.80}
    for yy, val in table.items():
        assert round(fi.bond_price(yy, c, T), 2) == val
    p9, p11 = fi.bond_price(0.09, c, T), fi.bond_price(0.11, c, T)
    assert round((p11 - p9) / 2, 3) == -5.975
    assert round((p9 - p11) / 2 / (p * 0.01), 3) == 6.372
    mid = (p9 + p11) / 2
    assert round(mid, 2) == 94.02
    assert round(mid - p, 2) == 0.26
    assert round(2 * (mid - p) / (p * 0.01 ** 2), 2) == 54.58
    drops = [fi.bond_price(a, c, T) - fi.bond_price(a + 0.01, c, T) for a in (0.08, 0.09, 0.10, 0.11)]
    assert [round(d, 2) for d in drops] == [6.80, 6.23, 5.72, 5.25]
    assert round(fi.macaulay_duration(y, c, T), 4) == 6.6816
    assert round(fi.modified_duration(y, c, T), 4) == 6.3635
    assert round(fi.convexity(y, c, T), 3) == 54.538
    assert round(fi.dv01(y, c, T), 6) == 0.059669


def _steepener():
    d2 = fi.dv01(0.042, 0.04, 2)
    d10 = fi.dv01(0.044, 0.0425, 10)
    dv10 = d10 / 100 * 50_000_000
    f2 = fi.hedge_ratio_dv01(dv10, d2 / 100)
    return d2, d10, dv10, f2


def test_example_6_4():
    d2, d10, dv10, f2 = _steepener()
    assert round(fi.bond_price(0.042, 0.04, 2), 4) == 99.6201
    assert round(fi.bond_price(0.044, 0.0425, 10), 4) == 98.7970
    assert round(d2, 6) == 0.018947
    assert round(d10, 6) == 0.079625
    assert round(dv10) == 39_813
    assert round(f2 / 1e6, 2) == 210.13
    assert round(f2 / 50e6, 3) == 4.203

    def pnl(a, b):
        return xr.curve_trade_pnl([
            dict(face=f2, coupon=0.04, years=2, y0=0.042, dy=a, side=1),
            dict(face=50e6, coupon=0.0425, years=10, y0=0.044, dy=b, side=-1)])

    cases = {(0.005, 0.005): (-1_978_629, 1_943_738, -34_891),
             (-0.005, -0.005): (2_002_759, -2_039_185, -36_426),
             (-0.004, -0.001): (1_600_260, -400_042, 1_200_218),
             (0.003, 0.0005): (-1_190_050, 198_587, -991_463),
             (0.015, 0.015): (-5_864_890, 5_563_917, -300_973)}
    for (a, b), (l2, l10, tot) in cases.items():
        r = pnl(a, b)
        assert [round(x) for x in r["legs"]] == [l2, l10]
        assert round(r["total"]) == tot
        assert r["dv01"] == R(0.0, abs=1e-6)
    assert round(pnl(0.001, 0.004)["total"]) == 1_164_746
    assert round(dv10 * 30) == 1_194_381
    assert round(dv10 * -25) == -995_318
    assert abs(1_200_218 / 1_194_381 - 1) < 0.005
    assert abs(991_463 / 995_318 - 1) < 0.005
    assert round(300_973 / dv10, 2) == 7.56
    assert round((f2 + 50e6) / 1e6) == 260


def test_example_6_5():
    spots = [0.04, 0.042, 0.0435, 0.0445, 0.045]
    f = xr.forward_rates_from_spots(spots)
    assert [round(100 * x, 4) for x in f] == [4.0, 4.4004, 4.6506, 4.7506, 4.7002]
    assert round(100 * fi.forward_rate(0.042, 2, 0.045, 5), 4) == 4.7005
    r = xr.carry_rolldown(0.045, 5, 0.045, 0.0435, 1.0, repo_rate=0.04)
    assert round(r["price0"], 4) == 100.0
    assert round(r["price_h_rolled"], 4) == 100.5453
    assert round(r["coupon_income"], 4) == 4.5
    assert round(r["financing"], 4) == 4.0
    assert round(r["carry"], 4) == 0.5
    assert round(r["pull_to_par"], 4) == 0.0
    assert round(r["rolldown"], 4) == 0.5453
    assert round(r["total"], 4) == 1.0453
    assert round(r["dv01_h"], 6) == 0.036470
    assert round(r["breakeven_bp"], 1) == 28.7
    # independent check of the rolled price
    pv = 2.25 * tvm.annuity_factor(0.02175, 8) + 100 * 1.02175 ** -8
    assert pv == R(r["price_h_rolled"])
    r0 = xr.carry_rolldown(0.045, 5, 0.045, 0.0435, 1.0, repo_rate=0.0)
    assert round(r0["total"], 4) == 5.0453
    r5 = xr.carry_rolldown(0.045, 5, 0.045, 0.0435, 1.0, repo_rate=0.05)
    assert round(r5["carry"], 2) == -0.50
    assert round(r5["total"], 4) == 0.0453
    assert round(r5["breakeven_bp"], 1) == 1.2
    rf = xr.carry_rolldown(0.045, 5, 0.045, 0.045, 1.0, repo_rate=0.04)
    assert round(rf["rolldown"], 4) == 0.0
    assert round(rf["breakeven_bp"], 1) == 13.8
    # decision consequence: $100m face at 5:1 on $20m
    face = 5 * 20_000_000
    assert round(r["dv01_h"] / 100 * face, -2) == 36_500
    assert round(r["total"] / 100 * face / 1e6, 2) == 1.05
    loss100 = r["dv01_h"] / 100 * face * 100
    assert round(loss100 / 1e6, 1) == 3.6
    assert round(loss100 / 20e6, 2) == 0.18


def test_example_6_6():
    a = [0.040, 0.036, 0.034, 0.033, 0.033, 0.034, 0.035, 0.035, 0.035, 0.035]
    b = [0.043, 0.042, 0.041, 0.040, 0.040, 0.040, 0.040, 0.040, 0.040, 0.040]
    assert round(100 * xr.expectations_yield(a), 4) == 3.4998
    assert round(100 * xr.term_premium(0.044, a), 2) == 0.90
    assert round(100 * xr.expectations_yield(b), 4) == 4.0600
    assert round(100 * xr.term_premium(0.044, b), 2) == 0.34
    assert round(100 * sum(a) / 10, 3) == 3.500 and round(100 * sum(b) / 10, 3) == 4.060
    assert abs(sum(a) / 10 - xr.expectations_yield(a)) * 1e4 < 0.02
    assert abs(sum(b) / 10 - xr.expectations_yield(b)) * 1e4 < 0.02


def test_example_6_7():
    s = 0.0610 - 0.0430
    assert round(s * 1e4) == 180
    assert round(100 * xr.credit_triangle_hazard(s, 0.40), 2) == 3.00
    el = 0.003 * 0.60
    assert round(el * 1e4) == 18
    assert round((s - el) * 1e4) == 162
    assert round((s - el) / s, 2) == 0.90
    p = fi.bond_price(0.061, 0.06, 5)
    assert round(p, 4) == 99.5746
    assert round(fi.modified_duration(0.061, 0.06, 5), 4) == 4.2615
    assert round(fi.dv01(0.061, 0.06, 5), 6) == 0.042434
    assert round(fi.bond_price(0.071, 0.06, 5) - p, 4) == -4.1372
    h = xr.carry_rolldown(0.06, 5, 0.061, 0.061, 1.0)
    assert round(h["dv01_h"], 6) == 0.034951
    assert round(1.80 / h["dv01_h"], 1) == 51.5


def test_example_6_8():
    d = xr.cap_spread_decomposition(0.0575, 0.044, 0.03)
    assert round(d["spread"] * 1e4) == 135
    assert round(100 * d["risk_premium"], 2) == 4.35
    assert round(100 * d["required_return"], 2) == 8.75
    cases = {"A": (0.0435, 0.03, 6.75, 135, -14.81),
             "B": (0.0435, 0.0375, 6.00, 60, -4.17),
             "C": (0.0485, 0.03, 7.25, 185, -20.69)}
    for rp, g, cap, spread, chg in cases.values():
        c = xr.implied_cap_rate(0.054, rp, g)
        assert round(100 * c, 2) == cap
        assert round((c - 0.054) * 1e4) == spread
        assert round(100 * cre.cap_rate_shock_pct(0.0575, c), 2) == chg
    assert round((0.0675 - 0.0575) / 0.01, 2) == 1.0
    assert round((0.0600 - 0.0575) / 0.01, 2) == 0.25
    assert round((0.0725 - 0.0575) / 0.01, 2) == 1.5


def _loan_flows():
    L, r = 32_500_000, 0.06
    pmt = tvm.payment(L, r, 30)
    bal = tvm.loan_balance(L, r, 30, 60)
    flows = [pmt] * 60
    flows[-1] += bal
    return L, pmt, bal, flows


def _pv_monthly(flows, annual_rate):
    i = annual_rate / 12
    return sum(cf / (1 + i) ** (k + 1) for k, cf in enumerate(flows))


def test_example_6_9():
    noi = 3_000_000
    L, pmt, bal, flows = _loan_flows()
    assert round(pmt) == 194_854
    assert round(pmt * 12) == 2_338_247
    assert round(100 * tvm.loan_constant(0.06, 30), 3) == 7.195
    assert round(noi / (pmt * 12), 3) == 1.283
    assert round(bal) == 30_242_666
    # (b) immediate shock
    r = xr.levered_rate_shock(noi, 0.06, L, 0.015, passthrough=0.6)
    assert round(100 * r["cap1"], 2) == 6.90
    assert round(r["v1"]) == 43_478_261
    assert round(100 * r["property_pct"], 2) == -13.04
    assert round(r["equity0"]) == 17_500_000
    assert round(r["equity1_book"]) == 10_978_261
    assert round(100 * r["equity_pct_book"], 2) == -37.27
    assert round(r["property_eff_duration"], 2) == 8.70
    assert round(r["equity_eff_duration_book"], 2) == 24.84
    assert round(xr.equity_duration_first_order(10, 0.65), 2) == 28.57
    # loan duration by finite difference on the monthly flows
    h = 1e-6
    dmod = (_pv_monthly(flows, 0.06 - h) - _pv_monthly(flows, 0.06 + h)) / (2 * _pv_monthly(flows, 0.06) * h)
    assert _pv_monthly(flows, 0.06) == R(L)
    assert round(dmod, 3) == 4.178
    reval = L * dmod * 0.015
    assert round(reval) == 2_036_838
    r2 = xr.levered_rate_shock(noi, 0.06, L, 0.015, passthrough=0.6, debt_mod_duration=dmod)
    assert round(100 * r2["equity_pct_econ"], 2) == -25.63
    assert round(r2["equity_eff_duration_econ"], 2) == 17.09
    assert round(r2["equity1_econ"]) == 13_015_099
    assert round(xr.equity_duration_first_order(10, 0.65, dmod), 2) == 20.81
    mv1 = _pv_monthly(flows, 0.075)
    assert round(mv1) == 30_533_976
    assert round(r["v1"] - mv1) == 12_944_285
    assert round(100 * ((r["v1"] - mv1) / 17_500_000 - 1), 2) == -26.03
    # (c) refinancing
    out = {}
    for rate, cap in ((0.06, 0.06), (0.075, 0.069)):
        v = noi / cap
        m = cre.max_loan(noi, v, rate, 30, ltv_max=0.65, dscr_min=1.25, debt_yield_min=0.09)
        out[rate] = (v, tvm.loan_constant(rate, 30), m, cre.refinance_gap(bal, m["max_loan"]),
                     noi / (bal * tvm.loan_constant(rate, 30)))
    v, k, m, gap, dscr_old = out[0.06]
    assert round(v) == 50_000_000 and round(100 * k, 3) == 7.195
    assert (round(m["ltv"]), round(m["dscr"]), round(m["debt_yield"])) == (32_500_000, 33_358_323, 33_333_333)
    assert m["binding"] == "ltv"
    assert round(gap) == -2_257_334
    assert round(dscr_old, 3) == 1.379
    v, k, m, gap, dscr_old = out[0.075]
    assert round(v) == 43_478_261 and round(100 * k, 3) == 8.391
    assert (round(m["ltv"]), round(m["dscr"]), round(m["debt_yield"])) == (28_260_870, 28_603_525, 33_333_333)
    assert m["binding"] == "ltv"
    assert round(gap) == 1_981_796
    assert round(dscr_old, 3) == 1.182
    assert round(2_257_334 + 1_981_796) == 4_239_130
    # 1.30x DSCR would bind in both columns
    for rate, cap in ((0.06, 0.06), (0.075, 0.069)):
        m = cre.max_loan(noi, noi / cap, rate, 30, ltv_max=0.65, dscr_min=1.30)
        assert m["binding"] == "dscr"
    # (d) floating IO
    assert L * 0.07 == R(2_275_000)
    assert round(noi / (L * 0.07), 3) == 1.319
    assert L * 0.015 == R(487_500)
    assert round(noi / (L * 0.085), 3) == 1.086
    # comparison with the 10-year note of Example 6.2
    p = fi.bond_price(0.045, 0.04, 10)
    assert round(100 * (fi.bond_price(0.06, 0.04, 10) / p - 1), 2) == -11.34


def test_section_6_7_cre_application():
    L = 32_500_000
    assert L * 0.0001 == R(3_250)
    k0, k1 = tvm.loan_constant(0.075, 30), tvm.loan_constant(0.0751, 30)
    assert round(100 * k0, 4) == 8.3906 and round(100 * k1, 4) == 8.3988
    assert round(100 * (k1 / k0 - 1), 3) == 0.098
    assert round((k1 / k0 - 1) * 1e4, 1) == 9.8
    l0 = 3e6 / 1.25 / k0
    l1 = 3e6 / 1.25 / k1
    assert round(l0 - l1, -1) == 27_990
    value_dv01 = 50_000_000 * 10 * 0.0001
    assert value_dv01 == R(50_000)
    d5 = fi.dv01(0.045, 0.045, 5)
    assert round(d5, 6) == 0.044331
    assert round(value_dv01 / (d5 / 100) / 1e6, 1) == 112.8
    assert round(0.6 / 0.25, 1) == 2.4


def test_section_6_9_history_arithmetic():
    # verified levels (see references/sources_ch06.md)
    assert round(8.05 - 5.19, 2) == 2.86
    assert 25 + 50 + 4 * 75 + 50 == 425
    assert round(3.00 + 0.25 + 0.25 + 0.25 + 0.50 + 0.50 + 0.75, 2) == 5.50
    assert round(3.88 - 1.63, 2) == 2.25
    assert round(4.41 - 0.78, 2) == 3.63
    assert round(3.88 - 4.41, 2) == -0.53
    assert round((4.41 - 0.78) - (3.88 - 1.63), 2) == 1.38
    # 1994 illustration
    p0 = fi.bond_price(0.0519, 0.0525, 10)
    p1 = fi.bond_price(0.0805, 0.0525, 10)
    assert (round(p0, 4), round(p1, 4)) == (100.4635, 81.0156)
    assert round(100 * (p1 / p0 - 1), 2) == -19.36
    a = fi.price_change_approx(p0, fi.modified_duration(0.0519, 0.0525, 10),
                               fi.convexity(0.0519, 0.0525, 10), 0.0286)
    assert round(a["duration_term"], 2) == -22.16
    assert round(a["total"], 2) == -19.18
    assert round(-a["duration_term"] - (p0 - p1), 1) == 2.7
    # 2022 illustration
    q0 = fi.bond_price(0.0163, 0.01625, 10)
    q1 = fi.bond_price(0.0388, 0.01625, 9)
    assert (round(q0, 3), round(q1, 3)) == (99.954, 83.007)
    assert round(100 * ((q1 + 1.625) / q0 - 1), 2) == -15.33
    assert round(100 * (fi.bond_price(0.0425, 0.01625, 10) / q0 - 1), 2) == -21.17
    dm = fi.modified_duration(0.0163, 0.01625, 10)
    assert round(dm, 2) == 9.19
    assert round(-100 * dm * 0.0225, 2) == -20.69


# --------------------------------------------------------------------------
# Problems and solutions
# --------------------------------------------------------------------------

def test_problem_6_1():
    gap = tvm.effective_annual_rate(0.065, 12) - fi.bond_equivalent_to_annual(0.045)
    assert round(gap * 1e4, 1) == 214.7


def test_problem_6_2():
    dv = 25_000_000 * 0.98 * 8.2 * 1e-4
    assert dv == R(20_090)
    assert 35 * dv == R(703_150)
    conv = 0.5 * 78 * 0.0035 ** 2
    assert round(100 * conv, 3) == 0.048
    assert round(conv * 24_500_000, -3) == 12_000
    assert conv * 24_500_000 / (35 * dv) < 0.02


def test_problem_6_3():
    v = cre.cap_rate_shock_pct(0.055, 0.0625)
    assert round(100 * v, 2) == -12.00
    assert round(100 * v / 0.35, 2) == -34.29


def test_problem_6_4():
    p = xr.bill_price_from_discount(0.048, 91)
    assert round(p, 4) == 98.7867
    assert round(100 * xr.bill_bey(p, 91), 4) == 4.9264
    assert round(100 * xr.bill_money_market_yield(p, 91), 4) == 4.8590
    assert round(100 * (100 - p) / p, 4) == 1.2282 or round(100 * (100 - p) / p, 4) == 1.2283
    assert round(100 * xr.bill_effective_annual(p, 91), 4) == 5.0183
    p2 = xr.bill_price_from_discount(0.046, 364)
    assert round(p2, 4) == 95.3489
    bey = xr.bill_bey(p2, 364)
    assert round(100 * bey, 4) == 4.8332
    assert round(100 * (100 - p2) / p2 * 365 / 364, 4) == 4.8914
    assert round(100 * xr.bill_effective_annual(p2, 364), 4) == 4.8917
    assert round(100 * fi.bond_equivalent_to_annual(bey), 4) == 4.8916


def test_problem_6_5():
    c, T, y = 0.0375, 7, 0.0425
    p = fi.bond_price(y, c, T)
    assert round(p, 4) == 96.9999 and round(p, 5) == 96.99989
    assert round(fi.macaulay_duration(y, c, T), 4) == 6.2065
    dmod = fi.modified_duration(y, c, T)
    assert round(dmod, 4) == 6.0774
    cx = fi.convexity(y, c, T)
    assert round(cx, 3) == 42.808
    assert round(fi.dv01(y, c, T), 6) == 0.058951
    assert round(fi.dv01(y, c, T) / 100 * 5e6, 2) == 2_947.53
    pv_tvm = 1.875 * tvm.annuity_factor(0.02125, 14) + 100 * 1.02125 ** -14
    assert pv_tvm == R(p)
    for dy, (dt, tot, ex, e1, e2) in {0.02: (-11.7901, -10.9596, -11.0004, -0.790, 0.041),
                                       -0.02: (11.7901, 12.6206, 12.6649, -0.875, -0.044)}.items():
        a = fi.price_change_approx(p, dmod, cx, dy)
        exact = fi.bond_price(y + dy, c, T) - p
        assert round(a["duration_term"], 4) == dt
        assert round(a["total"], 4) == tot
        assert round(exact, 4) == ex
        assert round(a["duration_term"] - exact, 3) == e1
        assert round(a["total"] - exact, 3) == e2


def test_problem_6_6():
    f = xr.forward_rates_from_spots([0.045, 0.043, 0.0425, 0.042, 0.042])
    assert [round(100 * x, 4) for x in f] == [4.5, 4.1004, 4.1501, 4.0501, 4.2000]
    assert round(100 * fi.forward_rate(0.043, 2, 0.042, 5), 4) == 4.1334
    r = xr.carry_rolldown(0.0425, 3, 0.0425, 0.041, 0.5, repo_rate=0.046)
    assert round(r["coupon_income"], 4) == 2.125
    assert round(r["financing"], 4) == 2.3
    assert round(r["carry"], 4) == -0.175
    assert round(r["price_h_rolled"], 4) == 100.3530
    assert round(r["rolldown"], 4) == 0.3530
    assert round(r["total"], 4) == 0.1780
    assert round(r["dv01_h"], 6) == 0.023584
    assert round(r["breakeven_bp"], 1) == 7.5


def test_problem_6_7():
    d5, d30 = fi.dv01(0.041, 0.04, 5), fi.dv01(0.046, 0.045, 30)
    assert round(fi.bond_price(0.041, 0.04, 5), 4) == 99.5520
    assert round(fi.bond_price(0.046, 0.045, 30), 4) == 98.3816
    assert (round(d5, 6), round(d30, 6)) == (0.044679, 0.159950)
    dv30 = d30 / 100 * 20e6
    assert round(dv30) == 31_990
    f5 = fi.hedge_ratio_dv01(dv30, d5 / 100)
    assert round(f5 / 1e6, 2) == 71.60
    assert round(f5 / 20e6, 3) == 3.580
    cases = {(-0.0025, 0.0010): (805_002, 316_188, 1_121_189),
             (0.01, 0.01): (-3_116_944, 2_855_608, -261_337),
             (-0.01, -0.01): (3_284_276, -3_609_312, -325_036),
             (0.0020, -0.0015): (-636_466, -488_388, -1_124_854)}
    for (a, b), (l5, l30, tot) in cases.items():
        r = xr.curve_trade_pnl([dict(face=f5, coupon=0.04, years=5, y0=0.041, dy=a, side=1),
                                dict(face=20e6, coupon=0.045, years=30, y0=0.046, dy=b, side=-1)])
        assert [round(x) for x in r["legs"]] == [l5, l30]
        assert round(r["total"]) == tot
    assert round(35 * dv30) == 1_119_648
    assert abs(1_121_189 / (35 * dv30) - 1) < 0.002
    assert round(261_337 / dv30, 1) == 8.2 and round(325_036 / dv30, 1) == 10.2


def test_problem_6_8():
    noi, L = 2_400_000, 19_500_000
    v = noi / 0.08
    assert v == R(30_000_000) and L / v == R(0.65)
    for idx, (rate, ds, d, cf) in {0.043: (7.55, 1_472_250, 1.630, 927_750),
                                    0.063: (9.55, 1_862_250, 1.289, 537_750)}.items():
        r = idx + 0.0325
        assert round(100 * r, 2) == rate
        assert round(L * r) == ds
        assert round(noi / (L * r), 3) == d
        assert round(noi - L * r) == cf
    assert round(100 * (537_750 / 927_750 - 1)) == -42
    s = xr.levered_rate_shock(noi, 0.08, L, 0.02, passthrough=0.5)
    assert round(100 * s["cap1"], 2) == 9.00
    assert round(s["v1"]) == 26_666_667
    assert round(100 * s["property_pct"], 2) == -11.11
    assert round(s["equity1_book"]) == 7_166_667
    assert round(100 * s["equity_pct_book"], 2) == -31.75
    assert round(s["property_eff_duration"], 2) == 5.56
    assert round(s["equity_eff_duration_book"], 2) == 15.87
    dv = xr.property_duration_first_order(0.08, 0.5)
    assert dv == R(6.25)
    assert round(xr.equity_duration_first_order(dv, 0.65), 2) == 17.86
    capped = 0.05 + 0.0325
    assert round(L * capped) == 1_608_750
    assert round(noi / (L * capped), 3) == 1.492
    assert round(1_862_250 - 1_472_250) == 390_000


def test_problem_6_9():
    for g, rp in ((0.02, 3.60), (0.03, 4.60), (0.04, 5.60)):
        d = xr.cap_spread_decomposition(0.06, 0.044, g)
        assert round(100 * d["risk_premium"], 2) == rp
        assert round(d["spread"] * 1e4) == 160
    c = xr.implied_cap_rate(0.044, 0.055, 0.025)
    assert round(100 * c, 2) == 7.40
    assert round(100 * cre.cap_rate_shock_pct(0.06, c), 2) == -18.92


def test_problem_6_10():
    dv = 30_000_000 * 7.5 * 1e-4
    assert dv == R(22_500)
    assert 50 * dv == R(1_125_000)
    assert round(1 - 0.40, 2) == 0.60


def test_decision_exercise_reference_figures():
    r = xr.carry_rolldown(0.045, 5, 0.045, 0.0435, 1.0, repo_rate=0.04)
    face = 100_000_000
    assert round(r["dv01_h"] / 100 * face, -1) == 36_470
    assert round(r["total"] / 100 * face / 1e6, 3) == 1.045
    assert round(r["dv01_h"] / 100 * face * 100 / 1e6, 2) == 3.65
    s = xr.levered_rate_shock(3_000_000, 0.06, 32_500_000, 0.015, passthrough=0.6)
    assert round(s["equity_eff_duration_book"], 1) == 24.8
    assert round(xr.equity_duration_first_order(10, 0.65), 1) == 28.6
