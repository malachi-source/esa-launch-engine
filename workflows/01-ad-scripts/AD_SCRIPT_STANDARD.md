# Ad Script Standard (pass/fail + scoring rubric)

> The bar EVERY auto-generated set of ad scripts must clear. The grader judges
> output against this; the generate -> grade -> rewrite loop REPLACES human approval.
> Model all output on `examples/ad-scripts-swipe.md` (ESA's real, used ad scripts).
> Inputs come from the client's MASTER_BRAIN (audience profile + event summary).

## The goal
A no-human-approval machine: master brain in -> 10 finished video ad scripts out,
self-graded until they pass. No person signs off.

## Deliverable
10 unique video ad scripts, each 45 to 60 seconds spoken (roughly 90 to 160 words).

## REQUIRED elements (every script)
1. **Scroll-stopping pain hook** in the first line. No "Hi, my name is."
2. **Speaks to ONE person** ("you"), spoken-word, casual and human.
3. **Empathy + quick credibility** (a relatable "I worked with people just like you" or a result).
4. **A shift / mechanism** — the insight or system that reframes their problem.
5. **Sell the after** — the identity-level transformation, not just features.
6. **Event-anchored CTA** — names the real event, and drives to register/secure a seat with urgency or scarcity.

## SET-level requirement (across the 10)
- 10 genuinely DISTINCT angles, not 10 rewordings of one idea.
- Spread across the three styles: Tai Lopez (curiosity/story), Russell Brunson (frameworks/epiphany), Grant Cardone (authority/urgency).
- Varied hooks (pain, curiosity, callout, question, contrarian).

## HARD GATES (any failure = auto-fail, rewrite required)
1. Exactly 10 scripts.
2. **Zero em dashes** anywhere (use periods or commas). This is checked in code too.
3. Every script speaks to one person ("you"), never "you all" / "everyone."
4. No script opens with a self-introduction ("Hi, my name is", "I'm X and").
5. Meta compliant: no prohibited personal attributes ("you are broke", "you have debt"), no income or health guarantees, no before-and-after claims, no unrealistic guarantees.
6. Each script names the real event and ends with a clear CTA.
7. Uses the audience's REAL language from the master brain (verbatim phrases where possible).
8. Each script reads as natural spoken word and fits 45 to 60 seconds.
9. The 10 are distinct angles (no near-duplicates).
10. No placeholders or "[fill in]" left anywhere.

## RUBRIC (score each 1-5; ALL must be >= 4 to pass)
1. Hook strength (stops the scroll)
2. Voice match (sounds like the real customer, not corporate)
3. Pain resonance (they feel seen)
4. Desire / identity pull (sells the after)
5. Meta compliance
6. CTA clarity and pull
7. Distinctiveness across the 10
8. Spoken-flow naturalness

## THE LOOP THAT REPLACES APPROVAL
```
generate 10 -> self-grade against gates + rubric -> rewrite anything failing a gate
or scoring under 4 -> repeat -> finish ONLY when all gates pass AND all 8 dimensions
are 4 or 5.
```

## CORE PRINCIPLES
- **Extract, do not invent:** pull the audience's exact words from the master brain.
- **One person, spoken:** write for the ear, not the page.
- **Every line earns the next:** no flat spots, momentum-driven.
- **Anchor to the event:** name, date, city, CTA in every script.
- **Compliance is non-negotiable:** a non-compliant script is a failed script.
