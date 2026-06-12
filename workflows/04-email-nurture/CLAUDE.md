---
# Email Nurture Sequence — working notes

## What this step does
Generates a flexible-length direct-response email follow-up sequence that nurtures new opt-ins toward buying an event ticket. Blends Iman Ghazi, Tai Lopez, Russell Brunson, and Grant Cardone styles, with an optional 14-day template that rebuckets to any chosen length.

## Inputs it needs (from the onboarding form / earlier steps)
- Sender Persona/Name and Role (default: Brian Rand + Founder & CEO)
- Series Length (number of emails/days)
- Event Summary and Target Audience Profile (uploaded; emails built from these)
- Event/Offer Name & Dates, Audience Type, Big Promise, Key Social Proof (if relevant)

## Output it produces
A full email follow-up series (chosen length) following the Brunson+Cardone hybrid guidelines, each email with one core idea, soft→hard CTA, and 5–10 (generator says 8–20) subject lines. Ends with a professional closing.

## Status
- [x] Prompt copied from the master Google Doc
- [ ] Reviewed/refined
- [ ] Tested with a real example

## Notes / decisions
- Token: {{contact.first_name}}. Primary CTA repeated 1–2x max.
- Compliance toggle no_em_dashes=[true/false]; tone sliders default 10.
- 8 built-in archetypes + 14-day template; rebucket arc must include Welcome/Value, Story/Pain, Authority/Proof, Objection Crushers, Transformation, Scarcity, Urgency, Final Call.
- Note: subject line count is inconsistent in source (Generator says 8–20; Generation Step 4 says 5–10) — copied verbatim, not reconciled.
---
