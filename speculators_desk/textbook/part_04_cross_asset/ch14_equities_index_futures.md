# Chapter 14 — Equities and Equity Index Futures

> **Status:** Complete (v1.0). Numerical examples are reproduced in `tests/test_ch14_examples.py` (library: `sdesk.x_equities`, new for this chapter, plus `sdesk.markets` and `sdesk.x_cre_distress`). Problems are in `problems/questions/ch14_problems.md` and solutions in `problems/solutions/ch14_solutions.md`. Sources are in `references/sources_ch14.md`. Pending verifications are flagged in the text: the S&P 500 closing low of October 2002, the size of the 1987 futures discount, the Rule 201 trigger details, and one bibliographic check (Gordon, 1959).

## Learning objectives

After this chapter you should be able to:

1. Build the bridge from EBITDA to EPS and from market capitalization to enterprise value, and convert a listed company's multiples into a **cap-rate equivalent**. Explain why an earnings yield and a cap rate are different quantities, even for the same buildings.
2. Estimate an **implied equity risk premium** (ERP) from a Gordon model and from a two-stage model. Compute the earnings-yield-minus-real-yield gap and state the conditions under which it is, and is not, an estimate of expected real return.
3. Price an equity **index future** by cost of carry, state the no-arbitrage band, and verify the CME E-mini (\$50) and Micro E-mini (\$5) multipliers before computing notional or P&L.
4. Distinguish **margin from notional**. Compute leverage, the price move that triggers a margin call, and the cash a hedge can consume.
5. Size a **beta hedge** with $N = \beta V/(F \times m)$, and decompose the hedged position into what the hedge removes and what it leaves behind.
6. Analyze **short selling** as a position with borrow cost, recall risk, a margin trigger, and unlimited loss, and recognize when the right answer is not to short.
7. Read **breadth, momentum, and earnings surprises** as information about the distribution of returns, not as signals in isolation.
8. Treat a **REIT as listed CRE**: compute its implied cap rate and NAV discount, compare it with private marks, and hedge a private CRE portfolio's equity beta with index futures while measuring the basis risk that remains.

---

## 14.1 Opening investment problem: the lodging allocation and the equity tape

You are the CIO of a family office with \$310 million of capital. The private book holds a hotel portfolio (gross value \$120 million, \$72 million of debt, \$48 million of equity at the last appraisal) and stabilized industrial and multifamily assets. A \$40 million liquid sleeve holds listed REITs. All figures in this opening problem and in the worked examples are [HYPOTHESIS], a constructed teaching case. Market levels such as "S&P 500 at 6,000" are illustrative inputs, not observations.

At Thursday's investment committee four items are on the agenda.

**Item 1 — The lodging REIT.** A listed lodging REIT trades at \$17.50 a share. Your analyst says that at the 7.00% cap rate your appraiser used for your own hotels, the REIT's net asset value is about \$21 a share. "We can buy hotels in the public market at a 17% discount." The private-equity sponsor down the street says the opposite: "The REIT market is telling you your own marks are too high."

**Item 2 — The equity market.** The S&P 500 is at 6,000 on forward operating earnings of 280 index points, a forward P/E of 21.4. The 10-year Treasury yields 4.25% and the 10-year TIPS yields 2.00%. A board member asks whether stocks are "expensive relative to bonds," and whether the office should sell REIT shares and hold Treasuries.

**Item 3 — The hedge.** You plan to sell the hotel portfolio in about six months. A broker proposes selling S&P 500 E-mini futures to "lock in" today's value against a market sell-off. He has sized it at about 310 contracts.

**Item 4 — The short.** A portfolio manager wants to short \$1 million of a hotel-booking technology stock that she considers overvalued. The stock is moderately hard to borrow.

By the end of the chapter you can answer each item with numbers and say what you would need to believe to act. Section 14.10 returns to the committee.

---

## 14.2 Economic intuition

### A share is a levered, taxed, managed claim on operating assets

A hotel appraiser capitalizes NOI after an FF&E reserve. That NOI belongs to the whole capital structure, it is before income tax, and it carries no corporate overhead. A share in a hotel C-corporation is a claim on what is left after interest, corporate overhead, income tax, and whatever management decides to reinvest. The earnings yield $E/P$ is the accounting version of that residual claim, divided by the price of the residual claim. Comparing it directly with a cap rate compares a levered, after-tax, after-depreciation yield with an unlevered, pre-tax, after-reserve yield. The two can differ by several hundred basis points for the same buildings, and the difference is mostly structure, not mispricing. The comparable public-market number is the **enterprise-value cap rate**: NOI after reserve divided by the market value of the whole capital structure. For a REIT this is the implied cap rate of Chapter 12.

### The equity premium is a forecast, not a datum

The equity risk premium is the expected return on equities in excess of a risk-free rate. It cannot be observed. It can only be inferred from prices and a model of future cash flows. Every implied ERP is a statement of the form "**if** distributions grow at $g$, **then** today's price implies a return of $k$." The model is only as good as $g$. A small error in $g$ is a one-for-one error in $k$. Treat any ERP to one decimal place as a scenario, and present several.

### Futures transfer exposure without transferring the asset

An index future lets you buy or sell the market's price exposure without buying or selling the stocks. The buyer of a future gives up the dividends and keeps the cash; the seller gives up the interest on the cash and keeps the dividends. In equilibrium the futures price adjusts so that neither side gains: $F = S \times (\text{1 + financing}) - \text{dividends}$. Because only margin changes hands, a future converts a small amount of cash into a large exposure. That is efficient for hedging and dangerous for speculation: the leverage is decided by the position size, not by the margin the exchange happens to demand.

### Hedging with index futures hedges the index, not your asset

A short index future pays when the S&P 500 falls. Your hotel portfolio falls when the S&P 500 falls only to the extent that the two share a common driver. Whatever the hotels do for their own reasons (a new competing hotel, a franchise dispute, a local recession) remains. In addition, the private portfolio is appraised quarterly and smoothed (Chapter 2), while the futures settle daily in cash. A hedge that is economically sound can still drain liquidity while the appraisal does not move. "Hedged" always means "hedged against a named risk, with a named residual."

### Short selling is not the mirror image of buying

A long position can lose at most 100% and shrinks as it loses. A short position can lose without limit and **grows** as it loses. The short seller also pays to borrow the shares, can be forced to return them at the worst moment (recall), and faces margin calls precisely when the price has moved against the thesis. A short needs a larger expected edge and a smaller size than a long with the same conviction.

### Breadth, momentum, and surprise are about the distribution

A cap-weighted index can rise while most of its members fall. Momentum (past winners keep winning over 3–12 months) is one of the best-documented return patterns and one of the most crash-prone (Jegadeesh and Titman, 1993; ch14-S12). Earnings surprises move prices, and the response historically continued for weeks after the announcement (post-earnings-announcement drift; Bernard and Thomas, 1989; ch14-S13). None of these is a trading rule on its own. Each is information about how concentrated, how trending, or how surprised the market is. That information changes the distribution of outcomes for a position, including a CRE position whose exit cap depends on the same capital flows.

---

## 14.3 Technical definitions

