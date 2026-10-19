# Chapter 18 — Derivatives, Volatility, and Convexity

> **Status:** Complete (v1.0). Numerical examples are reproduced in `tests/test_ch18_examples.py`. Problems are in `problems/questions/ch18_problems.md` and solutions in `problems/solutions/ch18_solutions.md`. Sources are listed in `references/sources_ch18.md`. New library module: `models/python/sdesk/x_derivatives.py`. It extends `sdesk.markets` and reuses `sdesk.x_capital_structure` (Chapter 10) for Bachelier caps. Drills D164–D170. Pending items: the exact VIX closing levels for 2 and 5 February 2018, and the XIV redemption amount, both marked *(verification pending)* in §18.9. Neither is used in any calculation.

## Learning objectives

After this chapter you should be able to:

1. Price forwards and swaps by replication, explain how futures differ through daily settlement, and say who bears counterparty, margin and basis risk in each contract.
2. Derive put–call parity from a static replication argument, then use it to find mispriced quotes and synthetic positions.
3. Derive the Black–Scholes equation from a delta-hedged portfolio. Compute delta, gamma, vega and theta with `sdesk.markets` and `sdesk.x_derivatives`, and use the identity $\Theta + \tfrac12\sigma^2S^2\Gamma = r(V - S\Delta)$ to explain where option P&L comes from.
4. Separate **implied** from **realized** volatility. Show, in theory and with a seeded simulation, that a delta-hedged option earns approximately $\sum \tfrac12\Gamma_i S_i^2(\sigma_{real}^2 - \sigma_{impl}^2)\Delta t$, and explain why the result depends on the path.
5. Price tail hedges, including the cumulative cost of carrying puts for years, and decide when insurance is worth its premium.
6. Value a fixed-for-floating interest-rate swap, its DV01, and the termination payment a CRE borrower faces on an early sale.
7. Price an interest-rate cap on a floating-rate CRE loan as a strip of caplets, and show how its cost responds to the strike, volatility and model (normal versus lognormal).
8. Treat sponsor equity as a call on the property and the lender's position as riskless debt minus a put, and use that to explain asset substitution, extension fights and covenant design.

---

## 18.1 Opening investment problem: three derivative decisions in one week

You run the markets book for a family office that also owns hotels. All facts below are [HYPOTHESIS], a constructed teaching case.

**Decision A: the cap on a hotel loan.** The office is closing on a full-service hotel for \$60.0 million. The lender is providing a \$45.0 million, three-year floating-rate loan at SOFR + 3.75%, interest-only, with quarterly payments. Underwritten NOI after the FF&E reserve is \$5.2 million. The term sheet requires an interest-rate cap for the full initial term, struck so that DSCR at the strike is at least 1.40x. The forward SOFR curve is roughly flat at 3.60%. A dealer quotes caps using a normal volatility of about 100 bp. Your asset manager asks two questions. Should we buy the minimum-compliant strike or something tighter? And is \$180,000 "a lot" for a cap?

**Decision B: the tail hedge.** The office also holds a \$50 million portfolio of listed equities and REITs. After a strong year, the investment committee wants "crash protection". A bank offers rolling three-month index puts struck 10% out of the money, at about 24% implied volatility. The CIO asks what the program will cost over a decade, and what it will actually pay.

**Decision C: the yield product.** A manager pitches a "volatility-income" fund. It sells one-month index puts, has returned about 1% per month for two years, and has "never had a down quarter". The sales deck shows a Sharpe ratio above 3.

These are one problem seen from three sides. In each case someone is buying or selling **convexity**: a payoff that is curved in the underlying. The cap buyer and the put buyer pay a premium for curvature. The volatility-income fund collects that premium and is short the curvature. By §18.10 you will be able to price each position, say what risk is being transferred, and decide which, if any, to accept.

---

## 18.2 Economic intuition

### Linear and non-linear claims

A **forward**, **future** or **swap** is linear in the underlying. If the price moves by \$1, the position gains or loses a fixed amount, up or down. These contracts move risk from one party to another at no upfront cost, apart from margin. The fair forward price is not a forecast. It is the price at which carrying the underlying, financed at the risk-free rate, replicates the contract (§18.4.1).

An **option** is non-linear. The holder has a right, not an obligation, so losses are truncated and the payoff bends. The bend is called **convexity** and, locally, **gamma**. Convexity cannot be created for free. The buyer pays a premium, and in a delta-hedged position that premium is paid continuously through **theta**, the decay in the option's value as time passes. The option holder is paid only if the underlying moves enough. "Enough" is set by the volatility implied in the price.

That is the central idea of the chapter. **An option is a bet on realized volatility against implied volatility, with the exposure weighted by gamma along the path.** Direction matters only through the hedge you do or do not run.

### Insurance, and who supplies it

Buying an option is buying insurance. A floating-rate borrower buying a cap insures debt service. An equity holder buying a put insures against a crash. As in property-casualty insurance, the policy pays when it is most valuable: in states of the world where marginal wealth is scarce. Investors pay for that state-contingent payment. Over long periods, implied volatility on equity indices has tended to exceed subsequently realized volatility, a gap called the **variance risk premium**. *[HYPOTHESIS for this chapter: the sign and rough size of the index variance risk premium are established in academic literature not reviewed here; Chapter 22 will source it. No number in this chapter depends on it.]*

The seller of insurance earns the premium in most periods and pays out rarely and heavily. The distribution of returns to selling options has a high median, a modest mean and a severe left tail. A short sample is dominated by the median, so it looks excellent. This is the statistical structure behind Decision C and behind the February 2018 episode (§18.9).

### Hedging changes the risk; it does not remove it

A hedge exchanges one risk for another:

* A **futures hedge** turns price risk into **basis risk**, the risk that the hedge and the exposure diverge, and into **margin risk**, the need to post cash daily on the hedge while the hedged asset's offsetting gain is unrealized or illiquid.
* An **OTC swap or cap** adds **counterparty risk**, the chance that the party owing you money on the hedge cannot pay when the hedge is most valuable.
* A **delta hedge** of an option turns directional risk into **volatility and path risk**.

None of these is a reason to avoid hedging. Each is a reason to state, before the trade, which risk is left.

### The CRE capital structure is already an option book

Chapter 10 showed that non-recourse debt makes the sponsor's equity a call on the property and the lender's claim riskless debt minus a put. This chapter supplies the pricing machinery. It also points to a consequence. The sponsor is **long volatility**, and the lender is **short volatility**. Anything that raises the volatility of the property's value, such as a riskier business plan, higher leverage or a shorter cap, transfers value from lender to sponsor even if expected NOI is unchanged (Example 18.9).

---

## 18.3 Technical definitions

| Term | Definition |
|---|---|
| Forward | Bilateral agreement to buy or sell at a fixed price $K$ at date $T$. No cash at inception if struck at the fair forward price. Counterparty risk throughout |
| Futures | Exchange-traded forward with daily mark-to-market (variation margin) through a clearing house. Counterparty risk is replaced by margin (liquidity) risk |
| Swap | Exchange of cash-flow streams; a fixed-for-floating interest-rate swap exchanges a fixed rate for a floating index on a notional |
| Call / put | Right to buy / sell at strike $K$. European: exercisable only at $T$. American: at any time up to $T$ |
| Payoff | Call: $\max(S_T - K, 0)$. Put: $\max(K - S_T, 0)$ |
| Moneyness | $K/S$ or $K/F$. A put is out of the money (OTM) when $K < S$ |
| Intrinsic / time value | Intrinsic = immediate exercise value. Time value = price − intrinsic |
| Delta $\Delta$ | $\partial V/\partial S$ |
| Gamma $\Gamma$ | $\partial^2 V/\partial S^2$ |
| Vega $\nu$ | $\partial V/\partial \sigma$, quoted here per 1 vol point (0.01) unless stated |
| Theta $\Theta$ | $\partial V/\partial t$ in calendar time, per year in formulas and per day (÷365) in examples |
| Implied volatility $\sigma_{impl}$ | The $\sigma$ that makes the model price equal the market price |
| Realized volatility $\sigma_{real}$ | Annualized standard deviation of observed log returns. This chapter uses the zero-mean estimator $\sqrt{(252/n)\sum r_i^2}$ unless stated |
| Skew / smile | Variation of implied volatility across strikes. For equity indices, low-strike puts trade at higher implied vol than at-the-money options |
| Caplet | Call on a floating rate: pays $N\tau\max(L - K, 0)$ at the end of the accrual period |
| Cap | Strip of caplets covering successive periods |
| Normal (Bachelier) vol $\sigma_N$ | Standard deviation of the rate's change, in rate units per $\sqrt{\text{year}}$ (0.01 = 100 bp) |
| Lognormal (Black) vol $\sigma_{LN}$ | Standard deviation of the log of the rate, per $\sqrt{\text{year}}$. Roughly $\sigma_N \approx \sigma_{LN} F$ near the money |
| DV01 | Value change for a 1 bp parallel move in rates |
| Basis | $b = S - F$, spot minus futures (or exposure minus hedge, in general) |
| Variation / initial margin | Daily cash settlement of futures gains and losses / collateral posted to open a position |
| Credit valuation adjustment (CVA) | Price reduction for the counterparty's default risk on an OTC derivative |

---

## 18.4 Equations and derivations

Throughout this section, $r$ and the dividend or cash yield $q$ are continuously compounded, and time is in years.

### 18.4.1 Forwards by replication

Borrow $Se^{-qT}$ at rate $r$, buy $e^{-qT}$ units of the asset, and reinvest the dividends in the asset. At $T$ you hold one unit and owe $Se^{(r-q)T}$. This replicates a long forward, so the fair forward price is

