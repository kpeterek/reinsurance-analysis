# Chapter 19 — Alternative and Emerging Speculative Assets

> **Status:** Complete (v1.0). All numbers are reproduced in `tests/test_ch19_examples.py`, using the new library module `models/python/sdesk/x_alt_assets.py`. Problems are in `problems/questions/ch19_problems.md`, solutions in `problems/solutions/ch19_solutions.md`, drills D171–D176 in `training/daily_drills/drill_bank_ch19.json`, and sources in `references/sources_ch19.md`. Historical figures in §19.9 are VERIFIED-SECONDARY (search excerpts of court filings, agency releases and contemporaneous reporting); items still marked *(verification pending)* are listed in the source file.

## Learning objectives

After this chapter you should be able to:

1. Score any asset on nine dimensions (cash-flow generation, intrinsic valuation anchor, financing, liquidity, custody and ownership rights, market transparency, transaction costs, speculative reflexivity, tail risk) and explain why two assets with the same composite score can be economically unlike each other and unlike CRE.
2. Show with an exact calculation why the **median** venture fund earns much less than the **mean** fund when deal outcomes follow a power law, and what that implies for manager selection and portfolio size.
3. Compute DPI, RVPI, TVPI and IRR for a private-equity fund. Trace the J-curve. Explain why IRR and TVPI can rank the same fund differently, and how a subscription line raises IRR while lowering TVPI.
4. Compute the Kaplan–Schoar public market equivalent (KS-PME) and interpret it as a multiple measured in index units.
5. Correct a stale or smoothed price series (Geltner filter, beta-adjusted stale NAV), and convert a gross return into a liquidity-adjusted return.
6. Compute the price-appreciation hurdle created by auction buyer's and seller's premiums, and explain why repeat-sales art indices overstate returns.
7. Value an asset that produces no cash flow from its expected resale price, and explain why that valuation has no anchor independent of other buyers' expectations.
8. Read the 2021–22 crypto boom and collapse as an episode about custody, self-referential collateral and reflexive leverage, and separate what the court record establishes from what it does not.

---

## 19.1 Opening investment problem: the alternatives sleeve

You advise a family office whose wealth came from a Texas hotel and multifamily portfolio. The family holds about \$180 million of CRE equity and \$60 million of Treasuries and listed equities. A new investment committee member argues that the family is "over-concentrated in real estate" and proposes a \$25 million alternatives sleeve. Six proposals are on the table. All facts are [HYPOTHESIS] — a constructed teaching case.

| # | Proposal | Size | Pitch |
|---|---|---|---|
| A | Commitment to a first-time venture fund (20 seed investments) | \$5m | "Top-quartile target: 3x net" |
| B | Secondary purchase of an LP interest in a 2019 buyout fund | \$6m | "Buy at 85% of NAV — a 15% discount" |
| C | A post-war painting at an evening sale | \$2m hammer | "Blue-chip art has returned 8–9% a year" |
| D | Bitcoin, held with a regulated custodian | \$4m | "Digital gold, uncorrelated with CRE" |
| E | A 40-acre entitlement play at the edge of a growing suburb | \$2.5m | "Land doubles once zoning is approved" |
| F | Voluntary carbon offsets from a forestry project, plus EU allowance futures | \$3m | "Policy tailwind; ESG premium" |

Each pitch states a return and implies an anchor. None states how the return is measured, what would make the price wrong, or what the family could sell, to whom, and at what cost, in a bad month. The family's existing book is CRE, so every proposal should be compared with what the family already understands: an asset with rent, a deed, a lender, an appraiser and a cap rate. Section 19.10 returns to the decision.

---

## 19.2 Economic intuition: anchors, rights, liquidity and reflexivity

### What makes CRE "anchored"

A stabilized building's price is tied to three things that exist independently of the next buyer's mood.

1. **Cash flow.** NOI pays the owner whether or not the asset trades. A buyer who never sells still earns a return.
2. **Replacement cost.** If price rises far above the cost of building a substitute, supply responds (Chapter 8). The supply response is slow, but it exists.
3. **Enforceable rights.** A recorded deed, title insurance, a lease, and a court system that enforces them. A lender will lend against these rights, which ties price to the credit market's independent judgment.

None of these makes CRE safe. Cap rates move, leverage amplifies, and appraisals lag (Chapters 2, 9, 12). But each gives the analyst a number that does not depend on what other speculators believe: NOI ÷ cap rate, replacement cost, or a lender's sizing.

### Remove the anchors one at a time

The assets in this chapter can be ordered by how many anchors they lose.

