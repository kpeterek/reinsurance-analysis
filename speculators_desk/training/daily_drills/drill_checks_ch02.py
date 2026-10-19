"""Independent recomputation of Chapter 2 drill answers (D071-D078).

Each function returns the list of part values in the same order and units as
``drill_bank_ch02.json`` (percentages as percent numbers, money in dollars).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import x_microstructure as xm  # noqa: E402


def d071(i):
    a = i["a"]
    return [100 * (i["r_star_now"] - a * i["r_star_prev"]) / (1 - a)]


def d072(i):
    s = xm.roll_spread_from_autocov(i["autocov"])
    return [s, 100 * s / i["mid"]]


def d073(i):
    z = xm.standardized_surprise(i["actual"], i["consensus"], i["surprise_sd"])
    dy = xm.yield_change_from_surprise(z, i["bp_per_sd"])
    dc = i["pass_through"] * dy
    return [dy * 1e4, 100 * xm.price_change_from_yield(i["mod_duration"], dy),
            100 * (i["cap0"] / (i["cap0"] + dc) - 1)]


def d074(i):
    vals = [i["noi"] / c for c in i["caps"]]
    before = xm.english_auction_price(vals)["price"]
    after = xm.english_auction_price([i["noi"] / c for c in i["caps"] if c not in i["exits"]])["price"]
    return [before, after, 100 * (after / before - 1)]


def d076(i):
    caps = [c for c, _ in i["comps"]]
    naive = i["noi"] / (sum(caps) / len(caps) / 100)
    adj = [xm.time_adjust_cap(c, idx, i["index_now"]) for c, idx in i["comps"]]
    avg = sum(adj) / len(adj)
    return [naive, avg, i["noi"] / ((avg + i["quality_premium_bp"] / 100) / 100)]


def d078(i):
    out = xm.call_auction_clearing([tuple(x) for x in i["buys"]], [tuple(x) for x in i["sells"]])
    return [out["price"], out["volume"], out["imbalance"]]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
