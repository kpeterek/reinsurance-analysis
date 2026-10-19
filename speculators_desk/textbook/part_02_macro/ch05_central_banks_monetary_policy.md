# Chapter 5 — Central Banks and Monetary Policy

> **Status:** Complete (v1.0). Numerical examples are reproduced in `tests/test_ch05_examples.py`. Problems are in `problems/questions/ch05_problems.md` and solutions in `problems/solutions/ch05_solutions.md`. Sources are listed in `references/sources_ch05.md` (IDs ch05-S01 to ch05-S22). Three items remain *(verification pending)* and are flagged where they appear: the exact peak-to-trough decline in a commercial property price index, the exact statutory wording of the Federal Reserve Act's monetary-policy objectives, and the current text of the FOMC's strategy statement after its 2025 review.

## Learning objectives

After this chapter you should be able to:

1. Describe how the Federal Reserve sets the overnight rate in an ample-reserves regime: the target range, interest on reserve balances (IORB), the overnight reverse repo facility (ON RRP), the standing repo facility (SRF), and the discount window. Explain why each administered rate sits where it does and which market rates it pins.
2. Compute a Taylor-rule prescription and its main variants (balanced-approach, inertial), and quantify how uncertainty about the neutral rate and the choice of inflation measure widen the prescription band.
3. Move between nominal rates, real rates, and inflation compensation with the exact Fisher relation. Interpret a TIPS breakeven, and say what it is not.
4. Price CME 30-Day Federal Funds futures as 100 minus the average daily effective rate for the month. Back out the market-implied probability of a policy move at a meeting with correct day-weighting, and cross-check it with the following month's contract.
5. Read the Treasury curve as expected policy plus a term premium. Compute an implied forward rate and decompose a long yield.
6. Trace the three channels by which policy reaches a CRE deal: (i) policy rate → SOFR → floating coupon → DSCR; (ii) 10-year Treasury → fixed coupon → loan constant → DSCR-sized proceeds; (iii) bank capital, liquidity, and lending standards → credit availability. Quantify the first two.
7. Explain the balance-sheet mechanics of quantitative easing and tightening, and state honestly how uncertain their term-premium effects are.
8. Use the 2022–23 tightening cycle as evidence, separating what was knowable at each date from what is known now.

---

## 5.1 Opening investment problem: a hotel refinance in a hiking month

It is a Thursday in the third week of the month. You advise the owner of a 210-room select-service hotel. All deal facts in this section are [HYPOTHESIS].

* The hotel's trailing NOI after a 4% FF&E reserve is \$2.4 million.
* The existing \$30.0 million floating-rate loan was originated three years ago at one-month Term SOFR + 3.00%, interest-only. It matures in seven months. The rate cap bought at origination is struck at 3.00% and expires with the loan.
* A life-company lender has quoted a 10-year fixed-rate refinance at the 10-year Treasury plus 2.00%, 30-year amortization, sized to the lesser of 65% LTV, 1.25x DSCR, and an 8.0% debt yield. The rate is set at closing, not today.
* A debt fund will extend the floating loan for 18 months at SOFR + 3.50%, conditional on a new cap.

The FOMC meets in eleven days. The fed funds futures contract for the meeting month implies a meaningful probability of a 25 bp hike. Overnight a consumer-price report surprised to the upside. The 10-year Treasury rose 15 bp on the release.

Three questions define the decision.

1. **What does the market expect the Fed to do, and how sure is it?** You need a probability, not a headline.
2. **Which loan is more exposed to the next move: the fixed refinance (priced off the 10-year) or the floating extension (priced off SOFR)?** The answer depends on which part of the curve the inflation surprise moves.
3. **What has already been priced?** If the futures already imply a hike, a hike that arrives will not move SOFR forwards much. What moves forwards is a surprise relative to that pricing.

The chapter builds the tools to answer each question with numbers. Example 5.4 computes the probability. Examples 5.6 and 5.7 size the two loans. Section 5.10 returns to the decision.

---

## 5.2 Economic intuition

### What a central bank actually controls

The Federal Reserve does not set mortgage rates, cap rates, or the 10-year Treasury yield. It sets a handful of **administered rates** on its own facilities. Through arbitrage, those rates anchor the price of overnight money. Everything else a CRE investor cares about is a market price that *depends on* the expected path of that overnight rate, plus compensation for risk.

Three layers matter:

| Layer | Who sets it | Example | How quickly policy reaches it |
|---|---|---|---|
| Overnight rates | Administered rates + arbitrage | EFFR, SOFR | Same day as the decision takes effect |
| Term risk-free rates | Market: expected path of overnight rates + term premium | 2-year and 10-year Treasury | Continuously, *before* decisions, on expectations |
| Risky rates and availability | Market and lenders: risk-free + credit spread + quantity rationing | CMBS coupons, bank loan spreads, LTV limits | Spreads immediately; lending standards over quarters |

The intuition for the speculator: **policy decisions are mostly priced before they happen**. Rate decisions that match expectations move little. What moves markets is news about the *path*: a data surprise, a change in guidance, a change in the reaction function. Then a CRE transaction market, which has no continuous price, absorbs that news over months.

### Why the policy rate matters for a property

A property's value is the present value of its NOI. Monetary policy enters through three doors.

1. **Discount rate.** Higher real risk-free rates raise the required return unless risk premia compress or expected growth rises. Cap rates are linked to long real yields, but the link is loose and lagged (Chapter 6).
2. **Debt cost and debt quantity.** Floating coupons reset with SOFR. Fixed coupons are set off the 10-year at closing. Higher coupons raise the loan constant, and with DSCR sizing they cut proceeds. Lower proceeds mean more equity per deal, fewer qualified buyers, and lower prices.
3. **Credit availability.** When tighter policy erodes bank capital (unrealized losses on securities), raises deposit costs, or triggers deposit flight, banks tighten standards. A borrower may face a lower LTV, a higher DSCR hurdle, or no quote at all. This channel is non-linear. It operates through quantities, not prices, and it is where CRE distress begins.

### Why an inflation surprise is a policy event

When inflation surprises upward, the market raises its estimate of the policy path. Short rates rise most if the surprise changes the next few meetings. Long rates rise if it changes the perceived persistence of inflation or the term premium. A hotel owner with a floating loan is exposed to the front end. A seller whose buyer needs fixed-rate debt is exposed to the 10-year. A sponsor with a bank relationship is exposed to whatever the shock does to the bank's balance sheet. Case H (`cases/hypothetical/case_H_cross_asset_macro_shock/`) traces one such shock across an entire portfolio.

---

## 5.3 Technical definitions

