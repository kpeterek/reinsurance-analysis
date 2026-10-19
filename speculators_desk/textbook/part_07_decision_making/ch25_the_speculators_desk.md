# Chapter 25 — The Speculator's Desk

> **Status:** Complete (v1.0). Numerical examples are reproduced in `tests/test_ch25_examples.py`. Problems are in `problems/questions/ch25_problems.md` and solutions in `problems/solutions/ch25_solutions.md`. Drills D215–D220 are in `training/daily_drills/drill_bank_ch25.json`. Worked desk documents: `desk/daily_blotter/example_filled_blotter.md` and `desk/investment_memos/example_ic_memo.md`. Four historical details are marked *(verification pending)*: the participants in the New York Fed's daily conference call, the edition date of one source, the date the FOMC began announcing decisions, and bibliographic details for two scoring-rule references. None of them affects a calculation.

## Learning objectives

After this chapter you should be able to:

1. Design a daily and weekly routine as a **time budget**, and reallocate hours using an explicit estimate of the value of information per hour.
2. Grade any information source on eight attributes: timeliness, reliability, bias, revisions, cost, coverage, relevance, and whether it is already widely known. Explain why the last attribute governs whether the source can produce an edge at all.
3. State the mechanics of the CFTC Commitments of Traders (COT) reports: what date the positions describe, when they are released, which trader categories each report uses, and what the reports cannot tell you.
4. Combine conflicting signals with likelihood ratios, and show how double-counting correlated sources produces false confidence.
5. Keep the desk's paper instruments: blotter, economic briefing, historical reference note, deal memo, trade ticket, risk register. Fill each one so that it supports a later calculation.
6. Attribute weekly P&L to factors (rates, equity beta, idiosyncratic, carry, costs), and aggregate DV01, beta-adjusted equity delta, and CRE equity at risk into a single risk register.
7. Run a postmortem that separates process from outcome. Analyze an error log. Compute a Brier score from a decision journal with `sdesk.stats.brier_score`, and decompose it into reliability and resolution.
8. Compare a 1987-style desk with a modern one on speed, error rates, and cost, without romanticizing either.

---

## 25.1 Opening investment problem: the Monday after a bad week

You run the same \$40 million discretionary real estate and markets account introduced in Chapter 1. All positions and prices in this chapter are [HYPOTHESIS], constructed for teaching, unless a source is cited. They are not market data for any date.

On Monday morning your book holds:

| Position | Size | Note |
|---|---|---|
| Short 10-year Treasury note futures | 40 contracts | DV01 assumed \$85 per contract |
| Long 5-year Treasury note | \$10.0 million face | 4.00% coupon, priced at par |
| Pay-fixed 5-year interest-rate swap | \$15.0 million notional | Hedges the floating-rate hotel loan |
| Long E-mini S&P 500 futures (ES) | 10 contracts | \$50 multiplier |
| Long listed REIT basket | \$2.0 million | Beta to ES assumed 1.1 |
| Select-service hotel (owned) | \$30.0 million value | \$18.0 million floating-rate loan |
| Industrial building (owned) | \$24.0 million value | \$14.4 million fixed-rate loan |

Last week the book lost \$59,250. Your partner asks three questions before Thursday's investment committee:

1. *Where did the loss come from, and was any of it a surprise?*
2. *What is our largest risk right now, measured in dollars, and is it the one we talk about most?*
3. *You spend 50 hours a week on this book. Which of those hours changed a decision?*

On the same morning four signals arrive about the industrial market where you are bidding on a second building. A transaction database shows two recent sales at cap rates near 6.25%. Two lender term sheets show wider spreads and lower proceeds than a quarter ago. A sell-side note calls cap rates "stable". The special-servicing rate on CMBS loans backed by the property type has risen for three months running. Separately, the weekly COT report shows leveraged funds holding a large net short in 10-year note futures, and the consumer price index (CPI) is released on Wednesday.

None of these questions needs a new model. Each needs a **process** that turns information into a dated, written, checkable decision and, later, into an honest score. This chapter builds that process, instrument by instrument, and costs it in hours and dollars. Section 25.14 returns to Thursday's decision.

---

## 25.2 Economic intuition: a desk is a production function for decisions

A desk turns three inputs into decisions: **information**, **analyst hours**, and **risk capital**. Every chapter so far has treated the decision. This one treats the production function.

**Information has a price, a decay rate, and a degree of publicity.** A Treasury yield is free, instant, and known to everyone. Its value to you lies only in what you do with it faster or differently. A rent roll from a seller is costly to obtain, decays over months, and is known to a handful of bidders. A lender term sheet is free to request and costs an afternoon of calls, but the signal it carries about credit availability is not in any database for weeks. The source that can produce an edge is rarely the one that feels most informative. It is the one whose content is **relevant, reliable, and not yet widely known**. Section 25.6 grades sources on that basis.

**Analyst hours are the binding constraint.** A 50-hour week is 3,000 minutes. Routine tasks expand to fill it: reading research, watching screens, answering email. The question a time budget asks is the same one a capital budget asks. *What is the marginal return on the next hour, and where is it highest?* Example 25.1 puts numbers on this.

**Writing is a commitment device.** A forecast that is not written down before the outcome cannot be scored. A risk that is not on the register is not managed. An error that is not logged recurs. Writing by hand has one real advantage: it is slow. That slowness forces selection, so a handwritten blotter tends to hold the twelve numbers that matter rather than the two hundred a screen displays. It also has real costs: transcription errors, no search, and no audit of arithmetic. Section 25.10 measures both. The reader's preference for pen and paper is useful when it acts as a filter and harmful when it becomes a ritual.

**Scoring closes the loop.** A desk that does not score its forecasts cannot tell skill from luck, even over years (Chapter 1, §1.2; Chapter 20). The Brier score is the simplest proper scoring rule for probability forecasts. Its decomposition separates two different failures. *Reliability* measures whether your 70% forecasts come true 70% of the time. *Resolution* measures whether your forecasts discriminate between events that happen and events that do not. A forecaster can be perfectly calibrated and useless by saying 50% to everything. Example 25.5 works through both.

**The process is the product.** A repeatable process does not guarantee good outcomes. It makes outcomes **interpretable**. When a deal loses money, the decision record says what you expected, the risk register says what you knew about exposure, and the error log says whether the loss came from judgment or from arithmetic. Without those documents, a postmortem is a story told after the fact.

---

## 25.3 Technical definitions

| Term | Definition |
|---|---|
| Blotter | A dated, handwritten or printed record of market levels, the day's calendar, positions, and changes of view, filled before the open and closed after the close |
| Economic briefing | A one-page note on a scheduled release: consensus, prior, revision, surprise, market reaction, and the implication for the book |
| Historical reference note | A short, sourced file on a past episode, with every number labeled by evidence status, kept for comparison with current events |
| Deal memo / IC memo | The written recommendation for a CRE transaction: thesis, valuation, capital structure, scenarios, risks, invalidation, walk-away terms |
| Trade ticket | The pre-trade record of a liquid position: size, multiplier, entry, invalidation, loss at invalidation, gap loss, approver |
| Risk register (risk ledger) | A position-by-position table of factor exposures (DV01, beta-adjusted equity delta, FX, credit, CRE value), stress losses, liquidity, and financing risk, with portfolio totals |
| DV01 | Dollar value of one basis point. In this chapter, **position DV01 is the P&L for a +1 bp parallel rise in yields**: positive for a short-duration position, negative for a long one |
| Beta-adjusted equity delta | $\sum_j \beta_j \times \text{market value}_j$: the dollar exposure to a 1-unit move in the reference index, scaled by 100 for a 1% move |
| CRE equity at risk | Loss of equity value under a stated cap-rate and NOI shock, before any change in debt |
| P&L attribution | Decomposition of realized P&L into factor contributions plus a residual (idiosyncratic) term. The terms must sum to the total |
| Decision journal | A dated record of forecasts and decisions, written before outcomes and never edited (addenda only) |
| Brier score | $BS = \frac{1}{N}\sum_{i}(f_i - o_i)^2$ for probability forecasts $f_i$ and 0/1 outcomes $o_i$. Lower is better. Always forecasting 0.5 scores 0.25 |
| Reliability (calibration) term | $\frac{1}{N}\sum_k n_k(f_k-\bar o_k)^2$: the penalty for forecasts whose stated probability differs from their observed frequency |
| Resolution term | $\frac{1}{N}\sum_k n_k(\bar o_k-\bar o)^2$: the credit for forecasts that separate events with different observed frequencies |
| Error log | A record of each error with its category (arithmetic, units, timing, concept, judgment, data), the correct method, and the date it was repeated correctly |
| Postmortem | A written review after a position closes. It compares the outcome with the ex-ante distribution and grades the process separately from the result |
| Already widely known | Information that is public, free or cheap, and processed by many participants within minutes. It can still matter for risk management, but it rarely supports an informational edge |
| COT report | The CFTC's weekly Commitments of Traders reports on open interest held by reportable traders, by trader category, for futures and options markets |

