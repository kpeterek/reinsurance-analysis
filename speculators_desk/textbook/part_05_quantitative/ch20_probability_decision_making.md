# Chapter 20 — Probability and Statistical Decision-Making

> **Status:** Complete (v1.0). Numerical examples, problems, and drills D177–D184 are reproduced in `tests/test_ch20_examples.py` and `training/daily_drills/drill_checks_ch20.py`, using the new library module `models/python/sdesk/x_decision.py`. Problems are in `problems/questions/ch20_problems.md` and solutions in `problems/solutions/ch20_solutions.md`. Sources are in `references/sources_ch20.md`. Open items: the SPF "anxious index" readings for the 2007:Q4–2008:Q3 surveys are marked *(verification pending)* and are not used in any calculation. Several bibliographic entries still need a direct check (see the source file).

## Learning objectives

After this chapter you should be able to:

1. Decompose the variance of a CRE outcome into within-scenario and between-scenario parts (the law of total variance), and say which part diligence can reduce.
2. Apply Bayes' theorem to a single diagnostic signal such as a property condition assessment (PCA) flag, and show why base-rate neglect turns an 85%-sensitive test into a coin flip.
3. Build a confidence interval for a mean return from a short annual series, adjust it for serial correlation, and explain why ten years of annual CRE returns cannot tell you whether a manager has skill.
4. Compare normal, Student-t, and power-law tail probabilities with numbers, estimate a tail index with the Hill estimator, and state what kurtosis does and does not tell you.
5. Combine competing models by Bayesian model averaging and show that the averaged forecast has more variance than either model's own forecast.
6. Replace a sponsor's "inside view" of cost overrun and lease-up time with a reference-class forecast, and correct the reference class for survivorship.
7. Score a forecaster with the Brier score, decompose it into reliability, resolution, and uncertainty, and read a calibration table.
8. Elicit scenario probabilities, test them for coherence, and construct the Dutch book that an incoherent set allows.
9. Use CRRA expected utility to compute the certainty equivalent of a CRE bet and the commitment size it supports. Compute EVPI and EVSI for diligence and market studies, and use minimax regret when probabilities are not credible.

Chapter 1 developed expected value, break-even probabilities, and the price of diligence in a lemons market. Chapter 3 developed sequential Bayesian updating in odds form. This chapter does not repeat them. It supplies the inference, calibration, and decision-theoretic machinery that those chapters assumed.

---

## 20.1 Opening investment problem: the Thursday committee packet

You run the investment committee for a family investment vehicle with \$20.0 million of liquid capital. All facts below are [HYPOTHESIS], a constructed teaching case. Four items are in Thursday's packet.

**Item 1: the development LP commitment.** A sponsor is raising equity for a 240-unit garden multifamily development in a Sun Belt metro. The sponsor asks you for a \$5.0 million limited-partner commitment. The pro forma shows a hard-plus-soft budget of \$60.0 million, an expected cost of \$61.2 million after a 2% overrun "already in contingency", a 14-month lease-up, and a stabilized value of \$68.0 million. The pitch book says "6.8 million of profit, roughly 11% on cost".

**Item 2: the sponsor's record.** The sponsor presents ten years of annual fund-level returns averaging 5.6% with "only two down years", and a table of 40 probability statements its acquisitions team made over five years ("70% likely to hit the underwritten exit", and so on), with the outcomes. The sponsor says, "We are well calibrated."

**Item 3: the hotel and the PCA.** Separately, you have a select-service hotel under contract. Your base rate for a material undisclosed capital need in hotels of this age and brand is 15%. A property condition assessment costs \$20,000. Your analyst asks whether it is worth ordering, since "we are buying anyway".

**Item 4: the REIT hedge.** You hold a listed hotel REIT position as a liquidity sleeve. Your risk report says the REIT's monthly volatility is 6% and that a −20% month is "a 3.3-sigma event, about once in 190 years".

You also hold Treasury bills and can decline everything.

By §20.6 you will be able to say what each item is worth, which statements in the packet are wrong, and what information to buy before deciding.

---

## 20.2 Economic intuition

**A probability is a price you are willing to act on.** Every underwriting assumption is an implicit probability statement. "Lease-up in 14 months" means something like "the median lease-up is 14 months" or "I would bet even money on 14 months or better". Unless the statement is made explicit, it cannot be scored, and a forecaster who cannot be scored cannot improve. The first discipline of this chapter is to write the probability down.

**Most of the variance in a CRE outcome is between scenarios, not within them.** A stabilized value of \$68 million plus or minus a few million within a given market regime is a small risk. Whether the metro is in a strong or a weak regime when you sell is a large one. Diligence can narrow the within-regime spread: better rent comps, a firm GMP contract, a PCA. It cannot tell you which regime will prevail. Knowing which part of the variance you can buy down tells you which information to buy.

**Short samples tell you little about means and less about tails.** An annual return series of ten observations has a standard error of roughly a third of its standard deviation. If annual CRE returns have a standard deviation near 10%, the standard error of the mean is about 3 percentage points. That is larger than any plausible manager alpha. Appraisal smoothing makes the series autocorrelated, so the effective number of independent observations is smaller still. Tails are worse. The events that determine survival, such as a −20% month for a REIT or a 25% cost overrun for a development, are rare enough that ten years may contain none. A normal model fitted to that sample will understate them by one to three orders of magnitude.

**A single model is a bet that the model is right.** When two reasonable models disagree, picking the one that fits slightly better and discarding the other throws away the most important uncertainty you have: uncertainty about which world you are in. Averaging the models by their posterior probability keeps it.

**The inside view is biased; the outside view is dull and usually closer.** A sponsor estimating its own project's cost builds the estimate from the project's specifics, which is the inside view. Kahneman and Lovallo (1993) argued that such forecasts are systematically optimistic, and that the remedy is to start from the distribution of outcomes for similar projects, the reference class [FACT: ch20-S12, bibliographic check pending]. Flyvbjerg, Holm and Buhl (2002) found that actual costs on 258 transport infrastructure projects averaged 28% above estimates [FACT: ch20-S09, VERIFIED-SECONDARY]. Transport megaprojects are not garden apartments. The lesson that transfers is that the distribution of overruns is skewed and centered well above zero, and that a sponsor's own record is filtered by which projects it chooses to show.

**Calibration is checkable; confidence is not.** A forecaster is calibrated if, among all the times it said 70%, the event happened about 70% of the time. Calibration alone is cheap: a forecaster who always quotes the base rate is perfectly calibrated and useless. What you want is calibration plus **resolution**, meaning forecasts that move away from the base rate and are right when they do. The Brier score measures both, and its decomposition separates them.

**Decision theory turns probabilities into actions.** Expected value is the right criterion for small, repeated, diversifiable bets. A \$5 million commitment from a \$20 million vehicle is none of those. Expected utility with constant relative risk aversion (CRRA) gives a certainty equivalent that falls as the bet grows relative to wealth, and it tells you how much to commit, not only whether to commit. The value of information tells you how much to pay to learn before acting. When probabilities are not credible at all, minimax regret gives a defensible rule that does not require them.

---

## 20.3 Technical definitions

| Term | Definition |
|---|---|
| Law of total variance | $\operatorname{Var}(X) = E[\operatorname{Var}(X\mid S)] + \operatorname{Var}(E[X\mid S])$ for any partition $S$ (scenario, regime) |
| Base rate | The unconditional frequency of an event in a reference class, $P(H)$ before case-specific evidence |
| Sensitivity, false-positive rate | $P(E \mid H)$ and $P(E \mid \neg H)$ for a binary signal $E$ |
| Standard error of the mean | $s/\sqrt{n}$ for i.i.d. observations with sample s.d. $s$ |
| Effective sample size | The number of i.i.d. observations that would give the same variance of the mean; $n(1-\rho)/(1+\rho)$ for AR(1) with autocorrelation $\rho$ |
| Excess kurtosis | $E[(X-\mu)^4]/\sigma^4 - 3$; zero for the normal |
| Student-t, $\nu$ d.f. | Symmetric distribution with polynomial tails $P(T>t) \sim C t^{-\nu}$; variance $\nu/(\nu-2)$ for $\nu>2$; excess kurtosis $6/(\nu-4)$ for $\nu>4$ |
| Power-law (Pareto) tail | $P(X>x) = P(X>u)(x/u)^{-\alpha}$ for $x \ge u$; $\alpha$ is the tail index |
| Hill estimator | $\hat\alpha = k / \sum_{i=1}^{k} \ln(X_{(i)}/X_{(k+1)})$ from the $k$ largest order statistics |
| Bayesian model averaging (BMA) | Predictive distribution $\sum_k w_k\, p(y \mid M_k)$ with $w_k = P(M_k \mid \text{data})$ |
| Inside / outside view | Forecast built from case specifics / from the outcome distribution of a reference class |
| Brier score | $BS = \frac1N \sum_i (f_i - o_i)^2$ for probability forecasts $f_i$ and outcomes $o_i \in \{0,1\}$ |
| Reliability, resolution, uncertainty | The three terms of Murphy's (1973) decomposition $BS = REL - RES + UNC$ |
| Brier skill score | $BSS = 1 - BS/UNC$; skill relative to always forecasting the base rate |
| Coherence | Probabilities satisfy the axioms (non-negativity, additivity, normalization). An incoherent set admits a Dutch book |
| Dutch book | A set of bets, each acceptable at the stated probabilities, that loses money in every state |
| CRRA utility | $u(W) = W^{1-\gamma}/(1-\gamma)$ for $\gamma \neq 1$; $\ln W$ for $\gamma = 1$ |
| Certainty equivalent (CE) | The sure wealth $W_{CE}$ with $u(W_{CE}) = E[u(W)]$ |
| EVPI | Expected value of perfect information: $E_s[\max_a x_{a,s}] - \max_a E_s[x_{a,s}]$ |
| EVSI | Expected value of sample information: the gain in expected value from acting after an imperfect signal |
| Regret | $R_{a,s} = \max_{a'} x_{a',s} - x_{a,s}$ |
| Minimax regret | Choose the action whose largest regret across states is smallest (Savage, 1951) |

