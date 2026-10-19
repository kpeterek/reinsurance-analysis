# Chapter 4 Solutions — The Business Cycle

Numerical results are verified in `tests/test_ch04_examples.py` (functions `test_problem_4_k` and `test_decision_exercise`). Figures are rounded for display only. All data are hypothetical unless a source is cited.

---

### Solution 4.1
(a) **Right:** in the expenditure identity, imports are subtracted, so a rise in imports lowers net exports' *contribution*. **Misleading:** imports were already counted in consumption, investment or government purchases when the goods were bought. The subtraction removes foreign production from a total that had included it. An import surge accompanied by an equal rise in domestic purchases leaves GDP unchanged. The informative question is whether *domestic demand* (final sales to private domestic purchasers) was strong or weak.

(b) Excluding inventories, GDP grew at about 3.5 − 2.4 = 1.1 points annualized, so the underlying pace of final demand was weak. Inventory accumulation of that size either anticipates demand that has not yet appeared or reflects goods that did not sell. Either way it tends to **reverse**. A drag of a similar size in the following one or two quarters is a material risk [HYPOTHESIS; inventory reversals are common but not guaranteed].

(c) **Accelerator:** investment is driven by the *change* in expected output, because the desired capital stock is proportional to expected output and investment is the flow that closes the gap, plus replacement. A slowdown in expected growth from 3% to 1% cuts the required net additions to capital by about two-thirds, even though output is still rising. Inventories follow the same logic. A sector that is 17% of GDP can therefore fall 10–15% while consumption, 68% of GDP, barely moves, so investment's contribution dominates (Example 4.1).

(d) YoY growth is the compound of the last four quarterly rates. It weights the current quarter one-quarter and includes quarters from up to a year ago. Its "center of mass" is therefore about 1.5–2 quarters in the past, and it turns roughly two quarters after the quarterly rate turns (Example 4.2).

### Solution 4.2
(a) $(1.008)^4 - 1 = 3.24\%$. Mental route: $4 \times 0.8 = 3.2$, plus $6q^2 \approx 6 \times 0.000064 = 0.04$ points.
(b) $(0.996)^4 - 1 = -1.59\%$. Mental route: $-1.6 + 0.01$.
(c) $(1.024)^{1/4} - 1 = 0.59\%$ (exactly 0.5947%). Mental: $2.4/4 = 0.6$, slightly less.
(d) The latest quarter's $q = (0.98)^{1/4} - 1 = -0.50\%$. The cumulative growth of the prior three quarters is $1.01/0.99496 - 1 = +1.51\%$. The economy grew about 2% annualized for three quarters and then contracted. YoY of 1.0% averages the two phases together.

### Solution 4.3
(a) Using GDP = 100 at the start:

| Component | Share | Growth | Contribution |
|---|---|---|---|
| C | 68 | +1% | +0.68 pp |
| I | 17 | −9% | −1.53 pp |
| G | 17 | +2% | +0.34 pp |
| NX | −2 | unchanged | 0.00 pp |
| **GDP** | | | **−0.51%** |

(b) Zero GDP growth requires $17 \times g_I = -(0.68 + 0.34)$, so $g_I = -1.02/17 = -6.0\%$. Any investment decline larger than 6% produces negative GDP growth while consumption and government grow as assumed.

### Solution 4.4
(a) Three-month averages (months 3–18):

| Month | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|
| MA3 | 3.9333 | 3.8667 | 3.8667 | 3.8667 | 3.9000 | 3.9333 | 3.9667 | 4.0333 |

| Month | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|
| MA3 | 4.0667 | 4.1333 | 4.1667 | 4.2333 | 4.3000 | 4.3667 | 4.4333 | 4.5000 |

(b) The minimum of the averages over months 3–14, 4–15, 5–16 and 6–17 is 3.8667 in every window (months 4–6).
Month 15: $4.3000 - 3.8667 = 0.4333$. Month 16: $4.3667 - 3.8667 = 0.5000$. Month 17: 0.5667. Month 18: 0.6333.

(c) **Month 16**, where the indicator equals the 0.50 threshold exactly. Under a strict ">" convention the signal would come in month 17.

(d) With month 4 at 3.9: MA3 for months 4, 5 and 6 become 3.9000, 3.9000 and 3.9000 (months 4: (3.9+3.9+3.9)/3; 5: (3.9+3.9+3.9)/3; 6: (3.9+3.9+3.9)/3), and month 3 stays 3.9333. The window minimum for months 16 and 17 becomes 3.9000.
Month 16: $4.3667 - 3.9000 = 0.4667$. No signal. Month 17: $4.4333 - 3.9000 = 0.5333$. **Signal in month 17**, one month later.

