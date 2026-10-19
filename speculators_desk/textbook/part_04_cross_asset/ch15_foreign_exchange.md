# Chapter 15 — Foreign Exchange

> **Status:** Complete (v1.0). Numerical examples, problems, and solutions are reproduced in `tests/test_ch15_examples.py`. Problems are in `problems/questions/ch15_problems.md` and solutions in `problems/solutions/ch15_solutions.md`. Drills D143–D149 are in `training/daily_drills/drill_bank_ch15.json`. Sources are in `references/sources_ch15.md`. Some figures in the historical episode (§15.9) are *(verification pending)* and are marked where they appear.

## Learning objectives

After this chapter you should be able to:

1. Read any currency quote as BASE/QUOTE, convert it in either direction, count pips, value a pip in your own currency, and state which currency appreciated. Do this without error under time pressure, because the most expensive FX mistakes are sign mistakes.
2. Build cross rates and cross bid–ask spreads from two dollar pairs, and detect a triangular mispricing.
3. Derive the covered-interest-parity (CIP) forward from a riskless replication, compute forward points with the correct day-count conventions, and measure the cross-currency basis that makes the market forward differ from the CIP forward.
4. Decompose carry-trade P&L into carry, spot, and cross terms. Compute the break-even crash probability and explain why a strategy with positive expected return can have a return distribution that most investors should not hold at leverage.
5. Explain first-generation (fundamentals run out) and second-generation (self-fulfilling) currency crises in intuitive form, compute the timing of an attack in a stylized first-generation model, and compute why an interest-rate defense cannot deter a short-horizon speculator once credibility is lost.
6. Explain what central-bank intervention can and cannot do, and why a defender of a weak currency faces a reserve constraint that a defender of a strong currency does not.
7. Hedge a foreign real estate investment with rolling forwards: compute the cash settlement at each roll, show that a rolling hedge re-strikes at spot each year, and choose a hedge ratio that balances variance reduction against the liquidity cost of cash calls.

---

## 15.1 Opening investment problem: the London hotel and the hedge committee

You are the head of acquisitions for a U.S. dollar fund. All figures in this section are [HYPOTHESIS]. A 180-room full-service hotel in London is offered at £50.0 million. Stabilized NOI after a 4% FF&E reserve is £3.5 million, a 7.0% cap rate on NOI. A U.K. lender will provide a £27.5 million interest-only loan (55% LTV) at 6.00% fixed for three years. Your equity is £22.5 million. At spot GBP/USD 1.2700 that is \$28,575,000. The business plan is a three-year hold.

The money markets show one-year rates of 4.25% in dollars and 4.75% in sterling. The fund's treasury team asks three questions before the investment committee:

1. **Do we hedge the currency?** If we sell sterling forward, what does the hedge cost, and what is it actually protecting?
2. **With what instrument and tenor?** A three-year forward matched to the business plan, or one-year forwards rolled annually? What happens at each roll?
3. **At what hedge ratio?** The fund holds a \$2.0 million liquidity reserve for this deal. If sterling rallies 18% in a year, a fully hedged position must pay about \$5.1 million in cash at the roll. Where does that money come from?

On the same morning a colleague on the macro desk pitches a yen-funded carry trade: borrow yen at 0.50%, buy dollars yielding 4.25%, "collect 3.75% a year". And the research team circulates a note on a small open economy whose currency peg "has held for eight years", where a hotel developer is offering an 11% local-currency yield.

The three proposals share one piece of arithmetic: interest parity. They differ in what the investor is betting on. By §15.10 you will be able to state, for each, which bet is being made and what it costs.

---

## 15.2 Economic intuition

**An exchange rate is the relative price of two monies.** It moves when the relative demand to hold one money's assets changes. That demand depends on relative interest rates, expected inflation, perceived safety, capital controls, and the balance of payments. None of these is a property of a building in London. Yet a U.S. investor's dollar return on that building depends on all of them. The currency return is often larger than the property return over a three-year hold. For a property investor, currency is usually an unwanted exposure that rides along with a wanted one.

**A forward is a financing trade, not a forecast.** The forward price is set by what it costs to replicate it: borrow one currency, convert at spot, lend the other. It therefore reflects the interest-rate differential. A forward that shows sterling 0.48% cheaper in a year does not mean the market expects sterling to fall 0.48%. It means sterling deposits pay 0.50 points more than dollar deposits. Covered interest parity (CIP) is an arbitrage relation, enforced by dealers when their balance sheets allow. Uncovered interest parity (UIP), the claim that the expected spot rate equals the forward, is a hypothesis about expectations and risk premia. It fails badly in the data (§15.8).

**Carry is the premium for bearing crash risk.** Because UIP fails, borrowing in low-rate currencies and lending in high-rate currencies has earned a positive average return in many samples. The return distribution is negatively skewed: small, steady gains punctuated by sudden losses when funding currencies rally, usually when risk appetite collapses and leveraged holders unwind together (Brunnermeier, Nagel, and Pedersen, 2009) [FACT: ch15-S04]. The carry trader is selling insurance against a disorderly world.

**A peg is a promise backed by a balance sheet and a political willingness to bear pain.** A central bank defending a weak currency sells foreign-currency reserves, and those reserves are finite. A central bank capping a strong currency sells its own currency, of which it has an unlimited supply. The two cases are not symmetric. When markets come to doubt that the government will keep paying the cost of defense, the cost of defense rises, and the doubt becomes self-fulfilling.

**Capital flows close the identity.** A country running a current-account deficit must attract an equal net inflow of capital or run down reserves. When inflows are hedged foreign investors, their demand depends on hedging costs. When inflows are short-term and unhedged, they can reverse abruptly. For real estate, the marginal foreign buyer of a property is often the marginal provider of capital to that country, and their behavior depends on interest differentials that have nothing to do with the property.

**Hedging transports a spread, not a yield.** A yen investor who hedges a 7.5% U.S. hotel yield back to yen does not earn 7.5%. Under CIP the investor earns the hotel's spread over U.S. short rates, added to yen short rates. §15.4.6 derives this. Most foreign-buyer mistakes in CRE come from comparing a foreign yield with a home yield without making this adjustment.

---

## 15.3 Technical definitions

| Term | Definition |
|---|---|
| BASE/QUOTE | A pair quoted at $S$ means 1 unit of BASE costs $S$ units of QUOTE. EUR/USD 1.0850: €1 = \$1.0850. USD/JPY 150.00: \$1 = ¥150.00 |
| Direct quote | Home-currency units per unit of foreign currency (home is QUOTE). For a U.S. investor, EUR/USD and GBP/USD are direct |
| Indirect quote | Foreign-currency units per unit of home currency (home is BASE). For a U.S. investor, USD/JPY and USD/CHF are indirect |
| Pip | Smallest conventional increment: 0.0001 for most pairs, 0.01 for JPY-quoted pairs |
| Pip value | Notional in BASE × pip size, in QUOTE currency. €10 million of EUR/USD: \$1,000 per pip |
| Cross rate | A rate between two non-USD currencies derived from their dollar rates, e.g. EUR/JPY = EUR/USD × USD/JPY |
| Outright forward | Price agreed today for exchange at a future date |
| Forward points | $(F - S)$ expressed in pips. Negative points: BASE trades at a forward discount |
| Covered interest parity (CIP) | $F = S(1+r_Q\tau_Q)/(1+r_B\tau_B)$ with money-market rates and their own day counts |
| Cross-currency basis $b$ | Spread added to the non-USD money-market rate so that CIP matches the market forward. Nonzero for major pairs since 2008 (Du, Tepper, and Verdelhan, 2018) [FACT: ch15-S03] |
| Uncovered interest parity (UIP) | $E[S_T] = F$: the forward is an unbiased forecast. Empirically rejected (Fama, 1984) [FACT: ch15-S05] |
| Carry trade | Borrow a low-yield currency, invest in a high-yield currency, unhedged |
| Policy-rate differential | Difference between two central banks' policy rates; the main driver of short-dated forward points |
| Rolling hedge | A sequence of short-dated forwards, each settled at maturity and replaced at the then-current forward |
| Hedge ratio $h$ | Hedged notional ÷ exposure. $h = 0$ unhedged; $h = 1$ fully hedged on the measured exposure |
| Sterilized intervention | FX purchase or sale whose effect on domestic money is offset by an open-market operation |
| First-generation crisis | A peg collapses because policy (e.g. credit-financed deficits) is inconsistent with it; timing is set by reserves (Krugman, 1979) [FACT: ch15-S01] |
| Second-generation crisis | A peg the government could defend is abandoned because defense is too costly once the market expects devaluation; multiple equilibria (Obstfeld, 1996) [FACT: ch15-S02] |
| Sudden stop | Abrupt reversal of net capital inflows forcing a current-account adjustment |

