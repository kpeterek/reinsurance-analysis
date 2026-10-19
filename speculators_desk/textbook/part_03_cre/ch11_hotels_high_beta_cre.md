# Chapter 11 — Hotels: The High-Beta CRE Asset

> **Status:** Complete (v1.0). Every number in this chapter, in the eight hotel cases of §11.6, in the problems, and in the solutions is reproduced in `tests/test_ch11_examples.py`. Problems: `problems/questions/ch11_problems.md`. Solutions: `problems/solutions/ch11_solutions.md`. Sources: `references/sources_ch11.md`. Drills D056–D070. The companion negotiation case is Case D (`cases/hypothetical/case_D_hotel_pip_negotiation/`). Historical figures marked *(verification pending)* have not yet been checked against a primary source.

## Learning objectives

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

## 11.1 Opening investment problem: the Monday BOV

A family owner calls on Monday. They own a 132-room upscale select-service hotel with a national flag in a growing suburban submarket. They want a broker opinion of value (BOV) by Friday because "it's a record year and the market is hot". The facts they send are [HYPOTHESIS], as is every hotel in this chapter:

* **T-12 performance.** Occupancy 71.0%, ADR \$158.50, RevPAR \$112.54. Last year: 74.0% and \$142.00, RevPAR \$105.08. "RevPAR up 7.1%."
* **Owner's valuation.** "EBITDA is \$1.46 million. Hotels trade at 9 caps, so it's worth \$16.2 million."
* **The brand** has told the owner, informally, that "a refresh will be needed on any sale". No property improvement plan (PIP) letter has been issued. Your recent experience with this brand's change-of-ownership PIPs on similar vintages is about \$14,000 per key.
* **The STR report** (a competitive-set benchmarking report of the kind STR, now part of CoStar, sells to hotel owners) is attached but the owner has not read it.

You have four questions to answer before Friday. What is the hotel earning, on the line a buyer capitalizes? Is its revenue growth its own, or the market's? What will a buyer deduct for the renovation, and is the owner better off selling now or after renovating? And what would make you refuse to put a number on the page? Section 11.11 returns to the decision after the chapter has built the tools. Cases 11.1–11.8 (§11.6) extend each tool to a full decision.

---

## 11.2 Economic intuition: why hotels have the highest beta in CRE

An apartment lease reprices once a year. An office lease reprices once a decade. A hotel room reprices every night. That single fact explains most of what follows.

**The lease term is one night.** There is no rent roll to protect income when demand falls, and no contractual rent bump to lift it when demand rises. Revenue moves with the business cycle, air travel, corporate travel budgets, group meeting calendars, and local events, with a lag of days rather than years. When demand falls, managers face a choice between holding rate and losing occupancy or cutting rate to defend occupancy. Either way revenue falls immediately.

**A hotel is an operating business wrapped around real estate.** The owner employs (directly or through a manager) a housekeeping, front-desk, engineering, sales and food-and-beverage staff. Labor is typically the largest cost line [HYPOTHESIS for any specific hotel; industry cost surveys should be cited when a figure is needed]. Much of that labor is fixed in the short run: a hotel cannot run a front desk with 70% of a clerk. Fixed costs create **operating leverage**. A 5% revenue change can move NOI by 14–20%, as Example 11.2 shows.

**Revenue-based fees are senior to the owner.** Franchise fees are charged on rooms revenue and base management fees on total revenue. They are paid before the owner sees a dollar of NOI, and they do not fall when margins compress. The owner holds the residual. The brand and the manager hold claims that behave like senior revenue participations. The incentive fee gives the manager a call option on the upside (Case 11.4).

**Capital wears out fast and on a schedule set by someone else.** Carpets, case goods, mattresses and bathrooms wear out on cycles of years, not decades. The brand enforces standards through PIPs at relicensing and on change of ownership. A hotel owner therefore carries two capital claims: the **FF&E reserve** (a recurring percentage of revenue that funds normal replacement) and the **PIP** (a lumpy, brand-mandated renovation that the reserve rarely covers in full). A buyer who capitalizes NOI without pricing the next PIP is buying the hotel twice.

**Value includes a business.** The price of a hotel pays for land and building, for the furniture, fixtures and equipment, and for an operating business with a flag, a workforce, a reservation system and a booking pace. How that total is allocated affects property taxes, depreciation, lender collateral and appraisal (Case 11.7).

**Supply arrives in lumps, and capital is pro-cyclical.** New hotels take years to entitle and build. Supply that was financed at the top of a cycle opens into the downturn. Hotel lenders retreat faster than lenders on leased property, because the collateral's income can disappear within a quarter. The historical episode in §11.10 shows how fast.

### Demand segments, seasonality and revenue management

A hotel sells the same room to different buyers at different prices on different terms. The segments behave differently and must be underwritten separately.

* **Transient** guests book individually, through brand channels, online travel agencies (OTAs), the global distribution system or directly. They pay the highest rates and the highest acquisition costs, and they disappear first in a downturn.
* **Group** business (associations, corporate meetings, sports teams, weddings) books blocks of rooms months in advance, at a negotiated rate, and usually brings banquet and meeting-room revenue. Groups give the hotel a base of occupancy that can be forecast, at the cost of capacity that cannot be resold at short notice. Contracts carry cutoff dates and attrition clauses that shift some of the forecast risk back to the group.
* **Contract** business (airline crews, rail crews, long-term project housing) pays the lowest rate for guaranteed volume, often every night of the year.

