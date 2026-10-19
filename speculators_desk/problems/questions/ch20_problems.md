# Chapter 20 Problems — Probability and Statistical Decision-Making

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch20_solutions.md`. Numerical answers are verified in `tests/test_ch20_examples.py`.
All facts are hypothetical [HYPOTHESIS] unless cited. Money is in \$ millions unless stated.

---

### Problem 20.1 (Level 1) — Concepts
(a) A forecaster states the base rate (say 45%) on every question. What are its reliability, resolution, and Brier skill score? Why is it nonetheless "perfectly calibrated"?
(b) Explain in two sentences why the expected value of sample information is zero for a study whose every possible result leaves the decision unchanged, however accurate the study is.
(c) Give one reason why the sample excess kurtosis of ten years of monthly returns is a poor guide to tail risk.
(d) When is minimax regret a better rule than expected value, and what property of the rule should make you cautious?

### Problem 20.2 (Level 2) — Base rates, mentally
One industrial building in ten in a submarket has a roof needing replacement within three years. A drone roof survey detects such roofs 90% of the time and flags 10% of sound roofs. The survey on your building comes back flagged. Without a calculator, what is the probability that the roof needs replacement? Give the odds-form calculation.

### Problem 20.3 (Level 2) — Normal versus fat tails
A hotel REIT has monthly volatility of 5% and mean zero. (a) Under a normal model, how likely is a month worse than −15%, and how many such months should a 30-year (360-month) history contain? (b) A variance-matched Student-t with 4 degrees of freedom gives $P = 0.006618$ for the same threshold. How many months in 360? What is the ratio to the normal?

### Problem 20.4 (Level 3) — Confidence interval for a hotel portfolio's mean return
A hotel owner-operator reports annual total returns for eight years: 18%, 9%, −22%, 25%, 11%, 4%, −8%, 14%.
(a) Compute the mean, sample standard deviation, standard error, and 95% t-interval for the mean ($t_{0.975,7} = 2.365$).
(b) Compute the geometric mean.
(c) If the series has lag-1 autocorrelation 0.3, compute the effective sample size and the normal-approximation 95% half-width.
(d) How many i.i.d. years would be needed for a ±2% half-width at the sample volatility?
(e) The owner says the record proves a 6% annual return. Respond.

### Problem 20.5 (Level 3) — A calibration table
An asset-management team forecast the probability that each of 40 leases would renew. Results:

| Stated probability | Count | Renewals |
|---|---|---|
| 0.20 | 10 | 1 |
| 0.40 | 10 | 3 |
| 0.60 | 10 | 7 |
| 0.80 | 10 | 9 |

(a) Compute the Brier score (use `sdesk.stats.brier_score` on the expanded lists), REL, RES, UNC, and the Brier skill score.
(b) Is the team over- or underconfident? 
(c) What would the Brier score have been if the team had stated 0.10, 0.30, 0.70, 0.90 for the same four groups?
(d) What is the Brier score of a forecaster who said 0.50 every time?

### Problem 20.6 (Level 3) — Model averaging for an exit cap rate
Two models forecast the exit cap rate on an apartment asset with forward NOI of \$3.0 million. $M_1$ (reversion to the long-run spread): $c \sim N(5.75\%, 0.40\%)$. $M_2$ (higher-rate regime): $c \sim N(6.50\%, 0.50\%)$. Prior weights are 0.5 each. The most recent comparable trade printed at 6.25%; use the density each model assigns to 6.25% as its likelihood.
(a) Compute the posterior weights.
(b) Compute the BMA mean and standard deviation of the exit cap.
(c) The refinancing fails if the exit cap exceeds 6.75%. Compute that probability under $M_1$, $M_2$, and BMA.
(d) Compute value at each model's mean cap, at the BMA mean cap, and the model-weighted average of the two model values. Explain the difference between the last two.

### Problem 20.7 (Level 4) — Should you buy the market study?
A sponsor offers you an LP position in a lease-up. If absorption is fast (prior 0.60), your profit is +1.5; if slow (0.40), −1.8. Passing yields 0.
(a) Compute the prior decision, its EV, and EVPI.
(b) An independent market study costs \$75,000. It reports "favorable" with probability 0.80 when absorption will be fast and 0.30 when slow. Compute the posterior after each report, the optimal action after each, EVSI, and the expected net gain of the study.
(c) The sponsor offers instead its own consultant's study, free. That consultant reports "favorable" 80% of the time when fast and 70% of the time when slow. Compute EVSI. Would you pay \$75,000 for it?
(d) Explain why the two studies have the same sensitivity but very different value.

### Problem 20.8 (Level 4) — CRRA and sizing a hotel bet
Wealth \$12.0 million. Bills return 10% cumulatively over the hold. A hotel equity commitment of \$3.0 million returns multiples 1.8 (probability 0.45), 1.1 (0.35), or 0.2 (0.20). The rest of wealth is in bills.
(a) Compute terminal wealth in each state, $E[W]$, and the riskless alternative.
(b) Compute the certainty equivalent for $\gamma = 2$ and $\gamma = 4$. Accept or reject the \$3.0 million commitment in each case.
(c) For each $\gamma$, find (to the nearest \$10,000) the commitment that maximizes the CE and the largest commitment with CE at least equal to the riskless alternative.
(d) The sponsor argues that because the expected multiple (1.235) exceeds bills (1.10), "any rational investor should take as much as possible." Respond.

### Problem 20.9 (Level 4) — Coherent scenarios and a decision without trusted probabilities
For a grocery-anchored center, the analyst writes: $P(A) = 0.25$ (the anchor leaves within two years), $P(B) = 0.40$ (a refinancing gap at maturity), $P(B\mid A) = 0.80$, and, in a separate table, $P(A\cap B) = 0.15$.
(a) Show that the quotes are incoherent.
(b) Construct a Dutch book against the analyst using a claim on $A\cap B$, a conditional claim on $B$ given $A$ (called off with the price refunded if $A$ does not occur), and a claim on $A$. What is the sure profit per \$1?
(c) Using $P(A)$, $P(B\mid A)$, and $P(B)$, build the coherent joint table and compute $P(B\mid\neg A)$.
(d) Three actions with payoffs by cell ($A\cap B$, $A\cap\neg B$, $\neg A\cap B$, $\neg A\cap\neg B$): Hold $H = (-4.0, -1.5, -2.0, +2.5)$; extend the loan early and pre-lease the anchor box $X = (-1.0, -0.5, -0.5, +1.2)$; sell now $S = (0, 0, 0, 0)$. Compute expected values under the coherent table, the regret table, and the minimax-regret action.
(e) Which action would you recommend, and what would change your mind?

### Problem 20.10 (Level 5) — The track record with missing projects (decision exercise, §20.9)
A sponsor asks for a \$4.0 million commitment from your \$20.0 million vehicle to a \$50.0 million multifamily development with a stabilized value of \$56.0 million. Its deck shows six completed developments, all within 3% of budget (mean overrun 2.0%). Its pro forma uses a 2% overrun. You learn informally that four further projects were transferred to lenders or recapitalized. The sponsor declines to provide files for them, calling them "legacy deals with a former partner". Your internal past correlation between sponsor cost forecasts and outcomes is $r = 0.3$.
(a) Compute the full-record mean overrun if the four missing projects overran by 25% on average, and again at 15%. Apply the regressive adjustment to each.
(b) Compute the adjusted expected profit in each case and compare it with the sponsor's.
(c) Can you compute a CRRA certainty equivalent for the commitment? If not, what is missing?
(d) What information has the highest value, and how would you obtain it?
(e) Decide: commit (with size), commit conditionally, or abstain. Your answer is graded with the rubric in §20.9.
