#!/usr/bin/env python3
"""
CORPORATE GRAVITAS TRAINING PROGRAM
====================================
A 12-week progressive training system to build executive presence,
commanding communication, and unshakable professional confidence.

Run: python3 app.py
"""

import os
import sys
import random
import textwrap

from curriculum import CURRICULUM, WEEKLY_SCHEDULE, MILESTONES
from progress import (
    load_progress, save_progress, update_streak, mark_drill_complete,
    mark_phrase_practiced, add_daily_log, calculate_overall_progress,
)
from drills import run_drill, run_all_drills_for_week


# ─────────────────────────────────────────────────────────────────────────────
# Display helpers
# ─────────────────────────────────────────────────────────────────────────────

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def wrap(text, width=76, indent="  "):
    return textwrap.fill(text, width=width, initial_indent=indent, subsequent_indent=indent)


def header(title, subtitle=""):
    clear()
    print()
    print("  ╔══════════════════════════════════════════════════════════════════════╗")
    print(f"  ║  {title:<66}  ║")
    if subtitle:
        print(f"  ║  {subtitle:<66}  ║")
    print("  ╚══════════════════════════════════════════════════════════════════════╝")
    print()


def section(title):
    print(f"\n  ── {title} {'─' * (62 - len(title))}\n")


def pause():
    input("\n  Press Enter to continue...")


# ─────────────────────────────────────────────────────────────────────────────
# Main menu
# ─────────────────────────────────────────────────────────────────────────────

def main_menu():
    progress = load_progress()
    stats = calculate_overall_progress(progress)

    header(
        "CORPORATE GRAVITAS TRAINING",
        f"Week {stats['current_week']}/12  |  Day {stats['days_in_program']}  |  Streak: {stats['streak_days']}d"
    )

    print("  Your mission: In 12 weeks, speak with the authority and composure")
    print("  of someone who has commanded boardrooms for decades.\n")

    if not stats["on_track"]:
        print("  ⚠  You're behind schedule. Expected week: "
              f"{stats['expected_week']}. Current: {stats['current_week']}.\n")

    print("  [1]  This Week's Training")
    print("  [2]  Study Concepts & Phrases")
    print("  [3]  Run Drills")
    print("  [4]  Phrase Flashcards")
    print("  [5]  Weekly Schedule & Daily Practice")
    print("  [6]  View Progress & Milestones")
    print("  [7]  Advance to Next Week")
    print("  [8]  Browse All Weeks")
    print("  [9]  Daily Reflection Journal")
    print("  [0]  Exit")
    print()

    return input("  Select: ").strip()


# ─────────────────────────────────────────────────────────────────────────────
# 1. This Week's Training
# ─────────────────────────────────────────────────────────────────────────────

def show_this_week(progress):
    week = progress["current_week"]
    data = CURRICULUM[week]

    header(f"WEEK {week}: {data['title'].upper()}", data["theme"])

    section("Core Concepts")
    for i, concept in enumerate(data["concepts"], 1):
        print(wrap(f"{i}. {concept}"))

    # Show the primary content for this week
    if "kill_phrases" in data:
        section("Kill These Phrases")
        for weak, strong in data["kill_phrases"].items():
            print(f"    ✗  \"{weak}\"")
            print(f"    ✓  \"{strong}\"")
            print()

    if "power_techniques" in data:
        section("Power Techniques")
        for name, desc in data["power_techniques"].items():
            print(f"    {name}")
            print(wrap(desc, indent="      "))
            print()

    if "frameworks" in data:
        section("Frameworks")
        for name, steps in data["frameworks"].items():
            print(f"    {name}")
            for step in steps:
                print(wrap(step, indent="      "))
            print()

    if "phrase_bank" in data:
        section("Phrase Bank (memorize these)")
        for category, phrases in data["phrase_bank"].items():
            print(f"    {category.replace('_', ' ').title()}")
            for phrase in phrases:
                print(f"      → \"{phrase}\"")
            print()

    if "power_phrases" in data:
        section("Power Phrases")
        for category, phrases in data["power_phrases"].items():
            print(f"    {category.replace('_', ' ').title()}")
            for phrase in phrases:
                print(f"      → \"{phrase}\"")
            print()

    if "templates" in data:
        section("Templates")
        for name, template in data["templates"].items():
            print(f"    {name.replace('_', ' ').title()}")
            print(wrap(f'"{template}"', indent="      "))
            print()

    if "masterclass_scenarios" in data:
        section("Masterclass Scenarios")
        for scenario in data["masterclass_scenarios"]:
            print(f"    SITUATION: {scenario['situation']}")
            for p in scenario["principles"]:
                print(f"      • {p}")
            print()

    section("Daily Practice")
    print(wrap(data["daily_practice"]))

    # Check milestones
    if week in MILESTONES:
        section(f"Milestone: {MILESTONES[week]['name']}")
        print("  By now, you should be able to:")
        for ability in MILESTONES[week]["you_should_be_able_to"]:
            print(f"    ✓ {ability}")

    pause()


