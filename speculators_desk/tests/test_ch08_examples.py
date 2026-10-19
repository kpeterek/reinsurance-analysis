"""Reproduces every number in Chapter 8 text, problems, and solutions."""

import math

import pytest

from sdesk import cre, hotel, tvm

R = pytest.approx


# ------------------------------------------------------------------ helpers

def _walt(rows, rent_weight=True):
    """rows: (area, rent_psf, years_remaining, ...)."""
    if rent_weight:
        w = [a * r for a, r, *_ in rows]
    else:
        w = [a for a, *_ in rows]
    return sum(wi * row[2] for wi, row in zip(w, rows)) / sum(w)


def _ner(cash_rents, ti, lc, k):
    pv = sum(c / (1 + k) ** (t + 1) for t, c in enumerate(cash_rents))
    return pv, (pv - ti - lc) / tvm.annuity_factor(k, len(cash_rents))


HOTEL_150 = dict(other_revenue_pct_of_rooms=0.06, rooms_expense_per_occupied_room=32.0,
                 other_dept_expense_ratio=0.60, undistributed_fixed=1_350_000,
                 undistributed_pct_of_revenue=0.04, mgmt_fee_pct=0.03,
                 franchise_fee_pct_of_rooms=0.10, property_tax=260_000, insurance=150_000,
                 ffe_reserve_pct=0.04)

HOTEL_120 = dict(HOTEL_150, undistributed_fixed=950_000, property_tax=190_000, insurance=110_000)


# ------------------------------------------------------------------ section 8.4

def test_section_8_4_noi_growth():
    rev, exp = 100, 40
    noi = rev - exp
    g = 0.03 * rev / noi - 0.04 * exp / noi
    assert round(rev / noi, 3) == 1.667 and round(exp / noi, 3) == 0.667
    assert round(g, 4) == 0.0233
    # identity check by direct computation
    assert (rev * 1.03 - exp * 1.04) / noi - 1 == R(g)


def test_section_8_2_combined_leverage():
    assert round(0.25 / 0.35, 2) == 0.71


def test_section_8_4_transaction_cost_drag():
    drag5 = 1 - (0.975 / 1.015) ** (1 / 5)
    assert round(drag5, 4) == 0.0080
    drag25 = 1 - (0.975 / 1.015) ** (1 / 2.5)
    assert round(drag25, 3) == 0.016


def test_section_8_6_land_carry():
    land = 5_000_000
    carry = 0.022 * land + 15_000 + 0.08 * land
    assert (0.022 * land, 0.08 * land, carry) == (R(110_000), R(400_000), R(525_000))
    assert carry / land == R(0.105)


def test_section_8_6_dol_table():
    nl = cre.operating_leverage(1_000_000, 20_000, 0.0, -0.10)
    ind = cre.operating_leverage(2_000_000, 60_000, 0.03, -0.10)
    ss = cre.operating_leverage(2_000_000, 640_000, 0.06, -0.10)
    mf = cre.operating_leverage(3_000_000, 1_110_000, 0.08, -0.10)
    of = cre.operating_leverage(3_600_000, 1_440_000, 0.03, -0.10)
    expected = [(nl, 980_000, 1_000_000, -0.1020, 1.02), (ind, 1_880_000, 2_000_000, -0.1032, 1.03),
                (ss, 1_240_000, 2_000_000, -0.1516, 1.52), (mf, 1_650_000, 3_000_000, -0.1673, 1.67),
                (of, 2_052_000, 3_600_000, -0.1702, 1.70)]
    for res, noi0, rev, chg, dol in expected:
        assert res["noi0"] == R(noi0)
        assert round(res["pct_change"], 4) == chg
        assert round(res["dol"], 2) == dol
        assert round(res["noi0"] / rev, 3) in (0.98, 0.94, 0.62, 0.55, 0.57)
    # DOL is the ratio of pct changes when all non-variable costs are fixed
    assert mf["pct_change"] / -0.10 == R(mf["dol"])
    # zero fixed costs -> DOL = 1 (boundary)
    assert cre.operating_leverage(1_000_000, 0, 0.0, -0.10)["dol"] == R(1.0)


def test_section_8_6_landlord_borne_expense_ratio():
    unrecovered = 59_500 + 0.04 * 930_165 + 18_000
    assert round(unrecovered) == 114_707
    assert round(unrecovered / 930_165, 3) == 0.123


# ------------------------------------------------------------------ examples

