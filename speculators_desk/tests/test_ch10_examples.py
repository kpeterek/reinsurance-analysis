"""Reproduces every number in Chapter 10 text, problems, and solutions."""

import math

import pytest

from sdesk import cre, markets, tvm
from sdesk import x_capital_structure as xc

R = pytest.approx


# ----------------------------------------------------------------- library sanity (new module)

def test_x_module_boundaries():
    # zero rate: balance falls linearly
    assert xc.io_then_amort_balance(1_200, 0.0, 10, 0, 60) == R(600)
    # no amortizing months -> balance unchanged
    assert xc.io_then_amort_balance(1_000_000, 0.06, 30, 36, 36) == R(1_000_000)
    # caplet at expiry is intrinsic; deep OTM caplet ~ 0
    assert xc.bachelier_caplet(0.05, 0.03, 0.01, 0.0, 0.25, 1.0, 100) == R(0.5)
    assert xc.bachelier_caplet(0.00, 0.10, 0.005, 1.0, 0.25, 1.0, 1e6) < 1e-6
    # put-call parity analogue: caplet - floorlet = tau*DF*(F-K); floorlet via symmetry
    F, K, s, T = 0.04, 0.035, 0.01, 1.5
    c = xc.bachelier_caplet(F, K, s, T, 0.25, 0.97)
    fl = 0.25 * 0.97 * ((K - F) * markets.norm_cdf((K - F) / (s * math.sqrt(T)))
                        + s * math.sqrt(T) * markets.norm_pdf((K - F) / (s * math.sqrt(T))))
    assert c - fl == R(0.25 * 0.97 * (F - K))
    # tranche losses: no decline -> no loss; 100% loss -> all lose
    t = xc.tranche_losses(100, 100, [("a", 60), ("b", 40)])
    assert [x["loss"] for x in t] == [0, 0]
    t = xc.tranche_losses(100, 0, [("a", 60), ("b", 40)])
    assert [x["loss_pct"] for x in t] == [1.0, 1.0]
    with pytest.raises(ValueError):
        xc.tranche_losses(100, 90, [("a", 50)])
    # catch-up with gamma = carry equals no catch-up
    no = xc.catchup_waterfall_terminal(10, 18, 0.08, 5, 0.2, 0.2)
    assert no["gp"] == R(0.2 * (8 - 10 * (1.08 ** 5 - 1)))
    # loss: no promote
    assert xc.catchup_waterfall_terminal(10, 9, 0.08, 5, 0.2)["gp"] == 0


# ----------------------------------------------------------------- examples

def test_example_10_1():
    noi, v = 2_400_000, 40_000_000
    assert v == R(noi / 0.06)
    k = tvm.loan_constant(0.065, 30)
    assert round(k, 6) == 0.075848
    m = cre.max_loan(noi, v, 0.065, 30, ltv_max=0.65, dscr_min=1.25, debt_yield_min=0.08)
    assert (m["ltv"], round(m["dscr"]), m["debt_yield"], m["binding"]) == (R(26_000_000), 25_313_731, R(30_000_000), "dscr")
    L = m["max_loan"]
    assert tvm.annual_debt_service(L, 0.065, 30) == R(1_920_000)
    assert round(L / v, 4) == 0.6328 and round(noi / L, 4) == 0.0948
    m625 = cre.max_loan(noi, v, 0.0625, 30, ltv_max=0.65, dscr_min=1.25)
    assert round(m625["dscr"]) == 25_985_956 and m625["binding"] == "dscr"
    assert round(tvm.loan_constant(0.0625, 30), 6) == 0.073886
    k_star = 0.06 / (0.65 * 1.25)
    assert round(k_star, 6) == 0.073846
    lo, hi = 0.03, 0.09
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if tvm.loan_constant(mid, 30) < k_star else (lo, mid)
    assert round(mid, 4) == 0.0624
    io = cre.max_loan(noi, v, 0.065, None, ltv_max=0.65, dscr_min=1.25, debt_yield_min=0.08, interest_only=True)
    assert round(io["dscr"]) == 29_538_462 and io["binding"] == "ltv"
    assert round(m625["dscr"] - m["dscr"], -4) == 670_000  # "about $0.67 million" per 25 bp


