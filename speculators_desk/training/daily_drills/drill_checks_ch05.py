"""Independent checks for Chapter 5 drills D095-D102."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import fixed_income as fi, markets as mk, tvm  # noqa: E402


def d095(i):
    return [100 - i["price"]]


def d096(i):
    return [100 * ((1 + i["nominal"]) / (1 + i["breakeven"]) - 1)]


def d097(i):
    avg = 100 - i["price"]
    r1 = (i["n_days"] * avg - i["pre_days"] * i["r0"]) / (i["n_days"] - i["pre_days"])
    return [r1, 100 * (r1 - i["r0"]) / i["move"]]


def d098(i):
    out = []
    for s in (i["sofr0"], i["sofr1"]):
        interest = i["loan"] * (s + i["spread"]) * 365 / 360
        out += [interest, i["noi"] / interest]
    return out


def d099(i):
    a = i["noi"] / i["dscr"] / tvm.loan_constant(i["rate0"], i["amort_years"])
    b = i["noi"] / i["dscr"] / tvm.loan_constant(i["rate1"], i["amort_years"])
    return [a, b, 100 * (b / a - 1)]


def d100(i):
    pi = i["inflation"]
    return [i["rstar"] + pi + 0.5 * (pi - i["target"]) + 0.5 * i["gap"]]


def d102(i):
    es = mk.futures_pnl(0.0, i["es_points"], i["es_contracts"], i["es_multiplier"], 1)
    p0 = fi.bond_price(i["y0"], i["ust_coupon"], i["ust_years"], i["ust_face"])
    p1 = fi.bond_price(i["y0"] + i["dy"], i["ust_coupon"], i["ust_years"], i["ust_face"])
    dv = fi.dv01(i["y0"], i["ust_coupon"], i["ust_years"], i["ust_face"])
    return [es, p1 - p0, dv, es + p1 - p0]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
