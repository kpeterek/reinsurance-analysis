# Case I — The Development Land Option

> **Evidence status:** Every property fact, cost, rent, cap rate, probability, and counterparty in this case is [HYPOTHESIS], constructed for teaching. Market parameters such as hard costs per unit, cap rates, entitlement odds, and land bids are assumptions chosen to be plausible for suburban North Texas garden multifamily. They are not sourced market data. Before using any of them, replace them with current evidence: contractor bids, appraisals, comparable land sales, and the city's actual zoning calendar.
>
> **Model:** `case_i_model.py` (run it to regenerate every number). **Tests:** `tests/test_case_i.py`. **Rubric:** `case_I_rubric.md`.
>
> **Chapters used:** 1 (immediacy, do-nothing alternative), 9 (residual land value), 10 (construction financing), 13 (real options, waiting, binomial trees), 18 (option pricing).

---

## Case facts (shared by all modes)

**The site.** Twelve acres on an arterial road in a growing North Texas suburb. Utilities are at the property line. The current zoning permits **240 garden apartment units by right**. A planned-development (PD) rezoning would permit **330 units**, with smaller units and a more efficient site plan.

**The owner.** A family partnership bought the land in 2009 for \$900,000. The partners have no development experience, no construction lender relationships, and about \$3 million of liquid capital among them. One partner says: "We paid \$900,000. Anything above \$5 million is a home run. Take the bid."

**The bid.** A merchant builder has offered **\$5.4 million cash** for the site as currently zoned, closing in 60 days, with no entitlement contingency.

**The alternatives the family is considering:**

1. **Sell the site now** to the merchant builder.
2. **Build now** under the by-right zoning, hiring a fee developer.
3. **Wait one year**, then sell (or build) depending on market conditions.
4. **Entitle and sell**: spend \$450,000 over 12 months pursuing the PD rezoning, then sell the site, entitled or not.
5. **Joint venture**: contribute the land at an agreed value of \$6.0 million to a JV with a developer, who funds the rest of the equity and builds the by-right project now.

**Market and development parameters** (assumptions for teaching):

| Parameter | Value |
|---|---|
| Stabilized NOI per unit, after reserves, at today's rents | \$16,500 |
| Stabilized cap rate (also the cash yield forgone by waiting) | 5.50% |
| Selling costs on the completed project | 2.0% of GDV |
| Hard cost per unit: by-right 240 / PD 330 | \$195,000 / \$192,000 |
| Soft costs | 12% of hard costs |
| Construction financing cost | 6% of hard + soft |
| Required developer margin on total cost | 15% |
| Escalation of all non-land costs | 4% a year |
| Completed value next year | ×1.20 or ×1/1.20 (= ×0.8333) |
| Risk-free rate | 4.5% |
| Land carry (tax, insurance, upkeep) | \$60,000 a year, paid at year-end |
| Alternative-use land value (retail pad / storage buyer) next year | \$1.5 million |
| Land sale costs | 3% |
| Fee developer cost if the family builds | 3% of hard costs |
| PD approval probability | 60% (independent of the market) |
| JV: land credit; loan-to-cost; preferred return; split above it | \$6.0m; 60%; 8% IRR; 70% to capital / 30% promote to the developer |
| JV completed-value scenarios at sale (year 2) | ×0.85 (25%), ×1.00 (50%), ×1.15 (25%) |
| Family's required return on a development-equity interest | 12% |

---

## Mode A — Guided instruction

### Step 1: The family's cost is not a value

The \$900,000 is sunk. It anchors the partner's sense of a "home run" but tells you nothing about what the site is worth. The questions are: what does the site's best use support, and what is the option to choose that use later worth?

### Step 2: Residual land value

A developer pays for land whatever is left after the completed project's value covers all other costs and the developer's required margin. With GDV net of selling costs $N$, non-land costs $H + S + F$, and margin $m$ on total cost:

$$N = (L + H + S + F)(1 + m) \;\Rightarrow\; L = \frac{N}{1+m} - (H + S + F).$$

This is `sdesk.cre.residual_land_value`. Note the **leverage** in the formula. Land is a thin residual between two large numbers, so a 20% change in GDV moves land value by far more than 20%.

### Step 3: Why a single RLV understates the site

Residual land value is a static valuation: it assumes you build today. The landowner is not obliged to build today. The landowner holds an **option**: to build, sell, or rezone later, when more is known. The down states are truncated by the option not to build (the land keeps its alternative-use value), while the up states are not. Section 13.4.8 shows how to value that asymmetry with a binomial tree.

### Step 4: Separate market risk from entitlement risk

