"""Independent recomputation of the Chapter 7 drill answers (D103-D110).

Each function returns the list of part values in the same order and units as
``drill_bank_ch07.json`` (percentages as percent numbers, money in the stated
currency units).
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import markets as mk  # noqa: E402


def d103(i):
    d, r, g, pb = i["debt_ratio"], i["r_effective"], i["g_nominal"], i["primary_balance"]
    pb_star = d * (r - g) / (1 + g)
    d_next = d * (1 + r) / (1 + g) - pb
    return [100 * pb_star, 100 * d_next]


def d104(i):
    lam = i["cds_spread_bps"] / 10_000 / (1 - i["recovery"])
    return [100 * lam, 100 * (1 - math.exp(-lam * i["years"]))]


def d105(i):
    f = mk.covered_interest_forward(i["spot_usdjpy"], i["r_jpy"], i["r_usd"], 1.0)
    usd = mk.convert(i["investment_jpy"], i["spot_usdjpy"], "JPY", "USD/JPY")
    jpy_end = usd * (1 + i["ust_yield"]) * f
    hedged = jpy_end / i["investment_jpy"] - 1
    return [f, 100 * hedged, 10_000 * (hedged - i["jgb_yield"])]


def d107(i):
    f = mk.covered_interest_forward(i["spot_eurusd"], i["r_usd"], i["r_eur"], 1.0)
    eur0 = mk.convert(i["price_usd"], i["spot_eurusd"], "USD", "EUR/USD")
    end_usd = i["price_usd"] * (1 + i["cap_rate"])
    hedged = mk.convert(end_usd, f, "USD", "EUR/USD") / eur0 - 1
    return [100 * hedged, 10_000 * (hedged - i["domestic_yield"])]


def d108(i):
    loss = i["sovereign_bonds"] * i["mod_duration"] * i["spread_shock_bps"] / 10_000
    e1 = i["equity"] - loss
    a1 = i["assets"] - loss
    return [loss, 100 * e1 / a1, a1 - e1 / i["target_leverage_ratio"]]


def d110(i):
    ca = (i["private_saving"] - i["private_investment"]) + i["government_balance"]
    return [100 * ca, -ca * i["gdp_bn"]]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
