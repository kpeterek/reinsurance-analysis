# Chapter 8 — The Fundamental Economics of CRE

> **Status:** Complete (v1.0). All numerical examples, problems, and solutions are reproduced in `tests/test_ch08_examples.py`. Problems are in `problems/questions/ch08_problems.md`, solutions in `problems/solutions/ch08_solutions.md`, drills D026–D035 in `training/daily_drills/drill_bank_ch08.json`. Historical facts in §8.9 are registered in `references/sources_ch08.md`; items still open are marked *(verification pending)*.

## Learning objectives

After this chapter you should be able to:

1. Build income from a rent roll through the full waterfall (potential gross income, effective gross income, net operating income, net cash flow) and say for every line item where it belongs and why.
2. Separate cash flow from accounting earnings. Quantify the effect of depreciation, straight-line rent, free rent, and capitalized tenant improvements, and reprice an asset whose marketed NOI is not cash.
3. Distinguish physical, leased, and economic occupancy, and compute net effective rent on a concession-laden lease.
4. Measure operating leverage by property type, and show why a hotel's NOI responds differently to a rate decline than to an occupancy decline.
5. Read a rent roll as a risk document: weighted average lease term, rollover concentration, and mark-to-market.
6. Forecast vacancy in a submarket from inventory, pipeline, and absorption, and convert the result into months of supply.
7. Use replacement cost correctly: as a test of whether new supply can enter, not as a value floor.
8. Value assets under property-tax reassessment with the loaded cap rate, and contrast market-value regimes (Texas) with acquisition-value regimes (California Proposition 13).
9. Price deferred maintenance and distinguish capital expenditure from replacement reserves.
10. Compare hotels, multifamily, office, retail, industrial, land, and specialty property on lease duration, operating leverage, capital intensity, cash-flow volatility, and liquidity, and translate each difference into a pricing or sizing consequence.

---

## 8.1 Opening investment problem: four offering memoranda, four different "NOIs"

You allocate capital for a regional family office with a \$40 million CRE sleeve. On Tuesday four broker packages arrive. Each leads with a single number: NOI capitalized at a cap rate. All facts below are [HYPOTHESIS], a constructed teaching case.

| Asset | Broker's headline | Implied price |
|---|---|---|
| **Oak Hollow**, 48,000 sf grocery-anchored neighborhood retail center | "In-place NOI \$575,000; 7.0% cap" | \$8.2 million |
| **Lakeside Plaza**, 120,000 rsf multi-tenant suburban office | "90% leased; NOI \$1.8 million; 8.0% cap" | \$22.5 million |
| **Interstate select-service hotel**, 150 rooms | "NOI \$1.43 million after 4% FF&E reserve; 9.0% cap" | \$15.9 million |
| **Cedar Court**, 200-unit garden apartments built in the 1980s | "T-12 NOI \$1.45 million; 6.0% cap" | \$24.2 million |

The four headlines look comparable. They are not. One "NOI" is before a reserve and was produced by skipping maintenance. One counts rent that tenants are not paying. One sits on top of fixed costs that will turn a 10% revenue decline into a 20–30% NOI decline. One depends on an anchor whose lease is eight years long while a third of the rest of the rent roll expires within two years. And every one of them carries a property-tax bill that will change when you buy.

This chapter teaches you to take each headline apart. By §8.10 you will reprice all four and decide which deserves diligence money.

---

## 8.2 Economic intuition

### Real estate is a claim on the cash flows of space

A building is a machine that converts space, location, and services into rent. The owner's claim is residual: rent, less the costs of keeping the space rentable, less the share of value claimed by local government through property tax, less the capital needed to keep the machine from wearing out. Value is the present value of that residual claim. Everything in this chapter is about measuring the residual correctly and understanding what makes it volatile.

Three features distinguish CRE cash flows from corporate earnings.

1. **Contracts allocate risk between owner and occupant.** A lease is not just a price. It decides who bears operating-cost inflation (gross versus net leases), who bears demand risk (term length), and who bears capital risk (tenant improvement allowances, repair clauses). A 15-year absolute-net lease to a creditworthy tenant is economically close to a bond with a real estate residual. A hotel "lease" is one night long, so the owner bears everything. The same building can be either, depending on the lease.
2. **Supply is slow and lumpy.** New space takes two to four years to entitle and build [HYPOTHESIS: typical range; varies by type and jurisdiction]. Developers start projects on today's rents and deliver into tomorrow's market. Absorption, the net change in occupied space, adjusts faster than supply. That timing mismatch produces the boom–bust pattern in vacancy that §8.9 documents for Texas in the 1980s.
3. **Value is anchored, loosely, by replacement cost.** When the value of existing buildings rises well above the cost of building new ones, developers build, and the new supply pulls rents and values back. When value is below replacement cost, nothing new is built, and existing owners are protected from new competition until demand catches up. Replacement cost is a long-run attractor for value, not a floor under it.

### The space market and the asset market

It helps to keep two markets separate. In the **space market**, occupants rent space; rent and vacancy are set by the demand for space relative to the stock. In the **asset market**, investors buy claims on rent; cap rates are set by interest rates, risk premia, and expected growth. The construction sector links them: when asset prices exceed replacement cost, new space is built, which feeds back into the space market. This four-part framing is associated with DiPasquale and Wheaton (1992) *(bibliographic verification pending)*. Its practical use is diagnostic. When a value rises, ask which market moved. A rent increase driven by low vacancy is vulnerable to supply. A cap-rate decline driven by cheap debt is vulnerable to rates. They fail in different ways and on different clocks.

### Operating leverage

Operating leverage is the ratio of fixed costs to revenue. A building whose costs are mostly fixed sees NOI move more than revenue. Net-leased industrial has almost no landlord costs, so NOI moves one-for-one with rent. A select-service hotel carries labor, utilities, franchise systems, and maintenance that do not fall when occupancy falls, so NOI moves two to three times as much as revenue. Operating leverage multiplies with financial leverage (Chapter 10): a 10% revenue decline that becomes a 25% NOI decline becomes a 71% equity decline at 65% LTV ($25\% / 0.35$) if cap rates do not move, and cap rates usually do move.

### Cash flow is not earnings

Accounting earnings smooth what cash does not. Straight-line rent recognizes free-rent months as revenue. Tenant improvements are capitalized and amortized instead of expensed. Depreciation is charged on a building that may be appreciating. None of that is wrong for financial reporting, but a buyer pays for cash, and a lender is repaid in cash. The analyst's first job with any income statement is to put each line on a cash basis and then decide which cash is recurring.

### Taxes, capital, and liquidity are claims too

Local government claims a share of value through property tax. In a market-value regime the claim resets to whatever you pay, so the tax line is a function of your bid. The physical building claims a share of cash through capital expenditure; a seller who stops paying that claim inflates NOI and leaves the bill for you. And the market claims a share of value whenever you need to transact quickly. These are the three most common sources of a gap between marketed NOI and the cash a buyer will actually receive.

---

## 8.3 Technical definitions

| Term | Definition |
|---|---|
| Potential gross income (PGI) | Rent the property would collect if 100% leased: in-place contract rent on occupied space plus market rent on vacant space, plus potential expense recoveries |
| Vacancy loss | PGI attributable to unleased space (and, in underwriting, a general allowance for future vacancy) |
| Credit loss | Rent billed but not collected; usually a percentage of income after vacancy |
| Expense recoveries (reimbursements) | Operating expenses billed back to tenants under net or modified-gross leases |
| Effective gross income (EGI) | PGI − vacancy − credit loss + other income |
| Operating expenses (OpEx) | Recurring costs of operating the property: taxes, insurance, utilities, repairs and maintenance, payroll, management, common-area maintenance (CAM). Excludes debt service, depreciation, income tax, and capital items |
| Net operating income (NOI) | EGI − OpEx. **In this chapter NOI is before replacement reserves and leasing costs**, which is the market convention for office, retail, industrial, and multifamily. This is a departure from the notation guide's default; hotels follow the guide's USALI convention, with NOI after the FF&E reserve |
| Net cash flow (NCF) | NOI − replacement reserves − normalized tenant improvements and leasing commissions (TI/LC). Lenders size on NCF |
| Expense ratio | OpEx ÷ EGI |
| Physical occupancy | Occupied area ÷ rentable area |
| Leased occupancy | Area under signed leases ÷ rentable area (includes signed-not-occupied and "dark" tenants) |
| Economic occupancy | Rent actually collected ÷ rent collectible at 100% occupancy at the same rents |
| Net effective rent (NER) | Level annual rent with the same present value as the lease's contractual cash rent less landlord concessions (free rent, TI, LC) |
| Straight-line rent | GAAP revenue recognition that spreads total contractual rent evenly over the lease term, including free-rent periods |
| WALT | Weighted average lease term remaining, weighted by rent (or area) |
| Mark-to-market | (Market rent − contract rent) on leases, in \$ or as a % of contract rent |
| Net absorption | Change in occupied space over a period (move-ins − move-outs) |
| Months of supply | (Vacant space + speculative space under construction) ÷ monthly net absorption |
| Replacement cost | Cost to build an equivalent new property today, including land, hard and soft costs, and (in the "with profit" version) a developer's margin |
| Yield on cost | Stabilized NOI ÷ total development cost |
| Loaded cap rate | $c + t$, where $t$ = property tax as a fraction of value; used when tax is reassessed at the purchase price |
| Replacement reserve | A periodic allowance (per unit, per sf, or % of revenue) for recurring capital replacement |
| Deferred maintenance | Capital or repair work past due at the date of sale |
| Operating leverage (DOL) | Percentage change in NOI per 1% change in revenue |

