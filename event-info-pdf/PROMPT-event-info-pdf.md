# Event Info PDF Generator -- Prompt

## Purpose
Generate a 1-2 page Event Info PDF that gives the website designer and GHL developer every detail they need about the client's event: pricing, speakers, offer details, event goals, ticket targets, brand assets, tech stack, and audience snapshot. This PDF lives in the client's Google Drive folder and is the single reference doc for anyone on the team.

## Trigger
Runs alongside TAP + Brain, 15 minutes after onboarding form submission. No approval needed -- fires automatically.

## Data Source
Supabase onboarding_submissions table, answers JSONB field (68 questions).

## PDF Sections (max 2 pages)
1. Header Banner -- Event name, company, location, date (branded with client colors)
2. Client Contact -- Name, email, phone, website, CRM, approver
3. Event Details -- Date, location, first event?, attendee goal, tickets sold, leads, speakers, team
4. Pricing & Offers -- Ticket prices, high-ticket offer (yes/no + price), ticket tiers, sales reps at event
5. Business & Positioning -- One-sentence description, products/services, competitive advantage, what clients want, core transformation
6. Target Audience Snapshot -- Ideal buyer, demographics, #1 problem
7. Marketing & Ad Strategy -- Ad budget, ad type, outbound calls, SMS/email strategy, sales process
8. Tech Stack & Data Flow -- Payment processor, A2P, email domain, domain verified, old leads, data flow, invoice automation
9. Brand Assets -- Colors (primary/secondary/accent hex), fonts, logo link, media folder
10. Footer -- Company name, generation date, ESA branding

## Design Rules
- Max 2 pages, compact layout (8-9pt body text)
- Client brand colors from form fields 48-50
- Clean, professional, scannable -- not a wall of text

## Slack Notification
Send alongside the Client Brain message in #esa-master-viktor-chat. Tag <@U088QGQ3H2Q>. Does NOT require approval.
