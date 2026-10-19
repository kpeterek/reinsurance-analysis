# Chapter 7 Problems — Fiscal Policy, Sovereign Risk, and Global Capital

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch07_solutions.md`. Numerical answers are verified in `tests/test_ch07_examples.py`.
All market levels, balance sheets, and property facts are hypothetical [HYPOTHESIS] unless cited. Rates are simple annual money-market rates unless stated. FX pairs are BASE/QUOTE.

---

### Problem 7.1 (Level 1) — Reading $r - g$
(a) Country A has debt of 130% of GDP, $r = 2.5\%$, $g = 4.0\%$. Country B has debt of 60% of GDP, $r = 7.0\%$, $g = 3.0\%$. Without computing a path, which country needs the larger primary surplus to stabilize its debt ratio? Show the sign and approximate size of $pb^*$ for each.
(b) A colleague says: "Since $r < g$ for Country A, its debt is free; it can borrow indefinitely." Give three reasons this is wrong or incomplete.
(c) Why does a government with a weighted average maturity of 2 years face a different risk from one with 7 years, at the same debt ratio and the same market yields?

### Problem 7.2 (Level 1) — The trilemma and the transmission to property
For each regime, state which corner of the impossible trinity is given up, and through which variable a sudden rise in global interest rates reaches local commercial property values.
(a) A small open economy with a hard peg to the U.S. dollar and no capital controls.
(b) A euro-area member.
(c) A large economy with a floating currency and an independent central bank.
(d) A country that pegs to a basket and restricts capital outflows.

### Problem 7.3 (Level 2) — Mental arithmetic: the stabilizing balance
Debt is 90% of GDP, the effective interest rate is 4.5%, and nominal growth is 3.5%.
(a) Estimate, then compute, the primary balance that stabilizes the debt ratio.
(b) If the government instead runs a primary deficit of 2.0% of GDP, what is next year's debt ratio?

### Problem 7.4 (Level 2) — Mental arithmetic: CDS to default probability
A sovereign's 5-year CDS trades at 300 bp. Assume 40% recovery.
(a) What is the hazard rate?
(b) Estimate the five-year cumulative risk-neutral default probability without a calculator, then compute it.
(c) Repeat (a) and the five-year probability with 25% recovery on a 300 bp spread. Which assumption gives the higher default probability, and why?

### Problem 7.5 (Level 3) — A Swiss investor and U.S. Treasuries
A Swiss pension fund can buy the 10-year Treasury at 4.30% or a 10-year Swiss government bond at 0.70%. One-year rates: USD 4.00%, CHF 0.25%. Spot USD/CHF = 0.8800. Assume the Treasury's yield is unchanged after one year, so its one-year local return is 4.30%.
(a) Compute the one-year CIP forward USD/CHF.
(b) Compute the one-year hedged return in CHF and the pick-up versus the Swiss bond.
(c) At what year-end spot USD/CHF does an unhedged Treasury match the Swiss bond? By what percentage can the dollar fall?
(d) Holding the Treasury yield at 4.30% and the CHF rate at 0.25%, what one-year USD rate makes the hedged Treasury exactly match the Swiss bond?
(e) Compare the one-year hedge cost with the annualized cost of rolling a three-month hedge at the same annual rates (compute the three-month forward and annualize the forward discount by compounding). Comment briefly.

### Problem 7.6 (Level 3) — Debt dynamics with a lagging effective rate
Debt is 120% of GDP. The effective interest rate is 2.5%. Market yields jump to 5.0% and stay there. Nominal growth is 3.5%, and the primary deficit is 1.0% of GDP every year. The debt has a weighted average maturity of five years, so assume 20% of the gap between the market rate and the effective rate closes each year: $r_t = r_{t-1} + 0.2(0.05 - r_{t-1})$, starting from year 1.
(a) Compute the effective rate in years 1–5.
(b) Compute the debt ratio at the end of each of years 1–5.
(c) Compare with (i) the path if the whole stock repriced to 5.0% immediately and (ii) the path if rates had stayed at 2.5%.
(d) In year 1, what primary balance would have stabilized debt under the gradual path? Under immediate repricing? What does the difference imply about how markets and governments perceive the same rate shock?

### Problem 7.7 (Level 3) — Balance-of-payments arithmetic
(a) Country P pegs its currency. Its GDP is \$2.0 trillion. Its current-account surplus is 3% of GDP, and private residents make net financial investments abroad of 1% of GDP. Ignoring the capital account and errors, how much do the central bank's foreign reserves change, in dollars?
(b) If the central bank does not sterilize, what happens to domestic money and credit conditions? What does this imply for local property prices under a peg?
(c) Country Q has private saving of 23% of GDP, private investment of 22%, and a government deficit of 5% of GDP. What is its current-account balance? A minister proposes to close the current-account deficit through import tariffs while keeping the budget deficit unchanged. What must happen to $S_p - I$ for the plan to succeed?

### Problem 7.8 (Level 4) — A regional bank, its sovereign, and your refinancing
A regional bank has total assets of €60 billion and equity of €3.6 billion (6.0% leverage ratio, which it targets). It holds €9 billion of domestic sovereign bonds (modified duration 4.0) at fair value and €10 billion of CRE loans. The sovereign spread widens by 300 bp. The bank keeps its sovereign bonds. Its funding cost rises by 40% of the sovereign spread change, which it passes through to new CRE loans.
(a) Compute the capital loss, new equity, and new leverage ratio.
(b) Compute the required balance-sheet shrinkage if no equity is raised, and the pro-rata cut in CRE loans.
(c) How much new equity would restore 6.0% without shrinking?
(d) You own a property with NOI of €1,000,000 that must be refinanced with this bank. The bank sizes loans at a 1.25× DSCR on a 25-year amortization (monthly). Before the shock its CRE loan rate was 5.0%. Compute the maximum loan before and after the funding-cost pass-through, and the percentage change.
(e) Write a short recommendation: refinance with this bank now, seek another lender, or arrange a different solution? Name the information you would want first.

### Problem 7.9 (Level 4) — A Japanese investor buys a U.S. hotel
A Japanese insurer buys a U.S. select-service hotel for \$40 million, all cash. Year-1 NOI after a 4% FF&E reserve is \$3.2 million (an 8.0% cap rate on NOI after reserve), received at year-end. USD/JPY spot is 150.00; one-year rates are USD 4.00% and JPY 0.50%. Assume the hotel's dollar value is unchanged after one year.
(a) Compute the hedged one-year return in yen if the insurer sells forward the full expected year-end dollar amount.
(b) If USD/JPY ends the year at 165.00, compute the cash settlement on the hedge in yen and as a share of the initial yen equity. Compute the unhedged return in that scenario.
(c) Compute the total return with a 50% hedge ratio in the scenario of (b).
(d) If USD/JPY instead ends at 135.00, compute the unhedged return and the hedge gain as a share of equity.
(e) Recommend a hedge policy, including a liquidity reserve. Explain how a hotel's demand mix (domestic versus international guests) changes the case for hedging.

### Problem 7.10 (Level 5) — The dollar-debt resort hotel under a fragile peg
A broker offers you a note secured by a 300-key beach resort in a small country whose currency is pegged to the U.S. dollar. Facts you have:
* The note is \$45 million, USD-denominated, matures in 18 months, and is offered at 72% of par.
* The resort's revenue is about 60% from foreign tourists paying in dollars and 40% from domestic guests and events paying in local currency. Most operating costs are in local currency.
* Trailing NOI after reserve is \$4.1 million. The broker's appraisal (dated 14 months ago) values the resort at \$58 million.
* The central bank's published foreign reserves fell by about a third over the past year. The government says the peg is "non-negotiable." A rating agency placed the sovereign on watch negative last week.
* Local banks are reported to be restricting dollar withdrawals informally. You cannot verify this.
* The borrower is current on interest. You have not seen the loan documents, the security package, or any information on local enforcement timelines.
* You have five business days to submit a binding bid.

Write a one-page decision memo. Address: (a) how a devaluation would affect the resort's dollar NOI and the borrower's ability to pay; (b) what the 72% price implies about the recovery you would need; (c) the three most important unknowns, ranked; (d) whether you bid, and on what conditions; (e) what information would change your answer. Abstention is a legitimate answer.
