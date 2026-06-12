#!/usr/bin/env python3
"""
ESA Audience Machine
====================
Builds the full ESA audience stack inside ONE client's Meta ad account by
talking straight to the Meta Marketing (Graph) API.

You almost never edit this file. WHAT gets built lives in
  config/warm_audiences.yml   (the master stack, same for every client)
WHO it gets built for lives in
  config/clients/<client>.yml  (that client's account IDs + interests)

Run it:
  export META_ACCESS_TOKEN="your-system-user-token"
  python create_audiences.py config/clients/acme.yml --dry-run   # show the plan
  python create_audiences.py config/clients/acme.yml             # build for real

It is SAFE TO RE-RUN. Anything that already exists (matched by name) is skipped,
so a second run just backfills whatever was missing (e.g. lookalikes once their
seed audience has enough people).

Nothing ever stops the whole run: if Meta rejects one audience, that one is
reported as FAILED and the tool keeps going. A summary is written to
  output/<client>-audiences.md
which you can paste straight into Slack for the launch checklist.
"""

import argparse
import hashlib
import json
import os
import sys
import warnings

# The system Python ships an old OpenSSL; requests/urllib3 prints a scary (but
# harmless) warning about it. Hide it so the team never sees red text.
warnings.filterwarnings("ignore")

try:
    import requests
    import yaml
except ImportError:
    sys.exit(
        "Missing Python packages. Run the one-time setup first:\n"
        "  ./setup.sh        (or:  python3 -m pip install requests pyyaml)\n"
    )

# -----------------------------------------------------------------------------
# Config / constants
# -----------------------------------------------------------------------------
API_VERSION = os.environ.get("META_API_VERSION", "v23.0")
GRAPH = f"https://graph.facebook.com/{API_VERSION}"
TOKEN = os.environ.get("META_ACCESS_TOKEN", "")
DAY = 86400  # seconds in a day

HERE = os.path.dirname(os.path.abspath(__file__))
MASTER_PATH = os.path.join(HERE, "config", "warm_audiences.yml")
OUTPUT_DIR = os.path.join(HERE, "output")


# -----------------------------------------------------------------------------
# Tiny console helpers (plain, readable output for non-coders)
# -----------------------------------------------------------------------------
def info(msg):
    print(msg)


def ok(msg):
    print(f"  [OK]   {msg}")


def skip(msg):
    print(f"  [skip] {msg}")


def fail(msg):
    print(f"  [FAIL] {msg}")


# -----------------------------------------------------------------------------
# Graph API plumbing
# -----------------------------------------------------------------------------
def graph(method, path, params=None, data=None):
    """One Graph API call. Returns (json_or_None, error_string_or_None).

    Never raises for an API rejection: the caller decides what to do so a
    single bad audience can't kill the whole run.
    """
    url = f"{GRAPH}/{path}"
    params = dict(params or {})
    params["access_token"] = TOKEN
    try:
        resp = requests.request(method, url, params=params, data=data, timeout=60)
    except requests.RequestException as e:
        return None, f"network error: {e}"
    try:
        body = resp.json()
    except ValueError:
        return None, f"non-JSON response (HTTP {resp.status_code}): {resp.text[:200]}"
    if resp.status_code >= 400 or "error" in body:
        err = body.get("error", {})
        msg = err.get("error_user_msg") or err.get("message") or json.dumps(body)[:300]
        return None, msg
    return body, None


def get_existing(act_id):
    """Map of {name: id} for custom + saved audiences already in the account.

    Drives idempotency: if a name already exists we skip creating it.
    """
    existing = {}
    for edge in ("customaudiences", "saved_audiences"):
        after = None
        while True:
            params = {"fields": "id,name", "limit": 200}
            if after:
                params["after"] = after
            body, err = graph("GET", f"{act_id}/{edge}", params=params)
            if err:
                # Not fatal: worst case we try to create and Meta rejects dupes.
                info(f"  (could not list existing {edge}: {err})")
                break
            for row in body.get("data", []):
                if row.get("name"):
                    existing[row["name"]] = row["id"]
            after = body.get("paging", {}).get("cursors", {}).get("after")
            if not after or not body.get("data"):
                break
    return existing