| Term | Definition |
|---|---|
| EPS | Net income attributable to common shareholders divided by diluted shares |
| P/E; earnings yield | Price ÷ EPS; its reciprocal $E/P$. "Forward" uses next-12-month expected EPS; "trailing" the last 12 months |
| Enterprise value (EV) | Equity market value + debt + preferred + minority interest − cash |
| EV/EBITDA | Enterprise value ÷ EBITDA. Capital-structure neutral but before capex and tax |
| EV cap rate | $(EBITDA - \text{maintenance capex})/EV$. For a hotel company, the numerator is NOI after FF&E reserve |
| Implied cap rate (REIT) | Forward cash NOI ÷ (market cap + debt + preferred − cash − non-real-estate assets) (Chapter 12) |
| NAV | Gross asset value at private cap rates − debt − preferred + cash + other assets |
| Equity risk premium (ERP) | Expected equity return minus a risk-free rate. *Implied* ERP is backed out of prices with a cash-flow model |
| Payout (cash) yield | (Dividends + net buybacks) ÷ market value |
| CAPE | Price ÷ 10-year average of inflation-adjusted earnings (Shiller) |
| Index future | Exchange-traded contract on an index level, cash-settled; notional $= F \times m$ |
| Multiplier $m$ | Dollars per index point. CME E-mini S&P 500: \$50; Micro E-mini S&P 500: \$5 [FACT; ch14-S01, S02] |
| Tick | Minimum price increment. E-mini and Micro S&P 500: 0.25 index points, worth \$12.50 and \$1.25 [FACT; ch14-S01, S02] |
| Basis | $F - S$. Converges to zero at expiry for a cash-settled contract |
| Initial / maintenance margin | Performance bond posted to open a position / the level below which a call is issued |
| Variation margin | The daily cash settlement of futures gains and losses |
| Beta $\beta$ | $\text{Cov}(r, r_m)/\text{Var}(r_m)$: sensitivity of an asset's return to the market's |
| Asset beta | Beta of the unlevered operating assets: $\beta_A = \beta_E (E/V) + \beta_D (D/V)$ |
| Borrow fee | Annualized fee paid by a short seller to the stock lender |
| Recall | The lender's right to demand the shares back, forcing the short to cover or re-borrow |
| Breadth | The share of index members participating in a move (advancers vs decliners, equal- vs cap-weighted return) |
| Time-series momentum | Position in the sign of an asset's own trailing return, scaled to a volatility target |
| SUE | Standardized unexpected earnings: (actual − consensus) ÷ standard deviation of past surprises |

---

## 14.4 Equations and derivations

### 14.4.1 From EBITDA to EPS, and from EV to a cap rate

$$EBIT = EBITDA - D\&A, \qquad EBT = EBIT - \text{Interest}, \qquad NI = EBT(1-\tau), \qquad EPS = NI/\text{shares}.$$

$$EV = \text{Mkt cap} + \text{Debt} + \text{Pref} - \text{Cash}, \qquad c_{EV} = \frac{EBITDA - \text{capex}_{maint}}{EV}.$$

If a multiple is quoted on EBITDA and the reserve is a share $\rho$ of revenue while EBITDA is a margin $\mu$ of revenue, then capex $= (\rho/\mu) EBITDA$ and

$$c_{EV} = \frac{1}{EV/EBITDA}\left(1 - \frac{\rho}{\mu}\right).$$

A 12.5x EBITDA multiple is an 8.0% EBITDA yield, but at a 30% margin and a 4% reserve it is a 6.93% cap rate (Problem 14.3). The reserve consumes $\rho/\mu = 13.3\%$ of EBITDA.

**Why $E/P \neq c$.** Write the equity yield before tax as $(c_{EV}\,EV - r_D D)/E$. With $EV = D + E$:

$$\frac{c_{EV} EV - r_D D}{E} = c_{EV} + \frac{D}{E}(c_{EV} - r_D).$$

This is the positive-leverage identity of Chapter 1 §1.4.6 applied to yields. On top of it, accounting depreciation differs from the reserve, and income tax takes $\tau$ of the remainder. The earnings yield can be above or below the cap rate depending on these three terms.

### 14.4.2 Implied equity returns

**Gordon.** If next-year cash distributions are $D_1$ and grow at $g$ forever, $P = D_1/(k-g)$ and

$$k = \frac{D_1}{P} + g, \qquad ERP = k - y_{10}.$$

This is the same algebra as the cap-rate relation $c = k - g$ (Chapter 9; `sdesk.cre.gordon_cap_rate`). An index payout yield plays the role of the cap rate.

**Two-stage.** Distributions are $CF_t = CF_1(1+g_1)^{t-1}$ for $t = 1,\dots,n$, then grow at $g_2$:

$$P = \sum_{t=1}^{n}\frac{CF_t}{(1+k)^t} + \frac{CF_n(1+g_2)}{(k-g_2)(1+k)^n}.$$

Solve for $k$ numerically. The right side falls monotonically in $k$ for $k > g_2$, so bisection always converges (`sdesk.x_equities.two_stage_implied_return`).

**Earnings yield minus real yield.** Suppose a firm pays out a fraction $b$ of earnings and reinvests the rest at return $ROE$. Then $g = (1-b)ROE$ and

$$k = \frac{bE_1}{P} + (1-b)ROE.$$

If $ROE = k$ (reinvestment earns exactly the cost of capital), this collapses to $k = E_1/P$. The earnings yield is then the expected return, and, because earnings are a real claim on a business that can reprice, it is approximately a **real** expected return. Hence the comparison

$$\text{Gap} = \frac{E_1}{P} - y_{TIPS}.$$

Three caveats govern its use. (i) If $ROE > k$, growth adds value and $E/P$ understates expected return. If $ROE < k$, it overstates it. (ii) Reported earnings are cyclical and subject to accounting choices, so the gap swings with margins. CAPE smooths this at the cost of staleness. (iii) Comparing $E/P$ with a **nominal** Treasury yield (the "Fed model") mixes a real yield with a nominal one. Asness (2003; ch14-S11) shows that this comparison has had no power to forecast long-horizon real stock returns. It describes how investors have priced stocks, not how they should.

### 14.4.3 Index futures: cost of carry

Buying the index now and financing it at $r$ costs $S(1+rt)$ at expiry and yields dividends $D$ along the way. Buying the future and holding cash gives the same exposure. No arbitrage requires

$$F = S(1+rt) - D \quad\text{(simple interest)}, \qquad F = S e^{(r-q)t} \quad\text{(continuous, dividend yield } q).$$

With round-trip costs of $\kappa$ index points (stock commissions and impact, futures fees, financing spread), arbitrage keeps $F$ only within the band

$$F^* - \kappa \;\le\; F \;\le\; F^* + \kappa.$$

Above the band, a **cash-and-carry** (buy stocks, sell futures) earns $F - F^* - \kappa$. Below it, the **reverse** trade requires shorting or selling the stocks you already hold. That is why the lower bound is enforced mainly by index holders who can sell stock they own, and why it fails when the cash market is impaired (§14.8).

**Notional, P&L, and ticks.**

$$\text{Notional} = F \times m \times N, \qquad P\&L = \text{side}\times(F_{exit}-F_{entry})\times m \times N.$$

At $m = 50$ a one-point move is \$50 per contract and a tick is \$12.50. At $m = 5$ (Micro) it is \$5 and \$1.25. Ten Micros equal one E-mini. **Check the multiplier on the exchange's contract page before every new contract.** A factor-of-ten error in a hedge is the most common futures mistake made by people who trade futures occasionally.

### 14.4.4 Margin and leverage

Margin is a performance bond, not a down payment. With initial margin $IM$ and maintenance $MM$ per contract, a call is issued after an adverse move of

$$\Delta F_{call} = \frac{IM - MM}{m}\ \text{points}.$$