The mix matters because contribution, not ADR, is the objective. A group room at \$148 with banquet profit can be worth more than a transient room at \$172 that carries a 15% commission (Example 11.5). An ADR-maximizing strategy that drops low-rate contract business can lower RevPAR and profit if the freed rooms do not refill.

**Seasonality** adds a time dimension. Resorts, ski hotels and hotels near universities or state capitals earn most of their annual cash in a few months. Fixed costs and debt service arrive every month, and annual bills (insurance, property tax) arrive when they are due, not when revenue does. Annual ratios conceal this. A hotel with a comfortable annual DSCR can run out of cash every winter (Case 11.5).

**Revenue management** is the practice of setting price and availability by night and segment to maximize contribution given a demand forecast. Its two core decisions are rate (what to charge transient guests given the booking pace) and displacement (whether to give capacity to a group or contract at a lower rate). Both are bets on a forecast. The analyst's question is not whether the revenue manager "is good", but whether the hotel's rate and mix decisions are consistent with its demand: whether the penetration indices show rate gained at the expense of share, and whether accepted groups would have survived a displacement test.

### Labor

Labor ties hotel cost to wage markets that move independently of hotel demand. Some labor is variable (housekeeping time per occupied room), some is semi-fixed (front desk, night audit, maintenance), and some is fixed (the general manager, the director of sales, the chief engineer). Wage inflation, scheduling rules, benefits and union contracts change all three. In underwriting, labor should be modeled as hours times wage in each category, not as a percentage of revenue, because a percentage-of-revenue assumption makes labor fall when the hotel's revenue falls and rise when ADR rises. Neither is true in the short run (Cases 11.1 and 11.6).

### The speculator's view

The result is an asset whose cash flow has a high beta to the economy and whose value has a high beta to its cash flow. To a speculator this is not a defect. It is the reason hotels offer the widest mispricings in CRE. Sellers anchor on peak NOI, buyers forget PIPs, lenders size on trailing figures, and owners confuse a rising market with rising share. Each of these errors has a price, and this chapter computes it.

---

## 11.3 Technical definitions

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

## 11.4 Equations and derivations

### 11.4.1 The RevPAR identity and its decomposition

With $N$ rooms, $D$ days, $RN$ rooms sold and rooms revenue $RR$:

$$\text{Occ} = \frac{RN}{N D}, \qquad ADR = \frac{RR}{RN}, \qquad RevPAR = \frac{RR}{N D} = \text{Occ} \times ADR.$$

Growth multiplies: $(1+g_{RevPAR}) = (1+g_{Occ})(1+g_{ADR})$. Logs make the decomposition additive and exact:

$$\ln(1+g_{RevPAR}) = \ln(1+g_{Occ}) + \ln(1+g_{ADR}).$$

The penetration indices are ratios to the comp set (subscript $c$):

$$MPI = 100\frac{\text{Occ}}{\text{Occ}_c}, \quad ARI = 100\frac{ADR}{ADR_c}, \quad RGI = 100\frac{RevPAR}{RevPAR_c} = \frac{MPI \times ARI}{100}.$$

**Why it matters.** RevPAR growth that merely matches the comp set's growth is the market's tide. Only a change in RGI is the hotel's own performance. A buyer pays for the tide through the cap rate and for the share through the NOI.

### 11.4.2 Cost structure and the NOI equation

Write total revenue as $TR = RR(1+o)$, where $o$ is other revenue as a fraction of rooms revenue. Group costs by behavior:

* $c$: variable cost per occupied room (housekeeping labor, amenities, laundry, breakfast, in-room supplies);
* $v$: costs proportional to revenue (franchise fees, management fees, card fees, commissions, the FF&E reserve, other-department costs where other revenue scales with rooms revenue);
* $F$: costs fixed in the short run (fixed labor, A&G, S&M, POM, utilities base load, property tax, insurance).

Then

$$NOI = TR(1-v) - c\,RN - F = RN\big[ADR(1+o)(1-v) - c\big] - F. \tag{11.1}$$

The bracket is the **contribution per occupied room**. Every equation below follows from (11.1).

### 11.4.3 Flow-through: rate versus occupancy

Raise RevPAR by a fraction $x$ through rate alone. Rooms sold are unchanged, so $c\,RN$ is unchanged and

$$\Delta NOI_{rate} = \Delta TR\,(1-v) \;\Rightarrow\; FT_{rate} = 1 - v.$$

Raise RevPAR by $x$ through occupancy alone. Rooms sold rise by $x\,RN$, so

$$\Delta NOI_{occ} = \Delta TR(1-v) - c\,x\,RN \;\Rightarrow\; FT_{occ} = 1 - v - \frac{c}{ADR(1+o)}.$$

The difference, $c/[ADR(1+o)]$, is the variable cost of servicing the extra guests as a share of the revenue they bring. For a limited-service hotel with \$36 of variable cost per occupied room and a \$157.50 total revenue per occupied room, it is about 23 points of flow-through (Example 11.2). Rate-led growth is worth more than occupancy-led growth of the same size. That is why revenue managers fight for rate, and why a buyer should ask how RevPAR growth was achieved, not just how much there was.

