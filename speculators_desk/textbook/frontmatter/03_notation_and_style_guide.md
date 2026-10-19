# Notation, Mathematical Conventions, and Editorial Style Guide

This guide is binding on every chapter, case, drill, and model. When a chapter departs from it, the chapter must say so at the point of departure.

## 1. Units and number formats

| Quantity | Convention | Example |
|---|---|---|
| Rates in prose | percent with up to two decimals | 6.25% |
| Rates in equations and code | decimals | $c = 0.0625$ |
| Rate changes | basis points (bp); 1 bp = 0.0001 | +150 bp |
| Money | U.S. dollars unless stated; \$ thousands written as \$000 | \$8.0 million; \$1,234,567 |
| Time | years unless stated; months written explicitly | 18 months = 1.5 years |
| Hotel keys | "rooms" = keys available for sale | 96 rooms |
| Per-key | value or cost divided by rooms | \$62,500/key |

Rounding: carry full precision through calculations; round only the displayed result. Display money to the nearest dollar in exhibits and to three significant figures in prose (\$6.17 million). When rounding changes a decision at the margin, say so.

## 2. Symbols

| Symbol | Meaning |
|---|---|
| $V$ | asset value (market value unless qualified) |
| $P$ | price paid (may differ from $V$) |
| $NOI_t$ | net operating income in year $t$, **after** replacement reserves unless stated |
| $c$, $c_0$, $c_T$ | capitalization rate; going-in; terminal/exit |
| $k$ | required unlevered total return (discount rate) |
| $g$ | growth rate of NOI |
| $L$ | loan amount; $B_t$ balance at end of period $t$ |
| $r$ | nominal annual interest rate; $i = r/m$ periodic rate with $m$ payments per year |
| $n$ | number of periods (amortization term in months unless stated) |
| $DS$ | annual debt service |
| $K$ | loan constant (annual debt service per \$1 of loan) |
| $E$ | equity |
| $y$ | bond yield to maturity |
| $D_{mac}$, $D_{mod}$ | Macaulay and modified duration (years) |
| $C$ | convexity (years²) |
| $p$ | probability; $p^*$ break-even probability |
| $\mu$, $\sigma$ | mean and standard deviation of returns |
| $S$, $F$, $K_{opt}$ | spot, futures/forward, option strike |
| Occ, ADR, RevPAR | occupancy (decimal), average daily rate, revenue per available room |

## 3. Timing conventions

1. Period 0 is today. Cash flow $CF_0$ is not discounted.
2. Annual property cash flows occur at year-end unless a chapter states mid-year convention.
3. Mortgage payments are monthly in arrears at $i = r/12$ — the U.S. commercial convention. The effective annual rate is $(1 + r/12)^{12} - 1$, and it is higher than $r$.
4. Reversion (sale) value at the end of year $T$ is computed from **forward** NOI, $NOI_{T+1}$, capitalized at $c_T$, less selling costs. If a chapter uses trailing NOI it must say so.
5. IRR computed on annual flows is an annual rate. IRR on monthly flows is a monthly rate that must be annualized as $(1+IRR_m)^{12}-1$.
6. Excel `NPV(rate, range)` discounts the first cell by one period. We always write `=CF0 + NPV(rate, CF1:CFn)`.

## 4. Sign conventions

* Investor outflows are negative and inflows positive in cash-flow vectors.
* Python functions return **positive** payment amounts. Excel `PMT` returns a negative number when principal is entered as positive; we enter `-principal` so that Excel also shows a positive payment.
* Long position: side = +1; short: side = −1. P&L = side × (exit − entry) × multiplier × contracts.
* FX pairs are BASE/QUOTE. EUR/USD 1.10 means one euro costs 1.10 dollars. P&L on a BASE position is earned in QUOTE currency.

## 5. Hotel accounting conventions (USALI-style)

* Room revenue excludes hotel occupancy taxes.
* **GOP** = total revenue − departmental expenses − undistributed operating expenses.
* **EBITDA** (as used here) = GOP − management fees − franchise fees − property taxes − insurance (and ground rent if any). It is before the FF&E reserve.
* **NOI** = EBITDA − FF&E reserve. The reserve is stated as a percentage of total revenue (typically 4% in this book unless the franchise or loan documents specify otherwise).
* A valuation states which line it capitalizes. "8.5% cap on NOI after a 4% reserve" is complete. "8.5% cap" is not.

## 6. Evidence labels

Historical and empirical statements carry one of four labels where there is any risk of confusion:

| Label | Meaning |
|---|---|
| **[FACT]** | Documented in a cited source listed in `SOURCE_REGISTER.md` |
| **[INFERENCE]** | A reasonable conclusion drawn from documented facts; the reasoning is shown |
| **[HYPOTHESIS]** | An illustrative assumption, model parameter, or hypothetical case value |
| **[SPECULATION]** | A view that cannot presently be tested |

All hypothetical case numbers are [HYPOTHESIS] by construction. Each case states this once in its header instead of tagging every number. Market "typical ranges" (for example, cap rates for limited-service hotels) are assumptions for teaching unless a dated source is cited.

Verification status of each source: `VERIFIED-PRIMARY`, `VERIFIED-SECONDARY`, `PENDING`. Do not present a `PENDING` figure as established. Mark it in the text with *(verification pending)*.

## 7. Chapter template

Each chapter follows this order. Headings can be renamed, but every element must be present.

1. Learning objectives
2. Opening investment problem
3. Economic intuition (before any equation)
4. Technical definitions
5. Equations and derivations
6. Worked examples (at least three, fully computed, each with a "Decision consequence" paragraph)
7. CRE application
8. When the relationship fails
9. Historical episode (sourced, with evidence labels)
10. Decision exercise
11. Frequent analytical errors
12. Connections to other chapters
13. One-page reference sheet
14. End-of-chapter problems (ten, Levels 1–5) → `problems/questions/`
15. Solutions with intermediate steps → `problems/solutions/`

## 8. Worked-example format

```
Example N.k — Title
Given:      every input with units
Find:       the quantities required
Solution:   formula → substitution → intermediate results → result
Check:      an independent check (reverse calculation, bound, or code reference)
Decision consequence: what changes in the investment decision and why
Reproduce:  tests/test_chNN_examples.py::test_example_N_k
```

## 9. Prose rules

* State the intuition first, then show the mathematics, then give the economic consequence.
* No motivational language, no slogans without derivations, no "the market always…".
* Every claim of an empirical regularity carries a source or the label [HYPOTHESIS].
* Do not write "obviously" or "simply". If it were obvious, it would not need to be written.
* Prefer short declarative sentences. Use tables for comparisons. Use lists only for genuinely parallel items.
* For judgment questions, give the decision **rubric** and say what would change the answer. Do not give a single "correct" trade unless the problem is objectively determinate.

## 10. Problem difficulty levels

| Level | Description | Typical time |
|---|---|---|
| 1 | Conceptual foundations | 2–5 min |
| 2 | Fast mental arithmetic | 30 s – 2 min |
| 3 | Multistep calculation | 10–15 min |
| 4 | Applied investment decision | 15–30 min |
| 5 | Ambiguous, incomplete information; professional judgment | 30–60 min |

## 11. Drill categories

A: 30-second mental calculation · B: 2-minute market interpretation · C: 5-minute investment decision · D: 15-minute underwriting · E: 30-minute ambiguous scenario · F: full investment committee case.
