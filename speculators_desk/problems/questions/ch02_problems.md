# Chapter 2 Problems — The Price Formation Process

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch02_solutions.md`. Numerical answers are verified in `tests/test_ch02_examples.py`.
All facts are hypothetical [HYPOTHESIS] unless cited.

---

### Problem 2.1 (Level 1) — Forms of efficiency
(a) State the weak, semi-strong, and strong forms of market efficiency in terms of information sets. Which implies which?
(b) An analyst says: "Private CRE is inefficient, so anyone who does the work will earn excess returns." Use the Grossman–Stiglitz argument to say what is right and wrong in this statement.
(c) Listed apartment REITs imply a 5.6% cap rate; appraisals of similar properties show 4.3%. For each form of efficiency, say what the gap would imply if that form held for the REIT market. Then give two reasons the gap can persist even if the REIT market is semi-strong efficient.

### Problem 2.2 (Level 2) — Unsmoothing in your head
An appraisal index reported +1.0% last quarter and −1.0% this quarter.
(a) With $a = 0.5$, what market return does the Geltner filter imply for this quarter?
(b) With $a = 0.8$?
(c) What does the difference tell you about how much weight to place on an unsmoothed number?

### Problem 2.3 (Level 2) — A payrolls surprise
Consensus for nonfarm payrolls is +180,000. The release prints +120,000. The standard deviation of past surprises is 75,000. The 10-year yield responds 5 bp per one-standard-deviation surprise, in the same direction as the surprise. The 10-year note's modified duration is 8.0.
(a) Compute the standardized surprise, the expected yield change, and the price change (duration only).
(b) Traders were positioned for +100,000. Recompute (a) using positioning as the expectation. Which direction would you expect yields to move, and why might a headline writer call the move "puzzling"?

### Problem 2.4 (Level 3) — Clearing a call auction
Opening auction orders for a REIT (thousands of shares):

| Buy limit (\$) | Qty | Sell limit (\$) | Qty |
|---|---|---|---|
| 25.30 | 15 | 25.05 | 20 |
| 25.25 | 25 | 25.10 | 30 |
| 25.20 | 30 | 25.15 | 35 |
| 25.15 | 40 | 25.20 | 40 |
| 25.10 | 50 | 25.25 | 50 |

(a) Build the cumulative demand and supply schedules and find the clearing price, volume, and imbalance.
(b) An index fund adds a market *buy* order for 60 thousand shares. Recompute.
(c) Compute the price impact per thousand shares, and explain why an informed trader might prefer to submit a limit order instead.

### Problem 2.5 (Level 3) — Roll's estimator and round-trip costs
Ten consecutive trade prices for a thinly traded preferred share (efficient price unchanged; the true spread is \$0.20 around \$41.20):

41.10, 41.30, 41.10, 41.30, 41.30, 41.10, 41.30, 41.10, 41.10, 41.30

(a) Compute the price changes, the sample autocovariance (divisor $n-1$, each vector demeaned by its own mean), and Roll's spread estimate in dollars and as a percentage of \$41.20.
(b) Why does the estimate differ from \$0.20?
(c) A private industrial building costs a buyer 2.0% and a seller 3.0%. Compute the round-trip cost and the geometric annual drag over a 5-year hold.
(d) For a different security, the autocovariance of price changes is +0.0012. What is Roll's estimate, and what does the result tell you?

### Problem 2.6 (Level 3) — Unsmoothing a quarterly series
Appraisal appreciation returns, quarter 0 to quarter 6: +1.5%, +1.0%, 0.0%, −1.0%, −1.5%, −1.5%, −1.2%.
(a) With $a = 0.7$, compute unsmoothed returns for quarters 1–6.
(b) Compute the cumulative change over quarters 1–6 for the appraisal and unsmoothed series.
(c) Compute the mean lag and the volatility ratio implied by $a = 0.7$.
(d) Repeat (a)–(b) with $a = 0.5$. Does your conclusion about the size of the decline depend on $a$? What would you report to an investment committee?

### Problem 2.7 (Level 4) — Who sets the price of an industrial building?
A distribution building has NOI after reserves of \$4,000,000. Bidders:

* **F1**, core-plus fund: \$30.0m of equity; loan max 60% LTV, min 1.35x DSCR, interest-only.
* **F2**, merchant buyer: \$18.5m of equity with a 75% LTV bridge loan.
* **F3**, pension separate account, unlevered, 5.50% cap.
* **F4**, REIT, unlevered, 5.75% cap.
* **F5**, private all-cash buyer, 6.00% cap.

(a) With F1's interest rate at 4.75%, compute every reservation price and the ascending-auction clearing price. Who is marginal? What is the implied cap rate?
(b) Rates rise: F1's rate becomes 7.25% and bridge lending stops (F2 exits). Recompute. By what percentage does the clearing price fall? What is the new implied cap rate?
(c) The seller's reserve is \$72.0 million (loan payoff plus costs). Does a trade occur after the rate rise, and at what price?
(d) F3's investment committee then raises its cap-rate hurdle to 5.75%. What happens? What would you observe in transaction data, and what would an appraiser using the last sale as a comp conclude?

### Problem 2.8 (Level 4) — Redeeming at a stale NAV
An open-end fund reports NAV of \$100 per unit, based on appraisals. Your estimate of the market value of its assets is \$88 per unit. Investors holding 12% of units have requested redemption. Ignore fund leverage and costs.
(a) If redemptions are paid at \$100 by selling assets at market value, what is the value per unit of the remaining investors' holdings? What is the percentage transfer from the remaining investors?
(b) What does a redeeming investor gain relative to market value?
(c) Suppose instead the fund marks NAV down 15% (to \$85) before paying. Recompute the remaining investors' value per unit.
(d) You hold \$25 million of units. Decide whether to submit a redemption request and what you would do with the proceeds. Give a rubric for your decision.

### Problem 2.9 (Level 4) — Cleaning a comp set
A Class B, 1990s suburban apartment property has NOI after reserves of \$2,400,000. Five comps (cap rates on in-place NOI after reserves); the market value index now stands at 90:

| Comp | Months ago | Cap rate | Index at sale | Class / note |
|---|---|---|---|---|
| K1 | 14 | 4.60% | 102 | A |
| K2 | 10 | 4.85% | 99 | A |
| K3 | 6 | 6.10% | 95 | B+, sold by a lender after foreclosure (REO) |
| K4 | 3 | 5.40% | 92 | A |
| K5 | 1 | 5.60% | 90.5 | B |

Assume a Class B premium of 30 bp over Class A.
(a) Compute the naive average cap rate (all five) and the implied value.
(b) Time-adjust every comp to today.
(c) Decide which comps to use and justify excluding any. Convert Class A comps to Class B equivalents, and give a point estimate and range for the subject.
(d) The time index is built from transactions. In which direction is it likely to be biased now, and how should that change your bid?

### Problem 2.10 (Level 5) — A hotel in a market that does not print
A 132-room select-service hotel is offered in a secondary market. Facts:
* The seller's appraisal, dated 10 months ago, is \$19.5 million. Trailing-12 NOI after a 4% FF&E reserve is \$1.62 million.
* Two hotel sales have closed in the market in the last 18 months: one at a 7.9% cap 16 months ago (newer, different brand) and one at a 9.6% cap 3 months ago (older, sold by a lender).
* Listed lodging REITs are down 22% over the year. The broker says "REITs are irrelevant to a select-service deal."
* STR data for the last three months show RevPAR down 6% for the competitive set, but the seller's management reports RevPAR up 2% for the subject. The two reports have not been reconciled.
* The brand's franchise agreement expires in 26 months; no PIP estimate has been provided.
* You must indicate a price within five business days.

Write a one-page memo: bid, pass, or decline to price until specified information arrives. State (a) what each price source tells you and what it does not; (b) the three facts that would most change your value, ranked; (c) your recommendation and its conditions.
