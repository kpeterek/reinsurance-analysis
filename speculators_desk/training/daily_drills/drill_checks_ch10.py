"""Independent recomputation of Chapter 10 drill answers (D046-D055)."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import cre, tvm  # noqa: E402
from sdesk import x_capital_structure as xc  # noqa: E402


def d046(i):
    return [i["noi"] / i["min_debt_yield"]]


def d047(i):
    k = tvm.loan_constant(i["rate"], i["amort_years"])
    return [100 * k, cre.dscr(i["noi"], i["loan"] * k)]


def d048(i):
    dy = i["dscr_min"] * i["io_rate"]
    return [100 * dy, cre.max_loan(i["noi"], 1e12, i["io_rate"], None, dscr_min=i["dscr_min"],
                                   interest_only=True)["max_loan"]]


def d050(i):
    v = cre.direct_cap_value(i["noi"], i["cap_rate"])
    m = cre.max_loan(i["noi"], v, i["rate"], i["amort_years"], ltv_max=i["ltv_max"],
                     dscr_min=i["dscr_min"], debt_yield_min=i["debt_yield_min"])
    L = m["max_loan"]
    return [L, cre.refinance_gap(i["balance"], L, i["refi_cost_pct"] * L)]


def d051(i):
    B, k = i["balance"], i["foreclosure_cost"]
    opt = sum(p * max(v - B, 0) for p, v in i["states"]) / (1 + i["equity_rate"])
    fc = i["value_now"] * (1 - k) / (1 + i["lender_rate"])
    ext = sum(p * (B if v >= B else v * (1 - k)) for p, v in i["states"]) / (1 + i["lender_rate"])
    return [opt, fc, ext]


def d052(i):
    t = xc.tranche_losses(i["value"], i["value"], [("s", i["senior"]), ("m", i["mezz"]),
                                                    ("e", i["value"] - i["senior"] - i["mezz"])])
    sds, mds = i["senior"] * i["senior_io_rate"], i["mezz"] * i["mezz_io_rate"]
    return [100 * t[1]["attach"], 100 * t[1]["detach"], i["noi"] / sds, i["noi"] / (sds + mds),
            100 * i["noi"] / (i["senior"] + i["mezz"]), 100 * (1 - t[1]["detach"])]


def d053(i):
    c = xc.cap_premium(i["notional"], i["strike"], i["forward"], i["normal_vol"], i["years"], i["freq"])
    return [c["premium"], c["premium"] / 12]


def d055(i):
    r = cre.distressed_loan_recovery(i["price"], i["scenarios"], i["required_return"])
    return [r["expected_pv"], r["npv"]]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
