# Chapter 9 — CRE Valuation and Mispricing

> **Status:** Complete (v1.0). All fourteen worked examples, the historical-episode arithmetic, the problems, and the solutions are reproduced in `tests/test_ch09_examples.py`. Problems are in `problems/questions/ch09_problems.md` and solutions in `problems/solutions/ch09_solutions.md`. Sources are listed in `references/sources_ch09.md`; two historical figures are marked *(verification pending)* in §9.9.

## Learning objectives

After this chapter you should be able to:

1. Value an income property by direct capitalization, discounted cash flow, sales comparison, and replacement cost. For each method, say which question it answers and when it fails.
2. Build a DCF with explicit timing: annual cash flows after capital costs, reversion on **forward** NOI at the exit cap, selling costs, and the share of value that sits in the reversion.
3. Choose the right NOI (trailing, in-place, or stabilized) and deduct the cost of reaching stabilization. Capitalize correctly when property tax is reassessed at the price paid (the loaded cap rate).
4. Derive the going-in cap rate from $k$, $g$, and the capital-expenditure burden. Use it backwards to state **what the marginal buyer must believe** at a given price. Explain why exit cap rates normally exceed going-in cap rates.
5. Separate property-level IRR from equity IRR. Show when leverage adds return and when it only adds variance.
6. Build two-way sensitivity grids and find break-even exit caps.
7. Decompose an IRR into income, market NOI growth, value-add NOI growth, and cap-rate change. Label the parts that are business plan and the parts that are speculation.
8. Recognize owners anchored to historical cost, replacement cost, or a prior appraisal. Quantify the gap and judge whether a transaction can occur.
9. Explain appraisal smoothing and the divergence between appraisal-based and listed-market prices, using 2008–09 and 2022–24 as evidence.

---

## 9.1 Opening investment problem: the office building with three anchors

All facts in this section are [HYPOTHESIS], a constructed teaching case.

A family office asks you to evaluate a 165,000 sf multi-tenant suburban office building. The listing broker sends a two-page summary.

