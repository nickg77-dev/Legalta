---
name: fact-check
description: >
  Rigorous multi-stage fact-checking skill. Triggers on: "fact check this", "fact-check",
  "verify this claim", "is this accurate", "check my facts", "how confident are you",
  "source this", or whenever a response makes specific empirical claims that could be
  wrong (statistics, dates, names, legal/financial facts, technical specs). Also triggers
  proactively any time Claude has stated something it is not certain about, or after
  generating a response that contains named sources, figures, or causal claims. Use this
  skill even if the user has not explicitly asked — if the stakes of being wrong are
  meaningful, fact-check before replying.
---

# Fact-Check Skill

Multi-stage self-verification with web search. Combines the VeriFact-CoT approach
(claim identification → verification query generation → evidence retrieval → refinement)
with calibrated confidence scoring.

Core principle: treat every empirical claim as innocent until proven guilty by a source.

---

## When to Trigger

Trigger this skill when:
- User says "fact check", "fact-check", "verify", "is this true", "source this"
- Claude has just generated a response containing statistics, dates, named events, legal
  or financial figures, technical specs, or causal claims
- User expresses doubt about something Claude said
- The topic is fast-moving (policy, regulation, tech releases, personnel changes)
- Stakes are high — legal, financial, medical, reputational content

Do NOT trigger for: purely subjective opinions, creative writing, hypothetical scenarios,
or when the claim is clearly flagged as an estimate or approximation.

---

## Workflow

### Step 1 — Generate the Initial Answer

Produce the answer as you normally would. Do not self-censor yet. Label this clearly:

> INITIAL ANSWER: [response here]

---

### Step 2 — Identify and Isolate Claims

Extract every specific, falsifiable claim from the initial answer. A claim is anything
that could be verified against an external source. Assign each a claim ID (C1, C2...).

Types to flag:
- Named facts (dates, figures, percentages, prices, names, titles)
- Causal assertions ("X causes Y")
- Existence claims ("X exists / is available / is in force")
- Comparative claims ("X is larger/faster/cheaper than Y")
- Regulatory or legal status
- Attribution ("X said Y", "X recommends Y")

> CLAIMS IDENTIFIED:
> C1: [claim text] — type: [named fact / causal / existence / etc]
> C2: ...

---

### Step 3 — Generate 5 Verification Questions

For each high-risk claim, write a verification question that would expose an error.
Prioritise the 5 questions most likely to find a mistake. Good verification questions:
- Are specific and searchable
- Target the assumption most likely to be wrong
- Probe for recency ("is this still true?")
- Check directionality and magnitude ("is the figure this high, or lower?")

> VERIFICATION QUESTIONS:
> Q1 (targets C1): [question]
> Q2 (targets C2): [question]
> ...

---

### Step 4 — Search and Answer Each Question

For each verification question, use web_search (and web_fetch for key sources).
Then answer each question with what the evidence says, noting conflicts between sources.

If no reliable source can be found, that is itself a finding — mark the claim
as UNVERIFIABLE.

> VERIFICATION ANSWERS:
> Q1 → [answer] | Source: [URL or "no reliable source found"]
>   Verdict: CONFIRMED / CORRECTED / UNVERIFIABLE / OUTDATED
> Q2 → ...

Verdict definitions:
- CONFIRMED: source directly supports the claim
- CORRECTED: source contradicts the claim — note the correct version
- UNVERIFIABLE: no reliable source found — claim should be hedged or removed
- OUTDATED: claim was once true but is no longer current

---

### Step 5 — Final Corrected Answer

Rewrite the initial answer incorporating all corrections and hedges. Apply these rules:

- Replace any CORRECTED claim with the verified version
- Hedge or remove any UNVERIFIABLE claims (do not present them as fact)
- Flag any OUTDATED claims with "as of [last known date]"
- CONFIRMED claims can remain as stated

> FINAL ANSWER:
> [corrected response]
>
> CONFIDENCE: [X]% — [brief rationale, e.g. "2 of 5 claims fully confirmed, 1 corrected, 2 unverifiable"]
> UNCERTAINTY: [anything still uncertain that could change the answer]
> WHAT WOULD CHANGE THIS: [conditions or sources that would update the conclusion]

---

## Confidence Scoring Guidelines

Calculate confidence as a weighted average based on claim verdicts:

| Verdict      | Contribution |
|--------------|--------------|
| CONFIRMED    | Full weight  |
| CORRECTED    | Neutral (error caught and fixed) |
| UNVERIFIABLE | Reduces confidence significantly |
| OUTDATED     | Reduces confidence moderately    |

Express as a percentage with a plain-English rationale. Do not overstate precision —
round to nearest 10%. If overall confidence is below 60%, say so prominently.

---

## Output Format

When invoked, output clearly separated blocks:

```
INITIAL ANSWER
--------------
[text]

CLAIMS IDENTIFIED
-----------------
C1: ...
C2: ...

VERIFICATION QUESTIONS
----------------------
Q1 (C1): ...
Q2 (C2): ...

VERIFICATION RESULTS
--------------------
Q1 → ... | Source: ... | Verdict: CONFIRMED
Q2 → ... | Source: ... | Verdict: CORRECTED — correct version is [X]

FINAL ANSWER
------------
[corrected text]

CONFIDENCE: X%
UNCERTAINTY: [any remaining unknowns]
WHAT WOULD CHANGE THIS: [conditions]
```

For conversational use (user just wants a quick check), collapse Steps 1-4 into a brief
"CHECKING..." summary and lead with the FINAL ANSWER. Only show full workings if the user
asks or if a significant correction was made.

---

## Research-Backed Rationale

This skill incorporates:
- VeriFact-CoT (arxiv 2509.05741): multi-stage claim identification → verification → refinement
  significantly reduces hallucination in empirical claims
- SelfCheckGPT (arxiv 2303.08896): self-consistency checking catches ~70% of factual errors
- Verification-First strategy (arxiv 2511.21734): asking the model to verify before finalising
  is described as "almost free lunch" for accuracy improvement
- Calibrated confidence prompting: forces explicit uncertainty acknowledgement rather than
  confident-sounding hedging

Key finding from multilingual fact-checking research (ACL 2024): zero-shot prompting with
self-consistency outperformed chain-of-thought for fact verification — hence the structured
question-answer loop above, not just "think step by step".

---

## Edge Cases

- If the initial answer contains no falsifiable claims (pure opinion, creative writing):
  output "No empirical claims to verify. Confidence in logical consistency: [X]%."

- If web search is unavailable: complete Steps 1-3 from internal knowledge, label all
  verdicts as INTERNAL-ONLY, and note that external verification was not possible.

- If the user provides a specific claim to check (rather than a full response):
  skip Step 1, treat the user's claim as C1, and run Steps 3-5 only.

- If multiple claims conflict with each other within the same response: flag this
  as an INTERNAL INCONSISTENCY before running web search.

---

## Triggering Phrases (for description matching)

fact check, fact-check, verify, is this accurate, source this, how confident, check my facts,
is this true, double-check, cross-check, validate this claim, am I right that, can you confirm,
what's the evidence for, are you sure about that, cite your sources
