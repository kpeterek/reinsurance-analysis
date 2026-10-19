# Chapter 9 Solutions

Numerical results are verified in `tests/test_ch09_examples.py`. Figures are rounded for display only.

---

### Solution 9.1
(a) **Seller's reservation price only.** The purchase price is a sunk cost. It predicts the owner's reluctance to sell below it (anchoring, loss aversion) and matters for the owner's taxes. It says nothing about current cash flows or required returns.

(b) **Weak, stale evidence of value, and evidence of the owner's anchor.** An appraisal is an opinion at a date, built from transactions before that date. Use its rent roll and expense data. Discount its cap rate and its conclusion, especially if market conditions or the lease profile have changed since (Example 9.12).

(c) **Evidence about supply, not value.** If value is far below replacement cost, new competing buildings will not be built, which supports future rents. It is a long-run ceiling on value through supply, never a floor (Example 9.13).

(d) **The best direct evidence, with adjustments.** Time-adjust for market movement since each sale. Adjust the lender's REO sale for conditions of sale: it may be below market (forced) or reflect a building in worse condition. Recent sales are few and selected, so treat the indication as a range.

(e) **Evidence of the bid side and of selection bias.** Withdrawn listings show where bids sat when sellers refused. In a falling market they are often more informative than closed sales about where the stock would clear.

(f) **Evidence of the listed market's view of value, which needs adjustment.** REIT-implied cap rates reflect levered, liquid, diversified portfolios priced daily. They lead appraisals, but differ in quality, leverage, and composition from a single private building. Use them as a directional signal and a check on stale private marks (§9.9).

### Solution 9.2
(a) $V_0 = 1{,}800{,}000/0.06 = \$30.0$m. $NOI_1 = 1{,}710{,}000$. $V_1 = 1{,}710{,}000/0.0675 = \$25.33$m. Change $= 0.95 \times 6.00/6.75 - 1 = -15.6\%$.

(b) Loaded cap $= 6.00\% + 1.50\% = 7.50\%$. $V = 2{,}200{,}000/0.075 = \$29.33$m. Forgetting reassessment means capitalizing pre-tax NOI at 6.00%: \$36.67m, an overstatement of \$7.33m (25% of the correct value). A partial version of this error, using the seller's lower tax bill, is the common real-world case (Example 9.2).

### Solution 9.3
(a) $g = k - c(1-\kappa) = 7.50\% - 5.25\% \times 0.90 = 7.50\% - 4.725\% = 2.775\%$.
(b) $k = c(1-\kappa) + g = 4.725\% + 2.00\% = 6.725\%$.
(c) $c = (k-g)/(1-\kappa) = (0.075 - 0.02)/0.90 = 6.11\%$.

At 5.25% a buyer requiring 7.50% must believe in about 2.8% perpetual NOI growth. If growth is 2%, the buyer earns about 6.7%. Whether that is adequate depends on the alternative, such as the Treasury yield plus a risk premium, at the time of the decision.

### Solution 9.4
(a)

| Year | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| NOI | 1,000,000 | 1,025,000 | 1,050,625 | 1,076,891 | 1,103,813 | 1,131,408 |
| Capital (3% of NOI; roof Y3) | 30,000 | 30,750 | 431,519 | 32,307 | 33,114 | — |
| Cash flow | 970,000 | 994,250 | 619,106 | 1,044,584 | 1,070,699 | — |

Reversion: gross $= 1{,}131{,}408/0.07 = \$16{,}162{,}974$; net $= \$15{,}839{,}715$. PV of reversion at 8.5% over 5 years $= \$10{,}534{,}130$.
**Value = \$14,223,221.**

(b) Reversion share $= 10{,}534{,}130/14{,}223{,}221 = 74.1\%$. Going-in cap $= 1{,}000{,}000/14{,}223{,}221 = 7.03\%$.

(c) Capitalizing Year 5 NOI (\$1,103,813) gives \$13,966,291, an understatement of \$256,930 (1.8%). The error equals the PV of one year's NOI growth capitalized at exit, net of selling costs.

(d) PV of the roof $= 400{,}000/1.085^3 = \$313,163$. A reserve of 3% of NOI (\$30,000 a year) does not fund a \$400,000 roof in Year 3. A buyer who assumes the reserve covers it overpays by about \$313,000, or 2.2% of value. Reserves are an average; known lumpy items belong in the DCF explicitly. Chapter 8 develops the reserve-versus-capex distinction.

### Solution 9.5
(a) $L = GDV(1-0.015)/1.15 - (52.0 + 9.5 + 4.0)$m, with non-land cost \$65.5m.

