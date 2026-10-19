# Case J — The Credit Crunch Hotel Acquisition

> **Evidence status:** Every property fact, operating figure, market parameter, loan term, buyer return target, probability, and counterparty in this case is [HYPOTHESIS], constructed for teaching. Market ranges such as cap rates, loan constants, leverage limits, and buyer hurdle rates are assumptions chosen to be plausible for an upscale select-service hotel in a growing Sun Belt metro during a credit contraction. They are not sourced market data. The short historical box in §A.0 uses only sourced facts, labeled [FACT], from `references/sources_caseJ.md`.
>
> **Model:** `case_j_model.py` (run it to regenerate every number). **Tests:** `tests/test_case_j.py`. **Data:** `cases/datasets/case_j_str_comp.csv`. **Rubric:** `case_J_rubric.md`.
>
> **Chapters used:** 1 (immediacy, liquidity, who is on the other side), 6 (cost of capital), 9 (valuation, loaded cap), 10 (debt sizing, leverage, refinancing), 11 (hotel P&L, penetration, supply), 23 (credit-crunch episodes).
>
> **Conventions (same as Case A):** NOI is after a 4% FF&E reserve. $N$ is NOI after reserve but **before** property tax. Property tax is reassessed on sale at $t$ = tax rate × assessment ratio of price, so value and tax are solved together (the loaded cap of Case A). Annual property cash flows at year-end. Mortgages pay monthly at $r/12$, 25-year amortization. Reversion at the end of year 5 capitalizes **year-6** NOI before tax at the loaded exit cap $c_T + t$, less 2% selling costs.

---

## Case facts (shared by all modes)

**The property.** A 150-room upscale select-service hotel under a national brand, built in 2016, in a suburban office and medical corridor of a growing Sun Belt metro. It has a breakfast room, a small bar and market, 2,400 square feet of meeting space, and surface parking. It is third-party managed. The franchise agreement has 13 years remaining and the brand completed a property inspection last year with no PIP requirement before 2029.

**The seller.** A regional developer that built the hotel and wants to recycle the equity into a new project. It is not distressed. Its existing loan (below) does not mature for seven years.

**The situation.** Eighteen months ago, three hotels of similar quality in the metro traded at prices the listing broker describes as "\$125,000–\$130,000 a key." Since then, bank and CMBS lending for hotels has contracted. Banks quote 45% loan-to-value instead of 65%, at 8.25% instead of 6.50%. Debt funds quote 50% instead of 70%, at 9.75% instead of 7.00%. The publicly traded lodging REITs trade below their net asset values and have stopped acquiring. The listing broker ran a process. The best bid, from a regional owner-operator, is \$17.1 million (\$114,000 a key) and carries a bank-financing contingency. **The broker's position: "Nothing is wrong with this hotel. NOI is basically flat. Buyers just can't get loans. In a normal market this is a \$19 million hotel."**

**Your role.** You are the analyst for a family-office-backed hotel vehicle with \$25 million of uncalled equity, a 13% target levered IRR on a five-year hold, and the ability to close all-cash. Your principal asks: *Is this a temporary liquidity discount we should buy, or a permanent impairment the broker is dressing up? What do we bid, and how?*

### Exhibit J-1 — Current T-12 operating summary (crunch period)

| Line | Amount (\$) | Notes |
|---|---:|---|
| Rooms revenue | 6,281,660 | 40,790 room-nights sold of 54,750 available; Occ 74.50%; ADR \$154.00 |
| Other operated revenue | 520,000 | Breakfast, bar and market, parking, meeting |
| **Total revenue** | **6,801,660** | |
| Rooms expense | 1,630,000 | |
| Other departmental expense | 330,000 | |
| Undistributed expenses | 1,610,000 | A&G, S&M, POM, utilities, IT |
| **Gross operating profit** | **3,231,660** | 47.5% |
| Management fee (3% of total revenue) | 204,050 | |
| Franchise fees (11% of rooms revenue) | 690,983 | Royalty, program, loyalty, reservations |
| Insurance | 175,000 | |
| **EBITDA before property tax** | **2,161,628** | |
| FF&E reserve (4% of total revenue) | 272,066 | |
| **$N$: NOI after reserve, before property tax** | **1,889,561** | |

