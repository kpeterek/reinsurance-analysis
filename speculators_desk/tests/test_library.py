"""Independent checks of the sdesk library against textbook identities and
published reference values. These tests do not reuse the function under test
to produce the expected value wherever an independent route exists."""

import math
from datetime import date

import pytest

from sdesk import cre, fixed_income as fi, hotel, markets as mk, risk, stats, tvm


# ---------------------------------------------------------------- TVM / loans

def test_payment_reference_value():
    # $100,000, 6% nominal, 30 years monthly: standard reference value $599.55
    assert tvm.payment(100_000, 0.06, 30) == pytest.approx(599.55, abs=0.005)


def test_amortization_reconciles():
    sched = tvm.amortization_schedule(1_000_000, 0.07, 25)
    assert len(sched) == 300
    assert sched[-1]["end"] == pytest.approx(0.0, abs=1e-6)
    assert sum(r["principal"] for r in sched) == pytest.approx(1_000_000, rel=1e-10)
    # every payment equals the formula payment
    pmt = tvm.payment(1_000_000, 0.07, 25)
    assert all(r["payment"] == pytest.approx(pmt) for r in sched)
    # closed-form balance agrees with schedule after 60 payments
    assert tvm.loan_balance(1_000_000, 0.07, 25, 60) == pytest.approx(sched[59]["end"], rel=1e-12)


def test_balance_equals_pv_of_remaining_payments():
    p, r, n, k = 5_000_000, 0.065, 30, 120
    pmt = tvm.payment(p, r, n)
    remaining = n * 12 - k
    pv_remaining = pmt * tvm.annuity_factor(r / 12, remaining)
    assert tvm.loan_balance(p, r, n, k) == pytest.approx(pv_remaining, rel=1e-12)


def test_interest_only_schedule():
    sched = tvm.amortization_schedule(1_000_000, 0.06, 30, periods=36, io_periods=24)
    assert sched[23]["end"] == pytest.approx(1_000_000)
    assert sched[24]["payment"] == pytest.approx(tvm.payment(1_000_000, 0.06, 30))


def test_rate_conversions_roundtrip():
    ear = tvm.effective_annual_rate(0.12, 12)
    assert ear == pytest.approx(0.126825030131969, rel=1e-12)
    assert tvm.nominal_rate(ear, 12) == pytest.approx(0.12, rel=1e-12)


def test_irr_npv_consistency():
    flows = [-1000, 100, 100, 1100]
    r = tvm.irr(flows)
    assert r == pytest.approx(0.10, abs=1e-10)
    assert tvm.npv(r, flows) == pytest.approx(0.0, abs=1e-7)


def test_xirr_one_year_exact():
    flows = [-100, 110]
    d = [date(2023, 1, 1), date(2024, 1, 1)]  # 365 days
    assert tvm.xirr(flows, d) == pytest.approx(0.10, abs=1e-9)


def test_irr_undefined_raises():
    with pytest.raises(ValueError):
        tvm.irr([100, 100])


# ---------------------------------------------------------------- CRE

def test_direct_cap_identity():
    assert cre.direct_cap_value(650_000, 0.065) == pytest.approx(10_000_000)
    assert cre.implied_cap_rate(650_000, 10_000_000) == pytest.approx(0.065)


def test_cap_shock_matches_ratio():
    r = cre.value_change_from_cap_and_noi(1_000_000, 0.06, 0.0, 0.065)
    assert r["pct_change"] == pytest.approx(0.06 / 0.065 - 1)
    assert r["pct_change"] == pytest.approx(-0.0769230769, rel=1e-8)


def test_max_loan_binding_constraint():
    out = cre.max_loan(noi=1_000_000, value=16_000_000, annual_rate=0.07, amort_years=30,
                       ltv_max=0.65, dscr_min=1.25, debt_yield_min=0.09)
    k = 12 * tvm.payment(1, 0.07, 30)
    assert out["dscr"] == pytest.approx(1_000_000 / 1.25 / k)
    assert out["ltv"] == pytest.approx(10_400_000)
    assert out["debt_yield"] == pytest.approx(1_000_000 / 0.09)
    assert out["binding"] == "dscr"
    loan = out["max_loan"]
    assert cre.dscr(1_000_000, tvm.annual_debt_service(loan, 0.07, 30)) == pytest.approx(1.25)


