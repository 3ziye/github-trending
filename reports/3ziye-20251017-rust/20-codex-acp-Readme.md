# Codex ACP Agent

[![MSRV](https://img.shields.io/badge/MSRV-1.90%2B-blue.svg)](rust-toolchain.toml)
[![Edition](https://img.shields.io/badge/Edition-2024-blueviolet.svg)](https://doc.rust-lang.org/edition-guide/rust-2024/index.html)

> Most of this repository code is implemented and reviewed by `codex` agents.

An Agent Client Protocol (ACP)–compatible agent that bridges the OpenAI Codex runtime with ACP clients over stdio. This project is under active development — features are evolving and breaking changes are likely.

## Highlights

- Agent Client Protocol (ACP) over stdio using `agent-client-protocol`.
- Integrates with the Codex Rust workspace for conversation management and event streaming.
- Slash commands with ACP AvailableCommands updates (advertised to clients on session start).
- Status output tailored for IDEs (workspace, account, model, token usage).
- Supports ACP session modes: `read-only`, `auto` (default), and `full-access`.
- Automatically launches an internal MCP filesystem server (`acp_fs`) so Codex reads/writes files through ACP tooling instead of shell commands.

## Requirements

- Rust (Rust 2024 edition; rustc 1.90+ as pinned in `rust-toolchain.toml`).
- Network access for building Git dependencies (Codex workspace, ACP crate).

## Build

```bash
make build
```

## Run

The agent communicates over stdin/stdout using ACP JSON-RPC. Launch it and connect from an ACP client (e.g., an IDE integration or a CLI client implementing ACP):

```bash
# With tracing logs
RUST_LOG=info cargo run --quiet
```

Because this agent speaks on stdio, it is intended to be spawned by your client. For manual testing, you can pipe ACP JSON-RPC messages to stdin and read replies from stdout.

> Tip: use `make release` (or `cargo build --release`) when shipping the binary to an IDE like Zed. The release build lives at `target/release/codex-acp`.

Example JSON-RPC (initialize → new session → /status):

```
{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"v1","clientName":"cli","capabilities":{}}}
{"jsonrpc":"2.0","id":2,"method":"session/new","params":{"cwd":"/absolute/path","mcpServers":[]}}
{"jsonrpc":"2.0","id":3,"method":"session/prompt","params":{"sessionId":"1","prompt":[{"type":"text","text":"/status"}]}}
```

## Usage (ACP over stdio)

Minimal smoke test from a shell piping JSON-RPC over stdio:

```bash
printf '%s\n' \
  '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"v1","clientName":"cli","capabilities":{}}}' \
  '{"jsonrpc":"2.0","id":2,"method":"session/new","params":{"cwd":"'"$PWD"'","mcpServers":[]}}' \
  '{"jsonrpc":"2.0","id":3,"method":"session/prompt","params":{"sessionId":"1","prompt":[{"type":"text","text":"/status"}]}}' \
| RUST_LOG=info cargo run --quiet
```

Or use the included script and Makefile target:

```bash
chmod +x scripts/stdio-smoke.sh
make smoke
```

### Configuration in [Zed](https://zed.dev)

> Add this configuration to zed settings.
```json
"agent_servers": {
  "Codex": {
    "command": "codex-acp",
    "args": [],
    "env": {
      "RUST_LOG": "info"
    }
  }
}
```

The agent automatically boots an MCP filesystem bridge. No extra configuration (or AGENTS.md edits) are required—Codex will discover the `acp_fs` server on every session.

## Filesystem tooling

When a session starts, `codex-acp` spins up an in-process TCP bridge and registers an MCP server named `acp_fs`. Codex then calls two structured tools:

- `read_text_file` — reads workspace files via ACP `client.read_text_file`, falling back to local disk if the client lacks FS support.
- `write_text_file` — writes workspace files via ACP `client.write_text_file`, with a local fallback.

`codex-acp` also injects a default instruction reminding the model to use these tools rather than shelling out with `cat`/`tee`. If your client exposes filesystem capabilities, file access stays within ACP.

## Plan Updates

When Codex emits plan updates (step lists with statuses), the agent translates them into ACP `SessionUpdate::Plan` events. Clients receive structured plan entries with status mapping:

- Pending → `pending`
- InProgress → `in_progress`
- Completed → `completed`

The agent preserves ordering and includes any optional explanation text. This allows IDEs to render a live task checklist during long-running operations.

## Features

- ACP Agent implementation
  - Handles `initialize`, `authenticate` (API key), `session/new`, `session/prompt`, `session/cancel`.
  - Streams Codex events (assistant text and deltas, reasoning deltas, token counts) as `session/update` notifications.

- Slash commands (advertised via `AvailableCommandsUpdate`)
  - Implemented today:
    - `/new` — Start a new chat during a conversation.
    - `/init` — Create an `AGENTS.md` with repository contributor guidance. Uses a bundled prompt (`src/agent/prompt_init_command.md`).
    - `/model` — Show or set the current model (uses `Op::OverrideTurnContext`).
    - `/approvals` — Set approval mode 