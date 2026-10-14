---
name: claude-craft-radar
description: "Expert-consensus research on how to use, configure and work with Claude (Claude Code, Cowork, claude.ai, skills, subagents, model choice, cloud vs local, MCP, CLAUDE.md, cost). Checks Anthropic's own docs first, then Nick's Gmail '1. AI' newsletters, then a curated roster of practitioners (Allie K. Miller, Ethan Mollick, Ruben Hassid, Simon Willison, Boris Cherny and others) and community threads, over the last 30 or 90 days. Returns a consensus table, a recommendation for Nick's actual task, confidence, and the contrarian view. Trigger on 'claude-craft on X', 'what do the experts say about [Claude question]', 'expert consensus on [Claude setup]', 'how are people setting up [Claude feature]', 'should I use Opus or Sonnet for X', 'cloud or local for X', or any how-should-I-work-with-Claude question where the answer depends on current practice rather than a single doc lookup. Do NOT use for general AI news or non-Claude topics (use last-30-days / last-90-days-browser)."
---

# Claude Craft Radar

A last-90-days variant narrowed to one question type: "what is current best practice for working with Claude, and what should I do?" Think of it as a jury with a judge: Anthropic's docs are the judge (what the product actually does today), the expert roster is the jury (what works in practice), and Nick's own test data, when he has it, outranks both.

## Inputs

- **Question** (required). If vague, rewrite it into a decision ("Opus or Sonnet for the UK research batch?") and say so in one line.
- **Window**: 30 or 90 days. Default 90, but weight the last 30 days double. Claude ships fast; advice older than the latest model or feature release is stale until shown otherwise.
- **Task context** (optional): the real task the answer feeds (a tracker item, a script, a cost). If given, the final recommendation must be specific to it.
- **Own evidence** (optional): any test results Nick already has (e.g. "quality gate: Sonnet 2/5, Opus 4/5, Opus +15% cost"). Ask once if the question is a model or setup choice and none is supplied.

Compute the cutoff date from today's date in context and use it in every phase.

## Workflow

Run Phases 1 to 4 in parallel (Agent subagents on a cheap model are fine for 3 and 4; see the model note at the end). Then Phase 5, then synthesise.

### Phase 1: Primary sources (the judge)

Establish what is true right now before collecting opinions. Search and fetch:

- Claude Code docs: `site:code.claude.com/docs [topic]` (sub-agents, settings, model config, cloud sessions, costs, hooks, skills)
- Claude / API docs: `site:docs.claude.com [topic]` and model overview / pricing pages
- Anthropic engineering blog and news: `site:anthropic.com/engineering [topic]`, `site:anthropic.com/news [topic]`
- Claude Code changelog: `github.com/anthropics/claude-code` CHANGELOG.md and recent issues for the feature
- If the `claude-code-guide` agent or `claude-api` skill is available, use it for the factual layer instead of raw search.

Record: current behaviour, defaults, limits, prices, model names and release dates. Every later claim is checked against this. If an expert recommends something the docs say no longer works or has changed, mark it STALE.

### Phase 2: Nick's newsletters (Gmail)

Search the Gmail label `1. AI` within the window:

```
label:"1. AI" newer_than:90d ([keyword1] OR [keyword2] OR [keyword3])
```

Use 3 to 5 keywords and synonyms (e.g. for model choice: `opus sonnet haiku "model routing" subagent effort cost`). Search previews only show the oldest messages, so call get_thread on every relevant hit and read the body. Also run one search outside the label (`newer_than:90d from:(substack.com OR beehiiv.com) [keywords]`) to catch newsletters not yet filed. Senders and their signal tier are in `references/expert-roster.md`.

### Phase 3: Expert roster (the jury)

For each Tier 1 and Tier 2 name in `references/expert-roster.md`, run one targeted search:

```
[name] [topic keywords] [current year]
site:[their domain] [topic keywords]
```

Fetch the 3 to 6 most relevant posts in full. For each, capture: position (one line), date, evidence type (TESTED with numbers / EXPERIENCE / OPINION / SPONSORED or affiliate), model or feature version referenced, link.

Social platforms: X, Instagram, LinkedIn and Threads mostly block fetches. Use search snippets (`site:x.com [name] [topic]`, `site:linkedin.com/posts [name] [topic]`) and label them snippet-level. If Claude in Chrome is available, use Grok as in last-90-days-cowork for X; otherwise skip and say so.

### Phase 4: Community signal

- Reddit: `site:reddit.com/r/ClaudeAI [topic]`, `site:reddit.com/r/ClaudeCode [topic]`
- Hacker News: `site:news.ycombinator.com [topic]`
- GitHub: `site:github.com/anthropics/claude-code/issues [topic]` (bugs and limits users actually hit)

Community posts count as one combined jury voice, not one vote each. Use them to find failure modes the experts skip.

### Phase 5: Gap fill

If fewer than 4 independent dated sources take a position, widen to 90 days (if on 30), then to Tier 3, then to a general search. If still thin, say the consensus is thin rather than inventing one.

## Weighting rules

1. Docs beat everyone on what the product does. They do not settle what is best for a task.
2. Nick's own test data beats expert consensus for his own task, unless the sample is too small to mean anything (flag n < 10 explicitly and say what a bigger test would cost).
3. TESTED with numbers > EXPERIENCE > OPINION. SPONSORED counts zero.
4. Anthropic staff posts are primary for intent and roadmap, and biased on cost and on "use the bigger model".
5. Recency: anything predating the current model generation is downgraded one level.
6. Convergence across tiers (docs + practitioner + community) is the strongest signal. One loud voice is not consensus.

## Output

Save to the visible Research folder (create `Research/Claude Craft/` if missing) as:
`Claude Craft - [Short Question] - Research Brief - YYYY MMM DD.md`

Then paste the full brief in chat. Structure:

```markdown
# [Question] - Claude Craft Radar
Window: [start] to [end] | Sources: [n docs, n newsletters, n experts, n community]

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

Phases 2 to 4 are retrieval and extraction: a Sonnet or Haiku subagent is enough. Run Phase 1 checking and the final synthesis on the strongest model available, since that is where judgement errors cost most.
