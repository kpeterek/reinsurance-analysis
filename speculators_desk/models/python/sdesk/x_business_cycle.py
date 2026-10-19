"""Business-cycle arithmetic for Chapter 4 (The Business Cycle).

Conventions follow the notation guide: rates and growth rates are decimals,
unemployment rates are entered in percent *points* (4.1 means 4.1%) because
that is how the BLS publishes them and how the Sahm rule threshold (0.50
percentage point) is stated. Every function documents its units.

Functions
---------
annualize_quarterly      (1 + q)^4 - 1, the BEA "SAAR" growth convention
quarterly_from_annualized inverse of the above
simple_annualized        4q, the approximation that the BEA does NOT use
yoy_growth               level_t / level_{t-4} - 1 on quarterly data
contributions            percentage-point contributions to GDP growth
moving_average           trailing k-period simple average
sahm_indicator           Sahm (2019) real-time recession indicator series
sahm_first_trigger       first index at which the indicator is >= threshold
net_percentage           SLOOS-style net percentage of respondents tightening
standardized_surprise    (actual - consensus) / sigma
lease_rollover_noi       first-year NOI change for a leased property

For hotel operating leverage use ``sdesk.cre.operating_leverage``.
"""

from __future__ import annotations

from typing import Sequence


# --------------------------------------------------------------------------
# Growth-rate conventions
# --------------------------------------------------------------------------

def annualize_quarterly(q: float) -> float:
    """Compound annual rate from a quarter-on-quarter growth rate q (decimal).

    BEA reports quarterly real GDP growth as (1 + q)^4 - 1, "at an annual rate".
    Excel: =(1+q)^4-1
    """
    return (1.0 + q) ** 4 - 1.0


def quarterly_from_annualized(a: float) -> float:
    """Quarter-on-quarter rate implied by an annualized rate a: (1 + a)^(1/4) - 1."""
    return (1.0 + a) ** 0.25 - 1.0


def simple_annualized(q: float) -> float:
    """4 x q. An approximation; understates positive and overstates negative growth."""
    return 4.0 * q


def yoy_growth(levels: Sequence[float], t: int, lag: int = 4) -> float:
    """Year-over-year growth on quarterly levels: levels[t] / levels[t-lag] - 1."""
    return levels[t] / levels[t - lag] - 1.0


# --------------------------------------------------------------------------
# Expenditure identity
# --------------------------------------------------------------------------

def contributions(prev: dict, curr: dict) -> dict:
    """Contribution of each expenditure component to GDP growth (decimal).

    GDP = C + I + G + NX. Contribution_i = (X_i,t - X_i,t-1) / GDP_t-1, so the
    contributions sum exactly to GDP growth. Components may be any keys; the
    GDP total is the sum of the values (NX enters with its own sign).
    """
    gdp0 = sum(prev.values())
    gdp1 = sum(curr.values())
    out = {k: (curr[k] - prev[k]) / gdp0 for k in prev}
    out["gdp_growth"] = gdp1 / gdp0 - 1.0
    out["gdp0"], out["gdp1"] = gdp0, gdp1
    return out


# --------------------------------------------------------------------------
# Sahm rule
# --------------------------------------------------------------------------

def moving_average(x: Sequence[float], k: int = 3) -> list:
    """Trailing k-period simple average; None for the first k-1 positions."""
    out: list = []
    for i in range(len(x)):
        out.append(None if i < k - 1 else sum(x[i - k + 1:i + 1]) / k)
    return out


def sahm_indicator(unrate: Sequence[float], window: int = 12, include_current: bool = False) -> list:
    """Sahm recession indicator, in percentage points.

    S_t = MA3(u)_t - min{MA3(u)_s : s in the previous ``window`` months}.
    Following the FRED SAHMREALTIME notes, the minimum is taken over the three-
    month averages of the previous 12 months (``include_current=False``).
    Returns None where a full window of prior averages is not available.
    The recession signal is S_t >= 0.50.
    """
    ma = moving_average(unrate, 3)
    out: list = []
    for t in range(len(unrate)):
        lo_idx = t - window
        hi_idx = t + 1 if include_current else t
        if ma[t] is None or lo_idx < 0 or ma[lo_idx] is None:
            out.append(None)
            continue
        prior = [m for m in ma[lo_idx:hi_idx] if m is not None]
        out.append(ma[t] - min(prior))
    return out


def sahm_first_trigger(indicator: Sequence, threshold: float = 0.50, tol: float = 1e-9):
    """Index of the first month with indicator >= threshold, or None."""
    for i, v in enumerate(indicator):
        if v is not None and v >= threshold - tol:
            return i
    return None


# --------------------------------------------------------------------------
# Surveys and surprises
# --------------------------------------------------------------------------

def net_percentage(tightened_considerably: int, tightened_somewhat: int,
                   eased_somewhat: int, eased_considerably: int, respondents: int) -> float:
    """SLOOS net percentage (decimal): share tightening minus share easing.

    "Considerably" and "somewhat" are combined, as in the Federal Reserve's
    published net-percentage series. Respondents include "basically unchanged".
    """
    return ((tightened_considerably + tightened_somewhat)
            - (eased_somewhat + eased_considerably)) / respondents


def standardized_surprise(actual: float, consensus: float, sigma: float) -> float:
    """(actual - consensus) / sigma, in units of the historical surprise s.d."""
    return (actual - consensus) / sigma


# --------------------------------------------------------------------------
# Transmission to NOI
# --------------------------------------------------------------------------

def lease_rollover_noi(revenue: float, opex: float, share_rolling: float,
                       market_rent_change: float, renewal_prob: float,
                       downtime_months: float, occupancy_change: float = 0.0) -> dict:
    """First-year NOI change for a leased property (office, industrial, retail).

    Only ``share_rolling`` of revenue reprices in the year. Of that share,
    a fraction ``renewal_prob`` renews at the new market rent with no downtime;
    the rest re-lease at market after ``downtime_months`` of zero rent.
    Leases are assumed to roll at the start of the year (a conservative, front-
    loaded simplification). ``occupancy_change`` (decimal of revenue) is any
    additional vacancy outside the rollover. Operating expenses are fixed.
    """
    rolling = revenue * share_rolling
    renew = rolling * renewal_prob * (1 + market_rent_change)
    relet = rolling * (1 - renewal_prob) * (1 + market_rent_change) * (12 - downtime_months) / 12
    rev1 = revenue - rolling + renew + relet + revenue * occupancy_change
    noi0 = revenue - opex
    noi1 = rev1 - opex
    return {"rev1": rev1, "noi0": noi0, "noi1": noi1,
            "rev_change": rev1 / revenue - 1.0, "pct_change": noi1 / noi0 - 1.0}
