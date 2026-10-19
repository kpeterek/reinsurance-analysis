"""Independent recomputation of every numeric drill answer using the sdesk library.

Each function returns the list of part values in the same order and units as the
JSON (percentages as percent numbers, money in dollars).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))

from sdesk import cre, fixed_income as fi, hotel, markets as mk, risk, tvm  # noqa: E402,F401


def d001(i):
    return [100 * cre.cap_rate_shock_pct(i["cap_rate_before"], i["cap_rate_after"])]


def d002(i):
    rev = hotel.room_revenue(i["rooms"], i["occupancy"], i["adr"], i["days"])
    lost = rev - hotel.room_revenue(i["rooms"], i["occupancy"] - 0.03, i["adr"], i["days"])
    return [rev, lost]


def d006(i):
    noi0 = i["value0"] * i["cap0"]
    r = cre.value_change_from_cap_and_noi(noi0, i["cap0"], i["noi_change"], i["cap1"])
    out = [r["v1"], 100 * r["pct_change"]]
    for ltv in i["ltvs"]:
        out.append(100 * cre.levered_equity_change(r["v0"], r["v1"], ltv * r["v0"])["pct_change"])
    return out


def d007(i):
    return [100 * risk.drawdown_recovery_required(i["drawdown"])]


def d008(i):
    return [i["noi"] / i["min_debt_yield"]]


def d009(i):
    k = tvm.loan_constant(i["rate"], i["amort_years"])
    return [100 * k, cre.dscr(i["noi"], i["loan"] * k)]


def d010(i):
    return [100 * cre.breakeven_probability(i["gain"], i["loss"])]


def d011(i):
    side = 1 if i["side"] == "long" else -1
    return [mk.futures_pnl(i["entry"], i["exit"], i["contracts"], i["multiplier"], side),
            mk.futures_notional(i["entry"], i["multiplier"], i["contracts"])]


def d012(i):
    side = 1 if i["side"] == "long" else -1
    return [mk.fx_pnl(i["base_amount_eur"], i["entry"], i["exit"], side)]


def d013(i):
    r = fi.price_change_approx(i["price"], i["modified_duration"], 0.0, i["yield_change_bps"] / 10_000)
    return [r["total"], 100 * r["total"] / i["price"]]


def d015(i):
    v = cre.loaded_cap_value(i["noi_before_property_tax"], i["cap_rate"], i["effective_tax_rate_on_value"])
    naive = (i["noi_before_property_tax"] - i["seller_current_tax_bill"]) / i["cap_rate"]
    return [v, naive - v]


CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
