# Chapter 1 — What Is Speculation?

> **Status:** Complete (v1.0). Numerical examples are reproduced in `tests/test_ch01_examples.py`. Problems are in `problems/questions/ch01_problems.md` and solutions in `problems/solutions/ch01_solutions.md`.

## Learning objectives

After this chapter you should be able to:

1. Classify a transaction as investment, speculation, arbitrage, hedging, or gambling by asking **what risk is being borne and who pays for bearing it**. The asset type does not decide the classification.
2. Separate expected return from realized return. Compute expected profit, dispersion, probability of loss, and the IRR of expected cash flows for a discrete scenario set, and explain why expected IRR and the IRR of expected cash flows differ.
3. Compute a **break-even probability** and use it to make decisions when probabilities are uncertain (Knightian uncertainty).
4. Price **immediacy**: compute the annualized rate a forced seller implicitly pays a liquidity provider, and judge whether that payment is compensation for risk or a genuine mispricing.
5. Show with arithmetic why a positive-expected-value position can still destroy capital when sized too large (volatility drag, ruin). Connect this to leverage in CRE.
6. Recognize "arbitrage" that is really speculation on execution, closing, or legging risk, and compute the minimum completion probability that justifies it.
7. Explain how information asymmetry (adverse selection) sets bid–ask spreads in securities and bid discipline in private real estate.
8. Judge decisions by their process rather than their outcome, and keep a decision record that makes that possible.

---

## 1.1 Opening investment problem: three opportunities on a Monday

You run a \$40 million discretionary real estate and markets account for a family office. On Monday morning three opportunities reach your desk. All facts below are [HYPOTHESIS] — a constructed teaching case.

**Opportunity A — the industrial building.** A broker offers a 100% leased, 140,000 sf warehouse in a Sun Belt metro at \$14.0 million. In-place NOI is \$875,000, a 6.25% going-in cap rate. The tenant has a seven-year remaining term with 3% annual bumps. A lender will provide 60% LTV at 6.50% on a 30-year amortization.

**Opportunity B — the hotel that must close.** A 110-room select-service hotel in a Texas secondary market is owned by an estate. The estate's \$6.1 million loan matures in 50 days and the lender has declined to extend. Your analysis, which Chapter 11 will teach you to replicate, says a patient, fully marketed sale would bring about \$9.0 million: trailing NOI after a 4% FF&E reserve of \$855,000, capitalized at 9.5%. The estate's broker says they will accept **\$7.8 million all cash with a 45-day close**, provided you waive most contingencies.

**Opportunity C — the "riskless" back-to-back.** A fund is selling a single-tenant net-leased retail building for \$5.0 million to close in 60 days. Separately, a 1031-exchange buyer has signed a letter of intent to buy the same building from you for \$5.4 million. The LOI is non-binding, and the buyer's deposit becomes non-refundable only after a 30-day inspection period that starts after your purchase. A junior colleague calls it "a \$400,000 arbitrage".

You also have the alternative every speculator always has: **do nothing**, hold Treasury bills, and wait.

By the end of the chapter you will be able to say what kind of activity each opportunity is, what you are being paid for, how much you could lose, and what you would need to believe to proceed. Section 1.10 returns to the decision.

---

## 1.2 Economic intuition: speculation is paid risk-bearing

The word *speculation* is used loosely, sometimes as an insult. Precise use matters because each activity requires a different analysis.

**Investment** in the narrow sense is the purchase of an asset whose expected return comes mainly from the **cash flows the asset produces**. The investor accepts the market's pricing of those cash flows. The warehouse in Opportunity A is an investment: you buy a 6.25% income stream with contractual growth, and most of your return over seven years is rent. You are not claiming the seller misjudged anything. You are accepting a market price for a risk you are willing to hold.

**Speculation** is taking a position whose expected return depends mainly on a **change in price**. That price change comes from one of three things: a change in expectations, the resolution of uncertainty, or the payment of a premium by someone who wants to shed risk or obtain immediacy. The speculator must answer a question the investor can partly avoid: *why is this price available to me?* Opportunity B is speculation. Its attraction is the gap between \$7.8 million today and \$9.0 million under patient marketing. That gap exists because the estate needs immediacy and you can supply it.

**Arbitrage** is the simultaneous purchase and sale of economically identical claims at different prices. When both legs are executed at once and settle against each other, it is riskless. True arbitrage is rare, small, and taken by those with the lowest transaction costs. Most of what is called arbitrage is **relative-value speculation**: positions in similar claims, or in identical claims that cannot be executed simultaneously. Opportunity C is a speculation on whether the second leg closes. Section 1.7 prices it.

**Hedging** is taking a position to reduce a pre-existing exposure. An owner of floating-rate hotel debt who buys an interest-rate cap is hedging. The hedger pays a premium in expected terms, and that premium is the speculator's compensation.

**Gambling** is taking risk in a game whose expected value to the participant is negative and which serves no risk-transfer function. The house edge is not compensation for bearing anyone else's risk. Gambling can also mean taking a positive-expected-value risk sized so that ruin becomes likely. Section 1.6 shows that the line between "speculation" and "gambling" often runs through position size, not through the asset.

### Risk transfer: why speculators are paid at all

In a market without speculators, a hedger must find another hedger with the opposite exposure, of the same size, on the same day. A wheat farmer would need a miller who wants to buy exactly when the farmer wants to sell. A forced hotel seller would need a strategic buyer who happens to be ready in 45 days. Speculators fill the gaps in time and size. They are paid through:

1. **Risk premia.** Expected compensation for holding risks that others want to shed. Examples are the term premium on long bonds, the equity premium, the illiquidity premium on private real estate, and insurance premia on volatility.
2. **Liquidity premia (the price of immediacy).** Compensation for transacting when someone else needs to and you do not.
3. **Information and analysis premia.** Returns from forming more accurate expectations than the marginal price-setter, using legal, public, or self-generated information. Chapter 2 and Appendix F treat the legal boundaries.