---

## 20.4 Equations and derivations

### 20.4.1 Expectation, variance, and the law of total variance

For a profit $\Pi = V - C$ (value at stabilization less cost),

$$E[\Pi] = E[V] - E[C], \qquad \operatorname{Var}(\Pi) = \operatorname{Var}(V) + \operatorname{Var}(C) - 2\rho_{VC}\,\sigma_V\sigma_C.$$

A positive correlation between value and cost *reduces* profit variance. Cost inflation tends to come with strong markets, so it partly hedges itself. A negative correlation, such as costs rising into a weakening market as in 2022–23, increases it.

When value depends on a regime $S$ (strong or weak market at sale), condition on it. Write $\mu_s = E[V \mid S=s]$ and $\sigma_s^2 = \operatorname{Var}(V\mid S=s)$. Then $E[V] = \sum_s p_s \mu_s$ and

$$\operatorname{Var}(V) = \underbrace{\sum_s p_s \sigma_s^2}_{\text{within}} + \underbrace{\sum_s p_s(\mu_s - E[V])^2}_{\text{between}}.$$

*Derivation.* $E[V^2] = \sum_s p_s E[V^2\mid s] = \sum_s p_s(\sigma_s^2 + \mu_s^2)$. Subtract $(E[V])^2 = (\sum p_s\mu_s)^2$ and regroup. The decomposition is exact and does not need normality. The mixture itself is not normal, and §20.4.4 returns to what that does to tail probabilities.

### 20.4.2 Bayes' theorem for one signal; base rates

For hypothesis $H$ and a binary signal $E$,

$$P(H\mid E) = \frac{P(E\mid H)P(H)}{P(E\mid H)P(H) + P(E\mid\neg H)(1-P(H))}, \qquad P(E) = P(E\mid H)P(H) + P(E\mid \neg H)(1-P(H)).$$

The predictive probability of the signal, $P(E)$, matters as much as the posterior. It is the weight used in the value-of-information calculation of §20.4.9. Chapter 3 (§3.4.9) treats a sequence of signals in odds form and the double-counting that follows from correlated signals. Here the issue is a single signal with a low base rate. When $P(H)$ is small, even a good test produces mostly false positives, because $P(E\mid\neg H)(1-P(H))$ dominates the denominator. **Base-rate neglect** is reading $P(E\mid H)$ as if it were $P(H\mid E)$.

### 20.4.3 Inference about a mean return

For $n$ i.i.d. returns with sample mean $\bar r$ and sample standard deviation $s$, the two-sided $1-\alpha$ confidence interval for the population mean $\mu$ is

$$\bar r \pm t_{1-\alpha/2,\,n-1}\, \frac{s}{\sqrt n}.$$

The Student-t critical value accounts for estimating $\sigma$ by $s$. With $n = 10$, $t_{0.975,9} = 2.262$, against 1.96 for a known $\sigma$.

**Serial correlation.** If returns follow an AR(1) with autocorrelation $\rho$,

$$\operatorname{Var}(\bar r) = \frac{\sigma^2}{n}\Big[1 + 2\sum_{k=1}^{n-1}\Big(1-\frac kn\Big)\rho^k\Big] \;\xrightarrow{\;n \text{ large}\;}\; \frac{\sigma^2}{n}\cdot\frac{1+\rho}{1-\rho}.$$

The effective sample size is therefore $n_{eff} \approx n(1-\rho)/(1+\rho)$. Appraisal-based CRE indices are smoothed (Chapter 2, §2.4 and the Geltner unsmoothing tools in `x_microstructure`), and their first-order autocorrelation is materially positive [HYPOTHESIS for the specific value used below; the sign is the established result]. Two further points matter:

* **Sample size needed.** To estimate a mean to within $\pm h$ at 95% confidence requires $n \approx (1.96\,\sigma/h)^2$ independent observations.
* **Manager skill.** To show a manager's alpha $a$ is nonzero at a $t$-statistic of 2 requires $n \approx (2\,\sigma_{TE}/a)^2$ years, where $\sigma_{TE}$ is tracking error. With $a = 2\%$ and $\sigma_{TE} = 6\%$, $n = 36$ years.

### 20.4.4 Fat tails: kurtosis, Student-t, and power laws

**Kurtosis** measures the weight of the tails *and* the peak relative to the shoulders. A positive excess kurtosis means that, for a fixed variance, more probability sits near the center and in the tails, and less in between. Kurtosis is a fourth-moment statistic. Its sample estimate is dominated by the largest few observations, and for $\nu \le 4$ in a Student-t it does not exist. A sample kurtosis of 3 from ten years of data is not evidence that the tails are thin.

**Variance-matched comparison.** To compare a normal and a Student-t fairly, give them the same variance. A standard $t_\nu$ has variance $\nu/(\nu-2)$. Scaling it by $s = \sqrt{(\nu-2)/\nu}$ gives unit variance. Then

$$P\big(X < -z\sigma\big) = F_{t_\nu}\!\left(-\frac{z}{\sqrt{(\nu-2)/\nu}}\right), \qquad \text{versus} \quad \Phi(-z) \text{ for the normal}.$$

At $z = 2$ the two are close. At $z = 4$ or 5 they differ by factors of tens to thousands (Example 20.4).

**The t tail is a power law.** For large $t$, the $t_\nu$ density is proportional to $|t|^{-(\nu+1)}$, so $P(T > t) \sim C_\nu t^{-\nu}$. The degrees of freedom are the tail index. A $t_3$ and a Pareto tail with $\alpha = 3$ have the same rate of decay. A normal tail decays like $e^{-z^2/2}$, faster than any power.

**Pareto tail and scale-free extrapolation.** Above a threshold $u$, $P(X>x) = P(X>u)(x/u)^{-\alpha}$. Doubling the threshold divides the exceedance probability by $2^\alpha$, whatever the starting point. Under a normal model, doubling a 3σ threshold to 6σ divides the probability by about 1.4 million. The Hill estimator is the maximum-likelihood estimator of $\alpha$ for exceedances that are exactly Pareto above $X_{(k+1)}$:

$$\hat\alpha_{k} = \frac{k}{\sum_{i=1}^{k}\ln\big(X_{(i)}/X_{(k+1)}\big)}, \qquad \operatorname{se}(\hat\alpha) \approx \hat\alpha/\sqrt k.$$

The choice of $k$ trades bias against variance. With $k = 11$, the standard error is about 30% of the estimate. A tail index is a range, not a number. Mandelbrot (1963) made the case for heavy-tailed price changes [ch20-S13, bibliographic check pending]; Gabaix (2009) surveys power laws in economics and finance [ch20-S14, bibliographic check pending].

### 20.4.5 Bayesian model averaging

Let models $M_1,\dots,M_K$ have prior probabilities $\pi_k$ and give likelihoods $L_k = p(\text{data}\mid M_k)$. The posterior weights are

$$w_k = \frac{\pi_k L_k}{\sum_j \pi_j L_j}.$$

The BMA predictive distribution for a future quantity $y$ is the mixture $\sum_k w_k\,p(y\mid M_k)$. By §20.4.1, its mean and variance are

$$\bar\mu = \sum_k w_k\mu_k, \qquad \sigma^2_{BMA} = \sum_k w_k\sigma_k^2 + \sum_k w_k(\mu_k-\bar\mu)^2.$$

The second term is model uncertainty. Selecting the best-fitting model sets it to zero by assumption. In a simple form usable on a desk, the "likelihood" can be the density each model assigned to the most recent observation, or to a short history of them. With two models, the posterior odds are the prior odds times the Bayes factor $L_1/L_2$, which is the same arithmetic as Chapter 3, applied to models instead of states. Hoeting et al. (1999) give the general treatment [ch20-S15, bibliographic check pending].

### 20.4.6 Reference-class forecasting and selection

Let $b$ be the reference-class mean outcome (for example the mean cost overrun), $x$ the inside-view forecast for this project, and $r \in [0,1]$ the correlation between past inside-view forecasts and outcomes. The regressive estimate is

$$\hat y = b + r\,(x - b).$$

If inside-view forecasts have no predictive power ($r = 0$), use the base rate. If they are perfect ($r = 1$), use the forecast. This is the same shrinkage as the normal–normal Bayesian posterior mean, where $r$ plays the role of the weight on the data. Kahneman and Tversky (1979) proposed this correction in this form [ch20-S12, bibliographic check pending].

**Selection.** A reference class assembled from completed projects excludes abandoned, recapitalized, and foreclosed projects. These are the projects with the largest overruns. If $n_c$ completed projects have mean overrun $m_c$ and $n_f$ failed projects have mean overrun $m_f$, the full-class mean is

