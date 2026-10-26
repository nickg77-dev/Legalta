---
name: brainstorming
description: Use before building anything substantive - documents, spreadsheets, automations, workflows, SOPs, dashboards, outreach campaigns, code or artefacts. Triggers on "brainstorm", "help me design", "what are my options for", "ideas for", "let's build", "create a", "I want to make", or any described deliverable that still has open decisions (audience, format, scope). Clarifies through one-at-a-time questions, generates and scores 10 approaches, shortlists the best 3-5, presents a short design for approval, then builds. Do NOT trigger for questions, single edits, edits to an already approved design, single-fact requests, or fully specified requests. When Nick already has the options and needs help choosing between them, use council instead.
---

# Brainstorming Ideas Into Designs

Turn a rough idea into an approved design before building. No building, drafting, file creation, or tool calls that create or modify anything until Nick approves the design.

If Nick says "skip brainstorm" or "just build it": state in one line what you will assume, then build.

## Stakes check (do this first, say which you picked)

- **LOW** (reversible in under 10 minutes, internal only, no money, people or client-facing decisions): one message with up to 3 clarifying questions together, your recommended approach and one alternative. Say: "Low stakes - recommending speed over polish." One approval, then build. Target: two messages of overhead.
- **STANDARD** (everything else): full process below.
- **TOO BIG** (several independent deliverables, e.g. "set up our whole Italy outreach"): propose a decomposition with a build order. Brainstorm only the first piece.

Anything client-facing (claimants, hauliers, municipalities) is never LOW. Unsure between LOW and STANDARD: pick STANDARD.

## Full process (STANDARD)

1. **Explore context.** Check the conversation, project knowledge, memory and connected tools (Drive, Gmail) before asking anything. Never ask a question the context already answers.

2. **Clarify.** One question per message, maximum four in total. Use lettered multiple choice (A/B/C) with a "something else" option, and make every option genuinely distinct. Each question must target purpose, audience, constraints (time, tools, budget) or success criteria. If an answer exposes an untested assumption, name it. Still uncertain after four questions: move on and label your assumptions.

3. **Generate 10, score, shortlist 3-5.**
   - **Generate** 10 approaches silently. Each must use a different mechanism (tool, format, workflow or owner); reworded duplicates count as one. If fewer than 10 genuinely distinct approaches exist, say how many you found and why. Never pad with filler.
   - **Score** each 1-5 per criterion, using the anchors, then weight:

     | Criterion | Weight | 1 | 3 | 5 |
     |---|---|---|---|---|
     | Goal fit | x3 | Misses a success criterion | Meets most criteria | Meets all criteria |
     | Effort | x2 | Weeks, or skills the team lacks | Days | Hours, with existing tools |
     | Risk | x2 | Compliance, legal or reputational exposure | Reversible with some rework | Fully reversible, internal only |
     | Cost | x1 | New paid tool or contractor | Small add-on spend | No new spend |
     | Confidence | x1 | Untested idea | Worked elsewhere | Already worked for Legalta |

     Maximum 45. Risk 1 = out, whatever the total. Tie-break: higher Goal fit, then higher Effort score.
   - **Shortlist** the top 3. Add a 4th and 5th only if each scores 30 or more and sits within 5 points of the top score. If fewer than 3 survive the Risk filter, say so and generate replacements.
   - **Present** in the format below, then ask: "Go with [recommendation], or pick another?" Wait for Nick's choice before step 4.

4. **Present the design** for the chosen approach:
   - **Goal:** one sentence
   - **Deliverable:** format, filename in house convention ("Subject - Artefact Type - YYYY MMM DD", no underscores), destination
   - **Structure:** sections, tabs or steps, one line each
   - **Decisions made:** each choice with its reason; anything Nick has not confirmed is labelled "Assumption"
   - **Out of scope:** at least one deliberate cut (YAGNI)
   - **Risks:** max three, each with a mitigation

   Cap the whole design at 300 words. Ask: "Approve, or what should change?"

5. **Build.** Only on clear approval ("approved", "go ahead", "looks good"). Hedged replies ("maybe", "I think so") or silence are not approval: ask once more. If Nick requests changes, revise only the affected sections and re-present those. When building, apply the matching polish skill (excel-polish for spreadsheets, doc-polish for documents, humanise-writing for public-facing copy).

## Shortlist format

| # | Approach | How it works | Fit | Effort | Risk | Cost | Conf | Score | Main trade-off |
|---|---|---|---|---|---|---|---|---|---|

Then three lines:
- **Recommended:** #1, and why in one sentence.
- **Strongest case against:** the best argument for not choosing it.
- **Discarded:** count, names and the main reason. All 10 shown only if Nick asks.

## Example: LOW stakes run

Nick: "Make me a tracker for the Italy fleet letters."

> Low stakes - recommending speed over polish. Two questions: (A) just you, or Thomas and Arlind too? (B) track replies only, or through to signed claim? Recommended: one Google Sheet, one row per haulier, columns for letter date, response, next action, owner. Alternative: add a contact log tab. Approve?

Nick: "Whole team, through to signed. Go."

> [Builds it.]

## Example: STANDARD shortlist (illustrative scores)

Goal: choose how to source the first list of Italian hauliers to contact.

| # | Approach | How it works | Fit | Effort | Risk | Cost | Conf | Score | Main trade-off |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Public register, manual scoring | Export the public haulier register, score by fleet size | 4 | 4 | 5 | 5 | 4 | 39 | Slow to enrich contacts |
| 2 | Trade association referrals | Partner with a regional association for introductions | 5 | 2 | 4 | 4 | 3 | 34 | Weeks to set up |
| 3 | Paid data vendor list | Buy an enriched fleet-owner list | 4 | 5 | 3 | 2 | 3 | 33 | Spend and data-quality risk |

- **Recommended:** #1 - no spend, fully reversible, and the team can start today.
- **Strongest case against:** the register gives company names without decision-makers, so outreach may stall at the switchboard.
- **Discarded:** 7, mainly low Goal fit; unsolicited bulk email scored Risk 1 on consent exposure.

Go with #1, or pick another?

## Example: STANDARD design (excerpt)

**Goal:** One sheet Thomas can scan in two minutes to pick the next municipal outreach wave.

**Deliverable:** Google Sheet, "Legalta Municipal Outreach - Wave Prioritisation - 2026 OCT 13", shared Legalta Drive.

**Structure:** Shortlist tab (one row per municipality, priority score, one-line rationale), Sources tab.

**Decisions made:** score on fleet size and truck purchases within the cartel period, because those drive potential claim size. Assumption: purchase data is available from public procurement records.

**Out of scope:** contact details, letter drafting.

**Risks:** procurement records may be incomplete for older years - mark gaps as unknown rather than estimating.

## Never do

- Never build, scaffold or create files before explicit approval.
- Never ask more than one question per message or four in total (LOW stakes batching excepted).
- Never invent requirements, scores or evidence; label assumptions as assumptions.
- Never shortlist a strawman or an option you would refuse to build.
- Never skip the stakes check, the scoring or the out-of-scope section.
- Never pad the design with generic sections that add nothing to this deliverable.
- Never design client-facing content that implies a guaranteed outcome or legal advice.
