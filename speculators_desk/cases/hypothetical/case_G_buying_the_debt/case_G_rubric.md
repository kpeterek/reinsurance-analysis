# Case G — Instructor Grading Rubric

Keep this file separate from the student version. Numbers are produced by `case_g_model.py` and asserted in `tests/test_case_g.py`.

## Mode C — Blind examination (100 points)

| Q | Pts | Full credit | Common deductions |
|---|---|---|---|
| 1 | 10 | Cure payoff \$51,060,000; note all-in \$33,150,000 (\$106,250/unit); REO all-in \$38,062,500 (\$121,995/unit) | −3 if default interest is included in the cure payoff without saying it was waived |
| 2 | 15 | Month 0 −\$33.15m; month 4 −\$0.75m (legal + cash for keys); months 5–28 NOI/12 − \$166,667 capex; first ownership month \$29,653; ownership total \$50,048,000 including sale | −5 if capex is omitted; −5 if NOI is collected before title |
| 3 | 20 | IRRs 136.32% / 73.71% / 18.45% / 14.31% / 11.62% / 6.60%; profits and NPVs as in Mode B | −5 for annualizing monthly IRR by ×12; −3 per scenario with timing errors |
| 4 | 10 | IRR of expected flows 18.62%; mean IRR 38.98%; explains that fast, small-dollar outcomes dominate the mean | −5 for presenting 39% as the expected return |
| 5 | 10 | \$35,080,359 (73.08% of UPB) | −3 if the \$150k closing cost is ignored |
| 6 | 10 | REO IRR 14.67%; profit \$11.85m; expected \$4.15m with 35% win probability | −3 if the losing-auction outcome is ignored |
| 7 | 10 | Note 10.34% vs REO 1.97% at −20% | −3 if only one strategy is stressed |
| 8 | 5 | Accept: DPO NPV +\$4.89m vs −\$0.48m conditional expected NPV of the non-payoff paths | −3 if the comparison uses only the deed-in-lieu path |
| 9 | 10 | Bid ≤ \$33m with title, lender-liability, guaranty, and valuation diligence; walk-away triggers stated | −5 for no walk-away |

Mastery threshold: 80 points, with at least 15/20 on Q3.

## Mode D — Investment committee: model answers and scoring

Score each answer 0–4: 0 missing or wrong; 2 qualitatively correct with no number; 4 quantified, honest about uncertainty, and decision-relevant.

1. **Why paper?** The note reaches the same collateral at \$33.15 million versus \$38.06 million for the REO, and controls the path (credit bid ≈ \$55.5 million after ten months, so no third party outbids it). In 65% of outcomes we own the property; in 30% we are paid off quickly at a profit.
2. **18.6% vs 39%.** 39% averages scenario IRRs and is dominated by the four- and six-month payoffs; 18.62% is the IRR of probability-weighted cash flows. Expected NPV at 15% is +\$2.08 million. Present both and explain.
3. **Bankruptcy on day one.** SARE rules force the debtor to file a confirmable plan or pay interest at the nondefault contract rate on the collateral value by the statutory deadline (11 U.S.C. §362(d)(3)); otherwise we can seek stay relief, which is not automatic. The model's stay-lifted path (20 months) earns 11.62% with NPV −\$3.40 million; the delay, not the principal, is the cost.
4. **Cramdown.** NPV −\$11.31 million, IRR 6.60%: our claim is written down to \$36 million and paid at 7% for five years. It gets worse if the court values the collateral lower or sets a lower rate. A strong answer says the cramdown rate and valuation are litigated and that our counsel's estimate of plan feasibility drives this probability.
5. **Valuation confidence.** At −20% stabilized value the note's IRR of expected flows is 10.34% with no losing scenario; the REO falls to 1.97%. A strong answer asks for an independent valuation and a property-condition report before closing, and notes the 30% stress (note 5.85%, REO −4.96%).
6. **Legal risks specific to the note.** Lender liability claims, defects in the loan file or assignment chain, borrower defenses and offsets, mechanic's liens, and limited seller representations. None of these come with a clean REO purchase.
7. **The \$40 million DPO.** Accept: +\$4.89 million NPV versus −\$0.48 million for the remaining paths. A strong answer also notes that accepting closes the position with certainty and frees capital.
8. **Why not wait for the REO?** Only a 35% chance to win, a \$4.9 million higher basis, a weaker starting NOI, and a 14.67% IRR if won. Waiting is defensible only if the note cannot be bought at or below the 15% maximum (\$35.08 million).
9. **Walk-away triggers.** Senior or priming liens; capex above about \$6 million; evidence that bankruptcy is likely (sponsor's other properties in default, a bankruptcy lawyer already engaged); a loan-file defect.
10. **Judicial state.** Every title path lengthens by many months and carry grows (Chapter 12, Example 12.4); the maximum price falls. A strong answer reprices with a longer timeline rather than asserting a direction.

Minimum passing committee performance: an average of at least 3.0, with no 0 on questions 2, 3, or 5.

## Mode B — Alternative defensible recommendations

* **Pass on the note and the REO.** Defensible if the analyst's bankruptcy probabilities total 30% or more and the as-is value is in doubt; state a re-engagement price for the note (for example, below \$30 million).
* **Buy the note with a co-investor holding a participation.** Reduces concentration; defensible if the participation terms preserve control of the workout.
* **Not defensible:** paying more than \$35.1 million without new information; presenting the 39% mean IRR as the expected return; treating the foreclosure auction as the place to buy the property.
