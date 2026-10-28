---
name: "software-vendor-evaluation"
description: "Use when comparing software/SaaS vendors or tools for a team decision (CRM, email platform, MCP server, etc.) - builds a weighted, sourced comparison artefact with TCO at real volumes."
---

# Software vendor evaluation

Sibling of `shopping-comparison-table`. Use that skill for physical products (condition, retailer listings, product photos). Use this one for software, SaaS, APIs and integrations, where the decision turns on cost at real volume, data handling, lock-in and fit to a defined job.

Reuse the shopping skill's build mechanics (sortable table, live filter, verdict cards, update banner, footnotes) but apply the rules below. Minimum font size 15px in any artefact; body 16px.

## 1. Frame before researching

Confirm, or state as assumptions if already given:

- **The job(s)**. Name each job the tool must do. If two jobs pull in different directions (e.g. warm drip vs cold outreach), build one table per job rather than forcing one winner.
- **Real volumes**: users/seats, records, sends, API calls, at normal and peak. Price every vendor at the tier that covers peak, never the headline entry price.
- **Must-haves** (disqualify if absent) and **nice-to-haves** (tiebreak only).
- **Constraints**: budget ceiling, data residency (EU/EEA default for Moonflake/Legalta), existing stack it must connect to, who maintains it.
- **Weights**: ask for or propose a weighting across the criteria below, so the recommendation is traceable.

## 2. Criteria to research per vendor

1. **Price at real volume**: the qualifying tier, annual vs monthly, add-ons needed to meet must-haves (e.g. warmup sold separately).
2. **Total cost of ownership**: hidden costs outside the subscription (mailboxes, domains, seats, implementation time, who maintains it). Show the calculation.
3. **Functional fit** to each named job, with the specific feature that meets or misses it.
4. **Data and compliance**: hosting location, DPA availability, GDPR posture, certifications (SOC 2, ISO 27001) where published. Write "not confirmed" rather than infer.
5. **Security of access**: for anything touching live data (MCP servers, integrations), read/write scope, permission model, whether source is inspectable, audit status.
6. **Integrations/API**: connects natively to the named stack, via Zapier/n8n, or not at all.
7. **Lock-in and exit**: data export, contract length, cancellation terms.
8. **Support and viability**: support channels by tier, maintenance activity (commits, release cadence) for open-source tools, company age/size where relevant.
9. **Reviews**: G2 (and Capterra if useful) rating plus review count. Note when review populations differ so ratings are not read as like-for-like.
10. **Trial**: free trial or free tier length, so the team can test before buying.

## 3. Build-vs-buy check (canivibecodeit)

Run after the shortlist is set and before building the artefact.

1. **What to check**: every shortlisted vendor, plus any single component that drives a big share of TCO or is sold as a separate add-on (e.g. a warmup tool, an enrichment API, a scheduling layer). Skip disqualified vendors.
2. **How**: load the `canivibecodeit` skill and run its batch mode on that list. Follow its rules in full: no building, no guessed verdicts.
3. **Unlisted tools**: report "not listed". Ask before submitting to canivibecodeit.com (it is a public form submission); never submit without an explicit yes.
4. **If any verdict is YES**: add a "Build it ourselves" row to the relevant job's table and score it on the same criteria and weights as the vendors:
   - Price at real volume = hosting + any APIs/models it calls at peak volume.
   - TCO = build time (from the verdict, doubled as a conservative buffer) x an hourly value agreed with the user, plus ongoing maintenance hours per month and a named owner. Show the calculation.
   - Functional fit = the verdict's "what you lose" mapped against the must-haves. A lost must-have disqualifies the build row, as it would a vendor.
   - Data and compliance = self-hosted means we become the controller/processor for that data: hosting location, backups, access control and DPA chain all need an answer. Default amber until named.
   - Security, support and viability = amber by default (no vendor support, bus factor of one) unless a technical owner is named.
   - Lock-in = green (we own the code), unless it depends on a single paid API.
   - Reviews and trial = "n/a - self-built"; cite the canivibecodeit verdict, vote count and date instead.
5. **KINDA or NOT REALLY**: no row. List the verdict in the footnote so the team sees it was checked.
6. A YES verdict is crowdsourced, single-source evidence. It can justify a row, never a recommendation on its own; the build row wins only if it beats vendors on the weighted score after the conservative TCO.

## 4. Verification rules

- Prices, limits and hosting from the vendor's own pricing/legal/help pages. Date every figure.
- At least one independent source for any claim that decides the recommendation (e.g. category placement, deliverability capability). Vendor blogs count as marketing.
- When sources disagree, show both and plan on the conservative figure.
- Never fabricate a link, rating or price. Use "no verified link" or "not confirmed".

## 5. Build

- One table per job, plus a TCO/sizing panel where hidden costs matter. Include any "Build it ourselves" row from step 3, visually marked as self-built.
- Colour-coded badges: green meets the criterion, amber partial or unconfirmed, red fails.
- Highlight the recommended row; verdict cards per job, plus a "one tool for both?" card when relevant, and a "build or buy?" card for any job with a build row.
- Footnote defining any jargon, listing what was and was not verified, and listing canivibecodeit verdicts for every tool checked.
- Publish as an Artifact; republish the same file for revisions and bump the version banner.

## 6. Deliver

In chat: the recommendation per job in one line each, confidence %, the one assumption most likely to change the answer, and what still needs a hands-on trial or a technical owner's review. If a build row exists, state the break-even point (months until build beats the best vendor on TCO). List any unlisted tools awaiting a yes to submit. Offer a short team summary, caveman style, under 100 words.