---

## 25.4 Equations and derivations

### 25.4.1 P&L attribution

For a position with market value $MV_j$, beta $\beta_j$ to a reference index whose return is $R_m$, and actual return $R_j$:

$$P\&L_j = MV_j R_j = \underbrace{MV_j\beta_j R_m}_{\text{systematic}} + \underbrace{MV_j(R_j - \beta_j R_m)}_{\text{idiosyncratic}}.$$

For a futures position, $P\&L = \text{side} \times (F_1 - F_0) \times \text{multiplier} \times \text{contracts}$ (style guide §4). For a rates position with position DV01 $D$ (P&L per +1 bp) and a yield change $\Delta y$ in basis points, the first-order rates P&L is $D \times \Delta y$. Adding carry $C$ and costs $K$:

$$P\&L_{\text{book}} = \sum_{\text{rates}} D\,\Delta y + \sum_{\text{equity}} MV_j\beta_j R_m + \sum MV_j(R_j-\beta_jR_m) + C - K.$$

The identity is exact by construction. The residual is everything the factors did not explain. A large residual means either a missing factor or a genuine idiosyncratic event. The attribution cannot tell you which.

### 25.4.2 Aggregating the risk register

Rates exposures add once they are expressed in the same sign convention and the same yield change. A parallel shift is assumed. Curve exposures need key-rate DV01s (Chapter 6):

$$D_{\text{book}} = \sum_i D_i.$$

Equity exposures add after beta adjustment: $\Delta_{\text{eq}} = \sum_j \beta_j MV_j$, so a 1% index move changes value by about $0.01\,\Delta_{\text{eq}}$.

For a CRE asset with NOI $N_0$, cap rate $c_0$, debt $L$, and a stress that moves NOI by $g$ and the cap rate to $c_1$:

$$V_1 = \frac{N_0(1+g)}{c_1},\qquad \text{Equity at risk} = V_0 - V_1,\qquad \frac{\Delta E}{E_0} = \frac{V_1 - V_0}{V_0 - L}.$$

The leverage multiplier $V_0/(V_0-L)$ converts an asset-value change into an equity change. At 60% LTV it is 2.5. The three totals are not additive into one number without a joint scenario, because they are measured in different units: dollars per basis point, dollars per 1%, and dollars under a stated shock. A **joint stress** fixes one move for each factor and adds the dollar results.

### 25.4.3 The Brier score and its decomposition

Group $N$ forecasts into $K$ bins in which every forecast in bin $k$ equals $f_k$. Bin $k$ holds $n_k$ forecasts with observed frequency $\bar o_k$, and the overall frequency is $\bar o$. Within bin $k$, $\sum_{i\in k}(f_k - o_i)^2 = n_k(f_k-\bar o_k)^2 + n_k\bar o_k(1-\bar o_k)$. This holds because $o_i \in \{0,1\}$, so the within-bin variance of outcomes is $\bar o_k(1-\bar o_k)$. Summing and using $\sum_k n_k\bar o_k(1-\bar o_k) = N\bar o(1-\bar o) - \sum_k n_k(\bar o_k - \bar o)^2$ gives Murphy's decomposition:

$$BS = \underbrace{\frac1N\sum_k n_k(f_k-\bar o_k)^2}_{\text{reliability}} - \underbrace{\frac1N\sum_k n_k(\bar o_k-\bar o)^2}_{\text{resolution}} + \underbrace{\bar o(1-\bar o)}_{\text{uncertainty}}.$$

The decomposition is exact when every forecast in a bin is identical, as in this chapter's examples. With continuous forecasts binned into ranges, a small within-bin term appears. The **Brier skill score** against the climatological forecast $\bar o$ is $BSS = 1 - BS/[\bar o(1-\bar o)]$.

### 25.4.4 Conflicting signals: likelihood ratios and double counting

For hypothesis $H$ with prior $p_0$ and signals $s_1,\dots,s_m$ that are **conditionally independent given $H$ and given not-$H$**:

$$\frac{p_m}{1-p_m} = \frac{p_0}{1-p_0}\prod_{j=1}^m LR_j,\qquad LR_j = \frac{P(s_j\mid H)}{P(s_j\mid \neg H)}.$$

This is `sdesk.stats.likelihood_ratio_update`. If two signals share a cause, such as two lenders reacting to the same CMBS data, their joint likelihood ratio is less than the product of their separate ratios. In the limit of perfect dependence it equals one of them. Multiplying correlated likelihood ratios is the most common way a desk manufactures conviction from repetition.

### 25.4.5 The value of an hour and the cost of a transcription

If an hour spent on activity $a$ changes a decision with probability $\pi_a$, and the change is worth $v_a$ when it happens, the expected value of that hour is $\pi_a v_a$. Reallocate hours toward the highest $\pi_a v_a$ until marginal values equalize. Both inputs are guesses, so the result is a hypothesis to test with a log, not an optimization to trust.

If each hand-copied number is wrong with probability $q$, independently, then a sheet of $n$ numbers contains at least one error with probability

$$P(\ge 1\ \text{error}) = 1-(1-q)^n.$$

An independent check that catches a fraction $h$ of errors reduces the per-number rate to $q(1-h)$.

---

## 25.5 The daily routine and the time budget

A routine has two purposes: to make sure nothing important is missed, and to protect the hours in which analysis happens. The schedule below is [HYPOTHESIS], a template for a one-person book with both liquid and CRE positions, U.S. Eastern time.

| Time | Block | Output | Minutes |
|---|---|---|---|
| 6:45–7:30 | Pre-open blotter: overnight levels, calendar, positions | Blotter §§1–2, 5 | 45 |
| 7:30–8:15 | Economic briefing on today's release(s); read only notes that change a number | Release sheet | 45 |
| 8:15–8:45 | Risk check: distance to invalidation, liquidity, maturities | Risk register update | 30 |
| 8:45–12:00 | Deep work: underwriting, diligence, lender and broker calls | Deal memo sections, call notes | 195 |
| 12:00–12:30 | Midday blotter: what changed, levels | Blotter §4 | 30 |
| 12:30–15:30 | Deep work or meetings | | 180 |
| 15:30–16:15 | Close: P&L, attribution flags, tickets reconciled | P&L line, ticket file | 45 |
| 16:15–16:45 | Decision journal and error log | Journal entries | 30 |

Two rules make the routine work. First, the **deep-work blocks are protected**. Screens are off unless a position is within one gap move of its invalidation level. Second, each block ends in a **document**. A block that produces no document, such as "reading" or "monitoring", is where hours disappear.

### Example 25.1 — A time budget and the value of an hour

**Given.** A 50-hour week. You estimate, for one hour of each activity, the probability $\pi$ that it changes a decision and the value $v$ of that change. All estimates are [HYPOTHESIS].

* **Rent-roll and T-12 audit** on the \$24 million industrial bid. Four hours of audit have a 10% chance of finding a \$60,000 overstatement of NOI. The bid is priced at a 6.5% cap rate.
* **Sell-side morning notes.** One hour of reading has a 2% chance of changing a \$5 million macro position by enough to be worth 0.5% of that position.

**Find.** The expected value per hour of each activity, and whether to move hours between them.

**Solution.**

*Audit.* An NOI overstatement of \$60,000 capitalized at 6.5% is a value error of
$$\frac{60{,}000}{0.065} = \$923{,}077.$$
Expected value of four hours $= 0.10 \times 923{,}077 = \$92{,}308$, or **\$23,077 per hour**.

*Morning notes.* A change worth $0.005 \times 5{,}000{,}000 = \$25{,}000$ occurs with probability 0.02 per hour, so the expected value is $0.02 \times 25{,}000 =$ **\$500 per hour**.