The same line for the T-12 that ended 18 months ago (the last period of normal credit) was **\$1,935,000**.

### Exhibit J-2 — STR-style performance (`case_j_str_comp.csv`)

The competitive set is six hotels with 940 rooms. It excludes the subject.

| T-12 ending | Subject Occ | Subject ADR | Comp Occ | Comp ADR |
|---|---:|---:|---:|---:|
| 36 months ago | 73.5% | \$146.00 | 69.0% | \$141.00 |
| 18 months ago | 75.2% | \$152.00 | 69.5% | \$147.00 |
| Current | 74.5% | \$154.00 | 68.0% | \$148.00 |

**Supply.** One directly competitive 96-room hotel is under construction. Its construction loan closed before the crunch, and it opens in about 15 months. A second, 120-room project is entitled but has no construction loan. Its developer says it will "go vertical as soon as the banks reopen." Your base assumption for room-night demand growth in the submarket is 2.5% a year.

### Exhibit J-3 — Market and financing parameters (assumptions for teaching)

| Parameter | Value |
|---|---|
| Property tax | 2.10% combined rate × 80% assessment ratio = $t$ = 1.68% of price |
| NOI and tax growth | 3.0% a year |
| Exit cap (on forward NOI after reassessed tax): normal credit / credit still shut | 8.50% / 9.75% |
| Buyer closing costs; seller's selling costs at exit | 1.5%; 2.0% |
| NOI flow-through on lost rooms revenue | 60% |

**Buyer universe.** Each buyer type keeps its required equity return fixed through the crunch. Only its financing and its ability to act change.

| Buyer type | Return test | Target | Normal debt (LTV / rate / min DSCR / min DY) | Crunch debt | Equity capacity | Active in crunch? |
|---|---|---:|---|---|---:|---|
| Owner-operator | Year-1 cash-on-cash | 9.0% | 65% / 6.50% / 1.35x / 10% | 45% / 8.25% / 1.50x / 13% | \$12.0m | Yes |
| Opportunity fund | 5-yr levered IRR | 16.0% | 70% / 7.00% / 1.25x / 9% | 50% / 9.75% / 1.40x / 12% | Unlimited | Yes |
| Lodging REIT | 5-yr unlevered IRR | 9.0% | None at asset level | None | Unlimited | **No** (stock below NAV) |
| Family-office cash buyer | 5-yr unlevered IRR | 10.5% | None | None | \$15.0m | Yes |

All bidders underwrite the 96-room hotel under construction. None underwrites the unfinanced 120-room project.

**Seller's existing loan.** Originated 36 months ago: \$12.5 million, 5.00% fixed, 25-year amortization, 10-year term (84 months remain). The loan is assumable with servicer approval and a 1% fee. Your estimate of a market rate for comparable debt today is 8.25%. You estimate an 85% probability that the servicer approves an assumption by your vehicle within 75 days.

**Your vehicle's refinancing plan.** If you buy all-cash, you will refinance when credit returns, on normal terms: 65% LTV, 6.50%, 1.35x DSCR, 10% debt yield, 1% cost. The appraisal will capitalize forward NOI after the (unreassessed) tax bill at 8.25%. Your scenario set:

| Scenario | Probability | Refinance | NOI path from year 2 | Exit market |
|---|---:|---|---|---|
| Credit returns in 1 year | 0.30 | End of year 1 | Base, less the 96-room supply hit | Normal (8.50%) |
| Credit returns in 2 years | 0.30 | End of year 2 | Same | Normal |
| Credit returns in 4 years | 0.15 | End of year 4 | Same | Normal |
| Credit shut through exit | 0.10 | None | Same | Crunch (9.75%) |
| Impairment | 0.15 | None | Base less 15% | Crunch |

**The seller's view of a financed bid.** You believe one in three financed bids in this market fails at the lender's credit committee or appraisal, so the owner-operator's bid closes with probability 0.65. If it fails, the seller re-markets for six months and takes the next-best bid. The seller discounts delay at 8% a year.

---

