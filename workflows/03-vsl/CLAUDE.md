---
# VSL (Ultimate Event VSL) — working notes

## What this step does
Generates a Hormozi-style spoken-word Video Sales Letter (3–7 minutes) that moves a viewer from "curious" to "I need this now" to "buy ticket." Follows a fixed flow: Pain Hook → Agitate → Authority → Introduce Event → Future Pace → Objections → Close.

## Inputs it needs (from the onboarding form / earlier steps)
- Audience profile (role, income, age, frustrations, what they want most) — from Target Audience Profile
- Event details (name, type, dates/times w/ timezone, location, capacity) — from Event Summary
- Offer details (GA vs VIP, pricing tiers, bonuses, guarantees, scarcity triggers)
- Transformation promise (single biggest outcome)
- Proof (case studies, stats, testimonials, names, logos, track record)
- Top objections (price, time, skepticism, "will it work for me?")
- Language already used in ads / by the audience

## Output it produces
A complete 3–7 minute VSL script in conversational spoken voice with bold section hooks, embedded NLP commands (3+), proof, urgency, scarcity, identity framing, and a clear repeatable CTA. Optionally 2–3 hook variations for split testing.

## Status
- [x] Prompt copied from the master Google Doc
- [ ] Reviewed/refined
- [ ] Tested with a real example

## Notes / decisions
- Compliance toggle no_em_dashes=[true/false]; tone sliders Directness/Warmth/Urgency default to 10.
- Compliance-safe: no exaggerated income/health claims, no "before & after" promises.
- "Do not include section titles" in the delivered script.
---
