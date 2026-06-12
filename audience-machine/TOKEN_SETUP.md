# Meta System User Token Setup

This is the **one and only blocker** to the first live run. Once this token
exists, the machine can build audiences in any client account ESA has access to.

A "system user token" is a master key tied to ESA's Business Manager (not to a
person, so it never breaks when someone leaves). You create it **once**. Then
for each client you do a tiny 2-minute step to hand that key access to their
account.

Plan about **15 minutes** for the one-time part. You need to be an **admin** of
ESA's Business Manager.

---

## Part A - one time (about 15 min)

### 1. Create a Meta app
1. Go to <https://developers.facebook.com/apps> and click **Create App**.
2. App type: **Business**.
3. Name it something like `ESA Audience Machine`. Link it to ESA's Business
   Manager (Business portfolio) when asked.
4. On the app dashboard, find **Marketing API** and click **Set up**.

### 2. Create a System User
1. Go to **Business Settings** (<https://business.facebook.com/settings>).
2. Left menu: **Users > System Users** > **Add**.
3. Name it `Audience Machine`, role **Admin**. Create.

### 3. Generate the token
1. Still on the System User, click **Generate new token**.
2. Pick the app you made in step 1.
3. Token expiration: **Never**.
4. Tick these permissions:
   - `ads_management`
   - `business_management`
   - `pages_read_engagement`
5. Generate. **Copy the token now** - Meta only shows it once.

### 4. Put the token in your terminal (NOT in any file)
```bash
export META_ACCESS_TOKEN="paste-the-long-token-here"
```
That's it. Now you can run the machine.

> To make it stick between terminal windows, you can add that one line to your
> `~/.zshrc`. That file is on your Mac only. **Never** put the token in the repo,
> a client config, or Slack.

---

## Part B - per client (about 2 min, the step people forget)

Partner access from the client goes to ESA's **business**, but the **system
user** still has to be handed each client's assets explicitly. Miss this and the
machine will say it can't see the account.

After the client adds ESA's Business Partner ID and grants their ad account,
Page, Pixel, and Instagram:

1. **Business Settings > Users > System Users >** `Audience Machine`.
2. Click **Add Assets**.
3. Add the client's:
   - **Ad account** - with **Manage** permission
   - **Page** - with full control / manage
   - **Pixel (dataset)** - manage
   - **Instagram account** - manage
4. Save.

Now fill that client's IDs into `config/clients/<client>.yml` and run.

> Add this 2-minute "assign assets to the system user" step to the client
> onboarding checklist so it never gets skipped.

---

## Access level (rate limits)

The Marketing API starts in **Development access**: rate-limited but completely
fine at ESA's current volume (~5 new clients/month). Once you're past a couple
dozen active ad accounts, apply for **Standard Access** in the app dashboard
under App Review / Marketing API.

---

## If the token leaks

Treat it like a password to every client's ad account, because it is.
1. **Business Settings > Users > System Users >** `Audience Machine`.
2. Revoke the old token, **Generate new token**, and re-export it in your
   terminal. The old one dies instantly.

---

## Quick test once it's set

```bash
cd audience-machine
./setup.sh                                          # once
export META_ACCESS_TOKEN="your-token"
./run.sh config/clients/example-client.yml --dry-run
```
A dry run needs no real account and creates nothing - it just proves the tool
and your config parse. The real test is the first live run on a real client,
which confirms the Instagram + video event names.
