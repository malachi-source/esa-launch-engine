---
doc_id: orchestration-logic
doc_type: "architecture / control flow"
repo_path: "workflows/_system/"
channel: "#esa-master-viktor-chat"
approval_emoji: "✅"                            # U+2705 — exact match only
approval_watcher_interval_min: 3
owner: "Event Sales Agency (ESA)"
version: "1.0"
status: "DEFAULT FLOW — confirm firing order; some tasks can run in parallel"
---

# ORCHESTRATION LOGIC — What Fires When

> The control flow for the whole system: how a client goes from onboarding to a full set of deliverables, and exactly where the human approval gate sits.

---

## 1. THE FLOW

```
Onboarding form submitted
        │
        ▼ (~15 min, parallel)
  ┌─────────────────────────────────────────────┐
  │  Stage 0 — auto-generate:                    │
  │   • Drive folder  (Auto Drive Folder SOP)    │
  │   • Client Brain  (Client Brain Builder)     │
  │   • Target Audience Profile (TAP)            │
  │   • Event Info PDF                            │
  └─────────────────────────────────────────────┘
        │
        ▼
  TAP posted to #esa-master-viktor-chat
  "Reply with ✅ to approve."
        │
        ▼  ←←← OWNER REACTS ✅  (the one human gate)
        │
  Approval Watcher detects ✅ (polls every 3 min)
        │
        ▼ (Stage 2 — creative generation)
   Ad Scripts → Ad Copy → VSL          (sequential)
   FB Lead Form                         ┐
   Reactivation Emails                  │ (can run in
   Reactivation Texts                   │  parallel after
   Confirmation (email + text)          │  approval)
   Phone Script                         ┘
        │
        ▼
  Each task: save Google Doc to the client's Drive folder
             + post the link to #esa-master-viktor-chat
```

---

## 2. THE APPROVAL GATE (the only human step)

- The gate is the owner's **exact `✅` (U+2705)** on the **most recent Target Audience Profile** in **`#esa-master-viktor-chat`**.
- The **Approval Watcher** polls every **3 minutes**.
- **Look-alikes do not fire:** `✔️` (U+2714), `☑️` (U+2611), `🆗`, `👍`, or the words "approved"/"yes." On a look-alike, reply once: *"Reply with ✅ on the audience profile to approve and generate."*
- **`✅` + text** still fires; treat the extra text as an override for that run.
- **Idempotency:** one approval per TAP version. If a TAP already has deliverables, require a **second ✅** to regenerate, and version the output rather than overwrite.

---

## 3. GATE CONDITIONS PER TASK

Before any Stage-2 task runs, it must confirm:
1. **Client Brain exists** (Voice Lock available). If not → hold + flag in channel.
2. **Event Info exists** (event facts available). If not → hold + flag.
3. **The approved TAP** is the current one.

Inside each task, missing specifics (price, date, links, proof) become `[[FILL: …]]` tokens and are flagged in the channel post — **never fabricated.**

---

## 4. FIRING ORDER

- **Sequential (established):** Ad Scripts → Ad Copy → VSL.
- **Parallel (independent):** FB Lead Form, Reactivation Emails, Reactivation Texts, Confirmation, Phone Script — any of these can run as soon as the ✅ lands, since they don't depend on each other.
- Order among the parallel set is configurable; adjust to your compute/rate limits.

---

## 5. EMAIL / TEXT TASKS — TWO TRIGGERS

For GoHighLevel deliverables (reactivation, confirmation, reminders):
- The **✅** triggers Viktor to **write** the copy.
- The **actual send** is a **GHL workflow trigger** — signup (confirmation), schedule (reactivation), or date-relative (reminders) — **not** the ✅.
- Each email/text Doc is therefore labeled with its **send timing** so it drops into GHL with no guesswork.

---

## 6. OUTPUTS + WHERE THEY GO

- **Deliverables** → editable Google Docs in the client's Drive folder (per the Drive SOP), link posted to the channel.
- **Task specs / prompts** → GitHub under `workflows/…`.
- **Status + gaps** → a one-line confirmation in `#esa-master-viktor-chat` after each run, including any `[[FILL]]` flags.

---

## 7. PREREQUISITES (must be connected to Viktor)

Google Drive (Client Brain + output Docs), GitHub (task specs), the Slack channel (watch for ✅, post links), and GoHighLevel (load the email/text copy). If any are disconnected, the matching trigger or save step won't fire — check these first when something doesn't run.
