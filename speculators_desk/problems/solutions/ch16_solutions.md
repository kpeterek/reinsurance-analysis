# Chapter 16 Solutions

Numerical results are verified in `tests/test_ch16_examples.py`. Figures are rounded for display only. All inputs are hypothetical [HYPOTHESIS] unless cited.

---

### Solution 16.1
(a) **Incorrect.** Backwardation means prompt barrels are scarce relative to deferred ones: inventories are low and the convenience yield is high. The futures price can differ from the expected spot price by a risk premium of either sign, so the curve is not a forecast. A buyer who waits is not "buying cheaper later". They are betting that spot falls toward the deferred price, and they bear the risk of a further squeeze. If the buyer needs fuel at a future date, the deferred futures price is the price they can lock in today.

(b) **Plausibly correct.** Contango near full carry is the theory-of-storage signature of ample inventory: the marginal holder is paid roughly financing plus storage. Confirm with inventory data, because exchange-warehouse stocks can differ from total stocks.

(c) **Incorrect.** Full carry bounds the curve only at the marginal storer's cost. When storage is nearly full, the marginal cost of storage rises sharply and the curve can sit far above *your* full carry without any arbitrage being available to anyone who lacks tank space (Example 16.4; April 2020).

(d) **Approximately correct.** Gold stocks are large relative to flows, the convenience yield (lease rate) is small, and the curve sits near financing carry. The rolling position earns spot change + collateral − (roughly) financing carry + lease rate. Excess return over bills is therefore close to the spot change less a small carry cost. It is not exactly spot.

(e) **Incorrect.** July is old crop and December is new crop. Stocks are lowest just before harvest and highest just after, so a July premium over December (an inverse) reflects scarce old-crop stocks. Storage cannot move new-crop corn back in time, so no cash-and-carry trade connects the two.

### Solution 16.2
(a) $+1 \times (29.15 - 28.40) \times 5{,}000 \times 2 = 0.75 \times 10{,}000 = +\$7{,}500$.
(b) $-1 \times (4.215 - 4.380) \times 25{,}000 \times 3 = 0.165 \times 75{,}000 = +\$12{,}375$.
(c) 437'0 = 437.00¢ and 425'4 = 425.50¢ (4/8 = 0.5). Move −11.50¢ × \$50 per cent × 4 = **−\$2,300**. (Reading cents as dollars would give −\$230,000.)
(d) $(3.140 - 2.875) \times 10{,}000 = +\$2{,}650$.
Total $= 7{,}500 + 12{,}375 - 2{,}300 + 2{,}650 = +\$20{,}225$.

### Solution 16.3
(a) $F = 2{,}000\, e^{(0.040 - 0.005)} = 2{,}000 \times 1.035620 = \$2{,}071.24$/oz.
(b) $2{,}000\, e^{0.04} = \$2{,}081.62$/oz.
(c) $2{,}071.24 \times 100 \times 10 = \$2{,}071{,}239$.
The lease rate plays the role of the convenience yield. It is small, so the gold curve sits close to financing carry.

### Solution 16.4
(a) $S e^{rT} = 60\, e^{0.0125} = \$60.7547$. $U_T = 3 \times 0.45 = \$1.35$. $F^* = 60.7547 + 1.35 = \$62.1047$.
$u = \frac{1}{0.25}\ln(1 + 1.35/60.7547) = 4\ln(1.022220) = 8.79\%$.

(b) $F = 63.20 > F^*$. Borrow \$60.00, buy a barrel, store it, and sell the three-month future at \$63.20. At delivery receive \$63.20, repay \$60.7547 and pay \$1.35 of storage. Profit $= 63.20 - 62.1047 = \$1.0953$/bbl; on 20 contracts $1.0953 \times 1{,}000 \times 20 = \$21{,}906$.
Implied $y = 4\ln(62.1047/63.20) = -6.99\%$. A negative convenience yield means the quoted curve pays more than full carry at the assumed storage cost. Either an arbitrage exists or the assumed storage is not actually available at \$0.45.

