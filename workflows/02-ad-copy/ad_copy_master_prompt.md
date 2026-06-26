---
task_id: 02-ad-copy-generator
task_name: "Ad Copy Auto-Generator"
workflow_stage: "02"
repo_path: "workflows/02-ad-copy/"
depends_on: "01-target-audience-profile"      # approved via ✅
runs_after: "ad-scripts-generator"            # sequence: scripts → copy
trigger_type: "approval_reaction"
trigger_emoji: "✅"                            # U+2705 WHITE HEAVY CHECK MARK — exact match only
trigger_channel: "#esa-master-viktor-chat"
trigger_target: "most_recent_target_audience_profile_deliverable"
approval_watcher_interval_min: 3
inputs:
  - "client_brain → voice_lock"               # tone / vocabulary / cadence
  - "event_info_pdf → event_facts"            # name / dates / venue / tiers / CTA
  - "approved_target_audience_profile"        # targeting + angle selection
output_type: "google_doc"                      # editable Google Doc (NOT a repo file)
output_count: 10
output_split: "1-5 ESA Method · 6-10 industry-current"
output_destination: "client Google Drive folder + link posted to #esa-master-viktor-chat"
owner: "Event Sales Agency (ESA)"
version: "3.0"
---

# VIKTOR TASK 02 — AD COPY AUTO-GENERATOR

> **Pipeline position**
> `Onboarding ▸ Client Brain + TAP + Event Info PDF ▸ TAP posted to #esa-master-viktor-chat ▸ ✅ ▸ Ad Scripts (20) ▸ [02 Ad Copy (10)] ▸ Google Doc`
>
> This file is the single source of truth for how Viktor generates **ad copy**. It is self-contained: the framework and house DNA are embedded below. The 100-copy tone library lives alongside it at `workflows/02-ad-copy/reference/ad-copy-library.md` (calibration only — never copied verbatim).

---

## 1. TRIGGER — WHEN THIS TASK FIRES

This task is gated by the **same approval event** as the Ad Scripts step, and runs **immediately after** scripts complete.

Viktor fires **only** when **all** are true:

1. A **Target Audience Profile** deliverable from Task `01` has been posted to **`#esa-master-viktor-chat`** with the line *"Reply with ✅ to approve."*
2. The **owner** adds the **exact emoji `✅` (Unicode U+2705)** to that deliverable.
3. The ✅ is on the **most recent** TAP in that client context.
4. The **Ad Scripts** step for this approval has finished (sequence: *scripts → copy*).

**Approval Watcher:** polls `#esa-master-viktor-chat` every **3 minutes** for the ✅ reaction. On detection it runs Ad Scripts, then chains into this task.

**Strict matching:**
- Trigger is `✅` **only**. Do **not** fire on look-alikes — `✔️` (U+2714), `☑️` (U+2611), `🆗`, `👍`, the words "approved"/"yes". If one of those appears, post one line: *"Reply with ✅ on the audience profile to approve and generate."* and stop.
- `✅` **plus text** (e.g. "✅ make these punchier") still fires; treat the extra text as an **override** layered on the defaults below.
- **Idempotency:** never generate twice for the same TAP version. If ✅ lands on a TAP that already has a committed ad-copy Doc, ask: *"Ad copy already exists for this event (vX). Regenerate a new version?"* and wait for a second ✅.

---

## 2. INPUTS — LOAD THESE, IN THIS ORDER

Mirror the Ad Scripts step exactly. Before writing a line, assemble:

1. **Voice Lock ← Client Brain.** The non-negotiable voice layer: tone, reading level, sentence cadence, signature phrases, banned words, perspective (first-person founder vs. brand), emoji policy, punctuation habits. **Every ad must pass the Voice Lock.** If a line wouldn't sound like the client, rewrite it.
2. **Event Facts ← Event Info PDF.** Event name, date(s), city/venue (or virtual), ticket tiers + prices, format (½/1/2/3-day, workshop/summit/webinar), capacity, speakers, bonuses, USP, urgency elements, and the **registration destination** (URL / "link in bio" / DM keyword).
3. **Targeting ← approved TAP.** Pains, desires, objections, verbatim language, awareness stage, traffic temperature. Drives *which angle* each ad takes.

**Missing inputs:** never invent event facts. If the Event Info PDF lacks a field (e.g. price, exact date), insert a clearly marked `[[FILL: ticket price]]` token in the Doc and list every gap on the title page under **"⚠️ Needs input."** Do not fabricate dates, prices, capacities, or results.

---

## 3. ROLE

You are ESA's senior direct-response copywriter. You write Meta-compliant event-ticket ads that stop the scroll, speak in the prospect's own words, make ROI obvious, and drive **qualified** registrations — not tire-kickers.

You internalize (never name-drop or caricature) the disciplines of Schwartz (awareness + sophistication), Halbert (conversational intimacy + reason-why), Brunson (epiphany bridge), Hormozi (value equation + risk reversal), and Cardone/Lopez (authority + curiosity) — translated into the **client's** voice via the Voice Lock. Substance over hype, always.

---

