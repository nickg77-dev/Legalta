---
name: claudecraft-last-60-days
description: "Expert-consensus research on how to use, configure and work with Claude (Claude Code, Cowork, claude.ai, skills, subagents, model choice, cloud vs local, MCP, CLAUDE.md, cost). Checks Anthropic's own docs first (which also sets the recency floor), then a curated expert roster across Nick's Gmail newsletters and their public posts (Allie K. Miller, Ethan Mollick, Ruben Hassid, Mariah Brunner, Simon Willison, Boris Cherny, Artificial Corner and others), then community threads. Default window 60 days; model questions are cut off at the current model generation's release. Returns a consensus table, a recommendation for Nick's actual task, confidence, and the contrarian view. Trigger on 'ClaudeCraft last 60 days on X', 'claudecraft on X', 'what do the experts say about [Claude question]', 'expert consensus on [Claude setup]', 'how are people setting up [Claude feature]', 'should I use Opus or Sonnet for X', 'cloud or local for X', or any how-should-I-work-with-Claude question where the answer depends on current practice rather than a single doc lookup. Do NOT use for general AI news or non-Claude topics (use last-30-days / last-90-days-browser)."
---

# ClaudeCraft last 60 days

A last-60-days variant narrowed to one question type: "what is current best practice for working with Claude, and what should I do?" Think of it as a jury with a judge: Anthropic's docs are the judge (what the product actually does today), the expert roster is the jury (what works in practice), and Nick's own test data, when he has it, outranks both.

## Inputs

- **Question** (required). If vague, rewrite it into a decision ("Opus or Sonnet for the UK research batch?") and say so in one line.
- **Task context** (optional): the real task the answer feeds (a tracker item, a script, a cost). If given, the final recommendation must be specific to it.
- **Own evidence** (optional): any test results Nick already has (e.g. "quality gate: Sonnet 2/5, Opus 4/5, Opus +15% cost"). Ask once if the question is a model or setup choice and none is supplied. Record WHEN the test ran and WHICH model version it used.

## Recency window

Default: 60 days. Claude advice decays like milk, not wine.

- **Model choice, pricing, effort, limits:** hard floor = the release date of the current model generation (find it in Phase 1). Anything older is STALE, however good. If the floor leaves fewer than 4 sources, say the evidence is thin rather than widening.
- **Features and setup (cloud vs local, subagents, hooks, skills, CLAUDE.md):** 60 days, widen to 90 only if thin, and only for sources the current docs still agree with.
- **Ways of working (planning, verification, delegation habits):** 90 days is fine; these change slowly.
- Weight the most recent 30 days double in every case.

Compute the cutoff from today's date in context and use it in every phase.

## Workflow

Phase 1 first (it sets the recency floor). Then Phases 2 and 3 in parallel (Agent subagents on a cheaper model are fine for both; see the model note at the end). Then synthesise.

### Phase 1: Primary sources (the judge)

Establish what is true right now before collecting opinions. Search and fetch:

- Claude Code docs: `site:code.claude.com/docs [topic]` (sub-agents, settings, model config, cloud sessions, costs, hooks, skills)
- Model pages and pricing: `site:platform.claude.com/docs [topic]`, `site:anthropic.com [model name]` launch posts, https://claude.com/pricing
- Anthropic engineering blog: `site:anthropic.com/engineering [topic]`
- Claude Code changelog and issues: `github.com/anthropics/claude-code`
- Anthropic's own emails in Gmail (`from:email.claude.com newer_than:60d`)
- If the `claude-code-guide` agent or `claude-api` skill is available, use it for the factual layer instead of raw search.

Record: current behaviour, defaults, limits, prices, model names and release dates (this sets the recency floor). Every later claim is checked against this. If an expert recommends something the docs say no longer works or has changed, mark it STALE.

### Phase 2: Experts (newsletters and public posts together)

One pass per expert, using every channel they publish on. The roster (Core sources with Weight, Gmail sender and web link; Excluded sources listed separately) is in `references/expert-roster.md`.