def test_example_10_2():
    P, r = 25_000_000, 0.065
    i = r / 12
    pmt = tvm.payment(P, r, 30)
    assert round(pmt, 2) == 158_017.01
    assert round(12 * pmt) == 1_896_204
    sch = tvm.amortization_schedule(P, r, 30, periods=12)
    yi, yp = sum(x["interest"] for x in sch), sum(x["principal"] for x in sch)
    assert (round(yi), round(yp)) == (1_616_773, 279_431)
    assert round(yp / (12 * pmt), 3) == 0.147
    b120 = tvm.loan_balance(P, r, 30, 120)
    assert round(b120, 2) == 21_194_031.59
    # independent: prospective form
    assert pmt * tvm.annuity_factor(i, 240) == R(b120)
    # independent: schedule
    assert tvm.amortization_schedule(P, r, 30, periods=120)[-1]["end"] == R(b120)
    assert round(P - b120) == 3_805_968
    assert round(120 * pmt - (P - b120), 2) == 15_156_072.30
    assert round((P - b120) / P, 3) == 0.152
    # IO variant
    assert P * r / 12 == R(135_416.6667) and P * r == R(1_625_000)
    bio = xc.io_then_amort_balance(P, r, 30, 36, 120)
    assert round(bio, 2) == 22_604_061.20
    sched = tvm.amortization_schedule(P, r, 30, periods=120, io_periods=36)
    assert sched[-1]["end"] == R(bio)
    assert round(bio - b120) == 1_410_030
    assert (round(b120 / P, 3), round(bio / P, 3)) == (0.848, 0.904)


def test_example_10_3():
    noi, v, spread, strike, L = 2_100_000, 40_000_000, 0.0325, 0.03, 30_000_000
    m = cre.max_loan(noi, v, 0.0, None, ltv_max=0.75, dscr_min=1.10, interest_only=True, dscr_rate=strike + spread)
    assert round(m["dscr"]) == 30_545_455 and m["max_loan"] == R(L) and m["binding"] == "ltv"
    lo = L * (0.0005 + spread)
    assert lo == R(990_000) and round(noi / lo, 2) == 2.12
    unh, cap = L * (0.053 + spread), L * (strike + spread)
    assert (unh, cap) == (R(2_565_000), R(1_875_000))
    assert (round(noi / unh, 2), round(noi / cap, 2)) == (0.82, 1.12)
    assert L * (0.053 - strike) == R(690_000)
    a = xc.cap_premium(L, strike, 0.0125, 0.008, 2)
    assert round(a["premium"]) == 3_680
    assert round(a["pct_notional"] * 100, 3) == 0.012
    assert round(a["annual_bp_equivalent"], 1) == 0.6
    b = xc.cap_premium(L, strike, 0.0475, 0.012, 2)
    assert round(b["premium"]) == 888_370
    assert round(b["pct_notional"] * 100, 2) == 2.96
    assert round(b["annuity"], 4) == 1.8972
    assert round(b["annual_bp_equivalent"]) == 156
    assert len(b["caplets"]) == 7
    assert round(xc.cap_premium(L, 0.0475, 0.0475, 0.012, 2)["premium"]) == 226_647
    c5 = xc.cap_premium(L, 0.05, 0.0475, 0.012, 2)
    assert round(c5["premium"]) == 170_675 and round(c5["annual_bp_equivalent"]) == 30
    intrinsic = sum(L * 0.25 * (0.0475 - 0.03) * (1 + 0.0475 / 4) ** (-j) for j in range(2, 9))
    assert L * 0.25 * 0.0175 == R(131_250)
    assert round(intrinsic) == 866_331
    assert round(b["premium"] - intrinsic) == 22_039


STACK = [("senior", 30e6), ("mezz", 7.5e6), ("pref", 5e6), ("common", 7.5e6)]