$$F_0 = S_0 e^{(r-q)T}.$$

A forward struck earlier at $K$ is worth, to the long,

$$f = S_0e^{-qT} - Ke^{-rT}.$$

The forward price contains no forecast of $S_T$. It is the arithmetic of carry. For a commodity, $q$ is a convenience yield net of storage. For a property, $q$ would be the NOI yield, which is why forward property prices (where they exist, e.g. on index swaps) sit below spot when cap rates exceed financing rates.

**Futures versus forwards.** With deterministic interest rates the futures price equals the forward price (Cox, Ingersoll and Ross, 1981). When the underlying is positively correlated with interest rates, the long futures holder receives variation margin when rates are high and pays it when rates are low. That is an advantage, so futures prices exceed forward prices. For short-term interest-rate futures the effect is a **convexity adjustment**: the futures-implied rate is above the forward rate, by an amount that grows with rate volatility and roughly with the square of maturity. Chapter 6's forward rates are forward rates. Do not read them off futures without the adjustment for maturities beyond a year or two.

### 18.4.2 Put–call parity

Consider two portfolios. Portfolio 1: one European call plus a zero-coupon bond paying $K$ at $T$. Portfolio 2: one European put plus $e^{-qT}$ units of the asset with dividends reinvested. At $T$ both are worth $\max(S_T, K)$. With no arbitrage they cost the same today:

$$C - P = S_0 e^{-qT} - K e^{-rT}.$$

The right-hand side is the value of a forward struck at $K$. So **a long call plus a short put at the same strike is a synthetic forward**, and any one of the four instruments can be synthesized from the other three. The identity holds for European options regardless of the model or the volatility. It fails, or holds only as an inequality, for American options, for underlyings that are hard to borrow, and when the financing rate available to you differs from $r$. `sdesk.markets.put_call_parity_gap` returns $C - P - (Se^{-qT} - Ke^{-rT})$.

### 18.4.3 The Black–Scholes equation from a hedged portfolio

Assume the asset follows geometric Brownian motion, $dS = \mu S\,dt + \sigma S\,dW$, and let $V(S,t)$ be the value of an option. Itô's lemma gives

$$dV = \left(V_t + \mu S V_S + \tfrac12\sigma^2S^2V_{SS}\right)dt + \sigma S V_S\,dW.$$

Hold the option and short $\Delta$ units of the asset, $\Pi = V - \Delta S$, receiving the dividend yield on the short leg's cost. Then

$$d\Pi = dV - \Delta\,dS - q\Delta S\,dt.$$

Choose $\Delta = V_S$. The $dW$ terms cancel and $\mu$ drops out:

$$d\Pi = \left(V_t + \tfrac12\sigma^2S^2V_{SS} - q S V_S\right)dt.$$

The portfolio is riskless over $dt$, so it must earn $r$: $d\Pi = r(V - SV_S)\,dt$. Rearranging gives the Black–Scholes–Merton equation:

$$V_t + (r-q)SV_S + \tfrac12\sigma^2S^2V_{SS} - rV = 0.$$

In Greek notation:

$$\boxed{\Theta + (r-q)S\Delta + \tfrac12\sigma^2S^2\Gamma = rV.}$$

Set $r=q=0$ and this becomes $\Theta = -\tfrac12\sigma^2S^2\Gamma$. **Theta is the rent paid for gamma.** A long-gamma position loses value through time at exactly the rate that makes it break even when the asset moves by one implied standard deviation.

The solution with terminal condition $\max(S_T-K,0)$ is the discounted risk-neutral expectation $C = e^{-rT}E^{\mathbb Q}[\max(S_T-K,0)]$, where under $\mathbb Q$, $\ln S_T \sim N(\ln S_0 + (r-q-\tfrac12\sigma^2)T,\ \sigma^2T)$. Splitting the expectation into $E[S_T\mathbf 1_{S_T>K}] - K\,\mathbb Q(S_T>K)$ and completing the square in the first term gives

$$C = S_0e^{-qT}N(d_1) - Ke^{-rT}N(d_2),\quad d_1 = \frac{\ln(S_0/K) + (r-q+\tfrac12\sigma^2)T}{\sigma\sqrt T},\quad d_2 = d_1 - \sigma\sqrt T.$$

$N(d_2)$ is the risk-neutral probability that the call finishes in the money. $N(d_1)e^{-qT}$ is the call's delta. The put follows from parity. These are `sdesk.markets.bs_price` and `bs_delta`.

### 18.4.4 The Greeks

With $\phi$ the standard normal density:

| Greek | Call | Put | Library |
|---|---|---|---|
| $\Delta$ | $e^{-qT}N(d_1)$ | $e^{-qT}[N(d_1)-1]$ | `markets.bs_delta` |
| $\Gamma$ | $e^{-qT}\phi(d_1)/(S\sigma\sqrt T)$ | same | `markets.bs_gamma` |
| $\nu$ (per 1.00 of $\sigma$) | $Se^{-qT}\phi(d_1)\sqrt T$ | same | `markets.bs_vega` (÷100 per vol point) |
| $\Theta$ (per year) | $-\frac{Se^{-qT}\phi(d_1)\sigma}{2\sqrt T} - rKe^{-rT}N(d_2) + qSe^{-qT}N(d_1)$ | $-\frac{Se^{-qT}\phi(d_1)\sigma}{2\sqrt T} + rKe^{-rT}N(-d_2) - qSe^{-qT}N(-d_1)$ | `x_derivatives.bs_theta` |

Two relations are worth knowing by heart.

**Vega–gamma.** From the table, $\nu = \sigma T S^2\Gamma$. An option with high gamma per unit of $S^2$ also has high vega, scaled by time. Short-dated options are gamma instruments. Long-dated options are vega instruments.

**Delta–gamma–vega expansion.** For a small move $\delta S$ and a change in implied vol $\delta\sigma$ over a short interval $\delta t$,

$$\delta V \approx \Delta\,\delta S + \tfrac12\Gamma(\delta S)^2 + \nu\,\delta\sigma + \Theta\,\delta t.$$

`markets.delta_gamma_pnl` returns the first two terms. For large moves the expansion fails, because gamma itself changes with $S$ (Example 18.2).

### 18.4.5 The P&L of a delta-hedged option

This is the derivation that matters most for a speculator. Buy an option at implied vol $\sigma_i$ and hedge it at the Black–Scholes delta computed at $\sigma_i$. The asset actually moves with volatility $\sigma_r$. Take $q=0$ for clarity. The hedged, self-financing position earns over $dt$:

$$d\Pi = dV - \Delta\,dS - r(V - \Delta S)\,dt.$$

Because $V$ is the Black–Scholes value at $\sigma_i$, it satisfies the PDE at $\sigma_i$:

$$\Theta = rV - rS\Delta - \tfrac12\sigma_i^2S^2\Gamma.$$

Itô's lemma under the *true* dynamics gives $dV = \Theta\,dt + \Delta\,dS + \tfrac12\Gamma\,(dS)^2$, with $(dS)^2 = \sigma_r^2S^2dt$. Substituting:

$$d\Pi = \tfrac12\Gamma\left[(dS)^2 - \sigma_i^2S^2dt\right] = \tfrac12\Gamma S^2\left(\sigma_r^2 - \sigma_i^2\right)dt.$$

Summed over discrete hedge dates $t_i$, with step $\Delta t$:

$$\boxed{\text{Hedged P\&L} \approx \sum_i \tfrac12\Gamma_i S_i^2\left[\left(\frac{\Delta S_i}{S_i}\right)^2 - \sigma_i^2\Delta t\right] \;\xrightarrow{E}\; \sum_i \tfrac12\Gamma_i S_i^2\left(\sigma_r^2 - \sigma_i^2\right)\Delta t.}$$

Four consequences follow.

1. **Direction does not matter. Size of moves does.** A long option hedged in this way makes money whenever the squared return over a step exceeds $\sigma_i^2\Delta t$, whatever its sign. The daily **break-even move** is $\sigma_i/\sqrt{252}$. At 16 vol it is about 1% a day.
2. **The P&L is gamma-weighted, so it is path-dependent.** Realized variance earned near the strike, close to expiry, where $\Gamma S^2$ is large, counts for much more than the same variance earned far from the strike. Two paths with identical realized volatility can produce different P&L.
3. **Discrete hedging adds noise, not bias.** Between hedge dates the squared return is a random draw, so P&L has a standard deviation that shrinks roughly with $1/\sqrt n$ for $n$ re-hedges. Its expectation is unaffected to first order.
4. **A first-order shortcut.** If $\Gamma S^2$ were constant, then using $\nu = \sigma_iTS^2\Gamma$ gives $\text{P\&L} \approx \nu(\sigma_r^2 - \sigma_i^2)/(2\sigma_i) \approx \nu(\sigma_r - \sigma_i)$. This is the desk rule "vega times the vol difference". It is an approximation that ignores consequence 2.

Ahmad and Wilmott (2005) analyze the alternative choice of hedging at the *realized* volatility. That choice locks in a deterministic profit equal to the value difference $V(\sigma_r) - V(\sigma_i)$, but the mark-to-market path is then volatile. The speculator cannot know $\sigma_r$ in advance, so in practice implied-vol hedging, with its path dependence, is the usual case.

### 18.4.6 Interest-rate swaps

