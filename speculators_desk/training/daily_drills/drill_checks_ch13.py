"""Independent checks for Chapter 13 drills D121-D130.

Each function returns the list of part values in the same order and units as the JSON.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import cre, fixed_income as fi, risk, tvm  # noqa: E402
from sdesk import x_options_real as ro  # noqa: E402


def d121(i):
    return [i["bid"] * (1 - i["selling_cost_pct"]) - i["loan_balance"] - i["prepayment"]]


def d122(i):
    return [100 * (i["required_return"] - i["cap_rate"]),
            100 * cre.cap_rate_shock_pct(i["cap_rate"], i["cap_rate_after"])]


def d123(i):
    n = fi.hedge_ratio_dv01(i["exposure_dv01"], i["futures_dv01"])
    return [n, n * i["futures_dv01"] * i["treasury_move_bp"]]


def d124(i):
    return [(i["spread_now_bp"] - i["hist_mean_bp"]) / i["hist_sd_bp"]]


def d125(i):
    res = ro.american_real_option(i["v0"], i["u"], i["d"], i["r"], 1, lambda v, t: v - i["k"], delta=i["delta"])
    return [res["q"], res["option_value"], res["value_of_waiting"]]


def d126(i):
    cash = i["new_loan"] - i["existing"] - i["prepayment"] - i["fee_pct"] * i["new_loan"]
    inc = i["new_loan"] * i["new_rate"] - i["existing"] * i["existing_rate"]
    flows = [-cash] + [inc] * i["years"]
    flows[-1] += i["new_loan"] - i["existing"]
    return [cash, 100 * tvm.irr(flows)]


def d127(i):
    w, v, c = i["weights"], i["vols"], i["corr"]
    s = risk.portfolio_volatility(w, v, c)
    h = len(w) - 1
    rc = w[h] * sum(c[h][j] * v[h] * v[j] * w[j] for j in range(len(w))) / s
    return [100 * s, 100 * rc / s]


def d128(i):
    flows = []
    for t in range(2):
        a = i["a_noi"] * (1 + i["a_stress"][t]) - i["a_ds"]
        h = i["h_noi"] * (1 + i["h_stress"][t]) - i["h_ds"]
        flows.append(a + h)
    value = i["h_noi"] * (1 + i["h_stress"][1]) / i["stress_cap"]
    gap = i["h_loan"] - i["refi_ltv"] * value
    cum, run = [], 0.0
    for t, m in enumerate([0.0, gap]):
        run += flows[t] - m
        cum.append(run)
    return [gap, max(0.0, -min(cum))]


def d130(i):
    f = i["switching_costs"] / i["equity_before_costs"]
    return [100 * ((1 + i["hold_return"]) / (1 - f) ** (1 / i["horizon_years"]) - 1)]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
