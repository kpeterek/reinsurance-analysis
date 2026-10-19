# Chapter 19 Solutions

Numerical results are verified in `tests/test_ch19_examples.py`. Figures are rounded for display only. All inputs are [HYPOTHESIS] unless cited.

---

### Solution 19.1

| Asset | Cash flow if never sold? | Strongest anchor | First dimension to examine |
|---|---|---|---|
| (a) Net-leased warehouse | Yes: contractual rent | NOI ÷ cap rate; replacement cost | Tail risk / tenant credit (a single tenant is the asset) |
| (b) EU allowance | No | Regulatory: marginal abatement cost under the cap; compliance demand | Tail risk from policy change |
| (c) Governance token | No (votes only, unless the protocol distributes fees) | None independent of resale | Custody/rights: what the token legally conveys |
| (d) Song royalties | Yes: royalty income | PV of a decaying income stream | Transparency: decay rate and the reliability of reported royalty statements |
| (e) Unentitled parcel | No; negative carry | Residual land value if entitled; agricultural value if not | Valuation anchor's leverage: sensitivity of the residual to GDV and to the entitlement probability |
| (f) Bitcoin on a non-U.S. exchange | No | None independent of resale | Custody: the holder owns an exchange claim, not a coin (§19.9) |

Items (a) and (d) are income assets despite their different labels. Item (f) shows that the same asset can score differently depending on the custody chain.

### Solution 19.2
DPI $= 18/60 = 0.30$. RVPI $= 66/60 = 1.10$. TVPI $= 1.40$. RVPI is $1.10/1.40 = 78.6\%$ of TVPI: most of the reported multiple is an estimate.

### Solution 19.3
(a) Paid $= 500{,}000 \times 1.27 = 635{,}000$. Net on resale $= 500{,}000 \times 0.90 = 450{,}000$. Round trip $= 1 - 450/635 = 29.13\%$. Equivalently `round_trip_cost(0.27, 0.10)` $= 1 - 0.90/1.27$.
(b) Annual drag $= 1 - (1 - 0.2913)^{1/4} = 1 - 0.7087^{0.25} = 8.25\%$ a year. Hammer prices must grow about 8.25% a year just to recover the cost over four years.

### Solution 19.4
(a) Paid-in 100; distributed 140; TVPI $= 1.40$. Net flows $[-40, -30, -10, 50, 40, 30]$; IRR $= 13.52\%$.

(b) Contributions in index units (×100): $40/1.00 + 30/0.90 + 30/0.95 = 40 + 33.333 + 31.579 = 104.912$.
Distributions: $20/0.95 + 50/1.10 + 40/1.20 + 30/1.30 = 21.053 + 45.455 + 33.333 + 23.077 = 122.917$.
KS-PME $= 122.917/104.912 = 1.172$.

(c) With a flat index every $I_t = 100$, so KS-PME = TVPI = 1.40. The PME is the multiple measured against an index that earns nothing; it rises above the actual 1.17 because the actual index rose 30% and the fund's distributions came mostly after the rise.

Note one subtlety: the index fell to 90 at year 1, so the year-1 call bought more index units ($30/0.90$) than its dollar amount. A fund that calls capital in a falling market is benchmarked against cheap index purchases, which raises the bar.

(d) $(130/100)^{1/5} - 1 = 5.39\%$ a year.

(e) Mirror balance at year 5 $= -23.4$. The fund distributed more than an index account receiving the same calls could have paid. That is consistent with KS-PME > 1, and it shows why an IRR on the mirror flows (the original Long–Nickels approach) can fail: the mirror position becomes a short.

### Solution 19.5
(a) $r_t = (r^*_t - 0.6\,r^*_{t-1})/0.4$:
* $r_1 = (0.07 - 0.024)/0.4 = 11.5\%$
* $r_2 = (0.06 - 0.042)/0.4 = 4.5\%$
* $r_3 = (0.01 - 0.036)/0.4 = -6.5\%$
* $r_4 = (-0.03 - 0.006)/0.4 = -9.0\%$
* $r_5 = (0.02 + 0.018)/0.4 = 9.5\%$

Sample s.d.: reported (7, 6, 1, −3, 2%) $= 4.04\%$; unsmoothed $= 9.30\%$. Theoretical ratio $\sqrt{(1-a)/(1+a)} = \sqrt{0.4/1.6} = 0.50$, so true volatility about twice reported; the sample ratio is $9.30/4.04 = 2.30$.

