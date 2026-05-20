<p align="center">
  <img src="docs/assets/hero.png" alt="Sales AI — a salesperson collaborating with an AI agent that reads customer email and queries the customer database" width="820" />
</p>

<p align="center">
  <strong>English</strong> &nbsp;·&nbsp;
  <a href="README.zh-TW.md">繁體中文</a> &nbsp;·&nbsp;
  <a href="README.ja.md">日本語</a> &nbsp;·&nbsp;
  <a href="README.ko.md">한국어</a>
</p>

<p align="center">
  <img alt="Java 21" src="https://img.shields.io/badge/Java-21-007396?style=flat-square&logo=openjdk&logoColor=white" />
  <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-22c55e?style=flat-square" />
  <img alt="Status: MVP" src="https://img.shields.io/badge/Status-MVP-3b82f6?style=flat-square" />
  <img alt="No dependencies" src="https://img.shields.io/badge/Dependencies-None-94a3b8?style=flat-square" />
  <img alt="MCP-ready" src="https://img.shields.io/badge/MCP-ready-f59e0b?style=flat-square" />
  <img alt="Claude Code skill" src="https://img.shields.io/badge/Claude%20Code-skill-8b5cf6?style=flat-square" />
</p>

<p align="center"><i>An AI sales copilot that reads your customer's email like a senior account manager would &mdash; context first, draft last, never hits send.</i></p>

---

## TL;DR

- A Java 21 copilot for B2B account managers. It loads the customer's profile and commercial history first, reads only the relevant thread, classifies intent and tone, evaluates risk against an explicit policy, and produces two reply drafts plus follow-up actions.
- It is not a chatbot. It is context-grounded by design. Refunds, legal language, contract concessions, exceptional discounts, cancellation talk, and churn signals on VIP accounts force a hard manager-approval gate that **blocks the drafts**.
- Run it in 60 seconds with the stock JDK, no dependencies, no credentials, no network &mdash; see [Run it](#run-it-in-60-seconds).

## Vision

The goal of Sales AI is to ship a **24/7 automated AI agent focused on the sales function** &mdash; a sales engine that never clocks out.

It doesn't lock you into one industry. **Plug in your existing customer database, meeting notes, contract archive, and CRM system**, and this agent will respond to customer email like a senior account manager around the clock &mdash; the daytime inquiry, the midnight refund request, the weekend renewal question, all caught in the first window. Manufacturing, finance, SaaS, cross-border e-commerce, B2B services &mdash; **wherever your customers write to you, this agent fits**.

### What's coming next

- **Phase 4 &mdash; Proactive outreach.** Not just inbound replies. Overdue proposals, contracts about to expire, accounts showing churn signals &mdash; the agent drafts the message, orders the priority, schedules the follow-up.
- **Phase 5 &mdash; Cross-channel messaging.** Beyond email: LinkedIn, WhatsApp, LINE OA, Slack, the website chat widget, social-media DMs &mdash; same customer context, consistent voice across channels.
- **Phase 6 &mdash; Autonomous closing.** Within manager-defined price bands, contract templates, and discount authorities, the agent runs the full loop &mdash; quote, negotiate, sign, log to CRM &mdash; without a human in the routine path.

### What this is worth to a company

- **Sales output stops being capped by headcount.** A 5,000-customer business that used to need 30 reps to keep coverage can run with 5 reps + AI and hit higher contact frequency.
- **Speed becomes a weapon.** Industry average reply time on a sales inquiry is 4&ndash;12 hours; this agent replies in 30 seconds. **Speed of reply is conversion.**
- **Institutional memory doesn't walk out the door.** When a rep leaves, they take customer history, talking points, and account context with them &mdash; every B2B company's biggest unforced loss. Sales AI lives in the database and shows up to work every day.
- **Managers spend their time where it matters.** Refunds, contract concessions, VIP risk &mdash; those need a signature. The other 80% of routine email no longer eats their calendar.
- **Auditable by default.** Regulated industries (banking, insurance, healthcare) cannot run a black-box agent. Every Sales AI step writes one audit line; the regulator, the board, and the external auditor can all read what happened and **why**.

Today we ship a context-first MVP with a hard manager-approval gate. As phases progress, the gate narrows and the autonomous portion grows &mdash; but **the gate never disappears**. That is our safety promise.

## Why Java

Not because Java is trendy. Because this project's destination *is* Java's home turf.

| Reason | How it shows up in this codebase |
|---|---|
| **B2B enterprise IT runs on Java** | Banks, insurers, manufacturing, ERP/CRM backends &mdash; ~90% Java/Spring. Embedding this agent next to existing services in the same process, sharing the same audit log, sharing the same DI container &mdash; far less friction than a Python sidecar. |
| **JDK 21 + zero dependencies = 60-second reprodu