These three sources must be distinguished in every decision. They behave differently under stress. Risk premia are earned on average and lost in bad states. Liquidity premia are earned when you have liquidity, and they disappear exactly when you need liquidity yourself. Information premia exist only to the extent your information is not already in the price.

### Liquidity provision versus liquidity consumption

A **liquidity provider** stands ready to transact when others need to and is paid a spread or discount. A **liquidity consumer** demands immediate execution and pays for it. The same institution can be either, depending on the trade. A dealer quoting bonds provides liquidity. A fund meeting redemptions by selling the most liquid assets consumes it. In private real estate, buyers with committed capital, short closing periods, and the ability to waive financing contingencies provide liquidity. Sellers facing loan maturities, fund wind-downs, estate settlements, or partner disputes consume it.

The economic danger is that **liquidity provision is short a put on liquidity itself**. The provider earns small premia in normal conditions and suffers large losses when everyone wants immediacy at once. At those moments prices gap, financing disappears, and the provider's own capital is impaired. Section 1.9 examines 19 October 1987 from this perspective.

### Expected return versus realized return

A position's **expected return** is a probability-weighted average across scenarios. Its **realized return** is what one draw from that distribution delivers. A good decision can produce a bad outcome, and a bad decision can produce a good one. In a single CRE deal held for five years you observe exactly one draw. You therefore cannot learn much about your skill from the outcome of one deal. You need a record of the **expected** distribution you underwrote, so that outcomes can later be compared with forecasts (Chapter 20 develops calibration).

### Risk versus uncertainty

Frank Knight (1921) distinguished **risk**, where outcomes are random but the probabilities are knowable, from **uncertainty**, where the probabilities themselves are not known. A roulette wheel is risk. Whether a newly vacant suburban office tower re-leases within three years is uncertainty. There is no frequency table for that building, in that submarket, in that interest-rate regime.

Professional speculation operates mostly under uncertainty. Two tools make it tractable:

* The **break-even probability**: the probability of the bad state at which the decision has zero expected value. If your plausible range for that probability sits well below the break-even, the decision is robust to your ignorance. If the range straddles it, the decision hinges on a number you do not know. Either gather information or decline.
* **Scenario construction** with explicit mechanisms rather than statistical extrapolation. Chapter 20 develops this.

### Information asymmetry

When one party knows more than the other, the less-informed party must protect itself. In securities, dealers widen spreads because some counterparties are better informed (Glosten and Milgrom, 1985). In private real estate, buyers shade bids and insist on due diligence because the seller knows about the roof, the franchise PIP, the tenant who has told the property manager they are leaving, and the property-tax protest that failed. Akerlof (1970) showed that when quality cannot be verified, good assets withdraw from the market and prices fall toward the value of bad ones. Due diligence is the purchase of information that closes the asymmetry, and its price is worth calculating (Example 1.7).

### Process versus outcome

A professional speculator's unit of performance is the **decision**, not the trade. A decision is good if, given what was knowable at the time, the thesis was coherent, the expected value was positive after costs, the position was sized to survive adverse outcomes, and invalidation criteria were specified. Outcomes are feedback, but noisy feedback. The decision journal (Chapter 25 and `desk/trade_journal/`) records the forecast distribution *before* the outcome is known. Without it, hindsight rewrites what you thought.

---

## 1.3 Technical definitions

| Term | Definition |
|---|---|
| Expected value (EV) | $E[X] = \sum_s p_s x_s$ for discrete scenarios $s$ with probabilities $p_s$ summing to 1 |
| Standard deviation | $\sigma_X = \sqrt{\sum_s p_s (x_s - E[X])^2}$ |
| Probability of loss | $\sum_{s:\,x_s<0} p_s$ |
| Expected loss (partial expectation) | $\sum_{s:\,x_s<0} p_s x_s$, a negative number. Not the same as the average loss *given* a loss |
| Break-even probability | For a two-outcome decision with gain $G>0$ and loss $L>0$: $p^* = G/(G+L)$ is the probability of loss at which EV = 0 |
| Price of immediacy | The discount accepted to transact now rather than after an orderly process, expressed as an annualized rate over the time saved |
| Bid–ask spread | Ask minus bid. The half-spread is the expected revenue per trade to a market maker before adverse selection |
| Adverse selection | Losses to the less-informed party from trading disproportionately with better-informed counterparties |
| Arithmetic mean return | $\bar r = E[r]$ |
| Geometric (compound) growth rate | $g = \exp(E[\ln(1+r)]) - 1$. This is the growth rate of wealth for a repeated position |
| Volatility drag | $\bar r - g$. For small returns, approximately $\sigma^2/2$ |
| Kelly fraction | The fraction of wealth that maximizes $E[\ln(\text{wealth})]$ for a repeated bet. Chapter 21 explains why practitioners use less |
| Leg risk | The risk that one leg of a multi-leg trade executes and another does not, or does so at a worse price |
| Liquidity provider/consumer | A party supplying versus demanding immediacy |

---

## 1.4 Equations and derivations

### 1.4.1 Expected profit and the IRR of expected flows

For a hold of $T$ years with scenario-dependent cash flows $CF_{s,t}$:

$$E[\text{Profit}] = \sum_s p_s \Big(\sum_{t=0}^{T} CF_{s,t}\Big).$$

There are two different "expected IRRs":

* **Expected IRR**: $\sum_s p_s \, IRR_s$, the probability-weighted average of scenario IRRs.
* **IRR of expected cash flows**: the IRR of the vector $E[CF_t] = \sum_s p_s CF_{s,t}$.

