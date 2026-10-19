"""Case D -- The Hotel PIP Negotiation. Reproducible model.

Run:  python3 cases/hypothetical/case_D_hotel_pip_negotiation/case_d_model.py
All inputs are hypothetical [HYPOTHESIS]. Every number quoted in case_D.md and
case_D_rubric.md is produced here and asserted in tests/test_case_d.py.
The PIP line items and the monthly demand profile are also published as
cases/datasets/case_d_pip_items.csv and cases/datasets/case_d_monthly_demand.csv.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "models" / "python"))

from sdesk import cre, hotel, tvm  # noqa: E402

# ----------------------------------------------------------------- property
ROOMS = 118
DAYS = 365

# Trailing-12 operating parameters (owner's statement, already normalized by the buyer)
T12 = dict(occ=0.735, adr=146.00)
COMP_T12 = dict(occ=0.720, adr=145.00)
RGI_BY_QUARTER = [106, 104, 102, 99]         # trailing four quarters, oldest first
OPEX = dict(other_pct=0.03, cpor=33.0, other_dept_ratio=0.50, undist_fixed=1_180_000,
            undist_pct=0.035, mgmt_pct=0.03, franchise_pct=0.12, tax=205_000, ins=98_000,
            reserve_pct=0.04)

# Owner's position
OWNER_CAP = 0.085
OWNER_ASK = 13_500_000

# ----------------------------------------------------------------- PIP letter (Exhibit D-2)
PIP_ITEMS = [  # (item, basis, amount)
    ("Guestroom soft goods (carpet, drapery, bedding, wallvinyl)", "7,500/key", 7_500 * ROOMS),
    ("Guestroom case goods and seating", "6,000/key", 6_000 * ROOMS),
    ("Bathrooms: tub-to-shower conversions, vanities, lighting", "5,500/key", 5_500 * ROOMS),
    ("PTAC/HVAC replacement", "1,400/key", 1_400 * ROOMS),
    ("Lobby, breakfast area, public restrooms", "lump sum", 420_000),
    ("Exterior: new-standard signage, paint, porte-cochere", "lump sum", 260_000),
    ("Pool and fitness", "lump sum", 95_000),
    ("Technology: Wi-Fi backbone, mobile key", "lump sum", 110_000),
]
SOFT_COST_PCT = 0.08          # design, permits, purchasing agent, project management
CONTINGENCY = 0.12
DEFERRED_CAPEX = [("Roof replacement", 180_000), ("Parking lot mill and overlay", 95_000),
                  ("Elevator modernization", 135_000)]   # PCA items outside the PIP

# ----------------------------------------------------------------- renovation and displacement
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTH_OCC = [0.64, 0.72, 0.80, 0.79, 0.78, 0.76, 0.74, 0.71, 0.76, 0.82, 0.71, 0.59]  # averages 73.5%
WEEKDAY_FACTOR, WEEKEND_FACTOR = 1.15, 0.80   # Mon-Thu vs Fri-Sun demand relative to the month
OOO_ROOMS = 20                                 # rooms out of order while a floor is renovated
RENO_MONTHS = 6
CONSTRUCTION_ADR_DISCOUNT = 0.05               # rate concession on rooms sold during works
VAR_PCT_OF_REVENUE = 0.03 + 0.12 / 1.03 + 0.035  # mgmt + franchise (on rooms) + undistributed %

# ----------------------------------------------------------------- stabilized and alternative paths
COMP_FWD = dict(occ=0.72, adr=150.00)          # comp-set forward year (stabilized)
POST_PIP = dict(rgi=106, occ=0.75)             # renovated, branded
INDEPENDENT = dict(rgi=88, occ=0.68, dist_pct=0.07, extra_sm=150_000, deflag_capex=350_000,
                   refresh_per_key=6_000, cap=0.0975)
STAB_CAP = 0.0875           # renovated, branded, NOI after 4% reserve
ASIS_CAP = 0.0925           # dated, PIP-encumbered comps (for reference only)
REQUIRED_PROFIT = 0.15      # buyer's required profit on PIP capital
CARRY_AND_SOFT = 150_000    # negative carry on held-back loan funds, extra legal, brand fees
BUYER_CLOSING = 0.02
OPENING_YIELD_ON_COST = 0.0950   # opening-bid discipline: stabilized NOI / all-in cost
RENO_HURDLE = 0.10               # required unlevered return on renovation capital

# Liquidated damages if the franchise terminates early (hypothetical contract formula)
LD_MONTHS = 24
LD_FEE_PCT = 0.085          # royalty + marketing share of rooms revenue used in the LD formula

# ----------------------------------------------------------------- lender term sheet
LOAN = dict(rate=0.076, amort=25, ltc=0.65, asis_debt_yield=0.105, stab_dscr=1.35,
            pip_funding_share=0.75)

# Owner's hold-and-renovate alternative
OWNER_DISC = 0.12            # concentrated, single-asset owner
SELLER_LOAN = dict(balance=7_400_000, months_to_maturity=11, refi_cost_pct=0.015)
SELL_COST = 0.03
OWNER_HOLD_RGI = [97, 95]   # years 1-2 before renewal: product keeps aging
RENEWAL_YEAR = 3            # PIP executed in year 3; sale at end of year 3 on year-4 NOI


# =================================================================== functions

def statement(occ: float, adr: float, *, rooms_pct: float | None = None, extra_undist: float = 0.0) -> dict:
    o = OPEX
    return hotel.operating_statement(
        ROOMS, occ, adr, other_revenue_pct_of_rooms=o["other_pct"],
        rooms_expense_per_occupied_room=o["cpor"], other_dept_expense_ratio=o["other_dept_ratio"],
        undistributed_fixed=o["undist_fixed"] + extra_undist, undistributed_pct_of_revenue=o["undist_pct"],
        mgmt_fee_pct=o["mgmt_pct"],
        franchise_fee_pct_of_rooms=o["franchise_pct"] if rooms_pct is None else rooms_pct,
        property_tax=o["tax"], insurance=o["ins"], ffe_reserve_pct=o["reserve_pct"])


def t12() -> dict:
    s = statement(T12["occ"], T12["adr"])
    idx = hotel.indices(T12["occ"], T12["adr"], COMP_T12["occ"], COMP_T12["adr"])
    return {**s, **idx, "owner_value": s["noi"] / OWNER_CAP, "owner_value_9_25": s["noi"] / ASIS_CAP}


def pip_budget() -> dict:
    hard = sum(a for _, _, a in PIP_ITEMS)
    soft = SOFT_COST_PCT * hard
    base = hard + soft
    deferred = sum(a for _, a in DEFERRED_CAPEX)
    return dict(hard=hard, soft=soft, base=base, per_key=base / ROOMS,
                contingency=CONTINGENCY * base, all_in=base * (1 + CONTINGENCY), deferred=deferred,
                hard_per_key=hard / ROOMS)


def displacement(start_month: int) -> dict:
    """Monthly displacement for a RENO_MONTHS-long phased renovation starting at index ``start_month``."""
    s = statement(T12["occ"], T12["adr"])
    contrib_per_rn = T12["adr"] * (1 + OPEX["other_pct"]) * (1 - VAR_PCT_OF_REVENUE) - OPEX["cpor"]
    rows = []
    for j in range(RENO_MONTHS):
        m = (start_month + j) % 12
        days = MONTH_DAYS[m]
        cap = ROOMS - OOO_ROOMS
        d_w = min(ROOMS, MONTH_OCC[m] * WEEKDAY_FACTOR * ROOMS)
        d_e = min(ROOMS, MONTH_OCC[m] * WEEKEND_FACTOR * ROOMS)
        lost = days * (4 / 7 * max(0.0, d_w - cap) + 3 / 7 * max(0.0, d_e - cap))
        sold = days * (4 / 7 * min(d_w, cap) + 3 / 7 * min(d_e, cap))
        lost_contrib = lost * contrib_per_rn
        concession = sold * T12["adr"] * CONSTRUCTION_ADR_DISCOUNT * (1 - VAR_PCT_OF_REVENUE)
        rows.append(dict(month=MONTHS[m], days=days, demand_rn=MONTH_OCC[m] * ROOMS * days,
                         lost_rn=lost, sold_rn=sold, lost_rooms_rev=lost * T12["adr"],
                         lost_noi=lost_contrib + concession, lost_contrib=lost_contrib,
                         concession=concession))
    tot = sum(r["lost_noi"] for r in rows)
    return dict(rows=rows, total=tot, lost_rn=sum(r["lost_rn"] for r in rows),
                contrib_per_rn=contrib_per_rn, t12_noi=s["noi"])


def stabilized() -> dict:
    revpar = POST_PIP["rgi"] / 100 * COMP_FWD["occ"] * COMP_FWD["adr"]
    adr = revpar / POST_PIP["occ"]
    s = statement(POST_PIP["occ"], adr)
    return {**s, "adr": adr, "value": s["noi"] / STAB_CAP}


def independent() -> dict:
    i = INDEPENDENT
    revpar = i["rgi"] / 100 * COMP_FWD["occ"] * COMP_FWD["adr"]
    adr = revpar / i["occ"]
    s = statement(i["occ"], adr, rooms_pct=i["dist_pct"], extra_undist=i["extra_sm"])
    capex = i["deflag_capex"] + i["refresh_per_key"] * ROOMS
    value = s["noi"] / i["cap"]
    return {**s, "adr": adr, "capex": capex, "value": value,
            "net_value": value - capex - pip_budget()["deferred"]}


def liquidated_damages() -> float:
    rooms_rev = statement(T12["occ"], T12["adr"])["rooms_revenue"]
    return LD_FEE_PCT * rooms_rev / 12 * LD_MONTHS


def return_on_renovation() -> dict:
    """RevPAR lift over the T-12 needed for the PIP to earn the target on its all-in cost."""
    b = pip_budget()
    st = stabilized()
    base = t12()
    # flow-through of a rate-led RevPAR gain (computed from the P&L, not assumed)
    up = statement(T12["occ"], T12["adr"] * 1.01)
    ft_noi = (up["noi"] - base["noi"]) / (up["rooms_revenue"] - base["rooms_revenue"])
    target_noi_gain = RENO_HURDLE * b["all_in"]
    d_revpar_needed = target_noi_gain / (ft_noi * ROOMS * DAYS)
    ind = independent()
    incr_capital = b["all_in"] - ind["capex"]
    incr_noi = st["noi"] - ind["noi"]
    return dict(ft_noi=ft_noi, target_noi_gain=target_noi_gain, d_revpar_needed=d_revpar_needed,
                revpar_needed=base["revpar"] + d_revpar_needed,
                pct_lift_needed=d_revpar_needed / base["revpar"],
                projected_lift=st["revpar"] - base["revpar"], projected_noi_gain=st["noi"] - base["noi"],
                yield_vs_t12=(st["noi"] - base["noi"]) / b["all_in"],
                incr_capital_vs_independent=incr_capital, incr_noi_vs_independent=incr_noi,
                yield_vs_independent=incr_noi / incr_capital)


def price() -> dict:
    b = pip_budget()
    st = stabilized()
    disp = displacement(10)   # recommended start: November (index 10)
    pa = hotel.pip_adjusted_price(st["value"], b["base"], disp["total"], CARRY_AND_SOFT + b["deferred"],
                                  CONTINGENCY, REQUIRED_PROFIT)
    owner = t12()
    return {**pa, "stabilized_value": st["value"], "displacement": disp["total"],
            "carry_soft_deferred": CARRY_AND_SOFT + b["deferred"],
            "gap_to_ask": OWNER_ASK - pa["price"], "price_per_key": pa["price"] / ROOMS,
            "implied_cap_t12": owner["noi"] / pa["price"]}


def yield_on_cost(purchase_price: float) -> dict:
    b = pip_budget()
    st = stabilized()
    other = b["all_in"] + displacement(10)["total"] + CARRY_AND_SOFT + b["deferred"]
    all_in = purchase_price * (1 + BUYER_CLOSING) + other
    return dict(all_in=all_in, yoc=st["noi"] / all_in, spread_bp=1e4 * (st["noi"] / all_in - STAB_CAP))


def opening_bid() -> dict:
    """Price at which stabilized NOI / all-in cost equals the opening yield-on-cost target."""
    b = pip_budget()
    st = stabilized()
    other = b["all_in"] + displacement(10)["total"] + CARRY_AND_SOFT + b["deferred"]
    p = (st["noi"] / OPENING_YIELD_ON_COST - other) / (1 + BUYER_CLOSING)
    return dict(price=p, per_key=p / ROOMS, **yield_on_cost(p))


def walk_away_price() -> dict:
    """Walk-away = the PIP-adjusted price (15% required profit, 12% contingency)."""
    p = price()["price"]
    return dict(price=p, per_key=p / ROOMS, **yield_on_cost(p))


def financing(purchase_price: float) -> dict:
    """Two lender structures: (1) PIP holdback funded at close; (2) future funding, equity first."""
    b = pip_budget()
    base = t12()
    st = stabilized()
    total_cost = purchase_price * (1 + BUYER_CLOSING) + b["all_in"] + b["deferred"]
    k = tvm.loan_constant(LOAN["rate"], LOAN["amort"])
    ltc_loan = LOAN["ltc"] * total_cost
    dy_loan = base["noi"] / LOAN["asis_debt_yield"]
    dscr_loan = st["noi"] / LOAN["stab_dscr"] / k
    loan = min(ltc_loan, dy_loan, dscr_loan)
    binding = {ltc_loan: "LTC", dy_loan: "as-is debt yield", dscr_loan: "stabilized DSCR"}[loan]
    # Structure 1: whole loan funded at close; PIP share sits in a lender-controlled reserve
    pip_loan = min(LOAN["pip_funding_share"] * b["all_in"], loan)
    s1_equity_close = total_cost - loan
    s1_reserve_carry = pip_loan * LOAN["rate"] * (RENO_MONTHS / 2 + 1) / 12   # avg balance idle ~4 months
    # Structure 2: initial advance excludes the PIP; future advances fund 75% of PIP after equity spends 25%
    initial = loan - pip_loan
    s2_equity_close = purchase_price * (1 + BUYER_CLOSING) + b["deferred"] - initial
    s2_equity_pip = b["all_in"] - pip_loan
    return dict(total_cost=total_cost, ltc_loan=ltc_loan, dy_loan=dy_loan, dscr_loan=dscr_loan,
                loan=loan, binding=binding, k=k, pip_loan=pip_loan, s1_equity_close=s1_equity_close,
                s1_reserve_carry=s1_reserve_carry, s2_initial=initial, s2_equity_close=s2_equity_close,
                s2_equity_pip=s2_equity_pip, s2_equity_total=s2_equity_close + s2_equity_pip,
                ltv_stab=loan / st["value"], dscr_asis=base["noi"] / (loan * k),
                dscr_stab=st["noi"] / (loan * k))


def held_occupancies() -> list[float]:
    """Unrenovated years: RGI erodes to OWNER_HOLD_RGI with ADR held at the T-12 level, so the
    erosion shows up as occupancy (occ scales with RGI / T-12 RGI)."""
    rgi0 = t12()["rgi"]
    return [T12["occ"] * rgi / rgi0 for rgi in OWNER_HOLD_RGI]


def seller_refi() -> dict:
    """Can the owner refinance around the PIP? Lender sizes on T-12 and requires a funded PIP reserve."""
    base = t12()
    b = pip_budget()
    k = tvm.loan_constant(LOAN["rate"], LOAN["amort"])
    dy_loan = base["noi"] / LOAN["asis_debt_yield"]
    dscr_loan = base["noi"] / LOAN["stab_dscr"] / k
    loan = min(dy_loan, dscr_loan)
    costs = SELLER_LOAN["refi_cost_pct"] * loan
    cash_out = loan - SELLER_LOAN["balance"] - costs
    shortfall = b["all_in"] - cash_out
    return dict(dy_loan=dy_loan, dscr_loan=dscr_loan, loan=loan, costs=costs, cash_out=cash_out,
                pip_reserve=b["all_in"], owner_check=shortfall)


def seller_net(purchase_price: float) -> float:
    return purchase_price * (1 - SELL_COST) - SELLER_LOAN["balance"]


def owner_deflag() -> dict:
    """Owner ignores the PIP: keeps the flag to expiry (years 1-2), operates independent from year 3,
    sells at end of year 3 on independent year-4 NOI."""
    flows = []
    for occ in held_occupancies():
        flows.append(statement(occ, T12["adr"])["noi"])
    ind = independent()
    sale = ind["noi"] * 1.03 / INDEPENDENT["cap"] * (1 - SELL_COST)
    y3 = ind["noi"] - ind["capex"] - pip_budget()["deferred"]
    flows.append(y3 + sale)
    pv = sum(f / (1 + OWNER_DISC) ** (t + 1) for t, f in enumerate(flows))
    return dict(flows=flows, sale=sale, y3=y3, pv=pv)


def owner_hold() -> dict:
    """Owner keeps the hotel, renovates at renewal (year 3) at cost without buyer profit, sells end of year 3."""
    b = pip_budget()
    flows = []
    nois = []
    for occ in held_occupancies():
        s = statement(occ, T12["adr"])
        nois.append(s["noi"])
        flows.append(s["noi"])
    st = stabilized()
    disp = displacement(10)["total"]
    y3 = st["noi"] - disp - b["all_in"] - b["deferred"]
    sale = st["noi"] * 1.03 / STAB_CAP * (1 - SELL_COST)
    flows.append(y3 + sale)
    pv = sum(f / (1 + OWNER_DISC) ** (t + 1) for t, f in enumerate(flows))
    return dict(nois=nois, y3=y3, sale=sale, flows=flows, pv=pv,
                gross_sale_now_at_walkaway=price()["price"] * (1 - SELL_COST))


def deflag_owner() -> dict:
    """What the owner's 'ignore the PIP' stance implies: brand lost at expiry, independent thereafter."""
    ind = independent()
    return dict(value=ind["value"], capex=ind["capex"], net=ind["net_value"], noi=ind["noi"],
                ld=liquidated_damages())