---

## 8.4 Equations and derivations

### 8.4.1 The income waterfall and what belongs where

$$\text{EGI} = \text{PGI} - \text{Vacancy} - \text{Credit loss} + \text{Other income}$$
$$\text{NOI} = \text{EGI} - \text{OpEx}, \qquad \text{NCF} = \text{NOI} - \text{Reserves} - \text{TI/LC}$$

Each line answers a different question. PGI asks what the rent roll could produce. EGI asks what it does produce. NOI asks what the real estate earns before capital and financing. NCF asks what a lender or owner can actually spend. The classification rules below are where most marketing packages and many internal models go wrong.

| Item | Belongs in | Reason |
|---|---|---|
| Base rent on occupied space | PGI | Contractual income |
| Market rent on vacant space | PGI, then deducted as vacancy | Shows the cost of vacancy explicitly |
| CAM, tax, and insurance reimbursements | PGI (potential recoveries) | Income, offset by the expenses they reimburse |
| Parking, storage, antenna, laundry income | Other income in EGI | Recurring operating income; test its durability |
| Lease termination fee | Exclude from NOI | Non-recurring; it is capital returned for lost future rent |
| Insurance proceeds | Exclude | Non-operating (Case A) |
| Property management fee | OpEx | A market cost even if the owner self-manages |
| Asset management or fund fee | Below NOI | An owner's cost, not the property's |
| Property tax, insurance, utilities, R&M, payroll | OpEx | Recurring operating costs |
| Ground rent | OpEx (or a separate line above NCF) | A senior claim on property cash flow; state treatment |
| Roof replacement, parking-lot resurfacing, HVAC units | Capital, below NOI | Non-recurring in any one year; recurring over the life of the asset, which is what reserves are for |
| Tenant improvements and leasing commissions | Below NOI, in NCF | Costs of acquiring rent; lumpy, tied to rollover |
| Replacement reserve | Below NOI, in NCF (hotel: above NOI per USALI) | An allowance, not a cash payment unless escrowed |
| Debt service | Below NCF | Financing, not operations |
| Depreciation and amortization | Never in NOI | Non-cash accounting allocations |
| Straight-line rent adjustment | Never in NOI | Non-cash; reverse it to get cash rent |
| Owner's income tax | Never in NOI | Depends on the owner, not the asset |

### 8.4.2 Three occupancy measures

Let $A$ be rentable area, $A_{occ}$ occupied area, $A_{lsd}$ leased area, and $r_i$ the contract rent on suite $i$. Then

$$\text{Physical occ.} = \frac{A_{occ}}{A}, \qquad \text{Leased occ.} = \frac{A_{lsd}}{A}, \qquad \text{Economic occ.} = \frac{\sum_i \text{cash rent collected}_i}{\sum_i r_i A_i + \sum_{\text{vacant}} r^{mkt} A_j}.$$

Leased occupancy exceeds physical occupancy when tenants have signed but not moved in, or have moved out but still pay ("dark" tenants). Economic occupancy falls below leased occupancy when tenants are in free-rent periods, in default, or paying below-market rent. A dark tenant is a warning: a tenant who pays for space it does not use is likely to leave at expiry or to seek a buyout. Free rent is a deferred concession: it is a cost the landlord has already agreed to bear.

### 8.4.3 NOI growth is levered rent growth

Write NOI $= R - E$ with revenue $R$ growing at $g_R$ and expenses $E$ growing at $g_E$. Then

$$g_{NOI} = \frac{\Delta R - \Delta E}{R - E} = g_R \frac{R}{NOI} - g_E \frac{E}{NOI}.$$

With $R = 100$, $E = 40$, $g_R = 3\%$, $g_E = 4\%$: $g_{NOI} = 3\% \times 1.667 - 4\% \times 0.667 = 5.00\% - 2.67\% = 2.33\%$. Rent growth above expense growth is magnified, and expense growth above rent growth is magnified in the other direction. The higher the expense ratio, the larger both multipliers. Net leases cut the link: if expenses are fully recovered, $E$ falls out of the landlord's equation and $g_{NOI} \approx g_R$. This is the formal reason that property taxes and insurance, which in recent years have in many markets grown faster than rents [HYPOTHESIS for any specific market; verify locally], matter much more to gross-lease office and to multifamily than to net-leased industrial.

### 8.4.4 Operating leverage

Split costs into fixed $F$ and variable $vR$. Then NOI $= R(1-v) - F$ and

$$\frac{\Delta NOI}{NOI} = \frac{(1-v)\Delta R}{R(1-v) - F} = \frac{\Delta R}{R}\times \underbrace{\frac{R(1-v)}{NOI}}_{DOL}.$$

DOL is contribution margin divided by NOI. It equals 1 when there are no fixed costs and rises without bound as NOI approaches zero. `sdesk.cre.operating_leverage` implements it.

For hotels, revenue changes through two channels with different variable costs. A **rate** (ADR) change carries only percentage-of-revenue costs (fees, reserve, credit-card commissions), so the flow-through to NOI is high. An **occupancy** change also carries cost per occupied room (housekeeping, laundry, amenities, breakfast), so flow-through is lower. Equal RevPAR declines therefore do *not* produce equal NOI declines. A rate-led decline is worse for NOI, and it is also slower to reverse, because ADR rebuilds after occupancy does [HYPOTHESIS: a common operator observation; Chapter 11 examines evidence].

### 8.4.5 Rent rolls: WALT, rollover, mark-to-market, and net effective rent

For leases $i$ with annual contract rent $R_i$, area $A_i$, and remaining term $T_i$:

$$WALT_R = \frac{\sum_i R_i T_i}{\sum_i R_i}, \qquad WALT_A = \frac{\sum_i A_i T_i}{\sum_i A_i}.$$

$$\text{Rollover}(h) = \frac{\sum_{i: T_i \le h} R_i}{\sum_i R_i}, \qquad MTM = \sum_i A_i \left(r^{mkt}_i - r_i\right).$$

WALT is an average and hides concentration. A center whose anchor has eight years left can show a five-year WALT while most of its small-shop rent turns over within two years. Always compute WALT with and without the largest tenant, and the rollover share at 12, 24, and 36 months.

**Net effective rent.** For a lease of $n$ years with cash rent $CR_t$ in year $t$ (after free rent), TI and LC paid at signing, and discount rate $k$:

$$NER = \frac{\sum_{t=1}^{n} CR_t (1+k)^{-t} - TI - LC}{a_{\overline{n}|k}}, \qquad a_{\overline{n}|k} = \frac{1-(1+k)^{-n}}{k}.$$

NER is the level rent with the same present value as the landlord's net receipts. Face rent is a marketing number; NER is the economic rent. We use annual-in-arrears timing for transparency. A monthly model raises the PV of rent slightly and changes no conclusion here.

### 8.4.6 Supply, absorption, and vacancy

Let $S_t$ be inventory, $V_t$ vacant space, $C_t$ completions, and $AB_t$ net absorption over a period. Then

$$V_{t+1} = V_t + C_t - AB_t, \qquad S_{t+1} = S_t + C_t, \qquad v_{t+1} = \frac{V_{t+1}}{S_{t+1}}.$$

**Months of supply** compares what is available with the pace of demand:

$$MOS = \frac{V_t + C^{spec}}{AB^{monthly}},$$

where $C^{spec}$ is speculative (not pre-leased) space under construction. Pre-leased space should not be counted as supply because it is already committed. Its move-ins *do* count in net absorption when the buildings deliver. Analysts who count pre-leased deliveries as supply and also exclude their move-ins from absorption double-penalize the market. Those who count the move-ins as absorption without asking whether the tenants vacated other space in the same submarket double-credit it.

A simple rent-adjustment rule links vacancy to rent growth:

$$g_{rent,t+1} = g^* - \beta (v_t - v^*),$$

where $v^*$ is the "natural" vacancy rate at which real rents are stable. Rents rise when vacancy is below $v^*$ and fall when it is above. This specification is associated with Rosen (1984) and Wheaton and Torto (1988) *(bibliographic verification pending)*. Its parameters differ by market and must be estimated. In this chapter $g^*$, $\beta$, and $v^*$ are [HYPOTHESIS].

### 8.4.7 Replacement cost and the entry condition

Let $H$ be hard cost, $S$ soft cost, and $L$ land, all per unit of space, and let $m$ be the developer's required margin on cost. Then cost $= H + S + L$ and replacement cost with profit $= (H+S+L)(1+m)$. New supply enters when

