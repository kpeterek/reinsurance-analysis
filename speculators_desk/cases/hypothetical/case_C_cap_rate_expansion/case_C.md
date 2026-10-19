# Case C — Cap Rate Expansion and Equity Destruction

> **Evidence status:** Every property fact, operating figure, loan term, market parameter, and counterparty in this case is [HYPOTHESIS], constructed for teaching. The assignment fixes three facts: a \$20 million asset, 70% leverage, and a shock of −10% NOI with +150 bp of cap-rate expansion. The going-in cap rate (6.00%), the loan terms, the covenants, the refinancing market, and the forced-sale buyer's underwriting were chosen by the author and are hypothetical. They are plausible for a bank-financed multi-tenant medical office building but are not sourced market data.
>
> **Model:** `case_c_model.py` (run it to regenerate every number). **Tests:** `tests/test_case_c.py`. **Rubric:** `case_C_rubric.md`.
>
> **Chapters used:** 1 (leverage and ruin, break-even reasoning), 3 (forced selling), 9 (valuation, DCF, marginal buyer), 10 (loan sizing, covenants, refinancing gaps), 12 (distressed debt), 17 (recovery and loss given default).

---

## Case facts (shared by all modes)

**The property.** A 78,000 rentable sf, three-story, multi-tenant medical office building (MOB) on a suburban arterial road, two miles from a regional hospital campus. It was built in 2009. Tenants are physician groups, an imaging center, and an outpatient surgery suite. No tenant occupies more than 18% of the space.

**The acquisition (Year 0).** A regional sponsor bought the building for **\$20,000,000** (\$256.41/sf) at a **6.00% going-in cap rate** on forward NOI after reserves of \$1,200,000. Buyer closing costs were 1.5% of price.

**The loan (Year 0).**

| Term | Value |
|---|---|
| Lender | Regional bank, full recourse for carve-outs only (non-recourse otherwise) |
| Amount | \$14,000,000 (70% LTV) |
| Rate | 5.00% fixed, nominal annual, monthly payments |
| Structure | Interest-only for 24 months, then 30-year amortization |
| Term | 5 years (balloon at month 60) |
| LTV maintenance covenant | Loan ≤ 75% of value on a lender-ordered appraisal; breach requires a cure (paydown or cash collateral) within 60 days |
| DSCR financial covenant | NOI ÷ annual debt service on the payment then due ≥ 1.15x (event of default) |
| Cash-management trigger | DSCR < 1.25x **or** debt yield < 8.00%: all cash flow after debt service is swept to a lender-controlled account and applied to principal |

**The shock (end of Year 3, month 36).** Two health systems merged and consolidated outpatient services onto their own campus. Two tenants left at lease expiry and the replacements signed at lower rents with higher TI. In-place NOI fell **10%**. Over the same period, higher Treasury yields and reduced bank appetite for CRE pushed MOB cap rates up **150 bp**. The bank's annual appraisal at month 36 values the building on forward NOI at the new market cap rate.

**After the shock (assumptions for teaching).**

| Parameter | Value |
|---|---|
| NOI growth from the shocked level | 2.0% a year |
| Selling costs | 2.0% of price |
| Refinance market at maturity | 6.75% fixed, 30-year amortization; lesser of 60% LTV, 1.30x DSCR, 9.5% debt yield |
| Opportunistic buyer's underwriting | 11.0% unlevered target; NOI growth 2.5%; capital spending 8% of NOI; exit at 8.00% on Year 6 NOI; 5-year hold; 2% selling costs |
| Foreclosure | 15 months; legal, receiver, and leasing disruption 5% of sale price; lender discount rate 8.0% |
| Note sale bid | 80% of the loan balance |
| Rescue preferred equity | 13% accruing, compounding annually, senior to the sponsor's common equity |
| Sponsor's discount rate on its residual equity | 12% |

---

## Mode A — Guided instruction

Try each step before reading the commentary.

### Step 1: Separate the two shocks, then combine them

Value is NOI divided by the cap rate. The two shocks multiply:

$$\frac{V_1}{V_0} = (1 + \Delta NOI)\times\frac{c_0}{c_0 + \Delta c} = 0.90 \times \frac{6.00\%}{7.50\%} = 0.72.$$

Each shock alone looks survivable. Together they remove 28% of asset value. Notice that the cap-rate shock is twice as damaging as the NOI shock here. A 150 bp move on a 6.00% base is a 20% change in the multiple. A 150 bp move on a 9.00% base would be 14%. Low going-in cap rates are high-duration positions (Chapter 6).

