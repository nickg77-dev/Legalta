---
name: gdoc-comment-analyser
description: Read and respond to comments in a Google Doc. Extracts all comments with their anchor location and generates suggested responses. Triggers on: "respond to comments in [doc]", "draft responses to Google Doc comments", "reply to these comments", "review doc comments", "comment responder", "respond to Paul's comments", or any variation of wanting to draft replies to Google Doc reviewer comments. Works from a Google Doc HTML export — NOT a screenshot or markdown file.
---

# Google Doc Comment Responder Skill

## Purpose
Extract all comments from a Google Doc (with their exact anchor location in the document), identify the latest comment per thread, and generate a suggested reply for each. Output is ready to copy-paste into the Google Doc comment thread.

## Critical: Input Format

### What works
HTML export (.zip or .html file) from Google Docs. This is the ONLY format that includes:
- All comment text in full (no truncation)
- Anchor location (which word or phrase is highlighted)
- Comment threads (multiple replies per anchor)
- Emoji reactions and timestamps

### What does NOT work
- Markdown download: comments are stripped entirely
- PDF export (standard File > Download > PDF): comments are stripped
- google_drive_fetch / Drive MCP: returns document body only, no comments
- Screenshot PDF: partial and unreliable — avoid

### How to export the HTML
1. Open the Google Doc in Chrome
2. File > Download > Web page (.html, zipped)
3. Upload the resulting .zip file to this chat (or the extracted .html file)

Note: With HTML export, there is no "show more" issue — all comment text is included in full, regardless of comment length.

## Workflow

### Step 1: Get document content
Use `google_drive_fetch` on the document ID to load the full document body. This provides context for generating accurate, document-aware responses. Extract the document ID from the URL:
https://docs.google.com/document/d/[DOCUMENT_ID]/edit

### Step 2: Check for HTML export
If the user has not yet uploaded the HTML export, instruct them:

"To read the comments, please export the doc as HTML:
File > Download > Web page (.html, zipped), then upload the .zip here."

If the user has already uploaded a .zip or .html file, proceed.

### Step 3: Parse the HTML export

Use Python (bash_tool) with BeautifulSoup to extract:
1. Comment text (from `<div class="c3">` elements at the bottom of the HTML)
2. Anchor context (the text immediately preceding each `<sup>` comment reference tag in the body)
3. Thread grouping (multiple `cmnt_refN` sup tags on the same span = same highlighted text)

```python
from bs4 import BeautifulSoup
import re, zipfile, os

# If .zip, extract first
if filename.endswith('.zip'):
    with zipfile.ZipFile(filename) as z:
        html_files = [f for f in z.namelist() if f.endswith('.html')]
        z.extract(html_files[0], '/tmp/gdoc/')
    html_path = f"/tmp/gdoc/{html_files[0]}"
else:
    html_path = filename

with open(html_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Extract comments
comment_divs = soup.find_all('div', class_='c3')
comments = {}
for div in comment_divs:
    anchor = div.find('a')
    if anchor and anchor.get('id', '').startswith('cmnt'):
        cmnt_id = anchor['id']
        full_text = div.get_text(separator=' ', strip=True)
        full_text = re.sub(r'^\[.\]', '', full_text).strip()
        comments[cmnt_id] = full_text

# Extract anchor contexts
def get_anchor_context(sup_tag):
    preceding_text = ''
    for sibling in sup_tag.previous_siblings:
        text = sibling.get_text() if hasattr(sibling, 'get_text') else str(sibling)
        preceding_text = text + preceding_text
        if len(preceding_text) > 100:
            break
    clean = re.sub(r'\s+', ' ', preceding_text).strip()
    return clean[-60:] if len(clean) > 60 else clean

anchor_contexts = {}
for sup in soup.find_all('sup'):
    link = sup.find('a', id=re.compile(r'cmnt_ref'))
    if link:
        href = link.get('href', '')
        cmnt_id = href.lstrip('#')
        anchor_contexts[cmnt_id] = get_anchor_context(sup)

# Group threads: consecutive cmnt IDs on same anchor = same thread
# The last cmnt in a group is the one to respond to
```

### Step 4: Identify thread structure
Multiple comment IDs on the same highlighted text form a thread. When a thread has multiple comments:
- Show the full thread only if context is needed
- The LATEST comment in the thread is the primary one to respond to
- Flag if earlier comments in the thread are unanswered questions from the same person

### Step 5: Generate output

For each comment (or thread), output:

```
---
Location: [searchable text fragment — last 5-10 words before the anchor, or section heading if the anchor is a heading. If only a single common word is highlighted, give the broader sentence fragment. Never give just one ambiguous word.]
Comment: [latest comment text in the thread. Full thread only if earlier comments are open questions]
Suggested response: [concise reply; match the tone/style of the commenter. Active voice. No filler.]
---
```

Output rules:
- Location should be a sentence fragment the user can Ctrl+F for. Never just "the" or another single ambiguous word.
- If the comment is from a senior stakeholder making a decision-level point: suggest a brief, direct acknowledgement + action commitment
- If the comment is a question: answer it or flag that it needs research first
- If the comment is a factual correction: accept or push back with evidence
- If the comment is a reaction emoji or "right, Nick?" style confirmation request: suggest a simple confirmation
- Keep suggested responses under 40 words unless the comment is multi-part

### Step 6: Present output
Present all comment responses in the chat, grouped in document order. After presenting, ask the user:
- Are there any comments they want to handle differently?
- Are there any where they need research before responding?
- Should any be marked as resolved without a reply?

## Output Example

```
---
Location: "...Why do we have a contracting model at all..."
Comment (Paul): Could you make this coherent. Remind readers why we have what may seem like an unconventional model. Important to know the trade-offs we'd be making if we went to a global EOR model.
Suggested response: Agreed — will add a short opening section framing the model's rationale and the trade-off vs EOR. Will include a cost comparison.
---

---
Location: "...Purpose..." [heading]
Comment (Paul): Suggest splitting this between "Facts" and "Analysis". Facts are mostly in your original documents (though need to be clearer). Analysis is currently a gap.
Suggested response: Will restructure into Facts and Analysis sections. Pulling the analysis layer through is the main gap — will prioritise that.
---
```

## Guardrails
- Never fabricate document content or comment text
- If the anchor context is ambiguous (very short or a common word), use the broader section heading instead
- If a comment is marked as resolved in the HTML (the `<div>` will be absent or have a resolved class), skip it
- Don't suggest responses that commit to timelines or actions without flagging them to the user for confirmation
- If a comment requires legal, financial, or HR-specific expertise to answer, flag this and suggest the user consults the relevant person before responding

