# Foundation Machine (machine #2 — "the BRAIN")

One command turns a client's onboarding submission into the three master docs the
whole launch runs on, files them into the **master brain**, and can fan out to the
downstream steps (ad scripts, etc.).

```
submission (Supabase or sample)
   -> Project Summary
   -> Event Summary
   -> Target Audience Profile   (generate -> grade -> rewrite until it passes)
        -> master-brain/<client>/MASTER_BRAIN.md
             -> ad scripts, ad copy, emails... (fan-out)
```

## One-time setup
```
cd foundation-machine
./setup.sh
open -e .env          # paste your ANTHROPIC_API_KEY, save
```

## Run it
```
./run.sh --sample --all-creative   # full chain on the sample: foundation + ad scripts + ad copy + VSL
./run.sh --sample --ad-scripts     # foundation + just the ad scripts
./run.sh --latest --all-creative   # newest real submission from Supabase (needs service_role key)
./run.sh --client thrive-coaching  # one client by client_id
./run.sh --sample --dry-run        # show the plan, call nothing
```

Output lands in `../master-brain/<client>/` (foundation docs) and `../master-brain/<client>/outputs/` (creative).

## No human approval (ad scripts, ad copy, VSL)
These three steps don't pause for a person. Each one:
1. Reads the client's `MASTER_BRAIN.md` (audience profile + event summary).
2. Loads its workflow's swipe examples (`workflows/<step>/examples/`) and its Standard.
3. Runs **generate -> grade -> rewrite** against the Standard's gates + rubric until it passes
   (`--max-grade-loops`, default 2), plus a hard-coded **no em dash** check.

Standards: `workflows/01-ad-scripts/AD_SCRIPT_STANDARD.md`, `workflows/02-ad-copy/AD_COPY_STANDARD.md`,
`workflows/03-vsl/VSL_STANDARD.md`. Edit a Standard or add examples to change the bar. No code change needed.

## What you need
| Secret | Where it goes | Get it from | Needed for |
|---|---|---|---|
| `ANTHROPIC_API_KEY` | `.env` | console.anthropic.com -> API Keys | always |
| `SUPABASE_SERVICE_ROLE_KEY` | `.env` | Supabase -> Project Settings -> API -> service_role | `--latest` / `--client` only |

Secrets live in `.env`, which is git-ignored. They are never committed.

## Notes
- The PROMPTS are the source of truth in `../workflows/00-foundation/*.md`. This tool
  just feeds them the survey and calls Claude — edit the prompts, not the code.
- The TAP grade loop scores against `Target_Audience_Profile_Standard.md` (10 gates +
  8-dimension rubric). `--max-grade-loops` controls how many rewrite passes (default 2).
- The **input gate**: if the survey is too thin (no customer quotes / source material),
  it warns. Add `--strict-gate` to make it stop instead.
- Model defaults to Opus 4.8. Override with `FOUNDATION_MODEL` in `.env`.
