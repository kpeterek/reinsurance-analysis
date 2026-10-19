# Chapter 13 Solutions

Numerical results are verified in `tests/test_ch13_examples.py`. Figures are rounded for display only.

---

### Solution 13.1
(a)
* **2018 price:** sunk. It affects nothing a buyer will pay or the property will earn.
* **\$12.0m original equity:** sunk. The capital at stake today is equity at market, not equity contributed.
* **19% since-inception IRR:** a performance-reporting number. It says nothing about the forward return of holding.
* **Current bid:** relevant. It sets equity at market, $E_M = V(1-s) - B - PP$, if the bid is firm.
* **Yield-maintenance cost:** relevant. It is a cost of selling and reduces $E_M$.
* **3.9% coupon:** relevant. Holding keeps below-market debt, which raises the forward levered IRR of holding. Because a buyer cannot assume it, the bid does not pay for it.
* **Tax basis:** relevant for an after-tax decision. A sale crystallizes depreciation recapture and capital gains, and a 1031 exchange or continued holding defers them. The pre-tax analysis in this chapter excludes it; Case F shows how to add it.

(b) "The question is not whether this deal has been a winner. It is whether the \$X of equity we could take out today would earn more held in this building, with this loan, than in our best alternative at the same risk, after the cost of selling and reinvesting. Here is that comparison." The past IRR is irrelevant except as a check on whether our forecasts have been calibrated.

### Solution 13.2
(a) $g = k - c = 8.00\% - 5.25\% = 2.75\%$.
(b) Approximation: $\Delta V/V \approx -\Delta c/c = 0.50/5.25 \approx 9.5\%$. Exact: $5.25/4.75 - 1 = 10.53\%$.
(c) Only if the required return is unchanged at 8.00%: $8.00\% - 4.75\% = 3.25\%$. If the cap rate fell because required returns fell (for example, lower Treasury yields), the implied growth is unchanged at 2.75%. A cap-rate move does not tell you which component moved.

### Solution 13.3
(a) $N = 36{,}000/80 = 450$ contracts short.
(b) Loan PV cost $= -36{,}000 \times 20 = -\$720{,}000$. Hedge $= 450 \times 80 \times 20 = +\$720{,}000$. Net \$0.
(c) Loan cost $= -36{,}000 \times 35 = -\$1{,}260{,}000$. Hedge +\$720,000. Net −\$540,000. The hedge covers the Treasury component only. The 15 bp of spread widening is unhedged.

### Solution 13.4
(a) $E_M = 18{,}000{,}000 \times 0.98 - 9{,}000{,}000 = \$8{,}640{,}000$.

(b) NOI years 1–5: 1,000,000; 1,025,000; 1,050,625; 1,076,891; 1,103,813. Interest \$450,000.
Reversion at year 4 $= 1{,}103{,}813/0.06 \times 0.98 - 9{,}000{,}000 = 18{,}396{,}882 \times 0.98 - 9{,}000{,}000 = \$9{,}028{,}944$.
Flows: −8,640,000; 550,000; 575,000; 600,625; 9,655,835. **Hold IRR = 7.78%.**

(c) The exit cap at which the hold IRR equals 8.50% is **5.91%**, below the 6.00% base case.

(d) **Sell**, if the 8.50% alternative is real and of equal risk. Holding requires believing the exit cap will be at or below 5.91%. That is about 35 bp above today's 5.56% going-in cap rate, but 9 bp below your own 6.00% base case. You would be holding against your own forecast. Unlike Example 13.1, there is no below-market debt to keep: the loan is prepayable at par, so the hold has no financing advantage. The recommendation changes if (i) the alternative's 8.50% is not available at the same risk, or is uncertain to close; (ii) a tax deferral (1031) is available only if the proceeds are reinvested, which changes the alternative; or (iii) you have specific information that NOI growth will exceed 2.5%, such as below-market leases rolling.

### Solution 13.5
(a) $\sigma_p = \sqrt{0.36(0.01) + 0.16(0.0324) + 2(0.6)(0.4)(0.10)(0.18)\rho}$:
* $\rho = 0.3$: **10.67%**
* $\rho = 0.8$: **12.53%**
* $\rho = 1.0$: **13.20%** (= $0.6 \times 10\% + 0.4 \times 18\%$)

(b) Use the stress correlation, 0.8 or higher. A reserve exists for the downturn, and the evidence is that the markets fall together in downturns. The 0.3 estimate is dominated by calm periods and, if it comes from appraisal-based data, is also biased by smoothing (Chapter 2).

(c) Equity volatility $= \sigma_p/0.40$: 26.66%, 31.32%, 33.00%.

