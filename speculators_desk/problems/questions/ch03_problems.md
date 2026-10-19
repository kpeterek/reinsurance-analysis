# Chapter 3 Problems — The Speculator's Mental Models

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch03_solutions.md`. Numerical answers are verified in `tests/test_ch03_examples.py`.
All facts are hypothetical [HYPOTHESIS] unless cited.

---

### Problem 3.1 (Level 1) — Classify the loop
For each situation, name the feedback loop, give its sign (amplifying or stabilizing), name the parameter that sets its gain, and state the lag.

(a) Open-end core real estate funds report appraisal-based returns. Investors allocate more to the funds after several quarters of good returns, and the funds buy more property.
(b) Multifamily rents in a Sun Belt metro rise 12% in a year. Developers file permits. Deliveries arrive three years later.
(c) A mortgage REIT finances CMBS on repo with daily mark-to-market and haircuts that widen when prices fall.
(d) A bank with concentrated CRE exposure takes losses, cuts CRE lending, and borrowers in its markets cannot refinance.
(e) A hotel owner raises ADR, occupancy falls, and the owner cuts ADR back.

### Problem 3.2 (Level 2) — Half-lives in your head
(a) An annual AR(1) has $\phi = 0.80$. What is the half-life? (Use $\ln 0.5 \approx -0.693$ and $\ln 0.8 \approx -0.223$.)
(b) A quarterly AR(1) has $\phi = 0.95$. What is the half-life in quarters and in years? What is the equivalent annual persistence?
(c) A colleague estimates a quarterly $\phi$ of 0.95 and reports a half-life of "13.5 years". What went wrong?

### Problem 3.3 (Level 2) — Two updates
Your prior that a seller is distressed (must sell within six months) is 30%. (a) The seller agrees to a 30-day close without a financing contingency. You judge this four times as likely if the seller is distressed (LR = 4). What is your posterior? (b) The seller then rejects a price 3% below ask. You judge this half as likely if distressed (LR = 0.5). What is your posterior now?

### Problem 3.4 (Level 3) — The loop near the boundary
In a metro office market, pledged collateral is $C = 110$ (\$ billions), owners draw $\theta = 0.8$ of lost or gained capacity, and $\psi = 0.015$ per \$ billion.
(a) Compute the loop gain and multiplier at $\lambda = 0.60$ and at $\lambda = 0.70$.
(b) A −4% fundamental shock hits. What is the total price change under each $\lambda$? What is the cumulative change after the first three rounds at $\lambda = 0.60$?
(c) What is the maximum $\lambda$ for stability?
(d) Why should you not trust the $\lambda = 0.70$ answer as a forecast? What does it tell you instead?

### Problem 3.5 (Level 3) — Regimes and the loan maturity
A quarterly two-state model has $p_{11} = 0.90$ (expansion) and $p_{22} = 0.75$ (contraction).
(a) Expected durations of each regime.
(b) Long-run probabilities.
(c) The probability of being in contraction two quarters from now, given expansion today.
(d) The probability of being in contraction eight quarters from now, given expansion today. Compare it with the long-run probability.
(e) A contraction has just begun. What is the probability that it lasts at least four quarters in total (this quarter plus at least three more)?
(f) You are choosing between a loan that matures in 8 quarters and one that matures in 20 quarters, on a hotel bought today in expansion. Which number above matters for that choice, and what else would you need?

### Problem 3.6 (Level 3) — The option to wait, two volatilities
A pad site supports a building worth $V_0 = \$30$ million today. Construction cost is \$28 million now or 2% more next year. The completed building yields 7% cash on $V_0$. The risk-free rate is 4%.
(a) With $u = 1.30$ and $d = 0.75$: compute $q$, the wait value, the option premium, and verify by replication.
(b) Find the cash yield $\delta$ at which building now and waiting have equal value (to 0.1%).
(c) Repeat (a) with $u = 1.10$ and $d = 0.90$. Should you build now or wait? Explain the difference from (a).

### Problem 3.7 (Level 3) — Near the spiral
A fund holds $Q_0 = 50$ units. After a shock the price is $P_1 = 46$. Debt is $D = 1{,}800$. The covenant is LTV ≤ 75%.
(a) Current LTV and the units to sell with no price impact.
(b) With $b = 0.20$, solve for units sold, post-sale price, and remaining equity.
(c) Compute the marginal impact threshold and the feasibility threshold $b^\dagger$.
(d) Interpret (b) in light of (c).

### Problem 3.8 (Level 4) — Crowded exit
You manage a \$200 million long/short real estate securities fund with monthly liquidity and 30 days' redemption notice. You hold \$45 million of one office REIT that trades \$25 million a day. You will not exceed 15% of volume. From 13F filings, you estimate that eight funds with similar strategies (including yours) hold \$300 million of the stock.
(a) Days to exit alone and when all eight exit at once.
(b) The largest position you could exit in 10 trading days if you receive one-eighth of exit capacity.
(c) A 15% redemption request (\$30 million) arrives. Treat the 30-day notice period as 21 trading days. Can you raise \$30 million from this position alone within the notice period, (i) exiting alone and (ii) with one-eighth of exit capacity?
(d) Recommend a position size and justify it. What would change your answer?

### Problem 3.9 (Level 4) — Second-order consequences in hotels
A \$20.0 million hotel loan was made interest-only at 3.75% when NOI was \$1.9 million and the cap rate 6.0%. At maturity the market lends at 7.0% on 25-year amortization with a 60% LTV maximum, 1.40x DSCR minimum, and 10% debt-yield minimum. The cap rate is now 7.5%. NOI is unchanged.
(a) Original value, LTV, and DSCR.
(b) New value, maximum loan under each test, the binding test, and the refinancing gap as a share of the old balance.
(c) A bank holds \$800 million of similar maturing loans. Half the balance refinances with sponsor equity. The other half defaults, with 20% loss severity. The bank holds capital of 9% of loans. What is the reduction in lending capacity?
(d) You run an opportunistic credit fund. Using the chain, say when and where you expect to find the best purchases, and what evidence would tell you the chain is *not* operating.

### Problem 3.10 (Level 5) — The upsize, with conflicting evidence
A fund owns \$500 million of industrial and hotel assets in two metros, financed at 50% LTV with a 65% LTV maintenance covenant. The lender offers to raise the facility to 60% LTV. Information:
* Industrial rents in metro A are up 9% this year; vacancy is rising from 3% to 5% as new supply delivers.
* Hotel RevPAR in metro B is flat; group pace is up; a competitor has just closed on two hotels at cap rates you think are 75 bp too low.
* Your lender says three other clients have taken similar upsizes. Another lender has just cut its maximum LTV on hotels by 5 points.
* You do not know how much of the market's collateral is financed at the covenant limit, or whether the hotel signals are independent.

(a) Compute the covenant buffer (the value decline that triggers a breach) at 50% and at 60% LTV.
(b) List the loops, regimes, and crowding considerations that bear on the decision.
(c) Decide: take the upsize, take part of it, decline, or defer. Give the information you would need to change your decision and how you would obtain it.
