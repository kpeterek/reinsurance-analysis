# Case C — Instructor Grading Rubric

Keep this file separate from the student version. Numbers are produced by `case_c_model.py` and asserted in `tests/test_case_c.py`. All inputs are [HYPOTHESIS].

## Mode C — Blind examination (100 points)

| Q | Pts | Full credit | Common deductions |
|---|---|---|---|
| 1 | 5 | DS \$700,000 IO / \$901,860 amortizing; DSCR 1.71x / 1.33x; DY 8.57%; CoC 7.94% / 4.73% on \$6.3m | −2 if equity omits closing costs; −2 if amortizing DS uses annual rather than monthly compounding |
| 2 | 10 | Value \$14,400,000; balance \$13,793,449 (12 amortizing payments); equity \$6,206,551 → \$606,551; asset −28.00%, equity −90.23% | −3 if the balance ignores the 24-month IO period (amortizing from month 1 gives a lower balance); −3 if equity is measured on the original \$14.0m with no comment |
| 3 | 10 | NOI \$2.0m; cap \$4.0m; interaction −\$0.4m; explains that 150 bp on a 6% base is a 20% change in the multiple | −4 if the student adds −10% and −20% to get −30% |
| 4 | 15 | LTV 95.79% breach; DSCR 1.198x passes 1.15x; both sweep triggers hit (1.198x < 1.25x; 7.83% < 8.00%); cure paydown \$2,993,449; DSCR default at NOI below \$1,037,139 (−3.97%) | −5 if only LTV is tested; −3 if DSCR uses IO debt service after month 24 |
| 5 | 10 | +38.89% asset; +923% equity; 11.1 years at 3%; 5.40% cap needed at current NOI | −3 if recovery is computed as the drawdown percentage (28%) |
| 6 | 10 | Balance at month 60 \$13,348,103; value \$14,981,760; new loan \$8,989,056 (LTV binds); gap \$4,359,047 | −3 if the refinance is sized on today's NOI without growth, with no statement of the assumption |
| 7 | 15 | DCF price \$12,723,818 (8.49% implied cap, −11.64% vs appraisal); shortfall \$1,324,107; identifies the opportunistic fund as the marginal buyer and explains why REITs and health systems are absent | −5 if the forced-sale price is set equal to the appraisal; −3 if the exit cap is applied to Year 5 NOI |
| 8 | 10 | Short sale 90.40%; foreclosure 86.10% (interim CF \$1,242,000; net sale \$11,833,150; PV at 8% over 1.25 years); note sale 80.00% | −3 if foreclosure costs or delay are ignored |
| 9 | 10 | PV cure \$3,616,854 (NPV +\$623,406); waiver \$1,296,574; pref \$988,808 to sponsor but only 4.94% expected return to the pref investor | −5 if the pref option is accepted at face value |
| 10 | 5 | Negotiate before curing; cure only as a stated bet on recovery; name the trigger for handing back the keys | −2 for "cure because we must protect our investment" (sunk-cost reasoning) |

Mastery threshold: 85 points, with at least 12/15 on Q4 and 12/15 on Q7.

### Supplementary problem C-4 (for discussion sections)
Holding the base-case probability at 50%, find the probability of the recovery scenario at which curing has zero NPV. **Answer: 10.49%.** Required EV $= 2{,}993{,}449 \times 1.12^2 = 3{,}754{,}982$; $q(7{,}109{,}482 - 1{,}719{,}482) = 3{,}754{,}982 - 0.5(4{,}659{,}482) - 0.5(1{,}719{,}482)$. Strong answers note that a 25% assumed probability clears the break-even only by a judgment the sponsor cannot verify, and that the sponsor's incentives bias that judgment upward.

## Mode D — Investment committee: model answers and scoring

Score each answer 0–4: 0 missing or wrong; 2 qualitatively correct with no number; 4 quantified, honest about uncertainty, and decision-relevant.