def test_loaded_cap_is_fixed_point():
    noi_pre_tax, c, t = 900_000, 0.08, 0.022
    v = cre.loaded_cap_value(noi_pre_tax, c, t)
    assert (noi_pre_tax - t * v) / c == pytest.approx(v)


def test_waterfall_hits_hurdle_exactly():
    # Size the final distribution so investors earn exactly 8%: no promote.
    contrib = 1_000_000
    final = contrib * 1.08 ** 3
    res = cre.irr_hurdle_waterfall([-contrib, 0, 0, final], [0.08, 0.12], [1.0, 0.8, 0.7])
    assert res["investor_irr"] == pytest.approx(0.08, abs=1e-9)
    assert sum(res["promote"]) == pytest.approx(0.0, abs=1e-6)


def test_waterfall_tier_two_boundary():
    contrib = 1_000_000
    target = contrib * 1.12 ** 3            # investor $ at 12% IRR
    tier1 = contrib * 1.08 ** 3             # investor $ at 8%
    # investors receive 100% to tier1, then 80% of gross until target
    gross = tier1 + (target - tier1) / 0.8
    res = cre.irr_hurdle_waterfall([-contrib, 0, 0, gross], [0.08, 0.12], [1.0, 0.8, 0.7])
    assert res["investor_irr"] == pytest.approx(0.12, abs=1e-9)
    assert res["promote"][-1] == pytest.approx((target - tier1) / 0.8 * 0.2)
    assert res["investor"][-1] + res["promote"][-1] == pytest.approx(gross)


def test_waterfall_conserves_cash_with_interim_flows():
    flows = [-10_000_000, 600_000, 650_000, 700_000, 750_000, 15_500_000]
    res = cre.irr_hurdle_waterfall(flows, [0.08, 0.12, 0.15], [1.0, 0.8, 0.7, 0.6])
    for t in range(1, len(flows)):
        assert res["investor"][t] + res["promote"][t] == pytest.approx(flows[t])
    assert res["investor_irr"] < tvm.irr(flows)


def test_residual_land_margin():
    r = cre.residual_land_value(50_000_000, 30_000_000, 5_000_000, 2_500_000, 0.15, 0.02)
    assert r["profit"] / r["total_cost"] == pytest.approx(0.15)


def test_breakeven_probability():
    p = cre.breakeven_probability(2.0, 3.0)
    assert (1 - p) * 2.0 - p * 3.0 == pytest.approx(0.0)


def test_recovery_required():
    assert cre.recovery_return_required(0.5) == pytest.approx(1.0)
    assert cre.recovery_return_required(1.0) == math.inf


def test_dcf_reduces_to_cap_when_flat_and_perpetual_like():
    # level NOI 100, k=8%, exit cap 8%, no costs => value = 100/0.08 exactly
    r = cre.dcf_value([100] * 10, 100, 0.08, 0.08)
    assert r["value"] == pytest.approx(1250.0)


# ---------------------------------------------------------------- Hotel

def test_hotel_revenue_identity():
    rev = hotel.room_revenue(120, 0.72, 125.0)
    assert rev == pytest.approx(120 * 365 * 0.72 * 125)
    assert rev / (120 * 365) == pytest.approx(hotel.revpar(0.72, 125.0))


def test_hotel_indices():
    ix = hotel.indices(0.70, 110, 0.65, 115)
    assert ix["rgi"] == pytest.approx(ix["mpi"] * ix["ari"] / 100)


