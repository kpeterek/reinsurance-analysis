"""Statistical decision tools for Chapter 20 (probability and decision-making).

Conventions
-----------
* Probabilities and rates are decimals (0.15 means 15%).
* Money amounts are in whatever unit the caller uses (the chapter uses $ millions);
  functions never rescale them.
* No external dependencies (no scipy): the Student-t distribution is computed from the
  regularized incomplete beta function by continued fraction (Numerical Recipes, betacf).
  Excel equivalents are given where they exist.

Functions
---------
student_t_cdf, student_t_ppf, t_interval        -- small-sample inference
effective_sample_size_ar1                        -- serial correlation and information
scaled_t_tail                                    -- variance-matched t vs normal tails
hill_estimator, pareto_tail_prob                 -- power-law tails
law_of_total_variance                            -- mixtures of scenarios
bma_weights, mixture_moments, normal_pdf         -- Bayesian model averaging
reference_class_adjust                           -- Kahneman-Lovallo shrinkage
brier_decomposition                              -- Murphy (1973) reliability/resolution/uncertainty
crra_utility, crra_certainty_equivalent          -- expected utility
evpi, evsi_binary_signal                         -- value of information
regret_table, minimax_regret                     -- decisions without probabilities
"""

from __future__ import annotations

import math
from typing import Sequence


# ---------------------------------------------------------------------------
# Student-t distribution
# ---------------------------------------------------------------------------