**Degree of operating leverage.** From (11.1), $\%\Delta NOI / \%\Delta TR = TR(1-v)/NOI$ for rate-led change. A hotel with a 19% NOI margin and $v = 0.25$ has DOL of about $0.75/0.19 \approx 3.9$. A multifamily property with a 60% NOI margin and nearly all-fixed operating costs has DOL near $1/0.6 \approx 1.7$ [HYPOTHESIS: an illustrative apartment cost structure]. The hotel is more than twice as sensitive to revenue.

### 11.4.4 The fee stack

$$\text{Franchise fees} = (r_{roy} + r_{mkt} + r_{res} + r_{loy})\,RR \;(+\text{per-room or per-stay charges}),$$
$$\text{Base management fee} = b\,TR,$$
$$IMF = i \times \max\!\big(0,\; ACF - \pi K\big), \qquad ACF = GOP - b\,TR - \text{fixed charges} - f\,TR,$$

where $ACF$ is "available cash flow" (here equal to NOI), $\pi$ is the owner's priority rate and $K$ the owner's invested capital. Contracts define ACF and the priority in many ways. Read the definitions; do not assume them. The base fee and franchise fees behave like senior revenue claims. The IMF is a call option held by the manager, struck at the owner's priority.

### 11.4.5 EBITDA, NOI and the cap rate that goes with each

$NOI = EBITDA - fTR$ with reserve rate $f$. A cap rate is a ratio to a named line. If the market prices a hotel at $c_{NOI}$ on NOI, the equivalent rate on EBITDA is

$$c_{EBITDA} = \frac{EBITDA}{V} = c_{NOI}\,\frac{EBITDA}{NOI} > c_{NOI}.$$

Applying $c_{NOI}$ to EBITDA overstates value by exactly $fTR / c_{NOI}$: the capitalized reserve. At a 9% cap and a \$218,544 reserve, that is \$2.43 million (Example 11.3).

**Normalization** applies before any cap rate: remove non-recurring revenue and expenses, impute market management and franchise costs if the owner self-manages or the flag will change, replace owner compensation with a market GM cost, re-underwrite insurance and reassessed property tax, and deduct the reserve. Case A works through a full normalization. This chapter assumes it has been done.

### 11.4.6 Break-even occupancy

Set (11.1) less debt service $DS$ equal to zero and solve for rooms sold:

$$RN^* = \frac{F + DS}{ADR(1+o)(1-v) - c}, \qquad \text{Occ}^* = \frac{RN^*}{N D}. \tag{11.2}$$

`sdesk.hotel.breakeven_occupancy(rooms, adr, fixed_costs, debt_service, variable_cost_per_occupied_room, variable_pct_of_revenue, other_revenue_pct_of_rooms=o)` implements (11.2). Two cautions. First, (11.2) holds ADR fixed; in a real downturn ADR falls with occupancy, so the true break-even is higher (Case 11.6 stresses both). Second, $F$ is fixed only in the short run. Over a year, managers cut fixed labor, which is why break-even analysis is a liquidity tool for the next few quarters and not a long-run value tool.

### 11.4.7 Displacement

A group of $G$ rooms per night for $n$ nights at rate $r_g$ is worth accepting if its total contribution, including banquet and meeting-room profit, exceeds the contribution of the transient business it displaces:

$$G_{picked}\,n\,\big[r_g(1-v_g) - c + s_g m_g\big] \;>\; \sum_{\text{nights}} D_t\big[ADR_t(1-v_t) - c + s_t m_t\big] + \text{shoulder-night losses},$$

where $D_t$ is displaced transient rooms (unconstrained demand minus what still fits), $v_g$ and $v_t$ include commissions specific to each channel, $s$ is ancillary spend per occupied room and $m$ its departmental margin net of fees. The **break-even group rate** sets the two sides equal. Displacement depends on a demand *forecast*, so the decision is a bet on that forecast and must be stress-tested (Case 11.2).

### 11.4.8 Hotel debt sizing

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

### 11.4.9 PIP-adjusted price and the return on renovation

A buyer who must complete a PIP can pay

$$P = V_{stab} - PIP(1+\kappa) - \text{Displacement} - \text{Carry and soft costs} - \rho\,PIP(1+\kappa), \tag{11.3}$$

with contingency $\kappa$ and required profit $\rho$ on renovation capital. `sdesk.hotel.pip_adjusted_price` implements (11.3). The last term is the one sellers forget: renovation capital bears execution risk, and a buyer who does a PIP "at cost" is working for free.

The **RevPAR lift needed** for a PIP to earn a hurdle $h$ on its all-in cost is

$$\Delta RevPAR^* = \frac{h \times PIP(1+\kappa)}{N \times D \times FT_{NOI}}, \tag{11.4}$$

where $FT_{NOI}$ is NOI flow-through on rooms revenue. When $\Delta RevPAR^*$ exceeds any plausible lift, the PIP does not pay for itself. It may still be worth doing, because the alternative is the loss of the flag (Case D, Case 11.3). That comparison, and not the stand-alone return, decides most PIPs.

### 11.4.10 Going-concern allocation

$$V_{TAB} = V_{real\ property} + V_{FF\&E} + V_{intangibles}.$$

