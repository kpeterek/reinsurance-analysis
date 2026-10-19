#!/usr/bin/env python3
"""Merge per-author source tables (references/sources_*.md) into SOURCE_REGISTER.md.

Rows are table lines beginning with "| <ID> |" where ID is not 'ID'. Rows whose ID
already appears in the register are skipped. Rows are appended to the main table
(before the "## Pending verification queue" heading). Idempotent.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "SOURCE_REGISTER.md"
ROW = re.compile(r"^\|\s*([A-Za-z0-9][A-Za-z0-9_\-]*)\s*\|")


def main():
    reg = REG.read_text()
    existing = {m.group(1) for line in reg.splitlines() if (m := ROW.match(line))}
    new_rows = []
    for f in sorted((ROOT / "references").glob("sources_*.md")):
        for line in f.read_text().splitlines():
            m = ROW.match(line)
            if not m or m.group(1) in ("ID", "Id", "id") or set(m.group(1)) <= {"-"}:
                continue
            if m.group(1) not in existing:
                new_rows.append(line.rstrip())
                existing.add(m.group(1))
    if not new_rows:
        print("no new rows")
        return
    marker = "\n## Pending verification queue"
    head, sep, tail = reg.partition(marker)
    REG.write_text(head.rstrip("\n") + "\n" + "\n".join(new_rows) + "\n" + sep + tail)
    print(f"merged {len(new_rows)} rows")


if __name__ == "__main__":
    main()
