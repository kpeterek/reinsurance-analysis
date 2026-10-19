# Chapter 13 — CRE Trading and Portfolio Strategy

> **Status:** Complete (v1.0). All ten worked examples are reproduced in `tests/test_ch13_examples.py`, together with every number in `problems/questions/ch13_problems.md` and `problems/solutions/ch13_solutions.md`. The real-option helper is `models/python/sdesk/x_options_real.py`. Drills D121–D130 are in `training/daily_drills/drill_bank_ch13.json`. Sources are listed in `references/sources_ch13.md`. Three items are marked *(verification pending)*: the transaction cap rate and the scope of one 10-K figure in the historical episode (§13.9), and fund-vintage return data (§13.8), which the chapter deliberately does not quote. None is used in a calculation.

## Learning objectives

After this chapter you should be able to:

1. Run a hold–sell–refinance analysis on **equity at market**. Convert today's bid into the equity you would actually take out after selling costs and debt prepayment, compute the forward IRR of holding that equity, and compare it with the IRR of the best reinvestment alternative at the same leverage and risk.
2. Compute the **marginal cost of a cash-out refinancing** and explain why replacing below-market debt can make the incremental dollar of debt the most expensive capital in the structure.
3. Measure geographic concentration using NOI or value correlations. Compute portfolio volatility and each asset's contribution to risk, and show why diversification shrinks when correlations rise in a stress.
4. Read cap-rate spreads across sectors as statements about required returns and expected growth, $c = k - g$, and say which of the two a spread trade is betting on.
5. Hedge the interest-rate exposure of an acquisition pipeline with Treasury futures, swaps, or caps. Size the hedge by DV01 and quantify basis risk and the risk that a deal fails to close.
6. Size a liquidity reserve to survive a specified stress, including debt maturities, and state its opportunity cost.
7. Allocate a fixed amount of portfolio debt across assets with different volatilities, and distinguish portfolio-level leverage from asset-level default risk.
8. Value the option to wait or to develop with a binomial tree. Explain why uncertainty raises the value of waiting, why the option holder forgoes the asset's cash yield, and when doing nothing is the investment decision with the highest value.

---

## 13.1 Opening investment problem: the partnership's Tuesday agenda

You are the CIO of a Texas family partnership. All facts are [HYPOTHESIS], a constructed teaching case. The partnership owns:

| Asset | Market value (bid) | Forward NOI | Debt | Debt terms |
|---|---:|---:|---:|---|
| 280-unit garden multifamily, Austin suburbs | \$44.0m | \$2.20m | \$24.0m | Fixed 4.25%, interest-only, 5 years left, yield maintenance |
| 210,000 sf flex industrial, Houston | \$28.8m | \$1.80m | \$15.0m | Fixed 6.00%, interest-only |
| 150-room select-service hotel, San Antonio | \$30.0m | \$2.40m (after 4% FF&E reserve) | \$22.0m | Floating, capped; all-in 7.5%; **matures in 24 months** |
| 12-acre suburban land parcel | see Case I | none | none | |

Gross value is \$102.8m, debt \$61.0m, and equity at gross market value \$41.8m. In addition, the partnership has two Dallas industrial acquisitions under contract. They close in four months and will need \$60m of 10-year fixed-rate debt, priced at the 10-year Treasury yield plus 175 bp.

The agenda for Tuesday's meeting has six items:

1. A broker has delivered a \$44.0m bid for the multifamily asset, a 5.00% cap on forward NOI. The acquisitions officer wants to sell and redeploy the equity into industrial at a 6.25% cap: "We'd be trading a 5% yield for a 6¼% yield."
2. A lender has offered a cash-out refinancing of the multifamily instead.
3. All three operating assets are in Texas. One director asks how concentrated the portfolio is.
4. Hotel cap rates sit 325 bp above multifamily cap rates. Is the hotel sector "cheap"?
5. Should the pipeline's interest-rate exposure be hedged before the loans lock?
6. How much cash should be held back, and should the land be developed now?

By the end of the chapter you will be able to answer each item with a number and a stated assumption. Section 13.10 returns to the agenda as a decision exercise.

---

## 13.2 Economic intuition

### Every hold is a purchase

The owner of an asset is, every day, implicitly buying it again at the price they could sell it for. Holding is economically the same as selling and buying back, except that holding saves the round-trip transaction costs and keeps the existing financing. The relevant capital is therefore not what you paid. It is what you could take out today: **equity at market**. The relevant return is not the IRR since inception. It is the forward IRR on equity at market. A building bought for \$33m that is now worth \$44m has an excellent historical IRR and possibly a poor forward one. The historical IRR is sunk. It belongs in the performance report, not in the decision.

### Capital recycling is a relative-value trade, not a yield trade

"Selling at a 5% cap and buying at a 6¼% cap" sounds accretive. It is only accretive if the 6¼% asset is not 1¼ points riskier or 1¼ points slower-growing. In a constant-growth world the cap rate is $c = k - g$. A higher cap rate can mean a higher required return (more risk), lower expected growth, or a mispricing. Only the third is a gain. Capital recycling earns money when the seller's asset is priced for more growth than it will deliver, or the buyer's asset for less. It loses money in every other case, and it always costs two sets of transaction costs.

### Correlation is the price of concentration

Owning three Texas assets in three property types looks diversified by sector. Their NOIs share a state economy, an energy cycle, a property-tax regime, an insurance market, and a population-growth story. Portfolio risk is governed by the correlations, and those correlations are highest exactly when diversification is needed most. A diversification benefit measured in calm years is an upper bound on the benefit you will have in a crisis.

### Market selection is a forecast with a holding period

Choosing markets means choosing a bundle of exposures: population and job growth, supply elasticity, the property-tax and insurance regime, the local lender base, and the depth of the buyer pool when you want to sell. A useful discipline is to write each market thesis as three numbers and one condition: expected NOI growth, the cap rate you expect to exit at, the correlation of the market's NOI with the rest of the portfolio, and the observable event that would make you leave. Supply elasticity deserves particular attention. In markets where land is plentiful and entitlement is fast, which describes much of Texas, strong demand produces new supply quickly, and rent growth is competed away sooner than in supply-constrained markets [HYPOTHESIS as a general statement; test it against permit and delivery data for the specific submarket, Chapter 8]. Strong demand growth and strong investment returns are therefore not the same thing. Section 13.9 shows a large REIT revising its market selection within six years.

### Opportunity cost is the only benchmark

Every number in this chapter is compared with something. The hold is compared with the best reinvestment at equal risk. The reserve is compared with the target equity return. The refinancing is compared with the cost of other capital. Waiting is compared with building now. The most common error in portfolio strategy is to evaluate an action against zero, or against the investor's own past returns, instead of against the next-best use of the same capital at the same risk. Case F makes this comparison explicit for a hotel against Treasuries after tax.

### Hedging transfers one risk and creates another

A Treasury-futures hedge on an acquisition pipeline removes exposure to the Treasury yield. It does not remove exposure to the lender's spread, and it creates new exposures: basis risk between Treasury and loan pricing, margin calls, and a naked position if the deal fails to close. The question is never "hedged or unhedged". It is "which risk do I want, and which risk am I left with?"

### Cash has a strategic value that its yield understates

A liquidity reserve earns the T-bill rate. Measured against a 10–12% target return it looks like a drag. Measured against the alternative of selling an asset in a stressed market, or handing it to a lender at a maturity, it is cheap insurance. The reserve also buys optionality: the ability to act when others are forced to sell. Chapter 1 called this being a liquidity provider. You can only provide liquidity if you have it.

### Waiting is an asset

A land parcel, an unexercised right to develop, or uncommitted capital is an option. Exercising it, by building or buying, kills the option. Exercise is optimal only when the value captured today exceeds the value of keeping the choice open. Conventional NPV analysis compares "build now" with "never build". The relevant comparison is "build now" with "decide later". When uncertainty is high and the cost of delay is low, waiting can dominate an investment with a positive NPV. This is not an argument for paralysis. It is a valuation that tells you precisely what delay costs and what it buys.

---

## 13.3 Technical definitions

