<p align="center">
  <img src="assets/mascot-no-bg.png" width="200" alt="Zippy — ZeptoClaw mascot">
</p>
<h1 align="center">ZeptoClaw</h1>
<p align="center">
  <strong>Ultra-lightweight personal AI assistant.</strong>
</p>
<p align="center">
  <a href="https://zeptoclaw.com/docs/"><img src="https://img.shields.io/badge/docs-zeptoclaw.com-3b82f6?style=for-the-badge&logo=bookstack&logoColor=white" alt="Documentation"></a>
</p>
<p align="center">
  <a href="https://github.com/qhkm/zeptoclaw/actions/workflows/ci.yml"><img src="https://github.com/qhkm/zeptoclaw/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/qhkm/zeptoclaw/releases/latest"><img src="https://img.shields.io/github/v/release/qhkm/zeptoclaw?color=blue" alt="Release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue" alt="License"></a>
</p>

---

```
$ zeptoclaw agent --stream -m "Analyze our API for security issues"

🤖 ZeptoClaw — Streaming analysis...

  [web_fetch]        Fetching API docs...
  [shell]            Running integration tests...
  [longterm_memory]  Storing findings...

→ Found 12 endpoints, 3 missing auth headers, 1 open redirect
→ Saved findings to long-term memory under "api-audit"

✓ Analysis complete in 4.2s
```

We studied the best AI assistants — and their tradeoffs. OpenClaw's integrations without the 100MB. NanoClaw's security without the TypeScript bundle. PicoClaw's size without the bare-bones feature set. One Rust binary with 32 tools, 9 channels, 9 providers, and 6 sandbox runtimes.

<p align="center">
  <img src="https://img.shields.io/badge/binary-~6MB-3b82f6" alt="~6MB binary">
  <img src="https://img.shields.io/badge/startup-~50ms-3b82f6" alt="~50ms startup">
  <img src="https://img.shields.io/badge/RAM-~6MB-3b82f6" alt="~6MB RAM">
  <img src="https://img.shields.io/badge/tests-2%2C900%2B-3b82f6" alt="2,900+ tests">
  <img src="https://img.shields.io/badge/providers-9-3b82f6" alt="9 providers">
</p>

## Why ZeptoClaw

We studied what works — and what doesn't.

**OpenClaw** proved an AI assistant can handle 12 channels and 100+ skills. But it costs 100MB and 400K lines. **NanoClaw** proved security-first is possible. But it's still 50MB of TypeScript. **PicoClaw** proved AI assistants can run on $10 hardware. But it stripped out everything to get there.

**ZeptoClaw** took notes. The integrations, the security, the size discipline — without the tradeoffs each one made. One 6MB Rust binary that starts in 50ms, uses 6MB of RAM, and ships with container isolation, prompt injection detection, and a circuit breaker provider stack.

## Security

AI agents execute code. Most frameworks trust that nothing will go wrong.

The OpenClaw ecosystem has seen CVE-2026-25253 (CVSS 8.8 — cross-site WebSocket hijacking to RCE), ClawHavoc (341 malicious skills, 9,000+ compromised installations), and 42,000 exposed instances with auth bypass. ZeptoClaw was built with this threat model in mind.

| Layer | What it does |
|-------|-------------|
| **6 Sandbox Runtimes** | Docker, Apple Container, Landlock, Firejail, Bubblewrap, or native — per request |
| **Prompt Injection Detection** | Aho-Corasick multi-pattern matcher (17 patterns) + 4 regex rules |
| **Secret Leak Scanner** | 22 regex patterns catch API keys, tokens, and credentials before they reach the LLM |
| **Policy Engine** | 7 rules blocking system file access, crypto key extraction, SQL injection, encoded exploits |
| **Input Validator** | 100KB limit, null byte detection, whitespace ratio analysis, repetition detection |
| **Shell Blocklist** | Regex patterns blocking reverse shells, `rm -rf`, privilege escalation |
| **SSRF Prevention** | DNS pinning, private IP blocking, IPv6 transition guard, scheme validation |
| **Chain Alerting** | Detects dangerous tool call sequences (write→execute, memory→execute) |
| **Tool Approval Gate** | Require explicit confirmation before executing dangerous tools |

Every layer runs by default. No flags to remember, no config to enable.

## Install

```bash
# One-liner (macOS / Linux)
curl -fsSL https://raw.githubusercontent.com/qhkm/zeptoclaw/main/install.sh | sh

# Homebrew
brew install qhkm/tap/zeptoclaw

# Docker
docker pull ghcr.io/qhkm/zeptoclaw:latest

# Build from source
cargo install zeptoclaw --git https://github.com/qhkm/zeptoclaw
```

## Uninstall

```bash
# Remove ZeptoClaw state (~/.zeptoclaw)
zeptoclaw uninstall --yes

# Also remove a direct-install binary from ~/.local/bin or /usr/local/bin
zeptoclaw uninstall --remove-binary --yes

# Package-managed installs still use their package manager
brew uninstall qhkm/tap/zeptoclaw
cargo uninstall zeptoclaw
```

## Quick Start

```bash
# Interactive setup (walks you through API keys, channels, workspace)
zeptoclaw onboard

# Talk to your agent
zeptoclaw agent -m "Hello, set up my workspace"

# Stream responses token-by-token
zeptoclaw agent --stream -m "Explain async Rust"

# Use a built-in template
zeptoclaw agent 