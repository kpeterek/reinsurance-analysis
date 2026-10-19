# Chapter 3 — The Speculator's Mental Models

> **Status:** Complete (v1.0). Every number in the text, problems, and solutions is reproduced in `tests/test_ch03_examples.py` (helpers in `models/python/sdesk/x_dynamics.py`). Problems are in `problems/questions/ch03_problems.md`, solutions in `problems/solutions/ch03_solutions.md`, sources in `references/sources_ch03.md`. Items marked *(verification pending)* are listed there and are not used as established fact.

## Learning objectives

After this chapter you should be able to:

1. Compute a hurdle rate from the **next-best alternative**, levered or de-levered to the risk of the deal in front of you, and state the dollar cost of choosing wrongly.
2. Write **reflexivity** as a collateral feedback loop (price → collateral value → lending capacity → demand → price), compute its loop gain, iterate it, and state the stability condition. Explain why the loop is stronger on the way down.
3. Convert an AR(1) coefficient into a **half-life**, forecast a mean-reverting spread, and say when the estimate cannot be trusted.
4. Define **time-series momentum**, size a volatility-scaled position, and state what the published evidence does and does not show.
5. Use a two-state **Markov regime** model to compute expected regime durations, long-run probabilities, and multi-period transition probabilities, and apply them to NOI forecasts and loan maturities.
6. Value the **option to wait** on a development parcel with a one-period binomial model and verify the answer by replication.
7. Compute the size and price impact of a **forced sale** under a leverage covenant, and the price-impact threshold beyond which selling cannot restore compliance.
8. Measure **exit capacity** for a crowded trade and size a position to it.
9. Trace a **second-order chain** from a rate rise to CRE refinancing gaps to bank lending capacity.
10. Update beliefs with **likelihood ratios** over a sequence of data points, and quantify the bid error caused by over- and under-reaction.

---

## 3.1 Opening investment problem: the lender calls with more money

You manage a closed-end fund that owns twelve select-service hotels in one Sun Belt metro. All facts in this section are [HYPOTHESIS], a constructed teaching case.

The portfolio was appraised last month at \$320 million, up roughly 30% in three years. Fund debt is a single portfolio facility of \$176 million, 55% of appraised value, with a **maintenance covenant**: if LTV on a fresh appraisal exceeds 70%, the fund must pay down the loan to 70% within 90 days. Fund equity is therefore \$144 million.

On Tuesday three things reach your desk.

1. **The upsize.** Your relationship lender offers to raise the facility to 65% LTV on the new appraisal. That is \$208 million of debt, releasing \$32 million of cash. The covenant stays at 70%. The banker mentions that "four or five" other owners in the metro have taken similar upsizes this year and are using the cash to buy hotels in the same metro.
2. **The land.** A landowner offers a pad site zoned for a 120-room hotel at a price equal to its residual land value: completed value less construction cost. The landowner argues that any price at or above residual is fair.
3. **The data.** The latest monthly STR report shows metro RevPAR down 4% year over year. It is the first negative print in 30 months. Your asset manager calls it noise.

You also have the alternative every speculator has: do nothing, keep the 55% facility, and put spare cash in a diversified core real estate fund.

Each item calls on a different mental model. The upsize is a question about **reflexivity**, **forced selling**, and **crowding**. The land is a question about **optionality**. The RevPAR print is a question about **Bayesian updating** and **regime change**. Doing nothing is the **opportunity cost** against which every action must be measured. Section 3.10 returns to the decision.

---

## 3.2 Economic intuition

A mental model is useful to a speculator only if it changes a number in a decision. "Markets are reflexive" is a slogan. "This lending market has a loop gain of 0.63 on the way up and 0.83 on the way down, so a 5% shock becomes 13.5% or 30%" is a model. The chapter treats each idea in this second sense. Each one is a small, explicit mechanism with parameters you can estimate, argue about, and stress.

The models group into four families.

**Valuation against alternatives.** Every action has an opportunity cost: the return on the best thing you are not doing. A hurdle is not a target return chosen to look respectable. It is the return of the next-best alternative at the same risk. A deal that beats an unlevered core fund but loses to the same core fund levered to the deal's risk is a bad deal.

**Dynamics: how prices move through time.** Three patterns recur. *Mean reversion*: deviations from a long-run level decay, at a rate you can measure. *Momentum*: recent returns predict near-term returns with the same sign. *Regimes*: the process generating returns switches between states, each persistent, and the switching probabilities determine how long each state lasts. These patterns are not contradictory. A cap-rate spread can mean-revert over years, trend over months, and behave differently in a credit crunch than in an expansion.

**Feedback: when prices change the fundamentals they are supposed to reflect.** George Soros called this *reflexivity* in *The Alchemy of Finance* (1987). Participants' beliefs move prices (the "manipulative function"), and prices change the reality participants are trying to understand (the "cognitive function") [FACT: Soros (1987); description verified against secondary sources, see ch03-S01]. In credit markets the mechanism is concrete. Real estate is collateral. Higher prices raise borrowing capacity. Borrowed money buys more real estate. Kiyotaki and Moore (1997) formalized the same loop in a macroeconomic model in which durable assets such as land serve both as factors of production and as collateral, so credit limits and asset prices reinforce each other [FACT: ch03-S02]. Forced selling, fire sales, and crowded exits are the same loop running in reverse, with the important difference that repayment is mandatory while borrowing is optional.

**Optionality and belief.** A convex payoff gains more from good outcomes than it loses from bad ones. The right to wait before committing irreversible capital is such a payoff. It has value that a static NPV ignores, which is why vacant land in expensive cities can be rational (Titman, 1985) [FACT: ch03-S09]. Bayesian updating is the discipline that tells you how much a new data point should move your probability of each state. It protects you against the two classic errors: overreacting to a vivid single print and underreacting to an accumulating pattern.

Each model has a failure mode, set out in §3.8. A mental model is a tool for organizing evidence. It does not replace the evidence.

---

## 3.3 Technical definitions

| Term | Definition |
|---|---|
| Opportunity cost | Return forgone on the best feasible alternative use of the same capital, time, and risk budget |
| Risk-matched hurdle | Return of the next-best alternative after levering or de-levering it to the deal's volatility: $h = r_B + (\sigma_D/\sigma_A)(r_A - r_B)$ |
| Reflexivity (operational) | A loop in which the price of an asset changes the fundamentals that determine its price; here, price → collateral → credit → demand → price |
| Loop gain $m$ | Price change in the next round of a feedback loop per unit of price change in the current round |
| Amplification multiplier | Total price change per unit of initial shock, $1/(1-m)$ for $|m|<1$ |
| AR(1) process | $x_t - \mu = \phi (x_{t-1} - \mu) + \varepsilon_t$ with persistence $\phi$ |
| Half-life | Periods for an expected deviation from $\mu$ to halve: $\ln 0.5/\ln\phi$ |
| Time-series momentum (TSMOM) | Position in an asset with the sign of its own trailing return (commonly 12 months), often scaled by inverse volatility |
| Cross-sectional momentum | Long recent winners and short recent losers *relative to each other*; distinct from TSMOM |
| Markov regime model | A model in which a hidden state $s_t$ follows a Markov chain with transition probabilities $p_{ij}$, and each state has its own return or growth distribution |
| Expected regime duration | $1/(1-p_{ii})$ periods |
| Convex payoff | Payoff $f$ with $f(\tfrac{a+b}{2}) \le \tfrac{f(a)+f(b)}{2}$; gains from upside exceed losses from equal downside |
| Option to wait | The right, not the obligation, to make an irreversible investment later rather than now |
| Forced sale | A sale whose timing and size are set by a constraint (covenant, margin, redemption), not by the seller's view of value |
| Price impact | Fall in the clearing price per unit sold, $b$ in $P(s) = P_1 - bs$ |
| Exit capacity | Amount that can be sold per unit of time without more than an accepted price concession, e.g. participation rate × average daily volume |
| Crowded trade | A position held by many investors with similar constraints, so their exits coincide |
| Likelihood ratio (LR) | $P(E\mid H)/P(E\mid \neg H)$; the factor by which evidence $E$ multiplies the odds on $H$ |

---

## 3.4 Equations and derivations

### 3.4.1 The risk-matched hurdle

Let the next-best alternative earn expected return $r_A$ with volatility $\sigma_A$. If it can be levered or de-levered at rate $r_B$, a position with weight $w$ in the alternative and $1-w$ in borrowing or lending earns $r_B + w(r_A - r_B)$ with volatility $w\sigma_A$. Matching the deal's volatility $\sigma_D$ requires $w = \sigma_D/\sigma_A$, so