OAK = [(22_000, 12.0, 8.0, 13.0), (8_000, 16.0, 4.5, 15.0), (4_000, 28.0, 2.0, 30.0),
       (1_500, 26.0, 0.5, 28.0), (3_500, 24.0, 3.0, 25.0), (3_000, 22.0, 1.0, 22.0)]


def test_example_8_1():
    gla, vac, mkt_vac, rec = 48_000, 6_000, 22.0, 3.00 + 2.50 + 0.75
    occ = sum(a for a, *_ in OAK)
    base = sum(a * r for a, r, *_ in OAK)
    assert occ == 42_000 and occ / gla == R(0.875) and base == R(693_000)
    pot_base = base + vac * mkt_vac
    pot_rec = rec * gla - 22_000 * (3.00 - 2.00)
    pgi = pot_base + pot_rec
    assert (pot_base, rec * gla, pot_rec, pgi) == (R(825_000), R(300_000), R(278_000), R(1_103_000))
    vac_loss = vac * mkt_vac + vac * rec
    assert vac_loss == R(169_500) and round(vac_loss / pgi, 4) == 0.1537
    after = pgi - vac_loss
    credit = 0.01 * after
    egi = after - credit + 6_000
    assert (after, credit, egi) == (R(933_500), R(9_335), R(930_165))
    mgmt = 0.04 * egi
    opex = rec * gla + mgmt + 18_000
    noi = egi - opex
    assert round(mgmt) == 37_207 and round(opex) == 355_207 and round(noi) == 574_958
    assert round(opex / egi, 4) == 0.3819
    ncf = noi - 0.20 * gla - 1.25 * 26_000
    assert round(ncf) == 532_858
    # recoveries actually collected and the landlord's shortfall
    collected = pot_rec - vac * rec
    assert collected == R(240_500) and rec * gla - collected == R(59_500)
    # tenant-side check
    assert base + collected + 6_000 - credit == R(egi)
    # rent roll metrics
    num = sum(a * r * t for a, r, t, _ in OAK)
    assert num == R(3_249_500)
    assert round(_walt(OAK), 2) == 4.69
    assert sum(a * t for a, _, t, _ in OAK) == R(234_250)
    assert round(_walt(OAK, rent_weight=False), 2) == 5.58
    ex = OAK[1:]
    assert sum(a * r * t for a, r, t, _ in ex) == R(1_137_500)
    assert sum(a * r for a, r, *_ in ex) == R(429_000)
    assert round(_walt(ex), 2) == 2.65
    assert round(264_000 / base, 3) == 0.381
    roll24 = sum(a * r for a, r, t, _ in OAK if t <= 2.0)
    assert roll24 == R(217_000) and round(roll24 / base, 3) == 0.313
    mkt = sum(a * m for a, _, _, m in OAK)
    assert mkt == R(721_500) and mkt - base == R(28_500) and round((mkt - base) / base, 4) == 0.0411
    assert 22_000 * (13 - 12) == 22_000
    assert sum(a * (m - r) for a, r, t, m in OAK if t <= 2.0) == R(11_000)
    # broker price and yield on NCF
    assert round(noi / 0.07) == 8_213_691
    assert round(ncf / 8_213_691, 4) == 0.0649