def test_hotel_statement_reconciles():
    s = hotel.operating_statement(100, 0.70, 120, other_revenue_pct_of_rooms=0.03,
                                  rooms_expense_per_occupied_room=28, other_dept_expense_ratio=0.5,
                                  undistributed_fixed=600_000, undistributed_pct_of_revenue=0.10,
                                  mgmt_fee_pct=0.03, franchise_fee_pct_of_rooms=0.10,
                                  property_tax=120_000, insurance=60_000, ffe_reserve_pct=0.04)
    assert s["noi"] == pytest.approx(s["ebitda"] - 0.04 * s["total_revenue"])
    assert s["gop"] == pytest.approx(s["total_revenue"] - s["rooms_expense"] - s["other_dept_expense"]
                                     - s["undistributed"])


def test_hotel_breakeven_occupancy_zero_cash_flow():
    rooms, adr = 100, 110.0
    fixed, ds, cpor, vpct = 900_000, 450_000, 30.0, 0.17
    occ = hotel.breakeven_occupancy(rooms, adr, fixed, ds, cpor, vpct)
    sold = rooms * 365 * occ
    cf = sold * adr * (1 - vpct) - sold * cpor - fixed - ds
    assert cf == pytest.approx(0.0, abs=1e-6)


# ---------------------------------------------------------------- Fixed income

def test_par_bond_prices_at_par():
    assert fi.bond_price(0.045, 0.045, 10) == pytest.approx(100.0, abs=1e-10)


def test_zero_coupon_duration_equals_maturity():
    assert fi.macaulay_duration(0.05, 0.0, 7) == pytest.approx(7.0)


def test_duration_convexity_vs_reprice():
    y, c, n = 0.04, 0.04, 10
    p0 = fi.bond_price(y, c, n)
    d = fi.modified_duration(y, c, n)
    cx = fi.convexity(y, c, n)
    dy = 0.01
    approx = fi.price_change_approx(p0, d, cx, dy)["total"]
    exact = fi.bond_price(y + dy, c, n) - p0
    assert approx == pytest.approx(exact, abs=0.02)  # second-order error small
    # numerical derivative agrees with analytic modified duration
    h = 1e-6
    num = -(fi.bond_price(y + h, c, n) - fi.bond_price(y - h, c, n)) / (2 * h) / p0
    assert num == pytest.approx(d, rel=1e-6)


def test_dv01_consistent_with_duration():
    p = fi.bond_price(0.04, 0.04, 10)
    assert fi.dv01(0.04, 0.04, 10) == pytest.approx(fi.modified_duration(0.04, 0.04, 10) * p * 0.0001, rel=1e-4)


# ---------------------------------------------------------------- Markets

def test_futures_multiplier():
    # E-mini S&P 500: $50 per index point
    assert mk.futures_pnl(5000.0, 5010.0, 2, 50.0) == pytest.approx(1000.0)
    assert mk.futures_pnl(5000.0, 5010.0, 2, 50.0, side=-1) == pytest.approx(-1000.0)


def test_fx_quote_direction():
    # EUR/USD 1.10 -> 1.12, long EUR 1,000,000: +$20,000 (USD)
    assert mk.fx_pnl(1_000_000, 1.10, 1.12) == pytest.approx(20_000)
    assert mk.convert(1_000_000, 150.0, "USD", "USD/JPY") == pytest.approx(150_000_000)
    assert mk.convert(150_000_000, 150.0, "JPY", "USD/JPY") == pytest.approx(1_000_000)
    with pytest.raises(ValueError):
        mk.convert(1, 1.1, "GBP", "EUR/USD")


def test_black_scholes_reference():
    # Hull reference: S=100, K=100, T=1, r=5%, sigma=20% -> call 10.4506, put 5.5735
    c = mk.bs_price(100, 100, 1, 0.05, 0.2, "call")
    p = mk.bs_price(100, 100, 1, 0.05, 0.2, "put")
    assert c == pytest.approx(10.4506, abs=1e-4)
    assert p == pytest.approx(5.5735, abs=1e-4)
    assert mk.put_call_parity_gap(c, p, 100, 100, 1, 0.05) == pytest.approx(0, abs=1e-10)