Let $P_j$ be discount factors to payment dates $t_1,\dots,t_n$, with accruals $\tau_j$. The forward rate for period $j$ satisfies $1 + \tau_jL_j = P_{j-1}/P_j$, with $P_0 = 1$ on a reset date. The floating leg's value telescopes:

$$\sum_j N\tau_jL_jP_j = N\sum_j(P_{j-1} - P_j) = N(1 - P_n).$$

This is the familiar statement that a floating-rate note resets to par. The fixed leg is $NK\sum_j\tau_jP_j = NK\,A$, where $A$ is the **annuity factor**. The par swap rate sets the two equal:

$$K_{par} = \frac{1 - P_n}{A}.$$

The value to the pay-fixed party is $N(1-P_n) - NKA = NA(K_{par} - K)$. **A pay-fixed swap gains when rates rise and loses when they fall, by roughly DV01 per bp, where DV01 ≈ $NA \times 0.0001$.** Between resets, with the next floating coupon already fixed at $L$, the floating leg is $N(1+\tau_1L)P_1 - NP_n$. `x_derivatives.swap_value` implements both cases.

### 18.4.7 Caplets: normal and lognormal

A caplet on rate $L$, fixing at $T$, paying at $T + \tau$, is worth $N\tau P(T+\tau)\,E[\max(L_T - K, 0)]$ under the payment-date forward measure, under which $L$ is a martingale with mean $F$.

**Normal (Bachelier).** If $L_T \sim N(F, \sigma_N^2T)$, write $s = \sigma_N\sqrt T$ and $d = (F-K)/s$. Then

$$E[(L_T - K)^+] = \int_{-d}^{\infty}(F - K + sz)\phi(z)\,dz = (F-K)N(d) + s\,\phi(d).$$

This is `x_capital_structure.bachelier_caplet`, already used in Chapter 10.

**Lognormal (Black, 1976).** If $\ln L_T \sim N(\ln F - \tfrac12\sigma_{LN}^2T,\ \sigma_{LN}^2T)$, the same calculation as Black–Scholes with zero carry gives

$$E[(L_T-K)^+] = FN(d_1) - KN(d_2),\qquad d_{1,2} = \frac{\ln(F/K) \pm \tfrac12\sigma_{LN}^2T}{\sigma_{LN}\sqrt T}.$$

This is `x_derivatives.black_caplet`. The two models agree near the money when $\sigma_N \approx \sigma_{LN}F$. They disagree away from the money. The lognormal distribution has a fatter right tail, so it prices high-strike caps more expensively and low-strike floors more cheaply. Neither is "correct". Dealers quote a vol smile in whichever convention they use, and the smile encodes the market's view of the rate distribution. If you price every strike with one flat vol in either model, you are imposing a distribution, not observing one.

**Cap vega.** Differentiating the Bachelier formula with respect to $\sigma_N$ gives $N\tau P\sqrt T\phi(d)$ per caplet. It is largest for at-the-money caplets with long fixing times.

### 18.4.8 Hedge ratios with basis risk

Let $\delta S$ be the change in the exposure's value and $\delta F$ the change in the futures price. Choose $h$ to minimize $\mathrm{Var}(\delta S - h\,\delta F)$:

$$h^* = \rho\frac{\sigma_S}{\sigma_F},\qquad \text{variance removed} = \rho^2,\qquad \sigma_{resid} = \sigma_S\sqrt{1-\rho^2}.$$

Number of contracts $= h^*\times(\text{exposure value})/(F\times\text{multiplier})$. A hedge with $\rho = 0.75$ removes only 56% of variance. Basis risk is not a footnote; it is most of the residual risk.

### 18.4.9 The structural (Merton) model of a mortgage

Let the property be worth $V$, with log-value volatility $\sigma_V$. Let the loan require a single payment $B$ at $T$. At $T$ the sponsor repays if $V_T > B$ and otherwise surrenders the property (non-recourse). So

$$E_T = \max(V_T - B, 0),\qquad D_T = \min(V_T, B) = B - \max(B - V_T, 0).$$

Today, $E = C(V, B, T, \sigma_V)$ and $D = Be^{-rT} - P(V, B, T, \sigma_V)$, with $E + D = V$. The credit spread is $s = -\ln(D/B)/T - r$. Two derivatives give the incentive structure:

$$\frac{\partial E}{\partial\sigma_V} = \nu_{call} > 0,\qquad \frac{\partial D}{\partial \sigma_V} = -\nu_{put} = -\nu_{call} < 0.$$

Raising asset volatility moves value from lender to sponsor dollar for dollar. This is **asset substitution** (Jensen and Meckling, 1976). It is strongest when the loan is near the money, which in CRE means near maturity and near a covenant breach. `x_derivatives.merton_claims` implements this model.

---

## 18.5 Worked examples

All inputs are [HYPOTHESIS] unless cited. Every number is reproduced in `tests/test_ch18_examples.py`.

### Example 18.1 — Put–call parity, a synthetic forward, and a quote that looks wrong

**Given.** An equity index at $S = 5{,}000$. Six-month European options ($T = 0.5$), strike $K = 5{,}000$. Risk-free rate $r = 4.00\%$, dividend yield $q = 1.50\%$, both continuous. Mid quotes: call 280.00, put 230.00. The executable quotes are call ask 281.00 and put bid 229.00.

**Find.** The parity value of $C - P$; the fair forward price; the mispricing at mid and at executable prices; the trade that captures it.

**Solution.**

$Se^{-qT} = 5{,}000e^{-0.0075} = 4{,}962.64$. $Ke^{-rT} = 5{,}000e^{-0.02} = 4{,}900.99$.

Parity value: $C - P = 4{,}962.64 - 4{,}900.99 = 61.65$.

Fair forward: $F = 5{,}000e^{(0.04-0.015)\times0.5} = 5{,}000e^{0.0125} = 5{,}062.89$.

Quoted at mid: $C - P = 50.00$. Gap $= 50.00 - 61.65 = -11.65$. The call is cheap relative to the put.

The trade is a **reversal**: buy the call, sell the put, and sell the forward (or short the index basket and invest the proceeds). The synthetic long forward costs $C - P$, against 61.65 of fair value. At executable prices, $C - P = 281.00 - 229.00 = 52.00$. The locked-in gain is $61.65 - 52.00 = 9.65$ index points per unit, before the cost of the short leg.

**Check.** At 18% implied volatility, Black–Scholes gives $C = 282.28$ and $P = 220.64$. The difference is 61.65, the parity value, as it must be for any volatility.

**Decision consequence.** Parity violations of this size in a liquid index are almost always an artifact. Likely causes are stale quotes, a dividend assumption that differs from the market's, a borrow cost on the short basket (which raises the effective $q$), or a funding rate above $r$. Solve parity for the implied dividend yield before trading. The practical use of parity for a CRE investor is different. It is the tool for reading options as forwards plus insurance. A long call is a synthetic long forward plus a put. That is exactly the sponsor's position in a levered property (Example 18.9).

### Example 18.2 — Pricing and Greeks of a protective put; where the Taylor expansion fails

**Given.** Index $S = 100$, three-month put ($T = 0.25$) struck at $K = 90$, $r = 4.00\%$, $q = 0$, implied volatility $\sigma = 22\%$.

**Find.** The price, delta, gamma, vega (per vol point) and theta (per day). Then estimate the value change for: (a) a 10-point fall with vol unchanged; (b) a 10-point fall with implied vol rising to 30%; (c) a 5-point fall; (d) a 5-point rise. Compare the delta, delta-gamma and delta-gamma-vega approximations with full repricing.

**Solution.**

$d_1 = [\ln(100/90) + (0.04 + 0.0242)\times0.25]/(0.22\times0.5) = (0.10536 + 0.01605)/0.11 = 1.1037$; $d_2 = 0.9937$.

| Quantity | Value |
|---|---|
| Put price | 0.7870 |
| Delta | −0.1349 |
| Gamma | 0.01972 |
| Vega per vol point | 0.1085 |
| Theta per day | −0.01151 |

Scenario P&L per unit:

| Scenario | Full reprice | Delta only | Delta + gamma | Delta + gamma + vega |
|---|---|---|---|---|
| (a) $\delta S = -10$, vol 22% | +2.7094 | +1.3485 | +2.3347 | +2.3347 |
| (b) $\delta S = -10$, vol 30% | +4.1310 | +1.3485 | +2.3347 | +3.2026 |
| (c) $\delta S = -5$ | +0.9679 | +0.6743 | +0.9208 | +0.9208 |
| (d) $\delta S = +5$ | −0.4700 | −0.6743 | −0.4277 | −0.4277 |

Full repricing gives new put values of 3.4963 in (a), 4.9180 in (b), 1.7549 in (c) and 0.3170 in (d).

The vega term in (b) is $\nu\,\delta\sigma = 10.848\times0.08 = 0.8678$ (vega per 1.00 of vol is 10.848).

**Check.** Theta and gamma satisfy the PDE: $\Theta_{yr} + rS\Delta + \tfrac12\sigma^2S^2\Gamma - rV = -4.2022 - 0.5394 + 4.7731 - 0.0315 = 0.0000$ (to rounding). `test_example_18_2` verifies the identity to $10^{-10}$.

**Decision consequence.** The put costs 0.79% of the index for three months. It decays at about 1.2 basis points of the index a day, and faster as expiry approaches. In the scenario it is bought for, a crash with a vol spike, its value rises more than fivefold, and more than half of that gain comes from the vol term, not from delta. Two lessons follow for anyone using Greeks to risk-manage a book. First, the delta-gamma expansion understates the gain in (a) by 0.37, because gamma rises as the put moves toward the money while the second-order term uses the starting gamma. In (d) it understates the loss. A put's gamma is itself convex in $S$ on this side of the strike. Second, and more important, in a crash the hedge's value depends on implied vol, which is a market price, not a parameter. Run stress tests by full repricing with a vol shock linked to the spot shock. Never use a Greek-based approximation alone for a tail scenario.


