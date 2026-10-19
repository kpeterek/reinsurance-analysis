# Chapter 21 — Risk Management and Position Sizing

> **Status:** Complete (v1.0), with open source-verification items flagged as in other chapters. Every chapter element is present and every number is reproduced in `tests/test_ch21_examples.py`. Problems are in `problems/questions/ch21_problems.md` and solutions in `problems/solutions/ch21_solutions.md`. Open verification items: (i) the historical-episode figures are confirmed only through search excerpts of the Senate report and secondary press (VERIFIED-SECONDARY). The \$132m/\$66m (Senate) and \$67m/\$129m (bank disclosure, as reported) VaR figures have not been reconciled against the primary documents. (ii) The Basel 97.5% expected-shortfall standard, the Basel back-testing zones cited in Solution 21.4, and the bibliographic details of Bangia et al. are PENDING. (iii) The S&P 500 futures move on 19 October 1987 is not used; the exercise uses the cash-index decline. See `references/sources_ch21.md`.

## Learning objectives

After this chapter you should be able to:

1. Size a position three ways (by stop distance, by volatility, and by a share of a risk budget), say why the three disagree, and decide which constraint binds.
2. Compute Value at Risk by the parametric, historical and Monte Carlo methods, and state the convention each uses. Compute expected shortfall, and show with a two-loan example that VaR is not subadditive while ES is.
3. Decompose portfolio VaR into component contributions, and recompute it with correlations moved to stress values, including +1.
4. Extend the Kelly analysis of Chapter 1 to a continuous asset. Compute half-Kelly's share of growth and of variance, and the expected growth lost when the drift is estimated with error. Compute the shrinkage that maximizes expected growth.
5. Compute the probability that wealth ever falls to a given fraction of its start (closed form) and within a horizon (reflection principle). Explain why running-peak drawdowns are more frequent, using a seeded simulation.
6. Compute gambler's-ruin probabilities and use `sdesk.risk.simulate_fixed_fraction` to show ruin as a function of size.
7. Measure liquidity risk: days to liquidate, liquidation-horizon VaR under even selling, and the spread-adjusted (liquidity-adjusted) VaR.
8. Compute the price move that triggers a futures margin call and the value decline that breaches a CRE loan-to-value covenant, and size the cash each requires.
9. Distinguish a stop order from a guaranteed loss limit. Compute the loss when price gaps through a stop and the cost of buying an actual limit.
10. Stress-test a book that holds both public and private assets under historical-analogue scenarios, and judge what the stress test says that VaR does not.

---

## 21.1 Opening investment problem: the Monday risk meeting

You are the risk officer for a \$60 million family-office account. Every figure in this problem and in the chapter's examples is [HYPOTHESIS] unless it carries a source. The book at Friday's close:

| Position | Exposure | Equity committed | Notes |
|---|---|---|---|
| 10-year U.S. Treasury notes | \$25.0m market value | \$25.0m | Modified duration 8.0, convexity 75 |
| E-mini S&P 500 futures (ES), long | 34 contracts at 5,000 → \$8.5m notional | \$1.0m margin (inside cash) | \$50 × index per contract |
| Select-service hotel, levered | \$30.0m value, \$21.0m non-recourse loan | \$9.0m | Loan has a 75% maximum-LTV covenant |
| Senior participation in an office loan | \$15.0m | \$15.0m | Marked to a dealer bid monthly |
| Cash and T-bills | \$11.0m (incl. \$1.0m futures margin) | \$11.0m | |
| **Net asset value** | | **\$60.0m** | |

The portfolio manager's report says the one-day 99% VaR is \$341,000, or 0.57% of NAV. The investment committee wants to know three things. Is that the right number? Is it the right question? And can the book take a new idea, a long position in a small-cap hotel REIT, without changing the answer?

The \$341,000 covers only the Treasuries and the futures, the positions with daily prices. The hotel and the loan carry \$45 million of gross exposure and \$24 million of equity, and they contribute nothing to it. The VaR also assumes the correlation between Treasuries and equities stays where it was over the estimation window. It assumes the futures can be closed at the screen price, and that a stop order caps the loss. By the end of the chapter each of these assumptions has a number attached, and Example 21.13 replaces the \$341,000 with a stress loss about thirty times larger.

---

## 21.2 Economic intuition

**Size is the decision you control.** You do not control whether a forecast is right. You control how much is lost if it is wrong. Chapter 1 showed that one positive-expected-value bet can compound wealth at one size and destroy it at another. Risk management is the discipline of choosing size so that the bad outcomes you can foresee, plus a margin for the ones you cannot, leave you able to keep playing.

**Every risk number is a summary of a distribution you estimated.** VaR, ES, volatility and correlation are statistics of a sample or of a model. They answer "how bad on an ordinary bad day, if the future resembles the window?" They do not answer "how bad can it get?" A risk number that falls sharply while the positions are unchanged usually means the model changed, not the risk. The historical episode in §21.8 turns on exactly this point.

**The loss that ends a strategy is usually the one that forces a sale.** A mark-to-market loss on an asset you can hold is painful. A loss that triggers a margin call, a covenant cure or a redemption converts a paper loss into a realized loss at the worst price. Leverage and financing terms determine *when* you are forced. Liquidity determines *at what price*. That is why position limits must look at funding and exit capacity, not only at volatility.

**Diversification is a regime-dependent claim.** Correlations estimated in calm periods understate co-movement in stress, when forced sellers sell whatever they can. A book that looks diversified in VaR can be one position in a crisis. Stress tests exist because the scenarios that matter are the ones the estimation window under-represents.

**A stop order is an instruction, not a guarantee.** It becomes a market order when the price trades through it. If the market opens beyond the stop, the fill is the open, not the stop. A guaranteed loss limit has to be bought, usually as an option, and it has a price.

---

## 21.3 Technical definitions

| Term | Definition |
|---|---|
| Risk per trade | Planned loss if the stop is hit, as a fraction of capital |
| Volatility target | Desired dollar standard deviation of a position or book over a stated horizon |
| Risk budget | Total allowed risk (e.g., VaR) allocated across sleeves or positions |
| VaR$_c$ (horizon $h$) | Loss level exceeded with probability $1-c$ over $h$; reported as a positive number |
| Expected shortfall ES$_c$ | Mean loss in the worst $1-c$ of outcomes |
| Component VaR | Position $i$'s share of portfolio VaR in the Euler allocation; the components sum to the total |
| Subadditivity | $\rho(A+B) \le \rho(A) + \rho(B)$: merging books cannot increase measured risk |
| Drawdown | Decline from a running peak: $1 - W_t/\max_{s\le t}W_s$ |
| Maximum drawdown (MDD) | Largest drawdown over a window |
| Ruin | Wealth reaching a level from which the strategy cannot continue (zero, a margin threshold, a mandate floor) |
| Kelly fraction $f^*$ | The fraction (or leverage) that maximizes the expected log growth of wealth |
| Days to liquidate | Position ÷ (participation rate × average daily volume) |
| Liquidity-adjusted VaR | VaR over the liquidation horizon plus the cost of crossing a stressed bid-ask spread |
| Herfindahl index (HHI) | $\sum s_i^2$ over shares $s_i$ of exposure or risk; $1/\text{HHI}$ = effective number of positions |
| Initial / maintenance margin | Deposit to open a futures position / level below which a margin call is issued |
| LTV covenant | Loan term requiring loan ÷ value to stay below a maximum, with paydown (cure) if breached |
| Gap | A price move between two trades (e.g., close to next open) with no trading in between |
| Stress test | Revaluation of the book under a specified scenario, without a probability attached |

---

## 21.4 Equations and derivations

### 21.4.1 Three sizing rules

Let $C$ be capital, $P$ the price, $M$ the contract multiplier and $\sigma$ the return volatility per period.

* **Stop distance.** With risk fraction $\rho$ and stop at $P_s$, units $n_{stop} = \rho C / (|P - P_s| M)$. (`risk.position_size_by_stop`.)
* **Volatility.** With a target dollar standard deviation $\tau$ per period, $n_{vol} = \tau / (P M \sigma)$. (`x_risk_mgmt.size_by_volatility`.)
* **Risk budget.** With a VaR allotment $B$ at confidence $c$, $n_{VaR} = B / (z_c \sigma P M)$. (`x_risk_mgmt.size_by_var_budget`.)

