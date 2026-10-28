# Deliverables, batch discipline and failure modes

Ported from truck-cartel-municipal-outreach-cc (lessons from the 20-batch Italy run).

## Deliverables

Default package. Read the `docx` and `xlsx` skills for mechanics before building.

### Word strategy brief
Cover page with a **"Read this first"** box naming every open decision the user must make before sending - and only that. **Keep this box to genuinely still-open items.** As items get resolved across batches, remove them from the box rather than leaving a growing narrative of resolved history on page one - a client who is told the brief is a "clean finish" while page one still lists things that were actually researchable will (correctly) push back. Move the full batch-by-batch changelog to an appendix at the back of the same document instead of the cover; leave a one-line pointer from the trimmed box to the appendix for anyone who wants the full trail. Then: executive summary, target table, contact doctrine, the emails (each in a bordered block with a "Why this opening" note explaining the personalisation choice), European scaling plan, hidden-volume section, risk register, verification log, and the appendix.

Use Calibri, navy `1F3864` headings, accent `C00000`, table shading `ShadingType.CLEAR`. Set `features: { updateFields: true }` for the TOC. Render to PDF and read the pages before delivering - pay particular attention to any table whose column count you changed (see the column-width gotcha below).

### Lead list (current standard, 2 Oct 2026)
The lead list is a Google Sheet copied from "Legalta Lead List - Template" (see SKILL.md section 7a). The Excel layout below is kept for reference from the Italy run only; do not use it for new batches unless someone asks for Excel.