def test_greeks_vs_finite_difference():
    s, h = 100.0, 0.01
    up = mk.bs_price(s + h, 105, 0.5, 0.03, 0.25)
    dn = mk.bs_price(s - h, 105, 0.5, 0.03, 0.25)
    mid = mk.bs_price(s, 105, 0.5, 0.03, 0.25)
    assert mk.bs_delta(s, 105, 0.5, 0.03, 0.25) == pytest.approx((up - dn) / (2 * h), rel=1e-6)
    assert mk.bs_gamma(s, 105, 0.5, 0.03, 0.25) == pytest.approx((up - 2 * mid + dn) / h ** 2, rel=1e-3)


def test_cip_forward():
    f = mk.covered_interest_forward(1.10, 0.05, 0.03, 1.0)
    assert f == pytest.approx(1.10 * 1.05 / 1.03)


def test_norm_ppf():
    assert mk.norm_ppf(0.99) == pytest.approx(2.326347874, abs=1e-8)


# ---------------------------------------------------------------- Risk / stats

def test_kelly_binary():
    # even-money bet with p=0.55 -> f* = 0.10
    assert risk.kelly_binary(0.55, 1.0) == pytest.approx(0.10)
    assert risk.kelly_general_binary(0.55, 1.0, 1.0) == pytest.approx(0.10)


def test_volatility_drag_example():
    # +60% / -50% coin flip: arithmetic mean +5%, geometric growth sqrt(0.8)-1
    assert risk.expected_value([0.6, -0.5], [0.5, 0.5]) == pytest.approx(0.05)
    g = math.exp(risk.expected_log_growth([0.6, -0.5], [0.5, 0.5]))
    assert g == pytest.approx(math.sqrt(0.8))


def test_parametric_var_es():
    v = risk.parametric_var(1_000_000, 0.0, 0.01, 0.99)
    assert v == pytest.approx(23_263.48, abs=0.05)
    es = risk.parametric_es(1_000_000, 0.0, 0.01, 0.99)
    assert es == pytest.approx(26_652.14, abs=0.1)
    assert es > v


def test_historical_var_order_statistic():
    pnl = list(range(-50, 50))  # 100 obs, worst -50
    assert risk.historical_var(pnl, 0.99) == 49  # index 1 -> -49
    assert risk.historical_es(pnl, 0.99) == pytest.approx(49.5)


def test_max_drawdown():
    r = risk.max_drawdown([100, 120, 90, 130, 65, 70])
    assert r["max_drawdown"] == pytest.approx(0.5)


def test_portfolio_vol_two_asset():
    v = risk.portfolio_volatility([0.5, 0.5], [0.2, 0.2], [[1, 0], [0, 1]])
    assert v == pytest.approx(0.2 / math.sqrt(2))


def test_bayes():
    # classic base-rate example
    post = stats.bayes_posterior(0.01, 0.9, 0.05)
    assert post == pytest.approx(0.009 / (0.009 + 0.0495))
    assert stats.likelihood_ratio_update(0.01, 0.9 / 0.05) == pytest.approx(post)


def test_ols_recovers_line():
    x = [1, 2, 3, 4, 5, 6]
    noise = [0.1, -0.1, 0.05, -0.05, 0.0, 0.0]
    y = [2 + 3 * v + e for v, e in zip(x, noise)]
    r = stats.ols(x, y)
    assert r["b"] == pytest.approx(3.0, abs=0.05)
    assert r["a"] == pytest.approx(2.0, abs=0.2)
    assert 0.99 < r["r2"] <= 1.0
    assert stats.correlation(x, y) ** 2 == pytest.approx(r["r2"])


def test_waterfall_without_irr_returns_none():
    flows = [-16920000, 1450000, 1400000, 1100000, 700000, -2785000, -102500, -302500, -452500]
    res = cre.irr_hurdle_waterfall(flows, [0.08, 0.12], [1.0, 0.8, 0.7])
    assert res["investor_irr"] is None
    assert sum(res["promote"]) == pytest.approx(0.0)
