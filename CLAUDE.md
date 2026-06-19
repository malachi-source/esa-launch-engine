# ESA Launch Engine — Project Context

> This file is read automatically by Claude Code at the start of every session.
> It tells Claude (and any teammate) what this project is and how to work in it.
> Keep it up to date. If something here is wrong, fix it.

## What we're building

A web app for **Event Sales Agency (ESA)**. ESA runs **done-for-you (DFY) webinar/event launches** for clients.

The flow:
1. A client fills out an **onboarding form** (Typeform-style, saves progress, one centralized form).
2. On submit, the app runs ESA's whole **launch checklist automatically using AI**, our own prompts.
3. A **human reviews and approves each step** before it's finalized.

Goal: automate **every** step with AI over time. Each step is its own focused workflow.

## The big idea: it's a pipeline, not all-at-once

The workflows have a dependency order. The "foundation" docs must run FIRST because every
other workflow uses them as input:

```
Onboarding form
   → 00-foundation (Project Summary + Event Summary + Audience Profile)
       → THEN fan out in parallel:
         ad scripts, ad copy, VSL, emails, texts, re-engagement, social,
         FB lead form, audiences, sales script
```

So "run everything in parallel on submit" really means: run foundation first, then run the rest in parallel.

## How the repo is organized

- `workflows/` — one folder per launch step. Each folder is self-contained:
  - `PROMPT.md` — the actual ESA prompt for that step (the source of truth).
  - `CLAUDE.md` — notes for that workflow: what it does, inputs, outputs, status, decisions, TODO.
  - `examples/` — sample inputs and good outputs.
- `form/` — the onboarding form. `form/app/index.html` is the live form (source of truth);
  `form/onboarding-form-questions.md` is the question spec; `form/DEPLOY.md` is the original deploy notes.
- `orchestrator/` — the engine that runs workflows in the right order (not built yet).
- `audience-machine/` — **machine #1, BUILT.** A one-command Python tool that builds a
  client's full Meta audience stack (35 audiences) via the Marketing API. Plug-and-play per
  client, idempotent, config-driven. See `audience-machine/README.md` + `CLAUDE.md`. Blocked
  only on the Meta system user token (`audience-machine/TOKEN_SETUP.md`) before its first live run.
- `reference/` — SOPs, the swipe files, audit checklists, anything shared.

## How the team works (we are non-coders directing Claude Code)

- Each person OWNS one or more workflow folders and perfects the prompt there.
- Work happens inside your own folder, so we rarely collide.
- Each person works on their own **branch**; Claude Code handles all git for you.
- At the END of every session, tell Claude: "update this folder's CLAUDE.md with what we did
  and what's left." That's how we never lose progress between chats.

## Mandatory document formatting standards

**Every generated document MUST follow its formatting standards file. No exceptions.**

- **TAP (Target Audience Profile):** see `reference/tap-formatting-standards.md`
  - No section breaks across pages (sections never split)
  - 5-7 pages only (including cover page)
  - Fortune 500 design quality (gold accent bars, branded tables, callout boxes)
  - Client brand colors applied throughout from form fields 48-50

These rules are non-negotiable. Read the full standards file before generating any TAP.

## Source of truth for the prompts

Master prompt library (Google Doc): id `1hUHbuSIrJ6DrkNFDuNhS1vKvzOuZOdbuYFoPsN0NL-Q`.
~22 prompts. House style: model Tai Lopez / Russell Brunson / Grant Cardone / Iman Ghazi
(Hormozi for the VSL), Meta-compliant, NO em dashes, spoken one-person voice, tone sliders.

## Current state — RESUME HERE (last updated 2026-06-12)

### Done & live
- **Repo** on GitHub (private): `github.com/malachi-source/esa-launch-engine`. Built by a non-coder
  using Claude Code. Team = each person their own GitHub account as a collaborator (never share logins).