---

## 15.4 Equations and derivations

### 15.4.1 Quote direction

For pair BASE/QUOTE at rate $S$:

* Converting BASE to QUOTE multiplies by $S$. Converting QUOTE to BASE divides by $S$. (`sdesk.markets.convert`.)
* A rise in $S$ means BASE **appreciated** and QUOTE **depreciated**.
* The inverse pair QUOTE/BASE trades at $1/S$. Percentage changes are **not** symmetric: if $S$ moves from $S_0$ to $S_1$, BASE changes by $S_1/S_0 - 1$ in QUOTE terms, and QUOTE changes by $S_0/S_1 - 1$ in BASE terms. A 5% rise in EUR/USD is a 4.76% fall in the dollar measured in euros.
* Inverting a two-way quote swaps the sides: if EUR/USD is $b/a$, then USD/EUR is $1/a$ bid, $1/b$ ask.
* P&L on a position of $N$ units of BASE is earned in QUOTE: $\Pi_Q = \text{side} \times N (S_1 - S_0)$ (`sdesk.markets.fx_pnl`). To report it in BASE, divide by the closing rate $S_1$.

**Test the direction every time.** Ask: "One unit of which currency costs how many units of which?" Then ask: "Which way does my home value of one foreign unit move?" For a U.S. investor holding yen assets, the home value of ¥1 is $1/S_{USD/JPY}$, so a rise in USD/JPY *hurts*.

### 15.4.2 Cross rates and the cross spread

From two dollar pairs:

$$\text{EUR/JPY} = \text{EUR/USD} \times \text{USD/JPY}, \qquad \text{EUR/GBP} = \frac{\text{EUR/USD}}{\text{GBP/USD}}.$$

The rule is to chain the pairs so that the dollar cancels. For two-way prices, the cross bid is the worst rate at which you can sell the cross BASE through the two legs, and the cross ask is the worst rate at which you can buy it:

* Multiplicative cross: bid = bid × bid; ask = ask × ask.
* Divisive cross (common QUOTE): bid = bid$_1$ / ask$_2$; ask = ask$_1$ / bid$_2$.

A direct dealer quote for the cross outside the synthetic spread is a triangular mispricing. In liquid pairs such quotes disappear within milliseconds. On a slow screen they are usually stale prices, not opportunities.

### 15.4.3 Policy-rate differentials and the front end

Short-dated money-market rates in each currency sit close to the policy rate of its central bank (Chapter 5). Short-dated forward points are therefore driven mainly by the **policy-rate differential** and by the market's expected path of each central bank over the forward's tenor. Two consequences follow:

1. A central-bank meeting moves forward points, and therefore hedge costs, before it moves the spot rate in any predictable way.
2. Hedging cost is a front-end rate differential even when the hedged asset is long-dated (Chapter 7, §7.4.7). A 10-year Treasury or a hotel with a 10-year hold is usually hedged with 1- to 12-month forwards.

### 15.4.4 Covered interest parity: derivation

Take pair BASE/QUOTE at spot $S$. Money-market rates are $r_B$ and $r_Q$, simple interest, with accrual fractions $\tau_B$ and $\tau_Q$ under each currency's day count. Two ways of holding QUOTE currency at time $T$ starting from 1 unit of BASE today:

* **Route 1.** Deposit 1 BASE: receive $1 + r_B\tau_B$ BASE at $T$. Sell it forward today at $F$: $F(1 + r_B\tau_B)$ QUOTE at $T$.
* **Route 2.** Sell 1 BASE spot for $S$ QUOTE. Deposit: $S(1 + r_Q\tau_Q)$ QUOTE at $T$.

Both routes are riskless and fixed today. If they differed, one could borrow on one route and lend on the other. Therefore

$$\boxed{F = S\,\frac{1 + r_Q\,\tau_Q}{1 + r_B\,\tau_B}}$$

and the **forward points** are

$$F - S = S\,\frac{r_Q\tau_Q - r_B\tau_B}{1 + r_B\tau_B} \approx S\,(r_Q - r_B)\,\tau.$$

The currency with the **higher** interest rate trades at a forward **discount**. That is the arbitrage, not a forecast.

**Day counts.** USD, EUR, JPY and CHF money markets use ACT/360. GBP uses ACT/365. Ignoring the difference on a 182-day sterling forward misprices it by several pips (Example 15.3). `sdesk.markets.covered_interest_forward(spot, r_quote, r_base, t)` uses one accrual fraction for both legs. To use it with mixed conventions, put the day-count ratio into the rate: pass $r_B \times 360/365$ with $t = \text{days}/360$ for a GBP base.

**The basis.** Since 2008 the market forward has differed persistently from the CIP forward for major currencies, with the gap largest at quarter-ends and in stress (Du, Tepper, and Verdelhan, 2018) [FACT: ch15-S03]. Write the market forward as

$$F^{mkt} = S\,\frac{1 + r_{USD}\tau}{1 + (r_{X} + b)\tau}\quad\text{(pair X/USD)},\qquad F^{mkt} = S\,\frac{1 + (r_{X} + b)\tau}{1 + r_{USD}\tau}\quad\text{(pair USD/X)}.$$

Here $b$ is the cross-currency basis on the non-dollar rate. A **negative** $b$ means that obtaining dollars synthetically (borrowing currency X and swapping into dollars) costs more than borrowing dollars directly. For a hedger the consequence is: a dollar investor hedging a euro or yen asset back into dollars earns *more* than the rate differential implies, and a euro or yen investor hedging a dollar asset earns *less* (Example 15.6). The CIP forward is a reference point. The market forward is the price you pay.

### 15.4.5 Uncovered interest parity and carry P&L

Borrow $N$ units of a funding currency at $r_f$; convert at spot $S_0$ (pair INV/FUND, so one unit of the investment currency costs $S_0$ units of funding currency); invest at $r_i$; convert back at $S_T$. Profit in the funding currency over one period of length $\tau$:

$$\Pi = N\left[(1 + r_i\tau)\frac{S_T}{S_0} - (1 + r_f\tau)\right].$$

Writing $s = S_T/S_0 - 1$:

$$\Pi = \underbrace{N(r_i - r_f)\tau}_{\text{carry}} + \underbrace{N s}_{\text{spot}} + \underbrace{N r_i \tau\, s}_{\text{cross}}.$$

The three terms are an exact identity. The break-even terminal spot is the CIP forward, $S_T^* = S_0(1+r_f\tau)/(1+r_i\tau) = F$. **Under UIP, expected carry profit is zero.** Carry is profitable on average only to the extent that high-yield currencies depreciate by less than the forward implies.

**Crash risk.** Suppose in each month the trade earns carry $c$ with probability $1-p$, and with probability $p$ the investment currency falls by $d$, producing a monthly result $L < 0$. Expected monthly profit is $(1-p)c + pL$. The break-even crash probability is

$$p^* = \frac{c}{c - L}.$$

If $c$ is 0.31% a month and a crash costs about 7.7%, $p^*$ is about 3.9% a month (Example 15.5). Over a year there is roughly a 30% chance of at least one crash at $p = 3\%$. The trade looks excellent in about seven years out of ten, and that is the problem: a short track record cannot distinguish $p = 1\%$ from $p = 5\%$, and the decision turns on that difference.

### 15.4.6 Hedged returns: hedging transports the spread

Chapter 7 derived the one-period hedged return. With home short rate $r_h$, foreign short rate $r_f$, and foreign-currency asset return $y$, a full hedge of the terminal amount under CIP gives

$$1 + R_{hedged} = (1 + y)\,\frac{1 + r_h}{1 + r_f}\quad\Longrightarrow\quad \frac{1 + R_{hedged}}{1 + r_h} = \frac{1 + y}{1 + r_f}.$$

The second form is the useful one. **The hedged asset's excess return over the home short rate equals its excess return over the foreign short rate.** A U.S. hotel at a 7.5% yield with U.S. short rates at 4.25% offers a gross spread ratio of $1.075/1.0425 = 1.0312$. Hedged into yen at 0.50% it yields $1.005 \times 1.0312 - 1 = 3.63\%$. A Japanese hotel yielding 4.0% has spread ratio $1.04/1.005 = 1.0348$, which is *higher*. Hedging cannot create spread. It can only move it between currencies (and subtract the basis).