Appraisers disagree about how to measure the intangible component. One family of methods holds that deducting market management and franchise fees from income already strips out the return to the business, so the remaining value is real property plus FF&E. Another identifies specific intangibles (assembled workforce, flag, booking pace, start-up costs) and values each. The method matters because property tax is levied on real property (and, in some jurisdictions, tangible personal property), not on intangibles. Income-tax recovery periods differ by asset class. Lenders take real property and FF&E as collateral but cannot foreclose on a workforce. Case 11.7 quantifies all three effects.

### 11.4.11 Seasonal working capital

Let $CF_m$ be monthly cash flow after debt service and $S_m = \sum_{j\le m} CF_j$. The working-capital reserve needed to survive the off-season without new equity is the largest peak-to-trough decline in $S$:

$$W = \max_{m}\Big(\max_{j \le m} S_j - S_m\Big).$$

If a cash trap sweeps peak-season surplus to the lender, the owner can no longer fund the trough from that surplus, and the equity requirement rises toward the sum of all negative months (Case 11.5).

---
## 11.5 Worked examples

The five examples below build the toolkit. The eight comprehensive cases in §11.6 apply it to full decisions. All inputs are [HYPOTHESIS]. Every number is reproduced in `tests/test_ch11_examples.py`.

### Example 11.1 — RevPAR up 7.1%, share down: the opening hotel against its comp set

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

### Example 11.2 — Flow-through: rate-led versus occupancy-led RevPAR growth

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

### Example 11.3 — The fee stack, and the cap rate that belongs to EBITDA

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

### Example 11.4 — How a hotel lender sizes the same NOI

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

### Example 11.5 — Segment mix: ADR-maximizing is not contribution-maximizing

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

## 11.6 Eight comprehensive hotel cases

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

### Case 11.1 — RevPAR up 6%, NOI down 17%: a flow-through diagnosis

#### Situation

You are the asset manager for a fund that owns a 120-room upscale select-service hotel. The operator's year-end letter opens: "RevPAR grew 6.1%, well ahead of budget." The fund's controller notes that NOI fell 17%. The investment committee wants to know which statement describes the asset, whether the decline is permanent, and what number a buyer would capitalize.

#### Data (Exhibit 11.1-1)

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

#### Solution

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

#### Decision

The committee should **underwrite Year 2 NOI as the base**, adjusted only for items shown to be non-recurring, and should not accept "RevPAR +6%" as evidence of value creation. Three actions follow:

1. **Channel mix.** Ask the operator for a channel-contribution report: rooms revenue net of commissions and loyalty costs, by channel. A shift to OTA business is justified only if the displaced alternative was empty rooms. At 76% occupancy on a 120-room hotel, it is unlikely that every one of the 2,628 extra room-nights required an OTA.
2. **Labor productivity.** Housekeeping minutes per occupied room (33 minutes here) and fixed staffing are the levers. Case 11.6 quantifies them.
3. **Budget discipline.** A budget that rewards RevPAR rather than GOP or NOI will produce this outcome again. Align the operator's incentive with the owner's line (Case 11.4).

**Decision consequence.** For a sale, the market will capitalize Year 2 NOI (\$790,516), not Year 1. Presenting Year 1 NOI as "normalized" without evidence that commissions and costs will reverse is seller anchoring of the kind Case A dismantles. The fund's book value should be marked toward \$8.8 million, not \$10.6 million, until the operator demonstrates a reversal.

**What would change the decision.** Evidence that the OTA shift filled rooms that would otherwise have gone empty, and that it was temporary (for example, a brand-channel outage). A one-off insurance spike reversed by a rebid. A demand generator that supports occupancy without commission (a new corporate account).

**Reproduce.** `tests/test_ch11_examples.py::test_case_11_1`

---

### Case 11.2 — The group on peak nights: displacement and the minimum rate

#### Situation

You are director of revenue management at a 300-room full-service hotel. A medical association requests a block of 180 rooms per night for Tuesday to Thursday (three nights) in the second week of October, at a group rate of \$189, with banquets. Your transient forecast for those nights is strong. The sales director wants to sign today.

#### Data (Exhibit 11.2-1)

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

#### Solution

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

#### Decision

**Counter with the alternate dates at \$189** (net +\$72,161). If the association insists on Tuesday–Thursday, accept at \$189 only with (a) a cutoff at 21 days with no extension, (b) an attrition clause at 80% with liquidated attrition charges, and (c) a food-and-beverage minimum that protects the \$110 banquet assumption. If the transient pace report three weeks before the first counter shows demand trending to the high case, do not accept below about \$197.

**Decision consequence.** The decision looks like "accept" on revenue (+\$47,545) and still "accept" on expected contribution (+\$19,480). But the margin of safety is thin: one scenario in five destroys value, and the expected gain is smaller than the gain from moving the dates. Revenue management is a pricing decision under a forecast. The output is a minimum rate conditional on demand, not "yes". Note also what the revenue figure hides: accepting adds \$47,545 of revenue but only \$17,414 of contribution, because the group arrives with commissions and banquet costs. A sales team paid on revenue will always want the group.

**What would change the decision.** A pace report that shows transient demand building above 240 (decline or raise the rate). Evidence that the association would return annually on low-demand dates (the lifetime value of the account may justify a one-time displacement). A banquet minimum below \$110.

**Reproduce.** `tests/test_ch11_examples.py::test_case_11_2`

---

### Case 11.3 — Renew the flag, convert, or go independent

#### Situation

