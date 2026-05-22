# zerostack

Minimal coding agent written in Rust, inspired by [pi](https://pi.dev/docs/latest/usage) and [opencode](https://opencode.ai/).

## Features

- **Multi-provider**: OpenRouter, OpenAI, Anthropic, Gemini, Ollama, plus custom providers
- **Standard tools**: all of the standard tools exposed to coding agents, as described by the opencode documentation.
- **Permission system**: four configurable modes with per-tool patterns, session allowlists, and external directory policies
- **Session management**: save/load/resume sessions, auto-compaction to stay within context windows
- **Terminal UI**: crossterm-based, markdown rendering, mouse selection/copy, scrollback, reasoning visibility toggle
- **Prompts system**: switch between system prompt modes at runtime (`code`, `plan`, `review`, `debug`, etc.) to tailor the agent's behavior to the task without having to manage Skills.
- **MCP support**: connect MCP servers for extended tooling (exposed as an optional compile-time feature)
- **Integrated Exa search**: allows for WebFetch and WebSearch tools
- **Integrated Ralph Wiggum loops**: looping capabilities for long-horizon tasks
- **Integrated Git Worktrees integration**: Use `/worktree` to move the agent from one worktree to another.
- **ACP support** (gated): Agent Communication Protocol server — lets editors (Zed, etc.) connect to zerostack as an ACP agent

**NOTE**: Windows support is not tested is any way, but feel free to try and open an issue if you encounter any bugs!

## Performance

_zerostack_ is one of the smallest and most performant coding agents on the market.

- Lines of code: ~9k LoC
- Binary size: 8.9MB
- RAM footprint: ~10MB on an empty session, ~13MB when working (vs ~300MB for opencode or other JS-based coding agents)
- CPU usage: 0.0% on idle, ~1.5% when using tools (measured on an Intel i5 7th gen, vs ~2% on idle and ~20% when working for opencode)

## Installation

In order to install _zerostack_, you must have Cargo and git installed. Then, run:

```bash
# Default — MCP, loop, and git-worktree included
cargo install zerostack

# With ACP (Agent Communication Protocol) support for editor integration
cargo install zerostack --features acp
```

You are now ready to work with a lightweight coding agent! (Note: you can also find pre-built binaries on Github Releases)

### Optional: sandbox mode

Install [bubblewrap](https://github.com/containers/bubblewrap) for `--sandbox`,
which runs every bash command inside an isolated environment to protect your
system from accidental or malicious damage:

```bash
# Debian/Ubuntu
apt install bubblewrap

# Fedora
dnf install bubblewrap

# Arch
pacman -S bubblewrap
```

## Quick start

```bash
# Set your API key (OpenRouter is default)
export OPENROUTER_API_KEY="[api_key]"

# Interactive session (default prompt: code)
zerostack

# Monochrome TUI
zerostack --no-color

# One-shot mode
zerostack -p "Explain this project"

# Continue last session
zerostack -c

# Explicit provider/model
zerostack --provider openrouter --model deepseek/deepseek-v4-flash
```

## Configuration

See [CONFIG.md](CONFIG.md) for config file location, accepted keys, provider
aliases, permission rules, and MCP server configuration.

## Prompts system

_zerostack_ includes a set of built-in system prompts that change the agent's behavior and tone.  
The idea is to build a complete suite of prompts that can fully substitute skills like [superpower](https://github.com/obra/superpowers) or the [Claude's official skills](https://github.com/anthropics/claude-plugins-official/tree/main).  
You can switch between different prompts or list all registered prompts using `/prompt`.

Built-in prompts:

| Prompt                | Description                                                              |
| --------------------- | ------------------------------------------------------------------------ |
| **`code`** (default)  | Coding mode with full file and bash tool access, TDD workflow            |
| **`plan`**            | Planning-only mode — explores and produces a plan without writing code   |
| **`review`**          | Code review mode — reviews for correctness, design, testing, and impact  |
| **`debug`**           | Debug mode — finds root cause before proposing fixes                     |
| **`ask`**             | Read-only mode — only read/grep/glob permitted, no writes or bash        |
| **`brainstorm`**      | Design-only mode — explores ideas and presents designs without code      |
| **`frontend-design`** | Frontend design mode — distinctive, production-grade UI                  |
| **`review-security`** | Security review mode — finds exploitable vulnerabilities                 |
| **`simplify`**        | Code simplification mode — refines for clarity without changing behavior |
| **`write-prompt`**    | Prompt writing mode — creates and optimizes agent prompts                |

You can also create custom prompts by placing markdown files in
`$XDG_CONFIG_HOME/zerostack/prompts/` an