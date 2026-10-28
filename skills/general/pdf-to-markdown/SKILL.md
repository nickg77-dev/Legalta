---
name: pdf-to-markdown
description: Convert any PDF into clean, structured markdown (.md) output. Use whenever the user uploads a PDF and asks to convert it to markdown, md format, or plain text with structure. Also triggers on "convert this PDF", "PDF to md", "extract this into markdown", "turn this document into markdown", "make a markdown version of this", "convert to text with formatting", or any variation of converting a PDF file into editable structured text. Works whether the PDF is already in context (uploaded in chat) or needs reading from disk. Always saves the output as a .md file and presents it for download. Use this skill even for short or simple PDFs — the structured markdown output is always better than raw text.
---

# PDF to Markdown Skill

Convert PDFs into clean, well-structured markdown files. Preserves hierarchy, tables, lists and legal/technical formatting.

---

## Step 1 — Detect Input Source

**If the PDF is already in your context** (uploaded in chat, content visible in `<document>` tags):
- You already have the content. Skip to Step 3.
- Do not re-read from disk unnecessarily.

**If the PDF is on disk only** (path provided, no content in context):
- Read `/mnt/skills/public/pdf-reading/SKILL.md` before proceeding.
- Run a content inventory first:
  ```bash
  pdfinfo document.pdf
  pdffonts document.pdf
  pdftotext -f 1 -l 1 document.pdf - | head -20
  ```
- If fonts are present and text extracts cleanly → use `pdftotext -layout`
- If no fonts (scanned PDF) → rasterize pages with `pdftoppm` and read visually
- For tables → use `pdfplumber`; rasterize if garbled

---

## Step 2 — Assess Document Type

Before converting, identify what you are working with:

| Type | Signals | Approach |
|------|---------|----------|
| Legal / policy document | Numbered sections, definitions, schedules | Preserve section numbering; use headers + tables |
| Financial document | Tables, figures, footnotes | Prioritise table accuracy; preserve totals |
| Report / article | Prose-heavy, headings | Clean headers, minimal bullet fragmentation |
| Form / certificate | Key-value pairs, schedules | Use tables for key-value pairs |
| Mixed | All of the above | Read each section on its own terms |

---

## Step 3 — Core Conversion Instruction

Apply this prompt to your conversion task:

```
You are a document conversion specialist with deep expertise in structured
technical and legal documents.

Convert the provided PDF content into clean, well-structured markdown.
The output will be used in Google Docs, Notion, or similar tools — so
preserve all information and hierarchy faithfully.

Rules:
1. HIERARCHY — Use H1 (#) for the document title only. H2 (##) for major
   sections. H3 (###) for subsections. Never skip levels.

2. TABLES — Convert ALL tabular data into markdown pipe tables. Column
   headers in bold is not needed — the pipe format is sufficient.
   Verify totals and alignment match the source exactly.

3. LISTS — Use numbered lists for sequentially ordered items (conditions,
   steps, clauses). Use unordered lists (-) only for genuinely
   unordered items.

4. KEY-VALUE PAIRS — Format as a two-column markdown table
   (| Field | Detail |), not as inline bold text followed by values.

5. LEGAL FORMATTING — Preserve clause numbering exactly as in the source
   (e.g. 1. (a) (b) not 1a, 1b). Do not paraphrase legal text;
   reproduce wording faithfully.

6. FOOTNOTES / NOTICES — Place at end of relevant section, in italics.

7. CONTACT DETAILS — Format as a table or clear block. Never bury in prose.

8. OMIT — Page numbers, headers/footers repeated on every page, and
   decorative elements (logos, dividers) that add no informational value.

9. FIDELITY OVER BREVITY — Do not summarise. Every clause, every table
   row, every defined term must appear in the output.

10. UNCERTAINTY — If a passage is unclear from extraction (garbled, 
    truncated), flag it inline as: [EXTRACTION UNCLEAR — VERIFY SOURCE]

Output: raw markdown only. No preamble. No explanation. Start directly
with the H1 title.
```

---

## Step 4 — Quality Check Before Saving

Before saving, verify:

- [ ] Every major section from the source has a corresponding header
- [ ] All tables are syntactically correct markdown (pipe-separated, with header row and separator line)
- [ ] No section numbering has been renumbered or paraphrased
- [ ] No content from the source has been omitted
- [ ] File name follows convention: `{original_filename_no_ext}.md`

If the document is > 10 pages, spot-check page 1, the middle, and the last page against your output.

---

## Step 5 — Save and Present

Save to `/mnt/user-data/outputs/{filename}.md`

Then call `present_files` with the output path.

Follow with a one-line summary: total sections converted, any tables, and any flagged extraction issues.

---

## Edge Cases

**Scanned PDFs (no text layer):**
Read `/mnt/skills/public/pdf-reading/SKILL.md` → rasterize pages → read visually → convert each page's content into markdown manually. Note at the top of the output: `> Note: Source is a scanned PDF. Content extracted via visual inspection.`

**Multi-column layouts:**
Extract text with `pdftotext -layout` which preserves spatial positioning better than default mode. Rasterize if still garbled.

**Heavily image-based PDFs (charts, diagrams):**
Convert text content faithfully. For each image/chart, insert a placeholder: `[FIGURE: {brief description from visual inspection}]`

**Encrypted PDFs:**
Tell the user the PDF is password-protected and ask for the password or a decrypted version.

**Very large PDFs (> 50 pages):**
Ask the user: "This is a {N}-page document. Do you want the full conversion or specific sections?" Convert the full document only if confirmed.

---

## Output File Naming Convention

`{OriginalFilename_no_extension}.md`

Examples:
- `XLB54325-0022_Farsight_Insurance.pdf` → `XLB54325-0022_Farsight_Insurance.md`
- `Q3_Report_2025.pdf` → `Q3_Report_2025.md`
- `Seefar_SOP_Finance_v3.pdf` → `Seefar_SOP_Finance_v3.md`
