---
name: italy-private-fleet-outreach-cc
description: "[CC] Adapts the truck-cartel municipal outreach method to privately-owned Italian fleets (owner-operated hauliers 10-50 trucks, mid-size logistics/courier fleets 50-200 trucks) per the Legalta ICP. Triggers on: 'find haulier/logistics/courier leads in Italy', 'write outreach to an Italian fleet owner', 'is this haulier a qualified target', 'run a saturation check', 'expand the Italy private-fleet list', or any request to research or approach Italian private-sector truck owners for the AT.39824 claim. Requires bash/filesystem (targets.py/emails.py source files, xlsx/docx builds) — will not run in a chat-only environment. For Italian municipalities, fire services or utilities, use truck-cartel-municipal-outreach-cc instead — do not duplicate sourcing across the two skills for the same Italian entities."
---

# Italy Private Fleet Outreach — Road Freight, Haulage, Logistics, Construction

## Quick start — how to invoke this

- **"Find [N] haulier/logistics leads in Italy"** → Phase 1. Start with Registro Imprese / Camere di Commercio filings and sector associations, not individual company names.
- **"Enrich the Italy private-fleet list"** → Phase 2, contact/hook/address plus the saturation check (run that first, before the other three).
- **"Draft the ready ones"** → Phase 3 only, per the same "not until marked ready" rule as the municipal skill.
- **Not this skill**: Italian municipalities or public utilities (`truck-cartel-municipal-outreach-cc`); non-EEA fleet owners or the general insolvency-administrator segment (out of scope — see the Latvia section below for the one part of that which is now active, and its blocker).
- **Output**: same Word brief + Excel target list mechanics as the municipal skill, reoriented tabs — see Deliverables below.

Adapts the municipal three-phase outreach method (Source → Enrich → Draft) to Italy's private-sector fleet owners, per the Legalta ICP (`Legalta - Ideal Customer Profile and Customer Segments`, owner Nick Graham, draft v1, 18 Aug 2026). **That document was a draft when this skill was written and Legalta's working documents move fast — re-read the current version in Drive (see Legalta project memory for the file ID) before treating the ten open ICP questions in the Deliverables section as current, rather than assuming the 18 Aug draft still holds.** Two segments in scope for the first batch:

- **Owner-operated road haulier (Primary segment)** — 10-50 trucks, family or single-owner, founded before 2005, owner 45-65. Road freight, construction haulage or agriculture. Turnover typically under €10m.
- **Mid-size logistics/courier fleet (Secondary segment)** — 50-200 trucks, professional management (finance director + fleet manager), courier/distribution/contract logistics/waste, has an asset register.

Everything in `truck-cartel-municipal-outreach-cc` about the underlying case (Commission decision, fines, CJEU rulings, the 1998–2012 window, the six manufacturers) still applies — it's the same cartel, the same investor, the same funding model. What changes is **who you're talking to and why they say yes**. A municipal officer needs cover to act; a haulage owner needs to believe it's real, that it costs nothing, and that it won't eat his afternoon.

---

## The core insight this rests on

A municipal officer's category error is thinking he doesn't own trucks. A haulier's category error is different: he assumes a European Commission cartel case from a decade-plus ago is either (a) not real, (b) already resolved, or (c) for someone bigger than him. He is not confused about ownership — he knows exactly which trucks he bought and when. He is skeptical that anyone owes *him* money, because every cold approach he's had before promised money and cost him time or worse.

That skepticism, not ignorance, is the objection every email has to clear. The municipal playbook's weapon was a legal citation (CJEU C-588/20). Here the weapon is **proof that this is boring and administrative, not a scheme** — a case number, a named peer who's already doing it, and a plain statement of what it costs him (nothing, and less than two hours).

---

## Workflow — same three phases, same discipline

Run Source → Enrich → Draft exactly as in the municipal skill, with the same rule: **do not draft until an entry clears Phase 2 in full.** The failure mode is identical — drafting the moment a hook appears produces ready-to-send emails for companies that later turn out to have already claimed, gone insolvent without a successor, or bought everything second-hand.

