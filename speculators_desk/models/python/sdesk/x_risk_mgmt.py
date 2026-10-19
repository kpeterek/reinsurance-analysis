"""Risk-management helpers for Chapter 21 (risk management and position sizing).

Extends ``sdesk.risk`` (which supplies VaR/ES, Kelly fractions, drawdown,
stop-based sizing, portfolio volatility and the fixed-fraction simulator). Nothing
here duplicates that module. Covers:

* volatility- and budget-based position sizing;
* VaR/ES for a discrete loss distribution (to show VaR's non-subadditivity);
* a seeded Monte Carlo VaR/ES for a one-factor equity book with option positions;
* the classical gambler's-ruin probability;
* first-passage (drawdown-from-start) probabilities for geometric Brownian wealth;
* continuous-Kelly growth, the half-Kelly trade-off, and the growth cost of
  estimating the drift with error;
* liquidity-horizon VaR under even liquidation and the exogenous-spread
  liquidity adjustment;
* concentration (Herfindahl) and effective number of positions;
* futures margin-call triggers, CRE LTV-covenant triggers, and gap losses.

Conventions: returns and rates are decimals; losses are returned as POSITIVE
numbers unless a docstring says otherwise; time is in years unless stated.
Every function is pure except the Monte Carlo routines, which take a seed.
"""

from __future__ import annotations

import math
import random
from typing import Callable, Sequence

from .markets import norm_cdf, norm_ppf

# --------------------------------------------------------------------------
# Position sizing
# --------------------------------------------------------------------------


def size_by_volatility(target_dollar_vol: float, price: float, multiplier: float, vol: float) -> float:
    """Units whose 1-period dollar standard deviation equals ``target_dollar_vol``.

    units = target / (price x multiplier x vol). ``vol`` is the per-period return
    volatility on the same horizon as the target (e.g. daily vol for a daily target).
    """
    return target_dollar_vol / (price * multiplier * vol)


def size_by_var_budget(var_budget: float, price: float, multiplier: float, vol: float,
                       confidence: float = 0.99) -> float:
    """Units whose zero-mean normal VaR equals ``var_budget``: budget / (z sigma P M)."""
    return var_budget / (norm_ppf(confidence) * vol * price * multiplier)


# --------------------------------------------------------------------------
# VaR and ES for discrete distributions
# --------------------------------------------------------------------------


def discrete_var_es(losses: Sequence[float], probs: Sequence[float], confidence: float) -> dict:
    """VaR and ES of a discrete LOSS distribution (losses positive).

    VaR_c = smallest loss l with P(L <= l) >= c.
    ES_c  = (1/(1-c)) x integral of the loss quantile over (c, 1): the tail
            probability mass 1-c is filled from the largest losses downward.
    """
    if abs(sum(probs) - 1.0) > 1e-9:
        raise ValueError("probabilities must sum to 1")
    pairs = sorted(zip(losses, probs))
    cum = 0.0
    var = pairs[-1][0]
    for l, p in pairs:
        cum += p
        if cum >= confidence - 1e-12:
            var = l
            break
    tail = 1.0 - confidence
    remaining = tail
    acc = 0.0
    for l, p in sorted(pairs, reverse=True):
        take = min(p, remaining)
        acc += take * l
        remaining -= take
        if remaining <= 1e-15:
            break
    return {"var": var, "es": acc / tail}


def mc_var_es(revalue: Callable[[float], float], sigma_h: float, paths: int, confidence: float = 0.99,
              seed: int = 21, mu_h: float = 0.0) -> dict:
    """Seeded Monte Carlo VaR/ES for a book driven by one normal log-return factor.

    For each path draw z ~ N(0,1), set the horizon log return x = mu_h + sigma_h z
    and compute P&L = revalue(x). Returns positive VaR and ES using the same order-
    statistic convention as ``risk.historical_var`` / ``risk.historical_es``, plus
    the mean P&L. Uses ``random.Random(seed).gauss`` so results are reproducible.
    """
    rng = random.Random(seed)
    pnl = sorted(revalue(mu_h + sigma_h * rng.gauss(0.0, 1.0)) for _ in range(paths))
    k = int(math.floor(paths * (1 - confidence)))
    tail = pnl[: k + 1]
    return {"var": -pnl[k], "es": -sum(tail) / len(tail), "mean": sum(pnl) / paths}


# --------------------------------------------------------------------------
# Ruin and drawdown
# --------------------------------------------------------------------------


def gamblers_ruin(p: float, start: int, target: int | None = None) -> float:
    """Probability of losing ``start`` units before reaching ``target`` with +/-1 steps.

    p is the probability of +1. With q = 1-p and rho = q/p:
      finite target N:  P_ruin = (rho^k - rho^N) / (1 - rho^N)   (p != 1/2)
                        P_ruin = 1 - k/N                          (p == 1/2)
      no target:        P_ruin = rho^k if p > 1/2, else 1.
    """
    q = 1 - p
    if target is None:
        return (q / p) ** start if p > 0.5 else 1.0
    if abs(p - 0.5) < 1e-15:
        return 1 - start / target
    rho = q / p
    return (rho ** start - rho ** target) / (1 - rho ** target)


def prob_ever_below(depth: float, log_drift: float, log_vol: float) -> float:
    """P(wealth ever falls to (1-depth) x its starting value), infinite horizon.

    Wealth is geometric Brownian motion; ln W has drift m (= log_drift) and vol s.
    P = exp(-2 m a / s^2) with a = -ln(1-depth), for m > 0; equals 1 if m <= 0.
    Measured from the START, not from a running peak.
    """
    if log_drift <= 0:
        return 1.0
    a = -math.log(1 - depth)
    return math.exp(-2 * log_drift * a / log_vol ** 2)


