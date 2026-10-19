"""Real options for real estate: binomial trees for the option to wait, develop, or abandon.

Added for Chapter 13 (CRE Trading and Portfolio Strategy) and Case I (Development
Land Option). Conventions follow the rest of ``sdesk``:

* Rates are decimals, annual, compounded once per tree step unless stated.
* The underlying ``V`` is the market value of the *completed, stabilized*
  building (or any income-producing asset) at the decision date.
* The underlying pays a cash yield ``delta`` per step: holding the completed
  asset from one node to the next earns ``delta * V`` at the end of the step,
  measured on the value at the start of the step. ``delta`` is the NOI yield
  (cap rate) that an owner of the finished building collects and that the
  holder of an unexercised development option forgoes.
* Exercise ("build") costs ``K`` at the node where it is chosen and delivers
  ``V`` at that node. Construction time is ignored unless the caller folds it
  into ``V`` and ``K`` (for example by valuing the delivered building at the
  start date and the cost at its present value).

Risk-neutral probability with a cash yield (one step of length 1 period):
    q (u V) + (1 - q)(d V) + delta V = (1 + r) V
    =>  q = (1 + r - delta - d) / (u - d)
It must lie in (0, 1); otherwise the tree admits arbitrage and is rejected.

Excel equivalent of one step: =MAX(V-K, (q*Vu_opt + (1-q)*Vd_opt)/(1+r)).

A real-world decision tree (probability ``p`` and a risk-adjusted discount rate)
is also provided, because practitioners use it. Section 13.4 explains why it
misprices options: the option is riskier than the asset, so one discount rate
cannot be right for both.
"""

from __future__ import annotations

import math
from typing import Callable, Sequence


def crr_factors(sigma: float, dt: float = 1.0) -> tuple[float, float]:
    """Cox-Ross-Rubinstein up and down factors: u = exp(sigma sqrt(dt)), d = 1/u."""
    u = math.exp(sigma * math.sqrt(dt))
    return u, 1.0 / u


def risk_neutral_prob(u: float, d: float, r: float, delta: float = 0.0) -> float:
    """q = (1 + r - delta - d)/(u - d) for an underlying paying cash yield ``delta`` per step.

    ``r`` and ``delta`` are per-step simple rates (annual rates when steps are one year).
    Raises ValueError when q is outside (0, 1).
    """
    if u <= d:
        raise ValueError("u must exceed d")
    q = (1.0 + r - delta - d) / (u - d)
    if not 0.0 < q < 1.0:
        raise ValueError(f"risk-neutral probability {q:.4f} outside (0,1): tree admits arbitrage")
    return q


def value_lattice(v0: float, u: float, d: float, steps: int) -> list[list[float]]:
    """Recombining lattice. lattice[t][j] = v0 * u**j * d**(t-j), j = number of up moves."""
    return [[v0 * u ** j * d ** (t - j) for j in range(t + 1)] for t in range(steps + 1)]


def american_real_option(v0: float, u: float, d: float, r: float, steps: int,
                         exercise_value: Callable[[float, int], float],
                         delta: float = 0.0, q: float | None = None) -> dict:
    """Value an option that may be exercised at any node up to ``steps``.

    ``exercise_value(V, t)`` returns the payoff from exercising at a node with
    underlying V at step t (e.g. ``lambda V, t: V - K * (1 + gk) ** t`` for a
    development option whose cost grows at gk). Unexercised at expiry = 0.
    ``q`` may be supplied (e.g. a real-world probability with a risk-adjusted
    ``r``); otherwise the risk-neutral q with cash yield ``delta`` is used.

    Returns the option value at t=0, the immediate exercise value, the value of
    waiting (option value minus max(immediate, 0)), the full lattices, and the
    exercise map (True where exercising is optimal and strictly positive).
    """
    if q is None:
        q = risk_neutral_prob(u, d, r, delta)
    lat = value_lattice(v0, u, d, steps)
    opt = [[0.0] * (t + 1) for t in range(steps + 1)]
    ex = [[False] * (t + 1) for t in range(steps + 1)]
    for j in range(steps + 1):
        e = exercise_value(lat[steps][j], steps)
        opt[steps][j] = max(e, 0.0)
        ex[steps][j] = e > 0.0
    for t in range(steps - 1, -1, -1):
        for j in range(t + 1):
            cont = (q * opt[t + 1][j + 1] + (1.0 - q) * opt[t + 1][j]) / (1.0 + r)
            e = exercise_value(lat[t][j], t)
            if e > cont and e > 0.0:
                opt[t][j], ex[t][j] = e, True
            else:
                opt[t][j] = cont
    immediate = exercise_value(v0, 0)
    return {"option_value": opt[0][0], "immediate": immediate,
            "value_of_waiting": opt[0][0] - max(immediate, 0.0),
            "exercise_now": ex[0][0], "q": q, "lattice": lat, "option": opt, "exercise": ex}


def european_real_option(v0: float, u: float, d: float, r: float, steps: int,
                         payoff: Callable[[float], float], delta: float = 0.0,
                         q: float | None = None) -> float:
    """Value of a claim exercisable only at ``steps`` (binomial expectation, discounted)."""
    if q is None:
        q = risk_neutral_prob(u, d, r, delta)
    total = 0.0
    for j in range(steps + 1):
        prob = math.comb(steps, j) * q ** j * (1.0 - q) ** (steps - j)
        total += prob * max(payoff(v0 * u ** j * d ** (steps - j)), 0.0)
    return total / (1.0 + r) ** steps


def decision_tree_ev(payoffs: Sequence[float], probs: Sequence[float], discount_rate: float,
                     t: float = 1.0) -> float:
    """Real-world expected payoff at time t discounted at one risk-adjusted rate."""
    if abs(sum(probs) - 1.0) > 1e-9:
        raise ValueError("probabilities must sum to 1")
    return sum(p * x for p, x in zip(probs, payoffs)) / (1.0 + discount_rate) ** t


def perpetual_option_threshold(r: float, delta: float, sigma: float) -> dict:
    """McDonald-Siegel / Dixit-Pindyck perpetual investment option (continuous time).

    Invest when V / K >= beta / (beta - 1), where beta > 1 solves
    0.5 sigma^2 b(b-1) + (r - delta) b - r = 0. ``r`` and ``delta`` are
    continuously compounded. Returns beta and the hurdle multiple.
    Requires delta > 0 (otherwise waiting forever is optimal).
    """
    if delta <= 0:
        raise ValueError("delta must be positive for a finite threshold")
    a = (r - delta) / sigma ** 2
    beta = 0.5 - a + math.sqrt((a - 0.5) ** 2 + 2.0 * r / sigma ** 2)
    return {"beta": beta, "hurdle_multiple": beta / (beta - 1.0)}
