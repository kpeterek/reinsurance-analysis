# Case A — Instructor Grading Rubric

Keep this file separate from the student version. Numbers are produced by `case_a_model.py` and asserted in `tests/test_case_a.py`.

## Mode C — Blind examination (100 points)

| Q | Pts | Full credit | Common deductions |
|---|---|---|---|
| 1 | 5 | Occ 70.00%, ADR \$118.00, RevPAR \$82.60 | −2 if RevPAR is computed on rooms sold |
| 2 | 5 | Insurance proceeds, pipeline block, owner personal costs, spouse/GM, roof, management fee, insurance quote, reserve, tax reassessment (9 items) | −1 per item missed. −3 if the roof is both added back *and* the reserve omitted, since that double-counts capital |
| 3 | 20 | Bridge to \$607,927 with the pipeline net of backfill (\$119,140), variable cost saved (\$15,540), and franchise saved (\$12,510) | −5 for removing the gross \$207,200 with no backfill or cost offset. −5 if management is calculated on the owner's revenue (including insurance proceeds) |
| 4 | 10 | $V = N/(c+t)$ derived. \$5,307,091 at 9.5%. Error \$268,986 | −5 for using the old tax bill. −3 for applying the tax rate to 100% of price without stating the assumption |
| 5 | 10 | As-is \$5.07m / \$4.53m / \$3.71m | −3 if PIP contingency or displacement is omitted |
| 6 | 10 | Cost basis is sunk and anchors behavior only. Replacement cost (\$11.07m) is not binding because development is infeasible at the supported value. Uses the numbers | −5 for "replacement cost is a floor" |
| 7 | 10 | Loan at 65% of price, LTV binding, DSCR about 2.0x, debt yield unused | −3 if the binding constraint is misidentified |
| 8 | 10 | Gap \$729,917. Payoff price \$4,432,990 | −3 if refinance is sized on reassessed tax |
| 9 | 15 | Price, PIP and PCA conditions, walk-away triggers, and owner-facing explanation that uses the bridge | −5 for no walk-away. −5 for a tone that would end the negotiation |
| 10 | 5 | Up: lower PIP, pipeline return, lower cap rates from comps. Down: higher PIP, insurance, new supply, falling RGI | |

Mastery threshold: 85 points, with at least 16/20 on Q3.

## Mode D — Investment committee: model answers and scoring

Score each answer 0–4: 0 missing or wrong; 2 qualitatively correct with no number; 4 quantified, honest about uncertainty, and decision-relevant.

1. **Most contestable adjustment.** The pipeline backfill. At 70% backfill instead of 40%, $N$ rises by \$46,717 to \$654,644, and loaded value at 9.5% rises by about **\$407,832**. A strong answer offers to verify backfill with 24 months of STR data, comparing the months with the crew to the same months a year earlier. Insurance is second: each \$10,000 of premium is worth about \$87,000 of value at a 11.455% loaded cap.
2. **What is priced?** Market cap rates on comparable sales are on *as-is* transactions in which PIPs may or may not have been deducted. A strong answer says you must know whether the comparable sales carried PIPs. If they did, a 9.5% cap on stabilized NOI with the PIP deducted separately is consistent. If they were already-renovated assets, also consistent. If comps were PIP-encumbered and priced on in-place NOI, there is a risk of double-counting. The answer identifies the data needed.
3. **Exit cap +100 bp.** Holding stabilized NOI after tax at \$504,174, value falls from \$5.31m (9.5%) to \$4.80m (10.5%), a **9.5%** decline. Equity is about 46% of the all-in basis (\$2.39m of \$5.22m at a \$4.35m price), so the \$0.51m value decline is about 21% of initial equity. A strong answer computes the five-year IRR effect in the model or states that it requires the hold model in Chapter 9.
4. **Cash loss tolerance and break-even.** At \$4.35m, debt service is \$256,283. Approximate break-even occupancy at normalized ADR is **55.6%** including debt service and **45.4%** before debt, against 66.3% normalized. A strong answer notes these are optimistic, because ADR usually falls when occupancy falls. It also proposes a working-capital reserve, for example six months of debt service plus insurance, about \$162,000.
5. **What forces the owner?** The maturity and the \$730k refinancing gap. If the lender extends, the owner's urgency falls but the economics do not change: the refinancing gap remains at the extended maturity. A strong answer says the bid should not depend on distress and should be justifiable at the yield-on-cost target alone.
6. **Most likely failure.** The PIP scope comes in higher, the renovation runs over, and penetration erodes during the work. Second: insurance and tax escalation, which is an ongoing Texas cost trend [HYPOTHESIS for this case; verify with current premium data].
7. **Withdraw if:** PIP above \$11k/key with no price relief; RGI below 95 on the T-3; PCA reveals structural or MEP issues above \$150k; insurance not bindable at or below \$75k.
8. **Versus Treasuries.** The base-case going-in yield on all-in cost is about 10% unlevered, before growth. A strong answer subtracts expected capex beyond the reserve, a liquidity premium, and the volatility of hotel NOI. It does not claim superiority on yield alone, and it quotes the current Treasury yield from a live source at the time of the committee.
9. **Hedging.** Rate risk can be hedged with fixed-rate debt or swaps. Insurance can be partly managed with deductible structure. Operating risk (RevPAR), PIP execution, and local supply **cannot** be hedged and must be priced or avoided.
10. **Why now?** A strong answer says that waiting may produce a lower price but carries competitive risk (another buyer) and the owner may secure an extension. It proposes a firm bid with a defined expiry, and is prepared to re-engage at maturity.

Minimum passing committee performance: an average of at least 3.0, with no score of 0 on questions 4, 6, or 7.

## Mode B — Alternative defensible recommendations

* **Pass.** Defensible if the analyst's view of the cap rate is 10.5% or higher (as-is \$3.71m, below the owner's payoff of \$4.43m). In that case no deal exists that both sides can sign. The analyst should say so and set a re-engagement trigger, such as the maturity date or listing expiry.
* **Bid at \$4.45m with seller-funded PIP credit.** Restructures the same economics so the headline price exceeds the owner's payoff. Defensible if the analysis shows that the total consideration is equivalent.
* **Not defensible:** any price above \$5.07m (the upside as-is value) without new information, or any reliance on cost basis or replacement cost as support.
