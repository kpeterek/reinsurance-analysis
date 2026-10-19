"""Non-interactive tests of the desk simulator."""

import datetime as dt

from sdesk import simulator as sim


def _bank():
    return sim.load_bank()


def _drill(bank, did):
    return next(d for d in bank if d["id"] == did)


def test_parse_number():
    assert sim.parse_number("$1,234.5") == 1234.5
    assert sim.parse_number("-7.69%") == -7.69
    assert sim.parse_number("(9,000)") == -9000
    assert sim.parse_number("1.25x") == 1.25
    assert sim.parse_number("abc") is None
    assert sim.parse_number("") is None


def test_numeric_session_records_and_grades():
    bank = _bank()
    con = sim.connect(":memory:")
    d = _drill(bank, "D002")
    answers = iter(["3,942,000", "150000"])  # second part wrong
    out = sim.run_drill(d, ask=lambda _: next(answers), say=lambda _: None, clock=iter([0.0, 20.0]).__next__)
    assert [ok for _, _, ok in out["results"]] == [True, False]
    sim.record_attempt(con, d, out["results"], seconds=out["seconds"])
    row = con.execute("SELECT numeric_parts, numeric_correct, seconds FROM attempts").fetchone()
    assert row == (2, 1, 20.0)
    rep = sim.weekly_report(con, bank)
    assert "hotel_metrics" in rep and "expected 1.642e+05" in rep
    assert "not evidence of trading ability" in rep


def test_judgment_drill_rubric_and_no_single_answer():
    bank = _bank()
    con = sim.connect(":memory:")
    d = _drill(bank, "D014")
    n_items = len(d["answer"]["rubric"])
    answers = iter(["wait", "lose deposit 100k", "lender quotes improve"] + ["2"] * n_items)
    lines = []
    out = sim.run_drill(d, ask=lambda _: next(answers), say=lines.append, clock=iter([0.0, 60.0]).__next__)
    assert out["decision"] == "wait"
    assert sim.rubric_score(out["rubric_points"]) == 4.0
    assert any("Several decisions can be defensible" in s for s in lines)
    sim.record_attempt(con, d, out["results"], out["rubric_points"], out["decision"],
                       out["risk_statement"], out["invalidation"], out["seconds"])
    assert con.execute("SELECT rubric_points FROM attempts").fetchone()[0] == 4.0


def test_mastery_gate_requires_85_percent_over_10():
    bank = _bank()
    con = sim.connect(":memory:")
    d = _drill(bank, "D007")
    part = d["answer"]["parts"][0]
    for i in range(10):
        ok = i != 0  # 9/10 correct
        sim.record_attempt(con, d, [(part, part["value"] if ok else 0.0, ok)])
    m = sim.topic_mastery(con)["risk_math"]
    assert m["numeric_accuracy"] == 0.9 and m["mastered"]
    sim.record_attempt(con, d, [(part, 0.0, False)])
    sim.record_attempt(con, d, [(part, 0.0, False)])
    m = sim.topic_mastery(con)["risk_math"]
    assert m["numeric_accuracy"] == 0.8 and not m["mastered"]  # last 10: 8 of 10
    assert any(r.startswith("risk_math") for r in sim.recommend_review(con, bank))


def test_report_window():
    bank = _bank()
    con = sim.connect(":memory:")
    d = _drill(bank, "D007")
    part = d["answer"]["parts"][0]
    sim.record_attempt(con, d, [(part, 1.0, False)], ts="2020-01-01T00:00:00")
    rep = sim.weekly_report(con, bank, today=dt.date(2026, 10, 19))
    assert "risk_math" not in rep.split("Recommended review:")[0]


def test_select_filters():
    bank = _bank()
    a = sim.select_drills(bank, category="A", n=100, seed=1)
    assert a and all(d["category"] == "A" for d in a)
    assert all(d["difficulty"] <= 1 for d in sim.select_drills(bank, max_difficulty=1, n=100))
