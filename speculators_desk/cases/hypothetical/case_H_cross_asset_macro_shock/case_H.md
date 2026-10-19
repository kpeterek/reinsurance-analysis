# Case H — Cross-Asset Macro Shock

> **Evidence status:** Every position, price level, shock size, loan term, and counterparty in this case is [HYPOTHESIS], constructed for teaching. The market moves are stylized to be internally consistent with a hawkish inflation surprise. They are not a record of any actual release day. Contract conventions (E-mini S&P 500 multiplier of \$50 per index point; fed funds futures at \$41.67 per basis point) are [FACT] and sourced in `references/sources_ch05.md` (ch05-S11, ch05-S22). Mechanism claims are [INFERENCE] unless labeled otherwise.
>
> **Model:** `case_h_model.py` (run it to regenerate every number). **Tests:** `tests/test_case_h.py`. **Rubric:** `case_H_rubric.md`.
>
> **Chapters used:** 2 (appraisal smoothing, price formation), 5 (policy transmission), 6 (duration, DV01, convexity), 10 (loan sizing, refinancing), 14 (equity index futures), 15 (FX conventions), 17 (credit spreads), 18 (rate caps).

---

## Case facts (shared by all modes)

**The book.** A single-family office runs a combined markets-and-property book with a net asset value of **\$400 million**. The investment committee meets monthly. The markets positions are marked daily. The two property interests are wholly owned and marked quarterly by an external appraiser.

**Exhibit H-1 — Positions at 8:29 a.m. ET on release day**

| # | Position | Size | Terms |
|---|---|---|---|
| 1 | Long 10-year U.S. Treasury note | \$60,000,000 face | 4.25% coupon, 10 years to maturity, priced at par (yield 4.25%), semiannual |
| 2 | Long 2-year U.S. Treasury note | \$40,000,000 face | 3.90% coupon, 2 years, at par (yield 3.90%) |
| 3 | Long E-mini S&P 500 futures (ES) | 50 contracts | Entry 6,000.00; multiplier \$50 per index point |
| 4 | Euro-listed property-company shares, unhedged | €25,000,000 market value | EUR/USD 1.1000 |
| 5 | Investment-grade corporate bonds | \$35,000,000 market value | Represented as an 8-year 5.10% bond at par |
| 6 | High-yield corporate bonds | \$15,000,000 market value | Represented as a 5-year 7.50% bond at par |
| 7 | Select-service hotel portfolio (owned 100%) | NOI \$4,600,000 | \$48,000,000 floating-rate loan at one-month Term SOFR + 3.40%, interest-only, actual/360. SOFR 3.85%. Rate cap strike 4.50%. Cash-management trap if DSCR < 1.20x. Value at a 7.00% cap: \$65.7 million |
| 8 | Multifamily property (owned 100%) | NOI \$3,300,000 | \$42,000,000 existing loan matures in about five months. Last appraisal at a 5.50% cap: \$60.0 million |

**Refinancing terms for position 8** (a life-company indication received last week): coupon = 10-year Treasury + 1.65%, rate set at closing, 30-year amortization, sized to the lesser of 65% LTV, 1.25x DSCR, and a 7.5% debt yield. Refinancing costs are 1% of the existing balance.

**The event.** At 8:30 a.m. ET, core CPI prints +0.6% month over month against a consensus of +0.3%. By the 4:00 p.m. close:

**Exhibit H-2 — Market moves on release day**

| Market | Move |
|---|---|
| 2-year Treasury yield | +25 bp |
| 5-year Treasury yield | +22 bp |
| 10-year Treasury yield | +18 bp |
| ES | 6,000.00 → 5,850.00 (−2.5%) |
| EUR/USD | 1.1000 → 1.0890 (dollar +1.0% against the euro) |
| Euro property shares, local currency | −2.0% |
| IG credit spreads | +12 bp |
| HY credit spreads | +40 bp |
| Expected average SOFR over the next 12 months (from SOFR futures) | +25 bp |
| Life-company spread over the 10-year (indicated by phone) | +15 bp |

Fed funds futures now price a meaningfully higher probability of a hike at the next meeting than they did the day before. The appraiser will not revisit position 8's value until the quarter-end review, eleven weeks away.

**Additional assumptions** for the private-market analysis [HYPOTHESIS]:

