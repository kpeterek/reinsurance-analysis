"""Case A — The Overpriced Hotel Owner. Reproducible model.

Run:  python3 cases/hypothetical/case_A_overpriced_hotel_owner/case_a_model.py
All inputs are hypothetical [HYPOTHESIS]. Every number quoted in the case text
is produced here and asserted in tests/test_case_a.py.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "models" / "python"))

from sdesk import cre, tvm  # noqa: E402

# ----------------------------------------------------------------- inputs
ROOMS = 82
DAYS = 365
ROOMS_SOLD = 20_951
ADR = 118.00

OWNER_PL = {  # trailing twelve months as presented by the owner
    "rooms_revenue": 2_472_218,
    "other_operated_revenue": 28_600,
    "misc_income_insurance_proceeds": 55_000,
    "rooms_expense": 672_000,
    "other_operated_expense": 9_500,
    "admin_general": 264_000,
    "sales_marketing": 68_000,
    "repairs_maintenance": 162_000,
    "utilities": 164_000,
    "it_telecom": 26_000,
    "management_fee": 0,
    "franchise_fees": 259_583,  # 10.5% of rooms revenue
    "property_tax": 78_200,      # CAD assessed value $3.4m x 2.30%
    "insurance": 41_000,
    "ffe_reserve": 0,
}

FRANCHISE_PCT = 0.105
MGMT_FEE_PCT = 0.03
RESERVE_PCT = 0.04
TAX_RATE = 0.023             # combined rate, hypothetical
ASSESSMENT_RATIO = 0.85      # assessed value / purchase price (real property only), hypothetical
EFFECTIVE_TAX_ON_PRICE = TAX_RATE * ASSESSMENT_RATIO  # 1.955%

# Normalization inputs
PIPELINE_RN = 1_850
PIPELINE_ADR = 112.0
BACKFILL_SHARE = 0.40
BACKFILL_ADR = 119.0
VARIABLE_CPOR = 14.0          # variable rooms cost per occupied room (housekeeping, supplies, laundry)
OWNER_PERSONAL = 38_000
SPOUSE_SALARY = 30_000
MARKET_GM_COST = 72_000
ROOF_CAPEX_EXPENSED = 62_000
INSURANCE_QUOTE = 68_000

# Valuation and transaction inputs
OWNER_ASK = 8_000_000
OWNER_COST_BASIS = 8_000_000  # 2015 development $7.6m + 2019 refresh $0.4m
REPLACEMENT_COST_PER_KEY = 135_000
PIP_PER_KEY = 8_000
PIP_CONTINGENCY = 0.10
PIP_DISPLACEMENT = 60_000     # NOI lost during renovation (rooms out of order)
BUYER_CLOSING_PCT = 0.02

SCENARIOS = {  # name: (NOI multiplier on normalized pre-tax NOI, cap rate)
    "Upside": (1.03, 0.0875),
    "Base": (1.00, 0.0950),
    "Downside": (0.92, 0.1050),
}

LOAN = dict(rate=0.0775, amort=25, ltv=0.65, dscr=1.40, debt_yield=0.11)

# Seller's existing debt (hypothetical): matures in 14 months
SELLER_LOAN_BALANCE = 4_300_000
SELLER_SALE_COST_PCT = 0.03       # broker + title + legal
REFI_COST_PCT = 0.015


def owner_statement() -> dict:
    p = OWNER_PL
    revenue = p["rooms_revenue"] + p["other_operated_revenue"] + p["misc_income_insurance_proceeds"]
    dept = p["rooms_expense"] + p["other_operated_expense"]
    undist = p["admin_general"] + p["sales_marketing"] + p["repairs_maintenance"] + p["utilities"] + p["it_telecom"]
    gop = revenue - dept - undist
    ebitda = gop - p["management_fee"] - p["franchise_fees"] - p["property_tax"] - p["insurance"]
    return {"total_revenue": revenue, "departmental": dept, "undistributed": undist, "gop": gop,
            "ebitda": ebitda, "owner_cap_value_8_5": ebitda / 0.085,
            "occupancy": ROOMS_SOLD / (ROOMS * DAYS), "adr": p["rooms_revenue"] / ROOMS_SOLD,
            "revpar": p["rooms_revenue"] / (ROOMS * DAYS)}


def normalized_statement() -> dict:
    """Normalize the owner's T-12 to a buyer's stabilized, pre-property-tax NOI."""
    p = OWNER_PL
    lost_rn = PIPELINE_RN * (1 - BACKFILL_SHARE)
    pipeline_rev_removed = PIPELINE_RN * PIPELINE_ADR - PIPELINE_RN * BACKFILL_SHARE * BACKFILL_ADR
    rooms_rev = p["rooms_revenue"] - pipeline_rev_removed
    rooms_sold = ROOMS_SOLD - lost_rn
    other_rev = p["other_operated_revenue"]
    total_rev = rooms_rev + other_rev                      # insurance proceeds removed
    rooms_exp = p["rooms_expense"] - lost_rn * VARIABLE_CPOR
    other_exp = p["other_operated_expense"]
    ag = p["admin_general"] - OWNER_PERSONAL - SPOUSE_SALARY + MARKET_GM_COST
    rm = p["repairs_maintenance"] - ROOF_CAPEX_EXPENSED
    undist = ag + p["sales_marketing"] + rm + p["utilities"] + p["it_telecom"]
    gop = total_rev - rooms_exp - other_exp - undist
    mgmt = MGMT_FEE_PCT * total_rev
    franchise = p["franchise_fees"] - FRANCHISE_PCT * pipeline_rev_removed
    insurance = INSURANCE_QUOTE
    reserve = RESERVE_PCT * total_rev
    noi_pre_tax = gop - mgmt - franchise - insurance - reserve
    return {
        "pipeline_rev_removed": pipeline_rev_removed, "lost_room_nights": lost_rn,
        "rooms_revenue": rooms_rev, "rooms_sold": rooms_sold,
        "occupancy": rooms_sold / (ROOMS * DAYS), "adr": rooms_rev / rooms_sold,
        "revpar": rooms_rev / (ROOMS * DAYS),
        "total_revenue": total_rev, "rooms_expense": rooms_exp, "admin_general": ag,
        "repairs_maintenance": rm, "undistributed": undist, "gop": gop,
        "gop_margin": gop / total_rev, "mgmt_fee": mgmt, "franchise_fees": franchise,
        "insurance": insurance, "ffe_reserve": reserve, "noi_before_property_tax": noi_pre_tax,
    }


def noi_bridge() -> list[tuple[str, float]]:
    """Owner EBITDA -> buyer NOI before property tax, line by line."""
    o, n = owner_statement(), normalized_statement()
    p = OWNER_PL
    steps = [
        ("Owner-presented EBITDA (no reserve)", o["ebitda"]),
        ("Add back owner's property tax (re-underwritten below)", p["property_tax"]),
        ("Remove hail insurance proceeds", -p["misc_income_insurance_proceeds"]),
        ("Remove non-recurring pipeline block, net of backfill", -n["pipeline_rev_removed"]),
        ("Variable rooms cost saved on lost room-nights", n["lost_room_nights"] * VARIABLE_CPOR),
        ("Franchise fees saved on removed revenue", FRANCHISE_PCT * n["pipeline_rev_removed"]),
        ("Add back owner personal expenses", OWNER_PERSONAL),
        ("Replace spouse salary with market GM", SPOUSE_SALARY - MARKET_GM_COST),
        ("Reclassify roof replacement to capital", ROOF_CAPEX_EXPENSED),
        ("Market management fee (3% of revenue)", -n["mgmt_fee"]),
        ("Insurance at buyer's renewal quote", p["insurance"] - INSURANCE_QUOTE),
        ("FF&E reserve (4% of revenue)", -n["ffe_reserve"]),
    ]
    total = sum(v for _, v in steps)
    assert abs(total - n["noi_before_property_tax"]) < 1e-6, (total, n["noi_before_property_tax"])
    steps.append(("Buyer NOI before property tax", total))
    return steps


def scenario_values() -> dict:
    n = normalized_statement()
    out = {}
    for name, (mult, cap) in SCENARIOS.items():
        noi_pt = n["noi_before_property_tax"] * mult
        v = cre.loaded_cap_value(noi_pt, cap, EFFECTIVE_TAX_ON_PRICE)
        tax = EFFECTIVE_TAX_ON_PRICE * v
        noi = noi_pt - tax
        pip_all_in = PIP_PER_KEY * ROOMS * (1 + PIP_CONTINGENCY)
        price = v - pip_all_in - PIP_DISPLACEMENT          # as-is value, PIP-adjusted
        out[name] = {"noi_before_tax": noi_pt, "stabilized_value": v, "property_tax": tax,
                     "noi": noi, "cap": cap, "pip_all_in": pip_all_in,
                     "as_is_value": price, "per_key": price / ROOMS}
    return out


def unloaded_value_error() -> dict:
    """Value if a buyer forgets reassessment and capitalizes NOI with the owner's tax bill."""
    n = normalized_statement()
    noi_with_old_tax = n["noi_before_property_tax"] - OWNER_PL["property_tax"]
    wrong = noi_with_old_tax / 0.095
    right = cre.loaded_cap_value(n["noi_before_property_tax"], 0.095, EFFECTIVE_TAX_ON_PRICE)
    return {"wrong": wrong, "right": right, "overstatement": wrong - right}


