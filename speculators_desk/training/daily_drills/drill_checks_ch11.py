"""Independent recomputation of the Chapter 11 drill answers (D056-D070).

Each function returns the list of part values in the same order and units as
drill_bank_ch11.json (percentages as percent numbers, money in dollars).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import cre, hotel, tvm  # noqa: E402


def d056(i):
    rp = hotel.revpar(i["occupancy"], i["adr"])
    point = 0.01 * i["rooms"] * 365 * i["adr"]
    return [rp, point, point * i["noi_flow_through"] / i["cap_rate"]]


def d057(i):
    x = hotel.indices(i["occ"], i["adr"], i["comp_occ"], i["comp_adr"])
    return [x["mpi"], x["ari"], x["rgi"]]


def d058(i):
    reserve = i["reserve_pct"] * i["total_revenue"]
    noi = i["ebitda"] - reserve
    right = noi / i["cap_rate_noi"]
    wrong = i["ebitda"] / i["cap_rate_noi"]
    return [noi, right, wrong - right]


def d060(i):
    d_rev = i["revenue1"] - i["revenue0"]
    return [100 * hotel.flow_through(i["gop1"] - i["gop0"], d_rev),
            100 * hotel.flow_through(i["noi1"] - i["noi0"], d_rev)]


def d061(i):
    g = i["group_rooms"] * i["nights"] * (i["group_rate"] * (1 - i["fees_pct"]) - i["cpor"]
                                          + i["banquet_per_rn"] * i["banquet_margin"])
    displaced = max(0, i["transient_demand"] - (i["rooms"] - i["base_rooms"] - i["group_rooms"]))
    t = displaced * i["nights"] * (i["transient_adr"] * (1 - i["fees_pct"] - i["transient_acq"]) - i["cpor"])
    r_star = (t / (i["group_rooms"] * i["nights"]) + i["cpor"] - i["banquet_per_rn"] * i["banquet_margin"]) / (1 - i["fees_pct"])
    return [displaced, g - t, r_star]


def d062(i):
    pre = hotel.breakeven_occupancy(i["rooms"], i["adr"], i["fixed_costs"], 0.0, i["cpor"], i["var_pct"],
                                    other_revenue_pct_of_rooms=i["other_pct"])
    post = hotel.breakeven_occupancy(i["rooms"], i["adr"], i["fixed_costs"], i["debt_service"], i["cpor"],
                                     i["var_pct"], other_revenue_pct_of_rooms=i["other_pct"])
    return [100 * pre, 100 * post]


def d063(i):
    out = []
    for gop in i["gop_scenarios"]:
        base = i["base_fee_pct"] * i["total_revenue"]
        acf = gop - base - i["fixed_charges"] - i["reserve_pct"] * i["total_revenue"]
        out.append(i["imf_pct"] * max(0.0, acf - i["priority_pct"] * i["invested"]))
    return out


def d064(i):
    v = i["stabilized_noi"] / i["cap_rate"]
    pa = hotel.pip_adjusted_price(v, i["pip"], i["displacement"], i["carry"], i["contingency"], i["required_profit"])
    return [v, pa["price"], pa["price"] / i["rooms"]]


def d065(i):
    r = cre.max_loan(i["t12_noi"], i["value"], i["rate"], i["amort_years"], ltv_max=i["ltv_max"],
                     dscr_min=i["dscr_min"], debt_yield_min=i["debt_yield_min"])
    return [r["ltv"], r["dscr"], r["debt_yield"], r["max_loan"]]


def d066(i):
    import math
    occ_chg = i["occ"] / i["occ_prior"] - 1
    adr_chg = i["adr"] / i["adr_prior"] - 1
    rp_chg = (i["occ"] * i["adr"]) / (i["occ_prior"] * i["adr_prior"]) - 1
    occ_share = math.log(1 + occ_chg) / math.log(1 + rp_chg)
    return [100 * rp_chg, 100 * occ_share]


def d068(i):
    out = []
    for o in (i["brand"], i["independent"]):
        v = o["noi"] / o["cap"] - o["capex"]
        out.append(v)
    out.append(out[0] - out[1])
    return out


def d069(i):
    cfs = i["monthly_cf_after_ds"]
    cum = peak = 0.0
    worst = 0.0
    for v in cfs + cfs:
        cum += v
        peak = max(peak, cum)
        worst = min(worst, cum - peak)
    return [-worst, -sum(v for v in cfs if v < 0)]


def d070(i):
    v = i["stabilized_noi"] / i["cap"]
    pa = hotel.pip_adjusted_price(v, i["pip"], i["displacement"], i["carry"], i["contingency"], i["required_profit"])
    net_now = pa["price"] * (1 - i["sell_cost"])
    pvs = []
    for s in i["hold_scenarios"]:
        pip = i["pip"] * (1 + s["overrun"])
        cf1 = i["noi_now"] - i["displacement"] - pip
        sale = i["stabilized_noi"] * (1 + i["noi_growth"]) / s["exit_cap"] * (1 - i["sell_cost"])
        cf2 = i["stabilized_noi"] + sale
        pvs.append(tvm.npv(i["discount_rate"], [0.0, cf1, cf2]))
    e_pv = sum(s["p"] * pv for s, pv in zip(i["hold_scenarios"], pvs))
    return [net_now, e_pv, e_pv - net_now]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