### Excel target list (Italy run, legacy)
Tabs:
1. **Target List** - number, city, country, legal entity name, entity type, fleet evidence, figure date, primary contact role, named individual, contact channel, secondary contact, email language, personalisation hook, priority 1-3, key risk, **postal address**, and a **Notes** column. The Notes column carries the one-line status that used to only live in prose changelogs - e.g. "contact confirmed Aug 2026 via decree," "DO NOT DRAFT - see Open Decisions (majority-private ownership)," "hook is an OPERATIONAL-SCALE PROXY, not confirmed," "ready to send" - so the spreadsheet is usable on its own without cross-referencing the brief's narrative. Group by wave with banner rows.
2. **Value Model** - yellow lever cells, blue hardcoded inputs, black formulas. Defaults: documentation survival **41%** (Zurich benchmark), average net price **€180,000** (blended, user-adjustable), overcharge **5%** (LG Berlin floor; substitute a better local anchor if a national judgment quantifies one, e.g. an Italian court's own overcharge percentage), interest multiplier **2.0x** (planning placeholder - flag as not a legal entitlement), litigation contribution 5%, split 65/35. Carry a visible warning that it is internal only.
3. **Qualification** - the screen, colour-coded KILL / UNLOCK / FLAG.
4. **Sources** - every factual claim with outlet and URL.

**If you insert rows into a sheet with formulas, openpyxl does not update the references - rewrite every formula afterwards and re-run `recalc.py`.** Verify computed values by reading them back, not just by a clean recalc.

### Verification log
Always. Three categories: verified with source, verified as reported (single source or press summary), and **NOT verified** with what to do about it. Name every estimate as an estimate.

---


## Running a large multi-session target programme (learned on the Italy run, batches 1-20)

When a single market is pushed well past the first wave of targets (Italy went from a handful of names to 105 targets and 89 drafted emails across 20 sessions), treat it as a standing programme with its own file architecture and batch discipline, not a one-off research task.

### File architecture
- Keep two Python source-of-truth files, not raw JSON or a spreadsheet as the master: `targets.py` (a `TARGETS` list of dicts - one per lead, with at minimum `n`, `wave`, `priority`, `city`, `entity`, `entity_type`, `segment`, `fleet_evidence`, `fleet_source`, `fleet_status`, `contact_role`, `contact_name`, `contact_note`, `hook`, `risk`, `address`, `note`) and `emails.py` (an `EMAILS` list of dicts, each linked to a target by `n`). Python source is easy to `git`-diff, easy to append to consistently, and easy to regenerate JSON/Excel/Word from - a spreadsheet edited by hand drifts.
- Regenerate `targets_data.json` / `emails_data.json` from the Python source every batch via a one-line `json.dump`, and build the Word/Excel deliverables from those, not by hand-editing the deliverables.
- If a build script needs scratch CSVs derived from large source registries (a national IPA entity registry, population data, etc.), do not keep them checked in - regenerate them from the original source file at the start of every batch and delete them at the end. Keeping the *regeneration script* (not the derived CSV) in the standard batch checklist below avoids both drift and repo bloat. If the build scripts expect scratch inputs under a fixed working path (a hardcoded `/tmp/...` directory, for instance), create that path and copy the needed inputs into it as the very first step of every rebuild - this is easy to forget after a session break and produces a confusing "file not found" rather than an obviously-missing-input error.
- **When adding a column to any generated table (Excel sheet or a docx table), the column-width/positioning array is coupled to the exact column count and must be updated in the same edit, not after.** A hardcoded width array (e.g. `TARGET_COL_WIDTHS`) that isn't resized when a column is added will silently misalign or clip content - always visually verify the rebuilt table (PDF + `pdftoppm` + Read, or reading the xlsx back) after any column-count change, not just a clean build.
- If an entry number is ever retired (found to be a duplicate, disqualified, or miscounted), do not renumber everything else - leave the gap and note it permanently in the `assert len(TARGETS) == N` comment (e.g. "entry numbers run to N+2, but #61 and #65 were removed"). Renumbering breaks every reference to that entry in prior deliverables, Sources tabs and correspondence.

### Discovery methods, ranked by efficiency (most efficient first)
1. **Official regional/national operator directory.** A single government or industry-network page that lists every water, waste, or transport operator in a region or network at once - e.g. a regional environment ministry's "gestori del servizio idrico" page, or an official multi-utility network's own membership page. One page can surface 5-15 usable candidates at once, and membership/listing on an official directory is itself adequate evidence of public ownership - you do not need a deep ownership dive per entity when the parent directory already establishes it, though you should still confirm the exact ownership percentage before an entity clears the KILL screen (see the qualification screen's note on this). Actively look for one of these before falling back to method 2. Once a region's directory has been used, note it as exhausted so future sessions don't re-search it.
2. **Direct search for the named public-capital multi-comune consortium pattern.** Searching for "[region] consorzio pubblico [servizio]"-style named entities outperforms population-band sampling of individual municipalities, because a single consortium often represents dozens of member comuni in one contact.
3. **Population-band sampling of individual municipalities** - the least efficient method; use only once the directory and consortium-pattern methods are exhausted for a market.

### Naming-collision discipline
Public-sector entity names collide across Italy far more than you'd expect (e.g. two unrelated organisations both abbreviated AMIU, two unrelated organisations both called ASIA, two unrelated organisations both called GAIA). Whenever a new candidate's name resembles an existing target's name, flag the collision explicitly in the new entry's own fields (not just a mental note) and cross-reference the entry number of the lookalike, so nobody merges or confuses them in a future session or in outreach. This applies equally to address sourcing (see above) - a collision that was correctly resolved for contact purposes can still resolve wrong when fuzzy-matched against an address registry, so re-check every flagged collision pair specifically at the address step too, not just once at sourcing time.

### Standard batch checklist
Run the right checklist for the phase you're actually in - don't let a sourcing batch quietly drift into drafting, or an enrichment batch into re-sourcing.

**Phase 1 batches (sourcing):**
1. Research and append new entries to `targets.py`, following the existing dict schema and wording conventions exactly, including an explicit ownership percentage where relevant.
2. Regenerate `targets_data.json`.
3. Regenerate any scratch CSVs the build scripts need, from source.
4. Append a new dated "Sources" block to the workbook build script documenting each new claim.
5. Rebuild both deliverables, re-run the xlsx formula-recalculation check (zero errors), convert the docx to PDF and visually spot-check for layout breakage.
6. Clean up scratch files, deliver both master documents, log the batch.

**Phase 2 batches (enrichment - the fill-in phase):**
Track three gaps per target: a **real named contact** (not a placeholder), a **real fleet-specific hook** (not a placeholder), and a **postal address**. Prioritise in this order: (1) targets with a hook but no contact - find the contact; (2) targets with a contact but no hook - dig for a fleet-specific fact (published fleet inventory, tender/gara documents, local news on vehicle procurement, sustainability/fleet-renewal reports); (3) targets missing more than one of the three. **Do not draft an email in the same pass, even when both contact and hook land together** - mark the entry "ready for Phase 3" and let the drafting pass pick it up deliberately, so there's a checkpoint between "the facts exist" and "the facts are trusted enough to send." Be honest in the file when a "hook" is really a governance/investment-cycle/operational-scale proxy rather than a confirmed vehicle fact - label it as such so a later session doesn't mistake it for verified fleet evidence. Re-run the KILL screen's ownership question on any entity where a hook or contact search surfaces new ownership information - this is where a previously-flagged "minority private shareholder" framing can flip to an actual majority-private KILL, as it did once on this project.

**Phase 3 batches (drafting):**
Draft only entries explicitly marked "ready for Phase 3." Draft in the recipient's language per the email doctrine. Update the Notes column and Open Decisions box for anything the drafting pass itself surfaces as newly risky.

### Handing off a long-running session
A programme like this can run a conversation long enough that starting a fresh session becomes worth the reset. Because the working files live in a session-scoped workspace, a fresh session needs the actual project files, not just a summary of them:
- Package the whole working folder (`targets.py`, `emails.py`, the two build scripts, the current deliverables, and any derived reference data the build scripts depend on) into a zip and deliver it.
- Write a companion Markdown briefing covering: current counts, the standing rules above (knockout rule, contact/email doctrine, naming-collision list, table-width/formatting fixes that must not regress), the exact regeneration commands for any scratch files, a short batch-history summary, and - most usefully - the **exact list of entry numbers still missing a contact, a hook, and/or an address, plus which phase each is currently in**, so the next session can start exactly where the last one left off without re-deriving the backlog from scratch or accidentally skipping a phase.

---


## Failure modes to avoid

- Writing to the mayor.
- Padding a target list with bodies that do not own their vehicles. Say plainly why a market is excluded instead.
- Stating limitation as fact.
- Naming a reference client without documented consent.
- Producing fleet figures without a date and source.
- Letting a paywalled article's search summary become an asserted fact - say when you could not read the primary source.
- Long emails.
- Forgetting that the person who agrees with you may not be the person who can sign.
- **Drafting an email before an entity's ownership, contact and hook are all independently settled.** This is what let a majority-private entity sit in the pipeline for three batches under a "minority shareholder" framing that was never actually checked against a real percentage.
- **Calling a batch a "clean finish" while the brief's own open-items section still lists things that further research could have resolved.** Only call something closed once it's actually been pushed as far as research can take it - a client who checks will notice the gap.
- **Carrying a regulator and its underlying operator as two separate targets** without confirming which one actually buys vehicles - this produces a redundant, weaker contact alongside the real claimant instead of one clean lead.

## Address check prompt for Claude Code (Stage 7d, new sheets only)
Only for a sheet that has no Address check columns yet. Paste into Claude Code with the batch sheet ID filled in. It writes results to Status and never overwrites an address. The DACH sheet already has the check (6 Oct 2026); there, resolve only the non-pass rows.

```
Task: verify the postal address of every "In batch" row in Google Sheet <SHEET_ID>, tabs Private and Municipalities, before the Pingen mail-merge file is built.

Setup
- Read the header row of each tab first; find columns by name (Organisation, Entity short name, Country, City, Street, Postcode, Status, In batch, Research notes). Do not assume column letters.
- Keep a LOOP-STATE.json file: last row done per tab, counts per result. Read it at the start of every pass. Stop after 50 rows per pass and save.

For each row where In batch is "Lion claim" or "Legalta":
1. Query Google Places (Text Search) with "<Organisation> <Street> <Postcode> <City> <Country>". Municipalities: "Rathaus <City>" or the named department (Bauhof, Feuerwehr) if Research notes name one.
2. Take the best match only if its name matches the organisation (ignore legal forms such as GmbH, AG, KG) and it is in the same city.
3. Decide:
   - pass: same street and postcode (house number may differ by formatting only)
   - moved: same organisation, different street or postcode in the same region
   - closed: business_status is CLOSED_PERMANENTLY or CLOSED_TEMPORARILY
   - not found: no confident match
4. Write to Status, appending to any existing text: "Address check: pass" / "Address check: moved to <street>, <postcode> <city>" / "Address check: closed" / "Address check: not found". Never edit Street, Postcode or City.
5. Log place_id, the formatted address and the date in LOOP-STATE.json.

Rules
- Batch writes: collect 50 Status updates and send them in one Sheets batchUpdate.
- Never trash, clear or reorder rows or tabs.
- At the end, print counts per result per tab and the list of rows that are not "pass". These rows are held until Nick or Thomas decides.
- Done when every In batch row has an "Address check:" value. Then add a dated line to the sheet's Read Me change log: "Address check run <date>: pass N, moved N, closed N, not found N".
```