* The economic (transaction-clearing) cap rate for position 8 moves by half of the 10-year move plus 6 bp of risk-premium widening.
* Quarterly appraisals follow $A_t = \alpha V^*_t + (1-\alpha)A_{t-1}$ with $\alpha = 0.35$. Here $V^*_t$ is the economic value, held constant after the shock.

---

## Mode A — Guided instruction

Work through each step before reading the commentary.

### Step 1: Write the chain before computing anything

A hawkish inflation surprise raises the expected policy path (Chapter 5). The chain:

1. **Front end.** The 2-year reprices the next several meetings. It rises most.
2. **Long end.** The 10-year rises by less unless the market doubts the Fed's resolve. The curve bear-flattens.
3. **Equities.** The discount rate rises and growth expectations fall, so the index falls.
4. **Dollar.** Expected U.S. rates rise relative to other countries' rates, so the dollar rallies. A U.S. investor's euro assets lose value in dollars.
5. **Credit.** Risk appetite falls and expected defaults rise, so spreads widen *on top of* the Treasury move.
6. **Floating CRE debt.** SOFR expectations rise, and debt service rises at the next resets.
7. **Fixed CRE debt.** The coupon at the next lock rises with the 10-year and the lender's spread. DSCR-sized proceeds fall.
8. **Private CRE values.** No price prints today. Cap rates adjust over months through bids, appraisals, and a thinning of transactions.

Map each position to its link in the chain. Positions 1–6 are links 1–5 and are marked today. Positions 7–8 are links 6–8, and their effects arrive on different clocks.

### Step 2: Treasuries — DV01 first, then reprice

The DV01 is the dollar change for a 1 bp yield change. Compute it with `sdesk.fixed_income.dv01`. The duration estimate of P&L is $-DV01 \times \Delta y_{bp}$. The exact P&L comes from repricing at the new yield. The difference between them is convexity, which favors the long.

Use the right curve point for each bond: +25 bp for the 2-year and +18 bp for the 10-year. Using a single "rates up 20 bp" figure misstates both.

### Step 3: Equity futures — notional and multiplier

ES P&L $=$ side $\times$ (exit − entry) $\times$ \$50 $\times$ contracts. The \$50 multiplier is the E-mini's. The \$250 multiplier belonged to the older full-size contract. Using it overstates the P&L fivefold. Also compute the notional, \$50 × 6,000 × 50, so the committee can see the equity exposure in dollars.

### Step 4: FX translation — quote direction and decomposition

EUR/USD 1.1000 means one euro costs 1.1000 dollars. Converting euros to dollars **multiplies** by the rate. The dollar value of the position changes for two reasons: the local price moved, and the currency moved. Decompose the change:

* Local effect at the old rate: $\Delta(\text{EUR value}) \times S_0$.
* FX effect on the new local value: $(\text{EUR value})_1 \times (S_1 - S_0)$.

The two sum exactly to the total change. The dollar return is $(1 + r_{local})(1 + \Delta S/S) - 1$, not the sum of the two.

### Step 5: Credit — separate rate duration from spread duration

A corporate bond's yield is the Treasury yield plus a spread. Its loss has a rate component, $-MV \times D_{mod} \times \Delta y_{Tsy}$, and a spread component, $-MV \times D_{mod} \times \Delta s$. Use the 5-year Treasury move for both credit positions, because their durations are in the 4–7 range. The spread component is the credit-specific loss. Hedging the rate component with Treasuries leaves it in place.

### Step 6: The floating-rate hotel loan

Floating interest $= L(SOFR + s) \times 365/360$. Compute DSCR before the shock, after the repricing of expected SOFR, and at the cap strike. Then find the SOFR at which the 1.20x cash-management trap springs. Compare that SOFR with the cap strike. A cap that sits *above* the trap level protects against default but not against cash being trapped.

### Step 7: The multifamily refinancing

Recompute the coupon: 10-year + spread, before and after. Size the loan on all three constraints with `sdesk.cre.max_loan`. The appraisal has not changed, so the LTV and debt-yield constraints do not move today. Only DSCR moves. Compute the refinancing gap (balance + costs − new loan) before and after.

Then ask how much of the proceeds loss came from the 10-year and how much from the lender's spread. Only the first can be hedged with Treasuries.

### Step 8: Immediate versus over subsequent months