def test_example_8_2():
    rsf, rent, opex = 120_000, 30.0, 12.0 * 120_000
    assert opex == R(1_440_000)
    assert (78_000 + 30_000) / rsf == R(0.90)
    assert (78_000 - 6_000 + 30_000) / rsf == R(0.85)
    assert 78_000 * rent / (rsf * rent) == R(0.65)
    cash_noi = 78_000 * rent - opex
    sl_rent = 9 * 30 / 10
    assert sl_rent == R(27.0)
    sl_noi = 78_000 * rent + 30_000 * sl_rent - opex
    contract = 108_000 * rent - opex
    assert (78_000 * rent, cash_noi) == (R(2_340_000), R(900_000))
    assert (78_000 * rent + 30_000 * sl_rent, sl_noi) == (R(3_150_000), R(1_710_000))
    assert (108_000 * rent, contract) == (R(3_240_000), R(1_800_000))
    # NER
    lc = 0.06 * 270
    assert lc == R(16.2)
    assert (270 - 60 - lc) / 10 == R(19.38)
    af = tvm.annuity_factor(0.08, 10)
    assert round(af, 5) == 6.71008 and round(1 / 1.08, 5) == 0.92593
    pv, ner = _ner([0.0] + [30.0] * 9, 60, lc, 0.08)
    assert round(pv, 2) == 173.52
    assert round(ner, 2) == 14.50
    assert round(ner / 30, 3) == 0.483
    # cash vs GAAP year 1 for 30,000 sf block
    cash_y1 = -60 * 30_000 - lc * 30_000
    gaap_y1 = sl_rent * 30_000 - 6 * 30_000 - lc / 10 * 30_000
    assert (60 * 30_000, lc * 30_000) == (R(1_800_000), R(486_000))
    assert (sl_rent * 30_000, 6 * 30_000, lc / 10 * 30_000) == (R(810_000), R(180_000), R(48_600))
    assert (cash_y1, gaap_y1, gaap_y1 - cash_y1) == (R(-2_286_000), R(581_400), R(2_867_400))
    # straight-line equals cash in total
    assert 10 * sl_rent == R(9 * 30)
    # valuation consequences
    assert contract / 0.08 == R(22_500_000)
    assert 30_000 * rent == R(900_000)
    assert contract / 0.08 - 900_000 == R(21_600_000)
    assert cash_noi / 0.08 == R(11_250_000)


def test_example_8_3():
    b = hotel.operating_statement(150, 0.72, 140.0, **HOTEL_150)
    a = hotel.operating_statement(150, 0.72, 126.0, **HOTEL_150)
    o = hotel.operating_statement(150, 0.648, 140.0, **HOTEL_150)
    assert b["rooms_sold"] == R(39_420) and o["rooms_sold"] == R(35_478)
    assert b["rooms_revenue"] == R(5_518_800) and a["rooms_revenue"] == R(4_966_920)
    assert o["rooms_revenue"] == R(4_966_920)
    assert round(b["total_revenue"]) == 5_849_928 and round(a["total_revenue"]) == 5_264_935
    assert round(o["total_revenue"]) == 5_264_935
    assert round(b["rooms_expense"]) == 1_261_440 and round(o["rooms_expense"]) == 1_135_296
    assert [round(x["gop"]) for x in (b, a, o)] == [2_805_814, 2_264_089, 2_390_233]
    assert [round(x["mgmt_fee"] + x["franchise_fee"]) for x in (b, a, o)] == [727_378, 654_640, 654_640]
    assert [round(x["ebitda"]) for x in (b, a, o)] == [1_668_436, 1_199_449, 1_325_593]
    assert [round(x["ffe_reserve"]) for x in (b, a, o)] == [233_997, 210_597, 210_597]
    assert [round(x["noi"]) for x in (b, a, o)] == [1_434_439, 988_851, 1_114_995]
    assert round(b["gop_margin"], 3) == 0.480 and round(b["noi_margin"], 3) == 0.245
    chg_a = a["noi"] / b["noi"] - 1
    chg_o = o["noi"] / b["noi"] - 1
    assert round(chg_a, 4) == -0.3106 and round(chg_o, 4) == -0.2227
    ft_a = hotel.flow_through(a["noi"] - b["noi"], a["total_revenue"] - b["total_revenue"])
    ft_o = hotel.flow_through(o["noi"] - b["noi"], o["total_revenue"] - b["total_revenue"])
    assert round(ft_a, 3) == 0.762 and round(ft_o, 3) == 0.546
    assert round(chg_o / -0.10, 2) == 2.23 and round(chg_a / -0.10, 2) == 3.11
    # check: difference equals CPOR saved on lost room-nights
    assert 39_420 - 35_478 == 3_942
    assert o["noi"] - a["noi"] == R(3_942 * 32) == R(126_144)
    assert round(b["noi"] / 0.09) == 15_938_212
    nl = cre.operating_leverage(1_000_000, 20_000, 0.0, -0.10)
    assert (nl["noi0"], nl["noi1"]) == (R(980_000), R(880_000))
    assert round(nl["pct_change"], 4) == -0.1020 and round(nl["dol"], 2) == 1.02
    # equity at 65% LTV, debt fixed, cap constant
    for chg, cap, eq in [(nl["pct_change"], 0.065, -0.2915), (chg_o, 0.09, -0.6363),
                         (chg_a, 0.09, -0.8875)]:
        v0 = 1.0 / cap
        res = cre.levered_equity_change(v0, v0 * (1 + chg), 0.65 * v0)
        assert round(res["pct_change"], 4) == eq
        assert res["pct_change"] == R(chg / 0.35)