### Example 18.3 — Implied versus realized volatility, and the daily break-even move

**Given.** A one-month at-the-money call ($S = K = 100$, $T = 1/12$, $r = 4.00\%$, $q = 0$) trades at 2.60. Over the following ten trading days the simple daily returns are: +1.2%, −0.8%, +0.4%, −1.5%, +0.9%, +0.2%, −1.1%, +0.6%, −0.3%, +1.0%.

**Find.** (a) Implied volatility. (b) The daily break-even move. (c) Realized volatility over the ten days with the zero-mean estimator, and with the sample standard deviation. (d) Whether a delta-hedged long position is earning or losing its theta.

**Solution.**

(a) Solve $\text{BS}(100, 100, 1/12, 0.04, \sigma) = 2.60$ by bisection: $\sigma_{impl} = 21.14\%$.

(b) Break-even daily move $= 0.2114/\sqrt{252} = 1.332\%$.

(c) Log returns $\ln(1+r_i)$. Zero-mean estimator: $\sqrt{(252/10)\sum \ln(1+r_i)^2} = 14.21\%$. Sample standard deviation (mean removed, $n-1$ divisor), annualized by $\sqrt{252}$: 14.95%.

(d) Only one of ten days (−1.5%) exceeded the break-even move in absolute size. Realized vol of about 14% against 21% implied means the long-gamma position is losing. To first order, its theta exceeds its gamma income in the ratio $\sigma_i^2/\sigma_r^2 \approx (0.2114/0.1421)^2 = 2.2$.

**Check.** A move of exactly $\sigma/\sqrt{252}$ every day produces a realized vol equal to $\sigma$, so the hedged long-gamma position breaks even on every day. ✓

**Decision consequence.** Implied vol is a price. Realized vol is an outcome. The trade is the spread between them. Ten days is a tiny sample. The standard error of a variance estimate from $n$ normal observations is about $\sqrt{2/n}$ of the variance, which is about 45% at $n=10$. A seller who sees ten quiet days has learned little about the next ten. Note also that the two estimators differ by about 0.7 vol points here. Variance swaps and most desk P&L attribution use the zero-mean version. When you compare your realized vol with someone else's, agree the estimator first.

### Example 18.4 — Discrete delta hedging: the gamma P&L identity in a seeded simulation

**Given.** Buy a three-month at-the-money call ($S_0 = K = 100$, $T = 0.25$) at $\sigma_{impl} = 20\%$, with $r = 4.00\%$, $q = 0$. Re-hedge to the implied-vol delta 63 times (about daily). The stock follows geometric Brownian motion with zero drift and true volatility $\sigma_r$. Random numbers come from `random.Random(18).gauss(0, 1)`. Run $\sigma_r$ = 25%, 20% and 15%. Then repeat over seeds 1–400 with 13, 63 and 252 re-hedges. Code: `x_derivatives.delta_hedge_simulation`.

**Find.** For seed 18: the hedged P&L, the gamma decomposition $\sum\tfrac12\Gamma_iS_i^2[(\Delta S_i/S_i)^2 - \sigma_i^2\Delta t]$, and the "theory" sum $\sum\tfrac12\Gamma_iS_i^2(\sigma_r^2 - \sigma_i^2)\Delta t$. Across seeds: the mean and standard deviation of P&L.

**Solution.** The premium is $C = 4.4852$. Vega is 19.724 per 1.00 of vol, or 0.1972 per vol point.

Seed 18, 63 re-hedges:

| $\sigma_r$ | Path realized vol | Hedged P&L | Gamma decomposition | Theory sum ($\sigma_r$ known) |
|---|---|---|---|---|
| 25% | 24.03% | +1.0289 | +0.9914 | +1.7223 |
| 20% | 19.22% | −0.4736 | −0.4956 | 0.0000 |
| 15% | 14.41% | −1.7954 | −1.7731 | −1.4722 |

Across seeds 1–400:

| $\sigma_r$ | Re-hedges | Mean P&L | Std. dev. of P&L | Mean theory sum |
|---|---|---|---|---|
| 25% | 13 | +1.0595 | 1.2978 | +1.0094 |
| 25% | 63 | +1.0468 | 0.6768 | +1.0214 |
| 25% | 252 | +1.0255 | 0.5248 | +1.0135 |
| 20% | 13 | +0.0360 | 0.9795 | 0.0000 |
| 20% | 63 | +0.0188 | 0.4433 | 0.0000 |
| 20% | 252 | +0.0067 | 0.2251 | 0.0000 |
| 15% | 13 | −0.9860 | 0.7907 | −0.9906 |
| 15% | 63 | −0.9998 | 0.4685 | −1.0091 |
| 15% | 252 | −1.0015 | 0.3727 | −1.0035 |

**Reading the results.**

1. **The identity works path by path.** On seed 18 the gamma decomposition, built from realized squared returns, explains the hedged P&L to within 0.04, or about 4% of the P&L. The residual comes from third-order terms and from the fact that theta and gamma are evaluated at the start of each step.
2. **The expectation is right, the single path is not.** On seed 18 the "theory" sum (+1.72) is far from the realized P&L (+1.03), even though the path's realized vol (24.0%) is close to 25%. The path spent much of its life away from the strike, where gamma is small. Across 400 paths the mean P&L (+1.02 to +1.06) matches the mean theory sum (+1.01 to +1.02).
3. **The vega shortcut is close but biased.** $\nu(\sigma_r - \sigma_i) = 19.724\times0.05 = 0.986$. That is a little below the simulated mean of about 1.03. The alternative form $\nu(\sigma_r^2 - \sigma_i^2)/(2\sigma_i) = 19.724\times0.05625 = 1.109$ is above it. The truth lies between, because $\Gamma S^2$ is not constant.
4. **Hedge frequency reduces dispersion, not the mean.** When $\sigma_r = \sigma_i = 20\%$, the standard deviation of P&L falls from 0.98 to 0.44 to 0.23 as re-hedging goes from weekly to daily to four times a day. That is close to $1/\sqrt n$ scaling (each fourfold increase roughly halves it). The mean stays close to zero.

**Check.** At $\sigma_r = \sigma_i$, the theory sum is exactly zero by construction, and the simulated mean P&L at 252 re-hedges is +0.0067 with a standard error of $0.2251/\sqrt{400} = 0.011$. That is consistent with zero. ✓

**Decision consequence.** A volatility position is not "long vol" in the abstract. It is long **gamma-weighted realized variance** against a price fixed today, and it can lose money on a path that realizes more volatility than was implied if the movement happens in the wrong place. Before buying options as a volatility view, write down where you expect the realized variance to occur relative to the strike and in time. Before selling options for income, recognize that daily hedging does not change the expected loss when realized vol exceeds implied. It only makes the path less noisy. Hedging frequency is a cost–noise trade-off. More re-hedges reduce variance but each one pays a bid–ask spread (Chapter 2), which this simulation ignores.

### Example 18.5 — The tail hedge: what it costs to carry puts for a decade

**Given.** A \$50,000,000 equity portfolio with the same return as the index. The hedge buys three-month index puts struck 10% below spot, rolled each quarter. Implied vol for the 90% strike is 24% (above the at-the-money level because of skew). $r = 4.00\%$ and $q = 1.50\%$. Assume the same relative strike, vol and rates at each roll, a steady-state estimate. Alternative: a put spread, buying the 90% put and selling the 75% put at 30% implied vol.

**Find.** (a) The premium per roll and the annual cost. (b) The cumulative drag over ten years if nothing is ever recovered. (c) The payoff if the index falls 30% within a quarter, measured at expiry. (d) The break-even frequency of such a crash. (e) The cost and payoff of the put spread. (f) The cost of the same 90% put if bought at 30% vol, after a scare.

**Solution.**

(a) Put price (per 100 of spot) $= \text{BS}_{put}(100, 90, 0.25, 0.04, 0.24, q=0.015) = 1.0730$, or 1.073% of the hedged value per quarter. Four rolls a year: annual cost $= 4.292\%$, or \$2,146,067 a year on \$50 million.

(b) Ten-year multiplicative drag with no payoffs: $(1 - 0.04292)^{10} = 0.645$, a 35.5% cumulative reduction relative to the unhedged portfolio.

(c) A 30% fall: payoff $= (0.90 - 0.70)\times\$50{,}000{,}000 = \$10{,}000{,}000$.

(d) Break-even frequency $= 2{,}146{,}067/10{,}000{,}000 = 0.215$ a year, or one such crash every 4.7 years. A 20% fall pays $(0.90 - 0.80)\times\$50\text{m} = \$5\text{m}$ and would need to happen every 2.3 years.

(e) The 75% put at 30% vol costs 0.1217 per 100. Spread cost per roll $= 1.0730 - 0.1217 = 0.9513$, or 3.805% a year. The spread pays at most $(0.90 - 0.75) = 15\%$, or \$7,500,000. The spread saves 0.49% a year (11% of the cost) and gives up 25% of the payoff in a 30% crash.

(f) The 90% put at 30% vol costs 1.8698 per roll, or 7.479% a year. That is 74% more than at 24%.

**Check.** The 90% put at 18% implied, roughly at-the-money vol in a calm market, costs 0.4376. Skew alone, from 18% to 24%, multiplies the cost of the 10%-OTM put by about 2.5. The insurance is priced on the vol at its own strike, not on the headline vol.