Liquid markets moved on the day. Private CRE did not print. The economic value of position 8 has fallen anyway. Compute it at the new economic cap rate. Then trace how a smoothed appraisal recognizes the decline over four quarters. Finally, explain why transaction volume falls: sellers anchor to the last appraisal, buyers bid at the new economic value, and the gap between them is the bid–ask gap.

---

## Mode B — Solved case

All figures are produced by `case_h_model.py`.

### B.1 Treasuries

| | 10-year | 2-year |
|---|---|---|
| Face | \$60,000,000 | \$40,000,000 |
| Yield move | +18 bp | +25 bp |
| Modified duration | 8.078 | 1.906 |
| DV01 | \$48,468 per bp | \$7,625 per bp |
| Duration estimate $-DV01 \times \Delta y$ | −\$872,418 | −\$190,618 |
| Full reprice | **−\$864,928** | **−\$190,040** |
| Convexity benefit | \$7,490 | \$577 |

Total Treasury P&L: **−\$1,054,969**. Combined DV01 \$56,092 per bp.

The 10-year carries 86% of the Treasury DV01, although the 2-year moved more. Exposure is DV01 × move, and the long bond's DV01 is more than six times larger.

### B.2 Equity futures

Notional $= 6{,}000 \times \$50 \times 50 = \$15{,}000{,}000$.
P&L $= (+1)(5{,}850 - 6{,}000) \times \$50 \times 50 =$ **−\$375,000**, or −2.5% of notional.
With the wrong \$250 multiplier: −\$1,875,000. That error alone would overstate the day's loss by \$1.5 million.

### B.3 FX translation

| Step | Calculation | USD |
|---|---|---|
| Starting dollar value | €25,000,000 × 1.1000 | \$27,500,000 |
| New local value | €25,000,000 × 0.98 = €24,500,000 | |
| New dollar value | €24,500,000 × 1.0890 | \$26,680,500 |
| **Total change** | | **−\$819,500** |
| Local effect at old rate | −€500,000 × 1.1000 | −\$550,000 |
| FX effect on new local value | €24,500,000 × (1.0890 − 1.1000) | −\$269,500 |

Dollar return $= (0.98)(0.99) - 1 = -2.98\%$, against the −3.00% sum of the two moves.

**Quote-direction trap.** Dividing €25 million by 1.1000, as if the quote were euros per dollar, gives \$22.7 million. That misstates the position by \$4.8 million before any market move.

**Hedge comparison.** A short EUR/USD forward on €25,000,000 would have earned \$275,000. The hedged P&L would have been −\$544,500, which is the local equity loss less a small mismatch (\$5,500) because the hedge was sized on the starting, not the ending, local value.

### B.4 Credit

| | IG (\$35m, 8-yr) | HY (\$15m, 5-yr) |
|---|---|---|
| Modified duration | 6.502 | 4.106 |
| Rate component (+22 bp) | −\$500,667 | −\$135,511 |
| Spread component | −\$273,091 (+12 bp) | −\$246,384 (+40 bp) |
| Duration total | −\$773,759 | −\$381,895 |
| Full reprice | **−\$763,638** | **−\$376,033** |

Total credit P&L: **−\$1,139,671**. The spread-only loss is \$519,475. Most of the HY loss is spread. Most of the IG loss is rates.

### B.5 Day-one marked P&L

| Line | P&L | 
|---|---:|
| Treasuries (2y + 10y) | −\$1,054,969 |
| ES futures | −\$375,000 |
| Euro property shares (USD) | −\$819,500 |
| Credit (IG + HY) | −\$1,139,671 |
| **Total** | **−\$3,389,139** |
| As a share of NAV | **−0.85%** |

Every marked line lost money. A book that looks diversified across five asset classes behaved as a single position on inflation: long duration, long risk, and short the dollar.

### B.6 The floating-rate hotel loan (position 7)

Value at 7.00% cap = \$65,714,286; LTV 73.0%.

| | Before | After (SOFR 4.10%) | At cap strike (SOFR 4.50%) |
|---|---|---|---|
| Coupon | 7.25% | 7.50% | 7.90% |
| Annual interest $= L \cdot c \cdot 365/360$ | \$3,528,333 | \$3,650,000 | \$3,844,667 |
| DSCR | 1.304x | 1.260x | **1.196x** |