def test_example_8_4():
    inv, vac = 40.0, 0.075 * 40.0
    spec = 4.0 * 0.70
    assert (vac, spec) == (R(3.0), R(2.8))
    out = {}
    for ab in (0.30, 0.20):
        mos = (vac + spec) / ab
        v_end = vac + 4.0 - 12 * ab
        vac_rate = v_end / (inv + 4.0)
        excess = v_end - 0.075 * (inv + 4.0)
        g = 0.03 - 0.8 * (vac_rate - 0.075)
        out[ab] = (mos, v_end, vac_rate, excess, excess / ab, g)
    assert round(out[0.30][0], 1) == 19.3 and round(out[0.20][0], 1) == 29.0
    assert out[0.30][1] == R(3.4) and out[0.20][1] == R(4.6)
    assert round(out[0.30][2], 4) == 0.0773 and round(out[0.20][2], 4) == 0.1045
    assert 0.075 * 44.0 == R(3.3)
    assert out[0.30][3] == R(0.1) and out[0.20][3] == R(1.3)
    assert round(out[0.30][4], 1) == 0.3 and round(out[0.20][4], 1) == 6.5
    assert round(out[0.30][5], 4) == 0.0282 and round(out[0.20][5], 4) == 0.0064
    # vacancy rises 23 bp at trailing pace
    assert round((out[0.30][2] - 0.075) * 1e4) == 23
    assert 4.0 * 0.30 == R(1.2)


def test_example_8_5():
    noi_n = 1_450_000 - 80_000
    reserve = 300 * 200
    ncf = noi_n - reserve
    v = ncf / 0.06
    imm = 1_200_000 * 1.10
    af5 = tvm.annuity_factor(0.08, 5)
    excess = (400_000 - reserve) * af5
    price = v - imm - excess
    assert (noi_n, reserve, ncf) == (1_370_000, 60_000, 1_310_000)
    assert round(v) == 21_833_333 and imm == R(1_320_000)
    assert round(af5, 5) == 3.99271 and round(excess) == 1_357_521
    assert round(price) == 19_155_812 and round(price / 200) == 95_779
    ask = 1_450_000 / 0.06
    assert round(ask) == 24_166_667 and round(ask / 200) == 120_833
    gap = ask - price
    assert round(gap) == 5_010_855 and round(gap / ask, 3) == 0.207
    # decomposition check
    parts = [reserve / 0.06, 80_000 / 0.06, imm, excess]
    assert round(parts[0]) == 1_000_000 and round(parts[1]) == 1_333_333
    assert sum(parts) == R(gap)
    assert round(ncf / ask, 4) == 0.0542
    # the error of capitalizing a one-time bill
    assert imm / 0.06 == R(22_000_000)


def test_example_8_6():
    n, c = 1_000_000, 0.06
    v_tx = cre.loaded_cap_value(n, c, 0.022)
    v_ca = cre.loaded_cap_value(n, c, 0.0115)
    assert round(v_tx) == 12_195_122 and round(v_ca) == 13_986_014
    assert round(0.022 * v_tx) == 268_293 and round(0.0115 * v_ca) == 160_839
    assert 8_000_000 * 0.022 == R(176_000) and 4_000_000 * 0.0115 == R(46_000)
    w_tx = (n - 176_000) / c
    w_ca = (n - 46_000) / c
    assert round(w_tx) == 13_733_333 and round(w_ca) == 15_900_000
    assert round(w_tx - v_tx) == 1_538_211 and round((w_tx - v_tx) / v_tx, 3) == 0.126
    assert round(w_ca - v_ca) == 1_913_986 and round((w_ca - v_ca) / v_ca, 3) == 0.137
    assert round(n / c) == 16_666_667
    assert round(v_ca / v_tx - 1, 3) == 0.147
    assert round(0.0115 * (1.02 / 1.04) ** 10, 5) == 0.00947
    # checks: yield on price equals c after reassessed tax
    assert (n - 0.022 * v_tx) / v_tx == R(c)
    assert (n - 0.0115 * v_ca) / v_ca == R(c)
    # boundary: zero tax -> plain direct cap
    assert cre.loaded_cap_value(n, c, 0.0) == R(cre.direct_cap_value(n, c))