The change in completed value is market risk. Price it with risk-neutral probabilities: $q = (1 + r - \delta - d)/(u - d)$, where $\delta$ is the 5.5% NOI yield a landowner forgoes. The PD vote is idiosyncratic. It does not depend on the market and can be diversified away across many sites, so weight it with its real-world probability inside each market node.

### Step 5: Put each alternative on the same basis

Express each alternative as a present value to the family today, net of every cost the family bears: sale costs, carry, entitlement spending, fee-developer cost, and the JV's waterfall.

### Step 6: Ask what the family can actually execute

Building requires roughly \$20+ million of equity and a construction loan. The family has about \$3 million. An alternative that cannot be financed is not an alternative, however high its PV.

---

## Mode B — Solved case

### B.1 Residual land values today

| | By-right 240 | PD 330 |
|---|---:|---:|
| GDV = units × \$16,500 / 5.5% | 72,000,000 | 99,000,000 |
| Net of 2% selling costs, $N$ | 70,560,000 | 97,020,000 |
| Hard | 46,800,000 | 63,360,000 |
| Soft (12%) | 5,616,000 | 7,603,200 |
| Financing (6% of hard + soft) | 3,144,960 | 4,257,792 |
| Non-land cost | 55,560,960 | 75,220,992 |
| $N/1.15$ | 61,356,522 | 84,365,217 |
| **Residual land value** | **5,795,562** | **9,144,225** |
| Per unit / per acre | \$24,148 / \$482,963 | \$27,710 / \$762,019 |

The \$5.4m bid is 93% of the by-right RLV. The PD rezoning would add about \$3.35m of land value if it were approved today.

**Leverage check.** A 20% rise in GDV to \$86.4m, with costs escalated one year, gives an RLV of \$15.84m, up 173%. A fall to \$60.0m gives −\$6.65m: no one would build, and the land falls to its \$1.5m alternative-use value.

### B.2 The market tree

$q = (1 + 0.045 - 0.055 - 0.8333)/(1.20 - 0.8333) = 0.4273$.

| Next-year node | Completed-value multiple | RLV by-right (costs +4%) | RLV PD 330 | Land value used |
|---|---:|---:|---:|---|
| Up | 1.20 | 15,844,428 | 23,008,429 | depends on zoning |
| Down | 0.8333 | −6,652,964 | −7,925,484 | floor 1,500,000 |

### B.3 The five alternatives

| Alternative | Calculation | PV to family |
|---|---|---:|
| 1. Sell now | 5,400,000 × 0.97 | **5,238,000** |
| 2. Build now (fee developer) | RLV 5,795,562 − 3% × 46,800,000 = 5,795,562 − 1,404,000 | **4,391,562** |
| 3. Wait one year, then sell | [(0.4273 × 15,844,428 + 0.5727 × 1,500,000) × 0.97 − 60,000] / 1.045 | **7,024,032** |
| 4. Entitle and sell | see below | **8,278,809** |
| 5. JV (build now) | see below | **6,162,768** |

*Entitle and sell.* Up node: approved \$23,008,429 (p = 0.60) or denied \$15,844,428, expected \$20,142,829. Down node: \$1,500,000 either way. PV $= [(0.4273 \times 20{,}142{,}829 + 0.5727 \times 1{,}500{,}000) \times 0.97 - 60{,}000]/1.045 - 450{,}000 = \$8{,}278{,}809$.

Break-even approval probability: entitlement beats waiting without it if $p > 15.8\%$.

*Joint venture.* Total cost $= 6{,}000{,}000 + 55{,}560{,}960 = \$61{,}560{,}960$. Loan (60%) \$36,936,576. Equity \$24,624,384: family land credit 24.37%, developer cash \$18,624,384.

| Scenario | p | Equity proceeds, year 2 | To capital (both partners) | Promote | Family share | Project equity IRR |
|---|---:|---:|---:|---:|---:|---:|
| ×0.85 | 0.25 | 23,039,424 | 23,039,424 | 0 | 5,613,807 | −3.27% |
| ×1.00 | 0.50 | 33,623,424 | 32,152,961 | 1,470,463 | 7,834,420 | 16.85% |
| ×1.15 | 0.25 | 44,207,424 | 39,561,761 | 4,645,663 | 9,639,655 | 33.99% |

Expected family cash at year 2 = \$7,730,576. PV at 12% = **\$6,162,768**. The implied return on the \$6.0m land credit is 13.51% a year.

### B.4 The value of waiting and of uncertainty

The value of waiting is the wait PV less what the site would fetch today at its full residual value net of sale costs ($5{,}795{,}562 \times 0.97 = 5{,}621{,}695$):

