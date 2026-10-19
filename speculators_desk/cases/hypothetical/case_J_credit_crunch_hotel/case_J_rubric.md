# Case J — Instructor Grading Rubric

Keep this file separate from the student version. Numbers are produced by `case_j_model.py` and asserted in `tests/test_case_j.py`. All case inputs are [HYPOTHESIS].

## Mode C — Blind examination (100 points)

| Q | Pts | Full credit | Common deductions |
|---|---|---|---|
| 1 | 5 | Occ 74.50%, ADR \$154.00, RevPAR \$114.73; $N$ = \$1,889,561; −2.35% vs \$1,935,000 | −2 if property tax is deducted from $N$ (the case defines $N$ before tax) |
| 2 | 10 | RGI 110.3 → 111.9 → 114.0; MPI 109.6, ARI 104.1 current. Subject RevPAR +0.37%, comp −1.49%. Interpretation: share gains in a slightly softer market, so no hotel-specific impairment | −3 if RGI is computed as MPI + ARI or from rooms sold. −3 for no interpretation |
| 3 | 10 | 96 rooms: $s$ = 8.81%, demand +5.06%, factor 0.9656, NOI hit \$129,718 (6.86%). With 120 more: $s$ = 19.82%, hit \$464,108 (24.56%). States that the 120-room project is financed in the same world in which the refinancing works | −4 if supply growth uses comp-set rooms only (940) without stating it. −4 for no link between the refinancing and the pipeline |
| 4 | 10 | $P = N/(t + \lambda K + y(1+c-\lambda))$ derived. $\partial(\text{denominator})/\partial\lambda = K - y$. LTV cut lowers price only if $K < y$. Example: at 8.25%, 65% LTV supports \$17,000,237 versus \$17,142,561 at 45% | −5 if the tax is left on the seller's old bill. −3 if closing costs are omitted without saying so |
| 5 | 15 | Normal: REIT \$19.00m, owner-operator \$18.91m, fund \$18.25m, family office \$14.78m (capacity). Clearing \$18,911,969. Crunch: owner-operator \$17.14m, fund \$15.98m, family office \$14.78m, REIT inactive. Clearing \$15,981,461. Marginal buyers named | −5 if the clearing price is the top bid without discussion. −3 if the family office's capacity limit is ignored. −3 if the REIT is left in the crunch universe |
| 6 | 15 | Order A: −444,102 / −318,413 / −1,006,893 / −1,161,100 (total −2,930,508, −15.5%). Order B: financing −2,546,197, fundamentals −384,311. Fundamentals 13–15%. Classifies as a liquidity and buyer-pool discount, conditional on supply | −5 for one order only, with no statement of path dependence. −5 for classifying without the durability tests |
| 7 | 10 | $CE = 0.65 \times 17{,}142{,}561 + 0.35 \times 15{,}378{,}168 = \$16{,}525{,}023$ | −3 if the fallback is not discounted for delay |
| 8 | 10 | Scenario IRRs 17.21 / 15.04 / 12.74 / 10.17 / 7.90%. Expected NPV +\$37,911. Maximum \$16,584,807. Expected IRR 13.79% vs IRR of expected flows 13.08%, with the explanation that IRR is non-linear | −5 for bidding off expected IRR (\$16.86m) without comment |
| 9 | 10 | Seller note: price \$18,129,408; note PV \$2,955,837; seller cash-equivalent \$17,459,363. Assumption: balance \$11,686,551; mark-to-market \$1,838,464; buyer maximum \$18.44m at 13% (\$17.96m at 15%) | −3 if the note is valued at face. −3 if the loan's value ignores the balloon |
| 10 | 5 | Rule with classification tests, NPV criterion, capital-protection test, robustness margin; bid and triggers | −3 for a bid with no walk-away |

Mastery threshold: 85 points, with at least 12/15 on Q6.

## Mode D — Investment committee: model answers and scoring

Score each answer 0–4: 0 missing or wrong; 2 qualitatively correct with no number; 4 quantified, honest about uncertainty, and decision-relevant.

