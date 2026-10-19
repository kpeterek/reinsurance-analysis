"""Hotel operating metrics and USALI-style income statements.

Conventions
-----------
* Occupancy, ADR, RevPAR are computed on AVAILABLE room-nights for the period.
* ``days`` defaults to 365. Use 366 for leap years when matching actual P&Ls.
* Room revenue excludes hotel occupancy taxes collected for the taxing authority.
* EBITDA here = income before FF&E reserve, interest, depreciation, and income
  taxes but after management fees, franchise fees, property taxes and insurance
  (a "net operating income before reserve"). NOI = EBITDA - FF&E reserve.
  Lenders and buyers in the U.S. typically capitalize NOI after a reserve of
  3-5% of total revenue; state the reserve explicitly.
"""

from __future__ import annotations


def available_room_nights(rooms: int, days: int = 365) -> int:
    return rooms * days


def rooms_sold(rooms: int, occupancy: float, days: int = 365) -> float:
    return rooms * days * occupancy


def room_revenue(rooms: int, occupancy: float, adr: float, days: int = 365) -> float:
    """Rooms x days x occupancy x ADR."""
    return rooms * days * occupancy * adr


def revpar(occupancy: float, adr: float) -> float:
    """RevPAR = occupancy x ADR = room revenue / available room-nights."""
    return occupancy * adr


def adr_from(room_rev: float, sold: float) -> float:
    return room_rev / sold


def occupancy_from(sold: float, available: float) -> float:
    return sold / available


def indices(subject_occ: float, subject_adr: float, comp_occ: float, comp_adr: float) -> dict:
    """STR-style penetration indices (100 = fair share).

    MPI = occ / comp occ; ARI = ADR / comp ADR; RGI = RevPAR / comp RevPAR = MPI*ARI/100.
    """
    mpi = 100 * subject_occ / comp_occ
    ari = 100 * subject_adr / comp_adr
    rgi = 100 * (subject_occ * subject_adr) / (comp_occ * comp_adr)
    return {"mpi": mpi, "ari": ari, "rgi": rgi}


def operating_statement(rooms: int, occupancy: float, adr: float, *, days: int = 365,
                        other_revenue_pct_of_rooms: float = 0.0,
                        rooms_expense_per_occupied_room: float = 0.0,
                        other_dept_expense_ratio: float = 0.0,
                        undistributed_fixed: float = 0.0,
                        undistributed_pct_of_revenue: float = 0.0,
                        mgmt_fee_pct: float = 0.0,
                        franchise_fee_pct_of_rooms: float = 0.0,
                        property_tax: float = 0.0, insurance: float = 0.0,
                        ffe_reserve_pct: float = 0.04) -> dict:
    """Simplified USALI-style P&L for a limited- or select-service hotel.

    Revenue: rooms + other (as % of rooms revenue).
    Departmental expenses: rooms cost per occupied room (CPOR) + other dept ratio.
    Undistributed: fixed dollar amount + % of total revenue (A&G, S&M, POM, utilities).
    Fees: management (% total revenue), franchise (% rooms revenue: royalty,
    marketing/reservation, loyalty combined).
    Fixed charges: property tax, insurance.
    """
    sold = rooms_sold(rooms, occupancy, days)
    rooms_rev = sold * adr
    other_rev = rooms_rev * other_revenue_pct_of_rooms
    total_rev = rooms_rev + other_rev
    rooms_exp = sold * rooms_expense_per_occupied_room
    other_exp = other_rev * other_dept_expense_ratio
    dept_profit = total_rev - rooms_exp - other_exp
    undistributed = undistributed_fixed + undistributed_pct_of_revenue * total_rev
    gop = dept_profit - undistributed
    mgmt = mgmt_fee_pct * total_rev
    franchise = franchise_fee_pct_of_rooms * rooms_rev
    ebitda = gop - mgmt - franchise - property_tax - insurance
    reserve = ffe_reserve_pct * total_rev
    noi = ebitda - reserve
    avail = rooms * days
    return {
        "rooms_sold": sold, "rooms_revenue": rooms_rev, "other_revenue": other_rev,
        "total_revenue": total_rev, "rooms_expense": rooms_exp, "other_dept_expense": other_exp,
        "departmental_profit": dept_profit, "undistributed": undistributed, "gop": gop,
        "gop_margin": gop / total_rev, "mgmt_fee": mgmt, "franchise_fee": franchise,
        "property_tax": property_tax, "insurance": insurance, "ebitda": ebitda,
        "ffe_reserve": reserve, "noi": noi, "noi_margin": noi / total_rev,
        "revpar": rooms_rev / avail, "trevpar": total_rev / avail, "goppar": gop / avail,
        "noi_per_key": noi / rooms,
    }


def flow_through(delta_profit: float, delta_revenue: float) -> float:
    """Incremental profit / incremental revenue (e.g., GOP flow-through)."""
    return delta_profit / delta_revenue


def breakeven_occupancy(rooms: int, adr: float, fixed_costs: float, debt_service: float,
                        variable_cost_per_occupied_room: float,
                        variable_pct_of_revenue: float, days: int = 365,
                        other_revenue_pct_of_rooms: float = 0.0) -> float:
    """Occupancy at which cash flow after debt service is zero.

    Contribution per occupied room = ADR (1 + o)(1 - v_pct) - CPOR
    Break-even sold = (fixed + debt service) / contribution
    ``variable_pct_of_revenue`` captures fees, reserve and other %-of-revenue costs.
    """
    contrib = adr * (1 + other_revenue_pct_of_rooms) * (1 - variable_pct_of_revenue) - variable_cost_per_occupied_room
    sold = (fixed_costs + debt_service) / contrib
    return sold / (rooms * days)


def pip_adjusted_price(as_stabilized_value: float, pip_cost: float, displacement_noi_loss: float,
                       carry_and_soft_costs: float, contingency_pct: float = 0.10,
                       required_profit_on_pip_pct: float = 0.0) -> dict:
    """Price a buyer can pay today for an asset requiring a PIP.

    Price = stabilized value - PIP x (1 + contingency) - lost NOI during renovation
            - carry/soft costs - required profit on the PIP capital.
    The 'required profit' term reflects that renovation capital is risk capital and
    must earn a return; omitting it means the buyer does the PIP for free.
    """
    pip_all_in = pip_cost * (1 + contingency_pct)
    profit = pip_all_in * required_profit_on_pip_pct
    price = as_stabilized_value - pip_all_in - displacement_noi_loss - carry_and_soft_costs - profit
    return {"pip_all_in": pip_all_in, "required_profit": profit, "price": price}