## Mode A — Guided instruction

Try each step before reading the commentary.

### A.0 Why this question is hard: two shocks that usually arrive together

**Historical box.** Real credit crunches rarely leave hotel NOI intact, which is why the clean case here is a teaching construction.

* **2009.** [FACT] U.S. CMBS issuance fell from a 2007 peak of roughly \$230 billion to about \$11–12 billion in 2008 and a few billion dollars in 2009; sources differ on the exact figures (caseJ-S04). [FACT] In the same year, STR reported U.S. hotel RevPAR down 16.7% for 2009, with occupancy at 55.1% and ADR at \$97.51 (caseJ-S03). Credit and fundamentals collapsed together.
* **2020.** [FACT] In the Federal Reserve's July 2020 Senior Loan Officer Opinion Survey, banks reported tightening standards on all three major CRE loan categories. They also described their standards as near the restrictive end of the range since 2005 (caseJ-S02). [FACT] Trepp reported the CMBS lodging delinquency rate at 24.30% in June 2020 (caseJ-S01). Again, credit contracted *because* hotel cash flow had collapsed.
* [INFERENCE] In both episodes, a buyer who saw a lower hotel price could not tell from the price alone how much was a financing discount and how much was impaired cash flow. Both forces pushed the same way. The decomposition in this case exists to separate them. When the separation fails, as in 2009, the "liquidity discount" story is the seller's broker's story, not an analysis.

### A.1 Who is the marginal buyer, and what can it pay?

A price is set by the buyer whose bid clears, not by "the market." In a sealed or open auction with several bidders who have private valuations, the winner pays roughly what is needed to beat the second-highest bidder. So the **clearing price is the second-highest maximum price** among active bidders. Each bidder's maximum price comes from its own return test, financing, and capacity:

$$P_j^{max} = \min\left(P_j^{return},\; P_j^{capacity}\right).$$

**Cash-on-cash buyers (band of investment).** Let $\lambda$ be LTV, $K$ the loan constant, $y$ the target cash-on-cash, and $c$ closing costs. With LTV binding, the loan is $\lambda P$ and equity is $P(1+c) - \lambda P$. Year-1 NOI after reassessed tax is $N - tP$. Setting cash-on-cash equal to target:

$$\frac{N - tP - \lambda K P}{P(1 + c - \lambda)} = y \;\Rightarrow\; P = \frac{N}{t + \lambda K + y\,(1 + c - \lambda)}.$$

The denominator is the band-of-investment cap rate, loaded for tax and closing costs. Its derivative with respect to $\lambda$ is $K - y$. **A cut in loan proceeds lowers the price only while $K < y$**, that is, while debt is cheaper than the equity it replaces. Once the loan constant exceeds the equity target, less leverage *raises* the price this buyer can pay, and the damage comes from the rate, not the proceeds.

**IRR buyers.** For a levered-IRR buyer, the price solves NPV = 0 at the target rate. Because tax, loan, and equity are all proportional to price when LTV binds, the equity flows are linear in $P$. The model solves by bisection, which also handles DSCR or debt-yield constraints if they bind.

**Capacity.** A buyer with a \$15 million equity limit cannot pay more than \$15.0m / 1.015 all-cash, whatever its return target says.

### A.2 Test the NOI before you blame the lenders

A liquidity discount is a claim about the *discount rate* and the *buyer pool*. It is only credible if cash flow is intact. Test three things:

1. **Penetration.** Compute MPI, ARI, and RGI for each period. A stable or rising RGI says the hotel is holding share. A falling RGI with a stable market says something hotel-specific is wrong.
2. **Market RevPAR.** Is the comp set's RevPAR falling? If it is falling hard, the market is weakening and the "credit" story is incomplete.
3. **Supply.** New rooms dilute occupancy unless demand grows as fast. With the subject's MPI held constant, the subject's occupancy moves with market occupancy:
$$\frac{Occ_1}{Occ_0} = \frac{(1+d)^{n}}{1 + s},$$
where $d$ is annual demand growth over $n$ years of absorption and $s$ is supply growth. Lost rooms revenue × flow-through gives the NOI hit. Then ask the uncomfortable question: **which pipeline projects are being held back by the same credit crunch that is depressing the price?**

