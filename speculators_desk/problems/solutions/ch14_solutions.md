# Chapter 14 Solutions

Numerical results are verified in `tests/test_ch14_examples.py`. Figures are rounded for display only.

---

### Solution 14.1
(a) (i) **Leverage.** The earnings yield is on levered equity and the cap rate on the whole capital structure: $c + (D/E)(c - r_D)$ can be above or below $c$. (ii) **Depreciation versus reserve.** Accounting D&A on a stepped-up or development basis usually exceeds a 4% FF&E reserve, which depresses earnings. (iii) **Tax and overhead.** A C-corp pays income tax and corporate G&A, and a private cap rate is quoted before both. A fourth reason is that the company's EBITDA may include management or franchise income that is not property NOI.

(b) $k = E_1/P$ when retained earnings are reinvested at exactly $ROE = k$, so growth adds no value. Earnings are a claim on a business whose prices and costs reset with inflation, so $E/P$ approximates a **real** expected return. That is why it is compared with a TIPS yield.

(c) It subtracts a nominal yield from an (approximately) real yield. When inflation expectations are high, nominal yields are high and the gap looks negative even if real expected equity returns are unchanged. Asness (2003) finds that the comparison has no power to forecast long-horizon real returns.

### Solution 14.2
Price change $= 5{,}900.00 - 5{,}860.25 = 39.75$ points in the short's favor.
(a) $P\&L = (-1)(5{,}860.25 - 5{,}900.00) \times 5 \times 3 = +\$596.25$.
(b) E-mini: $39.75 \times 50 \times 3 = +\$5{,}962.50$, ten times the intended exposure.
(c) $39.75/0.25 = 159$ ticks; $159 \times \$1.25 \times 3 = \$596.25$. ✓
(d) Notional $= 5{,}900 \times 5 \times 3 = \$88{,}500$.

### Solution 14.3
$c = (1/12.5)(1 - 0.04/0.30) = 0.08 \times 0.8667 = 6.93\%$.
The public market capitalizes hotel NOI at 6.93%, below the private 7.50%. It pays **more** for each dollar of NOI, before any adjustment for the company's platform value, G&A, and non-property income. If the EBITDA includes management fees, which deserve a higher multiple, the property-only cap rate is somewhat higher than 6.93%.

### Solution 14.4
(a) $F^* = 5{,}500 \times e^{(0.04 - 0.015)\times 0.5} = 5{,}500 \times e^{0.0125} = 5{,}569.18$.
(b) $5{,}585.00 - 5{,}569.18 = 15.82$ points rich. **Cash-and-carry:** buy the stock basket financed at 4%, sell futures, deliver (cash-settle) at expiry. Profit after costs $= (15.82 - 4) \times 50 = \$590.93$ per contract.
(c) $5{,}569.18 - 5{,}560.00 = 9.18$ points cheap. **Reverse cash-and-carry:** sell the stocks (or short them), invest the proceeds, buy futures. Profit $= (9.18 - 4) \times 50 = \$259.07$ per contract. In practice this is done by holders of index portfolios who can sell stock they own and replace it with cheaper futures. A trader without the stocks must borrow 500 names and pay borrow fees, which widens the lower bound of the band.

### Solution 14.5
(a) Solve $5{,}000 = \sum_{t=1}^{5} 170(1.08)^{t-1}/(1+k)^t + CF_5(1.035)/[(k - 0.035)(1+k)^5]$ by bisection: $k = 7.47\%$; $ERP = 7.47\% - 4.00\% = 3.47\%$.
(b) Gordon: $k = 3.40\% + 3.50\% = 6.90\%$; $ERP = 2.90\%$.
(c) Five years of 8% growth add 57 bp to the implied return. Most of the value is still the terminal value, so stress $g_2$ first: each 50 bp on $g_2$ moves $k$ by nearly 50 bp. The high-growth phase is the assumption most likely to be wrong in a downturn, but it matters less to $k$.

### Solution 14.6
(a) $SUE = (1.32 - 1.20)/0.05 = 2.4$.
(b) Forward P/E before $= 60.00/2.40 = 25.0$x. New forward EPS $= 2.40 \times 1.04 = \$2.496$. New price $= 2.496 \times 23 = \$57.41$, a decline of 4.3%.
(c) The beat raised forward earnings by 4%, but the guidance about unit growth cut the multiple by 8% ($23/25 - 1$). Price is forward earnings times the multiple, and the multiple embeds long-run growth. Post-earnings-announcement drift (Bernard and Thomas, 1989) suggests that prices historically continued to move in the direction of the surprise for weeks. Here the surprise in current EPS and the news about growth point in opposite directions, so the drift evidence does not give a clear prediction. Do not trade the headline SUE alone.

### Solution 14.7
(a) Total cap $= 7{,}000$. Contributions: $3{,}000 \times 0.25/7{,}000 = 10.71\%$; $2{,}500 \times 0.18/7{,}000 = 6.43\%$; $-0.69\%$; $-0.57\%$; $-0.51\%$. Cap-weighted $= 15.37\%$. Equal-weighted $= (25 + 18 - 6 - 10 - 12)/5 = 3.00\%$. Advancers 2, decliners 3. The two largest stocks contribute 17.14%, more than the index's total return.
(b) Compounded trailing return $= \prod(1 + r_t) - 1 = +5.89\%$, so the signal is long (+1). Weight $= 10\%/20\% = 0.5$ times capital.
(c) The index is trending up on narrow leadership. A REIT investor who sells S&P 500 futures is short mainly two large stocks with strong momentum. The hedge can lose money on a rally driven by those names while REITs, which resemble the typical member more than the leaders, fall. Basis risk is larger than the beta estimate suggests. Consider a hedge with a closer underlying (equal-weighted or REIT index exposure, or puts) or a smaller hedge.

