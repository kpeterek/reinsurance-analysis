"""sdesk -- calculation library for *The Speculator's Desk*.

Every numerical example in the textbook, the cases, and the drill bank is
reproduced by functions in this package and checked by the test suite in
``tests/``.

Conventions (see textbook/frontmatter/03_notation_and_style_guide.md):

* Rates are decimals (0.065 means 6.5%). Basis points appear only in names
  ending in ``_bps``.
* Cash flows are lists indexed by period; element 0 occurs at t = 0.
  Outflows from the investor's point of view are negative.
* Loan payments are positive numbers. We do NOT use Excel's sign flip in
  Python; the Excel equivalents are documented in each docstring.
* Unless stated otherwise, payments occur at the END of each period.
"""

from . import tvm, cre, hotel, fixed_income, markets, risk, stats  # noqa: F401

__all__ = ["tvm", "cre", "hotel", "fixed_income", "markets", "risk", "stats"]
