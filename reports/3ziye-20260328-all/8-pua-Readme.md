# pua

<p align="center">
  <img src="assets/hero.jpeg" alt="PUA Skill — Double Efficiency" width="250">
</p>

### Double your Codex / Claude Code productivity and output

[Telegram](https://t.me/+wBWh6h-h1RhiZTI1) · [Discord](https://discord.gg/EcyB3FzJND) · [Twitter/X](https://x.com/xsser_w) · [Landing Page](https://openpua.ai)

**[🇨🇳 中文](README.zh-CN.md)** | **[🇯🇵 日本語](README.ja.md)** | **🇺🇸 English**

<p align="center">
  <img src="assets/wechat-qr.jpg?v=5" alt="WeChat Group QR Code" width="250">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="assets/xiao.jpg" alt="Add Assistant on WeChat" width="250">
  <br>
  <sub>Scan to join WeChat group &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Add assistant on WeChat</sub>
</p>

<p>
  <img src="https://img.shields.io/badge/Claude_Code-black?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code">
  <img src="https://img.shields.io/badge/OpenAI_Codex_CLI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI Codex CLI">
  <img src="https://img.shields.io/badge/Cursor-000?style=flat-square&logo=cursor&logoColor=white" alt="Cursor">
  <img src="https://img.shields.io/badge/Kiro-232F3E?style=flat-square&logo=amazon&logoColor=white" alt="Kiro">
  <img src="https://img.shields.io/badge/CodeBuddy-00B2FF?style=flat-square&logo=tencent-qq&logoColor=white" alt="CodeBuddy">
  <img src="https://img.shields.io/badge/OpenClaw-FF6B35?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJMNCA3djEwbDggNSA4LTV2LTEweiIgZmlsbD0id2hpdGUiLz48L3N2Zz4=&logoColor=white" alt="OpenClaw">
  <img src="https://img.shields.io/badge/Antigravity-4285F4?style=flat-square&logo=google&logoColor=white" alt="Google Antigravity">
  <img src="https://img.shields.io/badge/OpenCode-00D4AA?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTkuNCA1LjJMMyAxMmw2LjQgNi44TTIxIDEybC02LjQtNi44TTE0LjYgMTguOCIgc3Ryb2tlPSJ3aGl0ZSIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIyIi8+PC9zdmc+&logoColor=white" alt="OpenCode">
  <img src="https://img.shields.io/badge/VSCode_Copilot-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white" alt="VSCode Copilot">
  <img src="https://img.shields.io/badge/🌐_Multi--Language-blue?style=flat-square" alt="Multi-Language">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License">
</p>

> Most people think this project is a joke. That's the biggest misconception. It genuinely doubles your Codex / Claude Code productivity and output.

An AI Coding Agent skill plugin that uses corporate PUA rhetoric (Chinese version) / PIP — Performance Improvement Plan (English version) from Chinese & Western tech giants to force AI to exhaust every possible solution before giving up. Supports **Claude Code**, **OpenAI Codex CLI**, **Cursor**, **Kiro**, **CodeBuddy**, **OpenClaw**, **Google Antigravity**, **OpenCode**, and **VSCode (GitHub Copilot)**. Three capabilities:

1. **PUA Rhetoric** — Makes AI afraid to give up
2. **Debugging Methodology** — Gives AI the ability not to give up
3. **Proactivity Enforcement** — Makes AI take initiative instead of waiting passively

## Live Demo

[https://openpua.ai](https://openpua.ai) · [📖 Beginner Guide](https://openpua.ai/guide.html)

## Real Case: MCP Server Registration Debugging

A real debugging scenario. The agent-kms MCP server failed to load. The AI kept spinning on the same approach (changing protocol format, guessing version numbers) multiple times until the user manually triggered `/pua`.

**L3 Triggered → 7-Point Checklist Enforced:**

![PUA L3 triggered — stopped guessing, executed systematic checklist, found real error in MCP logs](assets/pua1.jpg)

**Root Cause Located → Traced from Logs to Registration Mechanism:**

![Root cause — claude mcp managed server registration differs from manual .claude.json editing](assets/pua2.jpg)

**Retrospective → PUA's Actual Impact:**

![Conversation retrospective — PUA skill forced stop on spinning, systematic checklist drove discovery of previously unchecked Claude Code MCP log directory](assets/pua3.jpg)

**Key Turning Point:** The PUA skill forced the AI to stop spinning on the same approach (changing protocol format, guessing version numbers) and instead execute the 7-point checklist. Read error messages word by word → Found Claude Code's own MCP log directory → Discovered that `claude mcp` registration mechanism differs from manual `.claude.json` editing → Root cause resolved.

## The Problem: AI's Five Lazy Patterns

| Pattern | Behavior |
|---------|----------|
| Brute-force retry | Runs the same command 3 times, then says "I cannot solve this" |
| Blame the user | "I suggest you handle this manually" / "Probably an environment issue" / "Need more context" |
| Idle tools | Has WebSearch but d