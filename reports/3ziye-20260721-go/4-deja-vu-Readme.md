<p align="center"><img src="assets/logo.svg" width="340" alt="deja-vu"></p>

<p align="center"><strong>Your agents already solved this. deja finds it.</strong><br>Memory tools start empty and record forward. deja starts full: it indexes the sessions your coding agents already wrote to disk &mdash; months of history from before you installed it &mdash; searches 3.3&nbsp;GB in ~12&nbsp;ms, serves it back to any agent over MCP, and moves with you between machines over SSH. One zero-dependency binary, fully local.</p>

<p align="center"><a href="https://vshulcz.github.io/deja-vu/">vshulcz.github.io/deja-vu</a></p>

<p align="center">
  <a href="https://github.com/vshulcz/deja-vu/actions/workflows/ci.yml"><img src="https://github.com/vshulcz/deja-vu/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/vshulcz/deja-vu/releases"><img src="https://img.shields.io/github/v/release/vshulcz/deja-vu" alt="Release"></a>
  <a href="https://www.npmjs.com/package/@vshulcz/deja-vu"><img src="https://img.shields.io/npm/v/%40vshulcz%2Fdeja-vu?label=npm" alt="npm"></a>
  <a href="https://scorecard.dev/viewer/?uri=github.com/vshulcz/deja-vu"><img src="https://api.scorecard.dev/projects/github.com/vshulcz/deja-vu/badge" alt="OpenSSF Scorecard"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
</p>

<p align="center"><img src="assets/demo.gif" alt="deja demo"></p>

Claude Code, Codex, opencode, aider, Gemini CLI, Cursor, Antigravity, Grok Build, Qwen Code, pi and Copilot CLI write every conversation to local files — gigabytes of debugged problems and design decisions you can't search. deja is a zero-dependency binary that turns those histories into a memory layer:

| Feature | What it does |
| --- | --- |
| **Search** | `deja "connection pool exhausted"` — ~12 ms over gigabytes, retroactive: months of logs from before you installed it |
| **Agent recall** | MCP `recall` tool — the agent answers *"we fixed this three weeks ago"* instead of re-debugging, across harnesses: solve it in Codex, Claude remembers |
| **Sync** | `deja sync ssh laptop` — your memory follows you between machines, append-only, idempotent, no cloud in the middle |
| **Handoff** | `deja handoff --to codex` — stuck in one agent? package the live context and continue in another: `codex "$(deja handoff --to codex)"` |
| **Auto-recall** | `install --auto` adds a SessionStart hook: relevant memory lands in context before you ask; Claude Code also captures the current transcript before compaction |
| **Redaction** | API keys, JWTs, private keys are stripped at index time — the cache is safe to keep |
| **Stats** | `deja stats` — your agent work, wrapped: harnesses, top projects, activity sparkline |
| **Share** | `deja share <id>` — hand a colleague a sanitized digest of a session, secrets already scrubbed |
| **Remember** | `deja remember "text"` or MCP `remember` — keep durable decisions and conclusions |
| **Blame** | `deja blame <path>` — which sessions touched this file, what was decided and why |
| **Semantic** | optional: point `deja embed` at a local Ollama/LM Studio and rephrased queries still hit |

## Privacy

`deja forget` removes matching sessions from a rebuilt index and records exact
session tombstones so a later `deja index` cannot restore them from source
history. Tombstones are stored at `~/.config/deja/tombstones` (or
`$XDG_CONFIG_HOME/deja/tombstones`); use `--dry-run`, `--list`, or `--unforget`.
Ingest exclusions are one case-insensitive project pattern per line in
`~/.config/deja/exclude` (XDG-aware), or comma-separated in
`DEJA_EXCLUDE_PROJECTS`. `deja stats --redaction` reports redactions by
harness and rule, along with tombstone and semantic-sidecar facts.

One binary. No models to download, no services to run, nothing leaves your machine unless you sync or share it. (opencode and Cursor IDE indexing shell out to the `sqlite3` CLI, preinstalled on macOS and most Linux distros; Cursor CLI transcripts do not need it.)

## Install

```sh
curl -fsSL https://raw.githubusercontent.com/vshulcz/deja-vu/main/install.sh | sh
```

or:

```sh
go install github.com/vshulcz/deja-vu/cmd/deja@latest   # Go
npx @vshulcz/deja-vu "query"                            # npm, no install
brew install vshulcz/tap/deja-vu                        # Homebrew
```

### Shell completion

```sh
deja completion bash >> ~/.bashrc
deja completion zsh >> ~/.zshrc
deja completion fish > ~/.config/fish/completions/deja.fish
```

Wire it into the agents you use (edits config, keeps a `.bak`):

```sh
deja install --all     # MCP recall for every agent it finds on this machine
deja install --auto    # same, plus session-start auto-recall where supported
```

On Windows, register the MCP server through the shell wrapper most stdio servers need there: `cmd /c deja mcp` (deja install writes this form automatically; use it if you wire configs by hand).

Install also writes user-level guidance for the har