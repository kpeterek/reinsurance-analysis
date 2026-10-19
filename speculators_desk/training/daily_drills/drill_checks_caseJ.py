"""Independent recomputation of numeric answers for drills D131-D135 (Case J)."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import tvm  # noqa: E402


def d131(i):
    k = tvm.loan_constant(i["rate"], i["amort_years"])
    lam = i["ltv"]
    return [100 * k, 100 * (i["going_in_cap"] - lam * k) / (1 - lam)]


def d132(i):
    def price(t):
        k = tvm.loan_constant(t["rate"], i["amort_years"])
        return i["noi"] / (t["ltv"] * k + (1 - t["ltv"]) * i["target_coc"])
    pn, pc = price(i["normal"]), price(i["crunch"])
    return [pn, pc, 100 * (pc / pn - 1)]


def d133(i):
    total = i["p_normal_old_noi"] - i["p_crunch_new_noi"]
    first = (i["p_normal_old_noi"] - i["p_normal_new_noi"]) / total
    last = (i["p_crunch_old_noi"] - i["p_crunch_new_noi"]) / total
    return [100 * first, 100 * last]


def d134(i):
    e, l_ = i["early"], i["late"]
    h = i["hurdle"]
    exp_flows = [e["p"] * a + l_["p"] * b for a, b in zip(e["flows"], l_["flows"])]
    e_npv = e["p"] * tvm.npv(h, e["flows"]) + l_["p"] * tvm.npv(h, l_["flows"])
    return [100 * tvm.irr(e["flows"]), 100 * tvm.irr(l_["flows"]), e_npv, 100 * tvm.irr(exp_flows)]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
