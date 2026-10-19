# Chapter 20 Solutions

Numerical results are verified in `tests/test_ch20_examples.py`. Figures are rounded for display only. Money is in \$ millions unless stated.

---

### Solution 20.1
(a) Every forecast equals $\bar o$, so each bin's observed frequency equals its forecast: $REL = 0$. All forecasts sit in one bin whose frequency is $\bar o$: $RES = 0$. Hence $BS = UNC = 0.45 \times 0.55 = 0.2475$ and $BSS = 0$. The forecaster is calibrated, because when it says 45% the event happens 45% of the time, but it has no resolution. Calibration is necessary for a useful forecaster, not sufficient.

(b) EVSI compares the best expected value after seeing the signal with the best before it. If the optimal action is the same after every possible result, then $\sum_e P(e)\max_a E[x\mid e] = \max_a \sum_e P(e)E[x_a\mid e] = \max_a E[x_a]$, and the difference is zero. Information has decision value only through the actions it changes.

(c) Any one of: the fourth moment is dominated by the one or two largest observations, so the estimate is unstable; for tail indices at or below 4 the population kurtosis does not exist, so the sample value estimates nothing; ten years may contain no tail event at all, giving a low kurtosis precisely when the tail is unobserved; kurtosis also responds to the peak, not only to the tails.

(d) When the probabilities are elicited guesses whose plausible range straddles the break-even point, and when one action has a much smaller worst-case regret (Example 20.11). Caution: minimax regret is not invariant to the action set. Adding an irrelevant alternative can change the column maxima and so change the choice.

### Solution 20.2
Prior odds $= 1:9$. Likelihood ratio $= 0.90/0.10 = 9$. Posterior odds $= 1:1$, so $P = 50\%$.
Check: $P = 0.09/(0.09 + 0.09) = 0.50$. A 90%-accurate survey on a 10% base rate leaves you at a coin flip. A second, *independent* inspection (Chapter 3) is worth considering before the roof is priced at full replacement.

### Solution 20.3
(a) $z = 15/5 = 3$. $\Phi(-3) = 0.00135$. Expected count $= 360 \times 0.00135 = 0.49$, so a 30-year history would more likely than not contain none.
(b) $360 \times 0.006618 = 2.38$ months. Ratio $= 0.006618/0.00135 = 4.90$. A history containing two or three such months is what a fat-tailed model expects, and is not evidence that "something unprecedented" happened.

### Solution 20.4
(a) Sum $= 0.51$, mean $= 6.375\%$. Sample s.d. $= 15.052\%$. Standard error $= 15.052/\sqrt8 = 5.322\%$. Half-width $= 2.365 \times 5.322 = 12.58\%$. Interval $[-6.21\%,\ 18.96\%]$.
(b) Geometric mean $= (\prod(1+r_t))^{1/8} - 1 = 5.36\%$.
(c) $n_{eff} = 8(0.7)/(1.3) = 4.31$. Standard error $= 15.052/\sqrt{4.31} = 7.25\%$. Half-width $= 1.96 \times 7.25 = 14.21\%$.
(d) $n = (1.96 \times 15.052/2)^2 = 217.6$, about 218 years.
(e) The record is consistent with any mean from about −6% to +19%. It does not "prove" 6%. The −22% year alone contributes −2.75 points to the mean ($-22/8$); without it the mean of the other seven years is 10.43%. The geometric mean (5.36%), not the arithmetic mean, is the realized compound return. Any claim of skill requires deal-level evidence with more observations.

### Solution 20.5
(a) Expanded lists: 40 forecasts, 20 renewals. `brier_score` $= 0.160$.
REL $= \frac1{40}[10(0.2-0.1)^2 + 10(0.4-0.3)^2 + 10(0.6-0.7)^2 + 10(0.8-0.9)^2] = 0.4/40 = 0.010$.
RES $= \frac1{40}[10(0.1-0.5)^2 + 10(0.3-0.5)^2 + 10(0.7-0.5)^2 + 10(0.9-0.5)^2] = 4.0/40 = 0.100$.
UNC $= 0.5 \times 0.5 = 0.250$. Check: $0.010 - 0.100 + 0.250 = 0.160$. ✓ $BSS = 1 - 0.16/0.25 = 36\%$.
(b) **Underconfident.** Outcomes are more extreme than the forecasts: 10% at a stated 20% and 90% at a stated 80%. This is less common than overconfidence and suggests the team shades toward 50% to avoid being wrong.
(c) With 0.1, 0.3, 0.7, 0.9, REL $= 0$ and $BS = 0 - 0.10 + 0.25 = 0.150$ ($BSS = 40\%$). Resolution is unchanged, because the grouping is the same.
(d) $BS = 0.25$, the uncertainty term. Skill zero.