### A.3 Decompose the price decline

Move from the normal-credit clearing price to the crunch clearing price one factor at a time: fundamentals (NOI), loan proceeds, loan rate, and buyer universe (who is still bidding). Each step recomputes every bidder's maximum and the second-highest. The decomposition is **path-dependent**, because each buyer's sensitivity to one factor depends on the level of the others (see the $K - y$ result above). Report at least two orders and state the range.

### A.4 Price the all-cash purchase with a refinancing plan

All-cash removes financing risk at closing. It does not remove the bet. It converts a *credit* bet into a *timing* bet: equity is fully exposed until the refinancing returns part of it. Compute IRR and NPV at the 13% hurdle for each scenario, then weight by probability. Two traps:

* **Probability-weighted IRR is not the IRR of the expected deal.** IRR is non-linear in cash flows. Weighting IRRs overstates value when early-refinancing scenarios have high IRRs on small remaining equity. Use probability-weighted NPV at the hurdle.
* **IRR and dollars disagree about timing.** A late refinancing produces *more* dollar profit, because the asset carries no interest cost for longer, but a lower IRR. The cost of being wrong about timing is a time-value cost. Measure it at the hurdle rate.

### A.5 Price certainty, then consider structure

A seller compares bids on certainty-equivalent value, not headline price. A financed bid that closes with probability $q$, with a fallback bid $P_{fb}$ received $m$ months later, is worth:

$$CE = q\,P_{fin} + (1-q)\,\frac{P_{fb}}{(1+d)^{m/12}}.$$

Then look for structures that move financing from the frozen market to the seller:
* **Seller financing.** A seller note lets a levered buyer pay a higher headline price. The seller's cash-equivalent price is cash at closing plus the note's present value at the seller's opportunity rate. A below-market note is a price concession in disguise.
* **Assumable debt.** A below-market fixed-rate loan is an asset when market rates are higher. Its value is the balance minus the present value of its remaining payments at the market rate. A buyer who can assume it is not exposed to the refinancing-timing bet at all.

### A.6 Write the decision rule before you see the bid you want to make

State in advance: the tests that classify the discount as liquidity or impairment; the price criterion (NPV, not average IRR); the scenario that must not destroy capital; and the events that end the bid.

---

## Mode B — Solved case

### B.1 Operating profile

Occupancy $= 40{,}790 / (150 \times 365) = 40{,}790 / 54{,}750 = 74.50\%$. ADR = \$154.00. RevPAR = \$114.73.

$N$ = GOP 3,231,660 − management 204,050 − franchise 690,983 − insurance 175,000 − reserve 272,066 = **\$1,889,561**. Against the pre-crunch \$1,935,000, NOI before tax fell **\$45,439, or 2.35%**.

### B.2 NOI durability

**Penetration** (`hotel.indices`):

| T-12 ending | Subject RevPAR | Comp RevPAR | MPI | ARI | RGI |
|---|---:|---:|---:|---:|---:|
| 36 months ago | 107.31 | 97.29 | 106.5 | 103.5 | 110.3 |
| 18 months ago | 114.30 | 102.17 | 108.2 | 103.4 | 111.9 |
| Current | 114.73 | 100.64 | 109.6 | 104.1 | 114.0 |

Over the crunch, subject RevPAR rose 0.37% while comp-set RevPAR fell 1.49%. RGI rose from 111.9 to 114.0. The hotel is gaining share in a market that softened slightly. The 2.35% NOI decline is consistent with cost growth on flat revenue, not with a hotel-specific problem. Penetration tests: **pass**.

**Supply (96 rooms under construction).** Market rooms = 940 + 150 = 1,090. Supply growth $s = 96/1{,}090 = 8.81\%$. Two years of demand growth: $1.025^2 - 1 = 5.06\%$. Occupancy factor $= 1.050625/1.088073 = 0.9656$. Subject rooms revenue lost $= 6{,}281{,}660 \times (1 - 0.9656) = \$216{,}197$. NOI hit at 60% flow-through = **\$129,718, 6.86% of $N$**. Every bidder in the model, including you, underwrites this from year 2.

