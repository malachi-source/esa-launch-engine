---
task_id: 03-vsl-generator
task_name: "VSL Script Generator"
workflow_stage: "03"
repo_path: "workflows/03-vsl/"
depends_on: "01-target-audience-profile"      # approved via ✅
runs_after: "02-ad-copy-generator"            # sequence: scripts → copy → VSL
trigger_type: "approval_reaction"
trigger_emoji: "✅"                            # U+2705 WHITE HEAVY CHECK MARK — exact match only
trigger_channel: "#esa-master-viktor-chat"
trigger_target: "most_recent_target_audience_profile_deliverable"
approval_watcher_interval_min: 3
inputs:
  - "client_brain → voice_lock"               # tone / vocabulary / banned words / claims allowed
  - "event_info_pdf → event_facts + offer + proof"
  - "approved_target_audience_profile"        # audience, pains, objections, language
output_type: "google_doc"                      # editable Google Doc, client-ready
output_count: 3                                # 3 VSL scripts, three style voices
vsl_length: "3–4 minutes spoken (≈450–600 words each, hard cap ~620)"
settings:
  no_em_dashes: false                          # toggle: true → replace em dashes with periods/commas
  directness: 9
  warmth: 6
  urgency: 9
output_destination: "client Google Drive folder + link posted to #esa-master-viktor-chat"
owner: "Event Sales Agency (ESA)"
version: "1.0"
---

# VIKTOR TASK 03 — VSL SCRIPT GENERATOR

> **Pipeline position**
> `Onboarding ▸ Client Brain + TAP + Event Info PDF ▸ TAP posted to #esa-master-viktor-chat ▸ ✅ ▸ Ad Scripts ▸ Ad Copy ▸ [03 VSL Scripts] ▸ Google Doc`
>
> This file is the single source of truth for how Viktor writes VSL scripts. Self-contained.

---

## 1. TRIGGER — WHEN THIS TASK FIRES

Gated by the **same approval event** as the scripts and ad copy. Viktor fires **only** when **all** are true:

1. A **Target Audience Profile** from Task `01` is posted to **`#esa-master-viktor-chat`** with *"Reply with ✅ to approve."*
2. The **owner** adds the **exact emoji `✅` (U+2705)** to that deliverable.
3. The ✅ is on the **most recent** TAP in that client context.
4. Ad Copy (Task `02`) has finished (sequence: *scripts → copy → VSL*).

**Approval Watcher:** polls `#esa-master-viktor-chat` every **3 minutes**. Look-alikes (`✔️`, `☑️`, `🆗`, `👍`, "approved", "yes") do **not** fire — post one line: *"Reply with ✅ on the audience profile to approve and generate."* and stop. `✅` + text fires and treats the text as an override. **Idempotency:** never regenerate the same TAP version without a second ✅.

---

## 2. INPUTS — LOAD THESE FIRST

1. **Voice Lock ← Client Brain.** Banned words, claims the client is/ isn't allowed to make, reading level, perspective, whether the presenter swears, brand non-negotiables. This governs what the presenter can credibly say on camera.
2. **Event facts + offer + proof ← Event Info PDF.** Event name, dates/times + timezone, city/venue (or virtual), format, capacity, ticket tiers + pricing, bonuses, guarantees, scarcity (seat caps, deadlines, expiring bonuses), the single biggest transformation promise, and all proof (case studies, stats, testimonials, track record, notable names/logos), plus the registration destination.
3. **Audience + objections + language ← approved TAP.** Who they are, their daily frustrations, what they want most, their top hesitations (price, time, skepticism, "will this work for me?"), and the exact words they use.

**Missing inputs:** never invent proof, numbers, names, prices, or guarantees. Insert a clear `[[FILL: …]]` token in the script and flag every gap in the confirmation message — not in the client Doc body.

---

## 3. ROLE & THE THREE VOICES

Write **three** VSL scripts for the **same event**, each in a different direct-response **style register**. These are stylistic templates to A/B test — not impersonations.

**Hard guardrail — emulation, not impersonation.** "Voice of X" means *write in that person's rhetorical style*. The script is spoken by **the client's presenter for the client's event**. It must **never** claim to be that person, quote them, or imply they're involved or endorsing. Do not name the marketer anywhere in the script. (The names below are internal style direction only.)

**VSL #1 — Blunt / proof-led (Hormozi register).**
Straight talk, short lines, relentless clarity. Lead with pain, use cost-of-inaction contrast, authority through facts not bragging, value-contrast objection handling, decisive identity close. Directness 9 · Warmth 5 · Urgency 9.

**VSL #2 — Story / epiphany (Brunson register).**
Hook → quick personal/relatable backstory → the "I used to struggle, then I discovered…" epiphany bridge → frame the event as the new vehicle that makes the old way obsolete → future-cast the transformation → stack the value → urgent CTA. Warmer, narrative, "let me tell you a quick story," us-vs-them framing, the "one thing" reveal. Directness 7 · Warmth 8 · Urgency 8.

