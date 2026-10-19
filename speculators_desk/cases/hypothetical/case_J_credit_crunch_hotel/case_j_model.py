"""Case J -- The Credit Crunch Hotel Acquisition. Reproducible model.

Run:  python3 cases/hypothetical/case_J_credit_crunch_hotel/case_j_model.py
All inputs are hypothetical [HYPOTHESIS]. Every number quoted in case_J.md and
case_J_rubric.md is produced here and asserted in tests/test_case_j.py.

Conventions (book style guide): NOI is after a 4% FF&E reserve. ``N`` denotes
NOI after reserve but BEFORE property tax. Property tax is reassessed on sale at
t = tax rate x assessment ratio of price, so tax = t x P (loaded cap, Case A).
Annual property flows at year-end. Mortgages pay monthly at r/12; annual debt
service = 12 x monthly payment; balances use the closed form in sdesk.tvm.
Reversion at end of year H = forward NOI (year H+1, before tax) capitalized at
the loaded exit cap (c_T + t), less selling costs.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "models" / "python"))

from sdesk import cre, hotel, tvm  # noqa: E402

# ----------------------------------------------------------------- property
ROOMS = 150
DAYS = 365
ROOMS_SOLD = 40_790
ADR = 154.00

T12 = {  # current trailing twelve months (crunch period)
    "rooms_revenue": 6_281_660,       # 40,790 x $154.00
    "other_revenue": 520_000,         # F&B (breakfast/bar/market), parking, meeting, other
    "rooms_expense": 1_630_000,
    "other_dept_expense": 330_000,
    "undistributed": 1_610_000,       # A&G, S&M, POM, utilities, IT
    "insurance": 175_000,
}
MGMT_FEE_PCT = 0.03          # of total revenue
FRANCHISE_PCT = 0.11         # of rooms revenue (royalty, program, loyalty, reservations)
RESERVE_PCT = 0.04           # of total revenue
TAX_RATE = 0.021
ASSESSMENT_RATIO = 0.80
T_TAX = TAX_RATE * ASSESSMENT_RATIO   # 1.68% of price

N_PRE_CRUNCH = 1_935_000     # NOI before property tax, T-12 as of 18 months ago (normal credit)

# ----------------------------------------------------------------- market (STR-style, hypothetical)
STR = [  # period, subject occ, subject ADR, comp-set occ, comp-set ADR
    ("T-12 ending 36 months ago", 0.735, 146.00, 0.690, 141.00),
    ("T-12 ending 18 months ago", 0.752, 152.00, 0.695, 147.00),
    ("T-12 current", 0.745, 154.00, 0.680, 148.00),
]
COMP_SET_ROOMS = 940                 # six hotels, excluding subject
UNDER_CONSTRUCTION_ROOMS = 96        # financed before the crunch; opens in ~15 months
PLANNED_UNFINANCED_ROOMS = 120       # one entitled project; no construction loan available
DEMAND_GROWTH = 0.025                # annual room-night demand growth, base
ABSORPTION_YEARS = 2
ROOMS_FLOW_THROUGH = 0.60            # NOI flow-through on lost rooms revenue

# ----------------------------------------------------------------- valuation / hold conventions
G = 0.03                     # NOI (before tax) and tax growth, per year
HOLD = 5
EXIT_CAP_NORMAL = 0.085      # on forward NOI after reassessed tax, loaded with T_TAX
EXIT_CAP_CRUNCH = 0.0975
SELL_COST = 0.02
CLOSE_COST = 0.015
AMORT = 25

# ----------------------------------------------------------------- financing regimes and buyer universe
REGIMES = ("normal", "crunch")

BUYERS = {
    "Owner-operator": dict(
        metric="coc", target=0.09, max_equity=12_000_000,
        normal=dict(ltv=0.65, rate=0.0650, dscr=1.35, dy=0.10),
        crunch=dict(ltv=0.45, rate=0.0825, dscr=1.50, dy=0.13),
        active={"normal": True, "crunch": True}),
    "Opportunity fund": dict(
        metric="irr", target=0.16, max_equity=None,
        normal=dict(ltv=0.70, rate=0.0700, dscr=1.25, dy=0.09),
        crunch=dict(ltv=0.50, rate=0.0975, dscr=1.40, dy=0.12),
        active={"normal": True, "crunch": True}),
    "Lodging REIT": dict(
        metric="irr", target=0.09, max_equity=None,
        normal=None, crunch=None,
        active={"normal": True, "crunch": False}),   # equity trades below NAV; no acquisitions
    "Family-office cash buyer": dict(
        metric="irr", target=0.105, max_equity=15_000_000,
        normal=None, crunch=None,
        active={"normal": True, "crunch": True}),
}

# ----------------------------------------------------------------- client: all-cash with planned refinance
CLIENT_TARGET_IRR = 0.13
CLIENT_PRICE = 16_550_000
REFI_TERMS = dict(ltv=0.65, rate=0.0650, dscr=1.35, dy=0.10)     # normal-credit terms when credit returns
REFI_APPRAISAL_CAP = 0.0825       # applied to forward NOI after (unreassessed) tax at refi
REFI_COST_PCT = 0.01
UC_SHOCK = "uc"                   # sentinel: NOI shock equal to the under-construction supply hit
IMPAIRMENT_SHOCK = -0.15
SCENARIOS = {  # name: (probability, refi year or None, NOI shock from year 2, exit regime)
    "Credit returns in 1 year": (0.30, 1, UC_SHOCK, "normal"),
    "Credit returns in 2 years": (0.30, 2, UC_SHOCK, "normal"),
    "Credit returns in 4 years": (0.15, 4, UC_SHOCK, "normal"),
    "Credit shut through exit": (0.10, None, UC_SHOCK, "crunch"),
    "Impairment": (0.15, None, IMPAIRMENT_SHOCK, "crunch"),
}

# Certainty of close: the seller compares a financed bid with an all-cash bid
FINANCED_CLOSE_PROB = 0.65        # owner-operator's bank commitment survives credit committee and appraisal
REMARKET_MONTHS = 6               # if the financed deal fails, re-marketing delay before the fallback bid closes
SELLER_DELAY_RATE = 0.08          # seller's annual discount rate for delay

# ----------------------------------------------------------------- seller-side alternatives
SELLER_NOTE_SHARE = 0.20          # of price, second lien behind a crunch-terms bank loan
SELLER_NOTE_RATE = 0.06           # interest-only, balloon at year 5
SELLER_DISCOUNT_RATE = 0.11       # seller's opportunity rate on a subordinate note (mezz-like)
EXISTING_LOAN = dict(original=12_500_000, rate=0.05, amort=25, months_elapsed=36, term_months=120)
ASSUMPTION_FEE_PCT = 0.01
MARKET_RATE_FOR_MTM = 0.0825
ASSUMPTION_BID = 17_600_000       # client's alternative bid, conditional on servicer approval
ASSUMPTION_APPROVAL_PROB = 0.85   # servicer approves the assumption; otherwise the all-cash bid stands


# ======================================================================= operating statement
def operating_statement(rooms_revenue_factor: float = 1.0) -> dict:
    p = T12
    rooms_rev = p["rooms_revenue"] * rooms_revenue_factor
    total = rooms_rev + p["other_revenue"]
    gop = total - p["rooms_expense"] - p["other_dept_expense"] - p["undistributed"]
    mgmt = MGMT_FEE_PCT * total
    fran = FRANCHISE_PCT * rooms_rev
    res = RESERVE_PCT * total
    ebitda_pre_tax = gop - mgmt - fran - p["insurance"]
    n = ebitda_pre_tax - res
    return {"rooms_revenue": rooms_rev, "total_revenue": total, "gop": gop, "gop_margin": gop / total,
            "mgmt_fee": mgmt, "franchise_fee": fran, "ffe_reserve": res,
            "ebitda_before_tax": ebitda_pre_tax, "noi_before_tax": n,
            "occupancy": ROOMS_SOLD / (ROOMS * DAYS), "adr": p["rooms_revenue"] / ROOMS_SOLD,
            "revpar": p["rooms_revenue"] / (ROOMS * DAYS)}


def _n_current() -> float:
    return operating_statement()["noi_before_tax"]


# ======================================================================= durability tests
def penetration_history() -> list[dict]:
    out = []
    for label, so, sa, co, ca in STR:
        idx = hotel.indices(so, sa, co, ca)
        out.append({"period": label, "subject_revpar": so * sa, "comp_revpar": co * ca, **idx})
    return out


def supply_test() -> dict:
    market_rooms = COMP_SET_ROOMS + ROOMS
    supply_growth = UNDER_CONSTRUCTION_ROOMS / market_rooms
    demand_cum = (1 + DEMAND_GROWTH) ** ABSORPTION_YEARS - 1
    occ_factor = (1 + demand_cum) / (1 + supply_growth)       # market occupancy multiplier
    o = operating_statement()
    lost_rooms_rev = o["rooms_revenue"] * (1 - occ_factor)    # subject holds MPI constant
    noi_hit = ROOMS_FLOW_THROUGH * lost_rooms_rev
    with_planned = (UNDER_CONSTRUCTION_ROOMS + PLANNED_UNFINANCED_ROOMS) / market_rooms
    occ_factor_all = (1 + demand_cum) / (1 + with_planned)
    noi_hit_all = ROOMS_FLOW_THROUGH * o["rooms_revenue"] * (1 - occ_factor_all)
    return {"market_rooms": market_rooms, "supply_growth": supply_growth, "demand_cum": demand_cum,
            "occ_factor": occ_factor, "lost_rooms_revenue": lost_rooms_rev, "noi_hit": noi_hit,
            "noi_hit_pct": noi_hit / o["noi_before_tax"],
            "supply_growth_all": with_planned, "occ_factor_all": occ_factor_all,
            "noi_hit_all": noi_hit_all, "noi_hit_all_pct": noi_hit_all / o["noi_before_tax"]}


# ======================================================================= marginal-buyer model
def size_loan(price: float, noi_after_tax: float, terms: dict | None) -> dict:
    if not terms:
        return {"max_loan": 0.0, "binding": "none"}
    return cre.max_loan(noi=noi_after_tax, value=price, annual_rate=terms["rate"], amort_years=AMORT,
                        ltv_max=terms["ltv"], dscr_min=terms["dscr"], debt_yield_min=terms["dy"])


def buyer_cash_flows(price: float, n: float, terms: dict | None, exit_cap: float = EXIT_CAP_NORMAL,
                     shock: float | None = None) -> dict:
    """Equity flows for a buyer at ``price`` holding HOLD years with acquisition debt ``terms``.

    Every bidder underwrites the financed, under-construction hotel: NOI before tax from
    year 2 onward is reduced by the supply-test hit (``shock`` defaults to it). The tax
    bill t x P grows at G. Year-1 NOI is unaffected, so a cash-on-cash buyer ignores the
    new supply entirely.
    """
    shock = -supply_test()["noi_hit_pct"] if shock is None else shock
    nb = [n * (1 + G) ** (k - 1) * (1 + (shock if k >= 2 else 0.0)) for k in range(1, HOLD + 2)]
    noi = [nb[k - 1] - T_TAX * price * (1 + G) ** (k - 1) for k in range(1, HOLD + 1)]
    sized = size_loan(price, noi[0], terms)
    loan = sized["max_loan"]
    ds = tvm.annual_debt_service(loan, terms["rate"], AMORT) if loan else 0.0
    bal = tvm.loan_balance(loan, terms["rate"], AMORT, 12 * HOLD) if loan else 0.0
    reversion = nb[HOLD] / (exit_cap + T_TAX) * (1 - SELL_COST)
    equity = price * (1 + CLOSE_COST) - loan
    flows = [-equity] + [x - ds for x in noi]
    flows[-1] += reversion - bal
    return {"flows": flows, "loan": loan, "binding": sized["binding"], "debt_service": ds, "equity": equity,
            "noi1": noi[0], "coc": (noi[0] - ds) / equity, "reversion": reversion, "balance": bal}


def _return(buyer: dict, price: float, n: float, terms: dict | None) -> float:
    cf = buyer_cash_flows(price, n, terms)
    return cf["coc"] if buyer["metric"] == "coc" else tvm.irr(cf["flows"])


def _solve(f, lo: float = 2e6, hi: float = 60e6) -> float:
    """Largest P with f(P) >= 0 (f decreasing in P), by bisection."""
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) >= 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def coc_price_closed_form(n: float, y: float, terms: dict) -> float:
    """Band-of-investment price when LTV binds: P = N / (t + lambda K + y (1 + c - lambda))."""
    k = tvm.loan_constant(terms["rate"], AMORT)
    lam = terms["ltv"]
    return n / (T_TAX + lam * k + y * (1 + CLOSE_COST - lam))


def max_price(name: str, regime: str, n: float | None = None, overrides: dict | None = None) -> dict:
    """Maximum price buyer ``name`` can pay in ``regime``: min(return-based price, equity-capacity price)."""
    n = _n_current() if n is None else n
    b = dict(BUYERS[name])
    if overrides:
        b.update(overrides)
    terms = b[regime]
    p_ret = _solve(lambda p: _return(b, p, n, terms) - b["target"])
    p_cap = float("inf")
    if b["max_equity"] is not None:
        p_cap = _solve(lambda p: b["max_equity"] - buyer_cash_flows(p, n, terms)["equity"])
    p = min(p_ret, p_cap)
    cf = buyer_cash_flows(p, n, terms)
    return {"buyer": name, "regime": regime, "price_return": p_ret, "price_capacity": p_cap, "max_price": p,
            "capacity_binds": p_cap < p_ret, "loan": cf["loan"], "binding": cf["binding"],
            "equity": cf["equity"], "per_key": p / ROOMS, "going_in_cap": (n - T_TAX * p) / p}


def clearing(regime_terms: dict, n: float, active: dict) -> dict:
    """Clearing price = second-highest maximum price among active buyers.

    ``regime_terms``: buyer -> regime label used for that buyer's debt terms.
    ``active``: buyer -> bool.
    """
    bids = {}
    for name in BUYERS:
        if active[name]:
            bids[name] = max_price(name, regime_terms[name], n)["max_price"]
    ranked = sorted(bids.items(), key=lambda kv: kv[1], reverse=True)
    return {"bids": bids, "ranked": ranked, "top": ranked[0], "clearing": ranked[1][1],
            "marginal_buyer": ranked[1][0]}


def regime_table() -> dict:
    n_now = _n_current()
    out = {}
    for regime, n in (("normal", N_PRE_CRUNCH), ("crunch", n_now)):
        rows = {name: max_price(name, regime, n) for name in BUYERS}
        active = {name: BUYERS[name]["active"][regime] for name in BUYERS}
        c = clearing({name: regime for name in BUYERS}, n, active)
        out[regime] = {"rows": rows, **c}
    return out


def decomposition() -> dict:
    """Sequential decomposition of the clearing-price decline, normal -> crunch.

    Order A: fundamentals, loan proceeds (LTV/DSCR/DY), loan rate, buyer-universe exits.
    Order B: financing (proceeds+rate+universe) first, fundamentals last.
    """
    n0, n1 = N_PRE_CRUNCH, _n_current()
    all_on = {k: True for k in BUYERS}
    crunch_active = {k: BUYERS[k]["active"]["crunch"] for k in BUYERS}

    def proceeds_only(name):  # crunch LTV/DSCR/DY, normal rate
        b = BUYERS[name]
        if not b["normal"]:
            return None
        return {**b["crunch"], "rate": b["normal"]["rate"]}

    def clear_custom(n, terms_fn, active):
        bids = {}
        for name in BUYERS:
            if not active[name]:
                continue
            b = BUYERS[name]
            terms = terms_fn(name)
            p_ret = _solve(lambda p: _return(b, p, n, terms) - b["target"])
            p_cap = float("inf")
            if b["max_equity"] is not None:
                p_cap = _solve(lambda p: b["max_equity"] - buyer_cash_flows(p, n, terms)["equity"])
            bids[name] = min(p_ret, p_cap)
        ranked = sorted(bids.values(), reverse=True)
        return ranked[1]

    normal_terms = lambda name: BUYERS[name]["normal"]   # noqa: E731
    crunch_terms = lambda name: BUYERS[name]["crunch"]   # noqa: E731
    s0 = clear_custom(n0, normal_terms, all_on)
    s1 = clear_custom(n1, normal_terms, all_on)
    s2 = clear_custom(n1, proceeds_only, all_on)
    s3 = clear_custom(n1, crunch_terms, all_on)
    s4 = clear_custom(n1, crunch_terms, crunch_active)
    steps = {"start": s0, "after_fundamentals": s1, "after_proceeds": s2, "after_rate": s3, "after_universe": s4}
    order_a = {"start": s0, "fundamentals": s1 - s0, "proceeds": s2 - s1, "rate": s3 - s2,
               "universe": s4 - s3, "end": s4}
    b1 = clear_custom(n0, crunch_terms, crunch_active)
    order_b = {"financing": b1 - s0, "fundamentals": s4 - b1}
    total = s4 - s0
    return {"order_a": order_a, "order_b": order_b, "total": total, "total_pct": total / s0, "steps": steps,
            "financing_share_a": 1 - order_a["fundamentals"] / total,
            "fundamentals_share_a": order_a["fundamentals"] / total,
            "fundamentals_share_b": order_b["fundamentals"] / total}


def leverage_check() -> dict:
    """Loan constants vs going-in caps: is leverage accretive in each regime?"""
    rt = regime_table()
    out = {}
    for regime in REGIMES:
        r = rt[regime]["rows"]["Owner-operator"]
        k = tvm.loan_constant(BUYERS["Owner-operator"][regime]["rate"], AMORT)
        out[regime] = {"loan_constant": k, "going_in_cap": r["going_in_cap"], "spread": r["going_in_cap"] - k}
    return out


def seller_certainty_equivalent() -> dict:
    """All-cash price that leaves the seller indifferent to the top financed bid.

    E[financed] = q P_fin + (1 - q) P_fallback / (1 + d)^(m/12), with the fallback bid the crunch
    clearing price (second-highest maximum), received after re-marketing.
    """
    rt = regime_table()["crunch"]
    p_fin = rt["top"][1]
    fallback = rt["clearing"]
    disc = (1 + SELLER_DELAY_RATE) ** (REMARKET_MONTHS / 12)
    ev = FINANCED_CLOSE_PROB * p_fin + (1 - FINANCED_CLOSE_PROB) * fallback / disc
    return {"financed_bid": p_fin, "fallback": fallback, "fallback_pv": fallback / disc, "ev_financed": ev,
            "discount_vs_financed": p_fin - ev}


# ======================================================================= client: all-cash then refinance
def client_scenario(price: float, refi_year: int | None, noi_shock, exit_regime: str) -> dict:
    n = _n_current()
    if noi_shock == UC_SHOCK:
        noi_shock = -supply_test()["noi_hit_pct"]
    path = []
    for k in range(1, HOLD + 2):
        nb = n * (1 + G) ** (k - 1)
        if k >= 2:
            nb *= (1 + noi_shock)
        path.append(nb)
    tax = [T_TAX * price * (1 + G) ** (k - 1) for k in range(1, HOLD + 2)]
    noi = [a - b for a, b in zip(path, tax)]
    flows = [-price * (1 + CLOSE_COST)] + noi[:HOLD]
    loan = ds = 0.0
    refi = None
    if refi_year is not None:
        fwd = noi[refi_year]                     # year refi_year+1 NOI after (unreassessed) tax
        appraised = fwd / REFI_APPRAISAL_CAP
        sized = cre.max_loan(noi=fwd, value=appraised, annual_rate=REFI_TERMS["rate"], amort_years=AMORT,
                             ltv_max=REFI_TERMS["ltv"], dscr_min=REFI_TERMS["dscr"],
                             debt_yield_min=REFI_TERMS["dy"])
        loan = sized["max_loan"]
        ds = tvm.annual_debt_service(loan, REFI_TERMS["rate"], AMORT)
        flows[refi_year] += loan * (1 - REFI_COST_PCT)
        for k in range(refi_year + 1, HOLD + 1):
            flows[k] -= ds
        bal = tvm.loan_balance(loan, REFI_TERMS["rate"], AMORT, 12 * (HOLD - refi_year))
        refi = {"appraised": appraised, "loan": loan, "binding": sized["binding"], "debt_service": ds,
                "balance_at_exit": bal, "net_proceeds": loan * (1 - REFI_COST_PCT),
                "dscr": fwd / ds}
    else:
        bal = 0.0
    cap = EXIT_CAP_NORMAL if exit_regime == "normal" else EXIT_CAP_CRUNCH
    reversion = path[HOLD] / (cap + T_TAX) * (1 - SELL_COST)
    flows[HOLD] += reversion - bal
    return {"flows": flows, "irr": tvm.irr(flows), "multiple": tvm.equity_multiple(flows),
            "reversion": reversion, "refi": refi, "noi_y1": noi[0], "noi_shock": noi_shock,
            "profit": sum(flows), "npv_at_target": tvm.npv(CLIENT_TARGET_IRR, flows)}


def client_analysis(price: float = None) -> dict:
    price = CLIENT_PRICE if price is None else price
    res = {}
    for name, (p, ry, shock, ex) in SCENARIOS.items():
        res[name] = {"p": p, **client_scenario(price, ry, shock, ex)}
    probs = [v["p"] for v in res.values()]
    irrs = [v["irr"] for v in res.values()]
    profits = [v["profit"] for v in res.values()]
    exp_irr = sum(p * i for p, i in zip(probs, irrs))
    summ = cre.scenario_summary(profits, probs)
    no_refi_normal = client_scenario(price, None, UC_SHOCK, "normal")
    e_npv = sum(v["p"] * v["npv_at_target"] for v in res.values())
    return {"price": price, "scenarios": res, "expected_irr": exp_irr, "expected_profit": summ["ev"],
            "expected_npv": e_npv, "p_loss": summ["p_loss"], "unlevered_base_irr": no_refi_normal["irr"],
            "timing_cost_npv": res["Credit returns in 1 year"]["npv_at_target"] - res["Credit returns in 4 years"]["npv_at_target"],
            "timing_cost_irr": res["Credit returns in 1 year"]["irr"] - res["Credit returns in 4 years"]["irr"],
            "timing_cost_profit": res["Credit returns in 1 year"]["profit"] - res["Credit returns in 4 years"]["profit"]}


def client_max_price(criterion: str = "npv") -> float:
    """Highest all-cash price meeting the client's 13% hurdle.

    criterion "npv": probability-weighted NPV at 13% >= 0 (correct).
    criterion "irr": probability-weighted IRR >= 13% (common, and biased; see Mode B).
    """
    if criterion == "npv":
        return _solve(lambda p: client_analysis(p)["expected_npv"])
    return _solve(lambda p: client_analysis(p)["expected_irr"] - CLIENT_TARGET_IRR)


def naive_max_price() -> float:
    """Max price if the analyst assumes credit returns in one year with certainty (NPV of that path = 0)."""
    p, ry, shock, ex = SCENARIOS["Credit returns in 1 year"]
    return _solve(lambda x: client_scenario(x, ry, shock, ex)["npv_at_target"])


def client_assumption_scenario(price: float, noi_shock, exit_regime: str) -> dict:
    """Client buys with assumption of the seller's 5.00% loan; no refinancing; repays at par at exit."""
    n = _n_current()
    if noi_shock == UC_SHOCK:
        noi_shock = -supply_test()["noi_hit_pct"]
    a = assumable_debt()
    e = EXISTING_LOAN
    path = [n * (1 + G) ** (k - 1) * (1 + (noi_shock if k >= 2 else 0.0)) for k in range(1, HOLD + 2)]
    noi = [path[k - 1] - T_TAX * price * (1 + G) ** (k - 1) for k in range(1, HOLD + 1)]
    equity = price * (1 + CLOSE_COST) + a["fee"] - a["balance"]
    flows = [-equity] + [x - a["annual_ds"] for x in noi]
    bal_exit = tvm.loan_balance(e["original"], e["rate"], e["amort"], e["months_elapsed"] + 12 * HOLD)
    cap = EXIT_CAP_NORMAL if exit_regime == "normal" else EXIT_CAP_CRUNCH
    reversion = path[HOLD] / (cap + T_TAX) * (1 - SELL_COST)
    flows[HOLD] += reversion - bal_exit
    return {"flows": flows, "irr": tvm.irr(flows), "equity": equity, "balance_at_exit": bal_exit,
            "npv_at_target": tvm.npv(CLIENT_TARGET_IRR, flows), "dscr_y1": noi[0] / a["annual_ds"]}


