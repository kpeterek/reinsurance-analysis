"""Derivatives helpers for Chapter 18 (Derivatives, Volatility, and Convexity).

Extends ``sdesk.markets`` (Black-Scholes price, delta, gamma, vega, parity gap)
and reuses ``sdesk.x_capital_structure`` (Bachelier caplets and cap premium)
without duplicating either. New here:

* ``bs_theta`` -- calendar time decay, per year (divide by 365 for per day)
* ``bs_implied_vol`` -- implied volatility by bisection
* ``forward_contract_value`` -- value of an off-market forward
* ``delta_hedge_simulation`` -- discrete re-hedging of a long option with a
  fixed random seed, with the gamma-P&L decomposition
* ``put_roll_cost`` -- annual cost of carrying a rolling put hedge
* ``min_variance_hedge`` -- futures hedge ratio and effectiveness
* ``black_caplet`` / ``black_cap_premium`` -- lognormal (Black-76) caplets on the
  same flat-forward grid as ``x_capital_structure.cap_premium``
* ``swap_value`` -- fixed-for-floating swap from discount factors
* ``merton_claims`` -- equity as a call and risky debt as riskless debt less a put

Conventions
-----------
* Rates are decimals. ``r`` and ``q`` in Black-Scholes functions are
  continuously compounded annual rates; ``t`` is in years.
* Volatilities are annual, in decimals (0.20 = 20 vol points).
* Option values are per unit of underlying; multiply by contract size.
* ``side`` = +1 long, -1 short (notation guide section 4).
* Swap value is to the **pay-fixed** party (receives floating). Positive means the
  pay-fixed side is owed money.
"""

from __future__ import annotations

import math
import random
from typing import Sequence

from . import markets
from . import x_capital_structure as xc


# --------------------------------------------------------------------------
# Black-Scholes extensions
# --------------------------------------------------------------------------

def bs_theta(s: float, k: float, t: float, r: float, sigma: float, kind: str = "call",
             q: float = 0.0) -> float:
    """dV/dt in calendar time (value change per year as time passes, sign included).

    call: -S e^{-qt} phi(d1) sigma / (2 sqrt t) - r K e^{-rt} N(d2) + q S e^{-qt} N(d1)
    put:  -S e^{-qt} phi(d1) sigma / (2 sqrt t) + r K e^{-rt} N(-d2) - q S e^{-qt} N(-d1)
    Per calendar day: divide by 365. Excel has no built-in; build from NORM.S.DIST.
    """
    d1, d2 = markets._d1_d2(s, k, t, r, sigma, q)
    common = -s * math.exp(-q * t) * markets.norm_pdf(d1) * sigma / (2.0 * math.sqrt(t))
    if kind == "call":
        return (common - r * k * math.exp(-r * t) * markets.norm_cdf(d2)
                + q * s * math.exp(-q * t) * markets.norm_cdf(d1))
    return (common + r * k * math.exp(-r * t) * markets.norm_cdf(-d2)
            - q * s * math.exp(-q * t) * markets.norm_cdf(-d1))


def bs_implied_vol(price: float, s: float, k: float, t: float, r: float, kind: str = "call",
                   q: float = 0.0, lo: float = 1e-4, hi: float = 5.0, tol: float = 1e-10) -> float:
    """Implied volatility by bisection. Raises if the price is outside no-arbitrage bounds."""
    f_lo = markets.bs_price(s, k, t, r, lo, kind, q) - price
    f_hi = markets.bs_price(s, k, t, r, hi, kind, q) - price
    if f_lo > 0 or f_hi < 0:
        raise ValueError("price outside the Black-Scholes range for vol in [lo, hi]")
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        f = markets.bs_price(s, k, t, r, mid, kind, q) - price
        if abs(f) < tol:
            return mid
        if f > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def forward_contract_value(s: float, k: float, t: float, r: float, q: float = 0.0) -> float:
    """Value to the long of a forward struck at K: S e^{-qt} - K e^{-rt}."""
    return s * math.exp(-q * t) - k * math.exp(-r * t)


# --------------------------------------------------------------------------
# Delta hedging
# --------------------------------------------------------------------------