def test_example_10_4():
    noi = 3_250_000
    assert noi / 50e6 == R(0.065)
    sen = tvm.annual_debt_service(30e6, 0.06, 30)
    assert round(sen) == 2_158_382
    assert (round(noi / sen, 2), round(noi / 30e6, 4)) == (1.51, 0.1083)
    mz = 7.5e6 * 0.11
    assert mz == R(825_000)
    assert round(noi / (sen + mz), 2) == 1.09
    assert round(noi / 37.5e6, 4) == 0.0867
    assert round(noi - sen - mz - 600_000) == -333_382
    exp = {40e6: [0, 0, 2.5e6, 7.5e6], 35e6: [0, 2.5e6, 5e6, 7.5e6], 32.5e6: [0, 5e6, 5e6, 7.5e6]}
    for nv, losses in exp.items():
        t = xc.tranche_losses(50e6, nv, STACK)
        assert [x["loss"] for x in t] == [R(v) for v in losses]
        assert sum(x["loss"] for x in t) == R(50e6 - nv)
    t = xc.tranche_losses(50e6, 35e6, STACK)
    assert [(round(x["attach"], 2), round(x["detach"], 2)) for x in t] == [(0, 0.6), (0.6, 0.75), (0.75, 0.85), (0.85, 1.0)]
    assert round(t[1]["loss_pct"], 2) == 0.33
    assert round(xc.tranche_losses(50e6, 32.5e6, STACK)[1]["loss_pct"], 2) == 0.67
    # impairment thresholds
    assert xc.tranche_losses(50e6, 37.5e6, STACK)[1]["loss"] == 0
    assert xc.tranche_losses(50e6, 30e6, STACK)[1]["loss_pct"] == R(1.0)


def test_example_10_5():
    cases = {"down": ([-10e6, 0.5e6, 0.5e6, 0.5e6, 0.5e6, 10.5e6], 0.0500, 0.0500, 0),
             "base": ([-10e6, 0.6e6, 0.65e6, 0.7e6, 0.75e6, 14.0e6], 0.1193, 0.1119, 513_661),
             "up": ([-10e6, 0.6e6, 0.65e6, 0.7e6, 0.75e6, 17.0e6], 0.1589, 0.1419, 1_343_451)}
    prom = {}
    for k, (fl, pirr, iirr, p) in cases.items():
        w = cre.irr_hurdle_waterfall(fl, [0.08, 0.12], [1.0, 0.8, 0.7])
        assert round(tvm.irr(fl), 4) == pirr
        assert round(w["investor_irr"], 4) == iirr
        assert round(sum(w["promote"])) == p
        for t in range(len(fl)):  # conservation
            if fl[t] > 0:
                assert w["investor"][t] + w["promote"][t] == R(fl[t])
        prom[k] = sum(w["promote"])
    assert round(prom["up"] - prom["base"]) == 829_790
    assert round((prom["up"] - prom["base"]) / 3e6, 3) == 0.277
    full = xc.catchup_waterfall_terminal(10e6, 18e6, 0.08, 5, 0.20, 1.0)
    none = xc.catchup_waterfall_terminal(10e6, 18e6, 0.08, 5, 0.20, 0.20)
    assert round(full["pref_amount"]) == 4_693_281
    assert (round(full["gp"]), round(full["investor"])) == (1_600_000, 16_400_000)
    assert round(full["investor_irr"], 4) == 0.1040
    assert (round(none["gp"]), round(none["investor"])) == (661_344, 17_338_656)
    assert round(none["investor_irr"], 4) == 0.1164
    assert round(full["gp"] - none["gp"]) == 938_656
    x = 0.2 * full["pref_amount"] / 0.8
    assert round(x) == 1_173_320
    d_star = 10e6 + full["pref_amount"] + x
    assert round(d_star) == 15_866_601
    at = xc.catchup_waterfall_terminal(10e6, d_star, 0.08, 5, 0.20, 1.0)
    assert at["gp_share_of_profit"] == R(0.20)
    assert round(d_star - 10e6) == 5_866_601


def test_example_10_6():
    v0 = 2_000_000 / 0.0475
    assert round(v0) == 42_105_263
    L0 = 26_000_000
    assert round(tvm.annual_debt_service(L0, 0.0325, 30)) == 1_357_844
    b = tvm.loan_balance(L0, 0.0325, 30, 60)
    assert round(b) == 23_219_757
    v = 2_200_000 / 0.0625
    assert v == R(35_200_000) and round(v / v0 - 1, 3) == -0.164
    m = cre.max_loan(2_200_000, v, 0.065, 30, ltv_max=0.65, dscr_min=1.25, debt_yield_min=0.09)
    assert (m["ltv"], round(m["dscr"]), round(m["debt_yield"]), m["binding"]) == (R(22_880_000), 23_204_254, 24_444_444, "ltv")
    assert 0.015 * m["max_loan"] == R(343_200)
    gap = cre.refinance_gap(b, m["max_loan"], 0.015 * m["max_loan"])
    assert round(gap) == 682_957
    assert round(v0 - L0) == 16_105_263 and round(v - b) == 11_980_243
    ds_new = tvm.annual_debt_service(m["max_loan"], 0.065, 30)
    assert round(ds_new) == 1_735_406
    assert round(2_200_000 - tvm.annual_debt_service(L0, 0.0325, 30)) == 842_156
    assert round(2_200_000 - ds_new) == 464_594
    assert round(2_200_000 / (b * tvm.loan_constant(0.065, 30)), 3) == 1.249


