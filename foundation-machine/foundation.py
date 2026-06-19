#!/usr/bin/env python3
"""
ESA Foundation Machine  (machine #2 — "the BRAIN")
==================================================
Turns ONE client's onboarding submission into the three master reference docs
every other workflow needs, and files them into the MASTER BRAIN:

    master-brain/<client>/project-summary.md
    master-brain/<client>/event-summary.md
    master-brain/<client>/audience-profile.md      (the TAP)
    master-brain/<client>/MASTER_BRAIN.md           (all three, combined)
    master-brain/<client>/RUN_REPORT.md             (what ran + the grade scores)

The Target Audience Profile runs the generate -> grade -> rewrite loop from
workflows/00-foundation/Target_Audience_Profile_Standard.md (10 gates + 8-dim
rubric) instead of waiting for a human to approve it.

You almost never edit this file. The PROMPTS are the source of truth and live in
workflows/00-foundation/*.md — this just feeds them the survey + calls Claude.

Run it:
  ./run.sh --sample                       # use the bundled sample (no Supabase needed)
  ./run.sh --latest                       # read the newest real submission from Supabase
  ./run.sh --client acme-corp             # read one specific client by client_id
  ./run.sh --sample --ad-scripts          # also generate the ad scripts from the brain
  ./run.sh --sample --dry-run             # show the plan, call nothing

Secrets (put them in .env — see .env.example):
  ANTHROPIC_API_KEY            required (calls Claude)
  SUPABASE_SERVICE_ROLE_KEY    only needed for --latest / --client (reading live data)
"""

import argparse
import json
import os
import re
import sys
import warnings

warnings.filterwarnings("ignore")  # hide the harmless old-OpenSSL warning

try:
    import requests
except ImportError:
    sys.exit("Missing 'requests'. Run the one-time setup first:  ./setup.sh")

# -----------------------------------------------------------------------------
# Paths
# -----------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
FOUNDATION = os.path.join(REPO, "workflows", "00-foundation")
EXAMPLES_DIR = os.path.join(FOUNDATION, "examples")
BRAIN_ROOT = os.path.join(REPO, "master-brain")

PROMPT_PROJECT = os.path.join(FOUNDATION, "PROMPT-project-summary.md")
PROMPT_EVENT = os.path.join(FOUNDATION, "PROMPT-event-summary.md")
PROMPT_TAP = os.path.join(FOUNDATION, "PROMPT-audience-profile.md")
TAP_STANDARD = os.path.join(FOUNDATION, "Target_Audience_Profile_Standard.md")
TAP_FORMAT = os.path.join(REPO, "reference", "tap-formatting-standards.md")

# -----------------------------------------------------------------------------
# Tiny .env loader (no extra dependency)
# -----------------------------------------------------------------------------
def load_env():
    path = os.path.join(HERE, ".env")
    if not os.path.exists(path):
        return
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            v = v.strip().strip('"').strip("'")
            if k.strip() and k.strip() not in os.environ:
                os.environ[k.strip()] = v

load_env()

ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://hiqlubrygiprmelechza.supabase.co").rstrip("/")
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")

# The gating fields from the TAP Standard's INPUT GATE. We can't fix a thin
# survey, so we check the submission carries enough signal before generating.
GATE_CONCEPTS = [
    "ideal buyer / who it's for",
    "age / gender / location",
    "their #1 problem (in their words)",
    "5-10 real customer quotes (or uploaded source material)",
    "what they want / their objections",
    "event name, date, city, ticket tiers + prices, backend offer",
]


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def slugify(text):
    text = (text or "client").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "client"


# -----------------------------------------------------------------------------
# Claude API (plain requests — no SDK needed)
# -----------------------------------------------------------------------------
def call_claude(system, user, model, max_tokens):
    if not ANTHROPIC_KEY:
        sys.exit("No ANTHROPIC_API_KEY found. Put it in foundation-machine/.env (see .env.example).")
    r = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": ANTHROPIC_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        json={
            "model": model,
            "max_tokens": max_tokens,
            "system": system,
            "messages": [{"role": "user", "content": user}],
        },
        timeout=900,
    )
    if r.status_code != 200:
        raise RuntimeError(f"Claude API error {r.status_code}: {r.text[:600]}")
    data = r.json()
    return "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text").strip()