### Step 2: Push the asset loss through the capital structure

Debt does not absorb losses until equity is gone. The equity loss is the asset loss divided by the equity share, adjusted for amortization paid since closing. Compute equity before and after, at the loan balance actually outstanding at month 36.

### Step 3: Test every covenant, not just the one in the headline

A bank loan typically has three kinds of tests: a **maintenance** test on value (LTV), a **financial** covenant on income (DSCR), and **cash-management triggers** (DSCR and debt yield) that stop distributions before a default. Each uses a different denominator. LTV depends on an appraisal, which depends on a cap rate the sponsor does not control. DSCR depends on the payment then due, so the step from IO to amortization at month 24 matters. Debt yield ignores the rate and the amortization altogether. That is why lenders like it.

### Step 4: Ask what it takes to recover

A 28% asset loss needs a 38.9% gain to recover. A 90% equity loss needs a ninefold gain. Translate those percentages into years of NOI growth and into the cap rate that would be needed. The arithmetic of recovery is the arithmetic of whether the sponsor has a reason to keep putting in money.

### Step 5: Lay out each party's options

* **Sponsor:** cure the LTV breach with new equity, raise rescue capital, negotiate a modification, sell, or hand back the keys.
* **Lender:** waive and extend, enforce the cure, sweep cash, sell the note, accept a discounted payoff or short sale, or foreclose.
* **Buyers:** who is the marginal buyer for a 2009 MOB with recent tenant losses, and what must they believe?

For each option, compute what it is worth to whoever chooses it. Parties choose by their own payoffs, not by what is efficient for the asset.

### Step 6: Price the forced sale

A forced sale clears at the marginal buyer's price, not at the appraisal. Build that buyer's DCF and compare it with the appraisal and with the loan balance.

---

## Mode B — Solved case

### B.1 Origination

| Item | Amount |
|---|---:|
| Price; forward NOI; cap | \$20,000,000; \$1,200,000; 6.00% |
| Loan (70%) | \$14,000,000 |
| Equity cash invested (price × 1.015 − loan) | \$6,300,000 |
| Debt service, IO period ($0.05 \times 14{,}000{,}000$) | \$700,000 |
| Debt service, amortizing (monthly, 30 years) | \$901,860 (loan constant 6.4419%) |
| DSCR: IO / amortizing | 1.71x / 1.33x |
| Debt yield | 8.57% |
| Cash-on-cash: IO / amortizing | 7.94% / 4.73% |

At origination the loan passes every test, but not by much once amortization begins: the amortizing DSCR of 1.33x is only 0.08x above the 1.25x sweep trigger, and the 8.57% debt yield is 57 bp above the 8.00% trigger.

### B.2 The shock and the equity

| Item | Before (month 36, at \$20.0m) | After |
|---|---:|---:|
| Forward NOI | 1,200,000 | 1,080,000 |
| Cap rate | 6.00% | 7.50% |
| Value | 20,000,000 | **14,400,000** (\$184.62/sf) |
| Loan balance (12 amortizing payments made) | 13,793,449 | 13,793,449 |
| Equity (value − balance) | 6,206,551 | **606,551** |

* Asset drawdown: **28.00%**.
* Equity drawdown: $1 - 606{,}551/6{,}206{,}551 =$ **90.23%**, a multiplier of 3.22x on the asset loss.
* Against the \$6,300,000 of cash invested, mark-to-market equity is down 90.37%.

**Attribution of the \$5,600,000 value loss.** NOI alone (at 6.00%): \$2,000,000. Cap rate alone (on \$1.2m NOI): \$4,000,000. Interaction: −\$400,000. The interaction is negative because the cap-rate shock applies to a smaller NOI.

**Leverage table (same asset shock, IO debt, no amortization).**

| Initial LTV | 0% | 50% | 60% | 70% | 75% |
|---|---:|---:|---:|---:|---:|
| Equity drawdown | 28.00% | 56.00% | 70.00% | 93.33% | 112.00% (wiped out) |
| LTV after shock | — | 69.44% | 83.33% | 97.22% | 104.17% |

The 70% row with amortization (90.23%) is slightly better than the IO row (93.33%) because the sponsor had already paid down \$206,551 of principal.

**Sensitivity grid: LTV after the shock / equity drawdown, at month 36.**

