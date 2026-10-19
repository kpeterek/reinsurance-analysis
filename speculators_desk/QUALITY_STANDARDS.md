# Quality Standards

These standards apply to every chapter, case, drill, model, and template. A unit of work is **complete** only when every applicable check below passes. Incomplete work is labeled as such in its header and in `PROGRESS.md`.

## 1. Governing rules
1. Every major concept leads to a calculation, a realistic example, a historical case, or an investment decision.
2. Every numerical example is reproducible: a test in `tests/` recomputes it with the `sdesk` library or an explicit formula.
3. Every important claim is distinguishable from an assumption or opinion, using the labels [FACT], [INFERENCE], [HYPOTHESIS], [SPECULATION] (see the notation guide §6).
4. No invented quotations, historical prices, transaction terms, or sources. An unverified item is marked *(verification pending)* and listed in `SOURCE_REGISTER.md`.

## 2. Chapter completion checklist
- [ ] Status line at the top of the file
- [ ] Learning objectives
- [ ] Realistic opening investment problem
- [ ] Intuition before equations
- [ ] Technical definitions table
- [ ] Equations with derivations where useful
- [ ] At least three fully worked numerical examples, each with "Decision consequence"
- [ ] A CRE application (including in cross-asset chapters)
- [ ] "When the relationship fails" section
- [ ] A historical episode with sourced facts and evidence labels
- [ ] A decision exercise with a rubric
- [ ] Ten end-of-chapter problems, Levels 1–5, in `problems/questions/chNN_problems.md`
- [ ] Complete solutions with intermediate steps in `problems/solutions/chNN_solutions.md`
- [ ] One-page reference sheet
- [ ] Frequent analytical errors
- [ ] Connections to other chapters
- [ ] `tests/test_chNN_examples.py` passes and covers every number in the text, problems, and solutions
- [ ] Sources registered; pending items flagged in text
- [ ] Editorial pass: no padding, no slogans, no repetition, no unexplained equations

## 3. Numerical quality control
For every numerical example:
1. State assumptions explicitly, including timing (beginning or end of period), compounding, and units.
2. Show the formula, the substitution, and intermediate results.
3. Verify with Python in `tests/`. Prefer an independent route (reverse calculation, identity, closed form against schedule) over calling the same function twice.
4. Keep units consistent and check dimensions (\$ / \$ = ratio; \$/yr ÷ %/yr = \$).
5. Test boundary cases where the library is involved: zero rate, zero leverage, 100% loss, IRR undefined.
6. Distinguish model assumptions from empirical estimates.
7. Note when higher-order terms (convexity, Jensen's inequality, compounding) materially change a result.

Specific traps that tests must cover where relevant: annual versus monthly rates; nominal versus effective; end- versus beginning-of-period; room versus total revenue; NOI versus EBITDA; transaction costs; terminal value on forward NOI; reserves versus capex; balloon balances; IRR timing; futures multipliers; FX quote direction.

## 4. Historical case standard
Each historical case states: date and environment; information public at the time; documented expectations; valuation and financing context; participants and incentives; leverage and liquidity; catalysts; price behavior; alternative interpretations; strategies available then; what happened; what the case does and does not establish. Ex-ante knowledge is separated from hindsight.

## 5. Judgment problems
For Level 4–5 problems and judgment drills, provide a decision rubric, competing explanations, and the information that would change the conclusion. Do not present one trade as uniquely correct unless the problem is objectively determinate. Include problems where abstention is the best answer.

## 6. Code quality
* Library functions document units, sign conventions, timing, and Excel equivalents.
* No silent unit conversions. Inputs in decimals.
* Tests run with `python3 -m pytest -q tests` and must pass before any commit that changes numbers.
* Exports and models are not described as working unless a test or a recorded run has shown they work.

## 7. Editorial review stages
1. **Authoring**: content against the chapter checklist.
2. **Mathematical verification**: every number reproduced in tests; discrepancies fixed in the text, not in the test.
3. **Historical fact-check**: every [FACT] mapped to a register entry with status.
4. **Editorial**: cut padding and repetition, check tone, check cross-references.
