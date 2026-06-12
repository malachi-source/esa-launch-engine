# ESA Master Project Plan (canonical)

> Source: ESA's project tracker spreadsheet (Google Sheet 1YGXmOuevk8OyNlShx2azOtNZOkpD2LnDMuV3PsyMSk8).
> This is the FULL operational plan for a client webinar launch — every task, owner, timeline.
> The `workflows/` folders are the AI-content pieces of this; this plan is the whole thing
> (incl. human/ops/GHL tech). The eventual orchestrator should track this end to end.
> Owner key: ESA = our team, Client = the client, Both = joint.

## Pricing
| Service | Price |
|---|---|
| One-time webinar build-out | $10,000 |
| One-time ad management | $2,500 |
| Managed (account manager + Slack) | $2,500 |
| Ad management (ongoing) | $2,500 |

## Phase 0 — Onboarding & Kickoff
| Task | Owner | Timeline | Notes |
|---|---|---|---|
| Send invoice & contract | ESA | Day 0 | |
| Sign service agreement & pay invoice | Client | Day 0 | |
| Contract-signed + invoice-paid confirmation in Slack | ESA | Day 0 | |
| Send welcome email & schedule kickoff call | ESA | Day 0 | |
| Send onboarding questionnaire / intake form | ESA | Day 0 | ← our new live form |
| Client fills out onboarding questionnaire | Client | | |
| Collect access: GHL, domain/DNS, email & SMS, payment (Stripe), ad accounts, calendar | Client | Day 0–2 | Most common cause of delays — send a credentials checklist |
| Set up shared comms channel (Slack/WhatsApp) & this tracker | ESA | Day 1 | |
| Add additional team members to Slack (client + ESA) | ESA | Day 1 | |
| Onboarding call scheduled (client picks time) | Client | | |
| Onboarding call fulfilled + intro | Both | | |

## Phase 1 — Discovery & Assets
| Task | Owner | Notes |
|---|---|---|
| Confirm webinar topic and core messaging | Both | |
| Confirm webinar date & time | Client | |
| Confirm webinar platform & access link (e.g. Zoom) | Client | We request the live link closer to the date |
| Confirm the offer and pricing to be presented | Client | |
| Define target audience / ICP | Both | |
| Collect brand assets (logo, colors, fonts) | Client | |
| Collect testimonial videos, images & background media | Client | |
| Collect or confirm the VSL | Client | We can script this (see Promotion) |

## Phase 2 — Tech Setup & Account Configuration (GHL = GoHighLevel)
| Task | Owner | Notes |
|---|---|---|
| Audit existing setup (GHL access, contacts, workflows, A2P, domain, email, payment, pipelines, conflicts) | ESA | Only if migrating from an existing CRM |
| Create GHL sub-account (business details + team) | ESA | |
| Register A2P 10DLC (A2P funnel, business + campaign details) | ESA | Carrier compliance; approval min 72h |
| Purchase phone number | Client | |
| Import & customise snapshot (tags, pipelines, workflows, triggers, notifications, form/opportunity triggers, custom fields) | ESA | Loads our proven webinar system |
| Create pipeline stages & disposition dropdowns | ESA | |
| Connect domain for the funnel | Client | |
| Connect subdomain for email + auth (SPF/DKIM/DMARC) | Client | Protects deliverability |
| Provide old leads to ESA | Client | |
| Upload old leads to GHL | ESA | Client sends list; we clean & import |
| Build smart lists of hot leads to re-engage | ESA | |
| Set up AI Conversation Agent | ESA | |
| Training material for AI training | Client | |

## Phase 3 — Webinar Funnel Build
| Task | Owner | Notes |
|---|---|---|
| Build registration (opt-in) form, connect to funnel | ESA | |
| Develop initial funnel draft (brand, testimonials, VSL) | ESA | |
| Build registration, confirmation, replay pages | ESA | |
| Install website chat widget | ESA | |
| Optimize funnel for mobile & conversion | ESA | |
| Share draft with client, gather feedback | ESA | |
| Approve initial funnel draft | Client | |
| Implement feedback & revisions | ESA | |
| Confirm domain & get final approval | Both | No go-live without sign-off |
| Publish funnel live | ESA | |
| Configure tracking (pixels, GA4, conversion events) | ESA | |
| Full end-to-end QA of registration flow | ESA | Register as test lead; confirm every email/text fires |

