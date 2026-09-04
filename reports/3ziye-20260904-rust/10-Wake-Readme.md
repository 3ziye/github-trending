# Wake

[![License](https://img.shields.io/github/license/iAmCorey/Wake?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/iAmCorey/Wake?style=flat-square)](https://github.com/iAmCorey/Wake/releases/latest)
[![Platform](https://img.shields.io/badge/platform-macOS%2014%2B%20%7C%20Linux%20beta%20%7C%20Windows%20beta-007AFF?style=flat-square)](https://github.com/iAmCorey/Wake/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/iAmCorey/Wake/total?style=flat-square)](https://github.com/iAmCorey/Wake/releases)
[![Stars](https://img.shields.io/github/stars/iAmCorey/Wake?style=flat-square)](https://github.com/iAmCorey/Wake/stargazers)
[![CI](https://img.shields.io/github/actions/workflow/status/iAmCorey/Wake/ci.yml?branch=main&label=CI&style=flat-square)](https://github.com/iAmCorey/Wake/actions/workflows/ci.yml)

A native desktop app that gathers every coding-agent session on your machine into one place — browse, full-text search, and resume any conversation in seconds. Built with **Rust + GPUI** (gpui 0.2 + gpui-component 0.5). macOS first; experimental Linux support since v0.2.5, experimental Windows support since v0.2.7.

Your agent history is scattered across `~/.claude`, `~/.codex`, and a dozen other private directories. Wake reads them all, read-only, and gives you one fast window into it. Everything stays local; Wake only contacts GitHub when you explicitly check for an update.

![Wake — sessions list and transcript view](imgs/screenshot-1.webp)

## Features

- **Unified browsing** — all sessions grouped by agent / project, with Grok Build subagents nested under their parent and live file watching for incremental updates
- **Full-text search** (⌘K / Ctrl+K) — SQLite FTS5 trigram index; handles CJK text and code substrings (like `useEffect(`) equally well; jumps straight to the matched message in the transcript
- **Transcript view** — per-message rendering with user/assistant bubbles, inline images (copy or save them), collapsible tool-call clusters, thinking summaries, tree-sitter code highlighting (30+ languages)
- **One-click resume** — reopens the session in your terminal (Terminal/iTerm on macOS; native terminal hosts on Linux and Windows) at the original project directory (`claude --resume`, `codex resume`, …)
- **Manage** — star/pin (stored in Wake's own DB, original files untouched), export to Markdown or save an inline image through the system Save dialog (Wake remembers the last folder), delete (system Trash + tombstone so deleted sessions stay deleted)
- **Insights** — a stats page for your whole library: GitHub-style activity heatmap with streaks, hour / weekday / month breakdowns, and Agents / Projects / Models leaderboards switchable between sessions, tokens, and prompts
- **Remote hosts** — mirror the sessions on your other machines over SSH (Settings → Remote hosts); they show up next to local ones with an `@host` badge, searchable like everything else, and resume through a copied `ssh -t` command

![Full-text search across every agent's sessions](imgs/screenshot-2.webp)

## Supported agents

| Agent | Data source | Model | Via |
|---|---|---|---|
| Claude Code | `~/.claude/projects/**/*.jsonl` | ✅ | — |
| Codex CLI | `~/.codex/sessions` + `state_5.sqlite` (read-only) | ✅ | ✅ |
| Qoder CLI | `~/.qoder/projects/*/*.jsonl` (`QODER_CONFIG_DIR` is respected) | ✅ | — |
| Copilot CLI | `~/.copilot/session-store.db` | — | — |
| Cursor (CLI transcripts) | `~/.cursor/projects/**/agent-transcripts` | — | — |
| OpenCode | `~/.local/share/opencode/opencode.db` | ✅ | — |
| OpenCode 2 (`opencode2`) | `~/.local/share/opencode/{opencode.db,opencode-next.db}` (`session_v2` or `session` + `session_message`); both paths are scanned | ✅ | — |
| Kiro | `~/.kiro/sessions/cli` | ✅ | — |
| Gemini CLI | `~/.gemini/tmp/**/chats` | — | — |
| Pi | `~/.pi/agent/sessions/**/*.jsonl` | ✅ | — |
| Oh My Pi | `~/.omp/agent/sessions/**/*.jsonl` | ✅ | — |
| Grok Build | `~/.grok/sessions/**/updates.jsonl` | ✅ | — |
| Kimi Code | `~/.kimi-code/sessions/**/wire.jsonl` | — | — |
| Antigravity CLI | `~/.gemini/antigravity-cli/conversation_summaries.db` (metadata only — transcripts are encrypted) | — | — |
| DeepSeek Harness (`dsh`) | `~/.dsh/sessions/**/session.jsonl[.zstd]` (zstd-compressed logs are decoded transparently) | ✅ | — |
| Hermes Agent | `~/.hermes/state.db` + `profiles/*/state.db` (`HERMES_HOME` is respected) | ✅ | ✅ |
| OpenClaw | `~/.openclaw/agents/*/agent/openclaw-agent.sqlite` + legacy `agents/*/sessions/*.jsonl` (`OPENCLAW_STATE_DIR` is respected) | ✅ | ✅ |

**Model** = whether Wake shows which LLM a session used (the model the session last used). **Via** = whether Wake shows where the session was started from (CLI, IDE extension, desktop app) — Codex records this in its local data; Hermes and OpenClaw record the channel a session came in through (Telegram, Discord, …). A "—" means the agent's local data simply doesn't record that field, not a missing feature.

Cu