They are generally unequal because IRR is a nonlinear function of the cash flows. Neither is "the" expected return. The IRR of expected flows is the more defensible single number, because it applies the expectation to cash before the nonlinear transformation. The distribution of scenario IRRs is more informative than either average. Committees should see the full distribution, not just a point estimate.

### 1.4.2 Break-even probability

Suppose a decision yields $+G$ with probability $1-p$ and $-L$ with probability $p$. Then

$$EV = (1-p)G - pL = 0 \;\;\Rightarrow\;\; p^* = \frac{G}{G+L}.$$

With more than two scenarios, fix the *relative* probabilities of the non-bad scenarios and solve for the bad-state probability $q^*$ that sets EV to zero:

$$EV(q) = (1-q)\,\bar G - q L = 0 \;\Rightarrow\; q^* = \frac{\bar G}{\bar G + L}, \qquad \bar G = \frac{\sum_{s \neq \text{bad}} p_s x_s}{\sum_{s\neq\text{bad}} p_s}.$$

Here $\bar G$ is the conditional expected profit given that the bad state does not occur.

### 1.4.3 The annualized price of immediacy

A seller who sells now receives net proceeds $N_0$. Selling patiently yields expected net proceeds $E[N_\tau]$ after an expected delay of $\tau$ years, net of carrying costs incurred during the wait. The implied annualized rate the seller pays for immediacy is

$$r_{imm} = \left(\frac{E[N_\tau]}{N_0}\right)^{1/\tau} - 1.$$

Two cautions apply. First, $E[N_\tau]$ should include the probability that the patient sale fails. Second, a high $r_{imm}$ does not prove the buyer is getting a bargain. It may compensate the buyer for risks the seller is also avoiding: diligence waivers, information asymmetry, financing risk.

### 1.4.4 Market-making with informed traders

A market maker quotes a half-spread $h$ around the value they expect. A fraction $\pi$ of incoming orders come from informed traders. After an informed trade, value moves by $\Delta$ against the market maker. Uninformed trades carry no information. Expected profit per trade is

$$E[\Pi] = h - \pi \Delta.$$

The competitive half-spread is $h^* = \pi\Delta$. Spreads widen when the share of informed flow rises or when information events are larger. This is why spreads widen ahead of data releases and in stressed markets. The CRE analog is the "diligence discount": the buyer's bid shading increases with the probability and size of undisclosed defects.

### 1.4.5 Growth versus expectation: volatility drag

Repeatedly committing a fraction $f$ of wealth to a position with per-period return $r$ grows wealth at the rate

$$g(f) = E[\ln(1 + f r)].$$

For a two-outcome bet returning $+a$ with probability $p$ and $-b$ with probability $1-p$:

$$g(f) = p\ln(1+fa) + (1-p)\ln(1-fb).$$

Setting $g'(f) = 0$ gives the Kelly fraction

$$f^* = \frac{p}{b} - \frac{1-p}{a}.$$

For small $f r$, the expansion $\ln(1+x) \approx x - x^2/2$ gives $g(f) \approx f\mu - \tfrac{1}{2} f^2 (\sigma^2 + \mu^2)$. Growth is quadratic in size and turns negative beyond roughly $2f^*$. **The same positive-EV opportunity is an investment at one size and a path to ruin at another.**

### 1.4.6 Leverage on equity returns

For an asset with total return $r_A$ financed with loan-to-value $\lambda$ at interest rate $r_D$, and ignoring amortization and transaction costs over one period:

$$r_E = \frac{r_A - \lambda r_D}{1-\lambda} = r_A + \frac{\lambda}{1-\lambda}(r_A - r_D).$$

Leverage scales both the spread $r_A - r_D$ and the dispersion of $r_A$ by $1/(1-\lambda)$. At 75% LTV, a 25% decline in asset value eliminates all equity. With non-recourse debt the equity return is floored at −100%. That floor is the limited-liability put. It raises the arithmetic mean of equity returns while compounded growth collapses (Problem 1.9).

### 1.4.7 Arbitrage with leg risk

If leg two completes with probability $\pi$ and yields profit $G$, and failure leaves a loss $L$:

$$EV = \pi G - (1-\pi)L, \qquad \pi^* = \frac{L}{G+L}.$$

This is the break-even equation from the other side. It shows directly that an "arbitrage" with completion risk is a probabilistic bet.

---

## 1.5 Worked examples

All seven examples are reproduced in `tests/test_ch01_examples.py`.

### Example 1.1 — Expected versus realized return on the hotel bid (Opportunity B)

**Given.** Purchase price \$7,800,000. Buyer closing costs 1.5% of price. All cash (unlevered), with leverage added in Chapter 10. Two-year hold. Selling costs 3% of gross sale price. Scenario NOI is after FF&E reserve, received at year-end. Sale at end of year 2.

| Scenario | Probability | NOI Y1 | NOI Y2 | Gross sale, end Y2 |
|---|---|---|---|---|
| Good: orderly market, modest RevPAR growth | 0.55 | \$780,000 | \$850,000 | \$9,400,000 |
| Base: flat market | 0.30 | \$760,000 | \$800,000 | \$8,600,000 |
| Bad: new supply plus a regional slowdown | 0.15 | \$650,000 | \$560,000 | \$6,400,000 |

**Find.** Profit and IRR in each scenario; expected profit, standard deviation, probability of loss; expected IRR and IRR of expected flows.

**Solution.**

All-in basis $= 7{,}800{,}000 \times 1.015 = \$7{,}917{,}000$.

Net sale proceeds $=$ gross $\times 0.97$:

* Good: $9{,}400{,}000 \times 0.97 = \$9{,}118{,}000$
* Base: $8{,}600{,}000 \times 0.97 = \$8{,}342{,}000$
* Bad: $6{,}400{,}000 \times 0.97 = \$6{,}208{,}000$

