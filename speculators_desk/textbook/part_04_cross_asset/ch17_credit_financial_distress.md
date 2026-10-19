# Chapter 17 — Credit and Financial Distress

> **Status:** Complete (v1.0). Numerical examples are reproduced in `tests/test_ch17_examples.py` using `models/python/sdesk/x_credit.py`. Problems are in `problems/questions/ch17_problems.md` and solutions in `problems/solutions/ch17_solutions.md`. Sources are in `references/sources_ch17.md`. Several historical figures in §17.8 are VERIFIED-SECONDARY only (web-search excerpts) and are flagged in the text; the peak level of AAA CMBS and high-yield spreads in late 2008 is *(verification pending)*.

## Learning objectives

After this chapter you should be able to:

1. Convert between cumulative default probabilities, constant hazard rates and one-year default probabilities, and use the credit triangle $s \approx \lambda \cdot LGD$ in both directions without confusing risk-neutral and real-world probabilities.
2. Decompose a corporate bond spread into expected loss, a liquidity component and a residual risk premium, and say which of the three you are being paid for.
3. Apply absolute priority to a Chapter 11 capital structure, identify the **fulcrum security**, and explain why the fulcrum, not the cheapest bond, is where control and most of the upside sit.
4. Quantify **structural subordination**: what a holding-company creditor recovers when its only asset is the equity of an operating company, and what an upstream guarantee changes.
5. Price a distressed bond purchase from a recovery distribution, and compute the break-even probability of the bad outcome.
6. Explain CDS mechanics, compute the upfront payment for a standard running coupon, mark a CDS position to market, and recognize when a CDS does not hedge the bond you own.
7. Allocate a pool loss across CMBS tranches, compute credit enhancement and the default rate at which a tranche is first impaired, and connect the result to the capital stack of Chapter 10 and the special servicing of Chapter 12.
8. Value CRE equity as a call on property value with the Merton model, and use it to show why a sponsor with underwater equity prefers volatility.

---

## 17.1 Opening investment problem: one hotel company, three ways to bet

You run a \$60 million opportunistic credit sleeve for a family office that also owns hotels directly. All facts in this section are [HYPOTHESIS], a constructed teaching case.

**The issuer.** Harborline Hospitality Holdings ("Holdco") owns 100% of Harborline Hotel Operating LLC ("Opco"). Opco owns and operates 22 select-service hotels. Holdco has no other assets. The liabilities are:

| Entity | Claim | Amount |
|---|---|---|
| Opco | Secured bank term loan (lien on all hotels) | \$250 million |
| Opco | Senior unsecured notes | \$100 million |
| Opco | Trade payables and other general unsecured claims | \$30 million |
| Holdco | 8.0% senior unsecured notes (no Opco guarantee) | \$200 million |

Group EBITDA has fallen after a regional supply wave and a franchise dispute. Management has hired restructuring advisers, and a Chapter 11 filing within weeks is widely expected. Your hotel team, which knows these markets, puts Opco's enterprise value at emergence (about 18 months out) at \$400 million in a bad case, \$500 million in a base case, and \$600 million in a good case.

**Opportunity A — the Holdco notes.** A dealer offers \$20 million face of the Holdco notes at 38 (38% of face).

**Opportunity B — a CMBS bond.** A different dealer offers \$15 million face of the Class D bond of a 2019 conduit CMBS. It is rated at the bottom of investment grade, has 6.5% credit enhancement, and the pool is 25% office. The price is 72.

**Opportunity C — the CDS.** Five-year CDS on Harborline Hotel Operating LLC is quoted at 650 bp, which trades as an upfront payment plus a 500 bp running coupon. A colleague proposes buying the Holdco notes and "hedging" with Opco protection.

You also have the alternative of doing nothing and holding Treasury bills.

By the end of the chapter you will be able to say which of the Harborline claims is the fulcrum in each value scenario, what the Holdco notes are worth, whether Opco protection hedges anything you own, what pool loss the CMBS bond can absorb, and whether any of the three deserves capital. Section 17.9 returns to the decision.

---

## 17.2 Economic intuition

### Credit is a short put, and the spread is its premium

Chapter 10 established that a non-recourse lender owns a riskless claim minus a put on the collateral. Corporate credit has the same structure. The bondholder receives the promised payments unless the firm's value falls below what it owes, in which case the bondholder receives a share of what is left. The **credit spread**, the yield on the bond minus the yield on a riskless bond of the same maturity, is the annualized price of that put.

Three things follow, and they organize the chapter.

1. **The payoff is capped above and open below.** A bond bought at par can earn its coupon and no more. It can lose most of its principal. A credit investor makes money by avoiding losers more than by picking winners. Distressed investing reverses this: a bond bought at 38 has a payoff that looks like equity.
2. **The spread is larger than the expected loss.** Holders demand compensation for the expected loss, for bearing default risk that concentrates in recessions, and for the cost and risk of trading an illiquid instrument. How the spread divides among these components determines what you are actually paid for.
3. **What you recover depends on where you sit.** Default does not end a credit analysis. It starts the second part: who gets the remaining value, in what order, and after how long. In U.S. corporate bankruptcy that order is set by absolute priority, contractual subordination and the corporate structure.

### Corporate bonds and high yield

A corporate bond is a fixed-income claim governed by an **indenture**. The indenture sets the coupon, maturity, call schedule, ranking, any security, guarantees by subsidiaries, and covenants. Bonds rated BBB−/Baa3 or better are **investment grade**. Below that they are **high yield** (also called speculative grade or "junk"). The boundary matters for reasons that have little to do with default risk. Many insurers, pension funds and bank portfolios face capital charges or mandate limits on high-yield holdings. A downgrade across the line (a "fallen angel") therefore forces sales by holders who cannot keep the bond. Forced selling is a liquidity event, and Chapter 1's analysis of liquidity provision applies directly: the buyer of fallen angels is paid for immediacy.

High-yield indentures differ from investment-grade ones in three ways that matter to a speculator.

* **Covenants are incurrence-based.** They restrict actions (new debt, dividends, asset sales, investments in unrestricted subsidiaries) only when the issuer takes them. Bank loans often carry maintenance covenants tested every quarter. A high-yield bond can therefore stay current while the issuer's coverage collapses. The trigger for a restructuring is usually a maturity, a missed coupon or a bank covenant, not the bond indenture.
* **Calls make the bond's upside shorter.** A callable high-yield bond is priced to its **yield to worst**, the lowest yield across the call dates and maturity. A bond trading above its call price earns less than its stated yield if the issuer refinances.
* **Recovery matters as much as default.** At investment grade, default risk is small and recovery is a second-order issue. In high yield, the expected loss is a product of a meaningful default probability and a recovery that varies widely by ranking.

### Distressed debt: buying at a discount

A bond trading below about 60–70% of face, or at a spread over about 1,000 bp, is usually treated as **distressed** [HYPOTHESIS: market conventions vary and are not standardized]. At these prices the bond no longer trades on its coupon. It trades on the **recovery value** the holder will receive in a restructuring, discounted for time and uncertainty. The analysis changes from a yield calculation to a valuation of the firm plus a legal analysis of who gets what.

The central concept is the **fulcrum security**: the most senior class of claims that is *not* paid in full at the estimated enterprise value. Claims senior to the fulcrum are paid in full and usually receive cash or new debt. Claims junior to it receive nothing or a nominal amount. The fulcrum class receives most of the equity of the reorganized company. Owning the fulcrum therefore gives an investor three things: the residual upside if the enterprise value turns out higher than the plan valuation, votes on the plan, and often board seats. Distressed investors spend much of their effort deciding which class is the fulcrum, because a disagreement about enterprise value is a disagreement about which class becomes the new owner.

### Recovery rates: secured versus unsecured

