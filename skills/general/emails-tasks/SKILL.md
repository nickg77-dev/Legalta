---
name: emails-tasks
description: "Gmail inbox triage skill. Reads your Gmail inbox for a specified time window, filters for emails that need a response or decision, and outputs a structured action-items list with sender, subject, what they need, deadline urgency, and a draft opener for each. Trigger when Ilia says \"/emails-tasks\", \"triage my inbox\", \"what needs my attention in Gmail\", \"check my emails\", or any variation of wanting to know what action items are waiting in his inbox. Also trigger when he specifies a time window like \"/emails-tasks 4h\" or \"emails-tasks 2h\"."
---

---
name: emails-tasks
description: >
  Gmail inbox triage skill. Reads your Gmail inbox for a specified time window,
  filters for emails that need a response or decision, and outputs a structured
  action-items list with sender, subject, what they need, deadline urgency, and
  a draft opener for each.

  Trigger when Ilia says "/emails-tasks", "triage my inbox", "what needs my
  attention in Gmail", "check my emails", or any variation of wanting to know
  what action items are waiting in his inbox. Also trigger when he specifies a
  time window like "/emails-tasks 4h" or "emails-tasks 2h".
---

# Emails Tasks — Inbox Triage

You're running an inbox triage for Ilia. The goal is to cut through everything that doesn't need him and surface only the things that do — with enough context that he can act immediately.

## How to invoke

The user will typically say `/emails-tasks` or `/emails-tasks [time window]`.

- If a time window is specified (e.g., `4h`, `2h`, `30m`), use that.
- If no time window is specified, default to **8 hours**.

## Step 1: Read the inbox

Use the Gmail tool to fetch all emails received within the specified time window. Cast a wide net — you want everything, including threads.

## Step 2: Classify each email

For each email, determine which category it falls into:

- **Response needed** — someone is waiting for Ilia to reply
- **Decision needed** — something requires his judgment or approval, but may not need a reply
- **No action** — FYI messages, newsletters, automated notifications, receipts, marketing

Ignore the "No action" category entirely for action items. They're noise.

The classification should be based on what the *sender actually needs from Ilia*, not just the surface content. A calendar invite from a colleague is a decision; a newsletter is noise even if it's interesting.

There is one exception to "No action" emails: **notable creator content**. Flag these separately (see Step 3b below) but never mix them with action items.

## Step 3: Output the action items

For every email that needs a response or decision, output an entry in this exact format:

---

**From:** [sender name and company/context if relevant]
**Subject:** [subject line]
**What they need:** [one sentence — be specific about what action is required]
**My deadline:** [Today / This week / No urgency]
**Draft opener:** [one sentence Ilia could use to start his reply]

---

A few notes on quality:

- "What they need" should name the actual ask, not just describe the email. "Approval on the Q2 budget draft" is better than "They sent a budget document."
- "My deadline" is about urgency from *their* perspective, not just when they said it's due. If someone's blocked on Ilia, that's Today even if they didn't say so.
- "Draft opener" is the hardest part of an email — starting it. Give Ilia one sentence that sounds like him: direct, warm, no fluff. Not "I hope this message finds you well." Something like "Thanks for flagging — here's where I land on this:" or "Let's do it — I'll need X from your end first."

## Step 3b: Surface notable creator content

After the action items (or in place of them if there are none), scan the inbox for emails from real human creators — newsletter writers, collaborators, people Ilia follows. These are not tasks, but they're worth flagging if they're substantive.

**Include if:** a real person published something that's relevant to Ilia's work (AI tools, newsletters, BI, dev), asked for community feedback, or did something notable like recommending Prosper.

**Skip if:** it's a platform notification (automated subscriber counts, Stripe payouts), pure marketing, or content with no connection to his interests.

Output this section only if there's at least one item worth mentioning. Use this format:

---

**Worth a look**

- **[Creator / Publication]** — "[Subject line or description]" — one sentence on why it's relevant or what it's about.
- ...

---

Keep the list tight — 2–4 items max. If nothing qualifies, omit this section entirely. Don't pad it.

## Step 4: End with a quick summary

After everything, add one line:

**[N] items need your attention** — [response needed: X, decisions: Y]

If there were no action items but there was a "Worth a look" section, say:

**Inbox is clear** — nothing needs a reply, but a few things worth reading above.

That's it. No preamble, no explanation of what you did. Just the action items, the worth-a-look section if relevant, and the summary line.