# -----------------------------------------------------------------------------
# Get the submission (Supabase REST, or a local JSON file)
# -----------------------------------------------------------------------------
def fetch_from_supabase(client_id=None):
    if not SUPABASE_KEY:
        sys.exit(
            "Reading live submissions needs SUPABASE_SERVICE_ROLE_KEY in .env.\n"
            "Get it: Supabase dashboard -> Project Settings -> API -> service_role (secret).\n"
            "Or test offline with:  ./run.sh --sample"
        )
    q = "select=*&order=submitted_at.desc&limit=1"
    if client_id:
        q = f"select=*&client_id=eq.{client_id}&order=submitted_at.desc&limit=1"
    r = requests.get(
        f"{SUPABASE_URL}/rest/v1/onboarding_submissions?{q}",
        headers={"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"},
        timeout=60,
    )
    if r.status_code != 200:
        raise RuntimeError(f"Supabase error {r.status_code}: {r.text[:400]}")
    rows = r.json()
    if not rows:
        sys.exit("No submissions found in Supabase yet. Submit the live form once, then re-run.")
    return rows[0]


def load_submission(args):
    if args.submission_file or args.sample:
        path = args.submission_file or os.path.join(HERE, "examples", "sample-submission.json")
        return json.loads(read(path))
    return fetch_from_supabase(args.client)


def submission_context(row):
    """Flatten a submission row into one readable block for the prompts."""
    answers = row.get("answers", row)  # local sample may BE the answers
    meta = {k: row.get(k) for k in ("company_name", "email", "event_name", "client_id") if row.get(k)}
    parts = []
    if meta:
        parts.append("TOP-LEVEL FIELDS:\n" + json.dumps(meta, indent=2))
    parts.append("ALL ONBOARDING ANSWERS (JSON):\n" + json.dumps(answers, indent=2, ensure_ascii=False))
    return "\n\n".join(parts), answers, meta


# -----------------------------------------------------------------------------
# Input gate (the one thing the machine can't fix — a thin survey)
# -----------------------------------------------------------------------------
def check_input_gate(answers):
    """Heuristic gate: enough fields answered + at least one rich free-text block
    (stands in for the '5-10 customer quotes' / uploaded source material).
    Returns (ok: bool, notes: list[str])."""
    values = [str(v) for v in (answers.values() if isinstance(answers, dict) else []) if str(v).strip()]
    notes = []
    answered = len(values)
    longest = max((len(v) for v in values), default=0)
    notes.append(f"{answered} fields answered")
    notes.append(f"longest free-text answer = {longest} chars")
    ok = answered >= 12 and longest >= 150
    if not ok:
        notes.append("THIN SURVEY: not enough signal (need richer answers + customer quotes / source material).")
    return ok, notes


# -----------------------------------------------------------------------------
# Generators
# -----------------------------------------------------------------------------
def gen_summary(prompt_path, context, model):
    system = read(prompt_path)
    user = (
        "Here are the client's onboarding inputs from the form.\n\n"
        f"{context}\n\n"
        "Using ONLY this information (do not invent facts; if something is missing, "
        "write 'Not provided'), produce the document exactly as specified above."
    )
    return call_claude(system, user, model, max_tokens=4000)


# -----------------------------------------------------------------------------
# Fan-out step registry. Steps with a "standard" run the no-approval grade loop.
# -----------------------------------------------------------------------------
WORKFLOWS = os.path.join(REPO, "workflows")
STEPS = {
    "01-ad-scripts": {"prompts": ["PROMPT.md"],          "standard": "AD_SCRIPT_STANDARD.md", "label": "Ad Scripts", "max_tokens": 9000},
    "02-ad-copy":    {"prompts": ["PROMPT-ad-copy.md"],  "standard": "AD_COPY_STANDARD.md",   "label": "Ad Copy",    "max_tokens": 6000},
    "03-vsl":        {"prompts": ["PROMPT.md"],          "standard": "VSL_STANDARD.md",       "label": "VSL",        "max_tokens": 6000},
}


