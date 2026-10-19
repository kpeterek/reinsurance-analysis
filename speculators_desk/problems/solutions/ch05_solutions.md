# Chapter 5 Solutions

Numerical results are verified in `tests/test_ch05_examples.py`. Figures are rounded for display only. All inputs are hypothetical [HYPOTHESIS] unless cited.

---

### Solution 5.1
(a) In an ample-reserves regime, banks hold more reserves than they need, so the marginal value of an extra dollar of reserves is set by what the Fed pays on it, not by scarcity. **IORB** is the main tool. A bank will not lend overnight much below IORB, and it will borrow from institutions without IORB access (chiefly the Federal Home Loan Banks) whenever it can do so below IORB. That keeps EFFR close to, and usually slightly below, IORB. The **ON RRP** gives money funds and other eligible non-banks a risk-free alternative at the bottom of the range, which sets a soft floor under repo and other secured rates. The **SRF** and the **primary credit rate**, both at the top of the range (4.00% at 16 September 2026), cap how much eligible institutions need to pay for overnight cash. The FOMC changes all of these together when it moves the range.

(b) Two explanations. (i) **Reserves are becoming less than ample.** The demand curve for reserves has steepened, so small reserve drains (Treasury General Account rebuilds, tax dates, runoff) push rates up. Implication: the Fed may slow or end runoff, or add reserves through purchases. (ii) **Temporary frictions**: quarter-end window dressing, heavy Treasury settlements, or a shift in the mix of fed funds lenders. Implication: no balance-sheet change is needed. Distinguish the two by persistence and by whether repo rates (SOFR) are also elevated relative to IORB and whether SRF usage is rising.

(c) The borrower's coupon is SOFR + spread. If money markets tighten, SOFR can drift up relative to the policy range even with no FOMC action. A 5–10 bp persistent drift on a \$40 million loan is \$20,000–\$40,000 of extra annual interest. It also signals funding stress that can precede tighter lending conditions.

### Solution 5.2
(a) $100 - 96.18 = 3.82\%$.
(b) Expected change $= 3.82 - 3.88 = -0.06$, so $p(\text{cut}) = 0.06/0.25 = 24\%$.
(c) \$41.67 per basis point (\$4,167 per index point ÷ 100).
Because M+1 lies entirely after the meeting, no day-weighting is needed. This is why the next-month contract is the cleaner instrument when the meeting is late in the month.

### Solution 5.3
Approximate: $4.50\% - 2.30\% = 2.20\%$. Exact: $1.045/1.023 - 1 = 2.1505\%$.
The quoted TIPS yield can differ from both because (i) the breakeven quoted may be computed as a simple difference, not exactly; (ii) TIPS and nominal maturities and coupon structures rarely match exactly; and (iii) breakevens include an inflation risk premium and a TIPS liquidity premium, so "real yield" in the Fisher sense (nominal minus *expected* inflation) is not the same as the TIPS yield.

### Solution 5.4
(a) $1.0 + 2.6 + 0.5(0.6) + 0.5(0.5) = 1.0 + 2.6 + 0.30 + 0.25 = 4.15\%$.
(b) $1.0 + 2.6 + 0.30 + 1.0(0.5) = 4.40\%$.
(c) $1.0 + 3.2 + 0.5(1.2) + 0.25 = 1.0 + 3.2 + 0.60 + 0.25 = 5.05\%$.
(d) $0.8 \times 3.875 + 0.2 \times 4.15 = 3.100 + 0.830 = 3.93\%$.
(e) The choice of inflation measure alone moves the prescription by 90 bp (4.15% to 5.05%), and the gap weighting adds 25 bp. The underwriter should stress floating debt service at the upper end of the rule band (about 5%), not at the rule's central value, because the Committee's reaction function is not known to that precision.