**Decision consequence.** A rolling OTM put program is a commitment to pay about 4% a year, roughly the equity risk premium many investors assume *[HYPOTHESIS: no source cited for the premium's size]*, for a payoff that arrives irregularly and only for large, fast declines. A 30% decline spread over 18 months pays nothing on a quarterly 90% put that keeps being re-struck lower. Before buying, compare it with the alternatives that cost less in expectation: (i) lower gross exposure, which reduces the loss in every crash at the cost of the risk premium on the exposure removed; (ii) holding cash or Treasuries as dry powder, which earns $r$ rather than paying theta; (iii) put spreads or longer-dated puts, which have lower theta per unit of time. Tail hedges earn their cost when the investor has a **liability or forced action** in the crash state, such as a margin loan, a redemption queue or a loan covenant. For an investor with no forced action in a crash, the cheaper hedge is usually to hold less risk. Buy insurance after a scare (f) and you pay up to 74% more for the same strike.

### Example 18.6 — A futures hedge with basis risk and a margin call

**Given.** A fund holds \$40,000,000 of listed REIT shares and wants to hedge equity-market risk for three months with E-mini S&P 500 futures. The contract multiplier is \$50 per index point [FACT: CME contract specification; ch18-S09, VERIFIED-SECONDARY]. The index future is at 5,000 [HYPOTHESIS]. Over the hedge horizon the REIT portfolio's annualized vol is 24% and the future's is 17%, with correlation 0.75 [HYPOTHESIS]. The fund keeps \$3,000,000 of cash for margin.

**Find.** (a) The minimum-variance hedge ratio and the number of contracts. (b) Hedge effectiveness and residual vol. (c) The variation margin if the index rallies 6% (300 points) in the first week. (d) The outcome if, in that same week, REITs fall 2% on a rate shock.

**Solution.**

(a) $h^* = 0.75\times0.24/0.17 = 1.0588$. Contracts $= 1.0588\times40{,}000{,}000/(5{,}000\times50) = 169.4$. Round to 169 contracts, a notional of \$42,250,000.

(b) Effectiveness $= \rho^2 = 56.25\%$ of variance. Residual vol $= 0.24\sqrt{1 - 0.5625} = 15.87\%$, against 24% unhedged. The hedge removes about a third of the standard deviation, not all of it.

(c) Variation margin $= 169\times\$50\times300 = \$2{,}535{,}000$, payable in cash within a day.

(d) REITs fall 2%: −\$800,000 on the shares. The hedge loses \$2,535,000. Total: −\$3,335,000. The \$3,000,000 cash buffer is exhausted.

**Check.** Dimensional check: contracts = (dimensionless ratio × \$)/(index points × \$/point) = number of contracts. ✓

**Decision consequence.** The hedge is designed against the market factor. It does nothing about the rate factor that drives REITs independently of the broad index, and in (d) both legs lose. The margin call arrives in cash, immediately, while any offsetting gain on the shares would be unrealized. A hedger with an illiquid or unrealized offset is short liquidity. This is the Metallgesellschaft lesson discussed in Chapter 1: a hedge can be economically sound and still force liquidation through funding. A CRE owner hedging a property with listed instruments faces the extreme case. The property's offsetting gain cannot be pledged for margin at all. Size the margin buffer to a stress move in the hedge instrument, not to the expected move. Here a 10% rally needs \$4.2 million, more than the buffer.

### Example 18.7 — Valuing a pay-fixed swap, its DV01, and the breakage on an early sale

**Given.** A borrower swaps a \$45,000,000 floating-rate loan to fixed for three years with annual payments (accrual 1.0). Zero rates, annually compounded: 4.00% (1 year), 3.80% (2 years), 3.70% (3 years). The swap is struck at par at inception. Immediately afterwards, all zero rates fall 100 bp in parallel.

**Find.** (a) The discount factors and the par swap rate. (b) The swap's value to the borrower after the 100 bp fall. (c) The DV01 at inception. (d) The value after a 100 bp rise. (e) What happens if the borrower sells the hotel and repays the loan at that point.

**Solution.**

(a) $P_1 = 1/1.04 = 0.961538$; $P_2 = 1/1.038^2 = 0.928122$; $P_3 = 1/1.037^3 = 0.896734$. Annuity $A = 2.786395$. Par rate $K = (1 - 0.896734)/2.786395 = 3.7061\%$.

(b) New zeros 3.00%, 2.80%, 2.70%. New annuity $A' = 2.840326$. New par rate $= 2.7044\%$. Floating leg $= 45{,}000{,}000\times(1 - P_3') = \$3{,}456{,}682$. Fixed leg $= 45{,}000{,}000\times0.037061\times2.840326 = \$4{,}736{,}903$. Value to pay-fixed $= -\$1{,}280{,}221$.

Shortcut: $NA'(K_{par}' - K) = 45{,}000{,}000\times2.840326\times(0.027044 - 0.037061) = -\$1{,}280{,}221$. ✓

(c) DV01: value after a +1 bp shift $= +\$12{,}557$. Approximately $NA\times0.0001 = 45{,}000{,}000\times2.7864\times0.0001 = \$12{,}539$; the difference comes from the change in annuity.

(d) +100 bp: value $= +\$1{,}232{,}353$. The asymmetry against (b), \$1.28 million versus \$1.23 million, is convexity. The annuity rises when rates fall.

(e) The swap does not disappear when the loan is repaid. The borrower must terminate it at market value, paying about \$1.28 million in scenario (b) or receiving about \$1.23 million in (d), plus the dealer's bid–offer.

**Check.** At inception the swap value is zero at $K = K_{par}$. `test_example_18_7` confirms this to the cent.

**Decision consequence.** A swap converts floating debt into fixed debt and creates a **mark-to-market liability that crystallizes on any early exit**. Rates often fall in recessions, which is also when a sale or a refinancing might be forced. In that state the borrower owes the swap breakage on top of the loan. A cap has no such liability: the buyer's maximum loss is the premium. Pay-fixed swaps also create a two-way counterparty relationship. When rates fall, the bank is exposed to the borrower's credit, which is why bank swaps on CRE loans are typically secured by the same mortgage *[HYPOTHESIS: common practice, not sourced here]*. When rates rise, the borrower is exposed to the bank. Choose a swap when the hold period is certain and long, and a cap when the exit date is uncertain. Business plans for value-add hotels usually fall in the second category.

### Example 18.8 — CRE application: pricing the hotel loan's rate cap as a strip of caplets

**Given (Decision A).** Notional \$45,000,000. Three-year cap with quarterly caplets. The first period is already fixed, so caplets 2–12 fix at $t = 0.25, \dots, 2.75$. Flat forward SOFR $F = 3.60\%$, discounting at the same flat forward compounded quarterly (the Chapter 10 convention in `x_capital_structure.cap_premium`). Normal vol 1.00% (100 bp). NOI \$5,200,000. Spread 3.75%. Required DSCR at the strike: 1.40x.

**Find.** (a) The maximum strike allowed by the DSCR covenant. (b) The cap premium at that strike, as \$, % of notional, and annual bp equivalent. (c) A premium grid across strikes (3.50–5.00%) and vols (0.70–1.30%). (d) Vega per 10 bp. (e) The premium under the Black lognormal model at $\sigma_{LN} = \sigma_N/F$, for strikes 3.50%, 4.50% and 5.50%. (f) The premium at a 4.50% strike if, at the replacement date, the forward is 4.75%.

**Solution.**

(a) $DSCR = NOI/[N(K + s)] \ge 1.40 \Rightarrow K \le 5{,}200{,}000/(1.40\times45{,}000{,}000) - 0.0375 = 0.08254 - 0.0375 = 4.504\%$. Use $K = 4.50\%$. DSCR at the strike $= 5{,}200{,}000/(45{,}000{,}000\times0.0825) = 1.4007$x.

(b) Using `xc.cap_premium(45e6, 0.045, 0.036, 0.010, 3)`: premium **\$183,583**, 0.408% of notional. The annuity factor is 2.8316, so the annual equivalent is $0.004080/2.8316 = 14.4$ bp a year. The eleven caplets rise from \$789 (fixing at 0.25 years) to \$30,984 (fixing at 2.75 years), because $\sqrt T$ drives time value when the strike is 90 bp out of the money.

(c) Premium grid (\$):

| Strike \ normal vol | 0.70% | 1.00% | 1.30% |
|---|---|---|---|
| 3.50% | 438,698 | 599,445 | 760,636 |
| 4.00% | 194,604 | 342,061 | 495,787 |
| 4.50% | 76,738 | 183,583 | 311,046 |
| 5.00% | 27,110 | 93,525 | 189,122 |

At 1.00% vol, annual equivalents are 47.0, 26.8, 14.4 and 7.3 bp for the four strikes.

(d) Raising vol from 1.00% to 1.10% adds \$40,808 to the 4.50% cap, an increase of 22%. The cap's vega relative to its price is high because it is out of the money.

(e) Black, $\sigma_{LN} = 0.010/0.036 = 27.78\%$:

| Strike | Bachelier (\$) | Black (\$) | Black / Bachelier |
|---|---|---|---|
| 3.50% | 599,445 | 589,046 | 0.98 |
| 4.50% | 183,583 | 230,168 | 1.25 |
| 5.50% | 45,115 | 95,497 | 2.12 |

(f) Forward 4.75%, strike 4.50%, vol 1.00%: premium \$683,477, 3.7 times the original. Most of the increase is intrinsic value: each caplet is 25 bp in the money.