# ─────────────────────────────────────────────────────────────────────────────
# 2. Study Concepts & Phrases
# ─────────────────────────────────────────────────────────────────────────────

def study_mode(progress):
    week = progress["current_week"]
    data = CURRICULUM[week]

    header(f"STUDY MODE — WEEK {week}", "Deep-dive into this week's material")

    section("Concepts — Read each one carefully, then explain it in your own words")
    for i, concept in enumerate(data["concepts"], 1):
        print(wrap(f"{i}. {concept}"))
        input("  Explain this concept in your own words, then press Enter...")
        print()

    # Collect all phrases for this week
    all_phrases = []
    for source in ["kill_phrases", "power_phrases", "phrase_bank", "power_techniques"]:
        if source in data:
            content = data[source]
            if isinstance(content, dict):
                for key, value in content.items():
                    if isinstance(value, list):
                        all_phrases.extend(value)
                    elif isinstance(value, str):
                        all_phrases.append(value)

    if all_phrases:
        section("Phrase Memorization — Say each phrase aloud 3 times")
        random.shuffle(all_phrases)
        for phrase in all_phrases[:10]:  # limit to 10 per session
            print(f'    "{phrase}"')
            input("  Say it 3 times aloud, then press Enter...")
            mark_phrase_practiced(progress, phrase)

    save_progress(progress)
    print("\n  Study session complete. Phrases have been logged.")
    pause()


# ─────────────────────────────────────────────────────────────────────────────
# 3. Run Drills
# ─────────────────────────────────────────────────────────────────────────────

def drill_menu(progress):
    week = progress["current_week"]
    data = CURRICULUM[week]
    drills = data.get("drills", [])

    header(f"DRILLS — WEEK {week}", f"{len(drills)} drill(s) available")

    completed = progress["completed_drills"].get(str(week), [])

    for i, drill in enumerate(drills):
        status = "✓" if i in completed else " "
        print(f"  [{status}] {i + 1}. {drill['type'].replace('_', ' ').title()} — {drill['instruction'][:60]}")

    print(f"\n  [A] Run all drills for this week")
    print(f"  [B] Back")

    choice = input("\n  Select drill number or option: ").strip().upper()

    if choice == "B":
        return
    elif choice == "A":
        result = run_all_drills_for_week(week)
        if result:
            for i in range(len(drills)):
                mark_drill_complete(progress, week, i)
            update_streak(progress)
            save_progress(progress)
    else:
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(drills):
                result = run_drill(week, idx)
                if result:
                    mark_drill_complete(progress, week, idx)
                    update_streak(progress)
                    save_progress(progress)
        except ValueError:
            print("  Invalid selection.")

    pause()


# ─────────────────────────────────────────────────────────────────────────────
# 4. Phrase Flashcards
# ─────────────────────────────────────────────────────────────────────────────