| Term | Definition |
|---|---|
| Equity at market, $E_M$ | Today's net sale proceeds after selling costs, debt repayment, and prepayment costs: $E_M = V(1-s) - B - PP$ |
| IRR on equity at market | The forward IRR of holding, using $-E_M$ as the time-0 flow. It is the return earned by not selling |
| Reinvestment alternative | The best available use of $E_M$ at comparable leverage and risk, net of acquisition costs |
| Break-even exit cap | The exit cap rate at which the hold IRR equals the alternative's IRR |
| Marginal cost of a refinancing | The IRR of the incremental flows: net cash received today against the incremental debt service and the incremental balance repaid |
| Yield maintenance (simplified) | PV, at the Treasury rate, of the coupon above the Treasury rate over the remaining term |
| Capital recycling | Selling assets and redeploying the proceeds into other assets, debt reduction, or distributions |
| Risk contribution | $RC_i = w_i (\Sigma w)_i / \sigma_p$. The contributions sum to $\sigma_p$; $RC_i/\sigma_p$ is asset $i$'s share of risk |
| Diversification ratio | $\sum_i w_i \sigma_i / \sigma_p \geq 1$ |
| Cap-rate spread | The difference between two sectors' cap rates, or between a cap rate and a Treasury yield, in bp |
| DV01 | The dollar change in value for a 1 bp change in yield (positive number) |
| Basis risk | Risk that the hedge instrument and the exposure move by different amounts |
| Liquidity reserve | Cash or committed, unconditional capacity held to cover shortfalls and maturities in a defined stress |
| Real option | The right, but not the obligation, to take an action (build, expand, wait, abandon) at a cost |
| Risk-neutral probability $q$ | The probability that prices the underlying correctly when every claim is discounted at the risk-free rate |
| Cash yield $\delta$ | Income forgone by holding the option instead of the underlying asset; for a development option, the stabilized NOI yield |
| Value of waiting | Option value minus $\max(\text{NPV now}, 0)$ |

---

## 13.4 Equations and derivations

### 13.4.1 Equity at market and the hold IRR

Let $V_0$ be the bid, $s$ the selling-cost rate, $B_0$ the loan balance, and $PP$ the prepayment cost. Then

$$E_M = V_0(1-s) - B_0 - PP.$$

Holding for $T$ years produces cash flow after debt service $CF_t = NOI_t - DS_t$ and a reversion

$$R_T = \frac{NOI_{T+1}}{c_T}(1-s) - B_T.$$

The **hold IRR** solves $-E_M + \sum_{t=1}^{T} CF_t/(1+IRR)^t + R_T/(1+IRR)^T = 0$.

The alternative invests the same $E_M$. At loan-to-value $\lambda$ and buyer costs $b$, the purchase price it supports is

$$P = \frac{E_M}{1 + b - \lambda}.$$

**The decision rule.** Hold if $IRR_{hold} > IRR_{alt}$ at equal risk. If leverage or business risk differ, compare on a common basis: unlevered IRRs, or IRRs at the same LTV, before comparing levered results.

**Why prepayment belongs in $E_M$.** If the existing loan carries a below-market coupon, selling forces you to give up that loan and pay to retire it. Holding keeps it. A correct comparison charges the prepayment cost to the sale and credits the cheap coupon to the hold. Omit either and the comparison is biased.

### 13.4.2 Simplified yield maintenance

With coupon $r_L$, Treasury yield $y$ for the remaining term $n$, and balance $B$, using annual periods:

$$PP = B (r_L - y)\, a_{\overline{n}|y}, \qquad a_{\overline{n}|y} = \frac{1-(1+y)^{-n}}{y}.$$

Actual loan documents specify the discounting (often monthly, sometimes at Treasury flat, sometimes Treasury plus a spread) and a minimum penalty, often 1%. Use the document, not this formula, for a real transaction.

### 13.4.3 Marginal cost of a cash-out refinancing

An existing loan $B$ at rate $r_L$ is replaced by a new loan $L'$ at rate $r'$, both interest-only with $T$ years to maturity. Cash received today is $C_0 = L' - B - PP - \text{costs}$. The incremental flows to the borrower are