$$b = \frac{n_c m_c + n_f m_f}{n_c + n_f},$$

which exceeds $m_c$ whenever $m_f > m_c$. Chapter 2 (§2.4.8) derived the same bias for comparable sales. Here it applies to the sponsor's track record.

### 20.4.7 The Brier score and Murphy's decomposition

Group $N$ forecasts into $K$ bins in which all forecasts equal $f_k$. Bin $k$ has $n_k$ forecasts, of which $o_k$ events occurred, with observed frequency $\bar o_k = o_k/n_k$. The overall frequency is $\bar o = \sum_k o_k/N$. Then

$$BS = \underbrace{\frac1N\sum_k n_k(f_k - \bar o_k)^2}_{REL} \;-\; \underbrace{\frac1N\sum_k n_k(\bar o_k - \bar o)^2}_{RES} \;+\; \underbrace{\bar o(1-\bar o)}_{UNC}.$$

*Derivation.* Within bin $k$, $\sum_{i\in k}(f_k - o_i)^2 = n_k(f_k-\bar o_k)^2 + \sum_{i\in k}(o_i-\bar o_k)^2$, because the cross term vanishes. For binary outcomes, $\sum_{i\in k}(o_i-\bar o_k)^2 = n_k\bar o_k(1-\bar o_k)$. Summing over bins and applying the law of total variance to the outcomes, $\frac1N\sum_k n_k\bar o_k(1-\bar o_k) = \bar o(1-\bar o) - \frac1N\sum_k n_k(\bar o_k-\bar o)^2$. Substituting gives the identity.

* **REL** (reliability, lower is better) measures miscalibration.
* **RES** (resolution, higher is better) measures how far the bin frequencies move from the base rate.
* **UNC** (uncertainty) depends only on the outcomes, not on the forecaster.

A forecaster who always quotes $\bar o$ has $REL = RES = 0$ and $BS = UNC$. The Brier skill score $BSS = 1 - BS/UNC$ is the fractional improvement over that forecaster. The Brier score is a *proper* scoring rule: a forecaster minimizes expected score by reporting its true belief (Brier, 1950; Murphy, 1973) [ch20-S10, ch20-S11]. The library function `sdesk.stats.brier_score(forecasts, outcomes)` computes $BS$ from raw lists. `x_decision.brier_decomposition(bins)` computes the three components.

### 20.4.8 Coherence and the Dutch book

Elicited probabilities must satisfy $P(A\cup B) = P(A) + P(B) - P(A\cap B)$, $0 \le P(A\cap B) \le \min(P(A),P(B))$, and, for a partition of scenarios, $\sum_s p_s = 1$. If a committee quotes $P(A\cup B) = q$ while its other quotes imply $q' = P(A)+P(B)-P(A\cap B) < q$, then the following trade earns $q - q'$ in every state. Sell the committee a \$1 claim on $A\cup B$ at $q$. Buy from it \$1 claims on $A$ and on $B$ at $P(A)$ and $P(B)$, and sell it a \$1 claim on $A\cap B$ at $P(A\cap B)$. The position pays $1_A + 1_B - 1_{A\cap B} - 1_{A\cup B} = 0$ in every state, and you collected $q - q'$ up front. de Finetti's coherence theorem says that a set of probability quotes admits no such book if and only if it obeys the axioms [ch20-S20, bibliographic check pending].

For scenario design, the practical rule is to elicit **marginals plus conditionals**, $P(A)$ and $P(B\mid A)$, and to derive the joint table. Do not elicit joints and unions separately and hope they agree.

### 20.4.9 Expected utility, certainty equivalent, and the value of information

**CRRA utility.** $u(W) = W^{1-\gamma}/(1-\gamma)$ has relative risk aversion $-W u''(W)/u'(W) = \gamma$, which is constant in wealth. The certainty equivalent of a wealth lottery is

$$W_{CE} = \Big(\sum_s p_s W_s^{1-\gamma}\Big)^{1/(1-\gamma)} \quad (\gamma\neq1), \qquad W_{CE} = \exp\Big(\sum_s p_s \ln W_s\Big) \quad (\gamma = 1).$$

The risk premium is $E[W] - W_{CE}$. For small bets, Pratt's (1964) approximation gives $E[W] - W_{CE} \approx \tfrac12\gamma\,\sigma_W^2/E[W]$ [ch20-S16, bibliographic check pending]. The approximation drops third and higher moments. It understates the premium for large, negatively skewed bets, which describes most levered CRE equity. A bet is acceptable if $W_{CE}$ with the bet exceeds the wealth from the riskless alternative. With $\gamma = 1$ (log utility), maximizing $E[u]$ is the Kelly criterion of Chapter 1 (§1.4.5). Chapter 21 develops sizing in full.

**EVPI.** With actions $a$, states $s$, payoffs $x_{a,s}$, and prior $p_s$,

$$EVPI = \sum_s p_s \max_a x_{a,s} \;-\; \max_a \sum_s p_s x_{a,s} \;\ge 0.$$

EVPI is an upper bound on what any information about $s$ is worth.

**EVSI.** For a signal $E$ with outcomes $e$,

$$EVSI = \sum_e P(e)\,\max_a \sum_s P(s\mid e)\,x_{a,s} \;-\; \max_a \sum_s p_s x_{a,s}.$$

$0 \le EVSI \le EVPI$. EVSI is positive only if some signal outcome changes the action. A study whose every possible result leaves you doing what you would have done anyway is worth zero, however accurate it is. The **expected net gain of sampling** is EVSI minus the cost of the study. Raiffa and Schlaifer (1961) is the standard source [ch20-S18, bibliographic check pending].

**Minimax regret.** Regret is $R_{a,s} = \max_{a'}x_{a',s} - x_{a,s}$. Savage's rule chooses $\arg\min_a \max_s R_{a,s}$ [ch20-S17, bibliographic check pending]. It uses no probabilities. It is not invariant to adding an irrelevant action, because a new action can change the column maxima. Use it as a check on an expected-value decision when the probabilities are elicited rather than estimated, not as a replacement for thought.

---

## 20.5 Worked examples

All inputs are [HYPOTHESIS] unless cited. All examples are reproduced in `tests/test_ch20_examples.py`. Money is in \$ millions unless stated.

### Example 20.1 — Expected profit and its variance on the development (Item 1)