def client_assumption_analysis(price: float) -> dict:
    res = {}
    for name, (p, _ry, shock, ex) in SCENARIOS.items():
        res[name] = {"p": p, **client_assumption_scenario(price, shock, ex)}
    # identical paths for the three credit-return scenarios: the loan is fixed, refinancing timing is irrelevant
    return {"price": price, "scenarios": res,
            "expected_irr": sum(v["p"] * v["irr"] for v in res.values()),
            "expected_npv": sum(v["p"] * v["npv_at_target"] for v in res.values())}


def client_assumption_max_price(target: float | None = None) -> float:
    global CLIENT_TARGET_IRR
    old = CLIENT_TARGET_IRR
    try:
        if target is not None:
            CLIENT_TARGET_IRR = target
        return _solve(lambda p: client_assumption_analysis(p)["expected_npv"])
    finally:
        CLIENT_TARGET_IRR = old


def seller_options() -> dict:
    """Seller's certainty-equivalent value of each offer (before selling costs, which are common)."""
    se = seller_certainty_equivalent()
    sf = seller_financing()
    ce_assume = ASSUMPTION_APPROVAL_PROB * ASSUMPTION_BID + (1 - ASSUMPTION_APPROVAL_PROB) * CLIENT_PRICE
    return {"financed_bid_headline": se["financed_bid"], "financed_bid_ce": se["ev_financed"],
            "all_cash_bid": CLIENT_PRICE,
            "seller_note_headline": sf["price"], "seller_note_ce": sf["seller_cash_equivalent"],
            "assumption_headline": ASSUMPTION_BID, "assumption_ce": ce_assume}


