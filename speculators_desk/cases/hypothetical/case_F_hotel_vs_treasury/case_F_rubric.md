# Case F — Instructor Grading Rubric

Keep this file separate from the student version. Numbers are produced by `case_f_model.py` and asserted in `tests/test_case_f.py`. The tax treatment is simplified and labeled in the case. Grade the reasoning against the stated assumptions, not against an individual's actual tax position.

## Mode C — Blind examination (100 points)

| Q | Pts | Full credit | Common deductions |
|---|---|---|---|
| 1 | 5 | The cap rate is an unlevered, pre-tax, pre-capex first-year income yield on an illiquid risky asset; the Treasury yield is a riskless total return. Compare total-return, after-tax IRRs on equal equity | −3 if risk or liquidity is not mentioned |
| 2 | 10 | Payment \$69,971.14; DS \$839,654; DSCR 1.67x; balance \$9,025,053. Notes the loan constant (8.48%) equals the going-in cap | −3 for annual rather than monthly amortization |
| 3 | 10 | Basis \$16.83m; building \$12,622,500 / 39 = \$323,654; FF&E \$1,683,000 / 7 = \$240,429; land not depreciated | −5 for depreciating land; −2 for omitting closing costs from basis |
| 4 | 15 | Pre-tax 12.63%; after-tax 9.27%, with the yearly tax table | −5 for taxing cash flow after debt service instead of NOI − interest − depreciation |
| 5 | 10 | Gain \$3,482,570; unrecaptured §1250 \$1,618,269 at 28.8%; LTCG \$1,864,301 at 23.8%; tax \$909,765 | −5 for taxing all gain at 23.8% |
| 6 | 10 | Treasury after tax 2.37% (40.8% lost); hotel loses 26.6%. Explains depreciation, deferral, and rate character | −3 if NIIT is omitted |
| 7 | 10 | Expected after-tax IRR 7.36%; IRR of expected flows 7.79%; explains the nonlinearity (Chapter 1) | −3 for reporting only the base case |
| 8 | 10 | Treasury −4.49% per +100 bp; hotel equity −26.4% per +100 bp of cap rate. Treasury real after-tax −0.13% (2.5% CPI) and −2.51% (5% CPI); hotel 4.23% real in the inflation case | −3 for calling the hotel a perfect inflation hedge |
| 9 | 10 | Moot in Texas. In a hypothetical 6% state, the break-even corporate yield rises from 4.00% to 4.45% | −5 for applying a state tax to a Texas resident |
| 10 | 10 | Addresses concentration (87% of liquid capital), the reserve, the severe-case cash call, and a smaller-interest alternative | −5 for a recommendation based on expected IRR alone |

Mastery threshold: 85 points, with at least 12/15 on Q4.

## Mode D — Investment committee: model answers and scoring

Score each answer 0–4: 0 missing or wrong; 2 qualitatively correct with no number; 4 quantified, honest about uncertainty, and decision-relevant.

1. **"Twice the yield."** The comparable numbers are 7.36% expected after tax against 2.37% after tax. The hotel's premium is about 5 points a year, compensation for a 10% chance of losing money (−4.46% IRR), a 25% chance of earning only 3.08%, illiquidity, and operating risk. The cap rate is not a return.
2. **CPA's three assumptions.** (i) Passive-activity status and the usability of losses in the severe case. (ii) The purchase-price allocation and depreciation method: cost segregation and bonus depreciation would raise early deductions and recapture exposure. (iii) The character of gain on sale, including §1245 recapture on FF&E if FF&E is allocated more than its tax basis.
3. **A 2020.** Year-1 NOI \$490,000 against \$839,654 debt service: DSCR 0.58x and a \$349,654 cash call. The five-year after-tax IRR is −4.46%. A strong answer adds that a lender may also sweep cash or require reserves, and that the scenario's 11.0% exit cap is an assumption.
4. **Needing \$3m in year 2.** Treasuries: sell \$3m of notes in a day, with a price effect of a few percent at most for a 100 bp move (duration about 4.5 now, less by year 2). Hotel: no partial sale. Options are a full sale (months, 3% costs, possibly in a weak market) or a supplemental loan if DSCR allows. A strong answer concludes that the reserve must sit outside the hotel.
5. **Inflation hedge.** Partly. In the 5% CPI case the hotel earns 4.23% real after tax against −2.51% for Treasuries, but only if NOI growth keeps pace and the exit cap rises no more than 100 bp. Hotels reprice rooms daily, but labor, insurance, and property tax also rise.
6. **The 7% loan.** At 50% LTV, equity would be \$8.58m, more than the \$8.0m available, so it is infeasible without a smaller hotel. Base after-tax IRR falls to 8.33% and the expected after-tax IRR to 6.82%. The severe cash call falls to about \$210,000. Lower leverage buys survival, not return.
7. **Treasuries plus a small interest.** A 30% LP interest (about \$2.1m) plus \$5.9m in Treasuries keeps most of the capital liquid and riskless. A strong answer computes a blended expected after-tax return (about $0.26 \times 7.36\% + 0.74 \times 2.37\% \approx 3.7\%$ by capital weight) and argues that the concentration reduction is worth the lower mean.
8. **Probability-weighted cost of being wrong.** Undiscounted after-tax profit: Treasury \$820,512. Hotel: severe −\$1,339,663. Only the severe case falls below the Treasury, so the probability-weighted shortfall is $0.10 \times (820{,}512 + 1{,}339{,}663) = \$216,017$. A strong answer adds that the downside case (\$999,590) barely beats the Treasury.
9. **When Treasuries win.** If the base-case exit cap is above about 11.27%, the hotel's after-tax return falls to the Treasury's. If the investor requires a 400 bp after-tax premium, the threshold is a 9.88% exit cap. A higher Treasury yield raises the bar point for point (after tax, by 0.59 of the yield change).
10. **Decision.** Do not commit 87% of liquid capital to a single hotel. Either take a minority interest with an experienced operator or buy only if the \$8m is a minority of net worth, with a \$1m+ reserve outside the deal. Reverse if the hotel can be bought at a price that raises the expected after-tax premium, or if the investor's total wealth makes the concentration small.

Minimum passing committee performance: an average of at least 3.0, with no score of 0 on questions 1, 3, or 10.

## Mode B — Alternative defensible recommendations

* **Buy the hotel outright.** Defensible only if the investor's total net worth is several times \$8m, the reserve is held outside the deal, and the tax assumptions are confirmed.
* **All Treasuries.** Defensible if the investor's priority is liquidity, or if the investor cannot oversee an operating asset. It must be argued as a choice to forgo a 5-point expected premium, not as "hotels are too risky."
* **Not defensible:** comparing the 8.48% cap rate with the 4% yield; applying a state tax in Texas; omitting depreciation recapture; recommending the hotel without addressing the severe-case cash call.