**Given.** Stabilized value $V$ depends on the market regime at completion. Strong regime (probability 0.60): $E[V\mid S] = 72.0$, $\sigma = 4.0$. Weak regime (0.40): $E[V\mid W] = 62.0$, $\sigma = 5.0$. Cost $C$ has mean 61.2 (the sponsor's figure) and standard deviation 3.0. The correlation between $V$ and $C$ is +0.30.

**Find.** $E[V]$, $\operatorname{Var}(V)$ split into within and between, $E[\Pi]$, $\sigma_\Pi$, and a normal-approximation probability of loss.

**Solution.**

$E[V] = 0.60(72.0) + 0.40(62.0) = 43.2 + 24.8 = 68.0$.

Within $= 0.60(4.0^2) + 0.40(5.0^2) = 9.6 + 10.0 = 19.6$.

Between $= 0.60(72.0-68.0)^2 + 0.40(62.0-68.0)^2 = 9.6 + 14.4 = 24.0$.

$\operatorname{Var}(V) = 19.6 + 24.0 = 43.6$, so $\sigma_V = 6.603$.

$E[\Pi] = 68.0 - 61.2 = 6.8$.

$\operatorname{Var}(\Pi) = 43.6 + 3.0^2 - 2(0.30)(6.603)(3.0) = 43.6 + 9.0 - 11.885 = 40.715$, so $\sigma_\Pi = 6.381$.

Normal approximation: $P(\Pi<0) \approx \Phi(-6.8/6.381) = \Phi(-1.066) = 14.3\%$.

**Check.** Between-regime variance by the two-point formula: $p(1-p)(\mu_S-\mu_W)^2 = 0.24 \times 100 = 24.0$. ✓

**Decision consequence.** More than half (24.0 of 43.6) of the value variance comes from the regime, which no diligence on this project can reduce. That has two consequences. First, the information worth buying concerns the regime: supply pipeline, permits, and the absorption rate in the submarket. It is not a tighter appraisal of finishes. Second, the 14.3% loss probability is computed from a normal approximation to a two-regime mixture, which misstates the left tail (Example 20.4), and from the sponsor's cost mean, which Example 20.6 replaces. Treat 14.3% as a floor.

### Example 20.2 — Bayes and the PCA flag (Item 3)

**Given.** Base rate of a material undisclosed capital need, $P(B) = 0.15$. A PCA flags a material need with probability 0.85 when one exists (sensitivity) and 0.20 when none exists (false positives from conservative engineers and deferred-maintenance items that are not material).

**Find.** $P(\text{flag})$, $P(B\mid\text{flag})$, and $P(B\mid\text{no flag})$.

**Solution.**

$P(\text{flag}) = 0.85(0.15) + 0.20(0.85) = 0.1275 + 0.1700 = 0.2975$.

$P(B\mid\text{flag}) = 0.1275/0.2975 = 0.4286$.

$P(\text{no flag}) = 1 - 0.2975 = 0.7025$, and $P(B\mid\text{no flag}) = 0.15(0.15)/0.7025 = 0.0225/0.7025 = 0.0320$.

**Check.** Odds form (Chapter 3): prior odds $0.15/0.85 = 0.17647$; likelihood ratio $0.85/0.20 = 4.25$; posterior odds $0.75$; posterior $0.75/1.75 = 0.4286$. ✓ Also $0.2975(0.4286) + 0.7025(0.0320) = 0.15$, so the posteriors average back to the prior. ✓

**Decision consequence.** A flag moves the probability of a material problem from 15% to 43%, not to 85%. An analyst who reads the flag as "85% likely" will walk from deals that are more likely clean than not. The more useful output is the *no-flag* posterior: a clean report cuts the risk from 15% to 3.2%. Whether that is worth \$20,000 depends on whether either result changes the action, which is Example 20.10.

### Example 20.3 — What ten years of returns tell you (Item 2)

**Given.** The sponsor's annual fund-level total returns for ten years: 12%, 8%, −5%, 15%, 10%, 6%, −17%, 11%, 9%, 7%. Lag-1 autocorrelation in appraisal-based series of this kind: assume $\rho = 0.5$ [HYPOTHESIS].

**Find.** (a) The 95% confidence interval for the mean, treating the years as i.i.d. (b) The interval after the serial-correlation adjustment. (c) The years of i.i.d. data needed for a ±1% interval. (d) The years needed to show 2% alpha at $t = 2$ with 6% tracking error.

**Solution.**

(a) $\bar r = 56/10 = 5.60\%$. Sample s.d. $s = 9.548\%$. Standard error $= 9.548/\sqrt{10} = 3.019\%$. $t_{0.975,9} = 2.262$. Half-width $= 2.262 \times 3.019 = 6.830\%$. Interval: $[-1.23\%,\ 12.43\%]$. The geometric mean is 5.17%.

(b) $n_{eff} = 10(1-0.5)/(1+0.5) = 3.33$. Adjusted standard error $= 9.548/\sqrt{3.33} = 5.229\%$. Even with the optimistic normal critical value, the half-width is $1.96 \times 5.229 = 10.25\%$, giving $[-4.65\%,\ 15.85\%]$.

(c) $n = (1.96 \times 9.548/1)^2 = 350$ years.

(d) $n = (2 \times 6/2)^2 = 36$ years.

**Check.** Excel: `=AVERAGE(r)`, `=STDEV.S(r)`, `=T.INV.2T(0.05,9)` returns 2.2622, and `=CONFIDENCE.T(0.05, STDEV.S(r), 10)` returns 0.0683. ✓

**Decision consequence.** The record cannot distinguish a 0% mean from a 12% mean. It says nothing about whether the sponsor beat the market, because one market-wide down year (−17%) contributes more to the sample than any decision the sponsor made. "Only two down years" is a statement about ten draws from a distribution whose left tail, if the series is smoothed, is hidden. You must evaluate the sponsor on something with more observations: deal-level forecasts against outcomes (Example 20.7), cost and schedule against budget across all projects (Example 20.6), and the process. Do not treat a ten-year average as an estimate of skill.

### Example 20.4 — Fat tails: normal, Student-t, and a power law for the REIT sleeve (Item 4)

**Given.** Monthly REIT returns have mean 0 and standard deviation 6%. A −20% month is $z = 20/6 = 3.333$ standard deviations. Compare a normal model with Student-t models scaled to the same 6% volatility. Separately, the twelve largest monthly losses in a 360-month history are (in %): 31.7, 22.0, 20.1, 16.9, 15.2, 14.0, 13.1, 12.4, 11.8, 11.0, 10.4, 10.0 [HYPOTHESIS: an illustrative sample].

**Find.** (a) $P(r < -20\%)$ under each model and the expected count in 360 months. (b) The tail ratio at 2σ–5σ for $t_4$. (c) The Hill estimate of $\alpha$ using $k = 11$, and the Pareto-tail probability of months worse than −20%, −30%, and −40%.

**Solution.**

(a) Normal: $\Phi(-3.333) = 0.000429$, or one month in 2,331 (194 years). Expected count in 360 months: 0.15.

For $t_\nu$ with unit variance, the threshold in $t$ units is $3.333/\sqrt{(\nu-2)/\nu}$:

| Model | Scale (monthly) | $t$-threshold | $P(r<-20\%)$ | Count in 360 months | Ratio to normal | Excess kurtosis |
|---|---|---|---|---|---|---|
| Normal | 6.00% | 3.333 | 0.000429 | 0.15 | 1.0 | 0 |
| $t_8$ | 5.196% | 3.849 | 0.002442 | 0.88 | 5.7 | 1.5 |
| $t_5$ | 4.648% | 4.303 | 0.003846 | 1.38 | 9.0 | 6 |
| $t_4$ | 4.243% | 4.714 | 0.004606 | 1.66 | 10.7 | ∞ |
| $t_3$ | 3.464% | 5.774 | 0.005165 | 1.86 | 12.0 | ∞ |

(b) Variance-matched $t_4$ against the normal:

| Threshold | Normal | $t_4$ | Ratio |
|---|---|---|---|
| 2σ | 0.02275 | 0.02371 | 1.04 |
| 3σ | 0.001350 | 0.006618 | 4.90 |
| 4σ | 0.0000317 | 0.002406 | 76.0 |
| 5σ | 0.000000287 | 0.001055 | 3,682 |

(c) Threshold $u = X_{(12)} = 10.0\%$. $\sum_{i=1}^{11}\ln(X_{(i)}/10.0) = 4.7054$, so $\hat\alpha = 11/4.7054 = 2.338$, with standard error roughly $2.338/\sqrt{11} = 0.70$. Empirical $P(\text{loss} > 10\%) = 11/360 = 0.03056$.

* $P(\text{loss}>20\%) = 0.03056 \times 2^{-2.338} = 0.00604$, about 2.2 months in 360. The sample has three.
* $P(\text{loss}>30\%) = 0.03056 \times 3^{-2.338} = 0.00234$. The normal model gives $\Phi(-5) = 2.9\times10^{-7}$.
* $P(\text{loss}>40\%) = 0.03056 \times 4^{-2.338} = 0.00120$.

Doubling the loss threshold divides the probability by $2^{2.338} = 5.06$.

**Check.** At 2σ the variance-matched $t_4$ and the normal nearly agree (ratio 1.04). That is the region where the bulk of a short sample lives, which is why a short sample cannot distinguish them. The $t$ CDF is checked in the tests against the closed form for $\nu=2$, $F(t) = \tfrac12 + t/(2\sqrt{2+t^2})$, and against numerical integration of the density.

**Decision consequence.** The risk report's "once in 190 years" is a property of the normal model, not of REITs. Under the $t_3$–$t_5$ models and the Hill tail, a −20% month is a once-in-14-to-22-years event, and a 30-year history should contain one to two. This changes sizing (Chapter 21). A liquidity sleeve that must be sold at the bottom of such a month to meet a capital call is not a liquidity sleeve. The excess-kurtosis column also shows why kurtosis is a poor summary. The $t_4$ and $t_3$ have *undefined* kurtosis and only modestly fatter 3.3σ tails than the $t_5$. What matters for decisions is the tail probability at the loss that hurts you, estimated from tail data, with an honest standard error.

### Example 20.5 — Bayesian model averaging for rent growth

**Given.** Two models for next-year rent growth $g$ in the development's submarket. $M_1$ (normal cycle): $g \sim N(3.0\%,\ 2.0\%)$. $M_2$ (supply overhang): $g \sim N(-2.0\%,\ 3.0\%)$. Prior weights 0.70 and 0.30. This year's observed growth is 0.0%, and each model would have predicted this year's growth with the same distribution [HYPOTHESIS].

**Find.** The posterior model weights, the BMA predictive mean and standard deviation, and $P(g<0)$ and $P(g<-3\%)$ under BMA and under $M_1$ alone.

**Solution.**

Likelihoods: $L_1 = \phi(0; 3, 2) = 0.06476$, $L_2 = \phi(0;-2,3) = 0.10648$. Bayes factor $L_1/L_2 = 0.608$.

$w_1 = 0.70(0.06476)/[0.70(0.06476) + 0.30(0.10648)] = 0.04533/0.07728 = 0.5866$, and $w_2 = 0.4134$.

$\bar\mu = 0.5866(3.0) + 0.4134(-2.0) = 0.933\%$.

Within $= 0.5866(4) + 0.4134(9) = 6.067$. Between $= 0.5866(3.0-0.933)^2 + 0.4134(-2.0-0.933)^2 = 6.062$. Total variance $= 12.129$, so $\sigma_{BMA} = 3.483\%$.

| Quantity | $M_1$ alone | BMA mixture | Normal with BMA moments |
|---|---|---|---|
| Mean | 3.00% | 0.93% | 0.93% |
| S.d. | 2.00% | 3.48% | 3.48% |
| $P(g<0)$ | 6.7% | 34.8% | 39.4% |
| $P(g<-3\%)$ | 0.13% | 15.4% | 12.9% |

**Check.** Mixture probability $P(g<0) = 0.5866\,\Phi(-1.5) + 0.4134\,\Phi(0.667) = 0.5866(0.0668) + 0.4134(0.7475) = 0.0392 + 0.3090 = 0.348$. ✓

**Decision consequence.** One flat year moves the supply-overhang model from 30% to 41% weight, but $M_1$ remains the "best" single model. An analyst who selects it underwrites 3% growth with a 0.13% chance of a −3% year. The BMA forecast puts that chance at 15%. If a −3% year breaches the construction loan's debt-yield test at conversion, that is the difference between ignoring the covenant and pricing it. The between-model variance (6.06) is as large as the within-model variance (6.07). Half of the honest uncertainty is about which model is right. Note also that the normal approximation with BMA moments misstates both tails: the mixture is bimodal and skewed.

### Example 20.6 — Reference-class forecast for cost overrun and lease-up (Item 1, continued)

**Given.** Sponsor's inside view: cost overrun 2.0% on the \$60.0 million budget, lease-up 14 months. Your firm's reference class for garden multifamily developments by mid-sized sponsors [HYPOTHESIS: an illustrative internal database]: 30 projects started. Twenty-five were completed, with a mean overrun of 9.0% (s.d. 8.0%). Five were abandoned or recapitalized, with an estimated mean overrun of 30%. Mean lease-up in the reference class is 19 months. Past correlations between inside-view forecasts and outcomes: $r = 0.3$ for cost and $r = 0.4$ for lease-up. Each month of lease-up beyond plan costs \$0.25 million of net negative carry (construction-loan interest and operating deficit). Stabilized value as in Example 20.1.

**Find.** The full reference-class overrun, the adjusted cost and lease-up, the adjusted expected profit, and the normal-approximation probability of loss using Example 20.1's $\sigma_\Pi$.

**Solution.**

Completed-only class: $9.0 + 0.3(2.0 - 9.0) = 6.9\%$.

Full class mean: $b = (25 \times 9.0 + 5 \times 30.0)/30 = (225 + 150)/30 = 12.5\%$.

Adjusted overrun: $12.5 + 0.3(2.0 - 12.5) = 12.5 - 3.15 = 9.35\%$. Adjusted cost $= 60.0 \times 1.0935 = 65.61$.

Adjusted lease-up: $19 + 0.4(14 - 19) = 17$ months. Extra carry $= 3 \times 0.25 = 0.75$.

All-in expected cost $= 65.61 + 0.75 = 66.36$. Expected profit $= 68.0 - 66.36 = 1.64$, against the sponsor's 6.8.

$P(\Pi < 0) \approx \Phi(-1.64/6.381) = \Phi(-0.257) = 39.9\%$.

**Check.** Selection bias in the reference class: $12.5 - 9.0 = 3.5$ percentage points of overrun, or \$2.1 million on a \$60 million budget. That one correction equals 31% of the sponsor's projected profit.

**Decision consequence.** The pitch book's \$6.8 million profit (11% on cost) becomes \$1.6 million (2.5% on cost), with a loss probability near 40%. That is not a development return. The adjustment does not assume the sponsor is dishonest. It assumes the sponsor is like other sponsors, which is the base rate for this question. The decision is to decline at these terms, or to restructure: a fixed-price GMP contract that moves cost risk to the contractor, a sponsor completion guarantee, or a preferred return that subordinates the sponsor's promote to the reference-class outcome. The sponsor's track-record presentation also needs a direct question: *how many projects did you start, and what happened to the ones not shown?*

### Example 20.7 — Scoring the sponsor's calibration (Item 2, continued)

**Given.** The sponsor's acquisitions team made 40 probability statements of the form "probability that the deal meets its underwritten exit". Grouped by stated probability:

| Stated $f_k$ | Count $n_k$ | Events $o_k$ | Observed $\bar o_k$ |
|---|---|---|---|
| 0.10 | 8 | 1 | 0.125 |
| 0.30 | 10 | 4 | 0.400 |
| 0.50 | 8 | 5 | 0.625 |
| 0.70 | 8 | 4 | 0.500 |
| 0.90 | 6 | 4 | 0.667 |
| Total | 40 | 18 | 0.450 |

**Find.** $BS$ using `sdesk.stats.brier_score`, its decomposition, and the skill score.

**Solution.**

Expand the bins into 40 forecasts and 40 outcomes, then `stats.brier_score(f, o)` $= 0.2340$.

REL $= \frac1{40}[8(0.1-0.125)^2 + 10(0.3-0.4)^2 + 8(0.5-0.625)^2 + 8(0.7-0.5)^2 + 6(0.9-0.667)^2]$
$= \frac1{40}[0.005 + 0.100 + 0.125 + 0.320 + 0.327] = 0.877/40 = 0.02192$.

RES $= \frac1{40}[8(0.125-0.45)^2 + 10(0.4-0.45)^2 + 8(0.625-0.45)^2 + 8(0.5-0.45)^2 + 6(0.667-0.45)^2]$
$= \frac1{40}[0.845 + 0.025 + 0.245 + 0.020 + 0.282] = 1.417/40 = 0.03542$.

UNC $= 0.45 \times 0.55 = 0.2475$.

$BS = 0.02192 - 0.03542 + 0.2475 = 0.2340$. ✓ $BSS = 1 - 0.2340/0.2475 = 5.5\%$.

**Check.** The identity holds exactly because every forecast in a bin is identical. With continuous forecasts binned by range, a within-bin term appears and the identity is approximate.

**Decision consequence.** The team has some resolution: deals called at 10% mostly failed. But its high-confidence calls are badly overconfident. At 70% and 90% it hit 50% and 67%, and those two bins contribute 0.647 of the 0.877 reliability total. Its skill over always quoting 45% is 5.5%. The claim "we are well calibrated" is false at the end of the scale that matters for an LP, because the sponsor's 90% deals are the ones it asks you to fund. Two cautions temper the verdict. Bins of 6 to 10 forecasts have binomial standard errors of 15 to 20 percentage points, so the 0.90 bin's shortfall is suggestive rather than proven. And the record is only as honest as its selection: ask whether all forecasts were logged *before* outcomes were known (Chapter 25's decision journal).

### Example 20.8 — Eliciting scenario probabilities and checking coherence

**Given.** For a stabilized hotel hold, the committee elicits: $P(R) = 0.30$ (U.S. recession within two years), $P(C) = 0.45$ (exit cap rates up 50 bp or more), $P(R\cap C) = 0.10$, and, asked separately, $P(R\cup C) = 0.70$. Equity outcomes (\$ millions) by cell: $R\cap C$: −12.0; $R\cap\neg C$: −2.5; $\neg R\cap C$: +1.0; $\neg R\cap\neg C$: +4.0.

**Find.** (a) Whether the quotes are coherent, and the Dutch book if not. (b) The coherent joint table from $P(R)$, $P(C)$, $P(R\cap C)$, and the implied conditionals. (c) Expected equity outcome under the elicited dependence, under independence, and under positive dependence $P(C\mid R) = 0.60$.

**Solution.**

(a) Coherent union: $0.30 + 0.45 - 0.10 = 0.65 \neq 0.70$. Incoherent. The book: sell a \$1 claim on $R\cup C$ at 0.70. Buy \$1 claims on $R$ (0.30) and $C$ (0.45). Sell a \$1 claim on $R\cap C$ (0.10). Net premium received $= 0.70 + 0.10 - 0.30 - 0.45 = 0.05$. The payoffs net to $1_R + 1_C - 1_{R\cap C} - 1_{R\cup C} = 0$ in all four states. A sure \$0.05 per \$1.

(b) Joint table: $R\cap C = 0.10$; $R\cap\neg C = 0.20$; $\neg R\cap C = 0.35$; $\neg R\cap\neg C = 0.35$. $P(C\mid R) = 0.10/0.30 = 0.333$ and $P(C\mid\neg R) = 0.35/0.70 = 0.500$. The committee believes cap rates are *less* likely to rise in a recession, which is the falling-rates view.

(c)

| Dependence | $p(R\cap C)$ | $p(R\cap\neg C)$ | $p(\neg R\cap C)$ | $p(\neg R\cap\neg C)$ | Expected outcome |
|---|---|---|---|---|---|
| Elicited ($P(C\mid R)=0.33$) | 0.10 | 0.20 | 0.35 | 0.35 | +0.050 |
| Independent ($P(C\mid R)=0.45$) | 0.135 | 0.165 | 0.315 | 0.385 | −0.178 |
| Positive ($P(C\mid R)=0.60$) | 0.18 | 0.12 | 0.27 | 0.43 | −0.470 |

Elicited: $0.10(-12) + 0.20(-2.5) + 0.35(1) + 0.35(4) = -1.2 - 0.5 + 0.35 + 1.4 = 0.05$.

**Check.** Every table holds the marginals fixed: row sums give $P(R) = 0.30$ and column sums give $P(C) = 0.45$.

**Decision consequence.** The incoherence is not a technicality. It means the committee's probabilities were produced by different mental procedures for different questions, and at least one is wrong. The more important finding is in (c). With the marginals fixed, the sign of the expected outcome depends on the *dependence* between recession and cap-rate rise. That is the 2022 question: a recession accompanied by rising rates (stagflation) is the joint state that destroys this hold. The committee's falling-rates belief is the whole case for the deal, and it should be argued explicitly, not left implicit in a single joint number.

### Example 20.9 — CRRA expected utility and the certainty equivalent of the LP commitment

**Given.** Wealth \$20.0 million. Riskless alternative: Treasury bills returning 12% cumulatively over the three-year hold. The development commitment of \$5.0 million returns equity of 9.0 (probability 0.50), 5.5 (0.30), or 0.0 (0.20) at year 3. The other \$15.0 million earns the bill rate. Ignore taxes and interim distributions.

**Find.** Terminal wealth by state, the certainty equivalent for $\gamma = 1, 3, 5$, the deal's certainty equivalent at $\gamma = 3$, the Pratt approximation, and the commitment that maximizes the CE for each $\gamma$, holding the deal's payoff multiples fixed.

**Solution.**

Bills on the rest: $15.0 \times 1.12 = 16.8$. Terminal wealth: $16.8 + \{9.0, 5.5, 0.0\} = \{25.8,\ 22.3,\ 16.8\}$. Riskless alternative: $20.0 \times 1.12 = 22.4$.

$E[W] = 0.5(25.8) + 0.3(22.3) + 0.2(16.8) = 12.90 + 6.69 + 3.36 = 22.95$. $\sigma_W = 3.428$.

For $\gamma = 3$: $E[W^{-2}] = 0.5(25.8^{-2}) + 0.3(22.3^{-2}) + 0.2(16.8^{-2}) = 0.000751 + 0.000603 + 0.000709 = 0.002063$, so $W_{CE} = 0.002063^{-1/2} = 22.016$.

| $\gamma$ | $W_{CE}$ | vs. bills (22.4) | Risk premium $E[W]-W_{CE}$ | Pratt $\tfrac12\gamma\sigma^2/E[W]$ | Optimal commitment | Max acceptable commitment |
|---|---|---|---|---|---|---|
| 1 | 22.665 | +0.265 | 0.285 | 0.256 | 4.65 | 8.81 |
| 3 | 22.016 | −0.384 | 0.934 | 0.768 | 1.62 | 3.16 |
| 5 | 21.307 | −1.093 | 1.643 | 1.280 | 0.98 | 1.92 |

At $\gamma = 3$, the deal's own certainty equivalent is $22.016 - 16.8 = 5.216$, against its expected value of 6.15 and the bills' 5.6.

The optimal commitment $x$ maximizes the CE of $W(x) = 1.12(20 - x) + x\,m_s$ with multiples $m_s = \{1.8, 1.1, 0\}$ (grid search in \$10,000 steps).

**Check.** Expected multiple $0.5(1.8) + 0.3(1.1) = 1.23 > 1.12$, so a risk-neutral investor commits everything. Every finite $\gamma$ commits less. Log utility ($\gamma = 1$) is Kelly sizing (Chapter 1), and the \$4.65 million optimum is the Kelly fraction of 23% of wealth for this payoff profile.

**Decision consequence.** At moderate risk aversion ($\gamma = 3$), the \$5.0 million commitment is worse than bills, even though the deal has positive expected excess return of \$0.55 million. The right commitment is about \$1.6 million, and anything above \$3.2 million destroys certainty-equivalent wealth. The 20% chance of a total loss of a quarter of liquid wealth is what makes the size wrong. The Pratt approximation understates the premium by 18% (0.768 versus 0.934), because it ignores the negative skew of a payoff with a zero state. These figures use the sponsor's probabilities. With Example 20.6's reference-class adjustment, the zero state becomes more likely and the commitment shrinks further.

### Example 20.10 — EVPI and EVSI: is the \$20,000 PCA worth ordering? (Item 3)

**Given.** If the hotel has no material capital need (prior 0.85), buying at the contract price has NPV +0.60. If it has one (0.15), NPV is −2.40. Not buying (terminating in the diligence period) has NPV 0. PCA characteristics as in Example 20.2. PCA cost 0.020.

**Find.** The prior decision, EVPI, the decision after each PCA result, EVSI, and the expected net gain of ordering the PCA.

**Solution.**

Prior: $EV(\text{buy}) = 0.85(0.60) + 0.15(-2.40) = 0.51 - 0.36 = 0.15 > 0$. Buy.

EVPI: with perfect information you buy only in the clean state, so $E[\max] = 0.85(0.60) + 0.15(0) = 0.51$, and $EVPI = 0.51 - 0.15 = 0.36$.

After a flag (probability 0.2975, $P(B\mid\text{flag}) = 0.4286$): $EV(\text{buy}) = 0.5714(0.60) + 0.4286(-2.40) = 0.3429 - 1.0286 = -0.686$. Do not buy (or renegotiate).

After no flag (probability 0.7025, $P(B\mid\text{no flag}) = 0.0320$): $EV(\text{buy}) = 0.9680(0.60) + 0.0320(-2.40) = 0.5808 - 0.0769 = 0.504$. Buy.

EV with PCA $= 0.2975(0) + 0.7025(0.504) = 0.354$. $EVSI = 0.354 - 0.15 = 0.204$. Net gain $= 0.204 - 0.020 = 0.184$.

**Check.** $0 \le EVSI = 0.204 \le EVPI = 0.36$. ✓ The PCA captures 57% of the value of perfect information.

**Decision consequence.** "We are buying anyway" is exactly wrong. The PCA is valuable *because* a flag changes the action from buy to walk (or to a price cut). If the analyst would buy regardless of the report, the PCA's decision value is zero, and the \$20,000 buys only comfort. The calculation also shows what makes a study worth more. A lower false-positive rate raises EVSI, and so does a larger loss in the bad state. A cheaper study does not raise EVSI; it only lowers the cost side. Chapter 1, Example 1.7 showed that diligence can make a market exist. This example prices diligence for a single decision.

### Example 20.11 — Minimax regret when probabilities are not credible

**Given.** A land parcel for a future industrial development. Actions: $A_1$ buy now at the full price; $A_2$ pay \$0.5 million for a 12-month purchase option; $A_3$ pass. States over the option period: boom, base, bust. Payoffs (\$ millions):

| Action | Boom | Base | Bust |
|---|---|---|---|
| $A_1$ buy now | +8.0 | +3.0 | −7.0 |
| $A_2$ option | +6.5 | +2.0 | −0.5 |
| $A_3$ pass | 0.0 | 0.0 | 0.0 |

**Find.** The regret table, the minimax-regret action, the maximin and maximax actions, expected values at probabilities (0.40, 0.45, 0.15), and the bust probability that equates $A_1$ and $A_2$ (holding boom:base at 40:45).

**Solution.**

Column maxima: 8.0, 3.0, 0.0.

| Regret | Boom | Base | Bust | Max regret |
|---|---|---|---|---|
| $A_1$ | 0.0 | 0.0 | 7.0 | 7.0 |
| $A_2$ | 1.5 | 1.0 | 0.5 | **1.5** |
| $A_3$ | 8.0 | 3.0 | 0.0 | 8.0 |

Minimax regret: $A_2$. Maximin (best worst case): $A_3$ (0 versus −0.5 and −7.0). Maximax: $A_1$.

Expected values: $A_1 = 3.2 + 1.35 - 1.05 = 3.50$; $A_2 = 2.6 + 0.9 - 0.075 = 3.425$; $A_3 = 0$.

Break-even: $A_1 - A_2$ pays $(1.5, 1.0, -6.5)$. Holding boom:base at 40:45, $\bar G = (40 \times 1.5 + 45 \times 1.0)/85 = 1.235$, so $q^* = 1.235/(1.235 + 6.5) = 16.0\%$.

**Check.** At $q = 0.15$, $A_1$ beats $A_2$ by 0.075, consistent with $q < q^* = 0.160$. ✓

**Decision consequence.** Expected value favors buying now by \$75,000, but only if the bust probability is below 16.0%, and your estimate is 15%. That is the straddle Chapter 1 warned about. Minimax regret picks the option, whose worst regret is \$1.5 million against \$7.0 million for buying now. When the EV ranking depends on a probability you cannot defend to within a percentage point, and the regret rule points clearly to one action, take the robust action. Here that is paying \$0.5 million for the right to wait (Chapter 3, §3.4.6).

---

## 20.6 CRE application: rewriting the committee memo

Return to the Thursday packet. The analysis above converts four marketing claims into decisions.

| Item | Packet claim | Analysis | Decision |
|---|---|---|---|
| 1. Development LP | \$6.8m profit, 11% on cost | Reference class: \$1.6m expected profit, ~40% loss probability (Ex 20.6); regime is the dominant variance (Ex 20.1); CE at $\gamma=3$ is below bills even on sponsor numbers (Ex 20.9) | Decline at \$5.0m on these terms. Re-engage only with a GMP contract and a completion guarantee, and then at no more than about \$1.5m |
| 2. Track record | "5.6% average, two down years"; "well calibrated" | CI for the mean spans −1% to 12% before the smoothing adjustment (Ex 20.3); Brier skill 5.5%, overconfident at 70–90% (Ex 20.7) | Request the full project list, including abandoned projects, and the forecast log with timestamps |
| 3. Hotel PCA | "We are buying anyway" | EVSI \$204k against a \$20k cost; a flag reverses the decision (Ex 20.2, 20.10) | Order the PCA, and pre-commit to walking or renegotiating on a flag |
| 4. REIT sleeve | −20% month "once in 190 years" | Fat-tailed models: once in 14–22 years; Hill estimate implies about two in 30 years (Ex 20.4) | Resize the sleeve so that a −20% month does not force a sale; do not count it as liquidity at full value |

Two cross-cutting points. First, three of the four errors are failures to **condition on the right reference class**: the sponsor's completed projects only, a normal distribution fitted to calm years, a PCA flag read as its sensitivity. Second, every recommendation comes with **information to buy before acting**, priced by its value to the decision. The committee's job is not to forecast the metro. It is to decide what to learn and how much to commit while ignorant.

---

## 20.7 When the relationships fail

1. **Reference classes can be wrong, not just incomplete.** A 2010–2019 development reference class did not contain the 2021–2023 cost-inflation and rate shock. The outside view is only as good as the analogy. Use several reference classes and report the spread between them.
2. **Calibration is measurable only with many forecasts.** Ten deals per year gives a usable calibration table after five to ten years. For rare events such as recessions, a lifetime of quarterly forecasts contains a handful of positives (§20.8). Scores on small samples are noise.
3. **Proper scoring rules can be gamed by choosing questions.** A forecaster who answers only easy questions looks skilled. Fix the question set in advance.
4. **BMA assumes the true model is among the candidates.** If every model omits the mechanism that matters, such as a liquidity spiral, averaging them averages wrong answers. Model weights also move quickly on little data. In Example 20.5 one observation moved a weight by 11 points.
5. **Tail estimates are unstable.** The Hill estimator depends on the choice of $k$, and its standard error is large. Regime changes alter the tail. Use tail estimates to reject thin-tailed assumptions, not to fine-tune a 99.9% quantile.
6. **Utility functions are not observed.** A family office's $\gamma$ is a negotiated policy choice, not a fact. Report decisions for a range of $\gamma$, as in Example 20.9. Also, CRRA treats wealth as fungible. Liquidity constraints, capital calls, and covenants can make a loss far more costly than any smooth utility function implies.
7. **Value of information assumes you will act on it.** EVSI is zero for an organization that will not walk after a bad report. Commit to the decision rule before ordering the study.
8. **Minimax regret is not invariant.** Adding an irrelevant action changes the column maxima and can change the choice. Use it as a robustness check, not as a mechanical rule.
9. **Independence assumptions fail exactly in the tails.** Example 20.8 showed that the sign of a deal's expected value can depend on the joint behavior of two risks. In crises, correlations rise. A scenario tree with independent branches is a statement that they will not.

---

## 20.8 Historical episode: probability forecasts of recession, 2007–2008

### Date and environment

The U.S. expansion that began in November 2001 peaked in December 2007, according to the NBER's Business Cycle Dating Committee. The committee announced that peak on 1 December 2008, almost a year later [FACT: ch04-S01, VERIFIED-SECONDARY]. Chapter 4 (§4.9) documents the real-time data revisions of 2008. This episode asks a narrower question: **how good were published probability forecasts of a downturn, and how would we know?**

### What was published at the time

The Federal Reserve Bank of Philadelphia's Survey of Professional Forecasters (SPF) asks each panelist, every quarter, for the probability that real GDP will decline (quarter over quarter) in the current quarter and in each of the next four quarters. The SPF does not ask directly about "recession". The mean probability for the quarter after the survey quarter is published as the **anxious index** [FACT: ch20-S01, ch20-S02, VERIFIED-SECONDARY]. The Philadelphia Fed notes that the index often rises just before recessions begin. For example, it was 32% in the 2001:Q1 survey [FACT: ch20-S01, VERIFIED-SECONDARY]. The NBER later dated the 2001 peak to March 2001 (Chapter 4, ch04-S02).

The anxious-index readings for the surveys of 2007:Q4 through 2008:Q3, which are the readings that matter for the "before 2008" question, are *(verification pending)*. They must be read from the Philadelphia Fed's RECESS data file, which could not be opened in this authoring environment. This section does not state or use them.

What has been verified is the fourth-quarter 2008 survey, released on 17 November 2008, two weeks before the NBER announcement. Fifty-one panelists responded. They were unanimous that the economy had entered or would soon enter a recession. They dated its start to April 2008 and expected it to last 14 months. They projected real GDP declining at annual rates of 2.9% in 2008:Q4 and 1.1% in 2009:Q1 [FACT: ch20-S03, VERIFIED-SECONDARY]. Search-excerpt summaries of the same release report the mean probability of decline at 90% for the current quarter (up from 47% in the prior survey) and 75% for 2009:Q1 (up from 33%) [FACT: ch20-S03, VERIFIED-SECONDARY; to be checked against the release table].

### Documented evaluations

* **Rudebusch and Williams (2009)** compared SPF probability forecasts of GDP declines with a simple probit model based on the yield spread, estimated in real time. At horizons of three and four quarters, the yield-spread model was significantly more accurate. At shorter horizons the two were statistically indistinguishable. The authors called it a puzzle that forecasters appeared to put too little weight on the yield spread [FACT: ch20-S04, VERIFIED-SECONDARY].
* **Lahiri and Wang (2013)** evaluated SPF probability forecasts through 2011:Q1, using calibration, resolution, ROC curves, and Brier-score decompositions. Only the forecasts for the current quarter and the next two quarters showed significant skill on all measures. Even those showed excess variability and a lack of calibration [FACT: ch20-S05, VERIFIED-SECONDARY].
* **Potter (2011)**, writing about the New York Fed's own staff forecasts, reported that although staff saw the risks as to the downside throughout 2007–08, a recession as deep as the one that occurred did not receive more than 15% weight until fall 2008 [FACT: ch20-S06, VERIFIED-SECONDARY].

### Interpretations

**Interpretation 1: the forecasters were miscalibrated about rare events.** Declines in real GDP are rare. A forecaster who quotes low probabilities in most quarters will have a good average Brier score, because most quarters are not declines. That score hides poor performance in the quarters that matter. The Murphy decomposition shows the mechanism: when the base rate is low, the uncertainty term is small, and a forecaster can earn a "good" score with almost no resolution [INFERENCE from §20.4.7].

**Interpretation 2: the information was not in the data available at the time.** The real-time data understated the weakness of 2008 (Chapter 4, §4.9), and a probability forecast cannot be better than its inputs. On this view the forecasters were reasonably calibrated relative to the information they had [ALTERNATIVE INFERENCE].

**Interpretation 3: herding and loss functions.** Professional forecasters may face asymmetric reputational costs. Calling a recession that does not come may be costlier than missing one that everyone missed [HYPOTHESIS; not tested here].

The Rudebusch–Williams result weighs against a pure version of Interpretation 2. A public variable, the yield spread, carried information at longer horizons that the survey did not reflect.

### A second, cleaner illustration: one binary event

On 8 November 2016, FiveThirtyEight's poll-based model gave Donald Trump a 28.6% probability of winning the presidency [FACT: ch20-S07, VERIFIED-SECONDARY]. Betting exchanges on election day priced him lower. Reuters reported about 20% on Betfair and about 22% on PredictIt during the day [FACT: ch20-S08, VERIFIED-SECONDARY; intraday timing not specified]. Trump won.

Brier scores on this single event: FiveThirtyEight $(1-0.286)^2 = 0.510$; Betfair $(1-0.20)^2 = 0.640$. A forecaster who said 50% would have scored 0.25 and "beaten" both. The likelihood ratio of the outcome under the two forecasts is $0.286/0.20 = 1.43$. If a skeptic gave the model and the market equal prior weight, this one result would move the weights only to 59:41 (§20.4.5). **One outcome cannot establish calibration.** The widespread post-election claim that the forecasts "failed" confuses a 29% event occurring with a forecast being wrong.

### What the episode establishes and what it does not

It establishes that probability forecasts of macroeconomic downturns are published, can be scored, and have been scored. It establishes that formal evaluations found limited skill beyond two quarters and a tendency to under-weight at least one public signal [FACT, from the cited evaluations]. It establishes, through the 2016 case, that a single outcome carries little evidence about a forecaster's calibration.

It does **not** establish what the SPF's probability was at any specific date before the 2008 downturn; those readings are pending verification. It does not establish that any individual forecaster was miscalibrated. Nor does it show that a yield-spread model will outperform in future cycles. An extended yield-curve inversion in 2022–24 *(dates and depth: verification pending)* was not followed by an NBER-announced peak as of the time of writing (Chapter 4, ch04-S03: no peak after February 2020 found). If that holds, it is a live counterexample to over-trusting that model [INFERENCE].

### CRE connection

The underwriting equivalent of the anxious index is the probability, written in the memo, that the downside case occurs. Very few CRE firms log those probabilities and score them. Without that record, an organization cannot learn whether its 15% recession case was calibrated, and every post-mortem becomes a debate about outcomes (Chapter 1, §1.2).

---

## 20.9 Decision exercise: the calibration audit and the commitment

You are given (in `problems/questions/ch20_problems.md`, Problem 20.10) a sponsor's track record of six completed developments, all within 3% of budget, and a request for a \$4.0 million commitment from your \$20.0 million vehicle. You learn informally that four further projects started by the sponsor were transferred to lenders or recapitalized and are not in the deck.

Write a one-page decision record (`desk/investment_memos/decision_record_template.md`) that includes:

1. The reference-class overrun before and after including the four missing projects, under a stated assumption about their overruns.
2. The adjusted expected profit and a CE at $\gamma = 3$, or a reason why you cannot compute them.
3. The information you would buy before deciding, with an EVSI argument (qualitative is acceptable if the inputs do not exist).
4. A decision: commit (with size), commit conditionally, or abstain.

**Rubric** (see `problems/solutions/ch20_solutions.md`, Solution 20.10):

| Element | Full credit (4) | Partial (2) | None (0) |
|---|---|---|---|
| Selection correction | Recomputes the reference class with the missing projects and states the assumption | Notes survivorship qualitatively | Uses the six projects as presented |
| Inside vs outside view | Applies a regressive adjustment with a stated $r$ | Uses the outside view without adjustment | Uses the sponsor's 2% |
| Sizing | Uses CE or a fraction-of-wealth argument; size falls with reference-class risk | Mentions concentration | Commits \$4.0m because EV is positive |
| Information | Names the missing project files as the highest-EVSI item; pre-commits to a decision rule | Lists diligence items without priority | None |
| Abstention | Recognizes that abstaining until the full record is produced is the best current action | Commits conditionally without stating the condition | Commits unconditionally |

---

## 20.10 Frequent analytical errors

1. **Reading sensitivity as the posterior.** An 85%-sensitive test with a 15% base rate and a 20% false-positive rate gives a 43% posterior, not 85%.
2. **Treating ten annual returns as evidence of skill.** The standard error is about a third of the volatility, before the smoothing adjustment.
3. **Fitting a normal distribution and quoting its tail.** Normal and fat-tailed models agree at 2σ and disagree by orders of magnitude at 4–5σ.
4. **Using kurtosis as a tail measure.** It may not exist, and its sample value is dominated by a few points.
5. **Selecting the best model and discarding the rest.** This removes between-model variance, which is often half the total.
6. **Building a reference class from survivors.** Completed projects understate overruns. Ask how many were started.
7. **Claiming calibration from hit rates.** "We hit 18 of 40" says nothing about calibration without the stated probabilities. A calibration table needs the forecast, the count, and the outcomes.
8. **Eliciting unions, intersections, and marginals separately.** This produces incoherent probabilities. Elicit marginals and conditionals.
9. **Assuming independence between macro scenarios.** The joint state is often the one that matters (Example 20.8).
10. **Using expected value for a concentrated bet.** A positive-EV commitment of a quarter of wealth can have a CE below bills.
11. **Ordering diligence that cannot change the decision.** EVSI is zero if no report would change the action.
12. **Applying minimax regret mechanically.** It depends on the action set. Use it when probabilities cannot be defended, and say so.

---

## 20.11 Connections to other chapters

* **Chapter 1:** break-even probabilities (§1.4.2), the lemons problem and the value of diligence (Example 1.7), and Kelly growth (§1.4.5). This chapter adds EVSI, CRRA, and minimax regret.
* **Chapter 2:** selection bias in comparable sales (§2.4.8) and appraisal smoothing, which drive §20.4.3 and §20.4.6.
* **Chapter 3:** sequential Bayes in odds form (§3.4.9) and the value of waiting (§3.4.6). Example 20.11's option is the robust version of Chapter 3's real option.
* **Chapter 4:** real-time data, revisions, and NBER dating, the background to §20.8.
* **Chapter 11:** hotel PCA and PIP diligence, used in Examples 20.2 and 20.10.
* **Chapter 21:** VaR, expected shortfall, Kelly, and drawdowns. Example 20.4's tail estimates feed its risk limits, and Example 20.9's CRRA sizing is its starting point.
* **Chapter 22:** regressions, backtest hygiene, and the multiple-testing problem, which extends §20.4.3.
* **Chapter 25:** the decision journal that makes calibration scoring possible.

---

## 20.12 One-page reference sheet

| Tool | Formula | Use |
|---|---|---|
| Total variance | $\operatorname{Var}X = E[\operatorname{Var}(X\mid S)] + \operatorname{Var}(E[X\mid S])$ | Separate diligence-reducible from regime risk |
| Profit variance | $\sigma_V^2 + \sigma_C^2 - 2\rho\sigma_V\sigma_C$ | Development risk |
| Bayes | $P(H\mid E) = \frac{s\,p}{s\,p + f(1-p)}$ | One diagnostic signal |
| t interval | $\bar r \pm t_{1-\alpha/2,n-1}\,s/\sqrt n$ | Mean return |
| Effective $n$ | $n(1-\rho)/(1+\rho)$ | Smoothed series |
| Years for alpha | $(t\,\sigma_{TE}/a)^2$ | Is the record evidence? |
| Unit-variance t tail | $F_{t_\nu}(-z/\sqrt{(\nu-2)/\nu})$ | Fat-tail probability |
| Pareto tail | $P(X>x) = P(X>u)(x/u)^{-\alpha}$ | Extrapolate beyond data |
| Hill | $\hat\alpha = k/\sum_{i\le k}\ln(X_{(i)}/X_{(k+1)})$; se $\approx\hat\alpha/\sqrt k$ | Tail index |
| BMA | $w_k \propto \pi_k L_k$; $\sigma^2 = \sum w_k\sigma_k^2 + \sum w_k(\mu_k-\bar\mu)^2$ | Model uncertainty |
| Reference class | $\hat y = b + r(x-b)$; $b$ includes failures | Overruns, lease-up |
| Brier | $BS = REL - RES + UNC$; $BSS = 1 - BS/UNC$ | Score forecasters |
| Coherence | $P(A\cup B) = P(A)+P(B)-P(A\cap B)$ | Elicitation check |
| CRRA CE | $(\sum p_s W_s^{1-\gamma})^{1/(1-\gamma)}$ | Accept and size |
| Pratt | $E[W]-W_{CE} \approx \tfrac12\gamma\sigma_W^2/E[W]$ | Small bets only |
| EVPI | $E[\max_a x] - \max_a E[x]$ | Upper bound on information |
| EVSI | $\sum_e P(e)\max_a E[x\mid e] - \max_a E[x]$ | Price a study |
| Minimax regret | $\min_a\max_s(\max_{a'}x_{a',s} - x_{a,s})$ | No credible probabilities |

**Numbers worth remembering (from this chapter's examples).** Normal 3σ tail: 0.135%. Variance-matched $t_4$ at 3σ: 0.66%, about 5×. At 5σ: about 3,700×. Ten annual returns at 10% volatility: a 95% CI of roughly ±7%. A 2% alpha at 6% tracking error needs about 36 years to reach $t = 2$.

**Library.** `sdesk.stats.brier_score`, `sdesk.stats.bayes_posterior`, and `sdesk.x_decision`: `student_t_cdf`, `t_interval`, `scaled_t_tail`, `hill_estimator`, `bma_weights`, `mixture_moments`, `reference_class_adjust`, `brier_decomposition`, `crra_certainty_equivalent`, `evpi`, `evsi_binary_signal`, `minimax_regret`.

---

## References for this chapter

Full entries with verification status are in `references/sources_ch20.md`.

* Brier, G. W. (1950). "Verification of Forecasts Expressed in Terms of Probability." *Monthly Weather Review*, 78(1), 1–3.
* de Finetti, B. (1937). "La prévision: ses lois logiques, ses sources subjectives." *Annales de l'Institut Henri Poincaré*, 7, 1–68.
* Federal Reserve Bank of Philadelphia. "The Anxious Index"; "Survey of Professional Forecasters: Frequently Asked Questions"; *Survey of Professional Forecasters, Fourth Quarter 2008* (17 November 2008).
* Flyvbjerg, B., Holm, M. S., and Buhl, S. (2002). "Underestimating Costs in Public Works Projects: Error or Lie?" *Journal of the American Planning Association*, 68(3), 279–295.
* Gabaix, X. (2009). "Power Laws in Economics and Finance." *Annual Review of Economics*, 1, 255–294.
* Hill, B. M. (1975). "A Simple General Approach to Inference About the Tail of a Distribution." *Annals of Statistics*, 3(5), 1163–1174.
* Hoeting, J. A., Madigan, D., Raftery, A. E., and Volinsky, C. T. (1999). "Bayesian Model Averaging: A Tutorial." *Statistical Science*, 14(4), 382–417.
* Kahneman, D., and Lovallo, D. (1993). "Timid Choices and Bold Forecasts: A Cognitive Perspective on Risk Taking." *Management Science*, 39(1), 17–31.
* Kahneman, D., and Tversky, A. (1979). "Intuitive Prediction: Biases and Corrective Procedures." *TIMS Studies in Management Science*, 12, 313–327.
* Lahiri, K., and Wang, J. G. (2013). "Evaluating Probability Forecasts for GDP Declines Using Alternative Methodologies." *International Journal of Forecasting*, 29(1), 175–190.
* Mandelbrot, B. (1963). "The Variation of Certain Speculative Prices." *Journal of Business*, 36(4), 394–419.
* Murphy, A. H. (1973). "A New Vector Partition of the Probability Score." *Journal of Applied Meteorology*, 12, 595–600.
* Potter, S. (2011). "The Failure to Forecast the Great Recession." *Liberty Street Economics*, Federal Reserve Bank of New York, 25 November 2011.
* Pratt, J. W. (1964). "Risk Aversion in the Small and in the Large." *Econometrica*, 32(1/2), 122–136.
* Raiffa, H., and Schlaifer, R. (1961). *Applied Statistical Decision Theory*. Boston: Harvard Business School.
* Rudebusch, G. D., and Williams, J. C. (2009). "Forecasting Recessions: The Puzzle of the Enduring Power of the Yield Curve." *Journal of Business & Economic Statistics*, 27(4), 492–503.
* Savage, L. J. (1951). "The Theory of Statistical Decision." *Journal of the American Statistical Association*, 46(253), 55–67.
