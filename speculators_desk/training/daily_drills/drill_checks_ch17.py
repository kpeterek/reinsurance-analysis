"""Independent recomputation of the numeric Chapter 17 drills (D157-D163).

Each function returns the list of part values in the same order and units as
drill_bank_ch17.json (percentages as percent numbers, money in dollars).
D162 is judgment-only and has no check.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import x_credit as xc  # noqa: E402


def d157(i):
    lam = xc.triangle_hazard(i["spread"], i["recovery"])
    return [100 * lam, 100 * (1 - math.exp(-lam * i["years"]))]


def d158(i):
    lam = -math.log(1 - i["cum_pd"]) / i["years"]
    return [100 * lam, 100 * xc.annual_pd_from_hazard(lam)]


def d159(i):
    loss = i["default_rate"] * i["severity"]
    f = xc.tranche_loss(loss, i["attach"], i["detach"])
    return [100 * f, f * i["tranche_size"]]


def d160(i):
    h = xc.holdco_opco(i["opco_value"], [("S", i["opco_secured"]), ("U", i["opco_unsecured"])],
                       [("H", i["holdco_notes"])])
    rec = 100 * h["holdco"]["by_name"]["H"]["recovery"]
    return [rec, rec / i["price"]]


def d161(i):
    u = xc.cds_upfront_triangle(i["spread"], i["coupon"], i["recovery"], i["rate"], i["years"])
    return [u["rpv01"], 100 * u["upfront"], u["upfront"] * i["notional"]]


def d163(i):
    d = xc.spread_decomposition(i["spread"], i["real_world_pd"], i["recovery"], i["liquidity"])
    return [1e4 * d["expected_loss"], 1e4 * d["risk_premium"], 100 * d["rn_hazard"], d["rn_to_physical"]]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