The stop rule controls the loss *if the exit works*. The volatility rule controls the typical daily swing whatever the exit. The budget rule controls the position's claim on a shared resource. They disagree because they answer different questions. The size you trade is the minimum of the three, rounded down.

### 21.4.2 Value at Risk and expected shortfall

**Parametric (normal).** For position value $V$ with horizon mean $\mu_h$ and volatility $\sigma_h$,

$$\text{VaR}_c = (z_c\sigma_h - \mu_h)V, \qquad \text{ES}_c = \left(\frac{\phi(z_c)}{1-c}\sigma_h - \mu_h\right)V.$$

At $c = 0.99$, $z = 2.3263$ and $\phi(z)/(1-c) = 2.6652$. For i.i.d. returns $\sigma_h = \sigma_1\sqrt{h}$. That square-root-of-time rule fails when returns are autocorrelated, when volatility clusters, and when the position changes during the horizon (§21.4.6).

**Historical.** Sort $n$ observed P&Ls. Following `risk.historical_var`, VaR is the loss at sorted index $k = \lfloor n(1-c)\rfloor$, which is the $(k+1)$-th worst. ES is the average of the $k+1$ worst. Other conventions use the $k$-th worst or interpolate. With 500 observations at 99% the choice is between the 5th and 6th worst loss, and it can move VaR by 10% or more. State the convention.

**Monte Carlo.** Draw risk-factor moves from a model, revalue every position in full, and read the quantile of the simulated P&L. Monte Carlo earns its cost when positions are non-linear (options, prepayable loans, levered equity with a floor). For linear positions with normal factors it only reproduces the parametric answer with sampling noise.

**Coherence.** A risk measure is *coherent* (Artzner et al., 1999) if it is monotone, translation invariant, positively homogeneous and subadditive. VaR fails subadditivity when loss distributions have discrete jumps or heavy tails: two books can each show zero VaR while the combined book shows a large VaR (Example 21.5). ES is coherent. The cost is that ES depends on the part of the distribution where data are thinnest. Bank market-risk capital rules have moved from 99% VaR toward 97.5% ES for this reason *(verification pending: Basel Committee market-risk standard, ch21-S17)*.

### 21.4.3 Portfolio VaR, components, and correlation going to one

For dollar volatilities $s_i$ (position value × return vol) and correlation matrix $\rho$,

$$\sigma_p = \sqrt{\textstyle\sum_i\sum_j s_i s_j \rho_{ij}}, \qquad \text{VaR}_p = z_c\sigma_p .$$

The Euler (component) contribution of position $i$ is $\text{CVaR}_i = z_c\,\big(\sum_j s_i s_j\rho_{ij}\big)/\sigma_p$, and the components sum to $\text{VaR}_p$. When every $\rho_{ij} = 1$, $\sigma_p = \sum_i s_i$, so portfolio VaR equals the sum of standalone VaRs. **That sum is the upper bound for a long-only book of linear positions, and it is the right planning number when the positions share a crisis driver.** When a hedge's correlation changes sign (bonds that rallied in equity sell-offs begin to fall with them), VaR can rise above the "diversified" figure even though nothing in the book changed.

### 21.4.4 Continuous Kelly, half-Kelly, and estimation error

Chapter 1 (§1.4.5, Example 1.5) derived Kelly for a two-outcome bet. For a lognormal asset with drift $\mu$, volatility $\sigma$ and risk-free rate $r$, holding fraction (leverage) $f$ continuously rebalanced gives log growth

$$g(f) = r + f(\mu - r) - \tfrac12 f^2\sigma^2 .$$

Setting $g'(f) = 0$ gives $f^* = (\mu - r)/\sigma^2$ (`risk.kelly_continuous`) and excess growth $G^* = g(f^*) - r = (\mu - r)^2/(2\sigma^2)$.

**Fractional Kelly.** Write $f = c f^*$. Then

$$g(cf^*) - r = G^*\,c\,(2 - c), \qquad \text{vol of wealth} = c f^*\sigma .$$

At $c = \tfrac12$, half-Kelly earns $\tfrac12 \cdot \tfrac32 = 75\%$ of the maximum excess growth with half the volatility and one quarter of the variance. Growth is symmetric about $c = 1$: betting $1.5f^*$ earns the same as $0.5f^*$ with three times the volatility. At $c = 2$ growth equals the risk-free rate, and beyond that it is lower.

**Estimation error.** You never know $\mu - r$. Suppose you estimate it as $\hat m \sim N(m, s^2)$, with $m = \mu - r$, and bet $f = k\hat m/\sigma^2$. Taking expectations over $\hat m$, using $E[\hat m] = m$ and $E[\hat m^2] = m^2 + s^2$:

$$E[g] - r = k\frac{m^2}{\sigma^2} - \frac{k^2}{2}\cdot\frac{m^2 + s^2}{\sigma^2}.$$

At $k = 1$ the expected penalty relative to knowing $m$ is $s^2/(2\sigma^2)$. If the drift was estimated from $T$ years of returns, $s = \sigma/\sqrt T$, and the penalty is $1/(2T)$ per year *whatever the asset*. Twenty years of data cost 2.5% a year of expected growth at full Kelly. The $k$ that maximizes expected growth is

$$k^* = \frac{m^2}{m^2 + s^2} < 1,$$

which is a formal argument for fractional Kelly. It needs $m$, which you do not know. In practice you substitute a conservative $m$, and that pushes $k$ lower still. Overbetting is worse than underbetting by the same multiple: if the true edge is half the estimate, full Kelly on the estimate is $c = 2$ on the truth, and growth falls to zero.

### 21.4.5 Probability of a drawdown of given depth

Let $\ln W_t$ be Brownian with drift $m$ and volatility $s$ (with $f$ in the asset, $m = g(f)$ and $s = f\sigma$). The probability that wealth *ever* falls to $(1-d)$ of its starting value, for $m > 0$, is the first-passage probability

$$P(\text{ever} \le (1-d)W_0) = e^{-2ma/s^2} = (1-d)^{2m/s^2}, \qquad a = -\ln(1-d).$$

For a fractional-Kelly bettor, $2m/s^2 = 2/c - 1$ (with $r = 0$), so

$$P(\text{ever lose } d) = (1-d)^{2/c - 1}.$$

At full Kelly the exponent is 1: **the probability of ever halving is 50%**. At half-Kelly the exponent is 3, so the probability is $0.5^3 = 12.5\%$. Over a finite horizon $T$ the reflection principle gives

$$P(\min_{t\le T}\ln W_t/W_0 \le -a) = \Phi\!\left(\frac{-a - mT}{s\sqrt T}\right) + e^{-2ma/s^2}\,\Phi\!\left(\frac{-a + mT}{s\sqrt T}\right).$$

Both formulas measure the fall *from the start*. A drawdown from a *running peak* is more likely, because every new high resets the reference point. Example 21.8 shows the gap by simulation.

### 21.4.6 Gambler's ruin

With unit bets winning with probability $p$, $q = 1 - p$, $\rho = q/p$, starting $k$ units from ruin and stopping at $N$:

$$P_{ruin} = \frac{\rho^k - \rho^N}{1 - \rho^N}\ (p \ne \tfrac12), \qquad P_{ruin} = 1 - \frac{k}{N}\ (p = \tfrac12), \qquad P_{ruin}^{N\to\infty} = \rho^k\ (p > \tfrac12).$$

Derivation: $P_k = pP_{k+1} + qP_{k-1}$ with $P_0 = 1$, $P_N = 0$. The characteristic roots are 1 and $\rho$. The formula shows that **halving the bet size doubles $k$ and squares the ruin probability** when there is no target.

### 21.4.7 Liquidation horizon and liquidity-adjusted VaR

If a position takes $T$ days to sell in equal daily slices, exposure during day $j$ is $(T - j + 1)/T$ of the original. The variance of the liquidation P&L is

$$\sigma_1^2\sum_{j=1}^{T}\left(\frac{T-j+1}{T}\right)^2 = \sigma_1^2\,\frac{(T+1)(2T+1)}{6T},$$

so the liquidation-horizon VaR is the one-day VaR times $\sqrt{(T+1)(2T+1)/(6T)}$, about $\sqrt{T/3}$ for large $T$. That is less than $\sqrt T$ for holding the whole position for $T$ days, and more than one day. The exogenous-spread adjustment (Bangia et al.) adds the cost of crossing half a stressed bid-ask spread:

