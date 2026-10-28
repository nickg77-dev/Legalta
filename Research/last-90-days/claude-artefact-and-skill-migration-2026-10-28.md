# Claude Artefact and Skill Migration - Last 90 Days Research
*Generated: 2026 OCT 28 | Window: 2026 JUL 30 to 2026 OCT 28*

## TL;DR
Anthropic offers no export for custom skills or artefacts. Its personal-to-Team migration leaves both behind, and published artefacts cannot be republished on Team. The community answer is browser extensions and scripts that pull artefacts out of the claude.ai interface, plus keeping a master copy of every skill in your own repo.

## Reddit
Not run. This phase needs Claude in Chrome, which is not available in a Claude Code cloud session.

## Hacker News
No relevant threads found. A `site:news.ycombinator.com` search returned only Anthropic help pages.

## GitHub
- **agoramachina/claude-exporter** - Chrome and Firefox extension that bulk-exports conversations and pulls artefacts out as separate files. Its Firefox listing warns that older versions mis-exported after Anthropic changed how artefacts are generated - https://github.com/agoramachina/claude-exporter
- **ashwanthkumar/claude-artifacts-downloader** - Chrome plugin that zips every artefact in one conversation - https://github.com/ashwanthkumar/claude-artifacts-downloader
- **agarwalvishal/claude-chat-exporter** - exports chats to Markdown, with artefacts as labelled code blocks - https://github.com/agarwalvishal/claude-chat-exporter
- **claude-export (PyPI)** - command-line tool that parses the official data export zip, including an artefacts command - https://pypi.org/project/claude-export/

Dates on these projects were not checked; maintenance status is unverified.

## Substack
- **The Definitive Guide to Claude SKILLS** (limitededitionjonathan) - compares skills across Code, web, desktop and API - https://limitededitionjonathan.substack.com/p/the-definitive-guide-to-claude-skills
- **Tutorial: how to install Claude skills** (The AI Break) - covers upload only - https://theaibreak.substack.com/p/tutorial-how-to-install-claude-skills

## LinkedIn
Skipped. No useful signal expected for this narrow how-to topic.

## Web
- **Move your personal Claude account to a Team or Enterprise organisation** (Anthropic) - skills, published artefacts, share links, Cowork sessions and Claude Code cloud sessions do not move; the move is one-way - https://support.claude.com/en/articles/9267400
- **Export your Claude data** (Anthropic) - a zip of JSON files; it cannot be imported into another account - https://support.claude.com/en/articles/9450526
- **How to find and export all your Claude artifacts** (AI Toolbox, vendor) - bulk export is behind a paid tier - https://www.ai-toolbox.co/tutorials/claude/artifacts
- **How to export Claude conversation history** (llmnesia) - says the export format changes between versions and to check whether artefact bodies are included - https://www.llmnesia.com/blog/how-to-export-claude-conversation-history

## X/Twitter
Not run. Needs Claude in Chrome.

## Cross-Platform Patterns
- No official export for skills or artefacts. Every source keeps a master copy of each skill outside Claude, because claude.ai only supports upload.
- Artefact export relies on browser tools that read the live interface, and they break when Anthropic changes it.
- Whether the official export zip contains artefact bodies is unconfirmed (about 30% confidence that it does).

## Momentum Check
Not assessable. Most sources are undated how-to pages and the community phases did not run.

## Key Takeaways
- Use an agent that drives a browser (Cowork with Claude in Chrome) to harvest artefacts from the live interface, rather than relying on the export zip.
- Keep skills in a Git repo as the single source of truth and treat claude.ai as a deployment target.
- Before migrating, save the source of every published artefact; its link stops working and Team cannot republish it publicly.

## Coverage Note
Usable signal: Web, GitHub, Substack (thin). Empty: Hacker News. Skipped: LinkedIn (not relevant). Not run: Reddit and X, because Claude in Chrome is not available in this Claude Code cloud session.
