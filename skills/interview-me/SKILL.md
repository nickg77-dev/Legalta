---
name: "interview-me"
description: "Iteratively interview the user to define a plan or specification from scratch, round after round, until it has enough detail to build from. Use for 'interview me', 'help me spec this', 'define the plan'."
---

# Interview Me

Use this to build a specification with the user through repeated rounds of questions. It ends when the spec is detailed enough to build from, not after a fixed number of rounds.

This skill is for defining a new plan. To challenge or stress-test a plan that already exists, use anti-sycophancy or council instead.

## Overrides

- While this skill is active, the standing "max 4 clarifying questions" limit is suspended. There is no round cap. The limit per round is 4 questions, which is the AskUserQuestion tool's maximum.
- The user can stop at any point by saying "enough", "stop" or "build it". When they do, go straight to Step 5.

## Step 1: Frame

1. Before asking anything, gather what is already available: attached files, connected docs, earlier conversation and memory. Never ask for something you could look up.
2. Write a one-line draft goal and pick the spec type: deliverable or document, software or tool, process or workflow, campaign or outreach, decision, or other.
3. Build the coverage checklist. It is the core list plus the add-ons for that type.

Core checklist:

- Goal and why now
- Primary user or audience
- Success measure: how we will know it worked
- Scope in
- Scope out
- Constraints: time, budget, tools, people, legal
- Inputs and dependencies
- Output format and where it lives
- Owner and decision-maker
- Key risks

Type add-ons:

- Deliverable or document: structure, tone, length, reviewers
- Software or tool: core user flows, data, integrations, platform, edge cases, maintenance
- Process or workflow: trigger, steps and handoffs, tools, frequency, exceptions
- Campaign or outreach: target segment, channel, message, volume, compliance, tracking
- Decision: options, criteria and their weights, reversibility, deadline

4. Show the user the draft goal and the checklist with every item marked open. Then start Round 1 in the same turn.

## Step 2: Ask a round

Use the AskUserQuestion tool. If the tool is not available, ask the same questions as a numbered list in plain text.

- Ask 1-4 questions per round. Choose the open items with the highest impact first: the ones where the answer would most change what gets built.
- Questions in the same round must not depend on each other. Save any follow-up for a later round.
- Each question covers one decision. Keep it neutral, never leading.
- Give 2-4 concrete options that reflect real trade-offs.
- If one option is clearly better, put it first, label it "(Recommended)" and give the reason in its description.
- Use multiSelect when the options are not mutually exclusive.
- Use previews when the user is choosing between layouts, formats or wording.
- Do not ask about anything low-impact. Make an assumption and record it instead.

## Step 3: Update the running spec

After each round, show a compact running spec of 15 lines or fewer:

- Each checklist item, marked settled, assumed or open, with its one-line answer
- New open items raised by the answers
- Any contradiction with an earlier answer, flagged explicitly and never resolved silently
- One line giving your confidence that the spec is buildable, as a percentage

If an "Other" free-text answer is ambiguous, turn it into a follow-up question in the next round. Do not guess what it meant.

## Step 4: Decide whether to continue

The spec is sufficient when all of these are true:

- Every core item is settled, or is assumed and the user has accepted the assumption
- No open item would change the build materially
- Success can be tested

If the spec is not sufficient, return to Step 2.

Every 5 rounds, check whether returns are falling. If so, offer to stop: name what is still open and the assumption you would make for each item.

## Step 5: Output

1. Write the final spec. Default to a doc; ask about format only if the user has a standing preference.
2. Name it "<Subject> - Specification - YYYY MMM DD".
3. Include these sections:
   - Goal
   - Audience
   - Success measures
   - Scope in and out
   - Requirements
   - Constraints
   - Inputs
   - Output
   - Owner
   - Assumptions, each labelled as an assumption
   - Risks
   - Open questions
4. Each item appears in one section only.
5. End by asking for a go or no-go. Do not start building until the user approves.

## Style

- Use British English.
- Use hyphens with spaces, never em or en dashes.
- Keep text short and outputs concrete.
- Label unverified claims as unverified.