$$\text{LVaR} = \text{VaR}_{T} + \tfrac12\,S_{stress}\,V .$$

This omits market impact, the price concession that grows with the position's share of volume. Chapter 2 treats impact; here it is a reason to treat LVaR as a floor.

### 21.4.8 Leverage, margin and covenants

Equity volatility is asset volatility times $V/E$. That is all leverage does to the distribution, until a financing term forces action.

*Futures margin.* With account equity $A$, $n$ contracts, multiplier $M$, maintenance margin $m_m$ and initial margin $m_i$ per contract, a long position receives a call when the price falls by

$$\Delta P_{call} = \frac{A - n\,m_m}{nM}.$$

The call restores equity to $n\,m_i$, so at the trigger the call is $n(m_i - m_m)$, and it grows one-for-one with further losses.

*LTV covenant.* With loan $L$, value $V$ and maximum LTV $\lambda$, the breach occurs at a value decline of

$$d_{breach} = 1 - \frac{L}{\lambda V},$$

and the cure at new value $V_1$ is $\max(0, L - \lambda V_1)$.

### 21.4.9 Gap risk

A stop at $P_s$ fills at $\min(P_s, P_{open})$ for a long position when the market opens below the stop. Realized loss / planned loss $= (P - P_{fill})/(P - P_s)$. Only an instrument with a contractual payoff, such as a put struck at $P_s$, caps the loss, and it costs the premium whether or not the gap occurs.

### 21.4.10 Transaction costs

For annual turnover $\theta$ (round trips per year, as a multiple of capital) and round-trip cost $\kappa$, the return drag is $\theta\kappa$. For a CRE hold of $T$ years with buy cost $b$ and sell cost $s$, the round trip is $1 - (1-s)/(1+b)$ (`x_microstructure.round_trip_cost`), and the geometric annual drag is $1 - (1 - \text{round trip})^{1/T}$. Costs scale with turnover; edge usually does not. A sizing or rebalancing rule that trades often must be judged net of cost.

### 21.4.11 Concentration

For shares $s_i$ of exposure, of risk or of stress loss, $\text{HHI} = \sum s_i^2$ and the effective number of positions is $1/\text{HHI}$. Measure it on *stress loss*, not on capital. A book can be spread across four positions by capital and still have one position doing most of the damage.

---

## 21.5 Worked examples

All inputs are [HYPOTHESIS] unless sourced. Every number is reproduced in `tests/test_ch21_examples.py`.

### Example 21.1 — Three sizing rules for one futures trade

**Given.** NAV \$60m. Long ES at 5,000, multiplier \$50. Stop at 4,850. Risk per trade 0.5% of NAV. Daily ES volatility 1.2%. Daily volatility target for the position 0.25% of NAV. Book one-day 99% VaR budget 1.0% of NAV, of which 40% is allotted to the equity sleeve.

**Find.** Contracts under each rule; the binding rule.

**Solution.**

*Stop.* Risk = $0.005 \times 60{,}000{,}000 = \$300{,}000$. Loss per contract at the stop $= 150 \times 50 = \$7{,}500$. $n_{stop} = 300{,}000/7{,}500 = 40$.

*Volatility.* Target $= 0.0025 \times 60{,}000{,}000 = \$150{,}000$ per day. Dollar vol per contract $= 5{,}000 \times 50 \times 0.012 = \$3{,}000$. $n_{vol} = 150{,}000/3{,}000 = 50$.

*Budget.* Allotment $= 0.01 \times 60{,}000{,}000 \times 0.40 = \$240{,}000$. VaR per contract $= 2.3263 \times 3{,}000 = \$6{,}979$. $n_{VaR} = 240{,}000/6{,}979 = 34.39 \to 34$.

| Rule | Contracts | Constrains |
|---|---|---|
| Stop distance | 40 | Loss if the stop fills at 4,850 |
| Volatility target | 50 | Typical daily swing |
| VaR budget | 34 | Claim on the book's shared risk |

**Check.** The stop distance is $150/5{,}000 = 3.0\%$, which is 2.5 daily standard deviations. The stop rule therefore implies a one-day 2.5σ risk of \$300,000 on 40 contracts. That is consistent with $40 \times 2.5 \times 3{,}000 = \$300{,}000$. ✓

**Decision consequence.** Trade 34 contracts. The VaR budget binds because the book already carries rate risk. The stop rule would allow 40, but only if the stop fills at the stop, and Example 21.11 removes that assumption. Writing all three numbers in the trade ticket makes the binding constraint, and therefore the actual reason for the size, visible to the committee.

### Example 21.2 — The 1987 desk exercise: size and VaR by hand, then in Python

The historical setting of 19 October 1987 is in Chapter 1, §1.9. Here you are the risk manager of a futures desk on Friday 16 October 1987.

