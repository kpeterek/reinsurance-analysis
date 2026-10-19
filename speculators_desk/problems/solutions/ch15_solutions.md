# Chapter 15 Solutions — Foreign Exchange

Numerical results are verified in `tests/test_ch15_examples.py`. Figures are rounded for display only. All market data are hypothetical.

---

### Solution 15.1
(a) Direct quotes for a U.S. investor (USD is QUOTE): **EUR/USD and GBP/USD**. USD/JPY and USD/CHF are indirect.

(b) The dollar appreciated; the yen depreciated. The U.S. owner of a Tokyo building loses in dollars: the home value of ¥1 falls from 1/150 to 1/155 dollars, a change of $150/155 - 1 = -3.23\%$. The Japanese owner of a Dallas hotel gains in yen: one dollar of hotel value is now worth ¥155, +3.33%.

(c) If EUR/USD rose 5%, from $S_0$ to $1.05S_0$, the dollar's value in euros changed by $1/1.05 - 1 = -4.76\%$. The dollar fell 4.76%, not 5%.

(d) A EUR/USD position is denominated in euros (BASE), and its price is in dollars (QUOTE), so price changes are dollar amounts. USD/JPY P&L is in yen; convert at the **closing** rate, since that is the rate at which the yen P&L could be converted when it is realized.

### Solution 15.2
(a) $1.20/1.25 - 1 = -4.00\%$.
(b) $1.25/1.20 - 1 = +4.17\%$.
(c) $(1.2000 - 1.2500)/0.0001 = -500$ pips.
(d) Short: $-1 \times 5{,}000{,}000 \times (1.20 - 1.25) = +\$250{,}000$.

### Solution 15.3
(a) AUD/JPY = AUD/USD × USD/JPY (multiplicative). Bid = $0.6600 \times 150.00 = 99.000$ (sell AUD for USD at the AUD/USD bid, then sell USD for JPY at the USD/JPY bid). Ask = $0.6604 \times 150.04 = 99.086$.

(b) EUR/CHF = EUR/USD × USD/CHF (multiplicative). Bid = $1.0850 \times 0.8800 = 0.95480$. Ask = $1.0854 \times 0.8804 = 0.95559$.

In each case the synthetic bid uses both legs' bids because you are selling the cross BASE through both legs, and each leg's dealer buys from you at their bid. The synthetic ask uses both asks.

### Solution 15.4
(a) $F = 150.00 \times (1 + 0.004 \times 90/365)/(1 + 0.043 \times 90/360) = 150.00 \times 1.000986/1.010750 = 148.551$. Forward points $= (148.551 - 150.00)/0.01 = -144.9$ pips. The dollar, the higher-yielding currency, trades at a forward discount.

(b) $(148.551/150.00 - 1) \times 360/90 = -3.86\%$ a year, close to the rate differential of $0.40\% - 4.30\%$ after allowing for day counts and the division by $1 + r_{USD}\tau$.

(c) The dealer's 148.80 is **above** the CIP forward: dollars are rich forward. Sell dollars forward to the dealer at 148.80 and buy dollars forward synthetically:
1. Borrow yen; buy \$10,000,000/1.010750 = \$9,893,643 spot at 150.00, costing ¥1,484,046,500.
2. Invest the dollars at 4.30% for 90 days: \$10,000,000 at maturity.
3. At maturity deliver \$10,000,000 to the dealer and receive ¥1,488,000,000.
4. Repay the yen loan: $1{,}484{,}046{,}500 \times 1.000986 = ¥1{,}485{,}510{,}217$.

Profit $= 10{,}000{,}000 \times (148.80 - 148.551) = ¥2{,}489{,}783$.

(d) (i) A cross-currency basis: dealers price the balance-sheet cost of the trade, especially at quarter-ends. (ii) The deposit rates used are not the rates the arbitrageur can actually borrow and lend at (credit spreads, collateral). Also: stale or indicative quotes.

### Solution 15.5
Yen notional $= 10{,}000{,}000 \times 99.00 = ¥990{,}000{,}000$. $s = 92/99 - 1 = -7.07\%$.

(a) $\Pi = 990{,}000{,}000 \times [(1 + 0.041 \times 0.5)(92/99) - (1 + 0.005 \times 0.5)] = -¥53{,}615{,}000$.
* Carry $= 990{,}000{,}000 \times (0.041 - 0.005) \times 0.5 = ¥17{,}820{,}000$.
* Spot $= 10{,}000{,}000 \times (92 - 99) = -¥70{,}000{,}000$.
* Cross $= 990{,}000{,}000 \times 0.0205 \times (-0.0707) = -¥1{,}435{,}000$.
* Sum $= -¥53{,}615{,}000$. ✓