def load_examples(examples_dir, n=3, cap=8000):
    if not os.path.isdir(examples_dir):
        return ""
    files = sorted(f for f in os.listdir(examples_dir) if f.endswith(".md"))[:n]
    chunks = []
    for f in files:
        txt = read(os.path.join(examples_dir, f))
        chunks.append(f"### APPROVED EXAMPLE: {f}\n\n{txt[:cap]}")
    return "\n\n---\n\n".join(chunks)


def has_em_dash(text):
    return "—" in text or "–" in text  # em dash or en dash


def estimate_pages(md):
    """Rough page estimate for the TAP page gate (cover + ~520 compact words/page)."""
    words = len(re.findall(r"\S+", md))
    return 1 + max(1, round(words / 520))


def grade(text, standard, context, model):
    """Grade any deliverable against its Standard. Returns the grader's JSON verdict."""
    system = (
        "You are a strict QA grader for ESA deliverables. Grade the deliverable ONLY against "
        "the Standard provided. Respond with ONLY a JSON object, no prose.\n\n"
        "Schema:\n"
        '{ "gates": {"<gate>": true|false, ...},   // one key per HARD GATE in the Standard\n'
        '  "rubric": {"<dimension>": 1-5, ...},     // one key per RUBRIC dimension in the Standard\n'
        '  "passes": true|false,   // true ONLY if every gate is true AND every rubric dim >= 4\n'
        '  "issues": ["short, specific fixes"] }\n\n'
        "THE STANDARD:\n" + standard
    )
    user = f"CLIENT MASTER BRAIN (source of truth):\n{context}\n\nDELIVERABLE TO GRADE:\n{text}"
    raw = call_claude(system, user, model, max_tokens=2000)
    try:
        return json.loads(raw)
    except Exception:
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        if m:
            try:
                return json.loads(m.group(0))
            except Exception:
                pass
    return {"passes": False, "issues": ["grader did not return valid JSON"], "raw": raw[:400]}


def generate_with_loop(system, build_user, context, standard, model, max_loops, max_tokens, extra_checks=None):
    """generate -> grade -> rewrite until it passes the Standard (no human approval).
    build_user(prev, verdict): prev is None on the first pass.
    extra_checks(text) -> list of deterministic issue strings (empty = pass)."""
    text = call_claude(system, build_user(None, None), model, max_tokens)
    grades = []
    for i in range(max_loops):
        verdict = grade(text, standard, context, model)
        if has_em_dash(text):  # deterministic house-style gate
            verdict["passes"] = False
            verdict.setdefault("gates", {})["no_em_dashes (code-checked)"] = False
            verdict.setdefault("issues", []).append("Remove ALL em dashes and en dashes. Use periods or commas.")
        for issue in (extra_checks(text) if extra_checks else []):  # deterministic format gates
            verdict["passes"] = False
            verdict.setdefault("gates", {})["formatting (code-checked)"] = False
            verdict.setdefault("issues", []).append(issue)
        grades.append(verdict)
        if verdict.get("passes") or i == max_loops - 1:
            break
        text = call_claude(system, build_user(text, verdict), model, max_tokens)
    return text, grades


