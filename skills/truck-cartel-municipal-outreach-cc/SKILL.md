---
name: truck-cartel-municipal-outreach-cc
description: "[CC] Sources, enriches and drafts hyper-personalised outreach to EU public-sector truck owners (municipalities, fire services, utilities) for the AT.39824 truck cartel claim, on behalf of Lion Claim / Legalta. Triggers on: 'find municipal/public-sector leads in [country]', 'expand the target list for [market]', 'write outreach to a city/fire service/utility', 'run a Phase 1/2/3 batch', 'is this public body a qualified target', or any request to research or approach European public bodies for truck cartel damages. Enforces strict source-then-enrich-then-draft staging, a postal-address sourcing method, and a public-ownership KILL check with an explicit percentage threshold. Requires bash/filesystem access (targets.py/emails.py, xlsx/docx builds, PDF QA) - will not run in a chat-only environment. For Italy private-sector fleets, use italy-private-fleet-outreach-cc instead - same case, different qualification screen and email register."
---

# Truck Cartel — Municipal Lead Research and Outreach

Generates qualified public-sector leads for EU truck cartel damages claims (European Commission Case AT.39824) and writes hyper-personalised outreach emails in the recipient's own language, on behalf of **Lion Claim / Legalta**.

Use when asked to find municipalities or public bodies to approach, to write outreach for them, to research a market, or to expand an existing target list.

## Quick start — how to invoke this

- **"Find [N] municipal targets in [country]"** → runs Phase 1 (source). Start with the channel classes and discovery methods below before individual city names.
- **"Enrich the [country] list"** or **"close the gaps on batch [N]"** → runs Phase 2 (contact, hook, address).
- **"Draft the ready ones"** → runs Phase 3, and only Phase 3 — will refuse to draft anything not marked "ready for Phase 3."
- **"Is [named body] a target?"** → runs the qualification screen only, no drafting.
- **Not this skill**: private hauliers, logistics or courier fleets in Italy (`italy-private-fleet-outreach-cc`); anything about the value model, commercial split, or Lion Claim negotiation (that lives in Legalta project memory, not here).
- **Output**: a Word strategy brief and an Excel target list, built from `targets.py`/`emails.py` source-of-truth files — see Deliverables below. Nothing is sent; this produces drafts for Nick's sign-off only.

---

## The core insight this whole approach rests on

A city does not think it owns trucks. It thinks it owns refuse collection vehicles, street sweepers, gritters, jetting units, tipper trucks and fire appliances. Underneath every one of those bodies is a MAN, Mercedes, Iveco, Renault, Volvo, DAF or Scania chassis — and since 1 August 2022 the Court of Justice has held expressly that those vehicles are covered.

That category error is why this segment is underworked. Every email should be built to correct it.

**Why public bodies convert better than hauliers:**

- **They bought new.** The funding agreement requires the client to be first registered owner of a new vehicle. Municipalities buy new through public tender almost without exception; a large share of private hauliers fail on exactly this criterion.
- **They keep records.** Procurement files, fixed asset registers and audit trails survive far longer than a small haulier's paperwork, and retention is a legal duty rather than a habit.
- **Volume in one signature.** One relationship replaces a hundred small ones.
- **They can be given a non-commercial reason to act.** A public officer's real risk is being criticised for a decision. Framing this as a duty to at least *examine* a recoverable asset inverts that: examining is safe, ignoring is what needs justifying.
- **They talk to each other.** Municipal associations and peer networks are dense and trusted. One named reference travels across a country in a way it never does in haulage.

---

## Workflow — three staged phases, never interleaved

The single biggest lesson from running this at scale (105 targets, 20 batches on the Italy market): drafting an email the moment a hook appears, before the entity's qualification is fully settled, produces ready-to-send drafts for entities that later turn out disqualified or too risky — and a brief whose "open decisions" section never stops growing because nothing is ever forced to a close. Run every market as three separate phases, and do not draft a single email until Phase 3.

### Phase 1 — Source targets
Find and qualify entities against the screen below. Record identity, legal form, ownership structure (with an actual **percentage**, not a public/private binary — see the qualification screen), and evidence of a heavy fleet. Do **not** research contacts, hooks, or addresses yet, and do not draft. A target only enters the list once it clears every KILL question.

### Phase 2 — Enrich
For every sourced target, close three gaps in parallel across the whole list before moving to Phase 3:
1. **Named contact** — by legal form (see contact doctrine), with the source and date it was confirmed.
2. **Fleet-specific hook** — a fact true only of them, labelled honestly as confirmed evidence or as a proxy (GOVERNANCE-RESET / INVESTMENT-CYCLE / OPERATIONAL-SCALE PROXY) if no hard fleet figure could be found.
3. **Postal address** — see the address-sourcing method below. Needed for mail-merge and for the deliverable's Notes column.

An entry is "ready for Phase 3" only when it has a real contact, a real (or honestly-labelled proxy) hook, and no open qualification question. Track this per-entry as an explicit status, not something inferred from reading the whole file.

### Phase 3 — Draft
Once, and only once, an entry is ready: draft its email in the recipient's language (see email doctrine). Batch the drafting pass separately from research — don't draft opportunistically inside a research session, because a fact found five minutes ago has not yet been cross-checked against the ownership/collision/duplication risks that Phase 2 is supposed to catch.

### Before any of the above: re-verify case status
Case law moves. Before touching a target list, search for developments since the knowledge base below — new BGH or CJEU rulings, new municipal judgments, limitation developments, and whether any target is already claiming.

### Verify and flag, continuously
Produce a verification log distinguishing verified from estimated. Never let an unverified figure pass silently into an email, and never let a target reach Phase 3 carrying an unresolved qualification question.

