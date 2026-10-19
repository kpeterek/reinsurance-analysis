# Chapter 7 — Fiscal Policy, Sovereign Risk, and Global Capital

> **Status:** Complete (v1.0). All eight worked examples, the CRE application table, the problems, and the solutions are reproduced in `tests/test_ch07_examples.py`. Problems are in `problems/questions/ch07_problems.md` and solutions in `problems/solutions/ch07_solutions.md`. Sources are listed in `references/sources_ch07.md`. Items marked *(verification pending)* are flagged in that file: the exact trading day of Spain's July 2012 10-year yield peak, and the bibliographic page range of the ACM term-premium paper.

## Learning objectives

After this chapter you should be able to:

1. Write and use the law of motion for public debt, $d_{t+1} = d_t(1+r)/(1+g) - pb_{t+1}$. Compute the debt-stabilizing primary balance, project a ten-year debt path, and explain why the sign of $r-g$ matters more than the level of debt for short-run dynamics, while the level matters more for fragility.
2. Decompose a sovereign spread into an expected-loss component ($\text{PD} \times \text{LGD}$) and a residual risk, liquidity, and redenomination premium. Convert a CDS quote into a hazard rate and a cumulative default probability, and say what assumption on recovery drives the answer.
3. Translate Treasury auction sizes into duration supply (DV01 and 10-year equivalents). State, with its caveats, the channel from deficits to term premia to cap rates.
4. Use the savings–investment and balance-of-payments identities to say who must finance a fiscal deficit, and why an identity is not a causal theory.
5. Classify currency regimes using the impossible trinity, and identify which regimes push adjustment onto interest rates, onto the exchange rate, or onto capital controls.
6. Compute a foreign investor's FX-hedged and unhedged return on U.S. Treasuries and on U.S. CRE using covered interest parity. Explain why the hedged return depends on the short-rate differential, and why changes in hedging cost move foreign demand for U.S. assets.
7. Quantify the bank–sovereign doom loop: the bank capital loss from a sovereign spread shock, the balance-sheet shrinkage it forces, and the resulting cut in CRE lending capacity.
8. Trace a sovereign shock through to a specific property: cap rate, value, LTV, refinancing gap, and the decision it creates for the owner, the lender, and a rescue-capital provider.

---

## 7.1 Opening investment problem: the June 2012 Madrid office

It is late June 2012. You advise a U.S. family office with \$300 million of dollar capital that can be deployed globally. A Spanish bank, under pressure from new provisioning rules, offers a performing loan secured by a Madrid office building. It also offers the building itself through a consensual sale if you prefer to own it outright. The facts below are [HYPOTHESIS] except where cited. The setting is real and the facts about it are documented in §7.9.

* **The building.** NOI before the downturn was €4.0 million. The owner bought it at a 5.00% cap rate (€80 million) with a €52 million five-year loan that matures in 2013. Tenants are paying, but two leases roll in 18 months and local office rents are falling. Current NOI is about €3.8 million.
* **The sovereign.** Spain's 10-year yield has risen above 7% [FACT; §7.9]. Euro-area finance ministers have agreed to lend Spain up to €100 billion to recapitalize its banks [FACT; §7.9]. Some commentators discuss the possibility that Spain leaves the euro. If it did, a euro-denominated claim on a Spanish property might be redenominated into a new, weaker currency.
* **The bank.** The selling bank holds a large portfolio of Spanish government bonds and must raise its provisions on real estate developer loans [FACT; §7.9]. It is cutting new property lending.
* **Your alternatives.** You can (a) buy the building, (b) buy the loan at a discount, (c) buy nothing in Spain and instead buy 10-year U.S. Treasuries, or (d) wait.

Your investment committee will ask: What does the sovereign's condition have to do with this building's value? Is the discount compensation for risk, for illiquidity, or for a forced seller's needs? If you buy in euros, should you hedge back to dollars, and what will the hedge cost? What would make you wrong?

By the end of the chapter you will be able to answer these with numbers. Section 7.10 returns to the decision.

---

## 7.2 Economic intuition: the sovereign is the first borrower in the capital stack

Every country has a capital structure. The government sits at the top. Its bonds are the reference asset against which banks, corporations, and property owners are priced. When the sovereign's credit is strong, its bonds are the risk-free rate. When the sovereign's credit is weak, that "risk-free rate" acquires a credit spread, and everything priced off it reprices.

Five mechanisms connect fiscal policy and sovereign risk to commercial real estate.

**1. The discount-rate channel.** A cap rate is, roughly, a risk-free rate plus a property risk premium minus expected NOI growth (Chapter 6). If the sovereign yield rises because investors demand compensation for default risk, the floor under every domestic cap rate rises. This happens even if the property's tenants are unaffected.

**2. The bank-capital channel.** Banks hold government bonds. They hold them for liquidity regulation, as collateral for central-bank borrowing, and because regulation has historically assigned them low capital charges. When sovereign bond prices fall, bank capital falls. A bank with less capital must shrink its balance sheet or raise equity. CRE loans are among the first to be cut, because they are capital-intensive, illiquid, and usually renewable at maturity rather than contractually committed. The bank's weakness then feeds back into the sovereign's, because markets expect the government to recapitalize its banks. This is the **bank–sovereign doom loop** (§7.4.7).

**3. The supply channel.** A government running large deficits must sell bonds. Somebody must buy them. If domestic savers and foreign buyers absorb the supply only at lower prices, long-term yields carry a higher **term premium**. The size of this effect is genuinely uncertain (§7.4.3). Its direction is not seriously disputed.

**4. The external channel.** A country whose government and private sector together spend more than they save must borrow from abroad. Foreign investors compare returns in their own currency. For many of them, the relevant comparison is the **FX-hedged** return, which depends on the short-rate differential between the two currencies. When hedging costs rise, hedged foreign buyers step back. Foreign demand for a country's bonds and its property can then fall even though nothing about the assets themselves has changed.

**5. The currency-regime channel.** A country that fixes its exchange rate and allows free capital movement gives up independent monetary policy. Under stress, it must defend the peg with interest rates, which raises property cap rates and borrowing costs exactly when the economy is weakest. A euro-area member is an extreme case: it has no national exchange rate to adjust and no national central bank to act as lender of last resort to the sovereign. This is one explanation of why the 2010–12 crisis happened inside the euro area and not, for example, in the United Kingdom or Japan, both of which borrow in currencies their own central banks issue [INFERENCE: an interpretation common in the literature on the euro-area crisis, not a settled fact].

### Why a CRE investor should care before the sovereign is in trouble

Sovereign risk sounds like an emerging-market problem or a historical curiosity. It is neither. The U.S. federal government's debt held by the public was about 99% of GDP at the end of fiscal year 2025, and the Congressional Budget Office projects it reaching about 120% of GDP by 2036 [FACT; CBO February 2026 baseline as summarized by CRFB, ch07-S19]. Nobody serious expects the U.S. to default on Treasury securities. The relevant risks for a U.S. CRE investor are different and more plausible:

* A higher term premium that keeps long rates and cap rates elevated even if the Fed cuts short rates.
* A change in the identity of the marginal buyer of Treasuries, for example from hedged foreign institutions to price-sensitive domestic investors. This makes yields more volatile.
* Foreign CRE capital that disappears when hedging costs rise.
* An event in which fiscal news interacts with leverage somewhere in the financial system. The 2022 U.K. gilt episode (§7.8) is the template.

### The questions this chapter trains you to ask

When fiscal or sovereign news arrives, ask:

1. Did $r$ or $g$ change, or did the primary balance change? Which one, and is it persistent?
2. Is the spread move expected loss, risk premium, liquidity, or redenomination risk?
3. Who holds the bonds, and how leveraged are they?
4. Who is the marginal foreign buyer, and is that buyer hedged?
5. What does the local banking system own, and how much capital does it have?
6. Through which of the five channels does the news reach the property I own or am underwriting?

---

## 7.3 Technical definitions

