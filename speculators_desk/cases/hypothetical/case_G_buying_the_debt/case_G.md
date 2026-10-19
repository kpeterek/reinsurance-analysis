# Case G — Buying the Debt Instead of the Property

> **Evidence status:** Every loan term, property fact, probability, cost, and counterparty in this case is [HYPOTHESIS], constructed for teaching. Two legal rules are cited as facts and are documented in `references/sources_ch12.md`: the Texas foreclosure-sale timing rule (Tex. Prop. Code §51.002) and the single-asset-real-estate provision of the Bankruptcy Code (11 U.S.C. §362(d)(3)). Everything else — legal costs, timelines beyond the statutory minimums, cramdown terms, REO pricing — is an assumption. Before acting, replace them with advice from counsel in the relevant jurisdiction and with current market evidence.
>
> **Model:** `case_g_model.py`. **Tests:** `tests/test_case_g.py`. **Rubric:** `case_G_rubric.md`.
>
> **Chapters used:** 1 (expected value, IRR of expected flows), 10 (loan terms, default interest), 12 (NPL pricing, foreclosure economics, liquidity versus solvency), 17 (credit and recovery).

---

## Case facts (shared by all modes)

**The collateral.** A 312-unit garden apartment community in suburban Houston, built in 1984. Current NOI after reserves \$2.34 million; at a 6.50% cap the as-is value is \$36.0 million (\$115,385/unit). The property needs a \$4.0 million capital program (roofs, exterior, unit interiors on turnover). A competent owner who completes it over 24 months should reach a stabilized NOI of \$3.10 million, worth \$49.6 million at 6.25%, or \$48.608 million after 2% selling costs.

**The loan.** A \$48.0 million floating-rate bridge loan made in 2022 by a regional bank. Contract rate held at 7.75% for this case; default rate 5% higher. The interest-rate cap expired; the borrower stopped paying and then missed the maturity date. Unpaid contract interest is \$1.2 million. The loan is non-recourse with standard bad-boy carve-outs guaranteed by the sponsor. The sponsor has other troubled properties.

**The offer.** The bank will sell the note for **\$33.0 million (68.75% of UPB)**, as is, with limited representations. Your legal and diligence costs on the note purchase are \$150,000.

**The alternative.** Do not buy the note. Wait for the bank to foreclose (expected month 12), then bid in the bank's marketed REO sale. Your broker expects the REO to clear at about **\$37.5 million**, because other buyers will underwrite the same business plan. Buyer closing costs 1.5%. Your chance of winning a competitive REO process is estimated at 35%. By month 12 the property will have deteriorated, with NOI about \$2.20 million.

**Law (facts cited in Chapter 12).**
* Texas foreclosure sales under a deed of trust are public auctions held on the first Tuesday of a month between 10 a.m. and 4 p.m., after at least 21 days' notice of sale (Tex. Prop. Code §51.002). A borrower can delay with a lawsuit and temporary restraining order, or with a bankruptcy filing, which stays the sale.
* In a single-asset-real-estate bankruptcy, the debtor must, by a statutory deadline (generally the later of 90 days after the order for relief or 30 days after the court determines SARE status), either file a plan with a reasonable possibility of confirmation within a reasonable time or begin monthly payments to the secured creditor equal to interest at the nondefault contract rate on the value of the creditor's interest (11 U.S.C. §362(d)(3)). Failure gives the creditor grounds to seek relief from the stay; relief is not automatic.