$$h = r_B + \frac{\sigma_D}{\sigma_A}(r_A - r_B).$$

This is the deal's opportunity cost at equal risk. Equivalently, the deal must have a Sharpe-type ratio $(r_D - r_B)/\sigma_D$ at least as large as the alternative's. Volatility is a crude risk measure for private real estate (Chapter 2 explains appraisal smoothing). The formula is a floor, not a full risk adjustment: illiquidity, tail risk, and the time you spend running the deal all argue for a higher hurdle.

### 3.4.2 The reflexive collateral loop

Let $C$ be the value of real estate pledged as collateral in a market, $\lambda$ the LTV lenders will advance against it, $\theta$ the share of new borrowing capacity that owners actually draw and spend on more real estate in the same market, and $\psi$ the fractional price change caused by one unit of net new demand (the inverse of market depth).

A fractional price change $x_k$ in round $k$ changes:

* collateral value by $x_k C$;
* borrowing capacity by $\lambda x_k C$;
* net demand by $\theta \lambda x_k C$;
* the next-round price by $x_{k+1} = \psi\theta\lambda C \, x_k$.

Define the **loop gain** $m = \lambda\theta C\psi$. After an initial shock $x_0$, the cumulative price change after $n$ rounds is the geometric sum

$$X_n = x_0 \sum_{k=0}^{n-1} m^k = x_0\frac{1-m^n}{1-m}, \qquad X_\infty = \frac{x_0}{1-m}\quad (|m|<1).$$

The **stability condition** is $m<1$. At $m \ge 1$ each round is at least as large as the last, and the linear model has no finite end point. In reality the loop ends when something else binds: lenders' capital, a regulator, or buyers' income. The model is linear in $x$ and therefore only a local approximation; large moves change $\lambda$, $\theta$, and $\psi$ themselves.

**Why the loop is stronger downward.** On the way up, $\theta$ is a choice: owners draw only part of their new capacity. On the way down, a borrower whose loan sits at the maximum LTV must *repay* the lost capacity, whatever they think of value. The downside $\theta$ is the share of collateral whose loans are at the constraint, which in a late-cycle market is high. Lenders also cut $\lambda$ after losses, which raises the downside gain further. Brunnermeier and Pedersen (2009) model this asymmetry for traders as "loss spirals" and "margin spirals", in which funding constraints and market illiquidity reinforce each other [FACT: ch03-S08].

### 3.4.3 Mean reversion and the half-life

For an AR(1) process $x_t - \mu = \phi(x_{t-1}-\mu) + \varepsilon_t$ with $E[\varepsilon_t]=0$, iterating gives

$$E[x_{t+h}\mid x_t] = \mu + \phi^h (x_t - \mu).$$

The half-life $H$ solves $\phi^H = 0.5$:

$$H = \frac{\ln 0.5}{\ln\phi}.$$

Two traps follow. First, $\phi$ is per period, so a quarterly $\phi_q$ implies an annual $\phi_a = \phi_q^4$, and the half-life in years is the quarterly half-life divided by four. Second, $H$ is very sensitive to $\phi$ near one: $dH/d\phi = -\ln 0.5/[\phi(\ln\phi)^2]$, which grows without bound as $\phi\to 1$. The least-squares estimate of $\phi$ is also biased downward in short samples (Kendall, 1954) [FACT: bibliographic, ch03-S10; the commonly quoted first-order size of the bias, about $-(1+3\phi)/n$, is *(verification pending)*]. A downward-biased $\phi$ gives a half-life that is too short, which makes a mean-reversion trade look faster and safer than it is. The chapter's tests reproduce the size of this bias by simulation (Example 3.3).

### 3.4.4 Time-series momentum

The TSMOM rule studied by Moskowitz, Ooi and Pedersen (2012) takes a position in each instrument with the sign of its own trailing return and sizes it inversely to volatility. Over 58 liquid futures and forwards (equity indices, currencies, commodities, bonds), they report that an instrument's return over the past 1 to 12 months predicts its next-month return with the same sign, and that the effect partly reverses at longer horizons [FACT: ch03-S04]. Later work disputes how much of the reported performance comes from the volatility scaling rather than the sign rule [FACT that the dispute exists: ch03-S04 notes].

With trailing compounded return $R_{12}$, annualized volatility $\sigma$, and target volatility $\sigma^*$:

$$w = \operatorname{sign}(R_{12}) \cdot \frac{\sigma^*}{\sigma}.$$

The weight $w$ is notional exposure per dollar of capital. Momentum is a statement about the conditional mean of returns. It says nothing about value, and it is a separate phenomenon from mean reversion at longer horizons. A spread can trend for a year and revert over five.

### 3.4.5 Two-state Markov regimes

Let state 1 be expansion and state 2 contraction, with transition matrix

$$\mathbf P = \begin{pmatrix} p_{11} & 1-p_{11}\\ 1-p_{22} & p_{22}\end{pmatrix}.$$

Hamilton (1989) introduced this structure for business-cycle dynamics, with growth rates that shift between discrete states that the econometrician must infer [FACT: ch03-S06].

*Expected duration.* Once in state $i$, the number of periods $D$ spent there is geometric: $P(D = d) = p_{ii}^{d-1}(1-p_{ii})$. So $E[D] = 1/(1-p_{ii})$, and the probability that the regime lasts more than $d$ periods is $p_{ii}^d$.

*Long-run probabilities.* The stationary distribution solves $\pi = \pi\mathbf P$:

$$\pi_1 = \frac{1-p_{22}}{(1-p_{11})+(1-p_{22})}, \qquad \pi_2 = 1-\pi_1.$$

*Forecasts.* The $n$-step transition probabilities are the entries of $\mathbf P^n$. If NOI grows at $g_1$ in expansion and $g_2$ in contraction, expected growth in quarter $k$ from state $i$ is $[\mathbf P^k]_{i1} g_1 + [\mathbf P^k]_{i2} g_2$.

### 3.4.6 Optionality and the value of waiting

A payoff $\max(V - I, 0)$ is convex in $V$: an option to build. Static NPV compares building now ($V_0 - I_0$) with not building (0). It ignores a third choice: wait, observe $V$, and build only if it is worth building.

One-period binomial model. The completed building is worth $V_0$ today and $uV_0$ or $dV_0$ in one year. Its owner receives a cash yield $\delta V_0$ during the year, which a waiting developer forgoes. Construction costs $I_0$ now or $I_1 = I_0(1+g_I)$ next year. The risk-neutral probability $q$ prices the completed building:

$$V_0 = \frac{\delta V_0 + q\,uV_0 + (1-q)\,dV_0}{1+r_f}\;\;\Rightarrow\;\; q = \frac{V_0(1+r_f) - \delta V_0 - dV_0}{uV_0 - dV_0}.$$

The value of waiting is

$$W = \frac{q\max(uV_0 - I_1, 0) + (1-q)\max(dV_0 - I_1, 0)}{1+r_f},$$

and the developer should build now only if $V_0 - I_0 \ge W$. The **option premium** $W - \max(V_0 - I_0, 0)$ is the value that residual land valuation leaves out. Waiting has three costs: the forgone yield $\delta$, cost inflation $g_I$, and (not modeled here) the risk that someone else uses the site or the entitlement lapses. Dixit and Pindyck (1994) develop the continuous-time version (ch03-S11; bibliographic record *verification pending*).

### 3.4.7 Forced selling under a leverage covenant

A holder owns $Q_0$ units financed with debt $D$ and must keep $D/(Q P) \le \lambda^*$. After a shock the price is $P_1$ and $D > \lambda^* Q_0 P_1$: the covenant is breached. Selling $s$ units repays $sP$ of debt. With linear price impact, the price after the sale is $P(s) = P_1 - bs$, and we mark all units, sold and retained, at $P(s)$ (a uniform-price simplification). Compliance requires

$$D - sP(s) = \lambda^*(Q_0 - s)P(s) \;\;\Longleftrightarrow\;\; P(s)\,[\lambda^* Q_0 + (1-\lambda^*)s] = D.$$

*No impact* ($b=0$): $s = (D/P_1 - \lambda^* Q_0)/(1-\lambda^*)$. Each dollar of sales cuts debt by a dollar but cuts the *allowed* debt by only $\lambda^*$ dollars, so the gap closes at rate $1-\lambda^*$. At $\lambda^* = 0.75$ you must sell four dollars of assets to close one dollar of covenant gap.

