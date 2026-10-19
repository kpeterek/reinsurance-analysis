# Chapter 6 Problems — Fixed Income and the Cost of Capital

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch06_solutions.md`. Numerical answers are verified in `tests/test_ch06_examples.py`.
All facts are hypothetical [HYPOTHESIS] unless cited. Treasury yields are semiannual bond-equivalent yields; prices are per 100 face on a coupon date unless stated.

---

### Problem 6.1 (Level 1) — Conventions and concepts
(a) Explain why a Treasury bill's bank-discount rate is always lower than its bond-equivalent yield. Name the two separate reasons.
(b) A colleague says: "The 10-year yields 4.50% and our mortgage costs 6.50%, so our spread is 200 bp and our effective borrowing cost is 200 bp over the risk-free rate." What is imprecise about this statement, and does it matter for the decision?
(c) Give three distinct economic reasons why the cap-rate/10-year-Treasury spread need not return to its long-run average. For each, say which term of $c - r_f = RP - g$ it acts through.
(d) Why is the term premium not an observable quantity? What must be supplied to estimate it?

### Problem 6.2 (Level 2) — DV01 in your head
You hold \$25 million face of a 10-year note priced at 98.00 with modified duration 8.2. Without a calculator, estimate (a) the position DV01 and (b) the loss if yields rise 35 bp. (c) Is the duration estimate of the loss too high or too low, and roughly by how much?

### Problem 6.3 (Level 2) — Cap-rate shock through leverage
A stabilized multifamily property is bought at a 5.50% cap rate with 65% LTV. Market cap rates move to 6.25% with NOI unchanged. Estimate the percentage change in property value and in book equity.

### Problem 6.4 (Level 3) — Bills
(a) A 13-week (91-day) bill is quoted at a 4.80% discount rate. Compute its price, BEY, money-market yield, and effective annual yield.
(b) A 52-week (364-day) bill is quoted at a 4.60% discount rate. Compute its price and its BEY using the Treasury's quadratic formula. Compare it with the simple-interest yield $(F-P)/P \times 365/364$ and with the effective annual yield. Explain the ordering.

### Problem 6.5 (Level 3) — Bond analytics and the large-move error
A 7-year Treasury note pays a 3.75% semiannual coupon and yields 4.25%.
(a) Compute its price, Macaulay and modified duration, convexity, and the DV01 of \$5 million face.
(b) Estimate the price change for +200 bp and −200 bp using duration only and using duration plus convexity. Compare with exact repricing.
(c) Give the HP-12C keystrokes for the price, and an Excel formula that returns the modified duration.

### Problem 6.6 (Level 3) — Forwards, carry and roll-down on an inverted curve
(a) An annually compounded zero curve is: 1-year 4.50%, 2-year 4.30%, 3-year 4.25%, 4-year 4.20%, 5-year 4.20%. Compute the one-year forward rates and the 3-year rate two years forward.
(b) A 3-year note with a 4.25% coupon is bought at par. Today's 2.5-year par yield is 4.10%. The position is financed in repo at 4.60%. Over a six-month horizon, compute the carry, roll-down, total per 100 face, the horizon DV01, and the breakeven yield rise.
(c) What does the sign of the carry tell you about the shape of the money-market curve relative to the note? Would you hold the position for the roll-down alone?

### Problem 6.7 (Level 3) — A 5s30s steepener
5-year note: 4.00% coupon, 4.10% yield. 30-year bond: 4.50% coupon, 4.60% yield. You short \$20 million face of the 30-year and buy a DV01-matched amount of the 5-year.
(a) Compute both DV01s, the 5-year face amount, and the hedge ratio.
(b) By full repricing, compute the P&L for: (i) 5-year −25 bp, 30-year +10 bp; (ii) parallel +100 bp; (iii) parallel −100 bp; (iv) 5-year +20 bp, 30-year −15 bp.
(c) Explain the sign of the P&L in (ii) and (iii).

### Problem 6.8 (Level 4) — The floating-rate hotel
A 160-room select-service hotel earns NOI of \$2,400,000 after a 4% FF&E reserve. It is valued at an 8.00% cap rate. The owner has a \$19,500,000 floating-rate, interest-only loan at the index plus 3.25%. The index is currently 4.30%. Cash-management is triggered below 1.35x DSCR.
(a) Compute value, LTV, current interest cost, DSCR, and cash flow after debt service.
(b) Repeat (a)'s debt-service figures if the index rises 200 bp.
(c) Assume cap-rate pass-through of 0.5 to the same 200 bp move. Compute the new value, the change in book equity, and the effective duration of the property and of the equity. Compare with the first-order formulas.
(d) A rate cap struck at a 5.00% index is offered. What is the worst-case all-in rate and DSCR with the cap? Should the owner buy it? Give a decision rubric, not only a number, and state what information about the cap premium you would need.

### Problem 6.9 (Level 4) — The broker's spread argument
An industrial property is marketed at a 6.00% cap rate when the 10-year Treasury yields 4.40%. The broker writes: "The spread is only 160 bp against a long-run average near 300 bp. Cap rates must rise, so buy now, before the correction, at a price that already reflects today's rates."
(a) Compute the implied unlevered risk premium if expected NOI growth is 2%, 3% or 4%.
(b) Suppose the "normal" risk premium is 5.5% and long-run growth is 2.5%. What cap rate does (6.12) imply at today's Treasury yield? What value change from today's 6.00% does that imply?
(c) Identify the logical problem in the broker's sentence. Write a two-paragraph reply, with a rubric for judging the argument.

### Problem 6.10 (Level 5) — Should we hedge a deal that may not close?
You are 60 days from closing a \$40 million acquisition with a 10-year fixed-rate loan of \$30 million, to be priced at closing as the 10-year Treasury plus a spread. The loan's modified duration is about 7.5. The seller is entertaining a competing bid, the property-condition report is not yet in, and you put the probability of closing at 40%. A partner proposes shorting 10-year Treasury futures today, DV01-matched to the loan, "to lock the rate".
(a) Compute the loan's DV01 and the hedge's gain or loss if Treasury yields fall 50 bp.
(b) What is the hedge's P&L in the state where the deal does not close? What is the probability of that state?
(c) Lay out the alternatives: hedge now, hedge partially, buy an option-like instrument, ask the lender for a rate lock at application, or do nothing. Recommend one, and say what information would change your recommendation. Include a rubric.
