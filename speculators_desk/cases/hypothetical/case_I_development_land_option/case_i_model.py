"""Case I — The Development Land Option. Reproducible model.

Run:  python3 cases/hypothetical/case_I_development_land_option/case_i_model.py
All inputs are hypothetical [HYPOTHESIS]. Every number quoted in case_I.md and
case_I_rubric.md is produced here and asserted in tests/test_case_i.py.

Conventions
* Money in dollars. Rates are annual decimals. One binomial step = one year.
* GDV = gross development value = stabilized NOI / cap rate, valued at the
  decision date (construction time is folded into the financing-cost line, as
  in a standard residual land valuation; see cre.residual_land_value).
* The completed-value underlying pays a cash yield equal to the cap rate: the
  NOI an owner of the finished building collects and a landholder forgoes.
* Entitlement approval is idiosyncratic and is weighted with its real-world
  probability inside the risk-neutral market tree.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "models" / "python"))

from sdesk import cre, tvm  # noqa: E402
from sdesk import x_options_real as ro  # noqa: E402

# ----------------------------------------------------------------- inputs
ACRES = 12
OWNER_COST_2009 = 900_000          # the family's original price (an anchor, not a value)

NOI_PER_UNIT = 16_500              # stabilized NOI after reserves, today's rents
CAP = 0.055                        # stabilized cap rate; also the cash yield delta
SELL_COMPLETED = 0.02              # selling costs on the completed project (in GDV net)
MARGIN = 0.15                      # developer margin on total cost
SOFT_PCT = 0.12                    # soft costs as % of hard costs
FIN_PCT = 0.06                     # construction financing as % of hard + soft

SCHEMES = {                        # units, hard cost per unit
    "by_right_240": (240, 195_000),
    "pd_330": (330, 192_000),
}

COST_GROWTH = 0.04                 # escalation of all non-land costs per year
U, D = 1.20, 1 / 1.20              # one-year moves in completed value
R = 0.045                          # risk-free rate
CARRY = 60_000                     # land carry per year (tax, insurance, upkeep), paid at year-end
FLOOR = 1_500_000                  # alternative-use land value at t=1 (pad / storage buyer)
LAND_SALE_COST = 0.03

BID_NOW = 5_400_000                # merchant builder's cash bid for the by-right site today
FEE_DEV_PCT = 0.03                 # fee developer cost if the family builds (on hard costs)

ENTITLE_COST = 450_000             # spent today
P_APPROVE = 0.60                   # real-world approval probability (idiosyncratic)

# Joint venture: land contributed at an agreed value; developer funds the rest of equity
JV_LAND_CREDIT = 6_000_000
JV_LTC = 0.60
JV_PREF = 0.08
JV_SPLITS = [1.0, 0.70]            # investors (both partners pro rata) 100% to 8% IRR, then 70/30
JV_SCEN = [(0.25, 0.85), (0.50, 1.00), (0.25, 1.15)]  # (prob, completed-value multiple at t=2)
JV_DISCOUNT = 0.12                 # owner's required return on a development-equity interest


# ----------------------------------------------------------------- helpers
def gdv(units: int, value_multiple: float = 1.0) -> float:
    return units * NOI_PER_UNIT / CAP * value_multiple


def non_land_costs(scheme: str, years: int = 0) -> dict:
    units, hard_pu = SCHEMES[scheme]
    g = (1 + COST_GROWTH) ** years
    hard = units * hard_pu * g
    soft = SOFT_PCT * hard
    fin = FIN_PCT * (hard + soft)
    return {"hard": hard, "soft": soft, "fin": fin, "total": hard + soft + fin}


def rlv(scheme: str, value_multiple: float = 1.0, years: int = 0) -> dict:
    units, _ = SCHEMES[scheme]
    c = non_land_costs(scheme, years)
    out = cre.residual_land_value(gdv(units, value_multiple), c["hard"], c["soft"], c["fin"],
                                  MARGIN, SELL_COMPLETED)
    out.update(gdv=gdv(units, value_multiple), **{k: v for k, v in c.items() if k != "total"})
    return out


def q_neutral(u: float = U, d: float = D) -> float:
    return ro.risk_neutral_prob(u, d, R, CAP)


# ----------------------------------------------------------------- strategies
def sell_now() -> dict:
    net = BID_NOW * (1 - LAND_SALE_COST)
    return {"gross": BID_NOW, "net": net, "pv": net}


def build_now() -> dict:
    r0 = rlv("by_right_240")
    fee = FEE_DEV_PCT * r0["hard"]
    return {"rlv": r0["land_value"], "fee": fee, "pv": r0["land_value"] - fee}


def _land_t1(scheme: str, mult: float) -> float:
    return max(rlv(scheme, mult, years=1)["land_value"], FLOOR)


def wait_one_year(u: float = U, d: float = D) -> dict:
    """Hold the by-right site one year, then sell at max(RLV, floor) less sale costs."""
    q = q_neutral(u, d)
    up, dn = _land_t1("by_right_240", u), _land_t1("by_right_240", d)
    rlv_up = rlv("by_right_240", u, 1)["land_value"]
    rlv_dn = rlv("by_right_240", d, 1)["land_value"]
    ev = q * up + (1 - q) * dn
    pv = (ev * (1 - LAND_SALE_COST) - CARRY) / (1 + R)
    return {"q": q, "rlv_up": rlv_up, "rlv_down": rlv_dn, "land_up": up, "land_down": dn,
            "pv": pv}


def entitle_and_sell(u: float = U, d: float = D, p: float = P_APPROVE) -> dict:
    q = q_neutral(u, d)
    def node(mult):
        approved = max(rlv("pd_330", mult, 1)["land_value"], rlv("by_right_240", mult, 1)["land_value"], FLOOR)
        denied = _land_t1("by_right_240", mult)
        return approved, denied, p * approved + (1 - p) * denied
    au, du, eu = node(u)
    ad, dd, ed = node(d)
    ev = q * eu + (1 - q) * ed
    pv = (ev * (1 - LAND_SALE_COST) - CARRY) / (1 + R) - ENTITLE_COST
    return {"approved_up": au, "denied_up": du, "approved_down": ad, "denied_down": dd,
            "node_up": eu, "node_down": ed, "pv": pv,
            "rlv330_up": rlv("pd_330", u, 1)["land_value"], "rlv330_down": rlv("pd_330", d, 1)["land_value"]}


def entitlement_breakeven_p(u: float = U, d: float = D) -> float:
    """Approval probability at which entitling equals waiting without entitling."""
    target = wait_one_year(u, d)["pv"]
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if entitle_and_sell(u, d, mid)["pv"] > target:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def jv() -> dict:
    c = non_land_costs("by_right_240")
    total = JV_LAND_CREDIT + c["total"]
    loan = JV_LTC * total
    equity = total - loan
    owner_share = JV_LAND_CREDIT / equity
    rows = []
    e_owner = 0.0
    for p, m in JV_SCEN:
        proceeds = gdv(240, m) * (1 - SELL_COMPLETED) - loan
        wf = cre.irr_hurdle_waterfall([-equity, 0.0, max(proceeds, 0.0)], [JV_PREF], JV_SPLITS)
        inv = wf["investor"][2]
        owner = owner_share * inv
        e_owner += p * owner
        rows.append({"p": p, "mult": m, "proceeds": proceeds, "investors": inv,
                     "promote": wf["promote"][2], "owner": owner,
                     "project_irr": tvm.irr([-equity, 0.0, proceeds]) if proceeds > 0 else -1.0})
    pv = e_owner / (1 + JV_DISCOUNT) ** 2
    return {"total_cost": total, "loan": loan, "equity": equity, "owner_share": owner_share,
            "developer_cash": equity - JV_LAND_CREDIT, "rows": rows, "e_owner_t2": e_owner, "pv": pv,
            "owner_irr_on_credit": (e_owner / JV_LAND_CREDIT) ** 0.5 - 1}


def uncertainty_table(ups=(1.10, 1.20, 1.30)) -> list[dict]:
    out = []
    b = build_now()["rlv"]
    for u in ups:
        w = wait_one_year(u, 1 / u)
        e = entitle_and_sell(u, 1 / u)
        out.append({"u": u, "wait": w["pv"], "entitle": e["pv"],
                    "value_of_waiting": w["pv"] - b * (1 - LAND_SALE_COST)})
    return out


def naive_wait(p_up: float = 0.5, k: float = 0.10) -> float:
    """The common shortcut: real-world 50/50 tree discounted at a 'land' rate. Not risk-neutral."""
    w = wait_one_year()
    ev = ro.decision_tree_ev([w["land_up"], w["land_down"]], [p_up, 1 - p_up], 0.0)
    return (ev * (1 - LAND_SALE_COST) - CARRY) / (1 + k)


def summary() -> dict:
    return {"sell_now": sell_now()["pv"], "build_now": build_now()["pv"], "wait": wait_one_year()["pv"],
            "entitle": entitle_and_sell()["pv"], "jv": jv()["pv"]}


if __name__ == "__main__":
    for s in SCHEMES:
        r0 = rlv(s)
        print(s, {k: round(v) for k, v in r0.items()})
    print("q", round(q_neutral(), 4))
    print("sell", sell_now())
    print("build", build_now())
    print("wait", wait_one_year())
    print("entitle", entitle_and_sell())
    print("breakeven p", entitlement_breakeven_p())
    j = jv()
    print("jv", {k: v for k, v in j.items() if k != "rows"})
    for row in j["rows"]:
        print(row)
    print(uncertainty_table())
    print("naive", naive_wait())
    print(summary())
