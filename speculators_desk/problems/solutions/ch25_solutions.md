# Chapter 25 Solutions

Numerical results are verified in `tests/test_ch25_examples.py`. Figures are rounded for display only. All inputs are hypothetical [HYPOTHESIS].

---

### Solution 25.1
| Item | Source type | Reliability | Bias | Widely known? | Use |
|---|---|---|---|---|---|
| (a) Payroll release | Public data release | A (subject to revision) | A | Yes, within seconds | Risk management. Any edge comes from interpretation (revisions, composition) or positioning, not possession |
| (b) Seller T-12 | Property operating statement | C | D (seller wants a higher price) | No | Informational edge, **after** normalization and audit (Example 25.1). Never use it unadjusted |
| (c) Lender verbal indication | Lender term sheet (pre-term-sheet) | C–B (verbal, not committed) | B (lenders posture to manage pipeline) | No | Informational for financing. Confirm with a second lender and ask *why* (Example 25.3) |
| (d) COT extreme | COT report | A as a count | B (coarse categories; basis-trade legs) | Yes: free, Friday release | Risk management (squeeze fuel). Not timing. Positions are three days old |
| (e) Brokerage report | Industry report | C | C (brokers benefit from activity) | Partly | Neither, unless it contains verifiable transaction data. Grade the data, not the adjectives |

The pattern: the sources that could support an edge, (b) and (c), are the least reliable and the most biased. That is why they are cheap to misuse.

### Solution 25.2
(a) Net $= 182{,}400 - 96{,}900 = +85{,}500$. Change $= 85{,}500 - 71{,}200 = +14{,}300$. As % of OI $= 85{,}500/612{,}000 = 13.97\%$.
(b) Positions as of the close of business on **Tuesday**. Released normally on **Friday at 3:30 p.m. Eastern** (CFTC; ch25-S01).
(c) Tuesday to the following Monday is **6 calendar days**.

### Solution 25.3
(a) $(0.8-1)^2 = 0.04$. (b) $(0.8-0)^2 = 0.64$. (c) $(0.5-o)^2 = 0.25$ for either outcome, so the score is **0.25**.
(d) X: $[8(0.05)^2 + 2(0.95)^2]/10 = (0.02 + 1.805)/10 = 0.1825$. Y: $[8(0.2)^2 + 2(0.8)^2]/10 = (0.32 + 1.28)/10 = 0.16$. **Y is better** (lower). The observed frequency is 0.8. X is overconfident, and the squared penalty for the two misses at 0.95 outweighs the small gains on the eight hits.

### Solution 25.4
(a) Rates: position DV01 $= -20 \times 82 = -\$1{,}640$ per +1 bp; $\Delta y = -8$, so P&L $= +\$13{,}120$.
ES: $(-1)(5{,}841 - 5{,}900)(50)(6) = +\$17{,}700$.
REIT: $1{,}500{,}000 \times (-0.004) = -\$6{,}000$.
FX: $1{,}000{,}000 \times (1.0790 - 1.0850) = -\$6{,}000$ (P&L in USD, the quote currency).
Costs: $-\$1{,}100$. **Total $= +\$17{,}720$.**

(b) REIT systematic $= 1{,}500{,}000 \times 1.2 \times (-0.01) = -\$18{,}000$; idiosyncratic $= -6{,}000 + 18{,}000 = +\$12{,}000$.

| Factor | \$ |
|---|---|
| Rates | +13,120 |
| Equity beta: ES +17,700, REIT systematic −18,000 | −300 |
| REIT idiosyncratic | +12,000 |
| FX | −6,000 |
| Costs | −1,100 |
| **Total** | **+17,720** |

(c) The ES short almost exactly offset the REIT basket's beta exposure (−\$300 net). The hedge worked as designed. The week's equity P&L came entirely from the REIT idiosyncratic term, which is the exposure the thesis intended. The rates leg made money, but it is a separate thesis and should be judged separately.

