# Chapter 6 Solutions

Numerical results are verified in `tests/test_ch06_examples.py`. Figures are rounded for display only. Library: `sdesk.fixed_income` (`fi`), `sdesk.x_rates` (`xr`), `sdesk.tvm`, `sdesk.cre`.

---

### Solution 6.1
(a) Two reasons. (i) The discount rate divides the dollar discount by **face**, which is larger than the price actually invested. (ii) It annualizes over a **360-day** year, whereas BEY uses 365. Both lower the quoted figure. In Example 6.1 they cost 20 bp at a 5.00% discount rate on a 26-week bill.

(b) The 4.50% is a semiannual bond-equivalent yield, effective 4.5506%. The 6.50% mortgage compounds monthly, effective 6.6972%. The effective gap is 214.7 bp, not 200 bp. The mortgage spread is also not "over the risk-free rate" for the loan's actual life: a 10-year amortizing loan has a weighted-average life and duration well below 10 years, so the matching Treasury is shorter. Lenders quote over a benchmark by convention. The imprecision rarely changes an acquisition decision, but it matters for hedging (the hedge should match the loan's duration, not its stated term) and for comparing loan quotes that use different benchmarks.

(c) Any three of:
* **Expected growth changed** ($g$). Inflation, rent marks-to-market or supply conditions alter expected NOI growth; the spread narrows when growth expectations rise.
* **Risk premium changed** ($RP$). Credit availability, investor risk appetite, the liquidity of the property type, and obsolescence risk (for example office after 2020) all change $RP$.
* **The benchmark changed meaning** ($r_f$). A rise in the 10-year driven by real rates versus inflation expectations has different implications. In a flight to quality $r_f$ falls while $RP$ rises.
* **Measurement.** Appraisal-based cap rates lag. A measured spread can be "low" because the cap-rate index has not yet updated. That is not a term of the equation but a property of the data (Chapter 2).

(d) The term premium is the yield minus the expectations component, and the expected path of short rates is not observed. It must be supplied by a model (for example ACM or Kim–Wright, each with its own factor structure and data), by surveys, or by assumption. The estimate inherits those assumptions and is revised as data accumulate.

### Solution 6.2
(a) DV01 $= \text{face} \times \text{price}/100 \times D_{mod} \times 0.0001 = 25{,}000{,}000 \times 0.98 \times 8.2 \times 0.0001 = \$20{,}090$ per bp. Mental route: \$24.5 million of market value × 8.2 ≈ \$200 million "duration dollars"; one bp of that is about \$20,000.

(b) $35 \times \$20{,}090 = \$703{,}150$.

(c) Too high. Convexity reduces the loss. For a 10-year note with convexity near 78, the convexity term at 35 bp is about $\frac12 \times 78 \times 0.0035^2 = 0.048\%$ of market value, about \$12,000 on \$24.5 million: under 2% of the estimate. At 35 bp the duration estimate is good enough.

### Solution 6.3
Value: $V_1/V_0 = c_0/c_1 = 5.50/6.25 = 0.88$, so value changes by **−12.00%**.
Book equity: with debt unchanged at 65% of original value, equity falls by $12.00\%/0.35 =$ **−34.29%**.
Mental route: 75 bp on a 6.25% cap is $0.75/6.25 = 12\%$; at 35% equity multiply by 1/0.35 ≈ 2.86.

### Solution 6.4
(a) Price $= 100(1 - 0.048 \times 91/360) = 98.7867$.
* BEY $= (100 - 98.7867)/98.7867 \times 365/91 = 4.9264\%$.
* Money-market yield $= 1.2283\% \times 360/91 = 4.8590\%$.
* Effective annual $= (100/98.7867)^{365/91} - 1 = 5.0183\%$.

(b) Price $= 100(1 - 0.046 \times 364/360) = 95.3489$. With $t = 364/365$, equation (6.3) gives BEY $= 4.8332\%$. Simple-interest yield $= (100 - 95.3489)/95.3489 \times 365/364 = 4.8914\%$. Effective annual $= 4.8917\%$.

