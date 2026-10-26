---
name: "legalta-lead-gen"
description: "Legalta's master lead generation skill for EU truck cartel compensation claims (case AT.39824), for any country and segment: find, qualify, score, enrich, contact leads, hooks, addresses, CRM, market entry."
---

# Legalta lead generation

Find, qualify, score and contact companies and public bodies that bought or leased new trucks (6t and above) from DAF, Daimler, Iveco, MAN, Volvo / Renault or Scania between 1998 and 2012, for Lion Claim's funded claims. Legalta is not a law firm: never imply a guaranteed outcome.

The process lives in the Legalta Lead Generation - Process Flow workbook (Google Sheet 1vlPFUmFcZfKk6gfP3Pr9YSsm3N33hAVUc8UBwdELXQw). This skill is the engine that runs it. Every stage below maps to a Process Flow step.

## 1. Intake (ask only for what is missing, in one message)
- Country or country group.
- Segment and sub-segment. Use Market Fit Matrix segment names (see references/crm-and-registers.md, vocabulary table).
- Goal: qualify existing leads / build a new list / find contacts / draft outreach / all.
- Batch size and deadline (e.g. 600 letters by Monday).
- Owner, from the Who Does What tab. If the market has no owner, stop and ask Nick.

## 2. Tool check (works in chat, Cowork and Code)
Check which tools exist before starting, and say in one line which fallbacks you are using.

| Need | First choice | Fallback |
|---|---|---|
| Read Google Sheets and Docs | Google Drive / Sheets / Docs connectors | Project knowledge MD copies in /mnt/project; else ask the user to paste |
| Read the CRM | Sheets connector on Google Sheet v3.2 (1WTLfew1MFgHx2meQFmfGFSh0iIAAOiuBrsy93uK0Dwg) | Team project MD copy (weekly; state its date) |
| Write to the CRM | Sheets connector, only after listing every change (tab, row, column, old, new) and getting a yes; post the change log after | Paste-ready rows |
| Scrape public pages | Firecrawl connector | web_fetch; then bash curl + Python |
| Bulk downloads, cleaning, matching | bash + Python | Step-by-step instructions for a human |
| Lookup-only registers | Claude in Chrome or Playwright (Code) | A lookup worklist for a human |
| Phone numbers | Main company number from the website (imprint, contact page) | places_search (Google Places); trade directories |
| Emails | Treg email waterfall (Stage 7, "Email waterfall") | Company website via Firecrawl or web_fetch (imprint, team, contact pages); press releases |
| LinkedIn profiles | Parked (Nick, 22 Oct 2026) | - |

No paid contact databases or seats (decision 1 Oct 2026), with one exception: Treg pay-per-call email lookups and checks on the team's prepaid balance (decision 21 Oct 2026, after a 50-row UK test: $0.014 per usable named email against $0.099 for Claude + Firecrawl). Check the balance with Treg balance before a batch.

## 3. Documents (load only what the current stage needs)
Full list with IDs: references/doc-index.md.
- Always, before anything else: Legalta Fixed Facts (Google Doc 1JOJP6tYmXE261bk6Z3a7vnc-CDtQEC-NKycodqM7udk). It wins over every other document, this skill included; if they disagree, show both and ask.
- Always: Process Flow workbook (Who Does What, Existing Work, Data Sources, Market Scoring), the CRM, references/case-and-rules.md.
- Letters: Legalta Outreach Letters - Master Template Letter (Google Doc 1lG8Z9QApWtVx0yOmvasbKh4swoa2TRZMbN7zhXPKwDc). Country-neutral English master with slots; the only letter text anyone edits. Each non-English market has its own translation doc.
- Stage 2: Thomas's Truck Cartel Claims Market Research, Market Fit Matrix, Saturation register (Google Sheet; Rules, Entities, Claims Competitors - see crm-and-registers.md).
- Stage 5: Acquisition OS v1.1 (authority on gates and scoring), ICP and Customer Segments.
- Stage 9: the segment playbook, the Training FAQ and required-documents files for plain-language claims.

