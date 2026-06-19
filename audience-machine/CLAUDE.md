# audience-machine — workflow notes

> Read README.md for the operating manual. This file is the quick status/decisions/TODO.

## What it does
Machine #1 of ESA's automation set. One command builds a client's full Meta
audience stack (35 audiences) via the Marketing API. Maps to the prompt-library
steps "09 Warm Audiences SOP" + "10 Lookalike Audiences SOP", plus cold/broad.
Runs right AFTER the Target Audience Profile is approved, BEFORE the client
records videos (deliberate ordering).

## Inputs / outputs (the contract for the orchestrator)
- IN: one `config/clients/<client>.yml` (5 Meta IDs + cold interests + optional
  CSV paths) and the `META_ACCESS_TOKEN` env var.
- OUT: audiences created in Meta + a run report at `output/<slug>-audiences.md`.
- Cold interests come from the approved Target Audience Profile, section 13
  ("Where To Reach Them").

## Status (2026-06-12)
- BUILT and dry-run tested end to end (34 would-create on the example client).
- NEVER run live yet. The only blocker is the Meta system user token, which
  does not exist yet — see TOKEN_SETUP.md.
- Tool compiles clean; venv setup + dry-run both verified on the owner's Mac.

## Key decisions
- WHAT-to-build lives in `config/warm_audiences.yml` (YAML), never in code, so a
  Meta rejection is a one-line fix. WHO-for lives in `config/clients/*.yml`.
- Idempotent: skip-by-name, safe to re-run (backfills lookalikes once seeds fill).
- One rejection never kills the run; everything is reported per-audience.
- Stdlib + `requests` + `pyyaml` only, in a local `.venv`. No Node needed.

## Known unverified bits (the first LIVE run is the test)
- Instagram event names (`ig_business_profile_*`) and video-% names
  (`video_view_25_percent` …) are best guesses. Fix any Meta rejects in
  `warm_audiences.yml`, re-run.
- "Interacted with Video Ad or Reel": no public API event → flagged `manual`,
  create once by hand, its lookalike builds next run.
- Saved audiences (cold/broad/rollups): spotty API support; on reject the
  targeting spec is written to the summary for manual paste.

## TODO
- [ ] Brian's team creates the system user token (TOKEN_SETUP.md).
- [ ] Pick one real client, fill their config, dry-run together.
- [ ] First LIVE run → confirm/fix IG + video event names in the YAML.
- [ ] Add the 2-min "assign assets to system user" step to client onboarding.
- [ ] Later: have the orchestrator call this as the "build audiences" step;
      machine #3 (campaign builder) consumes these audiences.
