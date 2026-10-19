# Chapter 21 Solutions

Numerical results are verified in `tests/test_ch21_examples.py`. Figures are rounded for display only.

---

### Solution 21.1
(a) **False as stated.** VaR is a quantile. On the 1-in-100 day the loss can be any amount above \$2m, and ES or a stress test describes how much. The frequency claim also holds only if the model is correctly specified and the future resembles the estimation window.

(b) **False.** VaR is not subadditive for discrete or heavy-tailed losses. Two independent loans each with a 4% default probability show zero 95% VaR, but together have a 7.84% probability of a loss, so the pair's VaR is one full loan (Example 21.5). ES is subadditive.

(c) **True only if the market trades continuously through the stop.** A gap fills at the open. Example 21.11 shows a realized loss of twice the planned loss. A guaranteed cap requires an option, which has a price.

(d) **False.** Its *measured* daily volatility is zero because it has no daily price. Its economic exposure is levered hotel value. In Example 21.13 it is the largest stress loss.

(e) **False.** Half-Kelly earns $c(2-c) = 75\%$ of the maximum excess growth with 25% of the variance. Under estimation error it can earn *more* than full Kelly (Example 21.7).

### Solution 21.2
(a) Stop: risk $= 0.0075 \times 20{,}000{,}000 = \$150{,}000$; loss per contract $= 4 \times 1{,}000 = \$4{,}000$; $n = 37.5 \to 37$. Volatility: target $= 0.003 \times 20{,}000{,}000 = \$60{,}000$; dollar vol per contract $= 80 \times 1{,}000 \times 0.025 = \$2{,}000$; $n = 30$. **The volatility rule binds: 30 contracts.**

(b) Loss $= 30 \times (80 - 72) \times 1{,}000 = \$240{,}000$ (1.2% of capital). Planned stop loss on 30 contracts $= 30 \times 4{,}000 = \$120{,}000$, so the realized loss is **2.0×** the plan.

### Solution 21.3
$f^* = 0.05/0.04 = 1.25$. $G^* = 0.05^2/(2 \times 0.04) = 3.125\%$. Excess growth $= G^*c(2-c)$:

| $c$ | $c(2-c)$ | Growth |
|---|---|---|
| 0.5 | 0.75 | 2.34% |
| 1.5 | 0.75 | 2.34% |
| 2 | 0 | 0.00% |
| 3 | −3 | −9.375% |

Overbetting by 3× turns a 5% edge into a 9.4% a year compound *loss* relative to cash.

### Solution 21.4
(a) 99%: $k = \lfloor 250 \times 0.01\rfloor = 2$, so VaR is the 3rd worst: **\$1,410,000**. ES = mean of the 3 worst $= (2{,}150 + 1{,}630 + 1{,}410)/3 = $ **\$1,730,000**.
97.5%: $k = \lfloor 6.25\rfloor = 6$, so VaR is the 7th worst: **\$940,000**. ES = mean of the 7 worst $= 9{,}520/7 = $ **\$1,360,000**.

(b) Losses larger than \$1,000,000: 2,150; 1,630; 1,410; 1,220; 1,180, so **5 exceptions**. Expected $= 250 \times 0.01 = 2.5$. $P(X \ge 5)$ with $X \sim \text{Bin}(250, 0.01)$ is **10.8%**.

(c) Five exceptions against 2.5 expected is suspicious but not conclusive at conventional significance. (Under the Basel "traffic light", five exceptions in 250 days falls in the yellow zone; that classification is *verification pending* in this chapter.) The historical 99% VaR (\$1.41m) is 41% above the model's figure, and the worst loss is more than twice it. Check next: whether the exceptions cluster in time (volatility clustering), which positions drove them, and whether the model uses a window that excludes recent stress. Supplement with ES limits.

### Solution 21.5
(a) $\rho = 0.48/0.52 = 0.9231$. No target: $\rho^{15} = $ **30.1%**. Target 30: $(\rho^{15} - \rho^{30})/(1 - \rho^{30}) = $ **23.1%**.

(b) $f^* = 0.04/0.0225 = 1.778$.

| | $f$ | Log drift $m$ | Log vol $s$ | P(ever −40%) | P(−40% within 5 yrs) |
|---|---|---|---|---|---|
| Full Kelly | 1.778 | 3.556% | 26.67% | $0.6^1 = $ **60.0%** | **29.7%** |
| Half Kelly | 0.889 | 2.667% | 13.33% | $0.6^3 = $ **21.6%** | **3.76%** |

The 5-year figures use the reflection formula with $a = -\ln 0.6 = 0.5108$.

(c) The formulas measure the fall from the *starting* value. A running-peak drawdown resets its reference at every new high. Any path that rises first and then falls 40% from its high counts, even if it never goes below 60% of the start. Example 21.8's simulation shows the running-peak probability can be more than double the from-start figure.

### Solution 21.6
(a) Days $= 600{,}000/(0.25 \times 150{,}000) = $ **16**.

(b) Position \$21.0m. One-day VaR $= 2.3263 \times 0.022 \times 21{,}000{,}000 = $ **\$1,074,773**. Factor $= (17)(33)/(6 \times 16) = 5.84375$, $\sqrt{\ } = 2.4174$. Liquidation VaR $= $ **\$2,598,139**. LVaR $= 2{,}598{,}139 + 0.5 \times 0.008 \times 21{,}000{,}000 = $ **\$2,682,139**.