*With impact*, the left side $f(s) = (P_1 - bs)[\lambda^*Q_0 + (1-\lambda^*)s]$ is a downward-opening parabola. Two thresholds matter:

1. **Marginal condition.** Selling helps at the margin only if $f'(0) > 0$: $b < (1-\lambda^*)P_1/(\lambda^* Q_0)$. Above this, the first unit sold *worsens* the covenant, because the price impact on the retained position exceeds the debt repaid.
2. **Feasibility.** A cure exists only if the maximum of $f$ reaches $D$. The maximum is $[(1-\lambda^*)P_1 + b\lambda^*Q_0]^2 / [4b(1-\lambda^*)]$, so the critical impact $b^\dagger$ solves the quadratic $[(1-\lambda^*)P_1 + b\lambda^*Q_0]^2 = 4b(1-\lambda^*)D$ (take the smaller root). For $b > b^\dagger$ no partial sale cures the breach. The holder is liquidated or the lender must waive.

Shleifer and Vishny (1992) explain why $b$ is large exactly when forced sales occur: the natural buyers of a distressed asset are firms in the same industry, and they tend to be constrained at the same time [FACT: ch03-S07].

### 3.4.8 Exit capacity

If an asset trades an average daily volume $ADV$ and you can sell at a participation rate $\rho$ without more than an accepted concession, a position $X$ takes $T = X/(\rho\,ADV)$ days to exit. When $N$ holders with total position $\sum X_j$ exit at the same time and the market absorbs at most $\rho\,ADV$ of net selling per day, the relevant number is $\sum X_j/(\rho\,ADV)$, not your own $T$. For private real estate replace $ADV$ with annual transaction volume in the submarket and property type.

### 3.4.9 Bayesian updating in odds form

Bayes' rule in odds form is

$$\underbrace{\frac{P(H\mid E)}{P(\neg H\mid E)}}_{\text{posterior odds}} = \underbrace{\frac{P(H)}{P(\neg H)}}_{\text{prior odds}} \times \underbrace{\frac{P(E\mid H)}{P(E\mid\neg H)}}_{LR}.$$

For signals $E_1,\dots,E_n$ that are **conditionally independent** given $H$, the LRs multiply, and the order of arrival does not matter. Log-odds add: $\ell_n = \ell_0 + \sum_k \ln LR_k$. A simple model of biased updating scales each log-LR by a weight $\omega$: $\omega = 1$ is Bayesian, $\omega<1$ is under-reaction (conservatism), $\omega>1$ is over-reaction. Barberis, Shleifer and Vishny (1998) built a model in which investors produce both under-reaction to individual news and over-reaction to a series of news in the same direction [FACT: ch03-S05]. If the signals are correlated, multiplying their LRs double-counts the shared information. That is over-reaction by construction, even when each LR is individually correct.

### 3.4.10 Negative feedback with a lag

Not all feedback amplifies. High hotel RevPAR draws new supply, which lowers RevPAR, with a construction lag. If a deviation $x_t$ of RevPAR from its long-run level produces supply that changes the next period's deviation by $-g x_t$, then $x_{t+1} = -g x_t$. For $0<g<1$ the deviation oscillates with shrinking amplitude. With $g = 0.8$ and a +10% starting deviation, the path is +10%, −8%, +6.4%, −5.12%. For $g>1$ the oscillation grows, the classic cobweb instability [HYPOTHESIS: illustrative parameters]. A lagged supply response is stabilizing in the long run and destabilizing in the short run. Developers who all respond to the same high RevPAR deliver into the same down-phase.

---

## 3.5 Worked examples

All inputs are [HYPOTHESIS] unless cited. All ten examples are reproduced in `tests/test_ch03_examples.py`.

### Example 3.1 — Opportunity cost: the risk-matched hurdle