You advise the owner of a 140-room upper-midscale hotel whose franchise agreement expires in 12 months. Three options are on the table: renew with the current brand (which requires a PIP), convert to a lower-fee conversion brand from another family (smaller PIP, key money offered), or operate as an independent (no brand fees, no PIP, but higher distribution costs and a weaker demand engine). The comp set's stabilized RevPAR is \$95.00.

#### Data (Exhibit 11.3-1)

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

#### Solution

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

#### Decision

**Renew**, provided the PIP letter is within 10% of \$2.24 million and the new agreement runs at least ten years with a reasonable area of protection.

**Decision consequence.** The brand's fees are high, but the brand's RGI premium pays for them with room to spare. The fee comparison that owners instinctively make (12% versus 0%) is the wrong one. The right comparison is NOI after fees *and* after the demand the fees buy. Independence fails here not because brands are always better but because an RGI of 103 without a reservation system and loyalty program is not a credible assumption for this upper-midscale hotel. Conversion is the defensible fallback if the PIP letter comes in high: the gap between renewal and conversion is only \$0.53 million of net value, so a renewal PIP above about \$2.77 million (\$2.24 million plus \$0.53 million) reverses the ranking.

**What would change the decision.** A location with strong direct demand (a university, a hospital campus, a resort destination) where an independent can plausibly reach RGI above 100. A renewal PIP above \$2.77 million. A conversion brand with a demonstrated RGI above 104 in this market. A lender that will not finance an independent at all, which would make independence worse than the table shows.

**Reproduce.** `tests/test_ch11_examples.py::test_case_11_3`

---

### Case 11.4 — The management contract: incentive fee and owner's priority

#### Situation

You represent the owner of a 250-room full-service hotel managed under a third-party contract. The owner has invested \$52 million (purchase plus renovation). The manager proposes to cut the base fee from 3% to 2% of total revenue in exchange for a larger incentive fee with a lower owner's priority. The manager calls it "putting our money where our mouth is". The owner asks whether to accept.

#### Data (Exhibit 11.4-1)

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

#### Solution

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

#### Decision

**Counter, do not accept as proposed.** The proposal is nearly neutral in expectation (−\$14,000 a year to the owner) but redistributes risk: it gives the owner \$175,000 more in a downturn and takes \$42,500 in the base case and \$146,000 in a strong year. The manager is selling a put (lower base fee in bad years) and buying a call (a 25% share struck lower). A reasonable counter keeps the lower base fee, keeps the priority at 8%, and accepts a 25% incentive share, with an annual cap on the incentive fee and a performance test (for example, termination without fee if RGI is below 95 and GOP below 90% of budget in two consecutive years).

**Decision consequence.** Valued at an 8.5% cap rate, the base-case reduction in owner cash (\$42,500) is a \$500,000 transfer to the manager in sale value, because buyers capitalize NOI after all fees. The GOP-based benchmark shows why contract structure matters more than the headline percentage: a "10% incentive" on GOP without a priority costs the owner \$608,000 a year in expectation versus the existing contract, because it pays the manager even in years when the owner earns a small fraction of the priority. Incentive fees are options. Value them as options, with scenarios, before calling them "alignment".

**What would change the decision.** A manager track record of beating budget GOP by enough to move the base case above the \$6.79 million crossover by a wide margin (the owner then pays more but earns more). A lender requirement that management fees be subordinated below debt service. A planned sale within two years, in which case an unencumbered or terminable contract may be worth more than any fee saving.

**Reproduce.** `tests/test_ch11_examples.py::test_case_11_4`

---
### Case 11.5 — The seasonal resort: working capital and the cash trap

#### Situation

A fund is buying a 160-room independent beach resort with a \$21.0 million loan at 7.25%, 25-year amortization (monthly payments). The loan has a cash-management provision: if trailing-12 DSCR falls below 1.30x, all cash after operating expenses, reserves and debt service is swept monthly into a lender-controlled account and is not released until DSCR exceeds the trigger for two consecutive quarters. The investment committee asks how much working capital the fund must hold, and what the cash trap does to that number.

#### Data (Exhibit 11.5-1)

| Month | Occ | ADR | Month | Occ | ADR |
|---|---:|---:|---|---:|---:|
| Jan | 42% | \$165 | Jul | 93% | \$345 |
| Feb | 50% | \$185 | Aug | 85% | \$300 |
| Mar | 78% | \$260 | Sep | 55% | \$205 |
| Apr | 80% | \$255 | Oct | 50% | \$190 |
| May | 82% | \$270 | Nov | 40% | \$160 |
| Jun | 90% | \$320 | Dec | 45% | \$185 |

Other revenue (F&B, spa, parking) 35% of rooms revenue at a 65% departmental cost ratio. Variable rooms cost \$55 per occupied room. Undistributed \$220,000 per month fixed plus 6% of revenue. Management fee 3% of total revenue; distribution costs 8% of rooms revenue. FF&E reserve 4% of total revenue, deposited monthly with the lender. **Property tax \$540,000 paid in January; insurance \$720,000 paid at the June renewal** (cash timing, not accrual).

#### Solution

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

#### Decision

**Fund a working-capital reserve of \$1.7 million at closing** (the trapped-stress requirement, rounded up), or negotiate the loan so that it is not needed: a **seasonality reserve** in which the lender sweeps a fixed amount from March–August cash into a reserve that is released to pay operating shortfalls from September to February, with the cash-management test applied to a trailing-12 figure that excludes the reserve deposits. Negotiate also for monthly insurance installments (premium financing) and to pay property tax in installments where the jurisdiction allows, which reduces the January and June spikes.