### Solution 13.6
(a) $q = (1 + 0.05 - 0.06 - 0.80)/(1.25 - 0.80) = 0.19/0.45 = 0.4222$.
(b) NPV now $= 20.0 - 18.5 = \$1.50\text{m}$. Wait: up $25.0 - 18.5 = 6.5$; down $16.0 - 18.5 < 0$, so 0. Option $= 0.4222 \times 6.5/1.05 = \$2.614\text{m}$. **Value of waiting $= 2.614 - 1.500 = \$1.114\text{m}$.** Wait.
(c) Indifference requires $q \times 6.5/1.05 = 1.5$, so $q^* = 0.2423$. Then $\delta^* = 1 + 0.05 - 0.80 - 0.2423 \times 0.45 = 14.10\%$. Waiting would be worse than building now only if the completed building yielded more than 14.1% a year. The forgone cash yield is the cost of waiting, and at a 6% yield it is far too small to offset the value of avoiding the down state.

### Solution 13.7
(a) Year 1: office $2.40 - 2.40 = 0$; MF $1.425 - 1.00 = 0.425$. **Net +\$0.425m.**
Year 2: office $1.95 - 2.40 - 1.50 = -1.95$; MF +0.425. **Net −\$1.525m.**
Office value at maturity $= 1.95/0.09 = \$21.67\text{m}$. New loan $= 0.50 \times 21.67 = \$10.83\text{m}$. **Maturity gap $= 25.00 - 10.83 = \$14.17\text{m}$.**

(b) Cumulative: year 1 +0.425; year 2 $0.425 - 1.525 - 14.167 = -15.267$. **Reserve = \$15.27m.**

(c) $15.27 \times (0.10 - 0.045) = \$0.84\text{m}$ a year.

(d) Alternatives: (1) refinance or extend the office loan now, before the tenant leaves, which requires current lender terms and the cost of any prepayment; (2) sell the office now, which requires a current bid and an estimate of the buyer's view of the rollover; (3) arrange committed contingent capital, such as a preferred-equity commitment or a partner's capital call, which requires its fee and conditions; (4) negotiate with the tenant to extend early, which requires the cost of the concession package.

**Rubric (Level 4).**

| Criterion | Points |
|---|---|
| Correct year-by-year cash flows including TI/LC | 3 |
| Maturity gap computed at stressed value and stressed LTV | 3 |
| Reserve as the minimum cumulative balance, not the sum of shortfalls | 2 |
| Opportunity cost computed and compared with at least two alternatives | 3 |
| Recognizes that the reserve is driven by one maturity and addresses it directly | 3 |
| States what would change the conclusion (a lender extension, a tenant renewal) | 2 |

Mastery: 13 of 16.

### Solution 13.8
(a) Cash $= 18.0 - 15.0 - 0.40 - 0.18 = \$2.42\text{m}$.
(b) Incremental interest $= 18.0 \times 6.25\% - 15.0 \times 3.90\% = 1.125 - 0.585 = \$0.540\text{m}$ a year. Lender-side flows: −2.42; +0.54 for four years; +3.0 extra principal at year 4. **Marginal cost = 26.39%.**
(c) No. The development investment's 15% expected return is below the 26.4% marginal cost of this capital, and development equity is riskier than debt. Alternatives to price: a supplemental or second-lien loan that leaves the 3.90% first mortgage in place; preferred equity at the project level; a partner's capital; selling a different, lower-return asset; or deferring the development, which may itself have option value (§13.4.8).

**Rubric (Level 4).**

| Criterion | Points |
|---|---|
| Cash released net of prepayment and fees | 2 |
| Incremental flows set up correctly, including the balance difference at maturity | 3 |
| Marginal cost computed and compared with the use of proceeds on a risk-adjusted basis | 3 |
| At least two alternative sources priced or specified | 3 |
| Notes that the headline 6.25% is the wrong comparison | 2 |

Mastery: 11 of 13.

### Solution 13.9
(a) All six: mean 246.7 bp, sample s.d. 70.3 bp, $z = (330 - 246.7)/70.3 = 1.18$. Last three only: mean 310.0, s.d. 10.0, $z = 2.00$.

(b) What you need to know before acting:
* **Comparability.** Two sources with different definitions are mixed. Broker-survey cap rates and closed-transaction cap rates are not comparable, and the transaction series includes distressed sales, which raise cap rates. The current 330 bp figure is from the survey, but the three most recent comparable observations are from transactions.
* **Regime.** A level shift of about 120 bp occurred between observation 3 and observation 4. If suburban office's risk and growth outlook changed structurally, for example through remote work, the earlier observations are not from the same distribution, and "mean reversion" to 247 bp is not a forecast.
* **Implied growth.** At equal required returns, a 330 bp spread implies office NOI growth 330 bp a year below multifamily. Is that too pessimistic? That requires lease-rollover, vacancy, and TI/LC data, not cap rates.
* **Executability.** Can you buy suburban office at the survey cap rate? Transaction evidence suggests the clearing level may be different.