def breakeven_impairment_probability(price: float = None) -> float:
    """Probability of the impairment scenario (others rescaled pro rata) at which expected IRR = target."""
    price = CLIENT_PRICE if price is None else price
    a = client_analysis(price)["scenarios"]
    imp = a["Impairment"]["irr"]
    others = {k: v for k, v in a.items() if k != "Impairment"}
    w = sum(v["p"] for v in others.values())
    good = sum(v["p"] * v["irr"] for v in others.values()) / w
    # q*imp + (1-q)*good = target
    return (good - CLIENT_TARGET_IRR) / (good - imp)


# ======================================================================= seller financing and assumable debt
def seller_financing() -> dict:
    """Owner-operator buys with crunch bank loan (45%) + seller note (20%) at 9% target cash-on-cash.

    Bank sized at 45% of price (LTV binds; checked). Seller note IO at 6%.
    CoC = (N - tP - DS_bank - i_note * s P) / (P(1 + c) - lambda P - s P) = y. Linear in P.
    """
    n = _n_current()
    b = BUYERS["Owner-operator"]["crunch"]
    y = BUYERS["Owner-operator"]["target"]
    k = tvm.loan_constant(b["rate"], AMORT)
    lam, s = b["ltv"], SELLER_NOTE_SHARE
    price = n / (T_TAX + lam * k + SELLER_NOTE_RATE * s + y * (1 + CLOSE_COST - lam - s))
    bank = lam * price
    note = s * price
    equity = price * (1 + CLOSE_COST) - bank - note
    noi1 = n - T_TAX * price
    bank_ds = tvm.annual_debt_service(bank, b["rate"], AMORT)
    note_int = SELLER_NOTE_RATE * note
    # seller's cash-equivalent: cash at close + PV of note (IO, balloon year 5) at seller's opportunity rate
    pv_note = sum(note_int / (1 + SELLER_DISCOUNT_RATE) ** t for t in range(1, 6)) + note / (1 + SELLER_DISCOUNT_RATE) ** 5
    cash_equiv = price - note + pv_note
    sized = size_loan(price, noi1, b)
    return {"price": price, "bank_loan": bank, "note": note, "equity": equity, "noi1": noi1,
            "bank_ds": bank_ds, "note_interest": note_int, "dscr_total": noi1 / (bank_ds + note_int),
            "coc": (noi1 - bank_ds - note_int) / equity, "pv_note": pv_note, "note_discount": note - pv_note,
            "seller_cash_equivalent": cash_equiv, "bank_binding": sized["binding"],
            "combined_ltv": (bank + note) / price}


