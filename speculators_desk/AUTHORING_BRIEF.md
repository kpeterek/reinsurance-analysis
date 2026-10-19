# Authoring Brief (for every chapter and case author)

This brief applies to every author: human or AI, and every staged authoring pass. Read it in full before writing.

## 1. Read first
1. `textbook/frontmatter/03_notation_and_style_guide.md`: binding conventions, evidence labels, chapter template, worked-example format.
2. `QUALITY_STANDARDS.md`: the completion checklist.
3. The exemplar unit: `textbook/part_01_foundations/ch01_what_is_speculation.md`, `problems/questions/ch01_problems.md`, `problems/solutions/ch01_solutions.md`, `tests/test_ch01_examples.py`. Match its depth, tone, and verification discipline.
4. The exemplar case: `cases/hypothetical/case_A_overpriced_hotel_owner/` (case file with Modes A–D, separate rubric, `case_a_model.py`) and `tests/test_case_a.py`.
5. The library: `models/python/sdesk/*.py`. Use it. Do not duplicate it.
6. The drill format: `training/daily_drills/drill_bank.json` and `drill_checks.py`.

## 2. The reader
About 12 years of CRE finance, valuation, underwriting, and brokerage, including hotels. Strong Excel. Has passed actuarial probability and financial-mathematics exams. Prefers pen-and-paper reasoning and investment memoranda. Do not explain basic finance. Build from existing competence toward institutional judgment. Give the financial intuition first, then the mathematics, then the decision consequence.

## 3. Non-negotiables
* **Every number is reproducible.** Every number in the chapter text, problems, and solutions is recomputed in `tests/test_chNN_examples.py` (or `tests/test_case_x.py`). When a test disagrees with the text, fix the text.
* **No invented facts.** Never invent quotations, historical prices, yields, transaction terms, data values, or sources. Verify historical figures with web search against primary or official sources where possible (FRED, Federal Reserve, BLS, BEA, Treasury, FDIC, SEC, NBER, CME, CFTC, Nareit, company filings). If you cannot verify a figure, do not state it as fact: write *(verification pending)* or rephrase qualitatively. Label claims [FACT], [INFERENCE], [HYPOTHESIS], or [SPECULATION] wherever confusion is possible.
* **Hypothetical numbers are labeled** (state once at the top of a case or example that the inputs are hypothetical). Market "typical ranges" are assumptions unless a dated source is cited.
* **Every chapter contains:** learning objectives; a realistic opening investment problem; intuition; definitions; equations with derivations; **at least three** (preferably five to seven) fully worked numerical examples, each ending with "Decision consequence"; a CRE application; "When the relationship fails"; a sourced historical episode (date and environment, what was knowable then, interpretations, what it does and does not establish); a decision exercise with rubric; frequent analytical errors; connections; a one-page reference sheet. **Ten problems** (Levels 1–5) go in `problems/questions/chNN_problems.md` and complete solutions with intermediate steps in `problems/solutions/chNN_solutions.md`. Level 4–5 problems need rubrics. At least one problem or drill should have abstention as the best answer.
* **Status line** at the top of the chapter: `> **Status:** Complete (v1.0). ...` only if every checklist item is met; otherwise `> **Status:** Draft ...` with what is missing.
* **Style:** direct, technical, skeptical, precise. No motivational filler, trading clichés, slogans, or generic AI prose. Every five pages must give a sophisticated reader something tangible. Use tables for comparisons. Show formula → substitution → intermediate results → result.
* **Timing and units traps** (test where relevant): annual vs monthly rates; nominal vs effective; end- vs beginning-of-period; rooms vs total revenue; NOI vs EBITDA; transaction costs; terminal value on forward NOI; reserves vs capex; balloon balances; IRR timing; futures multipliers; FX quote direction; yields in decimals.

## 4. File ownership (parallel authors must not collide)
You may **create or edit only**:
* your chapter file in `textbook/part_NN_*/chNN_<slug>.md`
* `problems/questions/chNN_problems.md`, `problems/solutions/chNN_solutions.md`
* `tests/test_chNN_examples.py`
* `training/daily_drills/drill_bank_chNN.json` and `training/daily_drills/drill_checks_chNN.py` (your assigned drill ID range only)
* `references/sources_chNN.md` (your source entries, in the same table format as `SOURCE_REGISTER.md`, with IDs `chNN-S01`, ...); the editor merges them into the register
* any case folder assigned to you: `cases/hypothetical/case_X_<slug>/` plus `tests/test_case_x.py` and `cases/datasets/case_x_*.csv`
* **new** library modules only, named `models/python/sdesk/x_<topic>.py`, with tests in your own test file

Do **not** edit existing `sdesk` modules, `SOURCE_REGISTER.md`, `PROGRESS.md`, `ROADMAP.md`, other authors' files, or shared tests. Do not run `git commit` or `git push`. If an existing library function has a bug, report it with a failing example instead of editing it.

## 5. Drill file format
`drill_bank_chNN.json`: `{"schema_version": 1, "drills": [...]}` with the same fields as `drill_bank.json`. `drill_checks_chNN.py` defines `dNNN(inputs) -> list[float]` for each numeric or mixed drill and ends with:
```python
CHECKS = {k.upper(): v for k, v in globals().items() if k[0] == "d" and k[1:].isdigit() and callable(v)}
```
Import the library with:
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "models" / "python"))
```
Mix categories A–F. Include messy, contradictory, incomplete-information drills and at least one where the right answer is to abstain.

## 6. Done means
`python3 -m pytest -q tests` passes in full. Report: files created, approximate word counts, test count, verified sources, pending verifications, and any library issues found.

## 7. Working alongside other authors
Other authors write files at the same time. If the full test suite fails **only** in files you do not own (another author's work in progress), first run your own tests (`python3 -m pytest -q tests/test_chNN_examples.py tests/test_drills.py -k "DNNN or chNN"` and your case tests). Retry the full suite a few minutes later. Report the foreign failure, but do not fix another author's files. Do not delete or rewrite files you did not create.