**Resolution scenarios for the note** (your team's construction; probabilities are judgments):

| Scenario | $p$ | Resolution month | What happens | Legal and other costs |
|---|---:|---:|---|---:|
| Cure / refinance at par | 0.10 | 6 | Sponsor refinances; pays UPB + accrued interest + contract interest since purchase (default interest waived) | \$100,000 |
| Discounted payoff | 0.20 | 4 | Sponsor raises rescue capital; pays \$40.0 million | \$150,000 |
| Deed-in-lieu | 0.30 | 4 | You take title with releases; \$500,000 cash-for-keys; NOI at title \$2.34m | \$250,000 |
| Contested foreclosure | 0.25 | 10 | Sponsor sues and obtains a TRO; foreclosure at month 10; you pay taxes and insurance (\$75,000/month) for 8 months; NOI at title \$2.20m | \$600,000 |
| Bankruptcy, stay lifted | 0.10 | 20 | SARE case; you receive \$1.2m of §362(d)(3) payments over the case; stay lifted, foreclosure at month 20; NOI at title \$2.05m | \$1,500,000 |
| Bankruptcy, cramdown | 0.05 | 14 | Plan confirmed: your secured claim is written down to the \$36.0m collateral value and paid as a 5-year, 7.0% interest-only note | \$1,200,000 |

In every title scenario you then execute the business plan: 24 months, \$4.0 million capex spread evenly, NOI rising linearly to \$3.10 million, sale at \$48.608 million net. Required return on a distressed-debt position: 15%.

**Model conventions.** Monthly cash flows, month-end; monthly IRR annualized as $(1+IRR_m)^{12} - 1$. Unlevered. During default the borrower keeps the rents (no receiver), so the noteholder receives nothing from the property before title.

---

## Mode A — Guided instruction

### Step 1: What you are buying

A note is a claim, not a building. It pays through one of several doors: the borrower pays (cure or DPO), the borrower hands over the building (deed-in-lieu), the court process hands it over (foreclosure), or a bankruptcy court rewrites the claim (cramdown). Each door has a different amount, a different date, and different costs. Draw the tree before computing anything.

### Step 2: Why the note can be cheaper than the building

The note costs \$33.15 million all-in; the REO costs \$38.06 million. Both lead to the same collateral. The note is cheaper because its buyer bears time, legal, and borrower-behavior risk, and because the bank is a forced seller of a non-performing asset while the REO will be sold in a competitive process with clean title. Ask whether the \$4.9 million basis advantage is more than enough to pay for those risks.

### Step 3: Build each scenario's monthly cash flows

For title scenarios, the flows are: purchase price at month 0; protective advances while you wait; legal costs and cash-for-keys at title; then 24 months of NOI less capex; then the sale. For cash scenarios: purchase price, then one payoff.

### Step 4: Combine correctly

Compute per-scenario IRRs and multiples, then the IRR of expected flows and the expected NPV at 15%. Note the gap between the mean of scenario IRRs and the IRR of expected flows (Chapter 12, Example 12.3).

### Step 5: Compare with the REO path

Compute the REO IRR conditional on winning, and the expected profit including the 65% chance of losing the auction. Then stress both strategies for a lower stabilized value.

### Step 6: Decide what you would pay, and what you would not do

Solve for the maximum note price at 15%. Identify the scenario whose probability matters most and what diligence would narrow it.

---

## Mode B — Solved case

### B.1 Basis and value reference points

| Item | Amount | Per unit |
|---|---:|---:|
| UPB | \$48,000,000 | \$153,846 |
| As-is value (\$2.34m at 6.50%) | \$36,000,000 | \$115,385 |
| Note price | \$33,000,000 | \$105,769 |
| Note all-in (with \$150k costs) | \$33,150,000 | \$106,250 |
| REO price | \$37,500,000 | \$120,192 |
| REO all-in (1.5% closing) | \$38,062,500 | \$121,995 |
| Stabilized net sale | \$48,608,000 | \$155,795 |

The REO is expected to clear at 104.2% of today's as-is value: competing buyers are paying for the same upside you are.

### B.2 Business-plan flows after taking title

Monthly flow in month $k$ of ownership $= \text{NOI}_k/12 - 4{,}000{,}000/24$, with $\text{NOI}_k = \text{NOI}_{start} + (3{,}100{,}000 - \text{NOI}_{start})(k - 0.5)/24$; the month-24 flow adds \$48,608,000. Starting at \$2.34 million, the first month's flow is \$29,653 and the 24 months total \$50,048,000 including the sale.

### B.3 Note scenarios at \$33.0 million

| Scenario | $p$ | Months to final cash | IRR | Profit | Multiple | NPV at 15% |
|---|---:|---:|---:|---:|---:|---:|
| Cure / refinance at par | 0.10 | 6 | 136.32% | \$17,810,000 | 1.54x | \$14,370,445 |
| Discounted payoff | 0.20 | 4 | 73.71% | \$6,700,000 | 1.20x | \$4,886,077 |
| Deed-in-lieu | 0.30 | 28 | 18.45% | \$16,148,000 | 1.48x | \$2,378,624 |
| Contested foreclosure | 0.25 | 34 | 14.31% | \$15,558,000 | 1.45x | −\$568,540 |
| Bankruptcy, stay lifted | 0.10 | 44 | 11.62% | \$16,308,000 | 1.47x | −\$3,400,224 |
| Bankruptcy, cramdown | 0.05 | 74 | 6.60% | \$14,250,000 | 1.41x | −\$11,306,608 |

Cure payoff check: $48{,}000{,}000 + 1{,}200{,}000 + 48{,}000{,}000 \times 0.0775 \times 6/12 = \$51{,}060{,}000$, less \$100,000 legal; profit $= 50{,}960{,}000 - 33{,}150{,}000 = \$17{,}810{,}000$. ✓

**Summary.** Expected profit \$14,198,200; standard deviation \$3,820,622; probability of loss 0% in the base case. **IRR of expected flows 18.62%**; mean of scenario IRRs 38.98%. Expected NPV at 15%: **+\$2,080,359**. Probability that you end up owning the property: 0.65.

**Maximum note price at 15%:** \$35,080,359, **73.08% of UPB**. The \$33.0 million offer leaves about \$2.1 million of cushion.

**Observations.**
1. The profits are similar across scenarios (\$14–18 million except the DPO); the *returns* differ because of time. This note's risk is mostly a timing risk, not a principal risk, *provided the collateral values are right*.
2. The fast scenarios produce the eye-catching IRRs but the DPO makes the least money. A borrower who knows your basis may offer a DPO at \$40 million: accept only if the alternative paths are worth less in present value. Conditional on the loan *not* paying off, the four title and cramdown paths have a probability-weighted NPV at 15% of $(0.30 \times 2.379 + 0.25 \times (-0.569) + 0.10 \times (-3.400) + 0.05 \times (-11.307))/0.70 = -\$0.48$ million, against +\$4.89 million for the DPO at month 4. Take the \$40 million.
3. The cramdown is the scenario that hurts: a 7% note on \$36 million for five years, when you require 15%. Its probability is small, but its NPV is −\$11.3 million.

### B.4 The REO alternative

Conditional on winning at \$37.5 million: basis \$38,062,500; 24-month plan from NOI \$2.20 million; **IRR 14.67%**, profit \$11,845,500, multiple 1.31x. Including the 65% chance of losing the auction, the expected profit from pursuing the REO is $0.35 \times 11{,}845{,}500 = \$4{,}145{,}925$, and capital set aside for it earns only cash returns for 12 months.

### B.5 Stress: the stabilized value is lower than you think

| Stabilized NOI and value down by | Note IRR of expected flows | Note P(loss) | REO IRR (if won) |
|---|---:|---:|---:|
| 0% | 18.62% | 0% | 14.67% |
| 10% | 14.59% | 0% | 8.49% |
| 20% | 10.34% | 0% | 1.97% |
| 30% | 5.85% | 0% | −4.96% |

The note's lower basis is a margin of safety: a 30% error in stabilized value leaves the note profitable in every scenario, while the REO loses money. The REO is hurt more because its buyer pays for the same collateral at a \$4.9 million higher basis and starts from a weaker NOI; the note's fast cash scenarios (30% of probability) do not depend on the stabilized value at all.

### B.6 What the credit bid means

After ten months of default, the noteholder's claim (UPB, accrued and default interest, protective advances, legal) is about **\$55.5 million**. At a foreclosure sale you may credit-bid up to that amount without paying cash. A third party must outbid it in cash; on collateral worth \$36 million no one will. That is why the auction is not where the property trades, and why the note holder, not the auction, controls who ends up owning the building.

### B.7 Recommendation (one defensible answer)

* **Buy the note at \$33.0 million, or bid \$32.0–33.0 million**, subject to: (i) a title and lien review (mechanic's liens on a property with deferred maintenance can prime or complicate); (ii) a review of the loan file for lender-liability exposure (the sponsor's lawyers will look for it); (iii) the guaranty and the sponsor's balance sheet, which drive the cure, DPO, and deed-in-lieu probabilities; (iv) an independent valuation and property inspection.
* **Walk away if:** the bankruptcy probabilities together exceed about 30%, or the inspection shows capex above \$6 million, or the title review shows senior liens.
* **Do not plan on the REO path** as the primary strategy: a 35% chance of a 14.7% IRR on a higher basis is inferior in this setup.
* **What you are paid for:** bearing legal-process and timing risk, and supplying liquidity to a bank that wants a non-performing loan off its balance sheet.

**What would change the conclusion.** A receiver appointed quickly (which would capture rents for you during the default); a sponsor with a strong guarantor (which raises cure and DPO probabilities); evidence that the as-is value is lower than \$36 million; or a judicial-state location (Chapter 12, Example 12.4), which would lengthen every title scenario.

---

## Mode C — Blind examination

Use only the Case facts. Allow 120 minutes.

1. (10 pts) Compute the cure payoff and the all-in note and REO bases. Express each per unit.
2. (15 pts) Build the monthly cash-flow vector for the deed-in-lieu scenario. Give the first month of ownership and the total.
3. (20 pts) Compute IRR, profit, multiple, and NPV at 15% for all six scenarios.
4. (10 pts) Compute the IRR of expected flows and the mean of scenario IRRs. Explain the gap.
5. (10 pts) Compute the maximum note price at 15%.
6. (10 pts) Compute the REO IRR if won and the expected profit including the chance of losing.
7. (10 pts) Stress both strategies for a 20% lower stabilized value.
8. (5 pts) Should you accept a \$40 million DPO offered at month 4? Justify with present values.
9. (10 pts) State a bid, conditions, and walk-away triggers.

Answers: Mode B and `case_G_rubric.md`.

---

## Mode D — Investment committee

Each answer under 150 words, supported by a number.

1. **Why buy paper when we want to own apartments?**
2. **Your expected IRR is 18.6%. The deal sheet says 39%. Which is right?**
3. **What if the borrower files for bankruptcy the day after we close?**
4. **What does the cramdown scenario cost us, and how could it get worse?**
5. **How confident are you in \$36 million as-is and \$48.6 million stabilized?** What if both are 20% lower?
6. **What legal risks come with the note that would not come with the REO?**
7. **The borrower offers \$40 million in month 4. Do we take it?**
8. **Why not wait and buy the REO?**
9. **What would make you walk away during diligence?**
10. **How does this change if the property were in a judicial-foreclosure state?**

The committee rubric is in `case_G_rubric.md`.