**Check.** The 3.50% strike is only 10 bp in the money. Its intrinsic value is $45{,}000{,}000\times0.0010\times\sum_{j=2}^{12}0.25P_j = \$116{,}274$, about a fifth of the \$599,445 premium. Time value supplies the rest, because 10 bp is small relative to $\sigma_N\sqrt T$ (up to 166 bp for the last caplet). Lower strikes pay off in more states and cost more. The grid is monotone in both strike and vol. ✓

**Decision consequence.** At 14.4 bp a year the minimum-compliant cap is cheap relative to the 3.75% spread. But the price is not the useful question. The useful questions are these:

* **What does the cap protect?** It protects debt service above 4.50% SOFR. At SOFR of 6.00%, unhedged DSCR would be 1.19x, and capped DSCR stays at 1.40x.
* **What does a tighter strike buy?** Moving from 4.50% to 4.00% costs \$158,478 more and caps the all-in rate 50 bp lower. On \$45 million that is \$225,000 a year of protection, but only in states where SOFR exceeds 4.00%.
* **Model and smile risk.** For strikes above the forward the lognormal model charges much more, at the same at-the-money vol (e). The dealer's quote encodes a smile. Ask for the quote at your strike, and do not extrapolate from an at-the-money vol.
* **The replacement problem.** The loan's extension options will need a new cap. If forwards rise above the strike before then (f), the replacement costs several times more, almost all of it intrinsic value. This is the Chapter 10 squeeze. The cap's term should match the realistic hold, including extensions, or the cash for a replacement should be reserved at closing.

### Example 18.9 — Sponsor equity as a call, the lender as short a put

**Given.** The hotel is worth $V = \$60{,}000{,}000$. Treat the loan as a single \$45,000,000 balloon due in three years. Interest paid from NOI is ignored on both sides, so both claims are claims on terminal value only [HYPOTHESIS: a standard simplification, discussed in §18.7]. $r = 4.00\%$. Asset vol: 12% for the current business plan (stabilized operations), 18% for a repositioning, 25% for an aggressive conversion. Second case: after a downturn, $V = \$48{,}000{,}000$.

**Find.** Equity value, the lender's put, debt value, risk-neutral default probability $N(-d_2)$, and the credit spread under each plan, in both cases.

**Solution.** Using `x_derivatives.merton_claims`. Riskless PV of the balloon $= 45{,}000{,}000e^{-0.12} = \$39{,}911{,}420$.

$V = \$60.0$ million:

| $\sigma_V$ | Equity (call) | Lender's put | Debt | PD (risk-neutral) | Spread (bp) |
|---|---|---|---|---|---|
| 12% | 20,183,873 | 95,292 | 39,816,127 | 3.16% | 8.0 |
| 18% | 20,766,248 | 677,668 | 39,233,752 | 12.47% | 57.1 |
| 25% | 22,031,108 | 1,942,527 | 37,968,892 | 23.42% | 166.3 |

$V = \$48.0$ million:

| $\sigma_V$ | Equity (call) | Lender's put | Debt | PD (risk-neutral) | Spread (bp) |
|---|---|---|---|---|---|
| 12% | 9,019,661 | 931,080 | 38,980,339 | 21.65% | 78.7 |
| 18% | 10,405,572 | 2,316,991 | 37,594,428 | 33.14% | 199.4 |
| 25% | 12,239,830 | 4,151,250 | 35,760,170 | 41.70% | 366.1 |

**Check.** In every row, equity + debt = $V$ to the dollar, and equity − put = $V - Be^{-rT} = \$20{,}088{,}580$ (at \$60m). This is put–call parity, with the property as the underlying. ✓

**Decision consequence.** Moving from the stabilized plan to the aggressive conversion transfers \$1.85 million from the lender to the sponsor when $V = \$60$ million, and \$3.22 million when $V = \$48$ million. Expected NOI does not have to change for this to happen. The transfer is larger when the equity is closer to the money. That is when the sponsor's incentive to "swing for the fences" is strongest, and when the lender most needs covenants: limits on change of use, capex approval rights, cash management triggers, and maturity tests. Note that this model **overstates** sponsor value in one respect. Real CRE equity is not a European call. The lender can foreclose at a covenant breach, so the sponsor holds a call with a knock-out barrier, and its time value is less than shown. Example 10.8 computed the same option with a three-state tree. The continuous model is more general, but its inputs, especially $\sigma_V$ for an asset that has no traded price, are judgment calls (Chapter 2 on appraisal smoothing).

---

## 18.6 CRE application: a derivatives policy for a floating-rate hotel portfolio

Examples 18.7–18.9 combine into a policy that a CRE owner can write down. The reader should treat it as a template to adapt, not as a rule.

**1. Match the hedge to the uncertain exit.** Hotel business plans have uncertain holds, so the default instrument is a **cap**, not a swap (Example 18.7). The cap's maximum cost is its premium. A swap's breakage is a contingent liability that peaks when rates fall, which is often when the exit is forced.

**2. Choose the strike from the cash-flow stress, not the covenant.** The covenant sets the *maximum* strike (Example 18.8a). The right strike is the rate at which the property's cash flow, after reserves, still covers debt service in a moderate NOI downturn. For a hotel, NOI can fall 20–30% in a mild recession *[HYPOTHESIS: Chapter 11 develops hotel operating leverage]*. Compute DSCR at the strike on stressed NOI. If it is below 1.0x, either buy a lower strike or hold a debt-service reserve, and compare the costs.

**3. Price the replacement, not just the cap.** The extension options will need new caps. Value the expected replacement cost under a range of forwards (Example 18.8f). The vol and strike sensitivities in the grid tell you how much to reserve.

**4. Know the vega you are long.** A cap is long rate volatility. Buying it after a volatility shock is expensive (the 1.30% column of the grid is 69% more than the 1.00% column at the 4.50% strike). If the loan closes on a fixed date, the cap must be bought then. There is no option to wait. If the purchase date is flexible, for example a cap required only on a future extension, the timing of the purchase is itself a volatility trade.

**5. Counterparty.** The cap buyer is a creditor of the cap seller for the life of the cap, and the exposure is largest when rates are high. Loan documents usually set a minimum rating for the cap provider and require replacement on a downgrade *[HYPOTHESIS: common term-sheet practice, not sourced here]*. A replacement after a provider downgrade happens at market prices, which may be high.

**6. Read the capital structure as options.** The sponsor is long a call (Example 18.9) and the cap is a call on rates. Together, the sponsor's equity is long volatility in two places: property values and, through the cap, rates. The lender is short property volatility and is protected from rate volatility only to the extent that the cap is in place and the counterparty pays. A rescue investor or a note buyer should write down the full option position of each party before negotiating (Chapter 10, §10.8).

---

## 18.7 When the relationship fails

1. **Volatility is not constant, and it is correlated with the price.** Black–Scholes assumes a constant $\sigma$. Equity index vol rises when prices fall, so delta computed at a constant vol underhedges puts in a decline. The implied vol skew is the market's correction for this. Hedging a skewed book with flat-vol deltas leaves a residual directional exposure.
2. **Jumps defeat continuous hedging.** The P&L identity of §18.4.5 needs $(dS)^2 = \sigma^2S^2dt$. A gap move between hedge dates, such as an overnight crash or a rate decision, produces a P&L of $\tfrac12\Gamma(\delta S)^2$ on a large $\delta S$, with no chance to re-hedge. Short-gamma positions are exposed to exactly this.
3. **Liquidity disappears when hedges need to trade.** Dynamic hedging assumes you can trade the underlying at the model price. In October 1987, portfolio insurers' sell orders arrived when liquidity providers had withdrawn (Chapter 1, §1.9). In February 2018, volatility ETPs had to buy VIX futures into a spike (§18.9). Model hedging cost is a lower bound.
4. **Put–call parity can fail in funding stress.** When the arbitrageur cannot borrow at $r$, or the short leg cannot be borrowed, the parity band widens. The "arbitrage" in Example 18.1 is only available to someone with balance sheet.
5. **The basis can move against both legs.** Example 18.6 showed a hedge that loses while the hedged asset also loses. Correlations estimated in calm markets are an unreliable guide in stress.
6. **Normal and lognormal rate models give different answers away from the money.** Example 18.8e: at a 5.50% strike the two models differ by a factor of two at the same at-the-money vol. A cap price quoted on one model's flat vol is a statement about the tail of the rate distribution.
7. **The Merton model is a stylized picture of a mortgage.** Real loans have coupons, amortization, covenants that allow early foreclosure, extension options, recourse carve-outs and costly default. The property's value is not observed continuously, and its "volatility" is an estimate distorted by appraisal smoothing (Chapter 2). Use the model for direction and order of magnitude, as in Example 18.9, not to price a specific note.
8. **Counterparty risk is wrong-way risk.** A cap provider owes the most when rates are highest, which is also when financial-sector stress is likely. A put seller owes the most in a crash. Insurance is only as good as the insurer in the state you are insuring against.
9. **Margin rules change.** Clearing houses raise initial margin in volatile markets. A hedge that was funded at the old margin may need more cash exactly when the hedger is short of it.

---

## 18.8 Path dependency, convexity and leveraged products

Three senses of "path dependency" appear in this chapter. They are easy to confuse.

**The hedged-option P&L is path-dependent** (§18.4.5, Example 18.4). The payoff of the European option itself depends only on $S_T$, but the hedger's P&L depends on where the variance arrived.

