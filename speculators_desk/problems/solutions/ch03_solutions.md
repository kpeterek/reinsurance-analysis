# Chapter 3 Solutions

Numerical results are verified in `tests/test_ch03_examples.py`. Figures are rounded for display only.

---

### Solution 3.1
| Case | Loop | Sign | Gain set by | Lag |
|---|---|---|---|---|
| (a) | Reported returns → investor inflows → purchases → prices → reported returns | Amplifying | Investors' sensitivity of flows to past returns; appraisal smoothing (Chapter 2) makes it slower but more persistent | Appraisal and allocation cycle: quarters |
| (b) | Rents → permits → deliveries → rents | Stabilizing with a lag (cobweb, §3.4.10) | Supply elasticity times the rent response to supply ($g$) | Construction: about three years. Oscillates if $g$ is near or above 1 |
| (c) | Price → margin call and wider haircut → forced sale → price | Amplifying (margin and loss spirals) | Leverage, haircut sensitivity, market depth $b$ | Days |
| (d) | Losses → bank capital → lending → refinancing → defaults → losses | Amplifying | Capital ratio (losses removed ÷ capital ratio), share of borrowers needing refinancing | Quarters |
| (e) | Price → demand → price | Stabilizing, fast | Demand elasticity | Days to weeks |

Rubric: one point each for correct sign and gain driver; identifying (b) as stabilizing-but-oscillating and (c) as the fastest amplifying loop earns full credit.

### Solution 3.2
(a) $H = -0.693/-0.223 = 3.1$ years (exactly 3.106).
(b) $H = \ln 0.5/\ln 0.95 = 13.51$ quarters $= 3.38$ years. Annual persistence $= 0.95^4 = 0.8145$.
(c) The half-life is in quarters, because $\phi$ was estimated on quarterly data. 13.5 quarters is 3.4 years, not 13.5 years. The error overstates the reversion horizon fourfold.

### Solution 3.3
(a) Prior odds $= 0.3/0.7 = 0.4286$. Posterior odds $= 0.4286 \times 4 = 1.714$. $P = 1.714/2.714 = 63.2\%$.
(b) Odds $= 1.714 \times 0.5 = 0.857$. $P = 0.857/1.857 = 46.2\%$.
Comment: the second signal does not "cancel" the first; the net LR is $4 \times 0.5 = 2$, so the posterior is still well above the prior. Before relying on it, ask whether the two signals are independent. A seller who is well advised could both close fast *and* hold price, which makes the second signal less informative.

### Solution 3.4
(a) $m = \lambda \times 0.8 \times 110 \times 0.015 = 1.32\lambda$.
* $\lambda = 0.60$: $m = 0.792$; multiplier $= 1/0.208 = 4.81$.
* $\lambda = 0.70$: $m = 0.924$; multiplier $= 1/0.076 = 13.16$.

(b) $\lambda = 0.60$: total $= -4\% \times 4.81 = -19.2\%$. $\lambda = 0.70$: total $= -4\% \times 13.16 = -52.6\%$. After three rounds at $\lambda = 0.60$: $-4\% \times (1 - 0.792^3)/(1-0.792) = -4\% \times 2.419 = -9.68\%$. Only half the eventual move has happened after three rounds. Slow convergence is a property of gains near one.

(c) $\lambda_{max} = 1/(0.8 \times 110 \times 0.015) = 1/1.32 = 0.758$.

(d) At $m = 0.924$ the linear approximation is outside the range where it can be trusted. A 52.6% decline would change $\lambda$, $\theta$, and $\psi$ themselves: lenders would stop lending, and value buyers would enter. The answer is not a forecast. It says the market is close enough to the stability boundary that small changes in lender behavior produce very large changes in outcomes. It is a fragility indicator, and it argues for low leverage and for keeping dry powder for the bottom.

