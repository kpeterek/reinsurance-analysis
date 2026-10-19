# Case D — The Hotel PIP Negotiation

> **Evidence status:** Every property fact, operating figure, contract term, market parameter and counterparty in this case is [HYPOTHESIS], constructed for teaching. PIP costs, cap rates, lender terms, liquidated-damages formulas and brand premiums are plausible assumptions, not sourced market data. Before using any of them in a real negotiation, replace them with the actual PIP letter, franchise agreement, lender term sheet, PCA and comparable sales.
>
> **Model:** `case_d_model.py` (run it to regenerate every number). **Tests:** `tests/test_case_d.py`. **Data:** `cases/datasets/case_d_pip_items.csv` (PIP and PCA line items) and `cases/datasets/case_d_monthly_demand.csv` (monthly demand profile). **Rubric:** `case_D_rubric.md` (instructor file; keep separate).
>
> **Chapters used:** 1 (break-even probability, information asymmetry), 9 (valuation), 10 (debt sizing, reserves), 11 (hotel P&L, flow-through, displacement, PIP pricing, brand economics), 13 (hold/sell timing).

---

## Case facts (shared by all modes)

**The property.** A 118-room upscale select-service hotel with a national flag, on a suburban medical and office corridor in a Sun Belt metro. Built in 2008. Soft goods were last replaced in 2015; case goods, bathrooms and the lobby are original. There is a breakfast area, a small bar, a 1,200 sf meeting room, a pool and a fitness room.

**The franchise.** The franchise agreement expires in **26 months**. It cannot be assigned to a buyer. On a change of ownership the brand will offer the buyer a new 15-year agreement conditioned on a PIP. On expiry, the brand will renew with the current owner only on the same PIP. If the agreement is terminated early (for example, because a buyer de-flags at closing), the owner owes liquidated damages equal to 24 months of average royalty and marketing fees (8.5% of rooms revenue).

**The owner.** A single-asset partnership whose managing partner developed the hotel. The partnership's loan, with a balance of **\$7.4 million**, matures in 11 months. **The owner's position:** "Trailing NOI is \$1.11 million after the reserve. At an 8.5 cap that's \$13.0 million, and the hotel is worth more than that because it's the best-located hotel on the corridor. I'm asking \$13.5 million. The PIP is the brand's wish list. I'll negotiate it down at renewal, and in any case a buyer will get the upside from the renovation. I'm not giving it away twice."

**You** are the acquisitions director for a regional owner-operator. In diligence you have obtained:

1. **The T-12** (normalized by your team; Exhibit D-1).
2. **The PIP letter** (Exhibit D-2). It was issued to the owner six months ago for the renewal and reissued, unchanged, for a change of ownership.
3. **A property condition assessment (PCA)**, which identifies \$410,000 of capital needs outside the PIP.
4. **The STR report.** The comp set's T-12 occupancy is 72.0% at a \$145.00 ADR. The subject's quarterly RGI over the last four quarters, oldest first, is 106, 104, 102, 99.
5. **A lender term sheet** (Exhibit D-4).
6. **A monthly demand profile** (Exhibit D-3) for planning the renovation.

### Exhibit D-1 — Normalized T-12 (\$)

| Line | Amount | Note |
|---|---:|---|
| Occupancy / ADR / RevPAR | 73.5% / \$146.00 / \$107.31 | 31,656 room-nights of 43,070 |
| Rooms revenue | 4,621,842 | |
| Other revenue (3% of rooms) | 138,655 | |
| **Total revenue** | **4,760,497** | |
| Rooms expense (\$33 per occupied room) | 1,044,663 | |
| Other departmental expense (50%) | 69,328 | |
| Undistributed (\$1,180,000 + 3.5% of revenue) | 1,346,617 | |
| **GOP** | **2,299,889** | 48.3% |
| Management fee (3%) | 142,815 | |
| Franchise fees (12% of rooms) | 554,621 | |
| Property tax / insurance | 205,000 / 98,000 | |
| **EBITDA** | **1,299,453** | |
| FF&E reserve (4%) | 190,420 | |
| **NOI** | **1,109,033** | |

### Exhibit D-2 — PIP letter and PCA (from `case_d_pip_items.csv`)