**Decision consequence.** An annual DSCR of 1.37x hides a business that runs out of cash every winter. A buyer who underwrites annually and holds no reserve will be writing capital calls in its first January, and a 5% rate decline converts the lender's protective provision into a liquidity squeeze precisely when the owner needs the summer cash. The \$1.7 million is about 2.5 years of the base case's annual cash flow to the owner (\$667,361), which is why seasonal assets support less leverage than their annual DSCR suggests.

**What would change the decision.** A lender willing to test DSCR on a trailing-12 basis with a seasonality reserve. A group or wholesale contract that fills the shoulder months. A revolving credit line from the sponsor, which substitutes contingent capital for a funded reserve, at the risk that the line is unavailable in the same downturn that triggers the trap.

**Reproduce.** `tests/test_ch11_examples.py::test_case_11_5`

---

### Case 11.6 — The labor-cost shock and break-even occupancy

#### Situation

A city adopts a hospitality minimum-wage ordinance. For a 150-room select-service hotel you own, the loaded housekeeping wage rises from \$18.00 to \$21.60 an hour (+20%), and fixed labor (front desk, maintenance, management) rises 15% to preserve pay differentials. The lender asks for an updated break-even analysis; the investment committee asks what operational response restores NOI.

#### Data (Exhibit 11.6-1)

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

#### Solution

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

#### Decision

**Treat the shock as permanent and re-engineer the labor model before relying on rate.** A 4.5% ADR increase that the comp set is not also taking will cost share (Example 11.1); every competitor in the city faces the same ordinance, which makes some pass-through plausible, but the pass-through should be measured in the STR data over the following two quarters rather than assumed. Housekeeping productivity (stayover cleaning on request, room-attendant routing, linen programs) can recover most of the variable effect. Report to the lender the post-shock DSCR and the 7-point cushion, and agree in advance what happens in a recession, because the stressed DSCR is below 1.0x.

**Decision consequence.** A 20% wage increase on one job category cost 12% of NOI and \$1.9 million of value, and cut the break-even cushion from 11 points to 7. The broader lesson is that labor is a fixed cost in the short run and a variable cost in the long run only if management redesigns the work. In underwriting, apply labor inflation separately to fixed and variable labor; a single "expense growth" assumption misses the operating leverage.

**What would change the decision.** Evidence that the comp set has already raised rates (pass-through is market-wide). A franchise standard that prevents the stayover-cleaning change. A scheduled loan maturity within the stress window, which would make the DSCR the binding issue rather than the value.

**Reproduce.** `tests/test_ch11_examples.py::test_case_11_6`

---

### Case 11.7 — A BOV under stress, with a going-concern allocation

#### Situation

A special servicer has taken title to a 210-room full-service hotel and asks your brokerage for a BOV to set a list price. The hotel is recovering from a demand shock and a period of underinvestment. The servicer's asset manager also asks how the sale price should be allocated among real property, FF&E and intangibles, because a buyer's counsel has asked for an allocation in the purchase agreement.

#### Data (Exhibit 11.7-1)

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

#### Solution

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

#### Decision

**Publish a BOV of \$31.9 million most probable, \$26.5–36.7 million range, list at about \$33.5 million**, with the scenario weights, the recovery path and the deferred capital shown. Recommend that the servicer **not** state an allocation in the marketing materials, but agree one with the buyer before signing, consistent with an appraisal that documents the intangible components. The buyer will prefer Method B (lower property tax, faster depreciation); the servicer is largely indifferent because it is exiting, but the allocation must be defensible, because the assessor will see the deed price and may challenge any reduction.

**Decision consequence.** Allocation is worth about \$0.35 million in capitalized property-tax value and \$0.13 million in income-tax present value on a \$31.9 million hotel: about 1.5% of value. It is not a pricing lever for the seller, but it is a negotiating item the buyer values. The BOV's larger lesson is that under stress neither the T-12 (\$22.1 million) nor the peak (\$42.4 million) is a value. The defensible number is a probability-weighted recovery path, and the BOV should show the weights so that the servicer can disagree with them explicitly.

**What would change the decision.** A different jurisdiction (one that taxes intangibles, or does not tax personal property) changes the allocation economics. A stronger buyer pool (more 1031 or owner-operator demand) would justify listing nearer the base DCF. A franchise termination notice would reduce the base-case NOI and add a PIP, moving value toward the downside.

**Reproduce.** `tests/test_ch11_examples.py::test_case_11_7`

---

### Case 11.8 — Disposition timing: sell now or after the PIP?

#### Situation

A private owner holds a 130-room select-service hotel. The brand has issued a PIP of \$2,340,000 (\$18,000 per key), due within 18 months or on any sale. In-place NOI is \$1,300,000 and slipping as the product ages. A renovated hotel would earn a stabilized NOI of \$1,550,000. The owner can sell now to a buyer who will price the PIP, or renovate and sell in two years.

#### Data (Exhibit 11.8-1)

