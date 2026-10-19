# Chapter 6 — Fixed Income and the Cost of Capital

> **Status:** Complete (v1.0). Every number in the text, problems, and solutions is reproduced in `tests/test_ch06_examples.py`. Problems are in `problems/questions/ch06_problems.md` and solutions in `problems/solutions/ch06_solutions.md`. New library helpers are in `models/python/sdesk/x_rates.py`. Sources are in `references/sources_ch06.md`. Open verification items (flagged in the text as *(verification pending)*): the exact text of the 4 February 1994 FOMC statement, the dates and sizes of the March and August 1994 moves, and a recheck of the 2022 daily yield closes against FRED itself rather than a FRED-derived mirror.

## Learning objectives

After this chapter you should be able to:

1. Read Treasury quotes as a dealer does. Convert a bill's discount rate to its price, bond-equivalent yield, money-market yield, and effective annual yield. Convert a note's semiannual yield to an effective annual rate comparable with a monthly-pay mortgage. Read prices in 32nds and compute TIPS breakeven inflation.
2. Price a coupon bond and compute Macaulay duration, modified duration, convexity, and DV01, by formula, by HP-12C, in Excel, and in Python. Know when the duration approximation fails and by how much.
3. Construct and size a DV01-neutral curve trade. Name what it is exposed to (slope) and what it is not neutral to (convexity, financing, non-parallel moves at other tenors).
4. Derive forward rates from spot rates, decompose a long yield into expected short rates plus a term premium, and explain why the term premium is a model output, not an observation.
5. Compute carry and roll-down with worked numbers, and the yield rise that breaks even against them.
6. Decompose a credit spread into expected loss and premia, and size a spread-duration exposure.
7. Decompose the cap-rate/Treasury spread into a risk premium minus expected growth, and show with arithmetic why the spread is not a stable constant.
8. Compute the effective duration of a levered property's equity, and trace a rate rise through cap rates, loan constants, DSCR-sized proceeds, and refinancing.

---

## 6.1 Opening investment problem: one balance sheet, three rate exposures

You run the \$40 million discretionary account introduced in Chapter 1. On a Tuesday the investment committee asks one question about three proposals: *how much interest-rate risk are we taking, and are we paid for it?* All facts are [HYPOTHESIS].

**Proposal 1 — the Treasury note.** Buy \$20 million face of a new 5-year Treasury note at par with a 4.50% coupon. The 4-year point on the curve is 4.35%. A dealer will finance the position in repo at 4.00%. A junior analyst wants to lever it 5:1 "because it carries".

**Proposal 2 — the industrial building.** Buy a fully leased \$50 million distribution building at a 6.00% cap rate on \$3.0 million NOI after reserves. The lender offers a 65% LTV, 5-year fixed-rate loan at 6.00% on a 30-year amortization. The broker's memo says: "The cap rate is 160 bp over the 10-year Treasury. The long-run average spread is about 300 bp, so cap rates have room to *fall* relative to Treasuries." The 10-year Treasury yields 4.40%.

**Proposal 3 — the hedge.** A senior partner proposes shorting Treasury notes against the building "to lock in today's financing environment for the refinancing in year 5".

The three proposals look unrelated: a government bond, a warehouse, and a derivative overlay. They are one exposure in three forms. Each is a bet on the level and shape of the yield curve, on a spread to it, or on how a spread to it behaves when the curve moves. By the end of the chapter you will be able to state the DV01 of each, the break-even yield move for each, and what you would have to believe about cap-rate pass-through for the hedge in Proposal 3 to reduce risk rather than add a second speculation. Section 6.10 returns to the decision.

---

## 6.2 Economic intuition

### Yields are the price of time, and every asset is priced against them

A Treasury yield is the rate at which the market exchanges dollars today for dollars that the U.S. government promises to pay later. It contains no credit risk in the ordinary sense and very little liquidity risk at the benchmark tenors. It therefore serves as the base rate to which every other asset's required return is added. A cap rate, a mortgage coupon, an equity earnings yield and a hotel's discount rate all embed a Treasury yield plus compensation for other risks, minus expected growth where the cash flows grow.

This is the sense in which Treasury yields are the "cost of capital". They are not the cost of *your* capital. They are the opportunity cost against which your capital's use must be justified. When the 10-year yield rises 100 bp, a 6.00% cap rate does not automatically become 7.00%, but the hurdle a 6.00% income stream must clear has risen. Something must adjust: the cap rate, the growth forecast, the risk premium the buyer accepts, or the number of buyers.

### Duration is the time-weighted exposure to the discount rate

A bond's price is the present value of its cash flows. When the discount rate rises, distant cash flows lose more value than near ones because they are discounted over more periods. **Duration** measures the average time to the cash flows, weighted by their present values. It is also, after a small adjustment, the percentage price change per unit change in yield. A 10-year coupon note has a duration of about 8 years: a 1 percentage point rise in its yield costs about 8% of its price.

The same logic applies to any long-lived cash-flow stream. A stabilized property is a perpetuity-like claim. If its cap rate moves one-for-one with Treasuries, its effective duration to Treasury yields is $1/c$. At a 6% cap that is about 17 years, twice the duration of a 10-year note. If the cap rate moves only 0.6 for 1, the duration is 10. Either way, a stabilized property is a long-duration asset. Leverage then divides the equity's share of the capital structure into that duration: at 65% LTV, a property duration of 10 becomes an equity duration near 29 if the debt is floating. **The levered owner of a low-cap-rate building can hold more interest-rate risk per dollar than a holder of 30-year Treasury bonds.** Section 6.5.9 derives this and Example 6.9 computes it.

### Convexity: the curvature that helps the long and hurts the short

The price–yield curve of a non-callable bond is convex. Prices rise more when yields fall than they fall when yields rise by the same amount. Duration describes the tangent line. Convexity describes the bend. For small moves the bend is negligible. For the 200–300 bp moves of 1994 and 2022 it is several points of price. A position that is short convexity, such as a mortgage lender's book of prepayable loans, a short position in long bonds, or a DV01-neutral steepener that is short the longer, more convex leg, loses slightly on large moves in either direction.

### The yield curve: expectations plus a premium

The curve's slope reflects two things that cannot be observed separately: the expected path of short-term policy rates, and the extra compensation investors demand for locking money up at a fixed rate for longer, the **term premium**. A steep curve can mean the market expects the central bank to raise rates, or it can mean investors demand a large premium for duration risk, or both. An inverted curve usually means the market expects cuts. Chapter 5 develops the policy-expectations side. This chapter treats the premium and shows why every published estimate of it is a model output that can differ across models by enough to change a trading conclusion.

### Carry and roll-down: what you earn if nothing happens

A bond position earns its coupon and pays its financing. That difference is **carry**. If the curve is upward-sloping and does not move, a bond also "rolls down" the curve: as it ages, it is priced at the lower yield of a shorter maturity, and its price rises. Carry plus roll-down is the return to a bet that *nothing changes*. It is a real source of return. It is also the payment for a short option on curve moves: the larger the carry and roll, the larger the yield rise it can absorb, but there is always a rise that takes it away.

### Cap rates are real-asset yields with growth

A Treasury pays a fixed nominal coupon. A building pays NOI that is expected to grow, sometimes with inflation, and is risky. The Gordon relation $c = k - g$, with $k = r_f + RP$, gives

$$c - r_f = RP - g.$$

The cap-rate/Treasury spread is a risk premium *minus* expected growth. It has no reason to be constant. When Treasury yields rise because inflation expectations rose, and NOI growth expectations rise with them, the spread should narrow. When Treasuries rise because real rates rose, the spread should be unchanged and cap rates should rise with them. When credit tightens, the risk premium rises and the spread widens even if Treasuries fall. A broker's "long-run average spread" is an average across regimes with different growth expectations, different risk premia, and different financing conditions. It is not an anchor.

### How a rate shock reaches levered real estate

The chain has four links, each with its own timing:

1. **Valuation.** Higher Treasury yields raise required returns. Cap rates move by some pass-through $\beta$, which is unknown in advance and unstable.
2. **Debt service.** For floating-rate loans, interest cost rises immediately. For fixed-rate loans nothing happens until maturity.
3. **Loan sizing.** At refinancing, a higher rate raises the loan constant $K$. A lender who sizes to a minimum DSCR lends $NOI/(DSCR \cdot K)$, so proceeds fall in proportion to the rise in $K$, and the property value used for the LTV test falls with the cap rate.
4. **Refinancing gap.** The outstanding balance does not fall with the new loan amount. The difference is equity that the owner must contribute, or a default.

The first link is a mark-to-market loss that may or may not be realized. The fourth is a cash demand on a fixed date. A speculator must know which one threatens survival. It is almost always the fourth.

---

## 6.3 The Treasury market: instruments, auctions, and quoting conventions

### Instruments

| Security | Maturities at issue | Coupon | Quoted as | Notes |
|---|---|---|---|---|
| Bills | Up to one year (several weekly and monthly cycles) | None; sold at a discount | Discount rate (actual/360, face in denominator); also shown as investment rate (BEY) | Price = $100(1 - d \cdot \text{days}/360)$ |
| Notes | 2, 3, 5, 7, 10 years | Fixed, paid semiannually | Price in 32nds of a point; yield as semiannual bond-equivalent | The 2-, 5- and 10-year are the main benchmarks |
| Bonds | 20, 30 years | Fixed, semiannual | As notes | Highest duration and convexity |
| TIPS | 5, 10, 30 years | Fixed real coupon on CPI-indexed principal | Real yield; price in 32nds | Principal adjusts with CPI-U; at maturity the holder receives the greater of adjusted or original principal |
| FRNs | 2 years | Floating, indexed to the 13-week bill | Discount margin | Near-zero duration |