Profit = NOI Y1 + NOI Y2 + net sale − basis:

* Good: $780{,}000 + 850{,}000 + 9{,}118{,}000 - 7{,}917{,}000 = \$2{,}831{,}000$
* Base: $760{,}000 + 800{,}000 + 8{,}342{,}000 - 7{,}917{,}000 = \$1{,}985{,}000$
* Bad: $650{,}000 + 560{,}000 + 6{,}208{,}000 - 7{,}917{,}000 = -\$499{,}000$

Scenario IRRs solve $-7{,}917{,}000 + \frac{NOI_1}{1+IRR} + \frac{NOI_2 + \text{Net sale}}{(1+IRR)^2} = 0$:

| Scenario | Profit | IRR | Equity multiple |
|---|---|---|---|
| Good | \$2,831,000 | 17.24% | 1.358x |
| Base | \$1,985,000 | 12.37% | 1.251x |
| Bad | −\$499,000 | −3.34% | 0.937x |

Expected profit $= 0.55(2{,}831{,}000) + 0.30(1{,}985{,}000) + 0.15(-499{,}000) = 1{,}557{,}050 + 595{,}500 - 74{,}850 = \$2{,}077{,}700$.

Variance $= \sum p_s (x_s - 2{,}077{,}700)^2$, so the standard deviation is \$1,144,810. Probability of loss = 15%. Partial expected loss = $0.15 \times (-499{,}000) = -\$74{,}850$.

Expected IRR $= 0.55(17.24\%) + 0.30(12.37\%) + 0.15(-3.34\%) = 12.69\%$.

Expected cash flows: Year 1 $= 0.55(780{,}000) + 0.30(760{,}000) + 0.15(650{,}000) = \$754{,}500$. Year 2 $= E[NOI_2] + E[\text{Net sale}] = 791{,}500 + 8{,}448{,}700 = \$9{,}240{,}200$. The IRR of $[-7{,}917{,}000;\ 754{,}500;\ 9{,}240{,}200]$ is **12.90%**.

**Check.** The good-scenario IRR can be checked on a calculator. CF0 = −7,917,000; CF1 = 780,000; CF2 = 9,968,000. On an HP-12C: `7917000 CHS g CF0`, `780000 g CFj`, `9968000 g CFj`, `f IRR` → 17.24.

**Decision consequence.** The expected IRR is about 12.7–12.9% unlevered on a two-year hold, against a Treasury bill alternative yielding a fraction of that. Only one scenario will occur. If the bad scenario happens, you will lose about \$0.5 million. If your process was sound, that does not make the decision wrong, and a good outcome would not have made it right. What matters is whether the probabilities and scenario values were defensible *when you made them*. Write them down now, before you know.

### Example 1.2 — The break-even probability, and how one unknown fact moves it

**Given.** Example 1.1's three scenarios. Then a second case in which the franchisor will require a \$1.5 million property improvement plan (PIP) on change of ownership, which your diligence has not yet confirmed. Model the PIP as reducing profit by \$1.5 million in every scenario. This ignores timing and any revenue uplift from the renovation; Chapter 11 refines it.

**Find.** The break-even probability of the bad scenario, with and without the PIP.

**Solution (no PIP).**

Two-state collapse using only Good versus Bad: $p^* = G/(G+L) = 2{,}831{,}000/(2{,}831{,}000 + 499{,}000) = 85.0\%$.

Three-state version, keeping Good:Base at 55:30. The conditional expected profit if not Bad is $\bar G = (55 \times 2{,}831{,}000 + 30 \times 1{,}985{,}000)/85 = \$2{,}532{,}412$. Then $q^* = \bar G/(\bar G + L) = 2{,}532{,}412/(2{,}532{,}412 + 499{,}000) = 83.5\%$.

**Solution (with PIP).** Profits become Good \$1,331,000, Base \$485,000, Bad −\$1,999,000.

* Expected profit at the original probabilities: $0.55(1{,}331{,}000) + 0.30(485{,}000) + 0.15(-1{,}999{,}000) = \$577{,}700$.
* $\bar G = (55 \times 1{,}331{,}000 + 30 \times 485{,}000)/85 = \$1{,}032{,}412$.
* $q^* = 1{,}032{,}412/(1{,}032{,}412 + 1{,}999{,}000) = 34.1\%$.

**Decision consequence.** Without the PIP, the bad state would need to be more than 83% likely before the bid lost money in expectation. No reasonable view of a 15% bad-state probability is near that. The decision is robust to Knightian uncertainty about the bad state. With an unconfirmed \$1.5 million PIP, the break-even falls to 34%. A plausible recession probability for a two-year horizon can approach that number. The decision now depends on a figure you do not know. **The single most valuable action is to obtain the franchise transfer terms before bidding firm.** A phone call to the brand's franchise-sales office, or a request for the current PIP letter, is worth far more than refining the cap-rate assumption. Break-even analysis identifies which piece of information to buy next.

### Example 1.3 — The price of immediacy: what the estate is paying you

**Given.** The estate's alternatives:

* *Quick sale:* \$7,800,000 in 45 days, with seller costs of 1.0% (attorney, title, no broker co-op): net $N_0 = 7{,}800{,}000 \times 0.99 = \$7{,}722{,}000$.
* *Patient sale:* The lender grants a forbearance with a \$250,000 fee and default-interest cost. The hotel is fully marketed. With probability 0.80 it sells for \$9.0 million gross after 6 months. With probability 0.20 the first buyer fails and it sells for \$8.4 million after 9 months. Seller costs 3%.

**Find.** The annualized price of immediacy, $r_{imm}$.

**Solution.**

Expected gross proceeds $= 0.80(9{,}000{,}000) + 0.20(8{,}400{,}000) = \$8{,}880{,}000$.