### Solution 3.5
(a) Expansion $1/(1-0.90) = 10$ quarters; contraction $1/(1-0.75) = 4$ quarters.
(b) $\pi_1 = 0.25/(0.10 + 0.25) = 0.714$; $\pi_2 = 0.286$.
(c) $[\mathbf P^2]_{12} = 0.90 \times 0.10 + 0.10 \times 0.75 = 0.165$.
(d) $[\mathbf P^8]_{12} = 0.277$, close to the long-run 0.286. After eight quarters, today's regime tells you little.
(e) $p_{22}^3 = 0.75^3 = 0.422$.
(f) For an 8-quarter maturity, the relevant number is (d): about a 28% chance of facing a refinancing in contraction, close to the long-run base rate. The 20-quarter loan does not avoid the risk. It replaces one refinancing draw with a later one at a similar probability, but it lowers the number of draws over a long hold and gives time to recover if a contraction comes early. You would also need the cost difference between the two loans, the prepayment terms, NOI under each regime, and the refinancing terms lenders offer in contraction (Example 3.9).

### Solution 3.6
(a) $V_u = 39.0$, $V_d = 22.5$, payout $= 0.07 \times 30 = 2.10$, $I_1 = 28.56$.
$q = (30 \times 1.04 - 2.10 - 22.5)/(39.0 - 22.5) = (31.2 - 24.6)/16.5 = 0.40$.
Payoffs: up $39.0 - 28.56 = 10.44$; down 0.
$W = 0.40 \times 10.44/1.04 = \$4.015$ million. Build-now NPV $= 30 - 28 = \$2.0$ million. Option premium $= \$2.015$ million. Wait.
Replication: $\Delta = 10.44/16.5 = 0.63273$; $B = -0.63273 \times (22.5 + 2.10)/1.04 = -14.966$; value $= 0.63273 \times 30 - 14.966 = 4.015$. ✓

(b) Raising $\delta$ lowers $q$ and therefore $W$. Setting $W = 2.0$: $q \times 10.44/1.04 = 2.0 \Rightarrow q = 0.19923$, and $q = (31.2 - 30\delta - 22.5)/16.5 \Rightarrow \delta = (8.7 - 16.5 \times 0.19923)/30 = 18.0\%$. At this volatility, waiting dominates for any realistic cash yield.

(c) $V_u = 33.0$, $V_d = 27.0$; $q = (31.2 - 2.1 - 27.0)/6.0 = 0.35$; up payoff $33.0 - 28.56 = 4.44$; $W = 0.35 \times 4.44/1.04 = \$1.494$ million $< \$2.0$ million. **Build now.** Lower uncertainty shrinks the upside the option captures, while the costs of waiting (forgone 7% yield, 2% cost inflation) are unchanged. The option to wait is valuable because of uncertainty, not in spite of it.

### Solution 3.7
(a) LTV $= 1{,}800/(50 \times 46) = 78.3\%$. No impact: $s = (1{,}800/46 - 37.5)/0.25 = (39.130 - 37.5)/0.25 = 6.52$ units.

(b) Solve $(46 - 0.2s)(37.5 + 0.25s) = 1{,}800$: $1{,}725 + 11.5s - 7.5s - 0.05s^2 = 1{,}800 \Rightarrow 0.05s^2 - 4s + 75 = 0 \Rightarrow s = [4 - \sqrt{16 - 15}]/0.1 = 30$ units. Price $= 46 - 6 = 40$. Equity $= 50 \times 40 - 1{,}800 = 200$ (from 500 before the sale).

(c) Marginal threshold $= 0.25 \times 46/(0.75 \times 50) = 0.3067$. Feasibility: $(11.5 + 37.5b)^2 = 4b(0.25)(1{,}800) = 1{,}800b$, i.e. $1{,}406.25b^2 - 937.5b + 132.25 = 0$. The smaller root is $b^\dagger = 0.2027$.

(d) $b = 0.20$ sits just below $b^\dagger$. A cure exists, but it requires selling 60% of the position and costs 60% of the remaining equity. A small error in the estimate of $b$ separates a painful cure from full liquidation. A position whose cure depends on $b$ being 0.200 rather than 0.203 is already in the spiral zone. The time to deleverage was before the shock.

### Solution 3.8
(a) Alone: $45/(0.15 \times 25) = 12$ days. All eight: $300/3.75 = 80$ days.
(b) $25 \times 0.15 \times 10/8 = \$4.69$ million.
(c) (i) Alone: $30/3.75 = 8$ days. Yes, within 21 days. (ii) One-eighth of capacity: $30/(3.75/8) = 64$ days. No.
(d) Size so that the *crowded* exit of a plausible redemption fits inside the notice period. With a one-eighth share over 21 trading days, the exitable amount is $25 \times 0.15 \times 21/8 = \$9.8$ million. That is far below \$45 million. A defensible answer cuts the position toward \$10–20 million, or keeps it and holds offsetting liquidity (cash or liquid hedges) for the shortfall.

