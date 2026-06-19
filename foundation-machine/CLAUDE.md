# foundation-machine — working notes

## What it does
Machine #2 ("the BRAIN" from the TAP Standard). Reads ONE onboarding submission and
generates the three foundation docs (Project Summary, Event Summary, Target Audience
Profile) into `../master-brain/<client>/`, then optionally fans out to downstream
workflow steps (e.g. `01-ad-scripts`). The TAP runs the generate->grade->rewrite loop
against `../workflows/00-foundation/Target_Audience_Profile_Standard.md`.

## The contract (for the orchestrator later)
- IN: a submission (Supabase `onboarding_submissions` row, or a local JSON) + `ANTHROPIC_API_KEY`.
- OUT: `master-brain/<client>/{project-summary,event-summary,audience-profile,MASTER_BRAIN}.md`
  + `RUN_REPORT.md`, and `outputs/<step>.md` for any fan-out steps.

## Key decisions
- Plain `requests` to the Anthropic Messages API + Supabase REST. No SDK, no Node.
- Prompts stay the source of truth in `workflows/00-foundation/` — the machine reads
  them at runtime. Editing a prompt changes behavior with zero code changes.
- The master brain is one folder per client; downstream steps read `MASTER_BRAIN.md`.
- Model default = `claude-opus-4-8` (best for these high-value docs).

## Status (built this session)
- [x] Reads submission (Supabase `--latest`/`--client`, or `--sample`/`--submission-file`)
- [x] Input gate (heuristic — warns on thin surveys; `--strict-gate` to enforce)
- [x] Project Summary + Event Summary generation
- [x] TAP generate -> grade -> rewrite loop (scores gates + 8-dim rubric)
- [x] Writes master brain + run report
- [x] **No-approval creative fan-out**: ad scripts (01), ad copy (02), VSL (03) each run the
      generate -> grade -> rewrite loop against their own Standard + swipe examples, plus a
      code-checked no-em-dash gate. Flags: `--ad-scripts --ad-copy --vsl --all-creative`.
      Generic `run_step()` + `STEPS` registry; grader is generic (reads each Standard).
- [x] **TAP formatting standards HARD-CODED every run** (2026-06-18):
      1. PROMPT: `reference/tap-formatting-standards.md` is appended to the TAP system prompt every time.
      2. GRADE LOOP: the grader judges against content + formatting standards; plus deterministic
         code gates (`has_em_dash` + `estimate_pages` 5-7 page gate via `extra_checks`).
      3. RENDERER: `render_tap_docx.py` builds `audience-profile.docx` every run, applying the
         python-docx rules in code (cantSplit on all rows, keepNext/keepLines per section released
         on the last element, margins 0.6/0.5/0.85, brand colors from form fields 48-50, navy table
         headers + alternating shading, gold accent bars, dark callouts, branded cover page).
- [ ] First live run on a real Supabase submission (needs service_role key + a real submission)
- [ ] Exact page-count verification: estimate is word-count based. For a true 5-7 check, render
      the .docx -> PDF via LibreOffice headless (`soffice`) and count pages. Not installed yet.

## The no-approval engine (how it generalizes)
- `STEPS` maps a workflow folder to its prompt(s) + Standard + max_tokens.
- `run_step()` loads the step's `examples/` + `<STANDARD>.md`, then `generate_with_loop()`
  runs generate -> grade -> rewrite until the grader returns `passes: true`.
- To make a NEW step no-approval: add a `*_STANDARD.md` + `examples/` in its folder and an
  entry in `STEPS`. That's it. Email/text nurture are next candidates (examples already added).

## TODO / known gaps
- Input gate is a heuristic (field-count + longest-answer). Precise mapping of the
  Standard's gating fields (A1, B7, ...) to the form's question keys is still to do
  (the Standard calls this `Onboarding_Audience_Questions.md`). Once mapped, tighten
  `check_input_gate`.
- No PDF render yet (Standard's RENDERER step) and no Drive/Slack post (OUTPUT step).
- Avatar count should follow the offer (1 per tier/buyer type). Currently the prompt +
  Standard instruct the model; not enforced in code.