| Term | Definition |
|---|---|
| Dual mandate | The FOMC's statutory goals of maximum employment and stable prices. The statute also lists moderate long-term interest rates *(exact statutory wording, Federal Reserve Act §2A: verification pending)* [ch05-S21]. |
| Longer-run inflation goal | 2% inflation as measured by the annual change in the PCE price index, first stated in January 2012 and reaffirmed since [FACT; ch05-S20]. The surrounding strategy text was revised in 2020 and reviewed again in 2025 *(current wording: verification pending)*. |
| FOMC | Federal Open Market Committee. Twelve voting members: the seven Governors, the President of the New York Fed, and four of the other eleven Reserve Bank presidents on a rotating one-year basis. Eight scheduled meetings per year, normally two days long [FACT; ch05-S19]. |
| Target range | The 25 bp range the FOMC sets for the federal funds rate, for example 3.75%–4.00%. |
| EFFR | Effective federal funds rate: the volume-weighted median rate on overnight unsecured fed funds trades, published by the New York Fed. |
| IORB | Interest on reserve balances, paid by the Fed to banks on reserves. The principal tool for keeping EFFR in the range. Set by the Board. |
| ON RRP | Overnight reverse repurchase facility. Eligible non-banks (money funds, GSEs) lend cash to the Fed overnight against Treasury collateral at the offering rate. Sets a soft floor for money-market rates. |
| SRF | Standing repo facility. The Fed lends cash overnight against Treasuries, agency debt, and agency MBS at a fixed rate. A ceiling-type backstop for repo rates. Established 28 July 2021 [FACT; ch05-S09]. |
| Primary credit (discount window) | Fully secured lending to sound depository institutions, at the primary credit rate. |
| SOFR | Secured Overnight Financing Rate: a broad measure of overnight Treasury repo rates, published by the New York Fed. The base rate for most U.S. floating CRE loans. Term SOFR is a forward-looking term rate derived from SOFR derivatives. |
| Neutral rate $r^*$ | The real policy rate consistent with output at potential and stable inflation. Unobservable. Estimated with wide error bands. |
| Breakeven inflation | Nominal Treasury yield minus TIPS real yield of the same maturity. Inflation *compensation*: expected inflation plus an inflation risk premium, minus a TIPS liquidity premium. |
| Term premium | The extra yield investors demand to hold a long bond rather than roll short bills over the same horizon. Not directly observable. Model-dependent. |
| QE / QT | Quantitative easing: Fed purchases of long-duration securities paid for by creating reserves. Quantitative tightening: allowing securities to mature without reinvestment, which drains reserves. |
| Fed funds futures | CME 30-Day Federal Funds futures. Price $= 100 - R$, where $R$ is the arithmetic average of daily EFFR over the contract month. \$4,167 per index point, which is \$41.67 per basis point [FACT; ch05-S11]. |

---

## 5.4 Equations and derivations

### 5.4.1 The policy corridor in an ample-reserves regime

Since 2008 the Fed has operated with abundant reserves. In that regime the quantity of reserves does not pin the overnight rate at the margin. Administered rates do.

* **IORB** gives banks a risk-free overnight return on reserves. A bank will not lend fed funds much below IORB, because it can earn IORB instead. It will borrow fed funds from institutions that cannot earn IORB (chiefly the Federal Home Loan Banks) whenever it can borrow below IORB. Arbitrage profit per dollar per day $= (IORB - r_{ff})/360$.
* **ON RRP** offers non-banks a risk-free overnight rate. A money fund will not lend in repo below the ON RRP offering rate. That puts a soft floor under SOFR and other overnight secured rates.
* **SRF** and **primary credit** let eligible institutions borrow from the Fed at a fixed rate. A borrower that can use them will not pay much above that rate. That is a ceiling, softened by stigma and operational limits.

The settings in the implementation note of 16 September 2026, the most recent found when this chapter was written, were [FACT; ch05-S01, ch05-S02]:

| Instrument | Setting | Position in the range |
|---|---|---|
| Federal funds target range | 3.75%–4.00% (raised 25 bp) | — |
| IORB | 3.90%, effective 17 September 2026 | 15 bp above the bottom |
| ON RRP offering rate | 3.75%; per-counterparty limit \$160 billion per day | Bottom |
| SRF rate | 4.00% | Top |
| Primary credit rate | 4.00% | Top |

The 16 September 2026 decision raised the range by 25 bp after a hold at 3.50%–3.75% at the 28–29 July 2026 meeting [FACT; ch05-S02, ch05-S03]. Check the latest implementation note on federalreserve.gov before using these settings, because they change at every decision.

### 5.4.2 The Taylor rule and its variants

Taylor (1993) proposed a simple rule that described Federal Reserve behavior in the late 1980s and early 1990s [ch05-S13]:

$$i = r^* + \pi + a(\pi - \pi^*) + b\,y, \qquad a = b = 0.5,\ r^* = 2\%,\ \pi^* = 2\%,$$

where $i$ is the prescribed nominal policy rate, $\pi$ trailing inflation, and $y$ the output gap in percent of potential.

**Derivation of the intuition.** Write the real policy rate as $i - \pi$. The rule sets it equal to neutral, $r^*$, plus leaning against inflation and output deviations. Because the coefficient on $\pi$ in the nominal rate is $1 + a = 1.5 > 1$, a one-point rise in inflation raises the *real* policy rate by 0.5 points. This is the **Taylor principle**. A rule with a coefficient below one lets real rates fall as inflation rises, which feeds inflation.

**Variants** used in Federal Reserve communications [ch05-S14]:

| Rule | Prescription |
|---|---|
| Taylor (1993) | $r^* + \pi + 0.5(\pi - 2) + 0.5y$ |
| Balanced-approach | $r^* + \pi + 0.5(\pi - 2) + 1.0y$ (the gap coefficient is doubled) |
| Inertial | $i_t = \rho\, i_{t-1} + (1-\rho)\, i_t^{rule}$ with $\rho$ typically 0.8–0.9 [HYPOTHESIS for the range] |
| Unemployment form | replaces $y$ with $\approx 2(u^* - u)$ (Okun's-law conversion; the factor 2 is a convention [HYPOTHESIS]) |

**Limits.** Every input is uncertain:

* $r^*$ is unobservable. Different models give materially different estimates. A 1-point error in $r^*$ is a 1-point error in the prescription.
* The inflation measure matters: headline or core, CPI or PCE, trailing 12 months or forecast.
* The output gap is revised heavily after the fact. Real-time gaps differ from final ones.
* The rule ignores financial stability, the effective lower bound, balance-sheet policy, and the lag between policy and inflation.

The rule is a **benchmark for the reaction function**, not a forecast of the next decision. Its value to a speculator is to flag when the market's priced path diverges sharply from every reasonable rule. Then you ask why.

### 5.4.3 Fisher: nominal, real, and inflation compensation

The exact Fisher relation:

$$(1 + i) = (1 + r)(1 + \pi^e) \quad\Rightarrow\quad r = \frac{1+i}{1+\pi^e} - 1 \approx i - \pi^e.$$

The approximation error is about $r\,\pi^e$. It is small at low rates and grows when rates and inflation are both high. For TIPS, the market quotes a real yield $r_{TIPS}$ directly. The **breakeven** is

$$BEI = \frac{1 + y_{nom}}{1 + r_{TIPS}} - 1 \approx y_{nom} - r_{TIPS}.$$

Breakeven inflation is **compensation**, not a forecast:

$$BEI = E[\pi] + \text{inflation risk premium} - \text{TIPS liquidity premium}.$$

TIPS index to CPI-U, not to the PCE index in which the Fed's goal is stated. CPI inflation has tended to run above PCE inflation [HYPOTHESIS for any specific gap; the wedge varies over time]. In a flight to liquidity, nominal Treasuries can outperform TIPS for reasons unrelated to inflation, and breakevens fall.

**Survey measures** (University of Michigan, the New York Fed's Survey of Consumer Expectations, the Philadelphia Fed's Survey of Professional Forecasters) measure stated expectations directly. They have no risk premium, but they are subject to sampling noise, framing effects, and, for households, a tendency to track salient prices such as gasoline. When surveys and breakevens diverge, neither is automatically right. The divergence itself is information about which group is moving and why (Problem 5.10).

### 5.4.4 Fed funds futures and implied probabilities

Contract price $F = 100 - \bar R$, where $\bar R$ is the arithmetic average of daily EFFR over all calendar days in the contract month. Weekends and holidays carry the previous business day's rate.

Suppose a month has $N$ days, a decision takes effect on day $d+1$ (the day after the meeting's final day), the pre-meeting EFFR is $r_0$, and the post-meeting expected rate is $E[r_1]$. Then

$$\bar R = \frac{d\, r_0 + (N - d)\,E[r_1]}{N} \quad\Rightarrow\quad E[r_1] = \frac{N\bar R - d\, r_0}{N - d}.$$

If the only outcomes are "no change" and "change of size $\Delta$", then $E[r_1] = r_0 + p\Delta$, so

$$p = \frac{E[r_1] - r_0}{\Delta}.$$

**Day-weighting matters.** Only $(N-d)/N$ of the month is affected, so the naive formula $(\bar R - r_0)/\Delta$ understates $p$ by the factor $(N-d)/N$. When the meeting is late in the month, $(N-d)$ is small and the inference is noisy: one tick of price error is multiplied by $N/(N-d)$. Use the **next** month's contract, which lies entirely after the meeting, as the cross-check.

**Caveats.**

1. The futures price embeds a risk premium. Implied probabilities are risk-neutral, not physical.
2. The EFFR–IORB spread can drift for reasons unrelated to policy (reserve scarcity, quarter-end, Treasury settlement days). A 2 bp drift is 8% of a 25 bp move.
3. With three or more possible outcomes (hold, 25, 50), one price cannot identify the probabilities. You need another instrument (options, SOFR futures) or an assumption.

### 5.4.5 The yield curve as expected policy plus term premium

For zero-coupon yields with annual compounding, the one-year forward rate one year ahead is

$$f_{1,2} = \frac{(1+y_2)^2}{(1+y_1)} - 1.$$

Under the pure expectations hypothesis $f_{1,2}$ would equal the expected one-year rate a year from now. In practice

$$y_n \approx \frac{1}{n}\sum_{t=0}^{n-1} E_t[i_{t}] + TP_n,$$

where $TP_n$ is the term premium. The decomposition depends on the model used to estimate expected short rates. Published estimates from different models can differ by more than 50 bp at the same date [HYPOTHESIS: magnitude of model disagreement offered as an order of magnitude, not a sourced figure].

### 5.4.6 From the policy rate to a CRE loan

**Floating channel.** For an interest-only floating loan accruing on an actual/360 basis,

$$DS_{float} = L\,(SOFR + s)\,\frac{365}{360}, \qquad DSCR = \frac{NOI}{DS_{float}}.$$

A cap at strike $K_{cap}$ limits the SOFR component to $\min(SOFR, K_{cap})$. The SOFR at which DSCR hits a covenant level $D$ is

$$SOFR^{\dagger} = \frac{NOI}{D\, L\,(365/360)} - s.$$

**Fixed channel.** The coupon is set at closing as $c = y_{10} + s_{fixed}$. The loan constant with monthly amortization over $n$ months is

$$K = 12\cdot\frac{c/12}{1 - (1 + c/12)^{-n}},$$

and DSCR-constrained proceeds are $L_{DSCR} = NOI/(D\,K)$. The elasticity of DSCR proceeds to the coupon is $-\,(\partial K/\partial c)(c/K)$. For 30-year amortization it is −0.64 at a 6.00% coupon, −0.68 at 6.50%, and −0.71 at 7.00% [computed; Example 5.7]. A 10% proportional rise in the coupon (65 bp at 6.50%) cuts DSCR proceeds by roughly 6.8%. Actual loan proceeds are the minimum over LTV, DSCR, and debt-yield constraints, so a rate shock can leave proceeds unchanged if LTV binds. The shock then reaches proceeds later, through appraised value.

**Availability channel.** No equation fits it well. Track the Senior Loan Officer Opinion Survey (SLOOS) net percentage tightening CRE standards, bank CRE loan growth, CMBS issuance, and the number of lender quotes per deal.

### 5.4.7 QE and QT: balance-sheet mechanics

When the Fed buys \$100 of Treasuries from a dealer, the Fed's assets rise by \$100 (securities). Its liabilities rise by \$100 (reserves credited to the dealer's bank). The private sector holds \$100 less duration and \$100 more reserves. Under QT the Fed lets securities mature without reinvesting. The Treasury pays off the maturing bonds by drawing on its General Account (TGA), which it refills by issuing new debt to the public. Net effect: private holdings of Treasuries rise, and reserves or ON RRP balances fall.

The claimed effect on long yields operates through the **portfolio-balance** channel. Removing duration from private hands lowers the term premium, and returning it raises the term premium. Estimates of the size of the effect vary widely across studies and episodes. Announcement effects differ from flow effects, and they depend on the starting level of reserves. Treat any "bp per \$100 billion" figure as a model-dependent estimate with a wide range [HYPOTHESIS].

### 5.4.8 Transmission beyond CRE, and why the dollar and equities move together on policy news

A hawkish surprise (higher expected policy path) produces a recognizable cross-asset pattern. Each leg has a mechanism, and each mechanism can fail.

| Market | Typical direction on a hawkish surprise | Mechanism | When it fails |
|---|---|---|---|
| 2-year Treasury | Up most | Direct repricing of the next several meetings | Surprise read as raising recession odds within the 2-year horizon |
| 10-year Treasury | Up, usually less than the 2-year | Expected path beyond two years plus term premium | Credibility gain lowers long-run inflation expectations: the curve flattens or inverts |
| Equity index | Down | Higher discount rate; weaker growth expectations | Surprise driven by strong real growth: earnings effect dominates |
| U.S. dollar | Up | Higher expected U.S. rates relative to other countries attract capital (covered-interest parity links forward points to rate differentials; Chapter 15) | Other central banks surprise in the same direction |
| Credit spreads | Wider | Higher default probability and lower risk appetite | Spread moves dominated by supply or technical factors |
| Private CRE | No print the same day; later lower bids, lower proceeds, fewer trades | Debt cost, proceeds, required returns | Strong NOI growth offsets cap-rate pressure |

[INFERENCE: the directions are the standard mechanisms, not a sourced empirical regularity. Case H quantifies one such day with hypothetical moves.]

The pattern matters for portfolio construction. A book that is long duration, long equities, long foreign currency, long credit, and long levered CRE has one dominant risk factor on inflation-release days, however diversified it looks by asset class. Case H computes the P&L of such a book.

### 5.4.9 Inflation expectations: surveys versus markets

| Measure | Source | What it measures | Strength | Weakness |
|---|---|---|---|---|
| Household surveys | University of Michigan; New York Fed Survey of Consumer Expectations | Stated expectations of households | No risk premium; captures wage-setting psychology | Noisy; sensitive to gasoline and food prices; framing effects |
| Professional surveys | Philadelphia Fed Survey of Professional Forecasters | Forecasters' point and probability forecasts | Explicit horizons; probability bins | Herding; quarterly frequency |
| TIPS breakevens | Treasury market | Inflation compensation | Daily; tradable | Risk and liquidity premia; CPI not PCE |
| Inflation swaps | OTC market | Fixed-for-CPI swap rates | Clean term structure | Dealer balance-sheet effects; less transparent |
| 5-year, 5-year forward breakeven | Derived from 5- and 10-year breakevens | Long-run inflation compensation | Strips out near-term energy noise | Still contains premia |

The 5y5y forward breakeven uses the same forward arithmetic as Example 5.5: $(1+BEI_{10})^{10}/(1+BEI_5)^5$ raised to the power $1/5$, minus one. A central bank worried about de-anchoring watches whether long-horizon measures move with short-horizon ones. If a bad inflation print lifts one-year expectations but leaves 5y5y unchanged, expectations look anchored. If 5y5y also rises, the reaction function is likely to turn more hawkish [INFERENCE].

---

## 5.5 Worked examples

All inputs in the examples are hypothetical [HYPOTHESIS] unless tagged otherwise. Administered rates in Example 5.1 use the 16 September 2026 settings [FACT; ch05-S01].

### Example 5.1 — The corridor at work: IORB arbitrage and where SOFR can trade

**Given.** Target range 3.75%–4.00%, IORB 3.90%, ON RRP 3.75%, SRF 4.00% [FACT]. A Federal Home Loan Bank, which cannot earn IORB, lends \$1.0 billion overnight in fed funds to a bank at 3.86% [HYPOTHESIS]. Money-market convention: actual/360.

**Find.** (a) The bank's daily and annualized arbitrage profit if it holds the funds as reserves. (b) The band within which SOFR should trade, and why. (c) The base coupon on a floating CRE loan at SOFR + 3.00% if SOFR prints 3.88% [HYPOTHESIS].

**Solution.**

(a) Daily profit $= \$1{,}000{,}000{,}000 \times (0.0390 - 0.0386)/360 = \$1{,}111.11$. Annualized over 365 days: $1{,}111.11 \times 365 = \$405{,}556$, a 4 bp spread on \$1 billion.

(b) Lower bound: money funds can earn 3.75% at the ON RRP, so they will not lend repo much below 3.75%. Upper bound: dealers can borrow at the SRF at 4.00%, so repo should not trade persistently above 4.00% unless stigma or operational limits bind. SOFR should trade between 3.75% and 4.00%, and in an ample-reserves regime it should trade close to IORB. Persistent prints of SOFR above IORB are a sign that reserves are becoming less than ample.

(c) Coupon $= 3.88\% + 3.00\% = 6.88\%$.

**Check.** The profit is positive only because the lender lacks IORB access. If both counterparties could earn IORB, the rate would converge to IORB and the arbitrage would vanish. That is why EFFR has tended to trade slightly *below* IORB in the ample-reserves regime [INFERENCE from the mechanism].

**Decision consequence.** A floating CRE borrower's base rate is effectively an administered rate plus a few basis points. When the FOMC moves the range, IORB, ON RRP, and SRF move with it. SOFR follows within a day, and every floating loan's coupon follows at its next reset. There is no lag on the floating channel. The lag is in NOI, appraisals, and lender behavior. Underwrite floating debt service from the futures- or swap-implied path, not from today's print.

**Reproduce:** `tests/test_ch05_examples.py::test_example_5_1`

### Example 5.2 — Taylor-rule prescriptions and the width of the band

**Given.** Trailing core PCE inflation $\pi = 3.0\%$; output gap $y = -0.5\%$; inflation target 2%. Two neutral-rate estimates: Taylor's original $r^* = 2.00\%$ and a lower estimate $r^* = 0.75\%$. Policy range midpoint 3.875%. Inertial smoothing $\rho = 0.85$.

**Find.** Prescriptions under Taylor (1993) and balanced-approach rules for each $r^*$. Find the inertial next-step rate when the rule prescribes 4.00% and when it prescribes 5.25%.

**Solution.**

Taylor (1993), $r^* = 2.00\%$: $i = 2.00 + 3.00 + 0.5(3.00 - 2.00) + 0.5(-0.5) = 2.00 + 3.00 + 0.50 - 0.25 = 5.25\%$.

Taylor (1993), $r^* = 0.75\%$: $i = 0.75 + 3.00 + 0.50 - 0.25 = 4.00\%$.

Balanced-approach, $r^* = 2.00\%$: $i = 2.00 + 3.00 + 0.50 + 1.0(-0.5) = 5.00\%$.

Balanced-approach, $r^* = 0.75\%$: $i = 3.75\%$.

Inertial: $i_t = 0.85 \times 3.875 + 0.15 \times 4.00 = 3.89375\%$. With a rule prescription of 5.25%: $0.85 \times 3.875 + 0.15 \times 5.25 = 4.08125\%$.

| | $r^* = 0.75\%$ | $r^* = 2.00\%$ |
|---|---|---|
| Taylor (1993) | 4.00% | 5.25% |
| Balanced-approach | 3.75% | 5.00% |

**Check.** The difference between columns is exactly the 1.25-point difference in $r^*$, because $r^*$ enters one-for-one. The difference between rows is $0.5 \times |y| = 0.25$ point.

**Decision consequence.** Four defensible rules span 3.75%–5.25%, a 150 bp band, for the same data. The current range midpoint of 3.875% sits at the low end. A rule can tell you that policy is "restrictive relative to a low $r^*$" or "accommodative relative to Taylor's original $r^*$". It cannot tell you the next decision. For a CRE underwriter, the practical use is a stress range: a floating-rate deal that fails at a policy rate near the top of the rule band (here 5.25%) has a meaningful tail. The inertial row shows why actual policy moves in steps. Even a rule that prescribes 5.25% moves the rate only about 21 bp per step at $\rho = 0.85$.

**Reproduce:** `tests/test_ch05_examples.py::test_example_5_2`

### Example 5.3 — Real yields, breakevens, and the real return on a cap rate

**Given.** 10-year nominal Treasury yield 4.30%; 10-year TIPS real yield 1.90%. An apartment building trades at a 6.00% cap on NOI after reserves. Assume NOI grows with inflation at the breakeven rate, with zero real growth, in perpetuity.

**Find.** (a) The breakeven, approximate and exact. (b) The implied nominal and real unlevered required return under the Gordon model. (c) The real risk premium over TIPS.

**Solution.**

(a) Approximate: $4.30\% - 1.90\% = 2.40\%$. Exact: $1.043/1.019 - 1 = 2.3553\%$. The 4.5 bp gap is the cross-term $r \cdot \pi$.

(b) Using the approximate breakeven as expected nominal NOI growth $g = 2.40\%$: $k = c + g = 6.00\% + 2.40\% = 8.40\%$ nominal. Real: $1.084/1.024 - 1 = 5.8594\%$.

(c) Real risk premium $= 5.8594\% - 1.90\% = 3.9594\%$, about 396 bp over TIPS.

**Check.** $(1.019)(1.039594)(1.024) = 1.0848 \approx 1.084$. The small residual arises because the premium is computed by subtraction, not by compounding.

**Decision consequence.** The comparison an investor should make is real to real: a 6.00% cap with inflation-linked NOI against a 1.90% TIPS yield, not against a 4.30% nominal yield. If NOI cannot keep pace with inflation (long fixed leases, capped renewals, or rising insurance and taxes), real growth is negative and the premium shrinks one-for-one. A 1-point shortfall of NOI growth against inflation takes the premium from about 3.96% to about 2.98%. Breakevens include risk and liquidity premia, so using them as the growth assumption is itself a [HYPOTHESIS] to be stated.

**Reproduce:** `tests/test_ch05_examples.py::test_example_5_3`

### Example 5.4 — The implied probability of a hike, with day-weighting

**Given.** A 30-day month. The FOMC decision takes effect on day 17, so 16 days are at the pre-meeting rate. Pre-meeting EFFR $r_0 = 3.88\%$. The only alternatives are no change and a 25 bp hike. The meeting-month contract trades at 96.040. The next month's contract, which lies entirely after the meeting and has no meeting of its own, trades at 95.950. Assume EFFR stays at a fixed spread to IORB.

**Find.** (a) The expected post-meeting EFFR and the implied hike probability. (b) The naive (non-day-weighted) probability. (c) The cross-check from the next month's contract. (d) The P&L of 100 short meeting-month contracts at 96.040 in each outcome, and the expected P&L at the implied probability.

**Solution.**

(a) $\bar R = 100 - 96.040 = 3.960\%$.
$$E[r_1] = \frac{30(3.960) - 16(3.88)}{14} = \frac{118.80 - 62.08}{14} = \frac{56.72}{14} = 4.05143\%.$$
$p = (4.05143 - 3.88)/0.25 = 0.17143/0.25 = 68.57\%$.

(b) Naive: $(3.960 - 3.88)/0.25 = 32.0\%$. That understates $p$ by the factor $14/30$.

(c) Next month: $\bar R = 100 - 95.950 = 4.050\%$, so $p = (4.050 - 3.88)/0.25 = 68.0\%$. The two estimates agree within 0.6 percentage points. Tick rounding and EFFR–IORB drift explain differences of this size.

(d) If the Fed hikes, the month averages $(16 \times 3.88 + 14 \times 4.13)/30 = 3.99667\%$, so the contract settles at 96.00333. A short from 96.040 gains $3.667$ bp × \$41.67 × 100 = **\$15,279**. If the Fed holds, the settlement is $100 - 3.88 = 96.120$, and the short loses $8.0$ bp × \$41.67 × 100 = **−\$33,336**. Expected P&L at $p = 0.6857$: $0.6857(15{,}279) + 0.3143(-33{,}336) \approx \$0$.

**Check.** The expected P&L is zero at the market-implied probability, as it must be, because that probability was backed out of the price. Any profit from the trade requires a probability view that differs from 68.6% and is *correct*.

**Decision consequence.** A desk that read the meeting-month contract naively would believe a hike was a one-in-three chance when the market priced better than two-in-three. For the opening problem, the hike is mostly priced. If it arrives, forward SOFR moves little. If the Fed holds, front-end rates fall. A floating-rate borrower's real exposure is the path *after* this meeting, which the next several contracts and SOFR futures price. To bet on the meeting you need information the market lacks. Absent that, abstain (Drill D101).

**Reproduce:** `tests/test_ch05_examples.py::test_example_5_4`

### Example 5.5 — Reading the curve: the forward rate and what it implies for a floating borrower

**Given.** One-year zero yield 3.80%; two-year zero yield 3.60% (annual compounding). Assume a term premium on the one-year-forward rate of 0.10%.

**Find.** The one-year rate one year forward, the implied expected one-year rate, and the cuts the curve implies relative to today's 3.80%.

**Solution.**
$$f_{1,2} = \frac{(1.036)^2}{1.038} - 1 = \frac{1.073296}{1.038} - 1 = 3.4004\%.$$
Expected one-year rate in a year $= 3.4004\% - 0.10\% = 3.3004\%$, which is about 50 bp below today's one-year yield.

**Check.** Rolling 3.80% for a year and then 3.4004% gives $(1.038)(1.034004) = 1.073296 = (1.036)^2$. ✓

**Decision consequence.** An inverted front end prices easing. A floating-rate borrower who underwrites today's SOFR for two years overstates expected interest by roughly the average of the implied cuts. A borrower who underwrites the implied cuts as certain understates the tail. The curve is a risk-neutral, term-premium-contaminated mean. Size the cap and the DSCR covenant to a path *above* the forward curve, because the scenario in which cuts do not arrive is often the one in which NOI is also under pressure from inflation-driven expenses.

**Reproduce:** `tests/test_ch05_examples.py::test_example_5_5`

### Example 5.6 — Policy rate → SOFR → floating coupon → DSCR

**Given.** The opening problem's hotel: NOI \$2,400,000; floating loan \$30,000,000 interest-only at SOFR + 3.00%, actual/360. Two SOFR levels: 0.05% (near the start of the 2022 hiking cycle) and 5.30% (near the 2023 peak). These levels are rounded approximations of observed SOFR [VERIFIED-SECONDARY for the range: SOFR's first 2022 value was 0.05% and its 2023 high was 5.40%; ch05-S18]. Rate cap at 3.00% SOFR.

