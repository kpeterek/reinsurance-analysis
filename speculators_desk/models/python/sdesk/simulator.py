"""The Daily Trading Desk Simulator — command-line drill engine.

Design principles (see README §Simulator):
* Numeric parts are graded automatically against tolerances.
* Judgment parts are graded on a transparent rubric. The student self-scores
  each rubric item after seeing the worked solution; no single trade is declared
  "correct" when the evidence supports several reasonable decisions.
* Calculation and reasoning scores are stored separately.
* Progress lives in a local SQLite database (default:
  training/performance_tracking/desk_progress.sqlite).
* Mastery gating: objective topics advance at >= 85% rolling accuracy over the
  last 10 numeric parts; judgment topics at a mean rubric score >= 3.0/4 over the
  last 5 attempts.
* Simulated scores are not evidence of real-market trading ability.
"""

from __future__ import annotations

import datetime as dt
import json
import random
import sqlite3
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[3]
BANK_PATH = ROOT / "training" / "daily_drills" / "drill_bank.json"
DB_PATH = ROOT / "training" / "performance_tracking" / "desk_progress.sqlite"

DECISIONS = ("buy", "sell", "hold", "hedge", "wait", "pass", "invest", "not applicable")

SCHEMA = """
CREATE TABLE IF NOT EXISTS attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts TEXT NOT NULL,
    drill_id TEXT NOT NULL,
    topic TEXT NOT NULL,
    category TEXT NOT NULL,
    difficulty INTEGER NOT NULL,
    numeric_parts INTEGER NOT NULL DEFAULT 0,
    numeric_correct INTEGER NOT NULL DEFAULT 0,
    rubric_items INTEGER NOT NULL DEFAULT 0,
    rubric_points REAL NOT NULL DEFAULT 0,
    decision TEXT,
    risk_statement TEXT,
    invalidation TEXT,
    seconds REAL
);
CREATE TABLE IF NOT EXISTS part_results (
    attempt_id INTEGER NOT NULL REFERENCES attempts(id),
    label TEXT NOT NULL,
    expected REAL NOT NULL,
    given REAL,
    correct INTEGER NOT NULL
);
"""


# ----------------------------------------------------------------- data access

def load_bank(path: Path = BANK_PATH) -> list[dict]:
    return json.loads(Path(path).read_text())["drills"]


def connect(db_path: Path | str = DB_PATH) -> sqlite3.Connection:
    if str(db_path) != ":memory:":
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(str(db_path))
    con.executescript(SCHEMA)
    return con


# ----------------------------------------------------------------- grading

def parse_number(text: str) -> float | None:
    """Accept '1,234', '$1,234', '-7.7%', '1.25x', '(9,000)'."""
    if text is None:
        return None
    t = text.strip().replace(",", "").replace("$", "").replace("%", "").replace("x", "").replace("USD", "")
    neg = t.startswith("(") and t.endswith(")")
    t = t.strip("()").strip()
    if not t:
        return None
    try:
        v = float(t)
    except ValueError:
        return None
    return -v if neg else v


def grade_numeric(part: dict, given: float | None) -> bool:
    if given is None:
        return False
    return abs(given - part["value"]) <= part["tolerance"]


def rubric_score(points: list[int]) -> float:
    """Map per-item self-scores (0 = absent, 1 = partial, 2 = full) to a 0-4 scale."""
    if not points:
        return 0.0
    return 4.0 * sum(points) / (2 * len(points))


# ----------------------------------------------------------------- persistence

def record_attempt(con: sqlite3.Connection, drill: dict, part_results: list[tuple[dict, float | None, bool]],
                   rubric_points: list[int] | None = None, decision: str | None = None,
                   risk_statement: str | None = None, invalidation: str | None = None,
                   seconds: float | None = None, ts: str | None = None) -> int:
    ts = ts or dt.datetime.now().isoformat(timespec="seconds")
    rp = rubric_points or []
    cur = con.execute(
        "INSERT INTO attempts (ts, drill_id, topic, category, difficulty, numeric_parts, numeric_correct,"
        " rubric_items, rubric_points, decision, risk_statement, invalidation, seconds)"
        " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (ts, drill["id"], drill["topic"], drill["category"], drill["difficulty"], len(part_results),
         sum(1 for _, _, ok in part_results if ok), len(rp), rubric_score(rp) if rp else 0.0,
         decision, risk_statement, invalidation, seconds))
    aid = cur.lastrowid
    con.executemany("INSERT INTO part_results (attempt_id, label, expected, given, correct) VALUES (?,?,?,?,?)",
                    [(aid, p["label"], p["value"], g, int(ok)) for p, g, ok in part_results])
    con.commit()
    return aid


