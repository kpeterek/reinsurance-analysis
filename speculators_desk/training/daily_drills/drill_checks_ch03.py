"""Independent recomputation of Chapter 3 drill answers (D079-D086).

Each function returns the list of part values in the same order and units as
drill_bank_ch03.json (percentages as percent numbers).
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import stats, x_dynamics as xd  # noqa: E402


def d079(i):
    phi = i["phi_quarterly"]
    return [math.log(0.5) / math.log(phi), phi ** 4]


def d080(i):
    return [100 * stats.likelihood_ratio_update(i["prior"], i["likelihood_ratio"])]


def d081(i):
    m_up = xd.reflexive_loop_gain(i["ltv"], i["theta_up"], i["collateral_bn"], i["impact_per_bn"])
    m_dn = xd.reflexive_loop_gain(i["ltv"], i["theta_down"], i["collateral_bn"], i["impact_per_bn"])
    up = xd.reflexive_path(i["shock"], m_up, 1)
    return [m_up, up["multiplier"], 100 * up["total"], 1 / (1 - m_dn)]


def d082(i):
    b = xd.binomial_wait(i["v0"], i["cost_now"], i["up"], i["down"], i["rf"],
                         i["payout_yield"], i["cost_growth"])
    return [b["npv_now"], b["q"], b["wait_value"]]


def d083(i):
    args = (i["units"], i["debt"], i["price_after_shock"], i["max_ltv"])
    f0 = xd.forced_sale(*args, 0.0)
    f = xd.forced_sale(*args, i["impact"])
    return [f0["units"], f["units"], f["price"], f["equity"]]


def d084(i):
    return [xd.days_to_exit(i["position_m"], i["adv_m"], i["participation"]),
            xd.days_to_exit(i["crowd_total_m"], i["adv_m"], i["participation"])]


def d085(i):
    p = i["p_stay_contraction_quarterly"]
    return [xd.markov_expected_duration(p), p ** 8, p ** i["loan_maturity_quarters"]]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
