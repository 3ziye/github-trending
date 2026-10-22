<p align="center">
  <a href="https://mailcheap.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/logo-dark.svg">
      <img src="docs/logo.svg" alt="MailCheap" width="64" height="64">
    </picture>
  </a>
</p>

<h1 align="center">MailCheap</h1>

<p align="center">
  Newsletters where you pay for the emails you send, not for dormant subscribers.<br>
  A fraction of the price of beehiiv and the like.
</p>

<p align="center">
  <a href="https://mailcheap.ai">Website</a> ·
  <a href="https://mailcheap.ai/docs">API docs</a> ·
  <a href="https://mailcheap.ai/signin">Sign up for MailCheap Cloud</a>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: AGPL-3.0" src="https://img.shields.io/github/license/marclou/mailcheap?color=blue"></a>
  <a href="#self-hosting"><img alt="Node.js 22 or later" src="https://img.shields.io/badge/node-22%2B-339933?logo=nodedotjs&logoColor=white"></a>
  <a href="https://mailcheap.ai/docs/mcp"><img alt="MCP server" src="https://img.shields.io/badge/MCP-server-0a0a0a"></a>
</p>

![MailCheap's overview: emails sent, delivery, open, click, bounce and complaint rates, and subscribers over the last 30 days](docs/screenshots/overview.webp)

MailCheap is a newsletter app: write an issue, send it to your list, publish it on the web, from the dashboard or from your AI agent. This repository is the whole app. Self-host it with your own Amazon SES or PostShiba account, or use [MailCheap Cloud](https://mailcheap.ai), which runs this same code.

## Features

- **AI agents and the dashboard.** Everything the dashboard does also works from an AI agent through the MCP server, and from code through the REST API, with the same checks and limits. ChatGPT, Claude and Grok Bot connect with OAuth; Claude Code, Codex and Cursor with an API key. MCP marks sending as an action that can't be undone, so agents ask you first.
- **Write, review, send.** Write in an editor with slash commands, images and boxes, or send Markdown or a complete HTML email through the API and MCP. Review shows what to fix before sending: subject, preview text, unsubscribe link, Gmail's 100 KB clip, postal address, sender. Then send it, schedule it, or start with your most engaged readers and send to more later.
- **Imports from beehiiv, Substack and Mailchimp.** Their CSV exports import as they are, with each reader's status and signup date, and so do Kit's, MailerLite's, Buttondown's, Ghost's and EmailOctopus's.
- **A website for each newsletter**, on a free subdomain on MailCheap Cloud (`<slug>.mailcheap.ai`), or on your server: every issue gets a page search engines can find, with a signup form, an author page, share images and a sitemap.
- **Sending from your own domain**, with the DKIM, return path and DMARC records to add and a check for each. On MailCheap Cloud, a newsletter without a domain sends from its own shared address, `hello@<slug>.mailcheap.ai`.
- **Deliverability protections**, built in:
  - warm-up: contacts the account never emailed go out as a 5% slice first, and the rest 3 hours later if the slice's bounces and complaints stay low. On MailCheap Cloud, an account's sends also speed up as it proves clean volume;
  - list cleanup, on by default: readers who ignored several issues get one "do you still want this?" email, then stop getting issues;
  - contact cleaning: imports leave out invalid, misspelled (gmial.com), spam trap, role, throwaway and duplicate addresses, domains that can't receive email, and anyone who unsubscribed, bounced or complained before;
  - one never-email list for the whole server: an address the email provider says doesn't exist (for 180 days) or that turned out to be a spam trap (for good) is left out of every account's imports, signups and sends, and only a keyed hash of it is kept;
  - spam and bounce limits: a send pauses past 2% hard bounces or 0.08% complaints, and the account is blocked past 5% or 0.3%, or on a spam trap hit;
  - Gmail's spam rates, which Gmail never reports one complaint at a time: every email carries a `Feedback-ID` for Gmail's feedback loop (its campaign or newsletter, its account, its kind), and once an admin connects [Google Postmaster Tools](https://postmaster.google.com), MailCheap reads it every day. An account Gmail flags at 0.08% has its sends paused, at 0.3% it's blocked, and the admins hear when the whole domain reaches 0.1%;
  - one-click unsubscribe (RFC 8058) and a signed unsubscribe link in every email, and confirmed opt-in, on by default.
- **Several newsletters**: up to 3 per account, each with its own contacts, campaigns and website.
- **Signups and stats**: signup forms and a signup API, welcome emails, open and click tracking that leaves link scanners out, subscribers over time, and reports by inbox provider (Gmail, Outlook, Yahoo, iCloud...).

| Write, review, send | The newsletter's website |
| --- | --- |
| ![The campaign editor's Write step: the subject, preview text and body of a draft, with the Writ