---

## Case knowledge base

### The decision
- **European Commission Case AT.39824**, decision 19 July 2016. Fines €2.926bn against MAN (immunity, €0), Volvo/Renault (€670m), Daimler (€1,009m), Iveco (€495m), DAF (€753m).
- Scania did not settle; separate decision 27 September 2017, €880m. CJEU dismissed Scania's final appeal 1 February 2024 — now binding.
- **Infringement period 1997–2011**, EEA-wide. Covers **medium (6–16t) and heavy (over 16t) trucks**.
- Conduct: coordinating gross list prices, timing of Euro III–VI emissions technology introduction, and passing on emissions compliance costs.
- Not covered: light vehicles under 6t, trailers and semi-trailers, buses and coaches, after-sales services, used truck sales.
- Joint and several liability — each cartelist is liable for the others.

### Precedents that make the municipal pitch
Lead with the one that fits the market.

| Authority | What it establishes | Use where |
|---|---|---|
| **CJEU C-588/20**, *Landkreis Northeim v Daimler*, 01.08.2022 | Specialised trucks **including household refuse collection vehicles** are covered. Also concrete mixers, tipper chassis, flatbed chassis. Brought by a German district authority. | Everywhere. This is the citation that kills the "we don't own trucks" objection and needs no local legal context. |
| **LG Hannover**, 18.12.2017, **18 O 8/17**, *Stadt Göttingen v MAN* | First German court to award truck-cartel damages to anyone — and the claimant was a **city**, for **fire service, street cleaning and waste** vehicles. Affirmed municipal Kartellbetroffenheit; rejected the "only gross list prices were fixed" defence. Crucially: Göttingen's contracts contained a **15% liquidated damages clause** for cartel collusion, held **valid** because 15% corresponds to a typical average cartel damage. | Germany and Austria. Best municipal reference there is. |
| **LG Berlin**, 15.06.2023, **16a O 1/20 Kart**, *Berliner Stadtreinigung* | First German judgment to **quantify** the damage: ~200 MAN and Iveco trucks, 5% of net purchase price, ~€1m total, ~€5,000 per vehicle. Expert: Lademann & Associates. | Germany, especially against an Eigenbetrieb or AöR — same legal form. |
| **BGH**, 09.07.2024, **KZR 98/20** (also cited as *LKW-Kartell IV*) | No comparative market analysis required to plead damage; leasing and used purchases do not exclude a claim. **The DStGB publicly welcomed this from an explicitly municipal perspective.** | Germany. The DStGB endorsement is what a works manager shows their Kommunalreferat. |
| **BGH**, 12.05.2026, **KZR 6/24** | Bundled assignment-based claims (the FinancialRight/claims-vehicle "Sammelklage-Inkasso" model) permitted in principle, but a court may order separation where bundling defeats effective legal protection — the underlying case had 3,000+ assignors from 21 countries and 70,000+ purchase events. | Have a two-sentence answer ready. Lion Claim uses direct representation under power of attorney, not assignment to a collection vehicle — structurally less exposed. Confirm framing with the law firm. |
| **Court of Milan**, Sezione Imprese A, 11.01.2026 | First-instance damages judgment (**not yet final — appealable**) for 14 Italian haulage companies against Iveco, Scania, DAF and MAN, brought via CNA Fita's 2017 collective action (~3,000 members joined the broader action; only these 14 reached judgment). Quantified an **8% overcharge** (4% residual on some post-cartel purchases) plus interest and revaluation — average **~€13,000 per truck**. Passing-on and tax-benefit defences both rejected. | Italy and the italy-private-fleet-outreach-cc skill's peer-proof hook — see there for the corrected figure; the municipal skill's own targets are unaffected. |
| **CJEU on limitation** | Limitation runs from 2017 (publication of the decision), not 2016. | Anywhere limitation is raised. |

### The wider BGH "LKW-Kartell" series — cite by number, not just the Az.
KZR 98/20 above is one entry in a numbered German procedural series that keeps extending what a claimant needs to prove. Worth knowing the shape of it even where the municipal pitch doesn't need to cite each one directly, because a well-briefed Kommunalreferat may raise it:

| # | Date | Az. | Establishes |
|---|---|---|---|
| I | 23.09.2020 | KZR 35/19 | Foundational infringement/causation doctrine |
| II | 13.04.2021 | KZR 19/20 | Extends the damage presumption |
| III | 05.12.2023 | KZR 46/21 | **Leasing and hire-purchase claimants have standing**, not just direct buyers |
| IV | 09.07.2024 | KZR 98/20 | No comparative-market analysis required (table above) |
| V | 01.10.2024 | KZR 60/23 | A truck bought then re-financed via leasing/hire-purchase is **one claim (one Streitgegenstand)**, not several; clarifies §33g GWB disclosure claims |
| VI | 08.04.2025 | KZR 71/23 | Continues the damage presumption for leasing with mileage billing; where claimant can't show the leasing company's internal pricing and both are in the same corporate group, **the defendant can carry a secondary burden of proof** |

**Why this matters here:** the Lion Claim commercial model section below already asserts "leasing and hire-purchase qualify" and "sold or scrapped vehicles still qualify" — III and V are the actual authority for that, not previously cited. Use III/V/VI where a target's fleet was leased or hire-purchased rather than bought outright; VI in particular is useful if a leasing company and manufacturer turn out to be in the same group and refuse to disclose pricing.