| Exit cap | GDV | Net value | Land | Per unit |
|---|---:|---:|---:|---:|
| 5.00% | 84,000,000 | 82,740,000 | 6,447,826 | 25,791 |
| 5.25% | 80,000,000 | 78,800,000 | 3,021,739 | 12,087 |
| 5.50% | 76,363,636 | 75,218,182 | −92,885 | −372 |

(b) Total cost at \$6.0m land $= \$71.5$m. Margin $= 78{,}800{,}000/71{,}500{,}000 - 1 = 10.2\%$, below 15%. Yield on cost $= 4{,}200{,}000/71{,}500{,}000 = 5.87\%$.

(c) Land is the residual claim: a 25 bp cap move changes GDV by about 5% but changes land value by more than 100%. Landowners anchored to recent land sales will not accept bids that reflect this, and developers cannot pay more without missing their margin, so land volume falls to near zero well before completed-building prices visibly adjust.

### Solution 9.6
(a)

| Comp | Factor | Adjusted \$/unit | Gross adj. |
|---|---:|---:|---:|
| X | 0.90 × 1.05 = 0.9450 | 292,950 | 15% |
| Y | 0.98 × 1.08 = 1.0584 | 280,476 | 10% |
| Z | 0.96 × 0.97 × 0.95 = 0.8846 | 256,546 | 12% |

Weights $\propto 1/0.15, 1/0.10, 1/0.12$. Weighted value = **\$275,826/unit**, or \$33,099,072 for 120 units.

(b) Without the time adjustment, X indicates $310{,}000 \times 1.05 = \$325{,}500$/unit, 11% above its time-adjusted figure and above every other comp. Time adjustments matter most after sharp market moves. That is also when recent sales are scarce, so analysts lean on older sales and are tempted to treat the most similar building as the best comp even when it traded in a different market.

### Solution 9.7
(a) NOI: 1,170,000; 1,193,400; 1,217,268; 1,241,613; 1,266,446; Year 6 1,291,775. Cash flow after 6% capex: 1,099,800; 1,121,796; 1,144,232; 1,167,117; 1,190,459. Gross reversion \$18,453,922; net \$18,084,844. Flows $[-18{,}180{,}000; \ldots; 1{,}190{,}459 + 18{,}084{,}844]$. **Property IRR = 6.19%.**

(b) Loan \$11,700,000. Loan constant at 6.00%/25 years = 7.73%. Annual debt service \$904,599. DSCR $= 1{,}170{,}000/904{,}599 = 1.29$x. Debt yield 10.0%. Balance after 60 payments \$10,522,054.

(c) Equity flows $[-6{,}480{,}000;\ 195{,}201;\ 217{,}197;\ 239{,}633;\ 262{,}517;\ 7{,}848{,}649]$. **Equity IRR = 6.59%.** Cash-on-cash Year 1 $= 195{,}201/6{,}480{,}000 = 3.01\%$, against an unlevered cash yield of $1{,}099{,}800/18{,}180{,}000 = 6.05\%$.

Leverage is **negative on current yield** (6.50% cap < 7.73% constant) and **barely positive on IRR** (6.19% vs a 6.00% rate, so +40 bp). As in Example 9.8, the equity is mostly buying variance. A 25 bp worse exit cap would turn leverage negative on IRR as well: at 7.25%, property IRR is 5.58% and equity IRR 4.95%.

### Solution 9.8
(a)

| Step | IRR | Increment |
|---|---:|---:|
| Income (flat NOI, exit 6.00%) | 6.00% | 6.00% |
| + market growth 2% | 8.00% | +2.00% |
| + lease-up (−\$1.2m Y2; +\$300k NOI from Y3) | 10.46% | +2.46% |
| + exit at 5.75% | 11.26% | +0.81% |

(b) Business plan with zero market growth: exit 6.00% → **8.50%**; exit 6.50% → **7.04%**.

(c) Model comment: "Of the 11.3% IRR, 2.5 points come from the lease-up plan the sponsor controls; 2.8 points come from market growth and cap compression it does not control. With no market growth and a 50 bp wider exit cap, the plan returns about 7.0%. The deck's attribution of the whole return to 'value-add' is incorrect."

Rubric (Level 4; 0–4 each):

| Dimension | Strong answer |
|---|---|
| Decomposition | Correct sequence and increments; notes order dependence |
| Stress | Computes plan-only IRRs; identifies 7.0% as the return on execution with adverse market |
| Lease-up risk | Asks for downtime, TI/LC and rent evidence; notes that the \$300k is itself a forecast |
| Incentives | Promote hurdles set above the market-beta return (for example, promote only above about 8–9%), or promote measured relative to a market index |
| Decision | Proceeds only if the plan-only return clears the committee's hurdle for the risk, or negotiates price |