## 4. The stages (never skip a gate)

Stage 0 - Start in the CRM (Process Flow 1 to 1.2)
- Filter Leads, Research Inbox and Archive by country and segment. Read their Activity Log rows.
- Read the Existing Work tab and any market file for this country.
- Output: one paragraph on what already exists (counts by stage, last contact dates, earlier lists, open questions).

Stage 1 - Qualify existing leads first (Process Flow 2 to 2.1)
- Re-run the hard gates (references/case-and-rules.md) on every existing lead for the market. Grade evidence A to D and score using Acquisition OS v1.1.
- Clear the backlog: no reply after 14 days, undeliverable, or dead (close with a reason).
- Output: proposed Leads updates and Activity Log rows. Do not start new research until this is done or the user says skip.

Stage 2 - Size and saturation (Process Flow 3 to 3.2)
- Start from Thomas's figures. Research deeper only where his document has nothing for this segment. Record source and date for every number. Be conservative.
- Check saturation at market level (Saturation register; Matrix; competitor claim vehicles). The prior-claim gate is per company: any company or public body that has started, assigned or settled a claim for any truck is out (Thomas, 1 Oct 2026).
- Gate: Thomas gives go / no-go. Do not build a list for a market he has not approved, unless the user says it is already approved.

Stage 3 - Evaluate data scraping potential (Process Flow 4 to 4.1)
- Read this country's rating on the Market Scoring tab and its Data Sources rows (filter Country, then Segment).
- High: download and scrape. Medium: mix with association and manual research. Low: lead with intermediaries.
- Fewer than 4 live source types: run the Research Prompt tab for the country first and propose new Data Sources rows.
- Output: the chosen sources, the method per source (references/sources-and-data.md), expected list size.

Stage 4 - Build the target list (Process Flow 5)
- Extract from the chosen sources. Keep registry numbers.
- Load the data-clean skill if installed and apply it; otherwise use the match rules in references/crm-and-registers.md.
- Remove anything already in the CRM (Leads, Research Inbox, Archive) and anything the Saturation register marks Knock out, Hold or Exclude (Rules tab first, then Entities).
- For letter campaigns: generate well beyond the target (wide and cheap), but research hooks only for the rows chosen to send (Stage 7b). Generate well beyond the target (e.g. 500+ per bucket), score, then surface the top N. Do not force equal splits across buckets. Default priority: niches first, municipalities second, everything else third.

Stage 5 - Screen and score (Process Flow 6 to 6.1)
- Hard gates, evidence grade A to D, four scores (evidence, opportunity, conversion, relationship, 0 to 5 each), priority.
- Segment rules: references/segment-public-sector.md or references/segment-private-fleet.md.
- Gate: Thomas reviews the top tier in one batch.

Stage 6 - Map intermediaries (Process Flow 7)
- Associations, dealers, fleet maintenance chains and accountants that reach many fleets. references/segment-intermediaries.md.
- An association running its own claim is a competitor, not a channel.

Stage 7 - Find contacts (Process Flow 8 to 8.1)
- 2 to 3 people per company, from free sources plus the Treg email waterfall below; compliance checks before writing. references/contacts-and-compliance.md.
- Who to look for, in this order (ICP and references/contacts-and-compliance.md). Fill Contact 1 and Contact 2 with the first roles you can name and record each role:
  Owner-run fleet (10-50 trucks): Contact 1 transport or fleet manager, then operations or logistics manager, then office or finance manager. Contact 2 owner or managing director, then another director from the company register.
  Mid-size fleet (50-200+ trucks): Contact 1 fleet or transport manager, then operations director. Contact 2 finance director or CFO, then managing director, then procurement or legal lead.
  Public body: Contact 1 fleet, depot or works manager. Contact 2 finance or commercial director, then legal or procurement lead. Never the mayor.
  Name sources, in order: company register officers (Companies House for UK directors), the operator licence (UK transport manager), the company website, then Treg's find-by-role lookup (about $0.025) only if none of these names anyone.