### Phase 1 — Source targets
Find and qualify against the screen below. Record legal form (SRL, SPA, ditta individuale), fleet size band, sector, and entity status (trading / insolvent / liquidated — see below, this segment does **not** kill on insolvency the way it would elsewhere). Do not research contacts, hooks or addresses yet.

### Phase 2 — Enrich
Same three gaps as the municipal skill, adapted:
1. **Named decision-maker** — owner/MD for the 10-50 truck band; finance director, fleet manager or procurement lead for the 50-200 band (see contact doctrine).
2. **Fleet-specific hook** — labelled honestly as confirmed evidence or a proxy, per the same GOVERNANCE-RESET / INVESTMENT-CYCLE / OPERATIONAL-SCALE PROXY taxonomy.
3. **Postal/registered address** — via Registro Imprese / visura camerale (see below).

Add a fourth gap specific to this segment, ahead of the other three in priority order: **prior-claim / saturation check.** Run this before spending time on a hook or a contact — see the saturation discipline below.

### Phase 3 — Draft
Only entries marked "ready for Phase 3." Italian language, native register, per the email doctrine below — materially shorter and plainer than the municipal register.

### Before any of the above
Re-verify case status (same rule as the municipal skill), **and** check the Court of Milan proceeding (Sezione Imprese A, judgment deposited 11.01.2026) for any update, since it is this segment's single strongest peer-proof hook and its status can change.

**Corrected detail (refreshed 15.09.2026, confidence 90% across five independent Italian trade/legal-press sources — logisticamente.it, uominietrasporti.it, trasportoeuropa.it, dejalex.com, trans.info):** the judgment covers **14** Italian haulage companies, not 18, against **Iveco, Scania, DAF and MAN by name** — brought via CNA Fita's 2017 collective action, to which roughly 3,000 companies had joined; only these 14 reached judgment. The court quantified an **8% overcharge** on purchase price (4% residual on some post-cartel-window purchases), plus interest and revaluation, averaging **~€13,000 per truck**. Passing-on and tax-benefit defences were both rejected, with the burden placed squarely on the manufacturers. **This is a first-instance judgment and remains appealable** — say "a Milan court has already quantified and awarded damages" in outreach, not "this is settled law," and re-check appeal status before every batch.

**New competitive-intelligence item, not previously in this skill:** as of 4 September 2026, Confartigianato Trasporti announced that the first 18 of its member hauliers had completed onboarding with litigation funder **Libra — Finanziamento del Contenzioso** and received payment, with a further 29 pending. This is a separate funder and a separate claims programme from CNA Fita's, actively paying out right now. Two implications: (1) it is itself usable as a "this is real and already paying out" proof point in outreach, stated generically without naming Libra or Confartigianato as a Legalta reference; (2) any Confartigianato-affiliated haulier is now materially more likely to already be in a competing process — treat Confartigianato/CNA Fita membership as a prompt to ask the saturation question directly, not as a target-sourcing channel to approach cold.

---

## Qualification screen — adapted from the Legalta ICP

**KILL**
1. Were the trucks bought **new**, with the company as first registered owner? (Same as municipal — used purchases are out regardless of segment.)
2. Acquired, leased or hire-purchased between **1 Jan 1998 and 31 Mar 2012**?
3. Over **6 tonnes**, DAF / Daimler-Mercedes / Iveco / MAN / Renault-Volvo / Scania chassis? Trailers, semi-trailers and light vehicles under 6t are out.
4. **Has the claim already been assigned, sold, or settled** — with any provider, not just a competitor to Legalta? Unlike the municipal segment, this is common here: hauliers are the segment competitors have worked hardest, and Italy is explicitly a "priority but not yet saturated" market per the ICP, meaning some fraction has already gone. Ask directly; do not assume silence means no.
5. **Explicit opt-out on file?** Hard stop, no exceptions, regardless of any other qualifying fact.

