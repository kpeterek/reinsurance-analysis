# Chapter 14 Problems — Equities and Equity Index Futures

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch14_solutions.md`. Numerical answers are verified in `tests/test_ch14_examples.py`.
All inputs are hypothetical [HYPOTHESIS] unless cited. Contract multipliers: CME E-mini S&P 500 \$50 per point, Micro E-mini \$5 per point, tick 0.25 points (ch14-S01, S02).

---

### Problem 14.1 (Level 1) — Earnings yield, cap rate, and expected return
(a) A hotel C-corporation and a private hotel portfolio own similar hotels. The company's earnings yield is 4.5% and the private cap rate is 7.5%. Give three reasons the two yields can differ without any mispricing.
(b) Under what condition is a stock's earnings yield equal to its expected return? Why is that return approximately real rather than nominal?
(c) Why is "earnings yield minus the nominal 10-year Treasury yield" not an equity risk premium?

### Problem 14.2 (Level 2) — Multipliers and ticks
A trader sells 3 Micro E-mini S&P 500 contracts at 5,900.00 and buys them back at 5,860.25.
(a) What is the P&L?
(b) What would the P&L have been if the trader had mistakenly traded 3 E-minis?
(c) How many ticks did the price move, and what is the P&L computed from ticks?
(d) What was the notional of the original Micro position?

### Problem 14.3 (Level 2) — From EV/EBITDA to a cap rate
A lodging company trades at 12.5x EV/EBITDA. Its EBITDA margin is 30% of total revenue, and the FF&E reserve is 4% of total revenue. What cap rate on NOI after reserve does the multiple imply? If comparable private hotels trade at a 7.50% cap on the same NOI definition, is the public market paying more or less for the hotels?

### Problem 14.4 (Level 3) — Fair value and the arbitrage band
S&P 500 spot 5,500. Financing rate 4.00% and dividend yield 1.50%, both continuously compounded. Six months to expiry. Round-trip arbitrage costs total 4 index points.
(a) Compute the fair futures price.
(b) The future trades at 5,585.00. Describe the arbitrage and compute the profit per E-mini contract after costs.
(c) The future trades instead at 5,560.00. Describe the arbitrage, compute the profit per contract after costs, and say who can actually perform it.

### Problem 14.5 (Level 3) — Two-stage implied return
Index at 5,000. Next-year cash distributions 3.40% of price ($CF_1 = 170$ points), growing 8% a year through year 5, then 3.5% forever. The 10-year Treasury yields 4.00%.
(a) Solve for the implied return and ERP.
(b) Compute the Gordon return and ERP with $g = 3.5\%$ from year 1.
(c) Explain the difference and which assumption you would stress first.

### Problem 14.6 (Level 3) — An earnings beat that lowers the price
A REIT-adjacent hotel management company reports quarterly EPS of \$1.32 against a consensus of \$1.20. The standard deviation of its past surprises is \$0.05. Before the report the stock is \$60.00 on forward EPS of \$2.40. After the call, analysts raise forward EPS by 4%, but the company signals slower unit growth and the forward P/E falls to 23x.
(a) Compute the SUE.
(b) Compute the forward P/E before the report, the new forward EPS, and the new price.
(c) Reconcile a large positive surprise with a price decline. What does post-earnings-announcement drift suggest about the days after?

### Problem 14.7 (Level 3) — Breadth and momentum
A five-stock index has market caps (\$bn) of 3,000, 2,500, 800, 400 and 300, and one-year returns of +25%, +18%, −6%, −10% and −12%.
(a) Compute the cap-weighted and equal-weighted returns, advancers and decliners, and the contribution of the two largest stocks.
(b) The index's last 12 monthly returns are +2.0%, −1.0%, +3.0%, +1.0%, −4.0%, +2.0%, +1.5%, −2.0%, +1.0%, +3.0%, −1.5%, +1.0%. Its annualized volatility is 20% and your target is 10%. Give the time-series momentum signal and position weight.
(c) What do (a) and (b) together imply for a REIT investor who hedges with S&P 500 futures?

### Problem 14.8 (Level 4) — The hard-to-borrow short
A PM proposes shorting 50,000 shares of a travel-technology stock at \$30.00. The borrow fee is 25% a year. Horizon six months. Initial margin 50%, maintenance 30%. Her scenarios for six months out: −40% (p = 0.45), flat (p = 0.25), +60% (p = 0.30). Assume the fee accrues on the initial position value, and ignore the rebate and dividends.
(a) Compute the borrow cost, the scenario P&L, and the EV.
(b) At what price is a margin call triggered?
(c) Recommend. Use the rubric in the solutions.

### Problem 14.9 (Level 4) — Hedging a REIT sleeve over a four-month window
A \$25 million REIT sleeve has a beta of 0.85 to the S&P 500. The E-mini trades at 5,600. The office expects to need the cash in four months for a private acquisition. The ERP is 3.0%.
(a) How many contracts hedge the beta?
(b) What is the expected cost of the hedge over four months?
(c) If the index rallies 10%, what is the variation-margin outflow on the hedge (use 76 contracts)?
(d) Recommend whether to hedge, sell the REITs now, or do nothing, and state what evidence would change the answer.

### Problem 14.10 (Level 5) — Public cap rates, private marks, and a redemption queue
You manage an open-end private hotel fund. One asset has forward NOI after reserve of \$18 million and is appraised at a 7.00% cap with 55% LTV debt based on the appraised value. A listed lodging REIT with similar hotels trades at \$11.00; 150 million shares; debt \$1.9 billion; cash \$0.1 billion; no preferred and no other assets; forward NOI \$270 million. Limited partners have submitted redemption requests equal to 8% of NAV. Private hotel transaction volume in your markets fell sharply this year; you have two broker opinions of value but no closed comparable.
(a) Compute the REIT's implied cap rate, NAV per share at 7.00%, and discount.
(b) Revalue your asset at the REIT's implied cap. What happens to its equity value?
(c) The information is incomplete. Decide what the fund should do about (i) its marks, (ii) the redemption queue, and (iii) any REIT position, and say what you would need to know. Abstention from a REIT trade is an acceptable answer if justified.
