"""
Corporate Gravitas Training - 12-Week Progressive Curriculum

Structured from foundational presence through advanced executive communication.
Each week builds on the last. Phrases are drilled until reflexive.
"""

CURRICULUM = {
    # =========================================================================
    # PHASE 1: FOUNDATION (Weeks 1-3) - Eliminate weakness signals, build base
    # =========================================================================
    1: {
        "title": "Eliminating Weak Language",
        "theme": "Stop undermining yourself before you start building power",
        "concepts": [
            "Filler words ('um', 'like', 'you know') destroy perceived competence",
            "Hedging language ('I think', 'sort of', 'maybe') signals uncertainty",
            "Uptalk (rising intonation on statements) converts assertions into questions",
            "Apologetic preambles ('Sorry, but...') surrender authority before you speak",
            "Over-qualifying ('This might be wrong, but...') invites dismissal",
        ],
        "kill_phrases": {
            "I think maybe we should...": "We should...",
            "Sorry, but I just wanted to say...": "I want to flag something.",
            "This might be a stupid question, but...": "I have a question.",
            "I'm not sure, but...": "My understanding is...",
            "Does that make sense?": "Let me know if you'd like me to elaborate.",
            "I feel like...": "My assessment is...",
            "I'm no expert, but...": "Based on what I've seen...",
            "Just a thought...": "Here's what I'd recommend.",
            "I could be wrong, but...": "The evidence suggests...",
            "Hopefully that helps?": "That should address it.",
        },
        "drills": [
            {
                "type": "replacement",
                "instruction": "Replace the weak phrase with a powerful alternative",
                "items": [
                    ("I kind of think we should reconsider the timeline",
                     "We need to reconsider the timeline."),
                    ("Sorry, I just had a quick thought about the budget",
                     "I want to raise a point about the budget."),
                    ("I'm not really an expert on this, but maybe we could try a different approach?",
                     "I'd recommend a different approach."),
                    ("Um, so, like, I was thinking we could possibly look into this?",
                     "I've been looking into this. Here's what I found."),
                    ("This is probably wrong, but what if we changed the vendor?",
                     "We should evaluate changing the vendor."),
                ],
            },
            {
                "type": "spot_the_weakness",
                "instruction": "Identify every weak signal in the statement",
                "items": [
                    ("Sorry to bother you, but I just sort of wanted to maybe suggest that we could possibly look at the Q3 numbers, if that's okay?",
                     ["Sorry to bother you", "just", "sort of", "maybe", "could possibly", "if that's okay"]),
                    ("I think, um, like, we might want to kind of revisit the strategy? Just a thought.",
                     ["I think", "um", "like", "might want to", "kind of", "uptalk (?)", "Just a thought"]),
                    ("I'm no expert, but I feel like this approach is probably not the best, if you know what I mean?",
                     ["I'm no expert", "I feel like", "probably", "if you know what I mean"]),
                ],
            },
        ],
        "daily_practice": "Record yourself speaking for 2 minutes about your current project. Count every filler word and hedge. Target: zero.",
    },

    2: {
        "title": "Vocal Authority & Physical Presence",
        "theme": "Your body and voice speak before your words do",
        "concepts": [
            "Lower your vocal register slightly — deeper voices are perceived as more authoritative",
            "Pace: slow down. Powerful people are never in a rush to speak",
            "The pause is your most powerful tool — silence after a point lets it land",
            "Posture: occupy space. Shoulders back, chin level, feet planted",
            "Eye contact: hold it 3-5 seconds per person. Breaking eye contact downward signals submission",
            "Hand gestures: open palms signal confidence; fidgeting destroys it",
            "Enter a room like you belong there — walk to your seat with purpose",
        ],
        "power_techniques": {
            "The Strategic Pause": "After making a key point, pause for 2-3 seconds. Let the room absorb it. Do not fill the silence.",
            "The Downward Inflection": "End statements with falling pitch. 'We're moving forward with Option A.' (pitch drops on 'A')",
            "The Steeple": "Touch fingertips together — the 'steeple' gesture projects certainty and thoughtfulness",
            "Controlled Pace": "Speak at 130-150 words per minute for authority. Rushing signals anxiety.",
            "The Grounded Stance": "When standing, feet shoulder-width apart, weight evenly distributed. Do not shift or sway.",
        },
        "drills": [
            {
                "type": "delivery",
                "instruction": "Read each statement aloud with downward inflection, a pause after, and zero filler",
                "items": [
                    "We need to reallocate resources to meet the Q4 target.",
                    "I've reviewed the proposal. There are three areas that need revision.",
                    "This is the direction we're taking. Let me walk you through the rationale.",
                    "The data supports a different conclusion than what's been presented.",
                    "I want to be direct. The current approach isn't working.",
                ],
            },
            {
                "type": "pause_drill",
                "instruction": "Read the statement, then HOLD SILENCE for the indicated duration before continuing",
                "items": [
                    ("The numbers don't support this strategy.", 3, "Here's what the data actually shows."),
                    ("I have a different perspective on this.", 2, "Let me walk you through it."),
                    ("We have a decision to make.", 3, "And I think the answer is clear."),
                    ("I want to be candid with you.", 2, "This project is behind schedule."),
                ],
            },
        ],
        "daily_practice": "Stand in front of a mirror. Deliver a 60-second update on any topic. Maintain eye contact with your reflection, zero filler, deliberate pauses, and downward inflection on every statement.",
    },

    3: {
        "title": "The Architecture of Decisive Statements",
        "theme": "Structure your speech so every word carries weight",
        "concepts": [
            "Lead with the conclusion, then support it — never bury the lead",
            "The Rule of Three: three points are memorable, persuasive, and complete",
            "Eliminate weasel words: 'very', 'really', 'actually', 'basically', 'literally'",
            "Use concrete specifics over vague generalities",
            "Active voice > passive voice: 'I decided' not 'It was decided'",
        ],
        "frameworks": {
            "Bottom Line Up Front (BLUF)": [
                "State your conclusion or recommendation first",
                "Then provide 2-3 supporting points",
                "Example: 'We should delay the launch by two weeks. First, QA found 14 critical bugs. Second, the partner integration isn't tested. Third, a failed launch costs us more than a delay.'",
            ],
            "The Power Triangle": [
                "Point: State the position",
                "Proof: Provide evidence or reasoning",
                "Punch: Deliver the implication or call to action",
                "Example: 'Our churn rate doubled this quarter. Exit interviews show pricing is the primary driver. We need to revisit our pricing model before Q3.'",
            ],
            "The Three-Beat": [
                "Organize any argument into exactly three supporting points",
                "This works for everything from elevator pitches to board presentations",
                "Example: 'This investment makes sense for three reasons: the market timing is right, we have a competitive advantage in distribution, and the risk profile is manageable.'",
            ],
        },
        "drills": [
            {
                "type": "restructure",
                "instruction": "Restructure the rambling statement into a BLUF format",
                "items": [
                    ("So I was looking at the numbers and they're not great, and I've been thinking about it, and there are a bunch of issues, but mainly the costs are too high and revenue is flat, so maybe we should look at cutting some expenses, I guess.",
                     "We need to cut expenses. Revenue is flat while costs have risen significantly. The current trajectory is unsustainable."),
                    ("Um, so the project is going okay, I think, but we're a little behind and there are some issues with the vendor and also the team is understaffed, so it might take longer than we thought, possibly.",
                     "The project will miss its current deadline. We're understaffed, and vendor delivery is behind schedule. I recommend we extend the timeline by three weeks and backfill two roles."),
                ],
            },
            {
                "type": "three_beat",
                "instruction": "Argue the given position using exactly three supporting points",
                "items": [
                    "We should invest in employee training this year.",
                    "Remote work should remain our default policy.",
                    "We need to switch CRM platforms.",
                    "The marketing budget should increase by 20%.",
                ],
            },
        ],
        "daily_practice": "For every email you write today, start with your conclusion. No preamble. No 'I hope this finds you well.'",
    },

    # =========================================================================
    # PHASE 2: EXECUTIVE COMMUNICATION (Weeks 4-6) - Speak like a leader
    # =========================================================================
    4: {
        "title": "Commanding the Room",
        "theme": "Meetings are performances. Prepare like it.",
        "concepts": [
            "Arrive with a prepared point of view — never wing it",
            "Speak early in meetings to establish presence (within the first 5 minutes)",
            "When you speak, address the room, not just the person who asked",
            "If interrupted, calmly finish your point: 'Let me complete this thought.'",
            "Ask questions that demonstrate strategic thinking, not confusion",
        ],
        "power_phrases": {
            "opening_a_meeting": [
                "Let's get aligned on three things today.",
                "I want to frame the discussion before we dive in.",
                "Here's what I see as the core question we need to answer.",
                "Before we get into details, let me set context.",
            ],
            "redirecting_discussion": [
                "Let's bring this back to the central question.",
                "That's a valid point. And it connects to the bigger issue, which is...",
                "I want to make sure we don't lose sight of the main objective.",
                "Let me reframe this slightly.",
            ],
            "handling_interruptions": [
                "Let me finish this thought.",
                "I want to complete this point, then I'd like to hear yours.",
                "Hold that thought — let me land this first.",
                "I appreciate the input. Let me close this out.",
            ],
            "closing_a_discussion": [
                "Let me summarize where we've landed.",
                "Here's what I'm taking away from this conversation.",
                "The action items are clear. Let me recap.",
                "Good discussion. Here's what we've decided.",
            ],
        },
        "drills": [
            {
                "type": "scenario",
                "instruction": "You're in a leadership meeting. Deliver the appropriate power phrase for each situation.",
                "items": [
                    {"situation": "The meeting has been going for 10 minutes with no direction.", "goal": "Take control and set an agenda."},
                    {"situation": "A colleague keeps talking over you.", "goal": "Reclaim the floor without being aggressive."},
                    {"situation": "The discussion has gone off on a tangent about a minor detail.", "goal": "Redirect to the strategic issue."},
                    {"situation": "A 45-minute meeting is at the 40-minute mark with no summary.", "goal": "Close it out decisively."},
                ],
            },
        ],
        "daily_practice": "In your next meeting, commit to speaking within the first 5 minutes with a prepared observation or question. Write it down before the meeting starts.",
    },

    5: {
        "title": "The Language of Strategic Thinking",
        "theme": "Speak in a way that signals you see the bigger picture",
        "concepts": [
            "Frame issues in terms of business impact, not just tasks",
            "Use 'we' for shared wins and team efforts; 'I' for personal accountability",
            "Reference data, timelines, and specifics — vagueness kills credibility",
            "Connect tactical details to strategic outcomes",
            "Anticipate the 'so what?' before anyone asks it",
        ],
        "phrase_bank": {
            "elevating_from_tactical_to_strategic": [
                "The real question here isn't [tactical detail] — it's [strategic implication].",
                "If we zoom out, what this really means for the business is...",
                "This decision has downstream implications for...",
                "Let me connect this back to our broader objective.",
                "The strategic risk here is...",
            ],
            "demonstrating_business_acumen": [
                "What's the revenue impact of that decision?",
                "How does this affect our competitive position?",
                "I want to understand the unit economics before we commit.",
                "What's the opportunity cost of not doing this?",
                "Let me frame this in terms of ROI.",
            ],
            "showing_you_think_ahead": [
                "If we follow this path, we should anticipate...",
                "The second-order effect of this is...",
                "Let me flag a potential risk three quarters out.",
                "We should think about how this scales.",
                "The question we'll face next is...",
            ],
            "taking_ownership": [
                "I'll own this and have an update by Friday.",
                "Let me take the lead on this.",
                "I'm accountable for this outcome.",
                "I'll drive this to resolution.",
                "This is on me. Here's my plan.",
            ],
        },
        "drills": [
            {
                "type": "elevate",
                "instruction": "Transform the tactical statement into a strategic one",
                "items": [
                    ("The server went down twice this week.",
                     "Our infrastructure reliability is creating business risk. Two outages this week translates to approximately $X in lost revenue and erodes customer trust. We need to prioritize a resilience investment."),
                    ("We need to hire three more engineers.",
                     "Our current engineering capacity is the bottleneck to hitting our Q3 revenue targets. I'm recommending we add three engineers, which would accelerate delivery by six weeks and unlock an estimated $2M in pipeline."),
                    ("The marketing campaign didn't hit its targets.",
                     "Our customer acquisition cost increased 40% this quarter, which directly impacts our path to profitability. We need to reassess our channel strategy."),
                ],
            },
        ],
        "daily_practice": "Take one routine status update you'd normally give and reframe it in terms of business impact before delivering it.",
    },

    6: {
        "title": "Mastering the Executive Summary",
        "theme": "If you can't say it in 30 seconds, you don't understand it well enough",
        "concepts": [
            "The Elevator Pitch: situation, complication, resolution — in 30 seconds",
            "Never start with background. Start with what matters NOW.",
            "Pyramid Principle: main point first, supporting details on request",
            "If asked to elaborate, go one level deeper — not five",
            "Match your communication depth to your audience's seniority",
        ],
        "templates": {
            "30_second_update": "Here's where we are: [status]. The key issue is [problem]. My recommendation is [action].",
            "escalation": "I need to flag [issue]. The impact is [consequence]. I need [decision/resource] by [date].",
            "project_status": "[Project] is [on track / at risk / off track]. The primary driver is [reason]. Next milestone is [date/deliverable].",
            "recommendation": "I'm recommending [action] because [reason 1], [reason 2], and [reason 3]. The risk of not acting is [consequence].",
            "bad_news": "I want to be upfront about [issue]. Here's what happened, here's the impact, and here's what I'm doing about it.",
        },
        "drills": [
            {
                "type": "compress",
                "instruction": "Compress the long-winded update into a 30-second executive summary",
                "items": [
                    ("So we've been working on the new product feature for about three weeks now, and the team has been doing a great job, but we've run into some issues with the API integration which is taking longer than expected. The vendor has been slow to respond, and we've had to do some workarounds. Also, Sarah was out sick for a week, which didn't help. We think we'll probably be done in another two to three weeks, but it depends on the vendor. Oh, and the budget might need to increase because of the workarounds.",
                     "The product feature is two weeks behind schedule, primarily due to vendor API delays. I'm projecting delivery in three weeks and a 15% budget increase. I need a decision on whether to escalate with the vendor or build the integration in-house."),
                ],
            },
            {
                "type": "timed_delivery",
                "instruction": "Deliver each summary in under 30 seconds. Time yourself.",
                "items": [
                    "Give a status update on a project you're working on.",
                    "Explain why your team should adopt a new tool.",
                    "Deliver bad news about a missed deadline.",
                    "Recommend a strategic pivot for a product.",
                ],
            },
        ],
        "daily_practice": "Before every conversation today, write your main point in ONE sentence. Lead with that sentence.",
    },

    # =========================================================================
    # PHASE 3: PERSUASION & INFLUENCE (Weeks 7-9) - Win arguments elegantly
    # =========================================================================
    7: {
        "title": "The Art of Disagreeing Without Burning Bridges",
        "theme": "Disagree with the idea, never the person. Win the room, not the fight.",
        "concepts": [
            "Acknowledge before you counter — it shows you listened",
            "Separate the person from the position",
            "Use 'and' instead of 'but' — 'but' negates everything before it",
            "Frame disagreement as adding perspective, not opposing",
            "Never make someone wrong publicly if you can avoid it",
        ],
        "phrase_bank": {
            "acknowledging_then_redirecting": [
                "I see the logic in that approach, and I'd like to offer an additional consideration.",
                "You raise a valid point. Let me build on it with a different angle.",
                "I appreciate that perspective. Here's what I'd add to the picture.",
                "That's one way to look at it. Here's another lens worth considering.",
                "I understand why you'd reach that conclusion. The piece I think we're missing is...",
            ],
            "challenging_assumptions": [
                "Let me pressure-test that assumption for a moment.",
                "What if we challenged the premise here?",
                "I'd like to play devil's advocate on one element.",
                "The data actually tells a slightly different story.",
                "I want to examine an assumption we might be making.",
            ],
            "standing_firm_gracefully": [
                "I've considered that, and I still believe the stronger position is...",
                "I hear you, and my conviction on this hasn't changed. Here's why.",
                "I respect the disagreement. My position remains the same, and here's my reasoning.",
                "We may not align on this. Let me lay out my case one more time.",
                "I understand the counterargument. I don't find it persuasive, and here's why.",
            ],
            "finding_common_ground": [
                "We agree on the destination. The question is the route.",
                "I think we're closer than it appears. The gap is really about...",
                "We're aligned on the 'what.' Let's work through the 'how.'",
                "There's a synthesis here that might serve both perspectives.",
            ],
        },
        "drills": [
            {
                "type": "reframe",
                "instruction": "Rewrite the aggressive disagreement as a powerful but diplomatic one",
                "items": [
                    ("That's completely wrong. The numbers clearly show we should go with Plan B.",
                     "I see why Plan A has appeal. And when I look at the numbers, they point strongly toward Plan B. Let me walk you through what I'm seeing."),
                    ("You obviously haven't thought this through. There are major flaws in this proposal.",
                     "There are aspects of this proposal that show real promise. I'd like to pressure-test a few elements that I think could strengthen it significantly."),
                    ("I disagree. That's not how it works.",
                     "I have a different read on this. My understanding is... Let me share the basis for that."),
                ],
            },
            {
                "type": "scenario",
                "instruction": "Craft a diplomatic response to each situation",
                "items": [
                    {"situation": "Your manager proposes a strategy you believe will fail.", "goal": "Disagree while maintaining the relationship."},
                    {"situation": "A peer dismisses your idea in front of the team.", "goal": "Reassert your position without escalating conflict."},
                    {"situation": "A client insists on a direction that's technically wrong.", "goal": "Redirect them without making them feel foolish."},
                    {"situation": "An executive makes a claim that contradicts your data.", "goal": "Correct the record respectfully."},
                ],
            },
        ],
        "daily_practice": "In every disagreement today, lead with genuine acknowledgment before stating your position. 'I see X, and here's what I'd add.'",
    },

    8: {
        "title": "Influence Without Authority",
        "theme": "The most powerful people in the room don't need a title to lead",
        "concepts": [
            "Influence is built on credibility, relationships, and framing",
            "Frame proposals in terms of what THEY gain, not what YOU want",
            "Use social proof: 'Companies like ours have found that...'",
            "Pre-wire important conversations — never surprise stakeholders",
            "Ask questions that lead people to your conclusion organically",
        ],
        "phrase_bank": {
            "framing_for_their_benefit": [
                "The benefit to your team would be...",
                "This directly supports the goal you've outlined for Q3.",
                "Here's how this helps you hit your numbers.",
                "This removes a bottleneck your team has been dealing with.",
                "I'm thinking about this from your perspective, and here's what I see.",
            ],
            "building_coalition": [
                "I've spoken with [name], and they see similar value in this approach.",
                "Several teams have flagged the same concern, which suggests this is systemic.",
                "There's growing alignment around this direction.",
                "The feedback I've gathered points consistently toward...",
                "I wanted to get your perspective before bringing this to the broader group.",
            ],
            "socratic_leading": [
                "What do you think would happen if we continued on the current path?",
                "What would success look like in an ideal scenario?",
                "If resources weren't a constraint, what would you choose?",
                "What's the one thing that would make the biggest difference here?",
                "What concerns you most about the status quo?",
            ],
            "creating_urgency": [
                "The window for this decision is closing. Here's why.",
                "Every week we delay costs us approximately...",
                "Our competitors are already moving in this direction.",
                "The cost of inaction is higher than the cost of the investment.",
                "If we don't act by [date], our options narrow significantly.",
            ],
        },
        "drills": [
            {
                "type": "reframe_for_audience",
                "instruction": "Reframe the same proposal for three different audiences",
                "items": [
                    {
                        "proposal": "We should invest in automated testing.",
                        "audiences": {
                            "CTO": "Automated testing reduces deployment risk and accelerates our release cadence, directly supporting our reliability SLAs.",
                            "CFO": "Automated testing reduces our cost of quality by 35% annually and cuts incident-related revenue loss.",
                            "Engineering team": "Automated testing means fewer 2am pages, faster feedback loops, and more time building features instead of fighting fires.",
                        },
                    },
                ],
            },
            {
                "type": "socratic_path",
                "instruction": "Design a sequence of 3-4 questions that lead someone to your desired conclusion without stating it directly",
                "items": [
                    "You want to convince your manager to approve budget for a new tool.",
                    "You want a peer to volunteer to lead a difficult project.",
                    "You want a client to agree to extend the timeline.",
                ],
            },
        ],
        "daily_practice": "Before making any request today, reframe it from the other person's perspective. What's in it for THEM?",
    },

    9: {
        "title": "Handling Tough Questions & Pushback",
        "theme": "Never be caught off guard. Control the frame, control the outcome.",
        "concepts": [
            "Bridge: acknowledge the question, pivot to your message",
            "Flagging: signal the structure of your answer ('There are two parts to this')",
            "Buying time gracefully: 'That's a critical question. Let me give you a precise answer.'",
            "Handling 'I don't know': 'I don't have that number at hand. I'll have it for you by EOD.'",
            "Dealing with hostile questions: reframe the premise, don't accept a loaded frame",
        ],
        "phrase_bank": {
            "bridging": [
                "That's an important question, and it connects to a broader point...",
                "I'd frame it slightly differently...",
                "The more fundamental issue is...",
                "Let me address that directly, and then broaden the lens.",
                "Yes, and the context that's important here is...",
            ],
            "buying_time": [
                "Let me give you a precise answer rather than an approximation.",
                "I want to do that question justice. Let me pull the exact figures.",
                "That deserves a thorough response. Let me come back to you by [time].",
                "Great question. Let me think about the right framing for a moment.",
            ],
            "handling_loaded_questions": [
                "I'd challenge the premise of that question.",
                "The framing assumes X, and I don't accept that assumption. Here's why.",
                "Let me reframe that, because the question itself contains an assumption worth examining.",
                "I think the more productive question is...",
                "Before I answer that, let me address what's underneath it.",
            ],
            "admitting_gaps_with_authority": [
                "I don't have that figure at hand. I'll have it for you by end of day.",
                "That's outside my direct expertise. Let me connect you with the right person.",
                "I'd rather give you an accurate answer than speculate. Let me follow up.",
                "Honestly, that's a gap in our analysis. I'll close it and circle back.",
            ],
            "deflecting_personal_attacks": [
                "I'd prefer to keep this focused on the substance.",
                "Let's stay on the merits of the argument.",
                "I'm happy to debate the idea. Let's keep it there.",
                "The issue at hand is... Let's focus on that.",
            ],
        },
        "drills": [
            {
                "type": "rapid_fire",
                "instruction": "Answer each question using the bridge technique in under 15 seconds",
                "items": [
                    "Why is your project behind schedule?",
                    "Don't you think this is too risky?",
                    "What makes you qualified to lead this initiative?",
                    "Isn't this just going to cost us more money?",
                    "Why should we trust this approach when the last one failed?",
                    "Can you guarantee this will work?",
                ],
            },
            {
                "type": "reframe_hostile",
                "instruction": "Reframe the loaded question before answering it",
                "items": [
                    ("Why did your team drop the ball on this?",
                     "Let me address what happened and, more importantly, what we're doing about it. The delay was driven by [X]. We've already implemented [Y] to prevent recurrence. Here's where we stand now."),
                    ("Isn't this just a waste of money?",
                     "The real question is whether the ROI justifies the investment. Let me walk you through the numbers, because they tell a compelling story."),
                    ("Don't you think someone more experienced should handle this?",
                     "What matters is whether we have the right capability for this challenge. Let me share the specific experience and results that are directly relevant here."),
                ],
            },
        ],
        "daily_practice": "Ask a colleague to throw difficult questions at you for 5 minutes. Practice bridging to your key message every time.",
    },

    # =========================================================================
    # PHASE 4: ADVANCED PRESENCE (Weeks 10-12) - Executive-level mastery
    # =========================================================================
    10: {
        "title": "Storytelling for Business Impact",
        "theme": "Data informs. Stories persuade.",
        "concepts": [
            "Every business argument is stronger wrapped in a narrative",
            "Structure: Setup (context) -> Conflict (problem) -> Resolution (your solution)",
            "Use concrete details — specifics are more credible than generalities",
            "Personal stories build trust; data stories build conviction. Use both.",
            "The most powerful stories are about a transformation — before vs. after",
        ],
        "frameworks": {
            "The Business Story Arc": [
                "1. Paint the current state: 'Six months ago, our team was...'",
                "2. Introduce the tension: 'Then we discovered...'",
                "3. Show the turning point: 'So we decided to...'",
                "4. Deliver the result: 'The outcome was...'",
                "5. Extract the lesson: 'What this taught us is...'",
            ],
            "The Contrast Frame": [
                "1. Show the 'without' scenario: 'Without this investment, we'll see...'",
                "2. Show the 'with' scenario: 'With it, we position ourselves to...'",
                "3. Make the choice obvious: 'The question is whether we can afford not to.'",
            ],
            "The Analogy Play": [
                "Complex ideas become simple through the right analogy",
                "'Asking engineering to add features without addressing tech debt is like adding floors to a building with a cracking foundation.'",
                "'Our current sales process is like using a map from 2015 to navigate a city that's been rebuilt.'",
            ],
        },
        "drills": [
            {
                "type": "story_build",
                "instruction": "Build a 60-second business story using the Story Arc framework",
                "items": [
                    "Convince the board to invest in a new market.",
                    "Explain to a team why a reorganization is necessary.",
                    "Persuade a client to renew their contract despite a service disruption.",
                    "Pitch a cost-cutting initiative to the CFO.",
                ],
            },
            {
                "type": "analogy_creation",
                "instruction": "Create a compelling analogy to explain the concept",
                "items": [
                    "Technical debt accumulating in a codebase",
                    "The importance of investing in employee onboarding",
                    "Why diversifying revenue streams matters",
                    "The risk of over-reliance on a single vendor",
                ],
            },
        ],
        "daily_practice": "Replace one data-only argument today with a data-wrapped-in-story format. Watch how people lean in.",
    },

    11: {
        "title": "Reading the Room & Political Intelligence",
        "theme": "The unspoken dynamics matter more than the spoken ones",
        "concepts": [
            "Every room has a power map — identify who really decides",
            "Watch for micro-expressions: crossed arms, broken eye contact, the 'look' between two people",
            "Silence after your point = agreement or processing. Silence + eye shifting = resistance.",
            "Know when to push and when to table — reading resistance saves credibility",
            "Pre-meetings matter more than meetings. Align key stakeholders before the room.",
        ],
        "phrase_bank": {
            "reading_resistance": [
                "I'm sensing some hesitation. What concerns are we not addressing?",
                "I'd like to pause and check — are we aligned on this direction?",
                "I notice we might have different views on this. Let's surface them.",
                "Before we move forward, I want to make sure we've addressed any reservations.",
            ],
            "navigating_politics": [
                "I wanted to run this by you before the meeting so there are no surprises.",
                "I'd value your input before I present this to the group.",
                "I know you have strong views on this, and I want to make sure they're represented.",
                "Can I get your read on how this will land with [stakeholder]?",
            ],
            "adjusting_in_real_time": [
                "I can see this needs more discussion. Let me suggest we...",
                "Given the room's energy, I think the most productive next step is...",
                "Let me take a different approach to this.",
                "I think we've hit the point of diminishing returns on this discussion. Here's what I'd suggest.",
            ],
        },
        "drills": [
            {
                "type": "scenario",
                "instruction": "Read the situation and determine the best course of action",
                "items": [
                    {"situation": "You're presenting a proposal. The VP is checking their phone, and two directors exchanged a glance after your key slide.", "goal": "Recover the room's attention and address unspoken resistance."},
                    {"situation": "A colleague publicly supports your idea but privately tells others it won't work.", "goal": "Address the misalignment without creating a confrontation."},
                    {"situation": "You realize mid-presentation that the decision has already been made against your proposal.", "goal": "Pivot gracefully and preserve your credibility."},
                    {"situation": "Two senior leaders in the room have a known disagreement on this topic.", "goal": "Navigate the political dynamic without taking sides prematurely."},
                ],
            },
        ],
        "daily_practice": "In your next meeting, focus entirely on observing. Note who speaks, who defers, who checks in with whom before responding. Map the power dynamics.",
    },

    12: {
        "title": "Executive Presence Under Pressure",
        "theme": "Grace under fire is the ultimate test of gravitas",
        "concepts": [
            "Crisis communication: be first, be honest, be in control",
            "The SCQA framework: Situation, Complication, Question, Answer",
            "Emotional regulation: your calm IS the message in high-stakes moments",
            "When things go wrong, the leader who steps forward with clarity wins trust",
            "Your reputation is built in the hard moments, not the easy ones",
        ],
        "phrase_bank": {
            "crisis_communication": [
                "Here's what we know. Here's what we don't. Here's what we're doing.",
                "I'm going to be transparent about the situation.",
                "Let me give you the facts, then the plan.",
                "This is a serious issue, and I want you to know it has my full attention.",
                "We don't have all the answers yet, and I won't speculate. What I can tell you is...",
            ],
            "high_stakes_composure": [
                "Let's take a step back and look at this clearly.",
                "I understand the urgency. Let me outline our options.",
                "Reacting quickly and reacting well are different things. Let me suggest we...",
                "I want to make sure we respond rather than react.",
                "The most important thing right now is...",
            ],
            "delivering_difficult_messages": [
                "I'm going to be direct because you deserve clarity.",
                "This is a difficult conversation, and I want to have it honestly.",
                "I owe you candor on this.",
                "The straightforward answer is... and here's why.",
                "I'd rather tell you this directly than have you hear it another way.",
            ],
            "recovering_from_mistakes": [
                "I made an error in judgment. Here's what I've learned and what I'm doing differently.",
                "I own this. Here's my plan to make it right.",
                "Let me be upfront — I got this wrong. Here's the correction.",
                "I should have handled this differently. Here's my course correction.",
            ],
        },
        "masterclass_scenarios": [
            {
                "situation": "The board asks why the company missed revenue targets. All eyes are on you.",
                "principles": ["Lead with accountability", "Show you understand root causes", "Present a credible recovery plan", "Project confidence without arrogance"],
            },
            {
                "situation": "A major client threatens to leave during a live call.",
                "principles": ["Stay calm — your energy sets the tone", "Acknowledge their frustration genuinely", "Don't make promises you can't keep", "Commit to specific next steps and follow through"],
            },
            {
                "situation": "You're asked to present with zero preparation in front of senior leadership.",
                "principles": ["Use the Rule of Three to structure on the fly", "Lead with what you know, not what you don't", "Project composure even if you feel unprepared", "Keep it short — better to be brief and confident than long and rambling"],
            },
        ],
        "drills": [
            {
                "type": "rapid_fire",
                "instruction": "You have 20 seconds to respond to each crisis scenario. Go.",
                "items": [
                    "A data breach has been discovered. The press is calling. What do you say to your team?",
                    "A key employee just resigned publicly on social media. Stakeholders are asking questions.",
                    "Your product launch failed. The CEO wants an explanation in the next meeting.",
                    "A competitor just undercut your pricing by 40%. The sales team is panicking.",
                ],
            },
            {
                "type": "composure_challenge",
                "instruction": "Deliver each message with complete calm and authority. Record yourself.",
                "items": [
                    "Tell a team of 50 people that there will be layoffs.",
                    "Tell a client that a project will be delivered 3 months late.",
                    "Tell your board that you're recommending a complete strategy pivot.",
                    "Address your team after a public failure.",
                ],
            },
        ],
        "daily_practice": "Think of the hardest conversation you're avoiding. Write your opening three sentences. Deliver them to the mirror with composure. Then go have the real conversation.",
        "final_assessment": {
            "description": "The Gravitas Gauntlet — your 12-week final exam",
            "challenges": [
                "Deliver a 2-minute impromptu brief on a random business topic (Rule of Three, BLUF, no filler)",
                "Handle 5 rapid-fire hostile questions using bridging and reframing",
                "Disagree with a position diplomatically using acknowledge-redirect",
                "Deliver bad news with composure and a recovery plan",
                "Tell a 60-second business story that persuades",
                "Give a 30-second executive summary of a complex situation",
            ],
        },
    },
}