Note what is **not** a KILL question here, unlike the municipal screen: ownership percentage / public-private split is irrelevant (this is private industry), and there is no concessionaire-vs-owner distinction to run — a haulier that owns its trucks, owns its trucks.

**UNLOCK / do-not-discard**
6. **Insolvent, liquidated or ceased trading?** Per the ICP this does **not** disqualify — a claim can survive in an estate or with a successor entity. Do not drop these; route them to the insolvency-administrator angle instead of the owner-operator angle. Confirm who is currently entitled to pursue the claim (administrator, liquidator, or a successor company) before treating the entry as workable.
7. Sector beyond core haulage — construction haulage, agriculture, event/stage logistics, film production, fishing, waste collection under private concession. The ICP flags these as under-approached; don't filter the search to generic "trasporti" company names only.
8. Fleet acquired through a **leasing company or dealer intermediary** rather than direct manufacturer purchase — still qualifies per the ICP (lease agreements are accepted evidence), don't discard on that basis alone.

**FLAG**
9. Do invoices, lease/hire-purchase agreements, order confirmations, registration certificates, fixed-asset registers or bank statements survive? Same evidence-grade logic (A–D) as the canonical manual — grade every entry, don't just note yes/no.
10. **Fleet size above ~1,000-2,000 trucks** — per the ICP, "almost certainly already approached and decided, one way or the other." Treat as a soft kill: verify prior-claim status aggressively before investing further, and deprioritise even if unresolved.
11. Who can actually sign? Sole owner/MD for the primary segment (fast — this is the whole point of that segment's priority); for the secondary segment, confirm whether it's the finance director alone or needs a wider internal sponsor, since the ICP notes decisions there "go through several people."

### Saturation discipline (do this before drafting an entry)
The ICP sets an explicit market-exit rule: leave a market once roughly **80-90% of approached companies turn out to have already claimed**. Track this as a running ratio for the Italy private-fleet programme specifically (separately from the Italy municipal ratio, if that programme is also running) — the two buyer types are not saturated at the same rate, and conflating them will trigger a false exit signal in one direction or mask a real one in the other.

---

## Where the volume sits (Italy-specific)

Ordered roughly by how efficiently one contact yields qualifying volume:

- **Registro delle Imprese / Camere di Commercio filings** — every SRL/SPA above a size threshold files annual accounts including fixed-asset schedules; a "automezzi pesanti" or "autocarri" line item, cross-referenced against incorporation date (pre-2012, ideally pre-2005 for the primary segment), is a fast qualifying signal before any fleet-list research.
- **Albo Nazionale degli Autotrasportatori** (the national register of licensed road-haulage operators) — Italy's equivalent of the "national haulage operator register" the ICP's Registry Verification Lookup automation targets. Lookup-only per the ICP notes (not bulk-exportable), so use it to *verify* a candidate found elsewhere, not as a primary discovery source.
- **Sector associations as channel classes** (mirrors the municipal skill's "channel classes" insight — one contact, many members): Confartigianato Trasporti, FAI — Conftrasporto, Assotir, Assoautotrasporti, ANITA (logistics/intermodal), Unatras (the umbrella of the main haulage associations), and on the construction-haulage side ANCE and its regional Collegi. These map directly to the ICP's **Intermediary and association gatekeeper** segment — treat a good association contact as worth dozens of primary-segment leads, exactly as the Belgian hulpverleningszones or German VKU function in the municipal programme.
- **Court of Milan, Sezione Imprese A (11.01.2026)** — 18 transport companies already in follow-on proceedings against Iveco and others. This is simultaneously a peer-proof hook (use it in emails) and a source of named companies worth checking directly for who else in their sector is watching that case.
- **Tender/gara records and local business press** for construction-haulage firms with public-works contracts — a company doing public infrastructure work usually has a documented, dated fleet-acquisition history via the contracting authority's records, which solves the documentation-survival problem the ICP flags as the real blocker.

---

## Contact doctrine — private sector version

The municipal rule ("write to whoever owns the balance sheet, copy nobody") still holds in spirit, but the org chart is different.

| Segment | Who | Why |
|---|---|---|
| Owner-operated haulier (10-50 trucks) | The owner or managing director, directly, by name | Per the ICP: "owner is usually the sole decision-maker." There is no one else to route through — the fastest cycle in the entire target universe, faster even than the German Eigenbetrieb. |
| Mid-size logistics/courier (50-200 trucks) | Finance director first, fleet manager as a secondary/supporting contact, never the reverse | The ICP is explicit: nobody internally "owns" the question, records are split between finance, fleet and a former leasing provider, and a named sponsor is needed before anything moves. Finance director is the person with the balance-sheet incentive and enough authority to convene the others. |
| Either segment, if channel-first | The association's own contact (regional secretary, chamber representative) | Per the Intermediary segment: they evaluate slowly and by reputation, want to know what members get and what their exposure is — treat the first conversation as a partnership pitch, not a lead-gen pitch, and do not present a member list request until trust is established. |

**Practical differences from the municipal doctrine:**
1. Phone is a live channel here, not a fallback. The ICP notes the owner-operator "may answer a phone call" even while deleting cold email — for the primary segment, plan a call-first or call-after-email approach, not email-only.
2. Do not lead with a legal citation to the owner-operator. He is not evaluating case law; he is evaluating whether you are a scam. Lead with the peer and the "no cost" line.
3. For the mid-size segment, a written, evidenced case lands better than a call — the ICP notes this segment "will research the provider before replying" and "responds better to a written, evidenced case than a phone pitch." Inverse of the primary segment.

---

## Email doctrine — adapted

### Anatomy (primary segment — owner-operated haulier)
1. **Open on the fact that this is real and old news to someone like them** — a named peer haulier, or the Milan court case, in the first line. Not a legal citation.
2. **State what it costs him: nothing.** One sentence, no adjectives, exactly as the municipal rule — but move it earlier in this version, because "what does this cost me" is the ICP's literally-quoted first question.
3. **State the time cost: under two hours, and you do the paperwork.** The ICP is explicit that this segment has "no spare admin capacity to chase historic records" — this is the single biggest lever, more than the money itself.
4. **The peer proof**, stated plainly — "[Named haulier / a transport company like yours] is already part of a case in Milan."
5. **Ask for a short call**, not a meeting, not a signature. Offer to call him rather than asking him to reply to an email.

Target length: **120-160 words**, shorter than the municipal 180-220 — the ICP describes an owner who "deletes cold email."

### Anatomy (secondary segment — mid-size logistics/courier)
Closer to the municipal register: written, evidenced, addressed to a finance director who will read it properly and check the provider first.
1. Open on a fact specific to them — fleet size, a recent expansion, a new finance director, sector context.
2. State the legal basis in one sentence (Commission decision, CJEU C-588/20 if special-purpose vehicles are plausibly in their fleet).
3. Name the Milan proceeding and, where relevant, a comparable mid-size logistics firm.
4. Address the internal-fragmentation problem directly: offer explicitly to do the document reconstruction across finance/fleet/former leasing provider, since the ICP names this as the actual blocker, not willingness.
5. Address duplication risk directly: state plainly that you will check for any prior claim or assignment before proceeding, since the ICP notes this segment worries "how it looks if a claim is mishandled."
6. Ask for a call with the finance director and fleet manager together, not an unstructured "20 minutes."
Target length: 180-220 words, as the municipal doctrine.

### Rules common to both
- Italian, native register — plain and direct for the primary segment, professional-but-warm for the secondary segment. Avoid the bureaucratic register that works on a Comune.
- No exclamation marks, no "risk-free," no marketing superlatives — same rule as municipal, doubly important here since this segment has explicitly "been burned before by cold approaches promising money."
- Never state a guaranteed outcome or a specific payout figure as fact. The ICP's own working assumption (€4,000-5,000 realistic per truck, not the €10,000 ceiling) is an internal planning number, not something to put in an email — same discipline as the municipal skill's ban on showing the value model to a target.
- Give a real way to say no: "if this isn't a fit, feel free to say so — no further contact."

### Worked example — primary segment, structure to imitate

> **Oggetto:** Un tribunale di Milano ha già riconosciuto 13.000 euro a camion per il cartello dei costruttori
>
> Gentile Sig. [Nome],
>
> le scrivo per un fatto vecchio, non per una proposta commerciale.
>
> Un tribunale di Milano ha riconosciuto a 14 imprese di autotrasporto un risarcimento medio di circa 13.000 euro per ogni camion acquistato tra il 1998 e il 2012 da Iveco, Scania, DAF o MAN — per gli accordi sui prezzi che la Commissione Europea ha sanzionato con 2,93 miliardi di euro.
>
> Non le costa nulla verificare se riguarda anche lei: il costo legale, i rischi e la ricostruzione della documentazione sono a nostro carico.
>
> Le basta una telefonata di venti minuti. Posso chiamarla io questa settimana?
>
> Se non fa al caso suo, mi dica pure di no — non la contatterò di nuovo.

Note what it does: opens on the quantified Milan figure (not a bare legal citation), states cost is zero in one plain sentence, states who does the work, offers to call rather than asking for a reply, and gives a real way to say no — all per the anatomy above. 68 words in the body excluding the subject and sign-off, comfortably inside the 120-160 word target once a greeting and a personalisation line (fleet size, region, or a named peer) are added.

### Hook sources, in priority order for this segment
1. **A named peer in the same sector or region** who is already claiming or has claimed — strongest lever by far for the primary segment.
2. **The Milan court proceeding, with the number** — "a Milan court has already awarded roughly €13,000 per truck to 14 haulage companies" is a materially stronger opener than a bare case citation. Works for both segments, stronger for the secondary segment where a written legal basis matters more. Say "a Milan court," not "the Milan court" — it is one first-instance decision among several proceedings, and it is still appealable.
3. **A sector association's own endorsement or event** — if Confartigianato Trasporti, Assotir, ANITA etc. has said anything publicly about the case, that is a stronger opener than a cold legal citation.
4. **A structural fact about them** — recent fleet expansion, new ownership, a generational handover (common in the 45-65-year-old owner-operator segment), a recent finance-director appointment.
5. **A closing-window fact** — document retention schedules, an upcoming fleet electrification/renewal that will trigger disposal of the old asset register (same closing-window logic as the municipal skill).

---

## Honesty rules — carried over unchanged, two additions

All ten MANDATORY honesty rules from `truck-cartel-municipal-outreach-cc` apply without modification (limitation is a legal position not a promise; never overstate a reference; never state an unverified figure as fact; never show the value model; "no cost, no risk" is not a guaranteed outcome; raise your own weak points; flag grant clawback where relevant; use published contact channels — drop the procurement-law flag, that one's municipal-only). Two additions specific to this segment:

11. **Never claim or imply this is a large-firm-only process.** The ICP names this exact misconception ("assumed it was for large firms only") as a live objection — correct it plainly rather than avoiding the topic.
12. **Never let the owner-operator's low administrative capacity become a reason to skip his consent or understanding.** "I'll handle everything" must not slide into acting on assumed authority — get an explicit yes and a signed instrument (funding agreement + PoA) exactly as with any other segment; the low-effort promise is about paperwork reconstruction, not about consent.

---

## Deliverables — same package, reoriented tabs

Follow the municipal skill's Word brief + Excel target list structure and mechanics (Calibri, navy `1F3864` headings, `targets.py` / `emails.py` source-of-truth files, PDF verification pass, column-width discipline on any table edit). Reorient content:

- **Qualification tab**: replace the municipal ownership-percentage KILL question with the assignment/settlement and opt-out KILL questions above; add the insolvency-routing UNLOCK note so a liquidated entity isn't silently dropped.
- **Target List tab**: add a **Segment** column (Owner-operated haulier / Mid-size logistics/courier / Association channel) and a **Saturation check** column (checked / prior claim found / clear), since the 80-90% exit rule needs a per-entry record to be auditable across a multi-batch programme.
- **Risk register**: replace municipal-specific risks (procurement law, passing-on defence, grant clawback) with this segment's own — prior-assignment risk (higher base rate here), insolvency-entitlement risk, and the reputational risk of a mishandled claim for the mid-size segment.
- **Open Decisions box** (per the municipal skill's discipline): the ten open ICP questions listed in the source sheet (close-rate by fleet-size band and sector, top reasons deals died, per-country saturation baseline, average eligible trucks per closed company, pipeline-stage timing, the non-EEA EEA-nexus test, UK post-Brexit eligibility, top objections, investor-vs-legal-position gap, which intermediaries worked) are this programme's real open decisions — carry them in the brief exactly as listed, and update/retire them as Thomas and the back office answer them, per the same discipline that stops the municipal brief's box from becoming a growing, never-closed list.

---

## Latvia insolvency-administrator segment — scoped, not yet buildable

Confirmed 15.09.2026 as the next segment to extend into, ahead of Bulgaria/Romania/Portugal or the general non-EEA fleet-owner segment. This section holds the shape of that work; it does not authorise running it yet.

**Why this differs from every other segment in either skill.** The insolvency-routing UNLOCK note already in this skill's qualification screen (item 6) treats insolvency as an edge case discovered mid-programme for an otherwise ordinary target. Latvia inverts that: the segment's whole premise is entities where an **insolvency administrator, not the original owner, is the counterparty** — that is the entry point, not an exception to route around.

**The blocker, and it is a hard one, not a research task.** Legalta's standing Litigation Funding Agreement carries a representation that the client is **not** subject to insolvency proceedings. A segment built entirely around insolvency administrators as counterparties sits in direct tension with that clause. This is a legal-drafting question for Güray/MMG, not something a better-written email can route around — **do not build outreach for this segment until Güray confirms how, or whether, the LFA's insolvency representation is varied for an administrator-as-counterparty structure.**

**Time pressure, stated plainly.** The Latvia insolvency practitioner window was understood, per late-August conversations, to close around **1 October 2026** — roughly two weeks from when this skill pass was run. If the LFA question isn't resolved with enough runway to source, enrich and draft properly before that date, flag that the window may already be too tight for a first cohort rather than compressing the three-phase discipline to force a fit.

**Known contacts, not yet a target list:** Karlis (Baltic market access) and Carlos, via contact Monte (Latvia outreach partner) — per Legalta project memory. Confirm with them whether Latvia's national insolvency register is bulk-searchable or lookup-only before assuming either Italy discovery method transfers directly; Latvia is currently logged as lookup-only for fleet-size data specifically, which may or may not extend to insolvency-administrator records.

**Once the LFA question is resolved,** building this out is new-skill territory — a distinct qualification screen (who currently holds standing to pursue the claim: administrator, liquidator, court-appointed trustee, or a successor entity) and a register-driven discovery method, not an adaptation of this file's KILL/UNLOCK/FLAG list. Route that to skill-creator, not another skill-enhancer pass.

## What this skill deliberately does not yet cover

- The **non-EEA fleet owner** segment from the ICP, and Bulgaria/Romania/Portugal as markets — confirmed lower priority than Latvia as of 15.09.2026; different discovery methods and, for non-EEA, a different legal-nexus question (the EEA-nexus test) that warrant their own batch programme.
- The **municipal and public-sector fleet** segment inside Italy — already covered by `truck-cartel-municipal-outreach-cc`; don't duplicate sourcing effort across the two skills for the same Italian entities.
- A live-sourced target list. This file is the adapted methodology only; running Phase 1 against real Italian companies is a separate, explicit next step.