- **All ~22 prompts** copied verbatim from the Google Doc into `workflows/*/PROMPT*.md` + `reference/`.
- **Onboarding form — BUILT & DEPLOYED LIVE:**
  - Questions: `form/onboarding-form-questions.md` — **68 questions** (58 from the original esabuilder
    form + 10 keystone audience questions). Q "paste 5–10 real customer quotes" is the highest-value one.
  - Code (source of truth): `form/app/index.html` — static, Typeform-style, one-question-at-a-time,
    save-and-resume (localStorage), data-driven from a JS questions array.
  - Database: **Supabase** project ref `hiqlubrygiprmelechza` (`https://hiqlubrygiprmelechza.supabase.co`),
    table `onboarding_submissions` (RLS on; public can INSERT only, cannot read; answers stored as JSONB).
    The form posts directly to Supabase REST using the anon public key (embedded in the page — safe).
  - Hosting: **GitHub Pages** from a separate PUBLIC repo `github.com/malachi-source/esa-onboarding-form`.
    **LIVE URL: https://malachi-source.github.io/esa-onboarding-form/** — keep that public copy in sync
    with `form/app/index.html` when the form changes.
  - `form/app/api/submit.js` (a Vercel function) is UNUSED — we went GitHub Pages + direct Supabase instead.

### Next steps
- [ ] **Audience machine — go live:** create the Meta system user token (`audience-machine/TOKEN_SETUP.md`),
      fill one real client config, dry-run, then first live run (confirms IG + video event names).
- [ ] Submit a real test on the live form → read the Supabase row → run the `00-foundation` prompts on it
      (first true end-to-end loop: form → database → AI → deliverable).
- [ ] Refine each workflow prompt (loop: open folder → run prompt on a real example → improve → save/push).
- [ ] Add teammates as GitHub collaborators; each owns a workflow folder.
- [ ] Build the `orchestrator/` (runs foundation first, then fans the rest out in parallel).
- [ ] Later: point a custom domain (e.g. `forms.eventsalesagency.com`) at the form.

### Update 2026-06-17 — foundation machine + no-approval creative
- **`foundation-machine/` BUILT (machine #2, "the BRAIN").** One command reads a submission
  (Supabase `--latest`/`--client`, or `--sample`), runs the input gate, generates Project
  Summary + Event Summary + TAP (generate->grade->rewrite loop), and writes the **master brain**
  at top-level `master-brain/<client>/` (`MASTER_BRAIN.md` + the 3 docs + RUN_REPORT). Plain
  `requests`, no Node. Needs `ANTHROPIC_API_KEY` in `foundation-machine/.env` (+ Supabase
  service_role key for live data). Default model `claude-opus-4-8`.
- **No-approval creative**: ad scripts (01), ad copy (02), VSL (03) each fan out from the master
  brain and self-grade against a Standard until they pass. Flags `--ad-scripts --ad-copy --vsl
  --all-creative`. Standards: `workflows/0{1,2,3}-*/{AD_SCRIPT,AD_COPY,VSL}_STANDARD.md`. A
  code-checked no-em-dash gate runs on top.
- **Swipe corpora added** (from Malachi's Google Docs) into `workflows/*/examples/`:
  ad-scripts-swipe (122k), ad-copy-swipe, nurture-emails-swipe (54k), nurture email + text
  14-sequences, event-sales-followup-texts, and a 15th approved TAP (Credit Repair Expo).
- **Still needed from Malachi:** VSL example scripts, the ad-script FORMAT doc, and the SOP
  pieces (mentioned but not yet shared) to ground the VSL harder. Email/text nurture are the
  next easy no-approval steps (examples already in place, just need Standards + STEPS entries).

### How to read form submissions
Query Supabase project `hiqlubrygiprmelechza` (use the service_role key or a Supabase Management API token).

### Environment notes
git + GitHub CLI (`gh`) are installed on the owner's Mac. **Node.js is NOT installed** (not needed yet).
Optional future add-on: Playwright MCP would give Claude Code browser control (needs Node + a session restart;
flaky on OAuth/2FA logins).
