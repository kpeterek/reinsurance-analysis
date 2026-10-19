"""Independent recomputation of Chapter 9 drill answers (D036-D045) with the sdesk library.

Each function returns the list of part values in the same order and units as
drill_bank_ch09.json (percentages as percent numbers, money in dollars).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import cre, tvm  # noqa: E402


def d036(i):
    noi6 = i["noi_year5"] * (1 + i["growth"])
    right = cre.direct_cap_value(noi6, i["exit_cap"]) * (1 - i["selling_cost_pct"])
    wrong = cre.direct_cap_value(i["noi_year5"], i["exit_cap"]) * (1 - i["selling_cost_pct"])
    return [right, right - wrong]


def d037(i):
    t = i["tax_rate"] * i["assessment_ratio"]
    v = cre.loaded_cap_value(i["noi_before_tax"], i["cap_rate"], t)
    return [v, cre.direct_cap_value(i["noi_before_tax"], i["cap_rate"]) - v]


def d038(i):
    return [100 * (i["required_return"] - i["cap_rate"] * (1 - i["capex_ratio"]))]


def d039(i):
    stab = cre.direct_cap_value(i["stabilized_noi"], i["cap_rate"])
    return [stab - i["cost_to_stabilize"], cre.direct_cap_value(i["trailing_noi"], i["cap_rate"])]


def d040(i):
    noi0 = 1.0
    r = cre.value_change_from_cap_and_noi(noi0, i["cap0"], i["noi_change"], i["cap1"])
    v0 = r["v0"]
    eq = cre.levered_equity_change(v0, r["v1"], i["ltv"] * v0)
    return [100 * r["pct_change"], 100 * eq["pct_change"]]


def d041(i):
    out = []
    for c in (i["exit_cap"], i["exit_cap_stress"]):
        r = cre.residual_land_value(i["stabilized_noi"] / c, i["hard"], i["soft"], i["financing"],
                                    i["margin"], i["selling_cost_pct"])
        out.append(r["land_value"])
    return out


def _flat_growth_irr(c0, g, exit_cap, n):
    price = 1.0 / c0
    flows = [-price] + [(1 + g) ** (t - 1) for t in range(1, n)]
    flows.append((1 + g) ** (n - 1) + (1 + g) ** n / exit_cap)
    return tvm.irr(flows)


def d042(i):
    a = _flat_growth_irr(i["cap0"], i["growth"], i["cap0"], i["hold"])
    b = _flat_growth_irr(i["cap0"], i["growth"], i["exit_cap_stress"], i["hold"])
    return [100 * a, 100 * b]


def d044(i):
    def irr(c):
        n1, g, n = i["noi1"], i["growth"], i["hold"]
        flows = [-i["price"]] + [n1 * (1 + g) ** t for t in range(n - 1)]
        flows.append(n1 * (1 + g) ** (n - 1) + n1 * (1 + g) ** n / c)
        return tvm.irr(flows)
    lo, hi = 0.03, 0.15
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if irr(mid) > i["target_irr"]:
            lo = mid
        else:
            hi = mid
    return [100 * 0.5 * (lo + hi)]


def d045(i):
    loan = i["ltv"] * i["price"]
    interest = i["rate"] * loan
    out = []
    for c in (i["exit_cap"], i["exit_cap_stress"]):
        sale = i["noi"] / c
        eq = [-(i["price"] - loan)] + [i["noi"] - interest] * (i["hold"] - 1)
        eq.append(i["noi"] - interest + sale - loan)
        out.append(100 * tvm.irr(eq))
    return out


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
