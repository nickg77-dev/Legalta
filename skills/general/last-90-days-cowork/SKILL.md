---
name: last-90-days-cowork
description: "Deep research skill that investigates any topic across Reddit, Hacker News, GitHub, Substack, LinkedIn, the web, and X/Twitter over the past 90 days. Requires Claude in Chrome (browser automation) for Reddit and X/Twitter. Returns a synthesized research briefing with real citations and engagement data, saved as a markdown file and displayed in chat. Trigger this skill whenever the user says 'research [topic]', 'last-90-days on [topic]', 'what's happening with [topic]', 'what are people saying about [topic]', 'find me info on [topic]', 'run last-90-days on [topic]', or any variation where the goal is a multi-source research brief on a specific topic. Also use for competitor research, trend discovery, tool comparisons, and audience sentiment analysis. Use this variant when Claude in Chrome is enabled (Claude Cowork, or claude.ai with the Chrome extension active). If Claude in Chrome is not available, use last-90-days-browser instead."
---

# Last 90 Days Research — Cowork variant

Multi-source research agent that synthesises what people are actually saying about a topic across Reddit, Hacker News, GitHub, Substack, LinkedIn, the web, and X/Twitter — all within the past 90 days. Requires Claude in Chrome for the Reddit and X/Twitter phases.

## Invoking the skill

The user will provide a topic. It might come as:
- "last-90-days on [topic]"
- "research [topic] for me"
- "what's the word on [topic] lately"
- Or they'll just name a topic after invoking the skill

If no topic is specified, ask for one before proceeding.

Before starting, confirm Claude in Chrome is actually available as a tool in this session. If it isn't, stop and use last-90-days-browser instead — don't attempt the Reddit/X phases without it, they will fail silently or time out.

## Workflow

Run Phases 1 (Web), 2 (Hacker News), 3 (GitHub), 4 (Substack), 5 (LinkedIn) in parallel where possible — they're independent web_search/web_fetch calls. Then run Phase 6 (Reddit) and Phase 7 (X/Twitter) via Claude in Chrome. Then synthesise.

Calculate the 90-day cutoff date from today's date in context. Use this consistently across every phase's date filtering.

---

### Phase 1: Web Search

Use web_search with 2–3 targeted queries to catch recent news, reviews, and analysis:

- `"[TOPIC]" news site:techcrunch.com OR site:theverge.com OR site:wired.com`
- `[TOPIC] review` followed by the current year
- `[TOPIC] problems OR complaints OR "worth it"` — for honest opinions

For the 3–4 most relevant results, use web_fetch to pull actual page content — not just headlines. Grab the key points, quotes, and conclusions. Discard anything clearly older than 90 days even if it surfaces.

---

### Phase 2: Hacker News

Use web_search first — raw Algolia API fetches are blocked in this environment even with Claude in Chrome available for other tools, because web_fetch only succeeds on URLs already surfaced by a prior web_search.

1. web_search: `site:news.ycombinator.com [TOPIC]`
2. web_search: `site:news.ycombinator.com [TOPIC] discussion` (catches threads the first misses)
3. For threads with useful-looking snippets, web_fetch the actual item URL for full comment context — expect occasional 429s from HN directly; if so, use the search snippet content rather than retrying repeatedly.

Extract: story title, points/comments if visible, notable comment excerpts, URL, date. Discard anything older than 90 days.

---

### Phase 3: GitHub

Use web_search to surface relevant Discussions, Issues, and README/release chatter:

- `site:github.com [TOPIC] discussions`
- `site:github.com [TOPIC] issue`

This is strongest for tool/product/library research — bug reports and feature requests are closer to genuine pain-point signal than most review sites. Less useful for non-technical topics; if the topic clearly has no GitHub footprint, skip this phase and say so rather than forcing weak results in.

Extract: repo name, issue/discussion title, notable comments, URL, date.

---

### Phase 4: Substack

Use web_search:

- `site:substack.com [TOPIC]`

Substack is where considered, longer-form opinion tends to land before or alongside mainstream tech press — a different register from HN's builder-lens or Reddit's raw sentiment. web_fetch the 2–3 most relevant posts for actual argument content, not just the search snippet.

---

### Phase 5: LinkedIn

LinkedIn blocks web_fetch, so this phase is web_search-only — treat it as a headline/snippet-level pass, not full-content extraction.

- `site:linkedin.com/pulse [TOPIC]`
- `site:linkedin.com/posts [TOPIC]`

Useful for B2B, career, and professional-sentiment angles that the other sources miss entirely. If the topic has no natural LinkedIn presence (e.g. a consumer gadget), skip and say so.

---

### Phase 6: Reddit (via Claude in Chrome)