def owner_indifference() -> dict:
    """Probability the owner must assign to funding and executing the PIP himself for holding to beat
    selling at the buyer's walk-away price (all values are PVs to the owner, before loan payoff)."""
    hold = owner_hold()["pv"]
    deflag = owner_deflag()["pv"]
    sell = price()["price"] * (1 - SELL_COST)
    # p* solves p*hold + (1-p*)*deflag = sell
    p_star = (sell - deflag) / (hold - deflag)
    return dict(hold=hold, deflag=deflag, sell=sell, p_star=p_star,
                hold_gross_equivalent=hold / (1 - SELL_COST))


def sensitivities() -> dict:
    """Mode D sensitivities of the walk-away (PIP-adjusted) price."""
    b = pip_budget()
    st = stabilized()
    disp = displacement(10)["total"]
    carry = CARRY_AND_SOFT + b["deferred"]

    def px(v_stab, pip_base):
        return hotel.pip_adjusted_price(v_stab, pip_base, disp, carry, CONTINGENCY, REQUIRED_PROFIT)["price"]
    base = px(st["value"], b["base"])
    exit_up = px(st["noi"] / (STAB_CAP + 0.005), b["base"])
    pip_up = px(st["value"], b["base"] * 1.20)
    revpar = 1.02 * COMP_FWD["occ"] * COMP_FWD["adr"]          # post-PIP RGI 102 instead of 106
    weak = statement(POST_PIP["occ"], revpar / POST_PIP["occ"])
    rgi_low = px(weak["noi"] / STAB_CAP, b["base"])
    return dict(base=base, exit_cap_plus_50bp=exit_up, d_exit=exit_up - base, pip_plus_20=pip_up,
                d_pip=pip_up - base, rgi_102_noi=weak["noi"], rgi_102=rgi_low, d_rgi=rgi_low - base,
                schedule_saving=displacement(2)["total"] - disp,
                ask_cap_t12=t12()["noi"] / OWNER_ASK,
                stab_value_per_key=st["value"] / ROOMS)


