# Chapter 11 Problems — Hotels: The High-Beta CRE Asset

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch11_solutions.md`. Numerical answers are verified in `tests/test_ch11_examples.py` (functions `test_problem_11_*`).
All facts are hypothetical [HYPOTHESIS] unless cited. Use 365 days, and NOI after a 4% FF&E reserve unless stated.

---

### Problem 11.1 (Level 1) — Concepts
(a) Give three structural reasons why a 10% fall in revenue reduces a hotel's NOI by far more than 10%, while a 10% fall in market rents may not change a leased office building's NOI at all this year.
(b) A lender capitalizes NOI after a 4% reserve; a strategic buyer quotes "11× EBITDA". Are these inconsistent? What must be true for both to describe the same price?
(c) Why is RGI more informative than RevPAR growth for judging a hotel's operator? Name one way RGI itself can mislead.
(d) Distinguish the FF&E reserve, a PIP, and deferred capital expenditure. Which of them does a lender escrow, which does a buyer deduct from price, and which does neither normally capture?

### Problem 11.2 (Level 2) — Mental arithmetic
A 150-room hotel runs 68% occupancy at a \$140 ADR. Without a calculator: (a) RevPAR; (b) annual rooms revenue; (c) the rooms revenue in one occupancy point; (d) annual franchise fees at 11% of rooms revenue.

### Problem 11.3 (Level 2) — Penetration
Subject: occupancy 66%, ADR \$172. Comp set: 71%, \$160. Compute MPI, ARI and RGI. In one sentence, what is the revenue manager's strategy, and is it working?

### Problem 11.4 (Level 3) — The flow-through gap
A select-service hotel's total revenue rose from \$6.20 million to \$6.55 million, mostly through rate. GOP rose from \$2.48 million to \$2.53 million. The operator's budget assumed 75% flow-through on rate-led growth.
(a) Actual GOP flow-through.
(b) GOP expected at 75% flow-through, and the shortfall.
(c) The controller identifies wage inflation of \$130,000, an OTA commission increase of \$55,000 and a utilities increase of \$27,500. Do these explain the shortfall?
(d) Assuming the shortfall persists and passes to NOI dollar for dollar, what is it worth at a 9% cap?

### Problem 11.5 (Level 3) — Break-even occupancy
A 100-room hotel: ADR \$120; other revenue 2% of rooms revenue; variable cost \$28 per occupied room; revenue-variable costs (fees, card fees, reserve) 20% of total revenue; fixed costs \$1,250,000; debt service \$550,000.
(a) Contribution per occupied room.
(b) Break-even occupancy before and after debt service (use `sdesk.hotel.breakeven_occupancy` or equation 11.2).
(c) Break-even after debt service if ADR falls 8% in a downturn.
(d) What does (c) imply for the use of break-even occupancy in a lender's stress test?

### Problem 11.6 (Level 3) — Displacement
A 250-room hotel has 20 rooms of contract business every night. A group requests 120 rooms for two nights at \$175, with \$60 of banquet spend per room-night at a 35% margin and no commission. Transient demand on those nights is forecast at 190 rooms per night at \$235, with a 15% acquisition cost. Variable cost per occupied room is \$40; brand and management fees total 10% of rooms revenue; ignore ancillary transient spend, attrition and shoulder nights.
(a) Displaced transient rooms per night.
(b) Group contribution, displaced contribution, and the net effect of accepting.
(c) The break-even group rate.
(d) Name two facts that would change your answer.

### Problem 11.7 (Level 3) — Incentive fee
A full-service hotel: total revenue \$30.0 million; property tax and insurance \$2.1 million; reserve 4%; base fee 3% of total revenue; incentive fee 15% of available cash flow (GOP − base fee − tax and insurance − reserve) above an owner's priority of 9% on \$70 million invested.
(a) GOP \$9.6 million: base fee, ACF, incentive fee, owner cash.
(b) GOP \$11.5 million, revenue unchanged: the same four figures.
(c) An alternative contract pays 8% of GOP as the incentive fee with no priority. Owner cash in (a) and (b)?
(d) Which contract would you rather sign as the owner, and why?

### Problem 11.8 (Level 4) — The return on a PIP
A 160-room hotel at a \$98 RevPAR faces a \$3.2 million PIP; budget 10% contingency. NOI flow-through on rooms revenue is 72%. The owner requires an 11% return on renovation capital.
(a) The RevPAR lift needed (equation 11.4), in dollars and percent.
(b) The brand projects a \$6 RevPAR lift. What return does the PIP earn on its own?
(c) If the owner refuses the PIP, the brand will not renew; operating independent would cost \$420,000 of NOI a year relative to today. Recompute the return on the PIP relative to that alternative.
(d) Should the owner do the PIP? What is the right comparison?

### Problem 11.9 (Level 4) — The hotel loan
A buyer will pay \$17.8 million for a hotel with T-12 NOI of \$1.6 million (after reserve). Lender terms: 60% LTV, 1.45x DSCR, 11.0% debt yield, 7.40% rate, 25-year amortization, all on T-12 NOI and the purchase price. A \$2.0 million PIP is to be funded with equity. Buyer closing costs are 2%. The loan has a cash-management trigger at 1.25x DSCR.
(a) Each constraint, the binding constraint, and the loan.
(b) Annual debt service and the in-place DSCR.
(c) Equity required at closing.
(d) If NOI falls 15% during the renovation, does the cash trap trip? By how much can NOI fall before it does?

### Problem 11.10 (Level 5) — The 24-hour BOV
A special servicer asks for a "firm value by tomorrow" on a 100-room limited-service hotel for a loan-modification decision. You have: the borrower's T-12 showing RevPAR of \$104; an STR report showing the subject's RevPAR for the same twelve months at \$92; a franchise agreement that expires in 14 months, with no PIP letter; a tax bill on an assessment set before a sale three years ago; and no information about insurance. Typical NOI flow-through on rooms revenue for hotels of this type is about 75% and your working cap rate is 9.5% [HYPOTHESIS].
(a) Quantify how much value depends on which RevPAR figure is right.
(b) List the possible explanations for the RevPAR discrepancy and what document would resolve each.
(c) Write the response to the servicer: what you will deliver tomorrow, and what you will not. Is a point value the right output?
