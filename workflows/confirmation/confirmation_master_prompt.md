---
task_id: confirmation
task_name: "Confirmation Email + Text"
repo_path: "workflows/confirmation/"
depends_on: "01-target-audience-profile"      # approved via ✅ (generation)
trigger_type: "approval_reaction"             # generation trigger
trigger_emoji: "✅"                            # U+2705 — exact match only
trigger_channel: "#esa-master-viktor-chat"
send_trigger: "on_registration"               # actual send fires in GoHighLevel at signup
inputs:
  - "client_brain → voice_lock"
  - "event_page / event_info_pdf → access details + host"
  - "approved_target_audience_profile → tone"
output_type: "google_doc"                      # editable Google Doc, GoHighLevel-ready
scope: "ONE confirmation email + ONE confirmation text. No sequence."
platform: "GoHighLevel"
merge_token: "{{contact.first_name}}"
owner: "Event Sales Agency (ESA)"
version: "1.0"
---

# VIKTOR TASK — CONFIRMATION EMAIL + TEXT

> **One intent:** a single confirmation **email** and a single confirmation **text**, both sent the moment someone registers. Reminders are a separate task.

---

## 1. TRIGGER

My **`✅` (U+2705)** on the most recent **Target Audience Profile** in **`#esa-master-viktor-chat`** triggers Viktor to **write** the copy (Approval Watcher polls every 3 min; look-alikes don't fire). The email and text themselves **send immediately on signup inside GoHighLevel** — that's a GHL workflow trigger, not the ✅.

---

## 2. INPUTS — CHECK ALL THREE

1. **Voice Lock ← Client Brain.** Match the client's voice; sign off in the host's name.
2. **Event page / Event Info PDF.** Event name, date, start time + timezone, format (live/virtual vs in-person), the join link OR venue + address, and the add-to-calendar link.
3. **Approved TAP.** For tone.

Missing join link / address / calendar link → `[[FILL: …]]` token + flag. **Never invent a link or address.**

---

## 3. DISTINGUISH LIVE vs IN-PERSON

Write **both** versions, clearly labeled `[LIVE / VIRTUAL]` and `[IN-PERSON]`:
- **Live/virtual** → access = join link + add-to-calendar; close with "can't wait to see you online."
- **In-person** → access = venue + address + date/time; close with "can't wait to see you in [city]."

(If the event page makes the format obvious, the matching one is enough — but default to giving both, labeled.)

---

## 4. WHAT TO WRITE

### 1) Confirmation email — short and simple
- **Subject:** congratulatory — "You're in!" / "You're registered for [Event]."
- **Body (4–6 short sentences):** Congrats + we're super excited to see you there → confirm they're registered → the one key detail (join link / venue + address) → add to calendar → a quick "keep an eye out for your reminders, add us to your contacts so nothing lands in spam" line → sign-off in the host's name.
- `{{contact.first_name}}`, short line breaks, mobile-first.

### 2) Confirmation text — very short and simple
- **1–3 lines max.** `{{contact.first_name}}`.
- Congrats + the one essential (live: "your link is in your email — add it to your calendar"; in-person: "see you at [venue], [city]") + "can't wait to see you there!" + who it's from.
- SMS-friendly and compliant — identify the sender; let GHL handle the opt-out footer. No long raw links; use a short link or point to the email.

---

## 5. OUTPUT — EDITABLE GOOGLE DOC (GoHighLevel-ready)

- Two clearly labeled sections: **Confirmation Email** and **Confirmation Text**, each with its `[LIVE / VIRTUAL]` and `[IN-PERSON]` version — paste-ready (subject + body for the email; the message for the text). No strategy notes in the copy — zero reformatting.
- Keep `{{contact.first_name}}` and the link tokens intact.
- Title at the top: `[Event Name] Confirmation — Email + Text`, with a small line under it (client + event date + format).
- Save to the client's Drive folder; post the link to `#esa-master-viktor-chat`.

---

## 6. POST-RUN

Confirmation to `#esa-master-viktor-chat`: Doc link, version, and any `[[FILL]]` gaps.