$$\frac{NOI^{new}}{H+S+L} \;\ge\; c + s \quad\Longleftrightarrow\quad \frac{V^{new}}{H+S+L} = \frac{NOI^{new}/c}{H+S+L} \;\ge\; 1 + \frac{s}{c},$$

where $s$ is the required development spread over the market cap rate and $c$ the cap rate at which a stabilized new building sells. The required rent for feasibility is

$$r^{req} = \frac{(c+s)(H+S+L)}{(1-v)(1-e)},$$

where $v$ is the stabilized vacancy allowance and $e$ the share of revenue lost to non-recoverable costs. When market rent is below $r^{req}$, new construction is not feasible, and existing assets are protected from new competition for at least the length of the construction cycle once the gap closes. That protection is worth something. It is not the same as saying the asset is "worth" replacement cost.

### 8.4.8 Property tax: the loaded cap rate and acquisition-value regimes

**Market-value regime.** If the assessor resets taxable value to the purchase price, tax is $tV$, where $t$ is the combined tax rate times the assessment ratio. With pre-tax NOI $N$ and market cap rate $c$ on after-tax NOI,

$$V = \frac{N - tV}{c} \;\Rightarrow\; V = \frac{N}{c+t}.$$

This is the loaded cap rate of Case A and `sdesk.cre.loaded_cap_value`. Capitalizing the seller's (stale) tax bill instead overstates value by

$$\Delta V = \frac{N - T^{seller}}{c} - \frac{N}{c+t} ,$$

which grows with the gap between the old assessment and the price.

**Acquisition-value regime.** Under California's Proposition 13 the general levy is limited to 1% of taxable value plus voter-approved debt and certain assessments. Taxable value is the base-year value, set at a change in ownership or completion of new construction, and adjusted annually by inflation of no more than 2% [FACT; California State Board of Equalization and county assessor publications; VERIFIED-SECONDARY]. For a buyer, the base year resets to the purchase price, so the loaded-cap logic still applies at acquisition: $V = N/(c + t_{CA})$, with $t_{CA}$ = 1% plus the local debt rate. What differs is what happens *after* acquisition. While market value grows at $g_V$ and taxable value at most at 2%, tax as a share of market value after $n$ years is

$$t_n = t_{CA} \left(\frac{1.02}{1+g_V}\right)^{n}.$$

That drift belongs to the owner and disappears at the next sale. A long-held California asset therefore shows an unusually low tax bill, and its "cap rate" on the seller's NOI is not comparable to anything a buyer can obtain.

**Texas.** Texas appraisal districts appraise property at market value as of 1 January each year, and each taxing unit sets its own rate [FACT; Texas Property Tax Code §1.04 and §23.01 as summarized by county appraisal districts; VERIFIED-SECONDARY]. For tax years 2024 through 2026, a temporary "circuit breaker" limits annual increases in appraised value to 20% for non-homestead real property valued at or below an inflation-indexed threshold (\$5 million for 2024), but only after the owner has held the property for a full prior year [FACT; Tax Code §23.231 as published by appraisal districts; VERIFIED-SECONDARY]. Whether it is extended beyond 2026 is *(verification pending)*. For a buyer of an institutional-size asset, the relevant model is reassessment toward the price. Texas does not require public disclosure of sale prices, so appraisal districts may learn the price with a lag, or through the owner's protest, rather than at closing [INFERENCE consistent with Case A; the timing in any given county is an empirical question]. A prudent buyer underwrites full reassessment in year one and treats any lag as upside.

### 8.4.9 Capital expenditure versus reserves

A replacement reserve is a **budgeting allowance**: an estimate of the average annual cost of replacing short-lived components. Capital expenditure is **cash**. They match only on average over a long horizon. A property sold after years of deferred maintenance has a capital need concentrated at the start of the new owner's hold. Price it as

$$P = \frac{NOI^{norm} - \text{Reserve}}{c} - (1+\kappa)\,\text{Immediate capex} - \sum_{t=1}^{n} \frac{X_t - \text{Reserve}}{(1+k)^t},$$

where $NOI^{norm}$ normalizes operating repairs to market levels, $\kappa$ is a contingency, and $X_t$ is the scheduled catch-up capex in years $1..n$ in excess of the reserve. The perpetual reserve is already in the capitalized income. Only the excess is deducted, so nothing is counted twice.

### 8.4.10 Liquidity: the annualized cost of transacting

With buyer costs $b$ and seller costs $s$ (as fractions of price) and a hold of $T$ years, round-trip costs reduce the annualized return by approximately

$$\text{drag} = 1 - \left(\frac{1-s}{1+b}\right)^{1/T}.$$

With $b = 1.5\%$, $s = 2.5\%$, and $T = 5$: drag $= 1 - (0.975/1.015)^{0.2} = 0.80\%$ per year. Halve the hold and the drag roughly doubles. Illiquidity also has a time dimension that this formula ignores: the months needed to sell, during which the seller is exposed to price changes and cannot redeploy capital. For hotels, land, and special-purpose assets, the buyer pool is thinner and the time to sell is longer than for apartments or industrial [HYPOTHESIS: practitioner observation; transaction-volume data by type would test it].

---

## 8.5 Worked examples

All seven examples use hypothetical inputs [HYPOTHESIS] and are reproduced in `tests/test_ch08_examples.py`.

### Example 8.1 — From rent roll to NCF: Oak Hollow retail center

**Given.** A 48,000 sf neighborhood center. Leases are triple-net (NNN): tenants reimburse their pro-rata share of CAM (\$3.00/sf), real estate taxes (\$2.50/sf), and insurance (\$0.75/sf), a total of \$6.25/sf, or \$300,000 for the building. The anchor's lease caps its CAM contribution at \$2.00/sf. One 6,000 sf suite is vacant, with market rent \$22.00/sf. Credit loss is 1.0% of income after vacancy. Other income (a kiosk and a cell antenna) is \$6,000. Management is 4.0% of EGI and is not recoverable. Other non-recoverable costs are \$18,000. Replacement reserve \$0.20/sf on the whole GLA; normalized TI/LC \$1.25/sf on the 26,000 sf of non-anchor space (shop space plus the vacant suite).

| Tenant | Area (sf) | Rent (\$/sf) | Annual rent | Years remaining | Market rent (\$/sf) |
|---|---:|---:|---:|---:|---:|
| Anchor grocer | 22,000 | 12.00 | 264,000 | 8.0 | 13.00 |
| Fitness | 8,000 | 16.00 | 128,000 | 4.5 | 15.00 |
| Restaurant | 4,000 | 28.00 | 112,000 | 2.0 | 30.00 |
| Salon | 1,500 | 26.00 | 39,000 | 0.5 | 28.00 |
| Dental | 3,500 | 24.00 | 84,000 | 3.0 | 25.00 |
| Mattress retailer | 3,000 | 22.00 | 66,000 | 1.0 | 22.00 |
| **Occupied** | **42,000** | | **693,000** | | |
| Vacant | 6,000 | — | — | — | 22.00 |

**Find.** PGI, EGI, NOI, NCF; the expense ratio; WALT by rent and by area, with and without the anchor; 24-month rollover; mark-to-market.

**Solution.**

*Potential gross income.* Base rent at 100% occupancy $= 693{,}000 + 6{,}000 \times 22 = \$825{,}000$. Potential recoveries $= 300{,}000 - 22{,}000 \times (3.00 - 2.00) = 300{,}000 - 22{,}000 = \$278{,}000$. PGI $= 825{,}000 + 278{,}000 = \$1{,}103{,}000$.

*Vacancy.* The vacant suite forgoes base rent $6{,}000 \times 22 = \$132{,}000$ and recoveries $6{,}000 \times 6.25 = \$37{,}500$: vacancy loss \$169,500, which is 15.37% of PGI. Physical occupancy is $42{,}000/48{,}000 = 87.5\%$, but the economic vacancy rate is higher because the vacant suite would pay above-average rent.

*EGI.* Income after vacancy $= 1{,}103{,}000 - 169{,}500 = \$933{,}500$. Credit loss $= 1\% \times 933{,}500 = \$9{,}335$. EGI $= 933{,}500 - 9{,}335 + 6{,}000 = \$930{,}165$.

*OpEx.* Recoverable expenses \$300,000 (the landlord pays them all and bills tenants); management $4\% \times 930{,}165 = \$37{,}207$; non-recoverable \$18,000. Total OpEx $= \$355{,}207$. Expense ratio $= 355{,}207/930{,}165 = 38.19\%$.

*NOI* $= 930{,}165 - 355{,}207 = \$574{,}958$.

*NCF.* Reserve $= 0.20 \times 48{,}000 = \$9{,}600$. TI/LC $= 1.25 \times 26{,}000 = \$32{,}500$. NCF $= 574{,}958 - 9{,}600 - 32{,}500 = \$532{,}858$.