### 15.4.7 Rolling hedges: what is locked and what is not

A fund owns a foreign asset and sells $hN$ units of foreign currency forward for one year at $F_{t-1} = kS_{t-1}$, where $k = (1+r_h)/(1+r_f)$ under CIP (pair FOREIGN/HOME, so $S$ is home per foreign). At each year-end the forward settles in cash and a new one is struck at $F_t = kS_t$. The settlement received at $t$ is

$$C_t = hN\,(F_{t-1} - S_t) = hN\,(kS_{t-1} - S_t).$$

Summed over $T$ rolls the series telescopes:

$$\sum_{t=1}^{T} C_t = hN\left[(S_0 - S_T) + (k-1)\sum_{t=0}^{T-1} S_t\right].$$

Three conclusions follow.

1. **A rolling hedge offsets the change in spot from inception to exit** on the hedged notional, $hN(S_0 - S_T)$, plus a carry term. It does not lock the initial *forward* for the whole hold, because each roll is struck at the then-current spot.
2. **The carry term depends on the spot path and on future rate differentials**, which are unknown today. If the foreign rate is above the home rate, $k < 1$ and each roll costs about $(r_f - r_h)$ of the notional's current home value.
3. **Each settlement is cash, now.** The asset gain or loss that the settlement offsets is unrealized and illiquid. A 10% move against the hedge requires cash equal to about $10\% \times hN S$ at the next roll (Chapter 7, Example 7.6). A matched three-year forward avoids interim settlements, but under a collateral agreement (CSA) it requires variation margin on the mark-to-market instead, which can be larger and more frequent.

### 15.4.8 Choosing the hedge ratio

Let $r_L$ be the asset's local-currency return (volatility $\sigma_L$) and $x$ the percentage change in the home value of one unit of foreign currency (volatility $\sigma_x$, correlation $\rho$ with $r_L$). Ignoring the small cross term and the forward premium, the home-currency return with hedge ratio $h$ is $r_L + (1-h)x$, with variance

$$\sigma^2(h) = \sigma_L^2 + (1-h)^2\sigma_x^2 + 2(1-h)\rho\,\sigma_L\sigma_x.$$

Setting $d\sigma^2/dh = 0$:

$$h^* = 1 + \rho\,\frac{\sigma_L}{\sigma_x}.$$

If the asset and the currency tend to fall together ($\rho > 0$), the minimum-variance hedge exceeds 1. If a weak currency tends to coincide with strong local asset returns ($\rho < 0$, for example a hotel market whose inbound demand rises when the currency is cheap), $h^* < 1$.

A **liquidity constraint** sits on top. If the fund will not pay more than its reserve $R$ in cash at a roll under a $k_\sigma$-standard-deviation move,

$$h \le h_{liq} = \frac{R}{k_\sigma\,\sigma_x\,N_{home}}.$$

The decision is $h = \min(h^*, h_{liq})$, or a decision to raise $R$, add local-currency debt, or buy options. All three cost money. Which is cheapest is the hedge decision.

### 15.4.9 Currency crises in intuition form

**First generation (Krugman, 1979 [FACT: ch15-S01]; Flood and Garber, 1984, *bibliographic verification pending*, ch15-S06).** A government pegs its currency while financing deficits by domestic credit creation. Reserves leak steadily. The peg is doomed. The question is when it breaks. Define the **shadow exchange rate**: the floating rate that would prevail if reserves were exhausted and the currency floated. Speculators attack on the day the shadow rate reaches the peg. Before that day, an attack would give them a loss (the currency would appreciate after the float). After it, there would be an arbitrage gain. The attack therefore comes *before* reserves would run out on their own.

In the linear version (money $M = D + R$, prices equal to the exchange rate, money demand falling by $\alpha$ for each unit of expected depreciation per period), domestic credit grows by $\mu$ per period and reserves fall from $R_0$. After a collapse, the currency would depreciate at rate $\mu$, so money demand drops by $\alpha\mu$ at the moment of the float. That drop is the reserve loss on the day of the attack. The attack occurs when reserves fall to $\alpha\mu$:

$$T_{attack} = \frac{R_0 - \alpha\mu}{\mu}, \qquad \text{compared with naive exhaustion at } \frac{R_0}{\mu}.$$

The model's teaching point is that **the run is rational and its size is predictable from fundamentals**. Reserves that look ample against the steady drain are not ample against the stock shift.

**Second generation (Obstfeld, 1996) [FACT: ch15-S02].** The government can defend the peg, for example by raising interest rates, but it weighs the cost of defense (unemployment, mortgage costs, bank stress, debt service) against the benefit (credibility, anti-inflation commitment, political capital). If markets expect devaluation, defense requires higher rates, which raises its cost, which makes devaluation more likely. Two equilibria can exist with the same fundamentals: no attack and a credible peg, or an attack and a devaluation. Fundamentals determine whether the economy is in the zone where both are possible. Sentiment or a coordinating event decides which one occurs.

**The asymmetry of the one-way bet.** A speculator who shorts a pegged currency for $\tau$ years pays the interest differential $\Delta i\,\tau$. If the peg breaks the gain is the devaluation $d$. If it holds, the loss is the carry plus any bounce $u$ of the currency off its floor. The break-even probability of devaluation is

$$p^* = \frac{u + \Delta i\,\tau}{d + u}.$$

For a one-week horizon, $\tau = 7/365$, so even a 6-point rate differential costs only about 0.12% (Example 15.8). To deter a speculator who believes $p$ is 50%, the defender must make $\Delta i\,\tau \ge p d - (1-p)u$, which for a 10% expected devaluation is several hundred percent annualized. Interest-rate defense works against a slowly building, long-horizon position. It does not work against a short-horizon attack once the probability has moved.

### 15.4.10 Central-bank intervention and capital flows

**Intervention.** To support its currency, a central bank sells foreign reserves and buys its own currency. **Unsterilized**, this shrinks domestic money and raises domestic rates; it is monetary tightening. **Sterilized** (offset by buying domestic bonds), it changes only the currency composition of private portfolios and works mainly as a signal of future policy. A defender of a weak currency is limited by reserves plus credit lines. A central bank resisting appreciation sells its own currency and has no such limit, but accumulates foreign assets and their valuation risk (Chapter 7 discusses the Swiss franc floor, 2011–2015). If the defense fails, the central bank has sold foreign currency at the peg and must buy it back at a weaker rate. The loss, in domestic currency, is $X(S_{new} - S_{peg})$ for $X$ units of foreign currency sold, when $S$ is quoted as domestic per foreign.

**Capital flows.** The balance of payments identity, with the convention that the financial account records net inflows as positive, is

$$\text{Current account} + \text{Net capital inflows} + \text{(Reserve decrease)} = 0.$$

A current-account deficit of 5% of GDP must be financed by net inflows of 5% of GDP or by reserve losses. If inflows stop, the deficit must close within the year through lower spending, a weaker currency, or both. That is the sudden-stop mechanism. For CRE it matters in two ways. In a deficit country, real estate is often financed directly or indirectly by foreign capital, so a stop hits property prices and credit at once. In a surplus country, the domestic investors who export capital are the foreign buyers of property elsewhere, and their behavior depends on hedging costs (§15.4.6).

---

## 15.5 Worked examples

All inputs are [HYPOTHESIS] unless sourced. Rates are simple annual money-market rates. Examples 15.3 and 15.6 apply day counts; the others use a one-year accrual of 1.0 for clarity, as stated in each.

### Example 15.1 — Quote direction, pips, and pip value

**Given.** EUR/USD moves from 1.0850 to 1.0920. USD/JPY moves from 150.00 to 147.50. A U.S. desk is long €10 million of EUR/USD and long \$10 million of USD/JPY.

**Find.** (a) Which currency appreciated in each pair, and by how much in each direction. (b) Pips moved and P&L, in the quote currency and in dollars. (c) Pip value in dollars for each position.

**Solution.**

(a) EUR/USD rose, so the euro appreciated. In dollar terms the euro gained $1.0920/1.0850 - 1 = +0.645\%$. In euro terms the dollar lost $1.0850/1.0920 - 1 = -0.641\%$.
USD/JPY fell, so the dollar depreciated and the yen appreciated. The dollar lost $147.50/150.00 - 1 = -1.667\%$ in yen. The yen gained $150.00/147.50 - 1 = +1.695\%$ in dollars.

