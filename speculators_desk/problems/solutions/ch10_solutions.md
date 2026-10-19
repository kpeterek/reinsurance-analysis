# Chapter 10 Solutions

Numerical results are verified in `tests/test_ch10_examples.py`. Figures are rounded for display only. All inputs are hypothetical [HYPOTHESIS].

---

### Solution 10.1
| Event | Classification | What would change it |
|---|---|---|
| (a) DSCR below cash-management trigger | (i) None. It triggers cash management (a lockbox springs, excess cash is trapped), not recourse | A covenant making the trigger an event of default with recourse, which is unusual |
| (b) Maturity default, no refinancing | (i) None. This is the risk the lender priced. The lender's remedy is the property | A partial-recourse or payment guarantee; a "carry" guarantee covering interest until foreclosure |
| (c) Rents paid to an affiliate after default | (ii) Loss recourse for misapplied rents, in the amount diverted | If the documents treat diversion as a springing event (some do), (iii) |
| (d) Unpermitted transfer of 49% | (iii) Springing full recourse, if the transfer restriction covers indirect interests at that level | Many loans permit transfers below a threshold (e.g., less than 49% or without change of control) or to pre-approved transferees. Read the definition of "Permitted Transfer" |
| (e) Voluntary bankruptcy to stop foreclosure | (iii) Springing full recourse | Only if the documents or the jurisdiction make the provision unenforceable, a legal question outside this book |
| (f) Contamination discovered after default | (ii) Liability under the environmental indemnity for losses and remediation costs | Pre-existing contamination disclosed in the lender's own Phase I at origination may be excluded |

**Why net worth matters.** Carve-outs work only if the guarantor can pay. Their purpose is to make obstruction and theft costly at the moment equity is underwater, when the borrower's own entity has nothing to lose (Example 10.8: \$5.16 million deficiency against a \$0.78 million option). A guarantor with no assets turns the carve-out into a formality, so lenders test net worth and liquidity at closing and as ongoing covenants.

### Solution 10.2
* LTV: $0.65 \times 30{,}000{,}000 = \$19{,}500{,}000$.
* DSCR: $1{,}800{,}000/1.25 = 1{,}440{,}000$ of debt service; $1{,}440{,}000/0.075 = \$19{,}200{,}000$.
* Debt yield: $1{,}800{,}000/0.09 = \$20{,}000{,}000$.

Maximum loan \$19,200,000; DSCR binds. Mental route: $1.8/1.25 = 1.44$; $1.44/0.075 = 19.2$. Check against the crossover rule: $c = 6\%$, so DSCR binds iff $K > 0.06/(0.65 \times 1.25) = 7.38\%$. $7.50\% > 7.38\%$. ✓

### Solution 10.3
(a) Unhedged: $20{,}000{,}000 \times (0.0525 + 0.035) = \$1{,}750{,}000$. Capped: $20{,}000{,}000 \times (0.04 + 0.035) = \$1{,}500{,}000$. Cap payout: $20{,}000{,}000 \times (0.0525 - 0.04) = \$250{,}000$ a year.
(b) With cap $1{,}650{,}000/1{,}500{,}000 = 1.10x$; without $1{,}650{,}000/1{,}750{,}000 = 0.94x$.
(c) Sized at strike + spread = 7.50%: 1.10x. The property now earns exactly the sizing DSCR. Any NOI decline, or the cap's expiry, takes coverage below the sizing level.

### Solution 10.4
(a) IO: $12{,}000{,}000 \times 0.07/12 = \$70{,}000$ a month (\$840,000 a year). Amortizing: $PMT = 12{,}000{,}000 \times 0.0058333/(1 - 1.0058333^{-300}) = \$84{,}813.50$ a month (\$1,017,762 a year).
(b) Sixty amortizing payments (months 25–84) on the original schedule: $B = \$10{,}939{,}458$.
(c) Amortizing from month 1, the balance at month 84 is \$10,400,157. The IO period raises the balloon by \$539,302.
(d) HP-12C: `f CLEAR FIN`, `12000000 PV`, `7 g 12÷`, `25 g 12×`, `PMT` (−84,813.50), `60 n`, `FV` → −10,939,458.29.

Interpretation: the borrower gains \$177,762 a year of cash flow in years 1–2 and repays \$0.54 million less principal by maturity. The lender is relying more on refinancing.

### Solution 10.5
(a) Senior 0–60%; mezz 60–75%; pref 75–85%; common 85–100%.
(b) Senior DS $= 48{,}000{,}000 \times 0.0625 = \$3{,}000{,}000$; DSCR 1.60x. Mezz DS $= \$1{,}440{,}000$. Combined DSCR $= 4{,}800{,}000/4{,}440{,}000 = 1.081x$. NOI / (senior + mezz) $= 4{,}800{,}000/60{,}000{,}000 = 8.00\%$.
(c)