def gen_tap(context, model, max_loops):
    # MANDATORY: content Standard + document formatting Standard, every single time.
    standard = (
        read(TAP_STANDARD)
        + "\n\n# DOCUMENT FORMATTING STANDARDS (MANDATORY - reference/tap-formatting-standards.md)\n\n"
        + read(TAP_FORMAT)
        + "\n\nThese formatting rules are NON-NEGOTIABLE. The profile must fit 5-7 pages "
        "(including cover), keep each section together (never split a section across a page), "
        "and be structured for a branded Fortune 500 layout (cover page, section headers, "
        "tables for demographics/objections, callouts). Write tight. No padding."
    )
    system = read(PROMPT_TAP) + "\n\n# THE STANDARD YOU MUST MEET\n\n" + standard
    examples = load_examples(EXAMPLES_DIR)

    def page_gate(text):
        pages = estimate_pages(text)
        if pages < 5:
            return [f"Too short: ~{pages} pages estimated, need 5-7. Add depth to the required sections."]
        if pages > 7:
            return [f"Too long: ~{pages} pages estimated, need 5-7 (including cover). Tighten and cut padding."]
        return []

    def build_user(prev, verdict):
        if prev is None:
            return (
                "Study these APPROVED, client-delivered profiles. Match this bar and voice "
                "(do not copy their content):\n\n" + examples +
                "\n\n---\n\nNOW build the Target Audience Profile for THIS client, using only "
                "their onboarding answers below. Extract their real words; do not invent the "
                "audience. Hit every required section.\n\n" + context
            )
        return (
            "Here is a Target Audience Profile and the grader's findings. REWRITE it so every "
            "gate passes and every rubric dimension scores 4 or 5. Fix exactly what was flagged. "
            "Keep what already works.\n\n"
            f"GRADER FINDINGS:\n{json.dumps(verdict, indent=2)}\n\nCURRENT PROFILE:\n{prev}\n\n"
            f"CLIENT ANSWERS:\n{context}"
        )
    return generate_with_loop(system, build_user, context, standard, model, max_loops,
                              max_tokens=16000, extra_checks=page_gate)