End-point identity: reported sum $= 0.13$; unsmoothed sum $= 0.10$; correction $\frac{0.6}{0.4}(0.02 - 0.04) = -0.03$. ✓ Compounded: reported 13.34%, unsmoothed 8.56%. The reported series still contains past gains that the latest marks have not given back: the smoothed level overstates current value.

(b) Corrected value $= 50 \times (1 - 1.3 \times 0.15) = 50 \times 0.805 = \$40.25$ million. Bid $= 0.88 \times 50 = \$44.0$ million, which is $44/40.25 - 1 = 9.3\%$ **above** corrected value.

### Solution 19.6
(a) $\mu = 0.30 + 0.60 + 0.80 + 1.00 = 2.70\text{x}$. The 100x outcome contributes $1.00/2.70 = 37.0\%$.
(b) $0.99^{25} = 77.8\%$.
(c) $(2.70 - 0.01 \times 100)/0.99 = 1.70/0.99 = 1.72\text{x}$.
(d) With a 78% chance of no 100x outcome, the median fund is a fund without it, so its multiple is near the conditional mean of 1.72x plus whatever 20x outcomes it happens to hold; the exact median is 1.88x. The mean (2.70x) is pulled up by a minority of funds holding a 100x deal. With 100 investments, $P(\text{no }100\text{x}) = 0.99^{100} = 36.6\%$, so the median fund holds at least one, and the exact median rises to 2.56x (tested). Diversification does not change the mean; it raises the median toward it. The practical implication for an LP is that a single fund commitment, or a concentrated fund, is far more likely to deliver the median than the mean.

### Solution 19.7
(a) $S_{11} = 4$, $S_{22} = 4$, $S_{12} = -2$. $\sum x_1 y = 0.05 + 0.09 - (-0.04) - 0.00 = 0.18$. $\sum x_2 y = 0.02 + 0.08 + (-0.04) + 0.00 = 0.06$.
$\beta_1 = (0.18 \times 4 - 0.06 \times (-2))/12 = (0.72 + 0.12)/12 = 0.070$.
$\beta_2 = (4 \times 0.06 - (-2)(0.18))/12 = (0.24 + 0.36)/12 = 0.050$.
Index: 100, 107.25, 105.13.

(b) Population mean $= 0.25/8 = 0.03125$. Resold: 0.05, 0.10, 0.20, 0.35; mean $= 0.175$. Bias $= +0.144$. The index built from resales would show a large gain in a market whose average item gained about 3%.

### Solution 19.8
(a) Year-2 call to repay the line $= 25(1.07)^2 + 25(1.07) = 28.6225 + 26.75 = \$55.3725$ million. New calls: $[0, 0, 20 + 55.3725, 15, 5, 0, 0, 0, 0] = [0, 0, 75.3725, 15, 5, 0, 0, 0, 0]$.

(b)

| | Original | With line |
|---|---|---|
| Paid-in | 90.00 | 95.37 |
| TVPI | 1.778 | 1.678 |
| IRR | 13.14% | 14.75% |
| Profit (\$m) | 70.00 | 64.63 |

IRR rises by about 160 bp while the LP earns \$5.37 million less.

(c) Rubric:
1. Recognizes that IRR rewards delaying LP calls, independently of investment skill (required).
2. Reports IRR together with TVPI, DPI and a PME, and asks for IRR computed as if capital had been called when invested (the "unlevered" or line-adjusted IRR) (required).
3. Notes that the LP bears the line's interest cost and, in a stress, the risk of a large concentrated call (liquidity) (credit).
4. Notes that carried-interest hurdles measured by IRR can be met earlier with a line, which shifts value from LPs to the GP (credit).
5. States what would justify the line: short bridging for administrative convenience, disclosed and capped (credit).

### Solution 19.9
(a) $E[P_3] = 96.75$; $V_0 = 96.75/1.15^3 = 63.61$. A price of 80 implies an expected return of $(96.75/80)^{1/3} - 1 = 6.54\%$, below her own 15% requirement. On her own view the token is overpriced by about 26%.

(b) 121.67 at year 3; 323.64 at year 10; 1,309.32 at year 20.

