# Target Audience Profile — Standard (pass/fail + scoring rubric)

> Source: desktop session handoff (2026-06-12), codified into the repo.
> This is the bar EVERY auto-generated TAP must clear. The grader judges output
> against this; the generate→grade→rewrite loop replaces human approval.
> Model all output on the approved corpus in `examples/` (14 client-delivered TAPs).

## The goal
An automated, NO-human-approval machine: client submits the onboarding survey →
auto-generate their TAP → self-grade until it passes → render branded PDF → file to
Google Drive + post to the client's Slack channel. No person in the loop.

## 10 REQUIRED sections (every profile must contain all 10)
1. **Event-anchored header** — event name, date, city, ticket tiers + prices, backend offer
2. **Executive snapshot** — the buyer in a few sentences + the primary pain / desire / objection to lead with
3. **Named avatar** — a real, named person (not "the audience")
4. **Demographics table** — age, gender, location, income/role, business stage
5. **Layered pain WITH verbatim quotes** — surface → practical → the 3am emotional truth, in the customer's words
6. **Identity-level desires** — surface wants → practical outcomes → who they want to become
7. **Decoded objections** — what they say / what they really mean / how to overcome in copy
8. **USE / AVOID language** — exact phrases to lift into copy + the words/vibes that kill trust
9. **Buying triggers** — emotional triggers, offer elements, social proof, urgency/scarcity that move them
10. **Actionable channel map** — where to reach them, specific and targetable

## 10 HARD GATES (any failure = auto-fail, rewrite required)
1. All 10 required sections are present
2. No blanks, placeholders, or "[fill in]" left anywhere
3. Event-anchored (names the real event, date, city, tiers, prices, backend offer)
4. The avatar is a real NAMED person, not a generic group
5. Pain is layered all the way to the 3am emotional truth
6. At least **5 verbatim customer quotes** appear
7. Every objection is decoded (say / mean / overcome)
8. The AVOID-list exists and is specific to this avatar
9. No banned words are used (the avatar's trust-killers)
10. Channels are concrete and actually targetable

## 8-DIMENSION RUBRIC (score each 1–5; ALL must be ≥4 to pass)
1. Avatar realness
2. Pain depth
3. Desire depth
4. Voice match (sounds like the real customer)
5. Specificity (named tools, real dollar figures, real geos)
6. Objection decoding
7. Channel actionability
8. Offer alignment

## THE LOOP THAT REPLACES APPROVAL
```
generate → self-grade against gates + rubric → rewrite anything under 4
→ repeat → finish ONLY when all 10 gates pass AND all 8 dimensions are 4 or 5
```

## CORE PRINCIPLES
- **Anchor to the event:** name, date, city, ticket tiers, prices, backend offer.
- **Avatar count follows the offer:** 1 tier/buyer type = 1 avatar; multiple tiers/buyer
  types = one avatar each (Paul = 3, Carlos = 4, Rosie = 3, Israel = 2, Tony = dual).
- **Extract, do not invent:** use the customer's real words. Verbatim customer language is
  the strongest input. Inventing the audience is the #1 risk of a no-approval machine.
- **Always include the avoid-list:** the words/vibes that kill trust for this avatar.
- **Format flexes, the bar does not:** approved profiles use several layouts; hit every
  required section regardless of format.

## THE INPUT GATE (the one thing the machine cannot fix)
Before generating, REQUIRE these gating fields. If missing, PAUSE and Slack the team
with exactly what's missing (do not generate from a thin survey):
- A1 ideal buyer · A2 age · A3 gender · A4 location
- B1 #1 problem · B2 their words · **B7 paste 5–10 real customer quotes**
- C1 what they want · D1 top objections · E2 words that turn them off
- G1 platforms · H2 who it's NOT for · J1 why choose you · J2 the transformation
- Offer fields: event, date, city, tiers, prices, backend offer
- **EXCEPTION:** if B7 is blank but Block I source material (call recordings, reviews, DMs,
  past surveys) is uploaded, the gate passes — extract the quotes from that material.

## THE MACHINE (5 pieces to build)
1. **TRIGGER** — survey POSTs answers on submit (webhook) / read from where responses land
   (our Supabase `onboarding_submissions` table).
2. **RUNNER** — a serverless function / small service that receives the submission.
3. **BRAIN** — Claude API, fed this Standard + the approved corpus + the survey answers,
   running the generate→grade→rewrite loop. Use the latest Claude model.
4. **RENDERER** — HTML→PDF template + weasyprint → branded PDF (brand hex from the survey).
5. **OUTPUT** — save PDF + editable doc to Drive, post to the client's Slack channel.
Secrets needed: Anthropic API key, Google Drive creds, Slack creds.

## STATUS / WHERE THE PIECES ARE
- ✅ Approved corpus: `examples/` (14 of 15 approved TAPs; missing Mary/Unleash Academy — to fetch).
- ✅ Survey/trigger: live onboarding form → Supabase `onboarding_submissions`.
- ⏳ Standard: this file.
- ⏳ Onboarding_Audience_Questions.md mapping (gating fields ↔ form questions).
- ⏳ Design template (HTML→PDF) + render script — exists in the desktop branch; to be pulled or rebuilt.
- ⏳ Generator/runner glue (the new code) — to build.
