---
name: legalta-meeting-transcript-to-tasks
description: "[CC] Pulls the full transcript of a recent Legalta call, archives it to Drive and Slack, extracts the to-do list discussed, cross-checks each item against existing LEGALTA Jira tasks, and writes to Jira only after Nick confirms. ALWAYS use this skill when Nick says 'pull today's Legalta call', 'sync the Legalta meeting to Jira', 'process the Legalta call from [day]', 'legalta transcript to tasks', 'turn the call into Jira tasks', or asks in any form for a recent Legalta meeting to become Jira updates. Also use it when he asks what actions came out of a Legalta call and Jira is the obvious destination, even if he does not mention Jira by name. Do NOT use make-meeting-notes or wrike-task-format for this - neither touches Jira, and this workflow encodes matching logic plus a confirmation gate that must not be skipped."
---

# Legalta Meeting Transcript to Tasks

Turns a recorded Legalta call into archived records (Drive + Slack) and a reviewed, confirmed set of Jira changes. Manual trigger only. Never runs on a schedule.

**Hard gate: never write to Jira (create, edit, transition, delete) until Nick has explicitly confirmed the final numbered list in Step 4.** Everything before that point is a proposal. If Nick says "just do it, skip the review", state in one sentence what you are about to write, then proceed.

**Requires:** Granola (or Wispr Flow / Zoom), Google Drive, Slack, and Atlassian Rovo connectors, plus local file creation. If a connector is missing at run time, say which one and what breaks - do not silently skip that step.

## When NOT to use this skill

- Non-Legalta meetings, or Legalta calls where Nick only wants a summary and no Jira work - use `make-meeting-notes`.
- Seefar/Farsight work - that goes to Wrike, use `wrike-task-format`.
- Nick pastes a transcript directly and wants tasks extracted - Steps 3 to 5 still apply, skip Step 1.

## Step 1 - Retrieve the meeting

Priority order. Use whichever source actually holds the full transcript **with speaker names** for this call.

