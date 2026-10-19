# Case I — Instructor Grading Rubric

Keep this file separate from the student version. Numbers are produced by `case_i_model.py` and asserted in `tests/test_case_i.py`.

## Mode C — Blind examination (100 points)

| Q | Pts | Full credit | Common deductions |
|---|---|---|---|
| 1 | 5 | Sunk cost; anchors the partner's reservation price but not value | −3 for any use of \$900k in a valuation |
| 2 | 15 | RLV by-right \$5,795,562; PD \$9,144,225, with each cost line and the margin on total cost | −5 for applying the margin to GDV instead of cost. −3 for omitting selling costs on GDV |
| 3 | 10 | Up \$15,844,428 (+173%); down −\$6,652,964, so the floor of \$1.5m applies. Explains residual leverage | −5 for forgetting cost escalation |
| 4 | 10 | $q = 0.4273$; the cap rate is the yield forgone by the landholder | −5 for $q = (1 + r - d)/(u - d)$ without $\delta$ (gives 0.577) |
| 5 | 15 | Wait \$7,024,032; entitle \$8,278,809. The approval is idiosyncratic, so it carries no risk premium | −5 for omitting carry or sale costs. −5 for risk-neutralizing the vote |
| 6 | 10 | $p^* \approx 15.8\%$ | −3 for a correct method with an arithmetic slip |
| 7 | 10 | JV PV \$6,162,768 at 12%; the family gives up the option to wait and entitle, and the developer earns an expected promote of about \$1.90m at year 2 | −5 for valuing the JV at the \$6.0m credit |
| 8 | 10 | Value of waiting −\$1.06m / +\$1.40m / +\$3.62m. The decision flips within a plausible range of volatility | −3 for no interpretation |
| 9 | 10 | Clear recommendation, executable with the family's liquidity, with triggers | −5 for "build now" without a financing plan |
| 10 | 5 | Up: higher volatility, lower carry, cheap entitlement extension, no competing sites. Down: competitor pre-emption, high cost escalation, high cap rate (forgone yield), denial signals | |

Mastery threshold: 85 points, with at least 12/15 on Q5.

## Mode D — Investment committee: model answers and scoring

Score each answer 0–4: 0 missing or wrong; 2 qualitatively correct with no number; 4 quantified, honest about uncertainty, and decision-relevant.

1. **Bird in the hand.** The \$5.4m bid nets \$5.24m. The entitle path is worth \$8.28m in expectation, but its outcomes are dispersed: about \$22.3m net if the market rises and the PD is approved, \$15.4m if it rises and the PD is denied, and \$1.5m less carry if the market falls. A strong answer admits the family bears that dispersion. It proposes reducing it, for example with a contract at a higher price contingent on approval, rather than claiming the \$8.28m is "the value".
2. **Volatility.** $u = 1.20$ corresponds to roughly 18% annual volatility of completed value ($\ln 1.2 = 0.182$). At $u = 1.10$ the wait value is \$4.56m and entitlement \$5.26m, essentially equal to the \$5.24m net bid. Selling becomes defensible. A strong answer says the recommendation is conditional on the volatility estimate, and proposes checking it against the history of local rents and cap rates.
3. **Approval probability.** At 25%, entitlement is still worth \$7.28m, above waiting without it (\$7.02m), because break-even is about 16%. Evidence needed: staff recommendation, planning-commission record on similar PDs, neighborhood opposition, traffic study.
4. **If the builder walks.** The bid is 93% of by-right RLV, so other merchant builders using similar inputs should bid near it. But the bid is also evidence about the market's static valuation. Losing it costs time, not much value, unless the market falls.
5. **Cash cost of waiting.** Carry \$60,000; entitlement \$450,000; non-land cost escalation about \$2.22m (4% of \$55.56m), which reduces next year's RLV; the forgone 5.5% yield, which enters through $q$; 3% sale costs whenever the land is sold.
6. **Why not build?** The 15% margin is compensation for development risk and capital, not a free gain. Total cost is about \$61.4m. At 60% LTC the equity is about \$24.5m against the family's \$3m. After a 3% fee developer the build-now value is \$4.39m, below even the bid.
7. **JV fairness.** In a build-now JV the developer exercises the option immediately. The family's land is credited at \$6.0m, above its static RLV, but the family's PV is \$6.16m, against \$8.28m for entitling. The developer earns an expected promote of about \$1.90m at year 2. A better JV contributes the land after entitlement, or gives the family a share of the PD uplift.
8. **What makes waiting a mistake.** A competing landowner with an approved PD who starts first (pre-emption). A sharp cost spike. A rise in cap rates, which raises the forgone yield and lowers GDV together. A council signal of denial plus a falling market.
9. **Liquidity plan.** Entitlement \$450k plus 18 months of carry, \$90k: about \$0.54m of the family's \$3m. Feasible. A strong answer also states what the family would do with no sale for two years.
10. **Trigger.** Sell before the vote if an unconditional bid for the by-right site exceeds about \$8.5m gross. After approval, market the entitled site or a land-contribution JV. After denial with a falling market, sell to the best bid or the alternative-use buyer. Re-evaluate if rents fall 10% or hard costs rise 8%.

Minimum passing committee performance: an average of at least 3.0, with no score of 0 on questions 2, 6, or 10.

## Mode B — Alternative defensible recommendations

* **Sell now at \$5.4m.** Defensible only if the analyst argues, with data, that volatility is low ($u \le 1.10$), or that the family has a pressing liquidity need that makes the option's carry unbearable. It must be argued as a choice to give up option value, not as "the value".
* **Contingent sale.** A sale at a higher price contingent on PD approval, with the buyer funding entitlement. Often the best practical answer, because it shares the option with the party best able to exercise it.
* **Wait without entitling.** Defensible only if the PD has a very low approval probability (below about 16%) or entitlement would trigger opposition that harms the by-right path.
* **Not defensible:** building now with the family's capital; valuing the land at \$900k plus a return; valuing the JV at its \$6.0m credit.
