---
name: prompt-refiner
description: Refine and strengthen prompts using Anthropic's 10-component framework and context engineering principles. Trigger when user says "refine this prompt", "improve my prompt", "strengthen this", "make this prompt better", "prompt help", or asks for prompt options/variations. Also triggers when user shares a draft prompt and asks for feedback or alternatives.
---

# Prompt Refiner

Transform vague or underperforming prompts into structured, high-signal prompts that produce consistent, quality outputs.

## Core Principle: Context Engineering

Context is finite. Every token competes for attention. Goal: smallest set of high-signal tokens that maximises desired outcome.

Claude 4.x models take instructions literally - they do exactly what you ask, nothing more. Vague = vague output.

## Refinement Process

### 1. Diagnose the Original Prompt

Identify which problems exist:
- Missing context (WHO is this for? WHY does it matter?)
- Vague instructions (what does "good" mean specifically?)
- No output format specified
- No examples provided
- Missing constraints or guardrails
- Assumed shared knowledge Claude doesn't have

### 2. Apply the 10-Component Framework

Not all components needed for every prompt. Select based on complexity.

| Component | Purpose | When Essential |
|-----------|---------|----------------|
| 1. Task Context | WHO Claude is, WHAT role | Always |
| 2. Tone Context | HOW to communicate | When tone matters |
| 3. Background Data | Documents, data, context | When external info needed |
| 4. Detailed Task Description | Rules, requirements, constraints | Complex tasks |
| 5. Examples | 1-3 input/output pairs | Format-sensitive tasks |
| 6. Conversation History | Prior context if relevant | Multi-turn workflows |
| 7. Immediate Task | Specific deliverable NOW | Always |
| 8. Thinking Instructions | "Think step by step" | Complex reasoning |
| 9. Output Format | Structure, length, style | Always |
| 10. Prefilled Response | Start Claude's answer | Steering tone/format |

### 3. Present Options

Always offer 3 variations:

**Option A - Minimal (Low context overhead)**
Essential components only. Use when: simple tasks, token budget tight, fast iteration.

**Option B - Standard (Balanced)**
Core framework with examples. Use when: typical professional tasks, moderate complexity.

**Option C - Comprehensive (Maximum steering)**
Full framework with examples, guardrails, self-check. Use when: production prompts, critical outputs, complex reasoning.

## Refinement Patterns

### Pattern 1: Add Motivated Instructions
Before: "Never use bullet points"
After: "Write in flowing prose paragraphs. The output will be pasted into a formal report where bullet points would break the document style."

Why it matters: Claude generalises better when it understands the reason.

### Pattern 2: Define Success Explicitly
Before: "Write a good summary"
After: "Write a 3-sentence summary. Sentence 1: main finding. Sentence 2: key evidence. Sentence 3: implication. Each sentence under 25 words."

### Pattern 3: Add Examples
Before: "Format the data nicely"
After: Include one concrete example of desired input/output pair.

### Pattern 4: Include Self-Check
Add to complex prompts:
```
Before responding, verify:
- Does this answer the actual question asked?
- Have I included [specific requirement]?
- Is the length within [constraint]?
If unsure about any claim, say so explicitly.
```

### Pattern 5: Uncertainty Handling
Add: "If information is insufficient or ambiguous, state what's unclear and ask one clarifying question rather than guessing."

### Pattern 6: Authentic Friction (High Impact)
Add this line to any prompt where accuracy matters:
"If you lack enough information to give a complete answer, ask clarifying questions before proceeding."

Why it works: Real experts ask questions. Fakers pretend they know everything. This single line reportedly improved accuracy from 78% to 96% in testing. It prevents hallucinations by giving Claude permission to pause.

## Quick Templates

### Simple Task Template
```
You are a [role].

Task: [specific action verb] + [object] + [purpose/context]

Output: [format] in [length constraint]
```

### Standard Template
```
<context>
You are a [role] helping [audience] with [domain].
</context>

<task>
[Specific instructions with numbered steps if complex]
</task>

<constraints>
- [Limit 1]
- [Limit 2]
</constraints>

<output_format>
[Explicit structure]
</output_format>
```