1. **Mistake or bad luck?** Both elements are present. The shock itself (−10% NOI, +150 bp) was within a plausible range for a 6.00% cap asset. A strong answer shows that the structure had little room: only one cell of the sensitivity grid (0% NOI, +50 bp) passes the 75% LTV covenant, and NOI −10% alone breaches it (LTV 76.6%). Sizing the loan at 70% with a 75% maintenance test left 5 points of value cushion, about 6.7% of value. The decision was poor if the underwriting did not test a combined shock of this size; the outcome alone does not prove that.
2. **Why put in \$3.0m?** Not to protect the \$0.6m mark (sunk-cost reasoning scores 0). The only reason is a positive NPV on new money: +\$623k on the stated scenarios, driven by the recovery case. A strong answer adds the break-even (10.5%) and states that the cure is a cap-rate bet.
3. **What does the bank want?** Recovery and regulatory comfort. Its own numbers: about 90% from a cooperative outcome versus 86% from foreclosure and 80% from a note sale. A strong answer uses the \$593k difference as the value of sponsor cooperation and notes that bank-specific constraints (capital, CRE concentration, examiner pressure) can override recovery maximization.
4. **Next 90 days if we do nothing?** The cure period (60 days) lapses; the bank can declare default on the LTV covenant, sweep continues (\$178k a year diverted), default interest may accrue, and the bank may appoint a receiver or start foreclosure. Equity mark goes to zero in practice. A strong answer notes carve-out guarantee exposure if the sponsor takes any action that triggers recourse.
5. **60-day price?** About \$12.7m (8.49% implied cap), from the opportunistic buyer's 11% DCF. It differs from the 7.50% appraisal because the appraisal measures value in an orderly sale with typical marketing time, while a 60-day sale is priced by the one buyer type that can close without financing and demands a premium for immediacy and for the information asymmetry of a distressed seller (Chapter 1).
6. **Recovery drivers.** Leasing the vacant suites (each \$40k of NOI is about \$533k of value at 7.50%), cap-rate compression if rates fall, and a health-system lease. The sponsor can influence leasing (TI budget, broker incentives) but not cap rates. A strong answer separates the controllable from the uncontrollable, as in Chapter 9's IRR decomposition.
7. **Another tenant leaves.** A further 3.97% NOI decline breaches the DSCR covenant (event of default on income), removing the sponsor's argument that the loan is performing. The sponsor's negotiating leverage falls sharply; the cure analysis must be redone with a lower recovery probability.
8. **Fund contagion.** Check cross-default clauses, cross-collateralization, and whether the bank lends on other fund assets. A strong answer notes reputational value with a relationship lender and the risk that a contested foreclosure impairs future financing for the fund.
9. **Structural change at acquisition.** Examples with numbers: 60% LTV (\$12.0m loan) would leave LTV at about 83% after the shock, still a breach of 75% but a cure of about \$1.2m [check: $12.0\text{m} - 0.75 \times 14.4\text{m} = \$1.2$m, ignoring amortization]; or negotiate the LTV maintenance covenant out of the loan (common in non-bank and CMBS loans, at a higher rate), relying on DSCR and DY tests only. A strong answer prices the trade-off: lower leverage costs return in the base case (Chapter 9, Example 9.8).
10. **When to hand back the keys.** When the bank insists on a full cure and the sponsor's honest recovery probability is below the 10.5% break-even, or when new money would be better deployed elsewhere at the same risk. A strong answer also states the non-financial costs (relationship, guarantees, reputation) and does not treat them as decisive without quantifying them.

Minimum passing committee performance: an average of at least 3.0, with no score of 0 on questions 2, 5, or 10.

## Mode B — Alternative defensible recommendations

* **Cure in full now.** Defensible if the sponsor has strong evidence for the recovery scenario (signed LOIs for the vacant space) and wants to preserve the banking relationship. Must be presented as a new investment with its own NPV, not as protection of the original equity.
* **Cooperative short sale.** Defensible if the sponsor's recovery probability is low and the bank offers a release of guarantees and no deficiency claim. The sponsor gets 0 but avoids carve-out exposure and the cost of a contested foreclosure.
* **Not defensible:** curing "because we have \$6.3m in the deal"; assuming the appraisal value is the sale price; accepting rescue capital at 13% as if the coupon were the investor's expected return.
