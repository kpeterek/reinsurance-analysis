"""Reproduces every number in Chapter 11 (Hotels) text, the eight chapter cases,
the historical episode, the problems, and the solutions.

The module doubles as the chapter's calculation engine: run it directly
(``python3 tests/test_ch11_examples.py``) to print every intermediate result.
All inputs are hypothetical [HYPOTHESIS] except the historical STR/BLS/Trepp
figures in ``HIST`` (see references/sources_ch11.md).
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "models" / "python"))

from sdesk import cre, hotel, tvm  # noqa: E402

R = pytest.approx


# =====================================================================
# Shared helper: a USALI-style P&L with an explicit labor model
# =====================================================================

def pl(rooms, occ, adr, *, days=365, other_pct=0.0, cpor=0.0, other_dept_ratio=0.0,
       undist_fixed=0.0, undist_pct=0.0, mgmt_pct=0.0, rooms_pct=0.0, tax=0.0,
       ins=0.0, reserve_pct=0.04):
    """Thin wrapper over sdesk.hotel.operating_statement (keyword names shortened)."""
    return hotel.operating_statement(
        rooms, occ, adr, days=days, other_revenue_pct_of_rooms=other_pct,
        rooms_expense_per_occupied_room=cpor, other_dept_expense_ratio=other_dept_ratio,
        undistributed_fixed=undist_fixed, undistributed_pct_of_revenue=undist_pct,
        mgmt_fee_pct=mgmt_pct, franchise_fee_pct_of_rooms=rooms_pct, property_tax=tax,
        insurance=ins, ffe_reserve_pct=reserve_pct)


# =====================================================================
# Example 11.1 -- RevPAR decomposition and penetration
# =====================================================================

EX1 = dict(rooms=132, occ0=0.74, adr0=142.00, occ1=0.71, adr1=158.50,
           c_occ0=0.72, c_adr0=139.00, c_occ1=0.73, c_adr1=150.00)


def ex11_1():
    e = EX1
    rp0, rp1 = hotel.revpar(e["occ0"], e["adr0"]), hotel.revpar(e["occ1"], e["adr1"])
    crp0, crp1 = e["c_occ0"] * e["c_adr0"], e["c_occ1"] * e["c_adr1"]
    i0 = hotel.indices(e["occ0"], e["adr0"], e["c_occ0"], e["c_adr0"])
    i1 = hotel.indices(e["occ1"], e["adr1"], e["c_occ1"], e["c_adr1"])
    g = rp1 / rp0 - 1
    g_occ, g_adr = e["occ1"] / e["occ0"] - 1, e["adr1"] / e["adr0"] - 1
    # revenue the hotel would have earned had it held its prior RGI
    held = i0["rgi"] / 100 * crp1
    foregone = (held - rp1) * e["rooms"] * 365
    return dict(rp0=rp0, rp1=rp1, g=g, g_occ=g_occ, g_adr=g_adr, crp0=crp0, crp1=crp1,
                cg=crp1 / crp0 - 1, i0=i0, i1=i1, ln_g=math.log(1 + g),
                ln_occ=math.log(1 + g_occ), ln_adr=math.log(1 + g_adr),
                held=held, foregone=foregone)


def test_example_11_1():
    x = ex11_1()
    assert round(x["rp0"], 2) == 105.08
    assert round(x["rp1"], 3) == 112.535
    assert round(x["g"], 4) == 0.0709
    assert round(x["g_occ"], 4) == -0.0405
    assert round(x["g_adr"], 4) == 0.1162
    assert round(x["ln_g"], 4) == round(x["ln_occ"] + x["ln_adr"], 4) == 0.0685
    assert (round(x["crp0"], 2), round(x["crp1"], 2)) == (100.08, 109.50)
    assert round(x["cg"], 4) == 0.0941
    assert [round(x["i0"][k], 1) for k in ("mpi", "ari", "rgi")] == [102.8, 102.2, 105.0]
    assert [round(x["i1"][k], 1) for k in ("mpi", "ari", "rgi")] == [97.3, 105.7, 102.8]
    # independent route: RGI = MPI x ARI / 100
    assert x["i1"]["rgi"] == R(x["i1"]["mpi"] * x["i1"]["ari"] / 100)
    assert round(x["held"], 2) == 114.97
    assert round(x["foregone"], -2) == 117_300


# =====================================================================
# Example 11.2 -- flow-through: rate-driven versus occupancy-driven RevPAR
# =====================================================================

EX2 = dict(rooms=132, occ=0.72, adr=150.0, other_pct=0.05, cpor=36.0, other_dept_ratio=0.60,
           undist_fixed=1_450_000, undist_pct=0.04, mgmt_pct=0.03, rooms_pct=0.115,
           tax=260_000, ins=110_000, reserve_pct=0.04)


def ex11_2():
    e = dict(EX2)
    base = pl(e.pop("rooms"), e.pop("occ"), e.pop("adr"), **e)
    e = dict(EX2)
    rate = pl(e.pop("rooms"), e.pop("occ"), e.pop("adr") * 1.05, **e)
    e = dict(EX2)
    occ = pl(e.pop("rooms"), e.pop("occ") * 1.05, e.pop("adr"), **e)
    out = dict(base=base, rate=rate, occ=occ)
    for k in ("rate", "occ"):
        d_rev = out[k]["total_revenue"] - base["total_revenue"]
        out[k + "_drev"] = d_rev
        out[k + "_ft_gop"] = hotel.flow_through(out[k]["gop"] - base["gop"], d_rev)
        out[k + "_ft_noi"] = hotel.flow_through(out[k]["noi"] - base["noi"], d_rev)
        out[k + "_dnoi"] = out[k]["noi"] - base["noi"]
    out["value_gap_9pct"] = (out["rate_dnoi"] - out["occ_dnoi"]) / 0.09
    return out


def test_example_11_2():
    x = ex11_2()
    b = x["base"]
    assert round(b["rooms_sold"], 1) == 34_689.6
    assert round(b["rooms_revenue"]) == 5_203_440
    assert round(b["total_revenue"]) == 5_463_612
    assert round(b["gop"]) == 2_390_139
    assert round(b["gop_margin"], 4) == 0.4375
    assert round(b["ebitda"]) == 1_257_835
    assert round(b["noi"]) == 1_039_290
    assert round(b["revpar"], 2) == 108.00 and round(b["trevpar"], 2) == 113.40
    assert round(b["goppar"], 2) == 49.61
    assert round(x["rate_drev"]) == round(x["occ_drev"]) == 273_181
    assert round(x["rate_ft_gop"], 4) == 0.9314
    assert round(x["occ_ft_gop"], 4) == 0.7029
    assert round(x["rate_ft_noi"], 4) == 0.7519
    assert round(x["occ_ft_noi"], 4) == 0.5233
    assert round(x["rate_dnoi"]) == 205_406
    assert round(x["occ_dnoi"]) == 142_965
    assert round(x["value_gap_9pct"]) == 693_792
    # independent check of the occupancy case: extra rooms x CPOR and other-dept cost
    extra_rn = b["rooms_sold"] * 0.05
    # other revenue is a % of rooms revenue, identical in both cases, so the GOP gap is CPOR only
    assert (x["rate"]["gop"] - x["occ"]["gop"]) == R(extra_rn * 36)
    assert round(extra_rn * 36) == 62_441
    # degree of operating leverage (%dNOI / %dRevenue) for the two routes
    assert round(x["rate_dnoi"] / b["noi"] / 0.05, 2) == 3.95
    assert round(x["occ_dnoi"] / b["noi"] / 0.05, 2) == 2.75
    # closed-form NOI flow-throughs: v = undistributed% + mgmt% + franchise%/(1+o) + reserve% + other-dept share
    v = 0.04 + 0.03 + 0.115 / 1.05 + 0.04 + 0.60 * 0.05 / 1.05
    assert round(v, 4) == 0.2481
    assert x["rate_ft_noi"] == R(1 - v)
    assert x["occ_ft_noi"] == R(1 - v - 36 / (150 * 1.05))
    assert round(36 / (150 * 1.05), 4) == 0.2286
    # closed-form rate-driven GOP flow-through: 1 - undistributed % = 0.96 on rooms revenue,
    # diluted by the other-revenue department (60% cost ratio) -> (rooms*0.96 + other*0.36)/total
    assert x["rate_ft_gop"] == R((1.0 * 0.96 + 0.05 * 0.36) / 1.05)


# =====================================================================
# Example 11.3 -- the fee stack; EBITDA versus NOI capitalization
# =====================================================================

FEES = dict(royalty=0.055, marketing=0.030, reservation=0.015, loyalty=0.015)


def ex11_3():
    b = ex11_2()["base"]
    rr, tr = b["rooms_revenue"], b["total_revenue"]
    comp = {k: v * rr for k, v in FEES.items()}
    franchise = sum(comp.values())
    mgmt = 0.03 * tr
    fees = franchise + mgmt
    v_noi = b["noi"] / 0.09
    c_ebitda = b["ebitda"] / v_noi
    v_wrong = b["ebitda"] / 0.09
    return dict(comp=comp, franchise=franchise, mgmt=mgmt, fees=fees,
                fees_pct_tr=fees / tr, fees_pct_gop=fees / b["gop"],
                v_noi=v_noi, c_ebitda=c_ebitda, v_wrong=v_wrong, overstatement=v_wrong - v_noi,
                ebitda=b["ebitda"], noi=b["noi"], reserve=b["ffe_reserve"])


def test_example_11_3():
    x = ex11_3()
    assert round(x["comp"]["royalty"]) == 286_189
    assert round(x["comp"]["marketing"]) == 156_103
    assert round(x["comp"]["reservation"]) == 78_052
    assert round(x["comp"]["loyalty"]) == 78_052
    assert round(x["franchise"]) == 598_396
    assert round(x["mgmt"]) == 163_908
    assert round(x["fees"]) == 762_304
    assert round(x["fees_pct_tr"], 4) == 0.1395
    assert round(x["fees_pct_gop"], 4) == 0.3189
    assert round(x["reserve"]) == 218_544
    assert round(x["v_noi"]) == 11_547_670
    assert round(x["c_ebitda"], 4) == 0.1089
    assert round(x["v_wrong"]) == 13_975_942
    assert round(x["overstatement"]) == 2_428_272
    # identity: c_EBITDA = c_NOI x EBITDA / NOI; overstatement = reserve / c
    assert x["c_ebitda"] == R(0.09 * x["ebitda"] / x["noi"])
    assert x["overstatement"] == R(x["reserve"] / 0.09)


# =====================================================================
# Example 11.4 -- how a hotel lender sizes the same NOI
# =====================================================================

EX4 = dict(t12_noi=2_150_000, pro_forma_noi=2_400_000, cap=0.0875, rate=0.075, amort=25)


def ex11_4():
    e = EX4
    value = e["pro_forma_noi"] / e["cap"]
    hotel_loan = cre.max_loan(e["t12_noi"], value, e["rate"], e["amort"], ltv_max=0.60,
                              dscr_min=1.50, debt_yield_min=0.12)
    apt_loan = cre.max_loan(e["t12_noi"], value, e["rate"], e["amort"], ltv_max=0.70,
                            dscr_min=1.25, debt_yield_min=0.08)
    k = tvm.loan_constant(e["rate"], e["amort"])
    ds = hotel_loan["max_loan"] * k
    return dict(value=value, hotel=hotel_loan, apt=apt_loan, k=k, ds=ds,
                ltv_actual=hotel_loan["max_loan"] / value,
                dscr_actual=e["t12_noi"] / ds,
                dy_actual=e["t12_noi"] / hotel_loan["max_loan"],
                noi_drop_to_1x=1 - ds / e["t12_noi"])


def test_example_11_4():
    x = ex11_4()
    assert round(x["value"]) == 27_428_571
    assert round(x["k"], 5) == 0.08868
    h = x["hotel"]
    assert round(h["ltv"]) == 16_457_143
    assert round(h["dscr"]) == 16_163_176
    assert round(h["debt_yield"]) == 17_916_667
    assert h["binding"] == "dscr"
    a = x["apt"]
    assert a["binding"] == "ltv"
    assert round(a["max_loan"]) == 19_200_000
    assert round(a["dscr"]) == 19_395_811
    assert round(x["ds"]) == 1_433_333
    assert round(x["ltv_actual"], 4) == 0.5893
    assert round(x["dy_actual"], 4) == 0.1330
    assert round(x["noi_drop_to_1x"], 4) == 0.3333


# =====================================================================
# Example 11.5 -- segment mix: ADR-maximizing is not contribution-maximizing
# =====================================================================

EX5 = dict(rooms=200, occ=0.75, cpor=40.0,
           seg={"transient": (0.60, 172.0, 0.15, 0.0), "group": (0.25, 148.0, 0.05, 40.0),
                "contract": (0.15, 109.0, 0.00, 0.0)},   # (share of RN, ADR, acquisition cost, ancillary contribution/RN)
           fill_freed=0.60)


def ex11_5():
    e = EX5
    rn = hotel.rooms_sold(e["rooms"], e["occ"])
    adr = sum(sh * a for sh, a, _, _ in e["seg"].values())
    contrib = {k: a * (1 - acq) + anc - e["cpor"] for k, (sh, a, acq, anc) in e["seg"].items()}
    net_rev = {k: a * (1 - acq) + anc for k, (sh, a, acq, anc) in e["seg"].items()}
    freed = e["seg"]["contract"][0] * rn
    gain = e["fill_freed"] * freed * contrib["transient"]
    loss = freed * contrib["contract"]
    adr_after = (e["seg"]["transient"][0] * rn * 172 + e["fill_freed"] * freed * 172
                 + e["seg"]["group"][0] * rn * 148) / (rn - freed + e["fill_freed"] * freed)
    occ_after = (rn - freed + e["fill_freed"] * freed) / (e["rooms"] * 365)
    be_fill = contrib["contract"] / contrib["transient"]
    return dict(rn=rn, adr=adr, revpar=e["occ"] * adr, contrib=contrib, net_rev=net_rev, freed=freed,
                gain=gain, loss=loss, net=gain - loss, adr_after=adr_after, occ_after=occ_after,
                revpar_after=adr_after * occ_after, be_fill=be_fill)


def test_example_11_5():
    x = ex11_5()
    assert x["rn"] == R(54_750)
    assert round(x["adr"], 2) == 156.55 and round(x["revpar"], 2) == 117.41
    assert {k: round(v, 2) for k, v in x["net_rev"].items()} == {"transient": 146.20, "group": 180.60, "contract": 109.00}
    assert {k: round(v, 2) for k, v in x["contrib"].items()} == {"transient": 106.20, "group": 140.60, "contract": 69.00}
    assert x["freed"] == R(8_212.5)
    assert round(x["gain"], 1) == 523_300.5
    assert round(x["loss"], 1) == 566_662.5
    assert round(x["net"]) == -43_362
    assert round(x["adr_after"], 2) == 165.62
    assert round(x["occ_after"], 4) == 0.7050
    assert round(x["revpar_after"], 2) == 116.76
    assert round(x["be_fill"], 4) == 0.6497


# =====================================================================
# Case 11.1 -- select-service: RevPAR up, NOI down
# =====================================================================

C1_ROOMS = 120
C1 = {
    "Y1": dict(occ=0.700, adr=140.00, hk_wage=19.00, hk_hours=0.55, fixed_rooms_labor=360_000,
               cpor_nonlabor=14.00, ota_share=0.18, ota_comm=0.17, ag=380_000, sm=180_000,
               pom=210_000, util=230_000, it=60_000, card_pct=0.025, tax=140_000, ins=70_000),
    "Y2": dict(occ=0.760, adr=136.75, hk_wage=21.00, hk_hours=0.55, fixed_rooms_labor=396_000,
               cpor_nonlabor=15.00, ota_share=0.27, ota_comm=0.17, ag=405_000, sm=190_000,
               pom=225_000, util=245_000, it=64_000, card_pct=0.025, tax=168_000, ins=98_000),
}
C1_COMMON = dict(other_pct=0.03, other_dept_ratio=0.50, mgmt=0.03, franchise=0.11, reserve=0.04)


def c1_pl(p):
    c = C1_COMMON
    sold = hotel.rooms_sold(C1_ROOMS, p["occ"])
    rooms_rev = sold * p["adr"]
    other_rev = c["other_pct"] * rooms_rev
    tr = rooms_rev + other_rev
    hk = sold * p["hk_hours"] * p["hk_wage"]
    nonlabor = sold * p["cpor_nonlabor"]
    ota = rooms_rev * p["ota_share"] * p["ota_comm"]
    rooms_exp = hk + p["fixed_rooms_labor"] + nonlabor + ota
    other_exp = c["other_dept_ratio"] * other_rev
    undist = p["ag"] + p["sm"] + p["pom"] + p["util"] + p["it"] + p["card_pct"] * tr
    gop = tr - rooms_exp - other_exp - undist
    mgmt = c["mgmt"] * tr
    fr = c["franchise"] * rooms_rev
    ebitda = gop - mgmt - fr - p["tax"] - p["ins"]
    res = c["reserve"] * tr
    return dict(sold=sold, revpar=rooms_rev / (C1_ROOMS * 365), rooms_rev=rooms_rev, other_rev=other_rev,
                tr=tr, hk=hk, nonlabor=nonlabor, ota=ota, rooms_exp=rooms_exp, other_exp=other_exp,
                undist=undist, gop=gop, mgmt=mgmt, franchise=fr, tax=p["tax"], ins=p["ins"],
                ebitda=ebitda, reserve=res, noi=ebitda - res)


def case11_1():
    y1, y2 = c1_pl(C1["Y1"]), c1_pl(C1["Y2"])
    # sequential bridge from Y1 to Y2
    steps = [
        ("Volume and rate at Y1 unit costs and Y1 channel mix",
         dict(occ=C1["Y2"]["occ"], adr=C1["Y2"]["adr"])),
        ("OTA channel shift (18% -> 27% of rooms revenue)", dict(ota_share=C1["Y2"]["ota_share"])),
        ("Wage inflation (housekeeping $19 -> $21; fixed rooms labor +10%)",
         dict(hk_wage=C1["Y2"]["hk_wage"], fixed_rooms_labor=C1["Y2"]["fixed_rooms_labor"])),
        ("Non-labor CPOR $14 -> $15", dict(cpor_nonlabor=C1["Y2"]["cpor_nonlabor"])),
        ("Undistributed cost inflation (A&G, S&M, POM, utilities, IT)",
         {k: C1["Y2"][k] for k in ("ag", "sm", "pom", "util", "it")}),
        ("Property tax and insurance", dict(tax=C1["Y2"]["tax"], ins=C1["Y2"]["ins"])),
    ]
    p = dict(C1["Y1"])
    prev = y1["noi"]
    bridge = []
    for label, chg in steps:
        p.update(chg)
        n = c1_pl(p)["noi"]
        bridge.append((label, n - prev))
        prev = n
    assert abs(prev - y2["noi"]) < 1e-6
    d_rev = y2["tr"] - y1["tr"]
    vol_only = bridge[0][1]
    return dict(y1=y1, y2=y2, bridge=bridge, d_rev=d_rev,
                revpar_g=y2["revpar"] / y1["revpar"] - 1,
                ft_gop=hotel.flow_through(y2["gop"] - y1["gop"], d_rev),
                ft_noi=hotel.flow_through(y2["noi"] - y1["noi"], d_rev),
                ft_volume_only=vol_only / d_rev,
                value_y1=y1["noi"] / 0.09, value_y2=y2["noi"] / 0.09,
                ota_cost_per_incremental_rn=None)


def test_case_11_1():
    x = case11_1()
    y1, y2 = x["y1"], x["y2"]
    assert round(y1["revpar"], 2) == 98.00 and round(y2["revpar"], 2) == 103.93
    assert round(x["revpar_g"], 4) == 0.0605
    assert round(y1["sold"]) == 30_660 and round(y2["sold"]) == 33_288
    assert round(y1["rooms_rev"]) == 4_292_400 and round(y2["rooms_rev"]) == 4_552_134
    assert round(y1["tr"]) == 4_421_172 and round(y2["tr"]) == 4_688_698
    assert round(y1["hk"]) == 320_397 and round(y2["hk"]) == 384_476
    assert round(y1["ota"]) == 131_347 and round(y2["ota"]) == 208_943
    assert round(y1["rooms_exp"]) == 1_240_984 and round(y2["rooms_exp"]) == 1_488_739
    assert round(y1["undist"]) == 1_170_529 and round(y2["undist"]) == 1_246_217
    assert round(y1["gop"]) == 1_945_272 and round(y2["gop"]) == 1_885_459
    assert round(y1["franchise"]) == 472_164 and round(y2["franchise"]) == 500_735
    assert round(y1["ebitda"]) == 1_130_473 and round(y2["ebitda"]) == 978_064
    assert round(y1["reserve"]) == 176_847 and round(y2["reserve"]) == 187_548
    assert round(y1["noi"]) == 953_626 and round(y2["noi"]) == 790_516
    assert round(x["d_rev"]) == 267_526
    assert round(x["ft_gop"], 3) == -0.224
    assert round(x["ft_noi"], 3) == -0.610
    vals = [round(v) for _, v in x["bridge"]]
    assert vals == [137_442, -69_648, -72_617, -33_288, -69_000, -56_000]
    assert round(x["ft_volume_only"], 3) == 0.514
    assert round(x["value_y1"]) == 10_595_847 and round(x["value_y2"]) == 8_783_507
    assert sum(v for _, v in x["bridge"]) == R(y2["noi"] - y1["noi"])
    assert round(y2["noi"] / y1["noi"] - 1, 4) == -0.1710
    assert round(y1["gop"] / y1["tr"], 3) == 0.440 and round(y2["gop"] / y2["tr"], 3) == 0.402
    assert round(y1["noi"] / y1["tr"], 3) == 0.216 and round(y2["noi"] / y2["tr"], 3) == 0.169
    # incremental room-nights and what the OTA shift cost per incremental room-night
    d_rn = y2["sold"] - y1["sold"]
    assert round(d_rn) == 2_628
    assert round(69_648 / d_rn, 2) == 26.50


# =====================================================================
# Case 11.2 -- full-service group displacement
# =====================================================================

C2 = dict(rooms=300, nights=3, base_rooms=35, block=180, group_rate=189.0, pickup=0.90,
          resell_released=0.50, group_comm=0.07, banquet_per_rn=110.0, banquet_margin=0.38,
          trans_demand=200, trans_adr=265.0, trans_acq=0.12, outlet_per_rn=30.0, outlet_margin=0.25,
          cpor=45.0, rooms_pct_fees=0.08, mgmt_pct=0.03,
          shoulder_share=0.05, shoulder_adr=219.0)


def c2_contrib_group(rate, c=C2):
    """Contribution per actualized group room-night (rooms + banquet)."""
    return (rate * (1 - c["group_comm"] - c["rooms_pct_fees"] - c["mgmt_pct"]) - c["cpor"]
            + c["banquet_per_rn"] * (c["banquet_margin"] - c["mgmt_pct"]))


def c2_contrib_trans(adr, c=C2):
    return (adr * (1 - c["trans_acq"] - c["rooms_pct_fees"] - c["mgmt_pct"]) - c["cpor"]
            + c["outlet_per_rn"] * (c["outlet_margin"] - c["mgmt_pct"]))


def c2_net(demand, rate=None, c=C2):
    rate = c["group_rate"] if rate is None else rate
    picked = c["block"] * c["pickup"]
    released = c["block"] - picked
    cap_for_trans = c["rooms"] - c["base_rooms"] - c["block"] + c["resell_released"] * released
    accommodated = min(demand, cap_for_trans)
    no_group_accommodated = min(demand, c["rooms"] - c["base_rooms"])
    displaced = no_group_accommodated - accommodated
    shoulder = c["shoulder_share"] * displaced * c["nights"]  # Mon/Fri nights of displaced multi-night stays
    g = picked * c["nights"] * c2_contrib_group(rate, c)
    d = displaced * c["nights"] * c2_contrib_trans(c["trans_adr"], c) + shoulder * c2_contrib_trans(c["shoulder_adr"], c)
    return dict(picked=picked, released=released, cap_for_trans=cap_for_trans,
                displaced=displaced, shoulder=shoulder, group_contrib=g, displaced_contrib=d, net=g - d,
                group_rev=picked * c["nights"] * (rate + c["banquet_per_rn"]),
                displaced_rev=displaced * c["nights"] * (c["trans_adr"] + c["outlet_per_rn"])
                + shoulder * (c["shoulder_adr"] + c["outlet_per_rn"]))


def c2_breakeven_rate(demand, c=C2):
    lo, hi = 0.0, 2000.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if c2_net(demand, mid, c)["net"] > 0:
            hi = mid
        else:
            lo = mid
    return hi


C2_SCEN = [(0.30, 160), (0.50, 200), (0.20, 240)]


def case11_2():
    base = c2_net(C2["trans_demand"])
    scen = [(p, dmd, c2_net(dmd)) for p, dmd in C2_SCEN]
    ev = sum(p * r["net"] for p, dmd, r in scen)
    be = c2_breakeven_rate(C2["trans_demand"])
    be_scen = [(p, dmd, c2_breakeven_rate(dmd)) for p, dmd in C2_SCEN]
    alt = c2_net(90)  # alternate dates: Sun-Tue with weak transient demand
    return dict(g_unit=c2_contrib_group(C2["group_rate"]), t_unit=c2_contrib_trans(C2["trans_adr"]),
                s_unit=c2_contrib_trans(C2["shoulder_adr"]), base=base, scen=scen, ev=ev, be=be,
                be_scen=be_scen, alt=alt, rev_change=base["group_rev"] - base["displaced_rev"])


def test_case_11_2():
    x = case11_2()
    assert round(x["g_unit"], 2) == 148.48
    assert round(x["t_unit"], 2) == 165.65
    assert round(x["s_unit"], 2) == 130.23
    b = x["base"]
    assert b["picked"] == R(162) and b["released"] == R(18) and b["cap_for_trans"] == R(94)
    assert b["displaced"] == R(106) and b["shoulder"] == R(15.9)
    assert round(b["group_contrib"]) == 72_161
    assert round(b["displaced_contrib"]) == 54_747
    assert round(b["net"]) == 17_414
    assert round(b["group_rev"]) == 145_314
    assert round(b["displaced_rev"]) == 97_769
    assert round(x["rev_change"]) == 47_545
    assert [r["displaced"] for _, _, r in x["scen"]] == [66, 106, 146]
    assert [round(r["net"]) for _, _, r in x["scen"]] == [38_073, 17_414, -3_245]
    assert round(x["ev"]) == 19_480
    assert round(x["be"], 2) == 145.30
    assert [round(v, 2) for _, _, v in x["be_scen"]] == [93.46, 145.30, 197.14]
    assert round(x["alt"]["net"]) == 72_161 and x["alt"]["displaced"] == 0
    # independent: break-even rate solves 162*3*g(rate) = displaced contribution
    g_needed = b["displaced_contrib"] / (162 * 3)
    rate = (g_needed + 45 - 110 * 0.35) / (1 - 0.07 - 0.08 - 0.03)
    assert rate == R(x["be"], abs=0.01)


# =====================================================================
# Case 11.3 -- renew the brand, convert, or go independent
# =====================================================================

C3_ROOMS = 140
C3_COMP_REVPAR = 95.00
C3_COMMON = dict(other_pct=0.03, cpor=34.0, other_dept_ratio=0.55, undist_fixed=1_400_000,
                 undist_pct=0.03, mgmt_pct=0.03, tax=190_000, ins=110_000, reserve_pct=0.04)
C3_OPTIONS = {
    "Renew": dict(rgi=108, occ=0.74, fee=0.120, dist=0.04, extra_sm=0, capex=2_240_000,
                  key_money=0, cap=0.0875, ramp_rgi=104),
    "Convert": dict(rgi=101, occ=0.71, fee=0.095, dist=0.05, extra_sm=0, capex=1_260_000,
                    key_money=280_000, cap=0.0900, ramp_rgi=95),
    "Independent": dict(rgi=93, occ=0.68, fee=0.0, dist=0.09, extra_sm=175_000, capex=700_000,
                        key_money=0, cap=0.0950, ramp_rgi=84),
}


def c3_noi(o, rgi):
    revpar = rgi / 100 * C3_COMP_REVPAR
    adr = revpar / o["occ"]
    c = dict(C3_COMMON)
    c["undist_fixed"] += o["extra_sm"]
    return pl(C3_ROOMS, o["occ"], adr, rooms_pct=o["fee"] + o["dist"], **c), adr


def case11_3():
    out = {}
    for k, o in C3_OPTIONS.items():
        st, adr = c3_noi(o, o["rgi"])
        ramp, _ = c3_noi(dict(o, occ=o["occ"] * o["ramp_rgi"] / o["rgi"]), o["ramp_rgi"])
        value = st["noi"] / o["cap"]
        ramp_loss = st["noi"] - ramp["noi"]
        net = value - o["capex"] + o["key_money"] - ramp_loss
        out[k] = dict(adr=adr, revpar=st["revpar"], tr=st["total_revenue"], gop=st["gop"],
                      fees_dist=st["franchise_fee"], noi=st["noi"], value=value, ramp_noi=ramp["noi"],
                      ramp_loss=ramp_loss, net=net, roc=(st["noi"]) / (value) if value else 0)
    # independent break-even RGI to match the Renew net value (bisection on rgi; occ scales with RGI)
    target = out["Renew"]["net"]
    o = C3_OPTIONS["Independent"]

    def net_ind(rgi):
        st, _ = c3_noi(dict(o, occ=o["occ"] * rgi / o["rgi"]), rgi)
        rp, _ = c3_noi(dict(o, occ=o["occ"] * o["ramp_rgi"] / o["rgi"]), o["ramp_rgi"])
        return st["noi"] / o["cap"] - o["capex"] - (st["noi"] - rp["noi"])
    lo, hi = 80.0, 140.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if net_ind(mid) < target else (lo, mid)
    out["ind_breakeven_rgi"] = hi
    # Renew versus Convert: incremental NOI and the return on the incremental PIP
    d_noi = out["Renew"]["noi"] - out["Convert"]["noi"]
    d_cap = (C3_OPTIONS["Renew"]["capex"] - C3_OPTIONS["Convert"]["capex"]
             + C3_OPTIONS["Convert"]["key_money"])
    out["renew_vs_convert"] = dict(d_noi=d_noi, d_capital=d_cap, yield_on_increment=d_noi / d_cap)
    return out


def test_case_11_3():
    x = case11_3()
    exp = {"Renew": (138.65, 102.60, 5_400_146, 949_090, 10_846_748, 98_114, 8_508_633),
           "Convert": (135.14, 95.95, 5_050_136, 819_727, 9_108_077, 149_687, 7_978_390),
           "Independent": (129.93, 88.35, 4_650_126, 647_867, 6_819_653, 244_148, 5_875_505)}
    for k, (adr, rp, tr, noi, v, ramp, net) in exp.items():
        y = x[k]
        assert (round(y["adr"], 2), round(y["revpar"], 2), round(y["tr"]), round(y["noi"]), round(y["value"]),
                round(y["ramp_loss"]), round(y["net"])) == (adr, rp, tr, noi, v, ramp, net), k
    assert round(x["Renew"]["fees_dist"]) == 838_858
    assert round(x["Convert"]["fees_dist"]) == 710_942
    assert round(x["Independent"]["fees_dist"]) == 406_322
    assert round(x["ind_breakeven_rgi"], 1) == 103.2
    r = x["renew_vs_convert"]
    assert round(r["d_noi"]) == 129_363 and r["d_capital"] == 1_260_000
    assert round(r["yield_on_increment"], 4) == 0.1027


# =====================================================================
# Case 11.4 -- management contract: incentive fee and owner's priority
# =====================================================================

C4 = dict(invested=52_000_000, tax=900_000, ins=650_000, reserve=0.04)
C4_SCEN = [("Downturn", 0.25, 17_500_000, 4_200_000), ("Base", 0.50, 22_000_000, 7_040_000),
           ("Strong", 0.25, 24_500_000, 8_820_000)]
C4_CONTRACTS = {
    "Existing": dict(base=0.030, imf=0.20, priority=0.08),
    "Proposed": dict(base=0.020, imf=0.25, priority=0.06),
    "GOP-based": dict(base=0.030, imf_gop=0.10),
}


def c4_split(tr, gop, k, c=C4):
    base = k["base"] * tr
    acf = gop - base - c["tax"] - c["ins"] - c["reserve"] * tr  # available cash flow (= NOI)
    if "imf_gop" in k:
        imf = k["imf_gop"] * gop
    else:
        imf = k["imf"] * max(0.0, acf - k["priority"] * c["invested"])
    return dict(base=base, acf=acf, imf=imf, mgr=base + imf, owner=acf - imf)


def case11_4():
    out = {}
    for name, k in C4_CONTRACTS.items():
        rows = {s: c4_split(tr, gop, k) for s, p, tr, gop in C4_SCEN}
        e_owner = sum(p * rows[s]["owner"] for s, p, _, _ in C4_SCEN)
        e_mgr = sum(p * rows[s]["mgr"] for s, p, _, _ in C4_SCEN)
        out[name] = dict(rows=rows, e_owner=e_owner, e_mgr=e_mgr)
    # GOP level at which the proposed contract starts paying more than the existing one
    lo, hi = 4_000_000, 12_000_000
    tr_of = lambda gop: 22_000_000 * gop / 7_040_000  # hold the base-case margin  # noqa: E731
    for _ in range(200):
        mid = (lo + hi) / 2
        diff = (c4_split(tr_of(mid), mid, C4_CONTRACTS["Proposed"])["mgr"]
                - c4_split(tr_of(mid), mid, C4_CONTRACTS["Existing"])["mgr"])
        lo, hi = (mid, hi) if diff < 0 else (lo, mid)
    out["crossover_gop"] = hi
    out["crossover_tr"] = tr_of(hi)
    out["value_of_fee_change_base"] = (out["Existing"]["rows"]["Base"]["owner"]
                                       - out["Proposed"]["rows"]["Base"]["owner"]) / 0.085
    return out


def test_case_11_4():
    x = case11_4()
    S = ("Downturn", "Base", "Strong")
    ex = x["Existing"]["rows"]
    assert [round(ex[s]["base"]) for s in S] == [525_000, 660_000, 735_000]
    assert [round(ex[s]["acf"]) for s in S] == [1_425_000, 3_950_000, 5_555_000]
    assert [round(ex[s]["imf"]) for s in S] == [0, 0, 279_000]
    pr = x["Proposed"]["rows"]
    assert [round(pr[s]["acf"]) for s in S] == [1_600_000, 4_170_000, 5_800_000]
    assert [round(pr[s]["imf"]) for s in S] == [0, 262_500, 670_000]
    assert [round(pr[s]["owner"]) for s in S] == [1_600_000, 3_907_500, 5_130_000]
    gb = x["GOP-based"]["rows"]
    assert [round(gb[s]["imf"]) for s in S] == [420_000, 704_000, 882_000]
    assert [round(gb[s]["owner"]) for s in S] == [1_005_000, 3_246_000, 4_673_000]
    assert round(x["Existing"]["e_owner"]) == 3_650_250
    assert round(x["Proposed"]["e_owner"]) == 3_636_250
    assert round(x["GOP-based"]["e_owner"]) == 3_042_500
    assert round(x["Existing"]["e_mgr"]) == 714_750
    assert round(x["Proposed"]["e_mgr"]) == 728_750
    assert round(x["GOP-based"]["e_mgr"]) == 1_322_500
    assert round(x["crossover_gop"]) == 6_792_727
    assert round(x["crossover_tr"]) == 21_227_273
    assert round(x["value_of_fee_change_base"]) == 500_000
    # owner's priority: 8% x $52m = $4.16m; 6% = $3.12m
    assert 0.08 * 52_000_000 == R(4_160_000) and 0.06 * 52_000_000 == R(3_120_000)


# =====================================================================
# Case 11.5 -- the seasonal resort cash trap
# =====================================================================

C5_ROOMS = 160
C5_MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
C5_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
C5_OCC = [0.42, 0.50, 0.78, 0.80, 0.82, 0.90, 0.93, 0.85, 0.55, 0.50, 0.40, 0.45]
C5_ADR = [165, 185, 260, 255, 270, 320, 345, 300, 205, 190, 160, 185]
C5 = dict(other_pct=0.35, cpor=55.0, other_dept_ratio=0.65, undist_fixed_month=220_000,
          undist_pct=0.06, mgmt_pct=0.03, dist_pct=0.08, reserve=0.04,
          tax_annual=540_000, tax_month="Jan", ins_annual=720_000, ins_month="Jun",
          loan=21_000_000, rate=0.0725, amort=25, trap_dscr=1.30)


def c5_months(revpar_mult=1.0, c=C5):
    pmt = tvm.payment(c["loan"], c["rate"], c["amort"])
    rows = []
    for m, d, o, a in zip(C5_MONTHS, C5_DAYS, C5_OCC, C5_ADR):
        sold = C5_ROOMS * d * o
        rr = sold * a * revpar_mult
        tr = rr * (1 + c["other_pct"])
        dept = sold * c["cpor"] + c["other_dept_ratio"] * rr * c["other_pct"]
        undist = c["undist_fixed_month"] + c["undist_pct"] * tr
        gop = tr - dept - undist
        fees = c["mgmt_pct"] * tr + c["dist_pct"] * rr
        tax_paid = c["tax_annual"] if m == c["tax_month"] else 0.0
        ins_paid = c["ins_annual"] if m == c["ins_month"] else 0.0
        res = c["reserve"] * tr
        cash_noi = gop - fees - tax_paid - ins_paid - res
        rows.append(dict(month=m, sold=sold, rr=rr, tr=tr, gop=gop, cash_noi=cash_noi,
                         ds=pmt, cf=cash_noi - pmt))
    return rows, pmt


def _max_drawdown_cum(cfs, start=0):
    """Largest decline of cumulative cash from a running peak, rolling through two years."""
    seq = cfs[start:] + cfs[:start]
    cum, peak, worst = 0.0, 0.0, 0.0
    for v in seq + seq:
        cum += v
        peak = max(peak, cum)
        worst = min(worst, cum - peak)
    return -worst


def case11_5():
    rows, pmt = c5_months()
    ann_noi = sum(r["cash_noi"] for r in rows)
    ds = 12 * pmt
    stress, _ = c5_months(0.95)
    s_noi = sum(r["cash_noi"] for r in stress)
    cfs = [r["cf"] for r in rows]
    s_cfs = [r["cf"] for r in stress]
    neg = sum(v for v in cfs if v < 0)
    s_neg = sum(v for v in s_cfs if v < 0)
    return dict(rows=rows, pmt=pmt, ds=ds, noi=ann_noi, dscr=ann_noi / ds, cf=sum(cfs),
                revenue=sum(r["tr"] for r in rows), rooms_rev=sum(r["rr"] for r in rows),
                occ=sum(r["sold"] for r in rows) / (C5_ROOMS * 365),
                adr=sum(r["rr"] for r in rows) / sum(r["sold"] for r in rows),
                peak_to_trough=_max_drawdown_cum(cfs), neg_months=[r["month"] for r in rows if r["cf"] < 0],
                sum_negative=neg, stress_noi=s_noi, stress_dscr=s_noi / ds,
                stress_cf=sum(s_cfs), stress_sum_negative=s_neg,
                stress_peak_to_trough=_max_drawdown_cum(s_cfs), dy=ann_noi / C5["loan"],
                stress_rows=stress)


def test_case_11_5():
    x = case11_5()
    assert round(x["pmt"]) == 151_789
    assert round(x["ds"]) == 1_821_473
    assert round(x["revenue"]) == 13_246_870
    assert round(x["rooms_rev"]) == 9_812_496
    assert round(x["noi"]) == 2_488_834
    assert round(x["dscr"], 3) == 1.366
    assert round(x["dy"], 4) == 0.1185
    assert round(x["occ"], 4) == 0.6596
    assert round(x["adr"], 2) == 254.74
    assert round(x["cf"]) == 667_361
    assert [round(r["cf"]) for r in x["rows"]] == [-728_353, -135_705, 287_531, 265_977, 356_605, -130_849,
                                                    754_264, 492_912, -47_769, -99_659, -211_047, -136_548]
    assert x["neg_months"] == ["Jan", "Feb", "Jun", "Sep", "Oct", "Nov", "Dec"]
    assert round(x["sum_negative"]) == -1_489_929
    assert round(x["peak_to_trough"]) == 1_359_081
    # independent: Sep..Feb cumulative deficit equals the peak-to-trough drawdown
    cf = [r["cf"] for r in x["rows"]]
    assert -(sum(cf[8:]) + sum(cf[:2])) == R(x["peak_to_trough"])
    assert round(x["stress_noi"]) == 2_063_462
    assert round(x["stress_dscr"], 3) == 1.133
    assert round(x["stress_cf"]) == 241_989
    assert round(x["stress_sum_negative"]) == -1_657_826
    assert round(x["stress_peak_to_trough"]) == 1_467_050
    assert round(sum(r["gop"] for r in x["rows"]) / x["revenue"], 3) == 0.412
    assert round(sum(r["cf"] for r in x["rows"][2:8])) == 2_026_442   # Mar-Aug surplus


# =====================================================================
# Case 11.6 -- labor-cost shock and break-even occupancy
# =====================================================================

C6 = dict(rooms=150, occ=0.72, adr=128.0, other_pct=0.03, hk_hours=0.50, wage0=18.00, wage1=21.60,
          nonlabor_cpor=16.0, fixed_labor0=750_000, fixed_labor_growth=0.15, fixed_nonlabor=850_000,
          var_pct=0.21, loan=12_000_000, rate=0.0725, amort=25)


def c6_state(wage, fixed_labor, adr=None, occ=None, hk_hours=None, c=C6):
    adr = c["adr"] if adr is None else adr
    occ = c["occ"] if occ is None else occ
    hk_hours = c["hk_hours"] if hk_hours is None else hk_hours
    sold = hotel.rooms_sold(c["rooms"], occ)
    tr = sold * adr * (1 + c["other_pct"])
    cpor = c["nonlabor_cpor"] + hk_hours * wage
    fixed = fixed_labor + c["fixed_nonlabor"]
    noi = tr * (1 - c["var_pct"]) - sold * cpor - fixed
    ds = tvm.annual_debt_service(c["loan"], c["rate"], c["amort"])
    be_pre = hotel.breakeven_occupancy(c["rooms"], adr, fixed, 0.0, cpor, c["var_pct"],
                                       other_revenue_pct_of_rooms=c["other_pct"])
    be_post = hotel.breakeven_occupancy(c["rooms"], adr, fixed, ds, cpor, c["var_pct"],
                                        other_revenue_pct_of_rooms=c["other_pct"])
    return dict(sold=sold, tr=tr, cpor=cpor, fixed=fixed, noi=noi, ds=ds, dscr=noi / ds,
                be_pre=be_pre, be_post=be_post,
                contrib=adr * (1 + c["other_pct"]) * (1 - c["var_pct"]) - cpor)


def case11_6():
    c = C6
    before = c6_state(c["wage0"], c["fixed_labor0"])
    fl1 = c["fixed_labor0"] * (1 + c["fixed_labor_growth"])
    after = c6_state(c["wage1"], fl1)
    # ADR needed to restore NOI at the same occupancy (closed form)
    sold = before["sold"]
    adr_needed = (before["noi"] + sold * after["cpor"] + after["fixed"]) / (sold * (1 + c["other_pct"]) * (1 - c["var_pct"]))
    # housekeeping hours per occupied room needed to offset only the variable wage effect
    hk_needed = before["cpor"] - c["nonlabor_cpor"]
    hk_needed /= c["wage1"]
    # stress: occupancy -8 points and ADR -6% after the shock
    stress = c6_state(c["wage1"], fl1, adr=c["adr"] * 0.94, occ=c["occ"] - 0.08)
    return dict(before=before, after=after, d_noi=after["noi"] - before["noi"],
                adr_needed=adr_needed, adr_increase=adr_needed / c["adr"] - 1,
                hk_hours_needed=hk_needed, hk_minutes_needed=hk_needed * 60, stress=stress,
                value_loss_9_5=(before["noi"] - after["noi"]) / 0.095)


def test_case_11_6():
    x = case11_6()
    b, a, s = x["before"], x["after"], x["stress"]
    assert round(b["sold"]) == 39_420
    assert round(b["tr"]) == 5_197_133
    assert b["cpor"] == R(25.0) and a["cpor"] == R(26.8)
    assert b["fixed"] == R(1_600_000) and a["fixed"] == R(1_712_500)
    assert round(b["contrib"], 2) == 79.15 and round(a["contrib"], 2) == 77.35
    assert round(b["noi"]) == 1_520_235
    assert round(a["noi"]) == 1_336_779
    assert round(x["d_noi"]) == -183_456
    assert round(b["ds"]) == 1_040_842
    assert round(b["dscr"], 3) == 1.461 and round(a["dscr"], 3) == 1.284
    assert round(b["be_pre"], 4) == 0.3692 and round(a["be_pre"], 4) == 0.4044
    assert round(b["be_post"], 4) == 0.6094 and round(a["be_post"], 4) == 0.6501
    assert round(x["adr_needed"], 2) == 133.72
    assert round(x["adr_increase"], 4) == 0.0447
    assert round(x["hk_minutes_needed"], 1) == 25.0
    assert round(s["sold"]) == 35_040 and round(s["noi"]) == 778_998
    assert round(s["dscr"], 3) == 0.748
    assert round(s["be_post"], 4) == 0.7073
    assert round(x["value_loss_9_5"]) == 1_931_116
    # independent break-even check: at be_post occupancy, contribution covers fixed + DS
    sold_be = b["be_post"] * 150 * 365
    assert sold_be * b["contrib"] == R(b["fixed"] + b["ds"])


# =====================================================================
# Case 11.7 -- BOV under stress with a going-concern allocation
# =====================================================================

C7 = dict(rooms=210, t12_noi=2_100_000, peak_noi=3_600_000,
          noi=[2_450_000, 2_950_000, 3_300_000, 3_399_000, 3_500_970], noi6=3_606_000,
          capex_y1=1_500_000, exit_cap=0.0900, disc=0.1100, sell=0.025,
          direct_cap=0.0950, ffe_per_key=13_000, intangible=1_400_000, land_share=0.15,
          tax_rate=0.024, assess_ratio=1.0, income_tax=0.25, disc_tax=0.08)
C7_SCEN = [("Downside", 0.30, 0.85, 0.0975), ("Base", 0.50, 1.00, 0.0900), ("Upside", 0.20, 1.06, 0.0850)]


def c7_dcf(noi_mult=1.0, exit_cap=None, c=C7):
    exit_cap = c["exit_cap"] if exit_cap is None else exit_cap
    flows = [n * noi_mult for n in c["noi"]]
    flows[0] -= c["capex_y1"]
    return cre.dcf_value(flows, c["noi6"] * noi_mult, exit_cap, c["disc"], c["sell"])


def case11_7():
    c = C7
    base = c7_dcf()
    scen = [(n, p, m, ec, c7_dcf(m, ec)["value"]) for n, p, m, ec in C7_SCEN]
    ev = sum(p * v for _, p, _, _, v in scen)
    # direct cap on forward NOI less the lease-up (recovery) shortfall and capex
    stab = c["noi"][2]
    dc_stab = stab / c["direct_cap"]
    shortfall = (stab - c["noi"][0]) / 1.11 + (stab - c["noi"][1]) / 1.11 ** 2
    dc_asis = dc_stab - shortfall - c["capex_y1"] / 1.11
    t12_cap = c["t12_noi"] / c["direct_cap"]
    tab = round(ev, -5)  # BOV most-probable value: probability-weighted, rounded to $0.1m
    ffe = c["ffe_per_key"] * c["rooms"]
    alloc = {
        "A: fees-deducted (no separate intangible)": dict(real=tab - ffe, ffe=ffe, intangible=0.0),
        "B: business-enterprise allocation": dict(real=tab - ffe - c["intangible"], ffe=ffe,
                                                   intangible=c["intangible"]),
    }
    for a in alloc.values():
        land = c["land_share"] * a["real"]
        bldg = a["real"] - land
        a["land"], a["bldg"] = land, bldg
        a["dep_y1"] = bldg / 39 + a["ffe"] / 7 + a["intangible"] / 15
        a["re_tax"] = c["tax_rate"] * a["real"]
        a["re_plus_bpp_tax"] = c["tax_rate"] * (a["real"] + a["ffe"])
    A, B = list(alloc.values())
    tax_saving = B["re_tax"] - A["re_tax"]  # negative => B lowers tax
    # PV of the income-tax shield difference: intangible over 15 yrs vs building over 39 yrs
    ann_diff = c["intangible"] / 15 - (c["intangible"] * (1 - c["land_share"])) / 39
    pv_shield_diff = c["income_tax"] * ann_diff * tvm.annuity_factor(c["disc_tax"], 15)
    return dict(base=base, scen=scen, ev=ev, dc_stab=dc_stab, shortfall=shortfall, dc_asis=dc_asis,
                t12_cap=t12_cap, tab=tab, ffe=ffe, alloc=alloc, re_tax_saving=-tax_saving,
                re_tax_saving_value=-tax_saving / c["direct_cap"], ann_shield_diff=ann_diff,
                pv_shield_diff=pv_shield_diff,
                peak_value=c["peak_noi"] / 0.085)


def test_case_11_7():
    x = case11_7()
    b = x["base"]
    assert round(b["gross_reversion"]) == 40_066_667
    assert round(b["net_reversion"]) == 39_065_000
    assert round(b["value"]) == 33_162_932
    assert round(b["reversion_share"], 3) == 0.699
    assert [round(v) for *_, v in x["scen"]] == [26_469_966, 33_162_932, 36_679_328]
    assert round(x["ev"]) == 31_858_321
    assert round(x["dc_stab"]) == 34_736_842
    assert round(x["shortfall"]) == 1_049_834
    assert round(x["dc_asis"]) == 32_335_657
    assert round(x["t12_cap"]) == 22_105_263
    assert x["tab"] == 31_900_000
    assert x["ffe"] == 2_730_000
    A, B = list(x["alloc"].values())
    assert round(A["real"]) == 29_170_000 and round(B["real"]) == 27_770_000
    assert round(A["dep_y1"]) == 1_025_756 and round(B["dep_y1"]) == 1_088_577
    assert round(A["re_tax"]) == 700_080 and round(B["re_tax"]) == 666_480
    assert round(x["re_tax_saving"]) == 33_600
    assert round(x["re_tax_saving_value"]) == 353_684
    assert round(x["ann_shield_diff"]) == 62_821
    assert round(x["pv_shield_diff"]) == 134_428
    assert round(x["peak_value"]) == 42_352_941
    # independent DCF check, year by year
    flows = [2_450_000 - 1_500_000, 2_950_000, 3_300_000, 3_399_000, 3_500_970]
    pv = sum(f / 1.11 ** (t + 1) for t, f in enumerate(flows)) + 3_606_000 / 0.09 * 0.975 / 1.11 ** 5
    assert pv == R(b["value"])


# =====================================================================
# Case 11.8 -- disposition timing: sell now or after the PIP
# =====================================================================

C8 = dict(rooms=130, noi_now=1_300_000, noi_stab=1_550_000, cap=0.090, pip=2_340_000,
          buyer_cont=0.15, buyer_disp=260_000, buyer_carry=150_000, buyer_profit=0.15,
          sell_cost=0.025, owner_disc=0.11, owner_cont=0.08, owner_disp=260_000)
C8_SCEN = [("Good", 0.35, 0.0875, 0.00), ("Base", 0.45, 0.0900, 0.08), ("Bad", 0.20, 0.0975, 0.25)]


def c8_sell_now(c=C8):
    v_stab = c["noi_stab"] / c["cap"]
    pa = hotel.pip_adjusted_price(v_stab, c["pip"], c["buyer_disp"], c["buyer_carry"],
                                  c["buyer_cont"], c["buyer_profit"])
    net = pa["price"] * (1 - c["sell_cost"])
    return dict(v_stab=v_stab, **pa, net=net, implied_cap_on_current=c["noi_now"] / pa["price"])


def c8_hold(exit_cap, overrun, c=C8):
    """Owner renovates in year 1 (cost paid mid-year approximated at end of year 1),
    collects year-1 NOI net of displacement and year-2 stabilized NOI, sells at end of
    year 2 on forward (year-3) NOI grown 3%."""
    pip_cost = c["pip"] * (1 + overrun)
    cf1 = c["noi_now"] - c["owner_disp"] - pip_cost
    noi3 = c["noi_stab"] * 1.03
    sale = noi3 / exit_cap * (1 - c["sell_cost"])
    cf2 = c["noi_stab"] + sale
    pv = cf1 / (1 + c["owner_disc"]) + cf2 / (1 + c["owner_disc"]) ** 2
    return dict(pip_cost=pip_cost, cf1=cf1, sale=sale, cf2=cf2, pv=pv)


def case11_8():
    now = c8_sell_now()
    scen = [(n, p, ec, ov, c8_hold(ec, ov)) for n, p, ec, ov in C8_SCEN]
    e_pv = sum(p * h["pv"] for _, p, _, _, h in scen)
    # break-even exit cap (zero overrun -> base overrun 8%) at which hold PV = sell-now net
    lo, hi = 0.06, 0.20
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if c8_hold(mid, C8["owner_cont"])["pv"] > now["net"] else (lo, mid)
    be_cap = lo
    return dict(now=now, scen=scen, e_pv=e_pv, adv=e_pv - now["net"], be_cap=be_cap,
                pv_bad=scen[2][4]["pv"])


def test_case_11_8():
    x = case11_8()
    n = x["now"]
    assert round(n["v_stab"]) == 17_222_222
    assert round(n["pip_all_in"]) == 2_691_000
    assert round(n["required_profit"]) == 403_650
    assert round(n["price"]) == 13_717_572
    assert round(n["net"]) == 13_374_633
    assert round(n["implied_cap_on_current"], 4) == 0.0948
    hs = [h for *_, h in x["scen"]]
    assert [round(h["pip_cost"]) for h in hs] == [2_340_000, 2_527_200, 2_925_000]
    assert [round(h["cf1"]) for h in hs] == [-1_300_000, -1_487_200, -1_885_000]
    assert [round(h["sale"]) for h in hs] == [17_789_571, 17_295_417, 15_965_000]
    assert [round(h["pv"]) for h in hs] == [14_525_259, 13_955_543, 12_517_369]
    assert round(x["e_pv"]) == 13_867_309
    assert round(x["adv"]) == 492_676
    assert round(x["be_cap"], 4) == 0.0939
    # independent check of the buyer's deduction stack
    assert n["v_stab"] - n["price"] == R(2_691_000 + 260_000 + 150_000 + 403_650)


# =====================================================================
# Historical episode -- arithmetic on published STR / BLS / Trepp figures
# =====================================================================

HIST = dict(
    sep2001_occ=0.559, sep2001_occ_pts=-0.106, sep2001_revpar=44.30, sep2001_revpar_chg=-0.234,
    aug2001_occ=0.677, aug2001_revpar=57.08, aug2001_revpar_chg=-0.044,
    y2019=(0.661, 131.21, 86.76), y2020=(0.440, 103.25, 45.48), y2021=(0.576, 124.67, 71.87),
    apr2020=(0.245, 73.23, 17.93), apr2020_revpar_chg=-0.799,
    y2020_reported=dict(occ=-0.333, adr=-0.213, revpar=-0.475),
    bls_accom_apr2020=-839_000, bls_lh_apr2020=-7_700_000, trepp_lodging_jun2020=0.2430,
)


def hist():
    h = HIST
    sep2000_occ = h["sep2001_occ"] - h["sep2001_occ_pts"]
    sep2000_revpar = h["sep2001_revpar"] / (1 + h["sep2001_revpar_chg"])
    sep2001_adr = h["sep2001_revpar"] / h["sep2001_occ"]
    sep2000_adr = sep2000_revpar / sep2000_occ
    o19, a19, r19 = h["y2019"]
    o20, a20, r20 = h["y2020"]
    o21, a21, r21 = h["y2021"]
    # stylized hotel: 2019 GOP margin 38%, 55% of costs fixed in the short run
    margin, fixed_share = 0.38, 0.55
    rev0 = 100.0
    costs0 = rev0 * (1 - margin)
    fixed = costs0 * fixed_share
    var_ratio = (costs0 - fixed) / rev0
    rev1 = rev0 * (1 + h["y2020_reported"]["revpar"])
    gop1 = rev1 * (1 - var_ratio) - fixed
    return dict(sep2000_occ=sep2000_occ, sep2000_revpar=sep2000_revpar, sep2001_adr=sep2001_adr,
                sep2000_adr=sep2000_adr, sep_adr_chg=sep2001_adr / sep2000_adr - 1,
                sep_occ_pct_chg=h["sep2001_occ"] / sep2000_occ - 1,
                occ20_vs19=o20 / o19 - 1, adr20_vs19=a20 / a19 - 1, revpar20_vs19=r20 / r19 - 1,
                revpar20_identity=o20 * a20, revpar21_share=r21 / r19,
                apr_identity=h["apr2020"][0] * h["apr2020"][1],
                gop_stylized_2020=gop1, gop_change=gop1 / (rev0 * margin) - 1)


def test_historical_arithmetic():
    x = hist()
    assert round(x["sep2000_occ"], 3) == 0.665
    assert round(x["sep2000_revpar"], 2) == 57.83
    assert round(x["sep2001_adr"], 2) == 79.25
    assert round(x["sep2000_adr"], 2) == 86.97
    assert round(x["sep_adr_chg"], 3) == -0.089
    assert round(x["sep_occ_pct_chg"], 3) == -0.159
    assert round(x["occ20_vs19"], 3) == -0.334
    assert round(x["adr20_vs19"], 3) == -0.213
    assert round(x["revpar20_vs19"], 3) == -0.476
    assert round(x["revpar20_identity"], 2) == 45.43
    assert round(x["revpar21_share"], 3) == 0.828
    assert round(x["apr_identity"], 2) == 17.94
    assert round(x["gop_stylized_2020"], 2) == 3.75
    assert round(x["gop_change"], 3) == -0.901


# =====================================================================
# Section 11.13 decision exercise -- the opening BOV, rebuilt
# =====================================================================

def decision_exercise():
    e = dict(EX2)
    e.pop("rooms"), e.pop("occ"), e.pop("adr")
    subj = pl(132, EX1["occ1"], EX1["adr1"], **e)
    owner_claim = subj["ebitda"] / 0.09
    v_stab = subj["noi"] / 0.09
    pa = hotel.pip_adjusted_price(v_stab, 14_000 * 132, 90_000, 60_000, 0.10, 0.15)
    # value of restoring the prior RGI (105.0) at the current comp RevPAR, rate-led flow-through
    lift_rev = ex11_1()["foregone"] * 1.05          # rooms revenue plus other revenue at 5% of rooms
    lift_noi = lift_rev * ex11_2()["rate_ft_noi"]
    return dict(subj=subj, owner_claim=owner_claim, v_stab=v_stab, pa=pa, lift_noi=lift_noi,
                lift_value=lift_noi / 0.09)


def test_decision_exercise():
    x = decision_exercise()
    s = x["subj"]
    assert round(s["revpar"], 3) == 112.535
    assert round(s["total_revenue"]) == 5_693_033
    assert round(s["gop"]) == 2_621_173
    assert round(s["ebitda"]) == 1_456_859
    assert round(s["noi"]) == 1_229_138
    assert round(x["owner_claim"]) == 16_187_325
    assert round(x["v_stab"]) == 13_657_088
    assert round(x["pa"]["pip_all_in"]) == 2_032_800
    assert round(x["pa"]["price"]) == 11_169_368
    assert round(x["pa"]["required_profit"]) == 304_920
    assert round(x["lift_noi"]) == 92_647
    assert round(x["lift_value"]) == 1_029_406


# =====================================================================
# Secondary figures quoted in the prose (differences, ratios, per-key values)
# =====================================================================

def test_text_cross_checks():
    # 11.4.3 illustrative apartment DOL and the hotel's
    assert round(1 / 0.6, 2) == 1.67
    assert round(0.7519 / 0.1902, 2) == 3.95
    # Example 11.4: hotel lender lends ~$3.0m less
    x4 = ex11_4()
    assert round((x4["apt"]["max_loan"] - x4["hotel"]["max_loan"]) / 1e6, 2) == 3.04
    # Example 11.5
    x5 = ex11_5()
    assert x5["rn"] - x5["freed"] + 0.6 * x5["freed"] == R(51_465)
    assert 172 - 148 == 24
    assert round(x5["adr_after"] / x5["adr"] - 1, 3) == 0.058
    # Case 11.1
    c = case11_1()
    y1, y2 = c["y1"], c["y2"]
    assert round(y2["rooms_rev"] - y1["rooms_rev"]) == 259_734
    assert round(y2["hk"] - y1["hk"]) == 64_079
    assert round(y2["ota"] - y1["ota"]) == 77_596
    assert round(y2["rooms_exp"] - y1["rooms_exp"]) == 247_755
    assert round(y2["undist"] - y1["undist"]) == 75_688
    assert round(y2["gop"] - y1["gop"]) == -59_813
    assert round(y2["noi"] - y1["noi"]) == -163_111
    assert round(0.76 / 0.70 - 1, 3) == 0.086 and round(136.75 / 140 - 1, 3) == -0.023
    assert sum(v for _, v in c["bridge"][2:]) == R(-230_905, abs=1)
    assert round(26.50 / 136.75, 3) == 0.194
    assert round(c["value_y1"] - c["value_y2"]) == 1_812_340
    assert round(0.55 * 60) == 33
    # Case 11.2
    x = case11_2()
    assert round(318 * x["t_unit"]) == 52_677 and round(15.9 * x["s_unit"]) == 2_071
    assert round(x["t_unit"] - x["g_unit"], 2) == 17.17
    assert round(0.82 * x["be"] - 6.50, 2) == 112.65
    # Case 11.3
    c3 = case11_3()
    assert round(c3["Renew"]["tr"] / 1.03) == 5_242_860
    gap = c3["Renew"]["net"] - c3["Convert"]["net"]
    assert round(gap) == 530_243
    assert round(2_240_000 + gap) == 2_770_243
    # Case 11.4
    c4 = case11_4()
    d = {s: c4["Proposed"]["rows"][s]["owner"] - c4["Existing"]["rows"][s]["owner"]
         for s in ("Downturn", "Base", "Strong")}
    assert {k: round(v) for k, v in d.items()} == {"Downturn": 175_000, "Base": -42_500, "Strong": -146_000}
    assert round(c4["Proposed"]["e_owner"] - c4["Existing"]["e_owner"]) == -14_000
    assert round(c4["Existing"]["e_owner"] - c4["GOP-based"]["e_owner"]) == 607_750
    assert round(7_040_000 / 22_000_000, 2) == 0.32
    # Case 11.5
    c5 = case11_5()
    assert round(1_700_000 / c5["cf"], 2) == 2.55
    # Case 11.6
    c6 = case11_6()
    assert round(39_420 * 1.8) == 70_956
    assert round(c6["d_noi"] / c6["before"]["noi"], 3) == -0.121
    assert round(72 - 100 * c6["before"]["be_post"], 1) == 11.1
    assert round(72 - 100 * c6["after"]["be_post"], 1) == 7.0
    assert round((0.5 * 18) / 21.60 * 21.60, 2) == 9.00
    assert round(128 * 0.94, 2) == 120.32
    # Case 11.7
    c7 = case11_7()
    assert round(1_500_000 / 1.11) == 1_351_351
    assert round(c7["tab"] / 210) == 151_905
    assert round((c7["re_tax_saving_value"] + c7["pv_shield_diff"]) / c7["tab"], 4) == 0.0153
    # Case 11.8
    c8 = case11_8()
    assert round(c8["adv"] / c8["now"]["net"], 3) == 0.037
    assert round(c8["now"]["net"] - c8["pv_bad"]) == 857_264
    assert round(0.05 * 2_340_000 * 1.15) == 134_550 and round(0.05 * 2_691_000) == 134_550
    assert round(c8["now"]["v_stab"] - c8["now"]["price"]) == 3_504_650
    # Decision exercise and errors list
    de = decision_exercise()
    err = de["owner_claim"] - de["v_stab"]
    assert round(err) == 2_530_237
    assert err == R(de["subj"]["ffe_reserve"] / 0.09)
    assert round(err / de["v_stab"], 3) == 0.185
    x3 = ex11_3()
    assert round(x3["overstatement"] / x3["v_noi"], 3) == 0.210
    # Reference sheet: one occupancy point for 132 rooms
    assert round(132 * 365 * 0.01) == 482
    # Historical stylized hotel
    assert round(62 * 0.55, 2) == 34.10 and round(62 * 0.45, 2) == 27.90 and 100 * (1 - 0.475) == R(52.50)


# =====================================================================
# End-of-chapter problems (problems/questions/ch11_problems.md)
# =====================================================================

def test_problem_11_2():
    rp = hotel.revpar(0.68, 140)
    assert rp == R(95.20)
    rev = hotel.room_revenue(150, 0.68, 140)
    assert rev == R(5_212_200)
    assert 0.01 * 150 * 365 * 140 == R(76_650)
    assert 0.11 * rev == R(573_342)


def test_problem_11_3():
    i = hotel.indices(0.66, 172, 0.71, 160)
    assert (round(i["mpi"], 1), round(i["ari"], 1), round(i["rgi"], 1)) == (93.0, 107.5, 99.9)


def test_problem_11_4():
    d_rev = 6_550_000 - 6_200_000
    d_gop = 2_530_000 - 2_480_000
    assert round(d_gop / d_rev, 4) == 0.1429
    expected = 0.75 * d_rev
    assert expected == R(262_500)
    gap = expected - d_gop
    assert gap == R(212_500) == 130_000 + 55_000 + 27_500
    assert round(gap / 0.09) == 2_361_111


def p11_5():
    kw = dict(rooms=100, adr=120.0, fixed_costs=1_250_000, variable_cost_per_occupied_room=28.0,
              variable_pct_of_revenue=0.20, other_revenue_pct_of_rooms=0.02)
    pre = hotel.breakeven_occupancy(debt_service=0.0, **kw)
    post = hotel.breakeven_occupancy(debt_service=550_000, **kw)
    kw["adr"] = 120.0 * 0.92
    post_low = hotel.breakeven_occupancy(debt_service=550_000, **kw)
    contrib = 120 * 1.02 * 0.80 - 28
    return pre, post, post_low, contrib


def test_problem_11_5():
    pre, post, post_low, contrib = p11_5()
    assert round(contrib, 2) == 69.92
    assert round(pre, 4) == 0.4898
    assert round(post, 4) == 0.7053
    assert round(post_low, 4) == 0.7943


def p11_6(rate=175.0):
    group = 120 * 2 * (rate * (1 - 0.10) - 40 + 60 * 0.35)
    displaced_per_night = 190 - (250 - 20 - 120)
    trans = displaced_per_night * 2 * (235 * (1 - 0.15 - 0.10) - 40)
    return group, displaced_per_night, trans, group - trans


def test_problem_11_6():
    g, dpn, t, net = p11_6()
    assert dpn == 80
    assert round(g) == 33_240
    assert round(t) == 21_800
    assert round(net) == 11_440
    # break-even group rate: 240 x (0.9 r - 19) = 21,800
    r_star = (t / 240 + 40 - 21) / 0.90
    assert round(r_star, 2) == 122.04
    assert p11_6(r_star)[3] == R(0, abs=1e-6)


def p11_7(gop, tr=30_000_000):
    base = 0.03 * tr
    acf = gop - base - 2_100_000 - 0.04 * tr
    imf = 0.15 * max(0.0, acf - 0.09 * 70_000_000)
    return base, acf, imf, acf - imf


def test_problem_11_7():
    b, acf, imf, own = p11_7(9_600_000)
    assert (b, acf, imf, own) == (R(900_000), R(5_400_000), R(0), R(5_400_000))
    b, acf, imf, own = p11_7(11_500_000)
    assert (acf, imf, own) == (R(7_300_000), R(150_000), R(7_150_000))
    assert 0.08 * 9_600_000 == R(768_000) and 0.08 * 11_500_000 == R(920_000)
    assert 5_400_000 - 768_000 == R(4_632_000) and 7_300_000 - 920_000 == R(6_380_000)


def test_problem_11_8():
    all_in = 3_200_000 * 1.10
    assert all_in == R(3_520_000)
    need = 0.11 * all_in
    assert need == R(387_200)
    d_rp = need / (160 * 365 * 0.72)
    assert round(d_rp, 2) == 9.21
    assert round(d_rp / 98, 4) == 0.0940
    gain = 6 * 160 * 365 * 0.72
    assert round(gain) == 252_288
    assert round(gain / all_in, 4) == 0.0717
    assert round((gain + 420_000) / all_in, 4) == 0.1910


def p11_9():
    noi, value = 1_600_000, 17_800_000
    r = cre.max_loan(noi, value, 0.074, 25, ltv_max=0.60, dscr_min=1.45, debt_yield_min=0.11)
    k = tvm.loan_constant(0.074, 25)
    ds = r["max_loan"] * k
    dscr_pip = 0.85 * noi / ds
    return r, k, ds, dscr_pip


def test_problem_11_9():
    r, k, ds, dscr_pip = p11_9()
    assert round(r["ltv"]) == 10_680_000
    assert round(r["dscr"]) == 12_553_470
    assert round(r["debt_yield"]) == 14_545_455
    assert r["binding"] == "ltv"
    assert round(k, 5) == 0.08790
    assert round(ds) == 938_771
    assert round(dscr_pip, 3) == 1.449
    assert round(1_600_000 / ds, 3) == 1.704
    # NOI decline that trips a 1.25x cash-management trigger
    assert round(1 - 1.25 * ds / 1_600_000, 4) == 0.2666
    # equity: price 17.8m + 2% costs + PIP 2.0m (equity-funded) - loan
    assert round(17_800_000 * 1.02 + 2_000_000 - r["max_loan"]) == 9_476_000


def test_problem_11_10():
    gap_rev = (104 - 92) * 100 * 365
    assert gap_rev == 438_000
    assert 0.75 * gap_rev == R(328_500)
    assert round(0.75 * gap_rev / 0.095) == 3_457_895


def test_solution_cross_checks():
    assert round(1 / 11, 4) == 0.0909 and round(1 / 11 * 19 / 23, 3) == 0.075
    assert round(0.66 * 172, 2) == 113.52 and round(0.71 * 160, 2) == 113.60
    pre, post, post_low, contrib = p11_5()
    assert round(1_250_000 / contrib) == 17_878 and round(1_800_000 / contrib) == 25_744
    assert round(110.40 * 1.02 * 0.80 - 28, 2) == 62.09
    assert round(100 * (post_low - post), 1) == 8.9
    assert round(21_800 / 240 + 19, 2) == 109.83
    assert 10 * 2 * 136.25 == R(2_725)
    assert round(5.4 / 70, 4) == 0.0771 and 7_150_000 - 6_380_000 == 770_000
    r, k, ds, _ = p11_9()
    assert round(1.25 * ds) == 1_173_463
    noi = decision_exercise()["subj"]["noi"]
    lo = hotel.pip_adjusted_price(noi / 0.0925, 16_500 * 132, 90_000, 60_000, 0.10, 0.15)["price"]
    hi = hotel.pip_adjusted_price(noi / 0.0875, 11_500 * 132, 90_000, 60_000, 0.10, 0.15)["price"]
    assert round(lo / 1e6, 2) == 10.38 and round(hi / 1e6, 2) == 11.98


# =====================================================================
# Main: print everything
# =====================================================================

def _dump():
    import pprint
    for f in (ex11_1, ex11_2, ex11_3, ex11_4, ex11_5, case11_1, case11_2, case11_3, case11_4, case11_5,
              case11_6, case11_7, case11_8, hist, decision_exercise):
        print("=" * 20, f.__name__)
        r = f()
        if f is case11_5:
            for row in r.pop("rows"):
                print({k: (round(v) if isinstance(v, float) else v) for k, v in row.items()})
            for row in r.pop("stress_rows"):
                print("S", {k: (round(v) if isinstance(v, float) else v) for k, v in row.items()})
        pprint.pprint(r, width=140)


if __name__ == "__main__":
    _dump()
