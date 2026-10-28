# Prompt Refiner - Detailed Examples

Reference file loaded when user needs worked examples of prompt transformation.

## Example 1: Vague Research Request

### Original Prompt
"Research AI trends and write something useful"

### Diagnosis
- No role/context
- "Something useful" undefined
- No audience specified
- No format or length
- No specific focus areas

### Refined (Standard Option)

```
<context>
You are a technology analyst writing for non-technical senior executives at a mid-sized consultancy.
</context>

<task>
Research current AI trends relevant to professional services firms. Focus on:
1. Practical applications already generating ROI
2. Near-term opportunities (6-18 months)
3. Risks and implementation challenges
</task>

<constraints>
- Prioritise verifiable examples over speculation
- If citing statistics, note the source
- Avoid vendor-specific product recommendations
</constraints>

<output_format>
Executive briefing, 400-500 words:
- Opening paragraph: key takeaway
- 3 sections (one per focus area above)
- Closing paragraph: recommended next step
Write in prose, no bullet points.
</output_format>
```

Confidence: 8/10

---

## Example 2: Code Review Request

### Original Prompt
"Review my code"

### Diagnosis
- No code provided
- No review criteria specified
- No context on codebase/project
- No output format

### Refined (Comprehensive Option)

```
<context>
You are a senior software engineer conducting a code review. The code is from a production Python application handling financial transactions.
</context>

<task>
Review the following code for:
1. Security vulnerabilities (SQL injection, input validation, auth issues)
2. Performance concerns (N+1 queries, unnecessary loops, memory leaks)
3. Maintainability (naming, documentation, complexity)
4. Edge case handling
</task>

<code>
[CODE BLOCK HERE]
</code>

<constraints>
- Flag severity: Critical / Major / Minor / Suggestion
- Do not refactor entire sections - identify specific lines
- If uncertain about business logic intent, ask before suggesting changes
</constraints>

<output_format>
For each issue found:
- Line number(s)
- Severity
- Issue description (1 sentence)
- Suggested fix (code snippet or guidance)

End with: Overall assessment (1 paragraph) and priority order for fixes.
</output_format>

<self_check>
Before submitting review:
- Have I checked for the OWASP Top 10 vulnerabilities?
- Have I considered the happy path AND error paths?
- Are my suggestions actionable, not just observations?
</self_check>
```

Confidence: 9/10

---

## Example 3: Email Draft

### Original Prompt
"Write an email to decline a meeting"

### Diagnosis
- No context on relationship
- No reason for declining
- No tone guidance
- Unknown formality level

### Refined (Minimal Option)

```
You are a consultant maintaining professional relationships.

Task: Draft a polite email declining a meeting request. The meeting is a sales pitch from a software vendor. I'm not currently evaluating tools but want to leave the door open for future contact.

Output: 3-4 sentences. Professional but warm. No corporate jargon.
```

Confidence: 7/10 (would increase with more context on existing relationship)

---

## Context Engineering Principles Applied

### Principle 1: Token Efficiency
- Background data: only include what's necessary for THIS task
- Remove redundant instructions Claude already follows (politeness, helpfulness)
- Use tags to separate concerns - Claude parses structure efficiently

### Principle 2: Right Altitude
Too specific (brittle):
"If the user mentions budget, say 'I understand budget constraints are important' then list exactly 3 options priced under $1000"

Too vague (unreliable):
"Be helpful with budget questions"

Right altitude:
"When budget is mentioned, acknowledge the constraint and prioritise cost-effective options. Explain trade-offs between price and capability."

### Principle 3: Progressive Disclosure for Complex Tasks
For multi-step workflows, don't front-load everything. Structure as:

```
<phase_1>
[First task with clear completion criteria]
</phase_1>

When phase 1 complete, proceed to:

<phase_2>
[Second task]
</phase_2>
```

### Principle 4: Motivated Constraints
Claude generalises better when it understands WHY.

Weak: "Keep responses under 200 words"
Strong: "Keep responses under 200 words. This will be read on mobile during commutes, so brevity aids comprehension."

Weak: "Don't use technical jargon"
Strong: "Avoid technical jargon. The reader is a board member without engineering background who needs to make a funding decision."
