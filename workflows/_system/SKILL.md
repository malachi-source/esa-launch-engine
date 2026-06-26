# SKILL.md — ESA Event Marketing System (Viktor)

> The master doc. Read this first. It defines what the system is, the conventions every task shares, the full task map, and how to add new tasks. Viktor is a Slack-connected AI app that runs this system: it reads inputs from Google Drive, generates deliverables, saves them back to Drive, loads email/text copy into GoHighLevel, and posts links to Slack.

---

## 0. WHERE THESE FILES LIVE (GitHub — source of truth)

All Viktor specs live in GitHub repo **`malachi-source/esa-launch-engine`**, branch **`main`**, under `workflows/`. This is the source of truth — read the spec from here before running any task.

| What | Path |
|---|---|
| System docs | `workflows/_system/` → `SKILL.md` (this file), `orchestration_logic.md`, `drive_folder_sop.md` |
| Client Brain Builder | `workflows/00-client-brain/client_brain_builder.md` |
| Ad Copy | `workflows/02-ad-copy/ad_copy_master_prompt.md` |
| VSL | `workflows/03-vsl/vsl_master_prompt.md` |
| FB Lead Form | `workflows/09-fb-lead-form/fb_lead_form_master_prompt.md` |
| Reactivation Emails | task brief `workflows/10-reactivation-emails/10-reactivation-emails.task.md` · master prompt `workflows/reactivation-emails/reactivation_emails_master_prompt.md` |
| Re-Engagement Texts | `workflows/11-reengagement-texts/11-reengagement-texts.task.md` |
| Phone Script | `workflows/12-phone-script/12-phone-script.task.md` |
| Social Media Scripts | `workflows/08-social-media/08-social-media.task.md` |
| Confirmation | `workflows/confirmation/confirmation_master_prompt.md` |

**Two cautions when reading a folder:**
- Some folders (`02-ad-copy`, `03-vsl`, `09-fb-lead-form`, `08-social-media`) also contain an older `PROMPT*.md` / `*_STANDARD.md` from a separate build. For Viktor tasks, always use the **`*_master_prompt.md`** (or `*.task.md`) file — never the `PROMPT*.md`.
- Reactivation Emails is currently split: the human brief lives in `10-reactivation-emails/` and the generation spec in `reactivation-emails/`. Read both; the `*_master_prompt.md` is authoritative for generation.

---

## 1. WHAT THIS IS

An end-to-end pipeline that takes a new client from onboarding to a complete set of event-marketing assets — ad scripts, ad copy, VSLs, a Facebook lead form, reactivation and confirmation messaging, a phone script, and the supporting event collateral — all written in the client's own voice and gated by a single human approval.

---

## 2. ARCHITECTURE

```
Onboarding form
   │ (~15 min, parallel)
   ├─ Drive folder        →  Auto Drive Folder SOP
   ├─ Client Brain        →  Client Brain Builder (voice analysis)
   ├─ Target Audience Profile (TAP)
   └─ Event Info PDF
   │
   ▼
TAP → #esa-master-viktor-chat  "Reply with ✅ to approve."
   │
   ▼  ←← OWNER REACTS ✅  (the one gate)
   │
Creative generation (see Orchestration Logic):
   Ad Scripts → Ad Copy → VSL  ·  FB Lead Form  ·  Reactivation Emails  ·  Reactivation Texts  ·  Confirmation  ·  Phone Script
   │
   ▼
Deliverables → client's Google Drive folder  +  link posted to Slack
```

Full control flow, gates, and firing order: **`orchestration_logic.md`**.

---

## 3. THE SHARED CONTRACT (every task follows this)

1. **Trigger** — the owner's **exact `✅` (U+2705)** on the most recent **TAP** in **`#esa-master-viktor-chat`**. Look-alikes (`✔️ ☑️ 👍`) never fire. Idempotent per TAP version.
2. **Three inputs, every time** —
   - **Voice Lock** ← Client Brain (match the client's voice).
   - **Event facts** ← Event Info PDF / event page.
   - **Targeting/tone** ← approved TAP.
3. **Output** — an editable **Google Doc** in the client's Drive folder; link posted to the channel. Email/text tasks are **GoHighLevel-ready** (paste-and-go, with send-timing labels). Versioned — never overwrite.
4. **`[[FILL: …]]` convention** — missing facts become flagged tokens; **never fabricate** dates, prices, links, addresses, or proof.
5. **Compliance** — no income/health guarantees, no before/after promises; results stay conditional and proof-backed; scarcity must be true.
6. **Personalization** — GHL merge token is `{{contact.first_name}}`.

---

## 4. TASK MAP

| Task | Spec file | Output | Notes |
|---|---|---|---|
| Ad Scripts | `ad_scripts_master_prompt.md` | Google Doc | 20 scripts (1–10 ESA, 11–20 industry) — *spec pending* |
| Ad Copy | `ad_copy_master_prompt.md` | Google Doc | 10 copies (5 ESA / 5 industry); headline p1, 2/page, no internal labels |
| VSL | `vsl_master_prompt.md` | Google Doc | 3 scripts, 3–4 min, three style registers (emulation, not impersonation) |
| FB Lead Form | `fb_lead_form_master_prompt.md` | Google Doc | qualification tags + DQ logic + DQ page (tags KEPT in doc) |
| Reactivation Emails | `reactivation_emails_master_prompt.md` | Google Doc (GHL) | ~12–15 emails, ~30-day arc, value-first, 1/page |
| Reactivation Texts | `reengagement_texts_master_prompt.md` | Google Doc (GHL) | ~12 texts, YES-reply blend — *spec pending* |
| Confirmation | `confirmation_master_prompt.md` | Google Doc (GHL) | 1 email + 1 text, on signup, live vs in-person |
| Phone Script | `phone_script_master_prompt.md` | Google Doc | *spec pending* |
| Event Info PDF | `event_info_pdf_prompt.md` | Branded PDF | 8 sections — *spec pending* |

**System docs:** `client_brain_builder.md` · `drive_folder_sop.md` · `orchestration_logic.md` · this file.

---

## 5. STATUS

- **Built:** Ad Copy, VSL, FB Lead Form, Reactivation Emails, Confirmation + the four system docs (Client Brain Builder, Drive SOP, Orchestration, SKILL).
- **Pending specs:** Ad Scripts, Re-engagement Texts, Event Info PDF, Phone Script.

---

## 6. HOW TO ADD A NEW TASK

1. Copy the shape of an existing `*_master_prompt.md` (frontmatter → trigger → three inputs → role → what to write → output → post-run).
2. Keep the shared contract in §3 — same ✅ trigger, same three inputs, same Drive output + channel post, same `[[FILL]]` and compliance rules.
3. Decide output type: Google Doc (creative) or GHL-ready Google Doc (email/text, with send-timing labels).
4. Add a row to the Task Map above and slot the file into `workflows/`.
5. If it changes the flow, update `orchestration_logic.md`.