**Find.** Annual interest and DSCR at each SOFR level, unhedged and capped. Find the SOFR at which DSCR = 1.00x. Show the error from ignoring actual/360.

**Solution.**

| | SOFR 0.05% | SOFR 5.30% unhedged | SOFR 5.30% capped at 3.00% |
|---|---|---|---|
| All-in coupon | 3.05% | 8.30% | 6.00% (effective) |
| Interest $= L \cdot c \cdot 365/360$ | \$927,708 | \$2,524,583 | \$1,825,000 |
| DSCR $= 2{,}400{,}000/DS$ | 2.59x | 0.95x | 1.32x |

Break-even SOFR for DSCR = 1.00x: $2{,}400{,}000/(30{,}000{,}000 \times 365/360) - 0.03 = 4.8904\%$.

Day-count error at SOFR 5.30%: a 30/360 calculation gives \$2,490,000, understating interest by \$34,583 per year.

**Check.** \$2,524,583 / \$2,490,000 = 1.01389 = 365/360. ✓

**Decision consequence.** A 525 bp rise in SOFR took the hotel from 2.59x to below 1.0x unhedged. The cap is what kept it solvent, at 1.32x. The cap also expires. At extension, the lender requires a new cap priced at then-current forward rates and volatility, which can be a large cash outlay exactly when cash flow is weakest (Chapter 18). The floating channel is fast and mechanical. Every basis point reaches debt service at the next reset. Underwrite with the cap strike, the cap's expiry, and the replacement cost in the model, not just today's coupon.

