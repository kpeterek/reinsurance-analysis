"""Dynamics helpers for Chapter 3 (mental models made computable).

Covers: risk-matched hurdle rates, reflexive collateral loops, AR(1) mean
reversion, two-state Markov regimes, the binomial option to wait, forced sales
under a leverage cap with linear price impact, exit capacity for crowded trades,
time-series momentum sizing, and sequential Bayesian updating.

Conventions follow the package: rates and returns in decimals, money in any
consistent unit, time steps stated in each docstring. Every function is pure.
"""

from __future__ import annotations

import math
from typing import Sequence

from . import stats

# --------------------------------------------------------------------------
# Opportunity cost
# --------------------------------------------------------------------------


def risk_matched_hurdle(alt_return: float, borrow_rate: float, sigma_deal: float,
                        sigma_alt: float) -> float:
    """Return the next-best alternative earns when levered (or de-levered) to the deal's risk.

    h = r_B + (sigma_deal / sigma_alt) * (alt_return - r_B)

    ``borrow_rate`` is the rate at which the alternative can be levered (or the
    rate earned on cash if the ratio is below one). Annual decimals.
    Excel: =rB + (sd_deal/sd_alt)*(r_alt - rB)
    """
    if sigma_alt <= 0:
        raise ValueError("sigma_alt must be positive")
    return borrow_rate + sigma_deal / sigma_alt * (alt_return - borrow_rate)


# --------------------------------------------------------------------------
# Reflexive collateral loop
# --------------------------------------------------------------------------


def reflexive_loop_gain(ltv: float, draw_fraction: float, collateral_value: float,
                        impact_per_unit: float) -> float:
    """Loop gain m of the chain price -> collateral -> credit -> demand -> price.

    A fractional price change x raises pledged collateral by x * C, lending
    capacity by ltv * x * C, and spending by draw_fraction * ltv * x * C. Each
    unit of spending moves the price by ``impact_per_unit`` (fractional change
    per unit of money, same unit as C). So the next-round price change is m * x
    with m = ltv * draw_fraction * C * impact_per_unit. Stable iff |m| < 1.
    """
    return ltv * draw_fraction * collateral_value * impact_per_unit


def reflexive_path(initial_shock: float, gain: float, rounds: int) -> dict:
    """Round-by-round increments x_k = shock * m^k and the cumulative sum.

    Returns increments, cumulative after ``rounds`` rounds (k = 0..rounds-1),
    and the infinite-round total shock / (1 - m) when |m| < 1 (else ``inf``).
    Increments are additive fractional changes (a linear approximation).
    """
    inc = [initial_shock * gain ** k for k in range(rounds)]
    total = initial_shock / (1 - gain) if abs(gain) < 1 else math.inf
    return {"increments": inc, "cumulative": sum(inc), "total": total,
            "multiplier": (1 / (1 - gain)) if abs(gain) < 1 else math.inf}


# --------------------------------------------------------------------------
# Mean reversion
# --------------------------------------------------------------------------


def ar1_half_life(phi: float) -> float:
    """Half-life (in periods) of a deviation under x_t - mu = phi (x_{t-1} - mu).

    h = ln(0.5) / ln(phi), defined for 0 < phi < 1.
    """
    if not 0 < phi < 1:
        raise ValueError("half-life defined only for 0 < phi < 1")
    return math.log(0.5) / math.log(phi)


def ar1_forecast(x0: float, mu: float, phi: float, horizon: int) -> float:
    """E[x_{t+h} | x_t = x0] = mu + phi^h (x0 - mu)."""
    return mu + phi ** horizon * (x0 - mu)


def ar1_rescale(phi: float, periods: float) -> float:
    """Persistence over ``periods`` base periods: phi^periods (e.g. quarterly to annual: 4)."""
    return phi ** periods


def ar1_phi_ols(x: Sequence[float]) -> dict:
    """OLS of x_t on x_{t-1}: returns intercept a, slope phi, implied mean a/(1-phi)."""
    fit = stats.ols(list(x[:-1]), list(x[1:]))
    phi = fit["b"]
    return {"a": fit["a"], "phi": phi, "mu": fit["a"] / (1 - phi), "se_phi": fit["se_b"]}


# --------------------------------------------------------------------------
# Two-state Markov regimes
# --------------------------------------------------------------------------


def markov_expected_duration(p_stay: float) -> float:
    """Expected number of periods spent in a regime once entered: 1 / (1 - p_stay)."""
    return 1.0 / (1.0 - p_stay)


def markov2_stationary(p11: float, p22: float) -> tuple[float, float]:
    """Long-run probabilities (pi1, pi2) of a two-state chain with stay probabilities p11, p22."""
    a, b = 1 - p11, 1 - p22
    return b / (a + b), a / (a + b)