def assumable_debt() -> dict:
    """Existing 5.00% loan: balance, mark-to-market at the crunch rate, owner-operator max price with assumption."""
    e = EXISTING_LOAN
    bal = tvm.loan_balance(e["original"], e["rate"], e["amort"], e["months_elapsed"])
    pmt = tvm.payment(e["original"], e["rate"], e["amort"])
    rem = e["term_months"] - e["months_elapsed"]
    balloon = tvm.loan_balance(e["original"], e["rate"], e["amort"], e["term_months"])
    i = MARKET_RATE_FOR_MTM / 12
    pv = pmt * tvm.annuity_factor(i, rem) + balloon / (1 + i) ** rem
    mtm_gain = bal - pv
    ds = 12 * pmt
    n = _n_current()
    y = BUYERS["Owner-operator"]["target"]
    fee = ASSUMPTION_FEE_PCT * bal
    # (N - tP - DS) / (P(1+c) + fee - B) = y  =>  P = (N - DS + y(B - fee)) / (t + y(1+c))
    price = (n - ds + y * (bal - fee)) / (T_TAX + y * (1 + CLOSE_COST))
    equity = price * (1 + CLOSE_COST) + fee - bal
    noi1 = n - T_TAX * price
    return {"balance": bal, "monthly_payment": pmt, "annual_ds": ds, "remaining_months": rem,
            "balloon": balloon, "pv_at_market": pv, "mtm_gain": mtm_gain, "fee": fee,
            "price": price, "equity": equity, "ltv": bal / price, "dscr": noi1 / ds,
            "debt_yield": noi1 / bal, "coc": (noi1 - ds) / equity}


