# Chapter 2 — The Price Formation Process

> **Status:** Complete (v1.0). Numerical examples are reproduced in `tests/test_ch02_examples.py` using `models/python/sdesk/x_microstructure.py`. Problems are in `problems/questions/ch02_problems.md` and solutions in `problems/solutions/ch02_solutions.md`. Sources are in `references/sources_ch02.md`; figures from secondary coverage of NCREIF and Nareit releases are marked VERIFIED-SECONDARY there, and one item (the exact wording of the Federal Reserve's May 2023 *Financial Stability Report*) is paraphrased only and flagged *(verification pending)*.

## Learning objectives

After this chapter you should be able to:

1. Explain where a price comes from: who must trade, who may trade, and how an auction or a dealer converts orders into a single number. Compute a call-auction clearing price from supply and demand schedules, and show how a market order moves it.
2. State the weak, semi-strong, and strong forms of market efficiency precisely. Explain the Grossman–Stiglitz paradox and the limits to arbitrage, and say what each implies for a speculator who believes a price is wrong.
3. Convert a data surprise into a price change: standardize the surprise against consensus, apply a sensitivity, and translate a yield move into bond and property values. Distinguish surprise relative to consensus from surprise relative to positioning.
4. Identify the **marginal** buyer and seller of a CRE asset from a reservation-price distribution. Show numerically how the loss of the most aggressive financed buyers lowers the clearing price with no change in NOI, and why a gap between buyer and seller reservation prices produces a frozen market instead of a lower price.
5. Estimate an effective bid–ask spread with Roll's estimator. Compute and annualize the round-trip cost of a liquid security and a private property.
6. Explain why appraisal-based CRE indices lag and smooth economic value. Apply the Geltner unsmoothing filter $r_t = (r^*_t - a\,r^*_{t-1})/(1-a)$, compute the implied mean lag and volatility understatement, and know when the filter misleads.
7. Recognize transaction selection bias and stale comparable sales. Restate a comp set to today's market and to the subject's quality, and quantify how far a naive comp average is from a defensible value.

---

## 2.1 Opening investment problem: three prices for the same apartments

You are the real estate principal of a family office. It is 15 months into a monetary-tightening cycle; the 10-year Treasury yield is about 200 bp above its level when the cycle started. All facts below are [HYPOTHESIS], a constructed teaching case. Section 2.9 gives the historical episode that the case resembles, with documented figures.

Three numbers reach your desk on the same morning.

**Price 1: the fund statement.** The office holds \$25 million of units in an open-end core real estate fund. The fund's quarterly statement shows net asset value (NAV) per unit down 3% over the last twelve months. The NAV is based on independent appraisals. The fund's apartment holdings are appraised at a 4.30% cap rate on in-place NOI after reserves. The statement mentions, in a footnote, that redemption requests equal 12% of NAV and will be paid "as liquidity permits".

**Price 2: the screen.** Listed apartment REITs are down 28% over the same twelve months. Your analyst estimates that their share prices imply a 5.60% cap rate on their portfolios, which are of similar quality and location to the fund's.

**Price 3: the broker.** A broker offers a 240-unit, 1998-vintage garden apartment community in a Sun Belt suburb. In-place NOI after reserves is \$3,000,000. The seller is a closed-end fund near the end of its life. The broker's guidance is \$60.0 million, a 5.00% cap rate, which matches the seller's most recent appraisal. To justify the price, the broker cites four "recent comps" at an average cap rate of 4.95%.

You have three possible actions, plus abstention. You can (a) request redemption from the open-end fund, (b) buy apartment REIT shares, or (c) bid on the garden community. The questions are: Which of these prices is "the price"? Why do they differ? Who is on the other side of each? What would you need to believe to act?

By the end of the chapter you will be able to answer all three questions with numbers. Section 2.10 returns to the decision.

---

## 2.2 Economic intuition: prices are made by the marginal trader

### Who sets a price

A price is not a property of an asset. It is the terms at which the last trade happened, or would happen, between two parties who each preferred trading to not trading. Most owners of an asset do not trade on a given day. Their valuations do not set the price. They only stand behind it as potential sellers if the price rises far enough.

The price is set at the **margin**: by the buyer who is just willing to pay it and the seller who is just willing to accept it. In a liquid market there are many marginal participants on both sides, and their reservation prices are close together. In private CRE there may be four serious bidders for a building. The price depends on the second-highest of their valuations, and on whether the seller's reservation price is below it.

This has an immediate consequence. **A price can fall without anyone's estimate of the asset's cash flows changing.** It falls if the most aggressive buyers leave the market, for example because their lenders stop lending. The remaining buyers are those with lower valuations, and one of them becomes marginal. Example 2.3 computes this for the opening problem's apartment community.

### Order flow: who must trade and who may trade

Every trade has two sides, but the two sides rarely have the same urgency. Chapter 1 separated liquidity *consumers*, who must trade now, from liquidity *providers*, who will trade if paid. Price formation is the process by which consumers' urgency is matched against providers' willingness, and by which informed traders' information is transmitted into the price.

Three kinds of order flow matter:

* **Informed flow** comes from traders who know or have estimated something about value that the price does not yet reflect. Their trades move the price toward value and are the mechanism of price discovery.
* **Liquidity-motivated flow** comes from traders who must buy or sell for reasons unrelated to value: redemptions, loan maturities, index rebalancing, fund wind-downs, tax deadlines, estate settlements. Their trades move prices *away* from value temporarily, and providers are paid to absorb them.
* **Noise or sentiment flow** comes from traders who believe they are informed but are not. Their trades can push prices away from value for long periods. Arbitrageurs who bet against them bear the risk that the mispricing grows before it shrinks (§2.4.3).

A professional must ask of every price: which kind of flow produced it? A REIT that falls 3% on a day when its index weight is cut is not the same signal as a REIT that falls 3% after its largest tenant files for bankruptcy.

### Auctions and dealers

Markets aggregate orders into prices through two basic mechanisms.

A **call auction** collects orders over a period, then executes all compatible orders at a single price at one moment. Stock exchanges use call auctions to open and close trading. Treasury securities are first sold in auctions. Foreclosure sales, many loan-sale processes, and broker-run "best and final" rounds for CRE are auctions too, although they clear a single indivisible asset rather than many units.

A **continuous market** executes each order as it arrives against the orders already resting in a limit-order book, or against a dealer's quote. Prices update with every trade. Immediacy is available at all times, at the cost of the bid–ask spread and of the price impact of large orders.

The difference matters for what a price *means*. A call-auction price aggregates all orders submitted in the window and is the single price that maximizes trade. A continuous-market price is the price at which the last order happened to execute; it can be noisier, but it updates instantly. Private CRE is the limiting case of an infrequent, negotiated auction with high participation costs. Price discovery there is slow because each "auction" requires months of work and only a few happen in a given submarket each quarter.

### Expectations and surprise

Prices are forward-looking. A price today equals what the marginal trader expects the asset to be worth, discounted. Information that everyone expected is therefore already in the price. Only the **surprise**, the difference between what happened and what was expected, moves prices.

This is why a strong employment report can coincide with falling yields (drill D003), and why a REIT can fall on "record earnings". The question is never "was the news good?" It is "was the news better or worse than the marginal trader expected, and by how much, relative to how noisy such news usually is?"

### Why appraisals lag

Private CRE is valued, for accounting and fund-reporting purposes, by appraisers. An appraiser estimates what a property would sell for, using comparable sales, income capitalization, and judgment. Three features of this process slow down appraised values:

1. **Evidence lag.** Appraisers rely on closed sales. A sale that closes today was priced when the contract was signed, often 60–120 days earlier, on terms negotiated before that.
2. **Rational partial adjustment.** Each comparable sale is a noisy signal of value. An appraiser who combines the new evidence with the prior appraisal, weighting each by its precision, produces an estimate that moves only partly toward each new signal. That is optimal for minimizing the error of a single appraisal, but it smooths the *time series* (Quan and Quigley, 1991; Geltner, 1993).
3. **Staggered and anchored reappraisals.** Not every property in an index is reappraised every quarter, and an appraiser updating last year's value tends to anchor to it.

The appraisal-based index is therefore a moving average of past market values. It turns too late, turns too gently, and looks less volatile than the market it measures. Section 2.4.5 derives the filter that undoes the smoothing.

### Selection: which assets trade

In a downturn the assets that trade are not a random sample. Owners of properties that have lost the most value often cannot sell: the price would not repay the loan, or a sale would crystallize a loss the owner prefers not to report. Lenders often extend rather than foreclose. The properties that do sell are disproportionately those whose owners are unlevered or forced for non-value reasons, and those of the highest quality, for which buyers still exist. A comp set drawn from these sales overstates the value of the typical asset. Transaction-based indices built from them understate the decline (Fisher, Gatzlaff, Geltner and Haurin, 2003, develop indices that correct for this variable liquidity).

---

## 2.3 Technical definitions

| Term | Definition |
|---|---|
| Reservation price | The highest price a buyer would pay (or the lowest a seller would accept) and still prefer the trade to no trade |
| Marginal buyer / seller | The participant whose reservation price determines the clearing price. In an ascending single-asset auction, the second-highest bidder's reservation price sets the price |
| Call auction | Orders are accumulated and executed together at one price that maximizes executable volume |
| Continuous market | Orders execute on arrival against resting orders or dealer quotes |
| Limit order / market order | An order with a price limit / an order to trade immediately at any available price |
| Clearing price | The price at which cumulative demand meets cumulative supply (with a tie-breaking rule when schedules are discrete) |
| Order imbalance | Demand minus supply at the clearing price; the unfilled interest |
| Price impact ($\lambda$) | The price change per unit of net order flow (Kyle, 1985) |
| Quoted spread | Ask minus bid. The **effective spread** is twice the distance between a trade price and the midpoint |
| Roll estimator | $S = 2\sqrt{-\text{Cov}(\Delta p_t, \Delta p_{t-1})}$; an effective spread inferred from negative autocorrelation of trade-price changes (Roll, 1984) |
| Round-trip cost | Proportional loss from buying and then selling at an unchanged midpoint, including spread, commissions, transfer taxes, and fees |
| Weak-form efficiency | Prices reflect all information in past prices and volumes (Fama, 1970) |
| Semi-strong-form efficiency | Prices reflect all publicly available information |
| Strong-form efficiency | Prices reflect all information, public and private |
| Grossman–Stiglitz paradox | If prices fully reflected costly information, no one would pay to acquire it, so prices could not reflect it. Equilibrium requires some inefficiency to pay for information (Grossman and Stiglitz, 1980) |
| Limits to arbitrage | Capital, funding, short-sale, and noise-trader-risk constraints that prevent informed traders from eliminating mispricing (Shleifer and Vishny, 1997) |
| Consensus | The median or mean of published forecasts of a data release |
| Standardized surprise | $z = (\text{actual} - \text{consensus})/\sigma_{\text{surprise}}$ |
| Appraisal smoothing | Appraised values that adjust only partly to each period's change in market value |
| Smoothing parameter $a$ | Weight on the prior appraisal return in $r^*_t = (1-a)r_t + a\,r^*_{t-1}$; $0 \le a < 1$ |
| Geltner unsmoothing | $r_t = (r^*_t - a\,r^*_{t-1})/(1-a)$: recovers market-value returns from appraisal returns |
| Transaction-based index | A price index built from sales (repeat-sales or hedonic) rather than appraisals |
| Selection bias | A sample statistic that differs from the population value because inclusion in the sample depends on the variable being measured |
| Stale comp | A comparable sale whose price reflects a market that no longer exists |

---

## 2.4 Equations and derivations

### 2.4.1 Clearing a call auction

Let buy limit orders be $(L^b_j, q^b_j)$ and sell limit orders $(L^s_k, q^s_k)$. Market orders $M^b$ and $M^s$ execute at any price. At a candidate price $p$:

$$D(p) = M^b + \sum_{j:\,L^b_j \ge p} q^b_j, \qquad S(p) = M^s + \sum_{k:\,L^s_k \le p} q^s_k.$$

$D$ is non-increasing and $S$ non-decreasing in $p$. Executable volume is $\min\{D(p), S(p)\}$. The clearing price maximizes it:

$$p^* = \arg\max_p \min\{D(p), S(p)\}.$$

With discrete schedules there can be ties. Exchanges break them by minimizing the imbalance $|D - S|$, then by reference to a prior price. Our library takes the mean of any remaining tied prices, which is a teaching simplification.

A market sell order of size $Q$ shifts $S(p)$ up by $Q$ at every price. The new clearing price is lower. The ratio of the price change to $Q$ is an empirical price-impact coefficient $\lambda = \Delta p^*/Q$. Kyle (1985) derived $\lambda$ as the market maker's rational response to the share of informed flow: the more informative order flow is, the more a given imbalance must move the price.

### 2.4.2 Efficiency, costly information, and Grossman–Stiglitz

The three forms of efficiency are statements about **information sets**, not about whether prices are "right":

* **Weak form.** No trading rule based on past prices earns abnormal risk-adjusted returns after costs.
* **Semi-strong form.** No rule based on public information does.
* **Strong form.** Not even private information does.

The forms are nested: strong implies semi-strong implies weak.

Grossman and Stiglitz (1980) showed that the strong and semi-strong forms cannot hold exactly when information is costly. The argument fits on one line. If the price already reflected everything an analyst could learn, the analyst would earn nothing on the information, would stop paying for it, and the price would stop reflecting it.

A minimal equilibrium makes this concrete. Let $\lambda$ be the fraction of capital that is informed. Suppose informed capital earns a gross excess return $\alpha(\lambda) = \alpha_0(1 - \lambda)$, which falls as more informed capital competes for the same mispricings. Information costs $c$ per dollar per year. Entry stops where

$$\alpha_0(1 - \lambda^*) = c \;\;\Rightarrow\;\; \lambda^* = 1 - \frac{c}{\alpha_0}.$$

With $\alpha_0 = 2.0\%$ and $c = 0.75\%$ (for example, \$1.5 million of research cost on \$200 million of capital), $\lambda^* = 1 - 0.75/2.0 = 0.625$. In equilibrium the informed earn exactly their costs. The uninformed do no worse than the informed *after costs*. The market is "efficient" in the sense that no one earns abnormal net returns, yet prices are not fully informative.

The CRE implication is direct. Private real estate information is very costly: rent rolls, property condition reports, local leasing intelligence, lender relationships. Grossman–Stiglitz therefore predicts that private CRE prices will be *less* informationally efficient than REIT prices, and that the gross returns to local information will be correspondingly *higher*. Neither implies that a given investor's information is worth what it costs.

### 2.4.3 Limits to arbitrage

Suppose an informed trader is right that a price is too low. Shleifer and Vishny (1997) identify why the trader may still not correct it:

1. **Noise-trader risk.** The mispricing can widen before it closes. A trader who must mark to market and may face redemptions can be forced out at the worst moment.
2. **Funding and margin.** Positions are financed. A lender raises haircuts when prices fall, exactly when the opportunity is best.
3. **Short-sale constraints.** If the mispriced asset is *overvalued*, the arbitrage requires a short. Private real estate cannot be shorted at all. A REIT can be shorted, but borrow costs, recall risk, and the absence of a convergence date limit the trade.
4. **No convergence mechanism.** A futures contract converges to spot at expiry. A REIT's discount to the appraised value of its properties has no expiry. It closes only through events: takeovers, asset sales, buybacks, or appraisal write-downs.
5. **Fundamental risk.** The "arbitrage" between a REIT and private properties is not between identical claims. The REIT has leverage, management, and a cost structure.

A price can therefore be wrong for longer than an arbitrageur can stay solvent. A divergence between listed and private CRE values (§2.9) is not by itself an arbitrage opportunity.

### 2.4.4 Surprise and the price response

Let $V_t$ be the price of an asset whose value depends on a variable $x$ to be released. Before the release, the price embeds the expected value $E_{t-1}[x]$. After the release,

$$\Delta P = \beta\,(x - E_{t-1}[x]) + \varepsilon,$$

where $\beta$ is the price sensitivity per unit of surprise and $\varepsilon$ is the effect of everything else that day. Because the dispersion of surprises differs across releases, it is standard to measure surprises in standard deviations (Balduzzi, Elton and Green, 2001; Andersen, Bollerslev, Diebold and Vega, 2003):

$$z = \frac{x - \text{consensus}}{\sigma_{\text{surprise}}}, \qquad \Delta y = b \cdot z.$$

Here $b$ is the yield response in basis points per one-standard-deviation surprise. It is estimated by regressing yield changes in a narrow window around past releases on past standardized surprises (Chapter 4 builds such a regression). For a bond, the price consequence is

$$\frac{\Delta P}{P} \approx -D_{mod}\,\Delta y + \tfrac{1}{2} C\,(\Delta y)^2.$$

Two refinements matter in practice.

* **Consensus is not the market's expectation.** Traders position for a number that can differ from the published consensus (the "whisper"). The relevant surprise is relative to positioning, which is not directly observable. A move that seems inconsistent with the headline surprise is often consistent with positioning (Example 2.2).
* **A release is a bundle.** Revisions to prior months, components, and other same-day news all enter $\varepsilon$.

For CRE, the transmission is slower and partial. A change in the 10-year yield passes into cap rates over months, with a pass-through coefficient less than one that varies with credit conditions (Chapter 6). Write the cap-rate response as $\Delta c = \phi\,\Delta y$, with $0 < \phi$ and $\phi$ estimated, not assumed. Value at constant NOI changes by $c_0/(c_0 + \Delta c) - 1$.

### 2.4.5 The reservation-price model of a single-asset sale

Let buyers $i = 1, \dots, n$ have reservation prices $B_i$, and let the seller's reservation price be $R$. In an ascending (English) auction with private values, the bidder with the highest $B$ wins at a price just above the second-highest $B$:

$$P = \max\{B_{(2)}, R\}\quad \text{if } B_{(1)} \ge R; \qquad \text{no trade if } B_{(1)} < R.$$

Here $B_{(1)} \ge B_{(2)} \ge \dots$ are the order statistics. Two results follow.

1. **Removing the top bidder lowers the price to the old third-highest valuation.** If the top two bidders depend on financing that disappears, the price can fall a long way while the median buyer's valuation is unchanged.
2. **When $B_{(1)} < R$, there is no transaction and therefore no price.** The observed market goes quiet. Appraisals, which need transactions, do not fall. This is the mechanism of a frozen market.

For a buyer with fixed equity $E$, financed with a loan that is the lesser of LTV-based and DSCR-based proceeds, the reservation price is capped by financing:

$$B = \min\left\{\frac{E}{1-\text{LTV}},\; E + \frac{NOI}{DSCR \cdot K}\right\},$$

where $K$ is the loan constant (annual debt service per dollar of loan; equal to the interest rate for an interest-only loan). When rates rise, $K$ rises, the DSCR constraint binds, and the financed buyer's reservation price falls even if the buyer's view of the property is unchanged.

Fisher, Gatzlaff, Geltner and Haurin (2003) model transaction volume and prices from the distributions of buyer and seller reservation prices. When buyer reservation prices fall faster than seller reservation prices, as in a credit contraction, observed prices fall less than the buyers' side of the market, and volume collapses. The decline appears first in volume, not in price.

### 2.4.6 Spreads and Roll's estimator

Suppose the efficient price $m$ is constant, and each trade occurs at the ask $m + S/2$ or the bid $m - S/2$ with equal probability, independently of the last trade. Write $p_t = m + \tfrac{S}{2}q_t$, with $q_t = \pm 1$. Then

$$\Delta p_t = \tfrac{S}{2}(q_t - q_{t-1}).$$

The covariance of successive changes is

$$\text{Cov}(\Delta p_t, \Delta p_{t-1}) = \tfrac{S^2}{4}\,\text{Cov}(q_t - q_{t-1},\; q_{t-1} - q_{t-2}) = -\tfrac{S^2}{4}\,\text{Var}(q_{t-1}) = -\tfrac{S^2}{4},$$

because $q$ is serially independent with variance 1. Hence

$$S = 2\sqrt{-\text{Cov}(\Delta p_t, \Delta p_{t-1})}.$$

Roll (1984) showed that the estimator holds when $m$ follows a random walk independent of $q$, because the random-walk increments add no autocovariance. It fails when the autocovariance is positive, which happens when order flow is persistent or prices trend. The square root is then undefined. Small samples are noisy, and the estimate can be well away from the true spread (Example 2.4).

**Round-trip cost.** Buying at $V(1+b)$ and selling at $V(1-s)$ at an unchanged value $V$ loses, per dollar invested,

$$\kappa = 1 - \frac{1 - s}{1 + b} \approx b + s.$$

For a security, $b = s = \tfrac{S/2}{m}$. For private CRE, $b$ includes transfer taxes, legal, diligence, and financing fees, and $s$ includes brokerage and legal. Over a hold of $T$ years, the equivalent geometric annual drag is $1 - (1 - \kappa)^{1/T}$.

### 2.4.7 Appraisal smoothing and the Geltner filter

Model the appraiser's estimate of value, in logs, as a partial adjustment toward the current market value:

$$v^*_t = (1-a)\,v_t + a\,v^*_{t-1}, \qquad 0 \le a < 1.$$

Here $v_t$ is the log market value and $v^*_t$ the log appraised value. Differencing gives the same relation for returns:

$$r^*_t = (1-a)\,r_t + a\,r^*_{t-1}.$$

**Inversion (the Geltner filter).** Solve for $r_t$:

$$\boxed{r_t = \frac{r^*_t - a\,r^*_{t-1}}{1-a}}$$

The filter needs the appraisal return of the previous period, so a series of $N+1$ appraisal returns yields $N$ unsmoothed returns.

**Distributed lag.** Substituting repeatedly,

$$r^*_t = (1-a)\sum_{k=0}^{\infty} a^k\, r_{t-k}.$$

The appraisal return is a geometrically weighted average of current and past market returns. The weights sum to one, so the smoothed index eventually catches up with the market. The **mean lag** is

$$\bar k = \sum_{k} k\,(1-a)a^k = \frac{a}{1-a}\ \text{periods}.$$

**Volatility understatement.** If $r_t$ is i.i.d. with variance $\sigma^2$, then $\text{Var}(r^*) = (1-a)^2\sigma^2 \sum_k a^{2k} = \frac{(1-a)^2}{1-a^2}\sigma^2$, so

$$\frac{\sigma(r^*)}{\sigma(r)} = \sqrt{\frac{1-a}{1+a}}.$$

At $a = 0.6$ on quarterly data, the appraisal index shows half the true volatility, and its mean lag is 1.5 quarters. Correlations with other assets are understated as well, because the smoothed series is a blend of several periods.

**Choosing $a$.** The parameter cannot be observed. Three approaches are used: (i) set $a$ equal to the first-order autocorrelation of the appraisal series, which is exact only if true returns are serially uncorrelated (the assumption Geltner's 1993 method was designed to avoid); (ii) choose $a$ so that the unsmoothed volatility matches an external estimate, such as a REIT or transaction-based index; (iii) take $a$ from studies of the specific index. All three are estimates. Every unsmoothed figure in this book is labeled with the $a$ used, and the conclusion is tested at a second value.

### 2.4.8 Stale comps and selection

**Time adjustment.** At constant NOI, value moves inversely with the cap rate. If a market value index for comparable properties stood at $I_s$ at the comp's sale and $I_0$ now, the comp's cap rate restated to today is

$$c_{\text{now}} = c_{\text{sale}} \cdot \frac{I_s}{I_0}.$$

**Selection.** Let $\Delta_i$ be asset $i$'s change in value and let assets trade only if $\Delta_i > \theta$ (owners of assets that fell further cannot or will not sell). The mean change among traded assets is $E[\Delta \mid \Delta > \theta] \ge E[\Delta]$. The comp set is biased upward by $E[\Delta \mid \Delta > \theta] - E[\Delta]$. The bias rises with the dispersion of value changes and with the severity of the threshold. Both are largest in exactly the market where comps are most needed.

---

## 2.5 Worked examples

All inputs are [HYPOTHESIS] unless cited. All examples are reproduced in `tests/test_ch02_examples.py`.

### Example 2.1 — Clearing a closing auction, and what a market order does

**Given.** The closing call auction for an apartment REIT. Order quantities are in thousands of shares.

| Buy limit (\$) | Quantity | | Sell limit (\$) | Quantity |
|---|---|---|---|---|
| 50.40 | 20 | | 49.90 | 30 |
| 50.30 | 30 | | 50.00 | 40 |
| 50.20 | 40 | | 50.10 | 40 |
| 50.10 | 50 | | 50.20 | 50 |
| 50.00 | 60 | | 50.30 | 60 |

Then a fund meeting redemptions adds a **market sell order of 100** (thousand shares).

**Find.** The clearing price, volume, and imbalance before and after the market order, and the implied price impact.

**Solution.** Cumulative demand $D(p)$ sums buy orders with limits at or above $p$. Cumulative supply $S(p)$ sums sell orders with limits at or below $p$.

| Price | $D(p)$ | $S(p)$ | Volume $\min(D,S)$ | Imbalance $D-S$ | $S(p)$ with +100 market sell | Volume after |
|---|---|---|---|---|---|---|
| 49.90 | 200 | 30 | 30 | +170 | 130 | 130 |
| 50.00 | 200 | 70 | 70 | +130 | 170 | **170** |
| 50.10 | 140 | 110 | **110** | +30 | 210 | 140 |
| 50.20 | 90 | 160 | 90 | −70 | 260 | 90 |
| 50.30 | 50 | 220 | 50 | −170 | 320 | 50 |
| 50.40 | 20 | 220 | 20 | −200 | 320 | 20 |

*Before the market order:* volume is maximized at \$50.10, where 110 thousand shares trade. Demand of 140 exceeds supply of 110, so 30 thousand shares of buy interest at \$50.10 or better go unfilled. The clearing price is **\$50.10**.

*After the market order:* supply rises by 100 at every price. Volume is maximized at \$50.00 (170 thousand shares). At \$50.10, demand of 140 is now the binding side and volume is only 140. The clearing price is **\$50.00**, with 30 thousand shares of unfilled buy interest.

Price impact: $\lambda = \Delta p^*/Q = -0.10/100 = -\$0.001$ per thousand shares, a \$0.10 decline (−0.20%) for 100 thousand shares.

**Check.** At \$50.00 after the market sell, the buyers who trade are all 200 thousand of demand except 30 thousand left unfilled; the sellers who trade are the 100 market plus the 70 limit shares with limits at or below \$50.00. $100 + 30 + 40 = 170$. ✓ No price gives more volume: at \$49.90 supply is only 130, and at \$50.10 demand is only 140.

**Decision consequence.** The fund's redemption-driven selling lowered the close by 10 cents and transferred about $0.10 \times 100{,}000 = \$10{,}000$ to the buyers on that one print. The decline carries no information about the apartments. A desk that understands this can supply liquidity into such auctions: a buy limit order at \$50.00 would have been filled. A desk that *must* sell should split the order or route it to the auction with a limit, because a market order reveals urgency and pays for it. For the opening problem, note that the REIT price that marks your benchmark on any given day contains such non-informational flow. A 28% decline over a year is not produced by closing-auction noise. A 0.2% move on one day can be.

### Example 2.2 — Converting an inflation surprise into price changes

**Given.** Core CPI for the month is released at **0.5%** month over month. The published consensus was **0.3%**. The standard deviation of past surprises on this release is **0.1 percentage point**. Your regression estimate of the 10-year Treasury yield response is **6 bp per one-standard-deviation surprise** [HYPOTHESIS; Chapter 4 shows how to estimate it]. The 10-year note has modified duration **8.5** and convexity **85**. Private apartment cap rates eventually pass through **50%** of a sustained 10-year yield move ($\phi = 0.5$, [HYPOTHESIS]). The current cap rate is **5.50%**. Separately, desk chatter says the market was positioned for **0.4%**.

**Find.** (a) The standardized surprise and yield change. (b) The 10-year price change, with and without convexity. (c) The eventual property value change if the yield move persists. (d) The same quantities if the relevant expectation was the positioned 0.4%.

**Solution.**

(a) $z = (0.5 - 0.3)/0.1 = 2.0$ standard deviations. $\Delta y = 2.0 \times 6 = 12$ bp $= 0.0012$.

(b) Duration only: $\Delta P/P = -8.5 \times 0.0012 = -1.020\%$.
Convexity term: $\tfrac12 \times 85 \times 0.0012^2 = 0.0000612 = +0.006\%$. With convexity: $-1.020\% + 0.006\% = -1.014\%$. Convexity is immaterial for a 12 bp move.

(c) $\Delta c = 0.5 \times 12 = 6$ bp, so the cap rate moves from 5.50% to 5.56%. Value change at constant NOI $= 5.50/5.56 - 1 = -1.079\%$.

(d) Relative to positioning: $z = (0.5 - 0.4)/0.1 = 1.0$. $\Delta y = 6$ bp. $\Delta P/P = -8.5 \times 0.0006 = -0.510\%$. Cap rate +3 bp to 5.53%; value change $= 5.50/5.53 - 1 = -0.542\%$.

**Check.** If the release had printed exactly at consensus, $z = 0$ and the model predicts no move. That is the semi-strong-form statement that expected information is already in the price. Reverse check on (b): $1.02\%/8.5 = 0.12\%$ = 12 bp. ✓

**Decision consequence.** The headline "inflation hot, 0.5% versus 0.3%" overstates the news if traders had positioned for 0.4%. The yield move you should expect is half as large, and a trader who sold bonds on the headline would have bought the *consensus* surprise, not the *market's* surprise. For CRE the consequence is different in kind. A 6 bp change in apartment cap rates is a 1.1% value change, but it will not appear in any appraisal for quarters, and only if the yield move persists. A buyer bidding this week should not reprice an apartment community on one CPI print. A buyer should ask whether the *sequence* of prints has changed the expected path of rates (Chapters 4–6). The listed REIT will reflect the print within minutes; that is the first appearance of the price-discovery gap that §2.9 documents.

### Example 2.3 — The marginal buyer: losing the financed bidders

**Given.** The opening problem's 240-unit apartment community, NOI after reserves **\$3,000,000**. Five potential buyers:

| Bidder | Type | Reservation-price basis |
|---|---|---|
| A | Value-add fund using floating-rate bridge debt | 4.75% cap on in-place NOI |
| B | Syndicator, \$21.0m of equity, agency-style loan: max 65% LTV, min 1.25x DSCR, interest-only | Financing-constrained |
| C | Listed REIT, unlevered, cost-of-capital hurdle | 5.40% cap |
| D | Pension separate account, unlevered | 5.25% cap |
| E | Family office, all cash | 5.60% cap |

Initially the interest rate on B's loan is **4.50%** (interest-only, so $K = 0.045$). Then credit tightens: **bridge lenders stop quoting** (A exits), and B's rate rises to **6.25%**. Nobody's view of NOI changes. The seller's reservation price is **\$60.0 million**: the closed-end fund carries the asset at that appraised value and a lower sale would force a reported write-down.

**Find.** Reservation prices before and after; the clearing price and implied cap rate; whether a trade occurs at the seller's reserve.

**Solution.**

*Unlevered and cap-based reservation prices,* $B = NOI/c$:

* A: $3{,}000{,}000/0.0475 = \$63{,}157{,}895$
* C: $3{,}000{,}000/0.0540 = \$55{,}555{,}556$
* D: $3{,}000{,}000/0.0525 = \$57{,}142{,}857$
* E: $3{,}000{,}000/0.0560 = \$53{,}571{,}429$

*B before tightening:* LTV-bound price $= 21{,}000{,}000/(1 - 0.65) = \$60{,}000{,}000$. DSCR-bound loan $= 3{,}000{,}000/(1.25 \times 0.045) = \$53{,}333{,}333$, so DSCR-bound price $= 21{,}000{,}000 + 53{,}333{,}333 = \$74{,}333{,}333$. The LTV constraint binds: $B_B = \$60{,}000{,}000$.

*B after tightening:* DSCR-bound loan $= 3{,}000{,}000/(1.25 \times 0.0625) = \$38{,}400{,}000$. DSCR-bound price $= 21{,}000{,}000 + 38{,}400{,}000 = \$59{,}400{,}000$, below the LTV-bound \$60.0 million. Now the DSCR constraint binds: $B_B = \$59{,}400{,}000$.

| | Ranked reservation prices | $B_{(1)}$ | $B_{(2)}$ = clearing price (absent reserve) | Implied cap |
|---|---|---|---|---|
| Before | A 63.16, **B 60.00**, D 57.14, C 55.56, E 53.57 | 63.16 | **\$60.00m** | 5.00% |
| After | B 59.40, **D 57.14**, C 55.56, E 53.57 | 59.40 | **\$57.14m** | 5.25% |

Before tightening, A wins at about \$60.0 million. The marginal buyer is the levered syndicator B. After tightening, B would win at about \$57.14 million, and the marginal buyer is the unlevered pension account D. The clearing price falls by $57.142857/60.0 - 1 = -4.76\%$ and the implied cap rate rises 25 bp, with **no change in NOI and no change in any unlevered buyer's required return**.

*With the seller's reserve of \$60.0 million:* after tightening, $B_{(1)} = 59.4 < 60.0$. **No trade occurs.** Before tightening, $B_{(1)} = 63.16 \ge 60.0$ and the trade clears at $\max(60.0, 60.0) = \$60.0$ million.

**Check.** Price after tightening $= \max(B_{(2)}, R)$ only if $B_{(1)} \ge R$. Since $59.4 < 60.0$, the reserve, not the bidders, determines the outcome. Independent check of B's DSCR: at \$59.4 million with a \$38.4 million loan, interest $= 38{,}400{,}000 \times 0.0625 = \$2{,}400{,}000$, and $3{,}000{,}000/2{,}400{,}000 = 1.25$x. ✓ LTV $= 38.4/59.4 = 64.6\% < 65\%$. ✓

**Decision consequence.** Three lessons for the opening problem. First, the broker's \$60.0 million guidance was the price *when financed buyers were marginal*. With them gone, a fully marketed auction would clear near \$57.1 million on the same NOI, and that is before any change in the unlevered buyers' required returns. Second, because the seller will not accept \$57.1 million, the most likely outcome is **no trade**: the listing is withdrawn, the appraisal stays at \$60.0 million, and the "market" records nothing. Silence in a market is information. Third, your bid should be built from the valuation of the buyer you expect to be marginal *at closing*, which requires a view on credit availability, not only on rents. If you are an unlevered buyer with a 5.25% hurdle, you are D, and you will be marginal. The seller must move to you, or the asset will not trade.

### Example 2.4 — Roll's spread and the cost of a round trip

**Given.** Twelve consecutive trade prices for a small-capitalization REIT whose efficient price did not change during the sample. Prices in dollars:

20.05, 19.95, 20.05, 20.05, 19.95, 19.95, 20.05, 19.95, 20.05, 19.95, 19.95, 20.05

(The true quoted spread is \$0.10 around a \$20.00 midpoint; the estimator does not know this.)

Private CRE comparison: buyer costs **1.5%** of value (transfer tax, legal, diligence, loan fees), seller costs **2.5%** (brokerage, legal).

**Find.** (a) Roll's spread estimate and its proportion of the midpoint. (b) The round-trip cost of the REIT at the *true* spread and of the property. (c) The geometric annual drag of each over 1-, 3-, and 7-year holds.

**Solution.**

(a) Price changes $\Delta p_t$ ($N = 11$):

−0.10, +0.10, 0.00, −0.10, 0.00, +0.10, −0.10, +0.10, −0.10, 0.00, +0.10

Form ten pairs $(\Delta p_t, \Delta p_{t-1})$ for $t = 2, \dots, 11$. The sample covariance (divisor $n - 1 = 9$, each vector demeaned by its own mean) is

$$\widehat{\text{Cov}} = -0.0043333.$$

Then

$$\hat S = 2\sqrt{0.0043333} = 2 \times 0.065828 = \$0.1317,$$

which is $0.1317/20.00 = 0.658\%$ of the midpoint.

The estimate overstates the true \$0.10 spread by about 32%. With eleven price changes the sampling error is large. Roll's estimator is a tool for long samples or for comparisons across many securities, not a precise measurement from a few trades.

(b) REIT round trip at the true spread: $b = s = 0.05/20.00 = 0.25\%$.

$$\kappa_{\text{REIT}} = 1 - \frac{1 - 0.0025}{1 + 0.0025} = 0.499\%.$$

Property: $\kappa_{\text{CRE}} = 1 - \frac{1 - 0.025}{1 + 0.015} = 1 - 0.960591 = 3.941\%$.

(c) Annual drag $= 1 - (1-\kappa)^{1/T}$:

| Hold | REIT (0.499%) | Property (3.941%) |
|---|---|---|
| 1 year | 0.499% | 3.941% |
| 3 years | 0.167% | 1.331% |
| 7 years | 0.071% | 0.573% |

**Check.** The approximation $\kappa \approx b + s$ gives 0.50% and 4.00%. The exact values are slightly smaller because the sale cost is paid on a dollar that already bore the purchase cost. For (a), the sign of the covariance is what the model predicts: bid–ask bounce makes successive changes negatively correlated.

**Decision consequence.** A one-year speculation in private CRE must earn about 3.9% more than the same view expressed through a REIT, before considering the time and diligence cost of executing it. The private route is reasonable only for longer holds or for value the REIT cannot capture (operational improvement, a specific asset's mispricing, control). For the opening problem, a view that "apartment values will recover within a year" is cheaper to express through REIT shares; a view that "this specific community can be bought below replacement cost and held for seven years" justifies the private round trip. The spread is not the only cost: the REIT carries leverage and corporate overhead that the private asset does not (§2.4.3, item 5).

### Example 2.5 — Unsmoothing an appraisal index

**Given.** Quarterly appreciation returns from an appraisal-based index of core apartment properties, starting with the quarter *before* the sample (r*₀):

| Quarter | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| $r^*_t$ | +2.0% | +1.5% | +0.5% | −1.0% | −2.0% | −2.2% | −2.0% | −1.5% | −1.0% |

Smoothing parameter $a = 0.6$ [HYPOTHESIS; §2.4.7 explains why it must be treated as an estimate].

**Find.** (a) Unsmoothed quarterly returns $r_1, \dots, r_8$. (b) Cumulative change over the eight quarters, smoothed and unsmoothed. (c) The mean lag and the volatility ratio implied by $a$. (d) A check that re-smoothing recovers the appraisal series.

**Solution.**

(a) $r_t = (r^*_t - 0.6\,r^*_{t-1})/0.4$:

| $t$ | Computation | $r_t$ |
|---|---|---|
| 1 | $(1.5 - 0.6 \times 2.0)/0.4 = 0.3/0.4$ | +0.75% |
| 2 | $(0.5 - 0.6 \times 1.5)/0.4 = -0.4/0.4$ | −1.00% |
| 3 | $(-1.0 - 0.6 \times 0.5)/0.4 = -1.3/0.4$ | −3.25% |
| 4 | $(-2.0 - 0.6 \times (-1.0))/0.4 = -1.4/0.4$ | −3.50% |
| 5 | $(-2.2 - 0.6 \times (-2.0))/0.4 = -1.0/0.4$ | −2.50% |
| 6 | $(-2.0 - 0.6 \times (-2.2))/0.4 = -0.68/0.4$ | −1.70% |
| 7 | $(-1.5 - 0.6 \times (-2.0))/0.4 = -0.3/0.4$ | −0.75% |
| 8 | $(-1.0 - 0.6 \times (-1.5))/0.4 = -0.1/0.4$ | −0.25% |

(b) Smoothed: $\prod(1 + r^*_t) - 1$ over quarters 1–8 $= -7.50\%$. Unsmoothed: $\prod(1 + r_t) - 1 = -11.64\%$. The appraisal index has recognized about two-thirds of the decline ($7.50/11.64 = 0.64$).

(c) Mean lag $= a/(1-a) = 0.6/0.4 = 1.5$ quarters. Volatility ratio for i.i.d. true returns $= \sqrt{0.4/1.6} = 0.50$: the appraisal index shows half the true volatility.

(d) Re-smoothing with $r^*_t = 0.4\,r_t + 0.6\,r^*_{t-1}$ from $r^*_0 = 2.0\%$: $r^*_1 = 0.4(0.75) + 0.6(2.0) = 1.5\%$, $r^*_2 = 0.4(-1.0) + 0.6(1.5) = 0.5\%$, and so on. The original series is recovered exactly. ✓

**Check.** The unsmoothed series turns down in quarter 2, one quarter before the appraisal series, and its worst quarter is quarter 4, one quarter before the appraisal series' worst. By quarter 8 the unsmoothed market return (−0.25%) is close to flat while the appraisal index still reports −1.0%. That is the signature of lag: appraisals keep falling after the market has stabilized. The sample standard deviations are 1.32% (smoothed) and 1.49% (unsmoothed). The ratio is not 0.50 because this short path is trending, not i.i.d., which is a reminder that the volatility ratio formula is an asymptotic result.

**Decision consequence.** An LP reading the appraisal index in quarter 8 sees a 7.5% decline and continuing write-downs. The unsmoothed series says the decline was about 11.6% and that it has largely stopped. Two errors are possible. Investors who treat appraisal NAV as a price will redeem at NAV when NAV is above market (selling the remaining LPs a loss) and stay out at the bottom when NAV is still falling but the market has stabilized. Sensitivity matters too: with $a = 0.75$ the same data imply a cumulative decline of 15.69%, with the worst quarter (−5.50%) in quarter 3 rather than quarter 4, and a positive return (+0.50%) by quarter 8 (Problem 2.6 uses $a = 0.7$). The decision should hold at both values of $a$, or it is resting on an assumption you cannot verify.

### Example 2.6 — A biased comp set

**Given.** The broker's four comps for the opening problem's garden community. All are Class A, 2015–2021 vintage, with cap rates on in-place NOI after reserves. A transaction-based value index for Class A suburban apartments in the metro (now = 90) is used for time adjustment. The subject is Class B, 1998 vintage. Your assumption for the Class B cap-rate premium in this metro is **+30 bp** [HYPOTHESIS]. Subject NOI **\$3,000,000**.

| Comp | Months before today | Cap rate | Index at sale | Seller |
|---|---|---|---|---|
| C1 | 11 | 4.70% | 100 | Developer, merchant build |
| C2 | 9 | 4.80% | 98 | Core fund rebalancing |
| C3 | 2 | 5.10% | 92 | Estate, unlevered |
| C4 | 1 | 5.20% | 91 | Private owner, 1031 buyer |

A second dataset: eight properties in the submarket, with appraised value changes over the year of −4%, −6%, −9%, −12%, −15%, −18%, −22%, and −30%. Only the three with declines smaller than 10% traded; the others' owners withdrew or extended their loans.

**Find.** (a) The naive comp average and implied value. (b) Time-adjusted comp cap rates and value. (c) Quality-adjusted value for the subject. (d) The selection bias in the second dataset.

**Solution.**

(a) Naive average cap $= (4.70 + 4.80 + 5.10 + 5.20)/4 = 4.95\%$. Value $= 3{,}000{,}000/0.0495 = \$60{,}606{,}061$, which supports the broker's \$60.0 million.

(b) $c_{\text{now}} = c_{\text{sale}} \times I_s/90$:

* C1: $4.70 \times 100/90 = 5.2222\%$
* C2: $4.80 \times 98/90 = 5.2267\%$
* C3: $5.10 \times 92/90 = 5.2133\%$
* C4: $5.20 \times 91/90 = 5.2578\%$

Average $= 5.2300\%$. Class A value today $= 3{,}000{,}000/0.0523 = \$57{,}361{,}377$.

(c) Subject cap $= 5.23\% + 0.30\% = 5.53\%$. Value $= 3{,}000{,}000/0.0553 = \$54{,}249{,}548$. This is 10.5% below the naive \$60.6 million.

(d) Population mean change $= (-4 - 6 - 9 - 12 - 15 - 18 - 22 - 30)/8 = -14.50\%$. Traded mean $= (-4 - 6 - 9)/3 = -6.33\%$. Selection bias $= -6.33 - (-14.50) = +8.17$ percentage points.

**Check.** After time adjustment the four comps agree within 4.5 bp (5.2133% to 5.2578%). Before adjustment they span 50 bp. That convergence suggests the dispersion in the raw comps was mostly time, not property differences. Independent check of (c): $54{,}249{,}548 \times 0.0553 = 3{,}000{,}000$. ✓

**Decision consequence.** The broker's comp set fails three ways. Two comps are stale: they priced a market that financed buyers set (Example 2.3). All four are Class A, while the subject is Class B. And the time index itself is built from transactions that survived the selection filter in (d), so if anything it *understates* the decline. A defensible range for the subject is roughly \$54 million (time- and quality-adjusted) to \$57 million (the unlevered marginal buyer of Example 2.3 at 5.25%). That range sits entirely below the seller's \$60.0 million. Unless the seller is forced, there will be no trade at a price you should pay. The right action is to bid in the range, state the reason in writing, and wait. If the selection bias in (d) applies to the index, the right bid is lower still. Do not bid "close to ask to stay in the game".

### Example 2.7 — How much should appraisal NAV move? Reconciling three prices

**Given.** The opening problem's three numbers: fund appraisal cap 4.30%; REIT-implied cap 5.60%; and your own estimate for a similar private asset from Examples 2.3 and 2.6, which brackets 5.25%–5.53%.

**Find.** The percentage value gap between the appraisal and each market-based estimate at constant NOI.

**Solution.** Value ratio at constant NOI $= c_{\text{appraisal}}/c_{\text{market}}$:

* REIT-implied: $4.30/5.60 - 1 = -23.21\%$
* Private, unlevered marginal buyer (5.25%): $4.30/5.25 - 1 = -18.10\%$
* Private, comp-based (5.53%): $4.30/5.53 - 1 = -22.24\%$

**Check.** All three are negative and between 18% and 23%. The fund has written down only 3%. Even if the REIT market overreacted, the private-market evidence alone implies a gap of roughly 18–22%.

**Decision consequence.** The fund's NAV is a lagged moving average, not a price. If you can redeem at NAV, you sell at a price about 18–23% above where the fund's assets would trade. The remaining LPs pay for it (Problem 2.8 computes the transfer). The fund manager knows this, which is why redemptions are paid "as liquidity permits" and NAV is likely to be marked down before your units are paid. A request to redeem is still rational: it gives you a place in the queue at low cost. But the expected payout is not today's NAV. For the REIT, a 5.60% implied cap is close to the private-market evidence, so REIT shares are not obviously cheap relative to private value. They are cheap only relative to a stale appraisal.

---

## 2.6 CRE application: reading a market that does not print

Private CRE is a market where the price you need is usually not observable. The professional response is to triangulate, using each price source for what it can and cannot tell you.

| Source | What it measures | Lag | Main bias |
|---|---|---|---|
| Listed REIT implied cap rate | Marginal public-equity investor's valuation of a REIT's portfolio | Minutes | Includes REIT leverage, management, liquidity, sentiment; noise-trader risk |
| Transaction-based index (repeat-sales or hedonic) | Prices of properties that traded | 1–2 quarters (closing lag plus reporting) | Selection: in downturns, survivors overstate value |
| Appraisal-based index (NCREIF NPI, NFI-ODCE) | Appraisers' estimates of market value | Several quarters (smoothing) | Smoothing, anchoring; understates volatility and correlation |
| Broker opinion of value (BOV) | What a broker believes a listing can achieve | Current, but advocacy | Incentive to win the listing; comp selection |
| Your own reservation-price analysis | Who could pay what, now | Current | Your own assumptions |

Five working rules follow.

1. **Price the marginal buyer, not the average one.** Ask who will be the second-highest bidder at closing. Build that bidder's valuation from their cost of capital and their financing (Example 2.3).
2. **Restate every comp to today and to the subject.** A comp is a past auction result under past financing. Adjust for time with the least biased index available, and for quality with a stated, testable premium (Example 2.6).
3. **Read volume as a signal.** A collapse in transaction count with stable reported prices means the bid and ask distributions have separated. Prices on the few trades that do occur overstate where the median asset would clear.
4. **Use the REIT market as a lead indicator, not as a price.** REIT prices move first. Divergence tells you the direction appraisals will likely take. The size of the eventual private adjustment can differ because the claims differ (§2.8).
5. **Never treat NAV as a price.** When deciding whether to buy into, redeem from, or lend against an appraisal-valued fund, unsmooth or cross-check the NAV.

**Hotels.** Hotels reprice faster than other private CRE in the income line because rates reset nightly, but their *values* are still appraised and traded privately. In a downturn, hotel comps are especially biased: the hotels that trade are unencumbered, brand-strong, or in a forced sale, and the trades often carry PIPs or seller financing that change the effective price. Always restate the price to the cash-equivalent, PIP-adjusted basis before using it (Chapter 11).

---

## 2.7 Price discovery in liquid versus illiquid markets

Price discovery is the process by which new information is incorporated into prices. In a liquid market it happens through trades, which are cheap, frequent, and anonymous. In an illiquid market it happens through negotiations, which are costly, infrequent, and bilateral.

| Feature | Liquid (REITs, Treasuries, futures) | Illiquid (private CRE, hotels) |
|---|---|---|
| Trades per asset per year | Thousands to millions | Usually zero or one |
| Time to transact | Seconds | 3–9 months |
| Round-trip cost | Tens of basis points or less | About 3–6% (Example 2.4 assumes 3.9%) [HYPOTHESIS range] |
| Who is marginal | Many competing dealers and investors | The second-highest of a few bidders |
| Information in a price | Aggregated across many traders | One negotiation; terms often private |
| Short selling | Possible (with frictions) | Not possible |
| Reported value series | Transaction prices | Appraisals and occasional sales |
| Failure mode under stress | Prices gap down; spreads widen; volume rises | Volume collapses; reported values freeze |

Two consequences matter for a speculator.

**Lead–lag.** Because public prices incorporate information first, listed REIT returns tend to lead appraisal-based private returns. Nareit, an industry association for REITs, describes this lead as roughly four to eight quarters [FACT that Nareit makes this claim; ch02-S07. The size of the lead is an empirical estimate that varies across studies and periods; Nareit is an interested party]. A lead is not a profitable trading rule by itself: you cannot short the appraisal index, and an open-end fund's NAV is not a price at which you can freely trade.

**Two prices for one risk.** At any time the public and private markets may be pricing the same buildings differently. The gap closes through flows: REITs selling assets to private buyers when private values are higher, private buyers taking REITs private when REITs are cheaper, open-end funds marking down NAV under redemption pressure. Each mechanism has costs and delays. That is why gaps persist (§2.4.3).

---

## 2.8 When the relationship fails

1. **The unsmoothing parameter is wrong or unstable.** $a$ is not a physical constant. Appraisal practice changes. Appraisers in some markets have, in some downturns, marked values down *faster* than transaction evidence (MSCI has documented such a reversal in some European markets in the 2022–23 downturn [ch02-S11, VERIFIED-SECONDARY]). Applying a historical $a$ to such a series produces an overshoot. Always test at two values of $a$, and check the result against transaction evidence.
2. **The REIT is not the property.** A REIT is a levered, managed, taxed-differently claim with its own cost of capital, development pipeline, and sentiment. Its implied cap rate depends on the analyst's estimate of NOI and of the value of non-property items. A REIT discount to NAV can persist for years. Treating the REIT-implied cap rate as the true private value assumes away exactly the frictions that let the two diverge.
3. **Surprise sensitivities change with regime.** The bond market's response to an inflation surprise depends on what the central bank is believed to do about it. A sensitivity estimated in a low-inflation regime can understate the response in a high-inflation one, and vice versa (Chapter 5).
4. **Consensus is stale or gamed.** Forecasts submitted days before a release can miss late information. The relevant expectation is positioning, which is not observable. A model built on published consensus will sometimes give the wrong sign.
5. **Roll's estimator fails with trending or autocorrelated order flow.** When the autocovariance of price changes is positive, the estimator is undefined. In thin markets with persistent order flow, the spread is underestimated or cannot be estimated.
6. **The reservation-price model ignores strategic bidding and information.** In a common-value auction, bidders who know others are bidding shade their bids to avoid the winner's curse. Sellers can run processes that extract more than the second-highest valuation. Example 2.3 is a benchmark, not a forecast of the hammer price.
7. **Selection can run the other way.** In a boom, the properties that trade can be the weakest (owners selling into strength), so transaction indices understate quality-adjusted prices. Always ask why *these* assets traded *now*.
8. **The market is frozen because the seller has information.** A seller who will not accept the buyer's price may know something the buyer does not: a lease about to sign, a tax appeal about to succeed. The no-trade outcome does not always mean the seller is anchored.

---

## 2.9 Historical episode: the 2022–23 divergence between listed REITs and private appraisals

**Date and environment.** From the end of 2021 the Federal Reserve raised its policy rate rapidly to counter high inflation. According to Nareit's analysis, the 10-year Treasury yield rose 212 bp from the fourth quarter of 2021 to 3.65% in the first quarter of 2023 [FACT; ch02-S01, Nareit, VERIFIED-SECONDARY]. Higher rates raised the cost of mortgage debt and the yield required on real estate.

**What the listed market did.** The FTSE Nareit All Equity REITs index returned −24.95% in calendar 2022 [FACT; ch02-S02, Nareit fact sheet, VERIFIED-SECONDARY]. Nareit's T-Tracker analysis reports that REIT-implied cap rates rose 135 bp to 5.85% between the fourth quarter of 2021 and the first quarter of 2023 [FACT; ch02-S01].

**What the private market reported.** Over the same period, according to the same Nareit analysis, transaction cap rates rose 77 bp to 5.43%, and appraisal cap rates rose 22 bp to 4.05% [FACT; ch02-S01]. Nareit put the gap between the REIT-implied cap rate and the private appraisal cap rate at 180 bp in the first quarter of 2023 [FACT; ch02-S01]. Nareit also reported that the gap between REIT-implied and transaction cap rates peaked at 138 bp in the second quarter of 2022 and had narrowed to 42 bp by the first quarter of 2023 [FACT; ch02-S03, VERIFIED-SECONDARY].

The appraisal-based index of core open-end funds, NFI-ODCE, recorded a gross total return of +0.52% in the third quarter of 2022, with an appreciation return of −0.28% [FACT; ch02-S04, NCREIF, VERIFIED-SECONDARY]. In the fourth quarter of 2022 its gross total return was −4.97%, with appreciation of −5.76% [FACT; ch02-S05, VERIFIED-SECONDARY]. NCREIF's release for the third quarter of 2023 reported a one-year gross total return of −12.14%, made up of 3.46% income and −15.19% appreciation, and described it as the largest negative appreciation since the Global Financial Crisis [FACT; ch02-S06, NCREIF press release dated 30 October 2023, VERIFIED-SECONDARY].

**Reading the figures with this chapter's tools.**

* *Cap-rate gaps as value gaps* [INFERENCE]. At constant NOI, the first-quarter 2023 appraisal cap rate of 4.05% against a transaction cap rate of 5.43% implies appraisals about $4.05/5.43 - 1 = -25.4\%$ above where trades were clearing, if NOI and property mix were comparable. Against the REIT-implied 5.85%, the gap is $4.05/5.85 - 1 = -30.8\%$. These are upper bounds on the information in the figures: the three cap-rate series cover different property samples and NOI definitions, and REIT-implied cap rates depend on analysts' NOI estimates.
* *Order of adjustment* [INFERENCE]. The listed market moved first, the transaction market second (77 bp versus 135 bp by early 2023), and appraisals last (22 bp). That is the ordering the price-discovery and smoothing models of §§2.4.5–2.4.7 predict: continuous markets incorporate rate changes at once; transactions follow as buyers' reservation prices fall and some sellers accept them; appraisals follow the transactions with a lag.
* *Cumulative appraisal write-down* [INFERENCE]. Chaining the published NFI-ODCE appreciation figures, the four quarters to the third quarter of 2023 (−15.19%) followed the third quarter of 2022 (−0.28%), for a cumulative appreciation of $(1 - 0.0028)(1 - 0.1519) - 1 = -15.43\%$ over five quarters. Appraisals were therefore still converging toward the cap-rate gaps visible in early 2023 more than a year later, which is what a smoothed series does.
* *The Federal Reserve's view.* The Board's May 2023 *Financial Stability Report* described CRE valuations as elevated though declining and warned that a correction could be sizable and cause losses for holders of CRE debt [as reported in press coverage of the report, ch02-S08; not yet checked against the report itself, so treat as *(verification pending)*].

**Participants and incentives.** Open-end fund investors who wanted liquidity could redeem at appraisal-based NAV, which gave an incentive to redeem early, before NAV was marked down; funds responded by queuing redemptions [INFERENCE from the mechanism in Problem 2.8; queue sizes for specific funds are not stated here because they have not been verified]. Owners with maturing loans faced refinancing at higher rates with lower loan proceeds (Example 2.3's DSCR mechanism). Lenders and owners had joint incentives to extend rather than force sales, which kept distressed assets out of the transaction record (Example 2.6's selection mechanism) [INFERENCE].

**What was knowable at the time.** By the end of 2022, the rise in Treasury yields, the REIT index decline, and the gap between REIT-implied and appraisal cap rates were all public. A reader of this chapter in late 2022 could have predicted the *direction* of private write-downs with high confidence. What was not knowable was their *size*, which depended on how far NOI growth would offset higher cap rates, on how long rates would stay high, and on whether REIT prices were themselves overshooting. Nor was the *timing* knowable, because appraisal practice and fund governance determine how fast NAV moves.

**Competing interpretations.**

1. *Appraisal lag* (the interpretation this chapter emphasizes): private values had fallen as much as REIT prices implied, and appraisals were catching up.
2. *Listed-market overreaction*: REIT prices overshot because of sentiment, fund outflows, and leverage, and private values deserved a smaller decline. Part of the subsequent narrowing could come from REITs recovering rather than appraisals falling.
3. *Composition and quality*: the indices hold different property mixes (for example, office exposure differs), so some of the gap is not mispricing at all.

All three can be partly true. Distinguishing them requires property-level matching of REIT and private holdings, which is beyond public data. Note also that two of the sources are interested parties: Nareit represents REITs, and its framing tends to favor listed real estate.

**What the case does and does not establish.** It establishes that, in a sharp rate shock, private appraisal-based values moved far less, and later, than listed REIT prices and transaction cap rates, and that the gap was visible in public data at the time. It does **not** establish that REITs were "right" and appraisals "wrong" in any given quarter, that the gap was exploitable as an arbitrage (it could not be shorted directly, and a long-REIT, short-private position cannot be built), or that a specific unsmoothing parameter would have predicted the timing of write-downs.

**An earlier parallel.** In the 2008–09 crisis the appraisal-based NCREIF Property Index fell by about 31.5% from a peak in the first quarter of 2008 to a trough in the first quarter of 2010 [FACT as reported by Nareit, ch02-S09, VERIFIED-SECONDARY; check against NCREIF index levels before quoting the decimal]. Listed REITs peaked earlier, in early 2007 [same source]. The ordering was the same: public first, private later.

---

## 2.10 Decision exercise: three prices, one decision

Return to the opening problem. You have three possible actions and abstention. Complete the decision record at `desk/investment_memos/decision_record_template.md`. Your record must include:

1. **A value range for the 240-unit garden community**, built from the marginal-buyer analysis (Example 2.3) and the restated comps (Example 2.6). State which buyer you expect to be marginal and why.
2. **A bid, or a decision not to bid**, with the walk-away price and what would change it. Specify the information you would require: rent roll, trailing-twelve-month operating statement, capital needs, loan terms the seller is under, and the reason the seller is selling now.
3. **The redemption decision.** Compute the expected payout per unit if NAV is marked down 15% before the queue clears. Decide whether to file a redemption request, and say what you would do with the proceeds.
4. **The REIT decision.** Is a 5.60% implied cap rate cheap relative to your private-market estimate? What would you be speculating on if you bought the shares? What is the invalidation trigger?
5. **What you will not do, and why.** Abstention from any or all actions is acceptable if justified.

**Rubric** (see `problems/solutions/ch02_solutions.md`, §Decision exercise). Full credit requires: (a) a private value range that sits below \$60.0 million and is derived, not asserted; (b) recognition that the seller's reserve and the marginal buyer's valuation do not overlap, so the likely outcome is no trade at current guidance; (c) a correct statement that NAV is not a redemption price and that redeeming at a stale NAV transfers value from remaining LPs; (d) recognition that the REIT is cheap relative to the appraisal but not obviously relative to private-market evidence; and (e) explicit invalidation criteria. There is no single correct allocation.

---

## 2.11 Frequent analytical errors

1. **Treating the last trade as the value.** A price is a marginal transaction under the financing and urgency of its day.
2. **Treating appraised NAV as a price.** NAV is a smoothed, lagged estimate. Unsmooth it or cross-check it before buying, redeeming, or lending against it.
3. **Reacting to headlines instead of surprise.** A "strong" number that was expected is not news. Measure surprise against consensus *and* ask what was positioned.
4. **Averaging stale comps.** Restate each comp to today with a stated index and to the subject with a stated quality premium.
5. **Ignoring selection.** The comps that exist in a downturn are survivors. Ask why the others did not trade.
6. **Pricing the average buyer.** The price is set by the second-highest bidder at closing. If the most aggressive bidders depended on financing that has gone, so has their price.
7. **Calling a public–private gap an arbitrage.** It has no convergence date, cannot be shorted on the private side, and the claims are not identical.
8. **Using Roll's estimator on a handful of trades.** The estimate is noisy and can be undefined. Report it with the sample size.
9. **Unsmoothing with one value of $a$.** The parameter is an assumption. Show the result at two values.
10. **Confusing no trade with no price change.** A frozen market is one where the clearing price has fallen below sellers' reservations. The decline is real even though nothing prints.

---

## 2.12 Connections to other chapters

* Chapter 1 introduced liquidity provision, the price of immediacy, and adverse-selection spreads; this chapter shows how those forces set prices.
* Chapter 3 extends the marginal-buyer model to reflexive collateral loops and forced-selling price impact.
* Chapter 4 builds surprise indices and estimates the sensitivities used in Example 2.2.
* Chapter 6 develops the cap-rate/Treasury relationship and the pass-through coefficient $\phi$.
* Chapter 9 treats comparable-sales adjustment and valuation in full (`desk/investment_memos/comparable_sale_adjustment_worksheet.md`).
* Chapter 10 develops the loan-sizing constraints that determine financed buyers' reservation prices.
* Chapter 12 uses REIT-implied cap rates and maturity walls to time distressed CRE purchases.
* Chapter 23 revisits 2008–09 in full.

---

## 2.13 One-page reference sheet

**Questions to ask of any price:** Who was marginal? Who had to trade? What was expected? How old is the evidence? Why did *this* asset trade *now*?

| Formula | Expression |
|---|---|
| Call auction | $p^* = \arg\max_p \min\{D(p), S(p)\}$; ties: min $\lvert D-S \rvert$ |
| Price impact | $\lambda = \Delta p^*/Q$ |
| Grossman–Stiglitz informed share | $\lambda^* = 1 - c/\alpha_0$ (for $\alpha(\lambda) = \alpha_0(1-\lambda)$) |
| Standardized surprise | $z = (x - \text{consensus})/\sigma_{\text{surprise}}$ |
| Yield and price response | $\Delta y = b z$; $\Delta P/P \approx -D_{mod}\Delta y + \tfrac12 C \Delta y^2$ |
| Cap-rate pass-through | $\Delta c = \phi \Delta y$; $\Delta V/V = c_0/(c_0 + \Delta c) - 1$ |
| Single-asset auction | $P = \max\{B_{(2)}, R\}$ if $B_{(1)} \ge R$; else no trade |
| Financed reservation price | $B = \min\{E/(1-\text{LTV}),\; E + NOI/(DSCR \cdot K)\}$ |
| Roll spread | $S = 2\sqrt{-\text{Cov}(\Delta p_t, \Delta p_{t-1})}$ |
| Round trip | $\kappa = 1 - (1-s)/(1+b) \approx b + s$; annual drag $1 - (1-\kappa)^{1/T}$ |
| Smoothing | $r^*_t = (1-a) r_t + a r^*_{t-1}$ |
| Geltner filter | $r_t = (r^*_t - a r^*_{t-1})/(1-a)$ |
| Mean lag; volatility ratio | $a/(1-a)$; $\sqrt{(1-a)/(1+a)}$ |
| Comp time adjustment | $c_{\text{now}} = c_{\text{sale}} \cdot I_s/I_0$ |
| Selection bias | $E[\Delta \mid \text{traded}] - E[\Delta]$ |

**Benchmarks from this chapter's examples (hypothetical):** $a = 0.6$ quarterly → mean lag 1.5 quarters, volatility halved. Private round trip of about 4% → about 1.3% a year over 3 years. Losing the top two financed bidders on a \$3.0 million NOI asset moved the clearing price from \$60.0 million to \$57.1 million.

**Documented 2022–23 benchmarks (Nareit; §2.9):** Q4 2021 to Q1 2023: REIT-implied cap +135 bp to 5.85%; transaction cap +77 bp to 5.43%; appraisal cap +22 bp to 4.05%.

---

## References for this chapter

All sources are listed in `references/sources_ch02.md` with verification status.

* Andersen, T. G., Bollerslev, T., Diebold, F. X., and Vega, C. (2003). "Micro Effects of Macro Announcements: Real-Time Price Discovery in Foreign Exchange." *American Economic Review*, 93(1), 38–62.
* Balduzzi, P., Elton, E. J., and Green, T. C. (2001). "Economic News and Bond Prices: Evidence from the U.S. Treasury Market." *Journal of Financial and Quantitative Analysis*, 36(4), 523–543.
* Fama, E. F. (1970). "Efficient Capital Markets: A Review of Theory and Empirical Work." *Journal of Finance*, 25(2), 383–417.
* Fisher, J., Gatzlaff, D., Geltner, D., and Haurin, D. (2003). "Controlling for the Impact of Variable Liquidity in Commercial Real Estate Price Indices." *Real Estate Economics*, 31(2), 269–303.
* Geltner, D. (1993). "Estimating Market Values from Appraised Values without Assuming an Efficient Market." *Journal of Real Estate Research*, 8(3), 325–345.
* Grossman, S. J., and Stiglitz, J. E. (1980). "On the Impossibility of Informationally Efficient Markets." *American Economic Review*, 70(3), 393–408.
* Kyle, A. S. (1985). "Continuous Auctions and Insider Trading." *Econometrica*, 53(6), 1315–1335.
* Quan, D. C., and Quigley, J. M. (1991). "Price Formation and the Appraisal Function in Real Estate Markets." *Journal of Real Estate Finance and Economics*, 4(2), 127–146.
* Roll, R. (1984). "A Simple Implicit Measure of the Effective Bid-Ask Spread in an Efficient Market." *Journal of Finance*, 39(4), 1127–1139.
* Shleifer, A., and Vishny, R. W. (1997). "The Limits of Arbitrage." *Journal of Finance*, 52(1), 35–55.
* Nareit, NCREIF, MSCI, and Federal Reserve items for §2.9: see `references/sources_ch02.md` (ch02-S01 to ch02-S11).
