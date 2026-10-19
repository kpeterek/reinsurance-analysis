# Chapter 1 Solutions

Numerical results are verified in `tests/test_ch01_examples.py`. Figures are rounded for display only.

---

### Solution 1.1
(a) **Investment and hedging.** The fund bears little credit risk. Holding to maturity against a matching liability *reduces* its interest-rate exposure, so this is a hedge in asset-liability terms. If the fund had no liability, the same purchase would be an investment that bears interest-rate risk for the term premium.

(b) **Speculation.** The return depends on a change in expected land use. That depends on uncertain public funding, not on cash flow. The developer is paid for bearing entitlement and timing risk, in the form of a lower land price than an approved interchange would command. Treat it as a real option (Chapter 13, Case I).

(c) **Arbitrage**, *if* the contracts are fungible (same clearing house, so positions offset) and both fills are simultaneous. If execution is sequential, it carries leg risk. If clearing differs, it carries basis and margin risk and becomes relative-value speculation.

(d) **Hedging.** The owner pays a premium to transfer rate risk to the cap seller, who is the speculator or dealer.

(e) **Gambling.** State lotteries pay out less than they take in. EV is negative and there is no risk-transfer function.

(f) **Speculation.** The underlying exposure is gone, so the cap is now a naked long position on short rates (a long call on rates). It may still be worth holding, but it must be judged as a speculation (§1.7, item 1).

### Solution 1.2
(a) Y's decision was bad regardless of the outcome because: (i) it extrapolated a nine-year trend without asking what could break it; (ii) it did not consider any low-probability, high-severity scenarios; (iii) 75% LTV with no reserves leaves very little capacity to survive *any* revenue shock, and hotels have high operating leverage (Chapter 11); (iv) no invalidation or liquidity plan was stated. X's memo specified a tail scenario and sized leverage and reserves to survive it.

(b) No. One draw does not identify skill. To compare, you need the ex-ante distributions both analysts wrote down, and ideally many decisions, to assess calibration (Chapter 20). A higher realized IRR from a riskier structure is the expected *mean* reward for taking more risk. It is not evidence of better judgment unless the risk-adjusted, survival-weighted comparison also favors it.

### Solution 1.3
(a) Arithmetic: $0.5(40\%) + 0.5(-30\%) = +5\%$.
(b) One win and one loss: $1.4 \times 0.7 = 0.98$ over two periods. Per period: $\sqrt{0.98} - 1 \approx -1.0\%$ (exactly −1.005%). Mental shortcut: $\sqrt{1-x} \approx 1 - x/2$, so $-2\%/2 = -1\%$.

### Solution 1.4
$p^* = G/(G+L) = 1.2/(1.2 + 2.0) = 37.5\%$. The decision is **not** robust. The 25–45% estimate straddles 37.5%, so EV can be positive or negative within your range. Before bidding, gather information that narrows the foreclosure probability, such as borrower liquidity, guarantor strength, or the property's current DSCR. Alternatively, restructure the bid to lower $L$, for example with a lower price or a discounted payoff option.

### Solution 1.5
(a) Basis $= 5{,}200{,}000 \times 1.02 = \$5{,}304{,}000$.

(b) Net sale = gross × 0.97: Good 5,820,000; Base 5,238,000; Bad 4,171,000.

| Scenario | Profit = NOI1 + NOI2 + net sale − basis | IRR |
|---|---|---|
| Good | 420,000 + 450,000 + 5,820,000 − 5,304,000 = **1,386,000** | 12.76% |
| Base | 400,000 + 410,000 + 5,238,000 − 5,304,000 = **744,000** | 7.03% |
| Bad | 330,000 + 300,000 + 4,171,000 − 5,304,000 = **−503,000** | −5.02% |

(c) $E[\text{Profit}] = 0.5(1{,}386{,}000) + 0.35(744{,}000) + 0.15(-503{,}000) = 693{,}000 + 260{,}400 - 75{,}450 = \$877{,}950$. Standard deviation = \$649,146. P(loss) = 15%.