def test_example_10_7():
    L, noi, rate = 30e6, 2_100_000, 0.0625
    ds = L * rate
    assert ds == R(1_875_000) and round(noi / ds, 2) == 1.12 and noi / L == R(0.07)
    assert noi - ds == R(225_000)
    l_dscr = noi / 1.20 / rate
    l_dy = noi / 0.075
    assert (l_dscr, l_dy) == (R(28e6), R(28e6))
    assert 1.20 * 0.0625 == R(0.075)
    assert round(2e6 / (225_000 / 12), 1) == 106.7


def test_example_10_8():
    B = 30e6
    states = [(0.3, 33e6), (0.4, 27e6), (0.3, 21e6)]
    payoff = sum(p * max(v - B, 0) for p, v in states)
    assert payoff == R(900_000)
    assert round(payoff / 1.15) == 782_609
    assert sum(p * v for p, v in states) == R(27e6)
    fc = 27e6 * 0.92
    assert fc == R(24_840_000) and fc / 1.08 == R(23_000_000)
    ext = sum(p * (B if v >= B else v * 0.92) for p, v in states)
    assert ext == R(24_732_000) and ext / 1.08 == R(22_900_000)
    assert fc / 1.08 - ext / 1.08 == R(100_000)
    assert B - fc == R(5_160_000)


def test_example_10_9():
    a = xc.capital_call_dilution(90, 10, 4e6, 3e6, 0.9, True, True)
    assert a["share_b"] == R(0.10) and a["share_b"] * 7e6 == R(700_000)
    assert 2.7e6 / a["price_per_unit"] == R(67.5) and 0.3e6 / a["price_per_unit"] == R(7.5)
    b = xc.capital_call_dilution(90, 10, 4e6, 3e6, 0.9, True, False, 1.0)
    assert b["units_a"] - 90 == R(75) and round(b["share_b"], 5) == 0.05714
    assert b["share_b"] * 7e6 == R(400_000)
    c = xc.capital_call_dilution(90, 10, 4e6, 3e6, 0.9, True, False, 1.5)
    assert c["units_a"] - 90 == R(78.75) and round(c["share_b"], 5) == 0.05594
    assert round(c["share_b"] * 7e6) == 391_608 and round(400_000 - c["share_b"] * 7e6) == 8_392
    d = xc.capital_call_dilution(90, 10, 10e6, 3e6, 0.9, True, False, 1.0)
    assert d["units_a"] - 90 == R(30) and round(d["share_b"], 5) == 0.07692
    assert round(d["share_b"] * 7e6) == 538_462 and round(d["share_b"] * 7e6 - 400_000) == 138_462
    e = xc.capital_call_dilution(90, 10, 10e6, 3e6, 0.9, True, False, 1.5)
    assert e["units_a"] - 90 == R(31.5) and round(e["share_b"], 5) == 0.07605
    assert round(e["share_b"] * 7e6) == 532_319


NOTE_SC = [{"p": 0.25, "recovery": 30e6, "costs": 0.3e6, "years": 2},
           {"p": 0.35, "recovery": 26.5e6, "costs": 0.25e6, "years": 1},
           {"p": 0.40, "recovery": 27e6, "costs": 1.8e6, "years": 2}]


def test_example_10_10():
    r = cre.distressed_loan_recovery(24e6, NOTE_SC, 0.12)
    d = r["detail"]
    assert [x["net"] for x in d] == [R(29.7e6), R(26.25e6), R(25.2e6)]
    assert [round(x["pv"]) for x in d] == [23_676_658, 23_437_500, 20_089_286]
    assert [round(x["annualized_return"], 4) for x in d] == [0.1124, 0.0938, 0.0247]
    assert round(r["expected_pv"]) == 22_158_004 and round(r["npv"]) == -1_841_996
    assert round(r["expected_pv"] / 30e6, 3) == 0.739
    bank = cre.distressed_loan_recovery(24e6, NOTE_SC, 0.06)["expected_pv"]
    assert round(bank) == 24_246_841
    assert round(bank - 24e6, -4) == 250_000
    assert round(30e6 - bank, -4) == 5_750_000
    assert round(bank - r["expected_pv"], -5) == 2_100_000