Expected net proceeds $= 8{,}880{,}000 \times 0.97 - 250{,}000 = \$8{,}363{,}600$.

Expected delay $\tau = 0.80(0.5) + 0.20(0.75) = 0.55$ years.

$$r_{imm} = \left(\frac{8{,}363{,}600}{7{,}722{,}000}\right)^{1/0.55} - 1 = (1.08309)^{1.8182} - 1 = 15.62\%.$$

**Check.** Continuous-compounding version: $\ln(1.08309)/0.55 = 14.51\%$, which is consistent with a discrete rate of 15.6%. Using the expected delay rather than integrating over the two delays is an approximation; Problem 1.6 asks you to bound the error.

**Decision consequence.** The estate pays an implied 15.6% annualized for certainty and speed. The figure is meaningful only relative to the risks the buyer absorbs. You waive contingencies and therefore carry the information-asymmetry risk of Example 1.7. You bear two years of market risk. You may be unable to finance the purchase on a 45-day timeline. A 15.6% implied rate is not an "arbitrage"; it is a premium. Ask whether it is enough. Ask also whether the lender's refusal to extend is itself information about the asset.

### Example 1.4 — Why spreads exist: the market maker and the informed trader

**Given.** A dealer in an off-the-run corporate bond quotes 100.00 bid / 100.10 ask, so the half-spread is $h = 0.05$ points. Twenty percent of customer orders ($\pi = 0.20$) come from investors with genuinely better information. After their trades the bond's value moves 0.40 points ($\Delta$) against the dealer. Uninformed orders move nothing.

**Find.** The dealer's expected profit per trade and the competitive half-spread.

**Solution.** $E[\Pi] = h - \pi\Delta = 0.05 - 0.20 \times 0.40 = -0.03$ points per trade. The dealer loses money. The break-even half-spread is $h^* = \pi\Delta = 0.08$, a quoted spread of 0.16 points.

**Decision consequence.** The spread is not a toll the dealer collects for free. It is the price of trading against people who may know more. When you are the *informed* side, you pay a spread that is cheap relative to your information. When you are uninformed, wide spreads protect the dealer from you, and your realized trading cost will exceed the quoted half-spread. In private CRE, a buyer who is asked to waive diligence is being asked to post a zero spread to a counterparty who has better information. A rational buyer widens the bid, which means lowering it, by the expected value of what they cannot verify.

### Example 1.5 — Positive expected value, negative growth: where speculation turns into gambling

**Given.** A repeated opportunity returns +60% or −50% on the capital committed, each with probability ½. Compare an American roulette single-number bet, which pays 35 to 1 with win probability 1/38.

**Find.** The expected return of each. For the speculation, find the compound growth rate of wealth at commitment fractions $f$ = 0.10, $f^*$, 0.25, 0.50, 1.00, and 1.50 (the last means 50% borrowed on top of equity).

**Solution.**

Roulette: $E[r] = \frac{1}{38}(35) + \frac{37}{38}(-1) = -2/38 = -5.26\%$ per bet. No sizing rule makes a negative-EV bet worth taking for profit.

Speculation: $E[r] = 0.5(0.60) + 0.5(-0.50) = +5.0\%$ per period, which is positive.

Kelly fraction: $f^* = p/b - (1-p)/a = 0.5/0.5 - 0.5/0.6 = 1 - 0.8333 = 0.1667$.

Growth $g(f) = 0.5\ln(1 + 0.6f) + 0.5\ln(1 - 0.5f)$:

| $f$ | $g(f)$ (log) | Compound growth per period | Median wealth after 10 periods (from 1.00) |
|---|---|---|---|
| 0.10 | 0.003488 | +0.35% | 1.035 |
| 0.1667 ($f^*$) | 0.004149 | +0.42% | 1.042 |
| 0.25 | 0.003115 | +0.31% | 1.032 |
| 0.50 | −0.012659 | −1.26% | 0.881 |
| 1.00 | −0.111572 | −10.56% | 0.328 |
| 1.50 | −0.372220 | −31.08% | 0.024 |

At $f = 1$: $g = 0.5\ln 1.6 + 0.5\ln 0.5 = \ln\sqrt{0.8}$, so wealth compounds at $\sqrt{0.8} - 1 = -10.56\%$ per period even though each period's expected return is +5%. After ten periods the median outcome is $0.8^5 = 0.328$.

**Check.** With five wins and five losses in ten periods at $f=1$: $1.6^5 \times 0.5^5 = 0.8^5 = 0.32768$. ✓

**Decision consequence.** Arithmetic expected return is the wrong objective for a speculator who must survive many decisions. A positive-EV opportunity sized at 100% of capital is, for practical purposes, a bet against your own survival. The CRE parallel is direct. A 75–85% LTV acquisition turns modest asset volatility into large equity volatility, and the limited-liability floor flatters arithmetic averages (Problem 1.9). Section 1.6 returns to leverage, and Chapter 21 treats sizing formally, including why full Kelly is too aggressive when probabilities are estimated with error.

### Example 1.6 — The "riskless" back-to-back (Opportunity C)

**Given.** Purchase at \$5,000,000 with 1.5% buyer costs, so basis = \$5,075,000, all cash. If the 1031 buyer closes (probability $\pi = 0.70$), you sell at \$5,400,000 less 2% costs. If the buyer walks, you hold six months, collect \$150,000 of net rent, and sell at an expected \$4,900,000 gross less 2% costs. The lower price reflects a thinner buyer pool without an exchange buyer who must place funds.

**Find.** Profit in each case, EV, and the minimum completion probability $\pi^*$.

**Solution.**