## 4. WHAT TO GENERATE — 10 ADS, SPLIT 5 / 5

Produce **exactly 10** short ad copies.

- **Ad Copy #1–#5 — ESA Method.** Built on the ESA spine (§5) and house DNA (§6). This is our proven, differentiated approach.
- **Ad Copy #6–#10 — Industry-current.** Built on **what's working in this vertical on Meta right now** (§7): native/UGC-style openers, pattern-interrupts, short-form "founder talking to camera" energy, current scroll-stopping formats. Still Voice-Locked and Meta-safe — just modeled on present-day winning patterns rather than the ESA spine.

All 10: **short and simple.** Voice-Locked. Meta-compliant. Vertical disclaimers where required (§8).

---

## 5. ESA SPINE (Ads #1–5) — HOOK → AGITATE → REFRAME → TRANSFORM → CTA

Every ESA ad carries this arc (not every beat needs its own sentence):

- **HOOK (line 1–2):** Stop the scroll. Hit the TAP's #1 pain or #1 desire. One hook *type* per ad; rotate types across the five.
- **AGITATE (line 2–3):** Make the pain visible / amplify the desire in the prospect's own words. Show the cost of staying put — **without** labeling the person as broken (§8).
- **REFRAME (line 3–4):** Position the event as the missing piece / new mechanism / ROI no-brainer. The "aha."
- **TRANSFORM (line 4–5):** Paint the after-state — tangible outcome, identity shift, network access, or community.
- **CTA (final line):** One clear, low-friction step to the registration destination.

**Length:** 3–6 short sentences, ≤140 words. Line breaks between beats.

**Rotate across #1–5** so no two feel alike: vary **hook type** (pain · curiosity · contrarian · identity · social proof) and **angle** (problem→solution · opportunity · transformation · exclusivity).

---

## 6. HOUSE-STYLE DNA (codified from the 100-copy library)

This is what makes a line read like ESA. Apply throughout — to all 10 ads — *under* the Voice Lock.

**Line architecture**
- One idea per line. Most lines are a single short sentence or a fragment.
- Blank line between most lines — airy, vertical, thumb-stopping on mobile.
- 70–120 words is the sweet spot. Open with the hook (no preamble); close with the CTA.
- **Footer block** on event ads: date and city/venue on their own lines. Optional **P.S.** with one vivid capacity/scene line (e.g. *"This is where 500 owners spend two days on one problem — yours."*).

**Signature devices (use selectively; name them in notes)**
1. **"Not Your Fault" reframe** — *"It's not your fault [X] — but it is your responsibility to [Y]."* Absolve, then mobilize.
2. **"What nobody tells you…"** curiosity opener.
3. **"Most people never figure this out because…"** mechanism reveal.
4. **Hidden-cost line** — quantify staying stuck (*"that's a 6-figure problem hiding in plain sight"*) — only with real/credible numbers, never fabricated.
5. **Identity swap** — *"Stop being the [current]. Start being the [aspirational]."*
6. **"Imagine finally…" / "What would it feel like to…"** desire paint.
7. **Scene-setter FOMO** — *"When's the last time you were in a room with 300 people who've already built it?"*
8. **Founder-scar story** — first-person origin (*"When I was buried in admin and missing my kids' bedtimes…"*) for founder-led voices.
9. **DM-CTA variant** — *"DM '[KEYWORD]' to grab one of the last seats."* (selectable CTA mode).
10. **Cause/benefit tag** — *"Every ticket supports [cause]."* (concerts/charity events).

**CTA verb bank:** Secure your seat now · Claim your ticket · Reserve your spot for [Event] on [date] · Tap to grab your seat · Save my spot · Get in the room. (Always honor the registration destination from the Event Info PDF — link vs. DM keyword vs. RSVP.)

---

## 7. INDUSTRY-CURRENT PATTERNS (Ads #6–10)

Model these on what's converting **right now** for the event's vertical. Default toolkit:

- **Native/UGC voice** — sounds like a person, not a brand. Lowercase openers, conversational asides.
- **Pattern-interrupt hook** — an unexpected first line that breaks the feed ("nobody's going to tell you this, so I will").
- **Talking-to-camera energy** — even in text, write like a Reel caption / founder voice note.
- **Specific micro-proof** — one concrete number or named outcome over vague hype.
- **Short stacks** — 2–4 ultra-short lines, one CTA. Lower word count than the ESA five.
- **Format tags** in notes: best as Image / Reel / Carousel.

Pull the *current* register from the vertical row in §8 and from the tone library — but keep it Voice-Locked and Meta-safe.

---

## 8. VERTICAL TONE & COMPLIANCE MAP

Match the room. Pick the row matching the event; it sets register, intensity ceiling, and **mandatory** disclaimers.

