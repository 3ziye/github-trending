<div align="center">

<img src="apps/web/public/logo-mark.svg" alt="AiSOC" width="120" />

# AiSOC

An open-source, self-hostable AI SOC. The agent's prompts, tool calls, and rationale are logged step-by-step and replayable. MIT-licensed.

[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Public eval harness: CI-gated](https://img.shields.io/badge/eval%20harness-CI--gated-2563eb?style=flat-square)](apps/docs/docs/benchmark.md)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-8b5cf6?style=flat-square)](CONTRIBUTING.md)
[![Version](https://img.shields.io/badge/version-7.3.1-f59e0b?style=flat-square)](CHANGELOG.md)
[![Live demo on Fly.io (v8.0 launch)](https://img.shields.io/badge/Live%20demo-Fly.io-7b2bbe?style=flat-square&logo=fly-dot-io&logoColor=white)](https://tryaisoc.com)
[![Render demo (one-click)](https://img.shields.io/badge/Render%20demo-one%20click-46e3b7?style=flat-square&logo=render&logoColor=white)](https://render.com/deploy?repo=https://github.com/beenuar/AiSOC)

[Live demo](https://tryaisoc.com) · [How AiSOC compares](#how-aisoc-compares) · [Public eval harness](apps/docs/docs/benchmark.md) · [Deploy in 60 seconds](#deploy-in-60-seconds) · [Deployment options](#deployment-options) · [Architecture](#architecture) · [Docs](apps/docs/)

<sub>The demo at <a href="https://tryaisoc.com">tryaisoc.com</a> is a self-hosted instance fronted by a Cloudflare Tunnel — when it's reachable, the stack is running locally on a maintainer's box. It can therefore go offline at any time. To run your own (in 3.5 min, with seeded data), see <a href="#one-shot-demo">One-shot demo</a>; to expose your own instance on your own domain via Cloudflare Tunnel, see <a href="#public-demo-on-your-own-domain">Public demo on your own domain</a>. <strong>The Fly.io demo at <a href="https://tryaisoc.com">tryaisoc.com</a> is the canonical AiSOC instance — the badge above links there.</strong></sub>

[![GitHub topics](https://img.shields.io/badge/topics-soc%20%7C%20siem%20%7C%20ai--security%20%7C%20mitre--attack-0ea5e9?style=flat-square)](https://github.com/beenuar/AiSOC/topics)

</div>

---

## What AiSOC is

AiSOC is a single self-hostable stack that ingests security events, correlates them, runs AI-driven investigation, and surfaces the result in a SOC console. The agent and the substrate are MIT-licensed, so you can read, fork, or replace either of them.

Three properties distinguish it from closed-source AI SOC vendors:

1. **Agent decisions are logged.** The Investigation Ledger stores the LLM prompt, the response, the evidence cited, and the downstream tool calls for every step of every run. Replays are available later.
2. **The substrate has a public eval harness in CI.** Five suites gate every PR targeting `main` / `develop`: a 200-incident synthetic dataset drawn from 55 distinct templates drives the MITRE-tactic, investigation-completeness, and response-quality gates (each reporting both a per-case mean and a per-template macro so a single broken template can't hide behind 199 working duplicates); a separately generated 1,000-alert noisy stream drives the alert-reduction gate; and a schema/coverage gate validates `synthetic_telemetry.jsonl` — the companion corpus of ~360 backing events across 14 log sources (Sysmon, Windows Security, M365 audit, Azure sign-in, CloudTrail, Linux auditd, journald, EDR, DNS, web access, Kubernetes audit, GitHub audit, VPN, DB audit) that connector and Sigma PRs can wire against. Alert reduction is a real measurement against the fixed alert stream; the three rubric-based suites are substrate self-consistency gates over deterministic templates. The [benchmark page](apps/docs/docs/benchmark.md) explains exactly which is which.
3. **It runs entirely on your infrastructure.** No callbacks to a vendor cloud and no data exfiltration for "model improvement."

The orchestrator is a ~600-line LangGraph in [`services/agents/`](services/agents/). It is small enough to read end-to-end, swap models in, and patch.

---

## What's new

`VERSION` is `7.3.1`; everything below is captured under `[Unreleased]` in [`CHANGELOG.md`](CHANGELOG.md) and will tag with the v8.0 cut.

**Latest — security & stability (May 27–28, 2026)** — hardening, dependency, and boot-reliability work merged into `main`.
- **Security Audit green** — `cryptography` floor raised to `44.0.1` to clear CVE-2024-12797 and later 42.x advisories across `services/connectors` and `services/osquery-tls`; advisories without an upstream fix are time-boxed (90-day expiry) in [`scripts/security_audit_ignores.txt`](scripts/security_audit_ignores.txt) ([#229](https://github.com/beenuar/AiSOC/pull/229)).
- **Tenant-isolation fix** — detection-loop suggestion lookups are now scoped to the caller's tenant, closing a cross-tenant read path ([#221](https://github.com/beenuar/AiSOC/pull/221)).
- **Full stack boots clean** — the reserved `window` column is now quoted and `p