| Item | Basis | \$ |
|---|---|---:|
| Guestroom soft goods (carpet, drapery, bedding, wallvinyl) | \$7,500/key | 885,000 |
| Guestroom case goods and seating | \$6,000/key | 708,000 |
| Bathrooms: tub-to-shower conversions, vanities, lighting | \$5,500/key | 649,000 |
| PTAC/HVAC replacement | \$1,400/key | 165,200 |
| Lobby, breakfast area, public restrooms | lump sum | 420,000 |
| Exterior: new-standard signage, paint, porte-cochère | lump sum | 260,000 |
| Pool and fitness | lump sum | 95,000 |
| Technology: Wi-Fi backbone, mobile key | lump sum | 110,000 |
| **PIP hard cost** | \$27,900/key | **3,292,200** |
| PCA items outside the PIP: roof \$180,000; parking lot \$95,000; elevator \$135,000 | | **410,000** |

Your team's planning assumptions: soft costs (design, permits, purchasing agent, project management) 8% of hard cost; contingency 12%; required profit on PIP capital 15%; negative carry, extra legal and brand application fees \$150,000.

### Exhibit D-3 — Demand profile and renovation plan

| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T-12 occupancy | 64% | 72% | 80% | 79% | 78% | 76% | 74% | 71% | 76% | 82% | 71% | 59% |

Weekday (Mon–Thu) demand runs 1.15× the monthly average and weekend demand 0.80×. The renovation takes six months, one floor at a time, with **20 rooms out of order** throughout. Rooms sold during the works carry a 5% rate concession for noise and a closed lobby. Lost contribution per displaced room-night is ADR × (1 + other revenue share) × (1 − revenue-variable costs of 22.15%) − \$33 = **\$90.09**.

### Exhibit D-4 — Lender term sheet and market parameters

| Item | Value |
|---|---|
| Rate / amortization | 7.60% / 25 years, monthly |
| Maximum loan-to-cost (price + 2% closing + PIP all-in + PCA items) | 65% |
| Minimum as-is debt yield (T-12 NOI) | 10.5% |
| Minimum DSCR on underwritten stabilized NOI | 1.35x |
| PIP funding | Lender funds up to 75% of PIP all-in. Structure 1: funded at closing into a lender-controlled PIP reserve. Structure 2: future advances against completed work, after the borrower has spent its 25% |
| Cap rate, renovated and branded (NOI after 4% reserve) | 8.75% |
| Cap rate, dated PIP-encumbered comps (reference only) | 9.25% |
| Post-PIP stabilized performance | RGI 106 at 75% occupancy against a forward comp set of 72% / \$150.00 |
| Independent alternative | RGI 88 at 68% occupancy; 7% distribution costs; \$150,000 added sales and marketing; \$350,000 de-flagging plus \$6,000/key refresh; 9.75% cap |
| Your opening yield-on-cost discipline | 9.50% on stabilized NOI over all-in cost |
| Seller's selling costs; refinancing costs | 3%; 1.5% |
| Owner's discount rate (concentrated single-asset partnership) | 12% |

---

## Mode A — Guided instruction

Work each step before reading the commentary.

### Step 1: Is the PIP a liability or an option?

The owner frames the PIP as optional: something to negotiate at renewal, and a source of upside for the buyer. Test that framing against the documents. The PIP is triggered by two events, and the owner controls neither of them: the franchise expires in 26 months, and any sale is a change of ownership. The brand has issued the same letter for both. Unless the owner is prepared to lose the flag, the PIP is a **liability that already exists**. Only its timing is uncertain. The quarterly RGI trend (106 → 99) suggests the market already sees the product as dated. Part of the "upside" from renovating is the recovery of share that has already been lost.

### Step 2: Separate the three capital claims

Do not let the FF&E reserve, the PIP and the PCA items blur together. The 4% reserve (\$190,420 a year) funds routine replacement and is already deducted in NOI. The PIP (\$3.29 million hard, \$3.98 million all-in) is a brand-mandated renovation the reserve has not funded. The PCA items (\$410,000) are needed regardless of the brand. A buyer who deducts only the PIP is still buying a roof.

### Step 3: Renovation downtime is a monthly calculation

Displacement is not "rooms out of order × occupancy". With 98 of 118 rooms open, the hotel loses business only on nights when demand exceeds 98 rooms. That depends on the month and the day of the week. Compute it from Exhibit D-3, and compare a start in November (low season first) with a start in March (peak months first). Add the rate concession on rooms that do sell.

### Step 4: Read the financing constraints

Three constraints apply: loan-to-cost, as-is debt yield on the T-12, and DSCR on stabilized NOI. Which binds? Then compare the two PIP-funding structures. They require the same total equity but at different times, and structure 1 pays interest on money sitting in a reserve.

### Step 5: Price the alternatives to the brand

If the PIP is not done, the flag goes. Compute what the independent hotel is worth, and remember the liquidated damages if the flag is dropped before expiry. This is the realistic alternative against which the PIP must be judged.