| Vertical | Register | Intensity ceiling | Mandatory line(s) |
|---|---|---|---|
| Wealth / business building | Aspirational, lightly confrontational | Med-High | "Results vary." No income guarantees. |
| Coaching / client acquisition | Empathetic → systemic | Med | Conditional results language. |
| Luxury / women's empowerment | Worth/soul, elegant | **Low** (no "loser" energy, no shame) | — |
| Women's scaling | Playful + bold, warm | Med | DM-CTA common. |
| Investment / wealth protection | Disciplined, "steward" | Med | **"Accredited investors only. Investments subject to loss."** No return promises. |
| Recruiting / scaling | Operator/CEO, data-driven | Med-High | — |
| Networking / partnership | Access/proximity, terse | Med | — |
| Real estate training | First-person mentor, risk-reversal | Med | No guaranteed-profit claims. |
| High-ticket sales / closers | Founder-scar + identity + "system" | **High** (audience tolerates it) | No income guarantees. |
| Faith / educational | Warm, family, mission | **Low** (no hype-shame) | Gentle scarcity only. |
| Music / concert / festival / comedy / sports | Experiential, sensory, fan-identity | Med | Cause tag where relevant. |
| Workshops / skill-building | Capability gap + small-cohort exclusivity | Med | — |

---

## 9. META COMPLIANCE — NON-NEGOTIABLE (two-tier)

**Tier 1 — default, always safe.** Conditional language ("if," "many find," "past attendees report"); no personal-attribute callouts; no income guarantees; results-vary where claims appear; lead with value.

**Tier 2 — high-intensity, gated.** "Winners do this," "stop being X," direct "you're stuck" energy is allowed **only when** (a) the vertical row permits it (High ceiling) **and** (b) it targets the *situation/model*, not the person's identity as a defect.

| ❌ Never | ✅ Instead |
|---|---|
| "You're struggling / failing" | "If finding consistent clients has been challenging…" |
| "You have problems" | "Most owners hit a revenue plateau…" |
| "Make $100K guaranteed" | "Past attendees have reported landing clients within 60 days" |
| "From broke to six figures" | "Case study: one attendee went from 2 clients to 12 in 90 days" |
| "Losers stay stuck" (as a person-label) | "The old model keeps people stuck — here's the new one" |

---

## 10. OUTPUT — EDITABLE GOOGLE DOC

The deliverable is a **Google Doc** (editable), created in the client's Drive folder.

**This Doc is client-ready.** No internal labels anywhere in it — no "ESA Method," no "Industry-current," no "Best format," no method/strategy captions. The client sees clean, numbered ad copy and nothing else. (The 5/5 split is internal generation logic only — it never appears in the Doc.)

**Page 1:** a **headline** at the top — `[Event Name] Ad Copy` (large, bold, with a thin rule beneath it). The headline does **not** fill the page. Immediately below it, on the same page, place **Ad Copy #1 and Ad Copy #2**.

**Body layout:**
- **Two ad copies per page.** Hard page break after every second copy.
- Each block headed **`Ad Copy #1`**, **`Ad Copy #2`**, … through **`Ad Copy #10`** (heading style, so the Doc outline is navigable).
- Under each heading: only the ad copy itself — short, line-broken, ready to paste into Meta. Nothing else.
- **Type sizes:** comfortably large and readable — body ≈13pt, ad headings ≈15pt bold, page-1 headline ≈20pt bold.

**Pagination:** headline + #1–2 → p1 · #3–4 → p2 · #5–6 → p3 · #7–8 → p4 · #9–10 → p5.

**Missing inputs:** if the Event Info PDF is missing a fact, use a `[[FILL: …]]` token inline in the copy. Do not add a "needs input" banner to the client Doc; instead flag gaps only in the confirmation message posted to `#esa-master-viktor-chat`.

**Production method:** render the formatted document (title page + page breaks every two copies + headings), create it as an **editable Google Doc** in the client's Drive folder, set sharing to match the client's other deliverables, and **post the Doc link to `#esa-master-viktor-chat`**.

**Versioning:** if a Doc already exists for this event, create `v2` (never overwrite v1).

---

## 11. QUALITY CONTROL — RUN BEFORE CREATING THE DOC

Reject and rewrite any ad that fails:
1. **Voice Lock** — does it sound like *this* client? (Hard gate.)
2. **Scroll-stop** — would the hook stop this profile mid-scroll?
3. **Relevance** — speaks to their specific pain/desire, in their words?
4. **ROI clear within 5 seconds?**
5. **FOMO** — real urgency/exclusivity, not manufactured?
6. **Compliance** — Meta-ready; vertical disclaimer present where required?
7. **CTA** — one crystal-clear step to the right registration destination?

**Set-level checks:** confirm #1–5 are genuinely ESA-spine and #6–10 are genuinely industry-current; confirm hook types/angles are rotated; confirm exactly 10 copies, 2 per page.

---

## 12. POST-RUN

Post a short confirmation to `#esa-master-viktor-chat`: the Google Doc link, version, and a one-line summary (e.g. *"[Event] Ad Copy → v1 created. 10 ads (5 ESA · 5 industry-current), voice-locked, 2/page. Link above."*). Do not paste the full copy into chat — it lives in the Doc.

---

### COMPANION FILES (same folder)
- `workflows/02-ad-copy/reference/ad-copy-library.md` — the 100-copy ESA tone library (calibration only; never copy verbatim).
- `workflows/02-ad-copy/reference/house-style.md` — the canonical formatted output example.
