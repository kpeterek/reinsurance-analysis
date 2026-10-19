"""Case E — The Distressed Office Acquisition. Reproducible model.

Run:  python3 cases/hypothetical/case_E_distressed_office/case_e_model.py
All inputs are hypothetical [HYPOTHESIS]. Every number quoted in case_E.md and
case_E_rubric.md is produced here and asserted in tests/test_case_e.py.

Conventions: annual periods, cash flows at year-end, unlevered unless stated.
Rents are GROSS (tenant pays a full-service rent; landlord pays operating
expenses and property tax). "sf" means rentable square feet (RSF) unless GBA.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "models" / "python"))

from sdesk import cre, tvm  # noqa: E402
from sdesk import x_cre_distress as xd  # noqa: E402

# ----------------------------------------------------------------- building
RSF = 520_000
GBA = 560_000
LEASED_SF = 197_600                    # 38% leased at purchase
IN_PLACE_RENT = 33.00                  # $/sf/yr gross, flat to expiry
ROLLOVER = [40_000, 52_000, 45_600, 30_000, 30_000, 0, 0]  # in-place sf expiring, years 1-7
RENEWAL_PROB = 0.55                    # share of expiring sf that renews

# ----------------------------------------------------------------- price and costs
ASK = 52_000_000                       # lender-REO whisper price ($100/RSF)
REPLACEMENT_COST_PSF = 480.0           # $/RSF, hypothetical
CLOSING_PCT = 0.015
TAX_ON_PRICE = 0.020                   # property tax reassessed at 2.0% of price per year
FIXED_OPEX_PSF = 6.50                  # $/RSF/yr on the whole building, excl. property tax
VARIABLE_OPEX_PSF = 4.00               # $/occupied sf/yr (janitorial, utilities share)
RESERVE_PSF = 0.30                     # $/RSF/yr replacement reserve
CAPEX_PSF = 25.0                       # base-building program ($/RSF): elevators, HVAC, lobby
CAPEX_TIMING = [0.60, 0.40]            # share spent in years 1 and 2

# Leasing economics
TI_NEW, TI_RENEW = 65.0, 25.0          # $/sf
LC_NEW, LC_RENEW = 0.06 * 7, 0.03 * 5  # commission x term => multiple of first-year rent
FREE_NEW, FREE_RENEW = 7 / 12, 2 / 12  # years of free rent at signing

SALE_COST = 0.02
HOLD = 7

SCENARIOS = {
    # name: probability, year-end occupancy Y1..Y7, market-rent growth Y1..Y8,
    #       exit cap, exit liquidity discount, market rent in year 1
    "Recovery": dict(p=0.40, occ=[0.42, 0.53, 0.64, 0.74, 0.82, 0.86, 0.88],
                     growth=[0.0] + [0.03] * 7, exit_cap=0.0825, liq=0.0, rent1=34.0),
    "Grind": dict(p=0.35, occ=[0.38, 0.43, 0.50, 0.57, 0.63, 0.68, 0.70],
                  growth=[0.0] * 8, exit_cap=0.095, liq=0.0, rent1=34.0),
    "Structural": dict(p=0.25, occ=[0.34, 0.33, 0.35, 0.38, 0.41, 0.44, 0.46],
                       growth=[0.0, -0.03, -0.02] + [0.0] * 5, exit_cap=0.110, liq=0.10, rent1=34.0),
}

# Bridge loan (levered view)
LOAN_LTV_ON_PRICE = 0.55
LOAN_RATE = 0.0825                     # all-in floating, assumed constant, interest-only
LOAN_TERM = 3
EXTENSION_DEBT_YIELD = 0.09            # to extend, T-12 NOI / balance must be >= 9%

# Residential conversion (alternative use)
CONVERTIBLE_SHARE = 0.70               # share of GBA that can become apartments (deep floor plates)
RESI_EFFICIENCY = 0.80                 # net rentable / gross converted
AVG_UNIT_SF = 780
RESI_RENT_PSF_MONTH = 2.45
RESI_VACANCY = 0.07
RESI_OPEX_RATIO = 0.38                 # of effective gross income, incl. tax
RESI_CAP = 0.060
CONV_HARD_PSF_GBA = 240.0
CONV_SOFT_PCT = 0.18                   # of hard
CONV_FINANCING = 12_000_000
CONV_MARGIN = 0.15                     # developer margin on total cost

TARGET_UNLEVERED = 0.12


def market_rents(s: dict, years: int = HOLD + 1) -> list[float]:
    r, out = s["rent1"], []
    for t in range(years):
        if t > 0:
            r *= 1 + s["growth"][t]
        out.append(r)
    return out


def scenario_cash_flows(name: str, price: float = ASK, with_irr: bool = True) -> dict:
    """Annual unlevered cash flows for one scenario.

    Leasing in year t: renewals = RENEWAL_PROB * rollover_t; new leasing =
    (occ_t - occ_{t-1}) * RSF + (1 - RENEWAL_PROB) * rollover_t (space vacated by
    non-renewing tenants must be re-leased to hold occupancy). New and renewal
    leases are signed at that year's market rent. Revenue uses average occupied
    sf: the original in-place leases pay IN_PLACE_RENT until they roll; all other
    occupied space pays the current year's market rent (a simplification that marks
    post-acquisition leases to market each year). Free rent and leasing costs are
    charged in the signing year.
    """
    s = SCENARIOS[name]
    mr = market_rents(s)
    occ = [LEASED_SF / RSF] + s["occ"] + [s["occ"][-1]]   # year 8 held flat for exit NOI
    roll = ROLLOVER + [0]
    in_place = float(LEASED_SF)
    rows, flows = [], [-(price * (1 + CLOSING_PCT))]
    noi_by_year = []
    for t in range(1, HOLD + 2):
        mkt = mr[t - 1]
        renew = RENEWAL_PROB * roll[t - 1]
        new = (occ[t] - occ[t - 1]) * RSF + (1 - RENEWAL_PROB) * roll[t - 1]
        if new < -1e-6:
            # net move-outs exceed non-renewals: treat as additional non-renewal (no new leasing)
            new = 0.0
        occ_begin, occ_end = occ[t - 1] * RSF, occ[t] * RSF
        avg_occ = 0.5 * (occ_begin + occ_end)
        # revenue: in-place at contract rent (average of begin/end balance), rest at market
        in_place_end = in_place - roll[t - 1]
        in_place_avg = 0.5 * (in_place + in_place_end)
        other_avg = max(0.0, avg_occ - in_place_avg)
        revenue = in_place_avg * IN_PLACE_RENT + other_avg * mkt
        free = new * mkt * FREE_NEW + renew * mkt * FREE_RENEW
        opex = FIXED_OPEX_PSF * RSF + VARIABLE_OPEX_PSF * avg_occ + TAX_ON_PRICE * price
        reserve = RESERVE_PSF * RSF
        noi = revenue - free - opex - reserve
        ti = new * TI_NEW + renew * TI_RENEW
        lc = new * mkt * LC_NEW + renew * mkt * LC_RENEW
        capex = CAPEX_PSF * RSF * (CAPEX_TIMING[t - 1] if t - 1 < len(CAPEX_TIMING) else 0.0)
        cf = noi - ti - lc - capex
        in_place = in_place_end
        noi_by_year.append(noi)
        rows.append({"year": t, "market_rent": mkt, "occ_end": occ[t], "avg_occupied_sf": avg_occ,
                     "renewal_sf": renew, "new_sf": new, "revenue": revenue, "free_rent": free,
                     "opex": opex, "reserve": reserve, "noi": noi, "ti": ti, "lc": lc,
                     "capex": capex, "cash_flow": cf})
        if t <= HOLD:
            flows.append(cf)
    # Exit at end of year 7 on year-8 NOI (stabilized: no free rent in year 8 NOI for valuation)
    y8 = rows[HOLD]
    exit_noi = y8["noi"] + y8["free_rent"]
    gross_exit = exit_noi / s["exit_cap"] * (1 - s["liq"])
    net_exit = gross_exit * (1 - SALE_COST)
    flows[-1] += net_exit
    return {"rows": rows[:HOLD], "year8": y8, "exit_noi": exit_noi, "gross_exit": gross_exit,
            "net_exit": net_exit, "flows": flows, "irr": tvm.irr(flows) if with_irr else None,
            "profit": sum(flows), "multiple": tvm.equity_multiple(flows), "noi": noi_by_year}


def portfolio(price: float = ASK) -> dict:
    names = list(SCENARIOS)
    res = {n: scenario_cash_flows(n, price) for n in names}
    probs = [SCENARIOS[n]["p"] for n in names]
    summ = xd.scenario_irrs([res[n]["flows"] for n in names], probs)
    sd = cre.scenario_summary(summ["profits"], probs)
    return {"by_scenario": res, **summ, "sd_profit": sd["sd"], "p_loss": sd["p_loss"]}


def max_price(target: float = TARGET_UNLEVERED) -> float:
    """Price at which the NPV of probability-weighted flows at ``target`` is zero.

    Price affects flows through closing costs and reassessed property tax, so we
    solve by bisection rather than discounting once.
    """
    def f(p):
        fl = [scenario_cash_flows(n, p, with_irr=False)["flows"] for n in SCENARIOS]
        exp = [sum(SCENARIOS[n]["p"] * f[t] for n, f in zip(SCENARIOS, fl)) for t in range(HOLD + 1)]
        return tvm.npv(target, exp)
    lo, hi = 1_000_000.0, 200_000_000.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def bridge_loan_test(price: float = ASK) -> dict:
    """Year-3 maturity: can the bridge loan be extended at a 9% debt yield on year-3 NOI?"""
    loan = LOAN_LTV_ON_PRICE * price
    out = {"loan": loan, "annual_interest": loan * LOAN_RATE}
    for n in SCENARIOS:
        noi3 = scenario_cash_flows(n, price)["noi"][2]
        supportable = max(0.0, noi3 / EXTENSION_DEBT_YIELD)
        out[n] = {"noi3": noi3, "supportable": supportable, "paydown": max(0.0, loan - supportable)}
    return out


def carry_through_year3(name: str, price: float = ASK) -> dict:
    """Cumulative unlevered cash burn (negative flows) and with bridge interest, years 1-3."""
    flows = scenario_cash_flows(name, price)["flows"][1:4]
    interest = LOAN_LTV_ON_PRICE * price * LOAN_RATE
    return {"unlevered": sum(flows), "levered": sum(flows) - 3 * interest}


def conversion_feasibility(rent_psf_month: float = RESI_RENT_PSF_MONTH,
                           hard_psf: float = CONV_HARD_PSF_GBA) -> dict:
    nrsf = GBA * CONVERTIBLE_SHARE * RESI_EFFICIENCY
    units = nrsf / AVG_UNIT_SF
    gpr = nrsf * rent_psf_month * 12
    egi = gpr * (1 - RESI_VACANCY)
    noi = egi * (1 - RESI_OPEX_RATIO)
    gdv = noi / RESI_CAP
    hard = hard_psf * GBA
    soft = CONV_SOFT_PCT * hard
    rl = cre.residual_land_value(gdv, hard, soft, CONV_FINANCING, CONV_MARGIN, SALE_COST)
    return {"nrsf": nrsf, "units": units, "gpr": gpr, "egi": egi, "noi": noi, "gdv": gdv,
            "hard": hard, "soft": soft, **rl}


def conversion_breakeven_rent(land_price: float = ASK) -> float:
    """Residential rent ($/sf/month) at which the residual land value equals ``land_price``."""
    lo, hi = 0.5, 10.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if conversion_feasibility(mid)["land_value"] < land_price:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def replacement_cost_rent() -> float:
    """Gross rent a new tower needs to earn 7.0% on replacement cost at 90% occupancy.

    Uses this building's opex structure with tax at 2.0% of cost, and a $4.00/RSF
    leasing-capital reserve. This is the rent that would justify new construction.
    """
    cost = REPLACEMENT_COST_PSF * RSF
    opex = FIXED_OPEX_PSF * RSF + VARIABLE_OPEX_PSF * 0.90 * RSF + TAX_ON_PRICE * cost + RESERVE_PSF * RSF
    return xd.required_gross_rent(cost, 0.07, opex, RSF, 0.90, 4.00 * RSF)


def report() -> str:
    pf = portfolio()
    lines = [f"Ask {ASK:,.0f} = ${ASK / RSF:,.2f}/RSF; replacement cost {REPLACEMENT_COST_PSF * RSF:,.0f}"]
    for n, r in pf["by_scenario"].items():
        lines.append(f"\n{n}: IRR {r['irr']:.2%} profit {r['profit']:,.0f} multiple {r['multiple']:.2f}x "
                     f"exit NOI {r['exit_noi']:,.0f} gross exit {r['gross_exit']:,.0f} net {r['net_exit']:,.0f}")
        for row in r["rows"]:
            lines.append("  Y{year} rent {market_rent:6.2f} occ {occ_end:.0%} new {new_sf:8,.0f} ren {renewal_sf:7,.0f} "
                         "rev {revenue:11,.0f} free {free_rent:10,.0f} opex {opex:10,.0f} NOI {noi:11,.0f} "
                         "TI {ti:10,.0f} LC {lc:9,.0f} capex {capex:10,.0f} CF {cash_flow:11,.0f}".format(**row))
    lines.append(f"\nMean IRR {pf['mean_irr']:.2%}  IRR of expected flows {pf['irr_of_expected']:.2%}  "
                 f"E[profit] {pf['expected_profit']:,.0f}  sd {pf['sd_profit']:,.0f}  P(loss) {pf['p_loss']:.0%}")
    mp = max_price()
    lines.append(f"Max price for {TARGET_UNLEVERED:.0%} on expected flows: {mp:,.0f} (${mp / RSF:,.2f}/RSF)")
    b = bridge_loan_test()
    lines.append(f"Bridge loan {b['loan']:,.0f}, interest {b['annual_interest']:,.0f}/yr")
    for n in SCENARIOS:
        lines.append(f"  {n}: NOI3 {b[n]['noi3']:,.0f} supportable {b[n]['supportable']:,.0f} paydown {b[n]['paydown']:,.0f}"
                     f"  burn Y1-3 unlev {carry_through_year3(n)['unlevered']:,.0f} lev {carry_through_year3(n)['levered']:,.0f}")
    c = conversion_feasibility()
    lines.append("Conversion: NRSF {nrsf:,.0f} units {units:,.0f} NOI {noi:,.0f} GDV {gdv:,.0f} hard {hard:,.0f} "
                 "soft {soft:,.0f} residual land {land_value:,.0f}".format(**c))
    lines.append(f"Conversion break-even rent at ask: ${conversion_breakeven_rent():.2f}/sf/month")
    lines.append(f"Rent needed to justify new construction: ${replacement_cost_rent():.2f}/sf")
    return "\n".join(lines)


if __name__ == "__main__":
    print(report())


# ----------------------------------------------------------------- sensitivities
def with_probs(probs: dict, fn, *args, **kwargs):
    """Evaluate ``fn`` with scenario probabilities temporarily replaced."""
    old = {n: SCENARIOS[n]["p"] for n in SCENARIOS}
    try:
        for n, p in probs.items():
            SCENARIOS[n]["p"] = p
        return fn(*args, **kwargs)
    finally:
        for n, p in old.items():
            SCENARIOS[n]["p"] = p


def with_globals(overrides: dict, fn, *args, **kwargs):
    """Evaluate ``fn`` with module-level inputs (e.g. TI_NEW) temporarily replaced."""
    g = globals()
    old = {k: g[k] for k in overrides}
    try:
        g.update(overrides)
        return fn(*args, **kwargs)
    finally:
        g.update(old)


def with_exit_cap_shift(shift: float, fn, *args, **kwargs):
    old = {n: SCENARIOS[n]["exit_cap"] for n in SCENARIOS}
    try:
        for n in SCENARIOS:
            SCENARIOS[n]["exit_cap"] = old[n] + shift
        return fn(*args, **kwargs)
    finally:
        for n, c in old.items():
            SCENARIOS[n]["exit_cap"] = c


def structural_breakeven_probability(price: float = ASK, target: float = TARGET_UNLEVERED) -> float:
    """Probability of the Structural scenario at which expected NPV at ``target`` is zero,
    holding the Recovery:Grind ratio fixed (Chapter 1 multi-scenario break-even)."""
    rm = {n: tvm.npv(target, scenario_cash_flows(n, price, with_irr=False)["flows"]) for n in SCENARIOS}
    pr, pg = SCENARIOS["Recovery"]["p"], SCENARIOS["Grind"]["p"]
    gbar = (pr * rm["Recovery"] + pg * rm["Grind"]) / (pr + pg)
    loss = -rm["Structural"]
    if gbar <= 0:
        return 0.0
    return gbar / (gbar + loss)


def npv_by_scenario(price: float = ASK, target: float = TARGET_UNLEVERED) -> dict:
    return {n: tvm.npv(target, scenario_cash_flows(n, price, with_irr=False)["flows"]) for n in SCENARIOS}
