# Sources and data - using the Data Sources and Market Scoring tabs

## Data Sources tab (Process Flow workbook)
One row per source. Columns: Country | Source name | Segment | Sub-segment | Source type | URL | What it gives | Access | Est. database size | How to use it (tool + Claude prompt) | Check result | Cost | Licence / reuse terms | Named people | Covers 1998-2012 | Evidence | Confidence.

The eight source types: Operator licence registers; Company registers; Public-body registers; Tender databases; Association member directories; Trade fair exhibitor lists; Vehicle registration statistics; Court and claim records.

Filter by Country and Segment first, then read "How to use it". Only rows marked Live count as usable. Blocked rows need a human to open them in a browser.

## Picking the extraction method from the Access column
| Access | Method | Tool order |
|---|---|---|
| Bulk download (CSV, ZIP, XML) | Download, clean, filter in code | bash + Python; if no code execution, give the human exact download steps and a Sheets formula plan |
| API | Scripted calls, keep a request log | Python (requests); respect rate limits and key terms |
| Scrape (public directory pages) | Crawl listing pages, extract fields | Firecrawl connector; then web_fetch; then curl + Python |
| Lookup only (one company at a time) | Seed IDs from a company register, then look each up | Claude in Chrome or Playwright (Code); otherwise output a lookup worklist for a human |
| Paid | Do not buy. Flag the cost and what it would add to Nick | None |
| Login-gated (e.g. e-Devlet) | A local partner runs the search; Claude tabulates the export | Human + Claude |

Rules: obey robots.txt and terms of use; never scrape behind a login; record source URL and date on every row; keep company registration numbers wherever they exist (they are the match key).

## Market Scoring tab
Formula-driven from Data Sources: counts source types with a Live URL per country, weighted (operator licence register 3, company register 2, tender database 2, association directory 2, others 1). High 9+, Medium 5-8, Low below 5. Weights sit in yellow cells.
- High: download and scrape.
- Medium: mix scraping with association and manual research.
- Low: lead with intermediaries (associations, dealers); research list sources in parallel.
- Fewer than 4 live source types for the country: run the Research Prompt tab for that country and add results to Data Sources before building a list.

A High rating means rich data, not an open market. Always read it next to the Market Fit Matrix and the Saturation register.

## Sizing (Process Flow step 3)
Start from Thomas's Truck Cartel Claims Market Research figures. Only research further where his document has nothing for the segment. Use Vehicle registration statistics rows for the 1998-2012 stock. Record every figure with source and date. Be conservative.
