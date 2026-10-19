# Case A — The Overpriced Hotel Owner

> **Evidence status:** Every property fact, operating figure, market parameter, and counterparty in this case is [HYPOTHESIS], constructed for teaching. Market ranges such as cap rates, PIP costs, insurance, and tax rates are assumptions chosen to be plausible for a Texas limited-service hotel. They are not sourced market data. Before using any of them in a real valuation, replace them with current, documented evidence: comparable sales, lender quotes, CAD records, and brand PIP letters.
>
> **Model:** `case_a_model.py` (run it to regenerate every number). **Tests:** `tests/test_case_a.py`. **Data:** `cases/datasets/case_a_owner_t12.csv`. **Rubric:** `case_A_rubric.md`.
>
> **Chapters used:** 1 (immediacy, information asymmetry), 8 (NOI), 9 (valuation, loaded cap), 10 (debt sizing), 11 (hotel P&L, PIP).

---

## Case facts (shared by all modes)

**The property.** An 82-room, upper-midscale, nationally franchised limited-service hotel in a secondary Texas market on an interstate corridor. It was built in 2015 and refreshed in 2019. It has a hot breakfast area, a small meeting room, and a fitness room. There is no restaurant or bar.

**The owner.** A first-generation hotelier who developed the property. Total development cost was \$7.6 million: land \$0.7 million, construction \$6.1 million, soft costs and FF&E \$0.8 million. A \$0.4 million soft-goods refresh followed in 2019. The owner manages the hotel personally with family members. **The owner's position: "I have \$8 million in this hotel. My NOI is \$811,000. At a conservative 10% cap that's \$8.1 million. I won't take less than \$8 million."**

**The broker's call.** You are the buy-side analyst for a regional owner-operator. The listing broker sends the owner's trailing-twelve-month (T-12) operating statement (Exhibit A-1) and adds four pieces of information:

1. The brand has told the owner that a property improvement plan (PIP) will be required on change of ownership. No PIP letter has been issued. Your company's recent experience with this brand's PIPs on similar-vintage hotels is **\$7,000–\$9,000 per key**. The case uses \$8,000.
2. In the T-12, a pipeline-construction crew occupied a block of 1,850 room-nights at a negotiated \$112 ADR for five months. The pipeline is finished.
3. The owner's existing loan, with a balance of \$4.3 million, matures in 14 months.
4. "Replacement cost for this product today is \$130–140K a key. Buyers are getting a bargain."

**Market and financing parameters** (assumptions for teaching):

| Parameter | Value |
|---|---|
| Combined property-tax rate | 2.30% of assessed value |
| Assessed value after sale (real property) | 85% of purchase price. Effective tax on price $t$ = 1.955% |
| Market cap rate (NOI after 4% reserve, after reassessed tax): upside / base / downside | 8.75% / 9.50% / 10.50% |
| Management fee if third-party or imputed | 3.0% of total revenue |
| FF&E reserve | 4.0% of total revenue |
| Insurance renewal quote for a new owner | \$68,000 per year |
| Market GM compensation, loaded | \$72,000 |
| Buyer closing costs | 2.0% of price |
| PIP contingency; NOI displacement during PIP | 10%; \$60,000 |
| Acquisition loan | 7.75%, 25-year amortization; max 65% LTV, min 1.40x DSCR, min 11.0% debt yield |
| Variable rooms cost per occupied room | \$14 |
| Share of pipeline room-nights a normal year backfills with transient guests | 40%, at \$119 ADR |
| Replacement cost | \$135,000 per key |

### Exhibit A-1 — Owner's T-12 operating statement (as presented)