(b) Margin ¥99,000,000. Return $= -54.16\%$.

(c) Break-even $= 99.00 \times 1.0025/1.0205 = 97.254$. With spot unchanged, P&L = carry = ¥17,820,000 (+18.0% on margin).

### Solution 15.6
(a) Naive: $24/1.5 = 16$ months. Attack: $T = (24 - 4 \times 1.5)/1.5 = 12$ months. Reserves lost on the day: $\alpha\mu = \$6$ billion.
(b) $T = (30 - 6)/1.5 = 16$ months. The credit line buys four months.
(c) $T = (24 - 8 \times 1.5)/1.5 = 8$ months. The attack comes four months earlier with no change in reserves or the deficit.
(d) The life of the peg depends on the *stock* of mobile money relative to reserves, not only on the drain. Monitor short-term external debt, non-resident holdings of local deposits and bonds, and the ease of moving them (capital-account openness, bank funding structure), alongside reserves.

### Solution 15.7
(a) $F_0 = 1.10 \times 1.04/1.02 = 1.121569$. At the first roll, $F_1 = 1.00 \times 1.04/1.02 = 1.019608$.

(b) Year 1: $66{,}000{,}000 \times (1/1.121569 - 1/1.00) = 58{,}846{,}154 - 66{,}000{,}000 = -€7{,}153{,}846$ (paid).
Year 2: $66{,}000{,}000 \times (1/1.019608 - 1/1.05) = 64{,}730{,}769 - 62{,}857{,}143 = +€1{,}873{,}626$ (received).

(c) Initial euro equity $= 66{,}000{,}000/1.10 = €60{,}000{,}000$. The year-1 call is **11.92%** of equity. Year-1 NOI at 1.00 is €3,630,000, covering about 51% of the call, leaving a shortfall of €3,523,846.

(d) At an unchanged dollar value, the building is worth $66{,}000{,}000/1.00 = €66{,}000{,}000$, an unrealized gain of €6,000,000. The hedge loss offsets most of it, but the hedge loss is cash and the gain is not.

(e) **Rubric (10 points).**
* (2) Identifies that the problem is liquidity, not hedge effectiveness: the hedge did its job.
* (2) Proposes a reserve sized to a stated stress move (e.g. 2σ of EUR/USD on the hedged notional) or a reduced hedge ratio consistent with the reserve.
* (2) Considers U.S. dollar debt on the building as a natural hedge, noting its cost (negative leverage if the debt rate exceeds the cap rate; Chapter 7, Example 7.6(d)).
* (2) Considers a longer-dated forward or cross-currency swap with collateral thresholds, or options (a EUR call/USD put collar), and states their cost.
* (2) Resets the hedge notional to a stated exposure measure and specifies what happens if a sale is delayed past a roll date.

What would change the answer: a cheaper basis, a larger general-account liquidity buffer at the insurer, regulatory treatment of unhedged currency exposure, or a change in the correlation between the building's value and EUR/USD.

### Solution 15.8
(a) $h^* = 1 + 0.30 \times 0.15/0.10 = 1.45$.
(b) $h_{liq} = 1{,}500{,}000/(2 \times 0.10 \times 20{,}000{,}000) = 0.375$.
(c) $\sigma(h) = \sqrt{0.15^2 + (1-h)^2 (0.10)^2 + 2(1-h)(0.30)(0.15)(0.10)}$:

| $h$ | 0 | 0.375 | 1.00 | 1.45 |
|---|---|---|---|---|
| $\sigma(h)$ | 20.37% | 17.90% | 15.00% | 14.31% |

(d) **Rubric (10 points).**
* (2) Recognizes that with $\rho > 0$ the minimum-variance hedge exceeds 1; over-hedging is a currency short that only reduces variance if the correlation holds.
* (2) Notes the policy cap of 1.00 and the much tighter liquidity cap of 0.375; at 0.375 volatility is 17.9% versus 15.0% at 1.00.
* (2) Computes the reserve needed for $h = 1$: $2 \times 0.10 \times 20{,}000{,}000 = \$4{,}000{,}000$, and compares its opportunity cost with the 2.9-point reduction in volatility.
* (2) Considers local-currency debt (which hedges without roll calls) and options.
* (2) Questions the correlation estimate: with few observations and a regime-dependent relationship, an $h$ above 1 built on $\rho = 0.30$ is fragile.

A defensible answer: raise the reserve toward \$4 million and hedge at or near 1.00, or refinance part of the equity with local debt; do not over-hedge above 1.00 on a single correlation estimate.