# -----------------------------------------------------------------------------
# Rule builders
# -----------------------------------------------------------------------------
def engagement_rule(source_type, object_id, event, retention_seconds):
    """Build the 'rule' for an engagement / website custom audience."""
    src = {"event_sources": [{"type": source_type, "id": object_id}],
           "retention_seconds": retention_seconds}
    if event:
        src["filter"] = {"operator": "and",
                         "filters": [{"field": "event", "operator": "=", "value": event}]}
    return {"inclusions": {"operator": "or", "rules": [src]}}


def client_object_id(client, which):
    """Resolve object: page|ig|pixel -> the client's actual id."""
    return {
        "page": client.get("page_id"),
        "ig": client.get("ig_id"),
        "pixel": client.get("pixel_id"),
    }.get(which)


# -----------------------------------------------------------------------------
# Creators (each returns the new audience id, or None on skip/fail)
# -----------------------------------------------------------------------------
def create_engagement_audience(act_id, spec, client, existing, retention_default,
                               website_cap, dry_run, report):
    name = spec["name"]
    if name in existing:
        skip(f"{name} (already exists)")
        report.append((name, "skip", "already exists"))
        return existing[name]

    if spec.get("manual"):
        fail(f"{name} (NO API - create this one by hand once, see README)")
        report.append((name, "manual", "no public API event; create manually once"))
        return None

    object_id = client_object_id(client, spec.get("object", "page"))
    if not object_id:
        fail(f"{name} (client is missing the '{spec.get('object')}' id)")
        report.append((name, "fail", f"missing {spec.get('object')}_id in client file"))
        return None

    days = spec.get("retention_days", retention_default)
    kind = spec.get("kind", "engagement")
    subtype = "WEBSITE" if kind == "website" else "ENGAGEMENT"
    if kind == "website" and days > website_cap:
        info(f"  (clamping {name} retention {days}d -> {website_cap}d, Meta website cap)")
        days = website_cap

    rule = engagement_rule(spec["source_type"], object_id, spec.get("event"), days * DAY)
    verified_note = "" if spec.get("verified", True) else "  [unverified event name]"

    if dry_run:
        ok(f"WOULD CREATE {name} ({subtype}, {days}d){verified_note}")
        report.append((name, "would-create", f"{subtype} {days}d"))
        return f"DRYRUN::{name}"

    body, err = graph("POST", f"{act_id}/customaudiences", data={
        "name": name,
        "subtype": subtype,
        "rule": json.dumps(rule),
    })
    if err:
        fail(f"{name}: {err}{verified_note}")
        report.append((name, "fail", err))
        return None
    ok(f"{name}{verified_note}")
    report.append((name, "created", body.get("id", "")))
    return body.get("id")


def create_contact_audience(act_id, spec, client, existing, dry_run, report):
    name = spec["name"]
    if name in existing:
        skip(f"{name} (already exists)")
        report.append((name, "skip", "already exists"))
        return existing[name]

    csv_key = spec.get("csv")
    csv_path = (client.get("csv_files") or {}).get(csv_key)
    if not csv_path:
        skip(f"{name} (no CSV provided in client file -> skipped)")
        report.append((name, "skip", f"no csv path for '{csv_key}'"))
        return None
    if not os.path.isabs(csv_path):
        csv_path = os.path.join(HERE, csv_path)
    if not os.path.exists(csv_path):
        fail(f"{name}: CSV not found at {csv_path}")
        report.append((name, "fail", f"csv not found: {csv_path}"))
        return None

    rows = read_contacts(csv_path)
    if not rows:
        fail(f"{name}: CSV had no usable email/phone rows")
        report.append((name, "fail", "csv empty / no email or phone columns"))
        return None

    if dry_run:
        ok(f"WOULD CREATE {name} (CUSTOM list, {len(rows)} hashed rows from {os.path.basename(csv_path)})")
        report.append((name, "would-create", f"contact list, {len(rows)} rows"))
        return f"DRYRUN::{name}"

    body, err = graph("POST", f"{act_id}/customaudiences", data={
        "name": name,
        "subtype": "CUSTOM",
        "customer_file_source": "USER_PROVIDED_ONLY",
    })
    if err:
        fail(f"{name}: {err}")
        report.append((name, "fail", err))
        return None
    aud_id = body.get("id")

    added, up_err = upload_contacts(aud_id, rows)
    if up_err:
        fail(f"{name}: created but upload failed: {up_err}")
        report.append((name, "fail", f"created {aud_id} but upload failed: {up_err}"))
        return aud_id
    ok(f"{name} (uploaded {added} hashed rows)")
    report.append((name, "created", f"{aud_id} ({added} rows)"))
    return aud_id


