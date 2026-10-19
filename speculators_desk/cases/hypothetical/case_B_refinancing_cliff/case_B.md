# Case B — The Refinancing Cliff

> **Evidence status:** Every property fact, operating figure, loan term, market parameter, probability, and counterparty in this case is [HYPOTHESIS], constructed for teaching. The property, sponsor, and lender are fictional. Cap rates, loan terms, leasing costs, foreclosure costs, and discount rates are assumptions chosen to be plausible for a U.S. suburban office asset after a period of sharply higher interest rates. They are not sourced market data. Replace them with current lender quotes, comparable sales, broker leasing assumptions, and legal advice before using any of them.
>
> **Model:** `case_b_model.py` (run it to regenerate every number). **Tests:** `tests/test_case_b.py`. **Rubric:** `case_B_rubric.md`.
>
> **Chapters used:** 1 (break-even, process versus outcome), 9 (valuation), 10 (sizing, refinancing gap, default option, waterfalls, incentives, distressed debt), 12 (distress and loan sales), 18 (options).

---

## Case facts (shared by all modes)

**The property.** Cedar Hollow Office Park: three two-story suburban office buildings, 185,000 rentable square feet (rsf), built in the early 2000s, with surface parking and no structured amenities. Tenants are regional professional-service firms and medical users on three- to seven-year leases.

**The acquisition (five years ago, $t=-5$).** The sponsor, Larchmont Partners, bought the park for \$46,000,000 (\$249/rsf) at a 6.50% going-in cap rate on NOI of \$2,990,000. Occupancy was 93%. Closing costs were 2%.

**The maturing loan.** \$30,000,000 from a life insurance company: five-year term, fixed 3.40%, interest-only, non-recourse. Annual interest \$1,020,000. Larchmont's managing principal signed a standard carve-out guarantee: loss recourse for misapplied rents, waste, and environmental liabilities; springing full recourse for voluntary bankruptcy, collusive involuntary bankruptcy, and unpermitted transfers or financing. Upon a maturity default, the lender may require that all property cash be deposited into a lender-controlled account.

**The equity.** \$16,920,000: 90% from a single institutional LP, 10% GP co-invest. Waterfall: 100% to investors until an 8% IRR, 80/20 until 12%, 70/30 thereafter (pooled equity flows, `cre.irr_hurdle_waterfall`). The GP charges an asset-management fee of 1.0% of contributed equity (\$169,200 a year), paid by the partnership while it owns the asset. Distributions to date ($t=-4$ to $t=0$): \$1.45m, \$1.40m, \$1.10m, \$0.70m, \$0.35m.

**Today ($t=0$): the loan matures.**

| Item | Value |
|---|---|
| Occupancy | 82% (93% at acquisition) |
| NOI after replacement reserves | \$2,350,000 |
| Normalized TI/leasing commissions deducted by lenders | \$2.00/rsf = \$370,000 |
| Underwritten net cash flow (NCF) | \$1,980,000 |
| Market cap rate on NOI (broker opinion, two recent trades) | 8.25% |
| Selling costs | 2.0% |

**New senior debt available (two lender quotes, consistent terms).** 6.75% fixed, 30-year amortization, 10-year term; maximum 60% LTV; minimum 1.35x DSCR on NCF; minimum 10.0% debt yield on NCF; costs 1.5% of the loan.

**What the existing lender has said.** The life company's asset manager will "consider" a three-year extension if Larchmont pays down \$3,000,000, pays a 0.5% fee on the extended balance, accepts a 5.75% interest-only rate, and agrees to a full cash sweep: all cash after interest goes to principal, and the sponsor funds any interest shortfall. It has also said it "does not do discounted payoffs" but has not refused one in writing. A note buyer has called Larchmont to ask whether the loan will be for sale.