| Term | Definition |
|---|---|
| Debt ratio $d_t$ | Government debt held by the public at the end of year $t$ divided by nominal GDP in year $t$ (decimal) |
| Primary balance $pb_t$ | Revenue minus non-interest spending in year $t$, as a share of GDP. Positive = primary surplus; negative = primary deficit |
| Overall (headline) balance | Primary balance minus interest outlays, as a share of GDP |
| Effective interest rate $r$ | Interest paid in year $t$ divided by debt at the end of year $t-1$. Changes slowly because only maturing debt reprices |
| Marginal rate | The yield at which new debt is issued today |
| $r - g$ | Effective nominal interest rate minus nominal GDP growth. The "interest–growth differential" |
| Debt-stabilizing primary balance $pb^*$ | The primary balance that holds $d$ constant: $pb^* = d(r-g)/(1+g)$ |
| Weighted average maturity (WAM) | Average time to repayment of the debt stock; governs how fast $r$ follows the marginal rate |
| Sovereign spread | Sovereign yield minus a reference "risk-free" yield in the same currency (e.g., Italy minus Germany, both in euros) |
| Credit default swap (CDS) | Insurance on a reference entity: protection buyer pays an annual premium (the CDS spread) on the notional; seller pays LGD × notional on a credit event |
| Hazard rate $\lambda$ | Instantaneous risk-neutral default intensity. Survival to $T$: $e^{-\lambda T}$ |
| LGD, recovery $R$ | Loss given default $= 1 - R$, as a fraction of face |
| CDS–bond basis | CDS spread minus the bond's spread over the risk-free curve |
| Redenomination risk | The risk that a claim is converted into a different (weaker) currency by law |
| Term premium | The extra yield on a long bond over the expected average of future short rates. Not observable; estimated by models |
| 10-year equivalents | An auction's or portfolio's DV01 expressed as the face amount of 10-year notes with the same DV01 |
| Current account (CA) | Trade balance + net primary income + net secondary income. CA < 0 means the country is a net borrower from abroad |
| Financial account (FA) | Net acquisition of foreign assets minus net incurrence of foreign liabilities |
| Impossible trinity (trilemma) | A country cannot simultaneously have a fixed exchange rate, free capital movement, and an independent monetary policy |
| Covered interest parity (CIP) | $F = S(1 + r_{quote}t)/(1 + r_{base}t)$ for pair BASE/QUOTE; the forward price that removes riskless profit from borrowing in one currency and lending hedged in the other |
| Hedged yield | Foreign asset yield converted to home currency with a forward hedge; $\approx y_{foreign} - (r_{foreign} - r_{home})$ |
| Doom loop (diabolic loop) | Feedback in which weak banks raise sovereign risk (via expected bailouts) and sovereign risk weakens banks (via their bond holdings and guarantees) |
| LTRO | Longer-term refinancing operation: ECB collateralized lending to banks. The two three-year LTROs of December 2011 and February 2012 are the ones discussed here |
| OMT | Outright Monetary Transactions: the ECB's conditional program, announced in August–September 2012, to buy short-dated bonds of a country under an EFSF/ESM program |

---

## 7.4 Equations and derivations

### 7.4.1 The law of motion for the debt ratio

Let $D_t$ be nominal debt at the end of year $t$, $Y_t$ nominal GDP, $r$ the effective nominal interest rate, and $PB_t$ the nominal primary balance. Debt grows by interest and shrinks by any primary surplus:

$$D_{t+1} = D_t(1+r) - PB_{t+1}.$$

Divide by $Y_{t+1} = Y_t(1+g)$:

$$\boxed{d_{t+1} = d_t\,\frac{1+r}{1+g} - pb_{t+1}}$$

where $d_t = D_t/Y_t$ and $pb_{t+1} = PB_{t+1}/Y_{t+1}$. This is an accounting identity given the definitions. It ignores "stock-flow adjustments" such as bank recapitalizations financed by debt, privatization receipts, and valuation changes on foreign-currency debt. In crises these adjustments can be large: Ireland's bank interventions are the outstanding example (§7.9).

**The debt-stabilizing primary balance.** Set $d_{t+1} = d_t = d$:

$$d = d\,\frac{1+r}{1+g} - pb^* \;\;\Rightarrow\;\; pb^* = d\,\frac{r-g}{1+g}.$$

When $r > g$, the government must run a primary **surplus** to stabilize debt, and the required surplus is proportional to the debt level. When $r < g$, debt can be stabilized even with a primary **deficit**.

**Change in the ratio.** Subtract $d_t$ from both sides:

$$\Delta d_{t+1} = d_t\,\frac{r-g}{1+g} - pb_{t+1}.$$

The first term is the "snowball effect." At $d = 1.0$ (100% of GDP), each percentage point of $r-g$ adds about one point of GDP to the debt ratio every year.

**The steady state when $r < g$.** If $pb$ is held constant at a deficit and $r < g$, the ratio converges to

$$d^* = \frac{-pb\,(1+g)}{g - r}.$$

Convergence is slow and the limit can be very high. This is the core of Blanchard's (2019) argument that debt is less costly when $r < g$ [FACT that Blanchard makes this argument; ch07-S23]. It is also the core of the counter-argument: the steady state is reached only if $r < g$ persists for decades, and $r$ is not exogenous to $d$.

### 7.4.2 Why the effective rate lags the market rate

Only maturing debt and new borrowing reprice. If a fraction $\phi \approx 1/\text{WAM}$ of the stock reprices each year, a simple approximation is

$$r_t = r_{t-1} + \phi\,(r^{mkt} - r_{t-1}).$$

With a weighted average maturity of five years, a jump in market yields from 2.5% to 5.0% raises the effective rate by only about half a point in the first year. This lag is why debt dynamics look benign for several years after rates rise, and why a government with short-maturity debt (or floating-rate debt, or large central-bank reserves that pay the policy rate) is more exposed. Problem 7.6 computes it.

### 7.4.3 Deficits, supply, and the term premium

A 10-year yield can be written

$$y_{10} = \underbrace{\frac{1}{10}\sum_{\tau=0}^{9} E_t[r_{\tau}]}_{\text{expected short rates}} + \underbrace{TP_{10}}_{\text{term premium}}.$$

Larger deficits can raise $y_{10}$ through both terms. They may raise expected short rates, because the central bank responds to stronger demand or inflation. They may raise the term premium, because investors must be paid to hold more duration.

**Duration supply.** Treasury sells notes and bonds of different maturities. What the market absorbs is interest-rate risk, so measure supply as DV01:

$$\text{DV01}_{auction} = \frac{\text{Face}}{100} \times \text{DV01 per 100}, \qquad \text{10-yr equivalents} = \text{Face} \times \frac{\text{DV01}_{bond}}{\text{DV01}_{10yr}}.$$

**An empirical anchor, with caveats.** Laubach (2009) relates CBO's five-year-ahead deficit and debt projections to five-year-ahead forward Treasury rates. He estimates that a one-percentage-point increase in the projected deficit-to-GDP ratio raises long-term rates by roughly 25 basis points, and a one-point rise in projected debt-to-GDP by roughly 3–4 basis points [FACT about the published estimate; ch07-S22]. Three caveats are essential:

1. The estimate is about **forward** rates five years ahead, not today's 10-year yield.
2. Later IMF work extending the sample reports that the relationship is not stable over time: close to zero during periods of fiscal prudence and larger when fiscal positions deteriorate [FACT about the later finding; ch07-S22 notes; VERIFIED-SECONDARY; magnitudes not used here].
3. An estimate from U.S. data under a credible fiat-currency regime does not transfer to a euro-area member or to an emerging market.

Treat any coefficient as a scenario parameter, not a law. In this chapter, the supply effect is labeled [HYPOTHESIS] whenever it is used in a calculation.

**Term-premium models.** The New York Fed publishes the Adrian–Crump–Moench (ACM) estimate of the term premium. It is a five-factor affine term-structure model [FACT that the model exists and is published; ch07-S30; bibliographic page range *(verification pending)*]. Different models give different levels. Commentators in 2023 noted that the common models agreed on the direction of the rise in that year but not its size [FACT about the commentary; ch07-S30 notes]. Never cite a term-premium "level" without naming the model.

### 7.4.4 Sovereign spreads, default probability, and CDS

**One-period pricing.** A one-year zero-coupon sovereign bond yields $y$. The risk-free rate is $r_f$. The bond defaults with risk-neutral probability $p$ and then pays a fraction $R$ of its promised value. No-arbitrage requires

$$\frac{(1-p)(1+y) + pR(1+y)}{1+r_f} = 1 \;\;\Rightarrow\;\; p = \frac{1 - (1+r_f)/(1+y)}{1-R}.$$

For small spreads, $1 - (1+r_f)/(1+y) \approx y - r_f = s$, so

$$\boxed{s \approx p \times \text{LGD}}.$$

**Hazard rates.** With a constant default intensity $\lambda$ and recovery $R$, the "credit triangle" gives

$$\lambda \approx \frac{s}{1-R}, \qquad P(\text{default by } T) = 1 - e^{-\lambda T}.$$

Here $s$ is either the CDS spread or the bond spread to the risk-free curve.

**These are risk-neutral probabilities.** They include compensation for bearing default risk, for illiquidity, and, inside a currency union, for redenomination. Decompose the spread as

$$s = \underbrace{p^{phys}\cdot \text{LGD}}_{\text{expected loss}} + \underbrace{\pi_{risk} + \pi_{liq} + \pi_{redenom}}_{\text{premia}}.$$

A speculator buys sovereign credit when they believe the premia are larger than the risk warrants. They sell it when they believe the expected-loss term is understated.

**The CDS–bond basis.** $\text{Basis} = s_{CDS} - s_{bond}$. A negative basis can reflect funding costs (buying the bond requires balance sheet), counterparty risk on the CDS seller, or the fact that a CDS on a euro-area sovereign may pay out in a currency or on a deliverable that differs from what a bondholder receives after redenomination. The basis is not a free arbitrage when funding is scarce. That is precisely when it is widest.

### 7.4.5 The savings–investment identity and the balance of payments

From national income accounting, with private saving $S_p$, private investment $I$, and government balance $T - G$ (all as shares of GDP):

$$\boxed{CA = (S_p - I) + (T - G)}.$$

In balance-of-payments accounting, ignoring the small capital account and statistical discrepancy,

$$CA + KA - FA = 0 \;\Rightarrow\; FA \approx CA,$$

where FA is net acquisition of foreign assets minus net incurrence of liabilities. A current-account deficit means the country is, on net, selling assets or issuing liabilities to foreigners. For a country with a pegged currency, the central bank's reserve change is part of FA:

$$\Delta \text{Reserves} = CA + \text{private net financial inflows}.$$