(b) EUR/USD: $(1.0920 - 1.0850)/0.0001 = 70$ pips. P&L $= +1 \times 10{,}000{,}000 \times 0.0070 = +\$70{,}000$, earned in USD (the QUOTE currency).
USD/JPY: $(147.50 - 150.00)/0.01 = -250$ pips. P&L $= 10{,}000{,}000 \times (-2.50) = -¥25{,}000{,}000$, earned in JPY. In dollars at the closing rate: $-25{,}000{,}000/147.50 = -\$169{,}492$.

(c) EUR/USD: $10{,}000{,}000 \times 0.0001 = \$1{,}000$ per pip. USD/JPY: $10{,}000{,}000 \times 0.01 = ¥100{,}000$ per pip, which is \$666.67 at 150.00 and changes with the rate.

**Check.** Inverse-pair test: long \$10 million of USD/JPY is short ¥1.5 billion. At the close, ¥1.5 billion costs $1{,}500{,}000{,}000/147.50 = \$10{,}169{,}492$, so the position lost \$169,492. ✓

**Decision consequence.** For a U.S. investor, EUR/USD is a direct quote: up is good for euro assets. USD/JPY is indirect: up is *bad* for yen assets. A risk report that adds "FX moves" across pairs without normalizing direction will net a loss against a gain. Report every exposure as "home value of one foreign unit", and convert JPY-quoted P&L at the closing rate, not the opening rate.

### Example 15.2 — Cross rates, the cross spread, and a triangular mispricing

**Given.** EUR/USD 1.0848/1.0852; USD/JPY 149.98/150.02; GBP/USD 1.2698/1.2702. A second dealer shows EUR/JPY 162.90/162.95.

**Find.** (a) The synthetic EUR/JPY and EUR/GBP two-way prices. (b) Whether the dealer's EUR/JPY quote is a mispricing, and the profit per €1 million.

**Solution.**

(a) EUR/JPY (multiplicative):
* Bid $= 1.0848 \times 149.98 = 162.698$ (sell euros for dollars at 1.0848, then sell dollars for yen at 149.98).
* Ask $= 1.0852 \times 150.02 = 162.802$.

EUR/GBP (both quoted against USD; divide):
* Bid $= 1.0848/1.2702 = 0.85404$ (sell euros for dollars at the EUR/USD bid, buy sterling with dollars at the GBP/USD ask).
* Ask $= 1.0852/1.2698 = 0.85462$.

(b) The dealer bids 162.90 for euros, above the synthetic ask of 162.802. Buy euros synthetically (buy dollars with yen at 150.02, buy euros with dollars at 1.0852) and sell them to the dealer at 162.90. Profit per €1 million $= 1{,}000{,}000 \times (162.90 - 162.802) = ¥98{,}296$, about \$655.

**Check.** The cross spread (10.3 pips on EUR/JPY) is wider than either leg's relative spread, because both legs' spreads compound.

**Decision consequence.** A 6-pip-wide gap on a liquid cross almost always means a stale quote or a quote that will be withdrawn when you hit it. The arbitrage carries leg risk (Chapter 1, §1.4.7). For a real-estate treasury desk the practical lesson is narrower: when you need a cross (for example a yen investor funding a sterling purchase), compare the direct cross quote with the synthetic through dollars and execute the cheaper route.

### Example 15.3 — The 1987 desk exercise: forward, cross, and hedge P&L with a calculator, then in Python

The setting is a 1987-style desk: a screen of deposit rates, a four-function calculator or an HP-12C, and no spreadsheet. **All rates and prices below are hypothetical teaching inputs [HYPOTHESIS], not historical quotes.**

**Given.** Spot GBP/USD 1.6000; spot USD/DEM 1.8000. 182-day deposit rates: USD 7.00% (ACT/360), GBP 9.50% (ACT/365), DEM 4.00% (ACT/360). A U.S. client will receive £5,000,000 in 182 days from the sale of a London building and sells it forward today. At maturity spot GBP/USD is 1.5200.

**Find.** (a) The 182-day GBP/USD forward and forward points. (b) Spot and forward GBP/DEM, computed two ways. (c) Hedged and unhedged dollar proceeds and the hedge P&L. (d) The error from ignoring the GBP day count.

**Solution by calculator.**

(a) Accrual factors:
* USD: $1 + 0.07 \times 182/360 = 1 + 0.0353889 = 1.0353889$.
* GBP: $1 + 0.095 \times 182/365 = 1 + 0.0473699 = 1.0473699$.

On an HP-12C: `0.07 ENTER 182 × 360 ÷ 1 +` → 1.0353889; `0.095 ENTER 182 × 365 ÷ 1 +` → 1.0473699; then `1.6 × [USD factor] ÷ [GBP factor]`.

$$F = 1.6000 \times \frac{1.0353889}{1.0473699} = 1.581697.$$

Forward points $= (1.581697 - 1.6000)/0.0001 = -183.0$ pips. Sterling, the higher-yielding currency, trades at a forward discount.

(b) Spot GBP/DEM $= 1.6000 \times 1.8000 = 2.8800$.
Route 1, via the two forwards. USD/DEM forward $= 1.8000 \times (1 + 0.04 \times 182/360)/1.0353889 = 1.8000 \times 1.0202222/1.0353889 = 1.773633$ (−263.7 pips). GBP/DEM forward $= 1.581697 \times 1.773633 = 2.805351$.
Route 2, directly by CIP on GBP and DEM rates: $2.8800 \times 1.0202222/1.0473699 = 2.805351$. ✓ The dollar rate cancels.

(c) Hedged proceeds $= 5{,}000{,}000 \times 1.581697 = \$7{,}908{,}487$. Unhedged at 1.5200: $5{,}000{,}000 \times 1.52 = \$7{,}600{,}000$. Hedge P&L on the short sterling forward $= -1 \times 5{,}000{,}000 \times (1.5200 - 1.581697) = +\$308{,}487$, which is exactly the difference.

(d) If the desk had used ACT/360 for sterling, the GBP factor would be $1 + 0.095 \times 182/360 = 1.0480278$, the forward 1.580704, an error of about 9.9 pips, or \$4,965 on £5 million. The quick approximation $S(r_Q - r_B)\tau$ with mixed day counts gives −191.7 pips; the exact figure is −183.0 pips, because the approximation omits the division by $(1 + r_B\tau_B)$.

**In Python** (`sdesk.markets`):

```python
from sdesk import markets as mk
S, d = 1.60, 182
# covered_interest_forward uses one accrual fraction; fold GBP's ACT/365 into the rate
F = mk.covered_interest_forward(S, r_quote=0.07, r_base=0.095 * 360 / 365, t=d / 360)   # 1.581697
F_usddem = mk.covered_interest_forward(1.80, r_quote=0.04, r_base=0.07, t=d / 360)     # 1.773633
F_gbpdem = F * F_usddem                                                                # 2.805351
hedge_pnl = mk.fx_pnl(5_000_000, F, 1.52, side=-1)                                     # +308,487 USD
```

**Check.** The two GBP/DEM routes agree to every digit, which confirms the chain was built with the dollar cancelling.

**Decision consequence.** The hedge did not "make" \$308,487. It fixed the proceeds at \$7.91 million when the deal was signed, which is what the client's committee approved. Had sterling risen to 1.68, the hedge would have "lost" \$491,513 and the proceeds would still be \$7.91 million. Judge a hedge by whether it delivered the certainty it was bought for, not by its own P&L. The day-count error in (d) is small per trade but systematic: a desk that always uses 360 for sterling misprices every sterling forward in the same direction.

### Example 15.4 — Carry trade P&L decomposition

**Given.** Borrow ¥1,500,000,000 for one year at 0.50%. Convert at USD/JPY 150.00 into \$10,000,000. Invest at 4.25%. Margin posted: ¥150,000,000 (10%). Accrual fraction 1.0. Consider year-end spot rates of 150.00, 147.00, and 135.00.

**Find.** P&L in yen, its decomposition into carry, spot, and cross terms, the return on margin, and the break-even rate.

**Solution.** Here the investment currency is USD and the funding currency is JPY. $\Pi = N[(1.0425)S_T/150 - 1.005]$ with $N = ¥1.5$ billion.