| Line | Amount (\$) | Owner's notes |
|---|---:|---|
| Rooms revenue | 2,472,218 | 20,951 room-nights sold of 29,930 available (Occ 70.0%), ADR \$118.00 |
| Other operated revenue | 28,600 | Pantry, pet fees, meeting room |
| Miscellaneous income | 55,000 | "Other income" |
| **Total revenue** | **2,555,818** | |
| Rooms expense | 672,000 | Includes OTA commissions and breakfast |
| Other operated expense | 9,500 | |
| Administrative & general | 264,000 | |
| Sales & marketing | 68,000 | |
| Repairs & maintenance | 162,000 | |
| Utilities | 164,000 | |
| IT & telecom | 26,000 | |
| **Gross operating profit** | **1,190,318** | 46.6% margin |
| Management fee | 0 | Owner-operated |
| Franchise fees | 259,583 | 10.5% of rooms revenue |
| Property tax | 78,200 | Assessed \$3.4m × 2.30% |
| Insurance | 41,000 | |
| FF&E reserve | 0 | |
| **"NOI" (EBITDA)** | **811,535** | |

Detail obtained in a follow-up call with the owner's bookkeeper:
* "Miscellaneous income" is a hail-damage insurance recovery.
* A&G includes \$38,000 of owner vehicle, family phones, and travel. It also includes \$30,000 paid to the owner's spouse, who holds the GM title but works part-time.
* R&M includes a \$62,000 roof replacement.

---

## Mode A — Guided instruction

This section walks through the reasoning. Try each step before reading the commentary.

### Step 1: Why the owner's number is not a value

The owner states three different things:
1. **Cost basis** (\$8.0 million): what the owner spent. It is a sunk cost. A buyer pays for the cash flows the asset will produce, not for what the owner paid. The owner's basis matters only as a *behavioral* fact, because it anchors the owner's reservation price (Chapter 9, anchoring).
2. **Replacement cost** (\$11.07 million at \$135,000/key): what a new, comparable hotel would cost to build today. Replacement cost caps value only when new construction is *feasible*, meaning a developer could build at that cost and earn a return. If the market's income supports only \$5–6 million, nobody will build at \$11 million, so replacement cost is not a floor under value. What it does tell you is that new supply is unlikely in the near term. That supports future NOI, but it is not a value.
3. **Capitalized "NOI"** (\$811,535 / 10% = \$8.1 million): the right method applied to the wrong income at an unsupported cap rate. The owner's figure is pre-reserve EBITDA. It includes non-recurring income and personal expenses, excludes market management, and uses a tax bill that will be reassessed on sale.

### Step 2: Normalize the operating statement

The buyer's question is: *what will this hotel earn, in a normal year, under a new owner who pays market costs?* Work through each item:

| Adjustment | Direction | Reasoning |
|---|---|---|
| Hail insurance proceeds | Remove | Non-operating and non-recurring. |
| Pipeline block | Remove, net of backfill | The crew is gone. Some nights would have sold to transient guests anyway, so remove revenue net of backfill. Variable costs and franchise fees fall with the lost revenue. |
| Owner personal expenses | Add back | They are not hotel costs. |
| Spouse salary to market GM | Replace | A buyer must hire a real GM. |
| Roof replacement | Reclassify as capital | It is capital, not an operating expense. The FF&E reserve funds future capital, so do not count both. |
| Management fee | Deduct 3% | Even an owner-operator's time has a market cost. Lenders impute it. |
| Insurance | Use the buyer's quote | The new owner buys a new policy. |
| FF&E reserve | Deduct 4% | Required by most franchise agreements and by every institutional lender and buyer. |
| Property tax | Re-underwrite at the purchase price | Texas CADs appraise at market value. A sale is evidence of market value, even though Texas does not require disclosure of sale prices. Model reassessment explicitly. |

### Step 3: Handle property-tax reassessment correctly

If tax depends on the price you pay, value and tax are determined *simultaneously*. With pre-tax NOI $N$, cap rate $c$, and effective tax on price $t$:

$$V = \frac{N - tV}{c} \;\Rightarrow\; V = \frac{N}{c + t}.$$