### Solution 25.5
(a) `fi.dv01(0.042, 0.042, 10)` $= 0.080974$ per \$100 face, so the note's P&L per +1 bp $= -0.080974 \times 80{,}000 = -\$6{,}478$. Futures: $+30 \times 85 = +\$2{,}550$. **Book DV01 $= -\$3{,}928$**: net long duration.
(b) $\Delta_{eq} = 4 \times 50 \times 5{,}800 + 1.2 \times 3{,}000{,}000 = 1{,}160{,}000 + 3{,}600{,}000 = \$4{,}760{,}000$.
(c) NOI $= 0.055 \times 40{,}000{,}000 = \$2{,}200{,}000$; $V_1 = 2{,}200{,}000/0.0625 = \$35{,}200{,}000$. Equity at risk $= \$4{,}800{,}000$. Equity falls from \$14.0m to \$9.2m, **−34.3%** (leverage multiplier $40/14 = 2.857$; asset change −12.0%).
(d) Rates: $40 \times (-3{,}928) = -\$157{,}116$. Equities: $-0.12 \times 4{,}760{,}000 = -\$571{,}200$. CRE: $-\$4{,}800{,}000$. **Total $= -\$5{,}528{,}316$, or −11.06% of capital.**
(e) The CRE line is 86.8% of the stress loss. The liquid book is a rounding error relative to the apartment equity. The futures short reduces duration but does nothing about cap-rate risk unless cap rates move with Treasuries one for one.

### Solution 25.6
(a) 0.8 bin: $6(0.04) + 4(0.64) = 0.24 + 2.56 = 2.80$. 0.6 bin: $6(0.16) + 4(0.36) = 0.96 + 1.44 = 2.40$. 0.2 bin: $3(0.64) + 7(0.04) = 1.92 + 0.28 = 2.20$. Sum $7.40$; $BS = 7.40/30 = \mathbf{0.2467}$.
(b) Base rate $15/30 = 0.5$; $BSS = 1 - 0.2467/0.25 = \mathbf{0.0133}$.
(c) REL $= [10(0.8-0.6)^2 + 10(0.6-0.6)^2 + 10(0.2-0.3)^2]/30 = (0.4 + 0 + 0.1)/30 = 0.01667$. RES $= [10(0.1)^2 + 10(0.1)^2 + 10(0.2)^2]/30 = 0.6/30 = 0.02$. $0.01667 - 0.02 + 0.25 = 0.24667$ ✓.
(d) The **0.8 bin is overconfident** (observed 0.6). The 0.2 bin is slightly underconfident (observed 0.3). The 0.6 bin is perfectly calibrated. Note that the 0.8 and 0.6 bins have the same observed frequency, so the forecaster cannot yet distinguish those situations. With ten forecasts per bin, none of this is conclusive.

### Solution 25.7
(a) Value per hour: A \$400; B \$7,500; C \$9,600; D \$300. Weekly: $5(400) + 3(7{,}500) + 6(9{,}600) + 10(300) = 2{,}000 + 22{,}500 + 57{,}600 + 3{,}000 = \$85{,}100$.
(b) New hours A 3, B 7, C 12, D 2: $1{,}200 + 52{,}500 + 115{,}200 + 600 = \$169{,}500$. Gain **\$84,400** per week.
(c) C $= 8(9{,}600) + 4(4{,}800) = 76{,}800 + 19{,}200 = 96{,}000$. Total $= 1{,}200 + 52{,}500 + 96{,}000 + 600 = \$150{,}300$. Gain **\$65,200**. The reallocation still wins, by less.
(d) For each decision changed, log the date, the decision, the hour or source that changed it, and the estimated value. After a month, compare realized $\pi$ by activity with the guesses. Also log decisions made *without* any of these activities, to avoid crediting an activity that coincided with a decision but did not cause it.

### Solution 25.8
(a) Prior odds $0.35/0.65 = 0.53846$. Product $1.8 \times 0.8 \times 1.6 \times 1.4 = 3.2256$. Posterior odds $1.73686$, **posterior 63.46%**.
(b) Product $1.8 \times 0.8 \times 1.6 = 2.304$. Posterior odds $1.24062$, **posterior 55.37%**.
(c) Both posteriors exceed 0.45, so the independence question does not change the answer. **Do not bid at the current price.** Choose between re-pricing, at a price for which the bid is acceptable with $P(H) \approx 0.55$–$0.63$, and passing.

**Rubric (8 points).**
| Item | Points |
|---|---|
| Correct posteriors under both dependence assumptions | 2 |
| Notes that the decision is robust to the dependence assumption, unlike Example 25.3 | 1 |
| Ranks the signals: own operating statements are the most relevant and least known; the sell-side note is widely known and biased | 2 |
| Proposes re-pricing via a downside scenario, not a midpoint | 1 |
| States what would change the answer: forward bookings or group pace in the submarket; new supply delivered or cancelled; a reason the own-hotel decline is property-specific (renovation, management change) | 2 |

Competing explanation to address: the own-hotel RevPAR decline could be a renovation displacement or a lost group contract. That would make it uninformative about the submarket and pull the posterior back toward the prior. Find out before relying on the LR of 1.8.

