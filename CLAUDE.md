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
- `form/` — the new onboarding form (later phase).
- `orchestrator/` — the engine that runs workflows in the right order (later phase).
- `reference/` — SOPs, the swipe files, audit checklists, anything shared.

## How the team works (we are non-coders directing Claude Code)

- Each person OWNS one or more workflow folders and perfects the prompt there.
- Work happens inside your own folder, so we rarely collide.
- Each person works on their own **branch**; Claude Code handles all git for you.
- At the END of every session, tell Claude: "update this folder's CLAUDE.md with what we did
  and what's left." That's how we never lose progress between chats.

## Source of truth for the prompts

Master prompt library (Google Doc): id `1hUHbuSIrJ6DrkNFDuNhS1vKvzOuZOdbuYFoPsN0NL-Q`.
~22 prompts. House style: model Tai Lopez / Russell Brunson / Grant Cardone / Iman Ghazi
(Hormozi for the VSL), Meta-compliant, NO em dashes, spoken one-person voice, tone sliders.

## Status

- [x] Project scoped, prompt library reviewed, folder structure created.
- [ ] Prompts copied from the Google Doc into each workflow folder.
- [ ] Pushed to GitHub as the shared team repo.
- [ ] First workflow refined end-to-end as the template for the others.
- [ ] Onboarding form built.
- [ ] Orchestrator built.