### Solution 5.5
(a) $\bar R = 100 - 96.07 = 3.93\%$.
$E[r_1] = (31 \times 3.93 - 17 \times 3.88)/14 = (121.83 - 65.96)/14 = 55.87/14 = 3.99071\%$.
$p = (3.99071 - 3.88)/0.25 = 44.29\%$.
(b) Naive: $(3.93 - 3.88)/0.25 = 20.0\%$, which understates $p$ by the factor $14/31$.
(c) No. One price gives one equation, $E[r_1] = r_0 + 0.25p_{25} + 0.50p_{50}$, in two unknowns. Any combination with $0.25p_{25} + 0.50p_{50} = 0.11071$ fits, for example $(p_{25}, p_{50}) = (44.3\%, 0)$ or $(0, 22.1\%)$. You need options on fed funds or SOFR futures, a second contract with a different exposure to the same meeting, or an explicit assumption (for example, that 50 bp is ruled out by guidance). State the assumption.

### Solution 5.6
Interest $= 45{,}000{,}000 \times (SOFR + 0.035) \times 365/360$.
(a) $45{,}000{,}000 \times 0.0735 \times 1.013889 = \$3{,}353{,}438$; DSCR $= 4{,}000{,}000/3{,}353{,}438 = 1.193$x.
(b) $45{,}000{,}000 \times 0.0785 \times 1.013889 = \$3{,}581{,}563$; DSCR $= 1.117$x.
(c) Capped SOFR 4.25%: $45{,}000{,}000 \times 0.0775 \times 1.013889 = \$3{,}535{,}938$; DSCR $= 1.131$x.
(d) Cap payout $= 45{,}000{,}000 \times (0.0435 - 0.0425) \times 365/360 = \$45{,}625$ per year.
The cap is struck high enough that it protects only the last 10 bp. A cap struck near current SOFR would have cost more upfront. Whether the strike was right depends on the covenant levels (see Problem 5.9).

### Solution 5.7
Appraised value $= 1{,}800{,}000/0.0625 = \$28{,}800{,}000$.
(a) Coupon $= 4.30\% + 1.80\% = 6.10\%$; $K = 0.072719$.
LTV: $0.60 \times 28{,}800{,}000 = \$17{,}280{,}000$. DSCR: $1{,}800{,}000/(1.30 \times 0.072719) = \$19{,}040{,}529$. Debt yield: $1{,}800{,}000/0.09 = \$20{,}000{,}000$. **Maximum loan \$17,280,000 (LTV binds).**
(b) Coupon $= 6.75\%$; $K = 0.077832$. DSCR: \$17,789,848. LTV unchanged at \$17,280,000. **Maximum loan unchanged at \$17,280,000 (LTV still binds)**, although DSCR headroom fell from \$1.76 million to \$0.51 million.
(c) Value $= 1{,}800{,}000/0.0675 = \$26{,}666{,}667$. LTV: \$16,000,000. **Maximum loan \$16,000,000 (LTV binds)**, a 7.4% decline from (a).
(d) The rate shock reduced DSCR capacity, but LTV was the tighter constraint, so proceeds did not change until the appraisal moved. The private market transmits rates to proceeds in two steps: immediately through DSCR only where DSCR binds, and later through value. An analyst who sees "no change in proceeds" after a rate shock should check the headroom on the non-binding constraints, because the next appraisal can make them bind.

### Solution 5.8
(a) Value at 5.50%: $2{,}000{,}000/0.055 = \$36{,}363{,}636$.
$\beta = 0.5$: cap $= 5.625\%$, value $= \$35{,}555{,}556$ (−2.22%).
$\beta = 1.0$: cap $= 5.75\%$, value $= \$34{,}782{,}609$ (−4.35%).
(b) The seller's \$36.0 million floor sits above both shocked values. A disciplined answer is to bid in the range \$34.8–\$35.6 million, or to pass.

**Rubric (Level 4).**

| Element | Credit |
|---|---|
| Computes the three values correctly | 25% |
| Recognizes that the broker's comps predate the yield move and are stale by construction | 15% |
| Questions the attribution to term premium: a decomposition is model-dependent, and a rise in the expected policy path has different implications for financing | 15% |
| Treats $\beta$ as uncertain and shows the range rather than a point | 15% |
| States a price and conditions (financing contingency, rate lock, or price adjustment tied to the 10-year at closing) | 20% |
| Accepts passing as legitimate if the seller holds at \$36.0 million | 10% |

