# Chapter 17 Solutions

Numerical results are verified in `tests/test_ch17_examples.py` (library: `models/python/sdesk/x_credit.py`). Figures are rounded for display only.

---

### Solution 17.1
(a) $0.018/0.6 = 3.0\%$ is a **risk-neutral** hazard. It includes the risk premium, the liquidity premium and (for U.S. corporates) a state-tax effect, as well as expected default. Comparing it with historical default rates shows only that the spread contains premia, which is normal (Elton, Gruber, Agrawal and Mann, 2001). To call the bond cheap you need a decomposition (§17.4.3): an estimate of the real-world PD and recovery, a liquidity estimate, and a comparison of the residual premium with the premium on comparable bonds or with your own required compensation for recession-concentrated risk.

(b) The fulcrum is the most senior class not paid in full at the estimated enterprise value. Seniors are paid out; juniors get little or nothing; the fulcrum receives most of the reorganized equity. It therefore carries the residual upside if value exceeds the plan valuation, and it controls the plan through its vote and, usually, the new board. A cheap junior bond can be worthless; a cheap senior bond is capped at par. The fulcrum is where valuation disputes are decided and where mispricing is largest.

(c) CDS pays only on a credit event of its reference entity and is settled on that entity's deliverable obligations. Holdco notes without an Opco guarantee are claims on Opco's residual equity, so Holdco noteholders can lose most of their principal while Opco's creditors are paid in full and Opco CDS pays little or nothing (Example 17.6).

### Solution 17.2
(a) $\lambda = 0.03/0.60 = 5.0\%$.
(b) $1 - e^{-0.05 \times 5} = 1 - e^{-0.25} \approx 1 - 0.78 = 22\%$ (exact **22.12%**).
(c) $1 - e^{-0.05} \approx 0.05 - 0.00125 = 4.88\%$ (exact **4.877%**).

### Solution 17.3
(a) Severity 35%: pool loss $= 0.20 \times 0.35 = 7\%$, below the 8% attachment; tranche loss **0**. Severity 50%: pool loss **10%**; tranche loss $= (10 - 8)/(12 - 8) = $ **50%**.
(b) $DR^* = a/\delta = 0.08/0.50 = $ **16%**.

### Solution 17.4
(a) $\lambda_{0,3} = -\ln(0.925)/3 = 0.077962/3 = $ **2.599%**. $\lambda_{0,5} = -\ln(0.87)/5 = 0.139262/5 = $ **2.785%**. One-year hazard $= -\ln(0.98) = $ **2.020%**.
(b) $\lambda_{1,3} = [\ln 0.98 - \ln 0.925]/2 = (-0.020203 + 0.077962)/2 = $ **2.888%**. $\lambda_{3,5} = [\ln 0.925 - \ln 0.87]/2 = (-0.077962 + 0.139262)/2 = $ **3.065%**. The hazard rises with horizon, as is typical for an investment-grade-like class: survivors deteriorate before they default.
(c) $(0.130 - 0.075)/(1 - 0.075) = 0.055/0.925 = $ **5.95%**. Check: $1 - e^{-2 \times 0.030650} = 5.95\%$.
(d) $s_3 = 0.02599 \times 0.65 = $ **169 bp**; $s_5 = 0.02785 \times 0.65 = $ **181 bp**. If the table is real-world history, observed spreads should exceed these by the risk premium and the liquidity component. Spreads equal to these numbers would compensate only for expected losses, leaving nothing for bearing default risk that clusters in recessions.

### Solution 17.5

| Class | Claim | \$300m | \$380m | \$240m |
|---|---|---|---|---|
| Admin | 15 | 100% | 100% | 100% |
| First lien | 160 | 100% | 100% | 100% |
| Second lien | 90 | 100% | 100% | 65/90 = **72.22%** |
| Unsecured notes + trade | 150 | 35/150 = **23.33%** | 115/150 = **76.67%** | 0% |
| Subordinated | 50 | 0% | 0% | 0% |
| Fulcrum | | Unsecured | Unsecured | Second lien |