| $S_T$ | $s = S_T/S_0 - 1$ | Carry $N(r_i - r_f)$ | Spot $Ns$ | Cross $N r_i s$ | Total P&L | Return on margin |
|---|---|---|---|---|---|---|
| 150.00 | 0.00% | ¥56,250,000 | 0 | 0 | ¥56,250,000 | +37.50% |
| 147.00 | −2.00% | ¥56,250,000 | −¥30,000,000 | −¥1,275,000 | ¥24,975,000 | +16.65% |
| 135.00 | −10.00% | ¥56,250,000 | −¥150,000,000 | −¥6,375,000 | −¥100,125,000 | −66.75% |

Break-even $S_T = F = 150.00 \times 1.005/1.0425 = 144.604$, a 3.60% dollar depreciation.

**Check.** At 135.00: $1.5 \times 10^9 \times (1.0425 \times 0.9 - 1.005) = 1.5\times10^9 \times (-0.06675) = -¥100{,}125{,}000$. ✓

**Decision consequence.** The trade earns 37.5% on margin if nothing happens and loses two-thirds of margin on a 10% yen rally. The "3.75% a year" in the pitch is the carry term only. The trade is a bet that the dollar will fall by less than 3.6% against the yen, at 10× leverage. Whether that is attractive depends on the distribution of yen rallies, which is the subject of the next example.

### Example 15.5 — Crash risk: break-even probability and what a track record cannot tell you

**Given.** The position of Example 15.4, now held month by month. Monthly carry on notional $c = (1 + 0.0425/12) - (1 + 0.005/12) = 0.3125\%$. In a crash month the dollar falls 8% against the yen; the month's result is $L = (1 + 0.0425/12)(0.92) - (1 + 0.005/12) = -7.716\%$ of notional. In non-crash months, spot is unchanged on average.

**Find.** (a) Break-even monthly crash probability. (b) Expected monthly return at $p = 3\%$. (c) The probability of a year with no crash at $p = 3\%$, and the loss on margin in a crash month at 10× leverage.

**Solution.**

(a) $p^* = c/(c - L) = 0.003125/(0.003125 + 0.077158) = 3.89\%$ per month.

(b) $E = 0.97 \times 0.3125\% + 0.03 \times (-7.716\%) = 0.3031\% - 0.2315\% = +0.0717\%$ per month, about 0.86% a year on notional, against 3.75% of headline carry.

(c) $P(\text{no crash in 12 months}) = 0.97^{12} = 69.4\%$. A crash month loses $10 \times 7.716\% = 77.2\%$ of margin, which is 24.7 months of carry.

**Check.** At $p = p^*$, $E = (1 - 0.0389)(0.003125) + 0.0389(-0.07716) \approx 0$. ✓

**Decision consequence.** In about 70% of years at $p = 3\%$ the trade shows a smooth 37.5% return on margin, and its expected return is less than a quarter of the headline carry. A three-year track record without a crash is consistent with $p = 1\%$ (profitable) and with $p = 5\%$ (loss-making). The decision turns on a parameter that the trader's own history cannot estimate. Two responses are defensible: size so that a crash month costs a tolerable fraction of capital (at 2× rather than 10×, about 15% of margin), or buy downside protection and accept that it consumes much of the carry. Calling 3.75% "income" is not defensible.

### Example 15.6 — The CIP basis and a dollar investor's hedged euro yield

**Given.** EUR/USD spot 1.0850. One-year (365-day) rates: USD 4.25%, EUR 2.50%, both ACT/360, so $\tau = 365/360$. The market one-year outright is quoted 20 pips above the CIP forward. A U.S. investor owns a euro asset worth €20,000,000 that will return 5.00% in euros over the year and hedges the terminal amount.

**Find.** (a) The CIP forward and forward points. (b) The implied cross-currency basis. (c) The investor's hedged dollar return under CIP and at the market forward.

**Solution.**

(a) $F^{CIP} = 1.0850 \times (1 + 0.0425 \times 365/360)/(1 + 0.025 \times 365/360) = 1.103775$. Points $= +187.8$ pips. The euro, the lower-yielding currency, trades at a forward premium.

(b) Market forward $F^{mkt} = 1.105775$. Solve $F^{mkt} = S(1 + r_{USD}\tau)/(1 + (r_{EUR} + b)\tau)$ for $b$:
$$b = \frac{1}{\tau}\left(\frac{S(1 + r_{USD}\tau)}{F^{mkt}} - 1\right) - r_{EUR} = -18.3 \text{ bp}.$$

(c) Dollar cost: $20{,}000{,}000 \times 1.0850 = \$21{,}700{,}000$. Terminal euros $= €21{,}000{,}000$.
* Under CIP: $21{,}000{,}000 \times 1.103775 = \$23{,}179{,}282$, a hedged return of **6.817%**.
* At the market forward: $21{,}000{,}000 \times 1.105775 = \$23{,}221{,}282$, a hedged return of **7.011%**. The basis adds \$42,000 (\$40,000 on the initial €20 million notional).

**Check.** CIP identity: $(1.05)(1 + 0.0425\tau)/(1 + 0.025\tau) - 1 = 6.817\%$. ✓

**Decision consequence.** A negative basis is a gift to the dollar-based hedger of euro assets and a tax on the euro-based hedger of dollar assets. For a European buyer of U.S. property the effective hedge cost is the rate differential *plus* the basis, here about 18 bp more than the policy-rate arithmetic of Chapter 7 suggests. Basis can widen sharply at quarter-ends and in funding stress. A hedge budget built on policy rates alone is optimistic for foreign buyers of U.S. assets.

### Example 15.7 — First-generation crisis: when does the attack come?