1. **Broker \$19m vs you \$16.55m.** Both are internally consistent answers to different questions. The normal-credit clearing price was \$18.91m (\$126,080/key), so the broker describes the old market correctly. Today's clearing price is \$15.98m. The best financed bid is \$17.14m, but the seller should value it at \$16.53m once closing risk is included. The relevant number is what the seller can get with certainty *today*. A strong answer adds that the broker's "\$19m" assumes a REIT is bidding.
2. **What returns with credit?** The 120-room project. If credit returns in one year *and* both projects open (NOI hit 24.56% of $N$ from year 2), the all-cash plan returns **7.07%**, NPV at 13% **−\$2,011,932**. The refinancing "hedge" and the supply risk are positively correlated. A strong answer proposes to monitor the project's construction-loan status. It also notes that the assumption structure does not remove supply risk; it removes only timing risk.
3. **Why not \$17.2m all-cash?** Expected NPV at \$17.2m is **−\$670,054**, and expected IRR is 12.15%. The only underwriting that supports \$17.2m is the naive "credit returns in a year" case (maximum \$17,815,454). Winning outright means paying for a timing forecast.
4. **Averaged IRR.** It cannot be defended as a pricing criterion. The IRR of probability-weighted flows is 13.08%. The price at which expected NPV at 13% is zero is \$16.58m, while the price at which expected IRR is 13% is \$16.86m. The \$273k gap is an artifact of averaging a non-linear function. Use expected NPV, and report expected IRR only as a description.
5. **Break-even impairment probability.** 26.4% at \$16.55m (others rescaled pro rata), against 15% assumed. A strong answer says what evidence would move it above 26%, for example a T-3 RGI below 105 or a demand-generator loss such as a hospital expansion being cancelled.
6. **Servicer delay or refusal.** The letter carries the all-cash backup, so a refusal reverts to \$16.55m. At an approval probability of 0.70 instead of 0.85, the seller's certainty-equivalent of the assumption bid is still \$17,285,000, above the financed bid's \$16,525,023. A 120-day timeline costs the seller time but does not change the ranking. A strong answer asks for a deposit structure that becomes non-refundable only after approval.
7. **Seller note vs assumption.** On headline cash-equivalents they are nearly equal (\$17,459,363 vs \$17,442,500). But the seller-note bid still depends on a 45% bank loan. Applying the same 0.65 closing probability and fallback gives **\$16,730,945**. The seller also keeps a \$3.6m subordinate exposure. The assumption bid dominates for the seller. Its residual risk is servicer approval, which the backup covers.
8. **What reverses first.** The buyer-universe component (\$1.16m, 39.6%) reverses when lodging REITs can issue equity again: watch REIT price-to-NAV. The rate component (\$1.01m) reverses with credit spreads and bank standards: watch the Senior Loan Officer survey and CMBS hotel spreads. The proceeds component is the smallest (\$0.32m). A strong answer notes that each indicator is observable and dated, so the refinancing plan can be monitored rather than hoped for.
9. **Capital tied up.** \$16,798,250, 67% of the \$25m commitment. In the one-year case, net exposure after refinancing falls to \$4,893,444. In the four-year case the full \$16.8m is committed for four years. With the assumption structure, equity is \$6.29m from day one.
10. **Falling knife?** In 2009 hotel cash flow collapsed with credit: STR reported U.S. RevPAR down 16.7% [FACT, caseJ-S03]. Here NOI is down 2.35%, RGI is rising, and comp RevPAR is down 1.49%. The decomposition attributes 85–87% of the price decline to financing. But these tests are backward-looking. The defense is structural: all-cash at a 9.74% going-in yield returns 7.90% even in the impairment case. A strong answer concedes that a 2009-type demand shock (NOI −30% or worse) is outside the scenario set. It names that as the residual risk, which should be sized at the portfolio level.

Minimum passing committee performance: an average of at least 3.0, with no score of 0 on questions 2, 3, or 4.

## Mode B — Alternative defensible recommendations

* **All-cash only at \$16.55m.** Defensible if the analyst doubts servicer approval or will not take fixed-rate leverage at 66% LTV. The analyst must show that the margin over the seller's alternative (\$25k) and under the maximum (\$35k) is thin, and accept a meaningful probability of losing the deal.
* **Pass.** Defensible if the analyst's evidence puts the impairment probability above 26%, or if the 120-room project is likely to be financed within two years. A strong pass sets a re-engagement trigger, such as the financed bid failing at the lender.
* **Seller-note structure for your own vehicle.** Defensible only if the note rate and subordination are better for the buyer than in B.7. The analyst must compute the seller's cash-equivalent and not present the headline as value.
* **Not defensible:** any all-cash price above \$16.86m (the expected-IRR maximum, itself biased upward) without new information; any bid justified by "replacement cost" or "the pre-crunch comps"; any analysis that attributes the whole decline to financing without the durability tests.
