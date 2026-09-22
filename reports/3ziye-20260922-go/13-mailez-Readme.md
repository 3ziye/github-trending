<p align="center">
  <img src="branding/mailez-logo.svg" alt="mailez" width="320">
</p>

<p align="center"><b>English</b> | <a href="README.zh-CN.md">简体中文</a></p>

# mailez — mail easy

Self-hosted email that scales with you: from a personal mailbox of one to
ten-thousand-person organizations — teams, companies and public-sector
agencies alike. Send and receive mail with your own domain, keep your data in
your own hands, and enjoy a webmail that actually feels good to use. One
command deploys the whole thing — mail delivery, spam filtering,
authentication, admin console and webmail.

## Who is it for?

- **Individuals** — a mailbox that is truly yours, not rented from a mail provider
- **Businesses and organizations** — domain mail for everyone, with data kept 100% in-house
- **Public sector** — strict data-sovereignty and privacy requirements, fully covered

The common ground: self-hosted and privacy-first, with no Linux mail expert
required to run it.

## What you get

<p align="center">
  <img src="docs/screenshots/webmail-inbox.jpg" alt="mailez webmail — three-pane inbox" width="880">
</p>

### Webmail that feels like a native app

- **Live, not refreshed** — new mail arrives over a real-time push channel, so
  the inbox updates itself; reading, replying and organizing never reload the
  page, and long lists scroll smoothly through 10,000+ messages
- **Conversation view keeps threads readable** — replies under one subject
  merge into a single conversation with its full timeline, and quoted history
  in replies folds away until you expand it

<p align="center">
  <img src="docs/screenshots/webmail-conversation.jpg" alt="mailez webmail — conversation view" width="880">
</p>

- **Three-pane layout** — folders, list and reading pane side by side; the
  list column is draggable to your preferred width
- **Search that just works** — type naturally (`from:`, `to:`, `has:attachment`,
  dates…), save frequent searches, and filter with one click for unread,
  starred or messages with attachments
- **Keyboard-first** — press `/` to search, `⌘K` for the command palette, `?`
  for the full shortcut list
- **Day-to-day mail tasks made easy** — conversation threads, quick reply
  right in the action bar, snooze, scheduled send, undo toast for
  bulk move / archive / delete, and drafts that keep every recipient including
  Bcc
- **A workbench, not just an inbox** — the home dashboard surfaces recent
  files and upcoming events, both clickable straight into context
- **Privacy features built in** — PGP sign and encrypt (distinct from your
  personal signature, with an optional auto-signature), two-factor
  authentication, remote-image blocking, a Sieve filter editor, and contacts
  grouped by sender
- **Works offline** — installs as a PWA; light/dark themes and three list
  densities for comfort

### Mail is just the start

- **Calendar** — events with reminders, shared calendars, and subscriptions
  you can plug into Apple Calendar or Google Calendar via a private ICS link
- **Contacts** — vCard import/export, duplicate merging, and CardDAV sync for
  phones
- **Drive** — upload and organize files, share by link, restore from trash;
  recent files show up on the dashboard

### Any device, any client

- **Standard protocols** — SMTP / IMAP / POP3 (implicit TLS available), plus
  CardDAV / CalDAV sync for phones and desktops; popular clients configure
  themselves via autoconfig/autodiscover
- **Delta Chat** — generate a login QR in settings and scan it with the
  Delta Chat app to turn the mailbox into an end-to-end-encrypted chat
  account, server setup included in the scan
- **App tokens** — per-client tokens you can issue and revoke from settings

### An admin console that doesn't feel like admin work

- **Manage everything in one place** — domains, mailboxes, aliases, relays,
  external mailbox fetching and app tokens; deleting a user cleans up their
  engine-side mailbox automatically
- **One-click DKIM** — generate signing keys with a status hint, so your mail
  stops landing in spam
- **Domain health checks** — the Health page live-verifies MX / SPF / DMARC /
  DKIM key comparison / Spamhaus blocklists / autoconfig / MTA-STS for every
  domain, plus engine, database, disk and certificate-expiry probes — each
  item with a status and a fix hint; the DNS wizard lists every record you
  must publish and verifies each one live, so going live is copy-paste
- **See who did what** — audit log of admin actions and role-based access
  (admin / manager / user)
- **Backup or migrate easily** — export and import your whole configuration

<p align="center">
  <img src="docs/screenshots/admin-domains.jpg" alt="mailez admin console — domains" width="880">
</p>

<p align="center">
  <img src="docs/screenshots/health-check.png" alt="mailez admin console — domain health checks" width="880">
</p>

### Trust and security under the hood

- **Spam filtering that works** — Rspamd learns from your reporting; DKIM /
  DMARC signing and 