**Reproduce:** `tests/test_ch05_examples.py::test_example_5_6`

### Example 5.7 — 10-year Treasury → fixed coupon → loan constant → proceeds

**Given.** The same hotel's NOI (\$2,400,000) is refinanced fixed-rate on a 30-year amortization with constraints of 65% LTV, 1.25x DSCR, and 8.0% debt yield. Two environments [HYPOTHESIS, stylized on 2021 and 2023 levels]:

| | Low-rate | High-rate |
|---|---|---|
| 10-year Treasury | 1.50% | 4.50% |
| Lender spread | 1.75% | 2.00% |
| Coupon | 3.25% | 6.50% |
| Appraisal cap rate | 5.00% | 6.00% |

The existing loan balance at maturity is \$30,000,000 (interest-only). Refinancing costs are 1% of the existing balance.

**Find.** Loan constants, each constraint, the binding constraint, proceeds, and the refinance gap in the high-rate environment.

**Solution.**

Loan constants: $K(3.25\%) = 0.052225$; $K(6.50\%) = 0.075848$.

| Constraint | Low-rate | High-rate |
|---|---|---|
| Value $= NOI/c$ | \$48,000,000 | \$40,000,000 |
| LTV 65% | \$31,200,000 | \$26,000,000 |
| DSCR: $NOI/(1.25 K)$ | \$36,764,172 | \$25,313,731 |
| Debt yield: $NOI/0.08$ | \$30,000,000 | \$30,000,000 |
| **Maximum loan** | **\$30,000,000 (debt yield)** | **\$25,313,731 (DSCR)** |