* **Private equity** keeps cash flow (portfolio companies earn profits) and enforceable rights, but loses liquidity and price transparency. The LP sees a quarterly NAV that is an estimate, not a price.
* **Venture capital** keeps enforceable rights but has little current cash flow. Value depends on a few outliers that reach exit. Outcome distributions are heavy-tailed, so the average is a poor guide to what a typical investor earns.
* **Development land** has no current income and negative carry. It keeps a strong ownership right and an anchor through the residual: land is worth what a completed building is worth minus what it costs to build. That anchor exists but is levered. A small change in end value causes a large change in land value (Example 19.8).
* **Fine art and collectibles** have no cash flow and no replacement cost: an original cannot be reproduced. They keep ownership rights, but provenance and authenticity can be contested. Transactions are rare, costly and selective.
* **Compliance carbon allowances** have no cash flow, but they have a regulatory anchor. A covered emitter must surrender an allowance or pay a penalty, so the allowance is worth roughly what it costs the marginal emitter to abate a tonne. That anchor depends on a policy that can change.
* **Voluntary carbon offsets** lack the compliance demand. Their value depends on buyers' reputational demand and on whether the claimed emission reduction is real, which is hard to verify.
* **Bitcoin** has no cash flow, no replacement cost in the usual sense (supply follows a fixed protocol schedule regardless of price), and no issuer. It does have a highly liquid market and a novel form of custody. Its price is what the marginal holder believes others will pay.
* **Other tokens and NFTs** often add issuer risk, thin markets and contested rights to the bitcoin profile. An NFT usually conveys a token, not copyright in the image [INFERENCE: depends on each project's licence terms].

As anchors fall away, price depends more on expectations of other buyers' expectations. That is the definition of **speculative reflexivity** used here: a market is reflexive when price changes alter the fundamentals or the funding that are supposed to justify the price (Chapter 3). In CRE the loop runs through collateral values and lending. In crypto the loop can run through the asset itself: a token used as collateral for loans that buy more of the token.

### Three warnings before the mathematics

1. **Comparable is not equivalent.** Scoring every asset on the same nine dimensions makes them comparable. It does not make them interchangeable. A composite score hides the profile: bitcoin and a buyout LP interest can receive the same total score for opposite reasons (Example 19.9).
2. **Reported returns in private and illiquid markets are biased upward in level and downward in risk.** Smoothing, stale marks, survivorship and selection all push in the same direction. The first task in any alternative is to re-measure the return.
3. **The relevant return is the one you can get.** Power-law outcomes mean that the average across all funds is not the outcome of a typical commitment. High round-trip costs mean that the index return is not the return of an owner who must buy and sell through an auction house.

---

## 19.3 Technical definitions

| Term | Definition |
|---|---|
| Paid-in capital (PIC) | Cumulative capital called from the LP, $\sum C_t$ |
| DPI | Distributions to paid-in: $\sum D_t / \sum C_t$ (realized multiple) |
| RVPI | Residual value to paid-in: $NAV_T / \sum C_t$ (unrealized multiple) |
| TVPI | Total value to paid-in: DPI + RVPI |
| Interim IRR | IRR of LP flows with current NAV treated as a terminal distribution |
| J-curve | The negative early path of cumulative net cash flow (and of interim IRR) while capital is called and fees paid before exits |
| Subscription (capital-call) line | A fund-level credit facility secured by LP commitments, used to delay capital calls |
| KS-PME | Kaplan–Schoar public market equivalent: fund distributions plus NAV, each divided by the index level at its date, over contributions divided by the index level at their dates |
| Power-law (heavy-tailed) outcomes | A distribution in which a small fraction of outcomes accounts for most of the total, so the mean exceeds the median by a wide margin |
| Appraisal or NAV smoothing | Reported values that adjust only partly to each period's change in market value: $r^*_t = (1-a) r_t + a\, r^*_{t-1}$ |
| Stale price | A mark that has not been updated for information that has since become public |
| Buyer's premium | Auction-house fee paid by the buyer on top of the hammer price, usually on a tiered (marginal) schedule |
| Seller's commission | Fee deducted from the hammer price paid to the consignor (negotiable for high-value consignments) |
| Repeat-sales index | An index estimated only from items that sold at least twice, by regressing log price relatives on time dummies (Bailey, Muth and Nourse, 1963) |
| Selection bias (resale) | Bias that arises because whether an item is resold depends on how its price has moved |
| Compliance allowance | A government-issued permit to emit one tonne of CO₂-equivalent within a cap-and-trade system |
| Voluntary offset | A credit issued under a private standard for a claimed emission reduction or removal, bought for voluntary claims |
| Custody | Who controls the asset and whether the owner's claim survives the custodian's insolvency |
| Self-referential collateral | Collateral whose value depends on the solvency or reputation of the borrower or its affiliates |

---

## 19.4 Equations and derivations

### 19.4.1 Private-fund multiples and IRR

Let $C_t \ge 0$ be calls and $D_t \ge 0$ distributions at annual dates $t = 0,\dots,T$, and $NAV_T$ the reported residual value.

$$DPI = \frac{\sum_t D_t}{\sum_t C_t}, \qquad RVPI = \frac{NAV_T}{\sum_t C_t}, \qquad TVPI = DPI + RVPI.$$

The interim IRR solves $\sum_t (D_t - C_t)/(1+IRR)^t + NAV_T/(1+IRR)^T = 0$.

Multiples ignore time. IRR ignores scale and assumes, through its arithmetic, that interim distributions are reinvested at the IRR itself. Neither alone describes the investment. The decisive fact for interim figures is that RVPI is an estimate. Early in a fund's life almost all of TVPI is RVPI.

**Why a subscription line raises IRR and lowers TVPI.** If the fund borrows to pay for investments and calls LP capital later, the LP's first negative flow moves later while distributions do not. IRR rises because the same distributions are earned on capital held for a shorter time. The line costs interest, which the LP ultimately pays, so total contributions rise and TVPI falls. Problem 19.8 quantifies the effect.

### 19.4.2 The Kaplan–Schoar PME

Let $I_t$ be the level of a total-return public index. Kaplan and Schoar (2005) compare the fund with a strategy that invests each call in the index and withdraws each distribution from it. Discount every flow to date 0 at the realized index return, $I_0/I_t$:

$$KS\text{-}PME = \frac{\sum_t D_t\, (I_0/I_t) + NAV_T\,(I_0/I_T)}{\sum_t C_t\,(I_0/I_t)} = \frac{\sum_t D_t/I_t + NAV_T/I_T}{\sum_t C_t/I_t}.$$

**Interpretation.** $C_t/I_t$ is the number of index units the LP could have bought with each call. $D_t/I_t$ is the number of index units each distribution would buy. KS-PME is the fund's TVPI measured in index units. A value above 1 means the fund returned more index units than it consumed. Multiplying numerator and denominator by $I_T$ (compounding every flow forward to $T$) leaves the ratio unchanged, so the result does not depend on the discounting date.

**What KS-PME is not.** It is not risk-adjusted beyond assuming that the index is the right benchmark with a beta of one. A buyout fund with portfolio leverage has equity beta above one, and its KS-PME against an unlevered index flatters it [INFERENCE from the leverage identity, Chapter 1 §1.4.6]. KS-PME is also a ratio, not a rate: it does not say how many years the outperformance took. Chapter 22 treats direct alpha and stochastic-discount-factor methods, which address both points.

**Mirror account (Long–Nickels style).** Run an index account that receives every call and pays every distribution. If the fund distributes much more than the index could fund, the mirror account goes negative at $T$. The negative balance is a symptom that the fund outperformed, but it makes an "index IRR" on the mirror flows meaningless. That is one reason KS-PME, a ratio, became standard.

### 19.4.3 Power-law portfolios: mean versus median

Let each deal's gross multiple $X_i$ be drawn independently from a discrete distribution with mean $\mu$. A fund holding $n$ equal-sized deals has multiple $\bar X_n = \frac{1}{n}\sum X_i$, with $E[\bar X_n] = \mu$ for every $n$. The **mean** is unaffected by diversification. The **median** is not. When a small probability $p_{\max}$ of a very large multiple $x_{\max}$ contributes a large share of $\mu$, most funds contain no such outcome:

$$P(\text{no } x_{\max} \text{ in } n \text{ deals}) = (1 - p_{\max})^n,$$
$$E[\bar X_n \mid \text{no } x_{\max}] = \frac{\mu - p_{\max}\,x_{\max}}{1 - p_{\max}}.$$

The second line follows because, conditional on excluding the top outcome, each deal's distribution is renormalized over the remaining outcomes. When $(1-p_{\max})^n > 0.5$, the median fund is a fund without the top outcome, and its multiple is near the conditional mean, far below $\mu$. As $n$ grows, $\bar X_n$ concentrates around $\mu$ and the median rises toward the mean. Heavy tails make that convergence slow.

### 19.4.4 Stale prices, smoothing and liquidity adjustment

**Geltner filter.** Chapter 2 §2.4.7 derives the inversion of first-order smoothing:

$$r_t = \frac{r^*_t - a\, r^*_{t-1}}{1-a}.$$

Summing over $t = 1,\dots,N$ gives an end-point identity that is useful as a check:

$$\sum_{t=1}^{N} r_t = \sum_{t=1}^{N} r^*_t + \frac{a}{1-a}\left(r^*_N - r^*_0\right).$$

Over a long window the arithmetic sums agree. Over a short window they differ by the end-point term: if the latest reported return is below the first, the smoothed series still has unrecognized decline in the pipeline.

**Stale NAV correction.** If the last mark $NAV_s$ predates a public market move $R_m$, and the private asset has beta $\beta$ to that market,

$$\widehat{V} = NAV_s\,(1 + \beta R_m).$$

A secondary bid stated as a discount to $NAV_s$ must be re-expressed against $\widehat V$. A "discount" to a stale mark can be a premium to current value.

**Liquidity-adjusted return.** Suppose that over a $T$-year hold the owner is forced to sell early with probability $\pi$ and then accepts a haircut $h$ to fair value. The expected exit factor is $1 - \pi h$. Spreading it over the hold,

$$r_{LA} = (1 + r)\,(1 - \pi h)^{1/T} - 1.$$

This is an expected-value adjustment. It understates the cost to an owner whose forced sales happen in bad states, when $h$ is largest and the money is most valuable. A risk-averse owner should apply a larger haircut than the average.

### 19.4.5 Auction costs and the appreciation hurdle

With a tiered buyer's premium schedule $\{(U_j, b_j)\}$ (each rate applies only to the slice of hammer price in its band), the buyer pays

$$P^{buy} = H_0 + \sum_j b_j\,\big(\min(H_0, U_j) - U_{j-1}\big)^+.$$

The seller receives $H_T(1 - s)$, where $s$ is the seller's commission plus deductions. With annual carrying cost $m$ (insurance, storage, conservation) paid at year-ends and a required return $k$, the hammer price needed at $T$ is

$$H_T^{req} = \frac{P^{buy}(1+k)^T + \sum_{t=1}^{T} m\,(1+k)^{T-t}}{1-s}, \qquad g^{req} = \left(\frac{H_T^{req}}{H_0}\right)^{1/T} - 1.$$

$g^{req}$ is the annual growth in **hammer** prices needed to earn $k$. An index that measures hammer-to-hammer changes must be compared with $g^{req}$, not with $k$.

### 19.4.6 Repeat-sales regression

For item $i$ bought in period $b$ and sold in period $s$, let $y_i = \ln(P_{i,s}/P_{i,b})$. The Bailey–Muth–Nourse model is

$$y_i = \beta_s - \beta_b + \varepsilon_i, \qquad \beta_0 = 0,$$

estimated by OLS on time dummies that equal $+1$ in the sale period and $-1$ in the purchase period. The index is $100\,e^{\beta_t}$. Only items that sold twice enter. If the decision to resell depends on $y_i$, the sample is selected on the dependent variable and the estimated $\beta$ is biased. Owners of items that fell in value tend to hold them (or sell privately), so observed $y_i$ are skewed upward. Korteweg, Kräussl and Verwijmeren (2016) model the sale decision explicitly and find that correcting for selection lowers average annual index returns for paintings from 8.7% to 6.3% [FACT; ch19-S10, VERIFIED-SECONDARY].

### 19.4.7 Valuation by expected resale only

For an asset with no interim cash flow and required return $k$,

$$V_0 = \frac{E_0[P_T]}{(1+k)^T}.$$

Apply the same equation at $T$: $P_T = E_T[P_{T+n}]/(1+k)^n$. With no cash flows, iterating forward never reaches a fundamental. Every price path $P_t = P_0(1+k)^t$ satisfies the equation. For an asset with cash flows $CF_t$, the general solution is

$$P_t = \underbrace{\sum_{j\ge 1} \frac{E_t[CF_{t+j}]}{(1+k)^j}}_{F_t:\ \text{fundamental}} + \underbrace{B_t}_{\text{bubble}}, \qquad E_t[B_{t+1}] = (1+k) B_t.$$

When $CF \equiv 0$, $F_t = 0$ and the whole price has the same form as the bubble term: it must be expected to grow at $k$ forever, which requires an ever-larger pool of buyers. This does not prove the price is "wrong". Money itself has no cash flow and a positive value supported by expected acceptance. It does mean that the only anchor is the belief that future buyers will keep paying, and that belief can shift without any change in a measurable fundamental. Monetary assets add a demand anchor (transaction and store-of-value use); the question for a non-yielding token is whether such demand exists at the current price, independent of speculation.

### 19.4.8 The scored framework

Score asset $j$ on dimensions $d = 1,\dots,9$ with integer scores $s_{jd} \in \{1,\dots,5\}$, where 5 is the most anchored and least hazardous to an owner (for transaction costs, reflexivity and tail risk, 5 means low). Report three statistics, not one:

* **Composite**: $S_j = \sum_d s_{jd}$ (out of 45). A crude summary.
* **Weakest link**: $\min_d s_{jd}$. A score of 1 on custody or tail risk can dominate everything else.
* **Profile distance from CRE**: $L1_j = \sum_d |s_{jd} - s_{CRE,d}|$. Two assets with equal composites can be far apart in profile.

Add an **anchor sub-score**: cash flow + valuation anchor + reflexivity + tail risk (out of 20). It isolates the dimensions that determine whether a price can be checked against something other than other buyers.

---

## 19.5 Worked examples

All inputs are [HYPOTHESIS] unless a source is cited. Every number is reproduced in `tests/test_ch19_examples.py`.

### Example 19.1 — Venture capital: the mean fund and the median fund

**Given.** Each seed deal returns one of five gross multiples:

| Multiple | 0x | 1x | 3x | 10x | 50x |
|---|---|---|---|---|---|
| Probability | 0.45 | 0.30 | 0.15 | 0.08 | 0.02 |

A fund makes $n = 20$ equal-sized, independent investments. Ignore fees and timing; treat the hold as 8 years for annualization.

**Find.** (a) The mean deal multiple and the share of it from the 50x outcome. (b) The mean, median, 25th, 75th and 90th percentiles of the fund multiple. (c) The probability that the fund has no 50x deal and its expected multiple in that case. (d) The probability the fund returns less than 1x, and less than its own mean. (e) Annualized equivalents of the mean and median.

**Solution.**

(a) $\mu = 0.45(0) + 0.30(1) + 0.15(3) + 0.08(10) + 0.02(50) = 0 + 0.30 + 0.45 + 0.80 + 1.00 = 2.55\text{x}$. The 50x outcome contributes $1.00/2.55 = 39.2\%$ of the mean from 2% of deals.

(b) The fund multiple is the average of 20 draws. Its exact distribution comes from enumerating the 10,626 ways to allocate 20 deals across five outcomes, each with its multinomial probability (`x_alt_assets.portfolio_multiple_distribution`):

| Statistic | Fund multiple |
|---|---|
| Mean | 2.55x |
| 25th percentile | 1.35x |
| **Median** | **1.95x** |
| 75th percentile | 3.65x |
| 90th percentile | 4.65x |

(c) $P(\text{no 50x}) = 0.98^{20} = 66.8\%$. Conditional mean $= (2.55 - 0.02 \times 50)/0.98 = 1.55/0.98 = 1.58\text{x}$.

(d) $P(\bar X_{20} < 1) = 10.6\%$. $P(\bar X_{20} < 2.55) = 61.9\%$: most funds underperform the average fund.

(e) Mean: $2.55^{1/8} - 1 = 12.41\%$ a year. Median: $1.95^{1/8} - 1 = 8.71\%$ a year.

**Check.** The enumerated mean equals $\mu = 2.55$ exactly, as it must. With $n = 5$, 10 and 40 the median is 1.40x, 1.70x and 2.425x (tests): the median rises toward the mean as $n$ grows, slowly.

**Decision consequence.** The "industry average" VC return is the return of a hypothetical investor who owns every fund. A family making one commitment owns one draw, and that draw is more likely than not to fall below the average. The difference between 12.4% and 8.7% a year is a property of the outcome distribution, before any question of skill or fees. Three consequences follow. First, compare a VC commitment with the **median** of the relevant distribution, not the pooled mean. Second, access to the managers who repeatedly capture the tail is the whole game; Kaplan and Schoar (2005) document persistence in fund returns [FACT; ch19-S01], which is why access matters and why it is scarce. Third, a single first-time manager with 20 seed deals (Proposal A) is a lottery-like position for the family even if its expected value is positive. Size it as such.

### Example 19.2 — Private equity: the J-curve, interim IRR, and TVPI versus DPI

**Given.** A buyout fund with \$100 million of commitments. LP net-of-fee flows (\$ million) at year-ends:

| Year | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| Calls $C_t$ | 25 | 25 | 20 | 15 | 5 | 0 | 0 | 0 | 0 |
| Distributions $D_t$ | 0 | 0 | 0 | 5 | 15 | 30 | 40 | 45 | 25 |

Reported NAV is \$62 million at end of year 2 and \$95 million at end of year 4.

**Find.** (a) Net flows and the cumulative net cash flow (the J-curve). (b) Interim DPI, RVPI, TVPI and IRR at years 2 and 4. (c) Final multiples and IRR.

**Solution.**

(a) Net flows $D_t - C_t$: $-25, -25, -20, -10, +10, +30, +40, +45, +25$. Cumulative: $-25, -50, -70, -80, -70, -40, 0, +45, +70$. The trough is $-80$ at year 3. Cumulative cash breaks even at year 6.

(b) Year 2: paid-in $= 70$, distributed $= 0$. DPI $= 0$, RVPI $= 62/70 = 0.886$, TVPI $= 0.886$. Interim IRR on $[-25, -25, -20 + 62] = [-25, -25, 42]$: **−11.08%**.

Year 4: paid-in $= 90$, distributed $= 20$. DPI $= 20/90 = 0.222$, RVPI $= 95/90 = 1.056$, TVPI $= 1.278$. Interim IRR on $[-25, -25, -20, -10, 10 + 95]$: **9.97%**.

(c) Final: paid-in 90, distributed 160. DPI = TVPI $= 160/90 = 1.778$. IRR on the full vector: **13.14%**.

**Check.** At year 4, RVPI is 83% of TVPI ($1.056/1.278$): the interim figure is mostly an appraisal. The final DPI of 1.778 can be checked by hand: $5 + 15 + 30 + 40 + 45 + 25 = 160$. A common spreadsheet error is to compute the multiple from the *net* annual flows: netting year 3 (−15 + 5) and year 4 (−5 + 15) leaves total outflows of 80 and inflows of 150, so the "multiple" is $150/80 = 1.875$ instead of 1.778. Calls and distributions must be summed separately.

**Decision consequence.** At year 2 the fund "looks" like a loser (−11%) and at year 4 like a 10% fund. Neither figure is evidence about manager skill: the first is the arithmetic of fees and calls before exits; the second is 83% NAV estimate. An LP who must report quarterly will see the J-curve in its own performance and should budget for it. In 2022, when public markets fell before private NAVs were marked down, many LPs found their private allocations above target weights because of the lag rather than any outperformance (the "denominator effect") [INFERENCE; widely discussed in industry commentary, specific figures not used]. The same lag is why a secondary buyer must re-mark NAV before calling a price a discount (Example 19.4).

### Example 19.3 — Kaplan–Schoar PME for the same fund

**Given.** The flows in Example 19.2 and a total-return public index at the same year-ends:

| Year | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| $I_t$ | 100 | 112 | 105 | 120 | 135 | 128 | 150 | 165 | 160 |

**Find.** (a) KS-PME. (b) The index's annual return. (c) The mirror-account balance at year 8. (d) KS-PME if the index had instead risen steadily to 215.

**Solution.**

(a) Contributions in index units (×100 for readability, i.e. $\sum C_t\, I_0/I_t$):
$25(1) + 25(100/112) + 20(100/105) + 15(100/120) + 5(100/135) = 25 + 22.321 + 19.048 + 12.500 + 3.704 = 82.573.$

Distributions in index units:
$5(100/120) + 15(100/135) + 30(100/128) + 40(100/150) + 45(100/165) + 25(100/160)$
$= 4.167 + 11.111 + 23.438 + 26.667 + 27.273 + 15.625 = 108.280.$

$KS\text{-}PME = 108.280/82.573 = \mathbf{1.311}.$

(b) Index: $(160/100)^{1/8} - 1 = 6.05\%$ a year.

(c) Mirror account at year 8: $-41.1$. The fund paid out more than an index account fed with the same calls could have funded.

(d) With the index path $100, 115, 130, 140, 160, 175, 190, 205, 215$: KS-PME $= 1.115$.

**Check.** Compounding every flow forward to year 8 instead (multiplying by $I_8/I_t$) gives the same ratio, because numerator and denominator are scaled by the same constant $I_8/I_0$ (tested).

**Decision consequence.** TVPI of 1.78 says the LP got back \$1.78 per dollar. KS-PME of 1.31 says it got back 1.31 times what the index would have delivered on the same schedule. Against the stronger index path the premium shrinks to 1.12, before any adjustment for buyout leverage. The question for the committee is whether a 12–31% cumulative advantage over eight years, before risk adjustment, pays for illiquidity, a ten-year lock-up and the J-curve. That is a judgment, not an identity. It is the right question; "TVPI 1.78x" is not an answer to it.

### Example 19.4 — A liquidity-adjusted return with a stale-price correction

**Given.** A private fund reports annual NAV returns $r^*_0, \dots, r^*_6$ of 9%, 11%, 10%, 6%, −1%, 2%, 8%. Assume first-order smoothing with $a = 0.5$. The risk-free rate is 3%. The latest NAV of \$100 million was struck at the last quarter-end. Since then a listed index of comparable companies has fallen 20%, and the fund's assets have a beta of 1.2 to that index. A secondary buyer bids 85% of NAV. Separately, for a new 5-year commitment the committee expects a gross return of 9% a year, a 25% probability of a forced early sale, and a 20% secondary haircut if forced.

**Find.** (a) Unsmoothed returns $r_1, \dots, r_6$. (b) Mean, standard deviation and Sharpe ratio, reported versus unsmoothed. (c) The end-point check. (d) The corrected NAV and the bid against it. (e) The liquidity-adjusted annual return.

**Solution.**

(a) $r_t = (r^*_t - 0.5\,r^*_{t-1})/0.5$:
* $r_1 = (0.11 - 0.045)/0.5 = 13.0\%$
* $r_2 = (0.10 - 0.055)/0.5 = 9.0\%$
* $r_3 = (0.06 - 0.050)/0.5 = 2.0\%$
* $r_4 = (-0.01 - 0.030)/0.5 = -8.0\%$
* $r_5 = (0.02 + 0.005)/0.5 = 5.0\%$
* $r_6 = (0.08 - 0.010)/0.5 = 14.0\%$

(b) Reported (years 1–6): mean 6.00%, sample s.d. 4.69%, Sharpe $(6.00 - 3.00)/4.69 = 0.64$. Unsmoothed: mean 5.83%, s.d. 8.18%, Sharpe $(5.83 - 3.00)/8.18 = 0.35$. The unsmoothed volatility is 1.74 times the reported volatility. For i.i.d. true returns the theoretical ratio is $1/\sqrt{(1-a)/(1+a)} = 1/0.577 = 1.73$.

(c) Sums: reported $0.36$, unsmoothed $0.35$. End-point term: $\frac{0.5}{0.5}(0.08 - 0.09) = -0.01$. ✓

(d) $\widehat V = 100 \times (1 + 1.2 \times (-0.20)) = 100 \times 0.76 = \$76.0$ million. The bid of \$85.0 million is $85/76 - 1 = $ **+11.8% above** corrected value.

(e) $r_{LA} = 1.09 \times (1 - 0.25 \times 0.20)^{1/5} - 1 = 1.09 \times 0.95^{0.2} - 1 = 1.09 \times 0.98979 - 1 = 7.89\%$.

**Check.** The cumulative reported return (41.1%) and unsmoothed return (38.4%) differ by less than the annual noise, consistent with the end-point identity.

**Decision consequence.** Three corrections, each ordinary, change the picture. Unsmoothing halves the Sharpe ratio from 0.64 to 0.35. The stale-price correction turns a "15% discount" into an 11.8% premium (Proposal B): the seller, not the buyer, is being paid. The liquidity adjustment removes about 1.1 percentage points a year from the gross return, and more for an owner who would be forced in a bad state. A family that holds CRE, whose own appraisals smooth in the same way (Chapter 2), should not add a second smoothed asset and conclude that its portfolio volatility has fallen.

### Example 19.5 — The transaction-cost hurdle for a painting

**Given.** Hammer price $H_0 = \$2{,}000{,}000$. Buyer's premium schedule: 27% up to \$1 million, 22% from \$1 million to \$8 million, 15% above \$8 million. (This matches the Sotheby's schedule reported as effective in February 2025 [FACT; ch19-S12, VERIFIED-SECONDARY]; schedules change frequently, and the calculation is illustrative.) Ignore sales tax and import duties. Carrying cost (insurance, storage, conservation) 0.6% of the purchase cost a year, paid at year-ends. Resale through auction after 5 years with a seller's commission plus deductions of $s = 11\%$ of hammer. Required return $k = 7\%$.

