# Gopher Code

<p align="center">
  <img src="assets/go-gopher-pixel-art.png" width="200" alt="Gopher Code mascot — pixel art Go gopher">
</p>

<p align="center">
  <strong>Gopher Code, rewritten from scratch in Go. Zero Node.js. Zero Electron. One binary.</strong>
</p>

<p align="center">
  <img src="assets/demo.gif" alt="Gopher Code demo">
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Go-1.24+-00ADD8?style=for-the-badge&logo=go&logoColor=white">
    <img src="https://img.shields.io/badge/Go-1.24+-00ADD8?style=for-the-badge&logo=go&logoColor=white" alt="Go 1.24+">
  </picture>
  <img src="https://img.shields.io/badge/Gopher_Code-v2_Parity-blueviolet?style=for-the-badge&logo=go&logoColor=white" alt="Gopher Code v2 Parity">
  <img src="https://img.shields.io/badge/Tools-33_Built--In-orange?style=for-the-badge" alt="33 Tools">
  <img src="https://img.shields.io/badge/Binary-Single_Static-success?style=for-the-badge" alt="Single Binary">
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="MIT License">
</p>

<p align="center">
  <strong>513K lines of TypeScript &rarr; clean, idiomatic Go.</strong><br>
  <sub>Starts in 12ms. No runtime dependencies. Cross-compiles everywhere Go does.</sub>
</p>

---

> [!IMPORTANT]
> **This is an active ground-up rewrite.** Gopher Code is not a wrapper, binding, or transpilation.
> Every subsystem of Claude Code v2.1.88 has been analyzed and rebuilt natively in Go using
> modern 2026 packages. See [Porting Status](#porting-status) for current progress.

---

## Why This Exists

An incredible tool trapped inside a 500K-line TypeScript monolith that ships
with Node.js, a bundled Ink/React renderer, native addons for every platform, and a `node_modules`
tree deeper than the Mariana Trench.

Gopher Code asks: **what if it was just a binary?**

- **12ms cold start** vs multi-second Node.js bootstrap
- **Single static binary** — `go build` and ship, no `npm install`, no native addons
- **Native concurrency** — goroutines for parallel tool execution, not Promise.all
- **Cross-compile in seconds** — `GOOS=linux GOARCH=arm64 go build` and done
- **Memory efficient** — no V8 heap, no garbage collector pauses from React re-renders
- **Hackable** — read the source in an afternoon, not a week

---

## Repository Layout

```text
gopher/
├── cmd/gopher/       # CLI entry point & REPL
│   └── main.go
├── pkg/                   # Core packages
│   ├── compact/           # Token budget & context compaction
│   ├── message/           # Message types & normalization
│   ├── mcp/               # Model Context Protocol client
│   ├── permissions/        # Tool permission evaluation
│   ├── prompt/            # System prompt assembly
│   ├── provider/          # Anthropic API provider (SSE streaming)
│   ├── query/             # Query loop orchestration
│   ├── session/           # Session state & persistence
│   └── tools/             # 33 built-in tools
├── internal/
│   ├── cli/               # Bubble Tea TUI renderer
│   └── testharness/       # Golden file test framework
├── testdata/              # Parity test fixtures
└── notes/                 # Architecture & dependency docs
```

---

## Porting Status

Full parity audit of 1,885 TypeScript source files against the Go port.
594 tasks identified across 24 subsystems. Every behavior, string, flag,
keybinding, and error message has been classified.

| Subsystem | Parity | Tasks | Notes |
|-----------|-------:|------:|-------|
| API & Streaming | 8% | 25 | Core SSE streaming works; billing, analytics, retry gaps |
| CLI & Headless Mode | 0% | 21 | Auth, `--print` mode, subcommands not started |
| Commands (60+ slash) | 1% | 89 | Descriptors registered, handlers mostly stubs |
| Compaction & Context | 22% | 10 | Auto-compact works; reactive/collapse pipelines missing |
| Configuration & Constants | 13% | 22 | Beta headers ~80% done; OAuth config, prompt builders gap |
| Context & Overlays | 0% | 10 | Notification queue, modal system, voice state |
| Hook System | 1% | 25 | Execution exists; 100+ React hooks need bubbletea equivalents |
| IDE & Desktop | 0% | — | Entirely new subsystem |
| Keybindings | 0% | 15 | 13 of ~100 bindings across 17 contexts |
| Memory & CLAUDE.md | 5% | 8 | Type enum exists; scanning, relevance, paths missing |
| MCP Protocol | 0% | — | Client exists; service layer + 18 util files absent |
| Migrations | 0% | 12 | Startup migration registry not started |
| Model & Provider | 57% | — | Best coverage area; edge cases + allowlists remain |
| Permissions | 13% | — | Rule engine works; UI, classifiers, auto-mode missing |
| Plugins | 0% | 10 | Entirely new subsystem |
| Remote / Bridge (CCR) | 0% | 32 | 31-file subsystem, 100% absent |
| Session & Storage | 18% | 61 | Core state exists; 195 of 215 fields missing |
| Terminal UI (Ink → Bubbletea) | 1% | 17 | Architecture replaced; behavioral parity gaps |
| Tools (33 b