(a) After admin, first and second liens ($15 + 160 + 90 = 265$), \$35m remains for \$150m of unsecured claims: notes receive \$28.0m, trade \$7.0m.
(b) \$115m remains: notes \$92.0m, trade \$23.0m. The unsecured class is still the fulcrum; subordinated notes are still out of the money. Note that the subordinated class needs value above \$415m to recover anything.
(c) \$240m − 15 − 160 = \$65m for the second lien: 72.22%. Its \$25m deficiency claim is unsecured under §506(a) and shares pro rata with the \$150m of unsecured claims, but because both liens cover all assets, there is no unencumbered value to share. The deficiency claim matters only if unencumbered assets exist (cash outside the collateral, avoidance-action proceeds, some IP). It also gives the second lien a vote in the unsecured class, which can block a plan.

### Solution 17.6
(a) $\lambda = 0.032/0.60 = $ **5.333%**. $RPV01 = \sum_{i=1}^{20} 0.25\,e^{-(0.03 + 0.05333)i/4} = $ **4.0467**. Upfront $= (0.032 - 0.010) \times 4.0467 = $ **8.90 points**, **\$890,266**, paid by the protection buyer. Running premium $0.01 \times 10{,}000{,}000 = $ **\$100,000** a year (\$25,000 a quarter).
(b) At 250 bp: $\lambda = 4.1667\%$, $RPV01 = 4.1647$, upfront $= 0.015 \times 4.1647 = $ **6.25 points** (\$624,705). Mark-to-market for the protection buyer $= 6.247 - 8.903 = $ **−2.66 points**, **−\$265,562**.
(c) Linear: $-0.0070 \times 4.0467 = -2.83$ points (−\$283,267). It overstates the loss because RPV01 rises as spreads tighten: each remaining basis point of premium is worth more when survival is more likely. The actual change uses the average risky annuity over the move.

### Solution 17.7
(a) $d_1 = [\ln(50/35) + (0.04 + 0.0162) \times 2]/(0.18\sqrt2) = (0.356675 + 0.1124)/0.254558 = 1.8427$; $d_2 = 1.5881$.
$E = $ **\$17.87m**, $D = $ **\$32.13m**, yield $= \ln(35/32.130)/2 = $ **4.278%**, spread **27.8 bp**, risk-neutral PD $N(-1.5881) = $ **5.61%**.
(b) $V = 40$: $E = $ **\$8.71m**, $D = $ **\$31.29m**, yield **5.607%**, spread **160.7 bp**, PD **23.84%**.
(c) Equity fell $17.870 - 8.713 = \$9.16$m against a \$10m fall in property value, a ratio of **0.916**. The ratio is the average delta of the call over the move (0.967 at \$50m, 0.833 at \$40m). The lender absorbed the other \$0.84m. As value falls toward the debt, a growing share of each further loss falls on the lender, which is what a short put means.

### Solution 17.8
(a) Opco claims total \$240m. Holdco value $= V - 240$.

| Opco value | p | To Holdco | Holdco recovery |
|---|---|---|---|
| \$260m | 0.35 | \$20m | **13.33** |
| \$320m | 0.45 | \$80m | **53.33** |
| \$400m | 0.20 | \$160m | **100** (\$10m to old equity) |

$E[\text{recovery}] = 0.35(13.33) + 0.45(53.33) + 0.20(100) = 4.67 + 24.0 + 20.0 = $ **48.67**. Multiple $48.67/30 = $ **1.622x**. IRR $= 1.6222^{1/2} - 1 = $ **27.37%**.

(b) With \$40m of priming debt, Opco claims are \$280m:

| Opco value | To Holdco | Recovery |
|---|---|---|
| \$260m | 0 | **0** |
| \$320m | \$40m | **26.67** |
| \$400m | \$120m | **80.0** |

$E[\text{recovery}] = 0 + 0.45(26.67) + 0.20(80) = 12.0 + 16.0 = $ **28.0**, below the price of 30 (IRR on expected recovery $-3.39\%$).

(c) **Rubric.**