# ----------------------------------------------------------------- analytics

def topic_mastery(con: sqlite3.Connection) -> dict:
    """Rolling accuracy (last 10 numeric parts) and rubric mean (last 5) by topic."""
    out: dict = {}
    topics = [r[0] for r in con.execute("SELECT DISTINCT topic FROM attempts")]
    for t in topics:
        parts = con.execute(
            "SELECT pr.correct FROM part_results pr JOIN attempts a ON a.id = pr.attempt_id"
            " WHERE a.topic = ? ORDER BY a.id DESC, pr.rowid DESC LIMIT 10", (t,)).fetchall()
        rub = con.execute("SELECT rubric_points FROM attempts WHERE topic = ? AND rubric_items > 0"
                          " ORDER BY id DESC LIMIT 5", (t,)).fetchall()
        acc = sum(p[0] for p in parts) / len(parts) if parts else None
        rmean = sum(r[0] for r in rub) / len(rub) if rub else None
        objective_ok = acc is None or (len(parts) >= 10 and acc >= 0.85)
        judgment_ok = rmean is None or (len(rub) >= 5 and rmean >= 3.0)
        out[t] = {"numeric_accuracy": acc, "numeric_n": len(parts), "rubric_mean": rmean,
                  "rubric_n": len(rub), "mastered": objective_ok and judgment_ok and (parts or rub)}
    return out


def recommend_review(con: sqlite3.Connection, bank: list[dict]) -> list[str]:
    """Topics ordered by weakness, with related chapters to reread."""
    m = topic_mastery(con)
    related = {}
    for d in bank:
        related.setdefault(d["topic"], set()).update(d["related"])

    def weakness(item):
        t, s = item
        acc = s["numeric_accuracy"] if s["numeric_accuracy"] is not None else 1.0
        rub = (s["rubric_mean"] / 4.0) if s["rubric_mean"] is not None else 1.0
        return min(acc, rub)

    recs = []
    for t, s in sorted(m.items(), key=weakness):
        if s["mastered"]:
            continue
        recs.append(f"{t}: accuracy={_fmt(s['numeric_accuracy'])} (n={s['numeric_n']}), "
                    f"rubric={_fmt(s['rubric_mean'], pct=False)} (n={s['rubric_n']}); reread "
                    + ", ".join(sorted(related.get(t, []))))
    return recs


def weekly_report(con: sqlite3.Connection, bank: list[dict], days: int = 7, today: dt.date | None = None) -> str:
    today = today or dt.date.today()
    start = (today - dt.timedelta(days=days)).isoformat()
    rows = con.execute(
        "SELECT topic, COUNT(*), SUM(numeric_parts), SUM(numeric_correct), "
        "AVG(CASE WHEN rubric_items > 0 THEN rubric_points END), AVG(seconds) "
        "FROM attempts WHERE ts >= ? GROUP BY topic ORDER BY topic", (start,)).fetchall()
    lines = [f"Weekly desk report: {start} to {today.isoformat()}",
             "(Scores measure performance on curated drills only; they are not evidence of trading ability.)", "",
             f"{'topic':<22}{'attempts':>9}{'calc acc':>10}{'rubric':>8}{'avg sec':>9}"]
    for topic, n, parts, correct, rub, secs in rows:
        acc = (correct / parts) if parts else None
        lines.append(f"{topic:<22}{n:>9}{_fmt(acc):>10}{_fmt(rub, pct=False):>8}{(secs or 0):>9.0f}")
    errs = con.execute(
        "SELECT a.drill_id, pr.label, pr.expected, pr.given FROM part_results pr JOIN attempts a"
        " ON a.id = pr.attempt_id WHERE pr.correct = 0 AND a.ts >= ? ORDER BY a.id", (start,)).fetchall()
    if errs:
        lines += ["", "Calculation errors this period:"]
        lines += [f"  {d} | {lab}: expected {e:,.4g}, given {'blank' if g is None else f'{g:,.4g}'}"
                  for d, lab, e, g in errs]
    recs = recommend_review(con, bank)
    lines += ["", "Recommended review:"] + ([f"  - {r}" for r in recs] or ["  (no weak topics recorded)"])
    return "\n".join(lines)


