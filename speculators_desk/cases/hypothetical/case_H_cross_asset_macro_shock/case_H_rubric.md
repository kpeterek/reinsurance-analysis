# Case H — Instructor Grading Rubric

Keep this file separate from the student version. Numbers are produced by `case_h_model.py` and asserted in `tests/test_case_h.py`. All case inputs are [HYPOTHESIS].

## Mode C — Blind examination (100 points)

| Q | Pts | Full credit | Common deductions |
|---|---|---|---|
| 1 | 8 | 10-year DV01 \$48,468, P&L −\$864,928; 2-year DV01 \$7,625, P&L −\$190,040; convexity explains the \$7,490 and \$577 differences | −3 for applying one yield move to both bonds. −2 for DV01 per \$100 face not scaled to position size |
| 2 | 6 | Notional \$15.0m; P&L −\$375,000; \$50 multiplier | −4 for the \$250 multiplier (−\$1.875m) |
| 3 | 10 | −\$819,500 = −\$550,000 local − \$269,500 FX; return −2.98%; hedge +\$275,000; hedged −\$544,500 | −5 for dividing by the EUR/USD rate (quote direction). −2 for adding returns instead of compounding |
| 4 | 10 | IG: rate −\$500,667, spread −\$273,091, full −\$763,638. HY: rate −\$135,511, spread −\$246,384, full −\$376,033 | −4 for using the 10-year move instead of the 5-year. −3 for ignoring the rate component |
| 5 | 6 | −\$3,389,139; −0.85% of NAV | −2 for including unrealized private CRE changes in the day's marked P&L without labeling them |
| 6 | 12 | DSCR 1.304x → 1.260x; 1.196x at strike; trap SOFR 4.477% < 4.50% strike; actual/360 | −4 for 30/360. −4 for missing that the cap strike sits above the trap level |
| 7 | 14 | Coupon 5.90% → 6.23%; loan \$37.09m → \$35.81m (DSCR binds); gap \$5.33m → \$6.61m; 10-year part \$709k, spread part \$575k; hedge about \$49.5m face | −4 if the appraisal is changed today (it is lagged). −4 if the hedge is claimed to cover the spread |
| 8 | 14 | Economic −2.65% at 5.65%; appraisal path −0.93% after Q1 to −2.18% after Q4; bid–ask gap 2.73%; negative leverage at 6.23% coupon; volume falls before prices | −5 for "CRE was unaffected". −3 for no mechanism for the volume decline |
| 9 | 10 | Recommendations: common factor, refinancing hedge and gap funding, cap–trap fix, FX policy, reporting economic value; states what would change them | −5 for "sell everything" or "do nothing" without analysis |
| 10 | 10 | Examples: (i) surprise read as recession risk: 10-year falls, curve inverts, fixed refinancing cheaper, equities and credit still down; (ii) growth-driven surprise: equities rise; (iii) foreign central banks surprise in the same direction: dollar does not rally | −3 per example that names no position |

Mastery threshold: 85 points, with at least 11/14 on Q7 and Q8 each.

## Mode D — Investment committee: model answers and scoring

Score each answer 0–4: 0 missing or wrong; 2 qualitatively correct with no number; 4 quantified, honest about uncertainty, and decision-relevant.

1. **Common factor.** The book is long duration (DV01 \$56,092 in Treasuries plus credit duration), long equity beta, short the dollar through euro assets, and long credit risk. An upside inflation surprise hits all four at once. Sum: −\$3.39m, −0.85% of NAV, with every line negative. A strong answer proposes measuring exposure to an "inflation surprise" scenario directly, rather than relying on asset-class labels or historical correlations from a period when stocks and bonds moved in opposite directions.
2. **Multifamily value.** Defend the −2.65% as an *estimate* of the economic value conditional on the cap-rate assumption (pass-through 0.5 plus 6 bp), and show the sensitivity: with pass-through 1.0 the cap would move to 5.74% and value would fall 4.2%. The appraisal will recognize about 35% of the change after one quarter. Reject both "unchanged" and false precision.
3. **Hedging.** Hedgeable: Treasury DV01 (futures), equity beta (ES), FX (forwards: +\$275,000 today), the 10-year component of the refinancing (about \$49.5m short 10-year, +\$714,068 today), SOFR (caps, SOFR futures). Not hedgeable: the lender's spread (+15 bp, \$575,165 of proceeds), the lender's willingness to quote, and appraisal timing. Cost: hedges give up gains on the reverse shock, and caps cost premium.
4. **Hotel cap.** Protected against default, not against a cash trap: the trap springs at SOFR 4.477%, below the 4.50% strike. NOI cushion to the trap at the shocked rate is only 4.78%. Recommend a lower-strike cap or renegotiating the trap.
5. **Lock now?** The 18 bp is sunk. The question is the distribution from here to closing. Locking removes the 10-year exposure on a known, dated need (about \$40,000 of proceeds per bp). A strong answer separates the decision from regret about the past move and notes that a lock is consistent with a "no view" stance on rates.
6. **Reversal.** If yields reverse 18 bp, the hedge loses about \$714k while proceeds recover by about the same, so net proceeds are roughly unchanged. The cost of hedging is forgone upside, not a net loss on the combined position. Cap premia are a true cost.
7. **Liquidity.** The \$6.6m gap is 1.7% of NAV. Treasuries are the most liquid source but selling them reduces DV01 (which helps); selling ES reduces equity beta. A strong answer avoids selling the euro shares into a drawdown purely for liquidity and considers preferred equity or a partial paydown structure.
8. **Add risk if:** the surprise is traced to a volatile, non-recurring component; long-run inflation compensation (5y5y) is unchanged; credit spreads stabilize; and private sellers become motivated (volume picks up at lower prices). Then the bid–ask gap becomes an opportunity for buyers.
9. **Sell the multifamily?** Compare the economic value \$58.4m (net of selling costs) with the refinancing route: \$6.6m of new equity at a 5.65% going-in yield against a 6.23% coupon, which is negative leverage. Selling is defensible at or above about \$58.4m. Refinancing is defensible if the committee has a long horizon and expects NOI growth. A strong answer recognizes that few buyers will pay the old \$60m appraisal.
10. **Diversification.** Diversification measured by asset class or by correlation in calm periods understates common exposure to inflation and policy shocks. Measure it with scenario P&L by factor, and include private assets at economic, not appraised, values.

Minimum passing committee performance: an average of at least 3.0, with no score of 0 on questions 1, 4, or 5.

## Mode B — Alternative defensible recommendations

* **Sell the multifamily instead of refinancing.** Defensible if a bid near the economic value exists and the committee does not want to commit \$6.6m of new equity to a negatively levered asset.
* **Add duration after the shock.** Defensible only with a stated thesis (for example, that the surprise was transitory) and with the book's total inflation exposure sized explicitly. Not defensible as "buying the dip" without that.
* **Not defensible:** reporting the multifamily as unchanged to the committee; claiming the Treasury hedge would have covered the lender's spread; computing ES P&L with a \$250 multiplier; treating the cap as protection against the cash trap.
