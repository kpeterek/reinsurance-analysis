"""Case C numbers as stated in case_C.md and case_C_rubric.md."""

import importlib.util
import math
from pathlib import Path

import pytest

from sdesk import cre, tvm

R = pytest.approx
_P = Path(__file__).resolve().parents[1] / "cases/hypothetical/case_C_cap_rate_expansion/case_c_model.py"
_spec = importlib.util.spec_from_file_location("case_c_model", _P)
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)


def test_origination():
    o = m.origination()
    assert o["noi"] == R(1_200_000)
    assert o["loan"] == R(14_000_000)
    assert o["equity_cash"] == R(6_300_000)
    assert o["ds_io"] == R(700_000)
    assert round(o["ds_amort"]) == 901_860
    assert round(o["loan_constant"], 6) == 0.064419
    assert (round(o["dscr_io"], 2), round(o["dscr_amort"], 2)) == (1.71, 1.33)
    assert round(o["debt_yield"], 4) == 0.0857
    assert (round(o["cash_on_cash_io"], 4), round(o["cash_on_cash_amort"], 4)) == (0.0794, 0.0473)
    assert round(o["per_sf"], 2) == 256.41
    # independent: monthly payment from the closed-form annuity
    i = 0.05 / 12
    pmt = 14_000_000 * i / (1 - (1 + i) ** -360)
    assert 12 * pmt == R(o["ds_amort"])


def test_balances_and_io_timing():
    assert m.balance_at(24) == R(14_000_000)            # IO: no principal paid
    b36 = m.balance_at(36)
    assert round(b36) == 13_793_449
    # independent schedule check
    sched = tvm.amortization_schedule(14_000_000, 0.05, 30, periods=36, io_periods=24)
    assert sched[-1]["end"] == R(b36, abs=0.01)
    assert round(14_000_000 - b36) == 206_551
    assert round(m.balance_at(60)) == 13_348_103
    # trap: amortizing from month 1 instead of after the IO period gives a lower balance
    assert tvm.loan_balance(14_000_000, 0.05, 30, 36) < b36 - 400_000


def test_shock():
    s = m.shock()
    assert s["noi1"] == R(1_080_000)
    assert s["cap1"] == R(0.075)
    assert s["value1"] == R(14_400_000)
    assert round(s["per_sf1"], 2) == 184.62
    assert round(s["equity_pre"]) == 6_206_551
    assert round(s["equity_post"]) == 606_551
    assert round(s["asset_drawdown"], 4) == 0.28
    assert round(s["equity_drawdown"], 4) == 0.9023
    assert round(s["equity_vs_cash_invested"], 4) == -0.9037
    assert round(s["multiplier"], 2) == 3.22
    assert (round(s["loss_from_noi_alone"]), round(s["loss_from_cap_alone"]), round(s["interaction"])) == \
        (2_000_000, 4_000_000, -400_000)
    assert s["value_loss"] == R(5_600_000)
    assert 0.90 * 0.06 / 0.075 == R(0.72)
    # duration point in Mode A: 150 bp on 6% vs on 9%
    assert round(1 - 0.06 / 0.075, 2) == 0.20
    assert round(1 - 0.09 / 0.105, 2) == 0.14