### Solution 25.9
(a) $EV = 0.7(2.0) + 0.3(-1.5) = 1.40 - 0.45 = +\$0.95$m. Break-even $p^*_{bad} = G/(G+L) = 2.0/3.5 = 57.14\%$.
(b) $EV = 1.40 - 0.3(1.8) = +\$0.86$m; $p^* = 2.0/3.8 = 52.63\%$. With $p_{bad} = 0.3$, the decision would not have changed. EV stays positive, with a wide margin to break-even.
(c) $(0.7 - 0)^2 = 0.49$.
(d) A model postmortem:

| Dimension | Grade (0–4) | Reason |
|---|---|---|
| Thesis | 3 | Scenarios were explicit. The bad state was reasonable in probability |
| Sizing | 2 | The severity was underestimated. Sizing should allow for losses beyond the bad scenario |
| Execution | 3 | (Depends on facts; record them) |
| Exit | 2 | Did the invalidation trigger fire before the loss passed −\$1.5m? If not, why? |

What failed was **severity, not probability**. One outcome cannot show that 0.3 was wrong. A Brier contribution of 0.49 is one draw and says little alone. But a loss beyond the worst scenario is evidence that the scenario set was too narrow. Rule to change: every decision record must include a "beyond worst case" line, at least 1.5× the bad-scenario loss, with a survival check against it. Rule to keep: written scenarios with probabilities, which are what make this postmortem possible.

### Solution 25.10
(a) Position DV01 $= 60 \times 85 = \$5{,}100$ per bp. Loss at invalidation $= 5{,}100 \times 12 = \$61{,}200$. Gap loss $= 5{,}100 \times 25 = \$127{,}500$, which **exceeds** the \$100,000 limit. Maximum size under the gap: $\lfloor 100{,}000/(85 \times 25) \rfloor = \lfloor 47.06 \rfloor = 47$ contracts.
(b) Product of LRs $= 1.2 \times 0.8 \times 1.3 = 1.248$. Posterior $= 1.248/2.248 = 55.52\%$. Break-even $p^* = L/(G+L) = 25/45 = 55.56\%$. EV per contract in bp $= 0.5552(20) - 0.4448(25) = -0.02$ bp, which is zero within any honest error.
(c) **Best answer: abstain (wait)**, or at most a token position. The trade's EV is indistinguishable from zero. The gap loss at the proposed size breaches the limit. One of the three signals (the sell-side preview) is widely known, and another (the COT) is old and argues against the trade. Ticket decision field: "No trade before CPI. Re-assess after the release, using the surprise against revised consensus and the 2-year reaction. Would trade if: the post-release surprise is ≥ +0.2 pp core and yields have not already gapped through the target; size ≤ 47 contracts under a 25 bp gap assumption."

**Rubric (10 points).**
| Item | Points |
|---|---|
| Correct invalidation loss, gap loss, and maximum size | 2 |
| Posterior and break-even computed and compared | 2 |
| Recognizes that EV ≈ 0 and that the limit breach alone disqualifies the proposed size | 2 |
| Treats the sell-side preview as widely known and the COT as stale and two-sided | 2 |
| States abstention as the decision, with conditions for a post-release trade | 2 |

---

### Decision exercise (Chapter 25, §25.14) — model answer and rubric notes

A strong answer:
1. **Bid** \$23.0m with a walk-away at \$23.1m (the 8% hurdle price, \$23,095,880). Invalidation: lender spread widening shown to be independent of CMBS distress, which lifts the posterior on widening above 0.50. Passing is equally creditable if the lender question cannot be resolved by the bid date.
2. **Hotel exposure:** \$5.19m of the \$7.19m joint-stress loss (72%). Options: a partial REIT short (state the basis risk and that it hedges only the cap-rate component); review the loan's extension tests and maturity; or do nothing and record why. Any of the three is defensible with reasons.
3. **TY into CPI:** the gap loss at 30 bp (\$102,000) exceeds the \$100,000 limit. Cut to 39 contracts (\$99,450) or record the exception with the approver.
4. **Routine change:** cut morning-note reading in favor of diligence (Example 25.1), or install the three template fixes from the error-log Pareto (Example 25.5). Either way, state the test.
5. **Forecasts:** for example, "P(seller accepts ≤ \$23.0m within 10 days) = 0.45" and "P(Lender 1 issues a committed term sheet ≥ 55% LTV by Day 25) = 0.70". Both are binary, dated, and size a position.