**Case law refreshed 15.09.2026, confidence 85%.** Checked BGH press releases and three independent German legal-press summaries (LTO, beck-aktuell, betriebs-berater) plus the BGH's own termination notice for KZR 6/24. The numbered series (I–VI) is well corroborated across sources; KZR 6/24's relationship to that series (it is not itself numbered "LKW-Kartell VII" in any source found) is the one soft point — treat it as a related but procedurally distinct strand (collections-licensing, not substantive damages) until confirmed with MMG. Re-run this search before any batch — this case law moved twice in the last 12 months and will move again.

### The 15% clause — a qualification question nobody asks
Many German municipalities use Vergabehandbuch des Bundes standard wording containing a **liquidated damages clause of 15% of order volume** in the event of cartel collusion. The Göttingen court held such a clause valid. **Where it is present, the damage does not need proving and the figure is 15%, not 5%.** Always ask whether the purchase contracts contain it.

### The separate German fire appliance cartel
Distinct from the truck cartel — different regulator, different defendants, different vehicles (the **body**, not the chassis).

- Bundeskartellamt uncovered two cartels in 2011: **Löschfahrzeuge** (Iveco Magirus, Schlingmann, Rosenbauer, Ziegler — c.90% market share, meeting at Zurich airport 2001–2009) and **Hubrettungsfahrzeuge** (Metz Aerials + Iveco Magirus, from at least 1998). Fines €68m total.
- **May 2013**: Deutscher Städtetag, Deutscher Landkreistag and DStGB settled out of court — €6.74m fund, **€1,600–2,200 per vehicle** for purchases 2000 to mid-2004.
- **September 2013**: aerial ladders, €6.41m, **€10,500–16,000 per vehicle** for 2000–2007 purchases, 391 vehicles compensated.

**How to use it:** a German municipality will say "we settled the fire engine cartel in 2013." Answer: that was the **body**. The **chassis** underneath — MAN, Mercedes, Iveco, Scania — is a different cartel, a different decision, different defendants, and nobody has claimed it. Also useful anchoring: municipalities have already accepted five-figure per-vehicle compensation in this exact context.

### The German associations have organised this twice
The Kommunale Spitzenverbände negotiated the 2013 fire cartel settlement, and in 2017 jointly commissioned an expert opinion with **VKU** on truck-cartel overcharges plus limitation-suspending measures. The assessor on the related work was **Lademann & Associates** — the same firm the Berlin court relied on. **Ask DStGB and VKU whether that Gutachten can be shared or built on.** If it exists and is available it removes the largest cost and delay in every German municipal claim.

### Reference clients and public claimants
| Body | Detail | Status |
|---|---|---|
| **City of Zurich** | 194 affected vehicles across seven departments (waste, fire and rescue, police, civil engineering, water, electricity utility, transit). 79 with original purchase documents; a further 91 had only operating-software printouts. CHF 4.2m claimed; city expects ~CHF 2m net. First verdicts expected 2026/27. | Press attributes funding to **Park Truck Holdings LLC**, coordination to **IGV mbH**. **Confirm Lion Claim's actual relationship before naming Zurich as a client.** |
| **Stadt Winterthur** | At least 83 vehicles, 41 more under investigation. Engaged **IGVR**. Window used: **1998–2016** — materially wider than the standard 2012 cut-off. | Already claiming, with a competitor. |
| **Canton St. Gallen** | Up to 78 vehicles. | Claiming. |
| **St. Gallen municipalities** | ~100 vehicles in the canton, each worth **CHF 350,000–1,000,000**. | Claiming. |
| **Stadt Göttingen, Landkreis Northeim, Berliner Stadtreinigung** | Litigated and won. | References and intelligence sources rather than prospects — but worth a call. |

