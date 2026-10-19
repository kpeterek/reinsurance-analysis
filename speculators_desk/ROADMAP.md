# Production Roadmap

The book is built in stages. Each stage ends with all tests passing, `PROGRESS.md` refreshed by `scripts/progress.py`, and a commit. Chapters are written in full, one at a time (or in small parallel batches that each pass the full checklist), then verified. No stage produces outline-only placeholders presented as content.

Priority order, as the brief directs: **foundations → macro mechanics → the full CRE module → cross-asset → quantitative → history → decision-making**. CRE gets the most depth (planned share of the book: CRE and hotels about 40%, macro and rates 20%, quant and risk 20%, other markets 12%, history and desk operations 8%).

## Stage 0 — Infrastructure (complete)
- Repository structure, notation and style guide, competency map, table of contents, quality standards, source register
- `sdesk` Python library (TVM, CRE, hotel, fixed income, markets, risk, stats) with independent tests
- Simulator CLI with SQLite progress tracking, mastery gating, weekly report
- Excel workbook generator with LibreOffice recalculation tests
- SQL schema, simulated sample data, named queries with tests
- Manuscript assembly, navigation index, HTML and PDF export (tested in this environment with pandoc 3.1 and headless Chromium)

## Stage 1 — First production unit (complete)
- Chapter 1 with 10 problems and full solutions, verified by `tests/test_ch01_examples.py`
- Case A (Overpriced Hotel Owner), Modes A–D, separate rubric, reproducible model, data exhibit
- Drills D001–D015

## Stage 2 — Rates and core CRE (next)
1. Chapter 6 — Fixed Income and the Cost of Capital
2. Chapter 8 — Fundamental Economics of CRE
3. Chapter 9 — CRE Valuation and Mispricing
4. Chapter 10 — Capital Structure, Debt, and Equity
5. Chapter 11 — Hotels (eight hotel cases)
6. Cases B (Refinancing Cliff), C (Cap Rate Expansion), D (PIP Negotiation)
7. Drills D016–D060, weighted toward CRE, hotels, and rates

## Stage 3 — Macro and remaining CRE
- Chapters 2, 3, 4, 5, 7, 12, 13
- Cases E (Distressed Office), F (Hotel vs Treasury), G (Buying the Debt), H (Cross-Asset Shock), I (Land Option), J (Credit Crunch Hotel)
- Drills D061–D100

## Stage 4 — Cross-asset and quantitative
- Chapters 14–22
- Drills D101–D150+; a "1987 desk exercise" in each of Chapters 6, 11, 15, and 21

## Stage 5 — History and judgment
- Chapter 23 with a stand-alone historical case file per episode in `cases/historical/`
- Chapters 24–25; full template set in `desk/`

## Stage 6 — Program and capstone
- 16-week curriculum detail, weekly exams, baseline, intermediate, and final assessments
- Final capstone with instructor solution
- Appendices A–F (formula compendium completed from all chapters)

## Stage 7 — Verification and editorial pass
- Clear the `PENDING` queue in `SOURCE_REGISTER.md`
- Whole-book editorial pass for repetition and cross-references
- Final exports

## Checkpoint protocol
If a session ends mid-stage, `PROGRESS.md` §Checkpoint records: the file being written, what is complete in it, failing tests (if any), and the next action. Resume from that note.