### Comprehensive Template
```
<context>
You are a [role] with expertise in [domain].
Goal: [what success looks like]
Audience: [who will read this]
</context>

<background>
[Relevant documents/data wrapped in tags]
</background>

<task>
[Detailed instructions]
</task>

<constraints>
- [Hard limits]
- [Tone/style requirements]
- [What to avoid]
</constraints>

<examples>
<example>
Input: [sample input]
Output: [ideal output]
</example>
</examples>

<output_format>
[Explicit structure, length, style]
</output_format>

<self_check>
Before responding, verify: [criteria]
</self_check>
```

## Evaluation Checklist

After refining, score the prompt:

1. Specificity: Does it tell Claude exactly what to do? (not "help me" but "draft a 200-word email that...")
2. Context: Does Claude have the WHY, not just the WHAT?
3. Format: Is output structure explicit?
4. Constraints: Are limits clear?
5. Examples: Would one example clarify expectations?
6. Uncertainty: Does it handle edge cases?

Rate confidence: X/10 that this prompt produces desired output on first attempt.

## Persona Framework (5 Elements)

When defining WHO Claude should be, use this structure:

```
You are a [specific role + seniority] with [X years] experience in [industry/domain].
You specialise in [specific expertise].
Your approach: [methodologies/frameworks you use].
Your constraints: [budget/time/resource realities].
Deliver: [specific output format].
```

**Specificity questions to answer:**
- B2B or B2C?
- Digital or traditional?
- Startup or enterprise?
- Data-driven or creative-first?
- Strategic or executional?

**Example transformation:**
Before: "Act as a marketing expert and review my landing page."
After: "You are a Senior Conversion Copywriter specialising in B2B SaaS with 10 years experience. You use the PAS framework (Problem-Agitate-Solution) and test copy with A/B tests at 95% confidence. You have a 2% conversion baseline to beat. Deliver a line-by-line copy review with specific rewrites and predicted lift."

## Dual Persona Pattern (Main + Complementary)

One clear persona is better than three confused ones. BUT: a main persona plus one complementary lens can add valuable tension.

**Structure:**
```
Primary persona: [Role + seniority + domain] who leads the analysis.
Secondary lens: Before finalising, review through the eyes of a [complementary role] to surface [specific blind spots].
```

**Why it works:** The main persona does the heavy lifting. The secondary lens catches what the first might miss - without creating confusion about who's "driving."

**Good pairings (tension is the point):**
- Strategy Consultant + Implementation Specialist (vision vs execution reality)
- Grant Writer + Skeptical Funder (pitch vs due diligence)
- Copywriter + Target Customer (clever vs actually persuasive)
- Systems Thinker + Pragmatic Operator (elegant vs achievable)
- Facilitator + Difficult Participant (plan vs what might go wrong)

**Bad pairings (redundant or conflicting):**
- Two strategists (same lens, no tension)
- Designer + Developer + Marketer (too many cooks)
- Optimist + "Unlimited budget" (no useful constraints)

**Example:**
```
Primary: You are a Senior Grant Writer with 15 years experience in USAID and foundation funding. You specialise in Theory of Change narratives for systems-level social impact.

Secondary lens: Before submitting your draft, review it as a skeptical Programme Officer who has seen 200 applications this month and is looking for reasons to reject. Flag anything vague, unsubstantiated, or generic.
```

## Anti-Patterns to Fix

- "Be comprehensive" → Define what comprehensive means (word count, sections, depth)
- "Write a good..." → Specify criteria for "good"
- No format specified → Claude may default to bullets/lists when prose wanted
- Mixing context, task, format in one paragraph → Separate with tags or clear sections
- Assuming Claude knows your preferences → State them explicitly
- **"Act as an expert"** → Expert in what specifically? Define the niche.
- **Three+ personas** ("developer, marketer, and designer") → Pick ONE main + optionally ONE complementary lens. More than two creates confusion.
- **Contradictory constraints** ("startup founder with unlimited budget") → Realism matters. Contradictions break the persona.
- **Redundant dual personas** (two strategists) → The second lens should see what the first misses, not echo it.

## Usage

When user requests prompt refinement:

1. Show diagnosis of original (brief - 2-3 bullet points max)
2. Present 3 options (Minimal / Standard / Comprehensive)
3. Highlight key changes made
4. Rate confidence level for each option
5. Ask: "Which option fits your use case? Or shall I adjust any element?"
