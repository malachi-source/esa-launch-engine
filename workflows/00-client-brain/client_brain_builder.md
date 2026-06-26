---
doc_id: client-brain-builder
doc_type: "pipeline / SOP"
repo_path: "workflows/00-client-brain/"
runs_at: "onboarding (Stage 0, ~15 min, parallel with TAP + Event Info PDF)"
output_type: "google_doc"                      # the Client Brain, saved to the client folder
produces: "voice_lock + business_context"
consumed_by: "every downstream task (the Voice Lock input)"
owner: "Event Sales Agency (ESA)"
version: "1.0"
status: "DEFAULT SPEC — confirm/adjust to your real onboarding fields"
---

# CLIENT BRAIN BUILDER — Process + Voice Analysis Pipeline

> The **Client Brain** is the single source of voice truth for the whole system. Every task ("pull the Voice Lock from the Client Brain") depends on this doc being accurate. Build it once per client, at onboarding, before anything downstream runs.

---

## 1. WHEN IT RUNS

Fires automatically when the **onboarding form is submitted**, as part of the Stage-0 auto-generation (~15 min), in parallel with the Target Audience Profile and the Event Info PDF. It writes to the client's Drive folder (see the Auto Drive Folder SOP).

---

## 2. INPUTS

**A. Onboarding form answers** — business name, host name, offer(s) and price points, audience, the transformation they sell, proof/credentials, differentiators, and any "never say / always say" notes.

**B. Voice samples** (the more, the better — this is what makes the Voice Lock real):
- Website / sales / landing pages
- Past emails or newsletters
- Social posts and captions
- Existing ad copy
- Recorded talks, VSLs, or webinar transcripts
- Podcast / interview transcripts
- Books, lead magnets, long-form content

**Minimum viable:** a few hundred words across 2–3 sources. If samples are thin or missing, **flag it and request more — do not fabricate a voice.**

---

## 3. THE VOICE ANALYSIS PIPELINE

1. **Collect** every available sample from the onboarding inputs + the client's Drive uploads.
2. **Clean / normalize** — strip boilerplate, ads, and other people's words; keep only the client's own writing/speaking.
3. **Analyze** across the Voice Lock dimensions below.
4. **Extract** signature phrases (things they say a lot) and banned words (things they'd never say / can't claim).
5. **Draft the Voice Lock** and have it spot-checked by the owner.
6. **Assemble the Client Brain** (Voice Lock + Business Context) and save it to the client folder, versioned.

---

## 4. THE VOICE LOCK (the heart of the doc)

Capture each dimension with concrete examples pulled from the samples:

- **Tone & personality** — blunt, warm, playful, authoritative, etc.
- **Reading level** — simple/conversational vs. sophisticated.
- **Sentence length & rhythm** — short staccato lines? long flowing ones? line-break habits?
- **Vocabulary & signature phrases** — their go-to words and recurring expressions.
- **Banned words / things they'd never say** — and any compliance limits on what they can claim.
- **Perspective** — first-person founder ("I") vs. brand ("we").
- **Formality** — casual vs. professional; do they swear?
- **Humor** — present or not, and what kind.
- **Emoji & punctuation habits** — em dashes, ellipses, ALL CAPS for emphasis, emoji use.
- **Openers & closers** — how they start and sign off.

---

## 5. THE BUSINESS CONTEXT BLOCK

- Who the client is + the host's name and signature
- Offer(s), price points, and tiers
- Core audience
- The transformation they sell
- Proof / credentials / notable results (only real ones)
- Differentiators / unique mechanism
- Claims they ARE / are NOT allowed to make (compliance)

---

## 6. OUTPUT

A **Client Brain Google Doc** in the client's Drive folder, structured as **Voice Lock** + **Business Context**. This is the canonical "Voice Lock" every downstream task references. Versioned — never overwrite; create v2 when the client's voice or offer changes.

---

## 7. QUALITY GATE

Because everything downstream inherits this voice, the owner should **spot-check the Client Brain** before approving the Target Audience Profile (the ✅ that unlocks the creative tasks). A weak Client Brain produces weak, off-voice deliverables everywhere.
