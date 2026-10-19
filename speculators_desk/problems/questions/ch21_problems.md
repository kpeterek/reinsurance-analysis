# Chapter 21 Problems — Risk Management and Position Sizing

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch21_solutions.md`. Numerical answers are verified in `tests/test_ch21_examples.py`.
All facts are hypothetical [HYPOTHESIS] unless cited. Use $z_{0.99} = 2.3263$.

---

### Problem 21.1 (Level 1) — What the numbers do not say
For each statement, say whether it is true, false, or true only under stated conditions, and why.
(a) "Our one-day 99% VaR is \$2m, so we will not lose more than \$2m tomorrow except one day in a hundred."
(b) "Adding a second, independent position can never raise our VaR."
(c) "Our stop is 3% below entry, so our maximum loss on the position is 3% of notional."
(d) "The hotel has no daily price, so it adds nothing to the book's market risk."
(e) "We size at half-Kelly, so we give up half our growth."

### Problem 21.2 (Level 2) — Sizing a crude-oil futures trade
Capital \$20m. Long crude-oil futures at \$80 per barrel, 1,000 barrels per contract. Stop at \$76. Risk per trade 0.75% of capital. Daily crude volatility 2.5%. Daily volatility target for the position 0.30% of capital.
(a) Contracts by the stop rule and by the volatility rule. Which binds?
(b) You trade the binding number. Overnight the market opens at \$72. What is the loss, and what multiple of the planned stop loss is it?

### Problem 21.3 (Level 2) — Fractional Kelly without a calculator
An asset has expected excess return 5% and volatility 20%. With $r = 0$, give $f^*$ and the maximum excess growth $G^*$. Then give the excess growth at 0.5, 1.5, 2 and 3 times $f^*$.

### Problem 21.4 (Level 3) — Historical VaR, ES, and a back-test
A desk has 250 daily P&Ls. The seven worst, in \$000, are −2,150, −1,630, −1,410, −1,220, −1,180, −990 and −940. All other days are better than −940.
(a) Using the convention that VaR is the loss at sorted index $\lfloor n(1-c)\rfloor$ (counting from 0), give VaR and ES at 99% and at 97.5%.
(b) The desk's parametric model reported a 99% VaR of \$1,000,000 every day of the year. How many exceptions occurred, how many were expected, and what is the probability of at least that many exceptions if the model were correct?
(c) What do you conclude, and what would you check next?

### Problem 21.5 (Level 3) — Ruin and drawdown
(a) A trader makes unit bets that win with probability 0.52, starting 15 units above the point where the account is closed. What is the probability of ruin with no profit target? With a target of 30 units?
(b) A strategy has expected excess return 4% and volatility 15% ($r = 0$). At full Kelly and at half Kelly, compute the log drift and log volatility of wealth, the probability of ever losing 40% from the start, and the probability of losing 40% from the start within 5 years.
(c) Explain why the probability of a 40% drawdown from a running peak over 5 years is higher than your answer to (b).

### Problem 21.6 (Level 3) — Liquidity-adjusted VaR
You hold 600,000 shares of a REIT at \$35. ADV is 150,000 shares and you will not exceed 25% participation. Daily volatility is 2.2%. The stressed bid-ask spread is 0.80%.
(a) Days to liquidate.
(b) One-day 99% VaR, liquidation-horizon VaR with even daily sales, and LVaR.
(c) The largest position you could exit in five days at the same participation.

### Problem 21.7 (Level 3) — Margin and covenant arithmetic
(a) Long 20 crude contracts at \$80 (1,000 bbl each) with \$200,000 in the account. Initial margin \$7,000 and maintenance \$6,000 per contract. What price fall triggers a call, and how large is the call at the trigger? What is the call if the price falls \$8?
(b) An office building is worth \$40m with a \$26m loan and a 70% maximum-LTV covenant. What decline breaches the covenant? What cure is required if the value falls 20%?

### Problem 21.8 (Level 4) — Leverage for a long–short REIT strategy
An analyst's eight-year backtest of a long–short REIT strategy shows an excess return of 5% a year at 10% volatility. She proposes running it at the Kelly leverage. The prime broker allows up to 6× gross.
(a) What leverage does she propose? Compute the expected growth at $k = 1$, $k = 0.5$, and the optimal shrinkage, given the eight-year estimation error (assume the true edge equals the estimate).
(b) If the true edge is 2.5%, what growth does her proposed leverage produce? What does 2× leverage produce?
(c) Recommend a leverage and the limits around it. Rubric required.

### Problem 21.9 (Level 4) — Stress-testing a hedged book
NAV \$40m: \$15m of 10-year Treasuries (modified duration 8.5, convexity 85); short 20 ES contracts at 5,000 (\$50 multiplier); \$6m of equity in a \$20m hotel with a \$14m non-recourse loan; a \$5m hotel mezzanine loan. Two hypothetical scenarios:

| | A: deflationary crash | B: stagflation |
|---|---|---|
| 10-yr yield | −100 bp | +150 bp |
| ES | −30% | −15% |
| Hotel value | −30% | −10% |
| Mezz loan mark | −40% | −10% |

(a) P&L by position and in total under each scenario, in dollars and percent of NAV.
(b) Which position dominates? What single change most reduces the worst stress loss? Rubric required.

### Problem 21.10 (Level 5) — The model change during a breach
You are the independent risk officer for a credit-derivatives book. On Monday the book's 99% VaR is \$118m against a \$100m limit, the fourth consecutive day in breach. The desk head proposes a new VaR model, already "reviewed" by a modeler who reports to him, that produces \$62m on the same positions. He asks you to approve it today and to raise the book's index position by 30%, which he describes as a hedge. In a 60-day parallel run, daily losses exceeded the *new* model's VaR five times. Market liquidity in the index tranches is thin.
(a) Compute the VaR reduction and the probability of five or more exceptions in 60 days if the new model were correct.
(b) Decide on the model and on the position increase. Abstention (approving neither) is an admissible answer. Rubric required.