$c + t$ is called the **loaded cap rate**. If you forget reassessment, you capitalize the seller's tax bill and overpay. The size of the overpayment grows with the gap between the old assessment and the price.

### Step 4: Value under scenarios, then adjust for the PIP

Capitalize normalized NOI under several cap-rate and NOI scenarios. Then subtract the PIP (with contingency) and the NOI lost during renovation to get **as-is value**. The PIP is a cost of acquiring the stabilized income stream, so it reduces what a buyer can pay.

### Step 5: Debt and buyer basis

Size the acquisition loan on all three constraints. Compute the buyer's all-in basis: price + closing costs + PIP + displacement. Compute equity required and cash-on-cash return.

### Step 6: Seller motivation and the bid

Ask what the owner can do if they do not sell. With a \$4.3 million loan maturing in 14 months, can the owner refinance on the normalized NOI? If not, the owner faces bringing cash to a refinance, selling, or a lender workout. That is leverage in the negotiation, but it must be used professionally. A bid that the owner cannot accept without bringing cash to closing will not get signed, however correct it is.

---

## Mode B — Solved case

### B.1 Owner's figures re-stated

Occupancy $= 20{,}951 / (82 \times 365) = 20{,}951 / 29{,}930 = 70.00\%$. ADR = \$118.00. RevPAR = \$82.60.

Owner's arithmetic: \$811,535 / 0.10 = \$8,115,350. At the 8.5% cap rate the owner's broker friend suggested: \$9,547,471. Both figures capitalize pre-reserve EBITDA.

### B.2 NOI bridge (owner EBITDA → buyer NOI before property tax)

Pipeline adjustment detail:
* Revenue removed $= 1{,}850 \times \$112 - 0.40 \times 1{,}850 \times \$119 = 207{,}200 - 88{,}060 = \$119{,}140$.
* Net room-nights lost $= 1{,}850 \times 0.60 = 1{,}110$. Variable cost saved $= 1{,}110 \times \$14 = \$15{,}540$.
* Franchise fees saved $= 10.5\% \times 119{,}140 = \$12{,}510$.

| Step | Amount (\$) |
|---|---:|
| Owner-presented EBITDA (no reserve) | 811,535 |
| Add back owner's property tax (re-underwritten below) | +78,200 |
| Remove hail insurance proceeds | −55,000 |
| Remove non-recurring pipeline block, net of backfill | −119,140 |
| Variable rooms cost saved on lost room-nights | +15,540 |
| Franchise fees saved on removed revenue | +12,510 |
| Add back owner personal expenses | +38,000 |
| Replace spouse salary (\$30,000) with market GM (\$72,000) | −42,000 |
| Reclassify roof replacement to capital | +62,000 |
| Market management fee (3% × \$2,381,678) | −71,450 |
| Insurance at buyer's renewal quote (\$41,000 → \$68,000) | −27,000 |
| FF&E reserve (4% × \$2,381,678) | −95,267 |
| **Buyer NOI before property tax, $N$** | **607,927** |

Normalized operating profile: room-nights 19,841. Occupancy 66.29%, ADR \$118.60, RevPAR \$78.62. Total revenue \$2,381,678. GOP \$1,089,718 (45.8% margin).

**Check.** Rebuilt from the top: total revenue 2,381,678 − rooms expense 656,460 − other operated 9,500 − undistributed 626,000 = GOP 1,089,718. Then GOP − management 71,450 − franchise 247,073 − insurance 68,000 − reserve 95,267 = 607,927. ✓

### B.3 Loaded-cap valuation by scenario

Effective tax on price: $t = 2.30\% \times 85\% = 1.955\%$.

| Scenario | NOI multiplier | Cap $c$ | $N$ | Stabilized value $N/(c+t)$ | Reassessed tax | NOI after tax |
|---|---|---|---:|---:|---:|---:|
| Upside | 1.03 | 8.75% | 626,165 | 5,849,277 | 114,353 | 511,812 |
| Base | 1.00 | 9.50% | 607,927 | 5,307,091 | 103,754 | 504,174 |
| Downside | 0.92 | 10.50% | 559,293 | 4,490,510 | 87,789 | 471,504 |

