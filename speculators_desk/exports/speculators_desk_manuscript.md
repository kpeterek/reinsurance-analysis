*The Speculator's Desk — Commercial Real Estate, Global Macro, Market Intelligence, and the Art of Decision-Making Under Uncertainty*




# Preface and How to Use This Book

## Who this book is for

This book assumes you already underwrite. You can build a pro forma, read a T-12, and size a loan. You have sat through a broker's opinion of value and know which assumptions carry it. You have passed probability and financial mathematics examinations. You do not need finance explained from first principles. What you need is the bridge from **valuing an asset** to **making speculative decisions about it**: deciding when to buy, sell, hedge, or wait, and how much to commit, in markets where prices move on expectations, financing, and positioning as much as on fundamentals.

A superior analyst of value is not automatically a profitable speculator. Underwriting tells you what an asset is worth to a buyer with stated assumptions. Speculation also asks:
* Who is the marginal buyer, and what must they believe at today's price?
* What is already priced, and what new information would change the price?
* What forces a counterparty to transact, and on what timeline?
* How will financing conditions change the set of buyers who can close?
* What is the catalyst, and what evidence would show the thesis is wrong?
* How much can be committed without risking survival?

Every chapter returns to these questions.

## How the book is organized

Part I defines speculation and price formation. Part II builds macroeconomic intelligence: the business cycle, central banks, fixed income, and global capital. Part III, the longest, treats commercial real estate as a speculative asset, with hotels as the high-beta case. Part IV extends the toolkit to equities, FX, commodities, credit, derivatives, and alternative assets, comparing each with CRE. Part V covers probability, risk management, and quantitative market intelligence. Part VI uses financial history as a laboratory. Part VII turns everything into a professional decision process.

## How to read a chapter
1. Attempt the opening investment problem before reading. Write your answer down.
2. Read the intuition section. Then work the equations yourself.
3. Work each example **by hand first**: notebook, financial calculator, graph paper. Then reproduce it in Excel. Then read the Python test that verifies it. The order matters. Software should confirm your reasoning, not replace it.
4. Do the decision exercise in writing, using the templates in `desk/`.
5. Do the ten problems. Levels 1–3 have one correct answer. Levels 4–5 are scored by rubric, and some have several defensible answers. For some, abstention is the best answer.
6. Record your mistakes in the error log (`desk/trade_journal/error_log_template.md`). The simulator also tracks them.

## Evidence discipline

The book labels claims:
* **[FACT]**: documented, with a source in `SOURCE_REGISTER.md`.
* **[INFERENCE]**: a reasoned conclusion from facts.
* **[HYPOTHESIS]**: an assumption, model parameter, or hypothetical case value.
* **[SPECULATION]**: a view that cannot presently be tested.

Hypothetical cases are labeled at the top. Cap rates, PIP costs, insurance quotes, and tax rates in the cases are teaching assumptions, not market data. Where a historical figure could not be verified during production, the text says *(verification pending)* rather than presenting it as fact.

## What the book will not do
It will not tell you that a pattern "always" works, give you trading slogans, or imply that simulated profits show skill. It will show you the arithmetic, the mechanisms, the history, and the decision process. It will make you argue for your positions against hostile questions.


\newpage

# The Speculator's Desk — Definitive Table of Contents

*Commercial Real Estate, Global Macro, Market Intelligence, and the Art of Decision-Making Under Uncertainty*

Planned share of the book: CRE and hotels about 40%, macro and rates about 20%, quantitative methods and risk about 20%, other markets and derivatives about 12%, history and desk operations about 8%. Part III is deliberately the longest part.

File naming: `textbook/part_NN_<slug>/chNN_<slug>.md`. Problems: `problems/questions/chNN_problems.md`. Solutions: `problems/solutions/chNN_solutions.md`. Status values are maintained by `scripts/progress.py` and shown in `PROGRESS.md`.

## Front Matter
- 00 Preface and How to Use This Book (`frontmatter/00_preface.md`)
- 01 Table of Contents (this file)
- 02 Competency Map (`frontmatter/02_competency_map.md`)
- 03 Notation and Style Guide (`frontmatter/03_notation_and_style_guide.md`)

## Part I — The Anatomy of Speculation
| Ch | Title | Core calculation threads |
|---|---|---|
| 1 | What Is Speculation? | Expected vs realized return, break-even probability, the cost of immediacy, volatility drag, arbitrage with leg risk |
| 2 | The Price Formation Process | Bid/ask economics, appraisal smoothing (unsmoothing filter), stale-comp bias, auction clearing |
| 3 | The Speculator's Mental Models | Bayesian updating, reflexive collateral loops, forced-selling price impact, option value of waiting |

## Part II — Macroeconomic Intelligence
| Ch | Title | Core calculation threads |
|---|---|---|
| 4 | The Business Cycle | Surprise indices, recession base rates, the Sahm-type rule, transmission to NOI |
| 5 | Central Banks and Monetary Policy | Taylor-type rules, implied probabilities from fed funds futures, real rates, transmission to cap rates |
| 6 | Fixed Income and the Cost of Capital | Bond pricing, duration, convexity, DV01, carry and roll-down, cap-rate/Treasury spread, duration of levered CRE equity |
| 7 | Fiscal Policy, Sovereign Risk, and Global Capital | Debt dynamics, sovereign spreads, FX-hedged yields for foreign CRE buyers |

## Part III — Commercial Real Estate as a Speculative Asset (core)
| Ch | Title | Core calculation threads |
|---|---|---|
| 8 | The Fundamental Economics of CRE | NOI construction, operating leverage, absorption, reassessment, reserves, property-type comparison |
| 9 | CRE Valuation and Mispricing | Direct cap, DCF, loaded cap rates, residual land, sensitivity grids, anchoring cases |
| 10 | Capital Structure, Debt, and Equity | Loan sizing (LTV/DSCR/DY), amortization, balloons, rate caps, mezz/pref, waterfalls, refinancing gaps |
| 11 | Hotels — The High-Beta CRE Asset | ADR/Occ/RevPAR, USALI P&L, fees, FF&E, PIPs, flow-through, eight full hotel cases |
| 12 | CRE Cycles and Distressed Opportunity | Maturity walls, loan sales, foreclosure timelines, CMBS, REIT-implied cap rates |
| 13 | CRE Trading and Portfolio Strategy | Hold/sell/refi analysis, real options, hedging rate exposure, liquidity reserves |

## Part IV — The Other Speculative Markets
| Ch | Title | Core calculation threads |
|---|---|---|
| 14 | Equities and Equity Index Futures | Earnings yield vs real yield, ERP, futures notional and margin, beta hedging |
| 15 | Foreign Exchange | Quote conventions, CIP, carry P&L, hedged returns on foreign property |
| 16 | Commodities | Cost of carry, roll yield, contango/backwardation, inventory economics |
| 17 | Credit and Financial Distress | Hazard rates, spread ≈ PD × LGD, recovery waterfalls, CMBS tranches |
| 18 | Derivatives, Volatility, and Convexity | Payoffs, Black–Scholes, Greeks, delta hedging P&L, interest-rate caps for floating CRE debt |
| 19 | Alternative and Emerging Speculative Assets | Comparative framework vs CRE: cash flow, anchors, liquidity, reflexivity |

## Part V — Quantitative Trading and Risk
| Ch | Title | Core calculation threads |
|---|---|---|
| 20 | Probability and Statistical Decision-Making | Bayes, base rates, calibration, scenario trees, decision theory |
| 21 | Risk Management and Position Sizing | VaR/ES, Kelly and fractional Kelly, drawdown math, ruin, margin and liquidity stress |
| 22 | Quantitative Market Intelligence | Returns, regressions, rolling correlation, cointegration, backtest hygiene |

## Part VI — Financial History as a Laboratory
| Ch | Title |
|---|---|
| 23 | Historical Speculative Episodes (1929; 1970s inflation; Volcker; 1987; Japan 1990s; ERM 1992; bonds 1994; Asia 1997; LTCM 1998; 2000; 2007–09; 2020; 2022; post-2020 office; 1980s–90s Texas/RTC CRE cycle) |

## Part VII — The Investment Decision
| Ch | Title |
|---|---|
| 24 | Professional Trading and Investment Judgment |
| 25 | The Speculator's Desk (daily process, templates, postmortems) |

## Appendices
- A. Formula Compendium (`appendices/A_formula_compendium.md`)
- B. Financial Calculator Keystrokes (HP-12C / BA II Plus)
- C. Excel Function Map and Sign Conventions
- D. Data Sources and Their Quality (FRED/ALFRED, BLS, BEA, CFTC, CME, FDIC, SEC EDGAR, NCREIF/Nareit, STR-type data)
- E. Glossary
- F. Legal and Ethical Information Boundaries (MNPI, confidentiality)

## Cases (`cases/`)
Hypothetical (each with Modes A–D and a separate rubric): A Overpriced Hotel Owner · B Refinancing Cliff · C Cap Rate Expansion and Equity Destruction · D Hotel PIP Negotiation · E Distressed Office Acquisition · F Hotel versus Treasury · G Buying the Debt · H Cross-Asset Macro Shock · I Development Land Option · J Credit Crunch Hotel Acquisition.

Historical: one file per Chapter 23 episode, using the fact/inference/hypothesis/speculation labeling standard.


\newpage

# Competency Map

There are ten competencies, each with observable behaviors at three levels. **Foundation** is the minimum for leaving Week 4. **Practitioner** is the target for Week 10. **Professional** is the target at the capstone.

Objective calculation items must reach about 85% accuracy before the drill engine raises difficulty. Judgment items are scored on the reasoning rubric in `training/curriculum/reasoning_rubric.md`, not on whether a hypothetical trade "made money".

Scores here measure analytical skill on curated problems. They do **not** certify real-market trading ability, and simulated P&L is never treated as evidence of skill.

| # | Competency | Foundation | Practitioner | Professional | Primary chapters |
|---|---|---|---|---|---|
| 1 | Financial mechanics | Computes NPV/IRR, loan payments, and balances by hand and in Excel with correct timing | Reconciles levered and unlevered returns and catches sign and timing errors in others' models | Builds a full model with explicit conventions that an IC member can audit in 10 minutes | 6, 9, 10, App. A–C |
| 2 | Macroeconomics | Explains growth and inflation regimes and reads major releases against consensus | Maps a data surprise into rates, FX, credit, and CRE financing with plausible magnitudes | Builds a falsifiable macro view with stated probabilities and the data that would change it | 4, 5, 7 |
| 3 | CRE valuation | Direct cap, DCF, and comps with stated NOI definitions | Normalizes messy operating statements, handles reassessment and PIPs, and builds sensitivity grids | Identifies what the marginal buyer must believe and prices disagreement with the seller | 8, 9, 11 |
| 4 | Financing and leverage | Sizes loans on LTV, DSCR, and debt yield and finds the binding constraint | Models refinancing gaps, rate caps, cash traps, and waterfalls | Designs a capital structure that survives the stress case and states sponsor and lender incentives | 10, 12, 17 |
| 5 | Market intelligence | Names sources and their timeliness, bias, and revisions | Separates what is priced from what is new and reconciles conflicting signals | Runs a weekly intelligence process with a decision log and source-quality grades | 2, 13 (sources), 22, 25 |
| 6 | Probabilistic reasoning | Expected value, Bayes, base rates | Builds scenario trees, break-even probabilities, and calibrated forecasts | Reasons with model uncertainty and knows when a probability estimate is not meaningful | 1, 3, 20 |
| 7 | Risk management | Drawdown math, VaR/ES definitions, position size from a stop | Kelly limits, correlated exposures, margin and liquidity stress | Portfolio-level stress across public and private assets, with survival as the binding constraint | 18, 21 |
| 8 | Historical analysis | Narrates mechanisms of major episodes with dates and sources | Separates ex-ante information from hindsight and labels evidence | Uses history to generate hypotheses and stress scenarios without treating analogues as laws | 23 |
| 9 | Thesis development | Writes a thesis with catalyst and invalidation | Contrasts the thesis with consensus and prices it | Presents a thesis to an IC, survives hostile questioning, and changes their mind on evidence | 24 |
| 10 | Investment judgment | Chooses among buy, sell, hold, hedge, and wait with explicit reasons | Includes abstention, opportunity cost, and timing in the choice | Makes defensible decisions under ambiguity and audits their own past decisions | 1, 13, 24, 25, capstone |

## Assessment schedule
* **Baseline** (Week 0): `training/weekly_exams/baseline_assessment.md` — diagnostic, ungraded.
* **Intermediate** (Week 8): mixed objective items plus one CRE case in Mode C.
* **Final** (Week 16): capstone plus a timed objective exam.

## Mastery gating used by the simulator
* Objective drills: a topic advances when the rolling accuracy over the last 10 attempts is at least 85%.
* Judgment drills: a topic advances when the mean rubric score over the last 5 attempts is at least 3.0 out of 4, with no zero on "risk and invalidation".


\newpage

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


\newpage


# Part I — The Anatomy of Speculation

## Chapter 1 — What Is Speculation?

> **Status:** Complete (v1.0). Numerical examples are reproduced in `tests/test_ch01_examples.py`. Problems are in `problems/questions/ch01_problems.md` and solutions in `problems/solutions/ch01_solutions.md`.

### Learning objectives

After this chapter you should be able to:

1. Classify a transaction as investment, speculation, arbitrage, hedging, or gambling by asking **what risk is being borne and who pays for bearing it**. The asset type does not decide the classification.
2. Separate expected return from realized return. Compute expected profit, dispersion, probability of loss, and the IRR of expected cash flows for a discrete scenario set, and explain why expected IRR and the IRR of expected cash flows differ.
3. Compute a **break-even probability** and use it to make decisions when probabilities are uncertain (Knightian uncertainty).
4. Price **immediacy**: compute the annualized rate a forced seller implicitly pays a liquidity provider, and judge whether that payment is compensation for risk or a genuine mispricing.
5. Show with arithmetic why a positive-expected-value position can still destroy capital when sized too large (volatility drag, ruin). Connect this to leverage in CRE.
6. Recognize "arbitrage" that is really speculation on execution, closing, or legging risk, and compute the minimum completion probability that justifies it.
7. Explain how information asymmetry (adverse selection) sets bid–ask spreads in securities and bid discipline in private real estate.
8. Judge decisions by their process rather than their outcome, and keep a decision record that makes that possible.

---

### 1.1 Opening investment problem: three opportunities on a Monday

You run a \$40 million discretionary real estate and markets account for a family office. On Monday morning three opportunities reach your desk. All facts below are [HYPOTHESIS] — a constructed teaching case.

**Opportunity A — the industrial building.** A broker offers a 100% leased, 140,000 sf warehouse in a Sun Belt metro at \$14.0 million. In-place NOI is \$875,000, a 6.25% going-in cap rate. The tenant has a seven-year remaining term with 3% annual bumps. A lender will provide 60% LTV at 6.50% on a 30-year amortization.

**Opportunity B — the hotel that must close.** A 110-room select-service hotel in a Texas secondary market is owned by an estate. The estate's \$6.1 million loan matures in 50 days and the lender has declined to extend. Your analysis, which Chapter 11 will teach you to replicate, says a patient, fully marketed sale would bring about \$9.0 million: trailing NOI after a 4% FF&E reserve of \$855,000, capitalized at 9.5%. The estate's broker says they will accept **\$7.8 million all cash with a 45-day close**, provided you waive most contingencies.

**Opportunity C — the "riskless" back-to-back.** A fund is selling a single-tenant net-leased retail building for \$5.0 million to close in 60 days. Separately, a 1031-exchange buyer has signed a letter of intent to buy the same building from you for \$5.4 million. The LOI is non-binding, and the buyer's deposit becomes non-refundable only after a 30-day inspection period that starts after your purchase. A junior colleague calls it "a \$400,000 arbitrage".

You also have the alternative every speculator always has: **do nothing**, hold Treasury bills, and wait.

By the end of the chapter you will be able to say what kind of activity each opportunity is, what you are being paid for, how much you could lose, and what you would need to believe to proceed. Section 1.10 returns to the decision.

---

### 1.2 Economic intuition: speculation is paid risk-bearing

The word *speculation* is used loosely, sometimes as an insult. Precise use matters because each activity requires a different analysis.

**Investment** in the narrow sense is the purchase of an asset whose expected return comes mainly from the **cash flows the asset produces**. The investor accepts the market's pricing of those cash flows. The warehouse in Opportunity A is an investment: you buy a 6.25% income stream with contractual growth, and most of your return over seven years is rent. You are not claiming the seller misjudged anything. You are accepting a market price for a risk you are willing to hold.

**Speculation** is taking a position whose expected return depends mainly on a **change in price**. That price change comes from one of three things: a change in expectations, the resolution of uncertainty, or the payment of a premium by someone who wants to shed risk or obtain immediacy. The speculator must answer a question the investor can partly avoid: *why is this price available to me?* Opportunity B is speculation. Its attraction is the gap between \$7.8 million today and \$9.0 million under patient marketing. That gap exists because the estate needs immediacy and you can supply it.

**Arbitrage** is the simultaneous purchase and sale of economically identical claims at different prices. When both legs are executed at once and settle against each other, it is riskless. True arbitrage is rare, small, and taken by those with the lowest transaction costs. Most of what is called arbitrage is **relative-value speculation**: positions in similar claims, or in identical claims that cannot be executed simultaneously. Opportunity C is a speculation on whether the second leg closes. Section 1.7 prices it.

**Hedging** is taking a position to reduce a pre-existing exposure. An owner of floating-rate hotel debt who buys an interest-rate cap is hedging. The hedger pays a premium in expected terms, and that premium is the speculator's compensation.

**Gambling** is taking risk in a game whose expected value to the participant is negative and which serves no risk-transfer function. The house edge is not compensation for bearing anyone else's risk. Gambling can also mean taking a positive-expected-value risk sized so that ruin becomes likely. Section 1.6 shows that the line between "speculation" and "gambling" often runs through position size, not through the asset.

#### Risk transfer: why speculators are paid at all

In a market without speculators, a hedger must find another hedger with the opposite exposure, of the same size, on the same day. A wheat farmer would need a miller who wants to buy exactly when the farmer wants to sell. A forced hotel seller would need a strategic buyer who happens to be ready in 45 days. Speculators fill the gaps in time and size. They are paid through:

1. **Risk premia.** Expected compensation for holding risks that others want to shed. Examples are the term premium on long bonds, the equity premium, the illiquidity premium on private real estate, and insurance premia on volatility.
2. **Liquidity premia (the price of immediacy).** Compensation for transacting when someone else needs to and you do not.
3. **Information and analysis premia.** Returns from forming more accurate expectations than the marginal price-setter, using legal, public, or self-generated information. Chapter 2 and Appendix F treat the legal boundaries.

These three sources must be distinguished in every decision. They behave differently under stress. Risk premia are earned on average and lost in bad states. Liquidity premia are earned when you have liquidity, and they disappear exactly when you need liquidity yourself. Information premia exist only to the extent your information is not already in the price.

#### Liquidity provision versus liquidity consumption

A **liquidity provider** stands ready to transact when others need to and is paid a spread or discount. A **liquidity consumer** demands immediate execution and pays for it. The same institution can be either, depending on the trade. A dealer quoting bonds provides liquidity. A fund meeting redemptions by selling the most liquid assets consumes it. In private real estate, buyers with committed capital, short closing periods, and the ability to waive financing contingencies provide liquidity. Sellers facing loan maturities, fund wind-downs, estate settlements, or partner disputes consume it.

The economic danger is that **liquidity provision is short a put on liquidity itself**. The provider earns small premia in normal conditions and suffers large losses when everyone wants immediacy at once. At those moments prices gap, financing disappears, and the provider's own capital is impaired. Section 1.9 examines 19 October 1987 from this perspective.

#### Expected return versus realized return

A position's **expected return** is a probability-weighted average across scenarios. Its **realized return** is what one draw from that distribution delivers. A good decision can produce a bad outcome, and a bad decision can produce a good one. In a single CRE deal held for five years you observe exactly one draw. You therefore cannot learn much about your skill from the outcome of one deal. You need a record of the **expected** distribution you underwrote, so that outcomes can later be compared with forecasts (Chapter 20 develops calibration).

#### Risk versus uncertainty

Frank Knight (1921) distinguished **risk**, where outcomes are random but the probabilities are knowable, from **uncertainty**, where the probabilities themselves are not known. A roulette wheel is risk. Whether a newly vacant suburban office tower re-leases within three years is uncertainty. There is no frequency table for that building, in that submarket, in that interest-rate regime.

Professional speculation operates mostly under uncertainty. Two tools make it tractable:

* The **break-even probability**: the probability of the bad state at which the decision has zero expected value. If your plausible range for that probability sits well below the break-even, the decision is robust to your ignorance. If the range straddles it, the decision hinges on a number you do not know. Either gather information or decline.
* **Scenario construction** with explicit mechanisms rather than statistical extrapolation. Chapter 20 develops this.

#### Information asymmetry

When one party knows more than the other, the less-informed party must protect itself. In securities, dealers widen spreads because some counterparties are better informed (Glosten and Milgrom, 1985). In private real estate, buyers shade bids and insist on due diligence because the seller knows about the roof, the franchise PIP, the tenant who has told the property manager they are leaving, and the property-tax protest that failed. Akerlof (1970) showed that when quality cannot be verified, good assets withdraw from the market and prices fall toward the value of bad ones. Due diligence is the purchase of information that closes the asymmetry, and its price is worth calculating (Example 1.7).

#### Process versus outcome

A professional speculator's unit of performance is the **decision**, not the trade. A decision is good if, given what was knowable at the time, the thesis was coherent, the expected value was positive after costs, the position was sized to survive adverse outcomes, and invalidation criteria were specified. Outcomes are feedback, but noisy feedback. The decision journal (Chapter 25 and `desk/trade_journal/`) records the forecast distribution *before* the outcome is known. Without it, hindsight rewrites what you thought.

---

### 1.3 Technical definitions

| Term | Definition |
|---|---|
| Expected value (EV) | $E[X] = \sum_s p_s x_s$ for discrete scenarios $s$ with probabilities $p_s$ summing to 1 |
| Standard deviation | $\sigma_X = \sqrt{\sum_s p_s (x_s - E[X])^2}$ |
| Probability of loss | $\sum_{s:\,x_s<0} p_s$ |
| Expected loss (partial expectation) | $\sum_{s:\,x_s<0} p_s x_s$, a negative number. Not the same as the average loss *given* a loss |
| Break-even probability | For a two-outcome decision with gain $G>0$ and loss $L>0$: $p^* = G/(G+L)$ is the probability of loss at which EV = 0 |
| Price of immediacy | The discount accepted to transact now rather than after an orderly process, expressed as an annualized rate over the time saved |
| Bid–ask spread | Ask minus bid. The half-spread is the expected revenue per trade to a market maker before adverse selection |
| Adverse selection | Losses to the less-informed party from trading disproportionately with better-informed counterparties |
| Arithmetic mean return | $\bar r = E[r]$ |
| Geometric (compound) growth rate | $g = \exp(E[\ln(1+r)]) - 1$. This is the growth rate of wealth for a repeated position |
| Volatility drag | $\bar r - g$. For small returns, approximately $\sigma^2/2$ |
| Kelly fraction | The fraction of wealth that maximizes $E[\ln(\text{wealth})]$ for a repeated bet. Chapter 21 explains why practitioners use less |
| Leg risk | The risk that one leg of a multi-leg trade executes and another does not, or does so at a worse price |
| Liquidity provider/consumer | A party supplying versus demanding immediacy |

---

### 1.4 Equations and derivations

#### 1.4.1 Expected profit and the IRR of expected flows

For a hold of $T$ years with scenario-dependent cash flows $CF_{s,t}$:

$$E[\text{Profit}] = \sum_s p_s \Big(\sum_{t=0}^{T} CF_{s,t}\Big).$$

There are two different "expected IRRs":

* **Expected IRR**: $\sum_s p_s \, IRR_s$, the probability-weighted average of scenario IRRs.
* **IRR of expected cash flows**: the IRR of the vector $E[CF_t] = \sum_s p_s CF_{s,t}$.

They are generally unequal because IRR is a nonlinear function of the cash flows. Neither is "the" expected return. The IRR of expected flows is the more defensible single number, because it applies the expectation to cash before the nonlinear transformation. The distribution of scenario IRRs is more informative than either average. Committees should see the full distribution, not just a point estimate.

#### 1.4.2 Break-even probability

Suppose a decision yields $+G$ with probability $1-p$ and $-L$ with probability $p$. Then

$$EV = (1-p)G - pL = 0 \;\;\Rightarrow\;\; p^* = \frac{G}{G+L}.$$

With more than two scenarios, fix the *relative* probabilities of the non-bad scenarios and solve for the bad-state probability $q^*$ that sets EV to zero:

$$EV(q) = (1-q)\,\bar G - q L = 0 \;\Rightarrow\; q^* = \frac{\bar G}{\bar G + L}, \qquad \bar G = \frac{\sum_{s \neq \text{bad}} p_s x_s}{\sum_{s\neq\text{bad}} p_s}.$$

Here $\bar G$ is the conditional expected profit given that the bad state does not occur.

#### 1.4.3 The annualized price of immediacy

A seller who sells now receives net proceeds $N_0$. Selling patiently yields expected net proceeds $E[N_\tau]$ after an expected delay of $\tau$ years, net of carrying costs incurred during the wait. The implied annualized rate the seller pays for immediacy is

$$r_{imm} = \left(\frac{E[N_\tau]}{N_0}\right)^{1/\tau} - 1.$$

Two cautions apply. First, $E[N_\tau]$ should include the probability that the patient sale fails. Second, a high $r_{imm}$ does not prove the buyer is getting a bargain. It may compensate the buyer for risks the seller is also avoiding: diligence waivers, information asymmetry, financing risk.

#### 1.4.4 Market-making with informed traders

A market maker quotes a half-spread $h$ around the value they expect. A fraction $\pi$ of incoming orders come from informed traders. After an informed trade, value moves by $\Delta$ against the market maker. Uninformed trades carry no information. Expected profit per trade is

$$E[\Pi] = h - \pi \Delta.$$

The competitive half-spread is $h^* = \pi\Delta$. Spreads widen when the share of informed flow rises or when information events are larger. This is why spreads widen ahead of data releases and in stressed markets. The CRE analog is the "diligence discount": the buyer's bid shading increases with the probability and size of undisclosed defects.

#### 1.4.5 Growth versus expectation: volatility drag

Repeatedly committing a fraction $f$ of wealth to a position with per-period return $r$ grows wealth at the rate

$$g(f) = E[\ln(1 + f r)].$$

For a two-outcome bet returning $+a$ with probability $p$ and $-b$ with probability $1-p$:

$$g(f) = p\ln(1+fa) + (1-p)\ln(1-fb).$$

Setting $g'(f) = 0$ gives the Kelly fraction

$$f^* = \frac{p}{b} - \frac{1-p}{a}.$$

For small $f r$, the expansion $\ln(1+x) \approx x - x^2/2$ gives $g(f) \approx f\mu - \tfrac{1}{2} f^2 (\sigma^2 + \mu^2)$. Growth is quadratic in size and turns negative beyond roughly $2f^*$. **The same positive-EV opportunity is an investment at one size and a path to ruin at another.**

#### 1.4.6 Leverage on equity returns

For an asset with total return $r_A$ financed with loan-to-value $\lambda$ at interest rate $r_D$, and ignoring amortization and transaction costs over one period:

$$r_E = \frac{r_A - \lambda r_D}{1-\lambda} = r_A + \frac{\lambda}{1-\lambda}(r_A - r_D).$$

Leverage scales both the spread $r_A - r_D$ and the dispersion of $r_A$ by $1/(1-\lambda)$. At 75% LTV, a 25% decline in asset value eliminates all equity. With non-recourse debt the equity return is floored at −100%. That floor is the limited-liability put. It raises the arithmetic mean of equity returns while compounded growth collapses (Problem 1.9).

#### 1.4.7 Arbitrage with leg risk

If leg two completes with probability $\pi$ and yields profit $G$, and failure leaves a loss $L$:

$$EV = \pi G - (1-\pi)L, \qquad \pi^* = \frac{L}{G+L}.$$

This is the break-even equation from the other side. It shows directly that an "arbitrage" with completion risk is a probabilistic bet.

---

### 1.5 Worked examples

All seven examples are reproduced in `tests/test_ch01_examples.py`.

#### Example 1.1 — Expected versus realized return on the hotel bid (Opportunity B)

**Given.** Purchase price \$7,800,000. Buyer closing costs 1.5% of price. All cash (unlevered), with leverage added in Chapter 10. Two-year hold. Selling costs 3% of gross sale price. Scenario NOI is after FF&E reserve, received at year-end. Sale at end of year 2.

| Scenario | Probability | NOI Y1 | NOI Y2 | Gross sale, end Y2 |
|---|---|---|---|---|
| Good: orderly market, modest RevPAR growth | 0.55 | \$780,000 | \$850,000 | \$9,400,000 |
| Base: flat market | 0.30 | \$760,000 | \$800,000 | \$8,600,000 |
| Bad: new supply plus a regional slowdown | 0.15 | \$650,000 | \$560,000 | \$6,400,000 |

**Find.** Profit and IRR in each scenario; expected profit, standard deviation, probability of loss; expected IRR and IRR of expected flows.

**Solution.**

All-in basis $= 7{,}800{,}000 \times 1.015 = \$7{,}917{,}000$.

Net sale proceeds $=$ gross $\times 0.97$:

* Good: $9{,}400{,}000 \times 0.97 = \$9{,}118{,}000$
* Base: $8{,}600{,}000 \times 0.97 = \$8{,}342{,}000$
* Bad: $6{,}400{,}000 \times 0.97 = \$6{,}208{,}000$

Profit = NOI Y1 + NOI Y2 + net sale − basis:

* Good: $780{,}000 + 850{,}000 + 9{,}118{,}000 - 7{,}917{,}000 = \$2{,}831{,}000$
* Base: $760{,}000 + 800{,}000 + 8{,}342{,}000 - 7{,}917{,}000 = \$1{,}985{,}000$
* Bad: $650{,}000 + 560{,}000 + 6{,}208{,}000 - 7{,}917{,}000 = -\$499{,}000$

Scenario IRRs solve $-7{,}917{,}000 + \frac{NOI_1}{1+IRR} + \frac{NOI_2 + \text{Net sale}}{(1+IRR)^2} = 0$:

| Scenario | Profit | IRR | Equity multiple |
|---|---|---|---|
| Good | \$2,831,000 | 17.24% | 1.358x |
| Base | \$1,985,000 | 12.37% | 1.251x |
| Bad | −\$499,000 | −3.34% | 0.937x |

Expected profit $= 0.55(2{,}831{,}000) + 0.30(1{,}985{,}000) + 0.15(-499{,}000) = 1{,}557{,}050 + 595{,}500 - 74{,}850 = \$2{,}077{,}700$.

Variance $= \sum p_s (x_s - 2{,}077{,}700)^2$, so the standard deviation is \$1,144,810. Probability of loss = 15%. Partial expected loss = $0.15 \times (-499{,}000) = -\$74{,}850$.

Expected IRR $= 0.55(17.24\%) + 0.30(12.37\%) + 0.15(-3.34\%) = 12.69\%$.

Expected cash flows: Year 1 $= 0.55(780{,}000) + 0.30(760{,}000) + 0.15(650{,}000) = \$754{,}500$. Year 2 $= E[NOI_2] + E[\text{Net sale}] = 791{,}500 + 8{,}448{,}700 = \$9{,}240{,}200$. The IRR of $[-7{,}917{,}000;\ 754{,}500;\ 9{,}240{,}200]$ is **12.90%**.

**Check.** The good-scenario IRR can be checked on a calculator. CF0 = −7,917,000; CF1 = 780,000; CF2 = 9,968,000. On an HP-12C: `7917000 CHS g CF0`, `780000 g CFj`, `9968000 g CFj`, `f IRR` → 17.24.

**Decision consequence.** The expected IRR is about 12.7–12.9% unlevered on a two-year hold, against a Treasury bill alternative yielding a fraction of that. Only one scenario will occur. If the bad scenario happens, you will lose about \$0.5 million. If your process was sound, that does not make the decision wrong, and a good outcome would not have made it right. What matters is whether the probabilities and scenario values were defensible *when you made them*. Write them down now, before you know.

#### Example 1.2 — The break-even probability, and how one unknown fact moves it

**Given.** Example 1.1's three scenarios. Then a second case in which the franchisor will require a \$1.5 million property improvement plan (PIP) on change of ownership, which your diligence has not yet confirmed. Model the PIP as reducing profit by \$1.5 million in every scenario. This ignores timing and any revenue uplift from the renovation; Chapter 11 refines it.

**Find.** The break-even probability of the bad scenario, with and without the PIP.

**Solution (no PIP).**

Two-state collapse using only Good versus Bad: $p^* = G/(G+L) = 2{,}831{,}000/(2{,}831{,}000 + 499{,}000) = 85.0\%$.

Three-state version, keeping Good:Base at 55:30. The conditional expected profit if not Bad is $\bar G = (55 \times 2{,}831{,}000 + 30 \times 1{,}985{,}000)/85 = \$2{,}532{,}412$. Then $q^* = \bar G/(\bar G + L) = 2{,}532{,}412/(2{,}532{,}412 + 499{,}000) = 83.5\%$.

**Solution (with PIP).** Profits become Good \$1,331,000, Base \$485,000, Bad −\$1,999,000.

* Expected profit at the original probabilities: $0.55(1{,}331{,}000) + 0.30(485{,}000) + 0.15(-1{,}999{,}000) = \$577{,}700$.
* $\bar G = (55 \times 1{,}331{,}000 + 30 \times 485{,}000)/85 = \$1{,}032{,}412$.
* $q^* = 1{,}032{,}412/(1{,}032{,}412 + 1{,}999{,}000) = 34.1\%$.

**Decision consequence.** Without the PIP, the bad state would need to be more than 83% likely before the bid lost money in expectation. No reasonable view of a 15% bad-state probability is near that. The decision is robust to Knightian uncertainty about the bad state. With an unconfirmed \$1.5 million PIP, the break-even falls to 34%. A plausible recession probability for a two-year horizon can approach that number. The decision now depends on a figure you do not know. **The single most valuable action is to obtain the franchise transfer terms before bidding firm.** A phone call to the brand's franchise-sales office, or a request for the current PIP letter, is worth far more than refining the cap-rate assumption. Break-even analysis identifies which piece of information to buy next.

#### Example 1.3 — The price of immediacy: what the estate is paying you

**Given.** The estate's alternatives:

* *Quick sale:* \$7,800,000 in 45 days, with seller costs of 1.0% (attorney, title, no broker co-op): net $N_0 = 7{,}800{,}000 \times 0.99 = \$7{,}722{,}000$.
* *Patient sale:* The lender grants a forbearance with a \$250,000 fee and default-interest cost. The hotel is fully marketed. With probability 0.80 it sells for \$9.0 million gross after 6 months. With probability 0.20 the first buyer fails and it sells for \$8.4 million after 9 months. Seller costs 3%.

**Find.** The annualized price of immediacy, $r_{imm}$.

**Solution.**

Expected gross proceeds $= 0.80(9{,}000{,}000) + 0.20(8{,}400{,}000) = \$8{,}880{,}000$.

Expected net proceeds $= 8{,}880{,}000 \times 0.97 - 250{,}000 = \$8{,}363{,}600$.

Expected delay $\tau = 0.80(0.5) + 0.20(0.75) = 0.55$ years.

$$r_{imm} = \left(\frac{8{,}363{,}600}{7{,}722{,}000}\right)^{1/0.55} - 1 = (1.08309)^{1.8182} - 1 = 15.62\%.$$

**Check.** Continuous-compounding version: $\ln(1.08309)/0.55 = 14.51\%$, which is consistent with a discrete rate of 15.6%. Using the expected delay rather than integrating over the two delays is an approximation; Problem 1.6 asks you to bound the error.

**Decision consequence.** The estate pays an implied 15.6% annualized for certainty and speed. The figure is meaningful only relative to the risks the buyer absorbs. You waive contingencies and therefore carry the information-asymmetry risk of Example 1.7. You bear two years of market risk. You may be unable to finance the purchase on a 45-day timeline. A 15.6% implied rate is not an "arbitrage"; it is a premium. Ask whether it is enough. Ask also whether the lender's refusal to extend is itself information about the asset.

#### Example 1.4 — Why spreads exist: the market maker and the informed trader

**Given.** A dealer in an off-the-run corporate bond quotes 100.00 bid / 100.10 ask, so the half-spread is $h = 0.05$ points. Twenty percent of customer orders ($\pi = 0.20$) come from investors with genuinely better information. After their trades the bond's value moves 0.40 points ($\Delta$) against the dealer. Uninformed orders move nothing.

**Find.** The dealer's expected profit per trade and the competitive half-spread.

**Solution.** $E[\Pi] = h - \pi\Delta = 0.05 - 0.20 \times 0.40 = -0.03$ points per trade. The dealer loses money. The break-even half-spread is $h^* = \pi\Delta = 0.08$, a quoted spread of 0.16 points.

**Decision consequence.** The spread is not a toll the dealer collects for free. It is the price of trading against people who may know more. When you are the *informed* side, you pay a spread that is cheap relative to your information. When you are uninformed, wide spreads protect the dealer from you, and your realized trading cost will exceed the quoted half-spread. In private CRE, a buyer who is asked to waive diligence is being asked to post a zero spread to a counterparty who has better information. A rational buyer widens the bid, which means lowering it, by the expected value of what they cannot verify.

#### Example 1.5 — Positive expected value, negative growth: where speculation turns into gambling

**Given.** A repeated opportunity returns +60% or −50% on the capital committed, each with probability ½. Compare an American roulette single-number bet, which pays 35 to 1 with win probability 1/38.

**Find.** The expected return of each. For the speculation, find the compound growth rate of wealth at commitment fractions $f$ = 0.10, $f^*$, 0.25, 0.50, 1.00, and 1.50 (the last means 50% borrowed on top of equity).

**Solution.**

Roulette: $E[r] = \frac{1}{38}(35) + \frac{37}{38}(-1) = -2/38 = -5.26\%$ per bet. No sizing rule makes a negative-EV bet worth taking for profit.

Speculation: $E[r] = 0.5(0.60) + 0.5(-0.50) = +5.0\%$ per period, which is positive.

Kelly fraction: $f^* = p/b - (1-p)/a = 0.5/0.5 - 0.5/0.6 = 1 - 0.8333 = 0.1667$.

Growth $g(f) = 0.5\ln(1 + 0.6f) + 0.5\ln(1 - 0.5f)$:

| $f$ | $g(f)$ (log) | Compound growth per period | Median wealth after 10 periods (from 1.00) |
|---|---|---|---|
| 0.10 | 0.003488 | +0.35% | 1.035 |
| 0.1667 ($f^*$) | 0.004149 | +0.42% | 1.042 |
| 0.25 | 0.003115 | +0.31% | 1.032 |
| 0.50 | −0.012659 | −1.26% | 0.881 |
| 1.00 | −0.111572 | −10.56% | 0.328 |
| 1.50 | −0.372220 | −31.08% | 0.024 |

At $f = 1$: $g = 0.5\ln 1.6 + 0.5\ln 0.5 = \ln\sqrt{0.8}$, so wealth compounds at $\sqrt{0.8} - 1 = -10.56\%$ per period even though each period's expected return is +5%. After ten periods the median outcome is $0.8^5 = 0.328$.

**Check.** With five wins and five losses in ten periods at $f=1$: $1.6^5 \times 0.5^5 = 0.8^5 = 0.32768$. ✓

**Decision consequence.** Arithmetic expected return is the wrong objective for a speculator who must survive many decisions. A positive-EV opportunity sized at 100% of capital is, for practical purposes, a bet against your own survival. The CRE parallel is direct. A 75–85% LTV acquisition turns modest asset volatility into large equity volatility, and the limited-liability floor flatters arithmetic averages (Problem 1.9). Section 1.6 returns to leverage, and Chapter 21 treats sizing formally, including why full Kelly is too aggressive when probabilities are estimated with error.

#### Example 1.6 — The "riskless" back-to-back (Opportunity C)

**Given.** Purchase at \$5,000,000 with 1.5% buyer costs, so basis = \$5,075,000, all cash. If the 1031 buyer closes (probability $\pi = 0.70$), you sell at \$5,400,000 less 2% costs. If the buyer walks, you hold six months, collect \$150,000 of net rent, and sell at an expected \$4,900,000 gross less 2% costs. The lower price reflects a thinner buyer pool without an exchange buyer who must place funds.

**Find.** Profit in each case, EV, and the minimum completion probability $\pi^*$.

**Solution.**

* Completes: $5{,}400{,}000 \times 0.98 - 5{,}075{,}000 = 5{,}292{,}000 - 5{,}075{,}000 = +\$217{,}000$.
* Walks: $4{,}900{,}000 \times 0.98 + 150{,}000 - 5{,}075{,}000 = 4{,}802{,}000 + 150{,}000 - 5{,}075{,}000 = -\$123{,}000$.
* $EV = 0.70(217{,}000) + 0.30(-123{,}000) = 151{,}900 - 36{,}900 = +\$115{,}000$.
* $\pi^* = L/(G+L) = 123{,}000/(217{,}000 + 123{,}000) = 36.2\%$.

Sensitivity: if the fallback sale price is \$4.6 million rather than \$4.9 million, the walk-away loss becomes −\$417,000 and EV falls to $0.70(217{,}000) + 0.30(-417{,}000) = \$26{,}800$.

**Decision consequence.** The "\$400,000 arbitrage" is \$217,000 after costs if everything works. It is a probabilistic trade with an expected value of about \$115,000 on \$5.1 million of capital tied up for two to six months. Its EV is highly sensitive to the fallback price, about which you know little. It is speculation on the behavior of a counterparty who has made no binding commitment. A disciplined desk would do one of three things: (a) obtain a hard deposit from the 1031 buyer at signing, which converts leg risk into credit risk; (b) negotiate a longer close with the fund to align the two timelines; or (c) size the position as a speculation rather than as an arbitrage. "Arbitrage" in a pitch should prompt one question: *what happens if one leg fails?*

#### Example 1.7 — Information asymmetry: the lemons problem in hotel sales

**Given.** In a submarket, 60% of the hotels coming to market are "clean", worth \$10.0 million to a buyer. Forty percent carry undisclosed deferred capital needs and an imminent brand PIP, and are worth \$8.5 million. Sellers know their type; buyers cannot tell without diligence. Clean sellers will not accept less than \$9.8 million. Lemon owners will sell at any price above \$8.4 million.

**Find.** The pooling price a risk-neutral buyer would offer without diligence, and what happens at that price. Then find the value of diligence that perfectly reveals type at a cost of \$40,000.

**Solution.**

Pooling price $= 0.60(10.0) + 0.40(8.5) = \$9.40$ million.

At \$9.40 million clean sellers withdraw, because $9.40 < 9.80$. The only sellers who accept are lemons, worth \$8.5 million. A buyer who pays \$9.40 million loses \$0.90 million on every hotel bought. Anticipating this, buyers bid \$8.5 million, and only lemons trade. The market for clean hotels "unravels" (Akerlof, 1970).

With diligence costing \$40,000 per hotel, the buyer can identify clean hotels and pay up to \$10.0 million less diligence cost. Clean sellers asking \$9.8 million are then willing to trade. The buyer's surplus on a clean purchase at \$9.8 million is $10.0 - 9.8 - 0.04 = \$0.16$ million. Diligence creates a market that otherwise would not exist.

**Decision consequence.** Return to Opportunity B. The estate asks you to *waive most contingencies*. Reasoning as Akerlof did, ask whether a clean asset worth \$9.0 million would need to be sold this way. A forced timeline is one explanation. Hidden defects are another. The discount you are offered could be compensation for immediacy (Example 1.3), compensation for asymmetric information (this example), or both. Your bid should not assume it is all the former. Practical responses include a short, focused diligence period (PCA, franchise PIP letter, tax and lien searches, a review of the STR report and the last two years of P&Ls), a holdback or escrow, or a lower price.

---

### 1.6 CRE application: leverage converts investment into speculation

The industrial building (Opportunity A) is an investment at 0% leverage. Most of its return comes from contractual rent paid by a creditworthy tenant. Finance it at 85% LTV and the same building becomes a speculation on refinancing conditions, exit cap rates, and tenant renewal, because small changes in asset value now dominate the equity outcome.

Use equation 1.4.6 with Opportunity A's going-in cap rate of 6.25% and a debt rate of 6.50%. Ignore amortization for the moment; Chapter 10 adds it. In the first year:

* Unlevered income return = 6.25%.
* At 60% LTV, levered income return $= (6.25\% - 0.60 \times 6.50\%)/0.40 = (6.25\% - 3.90\%)/0.40 = 5.875\%$.

Leverage is **negative** on a current-income basis because the asset yields less than the debt costs. The levered investor is therefore relying on appreciation: rent bumps, cap-rate compression, or both. That reliance is a speculative component. It may be reasonable, since 3% bumps on a 6.25% yield imply an unlevered return near 9% if the exit cap equals the entry cap. But it should be stated as a forecast, not hidden inside a single IRR.

With amortization the first-year cash yield is lower still. On a \$8.4 million loan at 6.50% over 30 years, monthly payment = \$53,094 and annual debt service = \$637,125. Cash flow after debt service is $875{,}000 - 637{,}125 = \$237{,}875$ on equity of \$5.6 million, a cash-on-cash return of 4.25%. Part of debt service is amortization, which is retained in the equity. The 4.25% is a cash yield, not a total return.

**Question to carry forward.** If you accept a cash yield below the Treasury yield, what are you speculating on, and how would you know you were wrong? Chapter 6 compares cap rates with Treasury yields directly. Chapter 10 builds the refinancing analysis.

---

### 1.7 When the conventional relationships fail

The definitions above are clean. Markets are not.

1. **Hedges turn into speculations.** A hedge is defined by the exposure it offsets. If the underlying exposure changes, the hedge becomes a naked position. Examples are a hotel sold before its rate cap expires and a construction loan repaid early. Metallgesellschaft's 1993 losses on its rolling energy-futures hedge are a standard case of a hedge whose funding and timing mismatches produced liquidity stress. Culp and Miller (1995) and Mello and Parsons (1995) disagree on whether the hedge was economically sound, which itself shows how hard the classification can be.
2. **Liquidity premia invert.** The liquidity provider is paid in calm markets and pays in crises. Capital that "always" buys from forced sellers is itself forced to sell when its lenders pull lines.
3. **Arbitrages fail through financing, not logic.** Two claims can converge in theory and diverge in practice for longer than the arbitrageur can fund the position. Shleifer and Vishny (1997) call these the limits of arbitrage. Chapter 23's LTCM case is the canonical example.
4. **Expected-value reasoning fails when probabilities are not meaningful.** For one-off events with no reference class, a stated probability can be false precision. Break-even analysis is more robust than point estimates in these cases.
5. **Information asymmetry can run in your favor without your knowledge.** A seller may underprice an asset because *they* lack information, for example an estate's executor who does not know the brand has approved a conversion. Exploiting public or diligence-derived information is legitimate. Trading on material nonpublic information obtained in breach of a duty is not (Appendix F).
6. **Process can be good and the reference class wrong.** A disciplined process that uses 1995–2019 base rates for interest-rate moves would have badly underestimated 2022 (Chapter 23).

---

### 1.8 What distinguishes professional speculation from gambling

| Criterion | Professional speculation | Gambling |
|---|---|---|
| Source of expected return | Risk premium, liquidity premium, or analytical edge that can be articulated | House edge against the participant; none |
| Expected value after costs | Positive, with stated assumptions | Negative, or positive but sized for ruin |
| Sizing | Survives plausible adverse sequences; fraction of Kelly | Large relative to capital; "all in" |
| Invalidation | Stated before entry | Absent; losses are "temporary" |
| Record | Pre-decision forecast distribution | Outcome memory only |
| Economic function | Transfers risk, supplies liquidity, improves price discovery | Entertainment or transfer to the house |

Test any proposed position against all six rows. A single failure, especially on sizing or invalidation, should stop the trade until it is fixed.

---

### 1.9 Historical episode: 19 October 1987 — liquidity consumers meet absent liquidity providers

**Date and environment.** In the first three quarters of 1987, U.S. equities rose sharply while long-term interest rates rose. The dollar was under pressure, and U.S. trade deficits were a political issue [FACT: general context documented in the Federal Reserve History essay cited below; the detailed rate path is to be verified against FRED series GS10 *(verification pending)*].

**What happened.** On Monday, 19 October 1987, the Dow Jones Industrial Average fell 508 points, or 22.6%, the largest one-day percentage decline in its history [FACT; Federal Reserve History, "Stock Market Crash of 1987", VERIFIED-SECONDARY]. On the morning of 20 October the Federal Reserve issued a brief statement affirming its readiness to serve as a source of liquidity to support the economic and financial system [FACT; same source; exact wording to be checked against the Fed's published statement *(verification pending)*].

**Participants and mechanisms.**

* **Portfolio insurers** ran dynamic hedging programs that replicated a put option by selling stock-index futures as prices fell. Their selling was mechanical and largely insensitive to price. In option terms they were liquidity *consumers* whose demand rose as prices fell [FACT that these strategies existed and were a major focus of the post-crash inquiry: *Report of the Presidential Task Force on Market Mechanisms* (the "Brady Report"), January 1988; the magnitude of their selling is disputed — see below].
* **Index arbitrageurs** bought cheap futures and sold the underlying stocks. That transmitted futures selling into the stock market [FACT: Brady Report].
* **Specialists and market makers**, the designated liquidity providers, faced order imbalances far larger than their capital, and some stocks opened late or not at all [FACT: Brady Report].

**Competing interpretations.** The Brady Report emphasized portfolio insurance and the linkage between futures and stocks. The Chicago Mercantile Exchange's own studies argued that the futures market transmitted rather than caused the selling, and that cash-market selling by other investors was larger [INFERENCE from the existence of the dispute, documented in the CME's 1988 reports and in Miller's later writing; the specific shares of total selling attributed to each group are left *(verification pending)* until checked against the primary reports]. Shiller's surveys of investors during the crash found that many sellers reported reacting to the price decline itself rather than to news [FACT: Shiller, *Market Volatility*, 1989, ch. 23; VERIFIED-SECONDARY].

**What was knowable beforehand?** That portfolio insurance programs existed and would sell into declines was publicly discussed before October 1987 [REASONABLE INFERENCE: the strategy was commercially marketed]. What was not knowable was the *aggregate* size of mechanical selling relative to the capital of liquidity providers on a given day. That is the crucial quantity, and it is generally unobservable in advance. No one could know the date.

**What the case does and does not establish.** It establishes that a market's ability to absorb selling depends on the balance of price-sensitive liquidity providers and price-insensitive liquidity consumers, and that this balance can change abruptly. It does **not** establish that mechanical hedging *caused* the crash, a point that remains disputed. Nor does it establish that similar crashes are predictable from positioning data.

**CRE connection.** Private real estate has no specialist and no circuit breaker. When forced sellers (maturing loans, redemption queues in open-end funds) meet absent buyers, the result is not a 22% day. It is a market with **no transactions**. Appraisals go stale and price discovery happens slowly through the few trades that do occur (Chapter 2). The economics are the same, but the clock runs in months instead of hours.

---

### 1.10 Decision exercise: allocate the Monday capital

Return to the three opportunities, and assume you have \$12 million of deployable capital this month. Opportunity B requires about \$7.9 million all cash, which leaves room for acquisition financing later. Opportunity A requires \$5.6 million of equity at 60% LTV. Opportunity C requires \$5.1 million for two to six months.

Complete the decision on the template at `desk/investment_memos/decision_record_template.md`. Your record must include:

1. The classification of each opportunity and the premium it pays (risk, liquidity, or information).
2. For B: whether you would bid \$7.8 million *before* obtaining the franchise PIP letter, and the maximum price you would pay if a \$1.5 million PIP is confirmed.
3. For C: the minimum deposit you would require from the 1031 buyer to proceed.
4. For A: what you are speculating on at 60% LTV, and whether the same building is worth owning at 0% LTV versus Treasuries.
5. What you will *not* do, and why. Abstention is a legitimate answer for any of the three.
6. Invalidation criteria for anything you do.

**Rubric (see `problems/solutions/ch01_solutions.md` §Decision exercise).** Full credit requires that B be conditional on the PIP information. It requires that C be resized or restructured rather than called "arbitrage". It requires that A's levered return be decomposed into income and appreciation forecasts. It requires an explicit comparison with the risk-free alternative. There is no single correct allocation.

---

### 1.11 Frequent analytical errors

1. **Treating the expected IRR as the return you will earn.** You will earn one draw. Report the distribution.
2. **Averaging IRRs and calling it the expected return.** Distinguish the expected IRR from the IRR of expected flows, and give both when they differ materially.
3. **Calling a trade with execution risk "arbitrage".** Ask what happens if one leg fails.
4. **Ignoring the cause of a discount.** A forced-sale discount can be a liquidity premium, an information-asymmetry discount, or both.
5. **Equating positive EV with a good position.** Size determines whether a positive-EV position compounds or ruins.
6. **Judging a decision by its outcome.** Without a written ex-ante distribution, you cannot evaluate your own process.
7. **Mistaking leverage for return.** Negative leverage (asset yield below debt cost) means the levered return depends on appreciation.
8. **False precision under uncertainty.** A probability quoted to two decimals for a one-off event is often a disguised guess. Use break-even analysis.
9. **Forgetting transaction costs.** Buyer and seller costs of 1–3% each can absorb most of the edge in short holds.

---

### 1.12 Connections to other chapters

* Chapter 2 develops price formation and why appraisal-based CRE prices lag.
* Chapter 3 formalizes Bayesian updating, reflexivity, and forced selling.
* Chapter 10 adds amortization, refinancing, and debt-sizing to the leverage analysis of §1.6.
* Chapter 11 values Opportunity B's hotel properly: normalization, PIP, franchise, reserve.
* Chapter 20 formalizes scenario trees, calibration, and decision theory.
* Chapter 21 treats Kelly sizing, drawdowns, and ruin.
* Chapter 23 examines 1987, LTCM, and 2008 in full.
* Case A (`cases/hypothetical/case_A_overpriced_hotel_owner/`) applies these ideas to a seller anchored to original cost.

---

### 1.13 One-page reference sheet

**Classification questions:** What risk am I bearing? Who pays me to bear it? Why is this price available to me? What happens if a leg fails?

| Formula | Expression |
|---|---|
| Expected value | $E[X] = \sum p_s x_s$ |
| Std. deviation | $\sqrt{\sum p_s (x_s - E[X])^2}$ |
| Break-even bad-state probability | $p^* = G/(G+L)$ |
| Multi-scenario break-even | $q^* = \bar G/(\bar G + L)$, with $\bar G$ = expected profit given not bad |
| Leg-completion break-even | $\pi^* = L/(G+L)$ |
| Price of immediacy | $r_{imm} = (E[N_\tau]/N_0)^{1/\tau} - 1$ |
| Market maker | $E[\Pi] = h - \pi\Delta$; $h^* = \pi\Delta$ |
| Growth rate | $g(f) = E[\ln(1+fr)]$ |
| Kelly (two outcomes $+a$/$-b$) | $f^* = p/b - (1-p)/a$ |
| Volatility drag (approx.) | $\bar r - g \approx \sigma^2/2$ |
| Levered return | $r_E = r_A + \frac{\lambda}{1-\lambda}(r_A - r_D)$ |
| Recovery after loss $d$ | $1/(1-d) - 1$ |

**Rules of thumb (to be tested, not trusted).** A 50% loss needs a 100% gain to recover. At 75% LTV, a 25% fall in value eliminates equity. Doubling position size roughly quadruples the variance penalty in growth.

---

### References for this chapter

All sources are recorded in `SOURCE_REGISTER.md` with verification status.

* Akerlof, G. A. (1970). "The Market for 'Lemons': Quality Uncertainty and the Market Mechanism." *Quarterly Journal of Economics*, 84(3), 488–500.
* Glosten, L. R., and Milgrom, P. R. (1985). "Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders." *Journal of Financial Economics*, 14(1), 71–100.
* Knight, F. H. (1921). *Risk, Uncertainty and Profit*. Boston: Houghton Mifflin.
* Kelly, J. L. (1956). "A New Interpretation of Information Rate." *Bell System Technical Journal*, 35(4), 917–926.
* Shleifer, A., and Vishny, R. W. (1997). "The Limits of Arbitrage." *Journal of Finance*, 52(1), 35–55.
* Presidential Task Force on Market Mechanisms (1988). *Report of the Presidential Task Force on Market Mechanisms* ("Brady Report"). Washington, DC: U.S. Government Printing Office. Archived at https://www.sechistorical.org/collection/papers/1980/1988_0101_BradyReport.pdf.
* Federal Reserve History. "Stock Market Crash of 1987." https://www.federalreservehistory.org/essays/stock-market-crash-of-1987 (accessed 2026-10-19).
* Shiller, R. J. (1989). *Market Volatility*. Cambridge, MA: MIT Press.
* Culp, C. L., and Miller, M. H. (1995). "Metallgesellschaft and the Economics of Synthetic Storage." *Journal of Applied Corporate Finance*, 7(4), 62–76.
* Mello, A. S., and Parsons, J. E. (1995). "Maturity Structure of a Hedge Matters: Lessons from the Metallgesellschaft Debacle." *Journal of Applied Corporate Finance*, 8(1), 106–120.


\newpage

## Chapter 2 — The Price Formation Process

> **Status:** Complete (v1.0). Numerical examples are reproduced in `tests/test_ch02_examples.py` using `models/python/sdesk/x_microstructure.py`. Problems are in `problems/questions/ch02_problems.md` and solutions in `problems/solutions/ch02_solutions.md`. Sources are in `references/sources_ch02.md`; figures from secondary coverage of NCREIF and Nareit releases are marked VERIFIED-SECONDARY there, and one item (the exact wording of the Federal Reserve's May 2023 *Financial Stability Report*) is paraphrased only and flagged *(verification pending)*.

### Learning objectives

After this chapter you should be able to:

1. Explain where a price comes from: who must trade, who may trade, and how an auction or a dealer converts orders into a single number. Compute a call-auction clearing price from supply and demand schedules, and show how a market order moves it.
2. State the weak, semi-strong, and strong forms of market efficiency precisely. Explain the Grossman–Stiglitz paradox and the limits to arbitrage, and say what each implies for a speculator who believes a price is wrong.
3. Convert a data surprise into a price change: standardize the surprise against consensus, apply a sensitivity, and translate a yield move into bond and property values. Distinguish surprise relative to consensus from surprise relative to positioning.
4. Identify the **marginal** buyer and seller of a CRE asset from a reservation-price distribution. Show numerically how the loss of the most aggressive financed buyers lowers the clearing price with no change in NOI, and why a gap between buyer and seller reservation prices produces a frozen market instead of a lower price.
5. Estimate an effective bid–ask spread with Roll's estimator. Compute and annualize the round-trip cost of a liquid security and a private property.
6. Explain why appraisal-based CRE indices lag and smooth economic value. Apply the Geltner unsmoothing filter $r_t = (r^*_t - a\,r^*_{t-1})/(1-a)$, compute the implied mean lag and volatility understatement, and know when the filter misleads.
7. Recognize transaction selection bias and stale comparable sales. Restate a comp set to today's market and to the subject's quality, and quantify how far a naive comp average is from a defensible value.

---

### 2.1 Opening investment problem: three prices for the same apartments

You are the real estate principal of a family office. It is 15 months into a monetary-tightening cycle; the 10-year Treasury yield is about 200 bp above its level when the cycle started. All facts below are [HYPOTHESIS], a constructed teaching case. Section 2.9 gives the historical episode that the case resembles, with documented figures.

Three numbers reach your desk on the same morning.

**Price 1: the fund statement.** The office holds \$25 million of units in an open-end core real estate fund. The fund's quarterly statement shows net asset value (NAV) per unit down 3% over the last twelve months. The NAV is based on independent appraisals. The fund's apartment holdings are appraised at a 4.30% cap rate on in-place NOI after reserves. The statement mentions, in a footnote, that redemption requests equal 12% of NAV and will be paid "as liquidity permits".

**Price 2: the screen.** Listed apartment REITs are down 28% over the same twelve months. Your analyst estimates that their share prices imply a 5.60% cap rate on their portfolios, which are of similar quality and location to the fund's.

**Price 3: the broker.** A broker offers a 240-unit, 1998-vintage garden apartment community in a Sun Belt suburb. In-place NOI after reserves is \$3,000,000. The seller is a closed-end fund near the end of its life. The broker's guidance is \$60.0 million, a 5.00% cap rate, which matches the seller's most recent appraisal. To justify the price, the broker cites four "recent comps" at an average cap rate of 4.95%.

You have three possible actions, plus abstention. You can (a) request redemption from the open-end fund, (b) buy apartment REIT shares, or (c) bid on the garden community. The questions are: Which of these prices is "the price"? Why do they differ? Who is on the other side of each? What would you need to believe to act?

By the end of the chapter you will be able to answer all three questions with numbers. Section 2.10 returns to the decision.

---

### 2.2 Economic intuition: prices are made by the marginal trader

#### Who sets a price

A price is not a property of an asset. It is the terms at which the last trade happened, or would happen, between two parties who each preferred trading to not trading. Most owners of an asset do not trade on a given day. Their valuations do not set the price. They only stand behind it as potential sellers if the price rises far enough.

The price is set at the **margin**: by the buyer who is just willing to pay it and the seller who is just willing to accept it. In a liquid market there are many marginal participants on both sides, and their reservation prices are close together. In private CRE there may be four serious bidders for a building. The price depends on the second-highest of their valuations, and on whether the seller's reservation price is below it.

This has an immediate consequence. **A price can fall without anyone's estimate of the asset's cash flows changing.** It falls if the most aggressive buyers leave the market, for example because their lenders stop lending. The remaining buyers are those with lower valuations, and one of them becomes marginal. Example 2.3 computes this for the opening problem's apartment community.

#### Order flow: who must trade and who may trade

Every trade has two sides, but the two sides rarely have the same urgency. Chapter 1 separated liquidity *consumers*, who must trade now, from liquidity *providers*, who will trade if paid. Price formation is the process by which consumers' urgency is matched against providers' willingness, and by which informed traders' information is transmitted into the price.

Three kinds of order flow matter:

* **Informed flow** comes from traders who know or have estimated something about value that the price does not yet reflect. Their trades move the price toward value and are the mechanism of price discovery.
* **Liquidity-motivated flow** comes from traders who must buy or sell for reasons unrelated to value: redemptions, loan maturities, index rebalancing, fund wind-downs, tax deadlines, estate settlements. Their trades move prices *away* from value temporarily, and providers are paid to absorb them.
* **Noise or sentiment flow** comes from traders who believe they are informed but are not. Their trades can push prices away from value for long periods. Arbitrageurs who bet against them bear the risk that the mispricing grows before it shrinks (§2.4.3).

A professional must ask of every price: which kind of flow produced it? A REIT that falls 3% on a day when its index weight is cut is not the same signal as a REIT that falls 3% after its largest tenant files for bankruptcy.

#### Auctions and dealers

Markets aggregate orders into prices through two basic mechanisms.

A **call auction** collects orders over a period, then executes all compatible orders at a single price at one moment. Stock exchanges use call auctions to open and close trading. Treasury securities are first sold in auctions. Foreclosure sales, many loan-sale processes, and broker-run "best and final" rounds for CRE are auctions too, although they clear a single indivisible asset rather than many units.

A **continuous market** executes each order as it arrives against the orders already resting in a limit-order book, or against a dealer's quote. Prices update with every trade. Immediacy is available at all times, at the cost of the bid–ask spread and of the price impact of large orders.

The difference matters for what a price *means*. A call-auction price aggregates all orders submitted in the window and is the single price that maximizes trade. A continuous-market price is the price at which the last order happened to execute; it can be noisier, but it updates instantly. Private CRE is the limiting case of an infrequent, negotiated auction with high participation costs. Price discovery there is slow because each "auction" requires months of work and only a few happen in a given submarket each quarter.

#### Expectations and surprise

Prices are forward-looking. A price today equals what the marginal trader expects the asset to be worth, discounted. Information that everyone expected is therefore already in the price. Only the **surprise**, the difference between what happened and what was expected, moves prices.

This is why a strong employment report can coincide with falling yields (drill D003), and why a REIT can fall on "record earnings". The question is never "was the news good?" It is "was the news better or worse than the marginal trader expected, and by how much, relative to how noisy such news usually is?"

#### Why appraisals lag

Private CRE is valued, for accounting and fund-reporting purposes, by appraisers. An appraiser estimates what a property would sell for, using comparable sales, income capitalization, and judgment. Three features of this process slow down appraised values:

1. **Evidence lag.** Appraisers rely on closed sales. A sale that closes today was priced when the contract was signed, often 60–120 days earlier, on terms negotiated before that.
2. **Rational partial adjustment.** Each comparable sale is a noisy signal of value. An appraiser who combines the new evidence with the prior appraisal, weighting each by its precision, produces an estimate that moves only partly toward each new signal. That is optimal for minimizing the error of a single appraisal, but it smooths the *time series* (Quan and Quigley, 1991; Geltner, 1993).
3. **Staggered and anchored reappraisals.** Not every property in an index is reappraised every quarter, and an appraiser updating last year's value tends to anchor to it.

The appraisal-based index is therefore a moving average of past market values. It turns too late, turns too gently, and looks less volatile than the market it measures. Section 2.4.5 derives the filter that undoes the smoothing.

#### Selection: which assets trade

In a downturn the assets that trade are not a random sample. Owners of properties that have lost the most value often cannot sell: the price would not repay the loan, or a sale would crystallize a loss the owner prefers not to report. Lenders often extend rather than foreclose. The properties that do sell are disproportionately those whose owners are unlevered or forced for non-value reasons, and those of the highest quality, for which buyers still exist. A comp set drawn from these sales overstates the value of the typical asset. Transaction-based indices built from them understate the decline (Fisher, Gatzlaff, Geltner and Haurin, 2003, develop indices that correct for this variable liquidity).

---

### 2.3 Technical definitions

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

### 2.4 Equations and derivations

#### 2.4.1 Clearing a call auction

Let buy limit orders be $(L^b_j, q^b_j)$ and sell limit orders $(L^s_k, q^s_k)$. Market orders $M^b$ and $M^s$ execute at any price. At a candidate price $p$:

$$D(p) = M^b + \sum_{j:\,L^b_j \ge p} q^b_j, \qquad S(p) = M^s + \sum_{k:\,L^s_k \le p} q^s_k.$$

$D$ is non-increasing and $S$ non-decreasing in $p$. Executable volume is $\min\{D(p), S(p)\}$. The clearing price maximizes it:

$$p^* = \arg\max_p \min\{D(p), S(p)\}.$$

With discrete schedules there can be ties. Exchanges break them by minimizing the imbalance $|D - S|$, then by reference to a prior price. Our library takes the mean of any remaining tied prices, which is a teaching simplification.

A market sell order of size $Q$ shifts $S(p)$ up by $Q$ at every price. The new clearing price is lower. The ratio of the price change to $Q$ is an empirical price-impact coefficient $\lambda = \Delta p^*/Q$. Kyle (1985) derived $\lambda$ as the market maker's rational response to the share of informed flow: the more informative order flow is, the more a given imbalance must move the price.

#### 2.4.2 Efficiency, costly information, and Grossman–Stiglitz

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

#### 2.4.3 Limits to arbitrage

Suppose an informed trader is right that a price is too low. Shleifer and Vishny (1997) identify why the trader may still not correct it:

1. **Noise-trader risk.** The mispricing can widen before it closes. A trader who must mark to market and may face redemptions can be forced out at the worst moment.
2. **Funding and margin.** Positions are financed. A lender raises haircuts when prices fall, exactly when the opportunity is best.
3. **Short-sale constraints.** If the mispriced asset is *overvalued*, the arbitrage requires a short. Private real estate cannot be shorted at all. A REIT can be shorted, but borrow costs, recall risk, and the absence of a convergence date limit the trade.
4. **No convergence mechanism.** A futures contract converges to spot at expiry. A REIT's discount to the appraised value of its properties has no expiry. It closes only through events: takeovers, asset sales, buybacks, or appraisal write-downs.
5. **Fundamental risk.** The "arbitrage" between a REIT and private properties is not between identical claims. The REIT has leverage, management, and a cost structure.

A price can therefore be wrong for longer than an arbitrageur can stay solvent. A divergence between listed and private CRE values (§2.9) is not by itself an arbitrage opportunity.

#### 2.4.4 Surprise and the price response

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

#### 2.4.5 The reservation-price model of a single-asset sale

Let buyers $i = 1, \dots, n$ have reservation prices $B_i$, and let the seller's reservation price be $R$. In an ascending (English) auction with private values, the bidder with the highest $B$ wins at a price just above the second-highest $B$:

$$P = \max\{B_{(2)}, R\}\quad \text{if } B_{(1)} \ge R; \qquad \text{no trade if } B_{(1)} < R.$$

Here $B_{(1)} \ge B_{(2)} \ge \dots$ are the order statistics. Two results follow.

1. **Removing the top bidder lowers the price to the old third-highest valuation.** If the top two bidders depend on financing that disappears, the price can fall a long way while the median buyer's valuation is unchanged.
2. **When $B_{(1)} < R$, there is no transaction and therefore no price.** The observed market goes quiet. Appraisals, which need transactions, do not fall. This is the mechanism of a frozen market.

For a buyer with fixed equity $E$, financed with a loan that is the lesser of LTV-based and DSCR-based proceeds, the reservation price is capped by financing:

$$B = \min\left\{\frac{E}{1-\text{LTV}},\; E + \frac{NOI}{DSCR \cdot K}\right\},$$

where $K$ is the loan constant (annual debt service per dollar of loan; equal to the interest rate for an interest-only loan). When rates rise, $K$ rises, the DSCR constraint binds, and the financed buyer's reservation price falls even if the buyer's view of the property is unchanged.

Fisher, Gatzlaff, Geltner and Haurin (2003) model transaction volume and prices from the distributions of buyer and seller reservation prices. When buyer reservation prices fall faster than seller reservation prices, as in a credit contraction, observed prices fall less than the buyers' side of the market, and volume collapses. The decline appears first in volume, not in price.

#### 2.4.6 Spreads and Roll's estimator

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

#### 2.4.7 Appraisal smoothing and the Geltner filter

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

#### 2.4.8 Stale comps and selection

**Time adjustment.** At constant NOI, value moves inversely with the cap rate. If a market value index for comparable properties stood at $I_s$ at the comp's sale and $I_0$ now, the comp's cap rate restated to today is

$$c_{\text{now}} = c_{\text{sale}} \cdot \frac{I_s}{I_0}.$$

**Selection.** Let $\Delta_i$ be asset $i$'s change in value and let assets trade only if $\Delta_i > \theta$ (owners of assets that fell further cannot or will not sell). The mean change among traded assets is $E[\Delta \mid \Delta > \theta] \ge E[\Delta]$. The comp set is biased upward by $E[\Delta \mid \Delta > \theta] - E[\Delta]$. The bias rises with the dispersion of value changes and with the severity of the threshold. Both are largest in exactly the market where comps are most needed.

---

### 2.5 Worked examples

All inputs are [HYPOTHESIS] unless cited. All examples are reproduced in `tests/test_ch02_examples.py`.

#### Example 2.1 — Clearing a closing auction, and what a market order does

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

#### Example 2.2 — Converting an inflation surprise into price changes

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

#### Example 2.3 — The marginal buyer: losing the financed bidders

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

#### Example 2.4 — Roll's spread and the cost of a round trip

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

#### Example 2.5 — Unsmoothing an appraisal index

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

#### Example 2.6 — A biased comp set

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

#### Example 2.7 — How much should appraisal NAV move? Reconciling three prices

**Given.** The opening problem's three numbers: fund appraisal cap 4.30%; REIT-implied cap 5.60%; and your own estimate for a similar private asset from Examples 2.3 and 2.6, which brackets 5.25%–5.53%.

**Find.** The percentage value gap between the appraisal and each market-based estimate at constant NOI.

**Solution.** Value ratio at constant NOI $= c_{\text{appraisal}}/c_{\text{market}}$:

* REIT-implied: $4.30/5.60 - 1 = -23.21\%$
* Private, unlevered marginal buyer (5.25%): $4.30/5.25 - 1 = -18.10\%$
* Private, comp-based (5.53%): $4.30/5.53 - 1 = -22.24\%$

**Check.** All three are negative and between 18% and 23%. The fund has written down only 3%. Even if the REIT market overreacted, the private-market evidence alone implies a gap of roughly 18–22%.

**Decision consequence.** The fund's NAV is a lagged moving average, not a price. If you can redeem at NAV, you sell at a price about 18–23% above where the fund's assets would trade. The remaining LPs pay for it (Problem 2.8 computes the transfer). The fund manager knows this, which is why redemptions are paid "as liquidity permits" and NAV is likely to be marked down before your units are paid. A request to redeem is still rational: it gives you a place in the queue at low cost. But the expected payout is not today's NAV. For the REIT, a 5.60% implied cap is close to the private-market evidence, so REIT shares are not obviously cheap relative to private value. They are cheap only relative to a stale appraisal.

---

### 2.6 CRE application: reading a market that does not print

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

### 2.7 Price discovery in liquid versus illiquid markets

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

### 2.8 When the relationship fails

1. **The unsmoothing parameter is wrong or unstable.** $a$ is not a physical constant. Appraisal practice changes. Appraisers in some markets have, in some downturns, marked values down *faster* than transaction evidence (MSCI has documented such a reversal in some European markets in the 2022–23 downturn [ch02-S11, VERIFIED-SECONDARY]). Applying a historical $a$ to such a series produces an overshoot. Always test at two values of $a$, and check the result against transaction evidence.
2. **The REIT is not the property.** A REIT is a levered, managed, taxed-differently claim with its own cost of capital, development pipeline, and sentiment. Its implied cap rate depends on the analyst's estimate of NOI and of the value of non-property items. A REIT discount to NAV can persist for years. Treating the REIT-implied cap rate as the true private value assumes away exactly the frictions that let the two diverge.
3. **Surprise sensitivities change with regime.** The bond market's response to an inflation surprise depends on what the central bank is believed to do about it. A sensitivity estimated in a low-inflation regime can understate the response in a high-inflation one, and vice versa (Chapter 5).
4. **Consensus is stale or gamed.** Forecasts submitted days before a release can miss late information. The relevant expectation is positioning, which is not observable. A model built on published consensus will sometimes give the wrong sign.
5. **Roll's estimator fails with trending or autocorrelated order flow.** When the autocovariance of price changes is positive, the estimator is undefined. In thin markets with persistent order flow, the spread is underestimated or cannot be estimated.
6. **The reservation-price model ignores strategic bidding and information.** In a common-value auction, bidders who know others are bidding shade their bids to avoid the winner's curse. Sellers can run processes that extract more than the second-highest valuation. Example 2.3 is a benchmark, not a forecast of the hammer price.
7. **Selection can run the other way.** In a boom, the properties that trade can be the weakest (owners selling into strength), so transaction indices understate quality-adjusted prices. Always ask why *these* assets traded *now*.
8. **The market is frozen because the seller has information.** A seller who will not accept the buyer's price may know something the buyer does not: a lease about to sign, a tax appeal about to succeed. The no-trade outcome does not always mean the seller is anchored.

---

### 2.9 Historical episode: the 2022–23 divergence between listed REITs and private appraisals

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

### 2.10 Decision exercise: three prices, one decision

Return to the opening problem. You have three possible actions and abstention. Complete the decision record at `desk/investment_memos/decision_record_template.md`. Your record must include:

1. **A value range for the 240-unit garden community**, built from the marginal-buyer analysis (Example 2.3) and the restated comps (Example 2.6). State which buyer you expect to be marginal and why.
2. **A bid, or a decision not to bid**, with the walk-away price and what would change it. Specify the information you would require: rent roll, trailing-twelve-month operating statement, capital needs, loan terms the seller is under, and the reason the seller is selling now.
3. **The redemption decision.** Compute the expected payout per unit if NAV is marked down 15% before the queue clears. Decide whether to file a redemption request, and say what you would do with the proceeds.
4. **The REIT decision.** Is a 5.60% implied cap rate cheap relative to your private-market estimate? What would you be speculating on if you bought the shares? What is the invalidation trigger?
5. **What you will not do, and why.** Abstention from any or all actions is acceptable if justified.

**Rubric** (see `problems/solutions/ch02_solutions.md`, §Decision exercise). Full credit requires: (a) a private value range that sits below \$60.0 million and is derived, not asserted; (b) recognition that the seller's reserve and the marginal buyer's valuation do not overlap, so the likely outcome is no trade at current guidance; (c) a correct statement that NAV is not a redemption price and that redeeming at a stale NAV transfers value from remaining LPs; (d) recognition that the REIT is cheap relative to the appraisal but not obviously relative to private-market evidence; and (e) explicit invalidation criteria. There is no single correct allocation.

---

### 2.11 Frequent analytical errors

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

### 2.12 Connections to other chapters

* Chapter 1 introduced liquidity provision, the price of immediacy, and adverse-selection spreads; this chapter shows how those forces set prices.
* Chapter 3 extends the marginal-buyer model to reflexive collateral loops and forced-selling price impact.
* Chapter 4 builds surprise indices and estimates the sensitivities used in Example 2.2.
* Chapter 6 develops the cap-rate/Treasury relationship and the pass-through coefficient $\phi$.
* Chapter 9 treats comparable-sales adjustment and valuation in full (`desk/investment_memos/comparable_sale_adjustment_worksheet.md`).
* Chapter 10 develops the loan-sizing constraints that determine financed buyers' reservation prices.
* Chapter 12 uses REIT-implied cap rates and maturity walls to time distressed CRE purchases.
* Chapter 23 revisits 2008–09 in full.

---

### 2.13 One-page reference sheet

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

### References for this chapter

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


\newpage

## Chapter 3 — The Speculator's Mental Models

> **Status:** Complete (v1.0). Every number in the text, problems, and solutions is reproduced in `tests/test_ch03_examples.py` (helpers in `models/python/sdesk/x_dynamics.py`). Problems are in `problems/questions/ch03_problems.md`, solutions in `problems/solutions/ch03_solutions.md`, sources in `references/sources_ch03.md`. Items marked *(verification pending)* are listed there and are not used as established fact.

### Learning objectives

After this chapter you should be able to:

1. Compute a hurdle rate from the **next-best alternative**, levered or de-levered to the risk of the deal in front of you, and state the dollar cost of choosing wrongly.
2. Write **reflexivity** as a collateral feedback loop (price → collateral value → lending capacity → demand → price), compute its loop gain, iterate it, and state the stability condition. Explain why the loop is stronger on the way down.
3. Convert an AR(1) coefficient into a **half-life**, forecast a mean-reverting spread, and say when the estimate cannot be trusted.
4. Define **time-series momentum**, size a volatility-scaled position, and state what the published evidence does and does not show.
5. Use a two-state **Markov regime** model to compute expected regime durations, long-run probabilities, and multi-period transition probabilities, and apply them to NOI forecasts and loan maturities.
6. Value the **option to wait** on a development parcel with a one-period binomial model and verify the answer by replication.
7. Compute the size and price impact of a **forced sale** under a leverage covenant, and the price-impact threshold beyond which selling cannot restore compliance.
8. Measure **exit capacity** for a crowded trade and size a position to it.
9. Trace a **second-order chain** from a rate rise to CRE refinancing gaps to bank lending capacity.
10. Update beliefs with **likelihood ratios** over a sequence of data points, and quantify the bid error caused by over- and under-reaction.

---

### 3.1 Opening investment problem: the lender calls with more money

You manage a closed-end fund that owns twelve select-service hotels in one Sun Belt metro. All facts in this section are [HYPOTHESIS], a constructed teaching case.

The portfolio was appraised last month at \$320 million, up roughly 30% in three years. Fund debt is a single portfolio facility of \$176 million, 55% of appraised value, with a **maintenance covenant**: if LTV on a fresh appraisal exceeds 70%, the fund must pay down the loan to 70% within 90 days. Fund equity is therefore \$144 million.

On Tuesday three things reach your desk.

1. **The upsize.** Your relationship lender offers to raise the facility to 65% LTV on the new appraisal. That is \$208 million of debt, releasing \$32 million of cash. The covenant stays at 70%. The banker mentions that "four or five" other owners in the metro have taken similar upsizes this year and are using the cash to buy hotels in the same metro.
2. **The land.** A landowner offers a pad site zoned for a 120-room hotel at a price equal to its residual land value: completed value less construction cost. The landowner argues that any price at or above residual is fair.
3. **The data.** The latest monthly STR report shows metro RevPAR down 4% year over year. It is the first negative print in 30 months. Your asset manager calls it noise.

You also have the alternative every speculator has: do nothing, keep the 55% facility, and put spare cash in a diversified core real estate fund.

Each item calls on a different mental model. The upsize is a question about **reflexivity**, **forced selling**, and **crowding**. The land is a question about **optionality**. The RevPAR print is a question about **Bayesian updating** and **regime change**. Doing nothing is the **opportunity cost** against which every action must be measured. Section 3.10 returns to the decision.

---

### 3.2 Economic intuition

A mental model is useful to a speculator only if it changes a number in a decision. "Markets are reflexive" is a slogan. "This lending market has a loop gain of 0.63 on the way up and 0.83 on the way down, so a 5% shock becomes 13.5% or 30%" is a model. The chapter treats each idea in this second sense. Each one is a small, explicit mechanism with parameters you can estimate, argue about, and stress.

The models group into four families.

**Valuation against alternatives.** Every action has an opportunity cost: the return on the best thing you are not doing. A hurdle is not a target return chosen to look respectable. It is the return of the next-best alternative at the same risk. A deal that beats an unlevered core fund but loses to the same core fund levered to the deal's risk is a bad deal.

**Dynamics: how prices move through time.** Three patterns recur. *Mean reversion*: deviations from a long-run level decay, at a rate you can measure. *Momentum*: recent returns predict near-term returns with the same sign. *Regimes*: the process generating returns switches between states, each persistent, and the switching probabilities determine how long each state lasts. These patterns are not contradictory. A cap-rate spread can mean-revert over years, trend over months, and behave differently in a credit crunch than in an expansion.

**Feedback: when prices change the fundamentals they are supposed to reflect.** George Soros called this *reflexivity* in *The Alchemy of Finance* (1987). Participants' beliefs move prices (the "manipulative function"), and prices change the reality participants are trying to understand (the "cognitive function") [FACT: Soros (1987); description verified against secondary sources, see ch03-S01]. In credit markets the mechanism is concrete. Real estate is collateral. Higher prices raise borrowing capacity. Borrowed money buys more real estate. Kiyotaki and Moore (1997) formalized the same loop in a macroeconomic model in which durable assets such as land serve both as factors of production and as collateral, so credit limits and asset prices reinforce each other [FACT: ch03-S02]. Forced selling, fire sales, and crowded exits are the same loop running in reverse, with the important difference that repayment is mandatory while borrowing is optional.

**Optionality and belief.** A convex payoff gains more from good outcomes than it loses from bad ones. The right to wait before committing irreversible capital is such a payoff. It has value that a static NPV ignores, which is why vacant land in expensive cities can be rational (Titman, 1985) [FACT: ch03-S09]. Bayesian updating is the discipline that tells you how much a new data point should move your probability of each state. It protects you against the two classic errors: overreacting to a vivid single print and underreacting to an accumulating pattern.

Each model has a failure mode, set out in §3.8. A mental model is a tool for organizing evidence. It does not replace the evidence.

---

### 3.3 Technical definitions

| Term | Definition |
|---|---|
| Opportunity cost | Return forgone on the best feasible alternative use of the same capital, time, and risk budget |
| Risk-matched hurdle | Return of the next-best alternative after levering or de-levering it to the deal's volatility: $h = r_B + (\sigma_D/\sigma_A)(r_A - r_B)$ |
| Reflexivity (operational) | A loop in which the price of an asset changes the fundamentals that determine its price; here, price → collateral → credit → demand → price |
| Loop gain $m$ | Price change in the next round of a feedback loop per unit of price change in the current round |
| Amplification multiplier | Total price change per unit of initial shock, $1/(1-m)$ for $|m|<1$ |
| AR(1) process | $x_t - \mu = \phi (x_{t-1} - \mu) + \varepsilon_t$ with persistence $\phi$ |
| Half-life | Periods for an expected deviation from $\mu$ to halve: $\ln 0.5/\ln\phi$ |
| Time-series momentum (TSMOM) | Position in an asset with the sign of its own trailing return (commonly 12 months), often scaled by inverse volatility |
| Cross-sectional momentum | Long recent winners and short recent losers *relative to each other*; distinct from TSMOM |
| Markov regime model | A model in which a hidden state $s_t$ follows a Markov chain with transition probabilities $p_{ij}$, and each state has its own return or growth distribution |
| Expected regime duration | $1/(1-p_{ii})$ periods |
| Convex payoff | Payoff $f$ with $f(\tfrac{a+b}{2}) \le \tfrac{f(a)+f(b)}{2}$; gains from upside exceed losses from equal downside |
| Option to wait | The right, not the obligation, to make an irreversible investment later rather than now |
| Forced sale | A sale whose timing and size are set by a constraint (covenant, margin, redemption), not by the seller's view of value |
| Price impact | Fall in the clearing price per unit sold, $b$ in $P(s) = P_1 - bs$ |
| Exit capacity | Amount that can be sold per unit of time without more than an accepted price concession, e.g. participation rate × average daily volume |
| Crowded trade | A position held by many investors with similar constraints, so their exits coincide |
| Likelihood ratio (LR) | $P(E\mid H)/P(E\mid \neg H)$; the factor by which evidence $E$ multiplies the odds on $H$ |

---

### 3.4 Equations and derivations

#### 3.4.1 The risk-matched hurdle

Let the next-best alternative earn expected return $r_A$ with volatility $\sigma_A$. If it can be levered or de-levered at rate $r_B$, a position with weight $w$ in the alternative and $1-w$ in borrowing or lending earns $r_B + w(r_A - r_B)$ with volatility $w\sigma_A$. Matching the deal's volatility $\sigma_D$ requires $w = \sigma_D/\sigma_A$, so

$$h = r_B + \frac{\sigma_D}{\sigma_A}(r_A - r_B).$$

This is the deal's opportunity cost at equal risk. Equivalently, the deal must have a Sharpe-type ratio $(r_D - r_B)/\sigma_D$ at least as large as the alternative's. Volatility is a crude risk measure for private real estate (Chapter 2 explains appraisal smoothing). The formula is a floor, not a full risk adjustment: illiquidity, tail risk, and the time you spend running the deal all argue for a higher hurdle.

#### 3.4.2 The reflexive collateral loop

Let $C$ be the value of real estate pledged as collateral in a market, $\lambda$ the LTV lenders will advance against it, $\theta$ the share of new borrowing capacity that owners actually draw and spend on more real estate in the same market, and $\psi$ the fractional price change caused by one unit of net new demand (the inverse of market depth).

A fractional price change $x_k$ in round $k$ changes:

* collateral value by $x_k C$;
* borrowing capacity by $\lambda x_k C$;
* net demand by $\theta \lambda x_k C$;
* the next-round price by $x_{k+1} = \psi\theta\lambda C \, x_k$.

Define the **loop gain** $m = \lambda\theta C\psi$. After an initial shock $x_0$, the cumulative price change after $n$ rounds is the geometric sum

$$X_n = x_0 \sum_{k=0}^{n-1} m^k = x_0\frac{1-m^n}{1-m}, \qquad X_\infty = \frac{x_0}{1-m}\quad (|m|<1).$$

The **stability condition** is $m<1$. At $m \ge 1$ each round is at least as large as the last, and the linear model has no finite end point. In reality the loop ends when something else binds: lenders' capital, a regulator, or buyers' income. The model is linear in $x$ and therefore only a local approximation; large moves change $\lambda$, $\theta$, and $\psi$ themselves.

**Why the loop is stronger downward.** On the way up, $\theta$ is a choice: owners draw only part of their new capacity. On the way down, a borrower whose loan sits at the maximum LTV must *repay* the lost capacity, whatever they think of value. The downside $\theta$ is the share of collateral whose loans are at the constraint, which in a late-cycle market is high. Lenders also cut $\lambda$ after losses, which raises the downside gain further. Brunnermeier and Pedersen (2009) model this asymmetry for traders as "loss spirals" and "margin spirals", in which funding constraints and market illiquidity reinforce each other [FACT: ch03-S08].

#### 3.4.3 Mean reversion and the half-life

For an AR(1) process $x_t - \mu = \phi(x_{t-1}-\mu) + \varepsilon_t$ with $E[\varepsilon_t]=0$, iterating gives

$$E[x_{t+h}\mid x_t] = \mu + \phi^h (x_t - \mu).$$

The half-life $H$ solves $\phi^H = 0.5$:

$$H = \frac{\ln 0.5}{\ln\phi}.$$

Two traps follow. First, $\phi$ is per period, so a quarterly $\phi_q$ implies an annual $\phi_a = \phi_q^4$, and the half-life in years is the quarterly half-life divided by four. Second, $H$ is very sensitive to $\phi$ near one: $dH/d\phi = -\ln 0.5/[\phi(\ln\phi)^2]$, which grows without bound as $\phi\to 1$. The least-squares estimate of $\phi$ is also biased downward in short samples (Kendall, 1954) [FACT: bibliographic, ch03-S10; the commonly quoted first-order size of the bias, about $-(1+3\phi)/n$, is *(verification pending)*]. A downward-biased $\phi$ gives a half-life that is too short, which makes a mean-reversion trade look faster and safer than it is. The chapter's tests reproduce the size of this bias by simulation (Example 3.3).

#### 3.4.4 Time-series momentum

The TSMOM rule studied by Moskowitz, Ooi and Pedersen (2012) takes a position in each instrument with the sign of its own trailing return and sizes it inversely to volatility. Over 58 liquid futures and forwards (equity indices, currencies, commodities, bonds), they report that an instrument's return over the past 1 to 12 months predicts its next-month return with the same sign, and that the effect partly reverses at longer horizons [FACT: ch03-S04]. Later work disputes how much of the reported performance comes from the volatility scaling rather than the sign rule [FACT that the dispute exists: ch03-S04 notes].

With trailing compounded return $R_{12}$, annualized volatility $\sigma$, and target volatility $\sigma^*$:

$$w = \operatorname{sign}(R_{12}) \cdot \frac{\sigma^*}{\sigma}.$$

The weight $w$ is notional exposure per dollar of capital. Momentum is a statement about the conditional mean of returns. It says nothing about value, and it is a separate phenomenon from mean reversion at longer horizons. A spread can trend for a year and revert over five.

#### 3.4.5 Two-state Markov regimes

Let state 1 be expansion and state 2 contraction, with transition matrix

$$\mathbf P = \begin{pmatrix} p_{11} & 1-p_{11}\\ 1-p_{22} & p_{22}\end{pmatrix}.$$

Hamilton (1989) introduced this structure for business-cycle dynamics, with growth rates that shift between discrete states that the econometrician must infer [FACT: ch03-S06].

*Expected duration.* Once in state $i$, the number of periods $D$ spent there is geometric: $P(D = d) = p_{ii}^{d-1}(1-p_{ii})$. So $E[D] = 1/(1-p_{ii})$, and the probability that the regime lasts more than $d$ periods is $p_{ii}^d$.

*Long-run probabilities.* The stationary distribution solves $\pi = \pi\mathbf P$:

$$\pi_1 = \frac{1-p_{22}}{(1-p_{11})+(1-p_{22})}, \qquad \pi_2 = 1-\pi_1.$$

*Forecasts.* The $n$-step transition probabilities are the entries of $\mathbf P^n$. If NOI grows at $g_1$ in expansion and $g_2$ in contraction, expected growth in quarter $k$ from state $i$ is $[\mathbf P^k]_{i1} g_1 + [\mathbf P^k]_{i2} g_2$.

#### 3.4.6 Optionality and the value of waiting

A payoff $\max(V - I, 0)$ is convex in $V$: an option to build. Static NPV compares building now ($V_0 - I_0$) with not building (0). It ignores a third choice: wait, observe $V$, and build only if it is worth building.

One-period binomial model. The completed building is worth $V_0$ today and $uV_0$ or $dV_0$ in one year. Its owner receives a cash yield $\delta V_0$ during the year, which a waiting developer forgoes. Construction costs $I_0$ now or $I_1 = I_0(1+g_I)$ next year. The risk-neutral probability $q$ prices the completed building:

$$V_0 = \frac{\delta V_0 + q\,uV_0 + (1-q)\,dV_0}{1+r_f}\;\;\Rightarrow\;\; q = \frac{V_0(1+r_f) - \delta V_0 - dV_0}{uV_0 - dV_0}.$$

The value of waiting is

$$W = \frac{q\max(uV_0 - I_1, 0) + (1-q)\max(dV_0 - I_1, 0)}{1+r_f},$$

and the developer should build now only if $V_0 - I_0 \ge W$. The **option premium** $W - \max(V_0 - I_0, 0)$ is the value that residual land valuation leaves out. Waiting has three costs: the forgone yield $\delta$, cost inflation $g_I$, and (not modeled here) the risk that someone else uses the site or the entitlement lapses. Dixit and Pindyck (1994) develop the continuous-time version (ch03-S11; bibliographic record *verification pending*).

#### 3.4.7 Forced selling under a leverage covenant

A holder owns $Q_0$ units financed with debt $D$ and must keep $D/(Q P) \le \lambda^*$. After a shock the price is $P_1$ and $D > \lambda^* Q_0 P_1$: the covenant is breached. Selling $s$ units repays $sP$ of debt. With linear price impact, the price after the sale is $P(s) = P_1 - bs$, and we mark all units, sold and retained, at $P(s)$ (a uniform-price simplification). Compliance requires

$$D - sP(s) = \lambda^*(Q_0 - s)P(s) \;\;\Longleftrightarrow\;\; P(s)\,[\lambda^* Q_0 + (1-\lambda^*)s] = D.$$

*No impact* ($b=0$): $s = (D/P_1 - \lambda^* Q_0)/(1-\lambda^*)$. Each dollar of sales cuts debt by a dollar but cuts the *allowed* debt by only $\lambda^*$ dollars, so the gap closes at rate $1-\lambda^*$. At $\lambda^* = 0.75$ you must sell four dollars of assets to close one dollar of covenant gap.

*With impact*, the left side $f(s) = (P_1 - bs)[\lambda^*Q_0 + (1-\lambda^*)s]$ is a downward-opening parabola. Two thresholds matter:

1. **Marginal condition.** Selling helps at the margin only if $f'(0) > 0$: $b < (1-\lambda^*)P_1/(\lambda^* Q_0)$. Above this, the first unit sold *worsens* the covenant, because the price impact on the retained position exceeds the debt repaid.
2. **Feasibility.** A cure exists only if the maximum of $f$ reaches $D$. The maximum is $[(1-\lambda^*)P_1 + b\lambda^*Q_0]^2 / [4b(1-\lambda^*)]$, so the critical impact $b^\dagger$ solves the quadratic $[(1-\lambda^*)P_1 + b\lambda^*Q_0]^2 = 4b(1-\lambda^*)D$ (take the smaller root). For $b > b^\dagger$ no partial sale cures the breach. The holder is liquidated or the lender must waive.

Shleifer and Vishny (1992) explain why $b$ is large exactly when forced sales occur: the natural buyers of a distressed asset are firms in the same industry, and they tend to be constrained at the same time [FACT: ch03-S07].

#### 3.4.8 Exit capacity

If an asset trades an average daily volume $ADV$ and you can sell at a participation rate $\rho$ without more than an accepted concession, a position $X$ takes $T = X/(\rho\,ADV)$ days to exit. When $N$ holders with total position $\sum X_j$ exit at the same time and the market absorbs at most $\rho\,ADV$ of net selling per day, the relevant number is $\sum X_j/(\rho\,ADV)$, not your own $T$. For private real estate replace $ADV$ with annual transaction volume in the submarket and property type.

#### 3.4.9 Bayesian updating in odds form

Bayes' rule in odds form is

$$\underbrace{\frac{P(H\mid E)}{P(\neg H\mid E)}}_{\text{posterior odds}} = \underbrace{\frac{P(H)}{P(\neg H)}}_{\text{prior odds}} \times \underbrace{\frac{P(E\mid H)}{P(E\mid\neg H)}}_{LR}.$$

For signals $E_1,\dots,E_n$ that are **conditionally independent** given $H$, the LRs multiply, and the order of arrival does not matter. Log-odds add: $\ell_n = \ell_0 + \sum_k \ln LR_k$. A simple model of biased updating scales each log-LR by a weight $\omega$: $\omega = 1$ is Bayesian, $\omega<1$ is under-reaction (conservatism), $\omega>1$ is over-reaction. Barberis, Shleifer and Vishny (1998) built a model in which investors produce both under-reaction to individual news and over-reaction to a series of news in the same direction [FACT: ch03-S05]. If the signals are correlated, multiplying their LRs double-counts the shared information. That is over-reaction by construction, even when each LR is individually correct.

#### 3.4.10 Negative feedback with a lag

Not all feedback amplifies. High hotel RevPAR draws new supply, which lowers RevPAR, with a construction lag. If a deviation $x_t$ of RevPAR from its long-run level produces supply that changes the next period's deviation by $-g x_t$, then $x_{t+1} = -g x_t$. For $0<g<1$ the deviation oscillates with shrinking amplitude. With $g = 0.8$ and a +10% starting deviation, the path is +10%, −8%, +6.4%, −5.12%. For $g>1$ the oscillation grows, the classic cobweb instability [HYPOTHESIS: illustrative parameters]. A lagged supply response is stabilizing in the long run and destabilizing in the short run. Developers who all respond to the same high RevPAR deliver into the same down-phase.

---

### 3.5 Worked examples

All inputs are [HYPOTHESIS] unless cited. All ten examples are reproduced in `tests/test_ch03_examples.py`.

#### Example 3.1 — Opportunity cost: the risk-matched hurdle

**Given.** \$10 million of fund equity. The next-best alternative is a diversified core open-end real estate fund with expected net return $r_A = 7.0\%$ and volatility $\sigma_A = 8\%$. The fund can borrow on a subscription or NAV line at $r_B = 5.5\%$. The deal is a value-add hotel acquisition with expected levered equity IRR 11.0% and estimated volatility $\sigma_D = 16\%$ (twice the alternative's). Five-year horizon.

**Find.** The risk-matched hurdle; the terminal wealth of the deal and of the matched alternative; the verdict if the deal's IRR were 8.0%.

**Solution.**

$$h = r_B + \frac{\sigma_D}{\sigma_A}(r_A - r_B) = 5.5\% + \frac{16}{8}(7.0\% - 5.5\%) = 5.5\% + 3.0\% = 8.5\%.$$

Terminal wealth over five years, compounding annually:

* Deal: $10 \times 1.11^5 = 10 \times 1.68506 = \$16.85$ million.
* Matched alternative: $10 \times 1.085^5 = 10 \times 1.50366 = \$15.04$ million.
* Excess: \$1.81 million, or \$1.21 million in present value at the 8.5% hurdle ($1.814/1.50366$).

At an IRR of 8.0% the deal clears the *unlevered* alternative (7.0%) by 1.0 percentage point and fails the *risk-matched* one (8.5%) by 0.5 point.

**Check.** Sharpe-type ratios: alternative $(7.0 - 5.5)/8 = 0.1875$; deal at 11%: $(11.0-5.5)/16 = 0.344$; deal at 8%: $(8.0-5.5)/16 = 0.156 < 0.1875$. ✓

**Decision consequence.** The natural comparison, "11% versus 7%", overstates the deal's edge. The correct comparison is 11% versus 8.5%, a 2.5-point margin that must still pay for illiquidity, the hotel's operating risk beyond volatility, and the hours of asset management the core fund does not require. An 8% hotel deal should be rejected even though it "beats core". Write the risk-matched hurdle into the investment memo before you see the deal's IRR, so the hurdle is not adjusted to fit the deal.

#### Example 3.2 — Reflexivity as a collateral loop: iteration and the stability condition

**Given.** In a metro hotel market, collateral pledged to lenders is $C = 100$ (\$ billions is convenient, but any unit works as long as $\psi$ matches). Lenders advance $\lambda = 0.70$ against appraised value. Owners draw and spend $\theta = 0.60$ of any new capacity on more local hotels. Each \$1 billion of net new demand raises prices by 1.5%, so $\psi = 0.015$ per \$ billion. An initial demand shock raises prices by $x_0 = 5\%$.

**Find.** The loop gain; the first five rounds; the total effect; the gain if credit loosens to $\lambda = 0.85$ and $\theta = 0.80$.

**Solution.**

$$m = \lambda\theta C\psi = 0.70 \times 0.60 \times 100 \times 0.015 = 0.63.$$

In words: a 1% price rise adds \$1.0 billion of collateral, \$0.70 billion of capacity, and \$0.42 billion of spending, which raises prices by $0.42 \times 1.5\% = 0.63\%$.

| Round $k$ | Increment $x_0 m^k$ | Cumulative |
|---|---|---|
| 0 | 5.000% | 5.000% |
| 1 | 3.150% | 8.150% |
| 2 | 1.985% | 10.135% |
| 3 | 1.250% | 11.385% |
| 4 | 0.788% | 12.172% |
| ∞ | — | $5\%/(1-0.63) = 13.51\%$ |

The multiplier is $1/(1-0.63) = 2.70$: a 5% fundamental shock becomes a 13.5% price move.

With looser credit: $m = 0.85 \times 0.80 \times 100 \times 0.015 = 1.02 > 1$. The loop is unstable. Each round is larger than the last, and nothing inside the model stops it.

**Check.** After rounds 0–4 (five terms) the cumulative is $5\% \times (1-0.63^5)/(1-0.63) = 12.17\%$, matching the table. ✓

**Decision consequence.** The gain depends on lender behavior ($\lambda$), owner behavior ($\theta$), and market depth ($\psi$), not on hotel fundamentals. A rise in permitted LTV from 70% to 85% does not merely add 15 points of leverage. Combined with more aggressive drawing, it moves the market across the stability boundary. For the opening problem, the lender's offer to move from 55% to 65% is one fund's contribution to $\lambda$, and "four or five other owners doing the same" is $\theta$ rising. The question to ask is not "is 65% LTV safe for my fund?" but "what is the market's loop gain once everyone does this, and what happens when it runs in reverse?" Section 3.7 answers the second half.

#### Example 3.3 — Mean reversion: the half-life of a cap-rate spread

**Given.** You model the spread between a hotel cap-rate series and the 10-year Treasury yield as a quarterly AR(1) with long-run mean $\mu = 3.0\%$ and persistence $\phi = 0.90$, estimated on 80 quarters [HYPOTHESIS: illustrative parameters, not an estimate from published data]. The current spread is 2.0%. The Treasury is 4.5% and assumed constant. NOI is held constant.

**Find.** The half-life; the expected spread and cap rate in 4 and 8 quarters; the implied value change over 8 quarters; the same with $\phi = 0.97$; and the size of the small-sample bias in $\hat\phi$.

**Solution.**

Half-life: $H = \ln 0.5/\ln 0.90 = -0.69315/-0.10536 = 6.58$ quarters (1.64 years).

Expected spread: $E[x_{t+h}] = 3.0\% + 0.90^h(2.0\% - 3.0\%)$.

* $h=4$: $0.90^4 = 0.6561$; spread $= 3.0\% - 0.656\% = 2.344\%$; cap rate 6.844%.
* $h=8$: $0.90^8 = 0.43047$; spread $= 3.0\% - 0.430\% = 2.570\%$; cap rate $4.5\% + 2.570\% = 7.070\%$.

Value change with constant NOI: $V_8/V_0 = c_0/c_8 = 6.5\%/7.0695\% = 0.9194$, a decline of 8.06%.

With $\phi = 0.97$: $H = \ln 0.5/\ln 0.97 = 22.76$ quarters (5.7 years). In 8 quarters the spread is $3.0\% - 0.97^8 \times 1.0\% = 3.0\% - 0.784\% = 2.216\%$, the cap rate 6.716%, and the value change $6.5/6.7163 - 1 = -3.22\%$.

Annual persistence: $0.90^4 = 0.656$ per year. A model that mistakes the quarterly 0.90 for an annual coefficient would give a half-life of 6.58 *years* rather than quarters.

Small-sample bias: in 4,000 simulated 80-quarter paths with true $\phi = 0.90$ (random seed fixed in the tests), the average OLS estimate is about 0.85. The test asserts it lies between 0.83 and 0.87. A true $\phi$ of about 0.95 can therefore produce an estimate near 0.90. At $\phi = 0.95$ the half-life is 13.5 quarters, twice the estimate.

**Check.** $0.90^{6.58} = 0.500$. ✓ Reverse check on value: $6.5/0.9194 = 7.0695$. ✓

**Decision consequence.** A buyer who believes the spread is "too tight" and will revert is making a forecast whose horizon depends on $\phi$. At 0.90 the reversion costs 8% of value within two years. At 0.97 it costs 3%. The two cases call for different actions: at $\phi = 0.90$, wait or bid lower; at $\phi = 0.97$, the reversion is slow enough that NOI growth may offset it. Because estimated $\phi$ is biased toward faster reversion, a mean-reversion *trade* (betting on a quick snap-back) needs a margin of safety in time as well as price: size it to survive at least twice the estimated half-life.

#### Example 3.4 — Time-series momentum: sizing a listed hotel REIT position

**Given.** A listed lodging REIT index had these monthly total returns over the past 12 months: +6.3%, −3.9%, +10.2%, +2.4%, −8.1%, +4.5%, +3.6%, −1.2%, +7.8%, +2.7%, −5.4%, +3.3% [HYPOTHESIS]. You run a \$10 million liquid sleeve with a 10% annualized volatility target. Volatility is estimated from the same 12 months.

**Find.** The trailing 12-month return, annualized volatility, the TSMOM signal, and the notional position.

**Solution.**

Trailing return $= \prod(1+r_t) - 1 = 22.59\%$. (The arithmetic sum is 22.2%; compounding adds 0.4 point.)

Volatility: sample monthly standard deviation $= 5.494\%$; annualized $5.494\% \times\sqrt{12} = 19.03\%$.

Signal $= +1$. Weight $= 10\%/19.03\% = 0.5254$. Notional long $= 0.5254 \times \$10\text{ million} = \$5.25$ million.

If the same returns had the opposite sign, trailing return −21.43%, the position would be \$5.25 million short.

**Check.** Ex-ante position volatility $= 0.5254 \times 19.03\% = 10.0\%$ of the sleeve. ✓

**Decision consequence.** The momentum rule produces a number. Whether to use it depends on what the published evidence covers. Moskowitz, Ooi and Pedersen studied liquid futures, not REITs, and not private real estate. Applying their result to a single REIT index is an extrapolation [INFERENCE]. Two uses are defensible. As a *speculation*, a volatility-scaled TSMOM position is a small, diversifying sleeve with a known rule and a stop built into the signal. As an input to a *hedging* decision, the signal tells you the cost of carrying a short REIT hedge against your private hotels: you are shorting into a positive trend. That does not mean you should not hedge. A hedge is justified by the exposure, not by the signal (Chapter 1). It does mean the hedge's expected carry is negative while the trend persists. Private hotel values, which are appraisal-based, show positive autocorrelation partly because of smoothing (Chapter 2). That is a measurement artifact, not tradeable momentum.

#### Example 3.5 — Regime change: durations, long-run odds, and NOI growth

**Given.** A two-state quarterly Markov model of a hotel market: expansion (state 1) with $p_{11} = 0.95$ and NOI growth $g_1 = +4\%$ per year; contraction (state 2) with $p_{22} = 0.80$ and NOI growth $g_2 = -10\%$ per year [HYPOTHESIS]. Quarterly growth is the annual figure divided by four (a simple-rate approximation).

**Find.** Expected durations; long-run probabilities; the probability of being in contraction 1–4 quarters ahead from each state; expected NOI growth over the next year from each state; the probability that a contraction already under way lasts more than 8 more quarters; the probability that an expansion lasts more than 20 more quarters.

**Solution.**

Durations: $E[D_1] = 1/(1-0.95) = 20$ quarters (5 years); $E[D_2] = 1/(1-0.80) = 5$ quarters.

Stationary: $\pi_1 = 0.20/(0.05+0.20) = 0.80$; $\pi_2 = 0.20$.

$P(\text{contraction in } k \text{ quarters})$ from $\mathbf P^k$:

| $k$ | From expansion | From contraction |
|---|---|---|
| 1 | 0.0500 | 0.8000 |
| 2 | 0.0875 | 0.6500 |
| 3 | 0.1156 | 0.5375 |
| 4 | 0.1367 | 0.4531 |

Expected NOI growth over the next four quarters, $\sum_{k=1}^4 \tfrac14[\Pr(\text{exp})g_1 + \Pr(\text{con})g_2]$:

* From expansion: average contraction probability $= (0.05+0.0875+0.1156+0.1367)/4 = 0.0975$; growth $= 0.9025 \times 4\% + 0.0975 \times (-10\%) = +2.64\%$.
* From contraction: average contraction probability $= 0.6102$; growth $= 0.3898 \times 4\% + 0.6102 \times (-10\%) = -4.54\%$.

Survival: $P(\text{contraction lasts} > 8 \text{ more quarters}) = 0.80^8 = 0.168$. $P(\text{expansion lasts} > 20 \text{ more quarters}) = 0.95^{20} = 0.358$.

**Check.** Stationarity: $0.80 \times 0.05 = 0.04 = 0.20 \times 0.20$. Flows out of each state balance. ✓

**Decision consequence.** The same hotel has a 7.2-point difference in expected first-year NOI growth depending on the regime you are in today. Regime identification is therefore worth more than refining the growth assumption within a regime. That is the link to Bayesian updating (Example 3.10): the RevPAR print in the opening problem is evidence about *which regime* you are in. For debt structuring, a 16.8% chance that a contraction runs more than two more years is the number that sizes an interest reserve or argues against a loan maturing in 24 months. The memoryless geometric duration is itself an assumption. Real downturns may have duration dependence (§3.8).

#### Example 3.6 — Optionality: the value of waiting on a development parcel

**Given.** The pad site in the opening problem supports a hotel that would be worth $V_0 = \$42.0$ million if completed today (treat construction as instantaneous to isolate the option). Construction cost is $I_0 = \$40.0$ million today, rising 3% to $I_1 = \$41.2$ million next year. In one year the completed value will be $1.25 V_0 = \$52.5$ million or $0.80 V_0 = \$33.6$ million. A completed hotel yields $\delta = 6\%$ cash per year on $V_0$ (\$2.52 million), which a waiting owner forgoes. The risk-free rate is 4%.

**Find.** Static NPV (residual land value); the risk-neutral probability; the value of waiting; the option premium; a replication check.

**Solution.**

Residual land value (build now): $V_0 - I_0 = 42.0 - 40.0 = \$2.0$ million.

Risk-neutral probability:

$$q = \frac{42.0 \times 1.04 - 2.52 - 33.6}{52.5 - 33.6} = \frac{43.68 - 36.12}{18.9} = \frac{7.56}{18.9} = 0.40.$$

Payoffs from waiting: up $\max(52.5 - 41.2, 0) = 11.3$; down $\max(33.6 - 41.2, 0) = 0$.

$$W = \frac{0.40 \times 11.3 + 0.60 \times 0}{1.04} = \frac{4.52}{1.04} = \$4.346\text{ million}.$$

Option premium $= 4.346 - 2.0 = \$2.346$ million. Waiting is worth more than building.

**Check (replication).** Hold $\Delta$ units of the completed asset and a bond $B$ so that the portfolio matches the waiting payoff in both states (the asset pays its 2.52 cash yield in both):

$$\Delta = \frac{11.3 - 0}{52.5 - 33.6} = 0.59788, \qquad B = \frac{0 - 0.59788 \times (33.6 + 2.52)}{1.04} = -20.765.$$

Value $= 0.59788 \times 42.0 - 20.765 = 25.111 - 20.765 = \$4.346$ million. ✓

**Decision consequence.** The landowner's claim that residual value (\$2.0 million) is a fair price is wrong in the landowner's *favor*. The land is worth about \$4.35 million to a developer who can wait, because residual valuation assumes the build-now decision must be made today. A seller who prices land at residual is selling the option for nothing. That is a reason to buy, *if* the option is real: the entitlement must survive the wait, no competitor can pre-empt the demand, and you can carry the land. The same logic says you should not *build* on the site today even though NPV is positive. Build-now becomes optimal only when the forgone yield or cost inflation is high enough, or uncertainty low enough, that $V_0 - I_0 \ge W$ (Problem 3.6 finds the break-even yield).

#### Example 3.7 — Forced selling: a margin call meets a downward-sloping demand curve

**Given.** A leveraged fund holds $Q_0 = 100$ units of a CRE bond position (think of a block of CMBS or a pool of loans financed on repo) at \$100 per unit, so the position is worth \$10,000 (\$000). Debt is $D = \$7{,}000$ (70% LTV). The lender requires LTV ≤ 75%. A market shock drops the price to $P_1 = \$92$. Buyers absorb sales along $P(s) = 92 - b s$.

**Find.** The breach; units to sell with $b = 0$ and with $b = 0.15$; post-sale price and equity; the marginal impact threshold; the feasibility threshold.

**Solution.**

After the shock: value $= 100 \times 92 = 9{,}200$; LTV $= 7{,}000/9{,}200 = 76.09\% > 75\%$. Equity has fallen from 3,000 to 2,200.

*No impact:* $s = (7{,}000/92 - 0.75 \times 100)/(1 - 0.75) = (76.087 - 75)/0.25 = 4.35$ units.

*With $b = 0.15$:* solve $(92 - 0.15s)(75 + 0.25s) = 7{,}000$. Expanding: $6{,}900 + 23s - 11.25s - 0.0375s^2 = 7{,}000$, so $0.0375s^2 - 11.75s + 100 = 0$ and

$$s = \frac{11.75 - \sqrt{11.75^2 - 4(0.0375)(100)}}{2(0.0375)} = \frac{11.75 - \sqrt{123.0625}}{0.075} = \frac{11.75 - 11.0934}{0.075} = 8.755\text{ units}.$$

Post-sale price $= 92 - 0.15 \times 8.755 = \$90.687$. Equity $= 100 \times 90.687 - 7{,}000 = \$2{,}068.7$, a further loss of \$131.3 caused purely by the fund's own selling.

Thresholds:

* Marginal: $b < (1-0.75)\times 92/(0.75 \times 100) = 23/75 = 0.3067$.
* Feasibility: $[23 + 75b]^2 = 4b(0.25)(7{,}000)$, i.e. $5{,}625 b^2 - 3{,}550 b + 529 = 0$, giving $b^\dagger = (3{,}550 - \sqrt{700{,}000})/11{,}250 = 0.2412$.

At $b = 0.30$ the marginal condition still holds (0.30 < 0.3067) but no sale cures the breach (0.30 > 0.2412). The fund is driven to full liquidation or must obtain a waiver.

**Check.** At $s = 8.755$: debt after sale $= 7{,}000 - 8.755 \times 90.687 = 6{,}206.0$; value retained $= 91.245 \times 90.687 = 8{,}274.7$; LTV $= 75.0\%$. ✓

**Decision consequence.** Price impact *doubled* the forced sale, from 4.35 to 8.76 units, and the fund's own selling cost it 6% of its remaining equity. Above $b^\dagger$, a modest-looking 8% price drop on a 70% LTV position becomes a wipe-out. The lesson for the opening problem is direct. At 65% LTV against a 70% covenant, the buffer before a forced paydown is a value decline of only $1 - 0.65/0.70 = 7.1\%$. At 55% LTV it is $1 - 0.55/0.70 = 21.4\%$. Private hotels have no continuous price, but a fresh appraisal after a soft year plays the role of $P_1$, and the paydown must be funded by selling hotels into a market where other owners face the same appraisal. A covenant buffer should be sized against the *combined* shock: the market move plus the impact of everyone's forced sales.

#### Example 3.8 — Crowded trades: exit capacity versus position size

**Given.** (a) A listed hotel REIT trades \$40 million per day on average. You hold \$60 million. You will not exceed 20% of daily volume without accepting a concession. Twelve similar funds hold the stock with an aggregate \$720 million, including yours. (b) Private market: select-service hotel transaction volume in your metro averages \$450 million a year. You own \$200 million of such hotels. Above 25% of annual market volume, you expect prices to concede [HYPOTHESIS].

**Find.** Days to exit alone and when the crowd exits together; the maximum position exitable in five days alone and with a 1/12 share of capacity; years to exit the private portfolio.

**Solution.**

(a) Alone: $T = 60/(0.20 \times 40) = 7.5$ days. Crowd exiting together: $720/(0.20 \times 40) = 90$ days. Maximum position for a five-day exit alone: $40 \times 0.20 \times 5 = \$40$ million. With one-twelfth of capacity: $\$40/12 = \$3.33$ million.

(b) $T = 200/(0.25 \times 450) = 1.78$ years.

**Check.** At a one-twelfth share of capacity your \$60 million takes $60/(8/12) = 90$ days, the same as the crowd's aggregate figure. Equal shares exit together. ✓

**Decision consequence.** Liquidity measured on your own position (7.5 days) is the number you see in normal times. The relevant number in a stress is the crowd's (90 days), and you cannot observe it directly. You infer it from ownership filings, from lender conversations ("four or five other owners"), and from how similar your constraints are to theirs. Size positions so that exit time *under crowding* is shorter than the time your funding can survive a drawdown. In private CRE the arithmetic is starker: \$200 million in a \$450 million-a-year market is almost two years of disciplined selling. A fund with a maturity, covenant, or redemption inside that window is not holding a liquid position.

#### Example 3.9 — Second-order consequences: rate rise → refinancing → bank lending

**Given.** First order: an office loan of \$31.2 million was made in 2021 at 65% LTV against a \$48.0 million value (NOI \$2.4 million, 5.0% cap rate), interest-only at 4.0%. At maturity, the market lends at 6.5% on 30-year amortization, with maximum 65% LTV, minimum 1.35x DSCR, and minimum 9.0% debt yield, and the cap rate is 6.25%. NOI is unchanged. Second order: a regional bank holds \$500 million of similar loans maturing over two years. Borrowers on 60% of the balance inject equity to cover their gaps. The other 40% default or extend, with expected loss of 15% of balance. The bank holds capital equal to 10% of loans. Third order: new acquisitions in the bank's markets are financed at 60% LTV [HYPOTHESIS for all inputs].

**Find.** Original DSCR; new value; maximum new loan and the binding constraint; refinancing gap; the bank's capital loss and lending-capacity reduction; the acquisitions that lose financing.

**Solution.**

*First order: the loan.*

Original DSCR $= 2{,}400{,}000/(0.04 \times 31{,}200{,}000) = 2{,}400{,}000/1{,}248{,}000 = 1.92$x.

New value $= 2{,}400{,}000/0.0625 = \$38.4$ million.

Loan constant at 6.5%, 30 years, monthly $= 0.075848$.

* LTV: $0.65 \times 38.4 = \$24.96$ million.
* DSCR: $2{,}400{,}000/1.35/0.075848 = \$23.44$ million.
* Debt yield: $2{,}400{,}000/0.09 = \$26.67$ million.

Maximum loan $= \$23.44$ million (DSCR binds). Gap $= 31.20 - 23.44 = \$7.76$ million, 24.9% of the old balance.

*Second order: the bank.*

Aggregate gap on \$500 million $= 0.2488 \times 500 = \$124.4$ million. Borrowers on \$300 million cover gaps of $0.6 \times 124.4 = \$74.6$ million, which pays down the bank's book. The remaining \$200 million produce expected losses of $0.15 \times 200 = \$30$ million. At 10% capital, lending capacity falls by $30/0.10 = \$300$ million.

*Third order: the market.*

At 60% LTV, \$300 million of loans would have financed $300/0.60 = \$500$ million of acquisitions. That demand must find another lender or disappear.

**Check.** At \$23.44 million, debt service $= 23.44 \times 0.075848 = \$1.778$ million, and $2.4/1.778 = 1.35$x. ✓

**Decision consequence.** The first-order effect of a rate rise (higher debt cost) is the one everyone models. The second-order effect, a \$30 million capital hit at one bank, removes ten times its size in lending capacity. The third-order effect is \$500 million of buyers without financing in the same markets where defaulted collateral must be sold. That is the reflexive loop of Example 3.2 running downward through the banking system. For a speculator the chain identifies *where* opportunity appears and *when*: not at the first rate rise, but when bank capital constraints bind and lenders sell loans or foreclose into a market with fewer financed bidders (Chapter 12). For an owner it says that refinancing risk is correlated across borrowers through their lenders. Your own loan's DSCR is not a sufficient statistic.

#### Example 3.10 — Bayesian updating over three data points

**Given.** The opening problem's metro. Hypothesis $H$: the market has entered a supply-driven downturn. Prior $P(H) = 0.20$, from the base rate of such downturns in similar markets [HYPOTHESIS]. Three signals arrive over six weeks, assumed conditionally independent given the state:

| Signal | $P(E\mid H)$ | $P(E\mid\neg H)$ | LR |
|---|---|---|---|
| 1. Metro RevPAR −4% year over year | 0.60 | 0.20 | 3.0 |
| 2. A new 150-room hotel breaks ground nearby | 0.30 | 0.20 | 1.5 |
| 3. Group-booking pace for next year is up | 0.25 | 0.50 | 0.5 |

A hotel you are bidding on is worth \$24.0 million if $H$ is false and \$18.0 million if $H$ is true. The seller asks \$21.0 million. You require expected value to exceed the price by 5%.

**Find.** The posterior after each signal; the maximum bid; the same under over-reaction ($\omega = 2$) and under-reaction ($\omega = 0.5$).

**Solution.**

Prior odds $= 0.20/0.80 = 0.25$.

* After signal 1: odds $= 0.25 \times 3.0 = 0.75$; $P = 0.75/1.75 = 0.4286$. Check with the full form: $0.6 \times 0.2/(0.6 \times 0.2 + 0.2 \times 0.8) = 0.12/0.28 = 0.4286$. ✓
* After signal 2: odds $= 0.75 \times 1.5 = 1.125$; $P = 0.5294$.
* After signal 3: odds $= 1.125 \times 0.5 = 0.5625$; $P = 0.36$.

Expected value $= 24.0 - 6.0P$. At $P = 0.36$: $E[V] = 24.0 - 2.16 = \$21.84$ million. Maximum bid $= 21.84/1.05 = \$20.80$ million. The ask of \$21.0 million fails the test, narrowly.

Biased updaters apply $LR^\omega$:

| Updater | Posterior path | Final $P$ | $E[V]$ | Max bid | Bids at ask? |
|---|---|---|---|---|---|
| Bayesian ($\omega = 1$) | 0.429, 0.529, 0.360 | 0.360 | \$21.84m | \$20.80m | No |
| Over-reacting ($\omega = 2$) | 0.692, 0.835, 0.559 | 0.559 | \$20.65m | \$19.67m | No |
| Under-reacting ($\omega = 0.5$) | 0.302, 0.347, 0.273 | 0.273 | \$22.36m | \$21.30m | Yes |

**Check.** Order invariance: the product of LRs is $3.0 \times 1.5 \times 0.5 = 2.25$; $0.25 \times 2.25 = 0.5625$, so $P = 0.36$ whatever the order. ✓

**Decision consequence.** The disciplined bid is about \$20.8 million. The over-reactor bids \$1.1 million less and probably loses the deal. The under-reactor pays the ask, \$0.2 million above the disciplined maximum, and carries a downturn probability about a quarter too low (0.273 against 0.36). Two practical points matter more than the arithmetic. First, the LRs are themselves estimates. Writing them down *before* the data arrive is what prevents you from adjusting them to fit a conclusion. Second, independence is doubtful. If the RevPAR decline partly *reflects* new supply already open, signals 1 and 2 share information, and multiplying their LRs overstates the evidence. A conservative treatment uses only the larger of the two (LR 3.0) and gives a posterior of 0.273. The difference between 0.36 and 0.273 is the cost of not knowing the dependence structure. It is a reason to buy better data, such as the STR supply pipeline, before bidding.

---

### 3.6 CRE application: one hotel market through all the models

Return to the metro in the opening problem and assemble the pieces.

**The loop, both directions.** Suppose pledged hotel collateral in the metro is \$4,000 million, typical LTV is $\lambda = 0.65$, and each \$1 million of net demand moves prices by 0.04% ($\psi = 0.0004$ per \$ million) [HYPOTHESIS]. On the way up, owners draw half their new capacity ($\theta_{up} = 0.5$):

$$m_{up} = 0.65 \times 0.5 \times 4{,}000 \times 0.0004 = 0.52, \qquad \text{multiplier} = 1/(1-0.52) = 2.08.$$

On the way down, assume 80% of collateral sits in loans at or near the LTV covenant, so lost capacity must be repaid ($\theta_{down} = 0.8$):

$$m_{down} = 0.65 \times 0.8 \times 4{,}000 \times 0.0004 = 0.832, \qquad \text{multiplier} = 1/(1-0.832) = 5.95.$$

A 5% fundamental decline becomes a $5\% \times 5.95 = 29.8\%$ price decline, against $10.4\%$ for a 5% rise. The linear model overstates precision at that size, but the asymmetry is the point: **borrowing is optional, repayment is not.** If lenders also cut $\lambda$ after losses, $m_{down}$ rises further.

**Your fund's position in the loop.** Taking the upsize to 65% raises fund debt from \$176 million to \$208 million. A value decline $d$ breaches the 70% covenant when $0.65/(1-d) > 0.70$, i.e. $d > 7.14\%$. In the downside loop above, a fundamental shock of only $7.14\%/5.95 = 1.2\%$ is enough to push values past that point. At 55% LTV the breach requires $d > 21.4\%$, a fundamental shock of $21.4\%/5.95 = 3.6\%$. Neither is comfortable. The upsize roughly triples your sensitivity to a shock that, by Example 3.10, now has a posterior probability of about one in three.

**The regime question.** Under Example 3.5's parameters, a breach is most likely in a contraction, which lasts five quarters on average and more than two years with probability 0.168. A covenant cure that requires selling hotels in that window means selling into the crowded exit of Example 3.8.

**The land.** The option to wait on the pad site (Example 3.6) is worth more, not less, in the same environment. Higher uncertainty raises the value of waiting, and the landowner is pricing at residual. The two decisions point in opposite directions: be *less* levered on the operating portfolio, and *more* willing to own an option whose cost is small and whose downside is limited to the premium paid.

**The opportunity cost.** The \$32 million the upsize would release must beat the risk-matched hurdle of Example 3.1 *after* adding the cost of the extra covenant risk to the existing \$320 million portfolio. A deal that would earn 11% on \$32 million but adds a 1-in-10 chance of a forced \$30 million paydown at a 15% discount does not clear it. Problem 3.10 asks you to put numbers on that trade-off.

---

### 3.7 Feedback loops in general

A feedback loop exists when the output of a process changes its own input. Classify every loop you meet by **sign**, **gain**, and **lag**.

| Loop | Sign | Typical gain driver | Lag | CRE example |
|---|---|---|---|---|
| Collateral → credit → price | Positive | LTV, draw rate, market depth | Appraisal cycle (months) | Example 3.2; Japan, §3.9 |
| Margin call → forced sale → price | Positive | Leverage, price impact | Days (securities) to quarters (private) | Example 3.7 |
| Rent → supply → rent | Negative | Development elasticity | Construction (2–4 years) | §3.4.10 cobweb |
| Price → valuation-based fees and marks → fundraising → demand | Positive | Investor return chasing | Fundraising cycle | Open-end fund inflows and redemptions |
| Defaults → bank capital → lending → price | Positive | Capital ratio | Quarters | Example 3.9 |

Positive loops with short lags produce crashes. Negative loops with long lags produce oscillations. The worst environments combine a positive credit loop with a negative supply loop that arrives late: credit inflates prices, prices call forth supply, and the supply arrives just as credit reverses.

---

### 3.8 When the relationships fail

1. **Opportunity cost with no true alternative.** The risk-matched hurdle assumes the alternative can be levered at $r_B$ and that volatility captures risk. Neither holds for illiquid, fat-tailed positions. The hurdle is then a floor, and judgment must add a premium.
2. **Reflexive loops are not constant-gain.** $\lambda$, $\theta$, and $\psi$ change with the state of the market, especially near turning points. Loop gains estimated in a boom understate the bust. The Kiyotaki–Moore amplification result is itself disputed: a re-examination argues that the original model shows strong amplification only for some parameter settings [FACT: ch03-S02 notes].
3. **Mean reversion fails when the mean moves.** A spread "reverts" to a mean that is a property of the sample. After a structural break (a change in the inflation regime, in bank regulation, or in demand for a property type), the old mean is irrelevant. Post-2020 office is the obvious example (Chapter 23). Estimated $\phi$ is also biased toward faster reversion in short samples.
4. **Momentum fails at turning points.** Trend rules lose money in reversals, and the reported evidence partly reflects volatility scaling. Momentum evidence from liquid futures does not transfer to appraisal-based private indices.
5. **Regime models assume memorylessness.** The geometric duration implies that a regime is no more likely to end after eight quarters than after one. Real cycles may have duration dependence, and parameters estimated on a few regime switches are imprecise. With only three or four observed contractions, $p_{22}$ is barely identified.
6. **Optionality can be illusory.** The option to wait is worth nothing if the entitlement expires, a competitor takes the demand, or carrying costs are high. It is worth less if you cannot actually observe the value signal you would wait for.
7. **Forced-selling models omit the counterparty.** A lender may waive rather than force a sale when it expects fire-sale losses itself. Extend-and-pretend is a real-world response that the covenant arithmetic ignores. It postpones the loop without removing it.
8. **Crowding is unobservable in advance.** Exit capacity depends on others' positions and constraints, which are mostly private. Overlap estimates from filings are lagged and incomplete.
9. **Bayesian updating fails with bad likelihoods.** Correct arithmetic on wrong or dependent LRs gives confidently wrong posteriors. A prior from the wrong reference class does the same.

---

### 3.9 Historical episode: Japan's land and stock bubble, 1985–1992

**Date and environment.** The yen appreciated sharply after the Plaza Accord of September 1985 and Japan entered a slowdown. The Bank of Japan cut its official discount rate five times between January 1986 and February 1987 to offset the strong-yen recession, reaching 2.5%, then a postwar low. It held the rate at 2.5% for about two years and three months, until May 1989 [FACT: Okina, Shirakawa and Shiratsuka (2001), Bank of Japan IMES; ch03-S03, VERIFIED-SECONDARY via search excerpts of the paper]. The rate was then raised in steps to 6.0% by August 1990 [FACT: same source].

**Prices.** The Nikkei 225 closed at a record 38,915.87 on 29 December 1989 [FACT: ch03-S12, contemporary news reports of the 2024 record that cite the 1989 close]. It reached 14,309 in August 1992 [FACT: ch03-S13, secondary press reports; class C source], a decline of $1 - 14{,}309/38{,}915.87 = 63.2\%$. Commercial land prices in Japan's six largest cities, as measured by the Japan Real Estate Institute's urban land price index, peaked in September 1990 at almost four times their September 1985 level [FACT: ch03-S03, as reported in the Bank of Japan IMES study; VERIFIED-SECONDARY]. Secondary sources report declines in big-city commercial land prices of 70% to more than 80% from the peak by the early-to-mid 2000s, depending on the end point *(verification pending: exact figure against the JREI series)*.

**Financing and the collateral loop.** Japanese bank lending relied heavily on real estate collateral. As land prices rose, borrowing capacity rose with them [INFERENCE: the collateral mechanism is the subject of ch03-S02 and ch03-S14; Kanaya and Woo (2000) describe deregulation leading banks to take more risk, including increased lending to real estate, ch03-S15]. Gan (2007) uses the collapse of Japanese land prices as a natural experiment. Firms that lost more collateral value borrowed less and invested less, and they were less likely to keep their banking relationships. In the working-paper version, a 10% fall in collateral value reduced the average manufacturing firm's investment rate by about 0.8 percentage point [FACT: ch03-S14, VERIFIED-SECONDARY from the abstract and working-paper summary]. That is direct evidence for the downward leg of the loop in §3.4.2: falling collateral values reduced borrowing capacity and real activity.

**The policy catalyst.** In 1990 the Ministry of Finance issued administrative guidance limiting the growth of banks' total lending to real estate (the *sōryō kisei*, "total volume restriction") [FACT: ch03-S16 (IMF working paper) and ch03-S17; sources date it to March or April 1990, likely the difference between notice and effective date]. Loans to nonbanks were exempted, and lending through nonbanks, including the *jusen* housing-loan companies, grew rapidly in 1990–91 [FACT: ch03-S16]. The date on which the restriction was lifted is *(verification pending)*.

**What was knowable at the time.** Rising land prices, the low policy rate, rapid real-estate lending, and the reliance on land collateral were all public [INFERENCE: these are the variables the official studies document from contemporaneous data]. Commentators argued at the time about whether land prices reflected fundamentals. What could not be known was the loop gain: how much of the price level was supported by credit that would reverse. Okina, Shirakawa and Shiratsuka describe "intensified bullish expectations" as central to the episode [FACT: ch03-S03 abstract]. That is the cognitive half of Soros's loop.

**Competing interpretations.**

* *Monetary policy.* The discount rate was held at 2.5% for more than two years after the recovery began, and raised only as asset prices peaked. This view assigns the boom to cheap money and the bust to tightening [INFERENCE drawn from the documented rate path].
* *Financial deregulation and bank behavior.* Large firms moved to capital markets, and banks moved toward real estate and smaller borrowers with weaker risk control (Kanaya and Woo, 2000) [FACT that this interpretation is advanced: ch03-S15].
* *Expectations.* Extrapolative beliefs about land prices drove demand independent of rates [INFERENCE consistent with ch03-S03].
* *Regulatory catalyst.* The 1990 lending restriction cut $\lambda$ for new real-estate credit at the peak and helped start the downward loop [INFERENCE; the relative contributions of rate hikes and the restriction are disputed].

These interpretations are complementary rather than exclusive. In the loop model, cheap money and deregulation raised $\lambda$ and $\theta$, expectations raised $\theta$, and the restriction plus rate rises reversed them.

**What the episode establishes.** It establishes that a credit system built on real-estate collateral transmits land-price declines into lending and investment (Gan's evidence). It shows that a policy that cuts real-estate credit at a market peak can coincide with a long decline. And it shows that a nonbank channel left outside the restriction can absorb the displaced credit for a time.

**What it does not establish.** It does not establish the loop gain for any other market. It does not show that the bubble could have been identified in real time with enough confidence to time it. It does not separate the causal roles of monetary policy, the lending restriction, and expectations. And it does not imply that every rapid land-price rise ends this way.

**CRE connection.** Every element has a modern analog: appraisal-based LTV lending (the collateral loop), administrative guidance on CRE concentrations (a change in $\lambda$), lending migrating to private credit funds outside bank regulation (the nonbank channel), and owners who all upsized against the same appraisals (crowding). LTCM in 1998, the trading-desk version of the forced-selling loop, is treated in Chapter 23.

---

### 3.10 Decision exercise: the upsize, the land, and the bid

Return to the opening problem. Using the numbers developed in this chapter, write a decision record on `desk/investment_memos/decision_record_template.md` that answers:

1. **The upsize.** Accept, decline, or accept a smaller amount. State the covenant buffer under each choice (Example 3.7: 7.1% at 65%, 21.4% at 55%). State the fundamental shock that would trigger a breach given a downside loop multiplier (§3.6), and your posterior probability of a downturn (Example 3.10).
2. **Use of proceeds.** If you take any cash, state the risk-matched hurdle it must clear (Example 3.1). State the exit capacity of what you would buy (Example 3.8).
3. **The land.** Your maximum price for the pad site and the conditions under which the option to wait is real: entitlement life, carrying cost, competing sites.
4. **The bid on the hotel.** Your maximum bid and how it changes if signals 1 and 2 are not independent.
5. **Invalidation.** Name the data that would reverse each decision, such as group pace, STR supply pipeline, or lender behavior.
6. **Abstention.** Whether any of the three is better left alone, and why.

**Rubric.** Full credit requires:

* (a) the covenant buffer computed and compared with a plausible downside, not just with the base case;
* (b) explicit recognition that other owners' upsizes raise the market's loop gain and crowd your exit;
* (c) the land valued as an option, with the option's real-world conditions checked;
* (d) a bid that follows from a stated prior and stated LRs, with the dependence problem addressed;
* (e) the do-nothing alternative evaluated with numbers.

A strong answer declines or shrinks the upsize, considers the land at a price between residual and option value conditional on entitlement life, and bids at or below about \$20.8 million or waits for the supply data. Reasonable answers can differ on the land and the bid. An answer that accepts the full upsize to buy more hotels in the same metro must explain why the crowding and covenant arithmetic do not apply.

---

### 3.11 Frequent analytical errors

1. **Using the unlevered alternative as the hurdle for a levered deal.** Lever the alternative to the deal's risk first (Example 3.1).
2. **Calling a market "reflexive" without a gain.** Name $\lambda$, $\theta$, $\psi$, and the sign of the loop. Estimate $m$.
3. **Assuming symmetric feedback.** Borrowing is optional, repayment is forced: $\theta_{down} > \theta_{up}$.
4. **Quoting a half-life in the wrong period.** A quarterly $\phi$ gives a half-life in quarters.
5. **Trusting estimated $\phi$ near one.** Small-sample bias shortens the half-life, and $H$ is hypersensitive to $\phi$ near one.
6. **Confusing momentum with mean reversion, or with smoothing.** Appraisal-based autocorrelation is not a tradeable trend.
7. **Forecasting with the regime-average growth rate.** Expected growth depends on the current regime. Identifying the regime is worth more than refining growth within it.
8. **Valuing land at residual.** Residual value ignores the option to wait and understates land value when uncertainty is high.
9. **Sizing a covenant buffer to the market move only.** Add the impact of your own and others' forced sales.
10. **Measuring liquidity on your own position.** Exit capacity in a stress is shared with everyone holding the same trade.
11. **Multiplying likelihood ratios of correlated signals.** This double-counts evidence and causes over-reaction.
12. **Updating without writing down the prior.** Without a recorded prior and LRs, hindsight will rewrite both.

---

### 3.12 Connections to other chapters

* Chapter 1: break-even probabilities and immediacy are the static versions of this chapter's dynamic models. Leverage and ruin connect to forced selling.
* Chapter 2: appraisal smoothing creates spurious momentum in private indices and lags the collateral loop.
* Chapter 5: monetary policy sets $r_B$ and shifts lenders' $\lambda$.
* Chapter 10: loan sizing, covenants, and refinancing gaps (Example 3.9) in full.
* Chapter 12: maturity walls and loan sales are where the second-order chain produces opportunity.
* Chapter 13: real options in hold/sell/develop decisions extend Example 3.6.
* Chapter 18: convexity and option pricing in continuous time.
* Chapter 20: Bayesian inference, base rates, and calibration in depth.
* Chapter 21: margin, liquidity stress, and sizing for survival.
* Chapter 23: Japan 1990s, LTCM 1998, and 2007–09 as full historical cases.

---

### 3.13 One-page reference sheet

| Model | Formula | Decision use |
|---|---|---|
| Risk-matched hurdle | $h = r_B + (\sigma_D/\sigma_A)(r_A - r_B)$ | Reject deals below the alternative at equal risk |
| Loop gain | $m = \lambda\theta C\psi$ | Stable iff $m<1$ |
| Loop total | $X_\infty = x_0/(1-m)$; $X_n = x_0(1-m^n)/(1-m)$ | Size stress tests to the multiplier |
| AR(1) forecast | $E[x_{t+h}] = \mu + \phi^h(x_t-\mu)$ | Reversion path |
| Half-life | $H = \ln 0.5/\ln\phi$; quarterly $\to$ annual: $\phi^4$ | Time margin for reversion trades |
| TSMOM weight | $w = \operatorname{sign}(R_{12})\,\sigma^*/\sigma$ | Volatility-targeted trend sizing |
| Regime duration | $1/(1-p_{ii})$; $P(D>d) = p_{ii}^d$ | Loan maturity and reserve sizing |
| Stationary probability | $\pi_1 = (1-p_{22})/[(1-p_{11})+(1-p_{22})]$ | Long-run base rate |
| Risk-neutral $q$ | $q = [V_0(1+r_f) - \delta V_0 - dV_0]/(uV_0 - dV_0)$ | Option to wait |
| Wait value | $W = [q f_u + (1-q) f_d]/(1+r_f)$ | Build only if $V_0 - I_0 \ge W$ |
| Forced sale | $P(s)[\lambda^*Q_0 + (1-\lambda^*)s] = D$ | Units to sell |
| Impact thresholds | Marginal $b < (1-\lambda^*)P_1/(\lambda^*Q_0)$; feasible $b < b^\dagger$ | Spiral risk |
| Covenant buffer | $d^* = 1 - \lambda_0/\lambda^*$ | Value decline before breach |
| Exit time | $T = X/(\rho\, ADV)$, crowd: $\sum X_j/(\rho\, ADV)$ | Position limits |
| Bayes (odds) | posterior odds = prior odds × $\prod LR_k$ | Sequential updating |
| Biased updating | $LR^\omega$; $\omega>1$ over-, $\omega<1$ under-reaction | Bias audit |

**Questions before any position.** What is my next-best alternative at equal risk? Which loop am I in, and what is its gain in both directions? How fast does this deviation decay, and how sure am I of $\phi$? Which regime am I in, and how long does it last? What option am I buying or selling? Who else must sell when I must? What would each new data point have to look like to change my mind, and by how much?

---

### References for this chapter

Source IDs and verification status are in `references/sources_ch03.md`.

* Barberis, N., Shleifer, A., and Vishny, R. (1998). "A Model of Investor Sentiment." *Journal of Financial Economics*, 49(3), 307–343.
* Brunnermeier, M. K., and Pedersen, L. H. (2009). "Market Liquidity and Funding Liquidity." *Review of Financial Studies*, 22(6), 2201–2238.
* Dixit, A. K., and Pindyck, R. S. (1994). *Investment under Uncertainty*. Princeton University Press.
* Gan, J. (2007). "Collateral, Debt Capacity, and Corporate Investment: Evidence from a Natural Experiment." *Journal of Financial Economics*, 85(3), 709–734.
* Hamilton, J. D. (1989). "A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle." *Econometrica*, 57(2), 357–384.
* Kanaya, A., and Woo, D. (2000). "The Japanese Banking Crisis of the 1990s: Sources and Lessons." IMF Working Paper WP/00/7.
* Kendall, M. G. (1954). "Note on Bias in the Estimation of Autocorrelation." *Biometrika*, 41(3–4), 403–404.
* Kiyotaki, N., and Moore, J. (1997). "Credit Cycles." *Journal of Political Economy*, 105(2), 211–248.
* Moskowitz, T. J., Ooi, Y. H., and Pedersen, L. H. (2012). "Time Series Momentum." *Journal of Financial Economics*, 104(2), 228–250.
* Okina, K., Shirakawa, M., and Shiratsuka, S. (2001). "The Asset Price Bubble and Monetary Policy: Japan's Experience in the Late 1980s and the Lessons." *Monetary and Economic Studies*, 19(S1), 395–450. Bank of Japan, Institute for Monetary and Economic Studies.
* Shleifer, A., and Vishny, R. W. (1992). "Liquidation Values and Debt Capacity: A Market Equilibrium Approach." *Journal of Finance*, 47(4), 1343–1366.
* Soros, G. (1987). *The Alchemy of Finance*. New York: Simon & Schuster.
* Titman, S. (1985). "Urban Land Prices under Uncertainty." *American Economic Review*, 75(3), 505–514.
* IMF (1993). "Japanese Banks and the Asset Price 'Bubble'." IMF Working Paper 93/85.


\newpage


# Part II — Macroeconomic Intelligence

## Chapter 4 — The Business Cycle

> **Status:** Complete (v1.0). Numerical examples, problem answers and the arithmetic of the historical episode are reproduced in `tests/test_ch04_examples.py`. Problems are in `problems/questions/ch04_problems.md` and solutions in `problems/solutions/ch04_solutions.md`. Sources are in `references/sources_ch04.md`. Items marked *(verification pending)* have not yet been checked against a primary source; in particular, ALFRED vintage downloads could not be retrieved in this authoring pass, so the real-time figures in §4.9 rest on the original BEA and BLS releases rather than on ALFRED.

### Learning objectives

After this chapter you should be able to:

1. Decompose GDP with the expenditure identity, compute each component's **contribution** to growth in percentage points, and explain why investment, though about a sixth of GDP, often accounts for most of the swing in a recession.
2. Convert between quarter-on-quarter, annualized, and year-over-year growth, and recognize when a positive year-over-year number hides an economy that is already contracting.
3. Compute labor productivity and unit labor costs, and translate them into hotel and multifamily margin pressure.
4. Read the payroll and household surveys correctly, including their revisions, and size a data surprise in standard-deviation units net of revisions.
5. Compute the **Sahm rule** indicator from monthly unemployment rates by hand, and explain how rounding and revisions move the trigger date.
6. Treat yield-curve inversion as evidence with a hit rate and a false-positive rate. Use Bayes' rule to turn it into a recession probability that depends on the base rate.
7. Read the Federal Reserve's Senior Loan Officer Opinion Survey (SLOOS), compute a net percentage, and translate tighter standards into lower loan proceeds and a refinancing gap.
8. Map an economic surprise into moves in yields, the curve, equities, credit and CRE financing costs, and say which links are reliable and which are only tendencies.
9. Rank property types by the speed and size of the transmission from the cycle to NOI. Hotels come first and fastest, then apartments, then office and industrial. Compute the first-year NOI change for each.
10. Describe how the 2001 and 2007–09 recessions looked in real-time data, how much the data were later revised, and what that implies for underwriting decisions made during a downturn.

---

### 4.1 Opening investment problem: the hotel bid in a late-cycle fog

All facts in this section are [HYPOTHESIS], a constructed teaching case. Its macro readings are built to resemble a late-cycle environment. They do not reproduce any particular month.

You sit on the investment committee of a \$600 million real estate fund that is 30% hotels. On a Thursday in the fourth month of a quarter, two items reach the committee.

**Item 1 — the acquisition.** A 180-room select-service hotel in a Sun Belt metro is offered at \$29.5 million. Trailing-twelve-month NOI after a 4% FF&E reserve is \$2.43 million, a going-in cap rate of 8.24% on trailing NOI. The sponsor proposes 65% loan-to-cost floating-rate debt at SOFR + 3.25% with a two-year rate cap, and underwrites 4% RevPAR growth in each of the next two years. The broker says best-and-final bids are due in ten days.

**Item 2 — the refinancing.** A 210,000 sf suburban office building the fund owns has an \$18.0 million loan maturing in nine months. Last year an appraiser valued the building at \$28.6 million on NOI of \$2.0 million (a 7.0% cap rate).

**The macro dashboard on the committee's screen:**

| Indicator | Latest reading | Comment from the sponsor's deck |
|---|---|---|
| Real GDP, advance estimate | +1.2% annualized; +2.1% year over year | "Economy still growing" |
| Nonfarm payrolls | +95,000 vs consensus +150,000; prior two months revised down a combined 70,000 | "Labor market resilient" |
| Unemployment rate | 4.1%; three-month average 0.37 points above its 12-month low | "Still historically low" |
| 10-year minus 3-month Treasury spread | Inverted for nine months | "Distorted by Fed policy; different this time" |
| SLOOS, CRE standards | Net 34% of banks tightening (nonfarm nonresidential) | "Banks are always cautious" |
| Hotel market RevPAR (trailing 3 months) | −1.5% year over year | "Calendar shift" |

The sponsor's comments may all be true. They may also be the standard late-cycle explanations that turn out to be wrong. This chapter gives you the tools to put a probability on that, to estimate how much the hotel's NOI would fall if the dashboard is right, and to find what the office refinancing would look like if banks keep tightening. Section 4.10 returns to the decision.

---

### 4.2 Economic intuition: why the cycle exists and why CRE feels it unevenly

The business cycle is the recurring, irregular alternation of expansion and contraction in aggregate economic activity. *Recurring* means that recessions keep happening. *Irregular* means that no fixed period or amplitude describes them. Expansions in the post-war United States have ranged from about a year to more than ten years. A speculator gains nothing by forecasting "the cycle" as if it were a sine wave. What pays is knowing **which mechanisms amplify a slowdown into a recession, how quickly each shows up in the data, and how quickly each reaches the cash flows you own**.

#### Three amplifiers

1. **The investment accelerator.** Firms invest to *expand* capacity. When expected demand growth slows from 3% to 1%, the desired capital stock still grows, but the *flow* of new investment needed to reach it can fall by much more than 2%. Inventories behave the same way. A retailer that expects flat sales stops restocking; it does not cut orders by the 1% decline in sales. Investment is a derivative of expected output, so it swings more than output does. This is why housing, equipment, structures and inventories account for most of the variation in GDP during recessions, while consumption, the largest component, moves much less. Example 4.1 shows the arithmetic.

2. **The labor-income loop.** Lower investment cuts hiring. Lower hiring cuts household income growth. Lower income growth cuts consumption at the margin, which cuts expected demand and lowers investment again. Unemployment insurance and other automatic stabilizers dampen the loop, and the Sahm rule (§4.5.5) watches it directly. Once the three-month average unemployment rate has risen half a point, the loop has historically been running.

3. **The credit loop.** Lenders lend against collateral values and borrower cash flow. When the outlook darkens, banks tighten standards: lower LTVs, higher DSCR minimums, wider spreads (§4.5.6). Tighter credit lowers asset values and investment, which worsens the outlook, which justifies tighter credit. In CRE the loop runs through refinancing. A loan sized at 65% LTV in a loose market cannot be refinanced at 60% LTV of a lower value without new equity. Chapter 3 treats this reflexivity formally. Here we measure it.

#### Why CRE feels the cycle unevenly

A property's NOI is a claim on a slice of the economy, and the slice is defined by **lease duration** and **operating leverage**:

* **Hotels reprice every night.** Room rates and occupancy respond to demand within weeks, and fixed costs (labor minimums, property taxes, insurance, franchise systems) do not shrink with revenue. Hotels have the shortest leases and the highest operating leverage of any major property type. They are the first CRE asset class to show a downturn and usually the hardest hit in NOI terms (Example 4.8).
* **Apartments reprice annually.** About one-twelfth of leases roll each month, so market-rent changes pass through to the rent roll within a year. Operating leverage is moderate.
* **Office and industrial reprice slowly.** With five- to ten-year leases, only the share of the rent roll that expires in a given year marks to market. The NOI hit is delayed, but it is **embedded**. It arrives as leases roll, often after the recession has officially ended, and with downtime, free rent and tenant-improvement costs that NOI understates.
* **Retail** sits in between. It depends on the tenant mix and on percentage-rent clauses.

So "the cycle" reaches a diversified CRE portfolio as a sequence: hotel RevPAR first, then apartment rent growth, then office and industrial occupancy and rents, and finally appraisal-based values and cap rates. Lenders, meanwhile, have tightened before any of those NOI changes appear. A speculator who understands the sequence can price the lag.

---

### 4.3 Technical definitions

| Term | Definition |
|---|---|
| GDP (expenditure approach) | $Y = C + I + G + (X - M)$: personal consumption, gross private domestic investment (business fixed investment, residential investment, change in inventories), government consumption and investment, exports less imports |
| Real vs nominal GDP | Real GDP is measured in chained dollars of a reference year, nominal GDP in current dollars. Growth rates in this chapter are real unless stated |
| SAAR | Seasonally adjusted annual rate. U.S. quarterly GDP levels are expressed at annual rates, and quarterly growth is **compounded** to an annual rate |
| Annualized growth | $a = (1+q)^4 - 1$, where $q$ is quarter-on-quarter growth |
| Year-over-year (YoY) growth | $Y_t / Y_{t-4} - 1$ on quarterly data, $Y_t/Y_{t-12}-1$ on monthly data |
| Contribution to growth | $(\Delta X_i)/Y_{t-1}$, in percentage points. Contributions sum to GDP growth |
| GDI | Gross domestic income. In principle equal to GDP; in practice it differs by a *statistical discrepancy* that can be large near turning points |
| Labor productivity | Output per hour worked (the BLS publishes it for the nonfarm business sector) |
| Unit labor cost (ULC) | Compensation per unit of output = hourly compensation ÷ productivity |
| Establishment (payroll) survey | BLS Current Employment Statistics (CES): a sample of employers. It counts jobs, and is benchmarked annually to tax-record counts |
| Household survey | BLS Current Population Survey (CPS): a sample of households. It counts employed people and gives the unemployment rate |
| Benchmark revision | Annual re-anchoring of the payroll level to near-census counts from unemployment-insurance tax records |
| NBER recession | A significant decline in economic activity spread across the economy and lasting more than a few months, as dated by the NBER Business Cycle Dating Committee. The peak month is the last month of the expansion, and the trough month is the last month of the recession |
| Sahm rule indicator | Three-month average unemployment rate minus the minimum three-month average of the previous 12 months. A reading ≥ 0.50 percentage point signals a recession (Sahm, 2019) |
| Term spread | Long-term minus short-term Treasury yield, commonly 10-year minus 3-month (10y–3m) or 10-year minus 2-year (10y–2y). Inversion means the spread is below zero |
| SLOOS | The Federal Reserve's Senior Loan Officer Opinion Survey on Bank Lending Practices. It reports changes in standards and demand by loan category, including three CRE categories |
| Net percentage tightening | Share of banks reporting tighter standards minus share reporting easier standards |
| Leading / coincident / lagging indicator | A series that tends to turn before, with, or after the business cycle |
| Economic surprise | Released value minus the pre-release consensus forecast, often standardized by the historical standard deviation of surprises |
| Vintage | The version of a data series as published on a given date. ALFRED (the archival FRED database maintained by the Federal Reserve Bank of St. Louis) stores vintages |

---

### 4.4 GDP, its components, and productivity

#### 4.4.1 The expenditure identity and why investment is the volatile component

$$Y = C + I + G + NX.$$

This is an accounting identity, not a theory. It says where output went. It does not say what caused what. Two consequences are often misread.

* **Imports do not "subtract from GDP".** Imports appear in $C$, $I$ or $G$ when the goods are bought, and are subtracted in $NX$ so that only domestic production is counted. A fall in imports raises measured $NX$. In a recession that rise often partly offsets weaker domestic demand, because demand for imports falls along with everything else. It is a symptom of weakness, not a source of strength.
* **Inventory change is part of $I$.** Production that is not sold is counted as investment in inventories. A quarter of strong GDP growth driven by inventory accumulation can mean that firms produced goods nobody bought. That quarter borrows from the next one.

Personal consumption is about two-thirds of U.S. GDP. FRED's series of BEA percentage shares shows personal consumption expenditures at 68.0% of GDP in the fourth quarter of 2025 [FACT; FRED series DPCERE1Q156NBEA, from BEA NIPA data, VERIFIED-SECONDARY via search excerpt]. Gross private domestic investment is a much smaller share, conventionally in the high teens *(verification pending for a current value)*. The difference in **volatility** matters more than the difference in size.

Write the growth of GDP as a share-weighted sum of component growth rates:

$$\frac{\Delta Y}{Y_{t-1}} = \sum_i \frac{X_{i,t-1}}{Y_{t-1}} \cdot \frac{\Delta X_i}{X_{i,t-1}} = \sum_i s_i\, g_i .$$

Each term $s_i g_i$ is component $i$'s **contribution** in percentage points. If consumption ($s \approx 0.68$) slows from +2% to +0.5%, its contribution falls by about one point. If investment ($s \approx 0.17$) swings from +5% to −12%, its contribution falls by nearly three points. In this sense recessions are investment events.

#### 4.4.2 Annualized versus year-over-year growth

The BEA reports quarterly real GDP growth "at an annual rate". The rate is **compounded**, not multiplied by four:

$$a = (1+q)^4 - 1, \qquad q = (1+a)^{1/4} - 1.$$

Derivation: if output grew at the quarterly rate $q$ for four consecutive quarters, the level after a year would be $(1+q)^4$ times the starting level.

Year-over-year growth compares the current quarter with the same quarter a year earlier:

$$YoY_t = \frac{Y_t}{Y_{t-4}} - 1 = \prod_{j=0}^{3}(1+q_{t-j}) - 1.$$

YoY growth is the compound of the last four quarterly rates. It is therefore a **trailing average**, smoothed and lagged by roughly two quarters. Near a turning point the two measures can tell opposite stories: YoY can stay positive for two or three quarters after the economy has started to contract (Example 4.2). Annualized rates have the opposite fault. They multiply a single quarter's noise, including revisions, by about four. A desk should look at both, and at the level.

The simple approximation $a \approx 4q$ understates positive growth and overstates the magnitude of negative growth, but only slightly at normal growth rates. The gap is $6q^2 + 4q^3 + q^4$, about 1.5 bp at $q = 0.5\%$. It matters in high-inflation nominal series and in collapses like 2020.

#### 4.4.3 Productivity and unit labor costs

Labor productivity is output per hour:

$$\text{Productivity growth} = \frac{1 + g_{output}}{1 + g_{hours}} - 1 \approx g_{output} - g_{hours}.$$

Unit labor cost is compensation per unit of output:

$$\text{ULC growth} = \frac{1 + g_{comp/hour}}{1 + g_{productivity}} - 1 \approx g_{comp/hour} - g_{productivity}.$$

Productivity is the bridge between wages and inflation. Wage growth of 4.5% is consistent with 2% price inflation and stable margins only if productivity grows about 2.5%. When productivity is weak, high wage growth either raises prices or squeezes margins. For a hotel, where labor is typically the largest single expense *(typical share of revenue is an assumption; see Chapter 11)*, the comparison between wage growth and **rooms productivity**, measured as occupied rooms per labor hour, decides whether ADR growth reaches NOI.

Productivity is also cyclical in the measured data. Early in a downturn output falls before firms cut hours, so measured productivity falls. Later, layoffs cut hours faster than output, and productivity jumps. A productivity surge in a recession is often a symptom of labor shedding, not of technology.

#### Example 4.1 — Contributions: a recession driven by investment

All inputs are [HYPOTHESIS], scaled to resemble U.S. shares.

**Given.** GDP components in year 0 (\$ billions, real): $C$ = 15,000; $I$ = 3,600; $G$ = 3,900; $NX$ = −700. In year 1: consumption grows 0.5%, investment falls 12%, government grows 1.5%, and net exports rise by 100 because imports fall.

**Find.** GDP in both years, each component's share and contribution, and GDP growth.

**Solution.**

$Y_0 = 15{,}000 + 3{,}600 + 3{,}900 - 700 = 21{,}800$.

Shares of $Y_0$: $C$ 68.81%, $I$ 16.51%, $G$ 17.89%, $NX$ −3.21%.

Year-1 components: $C = 15{,}000 \times 1.005 = 15{,}075$; $I = 3{,}600 \times 0.88 = 3{,}168$; $G = 3{,}900 \times 1.015 = 3{,}958.5$; $NX = -600$.

$Y_1 = 15{,}075 + 3{,}168 + 3{,}958.5 - 600 = 21{,}601.5$.

Contributions ($\Delta X_i / Y_0$):

| Component | $\Delta X_i$ | Contribution (pp) |
|---|---|---|
| Consumption | +75.0 | +0.34 |
| Investment | −432.0 | −1.98 |
| Government | +58.5 | +0.27 |
| Net exports | +100.0 | +0.46 |
| **GDP** | **−198.5** | **−0.91** |

GDP growth $= 21{,}601.5/21{,}800 - 1 = -0.91\%$.

**Check.** The contributions sum to −0.91 pp. Investment's contribution is 2.18 times the size of the total decline. Consumption, government and net exports together offset more than half of the investment drag.

**Decision consequence.** In this recession consumers barely slow down; the hit falls on capital spending. Property demand follows the *composition* of GDP, not the headline. Industrial and flex space tied to capital goods, construction-related distribution and corporate office expansion feel an investment recession first. Leisure hotels and necessity retail feel a consumption recession first. Before you translate "GDP −0.9%" into a NOI haircut, ask which components moved. The rise in net exports is also a warning, not a comfort: it comes from falling imports, which is weak domestic demand appearing in another account.

*Reproduce:* `tests/test_ch04_examples.py::test_example_4_1`

#### Example 4.2 — Two negative quarters inside a positive year

**Given.** Real GDP levels (\$ billions, SAAR) [HYPOTHESIS]: Q0 22,000; Q1 22,110; Q2 22,143; Q3 22,121; Q4 22,066.

**Find.** Quarter-on-quarter growth, annualized growth, the simple ×4 approximation, and YoY growth in Q4.

**Solution.**

| Quarter | Level | $q$ | Annualized $(1+q)^4-1$ | $4q$ |
|---|---|---|---|---|
| Q1 | 22,110 | +0.50% | +2.02% | +2.00% |
| Q2 | 22,143 | +0.15% | +0.60% | +0.60% |
| Q3 | 22,121 | −0.10% | −0.40% | −0.40% |
| Q4 | 22,066 | −0.25% | −0.99% | −0.99% |

YoY in Q4 $= 22{,}066/22{,}000 - 1 = +0.30\%$.

**Check.** $(1.005)(1.0014925)(0.9990065)(0.9975137) - 1 = 0.30\%$, the YoY figure. Compounding versus ×4 differs by 1.5 bp in Q1 ($2.015\%$ vs $2.000\%$). That is immaterial here, but it would not be in a 2020-sized quarter.

**Decision consequence.** A sponsor deck that says "GDP up 0.3% over the past year" is accurate and misleading. The economy has contracted for two straight quarters, and the latest quarter is falling at about a 1% annual rate. Use YoY for level comparisons such as RevPAR versus last year. Use annualized quarterly or three-month annualized monthly data to see the turn. Expect the advance estimate of the latest quarter to be revised, possibly by more than its own size (§4.9).

*Reproduce:* `tests/test_ch04_examples.py::test_example_4_2`

#### Example 4.3 — Productivity, unit labor costs and the hotel labor ratio

**Given** [HYPOTHESIS]. Nonfarm business output grows 2.4% and hours grow 0.9%. Hourly compensation grows 4.5%. A select-service hotel has labor costs equal to 36.0% of revenue. Hotel wages grow 4.5% per hour, rooms productivity (occupied rooms per labor hour) improves 1.0%, occupancy is flat and ADR rises 2.5%.

**Find.** Economy-wide productivity and ULC growth. The hotel's new labor-cost ratio.

**Solution.**

Productivity $= 1.024/1.009 - 1 = 1.49\%$.

ULC $= 1.045/1.01487 - 1 = 2.97\%$. The additive approximation gives $4.5\% - 1.49\% = 3.01\%$.

Hotel: labor cost per occupied room rises by the factor $1.045/1.01$, and revenue per occupied room rises by $1.025$. The new labor ratio is

$$0.36 \times \frac{1.045}{1.01 \times 1.025} = 36.34\%,$$

an increase of 0.34 percentage point of revenue.

**Check.** If ADR grew 3.47%, the ratio would be unchanged, because $1.045/1.01 = 1.0347$.

**Decision consequence.** Unit labor costs rising near 3% while the central bank targets 2% inflation is a reason for policy to stay tight (Chapter 5). For the hotel, ADR growth of 2.5% with wage growth of 4.5% *compresses* margins unless productivity improves by about 2% rather than 1%. The 0.34-point loss looks small. At an NOI margin near 30%, it is roughly 1.1% of NOI, and it compounds every year the gap persists. An underwriting model that grows ADR and labor cost per occupied room at the same rate assumes away the main margin risk of the late cycle.

*Reproduce:* `tests/test_ch04_examples.py::test_example_4_3`

---

### 4.5 Employment, credit, indicators and recession detection

#### 4.5.1 Payrolls versus the household survey

| Feature | Establishment survey (CES) | Household survey (CPS) |
|---|---|---|
| Unit | Jobs on payrolls | Employed persons |
| Sample | Employers covering a large share of payroll employment | Households |
| Gives | Payroll change, hours, average hourly earnings | Unemployment rate, participation, employment-population ratio |
| Counts self-employed, farm workers | No | Yes |
| Counts multiple jobholders | Each job | Once |
| Monthly sampling error | Smaller | Larger: the household survey's monthly employment change is noisy *(BLS publishes confidence intervals; values to be cited, verification pending)* |
| Revisions | Two monthly revisions, then an annual benchmark | Population controls each January; seasonal factors are revised |
| Benchmark | Unemployment-insurance tax records (Quarterly Census of Employment and Wages) | Census population estimates |

The two surveys can diverge for months. Near turning points the household survey sometimes turns first. The NBER's December 2008 announcement noted that payroll employment peaked in December 2007, while the household-survey measure of employment peaked in November 2007 [FACT; NBER announcement of 1 December 2008, VERIFIED-PRIMARY via search excerpt]. Neither survey is "right". They measure different things with different errors, so a divergence is a reason to look harder, not a reason to pick the survey you prefer.

**Revisions are part of the release.** Each payroll report revises the previous two months. A headline of +150,000 with −100,000 of revisions to prior months is a report of +50,000 relative to what was previously believed. The annual benchmark revision can be much larger in recessions. The March 2009 benchmark lowered the payroll level by 902,000 jobs, against a preliminary estimate of 824,000 (§4.9).

#### 4.5.2 Wages

Average hourly earnings in the payroll survey are distorted by composition. When low-wage workers lose jobs first, as they did in 2020, average earnings *rise*, even though no individual worker got a raise. Use composition-adjusted measures such as the Employment Cost Index *(BLS quarterly series; cited qualitatively)* when the question is wage *pressure*. For CRE, wage growth enters twice: as a cost (hotel and multifamily payroll) and as a driver of revenue (apartment rents follow renter incomes with a lag [HYPOTHESIS supported by the affordability logic of rent-to-income underwriting]).

#### 4.5.3 Credit cycles and the Senior Loan Officer Opinion Survey

The SLOOS asks senior loan officers at a panel of domestic banks and U.S. branches of foreign banks whether their **standards** (the criteria for approving a loan) and **terms** (the price and structure of approved loans) have tightened, stayed basically unchanged, or eased over the past three months, and whether loan **demand** has strengthened or weakened. Answers come as "considerably" or "somewhat". The Federal Reserve publishes the **net percentage** tightening:

$$\text{Net \% tightening} = \frac{\#\text{tightened (considerably + somewhat)} - \#\text{eased (considerably + somewhat)}}{\#\text{respondents}}.$$

The survey reports CRE standards separately for **construction and land development**, **nonfarm nonresidential** (office, retail, industrial, hotel), and **multifamily** loans [FACT; Federal Reserve SLOOS releases, VERIFIED-PRIMARY via search excerpts; the date the three-way split began is *(verification pending)*].

Three cautions about reading the survey:

1. A net percentage measures **breadth**, not **degree**. Net 34% tightening means that, on balance, a third of banks tightened. It does not say whether the LTV cap moved 5 points or 15. Severity shows up in the special questions on specific terms and in loan pricing.
2. It is a **change** variable. Standards that tightened for six quarters and then stop tightening show "net 0%" while remaining tight. Cumulate the series, or read the questions on the *level* of standards relative to history, before concluding that credit has eased.
3. It is a **bank** survey. CMBS, life companies, debt funds and agency lenders do not respond. When banks retreat, other lenders may fill the gap at a higher price, or they may retreat together, as in 2008–09.

Example 4.4 turns a SLOOS reading into loan proceeds.

#### Example 4.4 — SLOOS tightening and the office refinancing

**Given** [HYPOTHESIS]. Of 64 SLOOS respondents, 6 tightened nonfarm-nonresidential CRE standards considerably, 20 somewhat, 34 were unchanged, 4 eased somewhat and none eased considerably. The office building of §4.1 has NOI of \$2.0m and an \$18.0m loan maturing in nine months.

* *Terms a year ago:* value at a 7.0% cap; max LTV 65%; min DSCR 1.25x at 6.50% on 30-year amortization; min debt yield 8.5%.
* *Terms expected at maturity:* NOI −5% (to \$1.9m); value at a 7.75% cap; max LTV 60%; min DSCR 1.40x at 7.25% on 30-year amortization; min debt yield 10.0%.

**Find.** The net percentage tightening; the maximum loan under each set of terms and the binding constraint; the refinancing gap.

**Solution.**

Net tightening $= (6 + 20 - 4 - 0)/64 = 34.4\%$.

*A year ago.* $V = 2{,}000{,}000/0.07 = \$28{,}571{,}429$. LTV test: $0.65 V = \$18{,}571{,}429$. DSCR test: loan constant at 6.50%/30 years $= 0.0758$, so $L = 2{,}000{,}000/1.25/0.0758 = \$21{,}094{,}776$. Debt-yield test: $2{,}000{,}000/0.085 = \$23{,}529{,}412$. **Binding: LTV, \$18,571,429.** The building could have been refinanced with \$571,429 of cash out.

*At maturity.* $NOI = 1{,}900{,}000$; $V = 1{,}900{,}000/0.0775 = \$24{,}516{,}129$. LTV: $0.60 V = \$14{,}709{,}677$. DSCR: loan constant at 7.25% $= 0.0819$; $L = 1{,}900{,}000/1.40/0.0819 = \$16{,}578{,}594$. Debt yield: $1{,}900{,}000/0.10 = \$19{,}000{,}000$. **Binding: LTV, \$14,709,677.**

Refinancing gap $= 18{,}000{,}000 - 14{,}709{,}677 = \$3{,}290{,}323$ of new equity, before closing costs. Loan proceeds fall 20.8%.

**Check.** Each test is recomputed in `tests/test_ch04_examples.py::test_example_4_4` with `cre.max_loan`. The LTV test binds in both cases, so the value decline (−14.2%) and the LTV cut (65% to 60%) compound: $0.60/0.65 \times 24.516/28.571 - 1 = -20.8\%$.

**Decision consequence.** A net 34% tightening reading is not an abstraction. Applied to this building, it means \$3.3 million of equity in nine months, or a negotiated extension, or a sale. Act while the NOI is still \$2.0m and the appraisal is still fresh. Options include an early refinancing (with prepayment cost), buying a rate hedge, or arranging the extension now. The cost of waiting is that the NOI and value inputs both deteriorate on the timetable of §4.8.2. This liquidity call also constrains the hotel decision in §4.10. Equity reserved for the office gap is not available for the hotel.

*Reproduce:* `tests/test_ch04_examples.py::test_example_4_4`

#### 4.5.4 Leading, coincident and lagging indicators

| Timing | Examples | CRE analogs |
|---|---|---|
| Leading | Term spread; initial jobless claims; building permits and housing starts; manufacturers' new orders; credit spreads; SLOOS standards; equity prices; consumer expectations | Hotel group-booking pace; leasing tours and proposals; construction-loan originations; REIT implied cap rates (Chapter 12) |
| Coincident | Payroll employment; industrial production; real personal income less transfers; real manufacturing and trade sales | Hotel RevPAR; apartment new-lease trade-outs |
| Lagging | Unemployment duration; services inflation; business loans outstanding; delinquency and charge-off rates | Office vacancy; appraisal-based values and cap rates; CMBS special servicing rates; CRE loan delinquencies |

The NBER weighs a set of monthly coincident measures, including payroll and household employment, real personal income less transfers, real consumption, real manufacturing and trade sales, and industrial production, rather than quarterly GDP alone *(list as described on the NBER business-cycle dating pages; current list verification pending)*. Leading indicators are leading *on average*. Their lead times vary from a few months to more than two years, and each has a history of false signals. Composite indices, such as the Conference Board's Leading Economic Index, reduce noise but inherit the components' false signals.

For CRE, notice that the classic CRE "data", meaning appraisal values, cap-rate surveys and delinquency rates, sit almost entirely in the **lagging** column. A committee that waits for cap rates to move before re-underwriting is reacting to the last war.

#### 4.5.5 Recession detection: NBER dating and the Sahm rule

**NBER dating is retrospective.** The Business Cycle Dating Committee waits until the data are clear, and the data are revised. The December 2007 peak was announced on 1 December 2008. The June 2009 trough was announced on 20 September 2010. The March 2001 peak was announced on 26 November 2001, eight months later, when the recession was already over: its trough came in November 2001, though that trough was not announced until 17 July 2003 [FACT; NBER Business Cycle Dating Committee announcements, VERIFIED-PRIMARY via search excerpts]. **No asset price waits for the NBER.** A recession-conditional strategy has to act on real-time indicators that are noisier than the official dates.

**The Sahm rule.** Claudia Sahm proposed the rule in 2019 as an automatic trigger for stimulus payments to households (Sahm, 2019, Hamilton Project / *Recession Ready*). FRED's description of the Sahm Rule Recession Indicator [FACT; FRED series notes, VERIFIED-SECONDARY via search excerpt]:

$$S_t = \overline{u}_t^{(3)} - \min_{t-12 \le s \le t-1} \overline{u}_s^{(3)}, \qquad \overline{u}_t^{(3)} = \tfrac{1}{3}(u_t + u_{t-1} + u_{t-2}),$$

with a signal when $S_t \ge 0.50$ percentage point. The rule measures a **change**, not a level. A 4.0% unemployment rate is consistent with expansion or recession; a half-point rise in the smoothed rate within a year has historically indicated that the labor-income loop of §4.2 has started.

Why does a half-point rise work? Unemployment rarely rises by half a point without continuing to rise. Once layoffs exceed hiring broadly enough to lift the smoothed rate, the spending loss feeds back into further layoffs. The rule is *not* a forecast. It recognizes a recession, typically some months after it has begun.

Three properties matter in practice:

1. **Rounding.** The unemployment rate is published to one decimal. The three-month average therefore moves in steps of 0.0333, and the indicator can land exactly on 0.50. Whether "≥" or ">" is used changes the trigger month (Example 4.5).
2. **Real-time versus revised data.** The real-time version (FRED's SAHMREALTIME) uses the unemployment rates available at each date. Annual seasonal-factor revisions can move recent months by a tenth, which moves the trigger date. Secondary sources disagree by one to several months about when the rule triggered in 2001 and 2008, depending on vintage *(trigger dates verification pending against ALFRED)*.
3. **Labor-supply shocks.** The rule was calibrated on recessions in which unemployment rose because hiring collapsed. If unemployment rises because the labor force grows quickly (for example through immigration or rising participation), the rule can trigger without the demand-side loop. Secondary sources report that the indicator crossed 0.50 on the July 2024 data without an NBER recession following, and Sahm herself cautioned that labor-supply shifts could distort the signal *(the July 2024 value of about 0.53 is reported by secondary sources; verification pending against FRED)*.

#### Example 4.5 — Computing the Sahm rule, and how one revision moves the trigger

**Given** [HYPOTHESIS]. Monthly unemployment rates (%) for months 1–20:

| Month | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| $u_t$ | 3.6 | 3.5 | 3.5 | 3.5 | 3.6 | 3.5 | 3.6 | 3.6 | 3.7 | 3.7 |

| Month | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| $u_t$ | 3.8 | 3.8 | 3.9 | 3.9 | 4.0 | 4.1 | 4.1 | 4.2 | 4.3 | 4.4 |

**Find.** The three-month averages, the Sahm indicator from month 15 on (the first month with a full 12-month window of prior averages), and the trigger month. Then suppose month 4 is revised from 3.5 to 3.6 and recompute.

**Solution.**

Three-month averages (selected): month 3: $(3.6+3.5+3.5)/3 = 3.5333$; month 4: $(3.5+3.5+3.5)/3 = 3.5000$; month 15: $(3.9+3.9+4.0)/3 = 3.9333$; month 16: $(3.9+4.0+4.1)/3 = 4.0000$; month 17: 4.0667; month 20: 4.3000.

* Month 15: prior window = months 3–14. Minimum average = 3.5000 (month 4). $S_{15} = 3.9333 - 3.5000 = 0.4333$. No signal.
* Month 16: window = months 4–15. Minimum = 3.5000 (month 4). $S_{16} = 4.0000 - 3.5000 = 0.5000$. **Signal** (≥ 0.50).
* Month 17: $S_{17} = 4.0667 - 3.5000 = 0.5333$ (window months 5–16; its minimum is again 3.5000, at months 5 and 6).
* Month 20: $S_{20} = 4.3000 - 3.5667 = 0.7333$.

With month 4 revised to 3.6, the month-4 average becomes 3.5333 and the month-5 and month-6 averages become 3.5667, so the window minimum rises:

* Month 16: $4.0000 - 3.5333 = 0.4667$. No signal.
* Month 17: $4.0667 - 3.5667 = 0.5000$. **Signal**, one month later.

**Check.** If the current month's average is included in the minimum, nothing changes while unemployment is rising, because the current average is never the minimum (tested). With a flat 4.0% series the indicator is identically zero.

**Decision consequence.** The rule is a blunt, transparent instrument. Its value is discipline: it gives a pre-committed trigger that a committee cannot argue away with "still historically low" (the sponsor's comment in §4.1). Its weakness is equally clear. A one-tenth revision to a single month from a year earlier shifted the signal by a month, and a reading exactly at 0.50 depends on the inequality convention. Treat a reading between about 0.30 and 0.50 as an *elevated-risk zone* that justifies pricing recession scenarios, rather than waiting for the bell. The dashboard in §4.1 shows 0.37.

*Reproduce:* `tests/test_ch04_examples.py::test_example_4_5`

#### 4.5.6 Yield-curve inversion: base rates and false signals

When short rates exceed long rates, the market expects policy rates to fall. That usually happens because it expects the central bank to respond to weakness. An inverted curve also squeezes bank net interest margins on new lending, which can tighten credit. The evidence:

* An inverted 10-year minus 3-month spread has preceded each U.S. recession since 1960, with one clear false positive, in 1966 [FACT; J.P. Morgan Asset Management, "Was the yield curve inversion wrong in predicting a US recession?", VERIFIED-SECONDARY]. The St. Louis Fed notes that spread-based probability models also gave false positives in the late 1960s and late 1990s [FACT; Federal Reserve Bank of St. Louis, *On the Economy*, September 2023, VERIFIED-SECONDARY].
* The 10y–3m spread inverted in October 2022 and stayed inverted until December 2024, the longest inversion in decades, and a recession "has yet to materialize" as of that commentary [FACT; same J.P. Morgan source]. Searches in October 2026 found no NBER announcement of a business-cycle peak after February 2020 [INFERENCE from the NBER chronology; *verification pending* against the NBER announcements page].
* Lead times between inversion and recession vary from several months to about two years *(range cited qualitatively; verification pending)*. J.P. Morgan notes that in the last four cycles the curve un-inverted on average about six months before the recession began.

Two consequences follow. First, a signal with a long and variable lead is a poor **timing** tool even when it is a good **regime** tool. Second, the sample is tiny, about eight or nine recessions, so the "hit rate" itself is uncertain. Treat inversion as a likelihood ratio, not as a verdict.

#### Example 4.6 — Turning an inversion into a recession probability

**Given** [HYPOTHESIS, teaching parameters]. The unconditional probability that a recession begins within the next 12–18 months is $P(R) = 0.15$. Inversion occurs before a recession with probability $P(Inv\mid R) = 0.90$. Inversion occurs without a subsequent recession with probability $P(Inv\mid \bar R) = 0.10$.

**Find.** $P(R\mid Inv)$. Then repeat with a false-positive rate of 0.20, and with prior probabilities of 0.30 and 0.05.

**Solution.**

$$P(R\mid Inv) = \frac{0.90 \times 0.15}{0.90 \times 0.15 + 0.10 \times 0.85} = \frac{0.135}{0.135 + 0.085} = 61.4\%.$$

In frequency terms: out of 1,000 comparable periods, 150 precede recessions, and 135 of those show an inversion. Of the 850 that do not, 85 show an inversion anyway. An inverted curve therefore puts you in a group of 220, of which 135 are recessions.

| Prior $P(R)$ | False-positive rate | Posterior $P(R \mid Inv)$ |
|---|---|---|
| 0.15 | 0.10 | 61.4% |
| 0.15 | 0.20 | 44.3% |
| 0.30 | 0.10 | 79.4% |
| 0.05 | 0.10 | 32.1% |

**Check.** Odds form: prior odds $0.15/0.85 = 0.1765$; likelihood ratio $0.90/0.10 = 9$; posterior odds $1.588$; probability $1.588/2.588 = 61.4\%$.

**Decision consequence.** "The curve has inverted before every recession" is a statement about $P(Inv\mid R)$. The committee needs $P(R\mid Inv)$, which depends on the false-positive rate and the base rate. The false-positive rate is uncertain because of the tiny sample and the 2022–24 episode. Moving it from 10% to 20% cuts the posterior from 61% to 44%. Neither number justifies certainty, and both are far above the 15% base rate. The right response is not "recession is coming" but **underwrite the recession scenario at a probability between roughly 40% and 60%, and check whether the deal survives it**. If the hotel acquisition in §4.1 works only when that scenario has a 15% weight, the curve has told you something important.

*Reproduce:* `tests/test_ch04_examples.py::test_example_4_6`

---

### 4.6 Growth and inflation regimes

A compact way to organize cross-asset expectations is the **four-quadrant framework**. It classifies the environment by the *direction* of growth (accelerating or decelerating relative to trend) and the *direction* of inflation (rising or falling).

| | **Inflation falling** | **Inflation rising** |
|---|---|---|
| **Growth rising** | *Disinflationary expansion.* Equities and credit tend to do well; long bonds are mixed; CRE NOI growth with stable or falling cap rates is the friendly case for levered real estate | *Overheating.* Commodities and short-duration assets tend to outperform; long bonds tend to suffer; hotels and apartments can reprice rents and ADR quickly; office and long-lease net-lease assets lag in real terms |
| **Growth falling** | *Disinflationary slowdown / recession.* Long Treasuries tend to rally; equities and credit spreads tend to suffer; CRE NOI falls but base rates fall too, so the net effect depends on credit availability and spreads | *Stagflation.* Few assets do well in real terms; cash and some commodities hold up; CRE suffers on both NOI and cap rates; floating-rate borrowers are hit hardest |

All entries are [HYPOTHESIS]: **tendencies**, not laws. Three reasons they fail:

1. **The stock–bond correlation is regime-dependent.** When inflation risk dominates, bonds and equities can fall together. In 2022 both fell sharply. The "long Treasuries hedge a recession" entry assumes that growth risk dominates inflation risk.
2. **Markets price expected regimes.** The quadrant you will be in is partly priced before you get there. Returns come from *surprises* relative to the priced regime (§4.7), not from the regime itself.
3. **CRE has two exposures that can offset.** In a disinflationary slowdown, lower Treasury yields push cap rates down while lower NOI and wider credit spreads push values down. The net effect depends on the lending market, which the quadrant does not show. In 2008–09 credit dominated. In 2001 lower rates cushioned values in several property types *(qualitative characterization; verification pending)*.

Use the framework to generate scenarios, not to make predictions. For each quadrant, write down the NOI path, the cap-rate path, and the financing terms. Then ask which quadrant your portfolio cannot survive.

---

### 4.7 How economic surprises propagate across asset classes

Markets move on the difference between what was released and what was expected. A useful standardization is

$$z = \frac{\text{actual} - \text{consensus}}{\sigma_{\text{surprise}}},$$

where $\sigma_{\text{surprise}}$ is the historical standard deviation of that release's surprises. For payrolls, the **effective** surprise should include revisions to prior months, because the market updates the *level* of employment:

$$\text{Effective payroll surprise} = (\text{actual} - \text{consensus}) + \text{net revision to prior months}.$$

Price responses can be described by sensitivities $\beta$ per one standard deviation of surprise. Estimated sensitivities vary by period and depend strongly on the policy regime: when the central bank is fighting inflation, a strong jobs number raises yields more and hurts equities, while in a growth scare the same number can lift both yields and equities.

**Surprise-to-price map (direction of tendency, [HYPOTHESIS]):**

| Surprise | Front-end yields | Curve (10y–2y) | Equities | USD | Credit spreads | REITs | CRE financing |
|---|---|---|---|---|---|---|---|
| Strong growth/jobs, inflation contained | Up | Flatter or little change | Up | Up | Tighter | Mixed (higher rates vs better NOI) | Fixed-rate quotes up; credit appetite up |
| Strong growth, inflation high (tightening regime) | Up sharply | Flatter | Down | Up | Wider | Down | Higher fixed and floating costs |
| Weak growth/jobs, inflation contained | Down sharply | Steeper (bull steepening) | Down or mixed | Down | Wider | Mixed: lower rates help, weaker NOI hurts | Fixed-rate quotes down; standards may tighten |
| Hot inflation print | Up | Flatter | Down | Up | Wider | Down | Higher fixed costs; rate-cap costs up |

The CRE column runs through **financing first and NOI later**. A surprise moves the 5-year and 10-year Treasury yields that price fixed-rate loans on the same day. It moves expected NOI only through expectations, which appear in private-market prices slowly (Chapter 2). This is one reason REITs, which trade on the news, lead private appraisals.

#### Example 4.7 — A payroll miss, net of revisions

**Given** [HYPOTHESIS]. Payrolls: actual +40,000 versus consensus +180,000. The prior two months are revised down by a combined 60,000. Historical surprise standard deviation $\sigma = 75{,}000$. Assumed same-day sensitivities per $1\sigma$ of effective surprise: 2-year Treasury 5.0 bp, 5-year 4.5 bp, 10-year 3.5 bp. A 10-year Treasury note with a 4% semiannual coupon trades at a 4.20% yield. A borrower is about to lock a \$25 million five-year fixed-rate loan priced at the 5-year Treasury plus a spread.

**Find.** Headline and effective $z$; the yield moves; the change in the 10-year note price; the annual interest saving on the loan if the spread is unchanged.

**Solution.**

Headline $z = (40{,}000 - 180{,}000)/75{,}000 = -1.87$.

Effective surprise $= -140{,}000 - 60{,}000 = -200{,}000$, so $z = -2.667$.

Yield moves: 2-year $5.0 \times -2.667 = -13.3$ bp; 5-year $-12.0$ bp; 10-year $-9.3$ bp. The 10y–2y curve steepens by 4.0 bp (a "bull steepener").

10-year note: price at 4.20% = 98.38; modified duration = 8.15. The yield change is −0.000933. Duration estimate $= -8.15 \times -0.000933 \times 98.38 = +0.748$; adding convexity gives +0.752. Exact repricing gives +0.75 points.

Loan: $25{,}000{,}000 \times 0.0012 = \$30{,}000$ per year lower interest, if the lender's spread does not widen.

**Check.** Duration-plus-convexity and exact repricing agree to within 0.001 points.

**Decision consequence.** The effective surprise is 43% larger than the headline surprise ($2.667/1.867 - 1$); reading only the headline understates the news by 30%. For the borrower, a weak jobs report is a mixed blessing. The base rate falls 12 bp. But if the report shifts the recession probability up, lenders may widen spreads or cut proceeds at the next credit committee, and the hotel's NOI forecast gets worse. Lock the rate only if the spread is locked too. Do not treat \$30,000 a year as a reason to proceed with a deal whose risk has just risen. For a speculator positioned for weakness, the effective surprise, not the headline, is the number to compare with the market's move. A move smaller than the effective surprise implies suggests that the market had already priced weakness.

*Reproduce:* `tests/test_ch04_examples.py::test_example_4_7`

---

### 4.8 CRE application: transmission to NOI by property type

#### 4.8.1 The two parameters: repricing speed and operating leverage

For a property with revenue $R$, variable costs at a ratio $v$ of revenue (including fees and the reserve), and fixed costs $F$:

$$NOI = R(1-v) - F, \qquad DOL = \frac{\%\Delta NOI}{\%\Delta R} = \frac{R(1-v)}{NOI}.$$

For a leased property, only the share of revenue that rolls in a given year reprices. With rolling share $\rho$, renewal probability $\pi$, market rent change $m$ and downtime $d$ months on non-renewals, first-year revenue is

$$R_1 = R(1-\rho) + R\rho\,\big[\pi(1+m) + (1-\pi)(1+m)\tfrac{12-d}{12}\big] + R\,\Delta occ,$$

assuming, conservatively, that rolling leases expire at the start of the year. For apartments, about one-twelfth of leases roll each month, so the *time-weighted* share of the year's revenue that reprices is about one-half. We use $\rho = 0.5$.

#### Example 4.8 — One recession, four property types

**Given** [HYPOTHESIS]. A recession reduces demand. The parameters below are chosen to illustrate repricing speed. The hotel revenue decline of 17% is set close to the 2009 U.S. industry RevPAR decline (16.7%, §4.9) but is not data for any property.

| Property | Revenue | Costs | Recession shock |
|---|---|---|---|
| Hotel | \$10.0m | Fixed \$3.6m; variable 34% of revenue (incl. fees and 4% reserve) | Revenue −17% |
| Apartment | \$5.0m | Opex \$2.0m fixed | $\rho = 0.5$, market rent −6%, renewal 55%, 1 month downtime, extra vacancy −2% of revenue |
| Office | \$8.0m | Opex \$3.2m fixed | $\rho = 0.12$, market rent −15%, renewal 50%, 9 months downtime |
| Industrial | \$4.0m | Opex \$0.6m fixed | $\rho = 0.15$, market rent −5%, renewal 70%, 4 months downtime |

**Find.** First-year NOI change for each. For the hotel, also the degree of operating leverage and the effect of an 8% cut in fixed costs.

**Solution.**

*Hotel.* $NOI_0 = 10.0(0.66) - 3.6 = \$3.000$m. $R_1 = 8.3$m; $NOI_1 = 8.3(0.66) - 3.6 = \$1.878$m, a change of **−37.4%**. $DOL = 6.6/3.0 = 2.20$. With fixed costs cut 8% to \$3.312m: $NOI_1 = 5.478 - 3.312 = \$2.166$m, a change of **−27.8%**.

*Apartment.* Rolling revenue $= 2.5$m. Renewals $2.5 \times 0.55 \times 0.94 = 1.2925$m. Re-lets $2.5 \times 0.45 \times 0.94 \times 11/12 = 0.969375$m. Extra vacancy $-0.10$m. $R_1 = 2.5 + 1.2925 + 0.969375 - 0.10 = \$4.661875$m. $NOI_1 = 2.661875$m versus 3.0m: **−11.3%**.

*Office.* Rolling $= 0.96$m. Renewals $0.96 \times 0.5 \times 0.85 = 0.408$m; re-lets $0.96 \times 0.5 \times 0.85 \times 3/12 = 0.102$m. $R_1 = 7.04 + 0.408 + 0.102 = \$7.55$m. $NOI_1 = 4.35$m versus 4.8m: **−9.4%**.

*Industrial.* Rolling $= 0.6$m. Renewals $0.6 \times 0.7 \times 0.95 = 0.399$m; re-lets $0.6 \times 0.3 \times 0.95 \times 8/12 = 0.114$m. $R_1 = 3.4 + 0.399 + 0.114 = \$3.913$m. $NOI_1 = 3.313$m versus 3.4m: **−2.6%**.

| Property | First-year NOI change | Main driver |
|---|---|---|
| Hotel | −37.4% (−27.8% with cost cuts) | Nightly repricing × operating leverage 2.2 |
| Apartment | −11.3% | Half of revenue reprices; turnover downtime |
| Office | −9.4% | Only 12% rolls, but downtime is long |
| Industrial | −2.6% | Long leases, high renewal, low opex |

**Check.** Once every office lease has rolled at the 15% lower market rent (ignoring downtime), NOI is $8.0 \times 0.85 - 3.2 = 6.8 - 3.2 = \$3.6$m, **−25.0%** from \$4.8m. That is far worse than the first-year −9.4%. Office's first-year number is a down payment on the full repricing.

**Decision consequence.** The hotel is the first and largest transmission channel. Its first-year NOI loss is more than three times the apartment's in percentage terms (37.4% versus 11.3%). For a lender, a 37% NOI decline turns a 1.50x DSCR into 0.94x. For an owner, it is the year the equity is tested. The office building looks resilient in year 1 and is not. Its NOI decline is delayed and accumulates as leases roll. A buyer who capitalizes the office's year-1 NOI in a recession overpays. A buyer who capitalizes the hotel's trough NOI may underpay, because hotel NOI also recovers first. **Value the hotel on through-cycle NOI with an explicit trough. Value the office on the NOI after the expected rollover, plus leasing costs.**

*Reproduce:* `tests/test_ch04_examples.py::test_example_4_8`

#### 4.8.2 Sequence through a cycle

[HYPOTHESIS, consistent with the operating mechanics above and with the 2009 hotel data in §4.9]:

1. **Months 0–6 after the peak:** hotel group cancellations and transient demand weaken; RevPAR turns negative; lenders begin tightening (SLOOS).
2. **Months 3–12:** apartment concessions rise and new-lease rents fall; hotel NOI declines accelerate as cost cuts lag revenue.
3. **Months 6–36:** office and industrial vacancy rises as leases expire; sublease space appears; effective rents fall through free rent and TI before face rents move.
4. **Months 12–48:** appraisals and cap rates adjust; delinquencies and special servicing rise; refinancing gaps crystallize at maturity.

Hotels also lead the recovery: the same nightly repricing that brings the fall forward brings the rebound forward too.

---

### 4.9 Historical episode: the 2007–09 recession in real time (with 2001 for contrast)

This section separates **what was published at the time** from **what we know now**. Facts are from the original BEA, BLS, NBER, Federal Reserve and STR releases cited in `references/sources_ch04.md`. ALFRED vintage downloads could not be retrieved in this pass. The real-time figures below are the published release values, which are the vintages themselves, but a cross-check against ALFRED is *(verification pending)*.

#### 4.9.1 Date and environment

By late 2007 housing construction was falling and subprime mortgage losses had disrupted funding markets. CRE prices were near cyclical highs, and CMBS issuance had financed a large share of acquisitions at high leverage *(magnitudes verification pending; qualitative characterization)*.

#### 4.9.2 What the early data showed

| Release date | Release | What it showed at the time | Source |
|---|---|---|---|
| 1 Feb 2008 | Employment Situation, January 2008 | Payrolls **−17,000**, the first decline since August 2003; unemployment rate 4.9%. Press reports put the consensus at about +70,000 | [FACT] BLS release (VERIFIED-PRIMARY via search excerpt); consensus figure from press reports (class C) |
| 30 Apr 2008 | GDP Q1 2008, advance | Real GDP **+0.6%** annualized, the same pace as the then-current estimate for Q4 2007. Inventory investment added 0.81 pp and residential investment subtracted 1.23 pp | [FACT] BEA release (VERIFIED-PRIMARY via search excerpt) |
| 30 Oct 2008 | GDP Q3 2008, advance | Real GDP **−0.3%** annualized; consumer spending −3.1% | [FACT] BEA |
| 25 Nov 2008 | GDP Q3 2008, preliminary | Revised to **−0.5%** | [FACT] BEA |
| 1 Dec 2008 | NBER announcement | Peak dated **December 2007**, a year after the fact. Payroll employment had peaked in December 2007 and household employment in November 2007 | [FACT] NBER |
| 30 Jan 2009 | GDP Q4 2008, advance | Real GDP **−3.8%** annualized | [FACT] BEA |
| 27 Feb 2009 | GDP Q4 2008, preliminary | Revised to **−6.2%**, mainly on inventories, services exports and nonresidential structures | [FACT] BEA |
| Mar 2009 | GDP Q4 2008, final (third) | **−6.3%** | [FACT] BEA |
| Feb 2009 | SLOOS, January 2009 survey | About **80%** of domestic banks reported tightening CRE standards over the prior three months, down from about 85% in October 2008; about 55% reported weaker CRE demand | [FACT] Federal Reserve SLOOS (VERIFIED-PRIMARY via search excerpt) |
| Oct 2009 | CES preliminary benchmark | March 2009 payroll level to be revised down about **824,000** | [FACT] BLS |
| 26 Jan 2010 | STR year-end 2009 | U.S. hotel occupancy 55.1% (−8.7%), ADR \$97.51 (−8.8%), RevPAR \$53.71 (**−16.7%**); New York RevPAR −26.3% | [FACT] STR via trade press (VERIFIED-SECONDARY) |
| Feb 2010 | CES final benchmark | March 2009 level revised down **902,000** (−0.7%) to 131,175,000. In the 12 months to March 2009 payrolls fell almost 5.8 million (−4.2%), the largest 12-month decline in the CES series' history back to 1939 | [FACT] BLS benchmark article |
| 20 Sep 2010 | NBER announcement | Trough dated **June 2009**, 15 months after the fact | [FACT] NBER |
| 2011 | BEA annual revision | Q4 2008 revised to **−8.9%** annualized | [FACT] BEA, *Survey of Current Business* (VERIFIED-SECONDARY via search excerpt); later comprehensive revisions may have changed the current-vintage value *(verification pending)* |

#### 4.9.3 The arithmetic of the revisions

The Q4 2008 advance estimate of −3.8% annualized corresponds to a quarterly decline of $(0.962)^{1/4} - 1 = -0.96\%$. The 2011 vintage of −8.9% corresponds to $(0.911)^{1/4} - 1 = -2.30\%$. The first published number captured well under half of the contraction later measured. The revision, −5.1 percentage points annualized, was larger than the advance estimate itself.

The payroll benchmark of −902,000 equals $902/(131{,}175 + 902) = 0.68\%$ of the pre-benchmark level, which BLS rounded to −0.7%. The preliminary benchmark announced in October 2009 (−824,000) captured 91% of the final revision. Early benchmark news was informative.

The STR figures are internally consistent: $(1-0.087)(1-0.088) - 1 = -16.7\%$, and $0.551 \times \$97.51 = \$53.73$, versus the reported \$53.71; the gap is rounding and day-weighting. They imply 2008 levels of about 60.4% occupancy, \$106.92 ADR and \$64.48 RevPAR [INFERENCE: back-calculated].

#### 4.9.4 The 2001 contrast: revisions that moved in both directions

In 2001 the BEA's advance estimate for Q3 2001 (31 October 2001) showed real GDP **−0.4%** annualized. The preliminary estimate (30 November) revised it to −1.1%, and the final estimate (21 December) to **−1.3%** [FACT; BEA releases, VERIFIED-PRIMARY via search excerpt]. Under the estimates available in late 2001, Q3 was the only negative quarter. The July 2002 annual revision showed declines in each of the first three quarters of 2001. The 2004 comprehensive revision changed the pattern again: a decline in Q1, an increase in Q2, and a decline in Q3 [FACT; secondary accounts of the BEA revisions, VERIFIED-SECONDARY]. The NBER dated the peak at March 2001 (announced 26 November 2001) and the trough at November 2001 (announced 17 July 2003). Under no vintage did the 2001 recession satisfy the "two consecutive negative quarters" rule of thumb in real time. The NBER does not use that rule.

#### 4.9.5 What was knowable then, and competing interpretations

**Knowable by mid-2008:** payrolls had been declining since January; the curve had inverted in 2006–07 *(timing verification pending)*; banks were tightening CRE standards broadly; hotel RevPAR growth was slowing *(2008 monthly STR data verification pending)*. **Not knowable:** that Q4 2008 would turn out to be the deepest quarterly decline of the post-war period to that date, or that a major investment bank would fail in September 2008.

**Interpretations available at the time** [INFERENCE]: (a) a housing-led slowdown similar to 1990–91 or 2001, mild because consumption would hold; (b) a credit-led recession in which bank capital losses would amplify the downturn through lending standards. The SLOOS data favored (b) well before the GDP data did, because standards were tightening at a breadth seen only in severe credit episodes *(historical comparison of breadth verification pending)*.

#### 4.9.6 The CRE transmission angle

* **Hotels moved first and hardest.** U.S. RevPAR fell 16.7% in 2009, with occupancy and ADR both falling by more than 8% [FACT; STR]. With operating leverage near 2× (Example 4.8), NOI declines of 30–40% for typical hotels were arithmetically implied [INFERENCE; property-level NOI data not cited].
* **Credit tightened before NOI fell.** Most domestic banks reported tighter CRE standards in October 2008 and January 2009 [FACT; SLOOS]. In the January 2009 survey about 15% of domestic banks, on net, said the CMBS market's shutdown had *increased* their own CRE lending, but not enough to replace the lost capacity [FACT for the 15%; INFERENCE for the replacement claim].
* **Refinancing gaps crystallized at maturity.** Loans written at 2005–07 values and LTVs could not be refinanced at lower values and tighter LTVs without new equity (Example 4.4 and Problem 4.9 show the arithmetic). The losses showed up years after the recession had ended, as loans matured.

#### 4.9.7 What the episode does and does not establish

It **establishes** that (1) advance GDP estimates near turning points can understate the contraction by more than half; (2) official recession dating comes far too late for investment timing; (3) bank-survey credit data and payroll trends carried information earlier than GDP; and (4) hotels transmitted the shock to CRE NOI first and most severely.

It does **not establish** that revisions are always toward weakness. The 2001 revisions moved in both directions across vintages. Nor does it establish that a given SLOOS reading forecasts a given NOI decline: one severe episode is not a calibration sample. Finally, 2007–09 was a credit-led recession. A demand shock such as 2020, or an inflation-driven slowdown, transmits through different channels and at different speeds.

---

### 4.10 Decision exercise: back to the hotel and the refinancing

Return to §4.1. You have ten days. Example 4.4 has already sized the office refinancing gap.

#### The decision

Prepare a one-page committee memo using `desk/investment_memos/investment_committee_memo.md` and `desk/scenario_templates/economic_release_analysis.md`. It must include:

1. **Recession probability.** Combine the curve (Example 4.6) and the Sahm reading of 0.37, which is not yet a signal but is in the elevated zone. State your prior, the likelihood ratios you assume, and whether you treat the signals as independent.
2. **Hotel NOI under recession.** Apply the operating-leverage arithmetic of Example 4.8 to the trailing \$2.43m NOI with stated assumptions. Compute DSCR at the cap strike and the debt yield at trough NOI.
3. **The sponsor's 4% RevPAR growth.** Compare it with trailing −1.5% RevPAR and the macro dashboard. Explain what would have to be true for it to be realistic.
4. **The office refinancing.** Reserve the equity gap from Example 4.4 before sizing the hotel commitment.
5. **The decision.** Bid at a stated maximum price, bid conditionally (for example, with lower leverage or a longer rate cap), or abstain. **Abstention is a legitimate and possibly the best answer** if the deal works only when recession has a weight well below the posterior you computed.
6. **Invalidation and update criteria.** Name the data releases over the next 90 days that would change your view in each direction.

**Rubric** (detailed in `problems/solutions/ch04_solutions.md` §Decision exercise). Full credit requires: a recession probability derived from the base rate rather than asserted; a trough-NOI calculation with operating leverage; recognition that the payroll figure is weak net of revisions; reserving liquidity for the office gap; and a decision rule that would have been written the same way before seeing the sponsor's deck. No single bid is correct.

---

### 4.11 When the relationships fail

1. **The yield curve can stay inverted without a recession.** The 2022–24 inversion was the longest in decades and had not been followed by an NBER recession as of the J.P. Morgan commentary. Explanations offered include term-premium compression and the economy's lower sensitivity to short rates because borrowers had locked in fixed-rate debt [competing interpretations; SPECULATION as to which dominates].
2. **The Sahm rule can trigger on labor-supply growth.** A rising unemployment rate driven by labor-force entrants is not the same as one driven by layoffs. Check initial claims and the layoff rate before concluding that the loop is running.
3. **GDP and GDI can disagree.** Near turning points, the income side has sometimes signaled weakness earlier than the expenditure side. The statistical discrepancy is information, not noise to be ignored *(specific episodes verification pending)*.
4. **Composition effects distort wages and productivity.** Average hourly earnings jump when low-wage workers lose jobs. Productivity jumps when hours are cut. Neither is a sign of strength.
5. **Surprise sensitivities change sign with the policy regime.** "Good news is bad news" is a regime, not a constant. A sensitivity estimated in a growth-scare period will mislead in an inflation-fighting period.
6. **Non-economic shocks bypass the leading indicators.** The 2020 recession began with a public-health shutdown that no yield curve or loan survey anticipated. The NBER dated it February to April 2020. Hotels fell further and faster than any leading indicator implied.
7. **CRE transmission depends on lease structure, not property-type labels.** A hotel with a long-term master lease to a creditworthy operator behaves like a net-lease asset. An office with 40% of leases rolling next year behaves like an apartment building with downtime. Use the parameters, not the label.
8. **Revisions are not symmetric across episodes.** 2007–09 revisions made the recession much worse; 2001's moved in both directions. Do not assume a direction. Assume a band.

---

### 4.12 Frequent analytical errors

1. **Multiplying quarterly growth by four.** It is close at normal rates, but the convention is compounding. More importantly, people forget that the reported number is *already* annualized and annualize it again.
2. **Reading YoY growth as the current pace.** YoY lags turning points by about two quarters (Example 4.2).
3. **Treating imports as a drag on GDP.** Imports are subtracted only because they were included elsewhere.
4. **Ignoring payroll revisions.** The effective surprise includes them (Example 4.7).
5. **Confusing $P(\text{signal}\mid\text{recession})$ with $P(\text{recession}\mid\text{signal})$.** "It has preceded every recession" says nothing about false positives or the base rate (Example 4.6).
6. **Waiting for the NBER.** Its dates arrive 8–20 months after the turning points in the episodes above.
7. **Reading SLOOS "net 0%" as "credit is easy".** It means standards stopped *changing*.
8. **Capitalizing a recession-year office NOI as if it were the full repricing.** The rollover is still coming (Example 4.8 check).
9. **Treating the four-quadrant table as a trading rule.** It describes tendencies conditional on surprises, not on the regime label.
10. **Underwriting hotel labor cost at the same growth rate as ADR.** The late-cycle margin squeeze lives in that gap (Example 4.3).
11. **Using the latest vintage to judge a past decision.** A 2008 decision should be judged against the data available in 2008, not the data published in 2011.

---

### 4.13 Connections to other chapters

* **Chapter 2 (Price Formation):** appraisal-based CRE values lag the cycle; REITs lead it.
* **Chapter 3 (Mental Models):** Bayesian updating (Example 4.6); reflexive credit loops (§4.2, Example 4.4).
* **Chapter 5 (Central Banks):** how policy responds to the unemployment and inflation data in this chapter; Taylor-type rules use the same inputs.
* **Chapter 6 (Fixed Income):** duration and the curve mechanics behind Example 4.7.
* **Chapter 10 (Capital Structure):** loan-sizing constraints in Example 4.4 and Problem 4.9.
* **Chapter 11 (Hotels):** a full USALI treatment of the operating leverage in Example 4.8.
* **Chapter 12 (CRE Cycles and Distress):** maturity walls and loan sales downstream of the credit loop.
* **Chapter 20 (Probability):** base rates, calibration, and combining dependent signals.
* **Chapter 23 (History):** fuller treatments of 2001, 2007–09 and 2020.
* `desk/scenario_templates/economic_release_analysis.md` and `weekly_macro_outlook.md` operationalize §4.7.

---

### 4.14 One-page reference sheet

**Growth conventions**

| Quantity | Formula |
|---|---|
| Annualized from quarterly | $a = (1+q)^4 - 1$ |
| Quarterly from annualized | $q = (1+a)^{1/4} - 1$ |
| YoY (quarterly data) | $Y_t/Y_{t-4} - 1 = \prod (1+q) - 1$ |
| Contribution of component $i$ | $\Delta X_i / Y_{t-1} = s_i g_i$ |
| Productivity growth | $(1+g_Y)/(1+g_H) - 1$ |
| ULC growth | $(1+g_{w})/(1+g_{prod}) - 1$ |

**Recession detection**

| Tool | Rule | Main weakness |
|---|---|---|
| NBER | Retrospective committee dating, monthly indicators | Announced 8–20 months after the turning points (2001, 2007–09) |
| Sahm rule | $\bar u^{(3)}_t - \min_{12m}\bar u^{(3)} \ge 0.50$ | Recognition, not forecast; rounding, revisions, labor-supply shifts |
| Term spread (10y–3m) | Inversion | Long, variable lead; false positives (1966; 2022–24 so far) |
| Bayes | $P(R\mid S) = \dfrac{P(S\mid R)P(R)}{P(S\mid R)P(R) + P(S\mid\bar R)(1-P(R))}$ | Signals are not independent; sample is tiny |

**Credit and surprises**

| Quantity | Formula |
|---|---|
| SLOOS net % | (tightened − eased) / respondents |
| Standardized surprise | $z = (\text{actual} - \text{consensus})/\sigma$ |
| Effective payroll surprise | headline surprise + net revisions |
| Max loan | $\min(LTV \cdot V,\ NOI/(DSCR \cdot K),\ NOI/DY)$ |

**Transmission**

| Quantity | Formula |
|---|---|
| Operating leverage | $NOI = R(1-v) - F$; $DOL = R(1-v)/NOI$ |
| Leased-asset year-1 revenue | $R(1-\rho) + R\rho[\pi(1+m) + (1-\pi)(1+m)(12-d)/12]$ |
| Speed ranking | Hotels → apartments → office/industrial → appraisals and cap rates |

**Rules of thumb (to be tested, not trusted).** Investment is about a sixth of GDP and often most of the recession. YoY growth lags turning points by about two quarters. A Sahm reading of 0.3–0.5 is a warning zone. Hotel NOI moves about twice as much as hotel revenue. Advance GDP near turning points can miss more than half of the move.

---

### References for this chapter

Full entries with verification status are in `references/sources_ch04.md`.

* Bureau of Economic Analysis. *Gross Domestic Product* news releases: Q3 2001 advance (31 Oct 2001), preliminary (30 Nov 2001) and final (21 Dec 2001); Q1 2008 advance (30 Apr 2008); Q3 2008 advance (30 Oct 2008) and preliminary (25 Nov 2008); Q4 2008 advance (30 Jan 2009) and preliminary (27 Feb 2009). https://www.bea.gov/news
* Bureau of Economic Analysis, *Survey of Current Business*, November 2012, "Taking Account" (Q4 2008 revision history).
* Bureau of Labor Statistics. *The Employment Situation — January 2008* (1 Feb 2008); CES benchmark revision articles for March 2009.
* National Bureau of Economic Research, Business Cycle Dating Committee announcements (26 Nov 2001; 17 Jul 2003; 1 Dec 2008; 20 Sep 2010) and the U.S. business-cycle chronology.
* Board of Governors of the Federal Reserve System. *Senior Loan Officer Opinion Survey on Bank Lending Practices*, January 2009, and later releases.
* Federal Reserve Bank of St. Louis, FRED: SAHMREALTIME series notes; DPCERE1Q156NBEA.
* Sahm, C. (2019). "Direct Stimulus Payments to Individuals." In *Recession Ready: Fiscal Policies to Stabilize the American Economy*, The Hamilton Project and Washington Center for Equitable Growth.
* STR, U.S. hotel performance year-end 2009 (26 Jan 2010), as reported in trade press.
* J.P. Morgan Asset Management. "Was the yield curve inversion wrong in predicting a US recession?"
* Federal Reserve Bank of St. Louis, *On the Economy* (Sep 2023). "What Is the Probability of a Recession? The Message from Yield Spreads."


\newpage

## Chapter 5 — Central Banks and Monetary Policy

> **Status:** Complete (v1.0). Numerical examples are reproduced in `tests/test_ch05_examples.py`. Problems are in `problems/questions/ch05_problems.md` and solutions in `problems/solutions/ch05_solutions.md`. Sources are listed in `references/sources_ch05.md` (IDs ch05-S01 to ch05-S22). Three items remain *(verification pending)* and are flagged where they appear: the exact peak-to-trough decline in a commercial property price index, the exact statutory wording of the Federal Reserve Act's monetary-policy objectives, and the current text of the FOMC's strategy statement after its 2025 review.

### Learning objectives

After this chapter you should be able to:

1. Describe how the Federal Reserve sets the overnight rate in an ample-reserves regime: the target range, interest on reserve balances (IORB), the overnight reverse repo facility (ON RRP), the standing repo facility (SRF), and the discount window. Explain why each administered rate sits where it does and which market rates it pins.
2. Compute a Taylor-rule prescription and its main variants (balanced-approach, inertial), and quantify how uncertainty about the neutral rate and the choice of inflation measure widen the prescription band.
3. Move between nominal rates, real rates, and inflation compensation with the exact Fisher relation. Interpret a TIPS breakeven, and say what it is not.
4. Price CME 30-Day Federal Funds futures as 100 minus the average daily effective rate for the month. Back out the market-implied probability of a policy move at a meeting with correct day-weighting, and cross-check it with the following month's contract.
5. Read the Treasury curve as expected policy plus a term premium. Compute an implied forward rate and decompose a long yield.
6. Trace the three channels by which policy reaches a CRE deal: (i) policy rate → SOFR → floating coupon → DSCR; (ii) 10-year Treasury → fixed coupon → loan constant → DSCR-sized proceeds; (iii) bank capital, liquidity, and lending standards → credit availability. Quantify the first two.
7. Explain the balance-sheet mechanics of quantitative easing and tightening, and state honestly how uncertain their term-premium effects are.
8. Use the 2022–23 tightening cycle as evidence, separating what was knowable at each date from what is known now.

---

### 5.1 Opening investment problem: a hotel refinance in a hiking month

It is a Thursday in the third week of the month. You advise the owner of a 210-room select-service hotel. All deal facts in this section are [HYPOTHESIS].

* The hotel's trailing NOI after a 4% FF&E reserve is \$2.4 million.
* The existing \$30.0 million floating-rate loan was originated three years ago at one-month Term SOFR + 3.00%, interest-only. It matures in seven months. The rate cap bought at origination is struck at 3.00% and expires with the loan.
* A life-company lender has quoted a 10-year fixed-rate refinance at the 10-year Treasury plus 2.00%, 30-year amortization, sized to the lesser of 65% LTV, 1.25x DSCR, and an 8.0% debt yield. The rate is set at closing, not today.
* A debt fund will extend the floating loan for 18 months at SOFR + 3.50%, conditional on a new cap.

The FOMC meets in eleven days. The fed funds futures contract for the meeting month implies a meaningful probability of a 25 bp hike. Overnight a consumer-price report surprised to the upside. The 10-year Treasury rose 15 bp on the release.

Three questions define the decision.

1. **What does the market expect the Fed to do, and how sure is it?** You need a probability, not a headline.
2. **Which loan is more exposed to the next move: the fixed refinance (priced off the 10-year) or the floating extension (priced off SOFR)?** The answer depends on which part of the curve the inflation surprise moves.
3. **What has already been priced?** If the futures already imply a hike, a hike that arrives will not move SOFR forwards much. What moves forwards is a surprise relative to that pricing.

The chapter builds the tools to answer each question with numbers. Example 5.4 computes the probability. Examples 5.6 and 5.7 size the two loans. Section 5.10 returns to the decision.

---

### 5.2 Economic intuition

#### What a central bank actually controls

The Federal Reserve does not set mortgage rates, cap rates, or the 10-year Treasury yield. It sets a handful of **administered rates** on its own facilities. Through arbitrage, those rates anchor the price of overnight money. Everything else a CRE investor cares about is a market price that *depends on* the expected path of that overnight rate, plus compensation for risk.

Three layers matter:

| Layer | Who sets it | Example | How quickly policy reaches it |
|---|---|---|---|
| Overnight rates | Administered rates + arbitrage | EFFR, SOFR | Same day as the decision takes effect |
| Term risk-free rates | Market: expected path of overnight rates + term premium | 2-year and 10-year Treasury | Continuously, *before* decisions, on expectations |
| Risky rates and availability | Market and lenders: risk-free + credit spread + quantity rationing | CMBS coupons, bank loan spreads, LTV limits | Spreads immediately; lending standards over quarters |

The intuition for the speculator: **policy decisions are mostly priced before they happen**. Rate decisions that match expectations move little. What moves markets is news about the *path*: a data surprise, a change in guidance, a change in the reaction function. Then a CRE transaction market, which has no continuous price, absorbs that news over months.

#### Why the policy rate matters for a property

A property's value is the present value of its NOI. Monetary policy enters through three doors.

1. **Discount rate.** Higher real risk-free rates raise the required return unless risk premia compress or expected growth rises. Cap rates are linked to long real yields, but the link is loose and lagged (Chapter 6).
2. **Debt cost and debt quantity.** Floating coupons reset with SOFR. Fixed coupons are set off the 10-year at closing. Higher coupons raise the loan constant, and with DSCR sizing they cut proceeds. Lower proceeds mean more equity per deal, fewer qualified buyers, and lower prices.
3. **Credit availability.** When tighter policy erodes bank capital (unrealized losses on securities), raises deposit costs, or triggers deposit flight, banks tighten standards. A borrower may face a lower LTV, a higher DSCR hurdle, or no quote at all. This channel is non-linear. It operates through quantities, not prices, and it is where CRE distress begins.

#### Why an inflation surprise is a policy event

When inflation surprises upward, the market raises its estimate of the policy path. Short rates rise most if the surprise changes the next few meetings. Long rates rise if it changes the perceived persistence of inflation or the term premium. A hotel owner with a floating loan is exposed to the front end. A seller whose buyer needs fixed-rate debt is exposed to the 10-year. A sponsor with a bank relationship is exposed to whatever the shock does to the bank's balance sheet. Case H (`cases/hypothetical/case_H_cross_asset_macro_shock/`) traces one such shock across an entire portfolio.

---

### 5.3 Technical definitions

| Term | Definition |
|---|---|
| Dual mandate | The FOMC's statutory goals of maximum employment and stable prices. The statute also lists moderate long-term interest rates *(exact statutory wording, Federal Reserve Act §2A: verification pending)* [ch05-S21]. |
| Longer-run inflation goal | 2% inflation as measured by the annual change in the PCE price index, first stated in January 2012 and reaffirmed since [FACT; ch05-S20]. The surrounding strategy text was revised in 2020 and reviewed again in 2025 *(current wording: verification pending)*. |
| FOMC | Federal Open Market Committee. Twelve voting members: the seven Governors, the President of the New York Fed, and four of the other eleven Reserve Bank presidents on a rotating one-year basis. Eight scheduled meetings per year, normally two days long [FACT; ch05-S19]. |
| Target range | The 25 bp range the FOMC sets for the federal funds rate, for example 3.75%–4.00%. |
| EFFR | Effective federal funds rate: the volume-weighted median rate on overnight unsecured fed funds trades, published by the New York Fed. |
| IORB | Interest on reserve balances, paid by the Fed to banks on reserves. The principal tool for keeping EFFR in the range. Set by the Board. |
| ON RRP | Overnight reverse repurchase facility. Eligible non-banks (money funds, GSEs) lend cash to the Fed overnight against Treasury collateral at the offering rate. Sets a soft floor for money-market rates. |
| SRF | Standing repo facility. The Fed lends cash overnight against Treasuries, agency debt, and agency MBS at a fixed rate. A ceiling-type backstop for repo rates. Established 28 July 2021 [FACT; ch05-S09]. |
| Primary credit (discount window) | Fully secured lending to sound depository institutions, at the primary credit rate. |
| SOFR | Secured Overnight Financing Rate: a broad measure of overnight Treasury repo rates, published by the New York Fed. The base rate for most U.S. floating CRE loans. Term SOFR is a forward-looking term rate derived from SOFR derivatives. |
| Neutral rate $r^*$ | The real policy rate consistent with output at potential and stable inflation. Unobservable. Estimated with wide error bands. |
| Breakeven inflation | Nominal Treasury yield minus TIPS real yield of the same maturity. Inflation *compensation*: expected inflation plus an inflation risk premium, minus a TIPS liquidity premium. |
| Term premium | The extra yield investors demand to hold a long bond rather than roll short bills over the same horizon. Not directly observable. Model-dependent. |
| QE / QT | Quantitative easing: Fed purchases of long-duration securities paid for by creating reserves. Quantitative tightening: allowing securities to mature without reinvestment, which drains reserves. |
| Fed funds futures | CME 30-Day Federal Funds futures. Price $= 100 - R$, where $R$ is the arithmetic average of daily EFFR over the contract month. \$4,167 per index point, which is \$41.67 per basis point [FACT; ch05-S11]. |

---

### 5.4 Equations and derivations

#### 5.4.1 The policy corridor in an ample-reserves regime

Since 2008 the Fed has operated with abundant reserves. In that regime the quantity of reserves does not pin the overnight rate at the margin. Administered rates do.

* **IORB** gives banks a risk-free overnight return on reserves. A bank will not lend fed funds much below IORB, because it can earn IORB instead. It will borrow fed funds from institutions that cannot earn IORB (chiefly the Federal Home Loan Banks) whenever it can borrow below IORB. Arbitrage profit per dollar per day $= (IORB - r_{ff})/360$.
* **ON RRP** offers non-banks a risk-free overnight rate. A money fund will not lend in repo below the ON RRP offering rate. That puts a soft floor under SOFR and other overnight secured rates.
* **SRF** and **primary credit** let eligible institutions borrow from the Fed at a fixed rate. A borrower that can use them will not pay much above that rate. That is a ceiling, softened by stigma and operational limits.

The settings in the implementation note of 16 September 2026, the most recent found when this chapter was written, were [FACT; ch05-S01, ch05-S02]:

| Instrument | Setting | Position in the range |
|---|---|---|
| Federal funds target range | 3.75%–4.00% (raised 25 bp) | — |
| IORB | 3.90%, effective 17 September 2026 | 15 bp above the bottom |
| ON RRP offering rate | 3.75%; per-counterparty limit \$160 billion per day | Bottom |
| SRF rate | 4.00% | Top |
| Primary credit rate | 4.00% | Top |

The 16 September 2026 decision raised the range by 25 bp after a hold at 3.50%–3.75% at the 28–29 July 2026 meeting [FACT; ch05-S02, ch05-S03]. Check the latest implementation note on federalreserve.gov before using these settings, because they change at every decision.

#### 5.4.2 The Taylor rule and its variants

Taylor (1993) proposed a simple rule that described Federal Reserve behavior in the late 1980s and early 1990s [ch05-S13]:

$$i = r^* + \pi + a(\pi - \pi^*) + b\,y, \qquad a = b = 0.5,\ r^* = 2\%,\ \pi^* = 2\%,$$

where $i$ is the prescribed nominal policy rate, $\pi$ trailing inflation, and $y$ the output gap in percent of potential.

**Derivation of the intuition.** Write the real policy rate as $i - \pi$. The rule sets it equal to neutral, $r^*$, plus leaning against inflation and output deviations. Because the coefficient on $\pi$ in the nominal rate is $1 + a = 1.5 > 1$, a one-point rise in inflation raises the *real* policy rate by 0.5 points. This is the **Taylor principle**. A rule with a coefficient below one lets real rates fall as inflation rises, which feeds inflation.

**Variants** used in Federal Reserve communications [ch05-S14]:

| Rule | Prescription |
|---|---|
| Taylor (1993) | $r^* + \pi + 0.5(\pi - 2) + 0.5y$ |
| Balanced-approach | $r^* + \pi + 0.5(\pi - 2) + 1.0y$ (the gap coefficient is doubled) |
| Inertial | $i_t = \rho\, i_{t-1} + (1-\rho)\, i_t^{rule}$ with $\rho$ typically 0.8–0.9 [HYPOTHESIS for the range] |
| Unemployment form | replaces $y$ with $\approx 2(u^* - u)$ (Okun's-law conversion; the factor 2 is a convention [HYPOTHESIS]) |

**Limits.** Every input is uncertain:

* $r^*$ is unobservable. Different models give materially different estimates. A 1-point error in $r^*$ is a 1-point error in the prescription.
* The inflation measure matters: headline or core, CPI or PCE, trailing 12 months or forecast.
* The output gap is revised heavily after the fact. Real-time gaps differ from final ones.
* The rule ignores financial stability, the effective lower bound, balance-sheet policy, and the lag between policy and inflation.

The rule is a **benchmark for the reaction function**, not a forecast of the next decision. Its value to a speculator is to flag when the market's priced path diverges sharply from every reasonable rule. Then you ask why.

#### 5.4.3 Fisher: nominal, real, and inflation compensation

The exact Fisher relation:

$$(1 + i) = (1 + r)(1 + \pi^e) \quad\Rightarrow\quad r = \frac{1+i}{1+\pi^e} - 1 \approx i - \pi^e.$$

The approximation error is about $r\,\pi^e$. It is small at low rates and grows when rates and inflation are both high. For TIPS, the market quotes a real yield $r_{TIPS}$ directly. The **breakeven** is

$$BEI = \frac{1 + y_{nom}}{1 + r_{TIPS}} - 1 \approx y_{nom} - r_{TIPS}.$$

Breakeven inflation is **compensation**, not a forecast:

$$BEI = E[\pi] + \text{inflation risk premium} - \text{TIPS liquidity premium}.$$

TIPS index to CPI-U, not to the PCE index in which the Fed's goal is stated. CPI inflation has tended to run above PCE inflation [HYPOTHESIS for any specific gap; the wedge varies over time]. In a flight to liquidity, nominal Treasuries can outperform TIPS for reasons unrelated to inflation, and breakevens fall.

**Survey measures** (University of Michigan, the New York Fed's Survey of Consumer Expectations, the Philadelphia Fed's Survey of Professional Forecasters) measure stated expectations directly. They have no risk premium, but they are subject to sampling noise, framing effects, and, for households, a tendency to track salient prices such as gasoline. When surveys and breakevens diverge, neither is automatically right. The divergence itself is information about which group is moving and why (Problem 5.10).

#### 5.4.4 Fed funds futures and implied probabilities

Contract price $F = 100 - \bar R$, where $\bar R$ is the arithmetic average of daily EFFR over all calendar days in the contract month. Weekends and holidays carry the previous business day's rate.

Suppose a month has $N$ days, a decision takes effect on day $d+1$ (the day after the meeting's final day), the pre-meeting EFFR is $r_0$, and the post-meeting expected rate is $E[r_1]$. Then

$$\bar R = \frac{d\, r_0 + (N - d)\,E[r_1]}{N} \quad\Rightarrow\quad E[r_1] = \frac{N\bar R - d\, r_0}{N - d}.$$

If the only outcomes are "no change" and "change of size $\Delta$", then $E[r_1] = r_0 + p\Delta$, so

$$p = \frac{E[r_1] - r_0}{\Delta}.$$

**Day-weighting matters.** Only $(N-d)/N$ of the month is affected, so the naive formula $(\bar R - r_0)/\Delta$ understates $p$ by the factor $(N-d)/N$. When the meeting is late in the month, $(N-d)$ is small and the inference is noisy: one tick of price error is multiplied by $N/(N-d)$. Use the **next** month's contract, which lies entirely after the meeting, as the cross-check.

**Caveats.**

1. The futures price embeds a risk premium. Implied probabilities are risk-neutral, not physical.
2. The EFFR–IORB spread can drift for reasons unrelated to policy (reserve scarcity, quarter-end, Treasury settlement days). A 2 bp drift is 8% of a 25 bp move.
3. With three or more possible outcomes (hold, 25, 50), one price cannot identify the probabilities. You need another instrument (options, SOFR futures) or an assumption.

#### 5.4.5 The yield curve as expected policy plus term premium

For zero-coupon yields with annual compounding, the one-year forward rate one year ahead is

$$f_{1,2} = \frac{(1+y_2)^2}{(1+y_1)} - 1.$$

Under the pure expectations hypothesis $f_{1,2}$ would equal the expected one-year rate a year from now. In practice

$$y_n \approx \frac{1}{n}\sum_{t=0}^{n-1} E_t[i_{t}] + TP_n,$$

where $TP_n$ is the term premium. The decomposition depends on the model used to estimate expected short rates. Published estimates from different models can differ by more than 50 bp at the same date [HYPOTHESIS: magnitude of model disagreement offered as an order of magnitude, not a sourced figure].

#### 5.4.6 From the policy rate to a CRE loan

**Floating channel.** For an interest-only floating loan accruing on an actual/360 basis,

$$DS_{float} = L\,(SOFR + s)\,\frac{365}{360}, \qquad DSCR = \frac{NOI}{DS_{float}}.$$

A cap at strike $K_{cap}$ limits the SOFR component to $\min(SOFR, K_{cap})$. The SOFR at which DSCR hits a covenant level $D$ is

$$SOFR^{\dagger} = \frac{NOI}{D\, L\,(365/360)} - s.$$

**Fixed channel.** The coupon is set at closing as $c = y_{10} + s_{fixed}$. The loan constant with monthly amortization over $n$ months is

$$K = 12\cdot\frac{c/12}{1 - (1 + c/12)^{-n}},$$

and DSCR-constrained proceeds are $L_{DSCR} = NOI/(D\,K)$. The elasticity of DSCR proceeds to the coupon is $-\,(\partial K/\partial c)(c/K)$. For 30-year amortization it is −0.64 at a 6.00% coupon, −0.68 at 6.50%, and −0.71 at 7.00% [computed; Example 5.7]. A 10% proportional rise in the coupon (65 bp at 6.50%) cuts DSCR proceeds by roughly 6.8%. Actual loan proceeds are the minimum over LTV, DSCR, and debt-yield constraints, so a rate shock can leave proceeds unchanged if LTV binds. The shock then reaches proceeds later, through appraised value.

**Availability channel.** No equation fits it well. Track the Senior Loan Officer Opinion Survey (SLOOS) net percentage tightening CRE standards, bank CRE loan growth, CMBS issuance, and the number of lender quotes per deal.

#### 5.4.7 QE and QT: balance-sheet mechanics

When the Fed buys \$100 of Treasuries from a dealer, the Fed's assets rise by \$100 (securities). Its liabilities rise by \$100 (reserves credited to the dealer's bank). The private sector holds \$100 less duration and \$100 more reserves. Under QT the Fed lets securities mature without reinvesting. The Treasury pays off the maturing bonds by drawing on its General Account (TGA), which it refills by issuing new debt to the public. Net effect: private holdings of Treasuries rise, and reserves or ON RRP balances fall.

The claimed effect on long yields operates through the **portfolio-balance** channel. Removing duration from private hands lowers the term premium, and returning it raises the term premium. Estimates of the size of the effect vary widely across studies and episodes. Announcement effects differ from flow effects, and they depend on the starting level of reserves. Treat any "bp per \$100 billion" figure as a model-dependent estimate with a wide range [HYPOTHESIS].

#### 5.4.8 Transmission beyond CRE, and why the dollar and equities move together on policy news

A hawkish surprise (higher expected policy path) produces a recognizable cross-asset pattern. Each leg has a mechanism, and each mechanism can fail.

| Market | Typical direction on a hawkish surprise | Mechanism | When it fails |
|---|---|---|---|
| 2-year Treasury | Up most | Direct repricing of the next several meetings | Surprise read as raising recession odds within the 2-year horizon |
| 10-year Treasury | Up, usually less than the 2-year | Expected path beyond two years plus term premium | Credibility gain lowers long-run inflation expectations: the curve flattens or inverts |
| Equity index | Down | Higher discount rate; weaker growth expectations | Surprise driven by strong real growth: earnings effect dominates |
| U.S. dollar | Up | Higher expected U.S. rates relative to other countries attract capital (covered-interest parity links forward points to rate differentials; Chapter 15) | Other central banks surprise in the same direction |
| Credit spreads | Wider | Higher default probability and lower risk appetite | Spread moves dominated by supply or technical factors |
| Private CRE | No print the same day; later lower bids, lower proceeds, fewer trades | Debt cost, proceeds, required returns | Strong NOI growth offsets cap-rate pressure |

[INFERENCE: the directions are the standard mechanisms, not a sourced empirical regularity. Case H quantifies one such day with hypothetical moves.]

The pattern matters for portfolio construction. A book that is long duration, long equities, long foreign currency, long credit, and long levered CRE has one dominant risk factor on inflation-release days, however diversified it looks by asset class. Case H computes the P&L of such a book.

#### 5.4.9 Inflation expectations: surveys versus markets

| Measure | Source | What it measures | Strength | Weakness |
|---|---|---|---|---|
| Household surveys | University of Michigan; New York Fed Survey of Consumer Expectations | Stated expectations of households | No risk premium; captures wage-setting psychology | Noisy; sensitive to gasoline and food prices; framing effects |
| Professional surveys | Philadelphia Fed Survey of Professional Forecasters | Forecasters' point and probability forecasts | Explicit horizons; probability bins | Herding; quarterly frequency |
| TIPS breakevens | Treasury market | Inflation compensation | Daily; tradable | Risk and liquidity premia; CPI not PCE |
| Inflation swaps | OTC market | Fixed-for-CPI swap rates | Clean term structure | Dealer balance-sheet effects; less transparent |
| 5-year, 5-year forward breakeven | Derived from 5- and 10-year breakevens | Long-run inflation compensation | Strips out near-term energy noise | Still contains premia |

The 5y5y forward breakeven uses the same forward arithmetic as Example 5.5: $(1+BEI_{10})^{10}/(1+BEI_5)^5$ raised to the power $1/5$, minus one. A central bank worried about de-anchoring watches whether long-horizon measures move with short-horizon ones. If a bad inflation print lifts one-year expectations but leaves 5y5y unchanged, expectations look anchored. If 5y5y also rises, the reaction function is likely to turn more hawkish [INFERENCE].

---

### 5.5 Worked examples

All inputs in the examples are hypothetical [HYPOTHESIS] unless tagged otherwise. Administered rates in Example 5.1 use the 16 September 2026 settings [FACT; ch05-S01].

#### Example 5.1 — The corridor at work: IORB arbitrage and where SOFR can trade

**Given.** Target range 3.75%–4.00%, IORB 3.90%, ON RRP 3.75%, SRF 4.00% [FACT]. A Federal Home Loan Bank, which cannot earn IORB, lends \$1.0 billion overnight in fed funds to a bank at 3.86% [HYPOTHESIS]. Money-market convention: actual/360.

**Find.** (a) The bank's daily and annualized arbitrage profit if it holds the funds as reserves. (b) The band within which SOFR should trade, and why. (c) The base coupon on a floating CRE loan at SOFR + 3.00% if SOFR prints 3.88% [HYPOTHESIS].

**Solution.**

(a) Daily profit $= \$1{,}000{,}000{,}000 \times (0.0390 - 0.0386)/360 = \$1{,}111.11$. Annualized over 365 days: $1{,}111.11 \times 365 = \$405{,}556$, a 4 bp spread on \$1 billion.

(b) Lower bound: money funds can earn 3.75% at the ON RRP, so they will not lend repo much below 3.75%. Upper bound: dealers can borrow at the SRF at 4.00%, so repo should not trade persistently above 4.00% unless stigma or operational limits bind. SOFR should trade between 3.75% and 4.00%, and in an ample-reserves regime it should trade close to IORB. Persistent prints of SOFR above IORB are a sign that reserves are becoming less than ample.

(c) Coupon $= 3.88\% + 3.00\% = 6.88\%$.

**Check.** The profit is positive only because the lender lacks IORB access. If both counterparties could earn IORB, the rate would converge to IORB and the arbitrage would vanish. That is why EFFR has tended to trade slightly *below* IORB in the ample-reserves regime [INFERENCE from the mechanism].

**Decision consequence.** A floating CRE borrower's base rate is effectively an administered rate plus a few basis points. When the FOMC moves the range, IORB, ON RRP, and SRF move with it. SOFR follows within a day, and every floating loan's coupon follows at its next reset. There is no lag on the floating channel. The lag is in NOI, appraisals, and lender behavior. Underwrite floating debt service from the futures- or swap-implied path, not from today's print.

**Reproduce:** `tests/test_ch05_examples.py::test_example_5_1`

#### Example 5.2 — Taylor-rule prescriptions and the width of the band

**Given.** Trailing core PCE inflation $\pi = 3.0\%$; output gap $y = -0.5\%$; inflation target 2%. Two neutral-rate estimates: Taylor's original $r^* = 2.00\%$ and a lower estimate $r^* = 0.75\%$. Policy range midpoint 3.875%. Inertial smoothing $\rho = 0.85$.

**Find.** Prescriptions under Taylor (1993) and balanced-approach rules for each $r^*$. Find the inertial next-step rate when the rule prescribes 4.00% and when it prescribes 5.25%.

**Solution.**

Taylor (1993), $r^* = 2.00\%$: $i = 2.00 + 3.00 + 0.5(3.00 - 2.00) + 0.5(-0.5) = 2.00 + 3.00 + 0.50 - 0.25 = 5.25\%$.

Taylor (1993), $r^* = 0.75\%$: $i = 0.75 + 3.00 + 0.50 - 0.25 = 4.00\%$.

Balanced-approach, $r^* = 2.00\%$: $i = 2.00 + 3.00 + 0.50 + 1.0(-0.5) = 5.00\%$.

Balanced-approach, $r^* = 0.75\%$: $i = 3.75\%$.

Inertial: $i_t = 0.85 \times 3.875 + 0.15 \times 4.00 = 3.89375\%$. With a rule prescription of 5.25%: $0.85 \times 3.875 + 0.15 \times 5.25 = 4.08125\%$.

| | $r^* = 0.75\%$ | $r^* = 2.00\%$ |
|---|---|---|
| Taylor (1993) | 4.00% | 5.25% |
| Balanced-approach | 3.75% | 5.00% |

**Check.** The difference between columns is exactly the 1.25-point difference in $r^*$, because $r^*$ enters one-for-one. The difference between rows is $0.5 \times |y| = 0.25$ point.

**Decision consequence.** Four defensible rules span 3.75%–5.25%, a 150 bp band, for the same data. The current range midpoint of 3.875% sits at the low end. A rule can tell you that policy is "restrictive relative to a low $r^*$" or "accommodative relative to Taylor's original $r^*$". It cannot tell you the next decision. For a CRE underwriter, the practical use is a stress range: a floating-rate deal that fails at a policy rate near the top of the rule band (here 5.25%) has a meaningful tail. The inertial row shows why actual policy moves in steps. Even a rule that prescribes 5.25% moves the rate only about 21 bp per step at $\rho = 0.85$.

**Reproduce:** `tests/test_ch05_examples.py::test_example_5_2`

#### Example 5.3 — Real yields, breakevens, and the real return on a cap rate

**Given.** 10-year nominal Treasury yield 4.30%; 10-year TIPS real yield 1.90%. An apartment building trades at a 6.00% cap on NOI after reserves. Assume NOI grows with inflation at the breakeven rate, with zero real growth, in perpetuity.

**Find.** (a) The breakeven, approximate and exact. (b) The implied nominal and real unlevered required return under the Gordon model. (c) The real risk premium over TIPS.

**Solution.**

(a) Approximate: $4.30\% - 1.90\% = 2.40\%$. Exact: $1.043/1.019 - 1 = 2.3553\%$. The 4.5 bp gap is the cross-term $r \cdot \pi$.

(b) Using the approximate breakeven as expected nominal NOI growth $g = 2.40\%$: $k = c + g = 6.00\% + 2.40\% = 8.40\%$ nominal. Real: $1.084/1.024 - 1 = 5.8594\%$.

(c) Real risk premium $= 5.8594\% - 1.90\% = 3.9594\%$, about 396 bp over TIPS.

**Check.** $(1.019)(1.039594)(1.024) = 1.0848 \approx 1.084$. The small residual arises because the premium is computed by subtraction, not by compounding.

**Decision consequence.** The comparison an investor should make is real to real: a 6.00% cap with inflation-linked NOI against a 1.90% TIPS yield, not against a 4.30% nominal yield. If NOI cannot keep pace with inflation (long fixed leases, capped renewals, or rising insurance and taxes), real growth is negative and the premium shrinks one-for-one. A 1-point shortfall of NOI growth against inflation takes the premium from about 3.96% to about 2.98%. Breakevens include risk and liquidity premia, so using them as the growth assumption is itself a [HYPOTHESIS] to be stated.

**Reproduce:** `tests/test_ch05_examples.py::test_example_5_3`

#### Example 5.4 — The implied probability of a hike, with day-weighting

**Given.** A 30-day month. The FOMC decision takes effect on day 17, so 16 days are at the pre-meeting rate. Pre-meeting EFFR $r_0 = 3.88\%$. The only alternatives are no change and a 25 bp hike. The meeting-month contract trades at 96.040. The next month's contract, which lies entirely after the meeting and has no meeting of its own, trades at 95.950. Assume EFFR stays at a fixed spread to IORB.

**Find.** (a) The expected post-meeting EFFR and the implied hike probability. (b) The naive (non-day-weighted) probability. (c) The cross-check from the next month's contract. (d) The P&L of 100 short meeting-month contracts at 96.040 in each outcome, and the expected P&L at the implied probability.

**Solution.**

(a) $\bar R = 100 - 96.040 = 3.960\%$.
$$E[r_1] = \frac{30(3.960) - 16(3.88)}{14} = \frac{118.80 - 62.08}{14} = \frac{56.72}{14} = 4.05143\%.$$
$p = (4.05143 - 3.88)/0.25 = 0.17143/0.25 = 68.57\%$.

(b) Naive: $(3.960 - 3.88)/0.25 = 32.0\%$. That understates $p$ by the factor $14/30$.

(c) Next month: $\bar R = 100 - 95.950 = 4.050\%$, so $p = (4.050 - 3.88)/0.25 = 68.0\%$. The two estimates agree within 0.6 percentage points. Tick rounding and EFFR–IORB drift explain differences of this size.

(d) If the Fed hikes, the month averages $(16 \times 3.88 + 14 \times 4.13)/30 = 3.99667\%$, so the contract settles at 96.00333. A short from 96.040 gains $3.667$ bp × \$41.67 × 100 = **\$15,279**. If the Fed holds, the settlement is $100 - 3.88 = 96.120$, and the short loses $8.0$ bp × \$41.67 × 100 = **−\$33,336**. Expected P&L at $p = 0.6857$: $0.6857(15{,}279) + 0.3143(-33{,}336) \approx \$0$.

**Check.** The expected P&L is zero at the market-implied probability, as it must be, because that probability was backed out of the price. Any profit from the trade requires a probability view that differs from 68.6% and is *correct*.

**Decision consequence.** A desk that read the meeting-month contract naively would believe a hike was a one-in-three chance when the market priced better than two-in-three. For the opening problem, the hike is mostly priced. If it arrives, forward SOFR moves little. If the Fed holds, front-end rates fall. A floating-rate borrower's real exposure is the path *after* this meeting, which the next several contracts and SOFR futures price. To bet on the meeting you need information the market lacks. Absent that, abstain (Drill D101).

**Reproduce:** `tests/test_ch05_examples.py::test_example_5_4`

#### Example 5.5 — Reading the curve: the forward rate and what it implies for a floating borrower

**Given.** One-year zero yield 3.80%; two-year zero yield 3.60% (annual compounding). Assume a term premium on the one-year-forward rate of 0.10%.

**Find.** The one-year rate one year forward, the implied expected one-year rate, and the cuts the curve implies relative to today's 3.80%.

**Solution.**
$$f_{1,2} = \frac{(1.036)^2}{1.038} - 1 = \frac{1.073296}{1.038} - 1 = 3.4004\%.$$
Expected one-year rate in a year $= 3.4004\% - 0.10\% = 3.3004\%$, which is about 50 bp below today's one-year yield.

**Check.** Rolling 3.80% for a year and then 3.4004% gives $(1.038)(1.034004) = 1.073296 = (1.036)^2$. ✓

**Decision consequence.** An inverted front end prices easing. A floating-rate borrower who underwrites today's SOFR for two years overstates expected interest by roughly the average of the implied cuts. A borrower who underwrites the implied cuts as certain understates the tail. The curve is a risk-neutral, term-premium-contaminated mean. Size the cap and the DSCR covenant to a path *above* the forward curve, because the scenario in which cuts do not arrive is often the one in which NOI is also under pressure from inflation-driven expenses.

**Reproduce:** `tests/test_ch05_examples.py::test_example_5_5`

#### Example 5.6 — Policy rate → SOFR → floating coupon → DSCR

**Given.** The opening problem's hotel: NOI \$2,400,000; floating loan \$30,000,000 interest-only at SOFR + 3.00%, actual/360. Two SOFR levels: 0.05% (near the start of the 2022 hiking cycle) and 5.30% (near the 2023 peak). These levels are rounded approximations of observed SOFR [VERIFIED-SECONDARY for the range: SOFR's first 2022 value was 0.05% and its 2023 high was 5.40%; ch05-S18]. Rate cap at 3.00% SOFR.

**Find.** Annual interest and DSCR at each SOFR level, unhedged and capped. Find the SOFR at which DSCR = 1.00x. Show the error from ignoring actual/360.

**Solution.**

| | SOFR 0.05% | SOFR 5.30% unhedged | SOFR 5.30% capped at 3.00% |
|---|---|---|---|
| All-in coupon | 3.05% | 8.30% | 6.00% (effective) |
| Interest $= L \cdot c \cdot 365/360$ | \$927,708 | \$2,524,583 | \$1,825,000 |
| DSCR $= 2{,}400{,}000/DS$ | 2.59x | 0.95x | 1.32x |

Break-even SOFR for DSCR = 1.00x: $2{,}400{,}000/(30{,}000{,}000 \times 365/360) - 0.03 = 4.8904\%$.

Day-count error at SOFR 5.30%: a 30/360 calculation gives \$2,490,000, understating interest by \$34,583 per year.

**Check.** \$2,524,583 / \$2,490,000 = 1.01389 = 365/360. ✓

**Decision consequence.** A 525 bp rise in SOFR took the hotel from 2.59x to below 1.0x unhedged. The cap is what kept it solvent, at 1.32x. The cap also expires. At extension, the lender requires a new cap priced at then-current forward rates and volatility, which can be a large cash outlay exactly when cash flow is weakest (Chapter 18). The floating channel is fast and mechanical. Every basis point reaches debt service at the next reset. Underwrite with the cap strike, the cap's expiry, and the replacement cost in the model, not just today's coupon.

**Reproduce:** `tests/test_ch05_examples.py::test_example_5_6`

#### Example 5.7 — 10-year Treasury → fixed coupon → loan constant → proceeds

**Given.** The same hotel's NOI (\$2,400,000) is refinanced fixed-rate on a 30-year amortization with constraints of 65% LTV, 1.25x DSCR, and 8.0% debt yield. Two environments [HYPOTHESIS, stylized on 2021 and 2023 levels]:

| | Low-rate | High-rate |
|---|---|---|
| 10-year Treasury | 1.50% | 4.50% |
| Lender spread | 1.75% | 2.00% |
| Coupon | 3.25% | 6.50% |
| Appraisal cap rate | 5.00% | 6.00% |

The existing loan balance at maturity is \$30,000,000 (interest-only). Refinancing costs are 1% of the existing balance.

**Find.** Loan constants, each constraint, the binding constraint, proceeds, and the refinance gap in the high-rate environment.

**Solution.**

Loan constants: $K(3.25\%) = 0.052225$; $K(6.50\%) = 0.075848$.

| Constraint | Low-rate | High-rate |
|---|---|---|
| Value $= NOI/c$ | \$48,000,000 | \$40,000,000 |
| LTV 65% | \$31,200,000 | \$26,000,000 |
| DSCR: $NOI/(1.25 K)$ | \$36,764,172 | \$25,313,731 |
| Debt yield: $NOI/0.08$ | \$30,000,000 | \$30,000,000 |
| **Maximum loan** | **\$30,000,000 (debt yield)** | **\$25,313,731 (DSCR)** |

DSCR capacity alone falls by $1 - 25{,}313{,}731/36{,}764{,}172 = 31.1\%$. Actual proceeds fall by 15.6%, because the binding constraint shifts from debt yield to DSCR.

Refinance gap $= 30{,}000{,}000 + 300{,}000 - 25{,}313{,}731 = \$4{,}986{,}269$.

The loan constant rises 45.2% ($0.075848/0.052225 - 1$). At the 6.50% coupon the elasticity of $K$ to the coupon is 0.676, so a further 10% proportional rise in the coupon would cut DSCR proceeds by about 6.8%.

**Check.** At the high-rate maximum loan, $DS = 25{,}313{,}731 \times 0.075848 = \$1{,}920{,}000$ and $DSCR = 2{,}400{,}000/1{,}920{,}000 = 1.25$x. ✓

**Decision consequence.** NOI never changed, yet the owner must bring about \$5.0 million of new equity, roughly 17% of the original loan, or sell, or negotiate an extension. That is the 2022–23 refinancing problem in a single line. Notice which constraint binds. When LTV or debt yield binds, a rate shock does not reduce proceeds immediately. It reduces them later through the appraisal. A model that sizes only on DSCR overstates the immediate effect. A model that sizes only on LTV at a stale appraisal understates the eventual effect.

**Reproduce:** `tests/test_ch05_examples.py::test_example_5_7`

#### Example 5.8 — QT, the term premium, and a cap rate

**Given.** 10-year Treasury yield 4.30%. A model estimate of the average expected short rate over ten years is 3.40% [HYPOTHESIS]. Suppose balance-sheet runoff and heavy issuance raise the term premium by 20 bp with expected short rates unchanged [HYPOTHESIS]. Hold a 10-year Treasury bought at par with a 4.30% coupon, \$100 face. An apartment cap rate of 6.00% moves by a pass-through fraction $\beta = 0.5$ of the 10-year move [HYPOTHESIS; Chapter 6 estimates and criticizes this parameter].

**Find.** (a) The implied term premium before and after. (b) DV01 per \$100 face and the price change. (c) The cap rate and the percentage value change for the apartment.

**Solution.**

(a) $TP = 4.30\% - 3.40\% = 0.90\%$ before and 1.10% after. The 10-year rises to 4.50%.

(b) DV01 (central difference) $= 0.08059$ per \$100 face. Duration estimate: $-0.08059 \times 20 = -1.612$. Full reprice at 4.50%: $-1.596$. Convexity makes up the 0.016 difference.

(c) Cap rate $= 6.00\% + 0.5 \times 0.20\% = 6.10\%$. Value change $= 6.00/6.10 - 1 = -1.64\%$.

**Check.** The duration estimate overstates the loss because of positive convexity, as expected. The cap-rate move of 10 bp on 6.00% is 1.67% to first order, and the exact figure is 1.64%.

**Decision consequence.** A term-premium shock reaches a bond immediately and a property only partly and slowly. Whether $\beta$ is 0.3 or 1.0 is the whole question, and the answer differs by property type, period, and financing conditions (Chapter 6). Do not attribute a yield move to QT without a decomposition. A term-premium rise and a rise in expected policy have different implications for floating-rate borrowers. The first leaves SOFR forwards unchanged. The second raises them.

**Reproduce:** `tests/test_ch05_examples.py::test_example_5_8`

---

### 5.6 CRE application: one policy shock, three channels, three clocks

Combine Examples 5.4–5.7 into a single map for a CRE book.

| Channel | Transmission | Clock | What to monitor | What to model |
|---|---|---|---|---|
| Floating debt | Policy → IORB/ON RRP/SRF → SOFR → coupon | Next reset (days to a month) | Fed funds and SOFR futures, cap strikes and expiries | DSCR path under forward curve + stress; cap replacement cost |
| Fixed debt | Policy expectations + term premium → 10-year → coupon → loan constant | At each rate lock (weeks to months) | 10-year, swap spreads, lender spreads | Proceeds under each constraint; refinance gap by maturity |
| Valuation | Real yields + risk premia → cap rates | Quarters to years; appraisals lag | Transaction cap rates, REIT-implied cap rates, bid-ask gap | Value under cap-rate scenarios; equity at risk |
| Availability | Policy → bank capital, deposits, funding → lending standards | Quarters | SLOOS, bank CRE loan growth, CMBS issuance, quotes per deal | Probability of no refinancing; extension economics |

Three practical rules follow.

1. **Map each loan to the curve point that sets its coupon.** Floating loans are front-end exposures. Fixed refinancings are 10-year exposures *at the lock date*. A borrower with both has a curve position, whether or not it chose one.
2. **Separate the rate shock from the availability shock.** A rate rise with open lending markets produces a refinance gap that equity can fill. A rate rise with closed lending markets produces forced sales. The second is where distressed opportunity appears (Chapter 12), and it is driven by bank balance sheets, not by the rate level alone.
3. **Expect private values to lag.** Liquid markets reprice the day of the news. Appraisals reprice over several quarters, and transaction volume falls while buyers and sellers disagree (Chapter 2, Case H). The lag is not evidence that CRE was insulated. It is evidence that CRE is priced infrequently.

---

### 5.7 When the relationships fail

1. **The policy rate rises and long yields fall.** If markets read the hike as raising recession odds, the 10-year can fall, and fixed-rate refinancing becomes cheaper while floating becomes dearer. The intuition "rates up, cap rates up" breaks down when the curve twists.
2. **Breakevens fall during a liquidity crisis.** TIPS are less liquid than nominals. In a scramble for cash, breakevens can collapse without any change in inflation expectations.
3. **Fed funds futures mislead around quarter-ends and regime changes.** EFFR–IORB spreads move when reserves approach scarcity. That shifts $\bar R$ without any policy change.
4. **Cap rates do not follow Treasuries.** In 2022, 10-year yields rose sharply while appraisal-based cap rates moved little for several quarters (§5.9). Spreads compress and widen with risk appetite, NOI growth expectations, and capital flows.
5. **The Taylor rule is silent on financial stability.** In March 2023 the FOMC raised rates while the Fed simultaneously opened an emergency lending facility (§5.9). No simple rule describes that combination.
6. **QT effects are not stable.** The same runoff pace can have small effects when reserves are abundant and large effects in money markets when reserves near scarcity. That is why runoff was slowed and then ended (§5.9).
7. **Availability can tighten without a rate move.** Bank failures, regulatory changes, or concentration limits can close lending to a property type even when the policy rate is unchanged.

---

### 5.8 Liquidity facilities: discount window, SRF, and the 2023 BTFP

| Facility | Borrower | Collateral and valuation | Rate | Term | Status |
|---|---|---|---|---|---|
| Primary credit (discount window) | Sound depository institutions | Broad collateral at lendable values (haircuts) | Primary credit rate, top of the range (4.00% at 16 Sep 2026) [FACT; ch05-S01] | Overnight to longer | Standing |
| Standing repo facility | Primary dealers, eligible banks | Treasuries, agency debt, agency MBS | SRF rate, top of the range (4.00% at 16 Sep 2026) [FACT; ch05-S01] | Overnight | Standing since 29 July 2021 [FACT; ch05-S09] |
| Bank Term Funding Program (BTFP) | Federally insured depository institutions and other eligible institutions | Treasuries, agency debt, agency MBS, and other qualifying assets **valued at par** | One-year OIS + 10 bp, fixed at advance [VERIFIED-SECONDARY; ch05-S08]; from 24 January 2024, not below IORB [FACT; ch05-S07] | Up to one year | Announced 12 March 2023; new loans ceased 11 March 2024 [FACT; ch05-S07, ch05-S08] |

**Why par valuation mattered.** A bank holding a Treasury bought at 100 that now trades at 85 could borrow 100 against it at the BTFP. At the discount window it could borrow only 85 minus a haircut. Par valuation removed the need to sell securities at a loss to meet deposit withdrawals. It addressed the specific vulnerability of 2023: unrealized losses created by the rate increases themselves [INFERENCE from the program design].

**CRE relevance.** Liquidity facilities stabilize banks' *funding*. They do not restore banks' *willingness to lend*. After March 2023, banks that had relied on emergency funding had strong reasons to shrink balance sheets and to raise CRE lending standards [INFERENCE; consistent with the SLOOS evidence in §5.9].

---

### 5.9 Historical episode: the 2022–23 tightening cycle and its CRE transmission

#### Date and environment

At the start of 2022 the federal funds target range was 0%–0.25%, and the Fed was still buying securities. SOFR's first published value of 2022 was 0.05% [VERIFIED-SECONDARY; ch05-S18]. Inflation was rising. The CPI-U for the 12 months to June 2022, released on 13 July 2022, rose 9.1%, the largest 12-month increase since the period ending November 1981 [FACT; BLS, ch05-S10]. In the same release, core CPI (excluding food and energy) rose 5.9% over 12 months [FACT; ch05-S10].

#### The policy path

| FOMC decision | Target range after decision | Move |
|---|---|---|
| 16 Mar 2022 | 0.25%–0.50% | +25 bp |
| 4 May 2022 | 0.75%–1.00% | +50 bp |
| 15 Jun 2022 | 1.50%–1.75% | +75 bp |
| 27 Jul 2022 | 2.25%–2.50% | +75 bp |
| 21 Sep 2022 | 3.00%–3.25% | +75 bp |
| 2 Nov 2022 | 3.75%–4.00% | +75 bp |
| 14 Dec 2022 | 4.25%–4.50% | +50 bp |
| 1 Feb 2023 | 4.50%–4.75% | +25 bp |
| 22 Mar 2023 | 4.75%–5.00% | +25 bp |
| 3 May 2023 | 5.00%–5.25% | +25 bp |
| 26 Jul 2023 | 5.25%–5.50% | +25 bp |

[FACT; FOMC statements, ch05-S04.] The cumulative increase was 525 bp in 16 months. The June 2022 move was the first 75 bp increase since 1994 [VERIFIED-SECONDARY; ch05-S04]. The range stayed at 5.25%–5.50% until 18 September 2024, when the FOMC cut it by 50 bp to 4.75%–5.00% [FACT; ch05-S12].

**Balance sheet.** On 4 May 2022 the FOMC announced runoff beginning 1 June 2022. The monthly caps were \$30 billion for Treasuries and \$17.5 billion for agency debt and MBS, rising after three months to \$60 billion and \$35 billion [FACT; ch05-S05]. From June 2024 the Treasury cap was reduced to \$25 billion [VERIFIED-SECONDARY; ch05-S06]. On 29 October 2025 the FOMC announced that runoff of its securities holdings would end on 1 December 2025 [VERIFIED-SECONDARY; ch05-S06].

**Long yields.** The 10-year Treasury yield briefly crossed 5% intraday on 19 October 2023, the first time since 2007, and settled at 4.98% that day [VERIFIED-SECONDARY, citing Treasury data; ch05-S17]. At the end of 2021 the 10-year had been near 1.5% [VERIFIED-SECONDARY for the approximate level; ch05-S17; exact year-end close *(verification pending)*].

#### The banking shock

Silicon Valley Bank failed on 10 March 2023. On 12 March 2023 the Fed announced the BTFP (§5.8) [FACT; ch05-S08]. Ten days later, on 22 March 2023, the FOMC raised rates by 25 bp. Its statement said the U.S. banking system was "sound and resilient" and that recent developments were "likely to result in tighter credit conditions for households and businesses" [FACT; ch05-S04].

#### CRE transmission: what the record shows

* **Lending standards.** In each of the Fed's Senior Loan Officer Opinion Surveys covering Q4 2022 through Q3 2023, major net shares of banks reported tightening standards for all categories of CRE loans, and weaker demand [FACT; ch05-S15].
* **Floating-rate borrowers.** SOFR's 2023 high was 5.40% [VERIFIED-SECONDARY; ch05-S18]. A floating loan at SOFR + 3.00% therefore moved from a coupon near 3.05% to one above 8.3%. Example 5.6 shows what that does to a hotel at constant NOI.
* **Fixed-rate refinancing.** Loans sized in 2021 at low coupons met 2023 loan constants roughly 45% higher (Example 5.7: 0.0522 to 0.0758) [INFERENCE from the arithmetic, using stylized inputs].
* **Prices.** Press coverage of Green Street's Commercial Property Price Index reported an all-property decline from its March 2022 peak on the order of 20% by 2023, with office and apartments falling more [VERIFIED-SECONDARY for the direction and peak month; exact magnitude and date *(verification pending)*; ch05-S16].

#### What was knowable at the time

| Date | Public information | What it implied for CRE |
|---|---|---|
| Early 2022 | Inflation high and rising; futures priced hikes; the FOMC signaled "ongoing increases" | Floating-rate cost would rise; caps were the immediate defense |
| Mid-2022 | 9.1% CPI print; 75 bp hikes; runoff announced | Fixed refinancings at maturity would face much higher constants |
| March 2023 | Bank failures; BTFP; FOMC expected tighter credit | Availability, not just price, would tighten |
| Late 2023 | 10-year near 5% | Refinance gaps at their widest for loans sized in 2020–21 |

What was **not** knowable: the size of the eventual peak (the market repeatedly underpriced the path in 2022), whether the bank stress would spread, and how long rates would stay high.

#### Interpretations

1. **Rate-driven repricing [INFERENCE].** CRE values fell because the discount rate and debt cost rose. Values recover when rates fall.
2. **Sector-driven repricing [INFERENCE].** Office faced a structural demand shock from remote work that coincided with higher rates. Rates revealed weakness rather than causing all of it.
3. **Availability-driven repricing [INFERENCE].** The tightening of bank lending after March 2023 cut the pool of buyers who could close, which depressed transaction prices beyond what rates alone imply.

The three are not exclusive. The data available here cannot apportion the decline among them.

#### What the episode establishes, and what it does not

It **establishes** that the floating channel transmits immediately and mechanically, that the fixed channel transmits at each maturity, and that availability can tighten sharply through the banking system. It does **not** establish a stable cap-rate beta to Treasuries, or that CRE prices fall by any particular amount for a given rate rise. Nor does it establish that the Fed will always pair hiking with liquidity support. The Volcker tightening of 1979–82 is a useful contrast: policy then targeted reserves rather than an interest rate, and short rates were far more volatile. Chapter 23 treats that episode with its own sources.

---

### 5.10 Decision exercise: the opening refinance

Return to §5.1. Use the futures inputs of Example 5.4, the loan terms of Examples 5.6 and 5.7, and today's 10-year at 4.50% after the 15 bp rise. Complete a decision record covering:

1. The market-implied probability of a hike and what it means for 18-month SOFR expectations.
2. Debt service and DSCR on (a) the floating extension at SOFR + 3.50% under the forward path and under a stress path 100 bp above it, and (b) the fixed refinance at today's 10-year. Show the binding constraint.
3. The refinance gap under the fixed option. State whether the owner can fund it and from what.
4. The cost and structure of the new cap for the extension, as a qualitative estimate if you do not have a cap quote. Name the inputs you need.
5. A recommendation: lock fixed now, extend floating, sell, or wait. Include what would change it.

**Rubric.**

| Criterion | Weight | Full credit |
|---|---|---|
| Probability correctly day-weighted and cross-checked | 15% | 68–69%, with the naive 32% identified as wrong |
| Floating DSCR under forward and stress paths | 20% | Uses actual/360, includes the cap, notes cap expiry and replacement |
| Fixed proceeds and binding constraint | 20% | Computes all three constraints; identifies the shift in the binding constraint |
| Refinance gap and funding source | 15% | Quantifies the gap; does not assume equity is free |
| Separates priced from unpriced information | 15% | States that a hike at a 68% implied probability is mostly priced; identifies the surprise scenario |
| Recommendation with invalidation criteria | 15% | Conditional on lender quotes and cap cost; names data that would reverse it |

There is no single correct answer. A recommendation to extend floating with a cap and pursue a sale is defensible if the cap is affordable. Locking fixed is defensible if the refinance gap can be funded and the owner wants certainty. Waiting for the meeting is defensible only if the option to lock survives the meeting.

---

### 5.11 Frequent analytical errors

1. **Reading fed funds futures without day-weighting.** It understates probabilities when the meeting is mid-month or late in the month.
2. **Treating implied probabilities as forecasts.** They are risk-neutral and include premia.
3. **Treating breakevens as expected inflation.** They include risk and liquidity premia and index to CPI, not PCE.
4. **Using the approximate Fisher relation at high rates.** The cross-term matters when nominal rates and inflation are both several percent.
5. **Ignoring actual/360 on floating loans.** It understates interest by 1.4%.
6. **Sizing proceeds on one constraint.** The binding constraint changes with rates and values.
7. **Assuming a stable cap-rate beta to the 10-year.** The pass-through varies by period and property type, and it lags.
8. **Equating a hike with higher long rates.** The curve can flatten or invert. Know which point sets your coupon.
9. **Confusing liquidity support with credit support.** The BTFP funded banks. It did not make them lend.
10. **Attributing every long-yield move to QT.** Decompose expected path versus term premium, and state the model.
11. **Using the Taylor rule as a point forecast.** Its band is wide because $r^*$ and the gap are uncertain.

---

### 5.12 Connections to other chapters

* Chapter 2: appraisal smoothing and why private prices lag liquid markets.
* Chapter 4: the data releases that move policy expectations, and surprise indices.
* Chapter 6: bond pricing, duration, DV01, and the cap-rate/Treasury spread in depth.
* Chapter 10: loan sizing, amortization, and refinancing gaps.
* Chapter 12: maturity walls and distressed CRE when availability closes.
* Chapter 14: equity index futures and their multipliers.
* Chapter 15: FX conventions and why the dollar rallies on hawkish surprises.
* Chapter 18: interest-rate caps for floating CRE debt and their replacement cost.
* Chapter 23: the Volcker disinflation and the 2022 episode in historical context.
* Case H: a single inflation surprise propagated through Treasuries, equity futures, FX, credit, and two CRE loans.

---

### 5.13 One-page reference sheet

**Administered rates at 16 Sep 2026** [FACT; ch05-S01]: range 3.75–4.00%; IORB 3.90%; ON RRP 3.75%; SRF 4.00%; primary credit 4.00%. Verify the current note before use.

| Item | Formula |
|---|---|
| Taylor (1993) | $i = r^* + \pi + 0.5(\pi - 2) + 0.5y$ |
| Balanced-approach | $i = r^* + \pi + 0.5(\pi - 2) + 1.0y$ |
| Inertial | $i_t = \rho i_{t-1} + (1-\rho) i^{rule}$ |
| Exact Fisher | $r = (1+i)/(1+\pi^e) - 1$ |
| Breakeven | $BEI = (1+y_{nom})/(1+r_{TIPS}) - 1$ |
| Fed funds futures | $F = 100 - \bar R$; \$41.67 per bp per contract |
| Post-meeting rate | $E[r_1] = (N\bar R - d\,r_0)/(N-d)$ |
| Hike probability | $p = (E[r_1] - r_0)/\Delta$ |
| Forward rate | $f_{1,2} = (1+y_2)^2/(1+y_1) - 1$ |
| Yield decomposition | $y_n \approx \text{avg } E[i] + TP_n$ |
| Floating debt service | $L(SOFR + s)(365/360)$ |
| Break-even SOFR at DSCR $D$ | $NOI/(D\,L\,365/360) - s$ |
| Loan constant | $K = 12 \cdot (c/12)/(1-(1+c/12)^{-n})$ |
| DSCR proceeds | $NOI/(D\,K)$ |
| Refinance gap | balance + costs − new loan |

**Checks before any rate-sensitive CRE decision.** Which curve point sets each coupon? What does the futures curve already price? Which loan constraint binds now, and which will bind after the next appraisal? Are lenders quoting at all?

---

### References for this chapter

All sources are listed with verification status in `references/sources_ch05.md` (for merger into `SOURCE_REGISTER.md`).

* Board of Governors of the Federal Reserve System. Implementation Note and FOMC statement, 16 September 2026; FOMC statement, 29 July 2026.
* Board of Governors of the Federal Reserve System. FOMC statements, 16 March 2022 through 26 July 2023; 18 September 2024.
* Board of Governors of the Federal Reserve System. "Plans for Reducing the Size of the Federal Reserve's Balance Sheet," 4 May 2022.
* Board of Governors of the Federal Reserve System. Press releases on the Bank Term Funding Program, 12 March 2023 and 24 January 2024.
* Board of Governors of the Federal Reserve System. "Policy Rules and How Policymakers Use Them."
* Board of Governors of the Federal Reserve System. Senior Loan Officer Opinion Surveys, January, April, July, and November 2023.
* Federal Open Market Committee. Statement on Longer-Run Goals and Monetary Policy Strategy (first adopted January 2012).
* Federal Open Market Committee. Statement regarding repurchase agreement arrangements, 28 July 2021.
* U.S. Bureau of Labor Statistics. Consumer Price Index — June 2022, released 13 July 2022.
* CME Group. 30-Day Federal Funds futures contract specifications; CBOT Rulebook Chapter 22.
* Taylor, J. B. (1993). "Discretion versus Policy Rules in Practice." *Carnegie-Rochester Conference Series on Public Policy* 39: 195–214.
* Federal Reserve Bank of St. Louis. "The FOMC Voting Rotation, Explained" (2022).


\newpage

## Chapter 6 — Fixed Income and the Cost of Capital

> **Status:** Complete (v1.0). Every number in the text, problems, and solutions is reproduced in `tests/test_ch06_examples.py`. Problems are in `problems/questions/ch06_problems.md` and solutions in `problems/solutions/ch06_solutions.md`. New library helpers are in `models/python/sdesk/x_rates.py`. Sources are in `references/sources_ch06.md`. Open verification items (flagged in the text as *(verification pending)*): the exact text of the 4 February 1994 FOMC statement, the dates and sizes of the March and August 1994 moves, and a recheck of the 2022 daily yield closes against FRED itself rather than a FRED-derived mirror.

### Learning objectives

After this chapter you should be able to:

1. Read Treasury quotes as a dealer does. Convert a bill's discount rate to its price, bond-equivalent yield, money-market yield, and effective annual yield. Convert a note's semiannual yield to an effective annual rate comparable with a monthly-pay mortgage. Read prices in 32nds and compute TIPS breakeven inflation.
2. Price a coupon bond and compute Macaulay duration, modified duration, convexity, and DV01, by formula, by HP-12C, in Excel, and in Python. Know when the duration approximation fails and by how much.
3. Construct and size a DV01-neutral curve trade. Name what it is exposed to (slope) and what it is not neutral to (convexity, financing, non-parallel moves at other tenors).
4. Derive forward rates from spot rates, decompose a long yield into expected short rates plus a term premium, and explain why the term premium is a model output, not an observation.
5. Compute carry and roll-down with worked numbers, and the yield rise that breaks even against them.
6. Decompose a credit spread into expected loss and premia, and size a spread-duration exposure.
7. Decompose the cap-rate/Treasury spread into a risk premium minus expected growth, and show with arithmetic why the spread is not a stable constant.
8. Compute the effective duration of a levered property's equity, and trace a rate rise through cap rates, loan constants, DSCR-sized proceeds, and refinancing.

---

### 6.1 Opening investment problem: one balance sheet, three rate exposures

You run the \$40 million discretionary account introduced in Chapter 1. On a Tuesday the investment committee asks one question about three proposals: *how much interest-rate risk are we taking, and are we paid for it?* All facts are [HYPOTHESIS].

**Proposal 1 — the Treasury note.** Buy \$20 million face of a new 5-year Treasury note at par with a 4.50% coupon. The 4-year point on the curve is 4.35%. A dealer will finance the position in repo at 4.00%. A junior analyst wants to lever it 5:1 "because it carries".

**Proposal 2 — the industrial building.** Buy a fully leased \$50 million distribution building at a 6.00% cap rate on \$3.0 million NOI after reserves. The lender offers a 65% LTV, 5-year fixed-rate loan at 6.00% on a 30-year amortization. The broker's memo says: "The cap rate is 160 bp over the 10-year Treasury. The long-run average spread is about 300 bp, so cap rates have room to *fall* relative to Treasuries." The 10-year Treasury yields 4.40%.

**Proposal 3 — the hedge.** A senior partner proposes shorting Treasury notes against the building "to lock in today's financing environment for the refinancing in year 5".

The three proposals look unrelated: a government bond, a warehouse, and a derivative overlay. They are one exposure in three forms. Each is a bet on the level and shape of the yield curve, on a spread to it, or on how a spread to it behaves when the curve moves. By the end of the chapter you will be able to state the DV01 of each, the break-even yield move for each, and what you would have to believe about cap-rate pass-through for the hedge in Proposal 3 to reduce risk rather than add a second speculation. Section 6.10 returns to the decision.

---

### 6.2 Economic intuition

#### Yields are the price of time, and every asset is priced against them

A Treasury yield is the rate at which the market exchanges dollars today for dollars that the U.S. government promises to pay later. It contains no credit risk in the ordinary sense and very little liquidity risk at the benchmark tenors. It therefore serves as the base rate to which every other asset's required return is added. A cap rate, a mortgage coupon, an equity earnings yield and a hotel's discount rate all embed a Treasury yield plus compensation for other risks, minus expected growth where the cash flows grow.

This is the sense in which Treasury yields are the "cost of capital". They are not the cost of *your* capital. They are the opportunity cost against which your capital's use must be justified. When the 10-year yield rises 100 bp, a 6.00% cap rate does not automatically become 7.00%, but the hurdle a 6.00% income stream must clear has risen. Something must adjust: the cap rate, the growth forecast, the risk premium the buyer accepts, or the number of buyers.

#### Duration is the time-weighted exposure to the discount rate

A bond's price is the present value of its cash flows. When the discount rate rises, distant cash flows lose more value than near ones because they are discounted over more periods. **Duration** measures the average time to the cash flows, weighted by their present values. It is also, after a small adjustment, the percentage price change per unit change in yield. A 10-year coupon note has a duration of about 8 years: a 1 percentage point rise in its yield costs about 8% of its price.

The same logic applies to any long-lived cash-flow stream. A stabilized property is a perpetuity-like claim. If its cap rate moves one-for-one with Treasuries, its effective duration to Treasury yields is $1/c$. At a 6% cap that is about 17 years, twice the duration of a 10-year note. If the cap rate moves only 0.6 for 1, the duration is 10. Either way, a stabilized property is a long-duration asset. Leverage then divides the equity's share of the capital structure into that duration: at 65% LTV, a property duration of 10 becomes an equity duration near 29 if the debt is floating. **The levered owner of a low-cap-rate building can hold more interest-rate risk per dollar than a holder of 30-year Treasury bonds.** Section 6.5.9 derives this and Example 6.9 computes it.

#### Convexity: the curvature that helps the long and hurts the short

The price–yield curve of a non-callable bond is convex. Prices rise more when yields fall than they fall when yields rise by the same amount. Duration describes the tangent line. Convexity describes the bend. For small moves the bend is negligible. For the 200–300 bp moves of 1994 and 2022 it is several points of price. A position that is short convexity, such as a mortgage lender's book of prepayable loans, a short position in long bonds, or a DV01-neutral steepener that is short the longer, more convex leg, loses slightly on large moves in either direction.

#### The yield curve: expectations plus a premium

The curve's slope reflects two things that cannot be observed separately: the expected path of short-term policy rates, and the extra compensation investors demand for locking money up at a fixed rate for longer, the **term premium**. A steep curve can mean the market expects the central bank to raise rates, or it can mean investors demand a large premium for duration risk, or both. An inverted curve usually means the market expects cuts. Chapter 5 develops the policy-expectations side. This chapter treats the premium and shows why every published estimate of it is a model output that can differ across models by enough to change a trading conclusion.

#### Carry and roll-down: what you earn if nothing happens

A bond position earns its coupon and pays its financing. That difference is **carry**. If the curve is upward-sloping and does not move, a bond also "rolls down" the curve: as it ages, it is priced at the lower yield of a shorter maturity, and its price rises. Carry plus roll-down is the return to a bet that *nothing changes*. It is a real source of return. It is also the payment for a short option on curve moves: the larger the carry and roll, the larger the yield rise it can absorb, but there is always a rise that takes it away.

#### Cap rates are real-asset yields with growth

A Treasury pays a fixed nominal coupon. A building pays NOI that is expected to grow, sometimes with inflation, and is risky. The Gordon relation $c = k - g$, with $k = r_f + RP$, gives

$$c - r_f = RP - g.$$

The cap-rate/Treasury spread is a risk premium *minus* expected growth. It has no reason to be constant. When Treasury yields rise because inflation expectations rose, and NOI growth expectations rise with them, the spread should narrow. When Treasuries rise because real rates rose, the spread should be unchanged and cap rates should rise with them. When credit tightens, the risk premium rises and the spread widens even if Treasuries fall. A broker's "long-run average spread" is an average across regimes with different growth expectations, different risk premia, and different financing conditions. It is not an anchor.

#### How a rate shock reaches levered real estate

The chain has four links, each with its own timing:

1. **Valuation.** Higher Treasury yields raise required returns. Cap rates move by some pass-through $\beta$, which is unknown in advance and unstable.
2. **Debt service.** For floating-rate loans, interest cost rises immediately. For fixed-rate loans nothing happens until maturity.
3. **Loan sizing.** At refinancing, a higher rate raises the loan constant $K$. A lender who sizes to a minimum DSCR lends $NOI/(DSCR \cdot K)$, so proceeds fall in proportion to the rise in $K$, and the property value used for the LTV test falls with the cap rate.
4. **Refinancing gap.** The outstanding balance does not fall with the new loan amount. The difference is equity that the owner must contribute, or a default.

The first link is a mark-to-market loss that may or may not be realized. The fourth is a cash demand on a fixed date. A speculator must know which one threatens survival. It is almost always the fourth.

---

### 6.3 The Treasury market: instruments, auctions, and quoting conventions

#### Instruments

| Security | Maturities at issue | Coupon | Quoted as | Notes |
|---|---|---|---|---|
| Bills | Up to one year (several weekly and monthly cycles) | None; sold at a discount | Discount rate (actual/360, face in denominator); also shown as investment rate (BEY) | Price = $100(1 - d \cdot \text{days}/360)$ |
| Notes | 2, 3, 5, 7, 10 years | Fixed, paid semiannually | Price in 32nds of a point; yield as semiannual bond-equivalent | The 2-, 5- and 10-year are the main benchmarks |
| Bonds | 20, 30 years | Fixed, semiannual | As notes | Highest duration and convexity |
| TIPS | 5, 10, 30 years | Fixed real coupon on CPI-indexed principal | Real yield; price in 32nds | Principal adjusts with CPI-U; at maturity the holder receives the greater of adjusted or original principal |
| FRNs | 2 years | Floating, indexed to the 13-week bill | Discount margin | Near-zero duration |

[FACT: the maturity menu and the single-price auction format are described by the Treasury (TreasuryDirect auction FAQs; 31 CFR Part 356, the Uniform Offering Circular), ch06-S14, ch06-S15, VERIFIED-SECONDARY. The menu changes with Treasury's borrowing needs; check TreasuryDirect before relying on any particular tenor.]

#### Auctions

Treasury sells marketable securities in **single-price auctions**. Competitive bidders submit yields (or discount rates for bills). Treasury accepts bids from the lowest yield upward until the offering is filled. Every successful bidder, competitive and noncompetitive, is awarded securities at the **highest accepted yield**, the "stop-out" [FACT; ch06-S14]. Desk vocabulary follows from this:

* **Tail**: the stop-out yield minus the "when-issued" yield trading just before the auction deadline. A positive tail (stop-out above when-issued) means demand was weaker than the market expected.
* **Bid-to-cover**: total bids divided by the amount sold. A ratio is informative only relative to recent auctions of the same tenor.
* **Indirect / direct / dealer takedown**: the shares awarded to bidders through primary dealers on behalf of others (often foreign official and other institutional accounts), to direct bidders, and to primary dealers themselves. Primary dealers are expected to bid in every auction. A large dealer takedown means end-investors bought less and dealers must distribute the balance.

None of these statistics predicts yields by itself. A tail in a 10-year auction on a day of heavy corporate issuance tells you something different from the same tail on a quiet day. Treat auction results as one input to market interpretation (Chapter 4's surprise logic applies: what matters is the result relative to what was priced).

#### Quoting conventions and why they matter for comparisons

Four conventions coexist on the same desk, and mixing them is one of the most common errors in comparing yields across instruments.

1. **Bank-discount rate (bills).** $d = \dfrac{F - P}{F}\cdot\dfrac{360}{\text{days}}$. It uses face value, not price, in the denominator and a 360-day year. It always *understates* the investment return.
2. **Bond-equivalent yield, BEY (notes, bonds, and bills shown as "investment rate").** For coupon securities, the semiannual yield to maturity times two. For bills of 182 days or less, $\text{BEY} = \dfrac{F-P}{P}\cdot\dfrac{365}{\text{days}}$. For longer bills the Treasury uses a quadratic that credits a hypothetical semiannual coupon (equation 6.3 below).
3. **Money-market yield.** $\dfrac{F-P}{P}\cdot\dfrac{360}{\text{days}}$, used to compare bills with instruments quoted on actual/360, such as repo and SOFR-indexed loans.
4. **Effective annual yield.** $(F/P)^{365/\text{days}} - 1$ for a bill; $(1 + y/2)^2 - 1$ for a semiannual coupon yield; $(1 + r/12)^{12} - 1$ for a monthly-pay mortgage rate.

A 4.50% Treasury yield and a 4.50% mortgage rate are not the same rate. The Treasury yield is a semiannual BEY, equivalent to 4.5506% effective. The mortgage rate compounds monthly. At 6.50%, a mortgage rate is 6.6972% effective (Example 6.1). Comparisons of "loan spread over Treasuries" are made in quoted terms by convention, which is acceptable if everyone knows the compounding differs.

**Prices in 32nds.** Notes and bonds are quoted in points and 32nds of a point. "98-17" means $98 + 17/32 = 98.53125$. A "+" adds half a 32nd: "98-17+" $= 98 + 17.5/32 = 98.546875$. A third digit gives eighths of a 32nd: "98-172" $= 98 + 17.25/32 = 98.5390625$. One 32nd on \$10 million face is \$3,125.

**Clean and dirty prices.** Quoted prices are **clean**: they exclude accrued interest. The buyer pays the dirty price, clean plus accrued interest since the last coupon. All examples in this chapter price on a coupon date, where the two coincide. Chapter 17 and Appendix C give the accrual formulas and Excel's `ACCRINT`.

#### TIPS and breakeven inflation

A TIPS pays a fixed real coupon on principal indexed to CPI-U. Its yield is a real yield. The **breakeven inflation rate** is the inflation rate at which a nominal note and a TIPS of the same maturity deliver the same return:

$$1 + y_{nom} = (1 + y_{real})(1 + \pi_{BE}) \;\Rightarrow\; \pi_{BE} = \frac{1+y_{nom}}{1+y_{real}} - 1 \approx y_{nom} - y_{real}.$$

Breakeven is **not** expected inflation. It contains an inflation risk premium, which raises it, and a TIPS liquidity premium, which lowers it because TIPS trade less actively than nominal notes. The relative size of these premia varies over time and is itself model-dependent [INFERENCE from the structure of the instruments; see Chapter 5 for survey-based inflation expectations]. For a CRE investor the TIPS real yield is the cleanest available market measure of the real risk-free rate, which is the right comparison for a property whose NOI grows with inflation (Section 6.5.8).

---

### 6.4 Technical definitions

| Term | Definition |
|---|---|
| Yield to maturity (YTM), $y$ | The single rate that discounts a bond's promised cash flows to its price, quoted as an annual rate with the instrument's compounding (semiannual for Treasuries) |
| Bank-discount rate, $d$ | $(F-P)/F \times 360/\text{days}$; the bill quoting convention |
| Bond-equivalent yield (BEY) | Semiannual YTM × 2 for coupon bonds; the "investment rate" for bills |
| Effective annual yield | The rate compounded once a year that gives the same growth: $(1+y/m)^m - 1$ |
| Macaulay duration, $D_{mac}$ | PV-weighted average time to cash flows, in years |
| Modified duration, $D_{mod}$ | $D_{mac}/(1+y/m)$; $-\frac{1}{P}\frac{dP}{dy}$ |
| Effective duration | $-\dfrac{P(y+\Delta) - P(y-\Delta)}{2P\Delta}$; defined for any instrument by revaluation, including those whose cash flows change with rates |
| Convexity, $C$ | $\frac{1}{P}\frac{d^2P}{dy^2}$, in years² |
| DV01 (PV01, PVBP) | Dollar price change for a 1 bp fall in yield: $P \cdot D_{mod} \cdot 0.0001$ per unit of price |
| Spot (zero) rate, $s_t$ | Yield on a zero-coupon claim paying at $t$ |
| Forward rate, $f_{t_1,t_2}$ | The rate between $t_1$ and $t_2$ locked in today by the spot curve |
| Term premium | Yield on a long bond minus the yield implied by the *expected* path of short rates; not directly observable |
| Carry | Coupon income minus financing cost over a horizon |
| Roll-down | Price change from a bond being repriced at the curve's yield for its shorter remaining maturity, curve unchanged |
| Steepener / flattener | A position that gains when the long-minus-short yield spread widens / narrows |
| Bull / bear move | Yields fall / rise. "Bear flattener": yields rise, short end more |
| Credit spread | Yield on a risky bond minus the Treasury yield of matching maturity (or a swap rate) |
| Spread duration | Percentage price change per unit change in the credit spread, Treasury yield held fixed |
| Cap-rate spread | Cap rate minus the 10-year Treasury yield, by market convention |
| Pass-through, $\beta$ | Change in cap rate per unit change in Treasury yield over a stated horizon; an empirical, unstable quantity |
| Loan constant, $K$ | Annual debt service per \$1 of loan |
| Refinancing gap | Outstanding balance plus costs minus the new maximum loan |

---

### 6.5 Equations and derivations

#### 6.5.1 Bond price

For a bond with face $F$, annual coupon rate $c$, $m$ payments per year, $n = mT$ periods, and yield $y$ (periodic rate $y/m$):

$$P = \sum_{k=1}^{n} \frac{cF/m}{(1+y/m)^k} + \frac{F}{(1+y/m)^n} = \frac{cF}{m}\cdot\frac{1-(1+y/m)^{-n}}{y/m} + F(1+y/m)^{-n}. \tag{6.1}$$

When $y = c$ the price is par. When $y > c$ the bond trades at a discount and accretes toward par as it ages (pull to par).

#### 6.5.2 Bills

$$P = F\left(1 - d\cdot\frac{\text{days}}{360}\right), \qquad \text{BEY}_{\le 182} = \frac{F-P}{P}\cdot\frac{365}{\text{days}}. \tag{6.2}$$

For bills longer than 182 days, set $t = \text{days}/365$. The Treasury's BEY solves $P\left(1 + \frac{y}{2}\right)\left(1 + \left(t - \tfrac{1}{2}\right)y\right) = F$, a quadratic in $y$:

$$y = \frac{-2t + 2\sqrt{t^2 - (2t-1)(1 - F/P)}}{2t - 1}. \tag{6.3}$$

The construction assumes a coupon paid at six months and reinvested at the same yield for the remaining $t - \frac12$ years. It makes long bills comparable with semiannual notes.

#### 6.5.3 Duration

Differentiate (6.1) with respect to $y$. Write $v = 1 + y/m$ and $CF_k$ for the cash flow at period $k$, which occurs at time $t_k = k/m$:

$$\frac{dP}{dy} = \sum_k CF_k \cdot (-k)\, v^{-k-1} \cdot \frac{1}{m} = -\frac{1}{v}\sum_k t_k \, CF_k\, v^{-k}.$$

Divide by $-P$:

$$-\frac{1}{P}\frac{dP}{dy} = \frac{1}{1+y/m}\underbrace{\sum_k t_k \frac{CF_k v^{-k}}{P}}_{D_{mac}} = D_{mod}. \tag{6.4}$$

Macaulay duration is a weighted average of payment times with present-value weights that sum to one. Modified duration is the price sensitivity. The two differ by the factor $1 + y/m$. For a zero-coupon bond $D_{mac} = T$.

**DV01** is the dollar price change for a 1 bp move:

$$DV01 = P \cdot D_{mod} \cdot 0.0001. \tag{6.5}$$

The library computes DV01 by a central finite difference, which is an independent route and agrees with (6.5) to seven significant figures (Example 6.2's check).

#### 6.5.4 Convexity and the second-order approximation

A Taylor expansion of $P(y)$ to second order gives

$$\frac{\Delta P}{P} \approx -D_{mod}\,\Delta y + \frac{1}{2} C\,(\Delta y)^2, \qquad C = \frac{1}{P}\frac{d^2P}{dy^2} = \frac{1}{P\,m^2}\sum_k \frac{k(k+1)\,CF_k}{(1+y/m)^{k+2}}. \tag{6.6}$$

The convexity term is always positive for an option-free bond. It is small for small moves and grows with the square of the move. At 300 bp it is worth several points on a 10-year note (Example 6.2). The error that remains after the convexity term comes from third and higher derivatives. It is negative for rises and positive for falls, so the second-order approximation slightly understates losses and overstates gains.

#### 6.5.5 Forward rates and the expectations hypothesis

With annually compounded spot rates $s_1, s_2, \ldots$, no-arbitrage requires that investing for $t_2$ years equal investing for $t_1$ years and rolling at the forward rate:

$$(1 + s_{t_2})^{t_2} = (1+s_{t_1})^{t_1}(1 + f_{t_1,t_2})^{t_2 - t_1} \;\Rightarrow\; f_{t_1,t_2} = \left[\frac{(1+s_{t_2})^{t_2}}{(1+s_{t_1})^{t_1}}\right]^{1/(t_2-t_1)} - 1. \tag{6.7}$$

A forward rate is a rate you can **lock in** today by trading spot instruments. Under the *pure expectations hypothesis* forwards equal expected future spot rates. Empirically they do not. Forwards have, on average, overstated subsequent short rates over long samples, which is the evidence for a positive average term premium [INFERENCE supported by the literature summarized in ch06-S12 and ch06-S13; not a law, and the sign has varied]. A forward is therefore the market's expected rate *plus* a premium. When you hedge a future borrowing by locking the forward, you pay that premium as insurance.

#### 6.5.6 Term premium

Let $y_n$ be the $n$-year zero yield and $E_t[r_{t+i}]$ the expected one-year rate in year $i+1$. Define

$$y_n = \underbrace{\left[\prod_{i=0}^{n-1}\big(1 + E_t[r_{t+i}]\big)\right]^{1/n} - 1}_{\text{expectations component}} + TP_n. \tag{6.8}$$

The decomposition is an identity only once you supply the expected path. The path is not observed. It must come from a model or a survey, so $TP_n$ inherits the model's assumptions. Two widely used estimates illustrate the point:

* The **ACM** model (Adrian, Crump and Moench, 2013, *Journal of Financial Economics* 110(1): 110–138) estimates an affine term-structure model by a sequence of linear regressions on principal components of yields. The New York Fed publishes daily and monthly estimates of term premia from it [FACT; ch06-S12, VERIFIED-SECONDARY].
* The **Kim–Wright** model (Kim and Wright, 2005, Federal Reserve FEDS working paper 2005-33) is a three-factor arbitrage-free model fitted to Treasury yields and, in a variant, to survey forecasts of short rates. Its authors attributed much of the 2004–05 decline in long-term yields and distant forwards to lower term premia [FACT; ch06-S13, VERIFIED-SECONDARY]. The Federal Reserve Board publishes estimates from it.

**Estimation caveats.** (1) The two models can disagree in level and sometimes in direction over short windows, because one leans on yields alone and the other on yields plus surveys. (2) Affine models assume the market price of risk is a linear function of a few factors. A regime change in policy reaction or inflation dynamics violates that. (3) Estimates are revised as the sample grows. A term premium "at a 10-year high" in today's vintage may not be at a high in next year's vintage. (4) The term premium is not tradable separately from expectations. A trader who is "long term premium" is long duration and must be right about the expected path as well. Treat published term-premium estimates as model-conditional diagnostics, never as observations. This book cites a specific estimate only with its model, vintage and date. Example 6.6 shows why.

#### 6.5.7 Carry and roll-down

Over a horizon $h$, a bond bought at $P_0$ (yield $y_0$, maturity $T$) and financed in repo at rate $r_{repo}$ earns, if the curve does not move:

$$\text{Total} = \underbrace{cFh - P_0 r_{repo}h}_{\text{carry}} + \underbrace{\big[P(y_0, T-h) - P_0\big]}_{\text{pull to par}} + \underbrace{\big[P(y_{T-h}, T-h) - P(y_0, T-h)\big]}_{\text{roll-down}}. \tag{6.9}$$

Here $y_{T-h}$ is today's curve yield at the shorter maturity. Coupons are not reinvested, and financing is simple interest, which is the desk approximation. The **breakeven yield rise** is

$$\Delta y^{*} \approx \frac{\text{Total}}{DV01_h}\ \text{bp}, \tag{6.10}$$

where $DV01_h$ is the bond's DV01 at the horizon. A larger carry-and-roll gives more protection, but protection only against a yield rise smaller than $\Delta y^*$. Carry is income for selling a cushion, not a free return.

#### 6.5.8 Credit spreads

A defaultable bond's spread $s$ over Treasuries compensates for expected default loss, the risk of that loss (default and spread risk premia), and lower liquidity. Under a constant risk-neutral default intensity $\lambda$ and recovery rate $R$, the **credit triangle** gives

$$s \approx \lambda (1 - R) \;\Rightarrow\; \lambda = \frac{s}{1-R}. \tag{6.11}$$

The $\lambda$ backed out this way is a *risk-neutral* intensity. It includes premia. Real-world default rates are lower, sometimes much lower, so the spread is mostly premium in high-grade credit and mostly expected loss in distressed credit (Chapter 17). The price sensitivity to the spread is the **spread duration**, which for a fixed-rate bond equals its modified duration to the total yield. A CRE mortgage coupon is a Treasury or swap rate plus a credit spread. Its two components move separately, and in stress they often move in opposite directions: Treasuries rally while spreads widen.

#### 6.5.9 Cap rates against Treasury yields

For NOI after reserves growing at a constant expected rate $g$, with required unlevered return $k = r_f + RP$:

$$c = r_f + RP - g, \qquad c - r_f = RP - g. \tag{6.12}$$

Take differentials:

$$\Delta c = \Delta r_f + \Delta RP - \Delta g.$$

The cap rate moves one-for-one with Treasuries only if $\Delta RP = \Delta g = 0$. Three regimes follow:

| Driver of the Treasury move | $\Delta g$ | $\Delta RP$ | Cap-rate pass-through | Spread |
|---|---|---|---|---|
| Real-rate rise (tighter policy, higher real yields) | ≈ 0 | ≈ 0, or up if credit tightens | ≈ 1 or more | Constant or wider |
| Inflation expectations rise, NOI indexed or marked to market | > 0 | ≈ 0 | < 1 | Narrower |
| Flight to quality (Treasuries rally in a crisis) | < 0 | > 0 | Negative: cap rates rise as Treasuries fall | Much wider |

The convention of quoting the spread over the *nominal* 10-year Treasury mixes a real asset with a nominal benchmark. Comparing the cap rate with the 10-year **TIPS** real yield removes the inflation component of $r_f$ but not the growth term. The spread over TIPS is $RP - g_{real}$, which is a cleaner object, though still not constant.

#### 6.5.10 Effective duration of levered property equity

Value $V = NOI/c$ with $c = c_0 + \beta\,\Delta r_f$ and NOI fixed. Then

$$\frac{dV}{V} = -\frac{dc}{c} = -\frac{\beta}{c}\,dr_f \;\Rightarrow\; D_V = \frac{\beta}{c}. \tag{6.13}$$

The equity is the residual $E = V - D$, where $D$ here denotes the market value of the debt with duration $D_{debt}$ (zero for floating-rate debt, positive for fixed). The balance-sheet duration identity $E\,D_E = V D_V - D\,D_{debt}$ gives, with $\lambda = D/V$:

$$D_E = \frac{D_V - \lambda D_{debt}}{1 - \lambda}. \tag{6.14}$$

Two readings matter. The **book** equity duration treats the debt at par, $D_{debt} = 0$. That is what a sale or a refinancing sees, because the borrower repays par, or par plus a prepayment premium. The **economic** equity duration marks a fixed-rate loan to market. A below-market fixed-rate loan is an asset to the borrower, but one that can be realized only by holding to maturity or by an assumption by a buyer. Most fixed-rate CRE loans carry yield maintenance or defeasance, which prevents the borrower from buying the loan back at its lower market value.

#### 6.5.11 Loan sizing and the refinancing gap

For a loan amortizing monthly at nominal rate $r$ over $N$ years, the loan constant is

$$K(r) = 12\cdot\frac{r/12}{1 - (1 + r/12)^{-12N}}. \tag{6.15}$$

A DSCR-constrained lender lends $L_{DSCR} = NOI/(DSCR_{min}\cdot K)$. The LTV-constrained amount is $\lambda_{max}\cdot NOI/c$, and the debt-yield-constrained amount is $NOI/DY_{min}$. The new loan is the minimum of the three. Since $\partial \ln L_{DSCR}/\partial r = -\partial \ln K/\partial r$, DSCR-sized proceeds have their own "duration" to the loan rate, close to 10 for a 30-year amortization at a 7–8% rate (Section 6.7). The refinancing gap is $B_T + \text{costs} - L_{new}$. The **debt-yield test is the only one of the three that does not depend on rates.** That is why lenders added it after 2008, and why it binds when rates are low.

---

### 6.6 Worked examples

All examples are reproduced in `tests/test_ch06_examples.py`. Inputs are [HYPOTHESIS] unless cited.

#### Example 6.1 — Four yields for one bill, and why a 4.50% note is not a 4.50% mortgage

**Given.** (a) A 26-week (182-day) bill quoted at a 5.00% discount rate. (b) A 52-week (364-day) bill quoted at a 4.80% discount rate. (c) A 10-year note yielding 4.30% and a 10-year TIPS yielding 1.95% real. (d) A Treasury note yielding 4.50% (semiannual BEY) and a mortgage at 6.50% (monthly pay). (e) A note quoted at 98-17+ and another at 98-172.

**Find.** Prices, BEY, money-market yield, and effective annual yield for (a) and (b); breakeven inflation for (c); effective annual rates for (d); decimal prices for (e).

**Solution.**

(a) Price $= 100(1 - 0.05 \times 182/360) = 100(1 - 0.025278) = 97.4722$.

* BEY $= (100 - 97.4722)/97.4722 \times 365/182 = 0.025934 \times 2.00549 = 5.2009\%$.
* Money-market yield $= 0.025934 \times 360/182 = 5.1297\%$.
* Effective annual $= (100/97.4722)^{365/182} - 1 = 5.2687\%$.

The quoted discount rate of 5.00% understates the bond-equivalent return by 20 bp.

(b) Price $= 100(1 - 0.048 \times 364/360) = 95.1467$. With $t = 364/365 = 0.99726$, equation (6.3) gives BEY $= 5.0513\%$. The naive simple-interest formula $(F-P)/P \times 365/364$ would give 5.1149%, which is close to the effective annual yield of 5.1153%. The quadratic BEY is lower because it is a semiannually compounded rate. Converting it gives $(1 + 0.050513/2)^2 - 1 = 5.1151\%$, which matches the effective annual yield to within the 364/365-day difference.

(c) Breakeven inflation, approximate: $4.30\% - 1.95\% = 2.35\%$. Exact: $1.0430/1.0195 - 1 = 2.305\%$. The 4.5 bp difference is small at these levels and grows with the level of rates.

(d) Note: $(1 + 0.045/2)^2 - 1 = 4.5506\%$. Mortgage: $(1 + 0.065/12)^{12} - 1 = 6.6972\%$.

(e) $98 + 17.5/32 = 98.546875$; $98 + 17.25/32 = 98.5390625$.

**Check.** Excel: `=TBILLPRICE(settle, settle+182, 5%)` returns 97.4722, `=TBILLEQ(settle, settle+182, 5%)` returns 5.2009%. Python: `x_rates.bill_bey`, `x_rates.bill_effective_annual`.

**Decision consequence.** When the account compares a bill with a SOFR-indexed money fund, use the money-market yield. When it compares a bill with a note, use BEY. When it compares any of them with a mortgage or a property IRR, convert all of them to effective annual rates. The 20 bp gap between the bill's discount rate and its BEY is larger than many of the spreads a desk trades. A memo that says "the bill yields 5.00%" has already made an error in the first sentence.

#### Example 6.2 — The 10-year note: price, duration, convexity, DV01, and the large-move error

**Given.** A 10-year Treasury note, 4.00% coupon, semiannual, priced on a coupon date at a 4.50% yield. Position: \$10 million face.

**Find.** Price; Macaulay and modified duration; convexity; DV01 per 100 and for the position; the price change for ±100 bp and ±300 bp by duration alone, by duration plus convexity, and by full repricing.

**Solution.** From (6.1) with $c/2 = 2.00$, $y/2 = 0.0225$, $n = 20$:

$$P = 2.00 \times \frac{1 - 1.0225^{-20}}{0.0225} + 100 \times 1.0225^{-20} = 96.0091.$$

From (6.4): $D_{mac} = 8.2978$ years; $D_{mod} = 8.2978/1.0225 = 8.1152$. From (6.6): $C = 78.005$.

DV01 $= 96.0091 \times 8.1152 \times 0.0001 = 0.077913$ per 100 face. For \$10 million face: $0.077913/100 \times 10{,}000{,}000 = \$7{,}791$ per bp.

| Shock | Duration term (points) | Convexity term | Duration + convexity | Exact repricing | Exact % |
|---|---|---|---|---|---|
| +100 bp | −7.7913 | +0.3745 | −7.4169 | −7.4295 | −7.74% |
| −100 bp | +7.7913 | +0.3745 | +8.1658 | +8.1791 | +8.52% |
| +300 bp | −23.3740 | +3.3701 | −20.0039 | −20.3274 | −21.17% |
| −300 bp | +23.3740 | +3.3701 | +26.7441 | +27.1260 | +28.25% |

For the position, the exact loss at +100 bp is $7.4295/100 \times \$10{,}000{,}000 = \$742{,}951$.

**Check.** DV01 by central difference, $[P(4.49\%) - P(4.51\%)]/2$, equals $P \cdot D_{mod} \cdot 0.0001$ to within $2 \times 10^{-8}$; the residual is the finite-difference error. The asymmetry of the exact column (−7.74% versus +8.52%) is convexity.

**Decision consequence.** For daily risk, DV01 is enough: the duration-only error at 100 bp is 0.36 points, about 5% of the move. For stress tests at 300 bp, the 1994 and 2022 scale, duration alone overstates the loss by 3.0 points (23.37 versus 20.33) and understates the gain by 3.8 points. Convexity removes most of that error, leaving 0.32 points on the loss side. **Stress tests must reprice, not multiply.** A committee shown "DV01 × 300" for a 10-year position overstates the downside and understates the upside, and if the position is short, it understates the downside.

#### Example 6.3 — The 1987 desk exercise: a financial calculator and a sheet of graph paper

*The setting.* It is a morning in 1987. There is no spreadsheet on the desk, only an HP-12C and a pad of graph paper. You must price a 10-year, 9.00% semiannual-coupon note at a 10.00% yield, find its duration and DV01 without a duration formula, and draw the price–yield curve to show a client why the bond's losses slow as yields rise. All numbers are [HYPOTHESIS]; the coupon and yield are chosen to be typical of the period's double-digit-yield environment, not to quote any specific issue.

**Step 1 — price on the HP-12C with TVM keys.** Semiannual periods: $n = 20$, $i = 5$, PMT $= 4.5$, FV $= 100$.

```
f CLEAR FIN
20 n
5 i
4.5 PMT
100 FV
PV            → -93.77        (price 93.7689 per 100)
```

The negative sign is the HP-12C cash-flow convention: you pay the price.

**Step 2 — price with the HP-12C bond functions** (settlement 15 January 1987, maturity 15 January 1997, a coupon date, so no accrued interest):

```
f CLEAR FIN
g M.DY
10 i          (annual yield, percent)
9 PMT         (annual coupon rate, percent)
1.151987 ENTER
1.151997
f PRICE       → 93.77         (x<>y shows accrued interest: 0.00)
```

To reverse: key `93.7689 PV`, re-enter the two dates, and press `f YTM` → 10.00.

**Step 3 — DV01 and duration by bumping.** Return to the TVM registers and change only `i`:

```
5.05 i   PV   → -93.17        (yield 10.10%: 93.1747)
4.95 i   PV   → -94.37        (yield  9.90%: 94.3682)
```

$DV01 = (94.3682 - 93.1747)/(2 \times 10) = 0.05967$ per 100 per bp. Effective duration $= (94.3682 - 93.1747)/(2 \times 93.7689 \times 0.001) = 6.3635$. Effective convexity $= (93.1747 + 94.3682 - 2 \times 93.7689)/(93.7689 \times 0.001^2) = 54.54$.

**Step 4 — graph paper.** Compute five points with Step 1's keystrokes, changing `i` to 4, 4.5, 5, 5.5, 6:

| Yield | 8% | 9% | 10% | 11% | 12% |
|---|---|---|---|---|---|
| Price | 106.80 | 100.00 | 93.77 | 88.05 | 82.80 |

Plot price (vertical, 80–110) against yield (horizontal, 7–13%). Use one large square per 1% of yield and per 5 points of price. Draw the chord from 9% to 11%. Its slope is $(88.05 - 100.00)/2 = -5.975$ points per 1%. Divide by the price at 10% and by the 0.01 yield step: $5.975/(93.77 \times 0.01) = 6.372$ years, an estimate of modified duration from a ruler. Measure the gap between the curve at 10% and the chord's midpoint: the chord passes through $(100.00 + 88.05)/2 = 94.02$, above the curve's 93.77 by 0.26 points. That gap is convexity made visible: $C \approx 2 \times 0.2556/(93.77 \times 0.01^2) = 54.58$. The successive one-point price drops shrink, 6.80, 6.23, 5.72, 5.25, and the client sees why.

**Step 5 — Excel.**

| Cell | Formula | Result |
|---|---|---|
| B1 | `=PV(10%/2, 20, 9/2, 100)` | −93.7689 |
| B2 | `=PRICE(DATE(1987,1,15), DATE(1997,1,15), 9%, 10%, 100, 2, 1)` | 93.7689 |
| B3 | `=MDURATION(DATE(1987,1,15), DATE(1997,1,15), 9%, 10%, 2, 1)` | 6.3635 |
| B4 | `=DURATION(DATE(1987,1,15), DATE(1997,1,15), 9%, 10%, 2, 1)` | 6.6816 |
| B5 | `=(PV(4.95%,20,4.5,100)-PV(5.05%,20,4.5,100))/2/10` | 0.05967 |

(B5 is positive because both PVs are negative, so the expression is the falling-yield price minus the rising-yield price.)

**Step 6 — Python.**

```python
from sdesk import fixed_income as fi
fi.bond_price(0.10, 0.09, 10)          # 93.7689
fi.macaulay_duration(0.10, 0.09, 10)   # 6.6816
fi.modified_duration(0.10, 0.09, 10)   # 6.3635
fi.convexity(0.10, 0.09, 10)           # 54.538
fi.dv01(0.10, 0.09, 10)                # 0.059669
```

**Check.** The calculator's bumped duration (6.3635), the graph-paper chord (6.372), Excel's `MDURATION` (6.3635) and the analytic formula agree to the precision each method allows. The chord estimate is biased upward slightly because a 200 bp chord is not a tangent.

**Decision consequence.** The point of the exercise is not nostalgia. A desk that can bump a yield on a calculator can audit any model's duration number in thirty seconds. And the graph makes convexity a physical object rather than a second derivative. Twice in this chapter (Examples 6.4 and 6.9), a position that looks hedged on a DV01 basis is exposed to curvature. Draw the curve.

#### Example 6.4 — A DV01-neutral 2s10s steepener, and what it is not neutral to

**Given.** 2-year note: 4.00% coupon, 4.20% yield. 10-year note: 4.25% coupon, 4.40% yield. The desk believes the curve will steepen and wants no exposure to the level of yields. It will short \$50 million face of the 10-year and buy a DV01-matched amount of the 2-year. Ignore financing for the moment.

**Find.** DV01 of each note; the 2-year face amount; P&L under six scenarios by full repricing; the DV01 approximation of the P&L.

**Solution.**

* 2-year: price 99.6201, DV01 $= 0.018947$ per 100.
* 10-year: price 98.7970, DV01 $= 0.079625$ per 100.
* DV01 of the short 10-year leg: $0.079625/100 \times 50{,}000{,}000 = \$39{,}813$ per bp.
* 2-year face to match: $39{,}813/(0.018947/100) = \$210.13$ million, a hedge ratio of 4.203.

| Scenario | 2y change | 10y change | 2y leg P&L | 10y leg P&L | Total (repriced) | DV01 approx. $= \$39{,}813 \times (\Delta y_{10} - \Delta y_2)$ |
|---|---|---|---|---|---|---|
| Parallel +50 | +50 | +50 | −1,978,629 | +1,943,738 | **−34,891** | 0 |
| Parallel −50 | −50 | −50 | +2,002,759 | −2,039,185 | **−36,426** | 0 |
| Bull steepener | −40 | −10 | +1,600,260 | −400,042 | **+1,200,218** | +1,194,381 |
| Bear flattener | +30 | +5 | −1,190,050 | +198,587 | **−991,463** | −995,318 |
| Bear steepener | +10 | +40 | — | — | **+1,164,746** | +1,194,381 |
| Parallel +150 | +150 | +150 | −5,864,890 | +5,563,917 | **−300,973** | 0 |

**Check.** The position's DV01, summed across legs, is zero to rounding. The DV01 column matches the repriced column to within about 0.5% for curve moves of 30 bp.

**Decision consequence.** The trade is a clean bet on the 2s10s spread for moderate moves. It is **short convexity**: it loses in both parallel scenarios, because the short 10-year leg has more convexity per dollar of DV01 than the long 2-year leg. At ±50 bp the cost is \$35,000–\$36,000, about one bp of spread. At 150 bp it is \$301,000, more than 7 bp of curve move. Three further exposures are absent from the DV01 calculation. **Financing**: the desk is long \$210 million of 2-years funded in repo and short \$50 million of 10-years, whose repo rate can go "special" (below general collateral) if the issue is scarce, which raises the cost of the short. **Gross notional**: \$260 million of face supports a position with zero net DV01, so a margin call or balance-sheet limit can force liquidation in exactly the stress the trade is meant to capture. **Other tenors**: the trade is neutral to 2s and 10s but not to a twist around the 5-year. Size the trade on the spread move you believe and the convexity cost of the parallel move you fear, not on DV01 alone.

#### Example 6.5 — Forward rates, carry, and roll-down

**Given.** (a) An annually compounded zero-coupon curve: 1-year 4.00%, 2-year 4.20%, 3-year 4.35%, 4-year 4.45%, 5-year 4.50%. (b) Proposal 1 of the opening problem: a 5-year note with a 4.50% coupon bought at par (yield 4.50%). Today's 4-year par yield is 4.35%. Repo is 4.00%. Horizon one year.

**Find.** (a) The one-year forward rates, and the 3-year rate starting in 2 years. (b) Carry, roll-down, total, and breakeven yield rise per 100 face, financed and unfinanced; then repeat with repo at 5.00% and with a flat curve.

**Solution.**

(a) From (6.7):

* $f_{0,1} = 4.00\%$.
* $f_{1,2} = 1.042^2/1.04 - 1 = 4.4004\%$.
* $f_{2,3} = 1.0435^3/1.042^2 - 1 = 4.6506\%$.
* $f_{3,4} = 4.7506\%$, $f_{4,5} = 4.7002\%$.
* $f_{2,5} = (1.045^5/1.042^2)^{1/3} - 1 = 4.7005\%$.

A borrower who expects to refinance in two years for three years can lock about 4.70% today in Treasury terms, 50 bp above today's 2-year spot. Whether that is expensive depends on whether the market's expected path is below the forward, which is to say on the term premium.

(b) Financed at 4.00%. Price today 100.00. At the horizon the note is a 4-year bond. At an unchanged 4.50% yield it would still be at par, so pull to par is 0. At the curve's 4-year yield of 4.35% it prices at 100.5453.

| Component | Per 100 face |
|---|---|
| Coupon income $4.50 \times 1$ | 4.5000 |
| Financing $100 \times 4.00\% \times 1$ | −4.0000 |
| **Carry** | **0.5000** |
| Pull to par | 0.0000 |
| **Roll-down** $100.5453 - 100.0000$ | **0.5453** |
| **Total** | **1.0453** |
| DV01 at horizon (4-year, 4.35%) | 0.036470 |
| **Breakeven yield rise** $1.0453/0.036470$ | **28.7 bp** |

Unfinanced, the total return is $4.50 + 0.5453 = 5.0453$ on 100, or 5.045%. Financed at 5.00% instead (an inverted money-market curve), carry is $4.50 - 5.00 = -0.50$, the total is 0.0453, and the breakeven rise is 1.2 bp. With a flat curve (4-year also 4.50%), roll-down is zero, the total is the 0.50 carry, and the breakeven rise is 13.8 bp.

**Check.** Roll-down repriced independently: a 4-year 4.50% coupon at 4.35% is $2.25 \times a_{\overline{8}|0.02175} + 100 \times 1.02175^{-8} = 100.5453$.

**Decision consequence.** The analyst's "it carries" is true: 1.05 points per year per 100 financed. Levered 5:1 on the account's \$20 million, the position is \$100 million face with a horizon DV01 of about \$36,500 per bp. Total expected carry and roll is about \$1.05 million if nothing moves. A 29 bp rise in 4-year yields over the year erases it. A 100 bp rise costs roughly \$3.6 million before convexity, 18% of the account's \$20 million allocation. Carry is a cushion, and the cushion is less than a third of a typical one-standard-deviation annual move in intermediate yields [HYPOTHESIS: compare with the 1994 and 2022 moves in Section 6.9]. Whether to take it depends on the view on the path of policy (Chapter 5). The carry itself is not a reason.

#### Example 6.6 — The term premium is a model output: one yield, two premia

**Given.** The 10-year zero yield is 4.40% (annual compounding). Two analysts supply expected one-year rates for years 1–10.

* Path A, "cuts then normal": 4.0, 3.6, 3.4, 3.3, 3.3, 3.4, 3.5, 3.5, 3.5, 3.5 (%).
* Path B, "higher for longer": 4.3, 4.2, 4.1, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0 (%).

**Find.** The expectations component and term premium under each path, from (6.8).

**Solution.**

* Path A: $\left[\prod(1+r_i)\right]^{1/10} - 1 = 3.4998\%$. Term premium $= 4.40\% - 3.50\% = 0.90\%$.
* Path B: expectations component $= 4.0600\%$. Term premium $= 4.40\% - 4.06\% = 0.34\%$.

The arithmetic average of each path, 3.500% and 4.060%, is within 0.02 bp of the geometric version at these levels.

**Check.** If Path B were the market's true expectation and the premium were zero, the 10-year would yield 4.06%. The 34 bp difference between that and 4.40% is all that Path B attributes to the premium.

**Decision consequence.** The same observed yield supports two opposite trading conclusions. Under A the 10-year pays a 90 bp premium for duration risk, which is attractive to a long-duration buyer. Under B the premium is thin and the buyer is mostly betting that the policy path will be lower than expected. Published estimates from the ACM and Kim–Wright models embed their own versions of A or B, estimated statistically. Before using any term-premium number in a memo, state which model produced it, its vintage, and what expected path it implies, and ask whether you believe that path. A long-duration position justified by "the term premium is high" is a position on the expected path as well.

#### Example 6.7 — Credit spread: expected loss versus premium, and the carry cushion

**Given.** A 5-year BBB corporate bond, 6.00% semiannual coupon, yields 6.10%. The 5-year Treasury yields 4.30%. Assumed recovery 40%. Your real-world estimate of the annual default probability for this issuer is 0.30% [HYPOTHESIS].

**Find.** The spread, the risk-neutral default intensity, the expected-loss portion of the spread, the price impact of a 100 bp spread widening, and the spread widening over one year that would offset the excess carry over Treasuries.

**Solution.**

* Spread $= 6.10\% - 4.30\% = 180$ bp.
* Credit triangle: $\lambda = 0.0180/(1 - 0.40) = 3.00\%$ per year.
* Expected loss at the real-world estimate: $0.30\% \times 0.60 = 0.18\%$ per year, or 18 bp. The remaining 162 bp is default-risk premium, spread-volatility premium and liquidity premium.
* Price 99.5746; modified duration 4.2615; DV01 0.042434 per 100. A 100 bp widening, Treasuries unchanged, reprices the bond from 6.10% to 7.10%: −4.1372 points.
* One-year horizon breakeven: excess carry of 1.80 per 100 divided by the horizon (4-year) DV01 of 0.034951 gives **51.5 bp** of widening.

**Decision consequence.** The spread is about 90% premium and 10% expected loss on your estimate. You are paid mainly for bearing spread volatility and illiquidity, not default. Those are exactly the risks that arrive together in a recession, when spreads can widen by more than the 51.5 bp cushion in weeks. The same anatomy applies to CRE debt. A fixed-rate mortgage coupon of "Treasury + 190 bp" contains a Treasury component that rallies in a crisis and a spread component that widens. The borrower who hedged only the Treasury component (Proposal 3) has hedged the leg that tends to move in the borrower's favour in a crisis.

#### Example 6.8 — The cap-rate/Treasury spread: decomposition and three ways it moves

**Given.** The industrial building of Proposal 2 at a 5.75% cap rate [a variant for this example], 10-year Treasury 4.40%, expected long-run NOI growth 3.00% after reserves. Then Treasuries rise 100 bp to 5.40% under three explanations:

* A: real-rate rise; $g$ and $RP$ unchanged.
* B: inflation-expectations rise; leases with CPI escalators and short remaining terms raise expected NOI growth by 75 bp; $RP$ unchanged.
* C: real-rate rise accompanied by credit tightening that raises the property risk premium by 50 bp.

**Find.** The initial spread, risk premium and required return; the new cap rate, spread and value change in each case.

**Solution.** From (6.12): spread $= 5.75\% - 4.40\% = 135$ bp; $RP = 5.75\% + 3.00\% - 4.40\% = 4.35\%$; required unlevered return $k = 8.75\%$.

| Case | New $r_f$ | $RP$ | $g$ | New cap $c = r_f + RP - g$ | Spread | Value change $c_0/c_1 - 1$ |
|---|---|---|---|---|---|---|
| A | 5.40% | 4.35% | 3.00% | 6.75% | 135 bp | −14.81% |
| B | 5.40% | 4.35% | 3.75% | 6.00% | 60 bp | −4.17% |
| C | 5.40% | 4.85% | 3.00% | 7.25% | 185 bp | −20.69% |

**Check.** Case A is the one-for-one benchmark: pass-through 1, spread unchanged. B has pass-through 0.25; C has 1.5.

**Decision consequence.** The same 100 bp Treasury move produces value changes from −4% to −21%, and spreads from 60 bp to 185 bp. That range is the answer to the broker in the opening problem. A spread "below its long-run average" may reflect expected growth higher than the average, which is plausible for some property types after a period of rent growth. It may reflect a risk premium compressed by abundant credit, which is fragile. Or it may simply reflect a cap-rate index that lags because appraisals and thin trading smooth it (Chapter 2). The spread tells you nothing until you decide which of $RP$ and $g$ moved. Section 6.8 discusses why history cannot settle this quickly.

#### Example 6.9 — Effective duration of levered CRE equity and the refinancing chain

**Given.** Proposal 2: value \$50,000,000, NOI \$3,000,000 after reserves (6.00% cap). Loan \$32,500,000 (65% LTV), fixed 6.00%, 5-year term, 30-year monthly amortization, no prepayment option assumed. Cap-rate pass-through $\beta = 0.6$ [HYPOTHESIS]. Shock: Treasuries +150 bp. For the refinancing at the end of year 5, assume NOI is flat at \$3,000,000 to isolate the rate effect. Lender terms at refinancing: 65% max LTV, 1.25x min DSCR, 9.0% min debt yield, 30-year amortization; the loan rate equals the Treasury yield plus an unchanged spread, so it is 6.00% if Treasuries are unchanged and 7.50% after the shock. The cap rate is 6.00% unchanged, or 6.90% after the shock.

**Find.** (a) Origination debt service and DSCR. (b) The immediate effect of the shock on value and on book and economic equity, and the corresponding effective durations; the first-order durations from (6.13)–(6.14). (c) The refinancing outcome in year 5 with and without the shock. (d) The same shock with a floating-rate interest-only loan at 7.00% all-in.

**Solution.**

(a) Monthly payment $= \$194{,}854$; annual debt service $= \$2{,}338{,}247$; loan constant 7.195%; DSCR $= 3{,}000{,}000/2{,}338{,}247 = 1.283$x. Balance after 60 payments $B_5 = \$30{,}242{,}666$.

(b) New cap rate $= 6.00\% + 0.6 \times 1.50\% = 6.90\%$. Value $= 3{,}000{,}000/0.069 = \$43{,}478{,}261$, down 13.04%.

* Book equity: $\$17{,}500{,}000 \to 43{,}478{,}261 - 32{,}500{,}000 = \$10{,}978{,}261$, down **37.27%**.
* Effective durations: property $0.1304/0.015 = 8.70$; book equity $0.3727/0.015 = 24.84$.
* First order, from (6.13)–(6.14): $D_V = 0.6/0.06 = 10.0$; $D_E = 10/0.35 = 28.57$ with floating or par-valued debt. The gap between 10.0 and 8.70 is convexity: $V = NOI/c$ is convex in $c$.
* Economic equity marks the fixed-rate loan to market. Its modified duration at origination is 4.178. The first-order debt revaluation is $-32{,}500{,}000 \times 4.178 \times 0.015 = -\$2{,}036{,}838$. Economic equity falls 25.63%, an effective duration of 17.09, against a first-order $D_E = (10 - 0.65 \times 4.178)/0.35 = 20.81$. Exact repricing of the loan's 60 payments and balloon at 7.50% gives a market value of \$30,533,976 and economic equity of \$12,944,285, down 26.03%.

(c) Refinancing at the end of year 5:

| | No shock (6.00%, cap 6.00%) | Shock (7.50%, cap 6.90%) |
|---|---|---|
| Value | \$50,000,000 | \$43,478,261 |
| Loan constant $K$ | 7.195% | 8.391% |
| LTV test (65%) | \$32,500,000 | \$28,260,870 |
| DSCR test $NOI/(1.25K)$ | \$33,358,323 | \$28,603,525 |
| Debt-yield test $NOI/0.09$ | \$33,333,333 | \$33,333,333 |
| **Maximum loan (binding)** | **\$32,500,000 (LTV)** | **\$28,260,870 (LTV)** |
| Balance due $B_5$ | \$30,242,666 | \$30,242,666 |
| **Refinancing gap** | **−\$2,257,334 (cash out)** | **+\$1,981,796 (equity required)** |
| DSCR on the old balance at the new rate | 1.379x | 1.182x |

(d) Floating-rate, interest-only \$32.5 million at 7.00% all-in: interest \$2,275,000, DSCR 1.319x. A 150 bp rise in the index adds \$487,500 per year immediately. DSCR falls to 1.086x, and with typical cash-management triggers [HYPOTHESIS: often set between 1.10x and 1.25x in loan documents] the lender would begin sweeping cash.

**Check.** The LTV and DSCR tests are close in both columns. A DSCR test of 1.30x instead of 1.25x would bind in both. The debt-yield test never binds here, and it is the only test that does not move with rates.

**Decision consequence.** A 150 bp Treasury shock that costs the holder of Example 6.2's 10-year note 11.34% of value (exact repricing from 4.50% to 6.00%) costs this equity 37% on paper. More importantly, it converts a \$2.26 million cash-out refinancing into a \$1.98 million equity call, a \$4.24 million swing on \$17.5 million of equity, due on a fixed date. The fixed-rate loan protects cash flow for five years and gives the economic equity a smaller duration (17 versus 25), but the protection expires at the refinancing date, which is exactly when the book-value loss becomes a cash demand. The floating-rate borrower feels the shock in the first month. **The fixed-rate borrower feels it at maturity, all at once.** This is the arithmetic behind every maturity wall (Chapter 12). For the account, it means the building is a long-duration rate position whose duration is an unstable function of $\beta$. Its realized size depends on what rates and cap rates are on one particular date five years from now.

---

### 6.7 CRE application: measuring and hedging a property's rate exposure

#### The transmission table

| Channel | Timing | Sensitivity measure | Example 6.9 value |
|---|---|---|---|
| Cap rate → value | Gradual, through appraisals and trades | $D_V = \beta/c$ | 10.0 (first order) |
| Value → book equity | Same | $D_V/(1-\lambda)$ | 28.6 |
| Floating rate → debt service | Immediate | \$ per bp $= L \times 0.0001$ | \$3,250 per bp per year |
| Rate → loan constant at refinancing | At maturity | $\partial \ln K/\partial r$ | ≈ 9.8 at 7.50% |
| Constant → DSCR-sized proceeds | At maturity | $-\partial \ln K/\partial r$ | ≈ \$27,990 less loan per bp |
| Value → LTV-sized proceeds | At maturity | $\lambda_{max}\,V\,D_V$ | binding in Ex. 6.9 |
| Proceeds − balance → equity call | At maturity, in cash | Refinancing gap | +\$1.98m in the shock |

The DSCR row: at 7.50% and 30-year amortization, a 1 bp rise raises $K$ from 8.3906% to 8.3988%, a 0.098% increase. A DSCR-sized loan of \$28.6 million shrinks by about \$27,990 per bp. Proceeds therefore have a "duration" to the loan rate of about 9.8 before any cap-rate effect.

#### Can the exposure be hedged with Treasuries?

Proposal 3 suggests shorting Treasury notes. Use Example 6.9's first-order value DV01: $V \times D_V \times 0.0001 = 50{,}000{,}000 \times 10 \times 0.0001 = \$50{,}000$ per bp. The 5-year note at par (4.50%) has a DV01 of 0.044331 per 100. Matching \$50,000 per bp requires $50{,}000/0.00044331 = \$112.8$ million face of 5-year notes, **more than twice the building's value.**

That hedge works only if three things hold:

1. **$\beta$ is stable.** If cap rates move 0.25 for 1 (Example 6.8, case B), the hedge is 2.4 times too large. Falling Treasuries with a stable cap rate then produce a loss on the hedge with no offsetting gain on the building.
2. **The correlation holds in stress.** In a flight to quality Treasuries rally while spreads and cap rates widen (Example 6.8's regime table, row 3). The short Treasury position loses at the same time as the building. The "hedge" doubles the loss.
3. **Funding is available.** The short must be financed and marked daily. The building is marked by appraisal, slowly. A hedge that loses in cash while the asset's offsetting gain exists only on paper can force liquidation of the hedge at the worst time.

What can be hedged with more confidence is the **debt-service channel**: an interest-rate cap on floating-rate debt, or a forward-starting swap or swaption that fixes the base rate of the refinancing loan. Those instruments hedge the *loan constant*, which is contractual, rather than the *cap rate*, which is an opinion. Sizing them to the refinancing balance (\$30.2 million) rather than to the property's value DV01 matches the exposure that threatens survival. The cost of the forward lock is the forward premium in Example 6.5(a): you pay the term premium as insurance. Chapter 13 develops hedge selection, and Chapter 18 prices caps.

#### What the buyer is actually underwriting

Proposal 2's 6.00% cap rate with a 6.00% loan has zero positive leverage at origination (Chapter 1, §1.6). The levered return depends on NOI growth and on exit and refinancing conditions. Example 6.9 shows the size of that dependence. An honest memo states: "The equity is a rate position with a duration of about 25–29 on book value. A 150 bp rise in Treasuries at 0.6 pass-through, without offsetting NOI growth, requires about \$2.0 million of new equity at refinancing. We are paid for this by [state the growth assumption] and accept it because [state the view]."

---

### 6.8 When the relationship fails

1. **Pass-through is not a parameter.** $\beta$ in (6.13) is the slope of a relationship that changes with the cause of the rate move (Example 6.8). Estimating it from a regression of cap-rate changes on Treasury changes mixes regimes and suffers from appraisal smoothing, which biases measured $\beta$ toward zero over short windows (Chapter 2). A pass-through estimated in one decade is a hypothesis for the next.
2. **The cap-rate spread mean-reverts slowly, if at all.** With a few decades of data and regimes lasting years, a sample contains only a handful of independent observations of the spread's "average". The standard error of that average is large. [INFERENCE from the persistence of the series; no specific estimate is asserted here.] Trading on a spread's deviation from its mean is a bet that the regime has not changed.
3. **Duration hedges fail when the cash flows change.** Mortgage-backed securities, callable bonds and floating-rate loans with caps have cash flows that depend on rates. Their modified duration from (6.4) is meaningless. Use effective duration by revaluation. A CRE loan with an open prepayment window is a callable bond from the lender's side.
4. **DV01-neutral is not risk-neutral.** Example 6.4's steepener is short convexity and exposed to repo specials, other curve points and balance-sheet limits.
5. **Treasuries are not always liquid.** Benchmark Treasuries are the deepest market most of the time. There have been episodes of sharp dislocation in Treasury market functioning, including the March 2020 "dash for cash" *(verification pending: register a Federal Reserve or Treasury primary account before stating magnitudes)*. A hedge that relies on continuous trading is weakest when it is needed.
6. **The stock–bond correlation can flip.** In low-inflation regimes, Treasuries have often rallied when risk assets fell, so long duration hedged equity risk. In 2022, both fell together (Section 6.9). A CRE portfolio whose diversification assumed negative correlation between rates and risk assets lost on both lines.
7. **Term-premium estimates are not data.** Two respected models can disagree in sign of change over a quarter. Never present a term-premium estimate without its model and vintage.
8. **Breakeven inflation is not expected inflation.** It contains an inflation risk premium and a liquidity component that move in stress. In a crisis TIPS can cheapen relative to nominals for liquidity reasons, depressing breakevens without any change in inflation expectations [INFERENCE from instrument structure].

---

### 6.9 Historical episode: the 1994 bond sell-off and the 2022 duration shock

Two episodes, 28 years apart, test the same mechanism: a central bank tightening faster than priced, a long-duration market caught positioned for stability, and leverage converting mark-to-market losses into forced selling. Daily yield levels below are from the FRED constant-maturity series DGS10 and DGS2 as reproduced by sources cited in `references/sources_ch06.md`. FRED and Treasury sites could not be accessed directly when this chapter was written. The figures are therefore VERIFIED-SECONDARY and flagged for a recheck against FRED itself.

#### 1994

**Date and environment.** Ten-year Treasury yields fell about 151 bp from the end of 1992 to a low in mid-October 1993 [FACT; Bank of England, *Quarterly Bulletin* 1995, ch06-S05, VERIFIED-SECONDARY from a search excerpt; confirm against the full text that the figure refers to U.S. yields *(verification pending)*]. The October 1993 low of the 10-year yield was 5.19% [FACT; CNN/Money 2003, ch06-S06, VERIFIED-SECONDARY]. The federal funds target stood at 3.00% before February 1994 [FACT: implied by the 25 bp increase to 3.25% described in the 2015 FEDS note, ch06-S01, and by the 1994 cycle running from 3.00% to 5.50%, ch06-S03].

**The policy move and what was knowable.** At its February 1994 meeting the FOMC raised its federal funds target by 25 bp to 3.25%, its first increase since 1989 [FACT; FEDS Notes 2015, ch06-S01, VERIFIED-SECONDARY]. It was also the first time the Committee announced a policy decision immediately after the meeting. Until then, the funds-rate objective and the outcome of meetings had not been announced, and minutes were released with a lag [FACT; ch06-S01, ch06-S02, VERIFIED-SECONDARY; exact text of the 4 February 1994 statement *(verification pending)*]. Chairman Greenspan explained the announcement as a way to avoid confusion about the first firming since early 1989 [FACT; ch06-S02, VERIFIED-SECONDARY]. Through 1994 the FOMC raised the target six times, from 3.00% to 5.50%, including 25 bp on 18 April and 50 bp on 17 May to 4.25% [FACT; Bank of England *Quarterly Bulletin* 1994 Q3, ch06-S04; Cleveland Fed, ch06-S03; VERIFIED-SECONDARY], and 75 bp on 15 November to 5.50% [FACT; secondary sources, ch06-S03]. A final increase on 1 February 1995 took the target to 6.00% [FACT; ch06-S03]. The 22 March move (+25 bp to 3.50%) and the 16 August move (+50 bp to 4.75%) are implied by these totals [INFERENCE; dates and sizes *(verification pending)* against the FOMC's historical table].

What was knowable in January 1994: the economy was growing, and the Fed had signalled that policy was accommodative. A tightening in 1994 was widely anticipated in direction. What was not knowable was the *speed and cumulative size*. The total was 250 bp in ten months, plus 50 bp in February 1995. Nor was it knowable how much leveraged duration had been accumulated on the premise of continued low short rates.

**What happened in the bond market.** The 10-year yield rose from 5.19% (October 1993) to a peak of 8.05% on 7 November 1994 [FACT; ch06-S06 and FRED-derived DGS10 data, ch06-S07, VERIFIED-SECONDARY], a rise of 286 bp. The Bank of England put the rise in 10-year yields during calendar 1994 at about 200 bp [FACT; ch06-S05, same caveat as above *(verification pending)*]. The difference from 286 bp is the measurement window: low-to-peak versus calendar year. Volatility rose across the major bond markets in 1994 [FACT; BIS, ch06-S16, VERIFIED-SECONDARY]. The Bloomberg U.S. Aggregate index, now the standard broad benchmark, returned about −2.9% in 1994 [FACT; ch06-S11, VERIFIED-SECONDARY]. For a diversified, coupon-paying index of intermediate duration that is a modest calendar-year loss. For leveraged and long-duration holders the same yield move was far more damaging [INFERENCE from the duration arithmetic below].

**Illustrative arithmetic** [HYPOTHESIS: a 10-year note with a 5.25% coupon repriced instantaneously from 5.19% to 8.05%; the actual move took 13 months and earned coupons]: price $100.4635 \to 81.0156$, a loss of 19.36%. Duration alone predicts −22.16 points. Adding convexity, −19.18. The full move is a tail scenario for which "DV01 × 286" would overstate the loss by about 2.7 points per 100 of price.

**Interpretations.** (i) *Policy surprise.* The pace of tightening exceeded what the curve had priced, so expected short rates were repriced upward. (ii) *Credibility and term premium.* Long yields rose by more than the revision to expected policy rates alone would suggest. Ganley and Noblet's Bank of England article (1995) explored the role of monetary-policy credibility in the 1993–94 yield changes, and noted that other proposed explanations included the changing cyclical conjuncture and technical factors such as the behaviour of hedge funds [FACT that these explanations were examined: ch06-S05, VERIFIED-SECONDARY; the article's quantitative findings were not read in full and are not reported here *(verification pending)*]. (iii) *Positioning and leverage.* Leveraged investors and mortgage-related hedging amplified the move. Holders of mortgage-backed securities saw durations extend as prepayments slowed, and hedging that extension meant selling Treasuries into a falling market [INFERENCE from MBS mechanics; the size of convexity-hedging flows in 1994 is *(verification pending)*]. These interpretations are complements, not rivals. Their weights are disputed.

**What it does and does not establish.** It establishes that a tightening anticipated in direction can still produce a large loss when its speed is mispriced and positions are levered. It establishes that duration hedges of negatively convex assets add to selling pressure. It does **not** establish that every tightening cycle produces a 1994-scale sell-off, nor that the Fed's new transparency caused the losses.

#### 2022

**Date and environment.** Consumer prices rose 9.1% over the twelve months ending June 2022, the largest 12-month increase since the period ending November 1981 [FACT; BLS CPI release of 13 July 2022, ch06-S08, VERIFIED-PRIMARY]. The FOMC began raising its target range in March 2022 with a 25 bp increase. It raised by 50 bp in May, 75 bp at each of the June, July, September and November meetings, and 50 bp in December, ending the year at 4.25%–4.50%, a cumulative 425 bp [FACT; ch06-S09, VERIFIED-SECONDARY; the June move was described as the largest single increase since 1994]. The March–December sequence sums to 425 bp: $25 + 50 + 4 \times 75 + 50 = 425$.

**What happened.** The 10-year Treasury yield (DGS10) was 1.63% on the first trading day of 2022 and 3.88% on the last, a rise of 225 bp, with a closing high of 4.25% on 24 October. The 2-year (DGS2) rose from 0.78% to 4.41%, a rise of 363 bp, with a high of 4.72% on 7 November [FACT; FRED-derived data, ch06-S07, VERIFIED-SECONDARY; recheck against FRED]. The 2s10s curve inverted and stayed inverted from 6 July 2022 [FACT; ch06-S10, VERIFIED-SECONDARY]. At year-end the 10-year was 53 bp *below* the 2-year. That was a bear flattener of historic size: the short end rose 138 bp more than the long end. The Bloomberg U.S. Aggregate returned about −13% for the year, its worst calendar year since the index began in 1976 [FACT; ch06-S11, VERIFIED-SECONDARY].

**Illustrative arithmetic** [HYPOTHESIS: a 10-year note with a 1.625% coupon bought at 1.63% on the first day of 2022; one year later it is a 9-year note, priced at 3.88% on the assumption that the 9-year yield equals the 10-year]: price $99.954 \to 83.007$; with 1.625 of coupons the one-year total return is **−15.33%**. At the October high (4.25%, instantaneous, 10-year maturity), the price loss would have been 21.17%. The note's modified duration at purchase was 9.19 years, so a first-order estimate for +225 bp is −20.69%. Low coupons mean long durations. The 2022 starting point had the lowest coupons and longest durations in the modern Treasury market, so the same basis-point move cost more than it would have from a 1994 starting point.

**Valuation and financing context for CRE.** Floating-rate CRE borrowers faced the debt-service channel of Section 6.7 within months. Fixed-rate borrowers faced the refinancing channel only as loans matured, from 2023 onward. Appraisal-based cap-rate indices adjusted more slowly than Treasury yields, so measured cap-rate spreads compressed in 2022 before transaction evidence accumulated [INFERENCE from appraisal smoothing (Chapter 2); specific index values *(verification pending)* and not stated here].

**Interpretations.** (i) *Inflation and policy repricing*: the dominant driver of the 2-year was the repricing of the policy path. (ii) *Term premium*: published model estimates of the 10-year term premium rose during 2022 from low levels. The size depends on the model and vintage (Section 6.5.6), so no figure is asserted here. (iii) *Correlation regime change*: bonds and equities fell together, removing the diversification that many portfolios had assumed (Section 6.8, item 6).

**What 1994 and 2022 together establish.** Both establish that duration is a risk factor, not a property of "safe" assets, and that leverage turns marks into cash calls. 2022 additionally establishes that the starting level of yields sets the duration, and therefore the damage per basis point. **What they do not establish:** that a curve inversion predicts recession on a fixed timetable (the 2022 inversion is a single observation with its own causes), or that cap rates must "catch up" to Treasuries by a fixed amount (Example 6.8 shows why they need not).

---

### 6.10 Decision exercise: the investment committee's three proposals

Return to Section 6.1. Prepare a two-page memo on `desk/investment_memos/investment_committee_memo.md` and fill in `desk/scenario_templates/yield_curve_worksheet.md`. Your memo must:

1. State the DV01 of each proposal in dollars per bp: the 5-year note financed at 5:1 (Example 6.5), the building's equity (Example 6.9, first order and effective), and the proposed Treasury short sized as the partner suggests.
2. For Proposal 1, state the breakeven yield rise, the loss at +100 bp, and whether the account's mandate permits 5:1 leverage on a position whose loss at +100 bp is about 18% of its allocation.
3. For Proposal 2, evaluate the broker's spread argument using (6.12). Give the growth and risk-premium assumptions under which the 160 bp spread is fair, cheap or rich.
4. For Proposal 2, report the refinancing gap at +0, +100 and +150 bp, and the equity reserve you would hold.
5. For Proposal 3, decide whether to hedge, with what instrument, and sized to what (value, debt service, or refinancing balance). State what $\beta$ the hedge assumes and what happens to it in a flight to quality.
6. State invalidation criteria and what you will *not* do. Abstention on any proposal is a legitimate answer.

**Rubric** (full version in `problems/solutions/ch06_solutions.md` §Decision exercise). Score 0–4 on each dimension.

| Dimension | Strong answer |
|---|---|
| Measurement | Correct DV01s; distinguishes book from economic equity duration; uses repricing for stress |
| Carry discipline | Treats carry and roll as a cushion with a stated breakeven, not as a return |
| Spread reasoning | Decomposes the spread into $RP - g$; refuses the "long-run average" anchor without regime evidence |
| Refinancing survival | Identifies the year-5 equity call as the binding risk; sizes a reserve or structure (lower leverage, longer term, extension option) |
| Hedge design | Hedges the contractual channel (loan constant) rather than the cap rate; recognizes basis and correlation risk in a Treasury short; does not hedge a deal that may not close |
| Judgment | Says what would change the decision: evidence on $\beta$, NOI growth, lender terms, policy path |

There is no single correct allocation. A memo that recommends all three proposals at full size without reconciling them has missed that they are the same exposure.

---

### 6.11 Frequent analytical errors

1. **Comparing yields with different conventions.** A bill's discount rate, a note's BEY and a mortgage's monthly rate are not comparable without conversion (Example 6.1).
2. **Using modified duration for large moves.** Stress tests at 200–300 bp must reprice (Example 6.2).
3. **Calling a DV01-neutral trade "hedged".** It is neutral only to parallel moves of the two legs and is short or long convexity (Example 6.4).
4. **Treating carry as return.** Carry is compensation for a breakeven yield move. State the breakeven (Example 6.5).
5. **Quoting a term-premium estimate as a fact.** It is a model output with a vintage (Example 6.6).
6. **Reading a credit spread as expected default loss.** In investment-grade credit the spread is mostly premium (Example 6.7).
7. **Anchoring on the average cap-rate spread.** The spread is $RP - g$. Its average spans regimes (Example 6.8).
8. **Assuming one-for-one cap-rate pass-through, or zero.** Both are special cases (Section 6.5.9).
9. **Ignoring leverage in rate sensitivity.** Equity duration is the property duration divided by the equity share (Example 6.9).
10. **Treating a fixed-rate loan as removing rate risk.** It defers the risk to the refinancing date and concentrates it (Example 6.9).
11. **Hedging cap-rate risk with Treasuries without considering correlation in stress.** The hedge can lose in a flight to quality while the property also loses (Section 6.7).
12. **Confusing price in 32nds with decimals.** 98-17 is 98.53125, not 98.17.

---

### 6.12 Connections to other chapters

* Chapter 1 §1.6 introduced negative leverage on the industrial building. This chapter measures its rate exposure.
* Chapter 2 explains appraisal smoothing, which biases measured cap-rate pass-through.
* Chapter 5 develops the expected path of policy rates, the first component of (6.8).
* Chapter 7 extends yields to sovereign spreads and FX-hedged yields for foreign buyers.
* Chapter 9 uses (6.12) in valuation and builds sensitivity grids on cap rates.
* Chapter 10 develops loan sizing, amortization and refinancing (Section 6.5.11).
* Chapter 12 applies the refinancing gap to maturity walls.
* Chapter 13 selects hedges for CRE rate exposure.
* Chapter 17 develops credit spreads, hazard rates and CMBS.
* Chapter 18 prices interest-rate caps and swaptions.
* Chapter 23 revisits 1994 and 2022 among the historical episodes.
* Case B (Refinancing Cliff) and Case C (Cap Rate Expansion and Equity Destruction) apply Example 6.9.

---

### 6.13 One-page reference sheet

| Quantity | Formula | Note |
|---|---|---|
| Bill price | $P = F(1 - d\cdot\text{days}/360)$ | $d$ = discount rate |
| Bill BEY (≤182 days) | $(F-P)/P \times 365/\text{days}$ | Quadratic (6.3) for longer bills |
| Money-market yield | $(F-P)/P \times 360/\text{days}$ | Compare with repo, SOFR |
| Effective annual | $(1+y/m)^m - 1$ | Use to compare across instruments |
| Bond price | $\sum CF_k (1+y/m)^{-k}$ | Excel `PRICE`, `PV` |
| Macaulay duration | $\sum t_k \, PV_k / P$ | Excel `DURATION` |
| Modified duration | $D_{mac}/(1+y/m)$ | Excel `MDURATION` |
| DV01 | $P \cdot D_{mod} \cdot 0.0001$ | per unit of face |
| Price change | $\Delta P/P \approx -D_{mod}\Delta y + \tfrac12 C(\Delta y)^2$ | Reprice for large moves |
| Hedge ratio | $DV01_{exposure}/DV01_{hedge}$ | Per unit of face |
| Forward | $[(1+s_2)^{t_2}/(1+s_1)^{t_1}]^{1/(t_2-t_1)} - 1$ | Annual compounding |
| Term premium | $y_n - \text{expectations yield}$ | Model-dependent |
| Carry + roll | coupon − financing + roll-down | Breakeven $\approx$ total / $DV01_h$ |
| Credit triangle | $\lambda = s/(1-R)$ | Risk-neutral |
| Breakeven inflation | $(1+y_{nom})/(1+y_{real}) - 1$ | Includes premia |
| Cap rate | $c = r_f + RP - g$ | Spread $= RP - g$ |
| Property duration | $D_V = \beta/c$ | $\beta$ unstable |
| Equity duration | $D_E = (D_V - \lambda D_{debt})/(1-\lambda)$ | Book: $D_{debt} = 0$ |
| Loan constant | $12 \cdot \frac{r/12}{1-(1+r/12)^{-12N}}$ | Excel `=PMT(r/12,12N,-1)*12` |
| DSCR-sized loan | $NOI/(DSCR \cdot K)$ | Proceeds "duration" ≈ $\partial\ln K/\partial r$ |
| Refinancing gap | $B_T + \text{costs} - L_{new}$ | Positive = equity required |

**Numbers worth remembering (from this chapter's examples, not universal constants).** A 10-year note at a 4–5% yield has a modified duration near 8 and a DV01 near \$780 per \$1 million face. A 2-year has a DV01 near \$190 per \$1 million. A 6% cap rate with full pass-through implies a property duration near 17. At 0.6 pass-through, it is 10. At 65% LTV with floating debt, equity duration is about 2.9 times the property's.

---

### References for this chapter

All sources are listed with verification status in `references/sources_ch06.md` (IDs ch06-S01 to ch06-S17), for merger into `SOURCE_REGISTER.md`.

* Adrian, T., Crump, R. K., and Moench, E. (2013). "Pricing the Term Structure with Linear Regressions." *Journal of Financial Economics*, 110(1), 110–138. Term-premium estimates published by the Federal Reserve Bank of New York.
* Kim, D. H., and Wright, J. H. (2005). "An Arbitrage-Free Three-Factor Term Structure Model and the Recent Behavior of Long-Term Yields and Distant-Horizon Forward Rates." Finance and Economics Discussion Series 2005-33, Board of Governors of the Federal Reserve System.
* Board of Governors of the Federal Reserve System (2015). "The Effects of FOMC Communications before Policy Tightening in 1994 and 2004." *FEDS Notes*, 24 September 2015.
* Federal Reserve Board (1994). Press release, 4 February 1994. https://www.federalreserve.gov/fomc/19940204default.htm.
* Federal Reserve Bank of Cleveland (1995). "Monetary Policy: An Interpretation of 1994, a Challenge for 1995." *Economic Commentary*, 15 February 1995.
* Bank of England (1994). "Financial Market Developments." *Quarterly Bulletin*, 1994 Q3.
* Ganley, J., and Noblet, G. (1995). "Bond Yield Changes in 1993 and 1994: An Interpretation." Bank of England *Quarterly Bulletin*, May 1995 (1995 Q2).
* Bank for International Settlements. Conference papers on financial market volatility (BIS Conference Papers vol. 1), https://www.bis.org/publ/confp01a.pdf.
* CNN/Money (2003). Commentary on the 1993–94 bond sell-off, 12 August 2003. https://money.cnn.com/2003/08/12/commentary/bidask/bidask/index.htm.
* U.S. Bureau of Labor Statistics (2022). "Consumer Price Index — June 2022." News release, 13 July 2022.
* Federal Reserve Bank of St. Louis, FRED: series DGS10 and DGS2 (10-year and 2-year Treasury constant-maturity yields).
* U.S. Department of the Treasury, TreasuryDirect: auction FAQs; 31 CFR Part 356 (Uniform Offering Circular).
* Gordon, M. J. (1962). *The Investment, Financing, and Valuation of the Corporation*. Homewood, IL: Irwin.


\newpage

## Chapter 7 — Fiscal Policy, Sovereign Risk, and Global Capital

> **Status:** Complete (v1.0). All eight worked examples, the CRE application table, the problems, and the solutions are reproduced in `tests/test_ch07_examples.py`. Problems are in `problems/questions/ch07_problems.md` and solutions in `problems/solutions/ch07_solutions.md`. Sources are listed in `references/sources_ch07.md`. Items marked *(verification pending)* are flagged in that file: the exact trading day of Spain's July 2012 10-year yield peak, and the bibliographic page range of the ACM term-premium paper.

### Learning objectives

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

### 7.1 Opening investment problem: the June 2012 Madrid office

It is late June 2012. You advise a U.S. family office with \$300 million of dollar capital that can be deployed globally. A Spanish bank, under pressure from new provisioning rules, offers a performing loan secured by a Madrid office building. It also offers the building itself through a consensual sale if you prefer to own it outright. The facts below are [HYPOTHESIS] except where cited. The setting is real and the facts about it are documented in §7.9.

* **The building.** NOI before the downturn was €4.0 million. The owner bought it at a 5.00% cap rate (€80 million) with a €52 million five-year loan that matures in 2013. Tenants are paying, but two leases roll in 18 months and local office rents are falling. Current NOI is about €3.8 million.
* **The sovereign.** Spain's 10-year yield has risen above 7% [FACT; §7.9]. Euro-area finance ministers have agreed to lend Spain up to €100 billion to recapitalize its banks [FACT; §7.9]. Some commentators discuss the possibility that Spain leaves the euro. If it did, a euro-denominated claim on a Spanish property might be redenominated into a new, weaker currency.
* **The bank.** The selling bank holds a large portfolio of Spanish government bonds and must raise its provisions on real estate developer loans [FACT; §7.9]. It is cutting new property lending.
* **Your alternatives.** You can (a) buy the building, (b) buy the loan at a discount, (c) buy nothing in Spain and instead buy 10-year U.S. Treasuries, or (d) wait.

Your investment committee will ask: What does the sovereign's condition have to do with this building's value? Is the discount compensation for risk, for illiquidity, or for a forced seller's needs? If you buy in euros, should you hedge back to dollars, and what will the hedge cost? What would make you wrong?

By the end of the chapter you will be able to answer these with numbers. Section 7.10 returns to the decision.

---

### 7.2 Economic intuition: the sovereign is the first borrower in the capital stack

Every country has a capital structure. The government sits at the top. Its bonds are the reference asset against which banks, corporations, and property owners are priced. When the sovereign's credit is strong, its bonds are the risk-free rate. When the sovereign's credit is weak, that "risk-free rate" acquires a credit spread, and everything priced off it reprices.

Five mechanisms connect fiscal policy and sovereign risk to commercial real estate.

**1. The discount-rate channel.** A cap rate is, roughly, a risk-free rate plus a property risk premium minus expected NOI growth (Chapter 6). If the sovereign yield rises because investors demand compensation for default risk, the floor under every domestic cap rate rises. This happens even if the property's tenants are unaffected.

**2. The bank-capital channel.** Banks hold government bonds. They hold them for liquidity regulation, as collateral for central-bank borrowing, and because regulation has historically assigned them low capital charges. When sovereign bond prices fall, bank capital falls. A bank with less capital must shrink its balance sheet or raise equity. CRE loans are among the first to be cut, because they are capital-intensive, illiquid, and usually renewable at maturity rather than contractually committed. The bank's weakness then feeds back into the sovereign's, because markets expect the government to recapitalize its banks. This is the **bank–sovereign doom loop** (§7.4.7).

**3. The supply channel.** A government running large deficits must sell bonds. Somebody must buy them. If domestic savers and foreign buyers absorb the supply only at lower prices, long-term yields carry a higher **term premium**. The size of this effect is genuinely uncertain (§7.4.3). Its direction is not seriously disputed.

**4. The external channel.** A country whose government and private sector together spend more than they save must borrow from abroad. Foreign investors compare returns in their own currency. For many of them, the relevant comparison is the **FX-hedged** return, which depends on the short-rate differential between the two currencies. When hedging costs rise, hedged foreign buyers step back. Foreign demand for a country's bonds and its property can then fall even though nothing about the assets themselves has changed.

**5. The currency-regime channel.** A country that fixes its exchange rate and allows free capital movement gives up independent monetary policy. Under stress, it must defend the peg with interest rates, which raises property cap rates and borrowing costs exactly when the economy is weakest. A euro-area member is an extreme case: it has no national exchange rate to adjust and no national central bank to act as lender of last resort to the sovereign. This is one explanation of why the 2010–12 crisis happened inside the euro area and not, for example, in the United Kingdom or Japan, both of which borrow in currencies their own central banks issue [INFERENCE: an interpretation common in the literature on the euro-area crisis, not a settled fact].

#### Why a CRE investor should care before the sovereign is in trouble

Sovereign risk sounds like an emerging-market problem or a historical curiosity. It is neither. The U.S. federal government's debt held by the public was about 99% of GDP at the end of fiscal year 2025, and the Congressional Budget Office projects it reaching about 120% of GDP by 2036 [FACT; CBO February 2026 baseline as summarized by CRFB, ch07-S19]. Nobody serious expects the U.S. to default on Treasury securities. The relevant risks for a U.S. CRE investor are different and more plausible:

* A higher term premium that keeps long rates and cap rates elevated even if the Fed cuts short rates.
* A change in the identity of the marginal buyer of Treasuries, for example from hedged foreign institutions to price-sensitive domestic investors. This makes yields more volatile.
* Foreign CRE capital that disappears when hedging costs rise.
* An event in which fiscal news interacts with leverage somewhere in the financial system. The 2022 U.K. gilt episode (§7.8) is the template.

#### The questions this chapter trains you to ask

When fiscal or sovereign news arrives, ask:

1. Did $r$ or $g$ change, or did the primary balance change? Which one, and is it persistent?
2. Is the spread move expected loss, risk premium, liquidity, or redenomination risk?
3. Who holds the bonds, and how leveraged are they?
4. Who is the marginal foreign buyer, and is that buyer hedged?
5. What does the local banking system own, and how much capital does it have?
6. Through which of the five channels does the news reach the property I own or am underwriting?

---

### 7.3 Technical definitions

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

### 7.4 Equations and derivations

#### 7.4.1 The law of motion for the debt ratio

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

#### 7.4.2 Why the effective rate lags the market rate

Only maturing debt and new borrowing reprice. If a fraction $\phi \approx 1/\text{WAM}$ of the stock reprices each year, a simple approximation is

$$r_t = r_{t-1} + \phi\,(r^{mkt} - r_{t-1}).$$

With a weighted average maturity of five years, a jump in market yields from 2.5% to 5.0% raises the effective rate by only about half a point in the first year. This lag is why debt dynamics look benign for several years after rates rise, and why a government with short-maturity debt (or floating-rate debt, or large central-bank reserves that pay the policy rate) is more exposed. Problem 7.6 computes it.

#### 7.4.3 Deficits, supply, and the term premium

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

#### 7.4.4 Sovereign spreads, default probability, and CDS

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

#### 7.4.5 The savings–investment identity and the balance of payments

From national income accounting, with private saving $S_p$, private investment $I$, and government balance $T - G$ (all as shares of GDP):

$$\boxed{CA = (S_p - I) + (T - G)}.$$

In balance-of-payments accounting, ignoring the small capital account and statistical discrepancy,

$$CA + KA - FA = 0 \;\Rightarrow\; FA \approx CA,$$

where FA is net acquisition of foreign assets minus net incurrence of liabilities. A current-account deficit means the country is, on net, selling assets or issuing liabilities to foreigners. For a country with a pegged currency, the central bank's reserve change is part of FA:

$$\Delta \text{Reserves} = CA + \text{private net financial inflows}.$$

**An identity is not a theory.** $CA = (S_p - I) + (T-G)$ says that if the government deficit widens by one point and the current account does not change, then private saving net of investment must rise by one point. It does not say which adjusts, or by what price mechanism. Interest rates, the exchange rate, and income all move. The "twin deficits" view (a fiscal deficit widens the current-account deficit one for one) is a special case that holds only if private behavior does not respond. It is [HYPOTHESIS] in any given episode.

#### 7.4.6 Currency regimes and the impossible trinity

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

#### 7.4.7 Covered interest parity and hedged returns

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

#### 7.4.8 The doom loop as balance-sheet arithmetic

A bank has assets $A$, equity $E$, and domestic sovereign bonds $B$ with modified duration $D$. A sovereign spread shock $\Delta s$ produces a mark-to-market loss of approximately

$$\Delta E \approx -B\,D\,\Delta s.$$

If the bank targets a leverage ratio $\ell = E/A$ and cannot raise equity, its maximum balance sheet after the shock is

$$A^{max} = \frac{E + \Delta E}{\ell}, \qquad \text{Shrinkage} = (A + \Delta E) - A^{max}.$$

Because $1/\ell$ is large (about 17 at 6%), a modest capital loss forces a large asset reduction. If the bank keeps its sovereign bonds, the shrinkage falls entirely on loans and other assets. That is the transmission from sovereign risk to CRE lending capacity. The loop closes when markets price the probability that the government must recapitalize the bank. Acharya, Drechsler, and Schnabl (2014) document that sovereign CDS rose after the 2008 bank bailouts and that subsequent sovereign CDS changes explain bank CDS changes [FACT about the paper's findings; ch07-S24]. Brunnermeier et al. (2016) argue that the loop can be avoided by limiting banks' domestic sovereign exposures relative to their equity [FACT about the paper's argument; ch07-S25].

Accounting matters for timing but not for economics. A bond held at amortized cost does not reduce reported capital when its price falls. Counterparties, rating agencies, and depositors can still see the exposure and price it.

---

### 7.5 Worked examples

All inputs are [HYPOTHESIS] unless a source is cited. Every number is reproduced in `tests/test_ch07_examples.py`.

#### Example 7.1 — Debt dynamics and the interest–growth differential

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

#### Example 7.2 — What a sovereign spread is paying you for

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

#### Example 7.3 — Auction sizes, duration supply, and the term-premium channel

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

#### Example 7.4 — Who finances the deficit? The savings–investment identity

**Given.** A large economy has nominal GDP of \$29.0 trillion [HYPOTHESIS: round number]. Private saving is 21.5% of GDP, private investment 21.0%, and the general government balance −4.4% of GDP [HYPOTHESIS for the decomposition]. For comparison, the U.S. current-account deficit in 2024 was \$1.13 trillion, or 3.9% of GDP, as first reported by BEA [FACT; ch07-S20].

**Find.** (a) The current-account balance as a share of GDP and in dollars. (b) The net financial inflow from abroad. (c) The extra foreign financing required if the government deficit widens by one point of GDP and private saving and investment do not respond.

**Solution.**

(a) $CA = (S_p - I) + (T-G) = (0.215 - 0.210) + (-0.044) = -0.039$, i.e., −3.9% of GDP. In dollars: $-0.039 \times 29.0 = -\$1.131$ trillion.

(b) Ignoring the capital account and statistical discrepancy, the country must sell \$1.131 trillion of net claims on itself to foreigners (Treasuries, corporate bonds, equities, property, or reductions in its holdings of foreign assets).

(c) $0.01 \times 29.0 = \$290$ billion per year of additional net foreign financing, *if* $S_p - I$ does not change.

**Check.** The constructed decomposition reproduces the BEA magnitude: \$1.131 trillion and 3.9% of GDP. The decomposition itself is illustrative and is not BEA's.

**Decision consequence.** The identity says the extra \$290 billion must come from somewhere. Three things can happen, alone or together. (i) Foreigners buy more U.S. assets, which requires a better expected return in their currency: a higher U.S. yield, a cheaper dollar, or a lower hedging cost (Example 7.5). (ii) Domestic private saving rises or investment falls, which in practice usually requires higher real interest rates (crowding out). (iii) The central bank buys the bonds, which raises the inflation question. All three raise the required return on U.S. assets at the margin, including property. The relevant question for a CRE investor is not "will foreigners stop buying?" It is "at what price will the marginal buyer absorb the supply, and who is that buyer?"

Reproduce: `tests/test_ch07_examples.py::test_example_7_4`

#### Example 7.5 — Hedged versus unhedged U.S. Treasuries for euro and yen investors

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

#### Example 7.6 — A euro investor buys a U.S. industrial building: hedged yield and hedge liquidity

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

#### Example 7.7 — The doom loop in one bank's balance sheet

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

#### Example 7.8 — From the sovereign to the building: the Madrid office

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

### 7.6 CRE application: the global-capital screen for a U.S. acquisition

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

### 7.7 When the relationship fails

1. **$r - g$ is not exogenous.** The debt dynamics equation treats $r$ and $g$ as given. In a crisis, $r$ rises *because* debt is high, and $g$ falls because fiscal tightening and bank deleveraging depress output. Fiscal consolidation can therefore raise the debt ratio in the short run if it shrinks nominal GDP enough. Projections that hold $r$ and $g$ fixed understate the nonlinearity.
2. **Spreads are not expected losses.** Inside a currency union, part of the spread is redenomination risk: the risk that the bond is repaid in a new currency. That risk is not captured by PD × LGD and can disappear quickly when a central bank credibly removes it. After the ECB's July–September 2012 statements and the OMT announcement, peripheral spreads fell without any change in fiscal fundamentals of comparable speed (§7.9) [INFERENCE: commentators widely credit the announcement; the counterfactual cannot be observed].
3. **CIP fails when balance sheets are scarce.** Since 2008, persistent deviations from CIP have been documented for major currencies (ch07-S27). The hedge cost then exceeds the rate differential, often most at quarter-ends and in stress. Treat the CIP forward as a lower bound on hedge cost for a non-bank investor.
4. **Pegs fail abruptly.** A peg is credible until the central bank decides its cost is too high. The Swiss National Bank discontinued its CHF 1.20 floor on 15 January 2015 and said enforcing it was no longer justified (ch07-S28). Investors who treated the floor as a permanent one-sided bet lost money on the day.
5. **A reserve-currency sovereign's bad news can lower its own yields.** When fiscal stress coincides with global risk aversion, investors may buy the stressed sovereign's bonds as a safe haven. The sign of the yield response to fiscal news therefore depends on whether the issuer's debt is the world's safe asset. This is an [INFERENCE] about mechanism; specific episodes should be checked against data before being cited.
6. **The transmission can run through leverage rather than default risk.** In September 2022, a U.K. fiscal announcement was followed by a sharp rise in long gilt yields. The damage came through collateral calls on leveraged pension hedges, not through any doubt about the U.K. government's ability to pay (§7.8). Models that look only at PD × LGD miss this channel entirely.
7. **The identity says nothing about timing.** A large current-account deficit can be financed smoothly for years, then suddenly cannot. The balance-of-payments identity holds at every moment; the price that clears it changes.

---

### 7.8 A second episode in brief: the 2022 U.K. gilt and LDI stress

**Date and environment.** In September 2022, U.K. inflation was high and the Bank of England was raising rates. U.K. defined-benefit pension schemes had widely used liability-driven investment (LDI) strategies [FACT that LDI funds were central to the episode; ch07-S17] that hedged long-dated liabilities with leveraged gilt positions and derivatives.

**What happened.** Following the government's fiscal announcement of 23 September 2022, long-dated gilt yields rose very rapidly. In a letter to the Treasury Committee dated 5 October 2022, Deputy Governor Jon Cunliffe described the move. Secondary coverage of the letter reports that the four-day rise in 30-year yields was more than twice as large as the largest such move since 2000 [FACT as reported; ch07-S18; VERIFIED-SECONDARY]. On 28 September 2022 the Bank announced temporary, targeted purchases of long-dated conventional gilts for financial-stability reasons. It raised the daily auction maximum from £5 billion to £10 billion on 10 October and extended purchases to index-linked gilts on 11 October. It ended the operations on 14 October 2022, having purchased £19.3 billion of gilts in total [FACT; ch07-S17].

**Mechanism.** When yields rose, LDI funds faced collateral calls. To meet them, they sold gilts, which raised yields further and triggered more calls. The Bank's stated purpose was to give LDI funds time to rebuild resilience, not to provide a permanent backstop [FACT; ch07-S17].

**What it establishes.** Fiscal news can transmit to asset prices through leverage and collateral in a specific investor class. The stress was concentrated in a market (long gilts) and in a group (pension LDI) that a CRE investor might not watch. The episode does *not* establish that U.K. sovereign credit risk rose materially, nor that the fiscal announcement alone would have produced that yield move without the leverage. Those are contested interpretations.

**CRE connection.** U.K. pension funds were also holders of property funds and other illiquid assets. When a leveraged hedge needs cash, the investor sells what it can, which may include its liquid holdings of real estate securities or units in open-ended property funds. The analog to Example 7.6(b) is exact: hedge settlement needs cash, and the hedged asset may not provide it.

---

### 7.9 Historical episode: the euro-area sovereign crisis, 2010–2012

#### Date and environment

The euro was introduced in 1999. Until the crisis, sovereign spreads within the euro area were small by later standards: Italy's spread over Bunds first exceeded 500 bp only in November 2011 [FACT; ch07-S06]. Banks across the area held government bonds of many members. Ireland and Spain had large domestic credit and property booms in the 2000s [INFERENCE from the scale of the later property-loan transfers and provisions documented below: ch07-S11, S12, S13].

#### The sequence of events

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

#### Information available at the time

By mid-2012, the following were public: Greek restructuring had occurred, so euro-area sovereign default was no longer hypothetical. Spain's banks needed external capital, and the government had borrowed from its partners to supply it. The ECB had provided about €1 trillion of three-year funding, and some of it had been used to buy domestic sovereign bonds (the carry trade of Example 7.7(e)) [INFERENCE that some was used this way is widely discussed; amounts by country are not stated here]. Euro-area governments had begun to discuss a banking union.

What was *not* knowable was whether the ECB would act as a backstop for sovereign bond markets, whether its governing council and its member governments would agree, and whether such a backstop would be legal. Those questions were answered between 26 July and 6 September 2012, and the legal question not until 2015.

#### Transmission to property values, borrowing costs, and lending capacity

The CRE evidence from the period runs through the channels of §7.2:

* **Discount rate and value.** Irish commercial property capital values fell by over 65% from their 2007 peak, according to IPD/SCSI index reporting, before returning to growth in 2013 [FACT as reported; ch07-S15; VERIFIED-SECONDARY].
* **Bank capital and forced recognition.** NAMA's 57% average discount on €74 billion of loans and the Spanish provisioning decrees of February and May 2012 forced banks to recognize property losses [FACT; ch07-S11, S13]. Recognition reduces capital, which (Example 7.7) reduces lending capacity.
* **Lender exit.** Commerzbank's decision of 26 June 2012 to wind down Eurohypo's commercial real estate finance business removed one of Europe's largest CRE lenders from new lending. The bank cited Basel III capital and liquidity requirements [FACT; ch07-S16]. This is a bank-capital transmission, not a sovereign default.
* **Transfer to state vehicles at deep discounts.** Sareb's announced transfer discounts are a price for illiquid property collateral set in the middle of the crisis [FACT as reported; ch07-S12].

#### Competing interpretations

1. **Fundamental insolvency view.** Some sovereigns had debt levels and growth prospects that made debt unsustainable without restructuring. Greece was the clear case. On this view, high spreads were correct pricing of expected loss.
2. **Self-fulfilling crisis (multiple-equilibria) view.** A sovereign without its own central bank can be pushed into default by a rise in yields that itself makes the debt unsustainable. On this view, spreads for Italy and Spain in 2011–12 contained a large premium for a bad equilibrium that a credible lender of last resort could remove. The rapid fall in spreads after the ECB's statements is consistent with this view, although it does not prove it.
3. **Bank-centric view.** The crisis was primarily a banking crisis that became sovereign through guarantees and recapitalizations (Ireland most clearly, Spain later). The doom-loop literature (ch07-S24, S25) supports this view for those countries.

These views are not mutually exclusive. They differ country by country.

#### What the case establishes, and what it does not

**Establishes.** (i) Sovereign risk in a currency union transmits to domestic banks, property values, and CRE credit availability. (ii) Policy announcements by a credible central bank can change the risk premium in sovereign spreads without the bank actually buying bonds, at least as of 2015 for OMT. (iii) CRE losses can be recognized suddenly by regulatory decree, which is itself a market event.

**Does not establish.** It does not establish how much of the 2012 spread was expected default loss versus a self-fulfilling premium. It does not establish that a U.S. or U.K. sovereign could experience the same dynamics, since both have their own currencies and central banks. It does not tell you the price at which a Madrid office should have been bought in June 2012; that requires underwriting the specific asset (Example 7.8) and a view on policy.

#### Strategies available then (ex ante)

* Buy discounted CRE or loans from forced sellers, sized so that a further 20–30% fall in value does not impair the fund. This is a speculation on policy and on liquidity premia.
* Provide rescue capital (preferred equity, mezzanine) where the refinancing gap is large and the senior lender is capital-constrained.
* Buy short-dated sovereign bonds as a speculation on a central-bank backstop. This had large tail risk until the OMT announcement.
* Wait. Abstention had a real option value, because the policy uncertainty was going to resolve within months.

---

### 7.10 Decision exercise: the Madrid office, late June 2012

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

### 7.11 Frequent analytical errors

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

### 7.12 Connections to other chapters

* **Chapter 5** develops central-bank reaction functions. The ECB's 2012 actions are a central bank acting as lender of last resort under legal constraints.
* **Chapter 6** develops duration, DV01, and the cap-rate/Treasury spread used in Examples 7.3 and 7.8.
* **Chapter 10** develops loan sizing (LTV, DSCR, debt yield) and refinancing gaps used in Example 7.8.
* **Chapter 12** develops distressed CRE opportunity, loan sales, and maturity walls, including rescue capital.
* **Chapter 15** develops FX in depth: quote conventions, carry trades, and hedged returns on foreign property.
* **Chapter 17** develops hazard rates, recovery, and spread ≈ PD × LGD for corporate and CMBS credit.
* **Chapter 23** examines the ERM crisis of 1992 (a peg under the trilemma), Asia 1997, and 2022 in detail.
* **Case H** (cross-asset macro shock) applies the chapter's transmission channels to a multi-asset portfolio.

---

### 7.13 One-page reference sheet

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

### References for this chapter

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


\newpage


# Part III — Commercial Real Estate as a Speculative Asset

## Chapter 8 — The Fundamental Economics of CRE

> **Status:** Complete (v1.0). All numerical examples, problems, and solutions are reproduced in `tests/test_ch08_examples.py`. Problems are in `problems/questions/ch08_problems.md`, solutions in `problems/solutions/ch08_solutions.md`, drills D026–D035 in `training/daily_drills/drill_bank_ch08.json`. Historical facts in §8.9 are registered in `references/sources_ch08.md`; items still open are marked *(verification pending)*.

### Learning objectives

After this chapter you should be able to:

1. Build income from a rent roll through the full waterfall (potential gross income, effective gross income, net operating income, net cash flow) and say for every line item where it belongs and why.
2. Separate cash flow from accounting earnings. Quantify the effect of depreciation, straight-line rent, free rent, and capitalized tenant improvements, and reprice an asset whose marketed NOI is not cash.
3. Distinguish physical, leased, and economic occupancy, and compute net effective rent on a concession-laden lease.
4. Measure operating leverage by property type, and show why a hotel's NOI responds differently to a rate decline than to an occupancy decline.
5. Read a rent roll as a risk document: weighted average lease term, rollover concentration, and mark-to-market.
6. Forecast vacancy in a submarket from inventory, pipeline, and absorption, and convert the result into months of supply.
7. Use replacement cost correctly: as a test of whether new supply can enter, not as a value floor.
8. Value assets under property-tax reassessment with the loaded cap rate, and contrast market-value regimes (Texas) with acquisition-value regimes (California Proposition 13).
9. Price deferred maintenance and distinguish capital expenditure from replacement reserves.
10. Compare hotels, multifamily, office, retail, industrial, land, and specialty property on lease duration, operating leverage, capital intensity, cash-flow volatility, and liquidity, and translate each difference into a pricing or sizing consequence.

---

### 8.1 Opening investment problem: four offering memoranda, four different "NOIs"

You allocate capital for a regional family office with a \$40 million CRE sleeve. On Tuesday four broker packages arrive. Each leads with a single number: NOI capitalized at a cap rate. All facts below are [HYPOTHESIS], a constructed teaching case.

| Asset | Broker's headline | Implied price |
|---|---|---|
| **Oak Hollow**, 48,000 sf grocery-anchored neighborhood retail center | "In-place NOI \$575,000; 7.0% cap" | \$8.2 million |
| **Lakeside Plaza**, 120,000 rsf multi-tenant suburban office | "90% leased; NOI \$1.8 million; 8.0% cap" | \$22.5 million |
| **Interstate select-service hotel**, 150 rooms | "NOI \$1.43 million after 4% FF&E reserve; 9.0% cap" | \$15.9 million |
| **Cedar Court**, 200-unit garden apartments built in the 1980s | "T-12 NOI \$1.45 million; 6.0% cap" | \$24.2 million |

The four headlines look comparable. They are not. One "NOI" is before a reserve and was produced by skipping maintenance. One counts rent that tenants are not paying. One sits on top of fixed costs that will turn a 10% revenue decline into a 20–30% NOI decline. One depends on an anchor whose lease is eight years long while a third of the rest of the rent roll expires within two years. And every one of them carries a property-tax bill that will change when you buy.

This chapter teaches you to take each headline apart. By §8.10 you will reprice all four and decide which deserves diligence money.

---

### 8.2 Economic intuition

#### Real estate is a claim on the cash flows of space

A building is a machine that converts space, location, and services into rent. The owner's claim is residual: rent, less the costs of keeping the space rentable, less the share of value claimed by local government through property tax, less the capital needed to keep the machine from wearing out. Value is the present value of that residual claim. Everything in this chapter is about measuring the residual correctly and understanding what makes it volatile.

Three features distinguish CRE cash flows from corporate earnings.

1. **Contracts allocate risk between owner and occupant.** A lease is not just a price. It decides who bears operating-cost inflation (gross versus net leases), who bears demand risk (term length), and who bears capital risk (tenant improvement allowances, repair clauses). A 15-year absolute-net lease to a creditworthy tenant is economically close to a bond with a real estate residual. A hotel "lease" is one night long, so the owner bears everything. The same building can be either, depending on the lease.
2. **Supply is slow and lumpy.** New space takes two to four years to entitle and build [HYPOTHESIS: typical range; varies by type and jurisdiction]. Developers start projects on today's rents and deliver into tomorrow's market. Absorption, the net change in occupied space, adjusts faster than supply. That timing mismatch produces the boom–bust pattern in vacancy that §8.9 documents for Texas in the 1980s.
3. **Value is anchored, loosely, by replacement cost.** When the value of existing buildings rises well above the cost of building new ones, developers build, and the new supply pulls rents and values back. When value is below replacement cost, nothing new is built, and existing owners are protected from new competition until demand catches up. Replacement cost is a long-run attractor for value, not a floor under it.

#### The space market and the asset market

It helps to keep two markets separate. In the **space market**, occupants rent space; rent and vacancy are set by the demand for space relative to the stock. In the **asset market**, investors buy claims on rent; cap rates are set by interest rates, risk premia, and expected growth. The construction sector links them: when asset prices exceed replacement cost, new space is built, which feeds back into the space market. This four-part framing is associated with DiPasquale and Wheaton (1992) *(bibliographic verification pending)*. Its practical use is diagnostic. When a value rises, ask which market moved. A rent increase driven by low vacancy is vulnerable to supply. A cap-rate decline driven by cheap debt is vulnerable to rates. They fail in different ways and on different clocks.

#### Operating leverage

Operating leverage is the ratio of fixed costs to revenue. A building whose costs are mostly fixed sees NOI move more than revenue. Net-leased industrial has almost no landlord costs, so NOI moves one-for-one with rent. A select-service hotel carries labor, utilities, franchise systems, and maintenance that do not fall when occupancy falls, so NOI moves two to three times as much as revenue. Operating leverage multiplies with financial leverage (Chapter 10): a 10% revenue decline that becomes a 25% NOI decline becomes a 71% equity decline at 65% LTV ($25\% / 0.35$) if cap rates do not move, and cap rates usually do move.

#### Cash flow is not earnings

Accounting earnings smooth what cash does not. Straight-line rent recognizes free-rent months as revenue. Tenant improvements are capitalized and amortized instead of expensed. Depreciation is charged on a building that may be appreciating. None of that is wrong for financial reporting, but a buyer pays for cash, and a lender is repaid in cash. The analyst's first job with any income statement is to put each line on a cash basis and then decide which cash is recurring.

#### Taxes, capital, and liquidity are claims too

Local government claims a share of value through property tax. In a market-value regime the claim resets to whatever you pay, so the tax line is a function of your bid. The physical building claims a share of cash through capital expenditure; a seller who stops paying that claim inflates NOI and leaves the bill for you. And the market claims a share of value whenever you need to transact quickly. These are the three most common sources of a gap between marketed NOI and the cash a buyer will actually receive.

---

### 8.3 Technical definitions

| Term | Definition |
|---|---|
| Potential gross income (PGI) | Rent the property would collect if 100% leased: in-place contract rent on occupied space plus market rent on vacant space, plus potential expense recoveries |
| Vacancy loss | PGI attributable to unleased space (and, in underwriting, a general allowance for future vacancy) |
| Credit loss | Rent billed but not collected; usually a percentage of income after vacancy |
| Expense recoveries (reimbursements) | Operating expenses billed back to tenants under net or modified-gross leases |
| Effective gross income (EGI) | PGI − vacancy − credit loss + other income |
| Operating expenses (OpEx) | Recurring costs of operating the property: taxes, insurance, utilities, repairs and maintenance, payroll, management, common-area maintenance (CAM). Excludes debt service, depreciation, income tax, and capital items |
| Net operating income (NOI) | EGI − OpEx. **In this chapter NOI is before replacement reserves and leasing costs**, which is the market convention for office, retail, industrial, and multifamily. This is a departure from the notation guide's default; hotels follow the guide's USALI convention, with NOI after the FF&E reserve |
| Net cash flow (NCF) | NOI − replacement reserves − normalized tenant improvements and leasing commissions (TI/LC). Lenders size on NCF |
| Expense ratio | OpEx ÷ EGI |
| Physical occupancy | Occupied area ÷ rentable area |
| Leased occupancy | Area under signed leases ÷ rentable area (includes signed-not-occupied and "dark" tenants) |
| Economic occupancy | Rent actually collected ÷ rent collectible at 100% occupancy at the same rents |
| Net effective rent (NER) | Level annual rent with the same present value as the lease's contractual cash rent less landlord concessions (free rent, TI, LC) |
| Straight-line rent | GAAP revenue recognition that spreads total contractual rent evenly over the lease term, including free-rent periods |
| WALT | Weighted average lease term remaining, weighted by rent (or area) |
| Mark-to-market | (Market rent − contract rent) on leases, in \$ or as a % of contract rent |
| Net absorption | Change in occupied space over a period (move-ins − move-outs) |
| Months of supply | (Vacant space + speculative space under construction) ÷ monthly net absorption |
| Replacement cost | Cost to build an equivalent new property today, including land, hard and soft costs, and (in the "with profit" version) a developer's margin |
| Yield on cost | Stabilized NOI ÷ total development cost |
| Loaded cap rate | $c + t$, where $t$ = property tax as a fraction of value; used when tax is reassessed at the purchase price |
| Replacement reserve | A periodic allowance (per unit, per sf, or % of revenue) for recurring capital replacement |
| Deferred maintenance | Capital or repair work past due at the date of sale |
| Operating leverage (DOL) | Percentage change in NOI per 1% change in revenue |

---

### 8.4 Equations and derivations

#### 8.4.1 The income waterfall and what belongs where

$$\text{EGI} = \text{PGI} - \text{Vacancy} - \text{Credit loss} + \text{Other income}$$
$$\text{NOI} = \text{EGI} - \text{OpEx}, \qquad \text{NCF} = \text{NOI} - \text{Reserves} - \text{TI/LC}$$

Each line answers a different question. PGI asks what the rent roll could produce. EGI asks what it does produce. NOI asks what the real estate earns before capital and financing. NCF asks what a lender or owner can actually spend. The classification rules below are where most marketing packages and many internal models go wrong.

| Item | Belongs in | Reason |
|---|---|---|
| Base rent on occupied space | PGI | Contractual income |
| Market rent on vacant space | PGI, then deducted as vacancy | Shows the cost of vacancy explicitly |
| CAM, tax, and insurance reimbursements | PGI (potential recoveries) | Income, offset by the expenses they reimburse |
| Parking, storage, antenna, laundry income | Other income in EGI | Recurring operating income; test its durability |
| Lease termination fee | Exclude from NOI | Non-recurring; it is capital returned for lost future rent |
| Insurance proceeds | Exclude | Non-operating (Case A) |
| Property management fee | OpEx | A market cost even if the owner self-manages |
| Asset management or fund fee | Below NOI | An owner's cost, not the property's |
| Property tax, insurance, utilities, R&M, payroll | OpEx | Recurring operating costs |
| Ground rent | OpEx (or a separate line above NCF) | A senior claim on property cash flow; state treatment |
| Roof replacement, parking-lot resurfacing, HVAC units | Capital, below NOI | Non-recurring in any one year; recurring over the life of the asset, which is what reserves are for |
| Tenant improvements and leasing commissions | Below NOI, in NCF | Costs of acquiring rent; lumpy, tied to rollover |
| Replacement reserve | Below NOI, in NCF (hotel: above NOI per USALI) | An allowance, not a cash payment unless escrowed |
| Debt service | Below NCF | Financing, not operations |
| Depreciation and amortization | Never in NOI | Non-cash accounting allocations |
| Straight-line rent adjustment | Never in NOI | Non-cash; reverse it to get cash rent |
| Owner's income tax | Never in NOI | Depends on the owner, not the asset |

#### 8.4.2 Three occupancy measures

Let $A$ be rentable area, $A_{occ}$ occupied area, $A_{lsd}$ leased area, and $r_i$ the contract rent on suite $i$. Then

$$\text{Physical occ.} = \frac{A_{occ}}{A}, \qquad \text{Leased occ.} = \frac{A_{lsd}}{A}, \qquad \text{Economic occ.} = \frac{\sum_i \text{cash rent collected}_i}{\sum_i r_i A_i + \sum_{\text{vacant}} r^{mkt} A_j}.$$

Leased occupancy exceeds physical occupancy when tenants have signed but not moved in, or have moved out but still pay ("dark" tenants). Economic occupancy falls below leased occupancy when tenants are in free-rent periods, in default, or paying below-market rent. A dark tenant is a warning: a tenant who pays for space it does not use is likely to leave at expiry or to seek a buyout. Free rent is a deferred concession: it is a cost the landlord has already agreed to bear.

#### 8.4.3 NOI growth is levered rent growth

Write NOI $= R - E$ with revenue $R$ growing at $g_R$ and expenses $E$ growing at $g_E$. Then

$$g_{NOI} = \frac{\Delta R - \Delta E}{R - E} = g_R \frac{R}{NOI} - g_E \frac{E}{NOI}.$$

With $R = 100$, $E = 40$, $g_R = 3\%$, $g_E = 4\%$: $g_{NOI} = 3\% \times 1.667 - 4\% \times 0.667 = 5.00\% - 2.67\% = 2.33\%$. Rent growth above expense growth is magnified, and expense growth above rent growth is magnified in the other direction. The higher the expense ratio, the larger both multipliers. Net leases cut the link: if expenses are fully recovered, $E$ falls out of the landlord's equation and $g_{NOI} \approx g_R$. This is the formal reason that property taxes and insurance, which in recent years have in many markets grown faster than rents [HYPOTHESIS for any specific market; verify locally], matter much more to gross-lease office and to multifamily than to net-leased industrial.

#### 8.4.4 Operating leverage

Split costs into fixed $F$ and variable $vR$. Then NOI $= R(1-v) - F$ and

$$\frac{\Delta NOI}{NOI} = \frac{(1-v)\Delta R}{R(1-v) - F} = \frac{\Delta R}{R}\times \underbrace{\frac{R(1-v)}{NOI}}_{DOL}.$$

DOL is contribution margin divided by NOI. It equals 1 when there are no fixed costs and rises without bound as NOI approaches zero. `sdesk.cre.operating_leverage` implements it.

For hotels, revenue changes through two channels with different variable costs. A **rate** (ADR) change carries only percentage-of-revenue costs (fees, reserve, credit-card commissions), so the flow-through to NOI is high. An **occupancy** change also carries cost per occupied room (housekeeping, laundry, amenities, breakfast), so flow-through is lower. Equal RevPAR declines therefore do *not* produce equal NOI declines. A rate-led decline is worse for NOI, and it is also slower to reverse, because ADR rebuilds after occupancy does [HYPOTHESIS: a common operator observation; Chapter 11 examines evidence].

#### 8.4.5 Rent rolls: WALT, rollover, mark-to-market, and net effective rent

For leases $i$ with annual contract rent $R_i$, area $A_i$, and remaining term $T_i$:

$$WALT_R = \frac{\sum_i R_i T_i}{\sum_i R_i}, \qquad WALT_A = \frac{\sum_i A_i T_i}{\sum_i A_i}.$$

$$\text{Rollover}(h) = \frac{\sum_{i: T_i \le h} R_i}{\sum_i R_i}, \qquad MTM = \sum_i A_i \left(r^{mkt}_i - r_i\right).$$

WALT is an average and hides concentration. A center whose anchor has eight years left can show a five-year WALT while most of its small-shop rent turns over within two years. Always compute WALT with and without the largest tenant, and the rollover share at 12, 24, and 36 months.

**Net effective rent.** For a lease of $n$ years with cash rent $CR_t$ in year $t$ (after free rent), TI and LC paid at signing, and discount rate $k$:

$$NER = \frac{\sum_{t=1}^{n} CR_t (1+k)^{-t} - TI - LC}{a_{\overline{n}|k}}, \qquad a_{\overline{n}|k} = \frac{1-(1+k)^{-n}}{k}.$$

NER is the level rent with the same present value as the landlord's net receipts. Face rent is a marketing number; NER is the economic rent. We use annual-in-arrears timing for transparency. A monthly model raises the PV of rent slightly and changes no conclusion here.

#### 8.4.6 Supply, absorption, and vacancy

Let $S_t$ be inventory, $V_t$ vacant space, $C_t$ completions, and $AB_t$ net absorption over a period. Then

$$V_{t+1} = V_t + C_t - AB_t, \qquad S_{t+1} = S_t + C_t, \qquad v_{t+1} = \frac{V_{t+1}}{S_{t+1}}.$$

**Months of supply** compares what is available with the pace of demand:

$$MOS = \frac{V_t + C^{spec}}{AB^{monthly}},$$

where $C^{spec}$ is speculative (not pre-leased) space under construction. Pre-leased space should not be counted as supply because it is already committed. Its move-ins *do* count in net absorption when the buildings deliver. Analysts who count pre-leased deliveries as supply and also exclude their move-ins from absorption double-penalize the market. Those who count the move-ins as absorption without asking whether the tenants vacated other space in the same submarket double-credit it.

A simple rent-adjustment rule links vacancy to rent growth:

$$g_{rent,t+1} = g^* - \beta (v_t - v^*),$$

where $v^*$ is the "natural" vacancy rate at which real rents are stable. Rents rise when vacancy is below $v^*$ and fall when it is above. This specification is associated with Rosen (1984) and Wheaton and Torto (1988) *(bibliographic verification pending)*. Its parameters differ by market and must be estimated. In this chapter $g^*$, $\beta$, and $v^*$ are [HYPOTHESIS].

#### 8.4.7 Replacement cost and the entry condition

Let $H$ be hard cost, $S$ soft cost, and $L$ land, all per unit of space, and let $m$ be the developer's required margin on cost. Then cost $= H + S + L$ and replacement cost with profit $= (H+S+L)(1+m)$. New supply enters when

$$\frac{NOI^{new}}{H+S+L} \;\ge\; c + s \quad\Longleftrightarrow\quad \frac{V^{new}}{H+S+L} = \frac{NOI^{new}/c}{H+S+L} \;\ge\; 1 + \frac{s}{c},$$

where $s$ is the required development spread over the market cap rate and $c$ the cap rate at which a stabilized new building sells. The required rent for feasibility is

$$r^{req} = \frac{(c+s)(H+S+L)}{(1-v)(1-e)},$$

where $v$ is the stabilized vacancy allowance and $e$ the share of revenue lost to non-recoverable costs. When market rent is below $r^{req}$, new construction is not feasible, and existing assets are protected from new competition for at least the length of the construction cycle once the gap closes. That protection is worth something. It is not the same as saying the asset is "worth" replacement cost.

#### 8.4.8 Property tax: the loaded cap rate and acquisition-value regimes

**Market-value regime.** If the assessor resets taxable value to the purchase price, tax is $tV$, where $t$ is the combined tax rate times the assessment ratio. With pre-tax NOI $N$ and market cap rate $c$ on after-tax NOI,

$$V = \frac{N - tV}{c} \;\Rightarrow\; V = \frac{N}{c+t}.$$

This is the loaded cap rate of Case A and `sdesk.cre.loaded_cap_value`. Capitalizing the seller's (stale) tax bill instead overstates value by

$$\Delta V = \frac{N - T^{seller}}{c} - \frac{N}{c+t} ,$$

which grows with the gap between the old assessment and the price.

**Acquisition-value regime.** Under California's Proposition 13 the general levy is limited to 1% of taxable value plus voter-approved debt and certain assessments. Taxable value is the base-year value, set at a change in ownership or completion of new construction, and adjusted annually by inflation of no more than 2% [FACT; California State Board of Equalization and county assessor publications; VERIFIED-SECONDARY]. For a buyer, the base year resets to the purchase price, so the loaded-cap logic still applies at acquisition: $V = N/(c + t_{CA})$, with $t_{CA}$ = 1% plus the local debt rate. What differs is what happens *after* acquisition. While market value grows at $g_V$ and taxable value at most at 2%, tax as a share of market value after $n$ years is

$$t_n = t_{CA} \left(\frac{1.02}{1+g_V}\right)^{n}.$$

That drift belongs to the owner and disappears at the next sale. A long-held California asset therefore shows an unusually low tax bill, and its "cap rate" on the seller's NOI is not comparable to anything a buyer can obtain.

**Texas.** Texas appraisal districts appraise property at market value as of 1 January each year, and each taxing unit sets its own rate [FACT; Texas Property Tax Code §1.04 and §23.01 as summarized by county appraisal districts; VERIFIED-SECONDARY]. For tax years 2024 through 2026, a temporary "circuit breaker" limits annual increases in appraised value to 20% for non-homestead real property valued at or below an inflation-indexed threshold (\$5 million for 2024), but only after the owner has held the property for a full prior year [FACT; Tax Code §23.231 as published by appraisal districts; VERIFIED-SECONDARY]. Whether it is extended beyond 2026 is *(verification pending)*. For a buyer of an institutional-size asset, the relevant model is reassessment toward the price. Texas does not require public disclosure of sale prices, so appraisal districts may learn the price with a lag, or through the owner's protest, rather than at closing [INFERENCE consistent with Case A; the timing in any given county is an empirical question]. A prudent buyer underwrites full reassessment in year one and treats any lag as upside.

#### 8.4.9 Capital expenditure versus reserves

A replacement reserve is a **budgeting allowance**: an estimate of the average annual cost of replacing short-lived components. Capital expenditure is **cash**. They match only on average over a long horizon. A property sold after years of deferred maintenance has a capital need concentrated at the start of the new owner's hold. Price it as

$$P = \frac{NOI^{norm} - \text{Reserve}}{c} - (1+\kappa)\,\text{Immediate capex} - \sum_{t=1}^{n} \frac{X_t - \text{Reserve}}{(1+k)^t},$$

where $NOI^{norm}$ normalizes operating repairs to market levels, $\kappa$ is a contingency, and $X_t$ is the scheduled catch-up capex in years $1..n$ in excess of the reserve. The perpetual reserve is already in the capitalized income. Only the excess is deducted, so nothing is counted twice.

#### 8.4.10 Liquidity: the annualized cost of transacting

With buyer costs $b$ and seller costs $s$ (as fractions of price) and a hold of $T$ years, round-trip costs reduce the annualized return by approximately

$$\text{drag} = 1 - \left(\frac{1-s}{1+b}\right)^{1/T}.$$

With $b = 1.5\%$, $s = 2.5\%$, and $T = 5$: drag $= 1 - (0.975/1.015)^{0.2} = 0.80\%$ per year. Halve the hold and the drag roughly doubles. Illiquidity also has a time dimension that this formula ignores: the months needed to sell, during which the seller is exposed to price changes and cannot redeploy capital. For hotels, land, and special-purpose assets, the buyer pool is thinner and the time to sell is longer than for apartments or industrial [HYPOTHESIS: practitioner observation; transaction-volume data by type would test it].

---

### 8.5 Worked examples

All seven examples use hypothetical inputs [HYPOTHESIS] and are reproduced in `tests/test_ch08_examples.py`.

#### Example 8.1 — From rent roll to NCF: Oak Hollow retail center

**Given.** A 48,000 sf neighborhood center. Leases are triple-net (NNN): tenants reimburse their pro-rata share of CAM (\$3.00/sf), real estate taxes (\$2.50/sf), and insurance (\$0.75/sf), a total of \$6.25/sf, or \$300,000 for the building. The anchor's lease caps its CAM contribution at \$2.00/sf. One 6,000 sf suite is vacant, with market rent \$22.00/sf. Credit loss is 1.0% of income after vacancy. Other income (a kiosk and a cell antenna) is \$6,000. Management is 4.0% of EGI and is not recoverable. Other non-recoverable costs are \$18,000. Replacement reserve \$0.20/sf on the whole GLA; normalized TI/LC \$1.25/sf on the 26,000 sf of non-anchor space (shop space plus the vacant suite).

| Tenant | Area (sf) | Rent (\$/sf) | Annual rent | Years remaining | Market rent (\$/sf) |
|---|---:|---:|---:|---:|---:|
| Anchor grocer | 22,000 | 12.00 | 264,000 | 8.0 | 13.00 |
| Fitness | 8,000 | 16.00 | 128,000 | 4.5 | 15.00 |
| Restaurant | 4,000 | 28.00 | 112,000 | 2.0 | 30.00 |
| Salon | 1,500 | 26.00 | 39,000 | 0.5 | 28.00 |
| Dental | 3,500 | 24.00 | 84,000 | 3.0 | 25.00 |
| Mattress retailer | 3,000 | 22.00 | 66,000 | 1.0 | 22.00 |
| **Occupied** | **42,000** | | **693,000** | | |
| Vacant | 6,000 | — | — | — | 22.00 |

**Find.** PGI, EGI, NOI, NCF; the expense ratio; WALT by rent and by area, with and without the anchor; 24-month rollover; mark-to-market.

**Solution.**

*Potential gross income.* Base rent at 100% occupancy $= 693{,}000 + 6{,}000 \times 22 = \$825{,}000$. Potential recoveries $= 300{,}000 - 22{,}000 \times (3.00 - 2.00) = 300{,}000 - 22{,}000 = \$278{,}000$. PGI $= 825{,}000 + 278{,}000 = \$1{,}103{,}000$.

*Vacancy.* The vacant suite forgoes base rent $6{,}000 \times 22 = \$132{,}000$ and recoveries $6{,}000 \times 6.25 = \$37{,}500$: vacancy loss \$169,500, which is 15.37% of PGI. Physical occupancy is $42{,}000/48{,}000 = 87.5\%$, but the economic vacancy rate is higher because the vacant suite would pay above-average rent.

*EGI.* Income after vacancy $= 1{,}103{,}000 - 169{,}500 = \$933{,}500$. Credit loss $= 1\% \times 933{,}500 = \$9{,}335$. EGI $= 933{,}500 - 9{,}335 + 6{,}000 = \$930{,}165$.

*OpEx.* Recoverable expenses \$300,000 (the landlord pays them all and bills tenants); management $4\% \times 930{,}165 = \$37{,}207$; non-recoverable \$18,000. Total OpEx $= \$355{,}207$. Expense ratio $= 355{,}207/930{,}165 = 38.19\%$.

*NOI* $= 930{,}165 - 355{,}207 = \$574{,}958$.

*NCF.* Reserve $= 0.20 \times 48{,}000 = \$9{,}600$. TI/LC $= 1.25 \times 26{,}000 = \$32{,}500$. NCF $= 574{,}958 - 9{,}600 - 32{,}500 = \$532{,}858$.

*Unrecovered "recoverables".* The landlord pays \$300,000 of recoverable expenses and collects \$240,500 ($278{,}000 - 37{,}500$). The \$59,500 shortfall is the vacant suite's share (\$37,500) plus the anchor cap (\$22,000). A net lease is only as net as its least-net tenant.

*Rent roll risk.*

* $WALT_R = (264{,}000 \times 8 + 128{,}000 \times 4.5 + 112{,}000 \times 2 + 39{,}000 \times 0.5 + 84{,}000 \times 3 + 66{,}000 \times 1)/693{,}000 = 3{,}249{,}500/693{,}000 = 4.69$ years.
* $WALT_A = 234{,}250/42{,}000 = 5.58$ years.
* Excluding the anchor: $WALT_R = 1{,}137{,}500/429{,}000 = 2.65$ years.
* The anchor pays 38.1% of base rent.
* Rollover within 24 months (restaurant, salon, mattress): \$217,000, which is 31.3% of base rent.
* Mark-to-market: market rent on occupied space \$721,500 versus contract \$693,000, so leases are 4.11% (\$28,500) below market. But \$22,000 of that gap sits in the anchor lease, which does not roll for eight years. The mark-to-market realizable within 24 months is \$11,000.

**Check.** NOI rebuilt from the tenants' side: base rent collected 693,000 + recoveries 240,500 + other 6,000 − credit loss 9,335 = 930,165 = EGI. ✓ The broker's \$575,000 "in-place NOI" is our NOI, before reserves and TI/LC. The broker's price, \$8.2 million, is NOI/7.0% = \$8,213,691, and on NCF the same price is a 6.49% yield.

**Decision consequence.** The headline cap rate is computed on the wrong line for comparison with lender-underwritten deals, which use NCF. More important is the shape of the risk: the center is two different assets. One is an eight-year anchor lease at slightly below market, which behaves like a bond. The other is 26,000 sf of shop space and vacancy with a 2.65-year WALT, 31% of rent rolling in 24 months, and only \$11,000 of near-term mark-to-market to offset leasing costs. Underwrite the shop space with explicit downtime, TI/LC, and renewal probabilities (Chapter 9's DCF), and price the anchor's renewal option as a risk, not as an upside. A lender will also apply a market vacancy allowance to the shop space even if it is full.

*Reproduce:* `tests/test_ch08_examples.py::test_example_8_1`

#### Example 8.2 — Lakeside Plaza: physical, leased, and economic occupancy; cash versus GAAP

**Given.** A 120,000 rsf suburban office building with full-service gross leases at \$30.00/sf; building operating expenses of \$12.00/sf (\$1,440,000) are paid by the landlord. Of the space:

* 78,000 sf is occupied and paying \$30.00/sf;
* 30,000 sf is under new 10-year leases at \$30.00/sf flat, signed this month, with 12 months of free rent, a \$60/sf TI allowance, and leasing commissions of 6% of aggregate cash rent, all paid at signing;
* 6,000 sf of the 78,000 sf paying tenant base is "dark": the tenant has moved out but pays rent until expiry;
* 12,000 sf is vacant.

Discount rate for NER: 8%. Annual cash flows in arrears.

**Find.** The three occupancy measures; cash NOI for the coming year; the "contract" NOI the broker capitalized; straight-line NOI; the NER of the new leases; and the year-1 difference between cash and GAAP for the new-lease block.

**Solution.**

*Occupancy.* Leased $= (78{,}000 + 30{,}000)/120{,}000 = 90.0\%$. Physically occupied space excludes the dark suite and includes the new tenants, who move in now: $(78{,}000 - 6{,}000 + 30{,}000)/120{,}000 = 85.0\%$. Economic occupancy in the coming year $= 78{,}000 \times 30/(120{,}000 \times 30) = 65.0\%$.

*Three NOIs for the same year.*

| Basis | Rent | − OpEx | NOI |
|---|---:|---:|---:|
| Cash (what will be collected) | $78{,}000 \times 30 = 2{,}340{,}000$ | 1,440,000 | **900,000** |
| Straight-line (GAAP) | $2{,}340{,}000 + 30{,}000 \times 27 = 3{,}150{,}000$ | 1,440,000 | **1,710,000** |
| "Contract" (broker) | $108{,}000 \times 30 = 3{,}240{,}000$ | 1,440,000 | **1,800,000** |

Straight-line rent on the new leases is total cash rent over the term divided by the term: $(9 \times 30)/10 = \$27.00$/sf per year, recognized even in the free-rent year.

*Net effective rent of the new leases (per sf).* Aggregate face rent \$300; free rent \$30; cash rent \$270; LC $= 6\% \times 270 = \$16.20$.

* Undiscounted NER $= (270 - 60 - 16.20)/10 = \$19.38$.
* PV of cash rent (years 2–10 at \$30): $30 \times (a_{\overline{10}|8\%} - 1.08^{-1}) = 30 \times (6.71008 - 0.92593) = \$173.52$.
* Discounted NER $= (173.52 - 60 - 16.20)/6.71008 = \$14.50$/sf per year, **48.3% of face rent**.

*Cash versus GAAP for the 30,000 sf block in year 1.* Cash: rent 0; TI $-\$1{,}800{,}000$; LC $-\$486{,}000$; net $-\$2{,}286{,}000$. GAAP: straight-line revenue \$810,000; TI amortization $-\$180{,}000$ (\$6/sf over 10 years); LC amortization $-\$48{,}600$; net $+\$581{,}400$. The difference is \$2,867,400 in a single year.

**Check.** Over ten years straight-line and cash rent agree: $10 \times 27 = 270 = 9 \times 30$. ✓ TI amortization sums to the TI paid. ✓ The differences are purely timing, and timing is what a buyer pays for.

**Decision consequence.** The broker's \$22.5 million is the contract NOI at 8.0%. A buyer who closes today inherits the 12 months of free rent (\$900,000 of foregone cash) unless the seller credits it at closing; a credit reduces the price to \$21.6 million on the broker's own cap rate. The building's cash NOI next year supports only \$11.25 million at the same cap rate. The truth for value lies between, and Chapter 9's DCF finds it. The economic lesson is that the market rent of \$30 is not the economic rent. The landlord is effectively leasing at \$14.50 after concessions. Comparable sales whose cap rates were computed on face rents will overstate what this market pays for office income. The 6,000 sf dark suite should be underwritten as vacant at its expiry, and a lender will treat it that way.

*Reproduce:* `tests/test_ch08_examples.py::test_example_8_2`

#### Example 8.3 — Operating leverage: select-service hotel versus a net-leased building under a 10% revenue shock

**Given.** *Hotel:* 150 rooms, 72% occupancy, \$140 ADR, 365 days. Other revenue 6% of rooms revenue. Rooms cost per occupied room (CPOR) \$32. Other departmental expense ratio 60%. Undistributed expenses: \$1,350,000 fixed plus 4% of total revenue. Management fee 3% of total revenue; franchise fees 10% of rooms revenue. Property tax \$260,000; insurance \$150,000. FF&E reserve 4% of total revenue (NOI after reserve, per the notation guide). Cap rate 9.0%.
*Net-lease building:* \$1,000,000 of rent; landlord's non-recoverable costs \$20,000 fixed. Cap rate 6.5%.
Both are financed at 65% LTV. Cap rates are held constant to isolate operating leverage.

**Find.** NOI and value before and after a 10% revenue decline; for the hotel, compare a decline led by ADR with one led by occupancy; equity impact at 65% LTV.

**Solution (hotel base case, via `sdesk.hotel.operating_statement`).**

| Line | Base | ADR −10% | Occupancy −10% |
|---|---:|---:|---:|
| Occupancy / ADR | 72.0% / \$140 | 72.0% / \$126 | 64.8% / \$140 |
| Rooms sold | 39,420 | 39,420 | 35,478 |
| Rooms revenue | 5,518,800 | 4,966,920 | 4,966,920 |
| Total revenue | 5,849,928 | 5,264,935 | 5,264,935 |
| Rooms expense | 1,261,440 | 1,261,440 | 1,135,296 |
| GOP | 2,805,814 | 2,264,089 | 2,390,233 |
| Management + franchise | 727,378 | 654,640 | 654,640 |
| EBITDA | 1,668,436 | 1,199,449 | 1,325,593 |
| FF&E reserve | 233,997 | 210,597 | 210,597 |
| **NOI** | **1,434,439** | **988,851** | **1,114,995** |
| NOI change | — | −31.06% | −22.27% |
| NOI flow-through on lost revenue | — | 76.2% | 54.6% |

Base GOP margin is 48.0% and NOI margin 24.5%. Value at 9.0% $= \$15{,}938{,}212$.

*Net lease (via `sdesk.cre.operating_leverage`).* NOI $= 1{,}000{,}000 - 20{,}000 = 980{,}000$. After a 10% rent decline, NOI $= 880{,}000$, a change of −10.20%. DOL $= 1{,}000{,}000/980{,}000 = 1.02$.

*Equity at 65% LTV.* With debt fixed, the percentage change in equity is the value change divided by 0.35:

| Asset | Value change | Equity change |
|---|---:|---:|
| Net lease | −10.20% | −29.15% |
| Hotel, occupancy-led | −22.27% | −63.63% |
| Hotel, ADR-led | −31.06% | −88.75% |

**Check.** Occupancy-led flow-through: the lost 3,942 room-nights save $3{,}942 \times 32 = \$126{,}144$ of rooms expense, and the rest of the lost revenue flows through at the percentage-cost margin. ADR-led: no rooms cost is saved. The two NOIs differ by exactly \$126,144 ($1{,}114{,}995 - 988{,}851$). ✓

**Decision consequence.** "A 10% revenue decline" is not one number for a hotel. A rate war that cuts ADR by 10% costs a third of NOI; the same RevPAR loss through occupancy costs a fifth. At 65% LTV the ADR-led shock nearly eliminates equity even before cap rates widen, and in a hotel downturn they do widen. The net-leased building's DOL near 1 does not make it riskless: its revenue risk is concentrated in one tenant's credit and renewal, so its revenue distribution is close to binary (rent paid or building dark) rather than continuous. Size hotel leverage to survive a rate-led decline with wider cap rates (Chapter 11), and size net-lease leverage to survive the loss of the tenant (Chapter 10).

*Reproduce:* `tests/test_ch08_examples.py::test_example_8_3`

#### Example 8.4 — Months of supply and a vacancy forecast for an industrial submarket

**Given.** Inventory 40.0 million sf; vacancy 7.5%. Under construction: 4.0 million sf, all delivering within 12 months, 30% pre-leased. Trailing-12-month net absorption 3.6 million sf (300,000 sf per month). Your base case: absorption slows to 200,000 sf per month as e-commerce occupiers pause. Natural vacancy $v^* = 7.5\%$. Rent rule $g = 3.0\% - 0.8\,(v - 7.5\%)$ [HYPOTHESIS for both].

**Find.** Months of supply at each absorption pace; vacancy in 12 months; months needed after that to return to 7.5%; implied rent growth.

**Solution.**

Vacant space $= 0.075 \times 40.0 = 3.0$ million sf. Speculative pipeline $= 4.0 \times 0.70 = 2.8$ million sf.

| | Trailing pace | Base case |
|---|---:|---:|
| Monthly absorption (m sf) | 0.30 | 0.20 |
| Months of supply $= (3.0 + 2.8)/AB$ | 19.3 | 29.0 |
| Vacant space in 12 months $= 3.0 + 4.0 - 12 \times AB$ | 3.4 | 4.6 |
| Inventory in 12 months | 44.0 | 44.0 |
| Vacancy in 12 months | 7.73% | 10.45% |
| Excess over 7.5% ($0.075 \times 44.0 = 3.3$) | 0.1 | 1.3 |
| Further months to return to 7.5% (no new starts) | 0.3 | 6.5 |
| Rent growth from the rule | 2.82% | 0.64% |

Absorption here includes the move-ins of pre-leased tenants (1.2 million sf), which is consistent with counting the whole 4.0 million sf of completions in the vacancy identity.

**Check.** At the trailing pace, 12 months absorb 3.6 million sf against 4.0 million sf of completions, so vacant space rises by 0.4 million sf (3.0 → 3.4); vacancy rises only 23 bp because inventory also grows. ✓

**Decision consequence.** The market's headline vacancy of 7.5% says nothing about the next year. What matters is the pipeline relative to the demand pace. A one-third slowdown in absorption moves 12-month vacancy from 7.7% to 10.5% and rent growth from about 2.8% to about 0.6% under the rule. An acquisition priced on 3% rent growth is therefore a bet on absorption holding at the trailing pace. Before bidding, verify three things: whether pre-leased tenants are relocating within the submarket (if so, net absorption is overstated and vacancy will be higher); whether any announced projects have not yet started (if starts continue, the excess persists); and what the leasing pipeline of the specific competing buildings shows.

*Reproduce:* `tests/test_ch08_examples.py::test_example_8_4`

#### Example 8.5 — Deferred maintenance capitalized into price: Cedar Court apartments

**Given.** 200 units. Seller's T-12 NOI \$1,450,000, before reserves. The property condition assessment (PCA) finds that repairs and maintenance were underspent by \$80,000 a year relative to comparable properties. It identifies \$1,200,000 of immediate needs (roofs, boilers, life-safety items) and \$400,000 a year of scheduled replacements in years 1–5 (windows, unit HVAC). A market replacement reserve is \$300 per unit per year. Market cap rate 6.0% on NOI after reserves. Contingency on immediate work 10%. Discount rate for catch-up capex 8%.

**Find.** Normalized NOI and NCF; the stabilized value; the deduction for capital catch-up; the price; the gap from the broker's \$24.2 million.

**Solution.**

* Normalized NOI $= 1{,}450{,}000 - 80{,}000 = \$1{,}370{,}000$.
* Reserve $= 300 \times 200 = \$60{,}000$. NCF $= \$1{,}310{,}000$.
* Stabilized value $= 1{,}310{,}000/0.06 = \$21{,}833{,}333$.
* Immediate capex with contingency $= 1{,}200{,}000 \times 1.10 = \$1{,}320{,}000$.
* Catch-up in excess of the reserve: $400{,}000 - 60{,}000 = \$340{,}000$ a year for 5 years. PV $= 340{,}000 \times a_{\overline{5}|8\%} = 340{,}000 \times 3.99271 = \$1{,}357{,}521$.
* Price $= 21{,}833{,}333 - 1{,}320{,}000 - 1{,}357{,}521 = \$19{,}155{,}812$, or \$95,779 per unit.

Broker's price $= 1{,}450{,}000/0.06 = \$24{,}166{,}667$ (\$120,833 per unit). The gap is \$5,010,855, or 20.7% of the broker's price.

**Check.** Decompose the gap: reserve not deducted, $60{,}000/0.06 = \$1{,}000{,}000$; underspent R&M, $80{,}000/0.06 = \$1{,}333{,}333$; immediate capex \$1,320,000; excess catch-up \$1,357,521. Sum $= \$5{,}010{,}855$. ✓ At the broker's price the buyer's yield on NCF would be $1{,}310{,}000/24{,}166{,}667 = 5.42\%$ before any capex.

**Decision consequence.** Two of the four pieces of the gap are capitalized at the cap rate because they are permanent (the reserve and normal R&M); two are deducted dollar for dollar because they are one-time. Mixing these up is the most common error in pricing deferred maintenance. Capitalizing a one-time \$1.32 million roof bill at 6% would deduct \$22 million. Ignoring the R&M normalization would leave \$1.33 million of value that does not exist. Negotiate in the same structure: price for the permanent items, and a credit or escrow for the one-time items. A lender will usually require an up-front escrow for immediate repairs and will size on NCF, so the broker's price is also unfinanceable on normal terms.

*Reproduce:* `tests/test_ch08_examples.py::test_example_8_5`

#### Example 8.6 — Reassessment in a market-value regime versus an acquisition-value regime

**Given.** Two otherwise identical buildings, each with pre-tax NOI $N = \$1{,}000{,}000$ and a market cap rate of 6.0% on NOI after reassessed tax. Hold the cap rate equal across states to isolate the tax effect.

* *Texas-style:* combined rate 2.20% of market value; appraisal at 100% of market value, reset toward the price, so $t = 2.20\%$. The seller's current appraisal is \$8.0 million.
* *California-style:* 1.00% general levy plus 0.15% of voter-approved debt, so $t = 1.15\%$ on the purchase price as the new base-year value. The seller's base-year value is \$4.0 million after decades of ownership.

[HYPOTHESIS: the rates are illustrative. Actual Texas rates vary by the combination of taxing units; California debt rates vary by tax rate area.]

**Find.** Value under each regime; the error from capitalizing the seller's tax bill; the drift of the California tax rate after 10 years if market value grows 4% a year.

**Solution.**

| | Texas-style | California-style |
|---|---:|---:|
| $t$ | 2.20% | 1.15% |
| Value $N/(c+t)$ | \$12,195,122 | \$13,986,014 |
| Reassessed tax $tV$ | \$268,293 | \$160,839 |
| Seller's tax bill | $8.0\text{m} \times 2.20\% = \$176{,}000$ | $4.0\text{m} \times 1.15\% = \$46{,}000$ |
| "Value" on seller's tax $(N - T^{seller})/c$ | \$13,733,333 | \$15,900,000 |
| Overpayment | \$1,538,211 (12.6%) | \$1,913,986 (13.7%) |

With no property tax at all, value would be $1{,}000{,}000/0.06 = \$16{,}666{,}667$. The California-style building is worth 14.7% more than the Texas-style building at the same cap rate, purely because of the lower tax rate.

*Drift.* After 10 years, $t_{10} = 1.15\% \times (1.02/1.04)^{10} = 0.947\%$ of market value, if the 2% inflation cap binds every year.

**Check.** Texas: $(1{,}000{,}000 - 268{,}293)/12{,}195{,}122 = 6.00\%$. ✓ California: $(1{,}000{,}000 - 160{,}839)/13{,}986{,}014 = 6.00\%$. ✓

**Decision consequence.** Both regimes reset tax at acquisition, so the loaded cap applies to both, and both punish the buyer who capitalizes the seller's bill. The California error is larger here because a long-held base year makes the seller's tax bill tiny. In California the tax advantage of a long hold is the owner's and not transferable, so cap rates computed from sellers' NOIs are not comparable to buyers' cap rates. In Texas the error comes from appraisal lag, and its size depends on how far the appraisal district's value trails the market. The comparison also explains a cross-state pricing pattern: holding cap rates equal, high-tax jurisdictions support lower prices per dollar of pre-tax NOI. A buyer comparing a Dallas and a Sacramento asset should compare loaded cap rates, $c + t$, not headline cap rates.

*Reproduce:* `tests/test_ch08_examples.py::test_example_8_6`

#### Example 8.7 — Replacement cost as an entry test: bulk industrial

**Given.** Per sf of building: hard cost \$110, soft cost 20% of hard, land \$18, developer margin 15% on cost. Market rent \$9.00/sf NNN; stabilized vacancy 5%; non-recoverable costs 3% of revenue. Stabilized new buildings sell at a 5.75% cap. Developers require a 125 bp spread of yield on cost over the cap rate. An existing building of similar quality is offered at \$130/sf.

**Find.** Cost and replacement cost with profit; yield on cost; value per sf of a stabilized new building; the rent needed for new supply; the existing building's discount to cost.

**Solution.**

* Cost $= 110 + 22 + 18 = \$150$/sf. Replacement cost with profit $= 150 \times 1.15 = \$172.50$/sf.
* Stabilized NOI per sf $= 9.00 \times 0.95 \times 0.97 = \$8.2935$.
* Yield on cost $= 8.2935/150 = 5.53\%$, below the 5.75% cap, let alone the 7.00% required.
* Stabilized value $= 8.2935/0.0575 = \$144.23$/sf. Value/cost $= 0.962$; value/replacement cost with profit $= 0.836$.
* Required rent $= (0.0575 + 0.0125) \times 150/(0.95 \times 0.97) = \$11.39$/sf, which is 26.6% above market.
* The existing building at \$130/sf is 86.7% of cost (13.3% below) and yields $8.2935/130 = 6.38\%$ if leased at market.

**Check.** At \$11.39 rent, NOI $= 11.394 \times 0.95 \times 0.97 = \$10.50$, and $10.50/150 = 7.00\%$. ✓

**Decision consequence.** New supply will not start until rents rise roughly 27%, construction costs fall, or cap rates compress about 125 bp. That is a real protection for the existing building, and it supports underwriting below-average competitive deliveries for the length of a construction cycle *after* the gap closes. It does not mean the existing building is "worth" \$172.50. Its value is set by its income: at market rent and a 5.75% cap it is worth about \$144/sf stabilized, and the \$130 offer is attractive only if lease-up costs and downtime are less than the \$14/sf difference. Sellers who quote replacement cost as a floor (Case A) are confusing a supply condition with a valuation.

*Reproduce:* `tests/test_ch08_examples.py::test_example_8_7`

---

### 8.6 CRE application: comparing the property types

The property types differ systematically in who bears which risk. The table below combines a computed operating-leverage illustration with qualitative characteristics. The archetype cost structures and all "typical" ranges are [HYPOTHESIS] for teaching. They are chosen to be representative, but no dated market source is cited for them, so verify them locally before use.

#### 8.6.1 Operating leverage by archetype (computed)

Each archetype is a stylized revenue and cost structure. "10% revenue shock" means revenue falls 10% with fixed costs unchanged. DOL is from `sdesk.cre.operating_leverage` except for the hotel, which uses the full USALI model of Example 8.3.

| Archetype | Revenue | Fixed costs | Variable cost (% rev.) | NOI | NOI margin | NOI change, −10% revenue | DOL |
|---|---:|---:|---:|---:|---:|---:|---:|
| Single-tenant net lease | 1,000,000 | 20,000 | 0% | 980,000 | 98.0% | −10.20% | 1.02 |
| Multi-tenant industrial (NNN) | 2,000,000 | 60,000 | 3% | 1,880,000 | 94.0% | −10.32% | 1.03 |
| Self-storage (specialty) | 2,000,000 | 640,000 | 6% | 1,240,000 | 62.0% | −15.16% | 1.52 |
| Multifamily | 3,000,000 | 1,110,000 | 8% | 1,650,000 | 55.0% | −16.73% | 1.67 |
| Multi-tenant office (gross) | 3,600,000 | 1,440,000 | 3% | 2,052,000 | 57.0% | −17.02% | 1.70 |
| Select-service hotel, occupancy-led | 5,849,928 | — | — | 1,434,439 | 24.5% | −22.27% | 2.23 |
| Select-service hotel, ADR-led | 5,849,928 | — | — | 1,434,439 | 24.5% | −31.06% | 3.11 |

For the hotel, "DOL" is the measured ratio of the NOI change to the revenue change. Two caveats apply. First, NOI margin and DOL are linked: low-margin assets are high-DOL assets. Second, the size of the shock is not the same across types. A 10% revenue decline is an ordinary year for a hotel and a severe event for a net-leased warehouse. Risk is DOL times the volatility of revenue, and the property types differ in both.

#### 8.6.2 Land: negative carry and pure optionality

Raw land produces no NOI. Its holder pays carry and owns an option on future development (Chapter 13, Case I). For a \$5,000,000 parcel with property tax at 2.2% (\$110,000), insurance and maintenance of \$15,000, and an 8% opportunity cost of capital (\$400,000), the annual carry is \$525,000, or **10.5% of value**. Land must appreciate about 10.5% a year just to break even against the alternative use of the capital. Note also that agricultural land in Texas may be appraised at productivity value rather than market value [FACT; Texas appraisal district summaries of the Tax Code; VERIFIED-SECONDARY], so a change of use can trigger a much higher tax and, under Texas law, rollback taxes *(rollback details verification pending)*. This is why land is the most speculative CRE asset: its return is almost entirely price change, and the carry runs against you while you wait.

#### 8.6.3 Systematic comparison

| Dimension | Hotel | Multifamily | Office | Retail | Industrial | Land | Specialty (storage, seniors, data centers) |
|---|---|---|---|---|---|---|---|
| Lease duration | One night | About 12 months | 5–10+ years | Anchors 10–20 years; shops 3–5 | 3–10 years; bulk often longer | None | Storage monthly; seniors monthly with care contracts; data centers often long |
| Who bears opex inflation | Owner | Owner (mostly) | Owner above base year under gross leases | Tenants (NNN), subject to caps | Tenants (NNN) | Owner (tax, insurance) | Owner |
| Operating leverage | Very high | Moderate | Moderate to high | Low to moderate | Low | n/a (negative carry) | Moderate to very high (seniors is an operating business) |
| Capex intensity | High: FF&E reserve 4% of revenue plus brand PIPs | Moderate: unit turns, roofs, systems | High: TI/LC on every rollover | Moderate: TI for shops, parking, roofs | Low: roofs, paving, dock equipment | Low until development | Varies widely |
| Cash-flow volatility | Highest; reprices daily | Low to moderate; reprices annually | Low in term, very high at rollover | Bimodal: anchors stable, shops cyclical | Low | None (no cash flow) | Varies with operator and contract |
| Liquidity (buyer pool, time to sell) | Thinner; brand and PIP diligence lengthen the process | Deepest; agency financing widely available | Narrowed sharply after 2020 for commodity suburban office *(verification pending for volume data)* | Moderate; anchors drive financeability | Deep | Thin; long marketing times | Thin; specialist buyers |
| Key underwriting variable | RevPAR and flow-through | Rent growth vs expense growth | Rollover, TI/LC, NER | Anchor health, co-tenancy, sales per sf | Supply pipeline, clear height, location | Entitlement and timing | Operator quality |

All entries in this table are [HYPOTHESIS] teaching generalizations. The one consistent pattern is that short leases transfer market risk to the owner quickly, which raises cash-flow volatility but also lets rents reset upward quickly in inflation. Long leases protect cash flow in downturns but lock in rent in inflations unless they have CPI escalators. "Defensive" and "inflation-protected" are opposite ends of the same choice.

#### 8.6.4 Expense ratios and what they tell you

Expense ratio = OpEx/EGI. In Example 8.1 it is 38.2%. The number is meaningless without the lease structure: NNN properties gross up EGI with recoveries, so their expense ratios look high even though the landlord bears little expense risk. Compare properties only on the same basis, preferably the **landlord-borne** expense ratio: unrecovered OpEx ÷ EGI. In Example 8.1 the landlord bears \$59,500 of unrecovered recoverables plus \$55,207 of management and non-recoverable costs, a total of \$114,707, or 12.3% of EGI. That is the operating leverage that matters.

---

### 8.7 Cash flow versus accounting earnings: a reconciliation discipline

Investors read REIT filings, appraisals, and seller statements prepared on different bases. Reconcile every income figure to cash using five adjustments.

1. **Depreciation and amortization.** Remove them entirely. Under current federal tax law, residential rental property is depreciated straight-line over 27.5 years and nonresidential real property over 39 years [FACT; IRS Publication 946 as summarized by secondary sources; VERIFIED-SECONDARY; check the current publication before relying on table values]. Depreciation affects the owner's income tax, which is an owner-level item, but it does not affect NOI.
2. **Straight-line rent.** Reverse the straight-line adjustment to get cash rent. In a portfolio with many recent leases with free rent, GAAP revenue exceeds cash rent. In a portfolio of old leases with fixed bumps, cash rent exceeds GAAP revenue late in the leases.
3. **Free rent.** Identify outstanding free rent at closing and require a credit, or deduct its PV from price (Example 8.2).
4. **TI and LC.** Treat them as capital at the time they are paid. On a stabilized basis, reserve for them per rentable sf, consistent with expected rollover.
5. **Non-recurring items.** Remove lease termination fees, insurance recoveries, real estate tax refunds from prior-year protests, and one-time expense savings.

REIT disclosures make the same point in their own vocabulary. Funds from operations adds back real estate depreciation to net income; adjusted measures then deduct straight-line rent and recurring capital. The conceptual chain is the same as the waterfall in §8.4.1. Definitions of these measures vary by company, so always read the reconciliation table.

---

### 8.8 When the relationships fail

1. **The rent roll is not the lease.** Rent rolls are summaries prepared by the seller's manager. Kick-out clauses, co-tenancy rights, exclusives, termination options, and expense caps live in the lease documents and estoppel certificates. A WALT computed to the stated expiry overstates term when tenants hold early termination options.
2. **Natural vacancy moves.** The rent-adjustment rule assumes a stable $v^*$. Structural change in how space is used shifts it. Post-2020 office demand is the obvious example: a vacancy rate that would once have signaled rent recovery may now be the new normal, and rent rules calibrated on older data will forecast recoveries that do not come [INFERENCE].
3. **Absorption can be negative while leasing is positive.** Gross leasing counts signed leases; net absorption counts occupancy changes. In a consolidation wave tenants sign smaller leases. Leasing volume looks healthy while occupied space shrinks.
4. **Replacement cost can fall.** When construction costs or land prices fall, or when a new building type (taller clear heights, better energy performance) makes older stock functionally obsolete, the replacement-cost "protection" evaporates. Value relative to *functional* replacement cost is what matters.
5. **Operating leverage can be reduced, at a price.** Hotels can cut labor and close floors; owners of gross-leased office can convert to net leases at renewal. Fixed costs are fixed only over the horizon in which contracts and labor arrangements cannot be changed. Over long horizons all costs are variable, and the ability to cut is part of the asset's option value.
6. **Tax regimes change.** Assessment caps, circuit breakers, and exemptions are set by legislatures and voters, and they change. Texas's 20% circuit breaker is explicitly temporary. Underwrite the statute in force, but stress-test the version that is less favorable to you.
7. **Reserves are fiction until funded.** A reserve deducted in a valuation is not cash in an account. Owners who distribute reserves, as most do, still face the capital bill when it comes, and it comes in lumps.
8. **Liquidity is regime-dependent.** In a credit contraction, transaction volume falls, bid–ask spreads widen, and the "market cap rate" is set by a handful of trades by motivated sellers (Chapter 2). The transaction-cost drag formula understates illiquidity because the cost of not being able to sell at all is not a percentage of price.

---

### 8.9 Historical episode: Texas commercial real estate, 1981–1995

#### Date and environment

[FACT] In the early 1980s federal tax policy raised the after-tax return on commercial real estate. The FDIC's history of the banking crises states that tax breaks enacted in the Economic Recovery Tax Act of 1981 greatly enhanced the after-tax returns on real estate investment, contributing to a construction boom (FDIC, *History of the Eighties*, vol. 1, ch. 3; VERIFIED-SECONDARY via excerpt). The 1981 Act shortened the tax recovery period for commercial real estate to 15 years (Tax Foundation; VERIFIED-SECONDARY). Later legislation in the mid-1980s lengthened recovery periods again; the exact sequence is reported differently by secondary sources *(verification pending)*.

[FACT] The Tax Reform Act of 1986 extended the recovery period for nonresidential real property to 31.5 years and for residential rental property to 27.5 years, required straight-line depreciation, and restricted the use of passive losses to offset other income (Tax Foundation; Federal Reserve Bank of Boston conference paper; both VERIFIED-SECONDARY).

[FACT] In Texas the boom coincided with an energy-driven economy. The FDIC attributes the high failure rate of Texas banks to the rapid rise and subsequent collapse of oil prices, together with real estate, agricultural, and branching factors (FDIC, *History of the Eighties*, vol. 1, ch. 1 and ch. 9; VERIFIED-SECONDARY). The specific oil price path is not quoted here *(verification pending against EIA or FRED series)*.

#### What happened in the space market

* [FACT] Office vacancy in Dallas rose from about 8% in 1980 to 28% in 1987 (FDIC, *History of the Eighties*, vol. 1, ch. 9; VERIFIED-SECONDARY via excerpt). A later FDIC regional publication describes Dallas office vacancy as peaking above 27% in 1988 (FDIC *Regional Outlook*, 2000; VERIFIED-SECONDARY). The two FDIC sources differ on the peak year by one year, which is consistent with different data vendors or definitions; we do not resolve it.
* [FACT] Texas commercial real estate growth outpaced office employment growth from 1982 to 1987, producing a combined office vacancy rate of about 30% by 1987 in the Austin, Dallas, Houston, and San Antonio areas (O'Keefe, *The Texas Banking Crisis: Causes and Consequences, 1980–1989*, FDIC, via FRASER; VERIFIED-SECONDARY).
* [FACT] Austin's office vacancy rate reached 39.5% in 1987, described as the highest ever recorded in the state (Federal Reserve Bank of Dallas, *Southwest Economy*, 1995; VERIFIED-SECONDARY).
* [FACT] The FDIC notes that office vacancies were already rising in the early 1980s while construction remained high (FDIC, *History of the Eighties*, vol. 1, ch. 9; VERIFIED-SECONDARY via excerpt).

#### What happened to the lenders

* [FACT] 425 Texas commercial banks failed or required assistance between 1980 and 1989, including nine of the state's ten largest bank holding companies (FDIC, *History of the Eighties*, vol. 1, ch. 9; O'Keefe; VERIFIED-SECONDARY).
* [FACT] Congress enacted FIRREA in August 1989 and created the Resolution Trust Corporation to resolve insolvent thrifts. By mid-1995 the RTC had resolved 747 thrifts with total assets of \$394 billion (FDIC *Banking Review*; Congressional Research Service report RS22959; VERIFIED-SECONDARY). These figures are national, not Texas-only.

#### What was knowable at the time

[INFERENCE] The ingredients were observable. Vacancy was rising while construction continued (the FDIC's own observation for the early 1980s). Office space was growing faster than office employment (O'Keefe). Tax benefits were raising the after-tax return on projects whose pre-tax economics did not need to work. In the language of §8.4.6, months of supply were rising while developers kept starting projects, which can be rational for a developer only if after-tax returns, fees, or lender incentives pay even when the building does not lease. In the language of §8.4.7, value was being supported by something other than the income of the space. What was not knowable was the timing and severity of the oil price collapse, or that the 1986 tax changes would remove part of the after-tax return from projects already financed.

#### Interpretations

1. **Overbuilding from mispriced incentives.** Tax benefits and lending practices made projects attractive to build independent of demand. The supply response overshot (FDIC's emphasis on tax policy and loosened underwriting).
2. **Regional demand shock.** Without the oil collapse, the excess space might have been absorbed over several years. The vacancy peaks reflect lost demand as much as excess supply.
3. **Policy reversal.** The 1986 Act changed the after-tax value of existing projects, which hurt owners and the lenders who financed them. Some analyses link the 1981 and 1986 changes to thrift failures; others note that real estate was volatile for many reasons beyond tax law (Tax Foundation discusses both views). [INFERENCE] The three interpretations are complementary rather than exclusive: overbuilt supply made the market fragile, and the demand and policy shocks exposed it.

#### What the case does and does not establish

It **establishes** that vacancy can rise from single digits to the high twenties or above within a few years when completions run far ahead of absorption. It shows that supply decisions made on after-tax or lender-driven economics rather than space-market economics produce stock that the market must absorb at falling rents. And it shows that lender losses follow the space market with a lag: the failures and the RTC came years after vacancy began rising.

It does **not** establish that any particular vacancy level predicts a crash, that tax law alone caused the bust, or that the same sequence will repeat in a market with different leverage, lending regulation, and supply constraints. Nor do our sources give rent or price declines for Texas office over the period; we state none *(verification pending)*.

**CRE connection.** Every quantity in Example 8.4 was measurable in Texas in 1983–1985: inventory, vacancy, pipeline, and absorption. The months-of-supply calculation would have shown a market whose pipeline needed years of absorption at a time when vacancy was already rising. The lesson for a speculator is not "avoid Texas." It is that the supply pipeline relative to absorption is the most predictive and least glamorous number in a market report.

---

### 8.10 Decision exercise: reprice the four offerings

Return to the four broker packages in §8.1. You have budget for detailed diligence on two of them. Using the results of Examples 8.1–8.6:

1. **Restate each NOI** on a consistent basis: cash NCF after reserves, after normalizing repairs, with property tax reassessed at the indicated price (assume a Texas-style $t = 2.2\%$ for all four). State which adjustments are facts and which are estimates.
2. **Reprice each asset** at the broker's cap rate applied to your restated income, using the loaded cap rate where tax is reassessed. Show the percentage gap from the broker's price.
3. **Rank the four by the quality of their income**: duration, operating leverage, capex exposure, and concentration. Rank them separately by price discount. Explain any divergence.
4. **Choose two for diligence.** For each, name the single piece of information most likely to change your view (for example: estoppels and anchor sales reports for Oak Hollow; the free-rent and TI schedule and the dark tenant's intentions for Lakeside; STR trend data and the PIP status for the hotel; the PCA and unit-level rent roll for Cedar Court).
5. **State what you will not pursue and why.** Declining all four is a legitimate answer if your restated yields do not clear your cost of capital by enough to pay for the risk.

**Rubric (see `problems/solutions/ch08_solutions.md` §Decision exercise).** Full credit requires that each NOI be restated on one basis with the adjustments labeled; that the hotel be stressed for an ADR-led decline; that Lakeside be valued on cash rather than contract rent with the free-rent credit; that Cedar Court separate permanent from one-time items; that the property-tax reassessment be loaded into each value; and that the choice of two be justified by information value, not only by discount. No single choice of two is correct.

---

### 8.11 Frequent analytical errors

1. **Capitalizing NOI when the comparables were capitalized on NCF, or the reverse.** State the line and the reserve every time.
2. **Counting free rent as income.** Contract rent is not cash rent. Ask for the concession schedule.
3. **Confusing leased with occupied with collecting.** Use all three occupancy measures. A dark tenant is a vacancy with a date.
4. **Treating "NNN" as zero landlord expense.** Caps, exclusions, and vacancy leave the landlord with unrecovered costs (Example 8.1).
5. **Using face rent instead of net effective rent** to compare office leases or to calibrate market rent.
6. **Reading WALT without concentration.** Report WALT with and without the largest tenant and the 24-month rollover share.
7. **Applying one DOL to a hotel.** Rate-led and occupancy-led declines have different flow-through.
8. **Counting pre-leased construction as supply** and then also ignoring its move-ins in absorption.
9. **Treating replacement cost as a value floor.** It is a supply condition (Example 8.7, Case A).
10. **Capitalizing the seller's property-tax bill.** Use the loaded cap rate in reassessment regimes and recognize that Proposition 13 base-year benefits do not transfer.
11. **Capitalizing one-time capex or ignoring permanent cost normalizations.** Permanent items go through the cap rate; one-time items are deducted in dollars.
12. **Treating the reserve as cash.** It is an allowance. The capex bill arrives on its own schedule.
13. **Ignoring transaction costs on short holds.** A 4% round trip is 0.8% a year over five years and about 1.6% a year over two and a half.

---

### 8.12 Connections to other chapters

* Chapter 1: operating leverage multiplies the financial leverage of §1.6; liquidity provision (§1.2) prices immediacy in illiquid property types.
* Chapter 2: price formation and appraisal smoothing explain why the "market cap rate" lags in illiquid types.
* Chapter 4: absorption is the transmission channel from employment and output to NOI.
* Chapter 6: the cap-rate/Treasury spread compares the asset market with fixed income.
* Chapter 9: DCF valuation of rollover, downtime, and TI/LC; loaded cap rates; sensitivity grids.
* Chapter 10: debt sizing on NCF; DSCR under operating-leverage shocks.
* Chapter 11: the full USALI hotel P&L, flow-through, PIPs, and Case A.
* Chapter 12: supply-driven cycles and distressed opportunities; the RTC as a disposal channel.
* Chapter 13: land and development as real options; hold/sell decisions with transaction costs.
* Chapter 23: the 1980s–90s Texas/RTC cycle in full.
* Case A: normalization, loaded cap, replacement cost, and PIP pricing applied to a hotel.

---

### 8.13 One-page reference sheet

**Waterfall:** PGI − vacancy − credit loss + other income = EGI; EGI − OpEx = NOI; NOI − reserves − TI/LC = NCF. In this chapter NOI is before reserves except for hotels (USALI: NOI after FF&E reserve).

| Formula | Expression |
|---|---|
| Physical / leased / economic occupancy | $A_{occ}/A$; $A_{lsd}/A$; cash rent ÷ potential rent |
| Expense ratio; landlord-borne ratio | OpEx/EGI; unrecovered OpEx/EGI |
| NOI growth | $g_{NOI} = g_R (R/NOI) - g_E (E/NOI)$ |
| Degree of operating leverage | $DOL = R(1-v)/NOI$ |
| WALT | $\sum R_i T_i / \sum R_i$ |
| Rollover within $h$ | $\sum_{T_i \le h} R_i / \sum R_i$ |
| Net effective rent | $\left[\sum CR_t (1+k)^{-t} - TI - LC\right] / a_{\overline{n}|k}$ |
| Vacancy identity | $V_{t+1} = V_t + C_t - AB_t$ |
| Months of supply | $(V + C^{spec}) / AB^{monthly}$ |
| Rent rule [HYPOTHESIS] | $g = g^* - \beta(v - v^*)$ |
| Yield on cost | $NOI^{new}/(H+S+L)$; build if $\ge c + s$ |
| Required rent | $(c+s)(H+S+L)/[(1-v)(1-e)]$ |
| Loaded cap value | $V = N/(c+t)$ |
| Prop 13 drift | $t_n = t_{CA}(1.02/(1+g_V))^n$ |
| Deferred-maintenance price | $(NOI^{norm} - Res)/c - (1+\kappa)\,Imm - PV(X_t - Res)$ |
| Transaction-cost drag | $1 - ((1-s)/(1+b))^{1/T}$ |

**Checks before any bid:** Which NOI line? Cash or straight-line? Leased, occupied, or collecting? WALT without the top tenant? Pipeline ÷ absorption? Value ÷ replacement cost and why? Tax reassessed? Reserve versus scheduled capex? How long to sell, and to whom?

---

### References for this chapter

All sources are listed with verification status in `references/sources_ch08.md` (to be merged into `SOURCE_REGISTER.md`).

* Federal Deposit Insurance Corporation (1997). *History of the Eighties — Lessons for the Future*, vol. 1: ch. 1 "The Banking Crises of the 1980s and Early 1990s: Summary and Implications"; ch. 3 "Commercial Real Estate and the Banking Crises of the 1980s and Early 1990s"; ch. 9 "Banking Problems in the Southwest." https://www.fdic.gov/publications/history-eighties-lessons-future-volume-1
* FDIC (2000). *Regional Outlook*, third quarter 2000 (office vacancy peaks). https://www.fdic.gov/analysis/archived-research/outlook/t3q2000.pdf
* O'Keefe, J. *The Texas Banking Crisis: Causes and Consequences, 1980–1989.* FDIC; archived on FRASER. https://fraser.stlouisfed.org/files/docs/publications/texasbankcrisis_1980_1989.pdf
* Federal Reserve Bank of Dallas (1995). *Southwest Economy*, issue 3. https://www.dallasfed.org/~/media/documents/research/swe/1995/swe9503a.pdf
* FDIC (1998). "The Banking Crises of the 1980s and Early 1990s." *FDIC Banking Review*, special issue. https://www.fdic.gov/analysis/archived-research/banking-review/brspecial.pdf
* Congressional Research Service (2008). *The Resolution Trust Corporation: Historical Analysis* (RS22959).
* Tax Foundation (2020). "1980s Tax Reform, Cost Recovery, and the Real Estate Industry: Lessons for Today."
* Federal Reserve Bank of Boston, conference series 36. "Tax Reform and the Housing Market in the Late 1980s." https://www.bostonfed.org/-/media/Documents/conference/36/conf36g.pdf
* California State Board of Equalization and county assessors (Sacramento, Santa Clara, San Luis Obispo). Proposition 13 and base-year value publications.
* Texas appraisal district publications summarizing Texas Property Tax Code §§1.04, 23.01, 23.231.
* IRS Publication 946, *How to Depreciate Property* (recovery periods; secondary confirmation).
* DiPasquale, D., and Wheaton, W. C. (1992). "The Markets for Real Estate Assets and Space: A Conceptual Framework." *Real Estate Economics* (formerly *AREUEA Journal*) *(bibliographic verification pending)*.
* Rosen, K. T. (1984). "Toward a Model of the Office Building Sector." *AREUEA Journal* *(bibliographic verification pending)*.
* Wheaton, W. C., and Torto, R. G. (1988). "Vacancy Rates and the Future of Office Rents." *AREUEA Journal* *(bibliographic verification pending)*.


\newpage

## Chapter 9 — CRE Valuation and Mispricing

> **Status:** Complete (v1.0). All fourteen worked examples, the historical-episode arithmetic, the problems, and the solutions are reproduced in `tests/test_ch09_examples.py`. Problems are in `problems/questions/ch09_problems.md` and solutions in `problems/solutions/ch09_solutions.md`. Sources are listed in `references/sources_ch09.md`; two historical figures are marked *(verification pending)* in §9.9.

### Learning objectives

After this chapter you should be able to:

1. Value an income property by direct capitalization, discounted cash flow, sales comparison, and replacement cost. For each method, say which question it answers and when it fails.
2. Build a DCF with explicit timing: annual cash flows after capital costs, reversion on **forward** NOI at the exit cap, selling costs, and the share of value that sits in the reversion.
3. Choose the right NOI (trailing, in-place, or stabilized) and deduct the cost of reaching stabilization. Capitalize correctly when property tax is reassessed at the price paid (the loaded cap rate).
4. Derive the going-in cap rate from $k$, $g$, and the capital-expenditure burden. Use it backwards to state **what the marginal buyer must believe** at a given price. Explain why exit cap rates normally exceed going-in cap rates.
5. Separate property-level IRR from equity IRR. Show when leverage adds return and when it only adds variance.
6. Build two-way sensitivity grids and find break-even exit caps.
7. Decompose an IRR into income, market NOI growth, value-add NOI growth, and cap-rate change. Label the parts that are business plan and the parts that are speculation.
8. Recognize owners anchored to historical cost, replacement cost, or a prior appraisal. Quantify the gap and judge whether a transaction can occur.
9. Explain appraisal smoothing and the divergence between appraisal-based and listed-market prices, using 2008–09 and 2022–24 as evidence.

---

### 9.1 Opening investment problem: the office building with three anchors

All facts in this section are [HYPOTHESIS], a constructed teaching case.

A family office asks you to evaluate a 165,000 sf multi-tenant suburban office building. The listing broker sends a two-page summary.

| Item | Broker's figure |
|---|---|
| Asking price | \$48.6 million |
| Trailing-12 NOI (after a \$0.25/sf reserve) | \$3,400,000 |
| Implied cap rate | 7.00% |
| 2021 appraisal (for the owner's lender) | \$52.0 million |
| Owner's acquisition price (2017) | \$47.5 million |
| Replacement cost | "\$400/sf, i.e., \$66 million" |
| Occupancy | 91% |

The broker's pitch is that the asking price is "below the appraisal, roughly at the owner's basis, and 26% below replacement cost."

Your leasing team adds what the summary leaves out. Tenant A occupies 49,500 sf, 30% of the building. Its lease expires in twelve months, and it has told several brokers it will consolidate into a smaller space downtown. Your team's lease-by-lease model projects twelve months of downtime, a new lease with tenant improvements of about \$55/sf, leasing commissions, and free rent. It also projects lower NOI than the trailing figure for three years. Your committee requires a 9.0% unlevered return on suburban office.

Three questions frame the chapter:

1. What is the building worth to a buyer who requires 9.0%?
2. At \$48.6 million, what must a buyer believe about growth, exit cap, or return?
3. Which of the broker's three anchors (appraisal, basis, replacement cost) is evidence of value, and which is only evidence of what the seller wants?

Section 9.10 returns to the bid.

---

### 9.2 Economic intuition: a price is a forecast that someone has agreed to

An income property is a claim on future net cash flow. Every valuation method estimates the present value of that claim. The methods differ in which observable quantity they lean on.

* **Direct capitalization** leans on market cap rates. One year of NOI is multiplied by a market multiple ($1/c$). All the forecasting is hidden inside $c$. The method works when the subject's cash flow profile resembles the profile of the assets whose sales set $c$.
* **Discounted cash flow** leans on your own forecast and your own required return. The forecast is explicit, so it can be wrong in visible ways. The method is necessary when the cash flow profile is irregular: lease rollover, lease-up, renovation, or a ground lease.
* **Sales comparison** leans on other people's recent decisions. It is the most direct market evidence when comparable trades are recent and numerous. It is weakest exactly when markets move fast, because comparable sales are then stale, few, and selected.
* **Replacement cost** leans on construction economics. It bounds value from above over the long run: if value exceeds cost plus a developer's margin, someone builds, and new supply pushes rents and values down. It does not bound value from below. Nobody is obliged to build, and a building that cannot earn a return on its cost is worth what its income supports.

A price agreed between a buyer and a seller is therefore a forecast that both parties have accepted. A sophisticated reader of a price asks what forecast it embeds. If the price implies NOI growth of 3% a year forever for a building with a 30% tenant leaving next year, the forecast is implausible, and either the buyer knows something you do not or the price will not hold.

#### Mispricing in private real estate

Private real estate prices are set in thin, slow, negotiated markets. Three features create persistent mispricing.

1. **No continuous price.** An asset trades every five to fifteen years. Between trades its "value" is an appraisal, which is an opinion built from past transactions. Appraisals smooth and lag (§9.9).
2. **Anchoring.** Owners anchor to their cost, to replacement cost, and to their last appraisal. These numbers are salient and personally meaningful, but they are not forecasts of cash flow. Kahneman and Tversky's work on anchoring and reference-dependent preferences predicts this behavior. In CRE it shows up as bid–ask gaps that close slowly and as low transaction volume after price declines.
3. **Heterogeneous information and constraints.** The buyer's NOI is not the seller's NOI. Each side has a different tax position, financing, and holding horizon. The marginal buyer, the one whose bid clears the market, sets the price. Their beliefs and constraints are what you must infer.

A mispricing is useful to a speculator only if it is **identifiable** (you can say what is wrong with the price), **actionable** (you can transact at it), and **likely to correct within your horizon** (something will force recognition). Anchored owners often fail the third test: the gap persists because they refuse to sell, not because the market eventually agrees with them.

---

### 9.3 Technical definitions

| Term | Definition |
|---|---|
| NOI | Revenue less operating expenses, **after** replacement reserves unless stated. Before debt service, income tax, depreciation, and leasing capital (TI/LC) unless stated |
| Cash flow after capex (CF) | NOI less tenant improvements, leasing commissions, and capital projects not funded by the reserve |
| Trailing NOI (T-12) | NOI over the last twelve months |
| In-place NOI | Current run-rate NOI from leases in place, annualized |
| Stabilized NOI | NOI at market occupancy, market rents, and normal expenses, once lease-up or renovation is complete |
| Forward NOI ($NOI_1$) | Expected NOI over the next twelve months. Brokers quote cap rates on forward NOI more often than on T-12; always ask which |
| Going-in cap rate $c_0$ | $NOI_1 / P$ |
| Terminal (exit) cap rate $c_T$ | The cap rate applied at sale to $NOI_{T+1}$ |
| Reversion | Sale proceeds at the end of the hold: gross $= NOI_{T+1}/c_T$; net = gross × (1 − selling costs) |
| Loaded cap rate | $c + t$, where $t$ is property tax as a fraction of price after reassessment |
| Discount rate $k$ | Required unlevered total return |
| Capex ratio $\kappa$ | Long-run average capital spending (TI/LC and building capital) as a fraction of NOI |
| Residual land value | GDV less all non-land costs less the developer's required profit |
| Replacement cost | Cost to build a functionally equivalent property today, including land at market. Depreciated replacement cost subtracts physical, functional, and external obsolescence |
| Property (unlevered) IRR | IRR of the property's cash flows, including purchase costs and net reversion |
| Equity (levered) IRR | IRR of equity flows after debt service and loan repayment |
| Marginal buyer | The bidder whose price clears the market; the one with the highest willingness to pay among those able to close |
| Anchor | A reference number (cost, prior appraisal, peak price) that shapes a reservation price but does not measure value |

---

### 9.4 Equations and derivations

#### 9.4.1 Direct capitalization

$$V = \frac{NOI_1}{c}.$$

The cap rate is a price multiple, not a return. It equals the expected return only if NOI is flat forever and no capital is spent.

#### 9.4.2 Discounted cash flow with explicit timing

For a hold of $T$ years with year-end cash flows:

$$V_0 = \sum_{t=1}^{T} \frac{NOI_t - CapEx_t}{(1+k)^t} + \frac{(1-s)\,NOI_{T+1}/c_T}{(1+k)^T}.$$

Here $s$ is the selling-cost fraction. Three timing rules are binding in this book:

1. The reversion capitalizes $NOI_{T+1}$, the buyer's forward income. Capitalizing $NOI_T$ applies a forward-NOI cap rate to trailing income and understates value by about a year of growth.
2. Capital spending is a cash outflow in the year it occurs, even if it raises NOI later. A DCF that adds the NOI uplift without the capex overstates value.
3. If the buyer at exit will face a large known capital need (a roof, a rollover), the exit cap or the reversion must reflect it.

The **reversion share** is $PV(\text{reversion})/V_0$. For a five-year hold it is usually 60–80% of value [HYPOTHESIS: typical of the examples in this chapter and Case C (70–78%); not a measured market statistic]. Most of a five-year DCF's value is therefore a forecast of someone else's cap rate five years from now.

#### 9.4.3 The cap rate as $k - g$, adjusted for capital spending

Suppose NOI grows at $g$ forever, and a constant fraction $\kappa$ of NOI is spent on capital. Free cash flow is $(1-\kappa)NOI_t$. The growing-perpetuity value is

$$V = \frac{(1-\kappa)\,NOI_1}{k - g} \quad\Rightarrow\quad c = \frac{NOI_1}{V} = \frac{k - g}{1-\kappa}.$$

Rearranged, the price tells you what a buyer must believe:

$$g_{\text{implied}} = k - c(1-\kappa), \qquad k_{\text{implied}} = c(1-\kappa) + g.$$

With $\kappa = 0$ this is the familiar $c = k - g$ (`sdesk.cre.gordon_cap_rate`). Ignoring $\kappa$ overstates the growth or return a buyer is getting. The bias is largest for office, where TI/LC can consume 15–25% of NOI over a cycle [HYPOTHESIS: teaching range; verify against your own lease-by-lease history].

#### 9.4.4 Why the exit cap usually exceeds the going-in cap

Apply 9.4.3 at two dates. At acquisition the building has growth $g_0$ and capex burden $\kappa_0$. At exit it is older: its growth is usually lower and its capex burden higher. Holding $k$ fixed,

$$c_T - c_0 = \frac{k - g_T}{1-\kappa_T} - \frac{k - g_0}{1-\kappa_0} > 0 \quad \text{when } g_T < g_0 \text{ or } \kappa_T > \kappa_0.$$

The **going-in/exit spread** is therefore not conservatism for its own sake. It is the cap-rate consequence of aging. Its typical size in underwriting practice is 25–75 bp for a five- to ten-year hold [HYPOTHESIS: practitioner convention, not a measured market statistic]. A further component reflects uncertainty about the rate environment at exit. That component is a forecast, and it should be labeled as one.

#### 9.4.5 The IRR identity: when IRR equals $c + g$

If NOI grows at constant $g$, no capital is spent, there are no transaction costs, and the exit cap equals the going-in cap, then the property IRR equals $c_0 + g$ exactly, for any hold period.

*Proof.* At $k = c_0 + g$, the price $NOI_1/c_0$ equals the Gordon value $NOI_1/(k-g)$. The reversion $NOI_{T+1}/c_0$ equals the Gordon value at $T$. Discounting a Gordon value at $k$ reproduces the Gordon value at 0, so NPV = 0 at $k = c_0 + g$. ∎

This identity is the backbone of the IRR decomposition in Example 9.10. Deviations from it come from cap-rate change, NOI growth different from $g$, capital spending, and transaction costs.

#### 9.4.6 Loaded cap rate

If property tax after the sale is $tP$, then $V = (N - tV)/c$, so

$$V = \frac{N}{c + t},$$

where $N$ is NOI before property tax (`sdesk.cre.loaded_cap_value`). Case A derived this for a Texas hotel. It applies to any property in a jurisdiction that reassesses to sale price.

#### 9.4.7 Residual land value

With gross development value $GDV$, selling cost $s$, non-land costs $H + S + F$ (hard, soft, financing), and required margin on total cost $m$:

$$N = GDV(1-s), \quad N = (L + H + S + F)(1+m) \;\Rightarrow\; L = \frac{N}{1+m} - (H + S + F).$$

Land is the residual claimant on development, so it is a levered position on GDV: a 1% change in GDV moves land value by $N/(1+m)/L$ percent, often 10–20 times as much (`sdesk.cre.residual_land_value`).

#### 9.4.8 Leverage and the equity IRR

For one period, with LTV $\lambda$ and debt cost $r_D$:

$$r_E = r_A + \frac{\lambda}{1-\lambda}(r_A - r_D).$$

On a multi-year hold, use the full equity cash-flow vector: equity in, NOI less capex less debt service each year, net reversion less loan balance at exit. Compare the **cash** yield with the loan constant $K$ and the **total** return with the interest rate. Leverage can be negative on cash yield (cap rate below $K$) and still positive on IRR, if appreciation is large enough. That configuration means the levered investor depends on appreciation.

#### 9.4.9 Appraisal smoothing

A simple model of an appraised value $A_t$ is a weighted average of the prior appraisal and current true value $V_t$:

$$A_t = \alpha A_{t-1} + (1-\alpha) V_t, \qquad 0 \le \alpha < 1.$$

Inverting it gives the unsmoothing filter used in the appraisal literature (Geltner, 1993):

$$V_t = \frac{A_t - \alpha A_{t-1}}{1-\alpha}.$$

With $\alpha = 0.6$, a sudden 25% fall in true value appears in appraisals as a 10% fall in the first period and is only about 85% recognized after three periods (Example 9.14).

---

### 9.5 Worked examples

All inputs are [HYPOTHESIS] unless cited. All examples are reproduced in `tests/test_ch09_examples.py`. NOI is after replacement reserves unless stated. Cash flows are annual and at year-end.

#### Example 9.1 — Three NOIs, three values: trailing, in-place, stabilized (multifamily)

**Given.** A 240-unit garden apartment community has just finished renovating 120 units. The market cap rate for stabilized assets of this quality is 5.50% on forward stabilized NOI after a \$300/unit reserve.

| NOI measure | Amount | What it reflects |
|---|---:|---|
| Trailing-12 | \$2,610,000 | Months with 20–30 units offline for renovation |
| In-place (last 3 months × 4) | \$2,880,000 | Renovation complete; concessions of one month free still on 60 new leases; 91% occupancy |
| Underwritten stabilized (Year 1 forward, after 9 months of lease-up) | \$3,060,000 | 95% occupancy; renovated-unit premiums; concessions burned off |

The cost to reach stabilization is the NOI shortfall during lease-up (\$310,000) plus marketing and turn costs (\$75,000), a total of \$385,000.

**Find.** The value implied by each NOI, and the as-is value.

**Solution.**

$V = NOI/c$ at $c = 0.055$:

| NOI basis | NOI | Value |
|---|---:|---:|
| Trailing | 2,610,000 | 47,454,545 |
| In-place | 2,880,000 | 52,363,636 |
| Stabilized | 3,060,000 | 55,636,364 |

As-is value = stabilized value − cost to stabilize $= 55{,}636{,}364 - 385{,}000 = \$55{,}251{,}364$.

The deduction is undiscounted. Discounting \$385,000 over nine months at 7% would change it by about \$19,000 and does not affect the decision.

**Check.** \$3,060,000 / \$55,636,364 = 5.50%. The spread between trailing and stabilized value is \$8.18 million. It is 14.7% of the stabilized value and is explained entirely by the choice of NOI.

**Decision consequence.** A seller will quote the stabilized figure. A buyer anchored to the trailing figure will lose every competitive bid. The correct bid starts from stabilized value and deducts the cost and the **risk** of reaching it. The \$385,000 deduction covers the cost. It does not cover the risk that the renovated-unit premium fails to hold. If the premium is the business plan you are buying, you are paying the seller for a forecast you will have to execute. Ask for 90 days of signed renovated leases before you pay for stabilized NOI. A 5.50% cap applied to trailing NOI is a convention mismatch: market cap rates are quoted on forward stabilized NOI, so the trailing value is not a "conservative" value. It is a wrong one.

Reproduce: `tests/test_ch09_examples.py::test_example_9_1`.

#### Example 9.2 — Reassessment: the loaded cap rate on the same apartments

**Given.** Example 9.1's property is in a jurisdiction that reassesses to market value after a sale. The trailing tax bill is \$520,000: assessed value \$26.0 million × 2.00%. After a sale the assessor will set assessed value at 90% of the price. Stabilized NOI before property tax is therefore $3{,}060{,}000 + 520{,}000 = \$3{,}580{,}000$. The market cap rate (on NOI after reassessed tax) is 5.50%.

**Find.** Value with reassessment, the new tax bill, and the error from capitalizing the seller's tax bill.

**Solution.**

Effective tax on price: $t = 2.00\% \times 0.90 = 1.80\%$.

Loaded cap rate: $c + t = 5.50\% + 1.80\% = 7.30\%$.

$$V = \frac{3{,}580{,}000}{0.073} = \$49{,}041{,}096.$$

New tax bill $= 0.018 \times 49{,}041{,}096 = \$882{,}740$. NOI after reassessed tax $= 3{,}580{,}000 - 882{,}740 = \$2{,}697{,}260$.

Error from capitalizing NOI that carries the seller's \$520,000 tax bill: $55{,}636{,}364 - 49{,}041{,}096 = \$6{,}595{,}268$. That is 13.4% of the correct value.

**Check.** \$2,697,260 / \$49,041,096 = 5.50%. ✓

**Decision consequence.** In a reassessment jurisdiction, the seller's T-12 tax line is a liability that resets at your price. A buyer who capitalizes it pays the seller for a tax bill the buyer will never enjoy. The effect is large because the old assessment (\$26.0 million) is far below the price. The gap between assessed value and market value is widest after a period of rising prices, which is when bidding is most competitive. Underwrite tax on the price you will pay. The loaded cap rate makes the circularity disappear.

Reproduce: `tests/test_ch09_examples.py::test_example_9_2`.

#### Example 9.3 — Office DCF with rollover, TI/LC, and forward NOI at exit

**Given.** The §9.1 office building. Your team's lease-by-lease projection (annual, year-end):

| Year | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| NOI | 3,400,000 | 2,300,000 | 2,850,000 | 3,300,000 | 3,400,000 | 3,500,000 |
| TI, LC, building capital | 250,000 | 3,550,000 | 450,000 | 300,000 | 350,000 | — |
| Cash flow after capex | 3,150,000 | −1,250,000 | 2,400,000 | 3,000,000 | 3,050,000 | — |

Year 1 still includes Tenant A's rent. Year 2 has twelve months of downtime on 49,500 sf, plus \$2.72 million of TI (\$55/sf) and leasing commissions. Year 3 carries free rent on the new lease. Exit at the end of Year 5 at an 8.25% cap on Year 6 NOI, with 2.0% selling costs. Discount rate 9.0%.

**Find.** Value, reversion share, implied going-in cap, the IRR at the asking price, and the exit cap needed to justify the ask.

**Solution.**

Reversion: gross $= 3{,}500{,}000 / 0.0825 = \$42{,}424{,}242$. Net $= 42{,}424{,}242 \times 0.98 = \$41{,}575{,}758$.

Present values at 9.0%:

| Year | Cash flow | Discount factor | PV |
|---|---:|---:|---:|
| 1 | 3,150,000 | 0.917431 | 2,889,908 |
| 2 | −1,250,000 | 0.841680 | −1,052,100 |
| 3 | 2,400,000 | 0.772183 | 1,853,240 |
| 4 | 3,000,000 | 0.708425 | 2,125,276 |
| 5 | 3,050,000 | 0.649931 | 1,982,291 |
| 5 | Net reversion 41,575,758 | 0.649931 | 27,021,390 |
| | **Value** | | **34,820,005** |

PV of operating cash flows = \$7,798,615. Reversion share $= 27{,}021{,}390 / 34{,}820{,}005 = 77.6\%$.

Implied going-in cap on Year 1 NOI $= 3{,}400{,}000 / 34{,}820{,}005 = 9.76\%$. Value per sf = \$211.

At the asking price of \$48,571,429 (= \$3,400,000 / 0.07), the same cash flows produce an IRR of **1.44%**. To earn 9.0% at the ask, a buyer would need an exit cap of **5.47%** on Year 6 NOI.

**The timing trap.** If you capitalize Year 5 NOI (\$3,400,000) instead of Year 6 NOI at exit, value falls to \$34,047,965, an understatement of \$772,040. The error is small here because Year 6 NOI grows only 2.9% over Year 5. It becomes large when the exit year contains a known NOI step: for example, a lease burning off free rent in Year 6.

**Check.** Rebuild by hand: $2{,}889{,}908 - 1{,}052{,}100 + 1{,}853{,}240 + 2{,}125{,}276 + 1{,}982{,}291 + 27{,}021{,}390 = 34{,}820{,}005$. ✓ `sdesk.cre.dcf_value(cf, 3_500_000, 0.0825, 0.09, 0.02)` returns the same.

**Decision consequence.** The broker's 7.0% cap applies a stabilized multiple to a year of income that will not recur until Year 5. The DCF shows that the building is worth about \$34.8 million to a 9% buyer, 28% below the ask. More than three-quarters of that value sits in a Year-5 sale. The bid therefore depends far more on your exit-cap view and on re-leasing Tenant A's space than on Year 1 NOI. The highest-value diligence is a leasing study of the 49,500 sf block: achievable rent, downtime, and TI package. A refined discount rate is worth much less. A 5.47% exit cap on a suburban office building sold five years from now is not a forecast any committee would sign, so the ask is not a price at which this building trades to an informed buyer.

Reproduce: `tests/test_ch09_examples.py::test_example_9_3`.

#### Example 9.4 — What must the marginal buyer believe? Implied growth across property types

**Given.** Three assets, each quoted at a market cap rate. Your required unlevered returns and long-run capex burdens:

| Asset | Cap rate $c$ | Required return $k$ | Capex ratio $\kappa$ |
|---|---:|---:|---:|
| Suburban office (the §9.1 ask) | 7.00% | 9.00% | 15% |
| Bulk industrial | 5.25% | 7.50% | 5% |
| Garden multifamily | 5.50% | 7.25% | 8% |

**Find.** The perpetual NOI growth each price implies. For the office, also find the return a buyer earns if long-run NOI growth is only 1%.

**Solution.** $g_{\text{implied}} = k - c(1-\kappa)$:

| Asset | $c(1-\kappa)$ | $g_{\text{implied}}$ |
|---|---:|---:|
| Office | $0.07 \times 0.85 = 5.95\%$ | $9.00\% - 5.95\% = 3.05\%$ |
| Industrial | $0.0525 \times 0.95 = 4.99\%$ | $7.50\% - 4.99\% = 2.51\%$ |
| Multifamily | $0.055 \times 0.92 = 5.06\%$ | $7.25\% - 5.06\% = 2.19\%$ |

Office at 1% growth: $k_{\text{implied}} = c(1-\kappa) + g = 5.95\% + 1.00\% = 6.95\%$. The cap rate consistent with 9.0% and 1% growth is $(0.09 - 0.01)/0.85 = 9.41\%$.

**Check.** `gordon_cap_rate(0.09, 0.0305) / 0.85` returns 0.0700. ✓

**Decision consequence.** The office ask requires a buyer to believe in 3% perpetual NOI growth on a building with structural vacancy risk, or to accept a 6.95% unlevered return. Both are statements you can test. Ask yourself whether 3% nominal NOI growth forever is plausible for suburban office, given the capex it takes to keep tenants. Then ask whether 6.95% is adequate compensation for an illiquid, high-capex asset. The industrial and multifamily prices imply growth near long-run inflation expectations. Those prices are not obviously wrong; they are bets that inflation-level rent growth persists. This "reverse" use of $k - g$ is the fastest way to locate an aggressive price. It does not tell you the right price. It tells you which belief to argue about.

Reproduce: `tests/test_ch09_examples.py::test_example_9_4`.

#### Example 9.5 — Deriving the going-in/exit cap spread from aging

**Given.** $k = 8.0\%$ for a five-year-old industrial building. Today: long-run NOI growth 2.5%, capex burden 10%. In ten years the building will be fifteen years old: growth 2.0% (lower functional competitiveness), capex burden 15% (roof, paving, HVAC).

**Find.** The going-in cap, the exit cap in Year 10, and the spread.

**Solution.**

$$c_0 = \frac{0.08 - 0.025}{1 - 0.10} = \frac{0.055}{0.90} = 6.11\%, \qquad c_{10} = \frac{0.08 - 0.020}{1 - 0.15} = \frac{0.060}{0.85} = 7.06\%.$$

Spread $= 7.06\% - 6.11\% = 95$ bp, with no change in rates or risk premia.

**Decision consequence.** A DCF that sets the exit cap equal to the going-in cap assumes the building does not age. That is a hidden forecast of either cap-rate compression or a capital program that restores the building's competitiveness. If your model contains that capital program, a flat exit cap may be defensible. Otherwise the 95 bp is not "cushion"; it is the structural cost of time. Any exit-cap view beyond aging (rates, risk appetite) is a macro forecast. State it separately, so the committee can see how much of the IRR rests on it.

Reproduce: `tests/test_ch09_examples.py::test_example_9_5`.

#### Example 9.6 — Sales comparison with a stale comp, a distressed comp, and reliability weights

**Given.** Subject: a 120,000 sf bulk industrial building, built 2008, 32-foot clear height, vacant at sale (owner-user or speculative buyer). Four sales within the submarket. Adjustments are multiplicative, in the order shown. The time adjustment uses your submarket price index, which has fallen since the older sales.

| Comp | Price/sf | Months ago | Time | Location | Physical (age, clear height) | Conditions of sale | Lease (occupancy, credit) |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | \$142 | 4 | −2% | 0% | +5% | 0% | 0% |
| B | \$165 | 20 | −14% | −5% | −5% | 0% | 0% |
| C | \$128 | 2 | −1% | +5% | +10% | +8% (forced seller) | 0% |
| D | \$150 | 9 | −6% | 0% | 0% | 0% | −7% (10-yr credit lease) |

Weight each comp by the inverse of its **gross** (absolute) adjustment, a common rule that favors comps needing fewer judgments.

**Find.** Adjusted prices, weights, and the indicated value.

**Solution.**

| Comp | Adjustment factor | Adjusted \$/sf | Gross adjustment | Weight |
|---|---:|---:|---:|---:|
| A | 0.98 × 1.05 = 1.0290 | 146.12 | 7% | 47.1% |
| B | 0.86 × 0.95 × 0.95 = 0.7761 | 128.06 | 24% | 13.7% |
| C | 0.99 × 1.05 × 1.10 × 1.08 = 1.2349 | 158.07 | 24% | 13.7% |
| D | 0.94 × 0.93 = 0.8742 | 131.13 | 13% | 25.4% |

Weighted indicated value = \$141.48/sf. Value = $141.48 \times 120{,}000 = \$16{,}977{,}094$. The simple average of adjusted prices is \$140.85/sf.

**The stale-comp error.** Comp B, unadjusted for time but adjusted for location and physical differences, indicates $165 \times 0.95 \times 0.95 = \$148.91$/sf. That is 16% above its time-adjusted figure. An appraiser who weights B heavily because "it is the best physical match" imports a pre-decline price into a post-decline valuation.

**Selection bias.** The four comps are the sales that closed. In the same period, suppose five listings were withdrawn because no bid met the seller's reservation price. Sales that close are the ones where some buyer valued the asset above the seller's reservation price. In a falling market, owners with no need to sell withdraw, so the closed sales are disproportionately (a) assets with buyers who value them unusually highly, and (b) forced sales like C. The two biases point in opposite directions. Neither is visible in the comp grid. Ask the broker for withdrawn listings and their best bids. That evidence is often more informative than a fifth closed sale.

**Decision consequence.** The indicated value of about \$17.0 million is a range, not a point: the adjusted comps span \$128–\$158/sf, or \$15.4–\$19.0 million. The width of that range comes from adjustments that are opinions (location, physical, conditions of sale). A bid at the indicated value is defensible only if your income approach agrees within a few percent. If it does not, the disagreement tells you which approach to investigate. Two weak comps that disagree are evidence of a moving market, not of a precise value.

Reproduce: `tests/test_ch09_examples.py::test_example_9_6`.

#### Example 9.7 — Replacement cost and residual land value: when does new supply arrive?

**Given.** A developer is considering a 200,000 sf speculative industrial building. Stabilized NOI \$1,600,000 (\$8.00/sf net). Hard costs \$90/sf = \$18,000,000. Soft costs 18% of hard = \$3,240,000. Financing costs \$1,300,000. Selling costs 1.5% of GDV. Required developer margin on total cost: 15%. The land seller asks \$2,500,000. Market exit cap: 5.75%, with sensitivity at 5.25% and 6.25%.

**Find.** Residual land value at each cap rate; the developer's margin if the land is bought at the asking price; replacement cost per sf.

**Solution.**

At 5.75%: $GDV = 1{,}600{,}000/0.0575 = \$27{,}826{,}087$. Net value $N = 27{,}826{,}087 \times 0.985 = \$27{,}408{,}696$. Non-land cost $= 18{,}000{,}000 + 3{,}240{,}000 + 1{,}300{,}000 = \$22{,}540{,}000$.

$$L = \frac{27{,}408{,}696}{1.15} - 22{,}540{,}000 = 23{,}833{,}648 - 22{,}540{,}000 = \$1{,}293{,}648.$$

| Exit cap | GDV | Net value | Residual land |
|---|---:|---:|---:|
| 5.25% | 30,476,190 | 30,019,048 | 3,563,520 |
| 5.75% | 27,826,087 | 27,408,696 | 1,293,648 |
| 6.25% | 25,600,000 | 25,216,000 | −613,043 |

At the \$2.5 million asking price for land, total cost is $22{,}540{,}000 + 2{,}500{,}000 = \$25{,}040{,}000$ (\$125.20/sf). This is replacement cost before developer's profit. The margin on cost is $27{,}408{,}696 / 25{,}040{,}000 - 1 = 9.46\%$, below the 15% requirement. Yield on cost $= 1{,}600{,}000/25{,}040{,}000 = 6.39\%$.

**Check.** At 5.75%, value/replacement cost $= 27{,}826{,}087/25{,}040{,}000 = 1.11$. A ratio below about $1.15/(1-s) = 1.17$ means development does not clear the required margin. ✓

**Decision consequence.** Two conclusions follow. First, the land is a levered call on cap rates: a 100 bp move in the exit cap (5.25% to 6.25%) moves GDV by \$4.88 million, 17.5% of the base-case GDV, and residual land value from +\$3.56 million to −\$0.61 million. Land sellers anchored to 2021-style land comps will not see that arithmetic, and land transactions will stall before building transactions do. Second, for owners of **existing** industrial buildings, the infeasibility of new construction at 5.75% is good news: new supply will not arrive until NOI (at a constant cap rate) rises about 5.1%: the developer needs net value of $1.15 \times 25{,}040{,}000 = \$28{,}796{,}000$ against \$27,408,696 today. Replacement cost sets a ceiling on how far values can rise before supply responds. It does not support a floor, which Example 9.13 shows.

Reproduce: `tests/test_ch09_examples.py::test_example_9_7`.

#### Example 9.8 — Property IRR versus equity IRR: positive leverage that is mostly variance

**Given.** Purchase of a stabilized industrial building for \$25,000,000 plus 1.0% buyer costs. Year 1 NOI \$1,400,000 (5.60% going-in), growing 3% a year. Capital spending 5% of NOI each year. Sale at the end of Year 5 at a 6.00% cap on Year 6 NOI, less 1.5% selling costs. Loan: 60% of price (\$15,000,000), 6.25% fixed, 30-year amortization, monthly payments, balloon at the end of Year 5.

**Find.** Property IRR, equity IRR, first-year cash-on-cash, DSCR and debt yield; the equity IRR at a 5.00% rate.

**Solution.**

NOI: 1,400,000; 1,442,000; 1,485,260; 1,529,818; 1,575,712; Year 6 1,622,984.
Cash flow after capex (×0.95): 1,330,000; 1,369,900; 1,410,997; 1,453,327; 1,496,927.
Gross reversion $= 1{,}622{,}984/0.06 = \$27{,}049{,}728$. Net $= \$26{,}643{,}982$.

Property flows: $[-25{,}250{,}000;\ 1{,}330{,}000;\ 1{,}369{,}900;\ 1{,}410{,}997;\ 1{,}453{,}327;\ 28{,}140{,}909]$.
**Property IRR = 6.54%**. Equity multiple 1.33x.

Debt: monthly payment on \$15,000,000 at 6.25%/12 over 360 months gives annual debt service \$1,108,291 (loan constant 7.39%). Balance after 60 payments \$14,000,586. DSCR Year 1 $= 1{,}400{,}000/1{,}108{,}291 = 1.26$x. Debt yield $= 1{,}400{,}000/15{,}000{,}000 = 9.33\%$.

Equity flows: $[-10{,}250{,}000;\ 221{,}709;\ 261{,}609;\ 302{,}706;\ 345{,}036;\ 13{,}032{,}032]$.
Year 5 equity flow $= 1{,}496{,}927 - 1{,}108{,}291 + 26{,}643{,}982 - 14{,}000{,}586$.
**Equity IRR = 6.97%**. Equity multiple 1.38x. First-year cash-on-cash $= 221{,}709/10{,}250{,}000 = 2.16\%$.

At a 5.00% loan rate (constant 6.44%), equity IRR = 8.59%.

**Decision consequence.** Leverage raised the IRR by 43 bp, from 6.54% to 6.97%, because the property IRR barely exceeds the 6.25% loan rate. It cut first-year cash yield from 5.27% (1,330,000/25,250,000) to 2.16%, because the 5.60% cap is below the 7.39% loan constant. The equity is therefore a bet that NOI growth and the exit cap deliver the reversion. Example 9.9 shows that the same 60% LTV that adds 43 bp in the base case multiplies the dispersion of outcomes. When the property IRR sits within about 50 bp of the debt cost, leverage is mostly a variance amplifier. A sponsor who presents only the 6.97% is presenting the mean of a wider distribution as if it were an improvement.

Reproduce: `tests/test_ch09_examples.py::test_example_9_8`.

#### Example 9.9 — Two-way sensitivity grids and the break-even exit cap

**Given.** Example 9.8 with NOI growth $g \in \{1\%, 2\%, 3\%, 4\%\}$ and exit cap $\in \{5.50\%, 5.75\%, 6.00\%, 6.25\%, 6.50\%\}$. All other inputs unchanged.

**Find.** Property and equity IRR grids, and the exit cap at which the property IRR equals 7.0% with 3% growth.

**Solution.** Property IRR (%):

| $g$ \\ exit cap | 5.50% | 5.75% | 6.00% | 6.25% | 6.50% |
|---|---:|---:|---:|---:|---:|
| 1% | 6.14 | 5.34 | 4.58 | 3.86 | 3.18 |
| 2% | 7.14 | 6.33 | 5.56 | 4.83 | 4.14 |
| 3% | 8.14 | 7.32 | **6.54** | 5.81 | 5.11 |
| 4% | 9.14 | 8.31 | 7.52 | 6.78 | 6.07 |

Equity IRR at 60% LTV, 6.25% (%):

| $g$ \\ exit cap | 5.50% | 5.75% | 6.00% | 6.25% | 6.50% |
|---|---:|---:|---:|---:|---:|
| 1% | 6.04 | 4.13 | 2.24 | 0.37 | −1.50 |
| 2% | 8.32 | 6.48 | 4.67 | 2.88 | 1.11 |
| 3% | 10.50 | 8.72 | **6.97** | 5.26 | 3.56 |
| 4% | 12.60 | 10.87 | 9.18 | 7.52 | 5.89 |

Break-even exit cap for a 7.0% property IRR at 3% growth: **5.85%**. That is 15 bp below the 6.00% base-case exit cap, which is itself the 5.60% going-in cap plus a 40 bp aging spread.

**Decision consequence.** Read the grids diagonally. Moving one cell toward the lower right (growth −1 point, exit cap +25 bp) costs about 170 bp of property IRR and about 400 bp of equity IRR. Leverage more than doubles the sensitivity. The property grid's range is 3.18%–9.14%; the equity grid's is −1.50%–12.60%. A committee that targets 7.0% unlevered should notice that the target requires an exit cap of 5.85% or lower at 3% growth. That is a cap-rate forecast, not a business plan. The grids do not assign probabilities. They tell you which two variables matter and how much, so you can decide which to research and which to hedge. A grid with an axis that does not move the answer is a wasted grid.

Reproduce: `tests/test_ch09_examples.py::test_example_9_9`.

#### Example 9.10 — Decomposing IRR: income, market growth, value-add, and cap compression

**Given.** A value-add apartment purchase at \$40,000,000 (no transaction costs, to keep the decomposition clean). Year 1 NOI \$2,000,000 (5.00% going-in). Market NOI growth 3%. A \$3,000,000 unit-renovation program in Year 1 adds \$450,000 of NOI from Year 2, growing at 3% thereafter. Sale at the end of Year 5 at a 4.75% cap on Year 6 NOI.

**Find.** The IRR, decomposed into income, market NOI growth, value-add, and cap-rate change.

**Solution.** Build the IRR up one assumption at a time.

| Step | Added assumption | Year 6 NOI | Gross reversion | IRR | Increment |
|---|---|---:|---:|---:|---:|
| (a) | Flat NOI, exit at 5.00% | 2,000,000 | 40,000,000 | 5.00% | 5.00% income |
| (b) | + market growth 3% | 2,318,548 | 46,370,963 | 8.00% | +3.00% market growth |
| (c) | + renovation (−\$3.0m Y1; +\$450k NOI from Y2) | 2,825,027 | 56,500,542 | 10.96% | +2.96% value-add |
| (d) | + exit at 4.75% | 2,825,027 | 59,474,255 | 11.97% | +1.00% cap compression |

Step (a) and step (b) confirm the identity of §9.4.5: with no capex and exit cap = going-in cap, IRR = $c_0 + g$ exactly.

The renovation earns a 15% yield on cost ($450{,}000/3{,}000{,}000$). At a 5.00% cap it creates \$6.0 million of value for \$3.0 million of capital.

**Order dependence.** Adding the cap-rate change before the renovation gives a cap-rate increment of 0.97% instead of 1.00% (growth plus cap compression alone gives 8.97%). The attribution depends on order because IRR is nonlinear. State the order you used.

**Decision consequence.** Of the 11.97% IRR, 5.00 points are income you can underwrite from leases, and 2.96 points are a business plan you control: renovation scope, cost, and rent premium. The remaining 4.00 points are market growth and cap compression, which you do not control. They are **speculative appreciation**. A sponsor who calls the whole 11.97% "value-add" is selling market beta as skill. Committees should ask two questions. First, what is the IRR with zero market growth and a 25–50 bp *higher* exit cap? That is the return on the business plan alone. Second, is the fee and promote structure paying the sponsor for the 4.00 points it does not control?

Reproduce: `tests/test_ch09_examples.py::test_example_9_10`.

#### Example 9.11 — Anchoring case I: the apartment owner and the 2021 basis

**Given.** An owner bought a 300-unit apartment community in 2021 for \$62,000,000, at a 3.90% cap on NOI of \$2,418,000. The loan is \$40,300,000, floating, now at 6.50% interest-only. NOI has grown: forward NOI is \$2,650,000. The market cap rate for comparable assets is now 5.60%. A buyer offers market value. The owner says: "I'm not selling below my \$62 million basis."

**Find.** Market value; the owner's loss versus basis; the owner's equity; the NOI growth or cap rate needed to get back to \$62 million in five years; and the forward-looking return on holding, at market value.

**Solution.**

Market value $= 2{,}650{,}000/0.056 = \$47{,}321{,}429$, a 23.7% decline from basis (\$14,678,571).

Equity: invested $62{,}000{,}000 - 40{,}300{,}000 = \$21{,}700{,}000$. Equity at market $= 47{,}321{,}429 - 40{,}300{,}000 = \$7{,}021{,}429$. Net cash from a sale today after 2% selling costs: $47{,}321{,}429 \times 0.98 - 40{,}300{,}000 = \$6{,}075{,}000$.

To reach a \$62 million gross price at the end of Year 5 at a 5.60% cap, Year 6 NOI must be $62{,}000{,}000 \times 0.056 = \$3{,}472{,}000$. From \$2,650,000 in Year 1, that requires growth of $(3{,}472{,}000/2{,}650{,}000)^{1/5} - 1 = 5.55\%$ a year for five years.

Alternatively, at 3% growth (Year 6 NOI \$3,072,076), the exit cap must fall to $3{,}072{,}076/62{,}000{,}000 = 4.95\%$.

Forward-looking unlevered return on holding, at market value, 3% growth, exit at 5.60%, ignoring costs: by §9.4.5, **8.60%** (= 5.60% + 3.00%).

Levered: treat the \$6,075,000 of net sale proceeds as the equity the owner reinvests by not selling. Annual interest $= 0.065 \times 40{,}300{,}000 = \$2{,}619{,}500$. Equity flows $[-6{,}075{,}000;\ 30{,}500;\ 110{,}000;\ 191{,}885;\ 276{,}227;\ 13{,}824{,}434]$, where Year 5 includes a sale at 5.60% on Year 6 NOI less 2% and repayment of \$40.3 million. Levered IRR **19.29%**.

**Decision consequence.** The basis enters none of the forward-looking numbers. The owner's real choice is between \$6.08 million of cash today and a levered position whose expected return is about 19% if NOI grows 3% and cap rates hold, with the property at 85% loan-to-value and near-zero cash flow after interest. That can be a reasonable bet. But it should be made on that arithmetic, not on the \$62 million. The anchor matters only through three channels: (1) tax, since realizing a loss has value and the timing of recapture matters; (2) the loan, which matures at a balance that market value barely covers; and (3) reporting, because a sale crystallizes a loss that an appraisal can defer. For a buyer, the anchor predicts behavior. This owner will not sell voluntarily until either the loan forces the issue or the owner's lenders or investors stop accepting the appraisal. Price your patience accordingly; Case B treats the refinancing cliff.

Reproduce: `tests/test_ch09_examples.py::test_example_9_11`.

#### Example 9.12 — Anchoring case II: the office owner and the 2021 appraisal

**Given.** The §9.1 office building. The 2021 appraisal capitalized T-12 NOI of \$3,510,000 at 6.75%: \$52,000,000. Current T-12 NOI is \$3,400,000. Assume today's market cap rate for a **stabilized** multi-tenant suburban office building with no near-term rollover is 8.00% [HYPOTHESIS]. Your DCF value is \$34,820,005 (Example 9.3).

**Find.** Decompose the decline from the appraisal to your value.

**Solution.**

| Step | Value | Change |
|---|---:|---:|
| 2021 appraisal: \$3,510,000 / 6.75% | 52,000,000 | |
| Current T-12 NOI at the 2021 cap: \$3,400,000 / 6.75% | 50,370,370 | −1,629,630 (NOI) |
| Current T-12 NOI at today's stabilized cap: \$3,400,000 / 8.00% | 42,500,000 | −7,870,370 (cap rate) |
| DCF with Tenant A rollover, TI/LC, downtime | 34,820,005 | −7,679,995 (rollover and capital) |
| **Total** | | **−17,179,995 (−33.0%)** |

**Decision consequence.** Less than 10% of the decline comes from NOI the owner can see on the T-12. The rest comes from two things the appraisal did not show. One is the market's repricing of office risk. The other is that a 30% tenant's lease, which had years left in 2021, now expires in twelve months. Lease term decays with time even if nothing else changes: the same building is a different asset with one year of term left than with five. The appraisal was an opinion at a date. It used a method (direct cap on T-12) that cannot see rollover. The owner who quotes it is quoting a stale answer to a question that has since changed. Show the owner this table. The NOI line is undeniable, the cap-rate line is visible in comparable sales, and the rollover line is the subject of a leasing study the owner can verify. Each line is evidence, not opinion. That is the only route to closing a 33% bid–ask gap without waiting for a maturity to close it for you.

Reproduce: `tests/test_ch09_examples.py::test_example_9_12`.

#### Example 9.13 — Anchoring case III: the retail owner and replacement cost

**Given.** A 95,000 sf grocery-anchored neighborhood center built in 1998. NOI \$1,710,000 (\$18.00/sf). Market cap rate 7.75%. The owner cites a contractor's estimate of replacement cost at \$310/sf, including land: \$29,450,000. "Nobody can build this for less, so it's worth at least that." A developer would require a 15% margin on cost.

**Find.** Market value; implied total depreciation from replacement cost; the NOI and rent that new construction would require.

**Solution.**

Market value $= 1{,}710{,}000/0.0775 = \$22{,}064{,}516$ (\$232.26/sf).

Implied total depreciation (physical, functional, external) $= 1 - 22{,}064{,}516/29{,}450{,}000 = 25.1\%$.

For a developer to build: value must reach $29{,}450{,}000 \times 1.15 = \$33{,}867{,}500$. At 7.75% that requires NOI of \$2,624,731, or \$27.63/sf, which is **53.5% above** the subject's \$18.00/sf.

**Decision consequence.** Replacement cost tells you that new competing centers will not be built until rents rise by about half. That protects the subject's income from new supply, which is worth something and belongs in the growth and exit assumptions. It does not make the building worth \$29.45 million. A 28-year-old center with a 1998 layout, parking ratio, and tenant mix carries functional and external obsolescence that a new building does not. The market measures that obsolescence at about 25%. An owner who will not sell below replacement cost has, in effect, decided not to sell. A buyer should spend no time on the argument and instead look for the event that will change the owner's position: the anchor's renewal, a loan maturity, or an estate.

Reproduce: `tests/test_ch09_examples.py::test_example_9_13`.

#### Example 9.14 — Appraisal smoothing and unsmoothing

**Given.** True market value of a portfolio is 100 at $t=0$ and falls to 75 at $t=1$, then stays there. Appraisals follow $A_t = 0.6A_{t-1} + 0.4V_t$ with $A_0 = 100$.

**Find.** The appraisal path for four periods, and the value recovered by unsmoothing.

**Solution.**

| $t$ | True $V_t$ | Appraisal $A_t$ | Appraisal change | Unsmoothed $(A_t - 0.6A_{t-1})/0.4$ |
|---|---:|---:|---:|---:|
| 0 | 100 | 100.00 | | |
| 1 | 75 | 90.00 | −10.0% | 75.00 |
| 2 | 75 | 84.00 | −6.7% | 75.00 |
| 3 | 75 | 80.40 | −4.3% | 75.00 |
| 4 | 75 | 78.24 | −2.7% | 75.00 |

After three periods the appraisal has recognized $(100 - 80.40)/25 = 78.4\%$ of the decline; after four, 87.0%.

**Decision consequence.** An appraisal-based index that falls 10% while a listed-market index falls 25% is consistent with both measuring the same 25% decline, if appraisals smooth with $\alpha = 0.6$. The smoothing parameter is not known in real time and varies across cycles. The arithmetic therefore does not tell you the true decline. It tells you that a small appraisal decline is weak evidence against a large one. Any capital decision tied to appraised values inherits the lag: fund NAVs, LTV covenants, redemption prices in open-end funds, and the owner anchoring of Examples 9.11–9.12.

Reproduce: `tests/test_ch09_examples.py::test_example_9_14`.

---

### 9.6 CRE application: the valuation reconciliation memo

Professional valuation is reconciliation, not calculation. A good memo states each method's indication, explains the gaps, and chooses. For the §9.1 office building:

| Method | Indication | What drives it | Weight and reason |
|---|---:|---|---|
| DCF (Ex 9.3) | \$34.8m | Re-leasing Tenant A, 8.25% exit cap, 9.0% $k$ | Primary. The cash-flow profile is irregular, so only a DCF can see it |
| Direct cap, stabilized cap on T-12 (Ex 9.12) | \$42.5m | T-12 NOI at 8.00% | Upper bound. It assumes the rollover costs nothing |
| Sales comparison | Not shown | Few recent suburban office sales; many are distressed | Low weight. Comps are stale and selected |
| Replacement cost | \$66m | Construction cost | No weight as value evidence. Tells you there will be no new supply |
| Seller's ask | \$48.6m | 7.0% on T-12 | Evidence of the seller's anchor, not of value |

The reconciliation also says what would change the answer: a signed renewal by Tenant A (value rises toward the direct-cap upper bound), or evidence that suburban office sales are clearing at 9%+ caps (value falls).

#### Buyer and seller expectations: the negotiation zone

A transaction requires a price above the seller's reservation price and below the buyer's. The seller's reservation price comes from the anchor, the alternatives (refinance, hold), and constraints (maturity, fund life). The buyer's comes from the DCF. When the two do not overlap, as here (\$34.8 million versus an owner who will not accept much below \$48 million), no amount of negotiating closes the gap. One of three things must happen:

1. **Information changes the buyer's number.** For example, Tenant A renews.
2. **A constraint changes the seller's number.** For example, the loan matures and the lender will not extend; Case B.
3. **Structure bridges the gap.** For example, an earn-out tied to re-leasing, seller financing, or a master lease on the vacant space.

A speculator's edge is often knowing which of the three is coming, and when.

---

### 9.7 When the relationships fail

1. **$k - g$ breaks when $g$ is not stable.** The Gordon form assumes constant growth forever. For an asset in lease-up, repositioning, or structural decline, use an explicit DCF and apply $k - g$ only to the stabilized terminal period.
2. **Cap rates on thin markets are not prices.** When few assets trade, the "market cap rate" is an appraiser's or broker's opinion, and the trades that do occur are selected (Example 9.6). Reported cap rates can lag reality by several quarters.
3. **Replacement cost fails as a ceiling when construction is constrained.** Zoning, entitlement risk, or a shortage of labor or materials can keep value above replacement cost for years. It fails as a floor always.
4. **The DCF fails quietly when the reversion dominates.** At a 75% reversion share, the DCF is a cap-rate forecast with some cash flows attached. Precision in the operating years cannot compensate for an arbitrary exit cap.
5. **IRR decompositions are order-dependent and ignore risk.** A higher IRR from cap compression is not equivalent to a higher IRR from contractual rent. Decompose, then weight by how confident you are in each component.
6. **Leverage arithmetic assumes the loan survives.** Equity IRR grids assume no covenant breach and a successful refinance or sale at exit. If value falls far enough to breach an LTV or DSCR covenant, cash flow is swept and the hold period may be chosen by the lender, not by you (Case C).
7. **Appraisal smoothing is not stable.** Unsmoothing with a fixed $\alpha$ assumes appraisers behave the same in every cycle. Regulatory pressure, auditor scrutiny, and transaction volume all change how fast appraisals move.

---

### 9.8 Mispricing in practice: where anchors bind

Anchors matter for prices only when the anchored party is the marginal seller. Three conditions make anchors bind:

* **No forced sellers.** If most owners have long-dated, fixed-rate debt and no redemption pressure, anchored owners simply hold. Volume falls and reported prices barely move.
* **Appraisal-based accounting.** If fund NAVs, bank collateral values, and compensation are tied to appraisals, owners have an incentive to avoid trades that would set a lower mark.
* **Optionality in waiting.** A levered owner near zero equity holds a call option on recovery (Example 9.11; Case C). Selling exercises it at zero. Waiting is rational for the owner even if it is irrational for a hypothetical unlevered owner.

Anchors stop binding when a constraint forces the marginal transaction: a loan maturity without an extension, a fund wind-down, or redemption queues in open-end funds. The speculator's question is therefore not "Is the owner anchored?" but "When does the anchored owner stop being the marginal seller?"

---

### 9.9 Historical episode: appraisal lag and public–private divergence, 2008–09 and 2022–24

**Date and environment.** Two episodes. In 2008, U.S. credit markets seized after the failure of major financial institutions. In 2022, the Federal Reserve raised policy rates rapidly from near zero, and office demand faced a post-pandemic shift to remote and hybrid work. In both, listed REIT prices and private appraisal-based indices gave very different readings of the same underlying property market for a year or more.

**What was observable at the time.**

*2008–09.*

* The FTSE NAREIT All REIT Index ended 2008 with a total return of −37.34% [FACT; Nareit, January 2009, VERIFIED-SECONDARY; ch09-S01]. The FTSE NAREIT Equity REIT Index was up 1.76% for 2008 through 30 September and down 30.47% through 31 October [FACT; Nareit media updates, autumn 2008, VERIFIED-SECONDARY; ch09-S02]. Most of the 2008 REIT decline therefore occurred in the fourth quarter.
* The FTSE NAREIT Equity REIT Index returned 27.99% in 2009 [FACT; Nareit, December 2009 media update, and a 2009 mutual-fund annual report filed with the SEC; VERIFIED-SECONDARY; ch09-S03].
* NCREIF reported in 2024 that the NCREIF Property Index's value fell by almost 30% during the 2008–09 financial crisis [FACT; NCREIF press release, 25 July 2024, VERIFIED-SECONDARY; ch09-S04]. The calendar-year path of that decline (how much in 2008 versus 2009 and 2010) is *(verification pending)* and is not stated here.

*2022–24.*

* In 2022 the FTSE Nareit All Equity REITs Index returned −24.9%, its steepest annual decline since 2008. Office REITs returned −37.6%, the worst of any sector [FACT; Nareit year-end 2022 commentary, VERIFIED-SECONDARY; ch09-S05].
* The NCREIF Property Index returned 5.53% for calendar 2022. The fourth quarter was −3.50%: income +0.95%, appreciation −4.45% [FACT; LaSalle Investment Management review of NCREIF data, VERIFIED-SECONDARY; ch09-S06]. Capital Economics described Q4 2022 as the weakest quarter for NPI total returns since Q2 2009 [FACT; same source family, ch09-S06].
* The NPI returned −3.02% in Q4 2023 (income +1.11%, appreciation −4.13%) and −7.95% over the four quarters of 2023 [FACT; NCREIF 4Q2023 press release, 25 January 2024, VERIFIED-SECONDARY; ch09-S07].
* NCREIF's Expanded NPI market-value index had declined by about 16% from its 2Q2022 peak as of 1Q2024 [FACT; NCREIF 1Q2024 Expanded NPI release, VERIFIED-SECONDARY; ch09-S08].
* Green Street's Commercial Property Price Index, a transaction-based index, was reported in November 2023 as 22% below its March 2022 peak, with office down 35% [FACT as publicly reported by trade press citing Green Street; class C, VERIFIED-SECONDARY; ch09-S09].
* The Federal Reserve's Financial Stability Reports from 2023 onward identified commercial real estate valuations, especially office, as a risk to financial stability and noted weak fundamentals and tighter bank lending standards [FACT; Federal Reserve Board FSR, October 2023, as summarized in trade press; VERIFIED-SECONDARY; ch09-S10]. The precise price statistics cited in that report, including the price measure used, are *(verification pending)* against the primary PDF.

**Interpretations.**

1. *Appraisal lag (the dominant interpretation).* Appraisal-based indices move slowly because appraisers rely on past transactions and adjust incrementally. Listed REITs reprice continuously. In 2022 the gap was about 30 percentage points: −24.9% versus +5.53%. The NPI's subsequent negative returns through 2023 and the cumulative 16% value decline by early 2024 are consistent with the private index catching up [INFERENCE from the sequence of documented returns].
2. *Leverage and composition, not just lag.* REIT returns are levered equity returns, and REIT portfolios differ from NPI portfolios in property type and quality. A rough unlevering at a hypothetical 35% debt ratio and a 4% debt return gives $0.65 \times (-24.9\%) + 0.35 \times 4.0\% = -14.8\%$ [HYPOTHESIS: illustrative leverage and debt return; not a measured REIT leverage ratio]. A large gap remains after this adjustment: about 20.3 percentage points against 5.53%, roughly two-thirds of the raw 30.4-point gap. Comparing a levered equity index with an unlevered property index overstates the divergence.
3. *Liquidity overshooting.* Listed prices may overshoot fundamental value when forced sellers of liquid assets sell what they can (Chapter 1, §1.9; Chapter 3). On this view, REIT prices in late 2008 and 2022 were too low, not appraisals too high. The rapid REIT rebound in 2009 (27.99%) is consistent with partial overshooting, but it does not prove it.

**What a speculator could have done then.** In late 2008 and in 2022, investors could observe REIT-implied values well below appraisal values. Strategies available at the time included: buying listed REITs at discounts to private NAV (betting on overshooting); delaying private acquisitions or bidding at REIT-implied cap rates (betting on lag); and selling interests in open-end private funds at appraisal-based NAV before marks caught up. The last strategy was available only until redemption queues formed. Redemption queues in large open-end funds in 2022–23 were widely reported *(verification pending: specific funds and queue sizes are not stated here until checked against primary filings)*.

**What the episode establishes.** Appraisal-based indices lagged transaction-based and listed-market indicators in both episodes. Investors and lenders who relied on appraisals for marks, covenants, or redemption prices made decisions on stale information.

**What it does not establish.** It does not establish that REIT prices are always the "true" value; overshooting is a live alternative. It does not establish a stable smoothing parameter or a reliable lead time. The lead varied between episodes, and the 2022–24 divergence was concentrated in office. It does not establish that the gap is exploitable after costs, because private assets cannot be shorted and REITs differ from private portfolios in leverage and composition.

**CRE connection.** In Example 9.12 the 2021 appraisal is the owner's anchor. The episode shows the institutional version of the same problem: an entire asset class marked to anchors for several quarters. Example 9.14 provides the arithmetic.

---

### 9.10 Decision exercise: the office bid

Return to §9.1. You have the DCF (Example 9.3), the implied-growth analysis (Example 9.4), and the appraisal decomposition (Example 9.12). Write a one-page recommendation on the template at `desk/investment_memos/investment_committee_memo.md`. It must include:

1. Your value range, with the two or three assumptions that drive it, stated as forecasts.
2. Whether to bid now, and if so at what price and on what conditions. Consider an earn-out tied to re-leasing Tenant A's space.
3. What the seller must believe to accept your bid, and what would change the seller's position (debt maturity, fund life, appraisal reset).
4. Which of the broker's three anchors you would address in the bid letter, and how.
5. Walk-away triggers and the information that would raise or lower your bid.
6. Whether abstaining and setting a re-engagement trigger is the better choice.

**Rubric.** Score each element 0–4.

| Element | Full credit (4) | Partial (2) | None (0) |
|---|---|---|---|
| Value | DCF-based range of about \$32–38m with exit cap and re-leasing as stated drivers; reversion share noted | Single point estimate | Uses T-12 × cap, or the appraisal |
| Implied beliefs | Computes the 3.05% implied growth or the 1.44% IRR at ask; explains why the ask is not a price an informed buyer pays | Notes the ask is high, no numbers | Accepts the ask as market |
| Bid structure | Bid near DCF value, or a lower base price with an earn-out; diligence conditions on Tenant A | Bid without structure | Bids the ask or above DCF |
| Anchors | Addresses the appraisal with the decomposition table; dismisses replacement cost as value evidence while noting its supply implication | Mentions anchors qualitatively | Treats any anchor as value support |
| Abstention | Recognizes that no overlap may exist; sets a trigger (maturity, listing expiry, Tenant A decision) | Mentions waiting | Absent |

There is no single correct bid. A pass with a defined re-engagement trigger can earn full marks.

---

### 9.11 Frequent analytical errors

1. **Capitalizing the wrong NOI.** Trailing NOI on a property in transition, or stabilized NOI without deducting the cost and risk of getting there.
2. **Terminal value on trailing NOI.** The reversion capitalizes $NOI_{T+1}$.
3. **Ignoring capex in the cap rate.** $c = k - g$ holds only on free cash flow. Use $c = (k-g)/(1-\kappa)$.
4. **Exit cap = going-in cap by default.** This assumes the building does not age.
5. **Forgetting reassessment.** Capitalizing the seller's tax bill in a reassessment jurisdiction.
6. **Stale comps without time adjustment.** Especially the "best physical match" from before a market move.
7. **Treating replacement cost as a floor.** It is a long-run ceiling, through supply.
8. **Treating basis or a prior appraisal as value.** They predict seller behavior, not value.
9. **Reporting equity IRR without the grid.** Leverage that adds 40 bp to the mean can double the range.
10. **Calling cap compression "value-add."** Decompose the IRR, and pay sponsors for what they control.
11. **Comparing levered REIT returns with unlevered appraisal indices without adjustment.**
12. **Applying a precise discount rate to an arbitrary exit cap.** At a 75% reversion share, the exit cap dominates.

---

### 9.12 Connections to other chapters

* Chapter 2 develops appraisal smoothing and price formation in thin markets in more depth.
* Chapter 3 treats forced selling and reflexive collateral loops, which end anchoring.
* Chapter 6 connects cap rates to Treasury yields and computes the duration of CRE equity.
* Chapter 8 builds the NOI that this chapter capitalizes, including reserves and reassessment.
* Chapter 10 builds the debt-sizing, refinancing, and waterfall mechanics behind Example 9.8.
* Chapter 11 values hotels, where the NOI-versus-EBITDA and PIP issues of Case A dominate.
* Chapter 12 treats REIT-implied cap rates and distressed cycles.
* Chapter 13 treats hold/sell and the option value of waiting.
* Case A applies the loaded cap rate and the cost-basis anchor to a hotel. Case B treats the refinancing cliff. Case C applies this chapter's leverage arithmetic to a cap-rate shock.

---

### 9.13 One-page reference sheet

| Quantity | Formula |
|---|---|
| Direct cap | $V = NOI_1/c$ |
| DCF | $V = \sum_{t=1}^{T} \frac{NOI_t - CapEx_t}{(1+k)^t} + \frac{(1-s)NOI_{T+1}/c_T}{(1+k)^T}$ |
| Reversion share | $PV(\text{net reversion})/V$ |
| Cap rate with capex | $c = (k-g)/(1-\kappa)$ |
| Implied growth | $g = k - c(1-\kappa)$ |
| Implied return | $k = c(1-\kappa) + g$ |
| IRR identity | IRR $= c_0 + g$ if flat cap, no capex, no costs |
| Exit spread from aging | $\frac{k-g_T}{1-\kappa_T} - \frac{k-g_0}{1-\kappa_0}$ |
| Loaded cap | $V = N/(c+t)$; $t$ = tax rate × assessment ratio |
| As-is value | Stabilized value − cost to stabilize (− risk discount) |
| Residual land | $L = GDV(1-s)/(1+m) - (H+S+F)$ |
| Developer margin | $GDV(1-s)/\text{total cost} - 1$ |
| Levered return (1 period) | $r_E = r_A + \frac{\lambda}{1-\lambda}(r_A - r_D)$ |
| Cash leverage test | Cap rate vs loan constant $K$ |
| Appraisal smoothing | $A_t = \alpha A_{t-1} + (1-\alpha)V_t$ |
| Unsmoothing | $V_t = (A_t - \alpha A_{t-1})/(1-\alpha)$ |

**Questions to ask of any price.** Which NOI? Forward or trailing? After reserves and capex? Reassessed tax? What growth and exit cap does it imply? What share of value is the reversion? Which part of the IRR is business plan and which is market? Who is the marginal buyer, and what must they believe? What anchor is the seller using, and what event will release it?

**Rules of thumb (test them, do not trust them).** A 100 bp exit-cap move changes a 5-year property IRR by about 300 bp at 5–6% caps (Example 9.9). Reversion is 60–80% of a 5-year DCF. Residual land value moves 10–20 times as much as GDV in percentage terms (Example 9.7). An appraisal index may show only a third to a half of a sudden decline in the first year [HYPOTHESIS; Example 9.14 uses $\alpha = 0.6$].

---

### References for this chapter

Source entries with IDs and verification status are in `references/sources_ch09.md`.

* Geltner, D. (1993). "Estimating Market Values from Appraised Values without Assuming an Efficient Market." *Journal of Real Estate Research*, 8(3), 325–345.
* Kahneman, D., and Tversky, A. (1979). "Prospect Theory: An Analysis of Decision under Risk." *Econometrica*, 47(2), 263–291.
* Tversky, A., and Kahneman, D. (1974). "Judgment under Uncertainty: Heuristics and Biases." *Science*, 185(4157), 1124–1131.
* Nareit. Media updates and market commentary, October 2008, January 2009, December 2009, and year-end 2022. https://www.reit.com
* NCREIF. NPI press releases for 4Q2023 (25 January 2024), Expanded NPI 1Q2024, and Expanded NPI 2Q2024 (25 July 2024). https://ncreif.org
* LaSalle Investment Management (2023). "U.S. Private Real Estate Returns Review, 2022 Q4."
* Board of Governors of the Federal Reserve System. *Financial Stability Report*, October 2023.
* Green Street Commercial Property Price Index, as publicly reported in November 2023 trade press coverage.


\newpage

## Chapter 10 — Capital Structure, Debt, and Equity

> **Status:** Complete (v1.0). Numerical examples are reproduced in `tests/test_ch10_examples.py`. Problems are in `problems/questions/ch10_problems.md` and solutions in `problems/solutions/ch10_solutions.md`. Sources are listed in `references/sources_ch10.md`. One item, the size of trade-press-reported replacement-cap price increases, is marked *(verification pending)* and is not used as a number. Drills D046–D055. Case B (`cases/hypothetical/case_B_refinancing_cliff/`) applies the chapter.

### Learning objectives

After this chapter you should be able to:

1. Size a commercial mortgage under loan-to-value (LTV), debt service coverage (DSCR), and debt-yield constraints. Identify the binding constraint and find the interest rate at which the binding constraint changes.
2. Compute payments, loan constants, amortization, and balloon balances, including loans with an interest-only (IO) period, both in Python and on an HP-12C.
3. Analyze floating-rate debt: index plus spread, interest-rate caps, DSCR sizing at the cap strike, the price of a cap under the normal (Bachelier) model, and why replacement caps became a solvency problem when forward rates rose.
4. Read a capital stack by attachment and detachment points. Allocate value losses across senior debt, mezzanine debt, preferred equity, and common equity, and explain what an intercreditor agreement changes.
5. Run an IRR-hurdle waterfall with `sdesk.cre.irr_hurdle_waterfall`, explain catch-up provisions, and value the sponsor's promote as an option on the upside.
6. Compute a refinancing gap and decompose it into its causes. Analyze covenants, cash traps, and cures.
7. Value the borrower's default option under non-recourse debt, and show how carve-out ("bad boy") guarantees change the borrower's behavior.
8. Compute dilution from capital calls under fair-value, book-value, and punitive terms.
9. Price a distressed loan purchase, and explain the lender incentives behind "extend and pretend".

---

### 10.1 Opening investment problem: Ridgeview's rescue request

All facts in this section are [HYPOTHESIS], a constructed teaching case. The same property recurs in Examples 10.3, 10.7, 10.8, and 10.10.

You run the structured-credit allocation of a family office. A sponsor you know asks for \$5.0 million of rescue capital for **Ridgeview**, a 280-unit garden apartment community in a Sun Belt metro.

* The sponsor bought Ridgeview three years ago for \$40.0 million with a \$30.0 million floating-rate bridge loan: 75% LTV at one-month SOFR + 3.25%, interest-only, with a three-year initial term and two one-year extension options. The lender required a two-year interest-rate cap struck at 3.00% SOFR. The sponsor bought it for a few thousand dollars because, at the time, forward SOFR was near zero.
* The business plan was to renovate units and grow NOI from \$2.1 million to \$2.8 million. Renovations are about half done. Insurance and payroll costs rose. NOI is still \$2.1 million.
* SOFR is now above the strike. The original cap has expired, and a replacement cap has been bought once, out of reserves. The current replacement cap expires in two months. The lender requires another replacement cap as a condition of the extension, and the lender has started trapping all excess cash because DSCR and debt yield are below their triggers.
* Comparable sales suggest a 7.75% cap rate on in-place NOI, which implies a value of about \$27 million. The loan balance is \$30.0 million.

The sponsor proposes \$5.0 million of **preferred equity** at a 12% current-pay rate, senior to the sponsor's common equity. Proceeds would buy the replacement cap, pay down the loan enough to release the cash trap, and finish the renovations. Separately, a broker tells you that the senior lender, a regional bank, would sell the \$30.0 million note at 80 cents on the dollar.

You have three choices: fund the preferred equity, buy the note, or do nothing. By the end of the chapter you will be able to value each one. Section 10.10 returns to the decision.

---

### 10.2 Economic intuition: debt is a short put on the property

Start from the payoff at maturity. A non-recourse lender with balance $B$ receives $\min(V, B)$, where $V$ is the property's value. The equity holder receives $\max(V - B, 0)$. The identity

$$\min(V,B) = B - \max(B - V, 0)$$

says that the lender owns a riskless claim of $B$ **minus a put option** on the property struck at $B$. The borrower bought that put. The borrower's equity is a **call** on the property. Every topic in this chapter follows from this structure:

* **Loan sizing** limits how far in the money the put can drift. LTV caps the strike relative to value. DSCR and debt yield cap it relative to income, which is harder to manipulate than an appraisal.
* **Amortization** lowers the strike over time. Interest-only debt keeps it constant. A balloon is the strike that must be refinanced.
* **Covenants and cash traps** let the lender act before maturity, when the put is moving into the money but has not yet been exercised.
* **Recourse and carve-out guarantees** take away part of the put. They make the borrower pay for specific bad acts, which changes what the borrower does when equity is underwater.
* **Mezzanine debt and preferred equity** split the claim between senior debt and common equity into further layers. Each layer is a call spread on the property: it gains nothing above its detachment point and loses everything below its attachment point.
* **The promote** is a call on the equity, which is a call on the property: a compound option. It makes the sponsor's payoff convex. Convex payoffs reward volatility, so a sponsor with an out-of-the-money promote prefers risk.
* **Refinancing risk** is the risk that, at maturity, the strike exceeds what new lenders will advance. The put is then exercised not because the property is worthless, but because nobody will refinance the strike.

Two consequences matter in practice.

**First, the option view explains behavior that cash-flow analysis cannot.** When $V < B$, equity is worth more than zero only because of time value. A sponsor with one more year of optionality will pay something for an extension even though the equity is "underwater". A lender who forecloses gives up nothing in option terms. The bargaining zone between them is computable (Example 10.8).

**Second, leverage is not a return; it is a transfer of risk.** The lender is short volatility. The equity is long volatility. The promote is longer still. When a lender's incentives (avoid recognizing losses) and a sponsor's incentives (keep the option alive, keep the fees) align against an outside investor, the result is "extend and pretend" (§10.8 and Example 10.10).

---

### 10.3 Technical definitions

| Term | Definition |
|---|---|
| Loan-to-value (LTV) | $L/V$. Value is an appraisal or the purchase price, whichever is lower, in most acquisition loans |
| Loan-to-cost (LTC) | $L/\text{total project cost}$. Used for construction and value-add loans, where "value" is a forecast |
| Debt service ($DS$) | Annual interest plus scheduled principal. For IO loans, interest only |
| Loan constant ($K$) | $DS/L$, annual debt service per dollar of loan. For IO debt $K = r$ |
| DSCR | $NOI/DS$, or underwritten net cash flow (NCF) / $DS$. Lenders specify which numerator |
| Debt yield ($DY$) | $NOI/L$. Independent of rate and amortization, so it cannot be gamed by IO or a low coupon |
| Balloon | Balance due at maturity, $B_T$ |
| Amortization term vs loan term | Amortization sets the payment (e.g., 30 years). Term sets maturity (e.g., 10 years). The difference creates the balloon |
| Index + spread | Floating rate = reference rate (SOFR in the U.S. since the end of LIBOR) + a fixed credit spread |
| Interest-rate cap | A strip of call options (caplets) on the index. Each pays notional × accrual × max(index − strike, 0) |
| Sizing at strike | DSCR computed at strike + spread, the worst-case rate when a cap is in place |
| Cash trap / sweep | After a trigger (DSCR or DY below a level), excess cash is held by the lender or applied to principal |
| Cash management | Hard lockbox (tenants pay into a lender-controlled account) or springing lockbox (activated on a trigger) |
| Recourse | The lender can pursue the borrower's or guarantor's other assets for a deficiency |
| Non-recourse carve-out ("bad boy") guarantee | A guarantee that converts non-recourse into recourse for specified acts. *Loss* carve-outs (misapplied rents, waste, environmental) cover actual losses. *Springing full recourse* (voluntary bankruptcy, unpermitted transfer or financing) makes the full debt recourse |
| Mezzanine loan | A loan secured by a pledge of the equity interests in the property-owning entity. Remedy: a UCC foreclosure on the equity, usually much faster than a mortgage foreclosure |
| Preferred equity | An equity interest with a priority return and, often, control rights on default. It is not debt and has no lien |
| Attachment / detachment | The cumulative LTV at which a tranche's claim begins (attachment) and ends (detachment), measured on original value. A mezz loan "from 60% to 75%" sits behind 60% of senior debt and ahead of everything above 75% |
| Intercreditor agreement | Contract between senior and mezzanine lenders: cure rights, purchase option, standstill, and what the mezz lender must do to take control |
| Waterfall | Rules for splitting equity cash flows between investors (LP) and sponsor (GP) |
| Preferred return ("pref") | Return investors receive before the promote applies, often 8%, usually compounding |
| Catch-up | After the pref, a tier in which the GP receives most or all distributions until it holds its target share of total profit |
| Promote (carried interest) | The GP's disproportionate share above hurdles |
| Refinancing gap | Balance + refinancing costs − new loan. Positive means equity must be contributed |
| Capital call dilution | Reduction in a non-funding partner's ownership when others fund a call |
| Discounted payoff (DPO) | Lender accepts less than the balance in full satisfaction |
| Deed-in-lieu | Borrower conveys the property to the lender instead of a contested foreclosure |
| Extend and pretend | Extending a loan whose collateral no longer supports it, to defer loss recognition |

Convention for attachment points: a 60–75% mezzanine loan is repaid in full if $V \ge 0.75\,V_0$, is partly impaired for $0.60\,V_0 < V < 0.75\,V_0$, and is wiped out if $V \le 0.60\,V_0$. Equivalently, it is impaired once value falls more than 25% and wiped out once value falls 40% or more. Accrued but unpaid interest or preference, which raises a tranche's claim over time, is ignored in this convention and must be added when a claim has been accruing.

---

### 10.4 Equations and derivations

#### 10.4.1 Payment, loan constant, and balance

With monthly rate $i = r/12$ and $n$ amortization months, the level payment solves $L = PMT \cdot a_{\overline{n}|i}$, where $a_{\overline{n}|i} = (1-(1+i)^{-n})/i$:

$$PMT = \frac{L\,i}{1-(1+i)^{-n}}, \qquad K = \frac{12\,PMT}{L} = \frac{12\,i}{1-(1+i)^{-n}}.$$

$K$ depends only on rate and amortization, not on the loan amount. That is why lenders size on it.

The balance after $k$ payments has two equivalent forms. **Prospectively**, it is the present value of the remaining payments:

$$B_k = PMT \cdot a_{\overline{n-k}|i}.$$

**Retrospectively**, it is the loan accumulated at $i$, less accumulated payments:

$$B_k = L(1+i)^k - PMT\,\frac{(1+i)^k - 1}{i}.$$

The two agree because the payment was set so that the loan's present value equals the payments' present value. Tests use both forms as independent checks.

With an IO period of $m$ months followed by amortization on an $n$-month schedule, the balance during IO stays at $L$, and the balance at month $T > m$ is $B_{T-m}$ computed on the original schedule. The IO period does not change the amortization payment. It delays principal reduction and raises the balloon.

#### 10.4.2 Sizing: three constraints, one loan

$$L^* = \min\left(\lambda_{max} V,\; \frac{NOI}{DSCR_{min}\,K},\; \frac{NOI}{DY_{min}}\right).$$

The DSCR constraint binds instead of LTV when $NOI/(DSCR_{min} K) < \lambda_{max} V$. Substituting $V = NOI/c$:

$$\text{DSCR binds} \iff K > \frac{c}{\lambda_{max}\,DSCR_{min}}.$$

The crossover loan constant depends only on the cap rate and the two covenants. At $c = 6.00\%$, $\lambda_{max} = 65\%$, $DSCR_{min} = 1.25$, the crossover is $K^* = 0.06/0.8125 = 7.385\%$, which a 30-year loan reaches at about 6.24% (Example 10.1). When rates rise and cap rates do not, DSCR takes over from LTV as the binding constraint. That is the first channel through which rate increases shrink loan proceeds, even before values fall.

For IO debt, the DSCR and debt-yield tests are linked:

$$\frac{NOI}{L\,r} \ge DSCR_{min} \iff \frac{NOI}{L} \ge DSCR_{min}\, r.$$

A 1.20x IO DSCR test at 6.25% is the same constraint as a 7.50% debt-yield test. Example 10.7 uses this identity.

#### 10.4.3 Floating-rate debt and caps

Interest on floating debt is $L(I + s)$ where $I$ is the index and $s$ the spread. With a cap struck at $K_{cap}$ on the index, the borrower's net interest is $L(\min(I, K_{cap}) + s)$, and the cap pays $L\max(I - K_{cap}, 0)$ per year. Lenders size such loans at the worst-case rate: $DSCR = NOI / [L(K_{cap} + s)]$.

A cap is a strip of caplets. This book prices caplets with normal (basis-point) volatility, because lognormal volatility explodes as the forward rate approaches zero, which makes it unusable for the near-zero forwards of 2020–2021 [INFERENCE from the model's mathematics; dealer quoting conventions vary and are not sourced here]. Under the normal (Bachelier) model a caplet fixing at $T$, covering accrual $\tau$, paid with discount factor $P$, on forward rate $F$ with normal volatility $\sigma_N$ is worth

$$c = N\,\tau\,P\left[(F - K)\,\Phi(d) + \sigma_N\sqrt{T}\,\phi(d)\right], \qquad d = \frac{F - K}{\sigma_N \sqrt{T}}.$$

Two terms matter. $(F-K)\Phi(d)$ is intrinsic value weighted by exercise probability. $\sigma_N\sqrt T\,\phi(d)$ is time value. When the forward is far below the strike, both are near zero and the cap is cheap. When the forward is above the strike, the cap is mostly intrinsic value: the borrower prepays, in cash, the interest the cap will save. **A deep in-the-money cap does not hedge anything. It converts future interest into an upfront payment.** That was the economics of replacement caps after 2022 (§10.9). Chapter 18 develops caps, floors, and swaptions fully.

#### 10.4.4 Capital stack loss allocation

Let tranches $j = 1,\dots,J$ be ordered senior to junior with amounts $A_j$ summing to $V_0$. A value decline $\Delta = V_0 - V$ is allocated from the bottom. The loss to tranche $j$ is

$$\ell_j = \min\left(A_j,\; \max\left(\Delta - \sum_{k>j} A_k,\; 0\right)\right).$$

Attachment $a_j = \sum_{k<j}A_k/V_0$; detachment $d_j = a_j + A_j/V_0$. Tranche $j$ is impaired once value falls by more than $1 - d_j$ and wiped out once it falls by more than $1 - a_j$.

#### 10.4.5 Waterfall mechanics

`sdesk.cre.irr_hurdle_waterfall` accrues one balance per hurdle $h$ at rate $h$ on contributions net of investor distributions. Distributable cash first goes to investors at the tier-1 split until the first balance is zero (investors have earned $h_1$), then at the tier-2 split until the second balance is zero, and so on. The investor IRR exceeds $h$ if and only if the final balance for $h$ is $\le 0$.

A **catch-up** changes the second tier. On a single terminal distribution $D$ against contribution $C$ over $T$ years with pref rate $h$ and carry share $\pi$:

1. Return of capital: $\min(D, C)$ to investors.
2. Pref: $p = \min(D - C, C[(1+h)^T - 1])$ to investors.
3. Catch-up: the GP receives a share $\gamma$ of each dollar until the GP holds $\pi$ of all profit distributed. If $x$ dollars flow through this tier, $\gamma x = \pi(p + x)$, so $x = \pi p/(\gamma - \pi)$.
4. Split the rest $(1-\pi)/\pi$.

With a full catch-up ($\gamma = 1$) and enough profit, the GP ends with exactly $\pi$ of total profit. The pref then only affects *timing* and *bad outcomes*: it protects investors when profit is low and gives nothing extra when profit is high. Without catch-up ($\gamma = \pi$), the GP's share applies only to profit above the pref.

#### 10.4.6 The refinancing gap

$$G = B_T + C_{refi} - L^*_{new}.$$

If $G > 0$, equity must be contributed or the loan defaults. Write $L^*_{new} = \lambda_{new} NOI_T / c_T$ when LTV binds. Then the gap rises with the balloon $B_T$, the new cap rate $c_T$, and falls with NOI and the permitted LTV. A **gap attribution** walks from the old loan to the new proceeds one cause at a time (Case B, Mode B).

#### 10.4.7 The borrower's default option

At maturity with balance $B$, a non-recourse borrower who must either repay or hand over the property holds equity worth $\max(V - B, 0)$. If the lender extends for one period for a fee $f$, and $V_1$ is uncertain, the borrower's extension value is

$$E_0 = \frac{E[\max(V_1 - B, 0)]}{1 + k_E} - f.$$

The lender compares extension with foreclosure. With foreclosure costs $\kappa$ as a fraction of value, and recovery in either path received at $t=1$:

$$PV_{ext} = \frac{E[\min(B,\; V_1(1-\kappa))]}{1+k_L} + f, \qquad PV_{fc} = \frac{V_0(1-\kappa)}{1+k_L}\ \text{(time-to-sale one period)}.$$

A bargaining zone exists for fees with $PV_{ext} \ge PV_{fc}$ and $E_0 \ge 0$. A springing-recourse guarantee adds a penalty $B - \text{recovery}$ to any borrower action that triggers it. Its purpose is to make obstruction (for example, a bankruptcy filing to stay foreclosure) unprofitable.

#### 10.4.8 Capital-call dilution

With pre-call fair equity value $E_{pre}$ over $U$ units, a funding partner buys new units at $E_{pre}/U$. If it also funds a non-funding partner's share $c_B$, punitive terms credit it with $\theta c_B$ of contributions ($\theta > 1$). The non-funding partner's post-call ownership is

$$s_B' = \frac{U_B}{U + c_A U/E_{pre} + \theta c_B U/E_{pre}}.$$

If new units are issued at fair value and $\theta = 1$, dilution transfers no value: the non-funder keeps the value of its old units. Value transfers come from **pricing** the units away from fair value, in either direction, and from $\theta > 1$.

---

### 10.5 Worked examples

All inputs are hypothetical [HYPOTHESIS]. All ten examples are reproduced in `tests/test_ch10_examples.py`.

#### Example 10.1 — Sizing a loan when rates move the binding constraint

**Given.** Multifamily NOI after reserves \$2,400,000. Appraised value \$40,000,000 (6.00% cap). Lender terms: 30-year amortization, max 65% LTV, min 1.25x DSCR on NOI, min 8.0% debt yield. Quoted rate 6.50%. Compare 6.25% and a 6.50% interest-only quote.

**Find.** Maximum loan, binding constraint, and the rate at which DSCR replaces LTV as binding.

**Solution.**

Loan constant at 6.50%, 30 years: $K = 12 \times 0.0054167/(1 - 1.0054167^{-360}) = 7.5848\%$.

| Constraint | Formula | Loan |
|---|---|---|
| LTV | $0.65 \times 40{,}000{,}000$ | \$26,000,000 |
| DSCR | $2{,}400{,}000 / 1.25 / 0.075848$ | \$25,313,731 |
| Debt yield | $2{,}400{,}000 / 0.08$ | \$30,000,000 |

DSCR binds: $L^* = \$25{,}313{,}731$. Debt service = $1{,}920{,}000$ by construction ($2{,}400{,}000/1.25$). Resulting LTV 63.28%, debt yield 9.48%.

At 6.25%: $K = 7.3886\%$, DSCR loan = \$25,985,956, still marginally below the LTV loan.

Crossover: $K^* = c/(\lambda_{max} DSCR_{min}) = 0.06/(0.65 \times 1.25) = 7.3846\%$. Solving $K(r, 30) = 7.3846\%$ gives $r^* = 6.24\%$.

Interest-only at 6.50%: $K = 6.50\%$, DSCR loan $= 2{,}400{,}000/1.25/0.065 = \$29{,}538{,}462$. LTV binds at \$26,000,000.

**Check.** $25{,}313{,}731 \times 0.075848 = 1{,}920{,}000$ and $2{,}400{,}000/1{,}920{,}000 = 1.25$. ✓

**Decision consequence.** Above about 6.24%, every 25 bp of rate costs about \$0.67 million of proceeds on this asset, because DSCR now binds. The borrower has three levers: accept less leverage, negotiate IO (which restores LTV as the binding test but leaves the balance undiminished at maturity), or buy down the rate with points. IO is the cheapest lever today and the most expensive at maturity: it raises the balloon (Example 10.2) exactly when refinancing is hardest. A lender that permits IO to make a deal "work" on DSCR is relying on value, not income, for repayment.

#### Example 10.2 — Amortization and balloon, with HP-12C keystrokes

**Given.** \$25,000,000 loan, 6.50%, 30-year amortization, 10-year term, monthly payments in arrears. Variant: the first 36 months are interest-only, then amortization on the original 30-year schedule.

**Find.** Monthly payment; annual debt service; year-1 interest and principal; balance after 120 months; total principal and interest paid over the term; the balloon with three years of IO.

**Solution.**

$i = 0.065/12 = 0.0054167$; $n = 360$.

$PMT = 25{,}000{,}000 \times 0.0054167/(1 - 1.0054167^{-360}) = \$158{,}017.01$ per month; $DS = \$1{,}896{,}204$ per year.

Year-1 interest = \$1,616,773; year-1 principal = \$279,431. Only 14.7% of first-year debt service reduces principal.

Balance after 120 payments (prospective form): $B_{120} = 158{,}017.01 \times a_{\overline{240}|i} = \$21{,}194{,}032$.

Principal repaid over 10 years: $25{,}000{,}000 - 21{,}194{,}032 = \$3{,}805{,}968$ (15.2% of the loan). Interest paid: $120 \times 158{,}017.01 - 3{,}805{,}968 = \$15{,}156{,}072$.

**Three years IO.** Months 1–36: payment = $25{,}000{,}000 \times 0.065/12 = \$135{,}417$ ($DS = \$1{,}625{,}000$). Months 37–120: the 30-year payment of \$158,017.01. Balloon = balance after 84 amortizing payments = **\$22,604,061**, which is \$1,410,030 higher than with full amortization.

**HP-12C keystrokes** (END mode; `f 2` display):

| Step | Keys | Display |
|---|---|---|
| Clear | `f` `CLEAR FIN` | |
| Loan | `25000000` `PV` | 25,000,000.00 |
| Rate | `6.5` `g` `12÷` | 0.54 |
| Term | `30` `g` `12×` | 360.00 |
| Payment | `PMT` | −158,017.01 |
| Balloon at month 120 | `120` `n` `FV` | −21,194,031.59 |
| Alternative: amortize 120 payments | (re-enter PV, i, n=360, PMT as above) `120` `f` `AMORT` | −15,156,072.30 (interest) |
| | `x≷y` | −3,805,968.41 (principal) |
| | `RCL` `PV` | 21,194,031.59 |
| IO variant: balloon after 84 amortizing months | `f CLEAR FIN`, `25000000 PV`, `6.5 g 12÷`, `360 n`, `PMT`, then `84` `n` `FV` | −22,604,061.20 |

The `AMORT` function rounds each period's interest to the display setting, so with `f 2` its results can differ from the closed form by a few cents. The `n`/`FV` route uses the unrounded payment held in the PMT register.

**Check.** Retrospective form: $25{,}000{,}000 \times 1.0054167^{120} - 158{,}017.01 \times (1.0054167^{120} - 1)/0.0054167 = \$21{,}194{,}032$, which matches the prospective form. ✓

**Decision consequence.** A 30-year amortization on a 10-year loan retires only 15% of principal. The refinancing risk at year 10 is therefore about 85% of the original loan, and about 90% with three years of IO. Underwriting that focuses on the year-1 DSCR is underwriting the wrong date. The question to ask is: on what NOI, cap rate, and lending terms does a \$21.2 million (or \$22.6 million) balloon refinance in year 10? (§10.6, Example 10.6.)

#### Example 10.3 — Floating-rate debt, the cap, and the cost of replacing it (Ridgeview)

**Given.** Ridgeview at acquisition: value \$40,000,000, NOI \$2,100,000. Bridge loan terms: SOFR + 3.25%, IO, max 75% LTV, min 1.10x DSCR **sized at the cap strike** of 3.00% SOFR. Two-year cap, quarterly caplets, on \$30,000,000. Flat forward curve and normal volatility are hypothetical: at acquisition, forward SOFR 1.25% with normal vol 0.80% (80 bp); at replacement, forward SOFR 4.75% with normal vol 1.20%.

**Find.** (a) The loan amount. (b) Interest and DSCR at SOFR of 0.05% and 5.30%, with and without the cap. (c) The upfront cost of the cap at acquisition and at replacement, as a percentage of notional and as an annual equivalent. (d) The replacement cost at strikes of 4.75% and 5.00%.

**Solution.**

(a) Sizing rate = 3.00% + 3.25% = 6.25%. DSCR loan $= 2{,}100{,}000/1.10/0.0625 = \$30{,}545{,}455$. LTV loan $= 0.75 \times 40{,}000{,}000 = \$30{,}000{,}000$. LTV binds: $L = \$30{,}000{,}000$.

(b)

| SOFR | Unhedged rate | Unhedged interest | DSCR | Capped rate | Capped interest | DSCR | Cap payout/yr |
|---|---|---|---|---|---|---|---|
| 0.05% | 3.30% | \$990,000 | 2.12x | 3.30% | \$990,000 | 2.12x | \$0 |
| 5.30% | 8.55% | \$2,565,000 | 0.82x | 6.25% | \$1,875,000 | 1.12x | \$690,000 |

(c) Caplets $j = 2,\dots,8$ fix at $t = 0.25, \dots, 1.75$ and pay one quarter later; the first period is already fixed. Discount factors use the flat forward compounded quarterly.

* Acquisition ($F = 1.25\%$, $\sigma_N = 0.80\%$): premium **\$3,680**, or 0.012% of notional, about 0.6 bp a year.
* Replacement ($F = 4.75\%$, $\sigma_N = 1.20\%$): premium **\$888,370**, or 2.96% of notional. Dividing by the quarterly annuity of 1.8972 gives an annual equivalent of **156 bp**.

(d) Replacement at a 4.75% strike (at the money): \$226,647. At a 5.00% strike: \$170,675 (30 bp a year).

**Check.** Most of the 3.00%-strike replacement premium is intrinsic value: seven caplets each worth $30{,}000{,}000 \times 0.25 \times (0.0475 - 0.03) \times P_j = 131{,}250\,P_j$ at expiry, summing to \$866,331 discounted. Time value adds the remaining \$22,039. ✓

**Decision consequence.** The original cap was nearly free because it was far out of the money. The same strike, bought when the forward is above it, costs almost 3% of the loan, payable in cash up front, at the moment the property's cash flow is already absorbed by higher interest. Buying a higher strike lowers the premium but raises the sizing rate, so the loan may fail the extension DSCR test. The cap protects the lender's DSCR. It does not protect the sponsor's liquidity. A sponsor who underwrote "the cap limits our rate risk" was right about the interest rate and wrong about the cash requirement.

#### Example 10.4 — The capital stack: attachment, detachment, and who loses first

**Given.** A \$50,000,000 office acquisition with NOI \$3,250,000 (6.50% cap). Senior loan \$30,000,000 at 6.00%, 30-year amortization (0–60%). Mezzanine \$7,500,000 at 11.0% IO (60–75%). Preferred equity \$5,000,000 at a 12% current-pay preference (75–85%). Common equity \$7,500,000 (85–100%).

**Find.** Coverage at each level; losses by tranche if value falls to \$40.0 million, \$35.0 million, and \$32.5 million; the value declines at which mezz is first impaired and wiped out.

**Solution.**

Senior DS $= \$2{,}158{,}382$ (DSCR 1.51x, DY 10.83%). Mezz DS $= 7{,}500{,}000 \times 0.11 = \$825{,}000$. Combined DSCR $= 3{,}250{,}000/2{,}983{,}382 = 1.09x$. Debt yield through the mezz $= 3{,}250{,}000/37{,}500{,}000 = 8.67\%$. Pref current pay \$600,000. Cash after senior, mezz and pref: $3{,}250{,}000 - 2{,}158{,}382 - 825{,}000 - 600{,}000 = -\$333{,}382$. The pref cannot be paid currently from property cash flow. It accrues.

| Tranche | Attach–detach | Loss at \$40.0m | Loss at \$35.0m | Loss at \$32.5m |
|---|---|---|---|---|
| Senior \$30.0m | 0–60% | 0 | 0 | 0 |
| Mezz \$7.5m | 60–75% | 0 | \$2.5m (33%) | \$5.0m (67%) |
| Pref \$5.0m | 75–85% | \$2.5m (50%) | \$5.0m (100%) | \$5.0m (100%) |
| Common \$7.5m | 85–100% | \$7.5m (100%) | \$7.5m (100%) | \$7.5m (100%) |

Mezz is impaired once value falls more than $1 - 0.75 = 25\%$, and wiped out beyond $1 - 0.60 = 40\%$.

**Check.** Losses sum to the value decline in each column: $10.0$, $15.0$, $17.5$ million. ✓

**Decision consequence.** A 20% value decline wipes out the common and half the pref while the mezz is untouched. The mezz lender's real risk is not the 25% decline threshold. It is **control**: when the common is wiped out, the mezz lender becomes the effective owner. It must be ready to foreclose on the equity pledge, cure senior defaults, and own an office building. The intercreditor agreement determines what it must do to get there: a typical agreement requires the mezz lender to cure monetary defaults on the senior loan, to be or hire a "qualified transferee" acceptable to the senior lender, and to replace any recourse guarantor. Preferred equity at 75–85% is economically a junior mezz loan without a lien, so it relies entirely on the partnership agreement's control rights. An investor who prices pref at 12% "because it is senior to the common" is pricing the wrong risk.

#### Example 10.5 — The waterfall and the promote as an option

**Given.** Total equity \$10,000,000 (90% LP, 10% GP co-invest, pooled). Annual flows, base case: −10.00, 0.60, 0.65, 0.70, 0.75, 14.00 (\$ million). Downside: −10.0, 0.5, 0.5, 0.5, 0.5, 10.5. Upside: as base, but 17.0 in year 5. Waterfall: 100% to investors until an 8% IRR; 80/20 until 12%; 70/30 thereafter. Catch-up comparison: \$10,000,000 contributed, a single distribution after five years, 8% compounding pref, 20% carry.

**Find.** Project IRR, investor IRR, and promote in each case; then the GP share with and without a full catch-up when the terminal distribution is \$18.0 million.

**Solution.** Using `cre.irr_hurdle_waterfall(flows, [0.08, 0.12], [1.0, 0.8, 0.7])`:

| Case | Project IRR | Investor IRR (after promote) | Promote |
|---|---|---|---|
| Downside | 5.00% | 5.00% | \$0 |
| Base | 11.93% | 11.19% | \$513,661 |
| Upside | 15.89% | 14.19% | \$1,343,451 |

Catch-up comparison: pref amount $= 10{,}000{,}000 \times (1.08^5 - 1) = \$4{,}693{,}281$. Total profit \$8,000,000.

* Full catch-up ($\gamma = 1$): GP receives 100% of distributions after the pref until it holds 20% of profit; GP = **\$1,600,000**; investors \$16,400,000 (IRR 10.40%).
* No catch-up: GP receives 20% only of profit above the pref: $0.20 \times (8{,}000{,}000 - 4{,}693{,}281) = \$661{,}344$; investors \$17,338,656.

The catch-up tier is $x = 0.2 \times 4{,}693{,}281/0.8 = \$1{,}173{,}320$, so it is complete when terminal distributions reach $10{,}000{,}000 + 4{,}693{,}281 + 1{,}173{,}320 = \$15{,}866{,}601$. At that point the GP holds exactly 20% of \$5,866,601 of profit. Above it, every dollar splits 80/20 and the GP's share stays at 20%. Investor IRR at \$18.0 million: 10.40% with the catch-up, 11.64% without.

**Check.** Base case: investor flows plus promote equal project flows in every year. ✓ (tested)

**Decision consequence.** The promote is zero in the downside and grows faster than profit in the upside: from base to upside, project profit rises \$3.0 million and the promote rises \$0.83 million, 28% of the increment. That convexity is the point of a promote and also its hazard. A GP whose promote is out of the money gains from volatility and loses nothing extra from failure beyond its co-invest. In Case B the promote is out of the money in every state, and the GP's remaining incentive is its fee stream. A catch-up shifts \$0.94 million to the GP at \$18 million of distributions in this example. LPs should value a catch-up as a transfer at good outcomes, not as a technicality.

#### Example 10.6 — The refinancing gap on a "good" asset

**Given.** Five years ago, an industrial property with NOI \$2,000,000 was bought at a 4.75% cap (\$42,105,263) with a \$26,000,000 loan at 3.25%, 30-year amortization, 5-year term. Today NOI is \$2,200,000 (up 10%). The market cap rate is 6.25%. New loan terms: 6.50%, 30-year amortization, max 65% LTV, min 1.25x DSCR, min 9.0% debt yield; costs 1.5% of the new loan.

**Find.** The balloon, today's value, the new loan, the refinancing gap, and the change in equity value and cash flow.

**Solution.**

Old DS $= \$1{,}357{,}844$. Balloon $B_{60} = \$23{,}219{,}757$.

Value $= 2{,}200{,}000/0.0625 = \$35{,}200{,}000$ (−16.4% despite +10% NOI).

| Constraint | Loan |
|---|---|
| LTV 65% | \$22,880,000 |
| DSCR 1.25x at $K = 7.5848\%$ | \$23,204,254 |
| Debt yield 9.0% | \$24,444,444 |

LTV binds at \$22,880,000. Costs \$343,200. Gap $= 23{,}219{,}757 + 343{,}200 - 22{,}880{,}000 = \$682{,}957$.

Equity value: \$16,105,263 at purchase; $35{,}200{,}000 - 23{,}219{,}757 = \$11{,}980{,}243$ today. New DS $= \$1{,}735{,}406$. Cash flow after debt service falls from \$842,156 to \$464,594.

**Check.** If the old balance were refinanced at 6.50%/30 years, DSCR would be $2{,}200{,}000/(23{,}219{,}757 \times 0.075848) = 1.249x$, just below 1.25x; the gap is LTV-driven, not coverage-driven. ✓

**Decision consequence.** NOI rose and the owner still has to write a \$0.68 million check to keep the asset, after which cash yield on remaining equity falls by almost half. This is the mild form of the refinancing cliff: a positive-equity sponsor funds the gap because the alternative is losing \$12 million of equity. The question is whether to fund it with the sponsor's cash, with partner capital calls (Example 10.9), or with expensive mezzanine debt. The severe form, where equity is negative and the gap exceeds the equity, is Case B.

#### Example 10.7 — Cash traps and cures (Ridgeview, year 3)

**Given.** Ridgeview's \$30,000,000 bridge loan, with SOFR above the 3.00% strike, so the capped rate is 6.25%. NOI \$2,100,000. Cash management triggers: DSCR below 1.20x (at the actual capped rate) or debt yield below 7.50%. When triggered, all excess cash after debt service is trapped in a lender-controlled account. A cure requires both tests to be met for two consecutive quarters, or a principal paydown that restores them.

**Find.** DSCR, DY, the trapped cash per year, the paydown needed to cure, and how long the trap would take to cure if the trapped cash were applied to principal.

**Solution.** DS $= 30{,}000{,}000 \times 0.0625 = \$1{,}875{,}000$; DSCR $= 1.12x$; DY $= 7.00\%$. Both tests fail. Trapped cash $= 2{,}100{,}000 - 1{,}875{,}000 = \$225{,}000$ a year.

Paydown to cure DSCR: $L$ must satisfy $2{,}100{,}000/(0.0625 L) \ge 1.20$, so $L \le \$28{,}000{,}000$: paydown \$2,000,000. Paydown to cure DY: $L \le 2{,}100{,}000/0.075 = \$28{,}000{,}000$: the same \$2,000,000, because $1.20 \times 6.25\% = 7.50\%$ (§10.4.2).

If trapped cash were swept to principal, the cure would take $2{,}000{,}000/(225{,}000/12) = 106.7$ months, far longer than the loan's remaining term.

**Check.** At $L = 28{,}000{,}000$: $2{,}100{,}000/1{,}750{,}000 = 1.20x$ and $2{,}100{,}000/28{,}000{,}000 = 7.50\%$. ✓

**Decision consequence.** The cash trap does not resolve the problem. It changes who controls the cash while the problem persists. For the sponsor, the trap ends distributions, which ends the LPs' current return and often the sponsor's ability to pay its own overhead. That creates pressure to inject capital to "cure", which is rational only if the equity option is worth more than the cure (Example 10.8). For the lender, trapped cash is a reserve against the next cap purchase or a partial paydown. A rescue investor should notice that \$2.0 million of the sponsor's \$5.0 million request goes to cure a test, not to create value.

#### Example 10.8 — The borrower's default option and the bargaining zone (Ridgeview at maturity)

**Given.** Ridgeview's \$30,000,000 non-recourse loan is at maturity. Value today \$27,000,000. In one year value will be \$33.0m, \$27.0m, or \$21.0m with probabilities 0.30, 0.40, 0.30. Property cash flow pays interest in both paths and is ignored. The lender offers a one-year extension for a fee $f$. Sponsor required return on new money 15%. Lender opportunity rate 8%. Foreclosure, holding and sale costs 8% of value; a foreclosure sale, or the sale of a property returned at maturity, closes in one year. The sponsor's principal has signed a springing-recourse guarantee triggered by a voluntary bankruptcy filing.

**Find.** The value of the sponsor's option; the maximum fee the sponsor will pay; the lender's PV under foreclosure and extension; the bargaining zone; the deficiency exposure if the sponsor files for bankruptcy to delay foreclosure.

**Solution.**

Sponsor: $E[\max(V_1 - 30, 0)] = 0.30 \times 3.0 = \$0.90$ million. PV at 15% = **\$782,609**. Intrinsic value today is zero ($27 < 30$), so all \$782,609 is time value. Note that $E[V_1] = \$27.0$ million, equal to today's value: the option value comes from dispersion, not drift. Maximum fee = \$782,609.

Lender, foreclosure: $27{,}000{,}000 \times 0.92 = \$24{,}840{,}000$ at $t=1$; PV at 8% = **\$23,000,000**.

Lender, extension: recovery at $t=1$ is \$30.0m if $V_1 \ge 30$; otherwise $V_1 \times 0.92$. $E = 0.30(30.0) + 0.40(24.84) + 0.30(19.32) = \$24{,}732{,}000$; PV = \$22,900,000, plus the fee.

Bargaining zone: the lender needs $22{,}900{,}000 + f \ge 23{,}000{,}000$, so $f \ge \$100{,}000$. The sponsor accepts $f \le \$782{,}609$. Any fee in **[\$100,000, \$782,609]** makes both better off than foreclosure today.

Bankruptcy deficiency: $30{,}000{,}000 - 24{,}840{,}000 = \$5{,}160{,}000$ owed personally by the guarantor if the springing-recourse trigger is pulled.

**Check.** At $f = 782{,}609$ the sponsor's NPV is zero; at $f = 100{,}000$ the lender's PV equals foreclosure. ✓

**Decision consequence.** Extension is efficient here: it preserves an option worth \$0.78 million to the sponsor at an expected cost to the lender of only \$0.10 million. Calling that "extend and pretend" would be wrong. It becomes extend-and-pretend when the lender's accounting, not the economics, drives the decision (Example 10.10). The springing guarantee does its job: a filing that might delay foreclosure by a year and preserve the option is worth at most \$0.78 million to the sponsor, against a \$5.16 million personal deficiency. The guarantee converts an obstruction strategy into a cooperative one (deed-in-lieu or a negotiated extension). That is why lenders insist on carve-outs from a creditworthy individual, and why a carve-out guarantor with no assets is a weaker structure than its paper suggests.

#### Example 10.9 — Capital-call dilution: who transfers value to whom

**Given.** A joint venture with 100 units: LP 90, GP 10, originally priced at \$100,000 a unit (\$10.0 million contributed). A \$3,000,000 capital call is needed to fund a refinancing gap. The pre-call fair value of the equity is \$4,000,000 (\$40,000 a unit). The LP will fund. The GP cannot. Compare: (a) both fund; (b) LP funds both shares, units issued at fair value; (c) as (b) with a 150% punitive credit on the GP's share; (d) LP funds both shares, units issued at the original \$100,000 price.

**Find.** GP ownership and the value of the GP's stake after the call (post-call equity \$7,000,000).

**Solution.**

| Case | New LP units | GP ownership | GP stake value | Transfer to (from) GP vs. fair |
|---|---|---|---|---|
| (a) Both fund | 67.5 (GP buys 7.5) | 10.00% | \$700,000 (after paying \$300,000) | 0 |
| (b) Fair value, no penalty | 75.0 | 5.714% | \$400,000 | 0 |
| (c) Fair value, 150% credit | 78.75 | 5.594% | \$391,608 | (\$8,392) |
| (d) Issued at \$100,000 | 30.0 | 7.692% | \$538,462 | +\$138,462 |

In (b), the GP's \$400,000 equals 10% of the \$4.0 million pre-call value: issuing at fair value is value-neutral. In (d), issuing units at the historical price, which is above today's value, **rewards** the non-funding partner. Even with a 150% credit at the historical price, the LP receives 31.5 units, the GP keeps 7.605%, and the GP's stake is worth \$532,319.

**Check.** (b): $10/(90 + 75 + 10) = 5.714\%$; $5.714\% \times 7{,}000{,}000 = 400{,}000$. ✓

**Decision consequence.** Many joint-venture agreements price capital-call units at capital-account or "book" value, which made sense when calls were expected to fund growth at values above cost. In a downturn the same clause penalizes the partner who funds and rewards the one who does not. A 150% punitive credit at book value still leaves the GP better off than fair-value issuance (\$532,319 against \$400,000). Before funding a call, compute the post-call value of your stake under the document's actual pricing rule, not the percentage it shows.

#### Example 10.10 — Buying the distressed note, and why the bank might not sell (Ridgeview)

**Given.** The bank will sell Ridgeview's \$30,000,000 defaulted note for \$24,000,000 (80% of par). You model three resolutions, with no interest received during the workout:

| Resolution | Probability | Gross recovery | Costs | Years |
|---|---|---|---|---|
| Modification, then payoff at par | 0.25 | \$30,000,000 | \$300,000 | 2 |
| DPO | 0.35 | \$26,500,000 | \$250,000 | 1 |
| Foreclosure and REO sale | 0.40 | \$27,000,000 | \$1,800,000 | 2 |

Your required return is 12%. The bank's cost of funds and hurdle on this asset is 6%, and it carries the note at par.

**Find.** Expected PV at 12%; NPV at the ask; scenario returns; the bank's PV at 6%.

**Solution.** Using `cre.distressed_loan_recovery`:

| Resolution | Net | PV at 12% | Annualized return on \$24.0m |
|---|---|---|---|
| Mod + payoff | \$29,700,000 | \$23,676,658 | 11.24% |
| DPO | \$26,250,000 | \$23,437,500 | 9.38% |
| Foreclosure | \$25,200,000 | \$20,089,286 | 2.47% |

Expected PV $= 0.25(23.68) + 0.35(23.44) + 0.40(20.09) = \$22{,}158{,}004$. NPV at \$24.0 million = **−\$1,841,996**. Maximum bid at 12%: \$22.16 million, 73.9% of par.

Bank's PV of the same resolutions at 6%: **\$24,246,841**, about \$0.25 million above the bid. Selling at \$24.0 million also realizes a \$6.0 million loss against the \$30.0 million carrying value.

**Check.** No scenario earns 12% at the ask, so expected PV at 12% must be below \$24.0 million. ✓

**Decision consequence.** Do not buy at 80. The bank's economic value of the note at its own cost of capital is already \$5.75 million below par; selling makes that loss visible now, while an extension keeps the loan at par on the bank's books for as long as accounting and examiners allow. That is the precise meaning of "extend and pretend": the lender's private value of delay includes avoided loss recognition and capital charges, which a note buyer does not share. The gap between a 6% holder and a 12% buyer, about \$2.1 million here, is the price of moving the risk to a specialist. Expect bid–ask gaps in distressed loan markets to close only when regulators, auditors, or the lender's own liquidity force recognition (Chapter 12).

---

### 10.6 CRE application: reading a loan as a sequence of dates

A loan document is a set of dated tests. Underwriting it means asking what NOI, rates, and values must hold on each date for the borrower to keep control.

| Date | Test | What fails it | Who gains control |
|---|---|---|---|
| Closing | LTV/LTC, DSCR at sizing rate, DY | Appraisal, rate, NOI | — |
| Each quarter | DSCR/DY cash-management triggers | NOI decline, rate rise (floating), cap expiry | Lender controls cash |
| Cap expiry | Replacement cap at required strike | Forward rates above strike | Lender (default if not bought) |
| Extension date | Extension DSCR/DY/LTV tests, fee, new cap | Same, plus value | Lender (maturity default) |
| Maturity | Refinance or repay balloon | Gap $G > 0$ | Lender (foreclosure, DPO, or extension) |

**Covenants.** Financial covenants (minimum DSCR, minimum DY, maximum LTV, minimum guarantor net worth and liquidity) usually do not cause immediate acceleration in CRE loans. They trigger cash management, reserve deposits, or rebalancing (paydown) obligations. Non-financial covenants (transfer restrictions, single-purpose-entity requirements, reporting) protect the lender's ability to enforce. Violating the transfer and SPE covenants is typically what springs full recourse.

**Recourse versus non-recourse.** Non-recourse debt prices the default option into the spread. Recourse debt from a creditworthy guarantor removes most of that option and is cheaper. The sponsor should value the difference explicitly: Example 10.8's put is worth \$0.78 million to the sponsor on a \$30 million loan over one year. Over a five-year term, in a volatile asset class, the put is worth much more. Banks often lend with partial recourse (a percentage of the loan, burning off as DSCR or DY targets are met). The burn-off tests are covenants in disguise.

**Lender types.** [INFERENCE from standard market structure; Chapters 12 and 17 document the details] Banks hold loans on balance sheet and can extend; CMBS loans are administered by servicers under pooling and servicing agreements that restrict modification until default and transfer to a special servicer; debt funds and CRE CLOs funded floating-rate bridge loans, and their own financing (repurchase lines, CLO coverage tests) can force them to act faster than banks. The same property in the same distress can receive a quick extension from a bank, a slow, rule-bound special-servicer process in CMBS, or a fast enforcement from a debt fund whose own lender is calling margin.

**Mezzanine and preferred equity in a recapitalization.** New junior capital raises proceeds but makes the stack more fragile. In Example 10.4 the combined DSCR is 1.09x, so a 9% NOI decline makes the mezz interest uncoverable. A rescue investor should insist on: (1) seniority to all existing equity, including its accrued preference; (2) control rights on default (removal of the GP, a forced sale); (3) a cash-flow sweep after its current pay; and (4) a recognition agreement from the senior lender, which mezz has through the intercreditor and pref usually does not.

**Distressed purchases.** A buyer can buy the property (after foreclosure), the note (before resolution), or a junior position (mezz or pref) that controls the equity. Buying the note buys the lender's remedies and the lender's timeline. Buying the mezz near its attachment point buys control at a low price but obliges the buyer to cure the senior loan.

---

### 10.7 When the relationships fail

1. **DSCR on trailing NOI misses the cap expiry.** A floating-rate loan sized at the strike can pass every covenant until the day the cap expires. The relevant DSCR is at the forward index on the next cap date, plus the cap's cost.
2. **LTV relies on a value that does not exist.** In illiquid markets appraisals lag (Chapter 2). A 65% LTV on a stale appraisal can be 85% on a clearing price. Debt yield is the more robust test because it uses income alone.
3. **Non-recourse is not non-recourse for everyone.** Carve-out guarantees, environmental indemnities, and completion guarantees create personal exposure that sponsors sometimes treat as remote. Whether and how a given carve-out is enforced is a legal question that depends on the documents and the jurisdiction; this book does not rely on specific court holdings. The analytical point is that the guarantee's value depends on the guarantor's assets and on which acts trigger it.
4. **Waterfall hurdles measured on IRR can be gamed by timing.** Early distributions (from a refinancing) raise IRR without raising multiple. A promote that crystallizes on an IRR test after an early cash-out refinance may pay the GP before the LP's capital is safe. Look-back and clawback provisions, and multiple-based hurdles, address this.
5. **"Senior to the common" is not "safe".** Preferred equity and mezz sit at 75–85% and 60–75% in Example 10.4. Their loss probability is governed by the probability of value declines of 15–40%. Whether such declines are rare is an empirical question by property type and period, which Chapter 23 examines; do not assume it.
6. **The lender may not behave as the option model predicts.** Regulatory capital, accounting, servicer standards, workout staff capacity, and reputational concerns enter the lender's objective. The bargaining zone in Example 10.8 can be wider or narrower than the economics alone imply.
7. **Correlated maturities break the refinancing market itself.** The refinancing gap assumes a lender exists at the stated terms. When many loans mature at once into a market where lenders are also impaired, the new-loan terms are not exogenous.

---

### 10.8 Lender and sponsor incentives

**Moral hazard in non-recourse debt.** Once equity is out of the money, the sponsor's payoff is a call. Calls gain from volatility. A sponsor with negative equity prefers riskier strategies (speculative re-leasing, deferred maintenance, aggressive lease-up concessions) because the lender bears the downside. Covenants, cash management, and recourse carve-outs are the lender's tools to limit this.

**The GP's fee incentive.** A GP whose promote is worthless still earns asset-management and property-management fees while the partnership owns the asset. In Case B the GP's 10% co-invest share of a fresh-equity refinance is negative, but adding three years of fees makes the GP's private payoff positive while the LP's is −\$2.8 million. LPs must compute the GP's private payoff from each strategy before accepting a GP recommendation.

**The lender's accounting incentive.** A lender carrying a loan at par must recognize a loss on sale or foreclosure. An extension, if it passes accounting and supervisory tests, defers recognition. In Example 10.10 the bank's economic value is \$24.2 million against a \$30.0 million book value. Extending keeps \$5.75 million of economic loss off the income statement for now. The lender is not wrong to extend when the extension is economically efficient (Example 10.8). It is wrong when the extension is chosen because it defers recognition, and the collateral is deteriorating while it waits.

**The special servicer's incentive.** CMBS special servicers earn workout and liquidation fees and may be affiliated with the controlling (most junior) bondholder. The controlling class prefers strategies that delay realized losses, which would wipe it out [INFERENCE from CMBS structure; Chapter 17 develops tranche incentives].

**Alignment tools.** For LPs: GP co-invest that is material relative to GP net worth; fee offsets; promote clawbacks; removal rights. For lenders: recourse carve-outs, cash management, and sizing on debt yield. For rescue investors: seniority, control, and a price that is right without assuming the sponsor's business plan.

---

### 10.9 Historical episode: floating-rate bridge loans and the rate-cap squeeze, 2022–2024

**Date and environment.** On 16 March 2022 the Federal Open Market Committee raised the target range for the federal funds rate to 1/4 to 1/2 percent, the first increase of the cycle [FACT: FOMC statement, 16 March 2022; ch10-S01, VERIFIED-PRIMARY]. On 26 July 2023 it raised the range to 5-1/4 to 5-1/2 percent [FACT: FOMC statement, 26 July 2023; ch10-S02, VERIFIED-PRIMARY], a cumulative increase of 525 bp in about sixteen months. SOFR, the index for most new floating-rate CRE loans, is a secured overnight rate that trades close to the policy range [INFERENCE from the policy implementation framework; the daily SOFR series on FRED was not retrieved for this edition, so no specific SOFR prints are quoted].

**What the loans looked like.** [INFERENCE from standard market structure, consistent with the GSE disclosures below] Value-add multifamily acquisitions in 2020–2022 were often financed with short-term (two- to three-year initial term) floating-rate bridge loans at high LTV, interest-only, with interest-rate caps required by the lender. Many such loans were funded by debt funds and securitized in CRE CLOs. A Federal Reserve Bank of Philadelphia working paper describes CRE CLOs as securitizations backed by pools of floating-rate, interest-only loans and reports that multifamily made up about three-quarters of their collateral [FACT: Philadelphia Fed Working Paper 25-43; ch10-S08, VERIFIED-SECONDARY].

**The cap mechanism.** Fannie Mae's 2023 annual report states that it generally requires multifamily borrowers with adjustable-rate loans to maintain interest-rate caps for the life of the loan, with escrows for replacement caps, and that rising cap replacement costs contributed to the increase in its multifamily serious delinquency rate in 2023 [FACT: Fannie Mae Form 10-K for 2023; ch10-S04, VERIFIED-SECONDARY: read via search excerpt of the SEC filing]. Freddie Mac's January 2024 *Multifamily Maturity Risk* research note describes a cap as functioning like insurance against the rate rising above the underwritten rate, and notes that floating-rate loans may come under more stress because of higher rates and cap premiums [FACT: ch10-S05, VERIFIED-SECONDARY; paraphrased from a search excerpt, not quoted]. Trade press reported that replacement-cap prices rose by more than an order of magnitude between 2019 and 2023 *(verification pending; ch10-S10, class C; no figure is used)*. Example 10.3 shows why: a cap bought far out of the money costs almost nothing, and the same strike bought after forwards rise above it is mostly prepaid intrinsic value.

**The maturity wall.** The Mortgage Bankers Association reported in February 2024 that \$929 billion, 20% of the \$4.7 trillion of outstanding commercial and multifamily mortgages held by lenders and investors, would mature in 2024, a 28% increase from the \$729 billion that matured in 2023, and attributed much of the increase to loans extended or modified in 2023. It also reported that 38% of hotel/motel loan balances and 25% of office balances would mature in 2024, against only 3% (\$28 billion) of multifamily and health-care mortgages held or guaranteed by Fannie Mae, Freddie Mac, FHA, and Ginnie Mae [FACT: MBA, "20 Percent of Commercial and Multifamily Mortgage Balances Mature in 2024", 12 February 2024; ch10-S03, VERIFIED-PRIMARY]. Different data providers estimate different totals; the MBA figure is a survey of lenders' own holdings.

**What the official sector said.** The Federal Reserve's April 2024 *Financial Stability Report* noted that delinquency rates on CRE loans, especially those backed by office properties, increased in the second half of 2023 [FACT: ch10-S06, VERIFIED-SECONDARY]. Its November 2024 *Supervision and Regulation Report* noted that multifamily delinquencies at large banks had risen steadily from a low base and that valuations had declined for certain multifamily properties [FACT: ch10-S07, VERIFIED-SECONDARY]. The Philadelphia Fed working paper reports CRE CLO delinquency rates in 2024 of 12.64% for static and 8.41% for managed deals, up from 0.63% and 1.20% in 2019 [FACT: ch10-S08, VERIFIED-SECONDARY; delinquency definitions follow the paper's data source]. The Federal Reserve's May 2023 report explicitly excluded multifamily mortgages from its CRE price-vulnerability analysis because the sector's fundamentals differ [FACT: ch10-S09, VERIFIED-SECONDARY].

**What was knowable at origination (2020–2022).** That the loans floated, that caps would expire before loan maturity, and that extension tests required new caps were all in the loan documents. The forward curve in 2021 implied low future rates [INFERENCE: consistent with the near-zero policy range before March 2022]. What was not knowable was the speed of the 2022–23 tightening: 525 bp in about sixteen months (ch10-S01, S02). A sponsor who stress-tested "SOFR at the cap strike for the full term" would have found the debt service bearable. A sponsor who also tested "the cost of a replacement cap when forwards are above the strike" would have found a cash requirement of several percent of the loan at each extension (Example 10.3).

**Interpretations.**

* *Rate shock.* Floating-rate debt transferred the policy shock directly to borrowers. Caps delayed it but did not remove it, because caps were shorter than the loans.
* *Underwriting.* High-LTV bridge loans sized on projected (post-renovation) NOI were vulnerable to any delay in the business plan, and expense growth (insurance, payroll) delayed many plans. On this view, rates exposed weak underwriting rather than causing losses on their own.
* *Structure.* CRE CLO and debt-fund lenders, financed with their own short-term or market-value-sensitive liabilities, had less ability to extend than banks [HYPOTHESIS for this edition; to be tested against servicer and rating-agency data].

**What the episode establishes.** That a hedge with a shorter maturity than the exposure is a roll-over bet on the price of the hedge. That DSCR sized at the cap strike is a statement about debt service, not about liquidity. That maturity walls are partly manufactured by extensions, which move maturities rather than resolve them (the MBA's own attribution of the 2024 increase).

**What it does not establish.** It does not establish loss severities on multifamily bridge loans as a class: delinquency is not loss, and resolution data are incomplete. It does not show that floating-rate debt is imprudent in general: a borrower with a matched-maturity cap, lower leverage, or a shorter business plan would have fared differently. It does not establish that 2007–09-style CMBS losses recurred; that comparison requires loss data not used here (Chapter 23 treats 2007–09).

**CRE connection.** Case B studies the fixed-rate version of the same cliff: a loan whose coupon was safe until the day it had to be refinanced.

---

### 10.10 Decision exercise: Ridgeview

Return to §10.1. Use Examples 10.3, 10.7, 10.8, and 10.10. Write a one-page decision record (`desk/investment_memos/decision_record_template.md`) that answers:

1. **What does the \$5.0 million buy?** Allocate it: replacement cap (about \$0.89 million at a 3.00% strike, less at a higher strike), the \$2.0 million cure paydown, renovation capital. Which uses create value and which only preserve the sponsor's option?
2. **Where does the pref attach?** With the loan at \$28.0 million after the paydown and value about \$27 million, the pref attaches above 100% of current value. What value must Ridgeview reach for the pref to be repaid in full, and in which of Example 10.8's states does that happen?
3. **Is the note at 80 better?** Compare your answer from Example 10.10 with the pref.
4. **What would you need to see** to invest in either: a signed extension from the lender with stated tests; a replacement cap bid; renovation results on the completed units (rent premiums achieved versus plan); insurance renewal; the GP's ability to fund its share.
5. **What is your decision?** Abstention is a legitimate answer, and is likely the best answer at the proposed terms.

**Rubric (see `problems/solutions/ch10_solutions.md` §Decision exercise).** Full credit requires: identifying that the pref attaches above current value and is therefore equity risk priced as credit; noting that \$2.0 million cures a test rather than creating value; valuing the note below 80 at a 12% target (Example 10.10); stating the conditions under which either investment would be acceptable (for example, pref only with the senior lender's extension signed, a lower attachment through a larger paydown by the existing equity, and control rights); and an explicit abstain/invest decision with invalidation criteria.

---

### 10.11 Frequent analytical errors

1. **Sizing on the coupon instead of the loan constant.** DSCR uses debt service, which includes amortization. A 6.50% loan on 30-year amortization has a 7.58% constant.
2. **Treating IO as free proceeds.** IO raises proceeds by moving principal repayment to the balloon (Example 10.2).
3. **Underwriting DSCR at today's index for floating debt.** Underwrite at the strike, at the forward index after cap expiry, and include the replacement cap's cost.
4. **Annual versus monthly.** The mortgage rate is nominal annual; the monthly rate is $r/12$; the effective annual rate is higher. Never divide an annual debt service by 12 and call it a payment when the loan pays monthly in arrears; the annual figure is 12 × the monthly payment.
5. **Ignoring the balloon in the exit analysis.** A sale or refinance at year $T$ repays $B_T$, not $L$.
6. **Reading attachment points as safety.** A 75–85% pref loses half its value on a 20% decline (Example 10.4).
7. **Confusing waterfall IRR hurdles with multiples.** An early refinancing distribution can meet an IRR hurdle without returning capital at risk.
8. **Assuming dilution is always punitive.** It depends on the issue price relative to fair value (Example 10.9).
9. **Taking the lender's ask as its reservation price.** A bank's private value of delay includes accounting effects that a buyer does not share (Example 10.10).
10. **Ignoring guarantees in the option analysis.** Carve-outs make some exercise strategies very expensive (Example 10.8).

---

### 10.12 Connections to other chapters

* Chapter 1 §1.6 introduced leverage as the conversion of investment into speculation. This chapter adds amortization, sizing, and maturity.
* Chapter 2 explains why appraisals lag, which weakens LTV as a covenant.
* Chapter 3 develops reflexive collateral loops: falling values tighten LTV, which forces sales, which lowers values.
* Chapter 6 links cap rates to Treasury yields and the cost of capital that drives $c_T$ in the refinancing gap.
* Chapter 9 supplies the valuation inputs ($V$, loaded cap rates) used in sizing.
* Chapter 11 applies debt sizing to hotels, where NOI volatility makes debt yield the dominant test.
* Chapter 12 treats maturity walls, loan sales, foreclosure timelines, and CMBS at market scale.
* Chapter 13 analyzes hold, sell, or refinance as real options.
* Chapter 17 prices credit tranches and CMBS subordination.
* Chapter 18 prices caps, floors, and swaptions.
* Case A uses the sizing functions on a hotel acquisition. Case B applies the whole chapter to a maturing office loan.

---

### 10.13 One-page reference sheet

| Quantity | Formula |
|---|---|
| Monthly payment | $PMT = L\,i/(1-(1+i)^{-n})$, $i = r/12$ |
| Loan constant | $K = 12\,PMT/L$; IO: $K = r$ |
| Balance (prospective) | $B_k = PMT \cdot a_{\overline{n-k}\vert i}$ |
| Balance (retrospective) | $B_k = L(1+i)^k - PMT[(1+i)^k-1]/i$ |
| IO then amortizing | Balance at $T$ = $B_{T-m}$ on the original schedule |
| Max loan | $\min(\lambda V,\ NOI/(DSCR\cdot K),\ NOI/DY)$ |
| DSCR binds iff | $K > c/(\lambda\,DSCR)$ |
| IO identity | DSCR test at rate $r$ ⇔ DY test at $DSCR \cdot r$ |
| Floating interest with cap | $L(\min(I,K_{cap}) + s)$; cap pays $L\max(I-K_{cap},0)$ |
| Bachelier caplet | $N\tau P[(F-K)\Phi(d) + \sigma_N\sqrt{T}\phi(d)]$, $d = (F-K)/(\sigma_N\sqrt T)$ |
| Tranche loss | $\ell_j = \min(A_j, \max(\Delta - \sum_{k>j}A_k, 0))$ |
| Catch-up tier size | $x = \pi p/(\gamma - \pi)$ |
| Refinancing gap | $G = B_T + C - L^*_{new}$ |
| Borrower option (1 period) | $E[\max(V_1-B,0)]/(1+k_E) - f$ |
| Lender extension PV | $E[\min(B, V_1(1-\kappa))]/(1+k_L) + f$ |
| Dilution | $s_B' = U_B/(U + \text{new units})$; transfers only if issue price ≠ fair value or $\theta > 1$ |

**HP-12C:** `f CLEAR FIN`, `L PV`, `r g 12÷`, `years g 12×`, `PMT`; balloon after $k$ months: `k n FV`.

**Questions for any loan:** On what date does each test bite? What is the balloon? What does the cap cost to replace? Who controls cash after a trigger? What springs recourse? What is the sponsor's option worth, and to whom does the sponsor's private payoff differ?

---

### References for this chapter

Source IDs refer to `references/sources_ch10.md`.

* Board of Governors of the Federal Reserve System. FOMC statement, 16 March 2022. https://www.federalreserve.gov/newsevents/pressreleases/monetary20220316a.htm (ch10-S01).
* Board of Governors of the Federal Reserve System. FOMC statement, 26 July 2023. https://www.federalreserve.gov/newsevents/pressreleases/monetary20230726a.htm (ch10-S02).
* Mortgage Bankers Association (2024). "20 Percent of Commercial and Multifamily Mortgage Balances Mature in 2024", 12 February 2024. https://www.mba.org/news-and-research/newsroom/news/2024/02/12/20-percent-of-commercial-and-multifamily-mortgage-balances-mature-in-2024 (ch10-S03).
* Fannie Mae, Form 10-K for fiscal year 2023. https://www.sec.gov/Archives/edgar/data/310522/000031052224000184/fnm-20231231.htm (ch10-S04).
* Freddie Mac Multifamily (2024). *Multifamily Maturity Risk*, January 2024. https://mf.freddiemac.com/docs/multifamily_maturity_risk_report.pdf (ch10-S05).
* Board of Governors of the Federal Reserve System (2024). *Financial Stability Report*, April 2024 (ch10-S06).
* Board of Governors of the Federal Reserve System (2024). *Supervision and Regulation Report*, November 2024, "Banking System Conditions" (ch10-S07).
* Federal Reserve Bank of Philadelphia (2025). "Does Skin in the Game Align Incentives? The Case of CRE CLOs." Working Paper 25-43 (ch10-S08).
* Board of Governors of the Federal Reserve System (2023). *Financial Stability Report*, May 2023, "Asset Valuations" (ch10-S09).
* Bachelier, L. (1900). *Théorie de la spéculation*. Annales scientifiques de l'École Normale Supérieure, 17, 21–86 (ch10-S11).


\newpage

## Chapter 11 — Hotels: The High-Beta CRE Asset

> **Status:** Complete (v1.0). Every number in this chapter, in the eight hotel cases of §11.6, in the problems, and in the solutions is reproduced in `tests/test_ch11_examples.py`. Problems: `problems/questions/ch11_problems.md`. Solutions: `problems/solutions/ch11_solutions.md`. Sources: `references/sources_ch11.md`. Drills D056–D070. The companion negotiation case is Case D (`cases/hypothetical/case_D_hotel_pip_negotiation/`). Historical figures marked *(verification pending)* have not yet been checked against a primary source.

### Learning objectives

After this chapter you should be able to:

1. Decompose a RevPAR change into occupancy and rate, place it against a competitive set with MPI, ARI and RGI, and say whether the hotel gained or lost share while "RevPAR was up".
2. Build a USALI-style P&L from rooms revenue to NOI. Keep departmental profit, GOP, EBITDA and NOI distinct, and say which line every fee, reserve and fixed charge sits on.
3. Derive flow-through for rate-led and occupancy-led revenue growth from the cost structure, and diagnose a hotel whose RevPAR rose while NOI fell.
4. Price the fee stack: franchise royalty, marketing, reservation and loyalty charges; base and incentive management fees; the owner's priority return. Explain who holds which option on hotel cash flow.
5. Compute break-even occupancy with and without debt service (`sdesk.hotel.breakeven_occupancy`), and show how labor-cost shocks move it.
6. Run a displacement analysis for a group request and state the minimum acceptable group rate.
7. Explain how hotel lenders size loans differently from apartment and office lenders (trailing NCF, debt yield, cash management, FF&E and PIP reserves), and compute the binding constraint.
8. Value a hotel under stress: direct capitalization on the correct line, DCF with a recovery path, scenario weighting. Allocate total value among real property, FF&E and business intangibles, and quantify why the allocation matters for property tax, income tax and appraisal.
9. Price a property improvement plan into a bid (`sdesk.hotel.pip_adjusted_price`), compute the RevPAR lift that justifies renovation capital, and decide between selling before or after a PIP.
10. Compare renewal, conversion and independence as brand strategies, and decide when the analytically correct answer is to give no point value at all.

---

### 11.1 Opening investment problem: the Monday BOV

A family owner calls on Monday. They own a 132-room upscale select-service hotel with a national flag in a growing suburban submarket. They want a broker opinion of value (BOV) by Friday because "it's a record year and the market is hot". The facts they send are [HYPOTHESIS], as is every hotel in this chapter:

* **T-12 performance.** Occupancy 71.0%, ADR \$158.50, RevPAR \$112.54. Last year: 74.0% and \$142.00, RevPAR \$105.08. "RevPAR up 7.1%."
* **Owner's valuation.** "EBITDA is \$1.46 million. Hotels trade at 9 caps, so it's worth \$16.2 million."
* **The brand** has told the owner, informally, that "a refresh will be needed on any sale". No property improvement plan (PIP) letter has been issued. Your recent experience with this brand's change-of-ownership PIPs on similar vintages is about \$14,000 per key.
* **The STR report** (a competitive-set benchmarking report of the kind STR, now part of CoStar, sells to hotel owners) is attached but the owner has not read it.

You have four questions to answer before Friday. What is the hotel earning, on the line a buyer capitalizes? Is its revenue growth its own, or the market's? What will a buyer deduct for the renovation, and is the owner better off selling now or after renovating? And what would make you refuse to put a number on the page? Section 11.11 returns to the decision after the chapter has built the tools. Cases 11.1–11.8 (§11.6) extend each tool to a full decision.

---

### 11.2 Economic intuition: why hotels have the highest beta in CRE

An apartment lease reprices once a year. An office lease reprices once a decade. A hotel room reprices every night. That single fact explains most of what follows.

**The lease term is one night.** There is no rent roll to protect income when demand falls, and no contractual rent bump to lift it when demand rises. Revenue moves with the business cycle, air travel, corporate travel budgets, group meeting calendars, and local events, with a lag of days rather than years. When demand falls, managers face a choice between holding rate and losing occupancy or cutting rate to defend occupancy. Either way revenue falls immediately.

**A hotel is an operating business wrapped around real estate.** The owner employs (directly or through a manager) a housekeeping, front-desk, engineering, sales and food-and-beverage staff. Labor is typically the largest cost line [HYPOTHESIS for any specific hotel; industry cost surveys should be cited when a figure is needed]. Much of that labor is fixed in the short run: a hotel cannot run a front desk with 70% of a clerk. Fixed costs create **operating leverage**. A 5% revenue change can move NOI by 14–20%, as Example 11.2 shows.

**Revenue-based fees are senior to the owner.** Franchise fees are charged on rooms revenue and base management fees on total revenue. They are paid before the owner sees a dollar of NOI, and they do not fall when margins compress. The owner holds the residual. The brand and the manager hold claims that behave like senior revenue participations. The incentive fee gives the manager a call option on the upside (Case 11.4).

**Capital wears out fast and on a schedule set by someone else.** Carpets, case goods, mattresses and bathrooms wear out on cycles of years, not decades. The brand enforces standards through PIPs at relicensing and on change of ownership. A hotel owner therefore carries two capital claims: the **FF&E reserve** (a recurring percentage of revenue that funds normal replacement) and the **PIP** (a lumpy, brand-mandated renovation that the reserve rarely covers in full). A buyer who capitalizes NOI without pricing the next PIP is buying the hotel twice.

**Value includes a business.** The price of a hotel pays for land and building, for the furniture, fixtures and equipment, and for an operating business with a flag, a workforce, a reservation system and a booking pace. How that total is allocated affects property taxes, depreciation, lender collateral and appraisal (Case 11.7).

**Supply arrives in lumps, and capital is pro-cyclical.** New hotels take years to entitle and build. Supply that was financed at the top of a cycle opens into the downturn. Hotel lenders retreat faster than lenders on leased property, because the collateral's income can disappear within a quarter. The historical episode in §11.10 shows how fast.

#### Demand segments, seasonality and revenue management

A hotel sells the same room to different buyers at different prices on different terms. The segments behave differently and must be underwritten separately.

* **Transient** guests book individually, through brand channels, online travel agencies (OTAs), the global distribution system or directly. They pay the highest rates and the highest acquisition costs, and they disappear first in a downturn.
* **Group** business (associations, corporate meetings, sports teams, weddings) books blocks of rooms months in advance, at a negotiated rate, and usually brings banquet and meeting-room revenue. Groups give the hotel a base of occupancy that can be forecast, at the cost of capacity that cannot be resold at short notice. Contracts carry cutoff dates and attrition clauses that shift some of the forecast risk back to the group.
* **Contract** business (airline crews, rail crews, long-term project housing) pays the lowest rate for guaranteed volume, often every night of the year.

The mix matters because contribution, not ADR, is the objective. A group room at \$148 with banquet profit can be worth more than a transient room at \$172 that carries a 15% commission (Example 11.5). An ADR-maximizing strategy that drops low-rate contract business can lower RevPAR and profit if the freed rooms do not refill.

**Seasonality** adds a time dimension. Resorts, ski hotels and hotels near universities or state capitals earn most of their annual cash in a few months. Fixed costs and debt service arrive every month, and annual bills (insurance, property tax) arrive when they are due, not when revenue does. Annual ratios conceal this. A hotel with a comfortable annual DSCR can run out of cash every winter (Case 11.5).

**Revenue management** is the practice of setting price and availability by night and segment to maximize contribution given a demand forecast. Its two core decisions are rate (what to charge transient guests given the booking pace) and displacement (whether to give capacity to a group or contract at a lower rate). Both are bets on a forecast. The analyst's question is not whether the revenue manager "is good", but whether the hotel's rate and mix decisions are consistent with its demand: whether the penetration indices show rate gained at the expense of share, and whether accepted groups would have survived a displacement test.

#### Labor

Labor ties hotel cost to wage markets that move independently of hotel demand. Some labor is variable (housekeeping time per occupied room), some is semi-fixed (front desk, night audit, maintenance), and some is fixed (the general manager, the director of sales, the chief engineer). Wage inflation, scheduling rules, benefits and union contracts change all three. In underwriting, labor should be modeled as hours times wage in each category, not as a percentage of revenue, because a percentage-of-revenue assumption makes labor fall when the hotel's revenue falls and rise when ADR rises. Neither is true in the short run (Cases 11.1 and 11.6).

#### The speculator's view

The result is an asset whose cash flow has a high beta to the economy and whose value has a high beta to its cash flow. To a speculator this is not a defect. It is the reason hotels offer the widest mispricings in CRE. Sellers anchor on peak NOI, buyers forget PIPs, lenders size on trailing figures, and owners confuse a rising market with rising share. Each of these errors has a price, and this chapter computes it.

---

### 11.3 Technical definitions

| Term | Definition |
|---|---|
| Rooms available | Rooms (keys) × days in period. Conventions for rooms out of order differ between operators and data providers; state whether they are excluded |
| Occupancy (Occ) | Rooms sold ÷ rooms available (a decimal) |
| ADR | Rooms revenue ÷ rooms sold. Excludes occupancy taxes |
| RevPAR | Rooms revenue ÷ rooms available = Occ × ADR |
| TRevPAR | Total operating revenue ÷ rooms available |
| Departmental profit | Revenue of an operated department (rooms, F&B, other) less that department's direct expenses |
| Undistributed expenses | Administrative & general (A&G), information & telecommunications, sales & marketing (S&M), property operations & maintenance (POM), utilities. Not charged to a department |
| GOP | Total revenue − departmental expenses − undistributed expenses (USALI) |
| GOPPAR | GOP ÷ rooms available |
| Fixed charges | Property tax, insurance, ground rent. In this book EBITDA is after them (style guide §5) |
| EBITDA | GOP − management fees − franchise fees − fixed charges. Before the FF&E reserve |
| NOI | EBITDA − FF&E reserve. The line this book capitalizes unless stated |
| FF&E reserve | Periodic set-aside, normally a % of total revenue (4% in this book), for replacing furniture, fixtures and equipment |
| PIP | Property improvement plan: a brand's list of required renovations, issued at relicensing or on change of ownership |
| Franchise fees | Royalty (% of rooms revenue), marketing or program fee, reservation or technology fee, loyalty-program charges. Some are % of rooms revenue, some per room or per stay |
| Base management fee | % of total revenue paid to the operator |
| Incentive management fee (IMF) | Share of profit above a threshold, often after an **owner's priority** return on invested capital |
| Comp set | A small group of competing hotels chosen to benchmark the subject (Appendix D discusses data quality) |
| MPI, ARI, RGI | Occupancy, ADR and RevPAR indices: subject ÷ comp set × 100. 100 is "fair share" |
| Flow-through | ΔProfit ÷ ΔRevenue, stated for a named profit line (GOP or NOI) |
| Displacement | Higher-value business turned away because capacity was given to lower-value business |
| Block, cutoff, pickup, attrition, wash | A group's reserved rooms; the date unsold block returns to inventory; rooms actually used; the contractual shortfall allowance; the gap between block and pickup |
| Owner's priority | A return on invested capital that must be paid to the owner before any incentive fee |
| Performance test | A contract clause allowing the owner to terminate a manager whose results fall below thresholds (e.g., RGI and budget) |
| TAB, BEV | Total assets of the business; business enterprise value (the intangible component) |
| Key money | Cash or credit a brand pays an owner to sign a franchise or management agreement, usually forgiven over the term and repayable on early exit |
| Liquidated damages (LD) | A contractual termination payment owed to a brand when a franchise ends early |
| Cash management (cash trap) | A loan provision that redirects excess cash to a lender-controlled account when a trigger (e.g., DSCR below a threshold) is breached |

---

### 11.4 Equations and derivations

#### 11.4.1 The RevPAR identity and its decomposition

With $N$ rooms, $D$ days, $RN$ rooms sold and rooms revenue $RR$:

$$\text{Occ} = \frac{RN}{N D}, \qquad ADR = \frac{RR}{RN}, \qquad RevPAR = \frac{RR}{N D} = \text{Occ} \times ADR.$$

Growth multiplies: $(1+g_{RevPAR}) = (1+g_{Occ})(1+g_{ADR})$. Logs make the decomposition additive and exact:

$$\ln(1+g_{RevPAR}) = \ln(1+g_{Occ}) + \ln(1+g_{ADR}).$$

The penetration indices are ratios to the comp set (subscript $c$):

$$MPI = 100\frac{\text{Occ}}{\text{Occ}_c}, \quad ARI = 100\frac{ADR}{ADR_c}, \quad RGI = 100\frac{RevPAR}{RevPAR_c} = \frac{MPI \times ARI}{100}.$$

**Why it matters.** RevPAR growth that merely matches the comp set's growth is the market's tide. Only a change in RGI is the hotel's own performance. A buyer pays for the tide through the cap rate and for the share through the NOI.

#### 11.4.2 Cost structure and the NOI equation

Write total revenue as $TR = RR(1+o)$, where $o$ is other revenue as a fraction of rooms revenue. Group costs by behavior:

* $c$: variable cost per occupied room (housekeeping labor, amenities, laundry, breakfast, in-room supplies);
* $v$: costs proportional to revenue (franchise fees, management fees, card fees, commissions, the FF&E reserve, other-department costs where other revenue scales with rooms revenue);
* $F$: costs fixed in the short run (fixed labor, A&G, S&M, POM, utilities base load, property tax, insurance).

Then

$$NOI = TR(1-v) - c\,RN - F = RN\big[ADR(1+o)(1-v) - c\big] - F. \tag{11.1}$$

The bracket is the **contribution per occupied room**. Every equation below follows from (11.1).

#### 11.4.3 Flow-through: rate versus occupancy

Raise RevPAR by a fraction $x$ through rate alone. Rooms sold are unchanged, so $c\,RN$ is unchanged and

$$\Delta NOI_{rate} = \Delta TR\,(1-v) \;\Rightarrow\; FT_{rate} = 1 - v.$$

Raise RevPAR by $x$ through occupancy alone. Rooms sold rise by $x\,RN$, so

$$\Delta NOI_{occ} = \Delta TR(1-v) - c\,x\,RN \;\Rightarrow\; FT_{occ} = 1 - v - \frac{c}{ADR(1+o)}.$$

The difference, $c/[ADR(1+o)]$, is the variable cost of servicing the extra guests as a share of the revenue they bring. For a limited-service hotel with \$36 of variable cost per occupied room and a \$157.50 total revenue per occupied room, it is about 23 points of flow-through (Example 11.2). Rate-led growth is worth more than occupancy-led growth of the same size. That is why revenue managers fight for rate, and why a buyer should ask how RevPAR growth was achieved, not just how much there was.

**Degree of operating leverage.** From (11.1), $\%\Delta NOI / \%\Delta TR = TR(1-v)/NOI$ for rate-led change. A hotel with a 19% NOI margin and $v = 0.25$ has DOL of about $0.75/0.19 \approx 3.9$. A multifamily property with a 60% NOI margin and nearly all-fixed operating costs has DOL near $1/0.6 \approx 1.7$ [HYPOTHESIS: an illustrative apartment cost structure]. The hotel is more than twice as sensitive to revenue.

#### 11.4.4 The fee stack

$$\text{Franchise fees} = (r_{roy} + r_{mkt} + r_{res} + r_{loy})\,RR \;(+\text{per-room or per-stay charges}),$$
$$\text{Base management fee} = b\,TR,$$
$$IMF = i \times \max\!\big(0,\; ACF - \pi K\big), \qquad ACF = GOP - b\,TR - \text{fixed charges} - f\,TR,$$

where $ACF$ is "available cash flow" (here equal to NOI), $\pi$ is the owner's priority rate and $K$ the owner's invested capital. Contracts define ACF and the priority in many ways. Read the definitions; do not assume them. The base fee and franchise fees behave like senior revenue claims. The IMF is a call option held by the manager, struck at the owner's priority.

#### 11.4.5 EBITDA, NOI and the cap rate that goes with each

$NOI = EBITDA - fTR$ with reserve rate $f$. A cap rate is a ratio to a named line. If the market prices a hotel at $c_{NOI}$ on NOI, the equivalent rate on EBITDA is

$$c_{EBITDA} = \frac{EBITDA}{V} = c_{NOI}\,\frac{EBITDA}{NOI} > c_{NOI}.$$

Applying $c_{NOI}$ to EBITDA overstates value by exactly $fTR / c_{NOI}$: the capitalized reserve. At a 9% cap and a \$218,544 reserve, that is \$2.43 million (Example 11.3).

**Normalization** applies before any cap rate: remove non-recurring revenue and expenses, impute market management and franchise costs if the owner self-manages or the flag will change, replace owner compensation with a market GM cost, re-underwrite insurance and reassessed property tax, and deduct the reserve. Case A works through a full normalization. This chapter assumes it has been done.

#### 11.4.6 Break-even occupancy

Set (11.1) less debt service $DS$ equal to zero and solve for rooms sold:

$$RN^* = \frac{F + DS}{ADR(1+o)(1-v) - c}, \qquad \text{Occ}^* = \frac{RN^*}{N D}. \tag{11.2}$$

`sdesk.hotel.breakeven_occupancy(rooms, adr, fixed_costs, debt_service, variable_cost_per_occupied_room, variable_pct_of_revenue, other_revenue_pct_of_rooms=o)` implements (11.2). Two cautions. First, (11.2) holds ADR fixed; in a real downturn ADR falls with occupancy, so the true break-even is higher (Case 11.6 stresses both). Second, $F$ is fixed only in the short run. Over a year, managers cut fixed labor, which is why break-even analysis is a liquidity tool for the next few quarters and not a long-run value tool.

#### 11.4.7 Displacement

A group of $G$ rooms per night for $n$ nights at rate $r_g$ is worth accepting if its total contribution, including banquet and meeting-room profit, exceeds the contribution of the transient business it displaces:

$$G_{picked}\,n\,\big[r_g(1-v_g) - c + s_g m_g\big] \;>\; \sum_{\text{nights}} D_t\big[ADR_t(1-v_t) - c + s_t m_t\big] + \text{shoulder-night losses},$$

where $D_t$ is displaced transient rooms (unconstrained demand minus what still fits), $v_g$ and $v_t$ include commissions specific to each channel, $s$ is ancillary spend per occupied room and $m$ its departmental margin net of fees. The **break-even group rate** sets the two sides equal. Displacement depends on a demand *forecast*, so the decision is a bet on that forecast and must be stress-tested (Case 11.2).

#### 11.4.8 Hotel debt sizing

The constraints are those of Chapter 10:

$$L \le \lambda V, \qquad L \le \frac{NOI}{DSCR_{min}\,K}, \qquad L \le \frac{NOI}{DY_{min}},$$

with $K$ the loan constant. Hotel lenders differ in what goes into the formulas, not in the formulas:

| Item | Typical hotel practice [HYPOTHESIS: conventions vary by lender and cycle] | Why |
|---|---|---|
| Income line | Trailing-12 NCF after a 4% FF&E reserve, sometimes the lower of T-12 and budget | Income can fall within a quarter; pro forma lift is not lent against |
| Debt yield | Higher minimums than for leased property | Debt yield ignores the rate and cap rate, so it binds when values look rich |
| LTV | Lower maximums | Value is volatile and includes non-real-estate components |
| Reserves | FF&E reserve escrowed monthly; PIP reserve funded at closing or held back | The collateral wears out; the brand can terminate the flag |
| Cash management | DSCR or debt-yield trigger sweeps excess cash to the lender | Lets the lender capture cash in a downturn before value falls further |
| Franchise | Comfort letter from the brand; loan default if the flag is lost | The flag is part of the collateral |

#### 11.4.9 PIP-adjusted price and the return on renovation

A buyer who must complete a PIP can pay

$$P = V_{stab} - PIP(1+\kappa) - \text{Displacement} - \text{Carry and soft costs} - \rho\,PIP(1+\kappa), \tag{11.3}$$

with contingency $\kappa$ and required profit $\rho$ on renovation capital. `sdesk.hotel.pip_adjusted_price` implements (11.3). The last term is the one sellers forget: renovation capital bears execution risk, and a buyer who does a PIP "at cost" is working for free.

The **RevPAR lift needed** for a PIP to earn a hurdle $h$ on its all-in cost is

$$\Delta RevPAR^* = \frac{h \times PIP(1+\kappa)}{N \times D \times FT_{NOI}}, \tag{11.4}$$

where $FT_{NOI}$ is NOI flow-through on rooms revenue. When $\Delta RevPAR^*$ exceeds any plausible lift, the PIP does not pay for itself. It may still be worth doing, because the alternative is the loss of the flag (Case D, Case 11.3). That comparison, and not the stand-alone return, decides most PIPs.

#### 11.4.10 Going-concern allocation

$$V_{TAB} = V_{real\ property} + V_{FF\&E} + V_{intangibles}.$$

Appraisers disagree about how to measure the intangible component. One family of methods holds that deducting market management and franchise fees from income already strips out the return to the business, so the remaining value is real property plus FF&E. Another identifies specific intangibles (assembled workforce, flag, booking pace, start-up costs) and values each. The method matters because property tax is levied on real property (and, in some jurisdictions, tangible personal property), not on intangibles. Income-tax recovery periods differ by asset class. Lenders take real property and FF&E as collateral but cannot foreclose on a workforce. Case 11.7 quantifies all three effects.

#### 11.4.11 Seasonal working capital

Let $CF_m$ be monthly cash flow after debt service and $S_m = \sum_{j\le m} CF_j$. The working-capital reserve needed to survive the off-season without new equity is the largest peak-to-trough decline in $S$:

$$W = \max_{m}\Big(\max_{j \le m} S_j - S_m\Big).$$

If a cash trap sweeps peak-season surplus to the lender, the owner can no longer fund the trough from that surplus, and the equity requirement rises toward the sum of all negative months (Case 11.5).

---
### 11.5 Worked examples

The five examples below build the toolkit. The eight comprehensive cases in §11.6 apply it to full decisions. All inputs are [HYPOTHESIS]. Every number is reproduced in `tests/test_ch11_examples.py`.

#### Example 11.1 — RevPAR up 7.1%, share down: the opening hotel against its comp set

**Given.** The opening hotel (132 rooms). Prior year: Occ 74.0%, ADR \$142.00. T-12: Occ 71.0%, ADR \$158.50. The STR-style comp set: prior year Occ 72.0%, ADR \$139.00; T-12 Occ 73.0%, ADR \$150.00.

**Find.** RevPAR growth and its decomposition; comp-set RevPAR growth; MPI, ARI, RGI in both years; the rooms revenue the hotel gave up by losing share.

**Solution.**

RevPAR: prior $0.74 \times 142.00 = \$105.08$; T-12 $0.71 \times 158.50 = \$112.535$. Growth $= 112.535/105.08 - 1 = +7.09\%$.

Decomposition: occupancy $0.71/0.74 - 1 = -4.05\%$; ADR $158.50/142.00 - 1 = +11.62\%$. In logs: $\ln(1.0709) = 0.0685 = -0.0414 + 0.1099$. Rate did all the work, and more than all of it.

Comp set: RevPAR $0.72 \times 139 = \$100.08$, then $0.73 \times 150 = \$109.50$, growth **+9.41%**.

| Index | Prior year | T-12 |
|---|---|---|
| MPI | $100 \times 0.74/0.72 = 102.8$ | $100 \times 0.71/0.73 = 97.3$ |
| ARI | $100 \times 142/139 = 102.2$ | $100 \times 158.5/150 = 105.7$ |
| RGI | 105.0 | 102.8 |

Had the hotel held its prior RGI of 105.0 against the T-12 comp RevPAR, its RevPAR would have been $1.050 \times 109.50 = \$114.97$. Rooms revenue forgone $= (114.97 - 112.535) \times 132 \times 365 \approx \$117{,}300$.

**Check.** $RGI = MPI \times ARI/100$: $97.26 \times 105.67/100 = 102.77$. ✓

**Decision consequence.** "RevPAR up 7.1%" is true and misleading. The market rose 9.4%; the hotel lost 2.2 points of RGI and moved from a share premium in occupancy to a share deficit, while pushing rate above the comp set. Either revenue management priced out demand or the product is losing appeal and rate is masking it. A buyer underwriting the T-12 should ask which, because the answers carry different values. Rate overreach is fixable in a quarter; product obsolescence needs a PIP. The BOV should present the RGI trend, not the RevPAR headline.

**Reproduce.** `tests/test_ch11_examples.py::test_example_11_1`

#### Example 11.2 — Flow-through: rate-led versus occupancy-led RevPAR growth

**Given.** A stylized 132-room select-service hotel at Occ 72.0% and ADR \$150.00 (Exhibit 11.2 below). Other revenue 5% of rooms revenue at a 60% departmental cost ratio. Variable rooms cost \$36 per occupied room. Undistributed: \$1,450,000 fixed plus 4% of total revenue. Management 3% of total revenue; franchise fees 11.5% of rooms revenue; property tax \$260,000; insurance \$110,000; reserve 4% of total revenue. Grow RevPAR 5% in two ways: (a) ADR +5%; (b) occupancy +5% (to 75.6%).

**Find.** Base P&L; GOP and NOI flow-through in each case; the value difference at a 9% cap on NOI.

**Solution.** Exhibit 11.2 (base), from `sdesk.hotel.operating_statement`:

| Line | \$ | Per available room-night |
|---|---:|---:|
| Rooms sold (34,689.6 of 48,180) | | Occ 72.0% |
| Rooms revenue | 5,203,440 | RevPAR \$108.00 |
| Other revenue | 260,172 | |
| **Total revenue** | **5,463,612** | TRevPAR \$113.40 |
| Rooms expense (\$36 × rooms sold) | 1,248,826 | |
| Other departmental expense | 156,103 | |
| Undistributed | 1,668,544 | |
| **GOP** | **2,390,139** | GOPPAR \$49.61; margin 43.75% |
| Management fee | 163,908 | |
| Franchise fees | 598,396 | |
| Property tax, insurance | 370,000 | |
| **EBITDA** | **1,257,835** | |
| FF&E reserve (4%) | 218,544 | |
| **NOI** | **1,039,290** | 19.0% margin |

Both cases raise total revenue by \$273,181.

| | ΔNOI | GOP flow-through | NOI flow-through | %ΔNOI ÷ %ΔRevenue |
|---|---:|---:|---:|---:|
| (a) ADR +5% | \$205,406 | 93.14% | 75.19% | 3.95 |
| (b) Occupancy +5% | \$142,965 | 70.29% | 52.33% | 2.75 |

Intermediate steps for (b): extra rooms sold $= 0.05 \times 34{,}689.6 = 1{,}734.5$; extra variable rooms cost $= 1{,}734.5 \times \$36 = \$62{,}441$. That is the entire difference between (a) and (b), because the percentage-of-revenue costs are identical in both.

Closed form (§11.4.3): $v = 0.04 + 0.03 + 0.115/1.05 + 0.04 + 0.60 \times 0.05/1.05 = 0.2481$, so $FT_{rate} = 75.19\%$ and $FT_{occ} = 0.7519 - 36/157.50 = 0.7519 - 0.2286 = 52.33\%$. ✓

Value difference at 9%: $(205{,}406 - 142{,}965)/0.09 = \$693{,}792$.

**Check.** GOP flow-through on rate is $(0.96 \times 1 + 0.36 \times 0.05)/1.05 = 93.14\%$: only the 4% undistributed variable cost and the other-department cost absorb rate gains at the GOP line. ✓

**Decision consequence.** The same RevPAR growth is worth \$0.69 million more in value when it comes from rate. When a seller's pro forma shows RevPAR growth, ask for the occupancy and rate split, and apply the matching flow-through. A pro forma that grows occupancy and applies a rate-led flow-through overstates NOI. The 3.95 operating-leverage ratio also cuts the other way: a 5% rate decline removes about 20% of NOI.

**Reproduce.** `tests/test_ch11_examples.py::test_example_11_2`

#### Example 11.3 — The fee stack, and the cap rate that belongs to EBITDA

**Given.** Exhibit 11.2. The 11.5% franchise charge consists of a 5.5% royalty, 3.0% marketing fee, 1.5% reservation and technology fee, and 1.5% loyalty-program assessment, all on rooms revenue [HYPOTHESIS: actual rates and bases differ by brand and contract]. Management fee 3% of total revenue. The market prices comparable hotels at a 9.0% cap on NOI after a 4% reserve.

**Find.** Each fee in dollars; total fees as a share of revenue and of GOP; value; the cap rate on EBITDA; the error from capitalizing EBITDA at 9%.

**Solution.**

| Fee | Base | \$ |
|---|---|---:|
| Royalty 5.5% | Rooms revenue \$5,203,440 | 286,189 |
| Marketing 3.0% | Rooms revenue | 156,103 |
| Reservation/technology 1.5% | Rooms revenue | 78,052 |
| Loyalty 1.5% | Rooms revenue | 78,052 |
| **Franchise total** | | **598,396** |
| Base management 3% | Total revenue \$5,463,612 | 163,908 |
| **All fees** | | **762,304** |

Fees are 13.95% of total revenue and **31.89% of GOP**. Value at 9% on NOI $= 1{,}039{,}290/0.09 = \$11{,}547{,}670$. The cap rate on EBITDA at that value is $1{,}257{,}835/11{,}547{,}670 = 10.89\%$. Capitalizing EBITDA at 9% gives \$13,975,942, an overstatement of **\$2,428,272**.

**Check.** The overstatement equals the capitalized reserve: $218{,}544/0.09 = \$2{,}428{,}272$. ✓ Also $c_{EBITDA} = 0.09 \times 1{,}257{,}835/1{,}039{,}290 = 10.89\%$. ✓

**Decision consequence.** Almost a third of GOP leaves the hotel before the owner's NOI. That makes the fee stack a value lever: a conversion to a lower-fee brand or a renegotiated management contract changes NOI as much as a large RevPAR gain (Cases 11.3 and 11.4). The cap-rate error is the most common one in owner-prepared valuations, including the opening problem. It is also the one most easily caught: ask "cap rate on which line, after what reserve?" A cap rate quoted without the line is not a cap rate.

**Reproduce.** `tests/test_ch11_examples.py::test_example_11_3`

#### Example 11.4 — How a hotel lender sizes the same NOI

**Given.** A 240-room hotel with T-12 NOI (after 4% reserve) of \$2,150,000. The seller's pro forma NOI is \$2,400,000. An appraiser values the hotel at an 8.75% cap on pro forma NOI. Loan terms: 7.50%, 25-year amortization, monthly payments. The hotel lender requires a maximum 60% LTV, a minimum 1.50x DSCR, and a minimum 12.0% debt yield, all on T-12 NOI. For comparison, a multifamily lender would apply 70% LTV, 1.25x and 8.0% to the same numbers.

**Find.** The appraised value; each constraint; the binding constraint and loan for each lender; the hotel loan's actual LTV and debt yield; how far NOI can fall before DSCR reaches 1.0x.

**Solution.**

Value $= 2{,}400{,}000/0.0875 = \$27{,}428{,}571$. Loan constant $K = 12 \times PMT(0.075/12, 300, 1) = 0.08868$.

| Constraint | Hotel lender | Multifamily lender |
|---|---:|---:|
| LTV | $0.60 \times 27{,}428{,}571 = \$16{,}457{,}143$ | $0.70 \times 27{,}428{,}571 = \$19{,}200{,}000$ |
| DSCR | $2{,}150{,}000/(1.50 \times 0.08868) = \$16{,}163{,}176$ | $2{,}150{,}000/(1.25 \times 0.08868) = \$19{,}395{,}811$ |
| Debt yield | $2{,}150{,}000/0.12 = \$17{,}916{,}667$ | $2{,}150{,}000/0.08 = \$26{,}875{,}000$ |
| **Binding** | **DSCR: \$16,163,176** | **LTV: \$19,200,000** |

Hotel loan: annual debt service $= 16{,}163{,}176 \times 0.08868 = \$1{,}433{,}333$; actual LTV 58.93%; actual debt yield 13.30%. DSCR reaches 1.0x when NOI falls to \$1,433,333, a decline of **33.3%**.

**Check.** $1 - 1/1.50 = 33.3\%$: at the DSCR-binding loan, the cushion is exactly $1 - 1/DSCR_{min}$. ✓

**Decision consequence.** The hotel lender lends about \$3.0 million less than a multifamily lender would on the same income, and none of the shortfall comes from the pro forma. The buyer who planned equity around a 70% loan is \$3.0 million short. The 33% cushion looks large until it is compared with §11.10, where U.S. RevPAR in April 2020 was about 80% below April 2019. The lender's conservatism is not timidity; it is an estimate of hotel income volatility. Cases 11.5 and D show what the lender adds on top: cash management, FF&E escrows and a PIP reserve.

**Reproduce.** `tests/test_ch11_examples.py::test_example_11_4`

#### Example 11.5 — Segment mix: ADR-maximizing is not contribution-maximizing

**Given.** A 200-room hotel at 75.0% occupancy (54,750 room-nights a year). Segment mix by room-nights: transient 60% at \$172 ADR with a 15% acquisition cost; group 25% at \$148 with a 5% acquisition cost and \$40 of banquet contribution per room-night; airline-crew contract 15% at \$109 with no acquisition cost. Variable cost per occupied room \$40 in all segments. The new asset manager proposes to drop the crew contract "to lift ADR". The revenue manager estimates that 60% of the freed room-nights would sell to transient guests at \$172.

**Find.** Blended ADR and RevPAR; contribution per room-night by segment; the effect of dropping the contract on ADR, occupancy, RevPAR and contribution; the transient fill rate at which dropping the contract breaks even.

**Solution.**

Blended ADR $= 0.60 \times 172 + 0.25 \times 148 + 0.15 \times 109 = \$156.55$. RevPAR $= 0.75 \times 156.55 = \$117.41$.

| Segment | Net revenue per room-night | Contribution per room-night (after \$40 CPOR) |
|---|---:|---:|
| Transient | $172 \times 0.85 = \$146.20$ | \$106.20 |
| Group | $148 \times 0.95 + 40 = \$180.60$ | \$140.60 |
| Contract | \$109.00 | \$69.00 |

The group segment, despite an ADR \$24 below transient, is the most valuable per room-night.

Dropping the contract frees $0.15 \times 54{,}750 = 8{,}212.5$ room-nights. Refilled at 60%: 4,927.5 transient room-nights, contribution $4{,}927.5 \times 106.20 = \$523{,}300.50$. Lost contract contribution $= 8{,}212.5 \times 69.00 = \$566{,}662.50$. **Net: −\$43,362 a year.**

After the change, ADR rises to \$165.62 (+5.8%), occupancy falls to 70.5%, and RevPAR falls to \$116.76. The break-even fill rate is $69.00/106.20 = 64.97\%$.

**Check.** Room-nights after the change: $54{,}750 - 8{,}212.5 + 4{,}927.5 = 51{,}465$; $51{,}465/73{,}000 = 70.5\%$. ✓

**Decision consequence.** The proposal raises the metric a casual reader of an STR report notices (ADR, and ARI) and lowers the ones that pay the owner (RevPAR, contribution). Keep the contract unless the transient forecast supports a refill above 65%, and renegotiate its rate at renewal instead. Contract business also has a value the annual figures understate: it fills the low season, which matters for working capital (Case 11.5) and for lender covenants.

**Reproduce.** `tests/test_ch11_examples.py::test_example_11_5`

---

### 11.6 Eight comprehensive hotel cases

Each case below states its data, solves it numerically, and ends in a decision with a "Decision consequence" and the facts that would change it. All inputs are [HYPOTHESIS]; market parameters (cap rates, fee rates, wage levels, PIP costs) are plausible teaching assumptions, not sourced data. Every number is reproduced in `tests/test_ch11_examples.py` (functions `case11_1` … `case11_8`).

These cases are deliberately distinct from Case A (seller anchoring on cost, with a full normalization) and Case D (a contested PIP negotiated from the buyer's side). Equation numbers refer to §11.4.

| Case | Hotel | Question |
|---|---|---|
| 11.1 | 120-room upscale select-service | Why did NOI fall when RevPAR rose? |
| 11.2 | 300-room full-service | Should we take the group? |
| 11.3 | 140-room upper-midscale | Renew the flag, convert, or go independent? |
| 11.4 | 250-room full-service, managed | Accept the manager's new fee proposal? |
| 11.5 | 160-room seasonal beach resort | How much working capital, and what does the cash trap cost? |
| 11.6 | 150-room select-service | What does a 20% housekeeping wage shock do to break-even occupancy? |
| 11.7 | 210-room full-service, special servicer | What is the BOV under stress, and how should value be allocated? |
| 11.8 | 130-room select-service, PIP due | Sell now or after the PIP? |

---

#### Case 11.1 — RevPAR up 6%, NOI down 17%: a flow-through diagnosis

##### Situation

You are the asset manager for a fund that owns a 120-room upscale select-service hotel. The operator's year-end letter opens: "RevPAR grew 6.1%, well ahead of budget." The fund's controller notes that NOI fell 17%. The investment committee wants to know which statement describes the asset, whether the decline is permanent, and what number a buyer would capitalize.

##### Data (Exhibit 11.1-1)

| Driver | Year 1 | Year 2 |
|---|---:|---:|
| Occupancy | 70.0% | 76.0% |
| ADR | \$140.00 | \$136.75 |
| Housekeeping hours per occupied room | 0.55 | 0.55 |
| Housekeeping loaded wage | \$19.00 | \$21.00 |
| Fixed rooms labor (front desk, night audit, supervisors) | \$360,000 | \$396,000 |
| Non-labor cost per occupied room (amenities, laundry, breakfast) | \$14.00 | \$15.00 |
| OTA share of rooms revenue | 18% | 27% |
| OTA commission rate | 17% | 17% |
| A&G, S&M, POM, utilities, IT (fixed \$) | \$1,060,000 | \$1,129,000 |
| Card fees (% of total revenue, in A&G) | 2.5% | 2.5% |
| Property tax | \$140,000 | \$168,000 |
| Insurance | \$70,000 | \$98,000 |

Common to both years: other revenue 3% of rooms revenue at a 50% departmental cost ratio; management fee 3% of total revenue; franchise fees 11% of rooms revenue; FF&E reserve 4% of total revenue; market cap rate 9.0% on NOI after reserve.

##### Solution

**Step 1: the P&L in both years.**

| Line | Year 1 | Year 2 | Change |
|---|---:|---:|---:|
| Rooms sold | 30,660 | 33,288 | +2,628 |
| RevPAR | \$98.00 | \$103.93 | +6.05% |
| Rooms revenue | 4,292,400 | 4,552,134 | +259,734 |
| Total revenue | 4,421,172 | 4,688,698 | +267,526 |
| Housekeeping labor | 320,397 | 384,476 | +64,079 |
| OTA commissions | 131,347 | 208,943 | +77,596 |
| Total rooms expense | 1,240,984 | 1,488,739 | +247,755 |
| Undistributed | 1,170,529 | 1,246,217 | +75,688 |
| **GOP** | **1,945,272** | **1,885,459** | **−59,813** |
| GOP margin | 44.0% | 40.2% | |
| Franchise fees | 472,164 | 500,735 | |
| **EBITDA** | **1,130,473** | **978,064** | |
| FF&E reserve | 176,847 | 187,548 | |
| **NOI** | **953,626** | **790,516** | **−163,111 (−17.1%)** |
| NOI margin | 21.6% | 16.9% | |

GOP flow-through $= -59{,}813/267{,}526 = -22.4\%$. NOI flow-through $= -163{,}111/267{,}526 = -61.0\%$. Each incremental dollar of revenue came with a \$0.61 fall in NOI.

**Step 2: a sequential bridge.** Change one driver at a time, in the order shown, holding the others at their prior values.

| Step | ΔNOI (\$) |
|---|---:|
| 1. Volume and rate (Year 2 occupancy and ADR at Year 1 unit costs and channel mix) | +137,442 |
| 2. OTA channel shift (18% → 27% of rooms revenue) | −69,648 |
| 3. Wage inflation (housekeeping \$19 → \$21; fixed rooms labor +10%) | −72,617 |
| 4. Non-labor cost per occupied room \$14 → \$15 | −33,288 |
| 5. Undistributed cost inflation | −69,000 |
| 6. Property tax and insurance | −56,000 |
| **Total** | **−163,111** |

**Step 3: read the bridge.**

* The revenue gain was occupancy-led (occupancy +8.6%, ADR −2.3%). At Year 1 costs and mix it would have flowed through at $137{,}442/267{,}526 = 51.4\%$, close to the occupancy-led figure of Example 11.2. The growth itself was not the problem.
* The occupancy was bought. The OTA share rose 9 points. The commission cost of that shift was \$69,648, which is **\$26.50 per incremental room-night** sold (2,628 extra room-nights). Against an ADR of \$136.75, the operator gave up about a fifth of the rate on the incremental business before housekeeping touched the room.
* Cost inflation (steps 3–6) took \$230,905. Of that, wages (\$72,617) and the tax and insurance increases (\$56,000) are structural. A reassessment and a hardening insurance market do not reverse because the operator tries harder. Some undistributed inflation may be one-off; the controller should identify it line by line.

**Step 4: value.** At 9.0%: Year 1 NOI is worth \$10,595,847 and Year 2 NOI \$8,783,507, a difference of \$1.81 million.

**Check.** The six bridge steps sum to the total NOI change (−\$163,111) to the dollar, because each step is computed by full re-run of the P&L, not by approximation. ✓

##### Decision

The committee should **underwrite Year 2 NOI as the base**, adjusted only for items shown to be non-recurring, and should not accept "RevPAR +6%" as evidence of value creation. Three actions follow:

1. **Channel mix.** Ask the operator for a channel-contribution report: rooms revenue net of commissions and loyalty costs, by channel. A shift to OTA business is justified only if the displaced alternative was empty rooms. At 76% occupancy on a 120-room hotel, it is unlikely that every one of the 2,628 extra room-nights required an OTA.
2. **Labor productivity.** Housekeeping minutes per occupied room (33 minutes here) and fixed staffing are the levers. Case 11.6 quantifies them.
3. **Budget discipline.** A budget that rewards RevPAR rather than GOP or NOI will produce this outcome again. Align the operator's incentive with the owner's line (Case 11.4).

**Decision consequence.** For a sale, the market will capitalize Year 2 NOI (\$790,516), not Year 1. Presenting Year 1 NOI as "normalized" without evidence that commissions and costs will reverse is seller anchoring of the kind Case A dismantles. The fund's book value should be marked toward \$8.8 million, not \$10.6 million, until the operator demonstrates a reversal.

**What would change the decision.** Evidence that the OTA shift filled rooms that would otherwise have gone empty, and that it was temporary (for example, a brand-channel outage). A one-off insurance spike reversed by a rebid. A demand generator that supports occupancy without commission (a new corporate account).

**Reproduce.** `tests/test_ch11_examples.py::test_case_11_1`

---

#### Case 11.2 — The group on peak nights: displacement and the minimum rate

##### Situation

You are director of revenue management at a 300-room full-service hotel. A medical association requests a block of 180 rooms per night for Tuesday to Thursday (three nights) in the second week of October, at a group rate of \$189, with banquets. Your transient forecast for those nights is strong. The sales director wants to sign today.

##### Data (Exhibit 11.2-1)

| Item | Value |
|---|---|
| Rooms | 300 |
| Base contract business (airline crew), every night | 35 rooms at a negotiated rate (unaffected) |
| Group block / rate / nights | 180 rooms, \$189, 3 nights |
| Expected pickup | 90% of block (the contract allows 20% attrition without penalty) |
| Unsold block released at cutoff (21 days out) | resold to transient with probability 50% |
| Group commission (third-party planner) | 7% of group rooms revenue |
| Banquet spend per group room-night / departmental margin | \$110 / 38% |
| Transient unconstrained demand per night (forecast) | 200 rooms at \$265 ADR |
| Transient acquisition cost (OTA, GDS, loyalty, blended) | 12% of transient rooms revenue |
| Transient outlet F&B spend per occupied room / margin | \$30 / 25% |
| Variable cost per occupied room | \$45 |
| Brand fees on rooms revenue / management fee on total revenue | 8% / 3% |
| Shoulder nights (Mon, Fri) | 5% of displaced room-nights belong to stays that also covered Monday or Friday; those nights are lost at \$219 |
| Forecast uncertainty | demand 160 (p = 0.30), 200 (p = 0.50), 240 (p = 0.20) rooms per night |

##### Solution

**Step 1: contribution per room-night.**

Group: $189 \times (1 - 0.07 - 0.08 - 0.03) - 45 + 110 \times (0.38 - 0.03) = 154.98 - 45 + 38.50 = \$148.48$.

Transient: $265 \times (1 - 0.12 - 0.08 - 0.03) - 45 + 30 \times (0.25 - 0.03) = 204.05 - 45 + 6.60 = \$165.65$.

Shoulder transient at \$219: $219 \times 0.77 - 45 + 6.60 = \$130.23$.

The group pays \$76 less in rate but only \$17 less in contribution, because banquet profit and lower acquisition cost close most of the gap.

**Step 2: how many transient guests are displaced.** Picked-up group rooms $= 0.90 \times 180 = 162$. Released at cutoff $= 18$, of which half resell. Capacity left for transient while the block is protected $= 300 - 35 - 180 + 0.5 \times 18 = 94$ per night. Without the group, all 200 transient guests fit ($300 - 35 = 265$). Displaced $= 200 - 94 = 106$ rooms per night, or 318 room-nights. Shoulder room-nights lost $= 0.05 \times 318 = 15.9$.

**Step 3: the comparison (base forecast).**

| | Room-nights | Contribution (\$) | Revenue (\$) |
|---|---:|---:|---:|
| Group | 486 | 72,161 | 145,314 |
| Displaced transient (peak) | 318 | 52,677 | |
| Displaced transient (shoulder) | 15.9 | 2,071 | |
| Displaced total | | 54,747 | 97,769 |
| **Net effect of accepting** | | **+17,414** | **+47,545** |

**Step 4: the minimum group rate.** Setting $486 \times [0.82\,r - 45 + 38.50] = 54{,}747$ gives $r^* = \$145.30$. Any group rate above \$145.30 adds contribution at the base forecast.

**Step 5: the forecast is uncertain.**

| Transient demand | p | Displaced per night | Net contribution of accepting | Break-even group rate |
|---|---:|---:|---:|---:|
| 160 | 0.30 | 66 | +38,073 | \$93.46 |
| 200 | 0.50 | 106 | +17,414 | \$145.30 |
| 240 | 0.20 | 146 | −3,245 | \$197.14 |
| **Expected** | | | **+19,480** | |

**Step 6: alternate dates.** The association's planner has said Sunday to Tuesday of the same week would work. Transient demand on those nights is forecast at 90 rooms, which fits within the 94 rooms left after the block. Nothing is displaced and the net gain is the full \$72,161.

**Check.** At $r^*$, group contribution $= 486 \times (0.82 \times 145.30 - 6.50) = 486 \times 112.65 \approx \$54{,}747$, equal to the displaced contribution. ✓

##### Decision

**Counter with the alternate dates at \$189** (net +\$72,161). If the association insists on Tuesday–Thursday, accept at \$189 only with (a) a cutoff at 21 days with no extension, (b) an attrition clause at 80% with liquidated attrition charges, and (c) a food-and-beverage minimum that protects the \$110 banquet assumption. If the transient pace report three weeks before the first counter shows demand trending to the high case, do not accept below about \$197.

**Decision consequence.** The decision looks like "accept" on revenue (+\$47,545) and still "accept" on expected contribution (+\$19,480). But the margin of safety is thin: one scenario in five destroys value, and the expected gain is smaller than the gain from moving the dates. Revenue management is a pricing decision under a forecast. The output is a minimum rate conditional on demand, not "yes". Note also what the revenue figure hides: accepting adds \$47,545 of revenue but only \$17,414 of contribution, because the group arrives with commissions and banquet costs. A sales team paid on revenue will always want the group.

**What would change the decision.** A pace report that shows transient demand building above 240 (decline or raise the rate). Evidence that the association would return annually on low-demand dates (the lifetime value of the account may justify a one-time displacement). A banquet minimum below \$110.

**Reproduce.** `tests/test_ch11_examples.py::test_case_11_2`

---

#### Case 11.3 — Renew the flag, convert, or go independent

##### Situation

You advise the owner of a 140-room upper-midscale hotel whose franchise agreement expires in 12 months. Three options are on the table: renew with the current brand (which requires a PIP), convert to a lower-fee conversion brand from another family (smaller PIP, key money offered), or operate as an independent (no brand fees, no PIP, but higher distribution costs and a weaker demand engine). The comp set's stabilized RevPAR is \$95.00.

##### Data (Exhibit 11.3-1)

| | Renew | Convert | Independent |
|---|---:|---:|---:|
| Stabilized RGI | 108 | 101 | 93 |
| Stabilized occupancy | 74% | 71% | 68% |
| Brand fees (% rooms revenue) | 12.0% | 9.5% | 0% |
| Distribution cost (OTA and GDS, % rooms revenue) | 4.0% | 5.0% | 9.0% |
| Added sales & marketing (website, revenue management, sales staff) | — | — | \$175,000 |
| Capital (PIP or rebranding) | \$2,240,000 (\$16,000/key) | \$1,260,000 (\$9,000/key) | \$700,000 (\$5,000/key) |
| Key money | — | \$280,000 | — |
| Year-1 RGI during ramp-up | 104 | 95 | 84 |
| Cap rate on stabilized NOI | 8.75% | 9.00% | 9.50% |

Common: other revenue 3% of rooms revenue at 55% cost; \$34 variable cost per occupied room; undistributed \$1,400,000 fixed plus 3% of revenue; management 3%; property tax \$190,000; insurance \$110,000; reserve 4%. Higher cap rates for weaker flags reflect a thinner buyer and lender pool [HYPOTHESIS]. Key money is forgiven over the agreement term and repayable on early exit.

##### Solution

**Step 1: stabilized operations.** Subject RevPAR $= RGI \times 95.00/100$, and ADR $= RevPAR/\text{Occ}$.

| | Renew | Convert | Independent |
|---|---:|---:|---:|
| RevPAR | \$102.60 | \$95.95 | \$88.35 |
| ADR | \$138.65 | \$135.14 | \$129.93 |
| Total revenue | 5,400,146 | 5,050,136 | 4,650,126 |
| Brand fees + distribution | 838,858 | 710,942 | 406,322 |
| **NOI** | **949,090** | **819,727** | **647,867** |
| Value at the option's cap rate | 10,846,748 | 9,108,077 | 6,819,653 |

**Step 2: net value created.** Net value = stabilized value − capital + key money − year-1 NOI shortfall during ramp-up.

| | Renew | Convert | Independent |
|---|---:|---:|---:|
| Stabilized value | 10,846,748 | 9,108,077 | 6,819,653 |
| Capital | −2,240,000 | −1,260,000 | −700,000 |
| Key money | — | +280,000 | — |
| Ramp-up NOI shortfall | −98,114 | −149,687 | −244,148 |
| **Net value** | **8,508,633** | **7,978,390** | **5,875,505** |

**Step 3: the incremental decision.** Renewing instead of converting costs $2{,}240{,}000 - 1{,}260{,}000 + 280{,}000 = \$1{,}260{,}000$ more (the forgone key money counts as a cost) and adds \$129,363 of NOI: a **10.27%** unlevered yield on the incremental capital, before the cap-rate benefit of the stronger flag.

**Step 4: what independence requires.** Holding the independent cost structure, the RGI at which independence matches renewal's net value is **103.2**: an independent hotel would have to beat its comp set by 3 points with no brand engine. The case assumes 93.

**Check.** Renew NOI rebuilt by hand: rooms revenue $= 140 \times 365 \times 0.74 \times 138.6486 = \$5{,}242{,}860$ (ADR carried at full precision, $102.60/0.74$); brand plus distribution at 16% $= \$838{,}858$. ✓

##### Decision

**Renew**, provided the PIP letter is within 10% of \$2.24 million and the new agreement runs at least ten years with a reasonable area of protection.

**Decision consequence.** The brand's fees are high, but the brand's RGI premium pays for them with room to spare. The fee comparison that owners instinctively make (12% versus 0%) is the wrong one. The right comparison is NOI after fees *and* after the demand the fees buy. Independence fails here not because brands are always better but because an RGI of 103 without a reservation system and loyalty program is not a credible assumption for this upper-midscale hotel. Conversion is the defensible fallback if the PIP letter comes in high: the gap between renewal and conversion is only \$0.53 million of net value, so a renewal PIP above about \$2.77 million (\$2.24 million plus \$0.53 million) reverses the ranking.

**What would change the decision.** A location with strong direct demand (a university, a hospital campus, a resort destination) where an independent can plausibly reach RGI above 100. A renewal PIP above \$2.77 million. A conversion brand with a demonstrated RGI above 104 in this market. A lender that will not finance an independent at all, which would make independence worse than the table shows.

**Reproduce.** `tests/test_ch11_examples.py::test_case_11_3`

---

#### Case 11.4 — The management contract: incentive fee and owner's priority

##### Situation

You represent the owner of a 250-room full-service hotel managed under a third-party contract. The owner has invested \$52 million (purchase plus renovation). The manager proposes to cut the base fee from 3% to 2% of total revenue in exchange for a larger incentive fee with a lower owner's priority. The manager calls it "putting our money where our mouth is". The owner asks whether to accept.

##### Data (Exhibit 11.4-1)

| Contract | Base fee | Incentive fee | Owner's priority |
|---|---|---|---|
| Existing | 3.0% of total revenue | 20% of ACF above priority | 8% of \$52m = \$4.16m |
| Proposed | 2.0% of total revenue | 25% of ACF above priority | 6% of \$52m = \$3.12m |
| Alternative (benchmark) | 3.0% of total revenue | 10% of GOP, no priority | — |

ACF (available cash flow) = GOP − base fee − property tax (\$900,000) − insurance (\$650,000) − FF&E reserve (4% of total revenue). Scenarios for next year:

| Scenario | p | Total revenue | GOP |
|---|---:|---:|---:|
| Downturn | 0.25 | \$17,500,000 | \$4,200,000 |
| Base | 0.50 | \$22,000,000 | \$7,040,000 |
| Strong | 0.25 | \$24,500,000 | \$8,820,000 |

##### Solution

**Step 1: existing contract.** Base case: base fee $= 0.03 \times 22{,}000{,}000 = \$660{,}000$; reserve \$880,000; ACF $= 7{,}040{,}000 - 660{,}000 - 900{,}000 - 650{,}000 - 880{,}000 = \$3{,}950{,}000$, below the \$4.16 million priority, so no incentive fee.

| Existing | Downturn | Base | Strong |
|---|---:|---:|---:|
| Base fee | 525,000 | 660,000 | 735,000 |
| ACF | 1,425,000 | 3,950,000 | 5,555,000 |
| Incentive fee | 0 | 0 | $0.20 \times (5{,}555{,}000 - 4{,}160{,}000) = 279{,}000$ |
| Owner cash (ACF − IMF) | 1,425,000 | 3,950,000 | 5,276,000 |

**Step 2: proposed contract.**

| Proposed | Downturn | Base | Strong |
|---|---:|---:|---:|
| Base fee | 350,000 | 440,000 | 490,000 |
| ACF | 1,600,000 | 4,170,000 | 5,800,000 |
| Incentive fee | 0 | $0.25 \times (4{,}170{,}000 - 3{,}120{,}000) = 262{,}500$ | 670,000 |
| Owner cash | 1,600,000 | 3,907,500 | 5,130,000 |

**Step 3: the GOP-based benchmark.** Incentive fee $= 0.10 \times GOP$ = 420,000 / 704,000 / 882,000; owner cash 1,005,000 / 3,246,000 / 4,673,000.

**Step 4: expected values.**

| Contract | E[owner cash] | E[manager fees] |
|---|---:|---:|
| Existing | 3,650,250 | 714,750 |
| Proposed | 3,636,250 | 728,750 |
| GOP-based | 3,042,500 | 1,322,500 |

**Step 5: where the proposal starts to cost the owner.** Holding the base-case GOP margin of 32%, the proposal pays the manager more than the existing contract whenever GOP exceeds **\$6,792,727** (total revenue about \$21.2 million). That is below the base case.

**Check.** Strong case, proposed: base fee $0.02 \times 24{,}500{,}000 = 490{,}000$; reserve 980,000; ACF $= 8{,}820{,}000 - 490{,}000 - 1{,}550{,}000 - 980{,}000 = 5{,}800{,}000$; IMF $= 0.25 \times 2{,}680{,}000 = 670{,}000$. ✓

##### Decision

**Counter, do not accept as proposed.** The proposal is nearly neutral in expectation (−\$14,000 a year to the owner) but redistributes risk: it gives the owner \$175,000 more in a downturn and takes \$42,500 in the base case and \$146,000 in a strong year. The manager is selling a put (lower base fee in bad years) and buying a call (a 25% share struck lower). A reasonable counter keeps the lower base fee, keeps the priority at 8%, and accepts a 25% incentive share, with an annual cap on the incentive fee and a performance test (for example, termination without fee if RGI is below 95 and GOP below 90% of budget in two consecutive years).

**Decision consequence.** Valued at an 8.5% cap rate, the base-case reduction in owner cash (\$42,500) is a \$500,000 transfer to the manager in sale value, because buyers capitalize NOI after all fees. The GOP-based benchmark shows why contract structure matters more than the headline percentage: a "10% incentive" on GOP without a priority costs the owner \$608,000 a year in expectation versus the existing contract, because it pays the manager even in years when the owner earns a small fraction of the priority. Incentive fees are options. Value them as options, with scenarios, before calling them "alignment".

**What would change the decision.** A manager track record of beating budget GOP by enough to move the base case above the \$6.79 million crossover by a wide margin (the owner then pays more but earns more). A lender requirement that management fees be subordinated below debt service. A planned sale within two years, in which case an unencumbered or terminable contract may be worth more than any fee saving.

**Reproduce.** `tests/test_ch11_examples.py::test_case_11_4`

---
#### Case 11.5 — The seasonal resort: working capital and the cash trap

##### Situation

A fund is buying a 160-room independent beach resort with a \$21.0 million loan at 7.25%, 25-year amortization (monthly payments). The loan has a cash-management provision: if trailing-12 DSCR falls below 1.30x, all cash after operating expenses, reserves and debt service is swept monthly into a lender-controlled account and is not released until DSCR exceeds the trigger for two consecutive quarters. The investment committee asks how much working capital the fund must hold, and what the cash trap does to that number.

##### Data (Exhibit 11.5-1)

| Month | Occ | ADR | Month | Occ | ADR |
|---|---:|---:|---|---:|---:|
| Jan | 42% | \$165 | Jul | 93% | \$345 |
| Feb | 50% | \$185 | Aug | 85% | \$300 |
| Mar | 78% | \$260 | Sep | 55% | \$205 |
| Apr | 80% | \$255 | Oct | 50% | \$190 |
| May | 82% | \$270 | Nov | 40% | \$160 |
| Jun | 90% | \$320 | Dec | 45% | \$185 |

Other revenue (F&B, spa, parking) 35% of rooms revenue at a 65% departmental cost ratio. Variable rooms cost \$55 per occupied room. Undistributed \$220,000 per month fixed plus 6% of revenue. Management fee 3% of total revenue; distribution costs 8% of rooms revenue. FF&E reserve 4% of total revenue, deposited monthly with the lender. **Property tax \$540,000 paid in January; insurance \$720,000 paid at the June renewal** (cash timing, not accrual).

##### Solution

**Step 1: the year.** Total revenue \$13,246,870 (rooms \$9,812,496); occupancy 65.96%; ADR \$254.74; GOP margin 41.2%. NOI \$2,488,834. Monthly debt service \$151,789; annual \$1,821,473. **DSCR 1.366x**; debt yield 11.85%. Cash flow after debt service +\$667,361. On annual figures the resort looks comfortable.

**Step 2: the months.** Cash flow after debt service (\$):

| Jan | Feb | Mar | Apr | May | Jun |
|---:|---:|---:|---:|---:|---:|
| −728,353 | −135,705 | 287,531 | 265,977 | 356,605 | −130,849 |
| **Jul** | **Aug** | **Sep** | **Oct** | **Nov** | **Dec** |
| 754,264 | 492,912 | −47,769 | −99,659 | −211,047 | −136,548 |

Seven of twelve months are negative. June is negative in the second-best revenue month because the insurance premium is paid then. January carries the tax bill on top of the weakest revenue.

**Step 3: the working-capital reserve without a trap.** Cumulative cash peaks at the end of August and falls through February. The September-to-February deficit is $47{,}769 + 99{,}659 + 211{,}047 + 136{,}548 + 728{,}353 + 135{,}705 = \$1{,}359{,}081$. That is the largest peak-to-trough fall in cumulative cash (§11.4.11), and the reserve the fund needs if it keeps the March–August surplus (\$2,026,442) in the property account.

**Step 4: the stress and the trap.** Cut ADR 5% in every month (occupancy unchanged). NOI falls to \$2,063,462 and **DSCR to 1.133x**, below the 1.30x trigger. Cash management begins. Now the peak-season surplus goes to the lender's account, and every negative month must be funded with new equity. The equity requirement is the sum of all negative months: **\$1,657,826**, against a peak-to-trough requirement of \$1,467,050 under the same stress without a trap. Under the trap the fund also loses access to the annual surplus (\$241,989) until the trigger is cured.

| | Base | ADR −5%, no trap | ADR −5%, with trap |
|---|---:|---:|---:|
| NOI | 2,488,834 | 2,063,462 | 2,063,462 |
| DSCR | 1.366 | 1.133 | 1.133 |
| Working capital needed | 1,359,081 | 1,467,050 | 1,657,826 |
| Annual cash to owner | 667,361 | 241,989 | 0 (trapped) |

**Check.** Base-case reserve: the sum of September through February cash flows equals the peak-to-trough figure computed by the running-maximum algorithm in `case11_5`. ✓

##### Decision

**Fund a working-capital reserve of \$1.7 million at closing** (the trapped-stress requirement, rounded up), or negotiate the loan so that it is not needed: a **seasonality reserve** in which the lender sweeps a fixed amount from March–August cash into a reserve that is released to pay operating shortfalls from September to February, with the cash-management test applied to a trailing-12 figure that excludes the reserve deposits. Negotiate also for monthly insurance installments (premium financing) and to pay property tax in installments where the jurisdiction allows, which reduces the January and June spikes.

**Decision consequence.** An annual DSCR of 1.37x hides a business that runs out of cash every winter. A buyer who underwrites annually and holds no reserve will be writing capital calls in its first January, and a 5% rate decline converts the lender's protective provision into a liquidity squeeze precisely when the owner needs the summer cash. The \$1.7 million is about 2.5 years of the base case's annual cash flow to the owner (\$667,361), which is why seasonal assets support less leverage than their annual DSCR suggests.

**What would change the decision.** A lender willing to test DSCR on a trailing-12 basis with a seasonality reserve. A group or wholesale contract that fills the shoulder months. A revolving credit line from the sponsor, which substitutes contingent capital for a funded reserve, at the risk that the line is unavailable in the same downturn that triggers the trap.

**Reproduce.** `tests/test_ch11_examples.py::test_case_11_5`

---

#### Case 11.6 — The labor-cost shock and break-even occupancy

##### Situation

A city adopts a hospitality minimum-wage ordinance. For a 150-room select-service hotel you own, the loaded housekeeping wage rises from \$18.00 to \$21.60 an hour (+20%), and fixed labor (front desk, maintenance, management) rises 15% to preserve pay differentials. The lender asks for an updated break-even analysis; the investment committee asks what operational response restores NOI.

##### Data (Exhibit 11.6-1)

| Item | Before | After |
|---|---:|---:|
| Rooms / occupancy / ADR | 150 / 72.0% / \$128.00 | unchanged |
| Other revenue (% of rooms revenue) | 3% | 3% |
| Housekeeping hours per occupied room | 0.50 | 0.50 |
| Housekeeping loaded wage | \$18.00 | \$21.60 |
| Non-labor variable cost per occupied room | \$16.00 | \$16.00 |
| Fixed labor | \$750,000 | \$862,500 |
| Fixed non-labor (undistributed, tax, insurance) | \$850,000 | \$850,000 |
| Revenue-variable costs (fees, card, commissions, reserve) | 21% of total revenue | 21% |
| Loan | \$12.0m, 7.25%, 25-year amortization | |

##### Solution

**Step 1: contribution and NOI.** Variable cost per occupied room: before $16 + 0.5 \times 18 = \$25.00$; after $16 + 0.5 \times 21.60 = \$26.80$. Contribution per occupied room $= 128 \times 1.03 \times (1 - 0.21) - CPOR$: before \$79.15, after \$77.35. Rooms sold $= 150 \times 365 \times 0.72 = 39{,}420$.

NOI before $= 39{,}420 \times 79.15 - 1{,}600{,}000 = \$1{,}520{,}235$. After $= 39{,}420 \times 77.35 - 1{,}712{,}500 = \$1{,}336{,}779$. Change **−\$183,456** (−12.1%): \$70,956 from variable labor and \$112,500 from fixed labor.

Debt service $= \$1{,}040{,}842$. DSCR falls from **1.461x to 1.284x**.

**Step 2: break-even occupancy** (`sdesk.hotel.breakeven_occupancy`, equation 11.2):

| | Before | After |
|---|---:|---:|
| Before debt service | 36.92% | 40.44% |
| After debt service | 60.94% | 65.01% |
| Cushion to actual 72% (after debt) | 11.1 points | 7.0 points |

**Step 3: the stress.** Combine the shock with a recession: occupancy −8 points to 64% and ADR −6% to \$120.32. NOI falls to \$778,998 and **DSCR to 0.748x**. Break-even occupancy after debt rises to 70.73%, above the stressed occupancy of 64%.

**Step 4: the responses.** To restore NOI at 72% occupancy through rate alone, ADR must rise to \$133.72, **+4.47%**. To offset only the variable-wage effect through productivity, housekeeping time must fall from 30 to **25.0 minutes** per occupied room, so that $0.4167 \times 21.60 = \$9.00$, the old labor cost per room. The fixed-labor increase (\$112,500) needs a separate response: staffing model, cross-training, or technology (self-service check-in, mobile key).

Value effect at a 9.5% cap if nothing is done: $183{,}456/0.095 = \$1{,}931{,}116$.

**Check.** At the "before" break-even occupancy after debt, $0.6094 \times 150 \times 365 \times 79.15 \approx 2{,}640{,}842 = 1{,}600{,}000 + 1{,}040{,}842$ (exact at full precision). ✓

##### Decision

**Treat the shock as permanent and re-engineer the labor model before relying on rate.** A 4.5% ADR increase that the comp set is not also taking will cost share (Example 11.1); every competitor in the city faces the same ordinance, which makes some pass-through plausible, but the pass-through should be measured in the STR data over the following two quarters rather than assumed. Housekeeping productivity (stayover cleaning on request, room-attendant routing, linen programs) can recover most of the variable effect. Report to the lender the post-shock DSCR and the 7-point cushion, and agree in advance what happens in a recession, because the stressed DSCR is below 1.0x.

**Decision consequence.** A 20% wage increase on one job category cost 12% of NOI and \$1.9 million of value, and cut the break-even cushion from 11 points to 7. The broader lesson is that labor is a fixed cost in the short run and a variable cost in the long run only if management redesigns the work. In underwriting, apply labor inflation separately to fixed and variable labor; a single "expense growth" assumption misses the operating leverage.

**What would change the decision.** Evidence that the comp set has already raised rates (pass-through is market-wide). A franchise standard that prevents the stayover-cleaning change. A scheduled loan maturity within the stress window, which would make the DSCR the binding issue rather than the value.

**Reproduce.** `tests/test_ch11_examples.py::test_case_11_6`

---

#### Case 11.7 — A BOV under stress, with a going-concern allocation

##### Situation

A special servicer has taken title to a 210-room full-service hotel and asks your brokerage for a BOV to set a list price. The hotel is recovering from a demand shock and a period of underinvestment. The servicer's asset manager also asks how the sale price should be allocated among real property, FF&E and intangibles, because a buyer's counsel has asked for an allocation in the purchase agreement.

##### Data (Exhibit 11.7-1)

| Item | Value |
|---|---|
| T-12 NOI (after 4% reserve) | \$2,100,000 |
| Prior peak NOI | \$3,600,000 |
| Forecast NOI, years 1–5 | \$2,450,000; \$2,950,000; \$3,300,000; \$3,399,000; \$3,500,970 |
| Year-6 NOI (for reversion) | \$3,606,000 |
| Deferred capital, year 1 (beyond the reserve) | \$1,500,000 |
| Discount rate / exit cap / selling costs | 11.0% / 9.0% / 2.5% |
| Direct cap on stabilized NOI | 9.5% |
| Scenarios (NOI multiple on the forecast; exit cap) | Downside 0.85, 9.75% (p = 0.30); Base 1.00, 9.0% (p = 0.50); Upside 1.06, 8.5% (p = 0.20) |
| FF&E, depreciated replacement cost | \$13,000/key |
| Identified intangibles (assembled workforce, flag and booking pace, start-up costs) | \$1,400,000 |
| Land share of real property | 15% |
| Property tax rate on real property (this jurisdiction taxes real property and tangible personal property, not intangibles) | 2.4% of value |
| Income tax rate / discount rate for tax shields | 25% / 8% |

##### Solution

**Step 1: base DCF.** Year-1 cash flow is NOI less the deferred capital: \$950,000. Reversion at end of year 5 on year-6 NOI: $3{,}606{,}000/0.09 = \$40{,}066{,}667$ gross, \$39,065,000 net of 2.5% costs (`sdesk.cre.dcf_value`). Present value at 11%: **\$33,162,932**. The reversion is 69.9% of value: most of the value is in the recovery, not the next five years of income.

**Step 2: scenario weighting.**

| Scenario | p | DCF value |
|---|---:|---:|
| Downside | 0.30 | 26,469,966 |
| Base | 0.50 | 33,162,932 |
| Upside | 0.20 | 36,679,328 |
| **Probability-weighted** | | **31,858,321** |

**Step 3: reconcile with direct capitalization.** Stabilized NOI (year 3) \$3,300,000 at 9.5% = \$34,736,842. Less the PV of the income shortfall in years 1–2, $(3{,}300{,}000 - 2{,}450{,}000)/1.11 + (3{,}300{,}000 - 2{,}950{,}000)/1.11^2 = \$1{,}049{,}834$, and the PV of deferred capital, \$1,351,351, gives **\$32,335,657**. Two reference points bound the range: the T-12 capitalized at 9.5% (\$22,105,263) understates value because it ignores a recovery that is already under way; the prior peak at 8.5% (\$42,352,941) overstates it because it assumes the recovery has finished and the capital has been spent.

**Step 4: the BOV.** Most probable price **\$31.9 million** (the probability-weighted value, rounded), with a range of \$26.5–36.7 million across scenarios. Recommended list price about \$33–34 million, supported by the base DCF and the direct-cap reconciliation. Per key: \$151,905 at \$31.9 million.

**Step 5: the going-concern allocation.** Total assets of the business (TAB) \$31,900,000. FF&E $= 210 \times 13{,}000 = \$2{,}730{,}000$.

| | A: fees deducted, no separate intangible | B: business-enterprise allocation |
|---|---:|---:|
| Real property | 29,170,000 | 27,770,000 |
| FF&E | 2,730,000 | 2,730,000 |
| Intangibles | 0 | 1,400,000 |
| Land (15% of real property) | 4,375,500 | 4,165,500 |
| Building | 24,794,500 | 23,604,500 |
| Property tax on real property (2.4%) | 700,080 | 666,480 |
| Year-1 tax depreciation (building 39 yrs, FF&E 7 yrs, intangibles 15 yrs, straight-line) | 1,025,756 | 1,088,577 |

Method A rests on the argument that deducting market management and franchise fees from income removes the return to the business, so no further intangible deduction is warranted. Method B identifies specific intangibles and values them. The difference in property tax is \$33,600 a year, worth **\$353,684** at the 9.5% cap. The difference in income-tax deductions is $1{,}400{,}000/15 - 1{,}400{,}000 \times 0.85/39 = \$62{,}821$ a year for 15 years, worth $0.25 \times 62{,}821 \times a_{\overline{15}|8\%} = \$134{,}428$ in present value [HYPOTHESIS: simplified straight-line recovery; actual recovery periods and conventions must be confirmed with tax counsel]. For an asset acquisition of a trade or business, federal reporting allocates consideration among asset classes using the residual method, with goodwill and going-concern value in the last class [FACT; IRS Instructions for Form 8594, ch11-S09]. The 15-year recovery of §197 intangibles is described in IRS guidance as summarized in secondary sources [ch11-S09, VERIFIED-SECONDARY]; the 39-year and 7-year recovery periods used above are *(verification pending)*.

**Check.** DCF base value recomputed year by year, $\sum_{t=1}^{5} CF_t/1.11^t + 39{,}065{,}000/1.11^5$, matches the library result. ✓

##### Decision

**Publish a BOV of \$31.9 million most probable, \$26.5–36.7 million range, list at about \$33.5 million**, with the scenario weights, the recovery path and the deferred capital shown. Recommend that the servicer **not** state an allocation in the marketing materials, but agree one with the buyer before signing, consistent with an appraisal that documents the intangible components. The buyer will prefer Method B (lower property tax, faster depreciation); the servicer is largely indifferent because it is exiting, but the allocation must be defensible, because the assessor will see the deed price and may challenge any reduction.

**Decision consequence.** Allocation is worth about \$0.35 million in capitalized property-tax value and \$0.13 million in income-tax present value on a \$31.9 million hotel: about 1.5% of value. It is not a pricing lever for the seller, but it is a negotiating item the buyer values. The BOV's larger lesson is that under stress neither the T-12 (\$22.1 million) nor the peak (\$42.4 million) is a value. The defensible number is a probability-weighted recovery path, and the BOV should show the weights so that the servicer can disagree with them explicitly.

**What would change the decision.** A different jurisdiction (one that taxes intangibles, or does not tax personal property) changes the allocation economics. A stronger buyer pool (more 1031 or owner-operator demand) would justify listing nearer the base DCF. A franchise termination notice would reduce the base-case NOI and add a PIP, moving value toward the downside.

**Reproduce.** `tests/test_ch11_examples.py::test_case_11_7`

---

#### Case 11.8 — Disposition timing: sell now or after the PIP?

##### Situation

A private owner holds a 130-room select-service hotel. The brand has issued a PIP of \$2,340,000 (\$18,000 per key), due within 18 months or on any sale. In-place NOI is \$1,300,000 and slipping as the product ages. A renovated hotel would earn a stabilized NOI of \$1,550,000. The owner can sell now to a buyer who will price the PIP, or renovate and sell in two years.

##### Data (Exhibit 11.8-1)

| Item | Value |
|---|---|
| Stabilized NOI (renovated) / cap rate | \$1,550,000 / 9.0% |
| Buyer's pricing of the PIP | contingency 15%; displacement \$260,000; carry and soft costs \$150,000; required profit 15% on PIP capital |
| Seller's costs | 2.5% of price |
| Owner's discount rate (unlevered) | 11% |
| Owner's hold path | Year 1: NOI \$1,300,000 less \$260,000 displacement, PIP paid (treated as year-end); year 2: stabilized NOI; sale at end of year 2 on year-3 NOI (\$1,550,000 × 1.03) less 2.5% |
| Hold scenarios | Good: exit cap 8.75%, no overrun (p = 0.35). Base: 9.0%, 8% overrun (p = 0.45). Bad: 9.75%, 25% overrun (p = 0.20) |

##### Solution

**Step 1: sell now** (`sdesk.hotel.pip_adjusted_price`). Stabilized value $= 1{,}550{,}000/0.09 = \$17{,}222{,}222$. PIP all-in $= 2{,}340{,}000 \times 1.15 = \$2{,}691{,}000$. Required profit $= 0.15 \times 2{,}691{,}000 = \$403{,}650$.

$$P = 17{,}222{,}222 - 2{,}691{,}000 - 260{,}000 - 150{,}000 - 403{,}650 = \$13{,}717{,}572.$$

Net to the owner after 2.5% costs: **\$13,374,633**. The price is a 9.48% cap on in-place NOI: the buyer will describe it as "a 9.5 cap", and the owner will hear "below a 9 cap market". Both are describing the deduction for the PIP.

**Step 2: renovate and sell.**

| Scenario | p | PIP paid | Year-1 cash | Net sale (end of year 2) | PV at 11% |
|---|---:|---:|---:|---:|---:|
| Good | 0.35 | 2,340,000 | −1,300,000 | 17,789,571 | 14,525,259 |
| Base | 0.45 | 2,527,200 | −1,487,200 | 17,295,417 | 13,955,543 |
| Bad | 0.20 | 2,925,000 | −1,885,000 | 15,965,000 | 12,517,369 |
| **Expected** | | | | | **13,867,309** |

Base-case PV in full: $(1{,}300{,}000 - 260{,}000 - 2{,}527{,}200)/1.11 + (1{,}550{,}000 + 17{,}295{,}417)/1.11^2 = \$13{,}955{,}543$.

**Step 3: compare.** Expected advantage of renovating: $13{,}867{,}309 - 13{,}374{,}633 = \$492{,}676$, about 3.7% of the sale-now proceeds. In the bad scenario the owner is \$857,264 worse off than selling now. Holding the base-case 8% overrun, the exit cap rate at which renovating and selling now are equal is **9.39%**: 39 bp above the assumed market.

**Check.** The buyer's total deduction, $17{,}222{,}222 - 13{,}717{,}572 = \$3{,}504{,}650$, equals PIP all-in + displacement + carry + required profit $= 2{,}691{,}000 + 260{,}000 + 150{,}000 + 403{,}650$. ✓

##### Decision

**Renovate and sell only if three conditions hold:** the owner can fund about \$2.5–2.9 million of PIP cost without forced selling in the bad case; the owner can accept a one-in-five chance of ending \$0.86 million worse off; and the owner's view of the exit cap two years out is comfortably inside 9.39%. Otherwise **sell now**, and use the analysis to negotiate the buyer's deductions: a 15% contingency and 15% required profit on a PIP whose scope is fixed by a letter are negotiable, and every five points of either is worth about \$135,000 of price.

**Decision consequence.** The "PIP profit" the buyer charges (\$403,650 plus the contingency spread) is the price of transferring execution and market risk. An owner who renovates captures it in expectation but bears both risks, plus two years of exposure to exit cap rates. This is a speculation on the owner's own execution and on the cap rate, not a free gain. The 39 bp break-even is the number to put in front of the owner: a modest widening in cap rates erases the advantage.

**What would change the decision.** A firm fixed-price construction bid (cuts the overrun tail). Evidence that the buyer pool is thin for unrenovated hotels (raises the buyer's discount, favoring renovation). A loan maturity inside the renovation period (forces a sale at the worst moment, favoring selling now). A lender willing to fund 75% of the PIP (changes the owner's liquidity condition, but not the risk).

**Reproduce.** `tests/test_ch11_examples.py::test_case_11_8`

---

### 11.7 CRE application: the hotel inside a real estate portfolio

The eight cases of §11.6 are the core CRE application of this chapter. They are summarized here, together with the portfolio-level lesson they share.

| Case | Situation | Tool | Decision |
|---|---|---|---|
| 11.1 | Select-service: RevPAR +6.05%, NOI −17.1% | Flow-through bridge | Underwrite forward NOI; fix channel mix; do not capitalize the T-12 |
| 11.2 | Full-service group request on peak nights | Displacement | Accept at contract rate only with cutoff protection; counter with alternate dates |
| 11.3 | Franchise expiring: renew, convert, or go independent | Brand economics | Renew; independence needs an RGI of 103 to compete |
| 11.4 | Manager proposes lower base, higher incentive fee | Option value of fees | Approximately neutral in expectation; accept only with a cap and performance test |
| 11.5 | Seasonal resort with a DSCR cash trap | Monthly cash and reserves | Fund a \$1.47m working-capital reserve or negotiate a seasonality reserve |
| 11.6 | 20% housekeeping wage shock | Break-even occupancy | Re-engineer labor; ADR +4.5% restores NOI; 5 fewer housekeeping minutes per room offset the variable wage effect |
| 11.7 | Special-servicer BOV under stress | DCF, scenario weights, TAB allocation | \$31.9m most probable value; allocation is worth \$0.35m in tax value |
| 11.8 | Sell now or after the PIP | PIP-adjusted price versus hold | Hold and renovate only if the owner can bear a 9.39% exit-cap break-even |

**The portfolio lesson.** Inside a CRE portfolio a hotel is a different asset class with the same physical form. A 20% revenue shock that costs an office owner nothing until leases roll costs a hotel owner most of its NOI within a quarter. A portfolio manager who allocates to hotels at the same leverage, liquidity reserve and hold-period assumptions as leased property is not diversifying. That manager is adding a high-beta position funded as if it were low-beta. The practical rules that follow from the chapter are:

1. **Lower leverage, more liquidity.** Size hotel debt on trailing NCF and a stressed RevPAR (Example 11.4), and hold a working-capital reserve sized from monthly, not annual, cash flow (Case 11.5).
2. **Underwrite capital as an operating cost.** The 4% reserve funds routine replacement. PIPs arrive on the brand's schedule and must be priced into every bid and every hold/sell decision (Case 11.8, Case D).
3. **Track share, not just level.** RGI is the operating metric that separates management skill from the market (Example 11.1).
4. **Read the contracts.** Franchise and management agreements are senior claims on revenue with termination costs. They can make a hotel unsellable to the best buyer (Cases 11.3, 11.4, D).

---
### 11.8 Hotel valuation practice: cap rates, BOVs, transaction costs, timing and anchoring

This section collects the practitioner judgments that sit between the equations and the cases.

**Hotel cap rates.** A hotel cap rate is a ratio to a named line after a named reserve, observed at a named point in the cycle. Three adjustments separate a usable comparable from a misleading one. (1) *Line:* T-12 NOI, forward NOI and "stabilized" NOI give different rates on the same price. A trade at 7.5% on forward NOI may be 6.5% on a trailing year that included a renovation. (2) *Encumbrance:* a sale that required the buyer to fund a PIP was priced net of it. Its cap rate on in-place NOI is high because the buyer deducted the PIP, not because the market's required return was high (Case A, Mode D question 2). (3) *Business mix:* full-service, resort and select-service hotels carry different volatility and capital intensity, and their cap rates are not interchangeable. This book does not quote "market" hotel cap rates as facts; every cap rate in an example is [HYPOTHESIS]. In practice, rates should be taken from documented comparable sales with these three adjustments shown.

**Valuation under stress.** When the T-12 is depressed (a recession, a renovation year, a lost contract), capitalizing it understates value, and capitalizing pre-shock NOI overstates it. The defensible approach is a DCF with an explicit recovery path, scenario weights, and a reversion on forward NOI (Case 11.7). Reconcile it to a direct capitalization of stabilized NOI less the present value of the income shortfall and capital needed to reach stabilization. Report the range and the probability weights, not only the point.

**Broker opinions of value.** A BOV is a marketing and pricing document, not an appraisal, and it should say so. A BOV that will survive a buyer's diligence contains: the T-12 and budget on a USALI basis with every normalization shown; the STR trend (36 months of RGI, not a single year); the fee stack and contract terms (franchise expiry, PIP status, management termination rights); a PIP estimate or letter; property-tax reassessment on sale; a value range from at least two methods; the buyer pool and the likely financing; and a recommended list price, an expected price and a marketing timeline. The opening problem fails on four of these.

**Transaction costs.** Hotel transactions carry the usual costs (broker fee, title, legal, lender fees, transfer taxes where levied) plus hotel-specific items: franchise application and transfer fees, PIP design costs, liquor-license transfer, the cost of re-bidding management, and the working capital and inventory (linen, supplies, F&B stock) that change hands at closing. In this chapter's cases, buyer costs are 2% and seller costs 2.5–3% of price [HYPOTHESIS]. For a short hold the round trip consumes a large share of the expected return (Chapter 1, error 9).

**Disposition timing.** The question "sell now or later?" is a comparison of two risky cash-flow streams, not of two prices. Selling before a PIP hands the renovation risk and the renovation profit to the buyer at a discount (equation 11.3). Selling after it captures the profit but bears overruns, displacement and the risk that the exit cap rate moves while the work is under way. Case 11.8 computes the trade-off and the break-even exit cap rate.

**Seller anchoring.** Owners anchor on cost, on peak NOI, on a neighbor's sale, or on EBITDA capitalized at an NOI cap rate (Case A; the opening problem). The analyst's job is to replace the anchor with a bridge whose every line is a verifiable fact. The owner's practical floor is usually set by the loan balance and selling costs, not by the anchor.

**Normalizing a hotel P&L.** Beyond the general normalization in Case A, hotel statements carry recurring traps: management fees omitted by owner-operators; franchise fees understated because loyalty, reservation and technology charges are booked in rooms expense or A&G; FF&E reserves omitted or below the franchise or loan requirement; capital items (PTAC units, roofs, mattresses) expensed through repairs and maintenance; one-off revenue (a pipeline crew, a storm-recovery block, a film production); payroll that excludes owner-family labor; and property tax on an assessment that will reset on sale. Each item should appear as a line in a bridge from the owner's statement to the buyer's NOI.

**Reading an STR-style report.** A competitive-set report gives the subject's and the set's occupancy, ADR and RevPAR by month and by day of week, and the three indices. Its strengths are that it is independent of the owner and that the indices strip out the market. Its limits: it reports revenue, not profit, so it cannot show the commission cost of buying occupancy (Case 11.1); a set is chosen by the subject's owner within the provider's rules and can be stale; segmentation reports depend on how the hotel codes its business; and small sets can be dominated by one hotel's renovation or closure. Use 36 months of data, look at the trend in RGI rather than its level, and check whether the set changed during the period.

**Hotel lending in practice.** Beyond the sizing constraints in Example 11.4, hotel loan documents typically include [HYPOTHESIS: terms vary by lender and cycle]:

* a **franchise comfort letter**, under which the brand agrees to give the lender notice and cure rights before terminating the flag, and to let a foreclosing lender keep the flag for a period;
* a monthly **FF&E reserve** escrow, usually 4% of revenue or the franchise requirement if higher;
* a **PIP reserve**, either funded at closing from loan proceeds or equity, or held back and advanced against completed work (Case D compares the two);
* **cash management** triggered by DSCR or debt yield, sometimes with a **seasonality reserve** for hotels with uneven monthly cash flow (Case 11.5);
* **extension tests** on floating-rate loans, typically a minimum debt yield on trailing NCF, which can force a paydown at the moment the borrower can least afford it;
* events of default tied to the hotel business: loss of the flag, termination of the management agreement without lender approval, or loss of a liquor license.

These provisions transfer liquidity risk from the lender to the owner. They do not show up in a DSCR or LTV, so an equity investor must read them and price them.

---

### 11.9 When the relationship fails

1. **RevPAR is not profit.** RevPAR can rise while NOI falls when the growth is bought through commissions, discounting to groups with low ancillary spend, or occupancy that drives variable labor (Case 11.1).
2. **Flow-through is not a constant.** Rate-led and occupancy-led growth flow through differently (Example 11.2). Flow-through on the way down is usually worse than on the way up, because managers cut fixed labor with a lag and contracts (union scheduling minimums, service standards) slow the cuts.
3. **Penetration indices depend on the comp set.** An owner who chooses the comp set can manufacture an RGI above 100. STR-style rules limit how a set can be built, but a set built three years ago may now include a hotel that has been repositioned or closed. Ask who chose the comp set and when it last changed.
4. **Break-even occupancy assumes ADR is fixed.** In downturns ADR falls with occupancy. In 2020 U.S. ADR fell about 21% for the year (§11.10), so a break-even computed at the old ADR was badly optimistic.
5. **Displacement depends on a forecast.** If transient demand comes in above forecast, the "profitable" group destroys value (Case 11.2's high-demand scenario). If it comes in below, rejecting the group leaves rooms empty.
6. **Cap rates and the reserve.** A 4% reserve is a convention, not a fact. A full-service hotel with an aging central plant may need far more. Capitalizing NOI after a 4% reserve when the true capital need is 6% overvalues the asset.
7. **The brand is not a constant premium.** Brand premiums (RGI above 100) vary by market, by segment and over time as distribution shifts between brand channels and online travel agencies. A brand that commanded a 10-point RGI premium in one decade may not in the next [SPECULATION about any specific brand; HYPOTHESIS in Case 11.3].
8. **Going-concern methods disagree.** Two competent appraisers can allocate the same total value differently between real property and intangibles (Case 11.7). Neither allocation is a market observation.
9. **Debt covenants bite before value does.** A cash trap can starve a seasonal hotel of working capital while its annual DSCR still looks acceptable (Case 11.5).

---

### 11.10 Historical episode: U.S. hotels after 11 September 2001 and in 2020

This section uses published STR figures, as reported in contemporaneous press coverage, together with BLS employment data and Trepp CMBS delinquency data. Verification status is shown in `references/sources_ch11.md`. Figures are national averages. Individual hotels, markets and segments diverged widely.

#### Date and environment

**2001.** The U.S. expansion that began in March 1991 ended in March 2001 [FACT; NBER business-cycle chronology, ch11-S06]. Hotel demand was already weakening before September. In August 2001, STR reported U.S. occupancy of 67.7% and RevPAR down 4.4% year over year to \$57.08 [FACT; STR figures as reported in trade press, ch11-S02, VERIFIED-SECONDARY]. The NBER later dated the trough to November 2001 *(verification pending)*.

**2020.** The NBER dated a business-cycle peak in February 2020 and a trough in April 2020, a two-month recession [FACT; NBER, ch11-S06]. In 2019 U.S. hotels had posted record nominal ADR and RevPAR: occupancy 66.1%, ADR \$131.21, RevPAR \$86.76 [FACT; STR via trade press, ch11-S03, VERIFIED-SECONDARY].

#### What happened

**September 2001.** STR reported U.S. occupancy down 10.6 percentage points to 55.9%, and RevPAR down 23.4% to \$44.30, for September 2001 [FACT; ch11-S01, VERIFIED-SECONDARY]. The implied prior-year figures are occupancy $0.559 + 0.106 = 66.5\%$ and RevPAR $44.30/0.766 = \$57.83$. The implied ADR fell from $57.83/0.665 = \$86.97$ to $44.30/0.559 = \$79.25$, a decline of 8.9% [INFERENCE: arithmetic on the reported figures]. Note the two ways to state the occupancy loss: −10.6 *points*, or −15.9% *in percentage terms*. Press releases mix them, so state which one you mean. A full-year 2001 U.S. figure is not used here *(verification pending)*.

**April 2020.** STR reported U.S. occupancy of 24.5%, ADR of \$73.23 and RevPAR of \$17.93, with RevPAR down 79.9% from April 2019. It described occupancy and RevPAR as the lowest monthly levels in its records [FACT; ch11-S04, VERIFIED-SECONDARY]. The identity holds: $0.245 \times 73.23 = \$17.94$, against the reported \$17.93 (rounding of the reported occupancy).

The Bureau of Labor Statistics reported that employment in accommodation fell by 839,000 in April 2020, within a 7.7 million decline in leisure and hospitality [FACT; BLS Employment Situation, 8 May 2020, ch11-S07, VERIFIED-PRIMARY for the release; later revisions not used].

**Full-year 2020.** STR reported occupancy of 44.0% (−33.3%), ADR of \$103.25 (−21.3%) and RevPAR of \$45.48 (−47.5%). It called 2020 the worst year on record for U.S. hotels and said the industry was expected to show close to zero profit for the year [FACT; ch11-S03, VERIFIED-SECONDARY]. Computing the changes from the published 2019 and 2020 levels gives −33.4%, −21.3% and −47.6%. The small differences most likely arise because percentage changes are computed on a matched sample of reporting hotels and the levels are rounded [INFERENCE; the methodology note should be checked]. The identity $0.440 \times 103.25 = \$45.43$ versus the reported \$45.48 shows the same rounding. These are not errors, but a model that mixes levels and reported changes will not reconcile to the cent. Cite one or the other.

**Financing.** Trepp reported that the CMBS delinquency rate for lodging loans reached 24.30% in June 2020, an all-time high for the sector in its data [FACT; Trepp via trade press, ch11-S08, VERIFIED-SECONDARY].

**Recovery.** For 2021 STR reported occupancy of 57.6%, ADR of \$124.67 and RevPAR of \$71.87, which it described as 83.2% of the 2019 comparable [FACT; ch11-S05, VERIFIED-SECONDARY]. From the published levels, $71.87/86.76 = 82.8\%$, again a sample-basis difference.

#### What was knowable then, and what was not

* **Knowable:** the operating leverage of hotels; the mechanics of revenue-based fees; that hotel loans carry cash-management triggers; that demand in 2001 was already falling before September; that a pandemic stops travel.
* **Not knowable:** the date of either shock, the depth (STR described April 2020 occupancy and RevPAR as the lowest in its U.S. records, so no prior month offered a reference point [INFERENCE]), or the duration and form of policy support.

#### Participants, leverage and the strategies available

[INFERENCE throughout this subsection: it describes structural positions implied by the contracts and loans discussed in this chapter, not documented aggregate data.] Owners held the residual claim, behind franchise and management fees and lenders. Owners financed with floating-rate or CMBS debt faced cash-management triggers within a quarter of the shock, which converted an income problem into a liquidity problem. Operators had incentives tied to revenue (base fees) and to profit above owner priorities (incentive fees, which disappeared). Brands collected revenue-based fees that fell with revenue but did not bear fixed costs. The strategies available to an owner were the same in both episodes: cut fixed labor quickly, decide whether to defend rate or occupancy, draw reserves and credit lines, negotiate forbearance or covenant relief early, and defer discretionary capital, including PIP deadlines where the brand allowed it. Capital that was unlevered, or that held a large working-capital reserve, could also act as a buyer of distressed hotels or loans; Chapter 12 develops that side.

#### Interpretations

**Operating leverage, quantified.** Take a stylized hotel with a 38% GOP margin in 2019 whose costs are 55% fixed in the short run [HYPOTHESIS]. Cut revenue 47.5%. Variable costs fall in proportion; fixed costs do not. Per \$100 of 2019 revenue: costs \$62, of which \$34.10 fixed and \$27.90 variable (27.9% of revenue). 2020 revenue \$52.50; GOP $= 52.50 \times (1 - 0.279) - 34.10 = \$3.75$, a **90% decline** in GOP from \$38.00. Fees, property tax and insurance then take the remaining GOP and more. That is consistent with STR's statement that the industry would show close to zero profit for the year [INFERENCE: a stylized calculation consistent with the reported outcome; it does not establish actual industry cost shares].

**Rate versus occupancy.** In September 2001 occupancy fell 15.9% and ADR 8.9%. In 2020 occupancy fell about a third and ADR about a fifth. In both shocks most of the RevPAR loss came through occupancy, and ADR followed. A break-even occupancy computed at pre-shock ADR (§11.4.6) would have understated the break-even in both episodes [INFERENCE].

**Competing explanations of 2020 survival.** Some hotels survived on reserves, some on lender forbearance and some on government programs. Their relative importance is not settled here *(verification pending: sector-level data on forbearance and program use)*.

#### What the episode does and does not establish

It establishes that national monthly hotel RevPAR can fall by about a quarter year over year (September 2001) and by about four-fifths (April 2020), that profit falls far more than revenue, and that hotel loan performance deteriorates within months. It does **not** establish the probability of another shock of either size, that recoveries will follow the 2021 path, or that any particular hotel would have experienced the national average. A stress test that uses a RevPAR decline of about a quarter for a month or two is grounded in 2001. One that uses −50% for a year is grounded in 2020. One that uses neither has no historical anchor.

---

### 11.11 Decision exercise: the Monday BOV, rebuilt

Return to the opening hotel. Apply Exhibit 11.2's cost structure to its T-12 occupancy (71.0%) and ADR (\$158.50), all other assumptions unchanged:

| Line | \$ |
|---|---:|
| Total revenue | 5,693,033 |
| GOP | 2,621,173 |
| EBITDA | 1,456,859 |
| NOI after 4% reserve | 1,229,138 |
| Owner's claim: EBITDA ÷ 9% | 16,187,325 |
| NOI ÷ 9% (stabilized, unencumbered) | 13,657,088 |
| PIP at \$14,000/key + 10% contingency | 2,032,800 |
| PIP-adjusted price (displacement \$90,000, carry \$60,000, 15% required profit = \$304,920) | **11,169,368** |
| NOI from restoring the prior RGI of 105.0 (rate-led, 75.19% flow-through) | 92,647 |
| Value of that NOI at 9% | 1,029,406 |

Prepare a BOV memo (template: `desk/investment_memos/decision_record_template.md`) that answers:

1. **Value.** Your value range and the most probable price, as-is with the PIP, and the line and reserve each cap rate applies to.
2. **The owner's number.** A one-paragraph explanation, for the owner, of why \$16.2 million is not a value. Use the bridge, not adjectives.
3. **Share.** What the RGI decline means for buyers, and what the \$1.03 million "share recovery" upside is worth to a buyer who must earn it.
4. **Timing.** Whether the owner should sell now, or obtain the PIP letter and decide whether to renovate first (use Case 11.8's method).
5. **Abstention.** What information would make you decline to publish a point value by Friday. Saying so is a legitimate output.

**Rubric** (full solution in `problems/solutions/ch11_solutions.md` §Decision exercise). Full credit requires: the EBITDA/NOI error quantified (\$2.53 million, the capitalized reserve); the PIP deducted with contingency and required profit; the RGI decline identified as the main diligence question; a range rather than a point, with the range's width justified; and a recommendation conditioned on the PIP letter. A memo that publishes \$16.2 million, or any figure above \$13.7 million as-is, without a PIP letter, fails. A memo that declines to give a point value until the PIP letter arrives, while giving a conditional range, earns full credit on item 5.

---

### 11.12 Frequent analytical errors

1. **Capitalizing EBITDA at an NOI cap rate.** The error equals the capitalized reserve: 21.0% of value in Example 11.3 and 18.5% in §11.11.
2. **Reading RevPAR growth without RGI.** A hotel can grow RevPAR and lose share (Example 11.1).
3. **One flow-through for all growth.** Use rate-led and occupancy-led flow-through separately (Example 11.2).
4. **Treating the FF&E reserve as covering the PIP.** The reserve funds routine replacement. A PIP is a separate capital claim with its own contingency, displacement and required return (Case D).
5. **Mixing percentage points and percentages.** Occupancy down 10.6 points is down 15.9% (§11.10).
6. **Sizing hotel debt on pro forma NOI.** Lenders use trailing NCF; equity plans built on pro forma loans fail at the term sheet (Example 11.4).
7. **Ignoring the timing of fixed charges.** Annual insurance premiums and property-tax installments create negative months in good years (Case 11.5).
8. **Break-even occupancy at a fixed ADR in a downturn.** ADR falls too (§11.10, Case 11.6).
9. **Accepting a group on rooms revenue alone.** Compare contribution, include banquet profit and channel costs, and stress the transient forecast (Case 11.2).
10. **Assuming the incentive fee is "only paid when the owner does well".** The priority, the ACF definition and the base-fee level decide how the manager's option is struck (Case 11.4).
11. **Allocating going-concern value inconsistently.** Use one allocation for the purchase agreement, the property-tax position and the depreciation schedule, or be prepared to explain the difference to the assessor and the tax authority (Case 11.7).
12. **Doing the PIP "at cost" in a bid.** A buyer who does not earn a return on renovation capital is donating it to the seller (equation 11.3).

---

### 11.13 Connections to other chapters

* **Chapter 1** introduced the hotel bid with an unconfirmed PIP (Example 1.2). Equation 11.3 is the refinement it promised.
* **Chapter 8** builds NOI and operating leverage for all property types. This chapter is the high-leverage case.
* **Chapter 9** develops direct capitalization, DCF and the loaded cap rate used in Case A.
* **Chapter 10** develops LTV, DSCR, debt yield and cash management. Example 11.4 and Cases 11.5 and D apply them.
* **Chapter 12** studies hotel distress, loan sales and CMBS; §11.10's delinquency data are its starting point.
* **Chapter 13** treats hold/sell/refinance decisions as real options. Case 11.8 is a two-period example.
* **Chapter 18** prices options; the incentive fee in Case 11.4 is a call on cash flow.
* **Chapter 20** develops scenario weighting and calibration, used in Cases 11.2, 11.7 and 11.8.
* **Case A** (the overpriced hotel owner) works a full normalization and seller anchoring on cost. **Case D** (the PIP negotiation) works a contested PIP from the buyer's side. **Cases F and J** will extend the hotel material to Treasury comparison and a credit crunch.

---

### 11.14 One-page reference sheet

| Quantity | Formula |
|---|---|
| RevPAR | $\text{Occ} \times ADR = RR/(N D)$ |
| Growth decomposition | $\ln(1+g_{RP}) = \ln(1+g_{Occ}) + \ln(1+g_{ADR})$ |
| Indices | $MPI = 100\,\text{Occ}/\text{Occ}_c$; $ARI = 100\,ADR/ADR_c$; $RGI = MPI \cdot ARI/100$ |
| NOI | $RN[ADR(1+o)(1-v) - c] - F$ |
| Flow-through | $FT_{rate} = 1 - v$; $FT_{occ} = 1 - v - c/[ADR(1+o)]$ |
| Operating leverage (rate-led) | $TR(1-v)/NOI$ |
| EBITDA → NOI | $NOI = EBITDA - f\,TR$; $c_{EBITDA} = c_{NOI}\,EBITDA/NOI$; error $= f\,TR/c_{NOI}$ |
| Break-even occupancy | $(F + DS)/\{[ADR(1+o)(1-v) - c] N D\}$ |
| Incentive fee | $i \max(0, ACF - \pi K)$ |
| Displacement | Accept if group contribution > displaced contribution (incl. shoulder nights) |
| PIP-adjusted price | $V_{stab} - PIP(1+\kappa)(1+\rho) - \text{Displ.} - \text{Carry}$ |
| RevPAR lift for a PIP | $h\,PIP(1+\kappa)/(N D\,FT_{NOI})$ |
| Hotel loan | $\min(\lambda V,\ NOI/(DSCR\cdot K),\ NOI/DY)$ on trailing NCF |
| Seasonal reserve | Largest peak-to-trough fall in cumulative monthly cash flow |
| Going concern | $V_{TAB} = V_{RP} + V_{FF\&E} + V_{BEV}$ |

**Questions to ask of any hotel number:** Which line? After which reserve? Trailing or forward? Rate-led or occupancy-led? Against which comp set, chosen by whom? Before or after the PIP? Whose fees, on what base?

**Rules of thumb (to be tested, not trusted).** One occupancy point is $N \times D \times 0.01$ room-nights (482 a year for 132 rooms). A rate-led RevPAR gain flows through to NOI at about $1 - v$, roughly three-quarters for a select-service hotel; an occupancy-led gain at about half. Capitalizing EBITDA at an NOI cap rate overstates value by the capitalized reserve.

---

### References for this chapter

Sources and verification status: `references/sources_ch11.md`. Hypothetical inputs are not registered.

* STR (CoStar Group). U.S. hotel performance press releases: September 2001 (as reported in *The Caterer*); August 2001 (as reported in trade press); April 2020; full-year 2019, 2020 and 2021. Accessed via search excerpts on 2026-10-19.
* U.S. Bureau of Labor Statistics. *The Employment Situation — April 2020.* News release, 8 May 2020. https://www.bls.gov/news.release/archives/empsit_05082020.pdf
* National Bureau of Economic Research. *US Business Cycle Expansions and Contractions* and the June 2020 Business Cycle Dating Committee announcement. https://www.nber.org/research/business-cycle-dating
* Trepp. CMBS delinquency report, June 2020 (as reported by Nareit and trade press).
* Internal Revenue Service. *Instructions for Form 8594, Asset Acquisition Statement Under Section 1060* (rev. 11/2021). https://www.irs.gov/instructions/i8594
* *Uniform System of Accounts for the Lodging Industry* (USALI). Edition and publisher details *(verification pending)*.


\newpage

## Chapter 12 — CRE Cycles and Distressed Opportunity

> **Status:** Complete (v1.0). Every number in the text, problems, and solutions is reproduced in `tests/test_ch12_examples.py` (library module `models/python/sdesk/x_cre_distress.py`, plus `sdesk.cre.distressed_loan_recovery`). Problems are in `problems/questions/ch12_problems.md` and solutions in `problems/solutions/ch12_solutions.md`. Sources are in `references/sources_ch12.md`. Items marked *(verification pending)* are not presented as established fact. Companion cases: Case E (`cases/hypothetical/case_E_distressed_office/`) and Case G (`cases/hypothetical/case_G_buying_the_debt/`).

### Learning objectives

After this chapter you should be able to:

1. Explain why real estate markets overshoot, using a stock-flow model with a construction lag. Simulate it numerically and identify which parameter, the lag or the developers' response to current rents, drives the size of the overbuild.
2. Separate the four causes of CRE distress: supply shocks, demand destruction (cyclical versus structural), maturity walls, and interest-rate resets. Diagnose a stressed asset as a *liquidity* problem or a *solvency* problem with a refinancing calculation.
3. Price a non-performing loan from resolution scenarios (cure, discounted payoff, deed-in-lieu, contested foreclosure, bankruptcy), compute the maximum bid at a required return, and explain why the mean scenario IRR overstates the return.
4. Quantify foreclosure economics: statutory timelines (verified for Texas non-judicial sales), carrying and legal costs, value drift, and the present-value cost of a judicial process.
5. Describe how CMBS special servicing works, compute an appraisal reduction amount and its effect on servicer advances and on the controlling class, and identify servicer incentives that diverge from bondholders'.
6. Apply the 2006 interagency CRE concentration screens (100% and 300% of total risk-based capital) to a bank balance sheet, and compute the loan sales a bank needs when sale losses reduce the capital in the denominator.
7. Read REIT prices as private-market signals: compute the implied cap rate from enterprise value and the discount to NAV, and say what each does and does not tell you about private values.
8. Compute a basis reset: show how a buyer at a lower basis can charge lower rents and still earn a higher yield, and why this pushes distress onto incumbent owners.
9. Judge "buying through the downturn" claims against the evidence actually available, and recognize when the right answer is to wait.

---

### 12.1 Opening investment problem: three ways into one downturn

You manage a \$250 million opportunistic real estate allocation for a family office. Office and some floating-rate multifamily credits are under stress in your Sun Belt metro. Three things arrive in the same week. All facts are [HYPOTHESIS] — a constructed teaching case.

**A. A non-performing loan.** A regional bank offers a \$40.0 million first-mortgage note on a suburban office property. The borrower missed its maturity date four months ago. The bank's broker says the collateral is "worth about \$31 million as-is" and asks for bids "in the low-to-mid 60s" (cents on the dollar of unpaid principal). The bank is above the regulators' 300% CRE concentration screen and wants the loan off its balance sheet before year-end.

**B. A bank-owned office tower.** A 520,000 sf, 38%-leased CBD tower is offered at about \$100/sf, against a replacement cost the broker puts at \$480/sf. "You are buying at a fifth of replacement cost." (Case E develops this asset.)

**C. A public REIT.** An office REIT with Sun Belt exposure trades at \$42 per share. Your analyst's net asset value, built from private-market cap rates, is about \$55. "The public market is offering private real estate at a 24% discount."

Each opportunity offers a discount. The discounts are measured against different reference points: unpaid principal, replacement cost, and appraised NAV. None of those reference points is a value. The work of this chapter is to replace each reference point with an estimate of what the claim will actually pay, when it will pay, and what can go wrong between now and then. Section 12.10 returns to the allocation.

---

### 12.2 Economic intuition

#### Why real estate cycles overshoot

Space is produced slowly and lasts a long time. An office tower takes three to five years from decision to delivery, and it then stands for fifty years. Developers decide to build on the basis of current rents and current financing. They cannot observe how much competing space is already in the pipeline until it shows up in construction starts, and even then the decision to start is not easily reversed. When demand rises, rents rise because supply cannot respond. High rents trigger starts. The starts arrive years later, often after demand growth has slowed, and vacancy rises. Rents then fall far enough to stop new construction for years. The cycle is a feature of the production lag, not of irrationality. Section 12.5.1 shows the mechanism with arithmetic.

Two features make the downturn worse than the upturn is good. First, existing space cannot be withdrawn: a half-empty building still exists, and its owner will cut rents to fill it as long as rent exceeds the marginal cost of occupancy. Second, most CRE is financed with debt that matures on a calendar date that has nothing to do with the cycle. Owners whose loans mature at the bottom must refinance into a market with lower values, lower loan-to-value limits, and often higher rates.

#### Four causes of distress

| Cause | Mechanism | Persistence | Diagnostic |
|---|---|---|---|
| Supply shock | Deliveries exceed absorption | Cyclical; ends when the pipeline clears | Deliveries and under-construction as % of stock |
| Cyclical demand loss | Recession reduces space demand | Cyclical; recovers with employment | Net absorption versus employment growth |
| Structural demand destruction | Use per worker or per unit of output falls permanently (e.g., remote and hybrid work for office, e-commerce for some retail) | Persistent; old stock may never re-lease | Leasing per employee, sublease space, tenant downsizing at renewal |
| Financing shock | Maturity wall, rate reset, lender retrenchment | Lasts until loans are refinanced, restructured, or foreclosed | Maturities by year; refinance gaps; bank concentration |

The first two causes are what "buy at the bottom of the cycle" assumes. The third makes that strategy dangerous: a structural loss in demand looks like a cyclical one in the first two years. Case E is built around that ambiguity.

#### Liquidity versus solvency

A property is in a **liquidity** problem when its value exceeds its debt but the owner cannot refinance or pay current obligations. A property is in a **solvency** problem when its value is below its debt. The distinction decides who has the economic interest, what the owner will do, and who the counterparty for a distressed buyer actually is.

* In a liquidity problem the equity has positive value. The owner will sell, recapitalize, or make a capital call. A distressed buyer is competing with the owner's own alternatives, and the discount available is the price of immediacy (Chapter 1).
* In a solvency problem the equity is worthless or nearly so. It retains only option value and hold-up value: the ability to delay, litigate, or file for bankruptcy. The lender is the real owner. A distressed buyer negotiates with the lender, buys the loan, or buys the property from the lender after foreclosure.

Interest-rate resets turn many solvent properties into liquidity problems and many marginal ones into insolvency. Example 12.2 shows both.

#### Who sells at a discount, and why

A distressed price exists because a seller values immediacy, certainty, or balance-sheet relief more than the expected value of waiting. Lenders sell loans to reduce concentration, to stop accruing workout costs, to recognize losses in a quarter of their choosing, or because their own regulators or funding sources require it. Funds sell because of redemption queues, fund-life expirations, or covenant breaches. CMBS trusts sell through a special servicer whose incentives are set by the pooling and servicing agreement. Each forced seller is a liquidity consumer, and the buyer is paid as a liquidity provider. The danger is the one Chapter 1 named: liquidity providers are short a put on liquidity itself, and the buyer of distressed real estate in the early part of a downturn is often the forced seller of the later part.

#### Public and private prices

REIT shares reprice every second. Private appraisals reprice when appraisers find comparable sales, which in a frozen market can take a year or more. When the public market falls and private marks do not, the gap is information: the REIT price is a fast but noisy estimate of where private transactions will clear. It is also a slow estimate of nothing in particular when REIT shares are moved by fund flows, index changes, or the REIT's own leverage and management. Section 12.5.7 makes the comparison precise.

---

### 12.3 Technical definitions

| Term | Definition |
|---|---|
| Stock, completions, starts | Existing space $S_t$; space delivered in year $t$, $C_t$; space begun in year $t$, $N_t$. With a lag of $L$ years, $C_t = N_{t-L}$ |
| Natural vacancy | The vacancy rate $v^*$ at which real rents are stable. Above it rents fall; below it they rise |
| Feasibility rent | The rent at which new construction earns the developer's required yield on total cost. Starts are near zero below it |
| Maturity wall | A concentration of loan maturities in a short period, usually loans originated in one vintage under one set of rates and underwriting standards |
| Refinance gap | Existing balance plus refinancing costs minus the maximum new loan. Positive means equity must be contributed |
| Capital call | A demand by a fund or joint venture for additional equity from its partners. A partner who does not fund is usually diluted |
| Non-performing loan (NPL) | A loan in payment or maturity default. Its value is the present value of the resolution, not its unpaid principal balance (UPB) |
| Discounted payoff (DPO) | A lender's agreement to accept less than the full debt in satisfaction of the loan |
| Deed-in-lieu | The borrower conveys the property to the lender in place of foreclosure, usually in exchange for releases and sometimes "cash for keys" |
| Judicial / non-judicial foreclosure | Foreclosure through a court action, versus a sale by a trustee under a power of sale in a deed of trust without a court action |
| Credit bid | At a foreclosure sale, the lender may bid up to the amount of its debt without paying cash |
| Special servicer | The CMBS servicer that manages defaulted or imminently defaulting loans for the trust |
| Appraisal reduction amount (ARA) | The amount by which a defaulted loan's claim exceeds a haircut appraised value; it reduces servicer advances and, in many deals, the voting balance of junior classes |
| Controlling class / B-piece | The most junior outstanding CMBS class (or its representative), which typically appoints or directs the special servicer |
| CLD loans | Construction, land development, and other land loans |
| Total risk-based capital | The capital measure used as the denominator in the 2006 CRE concentration screens |
| Implied cap rate | Forward NOI divided by the value of real estate implied by a REIT's enterprise value |
| NAV discount | Share price divided by net asset value per share, minus one |
| Basis | A buyer's all-in cost: price, closing costs, and capital required to stabilize |
| Basis reset | A transfer of ownership at a lower basis, which changes the rent at which the new owner earns its required return |
| Vintage year | The year a fund or investment begins deploying capital. "Vintage-year evidence" compares returns by start year |

---

### 12.4 Equations and derivations

#### 12.4.1 A stock-flow model with a construction lag

Let latent space demand be $D_t$ (square feet that would be occupied at today's rent), stock $S_t$, and rent $R_t$. Space depreciates or is withdrawn at rate $\delta$. Annual steps:

$$D_t = D_{t-1}(1+g_t), \qquad C_t = N_{t-L}, \qquad S_t = S_{t-1}(1-\delta) + C_t,$$
$$O_t = \min(D_t, S_t), \qquad v_t = 1 - \frac{O_t}{S_t},$$
$$R_t = R_{t-1}\,\big[1 + \alpha\,(v^* - v_t)\big], \qquad N_t = \kappa \,\max\!\Big(0,\ \frac{R_t}{R^F} - 1\Big)\, S_t.$$

Here $\alpha$ is the rent response to the vacancy gap, $R^F$ is the feasibility rent, and $\kappa$ is the starts response: starts as a fraction of stock per unit of rent premium over feasibility. The model is a discrete version of the stock-flow logic in DiPasquale and Wheaton (1992) and the cyclical models that followed it (Wheaton, 1999). The parameters here are [HYPOTHESIS] and chosen for teaching.

**Why the lag creates overshooting.** Starts depend on today's rent. Today's rent depends on today's vacancy. Today's vacancy does not yet include the space started in the last $L$ years. So the signal to keep building stays on for $L$ years after enough space has been started. Steady-state analysis hides this. In a steady state $C = N = \delta S$ and $v = v^*$, which is true and useless during the transition. Wheaton (1999) shows formally that whether the cycle dampens or explodes depends on the product of the lag, the supply response, and the rent response. The simulation in Example 12.1 shows the same thing numerically.

#### 12.4.2 Refinancing and the rate reset

From Chapter 10, the maximum new loan is

$$L_{\max} = \min\Big(\lambda V,\ \frac{NOI}{DSCR_{\min}\,K},\ \frac{NOI}{DY_{\min}}\Big), \qquad K = 12\cdot\frac{i}{1-(1+i)^{-n}},\ \ i = r/12,$$

and the refinance gap is $G = B + \text{costs} - L_{\max}$. For an interest-only loan refinanced into an amortizing loan, the coverage ratio on the *existing* balance moves from $NOI/(B r_0)$ to $NOI/(B K_1)$. The ratio of the two is $r_0/K_1$. A move from a 3.60% interest-only rate to a 6.25% rate with 30-year amortization ($K_1 = 7.389\%$) cuts coverage by a factor of $0.036/0.07389 = 0.487$, more than half, with no change in the property.

#### 12.4.3 Pricing a non-performing loan

Let resolution scenario $s$ occur with probability $p_s$, pay gross cash $X_s$, cost $c_s$ in legal and carrying expenses, and resolve at time $\tau_s$ (years). At required return $k$, the maximum price is

$$P_{\max} = \sum_s p_s\,\frac{X_s - c_s}{(1+k)^{\tau_s}}.$$

The library implements this as `sdesk.cre.distressed_loan_recovery`. Three cautions apply.

1. **Scenario IRRs are not additive.** Fast resolutions produce very high annualized returns on small dollar gains (a 0.5-year DPO), and slow resolutions produce low returns on capital tied up for years. The probability-weighted mean of scenario IRRs therefore overstates the return. The IRR of expected cash flows is the more defensible single number (Chapter 1, §1.4.1).
2. **The scenarios are not independent of the price you pay.** A borrower facing a buyer who paid 60 cents knows the buyer can accept a DPO at 75 and still profit. Your basis is information to the borrower.
3. **The discount rate is a required return, not a market yield.** It must compensate for legal uncertainty, valuation error, and the possibility that every scenario's collateral value is wrong in the same direction.

#### 12.4.4 Foreclosure recovery

If the collateral is worth $V_0$ today and drifts at rate $d$ per year while the lender waits $T$ years (foreclosure plus resale), the net recovery is

$$N_T = V_0(1+d)^T(1-s) - \text{carry}\times T - \text{legal}, \qquad PV = \frac{N_T}{(1+k)^T},$$

where $s$ is the selling cost. Time hurts three ways: the value drifts (usually down for a neglected asset), carry accumulates linearly, and discounting compounds. The library function is `x_cre_distress.foreclosure_recovery`.

#### 12.4.5 The appraisal reduction amount

In a typical CMBS pooling and servicing agreement, once a loan is in special servicing and a new appraisal is obtained, the **appraisal reduction amount** is

$$ARA = \max\Big(0,\ \underbrace{B + I_{acc} + A + O}_{\text{trust's claim}} - \big[(1-h)\,V_{appr} + \text{reserves}\big]\Big),$$

with $B$ the principal balance, $I_{acc}$ accrued unpaid interest, $A$ unreimbursed advances, $O$ other amounts due (taxes, insurance, fees), and $h$ the haircut, commonly 10% (so 90% of appraised value). Deal documents govern the exact items. Two consequences follow:

* **Advances shrink.** The servicer's interest advance is reduced, typically in proportion $1 - ARA/B$. The junior bondholders stop receiving interest first.
* **Control can shift.** Many post-2010 deals reduce the controlling class's balance by allocated ARAs when testing whether it still controls. If the reduced balance falls below a threshold of its original balance (25% is a common figure in post-2010 deals [HYPOTHESIS: deal-specific; check the governing PSA]), control passes to the next senior class.

#### 12.4.6 Bank concentration and forced sales

The 2006 interagency guidance on CRE concentrations identifies banks for heightened supervisory attention when (1) construction, land development, and other land loans are at least 100% of total risk-based capital, or (2) total non-owner-occupied CRE loans are at least 300% of total risk-based capital **and** that portfolio grew at least 50% in the prior 36 months [FACT; OCC Bulletin 2006-46 and 71 FR 74580; see `references/sources_ch12.md`]. The screens are not lending limits.

Suppose a bank with CRE loans $C$ and capital $K$ wants $C/K \le m$ by selling loans at price $p$ per dollar of carrying value, with tax rate $\tau$. Selling $X$ reduces the numerator by $X$ and the denominator by the after-tax loss $(1-p)(1-\tau)X$:

$$C - X = m\big[K - (1-p)(1-\tau)X\big] \;\Rightarrow\; X = \frac{C - mK}{1 - m(1-p)(1-\tau)}.$$

The denominator is the feedback loop. At $m = 3$ and no tax, a sale price below $p = 2/3$ makes the denominator zero or negative: selling cannot fix the ratio, because each dollar sold destroys more than a third of a dollar of capital, which at 3x supports more than a dollar of loans. Below that price, the bank must raise capital or wait.

#### 12.4.7 REIT-implied cap rates and NAV

$$V^{RE}_{implied} = \text{Market cap} + \text{Debt} + \text{Preferred} - \text{Cash} - \text{Other assets}, \qquad c_{implied} = \frac{NOI^{cash}_{fwd}}{V^{RE}_{implied}}.$$

$$NAV = \frac{NOI^{cash}_{fwd}}{c_{private}} - \text{Debt} - \text{Preferred} + \text{Cash} + \text{Other assets}, \qquad \text{Discount} = \frac{P}{NAV/\text{share}} - 1.$$

Because NAV is levered, a 1% change in gross asset value moves NAV by $GAV/NAV$ percent. In Example 12.7, debt and preferred equal 40% of gross asset value and $GAV/NAV = 1.58$, so modest disagreements about private cap rates produce large NAV disagreements.

#### 12.4.8 Basis and required rent

For rentable area $A$, occupancy $o$, operating expenses $E$, recurring leasing capital $LC$, and target yield $y$ on basis $P$:

$$R_{req} = \frac{yP + E + LC}{A\,o}.$$

Two owners of identical buildings face the same $E$, $LC$, and market rent, but their $R_{req}$ differ through $yP$ alone. The owner with the lower basis can cut rent by $\Delta R = (y_1P_1 - y_2P_2)/(Ao)$ and still earn its target.

---

### 12.5 Worked examples

All examples are reproduced in `tests/test_ch12_examples.py`. Inputs are [HYPOTHESIS] unless a source is cited.

#### Example 12.1 — A development cycle in sixteen years

**Given.** A metro office market with stock $S_0 = 100$ million sf and latent demand $D_0 = 92$ million sf (8.0% vacancy). Rent $R_0 = \$30.00$/sf. Natural vacancy $v^* = 10\%$. Rent response $\alpha = 0.5$ (rents rise 0.5% per year for each point that vacancy is below 10%). Feasibility rent $R^F = \$33.00$. Starts response $\kappa = 0.35$. Construction lag $L = 3$ years. Depreciation $\delta = 1\%$ per year. Demand growth: +3% in years 1–4, −3% in year 5, 0% in year 6, +1.5% thereafter. No space is under construction at the start.

**Find.** The path of stock, vacancy, rent, completions, and starts. Compare the peak vacancy with a market whose lag is one year.

**Solution.** Year 1: $D_1 = 92 \times 1.03 = 94.76$. No completions, so $S_1 = 100 \times 0.99 = 99.00$, $v_1 = 1 - 94.76/99.00 = 4.28\%$. $R_1 = 30 \times [1 + 0.5(0.10 - 0.0428)] = \$30.86$. Since $R_1 < 33$, starts are zero.

Year 3 is the first year with starts: $R_3 = \$33.95$, so $N_3 = 0.35 \times (33.95/33 - 1) \times 97.03 = 0.98$ million sf. Those starts deliver in year 6.

| Year | Stock | Latent demand | Vacancy | Rent | Completions | Starts |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 100.00 | 92.00 | 8.00% | 30.00 | 0.00 | 0.00 |
| 1 | 99.00 | 94.76 | 4.28% | 30.86 | 0.00 | 0.00 |
| 2 | 98.01 | 97.60 | 0.42% | 32.34 | 0.00 | 0.00 |
| 3 | 97.03 | 100.53 | 0.00% | 33.95 | 0.00 | 0.98 |
| 4 | 96.06 | 103.55 | 0.00% | 35.65 | 0.00 | 2.70 |
| 5 | 95.10 | 100.44 | 0.00% | 37.43 | 0.00 | 4.47 |
| 6 | 95.13 | 100.44 | 0.00% | 39.31 | 0.98 | 6.36 |
| 7 | 96.88 | 101.95 | 0.00% | 41.27 | 2.70 | 8.50 |
| 8 | 100.38 | 103.48 | 0.00% | 43.33 | 4.47 | 11.00 |
| 9 | 105.74 | 105.03 | 0.67% | 45.35 | 6.36 | 13.86 |
| 10 | 113.18 | 106.60 | 5.81% | **46.31** | 8.50 | 15.97 |
| 11 | 123.05 | 108.20 | 12.07% | 45.83 | 11.00 | 16.74 |
| 12 | 135.67 | 109.83 | 19.05% | 43.75 | 13.86 | 15.47 |
| 13 | 150.29 | 111.47 | 25.83% | 40.29 | 15.97 | 11.62 |
| 14 | 165.53 | 113.15 | 31.65% | 35.93 | 16.74 | 5.14 |
| 15 | 179.34 | 114.84 | 35.97% | 31.27 | 15.47 | 0.00 |
| 16 | 189.17 | 116.57 | 38.38% | 26.83 | 11.62 | 0.00 |

(Stock, demand, completions, and starts in millions of sf; rent in \$/sf.)

Three features stand out.

1. **The year-5 recession is invisible.** Demand falls 3%, but latent demand still exceeds stock, so vacancy stays at zero and rents keep rising. Developers see no reason to stop.
2. **Starts peak (year 11) after rents peak (year 10)** and keep coming at nearly 16 million sf a year while vacancy climbs from 6% to 19%. Rent is still above the \$33 feasibility level, so the rule keeps starting buildings that will deliver into a market already oversupplied.
3. **Peak vacancy arrives after starts stop.** Starts end in year 15. Completions continue through year 17, and vacancy peaks at **38.51% in year 17**.

Running the same model with $L = 1$ (everything else unchanged), peak vacancy is **19.62% in year 12**, the rent peak is **\$39.87 in year 8**, and twenty-year completions are 51.51 million sf instead of 112.82 million sf.

**Check.** Steady-state identity: once starts stop, stock declines at 1% a year. From year 18 to 19 in the $L=3$ run there are no completions, and the test confirms $S_{19} = 0.99\,S_{18}$. The table rows reproduce from `x_cre_distress.stock_flow_simulation`.

**Decision consequence.** The model is crude, and its rents in the late years are too low because it has no floor at operating cost (§12.7). Its lesson survives the crudeness: **the length of the construction lag, not the size of the demand shock, decides how bad the downturn is.** For an acquisition, the variable to measure is space under construction and recently started as a percentage of stock, relative to plausible absorption over the lag. A buyer at the end of year 10, when vacancy is under 6% and rents are at their peak, is buying into a market that has already started 40.83 million sf that will deliver over the next three years, 36% of the existing stock, and the rule will start another 48.98 million sf before it stops. The first number was knowable from construction-start data. The vacancy rate was not the right statistic to watch.

#### Example 12.2 — Maturity wall and rate reset: liquidity or solvency?

**Given.** A 300-unit apartment property financed in 2021 with a \$60.0 million five-year interest-only loan at 3.60%. NOI at origination was \$4.50 million. The loan now matures. Two states of the world:

* **State 1:** NOI has grown to \$4.80 million. The market cap rate is 5.75%.
* **State 2:** NOI is \$3.90 million (new supply forced concessions; insurance and taxes rose). The market cap rate is 6.50%.

New loan terms: 6.25% rate, 30-year amortization, maximum 65% LTV, minimum 1.25x DSCR, minimum 8.0% debt yield. Refinancing costs 1% of the new loan. Selling costs 2%.

**Find.** DSCR before and after the reset; the maximum new loan and the binding constraint; the refinance gap; and whether the owner faces a liquidity or a solvency problem.

**Solution.**

Coverage at origination: $DS_0 = 60{,}000{,}000 \times 0.036 = \$2{,}160{,}000$; $DSCR_0 = 4{,}500{,}000/2{,}160{,}000 = 2.08x$.

Loan constant at the new terms: $K = 7.3886\%$. Debt service on the existing \$60 million at the new terms would be $60{,}000{,}000 \times 0.073886 = \$4{,}433{,}164$.

*State 1.* $V = 4{,}800{,}000/0.0575 = \$83{,}478{,}261$. Coverage on the existing balance at new terms: $4{,}800{,}000/4{,}433{,}164 = 1.08x$, against 2.22x at the old rate. Constraints:

* LTV: $0.65 \times 83{,}478{,}261 = \$54{,}260{,}870$
* DSCR: $4{,}800{,}000/(1.25 \times 0.073886) = \$51{,}971{,}912$ ← binding
* Debt yield: $4{,}800{,}000/0.08 = \$60{,}000{,}000$

Gap $= 60{,}000{,}000 + 0.01 \times 51{,}971{,}912 - 51{,}971{,}912 = \$8{,}547{,}807$. Equity at market value $= 83{,}478{,}261 - 60{,}000{,}000 = \$23{,}478{,}261$; net of selling costs, a sale clears $83{,}478{,}261 \times 0.98 - 60{,}000{,}000 = \$21{,}808{,}696$.

*State 2.* $V = 3{,}900{,}000/0.065 = \$60{,}000{,}000$. Constraints: LTV \$39,000,000 ← binding; DSCR \$42,227,178; debt yield \$48,750,000. Gap $= 60{,}000{,}000 + 390{,}000 - 39{,}000{,}000 = \$21{,}390{,}000$. A sale nets $60{,}000{,}000 \times 0.98 - 60{,}000{,}000 = -\$1{,}200{,}000$.

| | State 1 | State 2 |
|---|---:|---:|
| Value | \$83.48m | \$60.00m |
| Max new loan (binding) | \$51.97m (DSCR) | \$39.00m (LTV) |
| Refinance gap | \$8.55m | \$21.39m |
| Net sale proceeds to equity | +\$21.81m | −\$1.20m |
| Diagnosis | Liquidity | Solvency |

**Check.** State 1 debt yield on the new loan: $4.80/51.97 = 9.24\% > 8\%$; LTV $= 62.3\% < 65\%$; DSCR exactly 1.25x. State 2 at the LTV-sized loan: DSCR $= 3.90/(39.0 \times 0.073886) = 1.35x$, consistent with DSCR not binding.

**Decision consequence.** In State 1 nothing is wrong with the property. The rate reset cut coverage by half and created an \$8.5 million gap, but the equity is worth about \$22 million after selling costs. The owner will sell, bring in preferred equity, or make a capital call, and any partner will fund it because \$8.5 million protects \$22 million. A distressed buyer here is buying from a seller with good alternatives and should expect a small discount. In State 2 the owner would have to contribute \$21.4 million to keep an asset whose equity is worth less than zero after costs. No rational partner funds that capital call without a restructuring. The lender is the counterparty. The opportunity, if there is one, is in the loan (Example 12.3 and Case G) or in the REO later. **Diagnose first, then pick the instrument.**

#### Example 12.3 — Pricing the non-performing loan (Opportunity A)

**Given.** The \$40.0 million UPB office note. Contract rate 6.0%. As-is collateral value \$31.0 million (broker), which you accept for the moment. Resolution scenarios, with gross cash to the noteholder, costs (legal, carry, protective advances, net of any cash collected), and timing:

| Scenario | $p$ | Gross recovery | Costs | Years |
|---|---:|---:|---:|---:|
| Cure: borrower refinances, pays UPB + one year's interest | 0.10 | \$42,400,000 | \$150,000 | 1.00 |
| Discounted payoff | 0.25 | \$34,000,000 | \$250,000 | 0.50 |
| Deed-in-lieu, then resale at \$31.0m less 2% | 0.30 | \$30,380,000 | \$1,000,000 | 1.25 |
| Contested foreclosure, resale at \$29.5m less 2% | 0.20 | \$28,910,000 | \$2,200,000 | 2.00 |
| Borrower bankruptcy, resale at \$29.0m less 2% | 0.15 | \$28,420,000 | \$3,500,000 | 3.00 |

Required return $k = 16\%$.

**Find.** The maximum bid; the scenario returns and expected profit at a \$24.0 million bid; the IRR of expected cash flows.

**Solution.** Net cash and present value at 16%:

| Scenario | Net cash | PV at 16% | $p \times PV$ |
|---|---:|---:|---:|
| Cure | 42,250,000 | 36,422,414 | 3,642,241 |
| DPO | 33,750,000 | 31,336,088 | 7,834,022 |
| Deed-in-lieu | 29,380,000 | 24,405,028 | 7,321,508 |
| Contested | 26,710,000 | 19,849,881 | 3,969,976 |
| Bankruptcy | 24,920,000 | 15,965,189 | 2,394,778 |
| **Total** | | | **25,162,526** |

Maximum bid at 16%: **\$25.16 million, 62.9% of UPB**.

At a \$24.0 million bid (60.0% of UPB):

| Scenario | Profit | Annualized return |
|---|---:|---:|
| Cure | 18,250,000 | 76.04% |
| DPO | 9,750,000 | 97.75% |
| Deed-in-lieu | 5,380,000 | 17.56% |
| Contested | 2,710,000 | 5.49% |
| Bankruptcy | 920,000 | 1.26% |

Expected profit $= \$6{,}556{,}500$. Probability-weighted mean of the scenario returns $= 0.10(76.04\%) + 0.25(97.75\%) + 0.30(17.56\%) + 0.20(5.49\%) + 0.15(1.26\%) = 38.60\%$. The IRR of expected cash flows, the rate $k$ solving $\sum_s p_s N_s/(1+k)^{\tau_s} = 24{,}000{,}000$, is **20.46%**. Expected NPV at 16% $= 25{,}162{,}526 - 24{,}000{,}000 = \$1{,}162{,}526$.

**Check.** The expected resolution time is $\sum p_s \tau_s = 1.45$ years, and expected net cash is \$30,556,500. A single payment of that amount at 1.45 years would imply $(30{,}556{,}500/24{,}000{,}000)^{1/1.45} - 1 = 18.1\%$. The exact figure is higher (20.46%) because the large payments arrive early. Discounting is convex in time, so averaging the timing understates the return here.

**Decision consequence.** The 38.6% average return is an artifact: it is dominated by small, fast outcomes. The defensible estimate is about 20%, and it depends on the 65% of probability in fast, consensual outcomes (cure, DPO, deed-in-lieu). If you believe the borrower will fight, shift 0.15 of probability from DPO to contested foreclosure. Expected PV falls by $0.15 \times (31{,}336{,}088 - 19{,}849{,}881) = \$1{,}722{,}931$ and the maximum bid at 16% falls to \$23.44 million, below the \$24.0 million bid. **The single most valuable piece of diligence is the borrower's position: its other assets, its guarantor's exposure under the carve-out guaranty, and its lawyers.** Two further points belong in the bid memo. First, the broker's \$31 million as-is value is the seller's number. Every title scenario depends on it, so commission your own valuation. Second, bidding 60 rather than 63 is not only about return: a lower basis lets you accept a DPO the borrower can actually finance.

#### Example 12.4 — Foreclosure economics: Texas versus a judicial state

**Given.** A defaulted loan secured by a property worth \$20.0 million today. While the lender waits, the value drifts at −4% per year (deferred maintenance, tenant attrition), carrying costs net of any rent collected are \$600,000 per year, and selling costs on resale are 2%. Resale takes six months after the lender takes title. Required return 12%.

* **Texas (non-judicial).** Under Tex. Prop. Code §51.002, a foreclosure sale under a deed of trust is a public auction held between 10 a.m. and 4 p.m. on the first Tuesday of a month, and notice of sale must be given at least 21 days before the sale [FACT; statute text, see sources]. For property used as the debtor's residence, the servicer must first give at least 20 days' notice to cure (§51.002(d)); commercial loans rely on their loan documents for default notices. Assume three months from default to sale (loan-document notice and acceleration plus the statutory notice period) and \$150,000 of legal costs.
* **Judicial state (hypothetical).** Assume 24 months from default to sale through a court action with a receiver, and \$600,000 of legal costs. This timeline is [HYPOTHESIS]. Actual judicial timelines vary by state, county, court backlog, and borrower defenses, and must be checked locally.

**Find.** Net recovery and present value in each case. Then find the earliest Texas sale date if notice is given on Wednesday 11 March 2026, and if it is given on Wednesday 18 March 2026.

**Solution.**

*Texas:* $T = (3 + 6)/12 = 0.75$ years. Value at resale $= 20{,}000{,}000 \times 0.96^{0.75} = \$19{,}396{,}949$. Carry $= 600{,}000 \times 0.75 = \$450{,}000$. Net $= 19{,}396{,}949 \times 0.98 - 450{,}000 - 150{,}000 = \$18{,}409{,}010$. $PV = 18{,}409{,}010/1.12^{0.75} = \$16{,}908{,}961$.

*Judicial:* $T = (24 + 6)/12 = 2.5$ years. Value $= 20{,}000{,}000 \times 0.96^{2.5} = \$18{,}059{,}598$. Carry $= \$1{,}500{,}000$. Net $= 18{,}059{,}598 \times 0.98 - 1{,}500{,}000 - 600{,}000 = \$15{,}598{,}406$. $PV = 15{,}598{,}406/1.12^{2.5} = \$11{,}749{,}927$.

| | Texas | Judicial |
|---|---:|---:|
| Years to cash | 0.75 | 2.50 |
| Value at resale | \$19.40m | \$18.06m |
| Carry + legal | \$0.60m | \$2.10m |
| Net cash | \$18.41m | \$15.60m |
| PV at 12% | **\$16.91m** | **\$11.75m** |
| PV as % of today's value | 84.5% | 58.7% |

The difference is \$5.16 million, 25.8% of today's collateral value.

*Texas sale dates.* Notice on 11 March 2026: the earliest permissible date is 1 April 2026; the first Tuesday of April 2026 is 7 April, which is later than 1 April, so the sale can be held **7 April 2026** (27 days after notice). Notice on 18 March 2026: the earliest date is 8 April 2026; the first Tuesday of April (7 April) is too early, so the sale moves to **5 May 2026** (48 days after notice). A one-week delay in posting notice costs four weeks.

**Check.** Decomposing the \$5.16 million: value drift accounts for $(19.40 - 18.06) \times 0.98 = \$1.31$ million of net cash, extra carry and legal \$1.50 million, and the remainder is discounting over the additional 1.75 years.

**Decision consequence.** The same loan is worth about 25 points of collateral value less in a slow judicial jurisdiction under these assumptions. That difference must be in the bid. In a non-judicial state the timeline risk moves from the court to the borrower's ability to delay: a temporary restraining order, a lender-liability suit, or a bankruptcy filing that stays the sale. In Texas, the borrower's bankruptcy lawyer is the timeline. Model that probability explicitly, as Example 12.3 and Case G do, rather than treating the statutory minimum as the expected time.

#### Example 12.5 — Special servicing: appraisal reduction, advances, and control

**Given.** A \$50.0 million CMBS loan, 5.0% coupon, transferred to special servicing. Accrued unpaid interest \$1.5 million. Unreimbursed advances for taxes and insurance \$0.6 million. Reserves held by the servicer \$0.4 million. A new appraisal values the property at \$38.0 million. The controlling class (the B-piece) has an original and current balance of \$40.0 million. Haircut 10%. Assume the deal tests control after deducting ARAs, with a 25% threshold [HYPOTHESIS; deal-specific]. Fees, also [HYPOTHESIS] for illustration: special servicing fee 0.25% per year on the loan balance, workout fee 1.0% of collections on a modified loan, liquidation fee 1.0% of liquidation proceeds.

**Find.** (a) The ARA, the reduced monthly interest advance, and the B-piece's balance for control purposes. (b) The same if the appraisal is \$24.0 million. (c) The servicer's fees under a three-year modification (one year in special servicing, then collections of principal plus three years of interest) versus liquidation after 18 months for \$30.0 million.

**Solution.**

(a) Claim $= 50.0 + 1.5 + 0.6 = \$52.1$ million. Haircut value plus reserves $= 0.9 \times 38.0 + 0.4 = \$34.6$ million.
$ARA = 52.1 - 34.6 = \$17.5$ million.
Full monthly interest advance $= 50{,}000{,}000 \times 0.05/12 = \$208{,}333$. Reduced advance $= 208{,}333 \times (1 - 17.5/50.0) = 208{,}333 \times 0.65 = \$135{,}417$.
B-piece for control: $40.0 - 17.5 = \$22.5$ million, 56.25% of original. Control does not shift.

(b) Haircut value plus reserves $= 0.9 \times 24.0 + 0.4 = \$22.0$ million. $ARA = 52.1 - 22.0 = \$30.1$ million. B-piece for control: $40.0 - 30.1 = \$9.9$ million, **24.75%** of original. Below 25%: control shifts to the next class.

(c) Modification: $0.0025 \times 50{,}000{,}000 \times 1 + 0.01 \times (50{,}000{,}000 + 3 \times 0.05 \times 50{,}000{,}000) = 125{,}000 + 575{,}000 = \$700{,}000$. Liquidation: $0.0025 \times 50{,}000{,}000 \times 1.5 + 0.01 \times 30{,}000{,}000 = 187{,}500 + 300{,}000 = \$487{,}500$.

**Check.** The advance reduction is proportional: $135{,}417/208{,}333 = 0.65 = 1 - ARA/B$. ✓

**Decision consequence.** Three conflicts follow from the arithmetic. (1) The B-piece holder, who often controls the special servicer, prefers *later and higher* appraisals: a lower appraisal costs it interest and, near the threshold, control. (2) The special servicer earns more under modification (\$700,000) than under liquidation (\$487,500) in this fee structure, whether or not modification maximizes the trust's recovery. (3) Senior bondholders, who are protected by subordination, prefer speed. A buyer of a loan or REO from a CMBS trust is negotiating with an agent whose incentives are written in the pooling and servicing agreement. Read it. Ask who controls, how close the controlling class is to a control shift, and when the next appraisal is due. Those facts predict whether the servicer will sell, extend, or wait.

#### Example 12.6 — A bank at the concentration screens

**Given.** A community bank with total risk-based capital of \$250 million; CLD loans \$280 million; total non-owner-occupied CRE loans (including CLD) \$820 million, which were \$520 million 36 months ago. CRE loans can be sold at 88% of carrying value.

**Find.** (a) Whether the bank meets either screen. (b) The par amount of CRE loans it must sell to bring CRE/capital to 300%, with no tax effect and with a 21% tax rate. (c) The same at a 60% sale price.

**Solution.**

(a) CLD ratio $= 280/250 = 112\% \ge 100\%$: screen 1 met. CRE ratio $= 820/250 = 328\% \ge 300\%$; growth $= 820/520 - 1 = 57.7\% \ge 50\%$: screen 2 met.

(b) The naive answer is $820 - 3 \times 250 = \$70$ million. But each dollar sold at 88 books a 12-cent loss. With no tax:
$$X = \frac{820 - 750}{1 - 3(0.12)} = \frac{70}{0.64} = \$109.375 \text{ million}.$$
Loss $= 0.12 \times 109.375 = \$13.125$ million. Capital after $= \$236.875$ million. CRE after $= \$710.625$ million $= 3.00 \times 236.875$. ✓
With a 21% tax benefit on the loss: $X = 70/(1 - 3 \times 0.12 \times 0.79) = 70/0.7156 = \$97.82$ million; after-tax loss \$9.27 million.

(c) At 60%: the denominator is $1 - 3 \times 0.40 = -0.20 < 0$. No amount of selling reaches 300%. The bank must raise capital, shrink other assets, or accept supervisory scrutiny while it works the loans out.

**Decision consequence.** The bank's need to sell is real, but it is not unlimited. The bank will sell its best-priced loans first, because those sales hurt capital least, and it will hold the deepest-discount loans, because selling them is self-defeating. A loan buyer should therefore expect the bank's offered pool to be adversely selected toward loans the bank can sell near par, and should expect the truly distressed loans to come out later, after capital is raised or losses are absorbed through earnings. A bank that sells at 88 is a liquidity seller. A bank that would have to sell at 60 is not a seller at all. The concentration screens are not limits, so "the regulators will force them to sell" is a hypothesis to verify, not a fact.

#### Example 12.7 — What the REIT price implies (Opportunity C)

**Given.** Share price \$42.00; 100 million shares; debt \$3.2 billion; preferred \$0.3 billion; cash \$0.1 billion; other non-real-estate assets (land held for development, at estimated value) \$0.2 billion; forward cash NOI \$480 million. Your private-market cap rate for the portfolio: 5.50%.

**Find.** The implied cap rate, NAV per share, the discount, and the leverage of NAV to gross asset value.

**Solution.**
Market cap $= 42 \times 100\text{m} = \$4.2$ billion. Implied real estate value $= 4.2 + 3.2 + 0.3 - 0.1 - 0.2 = \$7.4$ billion. Implied cap $= 480/7{,}400 = 6.49\%$.
GAV at 5.50% $= 480/0.055 = \$8.727$ billion. NAV $= 8.727 - 3.2 - 0.3 + 0.1 + 0.2 = \$5.527$ billion $= \$55.27$ per share. Discount $= 42.00/55.27 - 1 = -24.0\%$.
$GAV/NAV = 8.727/5.527 = 1.58$.

**Check.** The implied cap rate is the private cap rate at which NAV equals the share price. At 6.49%, GAV $= \$7.4$ billion and NAV $= 7.4 - 3.2 - 0.3 + 0.1 + 0.2 = \$4.2$ billion $= \$42$ per share. ✓

**Decision consequence.** The "24% discount" is the same statement as "the public market capitalizes this NOI at 6.49%, not 5.50%". It is a disagreement of 99 bp about the cap rate, magnified 1.58 times by leverage. Before calling it an opportunity, ask which number is stale. If private transactions in the REIT's markets are clearing near 6.5%, the appraisal-based 5.50% is the stale number and there is no discount. If private trades are clearing near 5.5% and the REIT is being sold for reasons unrelated to its assets (index deletion, fund redemptions, a management problem), the discount is real, but capturing it requires a catalyst: buybacks funded by asset sales at private prices, a take-private, or activist pressure. Without a catalyst, the discount can persist or widen.

#### Example 12.8 — The basis reset

**Given.** Two identical 400,000 sf office buildings across the street from each other. Operating expenses \$4.8 million per year (\$12/sf, fixed). Recurring leasing capital (TI and commissions, averaged) \$1.6 million per year (\$4/sf). Stabilized occupancy 88%. Owner 1 bought at \$140 million (\$350/sf) and needs a 7.0% yield on basis. Owner 2 bought the other building out of foreclosure at \$60 million and spent \$10 million on capital, a \$70 million basis, and needs 9.0%. Market gross rent is \$40.00/sf.

**Find.** Each owner's required gross rent; the yield each earns at the market rent.

**Solution.** Occupied area $= 400{,}000 \times 0.88 = 352{,}000$ sf.
Owner 1: $R_{req} = (0.07 \times 140{,}000{,}000 + 4{,}800{,}000 + 1{,}600{,}000)/352{,}000 = 16{,}200{,}000/352{,}000 = \$46.02$/sf.
Owner 2: $R_{req} = (0.09 \times 70{,}000{,}000 + 6{,}400{,}000)/352{,}000 = 12{,}700{,}000/352{,}000 = \$36.08$/sf.
At \$40.00: NOI after leasing capital $= 40 \times 352{,}000 - 6{,}400{,}000 = \$7{,}680{,}000$. Owner 1 yield $= 7.68/140 = 5.49\%$. Owner 2 yield $= 7.68/70 = 10.97\%$.

**Check.** The rent gap $46.02 - 36.08 = \$9.94$/sf equals $(9.8 - 6.3)\text{m}/352{,}000$. ✓

**Decision consequence.** Owner 2 can lease at \$36, \$4 below market and \$10 below what Owner 1 needs, and still earn 9%. If Owner 2 does so to fill the building quickly, the market rent falls and Owner 1's building, already short of its required return, loses tenants at renewal. This is how distress propagates through a submarket: each foreclosure resets one basis, which lowers rents for every incumbent, which pushes the next owner toward default. For a buyer, the lesson has two edges. A low basis is a competitive weapon. But the next buyer, one foreclosure later, may have an even lower basis. **Your basis is cheap only relative to the bases of the buildings you compete with.** Map the capital structures of the competitive set, not only their rents.

---

### 12.6 CRE application: reading a distressed market

The examples supply a sequence of questions for any distressed situation.

1. **Where is the market in the stock-flow cycle?** Measure under-construction and recently started space as a percentage of stock and compare it with absorption over the construction lag (Example 12.1). A market whose pipeline exceeds two to three years of absorption has not reached its vacancy peak, however bad today's vacancy looks.
2. **Is the demand loss cyclical or structural?** For office, compare leasing per employee and the space tenants take at renewal with what they gave up. Sublease space is a leading indicator of future direct vacancy. A recession explains falling absorption. It does not explain tenants that renew at 60% of their previous footprint with employment unchanged.
3. **Which owners face maturities, and are they in liquidity or solvency trouble?** Build the maturity schedule for the competitive set. For each loan, compute the refinance gap at current terms (Example 12.2). Liquidity-problem owners recapitalize. Solvency-problem owners hand the asset to their lender, slowly.
4. **Who holds the loans, and what are their constraints?** Bank balance-sheet loans (Example 12.6), CMBS loans controlled by special servicers (Example 12.5), debt funds with their own lenders, and life companies all behave differently. The holder decides whether loans come to market, when, and at what price.
5. **What is the fastest legal route to the collateral, and what does delay cost?** Jurisdiction, loan documents, guaranties, and the borrower's incentives (Example 12.4).
6. **What does the public market say?** Compare implied cap rates on REITs with private appraisal-based cap rates (Example 12.7). A persistent gap is evidence about where private prices will clear.
7. **What basis will your competitors have?** (Example 12.8.) The cheapest building in the market sets the rent floor.
8. **What is your edge?** Speed and certainty of closing (liquidity provision), legal and workout capability (process skill), or a better forecast of demand (information). Name it. If none applies, you are a price-taker in a market where sellers know more than you.

#### Buying through downturns: what the vintage-year evidence does and does not show

The standard argument is that funds that invest in the years after a downturn earn higher returns than funds that invest at the peak. The evidence available to this book is limited and secondary. An industry report in 2014, citing Preqin data as of September 2014, said that closed-end real estate funds of vintages 2009–2012 were posting median IRRs between 12.8% (vintage 2012) and 15.8% (vintage 2009), and that 2005 and 2006 vintages had not recovered to the same degree [FACT as a report of Preqin data; industry press, class C; VERIFIED-SECONDARY; see `references/sources_ch12.md`]. INREV's global IRR index for non-listed, closed-end funds reports its 2005–2007 vintage group as the weakest [FACT as reported in a search summary of the INREV snapshot; figures not quoted here *(verification pending)*].

What this does **not** establish:

* **Interim IRRs are not realized returns.** A 2014 snapshot of 2009–2012 vintages is mostly unrealized and depends on appraisals made during a recovery.
* **Survivorship and selection.** Managers who raised funds in 2009–2011 were the ones who could. They are not a random sample.
* **Timing within the downturn.** "Vintage 2009" includes funds that bought in early 2009 and funds that bought in 2011. The evidence does not tell you whether to buy at the first signs of distress or wait for the second wave.
* **Reference class.** The 2009–2012 recovery was supported by falling interest rates. A downturn driven by rising rates, or by structural demand loss, is a different reference class.

The defensible conclusion is narrow [INFERENCE]: capital that was available and patient after 2009 was paid for providing liquidity when others could not. That supports keeping dry powder and the ability to act. It does not support any specific entry date, and it says nothing about property types whose demand has changed.

---

### 12.7 When the relationships fail

1. **The stock-flow model has no rent floor.** In Example 12.1 rents in late years fall toward levels below operating cost. Real owners stop cutting rent when it no longer covers the marginal cost of occupying space, and they mothball, convert, or demolish. Obsolete stock leaves the market. That is the mechanism by which structural demand loss is eventually absorbed, and it is slow.
2. **Structural loss masquerades as cyclical.** A model calibrated on past office cycles assumes demand recovers with employment. If use per worker falls permanently, the "trough" vacancy is a new equilibrium for old stock. Case E is built to make you price that possibility explicitly.
3. **Extend-and-pretend changes the timeline.** Lenders may modify and extend loans rather than foreclose. In 2009 the federal banking agencies issued a policy statement on prudent CRE loan workouts, which said that loans to borrowers able to repay on reasonable terms would not be adversely classified merely because collateral value had fallen below the loan balance. It was replaced in June 2023 by an interagency statement on CRE loan accommodations and workouts [FACT; FDIC FIL-61-2009 and FIL-34-2023 / OCC Bulletin 2023-23; VERIFIED-SECONDARY]. Whatever the merits, accommodation delays the arrival of distressed supply. A buyer who waits for "the wave of foreclosures" may wait years.
4. **Credit bids and auction dynamics.** At a foreclosure sale the lender can credit-bid its debt. Third parties rarely outbid a credit bid when the debt exceeds value, so foreclosure auctions are a poor place to buy. The REO sale after foreclosure is the market (Case G).
5. **REIT discounts can be about the REIT, not the real estate.** Leverage, management, dividend policy, and fund flows move REIT prices. The implied cap rate is a signal about private values only after those are accounted for.
6. **Basis resets can reverse.** If the market recovers quickly, the low-basis buyer has no reason to undercut rents, and the incumbent's position improves. The basis-reset spiral requires excess vacancy.
7. **The legal timeline is the borrower's choice.** Statutory minimums (21 days in Texas) are not expected timelines. Bankruptcy, lender-liability litigation, and title disputes are probability-weighted outcomes, not tails to ignore.

---

### 12.8 Historical episode: the RTC era (1989–1995) and the institutionalization of distressed CRE

**Date and environment.** The savings and loan crisis of the 1980s left the federal deposit insurance fund for thrifts insolvent and many failed thrifts holding large portfolios of commercial real estate loans and foreclosed property. Congress responded with the Financial Institutions Reform, Recovery, and Enforcement Act (FIRREA) in August 1989, which created the Resolution Trust Corporation (RTC) to resolve failed thrifts and dispose of their assets [FACT; CRS Report RS22959, *The Resolution Trust Corporation: Historical Analysis*, 2008; VERIFIED-SECONDARY]. Texas and the Southwest were at the center of the real estate losses; the regional detail (energy-price collapse, overbuilding, and tax-law changes in 1986) is widely discussed but its quantitative attribution is *(verification pending)* and is not used here.

**Scale.** By mid-1995, the RTC had resolved 747 thrifts with total assets of \$394 billion [FACT; Curry and Shibut (2000), *FDIC Banking Review* 13(2), as reported in search excerpts; VERIFIED-SECONDARY]. The RTC shut down in 1995 [FACT; CRS RS22959; Texas A&M Real Estate Center]. CRS reports that the RTC eventually obtained \$105 billion of funding and that estimates of the total government cost of the crisis are about \$150 billion, with estimates varying [FACT; CRS RS22959; VERIFIED-SECONDARY]. Curry and Shibut's own final cost and taxpayer-share figures are *(verification pending)* in this edition and are not quoted.

**What was knowable at the time.** That the government held an enormous inventory of real estate and loans, and that it had to sell, was public. What was not knowable was the clearing price. The private market had little capital for CRE, banks were themselves under pressure, and appraisals were unreliable in a market with few trades.

**Participants and incentives.**

* *The RTC* wanted speed, maximum recovery, and political defensibility, goals that conflict. Asset-by-asset sales were slow and the inventory was too large for retail disposition.
* *Private buyers* — the opportunity funds that became the template for today's opportunistic real estate funds — offered liquidity in exchange for large discounts and needed scale and speed.
* *Securitization* became one of the RTC's disposition tools. Facing billions of dollars of commercial mortgages, the RTC placed many in pools backing bonds — commercial mortgage-backed securities — and the 1992–1995 period established the underwriting standards, rating criteria, and standardized structures on which the private CMBS market was built [FACT; Texas A&M Real Estate Center; Chandan (2012), *Wharton Real Estate Review*; VERIFIED-SECONDARY].

**Alternative interpretations.** One reading is that the RTC sold too cheaply, transferring wealth to opportunity funds. Another is that the discount was the competitive price of immediacy and information in a market without other buyers, and that holding the assets longer would have cost more in carry and deterioration (Example 12.4's arithmetic at national scale). A third emphasizes the institutional legacy: by creating the CMBS market and the opportunity-fund model, the RTC changed who holds CRE risk in the next downturn. These readings are not exclusive, and this book does not adjudicate them with numbers it has not verified.

**A second episode for contrast: 2008–2013.** In the later crisis the FDIC resolved nearly 500 failed banks [FACT; FDIC podcast transcript on the crisis, *Crisis and Response* series; VERIFIED-SECONDARY; exact count *(verification pending)*]. An FDIC staff study finds that the FDIC resolved more than three times as many banks in the 1980–1994 crisis as in 2008–2013, but that total failed-bank assets were larger in 2008–2013 [FACT; FDIC staff study 2020; VERIFIED-SECONDARY]. Regulators had issued the 2006 concentration guidance before the crisis; a Federal Reserve analysis reports that 31% of commercial banks in 2006 exceeded at least one of the concentration levels [FACT; Federal Reserve, 2013 analysis of the CRE concentration guidance; VERIFIED-SECONDARY]. In October 2009 the agencies issued the workout policy statement discussed in §12.7, and a large share of distressed CRE was modified and extended rather than sold. The CMBS special-servicing machinery that the RTC era had made possible was tested at scale.

**What the episodes do and do not establish.**

* They establish that when the holders of distressed CRE are forced and large, disposition channels are invented (bulk sales, joint ventures, securitization), and that those channels shape the market for decades [INFERENCE from the CMBS history above].
* They establish that regulatory posture changes the timing of distress: forced disposition in the RTC era, accommodation and extension after 2009 [INFERENCE].
* They do **not** establish the returns earned by RTC-era buyers. This book has not verified those figures.
* They do **not** establish that the next downturn will offer RTC-style discounts. Distressed supply depends on who holds the loans, on their capital, and on regulatory forbearance, and all three differ across episodes.

**CRE connection.** In each episode, the decisive variable for a buyer was not the size of the losses but the identity, capital, and incentives of the holder of the loans. Examples 12.5 and 12.6 give you the arithmetic for two kinds of holder.

---

### 12.9 Frequent analytical errors

1. **Using replacement cost or unpaid principal as a value.** Both are reference points. Value is the present value of what the claim will pay.
2. **Averaging scenario IRRs for a loan purchase.** Fast, small wins dominate the average. Report the IRR of expected cash flows and the distribution (Example 12.3).
3. **Treating the statutory foreclosure minimum as the expected timeline.** Model delay by probability: contested foreclosure, bankruptcy, injunctions.
4. **Ignoring value drift during the workout.** A neglected asset loses value while the lawyers work. Carry is not only taxes and insurance.
5. **Calling a rate-reset problem a solvency problem, or the reverse.** Compute the refinance gap *and* the equity value net of selling costs before choosing whom to negotiate with.
6. **Assuming banks "must" sell.** The 2006 screens are not limits. Sale losses reduce capital, which can make selling self-defeating (Example 12.6).
7. **Reading a REIT discount as a private bargain without asking which price is stale.**
8. **Forgetting that your low basis is someone else's rent ceiling and the next buyer's target.**
9. **Watching vacancy instead of the pipeline.** Vacancy is low at exactly the moment the cycle's damage has been committed (Example 12.1).
10. **Using vintage-year averages as an entry signal.** The evidence is interim, selected, and from a falling-rate recovery.

---

### 12.10 Decision exercise: allocate the downturn capital

Return to §12.1. You may commit up to \$60 million in the next 90 days.

1. **Opportunity A (the NPL).** Using Example 12.3, state your bid and the probability of contested resolution at which you would withdraw. List the three pieces of diligence that would most change your probabilities, and what you would pay for each.
2. **Opportunity B (the office tower).** Using Case E, state whether you would bid, at what price, and what fact would make you walk away. Explain why the discount to replacement cost is not evidence of value.
3. **Opportunity C (the REIT).** State whether the 24% discount is a disagreement about cap rates, a statement about the REIT, or both. Name the catalyst you would need to own it, and the size you would hold without one.
4. **What you will not do.** Waiting is a legitimate answer for each opportunity. If you wait, state the trigger that brings you back: a price, a data release, or an event such as a maturity or a bank capital raise.
5. **Sizing.** Total exposure to one metro's office market across A, B, and C. State the downside if demand loss is structural.

**Rubric (see `problems/solutions/ch12_solutions.md` §Decision exercise).**

| Element | Full credit (4) | Partial (2) | None (0) |
|---|---|---|---|
| NPL bid | Bid below max PV at stated required return; identifies the borrower's position as the key unknown; computes the effect of a higher contested probability | Bid with a return target but no scenario sensitivity | Bids on % of UPB alone |
| Office tower | Prices off lease-up, TI/LC, capex, and carry; rejects replacement cost as support; names a structural-demand test and a walk-away price | Recognizes leasing costs qualitatively | "Fifth of replacement cost" as the thesis |
| REIT | Converts the discount into an implied cap rate; asks which price is stale; requires a catalyst or sizes small | Computes discount only | Buys "because of the discount" |
| Correlation | Recognizes that A, B, and C are all short the same office-demand risk; sizes jointly | Mentions correlation | Treats them as diversifying |
| Abstention | States what is declined and the re-entry trigger | Partial | Absent |

---

### 12.11 Connections to other chapters

* Chapter 1: price of immediacy, liquidity provision, scenario EV, and why mean IRR differs from IRR of expected flows.
* Chapter 3: forced selling and reflexivity; the bank-sale feedback loop of Example 12.6 is a balance-sheet version.
* Chapter 8: absorption, operating leverage, and reassessment; Case E's tax line.
* Chapter 9: cap rates, DCF valuation, and why replacement cost is not a floor.
* Chapter 10: loan sizing, refinance gaps, and capital stacks used throughout §12.4.2.
* Chapter 13: hold/sell decisions and real options, including the option to convert.
* Chapter 17: credit, recovery rates, and CMBS tranching in depth.
* Chapter 23: the 1980s–1990s Texas and RTC cycle and the post-2020 office cycle as historical cases.
* Case B (refinancing cliff), Case E (distressed office), Case G (buying the debt), Case J (credit-crunch hotel acquisition).

---

### 12.12 One-page reference sheet

**First questions.** Liquidity or solvency? Who holds the loan, and what constrains them? What is the fastest legal route to the collateral, and what does delay cost? What basis will competitors have? What is my edge?

| Item | Formula |
|---|---|
| Stock-flow | $S_t = S_{t-1}(1-\delta) + N_{t-L}$; $v_t = 1 - \min(D_t,S_t)/S_t$ |
| Rent adjustment | $R_t = R_{t-1}[1 + \alpha(v^* - v_t)]$ |
| Starts | $N_t = \kappa\max(0, R_t/R^F - 1)S_t$ |
| Coverage after a reset | $DSCR_1/DSCR_0 = r_0/K_1$ (IO to amortizing, same balance) |
| Max loan | $\min(\lambda V,\ NOI/(DSCR\cdot K),\ NOI/DY)$ |
| Refinance gap | $B + \text{costs} - L_{\max}$ |
| NPL max price | $\sum p_s (X_s - c_s)/(1+k)^{\tau_s}$ |
| Foreclosure PV | $[V_0(1+d)^T(1-s) - \text{carry}\cdot T - \text{legal}]/(1+k)^T$ |
| Texas sale | First Tuesday of a month, 10 a.m.–4 p.m., notice $\ge 21$ days before (Tex. Prop. Code §51.002) |
| ARA (generic) | $\max(0, B + I + A + O - [0.9V_{appr} + \text{reserves}])$ |
| Reduced advance | $\text{advance} \times (1 - ARA/B)$ |
| Concentration screens | CLD $\ge 100\%$ of total RBC; or CRE $\ge 300\%$ and 36-month growth $\ge 50\%$ |
| Loan sales to target $m$ | $X = (C - mK)/[1 - m(1-p)(1-\tau)]$ |
| REIT implied cap | $NOI_{fwd}/(\text{Mkt cap} + \text{Debt} + \text{Pref} - \text{Cash} - \text{Other})$ |
| NAV leverage | $\%\Delta NAV \approx (GAV/NAV)\,\%\Delta GAV$ |
| Required rent | $(yP + E + LC)/(A\,o)$ |

**Rules of thumb (to be tested, not trusted).** A three-year lag can double peak vacancy relative to a one-year lag in the simple model. An IO-to-amortizing reset from 3.6% to 6.25% halves coverage. At 3x leverage to capital, a bank cannot sell its way below 300% at prices under 67 cents.

---

### References for this chapter

All sources, with verification status, are listed in `references/sources_ch12.md`.

* DiPasquale, D., and Wheaton, W. C. (1992). "The Markets for Real Estate Assets and Space: A Conceptual Framework." *Real Estate Economics* (formerly *AREUEA Journal*), 20(2), 181–197.
* Wheaton, W. C. (1999). "Real Estate 'Cycles': Some Fundamentals." *Real Estate Economics*, 27(2), 209–230.
* Office of the Comptroller of the Currency (2006). Bulletin 2006-46, "Concentrations in Commercial Real Estate Lending, Sound Risk Management Practices"; interagency guidance at 71 FR 74580 (12 December 2006).
* Federal Reserve Board (2013). "An Analysis of the Impact of the Commercial Real Estate Concentration Guidance."
* FDIC (2009). FIL-61-2009, "Policy Statement on Prudent Commercial Real Estate Loan Workouts" (30 October 2009); OCC Bulletin 2023-23 and FDIC FIL-34-2023, "Policy Statement on Prudent Commercial Real Estate Loan Accommodations and Workouts" (29 June 2023).
* Texas Property Code §51.002.
* 11 U.S.C. §362(d)(3) (single asset real estate).
* Curry, T., and Shibut, L. (2000). "The Cost of the Savings and Loan Crisis: Truth and Consequences." *FDIC Banking Review*, 13(2).
* Congressional Research Service (2008). *The Resolution Trust Corporation: Historical Analysis*, RS22959.
* Chandan, S. (2012). *Wharton Real Estate Review*, Spring 2012 (on the RTC origins of CMBS).
* Texas A&M Real Estate Center, article on the origins of CMBS (RTC securitization).
* FDIC (2017). *Crisis and Response: An FDIC History, 2008–2013*; FDIC staff studies (2020).
* CRE Finance Council (2026). "Spotlight on Servicing: Understanding CMBS Appraisal Reductions"; DBRS Morningstar commentary on appraised values and ARAs.


\newpage

## Chapter 13 — CRE Trading and Portfolio Strategy

> **Status:** Complete (v1.0). All ten worked examples are reproduced in `tests/test_ch13_examples.py`, together with every number in `problems/questions/ch13_problems.md` and `problems/solutions/ch13_solutions.md`. The real-option helper is `models/python/sdesk/x_options_real.py`. Drills D121–D130 are in `training/daily_drills/drill_bank_ch13.json`. Sources are listed in `references/sources_ch13.md`. Three items are marked *(verification pending)*: the transaction cap rate and the scope of one 10-K figure in the historical episode (§13.9), and fund-vintage return data (§13.8), which the chapter deliberately does not quote. None is used in a calculation.

### Learning objectives

After this chapter you should be able to:

1. Run a hold–sell–refinance analysis on **equity at market**. Convert today's bid into the equity you would actually take out after selling costs and debt prepayment, compute the forward IRR of holding that equity, and compare it with the IRR of the best reinvestment alternative at the same leverage and risk.
2. Compute the **marginal cost of a cash-out refinancing** and explain why replacing below-market debt can make the incremental dollar of debt the most expensive capital in the structure.
3. Measure geographic concentration using NOI or value correlations. Compute portfolio volatility and each asset's contribution to risk, and show why diversification shrinks when correlations rise in a stress.
4. Read cap-rate spreads across sectors as statements about required returns and expected growth, $c = k - g$, and say which of the two a spread trade is betting on.
5. Hedge the interest-rate exposure of an acquisition pipeline with Treasury futures, swaps, or caps. Size the hedge by DV01 and quantify basis risk and the risk that a deal fails to close.
6. Size a liquidity reserve to survive a specified stress, including debt maturities, and state its opportunity cost.
7. Allocate a fixed amount of portfolio debt across assets with different volatilities, and distinguish portfolio-level leverage from asset-level default risk.
8. Value the option to wait or to develop with a binomial tree. Explain why uncertainty raises the value of waiting, why the option holder forgoes the asset's cash yield, and when doing nothing is the investment decision with the highest value.

---

### 13.1 Opening investment problem: the partnership's Tuesday agenda

You are the CIO of a Texas family partnership. All facts are [HYPOTHESIS], a constructed teaching case. The partnership owns:

| Asset | Market value (bid) | Forward NOI | Debt | Debt terms |
|---|---:|---:|---:|---|
| 280-unit garden multifamily, Austin suburbs | \$44.0m | \$2.20m | \$24.0m | Fixed 4.25%, interest-only, 5 years left, yield maintenance |
| 210,000 sf flex industrial, Houston | \$28.8m | \$1.80m | \$15.0m | Fixed 6.00%, interest-only |
| 150-room select-service hotel, San Antonio | \$30.0m | \$2.40m (after 4% FF&E reserve) | \$22.0m | Floating, capped; all-in 7.5%; **matures in 24 months** |
| 12-acre suburban land parcel | see Case I | none | none | |

Gross value is \$102.8m, debt \$61.0m, and equity at gross market value \$41.8m. In addition, the partnership has two Dallas industrial acquisitions under contract. They close in four months and will need \$60m of 10-year fixed-rate debt, priced at the 10-year Treasury yield plus 175 bp.

The agenda for Tuesday's meeting has six items:

1. A broker has delivered a \$44.0m bid for the multifamily asset, a 5.00% cap on forward NOI. The acquisitions officer wants to sell and redeploy the equity into industrial at a 6.25% cap: "We'd be trading a 5% yield for a 6¼% yield."
2. A lender has offered a cash-out refinancing of the multifamily instead.
3. All three operating assets are in Texas. One director asks how concentrated the portfolio is.
4. Hotel cap rates sit 325 bp above multifamily cap rates. Is the hotel sector "cheap"?
5. Should the pipeline's interest-rate exposure be hedged before the loans lock?
6. How much cash should be held back, and should the land be developed now?

By the end of the chapter you will be able to answer each item with a number and a stated assumption. Section 13.10 returns to the agenda as a decision exercise.

---

### 13.2 Economic intuition

#### Every hold is a purchase

The owner of an asset is, every day, implicitly buying it again at the price they could sell it for. Holding is economically the same as selling and buying back, except that holding saves the round-trip transaction costs and keeps the existing financing. The relevant capital is therefore not what you paid. It is what you could take out today: **equity at market**. The relevant return is not the IRR since inception. It is the forward IRR on equity at market. A building bought for \$33m that is now worth \$44m has an excellent historical IRR and possibly a poor forward one. The historical IRR is sunk. It belongs in the performance report, not in the decision.

#### Capital recycling is a relative-value trade, not a yield trade

"Selling at a 5% cap and buying at a 6¼% cap" sounds accretive. It is only accretive if the 6¼% asset is not 1¼ points riskier or 1¼ points slower-growing. In a constant-growth world the cap rate is $c = k - g$. A higher cap rate can mean a higher required return (more risk), lower expected growth, or a mispricing. Only the third is a gain. Capital recycling earns money when the seller's asset is priced for more growth than it will deliver, or the buyer's asset for less. It loses money in every other case, and it always costs two sets of transaction costs.

#### Correlation is the price of concentration

Owning three Texas assets in three property types looks diversified by sector. Their NOIs share a state economy, an energy cycle, a property-tax regime, an insurance market, and a population-growth story. Portfolio risk is governed by the correlations, and those correlations are highest exactly when diversification is needed most. A diversification benefit measured in calm years is an upper bound on the benefit you will have in a crisis.

#### Market selection is a forecast with a holding period

Choosing markets means choosing a bundle of exposures: population and job growth, supply elasticity, the property-tax and insurance regime, the local lender base, and the depth of the buyer pool when you want to sell. A useful discipline is to write each market thesis as three numbers and one condition: expected NOI growth, the cap rate you expect to exit at, the correlation of the market's NOI with the rest of the portfolio, and the observable event that would make you leave. Supply elasticity deserves particular attention. In markets where land is plentiful and entitlement is fast, which describes much of Texas, strong demand produces new supply quickly, and rent growth is competed away sooner than in supply-constrained markets [HYPOTHESIS as a general statement; test it against permit and delivery data for the specific submarket, Chapter 8]. Strong demand growth and strong investment returns are therefore not the same thing. Section 13.9 shows a large REIT revising its market selection within six years.

#### Opportunity cost is the only benchmark

Every number in this chapter is compared with something. The hold is compared with the best reinvestment at equal risk. The reserve is compared with the target equity return. The refinancing is compared with the cost of other capital. Waiting is compared with building now. The most common error in portfolio strategy is to evaluate an action against zero, or against the investor's own past returns, instead of against the next-best use of the same capital at the same risk. Case F makes this comparison explicit for a hotel against Treasuries after tax.

#### Hedging transfers one risk and creates another

A Treasury-futures hedge on an acquisition pipeline removes exposure to the Treasury yield. It does not remove exposure to the lender's spread, and it creates new exposures: basis risk between Treasury and loan pricing, margin calls, and a naked position if the deal fails to close. The question is never "hedged or unhedged". It is "which risk do I want, and which risk am I left with?"

#### Cash has a strategic value that its yield understates

A liquidity reserve earns the T-bill rate. Measured against a 10–12% target return it looks like a drag. Measured against the alternative of selling an asset in a stressed market, or handing it to a lender at a maturity, it is cheap insurance. The reserve also buys optionality: the ability to act when others are forced to sell. Chapter 1 called this being a liquidity provider. You can only provide liquidity if you have it.

#### Waiting is an asset

A land parcel, an unexercised right to develop, or uncommitted capital is an option. Exercising it, by building or buying, kills the option. Exercise is optimal only when the value captured today exceeds the value of keeping the choice open. Conventional NPV analysis compares "build now" with "never build". The relevant comparison is "build now" with "decide later". When uncertainty is high and the cost of delay is low, waiting can dominate an investment with a positive NPV. This is not an argument for paralysis. It is a valuation that tells you precisely what delay costs and what it buys.

---

### 13.3 Technical definitions

| Term | Definition |
|---|---|
| Equity at market, $E_M$ | Today's net sale proceeds after selling costs, debt repayment, and prepayment costs: $E_M = V(1-s) - B - PP$ |
| IRR on equity at market | The forward IRR of holding, using $-E_M$ as the time-0 flow. It is the return earned by not selling |
| Reinvestment alternative | The best available use of $E_M$ at comparable leverage and risk, net of acquisition costs |
| Break-even exit cap | The exit cap rate at which the hold IRR equals the alternative's IRR |
| Marginal cost of a refinancing | The IRR of the incremental flows: net cash received today against the incremental debt service and the incremental balance repaid |
| Yield maintenance (simplified) | PV, at the Treasury rate, of the coupon above the Treasury rate over the remaining term |
| Capital recycling | Selling assets and redeploying the proceeds into other assets, debt reduction, or distributions |
| Risk contribution | $RC_i = w_i (\Sigma w)_i / \sigma_p$. The contributions sum to $\sigma_p$; $RC_i/\sigma_p$ is asset $i$'s share of risk |
| Diversification ratio | $\sum_i w_i \sigma_i / \sigma_p \geq 1$ |
| Cap-rate spread | The difference between two sectors' cap rates, or between a cap rate and a Treasury yield, in bp |
| DV01 | The dollar change in value for a 1 bp change in yield (positive number) |
| Basis risk | Risk that the hedge instrument and the exposure move by different amounts |
| Liquidity reserve | Cash or committed, unconditional capacity held to cover shortfalls and maturities in a defined stress |
| Real option | The right, but not the obligation, to take an action (build, expand, wait, abandon) at a cost |
| Risk-neutral probability $q$ | The probability that prices the underlying correctly when every claim is discounted at the risk-free rate |
| Cash yield $\delta$ | Income forgone by holding the option instead of the underlying asset; for a development option, the stabilized NOI yield |
| Value of waiting | Option value minus $\max(\text{NPV now}, 0)$ |

---

### 13.4 Equations and derivations

#### 13.4.1 Equity at market and the hold IRR

Let $V_0$ be the bid, $s$ the selling-cost rate, $B_0$ the loan balance, and $PP$ the prepayment cost. Then

$$E_M = V_0(1-s) - B_0 - PP.$$

Holding for $T$ years produces cash flow after debt service $CF_t = NOI_t - DS_t$ and a reversion

$$R_T = \frac{NOI_{T+1}}{c_T}(1-s) - B_T.$$

The **hold IRR** solves $-E_M + \sum_{t=1}^{T} CF_t/(1+IRR)^t + R_T/(1+IRR)^T = 0$.

The alternative invests the same $E_M$. At loan-to-value $\lambda$ and buyer costs $b$, the purchase price it supports is

$$P = \frac{E_M}{1 + b - \lambda}.$$

**The decision rule.** Hold if $IRR_{hold} > IRR_{alt}$ at equal risk. If leverage or business risk differ, compare on a common basis: unlevered IRRs, or IRRs at the same LTV, before comparing levered results.

**Why prepayment belongs in $E_M$.** If the existing loan carries a below-market coupon, selling forces you to give up that loan and pay to retire it. Holding keeps it. A correct comparison charges the prepayment cost to the sale and credits the cheap coupon to the hold. Omit either and the comparison is biased.

#### 13.4.2 Simplified yield maintenance

With coupon $r_L$, Treasury yield $y$ for the remaining term $n$, and balance $B$, using annual periods:

$$PP = B (r_L - y)\, a_{\overline{n}|y}, \qquad a_{\overline{n}|y} = \frac{1-(1+y)^{-n}}{y}.$$

Actual loan documents specify the discounting (often monthly, sometimes at Treasury flat, sometimes Treasury plus a spread) and a minimum penalty, often 1%. Use the document, not this formula, for a real transaction.

#### 13.4.3 Marginal cost of a cash-out refinancing

An existing loan $B$ at rate $r_L$ is replaced by a new loan $L'$ at rate $r'$, both interest-only with $T$ years to maturity. Cash received today is $C_0 = L' - B - PP - \text{costs}$. The incremental flows to the borrower are

$$\Big[+C_0;\ -(L' r' - B r_L) \text{ for } t=1..T;\ -(L' - B) \text{ at } T\Big].$$

The marginal cost $m$ is the IRR of those flows from the lender's side. When $r' > r_L$, the borrower pays the higher rate on the *whole* new balance, not only on the cash released. A small cash-out on top of a large below-market loan can carry a marginal cost far above $r'$.

#### 13.4.4 Portfolio volatility and risk contributions

With value weights $w$, volatilities $\sigma$, and correlation matrix $\rho$:

$$\sigma_p^2 = \sum_i \sum_j w_i w_j \sigma_i \sigma_j \rho_{ij}, \qquad RC_i = \frac{w_i \sum_j \rho_{ij}\sigma_i\sigma_j w_j}{\sigma_p}, \qquad \sum_i RC_i = \sigma_p.$$

The library function is `sdesk.risk.portfolio_volatility(weights, vols, corr)`. For two assets the expression reduces to $\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2 w_1 w_2 \rho \sigma_1 \sigma_2$. At $\rho = 1$, $\sigma_p = w_1\sigma_1 + w_2\sigma_2$, and there is no diversification.

**Equity volatility at the portfolio level.** If total debt $D$ is fixed in dollars, portfolio equity is $E = \sum V_i - D$ and

$$\sigma_E = \sigma_p \frac{\sum V_i}{E}.$$

How the debt is allocated among assets does not change $\sigma_E$. It changes which asset breaches a covenant or fails to refinance. Section 13.5, Example 13.7, quantifies this.

#### 13.4.5 Cap rates, required returns, and implied growth

For a perpetuity growing at $g$, priced to return $k$, with NOI after reserves:

$$V_0 = \frac{NOI_1}{k-g} \;\Rightarrow\; c = k - g.$$

For two sectors A and B:

$$c_A - c_B = (k_A - k_B) - (g_A - g_B).$$

A spread is one equation in two unknowns: the risk-premium differential and the growth differential. A spread trade is a claim that the market has mis-set one of them. You must say which one.

**Convergence arithmetic.** If the spread narrows by $\Delta$ and the move happens entirely in sector A's cap rate, A's value changes by $c_A/(c_A - \Delta) - 1$. If it happens entirely in B's, B's value changes by $c_B/(c_B + \Delta) - 1$. A long-A, short-B view (or, in private real estate, overweight A and underweight B) pays in the first case. In the second it only avoids a loss.

#### 13.4.6 DV01 hedge of an acquisition pipeline

A borrower who will lock a fixed-rate loan of principal $L$ in the future is exposed to the rate at lock. Each 1 bp increase in the locked rate costs approximately the PV of 1 bp per year on $L$ over the term:

$$DV01_{loan} \approx L \times 0.0001 \times a_{\overline{n}|r}.$$

A more precise version prices the loan as a bond with the actual payment frequency and takes the central difference, as `sdesk.fixed_income.dv01(ytm, coupon, years, face, freq)` does. The number of short futures contracts is

$$N = \frac{DV01_{loan}}{DV01_{fut}}, \qquad DV01_{fut} \approx \frac{DV01_{CTD}}{CF_{CTD}},$$

where CTD is the cheapest-to-deliver note and $CF$ its conversion factor. The CME 10-Year T-Note futures contract has a face value of \$100,000 [FACT; ch13-S07]. A futures DV01 must come from a live calculation. It moves with the level of yields and the identity of the CTD.

The locked loan rate is $y_{Tsy} + s$. The hedge offsets $\Delta y_{Tsy}$ but not $\Delta s$:

$$\text{Net P\&L} = -DV01_{loan}(\Delta y_{Tsy} + \Delta s) + N \cdot DV01_{fut} \cdot \Delta y_{Tsy}\quad(\text{changes in bp}).$$

When spreads widen as Treasuries rally, which is the usual pattern in a flight to quality, the hedged borrower loses on both lines.

**Swaps and caps for existing floating-rate debt.** The hotel loan in §13.1 floats. A **pay-fixed swap** converts it to fixed: the owner pays the swap rate and receives the floating index, so the all-in cost becomes swap rate plus the loan spread. The swap has no upfront premium, but it has a mark-to-market. If rates fall and the hotel is sold or refinanced early, breaking the swap costs roughly the swap's DV01 times the fall in rates. A **cap** is a strip of call options on the floating index. It costs an upfront premium and limits the index at the strike, while the owner keeps the benefit of falling rates. As a rough annualized cost, a hypothetical \$250,000 two-year cap on the \$22.0m hotel loan costs $250{,}000/22{,}000{,}000/2 = 0.57\%$, about 57 bp a year [HYPOTHESIS: cap premia depend on the strike, the term, and implied volatility; Chapter 18 prices them]. Lenders often require a cap on floating-rate loans, and the strike is set so the loan still meets a DSCR test at the strike rate (`cre.max_loan(..., dscr_rate=strike)`). The choice between the two is a choice of which risk to keep: the swap keeps prepayment and breakage risk, the cap keeps the cost of the premium and the rates between today's level and the strike.

#### 13.4.7 Liquidity reserve

Over a stress horizon $t = 1..H$, let $X_t$ be the portfolio's net cash flow after debt service and committed capital spending. Let $M_t$ be the cash needed at any debt maturity in the period: the existing balance less the new loan available at stressed value and stressed underwriting. The reserve that keeps cumulative cash non-negative is

$$R^* = \max\Big(0,\ -\min_{\tau \le H} \sum_{t=1}^{\tau} (X_t - M_t)\Big).$$

Its annual opportunity cost is $R^*(k_E - r_f)$, where $k_E$ is the target equity return and $r_f$ the yield earned on the reserve.

#### 13.4.8 The binomial real option

Let the value of the completed building be $V$. Over one period it moves to $uV$ or $dV$. An owner of the completed building also receives a cash yield $\delta V$ during the period. The holder of the option to build does not. Pricing by replication (see `sdesk/x_options_real.py`):

$$q\, uV + (1-q)\, dV + \delta V = (1+r)V \;\Rightarrow\; q = \frac{1 + r - \delta - d}{u - d}.$$

With construction cost $K_t$ at time $t$, the option to build at any node is valued backward:

$$F_t = \max\Big(V_t - K_t,\ \frac{q F_{t+1}^{u} + (1-q) F_{t+1}^{d}}{1+r}\Big),\qquad F_T = \max(V_T - K_T, 0).$$

The **value of waiting** is $F_0 - \max(V_0 - K_0, 0)$. Three forces govern it:

* **Volatility** ($u$, $d$) raises the value of keeping the choice open, because the downside of waiting is truncated at zero and the upside is not.
* **The cash yield $\delta$** is the cost of waiting. Every year you wait, you forgo the NOI the building would have produced. A high cap rate makes waiting expensive.
* **Cost escalation** raises the strike over time, which also makes waiting expensive.

The perpetual continuous-time version (McDonald and Siegel, 1986; Dixit and Pindyck, 1994) gives a closed-form hurdle. Invest when

$$\frac{V}{K} \ge \frac{\beta}{\beta - 1},\qquad \tfrac12\sigma^2\beta(\beta - 1) + (r - \delta)\beta - r = 0,\ \beta > 1.$$

At $\sigma = 0$ and $\delta > r$ the hurdle collapses to 1, which is the NPV rule. With uncertainty the hurdle exceeds 1. **A positive NPV is necessary but not sufficient.**

#### 13.4.9 Real-world versus risk-neutral valuation

Practitioners often value waiting with a decision tree: real-world probabilities $p$, discounted at the asset's required return $k$. That method misprices options, because an option is riskier than its underlying and needs a higher discount rate. The risk-neutral tree avoids the problem by changing the probabilities instead of the rate. When the two methods agree on the decision, the conclusion is robust. When they disagree, trust the risk-neutral answer for market risk. For **idiosyncratic** risks such as an entitlement vote, use real-world probabilities, because investors do not demand a premium for risk they can diversify away. Case I combines both.

---

### 13.5 Worked examples

All inputs are [HYPOTHESIS] unless cited. All ten examples are reproduced in `tests/test_ch13_examples.py`.

#### Example 13.1 — Hold or sell: the IRR on equity at market

**Given.** The multifamily asset from §13.1. Bid \$44,000,000. Forward NOI \$2,200,000, growing 3.0% a year. Selling costs 1.5%. Loan \$24,000,000, fixed 4.25%, interest-only, five years remaining. Yield maintenance per §13.4.2 with the five-year Treasury at 3.75%. Hold scenario: five more years, exit at a 5.25% cap on year-6 NOI, 1.5% selling costs, loan repaid at maturity.

Alternative: invest the same equity in stabilized industrial at a 6.25% cap on forward NOI. NOI grows 2.5%. Buyer costs 1.5%. Loan at 55% LTV, 6.00% interest-only. Exit at a 6.50% cap after five years, 1.5% selling costs.

**Find.** $E_M$, the hold IRR, the alternative IRR, the break-even exit cap, and unlevered IRRs for both.

**Solution.**

*Prepayment.* $a_{\overline{5}|3.75\%} = 4.4833$. $PP = 24{,}000{,}000 \times (0.0425 - 0.0375) \times 4.4833 = \$537{,}991$.

*Equity at market.* $E_M = 44{,}000{,}000 \times 0.985 - 24{,}000{,}000 - 537{,}991 = 43{,}340{,}000 - 24{,}537{,}991 = \$18{,}802{,}009$.

*Hold flows.* NOI path (years 1–6): 2,200,000; 2,266,000; 2,333,980; 2,403,999; 2,476,119; 2,550,403. Interest is \$1,020,000 a year.

| Year | NOI | Interest | Reversion | Equity flow |
|---|---:|---:|---:|---:|
| 0 | | | | −18,802,009 |
| 1 | 2,200,000 | 1,020,000 | | 1,180,000 |
| 2 | 2,266,000 | 1,020,000 | | 1,246,000 |
| 3 | 2,333,980 | 1,020,000 | | 1,313,980 |
| 4 | 2,403,999 | 1,020,000 | | 1,383,999 |
| 5 | 2,476,119 | 1,020,000 | 23,850,418 | 25,306,537 |

Gross reversion $= 2{,}550{,}403/0.0525 = \$48{,}579{,}104$. Net of 1.5% selling costs and the \$24.0m loan: \$23,850,418. **Hold IRR = 11.21%.**

*Alternative.* $P = 18{,}802{,}009/(1 + 0.015 - 0.55) = \$40{,}434{,}427$. Loan $= 0.55P = \$22{,}238{,}935$. Year-1 NOI $= 0.0625P = \$2{,}527{,}152$. Interest $= \$1{,}334{,}336$. The equity flows are −18,802,009; 1,192,816; 1,255,994; 1,320,753; 1,387,130; 22,544,717. **Alternative IRR = 9.01%.**

*Break-even exit cap.* Solving for the hold exit cap that gives 9.01% yields **5.57%**: 57 bp above today's 5.00% bid cap and 32 bp above the base exit cap.

*Unlevered comparison.* Hold, unlevered on net sale value: **7.17%**. Industrial, unlevered on gross cost: **7.41%**.

**Check.** The hold's year-0 equity and reversion can be verified by hand: $0.985 \times 48{,}579{,}104 = 47{,}850{,}418$, less 24,000,000 = 23,850,418. The alternative's LTV at purchase is $22{,}238{,}935 / 40{,}434{,}427 = 55.0\%$. The hold's LTV on the bid is $24.0/44.0 = 54.5\%$. Leverage is comparable.

**Decision consequence.** On an unlevered basis the industrial alternative is better by about 24 bp. That is before two sets of transaction costs are tested for robustness and before any adjustment for the industrial asset's different risk. On a levered basis the hold wins by 220 bp. The entire difference comes from the 4.25% loan, which the hold keeps and the sale destroys. The acquisitions officer's "5% versus 6¼%" framing compares yields and ignores both growth and financing. The defensible statement is: *hold unless you expect the multifamily exit cap to exceed about 5.57%, or unless the 4.25% loan could be assumed by a buyer and priced into the bid.* An assumable loan changes the analysis: the cheap debt then becomes part of what the buyer pays for, and the bid should rise.

#### Example 13.2 — Refinance instead: the marginal cost of a cash-out

**Given.** Same asset. A lender offers a new five-year interest-only loan at 6.00%. Sizing constraints: 65% LTV, 1.25x DSCR, 8.0% debt yield. Refinancing costs 1.0% of the new loan. Prepayment as in Example 13.1.

**Find.** The new loan, cash released, and the marginal cost of the cash-out.

**Solution.** `cre.max_loan`: LTV \$28,600,000; DSCR $2{,}200{,}000/1.25/0.06 = \$29{,}333{,}333$; debt yield $2{,}200{,}000/0.08 = \$27{,}500{,}000$. **Debt yield binds: \$27,500,000.**

Cash released $= 27{,}500{,}000 - 24{,}000{,}000 - 537{,}991 - 275{,}000 = \$2{,}687{,}009$.

Incremental interest $= 27{,}500{,}000 \times 0.06 - 24{,}000{,}000 \times 0.0425 = 1{,}650{,}000 - 1{,}020{,}000 = \$630{,}000$ a year.

Incremental flows from the borrower's side: $+2{,}687{,}009$ today; $-630{,}000$ in years 1–5; $-3{,}500{,}000$ extra principal at year 5. The IRR of these flows from the lender's side is the **marginal cost: 26.99%**.

**Check.** Bound: even with no prepayment or costs, cash of \$3.5m for \$630,000 a year plus \$3.5m at maturity is an 18.0% coupon. The penalty and fees push the cost higher.

**Decision consequence.** A 6.00% loan quote hides a 27% marginal cost, because the refinancing reprices \$24m of 4.25% debt in order to release \$2.7m. No plausible redeployment earns 27%. If the partnership needs liquidity from this asset, the comparison should be with supplemental financing that leaves the first mortgage in place, such as a supplemental loan where the loan program permits it or preferred equity. Those instruments are priced at their own coupons on the incremental dollars only. Rule: **always compute the cost of the incremental capital, not the headline rate of the new instrument.**

#### Example 13.3 — Geographic concentration: three Texas assets

**Given.** Value weights from §13.1: multifamily 44.0/102.8 = 0.4280, industrial 28.8/102.8 = 0.2802, hotel 30.0/102.8 = 0.2918. Annual value volatilities [HYPOTHESIS]: 12%, 9%, 20%. Correlations for the Texas portfolio [HYPOTHESIS]: MF–industrial 0.60, MF–hotel 0.50, industrial–hotel 0.55. Variant: replace the Houston industrial asset with industrial of the same volatility in a market with lower correlation to Texas (MF–industrial 0.25, industrial–hotel 0.30). Stress variant: every correlation 0.90.

**Find.** Portfolio volatility, each asset's share of risk, the diversification ratio, and a one-year 99% normal VaR in dollars.

**Solution.** With `risk.portfolio_volatility`:

| Portfolio | $\sigma_p$ | MF share of risk | Industrial share | Hotel share |
|---|---:|---:|---:|---:|
| All Texas | 11.34% | 38.2% | 17.3% | 44.5% |
| Industrial outside Texas | 10.59% | 39.8% | 12.5% | 47.7% |
| Stress ($\rho = 0.90$) | 13.06% | | | |
| No diversification ($\rho = 1$) | 13.49% | | | |

The weighted average volatility is $0.4280(12\%) + 0.2802(9\%) + 0.2918(20\%) = 13.49\%$. Diversification ratio, all Texas: $13.49/11.34 = 1.19$. With industrial outside Texas: 1.27.

One-year 99% VaR, all Texas, zero mean: $2.3263 \times 11.34\% \times \$102.8\text{m} = \$27.1\text{m}$. That is 65% of the \$41.8m of equity.

**Check.** At $\rho = 1$ the formula returns exactly the weighted average volatility, 13.49%. The stress case lies between the base case and that bound.

**Decision consequence.** Three findings. First, the hotel is 29% of value but **45% of risk**. Any decision about portfolio risk is mostly a decision about the hotel. Second, moving the industrial allocation outside Texas lowers volatility by only 75 bp, because industrial is the lowest-volatility asset and already contributes little risk. Diversifying the *hotel* exposure would do more. Third, in a stress the Texas portfolio's volatility rises to 13.06%, within 43 bp of no diversification at all. The diversification you measure in calm years is largely unavailable in the year you need it. A 99% VaR equal to 65% of equity says the portfolio's leverage, not its sector mix, is the first-order risk.

#### Example 13.4 — Relative value: what the hotel–multifamily spread says

**Given.** Hotel cap rate 8.50%, multifamily 5.25%: a spread of 325 bp. A hypothetical ten-year history of the year-end spread, in bp: 250, 240, 235, 245, 260, 290, 390, 320, 265, 255. The 390 bp observation is the pandemic year. Assume, as a [HYPOTHESIS], that investors require a 250 bp higher unlevered return on hotels than on multifamily.

**Find.** The z-score of today's spread, with and without the pandemic year. The growth differential implied by the spread. The value effect of convergence to the 275 bp mean, under each of the two possible paths.

**Solution.**

*Statistics.* All ten years: mean 275 bp, sample s.d. 47.8 bp, $z = (325 - 275)/47.8 = 1.05$. Excluding the pandemic year: mean 262.2 bp, s.d. 27.1 bp, $z = 2.32$.

*Implied growth.* $c_H - c_{MF} = (k_H - k_{MF}) - (g_H - g_{MF})$, so $3.25\% = 2.50\% - (g_H - g_{MF})$ and $g_{MF} - g_H = 0.75\%$. The spread is consistent with multifamily NOI growing 75 bp a year faster than hotel NOI in perpetuity.

*Convergence.* If the spread returns to 275 bp through the hotel cap falling to 8.00%, hotel values rise $8.50/8.00 - 1 = 6.25\%$. If it returns through the multifamily cap rising to 5.75%, multifamily values fall $5.25/5.75 - 1 = -8.70\%$ and hotel values do not move.

**Check.** The z-score formula is symmetric. The sensitivity to one observation is the point: removing one year more than doubles $z$.

**Decision consequence.** "Hotels are cheap" is a claim that one of two things is wrong: either the market's hotel risk premium is too high, or its forecast of hotel growth is too low. A z-score of 1.05 on ten annual observations, one of them a pandemic, is weak evidence of either. Two specific beliefs would justify an overweight. One is that the 75 bp growth gap is too wide, for example because hotel supply growth is low while multifamily deliveries are high (Chapter 8). The other is that the hotel risk premium reflects pandemic memory more than forward risk. If neither can be supported with data, the spread is information about the market's beliefs, not a signal. Note also that only one of the two convergence paths pays an owner of hotels. An owner of both sectors earns nothing from convergence that occurs through multifamily repricing.

#### Example 13.5 — Hedging the acquisition pipeline with Treasury futures

**Given.** Two acquisitions close in four months and require \$60,000,000 of 10-year, interest-only, monthly-pay fixed-rate debt priced at the 10-year Treasury plus 175 bp. Today that implies 6.00% [HYPOTHESIS: 10-year Treasury 4.25%]. The futures DV01 is \$85 per contract [HYPOTHESIS; obtain the live CTD-based figure before trading]. The CME 10-Year T-Note futures contract has \$100,000 face value [FACT; ch13-S07].

**Find.** The pipeline DV01, the number of contracts, and the P&L at lock in three scenarios: (a) Treasuries +50 bp, spread unchanged; (b) Treasuries −40 bp, spread +60 bp; (c) Treasuries −40 bp and the acquisitions fail to close.

**Solution.**

*DV01.* `fi.dv01(0.06, 0.06, 10, face=60_000_000, freq=12)` = **\$45,037** per bp. Annual-annuity approximation: $60{,}000{,}000 \times 0.0001 \times a_{\overline{10}|6\%} = 6{,}000 \times 7.3601 = \$44,161$, within 2%.

*Contracts.* $N = 45{,}037/85 = 529.8 \to$ **530 short contracts**.

| Scenario | Loan PV effect | Futures P&L | Net |
|---|---:|---:|---:|
| (a) Tsy +50, spread 0 | −2,251,837 | +2,252,500 | +663 |
| (b) Tsy −40, spread +60 | −900,735 | −1,802,000 | −2,702,735 |
| (c) Tsy −40, no deal | 0 | −1,802,000 | −1,802,000 |

Loan PV effect = $-45{,}037 \times (\Delta y + \Delta s)$. Futures P&L = $530 \times 85 \times \Delta y_{Tsy}$ (short gains when yields rise).

**Check.** In (a) the hedge offsets the loan within rounding, because only Treasuries moved. In (b) the all-in rate rose 20 bp. Unhedged, the cost would have been \$900,735. Hedged, it is \$2.70m, three times larger.

**Decision consequence.** The futures hedge removes Treasury risk and keeps spread risk, and in a flight to quality the two move against each other. It also creates closing risk, as (c) shows. Better tools are: (i) a **rate lock** from the lender, which covers the all-in rate; (ii) a **forward-starting swap**, which removes swap-rate risk but leaves the swap spread and the credit spread; or (iii) hedging only the probability-weighted pipeline. Each has a cost. The futures hedge is cheapest to execute and has the most basis. A desk that hedges should write down which risk it keeps, and size the hedge to the probability that the deal closes. Problem 13.10 develops this.

#### Example 13.6 — Sizing the liquidity reserve for a two-year stress

**Given.** The §13.1 portfolio. Annual debt service: multifamily \$1.02m, industrial \$0.90m, hotel \$1.65m (floating, capped). A two-year stress [HYPOTHESIS]:

| | Year 1 | Year 2 |
|---|---|---|
| Multifamily NOI | −8% (\$2.024m) | −8% (\$2.024m) |
| Industrial NOI | −5% (\$1.710m) | −15%: one tenant leaves (\$1.530m) |
| Hotel NOI | −55% (\$1.080m) | −30% (\$1.680m) |
| Committed capital | Hotel PIP \$1.2m | none |

The hotel loan of \$22.0m matures at the end of year 2. In the stress, a new lender will lend 55% of value. Value is year-2 NOI capitalized at 9.50%. No distributions are made during the stress.

**Find.** The portfolio's net cash flow by year, the maturity gap, the reserve $R^*$, and its opportunity cost at a 4.0% reserve yield and an 11.0% target equity return.

**Solution.**

| | Year 1 | Year 2 |
|---|---:|---:|
| MF: 2.024 − 1.020 | +1.004 | +1.004 |
| Industrial: NOI − 0.900 | +0.810 | +0.630 |
| Hotel: NOI − 1.650 | −0.570 | +0.030 |
| PIP | −1.200 | 0 |
| **Net cash flow $X_t$** | **+0.044** | **+1.664** |

Hotel stressed value $= 1.680/0.095 = \$17.68\text{m}$. New loan $= 0.55 \times 17.68 = \$9.73\text{m}$. **Maturity gap** $= 22.00 - 9.73 = \$12.27\text{m}$.

Cumulative cash: end of year 1 +\$0.044m; end of year 2 $0.044 + 1.664 - 12.274 = -\$10.57\text{m}$. **$R^* = \$10.57\text{m}$.**

If the hotel had to stand alone with no support from the other assets: $0.570 + 1.200 - 0.030 + 12.274 = \$14.01\text{m}$.

Opportunity cost: $10.57 \times (0.11 - 0.04) = \$0.74\text{m}$ a year, or 1.77% a year on \$41.8m of equity.

**Check.** Operating shortfalls total less than \$1.8m over two years. More than 85% of the hotel's stand-alone need is the maturity.

**Decision consequence.** The reserve is dominated by one event, the hotel maturity, not by operations. Holding \$10.6m of cash costs about 1.8% a year of portfolio return. Alternatives that address the same event include: extend or refinance the hotel loan now, while the hotel is valued at \$30m (Chapter 10); buy a maturity extension option; or sell the hotel, which is also the asset contributing 45% of portfolio risk (Example 13.3). The reserve calculation turns a vague worry into a price: \$0.74m a year is the most the partnership should pay, per year, to eliminate the maturity risk by other means.

#### Example 13.7 — Portfolio leverage: where the debt sits matters for default, not for equity volatility

**Given.** A simplified two-asset portfolio: \$50m of multifamily ($\sigma = 10\%$) and \$50m of hotel ($\sigma = 20\%$), correlation 0.50. Total debt is fixed at \$50m. A refinancing in three years requires value of at least the loan divided by 0.75 (a 75% LTV test). Log values are normal with no drift in expected value: $\ln V_T \sim N(\ln V_0 - \tfrac12\sigma^2T,\ \sigma^2T)$, so $E[V_T] = V_0$ [HYPOTHESIS]. Allocations of the \$50m: A, 50%/50% LTV; B, 70% on MF and 30% on hotel; C, 30% on MF and 70% on hotel; D, equal distance to the refinancing threshold.

**Find.** Portfolio equity volatility. The probability that each asset fails the refinancing test, $P_i = N\big((\ln(\lambda_i/0.75) + \tfrac12\sigma_i^2T)/(\sigma_i\sqrt T)\big)$. The expected number of failed refinancings.

**Solution.** Portfolio asset volatility $= \text{portfolio\_volatility}([0.5,0.5],[0.10,0.20],\rho=0.5) = 13.23\%$. Equity volatility $= 13.23\% \times 100/50 = 26.46\%$ in **every** allocation.

| Allocation | MF LTV | Hotel LTV | P(MF fails) | P(hotel fails) | Expected failures |
|---|---:|---:|---:|---:|---:|
| A | 50% | 50% | 1.21% | 15.93% | 0.171 |
| B | 70% | 30% | 37.76% | 0.67% | 0.384 |
| C | 30% | 70% | 0.00% | 48.96% | 0.490 |
| D | 57.4% | 42.6% | 7.23% | 7.23% | 0.145 |

D solves for the split at which both assets are the same number of standard deviations from the threshold.

**Check.** In C the hotel at 70% LTV needs its value to stay above 93.3% of today's value for three years at 20% volatility, which is close to a coin flip. That is consistent with 48.96%.

**Decision consequence.** Portfolio leverage determines equity volatility. Asset-level leverage determines how many separate default and refinancing events the portfolio faces. With non-recourse, asset-level debt, each failure is a separate negotiation, loss of control, or foreclosure. Placing the most debt on the most volatile asset (C) is the worst allocation. It is also the one lenders and sponsors often drift into, because hotels are the assets that "need" leverage to hit return targets. The minimum-failure allocation puts more debt on the low-volatility asset, roughly in proportion to the inverse of volatility. Cross-collateralization changes the analysis, because the assets then fail together or not at all, and it should be priced as such.

#### Example 13.8 — The option to develop: a binomial tree

**Given.** The value today of the completed building on a site is \$30.0m. The construction cost if started today is \$27.0m, escalating 3% a year. The risk-free rate is 4.0% a year. The stabilized NOI yield forgone while waiting is $\delta = 5.5\%$. Value volatility is 20%, so $u = e^{0.20} = 1.2214$ and $d = 0.8187$. The option to build lasts two years (the entitlement expires). For simplicity, construction is treated as instantaneous, with $V$ and $K$ measured at the decision date.

**Find.** The NPV of building now, the option value, the value of waiting, the optimal policy, and the sensitivity to volatility.

**Solution.**

$q = (1 + 0.04 - 0.055 - 0.8187)/(1.2214 - 0.8187) = 0.4129$.

Value lattice (\$m) and option values (\$m):

| Node | $V$ | $K_t$ | Exercise $V - K_t$ | Option value | Action |
|---|---:|---:|---:|---:|---|
| t=2, up-up | 44.75 | 28.64 | 16.11 | 16.11 | build |
| t=2, up-down | 30.00 | 28.64 | 1.36 | 1.36 | build |
| t=2, down-down | 20.11 | 28.64 | −8.53 | 0 | let lapse |
| t=1, up | 36.64 | 27.81 | 8.83 | 8.83 | build |
| t=1, down | 24.56 | 27.81 | −3.25 | 0.54 | wait |
| t=0 | 30.00 | 27.00 | 3.00 | **3.81** | **wait** |

At the down node: $(0.4129 \times 1.3557 + 0.5871 \times 0)/1.04 = 0.538$. At t=0: $(0.4129 \times 8.8321 + 0.5871 \times 0.5383)/1.04 = 3.810$.

NPV now = \$3.00m. Option value = **\$3.81m**. Value of waiting = **\$0.81m**.

Sensitivity to volatility:

| $\sigma$ | Option value | Value of waiting | Build now? |
|---|---:|---:|---|
| 10% | \$3.00m | \$0 | yes |
| 15% | \$3.10m | \$0.10m | no |
| 20% | \$3.81m | \$0.81m | no |
| 25% | \$4.51m | \$1.51m | no |

Perpetual-option hurdle (continuous $r = 4\%$, $\delta = 5.5\%$): $V/K \ge 1.22$ at $\sigma = 10\%$; 1.65 at 20%; 1.92 at 25%. Today $V/K = 1.11$.

**Check.** At $\sigma = 10\%$ the tree's value equals NPV exactly, so building now is optimal. The perpetual hurdle says wait even at 10%, because it assumes the option never expires and the cost never escalates. Both features make waiting more valuable than in the two-year tree. The binomial tree reflects this site's actual terms.

**Decision consequence.** A developer who builds because "NPV is positive" gives up \$0.81m of option value at 20% volatility, 27% of the NPV. The policy is a trigger, not a date: build after an up move; wait after a down move. The practical value of the tree is that it gives the trigger in observable terms. At t=1, build if the completed value exceeds about \$27.8m plus the remaining option value, and the tree shows that an up-move to \$36.6m clears it. If the entitlement could be extended cheaply, the option would be worth more, and the perpetual hurdle shows the direction.

#### Example 13.9 — When doing nothing dominates: a pending competitive-supply vote

**Given.** A hotel developer controls a site. A city council will vote in 12 months on a competing 250-room convention-center hotel. If the competitor is denied (real-world probability $p = 0.65$), the completed value of the developer's hotel at t=1 is \$33.0m. If it is approved, value is \$24.0m. The building's NOI in year 1, if built now, is \$1.6m. The required unlevered return is $k = 8\%$. The construction cost today is \$27.0m, escalating 3% to \$27.81m in a year. Risk-free rate 4%. Treat the vote as market-priced uncertainty about value for the risk-neutral check [HYPOTHESIS; §13.4.9 explains the alternative].

**Find.** The value today of the completed building, the NPV of building now, the value of waiting under a real-world decision tree and under risk-neutral pricing, and the cost escalation at which building now becomes optimal.

**Solution.**

$V_0 = [0.65(33.0) + 0.35(24.0) + 1.6]/1.08 = 31.45/1.08 = \$29.120\text{m}$.

NPV now $= 29.120 - 27.000 = \$2.120\text{m}$.

*Wait, real-world tree.* At t=1, build only if denied: $33.0 - 27.81 = \$5.19\text{m}$. Value today $= 0.65 \times 5.19/1.08 = \$3.124\text{m}$.

*Wait, risk-neutral.* $q = [(1.04)(29.120) - 1.6 - 24.0]/(33.0 - 24.0) = 0.5206$. Value $= 0.5206 \times 5.19/1.04 = \$2.598\text{m}$.

Value of waiting: \$1.00m (real-world) or \$0.48m (risk-neutral). Both say wait.

*Break-even escalation.* Building now wins when $q(33.0 - 27.0(1+g_K))/1.04 < 2.120$, which gives $33.0 - 27.0(1+g_K) < 4.236$, or $g_K > 6.53\%$.

**Check.** The real-world tree discounts the option at the asset's 8% rate and overstates the value of waiting, as §13.4.9 predicts. The decision does not change.

**Decision consequence.** The project has a positive NPV of \$2.1m, and doing nothing for a year is worth more. Waiting avoids committing \$27m in the 35% of states where the competitor is approved and the completed hotel would be worth \$24.0m against a \$27.0m commitment. The developer pays for waiting with a year of forgone NOI and 3% cost escalation, and both are explicit in the tree. Waiting stops being optimal if costs escalate faster than about 6.5% a year, if a competitor could take the site's position (pre-emption, Grenadier, 1996), or if the entitlement lapses. **Doing nothing has positive strategic value when information is about to arrive, the commitment is irreversible, and the cost of delay is small relative to the loss avoided.** All three conditions can be checked.

#### Example 13.10 — The round-trip hurdle for capital recycling

**Given.** An asset worth \$40.0m with a \$20.0m loan, so equity before costs is \$20.0m. The owner's forward hold return on that equity is 9.0% a year [HYPOTHESIS]. Recycling into an asset of the same size and leverage costs: selling costs 1.5% of value (\$0.60m), prepayment 1.0% of the loan (\$0.20m), buyer costs 1.5% of the new value (\$0.60m), and new-loan fees 1.0% (\$0.20m). Assume returns accumulate in the position (no interim distributions) and that the two assets carry the same risk.

**Find.** The gross annual return the replacement must earn to match holding, over 3-, 5-, and 10-year horizons.

**Solution.** Total switching cost $= 0.60 + 0.20 + 0.60 + 0.20 = \$1.60\text{m}$, or $f = 8.0\%$ of equity. Equal terminal wealth requires $(1-f)(1+r_{alt})^T = (1+r_{hold})^T$, so

$$r_{alt} = \frac{1 + r_{hold}}{(1-f)^{1/T}} - 1.$$

| Horizon $T$ | Required $r_{alt}$ | Hurdle over holding |
|---|---:|---:|
| 3 years | 12.07% | +307 bp |
| 5 years | 10.83% | +183 bp |
| 10 years | 9.91% | +91 bp |

**Check.** The first-order approximation is $f/T$: 267 bp, 160 bp, and 80 bp. Compounding makes the true hurdle larger.

**Decision consequence.** An 8% round trip is paid once and recovered only over the life of the new investment. A recycling proposal must show an expected return advantage, at equal risk, of roughly 180 bp a year over five years. That is a very large edge relative to the precision of any real estate forecast. Recycling is justified when the advantage is large and well-founded: a material mispricing, a strategic exit from a market whose thesis has broken, or a risk reduction the investor values for its own sake, as with the hotel in Example 13.3. It is not justified by a difference in going-in yields.

---

### 13.6 CRE application: the partnership's capital-recycling memo

The examples connect into one memo.

1. **Multifamily: hold, do not refinance.** The forward levered IRR on equity at market is 11.21% against 9.01% for the industrial alternative (Example 13.1). The advantage depends on the 4.25% loan, and the break-even exit cap is 5.57%. The cash-out refinancing costs 27% on the incremental dollar (Example 13.2). Revisit if the bid rises enough to put the break-even exit cap below the partnership's own exit forecast, or if a buyer offers to assume the loan.
2. **Hotel: the portfolio's risk lives here.** It is 29% of value, 45% of risk, and creates a \$12.3m maturity gap in a plausible stress (Examples 13.3 and 13.6). The decision is between paying about \$0.74m a year in reserve drag, refinancing early, or selling. Relative value (Example 13.4) does not by itself justify a larger hotel allocation.
3. **Pipeline: lock, don't speculate.** Prefer a lender rate lock or a forward-starting swap, sized to the probability that each deal closes (Example 13.5).
4. **Leverage placement.** New debt should go on low-volatility assets first (Example 13.7).
5. **Land: wait, with a trigger** (Examples 13.8 and 13.9; Case I).

A REIT or fund faces the same arithmetic plus one constraint the partnership does not: distribution requirements and investor-level reporting. That is why public REITs often recycle through special dividends rather than reinvestment when they judge acquisition yields to be inadequate (§13.9).

#### Development versus stabilized investment

A development project is a stabilized asset plus a set of options and obligations: the construction-cost exposure, a lease-up risk, a financing-market exposure at completion, and the option value examined in §13.4.8. The **development spread**, yield on cost minus market cap rate, is the compensation for those risks. A 7.0% yield on cost against a 5.50% market cap is a 150 bp spread and a 27% margin on cost ($7.0/5.5 - 1$). Whether 150 bp is enough depends on the time to stabilization, the volatility of $V$ over that time, and what the developer could earn by buying a stabilized asset instead. The real-option framework adds one more question. Even if the spread is adequate, is *now* the best time to commit?

---

### 13.7 When the relationships fail

1. **Equity at market assumes the bid is real.** A broker's opinion of value, an unfunded LOI, or a bid conditional on financing is not a market price. If the bid has a 30% chance of failing, $E_M$ is an expectation, not a number. Chapter 1's leg-risk framework applies.
2. **Hold–sell IRR comparisons hide risk differences.** A hold IRR of 11% on a 54% LTV multifamily and 9% on a 55% LTV industrial are comparable. A hold IRR on a hotel and an alternative on a net-leased building are not, even at the same leverage. Compare unlevered first, then adjust for risk explicitly.
3. **Correlation estimates are unstable.** NOI correlations estimated from appraisal-based indices are smoothed (Chapter 2) and understate co-movement. Transaction-based correlations are noisy. Stress correlations should be set by judgment and tested, not estimated from calm periods.
4. **Cap-rate spreads can stay "wide" for a decade.** If the growth differential the market prices is correct, the spread never converges. Cap-rate mean reversion is a [HYPOTHESIS] to test against a long series, not an assumption.
5. **DV01 hedges are linear; loans and pipelines are not.** Deals fail, loan amounts change with appraisals, and spreads move with Treasuries in crises. The hedge ratio is a starting point.
6. **Reserves sized to one stress fail in a different stress.** The two-year scenario in Example 13.6 does not cover a three-year hotel disruption, an insurance-market shock, or simultaneous maturities. Run several stresses, and size to the worst one you are willing to survive.
7. **Real-option values are only as good as $\sigma$ and $\delta$.** Property-level volatility is not observable. Using 20% instead of 15% raised the value of waiting eightfold in Example 13.8. When the decision flips within the plausible range of $\sigma$, say so. That is an abstention signal, not a reason to pick the convenient number.
8. **Options can be pre-empted.** The binomial model assumes the option is proprietary. In a market where several landowners hold similar options, waiting invites competitors to build first. Grenadier (1996) shows that competition can produce overbuilding cascades in which owners exercise early. The value of waiting falls when your option is shared.
9. **Waiting can become a habit.** The real-option argument is not a license to wait indefinitely. It produces a trigger. An investor who has not written down the trigger is not holding an option. They are avoiding a decision.

---

### 13.8 A note on fund vintages

The timing question in this chapter also appears at the level of commingled private equity real estate funds. Funds raised near a market peak deploy capital at high prices; funds raised after a downturn deploy at low prices. Industry performance surveys group closed-end real estate fund returns by vintage year for exactly this reason. This chapter does not quote vintage-year returns for 2006–2010 because they were not verified against a primary dataset (*verification pending*; candidate sources: NCREIF/Townsend fund indices, Cambridge Associates real estate benchmarks, or Preqin). The mechanism is the same as in Example 13.9: a fund that must deploy within its investment period cannot wait, and the inability to wait has a cost that the real-option framework can price.

---

### 13.9 Historical episode: Equity Residential's 2015–2016 portfolio sale and its later re-entry

**Date and environment.** Late 2015. U.S. apartment REITs had experienced several years of rent growth, and private buyers were active. Equity Residential (EQR), a large apartment REIT, held assets across coastal urban markets and several other metros [INFERENCE from the filings cited below].

**What happened.**

* On 23 October 2015 EQR agreed to sell 72 operating properties containing 23,262 apartment units in five U.S. markets to affiliates of Starwood Capital Group for \$5.365 billion. The portfolio included 33 properties in South Florida, 18 in Denver, 10 in Washington DC, 8 in Seattle, and 3 in the Inland Empire [FACT; EQR press release dated 26 October 2015 and EQR Form 8-K; ch13-S01, ch13-S02; VERIFIED-SECONDARY via search excerpts of the primary documents].
* The price is about \$230,600 per unit [INFERENCE: \$5.365 billion / 23,262 = \$230,634; reproduced in `tests/test_ch13_examples.py`]. Secondary coverage reported a capitalization rate of about 5.5% and quoted an analyst estimate of the buyer's forward nominal cap rate at about 5.3% *(verification pending: the definitions differ and the figures have not been checked against the primary release)*.
* EQR closed the sale on 26 and 27 January 2016 [FACT; EQR Form 10-K for 2016 and 2018; ch13-S03, ch13-S04].
* EQR paid special dividends of \$8.00 per share/unit (about \$3.0 billion) on 10 March 2016 and \$3.00 per share/unit (about \$1.1 billion) on 14 October 2016, \$11.00 in aggregate [FACT; EQR Form 10-K for 2016 and 2017; ch13-S03, ch13-S05]. It used the majority of the remaining proceeds to reduce aggregate indebtedness so that the transaction was leverage-neutral [FACT; same sources].
* At the October 2015 announcement, management described the sale as narrowing the company's focus to its core high-density urban markets [FACT, paraphrased; ch13-S01, VERIFIED-SECONDARY]. The 2016 10-K referred to the difficulty of recycling a large amount of capital, \$6.8 billion, in a competitive acquisition market *(verification pending: the exact scope of the \$6.8 billion figure — total disposition proceeds or a subset — has not been confirmed against the filing's disposition table)*.
* In 2021 EQR acquired properties in Atlanta, Austin, Dallas/Fort Worth, and Denver, described in its 2021 10-K as "expansion markets". The 10-K described the Atlanta, Austin, and Dallas/Fort Worth acquisitions as a re-entry into those markets. 2021 acquisitions totaled 17 properties for about \$1.7 billion, of which about 82% was in the expansion markets. The company funded them largely by selling older properties in established markets, mainly in California [FACT; EQR Form 10-K for 2021 and Q3/Q4 2021 earnings materials; ch13-S06; VERIFIED-SECONDARY].

**What was knowable then.** The sale price, the markets exited, and the stated reasons were public at announcement. The future relative performance of Denver and South Florida apartments against coastal urban apartments was not knowable. Neither was the 2020 pandemic, which hit dense urban rental markets particularly hard.

**Interpretation 1: the capital-recycling decision in this chapter's terms.** EQR compared the forward return on equity at market in the sold markets with the return on redeploying into its target markets. It concluded that acquisitions at prevailing prices did not justify redeploying most of the proceeds. The reinvestment alternative it chose was to return capital to shareholders and reduce debt [INFERENCE from the use of proceeds]. This is the public-company version of "doing nothing has positive strategic value": when the alternative's IRR is inadequate, return the capital rather than force deployment. It also delivered the proceeds to shareholders, who could redeploy them as they chose.

**Interpretation 2: a market-selection call that later partly reversed.** EQR exited Denver in 2016 and was buying in Denver again in 2021, and it re-entered Atlanta, Austin, and Dallas/Fort Worth. One reading is that the 2015 market-selection thesis (concentrate in coastal high-density markets) was revised after evidence accumulated, notably during 2020–2021 [INFERENCE]. Another reading is that both decisions were correct relative to the prices available at the time: selling Denver at 2015–2016 pricing and buying at 2021 pricing may each have been sound if prices reflected different information [ALTERNATIVE INFERENCE]. This chapter does not compute the round trip's return, because doing so requires asset-level prices that were not verified.

**What the case establishes.** A large, well-informed owner treated a hold as a repurchase decision. It sold a large block at a price it judged attractive, did not force reinvestment, and kept leverage constant. Market selection was treated as a revisable judgment rather than a permanent identity.

**What it does not establish.** That the 2016 sale was value-creating relative to holding: the counterfactual returns are not documented here. That coastal urban apartments outperform or underperform other markets in general. That special dividends are generally superior to reinvestment.

**Strategies available then.** For a holder of EQR shares: accept the special dividend and redeploy it. For a private buyer: the Starwood side of the trade, buying a large diversified block at a single price, a liquidity-provision trade in Chapter 1's sense. For a competing REIT: bid for individual assets after the portfolio split, if the buyer resold pieces.

---

### 13.10 Decision exercise: the Tuesday agenda

Use the decision record template at `desk/investment_memos/decision_record_template.md`. Answer each of the six agenda items in §13.1, with a number and an invalidation criterion for each.

Specifically:

1. Sell, hold, or refinance the multifamily. State the break-even exit cap and what would change your answer, for example an assumable-loan bid.
2. Size the reserve under the Example 13.6 stress and under one additional stress of your own design. State which hotel action, if any, you would take and what it costs per year.
3. Recommend a pipeline hedge instrument and size. State the deal-closing probability you used.
4. State whether the 325 bp hotel–multifamily spread justifies any change in allocation, and what evidence would be needed.
5. State the land policy as a trigger (see Case I).
6. State what you will *not* do and why.

**Rubric** (full version in `problems/solutions/ch13_solutions.md`, §Decision exercise):

| Criterion | Weight | Full credit |
|---|---|---|
| Hold–sell on equity at market | 20% | Uses $E_M$, not cost basis; separates the financing effect from the asset effect; gives the break-even exit cap |
| Incremental cost of capital | 15% | Rejects the cash-out refinancing on its 27% marginal cost or proposes a supplemental instrument |
| Concentration and leverage | 20% | Identifies the hotel as the dominant risk; uses stress correlations; places debt by volatility |
| Liquidity | 20% | Sizes the reserve with the maturity included; prices the drag; compares it with alternatives |
| Hedging | 15% | Identifies basis and closing risk; sizes to the closing probability; prefers an all-in lock where available |
| Abstention and triggers | 10% | Names at least one action not taken and a measurable trigger for revisiting it |

There is no single correct allocation. A recommendation to sell the hotel and hold everything else is defensible. So is a recommendation to refinance the hotel early and hold a smaller reserve.

---

### 13.11 Frequent analytical errors

1. **Using IRR since inception to decide whether to hold.** It is sunk. Use the forward IRR on equity at market.
2. **Comparing going-in yields across sectors and calling the difference "accretion".** $c = k - g$. A higher cap rate is not a higher return unless risk and growth are equal.
3. **Ignoring the financing in a hold–sell.** Below-market debt is an asset of the hold. Prepayment is a cost of the sale. Assumability changes the bid.
4. **Quoting the headline rate of a refinancing instead of the marginal cost.** Compute the IRR of the incremental flows.
5. **Measuring diversification with calm-period correlations.** Run the stress correlation.
6. **Hedging Treasuries and believing the loan rate is hedged.** Credit spreads are a separate risk and often move the other way.
7. **Hedging deals that may not close at 100% of notional.** A failed deal turns the hedge into a naked position.
8. **Sizing a reserve without the maturity schedule.** Operating shortfalls are usually small; maturities are not.
9. **Confusing portfolio leverage with asset leverage.** Equity volatility depends on the former. The number of defaults depends on the latter.
10. **Building because NPV is positive.** With irreversibility and uncertainty, NPV > 0 is necessary but not sufficient.
11. **Discounting option payoffs at the asset's required return.** It overstates or understates the option's value depending on the direction. Use risk-neutral pricing, or at least check the decision against it.
12. **Treating "wait" as a decision without a trigger.** An option without an exercise rule is not being managed.

---

### 13.12 Connections to other chapters

* Chapter 1: liquidity provision, leg risk, and the "do nothing" alternative.
* Chapter 2: appraisal smoothing biases the correlations in Example 13.3.
* Chapter 6: DV01, duration, and the cap-rate/Treasury spread used in Example 13.5.
* Chapter 8: supply pipelines and the growth differential in Example 13.4.
* Chapter 9: residual land value and DCF, used in Case I.
* Chapter 10: loan sizing (`cre.max_loan`), yield maintenance, and refinancing gaps (Examples 13.2 and 13.6).
* Chapter 11: hotel operating leverage, which is why the hotel dominates portfolio risk.
* Chapter 12: maturity walls and forced sellers, the counterparties to a liquidity reserve.
* Chapter 18: interest-rate caps and option pricing; the Black–Scholes counterpart of §13.4.8.
* Chapter 21: position sizing and ruin; Example 13.6 is a survival constraint.
* Case F: the hotel-versus-Treasury allocation, which is opportunity-cost analysis with taxes.
* Case I: the development land option, which extends Examples 13.8 and 13.9.

---

### 13.13 One-page reference sheet

| Quantity | Formula |
|---|---|
| Equity at market | $E_M = V_0(1-s) - B_0 - PP$ |
| Simplified yield maintenance | $PP = B(r_L - y)\,a_{\overline{n}|y}$ |
| Price supported by equity | $P = E_M/(1 + b - \lambda)$ |
| Hold IRR | IRR of $[-E_M;\ NOI_t - DS_t;\ NOI_{T+1}(1-s)/c_T - B_T]$ |
| Marginal cost of a cash-out | IRR of $[C_0;\ -(L'r' - Br_L);\ -(L'-B)]$, lender side |
| Portfolio volatility | $\sigma_p^2 = \sum\sum w_iw_j\sigma_i\sigma_j\rho_{ij}$ |
| Risk contribution | $RC_i = w_i(\Sigma w)_i/\sigma_p$ |
| Portfolio equity volatility | $\sigma_E = \sigma_p \sum V_i / E$ |
| Cap rate and growth | $c = k - g$; $c_A - c_B = \Delta k - \Delta g$ |
| Loan DV01 | $\approx L \times 0.0001 \times a_{\overline{n}|r}$ |
| Futures contracts | $N = DV01_{loan}/DV01_{fut}$ |
| Hedged P&L | $-DV01_L(\Delta y + \Delta s) + N\,DV01_F\,\Delta y$ |
| Reserve | $R^* = \max(0, -\min_\tau \sum_{t\le\tau}(X_t - M_t))$ |
| Reserve drag | $R^*(k_E - r_f)$ |
| Risk-neutral probability | $q = (1 + r - \delta - d)/(u - d)$ |
| Option recursion | $F_t = \max(V_t - K_t,\ [qF^u + (1-q)F^d]/(1+r))$ |
| Value of waiting | $F_0 - \max(V_0 - K_0, 0)$ |
| Perpetual hurdle | $V/K \ge \beta/(\beta-1)$ |
| Refinance distress probability | $N\big((\ln(\lambda/\lambda_{max}) + \tfrac12\sigma^2T)/(\sigma\sqrt T)\big)$ |

**Questions before any trade.** What is my equity at market? What is the best alternative at the same risk? What does the incremental capital cost? Which asset dominates portfolio risk, in a stress? Which risk does my hedge leave me with? How much cash do I need if the worst maturity arrives in the worst year? What does waiting cost, and what does it buy?

---

### References for this chapter

Source entries with verification status are in `references/sources_ch13.md`.

* Cox, J. C., Ross, S. A., and Rubinstein, M. (1979). "Option Pricing: A Simplified Approach." *Journal of Financial Economics*, 7(3), 229–263.
* Dixit, A. K., and Pindyck, R. S. (1994). *Investment under Uncertainty*. Princeton, NJ: Princeton University Press.
* Grenadier, S. R. (1996). "The Strategic Exercise of Options: Development Cascades and Overbuilding in Real Estate Markets." *Journal of Finance*, 51(5), 1653–1679.
* McDonald, R., and Siegel, D. (1986). "The Value of Waiting to Invest." *Quarterly Journal of Economics*, 101(4), 707–727.
* Titman, S. (1985). "Urban Land Prices under Uncertainty." *American Economic Review*, 75(3), 505–514.
* Equity Residential. Press release, 26 October 2015, "Equity Residential Announces Agreement to Sell 23,000 Apartment Units to Starwood Capital Group for \$5.365 Billion," and Form 8-K exhibit 99.1 (SEC EDGAR, CIK 906107).
* Equity Residential. Forms 10-K for fiscal years 2016, 2017, 2018, and 2021 (SEC EDGAR, CIK 906107).
* CME Group. 10-Year U.S. Treasury Note futures contract specifications. https://www.cmegroup.com/markets/interest-rates/us-treasury/10-year-us-treasury-note.contractSpecs.html


\newpage
