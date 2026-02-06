# dcg (Destructive Command Guard)

<div align="center">
  <img src="illustration.webp" alt="Destructive Command Guard - Protecting your code from accidental destruction">
</div>

<div align="center">

[![CI](https://github.com/Dicklesworthstone/destructive_command_guard/actions/workflows/ci.yml/badge.svg)](https://github.com/Dicklesworthstone/destructive_command_guard/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/codecov/c/github/Dicklesworthstone/destructive_command_guard?label=coverage)](https://codecov.io/gh/Dicklesworthstone/destructive_command_guard)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

A high-performance hook for AI coding agents that blocks destructive commands before they execute, protecting your work from accidental deletion.

**Supported:** [Claude Code](https://claude.ai/code), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [OpenCode](https://opencode.ai) (via [community plugin](https://github.com/jms830/opencode-dcg-plugin)), [Aider](https://aider.chat/) (limited—git hooks only), [Continue](https://continue.dev) (detection only), [Codex CLI](https://github.com/openai/codex) (detection only)

<div align="center">
<h3>Quick Install</h3>

```bash
curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/destructive_command_guard/master/install.sh?$(date +%s)" | bash -s -- --easy-mode
```

<p><em>Works on Linux, macOS, and Windows (WSL). Auto-detects your platform and downloads the right binary.</em></p>
</div>

---

## TL;DR

**The Problem**: AI coding agents (Claude, GPT, etc.) occasionally run catastrophic commands like `git reset --hard`, `rm -rf ./src`, or `DROP TABLE users`—destroying hours of uncommitted work in seconds.

**The Solution**: dcg is a high-performance hook that intercepts destructive commands *before* they execute, blocking them with clear explanations and safer alternatives.

### Why Use dcg?

| Feature | What It Does |
|---------|--------------|
| **Zero-Config Protection** | Blocks dangerous git/filesystem commands out of the box |
| **49+ Security Packs** | Databases, Kubernetes, Docker, AWS/GCP/Azure, Terraform, and more |
| **Sub-Millisecond Latency** | SIMD-accelerated filtering—you won't notice it's there |
| **Heredoc/Inline Script Scanning** | Catches `python -c "os.remove(...)"` and embedded shell scripts |
| **Smart Context Detection** | Won't block `grep "rm -rf"` (data) but will block `rm -rf /` (execution) |
| **Scan Mode for CI** | Pre-commit hooks and CI integration to catch dangerous commands in code review |
| **Fail-Open Design** | Never blocks your workflow due to timeouts or parse errors |
| **Explain Mode** | `dcg explain "command"` shows exactly why something is blocked |

### Quick Example

```bash
# AI agent tries to run:
$ git reset --hard HEAD~5

# dcg intercepts and blocks:
════════════════════════════════════════════════════════════════
BLOCKED  dcg
────────────────────────────────────────────────────────────────
Reason:  git reset --hard destroys uncommitted changes

Command: git reset --hard HEAD~5

Tip: Consider using 'git stash' first to save your changes.
════════════════════════════════════════════════════════════════
```

### Enable More Protection

```toml
# ~/.config/dcg/config.toml
[packs]
enabled = [
    "database.postgresql",    # Blocks DROP TABLE, TRUNCATE
    "kubernetes.kubectl",     # Blocks kubectl delete namespace
    "cloud.aws",              # Blocks aws ec2 terminate-instances
    "containers.docker",      # Blocks docker system prune
]
```

### Agent-Specific Profiles

dcg automatically detects which AI coding agent is invoking it and can apply
agent-specific trust levels:

```toml
# Trust Claude Code more
[agents.claude-code]
trust_level = "high"
additional_allowlist = ["npm run build"]

# Restrict unknown agents
[agents.unknown]
trust_level = "low"
extra_packs = ["paranoid"]
```

See [docs/agents.md](docs/agents.md) for full documentation on supported agents
and configuration options.

---

## Origins & Authors

This project began as a Python script by Jeffrey Emanuel, who recognized that AI coding agents, while incredibly useful, occasionally run catastrophic commands that destroy hours of uncommitted work. The original implementation was a simple but effective hook that intercepted dangerous git and filesystem commands before execution.

- **[Jeffrey Emanuel](https://github.com/Dicklesworthstone)** - Original concept and Python implementation ([source](https://github.com/Dicklesworthstone/misc_coding_agent_tips_and_scripts/blob/main/DESTRUCTIVE_GIT_COMMAND_CLAUDE_HOOKS_SETUP.md)); substantially expanded the Rust version with the modular pack system (49+ security packs), heredoc/inline-script scanning, the three-tier architecture, context classification, allowlists, scan mode, and the dual regex engine
- **[Darin Gordon](https://github.com/Dowwie)** - Initial Rust port with performance optimizations

The initial