**Some contracts are path-dependent by design.** Barrier options, Asian options and lookbacks pay on the path. A CRE loan with a covenant that triggers a cash sweep when DSCR falls below a level is a barrier option embedded in the capital structure.

**Daily-rebalanced leveraged products are path-dependent through compounding.** A product that delivers $L$ times the daily return of an index $I$ has value after $n$ days

$$\frac{A_n}{A_0} = \prod_{i=1}^n(1 + L\,r_i).$$

Over two days with index returns $+x$ and $-x$, the index ends at $1 - x^2$ while the product ends at $1 - L^2x^2$. For $L = -1$ the loss from round trips equals the index's, but for $L = 2$ it is four times as large. More importantly for 2018, **rebalancing is pro-cyclical for both long-leveraged and inverse products**. With net assets $A$ and target exposure $LA$, an index return $x$ changes exposure to $LA(1+x)$ and assets to $A(1+Lx)$. The trade needed to restore the target is

$$LA(1+Lx) - LA(1+x) = L(L-1)A\,x.$$

For $L = -1$, $L(L-1) = 2$. For $L = 2$, $L(L-1) = 2$. In both cases the product **buys** after the index rises and **sells** after it falls, in the amount $2Ax$. Inverse products (short the index) must buy back short exposure as the index rises. This is a feedback loop in the futures they trade.

---

## 18.9 Historical episode: 5 February 2018 ("Volmageddon"), with the 1987 skew as background

### Background: the skew that 1987 left behind

Before October 1987, implied volatilities of S&P 500 index options were roughly flat across strikes. After the crash, a downward slope appeared, with low-strike puts priced at higher implied vol, and it has persisted [FACT: Rubinstein (1994), "Implied Binomial Trees", *Journal of Finance* 49(3); ch18-S05, VERIFIED-SECONDARY]. Bates (1991) found that out-of-the-money puts on S&P 500 futures became unusually expensive during the year before the crash, but found little evidence of strong crash fears in the two months immediately before it [FACT: ch18-S06, VERIFIED-SECONDARY]. The 1987 episode itself is covered in Chapter 1, §1.9. For this chapter, its legacy is that the market charges for crash risk at low strikes, which is why Example 18.5 priced the 90% put at a higher vol than the at-the-money level.

### Date and environment