**Find.** (a) Buyer's premium, total paid and the effective premium rate. (b) The immediate round-trip cost. (c) The hammer price needed to break even in nominal dollars and to earn 7%, and the annual hammer-price growth each requires. (d) The IRR if hammer prices grow 5% a year.

**Solution.**

(a) Premium $= 0.27 \times 1{,}000{,}000 + 0.22 \times 1{,}000{,}000 = 270{,}000 + 220{,}000 = \$490{,}000$. Total paid $P^{buy} = \$2{,}490{,}000$. Effective rate $= 490{,}000/2{,}000{,}000 = 24.5\%$.

(b) Resale tomorrow at the same hammer: seller receives $2{,}000{,}000 \times 0.89 = \$1{,}780{,}000$. Round-trip cost $= 1 - 1{,}780{,}000/2{,}490{,}000 = 28.5\%$.

(c) Carrying cost $m = 0.006 \times 2{,}490{,}000 = \$14{,}940$ a year.

* Nominal break-even: $H_5 = (2{,}490{,}000 + 5 \times 14{,}940)/0.89 = 2{,}564{,}700/0.89 = \$2{,}881{,}685$; growth $(2{,}881{,}685/2{,}000{,}000)^{1/5} - 1 = 7.58\%$ a year.
* At 7%: $P^{buy}(1.07)^5 = \$3{,}492{,}354$. FV of carrying $= 14{,}940 \sum_{t=1}^{5} 1.07^{5-t} = \$85{,}916$. $H_5 = (3{,}492{,}354 + 85{,}916)/0.89 = \$4{,}020{,}528$; growth $= (4{,}020{,}528/2{,}000{,}000)^{1/5} - 1 = $ **14.99%** a year.

