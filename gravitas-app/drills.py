"""
Interactive drill engine for the Gravitas Training Program.
Runs drills from the curriculum and tracks completion.
"""

import random
import textwrap
from curriculum import CURRICULUM


def wrap(text, width=78, indent="  "):
    return textwrap.fill(text, width=width, initial_indent=indent, subsequent_indent=indent)


def run_replacement_drill(drill):
    """Drill: replace weak phrases with powerful alternatives."""
    print(f"\n  DRILL: {drill['instruction']}")
    print("  " + "=" * 60)
    items = list(drill["items"])
    random.shuffle(items)
    score = 0

    for i, (weak, strong) in enumerate(items, 1):
        print(f"\n  [{i}/{len(items)}] Weak statement:")
        print(wrap(f'"{weak}"'))
        input("\n  Press Enter when you've formulated your response...")
        print(f"\n  POWER VERSION:")
        print(wrap(f'"{strong}"'))
        rating = input("\n  How close was yours? (1=not close, 2=similar idea, 3=nailed it): ").strip()
        if rating == "3":
            score += 1
        elif rating == "2":
            score += 0.5

    pct = (score / len(items)) * 100
    print(f"\n  Score: {score}/{len(items)} ({pct:.0f}%)")
    return score, len(items)


def run_spot_the_weakness_drill(drill):
    """Drill: identify all weak signals in a statement."""
    print(f"\n  DRILL: {drill['instruction']}")
    print("  " + "=" * 60)
    score = 0

    for i, (statement, weaknesses) in enumerate(drill["items"], 1):
        print(f"\n  [{i}/{len(drill['items'])}] Find every weak signal:")
        print(wrap(f'"{statement}"'))
        input("\n  Write down all weak signals, then press Enter to see the answer...")
        print(f"\n  WEAK SIGNALS FOUND ({len(weaknesses)}):")
        for w in weaknesses:
            print(f"    - {w}")
        found = input(f"\n  How many did you identify? (0-{len(weaknesses)}): ").strip()
        try:
            score += int(found)
        except ValueError:
            pass

    total = sum(len(w) for _, w in drill["items"])
    pct = (score / total) * 100 if total > 0 else 0
    print(f"\n  Score: {score}/{total} weak signals identified ({pct:.0f}%)")
    return score, total


def run_delivery_drill(drill):
    """Drill: practice delivering statements with proper technique."""
    print(f"\n  DRILL: {drill['instruction']}")
    print("  " + "=" * 60)

    for i, statement in enumerate(drill["items"], 1):
        print(f"\n  [{i}/{len(drill['items'])}] Deliver this statement aloud:")
        print(wrap(f'"{statement}"'))
        print("\n  Checklist:")
        print("    [ ] Downward inflection at the end")
        print("    [ ] 2-3 second pause after")
        print("    [ ] Zero filler words")
        print("    [ ] Steady, controlled pace")
        input("  Press Enter after delivering it...")

    print("\n  Good. Repeat this drill until delivery feels automatic.")
    return len(drill["items"]), len(drill["items"])


def run_pause_drill(drill):
    """Drill: practice strategic pauses."""
    print(f"\n  DRILL: {drill['instruction']}")
    print("  " + "=" * 60)

    for i, (before, pause_seconds, after) in enumerate(drill["items"], 1):
        print(f"\n  [{i}/{len(drill['items'])}]")
        print(wrap(f'Say: "{before}"'))
        print(f"\n  >>> HOLD SILENCE FOR {pause_seconds} SECONDS <<<")
        print(wrap(f'Then say: "{after}"'))
        input("  Press Enter after completing this...")

    print("\n  The pause is your power move. Master it.")
    return len(drill["items"]), len(drill["items"])


