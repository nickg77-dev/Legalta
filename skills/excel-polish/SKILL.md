---
name: excel-polish
description: Nick's ultra-professional Excel polish standard. ALWAYS apply this skill in addition to the xlsx skill whenever creating or editing ANY spreadsheet (.xlsx, .csv exported to xlsx, financial model, tracker, budget, capacity plan, expense file, pipeline sheet, dashboard) - even if Nick does not mention polish, design, or formatting. Also triggers on "polish this spreadsheet", "make this look professional", "format this workbook", or when reviewing a spreadsheet Nick received from someone else. The xlsx skill governs mechanics (openpyxl, recalc, formulas); this skill governs layout, naming, formatting, and the strategic insight layer. If the two conflict, this skill wins for anything visual or structural.
---

# Excel Polish - Nick's Professional Standard

Purpose: every workbook leaving this environment should look like it was built by a senior operations consultant, read naturally as human work, and deliver strategic insight, not just data.

Read /mnt/skills/public/xlsx/SKILL.md first for mechanics (recalc.py is still mandatory). Then apply everything below.

## 1. Non-negotiables (NEVER do these)

- NEVER merge cells. Use "Center Across Selection" or left-aligned headers with overflow instead.
- NEVER use fonts smaller than 10pt anywhere, including chart labels and footnotes.
- NEVER use underscores in file names, tab names, chart titles, or named ranges. Use spaces in files and tabs ("Cash Flow 2026.xlsx", tab "Q3 Summary"). Named ranges cannot contain spaces, so use CamelCase there (TotalFee, not total_fee).
- NEVER use low-contrast combinations: no white or pale text on light fills, no dark text on dark fills. Minimum standard: if you squint and cannot read it, rebuild it. When in doubt use dark grey text (RGB 51,51,51) on white or very light fill.
- NEVER leave decimals on currency or whole numbers unless Nick asks (0 decimals default; percentages 1 decimal).
- NEVER wrap text in instruction cells that span visually across a row (ex-merged-cell style). Leave cells to the right empty and let the text overflow.
- NEVER use 3D charts, pie charts with more than 5 slices, default Excel blue-orange palettes, or chart junk (heavy gridlines, borders, shadows, legends when direct labels work).
- NEVER add page headers. Footers are permitted only under section 8 conditions.
- NEVER ship VBA macros unless Nick explicitly requests them and accepts they are untested here. List macro candidates in the Automations tab instead.
- NEVER ship robotic text. Headers and labels read like a colleague wrote them: "Days remaining", not "days_remaining" or "DaysRemaining". No "Utilize", "Leverage" as a verb, or filler like "Comprehensive Overview".
- NEVER hardcode a value where a formula belongs (xlsx skill rule; repeated because polish is worthless on a broken model).

## 2. Layout architecture