(d) Expected IRR $= 0.5(12.76\%) + 0.35(7.03\%) + 0.15(-5.02\%) = 8.09\%$.
Expected flows: Y1 $= 0.5(420{,}000) + 0.35(400{,}000) + 0.15(330{,}000) = 399{,}500$. Y2 $= E[NOI_2] + E[\text{net sale}] = 413{,}500 + 5{,}368{,}950 = 5{,}782{,}450$. The IRR of $[-5{,}304{,}000;\ 399{,}500;\ 5{,}782{,}450]$ is **8.25%**.

(e) $\bar G = (50 \times 1{,}386{,}000 + 35 \times 744{,}000)/85 = \$1{,}121{,}647$. $q^* = 1{,}121{,}647/(1{,}121{,}647 + 503{,}000) = 69.0\%$.

Interpretation: the expected return of about 8% unlevered over two years is thin relative to the risk, and a Bad outcome loses close to 10% of capital. A buyer should ask whether a two-year hotel hold at 8% beats the risk-free rate by enough to compensate for illiquidity and dispersion (Case F).

### Solution 1.6
(a) $E[N_\tau] = 5{,}100{,}000 \times 0.97 - 90{,}000 = \$4{,}857{,}000$; $N_0 = \$4{,}600{,}000$; $\tau = 8/12$.
$r_{imm} = (4{,}857{,}000/4{,}600{,}000)^{1.5} - 1 = (1.05587)^{1.5} - 1 = 8.50\%$.
Before calling this a bargain, compare 8.5% with the owner's cost of capital and the risk that the patient sale fails.

(b) $N_1 = 8{,}480{,}000$ and $N_2 = 7{,}898{,}000$. Solving by bisection gives $r = 15.72\%$, against the approximation's 15.62%. The error of about 0.1 percentage point does not affect the decision. The approximation slightly understates the rate because discounting is convex in time (Jensen's inequality).

### Solution 1.7
Quoted spread 0.12, so half-spread $h = 0.06$.
(a) $E[\Pi] = 0.06 - 0.15 \times 0.60 = -0.03$ points.
(b) $h^* = 0.15 \times 0.60 = 0.09$, so the competitive quoted spread is 0.18.
(c) $h^* = 0.30 \times 0.60 = 0.18$, a quoted spread of 0.36. Spreads should widen, and depth should thin, ahead of information events. Uninformed traders who must trade around releases pay more. Schedule non-urgent execution away from releases.

### Solution 1.8
Basis $= 3{,}200{,}000 \times 1.015 = \$3{,}248{,}000$.
(a) Close: $3{,}450{,}000 \times 0.98 - 3{,}248{,}000 = 3{,}381{,}000 - 3{,}248{,}000 = +\$133{,}000$.
Walk: $3{,}150{,}000 \times 0.98 + 60{,}000 - 3{,}248{,}000 = 3{,}087{,}000 + 60{,}000 - 3{,}248{,}000 = -\$101{,}000$.
$EV = 0.65(133{,}000) + 0.35(-101{,}000) = 86{,}450 - 35{,}350 = \$51{,}100$.
(b) $\pi^* = 101{,}000/(133{,}000 + 101{,}000) = 43.2\%$.
(c) A \$101,000 hard deposit makes the walk outcome break even, and EV rises to \$86,450. Without the deposit, EV is \$51,100 on \$3.25 million of capital, and the downside depends on a fallback price you have estimated loosely. A 2–3% hard deposit at signing is a standard protection. If the exchange buyer will not post one, their commitment is weak, which is itself evidence for revising $\pi$ downward (a Bayesian update; Chapter 3). A reasonable decision is to proceed only with a hard deposit, or to pass.

### Solution 1.9
Equity return $r_E = (r_A - \lambda \cdot 0.05)/(1-\lambda)$, floored at −100%.