Economic leverage is $\text{Notional}/\text{Capital at risk}$. If the position is backed only by initial margin, leverage is $\text{Notional}/IM$. A **fully collateralized** future, with Treasury bills equal to the notional, replicates an unlevered index position.

For a **long stock position bought on margin** with initial margin fraction $m_0$ and maintenance $m_m$: loan per share $= (1-m_0)P_0$. A call occurs when $(P - (1-m_0)P_0)/P = m_m$:

$$P^*_{long} = \frac{(1-m_0)P_0}{1-m_m}.$$

At $m_0 = 50\%$ and $m_m = 25\%$, $P^* = 0.5/0.75 \times P_0 = 66.7\%$ of $P_0$, a 33.3% decline.

### 14.4.5 Short selling

A short sale of $Q$ shares at $P_0$ with initial margin $m_0$ leaves collateral of $(1+m_0)QP_0$ (the proceeds plus the margin). Equity at price $P$ is $(1+m_0)QP_0 - QP$. A call occurs when equity falls below $m_m QP$:

$$P^*_{short} = \frac{(1+m_0)P_0}{1+m_m}.$$

At $m_0 = 50\%$ and $m_m = 30\%$, $P^* = 1.5/1.3 \times P_0 = 115.4\%$ of $P_0$: a 15.4% rise triggers a call. The account is wiped out at $P = (1+m_0)P_0$, a 50% rise. One-period P&L, ignoring the rebate on cash collateral:

$$P\&L_{short} = Q(P_0 - P_T) - f\,Q\,\bar P\,t - \text{dividends paid},$$

where $f$ is the annual borrow fee on the average position value $\bar P$. In the United States, Regulation SHO (adopted 2004) requires a broker to have reasonable grounds to believe the shares can be borrowed before accepting a short sale (the "locate"). Rule 201 (adopted 2010) restricts the price at which short sales may be executed after a stock has fallen sharply [FACT; ch14-S15; the trigger and duration of the Rule 201 restriction are *(verification pending)* against the rule text]. The payoff is the negative of a long stock: concave in price, with unlimited downside. Recall risk turns a chosen holding period into a random one. Recalls cluster when the stock is rising and hard to borrow, so the forced cover occurs near the worst price.

### 14.4.6 Beta hedging

For a long position $V$ with beta $\beta$ to the index underlying a future with price $F$ and multiplier $m$, the number of contracts to sell is

$$N = \frac{\beta V}{F m}.$$

*Derivation.* For a small index return $r_m$, the position changes by $\beta V r_m$, and one short future gains $-F m\, r_m$ (to first order, with the basis held constant). Setting $\beta V r_m - N F m\, r_m = 0$ gives $N$. Write the position's return as $r = \alpha + \beta r_m + \varepsilon$. The hedged return is then $\alpha + (\beta - \beta_h) r_m + \varepsilon$ plus the cash return embedded in the future. The hedge removes $\beta_h r_m$ and nothing else. Its volatility is

$$\sigma_{hedged} = \sqrt{(\beta-\beta_h)^2\sigma_m^2 + \sigma_\varepsilon^2}, \qquad \text{variance reduction} = \rho^2 \text{ when } \beta_h = \beta.$$

**The hedge has an expected cost.** Selling $\beta V$ of index exposure gives up $\beta V \times ERP$ per year in expectation. A hedge is insurance, and the premium is the ERP.

**Levering and unlevering beta.** With debt beta $\beta_D$ (zero unless stated),

$$\beta_A = \beta_E\frac{E}{V} + \beta_D\frac{D}{V}, \qquad \beta_E = \frac{\beta_A - \beta_D D/V}{1 - D/V}.$$

A REIT's equity beta is measured at the REIT's leverage. A private portfolio at higher leverage has a higher equity beta on the same assets. Note that the dollar beta $\beta_E E = \beta_A V$ when $\beta_D = 0$. The hedge is sized on gross asset exposure, whatever the leverage.

### 14.4.7 Breadth, momentum, and surprise

Cap-weighted and equal-weighted returns over $i = 1,\dots,n$ members:

$$r_{cw} = \sum_i \frac{w_i}{\sum_j w_j} r_i, \qquad r_{ew} = \frac{1}{n}\sum_i r_i.$$

A large gap $r_{cw} - r_{ew}$ with more decliners than advancers is **narrow** leadership. The index then depends on a few names, and diversification inside it is lower than its member count suggests.

Time-series momentum takes the sign of the trailing 12-month compounded return and scales the position to a volatility target: weight $= \text{sign}(\prod(1+r_t) - 1) \times \sigma^*/\sigma$ (`sdesk.x_dynamics.tsmom_position`).

Standardized unexpected earnings: $SUE = (EPS_{actual} - EPS_{consensus})/\sigma_{surprise}$ (`sdesk.x_microstructure.standardized_surprise`). The price reaction depends on the revision to **forward** earnings and to the multiple, not on the beat itself:

$$\frac{P_1}{P_0} = \frac{E^{fwd}_1}{E^{fwd}_0}\times\frac{(P/E)_1}{(P/E)_0}.$$

---

## 14.5 Worked examples

All eight examples are reproduced in `tests/test_ch14_examples.py`. Inputs are [HYPOTHESIS] unless a source is cited.

### Example 14.1 — Hotel C-corp: P/E, EV/EBITDA, and the cap rate the market is paying

**Given.** A hotel owner-operator organized as a C-corporation. Share price \$48.00; 200 million diluted shares. Debt \$4.20 billion; cash \$0.30 billion. Revenue \$4.00 billion; EBITDA \$1.20 billion; depreciation and amortization \$0.45 billion; interest \$0.24 billion; tax rate 21%. Maintenance capex equals a 4% FF&E reserve on revenue. No preferred and no minority interest.

**Find.** EPS, P/E, earnings yield, EV/EBITDA, and the EV cap rate. Reconcile the earnings yield with the cap rate.

**Solution.**

Market cap $= 48 \times 200\text{m} = \$9.60$ billion. $EV = 9.60 + 4.20 - 0.30 = \$13.50$ billion.

$EBIT = 1.20 - 0.45 = \$0.75$ billion. $EBT = 0.75 - 0.24 = \$0.51$ billion. $NI = 0.51 \times 0.79 = \$402.9$ million. $EPS = 402.9/200 = \$2.0145$.

$P/E = 48/2.0145 = 23.83$x. Earnings yield $= 4.20\%$.

$EV/EBITDA = 13.50/1.20 = 11.25$x, an EBITDA yield of 8.89%.

Reserve $= 0.04 \times 4.00 = \$0.16$ billion. EV cap rate $= (1.20 - 0.16)/13.50 = 1.04/13.50 = 7.70\%$.

Bridge from the cap rate to the earnings yield:

| Yield | Numerator ÷ denominator | Value |
|---|---|---|
| EV cap rate (unlevered, pre-tax, after reserve) | 1,040 / 13,500 | 7.70% |
| Levered pre-tax cash yield on equity | (1,040 − 240) / 9,600 | 8.33% |
| Levered after-tax cash yield (tax on cash yield) | 800 × 0.79 / 9,600 | 6.58% |
| Earnings yield (accounting D&A of 450, not the 160 reserve) | 402.9 / 9,600 | 4.20% |

The cost of debt is $240/4{,}200 = 5.71\%$, below the 7.70% cap rate, so leverage raises the pre-tax equity yield (positive leverage). Tax then removes 21%, and accounting depreciation of \$450 million instead of the \$160 million economic reserve removes a further \$229 million of after-tax earnings ($290 \times 0.79$).