The ratio is about 46 to 1.

**Check.** Reverse the audit calculation. At \$23,077 per hour the four hours are worth \$92,308. That is 10% of \$923,077, and \$923,077 × 0.065 returns the \$60,000 NOI error.

**Decision consequence.** Cut morning-note reading to what the economic briefing requires, about 15 minutes a day, and move the freed 3–4 hours a week into diligence on live bids. The comparison is robust even if the audit probability is overstated tenfold: \$2,308 per hour still beats \$500. The guess that would reverse it is a sell-side note that regularly changes positions, and the journal can test that directly. Log, for four weeks, every decision changed and the hour that changed it. The time budget is a hypothesis until that log exists.

**Reproduce:** `tests/test_ch25_examples.py::test_example_25_1`

---

## 25.6 Market intelligence and source discipline

### 25.6.1 The eight attributes

Every source is graded on eight attributes before its content is used:

1. **Timeliness**: the lag between the event and your receipt.
2. **Reliability**: the probability the content is accurate as stated.
3. **Bias**: a systematic direction in the content, arising from the source's incentives.
4. **Revisions**: whether and how much the figure changes after first publication.
5. **Cost**: money and analyst time.
6. **Coverage**: how much of the relevant universe the source observes.
7. **Relevance**: how directly it bears on the cash flows, discount rates, or financing of your positions.
8. **Already widely known**: whether many participants have processed it within minutes or hours.

The eighth attribute decides whether a source can support an *informational* edge. A widely known, highly reliable source, such as a payroll release, is indispensable for risk management. Any edge from it comes from interpretation, speed of execution, or positioning, not from possession. A private, noisy source, such as a lender's verbal quote, can carry information that is not in prices, but it must be discounted for reliability and bias.

### 25.6.2 Graded table

Grades run from **A** (best for the desk) to **D** (worst). The grades are the author's teaching assessments [HYPOTHESIS], not measured statistics. Where a mechanism is cited, the citation is given in §25.6.3. "Bias: A" means little systematic bias. "Revisions: A" means the figure is never revised. "Cost: A" means free.

| Source | Timeliness | Reliability | Bias | Revisions | Cost | Coverage | Relevance (macro/CRE book) | Already widely known? |
|---|---|---|---|---|---|---|---|---|
| Public data releases (payrolls, CPI, GDP) | B (weeks after reference period; instant on release) | A | A | C (payrolls, GDP revised) | A | A (national) | B | **Yes**, within seconds |
| Consensus estimates | A (before release) | B | B (herding toward prior) | n/a | A–B | B | B (defines the surprise) | **Yes** |
| Sell-side research | A–B | B | C (franchise, coverage and banking incentives) | Silent: views change without a revision log | B (bundled) | B (covered names only) | B | **Mostly**: distributed to many clients |
| Earnings calls | B (quarterly) | B (management framing) | C (management incentive to reassure) | Restated in later filings | A | C (one firm) | B for REIT/lender read-through | **Yes**, within hours |
| Regulatory filings (10-K, 10-Q, 8-K, call reports) | C (weeks after quarter-end) | A (legal liability) | B (permitted framing) | Restatements possible | A | B (public registrants) | B | **Partly**: public, but footnotes are read by few |
| Property operating statements (T-12, rent roll) | B (monthly, if obtained) | C (seller-prepared, unaudited) | D (seller incentive to overstate) | Frequent adjustments in diligence | C (access requires a deal) | D (one asset) | **A** | **No**: few bidders |
| Lender term sheets | A (current) | B (indicative, not committed) | B (lenders posture) | Re-trade risk before commitment | B (hours of calls) | C (lenders you call) | **A** for financing | **No**: private, and reaches databases with a lag |
| Transaction databases | C (closed deals, reported with lag) | B (verified sales) to C (reported terms) | C (selection: only assets that traded) | Backfilled as deals are reported | C (subscription) | B for institutional deals, C for small | A | **Partly**: subscribers see the same comps |
| COT reports | C (Tuesday positions, Friday release) | A (regulatory reporting) | B (category definitions are coarse) | Rare corrections | A | B (reportable traders only) | C (positioning, not value) | **Yes**: free, followed by many |
| Economic calendars | A | A for dates; B for times under holiday or shutdown changes | A | Schedules change | A | A | B (sets the risk windows) | **Yes** |
| Central-bank communication | A (statements); C (minutes three weeks later) | A | B (institutional messaging) | Speeches can be walked back | A | A | A for rates and financing | **Yes**, instantly |
| Industry reports (brokerage, data vendors) | C (quarterly) | C | C (brokerage incentive to support activity) | Methodology changes | B–C | B | B | **Partly** |
| Market prices (yields, futures, REITs, credit) | A (real time) | A | A (but can be distorted by forced flows) | None, though marks of illiquid assets are revised | A–B | A for liquid markets | A | **Yes** |
| Credit and financing indicators (spreads, CMBS delinquency, special servicing, senior loan officer surveys) | B–C | B | B | Some series revised | B | B | **A** for CRE | **Partly**: public, under-processed by CRE owners |

Three patterns stand out. The sources rated **A for relevance and "No" for widely known** are property statements and lender term sheets. They are also the costliest and least reliable. That is not a coincidence. In equilibrium, cheap, reliable, relevant information is already in prices. The second pattern is that **bias and revisions are different problems**. Revisions are noise that will be corrected. Bias is a direction that will not. The third is that **market prices are the most timely and the least informative about *why***. They are the scoreboard, not the explanation.

### 25.6.3 Mechanics worth getting exactly right

**COT reports.** The CFTC's Commitments of Traders reports describe open interest held by reportable traders as of the **close of business on Tuesday**. The data take about three days to process, and the reports are generally released on **Friday at 3:30 p.m. Eastern time**. Federal holidays can delay release by one or two days [FACT; CFTC, *Commitments of Traders* release-schedule and description pages, ch25-S01, VERIFIED-SECONDARY]. The CFTC publishes futures-only and futures-and-options-combined versions. A market appears in a report when 20 or more traders hold positions at or above the reporting levels the CFTC sets [FACT; CFTC explanatory notes, ch25-S02, ch25-S03, VERIFIED-SECONDARY]. The trader categories differ by report:

| Report | Categories | Typical use |
|---|---|---|
| Legacy | Commercial; non-commercial; non-reportable | Long history, coarse split |
| Disaggregated (physical commodities; first published 4 September 2009) | Producer/Merchant/Processor/User; Swap Dealers; Managed Money; Other Reportables | Energy, metals, agriculture |
| Traders in Financial Futures (TFF) | Dealer/Intermediary; Asset Manager/Institutional; Leveraged Funds; Other Reportables | Treasury, equity-index, currency futures |

[FACT; CFTC explanatory notes for the disaggregated and TFF reports, ch25-S02, ch25-S03, VERIFIED-SECONDARY.]

What the COT cannot tell you matters as much as what it can. [INFERENCE] (i) By release, the positions are three days old, and longer after a holiday. (ii) A leveraged-fund short in Treasury futures may be one leg of a cash-futures basis trade that is long cash Treasuries. The net rates exposure of that trader is then near zero, and the COT shows only the futures leg. (iii) Categories are assigned by trader type, not by motive. (iv) Because the report is free and followed widely, an "extreme" reading is already widely known. That is why the table grades COT relevance C. Positioning data can describe the fuel for a squeeze. It does not tell you the timing or the catalyst.

**Public data releases and revisions.** Payroll employment estimates are revised as more survey responses arrive, and an annual benchmark compares the March survey estimate with a fuller administrative count [FACT; BLS benchmark notices and Atlanta Fed review of payroll revisions, ch25-S04, ch25-S05, VERIFIED-SECONDARY]. A desk that compares today's surprise with an unrevised prior month, rather than the revised figure, mismeasures the surprise. The economic briefing template therefore has a "Prior (revised)" column.

**Central-bank communication.** The FOMC releases the minutes of regularly scheduled meetings three weeks after the date of the policy decision [FACT; Federal Reserve FOMC calendar and FAQ pages, ch25-S06, VERIFIED-SECONDARY]. The statement is therefore known at once, and the minutes add color with a three-week lag. By the time the minutes appear, the market has already priced the statement and the press conference.

### Example 25.2 — Weekly P&L attribution

**Given.** Last week, from the book in §25.1 (all [HYPOTHESIS]):