Base-case check: \$504,174 / \$5,307,091 = 9.50%. ✓

**The cost of forgetting reassessment.** Capitalizing NOI that still carries the owner's \$78,200 tax bill gives \$(607{,}927 - 78{,}200)/0.095 = \$5{,}576{,}076$. That overstates base value by **\$268,986**, about 5%. On a thin-margin hotel this is one of the most common and expensive mistakes in Texas underwriting.

### B.4 PIP-adjusted as-is value

PIP all-in = \$8,000 × 82 × 1.10 = \$721,600. Add \$60,000 displacement. Total deduction \$781,600.

| Scenario | Stabilized | As-is | Per key |
|---|---:|---:|---:|
| Upside | 5,849,277 | 5,067,677 | 61,801 |
| Base | 5,307,091 | 4,525,491 | 55,189 |
| Downside | 4,490,510 | 3,708,910 | 45,231 |

Against the owner's \$8.0 million, the base as-is value is **43% lower**. Even the upside scenario is 37% below the ask. The difference is not a rounding issue. It comes from four errors in the owner's figure: pre-reserve income, non-recurring items, a non-market cost structure, and an ignored PIP.

To justify \$8.0 million, the buyer would have to accept a **5.64%** going-in yield on price (NOI after reassessed tax of \$451,527 at that price). On an all-in basis of \$8.94 million the yield would be **5.05%**. That is below the acquisition loan rate of 7.75%, which means negative leverage on a high-beta asset. No rational buyer with financing accepts it.

### B.5 Financing and buyer basis at candidate prices

The buyer's bid rule is to reach a target **yield on all-in cost** (NOI after reassessed tax ÷ (price × 1.02 + PIP all-in + displacement)). The bid price solves $N - tP = y[P(1.02) + 781{,}600]$, so $P = (N - 781{,}600\,y)/(t + 1.02\,y)$:

| Target yield on cost | Price | Loan (binding) | Debt service | DSCR | Equity | Cash-on-cash |
|---|---:|---:|---:|---:|---:|---:|
| 9.5% | 4,582,870 | 2,978,866 (LTV) | 270,003 | 1.92x | 2,477,262 | 10.02% |
| 10.0% | 4,358,431 | 2,832,980 (LTV) | 256,780 | 2.04x | 2,394,219 | 11.11% |
| 10.5% | 4,152,067 | 2,698,843 (LTV) | 244,622 | 2.15x | 2,317,865 | 12.17% |

Equity includes closing costs and the PIP, which is funded with equity in this structure. LTV binds in every case because the lender sizes on price, and the price is low relative to NOI. DSCR and debt-yield capacity are unused. A lender might fund part of the PIP as future advances, but that is a negotiation point, not an assumption.

### B.6 The seller's alternatives

**Refinance.** The lender underwrites normalized NOI with the existing tax bill (no reassessment on a refinance): $607{,}927 - 78{,}200 = \$529{,}727$. Appraised value at 9.5% = \$5,576,076. Maximum loan = min(65% LTV = \$3,624,450; DSCR = \$4,174,524; debt yield = \$4,815,702) = **\$3,624,450**, with LTV binding. With 1.5% refinancing costs, the owner must bring **\$729,917** to refinance the \$4.3 million balance.

**Sell.** To pay off \$4.3 million after 3% selling costs, the owner needs a price of at least **\$4,432,990** to avoid bringing cash to closing.

**Implication.** The owner's practical floor is not \$8.0 million. It is roughly \$4.43 million: below that the owner must write a check, and above it the owner walks away with cash. The buyer's 9.5%–10.0% yield-on-cost range (\$4.36–\$4.58 million) straddles that floor. That is the negotiating zone, and it is where a deal is plausible *if* the owner can be brought from the cost-basis anchor to the economics.