**Given.** Desk capital \$10m. Long S&P 500 futures. Multiplier \$500 per index point [INFERENCE: CME states the standard contract's multiplier was 500 when the E-mini launched in 1997, and we assume it was unchanged in 1987; ch21-S08]. Entry at 280.00 [HYPOTHESIS: a round number near the level of the time; the actual Friday settlement is *(verification pending)*]. Risk per trade 1% of capital. Stop 3% below entry. Volatility assumption 15% annualized, 252 trading days [HYPOTHESIS, a trailing estimate a desk might have used]. On Monday 19 October the S&P 500 cash index fell 20.47% [FACT; ch21-S09, VERIFIED-SECONDARY].

**Find.** Contracts; one-day 99% VaR and ES; Monday's loss measured close to close, and its size in standard deviations.

**Solution by hand.**

Stop at $280.00 \times 0.97 = 271.60$. Loss per contract at the stop $= 8.40 \times 500 = \$4{,}200$. Risk budget $= \$100{,}000$. $n = 100{,}000/4{,}200 = 23.8 \to 23$ contracts.

Notional $= 23 \times 280 \times 500 = \$3{,}220{,}000$.

Daily vol $= 0.15/\sqrt{252} = 0.15/15.875 = 0.945\%$.

VaR$_{99}$ $= 2.326 \times 0.00945 \times 3{,}220{,}000 \approx \$70{,}800$ (exact: \$70,782). ES$_{99} = 2.665 \times 0.00945 \times 3{,}220{,}000 = \$81{,}092$.

Planned loss at the stop $= 23 \times 4{,}200 = \$96{,}600$.

Monday's close-to-close loss $= 0.2047 \times 3{,}220{,}000 = \$659{,}134$, which is 6.59% of capital and 6.8 times the planned loss.

Size of the move $= 20.47\%/0.945\% = 21.7$ standard deviations. Under the normal model the probability of a move that large is about $10^{-104}$.

**Solution in Python.**

```python
from sdesk import risk
n = risk.position_size_by_stop(10e6, 0.01, 280.0, 271.6, 500)      # 23.81 -> trade 23
sd = 0.15 / 252 ** 0.5                                              # 0.009449
var = risk.parametric_var(23 * 280 * 500, 0.0, sd, 0.99)            # 70,781.79
es = risk.parametric_es(23 * 280 * 500, 0.0, sd, 0.99)              # 81,092.18
```

**Check.** $23 \times 3{,}077 = 70{,}782$ with per-contract VaR $2.3263 \times 0.009449 \times 140{,}000 = \$3{,}077$. ✓

**Decision consequence.** Every number on Friday was internally consistent, and every number was beside the point on Monday. Three things failed together. The volatility estimate came from a calm window. The normal tail assigned zero probability to the actual move. The stop could not fill at 271.60 in a market that traded through it with few bids. The desk survived because 1% risk per trade put only 32% of capital in notional exposure. At 2.5× gross leverage (notional \$25m) the same day would have cost 51% of capital. Survival came from the notional cap, not from the VaR. **Set a maximum gross notional per unit of capital that does not depend on estimated volatility, because estimated volatility is lowest just before it matters most.**

### Example 21.3 — Portfolio VaR, component VaR, and correlation going to one

**Given.** The liquid sleeve of the opening book. Treasuries \$25m, modified duration 8.0, daily yield volatility 7 bp, so dollar vol $= 25{,}000{,}000 \times 8 \times 0.0007 = \$140{,}000$. ES 34 contracts, notional \$8.5m, daily vol 1.2%, so dollar vol \$102,000. P&L correlation (long bonds against long equity) −0.3 in the estimation window.

**Find.** Standalone and portfolio one-day 99% VaR at $\rho = -0.3$; the component VaRs; VaR at $\rho = 0, +0.5, +1$; the 10-day VaR by square-root-of-time.

**Solution.**

Standalone: $2.3263 \times 140{,}000 = \$325{,}689$; $2.3263 \times 102{,}000 = \$237{,}287$. Sum \$562,976.

$\sigma_p = \sqrt{140{,}000^2 + 102{,}000^2 + 2(-0.3)(140{,}000)(102{,}000)} = \sqrt{19{,}600 + 10{,}404 - 8{,}568}\times 10^3 = \$146{,}410$.

VaR$_p = 2.3263 \times 146{,}410 = \$340{,}601$. This is the \$341,000 in the PM's report.

Components: Treasuries $= 2.3263 \times (140{,}000^2 - 0.3 \times 140{,}000 \times 102{,}000)/146{,}410 = \$243{,}359$. ES $= 2.3263 \times (102{,}000^2 - 0.3 \times 140{,}000 \times 102{,}000)/146{,}410 = \$97{,}242$. They sum to \$340,601.

| ρ | σ$_p$ | 1-day VaR$_{99}$ | 10-day VaR (×√10) |
|---|---|---|---|
| −0.3 | \$146,410 | \$340,601 | \$1,077,076 |
| 0.0 | \$173,217 | \$402,962 | \$1,274,278 |
| +0.5 | \$210,438 | \$489,551 | \$1,548,097 |
| +1.0 | \$242,000 | \$562,976 | \$1,780,287 |

**Check.** At $\rho = 1$ the VaR equals the sum of standalone VaRs, \$562,976. ✓

A second illustration with three CRE-linked risk positions: a hotel REIT (\$10m, 25% annual vol), the levered hotel equity (\$9m, 30%), and a BBB− CMBS position (\$6m, 15%). With pairwise correlation 0.4 the portfolio dollar vol is \$4.85m, or 79.5% of the \$6.10m sum of standalone vols. At 0.9 it is \$5.91m (96.9%). At 1.0 it is \$6.10m. The diversification benefit of 20% exists only in a regime where hotel equity, hotel REITs and hotel-heavy CMBS do not move together. That is not the regime in which you need it.

**Decision consequence.** The \$341,000 depends on a negative stock–bond correlation. If that correlation turns positive, as it does when an inflation shock hits both assets, VaR rises 44% with no trade. Report VaR at the window correlation *and* at +1. Allocate risk budget using component VaR, which shows that Treasuries use 71% of this sleeve's VaR. If the committee wants more equity, the rate position is the one that pays for it.

### Example 21.4 — Historical VaR and ES, and what the convention changes

**Given.** 500 daily P&Ls of the liquid sleeve. The eight worst, in \$000: −620, −540, −505, −470, −455, −430, −410, −395.

**Find.** Historical one-day 99% VaR and ES under the library convention; the alternative 5th-worst VaR; comparison with the parametric figures from Example 21.3.

**Solution.** $k = \lfloor 500 \times 0.01\rfloor = 5$, so VaR is the 6th worst loss: **\$430,000**. ES = mean of the six worst $= (620 + 540 + 505 + 470 + 455 + 430)/6 = 3{,}020/6 = $ **\$503,333**. Under the 5th-worst convention VaR is \$455,000, 5.8% higher.

Parametric (ρ = −0.3): VaR \$340,601; ES $= 2.6652 \times 146{,}410 = \$390{,}215$.

| Measure | Parametric | Historical | Ratio |
|---|---|---|---|
| VaR$_{99}$ | \$340,601 | \$430,000 | 1.26 |
| ES$_{99}$ | \$390,215 | \$503,333 | 1.29 |

**Check.** The historical ES exceeds the historical VaR, and the worst observation (\$620,000) exceeds the ES. ✓

**Decision consequence.** The empirical tail is about 26–29% fatter than the normal model with the same volatility. Historical VaR is only as good as its window. A window without a stress episode understates risk, and one that includes a stress episode understates it again once that episode rolls out of the window. Use historical ES as the limit metric for the liquid book, with a stressed window (one that contains a known crisis) as a floor.

### Example 21.5 — VaR is not subadditive: two mezzanine loans

**Given.** Two \$5m mezzanine loans on unrelated hotels. Each defaults with probability 4% over the year, independently, with total loss on default. Confidence 95%.

**Find.** VaR and ES of each loan and of the pair.

**Solution.**

*Each loan.* P(loss = 5) = 0.04 < 0.05, so VaR$_{95}$ = **0**. ES: the worst 5% of outcomes contain 4% at a loss of 5 and 1% at 0, so ES $= 0.04 \times 5/0.05 = $ **\$4.0m**.

*The pair.* P(both default) = 0.0016 (loss 10). P(one default) $= 2(0.04)(0.96) = 0.0768$ (loss 5). P(no loss) = 0.9216. P(any loss) = 0.0784 > 0.05, so VaR$_{95}$ = **\$5.0m**. ES: the worst 5% contains 0.16% at 10 and 4.84% at 5, so ES $= (0.0016 \times 10 + 0.0484 \times 5)/0.05 = (0.016 + 0.242)/0.05 = $ **\$5.16m**.

| | Loan A | Loan B | A + B | Sum of standalone |
|---|---|---|---|---|
| VaR$_{95}$ | 0 | 0 | 5.00 | 0 |
| ES$_{95}$ | 4.00 | 4.00 | 5.16 | 8.00 |

**Check.** VaR(A+B) = 5 > VaR(A) + VaR(B) = 0, so VaR is not subadditive here. ES(A+B) = 5.16 ≤ 8.00. ✓

**Decision consequence.** A VaR limit invites a book of positions that each default just below the confidence level: short deep out-of-the-money options, senior tranches, mezzanine loans. Each one shows zero VaR. Diversifying such a book *raises* measured VaR, so the measure punishes diversification and rewards concentration. Credit and option-like books need ES limits, or explicit default-scenario limits, as well as VaR.

### Example 21.6 — Monte Carlo VaR for a short-put overlay

**Given.** The PM proposes selling 40 one-month ES puts struck at 4,750 (5% out of the money) to earn premium. Index 5,000; implied vol 18%; $r$ = 4%; time to expiry 21/252 years; multiplier \$50. Horizon 10 trading days. Model: 10-day log return normal with mean 0 and volatility $0.18\sqrt{10/252} = 3.586\%$. Full revaluation with Black–Scholes at the remaining 11 days. 20,000 paths, seed 21 (`x_risk_mgmt.mc_var_es`).

**Find.** Premium received; delta-normal VaR; Monte Carlo VaR and ES; Monte Carlo VaR if implied vol rises when the market falls.

**Solution.**

Put value 19.08 points, so premium $= 40 \times 50 \times 19.08 = \$38{,}161$. Put delta −0.1407, so the short position's delta is $+40 \times 50 \times 0.1407 = \$281.4$ per index point, equivalent to 5.6 long futures.

Delta-normal VaR $= 2.3263 \times 281.4 \times 5{,}000 \times 0.03586 = \$117{,}349$.

Monte Carlo (constant vol): VaR$_{99}$ = **\$292,336**, ES$_{99}$ = **\$378,887**. Full revaluation at the deterministic 99th-percentile move ($-2.3263\sigma_h$, a fall of 400 points) gives a loss of \$287,227, close to the simulated quantile.

Monte Carlo with implied vol $= \max(18\%, 18\% - 1.5x)$, where $x$ is the 10-day log return (a fall of 5% lifts vol by 7.5 points) [HYPOTHESIS: a stylized spot–vol rule]: VaR$_{99}$ = **\$372,800**, ES$_{99}$ = **\$456,374**.

**Check.** A delta-gamma approximation at the 400-point fall gives a loss of \$250,218. The difference from full revaluation (\$287,227) is the higher-order curvature. Both are far above delta-normal. ✓

**Decision consequence.** The overlay earns \$38,000 and adds about \$290,000–\$370,000 to 10-day VaR. Delta-normal VaR understates it by a factor of 2.5–3.2. The short put adds risk in exactly the states where the long futures already lose. Approve the overlay only if it replaces futures delta (sell about six contracts) *and* is charged to the risk budget at its Monte Carlo ES with vol-up dynamics. A book that reports linear VaR for non-linear positions is reporting a number that rises sharply when the model is corrected.

### Example 21.7 — Continuous Kelly, half-Kelly, and the cost of not knowing the drift

**Given.** An equity strategy with expected excess return $m = 6\%$, volatility $\sigma = 16\%$, $r = 0$ for simplicity. The 6% was estimated from 20 years of annual data.

**Find.** $f^*$ and $G^*$; growth and volatility at $c$ = 0.25, 0.5, 0.75, 1, 1.5, 2; expected growth under estimation error at full Kelly, half-Kelly and the optimal shrinkage; growth if the true edge is 3%.

**Solution.** $f^* = 0.06/0.16^2 = 2.344$ (234% gross exposure). $G^* = 0.06^2/(2 \times 0.0256) = 7.03\%$.

| $c$ | $f$ | Growth $G^*c(2-c)$ | Share of $G^*$ | Wealth vol |
|---|---|---|---|---|
| 0.25 | 0.586 | 3.08% | 43.75% | 9.4% |
| 0.50 | 1.172 | 5.27% | 75.0% | 18.75% |
| 0.75 | 1.758 | 6.59% | 93.75% | 28.1% |
| 1.00 | 2.344 | 7.03% | 100% | 37.5% |
| 1.50 | 3.516 | 5.27% | 75.0% | 56.25% |
| 2.00 | 4.688 | 0.00% | 0% | 75.0% |

*Estimation error.* $s = 0.16/\sqrt{20} = 3.58\%$, $s^2 = 0.00128$. Penalty at $k = 1$: $s^2/(2\sigma^2) = 1/(2 \times 20) = 2.50\%$.

* $k = 1$: $E[g] = 0.1406 - \tfrac12(0.0036 + 0.00128)/0.0256 = 0.1406 - 0.0953 = 4.53\%$.
* $k = 0.5$: $E[g] = 0.0703 - 0.125 \times 0.1906 = 4.65\%$.
* $k^* = 0.0036/(0.0036 + 0.00128) = 0.738$: $E[g] = 5.19\%$.

If the true edge is 3% while you bet $f = 2.344$ on the 6% estimate: $g = 2.344 \times 0.03 - \tfrac12 \times 2.344^2 \times 0.0256 = 0.0703 - 0.0703 = 0$.

**Check.** Half-Kelly and 1.5× Kelly have equal growth (5.27%) because $c(2-c)$ is symmetric about 1. ✓

**Decision consequence.** Under estimation error, half-Kelly *out-earns* full Kelly in expectation (4.65% versus 4.53%), with half the volatility. This is the result Chapter 1 promised. Full Kelly is the right size only if you know the edge, and you never do. If the edge was found by searching many backtests, the effective $s$ is larger than $\sigma/\sqrt T$ (Chapter 20). Treat 0.25–0.5 Kelly as a ceiling, not a target. Then apply the financing and liquidity constraints of Examples 21.9–21.10, which usually bind first.

### Example 21.8 — Drawdown and ruin: closed forms and seeded simulations

**Given.** (a) The Example 21.7 asset at full, two-thirds and half Kelly. (b) A trader with $k$ units of capital making unit bets that win with probability 0.53. (c) Chapter 1's repeated bet (+60% or −50%, each with probability ½, $f^* = 1/6$), simulated for 100 periods with `risk.simulate_fixed_fraction`, 4,000 paths, seed 7, with ruin defined as touching 50% of starting wealth.

**Find.** Probabilities of ever losing 50% and 30%, and of losing 50% within 10 years; simulated running-peak drawdowns; gambler's-ruin probabilities; simulated ruin by fraction.

**Solution (a).** Log drift and vol: full Kelly $m = 7.03\%$, $s = 37.5\%$; half Kelly $m = 5.27\%$, $s = 18.75\%$.

| Size | $2m/s^2$ | P(ever −50%) | P(ever −30%) | P(−50% within 10 yrs, from start) | Simulated P(MDD ≥ 50% in 10 yrs, from running peak) | Simulated median MDD |
|---|---|---|---|---|---|---|
| Full Kelly | 1 | 50.0% | 70.0% | 37.1% | 86.9% | 65.3% |
| ⅔ Kelly | 2 | 25.0% | 49.0% | 16.4% | — | — |
| Half Kelly | 3 | 12.5% | 34.3% | 6.9% | 18.7% | 38.4% |

The simulation uses weekly steps, 4,000 paths and seed 21 (`x_risk_mgmt.simulate_max_drawdowns`). Weekly monitoring slightly understates continuous-time drawdowns.

**Solution (b).** $\rho = 0.47/0.53 = 0.8868$. No target: $k = 10$ gives $\rho^{10} = 30.1\%$; $k = 20$ gives $\rho^{20} = 9.05\%$. With a target of doubling: $k = 10, N = 20$ gives 23.1%; $k = 20, N = 40$ gives 8.30%. A fair game ($p = 0.5$, $k = 20$, $N = 40$) gives 50%.

**Solution (c).**

| Fraction | Growth $g$ per period | Median terminal wealth | P(touched 50%) |
|---|---|---|---|
| 1/6 ($f^*$) | +0.415% | 1.514 | 27.1% |
| 1/3 ($2f^*$) | 0.000% | 1.000 | 68.0% |
| 1/2 | −1.266% | 0.282 | 85.3% |
| 1 | −11.16% | 0.00001 | 99.65% |

**Check.** The simulated median at $f^*$, 1.514, equals $e^{100 \times 0.004149} = 1.514$. In the gambler's-ruin case, halving the bet from 1/10 to 1/20 of capital doubles $k$ and squares the ruin probability, since $0.301^2 = 0.0905$. ✓

**Decision consequence.** At full Kelly a 50% fall from the start is a coin flip, and a 50% fall from *some* peak within ten years is close to certain (87%). Few mandates, and no lender, survive that. Half Kelly cuts the running-peak probability to about 19% while keeping 75% of the growth. Ruin is governed by size relative to capital, and doubling size does far more than double the danger. Write the drawdown at which the strategy will be stopped *before* sizing it, and size so that reaching that level is a tail event under conservative parameters.

### Example 21.9 — Liquidity: days to liquidate and liquidity-adjusted VaR

**Given.** The proposed hotel REIT position: 1,000,000 shares at \$20 (\$20m). Average daily volume 250,000 shares. Maximum participation 20%. Daily vol 2.0%. Normal bid-ask spread 0.20%; stressed spread 1.0%.

**Find.** Days to liquidate; one-day 99% VaR; liquidation-horizon VaR (even selling) versus holding for the full period; LVaR with the stressed spread; the comparison for a 200,000-share position.

**Solution.** Days $= 1{,}000{,}000/(0.20 \times 250{,}000) = 20$ (`x_dynamics.days_to_exit`).

One-day VaR $= 2.3263 \times 0.02 \times 20{,}000{,}000 = \$930{,}539$.

Liquidation factor $= (21)(41)/(6 \times 20) = 7.175$; $\sqrt{7.175} = 2.679$. Liquidation-horizon VaR $= 930{,}539 \times 2.679 = \$2{,}492{,}560$. Holding all of it for 20 days: $930{,}539 \times \sqrt{20} = \$4{,}161{,}498$.

LVaR $= 2{,}492{,}560 + 0.5 \times 0.01 \times 20{,}000{,}000 = \$2{,}592{,}560$. On a normal-spread day the one-day LVaR would be \$950,539.

A 200,000-share position exits in 4 days.

**Check.** For large $T$ the factor approaches $T/3 = 6.67$. At $T = 20$ it is 7.175, which is slightly higher, as expected. ✓

**Decision consequence.** The honest risk of the \$20m position is about \$2.6m (4.3% of NAV), not \$0.93m, because it cannot be sold in a day. Worse, the 20 days assume the 250,000-share ADV persists in stress, when ADV in small caps can halve as spreads widen. Either cut the position to what can be sold in about five days (250,000 shares), or charge the budget for LVaR at a stressed participation rate. A position you cannot exit before your stop is not controlled by your stop.

### Example 21.10 — Financing risk: futures margin and an LTV covenant

**Given.** (a) The 34 ES contracts with \$1.0m of account equity. Initial margin \$24,000 and maintenance \$22,000 per contract [HYPOTHESIS: margins are set by CME and change; check current levels]. (b) The hotel: value \$30m, loan \$21m (70% LTV), maximum-LTV covenant 75%, tested quarterly on an appraisal.

**Find.** (a) The fall in ES that triggers a call, the call at the trigger, and the call after a 10% fall. (b) The value decline that breaches the covenant, and the cure after declines of 15% and 35%.

**Solution (a).** Maintenance total $= 34 \times 22{,}000 = \$748{,}000$. Trigger $= (1{,}000{,}000 - 748{,}000)/(34 \times 50) = 148.2$ points (2.96%). Call at trigger $= 34 \times (24{,}000 - 22{,}000) = \$68{,}000$. After a 10% fall (500 points): loss $= 34 \times 500 \times 50 = \$850{,}000$; equity \$150,000; call $= 816{,}000 - 150{,}000 = \$666{,}000$, payable the next morning.

**Solution (b).** Breach decline $= 1 - 21/(0.75 \times 30) = 1 - 0.9333 = 6.67\%$. At −15%: $V_1 = \$25.5$m, cure $= 21.0 - 0.75 \times 25.5 = \$1.875$m. At −35%: $V_1 = \$19.5$m, cure $= 21.0 - 14.625 = \$6.375$m, and the equity is already worth zero (19.5 < 21.0).

**Check.** At the breach, $V = 30 \times (1 - 0.0667) = 28.0$ and $21.0/28.0 = 75.0\%$. ✓

**Decision consequence.** The futures fail on a 3% move and the hotel on a 6.7% appraisal decline. Neither is a tail event. What matters is whether the cash exists to meet the call or cure *without selling something else at a bad price*. The book's \$10m of free cash covers the futures in any plausible move and the 15% cure, but a 35% hotel decline presents a choice: inject \$6.4m into an asset whose equity is gone, or hand back the keys. Decide that in advance and write it into the hotel's position limit. Financing terms turn an asset's price path into a sequence of cash demands, and the cash demands are what you size.

### Example 21.11 — A gap through a stop, and the price of a real limit

**Given.** The 34 ES contracts entered at 5,000 with a stop at 4,850. A weekend event; Monday's first trade is 4,700 [HYPOTHESIS]. Alternative: buy 34 one-month 4,850 puts (18% vol, $r$ = 4%, $T$ = 1/12).

**Find.** Planned and realized loss; cost of the puts and the maximum loss with them.

**Solution.** Planned $= 34 \times 150 \times 50 = \$255{,}000$. Realized at 4,700: $34 \times 300 \times 50 = \$510{,}000$, twice the plan. Put premium 39.66 points, so cost $= 34 \times 50 \times 39.66 = \$67{,}424$ (0.79% of notional for one month). Maximum loss with the puts (to expiry) $= 255{,}000 + 67{,}424 = \$322{,}424$, whatever the gap.

**Check.** Realized/planned $= (5{,}000 - 4{,}700)/(5{,}000 - 4{,}850) = 2.0$. ✓

**Decision consequence.** A stop limits the loss only when the market trades continuously through the stop price. Overnight, over weekends, at limit-down halts and in private assets, it does not. Size off the gap you can plausibly suffer, not off the stop. If you need a hard cap, buy it. At about 0.8% a month, roughly 9.5% a year if rolled, permanent insurance on an equity position costs more than the equity premium. That is why hard caps are bought for events and windows (an election, a covenant test, a refinancing date), not as a standing policy.

### Example 21.12 — Transaction costs as a sizing input

**Given.** (a) A futures trend strategy with 5% gross excess return at 10% vol (gross Sharpe 0.50), 20 round trips a year, 5 bp round-trip cost. (b) The same signals applied to small-cap REITs: 8 round trips a year, 60 bp round trip. (c) A CRE acquisition with 2% buy costs and 3% sell costs, held 3 or 7 years.

**Find.** Net Sharpe for (a) and (b); the CRE round trip and annualized drag.

**Solution.** (a) Drag $= 20 \times 0.0005 = 1.0\%$; net Sharpe $= (5.0 - 1.0)/10 = 0.40$. (b) Drag $= 8 \times 0.006 = 4.8\%$; net Sharpe $= 0.2/10 = 0.02$. (c) Round trip $= 1 - 0.97/1.02 = 4.90\%$. Annualized drag: 3 years 1.66%, 7 years 0.72%.

**Check.** For small costs the round trip is about $b + s = 5\%$; the exact 4.90% is slightly lower because the sell cost applies to a base reduced by the buy cost. ✓

**Decision consequence.** The same signal is a strategy in futures and nothing in small caps. In CRE, a three-year hold must clear about 1.7 points a year of friction before any risk premium, which is one reason short CRE holds are speculative even when the asset is stable (Chapter 1). Kelly and volatility sizing both assume costless rebalancing. Every rebalance band, stop-out and roll pays the round trip, so the turnover a sizing rule creates belongs in its expected return.

### Example 21.13 — Stress-testing a public–private book

**Given.** The opening book and two historical-analogue scenarios. **The shocks are hypothetical, chosen to match the direction and rough character of each episode. They are not measured magnitudes from those episodes** [HYPOTHESIS].

| Shock | "2008-analogue": credit crunch, flight to quality | "2022-analogue": inflation and rate shock |
|---|---|---|
| 10-year yield | −150 bp | +200 bp |
| ES | −40% | −20% |
| Hotel value | −35% | −15% |
| Office loan mark | −12% | −5% |

Treasury P&L $= V(-D\,\Delta y + \tfrac12 C\,\Delta y^2)$. The hotel loan is non-recourse, so the equity loss is capped at \$9m.

**Find.** P&L by position and in total; the share of NAV; concentration of the stress loss; cash demands.

**Solution.**

*2008-analogue.* Treasuries: $25{,}000{,}000 \times (8 \times 0.015 + 0.5 \times 75 \times 0.000225) = 25{,}000{,}000 \times 0.12844 = +\$3{,}210{,}938$. ES: $8{,}500{,}000 \times (-0.40) = -\$3{,}400{,}000$. Hotel: $V_1 = \$19.5$m < \$21.0m loan, so equity is lost: $-\$9{,}000{,}000$. Loan: $15{,}000{,}000 \times (-0.12) = -\$1{,}800{,}000$.

*2022-analogue.* Treasuries: $25{,}000{,}000 \times (-8 \times 0.02 + 0.5 \times 75 \times 0.0004) = 25{,}000{,}000 \times (-0.145) = -\$3{,}625{,}000$. ES: −\$1,700,000. Hotel: $V_1 = \$25.5$m, equity \$4.5m, loss −\$4,500,000. Loan: −\$750,000.

| Position | 2008-analogue | 2022-analogue |
|---|---|---|
| Treasuries | +3,210,938 | −3,625,000 |
| ES futures | −3,400,000 | −1,700,000 |
| Hotel equity | −9,000,000 | −4,500,000 |
| Office loan | −1,800,000 | −750,000 |
| **Total** | **−10,989,063** | **−10,575,000** |
| % of NAV | −18.3% | −17.6% |
| Effective number of losing positions (1/HHI of losses) | 2.10 | 3.04 |
| Cash demand (futures variation margin + hotel cure to 75%) | \$3.40m + \$6.375m | \$1.70m + \$1.875m |

By gross exposure (Treasuries \$25m, ES \$8.5m, hotel \$30m, loan \$15m) the effective number of positions is 3.38. In the 2008-analogue the hotel alone accounts for 63% of the losses.

**Check.** The two totals are close, but their composition is not: the Treasury leg swings by \$6.8m between scenarios. ✓

**Decision consequence.** The stress loss is about 32 times the reported one-day VaR (\$10.99m against \$0.34m). The position that dominates it, the hotel, is invisible to VaR. The Treasuries hedge the equity in one regime and add to the loss in the other, so the book's diversification depends on which kind of crisis arrives. The decision levers, in order of effect: (1) set the hotel's LTV, and hold a dedicated cure reserve, to survive the 2008-analogue without a forced choice (§21.6); (2) do not add the hotel REIT, which would raise the hotel share of stress loss further; (3) report stress loss and VaR side by side, with a limit on each. Stress tests attach no probabilities, so they do not rank outcomes. They show which single assumption, if wrong, would cost the most.

---

## 21.6 CRE application: the cure reserve is the CRE stop-loss

A private property has no stop order. The closest equivalent is the combination of leverage and the cash set aside to defend the covenant. Hold the hotel's value at \$30m and apply the 2008-analogue's 35% decline ($V_1 = \$19.5$m), with the covenant at 75%:

| Initial LTV | Loan | Post-shock LTV | Cure to 75% | Equity after shock |
|---|---|---|---|---|
| 50% | \$15.0m | 76.9% | \$0.375m | \$4.5m |
| 60% | \$18.0m | 92.3% | \$3.375m | \$1.5m |
| 70% | \$21.0m | 107.7% | \$6.375m | \$0 (underwater by \$1.5m) |

The maximum initial LTV that stays inside the 75% covenant after a 35% decline is $0.75 \times 0.65 = 48.75\%$.

Three consequences follow. First, the sizing variable in CRE is LTV, and the "stop" is the cure reserve: equity committed = down payment + reserve. At 60% LTV the investor who reserves \$3.4m is committing \$15.4m to the hotel, not \$12m. Second, the reserve buys time, not value. It is worth funding only if your view of value after the shock is above the loan, because otherwise you are paying to keep an option on an underwater asset. That can still be rational if the option has time value (Chapter 12). Third, recourse carve-outs, completion guarantees and cash-management triggers can turn "non-recourse" into partial recourse. Read the guaranty before you assume the equity loss is capped.

---

## 21.7 When the relationship fails

1. **Volatility is not a constant.** Square-root-of-time scaling and sizing by trailing volatility both fail when volatility clusters. Vol targeting cuts positions *after* the shock, which is late and costly, and increases them in calm periods, when volatility is about to rise.
2. **Correlations are regime-dependent.** Estimated correlations average over regimes. In forced-selling episodes, correlations across risky assets rise toward one, and hedges can change sign (Example 21.3). Diversification estimated in calm markets is an upper bound on what you get in stress.
3. **Marks lag in private assets.** Appraisal-based values are smoothed (Chapter 2), so private CRE looks low-volatility and low-correlation in VaR. Unsmooth the marks, or carry private positions in the book only through stress scenarios.
4. **The model can change while the risk stays the same.** A new methodology, a new window or a data error can halve VaR overnight (§21.8). Any large VaR change without a position change needs an explanation and a parallel run.
5. **Kelly assumes known parameters, costless continuous rebalancing, and no financing constraint.** All three fail. The growth-optimal leverage of 2.3× in Example 21.7 is unreachable when a 3% move triggers a margin call.
6. **Ruin is often defined by someone else.** A lender's covenant, a prime broker's margin rule or an investor's redemption right can stop the strategy long before wealth reaches zero. Ruin probabilities must be computed against the *binding* floor.
7. **Stress scenarios are chosen by people.** A scenario set that omits the crisis that actually arrives gives false comfort. Use at least two analogues whose hedges behave differently, and a reverse stress test: what shock exhausts the cash?

---

## 21.8 Historical episode: JPMorgan's "London Whale", 2012 — a VaR model change during a limit breach

**Date and environment.** In 2011–2012 JPMorgan Chase's Chief Investment Office (CIO) ran a "Synthetic Credit Portfolio" (SCP) of credit-derivative index positions from its London office. The bank's Q1 2012 disclosures and later investigations are the record. The U.S. Senate Permanent Subcommittee on Investigations (PSI) published its bipartisan report, *JPMorgan Chase Whale Trades: A Case History of Derivatives Risks and Abuses*, on 14 March 2013 and held a hearing on 15 March 2013 [FACT; ch21-S01, VERIFIED-SECONDARY].

**What happened.**

* The SCP lost at least \$6.2 billion in 2012 [FACT; ch21-S01, VERIFIED-SECONDARY].
* According to the PSI, in the first quarter of 2012 the CIO built the SCP into a \$157 billion portfolio of synthetic credit derivatives [FACT; ch21-S01, VERIFIED-SECONDARY via summaries]. That is a notional figure, not a measure of risk.
* As early as January 2012 the SCP's growth breached the CIO's VaR limit and contributed to a breach of the bank-wide VaR limit. Between 1 January and 30 April 2012, CIO risk limits and advisories were breached more than 330 times [FACT, as reported from the PSI report; ch21-S01, ch21-S10; VERIFIED-SECONDARY].
* A new CIO VaR model was approved and implemented in late January 2012. The PSI report, as quoted in a Federal Reserve comment-file document, says the new model immediately reduced the CIO's VaR by 50%, from \$132 million to \$66 million [FACT; ch21-S02, VERIFIED-SECONDARY]. As reported by IFR, the bank's own task force found operational errors in the new model's spreadsheet implementation, including in the calculation of relative changes in hazard rates and correlation estimates, that muted volatility by about a factor of two. The CIO reverted to the prior model in the second quarter of 2012. Reported CIO VaR was about \$67 million on average for Q1 2012 under the new model and about \$129 million under the old model [FACT as reported; ch21-S03, ch21-S04, VERIFIED-SECONDARY]. The two pairs of numbers (\$132m/\$66m and \$129m/\$67m) come from different measurement points and have not been reconciled against the primary documents *(verification pending)*.
* On 13 July 2012 the bank announced a restatement of Q1 2012 results that reduced net income by \$459 million, after its review raised questions about the integrity of the traders' marks [FACT; ch21-S05, VERIFIED-SECONDARY].
* In September 2013 the bank agreed to penalties of about \$920 million: \$300 million to the OCC, \$200 million to the Federal Reserve, \$200 million to the SEC and £137.6 million to the UK FCA. As part of the SEC settlement it admitted the facts underlying the charges, which centered on internal controls [FACT; ch21-S06, VERIFIED-SECONDARY].

**Mechanism in this chapter's terms.** VaR is linear in volatility (§21.4.2). An implementation that halves the measured relative changes of the risk factors halves the measured volatility, and therefore halves VaR, with no change in positions. Put the reported \$66 million into Example 21.3's arithmetic: the same book under the prior model would read \$132 million, and the "breach" disappears by construction. The PSI's characterization is that the model change was pressed through in part to end the limit breach [FACT that the PSI so found; ch21-S02]. Whether that is the right reading of motive is a separate question from the arithmetic, which holds either way.

**What was knowable at the time.** Inside the bank: that the portfolio's notional size had grown sharply; that limits were being breached repeatedly; and that a model change had cut VaR roughly in half while positions grew. Whether other internal risk measures (credit-spread sensitivities, stress limits) were signalling the same growth is described in the PSI report but was not checked for this chapter *(verification pending)*. Outside the bank: press reports in April 2012 described a large CIO trader moving credit indices [INFERENCE from the episode's naming; specific articles not cited here, *(verification pending)*]. No outsider could see the VaR model.