[FACT: the maturity menu and the single-price auction format are described by the Treasury (TreasuryDirect auction FAQs; 31 CFR Part 356, the Uniform Offering Circular), ch06-S14, ch06-S15, VERIFIED-SECONDARY. The menu changes with Treasury's borrowing needs; check TreasuryDirect before relying on any particular tenor.]

### Auctions

Treasury sells marketable securities in **single-price auctions**. Competitive bidders submit yields (or discount rates for bills). Treasury accepts bids from the lowest yield upward until the offering is filled. Every successful bidder, competitive and noncompetitive, is awarded securities at the **highest accepted yield**, the "stop-out" [FACT; ch06-S14]. Desk vocabulary follows from this:

* **Tail**: the stop-out yield minus the "when-issued" yield trading just before the auction deadline. A positive tail (stop-out above when-issued) means demand was weaker than the market expected.
* **Bid-to-cover**: total bids divided by the amount sold. A ratio is informative only relative to recent auctions of the same tenor.
* **Indirect / direct / dealer takedown**: the shares awarded to bidders through primary dealers on behalf of others (often foreign official and other institutional accounts), to direct bidders, and to primary dealers themselves. Primary dealers are expected to bid in every auction. A large dealer takedown means end-investors bought less and dealers must distribute the balance.

None of these statistics predicts yields by itself. A tail in a 10-year auction on a day of heavy corporate issuance tells you something different from the same tail on a quiet day. Treat auction results as one input to market interpretation (Chapter 4's surprise logic applies: what matters is the result relative to what was priced).

### Quoting conventions and why they matter for comparisons

Four conventions coexist on the same desk, and mixing them is one of the most common errors in comparing yields across instruments.

1. **Bank-discount rate (bills).** $d = \dfrac{F - P}{F}\cdot\dfrac{360}{\text{days}}$. It uses face value, not price, in the denominator and a 360-day year. It always *understates* the investment return.
2. **Bond-equivalent yield, BEY (notes, bonds, and bills shown as "investment rate").** For coupon securities, the semiannual yield to maturity times two. For bills of 182 days or less, $\text{BEY} = \dfrac{F-P}{P}\cdot\dfrac{365}{\text{days}}$. For longer bills the Treasury uses a quadratic that credits a hypothetical semiannual coupon (equation 6.3 below).
3. **Money-market yield.** $\dfrac{F-P}{P}\cdot\dfrac{360}{\text{days}}$, used to compare bills with instruments quoted on actual/360, such as repo and SOFR-indexed loans.
4. **Effective annual yield.** $(F/P)^{365/\text{days}} - 1$ for a bill; $(1 + y/2)^2 - 1$ for a semiannual coupon yield; $(1 + r/12)^{12} - 1$ for a monthly-pay mortgage rate.

A 4.50% Treasury yield and a 4.50% mortgage rate are not the same rate. The Treasury yield is a semiannual BEY, equivalent to 4.5506% effective. The mortgage rate compounds monthly. At 6.50%, a mortgage rate is 6.6972% effective (Example 6.1). Comparisons of "loan spread over Treasuries" are made in quoted terms by convention, which is acceptable if everyone knows the compounding differs.

**Prices in 32nds.** Notes and bonds are quoted in points and 32nds of a point. "98-17" means $98 + 17/32 = 98.53125$. A "+" adds half a 32nd: "98-17+" $= 98 + 17.5/32 = 98.546875$. A third digit gives eighths of a 32nd: "98-172" $= 98 + 17.25/32 = 98.5390625$. One 32nd on \$10 million face is \$3,125.

**Clean and dirty prices.** Quoted prices are **clean**: they exclude accrued interest. The buyer pays the dirty price, clean plus accrued interest since the last coupon. All examples in this chapter price on a coupon date, where the two coincide. Chapter 17 and Appendix C give the accrual formulas and Excel's `ACCRINT`.

### TIPS and breakeven inflation

A TIPS pays a fixed real coupon on principal indexed to CPI-U. Its yield is a real yield. The **breakeven inflation rate** is the inflation rate at which a nominal note and a TIPS of the same maturity deliver the same return:

$$1 + y_{nom} = (1 + y_{real})(1 + \pi_{BE}) \;\Rightarrow\; \pi_{BE} = \frac{1+y_{nom}}{1+y_{real}} - 1 \approx y_{nom} - y_{real}.$$

Breakeven is **not** expected inflation. It contains an inflation risk premium, which raises it, and a TIPS liquidity premium, which lowers it because TIPS trade less actively than nominal notes. The relative size of these premia varies over time and is itself model-dependent [INFERENCE from the structure of the instruments; see Chapter 5 for survey-based inflation expectations]. For a CRE investor the TIPS real yield is the cleanest available market measure of the real risk-free rate, which is the right comparison for a property whose NOI grows with inflation (Section 6.5.8).

---

## 6.4 Technical definitions

| Term | Definition |
|---|---|
| Yield to maturity (YTM), $y$ | The single rate that discounts a bond's promised cash flows to its price, quoted as an annual rate with the instrument's compounding (semiannual for Treasuries) |
| Bank-discount rate, $d$ | $(F-P)/F \times 360/\text{days}$; the bill quoting convention |
| Bond-equivalent yield (BEY) | Semiannual YTM × 2 for coupon bonds; the "investment rate" for bills |
| Effective annual yield | The rate compounded once a year that gives the same growth: $(1+y/m)^m - 1$ |
| Macaulay duration, $D_{mac}$ | PV-weighted average time to cash flows, in years |
| Modified duration, $D_{mod}$ | $D_{mac}/(1+y/m)$; $-\frac{1}{P}\frac{dP}{dy}$ |
| Effective duration | $-\dfrac{P(y+\Delta) - P(y-\Delta)}{2P\Delta}$; defined for any instrument by revaluation, including those whose cash flows change with rates |
| Convexity, $C$ | $\frac{1}{P}\frac{d^2P}{dy^2}$, in years² |
| DV01 (PV01, PVBP) | Dollar price change for a 1 bp fall in yield: $P \cdot D_{mod} \cdot 0.0001$ per unit of price |
| Spot (zero) rate, $s_t$ | Yield on a zero-coupon claim paying at $t$ |
| Forward rate, $f_{t_1,t_2}$ | The rate between $t_1$ and $t_2$ locked in today by the spot curve |
| Term premium | Yield on a long bond minus the yield implied by the *expected* path of short rates; not directly observable |
| Carry | Coupon income minus financing cost over a horizon |
| Roll-down | Price change from a bond being repriced at the curve's yield for its shorter remaining maturity, curve unchanged |
| Steepener / flattener | A position that gains when the long-minus-short yield spread widens / narrows |
| Bull / bear move | Yields fall / rise. "Bear flattener": yields rise, short end more |
| Credit spread | Yield on a risky bond minus the Treasury yield of matching maturity (or a swap rate) |
| Spread duration | Percentage price change per unit change in the credit spread, Treasury yield held fixed |
| Cap-rate spread | Cap rate minus the 10-year Treasury yield, by market convention |
| Pass-through, $\beta$ | Change in cap rate per unit change in Treasury yield over a stated horizon; an empirical, unstable quantity |
| Loan constant, $K$ | Annual debt service per \$1 of loan |
| Refinancing gap | Outstanding balance plus costs minus the new maximum loan |

---

## 6.5 Equations and derivations

### 6.5.1 Bond price

For a bond with face $F$, annual coupon rate $c$, $m$ payments per year, $n = mT$ periods, and yield $y$ (periodic rate $y/m$):

$$P = \sum_{k=1}^{n} \frac{cF/m}{(1+y/m)^k} + \frac{F}{(1+y/m)^n} = \frac{cF}{m}\cdot\frac{1-(1+y/m)^{-n}}{y/m} + F(1+y/m)^{-n}. \tag{6.1}$$

When $y = c$ the price is par. When $y > c$ the bond trades at a discount and accretes toward par as it ages (pull to par).

### 6.5.2 Bills

$$P = F\left(1 - d\cdot\frac{\text{days}}{360}\right), \qquad \text{BEY}_{\le 182} = \frac{F-P}{P}\cdot\frac{365}{\text{days}}. \tag{6.2}$$

For bills longer than 182 days, set $t = \text{days}/365$. The Treasury's BEY solves $P\left(1 + \frac{y}{2}\right)\left(1 + \left(t - \tfrac{1}{2}\right)y\right) = F$, a quadratic in $y$:

$$y = \frac{-2t + 2\sqrt{t^2 - (2t-1)(1 - F/P)}}{2t - 1}. \tag{6.3}$$

The construction assumes a coupon paid at six months and reinvested at the same yield for the remaining $t - \frac12$ years. It makes long bills comparable with semiannual notes.

### 6.5.3 Duration

Differentiate (6.1) with respect to $y$. Write $v = 1 + y/m$ and $CF_k$ for the cash flow at period $k$, which occurs at time $t_k = k/m$:

$$\frac{dP}{dy} = \sum_k CF_k \cdot (-k)\, v^{-k-1} \cdot \frac{1}{m} = -\frac{1}{v}\sum_k t_k \, CF_k\, v^{-k}.$$

Divide by $-P$:

$$-\frac{1}{P}\frac{dP}{dy} = \frac{1}{1+y/m}\underbrace{\sum_k t_k \frac{CF_k v^{-k}}{P}}_{D_{mac}} = D_{mod}. \tag{6.4}$$

Macaulay duration is a weighted average of payment times with present-value weights that sum to one. Modified duration is the price sensitivity. The two differ by the factor $1 + y/m$. For a zero-coupon bond $D_{mac} = T$.

**DV01** is the dollar price change for a 1 bp move:

$$DV01 = P \cdot D_{mod} \cdot 0.0001. \tag{6.5}$$

The library computes DV01 by a central finite difference, which is an independent route and agrees with (6.5) to seven significant figures (Example 6.2's check).

### 6.5.4 Convexity and the second-order approximation

A Taylor expansion of $P(y)$ to second order gives

$$\frac{\Delta P}{P} \approx -D_{mod}\,\Delta y + \frac{1}{2} C\,(\Delta y)^2, \qquad C = \frac{1}{P}\frac{d^2P}{dy^2} = \frac{1}{P\,m^2}\sum_k \frac{k(k+1)\,CF_k}{(1+y/m)^{k+2}}. \tag{6.6}$$

The convexity term is always positive for an option-free bond. It is small for small moves and grows with the square of the move. At 300 bp it is worth several points on a 10-year note (Example 6.2). The error that remains after the convexity term comes from third and higher derivatives. It is negative for rises and positive for falls, so the second-order approximation slightly understates losses and overstates gains.

### 6.5.5 Forward rates and the expectations hypothesis

With annually compounded spot rates $s_1, s_2, \ldots$, no-arbitrage requires that investing for $t_2$ years equal investing for $t_1$ years and rolling at the forward rate:

$$(1 + s_{t_2})^{t_2} = (1+s_{t_1})^{t_1}(1 + f_{t_1,t_2})^{t_2 - t_1} \;\Rightarrow\; f_{t_1,t_2} = \left[\frac{(1+s_{t_2})^{t_2}}{(1+s_{t_1})^{t_1}}\right]^{1/(t_2-t_1)} - 1. \tag{6.7}$$

A forward rate is a rate you can **lock in** today by trading spot instruments. Under the *pure expectations hypothesis* forwards equal expected future spot rates. Empirically they do not. Forwards have, on average, overstated subsequent short rates over long samples, which is the evidence for a positive average term premium [INFERENCE supported by the literature summarized in ch06-S12 and ch06-S13; not a law, and the sign has varied]. A forward is therefore the market's expected rate *plus* a premium. When you hedge a future borrowing by locking the forward, you pay that premium as insurance.

### 6.5.6 Term premium

Let $y_n$ be the $n$-year zero yield and $E_t[r_{t+i}]$ the expected one-year rate in year $i+1$. Define

$$y_n = \underbrace{\left[\prod_{i=0}^{n-1}\big(1 + E_t[r_{t+i}]\big)\right]^{1/n} - 1}_{\text{expectations component}} + TP_n. \tag{6.8}$$

The decomposition is an identity only once you supply the expected path. The path is not observed. It must come from a model or a survey, so $TP_n$ inherits the model's assumptions. Two widely used estimates illustrate the point:

* The **ACM** model (Adrian, Crump and Moench, 2013, *Journal of Financial Economics* 110(1): 110–138) estimates an affine term-structure model by a sequence of linear regressions on principal components of yields. The New York Fed publishes daily and monthly estimates of term premia from it [FACT; ch06-S12, VERIFIED-SECONDARY].
* The **Kim–Wright** model (Kim and Wright, 2005, Federal Reserve FEDS working paper 2005-33) is a three-factor arbitrage-free model fitted to Treasury yields and, in a variant, to survey forecasts of short rates. Its authors attributed much of the 2004–05 decline in long-term yields and distant forwards to lower term premia [FACT; ch06-S13, VERIFIED-SECONDARY]. The Federal Reserve Board publishes estimates from it.

**Estimation caveats.** (1) The two models can disagree in level and sometimes in direction over short windows, because one leans on yields alone and the other on yields plus surveys. (2) Affine models assume the market price of risk is a linear function of a few factors. A regime change in policy reaction or inflation dynamics violates that. (3) Estimates are revised as the sample grows. A term premium "at a 10-year high" in today's vintage may not be at a high in next year's vintage. (4) The term premium is not tradable separately from expectations. A trader who is "long term premium" is long duration and must be right about the expected path as well. Treat published term-premium estimates as model-conditional diagnostics, never as observations. This book cites a specific estimate only with its model, vintage and date. Example 6.6 shows why.

### 6.5.7 Carry and roll-down

Over a horizon $h$, a bond bought at $P_0$ (yield $y_0$, maturity $T$) and financed in repo at rate $r_{repo}$ earns, if the curve does not move:

$$\text{Total} = \underbrace{cFh - P_0 r_{repo}h}_{\text{carry}} + \underbrace{\big[P(y_0, T-h) - P_0\big]}_{\text{pull to par}} + \underbrace{\big[P(y_{T-h}, T-h) - P(y_0, T-h)\big]}_{\text{roll-down}}. \tag{6.9}$$

Here $y_{T-h}$ is today's curve yield at the shorter maturity. Coupons are not reinvested, and financing is simple interest, which is the desk approximation. The **breakeven yield rise** is

$$\Delta y^{*} \approx \frac{\text{Total}}{DV01_h}\ \text{bp}, \tag{6.10}$$

where $DV01_h$ is the bond's DV01 at the horizon. A larger carry-and-roll gives more protection, but protection only against a yield rise smaller than $\Delta y^*$. Carry is income for selling a cushion, not a free return.

### 6.5.8 Credit spreads

A defaultable bond's spread $s$ over Treasuries compensates for expected default loss, the risk of that loss (default and spread risk premia), and lower liquidity. Under a constant risk-neutral default intensity $\lambda$ and recovery rate $R$, the **credit triangle** gives

$$s \approx \lambda (1 - R) \;\Rightarrow\; \lambda = \frac{s}{1-R}. \tag{6.11}$$

The $\lambda$ backed out this way is a *risk-neutral* intensity. It includes premia. Real-world default rates are lower, sometimes much lower, so the spread is mostly premium in high-grade credit and mostly expected loss in distressed credit (Chapter 17). The price sensitivity to the spread is the **spread duration**, which for a fixed-rate bond equals its modified duration to the total yield. A CRE mortgage coupon is a Treasury or swap rate plus a credit spread. Its two components move separately, and in stress they often move in opposite directions: Treasuries rally while spreads widen.

### 6.5.9 Cap rates against Treasury yields

For NOI after reserves growing at a constant expected rate $g$, with required unlevered return $k = r_f + RP$:

$$c = r_f + RP - g, \qquad c - r_f = RP - g. \tag{6.12}$$

Take differentials:

$$\Delta c = \Delta r_f + \Delta RP - \Delta g.$$

The cap rate moves one-for-one with Treasuries only if $\Delta RP = \Delta g = 0$. Three regimes follow:

| Driver of the Treasury move | $\Delta g$ | $\Delta RP$ | Cap-rate pass-through | Spread |
|---|---|---|---|---|
| Real-rate rise (tighter policy, higher real yields) | ≈ 0 | ≈ 0, or up if credit tightens | ≈ 1 or more | Constant or wider |
| Inflation expectations rise, NOI indexed or marked to market | > 0 | ≈ 0 | < 1 | Narrower |
| Flight to quality (Treasuries rally in a crisis) | < 0 | > 0 | Negative: cap rates rise as Treasuries fall | Much wider |

The convention of quoting the spread over the *nominal* 10-year Treasury mixes a real asset with a nominal benchmark. Comparing the cap rate with the 10-year **TIPS** real yield removes the inflation component of $r_f$ but not the growth term. The spread over TIPS is $RP - g_{real}$, which is a cleaner object, though still not constant.

### 6.5.10 Effective duration of levered property equity

Value $V = NOI/c$ with $c = c_0 + \beta\,\Delta r_f$ and NOI fixed. Then

$$\frac{dV}{V} = -\frac{dc}{c} = -\frac{\beta}{c}\,dr_f \;\Rightarrow\; D_V = \frac{\beta}{c}. \tag{6.13}$$

The equity is the residual $E = V - D$, where $D$ here denotes the market value of the debt with duration $D_{debt}$ (zero for floating-rate debt, positive for fixed). The balance-sheet duration identity $E\,D_E = V D_V - D\,D_{debt}$ gives, with $\lambda = D/V$:

$$D_E = \frac{D_V - \lambda D_{debt}}{1 - \lambda}. \tag{6.14}$$

Two readings matter. The **book** equity duration treats the debt at par, $D_{debt} = 0$. That is what a sale or a refinancing sees, because the borrower repays par, or par plus a prepayment premium. The **economic** equity duration marks a fixed-rate loan to market. A below-market fixed-rate loan is an asset to the borrower, but one that can be realized only by holding to maturity or by an assumption by a buyer. Most fixed-rate CRE loans carry yield maintenance or defeasance, which prevents the borrower from buying the loan back at its lower market value.

### 6.5.11 Loan sizing and the refinancing gap

For a loan amortizing monthly at nominal rate $r$ over $N$ years, the loan constant is

$$K(r) = 12\cdot\frac{r/12}{1 - (1 + r/12)^{-12N}}. \tag{6.15}$$

A DSCR-constrained lender lends $L_{DSCR} = NOI/(DSCR_{min}\cdot K)$. The LTV-constrained amount is $\lambda_{max}\cdot NOI/c$, and the debt-yield-constrained amount is $NOI/DY_{min}$. The new loan is the minimum of the three. Since $\partial \ln L_{DSCR}/\partial r = -\partial \ln K/\partial r$, DSCR-sized proceeds have their own "duration" to the loan rate, close to 10 for a 30-year amortization at a 7–8% rate (Section 6.7). The refinancing gap is $B_T + \text{costs} - L_{new}$. The **debt-yield test is the only one of the three that does not depend on rates.** That is why lenders added it after 2008, and why it binds when rates are low.

---

## 6.6 Worked examples

All examples are reproduced in `tests/test_ch06_examples.py`. Inputs are [HYPOTHESIS] unless cited.

### Example 6.1 — Four yields for one bill, and why a 4.50% note is not a 4.50% mortgage

**Given.** (a) A 26-week (182-day) bill quoted at a 5.00% discount rate. (b) A 52-week (364-day) bill quoted at a 4.80% discount rate. (c) A 10-year note yielding 4.30% and a 10-year TIPS yielding 1.95% real. (d) A Treasury note yielding 4.50% (semiannual BEY) and a mortgage at 6.50% (monthly pay). (e) A note quoted at 98-17+ and another at 98-172.

**Find.** Prices, BEY, money-market yield, and effective annual yield for (a) and (b); breakeven inflation for (c); effective annual rates for (d); decimal prices for (e).

**Solution.**

(a) Price $= 100(1 - 0.05 \times 182/360) = 100(1 - 0.025278) = 97.4722$.

* BEY $= (100 - 97.4722)/97.4722 \times 365/182 = 0.025934 \times 2.00549 = 5.2009\%$.
* Money-market yield $= 0.025934 \times 360/182 = 5.1297\%$.
* Effective annual $= (100/97.4722)^{365/182} - 1 = 5.2687\%$.

The quoted discount rate of 5.00% understates the bond-equivalent return by 20 bp.

(b) Price $= 100(1 - 0.048 \times 364/360) = 95.1467$. With $t = 364/365 = 0.99726$, equation (6.3) gives BEY $= 5.0513\%$. The naive simple-interest formula $(F-P)/P \times 365/364$ would give 5.1149%, which is close to the effective annual yield of 5.1153%. The quadratic BEY is lower because it is a semiannually compounded rate. Converting it gives $(1 + 0.050513/2)^2 - 1 = 5.1151\%$, which matches the effective annual yield to within the 364/365-day difference.

(c) Breakeven inflation, approximate: $4.30\% - 1.95\% = 2.35\%$. Exact: $1.0430/1.0195 - 1 = 2.305\%$. The 4.5 bp difference is small at these levels and grows with the level of rates.

(d) Note: $(1 + 0.045/2)^2 - 1 = 4.5506\%$. Mortgage: $(1 + 0.065/12)^{12} - 1 = 6.6972\%$.

(e) $98 + 17.5/32 = 98.546875$; $98 + 17.25/32 = 98.5390625$.

**Check.** Excel: `=TBILLPRICE(settle, settle+182, 5%)` returns 97.4722, `=TBILLEQ(settle, settle+182, 5%)` returns 5.2009%. Python: `x_rates.bill_bey`, `x_rates.bill_effective_annual`.

**Decision consequence.** When the account compares a bill with a SOFR-indexed money fund, use the money-market yield. When it compares a bill with a note, use BEY. When it compares any of them with a mortgage or a property IRR, convert all of them to effective annual rates. The 20 bp gap between the bill's discount rate and its BEY is larger than many of the spreads a desk trades. A memo that says "the bill yields 5.00%" has already made an error in the first sentence.

### Example 6.2 — The 10-year note: price, duration, convexity, DV01, and the large-move error

**Given.** A 10-year Treasury note, 4.00% coupon, semiannual, priced on a coupon date at a 4.50% yield. Position: \$10 million face.

**Find.** Price; Macaulay and modified duration; convexity; DV01 per 100 and for the position; the price change for ±100 bp and ±300 bp by duration alone, by duration plus convexity, and by full repricing.

**Solution.** From (6.1) with $c/2 = 2.00$, $y/2 = 0.0225$, $n = 20$:

$$P = 2.00 \times \frac{1 - 1.0225^{-20}}{0.0225} + 100 \times 1.0225^{-20} = 96.0091.$$

From (6.4): $D_{mac} = 8.2978$ years; $D_{mod} = 8.2978/1.0225 = 8.1152$. From (6.6): $C = 78.005$.

DV01 $= 96.0091 \times 8.1152 \times 0.0001 = 0.077913$ per 100 face. For \$10 million face: $0.077913/100 \times 10{,}000{,}000 = \$7{,}791$ per bp.

| Shock | Duration term (points) | Convexity term | Duration + convexity | Exact repricing | Exact % |
|---|---|---|---|---|---|
| +100 bp | −7.7913 | +0.3745 | −7.4169 | −7.4295 | −7.74% |
| −100 bp | +7.7913 | +0.3745 | +8.1658 | +8.1791 | +8.52% |
| +300 bp | −23.3740 | +3.3701 | −20.0039 | −20.3274 | −21.17% |
| −300 bp | +23.3740 | +3.3701 | +26.7441 | +27.1260 | +28.25% |

For the position, the exact loss at +100 bp is $7.4295/100 \times \$10{,}000{,}000 = \$742{,}951$.

**Check.** DV01 by central difference, $[P(4.49\%) - P(4.51\%)]/2$, equals $P \cdot D_{mod} \cdot 0.0001$ to within $2 \times 10^{-8}$; the residual is the finite-difference error. The asymmetry of the exact column (−7.74% versus +8.52%) is convexity.

**Decision consequence.** For daily risk, DV01 is enough: the duration-only error at 100 bp is 0.36 points, about 5% of the move. For stress tests at 300 bp, the 1994 and 2022 scale, duration alone overstates the loss by 3.0 points (23.37 versus 20.33) and understates the gain by 3.8 points. Convexity removes most of that error, leaving 0.32 points on the loss side. **Stress tests must reprice, not multiply.** A committee shown "DV01 × 300" for a 10-year position overstates the downside and understates the upside, and if the position is short, it understates the downside.

### Example 6.3 — The 1987 desk exercise: a financial calculator and a sheet of graph paper

*The setting.* It is a morning in 1987. There is no spreadsheet on the desk, only an HP-12C and a pad of graph paper. You must price a 10-year, 9.00% semiannual-coupon note at a 10.00% yield, find its duration and DV01 without a duration formula, and draw the price–yield curve to show a client why the bond's losses slow as yields rise. All numbers are [HYPOTHESIS]; the coupon and yield are chosen to be typical of the period's double-digit-yield environment, not to quote any specific issue.

**Step 1 — price on the HP-12C with TVM keys.** Semiannual periods: $n = 20$, $i = 5$, PMT $= 4.5$, FV $= 100$.

```
f CLEAR FIN
20 n
5 i
4.5 PMT
100 FV
PV            → -93.77        (price 93.7689 per 100)
```

The negative sign is the HP-12C cash-flow convention: you pay the price.

**Step 2 — price with the HP-12C bond functions** (settlement 15 January 1987, maturity 15 January 1997, a coupon date, so no accrued interest):

```
f CLEAR FIN
g M.DY
10 i          (annual yield, percent)
9 PMT         (annual coupon rate, percent)
1.151987 ENTER
1.151997
f PRICE       → 93.77         (x<>y shows accrued interest: 0.00)
```

To reverse: key `93.7689 PV`, re-enter the two dates, and press `f YTM` → 10.00.

**Step 3 — DV01 and duration by bumping.** Return to the TVM registers and change only `i`:

```
5.05 i   PV   → -93.17        (yield 10.10%: 93.1747)
4.95 i   PV   → -94.37        (yield  9.90%: 94.3682)
```

$DV01 = (94.3682 - 93.1747)/(2 \times 10) = 0.05967$ per 100 per bp. Effective duration $= (94.3682 - 93.1747)/(2 \times 93.7689 \times 0.001) = 6.3635$. Effective convexity $= (93.1747 + 94.3682 - 2 \times 93.7689)/(93.7689 \times 0.001^2) = 54.54$.

**Step 4 — graph paper.** Compute five points with Step 1's keystrokes, changing `i` to 4, 4.5, 5, 5.5, 6:

| Yield | 8% | 9% | 10% | 11% | 12% |
|---|---|---|---|---|---|
| Price | 106.80 | 100.00 | 93.77 | 88.05 | 82.80 |

Plot price (vertical, 80–110) against yield (horizontal, 7–13%). Use one large square per 1% of yield and per 5 points of price. Draw the chord from 9% to 11%. Its slope is $(88.05 - 100.00)/2 = -5.975$ points per 1%. Divide by the price at 10% and by the 0.01 yield step: $5.975/(93.77 \times 0.01) = 6.372$ years, an estimate of modified duration from a ruler. Measure the gap between the curve at 10% and the chord's midpoint: the chord passes through $(100.00 + 88.05)/2 = 94.02$, above the curve's 93.77 by 0.26 points. That gap is convexity made visible: $C \approx 2 \times 0.2556/(93.77 \times 0.01^2) = 54.58$. The successive one-point price drops shrink, 6.80, 6.23, 5.72, 5.25, and the client sees why.

**Step 5 — Excel.**

| Cell | Formula | Result |
|---|---|---|
| B1 | `=PV(10%/2, 20, 9/2, 100)` | −93.7689 |
| B2 | `=PRICE(DATE(1987,1,15), DATE(1997,1,15), 9%, 10%, 100, 2, 1)` | 93.7689 |
| B3 | `=MDURATION(DATE(1987,1,15), DATE(1997,1,15), 9%, 10%, 2, 1)` | 6.3635 |
| B4 | `=DURATION(DATE(1987,1,15), DATE(1997,1,15), 9%, 10%, 2, 1)` | 6.6816 |
| B5 | `=(PV(4.95%,20,4.5,100)-PV(5.05%,20,4.5,100))/2/10` | 0.05967 |

(B5 is positive because both PVs are negative, so the expression is the falling-yield price minus the rising-yield price.)

**Step 6 — Python.**

```python
from sdesk import fixed_income as fi
fi.bond_price(0.10, 0.09, 10)          # 93.7689
fi.macaulay_duration(0.10, 0.09, 10)   # 6.6816
fi.modified_duration(0.10, 0.09, 10)   # 6.3635
fi.convexity(0.10, 0.09, 10)           # 54.538
fi.dv01(0.10, 0.09, 10)                # 0.059669
```

**Check.** The calculator's bumped duration (6.3635), the graph-paper chord (6.372), Excel's `MDURATION` (6.3635) and the analytic formula agree to the precision each method allows. The chord estimate is biased upward slightly because a 200 bp chord is not a tangent.

**Decision consequence.** The point of the exercise is not nostalgia. A desk that can bump a yield on a calculator can audit any model's duration number in thirty seconds. And the graph makes convexity a physical object rather than a second derivative. Twice in this chapter (Examples 6.4 and 6.9), a position that looks hedged on a DV01 basis is exposed to curvature. Draw the curve.

### Example 6.4 — A DV01-neutral 2s10s steepener, and what it is not neutral to

**Given.** 2-year note: 4.00% coupon, 4.20% yield. 10-year note: 4.25% coupon, 4.40% yield. The desk believes the curve will steepen and wants no exposure to the level of yields. It will short \$50 million face of the 10-year and buy a DV01-matched amount of the 2-year. Ignore financing for the moment.

**Find.** DV01 of each note; the 2-year face amount; P&L under six scenarios by full repricing; the DV01 approximation of the P&L.

**Solution.**

* 2-year: price 99.6201, DV01 $= 0.018947$ per 100.
* 10-year: price 98.7970, DV01 $= 0.079625$ per 100.
* DV01 of the short 10-year leg: $0.079625/100 \times 50{,}000{,}000 = \$39{,}813$ per bp.
* 2-year face to match: $39{,}813/(0.018947/100) = \$210.13$ million, a hedge ratio of 4.203.

| Scenario | 2y change | 10y change | 2y leg P&L | 10y leg P&L | Total (repriced) | DV01 approx. $= \$39{,}813 \times (\Delta y_{10} - \Delta y_2)$ |
|---|---|---|---|---|---|---|
| Parallel +50 | +50 | +50 | −1,978,629 | +1,943,738 | **−34,891** | 0 |
| Parallel −50 | −50 | −50 | +2,002,759 | −2,039,185 | **−36,426** | 0 |
| Bull steepener | −40 | −10 | +1,600,260 | −400,042 | **+1,200,218** | +1,194,381 |
| Bear flattener | +30 | +5 | −1,190,050 | +198,587 | **−991,463** | −995,318 |
| Bear steepener | +10 | +40 | — | — | **+1,164,746** | +1,194,381 |
| Parallel +150 | +150 | +150 | −5,864,890 | +5,563,917 | **−300,973** | 0 |

**Check.** The position's DV01, summed across legs, is zero to rounding. The DV01 column matches the repriced column to within about 0.5% for curve moves of 30 bp.

**Decision consequence.** The trade is a clean bet on the 2s10s spread for moderate moves. It is **short convexity**: it loses in both parallel scenarios, because the short 10-year leg has more convexity per dollar of DV01 than the long 2-year leg. At ±50 bp the cost is \$35,000–\$36,000, about one bp of spread. At 150 bp it is \$301,000, more than 7 bp of curve move. Three further exposures are absent from the DV01 calculation. **Financing**: the desk is long \$210 million of 2-years funded in repo and short \$50 million of 10-years, whose repo rate can go "special" (below general collateral) if the issue is scarce, which raises the cost of the short. **Gross notional**: \$260 million of face supports a position with zero net DV01, so a margin call or balance-sheet limit can force liquidation in exactly the stress the trade is meant to capture. **Other tenors**: the trade is neutral to 2s and 10s but not to a twist around the 5-year. Size the trade on the spread move you believe and the convexity cost of the parallel move you fear, not on DV01 alone.

### Example 6.5 — Forward rates, carry, and roll-down

**Given.** (a) An annually compounded zero-coupon curve: 1-year 4.00%, 2-year 4.20%, 3-year 4.35%, 4-year 4.45%, 5-year 4.50%. (b) Proposal 1 of the opening problem: a 5-year note with a 4.50% coupon bought at par (yield 4.50%). Today's 4-year par yield is 4.35%. Repo is 4.00%. Horizon one year.

**Find.** (a) The one-year forward rates, and the 3-year rate starting in 2 years. (b) Carry, roll-down, total, and breakeven yield rise per 100 face, financed and unfinanced; then repeat with repo at 5.00% and with a flat curve.

**Solution.**

(a) From (6.7):

* $f_{0,1} = 4.00\%$.
* $f_{1,2} = 1.042^2/1.04 - 1 = 4.4004\%$.
* $f_{2,3} = 1.0435^3/1.042^2 - 1 = 4.6506\%$.
* $f_{3,4} = 4.7506\%$, $f_{4,5} = 4.7002\%$.
* $f_{2,5} = (1.045^5/1.042^2)^{1/3} - 1 = 4.7005\%$.

A borrower who expects to refinance in two years for three years can lock about 4.70% today in Treasury terms, 50 bp above today's 2-year spot. Whether that is expensive depends on whether the market's expected path is below the forward, which is to say on the term premium.

(b) Financed at 4.00%. Price today 100.00. At the horizon the note is a 4-year bond. At an unchanged 4.50% yield it would still be at par, so pull to par is 0. At the curve's 4-year yield of 4.35% it prices at 100.5453.

| Component | Per 100 face |
|---|---|
| Coupon income $4.50 \times 1$ | 4.5000 |
| Financing $100 \times 4.00\% \times 1$ | −4.0000 |
| **Carry** | **0.5000** |
| Pull to par | 0.0000 |
| **Roll-down** $100.5453 - 100.0000$ | **0.5453** |
| **Total** | **1.0453** |
| DV01 at horizon (4-year, 4.35%) | 0.036470 |
| **Breakeven yield rise** $1.0453/0.036470$ | **28.7 bp** |

Unfinanced, the total return is $4.50 + 0.5453 = 5.0453$ on 100, or 5.045%. Financed at 5.00% instead (an inverted money-market curve), carry is $4.50 - 5.00 = -0.50$, the total is 0.0453, and the breakeven rise is 1.2 bp. With a flat curve (4-year also 4.50%), roll-down is zero, the total is the 0.50 carry, and the breakeven rise is 13.8 bp.

**Check.** Roll-down repriced independently: a 4-year 4.50% coupon at 4.35% is $2.25 \times a_{\overline{8}|0.02175} + 100 \times 1.02175^{-8} = 100.5453$.

**Decision consequence.** The analyst's "it carries" is true: 1.05 points per year per 100 financed. Levered 5:1 on the account's \$20 million, the position is \$100 million face with a horizon DV01 of about \$36,500 per bp. Total expected carry and roll is about \$1.05 million if nothing moves. A 29 bp rise in 4-year yields over the year erases it. A 100 bp rise costs roughly \$3.6 million before convexity, 18% of the account's \$20 million allocation. Carry is a cushion, and the cushion is less than a third of a typical one-standard-deviation annual move in intermediate yields [HYPOTHESIS: compare with the 1994 and 2022 moves in Section 6.9]. Whether to take it depends on the view on the path of policy (Chapter 5). The carry itself is not a reason.

### Example 6.6 — The term premium is a model output: one yield, two premia

**Given.** The 10-year zero yield is 4.40% (annual compounding). Two analysts supply expected one-year rates for years 1–10.

* Path A, "cuts then normal": 4.0, 3.6, 3.4, 3.3, 3.3, 3.4, 3.5, 3.5, 3.5, 3.5 (%).
* Path B, "higher for longer": 4.3, 4.2, 4.1, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0 (%).

**Find.** The expectations component and term premium under each path, from (6.8).

**Solution.**

* Path A: $\left[\prod(1+r_i)\right]^{1/10} - 1 = 3.4998\%$. Term premium $= 4.40\% - 3.50\% = 0.90\%$.
* Path B: expectations component $= 4.0600\%$. Term premium $= 4.40\% - 4.06\% = 0.34\%$.

The arithmetic average of each path, 3.500% and 4.060%, is within 0.02 bp of the geometric version at these levels.

**Check.** If Path B were the market's true expectation and the premium were zero, the 10-year would yield 4.06%. The 34 bp difference between that and 4.40% is all that Path B attributes to the premium.

**Decision consequence.** The same observed yield supports two opposite trading conclusions. Under A the 10-year pays a 90 bp premium for duration risk, which is attractive to a long-duration buyer. Under B the premium is thin and the buyer is mostly betting that the policy path will be lower than expected. Published estimates from the ACM and Kim–Wright models embed their own versions of A or B, estimated statistically. Before using any term-premium number in a memo, state which model produced it, its vintage, and what expected path it implies, and ask whether you believe that path. A long-duration position justified by "the term premium is high" is a position on the expected path as well.

### Example 6.7 — Credit spread: expected loss versus premium, and the carry cushion

**Given.** A 5-year BBB corporate bond, 6.00% semiannual coupon, yields 6.10%. The 5-year Treasury yields 4.30%. Assumed recovery 40%. Your real-world estimate of the annual default probability for this issuer is 0.30% [HYPOTHESIS].

**Find.** The spread, the risk-neutral default intensity, the expected-loss portion of the spread, the price impact of a 100 bp spread widening, and the spread widening over one year that would offset the excess carry over Treasuries.

**Solution.**

* Spread $= 6.10\% - 4.30\% = 180$ bp.
* Credit triangle: $\lambda = 0.0180/(1 - 0.40) = 3.00\%$ per year.
* Expected loss at the real-world estimate: $0.30\% \times 0.60 = 0.18\%$ per year, or 18 bp. The remaining 162 bp is default-risk premium, spread-volatility premium and liquidity premium.
* Price 99.5746; modified duration 4.2615; DV01 0.042434 per 100. A 100 bp widening, Treasuries unchanged, reprices the bond from 6.10% to 7.10%: −4.1372 points.
* One-year horizon breakeven: excess carry of 1.80 per 100 divided by the horizon (4-year) DV01 of 0.034951 gives **51.5 bp** of widening.

**Decision consequence.** The spread is about 90% premium and 10% expected loss on your estimate. You are paid mainly for bearing spread volatility and illiquidity, not default. Those are exactly the risks that arrive together in a recession, when spreads can widen by more than the 51.5 bp cushion in weeks. The same anatomy applies to CRE debt. A fixed-rate mortgage coupon of "Treasury + 190 bp" contains a Treasury component that rallies in a crisis and a spread component that widens. The borrower who hedged only the Treasury component (Proposal 3) has hedged the leg that tends to move in the borrower's favour in a crisis.

### Example 6.8 — The cap-rate/Treasury spread: decomposition and three ways it moves

**Given.** The industrial building of Proposal 2 at a 5.75% cap rate [a variant for this example], 10-year Treasury 4.40%, expected long-run NOI growth 3.00% after reserves. Then Treasuries rise 100 bp to 5.40% under three explanations:

* A: real-rate rise; $g$ and $RP$ unchanged.
* B: inflation-expectations rise; leases with CPI escalators and short remaining terms raise expected NOI growth by 75 bp; $RP$ unchanged.
* C: real-rate rise accompanied by credit tightening that raises the property risk premium by 50 bp.

**Find.** The initial spread, risk premium and required return; the new cap rate, spread and value change in each case.

**Solution.** From (6.12): spread $= 5.75\% - 4.40\% = 135$ bp; $RP = 5.75\% + 3.00\% - 4.40\% = 4.35\%$; required unlevered return $k = 8.75\%$.

| Case | New $r_f$ | $RP$ | $g$ | New cap $c = r_f + RP - g$ | Spread | Value change $c_0/c_1 - 1$ |
|---|---|---|---|---|---|---|
| A | 5.40% | 4.35% | 3.00% | 6.75% | 135 bp | −14.81% |
| B | 5.40% | 4.35% | 3.75% | 6.00% | 60 bp | −4.17% |
| C | 5.40% | 4.85% | 3.00% | 7.25% | 185 bp | −20.69% |

**Check.** Case A is the one-for-one benchmark: pass-through 1, spread unchanged. B has pass-through 0.25; C has 1.5.

**Decision consequence.** The same 100 bp Treasury move produces value changes from −4% to −21%, and spreads from 60 bp to 185 bp. That range is the answer to the broker in the opening problem. A spread "below its long-run average" may reflect expected growth higher than the average, which is plausible for some property types after a period of rent growth. It may reflect a risk premium compressed by abundant credit, which is fragile. Or it may simply reflect a cap-rate index that lags because appraisals and thin trading smooth it (Chapter 2). The spread tells you nothing until you decide which of $RP$ and $g$ moved. Section 6.8 discusses why history cannot settle this quickly.

### Example 6.9 — Effective duration of levered CRE equity and the refinancing chain

**Given.** Proposal 2: value \$50,000,000, NOI \$3,000,000 after reserves (6.00% cap). Loan \$32,500,000 (65% LTV), fixed 6.00%, 5-year term, 30-year monthly amortization, no prepayment option assumed. Cap-rate pass-through $\beta = 0.6$ [HYPOTHESIS]. Shock: Treasuries +150 bp. For the refinancing at the end of year 5, assume NOI is flat at \$3,000,000 to isolate the rate effect. Lender terms at refinancing: 65% max LTV, 1.25x min DSCR, 9.0% min debt yield, 30-year amortization; the loan rate equals the Treasury yield plus an unchanged spread, so it is 6.00% if Treasuries are unchanged and 7.50% after the shock. The cap rate is 6.00% unchanged, or 6.90% after the shock.

**Find.** (a) Origination debt service and DSCR. (b) The immediate effect of the shock on value and on book and economic equity, and the corresponding effective durations; the first-order durations from (6.13)–(6.14). (c) The refinancing outcome in year 5 with and without the shock. (d) The same shock with a floating-rate interest-only loan at 7.00% all-in.

**Solution.**

(a) Monthly payment $= \$194{,}854$; annual debt service $= \$2{,}338{,}247$; loan constant 7.195%; DSCR $= 3{,}000{,}000/2{,}338{,}247 = 1.283$x. Balance after 60 payments $B_5 = \$30{,}242{,}666$.

(b) New cap rate $= 6.00\% + 0.6 \times 1.50\% = 6.90\%$. Value $= 3{,}000{,}000/0.069 = \$43{,}478{,}261$, down 13.04%.

* Book equity: $\$17{,}500{,}000 \to 43{,}478{,}261 - 32{,}500{,}000 = \$10{,}978{,}261$, down **37.27%**.
* Effective durations: property $0.1304/0.015 = 8.70$; book equity $0.3727/0.015 = 24.84$.
* First order, from (6.13)–(6.14): $D_V = 0.6/0.06 = 10.0$; $D_E = 10/0.35 = 28.57$ with floating or par-valued debt. The gap between 10.0 and 8.70 is convexity: $V = NOI/c$ is convex in $c$.
* Economic equity marks the fixed-rate loan to market. Its modified duration at origination is 4.178. The first-order debt revaluation is $-32{,}500{,}000 \times 4.178 \times 0.015 = -\$2{,}036{,}838$. Economic equity falls 25.63%, an effective duration of 17.09, against a first-order $D_E = (10 - 0.65 \times 4.178)/0.35 = 20.81$. Exact repricing of the loan's 60 payments and balloon at 7.50% gives a market value of \$30,533,976 and economic equity of \$12,944,285, down 26.03%.

(c) Refinancing at the end of year 5:

| | No shock (6.00%, cap 6.00%) | Shock (7.50%, cap 6.90%) |
|---|---|---|
| Value | \$50,000,000 | \$43,478,261 |
| Loan constant $K$ | 7.195% | 8.391% |
| LTV test (65%) | \$32,500,000 | \$28,260,870 |
| DSCR test $NOI/(1.25K)$ | \$33,358,323 | \$28,603,525 |
| Debt-yield test $NOI/0.09$ | \$33,333,333 | \$33,333,333 |
| **Maximum loan (binding)** | **\$32,500,000 (LTV)** | **\$28,260,870 (LTV)** |
| Balance due $B_5$ | \$30,242,666 | \$30,242,666 |
| **Refinancing gap** | **−\$2,257,334 (cash out)** | **+\$1,981,796 (equity required)** |
| DSCR on the old balance at the new rate | 1.379x | 1.182x |

(d) Floating-rate, interest-only \$32.5 million at 7.00% all-in: interest \$2,275,000, DSCR 1.319x. A 150 bp rise in the index adds \$487,500 per year immediately. DSCR falls to 1.086x, and with typical cash-management triggers [HYPOTHESIS: often set between 1.10x and 1.25x in loan documents] the lender would begin sweeping cash.

**Check.** The LTV and DSCR tests are close in both columns. A DSCR test of 1.30x instead of 1.25x would bind in both. The debt-yield test never binds here, and it is the only test that does not move with rates.

**Decision consequence.** A 150 bp Treasury shock that costs the holder of Example 6.2's 10-year note 11.34% of value (exact repricing from 4.50% to 6.00%) costs this equity 37% on paper. More importantly, it converts a \$2.26 million cash-out refinancing into a \$1.98 million equity call, a \$4.24 million swing on \$17.5 million of equity, due on a fixed date. The fixed-rate loan protects cash flow for five years and gives the economic equity a smaller duration (17 versus 25), but the protection expires at the refinancing date, which is exactly when the book-value loss becomes a cash demand. The floating-rate borrower feels the shock in the first month. **The fixed-rate borrower feels it at maturity, all at once.** This is the arithmetic behind every maturity wall (Chapter 12). For the account, it means the building is a long-duration rate position whose duration is an unstable function of $\beta$. Its realized size depends on what rates and cap rates are on one particular date five years from now.

---

## 6.7 CRE application: measuring and hedging a property's rate exposure

### The transmission table

| Channel | Timing | Sensitivity measure | Example 6.9 value |
|---|---|---|---|
| Cap rate → value | Gradual, through appraisals and trades | $D_V = \beta/c$ | 10.0 (first order) |
| Value → book equity | Same | $D_V/(1-\lambda)$ | 28.6 |
| Floating rate → debt service | Immediate | \$ per bp $= L \times 0.0001$ | \$3,250 per bp per year |
| Rate → loan constant at refinancing | At maturity | $\partial \ln K/\partial r$ | ≈ 9.8 at 7.50% |
| Constant → DSCR-sized proceeds | At maturity | $-\partial \ln K/\partial r$ | ≈ \$27,990 less loan per bp |
| Value → LTV-sized proceeds | At maturity | $\lambda_{max}\,V\,D_V$ | binding in Ex. 6.9 |
| Proceeds − balance → equity call | At maturity, in cash | Refinancing gap | +\$1.98m in the shock |

The DSCR row: at 7.50% and 30-year amortization, a 1 bp rise raises $K$ from 8.3906% to 8.3988%, a 0.098% increase. A DSCR-sized loan of \$28.6 million shrinks by about \$27,990 per bp. Proceeds therefore have a "duration" to the loan rate of about 9.8 before any cap-rate effect.

### Can the exposure be hedged with Treasuries?

Proposal 3 suggests shorting Treasury notes. Use Example 6.9's first-order value DV01: $V \times D_V \times 0.0001 = 50{,}000{,}000 \times 10 \times 0.0001 = \$50{,}000$ per bp. The 5-year note at par (4.50%) has a DV01 of 0.044331 per 100. Matching \$50,000 per bp requires $50{,}000/0.00044331 = \$112.8$ million face of 5-year notes, **more than twice the building's value.**

That hedge works only if three things hold:

1. **$\beta$ is stable.** If cap rates move 0.25 for 1 (Example 6.8, case B), the hedge is 2.4 times too large. Falling Treasuries with a stable cap rate then produce a loss on the hedge with no offsetting gain on the building.
2. **The correlation holds in stress.** In a flight to quality Treasuries rally while spreads and cap rates widen (Example 6.8's regime table, row 3). The short Treasury position loses at the same time as the building. The "hedge" doubles the loss.
3. **Funding is available.** The short must be financed and marked daily. The building is marked by appraisal, slowly. A hedge that loses in cash while the asset's offsetting gain exists only on paper can force liquidation of the hedge at the worst time.

What can be hedged with more confidence is the **debt-service channel**: an interest-rate cap on floating-rate debt, or a forward-starting swap or swaption that fixes the base rate of the refinancing loan. Those instruments hedge the *loan constant*, which is contractual, rather than the *cap rate*, which is an opinion. Sizing them to the refinancing balance (\$30.2 million) rather than to the property's value DV01 matches the exposure that threatens survival. The cost of the forward lock is the forward premium in Example 6.5(a): you pay the term premium as insurance. Chapter 13 develops hedge selection, and Chapter 18 prices caps.

### What the buyer is actually underwriting

Proposal 2's 6.00% cap rate with a 6.00% loan has zero positive leverage at origination (Chapter 1, §1.6). The levered return depends on NOI growth and on exit and refinancing conditions. Example 6.9 shows the size of that dependence. An honest memo states: "The equity is a rate position with a duration of about 25–29 on book value. A 150 bp rise in Treasuries at 0.6 pass-through, without offsetting NOI growth, requires about \$2.0 million of new equity at refinancing. We are paid for this by [state the growth assumption] and accept it because [state the view]."

---

## 6.8 When the relationship fails

1. **Pass-through is not a parameter.** $\beta$ in (6.13) is the slope of a relationship that changes with the cause of the rate move (Example 6.8). Estimating it from a regression of cap-rate changes on Treasury changes mixes regimes and suffers from appraisal smoothing, which biases measured $\beta$ toward zero over short windows (Chapter 2). A pass-through estimated in one decade is a hypothesis for the next.
2. **The cap-rate spread mean-reverts slowly, if at all.** With a few decades of data and regimes lasting years, a sample contains only a handful of independent observations of the spread's "average". The standard error of that average is large. [INFERENCE from the persistence of the series; no specific estimate is asserted here.] Trading on a spread's deviation from its mean is a bet that the regime has not changed.
3. **Duration hedges fail when the cash flows change.** Mortgage-backed securities, callable bonds and floating-rate loans with caps have cash flows that depend on rates. Their modified duration from (6.4) is meaningless. Use effective duration by revaluation. A CRE loan with an open prepayment window is a callable bond from the lender's side.
4. **DV01-neutral is not risk-neutral.** Example 6.4's steepener is short convexity and exposed to repo specials, other curve points and balance-sheet limits.
5. **Treasuries are not always liquid.** Benchmark Treasuries are the deepest market most of the time. There have been episodes of sharp dislocation in Treasury market functioning, including the March 2020 "dash for cash" *(verification pending: register a Federal Reserve or Treasury primary account before stating magnitudes)*. A hedge that relies on continuous trading is weakest when it is needed.
6. **The stock–bond correlation can flip.** In low-inflation regimes, Treasuries have often rallied when risk assets fell, so long duration hedged equity risk. In 2022, both fell together (Section 6.9). A CRE portfolio whose diversification assumed negative correlation between rates and risk assets lost on both lines.
7. **Term-premium estimates are not data.** Two respected models can disagree in sign of change over a quarter. Never present a term-premium estimate without its model and vintage.
8. **Breakeven inflation is not expected inflation.** It contains an inflation risk premium and a liquidity component that move in stress. In a crisis TIPS can cheapen relative to nominals for liquidity reasons, depressing breakevens without any change in inflation expectations [INFERENCE from instrument structure].

---

## 6.9 Historical episode: the 1994 bond sell-off and the 2022 duration shock

Two episodes, 28 years apart, test the same mechanism: a central bank tightening faster than priced, a long-duration market caught positioned for stability, and leverage converting mark-to-market losses into forced selling. Daily yield levels below are from the FRED constant-maturity series DGS10 and DGS2 as reproduced by sources cited in `references/sources_ch06.md`. FRED and Treasury sites could not be accessed directly when this chapter was written. The figures are therefore VERIFIED-SECONDARY and flagged for a recheck against FRED itself.

### 1994

**Date and environment.** Ten-year Treasury yields fell about 151 bp from the end of 1992 to a low in mid-October 1993 [FACT; Bank of England, *Quarterly Bulletin* 1995, ch06-S05, VERIFIED-SECONDARY from a search excerpt; confirm against the full text that the figure refers to U.S. yields *(verification pending)*]. The October 1993 low of the 10-year yield was 5.19% [FACT; CNN/Money 2003, ch06-S06, VERIFIED-SECONDARY]. The federal funds target stood at 3.00% before February 1994 [FACT: implied by the 25 bp increase to 3.25% described in the 2015 FEDS note, ch06-S01, and by the 1994 cycle running from 3.00% to 5.50%, ch06-S03].

**The policy move and what was knowable.** At its February 1994 meeting the FOMC raised its federal funds target by 25 bp to 3.25%, its first increase since 1989 [FACT; FEDS Notes 2015, ch06-S01, VERIFIED-SECONDARY]. It was also the first time the Committee announced a policy decision immediately after the meeting. Until then, the funds-rate objective and the outcome of meetings had not been announced, and minutes were released with a lag [FACT; ch06-S01, ch06-S02, VERIFIED-SECONDARY; exact text of the 4 February 1994 statement *(verification pending)*]. Chairman Greenspan explained the announcement as a way to avoid confusion about the first firming since early 1989 [FACT; ch06-S02, VERIFIED-SECONDARY]. Through 1994 the FOMC raised the target six times, from 3.00% to 5.50%, including 25 bp on 18 April and 50 bp on 17 May to 4.25% [FACT; Bank of England *Quarterly Bulletin* 1994 Q3, ch06-S04; Cleveland Fed, ch06-S03; VERIFIED-SECONDARY], and 75 bp on 15 November to 5.50% [FACT; secondary sources, ch06-S03]. A final increase on 1 February 1995 took the target to 6.00% [FACT; ch06-S03]. The 22 March move (+25 bp to 3.50%) and the 16 August move (+50 bp to 4.75%) are implied by these totals [INFERENCE; dates and sizes *(verification pending)* against the FOMC's historical table].

What was knowable in January 1994: the economy was growing, and the Fed had signalled that policy was accommodative. A tightening in 1994 was widely anticipated in direction. What was not knowable was the *speed and cumulative size*. The total was 250 bp in ten months, plus 50 bp in February 1995. Nor was it knowable how much leveraged duration had been accumulated on the premise of continued low short rates.

**What happened in the bond market.** The 10-year yield rose from 5.19% (October 1993) to a peak of 8.05% on 7 November 1994 [FACT; ch06-S06 and FRED-derived DGS10 data, ch06-S07, VERIFIED-SECONDARY], a rise of 286 bp. The Bank of England put the rise in 10-year yields during calendar 1994 at about 200 bp [FACT; ch06-S05, same caveat as above *(verification pending)*]. The difference from 286 bp is the measurement window: low-to-peak versus calendar year. Volatility rose across the major bond markets in 1994 [FACT; BIS, ch06-S16, VERIFIED-SECONDARY]. The Bloomberg U.S. Aggregate index, now the standard broad benchmark, returned about −2.9% in 1994 [FACT; ch06-S11, VERIFIED-SECONDARY]. For a diversified, coupon-paying index of intermediate duration that is a modest calendar-year loss. For leveraged and long-duration holders the same yield move was far more damaging [INFERENCE from the duration arithmetic below].

**Illustrative arithmetic** [HYPOTHESIS: a 10-year note with a 5.25% coupon repriced instantaneously from 5.19% to 8.05%; the actual move took 13 months and earned coupons]: price $100.4635 \to 81.0156$, a loss of 19.36%. Duration alone predicts −22.16 points. Adding convexity, −19.18. The full move is a tail scenario for which "DV01 × 286" would overstate the loss by about 2.7 points per 100 of price.

**Interpretations.** (i) *Policy surprise.* The pace of tightening exceeded what the curve had priced, so expected short rates were repriced upward. (ii) *Credibility and term premium.* Long yields rose by more than the revision to expected policy rates alone would suggest. Ganley and Noblet's Bank of England article (1995) explored the role of monetary-policy credibility in the 1993–94 yield changes, and noted that other proposed explanations included the changing cyclical conjuncture and technical factors such as the behaviour of hedge funds [FACT that these explanations were examined: ch06-S05, VERIFIED-SECONDARY; the article's quantitative findings were not read in full and are not reported here *(verification pending)*]. (iii) *Positioning and leverage.* Leveraged investors and mortgage-related hedging amplified the move. Holders of mortgage-backed securities saw durations extend as prepayments slowed, and hedging that extension meant selling Treasuries into a falling market [INFERENCE from MBS mechanics; the size of convexity-hedging flows in 1994 is *(verification pending)*]. These interpretations are complements, not rivals. Their weights are disputed.

**What it does and does not establish.** It establishes that a tightening anticipated in direction can still produce a large loss when its speed is mispriced and positions are levered. It establishes that duration hedges of negatively convex assets add to selling pressure. It does **not** establish that every tightening cycle produces a 1994-scale sell-off, nor that the Fed's new transparency caused the losses.

### 2022

**Date and environment.** Consumer prices rose 9.1% over the twelve months ending June 2022, the largest 12-month increase since the period ending November 1981 [FACT; BLS CPI release of 13 July 2022, ch06-S08, VERIFIED-PRIMARY]. The FOMC began raising its target range in March 2022 with a 25 bp increase. It raised by 50 bp in May, 75 bp at each of the June, July, September and November meetings, and 50 bp in December, ending the year at 4.25%–4.50%, a cumulative 425 bp [FACT; ch06-S09, VERIFIED-SECONDARY; the June move was described as the largest single increase since 1994]. The March–December sequence sums to 425 bp: $25 + 50 + 4 \times 75 + 50 = 425$.

**What happened.** The 10-year Treasury yield (DGS10) was 1.63% on the first trading day of 2022 and 3.88% on the last, a rise of 225 bp, with a closing high of 4.25% on 24 October. The 2-year (DGS2) rose from 0.78% to 4.41%, a rise of 363 bp, with a high of 4.72% on 7 November [FACT; FRED-derived data, ch06-S07, VERIFIED-SECONDARY; recheck against FRED]. The 2s10s curve inverted and stayed inverted from 6 July 2022 [FACT; ch06-S10, VERIFIED-SECONDARY]. At year-end the 10-year was 53 bp *below* the 2-year. That was a bear flattener of historic size: the short end rose 138 bp more than the long end. The Bloomberg U.S. Aggregate returned about −13% for the year, its worst calendar year since the index began in 1976 [FACT; ch06-S11, VERIFIED-SECONDARY].

**Illustrative arithmetic** [HYPOTHESIS: a 10-year note with a 1.625% coupon bought at 1.63% on the first day of 2022; one year later it is a 9-year note, priced at 3.88% on the assumption that the 9-year yield equals the 10-year]: price $99.954 \to 83.007$; with 1.625 of coupons the one-year total return is **−15.33%**. At the October high (4.25%, instantaneous, 10-year maturity), the price loss would have been 21.17%. The note's modified duration at purchase was 9.19 years, so a first-order estimate for +225 bp is −20.69%. Low coupons mean long durations. The 2022 starting point had the lowest coupons and longest durations in the modern Treasury market, so the same basis-point move cost more than it would have from a 1994 starting point.

**Valuation and financing context for CRE.** Floating-rate CRE borrowers faced the debt-service channel of Section 6.7 within months. Fixed-rate borrowers faced the refinancing channel only as loans matured, from 2023 onward. Appraisal-based cap-rate indices adjusted more slowly than Treasury yields, so measured cap-rate spreads compressed in 2022 before transaction evidence accumulated [INFERENCE from appraisal smoothing (Chapter 2); specific index values *(verification pending)* and not stated here].

**Interpretations.** (i) *Inflation and policy repricing*: the dominant driver of the 2-year was the repricing of the policy path. (ii) *Term premium*: published model estimates of the 10-year term premium rose during 2022 from low levels. The size depends on the model and vintage (Section 6.5.6), so no figure is asserted here. (iii) *Correlation regime change*: bonds and equities fell together, removing the diversification that many portfolios had assumed (Section 6.8, item 6).

**What 1994 and 2022 together establish.** Both establish that duration is a risk factor, not a property of "safe" assets, and that leverage turns marks into cash calls. 2022 additionally establishes that the starting level of yields sets the duration, and therefore the damage per basis point. **What they do not establish:** that a curve inversion predicts recession on a fixed timetable (the 2022 inversion is a single observation with its own causes), or that cap rates must "catch up" to Treasuries by a fixed amount (Example 6.8 shows why they need not).

---

## 6.10 Decision exercise: the investment committee's three proposals

Return to Section 6.1. Prepare a two-page memo on `desk/investment_memos/investment_committee_memo.md` and fill in `desk/scenario_templates/yield_curve_worksheet.md`. Your memo must:

1. State the DV01 of each proposal in dollars per bp: the 5-year note financed at 5:1 (Example 6.5), the building's equity (Example 6.9, first order and effective), and the proposed Treasury short sized as the partner suggests.
2. For Proposal 1, state the breakeven yield rise, the loss at +100 bp, and whether the account's mandate permits 5:1 leverage on a position whose loss at +100 bp is about 18% of its allocation.
3. For Proposal 2, evaluate the broker's spread argument using (6.12). Give the growth and risk-premium assumptions under which the 160 bp spread is fair, cheap or rich.
4. For Proposal 2, report the refinancing gap at +0, +100 and +150 bp, and the equity reserve you would hold.
5. For Proposal 3, decide whether to hedge, with what instrument, and sized to what (value, debt service, or refinancing balance). State what $\beta$ the hedge assumes and what happens to it in a flight to quality.
6. State invalidation criteria and what you will *not* do. Abstention on any proposal is a legitimate answer.

**Rubric** (full version in `problems/solutions/ch06_solutions.md` §Decision exercise). Score 0–4 on each dimension.

| Dimension | Strong answer |
|---|---|
| Measurement | Correct DV01s; distinguishes book from economic equity duration; uses repricing for stress |
| Carry discipline | Treats carry and roll as a cushion with a stated breakeven, not as a return |
| Spread reasoning | Decomposes the spread into $RP - g$; refuses the "long-run average" anchor without regime evidence |
| Refinancing survival | Identifies the year-5 equity call as the binding risk; sizes a reserve or structure (lower leverage, longer term, extension option) |
| Hedge design | Hedges the contractual channel (loan constant) rather than the cap rate; recognizes basis and correlation risk in a Treasury short; does not hedge a deal that may not close |
| Judgment | Says what would change the decision: evidence on $\beta$, NOI growth, lender terms, policy path |

There is no single correct allocation. A memo that recommends all three proposals at full size without reconciling them has missed that they are the same exposure.

---

## 6.11 Frequent analytical errors

1. **Comparing yields with different conventions.** A bill's discount rate, a note's BEY and a mortgage's monthly rate are not comparable without conversion (Example 6.1).
2. **Using modified duration for large moves.** Stress tests at 200–300 bp must reprice (Example 6.2).
3. **Calling a DV01-neutral trade "hedged".** It is neutral only to parallel moves of the two legs and is short or long convexity (Example 6.4).
4. **Treating carry as return.** Carry is compensation for a breakeven yield move. State the breakeven (Example 6.5).
5. **Quoting a term-premium estimate as a fact.** It is a model output with a vintage (Example 6.6).
6. **Reading a credit spread as expected default loss.** In investment-grade credit the spread is mostly premium (Example 6.7).
7. **Anchoring on the average cap-rate spread.** The spread is $RP - g$. Its average spans regimes (Example 6.8).
8. **Assuming one-for-one cap-rate pass-through, or zero.** Both are special cases (Section 6.5.9).
9. **Ignoring leverage in rate sensitivity.** Equity duration is the property duration divided by the equity share (Example 6.9).
10. **Treating a fixed-rate loan as removing rate risk.** It defers the risk to the refinancing date and concentrates it (Example 6.9).
11. **Hedging cap-rate risk with Treasuries without considering correlation in stress.** The hedge can lose in a flight to quality while the property also loses (Section 6.7).
12. **Confusing price in 32nds with decimals.** 98-17 is 98.53125, not 98.17.

---

## 6.12 Connections to other chapters

* Chapter 1 §1.6 introduced negative leverage on the industrial building. This chapter measures its rate exposure.
* Chapter 2 explains appraisal smoothing, which biases measured cap-rate pass-through.
* Chapter 5 develops the expected path of policy rates, the first component of (6.8).
* Chapter 7 extends yields to sovereign spreads and FX-hedged yields for foreign buyers.
* Chapter 9 uses (6.12) in valuation and builds sensitivity grids on cap rates.
* Chapter 10 develops loan sizing, amortization and refinancing (Section 6.5.11).
* Chapter 12 applies the refinancing gap to maturity walls.
* Chapter 13 selects hedges for CRE rate exposure.
* Chapter 17 develops credit spreads, hazard rates and CMBS.
* Chapter 18 prices interest-rate caps and swaptions.
* Chapter 23 revisits 1994 and 2022 among the historical episodes.
* Case B (Refinancing Cliff) and Case C (Cap Rate Expansion and Equity Destruction) apply Example 6.9.

---

## 6.13 One-page reference sheet

| Quantity | Formula | Note |
|---|---|---|
| Bill price | $P = F(1 - d\cdot\text{days}/360)$ | $d$ = discount rate |
| Bill BEY (≤182 days) | $(F-P)/P \times 365/\text{days}$ | Quadratic (6.3) for longer bills |
| Money-market yield | $(F-P)/P \times 360/\text{days}$ | Compare with repo, SOFR |
| Effective annual | $(1+y/m)^m - 1$ | Use to compare across instruments |
| Bond price | $\sum CF_k (1+y/m)^{-k}$ | Excel `PRICE`, `PV` |
| Macaulay duration | $\sum t_k \, PV_k / P$ | Excel `DURATION` |
| Modified duration | $D_{mac}/(1+y/m)$ | Excel `MDURATION` |
| DV01 | $P \cdot D_{mod} \cdot 0.0001$ | per unit of face |
| Price change | $\Delta P/P \approx -D_{mod}\Delta y + \tfrac12 C(\Delta y)^2$ | Reprice for large moves |
| Hedge ratio | $DV01_{exposure}/DV01_{hedge}$ | Per unit of face |
| Forward | $[(1+s_2)^{t_2}/(1+s_1)^{t_1}]^{1/(t_2-t_1)} - 1$ | Annual compounding |
| Term premium | $y_n - \text{expectations yield}$ | Model-dependent |
| Carry + roll | coupon − financing + roll-down | Breakeven $\approx$ total / $DV01_h$ |
| Credit triangle | $\lambda = s/(1-R)$ | Risk-neutral |
| Breakeven inflation | $(1+y_{nom})/(1+y_{real}) - 1$ | Includes premia |
| Cap rate | $c = r_f + RP - g$ | Spread $= RP - g$ |
| Property duration | $D_V = \beta/c$ | $\beta$ unstable |
| Equity duration | $D_E = (D_V - \lambda D_{debt})/(1-\lambda)$ | Book: $D_{debt} = 0$ |
| Loan constant | $12 \cdot \frac{r/12}{1-(1+r/12)^{-12N}}$ | Excel `=PMT(r/12,12N,-1)*12` |
| DSCR-sized loan | $NOI/(DSCR \cdot K)$ | Proceeds "duration" ≈ $\partial\ln K/\partial r$ |
| Refinancing gap | $B_T + \text{costs} - L_{new}$ | Positive = equity required |

**Numbers worth remembering (from this chapter's examples, not universal constants).** A 10-year note at a 4–5% yield has a modified duration near 8 and a DV01 near \$780 per \$1 million face. A 2-year has a DV01 near \$190 per \$1 million. A 6% cap rate with full pass-through implies a property duration near 17. At 0.6 pass-through, it is 10. At 65% LTV with floating debt, equity duration is about 2.9 times the property's.

---

## References for this chapter

All sources are listed with verification status in `references/sources_ch06.md` (IDs ch06-S01 to ch06-S17), for merger into `SOURCE_REGISTER.md`.

* Adrian, T., Crump, R. K., and Moench, E. (2013). "Pricing the Term Structure with Linear Regressions." *Journal of Financial Economics*, 110(1), 110–138. Term-premium estimates published by the Federal Reserve Bank of New York.
* Kim, D. H., and Wright, J. H. (2005). "An Arbitrage-Free Three-Factor Term Structure Model and the Recent Behavior of Long-Term Yields and Distant-Horizon Forward Rates." Finance and Economics Discussion Series 2005-33, Board of Governors of the Federal Reserve System.
* Board of Governors of the Federal Reserve System (2015). "The Effects of FOMC Communications before Policy Tightening in 1994 and 2004." *FEDS Notes*, 24 September 2015.
* Federal Reserve Board (1994). Press release, 4 February 1994. https://www.federalreserve.gov/fomc/19940204default.htm.
* Federal Reserve Bank of Cleveland (1995). "Monetary Policy: An Interpretation of 1994, a Challenge for 1995." *Economic Commentary*, 15 February 1995.
* Bank of England (1994). "Financial Market Developments." *Quarterly Bulletin*, 1994 Q3.
* Ganley, J., and Noblet, G. (1995). "Bond Yield Changes in 1993 and 1994: An Interpretation." Bank of England *Quarterly Bulletin*, May 1995 (1995 Q2).
* Bank for International Settlements. Conference papers on financial market volatility (BIS Conference Papers vol. 1), https://www.bis.org/publ/confp01a.pdf.
* CNN/Money (2003). Commentary on the 1993–94 bond sell-off, 12 August 2003. https://money.cnn.com/2003/08/12/commentary/bidask/bidask/index.htm.
* U.S. Bureau of Labor Statistics (2022). "Consumer Price Index — June 2022." News release, 13 July 2022.
* Federal Reserve Bank of St. Louis, FRED: series DGS10 and DGS2 (10-year and 2-year Treasury constant-maturity yields).
* U.S. Department of the Treasury, TreasuryDirect: auction FAQs; 31 CFR Part 356 (Uniform Offering Circular).
* Gordon, M. J. (1962). *The Investment, Financing, and Valuation of the Corporation*. Homewood, IL: Irwin.