(c) $y = 4\ln(62.1047/58.80) = 21.87\%$. No arbitrage is available to someone without inventory: the reverse trade requires selling barrels you do not own. A refiner or merchant holding crude could sell spot and buy futures, earning financing and storage savings. They do not, because the barrel in the tank is worth more to them now (it keeps a unit running or fills an order). That is the convenience yield.

### Solution 16.5
(a) Components ($F_t$ in the denominator):

| Month | Spot | Roll | Collateral | Total |
|---|---|---|---|---|
| 0 | $(78-80)/79 = -2.5316\%$ | $(80-79)/79 = +1.2658\%$ | 0.35% | −0.9158% |
| 1 | $(81-78)/77.2 = +3.8860\%$ | $(78-77.2)/77.2 = +1.0363\%$ | 0.35% | +5.2723% |
| 2 | $(77-81)/80.1 = -4.9938\%$ | $(81-80.1)/80.1 = +1.1236\%$ | 0.35% | −3.5202% |

(b) Compounded total $= (0.990842)(1.052723)(0.964798) - 1 = +0.636\%$. Compounded excess $= -0.415\%$. Spot change $= 77/80 - 1 = -3.75\%$.

(c) $\ln(77/80) = -3.8221\%$; $\sum\ln(S_t/F_t) = \ln(80/79) + \ln(78/77.2) + \ln(81/80.1) = +3.4061\%$. Sum $= -0.4160\%$, and $e^{-0.004160} - 1 = -0.415\%$, matching the compounded excess. ✓

(d) Wrong. Spot fell 3.75%, but positive roll (+3.4% in logs) offset almost all of it, and collateral interest turned the total positive (+0.64%). In backwardation a long rolling position is paid to hold. The colleague confused the spot index with the investable return.

### Solution 16.6
(a) Purchase per delivered unit $= 2.60/0.985 = \$2.6396$. Financing $= 2.6396 \times 0.06 \times 7/12 = \$0.0924$. Margin $= 3.40 - 2.6396 - 0.03 - 0.03 - 0.25 - 0.0924 = \$0.3580$/MMBtu. Total $= 0.3580 \times 5{,}000{,}000 = \$1{,}790{,}102$.
(b) Buy $5{,}000{,}000/0.985 = 5{,}076{,}142$ MMBtu, which is 507.6 contracts, so **508 long** summer contracts (or 507 with a small open short, stated). Sell **500** winter contracts.
(c) Break-even winter price $= 2.6396 + 0.03 + 0.03 + 0.25 + 0.0924 = \$3.0420$. The winter strip can fall 35.8 cents before intrinsic value is gone.

### Solution 16.7
(a) Rigs $1.2 \times (-35\%) = -42\%$; energy demand $0.85 \times (-42\%) = -35.7\%$; total demand $0.60 \times (-35.7\%) = -21.42\%$.
Occupancy $= 0.76 \times 0.7858/1.05 = 56.88\%$, a change of −25.16%.
ADR $= 135 \times (1 - 0.6 \times 0.2516) = \$114.62$.
RevPAR from \$102.60 to \$65.19, a change of **−36.5%**.

(b) Operating statement:

| Line | Before | After |
|---|---|---|
| Rooms revenue | \$3,370,410 | \$2,141,548 |
| Total revenue | \$3,505,226 | \$2,227,210 |
| GOP | \$1,666,441 | \$688,187 |
| EBITDA | \$984,243 | \$167,216 |
| NOI (after 4% reserve) | **\$844,034** | **\$78,128** |

NOI falls 90.7% on a 36.5% revenue decline.

(c) $\Delta NOI = \$765{,}906$; $\Delta P = 75 - 48.75 = \$26.25$; $\beta = \$29{,}177$ per \$/bbl; $N = 29.2$, so **29 short CL**. Hedge P&L at expiry with oil at \$48.75: $29 \times (71 - 48.75) \times 1{,}000 = \$645{,}250$. That covers **84.2%** of the NOI loss. The gap comes from backwardation: the hedge sells at \$71, not \$75.