def run_restructure_drill(drill):
    """Drill: restructure rambling statements into BLUF format."""
    print(f"\n  DRILL: {drill['instruction']}")
    print("  " + "=" * 60)
    score = 0

    for i, item in enumerate(drill["items"], 1):
        if isinstance(item, tuple):
            rambling, structured = item
            print(f"\n  [{i}/{len(drill['items'])}] Restructure this:")
            print(wrap(f'"{rambling}"'))
            input("\n  Formulate your BLUF version, then press Enter...")
            print(f"\n  POWER VERSION:")
            print(wrap(f'"{structured}"'))
        else:
            print(f"\n  [{i}/{len(drill['items'])}] Argue this position using exactly 3 points:")
            print(wrap(f'"{item}"'))
            input("\n  Formulate your three-beat argument, then press Enter to continue...")
            print("  Check: Did you have exactly 3 clear, distinct supporting points?")

        rating = input("  Rate yourself (1-3): ").strip()
        if rating == "3":
            score += 1
        elif rating == "2":
            score += 0.5

    print(f"\n  Score: {score}/{len(drill['items'])}")
    return score, len(drill["items"])


def run_scenario_drill(drill):
    """Drill: respond to situational scenarios."""
    print(f"\n  DRILL: {drill['instruction']}")
    print("  " + "=" * 60)

    for i, item in enumerate(drill["items"], 1):
        print(f"\n  [{i}/{len(drill['items'])}]")
        print(f"  SITUATION: {item['situation']}")
        print(f"  YOUR GOAL: {item['goal']}")
        response = input("\n  Your response (type it out): ")
        if response.strip():
            print("  Good. Now say it aloud with conviction.")
        input("  Press Enter to continue...")

    return len(drill["items"]), len(drill["items"])


def run_elevate_drill(drill):
    """Drill: transform tactical statements into strategic ones."""
    print(f"\n  DRILL: {drill['instruction']}")
    print("  " + "=" * 60)
    score = 0

    for i, (tactical, strategic) in enumerate(drill["items"], 1):
        print(f"\n  [{i}/{len(drill['items'])}] Elevate this tactical statement:")
        print(wrap(f'"{tactical}"'))
        input("\n  Formulate your strategic version, then press Enter...")
        print(f"\n  STRATEGIC VERSION:")
        print(wrap(f'"{strategic}"'))
        rating = input("  Rate yourself (1-3): ").strip()
        if rating == "3":
            score += 1
        elif rating == "2":
            score += 0.5

    print(f"\n  Score: {score}/{len(drill['items'])}")
    return score, len(drill["items"])


def run_compress_drill(drill):
    """Drill: compress verbose updates into executive summaries."""
    print(f"\n  DRILL: {drill['instruction']}")
    print("  " + "=" * 60)

    for i, item in enumerate(drill["items"], 1):
        if isinstance(item, tuple):
            verbose, compressed = item
            print(f"\n  [{i}] Compress this into 30 seconds:")
            print(wrap(f'"{verbose}"'))
            input("\n  Write your executive summary, then press Enter...")
            print(f"\n  TARGET VERSION:")
            print(wrap(f'"{compressed}"'))
        else:
            print(f"\n  [{i}] Time yourself — deliver in under 30 seconds:")
            print(wrap(f'"{item}"'))
            input("  Press Enter when done...")

    return len(drill["items"]), len(drill["items"])


def run_reframe_drill(drill):
    """Drill: rewrite aggressive disagreements diplomatically."""
    print(f"\n  DRILL: {drill['instruction']}")
    print("  " + "=" * 60)
    score = 0

    for i, item in enumerate(drill["items"], 1):
        if isinstance(item, tuple):
            aggressive, diplomatic = item
            print(f"\n  [{i}/{len(drill['items'])}] Reframe this:")
            print(wrap(f'"{aggressive}"'))
            input("\n  Write your diplomatic version, then press Enter...")
            print(f"\n  DIPLOMATIC POWER VERSION:")
            print(wrap(f'"{diplomatic}"'))
            rating = input("  Rate yourself (1-3): ").strip()
            if rating == "3":
                score += 1
            elif rating == "2":
                score += 0.5

    print(f"\n  Score: {score}/{len(drill['items'])}")
    return score, len(drill["items"])