def test_leverage_table_and_grid():
    t = {round(r["ltv"], 2): r for r in m.leverage_table()}
    exp = {0.0: (0.28, None), 0.5: (0.56, 0.6944), 0.6: (0.70, 0.8333), 0.7: (0.9333, 0.9722), 0.75: (1.12, 1.0417)}
    for k, (dd, ltv) in exp.items():
        assert round(t[k]["drawdown"], 4) == dd
        if ltv is not None:
            assert round(t[k]["ltv_after"], 4) == ltv
    g = m.shock_grid()
    table = {0.0: [(74.7, 24.8), (80.5, 46.0), (86.2, 64.4), (92.0, 80.6)],
             -0.05: [(78.6, 39.7), (84.7, 59.8), (90.7, 77.3), (96.8, 92.6)],
             -0.10: [(83.0, 54.5), (89.4, 73.7), (95.8, 90.2), (102.2, 104.7)],
             -0.15: [(87.9, 69.4), (94.7, 87.5), (101.4, 103.1), (108.2, 116.8)]}
    for dn, row in table.items():
        got = [(round(100 * g[(dn, dc)]["ltv"], 1), round(100 * g[(dn, dc)]["equity_drawdown"], 1))
               for dc in (0.005, 0.010, 0.015, 0.020)]
        assert got == row
    passing = [k for k, v in g.items() if v["ltv"] <= 0.75]
    assert passing == [(0.0, 0.005)]


def test_covenants():
    c = m.covenants()
    assert round(c["ltv"], 4) == 0.9579
    assert round(c["dscr"], 3) == 1.198
    assert round(c["debt_yield"], 4) == 0.0783
    assert c["ltv_breach"] and not c["dscr_default"] and c["sweep_dscr"] and c["sweep_dy"]
    assert round(c["paydown_ltv"]) == 2_993_449
    assert 0.75 * 14_400_000 == R(10_800_000)
    assert round(c["paydown_dy"]) == 293_449
    assert round(c["noi_for_dscr_cov"]) == 1_037_139
    assert round(c["noi_for_dscr_cov"] / 1_080_000 - 1, 4) == -0.0397
    assert round(c["noi_for_sweep_dscr"]) == 1_127_325
    assert round(c["noi_for_sweep_dscr"] / 1_080_000 - 1, 3) == 0.044
    assert round(c["cap_at_ltv_break"], 4) == 0.0587
    assert round(c["cash_flow_after_ds"]) == 178_140
    assert round(c["dscr"] - 1.15, 3) == 0.048
    # NOI shock alone breaches LTV
    assert round(m.balance_at(36) / (1_080_000 / 0.06), 3) == 0.766
    # origination headroom
    assert round(m.origination()["dscr_amort"] - 1.25, 2) == 0.08


def test_recovery():
    r = m.recovery()
    assert round(r["asset_gain"], 4) == 0.3889
    assert round(r["equity_gain"], 2) == 9.23
    assert r["noi_needed"] == R(1_500_000)
    assert round(r["years_at_3pct"], 1) == 11.1
    assert r["cap_needed_now"] == R(0.054)
    assert r["value_needed_for_equity"] == R(20_000_000)
    assert round(math.log(1.2 / 1.08) / math.log(1.03), 1) == 3.6


def test_maturity_refi():
    x = m.maturity_refi()
    assert round(x["noi_fwd"]) == 1_123_632
    assert round(x["value"]) == 14_981_760
    assert round(x["balance"]) == 13_348_103
    assert round(x["ltv_at_maturity"], 4) == 0.891
    assert (round(x["refi_ltv"]), round(x["refi_dscr"]), round(x["refi_debt_yield"])) == \
        (8_989_056, 11_105_135, 11_827_705)
    assert x["refi_binding"] == "ltv"
    assert round(x["gap"]) == 4_359_047


def test_forced_sale():
    f = m.forced_sale()
    assert [round(n) for n in f["noi_path"]] == [1_080_000, 1_107_000, 1_134_675, 1_163_042, 1_192_118, 1_221_921]
    assert [round(c) for c in f["cash_flows"]] == [993_600, 1_018_440, 1_043_901, 1_069_999, 1_096_748]
    assert (round(f["gross_reversion"]), round(f["net_reversion"]), round(f["pv_reversion"])) == \
        (15_274_011, 14_968_531, 8_883_094)
    assert round(f["reversion_share"], 3) == 0.698
    assert round(f["price"]) == 12_723_818
    assert round(f["per_sf"], 2) == 163.13
    assert round(f["implied_cap"], 4) == 0.0849
    assert round(f["discount_to_mark"], 4) == 0.1164
    assert round(f["net_to_seller"]) == 12_469_341
    assert round(f["shortfall"]) == 1_324_107
    assert round(f["lender_recovery_pct"], 4) == 0.904
    # independent: IRR of the buyer's flows at the forced-sale price equals 11%
    flows = [-f["price"]] + f["cash_flows"][:4] + [f["cash_flows"][4] + f["net_reversion"]]
    assert tvm.irr(flows) == R(0.11, abs=1e-9)


