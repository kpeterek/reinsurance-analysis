# Case F — The Hotel versus Treasury Trade

> **Evidence status:** The hotel, its operating figures, the loan terms, the Treasury yield, the inflation rates, and the scenario probabilities are [HYPOTHESIS], constructed for teaching. The Treasury yield in particular is not a market quote: replace it with the live 5-year yield on the day of any real decision.
>
> **Tax status:** The federal rates used here (37% top ordinary rate, 20% long-term capital gains, 25% maximum on unrecaptured §1250 gain, 3.8% net investment income tax) and the jurisdictional facts (no Texas personal income tax; Treasury interest exempt from state and local income tax under 31 U.S.C. §3124; 39-year straight-line life for nonresidential real property including hotels) were checked for this project. See `references/sources_ch13.md`, ch13-S13 to ch13-S16, all `VERIFIED-SECONDARY`. **They are applied in a deliberately simplified model. This case is not tax advice.** Real outcomes depend on the investor's whole return, passive-activity status, purchase-price allocation, cost segregation, bonus depreciation, the timing of placed-in-service dates, and law in force at the time. Consult a tax adviser.
>
> **Model:** `case_f_model.py`. **Tests:** `tests/test_case_f.py`. **Rubric:** `case_F_rubric.md`.
>
> **Chapters used:** 1 (risk premia, sizing), 6 (duration, Treasury yields), 10 (amortization, DSCR), 11 (hotel NOI and reserves), 13 (opportunity cost, liquidity reserves, hold–sell), 21 (concentration and ruin).

---

## Case facts (shared by all modes)

**The investor.** A Texas resident, married filing jointly, who has sold an operating business and has \$8.0 million of liquid capital to deploy. The investor's other income keeps every marginal dollar from either alternative in the top federal bracket and above the net investment income tax thresholds. The investor will not materially participate in hotel operations. The horizon is five years.

**Alternative 1: the hotel.** A 110-room select-service hotel in a Texas metro, offered at \$16.5 million (\$150,000 per key). Year-1 NOI after a 4% FF&E reserve is \$1,400,000, an 8.48% going-in cap rate. Buyer closing costs are 2%. A lender offers 60% LTV (\$9.9 million) at 7.00% fixed, 25-year amortization, 10-year term, monthly payments. Exit at the end of year 5, at a cap rate applied to year-6 NOI, with 3% selling costs.

**Alternative 2: Treasuries.** Five-year U.S. Treasury notes bought at par yielding 4.00% [HYPOTHESIS], held to maturity.

The investor's adviser frames the question as: "8.5% cap versus 4% Treasury. Obviously the hotel." The investor asks you to evaluate expected cash flow, taxes, liquidity, duration, risk, inflation, financing, downside scenarios, and opportunity cost.

**Simplified tax assumptions** (all labeled; not advice):

| Item | Assumption |
|---|---|
| State income tax | None: Texas has no personal income tax [FACT; ch13-S15]. The state exemption of Treasury interest [FACT; ch13-S14] is therefore worth nothing to this investor |
| Treasury interest | Ordinary income: 37% + 3.8% NIIT = 40.8% |
| Hotel net income | 40.8%. A hotel with average guest stays of seven days or less is generally not a "rental activity" for the passive-loss rules; for a non-participating investor the income is treated here as passive trade-or-business income subject to NIIT. Taxable losses are assumed usable in the year incurred, against other passive income. Verify with an adviser |
| Purchase-price allocation | Land 15%, building 75%, FF&E 10% of price plus closing costs |
| Depreciation | Building: 39-year straight-line [FACT on the life; ch13-S16]. FF&E: 7-year straight-line. Full-year convention from year 1; no mid-month convention, cost segregation, or bonus depreciation |
| FF&E reserve | Treated as deductible (in practice, replacements are capitalized) |
| Sale | FF&E sold at its remaining tax basis (no §1245 recapture). Gain up to building depreciation taken: unrecaptured §1250 gain at 25% + 3.8% = 28.8%. Remainder: long-term capital gain at 20% + 3.8% = 23.8% |
| Timing | Taxes paid in the year the income arises; sale tax at year 5 |

**Scenarios for the hotel** [HYPOTHESIS]. Multipliers apply to the base NOI path (year-1 NOI \$1.4m growing at the scenario growth rate):

