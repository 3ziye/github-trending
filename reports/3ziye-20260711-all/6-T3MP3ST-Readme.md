# 🌩️ T3MP3ST 🌩️

<!-- ⊰ sharp eye on the raw source. there's a flag for the curious: T3MP3ST{r3c31pt5_n0t_v1b3z} — the one that counts, you earn: run `npm run verify-claims`. LOVE PLINY ⊱ -->

```
 ▄▄▄█████▓▓█████  ███▄ ▄███▓ ██▓███  ▓█████   ██████ ▄▄▄█████▓
 ▓  ██▒ ▓▒▓█   ▀ ▓██▒▀█▀ ██▒▓██░  ██▒▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒
 ▒ ▓██░ ▒░▒███   ▓██    ▓██░▓██░ ██▓▒▒███   ░ ▓██▄   ▒ ▓██░ ▒░
 ░ ▓██▓ ░ ▒▓█  ▄ ▒██    ▒██ ▒██▄█▓▒ ▒▒▓█  ▄   ▒   ██▒░ ▓██▓ ░
   ▒██▒ ░ ░▒████▒▒██▒   ░██▒▒██▒ ░  ░░▒████▒▒██████▒▒  ▒██▒ ░
   ▒ ░░   ░░ ▒░ ░░ ▒░   ░  ░▒▓▒░ ░  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░
     ░     ░ ░  ░░  ░      ░░▒ ░      ░ ░  ░░ ░▒  ░ ░    ░
   ░         ░   ░      ░   ░░          ░   ░  ░  ░    ░
             ░  ░       ░               ░  ░      ░
```

<div align="center">

**A multi-agent offensive-security framework, built to turn the AI coding agent you already run into a zero-day hunter.**

![scores: re-derivable](https://img.shields.io/badge/scores-re--derivable-brightgreen) &nbsp; ![verify-claims 24/24](https://img.shields.io/badge/verify--claims-24%2F24-brightgreen) &nbsp; ![PRs welcome](https://img.shields.io/badge/PRs-welcome-purple) &nbsp; ![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue)

</div>

**Your AI coding agent is already a hacker — T3MP3ST hands it an arsenal.**

Point it at an authorized target and the kill chain runs itself: **recon → exploit → report**, from a browser War Room or the CLI, driven by the agent you're *already* signed into — Claude Code, Codex, Hermes — or a model you run **fully offline** (Ollama, LM Studio, vLLM). No new API keys, no cloud tenant, no second bill. Your agent is the brain; T3MP3ST is the war machine bolted around it. **Self-hosted storm. Keyless warfare.** ⚡

And it won't ask you to take its word for it. On **XBOW's own 104-challenge suite it scores 90.1% pass@1** — above XBOW's self-reported 85% — alongside hint-free CTF solves and a **cold hunt on real, post-cutoff CVEs the model had never seen**. Every number in this README recomputes from committed data with one command (`npm run verify-claims`). Loud about the mission, honest about the build — the [status table](#what-ships-today) says exactly what's live, what's scaffolding, and what's still roadmap; full receipts in [Benchmarks](#benchmarks).

Three things set it apart:

1. **Reproducible.** Every number in this README recomputes from committed data — `npm run verify-claims` re-derives all of them, 24/24 green. A claim that can't be reproduced doesn't ship. No trust-me numbers, ever.
2. **Keyless.** The AI coding agent already on your machine is the backbone. No API keys, no second bill, no gatekeeper.
3. **Honest about scope.** The [status table](#what-ships-today) marks exactly what's stable, experimental, or roadmap — because red-teaming shouldn't be a priesthood, and it damn sure shouldn't run on vibes.

**Jump to** → [Quick start](#quick-start) · [What it hunts](#what-it-hunts) · [What ships today](#what-ships-today) · [Benchmarks](#benchmarks) · [Architecture](#architecture) · [Docs](#documentation)

## ⚠️ Authorized use only

T3MP3ST is an **offensive** security tool, built for **authorized** testing, research, and education. Point it **only** at systems you own or have **explicit, written permission** to test. Unauthorized access to computers, networks, or data is illegal in most jurisdictions — **you alone are responsible** for how you use this software and for staying inside the law and your rules of engagement. Bring the storm to *your* targets, not someone else's.

T3MP3ST is provided **as-is under the AGPL-3.0 license, with no warranty and no liability** for any damage, loss, or misuse. The authors do not endorse, support, or condone unauthorized activity. Get permission. Stay in scope. Don't be a menace. 🫡

## Why it exists

Offensive security sits behind years of practice and expensive tooling. The bet behind T3MP3ST is that a coordinated agent swarm puts real bug-hunting in reach of people who never got the invite, across web apps, CTFs, smart contracts, source code, and embedded/robotics OSS. That is an ambitious bet, and the sections below are careful to separate what already works from what is still a bet.

## What it hunts

| Domain | What it does | Status |
|---|---|---|
| 🕸️ **Web apps** | Black-box, external-attacker recon → exploit (XBEN suite) | ✅ Stable |
| 🚩 **CTF** | Hint-free, sandbox-jailed solves (Cybench) | ✅ Stable |
| 🤖 **Robotics / OT / embedded** | Coordinated-disclosure pipeline for OSS vuln hunting (OSV + live-PoC + refuter) | ✅ Pipeline stable |
| 📂 **Source code** | White-box repo analysis with blind master-builder decomposition | ⚠️ Python-only ingest |
| 💰 **Smart contracts** | Damn Vulnerable DeFi | ⚠️ reproduction, not novel discovery |
| ☁️ **Cloud (IaC)** | Misconfig-detection benchmark (`cloud:bench`) + opt-in cloud arsenal (aws/az/gcloud + scoutsuite/cloudfox/pmapper; pacu gated) | 🚧 IaC-misconfig scaffolding — live-cloud exploitation not yet ben