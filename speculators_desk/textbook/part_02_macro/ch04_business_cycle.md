# Chapter 4 — The Business Cycle

> **Status:** Complete (v1.0). Numerical examples, problem answers and the arithmetic of the historical episode are reproduced in `tests/test_ch04_examples.py`. Problems are in `problems/questions/ch04_problems.md` and solutions in `problems/solutions/ch04_solutions.md`. Sources are in `references/sources_ch04.md`. Items marked *(verification pending)* have not yet been checked against a primary source; in particular, ALFRED vintage downloads could not be retrieved in this authoring pass, so the real-time figures in §4.9 rest on the original BEA and BLS releases rather than on ALFRED.

## Learning objectives

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

## 4.1 Opening investment problem: the hotel bid in a late-cycle fog

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

## 4.2 Economic intuition: why the cycle exists and why CRE feels it unevenly

The business cycle is the recurring, irregular alternation of expansion and contraction in aggregate economic activity. *Recurring* means that recessions keep happening. *Irregular* means that no fixed period or amplitude describes them. Expansions in the post-war United States have ranged from about a year to more than ten years. A speculator gains nothing by forecasting "the cycle" as if it were a sine wave. What pays is knowing **which mechanisms amplify a slowdown into a recession, how quickly each shows up in the data, and how quickly each reaches the cash flows you own**.

### Three amplifiers

1. **The investment accelerator.** Firms invest to *expand* capacity. When expected demand growth slows from 3% to 1%, the desired capital stock still grows, but the *flow* of new investment needed to reach it can fall by much more than 2%. Inventories behave the same way. A retailer that expects flat sales stops restocking; it does not cut orders by the 1% decline in sales. Investment is a derivative of expected output, so it swings more than output does. This is why housing, equipment, structures and inventories account for most of the variation in GDP during recessions, while consumption, the largest component, moves much less. Example 4.1 shows the arithmetic.

2. **The labor-income loop.** Lower investment cuts hiring. Lower hiring cuts household income growth. Lower income growth cuts consumption at the margin, which cuts expected demand and lowers investment again. Unemployment insurance and other automatic stabilizers dampen the loop, and the Sahm rule (§4.5.5) watches it directly. Once the three-month average unemployment rate has risen half a point, the loop has historically been running.

3. **The credit loop.** Lenders lend against collateral values and borrower cash flow. When the outlook darkens, banks tighten standards: lower LTVs, higher DSCR minimums, wider spreads (§4.5.6). Tighter credit lowers asset values and investment, which worsens the outlook, which justifies tighter credit. In CRE the loop runs through refinancing. A loan sized at 65% LTV in a loose market cannot be refinanced at 60% LTV of a lower value without new equity. Chapter 3 treats this reflexivity formally. Here we measure it.

### Why CRE feels the cycle unevenly

A property's NOI is a claim on a slice of the economy, and the slice is defined by **lease duration** and **operating leverage**:

* **Hotels reprice every night.** Room rates and occupancy respond to demand within weeks, and fixed costs (labor minimums, property taxes, insurance, franchise systems) do not shrink with revenue. Hotels have the shortest leases and the highest operating leverage of any major property type. They are the first CRE asset class to show a downturn and usually the hardest hit in NOI terms (Example 4.8).
* **Apartments reprice annually.** About one-twelfth of leases roll each month, so market-rent changes pass through to the rent roll within a year. Operating leverage is moderate.
* **Office and industrial reprice slowly.** With five- to ten-year leases, only the share of the rent roll that expires in a given year marks to market. The NOI hit is delayed, but it is **embedded**. It arrives as leases roll, often after the recession has officially ended, and with downtime, free rent and tenant-improvement costs that NOI understates.
* **Retail** sits in between. It depends on the tenant mix and on percentage-rent clauses.

So "the cycle" reaches a diversified CRE portfolio as a sequence: hotel RevPAR first, then apartment rent growth, then office and industrial occupancy and rents, and finally appraisal-based values and cap rates. Lenders, meanwhile, have tightened before any of those NOI changes appear. A speculator who understands the sequence can price the lag.

