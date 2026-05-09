# Open CoDesign

**简体中文**: [README.zh-CN.md](./README.zh-CN.md)

> Your prompts. Your model. Your laptop.
>
> Turn prompts into polished artifacts — locally, openly, and with whichever model you already pay for.

[Website](https://opencoworkai.github.io/open-codesign/) · [Quickstart](#quickstart) · [What's new](https://github.com/OpenCoworkAI/open-codesign/releases) · [Changelog](./CHANGELOG.md) · [Discussions](https://github.com/OpenCoworkAI/open-codesign/discussions) · [Docs](https://opencoworkai.github.io/open-codesign/quickstart) · [Contributing](./CONTRIBUTING.md) · [Security](./SECURITY.md)

**Open-source alternative to:** [Claude Design](https://opencoworkai.github.io/open-codesign/claude-design-alternative) · [v0 by Vercel](https://opencoworkai.github.io/open-codesign/v0-alternative) · [Lovable](https://opencoworkai.github.io/open-codesign/lovable-alternative) · [Bolt.new](https://opencoworkai.github.io/open-codesign/bolt-alternative) · [Figma AI](https://opencoworkai.github.io/open-codesign/figma-ai-alternative)

<p align="center">
  <img src="https://raw.githubusercontent.com/OpenCoworkAI/open-codesign/main/website/public/screenshots/product-hero.png" alt="Open CoDesign — prompt on the left, live artifact on the right" width="1000" />
</p>

<p align="center">
  <a href="https://github.com/OpenCoworkAI/open-codesign/releases"><img alt="GitHub release" src="https://img.shields.io/github/v/release/OpenCoworkAI/open-codesign?label=release&color=c96442" /></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-blue" /></a>
  <a href="https://github.com/OpenCoworkAI/open-codesign/actions"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/OpenCoworkAI/open-codesign/ci.yml?label=CI" /></a>
  <a href="https://github.com/OpenCoworkAI/open-codesign/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/OpenCoworkAI/open-codesign?style=social" /></a>
  <a href="#community"><img alt="WeChat Group" src="https://img.shields.io/badge/WeChat-Group-07C160?logo=wechat&logoColor=white" /></a>
</p>

<p align="center">
  <a href="https://github.com/OpenCoworkAI/open-codesign/commits/main"><img alt="Last commit" src="https://img.shields.io/github/last-commit/OpenCoworkAI/open-codesign?label=last%20commit&color=40b4a1" /></a>
  <a href="https://github.com/OpenCoworkAI/open-codesign/pulse"><img alt="Commit activity" src="https://img.shields.io/github/commit-activity/m/OpenCoworkAI/open-codesign?label=commits%2Fmonth" /></a>
  <a href="https://github.com/OpenCoworkAI/open-codesign/graphs/contributors"><img alt="Contributors" src="https://img.shields.io/github/contributors/OpenCoworkAI/open-codesign" /></a>
  <a href="https://github.com/OpenCoworkAI/open-codesign/releases"><img alt="Downloads" src="https://img.shields.io/github/downloads/OpenCoworkAI/open-codesign/total?label=downloads&color=6c5ce7" /></a>
</p>

<p align="center">
  <sub><code>claude-code</code> · <code>claude-design-alternative</code> · <code>v0-alternative</code> · <code>bolt-alternative</code> · <code>lovable-alternative</code> · <code>figma-alternative</code> · <code>ai-design</code> · <code>design-to-code</code> · <code>prompt-to-design</code> · <code>ai-prototyping</code> · <code>desktop-design-tool</code> · <code>byok</code> · <code>local-first</code> · <code>multi-model</code> · <code>electron</code></sub>
</p>

---

## What's new

- **v0.2.0** *(in preparation, expected in about a week)* — Agentic Design: workspace-backed design sessions · permissioned file/tool loop · lazy skills and scaffolds · `DESIGN.md` design systems
- **v0.1.4** *(2026-04-23)* — AI image generation · ChatGPT Plus/Codex subscription support · CLIProxyAPI one-click import · API config hardening
- **v0.1.3** *(2026-04-21)* — Gemini `models/` prefix fix · OpenAI-compatible relay "instructions required" fix · third-party relay SSE-truncation hint
- **v0.1.2** *(2026-04-21)* — Release pipeline · Homebrew / winget / Scoop packaging manifests

[Full release history →](https://github.com/OpenCoworkAI/open-codesign/releases) · [Changelog →](./CHANGELOG.md)

---

## What it is

Turn a prompt into a polished prototype, slide deck, or marketing asset, locally, with the model you already use.

**Open CoDesign is the open-source Claude Design alternative** — built for people who want the speed of AI-native design tools without subscription lock-in, cloud-only workflows, or being forced onto a single provider. An MIT-licensed desktop app, local-first from day one, with BYOK for any model (Claude, GPT, Gemini, DeepSeek, Kimi, GLM, Ollama, or any OpenAI-compatible endpoint). One-click import of your existing Claude Code or Codex API key gets you running in under 90 seconds.

---

## See it generate

From a blank prompt to a finished artifact, the agent plans, writes, self-checks, and ships something with hover states, tabs, and empty states already wired up:

![Generate a design from scratch](https://raw.githubusercontent