| Scenario | Probability | NOI multipliers, years 1–6 | NOI growth | Exit cap |
|---|---:|---|---:|---:|
| Upside | 20% | 1, 1, 1, 1, 1, 1 | 5% | 8.50% |
| Base | 45% | 1, 1, 1, 1, 1, 1 | 3% | 9.00% |
| Downside (recession in year 2) | 25% | 1, 0.75, 0.85, 0.95, 0.95, 0.95 | 3% | 10.00% |
| Severe (2020-type demand shock) | 10% | 0.35, 0.65, 0.80, 0.85, 0.90, 0.90 | 3% | 11.00% |

Inflation: 2.5% a year in the base case; a separate high-inflation case has 5% CPI, 5% NOI growth, and a 10.0% exit cap.

---

## Mode A — Guided instruction

### Step 1: The cap rate and the Treasury yield are not comparable returns

A cap rate is a first-year income yield on an unlevered, illiquid, operating business, before capital expenditure beyond the reserve and before taxes. A Treasury yield is a total return to maturity on a riskless, liquid claim. Comparing them directly compares an income yield with a total return and a risky asset with a riskless one. Build total-return cash flows for both, on the same equity, after tax.

### Step 2: Use the same capital

The hotel requires equity of $16.5\text{m} \times 1.02 - 9.9\text{m} = \$6.93\text{m}$. Compare it with \$6.93 million of Treasuries. The investor's remaining \$1.07 million is the liquidity reserve in both cases (Step 7).

### Step 3: Financing

Compute the monthly payment, annual debt service, DSCR, and the year-5 balance. Note that at 7.00% the loan constant (8.48%) almost equals the going-in cap rate (8.48%). Year-1 leverage is roughly neutral on cash yield. The levered return depends on growth and the exit.

### Step 4: Taxes

The hotel shelters part of its income with depreciation, defers the rest of its gain to the sale, and has part of that gain taxed at capital-gains rates. The Treasury's coupon is taxed every year at the full ordinary rate. Compute both after-tax IRRs and the share of the pre-tax return each loses to tax.

### Step 5: Scenarios

Run the four hotel scenarios. Report the expected after-tax IRR, the IRR of expected after-tax flows, the probability of loss, and the cash the investor must inject in the severe case.

### Step 6: Duration and inflation

The Treasury's price risk is its modified duration. The hotel equity's price risk is its sensitivity to the cap rate, amplified by leverage. Under inflation, the Treasury's nominal coupon is fixed and the hotel's room rates can reprice daily, but its cap rate may rise.

### Step 7: Liquidity and opportunity cost