### Competitive landscape
**IGVR / IGV mbH** and **Park Truck Holdings LLC** (Switzerland — Zurich, Winterthur; IGVR states it represents over a thousand claimants). **Truck-Cartel Compensation, Werner Rofner, Grünwald** (Swiss municipalities, introduced by the St. Gallen mayors' association). **Omni Bridgeway** (Netherlands; ran the Austrian municipal campaign 2020). **Financialright / myRight** (the KZR 6/24 case). Also Hausfeld, CDC, TruckRefunds/TruckLex, Edwin Coe.

**Treat Switzerland as contested.** Ask every Swiss target directly and early whether they are already in a process — a duplicate mandate is a serious problem.

### The Austrian 2020 campaign
Gemeindebund, Städtebund and VÖWG jointly recommended participation in a collective action via **Omni Bridgeway**, advised by Vienna firm **bkp**, with a stated deadline of **31.12.2020**. They led on **Tanklöschfahrzeuge** — fire tank trucks, not refuse trucks. Every Austrian target will raise this. Put the answer in the first paragraph.

### The Lion Claim commercial model
- Direct representation: signed litigation funding agreement + **original** power of attorney by post to the law firm (Munich).
- Forum: Munich. Cartel was coordinated from 2004 through the manufacturers' German subsidiaries; Munich is both crime scene and venue.
- Eligibility: **new** vehicles only, client must be **first registered owner**; ordered, purchased or leased **01.01.1998 – 31.03.2012**; over 6 tonnes.
- Leasing and hire-purchase qualify. Sold or scrapped vehicles still qualify.
- Costs: funder bears court fees, legal fees, expert fees, adverse costs. Litigation cost contribution of 5% of recovery plus VAT, or minimum €200 per truck, whichever is higher. Then **65% client / 35% funder**.
- Documents needed: funding agreement, original PoA, commercial register extract, ID of signatory, Excel of company and vehicle data (manufacturer, model, VIN, date, price, acquisition method, condition, seller), plus purchase invoices / lease agreements / hire-purchase agreements. Alternatives accepted: registration certificates, order confirmations, fixed asset registers, bank statements.

---

## MANDATORY honesty rules

Public bodies are a less forgiving audience than hauliers. One that feels oversold will say so in writing, to its association, in a market where everybody talks. These are not stylistic preferences.

1. **Limitation is a legal position, never a promise.** The 31.12.2029 date in the sales FAQ is contested. Swiss reporting in January 2026 stated claims on 1998–2001 purchases became time-barred on 01.01.2026, implying a **rolling annual cohort expiry**. Austria's own associations treated 31.12.2020 as the deadline. Always write "this is our law firm's legal position" and offer to substantiate it. Never write that a claim is definitely alive.
2. **Never overstate a reference.** Only name a client with documented consent — the client FAQ states client names are not disclosed without explicit consent, so naming without permission contradicts a published policy. If the relationship is indirect, say precisely that.
3. **Never state an unverified figure as fact.** Cite fleet numbers with their date and source. Mark estimates as estimates.
4. **Never show the value model to a target.** It is an internal prioritisation tool.
5. **"No cost, no risk" is true under the funding agreement — it is not a guaranteed outcome.** Do not let it drift.
6. **Raise the weakness in your own case before they do.** Where national limitation is tight, say so and explain the German forum. This is what gets you taken seriously by an administration that has been approached before.
7. **Flag procurement law.** A municipality engaging a law firm and funder may be procuring legal services; above threshold that can require a tender, and a 35% share of a public body's recovery may count as consideration. Raise it before the first target says yes.
8. **Flag grant clawback** where vehicles were EU or nationally co-financed — common in Poland, Czechia, Portugal, and for fire appliances almost everywhere.
9. **Anticipate the passing-on defence.** In Göttingen the court left MAN room to argue the city had passed the overcharge to fee-payers through waste and cleansing charges. This bites municipalities harder than hauliers because those services are financed by cost-covering charges. **Fire services are the answer** — fire protection is generally tax-financed, so there is no fee-payer. Another reason to lead with appliances.
10. **Use published institutional contact channels.** Do not scrape or guess personal addresses. Record the source of every contact detail.

---

## Qualification screen

Run before any tailored outreach, and re-run whenever new ownership information surfaces — an entity that cleared this screen in Phase 1 is not permanently cleared if a later fact changes the picture. A "No" at a KILL question ends it; a "No" at a FLAG question is a handling note.

**KILL**
1. Did the body (or a company it wholly/majority owns) **buy** the vehicles, or does a concessionaire own them? If collection is outsourced, the trucks and the claim belong to the contractor. This alone removes most Spanish and much Nordic city administration. **Get and record an actual ownership percentage, not a public/private label.** "Publicly owned" is not itself an answer — a body 45% owned by a municipality and 55% by a private group is majority-private and fails this question, even though press coverage or an older note may still describe it loosely as a "public operator." Whenever an entity's ownership is anything other than 100% or a clearly stated clean majority, verify the exact split from a named source (company registry, shareholder-agreement press coverage, the operator's own investor/governance page) before it clears this question — do not accept "minority private shareholder" as a settled framing without the number behind it, since that exact framing has previously flipped once a real percentage was found.
2. Bought **new**, with the body as **first registered owner**? Used purchases do not qualify.
3. Acquired, leased or hire-purchased between **01.01.1998 and 31.03.2012**?
4. Over **6 tonnes**, on a DAF, Daimler/Mercedes, Iveco, MAN, Renault, Scania or Volvo chassis? Buses and coaches are out.

**UNLOCK** — these find the hidden volume
5. Does the fleet include **special-purpose vehicles** — refuse collection, sweepers, gritters, jetting/vacuum units, tippers, crane trucks, fire appliances? CJEU C-588/20 covers them. Biggest single source of missed volume.
6. Do the **fire service** vehicles sit on the books? Highest per-unit value anywhere in this case.
7. Are there **other arms with heavy fleets** — water, sewerage, roads, parks, ports, energy utility, transit engineering? Zurich's 194 came from seven separate departments. A body that says "we only have refuse trucks" has not looked.
8. Do the purchase contracts contain a **liquidated damages clause** (15% or similar) for cartel collusion?

**FLAG**
9. Do original invoices, lease contracts or hire-purchase agreements still exist? **This is the binding constraint** — Zurich converted 194 affected vehicles into only 79 litigable ones, 41%.
10. Is a **retention or disposal schedule** about to destroy those records? Typically 10–15 years after asset disposal. For 1998–2012 vehicles that clock is expiring now, and every electrification programme accelerates it.
11. Already in an earlier action (Omni Bridgeway, a Dutch stichting, IGVR, an association scheme)? Ask directly — never guess.
12. Any EU or national grant co-financing?
13. **Who can sign** a funding agreement and PoA? Department head, managing director, finance director, or full council resolution? This is the difference between a six-week and a nine-month close.
14. **Is the target itself the vehicle owner, or a regulator/planning body one step removed from the operator that actually buys and holds the fleet?** A body that sets tariffs, approves plans, or coordinates operators (an ATO-style water authority, a regional planning consortium) is not a claimant even where it is clearly public — it should be represented by the operator underneath it, not carried as a separate target. Confirm which specific entity in a regulator/operator pair actually procures vehicles before adding both, and if only the regulator is on the list, replace it with the operator rather than running both as if they were independent leads.

### Where the hidden volume sits
Ordered by value:

- **Fire and rescue** — tank appliances, ladder platforms, rescue tenders, hazmat units. MAN, Mercedes, Iveco Magirus, Scania chassis. 20–30 year service lives so cartel-era units are often still on the register. Grant-funded, therefore unusually well documented. St. Gallen puts the range at CHF 350,000–1,000,000 per vehicle.
- **Works yards and roads** — gritters, ploughs, tippers, sweepers. Where small municipalities keep their only heavy vehicles.
- **Water and sewerage** — jetting units, vacuum tankers, combination units. Often a separate legal entity, therefore a second claim.
- **Municipal energy and lighting** — crane trucks, cable drum carriers, pole-setting vehicles. Zurich's claim includes its electricity utility. Overlooked almost everywhere.
- **Inter-municipal associations** — Zweckverbände, intercommunales, syndicats. Best value per contact in the whole case.
- **Ports, airports, markets, abattoirs** — municipally owned companies with their own balance sheets.
- **Public transport engineering** — workshop, recovery, overhead line trucks. The buses are out of scope; the fleet behind them is not.

---

## Contact doctrine

**The commonest failure is writing to the mayor.** A mayor's office forwards commercial approaches to procurement, where they die. The second commonest is writing to the fleet manager, who understands the vehicles perfectly and has no authority over litigation.

**The rule: write to whoever owns the balance sheet of the operating entity, and copy nobody.**

| Role | When | Why |
|---|---|---|
| Commercial / finance director of the municipal operator | Corporatised operators (AöR, GmbH, NV, a.s., S.p.A.) | Recovering money is their job description; they can convene legal and fleet themselves |
| Works management of a municipal enterprise | Eigenbetrieb | Delegated commercial authority — **can commission a review without a council resolution.** Fastest route in the German-speaking countries |
| Head of the department that owns the fleet | Magistratsabteilung, city directorate | The decision-maker, and the records sit under them |
| Elected member holding the portfolio | Southern European councils | The administration will not move without the vereador or assessore |
| Coordinating official at the tier above | Where vehicles sit with many small bodies | The person who convenes them is worth more than any one of them |

**Practical rules:**
1. Never send to a generic info@ address. Use the published functional mailbox and put the role holder's name in the salutation.
2. **Verify the name the morning you send.** Municipal leadership churns constantly — this applies even to a name confirmed in Phase 2; a decree, appointment or election between enrichment and sending can supersede it.
3. **Do not copy legal on the first email.** Legal's first instinct is to see a risk to manage. Let the commercial owner bring them in, so it arrives as their initiative.

---

## Email doctrine

### Anatomy
1. **Open on a fact true only of them.** Not the cartel — them. Their fleet number, their council paper, their new managing director, their electrification programme, their court's recent ruling.
2. **The peer proof.** A public body that has already done this. Match to market.
3. **The legal unlock.** CJEU C-588/20 in one sentence.
4. **Optional duty frame.** Budgetary law obliges an authority to collect claims it is entitled to; company law obliges a board to exercise the care of a prudent manager over recoverable assets. Softens the decision — examining is compliance, declining is what needs justifying.
5. **No cost, no risk** — one sentence, no adjectives.
6. **Who does the work.** For mid-size and smaller targets say explicitly that you handle the data collection and document reconstruction. "My team has no capacity" is the real objection at that scale.
7. **Ask for twenty minutes, not a signature.** A public official can grant twenty minutes without justifying it to anyone. That is the entire design.

### Rules
- **Write in the recipient's language**, natively. Not translated-sounding.
- **180–220 words.** Public officials do not read long emails.
- **No exclamation marks, no marketing register, no "risk-free!"** That reads as spam to an administrator.
- **No bullet lists of benefits.** Prose.
- Give them a way to say no that still counts as a result: "if not, you have a documented answer for your files."
- Placeholders in square brackets where a name could not be verified — and mark it for checking.

### Hook sources, in order of strength
1. **Their own published document** — a council paper recording old vehicles is unarguable and proves the approach is researched, not mass-mailed.
2. **A public statement by the recipient** — an official who has already said the issue is worth looking at is not a prospect to persuade.
3. **A named peer who acted** — especially the same legal form or the neighbouring city.
4. **A court in their own jurisdiction ruling on this** while they are not at the table.
5. **A structural change at their end** — new director, governance reset, fleet replacement programme, consolidation.
6. **A closing window they can see inside their own filing system** — retention schedules, scrappage.

### Worked example — structure to imitate

> **Subject:** Berliner Stadtreinigung hat geklagt und gewonnen – gilt das auch für die SRH?
>
> Sehr geehrter Herr [Name],
>
> zunächst: alles Gute zum Start als kaufmännischer Geschäftsführer der SRH.
>
> Ein Punkt, der erfahrungsgemäß in den ersten Wochen selten auf dem Tisch liegt, bilanziell aber relevant sein kann. Die Berliner Stadtreinigung – wie die SRH eine kommunale Anstalt öffentlichen Rechts – hat vor dem Landgericht Berlin geklagt und gewonnen. Urteil vom 15.06.2023 (Az. 16a O 1/20 Kart): rund 200 Fahrzeuge von MAN und Iveco, 5 % des Nettokaufpreises, etwa 5.000 Euro je Fahrzeug.
>
> Die SRH betreibt heute rund 1.016 Fahrzeuge, darunter etwa 200 Müllfahrzeuge. Der Bestand, der zwischen 1998 und 2012 beschafft wurde, dürfte den Berliner Fuhrpark, über den entschieden wurde, deutlich übersteigen.
>
> Kosten und Prozessrisiko trägt vollständig unser Prozesskostenfinanzierer.
>
> Hätten Sie 20 Minuten? Ich bringe die Berliner Entscheidung mit und eine kurze Einschätzung, was sie für einen Fuhrpark Ihrer Größenordnung bedeuten könnte.

Note what it does: opens on a peer of the **same legal form**, uses a fact about the recipient's own first weeks in post, gives a case number, compares fleet sizes, one risk sentence, asks for twenty minutes and offers to bring something.