- Email waterfall (UK test, 21 Oct 2026; results in the Lead Enrichment - Cost Model 1000 Leads sheet 1Hz0R2hFKwaV_R6CxhGo_RkjxVFAdXUE7l6R96qkImTQ, tab "Treg vs Firecrawl Test - 2026 OCT 21"). For each row, stop at the first step that gives a valid address:
  1. Named person: Treg call on treg.people.email.find (POST, body {"domain","first_name","last_name"}, headers X-Treg-Route-Verify: true and X-Treg-Route-Max-Cost: 0.10; pass an idempotency_key on retries). Accept only a "valid" result at the company's own domain, or at a domain the company clearly owns. Check the person is the right one: a result at another company's domain (e.g. royalmail.com) is a namesake, so reject it. If the email domain differs from Website, keep it but add "Email domain differs from website; check before sending (Treg, <date>)" to CRM notes. If the result is "unknown", re-check it once with treg.people.email.verify at the end of the batch (2 of 2 unknowns passed on recheck in the UK test) before moving on.
  2. No named person after the role order above, or step 1 gives invalid, still unknown after the recheck, or the wrong person: assume the shared inbox is info@<domain> and check it with Treg treg.people.email.verify (body {"email"}, about $0.0015). Use it only if the result is valid.
  3. info@ fails: use Firecrawl (search plus scrape of the contact, imprint and about pages) to find a published shared inbox (enquiries@, sales@, customerservice@, office@), then check it with treg.people.email.verify. Use a valid result. A published inbox that checks as unknown or valid-risky may be used, but note "unverified" in CRM notes. Never use a parent company's inbox without a note.
  4. Nothing valid: leave the "@domain" prefill and write "No verified email found (Treg, info@ and Firecrawl all failed, <date>)" in CRM notes.
  Record the method for every row (treg named / info@ check / Firecrawl shared inbox / none found). Run in batches of 5 and report cost per usable email at the end. Expect about 31 seconds per row; Treg charges for misses at one provider, so cap spend with the Max-Cost header.
- Legal form: record it for every row. Sole traders and partnerships of individuals stay in the market (Nick, 23 Oct 2026); tag them "Sole trader" in Status and choose channels from the Sole traders row of the Cold Outreach Rules page (in most countries letter, sometimes phone; email needs consent almost everywhere).
- PECR subscriber type (UK; decision 26 Oct 2026): set it from the legal form in Organisation. "Corporate" for Ltd, Limited, plc, LLP, CIC, unlimited companies, Scottish partnerships and public bodies; "Individual" for sole traders and other partnerships; "Check legal form" for associations, trading names and anything unclear, until Companies House confirms it. Corporate rows may get cold email; Individual rows need consent first (ICO B2B guidance). Other countries: use the Cold Outreach Rules page row instead and leave the column blank.
- Phone and emails are required for every In batch row (rules in the template section of 7a): one Phone value or "none found"; Contact 1 email and Contact 2 email filled with a found address or the "@domain" prefill. A row is not done until both are filled. A phone number is for consented calls and letters' reference only: it never licenses a UK cold call.
- LinkedIn profiles: parked (Nick, 22 Oct 2026). Email is the primary cold channel and Legalta's LinkedIn presence is too new to help. Do not search for or link profiles unless asked.

