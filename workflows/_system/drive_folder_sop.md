---
doc_id: drive-folder-sop
doc_type: "SOP"
repo_path: "workflows/_system/"
runs_at: "onboarding (Stage 0, part of the ~15-min auto-generation)"
owner: "Event Sales Agency (ESA)"
version: "1.0"
status: "DEFAULT STRUCTURE — adjust folder names/paths to your preference"
---

# AUTO DRIVE FOLDER SOP

> Every client/event gets a consistent Google Drive folder so deliverables are findable and every task knows exactly where to save. All tasks reference "save to the client's Drive folder" — this doc defines that folder.

---

## 1. WHEN IT'S CREATED

On **onboarding form submission**, as part of the Stage-0 auto-generation. If the client folder already exists, reuse it. If a folder for the same event name already exists, append the date to disambiguate.

---

## 2. DEFAULT STRUCTURE

```
/ESA Clients/
  └── [Client Name]/
        ├── 00 — Client Brain/          ← Client Brain + Voice Lock (per client)
        ├── _Assets/                    ← logos, brand, voice samples, uploads
        └── [Event Name] — [Date]/      ← one subfolder per event
              ├── 01 — Target Audience Profile/
              ├── 02 — Event Info/       ← Event Info PDF / event page
              ├── Ad Scripts/
              ├── Ad Copy/
              ├── VSL/
              ├── FB Lead Form/
              ├── Reactivation Emails/
              ├── Reactivation Texts/
              ├── Confirmation/
              └── Phone Script/
```

- **Client-level** holds what's true across all of that client's events (Client Brain, Voice Lock, brand assets).
- **Event-level** holds the TAP, Event Info, and every creative deliverable for that specific event.

---

## 3. NAMING CONVENTIONS

- Folders: as above.
- Files: `[Event Name] [Deliverable] — v[N]` (e.g., `Local Business Growth Summit Ad Copy — v1`).
- Always include the version. **Never overwrite** an existing deliverable — create `v2`.

---

## 4. SHARING / PERMISSIONS

- Internal team: full access by default.
- Client: view access to whichever folders you share with clients (typically the finished deliverables, not the working `_Assets`/Client Brain).
- Match each new deliverable's sharing to the client's existing deliverables so nothing leaks or gets locked.

---

## 5. HOW TASKS USE IT

Every task: (1) resolve the correct `[Client] / [Event]` folder, (2) save its Google Doc into the matching subfolder with a versioned name, (3) post the Doc link to `#esa-master-viktor-chat`.

---

## 6. EDGE CASES

- **Client folder missing** → create it.
- **Event folder missing** → create it under the client.
- **Duplicate event name** → append the date.
- **Re-run / regeneration** → new version file, never overwrite.
- **Drive not connected to Viktor** → the save + link-post steps fail; surface this clearly rather than silently dropping the deliverable.
