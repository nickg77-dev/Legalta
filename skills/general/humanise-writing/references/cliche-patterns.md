# LLM cliché patterns (Simon Willison's highlighter)

Source: https://tools.simonwillison.net/llm-cliche-highlighter
Extraction command (re-run this at each quarterly check):
curl -sL https://raw.githubusercontent.com/simonw/tools/main/llm-cliche-highlighter.html | sed -n '/^const patterns = \[/,/^];/p'

Pattern count at last check: 40 (26 original + 14 adapted from Wikipedia's "Signs of AI
writing" guide: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
Last checked: 2026-09-03
Next check due: 2026-12-03

Refresh procedure: re-run the curl command above, diff the pattern list against this file
(names and regex intent, not exact code), add anything new, remove anything the tool has
dropped, update the two dates above. Takes a couple of minutes.

Read this file when: doing a thorough top-to-bottom scrub, editing blog or social copy
where 2020s chatbot voice is most likely to show up, or when SKILL.md's shorter core list
hasn't caught something that still reads as AI-generated.

---

## Original patterns (not in Wikipedia's list)

These are the ones most likely to be missing from an older or more conventional banned-word
list, because they're syntactic shapes rather than single words.

**"No X, no Y" chains.** Two or more "no ..." items in a row. "No fluff, no filler, no
jargon." Cut to one plain sentence.

**"That's the whole point/game/thing."** Gesturing at significance instead of stating it.
Say what the point actually is.

**"Did not X, did not Y" chains.** Same shape as the "no" chain, negated verbs instead.

**"Don't VERB it ... VERB it."** "Don't call it a bug. Call it a feature." Say the thing
once, plainly.

**"Sit with that."** "Sit with the discomfort for a moment." Therapist-voiced filler with
nothing beneath it. Cut.

**"You already know [the answer/what/how/why]."** Faux-intimate stalling. Just say the
thing the reader supposedly already knows.

**"Is the entire point/game/business model."** Inflated singular-cause claims. Usually the
cause is one of several; say which one and why.

**"The entire [point/game] is..."** Flipped twin of the above.

**"Is real, and/not..."** "The risk is real, and it's growing." Vague intensifier standing
in for a specific claim.

**"The punchline is..."** Stage-managed reveal. Just state the fact.

**"Worth naming [that]..."** "That loss is real and it's worth naming." Announces
significance rather than showing it.

**"That's not nothing."** Hedge dressed as insight. Say what it actually is.

**"Is the whole point/trick/pitch/idea."** Generalised version of "that's the whole..." to
subjects other than that/this.

**Echoing sentence runs.** Consecutive sentences built on the same skeleton: "A shopping
cart is an object in the system. A chat room is an object in the system." Vary the
structure or cut the repetition.

**Performative honesty.** "I won't pretend," "let's be honest," "to be clear," sentence-
opening "Honestly," or "Look,". Sincerity announced rather than demonstrated. If you mean
it, just say the thing; the announcement is doing no work.

**"That's the part [that]..."** "That's the part a counter can't reach." "My favourite
part of..." Gestures at a favoured detail instead of naming it.

**"The only X I trust/need/want."** Narrowing superlative reveal used as a rhetorical
device rather than an actual claim.

**"Don't take my word for it."** Stock invitation to verify. Either link the source or cut
the line.

**"Turns out..."** Casual-revelation opener almost always bolted onto a tidy, too-neat
conclusion.

**"Fits in your head" / "batteries included" / "it just works" / "zero config" / "sane
defaults."** Dev-blog boilerplate for simplicity. Fine occasionally in genuinely technical
writing about tooling; a tell when used to describe something that isn't software.

**Stacked rhetorical questions.** "Do I know how it works? Where it breaks? Which corners
it cut?" Two or more fired in a row. Ask one question you'd actually ask, or none.

**Repeated sentence openers.** Three or more consecutive sentences starting on the same
word: "Maybe nobody needed it. Maybe it introduced... Maybe a small convenience..." Vary
openers.

**Colon into a triple.** A colon opening onto three comma-separated items: "separate ports,
processes, and local state." The single most common shape AI prose uses to sound concrete
without being concrete. Flag when it isn't a genuine, necessary list.

**"Here's the twist/thing/catch/kicker/rub."** Stage-managed reveal opener. State the fact
without the announcement.

**"X is dead" / "long live X."** Obituary-headline framing. Usually overstates a real but
partial shift.

**"That's why X mattered."** Retroactively assigns significance rather than showing it at
the time.

**Stranded auxiliary contrast.** A clause landing on a bare auxiliary for the reversal:
"The tool died; the data didn't." "Reading mostly passed. Writing didn't." Punchy but
mannered; use plain contrast instead.

---

## Patterns adapted from Wikipedia's "Signs of AI writing"

**AI vocabulary words.** delve, tapestry, meticulous(ly), pivotal, intricate(ly),
intricacies, interplay, underscore, garner, bolster, vibrant, bustling, multifaceted,
seamless(ly), commendable, ever-evolving. One hit can be coincidence; several is a tell.
(Overlaps SKILL.md's core word list and the fuller version in banned-list.md.)

**"Not just X, but Y."** Negative parallelism: "not just X, but (also) Y," "not only...
but...," and "it's not X, it's Y." Already a hard rule in SKILL.md; this is the same
pattern under the tool's name.

**"It's important to note."** "It's worth noting," "it should be noted," plus "worth
pausing/considering/asking." Didactic hedging that adds nothing.

**"Stands as a testament."** "Serves as a testament/reminder," "is a testament to."
Inflates significance instead of saying what happened.

**"Plays a crucial role."** "Plays a pivotal/vital/key/significant/central/critical role
in..." Say what the thing actually does.

**"Ever-evolving landscape."** "The changing/shifting landscape," "in today's fast-paced/
digital/modern world." Scene-setting boilerplate; delete and open with the actual point.

**"Experts argue."** Vague attribution: "some critics have noted," "observers suggest,"
"industry reports indicate." Name the source or cut the claim.

**"Despite these challenges."** The boilerplate challenges-and-outlook formula: "faces
several challenges," "challenges remain," "remains to be seen," "time will tell."

**Participle sentence tails.** ", highlighting/underscoring/showcasing/reflecting/
demonstrating the..." bolted onto a sentence end as a shortcut to sounding analytical.

**Promotional boilerplate.** "nestled in," "in the heart of," "rich cultural heritage,"
"hidden gem," "must-visit," "breathtaking," "boasts a," "stunning views." Travel-brochure
tone. Already covered in SKILL.md's promotional-tone section; this is the same list.

**Chatbot leftovers.** "as an AI language model," "as of my last update," "knowledge
cutoff," plus literal markup debris (contentReference, oaicite, turn0search, utm_source=).
Rare in finished prose but worth a final scan on anything pasted from a chat session.
