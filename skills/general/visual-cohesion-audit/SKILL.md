---
name: visual-cohesion-audit
description: Scores a website's visual cohesion (palette, typography, layout, dated look) on desktop and mobile against the two top-scoring Webby winners, and produces a plain-language report for business owners and designers. Use to critique a site's look and feel or judge if it feels dated, busy or jumbled.
---

# Visual Cohesion Audit

Turns "it looks jumbled and dated" into evidence a site owner can act on. Three layers:

1. **Measured**: a script reads the rendered page's computed styles and scores 11 measurements against top marks set by the two top-scoring award-winning sites, on desktop and mobile.
2. **Automated checks**: about 40 pass/fail rules adapted from three open-source design review tools.
3. **Designer's eye**: six fixed questions scored 1 to 5 from screenshots.

Not for accessibility compliance or SEO (use accessibility-review and seo-check).

## Who reads the report

Assume a business owner or a web designer receiving it cold. So:
- Objective commentary only. Never refer to the requester's opinions, earlier drafts, corrections, or the chat.
- Plain language on the main page. Rule ids, tool names, colour science and severities go in the Technical details tab.
- Call the audited site by its name everywhere, never "this site".
- Every score states its scale: "86 out of 100", or a percentage for single measurements.
- Plain section headings ("What is holding it back", "How it looks to a designer", "Recommended changes").
- Run the humanise-writing skill in formal mode over all prose. British English, sentence-case headings, no em or en dashes (write "15 to 18px").

## Workflow

1. **Render in a real browser** (built-in browser or Claude in Chrome, via javascript_tool). If no browser can reach the site, say so and stop: never estimate from scraped markdown, which misses navigation, cookie banners and computed styles.
2. **Read the copy** with get_page_text, and open any accordions (`document.querySelectorAll('details').forEach(d=>d.open=true)`) so FAQ answers are included. Copy issues found here can feed the recommendations.
3. **Desktop pass**: resize_window to 1366x800, reload, run the script. **Mobile pass**: resize_window preset mobile (375x812), reload, run again. The script picks desktop or mobile targets from the viewport width. Reset the viewport when finished.
4. Prepend this scroll loop so lazy sections load: `for(let y=0;y<document.body.scrollHeight;y+=700){scrollTo(0,y);await new Promise(r=>setTimeout(r,200))};scrollTo(0,0);await new Promise(r=>setTimeout(r,800));` If the tool struggles with length, minify with `npx terser -c -m` after changing the opening `(() => {` to `globalThis.__vca = (() => {`, ending `;JSON.stringify(globalThis.__vca)`.
5. **Screenshots**: desktop at 4 or 5 scroll positions (scale 0.75) and the mobile opening screen. Decline cookie banners only if they block the view; never accept.
6. **Optional**: if the user's computer has Node and Chrome and they approve, `npx impeccable detect --json <url>` adds Impeccable's 59 rules.
7. **Build the report** (format below), render it once to check, publish as an artifact.

## Scoring

- Each measurement scores 0 to 100%. **100% = matches the better of the two top sites.** 0% = a fixed level clearly below standard (5 typefaces, 14 text sizes, 5 colour families, accent chroma 0.05, 30% pastel, 80% centred, 40 gap sizes, 12 boxes over photos, 200 words before scrolling, 10 corner styles). Paragraph size scores 100% between 15 and 18px, falling to 0% at 10px or 26px.
- A category score is the plain average of its measurements. The Cohesion Index is the plain average of the three categories. Always show the arithmetic in the top-marks tab ("Average of 100% + 57% + 100%, divided by 3").
- Define the index in one sentence at the top: "The Cohesion Index scores a homepage out of 100 for how consistently it uses colour, type and layout, against the two highest-scoring award-winning websites we measured."
- Reading: 85 and above is at award-winner level; 70 to 84 is behind but coherent; under 70 looks inconsistent or dated.

## Top sites (refresh yearly)

