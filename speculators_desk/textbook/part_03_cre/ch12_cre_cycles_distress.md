# Chapter 12 — CRE Cycles and Distressed Opportunity

> **Status:** Complete (v1.0). Every number in the text, problems, and solutions is reproduced in `tests/test_ch12_examples.py` (library module `models/python/sdesk/x_cre_distress.py`, plus `sdesk.cre.distressed_loan_recovery`). Problems are in `problems/questions/ch12_problems.md` and solutions in `problems/solutions/ch12_solutions.md`. Sources are in `references/sources_ch12.md`. Items marked *(verification pending)* are not presented as established fact. Companion cases: Case E (`cases/hypothetical/case_E_distressed_office/`) and Case G (`cases/hypothetical/case_G_buying_the_debt/`).

## Learning objectives

After this chapter you should be able to:

1. Explain why real estate markets overshoot, using a stock-flow model with a construction lag. Simulate it numerically and identify which parameter, the lag or the developers' response to current rents, drives the size of the overbuild.
2. Separate the four causes of CRE distress: supply shocks, demand destruction (cyclical versus structural), maturity walls, and interest-rate resets. Diagnose a stressed asset as a *liquidity* problem or a *solvency* problem with a refinancing calculation.
3. Price a non-performing loan from resolution scenarios (cure, discounted payoff, deed-in-lieu, contested foreclosure, bankruptcy), compute the maximum bid at a required return, and explain why the mean scenario IRR overstates the return.
4. Quantify foreclosure economics: statutory timelines (verified for Texas non-judicial sales), carrying and legal costs, value drift, and the present-value cost of a judicial process.
5. Describe how CMBS special servicing works, compute an appraisal reduction amount and its effect on servicer advances and on the controlling class, and identify servicer incentives that diverge from bondholders'.
6. Apply the 2006 interagency CRE concentration screens (100% and 300% of total risk-based capital) to a bank balance sheet, and compute the loan sales a bank needs when sale losses reduce the capital in the denominator.
7. Read REIT prices as private-market signals: compute the implied cap rate from enterprise value and the discount to NAV, and say what each does and does not tell you about private values.
8. Compute a basis reset: show how a buyer at a lower basis can charge lower rents and still earn a higher yield, and why this pushes distress onto incumbent owners.
9. Judge "buying through the downturn" claims against the evidence actually available, and recognize when the right answer is to wait.

---

## 12.1 Opening investment problem: three ways into one downturn

You manage a \$250 million opportunistic real estate allocation for a family office. Office and some floating-rate multifamily credits are under stress in your Sun Belt metro. Three things arrive in the same week. All facts are [HYPOTHESIS] — a constructed teaching case.

**A. A non-performing loan.** A regional bank offers a \$40.0 million first-mortgage note on a suburban office property. The borrower missed its maturity date four months ago. The bank's broker says the collateral is "worth about \$31 million as-is" and asks for bids "in the low-to-mid 60s" (cents on the dollar of unpaid principal). The bank is above the regulators' 300% CRE concentration screen and wants the loan off its balance sheet before year-end.

**B. A bank-owned office tower.** A 520,000 sf, 38%-leased CBD tower is offered at about \$100/sf, against a replacement cost the broker puts at \$480/sf. "You are buying at a fifth of replacement cost." (Case E develops this asset.)

**C. A public REIT.** An office REIT with Sun Belt exposure trades at \$42 per share. Your analyst's net asset value, built from private-market cap rates, is about \$55. "The public market is offering private real estate at a 24% discount."

Each opportunity offers a discount. The discounts are measured against different reference points: unpaid principal, replacement cost, and appraised NAV. None of those reference points is a value. The work of this chapter is to replace each reference point with an estimate of what the claim will actually pay, when it will pay, and what can go wrong between now and then. Section 12.10 returns to the allocation.

---

## 12.2 Economic intuition

### Why real estate cycles overshoot

Space is produced slowly and lasts a long time. An office tower takes three to five years from decision to delivery, and it then stands for fifty years. Developers decide to build on the basis of current rents and current financing. They cannot observe how much competing space is already in the pipeline until it shows up in construction starts, and even then the decision to start is not easily reversed. When demand rises, rents rise because supply cannot respond. High rents trigger starts. The starts arrive years later, often after demand growth has slowed, and vacancy rises. Rents then fall far enough to stop new construction for years. The cycle is a feature of the production lag, not of irrationality. Section 12.5.1 shows the mechanism with arithmetic.

Two features make the downturn worse than the upturn is good. First, existing space cannot be withdrawn: a half-empty building still exists, and its owner will cut rents to fill it as long as rent exceeds the marginal cost of occupancy. Second, most CRE is financed with debt that matures on a calendar date that has nothing to do with the cycle. Owners whose loans mature at the bottom must refinance into a market with lower values, lower loan-to-value limits, and often higher rates.

### Four causes of distress

| Cause | Mechanism | Persistence | Diagnostic |
|---|---|---|---|
| Supply shock | Deliveries exceed absorption | Cyclical; ends when the pipeline clears | Deliveries and under-construction as % of stock |
| Cyclical demand loss | Recession reduces space demand | Cyclical; recovers with employment | Net absorption versus employment growth |
| Structural demand destruction | Use per worker or per unit of output falls permanently (e.g., remote and hybrid work for office, e-commerce for some retail) | Persistent; old stock may never re-lease | Leasing per employee, sublease space, tenant downsizing at renewal |
| Financing shock | Maturity wall, rate reset, lender retrenchment | Lasts until loans are refinanced, restructured, or foreclosed | Maturities by year; refinance gaps; bank concentration |

The first two causes are what "buy at the bottom of the cycle" assumes. The third makes that strategy dangerous: a structural loss in demand looks like a cyclical one in the first two years. Case E is built around that ambiguity.

### Liquidity versus solvency

A property is in a **liquidity** problem when its value exceeds its debt but the owner cannot refinance or pay current obligations. A property is in a **solvency** problem when its value is below its debt. The distinction decides who has the economic interest, what the owner will do, and who the counterparty for a distressed buyer actually is.

* In a liquidity problem the equity has positive value. The owner will sell, recapitalize, or make a capital call. A distressed buyer is competing with the owner's own alternatives, and the discount available is the price of immediacy (Chapter 1).
* In a solvency problem the equity is worthless or nearly so. It retains only option value and hold-up value: the ability to delay, litigate, or file for bankruptcy. The lender is the real owner. A distressed buyer negotiates with the lender, buys the loan, or buys the property from the lender after foreclosure.

Interest-rate resets turn many solvent properties into liquidity problems and many marginal ones into insolvency. Example 12.2 shows both.

### Who sells at a discount, and why

A distressed price exists because a seller values immediacy, certainty, or balance-sheet relief more than the expected value of waiting. Lenders sell loans to reduce concentration, to stop accruing workout costs, to recognize losses in a quarter of their choosing, or because their own regulators or funding sources require it. Funds sell because of redemption queues, fund-life expirations, or covenant breaches. CMBS trusts sell through a special servicer whose incentives are set by the pooling and servicing agreement. Each forced seller is a liquidity consumer, and the buyer is paid as a liquidity provider. The danger is the one Chapter 1 named: liquidity providers are short a put on liquidity itself, and the buyer of distressed real estate in the early part of a downturn is often the forced seller of the later part.

### Public and private prices

REIT shares reprice every second. Private appraisals reprice when appraisers find comparable sales, which in a frozen market can take a year or more. When the public market falls and private marks do not, the gap is information: the REIT price is a fast but noisy estimate of where private transactions will clear. It is also a slow estimate of nothing in particular when REIT shares are moved by fund flows, index changes, or the REIT's own leverage and management. Section 12.5.7 makes the comparison precise.

---

## 12.3 Technical definitions

