"""Independent recomputation of Chapter 8 drill answers (D026-D035) using the sdesk library.

Each function returns the list of part values in the same order and units as the JSON
(percentages as percent numbers, money in dollars, space in the units stated in the drill).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import cre, tvm  # noqa: E402,F401


def d026(i):
    a = i["rentable_sf"]
    leased = i["leased_sf"]
    physical = (leased - i["dark_sf"]) / a
    economic = (leased - i["free_rent_sf"]) / a
    return [100 * leased / a, 100 * physical, 100 * economic]


def d027(i):
    v = cre.loaded_cap_value(i["noi_pre_tax"], i["cap_rate"], i["tax_rate_on_value"])
    wrong = (i["noi_pre_tax"] - i["seller_tax"]) / i["cap_rate"]
    return [v, wrong - v]


def d028(i):
    spec = i["under_construction_msf"] * (1 - i["preleased_share"])
    return [(i["vacant_msf"] + spec) / i["monthly_absorption_msf"]]


def d030(i):
    r = cre.operating_leverage(i["revenue"], i["fixed_costs"], i["variable_cost_ratio"], i["revenue_change"])
    v0 = r["noi0"] / i["cap_rate"]
    v1 = r["noi1"] / i["cap_rate"]
    eq = cre.levered_equity_change(v0, v1, i["ltv"] * v0)["pct_change"]
    return [r["noi0"], 100 * r["pct_change"], 100 * eq]


def d031(i):
    n = i["units"]
    gpr = n * i["market_rent_monthly"] * 12
    deductions = i["loss_to_lease"] + i["vacancy"] + i["concessions"] + i["bad_debt"]
    egi = gpr * (1 - deductions) + n * i["other_income_monthly_per_unit"] * 12
    opex = n * i["opex_per_unit"] + i["mgmt_fee_pct_egi"] * egi
    noi = egi - opex
    ncf = noi - n * i["reserve_per_unit"]
    return [gpr, egi, noi, ncf]


def d032(i):
    v = (i["seller_noi"] - i["reserve"]) / i["cap_rate"]
    price = v - i["immediate_capex"] * (1 + i["contingency"])
    ask = i["seller_noi"] / i["cap_rate"]
    return [price, ask - price]


def d034(i):
    rents = [t["rent"] for t in i["tenants"]]
    terms = [t["years"] for t in i["tenants"]]
    walt = sum(r * t for r, t in zip(rents, terms)) / sum(rents)
    k = rents.index(max(rents))
    rest = [(r, t) for j, (r, t) in enumerate(zip(rents, terms)) if j != k]
    walt_ex = sum(r * t for r, t in rest) / sum(r for r, _ in rest)
    return [walt, walt_ex]


def d035(i):
    v = cre.loaded_cap_value(i["noi_pre_tax"], i["cap_rate"], i["tax_rate_on_value"])
    wrong = (i["noi_pre_tax"] - i["seller_tax"]) / i["cap_rate"]
    return [v, wrong, wrong - v]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