* Completes: $5{,}400{,}000 \times 0.98 - 5{,}075{,}000 = 5{,}292{,}000 - 5{,}075{,}000 = +\$217{,}000$.
* Walks: $4{,}900{,}000 \times 0.98 + 150{,}000 - 5{,}075{,}000 = 4{,}802{,}000 + 150{,}000 - 5{,}075{,}000 = -\$123{,}000$.
* $EV = 0.70(217{,}000) + 0.30(-123{,}000) = 151{,}900 - 36{,}900 = +\$115{,}000$.
* $\pi^* = L/(G+L) = 123{,}000/(217{,}000 + 123{,}000) = 36.2\%$.

Sensitivity: if the fallback sale price is \$4.6 million rather than \$4.9 million, the walk-away loss becomes −\$417,000 and EV falls to $0.70(217{,}000) + 0.30(-417{,}000) = \$26{,}800$.

**Decision consequence.** The "\$400,000 arbitrage" is \$217,000 after costs if everything works. It is a probabilistic trade with an expected value of about \$115,000 on \$5.1 million of capital tied up for two to six months. Its EV is highly sensitive to the fallback price, about which you know little. It is speculation on the behavior of a counterparty who has made no binding commitment. A disciplined desk would do one of three things: (a) obtain a hard deposit from the 1031 buyer at signing, which converts leg risk into credit risk; (b) negotiate a longer close with the fund to align the two timelines; or (c) size the position as a speculation rather than as an arbitrage. "Arbitrage" in a pitch should prompt one question: *what happens if one leg fails?*

### Example 1.7 — Information asymmetry: the lemons problem in hotel sales

**Given.** In a submarket, 60% of the hotels coming to market are "clean", worth \$10.0 million to a buyer. Forty percent carry undisclosed deferred capital needs and an imminent brand PIP, and are worth \$8.5 million. Sellers know their type; buyers cannot tell without diligence. Clean sellers will not accept less than \$9.8 million. Lemon owners will sell at any price above \$8.4 million.

**Find.** The pooling price a risk-neutral buyer would offer without diligence, and what happens at that price. Then find the value of diligence that perfectly reveals type at a cost of \$40,000.

**Solution.**

Pooling price $= 0.60(10.0) + 0.40(8.5) = \$9.40$ million.

At \$9.40 million clean sellers withdraw, because $9.40 < 9.80$. The only sellers who accept are lemons, worth \$8.5 million. A buyer who pays \$9.40 million loses \$0.90 million on every hotel bought. Anticipating this, buyers bid \$8.5 million, and only lemons trade. The market for clean hotels "unravels" (Akerlof, 1970).

With diligence costing \$40,000 per hotel, the buyer can identify clean hotels and pay up to \$10.0 million less diligence cost. Clean sellers asking \$9.8 million are then willing to trade. The buyer's surplus on a clean purchase at \$9.8 million is $10.0 - 9.8 - 0.04 = \$0.16$ million. Diligence creates a market that otherwise would not exist.

**Decision consequence.** Return to Opportunity B. The estate asks you to *waive most contingencies*. Reasoning as Akerlof did, ask whether a clean asset worth \$9.0 million would need to be sold this way. A forced timeline is one explanation. Hidden defects are another. The discount you are offered could be compensation for immediacy (Example 1.3), compensation for asymmetric information (this example), or both. Your bid should not assume it is all the former. Practical responses include a short, focused diligence period (PCA, franchise PIP letter, tax and lien searches, a review of the STR report and the last two years of P&Ls), a holdback or escrow, or a lower price.

---

## 1.6 CRE application: leverage converts investment into speculation

The industrial building (Opportunity A) is an investment at 0% leverage. Most of its return comes from contractual rent paid by a creditworthy tenant. Finance it at 85% LTV and the same building becomes a speculation on refinancing conditions, exit cap rates, and tenant renewal, because small changes in asset value now dominate the equity outcome.

Use equation 1.4.6 with Opportunity A's going-in cap rate of 6.25% and a debt rate of 6.50%. Ignore amortization for the moment; Chapter 10 adds it. In the first year:

* Unlevered income return = 6.25%.
* At 60% LTV, levered income return $= (6.25\% - 0.60 \times 6.50\%)/0.40 = (6.25\% - 3.90\%)/0.40 = 5.875\%$.

Leverage is **negative** on a current-income basis because the asset yields less than the debt costs. The levered investor is therefore relying on appreciation: rent bumps, cap-rate compression, or both. That reliance is a speculative component. It may be reasonable, since 3% bumps on a 6.25% yield imply an unlevered return near 9% if the exit cap equals the entry cap. But it should be stated as a forecast, not hidden inside a single IRR.

With amortization the first-year cash yield is lower still. On a \$8.4 million loan at 6.50% over 30 years, monthly payment = \$53,094 and annual debt service = \$637,125. Cash flow after debt service is $875{,}000 - 637{,}125 = \$237{,}875$ on equity of \$5.6 million, a cash-on-cash return of 4.25%. Part of debt service is amortization, which is retained in the equity. The 4.25% is a cash yield, not a total return.

**Question to carry forward.** If you accept a cash yield below the Treasury yield, what are you speculating on, and how would you know you were wrong? Chapter 6 compares cap rates with Treasury yields directly. Chapter 10 builds the refinancing analysis.

---

## 1.7 When the conventional relationships fail

The definitions above are clean. Markets are not.

