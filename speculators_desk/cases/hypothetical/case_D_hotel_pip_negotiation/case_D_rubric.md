# Case D — Instructor Grading Rubric

Keep this file separate from the student version. Numbers are produced by `case_d_model.py` and asserted in `tests/test_case_d.py`. All inputs are [HYPOTHESIS].

## Mode C — Blind examination (100 points)

| Q | Pts | Full credit | Common deductions |
|---|---|---|---|
| 1 | 5 | RevPAR \$107.31; MPI 102.1, ARI 100.7, RGI 102.8. The quarterly trend (106 → 99) shows share eroding; the annual RGI above 100 hides it | −2 if the annual RGI is read as "outperforming" without the trend |
| 2 | 5 | Reserve (\$190,420) is in NOI; PIP (\$3.98m all-in) and PCA items (\$410,000) are deducted from price; none double-counted | −3 for treating the reserve as funding the PIP |
| 3 | 10 | Hard \$3,292,200; soft \$263,376; base \$3,555,576 (\$30,132/key); contingency \$426,669; all-in \$3,982,245 | −3 if contingency is applied to hard cost only without saying so |
| 4 | 15 | November start: 345 lost room-nights, \$119,314; March start: 615, \$150,707; choose November, saving \$31,393. Shows the weekday/weekend split and the rate concession | −5 for "20 rooms × occupancy × days" (overstates displacement in low months, ignores weekday peaks). −3 for omitting the concession |
| 5 | 10 | Stabilized NOI \$1,330,702, value \$15,208,026; independent NOI \$826,048, value \$8,472,290, net \$7,004,290; LD \$785,713 | −3 for using the branded cap rate on the independent |
| 6 | 10 | Lift needed \$11.75 (10.95%); projected \$7.17, stand-alone 5.57%; vs independence 17.26%. States that the comparison with losing the flag decides | −5 for rejecting the PIP on its stand-alone return |
| 7 | 15 | Walk-away \$9,949,131 (\$84,315/key; 8.99% YOC); opening \$9,162,582 (9.50% YOC); ask = 7.22% YOC, −153 bp | −5 if required profit is omitted ("PIP at cost"). −3 if PCA items are omitted |
| 8 | 10 | LTC binds at \$9,451,233; equity \$5,089,125 in both structures; structure 2 defers \$995,561 of equity and avoids ≈\$75,663 carry | −3 if the as-is debt yield is said to bind |
| 9 | 10 | Refi check \$2,337,143; hold PV \$10,138,426; ignore-PIP PV \$7,155,519; p* = 83.6% | −3 if the refinance ignores the PIP reserve requirement |
| 10 | 10 | Price, structure, conditions, walk-away triggers; owner-facing explanation built on the refinancing check and alternatives, not on cap-rate argument | −5 for no walk-away; −5 for a tone that ends the negotiation |

Mastery threshold: 85 points, with at least 12/15 on Q4 and 12/15 on Q7.

## Mode D — Investment committee: model answers and scoring

Score each answer 0–4: 0 missing or wrong; 2 qualitatively correct with no number; 4 quantified, honest about uncertainty, and decision-relevant.

1. **"The PIP is negotiable."** Scope may be negotiable; existence is not. The same letter applies at renewal (26 months) and on sale. A strong answer offers to bid on the issued letter and to pass through, dollar for dollar grossed up by contingency and profit, any reduction the owner obtains from the brand before closing.
2. **Exit cap 9.25%.** Stabilized value falls to \$14,385,971 and the walk-away to **\$9,127,075**, \$822,055 lower. A strong answer notes the opening bid (\$9.16m) is near this level, so the opening bid already survives a 50 bp cap-rate miss.
3. **PIP +20%.** Walk-away falls by **\$915,916** to \$9,033,214 ($0.20 \times 3{,}555{,}576 \times 1.12 \times 1.15$). A strong answer proposes contractor bids before hard money and a price-adjustment mechanism tied to the bid.
4. **RGI 102 instead of 106.** Stabilized NOI \$1,184,299; walk-away **\$8,275,951**, \$1,673,179 lower. This is the largest single sensitivity. A strong answer ties the RGI assumption to evidence (renovated comps in the set, the brand's post-PIP data) and treats 106 as the key diligence item.
5. **Timing.** A March start costs \$150,707 of NOI against \$119,314 for November: \$31,393 more. The difference is small relative to price; a strong answer would accept a spring start if it bought scope concessions, and notes that construction lead times (case goods) may decide the start date anyway.
6. **Lender structure.** Same equity (\$5.09m) either way. Structure 2 saves ≈\$75,663 of negative carry and defers \$995,561 of equity, but adds draw risk and inspection delays. A strong answer prefers structure 2 with a draw schedule agreed at closing and a funded contingency.
7. **Cushion.** Break-even occupancy after debt service at the walk-away is **66.0%** (42.1% before debt service) against 73.5%: 7.5 points. During renovation 20 rooms are out of service, and the concession lowers ADR. A strong answer proposes a debt-service reserve or interest-only period covering the renovation and an operating covenant holiday.
8. **Why should the owner accept?** Because his alternatives are worse: refinancing requires a \$2.34m check; holding and renovating is worth \$10.14m only if he can fund and execute it, and ignoring the PIP is worth \$7.16m. He needs about 84% confidence in his own execution to prefer holding. A strong answer delivers this as arithmetic the owner can check, not as pressure.
9. **Most likely failure.** PIP scope creep and overruns combined with a slower RGI recovery. Second: a softer market during the renovation tripping lender covenants. A strong answer names the monitoring metric (monthly RGI against the renovated comps) and the remedy.
10. **Why not wait?** Waiting may lower the price, but the owner may refinance with a partner's equity, sell to another buyer, or obtain a short extension; the PIP liability does not go away for either side. A strong answer proposes a firm bid with an expiry and a plan to re-engage at maturity, and does not rely on distress to justify the price: the walk-away stands on yield-on-cost alone.

Minimum passing committee performance: an average of at least 3.0, with no score of 0 on questions 3, 4 or 7.

## Mode B — Alternative defensible recommendations

* **Pass.** Defensible if the analyst believes post-PIP RGI will not exceed about 102 (walk-away \$8.28m), so that no price the owner could accept leaves a renovation return. The analyst should say so and set a re-engagement trigger (the loan maturity, or a reduced PIP letter).
* **Joint venture with the owner.** The owner contributes the hotel at an agreed value near the walk-away; the buyer funds the PIP for a preferred return. Defensible if the owner's tax position makes a sale costly; it must be priced so the buyer's PIP capital still earns its required return.
* **Bid contingent on brand scope.** A bid of about \$9.9–10.0m conditioned on the brand accepting a reduced scope (for example, deferring the pool and exterior items), with the price falling dollar for dollar (grossed up) if scope is restored.
* **Not defensible:** any price above \$9.95m without new information (a reduced PIP, higher RGI evidence, lower cap rates from renovated comparable sales); any analysis that capitalizes the T-12 at a market cap rate and ignores the PIP; any recommendation that treats the owner's \$13.5m anchor as information about value.
