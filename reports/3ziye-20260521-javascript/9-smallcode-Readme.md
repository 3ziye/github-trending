# SmallCode

[简体中文](README_zh-CN.md) | [English](README.md)

---

[![npm](https://img.shields.io/npm/v/smallcode)](https://www.npmjs.com/package/smallcode)

**AI coding agent optimized for small LLMs (≤20B parameters)**

SmallCode is a terminal-native coding agent designed from the ground up to extract useful work from local models (7B-20B) running on consumer hardware. While tools like OpenCode assume frontier models with 128k+ context and perfect tool calling, SmallCode compensates for the limitations of small models through intelligent architecture.

## Why SmallCode?

| | OpenCode | SmallCode |
|---|----------|-----------|
| **Target** | Frontier models (Claude, GPT-5) | 7B-20B local models |
| **Context** | Dumps everything | Budget-managed, summarized |
| **Tool calling** | Assumes reliable JSON | Forgiving multi-format parser |
| **Planning** | Single-shot | TODO-file decomposed steps |
| **Editing** | Full file write | Search-and-replace patch |
| **Privacy** | API calls to cloud | Fully local, no network needed |

## Quick Start

```bash
# Install globally via npm
npm install -g smallcode

# Or run directly with npx
npx smallcode

# Start in your project directory
cd my-project
smallcode
```

### Prebuilt Binaries (no Node.js needed)

Pre-compiled tarballs for Windows, macOS, and Linux are built on every release — they bundle Node.js plus all native addons so you never need `node-gyp` or C++ build tools.

| Platform | One‑line install |
|---|---|
| Linux / macOS | `bash <(curl -fsSL https://raw.githubusercontent.com/Doorman11991/smallcode/master/install.sh)` |
| Windows | `iwr -Uri https://raw.githubusercontent.com/Doorman11991/smallcode/master/install.ps1 -UseBasicParsing \| iex` |

The install script downloads the correct tarball for your platform, extracts it to `~/.smallcode`, and adds it to your PATH. Run `smallcode --help` to verify.

SmallCode includes [BoneScript](https://github.com/Doorman11991/BoneScript) and [budget-aware-mcp](https://github.com/Doorman11991/budget-aware-mcp) as dependencies — everything installs in one go.

### Requirements

- Node.js 18+ (LTS recommended — 20.x or 22.x have prebuilt binaries for SQLite)
- A local LLM server (LM Studio, Ollama, or any OpenAI-compatible endpoint)

**Optional** (for code graph + FTS5 memory search):
- `better-sqlite3` needs native compilation if prebuilt binaries aren't available for your Node version
- Prebuilt binaries exist for Node LTS (20.x, 22.x) on Linux/macOS/Windows. no build tools needed
- If you're on a non-LTS Node (23+, 25+), you'll need:
  - **Linux**: `python3`, `make`, `gcc`/`g++` (`sudo apt install build-essential python3` or `pacman -S base-devel python`)
  - **macOS**: Xcode Command Line Tools (`xcode-select --install`)
  - **Windows**: Visual Studio Build Tools with "Desktop development with C++" workload, or `npm install -g windows-build-tools`
- **If build fails, SmallCode still works** — it falls back to JSON-based memory automatically

### Configuration

Create a `.env` file in your project root:

```bash
# Required
SMALLCODE_MODEL=your-model-name
SMALLCODE_BASE_URL=http://localhost:1234/v1

# Optional: escalation (auto-fallback to cloud on hard fail)
# ANTHROPIC_API_KEY=sk-ant-...
# OPENAI_API_KEY=sk-...
# DEEPSEEK_API_KEY=sk-...
```

You can override the endpoint for one run with:

```bash
smallcode --endpoint http://localhost:1234/v1 --model your-model-name
```

See `.env.example` for all options. Also supports `smallcode.toml` for backwards compatibility.

## Architecture

SmallCode is built with a modular architecture:

```
bin/
├── smallcode.js        Entry point, agent loop, TUI orchestration (1570 lines)
├── config.js           Config loading, endpoint detection, auth headers
├── executor.js         Tool execution (all 18 tools)
├── tools.js            Tool definitions + 2-stage routing
├── mcp_bridge.js       Built-in code graph MCP communication
├── model_client.js     LLM API calls, streaming, validation
├── governor.js         Tool scoring, verification, decompose
├── escalation.js       Cloud model fallback (Claude/OpenAI/DeepSeek)
├── commands.js         TUI slash commands
├── tui.js              Classic TUI renderer
└── bonescript_guide.js BoneScript syntax reference

src/
├── api/index.js        Programmatic API (require('smallcode'))
├── security/sanitize.js Centralized redaction, path safety, shell escaping
├── tui/fullscreen.js   Fullscreen alternate-buffer TUI
├── plugins/loader.js   Plugin system
├── plugins/skills.js   Skill system
├── tools/              Tool routing, MCP client, validators
├── governor/           Early-stop detection, verifier, tool scorer
├── model/              Multi-model profiles + routing
└── session/            Persistence, undo, sharing, references
```

## Security & Context-Leak Hardening

SmallCode runs untrusted-ish input — model output, MCP server output, tool
results, web pages — back into a context window. The `src/security/sanitize.js`
module is the single chok