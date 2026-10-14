# Opus vs Sonnet for the UK research batch (tracker item 2.1) - Claude Craft Radar

Window: 22 Sep to 14 Oct 2026 (floor: Opus 5.5 release, start of the current model generation) | Sources: 4 Anthropic primary, 2 newsletters read in full, 3 expert posts, 2 independent tested write-ups, 1 community sweep

## Answer

Switch `run-loop.sh` to Opus 5.5 at the default (medium) effort for the UK batch. Your own gate (Opus 4/5 vs Sonnet 2/5 for about 15% more per batch) points the same way as the only tested expert evidence and Anthropic's own positioning: Opus for open-ended judgement, Sonnet for well-scoped work. Research enrichment (finding a fleet, judging fit, applying exclusion rules) is judgement work. Confidence 70%. It would be 85% with a 20-row rerun.

## What the docs say (current)

- Opus 5.5 released 22 Sep 2026 at $4 / $20 per million input / output tokens; Sonnet 5.5 released 28 Sep at $2 / $10; Haiku 5.5 released 7 Oct from $0.10 / $0.50 ([Sonnet 5.5 model page](https://platform.claude.com/docs/en/models/sonnet-5-5/overview), [Opus 5.5 launch](https://www.anthropic.com/claude-opus-5-5)).
- Anthropic: "Where Opus 5.5 is built for complex work requiring careful judgment, Sonnet 5.5 is strongest at well-scoped everyday tasks... Opus 5.5 remains clearly stronger at complex, open-ended work requiring sustained judgment." Sonnet "complements Opus 5.5 best when running at lower effort settings... At higher settings, it can perform comparably at a similar cost" ([Sonnet 5.5 launch](https://www.anthropic.com/claude-sonnet-5-5)).
- Default effort is Medium in Claude Code and the apps, High on the API (same source).
- Subagents take a `model` field (`sonnet`, `opus`, `haiku`, full ID or inherit); the docs suggest an Explore subagent with `model: haiku` for cheap exploration ([sub-agents docs](https://code.claude.com/docs/en/sub-agents)).
- Sonnet 5.5 cache reads halved to $0.10 on 7 Oct (reported by Joozio, not checked against the pricing page).

## Consensus table

| Source | Position | Evidence type | Date | Version | Link |
|---|---|---|---|---|---|
| Anthropic | Opus for judgement-heavy open-ended work; Sonnet for well-scoped tasks at low or medium effort | Vendor claim | 28 Sep | 5.5 | [launch post](https://www.anthropic.com/claude-sonnet-5-5) |
| paddo.dev | 300 runs on real merged changes. Opus best at medium (13/20 clean, $44); Sonnet 11/20 at medium for $12, and 0 broken tests at every effort. Effort is "a spend dial, not a quality dial" | TESTED | 29 Sep | 5.5 | [The Default Was Right](https://paddo.dev/blog/default-was-right/) |
| Joozio | Opus 5.5 at medium is his daily driver for agentic work; Sonnet "when the best is more than the job needs"; Haiku 5.5 as "the hands" for lookups, classification, sweeps | EXPERIENCE (runs a live agent, publishes costs) | 9 Oct | 5.5 | [newsletter](https://thoughts.jock.pl/p/anthropic-5-5-lineup-opus-haiku-max-credits-2026) |
| Simon Willison | Uses Opus 5.5 as his Claude Code default; Sonnet 5.5 "almost as good as Opus on some coding tasks"; both break at max effort | EXPERIENCE | 22 and 28 Sep | 5.5 | [Opus post](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/), [Sonnet post](https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/) |
| Aleksei Aleinikov | Real price gap in cache-heavy agent loops is about 1.65x, falling to about 1.15x if Sonnet thinks longer. Sonnet savings live at low or medium effort only | Worked arithmetic (illustrative) | Oct | 5.5 | [Sonnet 5.5 vs Opus 5.5](https://www.alekseialeinikov.com/en/blog/topics/ai/claude-sonnet-5-5-vs-opus-5-5) |
| Ethan Mollick | Snippet only: called Opus 5.5 "affordable Fable-class" | OPINION (snippet-level) | Sep | 5.5 | [LinkedIn](https://www.linkedin.com/posts/emollick_opus-55-was-a-good-model-in-my-short-early-activity-7508207904194236416-4u4q) |
| r/ClaudeAI, r/ClaudeCode | Common pattern: Opus orchestrates with Sonnet subagents; mixed reports of Opus 5.5 regressing after launch | Community | Sep to Oct | 5.5 | [thread](https://www.reddit.com/r/ClaudeAI/comments/1wnecg9/introducing_claude_opus_55_the_first_model_in_our/), [thread](https://www.reddit.com/r/ClaudeAI/comments/1wp1yht/what_is_wrong_with_opus_55/) |

Silent on this question within the window: Allie K. Miller, Ruben Hassid, Mariah Brunner, Artificial Corner, Prosper in AI, AI Adopters Club (Gmail newsletters checked by subject and snippet).

## Where they agree

- Opus 5.5 for judgement; Sonnet 5.5 for well-scoped, checkable work.
- Leave effort at medium. Raising effort costs more without making either model more careful, and max effort breaks things.
- The real cost gap is well under the 2x list price in agent loops, because cached context costs the same on both. Your measured +15% fits this.

## Where they disagree (and why)

- **How close Sonnet gets.** Anthropic's benchmarks put Sonnet within about 2 points of Opus. paddo's real-work test puts it 2 clean runs behind at medium. Your gate shows a bigger gap (2/5 vs 4/5). Likely reason: benchmarks and coding tasks come with tests to check against. Lead research has no test, so judgement has to stand in for one.
- **Orchestration pattern.** Joozio and Reddit favour Opus as the head with cheaper subagents. Aleinikov warns that switching from Opus down to Sonnet loses Opus's reasoning, so per-turn routing saves less than it looks.

## Contrarian view

On five rows, a 4/5 vs 2/5 split could be chance. If the two Sonnet misses were rules a checker could catch (an exclusion rule, a formatting issue), Sonnet plus a Haiku 5.5 checker would match Opus for less money. Haiku 5.5 only shipped on 7 Oct, possibly after your gate was designed, and it is now a much stronger checker than it was. The strongest case for staying on Sonnet is that the failures were fixable process errors, not missing judgement.

## Applied to your task

1. Check in the results file in Legalta/Outputs what kind of mistakes Sonnet made. If they were judgement calls (wrong fit score, missed fleet evidence), switch to Opus. If they were rule breaches, test Sonnet plus a Haiku checker first.
2. Check the gate date. If the gate ran before 28 Sep, `--model sonnet` meant Sonnet 5, not 5.5, and the gate needs rerunning.
3. To switch, paste this into a **Local** Claude Code session (the file sits on your Mac, so a cloud session cannot see it):

   > In "Claude Macbook Folder/Projects/01 Work Projects/Legalta/2 Sales/DACH/legalta-enrichment/run-loop.sh", change --model sonnet to --model claude-opus-5-5 and leave effort at the default. Commit with the message: "Switch enrichment to Opus 5.5: quality gate 4/5 vs Sonnet 2/5 at about 15% more per batch."

   Pinning the full model ID instead of the `opus` alias stops the model changing silently partway through the UK campaign.
4. Rerun the gate on 20 rows with Opus before the full UK batch. At about 15% more per batch the rerun costs little, and it shows whether 4/5 holds.

## Why this might be wrong

Five rows is a coin-flip sample, and the gate may have compared Sonnet 5 with Opus 5.5 instead of like with like. Not considered: running the UK batch through the Batch API at 50% off (stated by Aleinikov; check that it applies to how `run-loop.sh` calls Claude), which would make Opus cheaper than Sonnet costs you today.

## Stale or rejected sources

- Joozio, July 2026 ("I Maxed Out Fable 5"): before Opus 5.5, so stale.
- [ClaudeLog tactical model selection](https://www.claudelog.com/mechanics/tactical-model-selection/), [morphllm comparison](https://www.morphllm.com/comparisons/claude-haiku-vs-sonnet-vs-opus): cover the 4.x and 5.0 generations, so stale.
- Facebook group claim that Sonnet 5.5 "costs even more" than Opus: unsourced.
- [MindStudio](https://www.mindstudio.ai/blog/claude-sonnet-5-5-pricing-benchmarks) and [Nate Herk video](https://www.youtube.com/watch?v=7eo-11K2e3c): consistent with the above but add nothing tested on research tasks; video sponsored.