* 10-year yield: +12 bp. Short 40 TY futures; position DV01 \$3,400 per +1 bp ($40 \times \$85$).
* ES: 5,800 → 5,713 (−1.5%). Long 10 contracts, \$50 multiplier.
* REIT basket: \$2,000,000, beta 1.1 to ES, actual return −3.2%.
* Private CRE: no mark change (quarterly appraisal). Accrued net income \$9,600.
* Commissions and financing: \$2,150.
* The 5-year note and the swap were bought at the end of the week and contributed nothing.

**Find.** Total P&L and its attribution to rates, equity beta, idiosyncratic, carry, and costs.

**Solution.**

*Rates:* $D\,\Delta y = 3{,}400 \times 12 = +\$40{,}800$.

*ES:* $(+1)(5{,}713 - 5{,}800)(50)(10) = -87 \times 500 = -\$43{,}500$.

*REIT total:* $2{,}000{,}000 \times (-0.032) = -\$64{,}000$.
Systematic: $2{,}000{,}000 \times 1.1 \times (-0.015) = -\$33{,}000$.
Idiosyncratic: $-64{,}000 - (-33{,}000) = -\$31{,}000$.

*Carry* $+\$9{,}600$; *costs* $-\$2{,}150$.

| Factor | P&L (\$) |
|---|---|
| Rates (short duration) | +40,800 |
| Equity beta (ES −43,500; REIT systematic −33,000) | −76,500 |
| REIT idiosyncratic | −31,000 |
| Carry (CRE income) | +9,600 |
| Costs | −2,150 |
| **Total** | **−59,250** |

**Check.** By position: $40{,}800 - 43{,}500 - 64{,}000 + 9{,}600 - 2{,}150 = -59{,}250$. The factor total agrees.

**Decision consequence.** Three findings, each leading to an action. (1) **Equity beta is the book's real directional exposure.** Combined beta exposure was about \$5.1 million, so a 1.5% index fall cost \$76,500. The short-duration position offset half of that only because yields happened to rise while equities fell. That correlation is not reliable. In the 2022-style regime the two moves coincide; in a growth scare they diverge [INFERENCE; Chapter 6]. Do not describe the rates short as an equity hedge on the register. (2) **The REIT idiosyncratic loss of 1.55% is within one assumed weekly idiosyncratic standard deviation of 2%** [HYPOTHESIS], about \$40,000. It does not by itself call for action, but it is logged. (3) **The CRE mark is stale.** Listed REITs fell 3.2% while the private assets were marked flat. Chapter 2 explains why appraisals lag. The register should carry an implied mark, not the appraisal, when it estimates risk.

**Reproduce:** `tests/test_ch25_examples.py::test_example_25_2`

### Example 25.3 — Conflicting signals on the industrial bid

**Given.** Hypothesis $H$: "Industrial cap rates in the target submarket will widen by at least 50 bp over the next 12 months." Prior from your weekly outlook: $p_0 = 0.40$. This week's signals, with likelihood ratios you assign [HYPOTHESIS]:

| Signal | Source type | Reading | LR |
|---|---|---|---|
| $s_1$ | Transaction database | Two sales near 6.25%, no widening | 0.7 (stale and selected) |
| $s_2$ | Lender term sheets | Wider spreads, lower proceeds | 2.0 |
| $s_3$ | Sell-side note | "Stable" | 0.9 (biased, widely known) |
| $s_4$ | CMBS special servicing | Rising three months | 1.5 |

Your bid assumes no widening. If $P(H) > 0.50$ you will lower the bid. If not, you will hold it.

**Find.** The posterior with all four signals treated as independent, and the posterior if $s_2$ and $s_4$ share a cause.

**Solution.**

*Independent:* prior odds $= 0.40/0.60 = 0.6667$. Product of LRs $= 0.7 \times 2.0 \times 0.9 \times 1.5 = 1.89$. Posterior odds $= 0.6667 \times 1.89 = 1.26$. Posterior $= 1.26/2.26 =$ **55.75%**.

*Correlated:* lenders tighten partly *because* special servicing is rising, so $s_4$ adds little once $s_2$ is known. Count the pair as one signal with LR 2.0. Product $= 0.7 \times 2.0 \times 0.9 = 1.26$. Posterior odds $= 0.6667 \times 1.26 = 0.84$. Posterior $= 0.84/1.84 =$ **45.65%**.

**Check.** `stats.likelihood_ratio_update(0.40, 1.89)` returns 0.5575 and `stats.likelihood_ratio_update(0.40, 1.26)` returns 0.4565. Both posteriors lie between the prior and 1 in the direction of the dominant signal, as they should.

**Decision consequence.** The decision threshold (0.50) lies **between** the two posteriors. The bid therefore turns on an independence assumption, not on the evidence. That is a finding, not a failure. The next hour should go to breaking the correlation. Ask the lenders directly whether the spread change reflects their own loss experience, a CMBS-market spread, or a capital-allocation decision at their institution. The third is the most independent of $s_4$. Until then, hold the bid but do not raise it. Conflicting signals are resolved by finding out *why* sources disagree, not by averaging them.

**Reproduce:** `tests/test_ch25_examples.py::test_example_25_3`

---

## 25.7 The instruments of the desk

Each instrument exists to support a calculation or a decision that would otherwise be made from memory. The templates are in `desk/`. Completed examples with hypothetical data are in `desk/daily_blotter/example_filled_blotter.md` and `desk/investment_memos/example_ic_memo.md`.

### 25.7.1 The handwritten market blotter

The blotter (`desk/daily_blotter/daily_market_blotter.md`) is one sheet. Its value lies in three columns most screens do not have: **Change** (computed by hand, which forces you to notice it), **Note (cause, if known)**, and **What would surprise?** on the calendar. The filled example shows a typical morning: 2-year yield +6 bp, 10-year +4 bp, so the 2s10s spread flattens by 2 bp. The analyst writes "flattening into CPI; front end repricing Fed path" and, in §4, records a belief change from 35% to 45% that the next FOMC meeting holds rather than cuts. That belief change is dated and will be scored.

Rules for the blotter: (i) record the source and time of every level; (ii) write "unknown" in the cause column rather than inventing a cause; (iii) close the sheet at the end of the day with the P&L line and any change of view; (iv) never erase. Strike through and initial.

### 25.7.2 The economic briefing

Use `desk/scenario_templates/economic_release_analysis.md`. The essential arithmetic is the **surprise against revised consensus**, together with a check of whether the market reaction had the expected sign. If CPI is 0.1 percentage point above consensus and the 2-year yield *falls*, the briefing must list explanations before anyone trades on them: a revision to the prior month, the composition of the surprise (shelter versus goods), positioning, or competing news. Release mechanics, including revision schedules, belong in the historical reference file for that series.

### 25.7.3 Historical reference notes

A historical reference note is a one-page file per episode, built on `desk/scenario_templates/historical_event_timeline.md`, with every number labeled [FACT] (with source ID) or *(verification pending)*. The discipline is the same as in Chapter 23. A reference note that says "spreads blew out in 2020" is useless. One that gives the dated level from a registered source, the financing conditions then, and what was knowable *at the time* can be compared with today. The desk's reference file is a register, not a story collection.

### 25.7.4 CRE deal memos

The IC memo (`desk/investment_memos/investment_committee_memo.md`) is the CRE equivalent of the trade ticket. It is longer because the position is larger, less liquid, and harder to exit. Section 25.11 works through a complete example. The rule that matters most: **state the walk-away price and the conditions that trigger it before you negotiate.** A memo without a walk-away is an argument for doing the deal, not a decision.

### 25.7.5 Trade tickets

A trade ticket (`desk/trade_journal/trade_ticket.md`) answers one question before the trade: *what do I lose if I am wrong, and what if the market gaps through my exit?* For the TY short in §25.1 (all [HYPOTHESIS]):

| Field | Entry |
|---|---|
| Instrument | 10-year T-note futures, short 40 |
| Position DV01 | $40 \times \$85 = \$3{,}400$ per bp |
| Invalidation | 10-year yield 15 bp below entry. Thesis: the term premium is rebuilding |
| Loss at invalidation | $3{,}400 \times 15 = \$51{,}000$, or $51{,}000/40{,}000{,}000 = 0.1275\%$ of capital |
| Gap risk (CPI day, 30 bp move) | $3{,}400 \times 30 = \$102{,}000$, or 0.255% of capital |
| Per-trade limit | 0.25% of capital $= \$100{,}000$ |