**Given.** \$10 million of fund equity. The next-best alternative is a diversified core open-end real estate fund with expected net return $r_A = 7.0\%$ and volatility $\sigma_A = 8\%$. The fund can borrow on a subscription or NAV line at $r_B = 5.5\%$. The deal is a value-add hotel acquisition with expected levered equity IRR 11.0% and estimated volatility $\sigma_D = 16\%$ (twice the alternative's). Five-year horizon.

**Find.** The risk-matched hurdle; the terminal wealth of the deal and of the matched alternative; the verdict if the deal's IRR were 8.0%.

**Solution.**

$$h = r_B + \frac{\sigma_D}{\sigma_A}(r_A - r_B) = 5.5\% + \frac{16}{8}(7.0\% - 5.5\%) = 5.5\% + 3.0\% = 8.5\%.$$

Terminal wealth over five years, compounding annually:

* Deal: $10 \times 1.11^5 = 10 \times 1.68506 = \$16.85$ million.
* Matched alternative: $10 \times 1.085^5 = 10 \times 1.50366 = \$15.04$ million.
* Excess: \$1.81 million, or \$1.21 million in present value at the 8.5% hurdle ($1.814/1.50366$).

At an IRR of 8.0% the deal clears the *unlevered* alternative (7.0%) by 1.0 percentage point and fails the *risk-matched* one (8.5%) by 0.5 point.

**Check.** Sharpe-type ratios: alternative $(7.0 - 5.5)/8 = 0.1875$; deal at 11%: $(11.0-5.5)/16 = 0.344$; deal at 8%: $(8.0-5.5)/16 = 0.156 < 0.1875$. ✓

**Decision consequence.** The natural comparison, "11% versus 7%", overstates the deal's edge. The correct comparison is 11% versus 8.5%, a 2.5-point margin that must still pay for illiquidity, the hotel's operating risk beyond volatility, and the hours of asset management the core fund does not require. An 8% hotel deal should be rejected even though it "beats core". Write the risk-matched hurdle into the investment memo before you see the deal's IRR, so the hurdle is not adjusted to fit the deal.

### Example 3.2 — Reflexivity as a collateral loop: iteration and the stability condition

**Given.** In a metro hotel market, collateral pledged to lenders is $C = 100$ (\$ billions is convenient, but any unit works as long as $\psi$ matches). Lenders advance $\lambda = 0.70$ against appraised value. Owners draw and spend $\theta = 0.60$ of any new capacity on more local hotels. Each \$1 billion of net new demand raises prices by 1.5%, so $\psi = 0.015$ per \$ billion. An initial demand shock raises prices by $x_0 = 5\%$.

**Find.** The loop gain; the first five rounds; the total effect; the gain if credit loosens to $\lambda = 0.85$ and $\theta = 0.80$.

**Solution.**

$$m = \lambda\theta C\psi = 0.70 \times 0.60 \times 100 \times 0.015 = 0.63.$$

In words: a 1% price rise adds \$1.0 billion of collateral, \$0.70 billion of capacity, and \$0.42 billion of spending, which raises prices by $0.42 \times 1.5\% = 0.63\%$.

| Round $k$ | Increment $x_0 m^k$ | Cumulative |
|---|---|---|
| 0 | 5.000% | 5.000% |
| 1 | 3.150% | 8.150% |
| 2 | 1.985% | 10.135% |
| 3 | 1.250% | 11.385% |
| 4 | 0.788% | 12.172% |
| ∞ | — | $5\%/(1-0.63) = 13.51\%$ |

The multiplier is $1/(1-0.63) = 2.70$: a 5% fundamental shock becomes a 13.5% price move.

With looser credit: $m = 0.85 \times 0.80 \times 100 \times 0.015 = 1.02 > 1$. The loop is unstable. Each round is larger than the last, and nothing inside the model stops it.

**Check.** After rounds 0–4 (five terms) the cumulative is $5\% \times (1-0.63^5)/(1-0.63) = 12.17\%$, matching the table. ✓

**Decision consequence.** The gain depends on lender behavior ($\lambda$), owner behavior ($\theta$), and market depth ($\psi$), not on hotel fundamentals. A rise in permitted LTV from 70% to 85% does not merely add 15 points of leverage. Combined with more aggressive drawing, it moves the market across the stability boundary. For the opening problem, the lender's offer to move from 55% to 65% is one fund's contribution to $\lambda$, and "four or five other owners doing the same" is $\theta$ rising. The question to ask is not "is 65% LTV safe for my fund?" but "what is the market's loop gain once everyone does this, and what happens when it runs in reverse?" Section 3.7 answers the second half.

### Example 3.3 — Mean reversion: the half-life of a cap-rate spread

**Given.** You model the spread between a hotel cap-rate series and the 10-year Treasury yield as a quarterly AR(1) with long-run mean $\mu = 3.0\%$ and persistence $\phi = 0.90$, estimated on 80 quarters [HYPOTHESIS: illustrative parameters, not an estimate from published data]. The current spread is 2.0%. The Treasury is 4.5% and assumed constant. NOI is held constant.

**Find.** The half-life; the expected spread and cap rate in 4 and 8 quarters; the implied value change over 8 quarters; the same with $\phi = 0.97$; and the size of the small-sample bias in $\hat\phi$.

**Solution.**

Half-life: $H = \ln 0.5/\ln 0.90 = -0.69315/-0.10536 = 6.58$ quarters (1.64 years).

Expected spread: $E[x_{t+h}] = 3.0\% + 0.90^h(2.0\% - 3.0\%)$.

* $h=4$: $0.90^4 = 0.6561$; spread $= 3.0\% - 0.656\% = 2.344\%$; cap rate 6.844%.
* $h=8$: $0.90^8 = 0.43047$; spread $= 3.0\% - 0.430\% = 2.570\%$; cap rate $4.5\% + 2.570\% = 7.070\%$.

Value change with constant NOI: $V_8/V_0 = c_0/c_8 = 6.5\%/7.0695\% = 0.9194$, a decline of 8.06%.

With $\phi = 0.97$: $H = \ln 0.5/\ln 0.97 = 22.76$ quarters (5.7 years). In 8 quarters the spread is $3.0\% - 0.97^8 \times 1.0\% = 3.0\% - 0.784\% = 2.216\%$, the cap rate 6.716%, and the value change $6.5/6.7163 - 1 = -3.22\%$.

Annual persistence: $0.90^4 = 0.656$ per year. A model that mistakes the quarterly 0.90 for an annual coefficient would give a half-life of 6.58 *years* rather than quarters.

Small-sample bias: in 4,000 simulated 80-quarter paths with true $\phi = 0.90$ (random seed fixed in the tests), the average OLS estimate is about 0.85. The test asserts it lies between 0.83 and 0.87. A true $\phi$ of about 0.95 can therefore produce an estimate near 0.90. At $\phi = 0.95$ the half-life is 13.5 quarters, twice the estimate.

**Check.** $0.90^{6.58} = 0.500$. ✓ Reverse check on value: $6.5/0.9194 = 7.0695$. ✓

**Decision consequence.** A buyer who believes the spread is "too tight" and will revert is making a forecast whose horizon depends on $\phi$. At 0.90 the reversion costs 8% of value within two years. At 0.97 it costs 3%. The two cases call for different actions: at $\phi = 0.90$, wait or bid lower; at $\phi = 0.97$, the reversion is slow enough that NOI growth may offset it. Because estimated $\phi$ is biased toward faster reversion, a mean-reversion *trade* (betting on a quick snap-back) needs a margin of safety in time as well as price: size it to survive at least twice the estimated half-life.

### Example 3.4 — Time-series momentum: sizing a listed hotel REIT position

**Given.** A listed lodging REIT index had these monthly total returns over the past 12 months: +6.3%, −3.9%, +10.2%, +2.4%, −8.1%, +4.5%, +3.6%, −1.2%, +7.8%, +2.7%, −5.4%, +3.3% [HYPOTHESIS]. You run a \$10 million liquid sleeve with a 10% annualized volatility target. Volatility is estimated from the same 12 months.

**Find.** The trailing 12-month return, annualized volatility, the TSMOM signal, and the notional position.

**Solution.**

Trailing return $= \prod(1+r_t) - 1 = 22.59\%$. (The arithmetic sum is 22.2%; compounding adds 0.4 point.)

Volatility: sample monthly standard deviation $= 5.494\%$; annualized $5.494\% \times\sqrt{12} = 19.03\%$.

Signal $= +1$. Weight $= 10\%/19.03\% = 0.5254$. Notional long $= 0.5254 \times \$10\text{ million} = \$5.25$ million.

If the same returns had the opposite sign, trailing return −21.43%, the position would be \$5.25 million short.

**Check.** Ex-ante position volatility $= 0.5254 \times 19.03\% = 10.0\%$ of the sleeve. ✓

**Decision consequence.** The momentum rule produces a number. Whether to use it depends on what the published evidence covers. Moskowitz, Ooi and Pedersen studied liquid futures, not REITs, and not private real estate. Applying their result to a single REIT index is an extrapolation [INFERENCE]. Two uses are defensible. As a *speculation*, a volatility-scaled TSMOM position is a small, diversifying sleeve with a known rule and a stop built into the signal. As an input to a *hedging* decision, the signal tells you the cost of carrying a short REIT hedge against your private hotels: you are shorting into a positive trend. That does not mean you should not hedge. A hedge is justified by the exposure, not by the signal (Chapter 1). It does mean the hedge's expected carry is negative while the trend persists. Private hotel values, which are appraisal-based, show positive autocorrelation partly because of smoothing (Chapter 2). That is a measurement artifact, not tradeable momentum.

### Example 3.5 — Regime change: durations, long-run odds, and NOI growth

**Given.** A two-state quarterly Markov model of a hotel market: expansion (state 1) with $p_{11} = 0.95$ and NOI growth $g_1 = +4\%$ per year; contraction (state 2) with $p_{22} = 0.80$ and NOI growth $g_2 = -10\%$ per year [HYPOTHESIS]. Quarterly growth is the annual figure divided by four (a simple-rate approximation).

**Find.** Expected durations; long-run probabilities; the probability of being in contraction 1–4 quarters ahead from each state; expected NOI growth over the next year from each state; the probability that a contraction already under way lasts more than 8 more quarters; the probability that an expansion lasts more than 20 more quarters.

**Solution.**

Durations: $E[D_1] = 1/(1-0.95) = 20$ quarters (5 years); $E[D_2] = 1/(1-0.80) = 5$ quarters.

Stationary: $\pi_1 = 0.20/(0.05+0.20) = 0.80$; $\pi_2 = 0.20$.

$P(\text{contraction in } k \text{ quarters})$ from $\mathbf P^k$:

| $k$ | From expansion | From contraction |
|---|---|---|
| 1 | 0.0500 | 0.8000 |
| 2 | 0.0875 | 0.6500 |
| 3 | 0.1156 | 0.5375 |
| 4 | 0.1367 | 0.4531 |

Expected NOI growth over the next four quarters, $\sum_{k=1}^4 \tfrac14[\Pr(\text{exp})g_1 + \Pr(\text{con})g_2]$:

* From expansion: average contraction probability $= (0.05+0.0875+0.1156+0.1367)/4 = 0.0975$; growth $= 0.9025 \times 4\% + 0.0975 \times (-10\%) = +2.64\%$.
* From contraction: average contraction probability $= 0.6102$; growth $= 0.3898 \times 4\% + 0.6102 \times (-10\%) = -4.54\%$.

Survival: $P(\text{contraction lasts} > 8 \text{ more quarters}) = 0.80^8 = 0.168$. $P(\text{expansion lasts} > 20 \text{ more quarters}) = 0.95^{20} = 0.358$.

**Check.** Stationarity: $0.80 \times 0.05 = 0.04 = 0.20 \times 0.20$. Flows out of each state balance. ✓

**Decision consequence.** The same hotel has a 7.2-point difference in expected first-year NOI growth depending on the regime you are in today. Regime identification is therefore worth more than refining the growth assumption within a regime. That is the link to Bayesian updating (Example 3.10): the RevPAR print in the opening problem is evidence about *which regime* you are in. For debt structuring, a 16.8% chance that a contraction runs more than two more years is the number that sizes an interest reserve or argues against a loan maturing in 24 months. The memoryless geometric duration is itself an assumption. Real downturns may have duration dependence (§3.8).

### Example 3.6 — Optionality: the value of waiting on a development parcel

**Given.** The pad site in the opening problem supports a hotel that would be worth $V_0 = \$42.0$ million if completed today (treat construction as instantaneous to isolate the option). Construction cost is $I_0 = \$40.0$ million today, rising 3% to $I_1 = \$41.2$ million next year. In one year the completed value will be $1.25 V_0 = \$52.5$ million or $0.80 V_0 = \$33.6$ million. A completed hotel yields $\delta = 6\%$ cash per year on $V_0$ (\$2.52 million), which a waiting owner forgoes. The risk-free rate is 4%.

**Find.** Static NPV (residual land value); the risk-neutral probability; the value of waiting; the option premium; a replication check.

**Solution.**

Residual land value (build now): $V_0 - I_0 = 42.0 - 40.0 = \$2.0$ million.

Risk-neutral probability:

$$q = \frac{42.0 \times 1.04 - 2.52 - 33.6}{52.5 - 33.6} = \frac{43.68 - 36.12}{18.9} = \frac{7.56}{18.9} = 0.40.$$

Payoffs from waiting: up $\max(52.5 - 41.2, 0) = 11.3$; down $\max(33.6 - 41.2, 0) = 0$.

$$W = \frac{0.40 \times 11.3 + 0.60 \times 0}{1.04} = \frac{4.52}{1.04} = \$4.346\text{ million}.$$

Option premium $= 4.346 - 2.0 = \$2.346$ million. Waiting is worth more than building.

**Check (replication).** Hold $\Delta$ units of the completed asset and a bond $B$ so that the portfolio matches the waiting payoff in both states (the asset pays its 2.52 cash yield in both):

$$\Delta = \frac{11.3 - 0}{52.5 - 33.6} = 0.59788, \qquad B = \frac{0 - 0.59788 \times (33.6 + 2.52)}{1.04} = -20.765.$$

Value $= 0.59788 \times 42.0 - 20.765 = 25.111 - 20.765 = \$4.346$ million. ✓

**Decision consequence.** The landowner's claim that residual value (\$2.0 million) is a fair price is wrong in the landowner's *favor*. The land is worth about \$4.35 million to a developer who can wait, because residual valuation assumes the build-now decision must be made today. A seller who prices land at residual is selling the option for nothing. That is a reason to buy, *if* the option is real: the entitlement must survive the wait, no competitor can pre-empt the demand, and you can carry the land. The same logic says you should not *build* on the site today even though NPV is positive. Build-now becomes optimal only when the forgone yield or cost inflation is high enough, or uncertainty low enough, that $V_0 - I_0 \ge W$ (Problem 3.6 finds the break-even yield).

### Example 3.7 — Forced selling: a margin call meets a downward-sloping demand curve

**Given.** A leveraged fund holds $Q_0 = 100$ units of a CRE bond position (think of a block of CMBS or a pool of loans financed on repo) at \$100 per unit, so the position is worth \$10,000 (\$000). Debt is $D = \$7{,}000$ (70% LTV). The lender requires LTV ≤ 75%. A market shock drops the price to $P_1 = \$92$. Buyers absorb sales along $P(s) = 92 - b s$.

**Find.** The breach; units to sell with $b = 0$ and with $b = 0.15$; post-sale price and equity; the marginal impact threshold; the feasibility threshold.

**Solution.**

After the shock: value $= 100 \times 92 = 9{,}200$; LTV $= 7{,}000/9{,}200 = 76.09\% > 75\%$. Equity has fallen from 3,000 to 2,200.

*No impact:* $s = (7{,}000/92 - 0.75 \times 100)/(1 - 0.75) = (76.087 - 75)/0.25 = 4.35$ units.

*With $b = 0.15$:* solve $(92 - 0.15s)(75 + 0.25s) = 7{,}000$. Expanding: $6{,}900 + 23s - 11.25s - 0.0375s^2 = 7{,}000$, so $0.0375s^2 - 11.75s + 100 = 0$ and

$$s = \frac{11.75 - \sqrt{11.75^2 - 4(0.0375)(100)}}{2(0.0375)} = \frac{11.75 - \sqrt{123.0625}}{0.075} = \frac{11.75 - 11.0934}{0.075} = 8.755\text{ units}.$$

Post-sale price $= 92 - 0.15 \times 8.755 = \$90.687$. Equity $= 100 \times 90.687 - 7{,}000 = \$2{,}068.7$, a further loss of \$131.3 caused purely by the fund's own selling.

Thresholds:

* Marginal: $b < (1-0.75)\times 92/(0.75 \times 100) = 23/75 = 0.3067$.
* Feasibility: $[23 + 75b]^2 = 4b(0.25)(7{,}000)$, i.e. $5{,}625 b^2 - 3{,}550 b + 529 = 0$, giving $b^\dagger = (3{,}550 - \sqrt{700{,}000})/11{,}250 = 0.2412$.

At $b = 0.30$ the marginal condition still holds (0.30 < 0.3067) but no sale cures the breach (0.30 > 0.2412). The fund is driven to full liquidation or must obtain a waiver.

**Check.** At $s = 8.755$: debt after sale $= 7{,}000 - 8.755 \times 90.687 = 6{,}206.0$; value retained $= 91.245 \times 90.687 = 8{,}274.7$; LTV $= 75.0\%$. ✓

**Decision consequence.** Price impact *doubled* the forced sale, from 4.35 to 8.76 units, and the fund's own selling cost it 6% of its remaining equity. Above $b^\dagger$, a modest-looking 8% price drop on a 70% LTV position becomes a wipe-out. The lesson for the opening problem is direct. At 65% LTV against a 70% covenant, the buffer before a forced paydown is a value decline of only $1 - 0.65/0.70 = 7.1\%$. At 55% LTV it is $1 - 0.55/0.70 = 21.4\%$. Private hotels have no continuous price, but a fresh appraisal after a soft year plays the role of $P_1$, and the paydown must be funded by selling hotels into a market where other owners face the same appraisal. A covenant buffer should be sized against the *combined* shock: the market move plus the impact of everyone's forced sales.

### Example 3.8 — Crowded trades: exit capacity versus position size

**Given.** (a) A listed hotel REIT trades \$40 million per day on average. You hold \$60 million. You will not exceed 20% of daily volume without accepting a concession. Twelve similar funds hold the stock with an aggregate \$720 million, including yours. (b) Private market: select-service hotel transaction volume in your metro averages \$450 million a year. You own \$200 million of such hotels. Above 25% of annual market volume, you expect prices to concede [HYPOTHESIS].

**Find.** Days to exit alone and when the crowd exits together; the maximum position exitable in five days alone and with a 1/12 share of capacity; years to exit the private portfolio.

**Solution.**

(a) Alone: $T = 60/(0.20 \times 40) = 7.5$ days. Crowd exiting together: $720/(0.20 \times 40) = 90$ days. Maximum position for a five-day exit alone: $40 \times 0.20 \times 5 = \$40$ million. With one-twelfth of capacity: $\$40/12 = \$3.33$ million.

(b) $T = 200/(0.25 \times 450) = 1.78$ years.

**Check.** At a one-twelfth share of capacity your \$60 million takes $60/(8/12) = 90$ days, the same as the crowd's aggregate figure. Equal shares exit together. ✓

**Decision consequence.** Liquidity measured on your own position (7.5 days) is the number you see in normal times. The relevant number in a stress is the crowd's (90 days), and you cannot observe it directly. You infer it from ownership filings, from lender conversations ("four or five other owners"), and from how similar your constraints are to theirs. Size positions so that exit time *under crowding* is shorter than the time your funding can survive a drawdown. In private CRE the arithmetic is starker: \$200 million in a \$450 million-a-year market is almost two years of disciplined selling. A fund with a maturity, covenant, or redemption inside that window is not holding a liquid position.

### Example 3.9 — Second-order consequences: rate rise → refinancing → bank lending

**Given.** First order: an office loan of \$31.2 million was made in 2021 at 65% LTV against a \$48.0 million value (NOI \$2.4 million, 5.0% cap rate), interest-only at 4.0%. At maturity, the market lends at 6.5% on 30-year amortization, with maximum 65% LTV, minimum 1.35x DSCR, and minimum 9.0% debt yield, and the cap rate is 6.25%. NOI is unchanged. Second order: a regional bank holds \$500 million of similar loans maturing over two years. Borrowers on 60% of the balance inject equity to cover their gaps. The other 40% default or extend, with expected loss of 15% of balance. The bank holds capital equal to 10% of loans. Third order: new acquisitions in the bank's markets are financed at 60% LTV [HYPOTHESIS for all inputs].

**Find.** Original DSCR; new value; maximum new loan and the binding constraint; refinancing gap; the bank's capital loss and lending-capacity reduction; the acquisitions that lose financing.

**Solution.**

*First order: the loan.*

Original DSCR $= 2{,}400{,}000/(0.04 \times 31{,}200{,}000) = 2{,}400{,}000/1{,}248{,}000 = 1.92$x.

New value $= 2{,}400{,}000/0.0625 = \$38.4$ million.

Loan constant at 6.5%, 30 years, monthly $= 0.075848$.

* LTV: $0.65 \times 38.4 = \$24.96$ million.
* DSCR: $2{,}400{,}000/1.35/0.075848 = \$23.44$ million.
* Debt yield: $2{,}400{,}000/0.09 = \$26.67$ million.

Maximum loan $= \$23.44$ million (DSCR binds). Gap $= 31.20 - 23.44 = \$7.76$ million, 24.9% of the old balance.

*Second order: the bank.*

Aggregate gap on \$500 million $= 0.2488 \times 500 = \$124.4$ million. Borrowers on \$300 million cover gaps of $0.6 \times 124.4 = \$74.6$ million, which pays down the bank's book. The remaining \$200 million produce expected losses of $0.15 \times 200 = \$30$ million. At 10% capital, lending capacity falls by $30/0.10 = \$300$ million.

*Third order: the market.*

At 60% LTV, \$300 million of loans would have financed $300/0.60 = \$500$ million of acquisitions. That demand must find another lender or disappear.

**Check.** At \$23.44 million, debt service $= 23.44 \times 0.075848 = \$1.778$ million, and $2.4/1.778 = 1.35$x. ✓

**Decision consequence.** The first-order effect of a rate rise (higher debt cost) is the one everyone models. The second-order effect, a \$30 million capital hit at one bank, removes ten times its size in lending capacity. The third-order effect is \$500 million of buyers without financing in the same markets where defaulted collateral must be sold. That is the reflexive loop of Example 3.2 running downward through the banking system. For a speculator the chain identifies *where* opportunity appears and *when*: not at the first rate rise, but when bank capital constraints bind and lenders sell loans or foreclose into a market with fewer financed bidders (Chapter 12). For an owner it says that refinancing risk is correlated across borrowers through their lenders. Your own loan's DSCR is not a sufficient statistic.

### Example 3.10 — Bayesian updating over three data points

**Given.** The opening problem's metro. Hypothesis $H$: the market has entered a supply-driven downturn. Prior $P(H) = 0.20$, from the base rate of such downturns in similar markets [HYPOTHESIS]. Three signals arrive over six weeks, assumed conditionally independent given the state:

| Signal | $P(E\mid H)$ | $P(E\mid\neg H)$ | LR |
|---|---|---|---|
| 1. Metro RevPAR −4% year over year | 0.60 | 0.20 | 3.0 |
| 2. A new 150-room hotel breaks ground nearby | 0.30 | 0.20 | 1.5 |
| 3. Group-booking pace for next year is up | 0.25 | 0.50 | 0.5 |

A hotel you are bidding on is worth \$24.0 million if $H$ is false and \$18.0 million if $H$ is true. The seller asks \$21.0 million. You require expected value to exceed the price by 5%.

**Find.** The posterior after each signal; the maximum bid; the same under over-reaction ($\omega = 2$) and under-reaction ($\omega = 0.5$).

**Solution.**

Prior odds $= 0.20/0.80 = 0.25$.

* After signal 1: odds $= 0.25 \times 3.0 = 0.75$; $P = 0.75/1.75 = 0.4286$. Check with the full form: $0.6 \times 0.2/(0.6 \times 0.2 + 0.2 \times 0.8) = 0.12/0.28 = 0.4286$. ✓
* After signal 2: odds $= 0.75 \times 1.5 = 1.125$; $P = 0.5294$.
* After signal 3: odds $= 1.125 \times 0.5 = 0.5625$; $P = 0.36$.

Expected value $= 24.0 - 6.0P$. At $P = 0.36$: $E[V] = 24.0 - 2.16 = \$21.84$ million. Maximum bid $= 21.84/1.05 = \$20.80$ million. The ask of \$21.0 million fails the test, narrowly.

Biased updaters apply $LR^\omega$:

| Updater | Posterior path | Final $P$ | $E[V]$ | Max bid | Bids at ask? |
|---|---|---|---|---|---|
| Bayesian ($\omega = 1$) | 0.429, 0.529, 0.360 | 0.360 | \$21.84m | \$20.80m | No |
| Over-reacting ($\omega = 2$) | 0.692, 0.835, 0.559 | 0.559 | \$20.65m | \$19.67m | No |
| Under-reacting ($\omega = 0.5$) | 0.302, 0.347, 0.273 | 0.273 | \$22.36m | \$21.30m | Yes |

**Check.** Order invariance: the product of LRs is $3.0 \times 1.5 \times 0.5 = 2.25$; $0.25 \times 2.25 = 0.5625$, so $P = 0.36$ whatever the order. ✓

**Decision consequence.** The disciplined bid is about \$20.8 million. The over-reactor bids \$1.1 million less and probably loses the deal. The under-reactor pays the ask, \$0.2 million above the disciplined maximum, and carries a downturn probability about a quarter too low (0.273 against 0.36). Two practical points matter more than the arithmetic. First, the LRs are themselves estimates. Writing them down *before* the data arrive is what prevents you from adjusting them to fit a conclusion. Second, independence is doubtful. If the RevPAR decline partly *reflects* new supply already open, signals 1 and 2 share information, and multiplying their LRs overstates the evidence. A conservative treatment uses only the larger of the two (LR 3.0) and gives a posterior of 0.273. The difference between 0.36 and 0.273 is the cost of not knowing the dependence structure. It is a reason to buy better data, such as the STR supply pipeline, before bidding.

---

## 3.6 CRE application: one hotel market through all the models

Return to the metro in the opening problem and assemble the pieces.

**The loop, both directions.** Suppose pledged hotel collateral in the metro is \$4,000 million, typical LTV is $\lambda = 0.65$, and each \$1 million of net demand moves prices by 0.04% ($\psi = 0.0004$ per \$ million) [HYPOTHESIS]. On the way up, owners draw half their new capacity ($\theta_{up} = 0.5$):

$$m_{up} = 0.65 \times 0.5 \times 4{,}000 \times 0.0004 = 0.52, \qquad \text{multiplier} = 1/(1-0.52) = 2.08.$$

On the way down, assume 80% of collateral sits in loans at or near the LTV covenant, so lost capacity must be repaid ($\theta_{down} = 0.8$):

$$m_{down} = 0.65 \times 0.8 \times 4{,}000 \times 0.0004 = 0.832, \qquad \text{multiplier} = 1/(1-0.832) = 5.95.$$

A 5% fundamental decline becomes a $5\% \times 5.95 = 29.8\%$ price decline, against $10.4\%$ for a 5% rise. The linear model overstates precision at that size, but the asymmetry is the point: **borrowing is optional, repayment is not.** If lenders also cut $\lambda$ after losses, $m_{down}$ rises further.

**Your fund's position in the loop.** Taking the upsize to 65% raises fund debt from \$176 million to \$208 million. A value decline $d$ breaches the 70% covenant when $0.65/(1-d) > 0.70$, i.e. $d > 7.14\%$. In the downside loop above, a fundamental shock of only $7.14\%/5.95 = 1.2\%$ is enough to push values past that point. At 55% LTV the breach requires $d > 21.4\%$, a fundamental shock of $21.4\%/5.95 = 3.6\%$. Neither is comfortable. The upsize roughly triples your sensitivity to a shock that, by Example 3.10, now has a posterior probability of about one in three.

**The regime question.** Under Example 3.5's parameters, a breach is most likely in a contraction, which lasts five quarters on average and more than two years with probability 0.168. A covenant cure that requires selling hotels in that window means selling into the crowded exit of Example 3.8.

**The land.** The option to wait on the pad site (Example 3.6) is worth more, not less, in the same environment. Higher uncertainty raises the value of waiting, and the landowner is pricing at residual. The two decisions point in opposite directions: be *less* levered on the operating portfolio, and *more* willing to own an option whose cost is small and whose downside is limited to the premium paid.

**The opportunity cost.** The \$32 million the upsize would release must beat the risk-matched hurdle of Example 3.1 *after* adding the cost of the extra covenant risk to the existing \$320 million portfolio. A deal that would earn 11% on \$32 million but adds a 1-in-10 chance of a forced \$30 million paydown at a 15% discount does not clear it. Problem 3.10 asks you to put numbers on that trade-off.

---

## 3.7 Feedback loops in general

A feedback loop exists when the output of a process changes its own input. Classify every loop you meet by **sign**, **gain**, and **lag**.

| Loop | Sign | Typical gain driver | Lag | CRE example |
|---|---|---|---|---|
| Collateral → credit → price | Positive | LTV, draw rate, market depth | Appraisal cycle (months) | Example 3.2; Japan, §3.9 |
| Margin call → forced sale → price | Positive | Leverage, price impact | Days (securities) to quarters (private) | Example 3.7 |
| Rent → supply → rent | Negative | Development elasticity | Construction (2–4 years) | §3.4.10 cobweb |
| Price → valuation-based fees and marks → fundraising → demand | Positive | Investor return chasing | Fundraising cycle | Open-end fund inflows and redemptions |
| Defaults → bank capital → lending → price | Positive | Capital ratio | Quarters | Example 3.9 |

Positive loops with short lags produce crashes. Negative loops with long lags produce oscillations. The worst environments combine a positive credit loop with a negative supply loop that arrives late: credit inflates prices, prices call forth supply, and the supply arrives just as credit reverses.

---

## 3.8 When the relationships fail

1. **Opportunity cost with no true alternative.** The risk-matched hurdle assumes the alternative can be levered at $r_B$ and that volatility captures risk. Neither holds for illiquid, fat-tailed positions. The hurdle is then a floor, and judgment must add a premium.
2. **Reflexive loops are not constant-gain.** $\lambda$, $\theta$, and $\psi$ change with the state of the market, especially near turning points. Loop gains estimated in a boom understate the bust. The Kiyotaki–Moore amplification result is itself disputed: a re-examination argues that the original model shows strong amplification only for some parameter settings [FACT: ch03-S02 notes].
3. **Mean reversion fails when the mean moves.** A spread "reverts" to a mean that is a property of the sample. After a structural break (a change in the inflation regime, in bank regulation, or in demand for a property type), the old mean is irrelevant. Post-2020 office is the obvious example (Chapter 23). Estimated $\phi$ is also biased toward faster reversion in short samples.
4. **Momentum fails at turning points.** Trend rules lose money in reversals, and the reported evidence partly reflects volatility scaling. Momentum evidence from liquid futures does not transfer to appraisal-based private indices.
5. **Regime models assume memorylessness.** The geometric duration implies that a regime is no more likely to end after eight quarters than after one. Real cycles may have duration dependence, and parameters estimated on a few regime switches are imprecise. With only three or four observed contractions, $p_{22}$ is barely identified.
6. **Optionality can be illusory.** The option to wait is worth nothing if the entitlement expires, a competitor takes the demand, or carrying costs are high. It is worth less if you cannot actually observe the value signal you would wait for.
7. **Forced-selling models omit the counterparty.** A lender may waive rather than force a sale when it expects fire-sale losses itself. Extend-and-pretend is a real-world response that the covenant arithmetic ignores. It postpones the loop without removing it.
8. **Crowding is unobservable in advance.** Exit capacity depends on others' positions and constraints, which are mostly private. Overlap estimates from filings are lagged and incomplete.
9. **Bayesian updating fails with bad likelihoods.** Correct arithmetic on wrong or dependent LRs gives confidently wrong posteriors. A prior from the wrong reference class does the same.

---

## 3.9 Historical episode: Japan's land and stock bubble, 1985–1992

**Date and environment.** The yen appreciated sharply after the Plaza Accord of September 1985 and Japan entered a slowdown. The Bank of Japan cut its official discount rate five times between January 1986 and February 1987 to offset the strong-yen recession, reaching 2.5%, then a postwar low. It held the rate at 2.5% for about two years and three months, until May 1989 [FACT: Okina, Shirakawa and Shiratsuka (2001), Bank of Japan IMES; ch03-S03, VERIFIED-SECONDARY via search excerpts of the paper]. The rate was then raised in steps to 6.0% by August 1990 [FACT: same source].

**Prices.** The Nikkei 225 closed at a record 38,915.87 on 29 December 1989 [FACT: ch03-S12, contemporary news reports of the 2024 record that cite the 1989 close]. It reached 14,309 in August 1992 [FACT: ch03-S13, secondary press reports; class C source], a decline of $1 - 14{,}309/38{,}915.87 = 63.2\%$. Commercial land prices in Japan's six largest cities, as measured by the Japan Real Estate Institute's urban land price index, peaked in September 1990 at almost four times their September 1985 level [FACT: ch03-S03, as reported in the Bank of Japan IMES study; VERIFIED-SECONDARY]. Secondary sources report declines in big-city commercial land prices of 70% to more than 80% from the peak by the early-to-mid 2000s, depending on the end point *(verification pending: exact figure against the JREI series)*.

**Financing and the collateral loop.** Japanese bank lending relied heavily on real estate collateral. As land prices rose, borrowing capacity rose with them [INFERENCE: the collateral mechanism is the subject of ch03-S02 and ch03-S14; Kanaya and Woo (2000) describe deregulation leading banks to take more risk, including increased lending to real estate, ch03-S15]. Gan (2007) uses the collapse of Japanese land prices as a natural experiment. Firms that lost more collateral value borrowed less and invested less, and they were less likely to keep their banking relationships. In the working-paper version, a 10% fall in collateral value reduced the average manufacturing firm's investment rate by about 0.8 percentage point [FACT: ch03-S14, VERIFIED-SECONDARY from the abstract and working-paper summary]. That is direct evidence for the downward leg of the loop in §3.4.2: falling collateral values reduced borrowing capacity and real activity.

**The policy catalyst.** In 1990 the Ministry of Finance issued administrative guidance limiting the growth of banks' total lending to real estate (the *sōryō kisei*, "total volume restriction") [FACT: ch03-S16 (IMF working paper) and ch03-S17; sources date it to March or April 1990, likely the difference between notice and effective date]. Loans to nonbanks were exempted, and lending through nonbanks, including the *jusen* housing-loan companies, grew rapidly in 1990–91 [FACT: ch03-S16]. The date on which the restriction was lifted is *(verification pending)*.

**What was knowable at the time.** Rising land prices, the low policy rate, rapid real-estate lending, and the reliance on land collateral were all public [INFERENCE: these are the variables the official studies document from contemporaneous data]. Commentators argued at the time about whether land prices reflected fundamentals. What could not be known was the loop gain: how much of the price level was supported by credit that would reverse. Okina, Shirakawa and Shiratsuka describe "intensified bullish expectations" as central to the episode [FACT: ch03-S03 abstract]. That is the cognitive half of Soros's loop.

**Competing interpretations.**

* *Monetary policy.* The discount rate was held at 2.5% for more than two years after the recovery began, and raised only as asset prices peaked. This view assigns the boom to cheap money and the bust to tightening [INFERENCE drawn from the documented rate path].
* *Financial deregulation and bank behavior.* Large firms moved to capital markets, and banks moved toward real estate and smaller borrowers with weaker risk control (Kanaya and Woo, 2000) [FACT that this interpretation is advanced: ch03-S15].
* *Expectations.* Extrapolative beliefs about land prices drove demand independent of rates [INFERENCE consistent with ch03-S03].
* *Regulatory catalyst.* The 1990 lending restriction cut $\lambda$ for new real-estate credit at the peak and helped start the downward loop [INFERENCE; the relative contributions of rate hikes and the restriction are disputed].

These interpretations are complementary rather than exclusive. In the loop model, cheap money and deregulation raised $\lambda$ and $\theta$, expectations raised $\theta$, and the restriction plus rate rises reversed them.

**What the episode establishes.** It establishes that a credit system built on real-estate collateral transmits land-price declines into lending and investment (Gan's evidence). It shows that a policy that cuts real-estate credit at a market peak can coincide with a long decline. And it shows that a nonbank channel left outside the restriction can absorb the displaced credit for a time.

**What it does not establish.** It does not establish the loop gain for any other market. It does not show that the bubble could have been identified in real time with enough confidence to time it. It does not separate the causal roles of monetary policy, the lending restriction, and expectations. And it does not imply that every rapid land-price rise ends this way.

**CRE connection.** Every element has a modern analog: appraisal-based LTV lending (the collateral loop), administrative guidance on CRE concentrations (a change in $\lambda$), lending migrating to private credit funds outside bank regulation (the nonbank channel), and owners who all upsized against the same appraisals (crowding). LTCM in 1998, the trading-desk version of the forced-selling loop, is treated in Chapter 23.

---

## 3.10 Decision exercise: the upsize, the land, and the bid

Return to the opening problem. Using the numbers developed in this chapter, write a decision record on `desk/investment_memos/decision_record_template.md` that answers:

1. **The upsize.** Accept, decline, or accept a smaller amount. State the covenant buffer under each choice (Example 3.7: 7.1% at 65%, 21.4% at 55%). State the fundamental shock that would trigger a breach given a downside loop multiplier (§3.6), and your posterior probability of a downturn (Example 3.10).
2. **Use of proceeds.** If you take any cash, state the risk-matched hurdle it must clear (Example 3.1). State the exit capacity of what you would buy (Example 3.8).
3. **The land.** Your maximum price for the pad site and the conditions under which the option to wait is real: entitlement life, carrying cost, competing sites.
4. **The bid on the hotel.** Your maximum bid and how it changes if signals 1 and 2 are not independent.
5. **Invalidation.** Name the data that would reverse each decision, such as group pace, STR supply pipeline, or lender behavior.
6. **Abstention.** Whether any of the three is better left alone, and why.

**Rubric.** Full credit requires:

* (a) the covenant buffer computed and compared with a plausible downside, not just with the base case;
* (b) explicit recognition that other owners' upsizes raise the market's loop gain and crowd your exit;
* (c) the land valued as an option, with the option's real-world conditions checked;
* (d) a bid that follows from a stated prior and stated LRs, with the dependence problem addressed;
* (e) the do-nothing alternative evaluated with numbers.

A strong answer declines or shrinks the upsize, considers the land at a price between residual and option value conditional on entitlement life, and bids at or below about \$20.8 million or waits for the supply data. Reasonable answers can differ on the land and the bid. An answer that accepts the full upsize to buy more hotels in the same metro must explain why the crowding and covenant arithmetic do not apply.

---

## 3.11 Frequent analytical errors

1. **Using the unlevered alternative as the hurdle for a levered deal.** Lever the alternative to the deal's risk first (Example 3.1).
2. **Calling a market "reflexive" without a gain.** Name $\lambda$, $\theta$, $\psi$, and the sign of the loop. Estimate $m$.
3. **Assuming symmetric feedback.** Borrowing is optional, repayment is forced: $\theta_{down} > \theta_{up}$.
4. **Quoting a half-life in the wrong period.** A quarterly $\phi$ gives a half-life in quarters.
5. **Trusting estimated $\phi$ near one.** Small-sample bias shortens the half-life, and $H$ is hypersensitive to $\phi$ near one.
6. **Confusing momentum with mean reversion, or with smoothing.** Appraisal-based autocorrelation is not a tradeable trend.
7. **Forecasting with the regime-average growth rate.** Expected growth depends on the current regime. Identifying the regime is worth more than refining growth within it.
8. **Valuing land at residual.** Residual value ignores the option to wait and understates land value when uncertainty is high.
9. **Sizing a covenant buffer to the market move only.** Add the impact of your own and others' forced sales.
10. **Measuring liquidity on your own position.** Exit capacity in a stress is shared with everyone holding the same trade.
11. **Multiplying likelihood ratios of correlated signals.** This double-counts evidence and causes over-reaction.
12. **Updating without writing down the prior.** Without a recorded prior and LRs, hindsight will rewrite both.

---

## 3.12 Connections to other chapters

* Chapter 1: break-even probabilities and immediacy are the static versions of this chapter's dynamic models. Leverage and ruin connect to forced selling.
* Chapter 2: appraisal smoothing creates spurious momentum in private indices and lags the collateral loop.
* Chapter 5: monetary policy sets $r_B$ and shifts lenders' $\lambda$.
* Chapter 10: loan sizing, covenants, and refinancing gaps (Example 3.9) in full.
* Chapter 12: maturity walls and loan sales are where the second-order chain produces opportunity.
* Chapter 13: real options in hold/sell/develop decisions extend Example 3.6.
* Chapter 18: convexity and option pricing in continuous time.
* Chapter 20: Bayesian inference, base rates, and calibration in depth.
* Chapter 21: margin, liquidity stress, and sizing for survival.
* Chapter 23: Japan 1990s, LTCM 1998, and 2007–09 as full historical cases.

---

## 3.13 One-page reference sheet

| Model | Formula | Decision use |
|---|---|---|
| Risk-matched hurdle | $h = r_B + (\sigma_D/\sigma_A)(r_A - r_B)$ | Reject deals below the alternative at equal risk |
| Loop gain | $m = \lambda\theta C\psi$ | Stable iff $m<1$ |
| Loop total | $X_\infty = x_0/(1-m)$; $X_n = x_0(1-m^n)/(1-m)$ | Size stress tests to the multiplier |
| AR(1) forecast | $E[x_{t+h}] = \mu + \phi^h(x_t-\mu)$ | Reversion path |
| Half-life | $H = \ln 0.5/\ln\phi$; quarterly $\to$ annual: $\phi^4$ | Time margin for reversion trades |
| TSMOM weight | $w = \operatorname{sign}(R_{12})\,\sigma^*/\sigma$ | Volatility-targeted trend sizing |
| Regime duration | $1/(1-p_{ii})$; $P(D>d) = p_{ii}^d$ | Loan maturity and reserve sizing |
| Stationary probability | $\pi_1 = (1-p_{22})/[(1-p_{11})+(1-p_{22})]$ | Long-run base rate |
| Risk-neutral $q$ | $q = [V_0(1+r_f) - \delta V_0 - dV_0]/(uV_0 - dV_0)$ | Option to wait |
| Wait value | $W = [q f_u + (1-q) f_d]/(1+r_f)$ | Build only if $V_0 - I_0 \ge W$ |
| Forced sale | $P(s)[\lambda^*Q_0 + (1-\lambda^*)s] = D$ | Units to sell |
| Impact thresholds | Marginal $b < (1-\lambda^*)P_1/(\lambda^*Q_0)$; feasible $b < b^\dagger$ | Spiral risk |
| Covenant buffer | $d^* = 1 - \lambda_0/\lambda^*$ | Value decline before breach |
| Exit time | $T = X/(\rho\, ADV)$, crowd: $\sum X_j/(\rho\, ADV)$ | Position limits |
| Bayes (odds) | posterior odds = prior odds × $\prod LR_k$ | Sequential updating |
| Biased updating | $LR^\omega$; $\omega>1$ over-, $\omega<1$ under-reaction | Bias audit |

**Questions before any position.** What is my next-best alternative at equal risk? Which loop am I in, and what is its gain in both directions? How fast does this deviation decay, and how sure am I of $\phi$? Which regime am I in, and how long does it last? What option am I buying or selling? Who else must sell when I must? What would each new data point have to look like to change my mind, and by how much?

---

## References for this chapter

Source IDs and verification status are in `references/sources_ch03.md`.

* Barberis, N., Shleifer, A., and Vishny, R. (1998). "A Model of Investor Sentiment." *Journal of Financial Economics*, 49(3), 307–343.
* Brunnermeier, M. K., and Pedersen, L. H. (2009). "Market Liquidity and Funding Liquidity." *Review of Financial Studies*, 22(6), 2201–2238.
* Dixit, A. K., and Pindyck, R. S. (1994). *Investment under Uncertainty*. Princeton University Press.
* Gan, J. (2007). "Collateral, Debt Capacity, and Corporate Investment: Evidence from a Natural Experiment." *Journal of Financial Economics*, 85(3), 709–734.
* Hamilton, J. D. (1989). "A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle." *Econometrica*, 57(2), 357–384.
* Kanaya, A., and Woo, D. (2000). "The Japanese Banking Crisis of the 1990s: Sources and Lessons." IMF Working Paper WP/00/7.
* Kendall, M. G. (1954). "Note on Bias in the Estimation of Autocorrelation." *Biometrika*, 41(3–4), 403–404.
* Kiyotaki, N., and Moore, J. (1997). "Credit Cycles." *Journal of Political Economy*, 105(2), 211–248.
* Moskowitz, T. J., Ooi, Y. H., and Pedersen, L. H. (2012). "Time Series Momentum." *Journal of Financial Economics*, 104(2), 228–250.
* Okina, K., Shirakawa, M., and Shiratsuka, S. (2001). "The Asset Price Bubble and Monetary Policy: Japan's Experience in the Late 1980s and the Lessons." *Monetary and Economic Studies*, 19(S1), 395–450. Bank of Japan, Institute for Monetary and Economic Studies.
* Shleifer, A., and Vishny, R. W. (1992). "Liquidation Values and Debt Capacity: A Market Equilibrium Approach." *Journal of Finance*, 47(4), 1343–1366.
* Soros, G. (1987). *The Alchemy of Finance*. New York: Simon & Schuster.
* Titman, S. (1985). "Urban Land Prices under Uncertainty." *American Economic Review*, 75(3), 505–514.
* IMF (1993). "Japanese Banks and the Asset Price 'Bubble'." IMF Working Paper 93/85.
