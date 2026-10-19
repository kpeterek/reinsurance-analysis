# Chapter 18 Problems — Derivatives, Volatility, and Convexity

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch18_solutions.md`. Numerical answers are verified in `tests/test_ch18_examples.py`.
All facts are hypothetical [HYPOTHESIS] unless cited. Rates in Black–Scholes problems are continuously compounded.

---

### Problem 18.1 (Level 1) — Which contract, which risk?
For each hedge, name the instrument (forward, futures, swap, option, cap), say whether the hedger is long or short convexity, and name the main residual risk (basis, counterparty, margin/liquidity, or premium/theta).

(a) A hotel owner fixes the rate on a \$30 million floating loan for five years with a bank.
(b) The same owner instead buys a five-year cap at 5.00% on the index.
(c) A REIT fund shorts E-mini S&P 500 futures against a portfolio of apartment REITs.
(d) A U.S. investor agrees with a bank to sell €20 million in 12 months at a fixed rate to hedge the sale proceeds of a German logistics asset.
(e) A family office buys three-month index puts struck 10% out of the money.
(f) A volatility-income fund sells one-month index puts.

### Problem 18.2 (Level 2) — Mental arithmetic
Without a calculator (a calculator check is fine afterwards):
(a) $S = K = 100$, $r = 5\%$, $q = 0$, $T = 1$. What is $C - P$?
(b) An option trades at 16% implied vol. What daily move, in percent, does a delta-hedged long position need to break even? Use 252 trading days.
(c) $S = 100$, $r = 5\%$, $q = 2\%$, $T = 1$. What is the forward price?

### Problem 18.3 (Level 2) — Delta-gamma P&L
You are long 10 call contracts, each on 100 shares. Each option has delta 0.55 and gamma 0.03. The stock rises \$4 in a day. Implied vol and the passage of time are ignored. Estimate the P&L.

### Problem 18.4 (Level 3) — Pricing and Greeks
$S = 50$, $K = 52$, $T = 0.5$, $r = 4.5\%$, $q = 0$, $\sigma = 30\%$.
(a) Price the European call and put.
(b) Verify put–call parity.
(c) Compute call and put delta, the common gamma, vega per vol point, and call and put theta per calendar day.
(d) Explain why the call's theta is more negative than the put's.

### Problem 18.5 (Level 3) — Implied versus realized
A three-month at-the-money call ($S = K = 80$, $T = 0.25$, $r = 4\%$, $q = 0$) trades at 4.10.
(a) Find implied vol.
(b) You expect realized vol of 22% over the life of the option. Using the vega approximation, estimate the expected P&L per unit of a delta-hedged long position, and for 50 contracts of 100 shares.
(c) Name two reasons the realized P&L could differ from (b) even if realized vol is exactly 22%.

### Problem 18.6 (Level 3) — Valuing a seasoned swap
A borrower pays fixed at 3.50% and receives floating on \$30,000,000 under a swap with three remaining annual payments at $t = 0.5$, 1.5 and 2.5 years. Each accrual is 1.0. The floating rate for the next payment was fixed six months ago at 4.20%. Discount factors: $P(0.5) = 0.9800$, $P(1.5) = 0.9420$, $P(2.5) = 0.9050$.
(a) Value the fixed leg, the floating leg and the swap to the borrower.
(b) The borrower is selling the property. What does it receive or pay to terminate, before dealer spread?

### Problem 18.7 (Level 3) — Cap pricing and sensitivities
A \$25,000,000 two-year cap with quarterly caplets, first period excluded, flat forward SOFR 3.80%, discounting on the same flat forward compounded quarterly (the `x_capital_structure.cap_premium` convention). Normal model.
(a) Price the cap at a 4.00% strike and 0.90% normal vol. Give \$, % of notional and annual bp.
(b) Reprice at 1.20% vol.
(c) Reprice at a 5.00% strike and 0.90% vol.
(d) The lender requires a cap at 4.00% or lower. The sponsor's model assumed 0.90% vol. The dealer quotes 1.20%. How much extra equity is needed at closing?

### Problem 18.8 (Level 4) — The tail-hedge mandate
An endowment with \$200 million in global equities is considering one of two rolling quarterly put programs: (i) 95% strike at 20% implied vol, or (ii) 80% strike at 28% implied vol. $r = 4\%$, $q = 1.5\%$. Assume steady-state rolling.
(a) Compute each program's premium per roll (per 100 of spot) and annual cost.
(b) Compute the ten-year multiplicative drag of program (i) if it never pays.
(c) For a 35% fall within one quarter, compute each program's payoff as a percentage of the portfolio, and the break-even annual frequency of such a fall.
(d) The endowment has no leverage, no capital calls and a 5% spending rule. Recommend one, both or neither, and say what would change your recommendation.

Your answer is graded with the rubric in the solutions.

### Problem 18.9 (Level 4) — Asset substitution in a hotel loan
A hotel is worth \$30,000,000. The loan is a \$30,000,000 balloon due in two years. As in Example 18.9, interest paid from NOI is ignored on both sides, $r = 4\%$. The sponsor proposes converting part of the hotel to extended-stay. You estimate the conversion raises asset vol from 15% to 30% with no change in expected value.
(a) Compute equity, the lender's put, debt value, credit spread and risk-neutral PD at both vols.
(b) How much value moves from lender to sponsor?
(c) Repeat (a) at $V = \$36{,}000{,}000$. Is the transfer larger or smaller? Why?
(d) You are the lender. What would you ask for in exchange for consent?

### Problem 18.10 (Level 5) — The volatility-income pitch
A manager describes the following strategy. Each month it sells index puts struck 10% out of the money with one month to expiry. "Notional is about five times NAV." The deck shows 24 consecutive positive months, about +1% per month, and a Sharpe ratio above 3. The manager will not disclose positions, and the audited statements cover only the most recent year. Use $S = 100$, $K = 90$, $T = 1/12$, $r = 4\%$, $q = 1.5\%$ and 20% implied vol to reconstruct the premium.

(a) Compute the premium per 100 of notional, the monthly premium income as a percentage of NAV at 5× notional, and its annualized compounding.
(b) Is 1% a month consistent with the stated terms? If not, list what would have to differ.
(c) Compute the NAV loss in a month in which the index falls 25%, at 5× notional and at the leverage implied by 1% a month.
(d) Decide: invest, invest a sized amount, or decline. State what information would change your answer.

Your answer is graded with the rubric in the solutions. Abstention is a legitimate answer.
