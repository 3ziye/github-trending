<p align="center">
  <a href="https://link.context.dev/crm">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="./docs/images/powered-by-context-dark.png">
      <img alt="Powered by Context" height="23" src="./docs/images/powered-by-context.png">
    </picture>
  </a>
</p>

<p align="center">
  <img alt="stars" height="21" src="https://afterglow.watch/badge/trycompai/crm">
</p>

<h1 align="center">CRM</h1>

<p align="center">
  <strong>Comp AI CRM is an open source, CRM designed for AI agents.</strong><br>
  Agentic-first CRM.
</p>

<p align="center">
  <a href="#the-agent"><strong>The agent</strong></a> ·
  <a href="#the-stack"><strong>Stack</strong></a> ·
  <a href="#quick-start"><strong>Quick start</strong></a> ·
  <a href="#configuration"><strong>Configuration</strong></a> ·
  <a href="#deploying"><strong>Deploying</strong></a> ·
  <a href="./CONTRIBUTING.md"><strong>Contributing</strong></a>
</p>

<p align="center">
  <img alt="MIT licence" src="https://img.shields.io/badge/licence-MIT-blue.svg">
  <img alt="Built with eve" src="https://img.shields.io/badge/agent-eve-black.svg">
  <img alt="Built with Bun" src="https://img.shields.io/badge/runtime-Bun-black.svg">
  <img alt="Postgres" src="https://img.shields.io/badge/database-Postgres-336791.svg">
</p>

<p align="center">
  <img alt="The companies list with an account open on its Agent tab" src="./docs/images/product-shot.png">
</p>

---

## What this is

Most CRMs are a database with a form in front of it. The AI ones bolt a chat box onto
the side of that form. Both leave the actual work — finding out what is true, and
writing it down — to a human who has better things to do.

This is built the other way round. **The agent is not a feature of the CRM; the CRM is
where the agent keeps its notes.** It runs on its own deployment, on its own schedule,
against its own work queue. It decides what to look at next, books its own follow-ups,
spends a research budget, and stops when the budget runs out. Nothing about it is
request-response: close the browser and it keeps going.

The rule the agent itself never breaks: **nothing about a person is guessed.** No tool
accepts a confidence score, because a model asked to grade its own certainty will, and
it will be wrong in the direction that makes it look useful. Tools report what they
*observed* — `crm.signature-block`, `github.account-identity` — and a ledger prices the
evidence. Strong evidence writes to the record. Weak evidence becomes a suggestion a
human settles. A confidently wrong fact about a customer is worse than a blank field,
because nobody can tell it is wrong.

## Screenshots

<table>
  <tr>
    <td width="50%">
      <img alt="Agents that automate your CRM: a composer describing an agent in one sentence, with suggested actions beneath it" src="./docs/images/landing-agents.png">
    </td>
    <td width="50%">
      <img alt="What it actually does: records fill themselves in, agents that build agents, it books its own follow-ups, and a question box on every record" src="./docs/images/landing-capabilities.png">
    </td>
  </tr>
</table>

## The agent

[`apps/agent`](./apps/agent) is its own deployment, built on
[**eve**](https://eve.dev) — Vercel's filesystem-first framework for durable agents.
A tool is a file, a skill is a markdown file, a schedule is a file, and the runtime
handles the durable part: sessions that survive a redeploy, work that resumes where it
stopped.

| | |
| --- | --- |
| **18 authored tools** | `read_crm_history`, `search_crm`, `identify_contact`, `research_person`, `enrich_company`, `record_fact`, `schedule_recheck`… |
| **4 skills** | `evidence.md`, `identity-matching.md`, `data-boundaries.md`, `writing-a-brief.md` — prose the agent reads, versioned like code |
| **1 schedule** | `dispatch.ts`, which decides nothing. It leases what is due and starts a session per row. |
| **A sandbox** | `bash`, `grep`, `glob` and a `/workspace`, with **`deny-all` egress** |

**It runs itself.** `lib/tasks.ts` is the work queue: `claimDue` leases rows with
`FOR UPDATE SKIP LOCKED`, so two dispatchers take disjoint work and a run that dies
frees its row when the lease expires. Anything that looks like "every N minutes, the
oldest ten contacts" belongs in a task's `dueAt`, not in a cron expression. When the
agent wants another look at somebody it calls `schedule_recheck` and says why — and
the reason is shown to the rep, because an agent that cannot say why it will be back
in fourteen days does not have a reason, it has a default.

**Every outside source is optional, and it is designed to run with none of them.**
With no API keys at all it still works: `read_crm_history` reads your own threads,
meetings and signature blocks, which is free and is the best evidence there is — no
data vendor can sell you a reply from the person's own address. Each key opens one
more place to look. It is told at the start of every session which ones this install
has, so it plans around what 