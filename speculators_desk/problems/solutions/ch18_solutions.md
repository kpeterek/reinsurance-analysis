# Chapter 18 Solutions

Numerical results are verified in `tests/test_ch18_examples.py`. Figures are rounded for display only. Library: `sdesk.markets`, `sdesk.x_derivatives`, `sdesk.x_capital_structure`.

---

### Solution 18.1

| | Instrument | Convexity | Main residual risk |
|---|---|---|---|
| (a) | Pay-fixed interest-rate swap | None (linear); slight convexity from the annuity | Counterparty in both directions; **breakage** on early exit if rates fall (Example 18.7) |
| (b) | Interest-rate cap | Long | Premium paid upfront; cap-provider counterparty risk, largest when rates are high; replacement cost if the cap is shorter than the loan |
| (c) | Futures | None (linear) | **Basis** (REITs respond to rates and property factors the index does not capture) and **margin** (variation margin in cash on a rally) (Example 18.6) |
| (d) | FX forward | None (linear) | Counterparty; **quantity basis**: if the sale price or timing changes, the forward is over- or under-hedged and becomes a speculation |
| (e) | Long puts | Long | Theta (premium decay); skew makes OTM puts expensive (Example 18.5) |
| (f) | Short puts | **Short** | Gap and tail risk; margin calls in a decline; its premium income is the counterpart of (e)'s cost (§18.9) |

The common thread is that linear hedges (a, c, d) cost nothing upfront but carry contingent cash needs or counterparty exposure. Option hedges (b, e) cost a known premium and cap the hedger's loss.

### Solution 18.2
(a) $C - P = S - Ke^{-rT} = 100 - 100e^{-0.05} = 100 - 95.123 = 4.877$. Mental: $e^{-0.05} \approx 1 - 0.05 + 0.00125 = 0.95125$.
(b) $0.16/\sqrt{252} = 1.008\%$. Mental: $\sqrt{252} \approx \sqrt{256} = 16$, so 16 vol ≈ 1% a day.
(c) $F = 100e^{(0.05-0.02)} = 100e^{0.03} = 103.05$. Mental: $e^{0.03} \approx 1.0305$.

### Solution 18.3
Per share: $\Delta\,\delta S + \tfrac12\Gamma(\delta S)^2 = 0.55\times4 + 0.5\times0.03\times16 = 2.20 + 0.24 = 2.44$.
Position: $10\times100 = 1{,}000$ shares-equivalent, so P&L ≈ \$2,440. The gamma term contributes \$240, about 10%. It would be larger for a larger move. Theta (ignored) would offset part of it.

### Solution 18.4
(a) $d_1 = [\ln(50/52) + (0.045 + 0.045)\times0.5]/(0.30\sqrt{0.5}) = (-0.039221 + 0.045)/0.212132 = 0.027244$. $d_2 = d_1 - 0.212132 = -0.184888$. $N(d_1) = 0.510867$, $N(d_2) = 0.426658$.
Call $= 50\times0.510867 - 52e^{-0.0225}\times0.426658 = 25.5434 - 21.6926 = 3.8508$.
Put $= 4.6938$.

(b) $C - P = 3.8508 - 4.6938 = -0.8431$. $S - Ke^{-rT} = 50 - 50.8431 = -0.8431$. Gap = 0. ✓

(c) Call delta 0.5109; put delta −0.4891 (they differ by exactly 1 since $q = 0$). Gamma 0.03760. Vega 0.1410 per vol point. Theta per day: call −0.01426, put −0.00799.

(d) Both share the time-decay term $-S\phi(d_1)\sigma/(2\sqrt T)$. The call has an additional $-rKe^{-rT}N(d_2)$: the call holder benefits from paying the strike later, and that benefit shrinks as time passes. The put has $+rKe^{-rT}N(-d_2)$: the put holder receives the strike later than she would like, and that cost shrinks as time passes. With positive rates the call's theta is therefore more negative.

### Solution 18.5
(a) Bisection: $\sigma_{impl} = 23.24\%$.
(b) Vega at 23.24% vol: 15.793 per 1.00 of vol. Expected P&L ≈ $\nu(\sigma_r - \sigma_i) = 15.793\times(0.22 - 0.23242) = -0.1961$ per unit. For 50 contracts × 100 = 5,000 units: about −\$981.
(c) (i) **Path dependency.** P&L is gamma-weighted: if most of the 22% realized variance occurs while the stock is far from the strike, the P&L is worse than −0.196; if it occurs near the strike late in the option's life, better (Example 18.4). (ii) **Discrete hedging noise** with a standard deviation that falls only as $1/\sqrt n$. (iii) Transaction costs on re-hedging. (iv) The vega approximation itself, which assumes $\Gamma S^2$ is constant. Any two suffice.