1. **Hedges turn into speculations.** A hedge is defined by the exposure it offsets. If the underlying exposure changes, the hedge becomes a naked position. Examples are a hotel sold before its rate cap expires and a construction loan repaid early. Metallgesellschaft's 1993 losses on its rolling energy-futures hedge are a standard case of a hedge whose funding and timing mismatches produced liquidity stress. Culp and Miller (1995) and Mello and Parsons (1995) disagree on whether the hedge was economically sound, which itself shows how hard the classification can be.
2. **Liquidity premia invert.** The liquidity provider is paid in calm markets and pays in crises. Capital that "always" buys from forced sellers is itself forced to sell when its lenders pull lines.
3. **Arbitrages fail through financing, not logic.** Two claims can converge in theory and diverge in practice for longer than the arbitrageur can fund the position. Shleifer and Vishny (1997) call these the limits of arbitrage. Chapter 23's LTCM case is the canonical example.
4. **Expected-value reasoning fails when probabilities are not meaningful.** For one-off events with no reference class, a stated probability can be false precision. Break-even analysis is more robust than point estimates in these cases.
5. **Information asymmetry can run in your favor without your knowledge.** A seller may underprice an asset because *they* lack information, for example an estate's executor who does not know the brand has approved a conversion. Exploiting public or diligence-derived information is legitimate. Trading on material nonpublic information obtained in breach of a duty is not (Appendix F).
6. **Process can be good and the reference class wrong.** A disciplined process that uses 1995–2019 base rates for interest-rate moves would have badly underestimated 2022 (Chapter 23).

---

## 1.8 What distinguishes professional speculation from gambling

| Criterion | Professional speculation | Gambling |
|---|---|---|
| Source of expected return | Risk premium, liquidity premium, or analytical edge that can be articulated | House edge against the participant; none |
| Expected value after costs | Positive, with stated assumptions | Negative, or positive but sized for ruin |
| Sizing | Survives plausible adverse sequences; fraction of Kelly | Large relative to capital; "all in" |
| Invalidation | Stated before entry | Absent; losses are "temporary" |
| Record | Pre-decision forecast distribution | Outcome memory only |
| Economic function | Transfers risk, supplies liquidity, improves price discovery | Entertainment or transfer to the house |

Test any proposed position against all six rows. A single failure, especially on sizing or invalidation, should stop the trade until it is fixed.

---

## 1.9 Historical episode: 19 October 1987 — liquidity consumers meet absent liquidity providers

**Date and environment.** In the first three quarters of 1987, U.S. equities rose sharply while long-term interest rates rose. The dollar was under pressure, and U.S. trade deficits were a political issue [FACT: general context documented in the Federal Reserve History essay cited below; the detailed rate path is to be verified against FRED series GS10 *(verification pending)*].

