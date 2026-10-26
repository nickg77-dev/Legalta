---
name: council
description: >-
  Convene four advisor voices (Architect, Skeptic, Pragmatist, Critic) for
  ambiguous decisions with multiple credible paths. Use when a decision has no
  obvious winner, you need tradeoffs surfaced, or conversational anchoring is a
  risk. Triggers on phrases like "help me decide", "I need a second opinion",
  "ship now vs wait", or any go/no-go call that would benefit from adversarial
  challenge. Do NOT use for code review, implementation planning, architecture
  design, or factual questions.
---

# Council

Convene four advisors for ambiguous decisions:

- the in-context Claude voice (Architect)
- a Skeptic subagent
- a Pragmatist subagent
- a Critic subagent

This is for decision-making under ambiguity, not code review, implementation planning, or architecture design.

## When to Use

Use council when:

- a decision has multiple credible paths and no obvious winner
- you need explicit tradeoff surfacing
- the user asks for second opinions, dissent, or multiple perspectives
- conversational anchoring is a real risk
- a go / no-go call would benefit from adversarial challenge

Examples: monorepo vs polyrepo, ship now vs hold for polish, feature flag vs full rollout, simplify scope vs keep strategic breadth.

## When NOT to Use

Instead of council for verifying output correctness, use santa-method.
Instead of council for implementation steps, use planner.
Instead of council for architecture design, use architect.
Instead of council for code review, use code-reviewer.
For factual questions or obvious execution tasks: just answer directly.

## Roles

- Architect: correctness, maintainability, long-term implications
- Skeptic: premise challenge, simplification, assumption breaking
- Pragmatist: shipping speed, user impact, operational reality
- Critic: edge cases, downside risk, failure modes

The three external voices should be launched as fresh subagents with only the question and relevant context, not the full ongoing conversation. That is the anti-anchoring mechanism.

## Workflow

### 1. Extract the real question

Reduce the decision to one explicit prompt: what are we deciding, what constraints matter, what counts as success. If the question is vague, ask one clarifying question before convening the council.

### 2. Gather only the necessary context

If codebase-specific: collect relevant files, snippets, issue text, or metrics - keep it compact. If strategic/general: skip repo snippets unless they materially change the answer.

### 3. Form the Architect position first

Before reading other voices, write down your initial position, the three strongest reasons for it, and the main risk in your preferred path. Do this first so the synthesis does not simply mirror the external voices.

### 4. Launch three independent voices in parallel

Each subagent gets: the decision question, compact context if needed, a strict role, and no unnecessary conversation history.

Prompt shape:

You are the [ROLE] on a four-voice decision council.

Question: [decision question]

Context: [only the relevant snippets or constraints]

Respond with:
1. Position - 1-2 sentences
2. Reasoning - 3 concise bullets
3. Risk - biggest risk in your recommendation
4. Surprise - one thing the other voices may miss

Be direct. No hedging. Keep it under 300 words.

Role emphasis:
- Skeptic: challenge framing, question assumptions, propose the simplest credible alternative
- Pragmatist: optimize for speed, simplicity, and real-world execution
- Critic: surface downside risk, edge cases, and reasons the plan could fail

### 5. Synthesize with bias guardrails

- do not dismiss an external view without explaining why
- if an external voice changed your recommendation, say so explicitly
- always include the strongest dissent, even if you reject it
- if two voices align against your initial position, treat that as a real signal
- keep the raw positions visible before the verdict

### 6. Present a compact verdict

## Council: [short decision title]

**Architect:** [1-2 sentence position]
[1 line on why]

**Skeptic:** [1-2 sentence position]
[1 line on why]

**Pragmatist:** [1-2 sentence position]
[1 line on why]

**Critic:** [1-2 sentence position]
[1 line on why]

### Verdict
- **Consensus:** [where they align]
- **Strongest dissent:** [most important disagreement]
- **Premise check:** [did the Skeptic challenge the question itself?]
- **Recommendation:** [the synthesized path]

Keep it scannable on a phone screen.

## Persistence Rule

Do not write ad-hoc notes to shadow paths from this skill. Only persist a decision when it materially changes something real - use knowledge-ops, /save-session, or update the relevant issue directly.

## Multi-Round Follow-up

Default is one round. If the user wants another round: keep the new question focused, include the previous verdict only if necessary, keep the Skeptic as clean as possible to preserve anti-anchoring value.

## Anti-Patterns

- using council for code review
- using council when the task is just implementation work
- feeding subagents the entire conversation transcript
- hiding disagreement in the final verdict
- persisting every decision as a note regardless of importance