| LTV | +16% state | −4% state | −25% state | $E[r_E]$ (floored) | $E[\ln(1+r_E)]$ |
|---|---|---|---|---|---|
| 0% | 16.00% | −4.00% | −25.00% | 5.90% | 0.04804 |
| 50% | 27.00% | −13.00% | −55.00% | 6.80% | 0.02178 |
| 65% | 36.43% | −20.71% | −80.71% | 7.57% | −0.04784 |
| 75% | 49.00% | −31.00% | −115% → −100% | 10.10% | −∞ |
| 85% | 78.33% | −55.00% | −195% → −100% | 20.50% | −∞ |

(c) At 75% and 85% LTV the bad state wipes out equity, so $\ln(0) = -\infty$. Any strategy repeated at this leverage is eventually ruined with probability one. Even at 65%, expected log growth is negative: the equity is expected to compound *downward* despite a higher arithmetic mean.

(d) The sponsor's claim is arithmetically true and economically misleading. The rising arithmetic mean at high LTV comes from the limited-liability floor: losses beyond 100% are shifted to the lender. Investors who make repeated decisions, or who cannot replace lost capital, care about growth and survival. A lender who prices this correctly will charge more for 85% LTV or refuse it. The sponsor's incentive (fees plus a promote that is an option on the upside) differs from the investor's. See Chapter 10 on incentives.

### Solution 1.10 — Rubric (Level 5; there is no single correct answer)

Score each dimension 0–4. A strong answer scores at least 3 on every dimension.

| Dimension | Strong answer includes |
|---|---|
| Value range | Capitalizes a *normalized* NOI, not the trailing or peak figure. Recognizes the \$2.6m-to-\$1.9m decline may be partly new supply (persistent) and partly cyclical. Uses a cap-rate range appropriate to full-service leisure hotels, stated as an assumption. For example, \$1.9m / 9.5% = \$20.0m and \$1.9m / 10.5% = \$18.1m before PIP. Deducts an estimated PIP and labels it an estimate. |
| Ranked unknowns | (1) PIP scope and cost at license renewal, since 30 months is near enough to be capitalized into price; (2) the competitor's ramp-up and its effect on the subject's penetration indices; (3) financing availability and terms. A strong answer explains why each moves value. |
| 10-day plan | Request the PIP letter or brand estimate, the STR reports for 24 months, and monthly P&Ls. Obtain two lender quotes. Walk the competitor. Do not spend on a full appraisal yet. |
| Bid and conditions | If a bid is made, it is conditional on PIP information, with a stated walk-away price. For example, "\$17.0–17.5m subject to PIP ≤ \$X; withdraw if PIP > \$Y or if the T-3 RevPAR index has fallen below Z." |
| Seller motivation | A partnership dissolution creates a deadline, which supports a liquidity discount. But the decline in NOI and the coming PIP mean part of the discount is fundamental. Do not count both as upside. |
| Abstention | Recognizes that passing is defensible if the PIP cannot be learned in 10 days and financing is unavailable. |

Answers that bid the asking price, capitalize peak NOI, ignore the license expiry, or present a single IRR without scenarios score 0–1 on the relevant dimension.

---

### Decision exercise (§1.10) — Rubric
| Element | Full credit (4) | Partial (2) | None (0) |
|---|---|---|---|
| Classification | A = investment, with a speculative appreciation component at 60% LTV; B = liquidity-provision speculation with information risk; C = speculation on completion | Two of three correct | "C is arbitrage" |
| Opportunity B | Bid conditional on PIP; computes a max price under a \$1.5m PIP; uses break-even logic | Mentions PIP qualitatively | Bids \$7.8m firm with waived diligence |
| Opportunity C | Requires a hard deposit, restructures, or passes; computes $\pi^*$ | Notes risk without numbers | Treats as riskless |
| Opportunity A | Decomposes levered return; notes negative leverage on current yield; compares to Treasuries | Notes leverage only | Reports a single IRR |
| Abstention and invalidation | States what is declined and why; gives invalidation triggers for each position | Partial | Absent |