**Three-year outlook (Larchmont's asset management team).** Annual NCF after all leasing capital, forward NOI at the end of year 3, and the exit cap rate in each state:

| State | Probability | NCF Y1 | NCF Y2 | NCF Y3 | NOI year 4 | Exit cap |
|---|---|---|---|---|---|---|
| Recovery | 0.30 | \$1,550,000 | \$1,850,000 | \$2,350,000 | \$2,900,000 | 7.50% |
| Base | 0.45 | \$1,700,000 | \$1,800,000 | \$1,950,000 | \$2,500,000 | 8.00% |
| Downside | 0.25 | \$1,450,000 | \$1,250,000 | \$1,100,000 | \$1,950,000 | 9.00% |

**Evaluation parameters.** New equity is valued at a 15% required return. The lender's opportunity rate is 6.75%. A lender that takes the property back (deed-in-lieu or foreclosure) incurs 7% of value in legal, carry, and sale costs and sells after one year. A deed-in-lieu costs the sponsor \$150,000 in legal fees; a DPO \$250,000. A note buyer requires 12%. A buyer of the real estate out of REO requires 10% unlevered.

---

## Mode A — Guided instruction

Try each step before reading the commentary.

### Step 1: Diagnose the cliff before solving it
Write down the old loan's coverage today, and the coverage the **same balance** would have on today's terms. The gap between the two numbers is the cliff. The loan was not unsafe while it lasted; it became unrefinanceable on the day it had to be replaced.

### Step 2: Size the new loan under all three tests
Value first (NOI ÷ cap). Then LTV, DSCR on NCF at the 30-year constant, and debt yield on NCF. Identify which binds. Ask: is this a rate problem or a value problem? The answer determines which levers (rate buy-down, IO, a lower-leverage lender) can help.

### Step 3: Attribute the gap
Walk from the old \$30.0 million loan to the new proceeds one change at a time: original value, the NOI decline at the original cap rate, the cap-rate expansion, and the tighter LTV. Most investment committees ask "how much of this is rates?" The attribution answers it.

### Step 4: List every strategy and both parties' payoffs
For each strategy — refinance with fresh equity, extension/modification, discounted payoff, deed-in-lieu, sale, short sale — compute the sponsor's expected NPV of new money and the lender's PV. A strategy happens only if both sides prefer it to their alternative. For a non-recourse borrower with negative equity, the alternative is the keys.

### Step 5: Value the equity as an option
Equity is worth $\max(V - B, 0)$ at the end of the extension. Today's intrinsic value is negative; time value is not. Compute both. Then ask whether the paydown and fee the lender demands are worth more or less than the option.

### Step 6: Compute private payoffs
The LP and the GP do not share the same payoff. The GP's promote may be dead; its fees are not. Compute the GP's private payoff from each strategy and compare it with the LP's.

### Step 7: Distressed value
What would a buyer pay for the real estate out of REO, and for the note today? These are the prices at which risk changes hands if Larchmont and the lender cannot agree.

---

## Mode B — Solved case

### B.1 The cliff

| Measure | Value |
|---|---|
| Value: \$2,350,000 / 8.25% | \$28,484,848 (\$154/rsf, against \$249/rsf paid) |
| LTV of the \$30.0m balance | 105.3% |
| Equity mark ($V - B$) | −\$1,515,152 |
| Old debt service (3.40% IO) | \$1,020,000; DSCR on NCF 1.94x; debt yield 6.60% |
| Same \$30.0m on new terms (6.75%, 30-yr; $K = 7.7832\%$) | DS \$2,334,953; DSCR 0.85x |

The loan was comfortably covered at 3.40%. The same balance on today's terms is covered 0.85 times.

### B.2 New loan sizing

| Constraint | Loan |
|---|---|
| LTV 60% × \$28,484,848 | **\$17,090,909** |
| DSCR: \$1,980,000 / 1.35 / 0.077832 | \$18,844,061 |
| Debt yield: \$1,980,000 / 10.0% | \$19,800,000 |

LTV binds. New debt service \$1,330,216 (DSCR 1.49x, debt yield 11.59%). Costs 1.5% = \$256,364. **Equity required to refinance = \$30,000,000 + \$256,364 − \$17,090,909 = \$13,165,455.** That is 78% of the equity originally invested, to keep an asset whose equity is marked at −\$1.5 million.

### B.3 Gap attribution

| Step | Proceeds at that step | Change |
|---|---|---|
| Original loan | \$30,000,000 | |
| 65% of original \$46.0m value | \$29,900,000 | −\$100,000 |
| NOI \$2.99m → \$2.35m at the original 6.50% cap | \$23,500,000 | −\$6,400,000 |
| Cap rate 6.50% → 8.25% | \$18,515,152 | −\$4,984,848 |
| LTV limit 65% → 60% | \$17,090,909 | −\$1,424,242 |

[INFERENCE] About half of the \$12.9 million shortfall comes from income (tenant departures in a weak office market), about 40% from the cap rate, and about 10% from tighter lending standards. Interest rates act mainly through the cap rate here, not through the DSCR test, which does not bind. A rate buy-down or IO would not fix this loan.

### B.4 Strategy payoffs

Strategy mechanics (all in `case_b_model.py`):

* **Refinance with fresh equity**: \$13,165,455 in at $t=0$; annual NCF less new debt service; at $t=3$ equity receives $\max(\text{net sale} - B_3, 0)$ with $B_3 = \$16{,}505{,}541$.
* **Extension**: \$3,000,000 paydown plus a \$135,000 fee in at $t=0$; balance \$27.0 million at 5.75% IO; all cash after interest sweeps to principal; the sponsor funds shortfalls; at $t=3$ equity receives net sale less balance if positive, otherwise the keys.
* **DPO**: the lender accepts \$24,000,000; the sponsor refinances with the new loan and funds \$7,415,455 (including \$250,000 legal and the new loan's costs); then as in the refinancing.
* **Deed-in-lieu (keys)**: the sponsor pays \$150,000 of legal costs and walks. No carve-out is triggered by a cooperative deed-in-lieu. The lender collects expected year-1 NCF (\$1,592,500) and sells at today's value less 7%.
* **Sale**: net proceeds \$27,915,152 do not repay \$30.0 million. Either the sponsor writes a \$2,084,848 check, or the lender consents to a **short sale** and takes \$27,915,152.

Sponsor equity NPV by state (15%):

| Strategy | Recovery (0.30) | Base (0.45) | Downside (0.25) | **Expected NPV** | New money |
|---|---|---|---|---|---|
| Refinance with fresh equity | \$2,152,039 | −\$2,797,387 | −\$10,164,719 | **−\$3,154,392** | \$13,165,455 |
| Extension | \$4,756,597 | −\$209,591 | −\$3,750,390 | **\$395,066** | \$3,135,000 |
| DPO at \$24.0m | \$7,902,039 | \$2,952,613 | −\$4,414,719 | **\$2,595,608** | \$7,415,455 |
| Deed-in-lieu | | | | **−\$150,000** | \$150,000 |
| Sale, sponsor pays shortfall | | | | **−\$2,084,848** | \$2,084,848 |
| Short sale (lender consents) | | | | \$0 | \$0 |

Lender PV (6.75%):

| Strategy | Lender PV |
|---|---|
| Refinance (paid at par) | \$30,000,000 |
| Sale with sponsor paying shortfall | \$30,000,000 |
| Extension | **\$28,018,240** (Recovery \$29,425,631; Base \$29,427,797; Downside \$23,792,168) |
| Short sale | \$27,915,152 |
| Deed-in-lieu | \$26,307,643 |
| DPO at \$24.0m | \$24,000,000 |

Extension cash flows by state:

| State | Sponsor flows ($t=0..3$) | Lender flows ($t=0..3$) | Balance at $t=3$ | Keys at $t=3$? |
|---|---|---|---|---|
| Recovery | −3,135,000; −2,500; 0; 12,005,440 | 3,135,000; 1,552,500; 1,850,000; 28,237,894 | \$25,887,894 | No |
| Base | −3,135,000; 0; 0; 4,449,181 | 3,135,000; 1,700,000; 1,800,000; 28,125,819 | \$26,175,819 | No |
| Downside | −3,135,000; −102,500; −302,500; −452,500 | 3,135,000; 1,552,500; 1,552,500; 21,702,500 | \$27,000,000 | Yes |

**Which strategies can actually happen?** The sponsor's walk-away payoff is −\$150,000 (keys). The lender's walk-away PV is \$26.31 million (deed-in-lieu).

* Refinancing with fresh equity and paying the shortfall on a sale are dominated for the sponsor: each is worse than the keys.
* The DPO at \$24.0 million is the sponsor's favorite and the lender's worst outcome. The sponsor would pay up to **\$26,595,608** in a DPO (where its NPV reaches zero). The lender needs at least **\$28,018,240** (its extension value). **No DPO price satisfies both.** The lender's statement that it "does not do discounted payoffs" is, on these numbers, consistent with its economics rather than a bargaining posture.
* The short sale beats the keys for both sides but is dominated by the extension for both (sponsor \$395,066 > \$0; lender \$28.02m > \$27.92m).
* **The extension is the only strategy that both parties prefer to every alternative available to them.**

### B.5 The equity as an option

Intrinsic value today: −\$1,515,152 (zero to a non-recourse holder). The option value at $t=0$ of the residual after the extension, $E[\max(\text{net sale}_3 - B_3, 0)]/1.15^3$, is **\$3,684,565**. The paydown and fee cost \$3,135,000, and expected interest shortfalls take the rest: the extension's expected NPV is \$395,066.

**The paydown range.** The sponsor's extension NPV reaches zero at a paydown of **\$4,042,682** (other terms fixed). The lender's extension PV exceeds its deed-in-lieu value at any paydown, including zero:

| Paydown | Lender extension PV |
|---|---|
| \$0 | \$27,335,392 |
| \$1,000,000 | \$27,562,877 |
| \$2,000,000 | \$27,790,558 |
| \$3,000,000 | \$28,018,240 |
| \$4,000,000 | \$28,246,210 |

The negotiable range for the paydown is therefore \$0 to about \$4.04 million. The lender's \$3.0 million ask sits inside it, closer to the sponsor's limit.

**Probability-weighted negotiation.** If Larchmont opens with a DPO request and the outcomes are extension 0.65, DPO 0.10, foreclosure/keys 0.25 [HYPOTHESIS], the sponsor's expected NPV is **\$478,854** and the lender's expected PV **\$27,188,767**. The DPO request costs the sponsor nothing if it does not provoke the lender into foreclosure. If the lender treats the request as bad faith and the foreclosure probability rises, the request becomes expensive.

### B.6 Sponsor incentives

**The promote is dead.** Using life-of-deal equity flows ($t=-5$ contribution, historical distributions, new money at $t=0$, outcomes to $t=3$), the promote is **\$0 in every state under every strategy**. The best life-of-deal IRR is 2.70% (DPO, Recovery). Handing back the keys today locks in a life-of-deal IRR of **−35.53%**.

`cre.irr_hurdle_waterfall` raises an error for the extension–Downside path, whose flows have no IRR (the last flow is negative and total distributions are below contributions). The model treats the promote as zero in that path, since no hurdle can be met when cumulative cash is below capital. This behavior is reported as a library issue.

**Private payoffs** (GP: 10% of NPV plus the PV of three years of AM fees, \$386,322 at 15%; LP: 90% of NPV):

| Strategy | LP | GP |
|---|---|---|
| Refinance with fresh equity | −\$2,838,953 | **+\$70,882** |
| Extension | \$355,559 | \$425,828 |
| DPO | \$2,336,047 | \$645,882 |

The fee stream makes a fresh-equity refinance look positive to the GP while it costs the LP \$2.84 million. A GP that recommends "protecting the asset" with a \$13.2 million capital call should be asked to show this table.

**Guarantees.** A voluntary bankruptcy to hold off the lender would spring full recourse on \$30.0 million against a deed-in-lieu recovery of \$26.3 million. The carve-out turns obstruction into a personal liability for the managing principal, which pushes the sponsor toward cooperation: an extension or a deed-in-lieu.

### B.7 Distressed values

* **Real estate out of REO.** Expected NCF \$1,592,500, \$1,677,500, \$1,857,500; expected net sale at $t=3$ \$30,457,583. Value at 10% unlevered: **\$27,112,891 (\$147/rsf)**, 4.8% below the broker's \$28.5 million. That is the price at which a distressed buyer would take the real estate if the lender forecloses.
* **The note.** At 12%, the note is worth \$24,878,341 if extended, \$22,677,868 if resolved by a \$24.0 million DPO in six months, and \$25,074,472 if the lender takes the keys. Weighted 0.45 / 0.20 / 0.35 [HYPOTHESIS]: **\$24,506,892, 81.7% of par.** The life company's own PV of its best strategy, at 6.75%, is \$28.0 million. A note sale near 82 would realize a \$5.5 million loss that holding avoids recognizing. The note buyer's call is unlikely to produce a trade [INFERENCE: Chapter 10, Example 10.10].

### B.8 Recommendation (one defensible answer)

* **Accept the extension in principle; negotiate the paydown down from \$3.0 million.** The lender's numbers support an extension at any paydown. Propose \$1.5–2.0 million in exchange for the full cash sweep, which the lender values because it reduces the balance in the good states.
* **Do not fund a \$13.2 million refinancing.** Expected NPV −\$3.15 million.
* **Do not pay the sale shortfall.** It is \$2.08 million to avoid a deed-in-lieu that costs \$0.15 million.
* **Ask for a DPO only in a way that does not jeopardize the extension.** The numbers say no DPO price works for both sides at the lender's 6.75% opportunity rate.
* **Fund the paydown only with LP consent after the LP sees the private-payoff table**, and price any new money from the LP as a priority (preferred) interest, not as common units at book value (Chapter 10, Example 10.9).
* **Set walk-away triggers now.** If Y1 NCF comes in below \$1.45 million (the Downside path) and the leasing pipeline has not converted, hand back the keys at the next interest shortfall rather than funding it. A rational sponsor does not fund three years of Downside shortfalls; the model's assumption that it does is conservative.

**What would change the conclusion.** A signed lease that moves occupancy above 88% (Recovery becomes more likely and refinancing becomes feasible sooner). A lower cap rate supported by new trades. A lender that needs liquidity (a DPO zone could then exist). A tax analysis showing that cancellation-of-debt income from a DPO or deed-in-lieu changes the LP's after-tax ranking [HYPOTHESIS: consult tax counsel; the case ignores taxes].

---

## Mode C — Blind examination

Use only the Case facts section. Do not look at Modes A or B. Allow 120 minutes. Calculators and spreadsheets are permitted.

1. (8 pts) Compute today's value, LTV of the maturing loan, the old loan's DSCR and debt yield on NCF, and the DSCR the same balance would have on the new loan terms.
2. (10 pts) Size the new loan on all three constraints. Identify the binding constraint and compute the equity required to refinance.
3. (10 pts) Attribute the reduction in loan proceeds to income, cap rate, and lending standards.
4. (20 pts) For the refinancing, extension, and DPO strategies, compute the sponsor's state-by-state and expected NPV at 15%. Compute the sponsor's result for the deed-in-lieu and the sale.
5. (12 pts) Compute the lender's PV for each strategy and identify which strategies both parties prefer to their walk-away alternatives.
6. (8 pts) Compute the option value of the equity under the extension. Explain why it exceeds the intrinsic value.
7. (8 pts) Find the paydown at which the sponsor is indifferent to the extension.
8. (8 pts) Show that the promote is worthless and compute the GP's and LP's private payoffs from each strategy.
9. (8 pts) Estimate the REO value of the real estate and the value of the note to a 12% buyer.
10. (8 pts) Write a five-sentence recommendation to the LP, with walk-away triggers.

Answers: Mode B, and `case_B_rubric.md`.

---

## Mode D — Investment committee

You are Larchmont's head of asset management presenting to a joint committee of Larchmont's partners and the LP's investment officer. Answer in writing, under 150 words each, with at least one number in each answer.

1. **Why not just refinance?** We still believe in the asset.
2. **How much of this is interest rates?** And would a rate buy-down fix it?
3. **Why should the LP put \$3 million into a property with negative equity?**
4. **What does the lender want, and what can we get?** What is the most we should pay down?
5. **Why not ask for a discounted payoff?**
6. **The GP earns fees if we keep the asset. How do we know this recommendation is not about fees?**
7. **What if the Downside happens?** When do we stop funding?
8. **What happens to the guarantor in each path?**
9. **If a note buyer buys the loan, does our plan change?**
10. **What would make you recommend handing back the keys today?**

The committee's rubric for these answers is in `case_B_rubric.md` (§Mode D).