**Supply including the unfinanced 120-room project.** $s = 216/1{,}090 = 19.82\%$. Occupancy factor 0.8769. NOI hit **\$464,108, 24.56% of $N$**. That project exists only if credit returns. **The scenario in which your refinancing works is the scenario in which your competitive supply gets financed.** Keep this for Mode D.

### B.3 The buyer universe and clearing prices

Loan constants (25-year, monthly): 6.50% → 8.1025%; 7.00% → 8.4814%; 8.25% → 9.4614%; 9.75% → 10.6936%.

**Normal credit, pre-crunch NOI \$1,935,000:**

| Buyer | Max price | Per key | Loan (binding) | Equity | Going-in cap |
|---|---:|---:|---:|---:|---:|
| Lodging REIT | 19,001,990 | 126,680 | none | 19,287,020 | 8.50% |
| Owner-operator | 18,911,969 | 126,080 | 12,292,780 (LTV) | 6,902,869 | 8.55% |
| Opportunity fund | 18,254,036 | 121,694 | 12,777,825 (LTV) | 5,750,021 | 8.92% |
| Family-office cash buyer | 14,778,325 (capacity) | 98,522 | none | 15,000,000 | 11.41% |

Clearing price (second-highest) **\$18,911,969, \$126,080 a key**, set by the owner-operator. The broker's "\$125,000–\$130,000 a key" is consistent with this market.

Check (owner-operator, closed form): $P = 1{,}935{,}000 / (0.0168 + 0.65 \times 0.081025 + 0.09 \times (1.015 - 0.65)) = \$18{,}911{,}969$. ✓

**Crunch credit, current NOI \$1,889,561:**

| Buyer | Max price | Per key | Loan (binding) | Equity | Going-in cap | Active |
|---|---:|---:|---:|---:|---:|---|
| Lodging REIT | (18,555,774) | (123,705) | none | | 8.50% | No |
| Owner-operator | 17,142,561 | 114,284 | 7,714,152 (LTV) | 9,685,547 | 9.34% | Yes |
| Opportunity fund | 15,981,461 | 106,543 | 7,990,730 (LTV) | 8,230,452 | 10.14% | Yes |
| Family-office cash buyer | 14,778,325 (capacity) | 98,522 | none | 15,000,000 | 11.11% | Yes |

The top bid is the owner-operator's \$17,142,561, which matches the bid the broker received. The clearing price in the second-price sense is **\$15,981,461, \$106,543 a key**, set by the opportunity fund. The clearing price fell **\$2,930,508, or 15.5%**.

Three observations matter more than the table:

1. **The owner-operator now needs \$9.69 million of equity instead of \$6.90 million**, 40% more, to buy a hotel at a lower price.
2. **At crunch rates, leverage is dilutive at the margin for the owner-operator.** The loan constant is 9.46%, above both its 9.00% equity target and the 9.34% going-in cap. At normal credit the constant was 8.10%, 45 bp below the going-in cap. For this buyer, 65% LTV at 8.25% supports only \$17,000,237. That is *less* than 45% LTV at 8.25% supports (\$17,142,561). The proceeds cut costs this buyer nothing once rates rose. The rate did the damage.
3. **The family-office cash buyer's return test would allow \$17.56 million in the crunch**, but its \$15 million equity limit caps it at \$14.78 million. Cash is scarce in exactly the size that matters. That scarcity is your vehicle's edge.

### B.4 Decomposition of the decline

Order A (fundamentals first, then proceeds, rate, and universe):

| Step | Clearing price | Change | Share of decline |
|---|---:|---:|---:|
| Normal credit, pre-crunch NOI | 18,911,969 | | |
| Current NOI (\$1,889,561) | 18,467,867 | −444,102 | 15.2% |
| Crunch LTV/DSCR/DY at normal rates | 18,149,454 | −318,413 | 10.9% |
| Crunch rates | 17,142,561 | −1,006,893 | 34.4% |
| REIT exits the market | 15,981,461 | −1,161,100 | 39.6% |
| **Total** | | **−2,930,508** | **100%** |