def _betacf(a: float, b: float, x: float, max_iter: int = 500, eps: float = 1e-15) -> float:
    """Continued fraction for the incomplete beta function (modified Lentz)."""
    tiny = 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = tiny if abs(d) < tiny else d
    d = 1.0 / d
    h = d
    for m in range(1, max_iter + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = tiny if abs(d) < tiny else d
        c = 1.0 + aa / c
        c = tiny if abs(c) < tiny else c
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = tiny if abs(d) < tiny else d
        c = 1.0 + aa / c
        c = tiny if abs(c) < tiny else c
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < eps:
            break
    return h


def reg_incomplete_beta(x: float, a: float, b: float) -> float:
    """Regularized incomplete beta I_x(a, b). Excel: BETA.DIST(x, a, b, TRUE)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    front = math.exp(lbeta + a * math.log(x) + b * math.log(1.0 - x))
    if x < (a + 1.0) / (a + b + 2.0):
        return front * _betacf(a, b, x) / a
    return 1.0 - front * _betacf(b, a, 1.0 - x) / b


def student_t_cdf(t: float, nu: float) -> float:
    """CDF of the standard Student-t with nu degrees of freedom. Excel: T.DIST(t, nu, TRUE)."""
    x = nu / (nu + t * t)
    tail = 0.5 * reg_incomplete_beta(x, nu / 2.0, 0.5)
    return 1.0 - tail if t >= 0 else tail


def student_t_ppf(p: float, nu: float) -> float:
    """Inverse Student-t CDF by bisection. Excel: T.INV(p, nu); two-sided T.INV.2T(alpha, nu).

    Accurate to about 1e-7 near the median (the incomplete beta loses precision as x -> 1)
    and to better than 1e-10 in the tails used in the book.
    """
    if not 0.0 < p < 1.0:
        raise ValueError("p must be in (0, 1)")
    lo, hi = -1e3, 1e3
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if student_t_cdf(mid, nu) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def t_interval(xs: Sequence[float], confidence: float = 0.95) -> dict:
    """Two-sided t confidence interval for a mean from an i.i.d. sample.

    Returns mean, sample sd (n-1), standard error, t critical value, half-width, lo, hi.
    """
    n = len(xs)
    m = sum(xs) / n
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1))
    se = sd / math.sqrt(n)
    tc = student_t_ppf(1.0 - (1.0 - confidence) / 2.0, n - 1)
    hw = tc * se
    return {"n": n, "mean": m, "sd": sd, "se": se, "t_crit": tc, "half_width": hw,
            "lo": m - hw, "hi": m + hw}


def effective_sample_size_ar1(n: int, rho: float) -> float:
    """Approximate effective number of independent observations for the mean of an AR(1)
    series with lag-1 autocorrelation rho: n (1 - rho) / (1 + rho). Large-n approximation."""
    return n * (1.0 - rho) / (1.0 + rho)


def scaled_t_tail(threshold_z: float, nu: float) -> float:
    """P(X < -threshold_z sd) for a Student-t scaled to unit variance (nu > 2).

    A unit-variance t has scale s = sqrt((nu - 2)/nu), so the standardized threshold
    in t units is threshold_z / s.
    """
    if nu <= 2:
        raise ValueError("variance is infinite for nu <= 2")
    s = math.sqrt((nu - 2.0) / nu)
    return student_t_cdf(-threshold_z / s, nu)


def t_excess_kurtosis(nu: float) -> float:
    """Excess kurtosis of Student-t: 6/(nu - 4) for nu > 4; infinite otherwise."""
    return math.inf if nu <= 4 else 6.0 / (nu - 4.0)


# ---------------------------------------------------------------------------
# Power-law tails
# ---------------------------------------------------------------------------

def hill_estimator(losses: Sequence[float], k: int) -> dict:
    """Hill estimator of the tail index alpha from the k largest observations (losses > 0).

    alpha_hat = k / sum_{i=1..k} ln(X_(i) / X_(k+1)), where X_(1) >= X_(2) >= ...
    The threshold u = X_(k+1). Requires k + 1 <= len(losses).
    """
    xs = sorted(losses, reverse=True)
    u = xs[k]
    s = sum(math.log(x / u) for x in xs[:k])
    return {"alpha": k / s, "threshold": u, "k": k}


def pareto_tail_prob(x: float, threshold: float, p_exceed_threshold: float, alpha: float) -> float:
    """P(X > x) = P(X > u) (x/u)^(-alpha) for x >= u under a Pareto tail above u."""
    return p_exceed_threshold * (x / threshold) ** (-alpha)


# ---------------------------------------------------------------------------
# Mixtures, model averaging
# ---------------------------------------------------------------------------

def law_of_total_variance(probs: Sequence[float], means: Sequence[float], sds: Sequence[float]) -> dict:
    """Mean and variance of a mixture: Var = E[Var | regime] + Var(E[. | regime])."""
    m = sum(p * mu for p, mu in zip(probs, means))
    within = sum(p * s * s for p, s in zip(probs, sds))
    between = sum(p * (mu - m) ** 2 for p, mu in zip(probs, means))
    return {"mean": m, "within": within, "between": between, "var": within + between,
            "sd": math.sqrt(within + between)}


def normal_pdf(x: float, mu: float, sigma: float) -> float:
    return math.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * math.sqrt(2.0 * math.pi))


def bma_weights(priors: Sequence[float], likelihoods: Sequence[float]) -> list[float]:
    """Posterior model probabilities w_k = prior_k L_k / sum_j prior_j L_j."""
    num = [p * l for p, l in zip(priors, likelihoods)]
    tot = sum(num)
    return [v / tot for v in num]


def mixture_moments(weights: Sequence[float], means: Sequence[float], sds: Sequence[float]) -> dict:
    """Alias of law_of_total_variance with model weights (BMA predictive moments)."""
    return law_of_total_variance(weights, means, sds)


def mixture_normal_cdf(x: float, weights: Sequence[float], means: Sequence[float], sds: Sequence[float]) -> float:
    """CDF of a finite mixture of normals."""
    return sum(w * 0.5 * (1.0 + math.erf((x - m) / (s * math.sqrt(2.0))))
               for w, m, s in zip(weights, means, sds))


# ---------------------------------------------------------------------------
# Reference-class forecasting
# ---------------------------------------------------------------------------

def reference_class_adjust(base_rate_mean: float, inside_view: float, predictive_corr: float) -> float:
    """Kahneman-Lovallo regressive correction: base + r (inside - base), 0 <= r <= 1.

    r is the correlation between past inside-view forecasts and outcomes. r = 0 ignores the
    case-specific estimate; r = 1 accepts it unchanged.
    """
    return base_rate_mean + predictive_corr * (inside_view - base_rate_mean)


# ---------------------------------------------------------------------------
# Calibration
# ---------------------------------------------------------------------------

def brier_decomposition(bins: Sequence[tuple[float, int, int]]) -> dict:
    """Murphy (1973) decomposition for forecasts grouped into bins of identical forecast value.

    bins: (forecast probability f_k, count n_k, number of events o_k).
    BS = REL - RES + UNC, where
      REL = (1/N) sum n_k (f_k - obar_k)^2
      RES = (1/N) sum n_k (obar_k - obar)^2
      UNC = obar (1 - obar).
    The identity is exact when every forecast in a bin equals f_k.
    """
    n_tot = sum(n for _, n, _ in bins)
    o_tot = sum(o for _, _, o in bins)
    obar = o_tot / n_tot
    rel = sum(n * (f - o / n) ** 2 for f, n, o in bins) / n_tot
    res = sum(n * (o / n - obar) ** 2 for f, n, o in bins) / n_tot
    unc = obar * (1.0 - obar)
    bs = sum(o * (f - 1.0) ** 2 + (n - o) * f ** 2 for f, n, o in bins) / n_tot
    return {"bs": bs, "rel": rel, "res": res, "unc": unc, "obar": obar, "n": n_tot,
            "bss": 1.0 - bs / unc}


def expand_bins(bins: Sequence[tuple[float, int, int]]) -> tuple[list[float], list[int]]:
    """Expand (f, n, o) bins into forecast and outcome lists for stats.brier_score."""
    fc, out = [], []
    for f, n, o in bins:
        fc += [f] * n
        out += [1] * o + [0] * (n - o)
    return fc, out


# ---------------------------------------------------------------------------
# Expected utility
# ---------------------------------------------------------------------------

def crra_utility(w: float, gamma: float) -> float:
    """CRRA utility: w^(1-gamma)/(1-gamma); ln w at gamma = 1. Wealth must be positive."""
    if w <= 0:
        raise ValueError("CRRA utility requires positive wealth")
    if abs(gamma - 1.0) < 1e-12:
        return math.log(w)
    return w ** (1.0 - gamma) / (1.0 - gamma)


def crra_certainty_equivalent(wealths: Sequence[float], probs: Sequence[float], gamma: float) -> float:
    """Certainty-equivalent wealth: u^{-1}(E[u(W)])."""
    if abs(gamma - 1.0) < 1e-12:
        return math.exp(sum(p * math.log(w) for w, p in zip(wealths, probs)))
    eu = sum(p * w ** (1.0 - gamma) for w, p in zip(wealths, probs))
    return eu ** (1.0 / (1.0 - gamma))


# ---------------------------------------------------------------------------
# Value of information
# ---------------------------------------------------------------------------

def evpi(payoffs: Sequence[Sequence[float]], probs: Sequence[float]) -> dict:
    """Expected value of perfect information.

    payoffs[a][s] is the payoff of action a in state s. Returns the prior-optimal action,
    its EV, the EV with perfect information, and EVPI.
    """
    evs = [sum(p * x for p, x in zip(probs, row)) for row in payoffs]
    best = max(range(len(evs)), key=lambda a: evs[a])
    ev_pi = sum(p * max(row[s] for row in payoffs) for s, p in enumerate(probs))
    return {"evs": evs, "best_action": best, "ev_prior": evs[best], "ev_perfect": ev_pi,
            "evpi": ev_pi - evs[best]}


def evsi_binary_signal(payoffs: Sequence[Sequence[float]], probs: Sequence[float],
                       p_signal_given_state: Sequence[float]) -> dict:
    """Expected value of sample information for a binary signal (e.g. a PCA 'flag').

    p_signal_given_state[s] = P(signal = 1 | state s). Returns predictive probabilities,
    posteriors, optimal action and EV after each signal, EV with the signal, and EVSI.
    """
    prior = evpi(payoffs, probs)
    out = {"ev_prior": prior["ev_prior"]}
    ev_with = 0.0
    for sig in (1, 0):
        like = [q if sig == 1 else 1.0 - q for q in p_signal_given_state]
        joint = [p * l for p, l in zip(probs, like)]
        ps = sum(joint)
        post = [j / ps for j in joint]
        evs = [sum(p * x for p, x in zip(post, row)) for row in payoffs]
        a = max(range(len(evs)), key=lambda k: evs[k])
        out[f"p_signal_{sig}"] = ps
        out[f"posterior_{sig}"] = post
        out[f"evs_{sig}"] = evs
        out[f"action_{sig}"] = a
        ev_with += ps * evs[a]
    out["ev_with_signal"] = ev_with
    out["evsi"] = ev_with - prior["ev_prior"]
    out["evpi"] = prior["evpi"]
    return out


# ---------------------------------------------------------------------------
# Regret
# ---------------------------------------------------------------------------

def regret_table(payoffs: Sequence[Sequence[float]]) -> list[list[float]]:
    """Regret[a][s] = max_a' payoff[a'][s] - payoff[a][s]."""
    n_s = len(payoffs[0])
    col_max = [max(row[s] for row in payoffs) for s in range(n_s)]
    return [[col_max[s] - row[s] for s in range(n_s)] for row in payoffs]


def minimax_regret(payoffs: Sequence[Sequence[float]]) -> dict:
    """Savage's minimax-regret action and each action's maximum regret."""
    reg = regret_table(payoffs)
    max_reg = [max(r) for r in reg]
    best = min(range(len(max_reg)), key=lambda a: max_reg[a])
    return {"regret": reg, "max_regret": max_reg, "action": best}