def test_section_10_8_and_exercise():
    # Ridgeview decision exercise numbers
    assert round(28e6 / 27e6, 3) == 1.037 and round(33e6 / 27e6, 3) == 1.222
    # pref repaid in full only in the 33.0m state
    assert [v >= 33e6 for v in (33e6, 27e6, 21e6)] == [True, False, False]


# ----------------------------------------------------------------- problems

def test_problem_10_2():
    assert (0.65 * 30e6, 1.8e6 / 1.25 / 0.075, 1.8e6 / 0.09) == (R(19.5e6), R(19.2e6), R(20e6))
    assert round(0.06 / (0.65 * 1.25), 4) == 0.0738


def test_problem_10_3():
    L = 20e6
    assert L * (0.0525 + 0.035) == R(1_750_000)
    assert L * 0.075 == R(1_500_000) and L * (0.0525 - 0.04) == R(250_000)
    assert round(1.65e6 / 1.5e6, 2) == 1.10 and round(1.65e6 / 1.75e6, 2) == 0.94


def test_problem_10_4():
    P, r = 12e6, 0.07
    assert P * r / 12 == R(70_000) and P * r == R(840_000)
    pmt = tvm.payment(P, r, 25)
    assert round(pmt, 2) == 84_813.50 and round(12 * pmt) == 1_017_762
    b = xc.io_then_amort_balance(P, r, 25, 24, 84)
    assert round(b, 2) == 10_939_458.29
    assert tvm.amortization_schedule(P, r, 25, periods=84, io_periods=24)[-1]["end"] == R(b)
    full = tvm.loan_balance(P, r, 25, 84)
    assert round(full) == 10_400_157 and round(b - full) == 539_302
    assert round(12 * pmt - P * r) == 177_762


def test_problem_10_5():
    st = [("senior", 48e6), ("mezz", 12e6), ("pref", 8e6), ("common", 12e6)]
    t = xc.tranche_losses(80e6, 64e6, st)
    assert [(round(x["attach"], 2), round(x["detach"], 2)) for x in t] == [(0, 0.6), (0.6, 0.75), (0.75, 0.85), (0.85, 1.0)]
    assert [x["loss"] for x in t] == [0, 0, R(4e6), R(12e6)]
    t = xc.tranche_losses(80e6, 56e6, st)
    assert [x["loss"] for x in t] == [0, R(4e6), R(8e6), R(12e6)]
    assert round(t[1]["loss_pct"], 2) == 0.33
    assert 4.8e6 / 3e6 == R(1.6) and 12e6 * 0.12 == R(1_440_000)
    assert round(4.8e6 / 4.44e6, 3) == 1.081 and 4.8e6 / 60e6 == R(0.08)
    assert round(1 - 4.44e6 / 4.8e6, 3) == 0.075


def test_problem_10_6():
    a = [-20e6, 1.2e6, 1.3e6, 1.4e6, 1.5e6, 27.0e6]
    w = cre.irr_hurdle_waterfall(a, [0.08, 0.13], [1.0, 0.85, 0.75])
    assert (round(tvm.irr(a), 4), round(w["investor_irr"], 4), round(sum(w["promote"]))) == (0.1121, 0.1075, 620_492)
    b = a[:-1] + [22.0e6]
    w = cre.irr_hurdle_waterfall(b, [0.08, 0.13], [1.0, 0.85, 0.75])
    assert round(tvm.irr(b), 4) == 0.0728 and sum(w["promote"]) == 0


def test_problem_10_7():
    a = xc.cap_premium(40e6, 0.035, 0.0425, 0.011, 3)
    assert len(a["caplets"]) == 11
    assert round(a["premium"]) == 1_000_378 and round(a["pct_notional"] * 100, 2) == 2.50
    assert round(a["annual_bp_equivalent"], 1) == 89.2
    b = xc.cap_premium(40e6, 0.045, 0.0425, 0.011, 3)
    assert round(b["premium"]) == 403_945 and round(b["pct_notional"] * 100, 2) == 1.01
    assert round(b["annual_bp_equivalent"], 1) == 36.0
    l1, l2 = 3e6 / 1.15 / 0.065, 3e6 / 1.15 / 0.075
    assert (round(l1), round(l2)) == (40_133_779, 34_782_609)
    assert round(a["premium"] - b["premium"]) == 596_434
    assert round((a["premium"] - b["premium"]) / (l1 - l2), 3) == 0.111
    assert round(l1 - l2, -4) == 5_350_000