**An identity is not a theory.** $CA = (S_p - I) + (T-G)$ says that if the government deficit widens by one point and the current account does not change, then private saving net of investment must rise by one point. It does not say which adjusts, or by what price mechanism. Interest rates, the exchange rate, and income all move. The "twin deficits" view (a fiscal deficit widens the current-account deficit one for one) is a special case that holds only if private behavior does not respond. It is [HYPOTHESIS] in any given episode.

### 7.4.6 Currency regimes and the impossible trinity

A country can choose at most two of:

1. A fixed exchange rate.
2. Free capital mobility.
3. An independent monetary policy.

| Regime | Gives up | Adjustment to a shock falls on | Example (verified) |
|---|---|---|---|
| Float, open capital account | Fixed rate | Exchange rate and policy rate | United States |
| Hard peg / currency board, open capital account | Monetary independence | Domestic interest rates, wages, asset prices | Hong Kong: pegged to the U.S. dollar since 17 October 1983 at about HK\$7.80; since 2005 a band of 7.75–7.85 [FACT; ch07-S29] |
| Monetary union member | National currency entirely | Domestic prices, wages, fiscal transfers, and sovereign spreads | Euro-area members |
| Peg with capital controls | Capital mobility | Controls absorb flows; misallocation risk | Various; not used numerically here |
| Floor or ceiling defended by intervention | Part of monetary independence (balance sheet becomes the tool) | Central-bank balance sheet, until the cost becomes unacceptable | Swiss National Bank minimum rate of CHF 1.20 per euro, introduced September 2011, discontinued 15 January 2015 [FACT; ch07-S28] |

Obstfeld, Shambaugh, and Taylor (2005) find that the trilemma's constraints are largely supported by more than 130 years of data on how closely interest rates move together across regimes [FACT about the paper's conclusion; ch07-S26].

**CRE consequence.** Under a peg with open capital markets, domestic interest rates follow the anchor currency's rates plus a risk premium. Property cap rates in Hong Kong therefore respond to Federal Reserve policy, not to Hong Kong's own cycle. Under a monetary union, a member's sovereign spread becomes the adjustment variable, and local cap rates and bank lending absorb it.

### 7.4.7 Covered interest parity and hedged returns

For pair BASE/QUOTE at spot $S$, with simple money-market rates over $t$ years:

$$F = S\,\frac{1 + r_{quote}\,t}{1 + r_{base}\,t}.$$

`sdesk.markets.covered_interest_forward(spot, r_quote, r_base, t)` implements this.

**Hedged return.** A home-currency investor converts $A$ units of home currency into foreign currency, earns a foreign-currency gross return $(1+y)$, and sells the entire terminal amount forward at $F$. The home-currency gross return is

$$1 + R_{hedged} = (1+y)\,\frac{1 + r_{home}\,t}{1 + r_{foreign}\,t}\quad (t = 1).$$

To first order, $R_{hedged} \approx y - (r_{foreign} - r_{home})$. **The hedge cost is the short-rate differential, not the long-rate differential.** A European investor buying 10-year Treasuries and hedging with one-year forwards pays roughly the one-year USD rate minus the one-year EUR rate. The yield on the Treasury is a long rate; the hedge cost is a short rate. When the U.S. yield curve is inverted, hedged Treasuries can yield less than the investor's own government bonds even when U.S. long yields are higher.

**Unhedged return.** With $x$ the percentage change in the home-currency value of one unit of foreign currency,

$$1 + R_{unhedged} = (1+y)(1+x).$$

`sdesk.markets.unhedged_foreign_return(local_return, fx_change)` implements this. Watch the quote direction. For a euro investor, the home value of one dollar is $1/S_{EUR/USD}$, so a move in EUR/USD from 1.10 to 1.15 means $x = 1.10/1.15 - 1 = -4.35\%$.

**Two cautions.**