def run_step(step, brain_dir, model, max_loops):
    """Fan-out a workflow against the master brain. With a Standard -> no-approval grade
    loop; without one -> single pass. Returns (text, grades)."""
    cfg = STEPS.get(step)
    step_dir = os.path.join(WORKFLOWS, step)
    if not os.path.isdir(step_dir):
        sys.exit(f"No such workflow step: {step_dir}")
    prompt_files = (cfg or {}).get("prompts") or sorted(
        f for f in os.listdir(step_dir) if f.startswith("PROMPT") and f.endswith(".md"))
    if not prompt_files:
        sys.exit(f"No PROMPT*.md in {step_dir}")
    prompt_text = "\n\n".join(read(os.path.join(step_dir, p)) for p in prompt_files)
    brain = read(os.path.join(brain_dir, "MASTER_BRAIN.md"))
    examples = load_examples(os.path.join(step_dir, "examples"), n=2, cap=14000)
    max_tokens = (cfg or {}).get("max_tokens", 8000)
    standard_path = os.path.join(step_dir, cfg["standard"]) if cfg and cfg.get("standard") else None

    if standard_path and os.path.exists(standard_path):
        standard = read(standard_path)
        system = prompt_text + "\n\n# THE STANDARD YOU MUST MEET\n\n" + standard

        def build_user(prev, verdict):
            if prev is None:
                return (
                    "Study these APPROVED ESA examples. Match this bar, voice, and structure "
                    "(do not copy their content):\n\n" + (examples or "(no examples on file yet)") +
                    "\n\n---\n\nHere is the client's MASTER BRAIN. Use it as the Audience profile "
                    "and Offer/event details. Produce the deliverable now, hitting every required "
                    "element in the Standard.\n\n" + brain
                )
            return (
                "Here is your draft and the grader's findings. REWRITE so every gate passes and "
                "every rubric dimension scores 4 or 5. Fix exactly what was flagged. Keep what works.\n\n"
                f"GRADER FINDINGS:\n{json.dumps(verdict, indent=2)}\n\nCURRENT DRAFT:\n{prev}\n\n"
                f"MASTER BRAIN:\n{brain}"
            )
        return generate_with_loop(system, build_user, brain, standard, model, max_loops, max_tokens)

    # no standard: single pass, no grading
    user = (
        "Here is the client's MASTER BRAIN (Project Summary + Event Summary + Target Audience "
        "Profile). Use it as the inputs the prompt asks for. Produce the deliverable now.\n\n" + brain
    )
    return call_claude(prompt_text, user, model, max_tokens), []


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="ESA Foundation Machine — build the master brain from a submission.")
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--latest", action="store_true", help="read the newest submission from Supabase")
    src.add_argument("--client", help="read one client by client_id from Supabase")
    src.add_argument("--submission-file", help="path to a local submission JSON")
    src.add_argument("--sample", action="store_true", help="use the bundled sample submission")
    ap.add_argument("--model", default=os.environ.get("FOUNDATION_MODEL", "claude-opus-4-8"))
    ap.add_argument("--max-grade-loops", type=int, default=2, help="TAP grade->rewrite passes (default 2)")
    ap.add_argument("--ad-scripts", action="store_true", help="after foundation, also generate 01-ad-scripts (no-approval loop)")
    ap.add_argument("--ad-copy", action="store_true", help="after foundation, also generate 02-ad-copy (no-approval loop)")
    ap.add_argument("--vsl", action="store_true", help="after foundation, also generate 03-vsl (no-approval loop)")
    ap.add_argument("--all-creative", action="store_true", help="generate ad scripts + ad copy + VSL")
    ap.add_argument("--step", action="append", default=[], help="fan-out step folder to run after foundation (repeatable)")
    ap.add_argument("--strict-gate", action="store_true", help="stop if the input gate fails (default: warn + continue)")
    ap.add_argument("--dry-run", action="store_true", help="show the plan, call nothing")
    args = ap.parse_args()

    if not (args.latest or args.client or args.submission_file or args.sample):
        args.sample = True  # friendliest default

    print("ESA Foundation Machine")
    print("=" * 50)
    row = load_submission(args)
    context, answers, meta = submission_context(row)
    client = slugify(meta.get("company_name") or meta.get("client_id") or meta.get("event_name") or row.get("event_name"))
    brain_dir = os.path.join(BRAIN_ROOT, client)

    ok, gate_notes = check_input_gate(answers)
    print(f"Client:        {client}")
    print(f"Model:         {args.model}")
    print(f"Input gate:    {'PASS' if ok else 'WEAK'}  ({'; '.join(gate_notes)})")
    print(f"Output:        master-brain/{client}/")

    steps = list(args.step)
    if args.ad_scripts or args.all_creative: steps.append("01-ad-scripts")
    if args.ad_copy or args.all_creative: steps.append("02-ad-copy")
    if args.vsl or args.all_creative: steps.append("03-vsl")
    seen = set(); steps = [s for s in steps if not (s in seen or seen.add(s))]  # dedup, keep order
    if args.dry_run:
        print("\n[dry-run] Would generate: Project Summary, Event Summary, Audience Profile (TAP)")
        if steps:
            print(f"[dry-run] Would fan out to: {', '.join(steps)}")
        print("[dry-run] No API calls made.")
        return

    if not ok and args.strict_gate:
        sys.exit("Input gate FAILED and --strict-gate is on. Enrich the survey (esp. customer quotes) and re-run.")

    os.makedirs(brain_dir, exist_ok=True)

    print("\n-> Project Summary ...")
    project = gen_summary(PROMPT_PROJECT, context, args.model)
    print("-> Event Summary ...")
    event = gen_summary(PROMPT_EVENT, context, args.model)
    print(f"-> Target Audience Profile (grade loop up to {args.max_grade_loops}x) ...")
    tap, grades = gen_tap(context, args.model, args.max_grade_loops)
    final = grades[-1] if grades else {}
    print(f"   TAP verdict: {'PASS' if final.get('passes') else 'NEEDS WORK'}  (after {len(grades)} grade pass(es))")

    # write the master brain
    def w(name, text):
        with open(os.path.join(brain_dir, name), "w", encoding="utf-8") as f:
            f.write(text)

    w("project-summary.md", project)
    w("event-summary.md", event)
    w("audience-profile.md", tap)
    w("MASTER_BRAIN.md",
      f"# MASTER BRAIN — {client}\n\n> Auto-generated foundation docs. Every downstream workflow reads from here.\n\n"
      f"---\n\n# PROJECT SUMMARY\n\n{project}\n\n---\n\n# EVENT SUMMARY\n\n{event}\n\n---\n\n# TARGET AUDIENCE PROFILE\n\n{tap}\n")

    # HARD-CODED FORMATTING: always render the branded .docx that physically obeys
    # reference/tap-formatting-standards.md (cantSplit, keepNext, margins, brand colors).
    pages_est = estimate_pages(tap)
    primary, secondary, accent = "1F3A5F", "2E5A88", "C5A253"
    try:
        import render_tap_docx as tapdoc
        primary, secondary, accent = tapdoc.extract_brand_colors(answers)
        title = meta.get("company_name") or client
        subtitle = (meta.get("event_name") or (answers.get("event_name") if isinstance(answers, dict) else "") or "")
        tapdoc.render_markdown(
            tap, os.path.join(brain_dir, "audience-profile.docx"),
            title=title, subtitle=subtitle, meta_lines=["Prepared by Event Sales Agency"],
            primary=primary, secondary=secondary, accent=accent)
        docx_status = f"audience-profile.docx (brand {primary}/{secondary}/{accent})"
        print(f"   Rendered branded .docx -> {docx_status}")
        # authoritative 5-7 page check (LibreOffice if available, else word estimate)
        real_pages, method = tapdoc.verify_pages(os.path.join(brain_dir, "audience-profile.docx"))
        if real_pages is not None:
            verdict_pages = "OK" if 5 <= real_pages <= 7 else "OUT OF RANGE (need 5-7)"
            docx_status += f"; {real_pages} pages [{verdict_pages}] via {method}"
            print(f"   Page check: {real_pages} pages -> {verdict_pages}  ({method})")
        else:
            docx_status += f"; ~{pages_est} pages (estimate; {method})"
            print(f"   Page check: ~{pages_est} pages (estimate; {method})")
    except ImportError:
        docx_status = "SKIPPED (python-docx missing; run ./setup.sh, then re-run)"
        print("   WARNING: python-docx not installed, .docx not rendered. Run ./setup.sh")

    report = [
        f"# Foundation run report — {client}\n",
        f"- Model: `{args.model}`",
        f"- Input gate: {'PASS' if ok else 'WEAK'} ({'; '.join(gate_notes)})",
        f"- TAP grade passes: {len(grades)}  ->  {'PASS' if final.get('passes') else 'NEEDS WORK'}",
    ]
    if final.get("rubric"):
        report.append(f"- TAP rubric: `{json.dumps(final['rubric'])}`")
    if final.get("issues"):
        report.append("- Remaining grader notes:\n" + "\n".join(f"  - {i}" for i in final["issues"]))
    report.append(f"- TAP document (branded): {docx_status}")
    report.append(f"- TAP estimated pages: ~{pages_est} (target 5-7, enforced in the grade loop)")
    report.append("\nFiles written: project-summary.md, event-summary.md, audience-profile.md, audience-profile.docx, MASTER_BRAIN.md")

    fanned = []
    for step in steps:
        label = (STEPS.get(step) or {}).get("label", step)
        graded = step in STEPS
        print(f"-> Fan-out: {label}" + (f" (grade loop up to {args.max_grade_loops}x, no approval) ..." if graded else " ..."))
        out, grades = run_step(step, brain_dir, args.model, args.max_grade_loops)
        verdict = grades[-1] if grades else {}
        if graded:
            print(f"   {label} verdict: {'PASS' if verdict.get('passes') else 'NEEDS WORK'}  (after {len(grades)} grade pass(es))")
        os.makedirs(os.path.join(brain_dir, "outputs"), exist_ok=True)
        with open(os.path.join(brain_dir, "outputs", f"{step}.md"), "w", encoding="utf-8") as f:
            f.write(out)
        note = f"  - {step}: {'PASS' if verdict.get('passes') else ('NEEDS WORK' if grades else 'single pass')}"
        if verdict.get("rubric"):
            note += f"  rubric={json.dumps(verdict['rubric'])}"
        fanned.append(note)
    if fanned:
        report.append("\nFan-out deliverables (master-brain/%s/outputs/):\n%s" % (client, "\n".join(fanned)))

    w("RUN_REPORT.md", "\n".join(report) + "\n")

    print("\nDONE.")
    print(f"Open: master-brain/{client}/MASTER_BRAIN.md")
    if fanned:
        print(f"Ad scripts etc: master-brain/{client}/outputs/")


if __name__ == "__main__":
    main()