### Solution 20.6
(a) $L_1 = \phi(6.25; 5.75, 0.40) = 0.4566$; $L_2 = \phi(6.25; 6.50, 0.50) = 0.7041$. Bayes factor $= 0.6485$. $w_1 = 0.3934$, $w_2 = 0.6066$.
(b) Mean $= 0.3934(5.75) + 0.6066(6.50) = 6.205\%$. Within $= 0.3934(0.16) + 0.6066(0.25) = 0.2146$. Between $= 0.1342$. Variance $= 0.3488$, s.d. $= 0.591\%$.
(c) $M_1$: $1 - \Phi((6.75-5.75)/0.40) = 1-\Phi(2.5) = 0.62\%$. $M_2$: $1 - \Phi(0.5) = 30.85\%$. BMA mixture: $0.3934(0.0062) + 0.6066(0.3085) = 18.96\%$.
(d) Value at 5.75%: $3.0/0.0575 = 52.17$. At 6.50%: $46.15$. At the BMA mean cap 6.205%: $48.35$. Weighted average of model values: $0.3934(52.17) + 0.6066(46.15) = 48.52$. The weighted average of values exceeds the value at the average cap because $V = NOI/c$ is convex in $c$ (Jensen's inequality). Averaging cap rates and then capitalizing understates expected value slightly. The more important point is (c): the refinancing-failure probability under BMA is 19%, not the 0.6% of the model that a reversion-minded analyst would pick.

### Solution 20.7
(a) $EV(\text{commit}) = 0.6(1.5) + 0.4(-1.8) = 0.90 - 0.72 = 0.18 > 0$: commit. $EVPI = 0.6(1.5) - 0.18 = 0.72$.
(b) $P(\text{fav}) = 0.8(0.6) + 0.3(0.4) = 0.60$. $P(\text{fast}\mid\text{fav}) = 0.48/0.60 = 0.80$; $EV = 0.8(1.5) - 0.2(1.8) = 0.84$: commit.
$P(\text{unfav}) = 0.40$. $P(\text{fast}\mid\text{unfav}) = 0.12/0.40 = 0.30$; $EV = 0.3(1.5) - 0.7(1.8) = -0.81$: pass.
EV with study $= 0.60(0.84) + 0.40(0) = 0.504$. $EVSI = 0.504 - 0.18 = 0.324$. Net gain $= 0.324 - 0.075 = 0.249$. Buy the study.
(c) $P(\text{fav}) = 0.48 + 0.28 = 0.76$; $P(\text{fast}\mid\text{fav}) = 0.6316$; $EV = 0.284$: commit. $P(\text{unfav}) = 0.24$; $P(\text{fast}\mid\text{unfav}) = 0.50$; $EV = -0.15$: pass. EV with study $= 0.76(0.284) = 0.216$. $EVSI = 0.036$, less than \$75,000. Do not pay for it. Even free, it is worth only \$36,000.
(d) Value depends on the likelihood ratio, not on sensitivity alone. The independent study's "favorable" has $LR = 0.8/0.3 = 2.67$ and its "unfavorable" has $LR = 0.2/0.7 = 0.29$. The sponsor's consultant says "favorable" to almost everything ($LR = 0.8/0.7 = 1.14$), so a favorable report barely moves the posterior. A study that cannot say no is worth little.

### Solution 20.8
(a) Bills on the rest: $9.0 \times 1.10 = 9.9$. $W = \{9.9 + 5.4,\ 9.9 + 3.3,\ 9.9 + 0.6\} = \{15.3, 13.2, 10.5\}$. $E[W] = 0.45(15.3) + 0.35(13.2) + 0.20(10.5) = 13.605$. Riskless: $12.0 \times 1.10 = 13.2$.
(b) $\gamma = 2$: $W_{CE} = [0.45/15.3 + 0.35/13.2 + 0.20/10.5]^{-1} = 13.338$. Above 13.2: accept. $\gamma = 4$: $W_{CE} = [\sum p_s W_s^{-3}]^{-1/3} = 13.044$. Below 13.2: reject.
(c) $\gamma = 2$: optimal \$2.25 million; break-even \$4.36 million. $\gamma = 4$: optimal \$1.14 million; break-even \$2.24 million. At $\gamma = 2$, \$3.0 million is acceptable but larger than optimal.
(d) A positive expected excess return justifies *some* commitment for any finite risk aversion. It does not justify *any* size. The CE falls as the bet grows relative to wealth, and the 20% state that returns 0.2× is what limits size. "As much as possible" is the risk-neutral answer, which no investor with concentrated wealth should hold. See also Chapter 1, Example 1.5.

### Solution 20.9
(a) $P(A\cap B) = P(A)P(B\mid A) = 0.25 \times 0.80 = 0.20 \neq 0.15$.
(b) Buy a \$1 claim on $A\cap B$ at 0.15. Sell the analyst a conditional claim on $B$ given $A$ at 0.80; its payoff to you is $1_A(0.80 - 1_B)$. Sell 0.80 units of a claim on $A$ at 0.25 each, receiving 0.20 and owing $0.80 \cdot 1_A$. Net payoff: $1_{A\cap B} + 0.80 \cdot 1_A - 1_{A\cap B} - 0.80 \cdot 1_A = 0$ in every state. Net premium: $-0.15 + 0.20 = +0.05$. Sure profit \$0.05 per \$1.
(c) Joint: $A\cap B = 0.20$; $A\cap\neg B = 0.05$; $\neg A\cap B = 0.40 - 0.20 = 0.20$; $\neg A\cap\neg B = 0.55$. $P(B\mid\neg A) = 0.20/0.75 = 0.267$.
(d) $EV(H) = 0.20(-4.0) + 0.05(-1.5) + 0.20(-2.0) + 0.55(2.5) = -0.800 - 0.075 - 0.400 + 1.375 = 0.100$. $EV(X) = -0.200 - 0.025 - 0.100 + 0.660 = 0.335$. $EV(S) = 0$.
Column maxima: 0, 0, 0, 2.5. Regrets: $H$: (4.0, 1.5, 2.0, 0.0), max 4.0. $X$: (1.0, 0.5, 0.5, 1.3), max 1.3. $S$: (0, 0, 0, 2.5), max 2.5. Minimax regret: $X$.
(e) $X$ is best on expected value and on minimax regret, so the recommendation does not depend on the disputed joint probability. It would change if early extension became unavailable or much costlier (the payoffs in $X$), or if the anchor signed a renewal (which lowers $P(A)$ sharply and makes $H$ competitive). Note that with the analyst's incoherent 0.15 the joint table cannot be built at all; fixing the elicitation was a prerequisite.

### Solution 20.10 — Rubric (Level 5; abstention is the best current answer)

Reference numbers (verified in tests):

| Missing-project overrun | Full-record mean | Regressive estimate ($r = 0.3$) | Expected cost | Expected profit |
|---|---|---|---|---|
| Sponsor's view | 2.0% | 2.0% | 51.00 | 5.00 |
| 15% | 7.2% | 5.64% | 52.82 | 3.18 |
| 25% | 11.2% | 8.44% | 54.22 | 1.78 |

Computation for 25%: $(6 \times 2 + 4 \times 25)/10 = 11.2\%$; $11.2 + 0.3(2.0 - 11.2) = 8.44\%$; cost $= 50 \times 1.0844 = 54.22$; profit $= 56.0 - 54.22 = 1.78$.

(c) A CE needs a distribution of LP outcomes: the probability of loss and its size, including the zero-equity state that the four missing projects suggest exists. The sponsor's record contains no failures by construction, so it cannot supply one. Any CE computed from the six shown projects is a CE of a censored distribution.

(d) The highest-value information is the four missing project files: budgets, final costs, and what LPs recovered. It bears directly on the overrun distribution *and* on the sponsor's honesty, and the refusal to provide it is itself evidence. In likelihood terms, a sponsor whose legacy projects were benign would usually share them. Secondary items: a GMP contract and a completion guarantee, which change the payoffs rather than the probabilities.

(e) Strong answers abstain *for now* and state the condition for re-engaging: the full record, or a structure (GMP plus a completion guarantee plus a preferred return) that makes the missing information less decision-relevant. A conditional commitment must name the conditions and a maximum size consistent with Example 20.9 (about a tenth of liquid wealth or less at $\gamma = 3$ with a material zero state).

| Element | Full credit (4) | Partial (2) | None (0) |
|---|---|---|---|
| Selection correction | Both cases computed; assumption stated | One case or qualitative | Six projects used as presented |
| Regressive adjustment | Applied with $r$ stated | Outside view only | Sponsor's 2% used |
| Sizing / CE | Explains why CE cannot be computed from a censored record; sizes conservatively if committing | Mentions concentration | \$4.0m because EV is positive |
| Information | Missing files ranked first; refusal treated as evidence | Generic diligence list | None |
| Decision | Abstain with explicit re-engagement conditions | Conditional commit with vague conditions | Unconditional commit |

---

### Decision exercise (§20.9) — Rubric
The rubric in the chapter applies, with Solution 20.10 as the reference answer. There is no single correct number. A commitment can earn full credit only if it is conditional on the missing records or on a structure that shifts cost risk to the sponsor or contractor, and is sized by a stated risk-aversion argument.