Stage 7b - Enrich: evidence for every row selected for sending (Process Flow 8, before any letter)
Carried over from Thomas's original skills (Phase 2 "Enrich"), tightened by the DACH depth test of 5 Oct 2026 (25 niche rows: the deep scan raised 8 grades, added 6 named contacts and disproved 3 figures the light scan had marked as confirmed).
- Light scan (homepage and obvious sub-pages, keyword snippets) is for ranking the longlist only. Every row selected for sending (the Top N per tab) gets a deep scan. Do not use "light first, deep only if weak": light scans produce false positives.
- Deep scan, run by the agent itself, one entity at a time, no human step: web_fetch the homepage and every page about fleet, logistics, delivery, company, history, team and jobs (Fuhrpark, Flotte, Fahrzeuge, Logistik, Zustellung, Über uns, Unternehmen, Geschichte, Chronik, Team, Karriere, Jobs) and read each in full; web_search "<name> <city> Lkw Fuhrpark" and "<name> <manufacturer names> Lkw"; web_fetch the best independent results (manufacturer press rooms and customer stories, DVZ, Trans aktuell, Verkehrsrundschau, Lebensmittel Zeitung, Getränke Zeitung, Brauwelt, regional papers, job adverts, company registers). Use press results if they exist; if none, write "No press coverage found" and move on. Never block a row or pad it. Claude's own web_search and web_fetch are the default; Firecrawl is optional, for speed. Snippets pulled by a script are pointers, not evidence.
- Municipalities: the public-sector method in references/segment-public-sector.md (council minutes, budgets and fleet lists, vehicle tenders, Bauhof, Stadtwerke and fire brigade fleets, local press), plus rules R05, R08, R13.
- Research notes (one cell per row) follow Thomas's Italy column I: exact fleet count with breakdown by type or weight class, vehicle types, manufacturers, founding year or generation and handovers, named contacts (fleet or logistics manager, managing director), the ICP band it falls in, and caveats (group ownership, insolvency, public ownership, prior-claim risk). Every fact is followed by its source as an inline hyperlink. End with "Checked <date>, deep". A tracker or earlier-scrape figure stays unconfirmed until a public source is linked, and says so.
- Research quality grade (A-C) (one column, A / B / C / Insufficient evidence):
  A = public fleet count plus at least two of: vehicle types or breakdown, manufacturer, named contact, founding year or generation.
  B = public fleet count alone, or a dated proxy fact (investment, fleet renewal, manufacturer story) without a count.
  C = only an unconfirmed figure (tracker, earlier scrape) or a vague fleet mention.
  Insufficient evidence = nothing usable, or the evidence shows no qualifying fleet (vans only, machinery dealer, not a fleet operator).
  Grade sits beside ICP match and is never merged with it. Hook strength for the channel skill, strongest first: named peer already claiming; court award with figure; sector association statement; own fleet facts; proxy.
- This stage collects evidence. Hooks are generated from Research notes in Stage 7c, never written by hand from memory.
- Track four gaps per row (named contact, evidence, postal address, phone and email). Re-run prior-claim and ownership checks when research surfaces new facts.
- Batches: run as a loop, not a prompt (find the work, do one row, verify, record, repeat): a LOOP-STATE file read first on every pass, a measurable done condition (every In batch row has Research notes with at least one opening source link, a Research quality grade, a Phone value and both Contact email cells filled), a verification step that opens each link before marking the row done, a reviewer sub-agent or second pass grading a 10% sample, items needing a human decision parked in a "needs Nick" list, and a stop after N rows per run. 10 rows per pass in Claude Code (/goal with that done condition, or claude -p in a shell loop), or 40 to 60 per chat turn with a pre-crawl cache. Save after each batch.

