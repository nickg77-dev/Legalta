---
name: last-90-days-browser
description: "Multi-source research skill for sessions without Claude in Chrome. Investigates a topic across the web, Hacker News, GitHub, Substack, and LinkedIn over the past 90 days. Reddit and X/Twitter are NOT reliably reachable from this environment — see coverage note in output. Trigger phrases: 'last-90-days on [topic]', 'research [topic] for me', 'what's the word on [topic] lately', 'run last-90-days on [topic]'. Use this variant when Claude in Chrome is not enabled or not available in this session. If Claude in Chrome is available, use last-90-days-cowork instead for full Reddit + X coverage."
---

# Last 90 Days Research — Browser variant

Adapted from last-90-days-cowork for sessions without Claude in Chrome. Five reliable sources (Web, Hacker News, GitHub, Substack, LinkedIn), not seven. Say so plainly in the output — don't present this as full cross-platform coverage.

## Invoking the skill

The user will provide a topic. It might come as:
- "last-90-days on [topic]"
- "research [topic] for me"
- "what's the word on [topic] lately"
- Or they'll just name a topic after invoking the skill

If no topic is specified, ask for one before proceeding.

If Claude in Chrome becomes available mid-session, mention that last-90-days-cowork would give fuller coverage (Reddit + X) and offer to switch — don't switch silently.

## Workflow

Calculate the 90-day cutoff date from today's date in context. Use this consistently across every phase's date filtering.

---

### Phase 1: Web Search

Use web_search with 2–3 targeted queries to catch recent news, reviews, and analysis:

- `"[TOPIC]" news site:techcrunch.com OR site:theverge.com OR site:wired.com`
- `[TOPIC] review` followed by the current year
- `[TOPIC] problems OR complaints OR "worth it"` — for honest opinions

For the 3–4 most relevant results, web_fetch the top results for actual content, not just headlines. Discard anything clearly older than 90 days.

---

### Phase 2: Hacker News (via web_search workaround)

Raw Algolia JSON fetch fails in this environment (web_fetch only allows URLs already surfaced by web_search). Workaround:

1. web_search: `site:news.ycombinator.com [TOPIC]`
2. web_search: `site:news.ycombinator.com [TOPIC] discussion` (catches threads the first query misses)
3. For threads with useful-looking snippets, web_fetch the actual item URL for full comment context — expect occasional 429s from HN directly; if so, use what the search snippet already gave you rather than retrying repeatedly.

Extract: story title, points/comments if visible, notable comment excerpts, URL, date. Discard anything older than 90 days.

---

### Phase 3: GitHub

Use web_search to surface relevant Discussions, Issues, and README/release chatter:

- `site:github.com [TOPIC] discussions`
- `site:github.com [TOPIC] issue`

Strongest for tool/product/library research. If the topic clearly has no GitHub footprint, skip and say so rather than forcing weak results in.

Extract: repo name, issue/discussion title, notable comments, URL, date.

---

### Phase 4: Substack

Use web_search:

- `site:substack.com [TOPIC]`

web_fetch the 2–3 most relevant posts for actual argument content, not just the search snippet.

---

### Phase 5: LinkedIn

LinkedIn blocks web_fetch, so this phase is web_search-only — headline/snippet-level, not full-content extraction.

- `site:linkedin.com/pulse [TOPIC]`
- `site:linkedin.com/posts [TOPIC]`

If the topic has no natural LinkedIn presence, skip and say so.

---

### Phase 6: Reddit — best-effort only, flag clearly

`site:reddit.com [TOPIC]` via web_search does not reliably return genuine reddit.com URLs in this environment (confirmed, not a one-off — the search index itself deprioritises/excludes Reddit here, independent of fetch permissions). Attempt it once; if no genuine reddit.com URLs come back, skip and state plainly in the output: "Reddit not accessible from this session — no Reddit signal in this briefing." Do not substitute other sites' mentions-of-Reddit-sentiment as if they were Reddit data.

