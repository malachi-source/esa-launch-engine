# Task 11 — Re-Engagement Texts (SMS / YES Campaign)

> Short conversational texts that wake up cold/old leads and get a YES reply so a sales
> rep can follow up and close the ticket. Built to paste straight into GoHighLevel.

## Trigger
- Fires on the exact ✅ (U+2705, the green check) reacted on a Target Audience Profile
  in `#esa-master-viktor-chat`.
- Same approval that drives the other content tasks. Look-alike reactions (👍, ✔️, ☑️)
  do NOT count.

## Inputs (same three as every other task)
- **Voice Lock** from the Client Brain — every text must sound like the client, like a
  real person texting.
- **Event Info PDF** — event name, dates, city/venue, host, the transformation.
- **Approved Target Audience Profile** — pains, goals, and the exact words the audience
  uses.
- Any fact not present in the Event Info PDF becomes a `[[FILL: …]]` token. Never
  fabricate facts.

## What to generate
- A re-engagement SMS sequence of **[X] texts** (default 12; I'll give the number).
- Goal: a **YES reply** so a sales rep picks up the conversation and closes the ticket.
- Each text 1–3 lines, conversational, best-friend energy, written to one person.
  Use `{{contact.first_name}}` so it's paste-ready for GoHighLevel.

### 50/50 blend
- **Half** are quick YES-reply reactivation texts — curiosity, a question, a gut-check
  ("red, yellow, or green light?"), ending in a short YES-style question.
- **Half** are value / person-focused texts — speak to the lead's specific situation and
  how the event helps *them*.
- Rotate angles so it never feels repetitive. Mostly push for a YES reply first; only
  about 1 in 5 should drop a CTA. The full event name appears across the sequence.

### Internal tone reference (never named in the doc)
- Brunson (story hooks), Cardone (bold/direct), Gadzhi (real talk), Tai Lopez
  (curiosity gaps) — for energy only. The evergreen rule below overrides all of them.

## Hard rule — keep it 100% evergreen
- **No time pressure of any kind.** No countdowns, no "48 hours left," no
  "seats almost gone / selling out," no "early bird ends soon," no promos, no discounts,
  no bonuses-for-registering-today.
- The event date may appear as a plain fact, but nothing that expires.
- Every text is about the person and how the event helps them.
- `no_em_dashes = true` (periods or commas only).

## Compliance
- No income or health guarantees. Keep results conditional and proof-backed.
- Only reference scarcity if it is literally true (default: none).

## Output — editable Google Doc, client-ready / GoHighLevel-ready
- Title at top: `[Event Name] Text Message Campaign`, with a small subline: client name +
  event date/location.
- Numbered **Text #1 … Text #[X]**. Number only — no headlines or labels above each
  text, and never show the 50/50 split or the style names.
- Comfortable, readable text size. Formatted to copy-paste straight into GoHighLevel.
- Save to the client's Drive folder; post the link back in `#esa-master-viktor-chat`.

## Repo
- Path: `workflows/11-reengagement-texts/`