1. *Hedging the terminal amount.* The formula hedges the expected terminal value. For a 10-year bond held for one year, the terminal value depends on where yields go, so the hedge is imperfect. For property, the terminal value is uncertain and illiquid. Hedge settlements are cash; property gains are not (Example 7.6).
2. *CIP can fail.* Since 2008, CIP deviations (the cross-currency basis) have been persistent for major currencies (Du, Tepper, and Verdelhan, 2018) [FACT about the paper's finding; ch07-S27]. The actual hedge cost then differs from the rate differential by the basis. This chapter computes the textbook CIP forward and treats the basis as an add-on to be checked in live markets.

### 7.4.8 The doom loop as balance-sheet arithmetic

A bank has assets $A$, equity $E$, and domestic sovereign bonds $B$ with modified duration $D$. A sovereign spread shock $\Delta s$ produces a mark-to-market loss of approximately

$$\Delta E \approx -B\,D\,\Delta s.$$

If the bank targets a leverage ratio $\ell = E/A$ and cannot raise equity, its maximum balance sheet after the shock is

$$A^{max} = \frac{E + \Delta E}{\ell}, \qquad \text{Shrinkage} = (A + \Delta E) - A^{max}.$$

Because $1/\ell$ is large (about 17 at 6%), a modest capital loss forces a large asset reduction. If the bank keeps its sovereign bonds, the shrinkage falls entirely on loans and other assets. That is the transmission from sovereign risk to CRE lending capacity. The loop closes when markets price the probability that the government must recapitalize the bank. Acharya, Drechsler, and Schnabl (2014) document that sovereign CDS rose after the 2008 bank bailouts and that subsequent sovereign CDS changes explain bank CDS changes [FACT about the paper's findings; ch07-S24]. Brunnermeier et al. (2016) argue that the loop can be avoided by limiting banks' domestic sovereign exposures relative to their equity [FACT about the paper's argument; ch07-S25].

Accounting matters for timing but not for economics. A bond held at amortized cost does not reduce reported capital when its price falls. Counterparties, rating agencies, and depositors can still see the exposure and price it.

---

## 7.5 Worked examples

All inputs are [HYPOTHESIS] unless a source is cited. Every number is reproduced in `tests/test_ch07_examples.py`.

### Example 7.1 — Debt dynamics and the interest–growth differential

**Given.** A sovereign has a debt ratio $d_0 = 100\%$ of GDP. Its effective nominal interest rate is $r = 3.50\%$ and nominal GDP growth is $g = 4.00\%$. It runs a primary deficit of 2.50% of GDP every year ($pb = -0.025$). Then consider a second case in which the effective rate is $r = 5.00\%$, with growth and the primary balance unchanged.

**Find.** (a) The debt ratio after one year. (b) The debt-stabilizing primary balance. (c) The debt path over ten years. (d) The same for $r = 5.00\%$, and the fiscal adjustment needed to stabilize debt. (e) The steady-state debt ratio in case 1.

**Solution.**

(a) $d_1 = 1.00 \times \dfrac{1.035}{1.040} - (-0.025) = 0.995192 + 0.025 = 1.0202$, i.e., 102.02% of GDP.

(b) $pb^* = d\,\dfrac{r-g}{1+g} = 1.00 \times \dfrac{0.035 - 0.040}{1.040} = -0.4808\%$. The government could run a primary deficit of 0.48% of GDP and keep debt constant. It runs 2.50%, so debt rises by about two points a year.

(c) Iterating the law of motion:

| Year | 0 | 1 | 5 | 10 |
|---|---|---|---|---|
| $d_t$, case 1 ($r = 3.5\%$) | 100.00% | 102.02% | 110.00% | 119.76% |
| $d_t$, case 2 ($r = 5.0\%$) | 100.00% | 103.46% | 117.64% | 136.15% |

(d) With $r = 5.00\%$: $pb^* = 1.00 \times 0.010/1.040 = +0.9615\%$. The government now needs a primary **surplus** of 0.96% of GDP. Relative to its current primary deficit of 2.50%, the required adjustment is $0.9615\% + 2.50\% = 3.46\%$ of GDP. If it delays ten years, the debt ratio is 136.15% and the required surplus becomes $1.3615 \times 0.010/1.040 = 1.31\%$ of GDP.

(e) Case 1 steady state: $d^* = -pb(1+g)/(g-r) = 0.025 \times 1.04/0.005 = 5.20$, i.e., 520% of GDP. The debt ratio converges, but to a level no government has sustained, and over a horizon of many decades.

**Check.** Case 1, one step: $\Delta d_1 = d_0(r-g)/(1+g) - pb = -0.004808 + 0.025 = 0.020192$. ✓. The ten-year values are reproduced by iteration in the test file.

**Decision consequence.** A 150-basis-point rise in the effective interest rate turns a manageable debt path into one that requires a fiscal adjustment of about 3½% of GDP. Fiscal adjustments of that size are politically hard and economically contractionary. The rise in $r$ does not happen overnight (§7.4.2), so markets typically react to the *expected* path of $r$ before the effective rate has moved. For a CRE investor the lesson is about the **sign of $r - g$**: when it turns positive with large primary deficits, expect sustained pressure on long yields through supply and term premia. That is a cap-rate risk on a five-to-ten-year hold, not a default risk.

Reproduce: `tests/test_ch07_examples.py::test_example_7_1`

### Example 7.2 — What a sovereign spread is paying you for

**Given.** A euro-area sovereign's 10-year bond yields 5.60%. The German 10-year yields 2.40%, so the spread is 320 bp. Its 5-year CDS trades at 280 bp. Market convention for sovereign CDS assumes 40% recovery. Your own estimate of the real-world annual default probability over the next five years is 1.5% [HYPOTHESIS].

**Find.** (a) The implied hazard rate and 5- and 10-year cumulative default probabilities using the bond spread, at 40% and 25% recovery. (b) The exact one-period default probability from the pricing equation. (c) The expected-loss and premium components of the spread under your real-world estimate. (d) The CDS–bond basis.

**Solution.**

(a) At $R = 40\%$: $\lambda = 0.032/0.60 = 5.33\%$ per year. Five-year default probability $= 1 - e^{-0.0533 \times 5} = 23.4\%$. Ten-year $= 1 - e^{-0.0533\times 10} = 41.3\%$.
At $R = 25\%$: $\lambda = 0.032/0.75 = 4.27\%$. Five-year $= 19.2\%$; ten-year $= 34.7\%$.

(b) $p = \dfrac{1 - 1.024/1.056}{0.60} = \dfrac{0.030303}{0.60} = 5.05\%$, versus the approximation 5.33%.

(c) Expected loss $= 0.015 \times 0.60 = 0.90\%$ per year, i.e., 90 bp. Premium $= 320 - 90 = 230$ bp. On your view, about 70% of the spread is compensation for risk, illiquidity, and redenomination, not expected default loss.

(d) Basis $= 280 - 320 = -40$ bp.

**Check.** With $\lambda = 5.33\%$ the five-year survival probability is $e^{-0.2667} = 0.766$, so the default probability is $0.234$. ✓. The approximation $s \approx p\cdot\text{LGD}$ overstates $p$ slightly because it ignores the $(1+y)$ discounting in the exact formula.

**Decision consequence.** The market-implied five-year default probability is 19–23%, depending on recovery. Your real-world estimate implies about 7% (that is, $1 - e^{-0.015\times5}$). If you are right, the sovereign's bonds are cheap, and so is anything whose price is anchored to them, including local property. But the gap between 7% and 23% is the premium the market demands for bearing a risk that is concentrated in a bad state of the world: a sovereign default inside a currency union would coincide with bank failures, capital controls, and perhaps redenomination. A premium of 230 bp may be fair compensation for that correlation. Buying the bonds is a speculation that the premium will compress, and it has a fat left tail. The negative basis tells you the cash bond is cheaper than the CDS. A basis trade (buy the bond, buy protection) requires funding that is scarce in exactly the states in which the basis widens.

Reproduce: `tests/test_ch07_examples.py::test_example_7_2`

### Example 7.3 — Auction sizes, duration supply, and the term-premium channel

**Given.** In its August 2026 quarterly refunding, the U.S. Treasury announced auction sizes of \$42 billion for the 10-year note and \$25 billion for the 30-year bond. It also stated that it anticipated maintaining nominal coupon and FRN auction sizes "for at least the next several quarters" [FACT; ch07-S21]. For the calculation, assume the 10-year is issued at par with a 4.25% coupon and the 30-year at par with a 4.75% coupon [HYPOTHESIS]. Separately, suppose the projected deficit-to-GDP ratio rises by 1.5 percentage points [HYPOTHESIS]. A U.S. industrial asset trades at a 6.00% cap rate. Assume that 50% of any change in the 10-year yield passes through to cap rates [HYPOTHESIS].

**Find.** (a) Modified duration and DV01 of each security, and the DV01 of each auction. (b) The 30-year auction in 10-year equivalents. (c) The change in long rates and in the asset's value under a 25 bp-per-point deficit sensitivity, and under 10 bp per point.

**Solution.**

(a) Using `fixed_income.modified_duration` and `fixed_income.dv01` (semiannual):

| Security | Coupon = yield | $D_{mod}$ (years) | DV01 per \$100 | Auction size | Auction DV01 |
|---|---|---|---|---|---|
| 10-year | 4.25% | 8.078 | \$0.08078 | \$42 billion | \$33.93 million |
| 30-year | 4.75% | 15.904 | \$0.15904 | \$25 billion | \$39.76 million |

Auction DV01 for the 10-year $= 42{,}000{,}000{,}000/100 \times 0.08078 = \$33.93$ million per basis point.

(b) 10-year equivalents of the 30-year auction $= 25 \times 0.15904/0.08078 = \$49.2$ billion. The smaller 30-year auction adds more interest-rate risk to the market than the larger 10-year auction.

(c) At 25 bp per point of projected deficit: $\Delta y = 1.5 \times 25 = 37.5$ bp. Cap-rate change $= 0.5 \times 37.5 = 18.75$ bp, so the cap rate goes from 6.00% to 6.1875%. Value change $= 6.00/6.1875 - 1 = -3.03\%$.
At 10 bp per point: $\Delta y = 15$ bp; cap change $= 7.5$ bp; new cap 6.075%; value change $= -1.23\%$.

**Check.** First-order duration approximation for the 10-year: $0.0001 \times 8.078 \times 100 = 0.0808$ per \$100, matching the central-difference DV01 to four decimals. ✓

**Decision consequence.** Measure Treasury supply in duration, not dollars. A refunding that shifts issuance toward the long end raises the risk the private sector must absorb even if total borrowing is unchanged. The deficit-to-yield sensitivity is uncertain by at least a factor of two. On a 6.00% cap asset, the plausible range of value effects from a 1.5-point deficit increase is about −1% to −3%. That is small compared with an ordinary cycle in cap rates, so fiscal supply is rarely the reason to buy or sell a building. It matters in two places: in the *exit cap rate* assumption of a long hold, and in a leveraged position whose refinancing depends on long rates. Do not present a supply-driven yield forecast as a fact; present it as a scenario with a range.

Reproduce: `tests/test_ch07_examples.py::test_example_7_3`

### Example 7.4 — Who finances the deficit? The savings–investment identity

**Given.** A large economy has nominal GDP of \$29.0 trillion [HYPOTHESIS: round number]. Private saving is 21.5% of GDP, private investment 21.0%, and the general government balance −4.4% of GDP [HYPOTHESIS for the decomposition]. For comparison, the U.S. current-account deficit in 2024 was \$1.13 trillion, or 3.9% of GDP, as first reported by BEA [FACT; ch07-S20].

**Find.** (a) The current-account balance as a share of GDP and in dollars. (b) The net financial inflow from abroad. (c) The extra foreign financing required if the government deficit widens by one point of GDP and private saving and investment do not respond.

**Solution.**

(a) $CA = (S_p - I) + (T-G) = (0.215 - 0.210) + (-0.044) = -0.039$, i.e., −3.9% of GDP. In dollars: $-0.039 \times 29.0 = -\$1.131$ trillion.

(b) Ignoring the capital account and statistical discrepancy, the country must sell \$1.131 trillion of net claims on itself to foreigners (Treasuries, corporate bonds, equities, property, or reductions in its holdings of foreign assets).

(c) $0.01 \times 29.0 = \$290$ billion per year of additional net foreign financing, *if* $S_p - I$ does not change.

**Check.** The constructed decomposition reproduces the BEA magnitude: \$1.131 trillion and 3.9% of GDP. The decomposition itself is illustrative and is not BEA's.

**Decision consequence.** The identity says the extra \$290 billion must come from somewhere. Three things can happen, alone or together. (i) Foreigners buy more U.S. assets, which requires a better expected return in their currency: a higher U.S. yield, a cheaper dollar, or a lower hedging cost (Example 7.5). (ii) Domestic private saving rises or investment falls, which in practice usually requires higher real interest rates (crowding out). (iii) The central bank buys the bonds, which raises the inflation question. All three raise the required return on U.S. assets at the margin, including property. The relevant question for a CRE investor is not "will foreigners stop buying?" It is "at what price will the marginal buyer absorb the supply, and who is that buyer?"

Reproduce: `tests/test_ch07_examples.py::test_example_7_4`

### Example 7.5 — Hedged versus unhedged U.S. Treasuries for euro and yen investors

**Given.** One-year horizon. The 10-year Treasury yields 4.30%. Assume its yield is unchanged at year-end, so its one-year local return equals 4.30%. One-year money-market rates (simple): USD 4.00%, EUR 2.00%, JPY 0.50%. Spot EUR/USD = 1.1000 and USD/JPY = 150.00. The euro investor's domestic alternative is a German 10-year at 2.60%. The Japanese investor's domestic alternative is a 10-year JGB at 1.60%. All market levels are [HYPOTHESIS]. Invest €10 million and ¥1.5 billion.

**Find.** (a) The CIP forwards. (b) Hedged returns and pick-up versus the home bond. (c) The euro investor's unhedged return if EUR/USD ends at 1.15. (d) The break-even year-end spot rates at which unhedged Treasuries match the home bond. (e) The euro hedged return if the USD money rate falls to 3.00% with the 10-year unchanged.

**Solution.**

(a) EUR/USD (base EUR, quote USD): $F = 1.10 \times 1.04/1.02 = 1.121569$.
USD/JPY (base USD, quote JPY): $F = 150 \times 1.005/1.04 = 144.9519$.

(b) *Euro investor.* Convert: €10,000,000 × 1.10 = \$11,000,000. Terminal value $= 11{,}000{,}000 \times 1.043 = \$11{,}473{,}000$. Sold forward: $11{,}473{,}000/1.121569 = €10{,}229{,}423$. Hedged return = **2.294%**. Pick-up versus the Bund $= 2.294\% - 2.60\% = -0.31\%$ (−31 bp).
Approximation: $4.30\% - (4.00\% - 2.00\%) = 2.30\%$. ✓

*Yen investor.* Convert: ¥1,500,000,000/150 = \$10,000,000. Terminal value \$10,430,000. Sold forward: $10{,}430{,}000 \times 144.9519 = ¥1{,}511{,}848{,}558$. Hedged return = **0.790%**. Pick-up versus the JGB $= -0.81\%$ (−81 bp).

(c) The home value of one dollar changes by $x = 1.10/1.15 - 1 = -4.348\%$. Unhedged return $= 1.043 \times (1 - 0.04348) - 1 = -0.235\%$. Equivalently $11{,}473{,}000/1.15 = €9{,}976{,}522$.

(d) Euro investor: unhedged matches the Bund when $11{,}473{,}000/S_T = 10{,}000{,}000 \times 1.026$, so $S_T = 1.1182$. The dollar can weaken by about 1.6% before unhedged Treasuries lose to Bunds.
Yen investor: $10{,}430{,}000 \times S_T = 1{,}500{,}000{,}000 \times 1.016$, so $S_T = 146.12$. The yen can appreciate by only 2.59% before unhedged Treasuries lose to JGBs.

(e) $1.043 \times 1.02/1.03 - 1 = 3.287\%$. Pick-up versus the Bund becomes +0.69%.

**Check.** Under CIP, the hedged return equals the unhedged return evaluated at $S_T = F$: $11{,}473{,}000/1.121569 = €10{,}229{,}423$. ✓

**Decision consequence.** With an inverted or flat U.S. curve and a large short-rate differential, hedged Treasuries are *worse* than home bonds for both investors, even though the U.S. 10-year yields 170 bp more than the Bund and 270 bp more than the JGB. The yen investor who wants a higher yield must go unhedged, which converts a bond purchase into a currency speculation with a 2.6% cushion. Part (e) shows that a Fed cut of 100 bp, with no change in the 10-year, swings the euro investor's hedged pick-up by about one point. **Foreign demand for U.S. duration is therefore sensitive to the front end of the U.S. curve and to the shape of the curve, not only to the level of U.S. long yields.** This is why the identity of the marginal buyer matters (Example 7.4): if hedged foreign buyers step back, unhedged buyers (who demand a currency risk premium) or domestic buyers (who demand a higher yield) must replace them.

Reproduce: `tests/test_ch07_examples.py::test_example_7_5`

### Example 7.6 — A euro investor buys a U.S. industrial building: hedged yield and hedge liquidity

**Given.** A German insurer buys a U.S. industrial building for \$60 million, all cash, at a 5.50% cap rate. Year-1 NOI after reserves is \$3.30 million, received at year-end. Market rates are those of Example 7.5 (EUR/USD 1.10; USD 4.00%; EUR 2.00%). A comparable German logistics asset yields 4.50% [HYPOTHESIS]. The insurer hedges the full expected year-end USD amount (value plus NOI) with a one-year forward. Assume the property's USD value is unchanged after one year.

**Find.** (a) The hedged one-year total return in euros, and the comparison with the domestic asset. (b) The cash settlement on the hedge if the dollar strengthens to EUR/USD 1.00, as a share of the euro equity. (c) The unhedged return in that scenario. (d) The hedged return if the insurer instead finances 50% with a USD interest-only loan at 6.00% and hedges only the equity.

**Solution.**

(a) Equity in euros $= 60{,}000{,}000/1.10 = €54{,}545{,}455$. Year-end USD amount $= 60{,}000{,}000 + 3{,}300{,}000 = \$63{,}300{,}000$. Sold forward at 1.121569: $€56{,}438{,}811$. Hedged return $= 56{,}438{,}811/54{,}545{,}455 - 1 = 3.471\%$. Check: $(1.055)(1.02/1.04) - 1 = 3.471\%$. Versus the domestic asset at 4.50%: −103 bp.

(b) If EUR/USD ends at 1.00, the \$63.3 million is worth €63,300,000 at spot. The insurer must deliver it under the forward for €56,438,811. The hedge settles at a loss of $63{,}300{,}000 - 56{,}438{,}811 = €6{,}861{,}189$, which is **12.58%** of the original euro equity. It is payable in cash at the forward date. The offsetting gain on the property is unrealized and illiquid.

(c) Unhedged, with the dollar up 10% against the euro ($x = 1.10/1.00 - 1 = +10\%$): $1.055 \times 1.10 - 1 = 16.05\%$.

(d) Loan \$30 million at 6.00% interest-only: interest \$1.80 million. Equity \$30 million = €27,272,727. Year-end USD equity value $= 30{,}000{,}000 + 3{,}300{,}000 - 1{,}800{,}000 = \$31{,}500{,}000$. Hedged: $31{,}500{,}000/1.121569 = €28{,}085{,}664$. Return $= 2.981\%$, lower than unlevered, because the 6.00% debt costs more than the 5.50% asset yields (negative leverage) and the hedge cost of about 1.9% applies to the equity.

**Check.** (a) and (d) are both of the form $(1 + \text{USD equity return})(1.02/1.04) - 1$ with USD returns of 5.50% and 5.00%. ✓

**Decision consequence.** At these rates, a hedged euro investor earns about 100 bp *less* on a U.S. building than on a comparable domestic one. A fully hedged buyer will not compete at a 5.50% cap. An unhedged buyer takes a currency view. This explains a pattern that U.S. brokers often describe as foreign capital "disappearing": its required cap rate in dollar terms rose when U.S. short rates rose relative to home rates [INFERENCE from the arithmetic; the size of any actual change in foreign CRE buying is not established here]. Part (b) is the hidden risk. Full hedging of an illiquid asset creates a cash call of 12.6% of equity on a 10% currency move. Institutions therefore use partial hedge ratios, longer-dated hedges, or local-currency debt as a natural hedge. Local debt hedges the currency exposure on the borrowed portion, but here it also introduces negative leverage. For a U.S. seller, the lesson is practical: a foreign bidder's hedge cost is part of what sets the price. When U.S. short rates fall relative to euro or yen rates, expect hedged foreign bidders to return.

Reproduce: `tests/test_ch07_examples.py::test_example_7_6`

### Example 7.7 — The doom loop in one bank's balance sheet

**Given.** A euro-area periphery bank has total assets of €100 billion and equity of €6.0 billion, a 6.0% leverage ratio that it targets. It holds €12 billion of its own government's bonds with modified duration 5.0 at fair value. It holds €15 billion of CRE loans. The sovereign spread widens by 250 bp. The bank cannot raise equity and chooses to keep its sovereign bonds (it uses them as collateral for central-bank funding). Its funding spread rises by half of the sovereign spread change [HYPOTHESIS].

**Find.** (a) The capital loss and the new leverage ratio. (b) The balance-sheet shrinkage required to restore 6.0%. (c) The cut in CRE loans if the shrinkage falls pro rata on all non-sovereign assets. (d) The rise in the bank's cost of funding. (e) The annual carry on €10 billion of two-year sovereign bonds yielding 5% funded by three-year central-bank borrowing at 1%, and why that matters for the loop.

**Solution.**

(a) $\Delta E \approx -12 \times 5.0 \times 0.025 = -€1.50$ billion. Equity $= €4.50$ billion. Assets $= 100 - 1.5 = €98.5$ billion. Leverage ratio $= 4.5/98.5 = 4.57\%$.

(b) $A^{max} = 4.5/0.06 = €75.0$ billion. Shrinkage $= 98.5 - 75.0 = €23.5$ billion, or 23.9% of the balance sheet.

(c) Non-sovereign assets after the shock $= 98.5 - 10.5 = €88.0$ billion. CRE share $= 15/88 = 17.05\%$. Pro-rata CRE cut $= 23.5 \times 15/88 = €4.01$ billion, about 27% of the CRE book. Because the sovereign holdings are retained, every non-sovereign asset class shrinks by $23.5/88 = 26.7\%$.

(d) Funding cost rises by $0.5 \times 250 = 125$ bp. If the bank passes this through, the coupon on new or refinanced CRE loans rises by 125 bp before any change in the credit spread on the property.

(e) Carry $= 10 \times (0.05 - 0.01) = €0.40$ billion per year.

**Check.** The 1.5 billion loss is 25% of equity; with leverage of $1/0.06 = 16.7\times$, a 25% equity loss forces roughly a 24% asset reduction. ✓

**Decision consequence.** A sovereign shock that costs the bank 1.5% of assets forces it to cut 27% of its CRE book if it cannot raise capital. CRE borrowers who need to refinance in that window face a lender that is not merely more expensive but *absent*. Part (e) shows the uncomfortable side of central-bank support. Cheap three-year funding stabilizes the bank's liquidity, but it also pays the bank to buy more of its own sovereign's bonds, which deepens the loop if the sovereign later deteriorates. When you underwrite CRE in a country with a weak sovereign, underwrite the *lender* as well as the property: its sovereign holdings relative to equity, its funding sources, and its likely response to a capital shock.

Reproduce: `tests/test_ch07_examples.py::test_example_7_7`

### Example 7.8 — From the sovereign to the building: the Madrid office

**Given.** The building in §7.1 was bought at a 5.00% cap rate on NOI of €4.0 million (value €80 million) with a €52 million loan (65% LTV) that matures shortly. The local 10-year sovereign yield rises 200 bp. Assume 50% pass-through to cap rates, so the cap rate rises 100 bp to 6.00% [HYPOTHESIS]. A recession reduces NOI by 5%. A new lender will offer at most 60% LTV, a 1.30× DSCR on a 25-year amortizing loan at 7.00% (monthly payments), and a 9.0% minimum debt yield. Refinancing costs are 1% of the new loan [HYPOTHESIS].

**Find.** (a) The new value and the percentage change. (b) Equity before and after, and the new LTV on the existing loan. (c) The maximum new loan and the binding constraint. (d) The equity required to refinance.

**Solution.**

(a) $NOI_1 = 4{,}000{,}000 \times 0.95 = €3{,}800{,}000$. $V_1 = 3{,}800{,}000/0.06 = €63{,}333{,}333$. Change $= -20.83\%$.

(b) Equity: $80{,}000{,}000 - 52{,}000{,}000 = €28{,}000{,}000$ before; $63{,}333{,}333 - 52{,}000{,}000 = €11{,}333{,}333$ after; change $-59.52\%$. LTV $= 52/63.33 = 82.1\%$.

(c) Constraints, using `cre.max_loan`:
* LTV: $0.60 \times 63{,}333{,}333 = €38{,}000{,}000$.
* Debt yield: $3{,}800{,}000/0.09 = €42{,}222{,}222$.
* DSCR: the loan constant at 7.00% over 25 years is $K = 0.084814$. Maximum loan $= 3{,}800{,}000/(1.30 \times 0.084814) = €34{,}464{,}759$.

The DSCR constraint binds at **€34.46 million**.

(d) Refinancing gap $= 52{,}000{,}000 + 0.01 \times 34{,}464{,}759 - 34{,}464{,}759 = €17{,}879{,}889$.

**Check.** At the binding loan, annual debt service $= 34{,}464{,}759 \times 0.084814 = €2{,}923{,}077$ and DSCR $= 3{,}800{,}000/2{,}923{,}077 = 1.30$. ✓

**Decision consequence.** A 200 bp sovereign shock and a mild NOI decline take the equity from €28.0 million to €11.3 million. To keep the building, the owner must inject €17.9 million, which is more than the equity is now worth. A rational owner with non-recourse debt will hand back the keys or negotiate an extension unless the owner has strong reasons to stay. The lender (which is itself under the pressure of Example 7.7) faces an 82% LTV loan that cannot be refinanced elsewhere. **This is where rescue capital earns its return:** a preferred-equity or mezzanine provider who can fund the €17.9 million gap has pricing power, because both the owner and the bank need a solution and the bank's own alternatives are constrained by its capital. But the rescue provider is taking a position whose value depends on whether the cap-rate rise is temporary (a sovereign liquidity premium that central-bank action can remove) or permanent (a re-rating of the country). Section 7.9 shows that in July 2012 that question was answered by policy, not by property fundamentals.

Reproduce: `tests/test_ch07_examples.py::test_example_7_8`

---

## 7.6 CRE application: the global-capital screen for a U.S. acquisition

You are bidding on a stabilized U.S. industrial or hotel asset. Expect foreign and domestic bidders. Before setting your bid, run a five-line screen.

**Line 1 — The rates you are really competing against.** Write down the 10-year Treasury, your all-in debt cost, and the going-in cap rate. If the cap rate is below the debt cost, leverage is negative (Chapter 1, §1.6). Your return depends on growth and exit pricing.

**Line 2 — The term-premium scenario.** Run the exit cap at your base case and at base + 25 bp and base + 50 bp. Justify the shocks by reference to fiscal supply (Example 7.3) and say which term-premium model you used, if any.

**Line 3 — The foreign bidder's hedged yield.** For each likely foreign bidder, compute the hedged income-plus-flat-value return at the asking cap rate. With the rates of Example 7.5:

| Bidder's home currency | Hedge cost ≈ $r_{USD} - r_{home}$ | Hedged return at a 5.50% cap, value flat | Typical domestic alternative (assumed) | Hedged pick-up |
|---|---|---|---|---|
| EUR | ≈ 1.9% | 3.47% | 4.50% | −1.03% |
| JPY | ≈ 3.4% | 1.95% | 3.50% | −1.55% |
| USD (domestic bidder) | 0 | 5.50% | — | — |

The yen figure is $(1.055)(1.005/1.04) - 1 = 1.95\%$. The domestic alternatives are [HYPOTHESIS].

On these numbers, hedged euro and yen bidders cannot pay a 5.50% cap rate on fundamentals. If they bid anyway, they are either unhedged (taking a currency view), using local USD debt (and negative leverage), or using strategic reasons such as diversification. **Your bid should not assume foreign competition will rescue your exit.**

**Line 4 — The lender's exposure to sovereign and funding stress.** For a U.S. asset this is usually not the sovereign but the lender's own funding, deposit stability, and CRE concentration. The structure of Example 7.7 still applies: a capital shock forces shrinkage, and CRE is the first casualty.

**Line 5 — What would change the conclusion.** A 100 bp fall in U.S. short rates relative to euro rates adds about 1 percentage point to the euro bidder's hedged return (Example 7.5(e)). A rise in the cross-currency basis does the opposite. Monitor the forward points, not just the policy rates.

**Hotel note.** Hotels have shorter "lease" duration than industrial assets: they reprice every night. Their NOI responds faster to domestic demand and to foreign travel flows, which depend on the exchange rate. A strong dollar reduces inbound international travel demand and favors outbound U.S. travel [HYPOTHESIS for any specific market; check STR source-market data]. A foreign owner of a U.S. hotel is therefore exposed to the dollar twice: once through the asset value translated to home currency and once through the hotel's demand mix.

---

## 7.7 When the relationship fails

1. **$r - g$ is not exogenous.** The debt dynamics equation treats $r$ and $g$ as given. In a crisis, $r$ rises *because* debt is high, and $g$ falls because fiscal tightening and bank deleveraging depress output. Fiscal consolidation can therefore raise the debt ratio in the short run if it shrinks nominal GDP enough. Projections that hold $r$ and $g$ fixed understate the nonlinearity.
2. **Spreads are not expected losses.** Inside a currency union, part of the spread is redenomination risk: the risk that the bond is repaid in a new currency. That risk is not captured by PD × LGD and can disappear quickly when a central bank credibly removes it. After the ECB's July–September 2012 statements and the OMT announcement, peripheral spreads fell without any change in fiscal fundamentals of comparable speed (§7.9) [INFERENCE: commentators widely credit the announcement; the counterfactual cannot be observed].
3. **CIP fails when balance sheets are scarce.** Since 2008, persistent deviations from CIP have been documented for major currencies (ch07-S27). The hedge cost then exceeds the rate differential, often most at quarter-ends and in stress. Treat the CIP forward as a lower bound on hedge cost for a non-bank investor.
4. **Pegs fail abruptly.** A peg is credible until the central bank decides its cost is too high. The Swiss National Bank discontinued its CHF 1.20 floor on 15 January 2015 and said enforcing it was no longer justified (ch07-S28). Investors who treated the floor as a permanent one-sided bet lost money on the day.
5. **A reserve-currency sovereign's bad news can lower its own yields.** When fiscal stress coincides with global risk aversion, investors may buy the stressed sovereign's bonds as a safe haven. The sign of the yield response to fiscal news therefore depends on whether the issuer's debt is the world's safe asset. This is an [INFERENCE] about mechanism; specific episodes should be checked against data before being cited.
6. **The transmission can run through leverage rather than default risk.** In September 2022, a U.K. fiscal announcement was followed by a sharp rise in long gilt yields. The damage came through collateral calls on leveraged pension hedges, not through any doubt about the U.K. government's ability to pay (§7.8). Models that look only at PD × LGD miss this channel entirely.
7. **The identity says nothing about timing.** A large current-account deficit can be financed smoothly for years, then suddenly cannot. The balance-of-payments identity holds at every moment; the price that clears it changes.

---

## 7.8 A second episode in brief: the 2022 U.K. gilt and LDI stress

**Date and environment.** In September 2022, U.K. inflation was high and the Bank of England was raising rates. U.K. defined-benefit pension schemes had widely used liability-driven investment (LDI) strategies [FACT that LDI funds were central to the episode; ch07-S17] that hedged long-dated liabilities with leveraged gilt positions and derivatives.

**What happened.** Following the government's fiscal announcement of 23 September 2022, long-dated gilt yields rose very rapidly. In a letter to the Treasury Committee dated 5 October 2022, Deputy Governor Jon Cunliffe described the move. Secondary coverage of the letter reports that the four-day rise in 30-year yields was more than twice as large as the largest such move since 2000 [FACT as reported; ch07-S18; VERIFIED-SECONDARY]. On 28 September 2022 the Bank announced temporary, targeted purchases of long-dated conventional gilts for financial-stability reasons. It raised the daily auction maximum from £5 billion to £10 billion on 10 October and extended purchases to index-linked gilts on 11 October. It ended the operations on 14 October 2022, having purchased £19.3 billion of gilts in total [FACT; ch07-S17].

**Mechanism.** When yields rose, LDI funds faced collateral calls. To meet them, they sold gilts, which raised yields further and triggered more calls. The Bank's stated purpose was to give LDI funds time to rebuild resilience, not to provide a permanent backstop [FACT; ch07-S17].

**What it establishes.** Fiscal news can transmit to asset prices through leverage and collateral in a specific investor class. The stress was concentrated in a market (long gilts) and in a group (pension LDI) that a CRE investor might not watch. The episode does *not* establish that U.K. sovereign credit risk rose materially, nor that the fiscal announcement alone would have produced that yield move without the leverage. Those are contested interpretations.

**CRE connection.** U.K. pension funds were also holders of property funds and other illiquid assets. When a leveraged hedge needs cash, the investor sells what it can, which may include its liquid holdings of real estate securities or units in open-ended property funds. The analog to Example 7.6(b) is exact: hedge settlement needs cash, and the hedged asset may not provide it.

---

## 7.9 Historical episode: the euro-area sovereign crisis, 2010–2012

### Date and environment

The euro was introduced in 1999. Until the crisis, sovereign spreads within the euro area were small by later standards: Italy's spread over Bunds first exceeded 500 bp only in November 2011 [FACT; ch07-S06]. Banks across the area held government bonds of many members. Ireland and Spain had large domestic credit and property booms in the 2000s [INFERENCE from the scale of the later property-loan transfers and provisions documented below: ch07-S11, S12, S13].

### The sequence of events

| Date | Event | Status |
|---|---|---|
| 30 Sep 2008 | Ireland guarantees essentially all liabilities of its systemically important banks, covering deposits, covered bonds, senior debt, and dated subordinated debt | [FACT; ch07-S14] |
| 2010 | Ireland records a general government deficit of 32% of GDP, the highest ever recorded in the EU, reflecting bank interventions and recession | [FACT; ch07-S14, as reported by the Central Bank of Ireland from Eurostat data] |
| May 2010 | Greece receives a €110 billion euro-area/IMF loan package | [FACT; ch07-S09] |
| 10 May 2010 | ECB launches the Securities Markets Programme (SMP) for interventions in public and private debt securities markets | [FACT; ch07-S05] |
| Late Nov 2010 | Ireland agrees an €85 billion program, including €10 billion for immediate bank recapitalization and €25 billion of contingent bank support | [FACT; ch07-S09] |
| By end-2011 | Ireland's NAMA acquires about €74 billion of property-related loans from five institutions for €31.8 billion, an overall discount of 57% | [FACT; ch07-S13] |
| 9 Nov 2011 | Italy's 10-year yield trades as high as 7.48% and closes at 7.25%, its first move above 7% since the euro's launch; the spread over Bunds exceeds 500 bp for the first time in the euro era | [FACT; ch07-S06] |
| 21–22 Dec 2011 | First three-year LTRO: €489.2 billion to 523 banks | [FACT; ch07-S01] |
| 3 Feb 2012 | Spain's Royal Decree-Law 2/2012 requires about €50 billion of additional write-downs on banks' real estate exposures, including a 7% charge on performing real estate financing | [FACT; ch07-S11] |
| 29 Feb 2012 | Second three-year LTRO: €529.5 billion to 800 banks; about €1.02 trillion in total across the two | [FACT; ch07-S01] |
| March 2012 | Greek private-sector involvement (PSI): about €197 billion of privately held bonds exchanged with a 53.5% cut in face value, reducing debt by about €107 billion | [FACT; ch07-S08] |
| 11 May 2012 | Spain's Royal Decree-Law 18/2012 adds further provisioning on performing real estate developer loans (by type: land, developments in progress, completed developments), reported at about €30 billion | [FACT; ch07-S11] |
| 9 Jun 2012 | Eurogroup agrees to lend Spain up to €100 billion for bank recapitalization | [FACT; ch07-S10] |
| 26 Jun 2012 | Commerzbank announces it will wind down its Commercial Real Estate and Ship Finance businesses (held in Eurohypo), citing Basel III capital and liquidity requirements; its U.K. arm states that no new business lending will take place | [FACT; ch07-S16] |
| July 2012 | Spain's 10-year yield reaches a euro-era record of 7.625% | [FACT; ch07-S07; exact trading day *(verification pending)*] |
| 26 Jul 2012 | Draghi, in London: "Within our mandate, the ECB is ready to do whatever it takes to preserve the euro. And believe me, it will be enough." | [FACT; ch07-S02] |
| 2 Aug 2012 | ECB Governing Council announces it will undertake outright transactions in secondary sovereign bond markets | [FACT; ch07-S03] |
| 6 Sep 2012 | ECB sets out OMT technical features: strict conditionality through an EFSF/ESM program, focus on shorter maturities, full sterilization, no ex ante quantitative limits; the SMP is terminated | [FACT; ch07-S03, ch07-S04] |
| Late 2012 | Spanish asset-management company Sareb announced with estimated average transfer discounts of about 63% for foreclosed assets (about 79.5% for land) and about 45.6% for loans to developers | [FACT as reported; ch07-S12; VERIFIED-SECONDARY; final applied discounts differed] |
| 16 Jun 2015 | EU Court of Justice (Gauweiler) holds that OMT does not exceed the ECB's monetary-policy powers; as of 2015 the program had not been activated | [FACT; ch07-S04] |

### Information available at the time

By mid-2012, the following were public: Greek restructuring had occurred, so euro-area sovereign default was no longer hypothetical. Spain's banks needed external capital, and the government had borrowed from its partners to supply it. The ECB had provided about €1 trillion of three-year funding, and some of it had been used to buy domestic sovereign bonds (the carry trade of Example 7.7(e)) [INFERENCE that some was used this way is widely discussed; amounts by country are not stated here]. Euro-area governments had begun to discuss a banking union.

What was *not* knowable was whether the ECB would act as a backstop for sovereign bond markets, whether its governing council and its member governments would agree, and whether such a backstop would be legal. Those questions were answered between 26 July and 6 September 2012, and the legal question not until 2015.

### Transmission to property values, borrowing costs, and lending capacity

The CRE evidence from the period runs through the channels of §7.2:

* **Discount rate and value.** Irish commercial property capital values fell by over 65% from their 2007 peak, according to IPD/SCSI index reporting, before returning to growth in 2013 [FACT as reported; ch07-S15; VERIFIED-SECONDARY].
* **Bank capital and forced recognition.** NAMA's 57% average discount on €74 billion of loans and the Spanish provisioning decrees of February and May 2012 forced banks to recognize property losses [FACT; ch07-S11, S13]. Recognition reduces capital, which (Example 7.7) reduces lending capacity.
* **Lender exit.** Commerzbank's decision of 26 June 2012 to wind down Eurohypo's commercial real estate finance business removed one of Europe's largest CRE lenders from new lending. The bank cited Basel III capital and liquidity requirements [FACT; ch07-S16]. This is a bank-capital transmission, not a sovereign default.
* **Transfer to state vehicles at deep discounts.** Sareb's announced transfer discounts are a price for illiquid property collateral set in the middle of the crisis [FACT as reported; ch07-S12].

### Competing interpretations

1. **Fundamental insolvency view.** Some sovereigns had debt levels and growth prospects that made debt unsustainable without restructuring. Greece was the clear case. On this view, high spreads were correct pricing of expected loss.
2. **Self-fulfilling crisis (multiple-equilibria) view.** A sovereign without its own central bank can be pushed into default by a rise in yields that itself makes the debt unsustainable. On this view, spreads for Italy and Spain in 2011–12 contained a large premium for a bad equilibrium that a credible lender of last resort could remove. The rapid fall in spreads after the ECB's statements is consistent with this view, although it does not prove it.
3. **Bank-centric view.** The crisis was primarily a banking crisis that became sovereign through guarantees and recapitalizations (Ireland most clearly, Spain later). The doom-loop literature (ch07-S24, S25) supports this view for those countries.

These views are not mutually exclusive. They differ country by country.

### What the case establishes, and what it does not

**Establishes.** (i) Sovereign risk in a currency union transmits to domestic banks, property values, and CRE credit availability. (ii) Policy announcements by a credible central bank can change the risk premium in sovereign spreads without the bank actually buying bonds, at least as of 2015 for OMT. (iii) CRE losses can be recognized suddenly by regulatory decree, which is itself a market event.

**Does not establish.** It does not establish how much of the 2012 spread was expected default loss versus a self-fulfilling premium. It does not establish that a U.S. or U.K. sovereign could experience the same dynamics, since both have their own currencies and central banks. It does not tell you the price at which a Madrid office should have been bought in June 2012; that requires underwriting the specific asset (Example 7.8) and a view on policy.

### Strategies available then (ex ante)

* Buy discounted CRE or loans from forced sellers, sized so that a further 20–30% fall in value does not impair the fund. This is a speculation on policy and on liquidity premia.
* Provide rescue capital (preferred equity, mezzanine) where the refinancing gap is large and the senior lender is capital-constrained.
* Buy short-dated sovereign bonds as a speculation on a central-bank backstop. This had large tail risk until the OMT announcement.
* Wait. Abstention had a real option value, because the policy uncertainty was going to resolve within months.

---

## 7.10 Decision exercise: the Madrid office, late June 2012

Return to §7.1. Use only information available on 30 June 2012: the Eurogroup's 9 June agreement, the Spanish provisioning decrees, the LTROs, the Greek PSI, and the record yields. **Do not use** Draghi's 26 July statement, OMT, or later developments.

Using the numbers of Example 7.8, prepare a decision record on the template at `desk/investment_memos/decision_record_template.md`. Address:

1. **The option set.** (a) Buy the building at a price you set. (b) Buy the €52 million loan at a discount. (c) Provide the €17.9 million refinancing gap as preferred equity. (d) Buy U.S. Treasuries. (e) Wait 3–6 months.
2. **Value range.** Value the building at cap rates of 6.0%, 6.5%, and 7.0% on NOI of €3.8 million and on a further 10% NOI decline. Say which cap rate is a sovereign-risk premium that could reverse and which is a permanent re-rating.
3. **Currency.** For a dollar investor, compute the hedged and unhedged return framework. In June 2012, euro short rates were close to U.S. short rates, so the hedge cost was small [HYPOTHESIS for this exercise; check historical forward points before relying on it]. The main currency risk was redenomination, which a forward does not hedge. Explain why.
4. **Counterparty.** The selling bank's position (Example 7.7). Is the discount compensation for its forced selling, for your bearing sovereign risk, or for asymmetric information about the asset (Chapter 1, Example 1.7)?
5. **Sizing and invalidation.** Maximum exposure as a share of the \$300 million. What event would make you exit or stop deploying (e.g., Spanish exit from the euro becoming explicit policy, or a bank resolution that cancels your contractual rights)?
6. **What you will not do.**

**Rubric (`problems/solutions/ch07_solutions.md` §Decision exercise).** Full credit requires: a value range that separates sovereign premium from property fundamentals; recognition that the forward hedge does not protect against redenomination; a structure (loan purchase or preferred equity) that sits above the existing equity; sizing that survives a further 30% value fall; explicit consideration of waiting; and no use of hindsight. There is no single correct answer. A committee that waited and a committee that bought a loan at 60–70% of par with protective covenants could both receive full credit.

---

## 7.11 Frequent analytical errors

1. **Reading the debt ratio without $r - g$.** A 120% ratio with $r < g$ can be more stable than a 60% ratio with $r \gg g$. Always compute $pb^*$.
2. **Using the marginal yield as the effective rate.** The effective rate on the debt stock follows market yields with a lag set by maturity. Debt dynamics deteriorate slowly and then persistently.
3. **Treating a sovereign spread as expected loss.** Risk-neutral default probabilities include premia. Inside a currency union they include redenomination risk.
4. **Ignoring the recovery assumption.** A 320 bp spread implies a five-year default probability of 19% at 25% recovery and 23% at 40%. State the recovery used.
5. **Measuring Treasury supply in dollars.** A \$25 billion 30-year auction carries more DV01 than a \$42 billion 10-year auction.
6. **Presenting a deficit-to-yield coefficient as a law.** Published estimates vary over time and across samples. Use them for scenarios.
7. **Comparing unhedged foreign yields with home yields.** The hedge cost is the short-rate differential. A higher foreign long yield can mean a lower hedged return.
8. **Getting the FX quote direction wrong.** For a euro investor, the home value of one dollar is $1/S_{EUR/USD}$. EUR/USD rising is the dollar *weakening*.
9. **Hedging an illiquid asset with a short-dated cash-settled hedge without a liquidity reserve.** A 10% currency move can require a cash payment of more than 10% of equity.
10. **Underwriting the property and not the lender.** In a sovereign-stress environment, refinancing risk depends on the lender's capital as much as on the property's DSCR.
11. **Calling an identity a forecast.** $CA = (S_p - I) + (T - G)$ does not predict the current account. It constrains the possibilities.
12. **Assuming a peg is permanent.** A peg is a policy, and policies end.

---

## 7.12 Connections to other chapters

* **Chapter 5** develops central-bank reaction functions. The ECB's 2012 actions are a central bank acting as lender of last resort under legal constraints.
* **Chapter 6** develops duration, DV01, and the cap-rate/Treasury spread used in Examples 7.3 and 7.8.
* **Chapter 10** develops loan sizing (LTV, DSCR, debt yield) and refinancing gaps used in Example 7.8.
* **Chapter 12** develops distressed CRE opportunity, loan sales, and maturity walls, including rescue capital.
* **Chapter 15** develops FX in depth: quote conventions, carry trades, and hedged returns on foreign property.
* **Chapter 17** develops hazard rates, recovery, and spread ≈ PD × LGD for corporate and CMBS credit.
* **Chapter 23** examines the ERM crisis of 1992 (a peg under the trilemma), Asia 1997, and 2022 in detail.
* **Case H** (cross-asset macro shock) applies the chapter's transmission channels to a multi-asset portfolio.

---

## 7.13 One-page reference sheet

**Questions on fiscal or sovereign news.** Did $r$, $g$, or $pb$ change, and is it persistent? Is the spread expected loss, premium, or redenomination? Who holds the debt and how leveraged are they? Who is the marginal foreign buyer and are they hedged? What does the local banking system own? Which of the five channels reaches my asset?

| Concept | Formula |
|---|---|
| Debt law of motion | $d_{t+1} = d_t(1+r)/(1+g) - pb_{t+1}$ |
| Change in debt ratio | $\Delta d = d(r-g)/(1+g) - pb$ |
| Debt-stabilizing primary balance | $pb^* = d(r-g)/(1+g)$ |
| Steady state ($r<g$, constant $pb$) | $d^* = -pb(1+g)/(g-r)$ |
| Effective-rate adjustment | $r_t = r_{t-1} + (1/\text{WAM})(r^{mkt} - r_{t-1})$ |
| Spread and default | $s \approx p \times \text{LGD}$; exact one-period $p = [1-(1+r_f)/(1+y)]/\text{LGD}$ |
| Hazard rate | $\lambda \approx s/(1-R)$; $P(\text{default by }T) = 1 - e^{-\lambda T}$ |
| Spread decomposition | $s = p^{phys}\text{LGD} + \pi_{risk} + \pi_{liq} + \pi_{redenom}$ |
| CDS–bond basis | $s_{CDS} - s_{bond}$ |
| Auction DV01 | Face/100 × DV01 per 100; 10-yr equivalents = Face × DV01/DV01$_{10}$ |
| Savings–investment | $CA = (S_p - I) + (T-G)$; $FA \approx CA$ |
| Reserves under a peg | $\Delta\text{Reserves} = CA + \text{private net inflows}$ |
| CIP forward (BASE/QUOTE) | $F = S(1 + r_{quote}t)/(1 + r_{base}t)$ |
| Hedged return | $(1+y)(1+r_{home})/(1+r_{foreign}) - 1 \approx y - (r_{foreign} - r_{home})$ |
| Unhedged return | $(1+y)(1+x) - 1$, $x$ = % change in home value of one unit of foreign currency |
| Doom-loop capital loss | $\Delta E \approx -B D \Delta s$ |
| Forced shrinkage | $(A + \Delta E) - (E + \Delta E)/\ell$ |
| Cap-rate value shock | $V_1/V_0 - 1 = c_0/c_1 - 1$ (NOI constant) |

**Numbers to remember (all from this chapter's examples, hypothetical).** At $d = 100\%$, 1 point of $r - g$ ≈ 1 point of GDP per year of debt drift. A 30-year bond has roughly twice the DV01 of a 10-year. A hedged euro investor's hedge cost ≈ $r_{USD} - r_{EUR}$. A 6% leverage-ratio bank shrinks roughly 17 euros of assets for every euro of capital lost.

---

## References for this chapter

Source IDs refer to `references/sources_ch07.md`.

* Acharya, V. V., Drechsler, I., and Schnabl, P. (2014). "A Pyrrhic Victory? Bank Bailouts and Sovereign Credit Risk." *Journal of Finance*, 69(6), 2689–2739. [ch07-S24]
* Adrian, T., Crump, R. K., and Moench, E. (2013). "Pricing the Term Structure with Linear Regressions." *Journal of Financial Economics*. [ch07-S30; page range *(verification pending)*]
* Bank of England (2022). Statements on gilt market operations, 28 September–17 October 2022; Governor's letter to the Chancellor, 16 January 2023. [ch07-S17]
* Blanchard, O. (2019). "Public Debt and Low Interest Rates." *American Economic Review*, 109(4), 1197–1229. [ch07-S23]
* Brunnermeier, M. K., Garicano, L., Lane, P. R., Pagano, M., Reis, R., Santos, T., Thesmar, D., Van Nieuwerburgh, S., and Vayanos, D. (2016). "The Sovereign-Bank Diabolic Loop and ESBies." *American Economic Review: Papers & Proceedings*, 106(5), 508–512. [ch07-S25]
* Congressional Budget Office (2026). *The Budget and Economic Outlook: 2026 to 2036* (February 2026), as summarized by the Committee for a Responsible Federal Budget. [ch07-S19]
* Draghi, M. (2012). Speech at the Global Investment Conference, London, 26 July 2012. BIS Central Bankers' Review r120727d. [ch07-S02]
* Du, W., Tepper, A., and Verdelhan, A. (2018). "Deviations from Covered Interest Rate Parity." *Journal of Finance*, 73(3), 915–957. [ch07-S27]
* European Central Bank (2012). "Technical features of Outright Monetary Transactions." Press release, 6 September 2012. [ch07-S03]
* Laubach, T. (2009). "New Evidence on the Interest Rate Effects of Budget Deficits and Debt." *Journal of the European Economic Association*, 7(4), 858–885. [ch07-S22]
* Obstfeld, M., Shambaugh, J. C., and Taylor, A. M. (2005). "The Trilemma in History: Tradeoffs among Exchange Rates, Monetary Policies, and Capital Mobility." *Review of Economics and Statistics*, 87(3), 423–438. [ch07-S26]
* U.S. Bureau of Economic Analysis (2025). "U.S. International Transactions, 4th Quarter and Year 2024." [ch07-S20]
* U.S. Department of the Treasury (2026). Quarterly Refunding Statement, August 2026. [ch07-S21]
* Further official and secondary sources for §7.9 (ECB, ESM, Eurogroup, Banco de España decrees via Uría Menéndez, NAMA, Central Bank of Ireland, Commerzbank, SNB, HKMA) are listed with status in `references/sources_ch07.md`.