| Criterion | Full credit |
|---|---|
| Arithmetic | Correct recoveries with and without priming |
| Mechanism | Recognizes that the priming basket transfers value from Holdco notes dollar for dollar, because Holdco sits below every Opco claim |
| Information | Asks for the Opco indenture's permitted-lien and debt baskets, unrestricted-subsidiary capacity, and the company's liquidity runway (which determines whether it will need to use the basket) |
| Decision | Either (i) a small position sized so the zero-recovery outcome is tolerable, with an explicit plan to organize with other holders to block or participate in the priming financing; or (ii) abstain until basket capacity is known. A full-size purchase on the 27% IRR fails |
| What would change it | An Opco guarantee (moves the notes into Opco's unsecured class); a covenant capping secured debt; evidence that the company has liquidity for 24 months without new money |

Competing view: if the noteholders can provide the priming financing themselves, they can capture its economics. That turns a threat into an opportunity, but only for holders large enough to be invited.

### Solution 17.9
(a) Tranche loss $= \min(\max(L - 0.065, 0), 0.045)/0.045$:

| Pool loss | p | Tranche loss | Principal returned | Total cash (4 × 4.0 + principal) |
|---|---|---|---|---|
| 4% | 0.40 | 0 | 100.0 | 116.0 |
| 8% | 0.35 | 33.33% | 66.67 | 82.67 |
| 12% | 0.25 | 100% | 0 | 16.0 |

Expected principal $= 0.40(100) + 0.35(66.67) + 0.25(0) = $ **63.33**. Expected total cash $= $ **79.33**.

(b) IRR on expected flows $[-72;\ 4;\ 4;\ 4;\ 67.33]$ is **2.66%**. Scenario IRRs: **13.51%**, **3.81%**, **−41.33%**. At 72 the bond earns less than Treasuries on these probabilities.

(c) Conditional expected cash if not 12%: $\bar G = (40 \times 116 + 35 \times 82.67)/75 = 100.44$. Solve $(1 - q)100.44 + 16q = 72$: $q^* = 28.44/84.44 = $ **33.7%** (undiscounted, so it is generous to the buyer).

(d) $CE = 65/700 = $ **9.29%**. Not as good as it looks because the loans that pay off at par are the ones that could refinance. The remaining \$700m pool is more concentrated in loans that could not, including the office loans, so the expected loss rate on the remaining pool rises as CE rises.

(e) The coupon will not be paid in full in the 8% and 12% scenarios. Appraisal reductions on specially serviced loans cut advances (Chapter 12, Example 12.5), and the interest shortfall hits the most junior outstanding classes first, so Class D loses interest well before principal losses are realized. The assumption overstates the bond's value. A defensible bid is below the price implied here.

### Solution 17.10
(a) Second-lien recovery $= \min(200, \max(V - 315, 0))/200$: at \$380m, **32.5**; at \$450m, **67.5**; at \$520m, **100** (with \$5m above the second lien). Recovery equals the price of 55 at $V = 315 + 110 = $ **\$425m**.

(b) Facts and how they change the answer:

| Fact | Why it matters |
|---|---|
| Intercreditor agreement | Whether the second lien can object to a DIP loan, credit-bid, or must turn over recoveries; whether it has waived rights to contest the first lien's valuation |
| Unrestricted subsidiary | If eight hotels sit outside the collateral, the relevant value for the second lien is the remaining hotels only. The \$380–520m range may overstate its collateral |
| Franchise defaults | Termination would cut value and force a rebrand or PIP (Chapter 11); the franchisor's consent may be a condition to any plan |
| Who owns the first lien | An ad hoc group with a low valuation may intend to own the company; the second lien's leverage is its ability to block or litigate |
| Liquidity runway and DIP terms | A priming DIP reduces value available to the second lien |

(c) **Recommendation: abstain for now.** The break-even value of \$425m sits inside the \$380–520m range, so the decision depends on the valuation fight. Two unverified facts, the unrestricted subsidiary and the intercreditor terms, can each move the second lien's recovery by more than the whole margin of safety. A defensible alternative is a small position bought only after reading the intercreditor agreement, at a price that is break-even at the first-lien group's \$380m valuation (32.5) plus a premium for the option to litigate. Buying at 55 without these facts is a bet on the sponsor's valuation, which is advocacy.

**Rubric.** Full credit: correct recoveries and break-even; identifies the unrestricted-subsidiary issue as a collateral question, not a valuation question; treats both valuations as advocacy; abstains or sizes small with explicit conditions. Partial: correct arithmetic with a buy recommendation conditioned on the midpoint. No credit: buys on the sponsor's \$520m.

### Decision exercise (§17.9) — notes for the grader
Harborline's Opco claims (\$380m) are covered in every scenario, so the Holdco notes are the fulcrum in all three cases: at \$400m and \$500m they are impaired and receive Holdco's equity in Opco; at \$600m they are paid in full and old Holdco equity keeps \$20m. Credit the candidate who notices that at \$600m no class is impaired and Holdco may not need to restructure the notes at all. The CMBS bid should come from scenarios like Problem 17.9, not from the rating; on those scenarios 72 is too high.