DSCR capacity alone falls by $1 - 25{,}313{,}731/36{,}764{,}172 = 31.1\%$. Actual proceeds fall by 15.6%, because the binding constraint shifts from debt yield to DSCR.

Refinance gap $= 30{,}000{,}000 + 300{,}000 - 25{,}313{,}731 = \$4{,}986{,}269$.

The loan constant rises 45.2% ($0.075848/0.052225 - 1$). At the 6.50% coupon the elasticity of $K$ to the coupon is 0.676, so a further 10% proportional rise in the coupon would cut DSCR proceeds by about 6.8%.

**Check.** At the high-rate maximum loan, $DS = 25{,}313{,}731 \times 0.075848 = \$1{,}920{,}000$ and $DSCR = 2{,}400{,}000/1{,}920{,}000 = 1.25$x. ✓

**Decision consequence.** NOI never changed, yet the owner must bring about \$5.0 million of new equity, roughly 17% of the original loan, or sell, or negotiate an extension. That is the 2022–23 refinancing problem in a single line. Notice which constraint binds. When LTV or debt yield binds, a rate shock does not reduce proceeds immediately. It reduces them later through the appraisal. A model that sizes only on DSCR overstates the immediate effect. A model that sizes only on LTV at a stale appraisal understates the eventual effect.

**Reproduce:** `tests/test_ch05_examples.py::test_example_5_7`

### Example 5.8 — QT, the term premium, and a cap rate

**Given.** 10-year Treasury yield 4.30%. A model estimate of the average expected short rate over ten years is 3.40% [HYPOTHESIS]. Suppose balance-sheet runoff and heavy issuance raise the term premium by 20 bp with expected short rates unchanged [HYPOTHESIS]. Hold a 10-year Treasury bought at par with a 4.30% coupon, \$100 face. An apartment cap rate of 6.00% moves by a pass-through fraction $\beta = 0.5$ of the 10-year move [HYPOTHESIS; Chapter 6 estimates and criticizes this parameter].

**Find.** (a) The implied term premium before and after. (b) DV01 per \$100 face and the price change. (c) The cap rate and the percentage value change for the apartment.

**Solution.**

(a) $TP = 4.30\% - 3.40\% = 0.90\%$ before and 1.10% after. The 10-year rises to 4.50%.

(b) DV01 (central difference) $= 0.08059$ per \$100 face. Duration estimate: $-0.08059 \times 20 = -1.612$. Full reprice at 4.50%: $-1.596$. Convexity makes up the 0.016 difference.

(c) Cap rate $= 6.00\% + 0.5 \times 0.20\% = 6.10\%$. Value change $= 6.00/6.10 - 1 = -1.64\%$.

**Check.** The duration estimate overstates the loss because of positive convexity, as expected. The cap-rate move of 10 bp on 6.00% is 1.67% to first order, and the exact figure is 1.64%.

**Decision consequence.** A term-premium shock reaches a bond immediately and a property only partly and slowly. Whether $\beta$ is 0.3 or 1.0 is the whole question, and the answer differs by property type, period, and financing conditions (Chapter 6). Do not attribute a yield move to QT without a decomposition. A term-premium rise and a rise in expected policy have different implications for floating-rate borrowers. The first leaves SOFR forwards unchanged. The second raises them.

**Reproduce:** `tests/test_ch05_examples.py::test_example_5_8`

---

## 5.6 CRE application: one policy shock, three channels, three clocks

Combine Examples 5.4–5.7 into a single map for a CRE book.

| Channel | Transmission | Clock | What to monitor | What to model |
|---|---|---|---|---|
| Floating debt | Policy → IORB/ON RRP/SRF → SOFR → coupon | Next reset (days to a month) | Fed funds and SOFR futures, cap strikes and expiries | DSCR path under forward curve + stress; cap replacement cost |
| Fixed debt | Policy expectations + term premium → 10-year → coupon → loan constant | At each rate lock (weeks to months) | 10-year, swap spreads, lender spreads | Proceeds under each constraint; refinance gap by maturity |
| Valuation | Real yields + risk premia → cap rates | Quarters to years; appraisals lag | Transaction cap rates, REIT-implied cap rates, bid-ask gap | Value under cap-rate scenarios; equity at risk |
| Availability | Policy → bank capital, deposits, funding → lending standards | Quarters | SLOOS, bank CRE loan growth, CMBS issuance, quotes per deal | Probability of no refinancing; extension economics |

Three practical rules follow.

1. **Map each loan to the curve point that sets its coupon.** Floating loans are front-end exposures. Fixed refinancings are 10-year exposures *at the lock date*. A borrower with both has a curve position, whether or not it chose one.
2. **Separate the rate shock from the availability shock.** A rate rise with open lending markets produces a refinance gap that equity can fill. A rate rise with closed lending markets produces forced sales. The second is where distressed opportunity appears (Chapter 12), and it is driven by bank balance sheets, not by the rate level alone.
3. **Expect private values to lag.** Liquid markets reprice the day of the news. Appraisals reprice over several quarters, and transaction volume falls while buyers and sellers disagree (Chapter 2, Case H). The lag is not evidence that CRE was insulated. It is evidence that CRE is priced infrequently.

---

## 5.7 When the relationships fail

1. **The policy rate rises and long yields fall.** If markets read the hike as raising recession odds, the 10-year can fall, and fixed-rate refinancing becomes cheaper while floating becomes dearer. The intuition "rates up, cap rates up" breaks down when the curve twists.
2. **Breakevens fall during a liquidity crisis.** TIPS are less liquid than nominals. In a scramble for cash, breakevens can collapse without any change in inflation expectations.
3. **Fed funds futures mislead around quarter-ends and regime changes.** EFFR–IORB spreads move when reserves approach scarcity. That shifts $\bar R$ without any policy change.
4. **Cap rates do not follow Treasuries.** In 2022, 10-year yields rose sharply while appraisal-based cap rates moved little for several quarters (§5.9). Spreads compress and widen with risk appetite, NOI growth expectations, and capital flows.
5. **The Taylor rule is silent on financial stability.** In March 2023 the FOMC raised rates while the Fed simultaneously opened an emergency lending facility (§5.9). No simple rule describes that combination.
6. **QT effects are not stable.** The same runoff pace can have small effects when reserves are abundant and large effects in money markets when reserves near scarcity. That is why runoff was slowed and then ended (§5.9).
7. **Availability can tighten without a rate move.** Bank failures, regulatory changes, or concentration limits can close lending to a property type even when the policy rate is unchanged.

---

## 5.8 Liquidity facilities: discount window, SRF, and the 2023 BTFP