def prob_below_within(depth: float, log_drift: float, log_vol: float, horizon: float) -> float:
    """P(min over [0,T] of ln W/W0 <= ln(1-depth)) for Brownian ln W (reflection principle).

    P = N((-a - mT)/(s sqrt T)) + exp(-2 m a / s^2) N((-a + mT)/(s sqrt T)), a = -ln(1-depth).
    """
    a = -math.log(1 - depth)
    m, s, t = log_drift, log_vol, horizon
    st = s * math.sqrt(t)
    return norm_cdf((-a - m * t) / st) + math.exp(-2 * m * a / s ** 2) * norm_cdf((-a + m * t) / st)


def simulate_max_drawdowns(log_drift: float, log_vol: float, years: float, steps_per_year: int,
                           paths: int, seed: int = 21) -> list[float]:
    """Seeded simulation of the maximum peak-to-trough drawdown (decimal) of GBM wealth."""
    rng = random.Random(seed)
    dt = 1.0 / steps_per_year
    n = int(round(years * steps_per_year))
    m, sd = log_drift * dt, log_vol * math.sqrt(dt)
    out = []
    for _ in range(paths):
        lw = 0.0
        peak = 0.0
        mdd = 0.0
        for _ in range(n):
            lw += m + sd * rng.gauss(0.0, 1.0)
            if lw > peak:
                peak = lw
            dd = 1 - math.exp(lw - peak)
            if dd > mdd:
                mdd = dd
        out.append(mdd)
    return out


# --------------------------------------------------------------------------
# Continuous Kelly
# --------------------------------------------------------------------------


def kelly_growth(f: float, excess_mu: float, sigma: float, r: float = 0.0) -> float:
    """Log growth rate of wealth with fraction f in a lognormal asset: r + f(mu-r) - f^2 sigma^2/2."""
    return r + f * excess_mu - 0.5 * f * f * sigma * sigma


def kelly_growth_with_estimation(k: float, excess_mu: float, sigma: float, se: float) -> float:
    """Expected excess log growth when f = k x (mu_hat - r)/sigma^2 and mu_hat ~ N(mu, se^2).

    E[g] = k (mu-r)^2/sigma^2 - (k^2/2) ((mu-r)^2 + se^2)/sigma^2.
    The penalty relative to knowing mu is (k^2/2) se^2/sigma^2.
    """
    return k * excess_mu ** 2 / sigma ** 2 - 0.5 * k * k * (excess_mu ** 2 + se ** 2) / sigma ** 2


def kelly_optimal_shrink(excess_mu: float, se: float) -> float:
    """Multiplier on the estimated Kelly fraction that maximizes expected growth: m^2/(m^2+se^2)."""
    return excess_mu ** 2 / (excess_mu ** 2 + se ** 2)


# --------------------------------------------------------------------------
# Liquidity
# --------------------------------------------------------------------------


def liquidation_variance_factor(days: int) -> float:
    """Sum of squared remaining exposure under even liquidation over ``days`` days.

    The position is sold in equal slices at the end of each day, so during day k the
    exposure is (T-k+1)/T. Factor = sum_k ((T-k+1)/T)^2 = (T+1)(2T+1)/(6T).
    Horizon VaR = 1-day VaR x sqrt(factor). Compare with sqrt(T) for holding to day T.
    """
    t = days
    return (t + 1) * (2 * t + 1) / (6 * t)


def liquidity_adjusted_var(var: float, position_value: float, spread: float) -> float:
    """Exogenous-spread liquidity adjustment (Bangia et al. 1999): VaR + 0.5 x spread x value.

    ``spread`` is the full bid-ask spread as a fraction of mid; use a stressed spread.
    """
    return var + 0.5 * spread * position_value


# --------------------------------------------------------------------------
# Concentration
# --------------------------------------------------------------------------


def herfindahl(weights: Sequence[float]) -> dict:
    """Herfindahl index of absolute shares and the effective number of positions (1/HHI)."""
    tot = sum(abs(w) for w in weights)
    shares = [abs(w) / tot for w in weights]
    hhi = sum(s * s for s in shares)
    return {"hhi": hhi, "effective_n": 1.0 / hhi, "shares": shares}


# --------------------------------------------------------------------------
# Financing, margin and gaps
# --------------------------------------------------------------------------


def futures_margin_call(account_equity: float, contracts: float, multiplier: float,
                        initial_margin: float, maintenance_margin: float) -> dict:
    """Adverse price move (index points) that triggers a margin call on a long futures position.

    Margins are per contract. A call occurs when equity < maintenance x contracts, and the
    call restores equity to the INITIAL level (exchange convention for speculative accounts).
    Returns the trigger move and the call amount at the trigger.
    """
    maint = maintenance_margin * contracts
    trigger = (account_equity - maint) / (contracts * multiplier)
    call = (initial_margin - maintenance_margin) * contracts
    return {"trigger_points": trigger, "call_at_trigger": call}


def ltv_covenant(loan: float, value: float, max_ltv: float) -> dict:
    """Value decline that breaches a maximum-LTV covenant, and cure paydown as a function of value.

    Breach decline = 1 - loan / (max_ltv x value). Cure paydown at new value V1 is
    max(0, loan - max_ltv x V1).
    """
    return {"breach_decline": 1 - loan / (max_ltv * value),
            "cure": lambda v1: max(0.0, loan - max_ltv * v1)}


def gap_loss(entry: float, stop: float, fill: float, units: float, multiplier: float = 1.0) -> dict:
    """Planned loss at the stop versus realized loss at the fill (long position; positive losses)."""
    planned = (entry - stop) * units * multiplier
    realized = (entry - fill) * units * multiplier
    return {"planned": planned, "realized": realized, "ratio": realized / planned}
