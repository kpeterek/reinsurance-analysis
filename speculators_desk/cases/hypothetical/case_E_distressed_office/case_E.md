# Case E — The Distressed Office Acquisition

> **Evidence status:** Every property fact, lease term, cost, market parameter, and counterparty in this case is [HYPOTHESIS], constructed for teaching. Rents, TI and leasing-commission levels, capex, cap rates, conversion costs, and replacement cost are assumptions chosen to be internally consistent for a Sun Belt CBD office tower. They are not sourced market data. Before using any of them in a real underwriting, replace them with current, documented evidence: leasing comparables, broker TI/LC surveys, contractor estimates, appraisals, and lender term sheets.
>
> **Model:** `case_e_model.py` (run it to regenerate every number). **Tests:** `tests/test_case_e.py`. **Rubric:** `case_E_rubric.md` (instructor copy).
>
> **Chapters used:** 1 (break-even probability, mean IRR versus IRR of expected flows), 8 (operating leverage, reassessment), 9 (DCF, replacement cost), 10 (bridge loans, debt yield), 12 (cycles, structural demand, basis reset), 13 (real options: conversion).

---

## Case facts (shared by all modes)

**The building.** A 24-story office tower completed in 1984 in the CBD of a Sun Belt metro. 520,000 rentable sf (RSF); 560,000 sf gross building area (GBA). Floor plates of about 23,000 sf with deep core-to-window depths. Original elevators and central plant. The lobby was renovated in 2008.

**The occupancy.** 197,600 sf (38%) is leased to 31 tenants at an average gross rent of \$33.00/sf. Rents are flat to expiry. The in-place rollover schedule:

| Year | 1 | 2 | 3 | 4 | 5 | 6–7 |
|---|---:|---:|---:|---:|---:|---:|
| Expiring sf | 40,000 | 52,000 | 45,600 | 30,000 | 30,000 | 0 |

Your leasing broker expects 55% of expiring space to renew.

**The seller.** A regional bank took title through foreclosure eight months ago. Its broker is running a two-round sale. Whisper price: **\$52.0 million (\$100/RSF)**. The broker's flyer reads: "Replacement cost exceeds \$480/sf. Own a CBD tower at a fifth of replacement cost." Replacement cost of \$480/RSF implies \$249.6 million.

**Market evidence (assumptions for teaching).**

| Parameter | Value |
|---|---|
| Market gross rent, year 1 | \$34.00/sf |
| New leases: TI / free rent / commission | \$65/sf; 7 months; 6% of rent × 7-year term |
| Renewals: TI / free rent / commission | \$25/sf; 2 months; 3% of rent × 5-year term |
| Fixed operating expenses (excluding tax) | \$6.50/RSF per year on the whole building |
| Variable operating expenses | \$4.00 per occupied sf per year |
| Property tax after sale | 2.0% of price per year (reassessed at the purchase price) |
| Replacement reserve | \$0.30/RSF per year |
| Base-building capex program | \$25/RSF (\$13.0 million): 60% in year 1, 40% in year 2 |
| Buyer closing costs | 1.5% of price |
| Selling costs at exit | 2.0% |
| Investor's unlevered target | 12% |

