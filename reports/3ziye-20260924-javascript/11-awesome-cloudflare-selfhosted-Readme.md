# Awesome Cloudflare Self-Hosted [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Open-source apps that replace a SaaS product, running in **your own Cloudflare account**.

A Worker, a D1 database, an R2 bucket and a `wrangler deploy` now cover what used to need a VPS
and a monthly invoice. This list tracks the software taking advantage of that: a booking page
instead of Calendly, a feedback board instead of Canny, an inbox instead of Google Workspace.

Every entry is checked rather than taken on trust: the licence is read from the project's own
licence file and the bindings from its deploy configuration, not from its description.
[How the audit works.](docs/auditing.md)

## Contents

<!-- BEGIN TOC -->

- [What belongs here](#what-belongs-here)
- [Analytics](#analytics)
- [Auth, secrets and security](#auth-secrets-and-security)
- [Blogs, CMS and docs](#blogs-cms-and-docs)
- [Business and operations](#business-and-operations)
- [Chat and realtime](#chat-and-realtime)
- [Community and comments](#community-and-comments)
- [Developer tools](#developer-tools)
- [Email and inboxes](#email-and-inboxes)
- [Files, images and sharing](#files-images-and-sharing)
- [Link shorteners](#link-shorteners)
- [Notes, knowledge and sync](#notes-knowledge-and-sync)
- [Notifications and push](#notifications-and-push)
- [Remote access](#remote-access)
- [Uptime and status pages](#uptime-and-status-pages)
- [Personal](#personal)
- [Reuse](#reuse)

<!-- END TOC -->

## What belongs here

**In:** a complete, deployable application that stands in for a product you'd otherwise pay for,
where the deploy target is your own Cloudflare account.

**Out:** frameworks, routers and SDKs; starters and templates; apps you host on your own server
or in Docker; Workers-compatible runtimes you self-host (those replace Cloudflare rather than run
on it); dashboards for administering Cloudflare; proxy and VPN subscription scripts; and API
relays that just shim someone else's SaaS. Full criteria are in the contributing guide.

**Know one that's missing? [Suggest it in an issue.](../../issues/new?template=add-entry.yml)**
Three fields, no pull request — the rest is read from the repository.

<!-- BEGIN ENTRIES -->

## Analytics

| Project                                                                                                                                                                                                                                                                                                                                                               | What it replaces                                                                                                                                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[Counterscale](https://github.com/benvinegar/counterscale)**<br><img alt="stars" src="https://img.shields.io/github/stars/benvinegar/counterscale?style=flat-square&amp;label=%E2%98%85&amp;color=brightgreen" align="absmiddle" height="18">&nbsp;<img alt="MIT" src="https://img.shields.io/badge/MIT-lightgrey?style=flat-square" align="absmiddle" height="18"> | Google Analytics alternative built on Analytics Engine, so traffic volume barely moves the bill.<br>R2 · Analytics Engine · Cron                                  |
| **[InsightFlare](https://github.com/RavelloH/InsightFlare)**<br><img alt="stars" src="https://img.shields.io/github/stars/RavelloH/InsightFlare?style=flat-square&amp;label=%E2%98%85" align="absmiddle" height="18">&nbsp;<img alt="MIT" src="https://img.shields.io/badge/MIT-lightgrey?style=flat-square" align="absmiddle" height="18">                           | Privacy-focused web analytics with realtime sessions, running entirely on Cloudflare.<br>D1 · R2 · KV · Durable Objects · Analytics Engine · Cron                 |
| **[OpenSEO](https://github.com/every-app/open-seo)**<br><img alt="stars" src="https://img.shields.io/github/stars/every-app/open-seo?style=flat-square&amp;label=%E2%98%85&amp;color=brightgreen" align="absmiddle" height="18">&nbsp;<img alt="MIT" src="https://img.shields.io/badge/MIT-lightgrey?style=flat-square" align="absmiddle" height="18">                | Ahrefs and Semrush alternative: keyword research, rank tracking, site audits and backlink data.<br>D1 · R2 · KV · Durable Objects · Workflows · Hyperdrive · Cron |
| **[traks](https://github.com/shivamanupadi/traks)**<br><img alt="stars" src="https://img.shields.io/github/stars/shivamanupadi/