* Each basis point of SOFR costs \$4,867 a year. The +25 bp repricing adds \$121,667 a year.
* The 1.20x trap springs at SOFR **4.477%**, which is **below** the 4.50% cap strike. The cap protects against default, but not against cash being trapped.
* At the shocked rate, the trap is hit if NOI falls to \$4,380,000, a decline of 4.78%. An inflation surprise that raises wages and insurance can produce that by itself.
* Day-count trap: a 30/360 calculation gives \$3,600,000 and understates interest by \$50,000.

None of this hits the mark-to-market today. It reaches cash flow at the next monthly reset, as each actual SOFR fixing comes in. The futures-implied repricing tells you what to expect.

### B.7 The multifamily refinancing (position 8)

| | Before | After |
|---|---|---|
| Coupon (10-year + spread) | 4.25% + 1.65% = **5.90%** | 4.43% + 1.80% = **6.23%** |
| Loan constant | 0.071176 | 0.073730 |
| LTV 65% × \$60.0m (appraisal unchanged) | \$39,000,000 | \$39,000,000 |
| DSCR: \$3.3m / (1.25 × K) | \$37,090,956 | \$35,806,299 |
| Debt yield: \$3.3m / 7.5% | \$44,000,000 | \$44,000,000 |
| **Maximum loan (DSCR binds)** | **\$37,090,956** | **\$35,806,299** |
| Refinancing gap ($42.0m + \$0.42m − loan) | \$5,329,044 | **\$6,613,701** |

* Proceeds fall \$1,284,656 in one day. The refinancing gap rises 24%.
* At 6.23%, the full \$42 million balance would have a DSCR of only 1.066x. The existing loan size does not refinance on this NOI.
* **Decomposition.** At a coupon of 6.08% (10-year move only), proceeds fall \$709,491. The remaining \$575,165 comes from the lender's spread widening.
* **What a hedge could have done.** DSCR proceeds change by about \$40,014 per bp of coupon. Dividing by the 10-year's DV01 per dollar of face gives a hedge of **\$49.5 million** face of short 10-year Treasuries. Under the 18 bp shock that short would have earned \$714,068, offsetting the 10-year component (\$709,491) but none of the spread component. A rate lock or forward-starting swap does the same job more cleanly. Neither hedges the lender's spread or the lender's willingness to quote.

### B.8 Immediate versus over subsequent months

**Economic value.** The economic cap rate moves to $5.50\% + 0.5 \times 0.18\% + 0.06\% = 5.65\%$. Value falls from \$60,000,000 to **\$58,407,080 (−2.65%)**. Nothing in the reporting system shows this today.

**Appraisal path** ($\alpha = 0.35$, economic value held at \$58.41 million):

| Quarter after the shock | Appraised value | Share of the \$1.59m decline recognized |
|---|---:|---:|
| Q1 | \$59,442,478 | 35.0% |
| Q2 | \$59,080,088 | 57.8% |
| Q3 | \$58,844,535 | 72.5% |
| Q4 | \$58,691,426 | 82.1% |

After four quarters, 17.9% of the decline is still unrecognized. Reported volatility is lower and reported correlation with liquid markets is lower than the true figures, because of how the series is built, not because of how the asset behaves (Chapter 2).

**Bid–ask gap.** A seller anchored at the \$60.0 million appraisal asks 2.73% above a buyer who bids the \$58.4 million economic value. A buyer who needs fixed-rate debt at 6.23% also faces a going-in yield (5.65%) below the coupon, which is negative leverage, so many buyers will bid lower still or not at all. Most potential sellers who are not forced to sell will wait for rates to fall or for the appraisal to catch up. **Transaction volume falls before prices do.** The few trades that occur are disproportionately forced sales, which bias observed prices downward and add noise [INFERENCE from the mechanism; Chapter 2].

**Clock summary.**

| Exposure | Today | Next 1–3 months | 3–12 months |
|---|---|---|---|
| Treasuries, ES, FX, credit | Fully marked: −\$3.39m | Depends on subsequent data | — |
| Hotel floating loan | Expected interest +\$121,667/yr | Realized at each SOFR reset | Covenant trap risk if SOFR > 4.48% or NOI −4.8% |
| Multifamily refinancing | Indicated proceeds −\$1.28m | Rate set at closing: the exposure is open until then | Gap must be funded or the asset sold |
| Multifamily value | Not marked; economic −2.65% | Q1 appraisal −0.93% | Q4 appraisal −2.18%; volume down; bid–ask gap |