The Reddit JSON API workaround (`reddit.com/search.json`) is confirmed dead in this environment — the search index deprioritises/excludes Reddit results regardless of query construction, and this is unrelated to whether Claude in Chrome is enabled. Do not attempt it.

Instead, use Claude in Chrome to browse Reddit directly:

1. Navigate to `https://www.reddit.com/search/?q=[TOPIC]&sort=top&t=year` (use `t=year` and filter by date manually, since Reddit's native "past 90 days" isn't a standard sort window)
2. From the results, identify posts within the last 90 days
3. For the top 3–5 posts by score, open the post and read the top comments
4. Also run a `sort=new` pass to catch recent posts that haven't ranked yet

Extract: post title, subreddit, score, comment count, date posted, URL, and recurring themes/complaints/praise from comments.

If Reddit shows a login wall, cookie consent blocker, or the page fails to load properly, note that in the output and move on — don't get stuck retrying.

---

### Phase 7: X/Twitter (via Claude in Chrome)

Two options depending on what loads:

**Option A — direct X search (preferred if accessible):**
1. Navigate to `https://x.com/search?q=[TOPIC]&src=typed_query&f=live`
2. Scroll and read recent posts within the 90-day window
3. Note notable accounts, post content, and engagement where visible

**Option B — Grok fallback (if X itself is gated behind login):**
1. Navigate to `https://grok.com/`
2. Wait for the page to fully load
3. Type and submit: "What are people saying about [TOPIC] on X/Twitter in the last 90 days? Summarize the main discussions, opinions, complaints, praise, and any notable posts or accounts. Give me specific examples where you can."
4. Wait for the full response and extract it

If both are gated or unavailable, note that in the output and skip this section — don't get stuck.

---

### Phase 8: Synthesize

Combine all seven sources into a coherent briefing. The goal is synthesis, not a dump of raw data. Look for:

- **Consensus** — What do people broadly agree on across platforms?
- **Controversy** — Where is there real disagreement or debate?
- **Pain points** — What frustrations keep surfacing?
- **Excitement** — What are people genuinely enthusiastic about?
- **Emerging patterns** — What's new or gaining momentum vs. settled wisdom, and does that momentum shift across the 90-day window (e.g. building steadily vs. spiking recently)?
- **Gaps** — What questions aren't being answered well anywhere?

Cross-platform convergence is your strongest signal. If something shows up on Reddit AND HN AND X AND GitHub, that's real — say so explicitly.

---

## Output Format

Use this exact structure for the markdown file:

```markdown
# [TOPIC] — Last 90 Days Research
*Generated: [DATE] | Window: [DATE - 90 days] to [DATE]*

## TL;DR
2–3 sentences. What's the most important thing someone should know right now?

## Reddit
### Top Posts
- **[Post Title]** (r/subreddit) — [X upvotes, Y comments] — [one-line summary] — [URL]

### What Reddit Is Saying
Narrative paragraph. What's the overall tone? What themes keep coming up? Any notable comment threads?

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

## X/Twitter
Response, lightly cleaned up. Keep specific handles or post references where available. Note whether this came from direct X search or the Grok fallback.

## Cross-Platform Patterns
What showed up consistently across multiple sources? This is the highest-confidence signal.

## Momentum Check (90-day view)
Is this topic building steadily, spiking recently, or cooling off across the window? Note where the signal is clearer earlier vs. later in the 90 days.

## Key Takeaways
- [Most important thing]
- [Second most important thing]
- [Third most important thing]

## Content Angles (if relevant)
If this research is for content creation, list 2–3 specific video/post angles the data actually supports.

## Coverage Note
State plainly which of the 7 sources returned usable signal, which were skipped (and why), and which hit access problems.
```

---

## Saving and delivering the output

1. Save the markdown file to a `last-90-days/` subfolder inside the user's research folder. Create the subfolder if it doesn't exist. Name the file `[TOPIC]-[YYYY-MM-DD].md`.

2. Provide a link to the file.

3. **Also paste the full research briefing directly in chat.** Don't make the user open a file to see the results — show them everything right there.

---

## Troubleshooting

- **Reddit shows a login wall or won't load in Chrome**: Note it in the output and move on. Don't retry endlessly.
- **HN returns no results**: Broaden the query — try shorter keywords, or widen past 90 days to check the topic isn't just older than that.
- **X search is gated**: Fall back to the Grok option in Phase 7. If that's also gated, skip and say so.
- **web_fetch times out on a long article**: Take what loaded, note it was truncated.
- **GitHub/Substack/LinkedIn have no relevant results**: This is a legitimate outcome for many topics, not a failure. Say so plainly rather than padding with weak matches.