# Weekly schedule template
WEEKLY_SCHEDULE = {
    "monday": {"focus": "Learn new concepts", "time": "30 min", "activity": "Study the week's concepts and phrase bank"},
    "tuesday": {"focus": "Phrase drilling", "time": "20 min", "activity": "Memorize and practice power phrases aloud"},
    "wednesday": {"focus": "Interactive drills", "time": "25 min", "activity": "Complete the week's drill exercises"},
    "thursday": {"focus": "Real-world application", "time": "All day", "activity": "Apply techniques in actual conversations/meetings"},
    "friday": {"focus": "Review and reflect", "time": "15 min", "activity": "Journal what worked, what didn't, plan next week"},
    "weekend": {"focus": "Reinforcement", "time": "10 min/day", "activity": "Review phrase cards, practice delivery in mirror"},
}


# Progression milestones
MILESTONES = {
    3: {
        "name": "Foundation Complete",
        "you_should_be_able_to": [
            "Speak for 2 minutes with zero filler words",
            "Use downward inflection consistently",
            "Structure any argument in BLUF format",
            "Use the Rule of Three automatically",
            "Pause for 2-3 seconds after key points without discomfort",
        ],
    },
    6: {
        "name": "Executive Communicator",
        "you_should_be_able_to": [
            "Command a meeting within the first 5 minutes",
            "Deliver a 30-second executive summary on any topic",
            "Use strategic framing to elevate tactical conversations",
            "Handle interruptions with composure and authority",
            "Speak in terms of business impact, not just activities",
        ],
    },
    9: {
        "name": "Influence Master",
        "you_should_be_able_to": [
            "Disagree diplomatically without damaging relationships",
            "Reframe hostile or loaded questions in real time",
            "Influence decisions even without direct authority",
            "Bridge from tough questions to your key message seamlessly",
            "Tailor the same message for different audiences instinctively",
        ],
    },
    12: {
        "name": "Executive Presence",
        "you_should_be_able_to": [
            "Maintain composure under pressure — your calm IS the message",
            "Command any room regardless of seniority dynamics",
            "Deliver impromptu briefs that are structured and compelling",
            "Navigate organizational politics with intelligence and grace",
            "Tell business stories that move people to action",
            "Recover from mistakes with authority and accountability",
        ],
    },
}