### Step 6: The return on renovation

Ask two questions. What RevPAR lift would the PIP need to earn a 10% return on its all-in cost on its own (equation 11.4)? And what return does it earn relative to losing the flag? The first question is the one owners ask. The second is the one that decides.

### Step 7: Price the hotel

Use `sdesk.hotel.pip_adjusted_price` with the stabilized value, PIP base cost, contingency, displacement, carry plus PCA items, and required profit. That is your **walk-away price**: the most you can pay and still be paid for taking renovation risk. Then compute the **opening bid** from your 9.50% yield-on-cost discipline. Express both as yields on all-in cost and compare with the owner's ask.

### Step 8: Understand the seller's alternatives

What does the owner actually face? (a) Refinance in 11 months: a lender will size on T-12 NOI and require a funded PIP reserve, because the flag expires during the new loan. (b) Hold, renovate at renewal, then sell. (c) Ignore the PIP and lose the flag. Value each from the owner's side at the owner's discount rate. The owner's real reservation price comes from these alternatives, not from the \$13.5 million anchor.

### Step 9: Walk-away conditions

Write them before negotiating. A walk-away that is decided at the table is not a walk-away.

---

## Mode B — Solved case

### B.1 What the owner's number is

At 8.5% the T-12 NOI of \$1,109,033 gives \$13,047,450. The ask of \$13.5 million is an **8.22%** cap on T-12 NOI. On an all-in basis (ask plus 2% closing, PIP all-in, displacement, carry and PCA items: \$18,431,559) the stabilized NOI of \$1,330,702 is a **7.22%** yield on cost, **153 bp below** the 8.75% cap rate at which the renovated hotel would be valued. A buyer at the ask would spend \$18.4 million to create an asset worth \$15.2 million.

### B.2 The PIP budget

| | \$ | Per key |
|---|---:|---:|
| Hard cost | 3,292,200 | 27,900 |
| Soft costs (8%) | 263,376 | |
| PIP base | 3,555,576 | 30,132 |
| Contingency (12%) | 426,669 | |
| **PIP all-in** | **3,982,245** | |
| PCA items outside the PIP | 410,000 | |

### B.3 Displacement by month

**Start in November** (Nov–Apr):

| Month | Demand (room-nights) | Lost room-nights | Lost NOI (\$) |
|---|---:|---:|---:|
| Nov | 2,513 | 0 | 15,018 |
| Dec | 2,158 | 0 | 12,895 |
| Jan | 2,341 | 0 | 13,988 |
| Feb | 2,379 | 0 | 14,214 |
| Mar | 2,926 | 187 | 33,219 |
| Apr | 2,797 | 158 | 29,979 |
| **Total** | | **345** | **119,314** |

March, for example: weekday demand $0.80 \times 1.15 \times 118 = 108.6$ rooms against 98 open, so $31 \times \tfrac{4}{7} \times 10.6 = 187$ room-nights are lost; weekend demand (75.5 rooms) fits. In November through February no demand is lost; the only cost is the 5% concession.

**Start in March** (Mar–Aug): lost room-nights 187, 158, 139, 88, 43, 0 (total 615); lost NOI **\$150,707**. Starting in November saves \$31,393. Use \$119,314.

### B.4 Stabilized value and the independent alternative

| | Renovated, branded | Independent |
|---|---:|---:|
| RevPAR | \$114.48 | \$95.04 |
| ADR | \$152.64 | \$139.76 |
| Total revenue | 5,078,573 | — |
| NOI | 1,330,702 | 826,048 |
| Cap rate | 8.75% | 9.75% |
| Value | 15,208,026 (\$128,882/key) | 8,472,290 |
| Capital required (beyond PCA) | 3,982,245 | 1,058,000 |
| Value net of capital and PCA items | 10,815,781 | 7,004,290 |

Liquidated damages if the flag is dropped before expiry: $0.085 \times 4{,}621{,}842/12 \times 24 = \$785{,}713$.

### B.5 Return on renovation

NOI flow-through on rate-led rooms revenue, computed from the P&L: **78.69%**. To earn 10% on \$3,982,245, NOI must rise \$398,225, which requires a RevPAR lift of $398{,}225/(118 \times 365 \times 0.7869) = \$11.75$: **10.95%**, to \$119.06. The projected lift is \$7.17 (to \$114.48), raising NOI by \$221,669: a stand-alone return of **5.57%**. On its own the PIP does not pay.

