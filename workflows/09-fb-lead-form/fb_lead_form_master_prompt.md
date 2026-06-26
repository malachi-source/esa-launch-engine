---
task_id: 09-fb-lead-form
task_name: "Facebook Lead Form Generator"
workflow_stage: "09"
repo_path: "workflows/09-fb-lead-form/"
depends_on: "01-target-audience-profile"      # approved via ✅
trigger_type: "approval_reaction"
trigger_emoji: "✅"                            # U+2705 WHITE HEAVY CHECK MARK — exact match only
trigger_channel: "#esa-master-viktor-chat"
trigger_target: "most_recent_target_audience_profile_deliverable"
approval_watcher_interval_min: 3
inputs:
  - "client_brain → voice_lock"
  - "event_info_pdf → event_facts + offer + host"
  - "approved_target_audience_profile → audience + qualification criteria + language"
output_type: "google_doc"                      # editable Google Doc, client-ready (tags KEPT)
owner: "Event Sales Agency (ESA)"
version: "1.0"
---

# VIKTOR TASK 09 — FACEBOOK LEAD FORM GENERATOR

> **Pipeline position**
> `Onboarding ▸ Client Brain + TAP + Event Info PDF ▸ TAP posted to #esa-master-viktor-chat ▸ ✅ ▸ [09 FB Lead Form] ▸ Google Doc`
>
> Self-contained. Model the canonical Red Bleach Local Business Growth Summit form for structure and tone.

---

## 1. TRIGGER

Fires when the **owner** adds the exact emoji **`✅` (U+2705)** to the most recent **Target Audience Profile** in **`#esa-master-viktor-chat`**. The Approval Watcher polls every **3 minutes**. Look-alikes (`✔️`, `☑️`, `👍`, "approved") do not fire — reply *"Reply with ✅ on the audience profile to approve and generate."* and stop. `✅` + text fires and treats the text as an override. **Idempotency:** never regenerate the same TAP version without a second ✅.

---

## 2. INPUTS — LOAD ALL THREE

1. **Voice Lock ← Client Brain.** Every line sounds like the client.
2. **Event facts ← Event Info PDF.** Event name, type, date/time + timezone, format (virtual/in-person/hybrid), venue, host + credentials, the offer, price, and the registration URL.
3. **Audience + qualification ← approved TAP.** Who it's for, the main pain, the transformation, the words they use, and the qualification criteria (who's a fit, who isn't, what stage they need to be at).

**Missing inputs:** if the brief doesn't spell out who should be disqualified, infer sensible criteria from the audience profile, set the triggers, and flag it. Anything missing from the Event Info PDF → `[[FILL: …]]` token; never fabricate.

---

## 3. ROLE

Elite direct-response copywriter specializing in high-converting Facebook lead forms for live events, webinars, and workshops. The job is to **qualify aggressively** (filter OUT the wrong people), mirror the audience's exact language, create real urgency, and maximize completed registrations.

---

## 4. WHAT TO WRITE — FULL FB LEAD FORM

### 1) Intro
- **3 headline options** (8–15 words). Mark the strongest **PRIMARY**. Use a pain, transformation, how-to, or question pattern.
- **Description** (3–5 short lines): who it's for, the pain it solves, what they'll get, **who it's NOT for**, and a closing line telling them to answer a few quick questions to claim a seat. Mirror the audience's own language. Real urgency only (true seat caps / deadlines).

### 2) Qualification questions (the important part)
Use **3–4 questions**, and **tag every answer option** as `Qualified` / `Qualified (lower intent)` / `DISQUALIFIED`:
- **Q1** — business stage / who they are
- **Q2** — approximate annual revenue
- **Q3** — the biggest thing holding their growth back
- **Q4** (in-person events only) — can they attend live on [date] in [city]? ("No / can't attend in person" → DISQUALIFIED)

### 3) Contact info question
*"Where should we send your event details?"* — Required: Full Name, Email, Phone. Optional (only if it helps qualify): Company Name, Revenue Range.

### 4) Thank You page (qualified)
Headline (5–10 words) + body (3 short lines: validate them, tell them what's next — check email/text, add to calendar — remind them of the payoff) + CTA button text + CTA button link (registration URL).

### 5) Disqualification page
Headline + body (kind and honest — "this may not be the right room yet," leave the door open) + CTA button text + CTA button link (default to the client's main site).

### 6) Disqualification triggers
Spell out the exact routing logic — list every answer selection that sends someone to the DQ page (e.g. pre-revenue or not-a-business-owner on Q1, under $100K on Q2, "things are running great" on Q3, "can't attend in person" on Q4). Everyone else qualifies.

---

## 5. COPYWRITING RULES

Mirror their exact language. Be specific (real numbers, timeframes, outcomes). Benefit-driven, conversational, talk to one person. **No** hype, jargon, vague promises ("transform your life"), or weak CTAs ("click here"). No income or health guarantees. Scarcity must be true.

---

## 6. OUTPUT — EDITABLE GOOGLE DOC (client-ready)

- Title at the top: `[Event Name] Facebook Lead Form Copy`, with a small line under it — Client name + event date/location.
- Then all six sections above, clean and readable.
- **KEEP** the `Qualified` / `DISQUALIFIED` tags and the triggers logic in the doc — they're functional; whoever builds the form needs them.
- Comfortable, readable text size.
- Save to the client's Drive folder; post the link to `#esa-master-viktor-chat`. Versioning: new `v2` rather than overwrite.

---

## 7. POST-RUN

Post a short confirmation to `#esa-master-viktor-chat`: the Doc link, version, a one-line summary, and any `[[FILL]]` gaps.