| Tranche | Loss at \$64m (−20%) | Loss at \$56m (−30%) |
|---|---|---|
| Senior | 0 | 0 |
| Mezz | 0 | \$4.0m (33%) |
| Pref | \$4.0m (50%) | \$8.0m (100%) |
| Common | \$12.0m (100%) | \$12.0m (100%) |

(d) Mezz: impaired beyond a 25% decline, wiped out at 40%. Pref: impaired beyond 15%, wiped out at 25%.

The combined DSCR of 1.08x means an NOI decline of 7.5% stops current mezz interest from being covered. Price the mezz on the probability of that NOI decline, not only on the 25% value cushion.

### Solution 10.6
(a) Project IRR 11.21%; investor IRR 10.75%; promote \$620,492, all paid from the year-5 flow.
(b) Project IRR 7.28%, below the 8% hurdle. Investor IRR 7.28%; promote \$0.
(c) A \$5.0 million fall in the final flow cuts project profit by \$5.0 million but cuts the GP's promote from \$620,492 to zero and leaves it there however much lower the outcome goes. The promote's payoff is zero below a threshold and rising above it: a call. Call values increase with volatility. A GP whose promote is near or out of the money gains from riskier strategies, while the LPs bear the downside. Remedies: hurdles with clawback, multiple-based tests, larger GP co-invest, and LP consent rights over leverage and major capital decisions.

### Solution 10.7
(a) Eleven caplets (periods 2–12). Premium **\$1,000,378**, 2.50% of notional, 89.2 bp a year.
(b) At 4.50%: **\$403,945**, 1.01% of notional, 36.0 bp a year.
(c) At 3.50%: sizing rate 6.50%; $L = 3{,}000{,}000/1.15/0.065 = \$40{,}133{,}779$. At 4.50%: sizing rate 7.50%; $L = \$34{,}782{,}609$.
(d) The lower strike costs \$596,434 more and supports about \$5.35 million more proceeds under the DSCR test. If the borrower needs the proceeds (an LTV or LTC limit does not bind first), the expensive cap buys leverage at a marginal cost of about 11% of the extra proceeds, paid up front. If the borrower does not need the proceeds, the cheaper cap gives the same protection against extreme rates at a 1.00 percentage-point higher worst-case coupon. The answer depends on (i) whether DSCR binds, (ii) the borrower's liquidity for the premium, (iii) its view of where SOFR will settle versus the forward (a view the cap market already prices), and (iv) whether the lender requires the same strike for extensions.

### Solution 10.8
Fair unit price $= 6{,}000{,}000/100 = \$60{,}000$. Book price \$250,000.

| Rule | LP new units | GP share | GP stake (post-call \$10.0m) |
|---|---|---|---|
| Both fund at fair value | 53.33 (GP buys 13.33) | 20.00% | \$2,000,000 for \$800,000 paid; net \$1,200,000 |
| LP funds all, fair value | 66.67 | 12.00% | \$1,200,000 |
| LP funds all, fair value, 125% credit | 70.00 | 11.76% | \$1,176,471 |
| LP funds all, book price | 16.00 | 17.24% | \$1,724,138 |
| LP funds all, book price, 125% credit | 16.80 | 17.12% | \$1,712,329 |

(c) At fair value with no penalty, the GP is indifferent: \$1.2 million net either way. With a 125% credit, not funding costs the GP \$23,529, a mild incentive to fund. Under book-value pricing, the GP is better off **not** funding by \$524,138 (or \$512,329 with the penalty), and the LP transfers that amount to the GP by funding. The LP should not fund under the book-value clause without amending it to fair-value pricing (with a valuation mechanism) or a much larger punitive multiple, or should fund the gap as a priority loan or preferred interest instead of common units.

### Solution 10.9
(a) Using `cre.distressed_loan_recovery(14_000_000, scenarios, 0.15)`:

| Resolution | Net | PV at 15% | Annualized return at \$14.0m |
|---|---|---|---|
| Mod + payoff | \$17,800,000 | \$13,459,357 | 12.76% |
| DPO | \$15,350,000 | \$13,347,826 | 9.64% |
| Foreclosure | \$14,600,000 | \$11,039,698 | 2.12% |

