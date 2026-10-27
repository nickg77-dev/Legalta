---
name: shopping-comparison-table
description: "Interview Nick on buying criteria, research candidate products across named sites, and build a dark-theme interactive HTML comparison table artifact with images, ticks/crosses, colour-coded ratings, review links and a live filter."
---

# Shopping comparison table

Builds the same kind of artifact as Nick's monitor shortlist: a dark-theme HTML table people actually use to make a buying decision, not a one-off written comparison. Four phases: interview, research, build, deliver. Do not skip the interview to save time - a table built on guessed criteria gets rebuilt anyway.

## 1. Interview

Ask before searching (per Nick's standing instruction to clarify before big tasks; skip only if he's already given all of this in his request):

- **Hard budget cap** vs a soft target, and whether it applies to new, used/refurb, or both
- **Must-haves** (deal-breakers if absent) vs **nice-to-haves** (tiebreakers only)
- **Explicit exclusions** - sizes, brands, conditions he won't accept
- **Condition tolerance** - new only, refurb OK, used OK, collection-only OK
- **Sources to search** - named retailers/marketplaces, or "anywhere legitimate"
- **The one or two hardest-to-verify specs** - ask what "good" looks like on these (e.g. Nick's curve-radius sweet spot of 1500-2000R). These become the colour-coded rating column(s).
- **Existing shortlist items** he's already found, so they're included and cross-checked rather than silently dropped or duplicated

State assumptions and move straight into research once answered - don't re-ask what's already stated.

## 2. Research

**Sourcing.** Two methods, use whichever fits:
- Web search + WebFetch against named retailers/marketplaces (eBay, Currys, etc.) - the default when Nick names sites or gives a broad brief.
- Reading directly from open browser tabs (claude-in-chrome) when Nick has specific listings already open - faster, and Anthropic's own "compare products across sites" workflow recommends this for a handful of specific pages. Ask Nick to specify priority criteria upfront either way; it focuses extraction and avoids pulling irrelevant specs.

**Verification discipline** (the recurring failure mode in Nick's monitor table): marketplace listings auto-fill item specifics from a master catalogue and are frequently wrong for the exact SKU listed - a 2017 Dell showed "USB-C" it never had; an AOC listing called a flat panel "curved." For any spec that's a deal-breaker or feeds a rating badge, cross-check against the manufacturer's own spec sheet or an independent review, not the listing text alone. When sources disagree, keep both and flag it in the note rather than picking one silently (Anthropic's pattern: "normalized both to comparable estimates" - state the normalization, don't hide it).

**Per-candidate research bundle**, gather all of this before building anything:
1. Model name + the current listing/retailer link
2. Price, with any postage/collection caveats
3. The must-have spec values, verified
4. **One manufacturer product-page link** (brand.com, not a retailer) - if none exists (discontinued, private-seller-only, generic/unbranded item), say so; never substitute a retailer link and call it the manufacturer's
5. **Two independent review links** where they exist - a reputable review site (RTINGS, PCMonitors.info, TechRadar, StorageReview, Tom's Hardware, Wirecutter, etc., pick the ones relevant to the product category) plus a retailer customer-reviews page (Amazon, John Lewis, etc.). If a genuine review can't be found, write "No verified review" - never fabricate a plausible-looking link
6. **One product image URL from the manufacturer's own site** - not a retailer photo, not a stock photo. If the manufacturer doesn't have a usable image (page requires JS, image is behind auth, discontinued product with no surviving page), fall back to the retailer listing photo and label it as such in the alt text, or omit the image and say why
7. Returns/warranty terms as stated by the seller

Fan this out to sub-agents only when the candidate list is long (8+) and each needs independent multi-step research - for a handful of items, do it directly.

## 3. Build

One self-contained HTML file, dark theme, following this structure (adapt column names/count to the product category - the mechanics below are the reusable part):

```html
<style>
/* base tokens - reuse Nick's monitor-table palette */
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-size:13px;background:#0f1117;color:#d4d4d8;padding:20px}
.table-wrap{overflow-x:auto;border-radius:8px;border:1px solid #27272a}
table{width:100%;border-collapse:collapse;min-width:1000px}
thead th{background:#18181b;color:#71717a;font-size:10px;text-transform:uppercase;letter-spacing:.05em;padding:8px;border-bottom:1px solid #27272a;white-space:nowrap}
th.sortable{cursor:pointer}
tbody tr{border-bottom:1px solid #1f1f23}
tbody tr:hover{background:#18181b}
td{padding:8px;vertical-align:top}

/* image cell - new */
.thumb{width:64px;height:64px;object-fit:cover;border-radius:6px;background:#18181b;border:1px solid #27272a}
.thumb-missing{width:64px;height:64px;display:flex;align-items:center;justify-content:center;color:#3f3f46;font-size:9px;border:1px dashed #27272a;border-radius:6px}

.model-name a{color:#f4f4f5;text-decoration:none;border-bottom:1px dotted #52525b}
.reviews{font-size:10px;line-height:1.6}
.reviews a{color:#6366f1;text-decoration:none;display:block}

/* generic rating badge - rename per product (was curve-badge) */
.rating-badge{display:inline-block;padding:2px 7px;border-radius:3px;font-size:11px;font-weight:600}
.rating-green{background:#0d2818;color:#4ade80;border:1px solid #166534}   /* meets Nick's target */
.rating-amber{background:#2a1f00;color:#fbbf24;border:1px solid #713f12}   /* off-target, not disqualifying */
.rating-red{background:#3b0000;color:#f87171;border:1px solid #7f1d1d}    /* fails a stated criterion */
.rating-grey{background:#1a1a1a;color:#71717a;border:1px solid #27272a}   /* unconfirmed/unpublished */

.verdict{display:inline-block;padding:2px 8px;border-radius:4px;font-size:10px;font-weight:600}
.v1{background:#14532d;color:#86efac} .v2{background:#1c3461;color:#93c5fd}
.v3{background:#312e00;color:#fde68a} .v4{background:#1f0a0a;color:#f87171}

/* live text filter - new */
#livefilter{background:#18181b;border:1px solid #27272a;color:#f4f4f5;padding:5px 10px;border-radius:4px;font-size:12px;min-width:200px}
</style>

<input id="livefilter" placeholder="Filter by anything (model, seller, spec)..." oninput="liveFilter(this.value)">
<!-- keep the existing preset filter-btn row alongside this - they're complementary, not a replacement -->

<!-- one row per candidate -->
<tr data-price="119.99" data-tags="used,top,curved,ips" data-rating="1900">
  <td><img class="thumb" src="https://manufacturer.example/product.jpg" alt="Model name, manufacturer photo" onerror="this.outerHTML='<div class=&quot;thumb-missing&quot;>No image</div>'"></td>
  <td><div class="model-name"><a href="https://manufacturer.example/product-page" target="_blank">Model name</a></div></td>
  <!-- ...spec columns, reviews column, verdict column as in the monitor table... -->
</tr>

<script>
function liveFilter(q) {
  q = q.toLowerCase();
  document.querySelectorAll('#tbody tr').forEach(row => {
    const match = row.textContent.toLowerCase().includes(q);
    // combine with any active preset filter - only show rows passing BOTH
    row.style.display = (match && row.dataset.hidden !== 'true') ? '' : 'none';
  });
}
// keep the existing setFilter()/sortBy() functions from the monitor table unchanged;
// setFilter should set data-hidden as before, then re-run liveFilter(current search value)
// so the two filters compose instead of fighting each other
</script>
```

Keep from the monitor table unchanged: preset filter buttons (`setFilter`), sortable price/rating columns (`sortBy`), the summary verdict cards at the bottom (best value / best on the top must-have / best budget / avoid), the VESA-style explanatory footnote pattern for any jargon term, and the `updatebox` banner at the top stating what changed since the last version and the date researched.

Add from this skill: the image column, the live filter box, and generalise `curve-badge` naming to whatever the hardest-to-verify spec is for this product category (rating-badge above).

## 4. Deliver

Publish via the Artifact tool if this is a one-off, or `project_write` if Nick has a project open for this purchase (check first) so revisions update the same doc. Confirm before creating a brand-new doc if one might already exist for this topic (search the project first). After delivering, state in plain text: what changed since the last version (if any), which specs came from manufacturer/independent sources vs listing auto-fill, and which items got "no verified review"/"no verified link"/missing image rather than a fabricated one.