| NOI shock \\ cap shock | +50 bp | +100 bp | +150 bp | +200 bp |
|---|---|---|---|---|
| 0% | 74.7% / 24.8% | 80.5% / 46.0% | 86.2% / 64.4% | 92.0% / 80.6% |
| −5% | 78.6% / 39.7% | 84.7% / 59.8% | 90.7% / 77.3% | 96.8% / 92.6% |
| −10% | 83.0% / 54.5% | 89.4% / 73.7% | **95.8% / 90.2%** | 102.2% / 104.7% |
| −15% | 87.9% / 69.4% | 94.7% / 87.5% | 101.4% / 103.1% | 108.2% / 116.8% |

Only one cell (no NOI change, +50 bp) passes the 75% LTV covenant.

### B.3 Covenants and cash management

| Test | Threshold | Result | Status |
|---|---|---|---|
| LTV (balance ÷ appraised value) | ≤ 75% | 13,793,449 / 14,400,000 = **95.79%** | **Breach** — cure required |
| DSCR covenant (amortizing DS \$901,860) | ≥ 1.15x | 1,080,000 / 901,860 = **1.198x** | Pass, by 0.048x |
| Cash-management DSCR | ≥ 1.25x | 1.198x | **Triggered** |
| Cash-management debt yield | ≥ 8.00% | 1,080,000 / 13,793,449 = **7.83%** | **Triggered** |

Consequences:

* **LTV cure.** To return to 75% of \$14.4m (\$10.8m), the sponsor must pay down **\$2,993,449**, almost half the original equity, to protect a mark-to-market equity of \$606,551.
* **Debt-yield cure.** A paydown of \$293,449 would bring the debt yield back to 8.00%. The DSCR trigger cannot be cured by a paydown without re-amortization, because the payment is fixed. The sweep therefore stays on until NOI recovers to \$1,127,325 (+4.4%).
* **Cash sweep.** Cash flow after debt service of \$178,140 a year now goes to the lender, not to the sponsor. Distributions stop.
* **Distance to default.** The DSCR covenant fails at NOI below \$1,037,139, a further **3.97%** decline. One more tenant departure would put the loan into default on income as well as on value.
* **The LTV covenant was fragile from the start.** With the shocked NOI, the LTV test fails at any cap rate above **5.87%**, lower than the 6.00% going-in cap. NOI −10% alone, with no cap-rate change, gives a value of \$18.0m and an LTV of 76.6%.

### B.4 What it takes to recover

| Measure | Requirement |
|---|---|
| Asset gain to recover \$20.0m | $1/0.72 - 1 =$ **38.89%** |
| Equity gain to recover the pre-shock equity mark | $1/(1-0.9023) - 1 =$ **923%** (with the balance unchanged, value must return to \$20.0m) |
| NOI needed at a 7.50% cap for \$20.0m | \$1,500,000 |
| Years of 3% NOI growth to get there from \$1,080,000 | $\ln(1.5/1.08)/\ln(1.03) =$ **11.1 years** |
| Cap rate needed at today's NOI for \$20.0m | 1,080,000 / 20,000,000 = **5.40%**, below the 6.00% going-in cap |
| Years of 3% growth just to restore \$1.2m of NOI | 3.6 years |

The loan matures in two years. No plausible path restores the original equity before maturity.

### B.5 The maturity in two years

At month 60, with NOI growing 2% from the shocked level and the cap rate still at 7.50%:

| Item | Amount |
|---|---:|
| Forward NOI at maturity ($1{,}080{,}000 \times 1.02^2$) | 1,123,632 |
| Value at 7.50% | 14,981,760 |
| Loan balance at month 60 | 13,348,103 (LTV 89.10%) |
| New loan: 60% LTV / 1.30x DSCR at 6.75% / 9.5% DY | 8,989,056 / 11,105,135 / 11,827,705 |
| Maximum new loan (LTV binds) | **8,989,056** |
| Equity needed to refinance | **4,359,047** |

The refinancing gap at maturity (\$4.36m) is larger than the LTV cure now (\$2.99m). Curing now does not avoid the gap later; it pre-pays part of it.

### B.6 The forced sale: price and marginal buyer

**Who is the marginal buyer?** For a 2009 MOB with recent tenant losses and a bank loan in breach, three buyer types exist:

1. **Health systems and physician groups (user-buyers)** may pay above investor value for strategic space. The consolidating systems in this case are the reason the tenants left, so they are unlikely bidders.
2. **Healthcare REITs and core MOB funds** prefer newer, on-campus assets. Their bids depend on their own cost of capital. When listed REIT prices fall, as they did broadly in 2022 [FACT; Nareit, ch09-S05], their implied cost of equity rises and they become sellers, not buyers.
3. **Opportunistic funds** with dry powder and no financing contingency. They are the marginal buyer for a quick sale, and they price to a high unlevered return.

