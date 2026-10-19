"""Time value of money: rates, annuities, loan amortization, NPV and IRR.

Excel equivalents are given in each docstring. Remember that Excel's PMT/PV/FV
return values with the opposite sign of the principal; the Python functions
here return positive payment amounts.
"""

from __future__ import annotations

from datetime import date
from typing import Sequence


# --------------------------------------------------------------------------
# Rate conversions
# --------------------------------------------------------------------------

def effective_annual_rate(nominal_rate: float, periods_per_year: int) -> float:
    """Effective annual rate from a nominal annual rate compounded m times.

    EAR = (1 + j/m)^m - 1.      Excel: =EFFECT(j, m)
    """
    m = periods_per_year
    return (1.0 + nominal_rate / m) ** m - 1.0


def nominal_rate(effective_rate: float, periods_per_year: int) -> float:
    """Nominal annual rate (compounded m times) equivalent to an effective rate.

    j = m * ((1 + EAR)^(1/m) - 1).      Excel: =NOMINAL(EAR, m)
    """
    m = periods_per_year
    return m * ((1.0 + effective_rate) ** (1.0 / m) - 1.0)


def periodic_rate_from_effective(effective_rate: float, periods_per_year: int) -> float:
    """Per-period rate equivalent to an effective annual rate."""
    return (1.0 + effective_rate) ** (1.0 / periods_per_year) - 1.0


# --------------------------------------------------------------------------
# Annuities and loans
# --------------------------------------------------------------------------

def annuity_factor(rate: float, n: int) -> float:
    """Present value of 1 per period for n periods, paid in arrears."""
    if n <= 0:
        return 0.0
    if rate == 0:
        return float(n)
    return (1.0 - (1.0 + rate) ** (-n)) / rate


def payment(principal: float, annual_rate: float, amort_years: float,
            periods_per_year: int = 12) -> float:
    """Level payment per period on a fully amortizing loan (end of period).

    Uses nominal annual rate / periods_per_year as the periodic rate, which is
    how U.S. commercial mortgages quote rates.

    Excel: =PMT(annual_rate/12, amort_years*12, -principal)
    """
    n = int(round(amort_years * periods_per_year))
    i = annual_rate / periods_per_year
    if i == 0:
        return principal / n
    return principal * i / (1.0 - (1.0 + i) ** (-n))


def annual_debt_service(principal: float, annual_rate: float, amort_years: float | None,
                        periods_per_year: int = 12, interest_only: bool = False) -> float:
    """Annual debt service. Interest-only if ``interest_only`` or amort is None.

    For interest-only loans this is principal * annual_rate (nominal, simple sum of
    periodic interest payments).
    """
    if interest_only or amort_years is None:
        return principal * annual_rate
    return payment(principal, annual_rate, amort_years, periods_per_year) * periods_per_year


def loan_constant(annual_rate: float, amort_years: float, periods_per_year: int = 12) -> float:
    """Annual debt service per dollar of principal (the 'mortgage constant')."""
    return annual_debt_service(1.0, annual_rate, amort_years, periods_per_year)


def loan_balance(principal: float, annual_rate: float, amort_years: float,
                 periods_elapsed: int, periods_per_year: int = 12) -> float:
    """Outstanding balance after ``periods_elapsed`` payments (closed form).

    B_k = P(1+i)^k - PMT * [((1+i)^k - 1)/i]
    Equivalent: PV of remaining payments at the loan rate.

    Excel: =-FV(rate/12, k, -PMT, principal)   (or =PV(rate/12, n-k, -PMT))
    """
    i = annual_rate / periods_per_year
    pmt = payment(principal, annual_rate, amort_years, periods_per_year)
    k = periods_elapsed
    if i == 0:
        return principal - pmt * k
    growth = (1.0 + i) ** k
    return principal * growth - pmt * (growth - 1.0) / i