Stage 7c - Hook sentences (letters; run after 7b, before Thomas reviews)
- Run scripts/hooks.py on the exported tab (Sheets get_values JSON or CSV): python3 scripts/hooks.py rows.json --tab Private (or --tab Municipalities). It writes hook_en, hook_de and a reason per row.
- Rules (from Fixed Facts and the Master Template Letter): one sentence ending with the fixed clause ", you are likely to have bought from the manufacturers involved in the EU truck cartel."; no amounts, eligibility wording or cartel dates; founding year only if 1997 or earlier, read from the Founded column or from notes next to "founded / established / gegründet" (never "since"); founded 2012 or later holds the lead; counts are current or dated before 2012; trucks by chassis (tippers, tractor units, refuse trucks, fire engines, truck-mounted cranes), never trailers, low-beds, excavators, telehandlers or vans; German uses "Sie" or "Ihr Unternehmen", never the company name; Germany and Austria start "da", Switzerland "Da" with Lastwagen, ss and 2'500.
- Known traps the script guards against, each found in the DACH pilot: thousands separators ("1,800" read as 800); weights read as counts ("26t trucks", "18t tipper"); emission classes ("Euro 6 tractor units"); model numbers ("Volvo L 385", "eActros 300", "Saurer 330 and 290"); counts of trailers or swap bodies; "since 2013" read as a founding year.
- Write hooks to "Hook sentence EN" and "Hook sentence DE" (columns right after Research notes). For every batch row left blank, append "Hook blank: <reason>." to Research notes (no usable facts / no fleet evidence / founded in <year> / only trailers named). When a hook is later added, remove that note.
- Then run scripts/validate_hooks.py on a fresh export. Zero problems, or every remaining line explained to Nick, before the batch goes to Thomas. Also hand-read a 10% sample against the notes: the script checks numbers and rules, not meaning.
- Entity short name must be filled for every batch row (the subject line uses it): cleaned trading name, no legal form.

Stage 7d - Postal address check (letters; after 7c, before the mailing-house file)
- Check every batch row's address against Google before any mail-merge file is built. The DACH sheet already holds the pattern (6 Oct 2026, Google Address Validation in Claude Code): columns Maps name, Maps street, Maps postcode, Maps city, Address check, Maps link, beside our Street, Postcode, City.
- Address check values: "pass" (matches Google), "pass: our address kept", "differs" (Google has another street or postcode), "review: not confirmed to building" or "review: postcode differs", "street missing" (no street in our sheet).
- If the columns already exist, do not re-run: resolve only the rows that are not "pass". Find a street for "street missing" rows (company imprint or legal-notice page, town hall site), confirm "differs" and "review" rows against the organisation's own website, then update the result.
- New sheets: add the same columns and run the check in Claude Code (prompt in references/deliverables-and-batches.md). Never overwrite Street, Postcode or City silently; hold every row that is not "pass" until a human decides.

Stage 8 - Update the CRM (Process Flow 9)
The CRM is the Google Sheet v3.2 (1WTLfew1MFgHx2meQFmfGFSh0iIAAOiuBrsy93uK0Dwg, owner Thomas). Never append or edit without first listing every proposed change (tab, row, column, old value, new value) and getting a yes; after writing, post the same list as a change log.
- New candidates to Research Inbox; updates to existing Leads rows; people to the proposed Contacts tab; every send or reply to the Activity Log.
- Show rows to the human before any write. Never overwrite history.