A Treasury note can be sold in minutes. A hotel takes months to sell, at a 3% cost, and possibly not at all in a crisis. The expected return premium must compensate for illiquidity, concentration (one asset is 87% of the investor's liquid capital), operating risk, and the work of oversight. The opportunity cost of the hotel is the Treasury return plus the option value of liquid capital (Chapter 13).

---

## Mode B — Solved case

### B.1 Financing and basis

| Item | Value |
|---|---:|
| Loan | \$9,900,000 |
| Monthly payment | \$69,971.14 |
| Annual debt service | \$839,654 |
| Year-1 DSCR | 1.67x |
| Balance at end of year 5 | \$9,025,053 |
| Total basis (price + 2%) | \$16,830,000 |
| Land / building / FF&E | \$2,524,500 / \$12,622,500 / \$1,683,000 |
| Annual depreciation: building / FF&E / total | \$323,654 / \$240,429 / \$564,082 |
| Equity | \$6,930,000 |

### B.2 Base case: pre-tax and after-tax

| Year | NOI | Interest | Taxable income | Tax (40.8%) | Pre-tax equity flow | After-tax equity flow |
|---|---:|---:|---:|---:|---:|---:|
| 0 | | | | | −6,930,000 | −6,930,000 |
| 1 | 1,400,000 | 688,202 | 147,715 | 60,268 | 560,346 | 500,078 |
| 2 | 1,442,000 | 677,254 | 200,664 | 81,871 | 602,346 | 520,475 |
| 3 | 1,485,260 | 665,514 | 255,664 | 104,311 | 645,606 | 541,295 |
| 4 | 1,529,818 | 652,925 | 312,810 | 127,627 | 690,164 | 562,538 |
| 5 | 1,575,712 | 639,427 | 372,203 | 151,859 | 9,203,163 | 8,141,539 |

Sale: year-6 NOI \$1,622,984 / 9.00% = \$18,033,152 gross; \$17,492,158 net of 3%. Adjusted basis $= 16{,}830{,}000 - 5 \times 564{,}082 = \$14{,}009{,}588$. Gain \$3,482,570, of which \$1,618,269 is unrecaptured §1250 gain (28.8%) and \$1,864,301 is long-term capital gain (23.8%). Sale tax = **\$909,765**. Loan payoff \$9,025,053.

| | Pre-tax IRR | After-tax IRR | Share of return lost to tax |
|---|---:|---:|---:|
| Hotel, base | 12.63% | 9.27% | 26.6% |
| Treasury | 4.00% | 2.37% | 40.8% |

After-tax equity multiple, hotel base: 1.48x.

**Tax insight.** The hotel keeps 73% of its pre-tax return after tax; the Treasury keeps 59%. As a result the after-tax spread over Treasuries (690 bp) is 80% of the pre-tax spread (863 bp), not 59% of it. Depreciation, deferral, and capital-gains rates make the hotel more tax-efficient than a fully taxed coupon. The tax advantage is real, but it is not free: depreciation is partly recaptured at 28.8% on sale, and the shelter is only as good as the investor's ability to use passive losses.

### B.3 Scenarios

| Scenario | p | Pre-tax IRR | After-tax IRR | Gain on sale | Sale tax | Cash injection needed |
|---|---:|---:|---:|---:|---:|---:|
| Upside | 0.20 | 18.67% | 14.33% | 6,380,887 | 1,599,565 | 0 |
| Base | 0.45 | 12.63% | 9.27% | 3,482,570 | 909,765 | 0 |
| Downside | 0.25 | 4.50% | 3.08% | 946,207 | 272,508 | 0 |
| Severe | 0.10 | −6.39% | −4.46% | −1,128,999 | −268,702 (benefit) | 349,654 |

Expected after-tax IRR $= 0.20(14.33\%) + 0.45(9.27\%) + 0.25(3.08\%) + 0.10(-4.46\%) = $ **7.36%**. IRR of expected after-tax flows: **7.79%**. Expected pre-tax IRR 9.90%. Probability of an after-tax loss: 10%.

Against the Treasury's 2.37% after tax, the expected premium is about **5.0 percentage points a year**. In the downside case the hotel earns 3.08% after tax, only 71 bp above the Treasury, for five years of illiquid, levered operating risk.

In the severe case, year-1 NOI of \$490,000 does not cover \$839,654 of debt service. The investor must inject \$349,654, and year-1 DSCR is 0.58x. The \$1.07 million held back covers it, provided the lender does not also demand a cash sweep or reserve.

### B.4 Break-even exit caps (base NOI path)

* After-tax IRR equal to the Treasury (2.37%): exit cap **11.27%**.
* After-tax IRR equal to the Treasury plus 400 bp (6.37%): exit cap **9.88%**.

### B.5 Duration and inflation

| Measure | Treasury | Hotel |
|---|---:|---:|
| Modified duration (5-year, 4%, semiannual) | 4.49 | |
| Price change for +100 bp | −4.49% | Asset −10.54%, equity −26.36% (cap 8.48% → 9.48%, debt fixed) |

The hotel equity behaves like an instrument with a cap-rate "duration" of about 26. Cap rates do not move one-for-one with Treasuries, so this is not a Treasury duration. It is the sensitivity to the variable that matters most for the hotel's value.

High-inflation case (CPI 5%, NOI growth 5%, exit cap 10.0%): hotel after-tax IRR 9.44%, real 4.23%; Treasury after-tax 2.37%, real **−2.51%**. In the base 2.5% inflation case, the Treasury's after-tax real return is −0.13%. A fully taxed nominal Treasury held by a top-bracket investor does not preserve purchasing power at either inflation rate. TIPS would address inflation but not the tax drag.

### B.6 What the state exemption would be worth elsewhere

For a Texas resident, a 4.60% corporate bond yields 2.72% after federal tax against 2.37% for the 4.00% Treasury. For an otherwise identical investor in a hypothetical state with a 6% income tax, the same corporate bond yields 2.45% and the Treasury still yields 2.37%, because Treasury interest is exempt from state tax. The break-even corporate yield rises to 4.45%. (The calculation ignores the federal deductibility of state taxes, which the SALT cap limits.) **In Texas the exemption is moot; in a high-tax state it can decide a close comparison.**

### B.7 Recommendation (one defensible answer)

* The adviser's "8.5% versus 4%" is the wrong comparison. The right one is **7.4% expected after tax, with a 10% chance of loss and a 25% chance of roughly Treasury-like returns, versus 2.4% after tax, riskless and liquid.**
* A 5-point expected after-tax premium is a reasonable price for hotel risk *if* the hotel is a modest share of the investor's total wealth. At \$6.93 million of an \$8.0 million liquid pool, it is 87% of the investor's liquid capital in one illiquid, levered, operating asset. That fails a basic sizing test (Chapter 21), whatever the expected return.
* **Recommended:** do not buy this hotel outright with 87% of liquid capital. Either (a) take a smaller interest, for example a 25–40% LP share in a hotel partnership with an experienced operator, and hold the balance in Treasuries or T-bills, or (b) buy the hotel only if the \$8.0 million is a minority of total net worth, and hold at least \$1.0 million of reserve outside the deal.
* **Conditions for any hotel investment:** a current STR competitive-set report, a PCA and PIP review, a confirmed loan quote, and a tax adviser's confirmation of passive-activity treatment.
* **Walk away if:** the exit cap needed for a 400 bp after-tax premium (9.88%) is below the investor's own downside exit assumption, or the lender's terms push year-1 DSCR below 1.40x.

**What would change the conclusion.** A Treasury yield materially above 4%, which raises the bar. A cost-segregation study and bonus depreciation, which raise after-tax hotel returns but increase recapture exposure. A larger total net worth, which makes the concentration acceptable. An operating partner whose track record narrows the downside.

---

## Mode C — Blind examination

Use only the Case facts section. Allow 90 minutes.

1. (5 pts) Explain why "8.5% cap versus 4% Treasury" is not a valid comparison.
2. (10 pts) Compute the loan payment, annual debt service, year-1 DSCR, and the balance after five years.
3. (10 pts) Compute the depreciable basis and annual depreciation under the stated assumptions.
4. (15 pts) Build the base-case pre-tax and after-tax equity flows and IRRs.
5. (10 pts) Compute the sale gain, its split into unrecaptured §1250 gain and capital gain, and the tax.
6. (10 pts) Compute the Treasury's after-tax return and the share of each investment's return lost to tax. Explain the difference.
7. (10 pts) Run the four scenarios. Report the expected after-tax IRR and the IRR of expected flows, and explain why they differ.
8. (10 pts) Compare price sensitivity (duration) and inflation exposure.
9. (10 pts) State what the Treasury's state-tax exemption is worth to this investor, and to an investor in a 6% state.
10. (10 pts) Make a recommendation that addresses sizing and liquidity.

Answers: Mode B and `case_F_rubric.md`.

---

## Mode D — Investment committee

The investor has convened a family committee: the investor, a spouse who is a CPA, an adult child who works in hotel management, and the adviser. Each answer must be under 150 words and supported by a number.

1. **"The hotel yields twice what Treasuries do."** Answer the adviser.
2. **What does the CPA need to confirm?** Name the three tax assumptions that move the after-tax IRR most.
3. **What does a 2020 look like?** Quantify the severe scenario's cash call and the DSCR.
4. **How illiquid is this?** If the investor needs \$3 million in year 2, what happens under each alternative?
5. **Is this an inflation hedge?** Use the high-inflation case.
6. **Is the 7% fixed-rate loan a good idea?** What happens at 50% LTV? (Directional answer acceptable; quantify if you can.)
7. **Why not Treasuries plus a small hotel interest?** Compare concentration.
8. **What is the probability-weighted cost of being wrong?** Use the scenario table.
9. **What would make Treasuries clearly better?** Give a yield level or a scenario.
10. **What is the decision, and what would reverse it?**

Model answers are in `case_F_rubric.md` (§Mode D).