| Volatility proxy $u$ | Wait PV | Entitle PV | Value of waiting |
|---:|---:|---:|---:|
| 1.10 | 4,564,200 | 5,262,072 | −1,057,495 |
| 1.20 | 7,024,032 | 8,278,809 | +1,402,337 |
| 1.30 | 9,242,077 | 10,984,650 | +3,620,382 |

At low uncertainty, waiting is worth *less* than selling today at full RLV, because a year of carry, 4% cost escalation, and the 5.5% forgone yield outweigh the option. At $u = 1.20$ and above, the option dominates. The decision hinges on the volatility estimate. That is the most important uncertainty in the case.

**A common shortcut and why it overstates.** A 50/50 real-world tree discounted at 10% gives a wait value of \$7,592,770, about \$0.57m higher than the risk-neutral value. It ignores the drift adjustment for the 5.5% yield the landholder does not collect. The direction of the error is not fixed. Here it flatters waiting.

### B.5 Recommendation (one defensible answer)

* **Do not sell at \$5.4m.** The bid is below the by-right RLV and well below the value of the family's options.
* **Do not build.** The family cannot finance it, and building now destroys the option (PV \$4.39m after the fee developer).
* **Entitle (PV \$8.28m), then decide in 12 months** among selling, a JV on the entitled site, or waiting further. Entitlement is worth pursuing at any approval probability above about 16%, so the decision is robust to the probability. The \$450,000 entitlement budget fits within the family's liquidity.
* **Re-approach the merchant builder with a counter-structure:** a purchase contract at a higher price contingent on PD approval, with the builder funding entitlement. This transfers the entitlement cost and keeps part of the upside.
* **Triggers.** Sell before the vote only if an unconditional bid for the by-right site exceeds about \$8.5m gross, because \$8,278,809 / 0.97 = \$8,534,854, the bid that matches the entitlement path after sale costs. Re-evaluate if rents fall more than 10% or hard costs rise more than 8% before the vote, or if the city signals denial.

**What would change the conclusion.** Evidence that volatility is low (u close to 1.10). A competing landowner nearby with an approved PD who could pre-empt demand (Grenadier, 1996). Faster cost escalation. A city signaling that the PD will fail. An improved JV structure that contributes the land *after* entitlement, which captures both the option and development profit without the family's capital.

---

## Mode C — Blind examination

Use only the Case facts section. Do not look at Modes A or B. Allow 90 minutes.

1. (5 pts) Explain in two sentences why the 2009 cost is irrelevant to the decision.
2. (15 pts) Compute the residual land value of both schemes today. Show GDV, each cost line, and the margin.
3. (10 pts) Compute the by-right RLV next year in the up and down states, with costs escalated. Explain what the result says about the leverage of land values.
4. (10 pts) Compute the risk-neutral probability. Explain why the 5.5% cap rate appears in it.
5. (15 pts) Value "wait one year, then sell" and "entitle and sell". Explain why the approval probability is not risk-neutralized.
6. (10 pts) Compute the break-even approval probability for entitlement.
7. (10 pts) Value the JV interest. Explain what option the family gives up by entering a build-now JV.
8. (10 pts) Show how the value of waiting changes with $u$ = 1.10, 1.20, 1.30, and interpret.
9. (10 pts) Write a one-page recommendation to the family, with triggers.
10. (5 pts) Name two facts that would most increase and two that would most decrease the value of waiting.

Answers: Mode B and `case_I_rubric.md`.

---

## Mode D — Investment committee

You present to the family's three partners and their outside advisor, a retired homebuilder. Each written answer must be under 150 words and supported by a number.

1. **"A bird in the hand."** The bid is \$5.4m cash today. Why should the family accept a model that says the land is worth \$7–8m, when no one has offered that?
2. **Where does the volatility come from?** Justify $u = 1.20$. What happens to the recommendation at $u = 1.10$?
3. **Is the entitlement probability credible?** What would you need to see from the city? What if it is 25%?
4. **What if the merchant builder walks?** Is there a next buyer at \$5.4m?
5. **What does waiting cost in cash?** List each cost and its size.
6. **Why not build?** Address the 15% margin the family would "leave on the table" by selling.
7. **Is the JV fair?** Who holds the option in the JV, and who is paid for it?
8. **What could make waiting a mistake?** Name the competitor or market scenario that hurts most.
9. **What is the family's liquidity plan?** Can it fund entitlement and carry if the vote slips six months?
10. **What is the trigger?** State the exact conditions under which you would sell, JV, or keep waiting.

Committee model answers are in `case_I_rubric.md` (§Mode D).