def test_example_8_7():
    cost = 110 + 0.20 * 110 + 18
    rc = cost * 1.15
    noi = 9.0 * 0.95 * 0.97
    assert cost == R(150) and rc == R(172.5) and noi == R(8.2935)
    assert round(noi / cost, 4) == 0.0553
    val = cre.direct_cap_value(noi, 0.0575)
    assert round(val, 2) == 144.23
    assert round(val / cost, 3) == 0.962 and round(val / rc, 3) == 0.836
    req = (0.0575 + 0.0125) * cost / (0.95 * 0.97)
    assert round(req, 2) == 11.39 and round(req / 9.0 - 1, 3) == 0.266
    assert round(130 / cost, 3) == 0.867 and round(noi / 130, 4) == 0.0638
    assert round(req * 0.95 * 0.97, 2) == 10.50 and req * 0.95 * 0.97 / cost == R(0.07)
    assert round(val - 130) == 14


# ------------------------------------------------------------------ problems

def test_problem_8_2():
    assert (1.8 + 0.6) / 0.15 == R(16.0)
    assert cre.operating_leverage(100, 60, 0.0, -0.10)["pct_change"] == R(-0.25)
    assert 0.94 * 0.92 == R(0.8648)


def test_problem_8_3():
    v = cre.loaded_cap_value(850_000, 0.075, 0.02)
    assert round(v) == 8_947_368 and round(0.02 * v) == 178_947
    w = 760_000 / 0.075
    assert round(w) == 10_133_333
    assert round(w - v) == 1_185_965 and round((w - v) / v, 4) == 0.1325


P84 = [(40_000, 7.50, 5.0, 8.25), (25_000, 8.00, 1.5, 8.75), (15_000, 9.00, 3.0, 9.00),
       (10_000, 8.50, 0.75, 9.25)]


def test_problem_8_4():
    occ = sum(a for a, *_ in P84)
    base = sum(a * r for a, r, *_ in P84)
    assert occ == 90_000 and base == R(720_000)
    assert sum(a * r * t for a, r, t, _ in P84) == R(2_268_750)
    assert round(_walt(P84), 2) == 3.15 and round(_walt(P84, False), 2) == 3.22
    r24 = sum(a * r for a, r, t, _ in P84 if t <= 2)
    assert r24 == R(285_000) and round(r24 / base, 3) == 0.396
    mkt = sum(a * m for a, _, _, m in P84)
    assert mkt == R(776_250) and mkt - base == R(56_250) and round((mkt - base) / base, 4) == 0.0781
    assert sum(a * (m - r) for a, r, t, m in P84 if t <= 2) == R(26_250)
    pgi = base + 10_000 * 9.0 + 2.5 * 100_000
    assert pgi == R(1_060_000)
    rec = 2.5 * occ
    egi = base + rec
    opex = 250_000 + 0.03 * egi + 0.10 * 100_000
    noi = egi - opex
    assert (rec, egi, 0.03 * egi, opex, noi) == (R(225_000), R(945_000), R(28_350), R(288_350), R(656_650))
    assert noi - 0.15 * 100_000 - 0.50 * 100_000 == R(591_650)


def test_problem_8_5():
    face = [28 * 1.03 ** t for t in range(10)]
    assert [round(f, 2) for f in face] == [28.00, 28.84, 29.71, 30.60, 31.51, 32.46, 33.43, 34.44,
                                          35.47, 36.53]
    agg = sum(face)
    assert round(agg, 2) == 320.99 and agg == R(28 * (1.03 ** 10 - 1) / 0.03)
    cash = [28 * 2 / 12] + face[1:]
    assert round(cash[0], 2) == 4.67
    agg_c = sum(cash)
    assert round(agg_c, 2) == 297.66
    lc = 0.05 * agg_c
    assert round(lc, 2) == 14.88
    pv, ner = _ner(cash, 55, lc, 0.08)
    assert round(pv, 2) == 189.80 and round(ner, 2) == 17.87
    assert round(ner / 28, 3) == 0.638
    assert round((agg_c - 55 - lc) / 10, 2) == 22.78
    assert round(agg_c / 10, 2) == 29.77


