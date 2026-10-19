# Chapter 17 Problems — Credit and Financial Distress

Levels: 1 conceptual · 2 mental arithmetic · 3 multistep calculation · 4 applied decision · 5 judgment under incomplete information.
Solutions are in `problems/solutions/ch17_solutions.md`. Numerical answers are verified in `tests/test_ch17_examples.py`.
All facts are hypothetical [HYPOTHESIS] unless cited. Rates are continuously compounded where the problem says so; otherwise state your convention.

---

### Problem 17.1 (Level 1) — Three distinctions
(a) A BBB bond trades at a 180 bp spread. A colleague divides by $(1 - R) = 0.6$ and says "the market expects a 3% annual default rate, but historically BBB defaults are far rarer, so the bond is cheap." What is wrong with the inference, and what would you need to make it correctly?
(b) Define the fulcrum security. Why do distressed investors care more about which class is the fulcrum than about which class is cheapest?
(c) Explain in two sentences why buying CDS protection on an operating subsidiary does not hedge notes issued by its holding company that carry no subsidiary guarantee.

### Problem 17.2 (Level 2) — Credit triangle, mentally
A five-year CDS trades at 300 bp. Assume recovery 40%. Give (a) the risk-neutral hazard, (b) the five-year cumulative risk-neutral PD, and (c) the one-year PD. For (b) use $e^{-0.25} \approx 0.78$.

### Problem 17.3 (Level 2) — A tranche in your head
A CMBS tranche attaches at 8% and detaches at 12%. 20% of the pool defaults.
(a) What is the tranche's loss if severity is 35%? If severity is 50%?
(b) At 50% severity, what default rate first impairs the tranche?

### Problem 17.4 (Level 3) — Hazard term structure
A rating class shows cumulative default rates of 2.0% at one year, 7.5% at three years and 13.0% at five years.
(a) Compute the average constant hazard over 0–3 years and over 0–5 years, and the one-year hazard.
(b) Compute the forward hazard for years 1–3 and years 3–5.
(c) Compute the probability of default in years 4–5 given survival to the end of year 3.
(d) If these were risk-neutral probabilities and recovery were 35%, what triangle spreads would the 3-year and 5-year average hazards imply? Why would observed spreads on bonds in this class be higher if the table is a real-world history?

### Problem 17.5 (Level 3) — Waterfall and fulcrum
All claims sit at one legal entity. Admin and priority claims \$15m; first-lien term loan \$160m; second-lien notes \$90m (both liens on all assets); senior unsecured notes \$120m, pari passu with \$30m of trade claims; subordinated notes \$50m; equity.
(a) Compute recoveries by class and identify the fulcrum at a distributable value of \$300m.
(b) Repeat at \$380m.
(c) Repeat at \$240m, and explain what happens to the second lien's deficiency claim.

### Problem 17.6 (Level 3) — CDS upfront and mark-to-market
Five-year CDS, par spread 320 bp, running coupon 100 bp, recovery 40%, riskless rate 3.0% continuous, quarterly premiums, notional \$10 million. Use the credit-triangle hazard to build the risky annuity.
(a) Compute the hazard, RPV01, upfront (points and dollars) and who pays it. What is the annual running premium in dollars?
(b) The next day the spread tightens to 250 bp. Compute the new upfront and the mark-to-market for the protection buyer.
(c) Compare with the linear estimate $(s_1 - s_0)\cdot RPV01$ and explain the difference.

### Problem 17.7 (Level 3) — Merton on a smaller building
A building is worth \$50m. Debt is modeled as a zero-coupon claim with face \$35m due in two years. Riskless rate 4.0% continuous; volatility 18%; no payout.
(a) Compute equity, debt, the debt yield and spread, and the risk-neutral PD.
(b) Repeat after the value falls to \$40m with volatility unchanged.
(c) By how much did the equity fall relative to the fall in property value? Interpret the ratio.

### Problem 17.8 (Level 4) — Holdco notes and the priming threat
A Holdco's only asset is 100% of an Opco. Opco has \$180m of secured debt and \$60m of unsecured claims. Holdco has \$150m of notes without an Opco guarantee, offered at 30. Your scenarios for Opco value at emergence in two years: \$260m (p = 0.35), \$320m (0.45), \$400m (0.20).
(a) Compute the Holdco note recovery in each scenario, the expected recovery and the IRR on the expected recovery.
(b) The Opco indenture permits \$40m of additional debt secured ahead of the existing secured claims, and the proceeds would be used to fund losses (they do not stay in the group). Recompute the recoveries and expected recovery if the priming debt is incurred.
(c) Decide whether to buy, at what size and with what conditions. Use the rubric.

### Problem 17.9 (Level 4) — Pricing the CMBS Class D bond
Class D of Example 17.7 (attach 6.5%, detach 11.0%) is offered at 72. Assume a 4.0% coupon on the original balance paid annually for four years, with any principal loss realized at the end of year 4 together with the remaining principal (a simplification). Pool loss scenarios: 4% (p = 0.40), 8% (p = 0.35), 12% (p = 0.25).
(a) Compute the tranche loss and the principal returned in each scenario, the expected principal, and the expected total cash.
(b) Compute the IRR on expected cash flows and the scenario IRRs.
(c) Holding the 4% and 8% scenarios at 40:35, at what probability of the 12% scenario does the expected undiscounted cash equal the price?
(d) If \$300m of the \$1,000m pool pays off at par before any loss, what is Class D's credit enhancement? Why is that not as good as it looks?
(e) What is wrong with the coupon assumption, and in which direction does it bias the price?

### Problem 17.10 (Level 5) — The second lien that might be the fulcrum
A hotel portfolio company is negotiating a restructuring. Admin claims \$15m; first-lien loan \$300m; second-lien loan \$200m, offered to you at 55. The sponsor's adviser presents an enterprise value of \$520m. An ad hoc group of first-lien lenders presents \$380m. You have not seen the intercreditor agreement. A press report says that eight of the hotels were moved to an unrestricted subsidiary last year, but the company has not confirmed it. Two franchise agreements are in default.
(a) Compute the second lien's recovery at \$380m, \$450m and \$520m, and the enterprise value at which recovery equals the price.
(b) List the facts you need before bidding and how each could change the answer.
(c) Make a recommendation. Abstention is permitted.