| Term | Definition |
|---|---|
| Stock, completions, starts | Existing space $S_t$; space delivered in year $t$, $C_t$; space begun in year $t$, $N_t$. With a lag of $L$ years, $C_t = N_{t-L}$ |
| Natural vacancy | The vacancy rate $v^*$ at which real rents are stable. Above it rents fall; below it they rise |
| Feasibility rent | The rent at which new construction earns the developer's required yield on total cost. Starts are near zero below it |
| Maturity wall | A concentration of loan maturities in a short period, usually loans originated in one vintage under one set of rates and underwriting standards |
| Refinance gap | Existing balance plus refinancing costs minus the maximum new loan. Positive means equity must be contributed |
| Capital call | A demand by a fund or joint venture for additional equity from its partners. A partner who does not fund is usually diluted |
| Non-performing loan (NPL) | A loan in payment or maturity default. Its value is the present value of the resolution, not its unpaid principal balance (UPB) |
| Discounted payoff (DPO) | A lender's agreement to accept less than the full debt in satisfaction of the loan |
| Deed-in-lieu | The borrower conveys the property to the lender in place of foreclosure, usually in exchange for releases and sometimes "cash for keys" |
| Judicial / non-judicial foreclosure | Foreclosure through a court action, versus a sale by a trustee under a power of sale in a deed of trust without a court action |
| Credit bid | At a foreclosure sale, the lender may bid up to the amount of its debt without paying cash |
| Special servicer | The CMBS servicer that manages defaulted or imminently defaulting loans for the trust |
| Appraisal reduction amount (ARA) | The amount by which a defaulted loan's claim exceeds a haircut appraised value; it reduces servicer advances and, in many deals, the voting balance of junior classes |
| Controlling class / B-piece | The most junior outstanding CMBS class (or its representative), which typically appoints or directs the special servicer |
| CLD loans | Construction, land development, and other land loans |
| Total risk-based capital | The capital measure used as the denominator in the 2006 CRE concentration screens |
| Implied cap rate | Forward NOI divided by the value of real estate implied by a REIT's enterprise value |
| NAV discount | Share price divided by net asset value per share, minus one |
| Basis | A buyer's all-in cost: price, closing costs, and capital required to stabilize |
| Basis reset | A transfer of ownership at a lower basis, which changes the rent at which the new owner earns its required return |
| Vintage year | The year a fund or investment begins deploying capital. "Vintage-year evidence" compares returns by start year |

---

## 12.4 Equations and derivations

### 12.4.1 A stock-flow model with a construction lag

