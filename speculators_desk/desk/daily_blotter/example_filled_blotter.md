# Daily Market Blotter — Worked Example (HYPOTHETICAL DATA)

> **Every level, price, position, and event on this sheet is hypothetical [HYPOTHESIS], constructed for teaching in Chapter 25.** The levels are not market data for any real date and must not be quoted as such. The arithmetic is checked in `tests/test_ch25_examples.py::test_example_blotter`. Blank template: `desk/daily_blotter/daily_market_blotter.md`.

Date: Day 1, Monday (hypothetical)  Time: 07:20 ET  Analyst: K.P. (initials)   *(Filled in by hand; strike-throughs initialed, nothing erased.)*

## 1. Overnight and pre-open levels
| Market | Prior close | Now | Change | Note (cause, if known) |
|---|---|---|---|---|
| 2-yr Treasury yield | 4.12% | 4.18% | +6 bp | Front end repricing Fed path into CPI (Wed) |
| 10-yr Treasury yield | 4.31% | 4.35% | +4 bp | Follows 2-yr; no long-end news found |
| 2s10s spread | +19 bp | +17 bp | −2 bp | Bear flattening |
| 10-yr TIPS real yield | 1.92% | 1.95% | +3 bp | Most of the 10-yr move is real, not breakeven |
| Fed funds futures: implied rate at next meeting | 4.10% | 4.16% | +6 bp | Fewer cuts priced; consistent with 2-yr |
| S&P 500 futures (ES) | 5,800 | 5,771 | −0.50% | Unknown; no single headline |
| DXY / EUR/USD / USD/JPY | EUR/USD 1.0850 | 1.0817 | −0.30% (EUR) | USD firmer with front-end yields |
| WTI / Brent | WTI 72.40 | 73.12 | +0.99% | Unknown |
| Gold | 2,410 | 2,398 | −0.50% | Real yields up |
| IG / HY credit spread (index) | IG 98 bp | IG 100 bp | +2 bp | Small; watch new-issue concessions |
| REIT index (industrial) | 1,250 | 1,240 | −0.80% | ~1.6x the ES move; rate-sensitive |

Sources and times: Treasury yields and futures from the desk feed at 07:10; REIT index prior close from exchange data; all hypothetical for this example. Reliability grade A for all prices (Chapter 25, §25.6.2).

## 2. Today's calendar
| Time | Release / event | Consensus | Prior | What would surprise? | Which positions are exposed? |
|---|---|---|---|---|---|
| Wed 08:30 | CPI (core m/m) | 0.3% | 0.3% (check revision) | Core ≥ 0.5% or ≤ 0.1% | TY short (gap risk), REIT basket, ES |
| Fri 15:30 | CFTC COT (positions as of Tue close) | n/a | Leveraged funds net short TY | A large cut in the net short would mean short covering has begun | TY short |
| Thu 10:00 | Investment committee: industrial bid | n/a | n/a | Lender call result (see §3) | Second industrial building |

## 3. CRE financing pulse
Lender quotes received (spread / index / proceeds): Lender 1: 5-yr fixed, +215 bp over 5-yr UST, 60% LTV max, 1.35x DSCR — **wider by 25 bp vs last quarter**; Lender 2: +225 bp, 55% LTV. *Grade: B reliability (indicative, not committed), not widely known.*
Loan sale, CMBS delinquency or special-servicing news: special-servicing rate for the property type up for a third month (industry report). *Grade: B; partly known.*
Transaction heard of (asset, price, cap, buyer type): two submarket industrial sales near 6.25% cap, private buyers, closed about four months ago — *source: transaction database; reliability B; stale and selected (only assets that traded). Grade C for current pricing.*

## 4. What changed my view today?
Prior belief → Evidence → Updated belief (probability or range):
1. P(next FOMC meeting holds rather than cuts): 35% → fed funds futures +6 bp, 2-yr +6 bp, TIPS +3 bp → **45%**. Dated; to be scored at the meeting.
2. P(industrial cap rates widen ≥ 50 bp in 12 months): 40% → lenders wider; servicing rate up; comps stale; sell-side "stable" → **45.65% if lender and servicing signals share a cause; 55.75% if independent** (Example 25.3). Action: ask both lenders *why* spreads widened before Thursday.

## 5. Positions and risk check
| Position | Size | P&L since entry | Distance to invalidation | Action today |
|---|---|---|---|---|
| Short TY futures (entry yield 4.20%) | 40 contracts, DV01 \$3,400/bp | +15 bp × \$3,400 = **+\$51,000** | Invalidation at 4.05% → 30 bp away (\$102,000 of profit to give back) | Hold; ticket gap-risk note into CPI |
| Long ES (entry 5,850) | 10 contracts, \$50 multiplier | (5,771 − 5,850) × 50 × 10 = **−\$39,500** | Invalidation 5,650 → 121 points, a further −\$60,500 | Hold; no add before CPI |
| REIT basket | \$2.0m, beta 1.1 | (from journal) | Thesis review Friday | None |
| Hotel / industrial | Appraisal marks | Stale marks; REIT index −0.8% today | Loan extension test review due this month | Flag in register |

Liquidity reserve vs. requirement: \$3.2m vs \$2.5m requirement (hypothetical) — OK.   Largest single risk today: **hotel equity under a cap-rate shock** (Example 25.4), not the TY short.

*Close (16:20):* P&L line and attribution flags entered in the journal; no change of view after the close. — K.P.