def run_rapid_fire_drill(drill):
    """Drill: rapid-fire responses under time pressure."""
    print(f"\n  DRILL: {drill['instruction']}")
    print("  " + "=" * 60)
    print("  This is a speed drill. Respond IMMEDIATELY to each prompt.\n")

    for i, item in enumerate(drill["items"], 1):
        if isinstance(item, tuple):
            question, answer = item
            print(f"  [{i}] {question}")
            input("  Your response: ")
            print(f"  MODEL RESPONSE:")
            print(wrap(f'"{answer}"'))
        else:
            print(f"  [{i}] {item}")
            input("  GO: ")
        print()

    print("  Speed builds reflexes. Repeat until responses are automatic.")
    return len(drill["items"]), len(drill["items"])


def run_reframe_audience_drill(drill):
    """Drill: reframe proposals for different audiences."""
    print(f"\n  DRILL: {drill['instruction']}")
    print("  " + "=" * 60)

    for item in drill["items"]:
        print(f"\n  PROPOSAL: {item['proposal']}")
        print()
        for audience, framing in item["audiences"].items():
            print(f"  For the {audience}:")
            input(f"  How would you frame this? (Type your version, then Enter): ")
            print(f"  MODEL VERSION:")
            print(wrap(f'"{framing}"'))
            print()

    return len(drill["items"]), len(drill["items"])


def run_story_build_drill(drill):
    """Drill: build business stories using frameworks."""
    print(f"\n  DRILL: {drill['instruction']}")
    print("  " + "=" * 60)

    for i, prompt in enumerate(drill["items"], 1):
        print(f"\n  [{i}] Build a 60-second story:")
        print(wrap(f'"{prompt}"'))
        print("\n  Structure:")
        print("    1. Current state (setup)")
        print("    2. Tension (conflict)")
        print("    3. Turning point (resolution)")
        print("    4. Result (outcome)")
        print("    5. Lesson (takeaway)")
        input("\n  Deliver it aloud, then press Enter...")

    return len(drill["items"]), len(drill["items"])


# Map drill types to runner functions
DRILL_RUNNERS = {
    "replacement": run_replacement_drill,
    "spot_the_weakness": run_spot_the_weakness_drill,
    "delivery": run_delivery_drill,
    "pause_drill": run_pause_drill,
    "restructure": run_restructure_drill,
    "three_beat": run_restructure_drill,
    "scenario": run_scenario_drill,
    "elevate": run_elevate_drill,
    "compress": run_compress_drill,
    "timed_delivery": run_compress_drill,
    "reframe": run_reframe_drill,
    "reframe_hostile": run_rapid_fire_drill,
    "rapid_fire": run_rapid_fire_drill,
    "reframe_for_audience": run_reframe_audience_drill,
    "socratic_path": run_story_build_drill,
    "story_build": run_story_build_drill,
    "analogy_creation": run_story_build_drill,
    "composure_challenge": run_delivery_drill,
}


def run_drill(week, drill_index):
    """Run a specific drill from a given week."""
    week_data = CURRICULUM.get(week)
    if not week_data:
        print(f"  Week {week} not found.")
        return None

    drills = week_data.get("drills", [])
    if drill_index >= len(drills):
        print(f"  Drill {drill_index + 1} not found for week {week}.")
        return None

    drill = drills[drill_index]
    runner = DRILL_RUNNERS.get(drill["type"])
    if not runner:
        print(f"  Unknown drill type: {drill['type']}")
        return None

    return runner(drill)


def run_all_drills_for_week(week):
    """Run all drills for a given week."""
    week_data = CURRICULUM.get(week)
    if not week_data:
        print(f"  Week {week} not found.")
        return

    drills = week_data.get("drills", [])
    total_score = 0
    total_possible = 0

    for i, drill in enumerate(drills):
        result = run_drill(week, i)
        if result:
            score, possible = result
            total_score += score
            total_possible += possible

    if total_possible > 0:
        pct = (total_score / total_possible) * 100
        print(f"\n  WEEK {week} DRILL RESULTS: {total_score}/{total_possible} ({pct:.0f}%)")

    return total_score, total_possible