*Unrecovered "recoverables".* The landlord pays \$300,000 of recoverable expenses and collects \$240,500 ($278{,}000 - 37{,}500$). The \$59,500 shortfall is the vacant suite's share (\$37,500) plus the anchor cap (\$22,000). A net lease is only as net as its least-net tenant.

*Rent roll risk.*

* $WALT_R = (264{,}000 \times 8 + 128{,}000 \times 4.5 + 112{,}000 \times 2 + 39{,}000 \times 0.5 + 84{,}000 \times 3 + 66{,}000 \times 1)/693{,}000 = 3{,}249{,}500/693{,}000 = 4.69$ years.
* $WALT_A = 234{,}250/42{,}000 = 5.58$ years.
* Excluding the anchor: $WALT_R = 1{,}137{,}500/429{,}000 = 2.65$ years.
* The anchor pays 38.1% of base rent.
* Rollover within 24 months (restaurant, salon, mattress): \$217,000, which is 31.3% of base rent.
* Mark-to-market: market rent on occupied space \$721,500 versus contract \$693,000, so leases are 4.11% (\$28,500) below market. But \$22,000 of that gap sits in the anchor lease, which does not roll for eight years. The mark-to-market realizable within 24 months is \$11,000.

**Check.** NOI rebuilt from the tenants' side: base rent collected 693,000 + recoveries 240,500 + other 6,000 − credit loss 9,335 = 930,165 = EGI. ✓ The broker's \$575,000 "in-place NOI" is our NOI, before reserves and TI/LC. The broker's price, \$8.2 million, is NOI/7.0% = \$8,213,691, and on NCF the same price is a 6.49% yield.