(d) Hammer growth 5%: $H_5 = 2{,}000{,}000 \times 1.05^5 = \$2{,}552{,}563$; net $= \$2{,}271{,}781$. Flows: $-2{,}490{,}000$; $-14{,}940$ in years 1–4; $2{,}271{,}781 - 14{,}940$ in year 5. IRR $= -2.44\%$.

**Check.** `x_microstructure.round_trip_cost(0.245, 0.11)` returns the same 28.5%.

**Decision consequence.** "Blue-chip art has returned 8–9%" (Proposal C) is a claim about hammer-to-hammer changes in a selected sample. A buyer at a \$2 million hammer needs about 7.6% a year of hammer growth just to get her money back in five years, and about 15% a year to earn 7%. A 5% index return, which is not far below the selection-corrected estimates in the literature, produces a loss. The only ways to change this arithmetic are a longer hold (the fixed round trip is spread over more years), lower costs (private sale, negotiated premiums, a guarantee), or a non-financial dividend (the pleasure of owning the work), which is real but should be named as consumption, not return.

### Example 19.6 — A repeat-sales index and selection bias

**Given.** Six paintings sold twice across periods 0, 1, 2 (log price relatives $y$):

| Item | Bought | Sold | $y$ |
|---|---|---|---|
| A | 0 | 1 | 0.10 |
| B | 0 | 2 | 0.25 |
| C | 1 | 2 | 0.12 |
| D | 0 | 1 | 0.06 |
| E | 1 | 2 | 0.20 |
| F | 0 | 2 | 0.15 |

Separately, ten works were bought at period 0. Their true log changes to period 2 are −0.30, −0.20, −0.10, 0.00, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40. Owners resell only if the change is at least +0.10, except one estate that must sell the −0.30 work.

**Find.** (a) The repeat-sales index. (b) The mean change of resold works versus the population.

**Solution.**

(a) Regressors $(x_1, x_2)$: A, D: $(1, 0)$; B, F: $(0, 1)$; C, E: $(-1, 1)$. Normal equations:

$S_{11} = 4$, $S_{22} = 4$, $S_{12} = -2$; $\sum x_1 y = 0.10 + 0.06 - 0.12 - 0.20 = -0.16$; $\sum x_2 y = 0.25 + 0.15 + 0.12 + 0.20 = 0.72$.