Order B (all financing changes first, fundamentals last): financing −\$2,546,197; fundamentals −\$384,311 (13.1%).

**Result.** Fundamentals explain **13–15%** of the decline. Financing (proceeds, rate, and the exit of the highest bidder) explains **85–87%**. The largest single factor is not the LTV cut that the broker cites. It is the exit of the REIT: in a second-price market, losing your highest bidder lowers the price to the next one. The second-largest is the rate. The decline is predominantly a liquidity and buyer-pool discount. **Classification: liquidity discount, conditional on the supply caveat in B.2.**

### B.5 What the seller will actually accept

The owner-operator's \$17,142,561 closes with probability 0.65. The fallback is the opportunity fund's \$15,981,461, received six months later and worth $15{,}981{,}461 / 1.08^{0.5} = \$15{,}378{,}168$ today. Certainty-equivalent of the financed bid:

$$CE = 0.65 \times 17{,}142{,}561 + 0.35 \times 15{,}378{,}168 = \$16{,}525{,}023.$$

A certain all-cash bid of about **\$16.53 million** is as good to the seller as the headline \$17.14 million. The financing contingency is worth \$617,538 to the seller.

### B.6 All-cash at \$16.55 million with a planned refinancing

Price \$16,550,000; equity \$16,798,250 including 1.5% closing. Reassessed tax \$278,040. Going-in yield on price 9.74%.

| Scenario | p | Refi loan (binding) | IRR | Equity multiple | Profit (\$) | NPV at 13% (\$) |
|---|---:|---:|---:|---:|---:|---:|
| Credit returns in 1 year | 0.30 | 12,025,056 (LTV) | 17.21% | 1.46x | 7,698,442 | 1,390,813 |
| Credit returns in 2 years | 0.30 | 12,385,808 (LTV) | 15.04% | 1.50x | 8,359,398 | 851,149 |
| Credit returns in 4 years | 0.15 | 13,140,104 (LTV) | 12.74% | 1.59x | 9,859,301 | −142,861 |
| Credit shut through exit | 0.10 | — | 10.17% | 1.52x | 8,690,580 | −1,695,074 |
| Impairment | 0.15 | — | 7.90% | 1.39x | 6,500,331 | −2,958,274 |

Year-1 refinancing detail: appraised value = year-2 NOI after the unreassessed tax ÷ 8.25% = \$18,500,087. Loan = 65% = \$12,025,056, with LTV binding. Debt service \$974,329; DSCR 1.57x. Net proceeds after 1% cost \$11,904,806.

* Probability-weighted IRR: **13.79%**. IRR of the probability-weighted cash flows: **13.08%**. Probability-weighted NPV at 13%: **+\$37,911**.
* **Maximum all-cash price** (expected NPV = 0): **\$16,584,807**. Using probability-weighted IRR = 13% instead would give \$16,857,793, an overpayment of \$272,986 caused by averaging IRRs.
* **Naive underwriting.** If you assume credit returns in one year with certainty, the maximum price is \$17,815,454. That is \$1.23 million above the probability-weighted maximum. This is the cost of being wrong about timing, capitalized into the bid.
* **Timing within the deal.** Refinancing in year 4 instead of year 1 cuts IRR by 4.47 points and NPV at 13% by \$1,533,674. Dollar profit *rises* by \$2,160,859 because there are fewer years of interest. The cost of delay is time value and the opportunity cost of trapped equity, not lost dollars.
* **Capital protection.** No scenario loses money. In the impairment case all-cash still returns 7.90%, because the going-in yield is 9.74%. All-cash converts a capital-loss risk into a return-shortfall risk.
* **Break-even impairment probability.** With the other scenarios rescaled pro rata, expected IRR falls to 13% at an impairment probability of **26.4%**, against 15% assumed.

**Conclusion on all-cash.** \$16.55 million beats the certainty-equivalent of the financed bid by about \$25,000 and sits \$35,000 below your maximum. It works, but the margin is thin on both sides. Most of the liquidity discount is already competed away by the certainty-adjusted financed bid.

### B.7 Seller financing