Recovery depends on ranking and collateral. Moody's studies of defaulted debt report that average recoveries fall with seniority. For instruments defaulting from 1987 to 2008, Moody's reported average recoveries of about 80.7% for loans, 63.7% for senior secured bonds, 48.9% for senior unsecured bonds and 28.7% for subordinated debt [FACT; Moody's, as reported by CFO.com; VERIFIED-SECONDARY, ch17-S01]. A later update covering 1987–2022, cited by an asset manager, gives 61.2%, 47.1% and 27.8% for senior secured, senior unsecured and subordinated bonds [FACT; VERIFIED-SECONDARY, ch17-S02]. Recoveries also fall when defaults are widespread: the Reserve Bank of Australia reported that the average recovery on defaulted senior unsecured bonds fell to 38% in 2009 [FACT; VERIFIED-SECONDARY, ch17-S03]. Whether each of these figures measures recovery at emergence or the trading price shortly after default should be confirmed in the primary studies before relying on the exact levels *(verification pending)*. The ranking is robust across studies. The levels are not stable, and they are lowest in exactly the years you are most likely to need them.

Two cautions apply to any historical recovery average. First, it is an average over firms with very different asset bases. A hotel company whose assets are real estate should recover more than a software company whose assets leave the building every evening, all else equal. Second, recovery is negatively correlated with the default rate. Using a long-run average recovery in a recession scenario double-counts good times.

### Default probabilities and hazard rates

Rating agencies publish **cumulative default rates**: the fraction of issuers with a given rating that defaulted within $t$ years. Pricing models use a **hazard rate** $\lambda$, the instantaneous default rate conditional on survival. Under a constant hazard, the probability of surviving to $t$ is $e^{-\lambda t}$. The hazard is not the one-year default probability, and five times a one-year probability is not the five-year cumulative probability. The errors are small for strong credits and material for weak ones (Example 17.1).

The **credit triangle** links spread, hazard and loss given default: $s \approx \lambda \cdot LGD$, with $LGD = 1 - R$. It is the single most useful relationship in credit. Its weakness is that the $\lambda$ it backs out of a market spread is a **risk-neutral** hazard. It contains every premium in the spread. It is not a forecast of the real-world default rate. The ratio of risk-neutral to real-world hazard is routinely several times one for investment-grade credits [INFERENCE from the spread-puzzle literature, e.g., Elton, Gruber, Agrawal and Mann (2001), who find that expected default accounts for a small fraction of corporate spreads; VERIFIED-PRIMARY bibliographic, ch17-S07].

### Capital structure and absolute priority

In a U.S. Chapter 11 reorganization, a plan can be confirmed over the objection of a dissenting impaired class of unsecured creditors only if that class is paid in full or no junior class receives anything. This is the **absolute priority rule** of 11 U.S.C. §1129(b)(2)(B) [FACT; VERIFIED-SECONDARY, ch17-S08]. Secured claims are paid from their collateral. An undersecured creditor's claim is split under §506(a) into a secured claim equal to the collateral value and an unsecured **deficiency claim** [FACT; ch17-S08]. Interest stops accruing on unsecured claims at the petition date under §502(b)(2), subject to a solvent-debtor exception [FACT; ch17-S08]. The waterfall is therefore:

1. Administrative and priority claims (professional fees, post-petition costs, some taxes and wages, any debtor-in-possession loan).
2. Secured claims, up to their collateral value, in lien priority.
3. General unsecured claims, pari passu: unsecured bonds, trade claims, deficiency claims, rejected-lease and rejected-contract damages.
4. Contractually subordinated claims.
5. Preferred and then common equity.

Negotiated plans often deviate from this order at the margin. Seniors give juniors a small distribution to avoid litigation or to speed confirmation. The rule is a bargaining baseline, not a guaranteed outcome (§17.7).

### Structural subordination: holdco versus opco

Absolute priority applies entity by entity. A creditor of a parent holding company has no claim against the assets of its subsidiaries. It has a claim on the parent's assets, and the parent's main asset is the subsidiaries' equity. Every creditor of the subsidiary, including trade creditors, is paid before a single dollar reaches the parent. This is **structural subordination**. It is often worse than contractual subordination because it puts the holdco creditor behind claims it cannot see in the parent's financial statements.

The fix is an **upstream guarantee**: the subsidiary guarantees the parent's notes, which gives the noteholders a direct claim against the subsidiary that ranks pari passu with the subsidiary's other unsecured creditors. Whether a guarantee exists, whether it is limited, and whether any subsidiary has been designated "unrestricted" (released from the covenant package and the guarantee) are among the first facts a distressed analyst checks.

The CRE analogue is precise. A mezzanine loan is secured by a pledge of the equity in the property-owning entity, not by the property. It is structurally subordinated to the mortgage. A REIT's unsecured bonds are structurally subordinated to the mortgages on its encumbered properties, which is why REIT bond indentures limit secured debt and require a minimum ratio of unencumbered assets to unsecured debt.

### Liquidity

Corporate bonds trade over the counter. Most individual issues trade infrequently, and dealer balance sheets absorb order imbalances only up to their risk limits. A bond's spread therefore contains a **liquidity component**: compensation for the bid–ask cost the holder expects to pay and for the risk that selling quickly will be expensive exactly when the holder needs to sell. Longstaff, Mithal and Neis (2005) use CDS spreads, which carry less of the bond's liquidity premium, to separate the two. They find that default risk accounts for roughly half to over four-fifths of corporate spreads, depending on rating and the riskless benchmark, and that the remainder is time-varying and related to bond-specific and market-wide illiquidity [FACT; VERIFIED-SECONDARY for the 50–83% range, ch17-S06].

For a hold-to-maturity investor, the liquidity component is earned. For an investor who may need to sell in a crisis, it is compensation for a risk that will be realized at the worst time.

### Credit derivatives

A **credit default swap** transfers the credit risk of a reference entity. The **protection buyer** pays a periodic premium. The **protection seller** pays the loss on a defaulted obligation after a **credit event** (bankruptcy, failure to pay, and for some contracts restructuring). Since the 2009 "Big Bang" protocol, North American single-name CDS trade with a standard fixed running coupon of 100 bp for investment-grade names or 500 bp for high-yield names, with an **upfront payment** that makes up the difference between the quoted spread and the fixed coupon. Premiums are paid on standard quarterly dates (20 March, June, September and December), and the recovery value after a credit event is fixed by an auction [FACT; BIS Quarterly Review (December 2010) and ISDA-protocol commentary; VERIFIED-SECONDARY, ch17-S09].

A CDS is a contract on one legal entity. It does not reference a corporate group. Protection on Opco pays only if Opco has a credit event, and it pays the loss on Opco's deliverable obligations, not on Holdco's. That single fact settles the colleague's hedging proposal in §17.1 (Example 17.6).

### CMBS and structured credit

A CMBS trust holds a pool of commercial mortgages and issues bonds in a sequence of **tranches**. Principal is generally paid to the most senior class first (sequential pay). Realized losses are allocated from the bottom up. A tranche is defined by its **attachment point** $a$ (the pool loss, as a fraction of the pool, at which the tranche starts to lose) and its **detachment point** $d$ (the loss at which it is wiped out). Its **credit enhancement** is its attachment point: the share of the pool that is junior to it.

This is the same arithmetic as the property capital stack in Chapter 10, with two differences. First, the collateral is a pool of loans, so the loss depends on how many loans default and how much is lost on each (the **severity**). Correlation between loans, not the average default rate alone, determines the risk of senior tranches. Second, a pool's losses arrive through special servicing (Chapter 12). Appraisal reductions and servicer advance decisions cut interest to the junior bonds before any principal loss is realized.

### The Merton view: CRE equity as a call

Merton (1974) treated a firm's equity as a European call option on the firm's assets, struck at the face value of its debt [FACT: bibliographic; ch17-S05]. Debt is then the asset value minus the call, or a riskless bond minus a put. The model turns credit questions into option questions: the spread rises with leverage, volatility and time to maturity. The equity holder gains from volatility at the lender's expense.

For a single-asset CRE borrower the model fits better than it does for most corporations. The asset is one building. The debt is a single mortgage with a known balloon. The borrower's choice at maturity is close to the exercise decision of a call. The weak points are the inputs: the property's volatility must be estimated from appraisal-smoothed data (Chapter 2), and default in practice happens when the loan cannot be refinanced, not when value crosses the balance.

---

## 17.3 Technical definitions

| Term | Definition |
|---|---|
| Credit spread $s$ | Yield on the risky bond minus the yield on a riskless bond (Treasury or swap) of the same maturity, in the same compounding convention |
| Hazard rate $\lambda$ | Instantaneous default intensity conditional on survival; survival to $t$ is $S(t) = e^{-\int_0^t \lambda(u)du}$, or $e^{-\lambda t}$ if constant |
| Cumulative PD | $PD(t) = 1 - S(t)$, probability of default by $t$ |
| Conditional (marginal) PD | $[PD(t_2) - PD(t_1)]/[1 - PD(t_1)]$, probability of default in $(t_1, t_2]$ given survival to $t_1$ |
| Recovery rate $R$ | Value received per unit of claim after default, as a fraction of face (par) |
| LGD | Loss given default, $1 - R$ |
| Expected loss (annual) | $PD_{1y} \times LGD$, using a real-world probability |
| Risk-neutral hazard | The hazard implied by market prices; includes risk and liquidity premia |
| Credit triangle | $s \approx \lambda (1 - R)$ |
| Yield to worst | Lowest of the yields to each call date and to maturity |
| Distressed debt | Debt trading at a deep discount because default or restructuring is likely; priced on recovery, not on coupon |
| Fulcrum security | The most senior class not paid in full at the estimated enterprise value; normally receives most of the reorganized equity |
| Absolute priority | No junior class receives value until each senior class is paid in full (the cram-down standard of §1129(b)(2)(B)) |
| Deficiency claim | The part of an undersecured creditor's claim exceeding collateral value, treated as unsecured (§506(a)) |
| Structural subordination | Ranking of a parent's creditors behind all creditors of its subsidiaries, because the parent owns only the subsidiaries' equity |
| Upstream guarantee | A subsidiary's guarantee of parent debt; removes structural subordination to the extent of the guarantee |
| CDS | Contract paying $(1 - R)$ times notional after a credit event of the reference entity, in exchange for a running premium |
| Running coupon $c$ | Fixed CDS premium, 100 bp or 500 bp for standard North American contracts |
| Upfront | PV paid at inception by the protection buyer (if positive) to compensate for $s \ne c$ |
| RPV01 (risky annuity) | PV of 1 per year of premium paid until the earlier of default or maturity |
| Attachment $a$ / detachment $d$ | Pool loss fractions at which a tranche starts to lose and is wiped out |
| Credit enhancement (CE) | Share of the current pool balance junior to a tranche; equals $a$ at issuance |
| Severity | Loss on a defaulted loan as a fraction of its balance |
| Pool loss | Default rate × severity (fraction of the pool) |
| Merton model | Equity = call on asset value struck at the face of zero-coupon debt |
| Distance to default | $d_2$ in the Merton model: standard deviations by which expected log asset value at $T$ exceeds the log of debt face |

---

## 17.4 Equations and derivations

### 17.4.1 Hazard rates and cumulative default probability

Let $\lambda$ be a constant hazard. The probability of surviving a short interval $dt$, conditional on surviving to $t$, is $1 - \lambda\,dt$. So $dS/dt = -\lambda S$, and

$$S(t) = e^{-\lambda t}, \qquad PD(t) = 1 - e^{-\lambda t}, \qquad \lambda = -\frac{\ln(1 - PD(t))}{t}.$$

The one-year default probability is $PD_{1y} = 1 - e^{-\lambda}$, which is slightly less than $\lambda$. For two horizons $t_1 < t_2$ the average (forward) hazard between them is

$$\lambda_{t_1,t_2} = \frac{\ln S(t_1) - \ln S(t_2)}{t_2 - t_1}.$$

Agency tables usually show cumulative default rates rising faster than linearly for strong credits (a firm must first deteriorate before it defaults) and more slowly for weak ones (survivors are firms that have recovered). A constant hazard is a simplification that should be checked against the term structure of the table you use.

### 17.4.2 The credit triangle

Assume a constant hazard $\lambda$, a constant riskless rate $r$, recovery $R$ of par paid at the moment of default, and a premium paid continuously at rate $s$. The PV of the premium leg per unit of notional is

$$PV_{prem} = s\int_0^T e^{-(r+\lambda)t}dt = s\,\frac{1 - e^{-(r+\lambda)T}}{r + \lambda}.$$

The protection leg pays $(1 - R)$ at the default time, whose density is $\lambda e^{-\lambda t}$:

$$PV_{prot} = (1 - R)\int_0^T \lambda e^{-\lambda t}e^{-rt}dt = (1 - R)\,\lambda\,\frac{1 - e^{-(r+\lambda)T}}{r + \lambda}.$$

Setting the two equal gives the par spread exactly:

$$s = \lambda (1 - R).$$

With quarterly premium payments and no accrued premium on default, the par spread is slightly higher than $\lambda(1-R)$, because the protection seller loses part of a quarter's premium when default occurs between payment dates. The standard ISDA model includes accrued premium, so the triangle is very close for it. The relationship holds for bonds as well, approximately: a par floating-rate bond with recovery of par earns a spread of about $\lambda(1 - R)$ over the riskless rate.

### 17.4.3 Spread decomposition

Write the observed spread as

$$s = \underbrace{PD_{1y}^{P}\,(1 - R)}_{\text{expected loss}} + \underbrace{\ell}_{\text{liquidity}} + \underbrace{\pi}_{\text{risk premium (residual)}}.$$

Here $PD^P$ is a real-world (physical) default probability, estimated from history or a model. $\ell$ is the liquidity component, estimated from bid–ask costs, from the bond–CDS basis, or from the yield difference between more and less liquid issues of the same issuer. $\pi$ is everything else: compensation for default risk that concentrates in bad states, and, in practice, the errors in the other two estimates. Elton, Gruber, Agrawal and Mann (2001) also identify a state-tax component for U.S. corporate bonds, because Treasury interest is exempt from state income tax [FACT; ch17-S07]. We fold it into $\pi$.

The risk-neutral hazard implied by the default-related part of the spread is $\lambda^Q = (s - \ell)/(1 - R)$. The ratio $\lambda^Q/PD^P$ measures how much the market charges per unit of expected default.

### 17.4.4 The absolute-priority waterfall

Order the classes $j = 1, \dots, J$ from senior to junior, with claims $C_j$. Pari passu claims form one class and share pro rata. With distributable value $V$, the amount paid to class $j$ is

$$P_j = \min\Big(C_j,\ \max\big(V - \textstyle\sum_{k<j} C_k,\ 0\big)\Big), \qquad R_j = P_j / C_j.$$

The fulcrum is the smallest $j$ with $R_j < 1$. Within a pari passu class, member $i$ receives $P_j \cdot C_{ij}/C_j$. Old equity receives $\max(V - \sum_j C_j, 0)$.

### 17.4.5 Structural subordination

For a holdco whose only asset is the equity of an opco:

$$V_{holdco} = \max\Big(V_{opco} - \sum_{k \in opco} C_k,\ 0\Big) + A_{holdco}^{other},$$

and the holdco's creditors run their own waterfall on $V_{holdco}$. An upstream guarantee from opco moves the holdco notes into opco's unsecured class, where they share pro rata with opco's unsecured creditors.

### 17.4.6 CDS valuation: upfront and running spread

With quarterly payment dates $t_i = i/4$ and a flat hazard, the risky annuity is

$$RPV01 = \sum_{i=1}^{4T} \tfrac{1}{4}\, e^{-(r+\lambda)t_i}.$$

A contract with running coupon $c$ and par spread $s$ has upfront value (paid by the protection buyer, per unit notional)

$$U = PV_{prot} - c \cdot RPV01 = (s - c)\cdot RPV01.$$

The desk approximation takes $\lambda = s/(1 - R)$ from the triangle and computes $RPV01$ from it. The mark-to-market of an existing position after the spread moves from $s_0$ to $s_1$ is the change in upfront value: $\Delta U = U(s_1) - U(s_0)$, approximately $(s_1 - s_0)\cdot RPV01$. The approximation ignores that $RPV01$ itself falls as spreads widen, so it overstates the gain for a protection buyer when spreads widen and overstates the loss when they tighten.

### 17.4.7 Tranche loss and credit enhancement

For pool loss $L$ (a fraction of the original pool), the fractional loss of tranche $[a, d]$ is

$$\ell(a,d) = \frac{\min\big(\max(L - a, 0),\ d - a\big)}{d - a}.$$

With default rate $DR$ and severity $\delta$, $L = DR \times \delta$. The tranche is first impaired at $DR = a/\delta$ and wiped out at $DR = d/\delta$. After senior principal is repaid sequentially, a class's credit enhancement is

$$CE_t = \frac{\text{balance of all junior classes}}{\text{current pool balance}},$$

which rises as the pool pays down, if no losses have occurred.

### 17.4.8 The Merton model

Let property value follow geometric Brownian motion with volatility $\sigma$ and payout yield $q$, and let the debt be a zero-coupon claim with face $F$ due at $T$. Equity is a call:

$$E = V e^{-qT}N(d_1) - F e^{-rT}N(d_2), \qquad d_{1,2} = \frac{\ln(V/F) + (r - q \pm \tfrac12\sigma^2)T}{\sigma\sqrt T}.$$

Debt is $D = Ve^{-qT} - E$. Its continuously compounded yield is $y = \ln(F/D)/T$ and its spread is $y - r$. The risk-neutral probability that $V_T < F$ is $N(-d_2)$. Because $\partial E/\partial \sigma > 0$ (vega is positive), an increase in volatility transfers value from the lender to the equity holder with no change in $V$.

---

## 17.5 Worked examples

All inputs are [HYPOTHESIS] unless cited. All eight examples are reproduced in `tests/test_ch17_examples.py`.

### Example 17.1 — Hazard rates, cumulative PD and the credit triangle in both directions

**Given.** (a) A rating class has a five-year cumulative default rate of 10.0%. Recovery 40%. (b) Separately, a high-yield issuer's five-year CDS trades at a par spread of 450 bp with assumed recovery 40%.

**Find.** (a) The constant hazard, the one-year PD and the triangle spread implied by the 10% cumulative rate. (b) The hazard, one-year PD and five-year cumulative PD implied by the 450 bp spread, and the error from treating the hazard as an annual probability.

**Solution.**

(a) $\lambda = -\ln(1 - 0.10)/5 = 0.105361/5 = 0.021072$, or **2.107%** per year.
$PD_{1y} = 1 - e^{-0.021072} = $ **2.085%**. The naive "10%/5 = 2.0% a year" is close here.
Triangle spread $= 0.021072 \times 0.60 = 0.012643$, or **126.4 bp**. This is the spread that would compensate *only* for expected default losses if the cumulative rate were a real-world probability.

(b) $\lambda = 0.0450/0.60 = $ **7.50%**.
Five-year cumulative PD $= 1 - e^{-0.075 \times 5} = 1 - e^{-0.375} = 1 - 0.687289 = $ **31.27%**.
$PD_{1y} = 1 - e^{-0.075} = $ **7.23%**.
Treating 7.5% as an annual probability and compounding survival, $1 - (1 - 0.075)^5 = $ **32.28%**, overstates the five-year PD by about 1 percentage point.

**Check.** Reverse (b): $-\ln(1 - 0.312711)/5 = 0.375/5 = 0.075$. ✓

**Decision consequence.** The 450 bp spread implies a 31% *risk-neutral* chance of default within five years. A credit analyst who believes the real-world probability is 12% is not finding a bargain on that number alone. The difference between 31% and 12% is the market's price for risk and liquidity, and it is earned only by holding through the states where defaults cluster. The comparison that matters is (a) against (b): a 126 bp spread compensates a 10% cumulative default rate at cost, so any spread above that is premium, and the analyst must say what the premium is for.

Reproduce: `tests/test_ch17_examples.py::test_example_17_1`

### Example 17.2 — What a BB spread pays you for

**Given.** A BB-rated bond: 6.75% coupon paid semiannually, five years to maturity, price 96.50. Five-year Treasury yield 4.10% (bond-equivalent). Your estimate of the real-world annual default probability: 1.20%. Recovery 45%. Liquidity component, estimated from the issuer's bond–CDS basis: 60 bp. Expected round-trip trading cost: 1.0 point of price. Expected holding period: two years.

**Find.** The yield and spread; the decomposition into expected loss, liquidity and risk premium; the risk-neutral hazard and its ratio to the real-world PD; and the spread-equivalent cost of trading.

**Solution.**

Yield to maturity solves $96.50 = \sum_{k=1}^{10} \frac{3.375}{(1+y/2)^k} + \frac{100}{(1+y/2)^{10}}$, giving $y = $ **7.605%** (Excel: `=YIELD(...)` on a coupon date, or `=RATE(10, 3.375, -96.5, 100)*2`).
Spread $= 7.605\% - 4.10\% = $ **350.5 bp**.

Expected loss $= 0.0120 \times 0.55 = 0.0066$, or **66 bp**.
Liquidity $= $ **60 bp**.
Residual risk premium $= 350.5 - 66 - 60 = $ **224.5 bp**.

Risk-neutral hazard from the default-related spread: $\lambda^Q = (0.035046 - 0.0060)/0.55 = $ **5.28%**. Ratio to the real-world PD: $5.28/1.20 = $ **4.40**.

Trading cost: modified duration at 7.605% is 4.153 years. One point of price is $1/(96.50 \times 4.153) = 0.002495$, or about **24.9 bp** of spread. Spread over a two-year hold, about **12.5 bp a year**.

**Check.** The three components sum to the spread: $66 + 60 + 224.5 = 350.5$ bp. ✓

**Decision consequence.** Of 350 bp, only 66 bp pays for expected defaults. The bond is a good hold-to-maturity investment if you are willing to bear 224 bp worth of recession-concentrated default risk, which is the same risk your hotel portfolio already carries. For a family office that owns hotels, adding BB credit adds correlated exposure, not diversification. The 60 bp liquidity component is income to a holder who will not be forced to sell. Count it only if your own funding cannot be withdrawn in a downturn.

Reproduce: `tests/test_ch17_examples.py::test_example_17_2`

### Example 17.3 — The Chapter 11 waterfall and the moving fulcrum

**Given.** Cobalt Lodging Corp. files for Chapter 11. All claims are at a single legal entity. Gross distributable value is estimated at \$620 million in one valuation and \$470 million in another. Claims (\$ millions):

| Priority | Class | Claim |
|---|---|---|
| 1 | Administrative and priority claims | 20 |
| 2 | First-lien term loan (lien on all assets) | 350 |
| 3 | Second-lien notes (lien on all assets, junior) | 150 |
| 4 | Senior unsecured notes | 200 |
| 4 | Trade and other general unsecured claims (pari passu with notes) | 40 |
| 5 | Subordinated notes | 80 |
| 6 | Equity | — |

**Find.** Recoveries by class and the fulcrum security at each valuation.

**Solution.**

*Valuation \$620 million.* Admin \$20m paid. Remaining \$600m. First lien \$350m paid in full, remaining \$250m. Second lien \$150m paid in full, remaining \$100m. Unsecured pool $200 + 40 = \$240$m; recovery $100/240 = $ **41.67%**: notes receive \$83.33m, trade \$16.67m. Subordinated notes and equity receive zero. **Fulcrum: the senior unsecured class.**

*Valuation \$470 million.* Admin \$20m, remaining \$450m. First lien \$350m, remaining \$100m. Second lien recovers $100/150 = $ **66.67%**. Unsecured, subordinated and equity receive zero. **Fulcrum: the second lien.**

Because both liens cover all assets, there is no unencumbered value at \$470m. The second lien's \$50m deficiency claim under §506(a) ranks with the unsecured class, but that class has nothing to share. In practice unencumbered assets (cash outside the collateral package, some intellectual property, commercial tort claims) are often found, and the fight over them can give unsecured creditors a recovery here.

| Class | Recovery at \$620m | Recovery at \$470m |
|---|---|---|
| Admin | 100% | 100% |
| First lien | 100% | 100% |
| Second lien | 100% | 66.67% |
| Senior unsecured / trade | 41.67% | 0% |
| Subordinated | 0% | 0% |

**Check.** Payments sum to distributable value: $20 + 350 + 150 + 83.33 + 16.67 = 620$; $20 + 350 + 100 = 470$. ✓

**Decision consequence.** A \$150 million difference in valuation, 24% of the higher figure, decides who owns the company. Second-lien holders argue for a low valuation, because at \$470m they receive the equity and keep any upside above it. Unsecured holders argue for a high one. Valuation testimony in a contested Chapter 11 is advocacy, and the plan valuation is a negotiated number. Before buying any class, compute the valuation at which it becomes the fulcrum and ask who controls the process that sets that number.

Reproduce: `tests/test_ch17_examples.py::test_example_17_3`

### Example 17.4 — Structural subordination at Harborline

**Given.** The Harborline structure of §17.1. Opco enterprise value at emergence \$400m, \$500m or \$600m. No other Holdco assets. Ignore administrative claims for clarity.

**Find.** Recovery on the Holdco notes in each case. Then recompute assuming Opco had given a full upstream guarantee of the Holdco notes.

**Solution.**

Opco claims: secured \$250m; unsecured \$100m notes plus \$30m trade = \$130m. Total \$380m. Every Opco scenario covers \$380m, so Opco creditors recover 100% in all three cases.

Holdco value $= V_{opco} - 380$:

| Opco EV | Value reaching Holdco | Holdco note recovery | To old Holdco equity |
|---|---|---|---|
| \$400m | \$20m | 20/200 = **10.0%** | 0 |
| \$500m | \$120m | 120/200 = **60.0%** | 0 |
| \$600m | \$220m | **100%** | \$20m |

*With an upstream guarantee*, the Holdco notes join Opco's unsecured class: $100 + 30 + 200 = \$330$m sharing $V_{opco} - 250$:

| Opco EV | Unsecured recovery (all three claims) | Holdco notes receive | Opco notes receive |
|---|---|---|---|
| \$400m | 150/330 = **45.45%** | \$90.9m | \$45.5m |
| \$500m | 250/330 = **75.76%** | \$151.5m | \$75.8m |
| \$600m | **100%** | \$200m | \$100m |

**Check.** At \$500m with the guarantee: $75.76 + 22.73 + 151.52 = 250.0$ = value after secured debt. ✓

**Decision consequence.** In the base case the guarantee is worth $151.5 - 120 = \$31.5$ million to the Holdco notes, 15.8 points of face, and it costs the Opco noteholders 24.2 points. The value of the Holdco notes therefore depends on a legal fact you can read in the indenture. It also depends on the risk that the guarantee is attacked as a fraudulent transfer, which turns on whether Opco received reasonably equivalent value for giving it. Note the asymmetry between the two Harborline layers: Opco claims are covered in every scenario, while Holdco recoveries run from 10 to 100. All the uncertainty in Opco's value is concentrated in the Holdco notes. They behave like levered equity in Opco.

Reproduce: `tests/test_ch17_examples.py::test_example_17_4`

### Example 17.5 — Buying the Holdco notes at 38

**Given.** Opportunity A: Holdco notes at 38. Probabilities of the Opco value scenarios: \$400m 0.30, \$500m 0.50, \$600m 0.20. Recoveries from Example 17.4 (no guarantee): 10, 60 and 100 per 100 of face, received at emergence in 1.5 years. Post-petition interest is disallowed on unsecured claims, so the claim is principal plus pre-petition accrued interest, which we ignore for simplicity. Ignore trading costs.

**Find.** Expected recovery, the expected multiple and the IRR on expected recovery; scenario IRRs; the break-even probability of the \$400m scenario holding the other two at a 5:2 ratio; and the maximum price for a 20% annual return on expected recovery.

**Solution.**

$E[\text{recovery}] = 0.30(10) + 0.50(60) + 0.20(100) = 3 + 30 + 20 = $ **53.0**.
Multiple $= 53.0/38 = $ **1.395x**. IRR on expected recovery $= 1.3947^{1/1.5} - 1 = $ **24.83%**.

Scenario IRRs: $(10/38)^{1/1.5} - 1 = $ **−58.93%**; $(60/38)^{1/1.5} - 1 = $ **35.60%**; $(100/38)^{1/1.5} - 1 = $ **90.61%**.

Break-even: with the \$500m and \$600m scenarios at 5:2, the conditional recovery if not bad is $\bar G = (5 \times 60 + 2 \times 100)/7 = 71.43$. Set $(1 - q)71.43 + q \cdot 10 = 38$: $q^* = (71.43 - 38)/(71.43 - 10) = $ **54.4%**.

Maximum price for 20%: $53.0/1.20^{1.5} = 53.0/1.31453 = $ **40.32**.

**Check.** At 40.32, $(53.0/40.32)^{1/1.5} = 1.20$. ✓

**Decision consequence.** The trade clears a 20% hurdle on expected recovery at 38, and the bad scenario would need a probability above 54% to make it lose money in expectation. That looks robust. Three things make it less so. First, the IRR of the expected recovery is not the expected IRR (Chapter 1). With a 30% chance of losing 74% of the investment, size matters more than the point estimate. Second, all three scenarios assume Opco value cannot leak away before emergence. A secured financing at Opco that primes the existing structure, or a transfer of hotels to an unrestricted subsidiary, reduces what reaches Holdco dollar for dollar (Problem 17.8). Third, the 18-month timeline is a guess. Each extra six months at the base case reduces the IRR substantially. The position is a bet on Opco's value and on the indenture, not on Holdco's credit.

Reproduce: `tests/test_ch17_examples.py::test_example_17_5`

### Example 17.6 — CDS upfront, running spread and the hedge that is not

**Given.** Opportunity C: five-year CDS on Harborline Hotel Operating LLC (Opco) quoted at a par spread of 650 bp. Standard running coupon 500 bp, paid quarterly. Assumed recovery 40%. Riskless rate 4.0% continuously compounded. Notional \$10 million. Use the credit-triangle hazard to build the risky annuity.

**Find.** (a) The hazard, RPV01 and upfront payment. (b) The mark-to-market if the quoted spread widens to 900 bp immediately. (c) The difference between the triangle approximation and an exact flat-hazard model. (d) Whether buying Opco protection hedges the Holdco notes.

**Solution.**

(a) $\lambda = 0.065/0.60 = $ **10.833%**.
$RPV01 = \sum_{i=1}^{20} 0.25\, e^{-(0.04 + 0.10833)\, i/4} = $ **3.4654** years.
Upfront $= (0.065 - 0.050) \times 3.4654 = 0.05198$, or **5.20 points**, \$519,806 paid by the protection buyer at inception.
Running premium $= 0.05 \times 10{,}000{,}000 = \$500{,}000$ a year, \$125,000 a quarter, until maturity or a credit event.

(b) At 900 bp: $\lambda = 0.09/0.60 = 15.0\%$; $RPV01 = 3.1516$; upfront $= 0.04 \times 3.1516 = 0.12607$, or **12.61 points** (\$1,260,651).
Mark-to-market gain to the protection buyer $= 12.607 - 5.198 = $ **7.41 points**, \$740,845.
The linear approximation $(0.090 - 0.065) \times 3.4654 = 8.66$ points overstates the gain, because the risky annuity shortens as the hazard rises.

(c) With $\lambda = 10.833\%$, the exact flat-hazard protection leg is $0.60 \times \frac{0.10833}{0.14833}(1 - e^{-0.14833 \times 5}) = 0.22948$. The par spread for quarterly premiums without accrued-on-default is $0.22948/3.4654 = $ **662.2 bp**, not 650, and the upfront at a 500 bp coupon is **5.62 points**. The 12 bp difference is the premium lost when default falls between payment dates. Dealer screens use the ISDA standard model, which includes accrued premium. Use the triangle for intuition and the standard model for settlement.

(d) If Opco's value is \$400–600 million, Opco's creditors are paid in full in every scenario of Example 17.4. In a joint Chapter 11 filing, Opco's bankruptcy is a credit event, but the auction will value Opco's deliverable obligations near par, so the protection pays little. Meanwhile the Holdco notes can lose 90% of face. Buying Opco protection against Holdco notes is a short position on the part of the structure that is safe and leaves the long position on the part that is not. It costs 5.2 points upfront plus 500 bp a year.

**Check.** $RPV01$ is bounded by the riskless annuity: $\sum 0.25\,e^{-0.04\,i/4} = 4.5091$ exceeds 3.4654, and the 5-year term exceeds both. ✓

**Decision consequence.** A CDS hedges the reference entity and its deliverable obligations, nothing else. The relevant hedges for Holdco notes are a short position in an instrument that loses when Opco's *equity* value falls: a short in Holdco stock if it trades, or protection on Holdco itself. Near default the upfront on Holdco protection converges toward par minus the price of the cheapest deliverable bond, roughly $100 - 38 = 62$ points here, so buying it is not a hedge but an offsetting position that cancels the trade. If no cheap hedge exists, the right control is position size.

Reproduce: `tests/test_ch17_examples.py::test_example_17_6`

### Example 17.7 — CMBS tranches under an office-loss scenario

**Given.** Opportunity B. A \$1,000 million conduit pool. The capital structure (attachment–detachment as a share of the original pool):

| Class | Indicative rating | Attach–detach | Size |
|---|---|---|---|
| A | AAA | 30.0–100% | \$700m |
| AS | AAA | 22.0–30.0% | \$80m |
| B | AA− | 16.0–22.0% | \$60m |
| C | A− | 11.0–16.0% | \$50m |
| D | BBB− | 6.5–11.0% | \$45m |
| E | BB | 4.0–6.5% | \$25m |
| F (B-piece) | NR | 0–4.0% | \$40m |

Scenario 1 (office stress): 25% of the pool by balance defaults with average severity 45%. Scenario 2 (moderate): 15% defaults with severity 40%. Losses are realized before any principal paydown.

**Find.** Pool loss and tranche losses in each scenario; the default rate at which Class D is first impaired and wiped out (severity 45%); and Class A and Class D credit enhancement after \$200 million of loans pay off at par before any loss.

**Solution.**

Scenario 1: $L = 0.25 \times 0.45 = $ **11.25%**, \$112.5m.

| Class | Loss | Fraction lost |
|---|---|---|
| F | \$40.0m | 100% |
| E | \$25.0m | 100% |
| D | \$45.0m | **100%** |
| C | \$2.5m | 5.0% |
| B, AS, A | 0 | 0% |

Scenario 2: $L = 0.15 \times 0.40 = $ **6.0%**, \$60m. F loses \$40m (100%); E loses $\$20$m (**80%**); D and above lose nothing.

Class D thresholds at 45% severity: impaired above $DR = 0.065/0.45 = $ **14.44%**; wiped out at $DR = 0.11/0.45 = $ **24.44%**.

After \$200m of payoffs paid sequentially to Class A, the pool is \$800m. Class A's CE $= 300/800 = $ **37.5%** (from 30%). Class D's CE $= 65/800 = $ **8.125%** (from 6.5%).

**Check.** Scenario 1 losses sum to $40 + 25 + 45 + 2.5 = 112.5$. ✓ The same allocation follows from `x_capital_structure.tranche_losses` (Chapter 10's capital-stack function) applied to the pool, as the test confirms.

**Decision consequence.** Class D is a thin tranche: 4.5% of the pool separates its first dollar of loss from its last. A move in the default rate from 14% to 24% at a 45% severity takes it from par to zero. The rating describes the probability of the first dollar of loss, not the loss given that event, so a thin BBB− tranche is closer to a binary bet than its rating suggests. Two features of the real deal make it riskier than this arithmetic. (1) Paydowns are adversely selected: the loans that refinance and pay off are the good ones, so the CE gain from paydown arrives together with a worse remaining pool. (2) Before any principal loss, appraisal reductions in special servicing (Chapter 12, Example 12.5) reduce the servicer's interest advances, and the shortfall hits the most junior outstanding classes first. At a price of 72 the D bond is a view on office severities and on the timing of resolutions. Problem 17.9 prices it.

Reproduce: `tests/test_ch17_examples.py::test_example_17_7`

### Example 17.8 — Merton: CRE equity as a call on the building

**Given.** An office building worth \$100 million. Its debt is modeled as a zero-coupon claim with face \$80 million due in three years (a balloon including accrued interest). Riskless rate 4.0% continuously compounded. Property value volatility 15% [HYPOTHESIS; unsmoothed volatility, not appraisal volatility]. No payout ($q = 0$; NOI is assumed to cover interest and capital, so the balloon is the only claim).

**Find.** (a) Equity value, debt value, debt yield and spread, risk-neutral PD and the value of the borrower's put. (b) The same after value falls to \$80 million and volatility rises to 20%. (c) The value transferred from lender to equity by the volatility increase alone at $V = \$80$m.

**Solution.**

(a) $d_1 = \frac{\ln(100/80) + (0.04 + 0.01125)\times 3}{0.15\sqrt 3} = \frac{0.223144 + 0.15375}{0.259808} = 1.4507$; $d_2 = 1.4507 - 0.2598 = 1.1909$.
$E = 100\,N(1.4507) - 80e^{-0.12}N(1.1909) = $ **\$29.99m**.
$D = 100 - 29.99 = $ **\$70.01m**.
Riskless PV of the face $= 80e^{-0.12} = \$70.95$m. The borrower's put is worth $70.95 - 70.01 = $ **\$0.95m**.
Debt yield $= \ln(80/70.006)/3 = $ **4.448%**; spread **44.8 bp**.
Risk-neutral PD $= N(-1.1909) = $ **11.69%**.

(b) $V = 80$, $\sigma = 20\%$: $d_1 = 0.5196$, $d_2 = 0.1732$.
$E = $ **\$15.51m**; $D = $ **\$64.49m**; yield **7.185%**; spread **318.5 bp**; risk-neutral PD **43.1%**.

(c) At $V = 80$ and $\sigma = 15\%$: $E = \$13.14$m and $D = \$66.86$m. Raising volatility to 20% moves $15.51 - 13.14 = $ **\$2.38m** from the lender to the equity.

**Check.** Put–call parity: $E - [V - Fe^{-rT}] = 29.99 - 29.05 = 0.95$, the put in (a). ✓

**Decision consequence.** At \$80m the building's value equals the debt's face, and an appraisal-based balance sheet shows zero equity. The option model values that equity at \$15.5 million, 19% of the building, because three years of volatility remain. That is why sponsors with "underwater" equity refuse to hand over the keys and pay for extensions (Chapter 10, Example 10.8). It is also why a lender should worry when an underwater sponsor proposes a riskier business plan, such as a speculative repositioning: volatility is worth \$2.4 million to the sponsor and costs the lender the same amount. Covenants and cash management exist to limit this transfer.

Reproduce: `tests/test_ch17_examples.py::test_example_17_8`

---

## 17.6 CRE application: reading CRE debt as credit

The tools of this chapter apply to CRE debt with three adjustments.

**Single-asset borrowers make structural subordination concrete.** In a typical mortgage-plus-mezzanine financing, the mortgage borrower is a special-purpose entity that owns the property. The mezzanine borrower owns the mortgage borrower's equity and pledges it to the mezzanine lender. The mezzanine lender's remedy is a UCC foreclosure on the pledged equity, which can be completed in weeks, rather than a mortgage foreclosure. Its claim is structurally subordinated: it receives nothing until the mortgage is paid, and it must cure mortgage defaults to protect its position. Holdco notes at Harborline and a mezzanine loan on a hotel are the same instrument in different clothes. The intercreditor agreement plays the role of the indenture's guarantee and covenant package (Chapter 10, Example 10.4).

**OpCo/PropCo splits move value between creditors.** Hotel companies are often split into a property company that owns the real estate and an operating company that runs it under a lease or management agreement. In a restructuring the rent or management fee between them is a transfer between two sets of creditors. An analyst who owns OpCo debt should model what happens to OpCo if PropCo's creditors terminate or reprice the lease, and vice versa.

**REIT unsecured bonds.** A REIT's unsecured bondholders rank behind its property-level mortgages on the encumbered assets. Their protection is the pool of unencumbered properties and indenture covenants on total leverage, secured leverage and unencumbered asset coverage. Rising secured debt at a REIT is the corporate equivalent of priming.

**CMBS is where corporate credit and CRE meet.** The B-piece buyer in a conduit (Chapter 12) is the first-loss investor and usually appoints the special servicer. Its incentives over appraisal timing and modification versus liquidation affect every class above it. The investment-grade classes are protected by subordination, but their risk depends on correlation across loans: a pool with 25% office exposure behaves like a smaller number of large bets on one property type. A CMBS investor should run the pool through property-level stress (Chapter 9 cap-rate and NOI shocks) and allocate the loss through the stack, rather than relying on the rating.

**The Merton model is a sanity check on sponsor behavior.** Example 17.8 explains why an underwater sponsor asks for time, takes risk and resists a deed-in-lieu. It is less useful for pricing CMBS bonds, because the inputs (property volatility, payout, the true default trigger) are uncertain and the trigger is a refinancing test, not a value crossing.

---

## 17.7 When the relationships fail

* **Recovery is not independent of default.** The triangle and the expected-loss formula treat $R$ as a constant. Recoveries fall when defaults cluster (§17.2). Using a long-run average recovery with a recession default rate understates loss.
* **The triangle breaks for distressed names.** When default is likely and soon, the bond trades on recovery, the term structure of hazard is steep and downward-sloping, and a single flat hazard says little. Price distressed debt from a recovery waterfall and a timeline, not from a spread.
* **Absolute priority is a baseline.** Negotiated plans give junior classes value to secure votes or avoid litigation. Debtors in possession and their sponsors sometimes use liability-management transactions outside court, such as transfers of collateral to unrestricted subsidiaries or exchanges that give some lenders new super-priority debt and leave others behind [INFERENCE: these structures are widely discussed in restructuring practice; individual cases are not cited here]. These transactions reorder priority without a bankruptcy. The indenture's covenant package and "sacred rights" provisions decide whether they are permitted.
* **Timing changes everything in distressed returns.** A recovery estimate without a timeline is not a return estimate. Contested valuations, appeals and regulatory approvals (franchise consents for hotels) extend the timeline, and unsecured claims do not accrue interest while they wait.
* **CDS and bonds diverge.** The **basis** (CDS spread minus bond spread) moves with funding costs, the cheapest-to-deliver option and dealer balance sheets. CDS pay on legal events of a specific entity. A distressed exchange may not be a credit event. A restructuring credit event may not be covered by North American contracts.
* **Tranche ratings depend on correlation.** The probability that a senior tranche loses depends on how loan losses co-move. Stanton and Wallace argue that falling subordination, not deteriorating loans, explains most of the 2007–09 CMBS collapse (§17.8). A rating model calibrated in a period of low correlation will understate senior risk.
* **Merton assumes things CRE does not have.** Continuous trading in the asset, a known volatility, a single zero-coupon debt claim and default only at maturity. Real loans pay coupons, have covenants and extension options, and default when they cannot be refinanced. Appraisal-based volatility is smoothed and understates true volatility (Chapter 2). Treat Merton outputs as directional.
* **Liquidity premia are not free income.** A spread component that compensates for illiquidity is earned only by a holder whose funding is stable. Leveraged or redeemable holders are short the liquidity they think they are being paid for.

---

## 17.8 Historical episode: the 2007–09 CMBS repricing

**Date and environment.** U.S. CMBS issuance grew rapidly from the late 1990s to 2007. Stanton and Wallace report average annual growth of about 18% from 1997 to 2007 [FACT; Stanton and Wallace (2010), NBER WP 16206; VERIFIED-SECONDARY, ch17-S10]. Issuance was about \$229 billion in 2007 [FACT; Chandan (2012), *Wharton Real Estate Review*; VERIFIED-SECONDARY, ch17-S11]. Conduit lending at the peak featured interest-only loans and pro forma underwriting [INFERENCE: widely reported in industry commentary; the share of IO loans by vintage is *(verification pending)*].

**What was knowable then.** Deal-level subordination levels were published in every offering document. Stanton and Wallace show that subordination fell for all classes of CMBS between 1996 and 2007, with a slight rise in 2008 [FACT; ch17-S10]. A later version of their work argues that a 2002 loosening of capital requirements for highly rated CMBS narrowed the spread between AA/AAA CMBS and corporate bonds of the same rating [FACT that they make this argument; VERIFIED-SECONDARY, ch17-S10]. A careful investor in 2006 could therefore see that the AAA classes had less protection than earlier vintages had, while spreads paid less for it. What was not knowable in advance was the severity of the 2008–09 collapse in CRE transaction volume and refinancing capacity.

**What happened.** Issuance fell to about \$12 billion in 2008 and \$3 billion in 2009 [FACT; Chandan (2012); VERIFIED-SECONDARY, ch17-S11]. A fund report filed with the SEC described October and November 2008 as particularly poor months for CMBS, with spreads versus Treasuries reaching all-time highs [FACT; T. Rowe Price Short-Term Bond Fund semiannual report, FY2008; VERIFIED-SECONDARY, ch17-S12]. The peak level of AAA CMBS spreads is *(verification pending)*: an investor presentation filed with the SEC shows AAA CMBS figures for late November 2008, but the benchmark and series are not clear from the excerpt. High-yield corporate spreads also widened to roughly 2,000 bp in late 2008 *(verification pending: single secondary source; check FRED series BAMLH0A0HYM2 or ICE)*.

The Federal Reserve authorized the Term Asset-Backed Securities Loan Facility (TALF) on 24 November 2008. On 19 May 2009 it announced that high-quality CMBS issued before 1 January 2009 ("legacy" CMBS) would become eligible TALF collateral starting in July 2009 [FACT; Federal Reserve press release of 19 May 2009; VERIFIED-SECONDARY, ch17-S13]. Eligibility required AAA ratings from at least two approved agencies [FACT; law-firm summaries; VERIFIED-SECONDARY, ch17-S13]. Trepp reported in August 2009 that AAA CMBS spreads had narrowed by 100 to 150 bp over two months, partly because investors could finance purchases through TALF [FACT; VERIFIED-SECONDARY, ch17-S12].

The repricing preceded the loan losses. The Trepp CMBS delinquency rate peaked in July 2012 at about 10.3%. Contemporary reports gave 10.36%; later Trepp-sourced reports cite 10.34% [FACT; VERIFIED-SECONDARY, ch17-S14]. Moody's reported in 2012 that loss severities on liquidated loans were 49.4% for the 2007 vintage and 54.4% for 2008 [FACT; VERIFIED-SECONDARY, ch17-S15]. KBRA's conduit loss study, updated through Q1 2025, reports a cumulative loss rate of 4.4% across all conduit loans since 1995. The 2008 vintage has the highest default rate (32.7%) and the highest cumulative loss rate (16.3%) [FACT; VERIFIED-SECONDARY, ch17-S16].

**Participants and incentives.** Conduit originators earned gains on sale and did not retain credit risk. Rating agencies were paid by issuers. B-piece buyers took first loss and appointed special servicers. AAA buyers, including banks and insurers, held bonds whose capital treatment depended on ratings. When the repricing came, holders who financed AAA CMBS with short-term borrowing were forced sellers, and buyers with unlevered capital or access to TALF were the liquidity providers.

**Interpretations.** (1) Stanton and Wallace: the collapse was caused mainly by subordination falling to levels that did not protect "safe" tranches, while the underlying loans did not change much in observable quality [FACT that this is their argument; ch17-S10]. (2) A market-liquidity view: the AAA price collapse in late 2008 reflected forced selling and the disappearance of financing more than expected credit losses. The tightening once TALF financing was available supports this for the senior classes [INFERENCE]. (3) A fundamental view: the 2006–08 vintages had weak underwriting, and later losses and severities confirmed it [INFERENCE from the vintage loss data above]. These views apply to different parts of the stack. Junior classes of 2006–08 deals did take heavy losses. The senior AAA classes of most deals were, on the evidence of later loss rates, mispriced by liquidity more than by credit [INFERENCE; a class-by-class loss tabulation is *(verification pending)*].

**Strategies available then.** Buying seasoned AAA CMBS in late 2008 required balance sheet that would not be forced to sell, plus a model of pool losses under severe stress. TALF in 2009 offered non-recourse term financing, which was itself a put written by the Fed on the collateral [INFERENCE]. Buying junior classes was a bet on loan-level outcomes that took years to resolve.

**What the episode does and does not establish.** It shows that structured-credit prices can fall far below any reasonable estimate of expected loss when funding disappears, and that subordination is a design choice that can erode in a boom. It shows that public policy (TALF) can change the price of liquidity quickly. It does **not** show that AAA CMBS are always safe; the outcome depended on subordination levels, the timing of the policy response and the recovery in CRE values. It does not show that buying at the bottom was easy: the peak in delinquencies came almost four years after the trough in prices.

**CRE connection.** The CMBS market is the bridge between property cash flows and bond prices. When it closes, conduit refinancing disappears and the maturity wall of Chapter 12 becomes a solvency event for borrowers who were merely illiquid.

---

## 17.9 Decision exercise: Harborline and the D bond

You have \$60 million. Return to the three opportunities of §17.1 and use Examples 17.4–17.7. Complete the decision on `desk/investment_memos/decision_record_template.md`. Your record must state:

1. Which Harborline class is the fulcrum in each of the three Opco value scenarios, and what that implies for control of the reorganized company.
2. Whether you buy the Holdco notes at 38, how much, and what you need to read first (indenture guarantee provisions, unrestricted-subsidiary capacity, permitted secured debt baskets).
3. Why Opco CDS is not a hedge of the Holdco notes, and what, if anything, you would use instead.
4. A price for the CMBS Class D bond from your own office-loss scenarios (Problem 17.9 gives one route), and the loan-level information you would need.
5. What you will not do. Abstention is a legitimate answer for any of the three.
6. Invalidation criteria: the facts that would make you sell.

**Rubric.**

| Criterion | Full credit | Partial | None |
|---|---|---|---|
| Fulcrum identification | Opco EV \$400–600m covers Opco claims; Holdco notes are the fulcrum at \$400m and \$500m and will own Holdco's equity in Opco; at \$600m no class is impaired | Correct recoveries without the control implication | Treats Holdco notes as senior because they are "senior notes" |
| Holdco notes decision | Sized to survive the 10-point outcome; conditional on reading the indenture; recognizes leakage risk | Uses expected IRR only | Buys full size on 24.8% IRR |
| CDS | Rejects Opco protection as a hedge with the Example 17.6 reasoning | Notes basis risk without the entity point | Treats CDS as a hedge |
| CMBS | Prices from scenarios, discusses thin tranche, adverse selection of paydowns, interest shortfalls | Uses a single loss scenario | Relies on the rating |
| Abstention and invalidation | States conditions under which each trade is not done | Generic | Absent |

There is no single correct allocation. A defensible answer can buy a reduced Holdco position, pass on the CDS, and bid well below 72 for the D bond or pass.

---

## 17.10 Frequent analytical errors

1. **Treating the risk-neutral hazard as a default forecast.** $s/(1-R)$ contains risk and liquidity premia. It is typically several times the real-world rate.
2. **Treating the hazard as an annual probability, or dividing cumulative PD by years.** Small errors for strong credits, material errors for weak ones.
3. **Reading "senior" in a bond's name as seniority in the structure.** Senior notes at a holding company rank behind every creditor of every subsidiary.
4. **Ignoring trade claims.** They are general unsecured claims and dilute bond recoveries pro rata.
5. **Forgetting that interest stops.** Unsecured claims do not accrue post-petition interest in an insolvent estate. A longer case lowers returns directly.
6. **Using average historical recoveries in a recession scenario.** Recoveries fall when defaults rise.
7. **Hedging a bond with CDS on a different entity.** CDS pays on its reference entity only.
8. **Using a linear RPV01 approximation for large spread moves.** The risky annuity shrinks as spreads widen.
9. **Reading a tranche rating as a loss estimate.** A rating describes the probability of first loss, not the loss given it. Thin tranches are nearly binary.
10. **Counting paydown as free credit enhancement.** Good loans refinance first, so the remaining pool gets worse while CE rises.
11. **Valuing CRE equity at book when the loan is underwater.** Equity has time value until maturity, and the sponsor's behavior follows the option value, not the book value.

---

## 17.11 Connections to other chapters

* Chapter 1: break-even probability, expected IRR versus IRR of expected flows, and liquidity provision, all applied to distressed purchases (Example 17.5).
* Chapter 2: appraisal smoothing, which biases the volatility input to the Merton model.
* Chapter 6: Treasury yields, duration and the riskless benchmark for spreads.
* Chapter 10: the capital stack, the borrower's default option and the bargaining zone; Example 17.7 applies its loss-allocation arithmetic to a loan pool, and Example 17.8 prices its option view.
* Chapter 12: special servicing, appraisal reductions and the B-piece's control; distressed loan pricing on a single asset.
* Chapter 18: option pricing and Greeks in full; interest-rate caps.
* Chapter 23: 2008 in full, including the interaction of CMBS, bank balance sheets and policy.
* Case G (`cases/hypothetical/case_G_buying_the_debt/`): buying a defaulted CRE loan, the single-asset version of Examples 17.3–17.5.
* Case J (`cases/hypothetical/case_J_credit_crunch_hotel/`): a hotel acquisition when credit markets close.

---

## 17.12 One-page reference sheet

**Questions before any credit trade.** What is the reference entity? Where in the structure does my claim sit, entity by entity? At what enterprise value is my class the fulcrum? How long until resolution, and does my claim accrue interest meanwhile? What is the spread paying for: default, liquidity or risk?

| Quantity | Formula |
|---|---|
| Survival, cumulative PD | $S(t) = e^{-\lambda t}$; $PD(t) = 1 - e^{-\lambda t}$ |
| Hazard from cumulative PD | $\lambda = -\ln(1 - PD(t))/t$ |
| One-year PD | $1 - e^{-\lambda}$ |
| Forward hazard | $[\ln S(t_1) - \ln S(t_2)]/(t_2 - t_1)$ |
| Conditional PD | $[PD(t_2) - PD(t_1)]/[1 - PD(t_1)]$ |
| Credit triangle | $s \approx \lambda(1 - R)$; $\lambda^Q = s/(1 - R)$ |
| Spread decomposition | $s = PD^P(1-R) + \ell + \pi$ |
| APR payment | $P_j = \min(C_j, \max(V - \sum_{k<j}C_k, 0))$ |
| Holdco value | $\max(V_{opco} - \sum C_{opco}, 0) + $ other holdco assets |
| Risky annuity | $RPV01 = \sum \tfrac14 e^{-(r+\lambda)t_i}$ |
| CDS upfront | $U = (s - c)\cdot RPV01$ (paid by protection buyer if $s > c$) |
| Tranche loss | $\min(\max(L - a, 0), d - a)/(d - a)$; $L = DR \times \delta$ |
| First-loss default rate | $DR^* = a/\delta$ |
| Credit enhancement | junior balance / current pool balance |
| Merton equity | $E = VN(d_1) - Fe^{-rT}N(d_2)$; $D = V - E$; PD$^Q = N(-d_2)$ |
| Spread per point of price | $1/(P \cdot D_{mod})$ |

**Recovery ordering (Moody's, 1987–2008, VERIFIED-SECONDARY):** loans ≈ 81%, senior secured bonds ≈ 64%, senior unsecured ≈ 49%, subordinated ≈ 29%. Lower in high-default years.

**Rules of thumb (to be tested, not trusted).** Distressed bonds trade on recovery and time, not yield. A thin tranche behaves like a binary option. Holdco debt is levered equity in opco.

---

## References for this chapter

All sources are recorded in `references/sources_ch17.md` with verification status.

* Merton, R. C. (1974). "On the Pricing of Corporate Debt: The Risk Structure of Interest Rates." *Journal of Finance*, 29(2), 449–470.
* Elton, E. J., Gruber, M. J., Agrawal, D., and Mann, C. (2001). "Explaining the Rate Spread on Corporate Bonds." *Journal of Finance*, 56(1), 247–277.
* Longstaff, F. A., Mithal, S., and Neis, E. (2005). "Corporate Yield Spreads: Default Risk or Liquidity? New Evidence from the Credit Default Swap Market." *Journal of Finance*, 60(5), 2213–2253.
* Stanton, R., and Wallace, N. (2010). "CMBS Subordination, Ratings Inflation, and the Crisis of 2007–2009." NBER Working Paper 16206. Later version: *Financial Management* 47(1), 175–201 (2018).
* Chandan, S. (2012). Article on CMBS, *Wharton Real Estate Review*, Spring 2012.
* Bank for International Settlements (2010). "The 'Big Bang' in the CDS market." *BIS Quarterly Review*, December 2010.
* Board of Governors of the Federal Reserve System (2009). Press release, 19 May 2009, on legacy CMBS in TALF.
* 11 U.S.C. §§ 502(b)(2), 506(a), 1129(b)(2)(B).
* Moody's Investors Service, default and recovery studies (as reported by CFO.com and Barings); Reserve Bank of Australia, *Financial Stability Review*, March 2010, Box A.
* Trepp, CMBS delinquency reports (as reported by Commercial Observer and others); KBRA, *Conduit CMBS Default and Loss Study* (2025 update).
