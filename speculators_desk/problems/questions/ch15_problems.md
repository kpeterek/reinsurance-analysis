# Chapter 15 Problems — Foreign Exchange

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch15_solutions.md`. Numerical answers are verified in `tests/test_ch15_examples.py`.
All market data are hypothetical [HYPOTHESIS] unless cited. Pairs are BASE/QUOTE: 1 BASE costs $S$ QUOTE.

---

### Problem 15.1 (Level 1) — Quote direction
(a) For a U.S. investor, which of EUR/USD, USD/JPY, GBP/USD and USD/CHF are direct quotes?
(b) USD/JPY rises from 150 to 155. Which currency appreciated? Is this good or bad for a U.S. owner of a Tokyo office building, measured in dollars? For a Japanese owner of a Dallas hotel, measured in yen?
(c) A colleague writes "EUR/USD rose 5%, so the dollar fell 5% against the euro." Correct the statement.
(d) Why is P&L on a EUR/USD position earned in dollars, and what rate should be used to report a USD/JPY position's P&L in dollars?

### Problem 15.2 (Level 2) — Mental arithmetic
GBP/USD moves from 1.2500 to 1.2000. Without a calculator give: (a) the percentage change of sterling in dollars; (b) the percentage change of the dollar in sterling; (c) the pips moved; (d) the P&L in dollars on a **short** £5,000,000 position.

### Problem 15.3 (Level 2) — Cross rates
Quotes: AUD/USD 0.6600/0.6604; USD/JPY 150.00/150.04; EUR/USD 1.0850/1.0854; USD/CHF 0.8800/0.8804.
Compute the synthetic two-way prices for (a) AUD/JPY and (b) EUR/CHF. State which leg's bid or ask you used for each side and why.

### Problem 15.4 (Level 3) — CIP with day counts, and which way to arbitrage
Spot USD/JPY 150.00. 90-day rates: USD 4.30% (ACT/360), JPY 0.40% (use ACT/365 for this problem).
(a) Compute the 90-day CIP forward and the forward points (JPY pips are 0.01).
(b) Express the forward premium as an annualized rate on a 360-day basis.
(c) A dealer quotes the 90-day outright at 148.80. Describe the arbitrage leg by leg and compute the profit at maturity per \$10,000,000, ignoring the dealer's spread and balance-sheet costs.
(d) Name two reasons why such a gap might persist.

### Problem 15.5 (Level 3) — AUD/JPY carry decomposition
Long A\$10,000,000 of AUD/JPY at 99.00 for six months (accrual 0.5), funded in yen at 0.50% and invested in AUD at 4.10%. Margin is 10% of the yen notional. At expiry AUD/JPY is 92.00.
(a) Compute the P&L in yen and decompose it into carry, spot, and cross terms.
(b) Return on margin.
(c) The break-even AUD/JPY at expiry, and the P&L if spot is unchanged.

### Problem 15.6 (Level 3) — First-generation attack timing
A peg is defended with \$24 billion of reserves, which a credit-financed deficit drains at \$1.5 billion per month. In the linear model of §15.4.9, $\alpha = 4$ months.
(a) Naive exhaustion date and attack date. Reserves lost on the attack day.
(b) The government arranges a \$6 billion credit line (treated as reserves). New attack date?
(c) Instead, money demand becomes more interest-sensitive, $\alpha = 8$. New attack date?
(d) What does (b) versus (c) suggest about which indicators an investor should monitor?

### Problem 15.7 (Level 4) — A euro insurer's rolling hedge on a U.S. office
A German insurer buys a U.S. office building for \$66,000,000, all cash, at EUR/USD 1.10. NOI is \$3,630,000 a year (5.5% cap), paid at year-end. It sells \$66,000,000 forward against euros for one year and rolls annually. Rates stay at USD 4.00% and EUR 2.00% (accrual 1.0). Year-end spots: 1.00 at year 1, 1.05 at year 2.
(a) The forward at inception and at the first roll.
(b) The euro settlement at each year-end. (A euro-based seller of dollars forward at $F$ receives $N/F$ euros and delivers dollars worth $N/S_T$ euros.)
(c) Year-1 settlement as a share of initial euro equity. How much of it does the year-1 NOI (converted at spot) cover?
(d) The unrealized euro gain on the building in year 1 at an unchanged dollar value.
(e) Recommend a hedging structure for the remaining hold. **Rubric required.**

### Problem 15.8 (Level 4) — Hedge ratio when the asset and currency move together
A U.S. fund owns a foreign logistics portfolio: equity \$20,000,000. Local equity return volatility 15%, currency volatility 10%, correlation +0.30 (the asset and the currency fall together in downturns). The liquidity reserve is \$1,500,000 and policy limits a 2σ roll call to the reserve.
(a) Minimum-variance hedge ratio.
(b) Liquidity-constrained maximum.
(c) Volatility at $h$ = 0, $h_{liq}$, 1.00, and $h^*$.
(d) Policy caps hedge ratios at 1.00. What do you recommend, and what else would you do? **Rubric required.**

### Problem 15.9 (Level 4) — Should the central bank defend?
An emerging-market central bank pegs at 25.0 local units per dollar. Its overnight rate is 20%; the dollar rate is 5%. Speculators consider a one-month short of the local currency. If the peg breaks the currency falls 15% (measured in dollars); if it holds it bounces 0.5%.
(a) The speculator's one-month carry cost and break-even devaluation probability.
(b) The interest differential needed to deter a speculator who puts $p = 40\%$, annualized, and the implied overnight rate.
(c) The bank has sold \$20 billion of reserves at 25.0. If it devalues to 40.0 and later rebuys the dollars, what is its loss in local currency and in dollars at the new rate?
(d) Advise the governor: defend, devalue, or something else? **Rubric required.**

### Problem 15.10 (Level 5) — The pegged-currency hotel
A developer offers a stabilized hotel in Country P at an 11% local-currency yield (NOI after reserve, all cash). Country P's currency has been pegged to the dollar for eight years. Your notes, gathered quickly:

* The non-deliverable forward (NDF) market implies the local currency trades at a 9% annual forward discount to the dollar; the market is thin beyond one year.
* Official reserves fell for six straight months; you do not know the level of short-term external debt.
* The current-account deficit is about 6% of GDP. A large share of local bank deposits is held by non-residents (exact share unknown).
* One-year U.S. Treasury bills yield 4.25%.
* The developer says the peg "has never been in doubt".

(a) Compute the hedged dollar yield (one year, using the NDF discount).
(b) If you go unhedged and assign a 30% probability to a 35% devaluation within the year (otherwise no change), compute the expected dollar return.
(c) Compute the devaluation probability at which the unhedged expected return equals the T-bill yield, holding the 35% devaluation size.
(d) What would you do, and what information would change your answer? **Rubric required.**
