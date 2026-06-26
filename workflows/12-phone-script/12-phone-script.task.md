# Task 12 — Phone Sales Script

> A complete, phone-ready closing script the sales reps read off of live to turn event
> leads into paid ticket holders. This is an INTERNAL rep tool, not client-facing copy.

## Trigger
- Fires on the exact ✅ (U+2705, the green check) reacted on a Target Audience Profile
  in `#esa-master-viktor-chat`.
- Same approval that drives the other content tasks. Look-alike reactions (👍, ✔️, ☑️)
  do NOT count.

## Inputs (same three as every other task)
- **Voice Lock** from the Client Brain — the script should sound like our client and our
  reps, not a corporate phone tree.
- **Event Info PDF** — event name, dates/location, host, the one-line promise, the unique
  mechanism, the proof, **ticket tiers with prices and benefits**, **payment methods
  accepted**, and **what happens after purchase** (fulfillment).
- **Approved Target Audience Profile** — goals, barriers, the dream payout, and the exact
  words the audience uses.
- Any fact not present in the Event Info PDF becomes a `[[FILL: …]]` token. Never
  fabricate prices, payment methods, fulfillment, or proof — these appear in the close
  and payment sections, so guessing is not acceptable.

## Script structure (write in this exact order)

### 1) Opener — Make Them Laugh
This is our mastered opener. Use it **word-for-word**. The only thing that changes is the
event name (and the rep / host / dates / promise tokens). Do not rewrite, embellish, or
add jokes. There are exactly **two** openers:

**Opener 1 — New Opt-In**
> "Hi, is this {{first_name}}? Amazing.
> This is {{rep_name}} with [Event Name]. I saw you checking out tickets for [Dates, Location].
> You're planning on being there… right?"

**Opener 2 — Warm / Old Leads**
> "This is {{rep_name}} with [Event Name]. [Host] asked me to personally invite you.
> You're looking to [event promise], correct?"

`[If yes, jump to the Close (Section 5). If no or maybe, keep going.]`

### 2) Anchor Question
"Why'd you check out the event?" Mirror their words, label the real reason. That reason
anchors the whole call.

### 3) Discovery — As-Is / Should-Be / Barrier / Payout
A few short questions for each: where they are now, where they want to be, what's blocking
them, and what the payout means for them and their family.

### 4) Event Frame
Bridge their own answers to the event ("That's exactly why [host] built this…").

### 5) Tiered Close
Present the tiers cleanly and ask which one feels best.

### 6) Objection Handling — Agree → Align → Advance
Modular lines for: Price, Will-it-work, Time/Travel, Spouse/Partner,
Been-to-events-before, Not-ready, plus 1–10 decision nudges. Every rebuttal loops back to
their stated goal.

### 7) Payment Capture
The verbatim lines to confirm details and take the card.

### 8) Confirmation / Future Pace
Congratulate, tell them what lands in their inbox, paint the after.

## Style (read-aloud rules)
- Speak to one person, use "you." Short lines, natural pauses, no jargon.
- **No em dashes.** Use periods or commas.
- Validate first, then advance. Use "And" to keep momentum after an objection.
- Build identity (leader, winner, the one who decides).
- Always loop back to their goal, barrier, and payout.

## Compliance
- No income or health guarantees. Keep results conditional and proof-backed.
- Only reference scarcity if it is literally true.

## Output — editable Google Doc, rep-ready
- Title at top: `[Event Name] Phone Sales Script`, with a small subline: client name +
  event date/location.
- **Keep the structure visible** — numbered sections, the objection labels, and the
  bracketed stage directions ("[Listen. Mirror their reason.]"). The rep needs them.
  Set stage directions in a lighter style so they're clearly not spoken.
- Comfortable, readable text size.
- Save to the client's Drive folder; post the link back in `#esa-master-viktor-chat`.

## Repo
- Path: `workflows/12-phone-script/`
