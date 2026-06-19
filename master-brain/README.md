# master-brain/

The shared memory of a launch. The **foundation-machine** writes one folder per client
here, and every downstream workflow (ad scripts, ad copy, emails, VSL, etc.) reads from it.

```
master-brain/
  <client-slug>/
    project-summary.md
    event-summary.md
    audience-profile.md     <- the TAP
    MASTER_BRAIN.md         <- all three combined (what downstream steps read)
    RUN_REPORT.md           <- what ran + the TAP grade scores
    outputs/                <- fan-out deliverables (ad scripts, etc.)
```

Client folders are git-ignored (they contain real client data). Only this README is tracked.