def report() -> str:
    lines = []
    t = t12()
    lines.append(f"T-12: RevPAR {t['revpar']:.2f}  TR {t['total_revenue']:,.0f}  GOP {t['gop']:,.0f} "
                 f"({t['gop_margin']:.1%})  EBITDA {t['ebitda']:,.0f}  NOI {t['noi']:,.0f}  "
                 f"MPI {t['mpi']:.1f} ARI {t['ari']:.1f} RGI {t['rgi']:.1f}  owner value {t['owner_value']:,.0f}")
    b = pip_budget()
    lines.append("PIP: " + ", ".join(f"{k} {v:,.0f}" for k, v in b.items()))
    for sm in (10, 2):
        d = displacement(sm)
        lines.append(f"Displacement start {MONTHS[sm]}: lost RN {d['lost_rn']:,.0f}  lost NOI {d['total']:,.0f}  "
                     f"contrib/RN {d['contrib_per_rn']:.2f}")
        for r in d["rows"]:
            lines.append("   " + ", ".join(f"{k} {v:,.0f}" if isinstance(v, float) else f"{k} {v}" for k, v in r.items()))
    st = stabilized()
    lines.append(f"Stabilized: ADR {st['adr']:.2f} RevPAR {st['revpar']:.2f} NOI {st['noi']:,.0f} value {st['value']:,.0f}")
    ind = independent()
    lines.append(f"Independent: ADR {ind['adr']:.2f} RevPAR {ind['revpar']:.2f} NOI {ind['noi']:,.0f} "
                 f"value {ind['value']:,.0f} capex {ind['capex']:,.0f} net {ind['net_value']:,.0f}")
    lines.append(f"LD: {liquidated_damages():,.0f}")
    lines.append("Return on renovation: " + ", ".join(f"{k} {v:,.4f}" for k, v in return_on_renovation().items()))
    p = price()
    lines.append("Price: " + ", ".join(f"{k} {v:,.4f}" for k, v in p.items()))
    w = walk_away_price()
    lines.append("Walk-away: " + ", ".join(f"{k} {v:,.4f}" for k, v in w.items()))
    ob = opening_bid()
    lines.append("Opening: " + ", ".join(f"{k} {v:,.4f}" for k, v in ob.items()))
    lines.append("Ask YOC: " + ", ".join(f"{k} {v:,.4f}" for k, v in yield_on_cost(OWNER_ASK).items()))
    lines.append("Seller refi: " + ", ".join(f"{k} {v:,.0f}" for k, v in seller_refi().items()))
    lines.append(f"Seller net at walk-away {seller_net(w['price']):,.0f}; at opening {seller_net(ob['price']):,.0f}")
    lines.append("Owner deflag: " + str(owner_deflag()))
    lines.append("Owner indifference: " + str(owner_indifference()))
    lines.append("Sensitivities: " + ", ".join(f"{k} {v:,.4f}" for k, v in sensitivities().items()))
    for px in (p["price"], 11_000_000):
        f = financing(px)
        lines.append(f"Financing at {px:,.0f}: " + ", ".join(
            f"{k} {v:,.4f}" if isinstance(v, float) else f"{k} {v}" for k, v in f.items()))
    o = owner_hold()
    lines.append("Owner hold: " + ", ".join(f"{k} {v}" for k, v in o.items()))
    return "\n".join(lines)


if __name__ == "__main__":
    print(report())