**Totals placement (Nick's convention, deliberately unconventional):**
- Total COLUMNS sit at the LEFT of the table, immediately after row labels. Example: | Consultant | Total Days | Total Fee | Jan | Feb | Mar |
- Total ROWS sit at the TOP of the table, immediately under the header row, bold. Example: header row 4, "Total" row 5, detail from row 6.
- Rationale: totals are the headline; nobody should scroll to find them.
- Override: if the file will be shared with an external finance audience expecting bottom-right totals, or Nick is editing someone else's file, follow the existing convention and tell Nick you did so.

**Multiple tables on one sheet:**
- Stack vertically with 2 blank rows between tables.
- Align columns: shared concepts occupy the same columns in both tables (dates under dates, money under money).
- If alignment is impossible, at minimum place long text-heavy columns in the same columns across tables so one column width serves both.
- Each table gets its own bold title in the cell above its header row.

**Sheet furniture:**
- Freeze the header row and label column(s) on every data sheet.
- Add filters when a table exceeds 30 rows and filtering would genuinely help.
- Park the cursor at A1 on every sheet before saving; set zoom to 100%; hide gridlines on summary, chart, and dashboard sheets, keep them on data sheets.
- Colour code tab strips sparingly: one colour for inputs, one for outputs, grey for reference. Three colours maximum per workbook.
- Workbooks with 3+ tabs get a "Read Me" first tab: purpose (one sentence), owner, date, tab guide, key assumptions, and which cells are editable.

## 3. Typography, alignment, formatting

- Font: Arial 10 or 11 throughout (per xlsx skill). Headers bold, same font, max 1-2pt larger.
- Text and headers: left aligned. Numbers: right aligned. Everything: vertically centred.
- Total columns and total rows: bold.
- Currency: symbol always shown, 0 decimals ("£#,##0" or "$#,##0"). Match the currency of the underlying data; default GBP for Nick's own finances. If mixed currencies, name the currency in the header ("Fee (EUR)") and never sum across currencies without a stated FX rate in a labelled cell.
- Negatives in parentheses, zeros as "-" for financial sheets (xlsx skill convention).
- Dates: "d mmm yyyy" (5 Mar 2026) unless the file already uses another format.
- Slash-separated terms get spaces: "Yes / No", "Draft / Final" (wrap text breaks cleanly).
- Cells containing multiple statements get a line break between statements (write with "\n" and enable wrap for that cell).
- When wrapping text: set row height and column width so every word is visible, but cap column width around 60 characters and row height so the sheet stays scannable. Verify nothing is clipped before delivery.
- Zebra striping only if a table exceeds ~15 rows, and only a very light fill (RGB 245,245,245 or lighter).

## 4. Conditional formatting (approved spec - use these and nothing else)

- RAG status cells: green fill RGB 198,239,206 with dark green text RGB 0,97,0 · amber fill 255,235,156 with text 156,101,0 · red fill 255,199,206 with text 156,0,6.
- Checks cells: green fill when TRUE; red fill with bold text when FALSE.
- Overdue or breached dates: red text RGB 192,0,0, no fill.
- Data bars: permitted only on a single utilisation or progress column, lightest blue, no gradient.
- Hard rules: maximum 3 conditional formatting rule types per sheet · colour is never the only signal (pair with text: "At risk", "Overdue") · never full-table colour scales or icon sets.

## 5. Charts (dedicated Charts tab is the default)

- Any workbook containing a chart gets a "Charts" tab; charts do not float over data tables. Exception: a single small dashboard sheet Nick explicitly asks for.
- Chart source data lives in a labelled block on the Charts tab, formula-linked to the source sheet, with a note "Chart data below feeds the chart; do not delete."
- Title states the insight, not the metric: "Q3 fees up 18% on new retainers", not "Fees by Quarter".
- Direct-label series where possible; kill the legend if labels do the job.
- One highlight colour for the story, greys for context. Max 4 series per chart; more than 4 means small multiples (a row of small identical charts, one per category) or a table.
- Axis starts at zero for bar charts, always. Line charts may truncate only with a visible axis break note.
- Source and date stamp in 10pt near the chart ("Source: Wrike export, 8 Jul 2026").
- No gridlines heavier than the lightest grey; no borders around plot area.

## 6. Automations tab (mandatory on EVERY workbook)

Every workbook ships with an "Automations" tab: a backlog of candidate automations relevant to that workbook's workflow. Minimum 3 realistic rows; do not pad with filler. Exact columns, in this order:

| Automation Name | What it does | Priority | Input Source | Trigger | Output / Destination | Frequency | Suggested Tool(s) | Notes / Constraints / Dependencies | Estimated Time Saved | Estimated Build Time |

- Priority: High / Medium / Low.
- Suggested Tool(s): prefer Apps Script, Zapier, Make, or a Claude skill over VBA, since Nick works in Google Workspace. Name VBA only where desktop Excel is genuinely required, with the constraint noted.
- Estimated Time Saved may be a quality metric where time is not the point ("audit trail", "catches slippage 2-3 weeks earlier").
- Notes column: line breaks between separate points, wrapped.
- This tab replaces shipping actual macros. Build an automation only when Nick asks.

## 7. Strategic insight layer (what separates the workbook from a data dump)

For any analytical or financial workbook, add an "Insights" section (on the summary sheet or Read Me) containing:

1. **Key assumptions register**: each assumption in its own row with columns: Assumption / Value / Source / Confidence % / Could this be challenged? (Yes / No plus one line why).
2. **Success measures**: 2-4 metrics that define whether the thing being modelled is working, each with a target and where in the workbook it is calculated.
3. **Trend context**: what has moved in the last 30 days and 6 months that affects this data, with a hyperlink per claim (real, verified URLs only; if no verified URL exists, say so in the cell). End with one line: "What to do with this".
4. **The hardest concept explained**: one metaphor or analogy in plain language, in a labelled cell, so any reader can grasp the trickiest mechanic in the model.
5. **Checks row**: at least one visible checksum (e.g. "Total across tabs matches: TRUE") using a formula, formatted per section 4.
6. **Sensitivity table**: a two-way grid flexing the 1-2 riskiest assumptions (the ones flagged "Could be challenged: Yes") against the headline output. Build it as an explicit formula grid (openpyxl cannot write native Excel Data Tables); each cell recomputes the output with that row and column input. 5x5 maximum. Shade the current-state cell.
7. **Scenario toggle**: one labelled cell with a data validation dropdown (Base / Upside / Downside), driving assumption values via INDEX/MATCH against a small scenario table. Yellow fill on the toggle cell; the Read Me names it as editable.

Items 6 and 7 apply to financial and forecasting workbooks; skip them (and say so) for pure trackers or lookup files. Skip the whole layer only for trivial files Nick explicitly wants raw.

## 8. Print setup and footers (only when printing is likely)

Apply when the file is likely to be printed or exported to PDF (board packs, work tests, anything Nick says will be shared as PDF). Otherwise leave print settings untouched.

- Landscape, fit to 1 page wide, defined print area per sheet, repeat header row on every page, margins ~1.5 cm.
- No headers or footers unless Nick asks for them. If asked: footer only (file name, tab name, "Page X of Y"), 10pt equivalent; never page headers.

## 9. Instructions as process flow

Any "how to use this" content is written as a process flow, not prose:

| Step | Who | What | When | How | Automation opportunity |

Cross-reference automation opportunities to the Automations tab rather than duplicating detail.

## 10. QA checklist (run before presenting the file)

Confirm every line. If any fails, fix and re-run recalc.py.

1. recalc.py returns success, zero errors.
2. No merged cells anywhere (scan with openpyxl: len(ws.merged_cells.ranges) == 0 on every sheet).
3. No underscores in file name or tab names.
4. No font below 10pt.
5. Totals: columns left, rows top (or documented override).
6. Freeze panes set; filters on 30+ row tables; cursor at A1; zoom 100%.
7. Currency symbols present, 0 decimals; percentages stored as fractions.
8. Contrast check passed on every filled cell; conditional formatting only per section 4 spec.
9. Wrapped cells fully readable; instruction cells overflow, not wrap.
10. Bold totals; vertical centre alignment throughout.
11. Charts on a Charts tab, insight titles, source stamps (section 5).
12. Automations tab present with 3+ realistic rows and all 11 columns (section 6).
13. Insight layer present: assumptions, checks, and (for financial workbooks) sensitivity table and scenario toggle, or a stated reason for skipping.
14. Print setup and footer applied only if printing is likely (section 8); no page headers anywhere.
15. Read the file names, tab names, and headers aloud in your head: would a human colleague have written them exactly like this?

## 11. Example of a great result (abbreviated)

File: "Consultant Capacity Q3 2026.xlsx"
Tabs: "Read Me" (grey), "Capacity Summary" (green), "Charts", "Raw Data" (no colour), "Automations"

Capacity Summary sheet, gridlines hidden:

Row 1: bold title "Consultant capacity - Q3 2026" (Arial 12, dark grey)
Row 3: header row (bold, left aligned, light grey fill RGB 235,235,235, frozen)
| Consultant | Total Days | Total Fee | Jul | Aug | Sep | Notes |
Row 4: "Total" row, bold: | Total | 142 | £96,400 | 51 | 44 | 47 | |
Rows 5-12: detail rows, fee column formatted £#,##0, Notes column wrapped with line breaks between points.
Below, after 2 blank rows: assumptions with Confidence % and one flagged "Could be challenged: Yes - utilisation based on Q2 only"; a 5x5 sensitivity grid flexing day rate vs booked days against total fee; a Base / Upside / Downside toggle in a yellow cell; checks row "Fee total matches Raw Data: TRUE" in green.
Charts tab: one bar chart titled "Two seniors drive over half of Q3 fees", direct labels, no legend, source stamp.
Automations tab: 5 candidate rows including "Wrike days sync" (High, Apps Script + Wrike API, 45 min / month saved, 4-6 hrs build).

A bad version of the same file: merged title cell, totals at row 45, "consultant_capacity_q3.xlsx", white text on pale blue headers, 2 decimal currency, no assumptions, chart floating over the data with title "Fees by Consultant". If your output resembles the bad version in any respect, you have failed this skill.