The gap loss slightly exceeds the limit. The ticket therefore records a choice: reduce to 39 contracts ($39 \times 85 \times 30 = \$99{,}450$), or hold 40 and record the exception with the approver's initials. Either is defensible. Not recording it is not.

### 25.7.6 Risk registers

### Example 25.4 — Aggregating the risk register

**Given.** The book in §25.1 at Monday's close (all [HYPOTHESIS]). The 5-year note and the swap are valued as 5-year, 4.00% semiannual par instruments at a 4.00% yield. The swap's DV01 is approximated by that of a par bond with the same notional. ES is at 5,713. Hotel NOI is \$2,550,000 (8.5% cap on NOI after a 4% FF&E reserve). Industrial NOI is \$1,500,000 (6.25% cap). Capital is \$40 million.

**Find.** (a) Book DV01. (b) Beta-adjusted equity delta. (c) CRE equity at risk under: hotel NOI −10% and cap +75 bp to 9.25%; industrial NOI flat and cap +50 bp to 6.75%. (d) A joint stress of rates +50 bp, equities −10%, and the CRE shocks in (c).

**Solution.**

(a) DV01 of a 5-year 4% par bond per \$100 face (`fi.dv01(0.04, 0.04, 5)`) $= 0.044913$.

| Position | P&L per +1 bp |
|---|---|
| Short 40 TY | +3,400 |
| Long \$10m 5-yr note: $-0.044913 \times 100{,}000$ | −4,491 |
| Pay-fixed \$15m swap: $+0.044913 \times 150{,}000$ | +6,737 |
| **Book DV01** | **+5,646** |

The book is net short duration: it gains about \$5,646 per basis-point rise.

(b) $\Delta_{eq} = 10 \times 50 \times 5{,}713 + 1.1 \times 2{,}000{,}000 = 2{,}856{,}500 + 2{,}200{,}000 = \$5{,}056{,}500$. A 1% fall costs \$50,565.

(c) Hotel: $V_1 = 2{,}550{,}000 \times 0.90 / 0.0925 = 2{,}295{,}000/0.0925 = \$24{,}810{,}811$. Equity at risk $= 30{,}000{,}000 - 24{,}810{,}811 = \$5{,}189{,}189$. Equity falls from \$12.0 million to \$6.81 million, or **−43.2%**.
Industrial: $V_1 = 1{,}500{,}000/0.0675 = \$22{,}222{,}222$. Equity at risk $= \$1{,}777{,}778$. Equity falls from \$9.6 million to \$7.82 million, or **−18.5%**.
Total CRE equity at risk $= \$6{,}966{,}967$, or 17.4% of capital.

(d) Rates: $50 \times 5{,}646 = +\$282{,}282$. Equities: $-0.10 \times 5{,}056{,}500 = -\$505{,}650$. CRE: $-\$6{,}966{,}967$. Total: **−\$7,190,335**, or **−17.98%** of capital.

**Check.** Hotel value change via the identity $V_1/V_0 = (1+g)c_0/c_1 = 0.9 \times 8.5/9.25 = 0.82703$, a −17.30% change. The leverage multiplier is $30/12 = 2.5$, and $2.5 \times -17.30\% = -43.2\%$. This agrees.

**Decision consequence.** The register answers the partner's second question. **The largest risk is the hotel's equity, about 72% of the joint-stress loss, and it is not the risk the desk talks about most.** Every morning's conversation is about rates and equities, which together account for −\$223,368 in the stress, about 3% of the loss. The liquid positions are the only ones that can be adjusted this week, so the register points to the real choices. One is to hedge part of the CRE beta with a short REIT position, accepting basis risk (Chapter 13). Another is to stop adding duration-short trades that do nothing for the dominant exposure. A third is to review the hotel loan's maturity and extension tests. The joint stress also exposes an internal inconsistency to examine: it pairs a +50 bp rates move with cap-rate widening of 50–75 bp, which implies a stable cap-rate spread. Chapter 9 shows that spreads can also widen.

**Reproduce:** `tests/test_ch25_examples.py::test_example_25_4`

### 25.7.7 Portfolio review

The monthly portfolio review uses three documents: the attribution (Example 25.2) summed over the month, the register (Example 25.4), and the decision journal. It asks four questions in order:

1. **Did P&L come from the risks we intended to take?** Compare the attribution with the theses on file. A month in which the REIT idiosyncratic term dominates, while the theses were all about rates, is a month of unintended risk.
2. **Is any position past its invalidation, or kept by an undocumented exception?**
3. **Has the register's largest risk changed?** If it has, why, and by whose decision?
4. **What did we decide not to do, and what happened to it?** Abstentions are positions too. Score them.

---

## 25.8 The weekly market intelligence meeting

The weekly meeting turns a week of blotters into a revised regime assessment (`desk/scenario_templates/weekly_macro_outlook.md`) and a list of decisions. A 60-minute agenda for a two- to four-person desk [HYPOTHESIS]:

| Minutes | Item | Rule |
|---|---|---|
| 0–10 | Scorecard: last week's dated forecasts that resolved; Brier contributions | Read aloud, no discussion |
| 10–20 | Regime table: growth, inflation, policy, credit, risk appetite | Each change needs a cited release or level |
| 20–35 | **Conflicting signals**: one item where sources disagree | Grade the sources (§25.6.2). State LRs and the dependence assumption |
| 35–45 | What is priced versus our view | Market-implied number first, our number second |
| 45–55 | Register: largest risk, joint stress, maturities | No new trade without a ticket |
| 55–60 | Actions, non-actions, owners, dates | Written into the journal |

Two disciplines keep the meeting from becoming a conversation. First, **the most junior person states a view first**, so that seniority does not anchor the room. Second, **no source is cited without its grade**. "A lender told me" becomes "one lender, indicative term sheet, B reliability, not widely known, possibly posturing".

---

## 25.9 Postmortems, the error log, and calibration

A postmortem (`desk/trade_journal/post_trade_review.md`) has a fixed order. Copy the ex-ante forecast unedited. State which scenario occurred. Ask whether the outcome lay inside the forecast distribution. Grade thesis, sizing, execution, and exit separately on a 0–4 scale. Name one rule to keep or change. The postmortem is written for every closed position, including winners. Winners carry the most dangerous lessons, because nobody examines them.

### Example 25.5 — Error-log analysis

**Given.** Over one quarter, 400 drills and work items produced 60 logged errors [HYPOTHESIS]:

| Category | Count |
|---|---|
| Units (bp vs %, monthly vs annual, \$ vs \$000) | 14 |
| Data (wrong source, stale or unrevised figure) | 12 |
| Timing (beginning vs end of period, forward vs trailing NOI) | 11 |
| Arithmetic | 9 |
| Judgment | 8 |
| Concept | 6 |
| **Total** | **60** |

By month: 26, 19, 15.

**Find.** The error rate, the share of the top three categories, and whether the decline from 26 to 15 is evidence of improvement.

**Solution.**

Error rate $= 60/400 =$ **15%** of items.
Top three (units, data, timing) $= 14 + 12 + 11 = 37$, which is $37/60 =$ **61.7%** of errors.

*Improvement test.* Suppose the true rate were constant at the quarterly mean of 20 per month. Under a Poisson model, the probability of observing 15 or fewer in a month is
$$P(X\le 15 \mid \lambda=20) = \sum_{k=0}^{15} e^{-20}\frac{20^k}{k!} = 0.1565.$$
A month as low as 15 would occur about one time in six with no improvement at all.

**Check.** The categories sum to 60, and so do the monthly counts ($26+19+15$). The Poisson tail can be cross-checked with a normal approximation: $(15.5-20)/\sqrt{20} = -1.006$, giving $\Phi(-1.006) \approx 0.157$.

**Decision consequence.** (1) Three mechanical categories account for nearly two-thirds of errors, and each has a mechanical fix. Write units in every blotter column header. Add a "revised?" checkbox to every data field. Write "forward NOI" or "trailing NOI" next to every cap rate. These are template changes, and they cost minutes. (2) Do **not** report "errors down 42%" to the partner. The decline is not yet distinguishable from noise. Report the count and repeat the test after the next quarter. (3) The 8 judgment errors are the expensive ones. Review each against the decision journal, because a judgment error in a live memo can cost more than all 52 of the others combined.