Expected PV = **\$12,458,034**; NPV at the ask = **−\$1,541,966**.
(b) The first two scenarios contribute \$8,042,155 of expected PV. Break-even requires the foreclosure scenario to contribute \$5,957,845, i.e., a PV of \$14,894,612, a net recovery of \$19,698,125, and a gross recovery of **\$21,098,125**. That exceeds par and the stated value. It is not plausible.
(c) Pass at \$14.0 million. A bid at or below \$12.46 million (69.2% of par) meets the target, if your scenarios are right. Before bidding, test the foreclosure timeline (judicial versus non-judicial state), the property value, and the borrower's capacity to pay a DPO; the foreclosure scenario dominates the outcome. If those cannot be verified, abstaining is the correct decision.

### Solution 10.10 — Rubric (Level 5; abstention is the expected best answer at the stated terms)

Illustrative numbers (assumptions stated): cap rates 6.00–6.50% on NOI are [HYPOTHESIS] for this exercise, not market data.

| Value basis | Value | Pref attachment (38.0/V) | Detachment (44.0/V) |
|---|---|---|---|
| Sponsor's "appraisal" | \$44.0m | 86.4% | 100.0% |
| T-12 NOI \$2.55m at 6.00% | \$42.5m | 89.4% | 103.5% |
| T-3 NOI \$2.35m at 6.25% | \$37.6m | 101.1% | 117.0% |
| T-3 NOI \$2.35m at 6.50% | \$36.2m | 105.1% | 121.7% |

If the cap strike were 4.00% (not disclosed; an assumption), the extension test rate is 7.40%, senior interest \$2,812,000, and DSCR is 0.84x on T-3, 0.91x on T-12, and 1.10x even on the sponsor's "stabilized" \$3.1 million, all below 1.15x. On T-3 NOI the loan that passes the test is about \$27.6 million, so the extension would need a paydown of about \$10.4 million. Cash after senior interest and a 13% current pref on T-3 NOI: −\$1,242,000 a year.

Score each dimension 0–4. A strong answer scores at least 3 on each.

| Dimension | Strong answer includes |
|---|---|
| Attachment | Shows the pref attaches near or above 100% of value on current NOI, so it is equity risk, not credit. Recognizes that a "1.6x multiple floor" is worthless if the claim sits above value |
| Contradictions | "Stabilized" \$3.1m versus T-3 \$2.35m (falling, not stabilizing); appraisal withheld until commitment; extension DSCR test likely failed on any NOI; cap strike and cost not disclosed; insurance "pending"; "most" LPs funding implies some are not, which means dilution terms and possibly a GP that cannot fund |
| Information required | The appraisal and its NOI and cap rate; the loan agreement's extension conditions and cap requirement; a cap quote; trailing 12 monthly operating statements and rent roll; insurance quote; the capital call status and JV dilution clause; the senior lender's written position on extension; the sponsor's sources and uses for the \$6.0m |
| Decision | Decline to commit by Tuesday. State the conditions for re-engagement: senior lender's signed extension or modification terms, a paydown funded by existing equity that lowers attachment below about 80% of a supportable value, control rights, and a price set on the T-3/T-12 NOI rather than the sponsor's model |
| Process | Rejects the artificial deadline as a negotiating device; notes that urgency is the sponsor's problem, not the investor's; records the decision and invalidation criteria |

Deduct 2 points for treating the sponsor's appraisal as fact, 2 for ignoring the extension test, and 3 for committing without the loan documents.

---

## Decision exercise (§10.10) — Ridgeview rubric

Key numbers (all verified in tests): replacement cap at a 3.00% strike \$888,370 (Example 10.3); cure paydown \$2,000,000 (Example 10.7); after the paydown the loan is \$28.0 million and the pref's claim runs from \$28.0 million to \$33.0 million of value, i.e., from 103.7% to 122.2% of a \$27.0 million value. In Example 10.8's one-year states (\$33.0m / \$27.0m / \$21.0m), the pref is repaid in full only in the \$33.0 million state (probability 0.30), and before costs of sale. The note at 80 has a negative NPV at 12% (−\$1.84 million; Example 10.10).

| Dimension (0–4 each) | Strong answer |
|---|---|
| Uses of funds | Separates value-creating uses (renovation with measured rent premiums) from option-preserving uses (cap, cure paydown) |
| Attachment | Computes that the pref attaches above current value; prices it as equity, not credit |
| Note alternative | Values the note below the ask at a 12% target; explains why the bank may still not sell lower (extend and pretend) |
| Conditions | Specifies what would make either investment acceptable: signed extension terms, larger paydown from existing equity, control rights, verified renovation premiums |
| Decision | States invest or abstain, with invalidation criteria. Abstention at the proposed terms is the expected answer; a strong "invest" answer restructures the terms rather than accepting them |

Minimum passing: 14 of 20, with no zero on Attachment.