Stage 9 - Draft outreach (Process Flow 10 to 11)
- Letter campaigns: draft the letter templates in the same run as the lead list, so Thomas approves both together (see "Lead list package" below). Other channels: only when a human asks.
- Thomas approves which leads and which channel.
- Letters: fill the market's Master Template Letter (variant slots, merge fields, hooks from 7c). Never redraft the body per batch; propose changes to the master in suggestion mode. Before handover: render the letters to PDF and check each fits one page, no {{ }} field is left, no instruction text sits in a letter body, and the bulk-post provider's address window (Pingen) lines up. Sample-check one letter with no hook and one with the longest hook.
- Emails and other channels: the email or letter doctrine in the segment playbook, in the recipient's language, then humanise-writing and fact-check on every claim.
- Email is the primary cold channel (Nick, 22 Oct 2026). Markets are opened one country at a time (Nick, 26 Oct 2026): read the country's row and card on the Cold Outreach Rules page (https://claude.ai/artifact/KKsc12mj1zNvQuTeQu1y7m), fact-check every link against the regulator or statute and note the date checked, then record the market's decisions (channels, consent, footer translation, local representative) on its own tab of that page, with the UK tab as the model. Sole traders are left out of the Country chart; include them at the country's human check only if the lead list for that country has some. Then apply the page: email only where the cell for that address type (company inbox or named employee) and recipient type (company or sole trader) is Yes or Yes, if, and meet its condition. UK: cold email only to rows with PECR subscriber type Corporate. Where email needs consent, send a letter first with an opt-in QR code. Every email and letter carries the Lion Claim compliance footer (formula doc 1ozlnlpIPYfXKHifCkxWn0b7n9xnaTWCZzAxj--_Up5o, section "Compliance footer"), one fixed text with no per-message fields.
- Calls (decision 26 Oct 2026): no UK cold calls. PECR reg 21A requires prior consent for claims management calls, businesses included, and TPS or CTPS screening does not replace it. Call only rows whose Call consent cell holds a date and source (asked for a call, booked through the calendar link, ticked the Fleet Check opt-in). Other countries: follow the Cold Outreach Rules page.
- Never send. Drafts only.

Stage 10 - Review (Process Flow 14)
- Weekly: leads added, qualified rate, replies, already-claimed share (counted in companies). Update the market file (references/market-file-template.md). Recommend continue, switch segment or stop.

## 5. Reference routing
| If the task involves | Read |
|---|---|
| Eligibility, case law, honesty rules, commercial model | references/case-and-rules.md |
| Public bodies (waste, fire, water, roads, consortia) | references/segment-public-sector.md |
| Private fleets and own-account niches | references/segment-private-fleet.md |
| Associations, dealers, accountants | references/segment-intermediaries.md |
| Choosing and using data sources, scoring a market | references/sources-and-data.md |
| CRM structure, dedupe, Saturation register, segment names | references/crm-and-registers.md |
| Contacts, GDPR, PECR, TPS | references/contacts-and-compliance.md |
| Word brief, Excel target list, long multi-batch runs | references/deliverables-and-batches.md |
| Where a document lives | references/doc-index.md |

## 6. Other skills this skill uses
Skills cannot call each other directly. Read the other skill's SKILL.md when it is installed and follow it; if it is missing, use the fallback.
- data-clean: Stage 4 and Stage 8 dedupe (fallback: match rules in crm-and-registers.md).
- fact-check: Stage 2 figures and every outreach claim.
- humanise-writing: Stage 9 emails and any new master-letter wording.
- google-workspace: before any Google Doc, Sheet or Slides edit.
- outreach-followup: drafting, sender switch and verification of emails after a batch.
- Lead lists: a fresh Google Sheet per batch in the batch folder; always follow excel-polish. Earlier rule: Google Sheet copied from the approved template, styled to excel-polish standards.

## 7. Rules that override everything
- Honesty rules in case-and-rules.md. No guaranteed outcomes. No invented peers, figures or quotes.
- Prior claims are checked per company: any started claim puts the whole company out (Thomas, 1 Oct 2026).
- Check the CRM Do not contact tab before every batch; a match on email or company domain is a hard stop. Mirror each match in the lead list's Do not contact column (the CRM tab stays the source of truth).
- No UK cold calls without Call consent (PECR reg 21A).
- Test every link before reporting on it or putting it in a message (curl, follow redirects). Gmail can save its own google.com/url redirect into a draft: links must point straight to the destination.
- UK data protection: Lion Claim has no UK office, so it needs a UK representative (UK GDPR art 27); the "occasional and low risk" exemption does not fit a running campaign. Options and risks are on the UK tab of the Cold Outreach Rules page. Open until Lion Claim decides.
- Humans decide: Thomas approves markets, top-tier leads and drafts. Never send anything.
- Every spreadsheet output: freeze the header row and the identifying columns.
- File names: "Subject (context + purpose) - artefact type - YYYY MMM DD", no underscores.
- British English. Hyphens with spaces, never em or en dashes.
- If two Legalta documents disagree, show both and ask. Do not silently pick one.