**Check.** $c_{EV} + (D/E)(c_{EV} - r_D)$ uses net debt: $D_{net} = 3.90$ billion and $E = 9.60$ billion. Interest of 240 on net debt of 3,900 is 6.154%. Then $0.07704 + (3.90/9.60)(0.07704 - 0.06154) = 0.07704 + 0.00630 = 8.33\%$. ✓

**Decision consequence.** A P/E of 23.8x sounds expensive for hotels. A 7.70% cap rate on NOI after reserve sounds like a private-market hotel cap rate. They describe the same price. The decision-relevant comparison for a CRE investor is 7.70% against the cap rate at which comparable private hotels trade, after adjusting for the company's management platform, brand fees, and overhead. The earnings yield is the wrong yardstick for a property investor, and the cap rate is the wrong one for a stock analyst comparing the company with other C-corps. Committee memos that put "P/E 24x" next to "private hotels at 7.5%" without the bridge are comparing different things.

### Example 14.2 — The implied equity risk premium three ways

**Given.** S&P 500 at 6,000. Forward operating EPS 280 index points. Next-year cash distributions (dividends plus net buybacks) 3.00% of price, or 180 points. Long-run nominal growth of distributions 4.50% (Gordon case). Two-stage case: distributions grow 6.00% a year for years 1–5 ($CF_1 = 180$, $CF_5 = 180 \times 1.06^4$), then 4.00% forever. 10-year Treasury 4.25%; 10-year TIPS 2.00%.

**Find.** Gordon and two-stage implied returns and ERPs; the earnings-yield gaps against real and nominal yields.

**Solution.**

*Gordon.* $k = 0.0300 + 0.0450 = 7.50\%$. $ERP = 7.50\% - 4.25\% = 3.25\%$.

*Two-stage.* $CF_5 = 180 \times 1.06^4 = 227.25$. Solve $6{,}000 = \sum_{t=1}^{5} CF_t/(1+k)^t + 227.25 \times 1.04/[(k-0.04)(1+k)^5]$. Bisection gives $k = 7.22\%$, so $ERP = 7.22\% - 4.25\% = 2.97\%$.

*Earnings yield.* Forward $P/E = 6{,}000/280 = 21.43$x and $E/P = 4.67\%$.
Against the real yield: $4.67\% - 2.00\% = 2.67\%$.
Against the nominal yield (Fed model): $4.67\% - 4.25\% = 0.42\%$.

Breakeven inflation $\approx 4.25\% - 2.00\% = 2.25\%$ (exactly $(1.0425/1.02) - 1 = 2.21\%$). The nominal Gordon return of 7.50% is a real return of about 5.2–5.3%, and against TIPS that is an ERP of about 3.2%, consistent with the nominal Gordon ERP.

| Method | Implied return | ERP | What drives it |
|---|---|---|---|
| Gordon, $g = 4.5\%$ | 7.50% nominal | 3.25% vs 10y UST | The perpetual $g$ |
| Two-stage, 6% → 4% | 7.22% nominal | 2.97% vs 10y UST | Terminal $g_2$ and the fade |
| $E/P$ − TIPS | 4.67% real | 2.67% vs TIPS | Assumes $ROE = k$ |
| $E/P$ − nominal UST | — | 0.42% | Mixes real and nominal; not an ERP |

**Check.** Raising the Gordon $g$ by 50 bp raises $k$ and the ERP by exactly 50 bp. The two-stage $k$ lies between the payout yield plus 4% (7.0%) and the payout yield plus 6% (9.0%), and close to the lower end because the terminal value dominates. ✓

**Decision consequence.** The defensible answer to the board member is a range of roughly 2.7–3.3% over the 10-year Treasury, with the spread between methods showing how much of the answer is assumption. The 0.42% "Fed model" gap is the number that makes stocks look expensive, and it is the one comparison that has no theoretical basis. Whether 3% is enough is a judgment about the distribution of equity outcomes, not a valuation fact. A CRE investor should run the same exercise on the hotel book: a 7.00% cap rate with 3.0% NOI growth is a 10.0% unlevered Gordon return, or about 5.75% over the 10-year Treasury (Chapter 9). Item 2 of the committee is therefore a relative-value question between two premia, not a question about whether stocks are expensive.

### Example 14.3 — Fair value of an E-mini future, and notional in two sizes

**Given.** S&P 500 spot 6,000. Financing rate 4.30%, dividend yield 1.30%, both continuously compounded. Three months to expiry ($t = 0.25$). CME E-mini multiplier \$50; Micro E-mini \$5 [FACT; ch14-S01, S02].

**Find.** Fair futures price, basis, and notional per contract for each size.

**Solution.**

$F = 6{,}000 \times e^{(0.043 - 0.013)\times 0.25} = 6{,}000 \times e^{0.0075} = 6{,}000 \times 1.0075282 = 6{,}045.17.$

Basis $F - S = +45.17$ points (positive because the financing rate exceeds the dividend yield).

E-mini notional $= 6{,}045.17 \times 50 = \$302{,}258$. Micro notional $= 6{,}045.17 \times 5 = \$30{,}226$.

**Check.** Simple-interest version: $F = 6{,}000(1 + 0.043 \times 0.25) - 6{,}000 \times 0.013 \times 0.25 = 6{,}064.50 - 19.50 = 6{,}045.00$. The two conventions differ by 0.17 points ($8.5 per E-mini), which is below one tick of 0.25 points. ✓

**Decision consequence.** A hedger who sells futures at 6,045 is not "locking in 6,000". The 45-point basis is the financing the hedger earns in exchange for giving up dividends, and it converges to zero by expiry. A hedger who compares a futures sale price with spot misreads the carry as a gain or loss. In a high-rate environment the basis is large, and each quarterly roll changes it.

### Example 14.4 — Margin is not the position

**Given.** A speculator buys 10 E-mini contracts at 6,045.00. Initial margin \$24,000 per contract and maintenance margin \$21,800 [HYPOTHESIS: margins are set by the exchange and the clearing firm, change with volatility, and must be checked on the day].

**Find.** Notional, leverage on initial margin, the adverse move that triggers a call, and the loss on a 5% decline.

**Solution.**

Notional $= 6{,}045 \times 50 \times 10 = \$3{,}022{,}500$. Initial margin $= 10 \times 24{,}000 = \$240{,}000$. Leverage on margin $= 3{,}022{,}500/240{,}000 = 12.6$x.

Call trigger $= (24{,}000 - 21{,}800)/50 = 44$ points per contract, or $44/6{,}045 = 0.73\%$ of the index.

A 5% decline $= 0.05 \times 6{,}045 = 302.25$ points. Loss $= 302.25 \times 50 \times 10 = \$151{,}125$, which is 63% of initial margin.

**Check.** \$151,125 / \$3,022,500 = 5.0% of notional. ✓

**Decision consequence.** An index move of less than 1% produces a margin call, and an ordinary 5% correction consumes two-thirds of the posted capital. A position sized on margin is a 12.6x levered equity position whatever the trader calls it. The disciplined way to hold futures is to set aside collateral equal to the exposure you intend (for an unlevered position, the full notional in T-bills) and to treat margin as a cash-management detail. The same logic applies to a hotel bought at 85% LTV: the lender's requirement is not your risk budget.

### Example 14.5 — Beta-hedging the REIT sleeve

**Given.** The \$40,000,000 REIT sleeve has an estimated beta of 1.10 to the S&P 500. E-mini fair value 6,045.17 (Example 14.3). Over the next three months, suppose the S&P 500 and the future both fall 10%, and the REIT sleeve falls by its beta times the market move plus a residual of −3%. Ignore carry for this scenario.

