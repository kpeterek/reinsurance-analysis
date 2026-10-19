#!/usr/bin/env python3
"""Structural checker for chapters marked Complete.

Verifies that every required element of the chapter template (style guide §7)
is present, that there are at least three worked examples each with a
"Decision consequence", that the problems file has ten problems spanning
Levels 1-5, that a solutions file exists, and that a test module exists.

  python3 scripts/check_chapter.py            # check all chapters, print report
  python3 scripts/check_chapter.py 1 6 11     # check specific chapters

Exit status 1 if any chapter whose status is Complete fails a check.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "learning objectives": r"learning objectives",
    "opening problem": r"opening (investment )?problem",
    "intuition": r"intuition",
    "definitions": r"definitions",
    "equations": r"equation|derivation|\$\$",
    "CRE application": r"CRE application|commercial real estate application|application to CRE|CRE connection",
    "failure modes": r"fail",
    "historical episode": r"historical (episode|case)",
    "decision exercise": r"decision exercise",
    "frequent errors": r"(frequent|common) (analytical )?errors",
    "connections": r"connections to other chapters|connections",
    "reference sheet": r"reference sheet|formula sheet",
}


def check(path: Path) -> dict:
    text = path.read_text()
    headings = "\n".join(l for l in text.splitlines() if l.lstrip().startswith("#"))
    n = re.match(r"ch(\d\d)", path.name).group(1)
    missing = [k for k, pat in REQUIRED.items()
               if not re.search(pat, headings, flags=re.I) and not (k == "equations" and "$$" in text)]
    examples = len(re.findall(r"^#{2,4}\s*(Worked )?Example\s+\d+\.\d+", text, flags=re.M | re.I))
    decisions = len(re.findall(r"Decision consequence", text))
    status = re.search(r"\*\*Status:\*\*\s*([A-Za-z]+)", text)
    q = ROOT / f"problems/questions/ch{n}_problems.md"
    s = ROOT / f"problems/solutions/ch{n}_solutions.md"
    t = ROOT / f"tests/test_ch{n}_examples.py"
    problems = levels = 0
    if q.exists():
        qt = q.read_text()
        problems = len(re.findall(r"^### Problem ", qt, flags=re.M))
        levels = len(set(re.findall(r"Level\s*([1-5])", qt)))
    issues = []
    if missing:
        issues.append("missing sections: " + ", ".join(missing))
    if examples < 3:
        issues.append(f"only {examples} worked examples")
    if decisions < min(examples, 3):
        issues.append(f"only {decisions} 'Decision consequence' paragraphs")
    if problems < 10:
        issues.append(f"{problems} problems (need 10)")
    if levels < 5:
        issues.append(f"problem levels present: {levels}/5")
    if not s.exists():
        issues.append("no solutions file")
    if not t.exists():
        issues.append("no example test module")
    return {"chapter": n, "status": status.group(1) if status else "Unknown", "examples": examples,
            "problems": problems, "issues": issues}


def main(argv):
    chosen = {f"{int(a):02d}" for a in argv}
    files = sorted((ROOT / "textbook").glob("part_*/ch[0-9][0-9]_*.md"))
    bad = False
    for f in files:
        n = re.match(r"ch(\d\d)", f.name).group(1)
        if chosen and n not in chosen:
            continue
        r = check(f)
        flag = "OK " if not r["issues"] else "!! "
        if r["issues"] and r["status"].lower() == "complete":
            bad = True
        print(f"{flag}ch{n} [{r['status']}] examples={r['examples']} problems={r['problems']}"
              + ("" if not r["issues"] else " | " + "; ".join(r["issues"])))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
