# Chapter 7 Solutions

Numerical results are verified in `tests/test_ch07_examples.py`. Figures are rounded for display only. All inputs are hypothetical [HYPOTHESIS] unless cited.

---

### Solution 7.1
(a) $pb^* = d(r-g)/(1+g)$.
* Country A: $1.30 \times (0.025 - 0.040)/1.040 = -1.875\%$. A can run a primary **deficit** of about 1.9% of GDP and still stabilize debt.
* Country B: $0.60 \times (0.070 - 0.030)/1.030 = +2.330\%$. B needs a primary **surplus** of about 2.3% of GDP.

B, with less than half A's debt, needs the larger surplus. The debt level scales the requirement; the sign of $r - g$ sets its direction.

(b) Three of the following:
1. $r - g < 0$ holds only while it holds. Debt at 130% of GDP is highly sensitive to a reversal: each point of $r-g$ then adds about 1.25 points of GDP to the debt ratio per year.
2. $r$ is endogenous: higher debt can raise $r$ through risk and term premia (§7.4.3), which is how the favorable condition ends.
3. With a constant primary deficit, the debt ratio converges to $-pb(1+g)/(g-r)$, which can be several hundred percent of GDP, and fragility rises with the level (rollover needs, exposure to market access).
4. The relevant $r$ is the effective rate, which lags the market rate. A government can face $r_{eff} < g$ today while marginal issuance is at a rate above $g$.
5. Blanchard (2019) himself frames the argument as being about costs that may be lower than assumed, not about debt being free [FACT about the paper's framing; ch07-S23].

(c) With a 2-year WAM, about half the stock reprices each year, so a rise in market yields reaches the effective rate within one to two years. With a 7-year WAM, only about one-seventh reprices each year. The short-maturity government also has larger gross financing needs every year, so it is more exposed to a buyers' strike (rollover risk). Long maturity buys time; it does not eliminate the eventual adjustment.

### Solution 7.2
| Regime | Corner given up | Transmission of a global rate rise to local property |
|---|---|---|
| (a) Hard peg, open capital account | Monetary independence | Local interest rates must rise with the anchor's (plus any risk premium) to hold the peg. Cap rates and borrowing costs rise even if the local economy is weak. No exchange-rate cushion. |
| (b) Euro-area member | Own currency and own central bank | ECB policy follows euro-area aggregates. The member's own adjustment comes through its sovereign spread, its banks' capital, and domestic wages and prices. Property feels the spread and the bank channel (Examples 7.7–7.8). |
| (c) Float, independent central bank | Fixed exchange rate | The currency depreciates, absorbing part of the shock. The central bank chooses its policy rate. Local long yields may still rise through global term premia, but the transmission is partial and the bank can lean against it. |
| (d) Basket peg with outflow controls | Capital mobility | Controls prevent residents from moving savings abroad, which can keep local rates low and push domestic savings into local property. Risk accumulates as misallocation, and controls can be relaxed or circumvented. |

### Solution 7.3
(a) Estimate: $0.9 \times (4.5\% - 3.5\%) \approx 0.9\%$. Exact: $0.90 \times 0.010/1.035 = 0.870\%$ of GDP (a primary surplus).

(b) $d_1 = 0.90 \times 1.045/1.035 + 0.020 = 0.9087 + 0.020 = 0.9287$, or 92.87% of GDP.

### Solution 7.4
(a) $\lambda = 0.03/0.60 = 5.0\%$ per year.
(b) Estimate: $5 \times 5\% = 25\%$, less a little for compounding of survival. Exact: $1 - e^{-0.25} = 22.12\%$.
(c) $\lambda = 0.03/0.75 = 4.0\%$; five-year probability $= 1 - e^{-0.20} = 18.13\%$. The 40% recovery assumption gives the higher default probability. A given spread must be explained by expected loss; if each default loses less, defaults must be more frequent to produce the same spread.

### Solution 7.5
(a) Pair USD/CHF: base USD, quote CHF. $F = 0.88 \times 1.0025/1.04 = 0.848269$.

(b) Hedged gross return $= 1.043 \times F/S = 1.043 \times 1.0025/1.04 = 1.005392$, so **0.539%**. Pick-up versus the Swiss bond $= 0.539\% - 0.70\% = -0.16\%$ (−16 bp).

(c) Unhedged CHF gross return $= 1.043 \times S_T/0.88$. Set equal to 1.007: $S_T = 0.88 \times 1.007/1.043 = 0.849626$. The dollar can fall by **3.45%** against the franc before the unhedged Treasury underperforms.

(d) $1.043 \times 1.0025/(1 + r_{USD}) = 1.007 \Rightarrow r_{USD} = 3.834\%$. A fall of about 17 bp in the one-year USD rate, with the 10-year unchanged, closes the gap.

(e) Three-month forward: $F_{0.25} = 0.88 \times (1 + 0.0025 \times 0.25)/(1 + 0.04 \times 0.25) = 0.871832$. Forward discount over three months $= F_{0.25}/S - 1 = -0.9282\%$. Annualized by compounding: $(0.871832/0.88)^4 - 1 = -3.661\%$. One-year discount: $0.848269/0.88 - 1 = -3.606\%$. Rolling quarterly is about 5.6 bp per year more expensive at constant rates, because simple money-market rates compound when rolled. The larger practical differences are the cross-currency basis, which is often wider at short tenors and at quarter-ends, and the fact that a rolled hedge resets to future rate differentials (§7.7, item 3).

### Solution 7.6
(a) Effective rates: year 1: $0.025 + 0.2(0.025) = 3.000\%$; year 2: 3.400%; year 3: 3.720%; year 4: 3.976%; year 5: 4.181%.

(b)–(c) $d_{t} = d_{t-1}(1+r_t)/1.035 + 0.01$:

| Year | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Gradual repricing | 120.00% | 120.42% | 121.30% | 122.56% | 124.13% | 125.94% |
| Immediate repricing to 5.0% | 120.00% | 122.74% | 125.52% | 128.34% | 131.20% | 134.10% |
| No rate change (2.5%) | 120.00% | 119.84% | 119.68% | 119.53% | 119.37% | 119.22% |

After five years, the gradual path is about 6.7 points above the no-change path and 8.2 points below immediate repricing. The effective rate has closed only about two-thirds of the gap.

(d) Year-1 stabilizing balance under the gradual path: $1.20 \times (0.030 - 0.035)/1.035 = -0.580\%$, i.e., a primary deficit of 0.58% is still compatible with stable debt. Under immediate repricing: $1.20 \times 0.015/1.035 = +1.739\%$, a surplus. The government's budget shows a mild problem; the market, which prices the eventual effective rate, sees a large one. This gap in perception is why fiscal adjustments tend to be forced by markets after a delay rather than chosen early.

### Solution 7.7
(a) $\Delta\text{Reserves} = CA + \text{private net inflows} = 3\% - 1\% = 2\%$ of GDP $= 0.02 \times 2{,}000 = \$40$ billion.

(b) Unsterilized reserve purchases create domestic base money: the central bank pays local currency for dollars. Money and credit expand, local interest rates fall relative to what they would otherwise be, and property prices tend to rise. Under a peg with a persistent surplus, property booms financed by this liquidity are a recurring pattern [HYPOTHESIS as a general claim; check the specific country]. Sterilization (selling domestic bonds to absorb the money) limits this but has a carrying cost if domestic rates exceed the yield on reserves.

(c) $CA = (0.23 - 0.22) + (-0.05) = -4.0\%$ of GDP. If the budget deficit stays at 5% and the current account must reach zero, the identity requires $S_p - I$ to rise from +1% to +5% of GDP. Tariffs can only succeed if they raise private saving or reduce private investment by four points of GDP, for example through higher prices that lower real incomes and investment. Otherwise imports fall but the exchange rate, incomes, or exports adjust so that the current account changes little. The identity does not tell you which; it tells you the plan is incomplete.

### Solution 7.8
(a) $\Delta E = -9 \times 4.0 \times 0.03 = -€1.08$ billion. Equity $= 3.6 - 1.08 = €2.52$ billion. Assets $= 60 - 1.08 = €58.92$ billion. Leverage ratio $= 2.52/58.92 = 4.28\%$.

(b) $A^{max} = 2.52/0.06 = €42.0$ billion. Shrinkage $= 58.92 - 42.0 = €16.92$ billion. Non-sovereign assets $= 58.92 - 7.92 = €51.0$ billion, so every non-sovereign class shrinks by $16.92/51.0 = 33.2\%$. The CRE cut is $10 \times 0.3318 = €3.32$ billion.

(c) Equity needed $= 0.06 \times 58.92 - 2.52 = €1.015$ billion.

(d) Rate after pass-through $= 5.0\% + 0.4 \times 3.00\% = 6.2\%$.
Loan constants (25 years, monthly): $K_{5.0\%} = 0.070151$; $K_{6.2\%} = 0.078790$.
Maximum loan before: $1{,}000{,}000/(1.25 \times 0.070151) = €11{,}404{,}003$.
After: $1{,}000{,}000/(1.25 \times 0.078790) = €10{,}153{,}592$.
Change $= -10.96\%$. This is before any reduction in the bank's appetite or LTV limit, and before any change in the property's value.

(e) **Rubric (Level 4).** A strong answer:
* Recognizes that a bank which must cut a third of its non-sovereign assets is unlikely to extend new credit on the old terms, whatever the DSCR arithmetic says. Ask the bank directly about its CRE allocation and its capital plan.
* Seeks alternative lenders whose capital is not tied to the domestic sovereign (foreign banks, insurers, debt funds), accepting a higher spread if needed, and compares all-in costs.
* Considers an extension with the existing lender. A capital-constrained bank may prefer extending a performing loan to recognizing a loss on refinancing (extend-and-pretend has a rational basis here), and may accept a paydown plus a fee.
* Sizes the equity needed under the €10.15 million constraint, plus a buffer for further rate rises.
* Names the information to obtain first: the loan maturity and extension options, the bank's latest capital ratios and sovereign exposure, the availability and pricing of alternative lenders, and the property's current value.
* Does not assume the shock is temporary; considers that a central-bank backstop could compress the spread (as in 2012) but does not rely on it.

Answers that refinance mechanically at the bank's DSCR, or ignore the bank's own constraint, score 0–1.

### Solution 7.9
(a) Pair USD/JPY: $F = 150 \times 1.005/1.04 = 144.9519$. Year-end amount $= 40{,}000{,}000 + 3{,}200{,}000 = \$43{,}200{,}000$. Hedged return $= 1.08 \times 144.9519/150 - 1 = 4.365\%$. Equity in yen $= 40{,}000{,}000 \times 150 = ¥6{,}000{,}000{,}000$.

(b) At 165.00 the insurer delivers \$43.2 million worth ¥7,128 million at spot for ¥6,261.9 million. Settlement loss $= 43{,}200{,}000 \times (165.00 - 144.9519) = ¥866{,}076{,}923$, or **14.43%** of initial equity, payable in cash. Unhedged return $= 1.08 \times 1.10 - 1 = 18.80\%$.

(c) With 50% hedged, return $= 0.5 \times 4.365\% + 0.5 \times 18.80\% = 11.58\%$. The cash settlement is half of (b): 7.22% of equity.

(d) Unhedged return at 135.00: $1.08 \times 0.90 - 1 = -2.80\%$. A full hedge would have gained $43{,}200{,}000 \times (144.9519 - 135.00)/6{,}000{,}000{,}000 = 7.17\%$ of equity.

(e) **Rubric (Level 4).** A strong answer:
* Notes that the hedged return of 4.37% is far below the 8.0% dollar income yield, because the hedge costs about 3.4% a year at these rates.
* Chooses a partial hedge ratio (for example 30–60%) or no hedge, and states why: the cost of hedging, the insurer's liability currency, its regulatory treatment of FX risk, and its tolerance for currency volatility in reported results.
* Holds a yen liquidity reserve sized to the hedge settlement in a plausible adverse move (for example 7–15% of equity for a 10% move on a 50–100% hedge), or uses longer-dated or option-based hedges to reduce cash calls.
* Considers dollar debt as a natural hedge and checks whether leverage is positive or negative at current U.S. rates.
* Explains demand mix: a U.S. hotel serving foreign tourists loses demand when the dollar is strong, partly offsetting the translation gain for a yen owner. A hotel serving domestic business travelers has NOI with little direct FX sensitivity, so the yen owner's exposure is mostly translation. The hedge decision should reflect which exposure dominates.

### Solution 7.10 — Rubric (Level 5; abstention is the best answer on the facts given)

**Arithmetic anchors.** Price $= 0.72 \times 45{,}000{,}000 = \$32.4$ million. Debt yield at par $= 4.1/45 = 9.11\%$; at the purchase price $= 4.1/32.4 = 12.65\%$. Stale appraised LTV $= 45/58 = 77.6\%$. Value at a 9% cap on current NOI $= \$45.6$ million; at 11% $= \$37.3$ million. The purchase is covered only if dollar NOI holds and cap rates do not reprice sharply, before enforcement costs and time.

| Dimension | Strong answer includes |
|---|---|
| Devaluation mechanics | Dollar-paying foreign demand (60%) is protected in dollar terms and may even rise if the country becomes cheaper. Local-currency revenue (40%) falls in dollars. Costs are mostly local, so they fall in dollars too: dollar NOI may *rise* after a devaluation if foreign demand holds. The borrower's ability to pay depends on whether dollar revenue is paid into accounts it can access. Capital or withdrawal controls can block dollar debt service even when the hotel is profitable: **transfer and convertibility risk**, not operating risk. |
| Price implications | At \$32.4 million you need recovery of at least 72% of par plus carry and costs to break even. The appraisal is stale and pre-dates the reserve loss. |
| Ranked unknowns | (1) Enforceability and timeline of the security in this jurisdiction, and whether dollar collections can be swept offshore; (2) the reality of informal dollar controls and the risk of formal controls; (3) the loan documents (cash management, guarantees, governing law, cross-defaults) and the borrower's other dollar debts. Operating unknowns rank below these. |
| Decision | Do not submit a binding bid in five business days without documents and legal advice on enforcement. Either decline, or submit a non-binding indication subject to diligence, at a price that reflects transfer risk, with exclusivity. A binding bid on these facts is a bet on the peg and on local courts, not on a hotel. |
| What changes the answer | Loan documents showing an offshore dollar collection account under foreign law; a legal opinion on enforcement; evidence that reserves have stabilized or that an IMF program is in place; a longer diligence window; a price low enough to compensate for a multi-year enforcement in a controlled-capital regime. |

Answers that value the resort on trailing NOI and the old appraisal and bid, or that treat the peg statement as information, score 0–1. Answers that decline and explain why, or that bid non-bindingly with clear conditions, can score full marks.

---

### Decision exercise (§7.10) — Rubric

**Value grid** (NOI after reserve; direct capitalization):

| Cap rate | NOI €3.80 million | NOI €3.42 million (−10%) |
|---|---|---|
| 6.0% | €63.33 million | €57.00 million |
| 6.5% | €58.46 million | €52.62 million |
| 7.0% | €54.29 million | €48.86 million |

A loan bought at 65% of par (€33.8 million) has an LTV on the worst cell of $33.8/48.86 = 69.2\%$, and remains covered with a further cushion.

| Element | Full credit (4) | Partial (2) | None (0) |
|---|---|---|---|
| Value range | Uses the grid; separates a reversible sovereign/liquidity premium (the move from 5.0% to 6.0–6.5%) from permanent re-rating; NOI stress included | Range without the decomposition | Single value at the old cap rate |
| Currency | Computes hedge cost from short-rate differential; explains that a forward on EUR does not protect against redenomination of a Spanish euro claim, which is legal and jurisdictional risk | Mentions FX without redenomination | Ignores currency |
| Structure | Prefers a senior position (loan at a discount, or preferred equity above the €11.3 million of remaining equity) with covenants and control rights | Buys equity with a discount but no structure | Buys equity at the bank's asking price |
| Counterparty | Analyzes why the bank sells (provisions, capital, Example 7.7) and the information-asymmetry risk | Mentions the bank's pressure | Treats the discount as a free lunch |
| Sizing and invalidation | Sized to survive a further 30% value fall; names invalidation events (explicit euro-exit planning, bank resolution, capital controls) | Sizing without invalidation | Concentrated bet |
| Waiting | Values the option to wait: policy uncertainty would resolve within months | Mentions waiting | Ignores it |
| No hindsight | Uses only information to 30 June 2012 | Minor hindsight | Relies on Draghi or OMT |
