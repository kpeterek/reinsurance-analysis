# Chapter 5 Problems — Central Banks and Monetary Policy

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch05_solutions.md`. Numerical answers are verified in `tests/test_ch05_examples.py`.
All market levels and deal facts are hypothetical [HYPOTHESIS] unless cited. Administered-rate settings, where used, are those of the 16 September 2026 implementation note (chapter §5.4.1).

---

### Problem 5.1 (Level 1) — The corridor
(a) Explain why the Federal Reserve can keep the effective federal funds rate inside its target range without changing the quantity of reserves day to day. Name the role of IORB, the ON RRP, the SRF, and the primary credit rate.
(b) EFFR has printed 2 bp *above* IORB for two weeks while the range is unchanged. Give two explanations, and say what each implies for the Fed's balance-sheet policy.
(c) Why does a floating-rate CRE borrower care about (b) even if the FOMC never changes the target range?

### Problem 5.2 (Level 2) — Reading a clean contract
The FOMC meets in the last days of month M. The contract for month M+1, which has no meeting, trades at 96.18. EFFR is 3.88% today. The only alternatives at the meeting are hold and a 25 bp cut. Without a calculator: (a) what average rate does M+1 imply, and (b) what is the implied probability of a cut? (c) What is a one-basis-point move in this contract worth per contract?

### Problem 5.3 (Level 2) — Fisher, exactly
The 10-year nominal Treasury yields 4.50% and the 10-year breakeven is 2.30%. Give the approximate real yield, then the exact one implied by the Fisher relation. Why might the TIPS yield differ from both?

### Problem 5.4 (Level 3) — A rule band
Core PCE inflation is 2.6%, headline PCE inflation 3.2%, and the output gap +0.5%. Take $r^* = 1.0\%$ and a 2% target.
(a) Compute the Taylor (1993) prescription using core inflation.
(b) Compute the balanced-approach prescription using core inflation.
(c) Compute the Taylor (1993) prescription using headline inflation.
(d) The target range midpoint is 3.875%. Compute the inertial next-step rate with $\rho = 0.8$ using (a).
(e) In two sentences, what does the spread between (b) and (c) tell an underwriter of floating-rate debt?

### Problem 5.5 (Level 3) — Day-weighting, and when it fails
A 31-day month has a meeting whose decision takes effect on day 18, so 17 days are at the old rate. EFFR is 3.88%. The meeting-month contract trades at 96.07.
(a) Compute the implied post-meeting EFFR and the probability of a 25 bp hike, assuming hold or hike are the only outcomes.
(b) Compute the naive probability that ignores day-weighting.
(c) Now suppose the outcomes are hold, +25 bp, or +50 bp. Can you recover three probabilities from this contract? What additional information would you need?

### Problem 5.6 (Level 3) — Floating debt service and a cap
A hotel with NOI of \$4,000,000 has a \$45,000,000 interest-only loan at SOFR + 3.50% (actual/360), with a rate cap struck at 4.25%.
(a) Compute annual interest and DSCR at SOFR of 3.85%.
(b) Repeat at SOFR of 4.35% unhedged.
(c) Repeat at SOFR of 4.35% with the cap.
(d) Compute the annual cap payout at SOFR of 4.35%.

### Problem 5.7 (Level 3) — Fixed refinance proceeds
An apartment property has NOI of \$1,800,000. A lender sizes 30-year amortizing loans at the lesser of 60% LTV, 1.30x DSCR, and a 9.0% debt yield. The appraisal cap rate is 6.25%.
(a) The 10-year Treasury is 4.30% and the lender spread is 1.80%. Compute the loan constant, each constraint, and the maximum loan.
(b) The 10-year rises 50 bp and the spread widens 15 bp. Repeat (a) with the appraisal unchanged.
(c) Two quarters later the appraiser moves the cap rate to 6.75%. Recompute the LTV constraint and the maximum loan.
(d) Explain why the rate shock in (b) did not change proceeds, and why (c) did.

### Problem 5.8 (Level 4) — Term premium and a bid
You are bidding on an apartment building with NOI of \$2,000,000 after reserves. The seller's broker quotes a 5.50% cap rate. Since the broker's comparable sales closed, the 10-year has risen 25 bp. Your desk attributes the rise entirely to a higher term premium during heavy Treasury issuance [HYPOTHESIS]. Your cap-rate pass-through estimate ranges from $\beta = 0.5$ to $\beta = 1.0$.
(a) Compute value at 5.50%, and at the cap rates implied by $\beta = 0.5$ and $\beta = 1.0$.
(b) The seller will not accept less than \$36.0 million. Decide whether to bid, at what price, and on what conditions. Use the rubric in the solutions.

### Problem 5.9 (Level 4) — Underwriting to whose path?
You are buying a hotel with NOI of \$2,200,000 financed with a \$25,000,000 interest-only floating loan at SOFR + 3.00% (actual/360). The loan has a 1.15x DSCR cash-sweep covenant. Average SOFR over the first year is 3.60% under the futures-implied path, 3.35% under your house view (one more cut than the market), and 3.88% if no cuts occur.
(a) Compute interest and DSCR under each path.
(b) Compute the SOFR at which the cash sweep is triggered.
(c) The sponsor asks you to underwrite the house view because "we have a better read on the Fed." Respond in one paragraph, using the rubric in the solutions.

### Problem 5.10 (Level 5) — Conflicting inflation signals
In the same month: the one-year household inflation expectation in a major consumer survey rises by 0.8 percentage points; the 5-year breakeven falls 15 bp; the 5y5y forward breakeven is unchanged; oil fell 12% over the month; and two FOMC participants give speeches with opposite emphases. A colleague proposes a large position in fed funds futures for the next meeting, and separately proposes accelerating a floating-rate acquisition so that it closes before "the Fed turns hawkish."
(a) Give at least two competing explanations for the divergence between the survey and the breakeven.
(b) For each proposal, state whether you would act, and why.
(c) Name the data that would change your view.
This problem has no single correct answer. See the rubric.
