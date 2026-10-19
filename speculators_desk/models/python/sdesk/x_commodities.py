"""Commodity-futures helpers used in Chapter 16 (Commodities).

Extends ``sdesk.markets`` (``futures_pnl``, ``futures_notional``,
``futures_fair_value``) without duplicating it. Conventions:

* Rates are decimals with CONTINUOUS compounding unless a docstring says
  otherwise: r = financing rate, u = storage cost as a proportional yield,
  y = convenience yield. Time t is in years.
* Futures prices are in the exchange's quotation unit. Corn (CBOT ZC) is quoted
  in CENTS per bushel; every other contract in ``CONTRACT_SPECS`` is quoted in
  dollars per unit. ``contract_pnl`` converts quotation units to dollars, so a
  corn move of 16.25 (cents) is $0.1625 per bushel, not $16.25.
* Sign convention: side = +1 long, -1 short, as in ``markets.futures_pnl``.
* The roll decomposition holds the nearby (one-period) contract each period,
  fully collateralized with bills: the futures position's notional F_t is
  invested at the bill rate, and the contract converges to spot at expiry.

Contract specifications (CME Group / NYMEX / COMEX / CBOT standard contracts;
checked 2026-10-19 via search excerpts of CME contract-spec pages and rulebook
chapters; see references/sources_ch16.md):

=====  =======================  ====================  ==========================
Code   Contract                 Unit (multiplier)     Quotation
=====  =======================  ====================  ==========================
CL     NYMEX WTI light sweet    1,000 barrels         $ per barrel
NG     NYMEX Henry Hub gas      10,000 MMBtu          $ per MMBtu
GC     COMEX gold               100 troy ounces       $ per troy ounce
SI     COMEX silver             5,000 troy ounces     $ per troy ounce
HG     COMEX copper             25,000 pounds         $ per pound
ZC     CBOT corn                5,000 bushels         cents per bushel
=====  =======================  ====================  ==========================
"""

from __future__ import annotations

import math
from typing import Sequence

from . import markets

# multiplier: units per contract; quote_to_usd: dollars per one quotation unit
CONTRACT_SPECS = {
    "CL": {"name": "NYMEX WTI crude oil", "multiplier": 1_000, "unit": "barrel", "quote_to_usd": 1.0},
    "NG": {"name": "NYMEX Henry Hub natural gas", "multiplier": 10_000, "unit": "MMBtu", "quote_to_usd": 1.0},
    "GC": {"name": "COMEX gold", "multiplier": 100, "unit": "troy ounce", "quote_to_usd": 1.0},
    "SI": {"name": "COMEX silver", "multiplier": 5_000, "unit": "troy ounce", "quote_to_usd": 1.0},
    "HG": {"name": "COMEX copper", "multiplier": 25_000, "unit": "pound", "quote_to_usd": 1.0},
    "ZC": {"name": "CBOT corn", "multiplier": 5_000, "unit": "bushel", "quote_to_usd": 0.01},
}


def dollar_multiplier(code: str) -> float:
    """Dollars of P&L per 1.0 quotation-unit move per contract (corn: 5,000 x $0.01 = $50)."""
    s = CONTRACT_SPECS[code]
    return s["multiplier"] * s["quote_to_usd"]


def contract_pnl(code: str, entry: float, exit_: float, contracts: int, side: int = 1) -> float:
    """P&L in dollars = side x (exit - entry) x multiplier x quote_to_usd x contracts."""
    return markets.futures_pnl(entry, exit_, contracts, dollar_multiplier(code), side)


def contract_notional(code: str, price: float, contracts: int = 1) -> float:
    """Dollar notional = price x multiplier x quote_to_usd x contracts."""
    return markets.futures_notional(price, dollar_multiplier(code), contracts)


# --------------------------------------------------------------------------
# Cost of carry
# --------------------------------------------------------------------------

def storage_yield_from_dollars(spot: float, r: float, t: float, storage_fv: float) -> float:
    """Convert a dollar storage cost paid at T (per unit) to a continuous yield u.

    Solves S e^{(r+u)t} = S e^{rt} + U_T, so u = ln(1 + U_T / (S e^{rt})) / t.
    """
    return math.log(1.0 + storage_fv / (spot * math.exp(r * t))) / t


def full_carry_forward(spot: float, r: float, t: float, storage_fv: float = 0.0, u: float = 0.0) -> float:
    """Upper no-arbitrage bound (cash-and-carry): F* = S e^{(r+u)t} + U_T.

    ``storage_fv`` is a dollar storage cost per unit paid at T; ``u`` a proportional yield.
    """
    return spot * math.exp((r + u) * t) + storage_fv


def implied_convenience_yield(spot: float, futures: float, r: float, t: float,
                              storage_fv: float = 0.0, u: float = 0.0) -> float:
    """Implied convenience yield y solving F = S e^{(r + u_total - y) t}.

    u_total = u + the yield equivalent of ``storage_fv``. Equivalently
    y = ln(F*/F)/t with F* the full-carry forward.
    """
    u_total = u + (storage_yield_from_dollars(spot, r, t, storage_fv) if storage_fv else 0.0)
    return r + u_total - math.log(futures / spot) / t


def annualized_slope(f_near: float, f_far: float, dt: float) -> float:
    """Annualized log slope of the curve: ln(F_far / F_near) / dt. Positive = contango."""
    return math.log(f_far / f_near) / dt


def carry_slope(r: float, u: float, y: float) -> float:
    """Theory-of-storage slope (annualized, continuous): r + u - y."""
    return r + u - y


