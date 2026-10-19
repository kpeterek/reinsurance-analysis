# Chapter 19 Problems — Alternative and Emerging Speculative Assets

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch19_solutions.md`. Numerical answers are verified in `tests/test_ch19_examples.py`.
All facts are hypothetical [HYPOTHESIS] unless cited.

---

### Problem 19.1 (Level 1) — What pays you if you never sell?
For each asset, state (i) whether a holder who never sells receives any cash flow, (ii) the strongest valuation anchor available, and (iii) the one dimension of the nine that you would examine first.

(a) A 20-year net-leased distribution warehouse.
(b) An EU emissions allowance.
(c) A governance token that votes on a lending protocol's parameters.
(d) A catalogue of song royalties.
(e) An unentitled 60-acre parcel at a metro fringe.
(f) A bitcoin held on a non-U.S. exchange.

### Problem 19.2 (Level 2) — Fund multiples
A fund has called \$60 million, distributed \$18 million and reports NAV of \$66 million. Without a calculator give DPI, RVPI and TVPI. What share of TVPI is an estimate?

### Problem 19.3 (Level 2) — An auction round trip
A print is bought at a \$500,000 hammer with a 27% buyer's premium (flat over this range). It is resold later at the same hammer with a 10% seller's commission. (a) What is the round-trip cost? (b) Spread over a 4-year hold, what annual return drag does it impose?

### Problem 19.4 (Level 3) — KS-PME
A fund's flows (\$ million) and a public index at year-ends:

| Year | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Calls | 40 | 30 | 30 | 0 | 0 | 0 |
| Distributions | 0 | 0 | 20 | 50 | 40 | 30 |
| Index | 100 | 90 | 95 | 110 | 120 | 130 |

(a) TVPI and IRR. (b) KS-PME. (c) KS-PME if the index had been flat at 100 throughout. Explain the result. (d) The index's annual return. (e) The year-5 balance of a mirror index account that receives each call and pays each distribution. What does its sign tell you?

### Problem 19.5 (Level 3) — Unsmoothing and a stale NAV
(a) Reported annual returns $r^*_0, \dots, r^*_5$ are 4%, 7%, 6%, 1%, −3%, 2%. With $a = 0.6$, compute unsmoothed $r_1, \dots, r_5$, the sample standard deviations of both series (years 1–5), and the theoretical volatility ratio. Verify the end-point identity for the arithmetic sums.
(b) A fund's last NAV is \$50 million. Since the mark the relevant listed index has fallen 15%, and the fund's beta is 1.3. A buyer bids 88% of NAV. What is the bid relative to corrected value?

### Problem 19.6 (Level 3) — Venture power law
Deal multiples: 0x (0.50), 1x (0.30), 4x (0.15), 20x (0.04), 100x (0.01). A fund makes 25 independent equal-sized investments.
(a) The mean deal multiple and the share contributed by the 100x outcome.
(b) The probability that the fund contains no 100x outcome.
(c) The expected fund multiple given no 100x outcome.
(d) The exact median fund multiple and the probability that the fund returns below 1x are 1.88x and 15.7% (by enumeration; see the tests). Explain why the median is so far below the mean, and what changes if the fund makes 100 investments instead.

### Problem 19.7 (Level 3) — Repeat sales and selection
(a) Six watches sold twice (periods 0–2): A 0→1, $y = 0.05$; B 0→1, $0.09$; C 1→2, $-0.04$; D 0→2, $0.02$; E 1→2, $0.00$; F 0→2, $0.08$. Estimate the repeat-sales index.
(b) Eight watches were bought at period 0 with true log changes −0.25, −0.15, −0.05, 0.00, 0.05, 0.10, 0.20, 0.35 to period 2. Only owners with gains of 0.05 or more resell. Compute the selection bias.

### Problem 19.8 (Level 4) — The subscription line
Take the fund of Example 19.2. The GP now funds the year-0 and year-1 investments (\$25 million each) with a subscription line at 7% a year, compounded annually, and repays principal and interest from an LP call at year 2. Distributions are unchanged.
(a) The year-2 call and the new contribution vector.
(b) The new IRR, TVPI and total profit, compared with the original.
(c) An LP's investment committee ranks managers by IRR. What is wrong with that, and what would you report instead? *(Rubric in solutions.)*

### Problem 19.9 (Level 4) — Token or land?
A client can put \$1 million into either (i) a token with no cash flow, priced at 80, for which her three-year resale view is 150 (p = 0.5), 60 (0.35), 5 (0.15), or (ii) a land parcel like Example 19.8 at \$2.1 million with partners.
(a) At a required return of 15%, what is the token worth? Is a price of 80 justified on her own view?
(b) What price must the token reach in 3, 10 and 20 years for a buyer at 80 to earn 15%?
(c) Compare the anchors. Which would you recommend, at what size, and what would change your mind? *(Rubric in solutions.)*

### Problem 19.10 (Level 5) — The 11% stablecoin yield
A platform offers the family office 11% a year on U.S.-dollar stablecoin deposits, paid weekly. Facts available: the platform is incorporated offshore; its terms of service say deposits may be "re-hypothecated"; its published reserve report is unaudited and lists 40% of assets as "loans to institutional counterparties" (unnamed) and 25% as the platform's own governance token; a large crypto newsletter calls it "the safest yield in DeFi"; a family member has had funds there for a year without a problem; and the platform's token rose 60% last quarter.
Write a one-page recommendation. Include: what the 11% compensates for; a stress test in which the platform's token falls 80% and 30% of the institutional loans default with zero recovery; what claim the family would have in an insolvency; and whether to invest. *(Rubric in solutions.)*
