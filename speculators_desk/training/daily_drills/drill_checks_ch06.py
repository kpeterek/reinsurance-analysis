"""Independent recomputation of the Chapter 6 drill answers (D016-D025).

Each function returns the list of part values in the same order and units as
``drill_bank_ch06.json`` (percentages as percent numbers, money in dollars).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import cre, fixed_income as fi, tvm, x_rates as xr  # noqa: E402


def d016(i):
    dv01 = i["face"] * i["price"] / 100 * i["mod_duration"] * 0.0001
    return [dv01, dv01 * i["shock_bps"]]


def d017(i):
    p = xr.bill_price_from_discount(i["discount_rate"], i["days"])
    return [p, 100 * xr.bill_bey(p, i["days"]), 100 * xr.bill_effective_annual(p, i["days"])]


def d019(i):
    dv01_short = i["face_10y"] * i["dv01_10y_per100"] / 100
    face_2y = fi.hedge_ratio_dv01(dv01_short, i["dv01_2y_per100"] / 100)
    spread_change = i["dy_10y_bps"] - i["dy_2y_bps"]
    return [face_2y, dv01_short, dv01_short * spread_change]


def d020(i):
    d = xr.cap_spread_decomposition(i["cap_rate"], i["treasury_10y"], i["noi_growth"])
    return [10000 * d["spread"], 100 * d["risk_premium"]]


def d021(i):
    v = i["noi"] / i["cap_rate"]
    k = tvm.loan_constant(i["new_rate"], i["amort_years"])
    m = cre.max_loan(i["noi"], v, i["new_rate"], i["amort_years"],
                     ltv_max=i["ltv_max"], dscr_min=i["dscr_min"])
    return [v, 100 * k, m["max_loan"], cre.refinance_gap(i["balance"], m["max_loan"]),
            cre.dscr(i["noi"], i["balance"] * k)]


def d022(i):
    r = xr.carry_rolldown(i["coupon"], i["years"], i["yield_now"], i["yield_rolled"],
                          i["horizon"], repo_rate=i["repo"])
    return [r["carry"], r["rolldown"], r["total"], r["breakeven_bp"]]


def d024(i):
    r = fi.price_change_approx(100.0, i["mod_duration"], i["convexity"], i["dy"])
    return [r["duration_term"], r["total"]]


def d025(i):
    return [100 * fi.forward_rate(i["spot_1y"], 1, i["spot_2y"], 2)]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