1. **Granola first.** Nick has a paid account with full transcript access, so this is almost always right for his own calls. Use `Granola:query_granola_meetings` for a natural-language pull, or `Granola:list_meetings` + `Granola:get_meetings` by ID to browse a date range.
2. **Wispr Flow fallback**, if Granola has no transcript (attendee-only note, or the call ran on someone else's platform). `Wispr Flow:search_meetings` with an ISO 8601 `since`. Transcripts paginate via `start_char` / `char_limit` in roughly 12,000-character chunks - page through fully, do not stop at chunk one.
3. **Zoom last resort.** `Zoom for Claude:search` for the UUID, then `get_meeting_assets`. The summary text is double-JSON-encoded: `data[0]['text']` needs two `json.loads()` passes to reach `meeting_summary.summary_plain_text`.

Prefer a full transcript over an AI summary as the source of truth for extracting actions. If only a summary exists anywhere, say so explicitly before proceeding. Never present summary-derived actions as if they came from the transcript.

**Identifying the meeting.** Match on title keyword ("Legalta" / "LEGALTA") and/or known attendees: Thomas Haselböck, Arlind Ramadani, Güray Ermegan, Mira, Karlis, Carlos, Andrey. If genuinely ambiguous - multiple candidates, unclear which Nick means - list them (date, time, title, attendees) and ask. Never guess silently.

**Multiple meetings in the window.** Ask whether to merge the to-do lists into one pass or process each separately. If merged, every item still carries a tag naming its source meeting. Traceability is never dropped, even when merged.

**Context pass.** Fuzzy-match the title against other Legalta calls from the past 2 weeks and skim for continuity (e.g. "this follows last week's register data discussion"). This informs judgement in Step 3. It is not a deliverable and does not need showing unless it changes a classification.

## Step 2 - Archive to Drive and post to Slack

**Drive.** One properly formatted Google Doc - headings, bullets, a Contents section, not a wall of plain text. Structure: title, attendee/source line, Contents, Summary (with sub-headed themes), Decisions Made, Action Items per person, Discussed-Not-Agreed, Compliance Check, then **Annex A: Transcript**. No filler metadata lines (e.g. an "Archived: [date]" line adds nothing the person can't see from the file's own timestamp - leave it out).

**Reference template - copy this doc's structure and formatting exactly:** https://docs.google.com/document/d/1Gut0IilCCa6AVt00DrQ3DUuPtir9_er6F8vrwAvqsLU/edit

Formatting requirements:
- Real `<h1>`/`<h2>`/`<h3>` and `<ul>`/`<li>` tags (via `contentMimeType: text/html`) so Google Docs renders proper heading styles.
- **Clickable Table of Contents:** give each `<h2>` an `id` attribute and link the Contents list items to it, e.g. `<h2 id="decisions-made">Decisions Made</h2>` and `<li><a href="#decisions-made">Decisions Made</a></li>`. Google's HTML import does not always preserve internal anchors reliably - after creating the doc, this needs a one-time visual check; if the links land dead, fall back to telling Nick to use Insert > Table of contents > "with blue links" (native Google feature, generates automatically from headings) and note that in the doc.
- **Horizontal rule between every top-level (`<h2>`) section** - use `<hr>` so the document is easy to scan, not solid text top to bottom.
- **Page break before the Annex** - `<div style="page-break-before: always;"></div>` immediately before the Annex heading. Google's HTML-to-Docs conversion honours this inconsistently; check visually on the first render each time this changes, and fall back to a manual note ("insert a page break here") if it doesn't take.

**Annex A: link out, don't embed, when a source link exists.** Embedding a full 50-60k-character transcript in every meeting doc clutters Drive for something the source platform already stores. Before embedding:
- Check whether the meeting object returned by Granola / Wispr Flow / Zoom includes a URL, permalink, or share-link field.
- **As of the last check:** none of the three connected tools return a usable public link for an individual meeting's transcript by default. Wispr Flow has a shared-notes mechanism (`notes.wisprflow.ai/shared/...`) but this project's tools only *resolve* an existing share link, not *create* one - so a working link can't be generated from here without Nick first sharing the note from the Wispr Flow app himself. Zoom recordings do expose a `play_url` via `get_recording_resource`, but only when the meeting was actually run through Zoom Cloud Recording - not for Wispr Flow or Granola-captured calls. Granola: no URL field surfaces via the connected tools.
- **If a genuine link is available** (checked fresh each run, since this may change as products add features): use it - "Full transcript: [link]" - and do not embed the text.
- **If no link is available:** embed the full verbatim transcript in Annex A as before, and say plainly in the doc which platform/meeting ID it came from so Nick could ask that platform directly for a shareable link if he wants one instead. Never fabricate or guess a URL pattern.

Destination folder: https://drive.google.com/drive/folders/1VqnN4jls-MSOHO2WF2Qzd8lMVD6SzfGa?usp=drive_link

**Naming convention for this and every other artefact:** subject first, then artefact type, then date as `YYYY MMM DD` - e.g. `Legalta & Projects - Meeting Summary - 2026 SEP 01`. Never use an underscore anywhere in the title.

Google Drive direct writes have a known silent-failure history on this account. Build the file locally with `create_file`, hand Nick a copy via `present_files` as the primary path, and only then attempt `Google Drive:create_file`. Confirm with `Google Drive:get_file_metadata` before reporting the Drive write as done - check the returned `fileSize` and `contentSnippet` actually contain real content, not a placeholder. Never assume a Drive write succeeded, and never write a placeholder line promising content "to follow" - if the transcript (or the link replacing it) isn't ready to include in the same call, don't create the doc yet.

**Slack.** Post the transcript and notes (or the Drive link) to the partner/meeting-records channel automatically as part of the run. This is low-risk archival and does not need the Jira confirmation gate.

Resolve the channel at run time with `Slack:slack_search_channels` rather than hardcoding an ID. The exact channel was never pinned down at spec time (working name "partners-meetings"); Legalta's other channels follow the numbered convention `1-strategy`, `2-sales`, `3-website`, `4-ops`, `5-hr`, `6-legal`, so also check whether the content belongs in one of those instead. If unclear, ask once and reuse the answer, rather than asking every run.

**Compliance check before posting anywhere.** Legalta is an acquisition partner, not a law firm. If the transcript or notes contain language that states or implies a guaranteed claim outcome, or quotes a headline compensation figure that has not been confirmed by Güray, flag it to Nick before the Slack post goes out. Do not silently edit the transcript - it is a record.

## Step 3 - Extract and match to-dos

Extract every actionable item discussed: what, who owns it, any date mentioned. Only extract what is actually in the transcript. Never infer a task that sounds sensible but was not agreed - if something is implied but not committed to, list it separately as "discussed, not agreed" rather than as a to-do.

**Personal check-in content is out of scope for Jira.** Legalta calls typically open with a personal check-in (how people are doing, health, family, other work). Ignore this content entirely when building the to-do list - it never becomes a Jira item. Exception: if the check-in surfaces a clear to-do (e.g. someone commits to doing something specific by a date), extract it but tag it `[PERSONAL]` in Step 4's list and never write it to Jira, even if Nick's Step 4 reply doesn't address it. State once, plainly, why: it's personal, not project work. This applies to the summary and action-item extraction; it does not mean scrubbing personal content from the archived transcript itself (see Step 2) - the record stays complete even where the actionable list doesn't.

**Matching scope.** The whole LEGALTA project via `Atlassian Rovo:searchJiraIssuesUsingJql` (`project = LEGALTA`). Not restricted by department label, even for a department-focused call - cross-department follow-ups happen.

**Classify each item:**

- `[ADD]` - no plausible existing match. Propose as new.
- `[EDIT]` - confidently the same task as an existing ticket, with a clear change. Cite the ticket number.
- `[CLOSE]` - the meeting indicates it is done or resolved. Cite the ticket number.
- `[POSSIBLE MATCH]` - resembles an existing ticket but not confidently enough to call it an edit. Surface for Nick to decide. Never auto-resolve a fuzzy match in either direction. When in doubt, this is the correct bucket.

**New task defaults**, used only where Nick's Step 4 reply does not override:

- Level: **Task**, not Sub-task, unless the meeting explicitly frames it as part of an existing Task.
- Department label: infer from content (`1-strategy`, `2-sales`, `3-website`, `4-ops`, `5-hr`, `6-legal`). If ambiguous between two, flag it rather than picking silently.
- Assignee: infer from who is named as owner in the transcript, mapped to Thomas, Arlind, Mira, Karlis, Carlos or Nick. Leave unassigned and flag if unclear. First-name-only mentions in an ambiguous context get flagged, not guessed.

## Step 4 - Present for review (confirmation gate)

**Word artefact only** - build a `.docx` (docx skill), not a plain-text chat dump and not a second Google Doc. Nick reviews it as a document, deletes the options that don't apply per item, and pastes the remainder back as his reply.

For each item: a short heading line with the ticket number if known (existing ticket numbers always take priority over inventing new labels), then the proposed change, then a set of selectable option lines Nick trims down to what he wants. Assume most items need no change - keep "approve as proposed" the first, least-effort option on every row. Example layout for one item:

```
3. LEGALTA-98 or NEW - Confirm cartel date range with Güray
   Resembles LEGALTA-98 ("Confirm compliance figures with Güray")

   [ ] Approve as proposed (treat as EDIT to LEGALTA-98)
   [ ] Treat as a separate new task instead
   [ ] Sub-task of LEGALTA-98 instead
   [ ] Reject - do not create or change anything
   [ ] Edit - specify: _____________________
```

Items with no ambiguity (clean ADD/EDIT/CLOSE, confident match) can drop straight to a single "Approve as proposed / Reject / Edit - specify" three-line block rather than the full multi-option set - reserve the longer option list for genuine `[POSSIBLE MATCH]` or `[PERSONAL]`-adjacent judgement calls.

Number every item once, consistently, across the whole document - Nick's reply references these numbers. Follow the artefact naming convention (Step 2) for the file itself, e.g. `Legalta & Projects - Proposed Jira Changes - 2026 SEP 01`.

Nick reviews the document (deleting unwanted option lines, or replying in free text against the numbers - both work) and pastes back or states his decisions. Parse the reply, apply overrides, then echo the final action set back, one line per item, before writing anything.

If any item is a `[POSSIBLE MATCH]` (or a flagged `[PERSONAL]` item) and Nick's reply does not address it, ask about that item specifically rather than defaulting either way.

## Step 5 - Write to Jira

Only after explicit confirmation. Use Atlassian Rovo against LEGALTA:

- New: `createJiraIssue`
- Edits: `editJiraIssue`
- Closes: `transitionJiraIssue` - check `getTransitionsForJiraIssue` first for the valid transition ID, do not guess a transition name

Report ticket numbers and links for everything created or changed, in the same numbered order as the confirmed list. If any write fails, say which item failed and why - never report a partial run as complete.

## Out of scope (v1)

- No calendar-based auto-trigger. Manual invocation every time.
- No auto-resolving of `[POSSIBLE MATCH]` items under any circumstance.
- No editing the Drive doc after creation. Re-run the skill if reprocessing is needed.
- No cross-project Jira search. LEGALTA only, not KAN.
- Slack posting is one-way archival. No reading or monitoring of replies.
- No hard-delete of Jira tasks. Items are closed or transitioned, preserving history. A hard delete only happens if Nick explicitly asks for one on a specific item in his Step 4 reply.