def financing(price: float, noi: float) -> dict:
    sized = cre.max_loan(noi=noi, value=price, annual_rate=LOAN["rate"], amort_years=LOAN["amort"],
                         ltv_max=LOAN["ltv"], dscr_min=LOAN["dscr"], debt_yield_min=LOAN["debt_yield"])
    loan = sized["max_loan"]
    ds = tvm.annual_debt_service(loan, LOAN["rate"], LOAN["amort"])
    closing = price * BUYER_CLOSING_PCT
    pip = PIP_PER_KEY * ROOMS * (1 + PIP_CONTINGENCY)
    equity = price + closing + pip + PIP_DISPLACEMENT - loan
    return {**sized, "debt_service": ds, "dscr_actual": noi / ds, "equity": equity,
            "cash_on_cash": (noi - ds) / equity, "all_in_basis": price + closing + pip + PIP_DISPLACEMENT}


def seller_position() -> dict:
    """The owner's refinancing alternative and the sale price that pays off the loan.

    Refinance is sized on the lender's normalized NOI (owner's current tax bill is
    NOT reassessed on a refinance) and an appraised value at the base cap rate.
    """
    n = normalized_statement()
    noi_refi = n["noi_before_property_tax"] - OWNER_PL["property_tax"]
    appraised = noi_refi / SCENARIOS["Base"][1]
    sized = cre.max_loan(noi=noi_refi, value=appraised, annual_rate=LOAN["rate"], amort_years=LOAN["amort"],
                         ltv_max=LOAN["ltv"], dscr_min=LOAN["dscr"], debt_yield_min=LOAN["debt_yield"])
    new_loan = sized["max_loan"]
    gap = cre.refinance_gap(SELLER_LOAN_BALANCE, new_loan, REFI_COST_PCT * new_loan)
    breakeven_sale = SELLER_LOAN_BALANCE / (1 - SELLER_SALE_COST_PCT)
    return {"noi_refi": noi_refi, "appraised": appraised, **{f"refi_{k}": v for k, v in sized.items()},
            "refi_gap": gap, "payoff_price": breakeven_sale}