The two highest-scoring of five Webby winners measured on 8 October 2026: Obama Foundation (https://www.obama.org/, Webby 2025 Non-Profit) and Soma Surf Therapy (https://www.somasurf.org/, Webby 2024 People's Voice Non-Profit). Desktop index 87 and 92, mobile 94 and 87. The others measured were Maui Food Bank, FOLLOW.ART and Cowboy. Exclude immersive 3D showpieces (Best Visual Design, Aesthetic). To refresh: measure current Webby non-profit and Visual Design (Function) winners on both screen sizes, keep the top two by average index, and update `TD` and `TM` in the script with the better of the two on each measurement.

Calibration lessons: these separate strong sites from dated ones: accent strength, pastel share, a display face used for paragraphs, paragraph size, centred text, number of section gap sizes, boxed text over photos, words before scrolling. These do not, so never lead with them: number of font families, text over photos in general, off-grid spacing, and strict-rule deductions (winners fail several). Orange and yellow accents cannot reach the chroma of blue or magenta on screen, so note that the accent measure understates them.

## Report format (artifact)

Header: title with the audited site linked, measurement date, the one-sentence index definition. A sticky bar with three tabs and a Desktop/Mobile switch that updates every number.

**Summary tab**
1. Large index out of 100 with the two top sites' scores, and three or four plain sentences on the cause. Name the era if it looks dated.
2. "How the homepage compares": bars for the site and the two top sites, names linked.
3. "Where the gaps are": per measurement, a single bar filled to the site's percentage (full bar in green, otherwise the site colour), the percentage on the right of the title row, and beneath it "[Site name]: [value]" on the left and "Top mark: [value], as on [top site]" on the right. Group by category with the category score in the group header.
4. "What is holding it back": the three biggest gaps, each with "[Category]: X out of 100 (top sites A and B)", a plain explanation and a screenshot.
5. "On a phone": the mobile score and what changes, with the mobile screenshot.
6. "What already works".
7. "How it looks to a designer": the six questions below, each with 1 to 5 pips and one plain sentence.
8. "Recommended changes": numbered, in order of impact, each specific enough to do (values, sizes, colours).
9. "Where to look for good examples": linked Webby category pages, Refero (https://refero.design), and both top sites.

**How to get top marks tab**: one card per category with its score and the averaging arithmetic, then a table: measurement and how to improve it, current value, top mark (with the site that sets it), score as a percentage.

**Technical details tab**: method, scoring rules and 0% levels, all scores table, automated checks (severity, plain name, what it means, rule id and source tool), colours found as a ranked stacked bar plus ranked swatches (number, hex, share, plain role), limits, credit line.

Never include anything about earlier versions of the report or what changed.

## Designer's eye (score 1 to 5)

1. Does each colour have a clear job?
2. Does it look current? Template era (about 2014 to 2018): highlighter behind headlines, translucent boxes over stock photos, a light display serif for paragraphs, pastels with no neutral system, centred paragraphs, patterned sticky headers, uncaptioned logo grids, justified text, mixed icon styles. AI era (2023 on): cream with orange or terracotta, orange or italic accent words in serif headlines, all-caps labels above sections, 01/02 numbering where order means nothing, purple-blue gradients, Inter everywhere, three identical icon cards, glass effects. 0 to 1 tells is current; 4 or more reads as dated or generic.
3. Is the main action obvious?
4. Is the spacing even?
5. Do the images share one style?
6. Does it suit the organisation?

## Sources (credit in the Technical tab)

- Impeccable by Paul Bakaus, https://github.com/pbakaus/impeccable (Apache-2.0).
- Design Auditor, https://github.com/Ashutos1997/claude-design-auditor-skill (MIT).
- avoid-ai-design, https://github.com/funboy322/avoid-ai-design (MIT).
- Inspiration library: Refero, https://refero.design.

## Audit script (v6)

```javascript
// Visual cohesion audit v6. Run in page context after the page has been scrolled once to load lazy sections.
// Returns raw metrics, rule findings (with severity), sub-scores, a Cohesion Index and a Craft score.
(() => {
  const VW = innerWidth, VH = innerHeight, SY = scrollY;
  const cs = el => getComputedStyle(el);
  const rect = el => el.getBoundingClientRect();
  const vis = el => { const r = rect(el), s = cs(el); return r.width > 2 && r.height > 2 && s.visibility !== 'hidden' && s.display !== 'none' && +s.opacity > 0.05; };
  const parse = c => { const m = c && c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); return { r: p[0], g: p[1], b: p[2], a: p[3] ?? 1 }; };
  const lin = v => { v /= 255; return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
  const oklab = ({ r, g, b }) => { const R = lin(r), G = lin(g), B = lin(b);
    const l = Math.cbrt(0.4122214708*R+0.5363325363*G+0.0514459929*B), m = Math.cbrt(0.2119034982*R+0.6806995451*G+0.1073969566*B), s = Math.cbrt(0.0883024619*R+0.2817188376*G+0.6299787005*B);
    const L = 0.2104542553*l+0.7936177850*m-0.0040720468*s, a = 1.9779984951*l-2.4285922050*m+0.4505937099*s, bb = 0.0259040371*l+0.7827717662*m-0.8086757660*s;
    return { L, a, b: bb, C: Math.hypot(a, bb), h: (Math.atan2(bb, a) * 180 / Math.PI + 360) % 360 }; };
  const lum = ({ r, g, b }) => 0.2126*lin(r)+0.7152*lin(g)+0.0722*lin(b);
  const contrast = (x, y) => { const a = lum(x), b = lum(y); return (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05); };
  const bgOf = el => { for (let e = el; e; e = e.parentElement) { const c = parse(cs(e).backgroundColor); if (c && c.a > 0.5) return c; } return { r: 255, g: 255, b: 255, a: 1 }; };
  const hex = c => '#' + [c.r, c.g, c.b].map(v => Math.round(v).toString(16).padStart(2, '0')).join('').toUpperCase();
  const ownText = el => [...el.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent).join(' ').replace(/\s+/g, ' ').trim();
  const findings = []; const flag = (id, sev, source, detail) => findings.push({ id, sev, source, detail });

  const all = [...document.body.querySelectorAll('*')].filter(vis);
  const textEls = all.filter(el => ownText(el).length > 1);
  const bodySizes = new Map(), bodyFam = new Map(), fam = new Map(), sizes = new Map(), weights = new Set(), lefts = new Map(), aligns = new Map();
  let words = 0, wordsFold = 0, lowContrast = 0, longLineWords = 0, textOverImage = 0, tightLeading = 0, tinyWords = 0, smallBody = 0, justified = 0, capsBody = 0;
  const images = all.filter(el => el.tagName === 'IMG' || el.tagName === 'VIDEO' || (cs(el).backgroundImage.includes('url(') && rect(el).width > 200)).map(rect).filter(r => r.width * r.height > 40000);
  const colourSamples = [], overlaid = new Set(), panels = new Set();
  for (const el of textEls) {
    const s = cs(el), r = rect(el), t = ownText(el), w = t.split(' ').filter(Boolean).length, px = parseFloat(s.fontSize);
    const f = s.fontFamily.split(',')[0].replace(/["']/g, '').trim().toLowerCase().replace(/[-_ ]?(light|regular|bold|medium|thin|semibold|italic|w0[0-9]|w[0-9]+)$/, '');
    fam.set(f, (fam.get(f) || 0) + w); sizes.set(Math.round(px), (sizes.get(Math.round(px)) || 0) + w); weights.add(s.fontWeight);
    aligns.set(s.textAlign, (aligns.get(s.textAlign) || 0) + w);
    if (w >= 8) { const x = Math.round((r.left + scrollX) / 4) * 4; lefts.set(x, (lefts.get(x) || 0) + 1); }
    words += w; if (r.top + SY < VH) wordsFold += w;
    const fg = parse(s.color), bg = bgOf(el);
    if (fg) { colourSamples.push({ c: fg, w: w * 3 }); if (contrast(fg, bg) < (px >= 24 ? 3 : 4.5) && w > 2) lowContrast += w; }
    const body = w >= 12 && px < 24;
    if (body) { bodySizes.set(Math.round(px), (bodySizes.get(Math.round(px)) || 0) + w); bodyFam.set(f, (bodyFam.get(f) || 0) + w);
      const charsPerLine = r.width / (px * 0.5); if (charsPerLine > 85 && t.length > 160) longLineWords += w;
      const lh = s.lineHeight === 'normal' ? 1.2 : parseFloat(s.lineHeight) / px; if (lh < 1.3) tightLeading += w;
      if (px < 14) smallBody += w; if (s.textAlign === 'justify') justified += w;
      if (s.textTransform === 'uppercase' && t.length > 40) capsBody += w;
    }
    if (px < 12 && w > 2) tinyWords += w;
    const cx = r.left + r.width / 2, cy = r.top + r.height / 2;
    const hit = images.findIndex(i => cx > i.left && cx < i.right && cy > i.top && cy < i.bottom);
    if (w > 3 && hit >= 0) { textOverImage++; overlaid.add(hit);
      for (let e = el; e && e !== document.body; e = e.parentElement) { const er = rect(e), ec = parse(cs(e).backgroundColor); if (ec && ec.a > 0.5 && er.width * er.height < 0.7 * images[hit].width * images[hit].height) { panels.add(e); break; } if (er.width * er.height >= 0.7 * images[hit].width * images[hit].height) break; } }
  }
  const W = Math.max(words, 1);
  // Boxes, radii, shadows, AI-tell surfaces
  let boxes = 0, sideTabs = 0, glows = 0, gradientText = 0, purpleGrad = 0, bounce = 0; const radii = new Set(), shadows = new Set(), spacing = [];
  for (const el of all) {
    const s = cs(el), r = rect(el), c = parse(s.backgroundColor), area = r.width * r.height;
    if (c && c.a > 0.5 && area > 5000) colourSamples.push({ c, w: Math.sqrt(area) / 10 });
    const boxed = (c && c.a > 0.5) || (s.borderStyle !== 'none' && parseFloat(s.borderWidth) > 0);
    if (boxed && area > 5000 && r.width < VW * 0.95) { boxes++; radii.add(s.borderRadius); }
    if (s.boxShadow !== 'none') { shadows.add(s.boxShadow); if (/(rgba?\([^)]*\))\s+0px\s+0px\s+([1-9]\d)px/.test(s.boxShadow)) { const sc = parse(s.boxShadow); if (sc && oklab(sc).C > 0.08) glows++; } }
    const bl = parseFloat(s.borderLeftWidth), br = parseFloat(s.borderRightWidth), bt = parseFloat(s.borderTopWidth);
    if (bl > 1 && bl > bt + 1 && area > 5000) { const bc = parse(s.borderLeftColor); if (bc && oklab(bc).C > 0.06) sideTabs++; }
    if ((s.webkitBackgroundClip === 'text' || s.backgroundClip === 'text') && s.backgroundImage.includes('gradient')) gradientText++;
    if (/linear-gradient/.test(s.backgroundImage) && area > 40000) { const cols = (s.backgroundImage.match(/rgba?\([^)]+\)/g) || []).map(parse).filter(Boolean).map(oklab); if (cols.some(o => o.h > 270 && o.h < 320 && o.C > 0.1) && cols.some(o => o.h > 230 && o.h < 270 && o.C > 0.1)) purpleGrad++; }
    if (/cubic-bezier\([^)]*(-0\.[1-9]|1\.[1-9])/.test(s.transitionTimingFunction + s.animationTimingFunction)) bounce++;
    if (area > 20000 && r.width > VW * 0.5) for (const p of ['paddingTop', 'paddingBottom', 'marginTop', 'marginBottom']) { const v = parseFloat(s[p]); if (v >= 8) spacing.push(Math.round(v)); }
  }
  // Colour clustering (OKLab deltaE > 0.06 = visibly different)
  const clusters = [];
  for (const { c, w } of colourSamples) { const o = oklab(c); const k = clusters.find(k => Math.hypot(k.o.L - o.L, k.o.a - o.a, k.o.b - o.b) < 0.06); if (k) k.w += w; else clusters.push({ o, c, w }); }
  const total = clusters.reduce((a, k) => a + k.w, 0) || 1;
  const sig = clusters.filter(k => k.w / total > 0.01).sort((a, b) => b.w - a.w);
  const chromatic = sig.filter(k => k.o.C > 0.04);
  const hueGroups = []; for (const k of chromatic) if (!hueGroups.some(h => Math.min(Math.abs(h - k.o.h), 360 - Math.abs(h - k.o.h)) < 25)) hueGroups.push(k.o.h);
  const neutralShare = sig.filter(k => k.o.C <= 0.04).reduce((a, k) => a + k.w, 0) / total;
  const peakChroma = chromatic.length ? Math.max(...chromatic.map(k => k.o.C)) : 0;
  const pastelShare = chromatic.filter(k => k.o.C < 0.12 && k.o.L > 0.6).reduce((a, k) => a + k.w, 0) / total;
  const chromaSpread = chromatic.length > 1 ? Math.max(...chromatic.map(k => k.o.C)) / Math.min(...chromatic.map(k => k.o.C)) : 1;
  const cream = sig[0] && sig[0].o.L > 0.93 && sig[0].o.C > 0.01 && sig[0].o.h > 60 && sig[0].o.h < 100 && chromatic.some(k => k.o.h > 30 && k.o.h < 60);
  // Type scale
  const usedSizes = [...sizes].filter(([, w]) => w / W > 0.01).map(([s]) => s).sort((a, b) => a - b);
  const ratios = usedSizes.slice(1).map((s, i) => s / usedSizes[i]);
  const mean = ratios.length ? ratios.reduce((x, y) => x + y) / ratios.length : 1;
  const ratioCV = ratios.length > 1 ? Math.sqrt(ratios.reduce((a, r) => a + (r - mean) ** 2, 0) / ratios.length) / mean : 0;
  const nearDupSizes = ratios.filter((r, i) => usedSizes[i + 1] - usedSizes[i] <= 2).length;
  const famUsed = [...fam].filter(([, w]) => w / W > 0.02).sort((a, b) => b[1] - a[1]);
  const leftEdges = lefts.size, centred = (aligns.get('center') || 0) / W;
  const isBtn = el => { const s = cs(el), c = parse(s.backgroundColor), pb = el.parentElement ? bgOf(el.parentElement) : null; return (c && c.a > 0.5 && pb && Math.abs(lum(c) - lum(pb)) > 0.02) || (parseFloat(s.borderTopWidth) >= 1 && s.borderTopStyle !== 'none' && parseFloat(s.borderBottomWidth) >= 1); };
  const ctasFold = all.filter(el => (el.tagName === 'A' || el.tagName === 'BUTTON') && !el.closest('nav,header,footer,[role=navigation]') && rect(el).top + SY < VH && rect(el).height > 28 && rect(el).width > 60 && isBtn(el)).length;
  // Headings: order, rhythm, hierarchy
  const hs = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].filter(vis);
  const h1s = hs.filter(h => h.tagName === 'H1').length; let skipped = 0, rhythmBad = 0;
  hs.forEach((h, i) => { const lvl = +h.tagName[1]; if (i && lvl > +hs[i - 1].tagName[1] + 1) skipped++;
    const s = cs(h); if (parseFloat(s.marginTop) + parseFloat(s.paddingTop) < parseFloat(s.marginBottom) + parseFloat(s.paddingBottom) - 4) rhythmBad++; });
  const bodySize = [...bodySizes].sort((a, b) => b[1] - a[1])[0]?.[0] || 16;
  const headSizes = [...new Set(hs.map(h => Math.round(parseFloat(cs(h).fontSize))))].sort((a, b) => a - b);
  const steps = [bodySize, ...headSizes.filter(s => s > bodySize)]; const flatSteps = steps.slice(1).filter((s, i) => s / steps[i] < 1.2).length;
  const invertedHeadings = hs.some(h => h.tagName === 'H1' && hs.some(o => o.tagName !== 'H1' && parseFloat(cs(o).fontSize) > parseFloat(cs(h).fontSize)));
  // Spacing grid + monotony
  const offGrid = spacing.filter(v => v % 4 !== 0).length / Math.max(spacing.length, 1);
  const spCounts = {}; spacing.forEach(v => spCounts[v] = (spCounts[v] || 0) + 1); const distinctSpacing = Object.keys(spCounts).length;
  // Copy and imagery tells
  const headText = hs.map(h => h.textContent.trim());
  const emojiHeads = headText.filter(t => /\p{Extended_Pictographic}/u.test(t)).length;
  const numbered = headText.filter(t => /^0[1-9]\b/.test(t)).length;
  const eyebrows = hs.filter(h => { const p = h.previousElementSibling; return p && vis(p) && cs(p).textTransform === 'uppercase' && p.textContent.trim().length < 40 && parseFloat(cs(p).fontSize) < 15; }).length;
  const brokenImgs = [...document.images].filter(i => vis(i) && i.complete && i.naturalWidth === 0).length;
  const badAlt = [...document.images].filter(i => vis(i) && /\.(png|jpe?g|webp|gif)$|^image by|^untitled|^img_?\d/i.test(i.alt || '')).length;
  const overused = famUsed.length && /^(inter|arial|helvetica|system-ui|-apple-system|roboto|open sans|geist)$/.test(famUsed[0][0]);

  // Rule findings (sources: IMP = Impeccable, DA = Design Auditor, AAD = avoid-ai-design, VCA = this skill)
  if (famUsed.length > 2) flag('font-count', 'warning', 'DA', `${famUsed.length} families carry text`);
  if (overused) flag('overused-font', 'tip', 'IMP/AAD', `primary face ${famUsed[0][0]}`);
  if (usedSizes.length > 7) flag('size-sprawl', 'warning', 'DA', `${usedSizes.length} font sizes`);
  if (nearDupSizes) flag('near-duplicate-sizes', 'warning', 'DA', `${nearDupSizes} size pairs within 2px`);
  if (flatSteps) flag('flat-type-hierarchy', 'warning', 'IMP', `${flatSteps} heading steps under 1.2:1`);
  if (invertedHeadings) flag('inverted-headings', 'critical', 'VCA', 'a lower heading is larger than the H1');
  if (h1s !== 1) flag('h1-count', 'critical', 'DA', `${h1s} H1 elements`);
  if (skipped) flag('skipped-heading', 'warning', 'IMP', `${skipped} skipped levels`);
  if (rhythmBad / Math.max(hs.length, 1) > 0.3) flag('heading-rhythm', 'warning', 'IMP', `${rhythmBad}/${hs.length} headings sit closer to the block above`);
  if (longLineWords / W > 0.1) flag('line-length', 'warning', 'IMP/DA', `${Math.round(100 * longLineWords / W)}% of words on lines over ~85 characters`);
  if (tightLeading / W > 0.1) flag('tight-leading', 'warning', 'IMP/DA', `${Math.round(100 * tightLeading / W)}% of body words under 1.3 line-height`);
  if (smallBody / W > 0.05) flag('small-body-text', 'critical', 'DA', `${Math.round(100 * smallBody / W)}% of body words under 14px`);
  if (tinyWords) flag('tiny-text', 'warning', 'IMP', `${tinyWords} words under 12px`);
  if (justified / W > 0.05) flag('justified-text', 'tip', 'IMP', 'justified body text');
  if (capsBody) flag('all-caps-body', 'warning', 'IMP', `${capsBody} words of uppercase body text`);
  if (lowContrast / W > 0.02) flag('low-contrast', 'blocker', 'DA/IMP', `${Math.round(100 * lowContrast / W)}% of words fail WCAG AA`);
  if (hueGroups.length > 2) flag('palette-size', 'warning', 'DA', `${hueGroups.length} chromatic hue families (aim 1 primary + 1 accent)`);
  if (chromaSpread > 3) flag('uneven-saturation', 'warning', 'VCA', `accent chroma varies ${chromaSpread.toFixed(1)}x`);
  if (overlaid.size > 2) flag('text-over-image', 'warning', 'IMP', `text placed over ${overlaid.size} different photos`);
  if (panels.size > 1) flag('panels-over-photos', 'warning', 'VCA', `${panels.size} boxed text panels floating over photos`);
  if (pastelShare > 0.08 && peakChroma < 0.15) flag('muted-pastel-palette', 'warning', 'VCA', `${Math.round(100 * pastelShare)}% of colour is low-chroma pastel with no strong accent (peak chroma ${peakChroma.toFixed(2)})`);
  const bodyFace = [...bodyFam].sort((a, b) => b[1] - a[1])[0]?.[0] || '';
  if (/display|cormorant|playfair|abril|bodoni|didot|lobster|pacifico|dancing|great vibes|bebas|anton|oswald|righteous|cinzel/.test(bodyFace)) flag('display-face-as-body', 'warning', 'VCA', `reading text set in a display face (${bodyFace})`);
  if (bodySize > 20) flag('oversized-body', 'warning', 'VCA', `main reading text set at ${bodySize}px`);
  if (centred > 0.3) flag('centred-text', 'warning', 'DA', `${Math.round(100 * centred)}% of words centred`);
  if (ctasFold > 2) flag('competing-ctas', 'warning', 'DA', `${ctasFold} calls to action above the fold`);
  if (radii.size > 4) flag('radius-sprawl', 'warning', 'DA', `${radii.size} corner radii in use`);
  if (shadows.size > 3) flag('shadow-sprawl', 'tip', 'DA', `${shadows.size} shadow styles`);
  if (distinctSpacing > 10) flag('spacing-sprawl', 'warning', 'VCA', `${distinctSpacing} distinct section spacing values`);
  if (brokenImgs) flag('broken-image', 'critical', 'IMP', `${brokenImgs} broken images`);
  if (badAlt) flag('filename-alt-text', 'blocker', 'DA', `${badAlt} images with file-name or credit alt text`);
  if (gradientText) flag('gradient-text', 'critical', 'AAD C6/IMP', `${gradientText} gradient-text elements`);
  if (purpleGrad) flag('purple-blue-gradient', 'critical', 'AAD C1', `${purpleGrad} purple-to-blue gradients`);
  if (sideTabs) flag('side-tab', 'warning', 'AAD K4/IMP', `${sideTabs} coloured side borders on cards`);
  if (glows) flag('dark-glow', 'tip', 'AAD C5/IMP', `${glows} coloured glow shadows`);
  if (cream) flag('cream-palette', 'warning', 'AAD SD1/IMP', 'cream ground with warm accent');
  if (eyebrows > 1) flag('kicker-above-heading', 'warning', 'AAD T5/IMP', `${eyebrows} uppercase eyebrows above headings`);
  if (numbered > 1) flag('numbered-section-labels', 'warning', 'AAD SD6/IMP', `${numbered} 01/02 style headings`);
  if (emojiHeads) flag('emoji-headings', 'warning', 'AAD I2', `${emojiHeads} headings with emoji`);
  if (bounce) flag('bounce-easing', 'tip', 'AAD M4/IMP', `${bounce} bounce/elastic easings`);

  // Top marks = better of the two top-scoring Webby winners (Obama Foundation, Soma Surf Therapy), measured Oct 2026.
  // 0% levels are fixed. Each measurement scores 0-100%; categories average their measurements; the index averages the categories.
  const TD = { fam: 2, sizes: 7, hues: 2, peak: 0.225, pastel: 0.01, centred: 0, spacing: 14, panels: 1, fold: 61, radii: 1 };
  const TM = { fam: 2, sizes: 8, hues: 1, peak: 0.225, pastel: 0, centred: 0.01, spacing: 13, panels: 0, fold: 83, radii: 2 };
  const POOR = { fam: 5, sizes: 14, hues: 5, peak: 0.05, pastel: 0.30, centred: 0.80, spacing: 40, panels: 12, fold: 200, radii: 10 };
  const T = VW < 768 ? TM : TD;
  const low = (k, v) => v <= T[k] ? 100 : Math.max(0, Math.round(100 * (POOR[k] - v) / (POOR[k] - T[k])));
  const peakPct = v => (v === 0 || v >= T.peak) ? 100 : Math.max(0, Math.round(100 * (v - POOR.peak) / (T.peak - POOR.peak)));
  const bodyPct = v => (v >= 15 && v <= 18) ? 100 : v < 15 ? Math.max(0, Math.round(100 * (1 - (15 - v) / 5))) : Math.max(0, Math.round(100 * (1 - (v - 18) / 8)));
  const avg = a => Math.round(a.reduce((x, y) => x + y, 0) / a.length);
  const metric = { fam: low('fam', famUsed.length), sizes: low('sizes', usedSizes.length), body: bodyPct(bodySize), hues: low('hues', hueGroups.length), peak: peakPct(peakChroma), pastel: low('pastel', pastelShare), centred: low('centred', centred), spacing: low('spacing', distinctSpacing), panels: low('panels', panels.size), fold: low('fold', wordsFold), radii: low('radii', radii.size) };
  const scores = { typography: avg([metric.fam, metric.sizes, metric.body]), colour: avg([metric.hues, metric.peak, metric.pastel]), layout: avg([metric.centred, metric.spacing, metric.panels, metric.fold, metric.radii]) };
  scores.cohesionIndex = avg([scores.typography, scores.colour, scores.layout]);
  const ded = { blocker: 12, critical: 8, warning: 4, tip: 1 };
  scores.craft = Math.max(0, 100 - findings.reduce((a, f) => a + ded[f.sev], 0));
  return {
    url: location.href, viewport: `${VW}x${VH}`,
    typography: { families: famUsed.map(([f, w]) => `${f} ${Math.round(100 * w / W)}%`), sizesPx: usedSizes, scaleRatioCV: +ratioCV.toFixed(2), weights: [...weights], headingSizes: headSizes, bodySize, bodyFamily: [...bodyFam].sort((a, b) => b[1] - a[1])[0]?.[0] },
    colour: { significant: sig.slice(0, 10).map(k => `${hex(k.c)} ${Math.round(100 * k.w / total)}%`), hueFamilies: hueGroups.length, chromaSpread: +chromaSpread.toFixed(2), lowContrastShare: +(lowContrast / W).toFixed(2), neutralShare: +neutralShare.toFixed(2), peakChroma: +peakChroma.toFixed(3), pastelShare: +pastelShare.toFixed(2) },
    alignment: { leftEdges, centredShare: +centred.toFixed(2) },
    clutter: { words, wordsAboveFold: wordsFold, textOverImage, photosWithText: overlaid.size, panelsOverPhotos: panels.size, ctasAboveFold: ctasFold, boxes, radii: radii.size, shadows: shadows.size, distinctSpacing, offGridShare: +offGrid.toFixed(2) },
    raw: { fam: famUsed.length, sizes: usedSizes.length, body: bodySize, hues: hueGroups.length, peak: +peakChroma.toFixed(3), pastel: +pastelShare.toFixed(2), centred: +centred.toFixed(2), spacing: distinctSpacing, panels: panels.size, fold: wordsFold, radii: radii.size },
    targets: T, metric, findings, scores
  };
})();
```