| Item | Value |
|---|---|
| Stabilized NOI (renovated) / cap rate | \$1,550,000 / 9.0% |
| Buyer's pricing of the PIP | contingency 15%; displacement \$260,000; carry and soft costs \$150,000; required profit 15% on PIP capital |
| Seller's costs | 2.5% of price |
| Owner's discount rate (unlevered) | 11% |
| Owner's hold path | Year 1: NOI \$1,300,000 less \$260,000 displacement, PIP paid (treated as year-end); year 2: stabilized NOI; sale at end of year 2 on year-3 NOI (\$1,550,000 × 1.03) less 2.5% |
| Hold scenarios | Good: exit cap 8.75%, no overrun (p = 0.35). Base: 9.0%, 8% overrun (p = 0.45). Bad: 9.75%, 25% overrun (p = 0.20) |

#### Solution

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

#### Decision

**Renovate and sell only if three conditions hold:** the owner can fund about \$2.5–2.9 million of PIP cost without forced selling in the bad case; the owner can accept a one-in-five chance of ending \$0.86 million worse off; and the owner's view of the exit cap two years out is comfortably inside 9.39%. Otherwise **sell now**, and use the analysis to negotiate the buyer's deductions: a 15% contingency and 15% required profit on a PIP whose scope is fixed by a letter are negotiable, and every five points of either is worth about \$135,000 of price.

**Decision consequence.** The "PIP profit" the buyer charges (\$403,650 plus the contingency spread) is the price of transferring execution and market risk. An owner who renovates captures it in expectation but bears both risks, plus two years of exposure to exit cap rates. This is a speculation on the owner's own execution and on the cap rate, not a free gain. The 39 bp break-even is the number to put in front of the owner: a modest widening in cap rates erases the advantage.

**What would change the decision.** A firm fixed-price construction bid (cuts the overrun tail). Evidence that the buyer pool is thin for unrenovated hotels (raises the buyer's discount, favoring renovation). A loan maturity inside the renovation period (forces a sale at the worst moment, favoring selling now). A lender willing to fund 75% of the PIP (changes the owner's liquidity condition, but not the risk).

**Reproduce.** `tests/test_ch11_examples.py::test_case_11_8`

---

## 11.7 CRE application: the hotel inside a real estate portfolio

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
## 11.8 Hotel valuation practice: cap rates, BOVs, transaction costs, timing and anchoring

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

## 11.9 When the relationship fails

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

## 11.10 Historical episode: U.S. hotels after 11 September 2001 and in 2020

This section uses published STR figures, as reported in contemporaneous press coverage, together with BLS employment data and Trepp CMBS delinquency data. Verification status is shown in `references/sources_ch11.md`. Figures are national averages. Individual hotels, markets and segments diverged widely.

### Date and environment

**2001.** The U.S. expansion that began in March 1991 ended in March 2001 [FACT; NBER business-cycle chronology, ch11-S06]. Hotel demand was already weakening before September. In August 2001, STR reported U.S. occupancy of 67.7% and RevPAR down 4.4% year over year to \$57.08 [FACT; STR figures as reported in trade press, ch11-S02, VERIFIED-SECONDARY]. The NBER later dated the trough to November 2001 *(verification pending)*.

**2020.** The NBER dated a business-cycle peak in February 2020 and a trough in April 2020, a two-month recession [FACT; NBER, ch11-S06]. In 2019 U.S. hotels had posted record nominal ADR and RevPAR: occupancy 66.1%, ADR \$131.21, RevPAR \$86.76 [FACT; STR via trade press, ch11-S03, VERIFIED-SECONDARY].

### What happened

**September 2001.** STR reported U.S. occupancy down 10.6 percentage points to 55.9%, and RevPAR down 23.4% to \$44.30, for September 2001 [FACT; ch11-S01, VERIFIED-SECONDARY]. The implied prior-year figures are occupancy $0.559 + 0.106 = 66.5\%$ and RevPAR $44.30/0.766 = \$57.83$. The implied ADR fell from $57.83/0.665 = \$86.97$ to $44.30/0.559 = \$79.25$, a decline of 8.9% [INFERENCE: arithmetic on the reported figures]. Note the two ways to state the occupancy loss: −10.6 *points*, or −15.9% *in percentage terms*. Press releases mix them, so state which one you mean. A full-year 2001 U.S. figure is not used here *(verification pending)*.

**April 2020.** STR reported U.S. occupancy of 24.5%, ADR of \$73.23 and RevPAR of \$17.93, with RevPAR down 79.9% from April 2019. It described occupancy and RevPAR as the lowest monthly levels in its records [FACT; ch11-S04, VERIFIED-SECONDARY]. The identity holds: $0.245 \times 73.23 = \$17.94$, against the reported \$17.93 (rounding of the reported occupancy).

The Bureau of Labor Statistics reported that employment in accommodation fell by 839,000 in April 2020, within a 7.7 million decline in leisure and hospitality [FACT; BLS Employment Situation, 8 May 2020, ch11-S07, VERIFIED-PRIMARY for the release; later revisions not used].

**Full-year 2020.** STR reported occupancy of 44.0% (−33.3%), ADR of \$103.25 (−21.3%) and RevPAR of \$45.48 (−47.5%). It called 2020 the worst year on record for U.S. hotels and said the industry was expected to show close to zero profit for the year [FACT; ch11-S03, VERIFIED-SECONDARY]. Computing the changes from the published 2019 and 2020 levels gives −33.4%, −21.3% and −47.6%. The small differences most likely arise because percentage changes are computed on a matched sample of reporting hotels and the levels are rounded [INFERENCE; the methodology note should be checked]. The identity $0.440 \times 103.25 = \$45.43$ versus the reported \$45.48 shows the same rounding. These are not errors, but a model that mixes levels and reported changes will not reconcile to the cent. Cite one or the other.