$\det = 4 \times 4 - (-2)^2 = 12$. $\beta_1 = (-0.16 \times 4 - 0.72 \times (-2))/12 = (-0.64 + 1.44)/12 = 0.0667$. $\beta_2 = (4 \times 0.72 - (-2)(-0.16))/12 = (2.88 - 0.32)/12 = 0.2133$.

Index: $100,\ 100e^{0.0667} = 106.9,\ 100e^{0.2133} = 123.8$.

(b) Population mean $= 0.60/10 = 0.060$. Resold: $-0.30, 0.10, 0.15, 0.20, 0.30, 0.40$, mean $= 0.85/6 = 0.142$. Bias $= +0.082$ in log terms over two periods.

**Check.** $\beta_1$ is pulled between the direct 0→1 evidence (mean 0.08) and the indirect evidence $\beta_2 - (1\to 2\text{ mean } 0.16)$. The OLS solution reconciles both.

**Decision consequence.** The repeat-sales method solves the quality-mix problem (each work is compared with itself) but not the selection problem. The resold sample more than doubles the true average change. The CRE analog is the transaction-based index in a downturn, when owners of impaired buildings do not sell (Chapter 2 §2.2). For art the effect is permanent rather than cyclical: losers are rarely consigned, they are kept, sold privately, or bought in. Any art return claim should state whether it is selection-corrected and whether it is measured hammer-to-hammer or premium-inclusive.

### Example 19.7 — An asset with no cash flow, valued only by expected resale

**Given.** A token (or NFT, or speculative collectible) produces no cash flow to its holder. A buyer forms a three-year view: with probability 0.50 demand persists and the price is 150; with 0.35 interest fades and the price is 60; with 0.15 the market collapses and the price is 5. Required return 15%. For comparison, a stabilized building with NOI of 6.0 at a 6.0% cap rate.

**Find.** (a) The value today. (b) Its sensitivity to $k = 25\%$ and to a shift of 0.10 probability from the good to the collapse scenario. (c) The price path a buyer at 80 needs to earn 15%. (d) The building's value and its response to a 50 bp cap-rate rise.

**Solution.**

(a) $E[P_3] = 0.50(150) + 0.35(60) + 0.15(5) = 75 + 21 + 0.75 = 96.75$. $V_0 = 96.75/1.15^3 = 96.75/1.520875 = 63.61$.

(b) At $k = 25\%$: $96.75/1.953125 = 49.54$ (−22%). With probabilities $(0.40, 0.35, 0.25)$: $E[P_3] = 60 + 21 + 1.25 = 82.25$, $V_0 = 54.08$ (−15%).

(c) $P_t = 80 \times 1.15^t$: 121.67 at year 3, 323.64 at year 10, 1,309.32 at year 20.

(d) Building: $6.0/0.06 = 100.0$. At 6.5%: $6.0/0.065 = 92.31$ (−7.7%). The owner still receives 6.0 a year whatever the cap rate.

**Check.** Each scenario price at year 3 must itself equal the year-3 expectation of a later resale discounted at $k$ (§19.4.7). Nothing in the problem pins down those later prices; the inputs 150/60/5 are beliefs about beliefs.

**Decision consequence.** Every input to the token's value is an opinion about other buyers. A 10-point change in the required return moves value 22%. A 10-point shift in scenario probability moves it 15%. Neither input can be checked against rent, replacement cost or a lender's sizing. The building's value also moves with its discount rate, but it pays 6.0 a year to a holder who never sells, and a buyer at 100 can check the cap rate against Treasuries (Chapter 6) and recent trades. A buyer at 80 for the token needs the price to reach about 324 in ten years and 1,309 in twenty, which requires an ever-growing pool of buyers or a non-speculative source of demand. The disciplined response is not to call such assets worthless. It is to size them as positions whose value can fall toward zero without any observable change in a fundamental, and to refuse leverage against them.

### Example 19.8 — Development land: an anchor that exists but is levered

**Given.** A 40-acre parcel (Proposal E) priced at \$2.5 million, with no income. Carry (taxes, insurance, maintenance) 1.5% of price, \$37,500 a year, paid at year-ends. Required return 12%. In three years the parcel is either entitled (probability 0.60) or not (value \$1.5 million as agricultural or rural-residential land). If entitled, it is worth its residual value: gross development value (GDV) \$60 million, selling costs 2%, hard costs \$38 million, soft costs \$6 million, financing \$3 million, developer margin 15% on cost.

**Find.** (a) The entitled residual land value. (b) Its value if GDV is 5% lower. (c) The present value of the parcel at 12% and the break-even entitlement probability at a \$2.5 million price.

**Solution.**

(a) Net GDV $= 60 \times 0.98 = 58.8$. $L = 58.8/1.15 - (38 + 6 + 3) = 51.130 - 47.0 = \$4.130$ million.

(b) GDV \$57 million: $55.86/1.15 - 47.0 = \$1.574$ million (−61.9% for a 5% change in GDV).

(c) $E[V_3] = 0.6 \times 4.130 + 0.4 \times 1.5 = \$3.078$ million. PV $= 3.078/1.12^3 - 37{,}500 \times a_{\bar 3|12\%} = 2.191 - 0.090 = \$2.101$ million.

Break-even probability: $p^* = \dfrac{2.5(1.12)^3 + FV(\text{carry}) - 1.5}{4.130 - 1.5} = \dfrac{3.512 + 0.127 - 1.5}{2.630} = 81.3\%.$

**Check.** `cre.residual_land_value` reproduces (a) and (b). With the 5% lower GDV and $p = 0.6$, PV falls to \$1.009 million.

**Decision consequence.** Land has an anchor that a token lacks: a residual computed from rents, cap rates and construction costs that can be checked. But the anchor is levered: residual value is a small difference between two large numbers, so it moves about 12 times as much as GDV. At \$2.5 million the purchase needs an 81% entitlement probability to earn 12%. The family should bid no more than about \$2.1 million at a 60% view, or pay for an option on the land (Chapter 13; Case I) rather than own it, so that the carry and the entitlement risk are not both borne up front.

### Example 19.9 — The nine-dimension score, and why equal totals do not mean equal assets

**Given.** Scores (1–5; 5 = most anchored, least hazardous to the owner). All scores are [HYPOTHESIS]: they are the author's teaching judgments, to be challenged, not measurements.

| Asset | Cash flow | Anchor | Financing | Liquidity | Custody/rights | Transparency | Trans. costs | Reflexivity | Tail risk |
|---|---|---|---|---|---|---|---|---|---|
| Core CRE | 4 | 4 | 5 | 2 | 5 | 3 | 3 | 3 | 3 |
| Development land | 1 | 3 | 2 | 1 | 5 | 2 | 2 | 2 | 2 |
| PE buyout LP interest | 3 | 3 | 2 | 1 | 4 | 2 | 2 | 3 | 3 |
| VC LP interest | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 2 | 2 |
| Bitcoin | 1 | 1 | 3 | 5 | 3 | 3 | 5 | 1 | 1 |
| Other tokens and NFTs | 1 | 1 | 1 | 2 | 2 | 2 | 3 | 1 | 1 |
| Fine art | 1 | 2 | 2 | 1 | 4 | 1 | 1 | 3 | 2 |
| Compliance allowances | 1 | 3 | 3 | 4 | 4 | 4 | 4 | 3 | 2 |
| Voluntary offsets | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 1 |

**Find.** Composite (out of 45), weakest link, L1 distance from core CRE, and anchor sub-score (cash flow + anchor + reflexivity + tail, out of 20).

**Solution.**

| Asset | Composite | Weakest link | L1 from CRE | Anchor sub-score |
|---|---|---|---|---|
| Core CRE | 32 | 2 | 0 | 14 |
| Compliance allowances | 28 | 1 | 12 | 9 |
| PE buyout LP interest | 23 | 1 | 9 | 12 |
| Bitcoin | 23 | 1 | 19 | 4 |
| Development land | 20 | 1 | 12 | 8 |
| Fine art | 17 | 1 | 15 | 8 |
| VC LP interest | 16 | 1 | 16 | 7 |
| Other tokens and NFTs | 14 | 1 | 18 | 4 |
| Voluntary offsets | 13 | 1 | 19 | 5 |

Bitcoin's composite: $1+1+3+5+3+3+5+1+1 = 23$. Its L1 distance from CRE: $3+3+2+3+2+0+2+2+2 = 19$.

**Check.** The PE interest and bitcoin tie at 23. Their L1 distance from each other is $2+2+1+4+1+1+3+2+2 = 18$.