def breakeven_occupancy_at_price(price: float, include_debt: bool = True) -> dict:
    """Occupancy at which cash flow (after reserve, tax, and optionally debt service) is zero.

    Cost structure from the normalized statement: rooms expense split into a
    variable part (VARIABLE_CPOR per occupied room) and a fixed remainder;
    undistributed, insurance, reassessed tax and other operated expense are fixed;
    other operated revenue is treated as a fixed offset. Franchise fees (on rooms),
    management fee and reserve (on revenue) vary with ADR x rooms sold. ADR is held
    at the normalized level -- in practice ADR falls with occupancy, so this is
    an optimistic bound.
    """
    n = normalized_statement()
    fixed_rooms = n["rooms_expense"] - VARIABLE_CPOR * n["rooms_sold"]
    tax = EFFECTIVE_TAX_ON_PRICE * price
    fixed = (n["undistributed"] + INSURANCE_QUOTE + tax + fixed_rooms
             + OWNER_PL["other_operated_expense"] - OWNER_PL["other_operated_revenue"])
    ds = 0.0
    if include_debt:
        ds = financing(price, n["noi_before_property_tax"] - tax)["debt_service"]
    contrib = n["adr"] * (1 - FRANCHISE_PCT - MGMT_FEE_PCT - RESERVE_PCT) - VARIABLE_CPOR
    occ = (fixed + ds) / contrib / (ROOMS * DAYS)
    return {"fixed_costs": fixed, "debt_service": ds, "contribution_per_room_night": contrib,
            "breakeven_occupancy": occ}


