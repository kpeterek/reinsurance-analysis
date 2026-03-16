#!/usr/bin/env python3
"""Generate Week 1 Study Guide as a Word document."""

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

doc = Document()

# ── Styles ──────────────────────────────────────────────────────────────────
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


def add_bold_para(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = True
    return p


def add_italic_para(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.italic = True
    return p


def add_example_box(before, after):
    """Add a before/after transformation example."""
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


def add_table(headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Light Grid Accent 1"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.bold = True
    for r_idx, row in enumerate(rows):
        for c_idx, val in enumerate(row):
            table.rows[r_idx + 1].cells[c_idx].text = val
    doc.add_paragraph()
    return table


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
run = subtitle.add_run("WEEK 1: ELIMINATING WEAK LANGUAGE")
run.font.size = Pt(18)
run.font.color.rgb = RGBColor(0x2C, 0x3E, 0x50)

doc.add_paragraph()

tagline = doc.add_paragraph()
tagline.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = tagline.add_run("Phase 1: Foundation")
run.font.size = Pt(14)
run.italic = True

doc.add_paragraph()

theme = doc.add_paragraph()
theme.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = theme.add_run('"Stop undermining yourself before you start building power"')
run.font.size = Pt(12)
run.italic = True
run.font.color.rgb = RGBColor(0x7F, 0x8C, 0x8D)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# WHY THIS WEEK MATTERS
# ═══════════════════════════════════════════════════════════════════════════

doc.add_heading("WHY THIS WEEK MATTERS", level=1)

doc.add_paragraph(
    "Before you can project authority, you have to stop actively destroying it. "
    "Most professionals unconsciously sabotage themselves dozens of times per day "
    "with filler words, hedging language, apologetic preambles, and uptalk. These "
    "aren't just bad habits — they are status signals. Every time you say \"I think "
    "maybe we should...\" instead of \"We should...\", you are broadcasting to the "
    "room: I'm not sure I belong here. Please don't challenge me."
)

add_bold_para(
    "This week has one objective: identify and eliminate every verbal tic that "
    "undermines your authority. Nothing else in this program works if this "
    "foundation isn't solid. You can't command a room while apologizing for "
    "being in it."
)

# ═══════════════════════════════════════════════════════════════════════════
# PART 1: THE FIVE WEAKNESS SIGNALS
# ═══════════════════════════════════════════════════════════════════════════

doc.add_heading("PART 1: THE FIVE WEAKNESS SIGNALS", level=1)

doc.add_paragraph(
    "Master this taxonomy. Once you can name these patterns, you'll hear them "
    "everywhere — in yourself and in others."
)

# 1.1 Filler Words
doc.add_heading("1.1 Filler Words", level=2)

add_bold_para('What they are: "Um," "uh," "like," "you know," "so," "right," "I mean"')

doc.add_paragraph(
    "Why they kill you: Fillers signal that your brain is lagging behind your "
    "mouth. They communicate processing time, nervousness, or lack of preparation. "
    "Research from the University of Michigan found that speakers who use excessive "
    "fillers are rated as less competent, less trustworthy, and less hirable — "
    "regardless of the actual content of what they say."
)

doc.add_paragraph(
    "The real problem: Fillers become invisible to you. You don't hear them. "
    "Other people do. A single \"um\" in a 5-minute presentation is nothing. "
    "Twelve of them make you sound like you're winging it."
)

add_bold_para("The fix:")
doc.add_paragraph("Record yourself speaking for 2 minutes. Count the fillers. The number will shock you.", style="List Bullet")
doc.add_paragraph("Replace fillers with silence. A pause where an \"um\" would have been actually makes you sound more authoritative, not less.", style="List Bullet")
doc.add_paragraph("Practice the \"clean sentence\" drill: speak one complete sentence with zero filler, pause, speak the next. No bridging sounds between them.", style="List Bullet")

add_example_box(
    "So, um, I was like, looking at the report, and, you know, I think there are some, like, issues with the numbers.",
    "I reviewed the report. There are three issues with the numbers."
)

# 1.2 Hedging Language
doc.add_heading("1.2 Hedging Language", level=2)

add_bold_para('What it is: "I think," "sort of," "kind of," "maybe," "perhaps," "might," "possibly," "somewhat," "a little bit"')

doc.add_paragraph(
    "Why it kills you: Hedges are linguistic insurance policies. You use them "
    "so that if you're wrong, you can retreat to \"Well, I only said 'maybe.'\" "
    "The problem is that they don't protect you from being wrong — they just "
    "guarantee nobody takes you seriously when you're right."
)

doc.add_paragraph(
    "The psychology: Hedging is driven by fear of being wrong in public. But "
    "here's the paradox: confident people who state things clearly and are "
    "occasionally wrong are perceived as MORE competent than cautious people who "
    "are always technically correct but never commit to anything."
)

add_bold_para("The fix:")
doc.add_paragraph("Catch yourself before the hedge leaves your mouth. Replace it with a direct assertion.", style="List Bullet")
doc.add_paragraph("If you genuinely are uncertain, say so with authority: \"I don't have complete data on this yet. My preliminary assessment is...\"", style="List Bullet")
doc.add_paragraph("There's a difference between intellectual humility and verbal weakness. \"The data suggests X\" is humble AND authoritative. \"I kind of think maybe X\" is neither.", style="List Bullet")

add_example_box(
    "I sort of think we might want to maybe consider a different approach to this.",
    "I'd recommend a different approach. Here's why."
)

# 1.3 Uptalk
doc.add_heading("1.3 Uptalk", level=2)

add_bold_para(
    "What it is: Rising intonation at the end of declarative statements, turning "
    "them into questions."
)

doc.add_paragraph(
    "Why it kills you: Uptalk converts your assertions into requests for "
    "validation. It tells the room: \"I'm saying this, but I need you to confirm "
    "it's okay.\" Leaders don't ask permission to state their views."
)

doc.add_paragraph(
    "The acoustic mechanics: In English, rising pitch at the end of a sentence "
    "signals a question. When you use rising pitch on a statement, your listener's "
    "brain processes it as a question — even if the words are declarative. The "
    "content says \"here's my recommendation.\" The delivery says \"is this okay?\""
)

add_bold_para("The fix:")
doc.add_paragraph("Consciously drop your pitch at the end of every statement. Picture your voice going down a staircase on the final word.", style="List Bullet")
doc.add_paragraph("Record yourself and listen specifically for uptalk. Mark each instance.", style="List Bullet")
doc.add_paragraph("Practice \"the landing\": deliver a statement and let your pitch DROP on the final word, then hold silence.", style="List Bullet")

add_example_box(
    "I think we should increase the budget? (rising pitch)",
    "We should increase the budget. (falling pitch, full stop, silence)"
)

# 1.4 Apologetic Preambles
doc.add_heading("1.4 Apologetic Preambles", level=2)

add_bold_para('What they are: "Sorry, but..." "I don\'t mean to interrupt, but..." "Sorry to bother you..." "Forgive me, but..."')

doc.add_paragraph(
    "Why they kill you: You are apologizing for having a point of view. You "
    "are asking forgiveness for contributing. You are framing your own input as "
    "an intrusion. This signals that you believe your contribution isn't welcome "
    "— and the room will take you at your word."
)

doc.add_paragraph(
    "The distinction: Apologize when you've genuinely caused harm. Never "
    "apologize for speaking, contributing, or having a perspective. Those are "
    "not offenses."
)

add_bold_para("The fix:")
doc.add_paragraph("Delete the apology. Just start with the point.", style="List Bullet")
doc.add_paragraph("If you need a transition, use a neutral lead-in: \"I want to flag something.\" \"Let me add a point here.\"", style="List Bullet")
doc.add_paragraph("Catch the impulse to apologize and ask yourself: \"Did I do something wrong?\" If the answer is no, don't apologize.", style="List Bullet")

add_example_box(
    "Sorry, I don't mean to interrupt, but I just had a quick thought about the timeline.",
    "I want to raise a point about the timeline."
)

# 1.5 Over-Qualifying
doc.add_heading("1.5 Over-Qualifying", level=2)

add_bold_para('What it is: "This might be wrong, but..." "I\'m no expert, but..." "This is probably a dumb question, but..." "Just a thought..."')

doc.add_paragraph(
    "Why it kills you: You are pre-rejecting your own idea. You are telling "
    "the room to discount what you're about to say before you've said it. Why "
    "would anyone take your idea seriously if YOU don't?"
)

doc.add_paragraph(
    "The psychology: Over-qualifying is a defense mechanism. If you pre-label "
    "your idea as potentially stupid, being dismissed hurts less. But the cost "
    "is that you train people to expect low-value contributions from you."
)

add_bold_para("The fix:")
doc.add_paragraph("State your point. Let the room evaluate it on its merits.", style="List Bullet")
doc.add_paragraph("If you're uncertain, frame it with authority: \"Based on what I've seen...\" \"The evidence suggests...\"", style="List Bullet")
doc.add_paragraph("The phrase \"Just a thought\" is a self-destruct button. Replace it with \"Here's what I'd recommend.\"", style="List Bullet")

add_example_box(
    "This is probably wrong, and I'm no expert, but what if we maybe tried a different vendor?",
    "We should evaluate changing the vendor. Here's my reasoning."
)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# PART 2: THE KILL LIST
# ═══════════════════════════════════════════════════════════════════════════

doc.add_heading("PART 2: THE KILL LIST — 10 PHRASES TO ELIMINATE PERMANENTLY", level=1)

doc.add_paragraph(
    "These are the specific phrases to purge from your vocabulary this week. "
    "For each one, there is a direct replacement. Memorize the replacement. "
    "Drill it until it's automatic."
)

kill_phrases = [
    ("1", "I think maybe we should...", "We should..."),
    ("2", "Sorry, but I just wanted to say...", "I want to flag something."),
    ("3", "This might be a stupid question, but...", "I have a question."),
    ("4", "I'm not sure, but...", "My understanding is..."),
    ("5", "Does that make sense?", "Let me know if you'd like me to elaborate."),
    ("6", "I feel like...", "My assessment is..."),
    ("7", "I'm no expert, but...", "Based on what I've seen..."),
    ("8", "Just a thought...", "Here's what I'd recommend."),
    ("9", "I could be wrong, but...", "The evidence suggests..."),
    ("10", "Hopefully that helps?", "That should address it."),
]

add_table(["#", "KILL THIS", "REPLACE WITH"], kill_phrases)

doc.add_heading("How to Drill These", level=3)
doc.add_paragraph("Day 1-2: Read the table aloud 5 times. Left column, then immediately right column. Speed up each repetition.", style="List Bullet")
doc.add_paragraph("Day 3-4: Cover the right column. Read each weak phrase and speak the replacement from memory. Repeat until you can do all 10 without looking.", style="List Bullet")
doc.add_paragraph("Day 5-7: Throughout the day, catch yourself using a kill phrase in real conversation. Correct it in real time. This real-time correction is where the rewiring happens.", style="List Bullet")

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# PART 3: EXTENDED REPLACEMENT PATTERNS
# ═══════════════════════════════════════════════════════════════════════════

doc.add_heading("PART 3: EXTENDED REPLACEMENT PATTERNS", level=1)

doc.add_heading("Starting a Point", level=2)
add_table(["Weak", "Strong"], [
    ("So basically what I'm trying to say is...", "Here's the point."),
    ("I just wanted to quickly mention...", "I want to highlight..."),
    ("If I could just add one thing...", "Let me add something."),
    ("I don't know if this is relevant, but...", "This is relevant."),
    ("Can I ask a dumb question?", "I have a question."),
])

doc.add_heading("Giving an Opinion", level=2)
add_table(["Weak", "Strong"], [
    ("I kind of feel like this isn't working.", "This isn't working. Here's what I'm seeing."),
    ("It seems like maybe we should...", "We should..."),
    ("I guess my thought would be...", "My recommendation is..."),
    ("I suppose one option could be...", "One option is..."),
    ("In my humble opinion...", "My view is... / simply state it"),
])

doc.add_heading("Responding to Questions", level=2)
add_table(["Weak", "Strong"], [
    ("That's a great question, um...", "Here's my take on that."),
    ("I'm not totally sure, but I think...", "My understanding is..."),
    ("I want to say it's around...", "It's approximately..."),
    ("I think so? Maybe?", "Yes. / No. / I'll confirm and follow up."),
    ("I mean, I guess...", "State the answer directly."),
])

doc.add_heading("In Emails and Slack", level=2)
add_table(["Weak", "Strong"], [
    ("Just following up...", "Following up on..."),
    ("Just wanted to check in...", "Checking in on..."),
    ("Sorry for the delayed response...", "Thank you for your patience. / Just respond."),
    ("I hope this email finds you well...", "Skip it. Start with the point."),
    ("Would it be possible to maybe...", "I'd like to... / Can we..."),
    ("No worries if not!", "Remove. Let your request stand."),
    ("Just my two cents...", "My recommendation:"),
    ("Thoughts??", "I'd like your input on [specific question]."),
])

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# PART 4: UNDERSTANDING THE PSYCHOLOGY
# ═══════════════════════════════════════════════════════════════════════════

doc.add_heading("PART 4: UNDERSTANDING THE PSYCHOLOGY", level=1)

doc.add_heading("Why We Use Weak Language", level=2)

doc.add_paragraph(
    "Weak language is a social survival strategy. Understanding why you do it "
    "makes it easier to stop."
)

add_bold_para("1. Status protection.")
doc.add_paragraph(
    "If you hedge, you can't be \"wrong.\" But being vague is worse than being "
    "wrong. People who commit to positions and occasionally miss are respected. "
    "People who never commit are ignored."
)

add_bold_para("2. Likability concern.")
doc.add_paragraph(
    "You worry that being direct will make you seem aggressive or arrogant. "
    "Research shows the opposite: clear, direct communicators are rated as MORE "
    "likable, not less — because they're easier to understand and waste less of "
    "people's time."
)

add_bold_para("3. Impostor syndrome.")
doc.add_paragraph(
    "You don't feel like you've \"earned\" the right to speak with authority. "
    "Here's the truth: authority is not granted. It's projected. You speak with "
    "authority, and people treat you as an authority. The permission comes from "
    "your delivery, not your resume."
)

add_bold_para("4. Cultural conditioning.")
doc.add_paragraph(
    "Many people — especially women, minorities, and those from cultures that "
    "prize deference — have been socialized to soften their language. Recognizing "
    "this conditioning is the first step to overriding it. Being direct is not "
    "being rude. It's being clear."
)

doc.add_heading("The Authority Paradox", level=2)

doc.add_paragraph(
    "People who speak with certainty are perceived as more competent, more "
    "trustworthy, and more leader-like — even when their actual knowledge is "
    "identical to someone who hedges."
)

doc.add_paragraph(
    "This is not about lying or overstating your knowledge. It's about matching "
    "your delivery to your conviction. If you believe something is true, say it "
    "like you believe it. If you're uncertain, name the uncertainty with "
    "authority: \"I don't have enough data to be definitive. Here's what I know "
    "so far.\""
)

doc.add_paragraph(
    "Both are authoritative. What's NOT authoritative is: \"I mean, I'm not sure, "
    "but I kind of think maybe...\""
)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# PART 5: DAILY DRILLS
# ═══════════════════════════════════════════════════════════════════════════

doc.add_heading("PART 5: DAILY DRILLS", level=1)

doc.add_heading("Drill 1: Phrase Replacement (15 minutes)", level=2)

doc.add_paragraph(
    "For each weak statement below, formulate a powerful replacement BEFORE "
    "reading the answer. Say your version aloud. Then compare."
)

drills = [
    ("I kind of think we should reconsider the timeline.",
     "We need to reconsider the timeline."),
    ("Sorry, I just had a quick thought about the budget.",
     "I want to raise a point about the budget."),
    ("I'm not really an expert on this, but maybe we could try a different approach?",
     "I'd recommend a different approach."),
    ("Um, so, like, I was thinking we could possibly look into this?",
     "I've been looking into this. Here's what I found."),
    ("This is probably wrong, but what if we changed the vendor?",
     "We should evaluate changing the vendor."),
]

for i, (weak, strong) in enumerate(drills, 1):
    add_bold_para(f"{i}. \"{weak}\"")
    p = doc.add_paragraph()
    r = p.add_run(f"Power version: ")
    r.bold = True
    r.font.color.rgb = RGBColor(0x27, 0xAE, 0x60)
    p.add_run(f'"{strong}"')
    doc.add_paragraph()

add_bold_para("Additional practice — rewrite these yourself:")
extras = [
    "I just want to quickly say that I feel like the numbers are a bit off.",
    "Sorry, does anyone mind if I share something? I'm not sure it's important, but...",
    "I could be wrong, but I think the client might not be happy with this?",
    "Just a thought — what if we, like, maybe tried to do it differently?",
    "I hope this makes sense, but basically what I'm trying to say is that we need more resources.",
]
for i, s in enumerate(extras, 6):
    doc.add_paragraph(f"{i}. \"{s}\"", style="List Bullet")

doc.add_paragraph()

doc.add_heading("Drill 2: Spot the Weakness (10 minutes)", level=2)

doc.add_paragraph("Read each statement and identify EVERY weak signal.")

add_bold_para("Statement 1:")
add_italic_para(
    "\"Sorry to bother you, but I just sort of wanted to maybe suggest that we "
    "could possibly look at the Q3 numbers, if that's okay?\""
)
add_bold_para("Weak signals (6):")
doc.add_paragraph("\"Sorry to bother you\" — apologetic preamble", style="List Bullet")
doc.add_paragraph("\"just\" — minimizer", style="List Bullet")
doc.add_paragraph("\"sort of\" — hedge", style="List Bullet")
doc.add_paragraph("\"maybe\" — hedge", style="List Bullet")
doc.add_paragraph("\"could possibly\" — double hedge", style="List Bullet")
doc.add_paragraph("\"if that's okay?\" — permission-seeking/uptalk", style="List Bullet")
p = doc.add_paragraph()
r = p.add_run("Power version: ")
r.bold = True
p.add_run("\"I want to look at the Q3 numbers. There's something worth examining.\"")
doc.add_paragraph()

add_bold_para("Statement 2:")
add_italic_para(
    "\"I think, um, like, we might want to kind of revisit the strategy? Just a thought.\""
)
add_bold_para("Weak signals (7):")
doc.add_paragraph("\"I think\" — hedge", style="List Bullet")
doc.add_paragraph("\"um\" — filler", style="List Bullet")
doc.add_paragraph("\"like\" — filler", style="List Bullet")
doc.add_paragraph("\"might want to\" — hedge", style="List Bullet")
doc.add_paragraph("\"kind of\" — hedge", style="List Bullet")
doc.add_paragraph("\"?\" (uptalk) — rising intonation on a statement", style="List Bullet")
doc.add_paragraph("\"Just a thought\" — self-dismissal", style="List Bullet")
p = doc.add_paragraph()
r = p.add_run("Power version: ")
r.bold = True
p.add_run("\"We need to revisit the strategy.\"")
doc.add_paragraph()

add_bold_para("Statement 3:")
add_italic_para(
    "\"I'm no expert, but I feel like this approach is probably not the best, if you know what I mean?\""
)
add_bold_para("Weak signals (4):")
doc.add_paragraph("\"I'm no expert\" — pre-disqualification", style="List Bullet")
doc.add_paragraph("\"I feel like\" — emotion over analysis", style="List Bullet")
doc.add_paragraph("\"probably\" — hedge", style="List Bullet")
doc.add_paragraph("\"if you know what I mean?\" — seeking validation", style="List Bullet")
p = doc.add_paragraph()
r = p.add_run("Power version: ")
r.bold = True
p.add_run("\"This approach has significant weaknesses. Let me walk you through what I'm seeing.\"")

doc.add_paragraph()

doc.add_heading("Drill 3: The 2-Minute Recording (Daily — Non-Negotiable)", level=2)

doc.add_paragraph("This is your most important daily exercise for the entire week.")

add_bold_para("Instructions:")
doc.add_paragraph("Open your phone's voice recorder.", style="List Number")
doc.add_paragraph("Pick any topic — your current project, what you did yesterday, a business problem you're thinking about.", style="List Number")
doc.add_paragraph("Speak for exactly 2 minutes.", style="List Number")
doc.add_paragraph("Play it back. Tally every instance of: filler words, hedges, apologies, uptalk.", style="List Number")
doc.add_paragraph("Write down the count.", style="List Number")
doc.add_paragraph("Do it again. Beat your previous count.", style="List Number")

doc.add_paragraph()
add_bold_para("Target by end of Week 1: Fewer than 3 total weakness signals in a 2-minute recording.")
add_bold_para("Target by end of Week 3: Zero.")

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# PART 6: REAL-WORLD APPLICATION SCENARIOS
# ═══════════════════════════════════════════════════════════════════════════

doc.add_heading("PART 6: REAL-WORLD APPLICATION SCENARIOS", level=1)

scenarios = [
    ("Scenario 1: The Team Meeting",
     "You're in a weekly team meeting. Your manager asks for opinions on the new project timeline.",
     "Um, I don't know, I kind of feel like maybe the timeline is a little aggressive? Just my opinion though. Sorry if that's not helpful.",
     "The timeline is aggressive. I see two specific risks: the vendor integration hasn't been scoped, and we don't have QA bandwidth until week 6. I'd recommend adding two weeks."),
    ("Scenario 2: The Slack Message",
     "A colleague asks for your take on a design document.",
     "Hey! So I took a quick look and I think it's mostly good? I had a few small thoughts, not sure if they're helpful. Sorry if this is obvious but maybe the auth flow could be a little cleaner? Just a thought! No worries if you disagree!",
     "I reviewed the document. Two recommendations: 1) Simplify the auth flow — the current design has three redundant steps. 2) Add error handling for the API timeout case. Happy to walk through either of these."),
    ("Scenario 3: The Executive Update",
     "Your director asks how your project is going in the hallway.",
     "Oh, um, it's going okay, I think? We've been kind of busy and there's a lot going on. Hopefully we'll have something to show soon?",
     "We're on track. The core feature ships Friday. One risk I'm watching: the third-party API has had latency issues. I have a fallback plan if it becomes a blocker."),
    ("Scenario 4: The Stakeholder Email",
     "You need to inform a stakeholder about a change in scope.",
     "Hi! Hope you're doing well! Just wanted to give you a quick heads up — so we've been thinking about the scope and I think we might need to adjust a few things. Sorry for any inconvenience! Let me know if you have any thoughts or concerns. Thanks so much!",
     "Subject: Scope adjustment — Project X\n\nWe're adjusting the scope for Project X. Specifically, we're deferring the reporting module to Phase 2 to ensure the core platform ships on schedule.\n\nThis doesn't affect the March delivery date. I'll share the updated scope document by Wednesday.\n\nLet me know if you have questions."),
]

for title, context, old, new in scenarios:
    doc.add_heading(title, level=2)
    add_italic_para(context)
    add_example_box(old, new)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# PART 7: THE WEEK 1 DAILY SCHEDULE
# ═══════════════════════════════════════════════════════════════════════════

doc.add_heading("PART 7: THE WEEK 1 DAILY SCHEDULE", level=1)

days = [
    ("Monday — Awareness Day", [
        "Morning (15 min): Read Part 1 (The Five Weakness Signals). Internalize each pattern.",
        "All day: Simply NOTICE your weak language. Don't try to fix it yet. Keep a tally on a notecard or phone.",
        "Evening (10 min): Do your first 2-minute recording. Count the signals. Write the number down.",
    ]),
    ("Tuesday — Kill List Day", [
        "Morning (20 min): Memorize the 10 Kill Phrases and their replacements (Part 2). Read the table aloud 5 times.",
        "All day: Actively replace kill phrases in conversation. Catch and correct in real time.",
        "Evening (10 min): 2-minute recording. Count signals. Compare to Monday.",
    ]),
    ("Wednesday — Drill Day", [
        "Morning (25 min): Complete Drill 1 (Phrase Replacement) and Drill 2 (Spot the Weakness).",
        "Lunch: Run the app drills if available.",
        "Evening (10 min): 2-minute recording. Target: measurable improvement.",
    ]),
    ("Thursday — Application Day", [
        "All day: Apply everything in actual work conversations, meetings, emails, and Slack messages.",
        "Before every meeting: Write down one point in power language. Deliver it exactly as written.",
        "Before every email: Check for kill phrases before hitting send.",
        "Evening (10 min): Journal what worked and what didn't.",
    ]),
    ("Friday — Review Day", [
        "Morning (15 min): Re-read the extended patterns (Part 3). Practice the ones you still struggle with.",
        "All day: Continue applying in real conversations.",
        "Evening (15 min): Final 2-minute recording. Compare to Monday. Celebrate improvement. Identify gaps.",
    ]),
    ("Weekend — Reinforcement", [
        "10 min/day: Run flashcard drills.",
        "Practice: Pick 3 kill phrase replacements you still fumble. Say each one 10 times aloud.",
        "Review: Read your journal notes. What patterns keep recurring?",
    ]),
]

for day_title, activities in days:
    doc.add_heading(day_title, level=2)
    for activity in activities:
        doc.add_paragraph(activity, style="List Bullet")

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# PART 8: SELF-ASSESSMENT
# ═══════════════════════════════════════════════════════════════════════════

doc.add_heading("PART 8: SELF-ASSESSMENT — END OF WEEK 1", level=1)

doc.add_paragraph("Rate yourself honestly on each item (1 = not at all, 5 = fully capable):")
doc.add_paragraph()

assessments = [
    "I can identify filler words in my own speech:  ___/5",
    "I can identify hedging language in real time:  ___/5",
    "I catch myself before an apologetic preamble and rephrase:  ___/5",
    "I end statements with downward inflection (not uptalk):  ___/5",
    "I can recite all 10 kill phrase replacements from memory:  ___/5",
    "My 2-minute recording has fewer than 5 weakness signals:  ___/5",
    "I've applied at least one replacement in a real conversation:  ___/5",
    "My emails and Slack messages are free of weak language:  ___/5",
]

for a in assessments:
    doc.add_paragraph(a, style="List Bullet")

doc.add_paragraph()
add_bold_para("Scoring:")
doc.add_paragraph("32-40: Excellent. You're ready for Week 2.", style="List Bullet")
doc.add_paragraph("24-31: Good progress. Spend an extra day on drills before advancing.", style="List Bullet")
doc.add_paragraph("Below 24: Stay on Week 1 for another week. The foundation must be solid.", style="List Bullet")

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# PART 9: KEY PRINCIPLES
# ═══════════════════════════════════════════════════════════════════════════

doc.add_heading("PART 9: KEY PRINCIPLES TO INTERNALIZE", level=1)

principles = [
    ("Silence is better than filler.", "A pause where an \"um\" would have been makes you sound thoughtful, not uncertain."),
    ("Direct is not rude.", "\"We should change the approach\" is professional. \"Sorry, I just kind of think maybe we could...\" is not more polite. It's less clear."),
    ("State, don't ask.", "Your recommendations are not requests for permission. \"I'd recommend X\" not \"Would it be okay if maybe we tried X?\""),
    ("Commit to your position.", "If you believe it, say it with conviction. If you're uncertain, name the uncertainty with authority. There is no scenario where hedging helps you."),
    ("Correct in real time.", "When you catch a weak phrase mid-sentence, stop and rephrase. This rewires the habit faster than anything else."),
    ("The goal is not perfection.", "The goal is awareness. Once you can hear the weakness, you can eliminate it. Awareness precedes change."),
]

for i, (title, body) in enumerate(principles, 1):
    add_bold_para(f"{i}. {title}")
    doc.add_paragraph(body)

doc.add_paragraph()
doc.add_paragraph()

# Closing
closing = doc.add_paragraph()
closing.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = closing.add_run('"Speak less. Mean more. Every word earns its place."')
run.italic = True
run.font.size = Pt(14)
run.font.color.rgb = RGBColor(0x2C, 0x3E, 0x50)

# ── Save ────────────────────────────────────────────────────────────────────

output_path = "/home/user/reinsurance-analysis/gravitas-app/guides/Week_01_Study_Guide.docx"
doc.save(output_path)
print(f"Saved to {output_path}")
