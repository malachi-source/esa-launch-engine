// Vercel serverless function: receives a form submission and saves it to Supabase.
// Runs server-side, so the secret Supabase key never touches the browser.
// Env vars (set in Vercel): SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY

import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY
);

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }
  try {
    const { clientId, submittedAt, answers } = req.body || {};
    if (!answers || typeof answers !== 'object') {
      return res.status(400).json({ error: 'Missing answers' });
    }

    const { error } = await supabase.from('onboarding_submissions').insert({
      client_id: clientId || null,
      submitted_at: submittedAt || new Date().toISOString(),
      company_name: answers.company_name || null,
      email: answers.email || null,
      event_name: answers.event_name || null,
      answers: answers,
    });

    if (error) {
      console.error('Supabase insert error:', error);
      return res.status(500).json({ error: error.message });
    }
    return res.status(200).json({ ok: true });
  } catch (e) {
    console.error('Submit handler error:', e);
    return res.status(500).json({ error: String(e) });
  }
}