In 2017 U.S. equity volatility was low by historical standards, and exchange-traded products that were short VIX futures had grown *[INFERENCE from the BIS article's discussion of the growth in VIX futures open interest; ch18-S01]*. The BIS reports that average daily VIX futures open interest grew from about 180,000 contracts in 2011 to about 590,000 in 2017 [FACT: ch18-S01, VERIFIED-SECONDARY].

The relevant products were exchange-traded notes and funds that delivered a fixed multiple, −1x for inverse and +2x for leveraged, of the **daily** return of an index of short-term VIX futures. The best known was Credit Suisse's VelocityShares Daily Inverse VIX Short-Term ETN (ticker XIV). Its terms allowed the issuer to accelerate (redeem) the notes if the intraday indicative value fell to 20% or less of the prior day's closing indicative value [FACT: Credit Suisse press release of 6 February 2018; ch18-S03, VERIFIED-SECONDARY].

### What happened

On Monday, 5 February 2018, the S&P 500 fell 4% and the VIX rose 20 points, the largest one-day increase in the VIX since 1987 [FACT: Sushko and Turner, BIS Quarterly Review, March 2018; ch18-S01, VERIFIED-SECONDARY]. Secondary data show the VIX closing at about 17 on 2 February and about 37 on 5 February *(exact closing levels verification pending against Cboe's published VIX history; ch18-S08)*.

The BIS article concluded that the daily rebalancing of leveraged and inverse volatility ETPs, concentrated in the last hour of trading, appeared to have been a key factor in that afternoon's VIX spike, even though the aggregate positions in these products were relatively small [FACT: ch18-S01, VERIFIED-SECONDARY; paraphrased]. A Bank of England staff blog post reported that the one-month VIX future rose 96% that day, its largest increase on record, with about a quarter of the rise at the end of the day when the ETP issuers had to buy futures to rebalance [FACT: ch18-S04, VERIFIED-SECONDARY].

On 6 February, Credit Suisse announced that an acceleration event had occurred. XIV's closing indicative value on 2 February had been \$108.3681. The accelerated valuation date was expected to be 15 February, with payment on 21 February [FACT: ch18-S03, VERIFIED-SECONDARY]. Reports put the redemption value near \$6 a note *(verification pending; ch18-S07)*.

On 17 May 2021, the SEC settled charges against S&P Dow Jones Indices, which calculated the index underlying XIV. S&P DJI agreed to a \$9 million penalty without admitting or denying the findings. The SEC found that an undisclosed "Auto Hold" feature caused the index to publish unchanged values for intervals between 4:00 and 5:08 p.m. on 5 February, and that these stale values contributed to a 96% drop in the value of the XIV notes. Commissioner Peirce dissented [FACT: ch18-S02, VERIFIED-SECONDARY via news reports of the SEC order]. Private class actions against Credit Suisse followed [FACT: Credit Suisse Group 20-F for 2018; ch18-S10, VERIFIED-SECONDARY].

### The arithmetic of the loss

The mechanism follows from §18.8. Take a hypothetical inverse product with assets $A = \$1{,}000$ million, short \$1,000 million of VIX futures [HYPOTHESIS].

* If the futures rise $x = 50\%$, assets fall to $A(1 - x) = \$500$ million. The short exposure has grown to \$1,500 million. To restore −1x, the product must buy back $L(L-1)Ax = 2\times1{,}000\times0.50 = \$1{,}000$ million of futures, twice its remaining assets.
* If the futures rise 96%, a −1x daily product loses 96% of its value in one day, before fees. That matches the size of the loss the SEC described [INFERENCE: from the Bank of England staff blog's 96% figure for the one-month future and the −1x daily design; the index tracked a blend of the first two VIX futures, so the match is approximate].
* A +80% intraday rise in the tracked index takes an inverse product's indicative value to 20% of the prior close, the acceleration threshold.

The products were, in effect, short gamma on VIX futures. Each rise in the futures forced them to buy, in the amount $2Ax$, the same pattern as a delta hedger who is short options. Their hedging added to the move it was responding to.

### What was knowable beforehand

The −1x daily design, the 20% acceleration trigger and the end-of-day rebalancing were in the offering documents [FACT for the trigger: ch18-S03; INFERENCE for the rest, from the products' stated design]. The rebalancing arithmetic above follows from those terms. The size of the products relative to VIX futures liquidity was observable in public open-interest data. What was not knowable was the date, or whether a shock large enough to set off the feedback would arrive while the products were large.

### Interpretations

* **Plumbing.** The BIS view: a small but mechanically pro-cyclical set of products amplified a moderate equity decline into a record volatility spike.
* **Positioning.** Short volatility had become a crowded, carry-like trade, and any shock would have forced exits.
* **Index operation.** The SEC's 2021 order identified a specific failure in the index calculation that afternoon. Commissioner Peirce's dissent shows the extent of that failure's contribution is disputed.

These are complementary rather than exclusive.

### What the case establishes and what it does not

It establishes that (i) selling insurance on volatility produces long periods of steady gains and rare, near-total losses; (ii) daily-rebalanced products are path-dependent and have pro-cyclical hedging demand; (iii) the acceleration terms of a structured note define a barrier that holders may not price. It does **not** establish that volatility ETPs caused the equity decline on 5 February. The BIS article does not claim this, and the Bank Underground post argues that there is no mechanical link from ETP hedging to equity prices. Nor does it establish the variance risk premium's size, or that short volatility is a losing strategy on average. A strategy can be positive on average and still ruinous at the wrong size (Chapter 1, Example 1.5).

### CRE connection

A floating-rate borrower who does not buy a cap is short rate volatility in the same way. The carry is positive (no premium is paid) until a rate shock, and then losses are severe and the forced action, a covenant breach, arrives mechanically. The 2022–2024 cap-replacement squeeze (Chapter 10, §10.9) was the CRE version: the short-vol position was the decision to buy caps shorter than the loan.

---

## 18.10 Decision exercise: the three decisions from §18.1

Write a one-page decision record (template: `desk/investment_memos/decision_record_template.md`) covering the following.

**Decision A (cap).**
1. Choose a strike between 4.00% and 4.50%. Justify it with DSCR at the strike on base and on stressed NOI (NOI down 25%).
2. State the premium and its annual equivalent. Is the premium reserved in the sources and uses?
3. Say how you will fund the replacement cap at the first extension. Give a premium range for forwards of 3.60% and 4.75%.

**Decision B (tail hedge).**
1. Identify whether the office has any **forced action** in a crash: margin, capital calls on the hotel, redemptions.
2. Compare: (i) the rolling 90% put; (ii) the 90/75 put spread; (iii) reducing the equity allocation by an amount with the same crash-state loss reduction. Use Example 18.5.
3. State an invalidation criterion. For example, stop the program if implied vol at the strike exceeds a stated level, because insurance bought after a scare is overpriced relative to its use.

**Decision C (yield fund).**
1. Reconstruct the strategy's premium income from the stated terms (Problem 18.10) and check whether 1% a month is consistent with them.
2. Compute the loss in a month in which the index falls 25%.
3. Decide whether to invest, invest small, or decline, and list the information you would need to change your answer.

**Rubric.**

| Element | Full credit requires |
|---|---|
| A: strike | DSCR computed at the strike on stressed NOI; covenant treated as the maximum, not the target |
| A: replacement | Replacement premium range computed; cash reserved or term matched |
| B: forced action | The hedge decision is tied to a specific crash-state liability; otherwise cheaper alternatives are preferred |
| B: cost | Ten-year cumulative drag stated (about 35% for the 90% put at 24% vol) and compared with alternatives |
| C: reconstruction | Inconsistency between the claimed 1% a month and the stated terms identified; implied leverage or strike inferred |
| C: tail | Loss in a −25% month computed and compared with the track record length |
| C: decision | Abstention or a small, sized allocation with an explicit maximum loss; "Sharpe above 3" treated as a symptom of short-sample short-convexity, not evidence of skill |
| All | Each derivative is named as long or short convexity, and the counterparty, margin and basis risks are stated |

There is no single correct allocation. Declining Decision C is the expected answer given the information supplied, but a candidate who sizes it so that a −25% month costs less than 2% of total capital and states the data required can earn full credit.

---

## 18.11 Frequent analytical errors

1. **Treating the forward price as a forecast.** It is carry arithmetic. A forward below spot does not predict a decline.
2. **Comparing implied and realized vol with different estimators or horizons.** Agree the estimator (zero-mean or demeaned), the annualization (252 trading days), and the window before calling vol "cheap".
3. **Running tail stress with Greeks.** Delta-gamma underestimates or overestimates large moves and ignores the vol response. Reprice fully with a linked vol shock (Example 18.2).
4. **Calling a delta-hedged option "long vol" without asking where.** P&L is gamma-weighted; the path matters (Example 18.4).
5. **Quoting a put program's cost per roll.** The relevant figure is the annual cost and its ten-year compounding (Example 18.5).
6. **Ignoring margin.** A futures hedge that is right on price can still force a sale through variation margin (Example 18.6).
7. **Forgetting swap breakage.** A pay-fixed swap is a liability on early exit when rates have fallen (Example 18.7).
8. **Pricing a cap at the wrong vol.** One at-the-money vol applied to an OTM strike imposes a model's tail on the price. Ask for the strike-specific quote (Example 18.8e).
9. **Buying a cap shorter than the realistic hold.** The cap is then a roll-over bet on future cap prices (Chapter 10).
10. **Ignoring the sponsor's volatility incentive.** Underwriting a loan on expected NOI alone misses the value transfer from a riskier plan (Example 18.9).
11. **Mixing rate conventions.** Black–Scholes uses continuously compounded rates. Swaps and caps here use annually or quarterly compounded discount factors. Convert before mixing.
12. **Reading a short track record of option selling as skill.** Selling insurance produces high Sharpe ratios until the insured event happens (§18.9, Problem 18.10).

---

## 18.12 Connections to other chapters

* **Chapter 1** (§1.9): the 1987 crash and portfolio insurance as a replicated put. **Chapter 2**: bid–ask costs that the delta-hedging simulation ignores, and appraisal smoothing that biases $\sigma_V$.
* **Chapter 6**: discount factors, forward rates, DV01 and convexity, used here for swaps. **Chapter 5**: policy-rate paths that drive SOFR forwards.
* **Chapter 10**: caps and the Bachelier caplet (`x_capital_structure`), equity as a call, the bargaining zone at maturity (Example 10.8), and the 2022–2024 cap-replacement squeeze.
* **Chapter 13**: real options on development (`x_options_real`), which use the same no-arbitrage logic on a binomial tree.
* **Chapter 15**: FX forwards and covered interest parity, the currency version of §18.4.1.
* **Chapter 17**: credit spreads, hazard rates and the structural model in more depth.
* **Chapter 21**: sizing short-convexity positions so that a tail event is survivable.
* **Chapter 23**: the full histories of 1987 and 2008.
* **Case B** (`cases/hypothetical/case_B_refinancing_cliff/`): the cap-replacement decision in a full refinancing case.

---

## 18.13 One-page reference sheet

| Item | Formula |
|---|---|
| Forward price | $F = Se^{(r-q)T}$; off-market forward value $Se^{-qT} - Ke^{-rT}$ |
| Put–call parity | $C - P = Se^{-qT} - Ke^{-rT}$ |
| Black–Scholes call | $Se^{-qT}N(d_1) - Ke^{-rT}N(d_2)$; $d_1 = [\ln(S/K) + (r-q+\sigma^2/2)T]/(\sigma\sqrt T)$ |
| Delta, gamma | $e^{-qT}N(d_1)$ (call); $e^{-qT}\phi(d_1)/(S\sigma\sqrt T)$ |
| Vega | $Se^{-qT}\phi(d_1)\sqrt T$ per 1.00; ÷100 per vol point; $\nu = \sigma TS^2\Gamma$ |
| PDE in Greeks | $\Theta + (r-q)S\Delta + \tfrac12\sigma^2S^2\Gamma = rV$ |
| Hedged P&L | $\sum\tfrac12\Gamma_iS_i^2[(\Delta S_i/S_i)^2 - \sigma_{impl}^2\Delta t]$; expectation $\sum\tfrac12\Gamma_iS_i^2(\sigma_r^2-\sigma_i^2)\Delta t \approx \nu(\sigma_r - \sigma_i)$ |
| Break-even daily move | $\sigma_{impl}/\sqrt{252}$ (16 vol ≈ 1%/day) |
| Realized vol | $\sqrt{(252/n)\sum r_i^2}$ (zero-mean, log returns) |
| Min-variance hedge | $h^* = \rho\sigma_S/\sigma_F$; effectiveness $\rho^2$; contracts $= h^*\times\text{exposure}/(F\times\text{mult})$ |
| Swap | Float leg $N(1-P_n)$; fixed $NKA$; $K_{par} = (1-P_n)/A$; value (pay fixed) $NA(K_{par} - K)$; DV01 ≈ $NA\times10^{-4}$ |
| Bachelier caplet | $N\tau P[(F-K)N(d) + \sigma_N\sqrt T\phi(d)]$, $d = (F-K)/(\sigma_N\sqrt T)$ |
| Black caplet | $N\tau P[FN(d_1) - KN(d_2)]$; $\sigma_N \approx \sigma_{LN}F$ near the money |
| Cap strike from DSCR | $K_{max} = NOI/(DSCR_{min}\cdot N) - s$ |
| Merton | $E = C(V,B)$; $D = Be^{-rT} - P(V,B)$; spread $= -\ln(D/B)/T - r$ |
| Leveraged ETP rebalance | Trade $= L(L-1)A\,x$; $= 2Ax$ for both −1x and +2x |
| Put program | Annual cost $=$ premium% × rolls/yr; 10-yr drag $(1-c)^{10}$; break-even crash frequency $=$ annual cost / crash payoff |

**Questions for any derivative.** Am I long or short convexity? Who pays me, and in which state? What is the counterparty's condition in that state? What cash does the position need before it pays off (margin, premium, breakage)? Is the hedge's term as long as the exposure's?

**Library.** `sdesk.markets` (BS price, delta, gamma, vega, parity gap); `sdesk.x_derivatives` (theta, implied vol, hedge simulation, put roll, hedge ratio, Black caplets, swaps, Merton); `sdesk.x_capital_structure` (Bachelier caplets and cap premium).

---

## References for this chapter

Sources are registered in `references/sources_ch18.md` with verification status.

* Ahmad, R., and Wilmott, P. (2005). "Which Free Lunch Would You Like Today, Sir?: Delta Hedging, Volatility Arbitrage and Optimal Portfolios." *Wilmott Magazine*, November, 64–79.
* Bachelier, L. (1900). *Théorie de la spéculation*. Annales scientifiques de l'École Normale Supérieure, 3e série, 17, 21–86.
* Bates, D. S. (1991). "The Crash of '87: Was It Expected? The Evidence from Options Markets." *Journal of Finance*, 46(3), 1009–1044.
* Black, F. (1976). "The Pricing of Commodity Contracts." *Journal of Financial Economics*, 3(1–2), 167–179.
* Black, F., and Scholes, M. (1973). "The Pricing of Options and Corporate Liabilities." *Journal of Political Economy*, 81(3), 637–654.
* Cox, J. C., Ingersoll, J. E., and Ross, S. A. (1981). "The Relation between Forward Prices and Futures Prices." *Journal of Financial Economics*, 9(4), 321–346.
* Jensen, M. C., and Meckling, W. H. (1976). "Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure." *Journal of Financial Economics*, 3(4), 305–360.
* Merton, R. C. (1973). "Theory of Rational Option Pricing." *Bell Journal of Economics and Management Science*, 4(1), 141–183.
* Merton, R. C. (1974). "On the Pricing of Corporate Debt: The Risk Structure of Interest Rates." *Journal of Finance*, 29(2), 449–470.
* Rubinstein, M. (1994). "Implied Binomial Trees." *Journal of Finance*, 49(3), 771–818.
* Sushko, V., and Turner, G. (2018). "The Equity Market Turbulence of 5 February — the Role of Exchange-Traded Volatility Products." *BIS Quarterly Review*, March 2018. https://www.bis.org/publ/qtrpdf/r_qt1803t.htm
* Bank of England, Bank Underground (2018). "Is the Tail Wagging the Dog? The Impact of VIX Exchange Traded Products on Equity Volatility." 24 April 2018.
* Credit Suisse AG (2018). "Credit Suisse AG Announces Event Acceleration of its XIV ETNs." Press release, 6 February 2018 (filed as Form 6-K exhibit with the SEC).
* U.S. Securities and Exchange Commission (2021). Order instituting cease-and-desist proceedings, *In the Matter of S&P Dow Jones Indices LLC*, 17 May 2021.
* CME Group. E-mini S&P 500 futures contract specifications.