Rubric: (1) computes both alone and crowded exit times; (2) links position size to the fund's own liability terms; (3) recognizes that crowding estimates from 13F filings are lagged and incomplete; (4) states what would change the answer: longer notice or gates, lower overlap, a higher ADV, or evidence that the other holders have longer-dated capital; (5) does not assume a single correct size.

### Solution 3.9
(a) Value $= 1.9/0.06 = \$31.67$ million; LTV $= 20/31.67 = 63.2\%$; DSCR $= 1.9/(0.0375 \times 20) = 2.53$x.
(b) Value $= 1.9/0.075 = \$25.33$ million. Loan constant (7.0%, 25 years, monthly) $= 0.084814$.
* LTV: $0.60 \times 25.33 = \$15.20$ million.
* DSCR: $1.9/1.40/0.084814 = \$16.00$ million.
* Debt yield: $1.9/0.10 = \$19.00$ million.
LTV binds at \$15.20 million. Gap $= 20.0 - 15.2 = \$4.80$ million, 24.0% of the old balance.
(c) Defaults: $0.5 \times 800 = \$400$ million; loss $= 0.20 \times 400 = \$80$ million; capacity reduction $= 80/0.09 = \$889$ million.
(d) Rubric. The strongest answers argue that:
1. Opportunity concentrates where bank capital is scarcest relative to maturing CRE, not where the first-order rate shock is largest.
2. Timing follows loss recognition. Loan sales and foreclosures come after extensions run out, typically several quarters after the rate rise.
3. The best purchases are performing-but-unrefinanceable loans and assets whose owners cannot fund the gap. Price is set by the shortage of financed bidders.
4. Evidence that the chain is *not* operating: banks extending rather than selling, private credit replacing bank lending (the nonbank channel of §3.9), sponsors funding gaps at high rates, or stable transaction volumes.
5. They state what they do not know: the actual loss severities, and whether regulators will press for recognition.

### Solution 3.10
(a) Buffer $d^* = 1 - \lambda_0/\lambda^*$. At 50%: $1 - 0.50/0.65 = 23.1\%$. At 60%: $1 - 0.60/0.65 = 7.7\%$.

(b) Considerations:
* *Collateral loop:* other owners' upsizes raise $\theta$ on the way up; on the way down your 60% facility puts you among the borrowers forced to repay. Unknown share at the limit means unknown $\theta_{down}$.
* *Negative supply loop:* metro A industrial vacancy rising from new deliveries is the lagged supply response arriving.
* *Lender behavior:* one lender cutting hotel LTV is a direct cut to $\lambda$ for the market's marginal financing.
* *Regime:* rising vacancy and a lender cut are weak evidence of a regime turn; flat RevPAR and rising group pace point the other way. The LRs are unknown and the signals are not clearly independent.
* *Crowding:* three other clients upsized with the same lender; their exits and yours would coincide.
* *Comparable sale at a low cap rate:* one data point, possibly from a buyer in the same loop; weak evidence about value.

(c) Decision rubric. The best answer, given the stated information, is to **defer or decline**. The covenant buffer at 60% (7.7%) is smaller than plausible appraisal moves in either metro. The evidence for and against a turn cannot be weighed without LRs you do not have. The use of proceeds has not been specified, so there is no deal to set against the risk-matched hurdle. A partial upsize (to 55%, buffer $1 - 0.55/0.65 = 15.4\%$) is acceptable *if* it is tied to a specific acquisition that clears the hurdle and is not in the same metros. Information that would change the decision: the share of metro collateral at covenant limits (lender surveys, CMBS data), the supply pipeline relative to absorption, lender terms across several banks, and a renegotiated covenant (for example, 70% or an equity-cure right). Credit is given for (1) computing both buffers; (2) naming the loops and the crowding; (3) separating evidence from assumptions; (4) making abstention or deferral an explicit, reasoned option; (5) naming the information to buy and how.