---

## Market ranking

Decision speed follows **legal form, not population**. Where the fleet sits in a separately incorporated entity, a managing director has delegated authority. Where it sits in the general administration, you need a council.

| Rank | Market | Verdict |
|---|---|---|
| 1 | **Germany** | Best by a distance. Dense Eigenbetrieb / AöR / kommunale GmbH structure. Two municipal precedents (Göttingen, Berliner Stadtreinigung). Home limitation regime — no cross-border argument needed. Associations have organised collective municipal claims twice. Make this the primary market. |
| 2 | **Belgium** | Structurally superb and apparently untouched. 34 hulpverleningszones; waste in intercommunales. |
| 3 | **Netherlands** | 25 veiligheidsregio's, strong records culture. Existing Dutch collective actions are haulier-focused. |
| 4 | **Austria** | Good structure, excellent fire channel — but limitation poisons every opening. Only enter with a written limitation note in hand. |
| 5 | **Switzerland** | Excellent structure, commercially contested (IGVR, Rofner). Go via the cantonal building insurers or stay out. |
| 6 | **Czechia / Slovakia** | Municipally-owned a.s. everywhere, total whitespace, tight limitation. Cheap to test off a German success. |
| 7 | **Poland** | Accession-funded procurement documented to audit standard. Resolve grant clawback first. |
| 8 | **Italy** | Standalone city companies are excellent; the big multi-utility groups are slow. |
| 9 | **France** | Waste is complicated by the régie/prestataire split. The SDIS are the real opportunity. |
| 10 | **Portugal** | In-house operation is normal; small market, tight limitation. |
| 11 | **Nordics** | Collection contracted out — skip waste entirely. Only fire is worth a look. |
| 12 | **Spain** | Concessionaire model. Do not work Spanish municipalities; consider the concessionaires as corporate targets instead. |

---

## Channel classes — worth 10 to 100 municipalities per contact

Prefer these over individual city names once the first references are signed.

- **Belgian hulpverleningszones — 34.** Created 01.01.2015 as public bodies with their own legal personality, taking over previously **municipal** fire services. Channel: Netwerk Brandweer within VVSG.
- **Dutch veiligheidsregio's — 25.** Last municipal brigades dissolved 2014 under the Wet veiligheidsregio's. Channel: Brandweer Nederland.
- **French SDIS — ~101.** Municipal fire services departementalised 1996–2001, right at the start of the cartel window. Verify transfer mechanics before investing; if it holds, the largest untouched pool in Europe.
- **VKG, Switzerland — 1 umbrella, 18 cantonal building insurers.** Fund fire services ~**CHF 260m a year** including vehicles, so they hold or can reach the procurement records for essentially every Swiss appliance. Gebäudeversicherung St. Gallen already used this position to coordinate claims.
- **German Kommunale Spitzenverbände + VKU.** Städtetag, Landkreistag, DStGB, plus VKU's ~1,500 members. Highest-value single conversation in Europe.
- **Austrian Landesfeuerwehrverbände — 9.** Appliance funding is conditional on compliance with their guidelines, so they hold a funding file for every co-financed vehicle. Lower Austria even regulates appliance numbers per municipality by ordinance.
- **Zweckverbände and waste intercommunales.** Harvest from VKU membership lists and TED rather than enumerating by hand.

### The consolidation insight
The 2014/2015 fire service consolidations in the Netherlands and Belgium, and the French departementalisation, each required a receiving body to **take legal title** to municipal fleets — which means somebody compiled a dated asset schedule listing every appliance with its acquisition details.

**This solves the documentation problem in reverse.** Zurich could only litigate 79 of 194 vehicles because the paperwork was gone. Ask these bodies for the **transfer schedule**, not the original invoices.

### TED as a target list
Tenders Electronic Daily is the EU's official procurement journal; above-threshold award notices since the 1990s name the contracting authority, supplier, value and often quantity. Every above-threshold municipal purchase of trucks, refuse vehicles, sweepers and fire appliances between 1998 and 2012 is therefore in a machine-readable public database with the buyer named against it. It is not a prospect list — it is a list of qualified claimants with documentary evidence of the qualifying transaction. It also works in reverse: where a body has lost its file, the TED notice is contemporaneous third-party evidence the purchase happened.

### The real product
Documentation, not eligibility, is the binding constraint. Zurich's conversion was 41%. So what municipalities actually want is **archive work**, not litigation funding. Nobody wants to reconstruct twenty-year-old procurement files, and that reluctance is the commonest reason these conversations stall after a good first meeting. An offer built on "we do the documentation recovery" — using TED notices, fixed asset registers, vehicle registration authorities, manufacturer dealer records, grant files, insurance records and consolidation transfer schedules — converts better than one built on funding terms, and is harder to copy.

---

## Postal address sourcing (Phase 2)

Needed for mail-merge and for the deliverable's Notes column. Two methods, in order of use:

