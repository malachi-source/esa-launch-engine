---
# Text Re-engagement (YES Campaign) — working notes

## What this step does
Generates a re-engagement SMS sequence of [X] texts aimed at older leads. The main goal is to get a YES reply so a sales rep can follow up and close the ticket sale (not necessarily to sell directly in-text). Blends Brunson, Cardone, Gadzhi, and Tai Lopez styles.

## Inputs it needs (from the onboarding form / earlier steps)
- Number of Texts to Generate (10, 20, 30, 50, 75, etc. — user chooses)
- Primary CTA URL
- (Audience/event context informs tone and merge fields like [first_name], [event])

## Output it produces
The chosen number of short texts (1–3 lines, best-friend energy), rotating the 10 SMS archetypes. Most texts end with a YES-style question; mix is 80% YES-style replies / 20% link CTAs.

## Status
- [x] Prompt copied from the master Google Doc
- [ ] Reviewed/refined
- [ ] Tested with a real example

## Notes / decisions
- Compliance toggle: no_em_dashes=[true/false].
- Key distinction vs 05-text-sequence: this targets OLDER/dormant leads and optimizes for a YES reply handed to a rep, rather than a daily nurture-to-purchase cadence.
- Maps to the "30–45 Day Text Re-Engagement Sequence for Older Leads" deliverable in the master SOP.
---
