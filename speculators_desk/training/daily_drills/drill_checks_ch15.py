"""Independent checks for Chapter 15 drills D143-D149.

Each function returns the list of part values in the same order and units as the JSON.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import markets as mk  # noqa: E402


def d143(i):
    pnl = mk.fx_pnl(i["base_amount"], i["entry"], i["exit"], side=i["side"])
    return [pnl, mk.convert(pnl, i["exit"], "JPY", "USD/JPY")]


def d144(i):
    return [100 * (i["s1"] / i["s0"] - 1), 100 * (i["s0"] / i["s1"] - 1)]


def d145(i):
    f_cip = mk.covered_interest_forward(i["spot"], i["r_usd"], i["r_eur"], 1.0)
    f_mkt = i["spot"] + i["market_points"] / 10_000
    b = i["spot"] * (1 + i["r_usd"]) / f_mkt - 1 - i["r_eur"]
    return [(f_cip - i["spot"]) * 10_000, b * 10_000]


def d146(i):
    c = i["monthly_carry"]
    loss = c + i["crash_spot_move"]
    p = c / (c - loss)
    return [100 * p, 100 * (1 - (1 - p) ** i["months"])]


def d147(i):
    s = mk.fx_pnl(i["hedge_ratio"] * i["equity_gbp"], i["forward"], i["spot_at_roll"], side=-1)
    f_new = mk.covered_interest_forward(i["spot_at_roll"], i["r_usd"], i["r_gbp"], 1.0)
    return [s, f_new, -s - i["reserve_usd"]]


def d149(i):
    hedged = (1 + i["us_cap"]) * (1 + i["r_jpy"]) / (1 + i["r_usd"]) - 1
    return [100 * hedged, (1 + i["us_cap"]) / (1 + i["r_usd"]), (1 + i["jp_yield"]) / (1 + i["r_jpy"])]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