## 7a. Lead list package (every batch, every market)
- Copy "Legalta Lead List - Template v2" (below) with Drive copy_file into the batch folder and fill the copy. Never build an xlsx.
- Tabs: Read Me (purpose, status, how to approve, how rows were chosen, letter link, summary formulas, pilot-only exclusions, sources, Related documents at the bottom as real links), one tab per category, Automations (hidden). No separate Summary, Exclusions, Sources or CRM tabs: existing CRM leads sit in their category tab with the CRM ID in Status.
- Approval is a Status value ("Approved by Thomas"). Thomas approves before anything else happens.
- Letters come from the market's Master Template Letter. In the same run, add any new hook examples and open decisions to the master; do not create a separate templates doc per batch.
- No mailing-house files (Pingen CSV or similar) until Thomas has approved the list and Lion Claim / MMG have run their own client clash check; then only on request. Lion Claim does not share its client list.
- Share Google Drive links only. Never upload deliverables to Slack or other chat tools.
- Data quality before handover: one row per legal entity, one letter per group (dedupe by legal name, website domain and managing director); drop non-fleet organisations (petrol stations, museums, clubs, offices); apply language rules; set postcodes as text. Never fill a cell with a guess: leave it blank and write "check" in Status. If the remaining candidates are weak, deliver fewer rows and say so.
- Edit cells in place in shared files. Never clear and rewrite a tab or Read Me that people edit.

