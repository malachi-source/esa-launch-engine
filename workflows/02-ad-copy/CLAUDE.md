# 01 Ad Scripts — working notes
Updated: 2026-06-25

## What this step does
Generates 20 unique, high-converting 45–60 second Meta video ad scripts per campaign.

- **Scripts 1-10:** ESA Proven Method (Five-Layer Persuasion Stack + 10-Script Variation Matrix). Modeled on Tai Lopez, Russell Brunson, and Grant Cardone. What's working to sell tickets to events and webinars.
- **Scripts 11-20:** Industry Cold Traffic Converters. Completely different formats from 1-10. Researched for the client's specific industry — what's working in THEIR niche right now.

The prompt lives in `PROMPT.md`; an approved swipe file of 30 real examples lives in `examples/30-example-scripts.md` to anchor tone and format.

## Trigger: TAP Approval (✅ Reaction)
Ad scripts do NOT auto-generate. They fire ONLY after:
1. Client Brain is complete
2. Event Info PDF is complete
3. **Malachi approves the TAP with a ✅ reaction on the TAP Slack message**

The TAP approval watcher (cron) polls for ✅ reactions every 3 minutes. When detected, it marks the submission as approved and the ad scripts generator fires on its next cycle.

## Pre-Generation Requirements (MANDATORY)
Before writing any scripts, two checks must be completed:

### 1. Voice Lock
Load the full Client Brain and build a Voice Lock Profile:
- Read social media captions, video/podcast transcripts, LinkedIn posts and comments
- Read how they filled out the onboarding form (strongest voice signal)
- Document: sentence length, vocabulary level, energy, signature phrases, words they never use
- Every script must pass: "Would they actually say this on camera?"

### 2. Event Info PDF Cross-Check
Load the Event Info PDF and verify:
- Event name, date, location, pricing are accurate
- Offer details, bonuses, speaker info match
- Event goals inform urgency angles

Scripts are NOT generated until both checks pass.

## Inputs it needs
- Client Brain (BRAIN.md, voice_samples.md, social_profiles.md, form_data.json)
- Event Info PDF (event details, pricing, speaker info, goals)
- Audience profile (demographics, pain points, desires, objections, identity labels)
- Offer/event details (name, date, location, CTA, transformation, pricing, benefits)

## Output it produces
20 video ad scripts, each 45–60 seconds, spoken-voice, Meta-policy compliant, in the client's exact voice, with varied hooks/angles, approval-ready.

## Status
- [x] Prompt copied from the master Google Doc
- [x] Updated with Voice Lock + Event Info pre-generation checks (2026-06-25)
- [x] Updated for 20 scripts (10 ESA + 10 Industry) (2026-06-25)
- [x] TAP approval gate wired — ✅ reaction triggers ad scripts (2026-06-25)
- [ ] Tested with a real example

## Notes / decisions
- Prompt copied verbatim from the "AD SCRIPT PROMPT / THE ULTIMATE META VIDEO AD SCRIPT PROMPT (MASTER VERSION)" section of the master doc. Only markdown-export artifacts were stripped.
- The 30 example scripts that follow the prompt in the master doc were saved separately as the swipe file in `examples/`.
- Swipe file spans four real campaigns: Elite Business Coaching Conference (1–5), Worthy London (6–10), Freedom Queen Live (11–15), The Advisor Advantage (16–20), and The A-Player Mindset Webinar (21–30).
- 2026-06-25: Added mandatory Voice Lock step — scripts must match client's exact speaking style from social media, videos, LinkedIn, form answers. Added Event Info PDF cross-reference. Scripts 11-20 must be completely different formats from 1-10, researched for the client's specific industry.
- 2026-06-25: Wired TAP approval gate — ad scripts only generate after Malachi reacts ✅ on the TAP message. Approval watcher cron checks every 3 minutes.
