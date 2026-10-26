---
name: skill-enhancer
description: Audit and sharpen ONE existing skill against Nick's own quality bar, without the eval/benchmark machinery skill-creator uses. Use when Nick says "upgrade this skill", "sharpen this skill", "audit this skill", "make this skill better", or pastes an existing SKILL.md and wants it strengthened. Applies Nick's voice and format preferences automatically, checks for overlap or naming clashes against his existing skill library, and applies the [CC] tag when a skill needs Code or Cowork tools (bash, filesystem, subagents). Does NOT create new skills from scratch and does NOT run test cases, subagent benchmarking, or description-optimisation loops — for those, defer to skill-creator. One skill at a time, never a batch pass across the whole library unless Nick explicitly asks for that.
---

# Skill Enhancer

A fast, opinionated companion to skill-creator. skill-creator is the general-purpose
build-and-validate framework (new skills, eval loops, benchmarking) and stays
current via Anthropic updates — don't fork or duplicate that logic here.
skill-enhancer exists for the narrower job: take one skill Nick already has and
make it sharper in a single pass, tuned to his standards, in a couple of minutes.

If the request is "build me a new skill for X" or "run evals on this skill" or
"optimise this skill's trigger rate", stop and point to skill-creator instead.

## When this triggers

- Nick pastes an existing SKILL.md and asks for it to be improved
- Nick names one skill from his library by name and asks to upgrade it
- Nick says "sharpen", "audit", "tighten up" about a specific skill

Never trigger this on more than one skill per request unless Nick explicitly
says "do all of them" or "batch upgrade" — default is one skill, one pass.

## Process

### Step 1: Get the skill

If Nick pasted it, use that. If he named it, read it from wherever it lives
(his /mnt/skills/user/ directory if working in Code/Cowork, or ask him to
paste it if working in claude.ai chat with no filesystem access).

### Step 2: Audit hard

Go through the skill and flag, specifically:

- Where is it vague? (instructions that could be read two ways)
- Where is it incomplete? (missing context, undefined terms, no edge cases)
- Does it have a concrete output format spelled out?
- Does it have at least one worked example of a good result?
- Does it say what it should never do?
- Does its description name specific trigger phrases, or is it generic enough
  to under-trigger?

### Step 3: Check portability only if running headless

Nick's standing style preferences (British English, no em dashes, banned
words, confidence percentages, hyperlinks, plain text) already apply to
everything produced in claude.ai chat — no need to restate them here.

The only case this step matters: if skill-enhancer is invoked by a subagent
in Code/Cowork with no access to Nick's claude.ai preferences, briefly note
in the output that style compliance wasn't auto-enforced and Nick should
spot-check it. Otherwise skip this step entirely.

### Step 4: Check against the library

Before finalising, scan Nick's current skill list (from the memory listing or
a fresh `ls` of his skills directory) for:

- Name collisions or near-duplicate slugs
- Alias clashes (two skills that would both plausibly trigger on the same phrase)
- Functional overlap worth flagging (not necessarily merging — just flag it
  and let Nick decide)

### Step 5: CC-suffix if needed

If the skill requires bash, filesystem access, or subagents to function
(i.e. genuinely breaks in plain claude.ai chat), the name/slug should end in
"-cc" (e.g. job-scanner-cc). If it works fine in chat-only mode, leave
untagged. Don't tag skills just because they *could* use Code/Cowork — only
when they have a hard dependency.

New skill being built from scratch: apply the -cc suffix directly, no need
to ask.

Existing skill being audited: flag that it should carry -cc and ask Nick to
confirm before renaming. Renaming an installed skill's slug breaks any
alias or automation already pointing at the old name — never do this
silently (see "must never do" below).

### Step 6: Deliver

Output format, always:

1. One line: what the skill is for (sanity check that the audit understood it)
2. Bullet list: what was wrong (the audit findings from Step 2)
3. The full rewritten SKILL.md, clean and copy-paste-ready, as its own block
4. Bullet list: what changed and why it performs better
5. Flag: any overlap or naming clash found in Step 4, with the specific
   skill name it clashes with
6. One dated changelog line appended to `changelog.md` in this skill's own
   directory (create it if it doesn't exist), e.g.:
   `2026-09-01: sharpened output format, added CC tag, fixed alias clash with job-application-writer`

## What this skill must never do

- Never batch-process the whole library without explicit instruction
- Never run eval loops, spawn subagents for benchmarking, or claim to have
  measured performance — this is a structured audit, not a validated one
- Never silently rename an existing skill or change its slug (breaks aliases
  and any automation pointing at it)
- Never drop Nick's stated preferences to save space
- Never invent a hyperlink for a tool or source that wasn't verified

## Example

Input: a skill with a vague description ("helps with expenses"), no output
format, no examples, American spelling throughout.

Output: one-line purpose restated, audit flags (generic description under-
triggers, no format spec, no do-nots, spelling), full rewrite with a named
output format, change summary, no library clashes found, a flag asking
whether to rename it expenses-cc (it shells out to bash for CSV parsing),
changelog line appended once Nick confirms.