(e) A rule written into policy inherits the indicator's measurement error. A one-tenth revision to a single month from a year earlier delays the trigger by a month, and a strict versus non-strict inequality does the same. The policy should (i) name the vintage (real-time, as first published), (ii) specify "≥ 0.50", and (iii) better, use a graduated response, for example a partial de-risking at 0.30–0.40 and the full response at 0.50, so that a one-month timing difference does not decide the whole action.

### Solution 4.5
(a) Productivity $= 1.012/1.015 - 1 = -0.30\%$. ULC $= 1.04/0.99704 - 1 = +4.31\%$. Productivity fell because hours grew faster than output, a pattern typical of late-cycle labor hoarding.

(b) Revenue $= 20.0 \times 1.01 = \$20.2$m. Labor $= 6.8 \times 1.04 = \$7.072$m. Other costs \$7.6m.
$NOI_1 = 20.2 - 7.072 - 7.6 = \$5.528$m, a change of **−1.29%**, although revenue *rose* 1%. Labor ratio $= 7.072/20.2 = 35.01\%$ (from 34.0%). NOI margin $= 27.37\%$ (from 28.0%).

(c) ULC growth above 4% with negative productivity is inconsistent with 2% inflation and stable margins. Either prices rise or margins compress, so the central bank is likely to stay tight (Chapter 5). For hotels, a pro forma that grows ADR at 1–3% and costs at the same rate assumes away the late-cycle squeeze. Underwrite labor cost per occupied room at expected wage growth less a *demonstrated* productivity gain, not at ADR growth.

### Solution 4.6
(a) $P = \dfrac{0.85 \times 0.12}{0.85 \times 0.12 + 0.15 \times 0.88} = \dfrac{0.102}{0.102 + 0.132} = 43.6\%$.

(b) $P = \dfrac{0.80 \times 0.436}{0.80 \times 0.436 + 0.05 \times 0.564} = 92.5\%$.

(c) LR(curve) $= 0.85/0.15 = 5.67$. LR(Sahm) $= 0.80/0.05 = 16$. The Sahm rule is more informative because it is a **recognition** indicator: it measures the recession's own labor-market footprint. The curve is a **forecast** of policy and growth expectations made months or years ahead, with a long and variable lead and more room for error.

(d) Both signals respond to the same underlying weakness: an inverted curve partly *reflects* expectations of the labor-market deterioration that the Sahm rule later records. Given a recession, they are positively correlated, and given no recession they may be too (a false growth scare can trigger both). Treating correlated evidence as independent double-counts it and **overstates** the posterior. A conservative approach discounts the second likelihood ratio, for example by using its square root, or by building a joint conditional table from history.

(e) $40 \times 0.15 = 6$ expected false signals. The U.S. post-war sample contains roughly a dozen recessions and a few documented false positives, so an estimated false-positive rate rests on a handful of events. Its standard error is of the same order as the estimate, so treat it as a range, not a point.

### Solution 4.7
(a) $z = (0.4 - 0.3)/0.08 = 1.25$. 5-year move $= 5 \times 1.25 = +6.25$ bp.

(b) $40{,}000{,}000 \times 0.000625 = \$25{,}000$ per year more interest.

(c) Loan constant at 6.00%/30 years $= 0.07195$; at 6.0625% $= 0.07243$.
Before: $L = 3{,}200{,}000/1.30/0.07195 = \$34{,}213{,}664$.
After: $L = 3{,}200{,}000/1.30/0.07243 = \$33{,}985{,}556$, a reduction of **\$228,109**.

(d) Sensitivities depend on what the market believes the central bank will do with the information. If inflation is well anchored and policy is on hold for growth reasons, a single hot print may be treated as noise and move yields little. In an inflation-fighting regime the same print raises the probability of further tightening and moves the front end much more. Estimate sensitivities over the current regime, and report the regime with the estimate.

### Solution 4.8
(a) *Hotel:* $NOI_0 = 14.0(0.67) - 5.0 = \$4.380$m. $R_1 = 11.9$m. $NOI_1 = 11.9(0.67) - 5.0 = \$2.973$m: **−32.1%**. $DOL = 9.38/4.38 = 2.14$.
*Apartment:* rolling 3.0m; renewals $3.0 \times 0.55 \times 0.95 = 1.5675$m; re-lets $3.0 \times 0.45 \times 0.95 \times 11/12 = 1.175625$m; vacancy $-0.09$m. $R_1 = \$5.653125$m; $NOI_1 = \$3.253125$m versus 3.6m: **−9.6%**.
*Office:* rolling 0.9m; renewals $0.9 \times 0.5 \times 0.88 = 0.396$m; re-lets $0.9 \times 0.5 \times 0.88 \times 3/12 = 0.099$m. $R_1 = \$8.595$m; $NOI_1 = \$4.995$m versus 5.4m: **−7.5%**.
*Industrial:* rolling 0.625m; renewals $0.625 \times 0.7 \times 0.96 = 0.42$m; re-lets $0.625 \times 0.3 \times 0.96 \times 8/12 = 0.12$m. $R_1 = \$4.915$m; $NOI_1 = \$4.165$m versus 4.25m: **−2.0%**.