### Solution 18.6
(a) Annuity $A = 0.9800 + 0.9420 + 0.9050 = 2.8270$.
Fixed leg $= 30{,}000{,}000\times0.035\times2.8270 = \$2{,}968{,}350$.
Floating leg (next coupon fixed): $N(1 + 0.042\times1.0)P(0.5) - N\,P(2.5) = 30{,}000{,}000\times1.042\times0.98 - 30{,}000{,}000\times0.905 = 30{,}634{,}800 - 27{,}150{,}000 = \$3{,}484{,}800$.
Value to pay-fixed $= 3{,}484{,}800 - 2{,}968{,}350 = +\$516{,}450$.

(b) The borrower **receives** about \$516,450, less the dealer's spread. The value is positive because every floating rate the borrower will receive exceeds the 3.50% it pays: the known fixing is 4.20%, and the forward rates for the later periods are $0.9800/0.9420 - 1 = 4.03\%$ and $0.9420/0.9050 - 1 = 4.09\%$. The floating leg uses the known fixing for the first period and the "par at the next reset" argument for the rest.

### Solution 18.7
Using `xc.cap_premium(25e6, K, 0.038, vol, 2)`. Seven caplets, at fixings 0.25 to 1.75 years. Annuity (all eight periods) = 1.9171.

| Case | Premium | % notional | Annual bp |
|---|---|---|---|
| (a) $K = 4.00\%$, 0.90% | \$106,007 | 0.424% | 22.1 |
| (b) $K = 4.00\%$, 1.20% | \$152,792 | 0.611% | 31.9 |
| (c) $K = 5.00\%$, 0.90% | \$17,578 | 0.070% | 3.7 |

(d) Extra equity $= 152{,}792 - 106{,}007 = \$46{,}785$, a 44% increase in the cap budget for a 30 bp rise in vol. The cap is long vega. A sponsor who budgets the cap at a model vol rather than at a dealer quote obtained close to closing is carrying an unhedged vega position. The cost is small relative to the loan but certain, and it falls at closing when cash is tight.

### Solution 18.8
(a) Using `xd.put_roll_cost`:
* (i) 95% strike, 20% vol: premium 1.6978 per 100; annual cost 6.791%.
* (ii) 80% strike, 28% vol: premium 0.2633 per 100; annual cost 1.053%.

(b) $(1 - 0.06791)^{10} = 0.495$. Program (i) halves the portfolio's terminal value relative to unhedged over ten years if it never pays out.

(c) A 35% fall within a quarter:
* (i) pays $95 - 65 = 30$% of the portfolio. Break-even frequency $= 6.791/30 = 0.226$ a year (once every 4.4 years).
* (ii) pays $80 - 65 = 15$%. Break-even frequency $= 1.053/15 = 0.0702$ a year (once every 14.2 years).

(d) **Rubric.**

| Element | Points | Full credit requires |
|---|---|---|
| Costs | 2 | (a)–(c) correct; the 50% ten-year drag of program (i) stated |
| Forced action | 3 | Recognizes that an unlevered endowment with no capital calls has **no forced sale** in a crash. The value of insurance comes from avoiding forced actions, so the case for either program is weak. The spending rule (5% of a trailing average) may create pressure, which should be quantified, not assumed |
| Alternatives | 2 | Compares with lowering equity exposure, holding a liquidity reserve, or (ii) as cheap disaster insurance if the governance cost of a crash (trustee pressure to sell at the bottom) is real |
| Recommendation | 2 | Neither, or (ii) only, with a stated budget cap (e.g. ≤1% a year) and a stated purpose. Program (i) is defensible only for an investor with a large crash-state liability |
| What would change it | 1 | Leverage, unfunded commitments to private funds (capital calls in a crash), a liability-matching mandate, or materially lower implied vol at the strike |

Competing view: a trustee may argue that program (i) prevents behavioral selling at the bottom. Answer: that is a governance problem with a cheaper governance solution (a written rebalancing policy). If it cannot be solved that way, price it explicitly as the cost of the insurance.

