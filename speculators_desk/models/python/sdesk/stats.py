"""Probability and statistics helpers used throughout the book."""

from __future__ import annotations

import math
from typing import Sequence


def bayes_posterior(prior: float, p_evidence_given_h: float, p_evidence_given_not_h: float) -> float:
    """P(H | E) = P(E|H)P(H) / [P(E|H)P(H) + P(E|~H)(1-P(H))]."""
    num = p_evidence_given_h * prior
    return num / (num + p_evidence_given_not_h * (1 - prior))


def likelihood_ratio_update(prior: float, likelihood_ratio: float) -> float:
    """Odds form of Bayes: posterior odds = prior odds x LR."""
    odds = prior / (1 - prior) * likelihood_ratio
    return odds / (1 + odds)


def mean(x: Sequence[float]) -> float:
    return sum(x) / len(x)


def stdev(x: Sequence[float], sample: bool = True) -> float:
    m = mean(x)
    d = len(x) - 1 if sample else len(x)
    return math.sqrt(sum((v - m) ** 2 for v in x) / d)


def covariance(x: Sequence[float], y: Sequence[float], sample: bool = True) -> float:
    mx, my = mean(x), mean(y)
    d = len(x) - 1 if sample else len(x)
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / d


def correlation(x: Sequence[float], y: Sequence[float]) -> float:
    return covariance(x, y) / (stdev(x) * stdev(y))


def ols(x: Sequence[float], y: Sequence[float]) -> dict:
    """Simple regression y = a + b x. Returns a, b, r2, residual sd, se(b)."""
    n = len(x)
    mx, my = mean(x), mean(y)
    sxx = sum((v - mx) ** 2 for v in x)
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    b = sxy / sxx
    a = my - b * mx
    resid = [yy - (a + b * xx) for xx, yy in zip(x, y)]
    sse = sum(r * r for r in resid)
    sst = sum((v - my) ** 2 for v in y)
    s = math.sqrt(sse / (n - 2))
    return {"a": a, "b": b, "r2": 1 - sse / sst, "resid_sd": s, "se_b": s / math.sqrt(sxx)}


def simple_returns(prices: Sequence[float]) -> list[float]:
    return [prices[i] / prices[i - 1] - 1 for i in range(1, len(prices))]


def log_returns(prices: Sequence[float]) -> list[float]:
    return [math.log(prices[i] / prices[i - 1]) for i in range(1, len(prices))]


def brier_score(forecasts: Sequence[float], outcomes: Sequence[int]) -> float:
    """Mean squared error of probability forecasts against 0/1 outcomes (lower is better)."""
    return sum((f - o) ** 2 for f, o in zip(forecasts, outcomes)) / len(forecasts)


def geometric_mean_return(returns: Sequence[float]) -> float:
    g = 1.0
    for r in returns:
        g *= 1 + r
    return g ** (1 / len(returns)) - 1