The owner-operator could pay more with a seller note: bank loan 45% at 8.25% plus a 20% seller second at 6.00% interest-only, five-year balloon, at its 9.0% cash-on-cash target:

$$P = \frac{N}{t + \lambda K + i_s s + y\,(1 + c - \lambda - s)} = \$18{,}129{,}408.$$

Bank \$8,158,233 (LTV binds), note \$3,625,882, equity \$6,617,234. Year-1 NOI \$1,584,987; bank debt service \$771,883; note interest \$217,553; total DSCR 1.60x.

The seller's cash-equivalent: PV of the note at the seller's 11% opportunity rate for a subordinate loan = \$2,955,837, a discount of \$670,044 to face. Cash-equivalent price = 18,129,408 − 3,625,882 + 2,955,837 = **\$17,459,363**. The headline is \$18.13 million. The seller would really receive \$17.46 million, and it would be lending behind a bank to a buyer with 35% equity.

### B.8 Assumable debt

Existing loan: balance after 36 payments **\$11,686,551**. Monthly payment \$73,073.76 (\$876,885 a year). The balloon at month 120 is \$9,240,559. PV of the remaining 84 payments and balloon at 8.25% is \$9,848,087. **Mark-to-market value of the below-market loan to a buyer: \$1,838,464.** The assumption fee is \$116,866.

**Your vehicle with assumption, price \$17,600,000:** equity \$6,294,314. Year-1 DSCR on the 5.00% loan: 1.82x. The loan runs past your exit, so there is no refinancing to time:

| Scenario | IRR | NPV at 13% |
|---|---:|---:|
| Credit returns (1, 2, or 4 years: identical) | 18.40% | 1,381,898 |
| Credit shut through exit | 13.92% | 216,136 |
| Impairment | 8.15% | −1,047,064 |
| **Probability-weighted** | **16.41%** | **900,978** |

Maximum price with assumption: **\$18,436,335** at 13%. A stricter analyst can argue that a fixed-rate structure at 66% LTV deserves a higher hurdle. At 15% the maximum is **\$17,957,636**. The rate advantage is worth more to a buyer who can keep it than to the seller, who can monetize it only through a sale.

### B.9 The seller's choice, on certainty-equivalent value

| Offer | Headline | Seller's certainty-equivalent |
|---|---:|---:|
| Owner-operator, bank-financed | 17,142,561 | 16,525,023 |
| Your all-cash | 16,550,000 | 16,550,000 |
| Owner-operator with 20% seller note | 18,129,408 | 17,459,363, with residual credit risk |
| Your assumption bid (all-cash backup if denied, p = 0.85) | 17,600,000 | 17,442,500, no residual risk |

### B.10 Decision rule and recommendation

**Decision rule (written before pricing):**

1. *Classify.* Treat the discount as a liquidity discount only if all four hold: (a) financing explains at least two-thirds of the clearing-price decline under both decomposition orders; (b) RGI is at least 100 and has not declined over the last 36 months; (c) comp-set RevPAR has declined no more than 5%; (d) the NOI hit from *financed* supply is no more than 10% of $N$. Here: 85–87%, RGI 114.0 and rising, −1.49%, 6.86%. **All pass.** If any fails, value the hotel on stressed fundamentals at normal-credit returns and treat the gap to the bid as impairment, not opportunity.
2. *Price.* Bid no more than the price at which probability-weighted NPV at the hurdle is zero. Do not use average IRR.
3. *Protect capital.* No scenario may return less than 0% unlevered. All-cash passes: the impairment case returns 7.90%.
4. *Robustness.* The break-even impairment probability must exceed the assumed probability by at least 10 points. All-cash at \$16.55m: 26.4% against 15%. **Passes.**
5. *Structure preference.* Prefer a structure that removes the refinancing-timing bet (assumption) over one that relies on it (all-cash then refinance), when expected NPV is higher.

**Recommendation (one defensible answer):**