def test_lender_options():
    lo = m.lender_options()
    assert round(lo["short_sale"]) == 12_469_341
    assert round(lo["foreclose_pv"]) == 11_875_913
    assert round(lo["note_sale"]) == 11_034_759
    assert (round(lo["short_sale_pct"], 4), round(lo["foreclose_pct"], 4), lo["note_sale_pct"]) == \
        (0.904, 0.861, R(0.80))
    assert 993_600 * 1.25 == R(1_242_000)
    assert round(m.forced_sale()["price"] * 0.93) == 11_833_150
    assert round(m.forced_sale()["price"] * 0.93 + 1_242_000) == 13_075_150
    assert round(lo["short_sale"] - lo["foreclose_pv"], -3) == 593_000


def test_sponsor_options():
    so = m.sponsor_options()
    assert round(so["paydown"]) == 2_993_449
    assert round(so["bal60_cured"]) == 10_040_518
    rows = so["rows"]
    assert [round(r["net"]) for r in rows] == [17_150_000, 14_700_000, 11_760_000]
    assert [round(r["cure_payoff"]) for r in rows] == [7_109_482, 4_659_482, 1_719_482]
    assert [round(r["no_cure_payoff"]) for r in rows] == [3_801_897, 1_351_897, 0]
    assert [round(r["pref_residual"]) for r in rows] == [3_287_147, 837_147, 0]
    assert round(so["ev_cure"]) == 4_536_982
    assert round(so["pv_cure"]) == 3_616_854
    assert round(so["npv_cure"]) == 623_406
    assert round(so["ev_waiver"]) == 1_626_423
    assert round(so["pv_waiver"]) == 1_296_574
    assert round(so["pref_due"]) == 3_822_335
    assert round(so["ev_pref"]) == 1_240_360
    assert round(so["pv_pref"]) == 988_808
    assert round(so["ev_pref_investor"]) == 3_296_622
    assert round(so["pref_investor_expected_irr"], 4) == 0.0494
    assert so["ev_value"] == R(14_875_000)
    # the waiver PV exceeds the cure NPV; option value exceeds the equity mark
    assert so["pv_waiver"] > so["npv_cure"]
    assert so["pv_waiver"] > 2 * m.shock()["equity_post"]


def test_cure_breakeven():
    q = m.cure_breakeven_recovery_probability()
    assert round(q, 4) == 0.1049
    assert round(2_993_449 * 1.12 ** 2) == 3_754_982
    # at q the cure's NPV is zero
    so = m.sponsor_options()
    up, base, dn = (r["cure_payoff"] for r in so["rows"])
    ev = q * up + 0.5 * base + (0.5 - q) * dn
    assert ev / 1.12 ** 2 - so["paydown"] == R(0.0, abs=1e-6)


def test_rubric_figures():
    assert round(1 - 14_000_000 / 0.75 / 20_000_000, 4) == 0.0667
    assert round(40_000 / 0.075, -3) == 533_000
    assert round(12_000_000 / 14_400_000, 3) == 0.833
    assert 12_000_000 - 0.75 * 14_400_000 == R(1_200_000)
    # zero-leverage boundary: equity drawdown equals asset drawdown
    assert m.leverage_table((0.0,))[0]["drawdown"] == R(m.shock()["asset_drawdown"])
    # recovery gain is undefined (infinite) at 100% loss
    assert cre.recovery_return_required(1.0) == float("inf")
