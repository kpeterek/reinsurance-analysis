# Chapter 9 Problems — CRE Valuation and Mispricing

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch09_solutions.md`. Numerical answers are verified in `tests/test_ch09_examples.py`.
All facts are hypothetical [HYPOTHESIS] unless cited. NOI is after replacement reserves; cash flows are annual and at year-end.

---

### Problem 9.1 (Level 1) — Which numbers are evidence of value?
A seller's package for a 1990s suburban office building contains the following. For each, say whether it is evidence of market value, evidence of the seller's reservation price, evidence of something else (say what), or irrelevant. Explain in one or two sentences.

(a) The owner's 2016 purchase price.
(b) A 2022 appraisal prepared for the owner's lender.
(c) A contractor's estimate of replacement cost.
(d) Three sales of comparable buildings in the last six months, one by a lender after foreclosure.
(e) Two withdrawn listings in the same submarket and their best bids.
(f) The current yield on listed office REITs, implied from their share prices and reported NOI.

### Problem 9.2 (Level 2) — Mental arithmetic
(a) A property with forward NOI of \$1.8 million is valued at a 6.00% cap. NOI then falls 5% and the cap rate rises to 6.75%. Give the new value and the percentage change.
(b) The same property has NOI before property tax of \$2.2 million, and post-sale tax will be 1.50% of price. At a 6.00% market cap rate on NOI after tax, what is the value? What value results if you forget that tax resets?

### Problem 9.3 (Level 2) — What must the buyer believe?
An industrial building trades at a 5.25% cap rate. Long-run capital spending is 10% of NOI.
(a) If buyers require 7.50% unlevered, what perpetual NOI growth does the price imply?
(b) If long-run NOI growth is 2.0%, what unlevered return does the buyer earn?
(c) What cap rate is consistent with 7.50% and 2.0% growth?

### Problem 9.4 (Level 3) — DCF timing traps
A single-tenant retail building has Year 1 NOI of \$1,000,000, growing 2.5% a year. Capital spending is 3% of NOI each year, plus a \$400,000 roof replacement in Year 3. You will sell at the end of Year 5 at a 7.00% cap with 2% selling costs. The discount rate is 8.5%.
(a) Build the cash-flow table for Years 1–6 and value the property.
(b) Compute the reversion share and the implied going-in cap rate.
(c) Compute the value if an analyst capitalizes Year 5 NOI at exit instead of Year 6 NOI. How large is the error?
(d) What is the present value of the roof? What does the answer imply for a buyer who "handles the roof through the reserve"?

### Problem 9.5 (Level 3) — Residual land value
A developer plans 250 apartment units. Stabilized NOI \$4,200,000. Hard costs \$52.0 million, soft costs \$9.5 million, financing \$4.0 million. Selling costs 1.5%. Required margin on total cost 15%.
(a) Compute residual land value at exit caps of 5.00%, 5.25%, and 5.50%, in total and per unit.
(b) The landowner asks \$6.0 million. At a 5.25% cap, what margin does the developer earn, and what is the yield on cost?
(c) Explain in two sentences why land prices tend to stop transacting before building prices fall.

### Problem 9.6 (Level 3) — Sales comparison with a stale comp
Subject: a 120-unit apartment building. Comparable sales, per unit, with multiplicative adjustments:

| Comp | Price/unit | Time | Location | Physical |
|---|---:|---:|---:|---:|
| X | \$310,000 (18 months ago) | −10% | 0% | +5% |
| Y | \$265,000 (2 months ago) | −2% | +8% | 0% |
| Z | \$290,000 (5 months ago) | −4% | −3% | −5% |

(a) Compute adjusted prices and the value weighted by the inverse of gross adjustment.
(b) What does Comp X indicate if the analyst omits the time adjustment? Why is this error most common exactly when it matters most?

### Problem 9.7 (Level 3) — Property versus equity IRR
Price \$18,000,000 plus 1% buyer costs. Year 1 NOI \$1,170,000 (6.50%), growing 2% a year. Capital spending 6% of NOI. Sale at the end of Year 5 at a 7.00% cap on Year 6 NOI, 2% selling costs. Loan 65% of price at 6.00%, 25-year amortization, monthly payments, balloon at Year 5.
(a) Property IRR.
(b) Loan constant, annual debt service, Year 1 DSCR and debt yield, balance at Year 5.
(c) Equity IRR and first-year cash-on-cash. Is leverage positive or negative on current yield? On IRR?

### Problem 9.8 (Level 4) — Is it value-add or market beta?
A sponsor proposes a \$30,000,000 acquisition of a partially vacant flex-industrial property. Year 1 NOI \$1,800,000 (6.00%). The plan: spend \$1,200,000 of TI/LC in Year 2 to lease the vacancy, adding \$300,000 of NOI from Year 3 (growing with the market after that). The sponsor assumes 2% market growth and an exit at 5.75% on Year 6 NOI at the end of Year 5. Ignore transaction costs. The sponsor's deck says: "11.3% IRR from our value-add strategy."
(a) Decompose the IRR into income, market growth, value-add, and cap-rate change, in that order.
(b) Compute the IRR with zero market growth and the business plan, at exit caps of 6.00% and 6.50%.
(c) Write a three-sentence committee comment on the deck's claim, and say how the fee and promote should be structured given your decomposition.

### Problem 9.9 (Level 4) — The anchored self-storage owner
A self-storage owner's 2022 appraisal valued the property at \$28.0 million (NOI \$1,260,000 at 4.50%). Forward NOI is now \$1,200,000 and comparable sales indicate a 6.00% cap. The owner's \$17.0 million loan matures in nine months. A refinance lender offers the lesser of 60% LTV, 1.25x DSCR at 6.75% on 30-year amortization, and a 9.0% debt yield, with 1% costs. A buyer has offered \$19.5 million; the owner's selling costs would be 2%.
(a) Compute market value, the maximum refinance loan and its binding constraint, and the cash the owner must bring to refinance.
(b) Compute the sale price at which the owner pays off the loan without bringing cash, and the owner's net cash at \$19.5 million.
(c) What will the owner do, and when? If you are the buyer, what is your strategy for the next nine months? Include what would make you raise or withdraw the offer.

### Problem 9.10 (Level 5) — The LP secondary at a discount to NAV
An open-end private real estate fund reports NAV of \$100 per unit. Its appraisals are down 8% from their 2022 peak. Gross assets are 40% office, 35% industrial, and 25% apartments by value, with 30% leverage (debt is 30% of gross assets). Listed office REITs are down about 35% over a similar period. An LP who cannot wait for the redemption queue offers units to you at \$78, a 22% discount to NAV.

Assume the fund's remaining appraisal lag means true asset values are below current appraisals by: office 20–30%, industrial about 5%, apartments about 8% [all HYPOTHESIS].
(a) Compute the implied "true" NAV per unit at office haircuts of 20% and 30%, and the discount or premium of \$78 to each.
(b) Find the office haircut at which \$78 equals true NAV.
(c) Decide: buy, pass, or gather information. Name the three pieces of information you would request and how each would change your answer. Identify the conditions under which abstention is the best answer.
