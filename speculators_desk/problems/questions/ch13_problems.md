# Chapter 13 Problems — CRE Trading and Portfolio Strategy

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch13_solutions.md`. Numerical answers are verified in `tests/test_ch13_examples.py`.
All facts are hypothetical [HYPOTHESIS] unless cited.

---

### Problem 13.1 (Level 1) — What is sunk, and what is not
An owner bought an apartment building in 2018 for \$30.0m with \$12.0m of equity. It is now worth \$44.0m, and the since-inception levered IRR is 19%. The loan carries a 3.9% fixed rate that cannot be assumed by a buyer, with a yield-maintenance prepayment provision.
(a) Which of the following belong in a hold–sell decision today: the 2018 price, the \$12.0m of original equity, the 19% since-inception IRR, the current bid, the yield-maintenance cost, the 3.9% coupon, and the owner's tax basis? Explain each in one sentence.
(b) The asset manager argues: "We've made 19% a year on this deal. Why would we sell a winner?" Rewrite the argument so that it addresses the decision.

### Problem 13.2 (Level 2) — Cap rates and implied growth
Without a calculator:
(a) A stabilized industrial asset trades at a 5.25% cap rate. Investors require an 8.00% unlevered return. What long-run NOI growth rate does the price imply?
(b) If the cap rate falls to 4.75% with NOI unchanged, by roughly what percentage does value rise? Give the exact figure too.
(c) A colleague says, "At 4.75% the asset is priced for 3.25% growth." Under what assumption is that statement true?

### Problem 13.3 (Level 2) — Futures hedge arithmetic
A borrower's pipeline has a DV01 of \$36,000. The 10-year T-note futures DV01 is \$80 per contract.
(a) How many contracts should be shorted?
(b) At lock, Treasuries are 20 bp higher and the lender's spread is unchanged. What are the loan PV cost, the hedge P&L, and the net?
(c) Same, but the spread also widens 15 bp.

### Problem 13.4 (Level 3) — Hold or sell an industrial asset
Forward NOI \$1,000,000, growing 2.5% a year. Bid today \$18,000,000. Selling costs 2.0% (today and at exit). Loan \$9,000,000, interest-only at 5.00%, prepayable at par with no penalty. A four-year hold would exit at a 6.00% cap on year-5 NOI. The best reinvestment alternative at the same leverage and risk earns a levered 8.50% after its own acquisition costs.
(a) Compute equity at market.
(b) Compute the hold cash flows and the hold IRR.
(c) Compute the break-even exit cap rate.
(d) Recommend, and state what would change the recommendation.

### Problem 13.5 (Level 3) — Two-market correlation
A portfolio holds 60% (by value) in a market with 10% value volatility and 40% in a market with 18% volatility.
(a) Compute portfolio volatility at correlations 0.3, 0.8, and 1.0 using $\sigma_p^2 = \sum\sum w_iw_j\sigma_i\sigma_j\rho_{ij}$.
(b) Historical data estimate the correlation at 0.3. In the last two downturns, the two markets' values fell together. Which number would you use for sizing a liquidity reserve, and why?
(c) The equity is 40% of gross value. What is equity volatility at each correlation?

### Problem 13.6 (Level 3) — One-step option to build
A completed building would be worth \$20.0m today. Construction costs \$18.5m now or next year (no escalation). Next year the completed value is either \$25.0m or \$16.0m ($u = 1.25$, $d = 0.80$). The risk-free rate is 5.0%. The stabilized NOI yield is 6.0%.
(a) Compute the risk-neutral probability $q$.
(b) Compute the NPV of building now, the value of the option to wait, and the value of waiting.
(c) What NOI yield $\delta$ would make building now and waiting equally valuable? Interpret.

### Problem 13.7 (Level 4) — Liquidity reserve with a maturity
A partnership owns an office building (NOI \$3.0m, debt service \$2.4m, loan \$25.0m maturing at the end of year 2) and a multifamily asset (NOI \$1.5m, debt service \$1.0m, long-term debt). Stress scenario: office NOI −20% in year 1 and −35% in year 2, when a tenant leaves; tenant improvements and leasing commissions of \$1.5m are paid in year 2. Multifamily NOI −5% in both years. At maturity a new lender will lend 50% of the office value, measured as year-2 NOI capitalized at 9.0%.
(a) Compute net cash flow in each year and the maturity gap.
(b) Compute the reserve required.
(c) Compute the annual opportunity cost at a 4.5% reserve yield and a 10.0% target return.
(d) List three alternatives to holding the reserve in cash and the information you would need to compare them. **Rubric required.**

### Problem 13.8 (Level 4) — Refinance or not
An apartment building is worth \$30.0m. The existing loan of \$15.0m carries 3.90% interest-only, four years to maturity. Yield maintenance today would cost \$0.4m. A lender offers \$18.0m (60% LTV), interest-only at 6.25%, four years, with 1.0% fees.
(a) Compute the cash released.
(b) Compute the marginal cost of the cash-out.
(c) The sponsor wants the cash to fund a 15% expected-return development equity investment. Should it refinance? What alternatives should it price? **Rubric required.**

### Problem 13.9 (Level 5) — Is the spread a signal?
An analyst brings you a "relative-value" trade: overweight suburban office relative to multifamily. The office–multifamily cap-rate spread is 330 bp. The analyst's six annual observations of the spread are 180, 170, 200, 320, 310, 300 bp. The first three are from a broker survey; the last three are from closed transactions in a database that includes distressed sales. The current 330 bp figure is from the broker survey.
(a) Compute the z-score of 330 bp against all six observations and against the last three only.
(b) What would you need to know before acting?
(c) Write your recommendation. **Rubric required.** (Consider whether the best answer is to take no position.)

### Problem 13.10 (Level 5) — Hedging a pipeline that may not close
A buyer has a \$40m, 7-year, interest-only, monthly-pay fixed-rate loan to lock in three months. The expected rate is 6.25%. The probability that the acquisition closes is 70%. Futures DV01 is \$80 per contract [HYPOTHESIS].
(a) Compute the loan DV01 with `fi.dv01(0.0625, 0.0625, 7, face=40_000_000, freq=12)` and the full-hedge and probability-weighted contract counts.
(b) For each hedge size, compute net P&L for Treasury moves of +40 bp and −40 bp, with the deal closing or failing. Spreads are unchanged.
(c) Compute the expected P&L of each hedge in the +40 bp scenario.
(d) Recommend a hedge, or no hedge, and name the instrument. **Rubric required.**
