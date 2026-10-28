---
name: "outreach-followup"
description: "After a Legalta email batch or consented calling session: turn notes and transcripts into Gmail drafts, fix hooks and emails in the lead list, log dates and move contacted leads to the CRM."
---

# Outreach follow-up (Legalta, case AT.39824)

Use after any batch of cold emails or consented calls ("draft the emails", "draft the follow-ups", "move today's leads to the CRM", "outreach followup"), and for the scheduled follow-ups 5 and 10 working days later. Jobs in order: (1) lead-list fixes, (2) email drafts, (3) CRM move. Never send. Before redrafting anything, ask whether Nick has already sent the current version. Delete only drafts Claude created, and only after Nick says yes.

## Inputs (read every run)

- Templates and rules: Google Doc 1ozlnlpIPYfXKHifCkxWn0b7n9xnaTWCZzAxj--_Up5o (sections "The formula", "UK example email", "Compliance footer", "Follow-up email - rules", "Process flow", "Follow-up emails"). Nick edits this doc directly: the doc wins over this skill, and its wording is used verbatim. Never cut or reword Nick's text without listing the change in the reply.
- Legalta Fixed Facts: 1JOJP6tYmXE261bk6Z3a7vnc-CDtQEC-NKycodqM7udk. Wins on any factual conflict.
- Lead list, UK and Ireland: 14BTh7K2MDrbvj0ZN_dcliWuDotBWnF-GC2Y_HzRkS5Y (tab "UK private"). Find columns by header name, never by letter: Entity short name, Hook sentence EN, Contact 1 first name / last name / role / email, Contact 2 first name / email, Website, In our CRM already?, CRM notes, Emailed, Snail mailed, Phoned, LinkedIn, Fleet checked, PECR subscriber type, Call consent, Do not contact.
- Nick's comments in Contact 1 email and CRM notes (typed mid-call).
- Transcripts: Wispr Flow (rolling "UK calls" file) and Granola (one meeting per call). If the calls are in neither, say so and use the sheet notes.
- Fleet Check submissions: Google Sheet 1-Dkz9Daepr00JQEJkt1KibSBGdGjI4GrcxZnbK2g-I8 (tab Submissions; match on Email, Company name and Website; ignore test rows; read the Consent and Marketing opt-in columns), plus the Fleet Check notification emails in Nick's inbox.
- CRM: 1WTLfew1MFgHx2meQFmfGFSh0iIAAOiuBrsy93uK0Dwg, tab Leads.
- Cold Outreach Rules page (https://claude.ai/artifact/KKsc12mj1zNvQuTeQu1y7m): tab "Sending from Lion Claim" (footer, steps), one tab per market with its decisions (the UK tab first), and the Country chart (filter by Yes / Yes, if / Consent / Unclear and by channel). Sole traders are not in the chart; their rules sit in each country card.
- Do not contact list: CRM tab "Do not contact" (match on email and company domain). It is the source of truth; the lead list's Do not contact column only mirrors it.
- Process map: Lead Generation - Process Flow workbook 1vlPFUmFcZfKk6gfP3Pr9YSsm3N33hAVUc8UBwdELXQw, steps 11.1 to 11.4. Keep it in step with this skill.

## UK channel rules (decision 26 Oct 2026)

- Email: allowed to corporate subscribers (PECR subscriber type = Corporate: Ltd, plc, LLP, CIC, Scottish partnership, public body) without consent, with sender identity, an opt-out and privacy information (ICO B2B guidance). PECR subscriber type = Individual (sole trader, other partnership) needs consent or soft opt-in: no cold email. "Check legal form": confirm on Companies House before drafting.
- Calls: PECR reg 21A bans unsolicited marketing calls about claims management services without prior consent, businesses included. TPS and CTPS screening does not make a cold call lawful. Call only rows whose Call consent cell holds a date and source (asked for a call by email, booked through the calendar link, or ticked the Fleet Check opt-in). "Check: ..." in Call consent means confirm by email first. Never plan new UK cold calls.

## Step 1 - Clean the lead list

1. Move any email typed in CRM notes into Contact 1 email.
2. Clear email cells that hold only "1" or "2" (regex ^[12]$). Never touch a digit inside an address.
3. Check each email's domain against Website; fix obvious typos and list every change.
4. Check the hook against the formula doc. UK licence counts = "vehicles". Founding year only if 1997 or earlier.
5. Write the call date (YYYY-MM-DD) in Phoned only for calls made with Call consent. If a call log shows a call without consent, flag it to Nick; do not fill Phoned silently.
6. Fill PECR subscriber type for any row missing it, from the legal form in Organisation (Corporate / Individual / Check legal form).
7. Record new consent in Call consent as "YYYY-MM-DD, <source>" (reply asking for a call, calendar booking, Fleet Check opt-in).

## Step 2 - Email 1 (Gmail drafts)

Body: the doc's "UK example email", verbatim, with the row's hook. It has one call to action only: the two-minute Fleet Check, linked to https://legalta-europe.com/#checker. No phone line, invoice offer or testimonials in the body; phone, invoice and the compliance footer (Lion Claim GmbH details, data source categories, opt-out, privacy link) sit in Nick's signature. The footer is one fixed text (no per-email company name or source), copied from the formula doc's "Compliance footer" section.

Greeting ("Dear", never "Hi"; one name only):
- Contact 1 named: Dear {Contact 1 first name}.
- Email address names someone else (craig@, Rob.Clarke@): Dear {that person}.
- General inbox (info@, aol), no Contact 1: Dear {Contact 2 first name}.
- Transport or fleet group inbox, no named contact: Dear Transport Manager.
- Never address Contact 1 and Contact 2 together; never copy in the director.

Context sentence, word for word, only after a call the lead agreed to (Call consent filled). Cold emails have no context sentence and open with the hook. No dates ("today", "last week"), names of absent colleagues or other call detail, as these risk being wrong:
- A, the office pointed to this person: "I'm following up from my call with your office, who recommended I contact you."
- B, no fleet contact yet: "I'm following up on my call with your office and looking to connect with {Company}'s fleet manager."
- Call did not connect, or no call: no context sentence; open with the hook.

Subject: "Compensation for {Company}'s trucks bought 1998 to 2012" (Company' when the name ends in s). Founded after 1998: use the founding year, e.g. "GLJ Recycling's trucks bought 2007 to 2012". Group inbox with a named contact: prefix "FAO {full name} - ".

Sender and signature: the Gmail connector cannot set From and Gmail adds no signature to API drafts. So:
1. Create each draft with create_draft, body only (no "Kind regards", no signature).
2. In Claude in Chrome, open each draft (set location.hash to #search/in%3Adraft+to%3A<email>, then click the first visible row), open the From menu (div.J-JN-M-I in the last dialog) and choose Nick Graham <nick@legalta-europe.com> by dispatching mouseover, mousemove, mousedown, mouseup and click with clientX/clientY on the menu item (coordinate clicks miss: the CSS viewport differs from the screenshot frame). Gmail then inserts Nick's Legalta signature, including "Kind regards" and the compliance footer. Save and close (button aria-label "Save & close"). Changing From does not refresh the signature in a draft that already has one: edit .gmail_signature directly, then type a space and BackSpace in the body to trigger autosave.
3. Check every link in each draft before saving it: an href that starts https://www.google.com/url?q= is a Gmail redirect saved into the draft (found 26 Oct 2026 on all 47 UK drafts); replace it with the decoded q value and remove data-saferedirecturl. Test each distinct URL in the body and signature once per batch with curl -sSL -o /dev/null -w "%{http_code} %{url_effective}" and report the result. Never report a link as working, broken or different without testing it.
4. Run the browser work as a background loop inside the Gmail page (an async function on window that opens each draft, edits it, types a space and deletes it with document.execCommand to trigger autosave, then clicks Save & close), and poll its progress in calls under 40 seconds: a single call that runs longer times out. If a call fails with "Cannot access a chrome-extension:// URL", close the tab and open a new one.
5. Verify with Gmail searches instead of reading every body: subject:"trucks bought" -"HRB 22469" must return nothing, subject:"trucks bought" "Not for you" must return nothing (the old one-line signature), and the batch count must match. Then read one draft in full with list_drafts (DRAFT_VIEW_FULL) and confirm that the sender is nick@legalta-europe.com and the body contains "Partner, Legalta" exactly once and "Lion Claim GmbH" with "HRB 22469" (the compliance footer). If the footer is missing, stop and tell Nick.

Skip: not eligible, hung up, Do not contact column filled, on the CRM Do not contact tab, no email address, PECR subscriber type Individual (unless consent is recorded) or Check legal form (until checked), or an address type the Cold Outreach Rules page does not show as Yes or Yes, if for that country and recipient. Sole traders and partnerships of individuals stay in the market but follow the Sole traders section of the country card (email needs consent in most countries, so they usually get a letter instead). List skipped rows. Fill Emailed only once Nick confirms sending.

## Step 3 - Follow-ups (from the doc's "Follow-up emails" section)

Before drafting, check the Fleet Check sheet and Nick's inbox for Fleet Check notifications and replies. Anyone who replied, completed the Fleet Check, sent an invoice or asked not to be contacted gets no follow-up; note them in the reply and update the CRM stage. Anyone who asks for a call or ticks the Fleet Check opt-in: write Call consent (Step 1.7). For anyone who asked not to be contacted, propose a Do not contact row on the CRM tab (date, company, domain, email, country, scope: whole company, source), write it after Nick's yes, mirror it in the lead list's Do not contact column, and block the domain in the sending tool.

- Follow-up 1 (email 2) at 5 working days: the doc's text (Fleet Check link, proof with "some of Europe's largest listed companies" and the City of Zurich example, and the request to forward to whoever looks after the trucks). Draft it as a reply in the original thread.
- LinkedIn: parked (Nick, 22 Oct 2026). Only when Nick asks: send a connection request to the named contact with the doc's note (under 300 characters); click Connect only after Nick says yes for that batch. Never automate bulk requests.
- Follow-up 2 (email 3) at 10 working days: the doc's last note, with {year} = 1998 or the founding year, and the Fleet Check link. Then stop.
- Every email carries the Fleet Check link and the compliance footer.

Rules: Legalta branding only; never imply a guaranteed outcome; British English; no em dashes.

## Step 4 - Move contacted leads (active or closed) to the CRM

1. Check the CRM for duplicates (company name and domain).
2. Append one row per contacted lead with the next Lead ID ({COUNTRY}-0001 style). Map by header name: Company, Country Market, Lead Type, Sector, Workstream ("{Market} emails {Mon YYYY}"), Owner, Stage (CRM outcome codes, e.g. "6 Outreach sent", "Closed - not eligible"), Next Action, Due Date (move weekend dates to Monday), Contact Name, Email, Phone, Last Contact, Latest Outcome, Website, Personalization Hook, plus the outreach date columns, and PECR subscriber type and Call consent once Thomas has added those columns.
3. Match the formatting of the rows above exactly:
   - Extend the Leads alternating-colour banding (updateBanding on the existing bandedRangeId) to cover the new rows. Do not use copyPaste PASTE_FORMAT across the banding boundary: it fails because the banding would be copied twice.
   - Set vertical alignment MIDDLE, wrap OVERFLOW_CELL, font size 10 and row height 45 on the new rows (repeatCell plus updateDimensionProperties).
   - Keep the date validation and date format on the outreach date columns.
   - Check the result by reading back the effective background and vertical alignment of the first two new rows.
4. Write "Yes - {Lead ID}" in the lead list's In our CRM already? column.
5. Check that the CRM view tabs (Action Board, Live Leads, Needs Contact Info) include the new rows; raise any capped range.

## Column alignment

Emailed, Snail mailed, Phoned, LinkedIn, Fleet checked, then PECR subscriber type, Call consent, Do not contact: same names and order in every lead list, the template and the CRM. Research columns stay in the lead lists.

## Editing the doc

Nick often edits the doc at the same time. Prefer replaceAllText; for index-based edits, read the doc first and pass its revisionId as requiredRevisionId, and re-read if it is refused.

## Reply

Short: drafts created (count, sender, footer and links verified), skipped rows and why, consent recorded, Fleet Check completions found, email fixes, hook changes, CRM rows added, every change made to Nick's wording, anything suspicious. Then confidence, one way this could be wrong, one option not considered.