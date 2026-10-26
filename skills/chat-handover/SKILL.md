---
name: chat-handover
description: >
  Generates a structured handover artefact to continue a conversation in a new chat thread
  when the current chat is approaching its context limit. Triggers on: "handover", "chat
  handover", "context limit reached", "continue in new chat", "extension", "capacity limit",
  "start a new chat", "transfer context", "pick up where we left off", or any signal that
  the conversation needs to migrate. Also triggers proactively when a chat has had 10 or
  more back-and-forth exchanges and the user is mid-task — suggest a handover before hitting
  the limit, not after. Always use this skill rather than attempting an ad hoc summary.
---

# Chat Handover Skill

Produces a copyable handover artefact — formatted as the opening prompt for the next chat
thread. The new chat will be in the same Claude Project, so project instructions and the
user's custom preferences are already loaded. The artefact must not repeat them.

Key principle from research: do this at 70-80% context capacity, not at the wall. A handover
done with breathing room captures more nuance than a panic summary.

---

## Trigger Recognition

Activate when:
- User says any variant of: "handover", "context limit", "new chat", "extension", "capacity"
- The conversation has 10+ exchanges AND the user is mid-task (suggest proactively)
- Claude notices it is running long and the task is not yet complete

Do NOT activate for: one-off questions, short tasks already resolved, or if the user says
they are done with this chat.

---

## Workflow

### Step 0 — Assess Before Writing

Scan the full conversation. Identify:
- The primary task / goal of this chat
- What has been completed vs. what remains
- Any instructions the user gave for specific process steps
- Open questions or unresolved items
- External files, links, or artefacts referenced
- What must carry forward vs. what is background noise

Filter ruthlessly. The handover is for continuation, not archiving.

---

### Step 1 — Build the Artefact

Write a single copyable block formatted as a prompt to be pasted into the new chat.
Use the structure below. Sections 4 and 5 are optional — include them only if there
is genuine content. Do not include empty section headings.

Use plain text throughout (no markdown headers, no bullet symbols that render oddly).
The user will paste this directly into a new chat — it must read as a natural opening prompt,
not a formatted document.

---

## Artefact Template

```
CONTINUING FROM PREVIOUS CHAT — [brief topic label, e.g. "Budget process build" or "API integration"]

You are [role from previous chat — e.g. "an expert operations advisor" or "a senior software engineer"].

CONTEXT
We were working on [1-2 sentence summary of what this chat was about — goals only, not history].

WHAT WE COMPLETED
[Bullet list of things actually finished or decided in the previous chat. Be specific — include outputs, file names, decisions made, approaches confirmed.]

NEXT STEPS — PICK UP FROM HERE
[Numbered list of the immediate next actions, in order. This is the most important section. Be specific enough that the new chat can act without asking clarifying questions.]

[SECTION: PROCESS INSTRUCTIONS — include only if the user gave detailed step-by-step instructions during the chat that will be repeated or continued]
PROCESS INSTRUCTIONS
[Reproduce in full fidelity any workflow, process steps, decision rules, or formatting instructions the user specified. These must be exact — paraphrasing loses critical detail.]

[SECTION: OPEN QUESTIONS — include only if there are unresolved issues that need addressing]
OPEN QUESTIONS
[List each unresolved question or decision point. For each, briefly explain why it matters and what is blocking resolution.]

[SECTION: REFERENCES — include only if there are files, links, or artefacts that must carry forward]
REFERENCES
[For each item: name / description / URL or file path / why it is relevant to the next steps. Include document URLs, file IDs, task links, artefact names.]

END OF HANDOVER — continue from Next Steps above.
```

---

### Step 2 — Quality Check Before Presenting

Before presenting the artefact, verify:

[ ] Contains no project instructions (system prompt content, standing rules, skill descriptions)
[ ] Contains no generic custom preferences (British English, formatting rules, output style)
[ ] Every item in "What We Completed" is actually done — not aspirational
[ ] "Next Steps" are specific enough to act on without re-reading the original chat
[ ] "Process Instructions" reproduce the user's exact words, not a paraphrase
[ ] All URLs are real links from the conversation — no invented ones
[ ] No section is a padded restatement of another section
[ ] The artefact reads as a prompt, not a report

If any check fails, revise before presenting.

---

### Step 3 — Present

Output the artefact inside a clear boundary:

```
--- HANDOVER ARTEFACT — copy everything below this line ---

[artefact content]

--- END OF ARTEFACT ---
```

Then add a one-line note of anything the artefact could not carry (e.g. uploaded files
that will need re-attaching, or context that was too implicit to summarise faithfully).

---

## Design Notes (rationale)

Structure based on:
- Anthropic's own guidance (support.claude.com): do the handover before the limit, not at it.
  "Better timing: around 70-80% capacity." Context window summarisation drops nuance.
- Claude API best practices (platform.claude.com, May 2026): "Use a different prompt for
  the very first context window" — the handover IS that different first prompt. Frame it
  as the opening instruction, not a history dump.
- Community practice (jdhodges.com, May 2026): HANDOVER.md pattern — two files (state + narrative).
  This skill merges both into one copyable block for chat-based workflows.
- Key finding: the handover artefact must be framed as the prompt to be typed into the new chat,
  not as a summary. That distinction is what makes it usable without editing.

What does NOT carry across:
- Project instructions (already loaded in the new chat automatically)
- The user's custom preferences (same)
- Resolved tangents with no bearing on next steps
- Raw conversation transcript

What MUST carry across:
- Exact process instructions the user specified during the chat
- Specific file IDs, URLs, task IDs (not just "the spreadsheet")
- Decisions made (especially ones that ruled out alternatives)
- Unresolved blockers (the new chat will re-derive the wrong answer without them)

---

## Edge Cases

Short chats with no unresolved tasks: output a one-paragraph summary instead of the
full artefact. Note: "This chat is self-contained — no handover needed unless you want
a record of decisions made."

Chats involving sensitive content (personnel, legal, financial disputes): flag any
section that contains sensitive details and ask the user whether to include or redact
before presenting.

Chats with large uploaded files: note in the References section that files will need
re-attaching. The handover cannot transfer binary content.

Multiple simultaneous threads: if the chat touched several unrelated topics, produce
one artefact per distinct thread, clearly labelled.