**Reproduce:** `tests/test_ch25_examples.py::test_example_25_5`

### Example 25.6 — Calibration review with a Brier score

**Given.** Twenty dated binary forecasts from the decision journal over six months [HYPOTHESIS]. Examples include "the lender will issue a term sheet at ≥ 60% LTV by the 30th", "CPI core will print at or above consensus", and "the seller will accept ≤ \$23.0m". Forecasts were recorded at four probability levels:

| Stated $f_k$ | $n_k$ | Occurred | $\bar o_k$ |
|---|---|---|---|
| 0.9 | 5 | 3 | 0.600 |
| 0.7 | 6 | 4 | 0.667 |
| 0.5 | 4 | 2 | 0.500 |
| 0.3 | 5 | 1 | 0.200 |
| **Total** | **20** | **10** | **0.500** |

**Find.** The Brier score with `sdesk.stats.brier_score`, the skill score against always forecasting the base rate, and the reliability and resolution terms. Then decide what to change.

**Solution.**

*Brier score, by bin:*
* 0.9: $3(0.9-1)^2 + 2(0.9-0)^2 = 0.03 + 1.62 = 1.65$
* 0.7: $4(0.09) + 2(0.49) = 0.36 + 0.98 = 1.34$
* 0.5: $4(0.25) = 1.00$
* 0.3: $1(0.49) + 4(0.09) = 0.49 + 0.36 = 0.85$

Sum $= 4.84$, so $BS = 4.84/20 =$ **0.242**. In code: `stats.brier_score([0.9]*5 + [0.7]*6 + [0.5]*4 + [0.3]*5, outcomes)` returns 0.242.

*Skill:* the base rate is $\bar o = 0.5$, so the climatological score is $0.5 \times 0.5 = 0.25$, and $BSS = 1 - 0.242/0.25 =$ **0.032**.

*Reliability:* $[5(0.3)^2 + 6(0.0333)^2 + 4(0)^2 + 5(0.1)^2]/20 = (0.45 + 0.00667 + 0 + 0.05)/20 =$ **0.02533**.

*Resolution:* $[5(0.1)^2 + 6(0.1667)^2 + 4(0)^2 + 5(0.3)^2]/20 = (0.05 + 0.16667 + 0 + 0.45)/20 =$ **0.03333**.

**Check.** $\text{REL} - \text{RES} + \text{UNC} = 0.02533 - 0.03333 + 0.25 = 0.242$, which equals the direct calculation.

**Decision consequence.** The forecaster has some resolution: the 0.3 bin really did occur less often than the 0.7 bin. But the score is barely better than saying 50% to everything, and almost all of the reliability penalty, 0.45 of 0.507, comes from the **0.9 bin**, where 5 forecasts of 90% came true only 3 times. How strong is that evidence? If the true probability were 0.9, the chance of 3 or fewer successes in 5 is $1 - \binom54 0.9^4(0.1) - 0.9^5 = 1 - 0.32805 - 0.59049 = 0.0815$. That is suggestive, not conclusive. The action is cheap and reversible. For the next quarter, any forecast above 0.8 requires a written base rate and a named reason it does not apply. A deal memo stating 90% confidence that a seller will accept a price should be read as roughly 60–75% until the record says otherwise. The review also shows what the score cannot do. Twenty forecasts over six months cannot separate a 0.24 forecaster from a 0.20 one. Calibration is a multi-year project, and the decision journal is its only data.

**Reproduce:** `tests/test_ch25_examples.py::test_example_25_6`

---

## 25.10 The 1987 desk exercise

The exercise reconstructs one morning on a 1987-style desk, using only a financial calculator, graph paper, printed quotes, and a newswire, and then does the same work with modern tools. The point is to see which parts of the work were judgment and which were clerical, and to measure both. All prices are [HYPOTHESIS]: they are illustrative levels, **not** historical quotes for any 1987 date.

**Tools then.** The HP-12C financial calculator was introduced in 1981 and has been sold essentially unchanged since [FACT; HP history pages and press coverage, ch25-S08, VERIFIED-SECONDARY]. It has bond price and yield functions. A desk in 1987 would also have had a dealer's printed quote sheet, a newswire printer, a telephone, and graph paper. The specific vendors and terminals on any given desk varied, and this chapter does not name them.

**The morning, by hand.** (i) Copy 25 quotes from the printed sheet onto the blotter. (ii) Compute changes by hand. (iii) Plot the yield curve on graph paper against yesterday's. (iv) Read the newswire for the overnight story and write down a cause, or "unknown". (v) Revalue the bond positions on the calculator. (vi) Phone the lender for a mortgage quote.

### Example 25.7 — Revaluing a long bond by hand, and counting transcription errors

**Given.** A 30-year, 9% semiannual-coupon bond at par (yield 9%). The yield rises 50 bp to 9.5%. On the hand desk, 100 numbers are copied each morning (25 quotes copied four times: sheet → blotter → worksheet → position sheet), with an assumed per-copy error rate of $q = 0.5\%$ [HYPOTHESIS].

**Find.** (a) The price change by duration and convexity, as it would be computed by hand. (b) The exact price. (c) The probability of at least one transcription error per morning, and the effect of an independent check that catches 90% of errors.

**Solution.**

(a) At 9%, modified duration $D_{mod} = 10.319$ and convexity $C = 183.83$ (from the calculator or a duration table). With $\Delta y = 0.005$:
$$\Delta P \approx 100\left[-10.319(0.005) + \tfrac12(183.83)(0.005)^2\right] = -5.160 + 0.230 = -4.930.$$

(b) Exact price at 9.5% (`fi.bond_price(0.095, 0.09, 30)`): **95.062**, a change of −4.938. The second-order estimate is off by less than 0.01 point. The duration-only estimate is off by 0.22 point, about 4.5% of the move.

(c) $P(\ge 1 \text{ error}) = 1 - (1-0.005)^{100} = 1 - 0.6058 =$ **39.4%**. With a 90% check, $q' = 0.0005$ and $P = 1 - 0.9995^{100} =$ **4.9%**.

**Check.** (b) brackets (a): the true loss (4.938) is smaller than the duration-only loss (5.160) because convexity is positive. (c) To first order, $nq = 0.5$ expected errors per morning. $1 - e^{-0.5} = 0.393$, close to 39.4%.

**Decision consequence.** The judgment content of the morning, which is step (iv) and the decision about what to do, was the same in 1987 as now. The clerical content was large and error-prone. With no check, a morning sheet contains at least one wrong number about two days in five. A desk that relied on hand transcription without a second reader was making decisions on corrupted data on a material fraction of days. The modern equivalent of steps (i)–(iii) and (v) takes seconds: a data feed into a spreadsheet or `sdesk.fixed_income.bond_price`. Its failure modes are different: a stale feed, a wrong ticker, a formula pointing at the wrong row. **What the hand desk had that is worth keeping** is the forced selection of 25 numbers, the habit of plotting by hand, which makes shape changes visible, and the "cause or unknown" column. **What it lacked** was speed, auditability, and arithmetic reliability. Keep the first list on paper and do the second list in code, with the paper sheet as the control total.

**Reproduce:** `tests/test_ch25_examples.py::test_example_25_7`

### 25.10.1 The same morning, modern

| Step | 1987 desk | Modern desk | What changed for the decision |
|---|---|---|---|
| Collect levels | Printed sheet, copied by hand (≈ 20–30 min) [HYPOTHESIS] | Feed into a spreadsheet (seconds) | Time freed, unless it is spent watching screens |
| Compute changes | Calculator | Formula | Transcription risk replaced by formula and feed risk |
| Curve | Graph paper | Chart | None if the chart is read; hand plotting still trains the eye |
| Story | Newswire printer | Many wires, social media, research | More noise; source grading becomes more important, not less |
| Revalue | Calculator, one bond at a time | Whole book, all scenarios | Joint stress (Example 25.4) becomes feasible daily |
| Lender quote | Phone | Phone and email | **Unchanged.** Still private, still the A-relevance source |

Do not romanticize the left column. Hand desks were slow, made unrecorded errors, and could not run a joint stress. They also could not score themselves, because forecasts were rarely written in a form that could be scored. Do not romanticize the right column either. A desk that sees 2,000 numbers sees none of them. The modern desk's failure is not error but **dilution of attention**. The paper blotter is a defense against it, not a nostalgic choice.