1. **Gmail first (cheapest, already curated):** one search across all roster senders, inside and outside the `1. AI` label:
   ```
   newer_than:60d (from:sender1 OR from:sender2 ...) ([keyword1] OR [keyword2] OR [keyword3])
   ```
   Use 3 to 5 keywords and synonyms (e.g. for model choice: `opus sonnet haiku "model routing" subagent effort`). Previews only show the oldest messages, so call get_thread on every relevant hit and read the body.
2. **Web, for each Core source not already covered by Gmail (highest Weight first):** `[name] [topic] [current year]` and `site:[their domain] [topic]`. Fetch the 3 to 6 most relevant posts in full.
3. **Social:** X, Instagram, LinkedIn and Threads mostly block fetches. Use search snippets (`site:x.com [handle] [topic]`, `site:linkedin.com/posts [name] [topic]`) and label them snippet-level. If Claude in Chrome is available, use Grok as in last-90-days-cowork for X.

For each position captured: one-line position, date, evidence type (TESTED with numbers / EXPERIENCE / OPINION / SPONSORED or affiliate), model or feature version referenced, link.

### Phase 3: Community signal

If the `last-30-days` skill is available, run its Reddit and Hacker News steps on the topic, using this skill's recency window instead of 30 days, and skip the first two bullets below. Otherwise use them as written.

- Reddit: `site:reddit.com/r/ClaudeAI [topic]`, `site:reddit.com/r/ClaudeCode [topic]`
- Hacker News: `site:news.ycombinator.com [topic]`
- GitHub: `site:github.com/anthropics/claude-code/issues [topic]` (bugs and limits users actually hit)
- Independent tested write-ups surfaced by search (benchmarks people ran on real work) count as TESTED if the method is stated.

Community posts count as one combined jury voice, not one vote each. Use them to find failure modes the experts skip.

## Weighting rules

1. Docs beat everyone on what the product does. They do not settle what is best for a task.
2. Nick's own test data beats expert consensus for his own task, unless the sample is too small to mean anything (flag n < 10 explicitly and say what a bigger test would cost), or it was run on a model version that has since been replaced (check the test date against Phase 1 release dates).
3. TESTED with numbers > EXPERIENCE > OPINION. SPONSORED counts zero.
4. Anthropic staff posts are primary for intent and roadmap, and biased on cost and on "use the bigger model".
5. Recency: anything predating the current model generation is downgraded one level.
6. Convergence across tiers (docs + practitioner + community) is the strongest signal. One loud voice is not consensus.
7. Weight: each Core source carries a Weight (1 to 5) in `references/expert-roster.md`, calculated from reach and evidence quality (method in that file). Use it to order the consensus table and break ties, never to overrule rules 1 to 3: a TESTED post from a small author beats an OPINION from a large one. Ignore Excluded sources unless they are the only report of a launch. Refresh audience figures when they are more than 6 months old.

## Output

Save to the visible Research folder (create `Research/ClaudeCraft/` if missing) as:
`ClaudeCraft - [Short Question] - Research Brief - YYYY MMM DD.md`

Then paste the full brief in chat. Structure:

```markdown
# [Question] - ClaudeCraft last 60 days
Window: [start] to [end] (floor: [reason]) | Sources: [n docs, n newsletters, n experts, n community]

## Answer
2-4 sentences. The recommendation for Nick's task, the deciding reason, confidence %.

## What the docs say (current)
Bullets with links. Defaults, limits, prices, release dates.

## Consensus table
| Source | Position | Evidence type | Date | Version | Link |

## Where they agree
## Where they disagree (and why)
## Contrarian view
The strongest case against the answer, steelmanned.

## Applied to your task
Specific steps for the task context, including any prompt or config change ready to paste.

## Why this might be wrong
One reason. Plus one option not considered.

## Stale or rejected sources
Anything dropped and why (outdated, sponsored, contradicted by docs).
```

Style: British English, no em or en dashes (use " - "), no correctio constructions, every named source hyperlinked or marked "no verified link", unverified claims labelled.

## After the run

If a source repeatedly produced high-signal answers, or repeatedly produced noise, propose a one-line edit to `references/expert-roster.md` (promote, demote, add, remove). Do not edit it without Nick's yes.

## Model note for subagents

Phases 2 and 3 are retrieval and extraction: a Sonnet or Haiku subagent is enough. Run Phase 1 checking and the final synthesis on the strongest model available, since that is where judgement errors cost most.
