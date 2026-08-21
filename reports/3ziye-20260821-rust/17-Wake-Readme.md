# Wake

[![License](https://img.shields.io/github/license/iAmCorey/Wake?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/iAmCorey/Wake?style=flat-square)](https://github.com/iAmCorey/Wake/releases/latest)
[![Platform](https://img.shields.io/badge/platform-macOS%2014%2B-007AFF?style=flat-square)](https://github.com/iAmCorey/Wake/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/iAmCorey/Wake/total?style=flat-square)](https://github.com/iAmCorey/Wake/releases)
[![Stars](https://img.shields.io/github/stars/iAmCorey/Wake?style=flat-square)](https://github.com/iAmCorey/Wake/stargazers)
[![CI](https://img.shields.io/github/actions/workflow/status/iAmCorey/Wake/ci.yml?branch=main&label=CI&style=flat-square)](https://github.com/iAmCorey/Wake/actions/workflows/ci.yml)

A native macOS app that gathers every coding-agent session on your machine into one place — browse, full-text search, and resume any conversation in seconds. Built with **Rust + GPUI** (gpui 0.2 + gpui-component 0.5).

Your agent history is scattered across `~/.claude`, `~/.codex`, and nine other private directories. Wake reads them all, read-only, and gives you one fast window into it. Everything stays local: no network requests, ever.

![Wake — sessions list and transcript view](imgs/screenshot-1.webp)

## Features

- **Unified browsing** — all sessions grouped by agent / project, live file watching for incremental updates
- **Full-text search** (⌘K) — SQLite FTS5 trigram index; handles CJK text and code substrings (like `useEffect(`) equally well; jumps straight to the matched message in the transcript
- **Transcript view** — per-message rendering with user/assistant bubbles, collapsible tool-call clusters, thinking summaries, tree-sitter code highlighting (30+ languages)
- **One-click resume** — reopens the session in Terminal/iTerm at the original project directory (`claude --resume`, `codex resume`, …)
- **Manage** — star/pin (stored in Wake's own DB, original files untouched), export to Markdown, delete (system Trash + tombstone so deleted sessions stay deleted)

![Full-text search across every agent's sessions](imgs/screenshot-2.webp)

## Supported agents

| Agent | Data source | Model | Via |
|---|---|---|---|
| Claude Code | `~/.claude/projects/**/*.jsonl` | ✅ | — |
| Codex CLI | `~/.codex/sessions` + `state_5.sqlite` (read-only) | ✅ | ✅ |
| Copilot CLI | `~/.copilot/session-store.db` | — | — |
| Cursor (CLI transcripts) | `~/.cursor/projects/**/agent-transcripts` | — | — |
| OpenCode | `~/.local/share/opencode/opencode.db` | ✅ | — |
| OpenCode 2 (`opencode2`, beta) | same DB as v1, new `session_v2` tables | ✅ | — |
| Kiro | `~/.kiro/sessions/cli` | ✅ | — |
| Gemini CLI | `~/.gemini/tmp/**/chats` | — | — |
| Pi | `~/.pi/agent/sessions/**/*.jsonl` | ✅ | — |
| Oh My Pi | `~/.omp/agent/sessions/**/*.jsonl` | ✅ | — |
| Grok Build | `~/.grok/sessions/**/updates.jsonl` | ✅ | — |
| Kimi Code | `~/.kimi-code/sessions/**/wire.jsonl` | — | — |
| Antigravity CLI | `~/.gemini/antigravity-cli/conversation_summaries.db` (metadata only — transcripts are encrypted) | — | — |

**Model** = whether Wake shows which LLM a session used (the model the session last used). **Via** = whether Wake shows where the session was started from (CLI, IDE extension, desktop app) — only Codex records this in its local data. A "—" means the agent's local data simply doesn't record that field, not a missing feature.

Cursor IDE chats, Windsurf, and Trae encrypt their local data; Amp, Factory (Droid), and Warp keep sessions in the cloud — none of those are supported. Reasonix stores sessions locally but hasn't been mapped yet.

## Privacy stance

- Agent data directories are opened **read-only**; Wake never writes to another tool's files or databases
- Credential files (`auth.json` and friends) are never read
- Zero network requests — Wake never constructs or calls an HTTP client (GPUI's dependency tree bundles one; Wake doesn't reach for it)
- Wake's own index lives at `~/Library/Application Support/wake/wake.db` and can be rebuilt from scratch at any time (stars/pins live in a separate table and survive rebuilds)

## Performance

On the author's machine (~310 sessions, ~800 MB of JSONL): full index ~5 s, subsequent launches are instant (mtime-based incremental scan), search results in under 1 ms.

## Install

Build from source (requires a Rust toolchain):

```bash
git clone https://github.com/iAmCorey/Wake && cd Wake
scripts/make-app.sh          # builds dist/Wake.app (icon + Info.plist, ad-hoc signed)
open dist/Wake.app
```

The app is ad-hoc signed, so if you download a prebuilt copy instead of building it yourself, macOS Gatekeeper will block the first launch — right-click the app and choose *Open*, or run `xattr -d com.apple.quarantine Wake.app`.

## Development

```bash
cargo run -p wake                      # run in dev mode
scripts/test.sh                        # one-command test entry: data-layer tests + UI compile 