### Solution 14.8
(a) Position $= 50{,}000 \times 30 = \$1{,}500{,}000$. Borrow cost $= 0.25 \times 0.5 \times 1{,}500{,}000 = \$187{,}500$.

| Scenario | Gross P&L | Net | p |
|---|---|---|---|
| −40% (\$18) | +600,000 | +412,500 | 0.45 |
| Flat | 0 | −187,500 | 0.25 |
| +60% (\$48) | −900,000 | −1,087,500 | 0.30 |

$EV = 0.45(412{,}500) + 0.25(-187{,}500) + 0.30(-1{,}087{,}500) = 185{,}625 - 46{,}875 - 326{,}250 = -\$187{,}500$. The expected price change is zero ($0.45 \times -40\% + 0.30 \times 60\% = 0$), so the EV equals minus the borrow fee.

(b) $P^* = 1.5 \times 30/1.3 = \$34.62$, a rise of 15.4%. In the +60% state the margin call comes long before the end of the horizon, and recall risk is highest in that state.

(c) **Decline the short as proposed.** The PM's most likely scenario is right, but the mean is zero before costs and negative after a 25% borrow fee. The loss state is the largest and arrives with a margin call and a likely recall.

*Rubric.* Full credit: computes the EV after borrow; identifies that the modal scenario is favorable but the mean is not; computes the margin trigger; names recall risk as correlated with the loss state; proposes abstention or a defined-loss alternative (puts, put spreads) with the premium compared to the expected decline; states what would change the decision (a lower borrow fee, a catalyst with a date, a lower probability of the squeeze state). Partial credit: computes the EV but recommends a smaller short without addressing borrow and recall. No credit: recommends the short because "the most likely outcome is −40%".

### Solution 14.9
(a) $N = 0.85 \times 25{,}000{,}000/(5{,}600 \times 50) = 21{,}250{,}000/280{,}000 = 75.89$; sell 76.
(b) $21.25\text{m} \times 3.0\% \times 4/12 = \$212{,}500$.
(c) $76 \times 50 \times 560 = \$2{,}128{,}000$ of variation margin, paid as the rally happens.
(d) The office needs **cash**, not beta-neutral exposure, in four months. Selling the REITs now converts the position to cash with certainty, at the cost of the expected premium on the sleeve (about the same \$212,500 if REIT premia match the ERP) plus trading costs and any tax. The futures hedge leaves REIT-specific and rate risk (Example 14.5), requires a cash reserve of at least \$2–3 million for a rally, and requires the REITs to be sold anyway in four months. Doing nothing is defensible only if the acquisition can be funded from other liquidity if the sleeve falls 20–25%.

*Rubric.* Full credit: correct $N$ and cost; recognizes that a known cash need favors selling over hedging; quantifies variation margin; identifies the residual (idiosyncratic and rate) risk; states what would change the answer (a tax cost of selling, uncertainty about whether the acquisition closes, a view that REITs are cheap relative to private assets). Partial: correct numbers but recommends the hedge without liquidity analysis.

### Solution 14.10
(a) Market cap $= 11 \times 150\text{m} = \$1.65$ billion. Implied real estate value $= 1.65 + 1.90 - 0.10 = \$3.45$ billion. Implied cap $= 270/3{,}450 = 7.83\%$. At 7.00%: GAV $= \$3.857$ billion; NAV $= 3.857 - 1.90 + 0.10 = \$2.057$ billion $= \$13.71$ per share. Discount $= 11.00/13.71 - 1 = -19.8\%$.

(b) Appraised value $= 18/0.07 = \$257.1$ million; debt $= 0.55 \times 257.1 = \$141.4$ million; equity $\$115.7$ million. At 7.83%: value $= 18/0.07826 = \$230.0$ million (−10.6%); equity $= \$88.6$ million (**−23.5%**).

(c) *A defensible decision.* (i) **Marks:** the fund cannot ignore an 83 bp public–private gap during a period with no private comparables. Commission an updated appraisal that explicitly weighs the broker opinions and the REIT evidence, and disclose the sensitivity (equity −23.5% at REIT pricing) to LPs. (ii) **Redemptions:** paying redeeming LPs at a stale NAV transfers value from remaining LPs to leavers. Use the fund's gating or queue provisions until marks are refreshed. (iii) **REIT position:** abstain, or take only a small position. The discount may be correct (your marks are stale) or REIT-specific, and without a catalyst it can persist. Buying the REIT while marking your own hotels at 7.00% asserts both that the REIT is cheap and that your marks are right. Those are the same claim seen from two sides, and the evidence does not support it yet.

*What would change the answer:* closed private trades near 7.0% (marks hold, REIT is cheap, a REIT position with a catalyst becomes reasonable); closed trades near 7.8% (write down, and the REIT is fairly priced); a REIT-specific explanation such as an index deletion or a dividend cut (the gap says little about private values).

*Rubric.* Full credit: computes the implied cap and the NAV discount; translates the gap into the fund's equity sensitivity; addresses the fairness of redemptions at stale marks; treats the REIT trade and the mark as one question; names the evidence that would decide it; accepts abstention. Partial: correct numbers and a REIT trade recommendation that ignores the fund's own marks. No credit: "buy the REIT at a 20% discount".
