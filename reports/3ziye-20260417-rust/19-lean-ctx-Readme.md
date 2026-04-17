```
  ██╗     ███████╗ █████╗ ███╗   ██╗     ██████╗████████╗██╗  ██╗
  ██║     ██╔════╝██╔══██╗████╗  ██║    ██╔════╝╚══██╔══╝╚██╗██╔╝
  ██║     █████╗  ███████║██╔██╗ ██║    ██║        ██║    ╚███╔╝ 
  ██║     ██╔══╝  ██╔══██║██║╚██╗██║    ██║        ██║    ██╔██╗ 
  ███████╗███████╗██║  ██║██║ ╚████║    ╚██████╗   ██║   ██╔╝ ██╗
  ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝   ╚═╝   ╚═╝  ╚═╝
             Context Runtime for AI Agents
```

<h3 align="center">Reduce Claude Code, Cursor & Copilot Token Costs by 99% — Open Source MCP Server</h3>

<p align="center">
  <strong>Shell Hook + Context Server · 42 tools · 10 read modes · 90+ patterns · Single Rust binary</strong>
</p>

<p align="center">
  <a href="https://github.com/yvgude/lean-ctx/actions/workflows/ci.yml"><img src="https://github.com/yvgude/lean-ctx/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/yvgude/lean-ctx/actions/workflows/security-check.yml"><img src="https://github.com/yvgude/lean-ctx/actions/workflows/security-check.yml/badge.svg" alt="Security"></a>
  <a href="https://crates.io/crates/lean-ctx"><img src="https://img.shields.io/crates/v/lean-ctx?color=%23e6522c" alt="crates.io"></a>
  <a href="https://crates.io/crates/lean-ctx"><img src="https://img.shields.io/crates/d/lean-ctx?color=%23e6522c" alt="Downloads"></a>
  <a href="https://www.npmjs.com/package/lean-ctx-bin"><img src="https://img.shields.io/npm/v/lean-ctx-bin?label=npm&color=%23cb3837" alt="npm"></a>
  <a href="https://www.npmjs.com/package/pi-lean-ctx"><img src="https://img.shields.io/npm/v/pi-lean-ctx?label=pi-lean-ctx&color=%23cb3837" alt="pi-lean-ctx"></a>
  <a href="https://aur.archlinux.org/packages/lean-ctx"><img src="https://img.shields.io/aur/version/lean-ctx?color=%231793d1" alt="AUR"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"></a>
  <a href="https://discord.gg/pTHkG9Hew9"><img src="https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://x.com/leanctx"><img src="https://img.shields.io/badge/𝕏-Follow-000000?logo=x&logoColor=white" alt="X/Twitter"></a>
  <img src="https://img.shields.io/badge/Telemetry-Zero-brightgreen?logo=shield&logoColor=white" alt="Zero Telemetry">
</p>

<p align="center">
  <a href="https://leanctx.com">Website</a> ·
  <a href="#-get-started-60-seconds">Install</a> ·
  <a href="#-how-lean-ctx-reduces-ai-token-costs">How It Works</a> ·
  <a href="#-42-intelligent-tools">Tools</a> ·
  <a href="#-shell-hook-patterns-90">Patterns</a> ·
  <a href="CHANGELOG.md">Changelog</a> ·
  <a href="https://discord.gg/pTHkG9Hew9">Discord</a>
</p>

---

<br>

> **lean-ctx** reduces LLM token consumption by **up to 99%** through three complementary strategies in a single binary — making AI coding faster, cheaper, and more effective.

<br>

## ⚡ How lean-ctx Reduces AI Token Costs

```
  Without lean-ctx:                              With lean-ctx:

  LLM ──"read auth.ts"──▶ Editor ──▶ File       LLM ──"ctx_read auth.ts"──▶ lean-ctx ──▶ File
    ▲                                  │           ▲                           │            │
    │      ~2,000 tokens (full file)   │           │   ~13 tokens (cached)     │ cache+hash │
    └──────────────────────────────────┘           └────── (compressed) ───────┴────────────┘

  LLM ──"git status"──▶  Shell  ──▶  git        LLM ──"git status"──▶  lean-ctx  ──▶  git
    ▲                                 │            ▲                       │              │
    │     ~800 tokens (raw output)    │            │   ~150 tokens         │ compress     │
    └─────────────────────────────────┘            └────── (filtered) ─────┴──────────────┘
```

| Strategy | How | Impact |
|:---|:---|:---|
| **Shell Hook** | Transparently compresses CLI output (90+ patterns) before it reaches the LLM | **60-95%** savings |
| **Context Server** | 46 MCP tools for cached reads, 10 read modes, deltas, dedup, memory, multi-agent sharing, adaptive compression | **74-99%** savings |
| **AI Tool Hooks** | One-command integration via `lean-ctx init --agent <tool>` | Works everywhere |

<br>

## 🎯 Token Savings — Real Numbers

| Operation | Freq | Without | With lean-ctx | Saved |
|:---|:---:|---:|---:|:---:|
| File reads (cached) | 15× | 30,000 | 195 | **99%** |
| File reads (map mode) | 10× | 20,000 | 2,000 | **90%** |
| ls / find | 8× | 6,400 | 1,280 | **80%** |
| git status/log/diff | 10× | 8,000 | 2,400 | **70%** |
| grep / rg | 5× | 8,000 | 2,400 | **70%** |
| cargo/npm build | 5× | 5,000 | 1,000 | **80%** |
| Test runners | 4× | 10,000 | 1,000 | **90%** |
| curl (JSON) | 3× | 1,500 | 165 | **89%** |
| docker ps/build | 3× | 900 | 180 | **80%** |
| **Session total** | | **~89,800** | **~10,620** | **88%** |

> Based on typical Cursor/Claude Code sessions with medium TypeScript/Rust projects. Cached re-reads cost ~13 tokens.

<br>

### Why lean-ctx?

AI coding tools like **Cursor**, **Claude Code**,