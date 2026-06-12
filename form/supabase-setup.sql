-- ESA onboarding — Supabase database setup.
-- Run this once in your Supabase project: SQL Editor → New query → paste → Run.

create table if not exists onboarding_submissions (
  id           uuid primary key default gen_random_uuid(),
  client_id    text,
  submitted_at timestamptz default now(),
  company_name text,
  email        text,
  event_name   text,
  status       text default 'new',     -- new | in_progress | done (used later by the orchestrator)
  answers      jsonb not null default '{}'::jsonb  -- the full set of form answers
);

-- Fast lookups by client
create index if not exists idx_onboarding_client on onboarding_submissions (client_id);

-- Security: lock the table down. Only the server function (service-role key) can read/write.
-- The public/anon key cannot touch this data.
alter table onboarding_submissions enable row level security;