**Competing interpretations.**

1. *Model risk and operational error.* The task-force reading: a flawed spreadsheet model, inadequately validated, understated risk [FACT that this was the task force's emphasis, as reported; ch21-S03].
2. *Governance and incentives.* The PSI reading: the risk limits were treated as obstacles, the model change served to end a breach, and marks were managed to hide losses [FACT that the PSI so found; ch21-S01].
3. *Hedge that became a position.* The SCP was described as a hedge of the bank's credit exposure. A hedge whose size, composition and P&L are managed as a stand-alone book has become a speculative position, which is the classification question of Chapter 1 [INFERENCE].

**What the case does and does not establish.** It establishes that a risk measure can be changed faster than the risk, and that a large VaR decline coinciding with a limit breach and growing positions is a red flag in itself. It establishes that limits are only as strong as the process for changing the model that feeds them. It does **not** establish that VaR is useless, or that the losses were *caused* by the model change rather than by the positions and market moves. Nor does it settle the motive question, which the PSI and the bank characterized differently.

**Desk rules that follow.** (i) No model change takes effect during a limit breach without a parallel run and sign-off from someone outside the business line. (ii) Every VaR report shows the prior model's number for at least one quarter after a change. (iii) Notional, CS01/DV01 and stress limits sit beside VaR, so that one model cannot clear all of them. (iv) Back-test exceptions are counted against the binomial distribution: five exceptions in 60 days at 99% has probability 0.035% under a correct model (Problem 21.10).

---

## 21.9 Decision exercise: re-limit the Monday book

You present to the investment committee. Use the opening book, Examples 21.3, 21.9, 21.10 and 21.13, and §21.6. Produce a one-page decision record (`desk/investment_memos/decision_record_template.md`) that contains:

1. A limit framework with at least four metrics (e.g., one-day 99% ES on liquid positions, stress loss under each analogue, gross notional/NAV, minimum free cash after stress) and a number for each.
2. A decision on the hotel REIT: size it, or decline it. If you size it, show the binding constraint.
3. A decision on the hotel's leverage: keep 70% LTV with a stated cure reserve, refinance lower, or sell. Show the cash arithmetic.
4. A decision on the short-put overlay of Example 21.6.
5. A stated rule for VaR model changes (§21.8).
6. What would change your recommendations: name the evidence.

**Rubric** (10 points).

| Points | Criterion |
|---|---|
| 2 | Uses stress loss and cash demands, not VaR alone, to size the private positions |
| 2 | Identifies the hotel as the dominant stress exposure and acts on leverage or reserves with explicit numbers |
| 1 | Declines the hotel REIT or sizes it to ≤ about 5 days of exit capacity, with the LVaR charged |
| 1 | Treats the short-put overlay as adding tail risk; prices it with Monte Carlo ES, not delta-normal |
| 1 | Notes the Treasury hedge's sign dependence across scenarios |
| 1 | Writes a model-change governance rule |
| 1 | States a pre-committed drawdown or cash-floor stop for the book |
| 1 | Names the evidence that would change the decision (e.g., stock–bond correlation regime, appraisal trend, refinancing terms) |

There is no single correct allocation. A recommendation to do nothing new and fund the hotel cure reserve can earn full marks.

---

## 21.10 Frequent analytical errors

1. **Reporting VaR as "the most we can lose".** VaR is a quantile, not a maximum. ES describes the tail beyond it, and a stress test shows what a named scenario would do.
2. **Leaving private assets out of the risk report** because they have no daily price. Their absence makes the reported number smaller, not the risk.
3. **Using the window correlation in a stress.** Re-run VaR at ρ = 1, and at hedge correlations of the opposite sign.
4. **Treating a stop as a cap.** Size off plausible gaps. Buy a cap if you need one.
5. **Linear VaR on non-linear books.** Short options, prepayable loans and levered equity need full revaluation.
6. **Full Kelly on estimated parameters.** Estimation error alone costs $1/(2T)$ a year in expected growth at full Kelly, and overbetting by 2× eliminates growth.
7. **Square-root-of-time scaling across a liquidation horizon** without asking whether the position can be sold in that time, and at what spread.
8. **Ignoring the financing path.** Ruin is reached at the margin call or covenant breach, not at zero wealth.
9. **Measuring concentration by capital.** Measure it by stress loss.
10. **Accepting a VaR drop that has no position change behind it.**
11. **Mixing conventions.** Historical VaR at "the 5th worst" versus "the 6th worst" out of 500 observations, one-day versus ten-day horizons, and percent of notional versus percent of NAV are all reported as "VaR".

---

## 21.11 Connections to other chapters

* Chapter 1 (§1.4.5, Example 1.5): the two-outcome Kelly bet and volatility drag that §21.4.4 extends.
* Chapter 2: appraisal smoothing, which hides private-asset volatility; market impact beyond the spread.
* Chapter 3: reflexive forced selling, the mechanism behind correlation going to one.
* Chapter 6: duration and convexity used in the Treasury stress leg.
* Chapter 10: LTV, DSCR and debt-yield covenants; cure mechanics.
* Chapter 11: hotel operating leverage, which explains why the hotel shock is the largest.
* Chapter 12: distress and the option value of holding an underwater asset.
* Chapter 20: estimation error and overfitting, which enlarge $s$ in the Kelly penalty.
* Chapter 23: 1987, LTCM and 2008 in full.
* Case H (cross-asset macro shock) and Case J (credit-crunch hotel) apply the stress-test and covenant arithmetic.

---

## 21.12 One-page reference sheet

| Quantity | Formula | Library |
|---|---|---|
| Size by stop | $n = \rho C/(\lvert P - P_s\rvert M)$ | `risk.position_size_by_stop` |
| Size by vol | $n = \tau/(PM\sigma)$ | `x_risk_mgmt.size_by_volatility` |
| Size by VaR budget | $n = B/(z_c\sigma PM)$ | `x_risk_mgmt.size_by_var_budget` |
| Normal VaR / ES | $z_c\sigma V$; $\frac{\phi(z_c)}{1-c}\sigma V$ ($z_{.99} = 2.3263$; 2.6652) | `risk.parametric_var`, `parametric_es` |
| Historical VaR (n obs) | $(\lfloor n(1-c)\rfloor + 1)$-th worst loss | `risk.historical_var`, `historical_es` |
| Portfolio σ | $\sqrt{\sum\sum s_is_j\rho_{ij}}$ | `risk.portfolio_volatility` |
| Component VaR | $z_c\sum_j s_is_j\rho_{ij}/\sigma_p$ | test helper |
| Continuous Kelly | $f^* = (\mu-r)/\sigma^2$; $G^* = (\mu-r)^2/2\sigma^2$ | `risk.kelly_continuous` |
| Fractional Kelly growth | $G^*c(2-c)$; half-Kelly: 75% of growth, 25% of variance | `x_risk_mgmt.kelly_growth` |
| Estimation penalty (k = 1) | $s^2/2\sigma^2 = 1/(2T)$ | `kelly_growth_with_estimation` |
| Optimal shrink | $k^* = m^2/(m^2 + s^2)$ | `kelly_optimal_shrink` |
| P(ever lose d) | $(1-d)^{2m/s^2}$; at $cf^*$: $(1-d)^{2/c-1}$ | `prob_ever_below` |
| Gambler's ruin (no target) | $(q/p)^k$ | `gamblers_ruin` |
| Liquidation VaR | VaR$_1\sqrt{(T+1)(2T+1)/6T}$ | `liquidation_variance_factor` |
| LVaR | VaR$_T$ + ½ S$_{stress}$ V | `liquidity_adjusted_var` |
| Margin-call trigger | $(A - n\,m_m)/(nM)$ | `futures_margin_call` |
| LTV breach decline | $1 - L/(\lambda V)$ | `ltv_covenant` |
| Gap loss ratio | $(P - P_{fill})/(P - P_s)$ | `gap_loss` |
| Cost drag | turnover × round trip | `x_microstructure.round_trip_cost` |
| Effective N | $1/\sum s_i^2$ | `herfindahl` |

**Rules of thumb (to be tested, not trusted).** At full Kelly, P(ever halving) = 50%. At half Kelly it is 12.5%. Halving bet size squares the gambler's-ruin probability. Even liquidation over $T$ days carries about $\sqrt{T/3}$ days of VaR. A 75% LTV covenant on a 70% LTV loan breaches on a 6.7% value decline.

---

## References for this chapter

Sources are listed with status in `references/sources_ch21.md`.

* Artzner, P., Delbaen, F., Eber, J.-M., and Heath, D. (1999). "Coherent Measures of Risk." *Mathematical Finance*, 9(3), 203–228.
* Bangia, A., Diebold, F. X., Schuermann, T., and Stroughair, J. D. (1999). "Modeling Liquidity Risk, with Implications for Traditional Market Risk Measurement and Management." Wharton Financial Institutions Center working paper *(bibliographic details pending)*.
* Kelly, J. L. (1956). "A New Interpretation of Information Rate." *Bell System Technical Journal*, 35(4), 917–926.
* Feller, W. (1968). *An Introduction to Probability Theory and Its Applications*, Vol. 1, 3rd ed. Wiley (ch. XIV, gambler's ruin).
* Jorion, P. (2007). *Value at Risk: The New Benchmark for Managing Financial Risk*, 3rd ed. McGraw-Hill.
* MacLean, L. C., Thorp, E. O., and Ziemba, W. T., eds. (2011). *The Kelly Capital Growth Investment Criterion: Theory and Practice*. World Scientific.
* U.S. Senate Permanent Subcommittee on Investigations (2013). *JPMorgan Chase Whale Trades: A Case History of Derivatives Risks and Abuses*. Staff report, 15 March 2013.
* CME Group, Rulebook Chapter 358, E-mini S&P 500 Index Futures; "The Origins of the E-mini S&P 500" (education article).