$$\Big[+C_0;\ -(L' r' - B r_L) \text{ for } t=1..T;\ -(L' - B) \text{ at } T\Big].$$

The marginal cost $m$ is the IRR of those flows from the lender's side. When $r' > r_L$, the borrower pays the higher rate on the *whole* new balance, not only on the cash released. A small cash-out on top of a large below-market loan can carry a marginal cost far above $r'$.

### 13.4.4 Portfolio volatility and risk contributions

With value weights $w$, volatilities $\sigma$, and correlation matrix $\rho$:

$$\sigma_p^2 = \sum_i \sum_j w_i w_j \sigma_i \sigma_j \rho_{ij}, \qquad RC_i = \frac{w_i \sum_j \rho_{ij}\sigma_i\sigma_j w_j}{\sigma_p}, \qquad \sum_i RC_i = \sigma_p.$$

The library function is `sdesk.risk.portfolio_volatility(weights, vols, corr)`. For two assets the expression reduces to $\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2 w_1 w_2 \rho \sigma_1 \sigma_2$. At $\rho = 1$, $\sigma_p = w_1\sigma_1 + w_2\sigma_2$, and there is no diversification.

**Equity volatility at the portfolio level.** If total debt $D$ is fixed in dollars, portfolio equity is $E = \sum V_i - D$ and

$$\sigma_E = \sigma_p \frac{\sum V_i}{E}.$$

How the debt is allocated among assets does not change $\sigma_E$. It changes which asset breaches a covenant or fails to refinance. Section 13.5, Example 13.7, quantifies this.

### 13.4.5 Cap rates, required returns, and implied growth

For a perpetuity growing at $g$, priced to return $k$, with NOI after reserves:

$$V_0 = \frac{NOI_1}{k-g} \;\Rightarrow\; c = k - g.$$

For two sectors A and B:

$$c_A - c_B = (k_A - k_B) - (g_A - g_B).$$

A spread is one equation in two unknowns: the risk-premium differential and the growth differential. A spread trade is a claim that the market has mis-set one of them. You must say which one.

**Convergence arithmetic.** If the spread narrows by $\Delta$ and the move happens entirely in sector A's cap rate, A's value changes by $c_A/(c_A - \Delta) - 1$. If it happens entirely in B's, B's value changes by $c_B/(c_B + \Delta) - 1$. A long-A, short-B view (or, in private real estate, overweight A and underweight B) pays in the first case. In the second it only avoids a loss.

### 13.4.6 DV01 hedge of an acquisition pipeline

A borrower who will lock a fixed-rate loan of principal $L$ in the future is exposed to the rate at lock. Each 1 bp increase in the locked rate costs approximately the PV of 1 bp per year on $L$ over the term:

$$DV01_{loan} \approx L \times 0.0001 \times a_{\overline{n}|r}.$$

A more precise version prices the loan as a bond with the actual payment frequency and takes the central difference, as `sdesk.fixed_income.dv01(ytm, coupon, years, face, freq)` does. The number of short futures contracts is

$$N = \frac{DV01_{loan}}{DV01_{fut}}, \qquad DV01_{fut} \approx \frac{DV01_{CTD}}{CF_{CTD}},$$

where CTD is the cheapest-to-deliver note and $CF$ its conversion factor. The CME 10-Year T-Note futures contract has a face value of \$100,000 [FACT; ch13-S07]. A futures DV01 must come from a live calculation. It moves with the level of yields and the identity of the CTD.

The locked loan rate is $y_{Tsy} + s$. The hedge offsets $\Delta y_{Tsy}$ but not $\Delta s$:

$$\text{Net P\&L} = -DV01_{loan}(\Delta y_{Tsy} + \Delta s) + N \cdot DV01_{fut} \cdot \Delta y_{Tsy}\quad(\text{changes in bp}).$$

When spreads widen as Treasuries rally, which is the usual pattern in a flight to quality, the hedged borrower loses on both lines.

**Swaps and caps for existing floating-rate debt.** The hotel loan in §13.1 floats. A **pay-fixed swap** converts it to fixed: the owner pays the swap rate and receives the floating index, so the all-in cost becomes swap rate plus the loan spread. The swap has no upfront premium, but it has a mark-to-market. If rates fall and the hotel is sold or refinanced early, breaking the swap costs roughly the swap's DV01 times the fall in rates. A **cap** is a strip of call options on the floating index. It costs an upfront premium and limits the index at the strike, while the owner keeps the benefit of falling rates. As a rough annualized cost, a hypothetical \$250,000 two-year cap on the \$22.0m hotel loan costs $250{,}000/22{,}000{,}000/2 = 0.57\%$, about 57 bp a year [HYPOTHESIS: cap premia depend on the strike, the term, and implied volatility; Chapter 18 prices them]. Lenders often require a cap on floating-rate loans, and the strike is set so the loan still meets a DSCR test at the strike rate (`cre.max_loan(..., dscr_rate=strike)`). The choice between the two is a choice of which risk to keep: the swap keeps prepayment and breakage risk, the cap keeps the cost of the premium and the rates between today's level and the strike.

### 13.4.7 Liquidity reserve

Over a stress horizon $t = 1..H$, let $X_t$ be the portfolio's net cash flow after debt service and committed capital spending. Let $M_t$ be the cash needed at any debt maturity in the period: the existing balance less the new loan available at stressed value and stressed underwriting. The reserve that keeps cumulative cash non-negative is

$$R^* = \max\Big(0,\ -\min_{\tau \le H} \sum_{t=1}^{\tau} (X_t - M_t)\Big).$$

Its annual opportunity cost is $R^*(k_E - r_f)$, where $k_E$ is the target equity return and $r_f$ the yield earned on the reserve.

### 13.4.8 The binomial real option

Let the value of the completed building be $V$. Over one period it moves to $uV$ or $dV$. An owner of the completed building also receives a cash yield $\delta V$ during the period. The holder of the option to build does not. Pricing by replication (see `sdesk/x_options_real.py`):

$$q\, uV + (1-q)\, dV + \delta V = (1+r)V \;\Rightarrow\; q = \frac{1 + r - \delta - d}{u - d}.$$

With construction cost $K_t$ at time $t$, the option to build at any node is valued backward:

$$F_t = \max\Big(V_t - K_t,\ \frac{q F_{t+1}^{u} + (1-q) F_{t+1}^{d}}{1+r}\Big),\qquad F_T = \max(V_T - K_T, 0).$$

The **value of waiting** is $F_0 - \max(V_0 - K_0, 0)$. Three forces govern it:

* **Volatility** ($u$, $d$) raises the value of keeping the choice open, because the downside of waiting is truncated at zero and the upside is not.
* **The cash yield $\delta$** is the cost of waiting. Every year you wait, you forgo the NOI the building would have produced. A high cap rate makes waiting expensive.
* **Cost escalation** raises the strike over time, which also makes waiting expensive.

The perpetual continuous-time version (McDonald and Siegel, 1986; Dixit and Pindyck, 1994) gives a closed-form hurdle. Invest when

$$\frac{V}{K} \ge \frac{\beta}{\beta - 1},\qquad \tfrac12\sigma^2\beta(\beta - 1) + (r - \delta)\beta - r = 0,\ \beta > 1.$$

At $\sigma = 0$ and $\delta > r$ the hurdle collapses to 1, which is the NPV rule. With uncertainty the hurdle exceeds 1. **A positive NPV is necessary but not sufficient.**

### 13.4.9 Real-world versus risk-neutral valuation

Practitioners often value waiting with a decision tree: real-world probabilities $p$, discounted at the asset's required return $k$. That method misprices options, because an option is riskier than its underlying and needs a higher discount rate. The risk-neutral tree avoids the problem by changing the probabilities instead of the rate. When the two methods agree on the decision, the conclusion is robust. When they disagree, trust the risk-neutral answer for market risk. For **idiosyncratic** risks such as an entitlement vote, use real-world probabilities, because investors do not demand a premium for risk they can diversify away. Case I combines both.

---

## 13.5 Worked examples

All inputs are [HYPOTHESIS] unless cited. All ten examples are reproduced in `tests/test_ch13_examples.py`.

### Example 13.1 — Hold or sell: the IRR on equity at market

**Given.** The multifamily asset from §13.1. Bid \$44,000,000. Forward NOI \$2,200,000, growing 3.0% a year. Selling costs 1.5%. Loan \$24,000,000, fixed 4.25%, interest-only, five years remaining. Yield maintenance per §13.4.2 with the five-year Treasury at 3.75%. Hold scenario: five more years, exit at a 5.25% cap on year-6 NOI, 1.5% selling costs, loan repaid at maturity.

Alternative: invest the same equity in stabilized industrial at a 6.25% cap on forward NOI. NOI grows 2.5%. Buyer costs 1.5%. Loan at 55% LTV, 6.00% interest-only. Exit at a 6.50% cap after five years, 1.5% selling costs.

**Find.** $E_M$, the hold IRR, the alternative IRR, the break-even exit cap, and unlevered IRRs for both.

**Solution.**

*Prepayment.* $a_{\overline{5}|3.75\%} = 4.4833$. $PP = 24{,}000{,}000 \times (0.0425 - 0.0375) \times 4.4833 = \$537{,}991$.

*Equity at market.* $E_M = 44{,}000{,}000 \times 0.985 - 24{,}000{,}000 - 537{,}991 = 43{,}340{,}000 - 24{,}537{,}991 = \$18{,}802{,}009$.

*Hold flows.* NOI path (years 1–6): 2,200,000; 2,266,000; 2,333,980; 2,403,999; 2,476,119; 2,550,403. Interest is \$1,020,000 a year.

| Year | NOI | Interest | Reversion | Equity flow |
|---|---:|---:|---:|---:|
| 0 | | | | −18,802,009 |
| 1 | 2,200,000 | 1,020,000 | | 1,180,000 |
| 2 | 2,266,000 | 1,020,000 | | 1,246,000 |
| 3 | 2,333,980 | 1,020,000 | | 1,313,980 |
| 4 | 2,403,999 | 1,020,000 | | 1,383,999 |
| 5 | 2,476,119 | 1,020,000 | 23,850,418 | 25,306,537 |

Gross reversion $= 2{,}550{,}403/0.0525 = \$48{,}579{,}104$. Net of 1.5% selling costs and the \$24.0m loan: \$23,850,418. **Hold IRR = 11.21%.**

*Alternative.* $P = 18{,}802{,}009/(1 + 0.015 - 0.55) = \$40{,}434{,}427$. Loan $= 0.55P = \$22{,}238{,}935$. Year-1 NOI $= 0.0625P = \$2{,}527{,}152$. Interest $= \$1{,}334{,}336$. The equity flows are −18,802,009; 1,192,816; 1,255,994; 1,320,753; 1,387,130; 22,544,717. **Alternative IRR = 9.01%.**

*Break-even exit cap.* Solving for the hold exit cap that gives 9.01% yields **5.57%**: 57 bp above today's 5.00% bid cap and 32 bp above the base exit cap.

*Unlevered comparison.* Hold, unlevered on net sale value: **7.17%**. Industrial, unlevered on gross cost: **7.41%**.

**Check.** The hold's year-0 equity and reversion can be verified by hand: $0.985 \times 48{,}579{,}104 = 47{,}850{,}418$, less 24,000,000 = 23,850,418. The alternative's LTV at purchase is $22{,}238{,}935 / 40{,}434{,}427 = 55.0\%$. The hold's LTV on the bid is $24.0/44.0 = 54.5\%$. Leverage is comparable.

**Decision consequence.** On an unlevered basis the industrial alternative is better by about 24 bp. That is before two sets of transaction costs are tested for robustness and before any adjustment for the industrial asset's different risk. On a levered basis the hold wins by 220 bp. The entire difference comes from the 4.25% loan, which the hold keeps and the sale destroys. The acquisitions officer's "5% versus 6¼%" framing compares yields and ignores both growth and financing. The defensible statement is: *hold unless you expect the multifamily exit cap to exceed about 5.57%, or unless the 4.25% loan could be assumed by a buyer and priced into the bid.* An assumable loan changes the analysis: the cheap debt then becomes part of what the buyer pays for, and the bid should rise.

### Example 13.2 — Refinance instead: the marginal cost of a cash-out

**Given.** Same asset. A lender offers a new five-year interest-only loan at 6.00%. Sizing constraints: 65% LTV, 1.25x DSCR, 8.0% debt yield. Refinancing costs 1.0% of the new loan. Prepayment as in Example 13.1.

**Find.** The new loan, cash released, and the marginal cost of the cash-out.

**Solution.** `cre.max_loan`: LTV \$28,600,000; DSCR $2{,}200{,}000/1.25/0.06 = \$29{,}333{,}333$; debt yield $2{,}200{,}000/0.08 = \$27{,}500{,}000$. **Debt yield binds: \$27,500,000.**

Cash released $= 27{,}500{,}000 - 24{,}000{,}000 - 537{,}991 - 275{,}000 = \$2{,}687{,}009$.

Incremental interest $= 27{,}500{,}000 \times 0.06 - 24{,}000{,}000 \times 0.0425 = 1{,}650{,}000 - 1{,}020{,}000 = \$630{,}000$ a year.

Incremental flows from the borrower's side: $+2{,}687{,}009$ today; $-630{,}000$ in years 1–5; $-3{,}500{,}000$ extra principal at year 5. The IRR of these flows from the lender's side is the **marginal cost: 26.99%**.

**Check.** Bound: even with no prepayment or costs, cash of \$3.5m for \$630,000 a year plus \$3.5m at maturity is an 18.0% coupon. The penalty and fees push the cost higher.

**Decision consequence.** A 6.00% loan quote hides a 27% marginal cost, because the refinancing reprices \$24m of 4.25% debt in order to release \$2.7m. No plausible redeployment earns 27%. If the partnership needs liquidity from this asset, the comparison should be with supplemental financing that leaves the first mortgage in place, such as a supplemental loan where the loan program permits it or preferred equity. Those instruments are priced at their own coupons on the incremental dollars only. Rule: **always compute the cost of the incremental capital, not the headline rate of the new instrument.**

### Example 13.3 — Geographic concentration: three Texas assets

**Given.** Value weights from §13.1: multifamily 44.0/102.8 = 0.4280, industrial 28.8/102.8 = 0.2802, hotel 30.0/102.8 = 0.2918. Annual value volatilities [HYPOTHESIS]: 12%, 9%, 20%. Correlations for the Texas portfolio [HYPOTHESIS]: MF–industrial 0.60, MF–hotel 0.50, industrial–hotel 0.55. Variant: replace the Houston industrial asset with industrial of the same volatility in a market with lower correlation to Texas (MF–industrial 0.25, industrial–hotel 0.30). Stress variant: every correlation 0.90.

**Find.** Portfolio volatility, each asset's share of risk, the diversification ratio, and a one-year 99% normal VaR in dollars.

**Solution.** With `risk.portfolio_volatility`:

| Portfolio | $\sigma_p$ | MF share of risk | Industrial share | Hotel share |
|---|---:|---:|---:|---:|
| All Texas | 11.34% | 38.2% | 17.3% | 44.5% |
| Industrial outside Texas | 10.59% | 39.8% | 12.5% | 47.7% |
| Stress ($\rho = 0.90$) | 13.06% | | | |
| No diversification ($\rho = 1$) | 13.49% | | | |

The weighted average volatility is $0.4280(12\%) + 0.2802(9\%) + 0.2918(20\%) = 13.49\%$. Diversification ratio, all Texas: $13.49/11.34 = 1.19$. With industrial outside Texas: 1.27.

One-year 99% VaR, all Texas, zero mean: $2.3263 \times 11.34\% \times \$102.8\text{m} = \$27.1\text{m}$. That is 65% of the \$41.8m of equity.

**Check.** At $\rho = 1$ the formula returns exactly the weighted average volatility, 13.49%. The stress case lies between the base case and that bound.

**Decision consequence.** Three findings. First, the hotel is 29% of value but **45% of risk**. Any decision about portfolio risk is mostly a decision about the hotel. Second, moving the industrial allocation outside Texas lowers volatility by only 75 bp, because industrial is the lowest-volatility asset and already contributes little risk. Diversifying the *hotel* exposure would do more. Third, in a stress the Texas portfolio's volatility rises to 13.06%, within 43 bp of no diversification at all. The diversification you measure in calm years is largely unavailable in the year you need it. A 99% VaR equal to 65% of equity says the portfolio's leverage, not its sector mix, is the first-order risk.

### Example 13.4 — Relative value: what the hotel–multifamily spread says

**Given.** Hotel cap rate 8.50%, multifamily 5.25%: a spread of 325 bp. A hypothetical ten-year history of the year-end spread, in bp: 250, 240, 235, 245, 260, 290, 390, 320, 265, 255. The 390 bp observation is the pandemic year. Assume, as a [HYPOTHESIS], that investors require a 250 bp higher unlevered return on hotels than on multifamily.

**Find.** The z-score of today's spread, with and without the pandemic year. The growth differential implied by the spread. The value effect of convergence to the 275 bp mean, under each of the two possible paths.

**Solution.**

*Statistics.* All ten years: mean 275 bp, sample s.d. 47.8 bp, $z = (325 - 275)/47.8 = 1.05$. Excluding the pandemic year: mean 262.2 bp, s.d. 27.1 bp, $z = 2.32$.

*Implied growth.* $c_H - c_{MF} = (k_H - k_{MF}) - (g_H - g_{MF})$, so $3.25\% = 2.50\% - (g_H - g_{MF})$ and $g_{MF} - g_H = 0.75\%$. The spread is consistent with multifamily NOI growing 75 bp a year faster than hotel NOI in perpetuity.

*Convergence.* If the spread returns to 275 bp through the hotel cap falling to 8.00%, hotel values rise $8.50/8.00 - 1 = 6.25\%$. If it returns through the multifamily cap rising to 5.75%, multifamily values fall $5.25/5.75 - 1 = -8.70\%$ and hotel values do not move.

**Check.** The z-score formula is symmetric. The sensitivity to one observation is the point: removing one year more than doubles $z$.

**Decision consequence.** "Hotels are cheap" is a claim that one of two things is wrong: either the market's hotel risk premium is too high, or its forecast of hotel growth is too low. A z-score of 1.05 on ten annual observations, one of them a pandemic, is weak evidence of either. Two specific beliefs would justify an overweight. One is that the 75 bp growth gap is too wide, for example because hotel supply growth is low while multifamily deliveries are high (Chapter 8). The other is that the hotel risk premium reflects pandemic memory more than forward risk. If neither can be supported with data, the spread is information about the market's beliefs, not a signal. Note also that only one of the two convergence paths pays an owner of hotels. An owner of both sectors earns nothing from convergence that occurs through multifamily repricing.

### Example 13.5 — Hedging the acquisition pipeline with Treasury futures

**Given.** Two acquisitions close in four months and require \$60,000,000 of 10-year, interest-only, monthly-pay fixed-rate debt priced at the 10-year Treasury plus 175 bp. Today that implies 6.00% [HYPOTHESIS: 10-year Treasury 4.25%]. The futures DV01 is \$85 per contract [HYPOTHESIS; obtain the live CTD-based figure before trading]. The CME 10-Year T-Note futures contract has \$100,000 face value [FACT; ch13-S07].

**Find.** The pipeline DV01, the number of contracts, and the P&L at lock in three scenarios: (a) Treasuries +50 bp, spread unchanged; (b) Treasuries −40 bp, spread +60 bp; (c) Treasuries −40 bp and the acquisitions fail to close.

**Solution.**

*DV01.* `fi.dv01(0.06, 0.06, 10, face=60_000_000, freq=12)` = **\$45,037** per bp. Annual-annuity approximation: $60{,}000{,}000 \times 0.0001 \times a_{\overline{10}|6\%} = 6{,}000 \times 7.3601 = \$44,161$, within 2%.

*Contracts.* $N = 45{,}037/85 = 529.8 \to$ **530 short contracts**.

| Scenario | Loan PV effect | Futures P&L | Net |
|---|---:|---:|---:|
| (a) Tsy +50, spread 0 | −2,251,837 | +2,252,500 | +663 |
| (b) Tsy −40, spread +60 | −900,735 | −1,802,000 | −2,702,735 |
| (c) Tsy −40, no deal | 0 | −1,802,000 | −1,802,000 |

Loan PV effect = $-45{,}037 \times (\Delta y + \Delta s)$. Futures P&L = $530 \times 85 \times \Delta y_{Tsy}$ (short gains when yields rise).

**Check.** In (a) the hedge offsets the loan within rounding, because only Treasuries moved. In (b) the all-in rate rose 20 bp. Unhedged, the cost would have been \$900,735. Hedged, it is \$2.70m, three times larger.

**Decision consequence.** The futures hedge removes Treasury risk and keeps spread risk, and in a flight to quality the two move against each other. It also creates closing risk, as (c) shows. Better tools are: (i) a **rate lock** from the lender, which covers the all-in rate; (ii) a **forward-starting swap**, which removes swap-rate risk but leaves the swap spread and the credit spread; or (iii) hedging only the probability-weighted pipeline. Each has a cost. The futures hedge is cheapest to execute and has the most basis. A desk that hedges should write down which risk it keeps, and size the hedge to the probability that the deal closes. Problem 13.10 develops this.

### Example 13.6 — Sizing the liquidity reserve for a two-year stress

**Given.** The §13.1 portfolio. Annual debt service: multifamily \$1.02m, industrial \$0.90m, hotel \$1.65m (floating, capped). A two-year stress [HYPOTHESIS]:

| | Year 1 | Year 2 |
|---|---|---|
| Multifamily NOI | −8% (\$2.024m) | −8% (\$2.024m) |
| Industrial NOI | −5% (\$1.710m) | −15%: one tenant leaves (\$1.530m) |
| Hotel NOI | −55% (\$1.080m) | −30% (\$1.680m) |
| Committed capital | Hotel PIP \$1.2m | none |

The hotel loan of \$22.0m matures at the end of year 2. In the stress, a new lender will lend 55% of value. Value is year-2 NOI capitalized at 9.50%. No distributions are made during the stress.

**Find.** The portfolio's net cash flow by year, the maturity gap, the reserve $R^*$, and its opportunity cost at a 4.0% reserve yield and an 11.0% target equity return.

**Solution.**

| | Year 1 | Year 2 |
|---|---:|---:|
| MF: 2.024 − 1.020 | +1.004 | +1.004 |
| Industrial: NOI − 0.900 | +0.810 | +0.630 |
| Hotel: NOI − 1.650 | −0.570 | +0.030 |
| PIP | −1.200 | 0 |
| **Net cash flow $X_t$** | **+0.044** | **+1.664** |

Hotel stressed value $= 1.680/0.095 = \$17.68\text{m}$. New loan $= 0.55 \times 17.68 = \$9.73\text{m}$. **Maturity gap** $= 22.00 - 9.73 = \$12.27\text{m}$.

Cumulative cash: end of year 1 +\$0.044m; end of year 2 $0.044 + 1.664 - 12.274 = -\$10.57\text{m}$. **$R^* = \$10.57\text{m}$.**

If the hotel had to stand alone with no support from the other assets: $0.570 + 1.200 - 0.030 + 12.274 = \$14.01\text{m}$.

Opportunity cost: $10.57 \times (0.11 - 0.04) = \$0.74\text{m}$ a year, or 1.77% a year on \$41.8m of equity.

**Check.** Operating shortfalls total less than \$1.8m over two years. More than 85% of the hotel's stand-alone need is the maturity.

**Decision consequence.** The reserve is dominated by one event, the hotel maturity, not by operations. Holding \$10.6m of cash costs about 1.8% a year of portfolio return. Alternatives that address the same event include: extend or refinance the hotel loan now, while the hotel is valued at \$30m (Chapter 10); buy a maturity extension option; or sell the hotel, which is also the asset contributing 45% of portfolio risk (Example 13.3). The reserve calculation turns a vague worry into a price: \$0.74m a year is the most the partnership should pay, per year, to eliminate the maturity risk by other means.

### Example 13.7 — Portfolio leverage: where the debt sits matters for default, not for equity volatility

**Given.** A simplified two-asset portfolio: \$50m of multifamily ($\sigma = 10\%$) and \$50m of hotel ($\sigma = 20\%$), correlation 0.50. Total debt is fixed at \$50m. A refinancing in three years requires value of at least the loan divided by 0.75 (a 75% LTV test). Log values are normal with no drift in expected value: $\ln V_T \sim N(\ln V_0 - \tfrac12\sigma^2T,\ \sigma^2T)$, so $E[V_T] = V_0$ [HYPOTHESIS]. Allocations of the \$50m: A, 50%/50% LTV; B, 70% on MF and 30% on hotel; C, 30% on MF and 70% on hotel; D, equal distance to the refinancing threshold.

**Find.** Portfolio equity volatility. The probability that each asset fails the refinancing test, $P_i = N\big((\ln(\lambda_i/0.75) + \tfrac12\sigma_i^2T)/(\sigma_i\sqrt T)\big)$. The expected number of failed refinancings.

**Solution.** Portfolio asset volatility $= \text{portfolio\_volatility}([0.5,0.5],[0.10,0.20],\rho=0.5) = 13.23\%$. Equity volatility $= 13.23\% \times 100/50 = 26.46\%$ in **every** allocation.

| Allocation | MF LTV | Hotel LTV | P(MF fails) | P(hotel fails) | Expected failures |
|---|---:|---:|---:|---:|---:|
| A | 50% | 50% | 1.21% | 15.93% | 0.171 |
| B | 70% | 30% | 37.76% | 0.67% | 0.384 |
| C | 30% | 70% | 0.00% | 48.96% | 0.490 |
| D | 57.4% | 42.6% | 7.23% | 7.23% | 0.145 |

D solves for the split at which both assets are the same number of standard deviations from the threshold.

**Check.** In C the hotel at 70% LTV needs its value to stay above 93.3% of today's value for three years at 20% volatility, which is close to a coin flip. That is consistent with 48.96%.

**Decision consequence.** Portfolio leverage determines equity volatility. Asset-level leverage determines how many separate default and refinancing events the portfolio faces. With non-recourse, asset-level debt, each failure is a separate negotiation, loss of control, or foreclosure. Placing the most debt on the most volatile asset (C) is the worst allocation. It is also the one lenders and sponsors often drift into, because hotels are the assets that "need" leverage to hit return targets. The minimum-failure allocation puts more debt on the low-volatility asset, roughly in proportion to the inverse of volatility. Cross-collateralization changes the analysis, because the assets then fail together or not at all, and it should be priced as such.

### Example 13.8 — The option to develop: a binomial tree

**Given.** The value today of the completed building on a site is \$30.0m. The construction cost if started today is \$27.0m, escalating 3% a year. The risk-free rate is 4.0% a year. The stabilized NOI yield forgone while waiting is $\delta = 5.5\%$. Value volatility is 20%, so $u = e^{0.20} = 1.2214$ and $d = 0.8187$. The option to build lasts two years (the entitlement expires). For simplicity, construction is treated as instantaneous, with $V$ and $K$ measured at the decision date.

**Find.** The NPV of building now, the option value, the value of waiting, the optimal policy, and the sensitivity to volatility.

**Solution.**

$q = (1 + 0.04 - 0.055 - 0.8187)/(1.2214 - 0.8187) = 0.4129$.

Value lattice (\$m) and option values (\$m):

| Node | $V$ | $K_t$ | Exercise $V - K_t$ | Option value | Action |
|---|---:|---:|---:|---:|---|
| t=2, up-up | 44.75 | 28.64 | 16.11 | 16.11 | build |
| t=2, up-down | 30.00 | 28.64 | 1.36 | 1.36 | build |
| t=2, down-down | 20.11 | 28.64 | −8.53 | 0 | let lapse |
| t=1, up | 36.64 | 27.81 | 8.83 | 8.83 | build |
| t=1, down | 24.56 | 27.81 | −3.25 | 0.54 | wait |
| t=0 | 30.00 | 27.00 | 3.00 | **3.81** | **wait** |

At the down node: $(0.4129 \times 1.3557 + 0.5871 \times 0)/1.04 = 0.538$. At t=0: $(0.4129 \times 8.8321 + 0.5871 \times 0.5383)/1.04 = 3.810$.

NPV now = \$3.00m. Option value = **\$3.81m**. Value of waiting = **\$0.81m**.

Sensitivity to volatility:

| $\sigma$ | Option value | Value of waiting | Build now? |
|---|---:|---:|---|
| 10% | \$3.00m | \$0 | yes |
| 15% | \$3.10m | \$0.10m | no |
| 20% | \$3.81m | \$0.81m | no |
| 25% | \$4.51m | \$1.51m | no |

Perpetual-option hurdle (continuous $r = 4\%$, $\delta = 5.5\%$): $V/K \ge 1.22$ at $\sigma = 10\%$; 1.65 at 20%; 1.92 at 25%. Today $V/K = 1.11$.

**Check.** At $\sigma = 10\%$ the tree's value equals NPV exactly, so building now is optimal. The perpetual hurdle says wait even at 10%, because it assumes the option never expires and the cost never escalates. Both features make waiting more valuable than in the two-year tree. The binomial tree reflects this site's actual terms.

**Decision consequence.** A developer who builds because "NPV is positive" gives up \$0.81m of option value at 20% volatility, 27% of the NPV. The policy is a trigger, not a date: build after an up move; wait after a down move. The practical value of the tree is that it gives the trigger in observable terms. At t=1, build if the completed value exceeds about \$27.8m plus the remaining option value, and the tree shows that an up-move to \$36.6m clears it. If the entitlement could be extended cheaply, the option would be worth more, and the perpetual hurdle shows the direction.

### Example 13.9 — When doing nothing dominates: a pending competitive-supply vote

**Given.** A hotel developer controls a site. A city council will vote in 12 months on a competing 250-room convention-center hotel. If the competitor is denied (real-world probability $p = 0.65$), the completed value of the developer's hotel at t=1 is \$33.0m. If it is approved, value is \$24.0m. The building's NOI in year 1, if built now, is \$1.6m. The required unlevered return is $k = 8\%$. The construction cost today is \$27.0m, escalating 3% to \$27.81m in a year. Risk-free rate 4%. Treat the vote as market-priced uncertainty about value for the risk-neutral check [HYPOTHESIS; §13.4.9 explains the alternative].

**Find.** The value today of the completed building, the NPV of building now, the value of waiting under a real-world decision tree and under risk-neutral pricing, and the cost escalation at which building now becomes optimal.

**Solution.**

$V_0 = [0.65(33.0) + 0.35(24.0) + 1.6]/1.08 = 31.45/1.08 = \$29.120\text{m}$.

NPV now $= 29.120 - 27.000 = \$2.120\text{m}$.

*Wait, real-world tree.* At t=1, build only if denied: $33.0 - 27.81 = \$5.19\text{m}$. Value today $= 0.65 \times 5.19/1.08 = \$3.124\text{m}$.

*Wait, risk-neutral.* $q = [(1.04)(29.120) - 1.6 - 24.0]/(33.0 - 24.0) = 0.5206$. Value $= 0.5206 \times 5.19/1.04 = \$2.598\text{m}$.

Value of waiting: \$1.00m (real-world) or \$0.48m (risk-neutral). Both say wait.

*Break-even escalation.* Building now wins when $q(33.0 - 27.0(1+g_K))/1.04 < 2.120$, which gives $33.0 - 27.0(1+g_K) < 4.236$, or $g_K > 6.53\%$.

**Check.** The real-world tree discounts the option at the asset's 8% rate and overstates the value of waiting, as §13.4.9 predicts. The decision does not change.

**Decision consequence.** The project has a positive NPV of \$2.1m, and doing nothing for a year is worth more. Waiting avoids committing \$27m in the 35% of states where the competitor is approved and the completed hotel would be worth \$24.0m against a \$27.0m commitment. The developer pays for waiting with a year of forgone NOI and 3% cost escalation, and both are explicit in the tree. Waiting stops being optimal if costs escalate faster than about 6.5% a year, if a competitor could take the site's position (pre-emption, Grenadier, 1996), or if the entitlement lapses. **Doing nothing has positive strategic value when information is about to arrive, the commitment is irreversible, and the cost of delay is small relative to the loss avoided.** All three conditions can be checked.

### Example 13.10 — The round-trip hurdle for capital recycling

**Given.** An asset worth \$40.0m with a \$20.0m loan, so equity before costs is \$20.0m. The owner's forward hold return on that equity is 9.0% a year [HYPOTHESIS]. Recycling into an asset of the same size and leverage costs: selling costs 1.5% of value (\$0.60m), prepayment 1.0% of the loan (\$0.20m), buyer costs 1.5% of the new value (\$0.60m), and new-loan fees 1.0% (\$0.20m). Assume returns accumulate in the position (no interim distributions) and that the two assets carry the same risk.

**Find.** The gross annual return the replacement must earn to match holding, over 3-, 5-, and 10-year horizons.

**Solution.** Total switching cost $= 0.60 + 0.20 + 0.60 + 0.20 = \$1.60\text{m}$, or $f = 8.0\%$ of equity. Equal terminal wealth requires $(1-f)(1+r_{alt})^T = (1+r_{hold})^T$, so

$$r_{alt} = \frac{1 + r_{hold}}{(1-f)^{1/T}} - 1.$$

| Horizon $T$ | Required $r_{alt}$ | Hurdle over holding |
|---|---:|---:|
| 3 years | 12.07% | +307 bp |
| 5 years | 10.83% | +183 bp |
| 10 years | 9.91% | +91 bp |

**Check.** The first-order approximation is $f/T$: 267 bp, 160 bp, and 80 bp. Compounding makes the true hurdle larger.

**Decision consequence.** An 8% round trip is paid once and recovered only over the life of the new investment. A recycling proposal must show an expected return advantage, at equal risk, of roughly 180 bp a year over five years. That is a very large edge relative to the precision of any real estate forecast. Recycling is justified when the advantage is large and well-founded: a material mispricing, a strategic exit from a market whose thesis has broken, or a risk reduction the investor values for its own sake, as with the hotel in Example 13.3. It is not justified by a difference in going-in yields.

---

## 13.6 CRE application: the partnership's capital-recycling memo

The examples connect into one memo.

1. **Multifamily: hold, do not refinance.** The forward levered IRR on equity at market is 11.21% against 9.01% for the industrial alternative (Example 13.1). The advantage depends on the 4.25% loan, and the break-even exit cap is 5.57%. The cash-out refinancing costs 27% on the incremental dollar (Example 13.2). Revisit if the bid rises enough to put the break-even exit cap below the partnership's own exit forecast, or if a buyer offers to assume the loan.
2. **Hotel: the portfolio's risk lives here.** It is 29% of value, 45% of risk, and creates a \$12.3m maturity gap in a plausible stress (Examples 13.3 and 13.6). The decision is between paying about \$0.74m a year in reserve drag, refinancing early, or selling. Relative value (Example 13.4) does not by itself justify a larger hotel allocation.
3. **Pipeline: lock, don't speculate.** Prefer a lender rate lock or a forward-starting swap, sized to the probability that each deal closes (Example 13.5).
4. **Leverage placement.** New debt should go on low-volatility assets first (Example 13.7).
5. **Land: wait, with a trigger** (Examples 13.8 and 13.9; Case I).

A REIT or fund faces the same arithmetic plus one constraint the partnership does not: distribution requirements and investor-level reporting. That is why public REITs often recycle through special dividends rather than reinvestment when they judge acquisition yields to be inadequate (§13.9).

### Development versus stabilized investment

A development project is a stabilized asset plus a set of options and obligations: the construction-cost exposure, a lease-up risk, a financing-market exposure at completion, and the option value examined in §13.4.8. The **development spread**, yield on cost minus market cap rate, is the compensation for those risks. A 7.0% yield on cost against a 5.50% market cap is a 150 bp spread and a 27% margin on cost ($7.0/5.5 - 1$). Whether 150 bp is enough depends on the time to stabilization, the volatility of $V$ over that time, and what the developer could earn by buying a stabilized asset instead. The real-option framework adds one more question. Even if the spread is adequate, is *now* the best time to commit?

---

## 13.7 When the relationships fail

1. **Equity at market assumes the bid is real.** A broker's opinion of value, an unfunded LOI, or a bid conditional on financing is not a market price. If the bid has a 30% chance of failing, $E_M$ is an expectation, not a number. Chapter 1's leg-risk framework applies.
2. **Hold–sell IRR comparisons hide risk differences.** A hold IRR of 11% on a 54% LTV multifamily and 9% on a 55% LTV industrial are comparable. A hold IRR on a hotel and an alternative on a net-leased building are not, even at the same leverage. Compare unlevered first, then adjust for risk explicitly.
3. **Correlation estimates are unstable.** NOI correlations estimated from appraisal-based indices are smoothed (Chapter 2) and understate co-movement. Transaction-based correlations are noisy. Stress correlations should be set by judgment and tested, not estimated from calm periods.
4. **Cap-rate spreads can stay "wide" for a decade.** If the growth differential the market prices is correct, the spread never converges. Cap-rate mean reversion is a [HYPOTHESIS] to test against a long series, not an assumption.
5. **DV01 hedges are linear; loans and pipelines are not.** Deals fail, loan amounts change with appraisals, and spreads move with Treasuries in crises. The hedge ratio is a starting point.
6. **Reserves sized to one stress fail in a different stress.** The two-year scenario in Example 13.6 does not cover a three-year hotel disruption, an insurance-market shock, or simultaneous maturities. Run several stresses, and size to the worst one you are willing to survive.
7. **Real-option values are only as good as $\sigma$ and $\delta$.** Property-level volatility is not observable. Using 20% instead of 15% raised the value of waiting eightfold in Example 13.8. When the decision flips within the plausible range of $\sigma$, say so. That is an abstention signal, not a reason to pick the convenient number.
8. **Options can be pre-empted.** The binomial model assumes the option is proprietary. In a market where several landowners hold similar options, waiting invites competitors to build first. Grenadier (1996) shows that competition can produce overbuilding cascades in which owners exercise early. The value of waiting falls when your option is shared.
9. **Waiting can become a habit.** The real-option argument is not a license to wait indefinitely. It produces a trigger. An investor who has not written down the trigger is not holding an option. They are avoiding a decision.

---

## 13.8 A note on fund vintages

The timing question in this chapter also appears at the level of commingled private equity real estate funds. Funds raised near a market peak deploy capital at high prices; funds raised after a downturn deploy at low prices. Industry performance surveys group closed-end real estate fund returns by vintage year for exactly this reason. This chapter does not quote vintage-year returns for 2006–2010 because they were not verified against a primary dataset (*verification pending*; candidate sources: NCREIF/Townsend fund indices, Cambridge Associates real estate benchmarks, or Preqin). The mechanism is the same as in Example 13.9: a fund that must deploy within its investment period cannot wait, and the inability to wait has a cost that the real-option framework can price.

---

## 13.9 Historical episode: Equity Residential's 2015–2016 portfolio sale and its later re-entry

**Date and environment.** Late 2015. U.S. apartment REITs had experienced several years of rent growth, and private buyers were active. Equity Residential (EQR), a large apartment REIT, held assets across coastal urban markets and several other metros [INFERENCE from the filings cited below].

**What happened.**

* On 23 October 2015 EQR agreed to sell 72 operating properties containing 23,262 apartment units in five U.S. markets to affiliates of Starwood Capital Group for \$5.365 billion. The portfolio included 33 properties in South Florida, 18 in Denver, 10 in Washington DC, 8 in Seattle, and 3 in the Inland Empire [FACT; EQR press release dated 26 October 2015 and EQR Form 8-K; ch13-S01, ch13-S02; VERIFIED-SECONDARY via search excerpts of the primary documents].
* The price is about \$230,600 per unit [INFERENCE: \$5.365 billion / 23,262 = \$230,634; reproduced in `tests/test_ch13_examples.py`]. Secondary coverage reported a capitalization rate of about 5.5% and quoted an analyst estimate of the buyer's forward nominal cap rate at about 5.3% *(verification pending: the definitions differ and the figures have not been checked against the primary release)*.
* EQR closed the sale on 26 and 27 January 2016 [FACT; EQR Form 10-K for 2016 and 2018; ch13-S03, ch13-S04].
* EQR paid special dividends of \$8.00 per share/unit (about \$3.0 billion) on 10 March 2016 and \$3.00 per share/unit (about \$1.1 billion) on 14 October 2016, \$11.00 in aggregate [FACT; EQR Form 10-K for 2016 and 2017; ch13-S03, ch13-S05]. It used the majority of the remaining proceeds to reduce aggregate indebtedness so that the transaction was leverage-neutral [FACT; same sources].
* At the October 2015 announcement, management described the sale as narrowing the company's focus to its core high-density urban markets [FACT, paraphrased; ch13-S01, VERIFIED-SECONDARY]. The 2016 10-K referred to the difficulty of recycling a large amount of capital, \$6.8 billion, in a competitive acquisition market *(verification pending: the exact scope of the \$6.8 billion figure — total disposition proceeds or a subset — has not been confirmed against the filing's disposition table)*.
* In 2021 EQR acquired properties in Atlanta, Austin, Dallas/Fort Worth, and Denver, described in its 2021 10-K as "expansion markets". The 10-K described the Atlanta, Austin, and Dallas/Fort Worth acquisitions as a re-entry into those markets. 2021 acquisitions totaled 17 properties for about \$1.7 billion, of which about 82% was in the expansion markets. The company funded them largely by selling older properties in established markets, mainly in California [FACT; EQR Form 10-K for 2021 and Q3/Q4 2021 earnings materials; ch13-S06; VERIFIED-SECONDARY].

**What was knowable then.** The sale price, the markets exited, and the stated reasons were public at announcement. The future relative performance of Denver and South Florida apartments against coastal urban apartments was not knowable. Neither was the 2020 pandemic, which hit dense urban rental markets particularly hard.

**Interpretation 1: the capital-recycling decision in this chapter's terms.** EQR compared the forward return on equity at market in the sold markets with the return on redeploying into its target markets. It concluded that acquisitions at prevailing prices did not justify redeploying most of the proceeds. The reinvestment alternative it chose was to return capital to shareholders and reduce debt [INFERENCE from the use of proceeds]. This is the public-company version of "doing nothing has positive strategic value": when the alternative's IRR is inadequate, return the capital rather than force deployment. It also delivered the proceeds to shareholders, who could redeploy them as they chose.

**Interpretation 2: a market-selection call that later partly reversed.** EQR exited Denver in 2016 and was buying in Denver again in 2021, and it re-entered Atlanta, Austin, and Dallas/Fort Worth. One reading is that the 2015 market-selection thesis (concentrate in coastal high-density markets) was revised after evidence accumulated, notably during 2020–2021 [INFERENCE]. Another reading is that both decisions were correct relative to the prices available at the time: selling Denver at 2015–2016 pricing and buying at 2021 pricing may each have been sound if prices reflected different information [ALTERNATIVE INFERENCE]. This chapter does not compute the round trip's return, because doing so requires asset-level prices that were not verified.

**What the case establishes.** A large, well-informed owner treated a hold as a repurchase decision. It sold a large block at a price it judged attractive, did not force reinvestment, and kept leverage constant. Market selection was treated as a revisable judgment rather than a permanent identity.

**What it does not establish.** That the 2016 sale was value-creating relative to holding: the counterfactual returns are not documented here. That coastal urban apartments outperform or underperform other markets in general. That special dividends are generally superior to reinvestment.

**Strategies available then.** For a holder of EQR shares: accept the special dividend and redeploy it. For a private buyer: the Starwood side of the trade, buying a large diversified block at a single price, a liquidity-provision trade in Chapter 1's sense. For a competing REIT: bid for individual assets after the portfolio split, if the buyer resold pieces.

---

## 13.10 Decision exercise: the Tuesday agenda

Use the decision record template at `desk/investment_memos/decision_record_template.md`. Answer each of the six agenda items in §13.1, with a number and an invalidation criterion for each.

Specifically:

1. Sell, hold, or refinance the multifamily. State the break-even exit cap and what would change your answer, for example an assumable-loan bid.
2. Size the reserve under the Example 13.6 stress and under one additional stress of your own design. State which hotel action, if any, you would take and what it costs per year.
3. Recommend a pipeline hedge instrument and size. State the deal-closing probability you used.
4. State whether the 325 bp hotel–multifamily spread justifies any change in allocation, and what evidence would be needed.
5. State the land policy as a trigger (see Case I).
6. State what you will *not* do and why.

**Rubric** (full version in `problems/solutions/ch13_solutions.md`, §Decision exercise):

| Criterion | Weight | Full credit |
|---|---|---|
| Hold–sell on equity at market | 20% | Uses $E_M$, not cost basis; separates the financing effect from the asset effect; gives the break-even exit cap |
| Incremental cost of capital | 15% | Rejects the cash-out refinancing on its 27% marginal cost or proposes a supplemental instrument |
| Concentration and leverage | 20% | Identifies the hotel as the dominant risk; uses stress correlations; places debt by volatility |
| Liquidity | 20% | Sizes the reserve with the maturity included; prices the drag; compares it with alternatives |
| Hedging | 15% | Identifies basis and closing risk; sizes to the closing probability; prefers an all-in lock where available |
| Abstention and triggers | 10% | Names at least one action not taken and a measurable trigger for revisiting it |

There is no single correct allocation. A recommendation to sell the hotel and hold everything else is defensible. So is a recommendation to refinance the hotel early and hold a smaller reserve.

---

## 13.11 Frequent analytical errors

1. **Using IRR since inception to decide whether to hold.** It is sunk. Use the forward IRR on equity at market.
2. **Comparing going-in yields across sectors and calling the difference "accretion".** $c = k - g$. A higher cap rate is not a higher return unless risk and growth are equal.
3. **Ignoring the financing in a hold–sell.** Below-market debt is an asset of the hold. Prepayment is a cost of the sale. Assumability changes the bid.
4. **Quoting the headline rate of a refinancing instead of the marginal cost.** Compute the IRR of the incremental flows.
5. **Measuring diversification with calm-period correlations.** Run the stress correlation.
6. **Hedging Treasuries and believing the loan rate is hedged.** Credit spreads are a separate risk and often move the other way.
7. **Hedging deals that may not close at 100% of notional.** A failed deal turns the hedge into a naked position.
8. **Sizing a reserve without the maturity schedule.** Operating shortfalls are usually small; maturities are not.
9. **Confusing portfolio leverage with asset leverage.** Equity volatility depends on the former. The number of defaults depends on the latter.
10. **Building because NPV is positive.** With irreversibility and uncertainty, NPV > 0 is necessary but not sufficient.
11. **Discounting option payoffs at the asset's required return.** It overstates or understates the option's value depending on the direction. Use risk-neutral pricing, or at least check the decision against it.
12. **Treating "wait" as a decision without a trigger.** An option without an exercise rule is not being managed.

---

## 13.12 Connections to other chapters

* Chapter 1: liquidity provision, leg risk, and the "do nothing" alternative.
* Chapter 2: appraisal smoothing biases the correlations in Example 13.3.
* Chapter 6: DV01, duration, and the cap-rate/Treasury spread used in Example 13.5.
* Chapter 8: supply pipelines and the growth differential in Example 13.4.
* Chapter 9: residual land value and DCF, used in Case I.
* Chapter 10: loan sizing (`cre.max_loan`), yield maintenance, and refinancing gaps (Examples 13.2 and 13.6).
* Chapter 11: hotel operating leverage, which is why the hotel dominates portfolio risk.
* Chapter 12: maturity walls and forced sellers, the counterparties to a liquidity reserve.
* Chapter 18: interest-rate caps and option pricing; the Black–Scholes counterpart of §13.4.8.
* Chapter 21: position sizing and ruin; Example 13.6 is a survival constraint.
* Case F: the hotel-versus-Treasury allocation, which is opportunity-cost analysis with taxes.
* Case I: the development land option, which extends Examples 13.8 and 13.9.

---

## 13.13 One-page reference sheet

| Quantity | Formula |
|---|---|
| Equity at market | $E_M = V_0(1-s) - B_0 - PP$ |
| Simplified yield maintenance | $PP = B(r_L - y)\,a_{\overline{n}|y}$ |
| Price supported by equity | $P = E_M/(1 + b - \lambda)$ |
| Hold IRR | IRR of $[-E_M;\ NOI_t - DS_t;\ NOI_{T+1}(1-s)/c_T - B_T]$ |
| Marginal cost of a cash-out | IRR of $[C_0;\ -(L'r' - Br_L);\ -(L'-B)]$, lender side |
| Portfolio volatility | $\sigma_p^2 = \sum\sum w_iw_j\sigma_i\sigma_j\rho_{ij}$ |
| Risk contribution | $RC_i = w_i(\Sigma w)_i/\sigma_p$ |
| Portfolio equity volatility | $\sigma_E = \sigma_p \sum V_i / E$ |
| Cap rate and growth | $c = k - g$; $c_A - c_B = \Delta k - \Delta g$ |
| Loan DV01 | $\approx L \times 0.0001 \times a_{\overline{n}|r}$ |
| Futures contracts | $N = DV01_{loan}/DV01_{fut}$ |
| Hedged P&L | $-DV01_L(\Delta y + \Delta s) + N\,DV01_F\,\Delta y$ |
| Reserve | $R^* = \max(0, -\min_\tau \sum_{t\le\tau}(X_t - M_t))$ |
| Reserve drag | $R^*(k_E - r_f)$ |
| Risk-neutral probability | $q = (1 + r - \delta - d)/(u - d)$ |
| Option recursion | $F_t = \max(V_t - K_t,\ [qF^u + (1-q)F^d]/(1+r))$ |
| Value of waiting | $F_0 - \max(V_0 - K_0, 0)$ |
| Perpetual hurdle | $V/K \ge \beta/(\beta-1)$ |
| Refinance distress probability | $N\big((\ln(\lambda/\lambda_{max}) + \tfrac12\sigma^2T)/(\sigma\sqrt T)\big)$ |

**Questions before any trade.** What is my equity at market? What is the best alternative at the same risk? What does the incremental capital cost? Which asset dominates portfolio risk, in a stress? Which risk does my hedge leave me with? How much cash do I need if the worst maturity arrives in the worst year? What does waiting cost, and what does it buy?

---

## References for this chapter

Source entries with verification status are in `references/sources_ch13.md`.

* Cox, J. C., Ross, S. A., and Rubinstein, M. (1979). "Option Pricing: A Simplified Approach." *Journal of Financial Economics*, 7(3), 229–263.
* Dixit, A. K., and Pindyck, R. S. (1994). *Investment under Uncertainty*. Princeton, NJ: Princeton University Press.
* Grenadier, S. R. (1996). "The Strategic Exercise of Options: Development Cascades and Overbuilding in Real Estate Markets." *Journal of Finance*, 51(5), 1653–1679.
* McDonald, R., and Siegel, D. (1986). "The Value of Waiting to Invest." *Quarterly Journal of Economics*, 101(4), 707–727.
* Titman, S. (1985). "Urban Land Prices under Uncertainty." *American Economic Review*, 75(3), 505–514.
* Equity Residential. Press release, 26 October 2015, "Equity Residential Announces Agreement to Sell 23,000 Apartment Units to Starwood Capital Group for \$5.365 Billion," and Form 8-K exhibit 99.1 (SEC EDGAR, CIK 906107).
* Equity Residential. Forms 10-K for fiscal years 2016, 2017, 2018, and 2021 (SEC EDGAR, CIK 906107).
* CME Group. 10-Year U.S. Treasury Note futures contract specifications. https://www.cmegroup.com/markets/interest-rates/us-treasury/10-year-us-treasury-note.contractSpecs.html