**Find.** Contracts to sell; the P&L of the sleeve, the hedge, and the total.

**Solution.**

$N = 1.10 \times 40{,}000{,}000/(6{,}045.17 \times 50) = 44{,}000{,}000/302{,}258 = 145.57$. Sell **146** E-minis. To match more closely, sell 145 E-minis and 6 Micros (0.57 E-mini ≈ 5.7 Micros), for an effective 145.6.

With 146 contracts, the hedge beta is $146 \times 302{,}258/40{,}000{,}000 = 1.103$.

Sleeve return $= 1.10 \times (-10\%) - 3\% = -14\%$. Loss $= \$5{,}600{,}000$.
Futures gain $= 146 \times 50 \times 604.517 = \$4{,}412{,}973$.
Net $= -\$1{,}187{,}027$.

**Check.** The net is the residual, $-3\% \times 40{,}000{,}000 = -\$1{,}200{,}000$, plus the 0.43-contract over-hedge: $0.43 \times 50 \times 604.517 = +\$12{,}973$. ✓

**Decision consequence.** The hedge removed the market move and kept the REIT-specific loss. That is the hedge working correctly. If the committee's worry is "REITs fall because rates rise" rather than "equities fall", the S&P 500 is the wrong hedge instrument, since a rate shock can hit REITs harder than the broad index (Chapter 6). Name the risk first, then choose the instrument whose payoff is driven by that risk.

### Example 14.6 — The lodging REIT's implied cap rate against private marks (Item 1)

**Given.** Share price \$17.50; 210 million shares. Debt \$2.40 billion; preferred \$0.15 billion; cash \$0.20 billion; non-hotel assets \$0.05 billion. Forward hotel NOI after a 4% FF&E reserve, on a cash basis, \$470 million. Your appraiser's private cap rate for similar hotels: 7.00%.

**Find.** Implied cap rate; NAV per share at 7.00%; discount to NAV; GAV/NAV leverage.

**Solution.** Using `sdesk.x_cre_distress.reit_implied_cap_rate` (Chapter 12):

Market cap $= 17.50 \times 210\text{m} = \$3.675$ billion. Implied real-estate value $= 3.675 + 2.40 + 0.15 - 0.20 - 0.05 = \$5.975$ billion. Implied cap $= 470/5{,}975 = 7.87\%$.

At 7.00%: GAV $= 470/0.07 = \$6.714$ billion. NAV $= 6.714 - 2.40 - 0.15 + 0.20 + 0.05 = \$4.414$ billion, or \$21.02 per share. Discount $= 17.50/21.02 - 1 = -16.7\%$. GAV/NAV $= 6.714/4.414 = 1.52$.

**Check.** At the implied cap of 7.866%, GAV $= \$5.975$ billion and NAV $= \$3.675$ billion $= \$17.50$ per share. ✓

**Decision consequence.** The 16.7% "discount" and the 87 bp cap-rate gap are the same fact. Your analyst and the sponsor disagree only about which price is stale. Two tests decide it. (1) Are private hotels actually trading near 7.0%, or is 7.0% an appraisal built from comparables a year old? (2) Is the REIT cheap for reasons unrelated to its hotels: leverage, a dividend cut, index flows, management? If private trades are clearing near 7.8–8.0%, you do not have a public bargain. You have a **mark problem** in your own book: at 7.87%, your \$120 million hotel portfolio would be worth about \$106.8 million ($120 \times 7.00/7.866$), and your \$48 million of equity about \$34.8 million, down 27.5%. The REIT price is a free, fast, noisy appraisal of your own assets. Ignoring it because it is noisy is the anchoring error of Chapter 3.

### Example 14.7 — Hedging the private hotel portfolio's equity beta (Item 3)

**Given.** Private hotel portfolio: gross value \$120 million, debt \$72 million (60% LTV), equity \$48 million. The lodging REIT of Example 14.6 has an equity beta of 1.30 to the S&P 500, measured on weekly returns, at a debt-to-value of 40% [HYPOTHESIS]. Assume debt beta zero, and that the private hotels share the REIT's asset beta. E-mini fair value 6,045.17. Equity risk premium 3.25% (Example 14.2). S&P 500 volatility 18%. Residual volatility of the private equity, after removing the market (property-specific risk plus public–private basis), 30% [HYPOTHESIS]. Horizon to sale: six months.

**Find.** (a) Asset beta, private equity beta, dollar beta, and contracts. (b) Volatility unhedged and hedged. (c) Expected cost of the hedge over six months. (d) Variation-margin outflow if the S&P 500 rallies 15%. (e) Hedged volatility if the true equity beta is 1.40, not 1.95.

**Solution.**

(a) $\beta_A = 1.30 \times (1 - 0.40) = 0.78$. Relevered at 60% LTV: $\beta_E = 0.78/0.40 = 1.95$. Dollar beta $= 1.95 \times 48\text{m} = \$93.6$ million $= 0.78 \times 120\text{m}$. $N = 93{,}600{,}000/302{,}258 = 309.67$; sell **310** contracts. Hedge beta on equity $= 310 \times 302{,}258/48\text{m} = 1.952$.

(b) Unhedged $\sigma_E = \sqrt{(1.95 \times 0.18)^2 + 0.30^2} = \sqrt{0.1232 + 0.0900} = 46.17\%$. Correlation with the market $\rho = 0.351/0.4617 = 0.760$. Hedged $\sigma = \sqrt{(1.95 - 1.952)^2 \times 0.18^2 + 0.30^2} = 30.00\%$. Variance falls 57.8% ($\approx \rho^2$). Volatility falls by a third.

(c) Expected cost $= 93.6\text{m} \times 3.25\% \times 0.5 = \$1{,}521{,}000$.

(d) A 15% rally in the future: loss $= 310 \times 302{,}258 \times 0.15 = \$14{,}055{,}018$, paid in cash as variation margin over the rally, while the hotel appraisal may not move at all.

(e) If the true beta is 1.40, the position before the hedge has $\sigma = \sqrt{(1.40 \times 0.18)^2 + 0.09} = 39.18\%$. After selling 1.952 betas it is short 0.552 beta of the market: $\sigma = \sqrt{(0.552 \times 0.18)^2 + 0.09} = 31.60\%$. The hedge still helps, but now it is partly a market short.

**Check.** Dollar beta is invariant to leverage: $\beta_E E = (\beta_A/0.40)(0.40 \times 120\text{m}) = \beta_A \times 120\text{m}$. ✓

**Decision consequence.** The broker's 310 contracts are arithmetically right and strategically doubtful. The hedge removes about a third of volatility, costs about \$1.5 million in expected terms, and in a rally can demand \$14 million of cash, 29% of the equity, with no offsetting cash from the hotels. The appraisal is smoothed, so the hedge makes reported results **more** volatile. The beta estimate has a wide error band, and the public–private basis can move against you exactly when you sell (Example 14.6). The better responses are cheaper and more targeted: (i) accelerate the sale or sign a contract with a hard deposit, which transfers the residual risk the futures leave behind; (ii) hedge a fraction (for example one-third, about 100 contracts) as catastrophe insurance, with the cash for a 25% rally reserved in advance; (iii) buy index puts, which cap the cost at the premium and do not drain liquidity in a rally (Chapter 18). "Hedge the full beta with futures" is the answer only if liquidity is ample and the sale is certain.

### Example 14.8 — The short: borrow cost, the margin trigger, and an asymmetric payoff (Item 4)

