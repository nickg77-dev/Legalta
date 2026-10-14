# Expert roster - Claude Craft Radar

Edit freely. Tier sets search order and weight. Gmail sender is what to put in the `from:` search; web is where to search when Gmail has nothing.
Link status: VERIFIED (resolved on 2026 OCT 14), INFERRED (from Gmail sender or a standard URL pattern, not yet fetched).

## Tier 0 - Primary (the judge)

| Source | Use for | Gmail sender | Web | Status |
|---|---|---|---|---|
| Claude Code docs | Features, defaults, sub-agents, cloud sessions, settings | - | https://code.claude.com/docs/en/sub-agents | VERIFIED |
| Model and pricing docs | Release dates, prices, default effort | - | https://platform.claude.com/docs/en/models/sonnet-5-5/overview | VERIFIED |
| Anthropic launch posts and engineering blog | Positioning of each model, patterns Anthropic uses | no-reply@email.claude.com | https://www.anthropic.com/engineering | VERIFIED |
| Claude Code changelog and issues | What changed and when | - | https://github.com/anthropics/claude-code | INFERRED |
| Boris Cherny (creator of Claude Code) | His own workflow: parallel sessions, plan mode, verification loops | - | https://x.com/bcherny | INFERRED (most coverage is second-hand, check originals) |

## Tier 1 - Core experts (Nick's list plus tested practitioners)

| Expert | Why | Gmail sender | Web | Status |
|---|---|---|---|---|
| Allie K. Miller (AI with Allie) | Business and operator workflows, Codex vs Claude Code | aiwithallie@mail.beehiiv.com | https://aiwithallie.beehiiv.com | INFERRED |
| Ethan Mollick (One Useful Thing) | Research-backed, non-developer framing | oneusefulthing@substack.com | https://www.oneusefulthing.org | INFERRED |
| Ruben Hassid (How to AI) | Practical Claude setup for non-coders, limits | ruben@substack.com | https://ruben.substack.com | INFERRED |
| Mariah Brunner (Learn AI With Mariah) | 300+ Claude guides: prompts, skills, workflows | mariah@dreamtuesday.com | https://learnaiwithmariah.com/guides/ | VERIFIED |
| Simon Willison | Most consistent hands-on, dated Claude Code writing; tests every release | - | https://simonwillison.net/tags/claude-code/ | VERIFIED (blog) |
| Artificial Corner | Long-run Claude lessons, skills reviews, Cowork and folder setup | artificialcorner@substack.com | https://artificialcorner.substack.com | INFERRED |
| Joozio (Pawel Jozefiak) | Runs a real agent daily and publishes costs; model routing playbooks | joozio@substack.com | https://thoughts.jock.pl | VERIFIED |
| Hamel Husain | Evals; the right lens for quality gates and model choice | - | https://hamel.dev | INFERRED |
| Kieran Klaassen / Every | Compounding engineering, multi-agent Claude Code | - | https://every.to | INFERRED |
| Peter Yang (Behind the Craft) | Claude Code for non-engineers | - | https://creatoreconomy.so | VERIFIED |

## Tier 2 - Useful, check evidence type

| Source | Why | Gmail sender | Web | Status |
|---|---|---|---|---|
| Prosper in AI | CLAUDE.md and instruction architecture | prosperinai@substack.com | https://prosperinai.substack.com | INFERRED |
| AI Adopters Club (Kamil Banc) | Operator and small-business adoption | aiadopters@substack.com | https://aiadopters.substack.com | INFERRED |
| paddo.dev | Publishes tested model and effort comparisons on real work | - | https://paddo.dev | VERIFIED |
| Nate B. Jones | Strategy and agent setup for operators | - | no verified link | - |
| Claire Vo (How I AI podcast) | Guest walkthroughs of real workflows | - | no verified link | - |
| Zvi Mowshowitz | Model release digests | - | https://thezvi.substack.com | INFERRED |
| Latent Space (swyx) | Builder-level agent practice | - | https://www.latent.space | INFERRED |
| ClaudeLog | Community docs on model selection and mechanics | - | https://www.claudelog.com/mechanics/tactical-model-selection/ | VERIFIED |

## Tier 3 - Low signal for setup questions (news and hype; use only for "what launched")

| Source | Note | Gmail sender | Status |
|---|---|---|---|
| LearnAIWithMe (Gencay) | Build-in-public, clickbait framing | gencay@substack.com | INFERRED |
| Superhuman AI (Zain Kahn) | Daily news | superhuman@mail.joinsuperhuman.ai | INFERRED |
| The Rundown AI | Daily news | news@daily.therundown.ai | INFERRED |
| Maverick Maltin (@mavgpt) | Instagram creator, hype-heavy | maverick@maltin.com | VERIFIED (profile https://www.elev8or.io/c/mavgpt) |
| Wonder Tools (Jeremy Caplan) | Tool round-ups | wondertools@substack.com | INFERRED |

## Community

- https://www.reddit.com/r/ClaudeAI/ and https://www.reddit.com/r/ClaudeCode/
- Hacker News via `site:news.ycombinator.com`
- https://github.com/anthropics/claude-code/issues

## Gmail search string (Tier 1 and 2 senders)

```
from:(aiwithallie@mail.beehiiv.com OR oneusefulthing@substack.com OR ruben@substack.com OR mariah@dreamtuesday.com OR artificialcorner@substack.com OR joozio@substack.com OR prosperinai@substack.com OR aiadopters@substack.com OR no-reply@email.claude.com)
```
