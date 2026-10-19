"""Independent checks for Chapter 21 drills D185-D192.

Each function returns the list of part values in the same order and units as the JSON.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import risk  # noqa: E402
from sdesk import x_dynamics as xd  # noqa: E402
from sdesk import x_risk_mgmt as xr  # noqa: E402


def d185(i):
    n = risk.position_size_by_stop(i["capital"], i["risk_fraction"], i["entry"], i["stop"], i["multiplier"])
    return [n, (i["entry"] - 1920) * i["multiplier"] * n]


def d186(i):
    f = risk.kelly_continuous(i["excess_return"], 0.0, i["sigma"])
    return [f, 100 * xr.kelly_growth(f, i["excess_return"], i["sigma"]),
            100 * xr.kelly_growth(i["c"] * f, i["excess_return"], i["sigma"])]


def d187(i):
    p, l, c = i["pd"], i["loss_each"], i["confidence"]
    one = xr.discrete_var_es([0, l], [1 - p, p], c)
    pair = xr.discrete_var_es([0, l, 2 * l], [(1 - p) ** 2, 2 * p * (1 - p), p * p], c)
    return [one["var"], pair["var"], pair["es"]]


def d188(i):
    mc = xr.futures_margin_call(i["account_equity"], i["contracts"], i["multiplier"],
                                i["initial_margin"], i["maintenance_margin"])
    equity = i["account_equity"] - i["price_fall_points"] * i["multiplier"] * i["contracts"]
    call = max(0.0, i["initial_margin"] * i["contracts"] - equity)
    cure = xr.ltv_covenant(i["loan"], i["value"], i["max_ltv"])["cure"](i["value"] * (1 - i["value_decline"]))
    return [mc["trigger_points"], call, cure]


def d189(i):
    g = xr.gap_loss(i["entry"], i["stop"], i["gap_open"], i["contracts"], i["multiplier"])
    hedged = g["planned"] + i["put_premium_points"] * i["multiplier"] * i["contracts"]
    return [g["planned"], g["realized"], hedged]


def d190(i):
    value = i["shares"] * i["price"]
    days = xd.days_to_exit(i["shares"], i["adv"], i["participation"])
    v1 = risk.parametric_var(value, 0.0, i["daily_vol"], i["confidence"])
    vl = v1 * math.sqrt(xr.liquidation_variance_factor(int(round(days))))
    return [days, v1, vl, xr.liquidity_adjusted_var(vl, value, i["stressed_spread"])]


def d192(i):
    dy = i["dy"]
    tsy = i["tsy_value"] * (-i["tsy_mod_duration"] * dy + 0.5 * i["tsy_convexity"] * dy * dy)
    es = i["es_contracts"] * i["es_price"] * i["es_multiplier"] * i["es_return"]
    v1 = i["hotel_value"] * (1 + i["hotel_return"])
    hotel = max(v1 - i["hotel_loan"], 0.0) - i["hotel_equity"]
    tot = tsy + es + hotel
    return [tsy, es, hotel, tot, 100 * tot / i["nav"]]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
