"""Case H — Cross-Asset Macro Shock. Reproducible model.

Run:  python3 cases/hypothetical/case_H_cross_asset_macro_shock/case_h_model.py

Every portfolio position, market level, and shock size is hypothetical
[HYPOTHESIS], constructed for teaching. Every number quoted in case_H.md and
case_H_rubric.md is produced here and asserted in tests/test_case_h.py.

Conventions
-----------
* Yields and rates are decimals. Shocks to yields are in decimals (+0.0018 = +18 bp).
* Treasury and corporate bonds: semiannual coupons, priced on a coupon date
  (no accrued interest), via sdesk.fixed_income.
* Futures P&L = side x (exit - entry) x multiplier x contracts (sdesk.markets).
  E-mini S&P 500 multiplier: $50 per index point.
* FX pairs are BASE/QUOTE. EUR/USD 1.1000 means 1 EUR = 1.1000 USD.
* Floating-rate CRE loans accrue interest on an actual/360 basis, so annual
  interest = L x (SOFR + spread) x 365/360. Fixed-rate loans: monthly payments
  at r/12 on a 30-year amortization schedule (sdesk.tvm).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "models" / "python"))

from sdesk import cre, fixed_income as fi, markets as mk, tvm  # noqa: E402

NAV = 400_000_000  # net asset value of the hypothetical family-office book, $

# ---------------------------------------------------------------- the shock
# Hypothetical: core CPI prints +0.6% m/m against a +0.3% consensus. Moves are
# measured from the 8:29 a.m. ET level to the 4:00 p.m. ET close on release day.
SHOCK = {
    "ust_2y_bp": 25,
    "ust_5y_bp": 22,
    "ust_10y_bp": 18,
    "es_from": 6_000.00,
    "es_to": 5_850.00,
    "eurusd_from": 1.1000,
    "eurusd_to": 1.0890,
    "ig_spread_bp": 12,
    "hy_spread_bp": 40,
    "sofr_12m_avg_bp": 25,       # repricing of the expected 12-month average SOFR path
    "cre_fixed_spread_bp": 15,   # lender spread over the 10-year widens
    "eur_local_equity": -0.020,  # local-currency move of the euro property shares
}

# ---------------------------------------------------------------- positions
UST10 = dict(face=60_000_000, coupon=0.0425, years=10, y0=0.0425)
UST2 = dict(face=40_000_000, coupon=0.0390, years=2, y0=0.0390)
ES = dict(contracts=50, multiplier=50.0, side=1)
EUR_EQUITY_LOCAL = 25_000_000   # EUR market value of euro-listed property-company shares, unhedged
IG = dict(mv=35_000_000, coupon=0.0510, years=8, y0=0.0510)   # priced at par
HY = dict(mv=15_000_000, coupon=0.0750, years=5, y0=0.0750)   # priced at par

# Floating-rate hotel loan (bridge), 100%-owned hotel
HOTEL = dict(loan=48_000_000, spread=0.0340, sofr0=0.0385, cap_strike=0.0450,
             noi=4_600_000, cash_trap_dscr=1.20, value_cap_rate=0.0700)

# Multifamily with a maturing loan to be refinanced fixed-rate in about five months
MF = dict(noi=3_300_000, existing_balance=42_000_000, ust10=0.0425, spread=0.0165,
          amort=30, dscr_min=1.25, ltv_max=0.65, debt_yield_min=0.075,
          appraisal_cap=0.0550, refi_cost_pct=0.01)

# Private-market translation assumptions [HYPOTHESIS]
CAP_PASS_THROUGH = 0.50       # share of the 10-year move that reaches cap rates in the base case
CAP_SPREAD_ADD_BP = 6         # plus a risk-premium widening, bp
APPRAISAL_ALPHA = 0.35        # weight of current economic value in each quarter's appraisal


# ---------------------------------------------------------------- liquid book
def bond_leg(face: float, coupon: float, years: float, y0: float, dy: float) -> dict:
    p0 = fi.bond_price(y0, coupon, years, face)
    p1 = fi.bond_price(y0 + dy, coupon, years, face)
    d = fi.dv01(y0, coupon, years, face)
    dmod = fi.modified_duration(y0, coupon, years)
    conv = fi.convexity(y0, coupon, years)
    return {"p0": p0, "p1": p1, "pnl": p1 - p0, "dv01": d, "dv01_approx_pnl": -d * dy * 1e4,
            "mod_duration": dmod, "convexity": conv}


def treasuries() -> dict:
    t10 = bond_leg(UST10["face"], UST10["coupon"], UST10["years"], UST10["y0"], SHOCK["ust_10y_bp"] / 1e4)
    t2 = bond_leg(UST2["face"], UST2["coupon"], UST2["years"], UST2["y0"], SHOCK["ust_2y_bp"] / 1e4)
    return {"t10": t10, "t2": t2, "total": t10["pnl"] + t2["pnl"], "dv01_total": t10["dv01"] + t2["dv01"]}


def equity_futures() -> dict:
    pnl = mk.futures_pnl(SHOCK["es_from"], SHOCK["es_to"], ES["contracts"], ES["multiplier"], ES["side"])
    notional = mk.futures_notional(SHOCK["es_from"], ES["multiplier"], ES["contracts"])
    wrong_mult = mk.futures_pnl(SHOCK["es_from"], SHOCK["es_to"], ES["contracts"], 250.0, ES["side"])
    return {"pnl": pnl, "notional": notional, "pct": SHOCK["es_to"] / SHOCK["es_from"] - 1,
            "pnl_if_250_multiplier": wrong_mult}


def fx_translation() -> dict:
    s0, s1 = SHOCK["eurusd_from"], SHOCK["eurusd_to"]
    usd0 = mk.convert(EUR_EQUITY_LOCAL, s0, "EUR", "EUR/USD")
    local1 = EUR_EQUITY_LOCAL * (1 + SHOCK["eur_local_equity"])
    usd1 = mk.convert(local1, s1, "EUR", "EUR/USD")
    local_effect = mk.convert(local1 - EUR_EQUITY_LOCAL, s0, "EUR", "EUR/USD")
    fx_effect = mk.fx_pnl(local1, s0, s1, side=1)
    fx_chg = s1 / s0 - 1
    ret = mk.unhedged_foreign_return(SHOCK["eur_local_equity"], fx_chg)
    hedge = mk.fx_pnl(EUR_EQUITY_LOCAL, s0, s1, side=-1)  # short EUR forward on the starting notional
    # Wrong direction: treating 1.1000 as EUR per USD (dividing instead of multiplying)
    wrong_usd0 = EUR_EQUITY_LOCAL / s0
    return {"usd0": usd0, "usd1": usd1, "pnl": usd1 - usd0, "local_effect": local_effect,
            "fx_effect": fx_effect, "fx_change": fx_chg, "usd_return": ret, "hedge_pnl": hedge,
            "hedged_pnl": usd1 - usd0 + hedge, "wrong_usd0": wrong_usd0}


def credit_leg(mv: float, coupon: float, years: float, y0: float, rate_bp: float, spread_bp: float) -> dict:
    dmod = fi.modified_duration(y0, coupon, years)
    conv = fi.convexity(y0, coupon, years)
    rate_loss = -mv * dmod * rate_bp / 1e4
    spread_loss = -mv * dmod * spread_bp / 1e4
    dy = (rate_bp + spread_bp) / 1e4
    full = fi.bond_price(y0 + dy, coupon, years, mv) - fi.bond_price(y0, coupon, years, mv)
    return {"mod_duration": dmod, "convexity": conv, "rate_loss": rate_loss, "spread_loss": spread_loss,
            "duration_total": rate_loss + spread_loss, "full_reprice": full}


def credit() -> dict:
    ig = credit_leg(IG["mv"], IG["coupon"], IG["years"], IG["y0"], SHOCK["ust_5y_bp"], SHOCK["ig_spread_bp"])
    hy = credit_leg(HY["mv"], HY["coupon"], HY["years"], HY["y0"], SHOCK["ust_5y_bp"], SHOCK["hy_spread_bp"])
    return {"ig": ig, "hy": hy, "total": ig["full_reprice"] + hy["full_reprice"],
            "spread_only": ig["spread_loss"] + hy["spread_loss"]}


def day_one() -> dict:
    t = treasuries()
    e = equity_futures()
    f = fx_translation()
    c = credit()
    lines = {"Treasuries (2y + 10y)": t["total"], "ES futures": e["pnl"],
             "Euro property shares (USD)": f["pnl"], "Credit (IG + HY)": c["total"]}
    total = sum(lines.values())
    return {"lines": lines, "total": total, "pct_nav": total / NAV}


# ---------------------------------------------------------------- private CRE
def act360_interest(loan: float, rate: float) -> float:
    return loan * rate * 365.0 / 360.0


def hotel_floating() -> dict:
    h = HOTEL
    sofr1 = h["sofr0"] + SHOCK["sofr_12m_avg_bp"] / 1e4
    i0 = act360_interest(h["loan"], h["sofr0"] + h["spread"])
    i1 = act360_interest(h["loan"], sofr1 + h["spread"])
    capped_max = act360_interest(h["loan"], h["cap_strike"] + h["spread"])
    # SOFR at which DSCR hits the cash-trap level (cap not yet in the money below the strike)
    sofr_trap = h["noi"] / h["cash_trap_dscr"] / (h["loan"] * 365 / 360) - h["spread"]
    # NOI decline that alone would trip the trap at the shocked rate
    noi_trap = h["cash_trap_dscr"] * i1
    value = cre.direct_cap_value(h["noi"], h["value_cap_rate"])
    return {"value": value, "ltv": h["loan"] / value, "sofr1": sofr1, "interest0": i0, "interest1": i1, "delta_interest": i1 - i0,
            "dscr0": h["noi"] / i0, "dscr1": h["noi"] / i1, "dscr_at_cap": h["noi"] / capped_max,
            "interest_at_cap": capped_max, "sofr_trap": sofr_trap, "noi_trap": noi_trap,
            "noi_cushion_pct": 1 - noi_trap / h["noi"], "wrong_360_interest1": h["loan"] * (sofr1 + h["spread"]),
            "per_bp_annual": act360_interest(h["loan"], 0.0001)}


def mf_refi() -> dict:
    m = MF
    r0 = m["ust10"] + m["spread"]
    r1 = m["ust10"] + SHOCK["ust_10y_bp"] / 1e4 + m["spread"] + SHOCK["cre_fixed_spread_bp"] / 1e4
    appraised = cre.direct_cap_value(m["noi"], m["appraisal_cap"])
    s0 = cre.max_loan(m["noi"], appraised, r0, m["amort"], ltv_max=m["ltv_max"], dscr_min=m["dscr_min"],
                      debt_yield_min=m["debt_yield_min"])
    s1 = cre.max_loan(m["noi"], appraised, r1, m["amort"], ltv_max=m["ltv_max"], dscr_min=m["dscr_min"],
                      debt_yield_min=m["debt_yield_min"])
    k0, k1 = tvm.loan_constant(r0, m["amort"]), tvm.loan_constant(r1, m["amort"])
    cost = m["existing_balance"] * m["refi_cost_pct"]
    gap0 = cre.refinance_gap(m["existing_balance"], s0["max_loan"], cost)
    gap1 = cre.refinance_gap(m["existing_balance"], s1["max_loan"], cost)
    ds_existing_balance_at_r1 = tvm.annual_debt_service(m["existing_balance"], r1, m["amort"])
    # proceeds sensitivity to the 10-year (DSCR-bound), $ per bp, by central difference
    h = 0.0001
    p_up = m["noi"] / m["dscr_min"] / tvm.loan_constant(r0 + h, m["amort"])
    p_dn = m["noi"] / m["dscr_min"] / tvm.loan_constant(r0 - h, m["amort"])
    proceeds_per_bp = (p_dn - p_up) / 2
    t10_dv01_per_face = fi.dv01(UST10["y0"], UST10["coupon"], UST10["years"], 1.0)
    hedge_face = fi.hedge_ratio_dv01(proceeds_per_bp, t10_dv01_per_face)
    r_10y_only = r0 + SHOCK["ust_10y_bp"] / 1e4
    s_10y_only = cre.max_loan(m["noi"], appraised, r_10y_only, m["amort"], ltv_max=m["ltv_max"],
                              dscr_min=m["dscr_min"], debt_yield_min=m["debt_yield_min"])
    loss_10y_part = s0["max_loan"] - s_10y_only["max_loan"]
    # P&L of a short 10-year Treasury hedge of hedge_face, under the same 18 bp shock
    p0 = fi.bond_price(UST10["y0"], UST10["coupon"], UST10["years"], hedge_face)
    p1 = fi.bond_price(UST10["y0"] + SHOCK["ust_10y_bp"] / 1e4, UST10["coupon"], UST10["years"], hedge_face)
    hedge_pnl = -(p1 - p0)
    return {"r_10y_only": r_10y_only, "proceeds_loss_10y_part": loss_10y_part,
            "proceeds_loss_spread_part": (s0["max_loan"] - s1["max_loan"]) - loss_10y_part,
            "hedge_pnl": hedge_pnl, "r0": r0, "r1": r1, "k0": k0, "k1": k1, "appraised": appraised, "sized0": s0, "sized1": s1,
            "proceeds_change": s1["max_loan"] - s0["max_loan"], "gap0": gap0, "gap1": gap1,
            "dscr_full_balance_r1": m["noi"] / ds_existing_balance_at_r1,
            "proceeds_per_bp": proceeds_per_bp, "hedge_face": hedge_face, "refi_cost": cost}


def private_value_path(quarters: int = 4) -> dict:
    """Economic (transaction-based) value versus a smoothed appraisal.

    Economic cap rate moves immediately by pass-through x d10y + spread add.
    Appraisal: A_t = alpha V*_t + (1 - alpha) A_{t-1}, with V* held at the new level.
    """
    m = MF
    c0 = m["appraisal_cap"]
    c1 = c0 + CAP_PASS_THROUGH * SHOCK["ust_10y_bp"] / 1e4 + CAP_SPREAD_ADD_BP / 1e4
    v0 = cre.direct_cap_value(m["noi"], c0)
    v1 = cre.direct_cap_value(m["noi"], c1)
    path = []
    a = v0
    for _ in range(quarters):
        a = APPRAISAL_ALPHA * v1 + (1 - APPRAISAL_ALPHA) * a
        path.append(a)
    gap_pct = v0 / v1 - 1   # seller's anchor (old appraisal) over buyer's economic bid
    # cap rate a buyer needs so that going-in yield equals the shocked fixed coupon (no negative leverage)
    return {"c1": c1, "v0": v0, "v1": v1, "pct": v1 / v0 - 1, "appraisal_path": path,
            "bid_ask_gap_pct": gap_pct, "remaining_after_4q": (path[-1] - v1) / (v0 - v1)}


def summary() -> dict:
    return {"day_one": day_one(), "hotel": hotel_floating(), "mf": mf_refi(), "private": private_value_path()}


if __name__ == "__main__":  # pragma: no cover
    import json

    def _clean(x):
        if isinstance(x, dict):
            return {k: _clean(v) for k, v in x.items()}
        if isinstance(x, list):
            return [_clean(v) for v in x]
        return round(x, 6) if isinstance(x, float) else x

    out = {"treasuries": treasuries(), "es": equity_futures(), "fx": fx_translation(), "credit": credit(),
           **summary()}
    print(json.dumps(_clean(out), indent=1))