def amortization_schedule(principal: float, annual_rate: float, amort_years: float,
                          periods: int | None = None, periods_per_year: int = 12,
                          io_periods: int = 0) -> list[dict]:
    """Period-by-period schedule. Optional initial interest-only periods.

    Returns list of dicts with keys: period, begin, payment, interest, principal, end.
    When io_periods > 0, amortization over ``amort_years`` starts after the IO period.
    """
    i = annual_rate / periods_per_year
    n_amort = int(round(amort_years * periods_per_year))
    total = periods if periods is not None else io_periods + n_amort
    amort_pmt = payment(principal, annual_rate, amort_years, periods_per_year)
    rows = []
    bal = principal
    for t in range(1, total + 1):
        interest = bal * i
        if t <= io_periods:
            pmt = interest
        else:
            pmt = amort_pmt
        princ = pmt - interest
        end = bal - princ
        rows.append({"period": t, "begin": bal, "payment": pmt, "interest": interest,
                     "principal": princ, "end": end})
        bal = end
    return rows


# --------------------------------------------------------------------------
# Discounting
# --------------------------------------------------------------------------

def pv(amount: float, rate: float, t: float) -> float:
    """Present value of a single amount received at time t."""
    return amount / (1.0 + rate) ** t


def fv(amount: float, rate: float, t: float) -> float:
    """Future value of a single amount."""
    return amount * (1.0 + rate) ** t


def npv(rate: float, cashflows: Sequence[float]) -> float:
    """NPV with cashflows[0] at t=0 (NOT discounted).

    Excel: =CF0 + NPV(rate, CF1:CFn)   -- Excel's NPV discounts its first argument.
    """
    return sum(cf / (1.0 + rate) ** t for t, cf in enumerate(cashflows))


def irr(cashflows: Sequence[float], lo: float = -0.9999, hi: float = 10.0,
        tol: float = 1e-12, max_iter: int = 500) -> float:
    """Periodic IRR by bisection (robust; requires a sign change of NPV on [lo, hi]).

    Excel: =IRR(CF0:CFn)
    Raises ValueError if no sign change is found (e.g., all flows the same sign).
    """
    f_lo, f_hi = npv(lo, cashflows), npv(hi, cashflows)
    if f_lo * f_hi > 0:
        raise ValueError("NPV does not change sign on the search interval; IRR undefined or not unique here")
    for _ in range(max_iter):
        mid = 0.5 * (lo + hi)
        f_mid = npv(mid, cashflows)
        if abs(f_mid) < tol or (hi - lo) < tol:
            return mid
        if f_lo * f_mid < 0:
            hi, f_hi = mid, f_mid
        else:
            lo, f_lo = mid, f_mid
    return 0.5 * (lo + hi)


def xnpv(rate: float, cashflows: Sequence[float], dates: Sequence[date]) -> float:
    """NPV with actual dates, Actual/365 year fractions from the first date.

    Excel: =XNPV(rate, values, dates)
    """
    d0 = dates[0]
    return sum(cf / (1.0 + rate) ** ((d - d0).days / 365.0) for cf, d in zip(cashflows, dates))


def xirr(cashflows: Sequence[float], dates: Sequence[date]) -> float:
    """IRR for irregularly timed flows (Actual/365). Excel: =XIRR(values, dates)"""
    lo, hi = -0.9999, 10.0
    f_lo, f_hi = xnpv(lo, cashflows, dates), xnpv(hi, cashflows, dates)
    if f_lo * f_hi > 0:
        raise ValueError("XNPV does not change sign on the search interval")
    for _ in range(500):
        mid = 0.5 * (lo + hi)
        f_mid = xnpv(mid, cashflows, dates)
        if abs(f_mid) < 1e-10 or hi - lo < 1e-13:
            return mid
        if f_lo * f_mid < 0:
            hi = mid
        else:
            lo, f_lo = mid, f_mid
    return 0.5 * (lo + hi)


def equity_multiple(cashflows: Sequence[float]) -> float:
    """Total distributions / total contributions."""
    inflow = sum(cf for cf in cashflows if cf > 0)
    outflow = -sum(cf for cf in cashflows if cf < 0)
    return inflow / outflow


def annualize_periodic(rate: float, periods_per_year: int) -> float:
    """Compound a periodic return to an annual effective return."""
    return (1.0 + rate) ** periods_per_year - 1.0
