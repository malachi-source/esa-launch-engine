# The ESA Audience Machine

A robot employee that never logs out. Point it at one client's Meta ad account
and it builds ESA's entire audience stack (35 audiences: warm engagement
audiences, lookalikes, cold and broad) in a couple of minutes, the same exact
way every single time. Then you do the next client. Or build every client at
once with `run_all.sh`.

This is **machine #1** of ESA's automation set. It is built so the later
fulfillment app can call it as one "build the audiences" workflow step.

---

## What it builds (one run = 35 audiences)

All warm audiences use **365-day retention** (the past year) and ESA naming so
they're easy to spot in Ads Manager.

- **Facebook Page (6):** Engaged, Visited, Clicked CTA, Messaged, Saved Posts,
  Interacted with Video Ad or Reel
- **Instagram (6):** Started Following, Engaged (all), Visited Profile, Engaged
  with Post or Ad, Sent DM, Saved or Liked
- **Video viewers (5):** watched 3 sec / 25% / 50% / 75% / 95% of any video
- **Website (1):** all visitors (Meta caps this at 180 days; the tool clamps it)
- **Contact lists (2):** All GHL Leads + All Past Customers (from CSV, hashed)
- **"ALL Warm Audiences"** saved bundle of everything above
- **Lookalikes (1%)** off the best seeds (CTA clickers, messagers, page likes,
  video/reel, IG followers/engagers/DMs/saves, 50/75/95% viewers, leads, customers)
- **"All Top Lookalikes"** saved bundle
- **Cold:** interests-based audience (15-20 interests from the Target Audience
  Profile, auto-matched to Meta interest IDs)
- **Broad:** open audience, no interests, let Meta find people

---

## First-time setup (once per computer)

```bash
cd audience-machine
./setup.sh
```

That builds a private Python sandbox and installs the two packages it needs.
You only do this once.

You also need a **Meta system user token** (the master key). It does not exist
yet. Follow **TOKEN_SETUP.md** to create it. Then, in the terminal:

```bash
export META_ACCESS_TOKEN="paste-your-token-here"
```

> The token is a master key. It lives ONLY in your terminal as that env var.
> Never paste it into a file, a config, Git, or Slack. If it ever leaks, revoke
> and regenerate it (TOKEN_SETUP.md says how).

---

## Building audiences for a client

```bash
# 1. Make that client's config from the template
cp config/clients/example-client.yml config/clients/acme.yml

# 2. Open config/clients/acme.yml and fill in:
#    - name + slug
#    - the 5 Meta IDs (ad account, page, IG, pixel)
#    - cold_interests  (from the approved Target Audience Profile, section 13)

# 3. PREVIEW first - this creates nothing, just prints the plan
./run.sh config/clients/acme.yml --dry-run

# 4. Build for real
./run.sh config/clients/acme.yml
```

When it finishes, a summary lands in `output/acme-audiences.md`. Paste that into
Slack for the launch checklist.

### All clients at once

```bash
./run_all.sh --dry-run    # preview every client config
./run_all.sh              # build them all
```

---

## It is safe to re-run

Every audience is matched by name. If it already exists, it's **skipped**. So
re-running just fills in whatever was missing. This matters because lookalikes
need ~100+ people in their seed audience; on a brand-new account some won't
build the first day. Just run it again in a few days and only the missing
lookalikes get created.

---

## Honest limitations (real, documented, do not be surprised)

- **Website audiences** are capped at 180 days by Meta. The tool clamps the
  365 down to 180 and tells you.
- **"Interacted with Video Ad or Reel"** has no reliable public API event. The
  tool flags it as a one-time **manual** create in Ads Manager. Once it exists,
  its lookalike builds on the next run.
- **Instagram and video-percentage event names** are best-known guesses, not
  yet confirmed against a live account. The **first live run is the test**:
  anything Meta rejects is reported per-audience, and you fix the one `event:`
  line in `config/warm_audiences.yml` and re-run. Nothing else breaks.
- **Saved audiences** (the cold/broad/rollup "bundles") have spotty API support.
  If Meta rejects one, the tool writes its targeting into the summary file so
  you can paste it into an ad set by hand.
- **Lookalikes** need a seed with enough people. "Seed too small" is normal on
  new accounts; re-run later.
- **New ad accounts** may need the client to accept Meta's custom-audience terms
  once in Ads Manager before any custom audience will build.

The design rule: one rejection never kills the run, and anything Meta might
reject lives in YAML config (not code) so fixes are one line.

---

## Files

```
audience-machine/
  create_audiences.py            the tool (you rarely touch this)
  config/
    warm_audiences.yml           THE MASTER STACK - what gets built (edit here)
    clients/
      example-client.yml         per-client template (copy it)
  output/                        per-run summaries (gitignored)
  setup.sh                       one-time install
  run.sh                         run one client
  run_all.sh                     run every client
  requirements.txt               the 2 Python packages
  README.md                      this file
  TOKEN_SETUP.md                 how to make the Meta token (the only blocker)
```

---

## How this plugs into the bigger system

The tool is a single command with a clean contract:
**input** = one client YAML (IDs + interests) + the `META_ACCESS_TOKEN` env var;
**output** = audiences created in Meta + a machine-readable run report in
`output/`. The eventual fulfillment app runs this right after the Target
Audience Profile is approved (audiences are built *before* the client records
videos, on purpose). Machine #3 (the campaign builder) will consume the
audiences this one creates.