(d) **Rubric.**
* *Instrument.* NOI is concave in oil (little upside at 76% occupancy, large downside). A put or put spread on 12-month WTI matches that shape. A short future gives away upside the hotel cannot capture anyway, but it creates margin calls if oil rises.
* *Basis.* CL hedges Cushing crude. The hotel's exposure is to local drilling activity, which depends on Permian differentials, operator budgets and productivity, not only on WTI.
* *Lags.* Room-night demand lags rigs, and rigs lag prices. A 12-month hedge may expire before the demand loss peaks.
* *Liquidity.* A 29-contract short needs a margin reserve. A \$25 rally costs \$725,000 in variation margin, nearly the hotel's pre-shock NOI.
* *What is unhedged.* The capital loss from many years of lower NOI and a higher cap rate, and the effect of new supply.
* *Alternatives.* Lower leverage, a reserve fund, or a lower purchase price.
* *Recommendation.* A modest put position sized to protect debt service, not NOI, is defensible. A full futures hedge is not a substitute for underwriting at mid-cycle oil. "No hedge, lower leverage" is also acceptable if argued.

### Solution 16.8
(a) $\Delta H = 42{,}000{,}000 \times (0.06 \times -0.20 + 0.09 \times 0.30 + 0.025 \times 0.40) = 42{,}000{,}000 \times 0.025 = \$1{,}050{,}000$.
$RC_0 = 6.0 + 42.0 \times 1.20 = \$56.40$ million; $RC_1 = 6.0 + 43.05 \times 1.20 = \$57.66$ million, **+2.23%**. Falling lumber offsets part of the steel rise. Industrial buildings are steel-heavy.

(b) Copper content $= 0.025 \times 42{,}000{,}000 = \$1{,}050{,}000$, which is $1{,}050{,}000/4.50 = 233{,}333$ lb, or 9.33 contracts. Use **9 long HG**. If copper rises 40%, the hedge earns $9 \times 25{,}000 \times 4.50 \times 0.40 = \$405{,}000$, against a cost rise of \$420,000.

(c) **Rubric.** The GMP premium is $0.015 \times 42{,}000{,}000 = \$630{,}000$. It insures all commodity-sensitive materials (17.5% of hard cost, \$7.35 million) plus other material price risk, subject to the contractor's credit and the contract's exclusions. Copper futures hedge only \$1.05 million of exposure and leave steel, the largest risk here, unhedged. Considerations:
* Taking the GMP **and** hedging copper makes the copper position a speculation, because the developer no longer bears copper risk.
* Compare the GMP premium with the expected cost of the risk transferred. Steel volatility and the bid-period length drive that comparison.
* Check the contractor's balance sheet. A GMP from a weak contractor is a promise that can fail exactly when prices spike.
* Information that would change the answer: GMP exclusions (escalation clauses for steel are common), the contractor's credit, the length of time before material buyout, and the lender's requirements.
* A defensible answer is "take the GMP if the contractor is creditworthy and steel is not excluded; do not hedge copper on top". Another defensible answer is to hedge copper and lock steel through an early mill order, if the GMP premium is excessive.

### Solution 16.9
(a) P&L $= +1 \times (-37.63 - 17.73) \times 1{,}000 = -\$55{,}360$. The prior notional was \$17,730, so the loss is **3.12 times** the prior notional in one day.

(b) Let $F_{May}$ and $F_{Jun}$ be the two prices. Rolling a long means selling May and buying June, at a cost per barrel of $F_{Jun} - F_{May}$. As expiry approached, a May long had to either take delivery at Cushing or sell to someone who could. With tank farms near their usable limit and spare capacity largely committed (EIA; §16.8.4), the marginal storage cost $u$ rose sharply, and the May–June spread widened toward the right-hand tail of the Working curve. Every day of delay raised the roll cost. For 2,000 contracts the cost is $2{,}000{,}000 \times (F_{Jun} - F_{May})$ dollars. A \$1 widening costs \$2 million.