Against the realistic alternative, losing the flag, the PIP adds \$504,654 of NOI for \$2,924,245 more capital than independence requires: **17.26%**. The PIP is defensive capital. Its job is to keep the flag, and at that job it earns well. This is also why the owner's "the buyer gets the upside" is wrong: most of the PIP's return is the avoidance of a loss the owner already faces.

### B.6 Price: walk-away and opening bid

Walk-away (`sdesk.hotel.pip_adjusted_price`):

$$P = 15{,}208{,}026 - 3{,}982{,}245 - 119{,}314 - 560{,}000 - 0.15 \times 3{,}982{,}245 = \$9{,}949{,}131,$$

where \$560,000 is carry and fees (\$150,000) plus PCA items (\$410,000) and the required profit is \$597,337. That is **\$84,315 per key**, and an 8.99% yield on all-in cost of \$14,809,672: 23.5 bp above the stabilized cap rate.

Opening bid at a 9.50% yield on cost: **\$9,162,582** (\$77,649 per key; all-in \$14,007,392).

| | Price | Per key | Yield on all-in cost | Spread to 8.75% cap |
|---|---:|---:|---:|---:|
| Owner's ask | 13,500,000 | 114,407 | 7.22% | −153 bp |
| Walk-away | 9,949,131 | 84,315 | 8.99% | +24 bp |
| Opening bid | 9,162,582 | 77,649 | 9.50% | +75 bp |

The gap between the ask and the walk-away is \$3,550,869, of the same order as the PIP all-in (\$3,982,245): the ask prices the hotel as if the PIP did not exist. At the walk-away price the T-12 cap rate is **11.15%**. The owner will call that a "vulture" cap rate. It is the T-12 NOI over a price that has already deducted a \$4 million obligation.

### B.7 Financing at the walk-away price

Total cost $= 9{,}949{,}131 \times 1.02 + 3{,}982{,}245 + 410{,}000 = \$14{,}540{,}358$. Loan constant 8.95%.

| Constraint | Loan |
|---|---:|
| 65% loan-to-cost | **9,451,233 (binding)** |
| 10.5% as-is debt yield on T-12 NOI | 10,562,222 |
| 1.35x DSCR on stabilized NOI | 11,018,274 |

| | Structure 1: funded reserve | Structure 2: future funding |
|---|---:|---:|
| Loan funded at closing | 9,451,233 | 6,464,549 |
| PIP share of loan (75% of PIP all-in) | 2,986,684 (in reserve) | 2,986,684 (advanced on completion) |
| Equity at closing | 5,089,125 | 4,093,564 |
| Equity spent on the PIP first | — | 995,561 |
| Total equity | 5,089,125 | 5,089,125 |
| Interest on idle reserve (about 4 months on average) | ≈ 75,663 | — |

Equity is 35% of total cost under either structure. Structure 2 saves the negative carry but leaves the borrower exposed to the lender's draw process and inspections; structure 1 is simpler but costs about \$76,000, which is already inside the \$150,000 carry assumption. Debt service \$845,516: DSCR 1.31x on T-12 NOI, 1.57x stabilized; LTV 62.2% on stabilized value. Break-even occupancy after debt service is **66.0%** at the T-12 ADR (42.1% before debt service), against 73.5% achieved, a 7.5-point cushion that is smallest during the renovation.

### B.8 The seller's position

**Refinance.** A lender sizes on T-12 NOI: min(10.5% debt yield → \$10,562,222; 1.35x DSCR → \$9,182,845) = \$9,182,845. After 1.5% costs and the \$7.4 million payoff, cash-out is \$1,645,102. The lender will require a funded PIP reserve of \$3,982,245 because the flag expires during the loan term. **The owner must write a check of \$2,337,143** to refinance. The PIP cannot be avoided by refinancing.

**Sell.** At the walk-away price the owner nets \$2,250,657 after 3% costs and the loan payoff; at the opening bid, \$1,487,705.

**Hold and renovate.** Years 1–2 unrenovated (RGI erodes to 97 and 95; occupancy 69.4% and 67.9%; NOI \$963,091 and \$912,656). Year 3: renovate and stabilize (NOI \$1,330,702 less \$119,314 displacement, PIP all-in and PCA items: −\$3,180,857), sell at the end of year 3 on year-4 NOI for \$15,194,339 net. PV at 12%: **\$10,138,426**, equivalent to a gross price of \$10,451,986 today.

**Ignore the PIP.** Keep the flag to expiry, operate independent from year 3 (capital \$1,058,000 plus PCA), sell at the end of year 3 for \$8,464,664 net. PV at 12%: **\$7,155,519**.