**Decision consequence.** A composite ranks bitcoin level with a buyout LP interest. The profiles show they are nearly opposite: the LP interest is illiquid and opaque but anchored in company cash flows (anchor sub-score 12); bitcoin is liquid and cheap to trade but has no cash-flow anchor and high reflexivity (sub-score 4). They fail in different states and require different controls: the LP interest needs a liquidity budget; bitcoin needs a loss budget and a custody standard. The framework's job is to say which controls an asset needs, not to rank assets on one scale. Any committee presentation that reports only the composite misuses it.

---

## 19.6 The markets one by one, against CRE

This section uses the nine dimensions to compare each market with stabilized CRE. Scores refer to Example 19.9.

### 19.6.1 Cryptocurrency (bitcoin)

**Cash flow and anchor.** None in the CRE sense. Proposed anchors include miners' marginal cost of production, network-adoption models, and a quantity-theory share of a store-of-value market. Each is weak. Production cost follows price, because mining difficulty adjusts to price-driven hashrate, rather than anchoring it [INFERENCE from the protocol's difficulty adjustment]. Adoption models fit past prices to user counts and have no out-of-sample discipline. A store-of-value share is a belief about what others will hold.

**Liquidity and costs.** High and cheap in normal conditions, with continuous trading on many venues. Liquidity is concentrated in venues whose solvency the trader must judge (§19.9).

**Custody and rights.** Bearer-like: whoever controls the private key controls the coin. Self-custody removes custodian risk and adds operational risk (loss of keys). Exchange custody adds counterparty risk: in an exchange insolvency a customer may be an unsecured creditor, depending on the terms of service and jurisdiction [INFERENCE; this was litigated in the 2022 bankruptcies].