def delta_hedge_simulation(s0: float, k: float, t: float, r: float, sigma_implied: float,
                           sigma_realized: float, n_steps: int, seed: int,
                           kind: str = "call", mu: float = 0.0, q: float = 0.0) -> dict:
    """Buy one option at ``sigma_implied``; hedge its delta (computed at the implied
    vol) at ``n_steps`` equally spaced dates; the stock follows GBM with drift ``mu``
    and volatility ``sigma_realized``. Cash is financed / invested at ``r``.

    Step P&L (long option, short delta shares, self-financing):
        pnl_i = V_{i+1} - V_i - Delta_i (S_{i+1} - S_i) - r dt (V_i - Delta_i S_i)
                - Delta_i q S_i dt   (dividends owed on short stock)
    with V valued at the implied vol (at expiry V = payoff).

    Gamma decomposition (what the chapter derives):
        gamma_i = 0.5 Gamma_i S_i^2 [ (dS_i/S_i)^2 - sigma_implied^2 dt ]
        theory_i = 0.5 Gamma_i S_i^2 (sigma_realized^2 - sigma_implied^2) dt
    ``gamma_i`` uses the realized squared return of each step; ``theory_i`` its
    expectation. Sums are undiscounted (r is small over the horizon).

    Random numbers: ``random.Random(seed).gauss(0, 1)``, so results are reproducible.
    """
    rng = random.Random(seed)
    dt = t / n_steps
    s = s0
    v0 = markets.bs_price(s0, k, t, r, sigma_implied, kind, q)
    v = v0
    path = [s0]
    pnl = gamma_pnl = theory = 0.0
    realized_sq = 0.0
    for i in range(n_steps):
        tau = t - i * dt
        delta = markets.bs_delta(s, k, tau, r, sigma_implied, kind, q)
        gamma = markets.bs_gamma(s, k, tau, r, sigma_implied, q)
        z = rng.gauss(0.0, 1.0)
        s_new = s * math.exp((mu - q - 0.5 * sigma_realized ** 2) * dt
                             + sigma_realized * math.sqrt(dt) * z)
        tau_new = tau - dt
        if i == n_steps - 1:
            v_new = markets.call_payoff(s_new, k) if kind == "call" else markets.put_payoff(s_new, k)
        else:
            v_new = markets.bs_price(s_new, k, tau_new, r, sigma_implied, kind, q)
        ret = s_new / s - 1.0
        realized_sq += math.log(s_new / s) ** 2
        pnl += (v_new - v) - delta * (s_new - s) - r * dt * (v - delta * s) - delta * q * s * dt
        gamma_pnl += 0.5 * gamma * s * s * (ret * ret - sigma_implied ** 2 * dt)
        theory += 0.5 * gamma * s * s * (sigma_realized ** 2 - sigma_implied ** 2) * dt
        s, v = s_new, v_new
        path.append(s)
    return {"premium": v0, "pnl": pnl, "gamma_pnl": gamma_pnl, "theory_pnl": theory,
            "realized_vol": math.sqrt(realized_sq / t), "final_spot": s, "path": path}


# --------------------------------------------------------------------------
# Tail hedges and futures hedges
# --------------------------------------------------------------------------

def put_roll_cost(s: float, moneyness: float, tenor: float, r: float, sigma: float,
                  q: float = 0.0) -> dict:
    """Cost of buying a put struck at ``moneyness`` x S every ``tenor`` years.

    Assumes the same spot-relative strike, vol and rates at each roll (a steady-state
    carry estimate). Returns the premium per roll (fraction of spot) and the annual
    cost = premium x rolls per year (no reinvestment of expired value).
    """
    k = moneyness * s
    p = markets.bs_price(s, k, tenor, r, sigma, "put", q)
    rolls = 1.0 / tenor
    return {"strike": k, "premium": p, "premium_pct": p / s, "rolls_per_year": rolls,
            "annual_cost_pct": p / s * rolls}


def min_variance_hedge(rho: float, sigma_exposure: float, sigma_hedge: float,
                       exposure_value: float, futures_price: float, multiplier: float) -> dict:
    """h* = rho sigma_S / sigma_F; contracts = h* x exposure / (F x multiplier).

    Effectiveness (variance removed) = rho^2; residual vol = sigma_S sqrt(1 - rho^2).
    Volatilities must be over the same horizon and in the same return units.
    """
    h = rho * sigma_exposure / sigma_hedge
    n = h * exposure_value / (futures_price * multiplier)
    return {"hedge_ratio": h, "contracts": n, "effectiveness": rho ** 2,
            "residual_vol": sigma_exposure * math.sqrt(1.0 - rho ** 2)}


# --------------------------------------------------------------------------
# Interest-rate caps: lognormal (Black-76) counterpart to x_capital_structure
# --------------------------------------------------------------------------