* **Primary offer: \$17.60 million with assumption of the existing 5.00% loan**, conditional on servicer approval within 75 days. Expected IRR 16.41%; expected NPV at 13% +\$0.90 million. The seller's certainty-equivalent is \$17.44 million, \$0.92 million better than the financed bid's.
* **Backup, in the same letter: \$16.55 million all-cash** if the servicer declines. No financing contingency, 30-day close. It beats the financed bid's certainty-equivalent.
* **Walk-away prices:** all-cash above \$16.58 million; with assumption above \$17.96 million (the 15%-hurdle maximum, which leaves margin for the leverage argument).
* **Walk-away events:** T-3 RGI below 105; comp-set RevPAR down more than 5% year over year; the 120-room project obtains a construction loan before closing (see Mode D); the servicer conditions the assumption on a principal paydown that pushes equity above \$8 million.
* **What you are paid for:** You supply certainty and scale of cash when both are scarce, and you can make use of a below-market loan that a weaker buyer could not get approved. You are *not* paid for predicting when credit returns. The bid is built so that it does not need that prediction.

**What would change the conclusion.** Evidence that the 120-room project has financing. A T-3 decline in RGI. A servicer refusal combined with a competing all-cash bidder. A shift in your timing probabilities toward "credit shut": moving 10 points of probability from "1 year" to "shut through exit" lowers the all-cash maximum from \$16.58 million to \$16.30 million, below the financed bid's certainty-equivalent. An increase in the REIT's share price that brings it back as a bidder: the largest single component of the discount would disappear.

---

## Mode C — Blind examination

Use only the Case facts section and Exhibits J-1 to J-3. Do not look at Modes A or B. Allow 120 minutes. Spreadsheets are permitted.

1. (5 pts) Compute occupancy, ADR, RevPAR, and $N$. State the percentage change in $N$ from the pre-crunch T-12.
2. (10 pts) Compute MPI, ARI, and RGI for all three periods and the change in subject and comp-set RevPAR over the last 18 months. Interpret.
3. (10 pts) Compute the NOI hit from the 96-room hotel, and from the 96-room plus the 120-room projects. Explain why the second number matters for a buyer whose plan depends on credit returning.
4. (10 pts) Derive the band-of-investment price for a cash-on-cash buyer with reassessed tax and closing costs. Show when a cut in LTV lowers the price and when it raises it.
5. (15 pts) Compute each buyer type's maximum price under normal and crunch conditions, the clearing price in each, and the marginal buyer.
6. (15 pts) Decompose the clearing-price decline into fundamentals, proceeds, rate, and buyer universe in at least two orders. Classify the discount.
7. (10 pts) Compute the seller's certainty-equivalent of the financed bid.
8. (10 pts) For an all-cash purchase at \$16.55 million, compute scenario IRRs and NPVs at 13%, the expected NPV, and the maximum price. Explain the difference between expected IRR and the IRR of expected cash flows.
9. (10 pts) Value the seller-note and assumable-debt alternatives from the seller's and the buyer's side.
10. (5 pts) State a decision rule and a bid, with walk-away triggers.

Answers: Mode B, and `case_J_rubric.md`.

---

## Mode D — Investment committee

You present to the CIO, the head of asset management, and an outside director who ran a hotel lending desk through two downturns. Prepare written answers, each under 150 words and supported by a number.

1. **"The broker says \$19 million. You say \$16.55 million. Who is right?"** Distinguish the normal-credit clearing price from the crunch clearing price and from the price the seller will accept today.
2. **"Your refinancing works only if credit returns. What else returns with credit?"** Quantify the case in which credit returns in one year *and* the 120-room project is built.
3. **"Why not just bid \$17.2 million all-cash and win outright?"** Use the expected NPV and the naive-underwriting maximum.
4. **"You averaged IRRs to get 13.8%. Defend that number."**
5. **"What is the probability of impairment at which you would not do this deal?"**
6. **"The servicer may take 120 days, not 75, or may refuse. What then?"**
7. **"Is the seller note a better deal for the seller than your assumption bid?"**
8. **"Which part of the 15.5% discount is most likely to reverse first, and what would you watch?"**
9. **"How much of our \$25 million does this tie up, and for how long, in the bad timing case?"**
10. **"Why is this not simply catching a falling knife, as buyers did in 2008?"**

The committee's rubric is in `case_J_rubric.md` (§Mode D).
