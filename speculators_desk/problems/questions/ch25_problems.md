# Chapter 25 Problems — The Speculator's Desk

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch25_solutions.md`. Numerical answers are verified in `tests/test_ch25_examples.py`.
All positions, prices, probabilities, and likelihood ratios are hypothetical [HYPOTHESIS] unless cited.

---

### Problem 25.1 (Level 1) — Grading sources
For each item, name the source type from §25.6.2, grade it on reliability, bias, and "already widely known", and say whether it could support an *informational* edge, a *risk-management* use, or neither.

(a) A payroll figure released at the scheduled time.
(b) A seller-prepared T-12 for a hotel you are bidding on.
(c) A lender's verbal indication that it is cutting hotel proceeds from 60% to 50% LTV next month.
(d) A weekly COT report showing leveraged funds at their largest net short in 10-year note futures in two years.
(e) A brokerage quarterly report stating that "investor appetite for industrial remains strong".

### Problem 25.2 (Level 2) — COT arithmetic and lag
In the Traders in Financial Futures report for a Treasury futures contract, Leveraged Funds hold 182,400 long and 96,900 short contracts. Open interest is 612,000. Last week's leveraged-fund net position was +71,200.
(a) Compute the net position, the weekly change, and the net position as a percentage of open interest.
(b) The report describes positions as of which day's close, and when is it normally released?
(c) A federal holiday delays release to Monday. How many calendar days old are the positions on the day of release?

### Problem 25.3 (Level 2) — Brier arithmetic
(a) A forecast of 0.8 for an event that occurs; (b) a forecast of 0.8 for an event that does not occur. Give each Brier contribution.
(c) What Brier score does a forecaster who always says 0.5 obtain, whatever happens?
(d) Ten events, eight of which occur. Forecaster X says 0.95 for all ten, and forecaster Y says 0.8 for all ten. Compute both Brier scores. Which is better, and why?

### Problem 25.4 (Level 3) — Weekly P&L attribution
Your book last week:
* Long 20 10-year note futures, DV01 \$82 per contract. The 10-year yield fell 8 bp.
* Short 6 ES contracts, \$50 multiplier, from 5,900 to 5,841 (−1.0%).
* Long \$1,500,000 REIT basket, beta 1.2 to ES, actual return −0.4%.
* Long €1,000,000 against USD: EUR/USD from 1.0850 to 1.0790.
* Costs \$1,100.

(a) Compute the P&L of each position. (b) Attribute total P&L to rates, equity beta, REIT idiosyncratic, FX, and costs, and check that the terms sum to the total. (c) What does the attribution say about the equity hedge?

### Problem 25.5 (Level 3) — Aggregating a risk register
Capital is \$50 million. Positions:
* Long \$8,000,000 face of a 10-year, 4.20% semiannual note priced at par (yield 4.20%).
* Short 30 10-year note futures, DV01 \$85 per contract.
* Long 4 ES at 5,800 (\$50 multiplier) and a \$3,000,000 REIT basket with beta 1.2.
* An apartment property worth \$40,000,000 at a 5.50% cap, with a \$26,000,000 loan.

(a) Book DV01 (P&L per +1 bp), using `fi.dv01` for the note. (b) Beta-adjusted equity delta. (c) CRE equity at risk if the cap rate rises to 6.25% with NOI flat, and the percentage change in property equity. (d) The joint stress of rates +40 bp, equities −12%, and the cap shock in (c), in dollars and as a percentage of capital. (e) Which line dominates?

### Problem 25.6 (Level 3) — Calibration review
Thirty journal forecasts: ten at 0.8 (six occurred), ten at 0.6 (six occurred), ten at 0.2 (three occurred).
(a) Compute the Brier score. (b) Compute the skill score against the base rate. (c) Compute the reliability and resolution terms, and verify the decomposition. (d) Which bin is miscalibrated, and in which direction?

### Problem 25.7 (Level 3) — Time budget
A 50-hour week. Twenty-six hours are fixed (meetings, administration, the routine of §25.5). The other 24 hours are now spent as follows, with your estimates of the probability $\pi$ that one hour changes a decision and the value $v$ of the change:

| Activity | Hours now | $\pi$ per hour | $v$ |
|---|---|---|---|
| A. Sell-side morning notes | 5 | 1.0% | \$40,000 |
| B. Lender calls for term sheets | 3 | 5.0% | \$150,000 |
| C. Rebuilding T-12 normalizations | 6 | 8.0% | \$120,000 |
| D. Watching screens intraday | 10 | 0.5% | \$60,000 |

(a) Value per hour of each activity and the weekly total now.
(b) Move 8 hours out of D and 2 out of A. Give 4 to B and 6 to C. Compute the new weekly total and the gain.
(c) Suppose C has diminishing returns: hours beyond the eighth are worth half as much per hour. Recompute (b).
(d) What would you log to test whether these estimates are right?

### Problem 25.8 (Level 4) — Conflicting signals on a hotel acquisition
Hypothesis $H$: "Submarket hotel RevPAR declines over the next 12 months." Prior 0.35. Signals and your likelihood ratios:
* Your own two hotels' operating statements show RevPAR −4% year over year (LR 1.8).
* A sell-side note says "stable" (LR 0.8).
* Lender term sheets cut hotel proceeds (LR 1.6).
* An industry report shows national RevPAR declining (LR 1.4).

Your bid is acceptable only if $P(H) \le 0.45$.
(a) Compute the posterior treating all signals as independent.
(b) Recompute it assuming the lender and the industry report react to the same national data, so that the pair counts as one signal with LR 1.6.
(c) Decide: bid, re-price, gather information, or pass. Give a rubric-style justification, including what information would change your answer.

### Problem 25.9 (Level 4) — Postmortem
Your decision record for a hotel acquisition stated two scenarios: Good, p = 0.7, profit +\$2.0m; Bad, p = 0.3, loss −\$1.5m. You also wrote "P(Good) = 0.70" in the journal. The outcome was a loss of \$1.8m.
(a) Compute the ex-ante EV and the break-even probability of the Bad state.
(b) The realized loss exceeded the Bad scenario. Recompute the EV and break-even with $L = \$1.8$m. Would the decision have changed?
(c) Give the Brier contribution of the journal forecast.
(d) Write the postmortem's process grades. State which part of the decision, probability or severity, failed, and what single rule you would change.

### Problem 25.10 (Level 5) — Into the CPI print
It is Tuesday. A colleague proposes shorting 60 10-year note futures (DV01 \$85 each) before Wednesday's CPI, with invalidation 12 bp below entry and a target of 20 bp. The per-trade limit is \$100,000 (0.25% of \$40 million). You assume a CPI-day gap of 25 bp is plausible. The evidence: prior 0.50 that yields rise 20 bp before falling 25 bp; a widely circulated sell-side preview calls for a hot print (LR 1.2); the COT shows a record leveraged-fund net short, which raises squeeze risk (LR 0.8); your own reading of shelter components points up (LR 1.3).
(a) Compute the loss at invalidation, the gap loss, and the maximum size within the limit under the gap.
(b) Compute the posterior and the break-even probability using the gap loss as $L$ and the target as $G$ (both in bp).
(c) Decide what to do, and write the trade ticket's decision field. Include what would change your answer.
