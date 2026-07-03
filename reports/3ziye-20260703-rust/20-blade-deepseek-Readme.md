# Orca

Orca is a DeepSeek-native coding agent.

A local terminal coding agent built in Rust, focused on DeepSeek reasoning and tool-use semantics. It runs a multi-turn agent loop with SSE streaming, automatic context window management, and HTTP retry with exponential backoff.

## Installation

### npm

```bash
npm install -g @blade-ai/orca
orca --version
```

The npm package installs a small Node.js launcher and the native `orca` binary for supported platforms.

Supported npm platforms:

- macOS Apple Silicon (`darwin/arm64`)
- macOS Intel (`darwin/x64`)
- Linux x64 (`linux/x64`)
- Linux ARM64 (`linux/arm64`)

### curl

```bash
curl -fsSL https://orcaagent.dev/install.sh | sh
```

The installer downloads the native binary for your platform from GitHub Releases.
Set `INSTALL_DIR` to choose a destination and `ORCA_VERSION` to pin a version:

```bash
curl -fsSL https://orcaagent.dev/install.sh | \
  INSTALL_DIR=/usr/local/bin ORCA_VERSION=0.1.106 sh
```

### GitHub Releases

Download the archive for your platform from the latest GitHub Release, extract it, and place `orca` on your `PATH`.

## Community

- QQ group: `472309526`
- Telegram: https://t.me/+11No1w5ZbTMyZTQ1

## Quick Start

```sh
# Set your API key
export DEEPSEEK_API_KEY=sk-...

# Run a task
orca exec "fix this test"

# With options
orca exec --approval-mode full-auto "refactor the auth module"
orca exec --model deepseek-v4-pro "explain this codebase"
orca exec --verifier "cargo test" "fix the failing test"
```

## Configuration

Priority chain (highest wins): Environment variables > CLI arguments > Config file > Defaults.

### Environment Variables

- `DEEPSEEK_API_KEY` — API key (required)
- `DEEPSEEK_MODEL` — Model override
- `DEEPSEEK_BASE_URL` — API base URL override
- `DEEPSEEK_REASONING_EFFORT` — Reasoning effort override (`high` or `max`; default `max`)
- `ORCA_NODE_PATH` — Node.js executable used by workflow scripts when `node` is not on `PATH` (npm installs set this automatically)

### Config File

`~/.orca/config.toml`:

```toml
model = "auto"
reasoning_effort = "max"
api_key = "sk-..."
base_url = "https://api.deepseek.com"
```

### Updates

When `update_check` is enabled, Orca checks for a newer release before opening the interactive TUI. If a newer release is available, Orca shows a startup prompt with `Update now`, `Skip`, and `Skip until next version`. Choosing `Update now` updates the currently running install: npm-managed launches run the npm upgrade command, while direct binary launches rerun the curl installer into the current executable's directory. Choosing either skip option continues into the TUI.

If you installed with curl and later switch to npm, make sure the npm global bin directory appears before `~/.local/bin` on `PATH`, or remove the older curl-installed `~/.local/bin/orca`. Otherwise your shell may keep running the curl-installed binary.

Disable the startup check with:

```toml
update_check = false
```

Hooks may return structured JSON on stdout. `{"action":"deny","reason":"..."}` blocks, `{"action":"modify","modified_target":"..."}` rewrites a tool target, and `{"action":"inject","context":"..."}` adds model context. When JSON declares an `action`, Orca validates the action and required string fields so typoed or malformed structured outputs fail visibly. Plain non-JSON stdout and JSON without `action` are treated as injected context for compatibility. Supported events are `session_start`, `session_end`, `pre_tool_use`, `post_tool_use`, `pre_model_call`, `post_model_call`, `on_budget_warning`, `pre_compact`, and `post_compact`.

Custom tools can be added with TOML descriptors under `~/.orca/tools/`:

```toml
name = "deploy"
description = "Deploy the current branch"
action_kind = "write"
command = "./scripts/deploy.sh"
schema = { target = { type = "string", description = "environment" } }
```

External tool commands run from the workspace directory. The raw JSON arguments are provided on stdin and in `ORCA_TOOL_ARGS`.

Tool output truncation can be configured under `[tools]`. Byte mode preserves the historical 8 KiB default; token mode adds an explicit warning with original token and line counts before compacting large outputs:

```toml
[tools]
output_truncation = { mode = "tokens", limit = 2000 }
```

### Defaults

- Model: `auto` (main loop uses `deepseek-v4-pro`, auxiliary tasks use `deepseek-v4-flash`)
- Reasoning effort: `max`
- Base URL: `https://api.deepseek.com`
- Approval mode: `suggest`
- Output format: `text`
- Max turns: 128

## Command

```sh
orca exec [options] <prompt>
orca --mode=server
```

For headless harnesses, `orca exec` also accepts prompt input from stdin:

```sh
printf 'fix the failing test\n' | orca exec --output-format jsonl
printf 'review this diff\n' | orca exec --output-format jsonl -
printf 'compiler output\n' | orca exec --output-format jsonl 'summarize this failure'
```

When no prompt argument is provided, stdin becomes the prompt. A lone `-` also
forces reading the prompt from st