def black_caplet(forward: float, strike: float, lognormal_vol: float, t_expiry: float,
                 accrual: float, discount_factor: float, notional: float = 1.0) -> float:
    """Black-76 caplet: N tau P [F N(d1) - K N(d2)], d1 = [ln(F/K) + 0.5 s^2 T]/(s sqrt T).

    Requires F > 0 and K > 0. At t_expiry = 0 returns intrinsic value.
    """
    if t_expiry <= 0 or lognormal_vol <= 0:
        return notional * accrual * discount_factor * max(forward - strike, 0.0)
    sd = lognormal_vol * math.sqrt(t_expiry)
    d1 = (math.log(forward / strike) + 0.5 * sd * sd) / sd
    d2 = d1 - sd
    return notional * accrual * discount_factor * (forward * markets.norm_cdf(d1)
                                                   - strike * markets.norm_cdf(d2))


def black_cap_premium(notional: float, strike: float, forward: float, lognormal_vol: float,
                      years: float, freq: int = 4, skip_first: bool = True) -> dict:
    """Same grid, discounting and first-period convention as
    ``x_capital_structure.cap_premium`` but with Black-76 caplets."""
    n = int(round(years * freq))
    tau = 1.0 / freq
    total = 0.0
    for j in range(1, n + 1):
        if skip_first and j == 1:
            continue
        df = (1.0 + forward * tau) ** (-j)
        total += black_caplet(forward, strike, lognormal_vol, (j - 1) * tau, tau, df, notional)
    return {"premium": total, "pct_notional": total / notional}


def bachelier_cap_grid(notional: float, forward: float, years: float,
                       strikes: Sequence[float], normal_vols: Sequence[float],
                       freq: int = 4) -> dict:
    """Premium grid {(strike, vol): premium} using ``x_capital_structure.cap_premium``."""
    return {(k, v): xc.cap_premium(notional, k, forward, v, years, freq)["premium"]
            for k in strikes for v in normal_vols}


# --------------------------------------------------------------------------
# Swaps
# --------------------------------------------------------------------------

def discount_factors_from_zero(zero_rates: Sequence[float], times: Sequence[float],
                               freq: int = 0) -> list[float]:
    """DF = exp(-z t) if freq == 0, else (1 + z/freq)^(-freq t)."""
    if freq == 0:
        return [math.exp(-z * t) for z, t in zip(zero_rates, times)]
    return [(1.0 + z / freq) ** (-freq * t) for z, t in zip(zero_rates, times)]


def par_swap_rate(dfs: Sequence[float], accruals: Sequence[float]) -> float:
    """Par fixed rate = (1 - P_n) / sum(tau_j P_j) for a spot-starting swap."""
    return (1.0 - dfs[-1]) / sum(a * d for a, d in zip(accruals, dfs))


def swap_value(notional: float, fixed_rate: float, dfs: Sequence[float],
               accruals: Sequence[float], next_float_fixing: float | None = None) -> dict:
    """Value to the pay-fixed / receive-floating party.

    Fixed leg = N K sum tau_j P_j. Floating leg: on a reset date = N (1 - P_n);
    between resets with the next coupon already fixed at L for accrual tau_1,
    = N (1 + L tau_1) P_1 - N P_n (the floater is worth par just after the next reset).
    """
    annuity = sum(a * d for a, d in zip(accruals, dfs))
    fixed = notional * fixed_rate * annuity
    if next_float_fixing is None:
        floating = notional * (1.0 - dfs[-1])
    else:
        floating = notional * (1.0 + next_float_fixing * accruals[0]) * dfs[0] - notional * dfs[-1]
    return {"fixed_leg": fixed, "floating_leg": floating, "value_pay_fixed": floating - fixed,
            "annuity": annuity, "par_rate": (1.0 - dfs[-1]) / annuity}


# --------------------------------------------------------------------------
# Structural (Merton) view of a mortgage
# --------------------------------------------------------------------------

def merton_claims(asset_value: float, face: float, t: float, r: float, sigma_asset: float,
                  payout: float = 0.0) -> dict:
    """Equity = call on assets struck at the loan balloon ``face``; debt = PV(face) - put.

    ``payout`` is a continuous asset cash yield (NOI yield paid out). Returns equity,
    debt, the put (lender's short option), risk-neutral default probability N(-d2),
    and the credit spread y - r with y = -ln(D/face)/t (continuous).
    """
    e = markets.bs_price(asset_value, face, t, r, sigma_asset, "call", payout)
    put = markets.bs_price(asset_value, face, t, r, sigma_asset, "put", payout)
    riskless = face * math.exp(-r * t)
    debt = riskless - put
    _, d2 = markets._d1_d2(asset_value, face, t, r, sigma_asset, payout)
    y = -math.log(debt / face) / t
    return {"equity": e, "put": put, "riskless_debt": riskless, "debt": debt,
            "pd_rn": markets.norm_cdf(-d2), "spread": y - r,
            "check": asset_value * math.exp(-payout * t) - e - debt}