---

### Phase 7: X/Twitter — skip

Not reachable without Claude in Chrome. State in output: "X/Twitter phase skipped — requires Claude in Chrome, not available in this session. Run via last-90-days-cowork for X coverage."

---

### Phase 8: Synthesize

Combine the available sources into a coherent briefing. The goal is synthesis, not a dump of raw data. Look for:

- **Consensus** — What do people broadly agree on across platforms?
- **Controversy** — Where is there real disagreement or debate?
- **Pain points** — What frustrations keep surfacing?
- **Excitement** — What are people genuinely enthusiastic about?
- **Emerging patterns** — What's new or gaining momentum vs. settled wisdom, and does that shift across the 90-day window?
- **Gaps** — What questions aren't being answered well anywhere?

With 5 sources instead of 7, cross-platform convergence is still your strongest signal but a weaker one than the Cowork variant's design assumes — don't claim "cross-platform convergence" language unless it's genuinely 2+ sources in real agreement.

---

## Output Format

Use this exact structure for the markdown file:

```markdown
# [TOPIC] — Last 90 Days Research
*Generated: [DATE] | Window: [DATE - 90 days] to [DATE]*

## TL;DR
2–3 sentences. What's the most important thing someone should know right now?

## Hacker News
### Notable Stories
- **[Story Title]** — [X points, Y comments] — [one-line summary] — [URL]

### What HN Is Saying
Narrative paragraph. HN skews technical/builder — note that lens in your synthesis.

## GitHub
### Notable Discussions/Issues
- **[Repo — Title]** — [one-line summary] — [URL]

### What GitHub Is Saying
Narrative paragraph, or "No meaningful GitHub footprint for this topic" if skipped.

## Substack
### Key Posts
- **[Post Title]** ([Author/Publication]) — [key takeaway] — [URL]

### What Substack Is Saying
Narrative paragraph on the considered/opinion-writing angle.

## LinkedIn
### Notable Posts/Articles
- **[Title or snippet]** — [one-line summary] — [URL]

### What LinkedIn Is Saying
Narrative paragraph, or "No meaningful LinkedIn presence for this topic" if skipped.

## Web
### Key Sources
- **[Article Title]** ([Publication]) — [key takeaway] — [URL]

### What the Web Is Saying
Paragraph synthesizing the broader coverage. Who's covering it, what angle, what conclusions.

## Cross-Source Patterns
What showed up consistently across multiple sources? This is the highest-confidence signal available in this variant.

## Momentum Check (90-day view)
Is this topic building steadily, spiking recently, or cooling off across the window?

## Key Takeaways
- [Most important thing]
- [Second most important thing]
- [Third most important thing]

## Content Angles (if relevant)
If this research is for content creation, list 2–3 specific video/post angles the data actually supports.

## Coverage Note
**Sources used:** Web, Hacker News, GitHub, Substack, LinkedIn (as available)
**Sources not accessible in this session:** Reddit (search index limitation), X/Twitter (requires Claude in Chrome — see last-90-days-cowork)
State clearly this is a 5-source brief, not 7-source, so it isn't mistaken for the fuller Cowork version.
```

---

## Saving and delivering the output

1. Save the markdown file to a `last-90-days/` subfolder inside the user's research folder. Create the subfolder if it doesn't exist. Name the file `[TOPIC]-[YYYY-MM-DD].md`.

2. Provide a link to the file.

3. **Also paste the full research briefing directly in chat.** Don't make the user open a file to see the results — show them everything right there.

---

## Troubleshooting

- **HN returns no results**: Broaden the query — try shorter keywords, or check the topic isn't just older than 90 days.
- **web_fetch times out on a long article**: Take what loaded, note it was truncated.
- **GitHub/Substack/LinkedIn have no relevant results**: Legitimate outcome for many topics, not a failure. Say so plainly.
- **Reddit search returns non-reddit.com results or nothing**: Expected. Skip per Phase 6, don't retry more than once.
