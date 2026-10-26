# CRM and registers - reading, matching and writing

## The CRM: Lion Claim Master Lead Registry - Lean CRM v3.1
Owner: Thomas. File: native Google Sheet v3.2, 1WTLfew1MFgHx2meQFmfGFSh0iIAAOiuBrsy93uK0Dwg (converted by Nick 1 Oct 2026; the old .xlsx v3.1 1UQOfNeQpjPo79DWp2nEmykOKlQ6mcWmA is retired). Team project: MD copy, refreshed weekly.

Tabs:
- Leads: one row per company, current state. Columns A to T are human-maintained (Lead ID, Company, Country Market, Lead Type, Sector, Workstream Campaign, Owner, Stage, Priority, Next Action, Due Date, Contact Name, Contact Role, Email, Phone, Last Contact, Latest Outcome, Est Eligible Trucks, Contact Status, Key Blocker Human Notes). Columns U to AB are AI background (Website, AI Company Summary, Personalization Hook, Eligibility Summary, Evidence and Source Links, Missing Information and Risks, AI Data Quality Confidence, Last AI Research). AI proposes, humans review; AI confidence is never eligibility.
- Activity Log: one row per interaction. Never overwrite history.
- Research Inbox: unqualified candidates (Queue ID RQ-xxxx). Assign a Lead ID only when a human promotes the row.
- Evidence Log, Action Board, Live Leads, Needs Contact, Archive, Guide: views and provenance. Do not edit views.
- Stages: 1 Research queued, 2 Researching, 3 Needs qualification, 4 Qualified, 5 Draft ready, 6 Outreach sent, 7 Recipient unresolved, 8 Engaged, then handover stages per Acquisition OS v1.1.
- Lead ID format: two-letter country prefix plus four digits (e.g. UK-0012). Check the highest existing number before proposing new IDs.

## Writing to the CRM
The CRM is an Excel file, so the Google Sheets connector cannot write to it. Until Thomas converts it to a native Google Sheet:
1. Produce paste-ready rows for Research Inbox (new candidates) and Leads (updates to existing rows), in the exact column order above, as an .xlsx (apply excel-polish: frozen header and ID columns) or a table in chat.
2. Produce Activity Log rows for anything sent or received.
3. Never invent a Lead ID for an unpromoted candidate.
Once converted, append via the Google Sheets connector and still show the rows to the human first.

Proposed Contacts tab (not yet in the CRM; see CRM Fields tab in the Process Flow workbook): one row per person, joined by Lead ID, holding up to 2-3 people per company with LinkedIn URL, email status, phone type, source and lawful basis.

## Matching and dedupe (before any row is proposed)
Load the data-clean skill if it is installed (e.g. /mnt/skills/plugins/data-clean/SKILL.md) and apply it to every new list. If it is not installed, apply these rules:
1. Match on company or registry number first (Companies House, SIREN, partita IVA, KVK, OIB, UID).
2. Then on normalised name (lower case, strip legal form such as Ltd, GmbH, S.r.l., S.A., remove punctuation) plus postcode or town.
3. Fuzzy name matches above about 90% similarity: mark "possible duplicate", do not merge automatically.
4. Check the Leads tab, the Research Inbox and the Archive. A match means update, not add.

## Saturation register
File: Legalta Market Saturation / Exclusion List (Google Sheet 1xL2j9fU1x2rwreZz_uL3v39rXHpslwgccgvpEdTfiiQ). Read its Read Me tab first: it holds the matching rules and the open to-do list.

Tabs:
| Tab | One row per | Used at |
|---|---|---|
| Rules | Company-wide rule by market and segment. Action: Exclude / Hold / Check / Deprioritise | Every stage |
| Entities | Named legal entity with an Action (Knock out / Hold / Check), status, date and source | Stage 4 list build, Stage 7, Stage 8 |
| Claims Competitors | Funder, law firm, association or aggregator running claims, with a link | Stage 2; Stage 6 (competitor, not channel); prior-claim question wording |

Order of checks: ICP Avoid tab hard disqualifiers, then Rules, then Entities.
- Match on country, organisation type and name together. A Landkreis and the Stadt of the same name are different entities.
- Add new entities straight to Entities (one tab only). Every "already claimed elsewhere" or "already a client" reply becomes a row.
- Pilot-specific rules (language filters, pilot exclusions) go in the pilot workbook, not the register.
- Market-level saturation lives in the Market Fit Matrix and the Competitor Saturation research, not the register.
- Lion Claim's own client list is not in the register yet: say so in every list deliverable.

## Segment vocabulary (Market Fit Matrix segments vs Data Sources sub-segments)
| Matrix segment | Data Sources sub-segments |
|---|---|
| Municipalities | Municipal waste and street cleansing; Fire and rescue; Water and sewerage; Roads and highways; Inter-municipal consortia; Ports and airports |
| Traditional logistics | General road haulage; Removals |
| Fuel and heating oil | Fuel and heating oil distribution |
| Food and drink | Food delivery (bakery, meat, dairy, wholesale); Food storage and cold chain; Brewing and drinks distribution |
| Construction | Construction (plant hire, builders' merchants, scaffolding, concrete, skip hire) |
| Waste management | Waste collection under private concession |
| Agriculture | Agriculture, forestry and timber |
| Events and film | Event production, stage, film and touring |
| Couriers | Courier and parcel |
| Fishing | Fishing and fish transport |
| Laundries and charities | Industrial laundries; Charity collection fleets; Hospital and institutional logistics |
| Small trucks | Cross-cutting: 6-7.5t fleets in any of the above |
