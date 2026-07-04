<h1 align="center">MiMoCode</h1>

<p align="center">
  <img src="assets/readme/mimocode-banner.png" alt="MiMoCode" width="700">
</p>

<p align="center"><strong>MiMo Code: Where Models and Agents Co-Evolve</strong></p>

<p align="center">
  <a href="README.zh.md">中文</a> | English
</p>

<p align="center">
  <a href="https://mimo.xiaomi.com/coder">Website</a> | <a href="https://mimo.xiaomi.com/en/blog/mimo-code-long-horizon">Blog</a>
</p>

---

MiMoCode is a terminal-native AI coding assistant. It can read and write code, run commands, manage Git, and use a persistent memory system to keep a deep understanding of your project across sessions while continuously improving itself.

MiMo Auto is built in as a free-for-limited-time channel, so you can start with zero configuration. MiMoCode also supports connecting to any mainstream LLM provider API.

---

## Quick Start

```bash
# One-line install (macOS / Linux)
curl -fsSL https://mimo.xiaomi.com/install | bash

# Or install via npm (all platforms)
# Mirror registries (e.g. cnpm/taobao) may have delayed platform package sync
npm install -g @mimo-ai/cli --registry https://registry.npmjs.org

# Run
mimo
```

<details>
<summary><strong>Windows native install (beta)</strong></summary>

PowerShell one-liner that installs to `%USERPROFILE%\.mimocode\bin` and adds to User PATH:

```powershell
powershell -ep Bypass -c "irm https://mimo.xiaomi.com/install.ps1 | iex"
```

**Note:** Installing versions prior to 0.1.5 with this method will cause `mimo upgrade` to not function. If you need to use an older version, please install via npm instead. Once 0.1.5+ is available, this becomes the recommended install method for Windows.

</details>

The first launch guides you through configuration automatically. Supported options:
- **MiMo Auto (free for a limited time)** — anonymous channel, zero configuration
- **Xiaomi MiMo Platform** — OAuth login
- **Import from Claude Code** — migrate existing authentication in one step
- **Custom Provider** — add any OpenAI-compatible API in the TUI

<details>
<summary><strong>WSL: clipboard issues</strong></summary>

If you encounter garbled text when copying on WSL, install `xsel`:
```bash
sudo apt install xsel
```
</details>

<details>
<summary><strong>Windows: garbled CJK (Chinese/Japanese/Korean) output in the shell</strong></summary>

On Windows with a non-UTF-8 system locale (e.g. zh-CN, whose active code page is 936/GBK),
command output containing CJK characters may appear garbled (mojibake). MiMoCode forces
UTF-8 output for spawned PowerShell/cmd subprocesses. If you still encounter garbled output
in cases this does not yet cover, enable Windows' system-wide UTF-8 support:

**Settings → Time & language → Language & region → Administrative language settings →
Change system locale → check "Beta: Use Unicode UTF-8 for worldwide language support" →
reboot.**

This switches the active code page (ACP) to UTF-8 (65001) for all programs, so subprocesses
no longer inherit the legacy code page. Note it is a system-wide Beta toggle and may cause
some older non-Unicode programs to display incorrectly, so treat it as a workaround.
</details>

---

## MiMo Ecosystem

Beyond MiMoCode, Xiaomi MiMo models also work in other agents and coding tools like Cursor, Cline, and Zed.

**[awesome-mimo-agent](https://github.com/XiaomiMiMo/awesome-mimo-agent)** collects setup guides for using MiMo in those tools — worth a look if you want to try MiMo elsewhere. Contributions welcome: open a PR to add your own setup.

---

## Core Features

### Multiple Agents

| Agent | Description |
|--------|------|
| **build** | Default. Full tool permissions for development |
| **plan** | Read-only analysis mode for code exploration and solution design |
| **compose** | Orchestration mode for specs-driven development and skill-driven workflows |

Press `Tab` to switch between primary agents. Subagents are created by the system as needed.

### Persistent Memory

Cross-session memory powered by SQLite FTS5 full-text search:

- **Project memory** (`MEMORY.md`) — persistent project knowledge, rules, and architecture decisions
- **Session checkpoint** (`checkpoint.md`) — structured state snapshots maintained automatically by the checkpoint-writer subagent
- **Scratch notes** (`notes.md`) — temporary note area for agents
- **Task progress** (`tasks/<id>/progress.md`) — per-task logs

Memory is injected automatically when a session resumes, so the agent does not need to relearn project context.

### Intelligent Context Management

- **Automatic checkpoints** — decides when to save session state based on the model context window
- **Context reconstruction** — when context approaches the limit, rebuilds it from the latest checkpoint, project memory, task progress, and retained recent messages so the agent can continue the current task
- **Budgeted injection** — uses a token budget to control how much checkpoint, memory, and notes content enters context, with importance ranking

### Ta