Let latent space demand be $D_t$ (square feet that would be occupied at today's rent), stock $S_t$, and rent $R_t$. Space depreciates or is withdrawn at rate $\delta$. Annual steps:

$$D_t = D_{t-1}(1+g_t), \qquad C_t = N_{t-L}, \qquad S_t = S_{t-1}(1-\delta) + C_t,$$
$$O_t = \min(D_t, S_t), \qquad v_t = 1 - \frac{O_t}{S_t},$$
$$R_t = R_{t-1}\,\big[1 + \alpha\,(v^* - v_t)\big], \qquad N_t = \kappa \,\max\!\Big(0,\ \frac{R_t}{R^F} - 1\Big)\, S_t.$$

Here $\alpha$ is the rent response to the vacancy gap, $R^F$ is the feasibility rent, and $\kappa$ is the starts response: starts as a fraction of stock per unit of rent premium over feasibility. The model is a discrete version of the stock-flow logic in DiPasquale and Wheaton (1992) and the cyclical models that followed it (Wheaton, 1999). The parameters here are [HYPOTHESIS] and chosen for teaching.

**Why the lag creates overshooting.** Starts depend on today's rent. Today's rent depends on today's vacancy. Today's vacancy does not yet include the space started in the last $L$ years. So the signal to keep building stays on for $L$ years after enough space has been started. Steady-state analysis hides this. In a steady state $C = N = \delta S$ and $v = v^*$, which is true and useless during the transition. Wheaton (1999) shows formally that whether the cycle dampens or explodes depends on the product of the lag, the supply response, and the rent response. The simulation in Example 12.1 shows the same thing numerically.

### 12.4.2 Refinancing and the rate reset

From Chapter 10, the maximum new loan is

$$L_{\max} = \min\Big(\lambda V,\ \frac{NOI}{DSCR_{\min}\,K},\ \frac{NOI}{DY_{\min}}\Big), \qquad K = 12\cdot\frac{i}{1-(1+i)^{-n}},\ \ i = r/12,$$

and the refinance gap is $G = B + \text{costs} - L_{\max}$. For an interest-only loan refinanced into an amortizing loan, the coverage ratio on the *existing* balance moves from $NOI/(B r_0)$ to $NOI/(B K_1)$. The ratio of the two is $r_0/K_1$. A move from a 3.60% interest-only rate to a 6.25% rate with 30-year amortization ($K_1 = 7.389\%$) cuts coverage by a factor of $0.036/0.07389 = 0.487$, more than half, with no change in the property.

### 12.4.3 Pricing a non-performing loan

Let resolution scenario $s$ occur with probability $p_s$, pay gross cash $X_s$, cost $c_s$ in legal and carrying expenses, and resolve at time $\tau_s$ (years). At required return $k$, the maximum price is

$$P_{\max} = \sum_s p_s\,\frac{X_s - c_s}{(1+k)^{\tau_s}}.$$

The library implements this as `sdesk.cre.distressed_loan_recovery`. Three cautions apply.

1. **Scenario IRRs are not additive.** Fast resolutions produce very high annualized returns on small dollar gains (a 0.5-year DPO), and slow resolutions produce low returns on capital tied up for years. The probability-weighted mean of scenario IRRs therefore overstates the return. The IRR of expected cash flows is the more defensible single number (Chapter 1, §1.4.1).
2. **The scenarios are not independent of the price you pay.** A borrower facing a buyer who paid 60 cents knows the buyer can accept a DPO at 75 and still profit. Your basis is information to the borrower.
3. **The discount rate is a required return, not a market yield.** It must compensate for legal uncertainty, valuation error, and the possibility that every scenario's collateral value is wrong in the same direction.

### 12.4.4 Foreclosure recovery

If the collateral is worth $V_0$ today and drifts at rate $d$ per year while the lender waits $T$ years (foreclosure plus resale), the net recovery is

$$N_T = V_0(1+d)^T(1-s) - \text{carry}\times T - \text{legal}, \qquad PV = \frac{N_T}{(1+k)^T},$$

where $s$ is the selling cost. Time hurts three ways: the value drifts (usually down for a neglected asset), carry accumulates linearly, and discounting compounds. The library function is `x_cre_distress.foreclosure_recovery`.

### 12.4.5 The appraisal reduction amount

In a typical CMBS pooling and servicing agreement, once a loan is in special servicing and a new appraisal is obtained, the **appraisal reduction amount** is

$$ARA = \max\Big(0,\ \underbrace{B + I_{acc} + A + O}_{\text{trust's claim}} - \big[(1-h)\,V_{appr} + \text{reserves}\big]\Big),$$

with $B$ the principal balance, $I_{acc}$ accrued unpaid interest, $A$ unreimbursed advances, $O$ other amounts due (taxes, insurance, fees), and $h$ the haircut, commonly 10% (so 90% of appraised value). Deal documents govern the exact items. Two consequences follow:

* **Advances shrink.** The servicer's interest advance is reduced, typically in proportion $1 - ARA/B$. The junior bondholders stop receiving interest first.
* **Control can shift.** Many post-2010 deals reduce the controlling class's balance by allocated ARAs when testing whether it still controls. If the reduced balance falls below a threshold of its original balance (25% is a common figure in post-2010 deals [HYPOTHESIS: deal-specific; check the governing PSA]), control passes to the next senior class.

### 12.4.6 Bank concentration and forced sales

The 2006 interagency guidance on CRE concentrations identifies banks for heightened supervisory attention when (1) construction, land development, and other land loans are at least 100% of total risk-based capital, or (2) total non-owner-occupied CRE loans are at least 300% of total risk-based capital **and** that portfolio grew at least 50% in the prior 36 months [FACT; OCC Bulletin 2006-46 and 71 FR 74580; see `references/sources_ch12.md`]. The screens are not lending limits.

Suppose a bank with CRE loans $C$ and capital $K$ wants $C/K \le m$ by selling loans at price $p$ per dollar of carrying value, with tax rate $\tau$. Selling $X$ reduces the numerator by $X$ and the denominator by the after-tax loss $(1-p)(1-\tau)X$:

$$C - X = m\big[K - (1-p)(1-\tau)X\big] \;\Rightarrow\; X = \frac{C - mK}{1 - m(1-p)(1-\tau)}.$$

The denominator is the feedback loop. At $m = 3$ and no tax, a sale price below $p = 2/3$ makes the denominator zero or negative: selling cannot fix the ratio, because each dollar sold destroys more than a third of a dollar of capital, which at 3x supports more than a dollar of loans. Below that price, the bank must raise capital or wait.

### 12.4.7 REIT-implied cap rates and NAV

$$V^{RE}_{implied} = \text{Market cap} + \text{Debt} + \text{Preferred} - \text{Cash} - \text{Other assets}, \qquad c_{implied} = \frac{NOI^{cash}_{fwd}}{V^{RE}_{implied}}.$$

$$NAV = \frac{NOI^{cash}_{fwd}}{c_{private}} - \text{Debt} - \text{Preferred} + \text{Cash} + \text{Other assets}, \qquad \text{Discount} = \frac{P}{NAV/\text{share}} - 1.$$

Because NAV is levered, a 1% change in gross asset value moves NAV by $GAV/NAV$ percent. In Example 12.7, debt and preferred equal 40% of gross asset value and $GAV/NAV = 1.58$, so modest disagreements about private cap rates produce large NAV disagreements.

### 12.4.8 Basis and required rent

For rentable area $A$, occupancy $o$, operating expenses $E$, recurring leasing capital $LC$, and target yield $y$ on basis $P$:

$$R_{req} = \frac{yP + E + LC}{A\,o}.$$

Two owners of identical buildings face the same $E$, $LC$, and market rent, but their $R_{req}$ differ through $yP$ alone. The owner with the lower basis can cut rent by $\Delta R = (y_1P_1 - y_2P_2)/(Ao)$ and still earn its target.

---

## 12.5 Worked examples

All examples are reproduced in `tests/test_ch12_examples.py`. Inputs are [HYPOTHESIS] unless a source is cited.

### Example 12.1 — A development cycle in sixteen years

**Given.** A metro office market with stock $S_0 = 100$ million sf and latent demand $D_0 = 92$ million sf (8.0% vacancy). Rent $R_0 = \$30.00$/sf. Natural vacancy $v^* = 10\%$. Rent response $\alpha = 0.5$ (rents rise 0.5% per year for each point that vacancy is below 10%). Feasibility rent $R^F = \$33.00$. Starts response $\kappa = 0.35$. Construction lag $L = 3$ years. Depreciation $\delta = 1\%$ per year. Demand growth: +3% in years 1–4, −3% in year 5, 0% in year 6, +1.5% thereafter. No space is under construction at the start.

**Find.** The path of stock, vacancy, rent, completions, and starts. Compare the peak vacancy with a market whose lag is one year.

**Solution.** Year 1: $D_1 = 92 \times 1.03 = 94.76$. No completions, so $S_1 = 100 \times 0.99 = 99.00$, $v_1 = 1 - 94.76/99.00 = 4.28\%$. $R_1 = 30 \times [1 + 0.5(0.10 - 0.0428)] = \$30.86$. Since $R_1 < 33$, starts are zero.

Year 3 is the first year with starts: $R_3 = \$33.95$, so $N_3 = 0.35 \times (33.95/33 - 1) \times 97.03 = 0.98$ million sf. Those starts deliver in year 6.

| Year | Stock | Latent demand | Vacancy | Rent | Completions | Starts |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 100.00 | 92.00 | 8.00% | 30.00 | 0.00 | 0.00 |
| 1 | 99.00 | 94.76 | 4.28% | 30.86 | 0.00 | 0.00 |
| 2 | 98.01 | 97.60 | 0.42% | 32.34 | 0.00 | 0.00 |
| 3 | 97.03 | 100.53 | 0.00% | 33.95 | 0.00 | 0.98 |
| 4 | 96.06 | 103.55 | 0.00% | 35.65 | 0.00 | 2.70 |
| 5 | 95.10 | 100.44 | 0.00% | 37.43 | 0.00 | 4.47 |
| 6 | 95.13 | 100.44 | 0.00% | 39.31 | 0.98 | 6.36 |
| 7 | 96.88 | 101.95 | 0.00% | 41.27 | 2.70 | 8.50 |
| 8 | 100.38 | 103.48 | 0.00% | 43.33 | 4.47 | 11.00 |
| 9 | 105.74 | 105.03 | 0.67% | 45.35 | 6.36 | 13.86 |
| 10 | 113.18 | 106.60 | 5.81% | **46.31** | 8.50 | 15.97 |
| 11 | 123.05 | 108.20 | 12.07% | 45.83 | 11.00 | 16.74 |
| 12 | 135.67 | 109.83 | 19.05% | 43.75 | 13.86 | 15.47 |
| 13 | 150.29 | 111.47 | 25.83% | 40.29 | 15.97 | 11.62 |
| 14 | 165.53 | 113.15 | 31.65% | 35.93 | 16.74 | 5.14 |
| 15 | 179.34 | 114.84 | 35.97% | 31.27 | 15.47 | 0.00 |
| 16 | 189.17 | 116.57 | 38.38% | 26.83 | 11.62 | 0.00 |

(Stock, demand, completions, and starts in millions of sf; rent in \$/sf.)

Three features stand out.

1. **The year-5 recession is invisible.** Demand falls 3%, but latent demand still exceeds stock, so vacancy stays at zero and rents keep rising. Developers see no reason to stop.
2. **Starts peak (year 11) after rents peak (year 10)** and keep coming at nearly 16 million sf a year while vacancy climbs from 6% to 19%. Rent is still above the \$33 feasibility level, so the rule keeps starting buildings that will deliver into a market already oversupplied.
3. **Peak vacancy arrives after starts stop.** Starts end in year 15. Completions continue through year 17, and vacancy peaks at **38.51% in year 17**.

Running the same model with $L = 1$ (everything else unchanged), peak vacancy is **19.62% in year 12**, the rent peak is **\$39.87 in year 8**, and twenty-year completions are 51.51 million sf instead of 112.82 million sf.

**Check.** Steady-state identity: once starts stop, stock declines at 1% a year. From year 18 to 19 in the $L=3$ run there are no completions, and the test confirms $S_{19} = 0.99\,S_{18}$. The table rows reproduce from `x_cre_distress.stock_flow_simulation`.

**Decision consequence.** The model is crude, and its rents in the late years are too low because it has no floor at operating cost (§12.7). Its lesson survives the crudeness: **the length of the construction lag, not the size of the demand shock, decides how bad the downturn is.** For an acquisition, the variable to measure is space under construction and recently started as a percentage of stock, relative to plausible absorption over the lag. A buyer at the end of year 10, when vacancy is under 6% and rents are at their peak, is buying into a market that has already started 40.83 million sf that will deliver over the next three years, 36% of the existing stock, and the rule will start another 48.98 million sf before it stops. The first number was knowable from construction-start data. The vacancy rate was not the right statistic to watch.

### Example 12.2 — Maturity wall and rate reset: liquidity or solvency?

**Given.** A 300-unit apartment property financed in 2021 with a \$60.0 million five-year interest-only loan at 3.60%. NOI at origination was \$4.50 million. The loan now matures. Two states of the world:

* **State 1:** NOI has grown to \$4.80 million. The market cap rate is 5.75%.
* **State 2:** NOI is \$3.90 million (new supply forced concessions; insurance and taxes rose). The market cap rate is 6.50%.

New loan terms: 6.25% rate, 30-year amortization, maximum 65% LTV, minimum 1.25x DSCR, minimum 8.0% debt yield. Refinancing costs 1% of the new loan. Selling costs 2%.

**Find.** DSCR before and after the reset; the maximum new loan and the binding constraint; the refinance gap; and whether the owner faces a liquidity or a solvency problem.

**Solution.**

Coverage at origination: $DS_0 = 60{,}000{,}000 \times 0.036 = \$2{,}160{,}000$; $DSCR_0 = 4{,}500{,}000/2{,}160{,}000 = 2.08x$.

Loan constant at the new terms: $K = 7.3886\%$. Debt service on the existing \$60 million at the new terms would be $60{,}000{,}000 \times 0.073886 = \$4{,}433{,}164$.

*State 1.* $V = 4{,}800{,}000/0.0575 = \$83{,}478{,}261$. Coverage on the existing balance at new terms: $4{,}800{,}000/4{,}433{,}164 = 1.08x$, against 2.22x at the old rate. Constraints:

* LTV: $0.65 \times 83{,}478{,}261 = \$54{,}260{,}870$
* DSCR: $4{,}800{,}000/(1.25 \times 0.073886) = \$51{,}971{,}912$ ← binding
* Debt yield: $4{,}800{,}000/0.08 = \$60{,}000{,}000$

Gap $= 60{,}000{,}000 + 0.01 \times 51{,}971{,}912 - 51{,}971{,}912 = \$8{,}547{,}807$. Equity at market value $= 83{,}478{,}261 - 60{,}000{,}000 = \$23{,}478{,}261$; net of selling costs, a sale clears $83{,}478{,}261 \times 0.98 - 60{,}000{,}000 = \$21{,}808{,}696$.

*State 2.* $V = 3{,}900{,}000/0.065 = \$60{,}000{,}000$. Constraints: LTV \$39,000,000 ← binding; DSCR \$42,227,178; debt yield \$48,750,000. Gap $= 60{,}000{,}000 + 390{,}000 - 39{,}000{,}000 = \$21{,}390{,}000$. A sale nets $60{,}000{,}000 \times 0.98 - 60{,}000{,}000 = -\$1{,}200{,}000$.

| | State 1 | State 2 |
|---|---:|---:|
| Value | \$83.48m | \$60.00m |
| Max new loan (binding) | \$51.97m (DSCR) | \$39.00m (LTV) |
| Refinance gap | \$8.55m | \$21.39m |
| Net sale proceeds to equity | +\$21.81m | −\$1.20m |
| Diagnosis | Liquidity | Solvency |

**Check.** State 1 debt yield on the new loan: $4.80/51.97 = 9.24\% > 8\%$; LTV $= 62.3\% < 65\%$; DSCR exactly 1.25x. State 2 at the LTV-sized loan: DSCR $= 3.90/(39.0 \times 0.073886) = 1.35x$, consistent with DSCR not binding.

**Decision consequence.** In State 1 nothing is wrong with the property. The rate reset cut coverage by half and created an \$8.5 million gap, but the equity is worth about \$22 million after selling costs. The owner will sell, bring in preferred equity, or make a capital call, and any partner will fund it because \$8.5 million protects \$22 million. A distressed buyer here is buying from a seller with good alternatives and should expect a small discount. In State 2 the owner would have to contribute \$21.4 million to keep an asset whose equity is worth less than zero after costs. No rational partner funds that capital call without a restructuring. The lender is the counterparty. The opportunity, if there is one, is in the loan (Example 12.3 and Case G) or in the REO later. **Diagnose first, then pick the instrument.**

### Example 12.3 — Pricing the non-performing loan (Opportunity A)

**Given.** The \$40.0 million UPB office note. Contract rate 6.0%. As-is collateral value \$31.0 million (broker), which you accept for the moment. Resolution scenarios, with gross cash to the noteholder, costs (legal, carry, protective advances, net of any cash collected), and timing:

| Scenario | $p$ | Gross recovery | Costs | Years |
|---|---:|---:|---:|---:|
| Cure: borrower refinances, pays UPB + one year's interest | 0.10 | \$42,400,000 | \$150,000 | 1.00 |
| Discounted payoff | 0.25 | \$34,000,000 | \$250,000 | 0.50 |
| Deed-in-lieu, then resale at \$31.0m less 2% | 0.30 | \$30,380,000 | \$1,000,000 | 1.25 |
| Contested foreclosure, resale at \$29.5m less 2% | 0.20 | \$28,910,000 | \$2,200,000 | 2.00 |
| Borrower bankruptcy, resale at \$29.0m less 2% | 0.15 | \$28,420,000 | \$3,500,000 | 3.00 |

Required return $k = 16\%$.

**Find.** The maximum bid; the scenario returns and expected profit at a \$24.0 million bid; the IRR of expected cash flows.

**Solution.** Net cash and present value at 16%:

| Scenario | Net cash | PV at 16% | $p \times PV$ |
|---|---:|---:|---:|
| Cure | 42,250,000 | 36,422,414 | 3,642,241 |
| DPO | 33,750,000 | 31,336,088 | 7,834,022 |
| Deed-in-lieu | 29,380,000 | 24,405,028 | 7,321,508 |
| Contested | 26,710,000 | 19,849,881 | 3,969,976 |
| Bankruptcy | 24,920,000 | 15,965,189 | 2,394,778 |
| **Total** | | | **25,162,526** |

Maximum bid at 16%: **\$25.16 million, 62.9% of UPB**.

At a \$24.0 million bid (60.0% of UPB):

| Scenario | Profit | Annualized return |
|---|---:|---:|
| Cure | 18,250,000 | 76.04% |
| DPO | 9,750,000 | 97.75% |
| Deed-in-lieu | 5,380,000 | 17.56% |
| Contested | 2,710,000 | 5.49% |
| Bankruptcy | 920,000 | 1.26% |

Expected profit $= \$6{,}556{,}500$. Probability-weighted mean of the scenario returns $= 0.10(76.04\%) + 0.25(97.75\%) + 0.30(17.56\%) + 0.20(5.49\%) + 0.15(1.26\%) = 38.60\%$. The IRR of expected cash flows, the rate $k$ solving $\sum_s p_s N_s/(1+k)^{\tau_s} = 24{,}000{,}000$, is **20.46%**. Expected NPV at 16% $= 25{,}162{,}526 - 24{,}000{,}000 = \$1{,}162{,}526$.

**Check.** The expected resolution time is $\sum p_s \tau_s = 1.45$ years, and expected net cash is \$30,556,500. A single payment of that amount at 1.45 years would imply $(30{,}556{,}500/24{,}000{,}000)^{1/1.45} - 1 = 18.1\%$. The exact figure is higher (20.46%) because the large payments arrive early. Discounting is convex in time, so averaging the timing understates the return here.

**Decision consequence.** The 38.6% average return is an artifact: it is dominated by small, fast outcomes. The defensible estimate is about 20%, and it depends on the 65% of probability in fast, consensual outcomes (cure, DPO, deed-in-lieu). If you believe the borrower will fight, shift 0.15 of probability from DPO to contested foreclosure. Expected PV falls by $0.15 \times (31{,}336{,}088 - 19{,}849{,}881) = \$1{,}722{,}931$ and the maximum bid at 16% falls to \$23.44 million, below the \$24.0 million bid. **The single most valuable piece of diligence is the borrower's position: its other assets, its guarantor's exposure under the carve-out guaranty, and its lawyers.** Two further points belong in the bid memo. First, the broker's \$31 million as-is value is the seller's number. Every title scenario depends on it, so commission your own valuation. Second, bidding 60 rather than 63 is not only about return: a lower basis lets you accept a DPO the borrower can actually finance.

### Example 12.4 — Foreclosure economics: Texas versus a judicial state

**Given.** A defaulted loan secured by a property worth \$20.0 million today. While the lender waits, the value drifts at −4% per year (deferred maintenance, tenant attrition), carrying costs net of any rent collected are \$600,000 per year, and selling costs on resale are 2%. Resale takes six months after the lender takes title. Required return 12%.

* **Texas (non-judicial).** Under Tex. Prop. Code §51.002, a foreclosure sale under a deed of trust is a public auction held between 10 a.m. and 4 p.m. on the first Tuesday of a month, and notice of sale must be given at least 21 days before the sale [FACT; statute text, see sources]. For property used as the debtor's residence, the servicer must first give at least 20 days' notice to cure (§51.002(d)); commercial loans rely on their loan documents for default notices. Assume three months from default to sale (loan-document notice and acceleration plus the statutory notice period) and \$150,000 of legal costs.
* **Judicial state (hypothetical).** Assume 24 months from default to sale through a court action with a receiver, and \$600,000 of legal costs. This timeline is [HYPOTHESIS]. Actual judicial timelines vary by state, county, court backlog, and borrower defenses, and must be checked locally.

**Find.** Net recovery and present value in each case. Then find the earliest Texas sale date if notice is given on Wednesday 11 March 2026, and if it is given on Wednesday 18 March 2026.

**Solution.**

*Texas:* $T = (3 + 6)/12 = 0.75$ years. Value at resale $= 20{,}000{,}000 \times 0.96^{0.75} = \$19{,}396{,}949$. Carry $= 600{,}000 \times 0.75 = \$450{,}000$. Net $= 19{,}396{,}949 \times 0.98 - 450{,}000 - 150{,}000 = \$18{,}409{,}010$. $PV = 18{,}409{,}010/1.12^{0.75} = \$16{,}908{,}961$.

*Judicial:* $T = (24 + 6)/12 = 2.5$ years. Value $= 20{,}000{,}000 \times 0.96^{2.5} = \$18{,}059{,}598$. Carry $= \$1{,}500{,}000$. Net $= 18{,}059{,}598 \times 0.98 - 1{,}500{,}000 - 600{,}000 = \$15{,}598{,}406$. $PV = 15{,}598{,}406/1.12^{2.5} = \$11{,}749{,}927$.

| | Texas | Judicial |
|---|---:|---:|
| Years to cash | 0.75 | 2.50 |
| Value at resale | \$19.40m | \$18.06m |
| Carry + legal | \$0.60m | \$2.10m |
| Net cash | \$18.41m | \$15.60m |
| PV at 12% | **\$16.91m** | **\$11.75m** |
| PV as % of today's value | 84.5% | 58.7% |

The difference is \$5.16 million, 25.8% of today's collateral value.

*Texas sale dates.* Notice on 11 March 2026: the earliest permissible date is 1 April 2026; the first Tuesday of April 2026 is 7 April, which is later than 1 April, so the sale can be held **7 April 2026** (27 days after notice). Notice on 18 March 2026: the earliest date is 8 April 2026; the first Tuesday of April (7 April) is too early, so the sale moves to **5 May 2026** (48 days after notice). A one-week delay in posting notice costs four weeks.

**Check.** Decomposing the \$5.16 million: value drift accounts for $(19.40 - 18.06) \times 0.98 = \$1.31$ million of net cash, extra carry and legal \$1.50 million, and the remainder is discounting over the additional 1.75 years.

**Decision consequence.** The same loan is worth about 25 points of collateral value less in a slow judicial jurisdiction under these assumptions. That difference must be in the bid. In a non-judicial state the timeline risk moves from the court to the borrower's ability to delay: a temporary restraining order, a lender-liability suit, or a bankruptcy filing that stays the sale. In Texas, the borrower's bankruptcy lawyer is the timeline. Model that probability explicitly, as Example 12.3 and Case G do, rather than treating the statutory minimum as the expected time.

### Example 12.5 — Special servicing: appraisal reduction, advances, and control

**Given.** A \$50.0 million CMBS loan, 5.0% coupon, transferred to special servicing. Accrued unpaid interest \$1.5 million. Unreimbursed advances for taxes and insurance \$0.6 million. Reserves held by the servicer \$0.4 million. A new appraisal values the property at \$38.0 million. The controlling class (the B-piece) has an original and current balance of \$40.0 million. Haircut 10%. Assume the deal tests control after deducting ARAs, with a 25% threshold [HYPOTHESIS; deal-specific]. Fees, also [HYPOTHESIS] for illustration: special servicing fee 0.25% per year on the loan balance, workout fee 1.0% of collections on a modified loan, liquidation fee 1.0% of liquidation proceeds.

**Find.** (a) The ARA, the reduced monthly interest advance, and the B-piece's balance for control purposes. (b) The same if the appraisal is \$24.0 million. (c) The servicer's fees under a three-year modification (one year in special servicing, then collections of principal plus three years of interest) versus liquidation after 18 months for \$30.0 million.

**Solution.**

(a) Claim $= 50.0 + 1.5 + 0.6 = \$52.1$ million. Haircut value plus reserves $= 0.9 \times 38.0 + 0.4 = \$34.6$ million.
$ARA = 52.1 - 34.6 = \$17.5$ million.
Full monthly interest advance $= 50{,}000{,}000 \times 0.05/12 = \$208{,}333$. Reduced advance $= 208{,}333 \times (1 - 17.5/50.0) = 208{,}333 \times 0.65 = \$135{,}417$.
B-piece for control: $40.0 - 17.5 = \$22.5$ million, 56.25% of original. Control does not shift.

(b) Haircut value plus reserves $= 0.9 \times 24.0 + 0.4 = \$22.0$ million. $ARA = 52.1 - 22.0 = \$30.1$ million. B-piece for control: $40.0 - 30.1 = \$9.9$ million, **24.75%** of original. Below 25%: control shifts to the next class.

(c) Modification: $0.0025 \times 50{,}000{,}000 \times 1 + 0.01 \times (50{,}000{,}000 + 3 \times 0.05 \times 50{,}000{,}000) = 125{,}000 + 575{,}000 = \$700{,}000$. Liquidation: $0.0025 \times 50{,}000{,}000 \times 1.5 + 0.01 \times 30{,}000{,}000 = 187{,}500 + 300{,}000 = \$487{,}500$.

**Check.** The advance reduction is proportional: $135{,}417/208{,}333 = 0.65 = 1 - ARA/B$. ✓

**Decision consequence.** Three conflicts follow from the arithmetic. (1) The B-piece holder, who often controls the special servicer, prefers *later and higher* appraisals: a lower appraisal costs it interest and, near the threshold, control. (2) The special servicer earns more under modification (\$700,000) than under liquidation (\$487,500) in this fee structure, whether or not modification maximizes the trust's recovery. (3) Senior bondholders, who are protected by subordination, prefer speed. A buyer of a loan or REO from a CMBS trust is negotiating with an agent whose incentives are written in the pooling and servicing agreement. Read it. Ask who controls, how close the controlling class is to a control shift, and when the next appraisal is due. Those facts predict whether the servicer will sell, extend, or wait.

### Example 12.6 — A bank at the concentration screens

**Given.** A community bank with total risk-based capital of \$250 million; CLD loans \$280 million; total non-owner-occupied CRE loans (including CLD) \$820 million, which were \$520 million 36 months ago. CRE loans can be sold at 88% of carrying value.

**Find.** (a) Whether the bank meets either screen. (b) The par amount of CRE loans it must sell to bring CRE/capital to 300%, with no tax effect and with a 21% tax rate. (c) The same at a 60% sale price.

**Solution.**

(a) CLD ratio $= 280/250 = 112\% \ge 100\%$: screen 1 met. CRE ratio $= 820/250 = 328\% \ge 300\%$; growth $= 820/520 - 1 = 57.7\% \ge 50\%$: screen 2 met.

(b) The naive answer is $820 - 3 \times 250 = \$70$ million. But each dollar sold at 88 books a 12-cent loss. With no tax:
$$X = \frac{820 - 750}{1 - 3(0.12)} = \frac{70}{0.64} = \$109.375 \text{ million}.$$
Loss $= 0.12 \times 109.375 = \$13.125$ million. Capital after $= \$236.875$ million. CRE after $= \$710.625$ million $= 3.00 \times 236.875$. ✓
With a 21% tax benefit on the loss: $X = 70/(1 - 3 \times 0.12 \times 0.79) = 70/0.7156 = \$97.82$ million; after-tax loss \$9.27 million.

(c) At 60%: the denominator is $1 - 3 \times 0.40 = -0.20 < 0$. No amount of selling reaches 300%. The bank must raise capital, shrink other assets, or accept supervisory scrutiny while it works the loans out.

**Decision consequence.** The bank's need to sell is real, but it is not unlimited. The bank will sell its best-priced loans first, because those sales hurt capital least, and it will hold the deepest-discount loans, because selling them is self-defeating. A loan buyer should therefore expect the bank's offered pool to be adversely selected toward loans the bank can sell near par, and should expect the truly distressed loans to come out later, after capital is raised or losses are absorbed through earnings. A bank that sells at 88 is a liquidity seller. A bank that would have to sell at 60 is not a seller at all. The concentration screens are not limits, so "the regulators will force them to sell" is a hypothesis to verify, not a fact.

### Example 12.7 — What the REIT price implies (Opportunity C)

**Given.** Share price \$42.00; 100 million shares; debt \$3.2 billion; preferred \$0.3 billion; cash \$0.1 billion; other non-real-estate assets (land held for development, at estimated value) \$0.2 billion; forward cash NOI \$480 million. Your private-market cap rate for the portfolio: 5.50%.

**Find.** The implied cap rate, NAV per share, the discount, and the leverage of NAV to gross asset value.

**Solution.**
Market cap $= 42 \times 100\text{m} = \$4.2$ billion. Implied real estate value $= 4.2 + 3.2 + 0.3 - 0.1 - 0.2 = \$7.4$ billion. Implied cap $= 480/7{,}400 = 6.49\%$.
GAV at 5.50% $= 480/0.055 = \$8.727$ billion. NAV $= 8.727 - 3.2 - 0.3 + 0.1 + 0.2 = \$5.527$ billion $= \$55.27$ per share. Discount $= 42.00/55.27 - 1 = -24.0\%$.
$GAV/NAV = 8.727/5.527 = 1.58$.

**Check.** The implied cap rate is the private cap rate at which NAV equals the share price. At 6.49%, GAV $= \$7.4$ billion and NAV $= 7.4 - 3.2 - 0.3 + 0.1 + 0.2 = \$4.2$ billion $= \$42$ per share. ✓

**Decision consequence.** The "24% discount" is the same statement as "the public market capitalizes this NOI at 6.49%, not 5.50%". It is a disagreement of 99 bp about the cap rate, magnified 1.58 times by leverage. Before calling it an opportunity, ask which number is stale. If private transactions in the REIT's markets are clearing near 6.5%, the appraisal-based 5.50% is the stale number and there is no discount. If private trades are clearing near 5.5% and the REIT is being sold for reasons unrelated to its assets (index deletion, fund redemptions, a management problem), the discount is real, but capturing it requires a catalyst: buybacks funded by asset sales at private prices, a take-private, or activist pressure. Without a catalyst, the discount can persist or widen.

### Example 12.8 — The basis reset

**Given.** Two identical 400,000 sf office buildings across the street from each other. Operating expenses \$4.8 million per year (\$12/sf, fixed). Recurring leasing capital (TI and commissions, averaged) \$1.6 million per year (\$4/sf). Stabilized occupancy 88%. Owner 1 bought at \$140 million (\$350/sf) and needs a 7.0% yield on basis. Owner 2 bought the other building out of foreclosure at \$60 million and spent \$10 million on capital, a \$70 million basis, and needs 9.0%. Market gross rent is \$40.00/sf.

**Find.** Each owner's required gross rent; the yield each earns at the market rent.

**Solution.** Occupied area $= 400{,}000 \times 0.88 = 352{,}000$ sf.
Owner 1: $R_{req} = (0.07 \times 140{,}000{,}000 + 4{,}800{,}000 + 1{,}600{,}000)/352{,}000 = 16{,}200{,}000/352{,}000 = \$46.02$/sf.
Owner 2: $R_{req} = (0.09 \times 70{,}000{,}000 + 6{,}400{,}000)/352{,}000 = 12{,}700{,}000/352{,}000 = \$36.08$/sf.
At \$40.00: NOI after leasing capital $= 40 \times 352{,}000 - 6{,}400{,}000 = \$7{,}680{,}000$. Owner 1 yield $= 7.68/140 = 5.49\%$. Owner 2 yield $= 7.68/70 = 10.97\%$.

**Check.** The rent gap $46.02 - 36.08 = \$9.94$/sf equals $(9.8 - 6.3)\text{m}/352{,}000$. ✓

**Decision consequence.** Owner 2 can lease at \$36, \$4 below market and \$10 below what Owner 1 needs, and still earn 9%. If Owner 2 does so to fill the building quickly, the market rent falls and Owner 1's building, already short of its required return, loses tenants at renewal. This is how distress propagates through a submarket: each foreclosure resets one basis, which lowers rents for every incumbent, which pushes the next owner toward default. For a buyer, the lesson has two edges. A low basis is a competitive weapon. But the next buyer, one foreclosure later, may have an even lower basis. **Your basis is cheap only relative to the bases of the buildings you compete with.** Map the capital structures of the competitive set, not only their rents.

---

## 12.6 CRE application: reading a distressed market

The examples supply a sequence of questions for any distressed situation.

1. **Where is the market in the stock-flow cycle?** Measure under-construction and recently started space as a percentage of stock and compare it with absorption over the construction lag (Example 12.1). A market whose pipeline exceeds two to three years of absorption has not reached its vacancy peak, however bad today's vacancy looks.
2. **Is the demand loss cyclical or structural?** For office, compare leasing per employee and the space tenants take at renewal with what they gave up. Sublease space is a leading indicator of future direct vacancy. A recession explains falling absorption. It does not explain tenants that renew at 60% of their previous footprint with employment unchanged.
3. **Which owners face maturities, and are they in liquidity or solvency trouble?** Build the maturity schedule for the competitive set. For each loan, compute the refinance gap at current terms (Example 12.2). Liquidity-problem owners recapitalize. Solvency-problem owners hand the asset to their lender, slowly.
4. **Who holds the loans, and what are their constraints?** Bank balance-sheet loans (Example 12.6), CMBS loans controlled by special servicers (Example 12.5), debt funds with their own lenders, and life companies all behave differently. The holder decides whether loans come to market, when, and at what price.
5. **What is the fastest legal route to the collateral, and what does delay cost?** Jurisdiction, loan documents, guaranties, and the borrower's incentives (Example 12.4).
6. **What does the public market say?** Compare implied cap rates on REITs with private appraisal-based cap rates (Example 12.7). A persistent gap is evidence about where private prices will clear.
7. **What basis will your competitors have?** (Example 12.8.) The cheapest building in the market sets the rent floor.
8. **What is your edge?** Speed and certainty of closing (liquidity provision), legal and workout capability (process skill), or a better forecast of demand (information). Name it. If none applies, you are a price-taker in a market where sellers know more than you.

### Buying through downturns: what the vintage-year evidence does and does not show

The standard argument is that funds that invest in the years after a downturn earn higher returns than funds that invest at the peak. The evidence available to this book is limited and secondary. An industry report in 2014, citing Preqin data as of September 2014, said that closed-end real estate funds of vintages 2009–2012 were posting median IRRs between 12.8% (vintage 2012) and 15.8% (vintage 2009), and that 2005 and 2006 vintages had not recovered to the same degree [FACT as a report of Preqin data; industry press, class C; VERIFIED-SECONDARY; see `references/sources_ch12.md`]. INREV's global IRR index for non-listed, closed-end funds reports its 2005–2007 vintage group as the weakest [FACT as reported in a search summary of the INREV snapshot; figures not quoted here *(verification pending)*].

What this does **not** establish:

* **Interim IRRs are not realized returns.** A 2014 snapshot of 2009–2012 vintages is mostly unrealized and depends on appraisals made during a recovery.
* **Survivorship and selection.** Managers who raised funds in 2009–2011 were the ones who could. They are not a random sample.
* **Timing within the downturn.** "Vintage 2009" includes funds that bought in early 2009 and funds that bought in 2011. The evidence does not tell you whether to buy at the first signs of distress or wait for the second wave.
* **Reference class.** The 2009–2012 recovery was supported by falling interest rates. A downturn driven by rising rates, or by structural demand loss, is a different reference class.

The defensible conclusion is narrow [INFERENCE]: capital that was available and patient after 2009 was paid for providing liquidity when others could not. That supports keeping dry powder and the ability to act. It does not support any specific entry date, and it says nothing about property types whose demand has changed.

---

## 12.7 When the relationships fail

1. **The stock-flow model has no rent floor.** In Example 12.1 rents in late years fall toward levels below operating cost. Real owners stop cutting rent when it no longer covers the marginal cost of occupying space, and they mothball, convert, or demolish. Obsolete stock leaves the market. That is the mechanism by which structural demand loss is eventually absorbed, and it is slow.
2. **Structural loss masquerades as cyclical.** A model calibrated on past office cycles assumes demand recovers with employment. If use per worker falls permanently, the "trough" vacancy is a new equilibrium for old stock. Case E is built to make you price that possibility explicitly.
3. **Extend-and-pretend changes the timeline.** Lenders may modify and extend loans rather than foreclose. In 2009 the federal banking agencies issued a policy statement on prudent CRE loan workouts, which said that loans to borrowers able to repay on reasonable terms would not be adversely classified merely because collateral value had fallen below the loan balance. It was replaced in June 2023 by an interagency statement on CRE loan accommodations and workouts [FACT; FDIC FIL-61-2009 and FIL-34-2023 / OCC Bulletin 2023-23; VERIFIED-SECONDARY]. Whatever the merits, accommodation delays the arrival of distressed supply. A buyer who waits for "the wave of foreclosures" may wait years.
4. **Credit bids and auction dynamics.** At a foreclosure sale the lender can credit-bid its debt. Third parties rarely outbid a credit bid when the debt exceeds value, so foreclosure auctions are a poor place to buy. The REO sale after foreclosure is the market (Case G).
5. **REIT discounts can be about the REIT, not the real estate.** Leverage, management, dividend policy, and fund flows move REIT prices. The implied cap rate is a signal about private values only after those are accounted for.
6. **Basis resets can reverse.** If the market recovers quickly, the low-basis buyer has no reason to undercut rents, and the incumbent's position improves. The basis-reset spiral requires excess vacancy.
7. **The legal timeline is the borrower's choice.** Statutory minimums (21 days in Texas) are not expected timelines. Bankruptcy, lender-liability litigation, and title disputes are probability-weighted outcomes, not tails to ignore.

---

## 12.8 Historical episode: the RTC era (1989–1995) and the institutionalization of distressed CRE

**Date and environment.** The savings and loan crisis of the 1980s left the federal deposit insurance fund for thrifts insolvent and many failed thrifts holding large portfolios of commercial real estate loans and foreclosed property. Congress responded with the Financial Institutions Reform, Recovery, and Enforcement Act (FIRREA) in August 1989, which created the Resolution Trust Corporation (RTC) to resolve failed thrifts and dispose of their assets [FACT; CRS Report RS22959, *The Resolution Trust Corporation: Historical Analysis*, 2008; VERIFIED-SECONDARY]. Texas and the Southwest were at the center of the real estate losses; the regional detail (energy-price collapse, overbuilding, and tax-law changes in 1986) is widely discussed but its quantitative attribution is *(verification pending)* and is not used here.

**Scale.** By mid-1995, the RTC had resolved 747 thrifts with total assets of \$394 billion [FACT; Curry and Shibut (2000), *FDIC Banking Review* 13(2), as reported in search excerpts; VERIFIED-SECONDARY]. The RTC shut down in 1995 [FACT; CRS RS22959; Texas A&M Real Estate Center]. CRS reports that the RTC eventually obtained \$105 billion of funding and that estimates of the total government cost of the crisis are about \$150 billion, with estimates varying [FACT; CRS RS22959; VERIFIED-SECONDARY]. Curry and Shibut's own final cost and taxpayer-share figures are *(verification pending)* in this edition and are not quoted.

**What was knowable at the time.** That the government held an enormous inventory of real estate and loans, and that it had to sell, was public. What was not knowable was the clearing price. The private market had little capital for CRE, banks were themselves under pressure, and appraisals were unreliable in a market with few trades.

**Participants and incentives.**

* *The RTC* wanted speed, maximum recovery, and political defensibility, goals that conflict. Asset-by-asset sales were slow and the inventory was too large for retail disposition.
* *Private buyers* — the opportunity funds that became the template for today's opportunistic real estate funds — offered liquidity in exchange for large discounts and needed scale and speed.
* *Securitization* became one of the RTC's disposition tools. Facing billions of dollars of commercial mortgages, the RTC placed many in pools backing bonds — commercial mortgage-backed securities — and the 1992–1995 period established the underwriting standards, rating criteria, and standardized structures on which the private CMBS market was built [FACT; Texas A&M Real Estate Center; Chandan (2012), *Wharton Real Estate Review*; VERIFIED-SECONDARY].

**Alternative interpretations.** One reading is that the RTC sold too cheaply, transferring wealth to opportunity funds. Another is that the discount was the competitive price of immediacy and information in a market without other buyers, and that holding the assets longer would have cost more in carry and deterioration (Example 12.4's arithmetic at national scale). A third emphasizes the institutional legacy: by creating the CMBS market and the opportunity-fund model, the RTC changed who holds CRE risk in the next downturn. These readings are not exclusive, and this book does not adjudicate them with numbers it has not verified.

**A second episode for contrast: 2008–2013.** In the later crisis the FDIC resolved nearly 500 failed banks [FACT; FDIC podcast transcript on the crisis, *Crisis and Response* series; VERIFIED-SECONDARY; exact count *(verification pending)*]. An FDIC staff study finds that the FDIC resolved more than three times as many banks in the 1980–1994 crisis as in 2008–2013, but that total failed-bank assets were larger in 2008–2013 [FACT; FDIC staff study 2020; VERIFIED-SECONDARY]. Regulators had issued the 2006 concentration guidance before the crisis; a Federal Reserve analysis reports that 31% of commercial banks in 2006 exceeded at least one of the concentration levels [FACT; Federal Reserve, 2013 analysis of the CRE concentration guidance; VERIFIED-SECONDARY]. In October 2009 the agencies issued the workout policy statement discussed in §12.7, and a large share of distressed CRE was modified and extended rather than sold. The CMBS special-servicing machinery that the RTC era had made possible was tested at scale.

**What the episodes do and do not establish.**

* They establish that when the holders of distressed CRE are forced and large, disposition channels are invented (bulk sales, joint ventures, securitization), and that those channels shape the market for decades [INFERENCE from the CMBS history above].
* They establish that regulatory posture changes the timing of distress: forced disposition in the RTC era, accommodation and extension after 2009 [INFERENCE].
* They do **not** establish the returns earned by RTC-era buyers. This book has not verified those figures.
* They do **not** establish that the next downturn will offer RTC-style discounts. Distressed supply depends on who holds the loans, on their capital, and on regulatory forbearance, and all three differ across episodes.

**CRE connection.** In each episode, the decisive variable for a buyer was not the size of the losses but the identity, capital, and incentives of the holder of the loans. Examples 12.5 and 12.6 give you the arithmetic for two kinds of holder.

---

## 12.9 Frequent analytical errors

1. **Using replacement cost or unpaid principal as a value.** Both are reference points. Value is the present value of what the claim will pay.
2. **Averaging scenario IRRs for a loan purchase.** Fast, small wins dominate the average. Report the IRR of expected cash flows and the distribution (Example 12.3).
3. **Treating the statutory foreclosure minimum as the expected timeline.** Model delay by probability: contested foreclosure, bankruptcy, injunctions.
4. **Ignoring value drift during the workout.** A neglected asset loses value while the lawyers work. Carry is not only taxes and insurance.
5. **Calling a rate-reset problem a solvency problem, or the reverse.** Compute the refinance gap *and* the equity value net of selling costs before choosing whom to negotiate with.
6. **Assuming banks "must" sell.** The 2006 screens are not limits. Sale losses reduce capital, which can make selling self-defeating (Example 12.6).
7. **Reading a REIT discount as a private bargain without asking which price is stale.**
8. **Forgetting that your low basis is someone else's rent ceiling and the next buyer's target.**
9. **Watching vacancy instead of the pipeline.** Vacancy is low at exactly the moment the cycle's damage has been committed (Example 12.1).
10. **Using vintage-year averages as an entry signal.** The evidence is interim, selected, and from a falling-rate recovery.

---

## 12.10 Decision exercise: allocate the downturn capital

Return to §12.1. You may commit up to \$60 million in the next 90 days.

1. **Opportunity A (the NPL).** Using Example 12.3, state your bid and the probability of contested resolution at which you would withdraw. List the three pieces of diligence that would most change your probabilities, and what you would pay for each.
2. **Opportunity B (the office tower).** Using Case E, state whether you would bid, at what price, and what fact would make you walk away. Explain why the discount to replacement cost is not evidence of value.
3. **Opportunity C (the REIT).** State whether the 24% discount is a disagreement about cap rates, a statement about the REIT, or both. Name the catalyst you would need to own it, and the size you would hold without one.
4. **What you will not do.** Waiting is a legitimate answer for each opportunity. If you wait, state the trigger that brings you back: a price, a data release, or an event such as a maturity or a bank capital raise.
5. **Sizing.** Total exposure to one metro's office market across A, B, and C. State the downside if demand loss is structural.

**Rubric (see `problems/solutions/ch12_solutions.md` §Decision exercise).**

| Element | Full credit (4) | Partial (2) | None (0) |
|---|---|---|---|
| NPL bid | Bid below max PV at stated required return; identifies the borrower's position as the key unknown; computes the effect of a higher contested probability | Bid with a return target but no scenario sensitivity | Bids on % of UPB alone |
| Office tower | Prices off lease-up, TI/LC, capex, and carry; rejects replacement cost as support; names a structural-demand test and a walk-away price | Recognizes leasing costs qualitatively | "Fifth of replacement cost" as the thesis |
| REIT | Converts the discount into an implied cap rate; asks which price is stale; requires a catalyst or sizes small | Computes discount only | Buys "because of the discount" |
| Correlation | Recognizes that A, B, and C are all short the same office-demand risk; sizes jointly | Mentions correlation | Treats them as diversifying |
| Abstention | States what is declined and the re-entry trigger | Partial | Absent |

---

## 12.11 Connections to other chapters

* Chapter 1: price of immediacy, liquidity provision, scenario EV, and why mean IRR differs from IRR of expected flows.
* Chapter 3: forced selling and reflexivity; the bank-sale feedback loop of Example 12.6 is a balance-sheet version.
* Chapter 8: absorption, operating leverage, and reassessment; Case E's tax line.
* Chapter 9: cap rates, DCF valuation, and why replacement cost is not a floor.
* Chapter 10: loan sizing, refinance gaps, and capital stacks used throughout §12.4.2.
* Chapter 13: hold/sell decisions and real options, including the option to convert.
* Chapter 17: credit, recovery rates, and CMBS tranching in depth.
* Chapter 23: the 1980s–1990s Texas and RTC cycle and the post-2020 office cycle as historical cases.
* Case B (refinancing cliff), Case E (distressed office), Case G (buying the debt), Case J (credit-crunch hotel acquisition).

---

## 12.12 One-page reference sheet

**First questions.** Liquidity or solvency? Who holds the loan, and what constrains them? What is the fastest legal route to the collateral, and what does delay cost? What basis will competitors have? What is my edge?

| Item | Formula |
|---|---|
| Stock-flow | $S_t = S_{t-1}(1-\delta) + N_{t-L}$; $v_t = 1 - \min(D_t,S_t)/S_t$ |
| Rent adjustment | $R_t = R_{t-1}[1 + \alpha(v^* - v_t)]$ |
| Starts | $N_t = \kappa\max(0, R_t/R^F - 1)S_t$ |
| Coverage after a reset | $DSCR_1/DSCR_0 = r_0/K_1$ (IO to amortizing, same balance) |
| Max loan | $\min(\lambda V,\ NOI/(DSCR\cdot K),\ NOI/DY)$ |
| Refinance gap | $B + \text{costs} - L_{\max}$ |
| NPL max price | $\sum p_s (X_s - c_s)/(1+k)^{\tau_s}$ |
| Foreclosure PV | $[V_0(1+d)^T(1-s) - \text{carry}\cdot T - \text{legal}]/(1+k)^T$ |
| Texas sale | First Tuesday of a month, 10 a.m.–4 p.m., notice $\ge 21$ days before (Tex. Prop. Code §51.002) |
| ARA (generic) | $\max(0, B + I + A + O - [0.9V_{appr} + \text{reserves}])$ |
| Reduced advance | $\text{advance} \times (1 - ARA/B)$ |
| Concentration screens | CLD $\ge 100\%$ of total RBC; or CRE $\ge 300\%$ and 36-month growth $\ge 50\%$ |
| Loan sales to target $m$ | $X = (C - mK)/[1 - m(1-p)(1-\tau)]$ |
| REIT implied cap | $NOI_{fwd}/(\text{Mkt cap} + \text{Debt} + \text{Pref} - \text{Cash} - \text{Other})$ |
| NAV leverage | $\%\Delta NAV \approx (GAV/NAV)\,\%\Delta GAV$ |
| Required rent | $(yP + E + LC)/(A\,o)$ |

**Rules of thumb (to be tested, not trusted).** A three-year lag can double peak vacancy relative to a one-year lag in the simple model. An IO-to-amortizing reset from 3.6% to 6.25% halves coverage. At 3x leverage to capital, a bank cannot sell its way below 300% at prices under 67 cents.

---

## References for this chapter

All sources, with verification status, are listed in `references/sources_ch12.md`.

* DiPasquale, D., and Wheaton, W. C. (1992). "The Markets for Real Estate Assets and Space: A Conceptual Framework." *Real Estate Economics* (formerly *AREUEA Journal*), 20(2), 181–197.
* Wheaton, W. C. (1999). "Real Estate 'Cycles': Some Fundamentals." *Real Estate Economics*, 27(2), 209–230.
* Office of the Comptroller of the Currency (2006). Bulletin 2006-46, "Concentrations in Commercial Real Estate Lending, Sound Risk Management Practices"; interagency guidance at 71 FR 74580 (12 December 2006).
* Federal Reserve Board (2013). "An Analysis of the Impact of the Commercial Real Estate Concentration Guidance."
* FDIC (2009). FIL-61-2009, "Policy Statement on Prudent Commercial Real Estate Loan Workouts" (30 October 2009); OCC Bulletin 2023-23 and FDIC FIL-34-2023, "Policy Statement on Prudent Commercial Real Estate Loan Accommodations and Workouts" (29 June 2023).
* Texas Property Code §51.002.
* 11 U.S.C. §362(d)(3) (single asset real estate).
* Curry, T., and Shibut, L. (2000). "The Cost of the Savings and Loan Crisis: Truth and Consequences." *FDIC Banking Review*, 13(2).
* Congressional Research Service (2008). *The Resolution Trust Corporation: Historical Analysis*, RS22959.
* Chandan, S. (2012). *Wharton Real Estate Review*, Spring 2012 (on the RTC origins of CMBS).
* Texas A&M Real Estate Center, article on the origins of CMBS (RTC securitization).
* FDIC (2017). *Crisis and Response: An FDIC History, 2008–2013*; FDIC staff studies (2020).
* CRE Finance Council (2026). "Spotlight on Servicing: Understanding CMBS Appraisal Reductions"; DBRS Morningstar commentary on appraised values and ARAs.