def markov2_nstep(p11: float, p22: float, n: int) -> list[list[float]]:
    """n-step transition matrix P^n by repeated multiplication. Rows: from-state."""
    P = [[p11, 1 - p11], [1 - p22, p22]]
    M = [[1.0, 0.0], [0.0, 1.0]]
    for _ in range(n):
        M = [[sum(M[i][k] * P[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    return M


# --------------------------------------------------------------------------
# Option to wait (one-period binomial)
# --------------------------------------------------------------------------


def binomial_wait(v0: float, cost_now: float, up: float, down: float, rf: float,
                  payout_yield: float, cost_growth: float = 0.0) -> dict:
    """Value of building now versus holding a one-year option to build.

    The completed asset is worth v0 today and v0*up or v0*down in one year. Its
    owner receives a cash payout of payout_yield * v0 during the year (forgone by
    a waiter). Construction costs cost_now today or cost_now*(1+cost_growth) in
    one year. Risk-neutral probability q solves
    v0 = [payout + q v_u + (1-q) v_d] / (1+rf).
    Returns q, npv_now, payoffs, wait value, option premium, and replicating
    portfolio (delta units of the asset, bond B) as an independent check.
    """
    vu, vd = v0 * up, v0 * down
    pay = payout_yield * v0
    q = (v0 * (1 + rf) - pay - vd) / (vu - vd)
    if not 0 < q < 1:
        raise ValueError("no-arbitrage requires 0 < q < 1")
    cost1 = cost_now * (1 + cost_growth)
    fu, fd = max(vu - cost1, 0.0), max(vd - cost1, 0.0)
    wait = (q * fu + (1 - q) * fd) / (1 + rf)
    npv_now = v0 - cost_now
    delta = (fu - fd) / (vu - vd)
    bond = (fd - delta * (vd + pay)) / (1 + rf)
    return {"q": q, "vu": vu, "vd": vd, "payout": pay, "cost1": cost1, "fu": fu, "fd": fd,
            "npv_now": npv_now, "wait_value": wait, "option_premium": wait - max(npv_now, 0.0),
            "delta": delta, "bond": bond, "replication_value": delta * v0 + bond,
            "decision": "wait" if wait > npv_now else "build"}


# --------------------------------------------------------------------------
# Forced selling under a leverage cap with linear impact
# --------------------------------------------------------------------------


def forced_sale(q0: float, debt: float, price: float, max_ltv: float, impact: float = 0.0) -> dict:
    """Units that must be sold so that LTV returns to ``max_ltv``.

    Sale proceeds repay debt. All units (sold and retained) are marked at the
    post-sale price p(s) = price - impact * s (uniform-price simplification).
    Condition: debt - s p(s) = max_ltv (q0 - s) p(s), i.e.
    p(s) [max_ltv q0 + (1 - max_ltv) s] = debt.
    Returns the smallest feasible s, the post-sale price, equity, and the
    critical impact above which selling cannot restore compliance at the margin.
    If no s in [0, q0] works, ``feasible`` is False (full liquidation spiral).
    """
    lam = max_ltv
    crit = (1 - lam) * price / (lam * q0)
    if debt <= lam * q0 * price:
        return {"feasible": True, "units": 0.0, "price": price, "equity": q0 * price - debt,
                "critical_impact": crit}
    if impact == 0:
        s = (debt / price - lam * q0) / (1 - lam)
    else:
        # -impact(1-lam) s^2 + [(1-lam) price - impact lam q0] s + lam q0 price - debt = 0
        a = -impact * (1 - lam)
        b = (1 - lam) * price - impact * lam * q0
        c = lam * q0 * price - debt
        disc = b * b - 4 * a * c
        if disc < 0:
            return {"feasible": False, "units": q0, "price": price - impact * q0,
                    "equity": q0 * (price - impact * q0) - debt, "critical_impact": crit}
        roots = [(-b + sg * math.sqrt(disc)) / (2 * a) for sg in (1, -1)]
        roots = [r for r in roots if 0 <= r <= q0]
        if not roots:
            return {"feasible": False, "units": q0, "price": price - impact * q0,
                    "equity": q0 * (price - impact * q0) - debt, "critical_impact": crit}
        s = min(roots)
    p = price - impact * s
    return {"feasible": True, "units": s, "price": p, "equity": q0 * p - debt,
            "critical_impact": crit}


# --------------------------------------------------------------------------
# Crowded trades
# --------------------------------------------------------------------------


def days_to_exit(position: float, adv: float, participation: float) -> float:
    """Trading days to liquidate at a participation rate of average daily volume."""
    return position / (participation * adv)


def max_position(adv: float, participation: float, days: float) -> float:
    """Largest position that can be exited within ``days`` at the participation rate."""
    return adv * participation * days


# --------------------------------------------------------------------------
# Time-series momentum sizing
# --------------------------------------------------------------------------


def tsmom_position(monthly_returns: Sequence[float], ann_vol: float, target_vol: float) -> dict:
    """Sign of the trailing compounded return times a volatility-scaled weight.

    Signal = sign(prod(1+r) - 1) over the supplied window (typically 12 months).
    Weight = target_vol / ann_vol (leverage multiple of notional per unit capital).
    """
    g = 1.0
    for r in monthly_returns:
        g *= 1 + r
    trailing = g - 1
    sign = 1 if trailing > 0 else (-1 if trailing < 0 else 0)
    return {"trailing": trailing, "signal": sign, "weight": sign * target_vol / ann_vol}


# --------------------------------------------------------------------------
# Bayesian updating
# --------------------------------------------------------------------------


def bayes_sequence(prior: float, likelihood_ratios: Sequence[float], weight: float = 1.0) -> list[float]:
    """Posterior after each likelihood ratio in turn (odds form).

    ``weight`` scales each log-likelihood ratio: 1 is Bayesian, < 1 models
    under-reaction (conservatism), > 1 models over-reaction.
    Assumes the signals are conditionally independent given the hypothesis.
    """
    out, p = [], prior
    for lr in likelihood_ratios:
        p = stats.likelihood_ratio_update(p, lr ** weight)
        out.append(p)
    return out