**Given.** A country pegs its currency. Foreign reserves are \$40 billion. A credit-financed fiscal deficit drains reserves at \$2 billion a month. In the linear model of §15.4.9 the money-demand semi-elasticity is $\alpha = 5$ months (money demand falls by 5 months' worth of credit growth when expected depreciation equals the credit growth rate). All values [HYPOTHESIS].

**Find.** (a) The naive exhaustion date. (b) The attack date and the reserve loss on the day of the attack. (c) The attack date if $\alpha = 8$.

**Solution.**

(a) $R_0/\mu = 40/2 = 20$ months.

(b) $T = (R_0 - \alpha\mu)/\mu = (40 - 5 \times 2)/2 = 15$ months. Reserves at the attack: $\alpha\mu = \$10$ billion, lost in a single day.

(c) $T = (40 - 16)/2 = 12$ months.

**Check.** At $T = 15$ months, reserves have fallen by $15 \times 2 = 30$ to \$10 billion, equal to $\alpha\mu$. ✓

**Decision consequence.** A reserve-coverage ratio computed against the steady drain overstates the peg's life by a quarter (here 5 of 20 months). The attack consumes the last quarter of reserves in one day, and it comes earlier the more interest-sensitive money demand is. An investor in a pegged-currency asset must model the *stock* that will leave when expectations flip, not the monthly flow. Short-term external debt and non-resident holdings of local deposits and bonds are the practical proxies for that stock.

### Example 15.8 — The one-way bet, the cost of a rate defense, and the defender's loss

**Given.** A currency trades at the floor of its peg against an anchor currency. A speculator considers a one-week short. The defender has raised its overnight rate to 15%; the anchor rate is 9%. If the peg breaks, the currency falls 10% against the anchor. If the peg holds, the currency bounces 1% off the floor. Separately, a defender sells 15 billion units of anchor currency at a floor of 2.7780 (anchor units per domestic unit) and the currency later settles at 2.55. All values [HYPOTHESIS].

**Find.** (a) The speculator's carry cost and break-even probability of devaluation, with and without the bounce. (b) The interest differential needed to deter a speculator who believes $p = 50\%$. (c) The defender's loss, in domestic currency, from rebuying the anchor currency.

**Solution.**

(a) Carry cost $= (0.15 - 0.09) \times 7/365 = 0.1151\%$.
Without a bounce: $p^* = 0.001151/0.10 = 1.15\%$.
With the 1% bounce: $p^* = (0.01 + 0.001151)/(0.10 + 0.01) = 10.14\%$.

(b) The weekly cost must satisfy $c \ge pd - (1-p)u = 0.5 \times 0.10 - 0.5 \times 0.01 = 4.5\%$ per week, an annualized differential of $0.045 \times 365/7 = 234.6\%$.

(c) The defender received $15/2.7780 = 5.3996$ billion domestic units for the anchor currency it sold. To rebuy 15 billion anchor units at 2.55 costs $15/2.55 = 5.8824$ billion. Loss $= 0.4828$ billion domestic units.

**Check.** At $p = 10.14\%$: $0.1014 \times (0.10 - 0.00115) - 0.8986 \times (0.01 + 0.00115) \approx 0$. ✓

**Decision consequence.** The speculator risks 1.1% to make 9.9%. Once the market's probability of devaluation exceeds about 10%, no tolerable interest rate stops a one-week attack, and a defense by rates only raises the domestic cost of defense, which is the second-generation channel. A real-estate investor holding assets in a currency under attack should not read a dramatic rate rise as proof of commitment. It can be the opposite signal: the authorities are using the last tool that remains.

### Example 15.9 — Rolling the hedge on the London hotel

**Given.** The §15.1 hotel. Equity £22.5 million (\$28,575,000 at 1.2700). Annual distribution $= 3{,}500{,}000 - 0.06 \times 27{,}500{,}000 = £1{,}850{,}000$, converted at year-end spot (income is left unhedged). Sale at end of year 3 for £53.0 million less 2% costs, repaying the £27.5 million loan: net equity proceeds £24,440,000. Rates stay at USD 4.25% and GBP 4.75%, so $k = 1.0425/1.0475 = 0.995227$. The fund sells £22.5 million forward for one year ($h = 1$ on initial equity) and rolls annually. The spot path is 1.1500, 1.2200, 1.3200 at the ends of years 1–3. Transaction costs on purchase are ignored for clarity.

**Find.** (a) The forward struck at each roll and the cash settlement at each year-end. (b) The fund's dollar equity IRR unhedged and hedged. (c) The local-currency IRR. (d) Reconcile the total hedge settlement with the telescoping formula of §15.4.7.

**Solution.**

(a)

| Year-end | Spot $S_t$ | Forward settling $F_{t-1}$ | Settlement $22.5\text{m} \times (F_{t-1} - S_t)$ | New forward $kS_t$ |
|---|---|---|---|---|
| 0 | 1.2700 | — | — | 1.263938 |
| 1 | 1.1500 | 1.263938 | +\$2,563,604 | 1.144511 |
| 2 | 1.2200 | 1.144511 | −\$1,698,508 | 1.214177 |
| 3 | 1.3200 | 1.214177 | −\$2,381,026 | — |
| Total | | | **−\$1,515,931** | |

(b) Unhedged dollar flows: $-28{,}575{,}000$; $1{,}850{,}000 \times 1.15 = 2{,}127{,}500$; $1{,}850{,}000 \times 1.22 = 2{,}257{,}000$; $(1{,}850{,}000 + 24{,}440{,}000) \times 1.32 = 34{,}702{,}800$. IRR **11.75%**.
Hedged flows add the settlements: $-28{,}575{,}000$; $4{,}691{,}104$; $558{,}492$; $32{,}321{,}774$. IRR **10.62%**.

(c) Sterling flows $-22{,}500{,}000$; $1{,}850{,}000$; $1{,}850{,}000$; $26{,}290{,}000$. IRR **10.81%**.

(d) $hN[(S_0 - S_3) + (k-1)(S_0 + S_1 + S_2)] = 22.5\text{m} \times [(1.27 - 1.32) + (-0.004773)(1.27 + 1.15 + 1.22)] = 22.5\text{m} \times (-0.05 - 0.017375) = -\$1{,}515{,}931$. ✓ The hedge offset the 5-cent rise in sterling (−\$1.125 million) and cost \$0.391 million of carry.

**Check.** On a path where spot equals each prior forward ($S_t = kS_{t-1}$), every settlement is zero and the dollar IRR is 10.28%: the sterling IRR less roughly the 0.48-point annual rate differential. ✓

**Decision consequence.** The hedge "lost" \$1.5 million on a path where sterling rose, and the hedged IRR (10.62%) is below the unhedged (11.75%). That is the insurance working as designed, not a mistake. Three facts matter more for the committee. First, the cash pattern: the fund *received* \$2.56 million in year 1, when the hotel's dollar value had fallen, then *paid* \$1.70 million in year 2 and \$2.38 million at exit. The year-2 call nearly equals that year's distribution. Second, the year-3 settlement falls due at the forward date whether or not the sale has closed. If the sale slips six months, the fund must pay \$2.38 million from reserves or roll at an off-market rate, which is a disguised loan from the bank. Third, the hedge covered £22.5 million of *initial* equity. By year 3 the equity is worth £24.4 million, so about 8% of the exposure was never hedged. A hedge notional should be reset at each roll to the current equity mark if the intent is a constant hedge ratio.

### Example 15.10 — Choosing the hedge ratio under a liquidity constraint

**Given.** The hotel of Example 15.9. Annual volatility of the local equity return $\sigma_L = 12\%$; volatility of GBP/USD $\sigma_x = 9\%$; correlation $\rho = -0.25$ (a weaker pound tends to coincide with stronger London hotel trading through inbound demand). Liquidity reserve \$2,000,000. Policy: no roll may require more cash than the reserve in a 2-standard-deviation currency move. Hedged notional \$28,575,000 × $h$. All parameters [HYPOTHESIS].

**Find.** (a) The minimum-variance hedge ratio. (b) The liquidity-constrained maximum. (c) Return volatility at $h = 0$, $h_{liq}$, $h^*$, and 1. (d) The reserve required to support $h^*$.

**Solution.**

(a) $h^* = 1 + \rho\sigma_L/\sigma_x = 1 - 0.25 \times 12/9 = 0.667$.

(b) $h_{liq} = R/(2\sigma_x N) = 2{,}000{,}000/(0.18 \times 28{,}575{,}000) = 0.389$.

(c) $\sigma(h) = \sqrt{0.12^2 + (1-h)^2 0.09^2 + 2(1-h)(-0.25)(0.12)(0.09)}$:

| $h$ | 0 | 0.389 | 0.667 | 1.00 |
|---|---|---|---|---|
| $\sigma(h)$ | 13.08% | 11.88% | 11.62% | 12.00% |

(d) $R = h^* \times 2\sigma_x \times N = 0.667 \times 0.18 \times 28{,}575{,}000 = \$3{,}429{,}000$.

**Check.** $\sigma(1) = \sigma_L = 12\%$, as it must be when the currency exposure is fully removed. ✓

**Decision consequence.** Full hedging *raises* volatility relative to $h^*$ when the currency and the asset are negatively correlated, because it removes a natural offset. The variance benefit of moving from 0.389 to 0.667 is small (about 27 bp of volatility: 11.885% versus 11.619%). The liquidity cost is \$1.43 million of additional reserve, about 5% of equity, earning money-market rates. On these numbers $h \approx 0.4$ with the existing reserve is defensible, and so is $h = 0.67$ with a larger reserve. $h = 1$ is not, on either ground. The correlation estimate is the weakest input: $\rho$ between a single hotel and a currency is estimated from few, noisy observations, and if it is zero, $h^* = 1$. A hedge policy that states its correlation assumption and its liquidity rule is auditable. "We hedge 100% because we are not currency speculators" is not, because at $\rho < 0$ the full hedge is itself a position.

---

## 15.6 CRE application: the foreign buyer and the U.S. buyer abroad

Chapter 7 (Examples 7.5–7.6) computed a euro investor's hedged yield on a U.S. industrial building and the cash call on a 10% currency move. This section adds the cases that Chapter 7 did not cover.

**1. The yen buyer of a U.S. hotel.** A Japanese insurer considers a U.S. hotel at a 7.5% cap rate on NOI after reserve, all cash. U.S. short rates are 4.25% and yen short rates 0.50% [HYPOTHESIS]. Hedged yield under CIP: $(1.075)(1.005/1.0425) - 1 = 3.63\%$. A Japanese hotel at 4.0% has a higher spread over its home short rate (ratio 1.0348 versus 1.0312). The hedged U.S. asset is not better than the domestic one; it is slightly worse, before the basis, which for yen hedgers of dollar assets has usually been a further cost (§15.4.4). A Japanese bidder who pays 7.5% for the U.S. hotel is therefore either unhedged (a currency position), partly hedged with U.S. dollar debt, or buying for diversification. **For a U.S. seller, the bidder's hedge arithmetic is part of the price.** When the U.S.–Japan policy differential narrows, hedged yen buyers can pay more.

**2. The U.S. buyer of a Japanese asset.** The same arithmetic runs the other way. A Tokyo asset yielding 4.0% hedged into dollars returns $(1.04)(1.0425/1.005) - 1 = 7.88\%$. This is not free yield. It is the Japanese asset's spread over yen rates, transported onto U.S. short rates, plus any basis benefit. A U.S. committee that compares 7.88% with a 7.5% U.S. cap rate is comparing a hedged short-rate-plus-spread with an unhedged property yield, and must also allow for the rolling-hedge cash pattern of Example 15.9.

**3. Local debt as a partial hedge.** Borrowing in the asset's currency hedges the borrowed portion without cash settlements: the loan's value moves with the asset's currency. In Example 15.9, the £27.5 million loan means only the £22.5 million equity is exposed. The cost is the local borrowing rate. The opposite structure, borrowing in dollars against local-currency property, adds currency exposure to property exposure: when the currency falls, the debt rises in local terms as asset values fall [INFERENCE from the mechanics]. Unhedged foreign-currency borrowing is widely described as an amplifier in the 1997 Asian crisis, which Chapter 23 examines with sources *(verification pending here)*.

**4. The hedge-ratio memo.** For any foreign acquisition, the investment memo (`desk/investment_memos/investment_committee_memo.md`) should state: the exposure measure (initial equity, current equity mark, or expected exit equity); the instrument and tenor; the hedge ratio and the correlation assumption behind it; the liquidity reserve and the stress move it covers; the policy on resetting notional at each roll; and what happens to the hedge if the sale is delayed.

---

## 15.7 When the relationships fail

1. **UIP fails systematically.** High-interest-rate currencies have not, on average, depreciated by the forward discount, and in Fama's (1984) regressions the forward premium often predicted the wrong sign of the spot change [FACT: ch15-S05]. The forward is not a forecast. Treat any analysis that uses the forward as "the market's expected exchange rate" as an assumption.
2. **CIP fails when dealer balance sheets are scarce.** The basis has been persistent since 2008 and has spiked at quarter-ends and in stress (ch15-S03). For hedgers it is a real cost or benefit. For arbitrageurs it is not free money: closing it requires balance sheet that banks price for leverage-ratio and capital purposes.
3. **Pegs fail abruptly, not gradually.** A peg compresses volatility until it breaks. Historical volatility measured during a peg understates risk. The relevant measures are reserves against the stock of mobile capital, the political cost of defense, and forward-implied devaluation expectations.
4. **Correlations flip in stress.** The negative correlation that justified $h^* < 1$ in Example 15.10 is a normal-times estimate. In a global risk-off episode, a pound sell-off and a London hotel sell-off can happen together, and the unhedged share then compounds the loss.
5. **Hedges fail through liquidity, not logic.** A rolling forward on an illiquid asset is economically sound and can still force a sale (Chapter 7, §7.8, the 2022 LDI episode).
6. **Convertibility and redenomination are not hedged by forwards.** If a currency is redenominated, capital controls are imposed, or the forward market closes (non-deliverable forwards settle against a fixing that may itself be suspended), the hedge contract may not deliver. Chapter 7 discussed euro redenomination risk.
7. **Carry crashes cluster.** Carry losses tend to arrive when funding liquidity dries up and many holders unwind at once (ch15-S04). Diversifying across carry pairs does little when the common factor is global risk appetite.

---

## 15.8 Policy-rate differentials, carry, and the forward premium puzzle: what the evidence supports

| Claim | Status |
|---|---|
| Short-dated forward points track the policy-rate differential | [FACT] by CIP arithmetic, up to the basis (ch15-S03) |
| High-yield currencies depreciate by the forward discount on average | Rejected for many samples [FACT: ch15-S05] |
| Carry returns are negatively skewed and crash in liquidity stress | [FACT: ch15-S04] for the samples studied |
| Carry will continue to earn a positive premium | [HYPOTHESIS]. The premium is compensation for crash risk and can be competed away or realized as a loss in a long bad stretch |
| Rate differentials explain the level of exchange rates over years | Weak. Over multi-year horizons, inflation differentials, terms of trade, and current-account sustainability matter more [INFERENCE from the failure of UIP and the literature on exchange-rate forecasting] |

---

## 15.9 Historical episode: sterling's exit from the ERM, 16 September 1992

**Date and environment.** Sterling joined the Exchange Rate Mechanism (ERM) of the European Monetary System on 8 October 1990 at a central rate of £1 = DM 2.95, in the wide 6% band [FACT: ch15-S07, Bank of England *Quarterly Bulletin* 1990 Q4, and ch15-S08, the Prime Minister's statement of 15 October 1990; VERIFIED-SECONDARY]. Secondary sources give the permitted range as about DM 2.78 to DM 3.13 [FACT: ch15-S09, VERIFIED-SECONDARY]. That range is consistent with limits set at about 6.18% above and below the central rate in ratio terms: $2.95 \times 1.0618 = 3.132$ and $2.95/1.0618 = 2.778$ [INFERENCE from the arithmetic; the exact intervention-limit formula is *(verification pending)*]. Using ratios rather than differences keeps the band symmetric when the pair is inverted, which is the quote-direction point of §15.4.1 applied to a treaty.

During the first eighteen months of membership, the Bank of England's own account is that ERM membership helped base rates come down from 15% to 10%, while German official rates were rising after reunification, and that sterling's ERM position constrained how far U.K. rates could fall below German rates [FACT: ch15-S10, Bank of England *Quarterly Bulletin* 1992 Q4, "Operation of monetary policy"; VERIFIED-SECONDARY from search excerpts of the article].

**What was knowable before the crisis.** It was public that the anchor country, Germany, was running tight monetary policy for domestic reasons, that the U.K. was in a weak economy, and that U.K. rates were constrained by the peg [FACT: ch15-S10]. A Federal Reserve Bank of San Francisco study later found that sterling's peg appeared credible for much of 1992, with realignment expectations rising only shortly before September [FACT: ch15-S11, VERIFIED-SECONDARY; the study's method and exact measures *(verification pending)*]. Eichengreen and Wyplosz (1993) argued soon afterward that the 1992 attacks were better explained by self-fulfilling expectations, given the removal of capital controls and the incentives created by the Maastricht process, than by fundamentals alone [FACT about their argument: ch15-S12].

**What happened.** On 16 September 1992, the Bank of England raised its minimum lending rate from 10% to 12% [FACT: ch15-S10 and ch15-S13; VERIFIED-SECONDARY]. Several secondary accounts report that a further rise to 15% was announced later that day [FACT: ch15-S13, class C sources, VERIFIED-SECONDARY]. Accounts differ on whether the 15% rate ever took effect. That evening the government suspended sterling's ERM membership after heavy official purchases of sterling [FACT: ch15-S10]. The Bank's account records that it was able to signal a 1-point reduction in interest rates later in September [FACT: ch15-S10]. Reports of the rate on 17 September conflict (10% in some accounts, 9% in one) *(verification pending)*. On 8 October 1992 the Chancellor announced an inflation target of 1–4% for underlying RPI inflation, to replace the framework previously provided by the ERM [FACT: ch15-S14, VERIFIED-SECONDARY].

**The cost.** A Treasury paper released in February 2005 under the Freedom of Information Act estimated the cost of Black Wednesday at about £3.3 billion [FACT: ch15-S15, VERIFIED-SECONDARY via reporting of the released paper]. The estimate compares reserves with and without intervention and depends on its valuation date. The share of reserves spent on the day and the profits of individual speculators are widely reported in secondary sources but are not used here *(verification pending)*.

**Interpretations.** Read through §15.4.9:

* *Second-generation reading.* The U.K. could in principle have kept raising rates, but a weak economy made the cost of defense high, and markets knew it. The announced moves to 12% and 15% did not lift sterling from its floor (ch15-S10). Example 15.8 shows why: against a one-week horizon, even a five-point rise in the overnight rate costs a speculator about a tenth of a percent, while the gain from a devaluation is a double-digit percentage. Once the market probability of exit was material, the rate defense could not work, and its domestic cost made exit more likely [INFERENCE].
* *Fundamentals reading.* German monetary policy was set for German conditions after reunification, and the U.K. economy needed lower rates. A peg that requires tighter money than the domestic economy can bear is inconsistent in the medium run, as in a first-generation model, even if reserves were not literally running out [INFERENCE].
* The two readings are not exclusive. Fundamentals put the U.K. in the zone where an attack could succeed; expectations and the removal of capital controls determined when.

**What the case does and does not establish.** It establishes that a credible-looking peg can be abandoned within a day, that interest-rate defense fails against short-horizon speculation once the probability of devaluation moves, and that a central bank selling reserves at the peg books the loss when the peg breaks. It does **not** establish that devaluation was inevitable on that date, that speculators caused rather than revealed the inconsistency, or that exits from pegs are generally good for the exiting economy. The U.K.'s subsequent experience under inflation targeting is a separate question with its own confounders.

**CRE connection.** An investor who owned a London building financed in Deutschmarks, or a German investor who owned it unhedged, experienced the exit as a large step change in the currency value of the investment, overnight, with no change in the building. A property underwriter who treated the peg as a fixed rate was speculating on the government's willingness to bear pain. Example 15.7's lesson applies: the relevant risk measure was not the peg's historical stability but the size of the capital that would move once expectations flipped.

---

## 15.10 Decision exercise: the three proposals

Return to §15.1. Write a decision record (`desk/investment_memos/decision_record_template.md`) covering:

1. **The London hotel hedge.** Choose an instrument (rolling one-year forwards, a three-year forward under a CSA, options, or more local debt), a hedge ratio, and a notional reset policy. State the correlation assumption, the stress move, and the reserve. Explain what happens if the sale slips by six months.
2. **The yen carry trade.** State the break-even monthly crash probability (Example 15.5). Say what information would let you estimate $p$, whether you have it, and what size you would accept. Abstention is a legitimate answer.
3. **The pegged-currency hotel.** Compute the hedged dollar yield if the forward market implies a 9% annual forward discount on the local currency (Problem 15.10 gives the numbers). Identify which data would tell you whether the economy is in the first- or second-generation danger zone: reserves against short-term external debt, the current-account deficit, non-resident holdings, and the domestic cost of a rate defense.

**Rubric (see `problems/solutions/ch15_solutions.md` §Decision exercise).** Full credit requires: a hedge ratio justified by both variance and liquidity, not by habit; a carry decision tied to a stated crash probability and sizing rule, recognizing that the track record cannot identify $p$; recognition that the hedged yield of a pegged high-yield currency is close to the dollar rate or below it, so that the unhedged return is a bet on the peg; and explicit invalidation criteria. There is no single correct allocation. Declining both the carry trade and the pegged-currency hotel, while hedging the London hotel at 0.4–0.7, can earn full credit.

---

## 15.11 Frequent analytical errors

1. **Reading the quote backwards.** Treating a rise in USD/JPY as good for yen assets, or computing the percentage change of the inverse pair by flipping the sign.
2. **Converting P&L at the wrong rate.** JPY-quoted P&L converts to dollars at the closing rate.
3. **Building cross bid/ask from mid rates, or with the wrong sides.** In a divisive cross, the bid uses the *ask* of the denominator pair.
4. **Ignoring day counts.** GBP is ACT/365; USD, EUR and JPY are ACT/360. The error is small per trade and systematic across a book.
5. **Treating the forward as a forecast.** The forward reflects the rate differential. UIP is rejected in the data.
6. **Quoting carry as income.** Carry is compensation for crash risk; expected return is carry minus expected crash losses.
7. **Inferring safety from a crash-free track record.** A few years of carry cannot distinguish a 1% from a 5% monthly crash probability.
8. **Comparing an unhedged foreign yield with a home yield.** Hedging transports the spread over short rates, not the yield.
9. **Forgetting the basis.** Hedge cost is the rate differential plus the basis.
10. **Believing a rolling hedge locks the initial forward.** Each roll re-strikes at spot; carry over the hold depends on future rates.
11. **Hedging the initial equity forever.** The exposure changes; the notional should be reset to a stated measure.
12. **Hedging an illiquid asset with cash-settled forwards and no reserve.** The cash call arrives at the roll; the offsetting gain is unrealized.
13. **Reading a dramatic rate rise as proof that a peg will hold.** It can be the last tool in use.

---

## 15.12 Connections to other chapters

* **Chapter 1** (§1.4.7): leg risk in triangular arbitrage; the carry trade as positive EV that can still ruin at the wrong size.
* **Chapter 5**: policy rates drive the front end, and therefore forward points and hedge costs.
* **Chapter 7** (§7.4.6–7.4.7, Examples 7.5–7.6): the trilemma, CIP and hedged yields, and the hedge cash call. This chapter adds rolling, hedge ratios, and the basis.
* **Chapter 10**: local-currency debt as a natural hedge; loan sizing in a foreign currency.
* **Chapter 13**: liquidity reserves and hedging rate exposure on a CRE portfolio; the same reserve logic applies to FX hedges.
* **Chapter 18**: currency options as an alternative to forwards when liquidity is the binding constraint.
* **Chapter 21**: sizing a negatively skewed strategy; Kelly under parameter uncertainty.
* **Chapter 23**: ERM 1992 and Asia 1997 in full.

---

## 15.13 One-page reference sheet

**Quote discipline.** BASE/QUOTE at $S$: 1 BASE = $S$ QUOTE. BASE→QUOTE: × $S$. QUOTE→BASE: ÷ $S$. P&L in QUOTE: side × $N$ × ($S_1 - S_0$). Inverse % change: $S_0/S_1 - 1$. Inverting a two-way quote swaps bid and ask.

| Formula | Expression |
|---|---|
| Pip value | $N_{BASE} \times$ pip size (in QUOTE) |
| Multiplicative cross | bid = bid × bid; ask = ask × ask |
| Divisive cross | bid = bid$_1$/ask$_2$; ask = ask$_1$/bid$_2$ |
| CIP forward | $F = S(1 + r_Q\tau_Q)/(1 + r_B\tau_B)$ |
| Forward points | $(F - S)/\text{pip}$; higher-rate currency at a discount |
| Basis (X/USD) | $F^{mkt} = S(1 + r_{USD}\tau)/(1 + (r_X + b)\tau)$ |
| Carry P&L | $N[(r_i - r_f)\tau + s + r_i\tau s]$ |
| Carry break-even crash probability | $p^* = c/(c - L)$ |
| Hedged return | $(1+R_h)/(1+r_h) = (1+y)/(1+r_f)$ |
| Rolling-hedge settlement | $C_t = hN(kS_{t-1} - S_t)$; $\sum C_t = hN[(S_0 - S_T) + (k-1)\sum_{t<T} S_t]$ |
| Minimum-variance hedge ratio | $h^* = 1 + \rho\sigma_L/\sigma_x$ |
| Liquidity cap on hedge ratio | $h \le R/(k_\sigma\sigma_x N)$ |
| First-generation attack time | $T = (R_0 - \alpha\mu)/\mu$ |
| One-way-bet break-even | $p^* = (u + \Delta i\,\tau)/(d + u)$ |
| Intervention loss | $X(S_{new} - S_{peg})$, $S$ = domestic per foreign |

**Day counts.** USD, EUR, JPY, CHF: ACT/360. GBP: ACT/365.

**Numbers to remember (from this chapter's hypothetical examples).** A 1-point rate differential is about 1% a year of hedge cost or carry. A one-week short of a pegged currency at a 6-point rate differential costs about 0.12%. At 10× leverage, an 8% currency crash erases about two years of 3.75% carry. Full hedging is not minimum-variance when the asset and currency are negatively correlated.

---

## References for this chapter

Source entries and verification status are in `references/sources_ch15.md`.

* Brunnermeier, M. K., Nagel, S., and Pedersen, L. H. (2009). "Carry Trades and Currency Crashes." *NBER Macroeconomics Annual 2008*, 23, 313–347.
* Du, W., Tepper, A., and Verdelhan, A. (2018). "Deviations from Covered Interest Rate Parity." *Journal of Finance*, 73(3), 915–957.
* Eichengreen, B., and Wyplosz, C. (1993). "The Unstable EMS." *Brookings Papers on Economic Activity*, 1993(1), 51–143 *(end page to be confirmed)*.
* Fama, E. F. (1984). "Forward and Spot Exchange Rates." *Journal of Monetary Economics*, 14(3), 319–338.
* Flood, R. P., and Garber, P. M. (1984). "Collapsing Exchange-Rate Regimes: Some Linear Examples." *Journal of International Economics*, 17(1–2), 1–13 *(bibliographic verification pending)*.
* Krugman, P. (1979). "A Model of Balance-of-Payments Crises." *Journal of Money, Credit and Banking*, 11, 311–325.
* Obstfeld, M. (1996). "Models of Currency Crises with Self-Fulfilling Features." *European Economic Review*, 40(3–5), 1037–1047.
* Bank of England (1990). "The exchange rate mechanism of the European monetary system." *Quarterly Bulletin*, 1990 Q4.
* Bank of England (1992). "Operation of monetary policy." *Quarterly Bulletin*, 1992 Q4 (November).