### Solution 18.9
(a) Using `xd.merton_claims(V, 30e6, 2, 0.04, σ)`. Riskless PV of the balloon $= 30{,}000{,}000e^{-0.08} = \$27{,}693{,}490$.

| $V$ | $\sigma$ | Equity | Put | Debt | Spread | PD (RN) |
|---|---|---|---|---|---|---|
| \$30.0m | 15% | 3,760,436 | 1,453,926 | 26,239,564 | 270 bp | 39.3% |
| \$30.0m | 30% | 6,083,954 | 3,777,444 | 23,916,046 | 733 bp | 50.9% |
| \$36.0m | 15% | 8,653,607 | 347,097 | 27,346,393 | 63 bp | 12.9% |
| \$36.0m | 30% | 10,472,955 | 2,166,445 | 25,527,045 | 407 bp | 34.2% |

(b) At \$30.0m: $6{,}083{,}954 - 3{,}760{,}436 = \$2{,}323{,}518$ moves from lender to sponsor.

(c) At \$36.0m the transfer is $10{,}472{,}955 - 8{,}653{,}607 = \$1{,}819{,}348$, smaller. Vega is highest near the money. With \$6 million of cushion, the put is further out of the money, and higher vol helps the sponsor less. The sponsor's incentive to take risk is strongest when the loan is underwater or nearly so, which is when lender consent matters most.

(d) **Rubric.**

| Element | Full credit requires |
|---|---|
| Quantification | The \$2.3 million transfer at \$30m is stated as the economic value of consent |
| Ask | A partial paydown, new sponsor equity into a reserve, a higher spread or exit fee roughly sized to the transfer, tighter cash management, a completion guarantee for the conversion capex, or springing recourse if the conversion fails to meet milestones |
| Model caveat | The Merton model ignores coupons, covenants and early foreclosure (§18.7). Volatility estimates for a single hotel are judgments. Use the figure as an order of magnitude |
| Alternative | Consider whether the conversion raises expected value. If it does, the lender can share in the gain (e.g. through an exit fee) rather than block it |

### Solution 18.10
(a) Put price $= \text{BS}_{put}(100, 90, 1/12, 0.04, 0.20, q = 0.015) = 0.0668$ per 100 of notional. At 5× notional: $5\times0.0668\% = 0.334\%$ of NAV per month. Compounded: $(1.00334)^{12} - 1 = 4.08\%$ a year, plus interest on the collateral.

(b) No. 1% a month is three times the reconstructed income. To earn it, at least one of the following must hold: (i) notional of about $1\%/0.0668\% = 15.0\times$ NAV; (ii) strikes much closer to the money; (iii) selling at implied vols well above 20%, which happens after a scare, when tail risk is also higher; (iv) other strategies or undisclosed risks. Each alternative raises the tail loss.

(c) A 25% fall with puts struck at 90 loses $90 - 75 = 15$ per 100 of notional, offset by the premium.
* At 5×: $5\times15\% - 0.334\% = 74.67\%$ of NAV.
* At 15× (implied by 1% a month): $15\times15\% - 1\% = 224\%$ of NAV. The fund is wiped out, and the excess loss falls on its prime broker or clearing firm (counterparty risk for others).

A 24-month record cannot distinguish these structures. The probability of no month with a large decline over two years is high under almost any plausible distribution of index returns [INFERENCE], so the track record carries little information about the tail.

(d) **Rubric. Abstention is the expected answer.**

| Element | Points | Full credit requires |
|---|---|---|
| Reconstruction | 2 | (a) computed; the 3× inconsistency in (b) identified |
| Tail | 2 | (c) computed at both leverages; loss beyond 100% recognized as a counterparty problem |
| Evidence quality | 2 | A 24-month record of short convexity and a Sharpe above 3 recognized as uninformative about the tail (§18.9); one year of audited data noted |
| Decision | 3 | **Decline** pending information, or invest only an amount whose loss in a −25% month (assume a total loss) is tolerable, e.g. under 1–2% of total capital |
| Information that changes it | 1 | Full position-level history; maximum notional and strike distance by month; margin terms and prime-broker agreements; a stress-test report for −20% and −30% months and a VIX shock; the 2018 and 2020 behavior of the strategy if it existed then; redemption terms |

A candidate who invests a full allocation on the strength of the Sharpe ratio fails this problem regardless of the arithmetic.
