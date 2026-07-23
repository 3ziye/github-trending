<h1 align="center">
  <img src="public/penecho-readme-header.png" alt="PenEcho" width="760">
</h1>

<p align="center"><strong>Think with AI beyond the chat box.</strong></p>

<p align="center">PenEcho is a shared canvas where handwriting, equations, diagrams, and spatial context become part of the conversation.</p>

<p align="center">
  <a href="https://discord.gg/3jrPJ3mXdX">
    <img src="https://img.shields.io/badge/Discord-Join%20the%20community-5865F2?style=for-the-badge&amp;logo=discord&amp;logoColor=white" alt="Join the PenEcho Discord">
  </a>
  <a href="https://github.com/penecho/penecho/stargazers">
    <img src="https://img.shields.io/github/stars/penecho/penecho?style=for-the-badge&amp;logo=github&amp;logoColor=white&amp;color=f5b301" alt="Star PenEcho on GitHub">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-AGPL%20v3-blue?style=for-the-badge" alt="License: AGPL v3">
  </a>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> &bull;
  <a href="#recommended-model-configurations">Recommended Models</a> &bull;
  <a href="docs/architecture.md">Architecture</a> &bull;
  <a href="https://discord.gg/3jrPJ3mXdX">Discord</a>
</p>

<p align="center">
  <img src="https://github.com/penecho/penecho/releases/download/v0.1.0/penecho_plugins_sub_x10.webp" alt="PenEcho plugins demo" width="100%">
</p>

<p align="center">
  <img src="https://github.com/penecho/penecho/releases/download/v0.1.0/penecho_full_demo.webp" alt="PenEcho full demo" width="100%">
</p>

## A Kimi Open Source Friend

<p align="center">
  <a href="https://www.kimi.com/code?aff=penecho">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/assets/kimi-open-source-friends-dark.svg">
      <img alt="Kimi Open Source Friends" src="docs/assets/kimi-open-source-friends-light.svg">
    </picture>
  </a>
</p>

PenEcho is an official member of **Kimi Open Source Friends**, [Moonshot AI](https://www.kimi.com/)'s program supporting outstanding open source projects. The Kimi team backs PenEcho's development with API credits, and Kimi K3 is one of the [recommended models](#recommended-model-configurations) for demanding canvas work — accurate on handwriting, strong on diagrams, and fast in practice.

Using these links directly supports the project:

- **[Kimi Code](https://www.kimi.com/code?aff=penecho)** — Kimi's coding subscription, available worldwide
- **[Kimi Open Platform · China](https://platform.kimi.com?aff=penecho)** — API access for mainland China
- **[Kimi Open Platform · Global](https://platform.kimi.ai?aff=penecho)** — API access for the rest of the world

## Contents

- [Quick start](#quick-start)
- [Think on the canvas](#think-on-the-canvas)
- [What's new in 0.7.0](#whats-new-in-070)
- [What's new in 0.6.0](#whats-new-in-060)
- [Animation scenes](#animation-scenes-in-060)
- [How it works](#how-it-works)
- [Recommended model configurations](#recommended-model-configurations)
- [Token use and cost](#token-use-and-cost)
- [Safe deployment](#safe-deployment)
- [Useful configuration](#useful-configuration)
- [Build it with us](#build-it-with-us)
- [License and commercial use](#license-and-commercial-use)

## Quick start

You need [Node.js 18.17+](https://nodejs.org/) and one of the following: an API key, an authenticated [Codex CLI](https://developers.openai.com/codex/cli), or an authenticated [Claude Code CLI](https://code.claude.com/docs/en/overview).

```bash
npm install -g penecho
penecho configure
penecho
```

Interactive starts print the current version immediately. After the server is listening, PenEcho displays `Checking latest PenEcho version...` and queries npm without delaying availability. If a newer version exists, press Enter at the default `Y` prompt to install it globally. The current service then stops without launching a background process; run `penecho` again when you are ready to start the updated version. When the installed version is current, PenEcho says so explicitly. Offline checks and non-interactive starts continue without blocking the running service.

`penecho configure` opens the interactive configuration center. Its main menu contains `LLM source`, `Settings`, and `Exit`. Use the arrow keys and Enter to navigate:

- `LLM source -> Claude CLI` selects a detected, recommended, default, or manually entered model and an effort level. Opus 4.8 or newer is recommended; Sonnet and Opus 4.6 can respond but may produce weaker canvas results.
- `LLM source -> Codex CLI` selects a model and effort. GPT-5.5 or newer is required for good results, `gpt-5.6-sol` is recommended, and `xhigh` is the highest listed Codex effort.
- `LLM source -> API` selects the OpenAI-compatible or Anthropic/Claude-compatible request format, then asks for the URL, model, effort, and hidden key. Kimi K3 ([China](https://platform.kimi.com?aff=penecho) / [Global](https://platform.kimi.ai?aff=penecho)) uses the OpenAI-compatible format with model `k3`; current testing recommends `