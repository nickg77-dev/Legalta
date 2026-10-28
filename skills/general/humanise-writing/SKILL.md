---
name: humanise-writing
description: >
  Nick Graham's prose voice layer. Applies to any text Nick will put his name to:
  covering letters, CV bullets, emails, LinkedIn posts, client proposals, slide deck
  copy, website copy, funding applications. Fires as an additive layer alongside format
  skills (docx, pptx, job-application-writer, seefar-brand) and on its own for editing
  requests. ALWAYS use this skill when generating or editing prose Nick will send,
  publish, or present - even when he hasn't explicitly asked for humanising. Also
  triggers on "humanise this," "de-AI this," "does this sound like AI," "clean this up,"
  "make this sound like me," "make this less ChatGPT-y." Do NOT use this skill for
  grading or reviewing other people's writing on Feather or Ethos content-grading tasks -
  those belong to ai-slop-writing-check and ai-slop-professional-writing.
---

# Humanise Writing

Edit or draft prose so it reads like Nick wrote it, not like an LLM's safest average
sentence.

This is a voice layer, not a grading tool. There is no verdict, no score, no BORDERLINE -
just a strip pass, a judgement pass, and a rewrite. The Ethos grading skills in this
project share some underlying detection logic with this one but exist for a different job
(scoring other people's writing on Feather); keep them separate and never borrow their
output format (verdicts, scores, MAJOR tags) here.

Nick's userPreferences already ban em dashes, correctio constructions ("X isn't A, it's
B"), and a named word list (dive deep, delve, embrace, burning question, unlock,
underscore, navigate). This skill does not restate those - they apply regardless. Where
anything below conflicts with userPreferences, userPreferences wins.

---

## Step 1: Pick the mode

Decide before editing. If genuinely ambiguous, ask once - don't guess between formal and
conversational, the wrong register is worse than a clarifying question.

**Formal** - CV, covering letter, funding bid, client proposal, anything to a regulator,
funder, or hiring panel. Personality section (below) is OFF. No first-person asides, no
half-formed thoughts, no acknowledging mixed feelings. Plain, precise, and complete.

**Conversational** - email, LinkedIn post, blog, internal note, anything informal. Personality
section is ON.

**Deck** - any pptx content or slide copy. Personality OFF. Read `references/deck-copy.md`
before drafting or editing - it holds the element-by-element rules (title, subtitle,
kicker, card body, label, footer) and an enforced sentence budget for card body text.
Deck mode always runs alongside whatever format skill produced the deck (pptx,
seefar-brand, design skills) - this skill owns the words, not the layout.

## Step 2: Strip pass

Remove the mechanical tells first.

- Em dashes, semicolons used for rhythm, ASCII dot or bar separators, arrows as
  connectors. (Semicolons and arrows are fine when doing real structural work - a genuine
  list or a real logical connector - not when manufacturing punchiness.)
- Correctio constructions: "It's not X, it's Y," "not just X, but Y," "no X, no Y, just Z."
- Passive voice: "The proposal was approved by the team" -> "The team approved the
  proposal."
