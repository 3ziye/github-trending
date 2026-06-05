![banner](https://github.com/gi-dellav/zerostack/blob/main/assets/banner.png?raw=true)

---

# zerostack
Minimal coding agent written in Rust, inspired by [pi](https://pi.dev/docs/latest/usage) and [opencode](https://opencode.ai/).

*blogposts:* [what we built in 2 weeks](https://rocketup.pages.dev/posts/what_we_built_in_2_weeks/) [memory design](https://rocketup.pages.dev/posts/how-zerostack-memory-works/) [subagents design](https://rocketup.pages.dev/posts/how-zerostack-subagents-work/)

<a href="https://www.producthunt.com/products/zerostack-coding-agent/reviews/new?utm_source=badge-product_review&utm_medium=badge&utm_source=badge-zerostack&#0045;coding&#0045;agent" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/product_review.svg?product_id=1236867&theme=light" alt="Zerostack&#0032;Coding&#0032;Agent - A&#0032;minimal&#0032;coding&#0032;agent&#0044;&#0032;with&#0032;a&#0032;bundle&#0032;of&#0032;innovative&#0032;features | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>

## Features

- **Multi-provider**: OpenRouter, OpenAI, Anthropic, Gemini, Ollama, plus custom providers
- **Standard tools**: all of the standard tools exposed to coding agents, as described by the opencode documentation.
- **Permission system**: five configurable modes with per-tool patterns, session allowlists, and configurable mode-to-rule application policies
- **Session management**: save/load/resume sessions, auto-compaction to stay within context windows
- **Terminal UI**: crossterm-based, markdown rendering, mouse selection/copy, scrollback, reasoning visibility toggle
- **Prompts system**: switch between system prompt modes at runtime (`code`, `plan`, `review`, `debug`, etc.) to tailor the agent's behavior to the task without having to manage Skills.
- **MCP support**: connect MCP servers for extended tooling (exposed as an optional compile-time feature)
- **Integrated Exa search**: allows for WebFetch and WebSearch tools
- **Integrated Ralph Wiggum loops**: looping capabilities for long-horizon tasks
- **Integrated Git Worktrees integration**: Use `/worktree` to move the agent from one worktree to another.
- **ACP support** (gated): Agent Communication Protocol server — lets editors (Zed, etc.) connect to zerostack as an ACP agent
- **Persistent memory** (gated): plain-Markdown memory across sessions: a global MEMORY.md plus per-project daily logs, scratchpad, and notes, injected into the system prompt each session
- **Subagents**: Parallel and fast, used for exploring the codebase
- **ARCHITECTURE.md**: Our own companion file for AGENTS.md, it allows to offer a shared core knowledge for all agents working on the same codebase

**NOTE**: Windows support is not tested is any way, but feel free to try and open an issue if you encounter any bugs!

## Performance

_zerostack_ is one of the smallest and most performant coding agents on the market.

- Lines of code: ~17k LoC
- Binary size: 26MB
- RAM footprint: ~16MB on average, with peaks at ~24MB (vs ~300MB with peaks at ~700MB for opencode or other JS-based coding agents)
- CPU usage: 0.0% on idle, ~1.5% when using tools (measured on an Intel i5 7th gen, vs ~2% on idle and ~20% when working for opencode)

## Installation

In order to install _zerostack_, you must have Cargo and git installed. Then, run:

```bash
# Default: MCP, loop, git-worktree and subagents
cargo install zerostack

# With ACP (Agent Communication Protocol) support for editor integration
cargo install zerostack --features acp

# With Memory support
cargo install zerostack --features memory

# With experimental multi-threaded subagents
cargo install zerostack --features multithread
```

You are now ready to work with a lightweight coding agent! (You can also find pre-built binaries on Github Releases)

Once installed, run `/prompt autoconfig` inside zerostack to explore the documentation and configure the tool interactively.

_note:_ If you have questions or you want to collaborate on the project, please join the [dedicated Matrix chatroom](https://app.element.io/#/room/#zerostack-general:matrix.org).

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

There is also support for zerobox as an alternative sandbox backend.

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

See [docs/CONFIG.md](docs/CONFIG.md) for c