# Chapter 10 Problems — Capital Structure, Debt, and Equity

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch10_solutions.md`. Numerical answers are verified in `tests/test_ch10_examples.py`.
All facts are hypothetical [HYPOTHESIS] unless cited. Mortgage payments are monthly in arrears at $r/12$ unless stated.

---

### Problem 10.1 (Level 1) — Recourse, carve-outs, and covenants
A borrower has a non-recourse loan with a standard carve-out guarantee from its principal: loss recourse for misapplied rents, waste, and environmental liabilities; springing full recourse for a voluntary bankruptcy filing and for any unpermitted transfer of an interest in the borrower. For each event say whether it creates (i) no personal liability, (ii) liability for actual losses, or (iii) full recourse. Say what fact, if any, would change your answer.

(a) NOI falls and DSCR drops below the 1.20x cash-management trigger.
(b) The loan matures and the borrower cannot refinance.
(c) After a monetary default, the property manager pays the sponsor's affiliate a "development fee" out of rents.
(d) The sponsor sells 49% of its interest in the borrower to a new partner without the lender's consent.
(e) The borrower files a voluntary Chapter 11 petition to stop a foreclosure sale.
(f) A Phase I report ordered by the lender after default reveals contamination from a former dry cleaner tenant.

Then explain in three sentences why a lender wants the guarantor to have meaningful net worth and liquidity even though the loan is "non-recourse".

### Problem 10.2 (Level 2) — Three constraints in your head
NOI \$1,800,000. Appraised value \$30,000,000. Lender: max 65% LTV, min 1.25x DSCR, min 9.0% debt yield. The quoted rate and amortization give a loan constant of 7.50%. Without a calculator, find the three loan amounts and the maximum loan. Which constraint binds?

### Problem 10.3 (Level 2) — Floating rate with a cap
A \$20,000,000 IO bridge loan pays SOFR + 3.50%. A cap is struck at 4.00% SOFR. NOI is \$1,650,000.
(a) SOFR is 5.25%. Compute annual interest without and with the cap, and the cap's annual payout.
(b) Compute DSCR with the cap and without it.
(c) The lender sized the loan at the strike. What was the sizing DSCR?

### Problem 10.4 (Level 3) — IO period, amortization and the balloon
\$12,000,000 loan at 7.00%, 25-year amortization, 7-year term. The first 24 months are interest-only; amortization on the 25-year schedule starts in month 25.
(a) Monthly payment during and after the IO period, and annual debt service in each phase.
(b) The balloon at month 84.
(c) The balance at month 84 if the loan had amortized from month 1. How much larger is the balloon because of the IO period?
(d) Give HP-12C keystrokes for (b).

### Problem 10.5 (Level 3) — Capital stack
An \$80,000,000 multifamily recapitalization: senior \$48,000,000 (6.25% IO), mezzanine \$12,000,000 (12% IO), preferred equity \$8,000,000, common \$12,000,000. NOI \$4,800,000.
(a) Attachment and detachment points of each tranche.
(b) Senior DSCR, combined senior + mezz DSCR, and NOI / (senior + mezz).
(c) Allocate losses if value falls to \$64,000,000 and to \$56,000,000.
(d) What percentage value decline first impairs the mezz, and what decline wipes it out? Same for the pref.

### Problem 10.6 (Level 3) — Waterfall and promote
Total equity \$20,000,000 (pooled LP and GP co-invest). Annual project equity flows (\$ million): −20.0, 1.2, 1.3, 1.4, 1.5, 27.0. Waterfall: 100% to investors until an 8% IRR; 85/15 to a 13% IRR; 75/25 thereafter.
(a) Use `sdesk.cre.irr_hurdle_waterfall` to compute the project IRR, the investor IRR, and the total promote.
(b) Repeat with a year-5 flow of 22.0 instead of 27.0.
(c) Explain, using (a) and (b), why the promote is an option and what that implies for the GP's attitude to risk.

### Problem 10.7 (Level 3) — Pricing a cap and the strike–proceeds trade-off
A 3-year cap on \$40,000,000 with quarterly caplets (the first period is already fixed). Flat forward SOFR 4.25% (quarterly compounding for discounting). Normal volatility 1.10%.
(a) Price the cap at a 3.50% strike: premium, percentage of notional, and annual-equivalent bp.
(b) Price it at a 4.50% strike.
(c) NOI is \$3,000,000, spread 3.00%, and the lender requires 1.15x DSCR sized at strike + spread, IO. Compute the maximum DSCR loan at each strike.
(d) Which strike should the borrower buy? State what the answer depends on.

### Problem 10.8 (Level 4) — Fund the call or be diluted
A JV has 100 units: LP 80, GP 20. Contributions were \$25,000,000 (\$250,000 a unit). The loan matures with a \$4,000,000 refinancing gap. The pre-call fair value of the equity is \$6,000,000. If the call is funded, post-call equity is worth \$10,000,000. The LP will fund; the GP may not.
(a) GP ownership and stake value if the LP funds both shares at fair value, with no penalty and with a 125% punitive credit.
(b) The same if units are issued at the original \$250,000 price.
(c) Should the GP fund its \$800,000 share under each pricing rule? Should the LP accept the JV's book-value pricing clause? Explain with numbers.

### Problem 10.9 (Level 4) — The distressed note bid
A defaulted \$18,000,000 senior note is offered at \$14,000,000. No interest will be collected during the workout. Your scenarios:

| Resolution | p | Gross recovery | Costs | Years |
|---|---|---|---|---|
| Modification, payoff at par | 0.30 | \$18,000,000 | \$200,000 | 2 |
| DPO | 0.30 | \$15,500,000 | \$150,000 | 1 |
| Foreclosure and REO sale | 0.40 | \$16,000,000 | \$1,400,000 | 2 |

Required return 15%.
(a) Expected PV, NPV at the ask, and the annualized return in each scenario.
(b) Holding the other scenarios fixed, what gross foreclosure recovery would make the ask break even? Is that plausible?
(c) What do you do?

### Problem 10.10 (Level 5) — The rescue preferred equity call
On a Friday a sponsor asks you to commit \$6.0 million of preferred equity by Tuesday into a 1990s-vintage 310-unit apartment property. Facts provided:
* Senior bridge loan \$38.0 million, SOFR + 3.40%, maturing in 5 months; one extension option requires a 1.15x DSCR at the cap strike and a new 12-month cap.
* "Stabilized NOI" on the sponsor's model: \$3.1 million. Trailing-3-month NOI annualized: \$2.35 million. Trailing-12: \$2.55 million.
* The sponsor says an appraisal "came in around \$44 million" but will not share it until you sign an NDA and term sheet.
* Insurance renewal is "pending".
* The sponsor's existing LPs have been asked to fund a capital call; "most" have agreed.
* Your pref would earn 13% current plus a 1.6x multiple-on-invested-capital floor, and sit behind the senior loan.

Write a one-page decision memo: (a) estimate attachment and detachment points on at least two value estimates and state your assumptions; (b) identify the contradictions in the facts and what each implies; (c) list the information you require and why; (d) state your decision and the conditions under which you would revisit it.