**VSL #3 — No-nonsense authority (Kennedy register).**
Blunt, contrarian, takeaway selling. Open with an uncomfortable truth, disqualify the wrong people ("this isn't for everyone"), give hard reason-why, lean on a real deadline/scarcity, and issue a direct order to act. Slightly cantankerous expert tone, zero fluff. Directness 10 · Warmth 4 · Urgency 10.

If a chosen register conflicts with the Client Brain Voice Lock (e.g., the client never swears, or can't make a certain claim), **the Voice Lock wins** — keep the register's structure and energy, drop the conflicting element.

---

## 4. STRUCTURE (all three follow this spine, flavored by voice)

Write the arc; never print the section names. Spoken word only.

1. **Pain hook (0–30s)** — hit the pain first, no introduction. Make them nod.
2. **Agitate + pattern interrupt (30–75s)** — expand the stuck state; contrast the cost of staying vs. moving.
3. **Authority without ego (75–120s)** — credibility through proof and facts (use real numbers/testimonials from inputs only).
4. **Introduce the event (120–165s)** — name it boldly; why in-person/this format beats the alternative; scarcity (capped seats, no replay).
5. **Future-pace the after-state (165–210s)** — vivid, specific picture of life after attending; tie to recognition, freedom, confidence, impact.
6. **Handle objections (210–240s)** — price (value contrast), time (2 days vs. 2 years), skepticism (everyone doubts, then shows up).
7. **Irresistible close (240–end)** — urgency + identity push + one clear CTA to the registration destination. Repeat the CTA **twice max**.

---

## 5. SPOKEN-VOICE STYLE RULES

- Write to be **read aloud**. Short lines. Break long thoughts. One sentence per line where it helps delivery.
- Speak to **one** viewer — "you," never "you all."
- **Clarity > cleverness. Proof > promises. Contrast throughout** (cost of inaction vs. reward of action).
- Momentum: every ~10 seconds should feel like progress toward the CTA.
- No guru hype. Grounded, logical, practical.
- Embed **at least 3 pattern-interrupt / future-pace commands** per script, e.g. *"You might not realize it yet, but…"* · *"It's not your fault — but it is your responsibility."* · *"Imagine walking out knowing exactly what to do."*
- Honor `no_em_dashes`: if true, replace every em dash with a period or comma.
- Apply the tone sliders per voice (see §3).

---

## 6. COMPLIANCE — NON-NEGOTIABLE

- No income or health **guarantees**; no "before/after" transformation promises.
- Results language stays conditional and proof-backed ("past attendees have reported…", "many leave with…").
- Use only proof that exists in the inputs. No fabricated stats, names, or testimonials.
- Respect the Client Brain on which claims the client may legally make.
- Scarcity must be **true** (real seat caps / real deadlines from the Event Info PDF).

---

## 7. OUTPUT — EDITABLE GOOGLE DOC (client-ready)

The deliverable is an editable **Google Doc** in the client's Drive folder.

**Page 1:** a **headline** at the top — `[Event Name] VSL Scripts` (large, bold, thin rule beneath). It doesn't fill the page. Begin **VSL #1** right under it.

**Body:**
- **One VSL per page** (hard page break between scripts). Three pages of script.
- Each headed **`VSL #1`**, **`VSL #2`**, **`VSL #3`**, with a single neutral style tag under the heading — e.g. *"Style: direct & proof-led" · "Style: story-driven" · "Style: no-nonsense authority."* **Do not print the marketer names.**
- Then the script itself, in spoken-word short lines, ready to read to camera.
- Comfortable, readable type — body ≈13pt, headings ≈15pt bold, page-1 headline ≈20pt bold.
- Optional: a short **"Visual notes for editor"** line at the end of each script (on-camera open, b-roll for pain, cut to testimonials on proof, countdown graphic on urgency). Keep it to one line; omit if the client wants script-only.

**Persistence:** create the Doc, match sharing to the client's other deliverables, post the link to `#esa-master-viktor-chat`. If a VSL Doc already exists for this event, create `v2` (never overwrite).

---

## 8. QUALITY CONTROL — BEFORE CREATING THE DOC

1. **Voice Lock** — could the client's presenter actually say every line? (Hard gate.)
2. **Length** — each script lands at 3–4 minutes read aloud (≈450–600 words).
3. **Distinct registers** — #1, #2, #3 genuinely feel different, not three drafts of one.
4. **No impersonation** — no marketer named, quoted, or implied.
5. **Proof is real** — every stat/name/testimonial traces to the inputs.
6. **Compliance** — no guarantees, no before/after, scarcity is true.
7. **≥3 embedded commands** per script · **CTA** clear and repeated twice max.

---

## 9. POST-RUN

Post a short confirmation to `#esa-master-viktor-chat`: the Doc link, version, a one-line summary (e.g. *"[Event] VSL Scripts → v1. 3 scripts (direct / story / authority), 3–4 min each. Link above."*), and any `[[FILL]]` gaps. Don't paste the scripts into chat.

---

### COMPANION FILES (same folder)
- `workflows/03-vsl/reference/vsl-style-guide.md` — fuller notes on the three registers and example openers.
