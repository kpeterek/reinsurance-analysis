# Chapter 2 Solutions

Numerical results are verified in `tests/test_ch02_examples.py`. Figures are rounded for display only.

---

### Solution 2.1
(a) **Weak form:** prices reflect all information in past prices and volume, so technical rules earn no abnormal risk-adjusted return after costs. **Semi-strong:** prices reflect all public information. **Strong:** prices reflect all information, public and private. Strong implies semi-strong, and semi-strong implies weak.

(b) *Right:* information in private CRE is costly, so Grossman–Stiglitz predicts prices will be less informative than in REIT markets and that gross returns to local information will be higher. *Wrong:* in equilibrium, those returns are competed down to roughly the cost of acquiring the information. "Doing the work" earns a normal return on the work, not an excess return, unless your information or execution is better or cheaper than that of the marginal informed buyer. The statement also confuses inefficiency (prices not reflecting information) with exploitability (being able to earn from it after costs and limits to arbitrage).

(c) If the REIT market were weak-form efficient, the gap would say nothing about future REIT returns that past REIT prices did not already say. If it were semi-strong efficient, the REIT-implied 5.6% would already reflect the public appraisal data, so the gap would imply that appraisals are stale (or that the REIT claim differs from the property claim). Strong-form efficiency would add that insiders could not profit either. The gap can persist under semi-strong efficiency because (i) the claims differ (leverage, management, fees, taxes, property mix), so 5.6% and 4.3% need not measure the same thing; and (ii) the appraisal is not a price at which anyone can trade freely, so there is no arbitrage to close the gap (no short of private real estate, no convergence date).

### Solution 2.2
(a) $r_t = (-1.0 - 0.5 \times 1.0)/0.5 = -1.5/0.5 = -3.0\%$.
(b) $r_t = (-1.0 - 0.8 \times 1.0)/0.2 = -1.8/0.2 = -9.0\%$.
(c) The implied market return triples when $a$ moves from 0.5 to 0.8. The filter divides by $1 - a$, so it amplifies noise and any error in $a$, especially for high $a$. Report unsmoothed figures as a range across plausible values of $a$, and cross-check against transaction or REIT evidence.

### Solution 2.3
(a) $z = (120{,}000 - 180{,}000)/75{,}000 = -0.80$. $\Delta y = -0.80 \times 5 = -4.0$ bp. $\Delta P/P = -8.0 \times (-0.0004) = +0.32\%$.
(b) $z = (120{,}000 - 100{,}000)/75{,}000 = +0.267$. $\Delta y = +1.33$ bp. $\Delta P/P = -8.0 \times 0.000133 = -0.107\%$. Yields would *rise* slightly, because the print was better than what traders had positioned for. A headline writer comparing the print with the published consensus would see a "miss" with rising yields and call it puzzling. The move is consistent with surprise relative to positioning. Check revisions and wages before accepting this explanation; they are part of the same release.

### Solution 2.4
(a) Cumulative schedules:

| Price | $D$ | $S$ | Volume | $D - S$ |
|---|---|---|---|---|
| 25.05 | 160 | 20 | 20 | +140 |
| 25.10 | 160 | 50 | 50 | +110 |
| 25.15 | 110 | 85 | **85** | +25 |
| 25.20 | 70 | 125 | 70 | −55 |
| 25.25 | 40 | 175 | 40 | −135 |
| 25.30 | 15 | 175 | 15 | −160 |

Clearing price **\$25.15**, volume 85, unfilled buy interest 25.

(b) Demand rises by 60 at every price: 220, 220, 170, 130, 100, 75. Volumes: 20, 50, 85, **125**, 100, 75. Clearing price **\$25.20**, volume 125, imbalance $130 - 125 = +5$.

(c) $\lambda = (25.20 - 25.15)/60 = \$0.000833$ per thousand shares (about 0.20% for the 60 thousand shares). A market order announces urgency and accepts any price; the auction moved 5 cents against the index fund. An informed trader wants to buy without revealing information or paying for immediacy, so would use limit orders, or split the order across auctions and the continuous session. That trader then accepts the risk of not being filled.

### Solution 2.5
(a) Price changes: +0.20, −0.20, +0.20, 0.00, −0.20, +0.20, −0.20, 0.00, +0.20. Pairs $(\Delta p_t, \Delta p_{t-1})$ for $t = 2, \dots, 9$: eight pairs. Sample covariance $= -0.022857$. $\hat S = 2\sqrt{0.022857} = \$0.3024$, which is $0.3024/41.20 = 0.734\%$ of the midpoint.
(b) Nine price changes is a very small sample. The estimator is consistent only as the sample grows. Here the run of alternating changes is stronger than the i.i.d. model implies, and the estimate overshoots by about 50%.
(c) $\kappa = 1 - (1 - 0.03)/(1 + 0.02) = 1 - 0.950980 = 4.902\%$. Annual drag over 5 years $= 1 - (0.950980)^{1/5} = 1.000\%$.
(d) The estimator is undefined (the square root of a negative number). Positive autocorrelation means price changes are persistent: trending prices, persistent order flow, or stale quotes. The bid–ask bounce model is rejected for this sample. Do not report a spread; report that the data are inconsistent with the model.