---

## 25.11 CRE application: the investment committee memo

The complete memo is in `desk/investment_memos/example_ic_memo.md`. Its central calculations follow (all [HYPOTHESIS]).

**The asset.** A 100% leased industrial building. NOI is \$1,500,000 in year 1, with 3% annual bumps and seven years of remaining term. The asking price is \$24.0 million (6.25% cap). Buyer costs are 2%, selling costs 2%, the hold is five years, and the reversion is priced on forward (year-6) NOI of $1{,}500{,}000 \times 1.03^5 = \$1{,}738{,}911$.

**Scenarios for the exit cap rate** at year 5, when the lease has two years left: 6.25% (p = 0.3), 6.75% (p = 0.5), 7.50% (p = 0.2). Net sale proceeds are \$27,266,126, \$25,246,413, and \$22,721,772.

| | Price \$24.0m | Price \$23.0m |
|---|---|---|
| Basis (incl. 2%) | \$24,480,000 | \$23,460,000 |
| Unlevered IRR at 6.25% / 6.75% / 7.50% exit | 8.40% / 7.02% / 5.19% | 9.44% / 8.05% / 6.21% |
| Expected IRR | 7.07% | 8.10% |
| IRR of expected cash flows | 7.09% | 8.13% |

The committee's hurdle is an 8.0% expected unlevered IRR [HYPOTHESIS]. The maximum price that meets it is **\$23,095,880**, a 6.49% going-in cap rate.

**Financing check at \$24.0m, 60% LTV.** Loan \$14.4 million, 6.50%, 30-year amortization. Annual debt service is \$1,092,214. DSCR is $1{,}500{,}000/1{,}092{,}214 = 1.37\times$, debt yield is 10.42%, and cash-on-cash is $(1{,}500{,}000 - 1{,}092{,}214)/9{,}600{,}000 = 4.25\%$. The going-in cap rate (6.25%) is below the 6.50% coupon. Leverage is negative, and the levered return depends on appreciation (Chapter 1, §1.6).

**Recommendation in the memo.** Bid \$23.0 million and walk away above \$23.1 million. Example 25.3 then applies. If the lender conversations show that the spread widening is independent of CMBS distress, the posterior on cap-rate widening moves above 50%, and the bid falls further or the desk passes. The memo states this as an invalidation condition **before** the negotiation.

The memo, the ticket, and the register all use the same structure: a number, the assumption behind it, and the condition that would change it. This is what makes a process repeatable. A second analyst can redo every step and reach the same numbers, and can disagree with the assumptions in writing.

---

## 25.12 When the process fails

1. **Ritual without selection.** The blotter has 200 numbers, the meeting reviews everything, and the journal records nothing that can be scored. Test: in the last month, how many written forecasts resolved? If none, the process is theater.
2. **Process as an alibi.** "We followed the process" is offered after a loss as proof the decision was sound. A process makes decisions *auditable*. It does not make them right. The postmortem must still ask whether the inputs were good.
3. **Scoring the wrong forecasts.** Easy, short-dated forecasts, such as "the release will be within 0.1 of consensus", inflate a Brier record while the expensive judgments, such as "the seller will accept" or "the lender will extend", go unscored. Score the forecasts that size positions.
4. **Correlated sources counted as independent.** Example 25.3. The weekly meeting multiplies five versions of one story into false certainty.
5. **Stale marks in the register.** Example 25.2. Appraisal-based CRE marks understate risk exactly when it is rising (Chapter 2).
6. **Regime change.** A routine built for one regime's important data watches the wrong releases in the next. In a low-inflation regime CPI matters less than payrolls. In a high-inflation regime the reverse holds [INFERENCE]. The weekly regime table exists to change the routine, not only the positions.
7. **Small samples.** Twenty forecasts or three months of error logs cannot establish improvement (Examples 25.5–25.6). Declaring victory early ends the measurement.
8. **Survivorship in the journal.** Abstentions and abandoned deals are not recorded, so the record shows only the decisions that were made. Score the "pass" decisions too.

---

## 25.13 Historical episode: the New York Fed's Trading Desk and its daily routine

**Why this episode.** A study of daily desk practice needs a primary, published description of a real operation's routine, not an anecdote about a famous trader. The Open Market Trading Desk of the Federal Reserve Bank of New York ("the Desk") is unusual in having described its own routine in official publications.

**Date and environment.** In the 1980s and 1990s the Desk implemented FOMC policy mainly through temporary operations (repurchase agreements) and occasional outright purchases or sales of Treasury securities. It aimed reserve supply at a path or a federal funds objective set by the FOMC [FACT; Edwards (1997), *Federal Reserve Bulletin*, "Open Market Operations in the 1990s", ch25-S09, VERIFIED-SECONDARY].

**What the published sources document.**

* Ann-Marie Meulendyke's *U.S. Monetary Policy and Financial Markets*, published by the Federal Reserve Bank of New York, describes monetary policy from the vantage point of the Desk. Its chapter on the view from the Desk has sections titled *Daily Dealer Meetings*, *The Treasury Call*, *Formulating the Day's Program*, *The Trading Room Scene*, *The Conference Call*, and *Executing the Daily Program*. The book also has a chapter on projecting reserves [FACT; table of contents via FRASER, ch25-S10, VERIFIED-SECONDARY]. Catalog records give both a 1989 and a 1998 date. These appear to be different editions, and this chapter has not confirmed which edition contains which wording *(verification pending)*.
* A Federal Reserve narrative excerpted from Paul Meek's New York Fed publication *Open Market Operations* and republished by the Minneapolis Fed (1 November 1990) describes a mid-June afternoon in the Desk's trading room. The Account Manager and officers agree to buy about \$1.25 billion of Treasury bills. About ten traders at telephones call a set of the three dozen primary dealers. About forty-five minutes after the first entry the Desk has bought \$1,304 million of bills, and the tickets go to the government bond department for settlement [FACT; ch25-S11, VERIFIED-SECONDARY]. The source does not let us confirm whether the narrative describes one dated day or a composite.
* The Desk's usual time for arranging temporary operations was **11:30 a.m. Eastern, shortly after revisions to the reserve projections became available**. In December 1996 the Desk announced that from 1997 its normal entry time would move up one hour, to shortly after 10:30 a.m. [FACT; "Open Market Operations during 1996", *Federal Reserve Bulletin*, July 1997, and the New York Fed's annual reports on open market operations for 1996 and 1997, ch25-S12, ch25-S13, VERIFIED-SECONDARY].
* The details of the daily conference call, including its exact time and which Board staff and Reserve Bank officials took part in a given era, are described in Meulendyke's chapter. They are not stated here until that text has been read *(verification pending)*.

**The routine as a process [INFERENCE from the documented section headings and timing].** The Desk's day was sequenced in this order: *collect* (reserve projections; meetings with dealers for market color; a call with the Treasury on its cash balance), *formulate* (the day's program), *review* (a conference call before acting), and then *execute* (market entry at a fixed, publicly understood time, with tickets settled through a separate department). Three features map directly onto this chapter:

1. **Information collection precedes the decision and is distinct from it.** Dealer meetings gather market intelligence. They do not decide the operation.
2. **The entry time was tied to the arrival of revised projections.** The Desk acted once the most important revised data were in, not continuously. That is a time budget built around a data release.
3. **Execution and settlement were separated.** Traders executed and a different department settled, which is the trade-ticket discipline of §25.7.5.

**A second documented practice: scoring forecasters.** The Good Judgment Project, one of the university teams in a two-year geopolitical forecasting tournament sponsored by IARPA, reported that probability training, teaming, and "tracking" (placing the top performers in elite teams) improved accuracy, measured by Brier-type scoring [FACT; Mellers et al. (2014), *Psychological Science* 25: 1106–1115, ch25-S14, VERIFIED-SECONDARY]. A 2025 reanalysis in the same journal argued that once extraneous variables are included, the effects of teaming and training are reduced, eliminated, or in some cases reversed [FACT; Holden et al. (2025), ch25-S15, VERIFIED-SECONDARY]. The practice of scoring every forecast is documented. How much the specific interventions caused improvement is disputed.

