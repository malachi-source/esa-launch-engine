---
# Text Sequence (SMS Nurture) — working notes

## What this step does
Generates a short-form SMS/text nurture sequence (14–30 days) that turns interested-but-not-buying warm leads into event ticket buyers (ideally VIP). Blends Brunson, Cardone, Gadzhi, and Tai Lopez styles. Includes a 14-day core structure with 21–30 day extensions.

## Inputs it needs (from the onboarding form / earlier steps)
- Sender Persona/Name and Role (default: Brian Rand + Founder & CEO)
- Series Length
- CTA URL (→ EventName.com)
- Event Summary and Target Audience Profile (uploaded; texts built from these)

## Output it produces
A numbered daily SMS sequence (14-day default or expanded), each text max 2–3 short lines / under 300 chars, following Hook → Value → Future Pace → Proof → CTA, drawing from the archetype library, escalating value → authority/proof → scarcity/urgency.

## Status
- [x] Prompt copied from the master Google Doc
- [ ] Reviewed/refined
- [ ] Tested with a real example

## Notes / decisions
- Token: {{contact.first_name}}. Texts daily; CTA links every 3rd day to avoid link fatigue.
- Toggles: no_em_dashes; link_frequency=[every_other/every_day/final_days_only]; tone=[friendly/urgent/bold/challenger].
- Source has "Event Summer" (typo for Event Summary) and mojibake in CTA bullets (ð) — cleaned the mojibake to → arrows in PROMPT.md; left "Event Summer" verbatim.
---