def read_contacts(csv_path):
    """Return list of (email_or_None, phone_or_None) from a CSV. Tolerant of
    column naming: anything with 'email' or 'phone'/'mobile' in the header."""
    import csv as _csv
    rows = []
    with open(csv_path, newline="", encoding="utf-8-sig", errors="ignore") as fh:
        reader = _csv.DictReader(fh)
        if not reader.fieldnames:
            return rows
        emap = next((c for c in reader.fieldnames if "email" in c.lower()), None)
        pmap = next((c for c in reader.fieldnames
                     if "phone" in c.lower() or "mobile" in c.lower()), None)
        for r in reader:
            email = (r.get(emap) or "").strip().lower() if emap else ""
            phone = (r.get(pmap) or "").strip() if pmap else ""
            phone = "".join(ch for ch in phone if ch.isdigit())  # digits only
            if email or phone:
                rows.append((email or None, phone or None))
    return rows


def _sha256(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def upload_contacts(aud_id, rows, batch=8000):
    """SHA-256 hash + upload contacts in batches to the audience's users edge."""
    total = 0
    for i in range(0, len(rows), batch):
        chunk = rows[i:i + batch]
        data = [[_sha256(e) if e else "", _sha256(p) if p else ""] for (e, p) in chunk]
        payload = {"schema": ["EMAIL", "PHONE"], "data": data}
        _, err = graph("POST", f"{aud_id}/users",
                       data={"payload": json.dumps(payload)})
        if err:
            return total, err
        total += len(chunk)
    return total, None


def create_lookalike(act_id, seed_id, seed_name, country, ratio, existing, dry_run, report):
    name = f"ESA - LAL 1% - {seed_name.replace('ESA - ', '')}"
    if name in existing:
        skip(f"{name} (already exists)")
        report.append((name, "skip", "already exists"))
        return existing[name]
    if not seed_id or str(seed_id).startswith("DRYRUN::"):
        if dry_run:
            ok(f"WOULD CREATE {name} (1% LAL of {seed_name})")
            report.append((name, "would-create", f"1% LAL of {seed_name}"))
        else:
            skip(f"{name} (seed not available yet -> re-run later)")
            report.append((name, "skip", "seed not created yet"))
        return None

    body, err = graph("POST", f"{act_id}/customaudiences", data={
        "name": name,
        "subtype": "LOOKALIKE",
        "origin_audience_id": seed_id,
        "lookalike_spec": json.dumps({"type": "custom_ratio", "ratio": ratio,
                                      "country": country}),
    })
    if err:
        # Most common cause: seed has < ~100 people yet. Not a real failure.
        fail(f"{name}: {err}  (often just 'seed too small yet' - re-run later)")
        report.append((name, "fail", err))
        return None
    ok(name)
    report.append((name, "created", body.get("id", "")))
    return body.get("id")


def create_saved_targeting(act_id, name, targeting, existing, dry_run, report):
    if name in existing:
        skip(f"{name} (already exists)")
        report.append((name, "skip", "already exists"))
        return existing[name]
    if dry_run:
        ok(f"WOULD CREATE saved audience: {name}")
        report.append((name, "would-create", "saved audience"))
        return f"DRYRUN::{name}"
    body, err = graph("POST", f"{act_id}/saved_audiences", data={
        "name": name,
        "targeting": json.dumps(targeting),
    })
    if err:
        # Saved-audience API support is spotty. Don't lose the work: write the
        # spec so it can be pasted into an ad set by hand.
        fail(f"{name}: {err} (targeting spec saved to summary for manual paste)")
        report.append((name, "fail-spec", json.dumps(targeting)))
        return None
    ok(name)
    report.append((name, "created", body.get("id", "")))
    return body.get("id")


def resolve_interests(names):
    """Turn interest words into Meta interest {id,name}. Returns (found, misses)."""
    found, misses = [], []
    for raw in names:
        q = raw.strip()
        if not q:
            continue
        body, err = graph("GET", "search", params={
            "type": "adinterest", "q": q, "limit": 1})
        if err or not body.get("data"):
            misses.append(q)
            continue
        hit = body["data"][0]
        found.append({"id": hit["id"], "name": hit["name"]})
    return found, misses


# -----------------------------------------------------------------------------
# Summary writer
# -----------------------------------------------------------------------------
def write_summary(client, report, interest_misses, dry_run):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    slug = client.get("slug") or client.get("name", "client").lower().replace(" ", "-")
    path = os.path.join(OUTPUT_DIR, f"{slug}-audiences.md")
    counts = {}
    for _, status, _ in report:
        counts[status] = counts.get(status, 0) + 1
    lines = []
    lines.append(f"# Audience build - {client.get('name', slug)}")
    lines.append("")
    lines.append(("DRY RUN (nothing was created)" if dry_run else "LIVE RUN"))
    lines.append("")
    lines.append("## Summary")
    for status in ("created", "would-create", "skip", "manual", "fail", "fail-spec"):
        if status in counts:
            lines.append(f"- {status}: {counts[status]}")
    lines.append("")
    lines.append("## Detail")
    lines.append("| Audience | Status | Notes / ID |")
    lines.append("|---|---|---|")
    for name, status, note in report:
        note = (note or "").replace("|", "/")
        if len(note) > 120:
            note = note[:117] + "..."
        lines.append(f"| {name} | {status} | {note} |")
    if interest_misses:
        lines.append("")
        lines.append("## Cold interests Meta could NOT match (fix names in client file)")
        for m in interest_misses:
            lines.append(f"- {m}")
    text = "\n".join(lines) + "\n"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return path


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Build the ESA audience stack for one client.")
    ap.add_argument("client_config", help="path to config/clients/<client>.yml")
    ap.add_argument("--dry-run", action="store_true",
                    help="show exactly what WOULD be built, create nothing")
    args = ap.parse_args()

    if not os.path.exists(args.client_config):
        sys.exit(f"Client config not found: {args.client_config}")
    if not os.path.exists(MASTER_PATH):
        sys.exit(f"Master stack not found: {MASTER_PATH}")
    if not TOKEN and not args.dry_run:
        sys.exit("META_ACCESS_TOKEN is not set. Run:\n"
                 '  export META_ACCESS_TOKEN="your-system-user-token"\n'
                 "(or use --dry-run to preview without a token)")

    with open(MASTER_PATH) as fh:
        master = yaml.safe_load(fh)
    with open(args.client_config) as fh:
        client = yaml.safe_load(fh)

    s = master.get("settings", {})
    retention_default = s.get("retention_days_default", 365)
    website_cap = s.get("website_retention_cap_days", 180)
    ratio = s.get("lookalike_ratio", 0.01)
    country = (client.get("country") or "US").upper()

    act = str(client.get("ad_account_id", "")).replace("act_", "")
    if not act:
        sys.exit("Client file is missing ad_account_id.")
    act_id = f"act_{act}"

    info("=" * 70)
    info(f"ESA Audience Machine   ({'DRY RUN' if args.dry_run else 'LIVE'})   API {API_VERSION}")
    info(f"Client: {client.get('name')}   Account: {act_id}   LAL country: {country}")
    info("=" * 70)

    existing = {} if args.dry_run else get_existing(act_id)
    if existing:
        info(f"Found {len(existing)} existing audiences (these will be skipped).")

    report = []
    name_to_id = {}        # warm audience name -> id (for rollups + lookalikes)
    lookalike_ids = []     # built lookalike ids (for the lookalike rollup)
    rollup_warm_ids = []   # warm custom ids that belong in the warm rollup

    # 1) Warm custom audiences (engagement + website + contact lists)
    info("\n-- Warm custom audiences --")
    for spec in master.get("warm_audiences", []):
        kind = spec.get("kind", "engagement")
        if kind == "contact_list":
            aid = create_contact_audience(act_id, spec, client, existing, args.dry_run, report)
        else:
            aid = create_engagement_audience(act_id, spec, client, existing,
                                             retention_default, website_cap,
                                             args.dry_run, report)
        if aid:
            name_to_id[spec["name"]] = aid
            if spec.get("in_rollup", True):
                rollup_warm_ids.append(aid)

    # 2) "ALL Warm Audiences" rollup (saved audience pointing at the customs)
    info("\n-- Saved rollups --")
    rollups = {r.get("includes"): r.get("name") for r in master.get("rollups", [])}
    if "warm" in rollups and rollup_warm_ids:
        real_ids = [i for i in rollup_warm_ids if not str(i).startswith("DRYRUN::")]
        targeting = {"geo_locations": {"countries": [country]},
                     "custom_audiences": [{"id": i} for i in real_ids] or [{"id": "DRYRUN"}]}
        create_saved_targeting(act_id, rollups["warm"], targeting, existing, args.dry_run, report)

    # 3) Lookalikes from every lal_seed audience
    info("\n-- Lookalikes (1%) --")
    for spec in master.get("warm_audiences", []):
        if not spec.get("lal_seed"):
            continue
        seed_id = name_to_id.get(spec["name"]) or existing.get(spec["name"])
        lid = create_lookalike(act_id, seed_id, spec["name"], country, ratio,
                               existing, args.dry_run, report)
        if lid:
            lookalike_ids.append(lid)

    # 4) "All Top Lookalikes" rollup
    if "lookalikes" in rollups and lookalike_ids:
        real_ids = [i for i in lookalike_ids if not str(i).startswith("DRYRUN::")]
        targeting = {"geo_locations": {"countries": [country]},
                     "custom_audiences": [{"id": i} for i in real_ids] or [{"id": "DRYRUN"}]}
        create_saved_targeting(act_id, rollups["lookalikes"], targeting, existing,
                               args.dry_run, report)

    # 5) Cold (interests) + Broad (open) saved audiences
    info("\n-- Cold + Broad saved audiences --")
    saved = master.get("saved_audiences", {})
    name_client = client.get("name", "Client")
    interest_misses = []

    cold_interests = client.get("cold_interests") or []
    if "cold" in saved and cold_interests:
        if args.dry_run:
            ok(f"WOULD resolve {len(cold_interests)} interests + build cold audience")
            report.append((saved["cold"]["name"].format(client=name_client),
                           "would-create", f"{len(cold_interests)} interests"))
        else:
            found, interest_misses = resolve_interests(cold_interests)
            if found:
                targeting = {
                    "geo_locations": {"countries": [country]},
                    "age_min": client.get("age_min", 18),
                    "age_max": client.get("age_max", 65),
                    "flexible_spec": [{"interests": found}],
                }
                create_saved_targeting(act_id, saved["cold"]["name"].format(client=name_client),
                                       targeting, existing, False, report)
            else:
                fail("Cold audience: none of the interests matched Meta - check names")
                report.append((saved["cold"]["name"].format(client=name_client),
                               "fail", "no interests matched"))
    elif "cold" in saved:
        skip("Cold audience (no cold_interests in client file)")

    if "broad" in saved:
        targeting = {"geo_locations": {"countries": [country]},
                     "age_min": client.get("age_min", 18),
                     "age_max": client.get("age_max", 65)}
        create_saved_targeting(act_id, saved["broad"]["name"].format(client=name_client),
                               targeting, existing, args.dry_run, report)

    # 6) Summary file
    path = write_summary(client, report, interest_misses, args.dry_run)
    info("\n" + "=" * 70)
    created = sum(1 for _, st, _ in report if st == "created")
    would = sum(1 for _, st, _ in report if st == "would-create")
    failed = sum(1 for _, st, _ in report if st.startswith("fail"))
    skipped = sum(1 for _, st, _ in report if st in ("skip", "manual"))
    if args.dry_run:
        info(f"DRY RUN complete: {would} would be created, {skipped} skipped/manual.")
    else:
        info(f"LIVE run complete: {created} created, {skipped} skipped/manual, {failed} failed.")
    info(f"Summary written to: {path}")
    info("Paste that file into Slack for the launch checklist.")
    info("=" * 70)


if __name__ == "__main__":
    main()