(c) $150{,}000 \times 0.25 \times 5 = $ **187,500 shares** (\$6.56m).

### Solution 21.7
(a) Maintenance total $= 20 \times 6{,}000 = \$120{,}000$. Trigger $= (200{,}000 - 120{,}000)/(20 \times 1{,}000) = $ **\$4.00 per barrel**. Call at trigger $= 20 \times 1{,}000 = $ **\$20,000**. After an \$8 fall: loss \$160,000, equity \$40,000, call to initial $= 140{,}000 - 40{,}000 = $ **\$100,000**.

(b) Breach decline $= 1 - 26/(0.70 \times 40) = 1 - 0.9286 = $ **7.14%**. At −20%: $V_1 = \$32$m; cure $= 26 - 0.70 \times 32 = $ **\$3.6m**.

### Solution 21.8
(a) $f^* = 0.05/0.01 = $ **5.0× gross**. Standard error of the mean $s = 0.10/\sqrt 8 = 3.54\%$, so $s^2 = 0.00125$. With $m^2/\sigma^2 = 0.25$ and $(m^2 + s^2)/\sigma^2 = 0.375$:

* $k = 1$: $E[g] = 0.25 - 0.1875 = $ **6.25%**.
* $k = 0.5$: $0.125 - 0.046875 = $ **7.81%**.
* $k^* = 0.0025/0.00375 = 0.667$ (3.33×): **8.33%**.

(b) True edge 2.5% at 5×: $g = 5 \times 0.025 - \tfrac12 \times 25 \times 0.01 = $ **0.0%**. At 2×: $2 \times 0.025 - \tfrac12 \times 4 \times 0.01 = $ **3.0%** (and 8.0% if the edge really is 5%).

(c) Recommendation: about 2× gross, and no more than 2.5×. At 5× the strategy's volatility is 50% a year, a 2% adverse day in the spread is a 10% NAV loss, and the prime broker can change margin terms in stress, so the financing limit sits well inside the 6× maximum. An eight-year backtest probably spans one rate regime, and if it was chosen from several variants, the effective estimation error is larger still.

**Rubric (10 points).** 3: computes the Kelly leverage and the estimation penalty correctly. 2: shows that a halved edge makes full Kelly worthless while 2× still earns. 2: brings in financing constraints (margin terms, borrow recall on shorts, PB discretion). 1: notes data-mining and regime risk in an eight-year backtest. 1: states a drawdown stop and a de-leveraging rule. 1: names the evidence that would justify more leverage (live track record, out-of-sample performance, stable borrow).

### Solution 21.9
(a) Treasuries: $15{,}000{,}000 \times (-8.5\,\Delta y + 0.5 \times 85\,\Delta y^2)$. Short ES notional $= 20 \times 5{,}000 \times 50 = \$5.0$m, so P&L $= -5{,}000{,}000 \times$ return. Hotel equity is capped at −\$6m.

| Position | A | B |
|---|---|---|
| Treasuries | +1,338,750 | −1,769,063 |
| Short ES | +1,500,000 | +750,000 |
| Hotel equity | −6,000,000 (value \$14m = loan) | −2,000,000 |
| Mezz loan | −2,000,000 | −500,000 |
| **Total** | **−5,161,250 (−12.9%)** | **−3,519,063 (−8.8%)** |

(b) The hotel stack (equity plus mezz on hotels) produces \$8.0m of A's losses, against \$2.8m of gains from the hedges. The equity hedge and duration hedge offset only about a third of it. The mezz loan and the equity are exposed to the *same* hotel cycle, so the book is more concentrated than its four-line capital table suggests. The single most effective change is to reduce hotel exposure: sell the mezz loan or de-lever the hotel. Adding more short ES would help in A but would add basis risk, because hotel values and ES do not fall in a fixed ratio. Note also that the Treasury leg hurts in B.

**Rubric (10 points).** 3: correct P&L including the convexity term and the sign of the short futures. 2: identifies common hotel exposure across equity and mezz. 2: proposes a change and quantifies its effect on the worst scenario. 1: notes the Treasury sign flip across regimes. 1: mentions cash demands (cure, margin) as well as P&L. 1: notes that scenario magnitudes are assumptions and tests sensitivity.

### Solution 21.10
(a) Reduction $= 1 - 62/118 = $ **47.5%**. With $X \sim \text{Bin}(60, 0.01)$, the expected number of exceptions is 0.6, and $P(X \ge 5) = $ **0.035%**. The parallel run itself rejects the new model at any conventional level.

(b) **Approve neither today.** The new model is not independently validated, it halves VaR with no change in positions, and its own back-test fails badly. Approving it during a limit breach would end the breach by measurement, not by risk reduction (§21.8). The position increase is described as a hedge, but it raises gross exposure in an illiquid market while the book is already over its limit. Require the desk to reduce risk to within the limit under the *current* model, or to obtain a documented temporary limit increase from the risk committee with stated conditions. Order an independent validation, and require at least a quarter of parallel reporting under both models.

**Rubric (10 points).** 2: computes the 47.5% reduction and the binomial back-test probability. 2: refuses to let a model change cure a breach, and states why. 2: rejects or defers the position increase, with reference to liquidity and the hedge's own risk. 2: specifies a governance process (independent validation, parallel run, sign-off outside the business line). 1: requires other limits (notional, CS01, stress) to be checked. 1: says what evidence would change the decision (a validated model, a passing back-test, a demonstrable hedge relationship with stress P&L).
