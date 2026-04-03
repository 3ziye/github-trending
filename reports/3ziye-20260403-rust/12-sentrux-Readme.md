<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg?v=2">
  <source media="(prefers-color-scheme: light)" srcset="assets/logo-light.svg?v=2">
  <img alt="sentrux" src="assets/logo-dark.svg?v=2" width="500">
</picture>

<br>

**The sensor that helps AI agents close the feedback loop.<br>Recursive self-improvement of code quality.**


[![CI](https://github.com/sentrux/sentrux/actions/workflows/ci.yml/badge.svg)](https://github.com/sentrux/sentrux/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/sentrux/sentrux)](https://github.com/sentrux/sentrux/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)


**English** | [中文](README.zh-CN.md) | [Deutsch](README.de.md) | [日本語](README.ja.md)

[How it Works](#how-it-works) · [Quick Start](#quick-start) · [MCP Integration](#mcp-server) · [Rules Engine](#rules-engine) · [Releases](https://github.com/sentrux/sentrux/releases)

</div>

<br>

<div align="center">

![sentrux demo](assets/demo.gif)

</div>

<div align="center">
<sub>Live: Claude Code Opus 4.6 builds a FastAPI project. Even with good prompts, quality lands at 6772.</sub>
<br>
<sub>Not because the agent can't do better — but because without a sensor, it doesn't know what to improve.</sub>
</div>

<div align="center">
<img src="assets/screenshot-health.gif" width="360" alt="Quality Signal">
</div>

## How it works

<div align="center">
<img src="assets/how-it-works.svg" width="600" alt="How sentrux works: scan → score → agent improves → rescan → better score → repeat">
</div>


## Quick Start

**Install** (macOS · Linux · Windows)

**macOS**
```bash
brew install sentrux/tap/sentrux
```

**Linux**
```bash
curl -fsSL https://raw.githubusercontent.com/sentrux/sentrux/main/install.sh | sh
```

**Windows** — download from [Releases](https://github.com/sentrux/sentrux/releases), or:
```
curl -L -o sentrux.exe https://github.com/sentrux/sentrux/releases/latest/download/sentrux-windows-x86_64.exe
```

Pure Rust. Single binary. No runtime dependencies. **52 languages** via tree-sitter plugins. Runs on **macOS**, **Linux**, and **Windows**.

**Run it**

```bash
sentrux                    # open the GUI — live treemap of your project
sentrux /path/to/project   # open GUI scanning a specific directory
sentrux check .            # check rules (CI-friendly, exits 0 or 1)
sentrux gate --save .      # save baseline before agent session
sentrux gate .             # compare after — catches degradation
```

**Connect to your AI agent (optional)**

Give your agent real-time access to structural health via [MCP](https://modelcontextprotocol.io).

Claude Code:

```
/plugin marketplace add sentrux/sentrux
/plugin install sentrux
```

Cursor / Windsurf / OpenCode / OpenClaw / any MCP client — add to your MCP config:

```json
{
  "mcpServers": {
    "sentrux": {
      "command": "sentrux",
      "args": ["--mcp"]
    }
  }
}
```

**From source / upgrade / troubleshooting**

```bash
# Build from source
git clone https://github.com/sentrux/sentrux.git
cd sentrux && cargo build --release

# Upgrade
brew update && brew upgrade sentrux
# or re-run the curl install — it always pulls the latest release
```

**Linux GPU issues?** If the app won't start, sentrux automatically tries multiple GPU backends (Vulkan → GL → fallback). You can also force one:

```bash
WGPU_BACKEND=vulkan sentrux    # force Vulkan
WGPU_BACKEND=gl sentrux        # force OpenGL
```

<br>

## The problem nobody talks about

You start a project with Claude Code or Cursor. Day one is magic. The agent writes clean code, understands your intent, ships features fast.

Then something shifts.

The agent starts hallucinating functions that don't exist. It puts new code in the wrong place. It introduces bugs in files it touched yesterday. You ask for a simple feature and it breaks three other things. You're spending more time fixing the agent's output than writing it yourself.

Everyone assumes the AI got worse. **It didn't.** Your codebase did.

Here's what actually happened: when you used an IDE, you saw the file tree. You opened files. You built a mental model of the architecture — which module does what, how they connect, where things belong. You were the governor. Every edit passed through your understanding of the whole.

Then AI agents moved us to the terminal. The agent modifies dozens of files per session. You see a stream of `Modified src/foo.rs` — but you've lost the spatial awareness. You don't see where that file sits in the dependency graph. You don't see that it just created a cycle. You don't see that three modules now depend on a file that was supposed to be internal. Many developers let AI agents build entire applications without ever opening the file browser.

**You've lost control. And you don't even know it yet.**

Every AI session silently degrades your architecture. Same function names, different purposes, scattered across files. Unrelated c