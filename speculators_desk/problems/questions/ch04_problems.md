# Chapter 4 Problems — The Business Cycle

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch04_solutions.md`. Numerical answers are verified in `tests/test_ch04_examples.py`.
All data are hypothetical [HYPOTHESIS] unless a source is cited.

---

### Problem 4.1 (Level 1) — Reading the expenditure identity
(a) A news report says: "Imports surged last quarter, subtracting 1.2 points from GDP." Explain what is right and what is misleading about this statement.
(b) Real GDP grew at a 3.5% annualized rate in a quarter in which inventory investment contributed 2.4 points. What does that tell you about the next quarter?
(c) Explain, using the accelerator mechanism, why gross private domestic investment, about a sixth of GDP, can account for most of the decline in a recession.
(d) Why does year-over-year growth lag turning points, and by roughly how much?

### Problem 4.2 (Level 2) — Annualization
Without a spreadsheet:
(a) Quarter-on-quarter real GDP growth is +0.8%. What is the annualized rate?
(b) Quarter-on-quarter growth is −0.4%. What is the annualized rate?
(c) The BEA reports +2.4% annualized. What was the quarter-on-quarter growth?
(d) YoY growth is +1.0% and the latest quarter was −2.0% annualized. What was cumulative growth over the three quarters before the latest one?

### Problem 4.3 (Level 2) — Contributions
GDP shares at the start of the year are: consumption 68%, investment 17%, government 17%, net exports −2%. Over the year consumption grows 1%, investment falls 9%, government grows 2%, and net exports are unchanged in dollars.
(a) Compute each contribution in percentage points and GDP growth.
(b) What investment decline, with the other components unchanged, would leave GDP growth at exactly zero?

### Problem 4.4 (Level 3) — Sahm rule by hand, and a revision
Monthly unemployment rates (%), months 1–18:

| Month | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| $u$ | 4.0 | 3.9 | 3.9 | 3.8 | 3.9 | 3.9 | 3.9 | 4.0 | 4.0 |

| Month | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|
| $u$ | 4.1 | 4.1 | 4.2 | 4.2 | 4.3 | 4.4 | 4.4 | 4.5 | 4.6 |

(a) Compute the three-month averages for months 3–18.
(b) Compute the Sahm indicator for months 15–18 using the minimum of the previous 12 months' three-month averages.
(c) In which month does the rule first signal?
(d) The annual seasonal revision changes month 4 from 3.8 to 3.9. Recompute months 16 and 17. When does the rule now signal?
(e) What does (d) imply for a fund that has written "reduce hotel exposure when the Sahm rule triggers" into its investment policy?

### Problem 4.5 (Level 3) — Productivity, unit labor costs and a hotel
(a) Nonfarm business output grows 1.2% and hours grow 1.5%. Hourly compensation grows 4.0%. Compute productivity growth and unit-labor-cost growth (exact, not additive).
(b) A full-service hotel has revenue of \$20.0 million, labor costs of \$6.8 million, and other costs of \$7.6 million that are fixed in dollars, so NOI is \$5.6 million (28.0% margin). Next year ADR rises 1% with occupancy flat, wages rise 4% and labor hours are unchanged. Compute next year's NOI, its percentage change, the labor ratio and the NOI margin.
(c) What does (a) suggest about the inflation pressure the central bank faces, and what does (b) suggest about underwriting hotels late in a cycle?

### Problem 4.6 (Level 3) — Two signals and a base rate
Your prior probability that a recession begins within 12–18 months is 12%. The 10y–3m curve inverts; assume $P(Inv\mid R) = 0.85$ and $P(Inv\mid \bar R) = 0.15$.
(a) Compute the posterior.
(b) Six months later the Sahm rule signals. Assume $P(Sahm\mid R) = 0.80$ and $P(Sahm \mid \bar R) = 0.05$, and treat the two signals as conditionally independent. Update again.
(c) Give the likelihood ratio of each signal. Which is more informative, and why does that make sense given what each indicator measures?
(d) Why might the conditional-independence assumption be wrong, and in which direction would the error bias your answer?
(e) If the curve's false-positive rate is 15% per non-recession year, how many false signals would you expect over 40 non-recession years? What does this imply about the size of the historical sample used to estimate that rate?

### Problem 4.7 (Level 3) — An inflation surprise and loan proceeds
Core CPI rises 0.4% month over month against a consensus of 0.3%. The historical standard deviation of core CPI surprises is 0.08 point. Assume a 5-year Treasury sensitivity of +5 bp per $1\sigma$ surprise.
(a) Compute $z$ and the expected move in the 5-year Treasury.
(b) A borrower is about to fix a \$40 million five-year loan priced off the 5-year Treasury. What is the change in annual interest cost?
(c) A different lender sizes a loan on a property with NOI of \$3.2 million at a minimum 1.30x DSCR with 30-year amortization. The loan rate was 6.00% before the release and moves one-for-one with the 5-year Treasury. Compute the maximum DSCR-constrained loan before and after the release.
(d) Explain why the same surprise might produce a smaller yield move in a different policy regime.

### Problem 4.8 (Level 4) — A portfolio meets a recession
A fund owns four properties [HYPOTHESIS]:

| Property | Revenue | Costs | Recession shock (first year) |
|---|---|---|---|
| Full-service hotel | \$14.0m | Fixed \$5.0m; variable 33% of revenue (incl. reserve) | Revenue −15% |
| Apartment | \$6.0m | Opex \$2.4m | $\rho = 0.5$; market rent −5%; renewal 55%; 1 month downtime; extra vacancy −1.5% of revenue |
| Office | \$9.0m | Opex \$3.6m | $\rho = 0.10$; market rent −12%; renewal 50%; 9 months downtime |
| Industrial | \$5.0m | Opex \$0.75m | $\rho = 0.125$; market rent −4%; renewal 70%; 4 months downtime |

The hotel has annual debt service of \$2.9 million and a 1.20x DSCR cash-management covenant.
(a) Compute first-year NOI and its percentage change for each property, and the hotel's degree of operating leverage.
(b) Compute portfolio NOI before and after, and the hotel's share of the portfolio NOI decline.
(c) Compute the hotel's DSCR before and after. What NOI keeps it at 1.20x?
(d) The asset manager proposes selling the office "because office is the problem sector" and keeping the hotel. Evaluate using your results and the timing argument of §4.8. (Rubric.)

### Problem 4.9 (Level 4) — SLOOS tightening and an office maturity
In the latest SLOOS, 68 banks responded on nonfarm nonresidential CRE: 9 tightened considerably, 25 somewhat, 32 unchanged, 2 eased somewhat, 0 eased considerably.

You own an office building with NOI of \$3.0 million. Its \$32.0 million loan matures in twelve months. At origination it was sized at 65% LTV on a 6.50% cap-rate value, with minimum 1.25x DSCR at 6.00% (30-year amortization) and a 9.0% minimum debt yield. At maturity you expect: NOI −8%; value at an 8.50% cap rate; maximum LTV 60%; minimum DSCR 1.35x at 7.25% (30-year amortization); minimum debt yield 10.0%.
(a) Compute the net percentage tightening.
(b) Compute the original value and maximum loan, and the binding constraint. (Note that the \$32.0 million loan exceeds the LTV-based maximum; the original lender must have used a higher valuation or LTV. Comment.)
(c) Compute the value and the maximum loan at maturity, the binding constraint, the loan-to-value of the existing loan at the new value, and the refinancing gap.
(d) List the options available (pay down, extension, sale, deed-in-lieu, discounted payoff, rescue capital) and the information you need to choose. Give a recommendation with a rubric.

### Problem 4.10 (Level 5) — Contradictory data and a deadline
It is late in a quarter [HYPOTHESIS]. You are offered a 220-room hotel in a gateway city at a price that equals a 7.6% cap rate on trailing NOI. Bids are due in a week. The data:

* Advance GDP: +2.8% annualized, but inventories contributed +1.9 points and final sales to private domestic purchasers rose 0.6% annualized.
* GDI for the prior quarter: −0.5% annualized; GDP for the same quarter: +1.5%.
* Payrolls: +210,000 vs consensus +160,000; household-survey employment −250,000; unemployment rate up 0.2 to 4.3%; Sahm indicator 0.40.
* 10y–3m spread: re-steepened from −80 bp to −10 bp over three months as markets priced rate cuts.
* SLOOS: net 12% tightening for nonfarm nonresidential CRE, down from net 40% a year earlier.
* The hotel's own STR data: RevPAR index (RGI) 104, flat; market RevPAR −3% YoY for three months. Group pace for next year −8%.
* The seller will provide only twelve months of P&Ls; the property-condition report is "in process".

(a) Classify each item as supporting expansion, supporting recession, or ambiguous, and explain.
(b) What is your recession probability, and how did you get it? State your prior and likelihood ratios. Discuss dependence.
(c) Which piece of missing information would most change your decision, and what would it cost to obtain?
(d) Decide: bid, bid conditionally, or abstain. Justify against the rubric in the solutions. Abstention is an acceptable answer.
