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
- ✅ Your **project directory** is mounted at `/workspace`
- ✅ The agent has **full permissions** and **sudo** inside the container
- ✅ Your **home directory is NOT mounted** (unless you explicitly opt in)
- ✅ Persistent volumes keep tools and configs across sessions

The AI can go absolutely wild inside the sandbox. Your actual home directory? Untouchable.

## Quick Start

```bash
# Install (requires Go)
curl -fsSL https://raw.githubusercontent.com/finbarr/yolobox/master/install.sh | bash

# Or clone and build
git clone https://github.com/finbarr/yolobox.git
cd yolobox
make install
```

Then from any project:

```bash
cd /path/to/your/project
yolobox claude    # Let it rip
```

Or use any other AI tool: `yolobox codex`, `yolobox gemini`, `yolobox copilot`.

## Runtime Support

- **macOS**: Docker Desktop, OrbStack, or Colima
- **Linux**: Docker or Podman

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

| Flag | Description |
|------|-------------|
| `--runtime <name>` | Use `docker` or `podman` |
| `--image <name>` | Custom base image |
| `--mount <src:dst>` | Extra mount (repeatable) |
| `--env <KEY=val>` | Set environment variable (repeatable) |
| `--setup` | Run interactive setup before starting |
| `--ssh-agent` | Forward SSH agent socket |
| `--no-network` | Disable network access |
| `--no-yolo` | Disable auto-confirmations (mindful mode) |
| `--readonly-project` | Mount project read-only (outputs go to `/output`) |
| `--claude-config` | Copy host `~/.claude` config into container |
| `--git-config` | Copy host `~/.gitconfig` into container |

## Configuration

Run `yolobox setup` to configure your preferences with an interactive wizard.

Settings are saved to `~/.config/yolobox/config.toml`:

```toml
git_config = true
ssh_agent = true
no_network = true
no_yolo = true
```

You can also create `.yolobox.toml` in your project for project-specific settings:

```toml
mounts = ["../shared-libs:/libs:ro"]
env = ["DEBUG=1"]
no_network = true
```

Priority: CLI flags > project config > global config > defaults.

> **Note:** Setting `claude_config = true` in your config will copy your host Claude config on **every** container start, overwriting any changes made inside the container (including auth and history). Prefer using `--claude-config` for one-time syncs.

### Auto-Forwarded Environment Variables

These are automatically passed into the container if set:
- `ANTHROPIC_API_KEY`
- `OPENAI_API_KEY`
- `COPILOT_GITHUB_TOKEN` / `GH_TOKEN` / `GITHUB_TOKEN`
- `OPENROUTER_API_KEY`
- `GEMINI_API_KEY`

## What's in the Box?

The base image comes batteries-included:
- **AI CLIs**: Claude Code, Gemini CLI, OpenAI Codex, OpenCode, Copilot (all pre-configured for full-auto mode!)
- **Runtimes**: Node.js 22, Python 3, Go, Bun
- **Build tools**: make, cmake, gcc
- **Git** + **GitHub CLI**
- **Common utilities**: ripgrep, fd, fzf, jq, vim

Need something else? The AI has sudo.

### AI CLIs Run in YOLO Mode

Inside yolobox, the AI CLIs are aliased to skip all permission prompts:

| Command | Expands to |
|---------|------------|
| `claude` | `claude --dangerously-skip-permissions` |
| `codex` | `codex --dangerously-bypass-approvals-and-sandbox` |
| `gemini` 