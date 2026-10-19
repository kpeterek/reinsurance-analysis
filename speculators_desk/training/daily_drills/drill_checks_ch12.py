"""Independent recomputation of the numeric Chapter 12 drills (D111-D120).

Each function returns the list of part values in the same order and units as
drill_bank_ch12.json (percentages as percent numbers, money in dollars).
"""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import cre, tvm  # noqa: E402
from sdesk import x_cre_distress as xd  # noqa: E402


def d111(i):
    k = tvm.loan_constant(i["new_rate"], i["amort_years"])
    return [100 * k, i["old_dscr"] * i["old_rate_io"] / k]


def d112(i):
    r = xd.reit_implied_cap_rate(i["share_price"], i["shares"], i["debt"], i["preferred"], i["cash"],
                                 i["other_assets"], i["forward_cash_noi"])
    return [100 * r["implied_cap"]]


def d114(i):
    notice = dt.date.fromisoformat(i["notice_date"])
    sale = xd.texas_earliest_sale_date(notice, i["min_notice_days"])
    return [float((sale - notice).days)]


def d115(i):
    s = xd.cre_concentration_screens(i["cld"], i["total_cre"], i["capital"], i["total_cre_36m_ago"])
    sale = xd.sale_needed_for_ratio(i["total_cre"], i["capital"], i["target"], i["sale_price"])
    return [100 * s["cld_ratio"], 100 * s["cre_ratio"], sale["sale_par"]]


def d116(i):
    # independent route: discount each scenario by hand, then cross-check the library
    k = i["required_return"]
    by_hand = sum(s["p"] * (s["recovery"] - s["costs"]) / (1 + k) ** s["years"] for s in i["scenarios"])
    lib = cre.distressed_loan_recovery(1.0, i["scenarios"], k)["expected_pv"]
    assert abs(by_hand - lib) < 1e-6
    return [by_hand]


def d117(i):
    ara = xd.appraisal_reduction_amount(i["principal"], i["accrued_interest"], i["advances"], i["other"],
                                        i["appraisal"], i["haircut"], i["reserves"])
    remaining = max(0.0, i["controlling_class_original"] - ara) / i["controlling_class_original"]
    adv = i["principal"] * i["coupon"] / 12 * (1 - ara / i["principal"])
    return [ara, 100 * remaining, adv]


def d119(i):
    occ_sf = i["sf"] * i["occupancy"]
    comp = (i["target_yield"] * i["competitor_basis"] + i["opex"] + i["leasing_capital"]) / occ_sf
    mine = xd.required_gross_rent(i["your_basis"], i["target_yield"], i["opex"], i["sf"], i["occupancy"],
                                  i["leasing_capital"])
    return [comp, mine]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
