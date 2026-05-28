> # Project Continuity Notice
>
> GSD is maintained by the **open-gsd** team at:
> **`open-gsd/get-shit-done-redux`**
>
> Use only these package names:
>
> - npm (main): `@opengsd/get-shit-done-redux`
> - npm (sdk): `@opengsd/gsd-sdk`
>
> The legacy upstream is outside open-gsd control. Based on public transition announcements and repository ownership reality, we strongly recommend removing legacy packages and migrating to `@opengsd/*`.
>
> Security status:
>
> - maintainers completed an internal security audit
> - maintainers report an independent review pass
> - no known active exploit was found in tracked source during those passes
>
> See:
>
> - continuity announcement: https://github.com/open-gsd/get-shit-done-redux/discussions/109
> - audit transparency report: https://github.com/open-gsd/get-shit-done-redux/discussions/119
>
> ---

<div align="center">

# GET SHIT DONE

**English** · [Português](README.pt-BR.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md)

**A light-weight meta-prompting, context engineering, and spec-driven development system for Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Cursor, Windsurf, and more.**

**Solves context rot — the quality degradation that happens as your AI fills its context window.**

[![npm version](https://img.shields.io/npm/v/%40opengsd%2Fget-shit-done-redux?style=for-the-badge&logo=npm&logoColor=white&color=CB3837)](https://www.npmjs.com/package/@opengsd/get-shit-done-redux)
[![npm downloads](https://img.shields.io/npm/dm/%40opengsd%2Fget-shit-done-redux?style=for-the-badge&logo=npm&logoColor=white&color=CB3837)](https://www.npmjs.com/package/@opengsd/get-shit-done-redux)
[![Tests](https://img.shields.io/github/actions/workflow/status/open-gsd/get-shit-done-redux/test.yml?branch=main&style=for-the-badge&logo=github&label=Tests)](https://github.com/open-gsd/get-shit-done-redux/actions/workflows/test.yml)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/mYgfVNfA2r)
[![GitHub stars](https://img.shields.io/github/stars/open-gsd/get-shit-done-redux?style=for-the-badge&logo=github&color=181717)](https://github.com/open-gsd/get-shit-done-redux)
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)

<br>

```bash
npx @opengsd/get-shit-done-redux@latest
```

**Works on Mac, Windows, and Linux.**

<br>

![GSD Install](assets/terminal.svg)

<br>

*"If you know clearly what you want, this WILL build it for you. No bs."*

*"I've done SpecKit, OpenSpec and Taskmaster — this has produced the best results for me."*

*"By far the most powerful addition to my Claude Code. Nothing over-engineered. Literally just gets shit done."*

<br>

**Trusted by engineers at Amazon, Google, Shopify, and Webflow.**

</div>

---

> [!IMPORTANT]
> **Returning to GSD?**
>
> Run `/gsd-map-codebase` to re-index your codebase, then `/gsd-new-project` to rebuild GSD's planning context. Your code is fine — GSD just needs its context rebuilt. See the [CHANGELOG](CHANGELOG.md) for what's new.

---

## Why We Continue Building GSD

GSD exists to help solo builders and small teams ship reliably with AI: clear specs, controlled context, and verification before release.

In May 2026, maintainers published a continuity announcement and migrated active development to `open-gsd/get-shit-done-redux` after trust and ownership concerns around the former upstream, including a meme-coin rug-pull incident publicly associated with that ecosystem.

The former creator and legacy lineage are no longer part of this program. This repository is the maintained continuation under open-gsd governance.

The current team continues release operations, triage, and security hardening in public. Audit status and follow-up security work are documented in Discussion #119 and linked issues.

---

## How It Works

The loop is six commands. Each one does exactly one thing.

### 1. Initialize

```bash
/gsd-new-project
```

Questions → research → requirements → roadmap. You approve it, then you're ready to build.

> **Already have code?** Run `/gsd-map-codebase` first. It analyzes your stack, architecture, and conventions so `/gsd-new-project` asks the right questions.

### 2. Discuss

```bash
/gsd-discuss-phase 1
```

Your roadmap has a sentence per phase. That's not enough to build it the way *you* imagine it. Discuss captures your decisions before anything gets planned: layouts, API shapes, error handling, data structures — whatever gray areas exist for this specific phase.

The output feeds directly into research and planning. Skip it, get reasonable defaults. Use it, get your vision.

### 3. Plan

```bash
/gsd-plan-phase 1
```

Research → plan → verify, in a loop until the plans pass. Each plan is small enough to execute in a fresh context window.

### 4. Execute

```bash
/gsd-execute-phase 1
```

Plans run in parallel waves. Each executor gets a fresh 200k-token context. Eac