#!/usr/bin/env python3
"""
Quick Reference Card — Print the most critical phrases by category.
Use this as a daily cheat sheet until they're reflexive.

Run: python3 quick_reference.py
"""

CARDS = {
    "REPLACING WEAK LANGUAGE": {
        "I think maybe...": "My recommendation is...",
        "Sorry, but...": "I want to flag something.",
        "I'm not sure, but...": "My understanding is...",
        "Does that make sense?": "Let me know if you'd like me to elaborate.",
        "I feel like...": "My assessment is...",
        "Just a thought...": "Here's what I'd recommend.",
        "I could be wrong...": "The evidence suggests...",
        "Hopefully that helps?": "That should address it.",
    },
    "COMMANDING A MEETING": {
        "Setting direction": "Let's get aligned on three things today.",
        "Taking control": "I want to frame the discussion before we dive in.",
        "Redirecting": "Let's bring this back to the central question.",
        "Handling interruptions": "Let me finish this thought.",
        "Closing": "Let me summarize where we've landed.",
    },
    "DISAGREEING WITH POWER": {
        "Acknowledge first": "I see the logic in that, and I'd offer an additional consideration.",
        "Challenge assumptions": "Let me pressure-test that assumption.",
        "Stand firm": "I've considered that. My conviction hasn't changed. Here's why.",
        "Find common ground": "We agree on the destination. The question is the route.",
    },
    "HANDLING TOUGH QUESTIONS": {
        "Bridging": "That's important, and it connects to a broader point...",
        "Buying time": "Let me give you a precise answer rather than an approximation.",
        "Loaded questions": "I'd challenge the premise of that question.",
        "Admitting gaps": "I don't have that figure at hand. I'll have it by EOD.",
    },
    "STRATEGIC FRAMING": {
        "Elevating": "The real question isn't [detail] — it's [strategic impact].",
        "Business acumen": "What's the revenue impact of that decision?",
        "Thinking ahead": "The second-order effect of this is...",
        "Taking ownership": "I'll own this and have an update by Friday.",
    },
    "CRISIS & COMPOSURE": {
        "Transparency": "Here's what we know. Here's what we don't. Here's what we're doing.",
        "Composure": "Let's take a step back and look at this clearly.",
        "Difficult messages": "I'm going to be direct because you deserve clarity.",
        "Recovery": "I own this. Here's my plan to make it right.",
    },
    "FRAMEWORKS": {
        "BLUF": "Conclusion first → 2-3 supporting points → implication",
        "Rule of Three": "Organize any argument into exactly 3 points",
        "Power Triangle": "Point (position) → Proof (evidence) → Punch (call to action)",
        "Story Arc": "Current state → Tension → Turning point → Result → Lesson",
        "Contrast Frame": "'Without this...' → 'With this...' → 'The choice is clear.'",
    },
}


def print_reference():
    print()
    print("  ╔══════════════════════════════════════════════════════════════════════╗")
    print("  ║              CORPORATE GRAVITAS — QUICK REFERENCE                   ║")
    print("  ╚══════════════════════════════════════════════════════════════════════╝")

    for category, items in CARDS.items():
        print(f"\n  ── {category} {'─' * (62 - len(category))}\n")
        for key, value in items.items():
            print(f"    {key:<30s} →  {value}")

    print("\n  ── DAILY REMINDERS ──────────────────────────────────────────────────\n")
    print("    1. Lead with the conclusion. Never bury the lead.")
    print("    2. Pause after key points. Silence is power.")
    print("    3. Downward inflection on every statement.")
    print("    4. Eliminate filler: um, like, you know, sort of.")
    print("    5. Active voice: 'I decided' not 'It was decided.'")
    print("    6. Three points. Always three.")
    print("    7. Frame for THEIR benefit, not yours.")
    print("    8. When you don't know, say so with authority.")
    print("    9. Your calm IS the message under pressure.")
    print("   10. Speak less. Mean more.\n")


if __name__ == "__main__":
    print_reference()