### Solution 15.9
(a) Carry cost $= (0.20 - 0.05)/12 = 1.25\%$ for one month. $p^* = (0.005 + 0.0125)/(0.15 + 0.005) = 11.29\%$.

(b) Required monthly cost: $c = pd - (1-p)u = 0.40 \times 0.15 - 0.60 \times 0.005 = 5.70\%$. Annualized differential $= 68.4\%$; overnight rate about $5\% + 68.4\% = 73.4\%$.

(c) The bank sold \$20 billion at 25.0 and received 500 billion local units. Rebuying at 40.0 costs 800 billion. Loss = **300 billion local units**, which is **\$7.5 billion** at 40.0.

(d) **Rubric (10 points).**
* (2) Recognizes that once speculators' probability exceeds about 11%, a one-month short is attractive at current rates, and that deterring it requires rates near 73%, with severe domestic costs (second-generation logic).
* (2) Quantifies the reserve loss from a failed defense, and notes that each further dollar sold at the peg raises the eventual loss.
* (2) Considers the fundamentals: if the peg is inconsistent with fiscal or monetary policy (first-generation), defense only delays the outcome and spends reserves.
* (2) Weighs the costs of devaluation: dollar-denominated private debt, bank balance sheets, inflation pass-through, and credibility.
* (2) Proposes an orderly alternative (a pre-emptive, larger-than-expected adjustment to a defensible level with fiscal measures, an IMF program, or a move to a float with an inflation target) rather than a binary defend/devalue.

### Solution 15.10
(a) The 9% annual forward discount means one dollar costs 9% more local currency forward than spot: $F/S = 1.09$ in local-per-dollar terms. Hedged dollar yield $= 1.11/1.09 - 1 = 1.83\%$, below the 4.25% T-bill.

(b) Unhedged: $1.11 \times (1 - 0.30 \times 0.35) - 1 = 1.11 \times 0.895 - 1 = -0.655\%$.

(c) Solve $1.11(1 - 0.35p) = 1.0425$: $p = (1 - 1.0425/1.11)/0.35 = 17.4\%$.

(d) **Best answer: abstain for now.** The hedged yield is below a riskless dollar alternative, so the asset offers no spread once currency risk is removed. Hedging transports the spread, and here the spread over local short rates is small. The unhedged return beats T-bills only if the annual devaluation probability is below about 17%, and the indicators (falling reserves, a 6% current-account deficit, large non-resident deposits, a 9% forward discount) suggest the market already prices a material probability. You do not know short-term external debt, which is the key variable in a first-generation timing analysis.

**Rubric (10 points).**
* (2) Computes the hedged yield and compares it with T-bills, recognizing that hedging transports the spread.
* (2) Computes the unhedged break-even probability and relates it to the market-implied signal in the forward discount.
* (2) Identifies the missing data (short-term external debt, non-resident holdings, reserve adequacy, forward-market depth beyond one year) and why each matters.
* (2) Recognizes illiquidity: a hotel cannot be sold quickly in a crisis, and the NDF hedge is one year against a multi-year hold, so rolling it may become impossible or costly when it is most needed.
* (2) States what would change the decision: a credible IMF program or reserve build, a large price reduction (pricing in the devaluation), local-currency debt for most of the capital stack, or an exit option. Accepting the deal because "the peg has never been in doubt" earns no credit.

---

## Decision exercise (§15.10) — Rubric

| Item | Full credit | Partial | None |
|---|---|---|---|
| London hotel hedge | Hedge ratio justified by both variance ($h^*$ with a stated $\rho$) and liquidity ($h_{liq}$ with a stated stress move); notional reset rule; plan for a delayed sale | Hedge ratio stated with one justification | "Hedge 100%" or "do not hedge" by habit |
| Carry trade | Break-even crash probability computed; acknowledges the track record cannot identify $p$; size limited so a crash costs a tolerable fraction of capital, or abstains | Computes carry but not crash EV | Treats carry as income |
| Pegged-currency hotel | Hedged yield compared with T-bills; unhedged return recognized as a peg bet; missing data named; abstention or price reduction | Computes yields but accepts the peg as given | Compares 11% with U.S. cap rates directly |
| Invalidation | Specific triggers (reserve thresholds, basis widening, forward discount, policy-rate moves) | Generic | None |

Declining the carry trade and the pegged-currency hotel while hedging the London hotel at 0.4–0.7 with a stated reserve can earn full credit. So can a small, explicitly sized carry position with a stop-loss and a stated $p$, if its crash loss fits the risk budget.