### B.9 Recommendation (one defensible answer)

1. **Do not sell liquid positions reflexively.** A 0.85% NAV loss is within the range a book like this should be built to absorb. The question is exposure, not the loss itself.
2. **Recognize the common factor.** Size the book's sensitivity to an inflation surprise as a single exposure. One way: re-run the day's moves at 2× as a stress scenario (about −\$6.8 million liquid, before CRE effects). Decide whether that is acceptable.
3. **Hedge the refinancing now.** The refinancing exposure is concentrated, dated, and hedgeable in its 10-year component: a rate lock or about \$50 million face of short 10-year Treasuries. Begin arranging the \$6.6 million gap (equity, preferred equity, or a partial paydown) now. Do not wait for the lock date.
4. **Address the hotel cap–trap mismatch.** Price a cap struck at or below 4.25%, or negotiate the trap level with the lender. Build a cash reserve against trapped cash flow.
5. **Consider a partial FX hedge** on the euro shares if the committee does not want currency risk in a property allocation. This is a policy decision: the dollar rally hurt today, and it can help on other shocks.
6. **Do not re-mark private values to zero change.** Report the economic estimate (−2.65%) alongside the appraisal to the committee.

**What would change the conclusion.** Evidence that the surprise was driven by one-off items (a rebound in a volatile component) would lower the persistence of the shock. A strong employment report would raise it. A life-company quote at a narrower spread would shrink the gap. A buyer at \$59–60 million for the multifamily would argue for selling rather than refinancing.

---

## Mode C — Blind examination

Use only the Case facts section and Exhibits H-1 and H-2. Allow 90 minutes. Calculators and spreadsheets are permitted.

1. (8 pts) Compute the DV01 and the full-reprice P&L of each Treasury position. Explain the difference from the duration estimate.
2. (6 pts) Compute the ES notional and P&L. State the multiplier and why it matters.
3. (10 pts) Compute the dollar P&L of the euro shares and decompose it into local and FX effects. Compute the P&L of a short EUR/USD forward hedge on the starting notional.
4. (10 pts) Compute the rate and spread components of the credit losses and the full-reprice totals.
5. (6 pts) Total the day-one marked P&L and express it as a share of NAV.
6. (12 pts) Compute hotel debt service and DSCR before, after, and at the cap strike. Find the SOFR at which the cash trap springs. Comment on the cap strike.
7. (14 pts) Size the multifamily refinancing before and after. Compute the refinancing gap. Split the proceeds loss into its 10-year and spread components. Size a Treasury hedge for the 10-year component.
8. (14 pts) Compute the economic value change of the multifamily and the four-quarter appraisal path. Explain the bid–ask gap and the fall in transaction volume.
9. (10 pts) Write a one-page memo to the investment committee with your recommendations and what would change them.
10. (10 pts) Name two ways in which the "standard" cross-asset pattern of Exhibit H-2 could fail on a different inflation surprise. For each, say which positions would then behave differently.

Answers: Mode B, and `case_H_rubric.md`.

---

## Mode D — Investment committee

You present to the CIO, the head of real estate, and an outside director who formerly ran a fixed-income desk. Prepare written answers. Each should be under 150 words and supported by a number.

1. **We hold five asset classes. Why did they all lose money on the same day?** What single factor explains it, and how large is the book's exposure to it?
2. **Is the multifamily really down 2.65%, when the appraiser says it is unchanged?** Defend or reject the number.
3. **Why not just hedge everything?** Which of today's losses could have been hedged, at what cost, and which could not?
4. **The hotel cap is struck at 4.50%. Is the hotel protected?**
5. **Should we lock the multifamily refinancing today, after the 10-year has already moved 18 bp?**
6. **What if the surprise was noise and reverses next month?** What is the cost of having hedged?
7. **Where is the liquidity?** If we need \$6.6 million for the refinancing gap, which assets do we sell, and what does that do to the book?
8. **What data would make you add risk rather than reduce it?**
9. **Would you sell the multifamily now rather than refinance?** At what price?
10. **What does this day tell us about how we measure diversification?**

The committee's rubric for these answers is in `case_H_rubric.md` (§Mode D).