Template: "Legalta Lead List - Template v2" (Google Sheet 1BK_FW4amcmY8NgatUw_y41GN2rxDsEakQtlHBAtVKVc). One Leads tab for all categories (filter on Category), an Examples tab, a Taxonomy tab, a Decisions tab and a Read Me with the definitions. Column order, widths and hidden columns copy the UK and Ireland lead list, tab UK private (Google Sheet 14BTh7K2MDrbvj0ZN_dcliWuDotBWnF-GC2Y_HzRkS5Y, Nick, 20 Oct 2026). 50 columns (26 Oct 2026):
Category | Sub-segment | Organisation | Entity short name | Country | Region | ICP match | Fit score (max 15) | In batch | Status | Decision needed (see Decisions tab) | Research quality grade (A-C) | Fleet size | Fleet size basis | Research notes | Hook sentence EN | Hook Sentence DE | Phone | Contact 1 title | Contact 1 first name | Contact 1 last name | Contact 1 role | Contact 1 email | Contact 2 title | Contact 2 first name | Contact 2 last name | Contact 2 role | Contact 2 email | Website | Postcode | City | In our CRM already? | CRM notes | Founded | Street | Population | Earlier scrape figure (unconfirmed) | Maps name | Maps street | Maps postcode | Maps city | Address check | Maps link | Sub-segment detail (before taxonomy) | Emailed | Snail mailed | Phoned | PECR subscriber type | Call consent | Do not contact.
(The UK private tab also has LinkedIn and Fleet checked between Phoned and PECR subscriber type.)
Hidden by default: Entity short name, Hook Sentence DE, Postcode, City, Street, Population, Earlier scrape figure, Maps name, Maps postcode. Find columns by header name, never by letter. Frozen: header row and the first three columns.
Sub-segment and Founded apply to companies, Population to municipalities, Region to all; leave a column blank where it does not apply. Never merge them.
Contacts: one row per organisation, up to two named people. Contact 1 = operational champion (Fuhrparkleiter, Logistikleiter, fleet or transport manager, Bauhof or works manager; Thomas: a champion inside the organisation is the biggest unlock). Contact 2 = owner, Geschäftsführer, managing director or finance director (public bodies: finance or commercial director, never the mayor), following the role order in Stage 7. If no name is found, the function sits in Role. The channel skill decides whether to write to one or both. No Approve? or Ready to send? column: approval is a Status value ("Approved by Thomas"); send readiness is decided in the channel skill.
Phone (one column, required): the main company number (decision 22 Oct 2026: no personal mobiles bought through Treg), international format (+49 89 ...). Order: website imprint or contact page, then places_search, then trade directories (WKO, Companies House, Gelbe Seiten). If none of these gives a number, write exactly "none found". Never leave the cell blank on an In batch row.
Emails (Contact 1 email and Contact 2 email, required): run the Email waterfall in Stage 7 (Treg named, then info@ checked by Treg, then a Firecrawl shared inbox checked by Treg). Website, press releases and LinkedIn remain the fallback when Treg is unavailable. A pattern (firstname.lastname@) counts only if a published address at the same domain confirms it; note "pattern" in Research notes. If the contact is a role without a name, use the general company address (info@, office@). If no email is found, prefill "@" plus the Website domain without www (e.g. "@haubis.com"), so the caller types only the name before the @ when a receptionist gives it on a call. Never invent the local part.
PECR subscriber type (dropdown: Corporate / Individual / Check legal form): set in Stage 7 from the legal form; UK only. Call consent: "YYYY-MM-DD, <source>" once the lead has asked for a call, booked one or ticked the Fleet Check opt-in; "Check: <reason>" when a call-back request needs confirming by email first; blank means no calls. Do not contact: date and reason when the lead has opted out or must not be contacted; mirrors the CRM Do not contact tab.
Fleet size: the best evidenced truck count (number only); Fleet size basis: its source and date. Decision needed: the Decisions tab ID when a row waits on a team call.
Fit score (max 15, sourcing stage): segment fit, size signal, country priority, address and website found, no exclusion hit. Rule from 5 Oct 2026: breweries and bakeries with no delivery-fleet signal on their own site lose 3 points; clear microbreweries and brewpubs are excluded as too small.
Status is written by the agent (or Thomas): "Excluded: reason", "Hold: reason", "Check: reason", "Address missing", "Researched", "Approved by Thomas", "Clash check passed". Hook sentence EN and Hook Sentence DE sit right after Research notes. No source or source-type columns; wrap Research notes and Status; all URLs as hyperlinks. The email-finding method is recorded in CRM notes (Stage 7), which also answers a GDPR access request asking where an address came from.
Deliverables default to Google Sheets and Google Docs created directly in the batch's Drive folder. Never xlsx or docx unless asked (the team has no Microsoft licence).

## 7b. Working across chat, Cowork and Claude Code
- One live file per artefact. Before editing any sheet, re-read its tab names and headers: another session may have merged tabs, moved columns or rewritten rows since your last read (DACH, 6 Oct 2026: a Code session merged two tabs and added 123 hooks while chat was editing).
- Write a short change log in the file's Read Me (date, session, what changed) after every bulk edit, so the next session can see it.
- Long loops (enrichment, hooks, address checks) run in Claude Code with parallel agents; chat sessions review, decide and fix. Each Code run ends with the validator output pasted into the change log.
- Facts change in Fixed Facts first, then everywhere else. Never fix a fact only in a letter or a sheet.

## 7c. QA gate before anything goes to Thomas
1. scripts/validate_hooks.py: no unexplained problems.
2. Every batch row has Entity short name, a hook or a "Hook blank" reason, an address check result, a Phone value (number or "none found"), both Contact email cells (address or "@domain" prefill) and, for UK rows, a PECR subscriber type.
3. Letters render to one page each; no unfilled fields or instruction text; Fixed Facts wording matches the letter.
4. 10% sample of hooks read against the notes by a second pass.
5. Change log written.

## 8. What to hand back at the end of each run
- What was done, by stage, in five lines or fewer.
- Files: CRM-ready rows (Leads, Research Inbox, Contacts, Activity Log), target list, any market file update.
- Decisions needed from Thomas or Nick, as a short list.
- Confidence per key figure, and which sources were Blocked or Down.