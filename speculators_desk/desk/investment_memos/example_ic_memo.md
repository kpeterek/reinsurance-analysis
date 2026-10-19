# Investment Committee Memorandum — Worked Example (HYPOTHETICAL DATA)

> **Every property fact, lease term, price, financing term, probability, and hurdle rate in this memo is hypothetical [HYPOTHESIS], constructed for teaching in Chapter 25 (§25.11).** No real property, lender, or counterparty is described. Every number is reproduced in `tests/test_ch25_examples.py::test_ic_memo`. Blank template: `desk/investment_memos/investment_committee_memo.md`.

To: Investment Committee   From: Analyst (K.P.)   Date: Day 4, Thursday (hypothetical)   Re: Bid on 240,000 sf single-tenant industrial building, submarket "North Corridor"

---

**1. Recommendation.** **Bid \$23,000,000** (\$95.83/sf; 6.52% going-in cap on year-1 NOI). **Walk away above \$23,100,000.** All cash at closing, with acquisition financing arranged separately and not a condition of the bid. Fifteen-day diligence period; deposit becomes non-refundable at the end of diligence.

**2. Thesis and what is priced.** The asking price of \$24,000,000 (\$100.00/sf; 6.25% cap) prices the building as if exit cap rates five years out will equal today's comparable sales. Our thesis is narrower. The building is a sound income stream with contractual 3% bumps, but at the asking price it does not clear our hurdle once exit-cap risk with two years of remaining term is priced. We are not claiming the seller has misjudged anything. We are declining to pay for an optimistic exit.

**3. Valuation.**

| Item | Value | Source / basis |
|---|---|---|
| Year-1 NOI (after reserves) | \$1,500,000 | Rent roll and lease; audited in diligence (Ch 25 Example 25.1) |
| NOI growth | 3.0% per year | Contractual bumps |
| Forward NOI for reversion (year 6) | \$1,738,911 | $1{,}500{,}000 \times 1.03^5$ |
| Buyer / seller costs | 2.0% / 2.0% | Assumption |
| Hold | 5 years | Year-end cash flows |
| Exit cap scenarios (p) | 6.25% (0.3); 6.75% (0.5); 7.50% (0.2) | Two years of remaining term at exit raises rollover risk |
| Net sale proceeds by scenario | \$27,266,126; \$25,246,413; \$22,721,772 | Forward NOI / cap × 0.98 |

| | At \$24.0m ask | At \$23.0m bid |
|---|---|---|
| Basis incl. 2% | \$24,480,000 | \$23,460,000 |
| Unlevered IRR (6.25% / 6.75% / 7.50% exit) | 8.40% / 7.02% / 5.19% | 9.44% / 8.05% / 6.21% |
| Expected IRR | 7.07% | 8.10% |
| IRR of expected cash flows | 7.09% | 8.13% |

Committee hurdle: 8.0% expected unlevered IRR. **Maximum price meeting the hurdle: \$23,095,880 (6.49% cap).** The walk-away of \$23.1m is that figure rounded.

**4. Capital structure and liquidity.** Indicative financing (Lender 1, B reliability, not committed): 60% LTV, 6.50% fixed, 30-year amortization. At the \$24.0m ask: loan \$14,400,000; debt service \$1,092,214 per year; DSCR 1.37x; debt yield 10.42%; cash-on-cash 4.25%. **Leverage is negative** (6.25% cap below the 6.50% coupon), so the levered return depends on the exit. We will not raise leverage to rescue the return.

**5. Scenarios and downside.** In the 7.50% exit scenario (p = 0.2) the unlevered IRR at our bid is 6.21%. Principal is not impaired: net sale proceeds of \$22.72m plus five years of NOI exceed the basis. Survival is not in question at 60% LTV with a 1.37x DSCR. The risk is opportunity cost, not ruin.

**6. Risks, ranked.**
1. Exit cap / rollover risk (cannot be hedged directly; partially hedgeable with an industrial REIT short at a basis risk we judge too large for this size).
2. Tenant credit (diligence: financials, guarantor).
3. Financing: lender spreads widened about 25 bp this quarter; independence from CMBS distress unresolved (Example 25.3).
4. Data: comparable sales are about four months old and selected (grade C for current pricing).

**7. Why now; why this rather than Treasuries.** At our bid the expected unlevered IRR (8.10%) exceeds the hurdle by 10 bp. That margin is thin. The case for acting now is that we expect few competing bidders, not that the asset is cheap. If competition is stronger than expected, we pass.

**8. Invalidation and exit plan.** We lower the bid or pass if any of the following occurs before signing: (a) the lender conversations show that the spread widening is independent of CMBS distress, which raises P(cap widening ≥ 50 bp) above 50%; (b) the rent-roll audit finds an NOI overstatement above \$25,000; (c) the seller asks for more than \$23.1m.

**9. Counterparty analysis.** The seller is a closed-end fund in its final year (per broker; reliability C). Its need for a timely close, not price discovery, is the source of any discount. Verify the fund's term from public sources if available.

**10. Open diligence items and walk-away conditions.** Tenant financials; estoppel; roof and slab condition report; environmental Phase I; title. Walk-away conditions as in §8.

---

*Decision record ID: DR-25-01 (hypothetical). Forecasts entered in the journal for the next calibration review: P(seller accepts ≤ \$23.0m within 10 days) = 0.45; P(Lender 1 issues a committed term sheet at ≥ 55% LTV by Day 25) = 0.70.*