**Given.** Short 20,000 shares at \$50.00 (\$1,000,000). Borrow fee 6% a year on the initial value; one-year horizon; no dividends; ignore the rebate on collateral. Initial margin 50% of the short value, maintenance 30% [HYPOTHESIS: brokers set house requirements at or above regulatory minimums; check the broker's schedule]. The PM's scenarios at one year: \$35 with probability 0.50; \$50 with probability 0.30; \$80 with probability 0.20 (a squeeze).

**Find.** Scenario P&L and EV; the price that triggers a margin call; the account equity at \$80.

**Solution.**

Fee $= 0.06 \times 1{,}000{,}000 = \$60{,}000$.

| Price | Gross P&L $= 20{,}000(50 - P)$ | Net of fee | Probability |
|---|---|---|---|
| \$35 | +300,000 | +240,000 | 0.50 |
| \$50 | 0 | −60,000 | 0.30 |
| \$80 | −600,000 | −660,000 | 0.20 |

$EV = 0.5(240{,}000) + 0.3(-60{,}000) + 0.2(-660{,}000) = 120{,}000 - 18{,}000 - 132{,}000 = -\$30{,}000$.

Expected price $= 0.5(35) + 0.3(50) + 0.2(80) = \$48.50$: an expected decline of 3.0%, against a 6% fee.

Margin call price $= 1.5 \times 50/1.3 = \$57.69$ (+15.4%). At \$80 the collateral is \$1.5 million against a \$1.6 million liability: equity $= -\$100{,}000$. The broker will have bought in the position long before \$80.

**Check.** The PM says the stock is "most likely" going to \$35, and her modal scenario is right. But the expectation includes the squeeze. ✓

**Decision consequence.** The PM's view has a positive mode and a negative mean. The short loses money in expectation once borrow is paid, and the 20% squeeze state reaches the margin trigger on the way. The right answer is **not to short at this size**. The alternatives are a defined-loss structure (a put or put spread, Chapter 18), a much smaller short sized so that a forced cover at +60% is tolerable, or a pair trade against a less overvalued peer that reduces the squeeze exposure. Abstaining is a position: it keeps capital for the trades where the mean, not the mode, is favorable.

---

## 14.6 CRE application: REITs as listed CRE, and what to do with the signal

The three CRE uses of equity markets in this chapter fit together.

**1. Use REIT prices as a fast appraisal of private assets.** Example 14.6 turns a share price into a cap rate. Do it routinely for the property types you own, with consistent NOI definitions: cash NOI after reserve, forward, excluding non-property income. Then de-lever the public move before you compare it with private marks. A REIT whose equity falls 20% at GAV/NAV of 1.5 implies an asset-value fall of about 13% (Chapter 12, drill D113). Keep a log of the implied cap minus the appraisal cap for each sector. A persistent positive gap with collapsing transaction volume is the classic signature of appraisal lag (Chapter 2).

**2. Use the gap to make decisions, not to make bets.** A positive gap (public implied cap above private) supports: deferring private acquisitions; selling private assets to buyers who still pay private prices; buying REIT shares **only** with a catalyst (buybacks funded by asset sales at private prices, take-private interest, activist pressure). A negative gap (public premium) supports the reverse: REITs can issue equity and buy private assets accretively, and they will compete with you on bids.

**3. Hedge the market factor only when the factor is the risk.** Private CRE equity has a market factor, through financing conditions, capital flows, and the economy. Index futures hedge that factor, cost the ERP, and require liquidity. They do not hedge property-specific risk, the public–private basis, or the risk that the appraisal is stale. Example 14.7 shows a full beta hedge removing only about a third of volatility. For a planned sale, the hedge that transfers the most risk is a signed contract. For a long hold, the hedge is usually not worth its expected cost unless it prevents a forced sale.

**Sector betas are estimates.** Lodging REITs carry high operating leverage (Chapter 11) and have historically shown higher equity betas than net-lease or industrial REITs [HYPOTHESIS as a general statement; estimate betas from your own return data, with the window and frequency stated]. Weekly betas over two to three years are a common compromise between noise and staleness. Recompute them after any regime change in rates.

---

## 14.7 Momentum, breadth, earnings events, and leverage: how they enter a CRE decision

**Momentum.** Jegadeesh and Titman (1993; ch14-S12) documented that U.S. stocks that outperformed over the previous 3–12 months tended to continue outperforming over the next 3–12 months. Part of the abnormal return reversed in the following two years. Time-series momentum applies the idea to an index's own trend. Momentum strategies have also suffered abrupt crashes when trends reverse sharply [INFERENCE from the reversal finding; the magnitude of specific crash episodes is not used in this chapter]. For a CRE investor, the relevance is that capital flows into listed real estate trend. A REIT sector in a strong 12-month downtrend will often keep falling for reasons unrelated to cap rates, which makes the "public discount" in §14.6 more persistent than valuation alone predicts.

**Breadth.** When an index is carried by a few large members (Problem 14.7), two things follow. First, the index's earnings yield is dominated by those members, so the ERP of §14.4.2 is mostly a statement about them. Second, an investor who sells futures to hedge a portfolio of mid-sized REITs is short a basket that is mostly technology and large-cap growth. The basis in Example 14.7 widens.

**Earnings and corporate events.** Earnings announcements, guidance changes, M&A, spin-offs, index inclusions and deletions, and secondary offerings move individual shares on dates you can schedule. For a REIT they include dividend changes and NAV updates. Post-earnings-announcement drift (Bernard and Thomas, 1989; ch14-S13) means prices have historically not fully adjusted on the day. Problem 14.6 shows that a beat on current EPS can still lower the price if the forward EPS and the multiple are revised. Treat corporate events as information about the cash flows and the multiple separately. Equity issuance by a REIT at a premium to NAV is accretive and tends to precede new competition for private acquisitions. Buybacks at a discount are the catalyst that makes a public discount capturable.

**Leverage.** Equity investors use leverage through margin accounts (§14.4.4), futures (Example 14.4), options, and leveraged ETFs. The arithmetic is the same as CRE leverage, with a different clock: margin calls are daily, CRE loan covenants are tested quarterly, and CRE refinancing happens at maturity. A 50%-margin stock position is called after a 33% fall. An 85%-LTV property's equity is gone after a 15% fall, but no one calls the loan until a covenant test or a maturity. Both are the same exposure; only the timing of the forced sale differs.

---

## 14.8 When the relationship fails

1. **Cost of carry fails when the cash market cannot trade.** The futures–cash arbitrage of §14.4.3 requires that stocks can be bought and sold at quoted prices. On 19–20 October 1987, many NYSE stocks opened late or did not trade, and S&P 500 futures traded at large discounts to the reported cash index (Brady Report; Chapter 1 §1.9; the size of the discount in index points is *(verification pending)*). The "discount" was partly stale cash prices and partly a genuine breakdown of arbitrage capital. A hedger who sells futures in such a market sells at a price below the value of the asset being hedged.
2. **Beta is not stable.** Betas measured in calm periods understate co-movement in crises, when correlations rise (Chapter 13, Example 13.3). A hedge sized on a 0.6 correlation can find itself facing 0.9, which helps the hedge. It can also face the reverse: REITs rising on falling rates while the broad index falls on recession fears, so both legs lose.
3. **Implied ERP fails when $g$ is unknowable.** A two-stage model with 6% growth is not an estimate in a technology transition or a pandemic. Use scenarios and report the range.
4. **The earnings yield fails when earnings are not representative.** At cyclical peaks, $E/P$ is high relative to normalized earnings. In recessions, reported earnings collapse and $E/P$ falls exactly when expected returns are highest. CAPE corrects for this but carries ten years of old accounting.
5. **Short-sale arbitrage fails when shares cannot be borrowed.** Lamont and Thaler (2003; ch14-S09) document a case in which a parent company traded below the value of its holding in a subsidiary. The arbitrage required shorting the subsidiary, and borrow was scarce and expensive (§14.9). Mispricing that needs a short can persist for months.
6. **REIT implied cap rates fail as private signals** when REIT prices are driven by fund flows, index events, or a REIT-specific problem. They also fail when the REIT's assets are not comparable to yours (different markets, brands, or lease terms).
7. **Momentum fails abruptly.** Trend-following positions are short the reversal. The losses arrive in a few weeks after long periods of gains.

---

## 14.9 Historical episode: the technology bubble, 1998–2002

**Date and environment.** The U.S. economy expanded through the late 1990s. The FOMC raised the federal funds target through 1999 and into 2000, reaching 6½% with a 50 bp increase on 16 May 2000 [FACT; ch14-S07]. It cut by 50 bp on 3 January 2001 [FACT; ch14-S07]. In early 2000 the 10-year TIPS yield stood near 4.3%, the highest since TIPS were first issued in 1997 [FACT; ch14-S06].

**Price behavior.** The Nasdaq Composite first closed above 5,000 on 9 March 2000 and set a closing high of 5,048.62 on 10 March 2000 [FACT; ch14-S03]. It closed at 1,114.11 on 9 October 2002 [FACT; ch14-S03]. The decline was

$$1{,}114.11/5{,}048.62 - 1 = -77.9\%,$$

and recovering the peak from the low required a gain of $5{,}048.62/1{,}114.11 - 1 = +353\%$. The index did not close above its 2000 high until 23 April 2015, at 5,056.06 [FACT; ch14-S03], about fifteen years later. The S&P 500 set a record close of 1,527.46 on 24 March 2000 and fell about 49% to its October 2002 low [FACT; ch14-S04; the exact closing low, reported as 776.76 on 9 October 2002, is *(verification pending)*].

**Valuation knowable at the time.** Shiller's cyclically adjusted P/E for the S&P 500 reached about 44.2 in December 1999, its highest on record [FACT; ch14-S05]. That is a CAPE earnings yield of $1/44.2 = 2.26\%$. Set against a TIPS yield of about 4.3%, the **CAPE earnings yield was about 2.0 percentage points below the real risk-free yield** [INFERENCE: arithmetic on two sourced figures, $2.26\% - 4.30\% = -2.04\%$; the dates differ by a few weeks]. On the §14.4.2 logic, equities offered a lower expected real return than an inflation-protected government bond unless earnings growth and reinvestment returns were going to be far above history. This was public information. Every input came from published prices and earnings.

**IPOs and issuance.** Ritter's IPO data show 446 IPOs with offer prices of at least \$8 in 1999, with an average first-day return of 70.9% [FACT; ch14-S08]. In a later tabulation, IPOs in 1999–2000 averaged a first-day return of 64.6%, against 14.8% in 1990–1998 [FACT; ch14-S08]. First-day returns of that size mean that issuers sold shares well below the price at which the market would trade them, and that allocations were valuable to whoever received them. Large IPO volume is also new **supply** of shares. Ofek and Richardson (2003; ch14-S10) argue that short-sale constraints held internet stock prices up while optimists set the price, and that the expiry of IPO lock-ups (which released insider shares for sale) coincided with the collapse.

**Short-sale constraints in a single case.** In March 2000, 3Com sold a minority of Palm in an IPO and announced that it would distribute its remaining Palm shares, about 1.5 Palm shares per 3Com share (1.525 precisely). On Palm's first trading day, the Palm shares implied a 3Com value of at least \$145, while 3Com traded at \$81.81 [FACT; ch14-S09]. The **stub value** of 3Com's other businesses was therefore about

$$81.81 - 145 = -\$63 \text{ per share},$$

a negative price for a company with real assets. The arbitrage (buy 3Com, short 1.5 Palm) required borrowing Palm shares, which was difficult and expensive [FACT; ch14-S09]. The mispricing persisted for weeks.

**Real estate in the same decade.** Nareit reported that \$10,000 invested in its equity REIT index at the start of 2000 grew to \$27,454 by the end of 2009, against \$9,090 for the S&P 500 [FACT; ch14-S16]. That is a compound annual return of $(2.7454)^{1/10} - 1 = 10.6\%$ against $(0.909)^{1/10} - 1 = -0.95\%$. REITs entered the decade priced on cash yields at a time when the broad market was priced on growth. [INFERENCE: the decade comparison does not separate the valuation starting point from the decade's later credit boom in real estate, which contributed to REIT returns before 2007.]

**Competing interpretations.** (i) **Rational exuberance:** the internet was a genuine technological shift, and expected growth justified high multiples for the eventual winners. Some winners did justify their valuations, but the index as a whole did not. (ii) **Limits to arbitrage:** prices reflected optimists because pessimists could not short cheaply (Ofek and Richardson; Lamont and Thaler). (iii) **Monetary and real-rate conditions:** a 4%+ real yield was a visible, rising hurdle, and the bubble deflated as the FOMC tightened into 2000 [INFERENCE: timing coincidence, not a demonstrated cause]. These are not mutually exclusive.

**What was knowable then, and what was not.** The level of CAPE, the negative gap to TIPS, the IPO first-day returns, and the cost of shorting were all public. What was not knowable was **when** the price would turn. Nasdaq rose substantially in 1999, after valuation measures were already extreme. A short seller in mid-1999 faced borrow costs, recalls, and margin calls (Example 14.8) through a further large rise.

**What the case establishes and does not.** It establishes that valuation measures can sit at extremes for a year or more before prices respond. It shows that short-sale constraints can sustain obvious mispricing. It shows that a long-horizon investor who used the real-yield comparison would have avoided the worst of the drawdown and owned assets (REITs, TIPS) that did well. It does **not** establish that high CAPE predicts a crash within any particular horizon, or that the same comparison will work in a period of low real yields. It does not show that any rule could have timed the peak.

**CRE connection.** In 1999–2000 the listed market priced technology on growth and real estate on yield. A CRE investor who read the REIT implied cap rate against TIPS saw a positive spread. One who read the Nasdaq earnings yield against TIPS saw a negative one. The skill this chapter teaches is to state every asset's expected return in the same currency (real, after costs, at stated leverage) before arguing about which is cheap.

---

## 14.10 Decision exercise: the committee's four items

Using the decision record template at `desk/investment_memos/decision_record_template.md`, answer each item.

1. **Item 1 (REIT vs private marks).** Do you buy the lodging REIT, write down your own hotels, both, or neither? State what private transaction evidence would change your answer, and the size you would buy without a catalyst.
2. **Item 2 (equities vs bonds).** Give the implied ERP as a range with methods (Example 14.2). Compare it with your hotel book's implied premium over Treasuries. Recommend an allocation shift, or none, with the evidence that would reverse it.
3. **Item 3 (the hedge).** Accept, resize, restructure (puts, partial hedge, or a REIT short), or reject the broker's 310-contract hedge. State the liquidity reserve required for a 25% rally and the expected cost.
4. **Item 4 (the short).** Approve, resize, restructure, or decline. Give the EV after borrow, the margin-call price, and the maximum loss you would accept.

**Rubric.** Full credit requires: (a) Item 1 stated as a cap-rate disagreement, with the stale-price question asked and a catalyst named, or the position sized small. A write-down of your own marks considered explicitly. (b) Item 2 answered with a range and with the Fed-model comparison rejected or caveated. (c) Item 3: dollar beta computed on gross assets, residual risk and expected cost quantified, a cash reserve for variation margin sized, and a signed sale contract or puts considered as alternatives. (d) Item 4: the mean distinguished from the mode, borrow cost included, and abstention or a defined-loss structure considered. There is no single correct allocation. A response that hedges the full beta with futures and shorts the full \$1 million without liquidity analysis fails (c) and (d) however good the market outcome turns out to be.

---

## 14.11 Frequent analytical errors

1. **Comparing a P/E with a cap rate.** Bridge them: leverage, tax, and depreciation versus reserve (Example 14.1).
2. **Using the wrong multiplier.** E-mini \$50, Micro \$5. A factor-of-ten error turns a hedge into a speculation.
3. **Treating margin as the position.** Leverage is notional divided by capital at risk, not by the exchange's margin.
4. **Reading the futures basis as a gain or loss.** It is carry, and it converges to zero at expiry.
5. **Hedging equity dollars instead of beta dollars.** Size on $\beta_E E = \beta_A V$. A REIT beta must be unlevered and relevered.
6. **Forgetting the hedge's expected cost.** Selling beta gives up the ERP.
7. **Ignoring variation-margin liquidity** against a smoothed, illiquid asset.
8. **Quoting a single ERP to one decimal.** Present methods and a range. Do not use the nominal "Fed model" gap as an ERP.
9. **Shorting on the mode.** The mean includes the squeeze, and borrow cost, recall, and the margin trigger cut against the short.
10. **Reading a REIT discount as a bargain without asking which price is stale** (Chapter 12).
11. **Reading index strength as broad strength.** Check equal-weighted returns and advancers versus decliners.
12. **Reacting to the EPS beat rather than the forward revision.** The price is forward EPS times the multiple.

---

## 14.12 Connections to other chapters

* Chapter 1: the 1987 futures–cash episode, leverage arithmetic, and the expected-versus-modal distinction used in Example 14.8.
* Chapter 2: appraisal smoothing, which explains why the private mark lags the REIT price.
* Chapter 3: anchoring on one's own marks; reflexive forced selling under margin.
* Chapter 5: real rates and policy; the 2000 tightening cycle.
* Chapter 6: real yields, TIPS, and the cap-rate–Treasury spread used to compare premia.
* Chapter 9: $c = k - g$, the CRE version of the Gordon ERP.
* Chapter 11: hotel EBITDA, NOI after reserve, and operating leverage behind lodging betas.
* Chapter 12: REIT implied cap rates and NAV (`sdesk.x_cre_distress`).
* Chapter 13: portfolio volatility, correlation in stress, and Treasury-futures hedges with basis risk.
* Chapter 15: hedged returns on foreign property use the same carry logic in FX.
* Chapter 18: puts as an alternative hedge with a defined cost; delta hedging.
* Chapter 21: sizing, margin stress, and ruin.
* Chapter 23: 1987, 2000, and 2008 in full.

---

## 14.13 One-page reference sheet

| Formula | Expression |
|---|---|
| EV | Mkt cap + debt + preferred + minority − cash |
| EV cap rate | $(EBITDA - \text{capex}_{maint})/EV$ |
| Cap from multiple | $(1/\text{multiple})(1 - \rho/\mu)$ |
| Levered equity yield (pre-tax) | $c + (D/E)(c - r_D)$ |
| Gordon implied return | $k = D_1/P + g$; $ERP = k - y$ |
| Two-stage | $P = \sum_{t=1}^n CF_t/(1+k)^t + CF_n(1+g_2)/[(k-g_2)(1+k)^n]$ |
| $E/P$ as real return | $k = E/P$ only if $ROE = k$ |
| Futures fair value | $F = S(1+rt) - D$; $F = Se^{(r-q)t}$ |
| No-arbitrage band | $F^* \pm \kappa$ |
| Notional, P&L | $F m N$; side $\times \Delta F \times m \times N$ |
| CME S&P 500 | E-mini \$50/pt, tick 0.25 = \$12.50; Micro \$5/pt, tick = \$1.25 |
| Margin-call move | $(IM - MM)/m$ points |
| Long margin call | $P^* = (1-m_0)P_0/(1-m_m)$ |
| Short margin call | $P^* = (1+m_0)P_0/(1+m_m)$ |
| Beta hedge | $N = \beta V/(F m)$ |
| Asset beta | $\beta_A = \beta_E E/V + \beta_D D/V$ |
| Hedged vol | $\sqrt{(\beta-\beta_h)^2\sigma_m^2 + \sigma_\varepsilon^2}$ |
| Hedge expected cost | $\beta V \times ERP \times t$ |
| REIT implied cap | $NOI_{fwd}/(\text{Mkt cap} + D + \text{Pref} - \text{Cash} - \text{Other})$ |
| SUE | $(A - C)/\sigma_{surprise}$ |
| Price from revisions | $P_1/P_0 = (E_1/E_0)((P/E)_1/(P/E)_0)$ |

**Rules of thumb (to be tested, not trusted).** At 50% initial and 25% maintenance, a margined long is called after a 33% fall. At 50%/30%, a short is called after a 15% rise. A full beta hedge removes only the $\rho^2$ share of variance. For a private CRE asset, $\rho$ is rarely high enough to make that share large. One E-mini at an index of 6,000 is about \$300,000 of exposure.

---

## References for this chapter

All sources are listed in `references/sources_ch14.md` with verification status.

* CME Group. E-mini S&P 500 futures contract specifications; Micro E-mini S&P 500 futures overview. https://www.cmegroup.com (accessed 2026-10-19).
* Asness, C. S. (2003). "Fight the Fed Model." *Journal of Portfolio Management*, 30(1), 11–24.
* Bernard, V. L., and Thomas, J. K. (1989). "Post-Earnings-Announcement Drift: Delayed Price Response or Risk Premium?" *Journal of Accounting Research*, 27 (Supplement), 1–36.
* Gordon, M. J. (1959). "Dividends, Earnings, and Stock Prices." *Review of Economics and Statistics*, 41(2), 99–105 *(bibliographic details pending check)*.
* Jegadeesh, N., and Titman, S. (1993). "Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency." *Journal of Finance*, 48(1), 65–91.
* Lamont, O. A., and Thaler, R. H. (2003). "Can the Market Add and Subtract? Mispricing in Tech Stock Carve-outs." *Journal of Political Economy*, 111(2), 227–268.
* Ofek, E., and Richardson, M. (2003). "DotCom Mania: The Rise and Fall of Internet Stock Prices." *Journal of Finance*, 58(3), 1113–1137.
* Board of Governors of the Federal Reserve System. Press release, 16 May 2000.
* Ritter, J. R. IPO statistics (University of Florida), as reproduced by PBS *Frontline*, "Dot Con" (2002), and in Ritter's "Some Factoids about the 2006 IPO Market."
* Cambridge Associates (2000). *U.S. Treasury Inflation-Protected Securities*.
* Nareit (2010). Press release on decade REIT returns, 2000–2009.
* Shiller, R. J. Online data (CAPE series).
* Presidential Task Force on Market Mechanisms (1988). *Report* ("Brady Report"). See Chapter 1.
* U.S. Securities and Exchange Commission. Regulation SHO (Release No. 34-50103, 2004; Rule 201, 2010).
