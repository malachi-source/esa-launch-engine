---
task_id: reactivation-emails
task_name: "Reactivation Email Generator"
repo_path: "workflows/reactivation-emails/"
depends_on: "01-target-audience-profile"      # approved via ✅
trigger_type: "approval_reaction"
trigger_emoji: "✅"                            # U+2705 WHITE HEAVY CHECK MARK — exact match only
trigger_channel: "#esa-master-viktor-chat"
trigger_target: "most_recent_target_audience_profile_deliverable"
approval_watcher_interval_min: 3
inputs:
  - "client_brain → voice_lock"
  - "event_page / event_info_pdf → event_facts + offer + host"
  - "approved_target_audience_profile → pains + desires + objections + language"
output_type: "google_doc"                      # editable Google Doc, GoHighLevel-ready
sequence_default: "≈12–15 emails over ~30 days, 3–4 per week"
platform: "GoHighLevel"
merge_token: "{{contact.first_name}}"
owner: "Event Sales Agency (ESA)"
version: "1.0"
---

# VIKTOR TASK — REACTIVATION EMAIL GENERATOR

> Wakes up old/cold leads and moves them to register. **Value-first and human — not a hard sell.**

---

## 1. TRIGGER

Fires on the **owner's** exact **`✅` (U+2705)** on the most recent **Target Audience Profile** in **`#esa-master-viktor-chat`** (Approval Watcher polls every 3 min). Look-alikes don't fire. `✅` + text = override. Idempotent per TAP version.

---

## 2. INPUTS — CHECK ALL THREE, EVERY TIME

1. **Voice Lock ← Client Brain.** Match the client's voice exactly; every email should sound like them.
2. **Event page / Event Info PDF.** Event name, date, location, offer + ticket tiers, bonuses, real scarcity, the registration link, and the host's name for the sign-off.
3. **Approved TAP.** Pains, desires, objections, and the exact words they use.

Missing event facts → `[[FILL: …]]` token + flag. Never fabricate.

---

## 3. PER-EMAIL RULES

- **Short. Under 7 sentences.** One idea per email. Mobile-first, lots of line breaks.
- **Lead with value** — a quick tip, reframe, insight, or short story the reader benefits from even if they never buy.
- **One soft CTA** at the end (one link, the registration page). Teach first, invite second.
- Personalize with `{{contact.first_name}}`.
- Sign off in the client's / host's name.
- **One ready-to-send subject line** at the top (2 alternates underneath are fine for A/B testing; the first is the paste-ready primary).

---

## 4. SEQUENCE ARC

Map to the runway before the event. Default to **≈12–15 emails over ~30 days at 3–4/week**.

- **Early — reactivation + quick wins.** "Haven't seen you in a while," one useful tip, a short relatable story. Warm, curious.
- **Middle — light proof + belief shifts.** A real result or testimonial from the inputs, a myth-buster, a behind-the-scenes from the host. Still teaching.
- **Late — gentle urgency.** Real deadline, limited seats, bonus expiring, final call. Human, not panicky — **no "winners vs losers."**

Rotate archetypes for variety: reactivation opener, quick-win lesson, relatable story, social proof, soft objection-handler, behind-the-scenes, scarcity, final call.

---

## 5. COMPLIANCE

No income or health guarantees, no before/after promises. Results stay conditional and tied to real proof from the inputs. Scarcity must be true.

---

## 6. OUTPUT — EDITABLE GOOGLE DOC (GoHighLevel-ready)

- **ONE email per page** — each isolated and easy to grab.
- Lay each email out exactly as it goes into GHL: subject line → body with short line breaks → CTA line with the link → sign-off. **No strategy notes in the body, no extra formatting — paste-and-go.**
- Keep `{{contact.first_name}}` and the `[link]` / registration-URL tokens intact.
- Title at the top of page 1: `[Event Name] Reactivation Emails`, with a small line under it — client name + event date.
- Comfortable, readable text size.
- Save to the client's Drive folder; post the link to `#esa-master-viktor-chat`.

---

## 7. POST-RUN

Confirmation to `#esa-master-viktor-chat`: Doc link, version, one-line summary (count + day-span), and any `[[FILL]]` gaps. If the event date/runway isn't clear, default to the 30-day, 3–4×/week plan and flag it.
