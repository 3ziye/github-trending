```
██╗   ██╗ ██████╗ ██╗      ██████╗ ██████╗  ██████╗ ██╗  ██╗
╚██╗ ██╔╝██╔═══██╗██║     ██╔═══██╗██╔══██╗██╔═══██╗╚██╗██╔╝
 ╚████╔╝ ██║   ██║██║     ██║   ██║██████╔╝██║   ██║ ╚███╔╝
  ╚██╔╝  ██║   ██║██║     ██║   ██║██╔══██╗██║   ██║ ██╔██╗
   ██║   ╚██████╔╝███████╗╚██████╔╝██████╔╝╚██████╔╝██╔╝ ██╗
   ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
```

**Let your AI go full send. Your home directory stays home.**

Run [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex/), or any AI coding agent in "yolo mode" without nuking your home directory.

## The Problem

AI coding agents are incredibly powerful when you let them run commands without asking permission. But one misinterpreted prompt and `rm -rf ~` later, you're restoring from backup (yea right, as if you have backups lol).

## The Solution

`yolobox` runs your AI agent inside a container where:
- ✅ Your **project directory** is mounted at its real path (e.g., `/Users/you/project`)
- ✅ The agent has **full permissions** and **sudo** inside the container
- ✅ Your **home directory is NOT mounted** (unless you explicitly opt in)
- ✅ Persistent volumes keep tools and configs across sessions
- ✅ **Session continuity** - AI sessions can be resumed across host/container boundary

The AI can go absolutely wild inside the sandbox. Your actual home directory? Untouchable.

## Quick Start

```bash
# Install via Homebrew (macOS/Linux)
brew install finbarr/tap/yolobox

# Or install via script (requires Go)
curl -fsSL https://raw.githubusercontent.com/finbarr/yolobox/master/install.sh | bash
```

Then from any project:

```bash
cd /path/to/your/project
yolobox claude    # Let it rip
```

Or use any other AI tool: `yolobox codex`, `yolobox gemini`, `yolobox copilot`.

## Runtime Support

- **macOS**: Docker Desktop, OrbStack, Colima, or [Apple container](https://github.com/apple/container) (macOS Tahoe+)
- **Linux**: Docker or Podman

yolobox auto-detects available runtimes. To use a specific runtime:
```bash
yolobox claude --runtime container   # Apple container
yolobox claude --runtime docker      # Docker
yolobox claude --runtime podman      # Podman
```

> **Memory:** Claude Code needs **4GB+ RAM** allocated to Docker. Colima defaults to 2GB which will cause OOM kills. Increase with: `colima stop && colima start --memory 8`

## Commands

```bash
# AI tool shortcuts (recommended)
yolobox claude              # Run Claude Code
yolobox codex               # Run OpenAI Codex
yolobox gemini              # Run Gemini CLI
yolobox opencode            # Run OpenCode
yolobox copilot             # Run GitHub Copilot

# General commands
yolobox                     # Drop into interactive shell (for manual use)
yolobox run <cmd...>        # Run any command in sandbox
yolobox setup               # Configure yolobox settings
yolobox upgrade             # Update binary and pull latest image
yolobox config              # Show resolved configuration
yolobox reset --force       # Delete volumes (fresh start)
yolobox version             # Show version
yolobox help                # Show help
```

## Flags

> **Note:** Flags go **after** the subcommand: `yolobox run --flag cmd` or `yolobox claude --flag`, not `yolobox --flag run cmd`.

| Flag | Description |
|------|-------------|
| `--runtime <name>` | Use `docker`, `podman`, or `container` (Apple) |
| `--image <name>` | Custom base image |
| `--mount <src:dst>` | Extra mount (repeatable) |
| `--env <KEY=val>` | Set environment variable (repeatable) |
| `--setup` | Run interactive setup before starting |
| `--ssh-agent` | Forward SSH agent socket |
| `--no-network` | Disable network access |
| `--network <name>` | Join specific network (e.g., docker compose) |
| `--no-yolo` | Disable auto-confirmations (mindful mode) |
| `--readonly-project` | Mount project read-only (outputs go to `/output`) |
| `--claude-config` | Copy host `~/.claude` config into container |
| `--git-config` | Copy host `~/.gitconfig` into container |
| `--gh-token` | Forward GitHub CLI token (extracts from keychain via `gh auth token`) |
| `--copy-agent-instructions` | Copy global agent instruction files (see below) |

> **Networking:** By default, yolobox uses Docker's bridge network (internet access, no container DNS). Use `--network <name>` to join a docker compose network and access services by name. Use `--no-network` for complete isolation.

## Configuration

Run `yolobox setup` to configure your preferences with an interactive wizard.

Settings are saved to `~/.config/yolobox/config.toml`:

```toml
git_config = true
gh_token = true
ssh_agent = true
no_network = true
network = "my_compose_network"
no_yolo = true
```

You can also create `.yolobox.toml` in your project for project-specific settings:

```toml
mounts = ["../shared-libs:/libs:ro"]
env = ["DEBUG=1"]
no_network = true
```

Priority: CLI flags > project config > global config > defaults.

> **Note:** Setting `claude_config = true` in your config will copy your h