def _fmt(x, pct: bool = True) -> str:
    if x is None:
        return "-"
    return f"{100 * x:.0f}%" if pct else f"{x:.2f}"


# ----------------------------------------------------------------- selection

def select_drills(bank: list[dict], category: str | None = None, topic: str | None = None,
                  max_difficulty: int | None = None, n: int = 5, seed: int | None = None) -> list[dict]:
    pool = [d for d in bank
            if (category is None or d["category"] == category.upper())
            and (topic is None or d["topic"] == topic)
            and (max_difficulty is None or d["difficulty"] <= max_difficulty)]
    rng = random.Random(seed)
    rng.shuffle(pool)
    return pool[:n]


def adaptive_difficulty(con: sqlite3.Connection, topic: str) -> int:
    """Raise the difficulty ceiling one level per mastered topic gate, starting at 2."""
    m = topic_mastery(con).get(topic)
    if not m:
        return 2
    return 5 if m["mastered"] else 3


# ----------------------------------------------------------------- interactive session

def run_drill(drill: dict, ask: Callable[[str], str] = input, say: Callable[[str], None] = print,
              clock: Callable[[], float] | None = None) -> dict:
    import time
    clock = clock or time.monotonic
    say("")
    say("=" * 78)
    say(f"[{drill['id']}] {drill['title']}  | category {drill['category']} | topic {drill['topic']}"
        f" | level {drill['difficulty']} | target {drill['time_minutes']} min")
    say("-" * 78)
    say(drill["question"])
    say(f"Inputs: {json.dumps(drill['inputs'])}")
    t0 = clock()
    a = drill["answer"]
    results = []
    for part in a.get("parts", []) if a["type"] in ("numeric", "mixed") else []:
        g = parse_number(ask(f"  {part['label']}: "))
        results.append((part, g, grade_numeric(part, g)))
    decision = risk_stmt = invalid = None
    if a["type"] in ("judgment", "mixed"):
        say("  Write your reasoning on paper or in your journal, then answer:")
        decision = ask(f"  Decision {DECISIONS}: ").strip().lower() or None
        risk_stmt = ask("  Risk exposure (what can you lose, how much): ").strip() or None
        invalid = ask("  Invalidation (what evidence would make you reverse): ").strip() or None
    seconds = clock() - t0
    say("-" * 78)
    for part, g, ok in results:
        say(f"  {part['label']}: {'CORRECT' if ok else 'INCORRECT'}  expected {part['value']:,} "
            f"(tolerance {part['tolerance']}) | you gave {g}")
    say("Worked solution: " + drill["solution"])
    say("Common mistakes: " + "; ".join(drill["common_mistakes"]))
    say("Intuition: " + drill["intuition"])
    say("Takeaway: " + drill["takeaway"])
    rubric_points: list[int] = []
    if a["type"] in ("judgment", "mixed"):
        say("Rubric self-assessment: score each item 0 (absent), 1 (partial), 2 (full).")
        say("Several decisions can be defensible; you are scoring the reasoning, not the trade.")
        for item in a["rubric"]:
            s = ask(f"  [{item}] 0/1/2: ").strip()
            rubric_points.append(int(s) if s in ("0", "1", "2") else 0)
        if not risk_stmt or not invalid:
            say("  Note: a decision without stated risk and invalidation scores 0 on those items in IC review.")
    say("Related reading: " + ", ".join(drill["related"]))
    return {"results": results, "rubric_points": rubric_points, "decision": decision,
            "risk_statement": risk_stmt, "invalidation": invalid, "seconds": seconds}


def session(category: str | None = None, topic: str | None = None, n: int = 5,
            db_path: Path | str = DB_PATH, ask: Callable[[str], str] = input,
            say: Callable[[str], None] = print, seed: int | None = None) -> None:
    bank = load_bank()
    con = connect(db_path)
    ceiling = adaptive_difficulty(con, topic) if topic else None
    drills = select_drills(bank, category, topic, ceiling, n, seed)
    if not drills:
        say("No drills match that selection.")
        return
    for d in drills:
        out = run_drill(d, ask, say)
        record_attempt(con, d, out["results"], out["rubric_points"], out["decision"],
                       out["risk_statement"], out["invalidation"], out["seconds"])
    say("")
    say(weekly_report(con, bank))