(c) *Knowable on 14 April:* the demand collapse, rising Cushing inventories and the published storage capacity (EIA weekly data), the contract's physical delivery terms, and the expiry date. *Not knowable:* the exact settlement path in the last two days, and whether enough storage-holding buyers would appear. *Discipline:* a desk that cannot take delivery treats the contract as a security with a hard exit date. It rolls or closes well before the last trading days, sizes the position for the possibility that the expiring contract cannot be sold at a positive price, and does not assume a zero lower bound.

(d) An energy-market hotel owner faced lower drilling and crew travel. At the same time, pandemic travel restrictions cut all demand segments. Because both shocks hit in the same months, a 2020 RevPAR decline cannot be attributed to oil without a control group, such as non-energy markets with similar pandemic exposure.

### Solution 16.10 (Level 5) — rubric
Implied price $= 205{,}000 \times 220 = \$45.1$ million. At a 6.25% cap, implied in-place NOI $= \$2{,}818{,}750$, or \$12,812.50 per unit.

(a) *Claims.*
* 97% occupancy with rents up 14%: consistent with a boom market. It says nothing about through-cycle NOI, and "in-place" may mean annualized current rents, not trailing collections.
* "Backwardation means a soft landing": wrong reasoning. Backwardation reflects tight inventory, not a forecast (§16.2).
* "Replacement cost above \$250,000": RC is a supply ceiling, not a value floor. In a demand collapse, existing assets trade below RC for years (Chapter 8).
* The pipeline project ending in 8 months is a known, dated loss of contract demand.

(b) *Facts that most change value, ranked:* (1) the share of residents employed in energy and pipeline construction, and the lease expirations tied to the pipeline project; (2) the trailing-12 monthly NOI versus "in-place" (concessions, bad debt, other income); (3) the supply pipeline of competing units delivering in the next 18 months.

(c) *Call requests:* rent roll with move-in dates and employers (or corporate leases), monthly T-12 and concession history, the in-place NOI calculation, corporate-lease agreements, and the seller's reason for selling now.

(d) *Recommendation.* Do not submit an offer before receiving the rent roll and T-12. A non-binding indication is acceptable only if it is explicitly conditioned and priced on through-cycle NOI. If the data never arrive, the committee recommendation is **abstain**: the value range spans more than any plausible edge, and the one dated fact in the teaser (pipeline completion) is negative. Full credit requires an explicit abstention case and a list of data that would reopen the decision.

---

## Decision exercise (Chapter 16, §16.9) — rubric detail

**Item 1.**
* *Stress NOI* from Example 16.6: \$658,054. At 55% LTV, 7.0%, 25-year amortization, the loan constant is 8.4814%. For DSCR ≥ 1.20x, maximum debt service $= 658{,}054/1.20 = \$548{,}379$, maximum loan $= \$6{,}465{,}699$, and maximum price $= 6{,}465{,}699/0.55 = \$11.76$ million. That is 34% below the \$17.8 million ask. A buyer who wants to pay more must either accept DSCR below 1.20x in the stress case, use lower leverage, or argue that the −45% oil case is too severe and say why.
* *Through-cycle NOI* between the base (\$1.69 million) and stress (\$0.66 million) figures, weighted by explicit probabilities, with the oil price assumption stated.
* *Hedge:* puts preferred; one-year income protection only; basis, lag and margin risk stated.
* *Walk-away:* energy-linked share materially above 50%, or a large contract (crew) account with a defined end date.

**Item 2.** RC after the shock is \$243,191 per unit against a projected stabilized value of \$255,000, a margin of 4.9%. That is thin for development risk. Full credit identifies the thin margin, asks who bears input risk under the construction contract, and recognizes that a copper hedge covers about 9% of the commodity shock.

**Item 3.** A rolling long is paid spot + roll + collateral. In a glut its expected roll is negative. The partner's spot chart is not evidence about the strategy's return. If the aim is to protect against construction-cost inflation, fix prices contractually (GMP, early material buyouts) or hedge specific inputs. An index of energy futures does not hedge apartment construction costs.