Ordering: discount rate (4.60%) < BEY (4.83%) < simple (4.89%) ≈ effective (4.89%). The BEY is a semiannually compounded rate, so it sits below the annually compounded effective yield: $(1 + 0.048332/2)^2 - 1 = 4.8916\%$, which matches the effective yield to within the 364-versus-365-day difference.

### Solution 6.5
(a) $n = 14$, periodic yield 2.125%, coupon 1.875 per period.
* Price $= 1.875 \times a_{\overline{14}|0.02125} + 100 \times 1.02125^{-14} = 96.9999$ (96.99989, effectively 97.00).
* $D_{mac} = 6.2065$; $D_{mod} = 6.2065/1.02125 = 6.0774$; convexity $= 42.808$.
* DV01 $= 0.058951$ per 100; on \$5 million face, **\$2,947.53** per bp.

(b)

| Shock | Duration only | + Convexity | Exact | Duration-only error | Second-order error |
|---|---|---|---|---|---|
| +200 bp | −11.7901 | −10.9596 | −11.0004 | −0.790 (overstates loss) | +0.041 |
| −200 bp | +11.7901 | +12.6206 | +12.6649 | −0.875 (understates gain) | −0.044 |

(c) HP-12C: `f CLEAR FIN`, `14 n`, `2.125 i`, `1.875 PMT`, `100 FV`, `PV` → −97.00. Excel: `=MDURATION(DATE(2026,1,15),DATE(2033,1,15),3.75%,4.25%,2,1)` → 6.0774 (any settlement date on a coupon date seven years before maturity gives the same result).

### Solution 6.6
(a) Forwards from (6.7):
* $f_{0,1} = 4.50\%$
* $f_{1,2} = 1.043^2/1.045 - 1 = 4.1004\%$
* $f_{2,3} = 1.0425^3/1.043^2 - 1 = 4.1501\%$
* $f_{3,4} = 4.0501\%$, $f_{4,5} = 4.2000\%$
* $f_{2,5} = (1.042^5/1.043^2)^{1/3} - 1 = 4.1334\%$

(b) Six-month horizon, per 100 face:

| Component | Value |
|---|---|
| Coupon $4.25 \times 0.5$ | 2.1250 |
| Financing $100 \times 4.60\% \times 0.5$ | −2.3000 |
| **Carry** | **−0.1750** |
| Roll-down: 2.5-year 4.25% note at 4.10% | 100.3530 − 100 = **+0.3530** |
| **Total** | **+0.1780** |
| Horizon DV01 | 0.023584 |
| **Breakeven yield rise** | **7.5 bp** |

(c) Negative carry means the money-market rate (4.60%) exceeds the note's coupon yield: the front of the curve is inverted relative to the note. The position earns only through roll-down and the price gain from falling yields. A 7.5 bp breakeven over six months is a thin cushion. Holding it "for the roll" alone is a bet that the curve does not move against you by 8 bp in six months. The real thesis must be a view that yields fall (Chapter 5), and it should be sized as such.

### Solution 6.7
(a) 5-year: price 99.5520, DV01 0.044679 per 100. 30-year: price 98.3816, DV01 0.159950 per 100. Short 30-year DV01 $= 0.159950/100 \times 20{,}000{,}000 = \$31{,}990$ per bp. 5-year face $= 31{,}990/0.00044679 = \$71.60$ million, a hedge ratio of 3.580.

(b) Full repricing:

| Scenario | 5y leg | 30y leg | Total |
|---|---|---|---|
| (i) 5y −25, 30y +10 (steepener) | +805,002 | +316,188 | **+1,121,189** |
| (ii) parallel +100 | −3,116,944 | +2,855,608 | **−261,337** |
| (iii) parallel −100 | +3,284,276 | −3,609,312 | **−325,036** |
| (iv) 5y +20, 30y −15 (flattener) | −636,466 | −488,388 | **−1,124,854** |