| Item | Broker's figure |
|---|---|
| Asking price | \$48.6 million |
| Trailing-12 NOI (after a \$0.25/sf reserve) | \$3,400,000 |
| Implied cap rate | 7.00% |
| 2021 appraisal (for the owner's lender) | \$52.0 million |
| Owner's acquisition price (2017) | \$47.5 million |
| Replacement cost | "\$400/sf, i.e., \$66 million" |
| Occupancy | 91% |

The broker's pitch is that the asking price is "below the appraisal, roughly at the owner's basis, and 26% below replacement cost."

Your leasing team adds what the summary leaves out. Tenant A occupies 49,500 sf, 30% of the building. Its lease expires in twelve months, and it has told several brokers it will consolidate into a smaller space downtown. Your team's lease-by-lease model projects twelve months of downtime, a new lease with tenant improvements of about \$55/sf, leasing commissions, and free rent. It also projects lower NOI than the trailing figure for three years. Your committee requires a 9.0% unlevered return on suburban office.

Three questions frame the chapter:

1. What is the building worth to a buyer who requires 9.0%?
2. At \$48.6 million, what must a buyer believe about growth, exit cap, or return?
3. Which of the broker's three anchors (appraisal, basis, replacement cost) is evidence of value, and which is only evidence of what the seller wants?

Section 9.10 returns to the bid.

---

## 9.2 Economic intuition: a price is a forecast that someone has agreed to

An income property is a claim on future net cash flow. Every valuation method estimates the present value of that claim. The methods differ in which observable quantity they lean on.

* **Direct capitalization** leans on market cap rates. One year of NOI is multiplied by a market multiple ($1/c$). All the forecasting is hidden inside $c$. The method works when the subject's cash flow profile resembles the profile of the assets whose sales set $c$.
* **Discounted cash flow** leans on your own forecast and your own required return. The forecast is explicit, so it can be wrong in visible ways. The method is necessary when the cash flow profile is irregular: lease rollover, lease-up, renovation, or a ground lease.
* **Sales comparison** leans on other people's recent decisions. It is the most direct market evidence when comparable trades are recent and numerous. It is weakest exactly when markets move fast, because comparable sales are then stale, few, and selected.
* **Replacement cost** leans on construction economics. It bounds value from above over the long run: if value exceeds cost plus a developer's margin, someone builds, and new supply pushes rents and values down. It does not bound value from below. Nobody is obliged to build, and a building that cannot earn a return on its cost is worth what its income supports.

A price agreed between a buyer and a seller is therefore a forecast that both parties have accepted. A sophisticated reader of a price asks what forecast it embeds. If the price implies NOI growth of 3% a year forever for a building with a 30% tenant leaving next year, the forecast is implausible, and either the buyer knows something you do not or the price will not hold.

### Mispricing in private real estate

Private real estate prices are set in thin, slow, negotiated markets. Three features create persistent mispricing.

1. **No continuous price.** An asset trades every five to fifteen years. Between trades its "value" is an appraisal, which is an opinion built from past transactions. Appraisals smooth and lag (§9.9).
2. **Anchoring.** Owners anchor to their cost, to replacement cost, and to their last appraisal. These numbers are salient and personally meaningful, but they are not forecasts of cash flow. Kahneman and Tversky's work on anchoring and reference-dependent preferences predicts this behavior. In CRE it shows up as bid–ask gaps that close slowly and as low transaction volume after price declines.
3. **Heterogeneous information and constraints.** The buyer's NOI is not the seller's NOI. Each side has a different tax position, financing, and holding horizon. The marginal buyer, the one whose bid clears the market, sets the price. Their beliefs and constraints are what you must infer.

A mispricing is useful to a speculator only if it is **identifiable** (you can say what is wrong with the price), **actionable** (you can transact at it), and **likely to correct within your horizon** (something will force recognition). Anchored owners often fail the third test: the gap persists because they refuse to sell, not because the market eventually agrees with them.

---

## 9.3 Technical definitions

| Term | Definition |
|---|---|
| NOI | Revenue less operating expenses, **after** replacement reserves unless stated. Before debt service, income tax, depreciation, and leasing capital (TI/LC) unless stated |
| Cash flow after capex (CF) | NOI less tenant improvements, leasing commissions, and capital projects not funded by the reserve |
| Trailing NOI (T-12) | NOI over the last twelve months |
| In-place NOI | Current run-rate NOI from leases in place, annualized |
| Stabilized NOI | NOI at market occupancy, market rents, and normal expenses, once lease-up or renovation is complete |
| Forward NOI ($NOI_1$) | Expected NOI over the next twelve months. Brokers quote cap rates on forward NOI more often than on T-12; always ask which |
| Going-in cap rate $c_0$ | $NOI_1 / P$ |
| Terminal (exit) cap rate $c_T$ | The cap rate applied at sale to $NOI_{T+1}$ |
| Reversion | Sale proceeds at the end of the hold: gross $= NOI_{T+1}/c_T$; net = gross × (1 − selling costs) |
| Loaded cap rate | $c + t$, where $t$ is property tax as a fraction of price after reassessment |
| Discount rate $k$ | Required unlevered total return |
| Capex ratio $\kappa$ | Long-run average capital spending (TI/LC and building capital) as a fraction of NOI |
| Residual land value | GDV less all non-land costs less the developer's required profit |
| Replacement cost | Cost to build a functionally equivalent property today, including land at market. Depreciated replacement cost subtracts physical, functional, and external obsolescence |
| Property (unlevered) IRR | IRR of the property's cash flows, including purchase costs and net reversion |
| Equity (levered) IRR | IRR of equity flows after debt service and loan repayment |
| Marginal buyer | The bidder whose price clears the market; the one with the highest willingness to pay among those able to close |
| Anchor | A reference number (cost, prior appraisal, peak price) that shapes a reservation price but does not measure value |

---

## 9.4 Equations and derivations

### 9.4.1 Direct capitalization

$$V = \frac{NOI_1}{c}.$$

The cap rate is a price multiple, not a return. It equals the expected return only if NOI is flat forever and no capital is spent.

### 9.4.2 Discounted cash flow with explicit timing

For a hold of $T$ years with year-end cash flows:

$$V_0 = \sum_{t=1}^{T} \frac{NOI_t - CapEx_t}{(1+k)^t} + \frac{(1-s)\,NOI_{T+1}/c_T}{(1+k)^T}.$$

Here $s$ is the selling-cost fraction. Three timing rules are binding in this book:

1. The reversion capitalizes $NOI_{T+1}$, the buyer's forward income. Capitalizing $NOI_T$ applies a forward-NOI cap rate to trailing income and understates value by about a year of growth.
2. Capital spending is a cash outflow in the year it occurs, even if it raises NOI later. A DCF that adds the NOI uplift without the capex overstates value.
3. If the buyer at exit will face a large known capital need (a roof, a rollover), the exit cap or the reversion must reflect it.

The **reversion share** is $PV(\text{reversion})/V_0$. For a five-year hold it is usually 60–80% of value [HYPOTHESIS: typical of the examples in this chapter and Case C (70–78%); not a measured market statistic]. Most of a five-year DCF's value is therefore a forecast of someone else's cap rate five years from now.

### 9.4.3 The cap rate as $k - g$, adjusted for capital spending

Suppose NOI grows at $g$ forever, and a constant fraction $\kappa$ of NOI is spent on capital. Free cash flow is $(1-\kappa)NOI_t$. The growing-perpetuity value is

$$V = \frac{(1-\kappa)\,NOI_1}{k - g} \quad\Rightarrow\quad c = \frac{NOI_1}{V} = \frac{k - g}{1-\kappa}.$$

Rearranged, the price tells you what a buyer must believe:

$$g_{\text{implied}} = k - c(1-\kappa), \qquad k_{\text{implied}} = c(1-\kappa) + g.$$

With $\kappa = 0$ this is the familiar $c = k - g$ (`sdesk.cre.gordon_cap_rate`). Ignoring $\kappa$ overstates the growth or return a buyer is getting. The bias is largest for office, where TI/LC can consume 15–25% of NOI over a cycle [HYPOTHESIS: teaching range; verify against your own lease-by-lease history].

### 9.4.4 Why the exit cap usually exceeds the going-in cap

Apply 9.4.3 at two dates. At acquisition the building has growth $g_0$ and capex burden $\kappa_0$. At exit it is older: its growth is usually lower and its capex burden higher. Holding $k$ fixed,

$$c_T - c_0 = \frac{k - g_T}{1-\kappa_T} - \frac{k - g_0}{1-\kappa_0} > 0 \quad \text{when } g_T < g_0 \text{ or } \kappa_T > \kappa_0.$$

The **going-in/exit spread** is therefore not conservatism for its own sake. It is the cap-rate consequence of aging. Its typical size in underwriting practice is 25–75 bp for a five- to ten-year hold [HYPOTHESIS: practitioner convention, not a measured market statistic]. A further component reflects uncertainty about the rate environment at exit. That component is a forecast, and it should be labeled as one.

### 9.4.5 The IRR identity: when IRR equals $c + g$

If NOI grows at constant $g$, no capital is spent, there are no transaction costs, and the exit cap equals the going-in cap, then the property IRR equals $c_0 + g$ exactly, for any hold period.

*Proof.* At $k = c_0 + g$, the price $NOI_1/c_0$ equals the Gordon value $NOI_1/(k-g)$. The reversion $NOI_{T+1}/c_0$ equals the Gordon value at $T$. Discounting a Gordon value at $k$ reproduces the Gordon value at 0, so NPV = 0 at $k = c_0 + g$. ∎

This identity is the backbone of the IRR decomposition in Example 9.10. Deviations from it come from cap-rate change, NOI growth different from $g$, capital spending, and transaction costs.

### 9.4.6 Loaded cap rate

If property tax after the sale is $tP$, then $V = (N - tV)/c$, so

$$V = \frac{N}{c + t},$$

where $N$ is NOI before property tax (`sdesk.cre.loaded_cap_value`). Case A derived this for a Texas hotel. It applies to any property in a jurisdiction that reassesses to sale price.

### 9.4.7 Residual land value

With gross development value $GDV$, selling cost $s$, non-land costs $H + S + F$ (hard, soft, financing), and required margin on total cost $m$:

$$N = GDV(1-s), \quad N = (L + H + S + F)(1+m) \;\Rightarrow\; L = \frac{N}{1+m} - (H + S + F).$$

Land is the residual claimant on development, so it is a levered position on GDV: a 1% change in GDV moves land value by $N/(1+m)/L$ percent, often 10–20 times as much (`sdesk.cre.residual_land_value`).

### 9.4.8 Leverage and the equity IRR

For one period, with LTV $\lambda$ and debt cost $r_D$:

$$r_E = r_A + \frac{\lambda}{1-\lambda}(r_A - r_D).$$

On a multi-year hold, use the full equity cash-flow vector: equity in, NOI less capex less debt service each year, net reversion less loan balance at exit. Compare the **cash** yield with the loan constant $K$ and the **total** return with the interest rate. Leverage can be negative on cash yield (cap rate below $K$) and still positive on IRR, if appreciation is large enough. That configuration means the levered investor depends on appreciation.

### 9.4.9 Appraisal smoothing

A simple model of an appraised value $A_t$ is a weighted average of the prior appraisal and current true value $V_t$:

$$A_t = \alpha A_{t-1} + (1-\alpha) V_t, \qquad 0 \le \alpha < 1.$$

Inverting it gives the unsmoothing filter used in the appraisal literature (Geltner, 1993):

$$V_t = \frac{A_t - \alpha A_{t-1}}{1-\alpha}.$$

With $\alpha = 0.6$, a sudden 25% fall in true value appears in appraisals as a 10% fall in the first period and is only about 85% recognized after three periods (Example 9.14).

---

## 9.5 Worked examples

All inputs are [HYPOTHESIS] unless cited. All examples are reproduced in `tests/test_ch09_examples.py`. NOI is after replacement reserves unless stated. Cash flows are annual and at year-end.

### Example 9.1 — Three NOIs, three values: trailing, in-place, stabilized (multifamily)

**Given.** A 240-unit garden apartment community has just finished renovating 120 units. The market cap rate for stabilized assets of this quality is 5.50% on forward stabilized NOI after a \$300/unit reserve.

| NOI measure | Amount | What it reflects |
|---|---:|---|
| Trailing-12 | \$2,610,000 | Months with 20–30 units offline for renovation |
| In-place (last 3 months × 4) | \$2,880,000 | Renovation complete; concessions of one month free still on 60 new leases; 91% occupancy |
| Underwritten stabilized (Year 1 forward, after 9 months of lease-up) | \$3,060,000 | 95% occupancy; renovated-unit premiums; concessions burned off |

The cost to reach stabilization is the NOI shortfall during lease-up (\$310,000) plus marketing and turn costs (\$75,000), a total of \$385,000.

**Find.** The value implied by each NOI, and the as-is value.

**Solution.**

$V = NOI/c$ at $c = 0.055$:

| NOI basis | NOI | Value |
|---|---:|---:|
| Trailing | 2,610,000 | 47,454,545 |
| In-place | 2,880,000 | 52,363,636 |
| Stabilized | 3,060,000 | 55,636,364 |

As-is value = stabilized value − cost to stabilize $= 55{,}636{,}364 - 385{,}000 = \$55{,}251{,}364$.

The deduction is undiscounted. Discounting \$385,000 over nine months at 7% would change it by about \$19,000 and does not affect the decision.

**Check.** \$3,060,000 / \$55,636,364 = 5.50%. The spread between trailing and stabilized value is \$8.18 million. It is 14.7% of the stabilized value and is explained entirely by the choice of NOI.

**Decision consequence.** A seller will quote the stabilized figure. A buyer anchored to the trailing figure will lose every competitive bid. The correct bid starts from stabilized value and deducts the cost and the **risk** of reaching it. The \$385,000 deduction covers the cost. It does not cover the risk that the renovated-unit premium fails to hold. If the premium is the business plan you are buying, you are paying the seller for a forecast you will have to execute. Ask for 90 days of signed renovated leases before you pay for stabilized NOI. A 5.50% cap applied to trailing NOI is a convention mismatch: market cap rates are quoted on forward stabilized NOI, so the trailing value is not a "conservative" value. It is a wrong one.

Reproduce: `tests/test_ch09_examples.py::test_example_9_1`.

### Example 9.2 — Reassessment: the loaded cap rate on the same apartments

**Given.** Example 9.1's property is in a jurisdiction that reassesses to market value after a sale. The trailing tax bill is \$520,000: assessed value \$26.0 million × 2.00%. After a sale the assessor will set assessed value at 90% of the price. Stabilized NOI before property tax is therefore $3{,}060{,}000 + 520{,}000 = \$3{,}580{,}000$. The market cap rate (on NOI after reassessed tax) is 5.50%.

**Find.** Value with reassessment, the new tax bill, and the error from capitalizing the seller's tax bill.

**Solution.**

Effective tax on price: $t = 2.00\% \times 0.90 = 1.80\%$.

Loaded cap rate: $c + t = 5.50\% + 1.80\% = 7.30\%$.

$$V = \frac{3{,}580{,}000}{0.073} = \$49{,}041{,}096.$$

New tax bill $= 0.018 \times 49{,}041{,}096 = \$882{,}740$. NOI after reassessed tax $= 3{,}580{,}000 - 882{,}740 = \$2{,}697{,}260$.

Error from capitalizing NOI that carries the seller's \$520,000 tax bill: $55{,}636{,}364 - 49{,}041{,}096 = \$6{,}595{,}268$. That is 13.4% of the correct value.

**Check.** \$2,697,260 / \$49,041,096 = 5.50%. ✓

**Decision consequence.** In a reassessment jurisdiction, the seller's T-12 tax line is a liability that resets at your price. A buyer who capitalizes it pays the seller for a tax bill the buyer will never enjoy. The effect is large because the old assessment (\$26.0 million) is far below the price. The gap between assessed value and market value is widest after a period of rising prices, which is when bidding is most competitive. Underwrite tax on the price you will pay. The loaded cap rate makes the circularity disappear.

Reproduce: `tests/test_ch09_examples.py::test_example_9_2`.

### Example 9.3 — Office DCF with rollover, TI/LC, and forward NOI at exit

**Given.** The §9.1 office building. Your team's lease-by-lease projection (annual, year-end):

| Year | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| NOI | 3,400,000 | 2,300,000 | 2,850,000 | 3,300,000 | 3,400,000 | 3,500,000 |
| TI, LC, building capital | 250,000 | 3,550,000 | 450,000 | 300,000 | 350,000 | — |
| Cash flow after capex | 3,150,000 | −1,250,000 | 2,400,000 | 3,000,000 | 3,050,000 | — |

Year 1 still includes Tenant A's rent. Year 2 has twelve months of downtime on 49,500 sf, plus \$2.72 million of TI (\$55/sf) and leasing commissions. Year 3 carries free rent on the new lease. Exit at the end of Year 5 at an 8.25% cap on Year 6 NOI, with 2.0% selling costs. Discount rate 9.0%.

**Find.** Value, reversion share, implied going-in cap, the IRR at the asking price, and the exit cap needed to justify the ask.

**Solution.**

Reversion: gross $= 3{,}500{,}000 / 0.0825 = \$42{,}424{,}242$. Net $= 42{,}424{,}242 \times 0.98 = \$41{,}575{,}758$.

Present values at 9.0%:

| Year | Cash flow | Discount factor | PV |
|---|---:|---:|---:|
| 1 | 3,150,000 | 0.917431 | 2,889,908 |
| 2 | −1,250,000 | 0.841680 | −1,052,100 |
| 3 | 2,400,000 | 0.772183 | 1,853,240 |
| 4 | 3,000,000 | 0.708425 | 2,125,276 |
| 5 | 3,050,000 | 0.649931 | 1,982,291 |
| 5 | Net reversion 41,575,758 | 0.649931 | 27,021,390 |
| | **Value** | | **34,820,005** |

PV of operating cash flows = \$7,798,615. Reversion share $= 27{,}021{,}390 / 34{,}820{,}005 = 77.6\%$.

Implied going-in cap on Year 1 NOI $= 3{,}400{,}000 / 34{,}820{,}005 = 9.76\%$. Value per sf = \$211.

At the asking price of \$48,571,429 (= \$3,400,000 / 0.07), the same cash flows produce an IRR of **1.44%**. To earn 9.0% at the ask, a buyer would need an exit cap of **5.47%** on Year 6 NOI.

**The timing trap.** If you capitalize Year 5 NOI (\$3,400,000) instead of Year 6 NOI at exit, value falls to \$34,047,965, an understatement of \$772,040. The error is small here because Year 6 NOI grows only 2.9% over Year 5. It becomes large when the exit year contains a known NOI step: for example, a lease burning off free rent in Year 6.

**Check.** Rebuild by hand: $2{,}889{,}908 - 1{,}052{,}100 + 1{,}853{,}240 + 2{,}125{,}276 + 1{,}982{,}291 + 27{,}021{,}390 = 34{,}820{,}005$. ✓ `sdesk.cre.dcf_value(cf, 3_500_000, 0.0825, 0.09, 0.02)` returns the same.

**Decision consequence.** The broker's 7.0% cap applies a stabilized multiple to a year of income that will not recur until Year 5. The DCF shows that the building is worth about \$34.8 million to a 9% buyer, 28% below the ask. More than three-quarters of that value sits in a Year-5 sale. The bid therefore depends far more on your exit-cap view and on re-leasing Tenant A's space than on Year 1 NOI. The highest-value diligence is a leasing study of the 49,500 sf block: achievable rent, downtime, and TI package. A refined discount rate is worth much less. A 5.47% exit cap on a suburban office building sold five years from now is not a forecast any committee would sign, so the ask is not a price at which this building trades to an informed buyer.

Reproduce: `tests/test_ch09_examples.py::test_example_9_3`.

### Example 9.4 — What must the marginal buyer believe? Implied growth across property types

**Given.** Three assets, each quoted at a market cap rate. Your required unlevered returns and long-run capex burdens:

| Asset | Cap rate $c$ | Required return $k$ | Capex ratio $\kappa$ |
|---|---:|---:|---:|
| Suburban office (the §9.1 ask) | 7.00% | 9.00% | 15% |
| Bulk industrial | 5.25% | 7.50% | 5% |
| Garden multifamily | 5.50% | 7.25% | 8% |

**Find.** The perpetual NOI growth each price implies. For the office, also find the return a buyer earns if long-run NOI growth is only 1%.

**Solution.** $g_{\text{implied}} = k - c(1-\kappa)$:

| Asset | $c(1-\kappa)$ | $g_{\text{implied}}$ |
|---|---:|---:|
| Office | $0.07 \times 0.85 = 5.95\%$ | $9.00\% - 5.95\% = 3.05\%$ |
| Industrial | $0.0525 \times 0.95 = 4.99\%$ | $7.50\% - 4.99\% = 2.51\%$ |
| Multifamily | $0.055 \times 0.92 = 5.06\%$ | $7.25\% - 5.06\% = 2.19\%$ |

Office at 1% growth: $k_{\text{implied}} = c(1-\kappa) + g = 5.95\% + 1.00\% = 6.95\%$. The cap rate consistent with 9.0% and 1% growth is $(0.09 - 0.01)/0.85 = 9.41\%$.

**Check.** `gordon_cap_rate(0.09, 0.0305) / 0.85` returns 0.0700. ✓

**Decision consequence.** The office ask requires a buyer to believe in 3% perpetual NOI growth on a building with structural vacancy risk, or to accept a 6.95% unlevered return. Both are statements you can test. Ask yourself whether 3% nominal NOI growth forever is plausible for suburban office, given the capex it takes to keep tenants. Then ask whether 6.95% is adequate compensation for an illiquid, high-capex asset. The industrial and multifamily prices imply growth near long-run inflation expectations. Those prices are not obviously wrong; they are bets that inflation-level rent growth persists. This "reverse" use of $k - g$ is the fastest way to locate an aggressive price. It does not tell you the right price. It tells you which belief to argue about.

Reproduce: `tests/test_ch09_examples.py::test_example_9_4`.

### Example 9.5 — Deriving the going-in/exit cap spread from aging

**Given.** $k = 8.0\%$ for a five-year-old industrial building. Today: long-run NOI growth 2.5%, capex burden 10%. In ten years the building will be fifteen years old: growth 2.0% (lower functional competitiveness), capex burden 15% (roof, paving, HVAC).

**Find.** The going-in cap, the exit cap in Year 10, and the spread.

**Solution.**

$$c_0 = \frac{0.08 - 0.025}{1 - 0.10} = \frac{0.055}{0.90} = 6.11\%, \qquad c_{10} = \frac{0.08 - 0.020}{1 - 0.15} = \frac{0.060}{0.85} = 7.06\%.$$

Spread $= 7.06\% - 6.11\% = 95$ bp, with no change in rates or risk premia.

**Decision consequence.** A DCF that sets the exit cap equal to the going-in cap assumes the building does not age. That is a hidden forecast of either cap-rate compression or a capital program that restores the building's competitiveness. If your model contains that capital program, a flat exit cap may be defensible. Otherwise the 95 bp is not "cushion"; it is the structural cost of time. Any exit-cap view beyond aging (rates, risk appetite) is a macro forecast. State it separately, so the committee can see how much of the IRR rests on it.

Reproduce: `tests/test_ch09_examples.py::test_example_9_5`.

### Example 9.6 — Sales comparison with a stale comp, a distressed comp, and reliability weights

**Given.** Subject: a 120,000 sf bulk industrial building, built 2008, 32-foot clear height, vacant at sale (owner-user or speculative buyer). Four sales within the submarket. Adjustments are multiplicative, in the order shown. The time adjustment uses your submarket price index, which has fallen since the older sales.

| Comp | Price/sf | Months ago | Time | Location | Physical (age, clear height) | Conditions of sale | Lease (occupancy, credit) |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | \$142 | 4 | −2% | 0% | +5% | 0% | 0% |
| B | \$165 | 20 | −14% | −5% | −5% | 0% | 0% |
| C | \$128 | 2 | −1% | +5% | +10% | +8% (forced seller) | 0% |
| D | \$150 | 9 | −6% | 0% | 0% | 0% | −7% (10-yr credit lease) |

Weight each comp by the inverse of its **gross** (absolute) adjustment, a common rule that favors comps needing fewer judgments.

**Find.** Adjusted prices, weights, and the indicated value.

**Solution.**

| Comp | Adjustment factor | Adjusted \$/sf | Gross adjustment | Weight |
|---|---:|---:|---:|---:|
| A | 0.98 × 1.05 = 1.0290 | 146.12 | 7% | 47.1% |
| B | 0.86 × 0.95 × 0.95 = 0.7761 | 128.06 | 24% | 13.7% |
| C | 0.99 × 1.05 × 1.10 × 1.08 = 1.2349 | 158.07 | 24% | 13.7% |
| D | 0.94 × 0.93 = 0.8742 | 131.13 | 13% | 25.4% |

Weighted indicated value = \$141.48/sf. Value = $141.48 \times 120{,}000 = \$16{,}977{,}094$. The simple average of adjusted prices is \$140.85/sf.

**The stale-comp error.** Comp B, unadjusted for time but adjusted for location and physical differences, indicates $165 \times 0.95 \times 0.95 = \$148.91$/sf. That is 16% above its time-adjusted figure. An appraiser who weights B heavily because "it is the best physical match" imports a pre-decline price into a post-decline valuation.

**Selection bias.** The four comps are the sales that closed. In the same period, suppose five listings were withdrawn because no bid met the seller's reservation price. Sales that close are the ones where some buyer valued the asset above the seller's reservation price. In a falling market, owners with no need to sell withdraw, so the closed sales are disproportionately (a) assets with buyers who value them unusually highly, and (b) forced sales like C. The two biases point in opposite directions. Neither is visible in the comp grid. Ask the broker for withdrawn listings and their best bids. That evidence is often more informative than a fifth closed sale.

**Decision consequence.** The indicated value of about \$17.0 million is a range, not a point: the adjusted comps span \$128–\$158/sf, or \$15.4–\$19.0 million. The width of that range comes from adjustments that are opinions (location, physical, conditions of sale). A bid at the indicated value is defensible only if your income approach agrees within a few percent. If it does not, the disagreement tells you which approach to investigate. Two weak comps that disagree are evidence of a moving market, not of a precise value.

Reproduce: `tests/test_ch09_examples.py::test_example_9_6`.

### Example 9.7 — Replacement cost and residual land value: when does new supply arrive?

**Given.** A developer is considering a 200,000 sf speculative industrial building. Stabilized NOI \$1,600,000 (\$8.00/sf net). Hard costs \$90/sf = \$18,000,000. Soft costs 18% of hard = \$3,240,000. Financing costs \$1,300,000. Selling costs 1.5% of GDV. Required developer margin on total cost: 15%. The land seller asks \$2,500,000. Market exit cap: 5.75%, with sensitivity at 5.25% and 6.25%.

**Find.** Residual land value at each cap rate; the developer's margin if the land is bought at the asking price; replacement cost per sf.

**Solution.**

At 5.75%: $GDV = 1{,}600{,}000/0.0575 = \$27{,}826{,}087$. Net value $N = 27{,}826{,}087 \times 0.985 = \$27{,}408{,}696$. Non-land cost $= 18{,}000{,}000 + 3{,}240{,}000 + 1{,}300{,}000 = \$22{,}540{,}000$.

$$L = \frac{27{,}408{,}696}{1.15} - 22{,}540{,}000 = 23{,}833{,}648 - 22{,}540{,}000 = \$1{,}293{,}648.$$

| Exit cap | GDV | Net value | Residual land |
|---|---:|---:|---:|
| 5.25% | 30,476,190 | 30,019,048 | 3,563,520 |
| 5.75% | 27,826,087 | 27,408,696 | 1,293,648 |
| 6.25% | 25,600,000 | 25,216,000 | −613,043 |

At the \$2.5 million asking price for land, total cost is $22{,}540{,}000 + 2{,}500{,}000 = \$25{,}040{,}000$ (\$125.20/sf). This is replacement cost before developer's profit. The margin on cost is $27{,}408{,}696 / 25{,}040{,}000 - 1 = 9.46\%$, below the 15% requirement. Yield on cost $= 1{,}600{,}000/25{,}040{,}000 = 6.39\%$.

**Check.** At 5.75%, value/replacement cost $= 27{,}826{,}087/25{,}040{,}000 = 1.11$. A ratio below about $1.15/(1-s) = 1.17$ means development does not clear the required margin. ✓

**Decision consequence.** Two conclusions follow. First, the land is a levered call on cap rates: a 100 bp move in the exit cap (5.25% to 6.25%) moves GDV by \$4.88 million, 17.5% of the base-case GDV, and residual land value from +\$3.56 million to −\$0.61 million. Land sellers anchored to 2021-style land comps will not see that arithmetic, and land transactions will stall before building transactions do. Second, for owners of **existing** industrial buildings, the infeasibility of new construction at 5.75% is good news: new supply will not arrive until NOI (at a constant cap rate) rises about 5.1%: the developer needs net value of $1.15 \times 25{,}040{,}000 = \$28{,}796{,}000$ against \$27,408,696 today. Replacement cost sets a ceiling on how far values can rise before supply responds. It does not support a floor, which Example 9.13 shows.

Reproduce: `tests/test_ch09_examples.py::test_example_9_7`.

### Example 9.8 — Property IRR versus equity IRR: positive leverage that is mostly variance

**Given.** Purchase of a stabilized industrial building for \$25,000,000 plus 1.0% buyer costs. Year 1 NOI \$1,400,000 (5.60% going-in), growing 3% a year. Capital spending 5% of NOI each year. Sale at the end of Year 5 at a 6.00% cap on Year 6 NOI, less 1.5% selling costs. Loan: 60% of price (\$15,000,000), 6.25% fixed, 30-year amortization, monthly payments, balloon at the end of Year 5.

**Find.** Property IRR, equity IRR, first-year cash-on-cash, DSCR and debt yield; the equity IRR at a 5.00% rate.

**Solution.**

NOI: 1,400,000; 1,442,000; 1,485,260; 1,529,818; 1,575,712; Year 6 1,622,984.
Cash flow after capex (×0.95): 1,330,000; 1,369,900; 1,410,997; 1,453,327; 1,496,927.
Gross reversion $= 1{,}622{,}984/0.06 = \$27{,}049{,}728$. Net $= \$26{,}643{,}982$.

Property flows: $[-25{,}250{,}000;\ 1{,}330{,}000;\ 1{,}369{,}900;\ 1{,}410{,}997;\ 1{,}453{,}327;\ 28{,}140{,}909]$.
**Property IRR = 6.54%**. Equity multiple 1.33x.

Debt: monthly payment on \$15,000,000 at 6.25%/12 over 360 months gives annual debt service \$1,108,291 (loan constant 7.39%). Balance after 60 payments \$14,000,586. DSCR Year 1 $= 1{,}400{,}000/1{,}108{,}291 = 1.26$x. Debt yield $= 1{,}400{,}000/15{,}000{,}000 = 9.33\%$.

Equity flows: $[-10{,}250{,}000;\ 221{,}709;\ 261{,}609;\ 302{,}706;\ 345{,}036;\ 13{,}032{,}032]$.
Year 5 equity flow $= 1{,}496{,}927 - 1{,}108{,}291 + 26{,}643{,}982 - 14{,}000{,}586$.
**Equity IRR = 6.97%**. Equity multiple 1.38x. First-year cash-on-cash $= 221{,}709/10{,}250{,}000 = 2.16\%$.

At a 5.00% loan rate (constant 6.44%), equity IRR = 8.59%.

**Decision consequence.** Leverage raised the IRR by 43 bp, from 6.54% to 6.97%, because the property IRR barely exceeds the 6.25% loan rate. It cut first-year cash yield from 5.27% (1,330,000/25,250,000) to 2.16%, because the 5.60% cap is below the 7.39% loan constant. The equity is therefore a bet that NOI growth and the exit cap deliver the reversion. Example 9.9 shows that the same 60% LTV that adds 43 bp in the base case multiplies the dispersion of outcomes. When the property IRR sits within about 50 bp of the debt cost, leverage is mostly a variance amplifier. A sponsor who presents only the 6.97% is presenting the mean of a wider distribution as if it were an improvement.

Reproduce: `tests/test_ch09_examples.py::test_example_9_8`.

### Example 9.9 — Two-way sensitivity grids and the break-even exit cap

**Given.** Example 9.8 with NOI growth $g \in \{1\%, 2\%, 3\%, 4\%\}$ and exit cap $\in \{5.50\%, 5.75\%, 6.00\%, 6.25\%, 6.50\%\}$. All other inputs unchanged.

**Find.** Property and equity IRR grids, and the exit cap at which the property IRR equals 7.0% with 3% growth.

**Solution.** Property IRR (%):

| $g$ \\ exit cap | 5.50% | 5.75% | 6.00% | 6.25% | 6.50% |
|---|---:|---:|---:|---:|---:|
| 1% | 6.14 | 5.34 | 4.58 | 3.86 | 3.18 |
| 2% | 7.14 | 6.33 | 5.56 | 4.83 | 4.14 |
| 3% | 8.14 | 7.32 | **6.54** | 5.81 | 5.11 |
| 4% | 9.14 | 8.31 | 7.52 | 6.78 | 6.07 |

Equity IRR at 60% LTV, 6.25% (%):

| $g$ \\ exit cap | 5.50% | 5.75% | 6.00% | 6.25% | 6.50% |
|---|---:|---:|---:|---:|---:|
| 1% | 6.04 | 4.13 | 2.24 | 0.37 | −1.50 |
| 2% | 8.32 | 6.48 | 4.67 | 2.88 | 1.11 |
| 3% | 10.50 | 8.72 | **6.97** | 5.26 | 3.56 |
| 4% | 12.60 | 10.87 | 9.18 | 7.52 | 5.89 |

Break-even exit cap for a 7.0% property IRR at 3% growth: **5.85%**. That is 15 bp below the 6.00% base-case exit cap, which is itself the 5.60% going-in cap plus a 40 bp aging spread.

**Decision consequence.** Read the grids diagonally. Moving one cell toward the lower right (growth −1 point, exit cap +25 bp) costs about 170 bp of property IRR and about 400 bp of equity IRR. Leverage more than doubles the sensitivity. The property grid's range is 3.18%–9.14%; the equity grid's is −1.50%–12.60%. A committee that targets 7.0% unlevered should notice that the target requires an exit cap of 5.85% or lower at 3% growth. That is a cap-rate forecast, not a business plan. The grids do not assign probabilities. They tell you which two variables matter and how much, so you can decide which to research and which to hedge. A grid with an axis that does not move the answer is a wasted grid.

Reproduce: `tests/test_ch09_examples.py::test_example_9_9`.

### Example 9.10 — Decomposing IRR: income, market growth, value-add, and cap compression

**Given.** A value-add apartment purchase at \$40,000,000 (no transaction costs, to keep the decomposition clean). Year 1 NOI \$2,000,000 (5.00% going-in). Market NOI growth 3%. A \$3,000,000 unit-renovation program in Year 1 adds \$450,000 of NOI from Year 2, growing at 3% thereafter. Sale at the end of Year 5 at a 4.75% cap on Year 6 NOI.

**Find.** The IRR, decomposed into income, market NOI growth, value-add, and cap-rate change.

**Solution.** Build the IRR up one assumption at a time.

| Step | Added assumption | Year 6 NOI | Gross reversion | IRR | Increment |
|---|---|---:|---:|---:|---:|
| (a) | Flat NOI, exit at 5.00% | 2,000,000 | 40,000,000 | 5.00% | 5.00% income |
| (b) | + market growth 3% | 2,318,548 | 46,370,963 | 8.00% | +3.00% market growth |
| (c) | + renovation (−\$3.0m Y1; +\$450k NOI from Y2) | 2,825,027 | 56,500,542 | 10.96% | +2.96% value-add |
| (d) | + exit at 4.75% | 2,825,027 | 59,474,255 | 11.97% | +1.00% cap compression |

Step (a) and step (b) confirm the identity of §9.4.5: with no capex and exit cap = going-in cap, IRR = $c_0 + g$ exactly.

The renovation earns a 15% yield on cost ($450{,}000/3{,}000{,}000$). At a 5.00% cap it creates \$6.0 million of value for \$3.0 million of capital.

**Order dependence.** Adding the cap-rate change before the renovation gives a cap-rate increment of 0.97% instead of 1.00% (growth plus cap compression alone gives 8.97%). The attribution depends on order because IRR is nonlinear. State the order you used.

**Decision consequence.** Of the 11.97% IRR, 5.00 points are income you can underwrite from leases, and 2.96 points are a business plan you control: renovation scope, cost, and rent premium. The remaining 4.00 points are market growth and cap compression, which you do not control. They are **speculative appreciation**. A sponsor who calls the whole 11.97% "value-add" is selling market beta as skill. Committees should ask two questions. First, what is the IRR with zero market growth and a 25–50 bp *higher* exit cap? That is the return on the business plan alone. Second, is the fee and promote structure paying the sponsor for the 4.00 points it does not control?

Reproduce: `tests/test_ch09_examples.py::test_example_9_10`.

### Example 9.11 — Anchoring case I: the apartment owner and the 2021 basis

**Given.** An owner bought a 300-unit apartment community in 2021 for \$62,000,000, at a 3.90% cap on NOI of \$2,418,000. The loan is \$40,300,000, floating, now at 6.50% interest-only. NOI has grown: forward NOI is \$2,650,000. The market cap rate for comparable assets is now 5.60%. A buyer offers market value. The owner says: "I'm not selling below my \$62 million basis."

**Find.** Market value; the owner's loss versus basis; the owner's equity; the NOI growth or cap rate needed to get back to \$62 million in five years; and the forward-looking return on holding, at market value.

**Solution.**

Market value $= 2{,}650{,}000/0.056 = \$47{,}321{,}429$, a 23.7% decline from basis (\$14,678,571).

Equity: invested $62{,}000{,}000 - 40{,}300{,}000 = \$21{,}700{,}000$. Equity at market $= 47{,}321{,}429 - 40{,}300{,}000 = \$7{,}021{,}429$. Net cash from a sale today after 2% selling costs: $47{,}321{,}429 \times 0.98 - 40{,}300{,}000 = \$6{,}075{,}000$.

To reach a \$62 million gross price at the end of Year 5 at a 5.60% cap, Year 6 NOI must be $62{,}000{,}000 \times 0.056 = \$3{,}472{,}000$. From \$2,650,000 in Year 1, that requires growth of $(3{,}472{,}000/2{,}650{,}000)^{1/5} - 1 = 5.55\%$ a year for five years.

Alternatively, at 3% growth (Year 6 NOI \$3,072,076), the exit cap must fall to $3{,}072{,}076/62{,}000{,}000 = 4.95\%$.

Forward-looking unlevered return on holding, at market value, 3% growth, exit at 5.60%, ignoring costs: by §9.4.5, **8.60%** (= 5.60% + 3.00%).

Levered: treat the \$6,075,000 of net sale proceeds as the equity the owner reinvests by not selling. Annual interest $= 0.065 \times 40{,}300{,}000 = \$2{,}619{,}500$. Equity flows $[-6{,}075{,}000;\ 30{,}500;\ 110{,}000;\ 191{,}885;\ 276{,}227;\ 13{,}824{,}434]$, where Year 5 includes a sale at 5.60% on Year 6 NOI less 2% and repayment of \$40.3 million. Levered IRR **19.29%**.

**Decision consequence.** The basis enters none of the forward-looking numbers. The owner's real choice is between \$6.08 million of cash today and a levered position whose expected return is about 19% if NOI grows 3% and cap rates hold, with the property at 85% loan-to-value and near-zero cash flow after interest. That can be a reasonable bet. But it should be made on that arithmetic, not on the \$62 million. The anchor matters only through three channels: (1) tax, since realizing a loss has value and the timing of recapture matters; (2) the loan, which matures at a balance that market value barely covers; and (3) reporting, because a sale crystallizes a loss that an appraisal can defer. For a buyer, the anchor predicts behavior. This owner will not sell voluntarily until either the loan forces the issue or the owner's lenders or investors stop accepting the appraisal. Price your patience accordingly; Case B treats the refinancing cliff.

Reproduce: `tests/test_ch09_examples.py::test_example_9_11`.

### Example 9.12 — Anchoring case II: the office owner and the 2021 appraisal

**Given.** The §9.1 office building. The 2021 appraisal capitalized T-12 NOI of \$3,510,000 at 6.75%: \$52,000,000. Current T-12 NOI is \$3,400,000. Assume today's market cap rate for a **stabilized** multi-tenant suburban office building with no near-term rollover is 8.00% [HYPOTHESIS]. Your DCF value is \$34,820,005 (Example 9.3).

**Find.** Decompose the decline from the appraisal to your value.

**Solution.**

| Step | Value | Change |
|---|---:|---:|
| 2021 appraisal: \$3,510,000 / 6.75% | 52,000,000 | |
| Current T-12 NOI at the 2021 cap: \$3,400,000 / 6.75% | 50,370,370 | −1,629,630 (NOI) |
| Current T-12 NOI at today's stabilized cap: \$3,400,000 / 8.00% | 42,500,000 | −7,870,370 (cap rate) |
| DCF with Tenant A rollover, TI/LC, downtime | 34,820,005 | −7,679,995 (rollover and capital) |
| **Total** | | **−17,179,995 (−33.0%)** |

**Decision consequence.** Less than 10% of the decline comes from NOI the owner can see on the T-12. The rest comes from two things the appraisal did not show. One is the market's repricing of office risk. The other is that a 30% tenant's lease, which had years left in 2021, now expires in twelve months. Lease term decays with time even if nothing else changes: the same building is a different asset with one year of term left than with five. The appraisal was an opinion at a date. It used a method (direct cap on T-12) that cannot see rollover. The owner who quotes it is quoting a stale answer to a question that has since changed. Show the owner this table. The NOI line is undeniable, the cap-rate line is visible in comparable sales, and the rollover line is the subject of a leasing study the owner can verify. Each line is evidence, not opinion. That is the only route to closing a 33% bid–ask gap without waiting for a maturity to close it for you.

Reproduce: `tests/test_ch09_examples.py::test_example_9_12`.

### Example 9.13 — Anchoring case III: the retail owner and replacement cost

**Given.** A 95,000 sf grocery-anchored neighborhood center built in 1998. NOI \$1,710,000 (\$18.00/sf). Market cap rate 7.75%. The owner cites a contractor's estimate of replacement cost at \$310/sf, including land: \$29,450,000. "Nobody can build this for less, so it's worth at least that." A developer would require a 15% margin on cost.

**Find.** Market value; implied total depreciation from replacement cost; the NOI and rent that new construction would require.

**Solution.**

Market value $= 1{,}710{,}000/0.0775 = \$22{,}064{,}516$ (\$232.26/sf).

Implied total depreciation (physical, functional, external) $= 1 - 22{,}064{,}516/29{,}450{,}000 = 25.1\%$.

For a developer to build: value must reach $29{,}450{,}000 \times 1.15 = \$33{,}867{,}500$. At 7.75% that requires NOI of \$2,624,731, or \$27.63/sf, which is **53.5% above** the subject's \$18.00/sf.

**Decision consequence.** Replacement cost tells you that new competing centers will not be built until rents rise by about half. That protects the subject's income from new supply, which is worth something and belongs in the growth and exit assumptions. It does not make the building worth \$29.45 million. A 28-year-old center with a 1998 layout, parking ratio, and tenant mix carries functional and external obsolescence that a new building does not. The market measures that obsolescence at about 25%. An owner who will not sell below replacement cost has, in effect, decided not to sell. A buyer should spend no time on the argument and instead look for the event that will change the owner's position: the anchor's renewal, a loan maturity, or an estate.

Reproduce: `tests/test_ch09_examples.py::test_example_9_13`.

### Example 9.14 — Appraisal smoothing and unsmoothing

**Given.** True market value of a portfolio is 100 at $t=0$ and falls to 75 at $t=1$, then stays there. Appraisals follow $A_t = 0.6A_{t-1} + 0.4V_t$ with $A_0 = 100$.

**Find.** The appraisal path for four periods, and the value recovered by unsmoothing.

**Solution.**

| $t$ | True $V_t$ | Appraisal $A_t$ | Appraisal change | Unsmoothed $(A_t - 0.6A_{t-1})/0.4$ |
|---|---:|---:|---:|---:|
| 0 | 100 | 100.00 | | |
| 1 | 75 | 90.00 | −10.0% | 75.00 |
| 2 | 75 | 84.00 | −6.7% | 75.00 |
| 3 | 75 | 80.40 | −4.3% | 75.00 |
| 4 | 75 | 78.24 | −2.7% | 75.00 |

After three periods the appraisal has recognized $(100 - 80.40)/25 = 78.4\%$ of the decline; after four, 87.0%.

**Decision consequence.** An appraisal-based index that falls 10% while a listed-market index falls 25% is consistent with both measuring the same 25% decline, if appraisals smooth with $\alpha = 0.6$. The smoothing parameter is not known in real time and varies across cycles. The arithmetic therefore does not tell you the true decline. It tells you that a small appraisal decline is weak evidence against a large one. Any capital decision tied to appraised values inherits the lag: fund NAVs, LTV covenants, redemption prices in open-end funds, and the owner anchoring of Examples 9.11–9.12.

Reproduce: `tests/test_ch09_examples.py::test_example_9_14`.

---

## 9.6 CRE application: the valuation reconciliation memo

Professional valuation is reconciliation, not calculation. A good memo states each method's indication, explains the gaps, and chooses. For the §9.1 office building:

| Method | Indication | What drives it | Weight and reason |
|---|---:|---|---|
| DCF (Ex 9.3) | \$34.8m | Re-leasing Tenant A, 8.25% exit cap, 9.0% $k$ | Primary. The cash-flow profile is irregular, so only a DCF can see it |
| Direct cap, stabilized cap on T-12 (Ex 9.12) | \$42.5m | T-12 NOI at 8.00% | Upper bound. It assumes the rollover costs nothing |
| Sales comparison | Not shown | Few recent suburban office sales; many are distressed | Low weight. Comps are stale and selected |
| Replacement cost | \$66m | Construction cost | No weight as value evidence. Tells you there will be no new supply |
| Seller's ask | \$48.6m | 7.0% on T-12 | Evidence of the seller's anchor, not of value |

The reconciliation also says what would change the answer: a signed renewal by Tenant A (value rises toward the direct-cap upper bound), or evidence that suburban office sales are clearing at 9%+ caps (value falls).

### Buyer and seller expectations: the negotiation zone

A transaction requires a price above the seller's reservation price and below the buyer's. The seller's reservation price comes from the anchor, the alternatives (refinance, hold), and constraints (maturity, fund life). The buyer's comes from the DCF. When the two do not overlap, as here (\$34.8 million versus an owner who will not accept much below \$48 million), no amount of negotiating closes the gap. One of three things must happen:

1. **Information changes the buyer's number.** For example, Tenant A renews.
2. **A constraint changes the seller's number.** For example, the loan matures and the lender will not extend; Case B.
3. **Structure bridges the gap.** For example, an earn-out tied to re-leasing, seller financing, or a master lease on the vacant space.

A speculator's edge is often knowing which of the three is coming, and when.

---

## 9.7 When the relationships fail

1. **$k - g$ breaks when $g$ is not stable.** The Gordon form assumes constant growth forever. For an asset in lease-up, repositioning, or structural decline, use an explicit DCF and apply $k - g$ only to the stabilized terminal period.
2. **Cap rates on thin markets are not prices.** When few assets trade, the "market cap rate" is an appraiser's or broker's opinion, and the trades that do occur are selected (Example 9.6). Reported cap rates can lag reality by several quarters.
3. **Replacement cost fails as a ceiling when construction is constrained.** Zoning, entitlement risk, or a shortage of labor or materials can keep value above replacement cost for years. It fails as a floor always.
4. **The DCF fails quietly when the reversion dominates.** At a 75% reversion share, the DCF is a cap-rate forecast with some cash flows attached. Precision in the operating years cannot compensate for an arbitrary exit cap.
5. **IRR decompositions are order-dependent and ignore risk.** A higher IRR from cap compression is not equivalent to a higher IRR from contractual rent. Decompose, then weight by how confident you are in each component.
6. **Leverage arithmetic assumes the loan survives.** Equity IRR grids assume no covenant breach and a successful refinance or sale at exit. If value falls far enough to breach an LTV or DSCR covenant, cash flow is swept and the hold period may be chosen by the lender, not by you (Case C).
7. **Appraisal smoothing is not stable.** Unsmoothing with a fixed $\alpha$ assumes appraisers behave the same in every cycle. Regulatory pressure, auditor scrutiny, and transaction volume all change how fast appraisals move.

---

## 9.8 Mispricing in practice: where anchors bind

Anchors matter for prices only when the anchored party is the marginal seller. Three conditions make anchors bind:

* **No forced sellers.** If most owners have long-dated, fixed-rate debt and no redemption pressure, anchored owners simply hold. Volume falls and reported prices barely move.
* **Appraisal-based accounting.** If fund NAVs, bank collateral values, and compensation are tied to appraisals, owners have an incentive to avoid trades that would set a lower mark.
* **Optionality in waiting.** A levered owner near zero equity holds a call option on recovery (Example 9.11; Case C). Selling exercises it at zero. Waiting is rational for the owner even if it is irrational for a hypothetical unlevered owner.

Anchors stop binding when a constraint forces the marginal transaction: a loan maturity without an extension, a fund wind-down, or redemption queues in open-end funds. The speculator's question is therefore not "Is the owner anchored?" but "When does the anchored owner stop being the marginal seller?"

---

## 9.9 Historical episode: appraisal lag and public–private divergence, 2008–09 and 2022–24

**Date and environment.** Two episodes. In 2008, U.S. credit markets seized after the failure of major financial institutions. In 2022, the Federal Reserve raised policy rates rapidly from near zero, and office demand faced a post-pandemic shift to remote and hybrid work. In both, listed REIT prices and private appraisal-based indices gave very different readings of the same underlying property market for a year or more.

**What was observable at the time.**

*2008–09.*

* The FTSE NAREIT All REIT Index ended 2008 with a total return of −37.34% [FACT; Nareit, January 2009, VERIFIED-SECONDARY; ch09-S01]. The FTSE NAREIT Equity REIT Index was up 1.76% for 2008 through 30 September and down 30.47% through 31 October [FACT; Nareit media updates, autumn 2008, VERIFIED-SECONDARY; ch09-S02]. Most of the 2008 REIT decline therefore occurred in the fourth quarter.
* The FTSE NAREIT Equity REIT Index returned 27.99% in 2009 [FACT; Nareit, December 2009 media update, and a 2009 mutual-fund annual report filed with the SEC; VERIFIED-SECONDARY; ch09-S03].
* NCREIF reported in 2024 that the NCREIF Property Index's value fell by almost 30% during the 2008–09 financial crisis [FACT; NCREIF press release, 25 July 2024, VERIFIED-SECONDARY; ch09-S04]. The calendar-year path of that decline (how much in 2008 versus 2009 and 2010) is *(verification pending)* and is not stated here.

*2022–24.*

* In 2022 the FTSE Nareit All Equity REITs Index returned −24.9%, its steepest annual decline since 2008. Office REITs returned −37.6%, the worst of any sector [FACT; Nareit year-end 2022 commentary, VERIFIED-SECONDARY; ch09-S05].
* The NCREIF Property Index returned 5.53% for calendar 2022. The fourth quarter was −3.50%: income +0.95%, appreciation −4.45% [FACT; LaSalle Investment Management review of NCREIF data, VERIFIED-SECONDARY; ch09-S06]. Capital Economics described Q4 2022 as the weakest quarter for NPI total returns since Q2 2009 [FACT; same source family, ch09-S06].
* The NPI returned −3.02% in Q4 2023 (income +1.11%, appreciation −4.13%) and −7.95% over the four quarters of 2023 [FACT; NCREIF 4Q2023 press release, 25 January 2024, VERIFIED-SECONDARY; ch09-S07].
* NCREIF's Expanded NPI market-value index had declined by about 16% from its 2Q2022 peak as of 1Q2024 [FACT; NCREIF 1Q2024 Expanded NPI release, VERIFIED-SECONDARY; ch09-S08].
* Green Street's Commercial Property Price Index, a transaction-based index, was reported in November 2023 as 22% below its March 2022 peak, with office down 35% [FACT as publicly reported by trade press citing Green Street; class C, VERIFIED-SECONDARY; ch09-S09].
* The Federal Reserve's Financial Stability Reports from 2023 onward identified commercial real estate valuations, especially office, as a risk to financial stability and noted weak fundamentals and tighter bank lending standards [FACT; Federal Reserve Board FSR, October 2023, as summarized in trade press; VERIFIED-SECONDARY; ch09-S10]. The precise price statistics cited in that report, including the price measure used, are *(verification pending)* against the primary PDF.

**Interpretations.**

1. *Appraisal lag (the dominant interpretation).* Appraisal-based indices move slowly because appraisers rely on past transactions and adjust incrementally. Listed REITs reprice continuously. In 2022 the gap was about 30 percentage points: −24.9% versus +5.53%. The NPI's subsequent negative returns through 2023 and the cumulative 16% value decline by early 2024 are consistent with the private index catching up [INFERENCE from the sequence of documented returns].
2. *Leverage and composition, not just lag.* REIT returns are levered equity returns, and REIT portfolios differ from NPI portfolios in property type and quality. A rough unlevering at a hypothetical 35% debt ratio and a 4% debt return gives $0.65 \times (-24.9\%) + 0.35 \times 4.0\% = -14.8\%$ [HYPOTHESIS: illustrative leverage and debt return; not a measured REIT leverage ratio]. A large gap remains after this adjustment: about 20.3 percentage points against 5.53%, roughly two-thirds of the raw 30.4-point gap. Comparing a levered equity index with an unlevered property index overstates the divergence.
3. *Liquidity overshooting.* Listed prices may overshoot fundamental value when forced sellers of liquid assets sell what they can (Chapter 1, §1.9; Chapter 3). On this view, REIT prices in late 2008 and 2022 were too low, not appraisals too high. The rapid REIT rebound in 2009 (27.99%) is consistent with partial overshooting, but it does not prove it.

**What a speculator could have done then.** In late 2008 and in 2022, investors could observe REIT-implied values well below appraisal values. Strategies available at the time included: buying listed REITs at discounts to private NAV (betting on overshooting); delaying private acquisitions or bidding at REIT-implied cap rates (betting on lag); and selling interests in open-end private funds at appraisal-based NAV before marks caught up. The last strategy was available only until redemption queues formed. Redemption queues in large open-end funds in 2022–23 were widely reported *(verification pending: specific funds and queue sizes are not stated here until checked against primary filings)*.

**What the episode establishes.** Appraisal-based indices lagged transaction-based and listed-market indicators in both episodes. Investors and lenders who relied on appraisals for marks, covenants, or redemption prices made decisions on stale information.

**What it does not establish.** It does not establish that REIT prices are always the "true" value; overshooting is a live alternative. It does not establish a stable smoothing parameter or a reliable lead time. The lead varied between episodes, and the 2022–24 divergence was concentrated in office. It does not establish that the gap is exploitable after costs, because private assets cannot be shorted and REITs differ from private portfolios in leverage and composition.

**CRE connection.** In Example 9.12 the 2021 appraisal is the owner's anchor. The episode shows the institutional version of the same problem: an entire asset class marked to anchors for several quarters. Example 9.14 provides the arithmetic.

---

## 9.10 Decision exercise: the office bid

Return to §9.1. You have the DCF (Example 9.3), the implied-growth analysis (Example 9.4), and the appraisal decomposition (Example 9.12). Write a one-page recommendation on the template at `desk/investment_memos/investment_committee_memo.md`. It must include:

1. Your value range, with the two or three assumptions that drive it, stated as forecasts.
2. Whether to bid now, and if so at what price and on what conditions. Consider an earn-out tied to re-leasing Tenant A's space.
3. What the seller must believe to accept your bid, and what would change the seller's position (debt maturity, fund life, appraisal reset).
4. Which of the broker's three anchors you would address in the bid letter, and how.
5. Walk-away triggers and the information that would raise or lower your bid.
6. Whether abstaining and setting a re-engagement trigger is the better choice.

**Rubric.** Score each element 0–4.

| Element | Full credit (4) | Partial (2) | None (0) |
|---|---|---|---|
| Value | DCF-based range of about \$32–38m with exit cap and re-leasing as stated drivers; reversion share noted | Single point estimate | Uses T-12 × cap, or the appraisal |
| Implied beliefs | Computes the 3.05% implied growth or the 1.44% IRR at ask; explains why the ask is not a price an informed buyer pays | Notes the ask is high, no numbers | Accepts the ask as market |
| Bid structure | Bid near DCF value, or a lower base price with an earn-out; diligence conditions on Tenant A | Bid without structure | Bids the ask or above DCF |
| Anchors | Addresses the appraisal with the decomposition table; dismisses replacement cost as value evidence while noting its supply implication | Mentions anchors qualitatively | Treats any anchor as value support |
| Abstention | Recognizes that no overlap may exist; sets a trigger (maturity, listing expiry, Tenant A decision) | Mentions waiting | Absent |

There is no single correct bid. A pass with a defined re-engagement trigger can earn full marks.

---

## 9.11 Frequent analytical errors

1. **Capitalizing the wrong NOI.** Trailing NOI on a property in transition, or stabilized NOI without deducting the cost and risk of getting there.
2. **Terminal value on trailing NOI.** The reversion capitalizes $NOI_{T+1}$.
3. **Ignoring capex in the cap rate.** $c = k - g$ holds only on free cash flow. Use $c = (k-g)/(1-\kappa)$.
4. **Exit cap = going-in cap by default.** This assumes the building does not age.
5. **Forgetting reassessment.** Capitalizing the seller's tax bill in a reassessment jurisdiction.
6. **Stale comps without time adjustment.** Especially the "best physical match" from before a market move.
7. **Treating replacement cost as a floor.** It is a long-run ceiling, through supply.
8. **Treating basis or a prior appraisal as value.** They predict seller behavior, not value.
9. **Reporting equity IRR without the grid.** Leverage that adds 40 bp to the mean can double the range.
10. **Calling cap compression "value-add."** Decompose the IRR, and pay sponsors for what they control.
11. **Comparing levered REIT returns with unlevered appraisal indices without adjustment.**
12. **Applying a precise discount rate to an arbitrary exit cap.** At a 75% reversion share, the exit cap dominates.

---

## 9.12 Connections to other chapters

* Chapter 2 develops appraisal smoothing and price formation in thin markets in more depth.
* Chapter 3 treats forced selling and reflexive collateral loops, which end anchoring.
* Chapter 6 connects cap rates to Treasury yields and computes the duration of CRE equity.
* Chapter 8 builds the NOI that this chapter capitalizes, including reserves and reassessment.
* Chapter 10 builds the debt-sizing, refinancing, and waterfall mechanics behind Example 9.8.
* Chapter 11 values hotels, where the NOI-versus-EBITDA and PIP issues of Case A dominate.
* Chapter 12 treats REIT-implied cap rates and distressed cycles.
* Chapter 13 treats hold/sell and the option value of waiting.
* Case A applies the loaded cap rate and the cost-basis anchor to a hotel. Case B treats the refinancing cliff. Case C applies this chapter's leverage arithmetic to a cap-rate shock.

---

## 9.13 One-page reference sheet

| Quantity | Formula |
|---|---|
| Direct cap | $V = NOI_1/c$ |
| DCF | $V = \sum_{t=1}^{T} \frac{NOI_t - CapEx_t}{(1+k)^t} + \frac{(1-s)NOI_{T+1}/c_T}{(1+k)^T}$ |
| Reversion share | $PV(\text{net reversion})/V$ |
| Cap rate with capex | $c = (k-g)/(1-\kappa)$ |
| Implied growth | $g = k - c(1-\kappa)$ |
| Implied return | $k = c(1-\kappa) + g$ |
| IRR identity | IRR $= c_0 + g$ if flat cap, no capex, no costs |
| Exit spread from aging | $\frac{k-g_T}{1-\kappa_T} - \frac{k-g_0}{1-\kappa_0}$ |
| Loaded cap | $V = N/(c+t)$; $t$ = tax rate × assessment ratio |
| As-is value | Stabilized value − cost to stabilize (− risk discount) |
| Residual land | $L = GDV(1-s)/(1+m) - (H+S+F)$ |
| Developer margin | $GDV(1-s)/\text{total cost} - 1$ |
| Levered return (1 period) | $r_E = r_A + \frac{\lambda}{1-\lambda}(r_A - r_D)$ |
| Cash leverage test | Cap rate vs loan constant $K$ |
| Appraisal smoothing | $A_t = \alpha A_{t-1} + (1-\alpha)V_t$ |
| Unsmoothing | $V_t = (A_t - \alpha A_{t-1})/(1-\alpha)$ |

**Questions to ask of any price.** Which NOI? Forward or trailing? After reserves and capex? Reassessed tax? What growth and exit cap does it imply? What share of value is the reversion? Which part of the IRR is business plan and which is market? Who is the marginal buyer, and what must they believe? What anchor is the seller using, and what event will release it?

**Rules of thumb (test them, do not trust them).** A 100 bp exit-cap move changes a 5-year property IRR by about 300 bp at 5–6% caps (Example 9.9). Reversion is 60–80% of a 5-year DCF. Residual land value moves 10–20 times as much as GDV in percentage terms (Example 9.7). An appraisal index may show only a third to a half of a sudden decline in the first year [HYPOTHESIS; Example 9.14 uses $\alpha = 0.6$].

---

## References for this chapter

Source entries with IDs and verification status are in `references/sources_ch09.md`.

* Geltner, D. (1993). "Estimating Market Values from Appraised Values without Assuming an Efficient Market." *Journal of Real Estate Research*, 8(3), 325–345.
* Kahneman, D., and Tversky, A. (1979). "Prospect Theory: An Analysis of Decision under Risk." *Econometrica*, 47(2), 263–291.
* Tversky, A., and Kahneman, D. (1974). "Judgment under Uncertainty: Heuristics and Biases." *Science*, 185(4157), 1124–1131.
* Nareit. Media updates and market commentary, October 2008, January 2009, December 2009, and year-end 2022. https://www.reit.com
* NCREIF. NPI press releases for 4Q2023 (25 January 2024), Expanded NPI 1Q2024, and Expanded NPI 2Q2024 (25 July 2024). https://ncreif.org
* LaSalle Investment Management (2023). "U.S. Private Real Estate Returns Review, 2022 Q4."
* Board of Governors of the Federal Reserve System. *Financial Stability Report*, October 2023.
* Green Street Commercial Property Price Index, as publicly reported in November 2023 trade press coverage.
