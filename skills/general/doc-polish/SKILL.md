---
name: "doc-polish"
description: "Nick's document polish standard. Use on 'doc polish', 'gdoc polish', 'polish this doc', or whenever creating or editing any document. Google Docs by default; Word only when .docx or Microsoft is asked for."
---

# Doc Polish - Nick's Professional Standard

Purpose: every document should look considered rather than default, read as controlled rather than decorated, and never carry AI-formatting tells (typed separators, mismatched spacing, first-line indents, defaults left untouched).

## 0. Which platform

- DEFAULT: Google Docs. Edit via the Google Docs connector (read_doc, then update_doc batchUpdate). A pasted docs.google.com link means edit that doc.
- Word (.docx) ONLY when Nick explicitly asks for .docx, Word or Microsoft. Then read /mnt/skills/public/docx/SKILL.md for mechanics and apply section 9.
- Europe, not USA: A4 always, never US Letter. UK English, UK date conventions.
- Ask before creating a new document. Editing a doc Nick links = edit in place unless he says copy.

## 1. Non-negotiables

- NEVER em or en dashes. Hyphen with spaces ( - ).
- NEVER typed separator lines, dash rows or empty 'rule' paragraphs. Whitespace or page breaks only.
- NEVER first-line indent a body paragraph. Block style: a blank paragraph between paragraphs.
- NEVER spacing-before on a heading that follows a page/section break.
- NEVER a second font family. Calibri throughout.
- NEVER a font smaller than 10pt anywhere, including tables, footnotes and captions.
- NEVER change Nick's wording during a polish. Formatting only. Suggest wording fixes separately.
- NEVER a full-grid table for 2-3 columns and up to ~5 rows. Use a plain text list (section 5).
- NEVER override hyperlink style. Default blue, underlined.
- NEVER underscores in file names.

## 2. Typography and page setup

- Calibri, 11pt body, pure black.
- Title: Title style, centred, Calibri 20pt bold navy (#1F3864). Title style keeps it out of the TOC.
- Heading 1: 16pt bold navy. Heading 2: 14pt bold navy. Heading 3: 11pt bold black.
- Line spacing single (100). Paragraph spacing 0pt above and below; separation comes from blank paragraphs.
- Left aligned, never justified. Only title and subtitle centred.
- A4: 595.28 x 841.89pt. Margins 2.5cm top/bottom (70.87pt), 1.9cm sides (53.86pt).
- Dates in body: '13th Oct 2026'. Never DD/MM/YYYY in prose. ISO only in file names.
- UK English. Google Docs: File > Language > English (UK) (no API for this; tell Nick if it needs setting).

## 3. Structure

- Heading hierarchy must be logical and unbroken (H1 > H2 > H3, no skipped levels, no bold-normal-text pretending to be a heading). This is what makes a TOC appear neatly if Nick chooses to add one.
- Do NOT insert a TOC. Nick adds it himself (Insert > Page elements > Table of contents). If one exists, leave it and remind him to click refresh after heading changes.
- Heading numbering (1, 1.1) only for governance, legal, policy and SOP documents.
- Bullets: solid round, no hanging indent (indentStart = indentFirstLine). Nested levels step in 18pt per level so hierarchy stays visible.
- Numbered lists 1. 2. 3.; roman numerals only for a nested sub-level.
- Lists are tight (no blank paragraphs between items). Major agenda items or sections get a blank paragraph between them, consistently.
- Emphasis: bold, sparingly. Quotes: indented italic. Code: Consolas on F2F2F2 shading, narrower than text width.
- Draft marking: 'DRAFT' suffix in file name and title. No watermark.

## 4. Page numbers and footers

- Page number in the footer, bottom centre, starting on page 1, on every document regardless of length. No running header.
- Google Docs API CANNOT insert a page number field. Either: (a) tell Nick: Insert > Page elements > Page numbers > the 'footer, all pages' option (bottom-left icon), or (b) do it via Claude in Chrome if he asks. Never type a static number.
- Word: 'Page X of Y' field in footer, bottom centre, from page 1.
- Citations: inline parenthetical for 5 or fewer sources, e.g. (Board minutes, 14th Mar 2026). More than that: Google Docs native footnotes are fine (no separator-line problem); in Word use the footer method only if asked.

## 5. Colour, tables, simple data

- Navy #1F3864 structural (title, headings). Teal #0F6E6E secondary (table header shading). Never teal for headings or body.
- Genuine tables (4+ columns or many rows): top/bottom rule, hairline under header, no verticals, bold header row on teal with white text.
- Simple 2-3 column data: bold header line, then one line per row, values separated by ' - '.

## 6. File naming

- 'Document Name & Purpose - STATUS', e.g. 'Governance Review - DRAFT'. Spaces, no underscores, no / \ : * ? " < > |. Front-load the differentiator.

## 7. Google Docs API mechanics (the gotchas)

- Always read_doc first and pass requiredRevisionId in writeControl so you never overwrite Nick's live edits.
- Named styles cannot be edited via the API. Apply direct formatting (updateTextStyle, updateParagraphStyle) to ranges instead. Setting namedStyleType still matters for TOC structure.
- Page size and margins: updateDocumentStyle.
- Do not apply styles inside a tableOfContents range; skip around it.
- Avoid the final newline of the body segment in ranges.
- Inserting a blank paragraph inside a list: insertText '\n' at the end of the previous item, then deleteParagraphBullets on the new empty paragraph and reset its indents. Order inserts last so earlier indices stay valid.
- Agenda items split across separate list IDs can number oddly. Fixing needs delete-and-recreate bullets; only do it if the rendered numbering is actually wrong.
- Batch everything in one update_doc call; if any request is invalid none apply.

## 8. QA checklist (Google Docs)

1. No em/en dashes in anything you wrote.
2. A4, correct margins.
3. Calibri everywhere, sizes and colours per section 2.
4. Spacing 0 above/below; blank paragraphs used consistently.
5. No hanging indents; nesting visible.
6. Headings form a clean hierarchy; title uses Title style.
7. Links default blue, underlined.
8. Page number in footer from page 1 (or Nick told how to add it in one click).
9. Nick's wording unchanged.
10. Re-read the doc after the update to confirm it applied.

## 9. Word (.docx) only when asked

Apply sections 1-6 using python-docx per the docx skill, plus:
- Set heading and Normal named styles (Word allows it), not just direct formatting.
- TOC: hyperlinked entries to bookmarks, simple list, under half a page, only if asked.
- Footer 'Page X of Y' bottom centre from page 1.
- Document properties: Title and Author set, Company blank. Proofing language English (UK).
- Bullets via numbering definitions with no hanging indent.
- Deliver via SendUserFile with a 'Name & Purpose - STATUS.docx' file name.