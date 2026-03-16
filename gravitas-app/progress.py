"""
Progress tracking and persistence for the Gravitas Training Program.
"""

import json
import os
from datetime import datetime, date

PROGRESS_FILE = os.path.join(os.path.dirname(__file__), "user_progress.json")


def _default_progress():
    return {
        "start_date": str(date.today()),
        "current_week": 1,
        "completed_drills": {},  # {week: [drill_indices]}
        "phrase_mastery": {},    # {phrase: {"times_practiced": N, "mastered": bool}}
        "daily_log": [],         # [{date, week, notes, self_rating}]
        "streak_days": 0,
        "last_practice_date": None,
        "milestone_assessments": {},  # {week: {passed: bool, date, notes}}
    }


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return _default_progress()


def save_progress(data):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(data, f, indent=2)


def update_streak(progress):
    today = str(date.today())
    last = progress.get("last_practice_date")
    if last == today:
        return  # already practiced today
    if last == str(date.today().replace(day=date.today().day - 1)) if date.today().day > 1 else None:
        progress["streak_days"] += 1
    else:
        progress["streak_days"] = 1
    progress["last_practice_date"] = today


def mark_drill_complete(progress, week, drill_index):
    key = str(week)
    if key not in progress["completed_drills"]:
        progress["completed_drills"][key] = []
    if drill_index not in progress["completed_drills"][key]:
        progress["completed_drills"][key].append(drill_index)


def mark_phrase_practiced(progress, phrase):
    if phrase not in progress["phrase_mastery"]:
        progress["phrase_mastery"][phrase] = {"times_practiced": 0, "mastered": False}
    progress["phrase_mastery"][phrase]["times_practiced"] += 1
    if progress["phrase_mastery"][phrase]["times_practiced"] >= 10:
        progress["phrase_mastery"][phrase]["mastered"] = True


def add_daily_log(progress, week, notes, self_rating):
    progress["daily_log"].append({
        "date": str(date.today()),
        "week": week,
        "notes": notes,
        "self_rating": self_rating,
    })


def get_week_progress_summary(progress, week):
    key = str(week)
    drills_done = len(progress["completed_drills"].get(key, []))
    phrases_for_week = {k: v for k, v in progress["phrase_mastery"].items()}
    mastered = sum(1 for v in phrases_for_week.values() if v["mastered"])
    return {
        "drills_completed": drills_done,
        "phrases_mastered": mastered,
        "total_phrases_practiced": len(phrases_for_week),
    }


def calculate_overall_progress(progress):
    start = datetime.strptime(progress["start_date"], "%Y-%m-%d").date()
    days_in = (date.today() - start).days
    expected_week = min(12, max(1, (days_in // 7) + 1))
    total_drills_done = sum(len(v) for v in progress["completed_drills"].values())
    total_phrases = len(progress["phrase_mastery"])
    mastered_phrases = sum(1 for v in progress["phrase_mastery"].values() if v["mastered"])
    return {
        "days_in_program": days_in,
        "expected_week": expected_week,
        "current_week": progress["current_week"],
        "on_track": progress["current_week"] >= expected_week,
        "streak_days": progress["streak_days"],
        "total_drills_completed": total_drills_done,
        "total_phrases_practiced": total_phrases,
        "phrases_mastered": mastered_phrases,
        "daily_logs_count": len(progress["daily_log"]),
    }