| Facility | Borrower | Collateral and valuation | Rate | Term | Status |
|---|---|---|---|---|---|
| Primary credit (discount window) | Sound depository institutions | Broad collateral at lendable values (haircuts) | Primary credit rate, top of the range (4.00% at 16 Sep 2026) [FACT; ch05-S01] | Overnight to longer | Standing |
| Standing repo facility | Primary dealers, eligible banks | Treasuries, agency debt, agency MBS | SRF rate, top of the range (4.00% at 16 Sep 2026) [FACT; ch05-S01] | Overnight | Standing since 29 July 2021 [FACT; ch05-S09] |
| Bank Term Funding Program (BTFP) | Federally insured depository institutions and other eligible institutions | Treasuries, agency debt, agency MBS, and other qualifying assets **valued at par** | One-year OIS + 10 bp, fixed at advance [VERIFIED-SECONDARY; ch05-S08]; from 24 January 2024, not below IORB [FACT; ch05-S07] | Up to one year | Announced 12 March 2023; new loans ceased 11 March 2024 [FACT; ch05-S07, ch05-S08] |

**Why par valuation mattered.** A bank holding a Treasury bought at 100 that now trades at 85 could borrow 100 against it at the BTFP. At the discount window it could borrow only 85 minus a haircut. Par valuation removed the need to sell securities at a loss to meet deposit withdrawals. It addressed the specific vulnerability of 2023: unrealized losses created by the rate increases themselves [INFERENCE from the program design].

**CRE relevance.** Liquidity facilities stabilize banks' *funding*. They do not restore banks' *willingness to lend*. After March 2023, banks that had relied on emergency funding had strong reasons to shrink balance sheets and to raise CRE lending standards [INFERENCE; consistent with the SLOOS evidence in §5.9].

---

## 5.9 Historical episode: the 2022–23 tightening cycle and its CRE transmission

### Date and environment

At the start of 2022 the federal funds target range was 0%–0.25%, and the Fed was still buying securities. SOFR's first published value of 2022 was 0.05% [VERIFIED-SECONDARY; ch05-S18]. Inflation was rising. The CPI-U for the 12 months to June 2022, released on 13 July 2022, rose 9.1%, the largest 12-month increase since the period ending November 1981 [FACT; BLS, ch05-S10]. In the same release, core CPI (excluding food and energy) rose 5.9% over 12 months [FACT; ch05-S10].

### The policy path

| FOMC decision | Target range after decision | Move |
|---|---|---|
| 16 Mar 2022 | 0.25%–0.50% | +25 bp |
| 4 May 2022 | 0.75%–1.00% | +50 bp |
| 15 Jun 2022 | 1.50%–1.75% | +75 bp |
| 27 Jul 2022 | 2.25%–2.50% | +75 bp |
| 21 Sep 2022 | 3.00%–3.25% | +75 bp |
| 2 Nov 2022 | 3.75%–4.00% | +75 bp |
| 14 Dec 2022 | 4.25%–4.50% | +50 bp |
| 1 Feb 2023 | 4.50%–4.75% | +25 bp |
| 22 Mar 2023 | 4.75%–5.00% | +25 bp |
| 3 May 2023 | 5.00%–5.25% | +25 bp |
| 26 Jul 2023 | 5.25%–5.50% | +25 bp |

[FACT; FOMC statements, ch05-S04.] The cumulative increase was 525 bp in 16 months. The June 2022 move was the first 75 bp increase since 1994 [VERIFIED-SECONDARY; ch05-S04]. The range stayed at 5.25%–5.50% until 18 September 2024, when the FOMC cut it by 50 bp to 4.75%–5.00% [FACT; ch05-S12].

**Balance sheet.** On 4 May 2022 the FOMC announced runoff beginning 1 June 2022. The monthly caps were \$30 billion for Treasuries and \$17.5 billion for agency debt and MBS, rising after three months to \$60 billion and \$35 billion [FACT; ch05-S05]. From June 2024 the Treasury cap was reduced to \$25 billion [VERIFIED-SECONDARY; ch05-S06]. On 29 October 2025 the FOMC announced that runoff of its securities holdings would end on 1 December 2025 [VERIFIED-SECONDARY; ch05-S06].

**Long yields.** The 10-year Treasury yield briefly crossed 5% intraday on 19 October 2023, the first time since 2007, and settled at 4.98% that day [VERIFIED-SECONDARY, citing Treasury data; ch05-S17]. At the end of 2021 the 10-year had been near 1.5% [VERIFIED-SECONDARY for the approximate level; ch05-S17; exact year-end close *(verification pending)*].

### The banking shock

Silicon Valley Bank failed on 10 March 2023. On 12 March 2023 the Fed announced the BTFP (§5.8) [FACT; ch05-S08]. Ten days later, on 22 March 2023, the FOMC raised rates by 25 bp. Its statement said the U.S. banking system was "sound and resilient" and that recent developments were "likely to result in tighter credit conditions for households and businesses" [FACT; ch05-S04].

### CRE transmission: what the record shows

* **Lending standards.** In each of the Fed's Senior Loan Officer Opinion Surveys covering Q4 2022 through Q3 2023, major net shares of banks reported tightening standards for all categories of CRE loans, and weaker demand [FACT; ch05-S15].
* **Floating-rate borrowers.** SOFR's 2023 high was 5.40% [VERIFIED-SECONDARY; ch05-S18]. A floating loan at SOFR + 3.00% therefore moved from a coupon near 3.05% to one above 8.3%. Example 5.6 shows what that does to a hotel at constant NOI.
* **Fixed-rate refinancing.** Loans sized in 2021 at low coupons met 2023 loan constants roughly 45% higher (Example 5.7: 0.0522 to 0.0758) [INFERENCE from the arithmetic, using stylized inputs].
* **Prices.** Press coverage of Green Street's Commercial Property Price Index reported an all-property decline from its March 2022 peak on the order of 20% by 2023, with office and apartments falling more [VERIFIED-SECONDARY for the direction and peak month; exact magnitude and date *(verification pending)*; ch05-S16].

### What was knowable at the time

| Date | Public information | What it implied for CRE |
|---|---|---|
| Early 2022 | Inflation high and rising; futures priced hikes; the FOMC signaled "ongoing increases" | Floating-rate cost would rise; caps were the immediate defense |
| Mid-2022 | 9.1% CPI print; 75 bp hikes; runoff announced | Fixed refinancings at maturity would face much higher constants |
| March 2023 | Bank failures; BTFP; FOMC expected tighter credit | Availability, not just price, would tighten |
| Late 2023 | 10-year near 5% | Refinance gaps at their widest for loans sized in 2020–21 |

What was **not** knowable: the size of the eventual peak (the market repeatedly underpriced the path in 2022), whether the bank stress would spread, and how long rates would stay high.

### Interpretations

1. **Rate-driven repricing [INFERENCE].** CRE values fell because the discount rate and debt cost rose. Values recover when rates fall.
2. **Sector-driven repricing [INFERENCE].** Office faced a structural demand shock from remote work that coincided with higher rates. Rates revealed weakness rather than causing all of it.
3. **Availability-driven repricing [INFERENCE].** The tightening of bank lending after March 2023 cut the pool of buyers who could close, which depressed transaction prices beyond what rates alone imply.

The three are not exclusive. The data available here cannot apportion the decline among them.

### What the episode establishes, and what it does not

It **establishes** that the floating channel transmits immediately and mechanically, that the fixed channel transmits at each maturity, and that availability can tighten sharply through the banking system. It does **not** establish a stable cap-rate beta to Treasuries, or that CRE prices fall by any particular amount for a given rate rise. Nor does it establish that the Fed will always pair hiking with liquidity support. The Volcker tightening of 1979–82 is a useful contrast: policy then targeted reserves rather than an interest rate, and short rates were far more volatile. Chapter 23 treats that episode with its own sources.

