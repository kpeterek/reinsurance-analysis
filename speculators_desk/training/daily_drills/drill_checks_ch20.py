"""Independent checks for Chapter 20 drills D177-D184.

Each function returns the list of part values in the same order and units as the JSON.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import markets, stats  # noqa: E402
from sdesk import x_decision as xd  # noqa: E402


def d177(i):
    # odds form, independent of stats.bayes_posterior
    odds = i["base_rate"] / (1 - i["base_rate"]) * i["sensitivity"] / i["false_positive"]
    return [100 * odds / (1 + odds)]


def d178(i):
    return [i["months"] * markets.norm_cdf(-i["z"]),
            i["months"] * xd.scaled_t_tail(i["z"], i["nu"])]


def d179(i):
    hw = i["t_crit"] * i["sd"] / i["n"] ** 0.5
    return [100 * hw, 100 * (i["mean"] - hw)]


def d180(i):
    e = xd.evpi([[i["gain"], -i["loss"]], [0.0, 0.0]], [i["p_good"], 1 - i["p_good"]])
    return [e["ev_prior"], e["evpi"]]


def d181(i):
    o = i["outcomes"]
    base = sum(o) / len(o)
    return [stats.brier_score(i["forecasts"], o), stats.brier_score([base] * len(o), o)]


def d182(i):
    pay = [[i["npv_clean"], i["npv_contaminated"]], [0.0, 0.0]]
    s = xd.evsi_binary_signal(pay, [i["p_clean"], 1 - i["p_clean"]],
                              [i["p_flag_clean"], i["p_flag_contaminated"]])
    return [s["ev_prior"], s["p_signal_1"], s["evs_1"][0], s["evs_0"][0], s["evsi"], s["evsi"] - i["cost"]]


def d183(i):
    rest = i["wealth"] - i["commit"]
    w = [rest + x for x in i["payoffs"]]
    ew = sum(p * x for p, x in zip(i["probs"], w))
    ce = xd.crra_certainty_equivalent(w, i["probs"], i["gamma"])
    return [ew, ce, ew - ce]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