(c) Rubric:
1. Computes the token value and its expected return at 80; concludes the price is not justified on her own inputs (required).
2. Identifies that the token's only anchor is expected resale and that the inputs cannot be checked against cash flow or cost (required).
3. Identifies that land has a checkable but levered anchor (residual value), negative carry and an entitlement probability that must be estimated; refers to Example 19.8's break-even (required).
4. Recommends a size consistent with possible total loss for the token, if any, and no leverage (credit).
5. States what would change the view: for the token, evidence of non-speculative demand (use), a cash-flow claim, or a lower price; for land, entitlement evidence, a lower price or an option structure (credit).
Abstaining from the token at 80 is the answer most consistent with her own inputs.

### Solution 19.10
**What the 11% compensates for.** The yield must come from somewhere. The platform lends deposits to unnamed institutions and holds its own token. The 11% is compensation for unsecured credit risk on opaque counterparties, re-hypothecation risk, self-referential collateral and regulatory risk, not a "stable" yield on a dollar instrument.

**Stress test.** Per \$100 of deposits, suppose assets of \$100: \$40 institutional loans, \$25 own token, \$35 other reserves assumed held at par (generous: they are unaudited). Loans default 30% with zero recovery: $40 \times 0.70 = 28$. Token falls 80%: $25 \times 0.20 = 5$. Reserves 35. Assets $= 68$ against deposits of 100: depositors face a 32% loss **before** any run, legal cost or delay. The token is most likely to fall in exactly the state in which loans default, so the two losses are correlated.

**Insolvency claim.** Under re-hypothecation terms the family is probably an unsecured creditor of an offshore entity, not the owner of identified dollars [INFERENCE; depends on terms and jurisdiction; obtain legal advice]. Recovery would be slow and uncertain (§19.9).

**Recommendation.** Abstain. The family member's one-year experience is a single draw from a distribution whose bad outcomes are rare and large; the newsletter and the token's price rise are not evidence of solvency. What would change the answer: audited reserves held in segregated accounts at regulated institutions; named counterparties with collateral; a legal opinion that deposits are bankruptcy-remote; and a yield consistent with those safer assets, which would be far below 11%.

**Rubric.**
1. Identifies the source of the yield and that it compensates for credit and structural risk (required).
2. Performs the stress test and notes correlation between the token and loan losses (required).
3. Identifies the custody/claim issue and the probable unsecured-creditor status (required).
4. Treats the anecdotal evidence (one year without problems, newsletter, token rally) as non-evidence of solvency (required).
5. Recommends abstention or states conditions so strict they amount to abstention, and lists information that would change the decision (required).
6. Connects to §19.9 (self-referential collateral) and to Chapter 1's "why is this price available to me?" (credit).

---

## Decision exercise (§19.10) — rubric and model answer

| Proposal | Key dimensions | Defensible answers | Red flags in a weak answer |
|---|---|---|---|
| A — First-time VC fund | Cash flow, anchor, tail (power law) | Small commitment sized to median outcome (≈1.9–2.0x on Example 19.1's assumptions) or abstain; prefer established managers if access exists | Using a top-quartile target as the expectation |
| B — Buyout secondary at 85% of NAV | Transparency (stale NAV), liquidity | Re-mark NAV for public moves; re-bid against corrected value; buy only at a discount to corrected NAV; compute KS-PME on history | Calling 85% of a stale NAV a discount |
| C — \$2m painting | Transaction costs, anchor | Treat as consumption; if bought, hold long and negotiate costs; compute the 15%/yr hurdle | Quoting an index return without selection or cost adjustment |
| D — Bitcoin | Custody, reflexivity, tail | Small, unlevered, segregated custody, written loss budget, or abstain | "Uncorrelated with CRE" from calm-period data |
| E — Land | Anchor leverage, carry, financing | Bid ≤ about \$2.1m at a 60% entitlement view, or an option | Pricing on the entitled value |
| F — Carbon | Policy (allowances); verification (offsets) | Separate the two; allowances only with a policy-scenario analysis; abstain on offsets without independent verification | Treating offsets and allowances as the same asset |

Overall: the sleeve does not diversify the family's dominant risk (credit availability and liquidity) as much as claimed. B, D and E all lose value when credit tightens; A and C cannot be sold. A strong answer may invest in only one or two proposals, or none.