def test_problem_10_8():
    both = xc.capital_call_dilution(80, 20, 6e6, 4e6, 0.8, True, True)
    assert both["share_b"] == R(0.20) and round(3.2e6 / both["price_per_unit"], 2) == 53.33
    assert round(0.8e6 / both["price_per_unit"], 2) == 13.33
    assert both["share_b"] * 10e6 - 0.8e6 == R(1.2e6)
    rows = [(6e6, 1.0, 66.67, 0.1200, 1_200_000), (6e6, 1.25, 70.00, 0.1176, 1_176_471),
            (25e6, 1.0, 16.00, 0.1724, 1_724_138), (25e6, 1.25, 16.80, 0.1712, 1_712_329)]
    for pre, pen, new_a, share, val in rows:
        d = xc.capital_call_dilution(80, 20, pre, 4e6, 0.8, True, False, pen)
        assert round(d["units_a"] - 80, 2) == new_a
        assert round(d["share_b"], 4) == share
        assert round(d["share_b"] * 10e6) == val
    assert 1_200_000 - 1_176_471 == 23_529
    assert 1_724_138 - 1_200_000 == 524_138 and 1_712_329 - 1_200_000 == 512_329


P9 = [{"p": 0.30, "recovery": 18.0e6, "costs": 0.2e6, "years": 2},
      {"p": 0.30, "recovery": 15.5e6, "costs": 0.15e6, "years": 1},
      {"p": 0.40, "recovery": 16.0e6, "costs": 1.4e6, "years": 2}]


def test_problem_10_9():
    r = cre.distressed_loan_recovery(14e6, P9, 0.15)
    d = r["detail"]
    assert [x["net"] for x in d] == [R(17.8e6), R(15.35e6), R(14.6e6)]
    assert [round(x["pv"]) for x in d] == [13_459_357, 13_347_826, 11_039_698]
    assert [round(x["annualized_return"], 4) for x in d] == [0.1276, 0.0964, 0.0212]
    assert round(r["expected_pv"]) == 12_458_034 and round(r["npv"]) == -1_541_966
    other = 0.3 * d[0]["pv"] + 0.3 * d[1]["pv"]
    assert round(other) == 8_042_155
    need = 14e6 - other
    assert round(need) == 5_957_845
    pv_f = need / 0.40
    assert round(pv_f) == 14_894_612
    net_f = pv_f * 1.15 ** 2
    assert round(net_f) == 19_698_125
    assert round(net_f + 1.4e6) == 21_098_125
    # check: plugging it back gives zero NPV
    sc = [dict(x) for x in P9]
    sc[2]["recovery"] = net_f + 1.4e6
    assert cre.distressed_loan_recovery(14e6, sc, 0.15)["npv"] == R(0, abs=1e-4)
    assert round(r["expected_pv"] / 18e6, 3) == 0.692


def test_problem_10_10():
    vals = {44e6: (0.864, 1.000), 2.55e6 / 0.06: (0.894, 1.035), 2.35e6 / 0.0625: (1.011, 1.170),
            2.35e6 / 0.065: (1.051, 1.217)}
    for v, (a, d) in vals.items():
        assert (round(38e6 / v, 3), round(44e6 / v, 3)) == (a, d)
    assert round(2.55e6 / 0.06) == 42_500_000 and round(2.35e6 / 0.0625) == 37_600_000
    assert round(2.35e6 / 0.065, -5) == 36_200_000
    i = 38e6 * (0.04 + 0.034)
    assert i == R(2_812_000)
    assert [round(n / i, 2) for n in (2.35e6, 2.55e6, 3.1e6)] == [0.84, 0.91, 1.10]
    assert round(2.35e6 / 1.15 / 0.074, -5) == 27_600_000
    assert round(38e6 - 2.35e6 / 1.15 / 0.074, -5) == 10_400_000
    assert 2.35e6 - i - 0.13 * 6e6 == R(-1_242_000)
