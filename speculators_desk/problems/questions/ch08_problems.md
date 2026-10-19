# Chapter 8 Problems — The Fundamental Economics of CRE

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch08_solutions.md`. Numerical answers are verified in `tests/test_ch08_examples.py`.
All facts are hypothetical [HYPOTHESIS] unless cited. In this chapter NOI is before reserves and TI/LC, except for hotels (NOI after FF&E reserve).

---

### Problem 8.1 (Level 1) — What belongs where
For each item, say whether it belongs in PGI, other income (EGI), operating expenses, below NOI (in NCF), or nowhere in the property's cash flow statement. Give a one-line reason, and flag any item whose treatment depends on facts not given.

(a) A \$250,000 lease termination fee paid by a departing office tenant.
(b) Straight-line rent adjustment of +\$140,000 in the seller's GAAP income statement.
(c) Parking-garage income of \$180,000 a year under month-to-month permits.
(d) A \$410,000 roof replacement.
(e) A fee of 1.0% of equity paid by the owning fund to its sponsor.
(f) Leasing commissions on a renewal.
(g) Ground rent of \$120,000 a year under a 60-year ground lease.
(h) Depreciation of \$900,000.
(i) A property-tax refund of \$75,000 from a successful protest of the prior year's appraisal.
(j) Hotel franchise royalty fees.

### Problem 8.2 (Level 2) — Mental arithmetic
Without a calculator:
(a) A submarket has 1.8 million sf vacant and 0.6 million sf of speculative space under construction. Monthly net absorption is 150,000 sf. What are the months of supply?
(b) An asset has an NOI margin of 40% and all of its costs are fixed. Revenue falls 10%. By how much does NOI fall?
(c) A building is 94% leased by area, and tenants on 8% of the leased area are in a free-rent period. All leases are at the same rent per sf. What is economic occupancy?

### Problem 8.3 (Level 2) — Loaded cap rate
Pre-tax NOI is \$850,000. The market cap rate on NOI after reassessed tax is 7.5%. The effective tax rate on price is 2.0%. The seller's current tax bill is \$90,000.
(a) Value with reassessment. (b) Reassessed tax. (c) The value a buyer would compute by capitalizing NOI after the seller's tax bill, and the overpayment in dollars and percent.

### Problem 8.4 (Level 3) — Rent roll of a multi-tenant industrial building
A 100,000 sf building. Leases are NNN; recoverable expenses are \$2.50/sf of building area (\$250,000), and the landlord absorbs the vacant share. Management is 3% of EGI. Non-recoverable costs are \$0.10/sf of building area. Reserves are \$0.15/sf and normalized TI/LC \$0.50/sf, both on building area. Ignore credit loss.

| Tenant | Area (sf) | Rent (\$/sf) | Years remaining | Market rent (\$/sf) |
|---|---:|---:|---:|---:|
| T1 | 40,000 | 7.50 | 5.0 | 8.25 |
| T2 | 25,000 | 8.00 | 1.5 | 8.75 |
| T3 | 15,000 | 9.00 | 3.0 | 9.00 |
| T4 | 10,000 | 8.50 | 0.75 | 9.25 |
| Vacant | 10,000 | — | — | 9.00 |

Compute: (a) physical occupancy and in-place base rent; (b) WALT by rent and by area; (c) the share of base rent rolling within 24 months; (d) total mark-to-market and the part realizable within 24 months; (e) PGI (base rent with vacant at market, plus potential recoveries); (f) EGI, OpEx, NOI, and NCF.

### Problem 8.5 (Level 3) — Net effective rent with escalations
A 10-year office lease on 20,000 sf starts at \$28.00/sf with 3% annual increases. The tenant receives 10 months of free rent at the start, so year-1 cash rent is 2/12 of \$28.00. The landlord pays a \$55/sf TI allowance and leasing commissions of 5% of aggregate cash rent, both at signing. Use annual cash flows in arrears and an 8% discount rate.
Compute per sf: (a) aggregate face rent; (b) aggregate cash rent; (c) LC; (d) PV of cash rent; (e) net effective rent (discounted) and as a percentage of the starting face rent; (f) the straight-line GAAP rent per year. (g) Explain to an investment committee why the broker's "\$28 deal" is not \$28.

### Problem 8.6 (Level 3) — Hotel flow-through
A 120-room select-service hotel runs 68% occupancy at a \$125 ADR (365 days). Other revenue is 6% of rooms revenue; CPOR \$32; other departmental expense ratio 60%; undistributed \$950,000 fixed plus 4% of total revenue; management 3% of total revenue; franchise 10% of rooms revenue; property tax \$190,000; insurance \$110,000; FF&E reserve 4% of total revenue. Use `sdesk.hotel.operating_statement`.
(a) Base RevPAR, total revenue, GOP, and NOI.
(b) RevPAR falls 15%. Compute NOI if the decline is all occupancy, and if it is all ADR. Give NOI flow-through in each case.
(c) Value each case at a 9.5% cap. A lender has a loan of 60% of base value at 7.5%, 25-year amortization, monthly payments. Compute annual debt service and the DSCR in each case.
(d) What does (b)–(c) imply for how a hotel buyer should write a downside scenario?

### Problem 8.7 (Level 4) — Deferred maintenance in a retail center
An 80,000 sf retail center. The seller reports NOI of \$900,000 with no reserve and asks a 7.25% cap (\$12.41 million). The PCA reports: parking lot reconstruction \$350,000 now; a roof replacement of \$600,000 in year 3; HVAC replacements of \$40,000 a year in years 1–5. Your market reserve is \$0.25/sf a year. The market cap rate is 7.25% on NCF. Discount rate 8%. Assume operating expenses are already at market levels and no capital cost is recoverable from tenants.
(a) Compute NCF and stabilized value.
(b) Compute the PV of the roof and of the HVAC spending in excess of the reserve.
(c) Compute the price. Compare it with the ask.
(d) The seller offers a \$350,000 closing credit for the parking lot "and nothing else, since the roof is three years away." Write the counter-proposal, using the structure of Example 8.5. What lease clauses would you check to see whether any of these costs are recoverable from tenants, and how would recoverability change your price?

### Problem 8.8 (Level 4) — Should the developer start?
A multifamily submarket has 12,000 units, 6.0% vacancy, and 1,800 units under construction (none pre-leased) delivering over the next 18 months. Trailing absorption is 100 units a month. A developer proposes 300 more units at \$260,000 per unit all-in. Stabilized NOI is \$16,500 per unit. New stabilized buildings trade at a 5.25% cap. The developer's lender and equity require a 125 bp development spread.
(a) Compute months of supply, and vacancy at 18 months if absorption stays at 100 a month or falls to 60 a month (ignore the proposed project, which would deliver later).
(b) Compute yield on cost, value per unit, value/cost, and the maximum all-in cost per unit that meets the spread requirement.
(c) Recommend start, delay, or abandon, using the rubric in the solutions. What would change your answer?

### Problem 8.9 (Level 4) — Texas versus California
Two buildings each have pre-tax NOI of \$2,000,000. The market cap rate on NOI after reassessed tax is 5.5% in both states [HYPOTHESIS]. In the Texas-style market the effective tax rate on price is 2.40% and value is reassessed at the price. In the California-style market the rate is 1.00% plus 0.22% of voter-approved debt (1.22%) on the new base-year value; the seller's current tax bill is \$60,000.
(a) Value each building with reassessment.
(b) Compute the overpayment of a buyer who capitalizes the California seller's NOI after its \$60,000 tax bill.
(c) Compute year-5 property tax for each buyer if the California base grows 2% a year after year 1 and Texas market value (and assessment) grows 3% a year after year 1.
(d) An investor says: "California is cheaper to own, so I'll pay a lower cap rate there." Evaluate. What is double-counted if the investor also lowers the cap rate?

### Problem 8.10 (Level 5) — The thin offering memorandum
A broker sends a two-page flyer for a 250,000 sf suburban office building in a Texas metro: "92% leased, NOI \$2.4 million, offered at \$30.0 million (8.0% cap). Call for best offers by Friday." The attached rent roll shows that leases on 41% of the area expire within 18 months, including a single 60,000 sf tenant. Outstanding free rent across recent leases totals \$1.1 million. The seller's current appraised value is \$18.0 million and the combined tax rate is 2.3%. You have no information on TI obligations, operating expenses by line, or the 60,000 sf tenant's intentions.
(a) Compute the NOI after reassessing tax at the asking price, and the resulting yield on price.
(b) Compute the loaded-cap value at the broker's 8.0% cap, before and after deducting outstanding free rent.
(c) List the information you would require before bidding, ranked by its effect on value.
(d) Decide whether to bid by Friday. Give your reasoning, and say what you would do instead if you do not bid.
