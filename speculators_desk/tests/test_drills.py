"""Validates the drill bank: schema completeness and numeric answers."""

import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
DRILL_DIR = ROOT / "training/daily_drills"
BANK = {"drills": []}
for _f in sorted(DRILL_DIR.glob("drill_bank*.json")):
    BANK["drills"].extend(json.loads(_f.read_text())["drills"])

CHECKS = {}
for _f in sorted(DRILL_DIR.glob("drill_checks*.py")):
    _spec = importlib.util.spec_from_file_location(_f.stem, _f)
    _m = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_m)
    overlap = set(CHECKS) & set(_m.CHECKS)
    assert not overlap, f"duplicate drill checks {overlap}"
    CHECKS.update(_m.CHECKS)

REQUIRED = ["id", "category", "topic", "difficulty", "time_minutes", "title", "inputs", "question",
            "answer", "solution", "common_mistakes", "intuition", "takeaway", "related"]


@pytest.mark.parametrize("drill", BANK["drills"], ids=lambda d: d["id"])
def test_schema(drill):
    for k in REQUIRED:
        assert k in drill and drill[k] not in (None, "", []), f"{drill['id']} missing {k}"
    assert drill["category"] in "ABCDEF"
    assert 1 <= drill["difficulty"] <= 5
    a = drill["answer"]
    assert a["type"] in ("numeric", "judgment", "mixed")
    if a["type"] in ("numeric", "mixed"):
        assert a["parts"]
    if a["type"] in ("judgment", "mixed"):
        assert len(a["rubric"]) >= 3


def test_unique_ids():
    ids = [d["id"] for d in BANK["drills"]]
    assert len(ids) == len(set(ids))


NUMERIC = [d for d in BANK["drills"] if d["answer"]["type"] in ("numeric", "mixed")]


@pytest.mark.parametrize("drill", NUMERIC, ids=lambda d: d["id"])
def test_numeric_answers(drill):
    assert drill["id"] in CHECKS, f"no independent check for {drill['id']}"
    computed = CHECKS[drill["id"]](drill["inputs"])
    parts = drill["answer"]["parts"]
    assert len(computed) == len(parts)
    for part, val in zip(parts, computed):
        assert val == pytest.approx(part["value"], abs=part["tolerance"]), (drill["id"], part["label"], val)