### Solution 9.9
(a) Market value $= 1{,}200{,}000/0.06 = \$20.0$m (the 2022 appraisal of \$28.0m is 40% higher). Refinance: LTV \$12.0m; DSCR \$12.33m; debt yield \$13.33m. **Binding: LTV, \$12.0m.** Cash to refinance $= 17{,}000{,}000 + 1\% \times 12{,}000{,}000 - 12{,}000{,}000 = \$5{,}120{,}000$.

(b) Payoff price $= 17{,}000{,}000/0.98 = \$17{,}346{,}939$. At \$19.5m the owner nets $19{,}500{,}000 \times 0.98 - 17{,}000{,}000 = \$2{,}110{,}000$.

(c) The owner's alternatives are to write a \$5.12m check to refinance, sell, or negotiate an extension. Anchored to \$28m, the owner is likely to seek an extension first. Whether the lender grants one depends on the lender's own position: a lender with a 85% LTV loan (\$17m/\$20m) and a 7.1% debt yield may prefer an extension with a paydown and cash sweep to a foreclosure.

Rubric (Level 4; 0–4 each):

| Dimension | Strong answer |
|---|---|
| Numbers | Value, binding constraint, gap, payoff price, and net cash correct |
| Owner behavior | Predicts extension-seeking; explains that the \$28m anchor and the \$2.1m net proceeds frame the decision as a loss |
| Buyer strategy | Keeps the \$19.5m offer open with an expiry near maturity; shows the owner the refinance arithmetic; considers approaching the lender about a note purchase or a coordinated sale |
| Triggers | Raises the bid on evidence that NOI is recovering (rental-rate trends, occupancy) or on cap-rate evidence below 6%; withdraws on new supply nearby or falling street rates |
| Ethics and tone | Uses the refinance arithmetic as information the owner's lender will provide anyway, not as a threat |

### Solution 9.10
(a) Gross assets per unit $= 100/0.70 = \$142.86$; debt \$42.86.
Further decline in gross assets at a 20% office haircut $= 0.40(20\%) + 0.35(5\%) + 0.25(8\%) = 11.75\%$, or \$16.79/unit. True NAV $= \$83.21$. \$78 is a **6.3% discount** to it.
At 30%: $0.40(30\%) + 1.75\% + 2.00\% = 15.75\%$, or \$22.50. True NAV $= \$77.50$. \$78 is a **0.6% premium**.

(b) Break-even: $142.86 \times (0.40x + 0.0375) = 22 \Rightarrow x = 29.1\%$.

(c) Rubric (Level 5; there is no single correct answer). Score each dimension 0–4.

| Dimension | Strong answer includes |
|---|---|
| Arithmetic | Correct look-through; recognizes leverage magnifies asset haircuts into NAV (11.75% of gross assets is 16.8% of NAV) |
| Break-even logic | Notes that the break-even office haircut (29%) lies inside the plausible 20–30% range, so the decision depends on a number you do not know (Chapter 1, break-even reasoning) |
| Information requests | (1) Property-level office data: lease rollover, vacancy, and recent appraisal cap rates by asset; (2) the fund's debt maturities and covenants, since forced sales inside the fund would realize haircuts; (3) the redemption queue and gating terms, which set when you could exit and at what mark. Also fees and the queue's effect on future NAV |
| Listed-market comparison | Uses the REIT decline as a directional signal but does not map −35% REIT equity one-for-one onto unlevered private office (leverage, quality, composition, §9.9) |
| Decision | **Abstention is the best answer** unless the information narrows the office haircut below about 25%, or the price falls enough to give a margin of safety at a 30% haircut (about \$70 or lower provides roughly 10%). Buying at \$78 on the headline "22% discount to NAV" scores 0 on this dimension |

Answers that treat appraisal NAV as fair value, or that treat the REIT decline as the exact private decline, score 0–1 on the relevant dimension.

---

### Decision exercise (§9.10) — Rubric
See the rubric in the chapter, §9.10. A model answer: value range \$32–38m from the DCF, with the exit cap (7.75–8.75%) and the Tenant A re-leasing outcome as drivers. Bid \$34–35m with a \$2–3m earn-out payable if the Tenant A space is re-leased at or above an agreed net effective rent within 24 months. Conditions: leasing study and estoppels. The seller is unlikely to accept until a debt maturity, fund deadline, or Tenant A's departure resets the anchor. A pass with a re-engagement trigger at Tenant A's notice date is equally defensible.