1. **A national public-body/entity registry, if the client can supply or you can source one** (e.g. Italy's IPA "Enti" registry). These typically carry `Indirizzo`/address and `CAP`/postal-code fields per entity, usually intended for a different purpose (contact lookups) but reusable directly for postal address. Fuzzy-match target entity names against the registry: normalise both sides (lowercase, strip punctuation), remove legal-form stopwords (spa/srl/comune/consorzio/scarl/etc. — localise the stopword list per country), then score candidates with a token-overlap or string-similarity (e.g. `difflib.SequenceMatcher`) method. For anything beyond a few hundred targets against a large registry, pre-filter with an inverted token index before running string-similarity — a naive full cross product will time out.
2. **A national business/company registry lookup site** (e.g. Italy's ufficiocamerale.it) for corporatised entities (S.p.A./S.r.l.) not covered by the public-body registry — these reliably return the "sede legale" / registered-office address.

**Naming-collision risk applies to address matching just as much as to target sourcing** — see the naming-collision discipline below. Never accept an automated fuzzy match for an address without a manual sanity check against the target's known city/region; a plausible-looking match for the right entity name can still resolve to a same-named but unrelated company in a different city. When a match looks geographically wrong for what the target is known to be, do not write it in — flag it for a second, more targeted search instead.

---

## Deliverables

Default package. Read the `docx` and `xlsx` skills for mechanics before building.

### Word strategy brief
Cover page with a **"Read this first"** box naming every open decision the user must make before sending — and only that. **Keep this box to genuinely still-open items.** As items get resolved across batches, remove them from the box rather than leaving a growing narrative of resolved history on page one — a client who is told the brief is a "clean finish" while page one still lists things that were actually researchable will (correctly) push back. Move the full batch-by-batch changelog to an appendix at the back of the same document instead of the cover; leave a one-line pointer from the trimmed box to the appendix for anyone who wants the full trail. Then: executive summary, target table, contact doctrine, the emails (each in a bordered block with a "Why this opening" note explaining the personalisation choice), European scaling plan, hidden-volume section, risk register, verification log, and the appendix.

Use Calibri, navy `1F3864` headings, accent `C00000`, table shading `ShadingType.CLEAR`. Set `features: { updateFields: true }` for the TOC. Render to PDF and read the pages before delivering — pay particular attention to any table whose column count you changed (see the column-width gotcha below).

### Excel target list
Tabs:
1. **Target List** — number, city, country, legal entity name, entity type, fleet evidence, figure date, primary contact role, named individual, contact channel, secondary contact, email language, personalisation hook, priority 1–3, key risk, **postal address**, and a **Notes** column. The Notes column carries the one-line status that used to only live in prose changelogs — e.g. "contact confirmed Aug 2026 via decree," "DO NOT DRAFT — see Open Decisions (majority-private ownership)," "hook is an OPERATIONAL-SCALE PROXY, not confirmed," "ready to send" — so the spreadsheet is usable on its own without cross-referencing the brief's narrative. Group by wave with banner rows.
2. **Value Model** — yellow lever cells, blue hardcoded inputs, black formulas. Defaults: documentation survival **41%** (Zurich benchmark), average net price **€180,000** (blended, user-adjustable), overcharge **5%** (LG Berlin floor; substitute a better local anchor if a national judgment quantifies one, e.g. an Italian court's own overcharge percentage), interest multiplier **2.0x** (planning placeholder — flag as not a legal entitlement), litigation contribution 5%, split 65/35. Carry a visible warning that it is internal only.
3. **Qualification** — the screen, colour-coded KILL / UNLOCK / FLAG.
4. **Sources** — every factual claim with outlet and URL.

**If you insert rows into a sheet with formulas, openpyxl does not update the references — rewrite every formula afterwards and re-run `recalc.py`.** Verify computed values by reading them back, not just by a clean recalc.

### Verification log
Always. Three categories: verified with source, verified as reported (single source or press summary), and **NOT verified** with what to do about it. Name every estimate as an estimate.

---

## Running a large multi-session target programme (learned on the Italy run, batches 1–20)

When a single market is pushed well past the first wave of targets (Italy went from a handful of names to 105 targets and 89 drafted emails across 20 sessions), treat it as a standing programme with its own file architecture and batch discipline, not a one-off research task.

### File architecture
- Keep two Python source-of-truth files, not raw JSON or a spreadsheet as the master: `targets.py` (a `TARGETS` list of dicts — one per lead, with at minimum `n`, `wave`, `priority`, `city`, `entity`, `entity_type`, `segment`, `fleet_evidence`, `fleet_source`, `fleet_status`, `contact_role`, `contact_name`, `contact_note`, `hook`, `risk`, `address`, `note`) and `emails.py` (an `EMAILS` list of dicts, each linked to a target by `n`). Python source is easy to `git`-diff, easy to append to consistently, and easy to regenerate JSON/Excel/Word from — a spreadsheet edited by hand drifts.
- Regenerate `targets_data.json` / `emails_data.json` from the Python source every batch via a one-line `json.dump`, and build the Word/Excel deliverables from those, not by hand-editing the deliverables.
- If a build script needs scratch CSVs derived from large source registries (a national IPA entity registry, population data, etc.), do not keep them checked in — regenerate them from the original source file at the start of every batch and delete them at the end. Keeping the *regeneration script* (not the derived CSV) in the standard batch checklist below avoids both drift and repo bloat. If the build scripts expect scratch inputs under a fixed working path (a hardcoded `/tmp/...` directory, for instance), create that path and copy the needed inputs into it as the very first step of every rebuild — this is easy to forget after a session break and produces a confusing "file not found" rather than an obviously-missing-input error.
- **When adding a column to any generated table (Excel sheet or a docx table), the column-width/positioning array is coupled to the exact column count and must be updated in the same edit, not after.** A hardcoded width array (e.g. `TARGET_COL_WIDTHS`) that isn't resized when a column is added will silently misalign or clip content — always visually verify the rebuilt table (PDF + `pdftoppm` + Read, or reading the xlsx back) after any column-count change, not just a clean build.
- If an entry number is ever retired (found to be a duplicate, disqualified, or miscounted), do not renumber everything else — leave the gap and note it permanently in the `assert len(TARGETS) == N` comment (e.g. "entry numbers run to N+2, but #61 and #65 were removed"). Renumbering breaks every reference to that entry in prior deliverables, Sources tabs and correspondence.

### Discovery methods, ranked by efficiency (most efficient first)
1. **Official regional/national operator directory.** A single government or industry-network page that lists every water, waste, or transport operator in a region or network at once — e.g. a regional environment ministry's "gestori del servizio idrico" page, or an official multi-utility network's own membership page. One page can surface 5–15 usable candidates at once, and membership/listing on an official directory is itself adequate evidence of public ownership — you do not need a deep ownership dive per entity when the parent directory already establishes it, though you should still confirm the exact ownership percentage before an entity clears the KILL screen (see the qualification screen's note on this). Actively look for one of these before falling back to method 2. Once a region's directory has been used, note it as exhausted so future sessions don't re-search it.
2. **Direct search for the named public-capital multi-comune consortium pattern.** Searching for "[region] consorzio pubblico [servizio]"-style named entities outperforms population-band sampling of individual municipalities, because a single consortium often represents dozens of member comuni in one contact.
3. **Population-band sampling of individual municipalities** — the least efficient method; use only once the directory and consortium-pattern methods are exhausted for a market.

### Naming-collision discipline
Public-sector entity names collide across Italy far more than you'd expect (e.g. two unrelated organisations both abbreviated AMIU, two unrelated organisations both called ASIA, two unrelated organisations both called GAIA). Whenever a new candidate's name resembles an existing target's name, flag the collision explicitly in the new entry's own fields (not just a mental note) and cross-reference the entry number of the lookalike, so nobody merges or confuses them in a future session or in outreach. This applies equally to address sourcing (see above) — a collision that was correctly resolved for contact purposes can still resolve wrong when fuzzy-matched against an address registry, so re-check every flagged collision pair specifically at the address step too, not just once at sourcing time.

### Standard batch checklist
Run the right checklist for the phase you're actually in — don't let a sourcing batch quietly drift into drafting, or an enrichment batch into re-sourcing.

**Phase 1 batches (sourcing):**
1. Research and append new entries to `targets.py`, following the existing dict schema and wording conventions exactly, including an explicit ownership percentage where relevant.
2. Regenerate `targets_data.json`.
3. Regenerate any scratch CSVs the build scripts need, from source.
4. Append a new dated "Sources" block to the workbook build script documenting each new claim.
5. Rebuild both deliverables, re-run the xlsx formula-recalculation check (zero errors), convert the docx to PDF and visually spot-check for layout breakage.
6. Clean up scratch files, deliver both master documents, log the batch.

**Phase 2 batches (enrichment — the fill-in phase):**
Track three gaps per target: a **real named contact** (not a placeholder), a **real fleet-specific hook** (not a placeholder), and a **postal address**. Prioritise in this order: (1) targets with a hook but no contact — find the contact; (2) targets with a contact but no hook — dig for a fleet-specific fact (published fleet inventory, tender/gara documents, local news on vehicle procurement, sustainability/fleet-renewal reports); (3) targets missing more than one of the three. **Do not draft an email in the same pass, even when both contact and hook land together** — mark the entry "ready for Phase 3" and let the drafting pass pick it up deliberately, so there's a checkpoint between "the facts exist" and "the facts are trusted enough to send." Be honest in the file when a "hook" is really a governance/investment-cycle/operational-scale proxy rather than a confirmed vehicle fact — label it as such so a later session doesn't mistake it for verified fleet evidence. Re-run the KILL screen's ownership question on any entity where a hook or contact search surfaces new ownership information — this is where a previously-flagged "minority private shareholder" framing can flip to an actual majority-private KILL, as it did once on this project.

**Phase 3 batches (drafting):**
Draft only entries explicitly marked "ready for Phase 3." Draft in the recipient's language per the email doctrine. Update the Notes column and Open Decisions box for anything the drafting pass itself surfaces as newly risky.

### Handing off a long-running session
A programme like this can run a conversation long enough that starting a fresh session becomes worth the reset. Because the working files live in a session-scoped workspace, a fresh session needs the actual project files, not just a summary of them:
- Package the whole working folder (`targets.py`, `emails.py`, the two build scripts, the current deliverables, and any derived reference data the build scripts depend on) into a zip and deliver it.
- Write a companion Markdown briefing covering: current counts, the standing rules above (knockout rule, contact/email doctrine, naming-collision list, table-width/formatting fixes that must not regress), the exact regeneration commands for any scratch files, a short batch-history summary, and — most usefully — the **exact list of entry numbers still missing a contact, a hook, and/or an address, plus which phase each is currently in**, so the next session can start exactly where the last one left off without re-deriving the backlog from scratch or accidentally skipping a phase.

---

## Failure modes to avoid

- Writing to the mayor.
- Padding a target list with bodies that do not own their vehicles. Say plainly why a market is excluded instead.
- Stating limitation as fact.
- Naming a reference client without documented consent.
- Producing fleet figures without a date and source.
- Letting a paywalled article's search summary become an asserted fact — say when you could not read the primary source.
- Long emails.
- Forgetting that the person who agrees with you may not be the person who can sign.
- **Drafting an email before an entity's ownership, contact and hook are all independently settled.** This is what let a majority-private entity sit in the pipeline for three batches under a "minority shareholder" framing that was never actually checked against a real percentage.
- **Calling a batch a "clean finish" while the brief's own open-items section still lists things that further research could have resolved.** Only call something closed once it's actually been pushed as far as research can take it — a client who checks will notice the gap.
- **Carrying a regulator and its underlying operator as two separate targets** without confirming which one actually buys vehicles — this produces a redundant, weaker contact alongside the real claimant instead of one clean lead.