def flashcard_mode(progress):
    week = progress["current_week"]
    data = CURRICULUM[week]

    header("PHRASE FLASHCARDS", "Rapid-fire phrase practice")

    # Gather all replacement pairs
    cards = []
    if "kill_phrases" in data:
        for weak, strong in data["kill_phrases"].items():
            cards.append(("Replace this:", weak, strong))

    # Gather phrase bank items
    for source in ["phrase_bank", "power_phrases"]:
        if source in data:
            for category, phrases in data[source].items():
                for phrase in phrases:
                    cards.append(("Complete from memory:", category.replace("_", " ").title(), phrase))

    if not cards:
        print("  No flashcards available for this week.")
        pause()
        return

    random.shuffle(cards)
    correct = 0

    print(f"  {len(cards)} cards loaded. Let's drill.\n")

    for i, card in enumerate(cards, 1):
        if card[0] == "Replace this:":
            print(f"  [{i}/{len(cards)}] WEAK: \"{card[1]}\"")
            input("  Say the power version aloud, then press Enter...")
            print(f'  ANSWER: "{card[2]}"')
        else:
            print(f"  [{i}/{len(cards)}] Category: {card[1]}")
            print(f"  Can you recall a power phrase for this?")
            input("  Say it aloud, then press Enter...")
            print(f'  ONE OPTION: "{card[2]}"')

        got_it = input("  Got it right? (y/n): ").strip().lower()
        if got_it == "y":
            correct += 1
            mark_phrase_practiced(progress, card[2] if len(card) > 2 else card[1])
        print()

    pct = (correct / len(cards)) * 100 if cards else 0
    print(f"\n  RESULTS: {correct}/{len(cards)} ({pct:.0f}%)")

    if pct >= 90:
        print("  Excellent. These phrases are becoming reflexive.")
    elif pct >= 70:
        print("  Good progress. Keep drilling daily.")
    else:
        print("  These need more repetition. Run flashcards again tomorrow.")

    update_streak(progress)
    save_progress(progress)
    pause()


# ─────────────────────────────────────────────────────────────────────────────
# 5. Weekly Schedule
# ─────────────────────────────────────────────────────────────────────────────

def show_schedule(progress):
    week = progress["current_week"]
    data = CURRICULUM[week]

    header("WEEKLY TRAINING SCHEDULE", f"Week {week}: {data['title']}")

    for day, info in WEEKLY_SCHEDULE.items():
        print(f"  {day.upper():12s}  {info['time']:>8s}  │  {info['focus']}")
        print(f"  {'':12s}  {'':>8s}  │  {info['activity']}")
        print()

    section("Today's Daily Practice")
    print(wrap(data["daily_practice"]))

    pause()


# ─────────────────────────────────────────────────────────────────────────────
# 6. Progress & Milestones
# ─────────────────────────────────────────────────────────────────────────────

def show_progress(progress):
    stats = calculate_overall_progress(progress)

    header("YOUR PROGRESS", "Track your transformation")

    print(f"  Program Day:           {stats['days_in_program']}")
    print(f"  Current Week:          {stats['current_week']}/12")
    print(f"  Expected Week:         {stats['expected_week']}")
    print(f"  On Track:              {'Yes' if stats['on_track'] else 'No — step it up'}")
    print(f"  Practice Streak:       {stats['streak_days']} day(s)")
    print(f"  Drills Completed:      {stats['total_drills_completed']}")
    print(f"  Phrases Practiced:     {stats['total_phrases_practiced']}")
    print(f"  Phrases Mastered:      {stats['phrases_mastered']}")
    print(f"  Journal Entries:       {stats['daily_logs_count']}")

    # Phase progress
    section("Phase Progress")
    phases = [
        (1, 3, "Foundation", "Eliminate weakness, build vocal authority, structure speech"),
        (4, 6, "Executive Communication", "Command rooms, speak strategically, summarize like a leader"),
        (7, 9, "Persuasion & Influence", "Disagree elegantly, influence without authority, handle pushback"),
        (10, 12, "Advanced Presence", "Storytelling, political intelligence, composure under fire"),
    ]
    for start, end, name, desc in phases:
        current = stats["current_week"]
        if current > end:
            status = "COMPLETE"
        elif current >= start:
            status = f"IN PROGRESS ({current - start + 1}/{end - start + 1} weeks)"
        else:
            status = "LOCKED"
        print(f"  Weeks {start}-{end}: {name}")
        print(f"    {desc}")
        print(f"    Status: {status}")
        print()

    # Milestone checks
    section("Milestones")
    for week_num, milestone in MILESTONES.items():
        reached = stats["current_week"] >= week_num
        marker = "■" if reached else "□"
        print(f"  {marker} Week {week_num}: {milestone['name']}")
        if reached:
            for ability in milestone["you_should_be_able_to"]:
                print(f"      ✓ {ability}")
        print()

    pause()