---

## 5.10 Decision exercise: the opening refinance

Return to §5.1. Use the futures inputs of Example 5.4, the loan terms of Examples 5.6 and 5.7, and today's 10-year at 4.50% after the 15 bp rise. Complete a decision record covering:

1. The market-implied probability of a hike and what it means for 18-month SOFR expectations.
2. Debt service and DSCR on (a) the floating extension at SOFR + 3.50% under the forward path and under a stress path 100 bp above it, and (b) the fixed refinance at today's 10-year. Show the binding constraint.
3. The refinance gap under the fixed option. State whether the owner can fund it and from what.
4. The cost and structure of the new cap for the extension, as a qualitative estimate if you do not have a cap quote. Name the inputs you need.
5. A recommendation: lock fixed now, extend floating, sell, or wait. Include what would change it.

**Rubric.**

| Criterion | Weight | Full credit |
|---|---|---|
| Probability correctly day-weighted and cross-checked | 15% | 68–69%, with the naive 32% identified as wrong |
| Floating DSCR under forward and stress paths | 20% | Uses actual/360, includes the cap, notes cap expiry and replacement |
| Fixed proceeds and binding constraint | 20% | Computes all three constraints; identifies the shift in the binding constraint |
| Refinance gap and funding source | 15% | Quantifies the gap; does not assume equity is free |
| Separates priced from unpriced information | 15% | States that a hike at a 68% implied probability is mostly priced; identifies the surprise scenario |
| Recommendation with invalidation criteria | 15% | Conditional on lender quotes and cap cost; names data that would reverse it |

There is no single correct answer. A recommendation to extend floating with a cap and pursue a sale is defensible if the cap is affordable. Locking fixed is defensible if the refinance gap can be funded and the owner wants certainty. Waiting for the meeting is defensible only if the option to lock survives the meeting.

---

## 5.11 Frequent analytical errors

1. **Reading fed funds futures without day-weighting.** It understates probabilities when the meeting is mid-month or late in the month.
2. **Treating implied probabilities as forecasts.** They are risk-neutral and include premia.
3. **Treating breakevens as expected inflation.** They include risk and liquidity premia and index to CPI, not PCE.
4. **Using the approximate Fisher relation at high rates.** The cross-term matters when nominal rates and inflation are both several percent.
5. **Ignoring actual/360 on floating loans.** It understates interest by 1.4%.
6. **Sizing proceeds on one constraint.** The binding constraint changes with rates and values.
7. **Assuming a stable cap-rate beta to the 10-year.** The pass-through varies by period and property type, and it lags.
8. **Equating a hike with higher long rates.** The curve can flatten or invert. Know which point sets your coupon.
9. **Confusing liquidity support with credit support.** The BTFP funded banks. It did not make them lend.
10. **Attributing every long-yield move to QT.** Decompose expected path versus term premium, and state the model.
11. **Using the Taylor rule as a point forecast.** Its band is wide because $r^*$ and the gap are uncertain.

---

## 5.12 Connections to other chapters

* Chapter 2: appraisal smoothing and why private prices lag liquid markets.
* Chapter 4: the data releases that move policy expectations, and surprise indices.
* Chapter 6: bond pricing, duration, DV01, and the cap-rate/Treasury spread in depth.
* Chapter 10: loan sizing, amortization, and refinancing gaps.
* Chapter 12: maturity walls and distressed CRE when availability closes.
* Chapter 14: equity index futures and their multipliers.
* Chapter 15: FX conventions and why the dollar rallies on hawkish surprises.
* Chapter 18: interest-rate caps for floating CRE debt and their replacement cost.
* Chapter 23: the Volcker disinflation and the 2022 episode in historical context.
* Case H: a single inflation surprise propagated through Treasuries, equity futures, FX, credit, and two CRE loans.

---

## 5.13 One-page reference sheet

**Administered rates at 16 Sep 2026** [FACT; ch05-S01]: range 3.75–4.00%; IORB 3.90%; ON RRP 3.75%; SRF 4.00%; primary credit 4.00%. Verify the current note before use.

| Item | Formula |
|---|---|
| Taylor (1993) | $i = r^* + \pi + 0.5(\pi - 2) + 0.5y$ |
| Balanced-approach | $i = r^* + \pi + 0.5(\pi - 2) + 1.0y$ |
| Inertial | $i_t = \rho i_{t-1} + (1-\rho) i^{rule}$ |
| Exact Fisher | $r = (1+i)/(1+\pi^e) - 1$ |
| Breakeven | $BEI = (1+y_{nom})/(1+r_{TIPS}) - 1$ |
| Fed funds futures | $F = 100 - \bar R$; \$41.67 per bp per contract |
| Post-meeting rate | $E[r_1] = (N\bar R - d\,r_0)/(N-d)$ |
| Hike probability | $p = (E[r_1] - r_0)/\Delta$ |
| Forward rate | $f_{1,2} = (1+y_2)^2/(1+y_1) - 1$ |
| Yield decomposition | $y_n \approx \text{avg } E[i] + TP_n$ |
| Floating debt service | $L(SOFR + s)(365/360)$ |
| Break-even SOFR at DSCR $D$ | $NOI/(D\,L\,365/360) - s$ |
| Loan constant | $K = 12 \cdot (c/12)/(1-(1+c/12)^{-n})$ |
| DSCR proceeds | $NOI/(D\,K)$ |
| Refinance gap | balance + costs − new loan |

**Checks before any rate-sensitive CRE decision.** Which curve point sets each coupon? What does the futures curve already price? Which loan constraint binds now, and which will bind after the next appraisal? Are lenders quoting at all?

---

## References for this chapter

All sources are listed with verification status in `references/sources_ch05.md` (for merger into `SOURCE_REGISTER.md`).

* Board of Governors of the Federal Reserve System. Implementation Note and FOMC statement, 16 September 2026; FOMC statement, 29 July 2026.
* Board of Governors of the Federal Reserve System. FOMC statements, 16 March 2022 through 26 July 2023; 18 September 2024.
* Board of Governors of the Federal Reserve System. "Plans for Reducing the Size of the Federal Reserve's Balance Sheet," 4 May 2022.
* Board of Governors of the Federal Reserve System. Press releases on the Bank Term Funding Program, 12 March 2023 and 24 January 2024.
* Board of Governors of the Federal Reserve System. "Policy Rules and How Policymakers Use Them."
* Board of Governors of the Federal Reserve System. Senior Loan Officer Opinion Surveys, January, April, July, and November 2023.
* Federal Open Market Committee. Statement on Longer-Run Goals and Monetary Policy Strategy (first adopted January 2012).
* Federal Open Market Committee. Statement regarding repurchase agreement arrangements, 28 July 2021.
* U.S. Bureau of Labor Statistics. Consumer Price Index — June 2022, released 13 July 2022.
* CME Group. 30-Day Federal Funds futures contract specifications; CBOT Rulebook Chapter 22.
* Taylor, J. B. (1993). "Discretion versus Policy Rules in Practice." *Carnegie-Rochester Conference Series on Public Policy* 39: 195–214.
* Federal Reserve Bank of St. Louis. "The FOMC Voting Rotation, Explained" (2022).
