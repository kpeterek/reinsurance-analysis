#!/usr/bin/env python3
"""Command-line entry point for the Daily Trading Desk Simulator.

Examples
--------
  python3 scripts/desk.py list                      # list drills
  python3 scripts/desk.py drill -n 5                # five random drills
  python3 scripts/desk.py drill --category A -n 10  # 30-second mental math
  python3 scripts/desk.py drill --topic hotel_metrics
  python3 scripts/desk.py report                    # weekly performance report
  python3 scripts/desk.py mastery                   # topic mastery table
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "models" / "python"))

from sdesk import simulator as sim  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser(description="The Speculator's Desk — drill simulator")
    ap.add_argument("--db", default=str(sim.DB_PATH), help="progress database path")
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("drill")
    d.add_argument("--category", choices=list("ABCDEF"))
    d.add_argument("--topic")
    d.add_argument("-n", type=int, default=5)
    d.add_argument("--seed", type=int)
    sub.add_parser("list")
    sub.add_parser("report")
    sub.add_parser("mastery")
    a = ap.parse_args(argv)

    bank = sim.load_bank()
    if a.cmd == "list":
        for x in bank:
            print(f"{x['id']}  {x['category']}  L{x['difficulty']}  {x['topic']:<22} {x['title']}")
    elif a.cmd == "drill":
        sim.session(a.category, a.topic, a.n, a.db, seed=a.seed)
    elif a.cmd == "report":
        print(sim.weekly_report(sim.connect(a.db), bank))
    elif a.cmd == "mastery":
        for t, s in sim.topic_mastery(sim.connect(a.db)).items():
            print(t, s)


if __name__ == "__main__":
    main()