**The owner's break-even.** Selling at the walk-away price is worth \$9,650,657 to the owner after selling costs. Holding beats selling only if the owner's probability of funding and executing the PIP (rather than ending up de-flagged) exceeds

$$p^* = \frac{9{,}650{,}657 - 7{,}155{,}519}{10{,}138{,}426 - 7{,}155{,}519} = 83.6\%.$$

An owner who must write a \$2.3 million check just to refinance, with a renovation that he publicly calls a wish list, is unlikely to be 84% confident of executing it.

### B.9 Recommendation (one defensible answer)

* **Opening bid: \$9.15 million** (about \$77,500 per key), presented with the PIP letter, the displacement schedule and the refinancing arithmetic. Conditions: brand approval of a new 15-year agreement on the issued PIP with no scope additions; PCA items confirmed by contractor bids; 45-day diligence.
* **Walk-away: \$9.95 million.** Above it the buyer is doing the renovation for less than a 15% return on renovation capital.
* **Structure options that move the headline without moving value:** a seller credit at closing for the PCA items. At the walk-away, for example, a headline price of \$10.36 million with a \$410,000 credit is the same economics as \$9.95 million, and may be the number the owner needs to show his partners.
* **Walk away if:** the brand adds scope or will not issue a comfort letter; contractor bids put the PIP hard cost above about \$3.7 million (each 20% on the PIP base costs \$915,916 of price); the T-3 RGI falls below 97; the lender's as-is debt yield or LTC terms tighten so that equity exceeds 40% of cost; or the seller will not give access for a pre-closing measurement survey of the bathrooms.
* **Negotiation approach:** Do not argue about the cap rate. Show the owner the refinancing check (\$2.3 million), the independent alternative (\$7.2 million PV), and the break-even probability (84%). The owner's anchor is \$13.5 million; his best realistic alternative is close to the walk-away.

**What would change the conclusion.** A PIP letter negotiated down by the owner before sale (raises the walk-away dollar for dollar, grossed up by contingency and profit). Evidence that post-PIP RGI will exceed 106. A lender offering 75% LTC. A lower renovated cap rate supported by comparable sales. Any of these should move the bid. The owner's cost of development and the T-12 cap rate should not.

---

## Mode C — Blind examination

Use only the Case facts and Exhibits D-1 to D-4. Do not look at Modes A or B. Allow 120 minutes. Spreadsheets and the `sdesk` library are permitted.

1. (5 pts) Compute RevPAR, MPI, ARI and RGI from the T-12 and comp-set data. What does the quarterly RGI trend suggest?
2. (5 pts) Distinguish the FF&E reserve, the PIP and the PCA items, and state how each enters your valuation.
3. (10 pts) Compute the PIP budget: soft costs, contingency and all-in cost.
4. (15 pts) Compute monthly displacement for a November start and a March start. Which do you choose, and what is the saving?
5. (10 pts) Compute stabilized NOI and value, and the independent alternative's NOI, value and net value. Compute the liquidated damages.
6. (10 pts) Compute the RevPAR lift the PIP needs to earn 10% on its own, the projected lift and stand-alone return, and the return relative to independence. Explain which comparison decides.
7. (15 pts) Compute the walk-away price with `pip_adjusted_price`, the opening bid at a 9.50% yield on cost, and the owner's ask as a yield on all-in cost.
8. (10 pts) Size the loan at the walk-away price; name the binding constraint; compare equity timing under the two PIP-funding structures.
9. (10 pts) Compute the owner's refinancing check, hold-and-renovate PV, ignore-the-PIP PV, and the break-even probability.
10. (10 pts) Write the bid summary: price, structure, conditions, walk-away triggers, and a two-paragraph explanation for the owner.

Answers: Mode B and `case_D_rubric.md`.

---

## Mode D — Investment committee

You present to the CIO, the head of asset management, and an outside director who spent twenty years as a hotel lender. Each answer must be under 150 words and supported by a number.

1. **The owner says the PIP is negotiable at renewal. Why are you deducting all of it?**
2. **What happens to your walk-away price if the exit cap rate is 9.25% rather than 8.75%?**
3. **What if the PIP comes in 20% over budget?**
4. **What if the renovation only restores RGI to 102, not 106?**
5. **Why November? What if the brand insists on a spring start?**
6. **Which lender structure do you prefer, and what does it cost?**
7. **How thin is the cushion during the renovation?** Give break-even occupancy at the walk-away price.
8. **Why should the owner accept a price \$3.5 million below his ask?**
9. **What is the most likely way this deal fails after closing?**
10. **Why not wait 11 months for the loan maturity to force a lower price?**

The committee's rubric is in `case_D_rubric.md` (§Mode D).