DV01 check for (i): $35 \times \$31{,}989.96 = \$1{,}119{,}648$, within 0.2% of the repriced total.

(c) Both parallel moves lose because the position is short convexity. The 30-year bond's convexity per unit of DV01 is much larger than the 5-year's, so for a large move up the short 30-year gains less than the long 5-year loses, and for a large move down the short 30-year loses more than the long 5-year gains. The cost at ±100 bp is 8–10 bp of spread-equivalent. A 5s30s steepener is a curve view combined with a short volatility position.

### Solution 6.8 — Rubric for (d) included
(a) Value $= 2{,}400{,}000/0.08 = \$30{,}000{,}000$; LTV $= 65\%$. Rate $= 4.30\% + 3.25\% = 7.55\%$; interest $= \$1{,}472{,}250$; DSCR $= 1.630$x; cash flow after debt service $= \$927{,}750$.

(b) Rate 9.55%; interest \$1,862,250; DSCR **1.289x**, below the 1.35x trigger, so cash management begins; cash flow after debt service \$537,750 (−42%).

(c) Cap rate $= 8.00\% + 0.5 \times 2.00\% = 9.00\%$. Value \$26,666,667 (−11.11%). Book equity \$10,500,000 → \$7,166,667 (−31.75%). Effective durations: property $11.11/2 = 5.56$; equity $31.75/2 = 15.87$. First order: $D_V = 0.5/0.08 = 6.25$; $D_E = 6.25/0.35 = 17.86$. The first-order values overstate because value is convex in the cap rate.

(d) With the cap the worst-case rate is $5.00\% + 3.25\% = 8.25\%$: interest \$1,608,750, DSCR **1.492x**, above the trigger.

Rubric (score 0–4 each):

| Dimension | Strong answer |
|---|---|
| Identifies the binding risk | The cash-management trigger and loss of distributions at +200 bp, not the mark-to-market |
| Prices the protection | Compares the cap premium with the expected and worst-case interest savings; needs the dealer quote, term, and the forward curve for the index |
| Considers alternatives | Lower-strike cap, shorter-term cap, a swap (gives up the benefit of falling rates), partial paydown, or interest reserve |
| Lender constraints | Checks whether the loan already requires a cap and its replacement terms at extension |
| What would change the answer | A forward curve already pricing cuts (makes the cap cheap but perhaps less needed); hotel RevPAR outlook; liquidity to fund a reserve |

A reasonable answer buys the cap if its premium is small relative to one year of the +200 bp interest increase (\$390,000), because the trigger converts a rate rise into a liquidity event. Declining the cap is defensible only with a funded reserve and a documented view on the index path.

### Solution 6.9 — Rubric for (c) included
(a) $RP = c + g - r_f$:
* $g = 2\%$: $6.00 + 2.00 - 4.40 = 3.60\%$
* $g = 3\%$: 4.60%
* $g = 4\%$: 5.60%
The spread is 160 bp in each case.

(b) $c = 4.40\% + 5.50\% - 2.50\% = 7.40\%$. Value change from 6.00%: $6.00/7.40 - 1 = -18.92\%$.

(c) The broker's sentence is internally inconsistent. If cap rates "must rise", a buyer at today's 6.00% cap rate would suffer the value loss in (b), so the argument is a reason to wait or to bid lower, not to buy now. The spread being below average says nothing until you know whether $g$ is higher than average (spread narrower for a good reason) or $RP$ is lower (spread narrower because risk is underpriced). A strong reply:

> The 160 bp spread is consistent with a 4.6% risk premium if NOI grows at 3%, and with a 3.6% premium if it grows at 2%. Whether that is cheap depends on our growth underwriting, not on the spread's history. If you believe cap rates will move toward the historical spread, the property is overpriced today by roughly 19% on your own numbers. We will bid on our growth case and a risk premium we can defend for this tenant and market, and we will test the bid against a 100 bp rise in Treasuries at pass-through between 0.25 and 1.0.

