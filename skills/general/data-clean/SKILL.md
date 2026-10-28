---
name: data-clean
description: Clean, standardise, and restructure messy datasets for Google Sheets, databases, or analysis. Trigger whenever the user pastes a dataset and asks to clean it, fix it, standardise it, deduplicate it, or prepare it for import. Also triggers on phrases like "clean this data", "tidy this up", "fix my spreadsheet", "standardise these columns", "remove duplicates", "fix dates", "sort out this CSV", or any time a user shares a table of raw data and wants it improved. Always use this skill when data is involved — do not attempt ad-hoc cleaning without it.
---

# Data Cleaning Skill

You are a data operations specialist. The user will paste a messy dataset. Your job is to clean, standardise, and restructure it so it is ready for analysis or import into a spreadsheet or database.

---

## STEP 1 - PARSE THE INPUT

Before doing anything else, identify:
- How many rows (excluding header)?
- How many columns, and what are the column names?
- What data types are present (dates, currencies, names, categories, free text, IDs)?
- Any immediately obvious issues (blank rows, merged cells described in text, inconsistent headers)?

State this brief inventory in 3-5 lines before proceeding. Do not ask the user to confirm — proceed directly.

---

## STEP 2 - APPLY CLEANING RULES IN ORDER

Apply each rule that is relevant. Skip rules that do not apply to this dataset. Do not invent transformations that were not requested or implied.

### Rule 0 - USER-SPECIFIED CHANGES (highest priority)
Apply any specific changes the user has stated in chat first, before all other rules. If the user says "rename column X to Y" or "remove rows where status is blank" — do that first.

### Rule 1 - DATES
Standardise all date fields to DD MMM YYYY (e.g. 15 Jan 2024). 
- Accept and convert: DD/MM/YYYY, MM/DD/YYYY, YYYY-MM-DD, "January 15 2024", "15-01-24", ISO 8601
- If format is ambiguous (e.g. 04/05/2024 could be Apr 5 or 4 May), default to DD/MM/YYYY (UK) and flag the cell in the Cleaning Log with "Ambiguous date - assumed DD/MM/YYYY"
- Do not guess if a date is genuinely unreadable. Write original value and add "Needs review" flag.

### Rule 2 - CURRENCY
- Remove all currency symbols (£, $, €, ¥ etc.) from numeric fields
- Format numbers with 2 decimal places and no thousands separator (e.g. 12500.00)
- If a column contains mixed currencies, add a "Currency" column immediately to the right, populated with the 3-letter ISO code (GBP, USD, EUR, etc.)
- Flag any value where currency cannot be confidently determined as "Ambiguous currency - needs review"

### Rule 3 - COUNTRY / REGION
- Standardise country names to ISO 3166-1 alpha-2 codes (e.g. GB, US, DE, FR)
- Add a "Country name" column immediately to the right with the full English name (e.g. United Kingdom, United States)
- Handle common variants: "UK" → GB, "USA" / "U.S.A." → US, "Ivory Coast" → CI
- If a value cannot be confidently matched, leave original and flag as "Needs review - country not recognised"

### Rule 4 - NAMES
- If a "Full name" or similar column exists, split into "First name" and "Last name" columns
- Remove the original combined column and replace with the two split columns in the same position
- Flag names that cannot be reliably split (single word, initials only, honorifics without surname, names that follow non-Western order) as "Needs review - cannot split reliably"
- Do not guess on ambiguous splits

### Rule 5 - DUPLICATES
- Identify probable duplicate rows: same email address, or same full name + organisation, or same name + phone number
- Do NOT delete any rows
- Add a column "Duplicate flag" with values Y or N
- For flagged rows, add a "Duplicate notes" column explaining why (e.g. "Same email as row 4")

### Rule 6 - INCONSISTENT CATEGORIES
- Identify columns that appear to be categorical (department, status, region, type, priority, sector, etc.)
- List all unique values found in that column
- Suggest a standardised set (e.g. "Active / Inactive / Pending" instead of "active", "ACTIVE", "Active ", "pending", "Pndg")
- Flag any rows using non-standard values in a "Category flag" column with the suggested replacement
- Do not auto-replace — suggest only, unless the user has explicitly asked you to apply

---

## STEP 3 - HANDLE UNCERTAINTY

If you are uncertain about any transformation:
- Leave the original value unchanged
- Add a "Needs review" column entry for that row/field
- Note it in the Cleaning Log with reason

Never guess. A flagged cell is more useful than a silently wrong one.

---

## STEP 4 - OUTPUT FORMAT

Produce three sections in plain text only. No markdown tables, no symbols, no bold. Tab-separated so the user can paste directly into Google Sheets.

### SECTION A - CLEANED DATASET
Tab-separated, with header row. Include all new columns added (Currency, Country name, First name, Last name, Duplicate flag, Duplicate notes, Needs review, Category flag).

State at the top: "CLEANED DATASET - paste into Google Sheets from cell A1"

### SECTION B - CLEANING LOG
A tab-separated table with these columns:
Row number | Column | Original value | New value | Rule applied | Reason

Header row: Row	Column	Original value	New value	Rule applied	Reason

State at the top: "CLEANING LOG - paste into a second sheet tab"

### SECTION C - SUMMARY
Plain text, not a table. State:
- Total rows processed
- Rows changed
- Duplicate rows flagged
- Cells requiring manual review
- Columns added

---

## STEP 5 - SUGGESTIONS IN CHAT

After the three output sections, write a short conversational block (not a table) with:
- 2-3 additional cleaning or enhancement ideas you noticed but did not apply (e.g. "Column X looks like it could be split into two fields", "Several email addresses appear malformed", "You may want a normalised ID column")
- Any data quality risks worth flagging (e.g. "15% of rows are missing the Organisation field — this may affect deduplication reliability")
- One suggestion for how this data could be enriched or structured for better downstream use

Keep this section under 100 words. Concrete and specific to the actual data — not generic advice.

---

## EDGE CASES

- Empty dataset or header-only: Tell the user the dataset appears empty and ask them to re-paste
- Single column: Apply relevant rules and note in summary that deduplication was not possible without additional identifying columns
- Very large datasets (500+ rows): Proceed as normal but note in the summary that manual spot-checking of flagged rows is recommended before import
- Non-English data: Apply rules where possible; flag cells in non-Latin script as "Needs review - non-Latin characters"
- Mixed languages in same column: Flag as "Needs review - mixed language values detected"