**What was knowable at the time.** The Desk's practices were published by the Federal Reserve itself, so they were public. Its policy objective was not always public in the period before the FOMC began announcing its decisions, which is commonly dated to 1994 *(verification pending)*. Inferring the Desk's intentions from its operations ("Fed watching") was a market activity in its own right [INFERENCE; the announcement-effect literature, e.g. the New York Fed *Economic Policy Review* article "The Announcement Effect: Evidence from Open Market Desk Data", ch25-S16, VERIFIED-SECONDARY for the article's existence only].

**Interpretations.** One reading is that the routine is a model of disciplined process: projection, intelligence, review, execution. A second reading is that it fit a narrow task. The Desk was not speculating. It had a defined objective, a dominant position in the market, and no profit motive. A private desk lacks all three, so the routine cannot be copied wholesale.

**What the episode establishes and what it does not.** It establishes that a large, consequential market operation documented a fixed daily sequence that separated information collection, decision, review, and execution, and timed its action to the arrival of revised data. It does **not** establish that this routine produced better outcomes than an alternative. No counterfactual exists. Nor does it say anything about the practices of private trading firms, and this chapter makes no claims about any individual trader's routine. The GJP evidence establishes that systematic forecast scoring is feasible at scale. Whether scoring alone improves accuracy is contested.

---

## 25.14 Decision exercise: Thursday's committee

Return to §25.1. Using the attribution (Example 25.2), the register (Example 25.4), the conflicting signals (Example 25.3), and the memo (§25.11), prepare for the committee on `desk/investment_memos/decision_record_template.md`:

1. Your recommendation on the second industrial building: bid, at what price, with what walk-away; or pass.
2. What you will do about the hotel equity exposure that dominates the joint stress, including the option of doing nothing.
3. Whether to keep the TY short through Wednesday's CPI release, and at what size, using the ticket arithmetic of §25.7.5.
4. One change to the weekly routine, justified by Example 25.1 or 25.5.
5. Two dated forecasts, with probabilities, that will be scored at the next calibration review.

**Rubric (see `problems/solutions/ch25_solutions.md`, §Decision exercise).**

| Item | Full credit (2) | Partial (1) | None (0) |
|---|---|---|---|
| Bid | Price ≤ \$23.1m tied to the 8% hurdle; walk-away stated; invalidation tied to the lender-independence question | Price stated without walk-away | "Bid ask" or no number |
| Hotel exposure | Quantifies the share of stress loss; considers a REIT hedge with basis risk, loan terms, and doing nothing | Mentions the risk without numbers | Ignores it |
| TY into CPI | Uses the gap loss against the limit; resizes or records the exception | Mentions gap risk qualitatively | No sizing |
| Routine change | Uses value per hour or the error-log Pareto, and states how it will be tested | Change without a test | None |
| Forecasts | Two binary, dated, resolvable forecasts that size a position | Vague or unresolvable | None |

Passing on the second building is fully defensible if the posterior in Example 25.3 cannot be resolved before the bid date. Abstention scores full credit when it is reasoned this way.

---

## 25.15 Frequent analytical errors

1. **Treating a widely known source as an edge.** Payrolls, CPI, the COT, and FOMC statements are processed by everyone within minutes. The edge, if any, lies in interpretation or positioning.
2. **Reading the COT as current.** It describes Tuesday's positions, released on Friday. A futures-only short may be one leg of a hedged basis trade.
3. **Measuring a surprise against an unrevised prior.**
4. **Multiplying likelihood ratios from correlated sources.**
5. **Adding DV01, equity delta, and CRE value changes as if they were one unit.** Aggregate through a joint stress.
6. **Mixing DV01 sign conventions.** Say whether DV01 is P&L for a rise or a fall in yields, and keep it fixed.
7. **Using appraisal marks in a risk register.**
8. **Reporting an improvement in errors or calibration from a small sample.**
9. **Scoring only easy forecasts.**
10. **Romanticizing the paper desk, or the screen.** Each has a measurable failure rate. Use paper for selection and code for arithmetic.
11. **A memo without a walk-away price.**

---

## 25.16 Connections to other chapters

* Chapter 1: decision records, process versus outcome, and the \$40 million book used here.
* Chapter 2: stale appraisal marks (Example 25.2) and price formation in private markets.
* Chapter 3: Bayesian updating (Example 25.3).
* Chapters 4–5: the releases and central-bank communication on the calendar.
* Chapter 6: DV01, duration, and convexity (Examples 25.4 and 25.7).
* Chapters 9–10: cap-rate shocks, leverage, and debt sizing in the register and the memo.
* Chapter 13: hedging CRE beta with REITs.
* Chapter 20: calibration and proper scoring rules in depth.
* Chapter 14: beta hedging with equity index futures (Example 25.2).
* Chapter 21: position sizing and gap risk behind the trade-ticket limit.
* Chapter 22: quantitative market intelligence, including positioning data and backtest hygiene.
* Chapter 23: historical reference notes and the 1987 episode.
* Chapter 24: the professional judgment that this chapter's process supports.

---

## 25.17 One-page reference sheet

**Daily outputs:** blotter (open, midday, close) · economic briefing per release · register update · tickets reconciled · journal and error log.
**Weekly:** scorecard → regime → one conflicting-signal item → priced vs view → register → actions and non-actions.
**Monthly:** portfolio review (attribution vs theses; invalidations; largest risk; abstentions).
**Quarterly:** calibration review; error-log Pareto; time-budget audit.

| Formula | Expression |
|---|---|
| Futures P&L | side × $(F_1-F_0)$ × multiplier × contracts |
| Rates P&L | position DV01 × $\Delta y$ (bp); state the sign convention |
| Systematic / idiosyncratic | $MV\beta R_m$ / $MV(R-\beta R_m)$ |
| Beta-adjusted equity delta | $\sum \beta_j MV_j$ |
| CRE value under stress | $V_1 = N_0(1+g)/c_1$; $\Delta E/E_0 = (V_1-V_0)/(V_0-L)$ |
| Brier score | $\frac1N\sum (f_i-o_i)^2$; constant 0.5 scores 0.25 |
| Murphy decomposition | $BS = \text{REL} - \text{RES} + \bar o(1-\bar o)$ |
| Brier skill | $1 - BS/[\bar o(1-\bar o)]$ |
| Odds update | posterior odds = prior odds × $\prod LR_j$ (independent signals only) |
| Value of an hour | $\pi_a v_a$ |
| Transcription risk | $1-(1-q)^n$; with check $q(1-h)$ |
| Loss at invalidation | DV01 × distance (bp); gap loss = DV01 × gap |

**Source grading checklist:** timeliness · reliability · bias · revisions · cost · coverage · relevance · already widely known?
**COT:** Tuesday close → Friday 3:30 p.m. ET; legacy / disaggregated / TFF categories; reportable traders only.
**Rules to test, not trust:** the most relevant sources are the least reliable and least known; a decline in errors from 26 to 15 is noise until shown otherwise; 90% means 90%.

---

## References for this chapter

Full entries with verification status are in `references/sources_ch25.md` (to be merged into `SOURCE_REGISTER.md`).

* Commodity Futures Trading Commission. *Commitments of Traders* (reports descriptions; release schedule; explanatory notes for the disaggregated and Traders in Financial Futures reports). https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm
* Edwards, C. L. (1997). "Open Market Operations in the 1990s." *Federal Reserve Bulletin* 83 (November): 859–874.
* Federal Reserve Bank of New York. *Open Market Operations during 1996* (in *Federal Reserve Bulletin*, July 1997) and annual reports on open market operations, 1996 and 1997.
* Meek, P. *Open Market Operations*. Federal Reserve Bank of New York; excerpt republished by the Federal Reserve Bank of Minneapolis, 1 November 1990.
* Meulendyke, A.-M. *U.S. Monetary Policy and Financial Markets*. Federal Reserve Bank of New York (1989; 1998 edition).
* Mellers, B., et al. (2014). "Psychological Strategies for Winning a Geopolitical Forecasting Tournament." *Psychological Science* 25(5): 1106–1115.
* Murphy, A. H. (1973). "A New Vector Partition of the Probability Score." *Journal of Applied Meteorology* 12(4): 595–600. *(Bibliographic details verification pending.)*
* Brier, G. W. (1950). "Verification of Forecasts Expressed in Terms of Probability." *Monthly Weather Review* 78(1): 1–3. *(Bibliographic details verification pending.)*
* U.S. Bureau of Labor Statistics. Current Employment Statistics benchmark revision notices.
