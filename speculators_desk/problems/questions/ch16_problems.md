# Chapter 16 Problems — Commodities

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch16_solutions.md`. Numerical answers are verified in `tests/test_ch16_examples.py`.
All prices, elasticities and deal facts are hypothetical [HYPOTHESIS] unless a source is cited. Contract multipliers are those in Chapter 16, §16.3. Rates are continuously compounded unless stated.

---

### Problem 16.1 (Level 1) — What the curve says
For each statement, say whether it is correct, and explain in two or three sentences using the theory of storage.

(a) "Crude is in steep backwardation, so the market expects prices to fall. We should wait to buy our fuel."
(b) "Copper is in contango near full carry. Inventories are probably ample."
(c) "Full carry is an arbitrage bound, so a WTI curve can never be in contango by more than financing plus our storage cost."
(d) "A long rolling position in gold earns roughly the spot change of gold."
(e) "Corn's July contract trades above the December contract. That is a mispricing, because December is further away and should include more carry."

### Problem 16.2 (Level 2) — Multipliers without a calculator
Compute the P&L of each position and the total.
(a) Long 2 SI (silver) from \$28.40 to \$29.15.
(b) Short 3 HG (copper) from \$4.380 to \$4.215.
(c) Long 4 ZC (corn) from 437'0 to 425'4.
(d) Long 1 NG (Henry Hub) from \$2.875 to \$3.140.

### Problem 16.3 (Level 2) — Gold carry
Gold spot is \$2,000/oz (hypothetical). The one-year financing rate is 4.0% and the gold lease rate is 0.5%, both continuous. Storage and insurance are negligible. (a) What is the one-year futures price implied by carry? (b) What would it be with a zero lease rate? (c) What is the notional of 10 GC contracts at the price in (a)?

### Problem 16.4 (Level 3) — Cash-and-carry and the implied convenience yield
WTI spot \$60.00/bbl. Three-month financing 5.0% continuous. Storage costs \$0.45/bbl/month, paid at delivery.
(a) Compute full carry $F^*$ for three months and the storage cost expressed as a continuous yield.
(b) The three-month futures trade at \$63.20. Describe the arbitrage, compute its profit per barrel and on 20 contracts, and compute the implied convenience yield.
(c) If instead the futures trade at \$58.80, compute the implied convenience yield. Can you arbitrage this? Explain who could, and why they might not.

### Problem 16.5 (Level 3) — Roll decomposition in backwardation
A fully collateralized long rolls the one-month contract for three months. Bills pay 0.35% per month. Spot: $S_0 = 80$, $S_1 = 78$, $S_2 = 81$, $S_3 = 77$. Nearby futures at the start of each month: $F_0 = 79.00$, $F_1 = 77.20$, $F_2 = 80.10$.
(a) Compute each month's spot, roll, collateral and total components.
(b) Compute the compounded total return, the compounded excess return, and the spot change.
(c) Verify the log identity: cumulative log excess = $\ln(S_3/S_0) + \sum \ln(S_t/F_t)$.
(d) A colleague says: "Spot fell 3.75%, so a long commodity position lost money." Evaluate.

### Problem 16.6 (Level 3) — Gas storage
A storage operator has 5,000,000 MMBtu of deliverable capacity. The summer injection strip is \$2.60/MMBtu and the winter withdrawal strip is \$3.40. Fuel loss 1.5%. Injection and withdrawal costs \$0.03 each. Capacity rent \$0.25. Financing 6% simple for seven months.
(a) Intrinsic margin per delivered MMBtu and in total.
(b) How many NG contracts must be bought in the summer strip and sold in the winter strip?
(c) What winter price makes the intrinsic margin zero?

### Problem 16.7 (Level 4) — An Odessa hotel and an oil hedge
A 90-room limited-service hotel: occupancy 76%, ADR \$135. Other revenue 4% of rooms revenue; rooms expense \$28 per occupied room; other departmental expense ratio 70%; undistributed \$800,000 fixed plus 7% of total revenue; management 3% of total revenue; franchise 10% of rooms revenue; property tax \$150,000; insurance \$90,000; FF&E reserve 4%. Oil shock −35% from \$75 to \$48.75. Elasticities [HYPOTHESIS]: $\varepsilon_{rig} = 1.2$, $\varepsilon_D = 0.85$, energy share $s = 0.60$, $\eta = 0.6$. Supply +5%. The 12-month WTI future is \$71.
(a) Compute occupancy, ADR and RevPAR after the shock.
(b) Compute NOI before and after.
(c) Compute the NOI oil sensitivity $\beta$ and the number of CL contracts to hedge one year of it. What does the hedge earn if oil ends at \$48.75? What share of the NOI loss does it cover?
(d) Would you recommend the hedge to the owner? Give a rubric-style answer covering instrument choice, basis, lags, margin and what remains unhedged.

### Problem 16.8 (Level 4) — Replacement cost and a copper hedge
A 300,000 sf industrial project: land \$6.0 million; hard cost \$42.0 million; soft costs 20% of hard. Commodity shares of hard cost: lumber 6%, steel 9%, copper 2.5%. Over the bid period lumber falls 20%, steel rises 30%, copper rises 40% (full pass-through).
(a) Compute the hard-cost change and replacement cost before and after.
(b) With copper at \$4.50/lb at budget, how many HG contracts hedge the copper content?
(c) The general contractor offers a GMP contract with a 1.5% premium on hard cost that fixes all material prices. Should the developer hedge copper, take the GMP, or both? Explain, and say what information would change your answer.

### Problem 16.9 (Level 4) — April 2020
On 20 April 2020 the NYMEX WTI May 2020 contract fell from \$17.73 to settle at −\$37.63 per barrel [FACT; CFTC; Chapter 16, §16.8.4].
(a) Compute the one-day P&L on one long CL contract and express it as a multiple of the prior day's notional.
(b) A hypothetical fund holds 2,000 long May contracts on 14 April and must roll into the June contract before expiry. Explain, using the Working curve, why the cost of rolling rose as expiry approached. Do not invent the historical June price; work with symbols.
(c) What was knowable on 14 April (§16.8.4), and what was not? What would a disciplined desk have done with a long front-month position it could not take delivery on?
(d) Name one way this episode affected an energy-market hotel owner, and one reason the oil channel cannot be isolated in 2020 data.

### Problem 16.10 (Level 5) — The broker's Permian multifamily pitch
A broker sends a two-page teaser for a 220-unit, 2015-vintage apartment community in Midland. The asking price is a 6.25% cap rate on "in-place NOI". The teaser says:
* Occupancy 97%, effective rents up 14% year over year.
* "Oil futures are backwardated, so the market expects a gentle decline in oil prices — a soft landing."
* "Replacement cost is above \$250,000 per unit; our price is \$205,000 per unit."
* No rent roll, no T-12 by month, no unit mix, no concession history.
* A pipeline construction project 5 miles away is scheduled to finish in 8 months.

You have a one-hour call with the broker tomorrow and an investment committee in two weeks.

Write a one-page memo: (a) what each claim does and does not show; (b) the three facts that would most change value, ranked; (c) what you would ask for on the call; (d) whether you would submit an offer before receiving them, and what your committee recommendation would be if the data never arrive.