(c) **Recommended answer: no position now.** The data cannot distinguish a mispricing from a regime change, and the series mixes two definitions. Ask for a consistent transaction-based series, at least 15–20 years of it, with distressed sales flagged. Ask also for an explicit forecast of office NOI growth with lease-by-lease rollover. Revisit when the spread is measured consistently and the implied growth gap can be compared with a fundamentals-based forecast.

**Rubric (Level 5).**

| Criterion | Points |
|---|---|
| Computes both z-scores and notes their sensitivity to the sample | 2 |
| Identifies the mixed-source problem | 3 |
| Identifies the possible regime change and explains why mean reversion may not apply | 3 |
| Translates the spread into an implied growth differential ($c = k - g$) | 2 |
| Recommends abstention, or a small, explicitly experimental position with a stated invalidation, and specifies the data needed | 3 |
| Avoids the claim that a high z-score alone is a trade | 2 |

Mastery: 12 of 15. Recommending a full-size overweight on these data scores at most 6.

### Solution 13.10
(a) Loan DV01 = **\$22,632**. Full hedge $= 22{,}632/80 = 282.9 \to 283$ contracts. Probability-weighted $= 0.7 \times 282.9 = 198.0 \to 198$ contracts.

(b) Loan PV effect for ±40 bp: ∓\$905,262. Hedge P&L: full hedge ±\$905,600; partial hedge ±\$633,600.

| Hedge | Treasuries | Deal closes | Deal fails |
|---|---|---:|---:|
| 283 (full) | +40 bp | +338 | +905,600 |
| 283 (full) | −40 bp | −338 | −905,600 |
| 198 (weighted) | +40 bp | −271,662 | +633,600 |
| 198 (weighted) | −40 bp | +271,662 | −633,600 |

(c) +40 bp, expected P&L: full hedge $0.7(338) + 0.3(905{,}600) = +\$271,916$; weighted hedge $0.7(-271{,}662) + 0.3(633{,}600) = -\$84$, approximately zero.

The weighted hedge has expected P&L close to zero in both rate scenarios, so it is unbiased. The full hedge is, in expectation, a 30% naked short position in Treasuries. It gains about \$272,000 if rates rise and loses the same if they fall.

(d) A defensible answer: hedge about 70% of DV01, or lock the rate with the lender if a rate-lock agreement is available with a fee that is refundable or reduced if the deal fails. Revisit the hedge size as the probability of closing changes (for example, after the inspection period ends). A forward-starting swap has the same closing-risk problem as futures. Doing nothing is also defensible if the acquisition's returns are robust to a ±50 bp change in the loan rate and the buyer's equity can absorb it. Then the hedge buys little.

**Rubric (Level 5).**

| Criterion | Points |
|---|---|
| Correct DV01 and both contract counts | 2 |
| Scenario table with closing risk | 3 |
| Recognizes that a full hedge on an uncertain deal is partly speculative | 3 |
| Discusses basis (spread) risk even though spreads are held constant here | 2 |
| Chooses an instrument and explains its residual risk | 3 |
| States when the hedge would be resized | 2 |

Mastery: 12 of 15.

---

## Decision exercise (§13.10) — rubric and model answer

**Model answer (one defensible version).**

1. **Multifamily:** hold. Forward levered IRR on equity at market is 11.21% against 9.01% for the industrial alternative. The break-even exit cap is 5.57%. Do not refinance: the marginal cost of the cash-out is 26.99%. Invalidation: a bid that implies a break-even exit cap below our own exit forecast, or a buyer who will assume the loan and pay for it.
2. **Liquidity:** the Example 13.6 stress requires \$10.57m, almost all for the hotel maturity, and costs about \$0.74m a year to hold. Preferred action: refinance or extend the hotel loan now, if the cost is less than \$0.74m a year. Otherwise hold the reserve. A second stress, such as a three-year hotel disruption, should also be run.
3. **Pipeline:** hedge with a lender rate lock if available. If not, use 10-year futures sized to the probability of closing, and accept the spread risk explicitly.
4. **Relative value:** no change in hotel allocation on the spread alone (z = 1.05 on ten observations including a pandemic year). The hotel is already 45% of portfolio risk.
5. **Land:** wait with a trigger (Example 13.8: build after an up move; let the option lapse after two down moves). See Case I.
6. **Not doing:** the sell-and-recycle trade, the cash-out refinancing, and any increase in hotel exposure.

**Scoring.** The weights are in §13.10. Deduct heavily for: using the since-inception IRR; comparing going-in yields as returns; sizing a reserve without the maturity; a full hedge with no mention of closing risk; any land decision without a stated trigger.
