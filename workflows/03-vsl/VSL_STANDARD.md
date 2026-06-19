# VSL Standard (pass/fail + scoring rubric)

> The bar EVERY auto-generated VSL must clear. The grader judges output against this;
> the generate -> grade -> rewrite loop REPLACES human approval.
> Inputs come from the client's MASTER_BRAIN (audience profile + event summary + offer).
> Voice: Alex Hormozi if he wrote VSLs. Blunt, proof-heavy, future-focused.

> NOTE: no client VSL examples are in `examples/` yet. Add 1 to 3 approved VSL
> scripts there to ground the voice harder. Until then, model the spoken tone on
> `../01-ad-scripts/examples/ad-scripts-swipe.md` plus the Hormozi method below.

## The goal
A no-human-approval machine: master brain in -> one finished VSL script out,
self-graded until it passes. No person signs off.

## Deliverable
One spoken-word VSL script, 3 to 5 minutes (roughly 450 to 750 words), that moves a
viewer from "curious" to "I need this now" to "buy the ticket."

## REQUIRED sections (in order)
1. **Pain hook (0-45s)** — hit the pain first, make them nod. Do NOT introduce yourself.
2. **Agitate + pattern break (45-90s)** — wasted time, missed deals, lost confidence; use contrast ("staying is more expensive than moving").
3. **Authority without ego (90-150s)** — credibility through facts and proof, not bragging; optional quick "I lived this" story.
4. **Introduce the event (150-210s)** — name, type, dates, city, what it is.
5. **The transformation + what they get** — the single biggest outcome, plus tiers/bonuses.
6. **Crush the top objections** — price, time, skepticism, "will it work for me?"
7. **Offer + urgency** — tiers, price, scarcity (seats, deadline, bonuses expiring).
8. **Strong CTA** — buy the ticket now, one clear action.

## HARD GATES (any failure = auto-fail, rewrite required)
1. Length is a true 3 to 5 minutes spoken (about 450 to 750 words).
2. **Zero em dashes** anywhere (use periods or commas). Checked in code too.
3. Spoken-word voice, Hormozi straight talk (not written/corporate).
4. Does NOT open with a self-introduction. Pain first.
5. Proof-driven (uses the real stats / testimonials / track record from the brain).
6. Meta compliant: no income or health guarantees, no before-and-after, no prohibited attributes, no unrealistic guarantees.
7. Event-anchored: names the real event, dates, city, tiers, and price.
8. Ends with a clear buy-the-ticket CTA.
9. Uses the audience's real language from the master brain.
10. No placeholders or "[fill in]" left anywhere.

## RUBRIC (score each 1-5; ALL must be >= 4 to pass)
1. Hook strength (instant recognition)
2. Agitation + contrast
3. Authority / proof (facts, not bragging)
4. Clarity (blunt and clear)
5. Voice match (sounds like Hormozi)
6. Objection handling
7. Urgency / scarcity
8. CTA strength

## THE LOOP THAT REPLACES APPROVAL
```
generate -> self-grade against gates + rubric -> rewrite anything failing a gate or
scoring under 4 -> repeat -> finish ONLY when all gates pass AND all 8 dimensions
are 4 or 5.
```

## CORE PRINCIPLES
- **Pain first, ego never.**
- **Proof over promises:** lead with facts, stats, real results from the brain.
- **Extract, do not invent:** use the audience's exact words.
- **Anchor to the event** and end on one clear CTA.
- **Compliance is non-negotiable.**