# ─────────────────────────────────────────────────────────────────────────────
# 7. Advance Week
# ─────────────────────────────────────────────────────────────────────────────

def advance_week(progress):
    current = progress["current_week"]
    if current >= 12:
        header("PROGRAM COMPLETE", "You've completed all 12 weeks")

        if "final_assessment" in CURRICULUM[12]:
            section("Final Assessment: The Gravitas Gauntlet")
            print(wrap(CURRICULUM[12]["final_assessment"]["description"]))
            print()
            for i, challenge in enumerate(CURRICULUM[12]["final_assessment"]["challenges"], 1):
                print(f"    {i}. {challenge}")

        pause()
        return

    # Check readiness
    drills_done = progress["completed_drills"].get(str(current), [])
    total_drills = len(CURRICULUM[current].get("drills", []))

    header(f"ADVANCE FROM WEEK {current} TO WEEK {current + 1}")

    if len(drills_done) < total_drills:
        print(f"  Warning: You've completed {len(drills_done)}/{total_drills} drills this week.")
        print("  It's recommended to complete all drills before advancing.\n")

    if current in MILESTONES:
        section(f"Milestone Check: {MILESTONES[current]['name']}")
        print("  Can you honestly do all of these?")
        for ability in MILESTONES[current]["you_should_be_able_to"]:
            print(f"    • {ability}")
        print()

    confirm = input("  Advance to next week? (y/n): ").strip().lower()
    if confirm == "y":
        progress["current_week"] = current + 1
        save_progress(progress)
        print(f"\n  Advanced to Week {current + 1}: {CURRICULUM[current + 1]['title']}")
        print(f"  Theme: {CURRICULUM[current + 1]['theme']}")
    else:
        print("  Stay on this week. Master the material before moving on.")

    pause()


# ─────────────────────────────────────────────────────────────────────────────
# 8. Browse All Weeks
# ─────────────────────────────────────────────────────────────────────────────

def browse_weeks(progress):
    header("ALL 12 WEEKS", "Your complete transformation roadmap")

    current = progress["current_week"]
    for week_num, data in CURRICULUM.items():
        marker = "→" if week_num == current else " "
        lock = "" if week_num <= current else " [LOCKED]"
        phase = ""
        if week_num <= 3:
            phase = "Phase 1: Foundation"
        elif week_num <= 6:
            phase = "Phase 2: Executive Communication"
        elif week_num <= 9:
            phase = "Phase 3: Persuasion & Influence"
        else:
            phase = "Phase 4: Advanced Presence"

        if week_num in [1, 4, 7, 10]:
            print(f"\n  ── {phase} {'─' * (60 - len(phase))}")

        drills_done = len(progress["completed_drills"].get(str(week_num), []))
        total_drills = len(data.get("drills", []))

        print(f"  {marker} Week {week_num:2d}: {data['title']:<45} [{drills_done}/{total_drills} drills]{lock}")

    print()
    choice = input("  Enter week number to view (or Enter to go back): ").strip()
    if choice:
        try:
            week_num = int(choice)
            if 1 <= week_num <= 12:
                if week_num <= current:
                    # Temporarily show that week
                    old_week = progress["current_week"]
                    progress["current_week"] = week_num
                    show_this_week(progress)
                    progress["current_week"] = old_week
                else:
                    print(f"  Week {week_num} is locked. Advance to unlock it.")
                    pause()
        except ValueError:
            pass