**Decision consequence.** The headline cap rate is computed on the wrong line for comparison with lender-underwritten deals, which use NCF. More important is the shape of the risk: the center is two different assets. One is an eight-year anchor lease at slightly below market, which behaves like a bond. The other is 26,000 sf of shop space and vacancy with a 2.65-year WALT, 31% of rent rolling in 24 months, and only \$11,000 of near-term mark-to-market to offset leasing costs. Underwrite the shop space with explicit downtime, TI/LC, and renewal probabilities (Chapter 9's DCF), and price the anchor's renewal option as a risk, not as an upside. A lender will also apply a market vacancy allowance to the shop space even if it is full.

*Reproduce:* `tests/test_ch08_examples.py::test_example_8_1`

### Example 8.2 — Lakeside Plaza: physical, leased, and economic occupancy; cash versus GAAP

**Given.** A 120,000 rsf suburban office building with full-service gross leases at \$30.00/sf; building operating expenses of \$12.00/sf (\$1,440,000) are paid by the landlord. Of the space:

* 78,000 sf is occupied and paying \$30.00/sf;
* 30,000 sf is under new 10-year leases at \$30.00/sf flat, signed this month, with 12 months of free rent, a \$60/sf TI allowance, and leasing commissions of 6% of aggregate cash rent, all paid at signing;
* 6,000 sf of the 78,000 sf paying tenant base is "dark": the tenant has moved out but pays rent until expiry;
* 12,000 sf is vacant.

Discount rate for NER: 8%. Annual cash flows in arrears.

**Find.** The three occupancy measures; cash NOI for the coming year; the "contract" NOI the broker capitalized; straight-line NOI; the NER of the new leases; and the year-1 difference between cash and GAAP for the new-lease block.

**Solution.**

*Occupancy.* Leased $= (78{,}000 + 30{,}000)/120{,}000 = 90.0\%$. Physically occupied space excludes the dark suite and includes the new tenants, who move in now: $(78{,}000 - 6{,}000 + 30{,}000)/120{,}000 = 85.0\%$. Economic occupancy in the coming year $= 78{,}000 \times 30/(120{,}000 \times 30) = 65.0\%$.

*Three NOIs for the same year.*

| Basis | Rent | − OpEx | NOI |
|---|---:|---:|---:|
| Cash (what will be collected) | $78{,}000 \times 30 = 2{,}340{,}000$ | 1,440,000 | **900,000** |
| Straight-line (GAAP) | $2{,}340{,}000 + 30{,}000 \times 27 = 3{,}150{,}000$ | 1,440,000 | **1,710,000** |
| "Contract" (broker) | $108{,}000 \times 30 = 3{,}240{,}000$ | 1,440,000 | **1,800,000** |

Straight-line rent on the new leases is total cash rent over the term divided by the term: $(9 \times 30)/10 = \$27.00$/sf per year, recognized even in the free-rent year.

*Net effective rent of the new leases (per sf).* Aggregate face rent \$300; free rent \$30; cash rent \$270; LC $= 6\% \times 270 = \$16.20$.

* Undiscounted NER $= (270 - 60 - 16.20)/10 = \$19.38$.
* PV of cash rent (years 2–10 at \$30): $30 \times (a_{\overline{10}|8\%} - 1.08^{-1}) = 30 \times (6.71008 - 0.92593) = \$173.52$.
* Discounted NER $= (173.52 - 60 - 16.20)/6.71008 = \$14.50$/sf per year, **48.3% of face rent**.

*Cash versus GAAP for the 30,000 sf block in year 1.* Cash: rent 0; TI $-\$1{,}800{,}000$; LC $-\$486{,}000$; net $-\$2{,}286{,}000$. GAAP: straight-line revenue \$810,000; TI amortization $-\$180{,}000$ (\$6/sf over 10 years); LC amortization $-\$48{,}600$; net $+\$581{,}400$. The difference is \$2,867,400 in a single year.

**Check.** Over ten years straight-line and cash rent agree: $10 \times 27 = 270 = 9 \times 30$. ✓ TI amortization sums to the TI paid. ✓ The differences are purely timing, and timing is what a buyer pays for.

**Decision consequence.** The broker's \$22.5 million is the contract NOI at 8.0%. A buyer who closes today inherits the 12 months of free rent (\$900,000 of foregone cash) unless the seller credits it at closing; a credit reduces the price to \$21.6 million on the broker's own cap rate. The building's cash NOI next year supports only \$11.25 million at the same cap rate. The truth for value lies between, and Chapter 9's DCF finds it. The economic lesson is that the market rent of \$30 is not the economic rent. The landlord is effectively leasing at \$14.50 after concessions. Comparable sales whose cap rates were computed on face rents will overstate what this market pays for office income. The 6,000 sf dark suite should be underwritten as vacant at its expiry, and a lender will treat it that way.

*Reproduce:* `tests/test_ch08_examples.py::test_example_8_2`

### Example 8.3 — Operating leverage: select-service hotel versus a net-leased building under a 10% revenue shock

**Given.** *Hotel:* 150 rooms, 72% occupancy, \$140 ADR, 365 days. Other revenue 6% of rooms revenue. Rooms cost per occupied room (CPOR) \$32. Other departmental expense ratio 60%. Undistributed expenses: \$1,350,000 fixed plus 4% of total revenue. Management fee 3% of total revenue; franchise fees 10% of rooms revenue. Property tax \$260,000; insurance \$150,000. FF&E reserve 4% of total revenue (NOI after reserve, per the notation guide). Cap rate 9.0%.
*Net-lease building:* \$1,000,000 of rent; landlord's non-recoverable costs \$20,000 fixed. Cap rate 6.5%.
Both are financed at 65% LTV. Cap rates are held constant to isolate operating leverage.

**Find.** NOI and value before and after a 10% revenue decline; for the hotel, compare a decline led by ADR with one led by occupancy; equity impact at 65% LTV.

**Solution (hotel base case, via `sdesk.hotel.operating_statement`).**

| Line | Base | ADR −10% | Occupancy −10% |
|---|---:|---:|---:|
| Occupancy / ADR | 72.0% / \$140 | 72.0% / \$126 | 64.8% / \$140 |
| Rooms sold | 39,420 | 39,420 | 35,478 |
| Rooms revenue | 5,518,800 | 4,966,920 | 4,966,920 |
| Total revenue | 5,849,928 | 5,264,935 | 5,264,935 |
| Rooms expense | 1,261,440 | 1,261,440 | 1,135,296 |
| GOP | 2,805,814 | 2,264,089 | 2,390,233 |
| Management + franchise | 727,378 | 654,640 | 654,640 |
| EBITDA | 1,668,436 | 1,199,449 | 1,325,593 |
| FF&E reserve | 233,997 | 210,597 | 210,597 |
| **NOI** | **1,434,439** | **988,851** | **1,114,995** |
| NOI change | — | −31.06% | −22.27% |
| NOI flow-through on lost revenue | — | 76.2% | 54.6% |

Base GOP margin is 48.0% and NOI margin 24.5%. Value at 9.0% $= \$15{,}938{,}212$.

*Net lease (via `sdesk.cre.operating_leverage`).* NOI $= 1{,}000{,}000 - 20{,}000 = 980{,}000$. After a 10% rent decline, NOI $= 880{,}000$, a change of −10.20%. DOL $= 1{,}000{,}000/980{,}000 = 1.02$.

*Equity at 65% LTV.* With debt fixed, the percentage change in equity is the value change divided by 0.35:

| Asset | Value change | Equity change |
|---|---:|---:|
| Net lease | −10.20% | −29.15% |
| Hotel, occupancy-led | −22.27% | −63.63% |
| Hotel, ADR-led | −31.06% | −88.75% |

**Check.** Occupancy-led flow-through: the lost 3,942 room-nights save $3{,}942 \times 32 = \$126{,}144$ of rooms expense, and the rest of the lost revenue flows through at the percentage-cost margin. ADR-led: no rooms cost is saved. The two NOIs differ by exactly \$126,144 ($1{,}114{,}995 - 988{,}851$). ✓

**Decision consequence.** "A 10% revenue decline" is not one number for a hotel. A rate war that cuts ADR by 10% costs a third of NOI; the same RevPAR loss through occupancy costs a fifth. At 65% LTV the ADR-led shock nearly eliminates equity even before cap rates widen, and in a hotel downturn they do widen. The net-leased building's DOL near 1 does not make it riskless: its revenue risk is concentrated in one tenant's credit and renewal, so its revenue distribution is close to binary (rent paid or building dark) rather than continuous. Size hotel leverage to survive a rate-led decline with wider cap rates (Chapter 11), and size net-lease leverage to survive the loss of the tenant (Chapter 10).

*Reproduce:* `tests/test_ch08_examples.py::test_example_8_3`

### Example 8.4 — Months of supply and a vacancy forecast for an industrial submarket

**Given.** Inventory 40.0 million sf; vacancy 7.5%. Under construction: 4.0 million sf, all delivering within 12 months, 30% pre-leased. Trailing-12-month net absorption 3.6 million sf (300,000 sf per month). Your base case: absorption slows to 200,000 sf per month as e-commerce occupiers pause. Natural vacancy $v^* = 7.5\%$. Rent rule $g = 3.0\% - 0.8\,(v - 7.5\%)$ [HYPOTHESIS for both].

**Find.** Months of supply at each absorption pace; vacancy in 12 months; months needed after that to return to 7.5%; implied rent growth.

**Solution.**

Vacant space $= 0.075 \times 40.0 = 3.0$ million sf. Speculative pipeline $= 4.0 \times 0.70 = 2.8$ million sf.

| | Trailing pace | Base case |
|---|---:|---:|
| Monthly absorption (m sf) | 0.30 | 0.20 |
| Months of supply $= (3.0 + 2.8)/AB$ | 19.3 | 29.0 |
| Vacant space in 12 months $= 3.0 + 4.0 - 12 \times AB$ | 3.4 | 4.6 |
| Inventory in 12 months | 44.0 | 44.0 |
| Vacancy in 12 months | 7.73% | 10.45% |
| Excess over 7.5% ($0.075 \times 44.0 = 3.3$) | 0.1 | 1.3 |
| Further months to return to 7.5% (no new starts) | 0.3 | 6.5 |
| Rent growth from the rule | 2.82% | 0.64% |

Absorption here includes the move-ins of pre-leased tenants (1.2 million sf), which is consistent with counting the whole 4.0 million sf of completions in the vacancy identity.

**Check.** At the trailing pace, 12 months absorb 3.6 million sf against 4.0 million sf of completions, so vacant space rises by 0.4 million sf (3.0 → 3.4); vacancy rises only 23 bp because inventory also grows. ✓

**Decision consequence.** The market's headline vacancy of 7.5% says nothing about the next year. What matters is the pipeline relative to the demand pace. A one-third slowdown in absorption moves 12-month vacancy from 7.7% to 10.5% and rent growth from about 2.8% to about 0.6% under the rule. An acquisition priced on 3% rent growth is therefore a bet on absorption holding at the trailing pace. Before bidding, verify three things: whether pre-leased tenants are relocating within the submarket (if so, net absorption is overstated and vacancy will be higher); whether any announced projects have not yet started (if starts continue, the excess persists); and what the leasing pipeline of the specific competing buildings shows.

*Reproduce:* `tests/test_ch08_examples.py::test_example_8_4`

### Example 8.5 — Deferred maintenance capitalized into price: Cedar Court apartments

**Given.** 200 units. Seller's T-12 NOI \$1,450,000, before reserves. The property condition assessment (PCA) finds that repairs and maintenance were underspent by \$80,000 a year relative to comparable properties. It identifies \$1,200,000 of immediate needs (roofs, boilers, life-safety items) and \$400,000 a year of scheduled replacements in years 1–5 (windows, unit HVAC). A market replacement reserve is \$300 per unit per year. Market cap rate 6.0% on NOI after reserves. Contingency on immediate work 10%. Discount rate for catch-up capex 8%.

**Find.** Normalized NOI and NCF; the stabilized value; the deduction for capital catch-up; the price; the gap from the broker's \$24.2 million.

**Solution.**

* Normalized NOI $= 1{,}450{,}000 - 80{,}000 = \$1{,}370{,}000$.
* Reserve $= 300 \times 200 = \$60{,}000$. NCF $= \$1{,}310{,}000$.
* Stabilized value $= 1{,}310{,}000/0.06 = \$21{,}833{,}333$.
* Immediate capex with contingency $= 1{,}200{,}000 \times 1.10 = \$1{,}320{,}000$.
* Catch-up in excess of the reserve: $400{,}000 - 60{,}000 = \$340{,}000$ a year for 5 years. PV $= 340{,}000 \times a_{\overline{5}|8\%} = 340{,}000 \times 3.99271 = \$1{,}357{,}521$.
* Price $= 21{,}833{,}333 - 1{,}320{,}000 - 1{,}357{,}521 = \$19{,}155{,}812$, or \$95,779 per unit.

Broker's price $= 1{,}450{,}000/0.06 = \$24{,}166{,}667$ (\$120,833 per unit). The gap is \$5,010,855, or 20.7% of the broker's price.

**Check.** Decompose the gap: reserve not deducted, $60{,}000/0.06 = \$1{,}000{,}000$; underspent R&M, $80{,}000/0.06 = \$1{,}333{,}333$; immediate capex \$1,320,000; excess catch-up \$1,357,521. Sum $= \$5{,}010{,}855$. ✓ At the broker's price the buyer's yield on NCF would be $1{,}310{,}000/24{,}166{,}667 = 5.42\%$ before any capex.

**Decision consequence.** Two of the four pieces of the gap are capitalized at the cap rate because they are permanent (the reserve and normal R&M); two are deducted dollar for dollar because they are one-time. Mixing these up is the most common error in pricing deferred maintenance. Capitalizing a one-time \$1.32 million roof bill at 6% would deduct \$22 million. Ignoring the R&M normalization would leave \$1.33 million of value that does not exist. Negotiate in the same structure: price for the permanent items, and a credit or escrow for the one-time items. A lender will usually require an up-front escrow for immediate repairs and will size on NCF, so the broker's price is also unfinanceable on normal terms.

*Reproduce:* `tests/test_ch08_examples.py::test_example_8_5`

### Example 8.6 — Reassessment in a market-value regime versus an acquisition-value regime

**Given.** Two otherwise identical buildings, each with pre-tax NOI $N = \$1{,}000{,}000$ and a market cap rate of 6.0% on NOI after reassessed tax. Hold the cap rate equal across states to isolate the tax effect.

* *Texas-style:* combined rate 2.20% of market value; appraisal at 100% of market value, reset toward the price, so $t = 2.20\%$. The seller's current appraisal is \$8.0 million.
* *California-style:* 1.00% general levy plus 0.15% of voter-approved debt, so $t = 1.15\%$ on the purchase price as the new base-year value. The seller's base-year value is \$4.0 million after decades of ownership.

[HYPOTHESIS: the rates are illustrative. Actual Texas rates vary by the combination of taxing units; California debt rates vary by tax rate area.]

**Find.** Value under each regime; the error from capitalizing the seller's tax bill; the drift of the California tax rate after 10 years if market value grows 4% a year.

**Solution.**

| | Texas-style | California-style |
|---|---:|---:|
| $t$ | 2.20% | 1.15% |
| Value $N/(c+t)$ | \$12,195,122 | \$13,986,014 |
| Reassessed tax $tV$ | \$268,293 | \$160,839 |
| Seller's tax bill | $8.0\text{m} \times 2.20\% = \$176{,}000$ | $4.0\text{m} \times 1.15\% = \$46{,}000$ |
| "Value" on seller's tax $(N - T^{seller})/c$ | \$13,733,333 | \$15,900,000 |
| Overpayment | \$1,538,211 (12.6%) | \$1,913,986 (13.7%) |

With no property tax at all, value would be $1{,}000{,}000/0.06 = \$16{,}666{,}667$. The California-style building is worth 14.7% more than the Texas-style building at the same cap rate, purely because of the lower tax rate.

*Drift.* After 10 years, $t_{10} = 1.15\% \times (1.02/1.04)^{10} = 0.947\%$ of market value, if the 2% inflation cap binds every year.

**Check.** Texas: $(1{,}000{,}000 - 268{,}293)/12{,}195{,}122 = 6.00\%$. ✓ California: $(1{,}000{,}000 - 160{,}839)/13{,}986{,}014 = 6.00\%$. ✓

**Decision consequence.** Both regimes reset tax at acquisition, so the loaded cap applies to both, and both punish the buyer who capitalizes the seller's bill. The California error is larger here because a long-held base year makes the seller's tax bill tiny. In California the tax advantage of a long hold is the owner's and not transferable, so cap rates computed from sellers' NOIs are not comparable to buyers' cap rates. In Texas the error comes from appraisal lag, and its size depends on how far the appraisal district's value trails the market. The comparison also explains a cross-state pricing pattern: holding cap rates equal, high-tax jurisdictions support lower prices per dollar of pre-tax NOI. A buyer comparing a Dallas and a Sacramento asset should compare loaded cap rates, $c + t$, not headline cap rates.

*Reproduce:* `tests/test_ch08_examples.py::test_example_8_6`

### Example 8.7 — Replacement cost as an entry test: bulk industrial

**Given.** Per sf of building: hard cost \$110, soft cost 20% of hard, land \$18, developer margin 15% on cost. Market rent \$9.00/sf NNN; stabilized vacancy 5%; non-recoverable costs 3% of revenue. Stabilized new buildings sell at a 5.75% cap. Developers require a 125 bp spread of yield on cost over the cap rate. An existing building of similar quality is offered at \$130/sf.

**Find.** Cost and replacement cost with profit; yield on cost; value per sf of a stabilized new building; the rent needed for new supply; the existing building's discount to cost.

**Solution.**

* Cost $= 110 + 22 + 18 = \$150$/sf. Replacement cost with profit $= 150 \times 1.15 = \$172.50$/sf.
* Stabilized NOI per sf $= 9.00 \times 0.95 \times 0.97 = \$8.2935$.
* Yield on cost $= 8.2935/150 = 5.53\%$, below the 5.75% cap, let alone the 7.00% required.
* Stabilized value $= 8.2935/0.0575 = \$144.23$/sf. Value/cost $= 0.962$; value/replacement cost with profit $= 0.836$.
* Required rent $= (0.0575 + 0.0125) \times 150/(0.95 \times 0.97) = \$11.39$/sf, which is 26.6% above market.
* The existing building at \$130/sf is 86.7% of cost (13.3% below) and yields $8.2935/130 = 6.38\%$ if leased at market.

**Check.** At \$11.39 rent, NOI $= 11.394 \times 0.95 \times 0.97 = \$10.50$, and $10.50/150 = 7.00\%$. ✓

**Decision consequence.** New supply will not start until rents rise roughly 27%, construction costs fall, or cap rates compress about 125 bp. That is a real protection for the existing building, and it supports underwriting below-average competitive deliveries for the length of a construction cycle *after* the gap closes. It does not mean the existing building is "worth" \$172.50. Its value is set by its income: at market rent and a 5.75% cap it is worth about \$144/sf stabilized, and the \$130 offer is attractive only if lease-up costs and downtime are less than the \$14/sf difference. Sellers who quote replacement cost as a floor (Case A) are confusing a supply condition with a valuation.

*Reproduce:* `tests/test_ch08_examples.py::test_example_8_7`

---

## 8.6 CRE application: comparing the property types

The property types differ systematically in who bears which risk. The table below combines a computed operating-leverage illustration with qualitative characteristics. The archetype cost structures and all "typical" ranges are [HYPOTHESIS] for teaching. They are chosen to be representative, but no dated market source is cited for them, so verify them locally before use.

### 8.6.1 Operating leverage by archetype (computed)

Each archetype is a stylized revenue and cost structure. "10% revenue shock" means revenue falls 10% with fixed costs unchanged. DOL is from `sdesk.cre.operating_leverage` except for the hotel, which uses the full USALI model of Example 8.3.

| Archetype | Revenue | Fixed costs | Variable cost (% rev.) | NOI | NOI margin | NOI change, −10% revenue | DOL |
|---|---:|---:|---:|---:|---:|---:|---:|
| Single-tenant net lease | 1,000,000 | 20,000 | 0% | 980,000 | 98.0% | −10.20% | 1.02 |
| Multi-tenant industrial (NNN) | 2,000,000 | 60,000 | 3% | 1,880,000 | 94.0% | −10.32% | 1.03 |
| Self-storage (specialty) | 2,000,000 | 640,000 | 6% | 1,240,000 | 62.0% | −15.16% | 1.52 |
| Multifamily | 3,000,000 | 1,110,000 | 8% | 1,650,000 | 55.0% | −16.73% | 1.67 |
| Multi-tenant office (gross) | 3,600,000 | 1,440,000 | 3% | 2,052,000 | 57.0% | −17.02% | 1.70 |
| Select-service hotel, occupancy-led | 5,849,928 | — | — | 1,434,439 | 24.5% | −22.27% | 2.23 |
| Select-service hotel, ADR-led | 5,849,928 | — | — | 1,434,439 | 24.5% | −31.06% | 3.11 |

For the hotel, "DOL" is the measured ratio of the NOI change to the revenue change. Two caveats apply. First, NOI margin and DOL are linked: low-margin assets are high-DOL assets. Second, the size of the shock is not the same across types. A 10% revenue decline is an ordinary year for a hotel and a severe event for a net-leased warehouse. Risk is DOL times the volatility of revenue, and the property types differ in both.

### 8.6.2 Land: negative carry and pure optionality

Raw land produces no NOI. Its holder pays carry and owns an option on future development (Chapter 13, Case I). For a \$5,000,000 parcel with property tax at 2.2% (\$110,000), insurance and maintenance of \$15,000, and an 8% opportunity cost of capital (\$400,000), the annual carry is \$525,000, or **10.5% of value**. Land must appreciate about 10.5% a year just to break even against the alternative use of the capital. Note also that agricultural land in Texas may be appraised at productivity value rather than market value [FACT; Texas appraisal district summaries of the Tax Code; VERIFIED-SECONDARY], so a change of use can trigger a much higher tax and, under Texas law, rollback taxes *(rollback details verification pending)*. This is why land is the most speculative CRE asset: its return is almost entirely price change, and the carry runs against you while you wait.

### 8.6.3 Systematic comparison

| Dimension | Hotel | Multifamily | Office | Retail | Industrial | Land | Specialty (storage, seniors, data centers) |
|---|---|---|---|---|---|---|---|
| Lease duration | One night | About 12 months | 5–10+ years | Anchors 10–20 years; shops 3–5 | 3–10 years; bulk often longer | None | Storage monthly; seniors monthly with care contracts; data centers often long |
| Who bears opex inflation | Owner | Owner (mostly) | Owner above base year under gross leases | Tenants (NNN), subject to caps | Tenants (NNN) | Owner (tax, insurance) | Owner |
| Operating leverage | Very high | Moderate | Moderate to high | Low to moderate | Low | n/a (negative carry) | Moderate to very high (seniors is an operating business) |
| Capex intensity | High: FF&E reserve 4% of revenue plus brand PIPs | Moderate: unit turns, roofs, systems | High: TI/LC on every rollover | Moderate: TI for shops, parking, roofs | Low: roofs, paving, dock equipment | Low until development | Varies widely |
| Cash-flow volatility | Highest; reprices daily | Low to moderate; reprices annually | Low in term, very high at rollover | Bimodal: anchors stable, shops cyclical | Low | None (no cash flow) | Varies with operator and contract |
| Liquidity (buyer pool, time to sell) | Thinner; brand and PIP diligence lengthen the process | Deepest; agency financing widely available | Narrowed sharply after 2020 for commodity suburban office *(verification pending for volume data)* | Moderate; anchors drive financeability | Deep | Thin; long marketing times | Thin; specialist buyers |
| Key underwriting variable | RevPAR and flow-through | Rent growth vs expense growth | Rollover, TI/LC, NER | Anchor health, co-tenancy, sales per sf | Supply pipeline, clear height, location | Entitlement and timing | Operator quality |

All entries in this table are [HYPOTHESIS] teaching generalizations. The one consistent pattern is that short leases transfer market risk to the owner quickly, which raises cash-flow volatility but also lets rents reset upward quickly in inflation. Long leases protect cash flow in downturns but lock in rent in inflations unless they have CPI escalators. "Defensive" and "inflation-protected" are opposite ends of the same choice.

### 8.6.4 Expense ratios and what they tell you

Expense ratio = OpEx/EGI. In Example 8.1 it is 38.2%. The number is meaningless without the lease structure: NNN properties gross up EGI with recoveries, so their expense ratios look high even though the landlord bears little expense risk. Compare properties only on the same basis, preferably the **landlord-borne** expense ratio: unrecovered OpEx ÷ EGI. In Example 8.1 the landlord bears \$59,500 of unrecovered recoverables plus \$55,207 of management and non-recoverable costs, a total of \$114,707, or 12.3% of EGI. That is the operating leverage that matters.

---

## 8.7 Cash flow versus accounting earnings: a reconciliation discipline

Investors read REIT filings, appraisals, and seller statements prepared on different bases. Reconcile every income figure to cash using five adjustments.

1. **Depreciation and amortization.** Remove them entirely. Under current federal tax law, residential rental property is depreciated straight-line over 27.5 years and nonresidential real property over 39 years [FACT; IRS Publication 946 as summarized by secondary sources; VERIFIED-SECONDARY; check the current publication before relying on table values]. Depreciation affects the owner's income tax, which is an owner-level item, but it does not affect NOI.
2. **Straight-line rent.** Reverse the straight-line adjustment to get cash rent. In a portfolio with many recent leases with free rent, GAAP revenue exceeds cash rent. In a portfolio of old leases with fixed bumps, cash rent exceeds GAAP revenue late in the leases.
3. **Free rent.** Identify outstanding free rent at closing and require a credit, or deduct its PV from price (Example 8.2).
4. **TI and LC.** Treat them as capital at the time they are paid. On a stabilized basis, reserve for them per rentable sf, consistent with expected rollover.
5. **Non-recurring items.** Remove lease termination fees, insurance recoveries, real estate tax refunds from prior-year protests, and one-time expense savings.

REIT disclosures make the same point in their own vocabulary. Funds from operations adds back real estate depreciation to net income; adjusted measures then deduct straight-line rent and recurring capital. The conceptual chain is the same as the waterfall in §8.4.1. Definitions of these measures vary by company, so always read the reconciliation table.

---

## 8.8 When the relationships fail

1. **The rent roll is not the lease.** Rent rolls are summaries prepared by the seller's manager. Kick-out clauses, co-tenancy rights, exclusives, termination options, and expense caps live in the lease documents and estoppel certificates. A WALT computed to the stated expiry overstates term when tenants hold early termination options.
2. **Natural vacancy moves.** The rent-adjustment rule assumes a stable $v^*$. Structural change in how space is used shifts it. Post-2020 office demand is the obvious example: a vacancy rate that would once have signaled rent recovery may now be the new normal, and rent rules calibrated on older data will forecast recoveries that do not come [INFERENCE].
3. **Absorption can be negative while leasing is positive.** Gross leasing counts signed leases; net absorption counts occupancy changes. In a consolidation wave tenants sign smaller leases. Leasing volume looks healthy while occupied space shrinks.
4. **Replacement cost can fall.** When construction costs or land prices fall, or when a new building type (taller clear heights, better energy performance) makes older stock functionally obsolete, the replacement-cost "protection" evaporates. Value relative to *functional* replacement cost is what matters.
5. **Operating leverage can be reduced, at a price.** Hotels can cut labor and close floors; owners of gross-leased office can convert to net leases at renewal. Fixed costs are fixed only over the horizon in which contracts and labor arrangements cannot be changed. Over long horizons all costs are variable, and the ability to cut is part of the asset's option value.
6. **Tax regimes change.** Assessment caps, circuit breakers, and exemptions are set by legislatures and voters, and they change. Texas's 20% circuit breaker is explicitly temporary. Underwrite the statute in force, but stress-test the version that is less favorable to you.
7. **Reserves are fiction until funded.** A reserve deducted in a valuation is not cash in an account. Owners who distribute reserves, as most do, still face the capital bill when it comes, and it comes in lumps.
8. **Liquidity is regime-dependent.** In a credit contraction, transaction volume falls, bid–ask spreads widen, and the "market cap rate" is set by a handful of trades by motivated sellers (Chapter 2). The transaction-cost drag formula understates illiquidity because the cost of not being able to sell at all is not a percentage of price.

---

## 8.9 Historical episode: Texas commercial real estate, 1981–1995

### Date and environment

[FACT] In the early 1980s federal tax policy raised the after-tax return on commercial real estate. The FDIC's history of the banking crises states that tax breaks enacted in the Economic Recovery Tax Act of 1981 greatly enhanced the after-tax returns on real estate investment, contributing to a construction boom (FDIC, *History of the Eighties*, vol. 1, ch. 3; VERIFIED-SECONDARY via excerpt). The 1981 Act shortened the tax recovery period for commercial real estate to 15 years (Tax Foundation; VERIFIED-SECONDARY). Later legislation in the mid-1980s lengthened recovery periods again; the exact sequence is reported differently by secondary sources *(verification pending)*.

[FACT] The Tax Reform Act of 1986 extended the recovery period for nonresidential real property to 31.5 years and for residential rental property to 27.5 years, required straight-line depreciation, and restricted the use of passive losses to offset other income (Tax Foundation; Federal Reserve Bank of Boston conference paper; both VERIFIED-SECONDARY).

[FACT] In Texas the boom coincided with an energy-driven economy. The FDIC attributes the high failure rate of Texas banks to the rapid rise and subsequent collapse of oil prices, together with real estate, agricultural, and branching factors (FDIC, *History of the Eighties*, vol. 1, ch. 1 and ch. 9; VERIFIED-SECONDARY). The specific oil price path is not quoted here *(verification pending against EIA or FRED series)*.

### What happened in the space market

* [FACT] Office vacancy in Dallas rose from about 8% in 1980 to 28% in 1987 (FDIC, *History of the Eighties*, vol. 1, ch. 9; VERIFIED-SECONDARY via excerpt). A later FDIC regional publication describes Dallas office vacancy as peaking above 27% in 1988 (FDIC *Regional Outlook*, 2000; VERIFIED-SECONDARY). The two FDIC sources differ on the peak year by one year, which is consistent with different data vendors or definitions; we do not resolve it.
* [FACT] Texas commercial real estate growth outpaced office employment growth from 1982 to 1987, producing a combined office vacancy rate of about 30% by 1987 in the Austin, Dallas, Houston, and San Antonio areas (O'Keefe, *The Texas Banking Crisis: Causes and Consequences, 1980–1989*, FDIC, via FRASER; VERIFIED-SECONDARY).
* [FACT] Austin's office vacancy rate reached 39.5% in 1987, described as the highest ever recorded in the state (Federal Reserve Bank of Dallas, *Southwest Economy*, 1995; VERIFIED-SECONDARY).
* [FACT] The FDIC notes that office vacancies were already rising in the early 1980s while construction remained high (FDIC, *History of the Eighties*, vol. 1, ch. 9; VERIFIED-SECONDARY via excerpt).

### What happened to the lenders

* [FACT] 425 Texas commercial banks failed or required assistance between 1980 and 1989, including nine of the state's ten largest bank holding companies (FDIC, *History of the Eighties*, vol. 1, ch. 9; O'Keefe; VERIFIED-SECONDARY).
* [FACT] Congress enacted FIRREA in August 1989 and created the Resolution Trust Corporation to resolve insolvent thrifts. By mid-1995 the RTC had resolved 747 thrifts with total assets of \$394 billion (FDIC *Banking Review*; Congressional Research Service report RS22959; VERIFIED-SECONDARY). These figures are national, not Texas-only.

### What was knowable at the time

[INFERENCE] The ingredients were observable. Vacancy was rising while construction continued (the FDIC's own observation for the early 1980s). Office space was growing faster than office employment (O'Keefe). Tax benefits were raising the after-tax return on projects whose pre-tax economics did not need to work. In the language of §8.4.6, months of supply were rising while developers kept starting projects, which can be rational for a developer only if after-tax returns, fees, or lender incentives pay even when the building does not lease. In the language of §8.4.7, value was being supported by something other than the income of the space. What was not knowable was the timing and severity of the oil price collapse, or that the 1986 tax changes would remove part of the after-tax return from projects already financed.

### Interpretations

1. **Overbuilding from mispriced incentives.** Tax benefits and lending practices made projects attractive to build independent of demand. The supply response overshot (FDIC's emphasis on tax policy and loosened underwriting).
2. **Regional demand shock.** Without the oil collapse, the excess space might have been absorbed over several years. The vacancy peaks reflect lost demand as much as excess supply.
3. **Policy reversal.** The 1986 Act changed the after-tax value of existing projects, which hurt owners and the lenders who financed them. Some analyses link the 1981 and 1986 changes to thrift failures; others note that real estate was volatile for many reasons beyond tax law (Tax Foundation discusses both views). [INFERENCE] The three interpretations are complementary rather than exclusive: overbuilt supply made the market fragile, and the demand and policy shocks exposed it.

### What the case does and does not establish

It **establishes** that vacancy can rise from single digits to the high twenties or above within a few years when completions run far ahead of absorption. It shows that supply decisions made on after-tax or lender-driven economics rather than space-market economics produce stock that the market must absorb at falling rents. And it shows that lender losses follow the space market with a lag: the failures and the RTC came years after vacancy began rising.

It does **not** establish that any particular vacancy level predicts a crash, that tax law alone caused the bust, or that the same sequence will repeat in a market with different leverage, lending regulation, and supply constraints. Nor do our sources give rent or price declines for Texas office over the period; we state none *(verification pending)*.

**CRE connection.** Every quantity in Example 8.4 was measurable in Texas in 1983–1985: inventory, vacancy, pipeline, and absorption. The months-of-supply calculation would have shown a market whose pipeline needed years of absorption at a time when vacancy was already rising. The lesson for a speculator is not "avoid Texas." It is that the supply pipeline relative to absorption is the most predictive and least glamorous number in a market report.

---

## 8.10 Decision exercise: reprice the four offerings

Return to the four broker packages in §8.1. You have budget for detailed diligence on two of them. Using the results of Examples 8.1–8.6:

1. **Restate each NOI** on a consistent basis: cash NCF after reserves, after normalizing repairs, with property tax reassessed at the indicated price (assume a Texas-style $t = 2.2\%$ for all four). State which adjustments are facts and which are estimates.
2. **Reprice each asset** at the broker's cap rate applied to your restated income, using the loaded cap rate where tax is reassessed. Show the percentage gap from the broker's price.
3. **Rank the four by the quality of their income**: duration, operating leverage, capex exposure, and concentration. Rank them separately by price discount. Explain any divergence.
4. **Choose two for diligence.** For each, name the single piece of information most likely to change your view (for example: estoppels and anchor sales reports for Oak Hollow; the free-rent and TI schedule and the dark tenant's intentions for Lakeside; STR trend data and the PIP status for the hotel; the PCA and unit-level rent roll for Cedar Court).
5. **State what you will not pursue and why.** Declining all four is a legitimate answer if your restated yields do not clear your cost of capital by enough to pay for the risk.

**Rubric (see `problems/solutions/ch08_solutions.md` §Decision exercise).** Full credit requires that each NOI be restated on one basis with the adjustments labeled; that the hotel be stressed for an ADR-led decline; that Lakeside be valued on cash rather than contract rent with the free-rent credit; that Cedar Court separate permanent from one-time items; that the property-tax reassessment be loaded into each value; and that the choice of two be justified by information value, not only by discount. No single choice of two is correct.

---

## 8.11 Frequent analytical errors

1. **Capitalizing NOI when the comparables were capitalized on NCF, or the reverse.** State the line and the reserve every time.
2. **Counting free rent as income.** Contract rent is not cash rent. Ask for the concession schedule.
3. **Confusing leased with occupied with collecting.** Use all three occupancy measures. A dark tenant is a vacancy with a date.
4. **Treating "NNN" as zero landlord expense.** Caps, exclusions, and vacancy leave the landlord with unrecovered costs (Example 8.1).
5. **Using face rent instead of net effective rent** to compare office leases or to calibrate market rent.
6. **Reading WALT without concentration.** Report WALT with and without the largest tenant and the 24-month rollover share.
7. **Applying one DOL to a hotel.** Rate-led and occupancy-led declines have different flow-through.
8. **Counting pre-leased construction as supply** and then also ignoring its move-ins in absorption.
9. **Treating replacement cost as a value floor.** It is a supply condition (Example 8.7, Case A).
10. **Capitalizing the seller's property-tax bill.** Use the loaded cap rate in reassessment regimes and recognize that Proposition 13 base-year benefits do not transfer.
11. **Capitalizing one-time capex or ignoring permanent cost normalizations.** Permanent items go through the cap rate; one-time items are deducted in dollars.
12. **Treating the reserve as cash.** It is an allowance. The capex bill arrives on its own schedule.
13. **Ignoring transaction costs on short holds.** A 4% round trip is 0.8% a year over five years and about 1.6% a year over two and a half.

---

## 8.12 Connections to other chapters

* Chapter 1: operating leverage multiplies the financial leverage of §1.6; liquidity provision (§1.2) prices immediacy in illiquid property types.
* Chapter 2: price formation and appraisal smoothing explain why the "market cap rate" lags in illiquid types.
* Chapter 4: absorption is the transmission channel from employment and output to NOI.
* Chapter 6: the cap-rate/Treasury spread compares the asset market with fixed income.
* Chapter 9: DCF valuation of rollover, downtime, and TI/LC; loaded cap rates; sensitivity grids.
* Chapter 10: debt sizing on NCF; DSCR under operating-leverage shocks.
* Chapter 11: the full USALI hotel P&L, flow-through, PIPs, and Case A.
* Chapter 12: supply-driven cycles and distressed opportunities; the RTC as a disposal channel.
* Chapter 13: land and development as real options; hold/sell decisions with transaction costs.
* Chapter 23: the 1980s–90s Texas/RTC cycle in full.
* Case A: normalization, loaded cap, replacement cost, and PIP pricing applied to a hotel.

---

## 8.13 One-page reference sheet

**Waterfall:** PGI − vacancy − credit loss + other income = EGI; EGI − OpEx = NOI; NOI − reserves − TI/LC = NCF. In this chapter NOI is before reserves except for hotels (USALI: NOI after FF&E reserve).

| Formula | Expression |
|---|---|
| Physical / leased / economic occupancy | $A_{occ}/A$; $A_{lsd}/A$; cash rent ÷ potential rent |
| Expense ratio; landlord-borne ratio | OpEx/EGI; unrecovered OpEx/EGI |
| NOI growth | $g_{NOI} = g_R (R/NOI) - g_E (E/NOI)$ |
| Degree of operating leverage | $DOL = R(1-v)/NOI$ |
| WALT | $\sum R_i T_i / \sum R_i$ |
| Rollover within $h$ | $\sum_{T_i \le h} R_i / \sum R_i$ |
| Net effective rent | $\left[\sum CR_t (1+k)^{-t} - TI - LC\right] / a_{\overline{n}|k}$ |
| Vacancy identity | $V_{t+1} = V_t + C_t - AB_t$ |
| Months of supply | $(V + C^{spec}) / AB^{monthly}$ |
| Rent rule [HYPOTHESIS] | $g = g^* - \beta(v - v^*)$ |
| Yield on cost | $NOI^{new}/(H+S+L)$; build if $\ge c + s$ |
| Required rent | $(c+s)(H+S+L)/[(1-v)(1-e)]$ |
| Loaded cap value | $V = N/(c+t)$ |
| Prop 13 drift | $t_n = t_{CA}(1.02/(1+g_V))^n$ |
| Deferred-maintenance price | $(NOI^{norm} - Res)/c - (1+\kappa)\,Imm - PV(X_t - Res)$ |
| Transaction-cost drag | $1 - ((1-s)/(1+b))^{1/T}$ |

**Checks before any bid:** Which NOI line? Cash or straight-line? Leased, occupied, or collecting? WALT without the top tenant? Pipeline ÷ absorption? Value ÷ replacement cost and why? Tax reassessed? Reserve versus scheduled capex? How long to sell, and to whom?

---

## References for this chapter

All sources are listed with verification status in `references/sources_ch08.md` (to be merged into `SOURCE_REGISTER.md`).

* Federal Deposit Insurance Corporation (1997). *History of the Eighties — Lessons for the Future*, vol. 1: ch. 1 "The Banking Crises of the 1980s and Early 1990s: Summary and Implications"; ch. 3 "Commercial Real Estate and the Banking Crises of the 1980s and Early 1990s"; ch. 9 "Banking Problems in the Southwest." https://www.fdic.gov/publications/history-eighties-lessons-future-volume-1
* FDIC (2000). *Regional Outlook*, third quarter 2000 (office vacancy peaks). https://www.fdic.gov/analysis/archived-research/outlook/t3q2000.pdf
* O'Keefe, J. *The Texas Banking Crisis: Causes and Consequences, 1980–1989.* FDIC; archived on FRASER. https://fraser.stlouisfed.org/files/docs/publications/texasbankcrisis_1980_1989.pdf
* Federal Reserve Bank of Dallas (1995). *Southwest Economy*, issue 3. https://www.dallasfed.org/~/media/documents/research/swe/1995/swe9503a.pdf
* FDIC (1998). "The Banking Crises of the 1980s and Early 1990s." *FDIC Banking Review*, special issue. https://www.fdic.gov/analysis/archived-research/banking-review/brspecial.pdf
* Congressional Research Service (2008). *The Resolution Trust Corporation: Historical Analysis* (RS22959).
* Tax Foundation (2020). "1980s Tax Reform, Cost Recovery, and the Real Estate Industry: Lessons for Today."
* Federal Reserve Bank of Boston, conference series 36. "Tax Reform and the Housing Market in the Late 1980s." https://www.bostonfed.org/-/media/Documents/conference/36/conf36g.pdf
* California State Board of Equalization and county assessors (Sacramento, Santa Clara, San Luis Obispo). Proposition 13 and base-year value publications.
* Texas appraisal district publications summarizing Texas Property Tax Code §§1.04, 23.01, 23.231.
* IRS Publication 946, *How to Depreciate Property* (recovery periods; secondary confirmation).
* DiPasquale, D., and Wheaton, W. C. (1992). "The Markets for Real Estate Assets and Space: A Conceptual Framework." *Real Estate Economics* (formerly *AREUEA Journal*) *(bibliographic verification pending)*.
* Rosen, K. T. (1984). "Toward a Model of the Office Building Sector." *AREUEA Journal* *(bibliographic verification pending)*.
* Wheaton, W. C., and Torto, R. G. (1988). "Vacancy Rates and the Future of Office Rents." *AREUEA Journal* *(bibliographic verification pending)*.
