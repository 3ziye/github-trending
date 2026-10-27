<div align="center">

# ARTEX — Global Edition

**An autonomous penetration-testing system driven by LLM multi-agents** (Go backend + Next.js frontend)

The UI and generated output default to English, and **can be switched to Korean, Chinese, Spanish or Japanese in Settings (System → Settings → Display language).** Changing the language also changes the language of agent-generated reports, summaries and chat replies.

English · [한국어](README.ko.md) · [中文](README.zh.md) · [Español](README.es.md) · [日本語](README.ja.md)

[![ci](https://github.com/jiwoochris/artex-global/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/jiwoochris/artex-global/actions/workflows/ci.yml) [![detections](https://github.com/jiwoochris/artex-global/actions/workflows/detections.yml/badge.svg?branch=main)](https://github.com/jiwoochris/artex-global/actions/workflows/detections.yml) [![web](https://github.com/jiwoochris/artex-global/actions/workflows/web.yml/badge.svg?branch=main)](https://github.com/jiwoochris/artex-global/actions/workflows/web.yml) [![license: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-blue.svg)](LICENSE)

</div>

---

> ## 🚨 Security & misuse warning — read this first
>
> **This repository is published for use only within authorized environments, and only to build defensive and detection capabilities.**
>
> ARTEX is an autonomous offensive tool powerful enough to carry an attack from reconnaissance through intrusion to data exfiltration with little human involvement, so the harm from misuse is correspondingly large. In October 2026, several Korean news outlets reported that investigators had found indications the upstream ARTEX was used in personal-data breaches targeting Korean financial institutions; the related investigation is ongoing. This global edition is not published to help attackers. Its purpose is to help defenders understand how such autonomous AI attacks work and build the capability to detect and block them.
>
> - **Unauthorized use is a crime in itself.** Do not run any scanning, probing, or exploitation against systems you do not own or for which you lack explicit written authorization. In the Republic of Korea, unauthorized intrusion into an information and communications network violates the Network Act, and the Personal Information Protection Act also applies where personal data is involved.
> - **Do not target live services or other parties' assets.** Verify only in learning, research, and locally isolated environments you own (deliberately vulnerable targets such as OWASP Juice Shop or DVWA).
> - **Read it from a defender's point of view.** This repository also compiles defensive and detection material, such as detection signatures and hardening checklists, for autonomous AI attacks. → **[Defense & Detection Guide](docs/defense-en.md)** (also in [Korean](docs/defense-ko.md))
>
> If you do not agree to this warning and to the [usage restrictions and disclaimer](#license-and-disclaimer) below, do not download or use this repository.

---

> **This repository is a localized edition of the Chinese open-source project [Autumn-27/ARTEX](https://github.com/Autumn-27/ARTEX) (AGPL-3.0 · upstream repository currently unreachable, checked 2026-10), adapted so that users and teams worldwide can adopt it as-is.** To preserve the agents' decision-making performance, the internal reasoning prompts are kept in the original language, and only the user-facing output (findings, summaries, reports, chat replies) is forced into the selected language (English by default). See ["Why a global edition"](#why-a-global-edition) below for the rationale.

ARTEX is a system in which several LLM-driven agents autonomously run a penetration test: they **break goals down on their own, execute real tools, and accumulate discovered assets and vulnerabilities into a graph** as they go. A single Go binary ships with the Next.js frontend embedded, and all data is stored in PostgreSQL.

> **Note on this edition's language.** This fork makes the product usable in five languages — **English (default), Korean, Chinese, Spanish, and Japanese** — selectable in Settings. The user-facing output is forced into the selected language, while the agents' internal reasoning prompts are kept in the original language to preserve benchmarked performance. See [Configuration](#configuration) for how the output language is enforced by a small code-fixed directive.

---

## ⚠️ Read first — authorized use and legal notice

ARTEX may be used **only against targets you own or for which you have explicit written authorization.** Any scanning, probing, or exploitation beyond the authorized scope may itself be illegal.

- In the Republic of Korea, intruding into or disrupting another party's information and communications network without authorization violates the **Act on Promotion of Information and Communications Network Utilization and Information Protection** (정보통신망법).
- Personal data collected or exposed during a penetratio