def test_problem_8_6():
    b = hotel.operating_statement(120, 0.68, 125.0, **HOTEL_120)
    o = hotel.operating_statement(120, 0.68 * 0.85, 125.0, **HOTEL_120)
    a = hotel.operating_statement(120, 0.68, 125.0 * 0.85, **HOTEL_120)
    assert b["revpar"] == R(85.0) and o["revpar"] == R(72.25) and a["revpar"] == R(72.25)
    assert round(b["total_revenue"]) == 3_946_380 and round(o["total_revenue"]) == 3_354_423
    assert round(a["total_revenue"]) == 3_354_423
    assert round(b["gop"]) == 1_751_409
    assert [round(x["noi"]) for x in (b, o, a)] == [802_862, 494_933, 351_970]
    assert round(b["noi_margin"], 3) == 0.203
    assert round(o["noi"] / b["noi"] - 1, 3) == -0.384 and round(a["noi"] / b["noi"] - 1, 3) == -0.562
    ft_o = hotel.flow_through(o["noi"] - b["noi"], o["total_revenue"] - b["total_revenue"])
    ft_a = hotel.flow_through(a["noi"] - b["noi"], a["total_revenue"] - b["total_revenue"])
    assert round(ft_o, 3) == 0.520 and round(ft_a, 3) == 0.762
    vals = [x["noi"] / 0.095 for x in (b, o, a)]
    assert [round(v) for v in vals] == [8_451_181, 5_209_820, 3_704_944]
    loan = 0.60 * vals[0]
    assert round(loan) == 5_070_709
    ds = tvm.annual_debt_service(loan, 0.075, 25)
    assert round(ds) == 449_665
    assert [round(x["noi"] / ds, 2) for x in (b, o, a)] == [1.79, 1.10, 0.78]


def test_problem_8_7():
    reserve = 0.25 * 80_000
    ncf = 900_000 - reserve
    v = ncf / 0.0725
    roof = 600_000 / 1.08 ** 3
    hvac = (40_000 - reserve) * tvm.annuity_factor(0.08, 5)
    price = v - 350_000 - roof - hvac
    assert (reserve, ncf) == (20_000, 880_000)
    assert round(v) == 12_137_931 and round(roof) == 476_299 and round(hvac) == 79_854
    assert round(price) == 11_231_777
    ask = 900_000 / 0.0725
    assert round(ask) == 12_413_793
    assert round(ask - price) == 1_182_016 and round((ask - price) / ask, 3) == 0.095
    assert round(price + 350_000) == 11_581_777
    assert round(reserve / 0.0725) == 275_862


def test_problem_8_8():
    vac = 0.06 * 12_000
    assert vac == R(720)
    assert (vac + 1_800) / 100 == R(25.2)
    assert round(vac / 13_800, 4) == 0.0522
    assert round((vac + 1_800 - 60 * 18) / 13_800, 4) == 0.1043
    assert round(16_500 / 260_000, 4) == 0.0635
    assert round(16_500 / 0.0525) == 314_286
    assert round(16_500 / 0.0525 / 260_000, 3) == 1.209
    max_cost = 16_500 / 0.065
    assert round(max_cost) == 253_846 and round(260_000 - max_cost) == 6_154
    assert round(0.065 * 260_000) == 16_900
    assert round(1 + 0.0125 / 0.0525, 3) == 1.238


def test_problem_8_9():
    n = 2_000_000
    v_tx = cre.loaded_cap_value(n, 0.055, 0.024)
    v_ca = cre.loaded_cap_value(n, 0.055, 0.0122)
    assert round(v_tx) == 25_316_456 and round(0.024 * v_tx) == 607_595
    assert round(v_ca) == 29_761_905 and round(0.0122 * v_ca) == 363_095
    w = (n - 60_000) / 0.055
    assert round(w) == 35_272_727 and round(w - v_ca) == 5_510_823
    assert round((w - v_ca) / v_ca, 3) == 0.185
    assert round(0.0122 * v_ca * 1.02 ** 4) == 393_026
    assert round(0.024 * v_tx * 1.03 ** 4) == 683_853
    assert round(v_ca / v_tx - 1, 3) == 0.176


def test_problem_8_10():
    new_tax, old_tax = 0.023 * 30_000_000, 0.023 * 18_000_000
    assert (new_tax, old_tax) == (R(690_000), R(414_000))
    noi = 2_400_000 - (new_tax - old_tax)
    assert noi == R(2_124_000) and round(noi / 30_000_000, 4) == 0.0708
    v = cre.loaded_cap_value(2_400_000 + old_tax, 0.08, 0.023)
    assert round(v) == 27_320_388 and round(v - 1_100_000) == 26_220_388
    assert round(1 - (v - 1_100_000) / 30_000_000, 3) == 0.126
    assert 60_000 / 250_000 == R(0.24)