- Imperative headings or titles standing in for a description ("Screen the energy credit,
  not the headline retail tariff" as a title). Imperatives are correct inside an explicit
  action list ("Recommended actions," "Next steps") - don't strip those.
- Rule-of-three lists ("efficient, effective, and reliable"). Two items or four items are
  fine; three every time is the tell.
- Rhetorical transition questions: "The catch?" "So what does this mean?"
- "Let's" openers, fake-naming ("The 5-Step Method" for an idea with no real name),
  self-narration ("this underscores," "the key takeaway is").
- Check the twenty highest-frequency banned words and phrases below. For a full scrub, or
  when editing blog/social copy where 2020s chatbot voice shows up most, read
  `references/cliche-patterns.md` (40 patterns from Simon Willison's cliché highlighter)
  and `references/banned-list.md` (the fuller word and phrase list).

**Core word list** (swap for the plain alternative): leverage -> use; delve -> look at;
underscore -> show; foster -> build; navigate (figurative) -> handle; unlock (figurative)
-> enable; streamline -> simplify; utilize -> use; facilitate -> help; robust, seamless,
comprehensive, cutting-edge, transformative, pivotal, vibrant, groundbreaking -> cut or
replace with the specific fact.

**Core phrase list** (delete outright): "it's worth noting that," "at the end of the day,"
"in today's rapidly evolving landscape," "needless to say," "the reality is," "here's why
this matters," "stands out as," "plays a crucial role," "despite these challenges,"
"experts argue" (unless the expert is named).

## Step 3: Judgement pass - the five-lens check

Mechanical stripping catches known patterns. This pass catches everything else: could this
sentence be rewritten significantly better? Read `references/five-lens.md` for the full
version with worked examples. The five lenses, in brief:

1. **Awkward** - strained or unnatural phrasing a person wouldn't actually use.
2. **Excessive** - reaches for a grander register than the point needs.
3. **Vague** - the reader can't tell what's actually being claimed.
4. **Unnecessary** - deleting it costs the sentence nothing.
5. **Illogical** - the words don't hold together (verb/object mismatch, broken
   comparison).

Also run: is this comparative missing its other side ("grew faster" - than what?), and is
this sentence carrying too much in one clause (five-lens.md has the density rules)?

Unfamiliar or technical terms are not, by themselves, a problem - don't flag genuine
domain terminology just because it sounds specialist. Flag it only when a plainer word
means the same thing, or the term has no clear referent.

## Step 4: Add personality (conversational mode only - skip entirely in formal or deck mode)

Clean text with the AI patterns stripped but no voice added still reads like a flat press
release. After stripping:

- Have opinions. React to what you're writing about, don't just list pros and cons.
- Vary rhythm - mix short sentences with longer ones.
- Use "I" when it's natural. "I keep coming back to..." reads like a person thinking.
- Be specific rather than abstractly evaluative: not "this is concerning" but what,
  exactly, is concerning and why.
- Leave a little imperfection. An aside or an honest "I'm not sure" beats a suspiciously
  clean five-paragraph structure.
- Acknowledge mixed feelings where they're genuinely there, rather than forcing a single
  clean verdict.

## Step 5: Self-check before delivering

Scan the output for: em dash, semicolon doing rhythm-work, "—", "let's," "leverage,"
"unlock," "underscore," any "it's not X, it's Y" shape, three short sentences in a row, a
rule-of-three list, a title-cased heading, curly quotes. Fix anything found.

In deck mode, also check every card body sentence against the enforced budget in
`references/deck-copy.md` (one clause, roughly fifteen to twenty words, no more than two
or three enumerated items, no stacked hyphenated modifiers) - rewrite over-budget
sentences rather than flagging them.

## Step 6: Deliver

Hand back the text. No preamble ("here's the rewrite!"). If a comparison or explanation of
changes was asked for, give it after the text, not before.

---

## Style mechanics (always, regardless of mode)

- Straight quotes, not curly.
- Sentence case in headings: "How to write better emails," not "How To Write Better
  Emails."
- No boldface abuse - don't bold a key term in every sentence.
- No synonym cycling - if it's "the platform" in sentence one, don't call it "the system"
  in sentence two for variety's sake. Pick one term and keep it.
- No false ranges - cut "from X to Y" constructions where X and Y aren't a real spectrum
  ("from hobbyist experiments to enterprise rollouts").
- British spelling throughout (-ise, colour, organisation) per userPreferences.

---

## Example

**Before (AI):**

DataSync is a cutting-edge, AI-powered data integration platform that seamlessly connects
your entire tech stack. Our innovative solution leverages advanced machine learning to
streamline workflows, enhance productivity, and drive transformative results. It's not
just a tool. It's not even a platform. It's a paradigm shift in how enterprises harness
the power of their data.

**After (human, conversational mode):**

DataSync moves data between your apps without you having to think about it. Connect
Salesforce and HubSpot once, set a few rules, and it keeps them in sync. When a deal
closes in one, the other knows within a few minutes. Most customers are mid-size sales
teams tired of copying and pasting between tabs. It costs $200/month and takes about an
hour to set up.

What changed: the escalating "it's not X, it's not even Y, it's Z" gone, the
leverage/streamline/enhance verb stack gone, the rule-of-three adjective run gone. What
got added: a concrete price, a concrete setup time, a real description of the customer.

---

## Reference files

- `references/cliche-patterns.md` - full 40-pattern list from Simon Willison's cliché
  highlighter, refreshed quarterly. Read for a thorough scrub or when editing blog/social
  copy.
- `references/five-lens.md` - the five judgement categories in full, with worked
  before/after pairs and the density and comparative rules.
- `references/deck-copy.md` - element-by-element rules for slide copy (title, subtitle,
  kicker, card body, label, footer, source line) and the enforced card body sentence
  budget. Read whenever the output is a deck.
- `references/banned-list.md` - the fuller word, phrase, transition, and emoji list
  beyond the core list in Step 2.
