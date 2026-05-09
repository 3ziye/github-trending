# Open Design

> **The open-source alternative to [Claude Design][cd].** Local-first, web-deployable, BYOK at every layer — **16 coding-agent CLIs** auto-detected on your `PATH` (Claude Code, Codex, Devin for Terminal, Cursor Agent, Gemini CLI, OpenCode, Qwen, Qoder CLI, GitHub Copilot CLI, Hermes, Kimi, Pi, Kiro, Kilo, Mistral Vibe, DeepSeek TUI) become the design engine, driven by **31 composable Skills** and **72 brand-grade Design Systems**. No CLI? An OpenAI-compatible BYOK proxy is the same loop minus the spawn.

<p align="center">
  <img src="docs/assets/banner.png" alt="Open Design — editorial cover: design with the agent on your laptop" width="100%" />
</p>

<p align="center">
  <a href="https://github.com/nexu-io/open-design/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/nexu-io/open-design?style=for-the-badge&labelColor=0d1117&color=ffd700&logo=github&logoColor=white" /></a>
  <a href="https://github.com/nexu-io/open-design/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/nexu-io/open-design?style=for-the-badge&labelColor=0d1117&color=2ecc71&logo=github&logoColor=white" /></a>
  <a href="https://github.com/nexu-io/open-design/issues"><img alt="Issues" src="https://img.shields.io/github/issues/nexu-io/open-design?style=for-the-badge&labelColor=0d1117&color=ff6b6b&logo=github&logoColor=white" /></a>
  <a href="https://github.com/nexu-io/open-design/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/nexu-io/open-design?style=for-the-badge&labelColor=0d1117&color=9b59b6&logo=github&logoColor=white" /></a>
  <a href="https://github.com/nexu-io/open-design/graphs/contributors"><img alt="Contributors" src="https://img.shields.io/github/contributors/nexu-io/open-design?style=for-the-badge&labelColor=0d1117&color=3498db&logo=github&logoColor=white" /></a>
  <a href="https://github.com/nexu-io/open-design/commits/main"><img alt="Commit activity" src="https://img.shields.io/github/commit-activity/m/nexu-io/open-design?style=for-the-badge&labelColor=0d1117&color=e67e22&logo=git&logoColor=white" /></a>
  <a href="https://github.com/nexu-io/open-design/commits/main"><img alt="Last commit" src="https://img.shields.io/github/last-commit/nexu-io/open-design?style=for-the-badge&labelColor=0d1117&color=8e44ad&logo=git&logoColor=white" /></a>
</p>

<p align="center">
  <a href="https://open-design.ai/"><img alt="Download" src="https://img.shields.io/badge/download-open--design.ai-ff6b35?style=flat-square" /></a>
  <a href="https://github.com/nexu-io/open-design/releases"><img alt="Latest release" src="https://img.shields.io/github/v/release/nexu-io/open-design?style=flat-square&color=blueviolet&label=release&include_prereleases&display_name=tag" /></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=flat-square" /></a>
  <a href="#supported-coding-agents"><img alt="Agents" src="https://img.shields.io/badge/agents-16%20CLIs%20%2B%20BYOK%20proxy-black?style=flat-square" /></a>
  <a href="#design-systems"><img alt="Design systems" src="https://img.shields.io/badge/design%20systems-72-orange?style=flat-square" /></a>
  <a href="#skills"><img alt="Skills" src="https://img.shields.io/badge/skills-31-teal?style=flat-square" /></a>
  <a href="https://discord.gg/qhbcCH8Am4"><img alt="Discord" src="https://img.shields.io/badge/discord-join-5865F2?style=flat-square&logo=discord&logoColor=white" /></a>
  <a href="https://x.com/nexudotio"><img alt="Follow @nexudotio on X" src="https://img.shields.io/badge/follow-%40nexudotio-1DA1F2?style=flat-square&logo=x&logoColor=white" /></a>
  <a href="QUICKSTART.md"><img alt="Quickstart" src="https://img.shields.io/badge/quickstart-3%20commands-green?style=flat-square" /></a>
</p>

<p align="center"><b>English</b> · <a href="README.es.md">Español</a> · <a href="README.pt-BR.md">Português (Brasil)</a> · <a href="README.de.md">Deutsch</a> · <a href="README.fr.md">Français</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ko.md">한국어</a> · <a href="README.ja-JP.md">日本語</a> · <a href="README.ar.md">العربية</a> · <a href="README.ru.md">Русский</a> · <a href="README.uk.md">Українська</a> · <a href="README.tr.md">Türkçe</a></p>

---

## Why this exists

Anthropic's [Claude Design][cd] (released 2026-04-17, Opus 4.7) showed what happens when an LLM stops writing prose and starts shipping design artifacts. It went viral — and stayed closed-source, paid-only, cloud-only, locked to Anthropic's model and Anthropic's skills. There is no checkout, no self-host, no Vercel deploy, no swap-in-your-own-agent.

**Open Design (OD) is the open-source alternative.** Same loop, same artifact-first mental model, none of the lock-in. We don't ship an agent — the strongest coding agents already live on your laptop. We wire them into a skill-driven design workflow that runs locally with `pnpm tools-dev`, can deploy the web layer to Vercel