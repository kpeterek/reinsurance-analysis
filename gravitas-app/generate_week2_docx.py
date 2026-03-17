#!/usr/bin/env python3
"""Generate Week 2 Study Guide as a Word document."""

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

doc = Document()

style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)
style.paragraph_format.space_after = Pt(6)

style_h1 = doc.styles["Heading 1"]
style_h1.font.color.rgb = RGBColor(0x1A, 0x1A, 0x2E)
style_h1.font.size = Pt(22)

style_h2 = doc.styles["Heading 2"]
style_h2.font.color.rgb = RGBColor(0x2C, 0x3E, 0x50)
style_h2.font.size = Pt(16)

style_h3 = doc.styles["Heading 3"]
style_h3.font.color.rgb = RGBColor(0x34, 0x49, 0x5E)
style_h3.font.size = Pt(13)


def bold(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    return p

def italic(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.italic = True
    return p

def example(before, after):
    p = doc.add_paragraph()
    r = p.add_run("BEFORE: ")
    r.bold = True
    r.font.color.rgb = RGBColor(0xC0, 0x39, 0x2B)
    p.add_run(f'"{before}"')
    p2 = doc.add_paragraph()
    r2 = p2.add_run("AFTER:  ")
    r2.bold = True
    r2.font.color.rgb = RGBColor(0x27, 0xAE, 0x60)
    p2.add_run(f'"{after}"')
    doc.add_paragraph()

def table(headers, rows):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.style = "Light Grid Accent 1"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]
        c.text = h
        for p in c.paragraphs:
            for r in p.runs:
                r.bold = True
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            t.rows[ri + 1].cells[ci].text = val
    doc.add_paragraph()

def bullet(text):
    doc.add_paragraph(text, style="List Bullet")

def quote_block(text):
    p = doc.add_paragraph()
    p.style = doc.styles["Normal"]
    r = p.add_run(text)
    r.italic = True
    r.font.color.rgb = RGBColor(0x2C, 0x3E, 0x50)
    p.paragraph_format.left_indent = Pt(36)

# ═══════════════════════════════════════════════════════════════════════════
# TITLE PAGE
# ═══════════════════════════════════════════════════════════════════════════
for _ in range(6):
    doc.add_paragraph()

title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run("CORPORATE GRAVITAS\nTRAINING PROGRAM")
run.font.size = Pt(32)
run.bold = True
run.font.color.rgb = RGBColor(0x1A, 0x1A, 0x2E)

doc.add_paragraph()
subtitle = doc.add_paragraph()
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = subtitle.add_run("WEEK 2: VOCAL AUTHORITY & PHYSICAL PRESENCE")
run.font.size = Pt(18)
run.font.color.rgb = RGBColor(0x2C, 0x3E, 0x50)

doc.add_paragraph()
phase = doc.add_paragraph()
phase.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = phase.add_run("Phase 1: Foundation")
run.font.size = Pt(14)
run.italic = True

doc.add_paragraph()
theme = doc.add_paragraph()
theme.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = theme.add_run('"Your body and voice speak before your words do"')
run.font.size = Pt(12)
run.italic = True
run.font.color.rgb = RGBColor(0x7F, 0x8C, 0x8D)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# WHY THIS WEEK MATTERS
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading("WHY THIS WEEK MATTERS", level=1)

doc.add_paragraph(
    "Last week you stopped undermining yourself with weak language. Now you build "
    "the instrument that delivers your words: your voice and your body."
)
doc.add_paragraph(
    "Here's a fact that should change how you think about communication forever: "
    "research consistently shows that 55% of how you're perceived comes from body "
    "language, 38% from vocal tone, and only 7% from the actual words you say "
    "(Mehrabian, 1971). You can have the most brilliant insight in the room — but "
    "if you deliver it with a shaky voice, shifting feet, and darting eyes, the "
    "room hears \"uncertain.\""
)
bold(
    "This week is about building the physical and vocal chassis of authority. When "
    "you walk into a room, people should feel your presence before you open your "
    "mouth. When you speak, the WAY you speak should make people lean in."
)
doc.add_paragraph(
    "This isn't about being loud. It's about being deliberate, grounded, and "
    "impossible to ignore."
)

# ═══════════════════════════════════════════════════════════════════════════
# PART 1: THE VOICE OF AUTHORITY
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading("PART 1: THE VOICE OF AUTHORITY", level=1)
doc.add_paragraph("Your voice is an instrument. Most people have never tuned it.")

# 1.1 Vocal Register
doc.add_heading("1.1 Vocal Register — Go Lower", level=2)
doc.add_paragraph(
    "The science: Studies from McMaster University found that candidates with "
    "lower-pitched voices are perceived as stronger, more competent, and more "
    "trustworthy leaders. Both men and women benefit from a slightly lower "
    "register — not unnaturally deep, but consciously anchored."
)
doc.add_paragraph(
    "What's happening now: When you're nervous or excited, your vocal cords "
    "tighten and your pitch rises. This is a biological stress response — the "
    "same reason your voice cracks when you're anxious. Higher pitch signals "
    "submission in virtually every primate species, including humans."
)
bold("How to lower your register:")
bullet("Morning warm-up: Hum at the lowest comfortable pitch for 30 seconds each morning. This relaxes your vocal cords and sets your baseline.")
bullet("Breathe from the diaphragm: Shallow chest breathing produces a thin, higher voice. Deep belly breathing gives you resonance and power. Place your hand on your stomach — it should expand when you breathe in.")
bullet("Speak from the chest, not the throat: Imagine the sound originating from behind your sternum, not from your neck. This produces a richer, more resonant tone.")
bullet("Before important moments: Take three slow, deep breaths. This physically lowers your pitch by relaxing the muscles around your larynx.")

doc.add_paragraph(
    "The target: Not a fake baritone. A relaxed, resonant, grounded version of your "
    "natural voice. Record yourself after 5 minutes of humming and diaphragmatic "
    "breathing — you'll hear the difference."
)

# 1.2 Pace
doc.add_heading("1.2 Pace — Slow Down", level=2)
bold("The principle: Powerful people are never in a rush to speak. Speed communicates anxiety. Deliberate pace communicates control.")

bold("The numbers:")
bullet("Anxious/low-status speech: 170-200+ words per minute")
bullet("Conversational speech: 150-170 words per minute")
bullet("Authoritative speech: 130-150 words per minute")
bullet("High-impact moments: 100-120 words per minute")

doc.add_paragraph(
    "Why we rush: You rush because you subconsciously fear the room will stop "
    "listening. You feel you need to \"get it all out\" before someone interrupts "
    "or loses interest. This is a low-status instinct. High-status speakers assume "
    "the room will wait. And it does."
)

bold("How to slow down:")
bullet("The mental trick: Pretend every sentence costs you $100. You'd choose your words more carefully and deliver them more slowly.")
bullet("The physical trick: Between sentences, take a full breath. Not a quick gasp — a real, complete inhale. This automatically creates pace.")
bullet("Practice with a timer: Read a 150-word paragraph in exactly 60 seconds. This is 150 wpm — it will feel painfully slow at first. That's the point.")

bold("Practice paragraph (150 words) — read in exactly 60 seconds:")
quote_block(
    "The proposal we're reviewing today represents a significant shift in our "
    "approach to market expansion. Over the past quarter, our team has analyzed "
    "three potential entry strategies, each with distinct risk profiles and "
    "resource requirements. The data consistently points toward a phased "
    "approach, beginning with the Southeast region where our existing "
    "relationships provide a natural advantage. This isn't a conservative play "
    "— it's a calculated one. The companies that succeed in new markets are "
    "rarely the first movers. They're the ones who enter with precision, learn "
    "fast, and scale deliberately. I'm recommending we commit to the phased "
    "approach with a six-month evaluation window. The investment is modest, the "
    "downside is contained, and the upside — if the Southeast market validates "
    "our thesis — positions us for national expansion in eighteen months."
)

# 1.3 Silence
doc.add_heading("1.3 The Power of Silence", level=2)
bold("The rule: After you make a key point, STOP TALKING.")
doc.add_paragraph(
    "Most people fill silence with noise because silence feels uncomfortable. But "
    "silence after a statement is the verbal equivalent of a bold, underlined "
    "headline. It says: \"What I just said is important enough to sit with.\""
)
bold("Why silence works:")
bullet("It gives the room time to process your point")
bullet("It demonstrates that YOU believe what you said is significant")
bullet("It signals confidence — you don't need to keep talking to justify yourself")
bullet("It creates contrast — the silence makes the next thing you say hit harder")

bold("The three types of strategic silence:")

bold("The Landing Pause (2-3 seconds): After stating a conclusion or recommendation.")
quote_block('"We need to change direction on this." [2 seconds of silence] "Here\'s why."')

bold("The Weight Pause (3-5 seconds): After delivering a significant or surprising point.")
quote_block('"Our largest client is considering terminating the contract." [4 seconds] "I have a plan to prevent that."')

bold("The Dominance Pause (2 seconds before speaking): When asked a question, don't answer immediately.")
quote_block('"Why did the project miss its deadline?" [2-second pause] "There were two primary factors. Let me walk through both."')

doc.add_paragraph(
    "The discomfort is the point. If the pause feels uncomfortably long to you, "
    "it's the right length. Your internal clock overestimates silence when you're "
    "the speaker."
)

# 1.4 Downward Inflection
doc.add_heading("1.4 Downward Inflection — The Sound of Certainty", level=2)
doc.add_paragraph(
    "Every declarative statement should end with your pitch going DOWN. This is "
    "the single most important vocal technique for projecting authority."
)

example(
    "We should move forward with this plan? (rising pitch — asks permission)",
    "We should move forward with this plan. (falling pitch — declares)"
)

bold("How to practice:")
bullet("Pick any sentence. Say it while moving your hand DOWNWARD on the last two words. Your voice will follow your hand.")
bullet("Record yourself reading five sentences. Listen for the pitch on the final word. If it rises, re-record.")
bullet("Think of a period as a vocal cliff. Your pitch steps off the edge and drops.")

bold("Practice sentences — say each with deliberate downward inflection:")
for i, s in enumerate([
    "The numbers support this direction.",
    "I've considered the alternatives.",
    "This is my recommendation.",
    "We don't have room for another delay.",
    "The decision is clear.",
    "I take full responsibility for this outcome.",
    "Here's what we're going to do.",
    "The current approach is not working.",
], 1):
    doc.add_paragraph(f"{i}. \"{s}\"", style="List Number")

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# PART 2: THE BODY OF AUTHORITY
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading("PART 2: THE BODY OF AUTHORITY", level=1)
doc.add_paragraph(
    "Your body broadcasts your internal state before you speak a single word. "
    "A person with authoritative body language is perceived as a leader within "
    "seconds of entering a room."
)

doc.add_heading("2.1 Posture — Occupy Space", level=2)
bold("The power posture:")
bullet("Shoulders: Back and down. Not puffed up — just naturally pulled back, opening your chest.")
bullet("Chin: Level with the ground. Not tilted up (arrogant) or down (submissive). Parallel to the floor.")
bullet("Spine: Imagine a string pulling the crown of your head toward the ceiling. Elongate.")
bullet("Feet: Shoulder-width apart when standing. Planted. No crossing, no shifting weight.")
bullet("Arms: At your sides or in controlled gestures. Never crossed, never in pockets.")

bold("What NOT to do:")
bullet("Cross your arms (defensive barrier)")
bullet("Touch your face, neck, or hair (self-soothing = anxiety)")
bullet("Lean against walls or furniture (lack of core confidence)")
bullet("Stand with feet together or crossed (unstable, submissive)")
bullet("Rock or sway (nervous energy with no outlet)")
bullet("Shrink into your chair (minimize yourself = minimize your authority)")

bold("Seated power posture:")
bullet("Sit back in the chair with your full back supported")
bullet("Both feet flat on the floor")
bullet("Hands on the table or armrests — visible")
bullet("Lean forward slightly when making a point (engagement)")
bullet("Lean back slightly when listening (composure, evaluation)")

doc.add_heading("2.2 Eye Contact — Hold It", level=2)
bold("The rule: 3-5 seconds of direct eye contact per person. Breaking eye contact downward signals submission.")

bold("How to build eye contact strength:")
bullet("The triangle technique: If direct eye contact feels too intense, look at the triangle formed by the other person's eyes and the bridge of their nose. They can't tell the difference.")
bullet("In meetings: When you speak, address one person per sentence. Hold eye contact for the full sentence, then move to the next person.")
bullet("When listening: Maintain eye contact with the speaker about 70% of the time.")
bullet("When being challenged: Do NOT look away. Looking down when someone pushes back is a submission signal. Hold eye contact, pause, then respond.")

doc.add_heading("2.3 Hand Gestures — Controlled and Open", level=2)
bold("Power gestures:")
bullet("Open palms facing up: \"I'm being transparent\"")
bullet("Open palms facing forward: \"This is definitive\"")
bullet("The steeple (fingertips touching): Projects deep thought and certainty")
bullet("Counting on fingers: Signals structure and preparation")
bullet("Hands at rest on the table: Calm, grounded, ready")

bold("Weak gestures to eliminate:")
bullet("Fidgeting with pens, rings, hair, or clothing — screams anxiety")
bullet("Wringing hands — signals stress")
bullet("Touching face or neck — subconscious anxiety display")
bullet("Hiding hands under the table or in pockets — reduces trust")
bullet("Excessive gesturing — distracting, loses impact")

bold("The stillness principle: Between gestures, return to stillness. The contrast between stillness and a deliberate gesture gives the gesture power.")

doc.add_heading("2.4 Entering a Room", level=2)
bold("The power entrance:")
doc.add_paragraph("1. Walk at a measured pace. Deliberate, not rushed.", style="List Number")
doc.add_paragraph("2. Head up, shoulders back. Chin level, eyes forward.", style="List Number")
doc.add_paragraph("3. Walk to your seat with purpose. Don't hover. Don't linger.", style="List Number")
doc.add_paragraph("4. Place your materials deliberately. Notebook, pen, water — ownership of your space.", style="List Number")
doc.add_paragraph("5. Make eye contact with people as you sit down. A nod, a brief acknowledgment.", style="List Number")

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# PART 3: THE FIVE POWER TECHNIQUES
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading("PART 3: THE FIVE POWER TECHNIQUES", level=1)
doc.add_paragraph("Named, specific techniques to practice until they become unconscious habits.")

techniques = [
    ("Technique 1: The Strategic Pause",
     "After making a key point, pause for 2-3 seconds. Let the room absorb it. Do not fill the silence.",
     ["After stating a recommendation or conclusion", "After sharing a significant data point",
      "After asking a question (let the silence compel an answer)", "Before answering a difficult question (shows composure)"]),
    ("Technique 2: The Downward Inflection",
     "End every statement with falling pitch. The pitch drops on the final word.",
     ["\"This is the direction we're taking.\"", "\"The data is unambiguous.\"",
      "\"I need a decision by Friday.\"", "\"We're not going to accept that.\"", "\"Let me be clear about this.\""]),
    ("Technique 3: The Steeple",
     "Touch your fingertips together in front of your chest. This is the gesture of deliberation and certainty.",
     ["While listening to someone else (shows engaged evaluation)", "When pausing before answering a question",
      "During a moment of disagreement (projects calm confidence)"]),
    ("Technique 4: Controlled Pace",
     "Speak at 130-150 words per minute for authority. At high-impact moments, slow to 100-120 wpm.",
     ["Count words in a paragraph, time your delivery", "Divide words by seconds, multiply by 60",
      "When catching yourself speeding up, take a full breath between sentences"]),
    ("Technique 5: The Grounded Stance",
     "When standing, feet shoulder-width apart, weight evenly distributed. Do not shift, sway, or rock.",
     ["Stand and deliver a 30-second point", "Have someone watch your feet — are they planted?",
      "If you're moving, anchor yourself and try again"]),
]

for title, desc, points in techniques:
    doc.add_heading(title, level=2)
    bold(desc)
    for point in points:
        bullet(point)
    doc.add_paragraph()

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# PART 4: DAILY DRILLS
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading("PART 4: DAILY DRILLS", level=1)

doc.add_heading("Drill 1: The Authority Delivery (15 minutes)", level=2)
doc.add_paragraph(
    "Read each statement aloud with downward inflection, a 2-3 second pause after, "
    "zero filler words, controlled pace, and grounded stance."
)
statements = [
    "We need to reallocate resources to meet the Q4 target.",
    "I've reviewed the proposal. There are three areas that need revision.",
    "This is the direction we're taking. Let me walk you through the rationale.",
    "The data supports a different conclusion than what's been presented.",
    "I want to be direct. The current approach isn't working.",
]
for i, s in enumerate(statements, 1):
    bold(f'{i}. "{s}"')

bold("Self-check after each statement:")
bullet("Pitch dropped on the last word?")
bullet("Held silence for 2-3 seconds after?")
bullet("Zero filler words?")
bullet("Pace felt deliberate, not rushed?")
bullet("Body was still and grounded?")

doc.add_heading("Drill 2: The Pause Drill (10 minutes)", level=2)
doc.add_paragraph("Read the first statement, HOLD SILENCE, then deliver the follow-up.")

pause_drills = [
    ("The numbers don't support this strategy.", 3, "Here's what the data actually shows."),
    ("I have a different perspective on this.", 2, "Let me walk you through it."),
    ("We have a decision to make.", 3, "And I think the answer is clear."),
    ("I want to be candid with you.", 2, "This project is behind schedule."),
    ("Our client retention rate dropped 15% this quarter.", 4, "That should concern everyone in this room."),
    ("I've spent the last two weeks analyzing this.", 2, "And my conclusion is clear."),
    ("There's something we need to discuss.", 3, "It's not going to be comfortable, but it's necessary."),
    ("I disagree.", 3, "Here's why."),
]
for i, (before, secs, after) in enumerate(pause_drills, 1):
    bold(f'{i}. "{before}"')
    p = doc.add_paragraph()
    r = p.add_run(f"    >>> HOLD {secs} SECONDS OF SILENCE <<<")
    r.bold = True
    r.font.color.rgb = RGBColor(0xE7, 0x4C, 0x3C)
    doc.add_paragraph(f'    "{after}"')
    doc.add_paragraph()

doc.add_heading("Drill 3: The Mirror Drill (Daily — 5 minutes)", level=2)
bold("This is your most important daily exercise for Week 2.")
doc.add_paragraph("1. Stand in front of a mirror, feet shoulder-width apart", style="List Number")
doc.add_paragraph("2. Make eye contact with your own reflection", style="List Number")
doc.add_paragraph("3. Deliver a 60-second update on ANY topic", style="List Number")
doc.add_paragraph("4. Maintain: constant eye contact, zero filler, deliberate pauses, downward inflection, still body", style="List Number")
doc.add_paragraph("5. Record it on your phone (audio or video)", style="List Number")
doc.add_paragraph("6. Play it back. Grade yourself.", style="List Number")

doc.add_heading("Drill 4: The Pace Calibration (10 min, twice this week)", level=2)
doc.add_paragraph("Use the 150-word practice paragraph from Part 1.2.")
bullet("Set a timer for 60 seconds")
bullet("Read the paragraph aloud — you should finish right at 60 seconds")
bullet("If you finish early, you're rushing — slow down")
bullet("Record it. Listen. Notice how \"slow\" 150 wpm actually sounds.")

doc.add_heading("Drill 5: The Eye Contact Challenge", level=2)
doc.add_paragraph("This week, in at least 3 real conversations:")
bullet("Maintain eye contact for a full 5 seconds while making a point")
bullet("When someone challenges you, do NOT look away. Hold eye contact, pause, then respond.")
bullet("In a meeting, deliver one sentence directly to one person with full eye contact before moving to the next.")

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# PART 5: INTEGRATED DELIVERY
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading("PART 5: THE INTEGRATED DELIVERY", level=1)
doc.add_paragraph("This is where Weeks 1 and 2 merge. Combine clean language with vocal authority and physical presence.")

doc.add_heading("Scenario 1: The Project Update (stand and deliver)", level=2)
doc.add_paragraph("Stand up. Feet planted. Shoulders back. Deliver in under 45 seconds:")
quote_block(
    "The project is on track for March delivery. [PAUSE] We hit the API integration "
    "milestone last week, which was the highest-risk item on the timeline. Two items "
    "remain: the load testing phase, which starts Monday, and the security review, "
    "scheduled for the following week. [PAUSE] I don't anticipate any blockers, but "
    "I'm monitoring vendor response times closely. If they slip, I have a contingency "
    "plan ready."
)

doc.add_heading("Scenario 2: The Difficult Point (seated)", level=2)
doc.add_paragraph("Sit with power posture. Lean forward slightly. Make eye contact.")
quote_block(
    "I want to be direct about something. [PAUSE] The timeline we agreed to in January "
    "is no longer realistic. The scope has expanded twice since then, and we haven't "
    "adjusted the deadline. [PAUSE] I'm recommending we extend by three weeks. The "
    "alternative is shipping something we're not confident in, and I don't think that "
    "serves anyone."
)

doc.add_heading("Scenario 3: The Confident Disagreement (standing)", level=2)
doc.add_paragraph("Stand. Grounded stance. Steeple gesture while listening, then deliver:")
quote_block(
    "I see the logic in that approach. [PAUSE] And I've arrived at a different "
    "conclusion. [PAUSE] The data from Q3 shows that the strategy you're proposing "
    "was tested in the Southeast market and underperformed by 22%. My recommendation "
    "is we take the lessons from that pilot and design a different entry strategy. "
    "Let me walk you through what I have in mind."
)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# PART 6: COMMON MISTAKES
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading("PART 6: COMMON MISTAKES AND CORRECTIONS", level=1)

table(["Mistake", "Why It Happens", "The Fix"], [
    ("Voice rises when challenged", "Stress tightens vocal cords", "Breathe before responding. Consciously push pitch down."),
    ("Rushing through points", "Fear of losing the room", "Trust the room. One point at a time. Breathe between sentences."),
    ("Filling every silence", "Discomfort with quiet", "Practice silence tolerance. 3 seconds is not an eternity."),
    ("Looking down when disagreed with", "Submission instinct", "Pre-commit: decide you will NOT break eye contact downward."),
    ("Fidgeting with pen/phone", "Nervous energy outlet", "Put the pen down. Phone face-down. Hands on table, at rest."),
    ("Swaying when standing", "Ungrounded stance", "Plant feet shoulder-width. Imagine roots into the floor."),
    ("Speaking from the throat", "Shallow breathing", "Start with 3 diaphragmatic breaths."),
    ("Over-gesturing", "Compensating for weak delivery", "Let the WORDS carry weight. Gesture only to emphasize."),
])

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# PART 7: DAILY SCHEDULE
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading("PART 7: THE WEEK 2 DAILY SCHEDULE", level=1)

days = [
    ("Monday — Voice Day", [
        "Morning (15 min): Read Part 1. Do the morning hum and diaphragmatic breathing.",
        "Lunch (10 min): Practice the 150-word paragraph at 150 wpm. Record and listen.",
        "Evening (5 min): Mirror drill. Focus on vocal register and pace.",
    ]),
    ("Tuesday — Body Day", [
        "Morning (15 min): Read Part 2. Practice power posture — standing and seated.",
        "All day: Notice your posture in meetings. Are you shrinking? Leaning? Fidgeting? Correct in real time.",
        "Evening (5 min): Mirror drill. Focus on posture, stillness, and eye contact.",
    ]),
    ("Wednesday — Pause Day", [
        "Morning (10 min): Complete Drill 2 (The Pause Drill). All 8 exercises.",
        "All day: Insert at least 3 strategic pauses in real conversations.",
        "Evening (5 min): Mirror drill. Focus on pause integration.",
    ]),
    ("Thursday — Integration Day", [
        "Morning (15 min): Complete the Integrated Delivery scenarios (Part 5). Stand and deliver all three.",
        "All day: Apply everything in real meetings: voice, pace, pause, posture, eye contact, stillness.",
        "Evening (10 min): Journal — what felt natural? What felt forced? What landed?",
    ]),
    ("Friday — Drill Day", [
        "Morning (20 min): Complete Drill 1 (Authority Delivery) and Drill 4 (Pace Calibration).",
        "All day: Eye Contact Challenge (Drill 5) — hit your 3-conversation minimum.",
        "Evening (5 min): Final mirror drill. Record video. Watch with sound off — does your body say authority? Sound on — does your voice match?",
    ]),
    ("Weekend — Reinforcement", [
        "10 min/day: Mirror drill. Integrate everything.",
        "Watch: Find a 5-minute speech by someone authoritative. Watch HOW they deliver: pace, pauses, posture, eye contact. Take notes.",
        "Record: 2-minute impromptu brief on any topic. Compare to Week 1 recordings.",
    ]),
]

for day_title, activities in days:
    doc.add_heading(day_title, level=2)
    for a in activities:
        bullet(a)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# PART 8: SELF-ASSESSMENT
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading("PART 8: SELF-ASSESSMENT — END OF WEEK 2", level=1)
doc.add_paragraph("Rate yourself honestly (1 = not at all, 5 = fully capable):")

assessments = [
    "I speak at a controlled pace (130-150 wpm) without rushing:  ___/5",
    "I use downward inflection on every statement:  ___/5",
    "I can hold a strategic pause for 3 seconds without filling it:  ___/5",
    "My posture is open and grounded (standing and seated):  ___/5",
    "I maintain eye contact for 3-5 seconds per person:  ___/5",
    "I do not fidget, sway, or shift when speaking:  ___/5",
    "I enter rooms with purpose and settle deliberately:  ___/5",
    "My mirror drill integrates Week 1 + Week 2 skills:  ___/5",
]
for a in assessments:
    bullet(a)

doc.add_paragraph()
bold("Scoring:")
bullet("32-40: Outstanding. You're projecting real physical authority. Move to Week 3.")
bullet("24-31: Good foundation. Spend extra time on your weakest area before advancing.")
bullet("Below 24: Stay on Week 2. Physical presence is a skill — it takes reps.")

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# PART 9: PRINCIPLES
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading("PART 9: PRINCIPLES TO INTERNALIZE", level=1)

principles = [
    ("Your voice is the first thing the room judges.",
     "Before they process your words, they've already decided if you sound authoritative. Tune the instrument."),
    ("Silence is a weapon.",
     "The pause after a statement isn't dead air — it's where your point gains weight. Use it aggressively."),
    ("Stillness is power.",
     "Constant movement bleeds energy and attention away from your message. Be still. Move with purpose. Return to still."),
    ("Your body talks louder than your mouth.",
     "If your words say \"I'm confident\" but your body says \"I'm nervous,\" the room believes your body."),
    ("Slow is smooth, smooth is fast.",
     "When you slow down, you sound more articulate, more prepared, and more in control."),
    ("Eye contact is a commitment.",
     "Looking someone in the eye while you make a point says: \"I believe this, and I'm telling YOU directly.\""),
]
for i, (title, body) in enumerate(principles, 1):
    bold(f"{i}. {title}")
    doc.add_paragraph(body)

doc.add_paragraph()
doc.add_paragraph()

# Closing
closing = doc.add_paragraph()
closing.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = closing.add_run('"Stand like you mean it. Speak like you own it. Pause like the room can wait."')
run.italic = True
run.font.size = Pt(14)
run.font.color.rgb = RGBColor(0x2C, 0x3E, 0x50)

# ── Save ────────────────────────────────────────────────────────────────────
output_path = "/home/user/reinsurance-analysis/gravitas-app/guides/Week_02_Study_Guide.docx"
doc.save(output_path)
print(f"Saved to {output_path}")
