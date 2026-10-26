---
name: canivibecodeit
description: "Check whether a tool or app can be vibe coded, using canivibecodeit.com verdicts, and submit any unlisted tool to the site. Use when Nick asks to check a tool, a shortlist, or his tech stack against vibe-coding potential."
---

# Can I Vibe Code It

Checks canivibecodeit.com for a verdict on whether a piece of software can be replaced by a self-built ("vibe coded") app, summarises the verdict, and handles unlisted tools by submitting them to the site. This skill never builds anything itself - it only checks, reports, and (for a YES + one-shot verdict) drafts a build plan for Nick to approve separately.

## When invoked

Nick will either:
- name one tool ("can I vibe code Granola"), or
- ask for batch mode: check his whole tech stack (the CSV/synced sheet in the Tech Flow project, or a pasted list), or a specific shortlist.

## Single-tool check

1. Slugify the tool name (lowercase, spaces to hyphens) and fetch `https://canivibecodeit.com/<slug>` with WebFetch, asking for: verdict tier (YES / KINDA / NOT REALLY), build time, complexity (specifically whether it says "one-shot"), suggested tech stack, price to replace, what you lose, and vote count.
2. If the page resolves and has verdict data, report it as a compact table:

| Field | Detail |
|---|---|
| Verdict | ... |
| Complexity | ... |
| Build time | ... |
| Stack | ... |
| Price to replace | ... |
| What you lose | ... |

3. If Verdict = YES and Complexity/build-time says one-shot: add one line flagging it as a build candidate, plus a short (3-5 line) build plan - stack, rough scope, what's kept vs dropped. Do not start building. End with something like "say the word and I'll build it" so Nick decides separately.
4. If Verdict = YES but not one-shot, or Verdict = KINDA: report the table only, no build plan.
5. If Verdict = NOT REALLY: report the table only and stop.
6. If the page 404s, redirects to a "not listed" state, or WebFetch can't find verdict data: treat as not listed (see below).

## Batch mode

- Source the list from wherever Nick points (the Tech Flow project's tech stack file/sheet, or a pasted list). Read it first (project_read / project_search for the project file, or the pasted text) rather than guessing tool names.
- Run the single-tool check above for each entry. Pace fetches (don't fire them all at once) to avoid hammering the site.
- Present one summary table sorted with YES + one-shot candidates first:

| App | Verdict | Complexity | Build time | Notes |
|---|---|---|---|---|

- List not-listed tools separately underneath, after submitting each (see below).

## Not listed - submit it

When a tool isn't listed:
1. Tell Nick plainly it's not listed - don't fabricate a verdict.
2. Submit it via https://canivibecodeit.com/submit. That form is JavaScript-driven (no query-param/API route), so use browser automation:
   - Prefer Claude in Chrome (Nick's default browser this session) unless he's asked for the built-in browser.
   - Navigate to the submit page, fill "App name" with the tool's name and "Website" with its official homepage (look this up if not already known - don't guess a URL), leave "Your take" and "Credit" as given or blank, leave the honeypot field untouched, and submit.
   - Confirm to Nick whether the submission went through (the flow is: bot drafts a verdict, opens a PR, a human merges - so there's no instant verdict back).
3. If no browser automation is available in the session (neither Chrome extension nor built-in browser reachable), say so and give Nick the submit link instead of retrying blind.
4. Don't log a separate watchlist file - the site's own submission queue is the record. Just tell Nick what was submitted.

## Rules

- Never build, install, or scaffold anything as part of this skill. A YES + one-shot verdict produces a plan, not code - building happens only if Nick separately asks for it.
- Don't guess a verdict for an unlisted tool - report "not listed" and submit, nothing else.
- Match Nick's style: concise, plain text, markdown tables only for the tabular output above, British English, no filler.