**The opportunistic buyer's DCF.** NOI from \$1,080,000 at 2.5% growth; cash flow after 8% capital spending; exit at 8.00% on Year 6 NOI; 2% selling costs; 11.0% discount rate.

| Year | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| NOI | 1,080,000 | 1,107,000 | 1,134,675 | 1,163,042 | 1,192,118 | 1,221,921 |
| Cash flow (92%) | 993,600 | 1,018,440 | 1,043,901 | 1,069,999 | 1,096,748 | — |

Gross reversion \$15,274,011; net \$14,968,531; PV of reversion \$8,883,094 (69.8% of value).

**Forced-sale price: \$12,723,818** (\$163.13/sf), an implied cap rate of **8.49%** on current NOI and **11.64% below** the \$14.4m appraisal.

| Item | Amount |
|---|---:|
| Net to seller after 2% costs | 12,469,341 |
| Loan balance | 13,793,449 |
| **Shortfall to lender** | **1,324,107** |
| Lender recovery | 90.40% of balance |

The appraisal says the equity is worth \$606,551. The clearing price says it is worth zero and the lender is impaired by \$1.32m. The difference is the gap between an appraiser's cap rate (7.50%) and the price of immediacy demanded by the only buyer able to close quickly (8.49%). Chapter 1's price of immediacy now runs against the sponsor.

### B.7 The lender's options

| Option | Recovery (PV) | % of balance | Comment |
|---|---:|---:|---|
| Consensual short sale now | 12,469,341 | **90.40%** | Fastest; requires sponsor cooperation |
| Foreclose, receiver, sell in 15 months | 11,875,913 | 86.10% | Interim cash flow \$1,242,000; sale net of 7% costs \$11,833,150; total \$13,075,150 discounted at 8% for 1.25 years |
| Sell the note at 80% | 11,034,759 | 80.00% | Removes the asset from the bank's books immediately |
| Waive, extend with sweep and partial paydown | Not computed | — | Depends on sponsor equity and the recovery path |

A rational lender prefers a cooperative short sale or a modification with new equity over foreclosure. That preference is the sponsor's bargaining power: the sponsor's cooperation is worth about \$593,000 to the lender (90.40% − 86.10% of the balance). A bank under regulatory or capital pressure may still sell the note at 80%, accepting a lower recovery for certainty and balance-sheet relief.

### B.8 The sponsor's options

Model: sale at maturity (end of Year 5) at one of three values, net of 2% costs. Swept cash flow is ignored (it reduces the loan, which favors the lender). Discount rate 12%.

| Scenario | p | Value at maturity | Net | Payoff if cured (balance \$10,040,518) | Payoff if lender waives (balance \$13,348,103) | Residual after rescue pref (\$3,822,335 due) |
|---|---:|---:|---:|---:|---:|---:|
| Recovery | 0.25 | 17,500,000 | 17,150,000 | 7,109,482 | 3,801,897 | 3,287,147 |
| Base | 0.50 | 15,000,000 | 14,700,000 | 4,659,482 | 1,351,897 | 837,147 |
| Further decline | 0.25 | 12,000,000 | 11,760,000 | 1,719,482 | 0 | 0 |
| **Expected** | | 14,875,000 | | 4,536,982 | 1,626,423 | 1,240,360 |
| **PV at 12%** | | | | **3,616,854** | **1,296,574** | **988,808** |

The cured balance at month 60 is the scheduled balance less the paydown compounded at the loan rate: $13{,}348{,}103 - 2{,}993{,}449 \times (1 + 0.05/12)^{24} = 10{,}040{,}518$.

Interpretation:

1. **Keys back (deed in lieu):** sponsor receives 0. It forfeits the \$606,551 mark and the option value of the equity.
2. **Cure with own money:** pay \$2,993,449 now for an expected PV of \$3,616,854. NPV **+\$623,406** relative to handing back the keys. The positive NPV comes almost entirely from the recovery scenario. It is a leveraged bet on the cap rate.
3. **Negotiate a waiver/modification without new money:** PV \$1,296,574. That is more than the cure's NPV, so a sponsor should try to negotiate before curing. The equity's option value (\$1.30m) is more than twice its mark (\$0.61m). Limited liability makes deeply underwater equity worth more than its book value.
4. **Rescue preferred equity at 13%:** sponsor PV \$988,808, with no new sponsor money. But the pref investor's expected payoff is \$3,296,622 on \$2,993,449, an expected annualized return of **4.94%**, far below 13%. Rescue capital priced at 13% coupon is not available on these scenarios; a rational provider would demand a higher coupon, a larger share of the upside, or control rights. The sponsor's apparent PV from the pref option is an illusion of the coupon.

