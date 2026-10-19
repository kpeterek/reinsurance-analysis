# Chapter 1 Problems — What Is Speculation?

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch01_solutions.md`. Numerical answers are verified in `tests/test_ch01_examples.py`.
All facts are hypothetical [HYPOTHESIS] unless cited.

---

### Problem 1.1 (Level 1) — Classification
Classify each activity as investment, speculation, arbitrage, hedging, or gambling. Name the risk borne and who, if anyone, pays to have it borne. Some items fit more than one category depending on facts not given; say which facts would decide.

(a) A pension fund buys a 10-year Treasury note to hold to maturity against a 10-year liability.
(b) A developer buys an agricultural parcel at the edge of a metro because a highway interchange has been proposed but not funded.
(c) A trader buys a futures contract on one exchange and simultaneously sells the identical contract (same delivery, same clearing house) on another venue at a 0.5-point higher price.
(d) A hotel owner with a floating-rate loan buys a two-year interest-rate cap struck at 5%.
(e) An individual buys \$500 of state lottery tickets.
(f) The same hotel owner from (d) sells the hotel but keeps the cap.

### Problem 1.2 (Level 1) — Process versus outcome
Two analysts each recommended a hotel acquisition in 2019. Analyst X wrote a memo with three scenarios, including a 10% "severe travel shock" scenario that would cut NOI by 60% for one year, and recommended 55% LTV with 18 months of debt-service reserves. Analyst Y wrote "RevPAR has grown for nine straight years" and recommended 75% LTV with no reserve. In 2020 both hotels lost most of their revenue for a time. X's investment survived and Y's was foreclosed.
(a) Was Y's decision bad because of the outcome? Explain what would make it bad independent of outcome.
(b) Suppose instead that no pandemic had occurred and Y earned a higher IRR than X. Would that make Y's decision better? What evidence would you need to judge?

### Problem 1.3 (Level 2) — Mental arithmetic: drag
A strategy returns +40% or −30% with equal probability each period, and the full capital is committed every period. Without a calculator, give (a) the arithmetic expected return per period and (b) the compound growth rate per period. (Hint: consider one win and one loss.)

### Problem 1.4 (Level 2) — Break-even probability
A bid on a distressed loan makes \$1.2 million if the borrower cures and loses \$2.0 million if the lender must foreclose. What foreclosure probability makes the bid's EV zero? If your estimate of the foreclosure probability is 25–45%, is the decision robust?

### Problem 1.5 (Level 3) — Scenario analysis of a hotel bid
A buyer pays \$5,200,000 for a 78-room hotel plus 2% closing costs, all cash. Two-year hold. Selling costs 3%. NOI is after reserve and received at year-end.

| Scenario | p | NOI Y1 | NOI Y2 | Gross sale end Y2 |
|---|---|---|---|---|
| Good | 0.50 | 420,000 | 450,000 | 6,000,000 |
| Base | 0.35 | 400,000 | 410,000 | 5,400,000 |
| Bad | 0.15 | 330,000 | 300,000 | 4,300,000 |

Compute (a) basis; (b) profit and IRR per scenario; (c) expected profit, standard deviation, probability of loss; (d) expected IRR and the IRR of expected cash flows; (e) the three-state break-even bad-state probability holding Good:Base at 50:35.

### Problem 1.6 (Level 3) — Price of immediacy
(a) An owner can sell an apartment building today for \$4,600,000 with negligible costs, or market it for an expected 8 months and receive an expected \$5,100,000 gross, less 3% selling costs and \$90,000 of carrying costs. Compute the annualized price of immediacy.
(b) In Example 1.3 the chapter used the expected delay (0.55 years) in place of the two separate delays. Compute the exact rate $r$ that solves $0.8 N_1/(1+r)^{0.5} + 0.2 N_2/(1+r)^{0.75} = N_0$. Here $N_1 = 9{,}000{,}000 \times 0.97 - 250{,}000$, $N_2 = 8{,}400{,}000 \times 0.97 - 250{,}000$, and $N_0 = 7{,}722{,}000$. How large is the approximation error?

### Problem 1.7 (Level 3) — Market making
A dealer quotes a quoted spread of 0.12 points. Fifteen percent of order flow is informed, and informed trades move fair value 0.60 points against the dealer.
(a) Expected profit per trade?
(b) Competitive quoted spread?
(c) Ahead of a major data release the informed share rises to 30%. What spread should the dealer quote? What does this predict about trading costs around releases?

### Problem 1.8 (Level 4) — The back-to-back deal
You can buy a net-leased building for \$3,200,000 (buyer costs 1.5%). An exchange buyer has signed a non-binding LOI at \$3,450,000 (your selling costs 2%). Probability the exchange buyer closes: 0.65. If they walk you collect \$60,000 of net rent and sell later at an expected \$3,150,000 gross (2% costs).
(a) Profit if the buyer closes and if they walk; EV.
(b) Minimum closing probability for non-negative EV.
(c) What hard (non-refundable) deposit from the exchange buyer, received only if they walk, would make your walk-away outcome break even? Would you proceed without it? Explain.

### Problem 1.9 (Level 4) — Leverage and survival
An asset's one-year total return (income plus appreciation) is +16% with probability 0.60, −4% with probability 0.30, and −25% with probability 0.10. Debt costs 5% (interest only). Debt is non-recourse, so equity cannot lose more than 100%.
(a) Compute equity returns in each state at LTV of 0%, 50%, 65%, 75%, and 85%.
(b) Compute the arithmetic expected equity return at each LTV, applying the −100% floor.
(c) Compute expected log growth $E[\ln(1+r_E)]$ at each LTV. Where is it undefined, and what does that mean?
(d) A sponsor argues: "Expected equity return rises monotonically with leverage, so 85% LTV is best for investors." Evaluate.

### Problem 1.10 (Level 5) — Judgment under incomplete information
A broker calls on Thursday. A 140-room full-service hotel in a drive-to leisure market is available because the owner's partnership is dissolving. Facts you have:
* Trailing-12 NOI after reserve \$1.9 million; NOI two years earlier was \$2.6 million.
* Asking price \$21 million. The broker hints that "\$18 million would get it done before year-end."
* A competing 120-room hotel opened 3 miles away 14 months ago.
* The brand's license expires in 30 months. No PIP letter has been provided.
* Regional banks you know have stopped quoting hotel loans above 55% LTV.
* You have 10 business days before the owner's partners vote.

Write a one-page decision memo: bid, pass, or wait-and-gather-information. State (a) your preliminary value range and the assumptions behind it, (b) the three most important unknowns, ranked by their effect on value, (c) what you would do in the 10 days, (d) your bid (if any), its conditions, and walk-away triggers, and (e) what the seller's motivations imply about price.