### Solution 2.6
(a) $r_t = (r^*_t - 0.7\,r^*_{t-1})/0.3$:

| $t$ | Computation | $r_t$ |
|---|---|---|
| 1 | $(1.0 - 1.05)/0.3$ | −0.167% |
| 2 | $(0.0 - 0.70)/0.3$ | −2.333% |
| 3 | $(-1.0 - 0.0)/0.3$ | −3.333% |
| 4 | $(-1.5 + 0.70)/0.3$ | −2.667% |
| 5 | $(-1.5 + 1.05)/0.3$ | −1.500% |
| 6 | $(-1.2 + 1.05)/0.3$ | −0.500% |

(b) Appraisal: $(1.010)(1.000)(0.990)(0.985)(0.985)(0.988) - 1 = -4.15\%$. Unsmoothed: $-10.09\%$.
(c) Mean lag $= 0.7/0.3 = 2.33$ quarters. Volatility ratio $= \sqrt{0.3/1.7} = 0.420$.
(d) With $a = 0.5$: $r = +0.50\%, -1.00\%, -2.00\%, -2.00\%, -1.50\%, -0.90\%$; cumulative $-6.73\%$. The size of the decline depends heavily on $a$ (−6.7% versus −10.1%), while the *direction* and the *timing of the turn* (the market declines faster than the appraisal series, and the decline decelerates by quarter 6) hold at both values. Report the range, state that the size depends on an unobservable parameter, and cross-check against transaction cap rates or REIT-implied cap rates for the same property type.

### Solution 2.7
(a) F1: LTV-bound $= 30.0/0.40 = \$75.0$m; DSCR loan $= 4{,}000{,}000/(1.35 \times 0.0475) = \$62.38$m, so DSCR-bound price $= \$92.38$m; LTV binds: **\$75.0m**. F2: $18.5/0.25 = $ **\$74.0m**. F3: $4.0/0.055 = $ **\$72.73m**. F4: $4.0/0.0575 = $ **\$69.57m**. F5: $4.0/0.06 = $ **\$66.67m**.
F1 wins at about F2's \$74.0m. **F2, the bridge-financed buyer, is marginal.** Implied cap $= 4.0/74.0 = 5.41\%$.

(b) F1: DSCR loan $= 4{,}000{,}000/(1.35 \times 0.0725) = \$40.87$m; price $= 30.0 + 40.87 = \$70.87$m (DSCR binds). F2 exits. Ranking: F3 72.73, F1 70.87, F4 69.57, F5 66.67. F3 wins at about **\$70.87m**; F1 is marginal. Change $= 70.87/74.0 - 1 = -4.23\%$. Implied cap $= 4.0/70.87 = 5.64\%$.

(c) $B_{(1)} = 72.73 \ge 72.0$, so a trade occurs at $\max(70.87, 72.0) = $ **\$72.0m**. The seller's reserve, not the second bidder, sets the price. Implied cap $5.56\%$.

(d) F3 at 5.75% $= \$69.57$m. Now $B_{(1)} = $ F1's \$70.87m $< 72.0$: **no trade**. Transaction data record nothing; the listing is withdrawn or ages. An appraiser using the last sale (at a 5.41% cap) as a comp would leave value near \$74m, about 4–6% above where the building would clear today if the seller had to sell. Decision: if you are F4 or F5, you are not marginal and should not chase. If you are F3, your hurdle change is the market; wait for the seller's reserve to fall (loan maturity, fund life) rather than raise your bid.

### Solution 2.8
(a) Before redemptions, market value is $88N$. Paying $0.12N$ units at \$100 removes $12N$ of assets. Remaining value per unit $= (88 - 12)/0.88 = \$86.36$, against \$88 of underlying market value per unit: a transfer of $86.36/88 - 1 = -1.86\%$ from remaining investors.
(b) Redeemers receive \$100 for units worth \$88: a gain of $100/88 - 1 = 13.64\%$ relative to market value.
(c) Paid at \$85: remaining value per unit $= (88 - 0.12 \times 85)/0.88 = (88 - 10.2)/0.88 = \$88.41$. Now redeemers transfer value *to* remaining investors (\$85 for units worth \$88).
(d) **Rubric (Level 4).** A strong answer: (1) files the request, because it costs little and gives an option on being paid before NAV adjusts; (2) does not count on receiving \$100, because queues are paid over time and NAV is likely to be marked down first (the expected payout depends on the speed of write-downs relative to the queue); (3) computes the payout range: on \$25 million, \$25.0m at current NAV, \$21.25m after a 15% write-down; (4) states the use of proceeds conditionally: REITs if their implied cap rate is attractive relative to *private-market* evidence, not merely relative to the stale NAV (Example 2.7); direct assets only at prices consistent with the marginal-buyer analysis; T-bills otherwise; (5) recognizes the fiduciary or relationship cost of redeeming (the fund may treat redeemers differently in future offerings) and the possibility that the fund gates. What would change the answer: evidence that NAV has already been marked to transaction evidence; fund leverage (which magnifies the transfer); or a secondary-market bid for the units at a discount smaller than the estimated NAV overstatement.

