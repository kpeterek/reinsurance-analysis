# Sixteen-Week Study Program

> **Status:** Plan (v1.0). Weeks that reference chapters or cases not yet written are marked ◻. Their assignments are fixed, but the material arrives as production proceeds (see `PROGRESS.md`). Daily drills come from the simulator. Ten to fifteen minutes a day is the minimum.

Weekly time budget: about 10–12 hours. Reading 3–4 h, problems 3 h, drills 1.5 h, CRE exercise 2 h, cross-asset exercise 1 h, exam 1 h.

Mastery gate: about 85% on objective items before moving up in difficulty (the simulator enforces this per topic). Judgment work is scored on `reasoning_rubric.md`.

| Wk | Chapters | Required calculations | Historical cases (2) | Long CRE exercise | Cross-asset exercise | Exam |
|---|---|---|---|---|---|---|
| 0 | Preface, notation guide | — | — | — | — | Baseline assessment (diagnostic) |
| 1 | 1 | EV/SD, break-even p, price of immediacy, Kelly growth, levered returns | 1987 crash; Metallgesellschaft ◻ | Case A Mode A–B | Ch 1 Ex 1.4 (market making) | Week 1 exam ◻ |
| 2 | 2 ◻, 3 ◻ | Appraisal unsmoothing, Bayesian updates | 1987 (positioning); 1998 LTCM ◻ | Case A Mode C (blind) | Fed funds futures implied probabilities | ◻ |
| 3 | 6 ◻ | Price/yield, duration, convexity, DV01, carry, cap-rate spread | 1994 bond crash ◻; 2022 duration shock ◻ | Rate shock on levered CRE equity | Treasury DV01 hedge of a floating loan | ◻ |
| 4 | 4 ◻, 5 ◻ | Surprise indices, policy-rule arithmetic | Volcker disinflation ◻; 1970s inflation ◻ | Case H ◻ | Release analysis worksheet | ◻ |
| 5 | 8 ◻ | NOI construction, operating leverage, reassessment | Texas/RTC 1980s–90s ◻; Japan 1990s ◻ | NOI bridge drills | REIT-implied cap rates | ◻ |
| 6 | 9 ◻ | DCF, loaded cap, residual land, sensitivity grids | U.S. office post-2020 ◻; 2000 tech bubble ◻ | Case C ◻ | Equity earnings yield vs. real yield | ◻ |
| 7 | 10 ◻ | Loan sizing, amortization, balloon, waterfalls, refinancing gap | 2007–09 ◻; CMBS 2.0 ◻ | Case B ◻ | Swap/cap hedge pricing | ◻ |
| 8 | Review | Mixed | — | Case A Mode D (IC) | — | **Intermediate assessment** ◻ |
| 9 | 11 ◻ | Hotel P&L, flow-through, PIP, break-even occupancy | Post-9/11 hotels ◻; 2020 hotels ◻ | Case D ◻ | FX-hedged returns for a foreign hotel buyer | ◻ |
| 10 | 11 ◻ (cases) | Eight hotel cases | 2008–10 hotel distress ◻; COVID liquidity ◻ | Case J ◻ | Credit spread vs. hotel debt pricing | ◻ |
| 11 | 12 ◻, 17 ◻ | Maturity walls, recovery math, PD×LGD | Asian crisis 1997 ◻; 2007–09 ◻ | Case G ◻ | Distressed bond recovery | ◻ |
| 12 | 13 ◻, 18 ◻ | Real options, rate caps, Greeks | ERM 1992 ◻; LTCM ◻ | Case I ◻ | Option payoff and delta hedge | ◻ |
| 13 | 14 ◻, 15 ◻, 16 ◻ | Futures exposure, CIP, roll yield | 1929 ◻; 2000 ◻ | Case E ◻ | Commodity carry | ◻ |
| 14 | 20 ◻, 21 ◻, 22 ◻ | VaR/ES, Kelly limits, regressions, backtests | 1987; 2020 ◻ | Case F ◻ | Portfolio stress test | ◻ |
| 15 | 19 ◻, 23 ◻, 24 ◻ | Thesis construction | Two of your choice | IC defense of any case | Alternative-asset comparison | ◻ |
| 16 | 25 ◻ | Process review | — | **Capstone** ◻ | **Capstone** ◻ | **Final assessment** ◻ |

## Daily routine (weeks 1–16)
1. Five minutes: fill in the daily market blotter (`desk/daily_blotter/`).
2. Ten minutes: `python3 scripts/desk.py drill -n 5`, mixing categories A and B.
3. Twice a week: one category C–E drill, written out in full.
4. Friday: weekly macro outlook and error-log review. Run `python3 scripts/desk.py report`.

## "1987 desk exercises"
In weeks 3, 9, 13, and 14, solve one exercise using only a financial calculator, pencil, graph paper, printed quotes, and a short newswire. Then solve it again in Excel and Python. The aim is to understand the reasoning independently of software, not to romanticize older workflows.