**What happened.** On Monday, 19 October 1987, the Dow Jones Industrial Average fell 508 points, or 22.6%, the largest one-day percentage decline in its history [FACT; Federal Reserve History, "Stock Market Crash of 1987", VERIFIED-SECONDARY]. On the morning of 20 October the Federal Reserve issued a brief statement affirming its readiness to serve as a source of liquidity to support the economic and financial system [FACT; same source; exact wording to be checked against the Fed's published statement *(verification pending)*].

**Participants and mechanisms.**

* **Portfolio insurers** ran dynamic hedging programs that replicated a put option by selling stock-index futures as prices fell. Their selling was mechanical and largely insensitive to price. In option terms they were liquidity *consumers* whose demand rose as prices fell [FACT that these strategies existed and were a major focus of the post-crash inquiry: *Report of the Presidential Task Force on Market Mechanisms* (the "Brady Report"), January 1988; the magnitude of their selling is disputed — see below].
* **Index arbitrageurs** bought cheap futures and sold the underlying stocks. That transmitted futures selling into the stock market [FACT: Brady Report].
* **Specialists and market makers**, the designated liquidity providers, faced order imbalances far larger than their capital, and some stocks opened late or not at all [FACT: Brady Report].

**Competing interpretations.** The Brady Report emphasized portfolio insurance and the linkage between futures and stocks. The Chicago Mercantile Exchange's own studies argued that the futures market transmitted rather than caused the selling, and that cash-market selling by other investors was larger [INFERENCE from the existence of the dispute, documented in the CME's 1988 reports and in Miller's later writing; the specific shares of total selling attributed to each group are left *(verification pending)* until checked against the primary reports]. Shiller's surveys of investors during the crash found that many sellers reported reacting to the price decline itself rather than to news [FACT: Shiller, *Market Volatility*, 1989, ch. 23; VERIFIED-SECONDARY].

**What was knowable beforehand?** That portfolio insurance programs existed and would sell into declines was publicly discussed before October 1987 [REASONABLE INFERENCE: the strategy was commercially marketed]. What was not knowable was the *aggregate* size of mechanical selling relative to the capital of liquidity providers on a given day. That is the crucial quantity, and it is generally unobservable in advance. No one could know the date.

**What the case does and does not establish.** It establishes that a market's ability to absorb selling depends on the balance of price-sensitive liquidity providers and price-insensitive liquidity consumers, and that this balance can change abruptly. It does **not** establish that mechanical hedging *caused* the crash, a point that remains disputed. Nor does it establish that similar crashes are predictable from positioning data.

**CRE connection.** Private real estate has no specialist and no circuit breaker. When forced sellers (maturing loans, redemption queues in open-end funds) meet absent buyers, the result is not a 22% day. It is a market with **no transactions**. Appraisals go stale and price discovery happens slowly through the few trades that do occur (Chapter 2). The economics are the same, but the clock runs in months instead of hours.

---

## 1.10 Decision exercise: allocate the Monday capital

Return to the three opportunities, and assume you have \$12 million of deployable capital this month. Opportunity B requires about \$7.9 million all cash, which leaves room for acquisition financing later. Opportunity A requires \$5.6 million of equity at 60% LTV. Opportunity C requires \$5.1 million for two to six months.

Complete the decision on the template at `desk/investment_memos/decision_record_template.md`. Your record must include:

1. The classification of each opportunity and the premium it pays (risk, liquidity, or information).
2. For B: whether you would bid \$7.8 million *before* obtaining the franchise PIP letter, and the maximum price you would pay if a \$1.5 million PIP is confirmed.
3. For C: the minimum deposit you would require from the 1031 buyer to proceed.
4. For A: what you are speculating on at 60% LTV, and whether the same building is worth owning at 0% LTV versus Treasuries.
5. What you will *not* do, and why. Abstention is a legitimate answer for any of the three.
6. Invalidation criteria for anything you do.

**Rubric (see `problems/solutions/ch01_solutions.md` §Decision exercise).** Full credit requires that B be conditional on the PIP information. It requires that C be resized or restructured rather than called "arbitrage". It requires that A's levered return be decomposed into income and appreciation forecasts. It requires an explicit comparison with the risk-free alternative. There is no single correct allocation.

---

## 1.11 Frequent analytical errors

1. **Treating the expected IRR as the return you will earn.** You will earn one draw. Report the distribution.
2. **Averaging IRRs and calling it the expected return.** Distinguish the expected IRR from the IRR of expected flows, and give both when they differ materially.
3. **Calling a trade with execution risk "arbitrage".** Ask what happens if one leg fails.
4. **Ignoring the cause of a discount.** A forced-sale discount can be a liquidity premium, an information-asymmetry discount, or both.
5. **Equating positive EV with a good position.** Size determines whether a positive-EV position compounds or ruins.
6. **Judging a decision by its outcome.** Without a written ex-ante distribution, you cannot evaluate your own process.
7. **Mistaking leverage for return.** Negative leverage (asset yield below debt cost) means the levered return depends on appreciation.
8. **False precision under uncertainty.** A probability quoted to two decimals for a one-off event is often a disguised guess. Use break-even analysis.
9. **Forgetting transaction costs.** Buyer and seller costs of 1–3% each can absorb most of the edge in short holds.

---

## 1.12 Connections to other chapters

* Chapter 2 develops price formation and why appraisal-based CRE prices lag.
* Chapter 3 formalizes Bayesian updating, reflexivity, and forced selling.
* Chapter 10 adds amortization, refinancing, and debt-sizing to the leverage analysis of §1.6.
* Chapter 11 values Opportunity B's hotel properly: normalization, PIP, franchise, reserve.
* Chapter 20 formalizes scenario trees, calibration, and decision theory.
* Chapter 21 treats Kelly sizing, drawdowns, and ruin.
* Chapter 23 examines 1987, LTCM, and 2008 in full.
* Case A (`cases/hypothetical/case_A_overpriced_hotel_owner/`) applies these ideas to a seller anchored to original cost.

---

## 1.13 One-page reference sheet

**Classification questions:** What risk am I bearing? Who pays me to bear it? Why is this price available to me? What happens if a leg fails?

| Formula | Expression |
|---|---|
| Expected value | $E[X] = \sum p_s x_s$ |
| Std. deviation | $\sqrt{\sum p_s (x_s - E[X])^2}$ |
| Break-even bad-state probability | $p^* = G/(G+L)$ |
| Multi-scenario break-even | $q^* = \bar G/(\bar G + L)$, with $\bar G$ = expected profit given not bad |
| Leg-completion break-even | $\pi^* = L/(G+L)$ |
| Price of immediacy | $r_{imm} = (E[N_\tau]/N_0)^{1/\tau} - 1$ |
| Market maker | $E[\Pi] = h - \pi\Delta$; $h^* = \pi\Delta$ |
| Growth rate | $g(f) = E[\ln(1+fr)]$ |
| Kelly (two outcomes $+a$/$-b$) | $f^* = p/b - (1-p)/a$ |
| Volatility drag (approx.) | $\bar r - g \approx \sigma^2/2$ |
| Levered return | $r_E = r_A + \frac{\lambda}{1-\lambda}(r_A - r_D)$ |
| Recovery after loss $d$ | $1/(1-d) - 1$ |

**Rules of thumb (to be tested, not trusted).** A 50% loss needs a 100% gain to recover. At 75% LTV, a 25% fall in value eliminates equity. Doubling position size roughly quadruples the variance penalty in growth.

---

## References for this chapter

All sources are recorded in `SOURCE_REGISTER.md` with verification status.

* Akerlof, G. A. (1970). "The Market for 'Lemons': Quality Uncertainty and the Market Mechanism." *Quarterly Journal of Economics*, 84(3), 488–500.
* Glosten, L. R., and Milgrom, P. R. (1985). "Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders." *Journal of Financial Economics*, 14(1), 71–100.
* Knight, F. H. (1921). *Risk, Uncertainty and Profit*. Boston: Houghton Mifflin.
* Kelly, J. L. (1956). "A New Interpretation of Information Rate." *Bell System Technical Journal*, 35(4), 917–926.
* Shleifer, A., and Vishny, R. W. (1997). "The Limits of Arbitrage." *Journal of Finance*, 52(1), 35–55.
* Presidential Task Force on Market Mechanisms (1988). *Report of the Presidential Task Force on Market Mechanisms* ("Brady Report"). Washington, DC: U.S. Government Printing Office. Archived at https://www.sechistorical.org/collection/papers/1980/1988_0101_BradyReport.pdf.
* Federal Reserve History. "Stock Market Crash of 1987." https://www.federalreservehistory.org/essays/stock-market-crash-of-1987 (accessed 2026-10-19).
* Shiller, R. J. (1989). *Market Volatility*. Cambridge, MA: MIT Press.
* Culp, C. L., and Miller, M. H. (1995). "Metallgesellschaft and the Economics of Synthetic Storage." *Journal of Applied Corporate Finance*, 7(4), 62–76.
* Mello, A. S., and Parsons, J. E. (1995). "Maturity Structure of a Hedge Matters: Lessons from the Metallgesellschaft Debacle." *Journal of Applied Corporate Finance*, 8(1), 106–120.