**Competing explanations.** (i) The rise is transitory issuance pressure that will reverse: then bidding near the seller's floor is reasonable if you can lock financing. (ii) It reflects a persistently higher term premium: then the lower end is right. (iii) NOI growth expectations have risen with inflation, offsetting the rate effect: then the cap may not move at all. **What would change the conclusion:** new comparable sales after the yield move; a fixed-rate quote with a rate lock; evidence on rent growth.

### Solution 5.9
Interest $= 25{,}000{,}000 \times (SOFR + 0.03) \times 365/360$.
(a) Futures path (3.60%): \$1,672,917; DSCR 1.315x. House view (3.35%): \$1,609,549; DSCR 1.367x. No cuts (3.88%): \$1,743,889; DSCR 1.262x.
(b) $SOFR^\dagger = 2{,}200{,}000/(1.15 \times 25{,}000{,}000 \times 365/360) - 0.03 = 4.547\%$.
(c) **Model answer.** Underwrite at the market path at most, and size covenants and the cap to the no-cut path and above. The futures-implied path is the price at which the risk can be hedged today. A house view that is more dovish than the market is a speculation on the Fed, and it should be expressed (if at all) as a separate, sized position, not hidden inside a property's debt underwriting. The covenant breaks at 4.55% SOFR, only about 67 bp above today's rate. A 25 bp difference in path views is small next to the hike scenario that breaches the covenant.

**Rubric (Level 4).** Correct DSCRs (30%); break-even SOFR (20%); separates the hedgeable market path from a house view (20%); identifies the covenant cushion as the binding risk and recommends a cap at or below the trigger (20%); notes that NOI risk and rate risk may be correlated (10%).

### Solution 5.10
(a) Competing explanations:
1. **Household salience.** Households react to recent price changes in visible goods; the survey may lag the oil decline or reflect food and services prices. Breakevens respond to the oil fall at once.
2. **Risk and liquidity premia.** The breakeven fall could be a fall in the inflation risk premium or a flight to nominal Treasuries, not a fall in expected inflation.
3. **Horizon mismatch.** The survey is one-year; the breakeven is five-year; 5y5y is unchanged. Near-term expectations may diverge while long-run expectations remain anchored.
4. **Sampling noise.** A 0.8-point move in a monthly household survey may be within its normal month-to-month variability. Check the survey's own error and history before treating it as a signal.

(b) **Fed funds futures position: abstain.** There is no identified informational edge. The divergence has several explanations that point in opposite directions, and speakers disagree. The futures price already aggregates this information. Expected P&L at the market-implied probability is zero before costs (Example 5.4). **Accelerating the acquisition: do not accelerate on this rationale.** The closing date should be driven by diligence and financing. If rate risk is the concern, buy the cap or lock the rate. Do not compress diligence to front-run a Fed decision you cannot forecast.

(c) Data that would change the view: a rise in 5y5y breakevens or in professional-forecaster long-horizon expectations (de-anchoring risk); core services inflation prints; a clear shift in the Chair's guidance; a widening of the futures-implied path relative to the rule band in Example 5.2.

**Rubric (Level 5).**

| Element | Weight |
|---|---|
| At least two competing, mechanism-based explanations | 25% |
| Correctly separates horizons (1-year vs 5-year vs 5y5y) | 15% |
| Identifies abstention as the best answer for the futures trade, with a reason | 25% |
| Rejects deal acceleration as a substitute for hedging; proposes the hedge | 20% |
| Names specific data that would change the view | 15% |

---

### Decision exercise (chapter §5.10): model numbers

* Implied hike probability: 68.57% (meeting month) and 68.0% (next month). Naive: 32.0%.
* Fixed refinance at a 4.50% 10-year + 2.00% spread with the high-rate appraisal (6.00% cap): maximum loan \$25,313,731 (DSCR binds); gap \$4,986,269 including 1% costs (Example 5.7).
* Floating extension at SOFR + 3.50% on \$30,000,000, actual/360: at SOFR 3.88%, interest \$2,244,750 and DSCR 1.069x. At SOFR 4.88% (forward + 100 bp stress), interest \$2,548,917 and DSCR 0.942x. A cap is necessary, and its strike should be below about 4.39% SOFR to keep DSCR at or above 1.00x (break-even SOFR $= 2{,}400{,}000/(30{,}000{,}000 \times 365/360) - 0.035 = 4.390\%$).
