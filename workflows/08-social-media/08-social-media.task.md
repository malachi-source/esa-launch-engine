# Task 14 — Social Media Scripts (read-aloud video scripts)

> Spoken video scripts the client reads to camera to promote the event.
> These are SCRIPTS, not written ad copy. They are made to be read out loud.

## Trigger
- Fires on the exact ✅ (U+2705, the green check) reacted on a Target Audience Profile
  in `#esa-master-viktor-chat`.
- Same approval that drives the other content tasks. Look-alike reactions (👍, ✔️, ☑️)
  do NOT count.

## Inputs (same three as every other task)
- **Voice Lock** from the Client Brain — these come out of the client's own mouth on
  camera, so they must sound exactly like the client.
- **Event Info PDF** — event name, live-event vs. webinar, dates/location, the
  transformation, what attendees learn, the proof, and the registration link.
- **Approved Target Audience Profile** — pains, desires, and the exact words the
  audience uses.
- Any fact not present in the Event Info PDF becomes a `[[FILL: …]]` token. Never
  fabricate facts, prices, dates, or proof.

## What to generate
- **30 short-form video scripts** (Reels / TikTok / Shorts / talking-head) promoting
  the event.
- Each script is written to be **spoken, not read off a page**: short lines,
  contractions, natural pauses, talking to one person, hook landing in the first
  ~3 seconds. Roughly 15–45 seconds spoken.

### Every script follows the same 3-step structure
1. **Hook their pain** — a big, scroll-stopping opening line naming a pain the
   audience actually feels.
2. **Teach / give value** — one genuinely useful insight, tip, shift, or mini-framework
   they can use right now. Give before you ask.
3. **Invite to the event/webinar** — a clean invite to the event (or webinar). This is
   social media, so the call to action ALWAYS routes to **link in bio** (e.g. "tap the
   link in my bio to grab your ticket," "secure your ticket today, link in bio").
   NEVER say "link below" and NEVER paste a URL into the script. The registration link
   lives in the bio, not in the script.

### Variety
- Rotate hooks and value across all 30 so nothing repeats: question hooks, bold-claim
  hooks, myth-busts, common-mistake callouts, story teases, before/after framing, etc.
- Each value step teaches something different.

### Event name
- The full event name must appear in the **invite** of every script (not only implied).
- The CTA destination is always **link in bio**. No "link below," no pasted URLs.

## Style (read-aloud rules)
- Spoken word, not page copy. Short lines, natural pauses, no jargon, talk to one person.
- Sound like the client (Voice Lock wins over everything).
- **No em dashes.** Use periods or commas.

## Compliance
- No income or health guarantees. Keep results conditional and proof-backed.
- Only reference scarcity if it is literally true.

## Output — editable Google Doc, client-ready
- Title at top: `[Event Name] Social Media Scripts`, with a small subline under it:
  client name + event date/location.
- Numbered **Script #1 … Script #30**.
- Beat labels `[Hook] / [Value] / [Invite]` shown in a subtle, grayed style as a
  delivery guide. They are NOT read aloud.
- Comfortable, readable text size. Formatted to copy-paste and record straight from.
- Save to the client's Drive folder; post the link back in `#esa-master-viktor-chat`.

## Formatting constraints — PAGINATION (do not violate)
- **A script must NEVER break across a page.** Hook, Value, and Invite for a single
  script always stay together on the same page.
- **Two scripts per page. No more, no less**, and no script may extend past its page.
- **Page 1 may carry the headline plus its two scripts** — the title block does not
  reduce page 1 below two scripts.
- Implementation: hard page break after every 2nd script, plus keep-together on every
  paragraph within a script (keepLines + keepNext) as a safety net so a script can
  never split even if content runs long.

## Repo
- Path: `workflows/08-social-media/`