**Financing.** Trepp reported that the CMBS delinquency rate for lodging loans reached 24.30% in June 2020, an all-time high for the sector in its data [FACT; Trepp via trade press, ch11-S08, VERIFIED-SECONDARY].

**Recovery.** For 2021 STR reported occupancy of 57.6%, ADR of \$124.67 and RevPAR of \$71.87, which it described as 83.2% of the 2019 comparable [FACT; ch11-S05, VERIFIED-SECONDARY]. From the published levels, $71.87/86.76 = 82.8\%$, again a sample-basis difference.

### What was knowable then, and what was not

* **Knowable:** the operating leverage of hotels; the mechanics of revenue-based fees; that hotel loans carry cash-management triggers; that demand in 2001 was already falling before September; that a pandemic stops travel.
* **Not knowable:** the date of either shock, the depth (STR described April 2020 occupancy and RevPAR as the lowest in its U.S. records, so no prior month offered a reference point [INFERENCE]), or the duration and form of policy support.

### Participants, leverage and the strategies available

[INFERENCE throughout this subsection: it describes structural positions implied by the contracts and loans discussed in this chapter, not documented aggregate data.] Owners held the residual claim, behind franchise and management fees and lenders. Owners financed with floating-rate or CMBS debt faced cash-management triggers within a quarter of the shock, which converted an income problem into a liquidity problem. Operators had incentives tied to revenue (base fees) and to profit above owner priorities (incentive fees, which disappeared). Brands collected revenue-based fees that fell with revenue but did not bear fixed costs. The strategies available to an owner were the same in both episodes: cut fixed labor quickly, decide whether to defend rate or occupancy, draw reserves and credit lines, negotiate forbearance or covenant relief early, and defer discretionary capital, including PIP deadlines where the brand allowed it. Capital that was unlevered, or that held a large working-capital reserve, could also act as a buyer of distressed hotels or loans; Chapter 12 develops that side.

### Interpretations

**Operating leverage, quantified.** Take a stylized hotel with a 38% GOP margin in 2019 whose costs are 55% fixed in the short run [HYPOTHESIS]. Cut revenue 47.5%. Variable costs fall in proportion; fixed costs do not. Per \$100 of 2019 revenue: costs \$62, of which \$34.10 fixed and \$27.90 variable (27.9% of revenue). 2020 revenue \$52.50; GOP $= 52.50 \times (1 - 0.279) - 34.10 = \$3.75$, a **90% decline** in GOP from \$38.00. Fees, property tax and insurance then take the remaining GOP and more. That is consistent with STR's statement that the industry would show close to zero profit for the year [INFERENCE: a stylized calculation consistent with the reported outcome; it does not establish actual industry cost shares].

**Rate versus occupancy.** In September 2001 occupancy fell 15.9% and ADR 8.9%. In 2020 occupancy fell about a third and ADR about a fifth. In both shocks most of the RevPAR loss came through occupancy, and ADR followed. A break-even occupancy computed at pre-shock ADR (§11.4.6) would have understated the break-even in both episodes [INFERENCE].

**Competing explanations of 2020 survival.** Some hotels survived on reserves, some on lender forbearance and some on government programs. Their relative importance is not settled here *(verification pending: sector-level data on forbearance and program use)*.

### What the episode does and does not establish

It establishes that national monthly hotel RevPAR can fall by about a quarter year over year (September 2001) and by about four-fifths (April 2020), that profit falls far more than revenue, and that hotel loan performance deteriorates within months. It does **not** establish the probability of another shock of either size, that recoveries will follow the 2021 path, or that any particular hotel would have experienced the national average. A stress test that uses a RevPAR decline of about a quarter for a month or two is grounded in 2001. One that uses −50% for a year is grounded in 2020. One that uses neither has no historical anchor.

---

## 11.11 Decision exercise: the Monday BOV, rebuilt

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

## 11.12 Frequent analytical errors

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

## 11.13 Connections to other chapters

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

## 11.14 One-page reference sheet

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

## References for this chapter

Sources and verification status: `references/sources_ch11.md`. Hypothetical inputs are not registered.

* STR (CoStar Group). U.S. hotel performance press releases: September 2001 (as reported in *The Caterer*); August 2001 (as reported in trade press); April 2020; full-year 2019, 2020 and 2021. Accessed via search excerpts on 2026-10-19.
* U.S. Bureau of Labor Statistics. *The Employment Situation — April 2020.* News release, 8 May 2020. https://www.bls.gov/news.release/archives/empsit_05082020.pdf
* National Bureau of Economic Research. *US Business Cycle Expansions and Contractions* and the June 2020 Business Cycle Dating Committee announcement. https://www.nber.org/research/business-cycle-dating
* Trepp. CMBS delinquency report, June 2020 (as reported by Nareit and trade press).
* Internal Revenue Service. *Instructions for Form 8594, Asset Acquisition Statement Under Section 1060* (rev. 11/2021). https://www.irs.gov/instructions/i8594
* *Uniform System of Accounts for the Lodging Industry* (USALI). Edition and publisher details *(verification pending)*.