---

## 4.3 Technical definitions

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

## 4.4 GDP, its components, and productivity

### 4.4.1 The expenditure identity and why investment is the volatile component

$$Y = C + I + G + NX.$$

This is an accounting identity, not a theory. It says where output went. It does not say what caused what. Two consequences are often misread.

* **Imports do not "subtract from GDP".** Imports appear in $C$, $I$ or $G$ when the goods are bought, and are subtracted in $NX$ so that only domestic production is counted. A fall in imports raises measured $NX$. In a recession that rise often partly offsets weaker domestic demand, because demand for imports falls along with everything else. It is a symptom of weakness, not a source of strength.
* **Inventory change is part of $I$.** Production that is not sold is counted as investment in inventories. A quarter of strong GDP growth driven by inventory accumulation can mean that firms produced goods nobody bought. That quarter borrows from the next one.

Personal consumption is about two-thirds of U.S. GDP. FRED's series of BEA percentage shares shows personal consumption expenditures at 68.0% of GDP in the fourth quarter of 2025 [FACT; FRED series DPCERE1Q156NBEA, from BEA NIPA data, VERIFIED-SECONDARY via search excerpt]. Gross private domestic investment is a much smaller share, conventionally in the high teens *(verification pending for a current value)*. The difference in **volatility** matters more than the difference in size.

Write the growth of GDP as a share-weighted sum of component growth rates:

$$\frac{\Delta Y}{Y_{t-1}} = \sum_i \frac{X_{i,t-1}}{Y_{t-1}} \cdot \frac{\Delta X_i}{X_{i,t-1}} = \sum_i s_i\, g_i .$$

Each term $s_i g_i$ is component $i$'s **contribution** in percentage points. If consumption ($s \approx 0.68$) slows from +2% to +0.5%, its contribution falls by about one point. If investment ($s \approx 0.17$) swings from +5% to −12%, its contribution falls by nearly three points. In this sense recessions are investment events.

### 4.4.2 Annualized versus year-over-year growth

The BEA reports quarterly real GDP growth "at an annual rate". The rate is **compounded**, not multiplied by four:

$$a = (1+q)^4 - 1, \qquad q = (1+a)^{1/4} - 1.$$

Derivation: if output grew at the quarterly rate $q$ for four consecutive quarters, the level after a year would be $(1+q)^4$ times the starting level.

Year-over-year growth compares the current quarter with the same quarter a year earlier:

$$YoY_t = \frac{Y_t}{Y_{t-4}} - 1 = \prod_{j=0}^{3}(1+q_{t-j}) - 1.$$

YoY growth is the compound of the last four quarterly rates. It is therefore a **trailing average**, smoothed and lagged by roughly two quarters. Near a turning point the two measures can tell opposite stories: YoY can stay positive for two or three quarters after the economy has started to contract (Example 4.2). Annualized rates have the opposite fault. They multiply a single quarter's noise, including revisions, by about four. A desk should look at both, and at the level.

The simple approximation $a \approx 4q$ understates positive growth and overstates the magnitude of negative growth, but only slightly at normal growth rates. The gap is $6q^2 + 4q^3 + q^4$, about 1.5 bp at $q = 0.5\%$. It matters in high-inflation nominal series and in collapses like 2020.

### 4.4.3 Productivity and unit labor costs

Labor productivity is output per hour:

$$\text{Productivity growth} = \frac{1 + g_{output}}{1 + g_{hours}} - 1 \approx g_{output} - g_{hours}.$$

Unit labor cost is compensation per unit of output:

$$\text{ULC growth} = \frac{1 + g_{comp/hour}}{1 + g_{productivity}} - 1 \approx g_{comp/hour} - g_{productivity}.$$

Productivity is the bridge between wages and inflation. Wage growth of 4.5% is consistent with 2% price inflation and stable margins only if productivity grows about 2.5%. When productivity is weak, high wage growth either raises prices or squeezes margins. For a hotel, where labor is typically the largest single expense *(typical share of revenue is an assumption; see Chapter 11)*, the comparison between wage growth and **rooms productivity**, measured as occupied rooms per labor hour, decides whether ADR growth reaches NOI.