(b) Portfolio NOI: \$17.630m → \$15.386m, **−12.7%**. The hotel accounts for $1.407/2.244 = 62.7\%$ of the decline while contributing 24.8% of starting NOI.

(c) DSCR before $= 4.38/2.90 = 1.51$x; after $= 2.973/2.90 = 1.025$x. Covenant NOI $= 1.20 \times 2.9 = \$3.48$m, so the covenant is breached and cash management is triggered. The hotel's NOI can fall only $1 - 3.48/4.38 = 20.5\%$ before the trigger.

(d) **Rubric (10 points).**
* (3) Recognizes that the hotel drives most of the *first-year* decline and the covenant breach, so "office is the problem" is wrong on a one-year view.
* (3) Recognizes that the office's −7.5% is a down payment: once all leases roll at −12%, office NOI falls by about 20% ($9.0 \times 0.88 - 3.6 = 4.32$ versus 5.4), and leasing costs come on top. Over three to five years the office may be the larger value problem.
* (2) Separates *timing of sale* from *sector view*. Selling the office in a recession crystallizes a loss at the worst bid. Selling the hotel near the trough does the same. The relevant comparison is each asset's price versus the hold value under the scenario, plus the liquidity needed to cure the hotel covenant.
* (2) Proposes a liquidity plan: reserves for the hotel's cash-sweep period, an early lender conversation, and a decision rule tied to observable data (RevPAR, office renewal notices).
No single answer is correct. Full credit requires the timing argument and the covenant arithmetic.

### Solution 4.9
(a) Net tightening $= (9 + 25 - 2 - 0)/68 = 47.1\%$.

(b) Original value $= 3.0/0.065 = \$46{,}153{,}846$. LTV test: $0.65 \times 46.15 = \$30.0$m. DSCR test: $3.0/1.25/0.07195 = \$33.36$m. Debt-yield test: $3.0/0.09 = \$33.33$m. **Binding: LTV at \$30.0m.** The existing \$32.0m loan equals 69.3% of this value, so the original lender either used a higher appraised value, a higher LTV, or a pro forma NOI. That is itself information: the loan was aggressive at origination, which is typical of late-cycle lending and is what the SLOOS tightening is correcting.

(c) $NOI_1 = 3.0 \times 0.92 = \$2.76$m; $V_1 = 2.76/0.085 = \$32{,}470{,}588$.
LTV test: $0.60 \times V_1 = \$19{,}482{,}353$. DSCR test (constant 0.08186 at 7.25%): $2.76/1.35/0.08186 = \$24{,}974{,}537$. Debt yield: $2.76/0.10 = \$27{,}600{,}000$. **Binding: LTV, \$19.48m.**
Existing loan-to-new-value $= 32.0/32.47 = 98.6\%$. Refinancing gap $= 32.0 - 19.48 = \$12{,}517{,}647$.

(d) **Options:** (1) pay down \$12.5m of new equity; (2) negotiate an extension with a partial paydown, cash sweep and rate hedge; (3) sell, with net proceeds after costs probably below the loan balance; (4) deed-in-lieu or consensual foreclosure if the loan is non-recourse; (5) a discounted payoff if the lender prefers resolution; (6) rescue capital (preferred equity or mezzanine) at a high coupon.
**Information needed:** recourse and guarantees; the lender's position (bank versus CMBS special servicer; reserves already taken); the rent roll and renewal probabilities; the sponsor's other liquidity calls; the replacement-cost and land-value floor.
**Rubric (10 points).** (3) Computes the gap correctly and notes that the equity required is about 39% of the building's new value, so new equity buys an asset at 60% LTV with a cost basis above market. (3) Compares the expected value of putting \$12.5m in against handing back the keys, given non-recourse status. Paying down is rational only if the expected value of the equity after paydown exceeds \$12.5m. (2) Uses the SLOOS reading to argue that waiting will not help, and opens extension talks early. (2) States what would change the answer: a recourse guarantee, a strong renewal pipeline, or a buyer at a value above the loan. Abstaining from new equity, by negotiating a handback or a discounted payoff, can be the best answer for a non-recourse loan on an asset with weak prospects.

