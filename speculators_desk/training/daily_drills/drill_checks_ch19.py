"""Independent checks for Chapter 19 drills D171-D176.

Each function returns the list of part values in the same order and units as the JSON.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import x_alt_assets as aa  # noqa: E402


def d171(i):
    pic = i["called"]
    return [i["distributed"] / pic, i["nav"] / pic, (i["distributed"] + i["nav"]) / pic]


def d172(i):
    paid = i["hammer"] * (1 + i["buyer_premium"])
    net = i["hammer"] * (1 - i["seller_commission"])
    rt = 1 - net / paid
    return [100 * rt, 100 * (1 - (1 - rt) ** (1 / i["years"]))]


def d173(i):
    # hand formula, independent of the library ks_pme
    c, d, idx = i["calls"], i["distributions"], i["index"]
    num = sum(x / k for x, k in zip(d, idx))
    den = sum(x / k for x, k in zip(c, idx))
    return [sum(d) / sum(c), num / den]


def d174(i):
    v = aa.stale_nav_correction(i["nav"], i["beta"], i["index_move"])
    bid = i["bid_pct_nav"] * i["nav"]
    return [v, 100 * (bid / v - 1)]


def d175(i):
    p, x, n, mu = i["p_top"], i["x_top"], i["n_deals"], i["mean_multiple"]
    return [100 * (1 - p) ** n, (mu - p * x) / (1 - p)]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