| Dimension | Strong answer |
|---|---|
| Decomposition | Uses $RP - g$; shows the spread is consistent with several RP/g pairs |
| Logic | Spots that "cap rates must rise" argues against buying at today's cap |
| Evidence | Asks for rent-growth evidence, lease marks, and transaction (not appraisal) cap rates |
| Regime awareness | Notes that the long-run average mixes inflation and credit regimes |
| Decision | Bids from its own required return; states a walk-away price |

### Solution 6.10 — Rubric (Level 5; abstention is the best answer under the stated facts)
(a) DV01 $= 30{,}000{,}000 \times 7.5 \times 0.0001 = \$22{,}500$ per bp. A short futures hedge loses when yields fall: $50 \times 22{,}500 = \$1{,}125{,}000$ loss at −50 bp (first order; futures DV01 conversion ignored).

(b) If the deal does not close (probability 60%), the hedge is a naked short-duration position. It gains or loses about \$22,500 per bp with nothing to offset it. On the partner's description, the hedge reduces risk in 40% of states and creates a pure speculation in 60% of states.

(c) Ranking under the stated facts:
1. **Do not hedge now; ask the lender for a rate lock at loan application** or a quoted spread with a lock fee. This ties the protection to the loan, so it disappears if the deal does not close. *This is the best answer here.*
2. If market exposure must be hedged before a lock is available, buy an option-like instrument (a payer swaption or a put on Treasury futures) sized to the probability-weighted exposure. The premium is the known cost of protection in the fail state.
3. A partial futures hedge (for example 40% of DV01) reduces but does not remove the speculation in the fail state.
4. A full futures hedge today is speculation in the most likely state.

| Dimension | Strong answer |
|---|---|
| Recognizes contingent exposure | The rate exposure exists only if the deal closes; a linear hedge of a contingent exposure creates risk |
| Quantifies | \$22,500 per bp; \$1.125m at 50 bp; 60% probability that the hedge is naked |
| Alternatives | Lender rate lock, swaption or options, partial hedge, waiting |
| Information that changes the answer | Signed PSA with hard deposit; clean PCA; loan commitment; a lender unwilling to lock |
| Process | Revisits the hedge when the probability of closing jumps (commitment, deposit going hard) |

---

### Decision exercise (Section 6.10) — reference answer and rubric

Reference figures (all from the chapter's examples):

| Item | Figure |
|---|---|
| Proposal 1 at 5:1 (\$100 million face), horizon DV01 | ≈ \$36,470 per bp |
| Proposal 1 carry + roll over one year | ≈ \$1.045 million; breakeven rise 28.7 bp |
| Proposal 1 loss at +100 bp (first order, horizon DV01) | ≈ \$3.65 million, 18% of the \$20 million allocation |
| Proposal 2 equity, first-order book duration | 28.6 (floating or par debt); effective 24.8 at +150 bp |
| Proposal 2 equity value DV01 (first order) | $50{,}000{,}000 \times 10 \times 0.0001 = \$50{,}000$ per bp |
| Proposal 2 refinancing gap at +150 bp | +\$1.98 million (equity required) versus −\$2.26 million cash-out at +0 |
| Proposal 3, value-matched 5-year short | \$112.8 million face |

Rubric (0–4 per dimension, as in the chapter table). Points are deducted for: presenting carry as a return without a breakeven; accepting the "long-run average spread" anchor; hedging the building's value DV01 with Treasuries without discussing $\beta$ instability and flight-to-quality correlation; and treating the three proposals as independent when all three are long-duration exposures (Proposals 1 and 2) or a hedge whose sign depends on the cause of the rate move (Proposal 3). A strong memo usually takes Proposal 2 only with lower leverage or a funded refinancing reserve, takes Proposal 1 unlevered or at modest leverage with a stated stop, and replaces Proposal 3 with a forward-starting hedge of the refinancing loan constant, sized to the balance and bought as an option if the cost is acceptable. Abstaining from Proposals 1 and 3 is fully defensible.
