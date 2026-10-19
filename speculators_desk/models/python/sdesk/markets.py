"""Futures, FX, and options mathematics.

Sign convention: ``side`` = +1 for long, -1 for short.

FX quote convention: a pair "BASE/QUOTE" at rate S means 1 unit of BASE costs S
units of QUOTE. EUR/USD = 1.10 means 1 EUR = 1.10 USD. USD/JPY = 150 means
1 USD = 150 JPY. P&L on a position in BASE is realized in QUOTE currency.
"""

from __future__ import annotations

import math


# --------------------------------------------------------------------------
# Futures
# --------------------------------------------------------------------------

def futures_notional(price: float, multiplier: float, contracts: int = 1) -> float:
    """Notional = price x multiplier x contracts (e.g., ES: $50 x index)."""
    return price * multiplier * contracts


def futures_pnl(entry: float, exit_: float, contracts: int, multiplier: float, side: int = 1) -> float:
    """P&L = side x (exit - entry) x multiplier x contracts."""
    return side * (exit_ - entry) * multiplier * contracts


def futures_pnl_ticks(ticks: float, tick_value: float, contracts: int, side: int = 1) -> float:
    return side * ticks * tick_value * contracts


def contracts_for_notional(target_notional: float, price: float, multiplier: float) -> float:
    return target_notional / (price * multiplier)


def futures_fair_value(spot: float, r: float, carry_yield: float, t: float) -> float:
    """Cost-of-carry: F = S exp((r - q) t), continuous rates; q = dividend/convenience yield net of storage."""
    return spot * math.exp((r - carry_yield) * t)


# --------------------------------------------------------------------------
# FX
# --------------------------------------------------------------------------

def fx_pnl(base_amount: float, entry_rate: float, exit_rate: float, side: int = 1) -> float:
    """P&L in QUOTE currency for a position of ``base_amount`` units of BASE."""
    return side * base_amount * (exit_rate - entry_rate)


def convert(amount: float, rate: float, from_ccy: str, pair: str) -> float:
    """Convert ``amount`` of ``from_ccy`` using ``pair`` 'BASE/QUOTE' quoted at ``rate``.

    BASE -> QUOTE multiplies by rate; QUOTE -> BASE divides.
    """
    base, quote = pair.upper().split("/")
    f = from_ccy.upper()
    if f == base:
        return amount * rate
    if f == quote:
        return amount / rate
    raise ValueError(f"{from_ccy} not in pair {pair}")


def covered_interest_forward(spot: float, r_quote: float, r_base: float, t: float) -> float:
    """CIP forward for BASE/QUOTE with simple (money-market) rates over t years.

    F = S (1 + r_quote t) / (1 + r_base t).
    """
    return spot * (1 + r_quote * t) / (1 + r_base * t)


def unhedged_foreign_return(local_return: float, fx_change: float) -> float:
    """Home-currency return: (1 + r_local)(1 + fx_change) - 1, fx_change = % change in
    the home value of one unit of foreign currency."""
    return (1 + local_return) * (1 + fx_change) - 1


# --------------------------------------------------------------------------
# Options
# --------------------------------------------------------------------------

def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def norm_pdf(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def norm_ppf(p: float) -> float:
    """Inverse standard normal CDF (bisection; adequate for textbook precision)."""
    if not 0 < p < 1:
        raise ValueError("p must be in (0,1)")
    lo, hi = -12.0, 12.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if norm_cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def call_payoff(s: float, k: float) -> float:
    return max(s - k, 0.0)


def put_payoff(s: float, k: float) -> float:
    return max(k - s, 0.0)


def _d1_d2(s, k, t, r, sigma, q=0.0):
    d1 = (math.log(s / k) + (r - q + 0.5 * sigma ** 2) * t) / (sigma * math.sqrt(t))
    return d1, d1 - sigma * math.sqrt(t)


def bs_price(s: float, k: float, t: float, r: float, sigma: float, kind: str = "call", q: float = 0.0) -> float:
    """Black-Scholes-Merton price, continuous r and dividend yield q."""
    d1, d2 = _d1_d2(s, k, t, r, sigma, q)
    if kind == "call":
        return s * math.exp(-q * t) * norm_cdf(d1) - k * math.exp(-r * t) * norm_cdf(d2)
    return k * math.exp(-r * t) * norm_cdf(-d2) - s * math.exp(-q * t) * norm_cdf(-d1)


def bs_delta(s, k, t, r, sigma, kind="call", q=0.0):
    d1, _ = _d1_d2(s, k, t, r, sigma, q)
    return math.exp(-q * t) * (norm_cdf(d1) if kind == "call" else norm_cdf(d1) - 1.0)


def bs_gamma(s, k, t, r, sigma, q=0.0):
    d1, _ = _d1_d2(s, k, t, r, sigma, q)
    return math.exp(-q * t) * norm_pdf(d1) / (s * sigma * math.sqrt(t))


def bs_vega(s, k, t, r, sigma, q=0.0):
    """Price change per 1.00 (100 vol points) change in sigma; divide by 100 for per-vol-point."""
    d1, _ = _d1_d2(s, k, t, r, sigma, q)
    return s * math.exp(-q * t) * norm_pdf(d1) * math.sqrt(t)


def delta_gamma_pnl(delta: float, gamma: float, ds: float) -> float:
    """Taylor approximation of option P&L: delta dS + 0.5 gamma dS^2."""
    return delta * ds + 0.5 * gamma * ds ** 2


def put_call_parity_gap(call: float, put: float, s: float, k: float, t: float, r: float, q: float = 0.0) -> float:
    """C - P - (S e^{-qt} - K e^{-rt}); zero under no-arbitrage."""
    return call - put - (s * math.exp(-q * t) - k * math.exp(-r * t))
