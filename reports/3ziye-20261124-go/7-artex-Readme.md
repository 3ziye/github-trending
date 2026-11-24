# FailSafe ARTEX

<p align="center">
  <img src="assets/artex-failsafe-header.png" alt="ARTEX — a source-built FailSafe distribution" width="100%">
</p>

A source-built, locally bound distribution of [ARTEX](https://github.com/RuoJi6/ARTEX),
an open-source multi-agent security testing harness — with an English interface,
a hardened supply chain, and deployment controls.

This repository exists because the prebuilt `tomicdd/artex` Docker image was
found to contain an unauthenticated command-execution backdoor in November 2026.
This build is compiled from the audited `v0.3.15` source tag and keeps upstream's
full runtime capabilities, including Node 22, Playwright, Chromium, and nmap.
The compose file binds the console to localhost and does not publish the
recording proxy.

> **Authorized testing only.** ARTEX runs an autonomous agent that can execute
> shell commands and send network traffic. Use it only against systems you own
> or have explicit written permission to test.

## Maintained by FailSafe Cyber Frontier Labs

This distribution is maintained by **FailSafe Cyber Frontier Labs**, the team
behind GlassBreak and FailSafe's managed security-testing runtime. We review
upstream changes, maintain the hardened build, and operate ARTEX for teams that
need the capability without building the guardrails themselves.

- General and security questions: <hello@getfailsafe.com>
- Managed ARTEX runs and cyber-model access: <hello@getfailsafe.com>
- Website: <https://getfailsafe.com>

## Recommended models

ARTEX is an agentic harness: the model plans, calls tools, and reasons about
targets across many turns. For authorized security work we recommend a
**cyber-specialized model** — one trained or fine-tuned for security tasks
(cyber-domain SFT) with minimal refusal behavior, rather than a general-purpose
chat model. General consumer models routinely refuse reconnaissance, payload
construction, or exploitation reasoning even when the engagement is authorized,
which turns a legitimate test into a stream of blocked tool calls and wasted
tokens.

**GlassBreak** is FailSafe's cyber-grade model, built for this workload. It is
what we run when we operate ARTEX ourselves, and it is what the managed runs
use. If you do not already have a cyber model you can use, contact
<hello@getfailsafe.com> to arrange a managed run or rent model access for
runs on infrastructure you control.

## Features

- **Autonomous multi-agent testing.** A goals agent decomposes the objective, an
  event-driven planner explores, and concurrent workers execute intents. New
  assets, facts, findings, and results feed back into planning. A main
  conversation agent lets a human steer mid-run.
- **Real execution capabilities.** Shell and file tools, browser automation
  through Playwright MCP/CLI and bundled Chromium, skills, MCP servers, custom
  Python tools, DNS/network recon, and raw SYN scans with `nmap`.
- **Evidence-backed findings.** Findings keep task/asset lineage and recorded
  HTTP evidence, generate reports, and enter a dedicated retest workflow with
  `reproduced`, `fixed`, or `inconclusive` verdicts.
- **Traffic capture.** A recording proxy indexes HTTP exchanges, bodies, and
  archives; evidence binds to findings; archives export and reclaim safely.
- **Operational controls.** Admin authentication, configurable tool
  intercept/allow/deny rules, optional model-judge approvals, pause/resume,
  queueing, cancellation, deadlines, restart recovery, and task isolation.
- **Full English interface and documentation.** The console, agent skills, and
  project documentation are in English for international teams.
- **Fast static delivery.** The embedded web console is served with Brotli/gzip
  compression, content-hash ETags, and immutable caching, so the UI stays
  responsive when the binary is reached directly on `:8787` — no reverse proxy
  required for acceptable load times.

## What is different from upstream

| Area | Upstream default | This build |
|---|---|---|
| Image | prebuilt `tomicdd/artex` (backdoored) | compiled from this source tree |
| Runtime user | root | root (upstream parity) |
| Console binding | `0.0.0.0:8787` | `127.0.0.1:8787` |
| Recording proxy | published on `8788` | not published |
| Static UI delivery | uncompressed, no cache validators | Brotli/gzip + immutable cache + ETags |
| Interface language | Chinese | English |
| Browser automation | Node 22 + Playwright + Chromium | same, pinned versions |
| Browser MCP launcher | `npx @playwright/mcp` | pinned `playwright-mcp` |
| API-recon dependencies | installed during a run | preinstalled from a locked official registry |
| Online self-update | enabled, points upstream | compiled off; no remote check or download |
| Capabilities | default Docker set | default Docker set + `no-new-privileges` |
| Base images | floating tags | pinned by digest |

The API, UI, skills, browser MCP, and browser-driven recon are otherwise
unchanged. Node, Playwright, the Playwright MCP/CLI, a