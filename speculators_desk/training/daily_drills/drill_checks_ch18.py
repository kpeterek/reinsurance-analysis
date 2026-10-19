"""Independent checks for Chapter 18 drills D164-D170.

Each function returns the list of part values in the same order and units as the JSON.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import markets as m  # noqa: E402
from sdesk import x_capital_structure as xc  # noqa: E402
from sdesk import x_derivatives as xd  # noqa: E402


def d164(i):
    return [100 * i["implied_vol"] / math.sqrt(i["trading_days"]),
            100 * i["implied_vol"] / math.sqrt(i["weeks"])]


def d165(i):
    parity = i["s"] - i["k"] * math.exp(-i["r"] * i["t"])
    return [parity, m.put_call_parity_gap(i["call"], i["put"], i["s"], i["k"], i["t"], i["r"])]


def d166(i):
    return [i["vega_per_vol_point"] * (i["realized_vol_pts"] - i["implied_vol_pts"]) * i["units"]]


def d167(i):
    kmax = i["noi"] / (i["min_dscr"] * i["notional"]) - i["spread"]
    dscr_a = i["noi"] / (i["notional"] * (i["strike_a"] + i["spread"]))
    pa = xc.cap_premium(i["notional"], i["strike_a"], i["forward"], i["normal_vol"], i["years"])["premium"]
    pb = xc.cap_premium(i["notional"], i["strike_b"], i["forward"], i["normal_vol"], i["years"])["premium"]
    return [100 * kmax, dscr_a, pa, pb]


def d168(i):
    h = xd.min_variance_hedge(i["rho"], i["sigma_exposure"], i["sigma_futures"], i["exposure"],
                              i["futures_price"], i["multiplier"])
    n = round(h["contracts"])
    return [h["hedge_ratio"], h["contracts"], h["effectiveness"],
            n * i["multiplier"] * i["futures_price"] * i["rally"]]


def d169(i):
    dfs = xd.discount_factors_from_zero([i["zero_1y"], i["zero_2y"]], [1, 2], 1)
    sw = xd.swap_value(i["notional"], i["fixed_rate"], dfs, [1, 1])
    return [sw["annuity"], 100 * sw["par_rate"], sw["value_pay_fixed"]]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