### B.7 Recommendation (one defensible answer)

* **Opening bid: \$4.35 million**, about a 10.0% yield on all-in cost. Conditions: a PIP letter at or below \$9,000 per key, satisfactory PCA, and 30-day diligence.
* **Maximum price: \$4.60 million**, about a 9.5% yield on cost, near the base as-is value. Justify going above \$4.45 million only if the PIP letter comes in at or below \$7,000 per key, or if the STR data show the T-12 decline in penetration is reversing.
* **Walk away if:** the PIP exceeds \$11,000 per key without a price reduction; the T-3 RevPAR index has fallen below 95; or insurance cannot be bound at or below \$75,000.
* **Negotiation approach:** Present the NOI bridge line by line, so the owner sees each adjustment as a fact rather than an opinion. Show the refinancing arithmetic, which tells the owner something their lender will soon tell them anyway. Point out that a \$4.45 million price pays off the loan without a check, and that the PIP risk passes to the buyer.
* **What you are paid for:** You absorb PIP execution risk, insurance and tax uncertainty, and a hotel with no professional management in place. You provide certainty to an owner facing a maturity.

**What would change the conclusion.** A PIP letter at \$5,000/key or less. Evidence that the pipeline crew will return, or that a new demand generator is coming. A financing market offering 75% LTV. A lower cap-rate environment confirmed by recent comparable sales. Any of these moves value upward, and the bid should move with it. The cost basis and replacement cost should not.

---

## Mode C — Blind examination

Use only the Case facts section and Exhibit A-1. Do not look at Modes A or B. Allow 90 minutes. Calculators and spreadsheets are permitted.

1. (5 pts) Compute occupancy, ADR, and RevPAR from the owner's statement.
2. (5 pts) Identify every line item that requires normalization and say why.
3. (20 pts) Build the NOI bridge from owner EBITDA to buyer NOI before property tax. Show the pipeline calculation explicitly.
4. (10 pts) Derive the loaded cap-rate formula. Value the hotel at a 9.5% cap with reassessment. Quantify the error from forgetting reassessment.
5. (10 pts) Compute as-is values in the three scenarios after the PIP.
6. (10 pts) Explain, with numbers, why neither the owner's cost basis nor replacement cost sets value.
7. (10 pts) Size the acquisition loan at your proposed price. State the binding constraint.
8. (10 pts) Compute the owner's refinancing gap and the payoff price.
9. (15 pts) Write a bid letter summary: price, conditions, walk-away triggers, and a two-paragraph explanation for the owner.
10. (5 pts) Name two facts that would most increase your bid and two that would most decrease it.

Answers: Mode B, and `case_A_rubric.md`.

---

## Mode D — Investment committee

You present the recommendation to a three-member investment committee: the CIO, the head of asset management, and an outside director who was formerly a lender. Prepare written answers. Each should be under 150 words and supported by a number.

1. **Why is your NOI better than the owner's?** Which adjustment is most contestable, and what happens to value if you are wrong about it? (Hint: the pipeline backfill share and the insurance quote are the most contestable. Compute the value effect of 70% backfill.)
2. **What is already reflected in the price?** If the market already knows about the PIP, are you double-counting it by also using a 9.5% cap?
3. **What if exit cap rates widen another 100 bp** by the time you sell in year five?
4. **How much cash can you lose before the debt matures**, and what is the hotel's break-even occupancy at the proposed price?
5. **What forces the owner to transact?** What if the lender extends the loan?
6. **What is the most likely way this thesis fails?**
7. **What data would cause you to withdraw the bid?**
8. **Why is this better than owning 5-year Treasuries?**
9. **How would you hedge the risks?** Which risks cannot be hedged?
10. **Why must we transact now rather than wait for the maturity to force a lower price?**

The committee's rubric for these answers is in `case_A_rubric.md` (§Mode D).
