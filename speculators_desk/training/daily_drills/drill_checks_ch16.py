"""Independent checks for Chapter 16 drills D150-D156.

Each function returns the list of part values in the same order and units as the JSON.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import markets  # noqa: E402
from sdesk import x_commodities as xc  # noqa: E402


def d150(i):
    return [markets.futures_pnl(i["entry"], i["exit"], i["contracts"], i["multiplier"], i["side"])]


def d151(i):
    # independent of the ZC spec table: cents -> dollars explicitly
    return [i["side"] * (i["exit_cents"] - i["entry_cents"]) / 100 * i["bushels"] * i["contracts"]]


def d152(i):
    slope = math.log(i["six_month"] / i["front"]) / i["t"]
    y = xc.implied_convenience_yield(i["front"], i["six_month"], i["r"], i["t"], u=i["u"])
    return [100 * slope, 100 * y]


def d153(i):
    roll = -i["contango_per_month"] / (1 + i["contango_per_month"])
    m = i["bill_per_month"] + roll
    n = i["months"]
    return [100 * m, 100 * ((1 + m) ** n - 1), 100 * ((1 + roll) ** n - 1)]


def d154(i):
    t = xc.oil_to_revpar(i["oil_change"], i["rig_elasticity"], i["energy_share"],
                         i["energy_demand_elasticity"], i["supply_change"], i["occ0"], i["adr0"],
                         i["adr_elasticity"])
    return [100 * t["occ1"], t["adr1"], 100 * t["revpar_change"]]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