### Solution 2.9
(a) Naive average $= (4.60 + 4.85 + 6.10 + 5.40 + 5.60)/5 = 5.31\%$. Value $= 2{,}400{,}000/0.0531 = \$45.20$m.
(b) $c_{\text{now}} = c \times I_s/90$: K1 5.213%; K2 5.335%; K3 6.439%; K4 5.520%; K5 5.631%.
(c) **Exclude K3** as evidence of market value: an REO sale by a lender is a forced sale and fails the "willing seller, not under compulsion" condition. Keep it as a lower bound on what a forced seller would get. Class B equivalents: K1 5.513%; K2 5.635%; K4 5.820%; K5 5.631%. Average $= 5.650\%$, value $= 2{,}400{,}000/0.0565 = \$42.48$m. Range from the extremes: 5.513% → \$43.53m; 5.820% → \$41.24m. Weight the recent comps (K4, K5) more heavily: they need the least time adjustment, which is the least reliable step. That points to the lower half of the range.
(d) The index is built from properties that traded. In a downturn, survivors are disproportionately those that fell least (Example 2.6(d)), so the index likely *understates* the decline. Time-adjusted older comps are therefore still too high. Bid toward the lower end of the range, or below it, and expect the seller to reject a bid of that size unless motivated. The naive \$45.2m overstates the defensible value by about 6%, or about \$2.7m. That error is larger than most negotiating concessions.

### Solution 2.10 — Rubric (Level 5; abstention or a conditional non-binding indication is the best answer)

The facts do not support a firm price within five days. A strong answer declines to commit to a firm price, gives a wide non-binding indication with explicit conditions, or passes. It does not split the difference between the appraisal and the latest comp.

Reference arithmetic (hypothetical): appraisal-implied cap $= 1.62/19.5 = 8.31\%$. At the 16-month-old comp's 7.9% cap, value $= \$20.51$m. At the REO comp's 9.6%, value $= \$16.875$m, 13.5% below the appraisal. A PIP at an illustrative \$8,000 per key would cost about \$1.06m [HYPOTHESIS]. All of these use a trailing NOI that the STR data may contradict.

| Dimension | Strong answer includes |
|---|---|
| Price sources | The appraisal is 10 months old and smoothed. The 7.9% comp is stale and of a different product. The 9.6% comp is a forced sale (a lower bound, not market value). REIT prices are a lead indicator of direction for lodging values even if the product differs; the broker's dismissal is advocacy. |
| Contradictory data | The STR comp set is down 6% while the seller reports +2%. Either the subject is gaining share (verify with STR penetration indices for the subject) or the P&L is wrong. This contradiction alone justifies declining to price until resolved. |
| Ranked unknowns | (1) True trailing and forward NOI (resolve STR versus P&L); (2) PIP scope and cost at the franchise renewal 26 months out; (3) financing: what the marginal buyer can borrow, which sets who is marginal. |
| Recommendation | Pass, or give a non-binding range (for example, \$16–18m) conditional on the STR reconciliation, the PIP letter, and a lender quote. Explicitly decline a firm price on the five-day timetable. |
| Process | States what would make a bid worthwhile: verified NOI, a PIP estimate, a seller motive that makes the reserve flexible (loan maturity, fund end). States the invalidation trigger: a confirmed NOI below \$1.5m, or a PIP above a stated amount. |

A weak answer averages the comps, uses the appraisal as a price, or bids firm to "stay in the process".

---

### Decision exercise (chapter §2.10) — Rubric

Score each dimension 0–4. A strong answer scores at least 3 on every dimension.

| Dimension | Strong answer includes |
|---|---|
| Private value range | Derived range, for example \$54.2m (comps restated to today and to Class B; Example 2.6) to \$57.1m (unlevered marginal buyer at 5.25%; Example 2.3). Notes that the selection bias in the time index argues for the lower half. |
| Market outcome | Recognizes that the seller's \$60.0m reserve exceeds every remaining buyer's reservation price, so no trade is the likely outcome at current guidance. A bid is a long-dated option on the seller's circumstances changing. |
| Redemption | Files the request at low cost; does not treat \$100 NAV as the payout; computes \$21.25m on \$25m if NAV falls 15% first; explains the transfer from remaining LPs. |
| REIT | Notes the 5.60% REIT-implied cap is 23% "cheap" relative to the 4.30% appraisal (Example 2.7) but close to private-market evidence (5.25–5.53%), so the REIT is not obviously cheap relative to value. Any REIT purchase is a speculation on rates, sentiment, or a REIT-specific discount, and must be named as such with an invalidation trigger. |
| Abstention and invalidation | States what will not be done (for example, no bid above \$57m; no REIT position sized as an "arbitrage"). States what would change the plan: a seller's loan maturity, a fund write-down, a move in the 10-year yield, a change in agency lending terms. |
