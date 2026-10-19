"""Independent checks for Chapter 25 drills D215-D220.

Each function returns the list of part values in the same order and units as the JSON.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import markets as mk, stats  # noqa: E402


def d215(i):
    net = i["long"] - i["short"]
    return [net, 100 * net / i["open_interest"]]


def d216(i):
    return [stats.brier_score(i["forecasts"], i["outcomes"])]


def d217(i):
    es = mk.futures_pnl(i["es_entry"], i["es_exit"], i["es_contracts"], i["multiplier"], side=-1)
    r_m = i["es_exit"] / i["es_entry"] - 1
    sys_ = i["reit_value"] * i["reit_beta"] * r_m
    idio = i["reit_value"] * i["reit_return"] - sys_
    return [es, sys_, idio]


def d218(i):
    dv = i["contracts"] * i["dv01_per_contract"]
    return [dv * i["invalidation_bp"], dv * i["gap_bp"],
            math.floor(i["limit"] / (i["dv01_per_contract"] * i["gap_bp"]))]


def d219(i):
    lrs = i["likelihood_ratios"]
    p_ind = stats.likelihood_ratio_update(i["prior"], math.prod(lrs.values()))
    p_cor = stats.likelihood_ratio_update(
        i["prior"], math.prod(v for k, v in lrs.items() if k != i["correlated_with_lender"]))
    return [100 * p_ind, 100 * p_cor]


def d220(i):
    q, n = i["error_rate"], i["numbers_per_day"]
    return [100 * (1 - (1 - q) ** n), 100 * (1 - (1 - q * (1 - i["check_catch_rate"])) ** n), n * q]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
