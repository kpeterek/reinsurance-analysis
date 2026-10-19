"""Risk measurement, position sizing, and growth/ruin mathematics."""

from __future__ import annotations

import math
import random
from typing import Sequence

from .markets import norm_cdf, norm_pdf, norm_ppf  # noqa: F401


def expected_value(outcomes: Sequence[float], probs: Sequence[float]) -> float:
    if abs(sum(probs) - 1.0) > 1e-9:
        raise ValueError("probabilities must sum to 1")
    return sum(o * p for o, p in zip(outcomes, probs))


def variance(outcomes: Sequence[float], probs: Sequence[float]) -> float:
    m = expected_value(outcomes, probs)
    return sum(p * (o - m) ** 2 for o, p in zip(outcomes, probs))


def expected_log_growth(returns: Sequence[float], probs: Sequence[float], fraction: float = 1.0) -> float:
    """E[ln(1 + f r)] -- the per-period growth rate of a repeated bet at fraction f."""
    return sum(p * math.log(1 + fraction * r) for r, p in zip(returns, probs))


def kelly_binary(p_win: float, net_odds: float) -> float:
    """Kelly fraction for a bet that wins b per 1 staked with prob p, else loses the stake.

    f* = p - (1-p)/b = (b p - (1-p)) / b
    """
    return p_win - (1 - p_win) / net_odds


def kelly_general_binary(p_win: float, gain: float, loss: float) -> float:
    """Kelly fraction when a unit position returns +gain w.p. p and -loss otherwise.

    f* = p/loss - (1-p)/gain.
    """
    return p_win / loss - (1 - p_win) / gain


def kelly_continuous(mu: float, r: float, sigma: float) -> float:
    """Merton/Kelly leverage for lognormal asset: (mu - r) / sigma^2."""
    return (mu - r) / sigma ** 2


def drawdown_recovery_required(drawdown: float) -> float:
    return 1.0 / (1.0 - drawdown) - 1.0


def max_drawdown(values: Sequence[float]) -> dict:
    """Maximum peak-to-trough decline of a value series (decimal)."""
    peak = values[0]
    mdd = 0.0
    peak_i = trough_i = best_peak = 0
    for i, v in enumerate(values):
        if v > peak:
            peak, peak_i = v, i
        dd = 1 - v / peak
        if dd > mdd:
            mdd, trough_i, best_peak = dd, i, peak_i
    return {"max_drawdown": mdd, "peak_index": best_peak, "trough_index": trough_i}


def scale_volatility(sigma: float, from_periods_per_year: float, to_periods_per_year: float) -> float:
    """Square-root-of-time scaling (assumes i.i.d. returns)."""
    return sigma * math.sqrt(from_periods_per_year / to_periods_per_year)


def parametric_var(value: float, mu: float, sigma: float, confidence: float = 0.99) -> float:
    """Normal VaR as a positive loss: -(mu - z sigma) x value."""
    z = norm_ppf(confidence)
    return -(mu - z * sigma) * value


def parametric_es(value: float, mu: float, sigma: float, confidence: float = 0.99) -> float:
    """Normal expected shortfall (positive loss): -(mu - sigma phi(z)/(1-c)) x value."""
    z = norm_ppf(confidence)
    return -(mu - sigma * norm_pdf(z) / (1 - confidence)) * value


def historical_var(pnl: Sequence[float], confidence: float = 0.99) -> float:
    """Historical VaR (positive loss) using the empirical quantile, lower-order-statistic rule.

    With n observations, VaR is the loss at sorted index floor(n(1-c)) -- i.e., the
    k-th worst loss with k = floor(n(1-c)) + 1. Conventions differ; state yours.
    """
    s = sorted(pnl)
    k = int(math.floor(len(s) * (1 - confidence)))
    return -s[k]


def historical_es(pnl: Sequence[float], confidence: float = 0.99) -> float:
    """Average of the losses at or beyond the historical VaR observation (positive)."""
    s = sorted(pnl)
    k = int(math.floor(len(s) * (1 - confidence)))
    tail = s[: k + 1]
    return -sum(tail) / len(tail)


def position_size_by_stop(capital: float, risk_fraction: float, entry: float, stop: float,
                          multiplier: float = 1.0) -> float:
    """Units such that a move from entry to stop loses capital x risk_fraction.

    NOTE: a stop order is not a guaranteed exit price; gaps make realized loss larger.
    """
    per_unit = abs(entry - stop) * multiplier
    return capital * risk_fraction / per_unit


def portfolio_volatility(weights: Sequence[float], vols: Sequence[float], corr: Sequence[Sequence[float]]) -> float:
    n = len(weights)
    var = 0.0
    for i in range(n):
        for j in range(n):
            var += weights[i] * weights[j] * vols[i] * vols[j] * corr[i][j]
    return math.sqrt(var)


def simulate_fixed_fraction(returns: Sequence[float], probs: Sequence[float], fraction: float,
                            periods: int, paths: int, seed: int = 7, ruin_level: float = 0.0) -> dict:
    """Monte Carlo of repeated betting at a fixed fraction of wealth.

    Returns median terminal wealth (starting at 1), mean terminal wealth and the
    fraction of paths that touched ``ruin_level`` (e.g., 0.2 = lost 80%).
    """
    rng = random.Random(seed)
    cum = []
    acc = 0.0
    for p in probs:
        acc += p
        cum.append(acc)
    terminals = []
    ruined = 0
    for _ in range(paths):
        w = 1.0
        hit = False
        for _ in range(periods):
            u = rng.random()
            idx = next(i for i, c in enumerate(cum) if u <= c)
            w *= 1 + fraction * returns[idx]
            if w <= ruin_level:
                hit = True
        terminals.append(w)
        ruined += hit
    terminals.sort()
    return {"median": terminals[len(terminals) // 2], "mean": sum(terminals) / paths,
            "ruin_prob": ruined / paths}