def bid_price(target_yield_on_cost: float, noi_before_tax: float) -> float:
    """Price P such that NOI after reassessed tax / all-in basis = target.

    all-in = P(1 + closing) + PIP_all_in + displacement ; NOI = N - t*P
    => N - tP = y [P(1+c) + K]  =>  P = (N - yK) / (t + y(1+c))
    """
    k = PIP_PER_KEY * ROOMS * (1 + PIP_CONTINGENCY) + PIP_DISPLACEMENT
    t, y, c = EFFECTIVE_TAX_ON_PRICE, target_yield_on_cost, BUYER_CLOSING_PCT
    return (noi_before_tax - y * k) / (t + y * (1 + c))


def report() -> str:
    o, n = owner_statement(), normalized_statement()
    lines = ["Owner T-12: revenue {:,.0f}  GOP {:,.0f}  EBITDA {:,.0f}  -> 8.5% cap {:,.0f}".format(
        o["total_revenue"], o["gop"], o["ebitda"], o["owner_cap_value_8_5"]),
        "Occ {:.2%}  ADR {:.2f}  RevPAR {:.2f}".format(o["occupancy"], o["adr"], o["revpar"]), "",
        "NOI bridge:"]
    for label, v in noi_bridge():
        lines.append(f"  {label:<58s}{v:>12,.0f}")
    lines.append("Normalized: occ {:.2%} ADR {:.2f} RevPAR {:.2f} revenue {:,.0f} GOP {:,.0f} ({:.1%})".format(
        n["occupancy"], n["adr"], n["revpar"], n["total_revenue"], n["gop"], n["gop_margin"]))
    lines.append("")
    for name, s in scenario_values().items():
        lines.append("{:<9s} cap {:.2%} NOI {:,.0f} tax {:,.0f} stabilized {:,.0f} as-is {:,.0f} ({:,.0f}/key)".format(
            name, s["cap"], s["noi"], s["property_tax"], s["stabilized_value"], s["as_is_value"], s["per_key"]))
    e = unloaded_value_error()
    lines.append("Forgetting reassessment at 9.5%: {:,.0f} vs {:,.0f} (overstates by {:,.0f})".format(
        e["wrong"], e["right"], e["overstatement"]))
    lines.append("Replacement cost: {:,.0f}".format(REPLACEMENT_COST_PER_KEY * ROOMS))
    for y in (0.095, 0.10, 0.105):
        p = bid_price(y, n["noi_before_property_tax"])
        f = financing(p, n["noi_before_property_tax"] - EFFECTIVE_TAX_ON_PRICE * p)
        lines.append("Bid @ {:.1%} yield on cost: price {:,.0f} | loan {:,.0f} ({}) DS {:,.0f} DSCR {:.2f} "
                     "equity {:,.0f} CoC {:.2%}".format(y, p, f["max_loan"], f["binding"], f["debt_service"],
                                                        f["dscr_actual"], f["equity"], f["cash_on_cash"]))
    sp = seller_position()
    lines.append("Seller refi: NOI {:,.0f} appraised {:,.0f} loan {:,.0f} ({}) gap {:,.0f}; payoff price {:,.0f}".format(
        sp["noi_refi"], sp["appraised"], sp["refi_max_loan"], sp["refi_binding"], sp["refi_gap"], sp["payoff_price"]))
    return "\n".join(lines)


if __name__ == "__main__":
    print(report())
