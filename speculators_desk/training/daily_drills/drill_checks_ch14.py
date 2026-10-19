"""Independent recomputation of Chapter 14 drill answers (D136-D142)."""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import x_cre_distress as xd  # noqa: E402


def d136(i):
    notional = i["index"] * i["multiplier"] * i["contracts"]
    loss = i["adverse_points"] * i["multiplier"] * i["contracts"]
    return [notional, loss]


def d137(i):
    dollar_beta = i["beta"] * i["value"]
    return [dollar_beta / (i["futures"] * 50), dollar_beta / (i["futures"] * 5)]


def d138(i):
    ey = 1 / i["forward_pe"]
    return [100 * ey, 100 * (ey - i["tips_yield"])]


def d139(i):
    d = xd.reit_implied_cap_rate(i["price"], i["shares"], i["debt"], i["preferred"], i["cash"], 0.0,
                                 i["forward_noi"])
    # NAV computed directly (independent of reit_nav_per_share)
    gav = i["forward_noi"] / i["private_cap"]
    nav_ps = (gav - i["debt"] - i["preferred"] + i["cash"]) / i["shares"]
    return [100 * d["implied_cap"], nav_ps, 100 * (i["price"] / nav_ps - 1)]


def d140(i):
    f = i["spot"] * math.exp((i["r"] - i["q"]) * i["t"])
    rich = i["quoted"] - f
    return [f, rich, (rich - i["cost_points"]) * 50]


def d142(i):
    dollar_beta = i["asset_beta"] * i["gross_value"]
    n = dollar_beta / (i["futures"] * 50)
    cost = dollar_beta * i["erp"] * i["years"]
    vm = round(n) * 50 * i["futures"] * i["rally"]
    return [n, cost, vm]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