def convenience_yield_inventory(cover_ratio: float, theta: float) -> float:
    """Illustrative Working curve: y(x) = theta / x, x = inventory / normal inventory.

    A teaching functional form [HYPOTHESIS]; it is convex and falls as inventory rises,
    which is the qualitative shape documented by Gorton, Hayashi and Rouwenhorst (2013).
    """
    return theta / cover_ratio


def storage_cost_fill(fill: float, u0: float, kappa: float) -> float:
    """Illustrative marginal storage cost rising toward tank-tops: u0 + kappa f/(1-f). [HYPOTHESIS]"""
    if not 0 <= fill < 1:
        raise ValueError("fill must be in [0, 1)")
    return u0 + kappa * fill / (1.0 - fill)


# --------------------------------------------------------------------------
# Roll-yield decomposition
# --------------------------------------------------------------------------

def roll_decomposition(spots: Sequence[float], futures: Sequence[float],
                       bill_rates: Sequence[float]) -> dict:
    """Return decomposition for a fully collateralized, rolling nearby position.

    Period t (t = 0..n-1): buy the contract expiring at t+1 at ``futures[t]``; it
    converges to ``spots[t+1]``. Collateral F_t earns ``bill_rates[t]`` (per-period,
    simple). Per-period total return, exactly additive:

        R_t = i_t + (S_{t+1} - S_t)/F_t + (S_t - F_t)/F_t
            = collateral + spot component + roll component.

    ``spots`` has n+1 entries, ``futures`` and ``bill_rates`` n entries.
    Also returns the compounded total and excess returns and the log split
    sum ln(S_{t+1}/F_t) = ln(S_n/S_0) + sum ln(S_t/F_t).
    """
    n = len(futures)
    if len(spots) != n + 1 or len(bill_rates) != n:
        raise ValueError("need len(spots) = len(futures) + 1 = len(bill_rates) + 1")
    rows = []
    tot = exc = 1.0
    for t in range(n):
        s0, s1, f, i = spots[t], spots[t + 1], futures[t], bill_rates[t]
        spot_c = (s1 - s0) / f
        roll_c = (s0 - f) / f
        rows.append({"collateral": i, "spot": spot_c, "roll": roll_c,
                     "excess": spot_c + roll_c, "total": i + spot_c + roll_c})
        tot *= 1 + i + spot_c + roll_c
        exc *= 1 + spot_c + roll_c
    log_roll = sum(math.log(spots[t] / futures[t]) for t in range(n))
    log_spot = math.log(spots[-1] / spots[0])
    return {
        "rows": rows,
        "sum_collateral": sum(r["collateral"] for r in rows),
        "sum_spot": sum(r["spot"] for r in rows),
        "sum_roll": sum(r["roll"] for r in rows),
        "compound_total": tot - 1.0,
        "compound_excess": exc - 1.0,
        "spot_change": spots[-1] / spots[0] - 1.0,
        "log_spot": log_spot,
        "log_roll": log_roll,
        "log_excess": log_spot + log_roll,
    }


# --------------------------------------------------------------------------
# Seasonal storage (natural gas)
# --------------------------------------------------------------------------

def storage_intrinsic_margin(buy: float, sell: float, fuel_loss: float, inj_cost: float,
                             wd_cost: float, capacity_rent: float, finance_rate: float,
                             months: float) -> dict:
    """Intrinsic margin per DELIVERED MMBtu of a buy-summer / sell-winter storage trade.

    To deliver 1 unit you must buy 1/(1 - fuel_loss). Financing is simple interest on the
    purchase cost for ``months``/12 years. Costs are per delivered unit.
    """
    purchase = buy / (1.0 - fuel_loss)
    finance = purchase * finance_rate * months / 12.0
    margin = sell - purchase - inj_cost - wd_cost - capacity_rent - finance
    return {"purchase": purchase, "finance": finance, "margin": margin,
            "raw_spread": sell - buy}


# --------------------------------------------------------------------------
# Oil-to-hotel transmission
# --------------------------------------------------------------------------

def oil_to_revpar(oil_change: float, rig_elasticity: float, energy_share: float,
                  energy_demand_elasticity: float, supply_change: float,
                  occ0: float, adr0: float, adr_elasticity_to_occ: float) -> dict:
    """Chain of proportional (simple %) changes. All elasticities are [HYPOTHESIS].

    rigs = e_rig x oil; energy demand = e_dem x rigs; total demand = share x energy demand;
    occ1 = occ0 (1 + demand)/(1 + supply); ADR change = e_adr x (occ1/occ0 - 1).
    """
    rigs = rig_elasticity * oil_change
    energy_dem = energy_demand_elasticity * rigs
    demand = energy_share * energy_dem
    occ1 = occ0 * (1 + demand) / (1 + supply_change)
    occ_chg = occ1 / occ0 - 1
    adr1 = adr0 * (1 + adr_elasticity_to_occ * occ_chg)
    rp0, rp1 = occ0 * adr0, occ1 * adr1
    return {"rigs": rigs, "energy_demand": energy_dem, "demand": demand, "occ1": occ1,
            "occ_change": occ_chg, "adr1": adr1, "revpar0": rp0, "revpar1": rp1,
            "revpar_change": rp1 / rp0 - 1}


def replacement_cost(land: float, hard: float, soft_pct_of_hard: float) -> float:
    """Replacement cost = land + hard x (1 + soft %)."""
    return land + hard * (1.0 + soft_pct_of_hard)


def hard_cost_shock(hard: float, shares: Sequence[float], price_changes: Sequence[float]) -> float:
    """Dollar change in hard cost = hard x sum(share_i x change_i) (full pass-through)."""
    return hard * sum(s * c for s, c in zip(shares, price_changes))