### B.9 Recommendation (one defensible answer)

**For the sponsor:**

* Do **not** cure immediately. Open negotiations with the bank using the lender's own arithmetic: foreclosure recovers about 86% versus about 90% for a cooperative outcome.
* Propose a modification: a \$1.0–1.5m paydown (enough to restore the 8.0% debt yield with headroom), a two-year extension, continued cash sweep, and an LTV covenant waiver until maturity. Offer a springing guarantee of leasing costs as the sponsor's contribution.
* If the bank insists on the full LTV cure, the cure has a positive expected NPV on these scenarios but depends on the 25% recovery case. Test whether investors will fund it, and state that it is a bet on cap rates, not a rescue of the original investment.
* Hand back the keys if the bank demands the full cure *and* the sponsor's own probability of the recovery scenario is below about **10.5%**. That is the break-even at which the cure's NPV is zero, holding the base case at 50% and moving probability between the recovery and decline scenarios. The assumed 25% clears the break-even, but the cure's whole NPV rests on a scenario probability nobody can estimate precisely, which is why negotiating comes first.

**For the lender:** Prefer a modification with new money over a sale or foreclosure. Set the paydown so that the debt yield exceeds 8% and the loan is covered at a stressed value. Keep the sweep. Sell the note only if regulatory capital or concentration limits force the issue.

**For a buyer:** The clearing price for a quick sale is about \$12.7m. That is the price at which an opportunistic fund earns 11% under its assumptions. A buyer who can wait for the lender to take control and run a marketed sale may pay less in competition, or more if MOB cap rates recover. Approach the bank about the note at 80–85% of the balance as an alternative entry.

**What would change the conclusion.** A lease with a health system for the vacant space; evidence that MOB cap rates are compressing in recent trades; a bank under pressure to reduce CRE exposure (favoring a note sale); or a further tenant loss (which would trigger the DSCR covenant and remove the sponsor's negotiating leverage).

---

## Mode C — Blind examination

Use only the Case facts section. Do not look at Modes A or B. Allow 90 minutes. Calculators and spreadsheets are permitted.

1. (5 pts) Compute origination DSCR (IO and amortizing), debt yield, and cash-on-cash.
2. (10 pts) Compute the post-shock value, loan balance at month 36, equity before and after, and the asset and equity drawdowns.
3. (10 pts) Attribute the value loss to NOI, cap rate, and interaction. Explain why the cap-rate shock dominates.
4. (15 pts) Test every covenant and trigger. Compute the paydown that cures the LTV breach and the NOI decline that would breach the DSCR covenant.
5. (10 pts) Compute the gain required to recover the asset value and the equity, and the years of 3% NOI growth needed at a 7.50% cap.
6. (10 pts) Compute the refinancing gap at maturity.
7. (15 pts) Price the forced sale using the opportunistic buyer's underwriting. Identify the marginal buyer and explain why the clearing price differs from the appraisal.
8. (10 pts) Compute the lender's recovery under a short sale, foreclosure, and note sale.
9. (10 pts) Compute the sponsor's expected PV from curing, from a waiver, and from rescue preferred equity. Explain why the pref result is misleading.
10. (5 pts) Write a three-sentence recommendation to the sponsor.

Answers: Mode B, and `case_C_rubric.md`.

---

## Mode D — Investment committee

You are presenting to the sponsor's investment committee, whose members include the fund's CIO, its head of asset management, and an outside director who spent twenty years in bank special-assets workouts. Prepare written answers, each under 150 words and supported by a number.

1. **We underwrote 70% LTV with 1.33x coverage. Was that a mistake, or bad luck?** Separate the decision from the outcome.
2. **Why should we put \$3.0 million into an asset in which our equity is marked at \$0.6 million?**
3. **What does the bank actually want, and how do we know?**
4. **If we do nothing, what happens in the next 90 days?**
5. **What price would this building clear at in 60 days, and why is that not the appraisal?**
6. **What would make the recovery scenario more likely, and can we influence it?**
7. **If another tenant leaves, what changes?**
8. **How does this affect the other assets in the fund?** (Cross-collateralization, guarantees, reputation with the bank.)
9. **What should we have done at acquisition to survive this shock?** Quantify one structural change.
10. **What would make you recommend handing back the keys?**

The committee's rubric for these answers is in `case_C_rubric.md` (§Mode D).