# ======================================================================= report
def report() -> str:
    o = operating_statement()
    L = [f"Revenue {o['total_revenue']:,.0f} GOP {o['gop']:,.0f} ({o['gop_margin']:.1%}) "
         f"N (NOI before tax) {o['noi_before_tax']:,.0f}; pre-crunch N {N_PRE_CRUNCH:,.0f}",
         f"Occ {o['occupancy']:.2%} ADR {o['adr']:.2f} RevPAR {o['revpar']:.2f}"]
    for r in penetration_history():
        L.append(f"  {r['period']:<28s} subj RevPAR {r['subject_revpar']:.2f} comp {r['comp_revpar']:.2f} "
                 f"MPI {r['mpi']:.1f} ARI {r['ari']:.1f} RGI {r['rgi']:.1f}")
    s = supply_test()
    L.append(f"Supply: +{s['supply_growth']:.2%} vs demand +{s['demand_cum']:.2%}; occ factor {s['occ_factor']:.4f}; "
             f"NOI hit {s['noi_hit']:,.0f} ({s['noi_hit_pct']:.1%}); with planned +{s['supply_growth_all']:.2%} "
             f"hit {s['noi_hit_all']:,.0f} ({s['noi_hit_all_pct']:.1%})")
    for regime, d in regime_table().items():
        L.append(f"[{regime}]")
        for name, r in d["rows"].items():
            act = "active" if BUYERS[name]["active"][regime] else "inactive"
            L.append(f"  {name:<26s} max {r['max_price']:>12,.0f} ({r['per_key']:,.0f}/key) loan {r['loan']:>12,.0f} "
                     f"({r['binding']}) equity {r['equity']:>12,.0f} cap {r['going_in_cap']:.2%} "
                     f"{'CAPACITY' if r['capacity_binds'] else ''} {act}")
        L.append(f"  top {d['top'][0]} {d['top'][1]:,.0f}; clearing {d['clearing']:,.0f} set by {d['marginal_buyer']}")
    dc = decomposition()
    L.append("Decomposition A: " + ", ".join(f"{k} {v:,.0f}" for k, v in dc["order_a"].items()))
    L.append("Decomposition B: " + ", ".join(f"{k} {v:,.0f}" for k, v in dc["order_b"].items()))
    L.append(f"Total {dc['total']:,.0f} ({dc['total_pct']:.1%}); fundamentals share {dc['fundamentals_share_a']:.1%} / "
             f"{dc['fundamentals_share_b']:.1%}")
    for k, v in decomposition()["steps"].items():
        L.append(f"  step {k:<20s} {v:,.0f}")
    for k, v in leverage_check().items():
        L.append(f"  leverage {k}: K {v['loan_constant']:.4%} cap {v['going_in_cap']:.4%} spread {v['spread']:.4%}")
    se = seller_certainty_equivalent()
    L.append("Seller CE: " + ", ".join(f"{k} {v:,.0f}" for k, v in se.items()))
    ca = client_analysis()
    for name, v in ca["scenarios"].items():
        rf = v["refi"]
        L.append(f"  {name:<28s} p {v['p']:.2f} IRR {v['irr']:.2%} EM {v['multiple']:.2f}x profit {v['profit']:,.0f} NPV {v['npv_at_target']:,.0f} shock {v['noi_shock']:.4f} "
                 + (f"refi loan {rf['loan']:,.0f} ({rf['binding']}) DSCR {rf['dscr']:.2f}" if rf else ""))
    L.append(f"Client @ {ca['price']:,.0f}: E[IRR] {ca['expected_irr']:.2%}, E[profit] {ca['expected_profit']:,.0f}, "
             f"E[NPV@13%] {ca['expected_npv']:,.0f} timing NPV {ca['timing_cost_npv']:,.0f} P(loss) {ca['p_loss']:.2f}, unlevered base {ca['unlevered_base_irr']:.2%}, timing cost "
             f"{ca['timing_cost_irr']:.2%} / {ca['timing_cost_profit']:,.0f}")
    L.append(f"Client max price: E[NPV]=0 {client_max_price():,.0f}; E[IRR]=13% {client_max_price('irr'):,.0f}; break-even impairment prob "
             f"{breakeven_impairment_probability():.3f}")
    sf = seller_financing()
    L.append("Seller financing: " + ", ".join(f"{k} {v:,.4f}" if isinstance(v, float) else f"{k} {v}" for k, v in sf.items()))
    ad = assumable_debt()
    L.append("Assumable: " + ", ".join(f"{k} {v:,.4f}" for k, v in ad.items()))
    ASSUME_BID = ASSUMPTION_BID
    aa = client_assumption_analysis(ASSUME_BID)
    for name, v in aa["scenarios"].items():
        L.append(f"  assume {name:<28s} IRR {v['irr']:.2%} NPV {v['npv_at_target']:,.0f} DSCR {v['dscr_y1']:.2f}")
    L.append(f"Assumption @ {ASSUME_BID:,.0f}: E[IRR] {aa['expected_irr']:.2%} E[NPV] {aa['expected_npv']:,.0f}; "
             f"max price {client_assumption_max_price():,.0f}; at 15% {client_assumption_max_price(0.15):,.0f}")
    L.append(f"Naive (1-yr refi certain) max price {naive_max_price():,.0f}")
    L.append("Seller options: " + ", ".join(f"{k} {v:,.0f}" for k, v in seller_options().items()))
    return "\n".join(L)


if __name__ == "__main__":
    print(report())