# ─────────────────────────────────────────────────────────────────────────────
# 9. Daily Reflection
# ─────────────────────────────────────────────────────────────────────────────

def daily_reflection(progress):
    week = progress["current_week"]
    header("DAILY REFLECTION", f"Week {week} — Build self-awareness")

    print("  Answer honestly. This journal tracks your growth over 12 weeks.\n")

    print("  1. What technique did you practice today?")
    technique = input("     > ")

    print("\n  2. Describe a moment where you applied (or missed applying) a skill:")
    moment = input("     > ")

    print("\n  3. What will you do differently tomorrow?")
    tomorrow = input("     > ")

    print("\n  4. Rate today's gravitas on a scale of 1-10:")
    rating = input("     > ").strip()
    try:
        rating = max(1, min(10, int(rating)))
    except ValueError:
        rating = 5

    notes = f"Technique: {technique} | Moment: {moment} | Tomorrow: {tomorrow}"
    add_daily_log(progress, week, notes, rating)
    update_streak(progress)
    save_progress(progress)

    print(f"\n  Logged. Self-rating: {rating}/10")

    # Show trend if we have enough data
    logs = progress["daily_log"]
    if len(logs) >= 3:
        recent = [l["self_rating"] for l in logs[-7:]]
        avg = sum(recent) / len(recent)
        trend = "↑" if len(recent) > 1 and recent[-1] > recent[0] else "→" if len(recent) > 1 and recent[-1] == recent[0] else "↓"
        print(f"  7-day average: {avg:.1f}/10  Trend: {trend}")

    pause()


# ─────────────────────────────────────────────────────────────────────────────
# Main loop
# ─────────────────────────────────────────────────────────────────────────────

def main():
    # First run welcome
    progress = load_progress()
    if progress["current_week"] == 1 and not progress["daily_log"]:
        header("WELCOME TO CORPORATE GRAVITAS TRAINING")
        print("  Over the next 12 weeks, you will systematically build the ability")
        print("  to command any room, speak with authority, and project the kind")
        print("  of executive presence that makes people listen.\n")
        print("  This is not about being loud. It's about being undeniable.\n")
        print("  The program is structured in 4 phases:")
        print("    Weeks  1-3:  Foundation — eliminate weakness signals")
        print("    Weeks  4-6:  Executive Communication — speak like a leader")
        print("    Weeks  7-9:  Persuasion & Influence — win without fighting")
        print("    Weeks 10-12: Advanced Presence — grace under fire\n")
        print("  Commit to daily practice. The phrases must become reflexive.")
        print("  The delivery must become second nature.\n")
        print("  Let's begin.\n")
        save_progress(progress)
        pause()

    while True:
        choice = main_menu()
        progress = load_progress()

        if choice == "1":
            show_this_week(progress)
        elif choice == "2":
            study_mode(progress)
        elif choice == "3":
            drill_menu(progress)
        elif choice == "4":
            flashcard_mode(progress)
        elif choice == "5":
            show_schedule(progress)
        elif choice == "6":
            show_progress(progress)
        elif choice == "7":
            advance_week(progress)
        elif choice == "8":
            browse_weeks(progress)
        elif choice == "9":
            daily_reflection(progress)
        elif choice == "0":
            header("", "\"Speak less. Mean more. Command the room.\"")
            print("  See you tomorrow. Consistency builds gravitas.\n")
            sys.exit(0)
        else:
            pass


if __name__ == "__main__":
    main()
