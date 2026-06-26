# Task 10 — Reactivation Emails (re-engagement email sequence)

> Short, value-led emails that wake up cold/old leads and warm them toward the event.
> Built to drop straight into GoHighLevel with zero reformatting.

## Trigger
- Fires on the exact ✅ (U+2705, the green check) reacted on a Target Audience Profile
  in `#esa-master-viktor-chat`.
- Same approval that drives the other content tasks. Look-alike reactions (👍, ✔️, ☑️)
  do NOT count.

## Inputs (same three as every other task)
- **Voice Lock** from the Client Brain — every email must sound like the client.
- **Event Info PDF** (the event page) — event name, dates/location, the transformation,
  what they'll learn, the proof.
- **Approved Target Audience Profile** — pains, desires, and the exact words the
  audience uses.
- Any fact not present in the Event Info PDF becomes a `[[FILL: …]]` token. Never
  fabricate facts, dates, or proof.

## What to generate
- A re-engagement email sequence of **[X] emails** (default 14; I'll give the number).
- Each email is **short: under 7 sentences. Quick to read.**
- **Lead with value, not promotion.** Give a useful insight, mindset shift, or quick
  win first. The event is the soft next step, not the whole email.
- Conversational, one-to-one, in the client's voice. Use `{{contact.first_name}}` and any
  other GoHighLevel merge fields so it's paste-ready.
- Each email has a **subject line** + **body**. Keep subject lines short and curiosity
  or value driven (no spammy hype).
- End with a soft, single call to action that points toward the event. Avoid heavy
  urgency, scarcity, or discount-pushing. Keep it helpful, not salesy.

## Style
- Short. Plain. Human. Talk to one person.
- Mirror the audience's own language. No jargon, no corporate speak.
- **No em dashes.** Use periods or commas.

## Compliance
- No income or health guarantees. Keep results conditional and proof-backed.
- Only reference scarcity if it is literally true (default: none).

## Output — editable Google Doc, client-ready / GoHighLevel-ready
- Title at top: `[Event Name] Reactivation Emails`, with a small subline: client name +
  event date/location.
- Numbered **Email #1 … Email #[X]**, each showing its Subject line and Body.
- Comfortable, readable text size. Formatted to copy-paste straight into GoHighLevel
  with no reformatting needed.
- Save to the client's Drive folder; post the link back in `#esa-master-viktor-chat`.

## Formatting constraints — PAGINATION (do not violate)
- **One email per page.** Subject line and body for a single email always stay together
  on the same page. An email must never split across a page.
- Page 1 may carry the headline plus its email.
- Implementation: hard page break after each email, plus keep-together (keepLines +
  keepNext) on every line of an email as a safety net.

## Repo
- Path: `workflows/10-reactivation-emails/`