## Phase 4 — Automations & Workflows
| Task | Owner | Notes |
|---|---|---|
| Import & configure automation snapshot | ESA | |
| Registration confirmations, internal notifications, SMS opener | ESA | |
| Reminder sequence for all registrants | ESA | |
| Email/SMS nurture sequence + content | ESA | |
| Reactivation / re-engagement campaign | ESA | Begins T-14 days |
| No-show automations + content | ESA | |
| Replay automation + post-webinar replay email | ESA | |
| Write all webinar email & SMS copy | ESA | |
| Approve/tweak all content | Client | |
| Add approved content into all automations | ESA | |
| Pipeline stage-change automations | ESA | |
| Post-purchase (buyer) automations | ESA | |
| Do-not-contact (DNC) compliance automations | ESA | Honors opt-outs |
| Booking calendar + video-conf integration for sales calls | ESA | |
| Smart lists for registrants & reactivation | ESA | |
| Reactivation stops on successful registration | ESA | |
| Pause promo automations before event | ESA | Webinar day |
| Test all workflows end to end | ESA | |

## Phase 5 — Promotion & Outreach
| Task | Owner | Notes |
|---|---|---|
| Suggest webinar topic | ESA | |
| Create TAP (Target Audience Profile) | ESA | = our Audience Profile prompt |
| Create VSL script | ESA | = our VSL prompt |
| SMS blast / invitation (needs webinar link) | ESA | |
| Email invitation to database | ESA | |
| Reactivation outreach to old leads | ESA | T-14 days |
| [Paid ads] Create ad copies | ESA | If running paid traffic |
| [Paid ads] Share VSL script & ad copies with client | ESA | |
| [Paid ads] Video editing if required | ESA | |
| [Paid ads] Set up ad accounts & campaign structure | ESA | |
| [Paid ads] Launch ads 7 days before event | ESA | T-7 days |
| [Paid ads] Optimize ads & track CPL / registrations | ESA | Daily |

## Phase 6 — Optimization & Iteration (ongoing)
| Task | Owner |
|---|---|
| Optimize AI chatbot responses & flows | ESA |
| Run 'Yes' campaigns to re-engage/qualify unresponsive leads | ESA |
| Refine email & SMS copy from engagement data | ESA |
| Implement funnel improvements from conversion data | ESA |
| Audit lead quality & data; clean & re-segment | ESA |
| Launch additional campaigns for more opt-ins | ESA |

## Phase 7 — Webinar Day (Live)
| Task | Owner |
|---|---|
| Final tech check with client/host | Both |
| Confirm webinar link is live & tested | ESA |
| Verify day-of reminders firing | ESA |
| Confirm promo automations paused | ESA |
| Monitor live registrations | ESA |
| Provide live support during event | ESA |
| Capture/save recording for replay, send to ESA | Client |

## Phase 8 — Post-Webinar
| Task | Owner | Timeline |
|---|---|---|
| Turn off all automations after event | ESA | |
| Trigger replay automation & send replay email | ESA | T+0–1 day |
| Launch follow-up sequence (attendees vs no-shows) | ESA | |
| Activate booking / sales-call automation for the offer | ESA | |
| Move buyers into purchased pipeline & automations | ESA | |
| Wind down / pause ads & promo | ESA | |
| Share post-event metrics with client | ESA | |

## Phase 9 — Reporting & Offboarding
| Task | Owner |
|---|---|
| Review / wrap-up call with client | Both |
| Collect testimonial & feedback | ESA |
| Hand over assets, funnel & documentation | ESA |
| Transfer / revoke access as agreed | ESA |
| Send final invoice & settle payments | ESA |
| Archive project & assets | ESA |
| Send offboarding email & discuss renewal / next campaign | ESA |

## Team roster
| Name | Role | Core responsibilities | Talks to clients in Slack? |
|---|---|---|---|
| James Mungai | Operations / Strategy | Building strategy for clients | Yes |
| Malachi Broadaway | Marketing | Ads for clients & ESA | Yes |
| Shah | GHL Lead | All tech for clients & ESA | Yes |
| Kim Pusa | Admin Assistant | Admin tasks incl. client onboarding | Yes |
| Kim Ortega | Client Success | Client communications | Yes |
| Zohaib | Ads Buyer | Assists Malachi with ads | Yes |
| So (Zo) | Ads Buyer | Assists Malachi with ads | No |
| Jawad | GHL Tech | Assists Shah with GHL builds | Yes |
| Hamza | GHL Tech | Assists Shah with GHL builds | Yes |
| Michaela | CSM | Client communications (new) | Yes |
