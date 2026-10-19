"""Independent recomputation of the Chapter 4 drill answers (D087-D094).

Each function returns the part values in the same order and units as
drill_bank_ch04.json (percentages as percent numbers, money in dollars).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import cre, stats, tvm  # noqa: E402
from sdesk import x_business_cycle as bc  # noqa: E402


def d087(i):
    q = i["qoq_growth"]
    return [100 * bc.annualize_quarterly(q), 100 * (bc.annualize_quarterly(q) - bc.simple_annualized(q))]


def d088(i):
    s, g = i["shares"], i["growth"]
    contrib = {k: s[k] * g[k] for k in s}
    return [100 * contrib["I"], 100 * contrib["C"], 100 * sum(contrib.values())]


def d089(i):
    s = bc.sahm_indicator(i["unemployment_rate"])
    return [s[-1]]


def d091(i):
    return [100 * stats.bayes_posterior(i["prior"], i["p_inv_given_r"], i["p_inv_given_not_r"])]


def d092(i):
    r = cre.operating_leverage(i["revenue"], i["fixed_costs"], i["variable_ratio"], i["revenue_change"])
    return [r["noi1"], 100 * r["pct_change"], r["noi1"] / i["debt_service"]]


def d093(i):
    c = i["counts"]
    net = bc.net_percentage(c["tightened_considerably"], c["tightened_somewhat"],
                            c["eased_somewhat"], c["eased_considerably"], c["respondents"])
    v = i["noi"] / i["cap_rate"]
    m = cre.max_loan(i["noi"], v, i["rate"], i["amort_years"], ltv_max=i["ltv_max"],
                     dscr_min=i["dscr_min"], debt_yield_min=i["debt_yield_min"])
    return [100 * net, m["max_loan"], cre.refinance_gap(i["existing_loan"], m["max_loan"])]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
