# Deploy the ESA Onboarding Form (Supabase + Vercel)

Follow these once. Total time ~15 min. You do the clicks; the code is already built.

```
Client fills form  →  /api/submit (Vercel function)  →  Supabase database
                                                          ↑ we read this to run the prompts
```

---

## PART A — Create the database (Supabase)

1. Go to **https://supabase.com** → **Start your project** → sign in with **GitHub** (your malachi-source account).
2. **New project**:
   - Name: `esa-launch-engine`
   - Database password: make one up and **save it somewhere** (you rarely need it again)
   - Region: pick the one closest to you
   - Click **Create new project** and wait ~2 minutes while it sets up.
3. In the left sidebar click **SQL Editor** → **+ New query**. Open the file
   `form/supabase-setup.sql` from this repo, copy ALL of it, paste it in, and click **Run**.
   You should see "Success." (This creates the `onboarding_submissions` table.)
4. Get your keys: left sidebar → **Project Settings** (gear) → **API**. Copy these two:
   - **Project URL** (looks like `https://abcd1234.supabase.co`)
   - **service_role** key (under "Project API keys" — click reveal). ⚠️ This is a SECRET — it has full
     database access. Do NOT paste it in chat or commit it. You'll paste it into Vercel in Part B only.

---

## PART B — Put the form online (Vercel)

1. Go to **https://vercel.com** → **Sign up / Log in** with **GitHub** (malachi-source).
2. **Add New… → Project**. Find **esa-launch-engine** in the list and click **Import**.
   (If you don't see it, click "Adjust GitHub App Permissions" and give Vercel access to the repo.)
3. **Configure the project:**
   - **Root Directory** → click **Edit** → choose **`form/app`** ← important
   - Framework Preset: **Other** (it's a static site + function; no build needed)
4. Expand **Environment Variables** and add these two (from Part A, step 4):
   | Name | Value |
   |------|-------|
   | `SUPABASE_URL` | your Project URL |
   | `SUPABASE_SERVICE_ROLE_KEY` | your service_role key |
5. Click **Deploy**. Wait ~1 minute. You'll get a live link like `https://esa-launch-engine.vercel.app`.

---

## PART C — Test it end to end

1. Open your new Vercel link, fill out a few questions, and hit **Submit**.
2. Back in Supabase → left sidebar **Table Editor** → `onboarding_submissions`. You should see a new row. 🎉
3. Tell Claude "a test submission is in Supabase" and we'll confirm we can read it to run your prompts.

## Later (optional)
- Point your own domain (e.g. `forms.eventsalesagency.com`) at the Vercel project: Vercel → Project →
  Settings → Domains.
- Every time we push improvements to GitHub, Vercel auto-redeploys. No manual steps.