**Three demand scenarios** (your research team's construction; probabilities are judgments):

| Scenario | $p$ | Year-end occupancy, years 1–7 | Market-rent growth | Exit cap (on year-8 NOI) | Exit liquidity discount |
|---|---:|---|---|---:|---:|
| Recovery | 0.40 | 42, 53, 64, 74, 82, 86, 88% | +3% a year from year 2 | 8.25% | 0% |
| Grind | 0.35 | 38, 43, 50, 57, 63, 68, 70% | 0% | 9.50% | 0% |
| Structural | 0.25 | 34, 33, 35, 38, 41, 44, 46% | −3% in year 2, −2% in year 3, then 0% | 11.00% | 10% |

*Structural* is the scenario in which demand for this class of office space has fallen permanently: tenants shrink at renewal, sublease space stays on the market, and exit buyers are scarce and require a further discount for illiquidity.

**Financing on offer.** A debt fund will lend 55% of the price (\$28.6 million at the whisper price) as a three-year, interest-only bridge loan at an all-in 8.25%. Extension at year 3 requires a 9.0% debt yield on year-3 NOI, with any shortfall paid down.

**Alternative use.** A residential developer suggests converting the tower to apartments. Assumptions: 70% of GBA is convertible given the deep floor plates; 80% efficiency; 780 sf average unit; rent \$2.45/sf per month; 7% vacancy and credit loss; operating expenses 38% of effective gross income; 6.0% exit cap; hard cost \$240/sf of GBA; soft costs 18% of hard; financing costs \$12.0 million; developer margin 15% on total cost.

**Model conventions.** Annual periods; cash flows at year-end. Leasing in year $t$: renewals $= 0.55 \times$ expiring sf; new leasing $=$ (change in occupied sf) $+ 0.45 \times$ expiring sf. Original in-place leases pay \$33.00 until they expire; all other occupied space pays the current year's market rent. Free rent and leasing costs fall in the signing year. Exit at the end of year 7 on year-8 NOI (occupancy held at the year-7 level), with no free rent in the capitalized NOI.

---

## Mode A — Guided instruction

### Step 1: Why "a fifth of replacement cost" says nothing about value

Replacement cost matters only if someone would build at that cost. Compute the rent a new tower of this size would need to earn a 7.0% yield on \$480/RSF at 90% occupancy, with this building's operating costs, tax at 2.0% of cost, and a \$4.00/RSF leasing reserve. The answer (Mode B) is about **\$64/sf**, against a market rent of \$34. No one will build. When replacement cost is far above value, it tells you that new supply is unlikely. It does not support price. The relevant floor is what the building's cash flows will pay, net of the large capital required to produce them.

### Step 2: Cash burn before cash yield

A 38%-leased tower does not earn its operating costs with any margin. Fixed costs (\$6.50/RSF plus tax) are paid on the whole building. Each new lease costs TI, commissions, and free rent upfront, and pays back over years. Build the annual cash flow. The question is not "what is it worth stabilized?" but "how much capital goes in, for how long, before it comes back?"

### Step 3: Price each scenario, then combine

Compute the IRR in each scenario, the IRR of expected flows, the expected profit, and the probability of loss. Then compute the price at which the expected flows earn 12%. Note that the tax bill depends on the price, so the maximum price must be solved, not discounted once.

### Step 4: The structural-demand question

The Structural scenario is the value trap: the building looks cheap because its demand has gone. Compute the break-even probability of the Structural scenario at your bid (Chapter 1, §1.4.2). Ask what evidence would distinguish Structural from Grind in the first 12–24 months.

### Step 5: Debt maturity

Test the bridge loan at year 3 in each scenario. A three-year loan on a seven-year business plan is a bet that the asset will be financeable at year 3.

### Step 6: Alternative use and exit liquidity

Compute the residual land value of a residential conversion. If it exceeds the price, conversion is a floor under value; if not, it is not. Then ask who buys a 46%-leased tower in year 7.

---

## Mode B — Solved case

### B.1 Replacement cost and the rent needed to build

Total replacement cost $= 480 \times 520{,}000 = \$249{,}600{,}000$. Operating costs for a new tower at 90% occupancy: fixed $6.50 \times 520{,}000 = 3{,}380{,}000$; variable $4.00 \times 468{,}000 = 1{,}872{,}000$; tax $0.02 \times 249{,}600{,}000 = 4{,}992{,}000$; reserve \$156,000; total \$10,400,000. Leasing reserve $4.00 \times 520{,}000 = \$2{,}080{,}000$.
$$R_{req} = \frac{0.07 \times 249{,}600{,}000 + 10{,}400{,}000 + 2{,}080{,}000}{520{,}000 \times 0.90} = \frac{29{,}952{,}000}{468{,}000} = \$64.00/\text{sf}.$$
Market rent is \$34.00, 53% of the rent that would justify building. Replacement cost is irrelevant to price.

### B.2 Annual cash flows by scenario (price \$52.0 million)

All-in purchase cost $= 52{,}000{,}000 \times 1.015 = \$52{,}780{,}000$. Property tax $= 0.02 \times 52{,}000{,}000 = \$1{,}040{,}000$ a year.

**Recovery**

| Year | Occ (end) | Mkt rent | Revenue | Free rent | Opex + tax + reserve | NOI | TI | LC | Capex | Cash flow |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 42% | 34.00 | 6,894,400 | 894,200 | 5,408,000 | 592,200 | 3,072,000 | 666,264 | 7,800,000 | −10,946,064 |
| 2 | 53% | 35.02 | 8,384,108 | 1,813,452 | 5,564,000 | 1,006,656 | 5,954,000 | 1,335,733 | 5,200,000 | −11,483,077 |
| 3 | 64% | 36.07 | 10,718,431 | 1,786,096 | 5,792,800 | 3,139,535 | 5,678,800 | 1,313,129 | 0 | −3,852,394 |
| 4 | 74% | 37.15 | 13,143,523 | 1,521,713 | 6,011,200 | 5,610,610 | 4,670,000 | 1,114,024 | 0 | −173,415 |
| 5 | 82% | 38.27 | 15,442,207 | 1,335,210 | 6,198,400 | 7,908,597 | 3,994,000 | 980,293 | 0 | 2,934,304 |
| 6 | 86% | 39.42 | 17,216,611 | 478,239 | 6,323,200 | 10,415,172 | 1,352,000 | 344,332 | 0 | 8,718,840 |
| 7 | 88% | 40.60 | 18,366,435 | 246,293 | 6,385,600 | 11,734,542 | 676,000 | 177,331 | 0 | 10,881,211 |

Year-8 NOI \$12,728,470 capitalized at 8.25%: gross exit \$154,284,479; net of 2% \$151,198,790.

**Grind**

| Year | Occ (end) | Mkt rent | Revenue | Free rent | Opex + tax + reserve | NOI | TI | LC | Capex | Cash flow |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 38% | 34.00 | 6,540,800 | 481,667 | 5,366,400 | 692,733 | 1,720,000 | 369,240 | 7,800,000 | −9,196,507 |
| 2 | 43% | 34.00 | 7,028,800 | 1,141,833 | 5,418,400 | 468,567 | 3,926,000 | 851,292 | 5,200,000 | −9,508,725 |
| 3 | 50% | 34.00 | 8,138,400 | 1,271,033 | 5,543,200 | 1,324,167 | 4,326,800 | 940,726 | 0 | −3,943,359 |
| 4 | 57% | 34.00 | 9,413,800 | 1,083,183 | 5,688,800 | 2,641,817 | 3,656,000 | 796,722 | 0 | −1,810,905 |
| 5 | 63% | 34.00 | 10,593,000 | 980,050 | 5,824,000 | 3,788,950 | 3,318,000 | 722,466 | 0 | −251,516 |
| 6 | 68% | 34.00 | 11,580,400 | 515,667 | 5,938,400 | 5,126,333 | 1,690,000 | 371,280 | 0 | 3,065,053 |
| 7 | 70% | 34.00 | 12,199,200 | 206,267 | 6,011,200 | 5,981,733 | 676,000 | 148,512 | 0 | 5,157,221 |

Year-8 NOI \$6,344,000 at 9.50%: gross exit \$66,778,947; net \$65,443,368.

**Structural**

| Year | Occ (end) | Mkt rent | Revenue | Free rent | Opex + tax + reserve | NOI | TI | LC | Capex | Cash flow |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 34% | 34.00 | 6,187,200 | 124,667 | 5,324,800 | 737,733 | 550,000 | 112,200 | 7,800,000 | −7,724,467 |
| 2 | 33% | 32.98 | 5,747,748 | 507,342 | 5,272,800 | −32,394 | 1,898,000 | 393,583 | 5,200,000 | −7,523,978 |
| 3 | 35% | 32.32 | 5,770,518 | 718,052 | 5,283,200 | −230,734 | 2,636,800 | 541,315 | 0 | −3,408,849 |
| 4 | 38% | 32.32 | 6,164,994 | 637,520 | 5,335,200 | 192,274 | 2,304,000 | 475,013 | 0 | −2,586,739 |
| 5 | 41% | 32.32 | 6,648,804 | 637,520 | 5,397,600 | 613,684 | 2,304,000 | 475,013 | 0 | −2,165,329 |
| 6 | 44% | 32.32 | 7,142,808 | 294,116 | 5,460,000 | 1,388,693 | 1,014,000 | 211,763 | 0 | 162,929 |
| 7 | 46% | 32.32 | 7,562,974 | 196,077 | 5,512,000 | 1,854,897 | 676,000 | 141,176 | 0 | 1,037,721 |

Year-8 NOI \$2,198,240 at 11.0% less a 10% liquidity discount: gross exit \$17,985,597; net \$17,625,885.

**Check (Recovery, year 1).** Revenue: in-place leases average $(197{,}600 + 157{,}600)/2 = 177{,}600$ sf at \$33 $= \$5{,}860{,}800$; other occupied space averages $(197{,}600 + 218{,}400)/2 - 177{,}600 = 30{,}400$ sf at \$34 $= \$1{,}033{,}600$; total \$6,894,400. ✓ New leasing $= (0.42 - 0.38) \times 520{,}000 + 0.45 \times 40{,}000 = 38{,}800$ sf; renewals 22,000 sf. TI $= 38{,}800 \times 65 + 22{,}000 \times 25 = \$3{,}072{,}000$. ✓

### B.3 Returns at the whisper price

| Scenario | $p$ | IRR | Profit | Multiple |
|---|---:|---:|---:|---:|
| Recovery | 0.40 | 13.10% | \$94,498,194 | 2.19x |
| Grind | 0.35 | −0.80% | −\$3,825,369 | 0.95x |
| Structural | 0.25 | −20.62% | −\$57,362,825 | 0.25x |

Expected profit \$22,119,692; standard deviation \$62,533,414; probability of loss 60%. Mean of scenario IRRs −0.19%; **IRR of expected flows 4.03%**.

**Peak capital.** In the Recovery scenario cumulative cash reaches −\$79,234,950 at the end of year 4. The equity check is not \$52 million; it is about \$79 million, of which \$26 million is spent after closing on capex, TI, commissions, and free rent. The other scenarios need about \$76–77 million.

### B.4 What the building is worth to a 12% buyer

Solving for the price at which expected flows have zero NPV at 12% (with the tax bill reassessed at that price): **\$29,175,730, or \$56.11/RSF**. At that price the scenario IRRs are 21.35% (Recovery), 7.04% (Grind), and −12.28% (Structural), and the probability of loss falls to 25%.

| Sensitivity (other inputs unchanged) | Max price at 12% |
|---|---:|
| Base case | \$29.18m |
| Structural probability 0 (Recovery:Grind kept at 40:35) | \$38.99m |
| Structural probability 0.50 (Recovery:Grind kept at 40:35) | \$19.24m |
| New-lease TI \$85/sf instead of \$65 | \$26.21m |
| Fixed opex \$7.50/RSF instead of \$6.50 | \$25.17m |
| All exit caps +100 bp | \$25.55m |

**Break-even probability of the Structural scenario.** At \$52 million the Recovery and Grind scenarios together have negative NPV at 12% (Recovery +\$4.84 million, Grind −\$39.18 million), so the deal fails the target even if Structural has zero probability. At \$30 million, the break-even Structural probability is **22.9%**. Your team's 25% is above it, which is consistent with a \$30 million price earning slightly less than 12% (11.64%).

### B.5 Debt maturity

Bridge loan \$28.6 million; interest \$2,359,500 a year. Year-3 NOI and extension test at a 9.0% debt yield:

| Scenario | Year-3 NOI | Supportable loan | Paydown required |
|---|---:|---:|---:|
| Recovery | \$3,139,535 | \$34,883,722 | \$0 |
| Grind | \$1,324,167 | \$14,712,963 | \$13,887,037 |
| Structural | −\$230,734 | \$0 | \$28,600,000 |

In 60% of the probability mass the sponsor must find \$13.9–28.6 million at year 3, in addition to unlevered deficits in years 1–3 of \$22.6 million (Grind) or \$18.7 million (Structural), plus \$7.1 million of interest. Leverage does not reduce the equity requirement much; it converts the Grind scenario into a forced recapitalization at the worst moment. A bridge loan whose term is shorter than the lease-up is a source of distress, not of returns.

### B.6 Residential conversion

Net residential area $= 560{,}000 \times 0.70 \times 0.80 = 313{,}600$ sf, about 402 units of 780 sf. Gross potential rent $= 313{,}600 \times 2.45 \times 12 = \$9{,}219{,}840$. EGI $= \$8{,}574{,}451$. NOI $= 0.62 \times EGI = \$5{,}316{,}160$. Value at 6.0% $= \$88{,}602{,}662$; net of 2% selling costs \$86,830,609.
Costs: hard $= 240 \times 560{,}000 = \$134{,}400{,}000$; soft \$24,192,000; financing \$12,000,000; total non-land \$170,592,000.
Residual land value $= 86{,}830{,}609/1.15 - 170{,}592{,}000 = -\$95{,}087{,}122$.

Conversion is deeply infeasible: the completed apartments would be worth about half the cost of creating them. At hard costs of \$150/GBA sf the residual is still −\$35.6 million. Holding costs as given, residential rent would have to be **\$5.54/sf per month** for the residual to reach zero, and **\$7.22/sf per month** to support the \$52 million price, about three times the assumed \$2.45. Conversion is not a floor under value for this building. It would require a large public subsidy or a building with shallower floor plates.

### B.7 Exit liquidity

In the Structural scenario the year-7 buyer is purchasing a 46%-leased, 30-year-old tower in a market whose demand has shrunk. The 11.0% cap and 10% liquidity discount are assumptions; the true risk is that no buyer with financing exists at any reasonable price, in which case the hold extends and the losses grow. The model's −20.62% IRR is therefore not a floor.

### B.8 Recommendation (one defensible answer)

* **Do not bid at \$52 million.** The IRR of expected flows is 4.0%; even with zero probability of structural decline the deal does not reach 12%.
* **A first-round bid of \$27–29 million (\$52–56/RSF)**, conditional on (i) a lease audit and tenant interviews covering the 2027–2028 expirations, (ii) an engineering report confirming the \$13 million capex scope, and (iii) no bridge loan shorter than five years.
* **Walk away above \$32 million**, or if tenant interviews show renewals below 40% of expiring space or average downsizing of more than 25% at renewal, which would move probability from Grind toward Structural.
* **What you are paid for.** Lease-up execution, capital for TI and free rent that leveraged owners lack, and a structural-demand bet. Be explicit that the last is a bet.

**What would change the conclusion.** Evidence that the submarket's leasing per employee has stabilized; a tenant with a large requirement willing to sign a pre-lease; a municipal conversion incentive large enough to make the residual positive; or a seller willing to provide five-year financing at a fixed rate.

---

## Mode C — Blind examination

Use only the Case facts section. Do not look at Modes A or B. Allow 120 minutes. Spreadsheets are permitted.

1. (10 pts) Compute the gross rent a new tower needs to earn 7.0% on replacement cost (assumptions in Mode A Step 1). Explain why the discount to replacement cost is not evidence of value.
2. (20 pts) Build the year-1 to year-7 cash flows for the Recovery scenario. Show the year-1 revenue, leasing volumes, TI, LC, and free-rent calculations explicitly.
3. (10 pts) Compute the exit value in each scenario.
4. (15 pts) Compute each scenario's IRR, the IRR of expected flows, expected profit, and probability of loss at \$52 million. Explain why the mean of scenario IRRs differs from the IRR of expected flows.
5. (10 pts) Solve for the maximum price at a 12% unlevered target. State how you handled the property-tax reassessment.
6. (10 pts) Test the bridge loan at year 3 in each scenario. What does the result imply about leverage?
7. (10 pts) Compute the residual land value of a residential conversion and the rent at which conversion supports the whisper price.
8. (10 pts) Name the two observations in the first 18 months that would best distinguish Grind from Structural, and how each would change your probabilities.
9. (5 pts) State a bid, conditions, and walk-away triggers.

Answers: Mode B and `case_E_rubric.md`.

---

## Mode D — Investment committee

Prepare written answers, each under 150 words and supported by a number.

1. **The broker says we are buying at a fifth of replacement cost. Why is that not a reason to buy?**
2. **How much equity does this take, and when is it at risk?** (Peak capital, not purchase price.)
3. **What is your evidence that this is not a structural decline?** What would you observe in the first year if it were?
4. **What happens if TI rises to \$85/sf for new leases**, as the leasing broker warned it might?
5. **Why not use the bridge loan?** The sponsor's partner says leverage improves IRR.
6. **The developer says conversion gives us a floor. Does it?**
7. **Who buys this in year 7 in the Grind scenario, and at what cap rate?** What if exit caps are 100 bp wider?
8. **The bank may lower its price in the second round. Why bid now at all?**
9. **Which of these risks can be hedged?**
10. **What is the most likely way this thesis fails?**

The committee rubric is in `case_E_rubric.md`.