**Reflexivity and tail risk.** Very high. Rising prices raise collateral values on crypto-lending platforms and derivatives venues, which supports more leveraged buying; falling prices trigger liquidations that sell into the decline (Chapter 3's collateral loop, with automated margin rather than appraisals). Historical drawdowns of 70–80% are documented in §19.9.

**Against CRE.** Higher liquidity, lower costs and much weaker anchors. A CRE investor should not use crypto's liquidity as a reason to treat it as a cash substitute: liquidity is high in the asset's price, not in its value.

### 19.6.2 Digital assets beyond bitcoin

Tokens issued by projects, stablecoins, and NFTs add issuer and design risk. A **governance token** may confer votes but no cash-flow claim. A **staking reward** is paid in the same token and is partly funded by new issuance, so it is closer to a stock dividend than to rent [INFERENCE]. A **stablecoin** is a claim whose value depends on the reserve and on redemption rights; an algorithmic stablecoin without full reserves is a reflexive structure by design (the TerraUSD collapse, §19.9). An **NFT** is a token pointing to an asset; whether it conveys any intellectual-property rights depends on its licence. Tokenized real-world assets (including tokenized real estate) inherit the rights of the legal wrapper that holds the underlying asset. The token is only as good as the legal claim on the deed.

### 19.6.3 Venture capital

**Cash flow.** Little until exit. **Anchor.** Weak: venture rounds are priced by the next investor, and headline post-money valuations are often inflated by preferred-stock terms, so they overstate the value of common equity [INFERENCE]. **Outcome distribution.** Power-law (Example 19.1). Cochrane (2005) shows that correcting for the fact that only successful companies report valuations reduces estimated mean arithmetic returns from 698% to 59% [FACT; ch19-S03, VERIFIED-SECONDARY via abstract]. **Against CRE.** VC is the opposite of core CRE: a small number of outcomes deliver almost all the value, and a typical investment is expected to lose money. The CRE analog is not stabilized property but ground-up development in an untested submarket, with the difference that a failed building still has land value.

### 19.6.4 Private equity (buyout)

**Cash flow.** Portfolio companies generate cash; LPs receive it only through distributions. **Anchor.** Enterprise value from EBITDA multiples, checkable against public comparables. **Financing.** Heavy at portfolio level; at LP level, NAV lending and subscription lines. **Liquidity.** Ten-year commitment; secondary sales at a discount or premium to stale NAV. **Transparency.** Quarterly NAV, smoothed and lagged (Examples 19.2–19.4). **Against CRE.** The closest relative in the group. A closed-end real estate fund has the same J-curve, the same IRR-versus-multiple issues and the same appraisal lag. Everything in Examples 19.2–19.4 applies to a value-add CRE fund commitment.

### 19.6.5 Development land

Treated in Example 19.8. Land is CRE, but it is CRE stripped of its cash flow and with a levered residual anchor. It is the CRE asset most like an option (Chapter 13; Titman, 1985), and its value is most sensitive to credit availability: when construction lending stops, the residual falls even if rents do not, because the financing cost and the required margin rise.

### 19.6.6 Collectibles and fine art

**Cash flow.** None (some works earn loan fees from museums; negligible). **Anchor.** Weak: no replacement cost; comparable sales of the same artist and period, adjusted for size, condition and provenance. **Costs.** The highest in the group (Example 19.5). **Measurement.** Repeat-sales indices (Mei and Moses, 2002; Goetzmann, 1993) control for quality but suffer from selection (Example 19.6). Mei and Moses (2002) report that art outperformed fixed income but underperformed U.S. stocks over 1875–2000, and that expensive works ("masterpieces") underperformed the art index [FACT; ch19-S09, VERIFIED-SECONDARY]. **Reflexivity.** Moderate: prices of an artist's work are set by a small group of dealers, collectors and auction guarantors whose interests are aligned with high prices; guarantees and irrevocable bids make some public sale prices partly negotiated outcomes [INFERENCE]. Other collectible markets (cars, watches, sports cards, wine, whisky casks) share the profile, with thinner data and, for perishable goods, storage and authentication risk.

### 19.6.7 Carbon credits

**Compliance allowances** (for example the EU Emissions Trading System and the California cap-and-trade program) are permits created by regulation. Covered emitters must surrender allowances or pay a penalty, so demand is legally compelled, and the cap fixes supply. The economic anchor is the marginal abatement cost at the cap, which is uncertain but analyzable. Exchange-traded futures give liquidity and transparency. The tail risk is political: a government can change the cap, the reserve mechanisms or the coverage, which can move prices sharply without any change in emissions [INFERENCE]. **Voluntary offsets** have no compliance demand in most cases. Their value depends on project quality (additionality, permanence, leakage, baseline integrity) and on buyers' reputational needs. Investigative reporting and academic studies have questioned whether some forest-protection offsets represent real reductions *(verification pending: specific studies and figures not used here)*. A voluntary offset is closer to an unaudited receivable than to a commodity. **Against CRE.** Compliance allowances score higher than most alternatives (Example 19.9) because the anchor, liquidity and transparency are real. They have no cash flow and their key risk is policy, which is the closest analogy to CRE zoning risk.

### 19.6.8 Other expectation-driven, liquidity-scarce markets

| Market | What anchors price | Main hazard | CRE analog |
|---|---|---|---|
| Pre-IPO secondary shares | Last round price; expected IPO | Transfer restrictions, information asymmetry, preference stack | Buying an LP interest without the books |
| SPAC warrants and units | Trust value floors the unit; warrants are options on a deal not yet announced | Redemptions, dilution, deal failure | Option on unentitled land |
| Domain names, in-game items | Expected resale | Platform and rights risk | None |
| Music and film royalties | Cash flow from royalties (an exception: a genuine income stream) | Decay rate of royalty income; small, opaque market | A net-leased asset with a decaying rent |
| Litigation finance | Expected judgment or settlement | Binary legal outcome, duration | Distressed-debt workout (Chapter 17) |
| Rare whisky casks, wine | Expected resale; consumption demand | Storage, authenticity, fraud | Collectible land without zoning |

The common thread: **when the anchor is expected resale, the analyst's question is who the next buyer is and why that buyer will pay more.** When the anchor is cash flow (royalties, litigation proceeds), the asset is closer to CRE than its label suggests and should be valued as an income stream with its own decay and default risks.

---

## 19.7 CRE application: what the alternatives teach about CRE

**CRE contains its own alternatives.** Land banking, ground-up development, hotel turnarounds and recapitalizations of distressed office have more in common with VC and land speculation than with core property. A CRE investor already makes speculative decisions; the nine dimensions make them explicit. A stabilized industrial building scores 4 on cash flow. The same building's development phase scores 1.

**CRE fund commitments are private-equity commitments.** A value-add CRE fund has a J-curve, interim IRRs driven by NAV estimates, and the same subscription-line effect on IRR. Before comparing a CRE fund's 15% target IRR with a REIT's total return, compute TVPI, DPI and a PME against a REIT index (Problem 19.4 shows the method).

**CRE NAVs are stale in the same way.** Example 19.4's correction applies to an open-end core fund in 2022–23 (Chapter 2 §2.9). A redemption queue is the open-end fund's version of the secondary discount.

**Tokenized CRE does not change CRE.** A token representing an interest in a property-owning entity has the property's cash flow and the entity's rights. It adds a custody and platform layer and, often, a thin secondary market. It does not create liquidity in the building. If the token trades at a premium to NAV because it is "liquid", the premium is a bet on the token market's continued depth [INFERENCE].

**Hotels sit between.** A hotel has cash flow but with high operating leverage (Chapter 11); its reflexivity and tail scores are closer to land than to apartments. The framework explains why a hotel family office can be "over-concentrated in real estate" and still not be diversified by adding assets whose bad states coincide with travel and credit shocks. Bitcoin's correlation with risk assets in 2022 is a reminder that "uncorrelated" in calm data says little about behavior in a liquidity crisis [INFERENCE from the 2022 price path, §19.9].

---

## 19.8 When the relationship fails

1. **The anchor itself moves.** CRE's cash-flow anchor fails when cash flow is not durable (office after 2020; Chapter 12). A compliance allowance's regulatory anchor fails when policy changes. The framework scores an anchor's existence, not its permanence; add a judgment about durability.
2. **Liquidity scores invert in a crisis.** Bitcoin scores 5 on liquidity. During an exchange failure, coins on that exchange had zero liquidity to their owners. Liquidity is a property of the market and the custody chain, not of the asset.
3. **PME and multiples can mislead together.** A fund with high leverage can beat the index on KS-PME in a rising market purely through beta. A fund with a short life can have a high IRR and low TVPI. Report IRR, TVPI, DPI and a PME, and state the benchmark beta.
4. **Selection correction depends on a model.** Korteweg, Kräussl and Verwijmeren's correction requires a model of the sale decision. A different model gives a different number. The direction of the bias is robust; its size is not.
5. **Power laws can change shape.** Example 19.1 assumes a fixed outcome distribution. If capital flows into VC and pushes up entry prices, the right tail shrinks and the mean falls with it (Kaplan and Schoar, 2005, document procyclical entry [FACT; ch19-S01]).
6. **"No cash flow" does not imply "no value".** Gold and fiat money have positive values without cash flow, supported by demand that is partly non-speculative. A resale-only valuation is weak, not necessarily wrong. The error is pretending it is anchored.
7. **Scores are judgments.** Two careful analysts could disagree by one point on several cells. The method's value is that disagreements become explicit and testable.

---

## 19.9 Historical episode: the 2021–22 crypto boom and collapse

**Date and environment.** In 2020–21, U.S. policy rates were near zero and asset prices broadly rose (Chapter 5). Crypto prices rose sharply. Bitcoin reached an all-time high of about \$69,000 on 10 November 2021 [FACT; ch19-S13, VERIFIED-SECONDARY: sources report peaks between \$68,789 and \$69,044 depending on venue], when total crypto-asset market capitalization was reported at close to \$3 trillion [FACT; ch19-S13, VERIFIED-SECONDARY]. NFT trading volume in 2021 was estimated by DappRadar at roughly \$23–26 billion, against about \$95 million in 2020 [FACT; ch19-S14, VERIFIED-SECONDARY; estimates differ by source and methodology]. OpenSea's Ethereum volume reached a monthly record of roughly \$5 billion in January 2022 [FACT; ch19-S14, VERIFIED-SECONDARY], with contemporaneous reporting noting that a material share of some NFT volume reflected wash trading [INFERENCE; the share is not established here].

**What was knowable at the time.** Most of the system's leverage and custody arrangements were opaque. Public information included: the existence of high-yield crypto deposit products; algorithmic stablecoins whose stability depended on arbitrage with a companion token; exchanges that were unregulated in the United States and also operated affiliated trading firms; and exchange-issued tokens used as collateral. What was not public was how much customer money was being lent to affiliates.

**The 2022 sequence.**

| Date (2022) | Event | Status |
|---|---|---|
| May | TerraUSD (UST), an algorithmic stablecoin, lost its dollar peg and UST and its companion token LUNA collapsed. The SEC later alleged the collapse wiped out at least \$40 billion of market value | [FACT that the SEC alleged this; ch19-S06, VERIFIED-SECONDARY. Allegations, not findings] |
| Late June | Three Arrows Capital entered liquidation in the British Virgin Islands after Terra-related losses and margin calls | [FACT; ch19-S07, VERIFIED-SECONDARY; exact date differs by source] |
| 5 July | Voyager Digital filed for Chapter 11 in the Southern District of New York, citing a \$650 million exposure to Three Arrows | [FACT; ch19-S07, VERIFIED-SECONDARY] |
| July | Celsius Network filed for Chapter 11 in the Southern District of New York after suspending withdrawals | [FACT; ch19-S07, VERIFIED-SECONDARY; exact filing date *(verification pending)*] |
| 2 November | CoinDesk reported a balance sheet of Alameda Research, the trading firm affiliated with the FTX exchange, showing about \$14.6 billion of assets of which a large share was FTX's own token, FTT (\$3.66 billion "unlocked FTT" and \$2.16 billion "FTT collateral"), against about \$8 billion of liabilities | [FACT that this was reported; ch19-S05, VERIFIED-SECONDARY via The Block] |
| 6 November | Binance's chief executive said Binance would sell its FTT holdings; Alameda's chief executive publicly offered to buy them at \$22 | [FACT; ch19-S05, VERIFIED-SECONDARY] |
| 11 November | FTX and over 100 affiliated entities filed for Chapter 11 in Delaware (Case No. 22-11068). John J. Ray III became chief executive | [FACT; ch19-S04, VERIFIED-SECONDARY] |
| 17 November | Ray's first-day declaration stated: "Never in my career have I seen such a complete failure of corporate controls and such a complete absence of trustworthy financial information as occurred here" | [FACT; ch19-S04, VERIFIED-SECONDARY: quotation as reproduced in reporting of the filing; to be checked against the docket text *(verification pending)*] |
| 13 December | The SEC and CFTC filed civil complaints against Samuel Bankman-Fried. The SEC alleged he diverted FTX customer funds to Alameda and that Alameda had a virtually unlimited line of credit funded by customers and exemption from FTX's risk controls. The CFTC alleged the loss of over \$8 billion of customer deposits and that customers' fiat deposits were directed to bank accounts controlled by Alameda | [FACT that these were alleged; ch19-S02, ch19-S11, VERIFIED-SECONDARY] |

Bitcoin traded near \$15,500–15,800 at its November 2022 low [FACT; ch19-S13, VERIFIED-SECONDARY; sources differ], roughly 77% below its 2021 peak [INFERENCE: $15{,}800/69{,}000 - 1 = -77.1\%$]. On 2 November 2023 a jury convicted Bankman-Fried on seven counts of fraud and conspiracy, and on 28 March 2024 he was sentenced to 25 years in prison [FACT; ch19-S08, VERIFIED-SECONDARY].

**Mechanisms, mapped to the nine dimensions.**

* **Custody and ownership rights.** The CFTC and SEC allegations concern customers who believed they owned assets held on an exchange, while the exchange is alleged to have lent them to an affiliate. The asset (bitcoin) and the claim (an exchange account) were different things. A CRE analogy is a tenant's security deposit held by a landlord who spends it: the tenant's claim is only as good as the landlord's solvency.
* **Self-referential collateral.** An affiliate whose balance sheet was concentrated in a token issued by its sister exchange has collateral whose value falls exactly when the exchange's solvency is questioned [INFERENCE from the reported balance sheet]. Problem 19.10 and Drill D176 work through this structure.
* **Reflexivity.** Terra's design linked a stablecoin's peg to the market value of its companion token, a loop with gain above one once confidence fell (Chapter 3 §3.4.2 and Example 3.2: the stability condition). Lenders exposed to Terra-related losses then cut credit to others, as in a CRE credit crunch but compressed into weeks.
* **Transparency.** Prices were public and continuous. Balance sheets were not. A market can be transparent in prices and opaque in counterparties.

**Competing interpretations.** (1) *Fraud and governance failure*: the court record and conviction support this for FTX specifically. (2) *Leverage cycle*: rates rose sharply in 2022 and speculative assets of all kinds fell; crypto's decline began before FTX's failure and would have happened without it [INFERENCE: bitcoin had already fallen well below its peak before November 2022 *(exact path verification pending)*]. (3) *Design failure*: algorithmic stablecoins and token-collateralized lending are reflexive by construction. These interpretations are complementary rather than exclusive.

**What the case establishes.** That custody and counterparty structure can dominate asset-price risk; that self-issued collateral fails when it is needed; that a liquid market price provides no information about the solvency of the venue quoting it; and that alleged and proven misconduct must be distinguished (FTX's founder was convicted; the Terra allegations are SEC allegations as stated here).

**What it does not establish.** It does not establish a fundamental value for bitcoin or any token, high or low. It does not establish that crypto markets are inherently fraudulent: the convicted conduct was specific to identified firms. It does not establish how much of the 2022 price decline was caused by the failures rather than by the rise in interest rates.

**CRE connection.** The 1980s–90s Texas cycle (Chapter 23) involved lenders whose capital was invested in the collateral they lent against and who failed together when values fell. The structure in 2022 was similar; the speed was not.

---

## 19.10 Decision exercise: the alternatives sleeve

Return to §19.1. The family's CRE book is \$180 million, mostly Texas hotels and multifamily, financed at 55–65% LTV. The proposal is \$25 million across A–F.

For each proposal, write on `desk/investment_memos/decision_record_template.md`:

1. Its nine-dimension scores, and which one or two dimensions decide the decision.
2. The return measure you would require (median, not mean, for A; KS-PME and corrected NAV for B; premium-inclusive hurdle for C; loss budget for D; break-even entitlement probability for E; policy scenario for F).
3. The state of the world in which it would hurt the family most, and whether that state coincides with stress in the CRE book (higher rates, tighter credit, travel shock).
4. Size, funding source, and the condition under which you would sell or stop funding.
5. Whether to abstain.

**Rubric** (`problems/solutions/ch19_solutions.md` §Decision exercise). Full credit requires: (a) re-pricing B against a corrected NAV before treating the bid as a discount; (b) a median-based expectation and position size for A, with recognition that access, not the asset class, determines the outcome; (c) the transaction-cost hurdle for C and an explicit statement of consumption value if the family buys anyway; (d) for D, a custody standard, no leverage, and a size the family can lose entirely; (e) for E, a maximum bid near \$2.1 million or an option structure; (f) for F, a separation of compliance allowances (analyzable policy risk) from voluntary offsets (verification risk), with abstention on offsets absent independent verification; (g) a statement that the sleeve does not diversify the family's main risk (credit and liquidity conditions) as much as the pitch implies. There is no single correct allocation. Abstaining from most of the sleeve is defensible.

---

## 19.11 Frequent analytical errors

1. **Comparing a private-fund IRR with a public-market annual return.** Compute a PME, and report TVPI and DPI.
2. **Reading interim TVPI as performance.** Early TVPI is mostly NAV estimate (RVPI).
3. **Computing multiples from net annual flows.** Netting a call against a distribution in the same period understates paid-in capital and overstates TVPI (1.875 versus 1.778 in Example 19.2).
4. **Using the mean VC fund as the expected outcome of one commitment.** Use the median and the access-adjusted distribution.
5. **Calling a bid below stale NAV a discount.** Correct the NAV for public moves since the mark.
6. **Accepting smoothed volatility.** Unsmooth with a stated $a$ and test a second value.
7. **Ignoring buyer's and seller's premiums.** Round trips of 25–30% at auction require large hammer growth to break even.
8. **Trusting repeat-sales indices without asking about selection.** Resold items are not a random sample.
9. **Inventing an anchor for a resale-only asset.** If the only route to value is a later buyer, say so and size accordingly.
10. **Treating liquid price as liquid value.** A continuously quoted price says nothing about the solvency of the custodian.
11. **Ranking assets by a composite score.** Report the profile; equal totals can hide opposite risks.
12. **Accepting self-referential collateral at face value.** Collateral issued by the borrower or an affiliate should be haircut to near zero in a stress test.

---

## 19.12 Connections to other chapters

* Chapter 2: appraisal smoothing, the Geltner filter and selection bias in transaction indices (used in Examples 19.4 and 19.6).
* Chapter 3: reflexivity and collateral loops (crypto lending, Terra).
* Chapter 6: the risk-free alternative and cap-rate spreads used to anchor CRE in Example 19.7.
* Chapter 9: valuation anchors for CRE; residual land valuation.
* Chapter 13: real options, land as an option, and Case I.
* Chapter 17: credit, recovery and the position of unsecured creditors in an insolvency.
* Chapter 21: sizing positions whose value can fall toward zero (Kelly, loss budgets).
* Chapter 22: direct alpha and risk-adjusted private-fund performance.
* Chapter 23: historical episodes; the 1980s Texas cycle as a structural parallel to 2022.

---

## 19.13 One-page reference sheet

| Quantity | Formula |
|---|---|
| DPI, RVPI, TVPI | $\sum D/\sum C$; $NAV/\sum C$; DPI + RVPI |
| Interim IRR | IRR of $D_t - C_t$ with $NAV_T$ added at $T$ |
| KS-PME | $\big(\sum D_t/I_t + NAV_T/I_T\big)\big/\sum C_t/I_t$ |
| Portfolio mean | $E[\bar X_n] = \mu$ for all $n$ |
| No-tail probability | $(1-p_{\max})^n$ |
| Mean without tail | $(\mu - p_{\max}x_{\max})/(1-p_{\max})$ |
| Geltner filter | $r_t = (r^*_t - a r^*_{t-1})/(1-a)$ |
| End-point identity | $\sum r_t = \sum r^*_t + \frac{a}{1-a}(r^*_N - r^*_0)$ |
| Stale NAV | $\widehat V = NAV(1 + \beta R_m)$ |
| Liquidity-adjusted return | $(1+r)(1-\pi h)^{1/T} - 1$ |
| Tiered premium | $\sum_j b_j(\min(H,U_j) - U_{j-1})^+$ |
| Hammer hurdle | $H_T = [P^{buy}(1+k)^T + FV(m)]/(1-s)$ |
| Repeat sales | $y_i = \beta_s - \beta_b + \varepsilon_i$ |
| Resale-only value | $V_0 = E[P_T]/(1+k)^T$ |
| Bubble term | $E_t[B_{t+1}] = (1+k)B_t$ |
| Residual land | $L = GDV(1-s)/(1+m) - (H+S+F)$ |

**Nine dimensions:** cash flow · valuation anchor · financing · liquidity · custody/rights · transparency · transaction costs · reflexivity · tail risk. Report composite, weakest link, L1 distance from CRE and the anchor sub-score.

**Numbers to remember from this chapter (all [HYPOTHESIS] unless cited).** Median VC fund 1.95x vs mean 2.55x (Example 19.1). Art round trip at a \$2m hammer ≈ 28.5%; hammer growth needed for 7% ≈ 15% a year over five years (Example 19.5). A 15% "discount" to a NAV marked before a 20% market fall, at beta 1.2, is an 11.8% premium (Example 19.4). Selection correction lowers painting index returns from 8.7% to 6.3% (Korteweg et al., 2016; cited).

**Questions for any alternative.** What pays me if I never sell? Who is the next buyer and why will they pay more? Who holds the asset, and what is my claim if they fail? What does the return figure omit: fees, premiums, selection, smoothing, staleness?

---

## References for this chapter

All sources are recorded in `references/sources_ch19.md` with verification status.

* Bailey, M. J., Muth, R. F., and Nourse, H. O. (1963). "A Regression Method for Real Estate Price Index Construction." *Journal of the American Statistical Association*, 58(304), 933–942. *(Bibliographic details verification pending.)*
* Cochrane, J. H. (2005). "The Risk and Return of Venture Capital." *Journal of Financial Economics*, 75(1), 3–52.
* Goetzmann, W. N. (1993). "Accounting for Taste: Art and the Financial Markets over Three Centuries." *American Economic Review*, 83(5), 1370–1376. *(Bibliographic details verification pending.)*
* Kaplan, S. N., and Schoar, A. (2005). "Private Equity Performance: Returns, Persistence, and Capital Flows." *Journal of Finance*, 60(4), 1791–1823.
* Korteweg, A., Kräussl, R., and Verwijmeren, P. (2016). "Does It Pay to Invest in Art? A Selection-Corrected Returns Perspective." *Review of Financial Studies*, 29(4), 1007–1038. *(Volume and pages verification pending.)*
* Mei, J., and Moses, M. (2002). "Art as an Investment and the Underperformance of Masterpieces." *American Economic Review*, 92(5), 1656–1668.
* Titman, S. (1985). "Urban Land Prices under Uncertainty." *American Economic Review*, 75(3), 505–514.
* U.S. Securities and Exchange Commission (2022). *SEC v. Samuel Bankman-Fried*, complaint, S.D.N.Y., 13 December 2022; and SEC v. Terraform Labs Pte. Ltd. and Do Hyeong Kwon, complaint, S.D.N.Y., February 2023.
* U.S. Commodity Futures Trading Commission (2022). Press Releases 8638-22 (13 December 2022) and 8644-22 (21 December 2022), *CFTC v. Bankman-Fried, FTX Trading Ltd., and Alameda Research LLC*.
* *In re FTX Trading Ltd.*, Case No. 22-11068 (JTD) (Bankr. D. Del.), Declaration of John J. Ray III in Support of Chapter 11 Petitions and First Day Pleadings, 17 November 2022.
