# Case B — Instructor Grading Rubric

Keep this file separate from the student version. Numbers are produced by `case_b_model.py` and asserted in `tests/test_case_b.py`. All inputs are hypothetical [HYPOTHESIS].

## Mode C — Blind examination (100 points)

| Q | Pts | Full credit | Common deductions |
|---|---|---|---|
| 1 | 8 | Value \$28,484,848; LTV 105.3%; old DSCR 1.94x and DY 6.60% on NCF \$1,980,000; same balance on new terms 0.85x | −3 for using NOI instead of NCF for coverage; −2 for using the 6.75% coupon instead of the 7.783% constant |
| 2 | 10 | LTV \$17,090,909 binds (DSCR \$18,844,061; DY \$19,800,000); equity to refinance \$13,165,455 including \$256,364 costs | −3 for omitting costs; −5 for sizing DSCR on NOI |
| 3 | 10 | Income −\$6.40m, cap rate −\$4.98m, LTV −\$1.42m (and −\$0.10m because the original loan was slightly above 65%); concludes rates act mainly through the cap rate and the DSCR test does not bind | −4 for attributing the gap to "rates" without showing DSCR is not binding |
| 4 | 20 | Expected NPVs: refinance −\$3,154,392; extension \$395,066; DPO \$2,595,608; keys −\$150,000; sale −\$2,084,848; state values as in Mode B | −5 if terminal equity is not floored at zero (non-recourse); −5 if the extension's cash sweep is ignored; −3 for discounting at the loan rate |
| 5 | 12 | Lender PVs: extension \$28,018,240; short sale \$27,915,152; keys \$26,307,643; DPO \$24.0m. Extension is the only strategy both prefer to their alternatives; no DPO zone (sponsor max \$26,595,608 < lender min \$28,018,240) | −6 for recommending a DPO without checking the lender's alternative |
| 6 | 8 | Option value \$3,684,565 versus intrinsic −\$1,515,152; explains time value and dispersion with a floor | −4 for "the equity is worthless" |
| 7 | 8 | Break-even paydown \$4,042,682; lender accepts any paydown ≥ \$0 (PV \$27,335,392 at zero paydown) | −3 without the lender side |
| 8 | 8 | Promote \$0 in all states and strategies; keys IRR −35.53%; GP/LP private payoffs; notes the GP's refinance payoff is positive (\$70,882) while the LP's is −\$2,838,953 | −4 if fees are ignored |
| 9 | 8 | REO value \$27,112,891 (\$147/rsf); note \$24,506,892 (81.7% of par) under the stated mix | −3 for valuing the note at the property value without resolution costs and timing |
| 10 | 8 | Extension with a negotiated paydown; no fresh-equity refinance; no shortfall payment; walk-away trigger on Downside evidence; LP-protective pricing of new money | −4 for no walk-away trigger |

Mastery threshold: 85 points, with at least 16/20 on Q4 and 10/12 on Q5.

## Mode D — Investment committee: model answers and scoring

Score each answer 0–4: 0 missing or wrong; 2 qualitatively correct with no number; 4 quantified, honest about uncertainty, and decision-relevant.

1. **Why not refinance?** It requires \$13.17 million of new equity (78% of the original equity) and has an expected NPV of −\$3.15 million at 15%. Belief in the asset is captured more cheaply by the extension, which keeps the same upside for \$3.1 million. A strong answer shows the Recovery-state NPV (\$2.15 million) is positive but the Downside (−\$10.16 million) dominates.
2. **How much is rates?** DSCR at the new rate does not bind: the DSCR loan is \$18.84 million versus the \$17.09 million LTV loan. Rates matter through the cap rate (−\$4.98 million of proceeds) and through the 0.85x DSCR on the old balance. A buy-down or IO would not change the LTV-binding loan. A strong answer separates the two channels.
3. **Why \$3 million into negative equity?** Because the equity is an option worth \$3.68 million at 15%, more than the \$3.135 million paydown and fee. Expected NPV \$395,066, with a 25% probability of losing the full amount. A strong answer states this is a speculative position sized at 18.5% of original equity and shows the downside.
4. **Lender's position.** Its extension PV exceeds its deed-in-lieu value at any paydown (\$27.34 million at zero versus \$26.31 million). The sponsor's maximum paydown is \$4.04 million. A strong answer proposes a lower paydown with the full sweep and explains why the lender should accept.
5. **Why not a DPO?** The sponsor would pay up to \$26.60 million; the lender's alternative is worth \$28.02 million. No price works for both unless the lender's own situation changes (liquidity need, regulator, portfolio sale). A strong answer suggests asking in a way that does not threaten the extension.
6. **Fees.** Shows the private-payoff table: the GP gains \$70,882 from a fresh-equity refinance that costs the LP \$2.84 million. Offers fee deferral or subordination during the extension, and LP approval rights over new money.
7. **Downside.** Shortfalls of \$102,500, \$302,500, \$452,500 in years 1–3 and a deed-in-lieu at $t=3$. A strong answer sets a trigger (e.g., Y1 NCF below \$1.45 million with no signed leases in the pipeline) to stop funding and hand back the keys early, and notes that the model's full-funding assumption overstates the Downside loss.
8. **Guarantor.** Extension, short sale, or deed-in-lieu: no recourse if the documents are followed and rents are not diverted. Bankruptcy or an unpermitted transfer: full recourse on \$30.0 million. Cash sweep compliance matters: misapplied rents are loss recourse.
9. **Note buyer.** A 12% buyer values the note at about \$24.5 million; a 6.75% holder at \$28.0 million. A sale is unlikely. If it happens, the new holder's higher required return makes foreclosure or a DPO more likely; Larchmont should re-run Q5 at 12% and prepare for a harder negotiation.
10. **Keys today?** If the lender refuses any extension, or demands a paydown above \$4.04 million, or if new evidence moves the Downside probability materially above 25%. Also if the LP will not fund and the GP cannot. A strong answer gives the break-even probability or paydown.

Minimum passing committee performance: an average of at least 3.0, with no score of 0 on questions 3, 6, or 7.

## Mode B — Alternative defensible recommendations

* **Deed-in-lieu now.** Defensible if the analyst assigns a Downside probability materially above 25% or a Recovery probability below about 20%, or believes the 8.25% cap rate is stale and the true clearing level is higher. The analyst must show the extension's NPV turning negative under those inputs and must use a cooperative deed-in-lieu to avoid springing recourse.
* **Extension with LP-funded paydown as preferred equity.** The same economics as Mode B, restructured so the new money ranks ahead of the existing common.
* **Not defensible:** a fresh-equity refinance at \$13.2 million without new information; paying the \$2.08 million sale shortfall; a bankruptcy filing to stall the lender; any recommendation that ignores the GP's fee incentive.
