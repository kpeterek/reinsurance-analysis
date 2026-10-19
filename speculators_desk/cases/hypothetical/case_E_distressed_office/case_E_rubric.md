# Case E — Instructor Grading Rubric

Keep this file separate from the student version. Numbers are produced by `case_e_model.py` and asserted in `tests/test_case_e.py`.

## Mode C — Blind examination (100 points)

| Q | Pts | Full credit | Common deductions |
|---|---|---|---|
| 1 | 10 | Required rent \$64.00/sf vs market \$34.00; states that replacement cost bounds supply, not value | −5 for "replacement cost is a floor"; −3 if tax on cost or leasing reserve omitted |
| 2 | 20 | Recovery year-1 revenue \$6,894,400; new leasing 38,800 sf, renewals 22,000 sf; TI \$3,072,000; LC \$666,264; free rent \$894,200; NOI \$592,200; CF −\$10,946,064. Years 2–7 as in Mode B | −5 if in-place and market rents are not separated; −5 if non-renewing space is not re-leased (new leasing understated); −5 if capex or free rent omitted |
| 3 | 10 | Net exits \$151.20m / \$65.44m / \$17.63m on year-8 NOI | −5 for capitalizing year-7 NOI (trailing) without saying so; −3 for omitting the Structural liquidity discount |
| 4 | 15 | IRRs 13.10% / −0.80% / −20.62%; IRR of expected flows 4.03%; mean IRR −0.19%; E[profit] \$22.12m; P(loss) 60% | −5 for reporting a single IRR; −3 if the two "expected IRRs" are not distinguished |
| 5 | 10 | \$29.18m (\$56.11/RSF), solved with tax reassessed at the solved price | −3 if tax is held at the ask-price level |
| 6 | 10 | Paydowns \$0 / \$13.89m / \$28.60m; concludes the three-year bridge is mismatched to a seven-year plan | −5 if leverage is called "positive" without testing maturity |
| 7 | 10 | Residual −\$95.09m; break-even rent \$7.22/sf/month at the ask (\$5.54 for zero land) | −5 for treating conversion as a floor |
| 8 | 10 | Renewal rate and downsizing at renewal; sublease availability; leasing per employee; tour activity converting to signed leases | −3 per vague indicator ("the market") |
| 9 | 5 | Bid near \$27–29m with lease-audit, engineering, and financing conditions; walk-away above about \$32m or on weak renewal data | −5 for bidding the ask |

Mastery threshold: 80 points, with at least 15/20 on Q2.

## Mode D — Investment committee: model answers and scoring

Score each answer 0–4: 0 missing or wrong; 2 qualitatively correct with no number; 4 quantified, honest about uncertainty, and decision-relevant.

1. **Replacement cost.** A new tower needs about \$64/sf to earn 7% on \$480/sf; the market pays \$34. Nobody will build, which helps future occupancy, but price is set by this building's cash flows net of the capital needed to produce them. At \$100/sf those flows earn about 4% in expectation.
2. **Equity and timing.** Peak capital is about \$79 million in Recovery (end of year 4) and \$76–77 million in the others, against a \$52.8 million closing. Capital is most at risk in years 1–3, when \$19–26 million of deficits are funded before the demand question resolves.
3. **Structural evidence.** Year-1 renewals: the base assumes 55% renewal at full size. A strong answer names renewal rate and downsizing at renewal, sublease availability, and leasing per employee in the submarket, and says that a year-1 renewal rate below 40% with 25%+ downsizing would move probability toward Structural. It notes that at \$30 million the break-even Structural probability is 22.9%, close to the team's 25%.
4. **TI at \$85.** Maximum price at 12% falls from \$29.18 million to \$26.21 million; IRR of expected flows at \$52 million falls to 3.06%. A strong answer notes TI is the largest controllable cost and asks for current TI comparables.
5. **Bridge loan.** In Grind and Structural (60% of probability) the year-3 extension test requires paydowns of \$13.9 million and \$28.6 million. Leverage raises Recovery's IRR but forces a recapitalization exactly when the business plan is behind. Strong answers propose either all-cash with optional later financing or a loan of at least five years with funded TI/LC.
6. **Conversion floor.** No: residual land value is −\$95 million; conversion needs about \$7.22/sf/month to support the ask, three times assumed rent. A strong answer says which building features (floor depth, window line, plumbing risers) would change this and that subsidy is a political variable.
7. **Year-7 buyer.** Grind exit at 9.5% on \$6.34 million is \$66.8 million gross. With all exit caps 100 bp wider the maximum price at 12% falls to \$25.55 million and the IRR of expected flows at the ask to 2.48%. A strong answer names the likely buyer type (local private capital, possibly with seller financing) and the financing they will need.
8. **Why bid now.** A strong answer bids conditionally at its own number, not the bank's, accepts that it may lose, and states a re-engagement trigger (second round, or a re-trade after the bank's capital plan). It does not raise the bid for fear of missing out.
9. **Hedging.** Interest-rate risk can be hedged if debt is used. Leasing, TI inflation, structural demand, and exit liquidity cannot be hedged and must be priced or avoided.
10. **Most likely failure.** Grind or Structural leasing with TI and free-rent inflation; a strong answer ranks demand first and quantifies with the probability-weighted loss.

Minimum passing committee performance: an average of at least 3.0, with no 0 on questions 2, 3, or 5.

## Mode B — Alternative defensible recommendations

* **Pass.** Defensible if the analyst's Structural probability is above about 30% or if TI comparables are above \$80/sf. State a re-engagement price (for example, below \$25 million) and a trigger.
* **Bid with a structural-demand earn-out.** Pay \$27 million at closing plus a contingent payment if year-3 occupancy exceeds 60%. Defensible if the seller (a bank wanting to book a sale) accepts contingent consideration.
* **Not defensible:** any price above \$39 million (the maximum even with zero Structural probability) without new information, or any use of replacement cost or conversion as support for price.