Productivity is also cyclical in the measured data. Early in a downturn output falls before firms cut hours, so measured productivity falls. Later, layoffs cut hours faster than output, and productivity jumps. A productivity surge in a recession is often a symptom of labor shedding, not of technology.

### Example 4.1 — Contributions: a recession driven by investment

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

### Example 4.2 — Two negative quarters inside a positive year

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

### Example 4.3 — Productivity, unit labor costs and the hotel labor ratio

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

## 4.5 Employment, credit, indicators and recession detection

### 4.5.1 Payrolls versus the household survey

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

### 4.5.2 Wages

Average hourly earnings in the payroll survey are distorted by composition. When low-wage workers lose jobs first, as they did in 2020, average earnings *rise*, even though no individual worker got a raise. Use composition-adjusted measures such as the Employment Cost Index *(BLS quarterly series; cited qualitatively)* when the question is wage *pressure*. For CRE, wage growth enters twice: as a cost (hotel and multifamily payroll) and as a driver of revenue (apartment rents follow renter incomes with a lag [HYPOTHESIS supported by the affordability logic of rent-to-income underwriting]).

### 4.5.3 Credit cycles and the Senior Loan Officer Opinion Survey

The SLOOS asks senior loan officers at a panel of domestic banks and U.S. branches of foreign banks whether their **standards** (the criteria for approving a loan) and **terms** (the price and structure of approved loans) have tightened, stayed basically unchanged, or eased over the past three months, and whether loan **demand** has strengthened or weakened. Answers come as "considerably" or "somewhat". The Federal Reserve publishes the **net percentage** tightening:

$$\text{Net \% tightening} = \frac{\#\text{tightened (considerably + somewhat)} - \#\text{eased (considerably + somewhat)}}{\#\text{respondents}}.$$

The survey reports CRE standards separately for **construction and land development**, **nonfarm nonresidential** (office, retail, industrial, hotel), and **multifamily** loans [FACT; Federal Reserve SLOOS releases, VERIFIED-PRIMARY via search excerpts; the date the three-way split began is *(verification pending)*].

Three cautions about reading the survey:

1. A net percentage measures **breadth**, not **degree**. Net 34% tightening means that, on balance, a third of banks tightened. It does not say whether the LTV cap moved 5 points or 15. Severity shows up in the special questions on specific terms and in loan pricing.
2. It is a **change** variable. Standards that tightened for six quarters and then stop tightening show "net 0%" while remaining tight. Cumulate the series, or read the questions on the *level* of standards relative to history, before concluding that credit has eased.
3. It is a **bank** survey. CMBS, life companies, debt funds and agency lenders do not respond. When banks retreat, other lenders may fill the gap at a higher price, or they may retreat together, as in 2008–09.

Example 4.4 turns a SLOOS reading into loan proceeds.

### Example 4.4 — SLOOS tightening and the office refinancing

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

### 4.5.4 Leading, coincident and lagging indicators

| Timing | Examples | CRE analogs |
|---|---|---|
| Leading | Term spread; initial jobless claims; building permits and housing starts; manufacturers' new orders; credit spreads; SLOOS standards; equity prices; consumer expectations | Hotel group-booking pace; leasing tours and proposals; construction-loan originations; REIT implied cap rates (Chapter 12) |
| Coincident | Payroll employment; industrial production; real personal income less transfers; real manufacturing and trade sales | Hotel RevPAR; apartment new-lease trade-outs |
| Lagging | Unemployment duration; services inflation; business loans outstanding; delinquency and charge-off rates | Office vacancy; appraisal-based values and cap rates; CMBS special servicing rates; CRE loan delinquencies |

The NBER weighs a set of monthly coincident measures, including payroll and household employment, real personal income less transfers, real consumption, real manufacturing and trade sales, and industrial production, rather than quarterly GDP alone *(list as described on the NBER business-cycle dating pages; current list verification pending)*. Leading indicators are leading *on average*. Their lead times vary from a few months to more than two years, and each has a history of false signals. Composite indices, such as the Conference Board's Leading Economic Index, reduce noise but inherit the components' false signals.

For CRE, notice that the classic CRE "data", meaning appraisal values, cap-rate surveys and delinquency rates, sit almost entirely in the **lagging** column. A committee that waits for cap rates to move before re-underwriting is reacting to the last war.

### 4.5.5 Recession detection: NBER dating and the Sahm rule

**NBER dating is retrospective.** The Business Cycle Dating Committee waits until the data are clear, and the data are revised. The December 2007 peak was announced on 1 December 2008. The June 2009 trough was announced on 20 September 2010. The March 2001 peak was announced on 26 November 2001, eight months later, when the recession was already over: its trough came in November 2001, though that trough was not announced until 17 July 2003 [FACT; NBER Business Cycle Dating Committee announcements, VERIFIED-PRIMARY via search excerpts]. **No asset price waits for the NBER.** A recession-conditional strategy has to act on real-time indicators that are noisier than the official dates.

**The Sahm rule.** Claudia Sahm proposed the rule in 2019 as an automatic trigger for stimulus payments to households (Sahm, 2019, Hamilton Project / *Recession Ready*). FRED's description of the Sahm Rule Recession Indicator [FACT; FRED series notes, VERIFIED-SECONDARY via search excerpt]:

$$S_t = \overline{u}_t^{(3)} - \min_{t-12 \le s \le t-1} \overline{u}_s^{(3)}, \qquad \overline{u}_t^{(3)} = \tfrac{1}{3}(u_t + u_{t-1} + u_{t-2}),$$

with a signal when $S_t \ge 0.50$ percentage point. The rule measures a **change**, not a level. A 4.0% unemployment rate is consistent with expansion or recession; a half-point rise in the smoothed rate within a year has historically indicated that the labor-income loop of §4.2 has started.

Why does a half-point rise work? Unemployment rarely rises by half a point without continuing to rise. Once layoffs exceed hiring broadly enough to lift the smoothed rate, the spending loss feeds back into further layoffs. The rule is *not* a forecast. It recognizes a recession, typically some months after it has begun.

Three properties matter in practice:

1. **Rounding.** The unemployment rate is published to one decimal. The three-month average therefore moves in steps of 0.0333, and the indicator can land exactly on 0.50. Whether "≥" or ">" is used changes the trigger month (Example 4.5).
2. **Real-time versus revised data.** The real-time version (FRED's SAHMREALTIME) uses the unemployment rates available at each date. Annual seasonal-factor revisions can move recent months by a tenth, which moves the trigger date. Secondary sources disagree by one to several months about when the rule triggered in 2001 and 2008, depending on vintage *(trigger dates verification pending against ALFRED)*.
3. **Labor-supply shocks.** The rule was calibrated on recessions in which unemployment rose because hiring collapsed. If unemployment rises because the labor force grows quickly (for example through immigration or rising participation), the rule can trigger without the demand-side loop. Secondary sources report that the indicator crossed 0.50 on the July 2024 data without an NBER recession following, and Sahm herself cautioned that labor-supply shifts could distort the signal *(the July 2024 value of about 0.53 is reported by secondary sources; verification pending against FRED)*.

### Example 4.5 — Computing the Sahm rule, and how one revision moves the trigger

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

### 4.5.6 Yield-curve inversion: base rates and false signals

When short rates exceed long rates, the market expects policy rates to fall. That usually happens because it expects the central bank to respond to weakness. An inverted curve also squeezes bank net interest margins on new lending, which can tighten credit. The evidence:

* An inverted 10-year minus 3-month spread has preceded each U.S. recession since 1960, with one clear false positive, in 1966 [FACT; J.P. Morgan Asset Management, "Was the yield curve inversion wrong in predicting a US recession?", VERIFIED-SECONDARY]. The St. Louis Fed notes that spread-based probability models also gave false positives in the late 1960s and late 1990s [FACT; Federal Reserve Bank of St. Louis, *On the Economy*, September 2023, VERIFIED-SECONDARY].
* The 10y–3m spread inverted in October 2022 and stayed inverted until December 2024, the longest inversion in decades, and a recession "has yet to materialize" as of that commentary [FACT; same J.P. Morgan source]. Searches in October 2026 found no NBER announcement of a business-cycle peak after February 2020 [INFERENCE from the NBER chronology; *verification pending* against the NBER announcements page].
* Lead times between inversion and recession vary from several months to about two years *(range cited qualitatively; verification pending)*. J.P. Morgan notes that in the last four cycles the curve un-inverted on average about six months before the recession began.

Two consequences follow. First, a signal with a long and variable lead is a poor **timing** tool even when it is a good **regime** tool. Second, the sample is tiny, about eight or nine recessions, so the "hit rate" itself is uncertain. Treat inversion as a likelihood ratio, not as a verdict.

### Example 4.6 — Turning an inversion into a recession probability

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

## 4.6 Growth and inflation regimes

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

## 4.7 How economic surprises propagate across asset classes

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

### Example 4.7 — A payroll miss, net of revisions

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

## 4.8 CRE application: transmission to NOI by property type

### 4.8.1 The two parameters: repricing speed and operating leverage

For a property with revenue $R$, variable costs at a ratio $v$ of revenue (including fees and the reserve), and fixed costs $F$:

$$NOI = R(1-v) - F, \qquad DOL = \frac{\%\Delta NOI}{\%\Delta R} = \frac{R(1-v)}{NOI}.$$

For a leased property, only the share of revenue that rolls in a given year reprices. With rolling share $\rho$, renewal probability $\pi$, market rent change $m$ and downtime $d$ months on non-renewals, first-year revenue is

$$R_1 = R(1-\rho) + R\rho\,\big[\pi(1+m) + (1-\pi)(1+m)\tfrac{12-d}{12}\big] + R\,\Delta occ,$$

assuming, conservatively, that rolling leases expire at the start of the year. For apartments, about one-twelfth of leases roll each month, so the *time-weighted* share of the year's revenue that reprices is about one-half. We use $\rho = 0.5$.

### Example 4.8 — One recession, four property types

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

### 4.8.2 Sequence through a cycle

[HYPOTHESIS, consistent with the operating mechanics above and with the 2009 hotel data in §4.9]:

1. **Months 0–6 after the peak:** hotel group cancellations and transient demand weaken; RevPAR turns negative; lenders begin tightening (SLOOS).
2. **Months 3–12:** apartment concessions rise and new-lease rents fall; hotel NOI declines accelerate as cost cuts lag revenue.
3. **Months 6–36:** office and industrial vacancy rises as leases expire; sublease space appears; effective rents fall through free rent and TI before face rents move.
4. **Months 12–48:** appraisals and cap rates adjust; delinquencies and special servicing rise; refinancing gaps crystallize at maturity.

Hotels also lead the recovery: the same nightly repricing that brings the fall forward brings the rebound forward too.

---

## 4.9 Historical episode: the 2007–09 recession in real time (with 2001 for contrast)

This section separates **what was published at the time** from **what we know now**. Facts are from the original BEA, BLS, NBER, Federal Reserve and STR releases cited in `references/sources_ch04.md`. ALFRED vintage downloads could not be retrieved in this pass. The real-time figures below are the published release values, which are the vintages themselves, but a cross-check against ALFRED is *(verification pending)*.

### 4.9.1 Date and environment

By late 2007 housing construction was falling and subprime mortgage losses had disrupted funding markets. CRE prices were near cyclical highs, and CMBS issuance had financed a large share of acquisitions at high leverage *(magnitudes verification pending; qualitative characterization)*.

### 4.9.2 What the early data showed

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

### 4.9.3 The arithmetic of the revisions

The Q4 2008 advance estimate of −3.8% annualized corresponds to a quarterly decline of $(0.962)^{1/4} - 1 = -0.96\%$. The 2011 vintage of −8.9% corresponds to $(0.911)^{1/4} - 1 = -2.30\%$. The first published number captured well under half of the contraction later measured. The revision, −5.1 percentage points annualized, was larger than the advance estimate itself.

The payroll benchmark of −902,000 equals $902/(131{,}175 + 902) = 0.68\%$ of the pre-benchmark level, which BLS rounded to −0.7%. The preliminary benchmark announced in October 2009 (−824,000) captured 91% of the final revision. Early benchmark news was informative.

The STR figures are internally consistent: $(1-0.087)(1-0.088) - 1 = -16.7\%$, and $0.551 \times \$97.51 = \$53.73$, versus the reported \$53.71; the gap is rounding and day-weighting. They imply 2008 levels of about 60.4% occupancy, \$106.92 ADR and \$64.48 RevPAR [INFERENCE: back-calculated].

### 4.9.4 The 2001 contrast: revisions that moved in both directions

In 2001 the BEA's advance estimate for Q3 2001 (31 October 2001) showed real GDP **−0.4%** annualized. The preliminary estimate (30 November) revised it to −1.1%, and the final estimate (21 December) to **−1.3%** [FACT; BEA releases, VERIFIED-PRIMARY via search excerpt]. Under the estimates available in late 2001, Q3 was the only negative quarter. The July 2002 annual revision showed declines in each of the first three quarters of 2001. The 2004 comprehensive revision changed the pattern again: a decline in Q1, an increase in Q2, and a decline in Q3 [FACT; secondary accounts of the BEA revisions, VERIFIED-SECONDARY]. The NBER dated the peak at March 2001 (announced 26 November 2001) and the trough at November 2001 (announced 17 July 2003). Under no vintage did the 2001 recession satisfy the "two consecutive negative quarters" rule of thumb in real time. The NBER does not use that rule.

### 4.9.5 What was knowable then, and competing interpretations

**Knowable by mid-2008:** payrolls had been declining since January; the curve had inverted in 2006–07 *(timing verification pending)*; banks were tightening CRE standards broadly; hotel RevPAR growth was slowing *(2008 monthly STR data verification pending)*. **Not knowable:** that Q4 2008 would turn out to be the deepest quarterly decline of the post-war period to that date, or that a major investment bank would fail in September 2008.

**Interpretations available at the time** [INFERENCE]: (a) a housing-led slowdown similar to 1990–91 or 2001, mild because consumption would hold; (b) a credit-led recession in which bank capital losses would amplify the downturn through lending standards. The SLOOS data favored (b) well before the GDP data did, because standards were tightening at a breadth seen only in severe credit episodes *(historical comparison of breadth verification pending)*.

### 4.9.6 The CRE transmission angle

* **Hotels moved first and hardest.** U.S. RevPAR fell 16.7% in 2009, with occupancy and ADR both falling by more than 8% [FACT; STR]. With operating leverage near 2× (Example 4.8), NOI declines of 30–40% for typical hotels were arithmetically implied [INFERENCE; property-level NOI data not cited].
* **Credit tightened before NOI fell.** Most domestic banks reported tighter CRE standards in October 2008 and January 2009 [FACT; SLOOS]. In the January 2009 survey about 15% of domestic banks, on net, said the CMBS market's shutdown had *increased* their own CRE lending, but not enough to replace the lost capacity [FACT for the 15%; INFERENCE for the replacement claim].
* **Refinancing gaps crystallized at maturity.** Loans written at 2005–07 values and LTVs could not be refinanced at lower values and tighter LTVs without new equity (Example 4.4 and Problem 4.9 show the arithmetic). The losses showed up years after the recession had ended, as loans matured.

### 4.9.7 What the episode does and does not establish

It **establishes** that (1) advance GDP estimates near turning points can understate the contraction by more than half; (2) official recession dating comes far too late for investment timing; (3) bank-survey credit data and payroll trends carried information earlier than GDP; and (4) hotels transmitted the shock to CRE NOI first and most severely.

It does **not establish** that revisions are always toward weakness. The 2001 revisions moved in both directions across vintages. Nor does it establish that a given SLOOS reading forecasts a given NOI decline: one severe episode is not a calibration sample. Finally, 2007–09 was a credit-led recession. A demand shock such as 2020, or an inflation-driven slowdown, transmits through different channels and at different speeds.

---

## 4.10 Decision exercise: back to the hotel and the refinancing

Return to §4.1. You have ten days. Example 4.4 has already sized the office refinancing gap.

### The decision

Prepare a one-page committee memo using `desk/investment_memos/investment_committee_memo.md` and `desk/scenario_templates/economic_release_analysis.md`. It must include:

1. **Recession probability.** Combine the curve (Example 4.6) and the Sahm reading of 0.37, which is not yet a signal but is in the elevated zone. State your prior, the likelihood ratios you assume, and whether you treat the signals as independent.
2. **Hotel NOI under recession.** Apply the operating-leverage arithmetic of Example 4.8 to the trailing \$2.43m NOI with stated assumptions. Compute DSCR at the cap strike and the debt yield at trough NOI.
3. **The sponsor's 4% RevPAR growth.** Compare it with trailing −1.5% RevPAR and the macro dashboard. Explain what would have to be true for it to be realistic.
4. **The office refinancing.** Reserve the equity gap from Example 4.4 before sizing the hotel commitment.
5. **The decision.** Bid at a stated maximum price, bid conditionally (for example, with lower leverage or a longer rate cap), or abstain. **Abstention is a legitimate and possibly the best answer** if the deal works only when recession has a weight well below the posterior you computed.
6. **Invalidation and update criteria.** Name the data releases over the next 90 days that would change your view in each direction.

**Rubric** (detailed in `problems/solutions/ch04_solutions.md` §Decision exercise). Full credit requires: a recession probability derived from the base rate rather than asserted; a trough-NOI calculation with operating leverage; recognition that the payroll figure is weak net of revisions; reserving liquidity for the office gap; and a decision rule that would have been written the same way before seeing the sponsor's deck. No single bid is correct.

---

## 4.11 When the relationships fail

1. **The yield curve can stay inverted without a recession.** The 2022–24 inversion was the longest in decades and had not been followed by an NBER recession as of the J.P. Morgan commentary. Explanations offered include term-premium compression and the economy's lower sensitivity to short rates because borrowers had locked in fixed-rate debt [competing interpretations; SPECULATION as to which dominates].
2. **The Sahm rule can trigger on labor-supply growth.** A rising unemployment rate driven by labor-force entrants is not the same as one driven by layoffs. Check initial claims and the layoff rate before concluding that the loop is running.
3. **GDP and GDI can disagree.** Near turning points, the income side has sometimes signaled weakness earlier than the expenditure side. The statistical discrepancy is information, not noise to be ignored *(specific episodes verification pending)*.
4. **Composition effects distort wages and productivity.** Average hourly earnings jump when low-wage workers lose jobs. Productivity jumps when hours are cut. Neither is a sign of strength.
5. **Surprise sensitivities change sign with the policy regime.** "Good news is bad news" is a regime, not a constant. A sensitivity estimated in a growth-scare period will mislead in an inflation-fighting period.
6. **Non-economic shocks bypass the leading indicators.** The 2020 recession began with a public-health shutdown that no yield curve or loan survey anticipated. The NBER dated it February to April 2020. Hotels fell further and faster than any leading indicator implied.
7. **CRE transmission depends on lease structure, not property-type labels.** A hotel with a long-term master lease to a creditworthy operator behaves like a net-lease asset. An office with 40% of leases rolling next year behaves like an apartment building with downtime. Use the parameters, not the label.
8. **Revisions are not symmetric across episodes.** 2007–09 revisions made the recession much worse; 2001's moved in both directions. Do not assume a direction. Assume a band.

---

## 4.12 Frequent analytical errors

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

## 4.13 Connections to other chapters

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

## 4.14 One-page reference sheet

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

## References for this chapter

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