### Solution 4.10
(a) **Supporting recession:** final sales to private domestic purchasers at 0.6% (weak underlying demand); GDI −0.5% against GDP +1.5% (the income side is weaker); household employment −250,000; unemployment +0.2 with a Sahm reading of 0.40; the re-steepening after a long inversion (un-inversion has often come shortly before recessions, as the market prices cuts in response to weakness [FACT for the historical tendency per J.P. Morgan; interpretation INFERENCE]); market RevPAR −3% and group pace −8%.
**Supporting expansion:** headline GDP +2.8%; payrolls beat consensus; SLOOS tightening has narrowed from 40% to 12%.
**Ambiguous:** RGI flat at 104 (the hotel holds share in a weakening market; good for relative value, silent on the level); the inventory contribution (an inventory build can mean confidence or unsold goods).

(b) Illustrative computation (any coherent set of stated ratios is acceptable). Prior 15%. Likelihood ratios [HYPOTHESIS]: GDI/GDP divergence 1.5; household-survey weakness 1.3; Sahm 0.40 (elevated zone) 2.0; re-steepening after inversion 2.0; SLOOS easing 0.8; group pace −8% 1.5. Product = 9.36. Treating them as independent: posterior odds $= 0.1765 \times 9.36 = 1.652$, probability **62.3%**. These signals overlap heavily (most of them measure the same labor-income weakness), so independence overstates the evidence. Applying a square-root discount to the combined ratio ($\sqrt{9.36} = 3.06$) gives **35.1%**. A defensible answer is a range of roughly 35–60%, well above the 15% prior.

(c) The most valuable missing information is **property-level**: two to three years of P&Ls, to test trailing NOI against the market slowdown and to normalize it, and the property-condition report or PIP exposure (Chapter 1, Example 1.2). These cost days and a few tens of thousands of dollars. Group-pace detail by segment (corporate versus association versus SMERF) would show how much of next year's −8% is already contracted. No macro release in the next week will move the recession probability as much as these items move the NOI distribution.

(d) **Rubric (20 points).**
* (4) Recession probability derived from a stated prior and likelihood ratios, with dependence discussed.
* (4) Trough NOI computed with operating leverage (§4.8); the bid price tested at the trough, not at the trailing NOI. A 7.6% cap on trailing NOI is a much lower yield on trough NOI.
* (3) Recognizes the headline GDP and payroll beats as weak evidence relative to final sales, GDI, the household survey and the Sahm reading.
* (3) Identifies the information gap (one year of P&Ls, no PCR) as a reason to refuse a firm bid in a week, citing the adverse-selection logic of Chapter 1.
* (3) A decision with a rule: for example, "abstain unless the seller grants a 30-day diligence period and three years of P&Ls; if granted, bid at a price that yields at least X% on trough NOI at 50–55% leverage."
* (3) Names the data that would change the view (two consecutive months of positive household employment and stable claims; group pace recovery; a Sahm reading back below 0.30).
**Abstention**, or a conditional bid that the seller is likely to reject, is the expected best answer. A firm bid at the asking price on these facts earns at most 8 of 20 points, however well argued.

---

## Decision exercise (§4.10) — rubric and reference computation

Reference computation [HYPOTHESIS; the case does not give revenue, so assume a 30% NOI margin and the cost structure of Example 4.8]:
* Revenue $= 2.43/0.30 = \$8.10$m; variable ratio 0.34; fixed costs $= 8.10 \times 0.66 - 2.43 = \$2.916$m.
* Recession: revenue −15% → $NOI = 6.885 \times 0.66 - 2.916 = \$1.628$m, **−33.0%** ($DOL = 2.20$).
* Loan $= 0.65 \times 29.5 = \$19.175$m. Assume the cap strike plus spread gives an all-in rate of 7.75% interest-only (SOFR strike 4.50% + 3.25%) [HYPOTHESIS]. Debt service = \$1,486,063.
* DSCR: 1.64x on trailing NOI, **1.10x** on recession NOI. Debt yield: 12.7% trailing, **8.5%** at the trough.
* The sponsor's 4% RevPAR growth for two years implies Year-2 revenue 8.16% above trailing. With trailing market RevPAR at −1.5%, that requires a turn the dashboard does not show.
* Recession probability: prior 15%; curve LR 9 (Example 4.6) and an assumed LR of 2 for the 0.37 Sahm reading give 76.1% if independent. With the curve's false-positive rate at 20% (LR 4.5), the result is 61.4%. Discounting for dependence lowers both.

**Rubric (20 points).**
* (4) Recession probability built from a base rate, with stated likelihood ratios and dependence addressed.
* (4) Trough NOI, DSCR and debt yield computed with operating leverage; the deal tested at the cap strike.
* (3) The payroll figure read net of revisions (effective surprise −125,000 against consensus).
* (3) Equity reserved for the office refinancing gap of about \$3.3m (Example 4.4) before sizing the hotel.
* (3) A decision with a maximum price or a conditional structure (lower leverage, longer or lower-strike cap, a price based on trough NOI), or abstention.
* (3) Invalidation and update criteria tied to named releases over the next 90 days.
There is no single correct bid. Abstention scores full marks if items 1–4 support it.
