# SmallCode

[简体中文](README_zh-CN.md) | [English](README.md)

---

[![npm](https://img.shields.io/npm/v/smallcode)](https://www.npmjs.com/package/smallcode)

**AI coding agent optimized for small LLMs (8B-35B parameters)**

SmallCode is a terminal-native coding agent designed from the ground up to extract useful work from local models (8B-35B) running on consumer hardware. While tools like OpenCode assume frontier models with 128k+ context and perfect tool calling, SmallCode compensates for the limitations of small models through intelligent architecture.

> **Recommended model size: 8B-35B parameters.** Smaller models (≤4B) struggle with multi-step tool use and lose context across turns. Larger models (>35B) don't need SmallCode's adaptations and are better served by tools designed for frontier models.

## Why SmallCode?

| | OpenCode | SmallCode |
|---|----------|-----------|
| **Target** | Frontier models (Claude, GPT-5) | 8B-35B local models |
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
# Or use the packaged command alias:
smolv2
```

### Prebuilt Binaries (no Node.js needed)

Pre-compiled tarballs for Windows, macOS, and Linux are built on every release — they bundle Node.js plus all native addons so you never need `node-gyp` or C++ build tools.

| Platform | One‑line install |
|---|---|
| Linux / macOS | `bash <(curl -fsSL https://raw.githubusercontent.com/Doorman11991/smallcode/master/install.sh)` |
| Windows | `iwr -Uri https://raw.githubusercontent.com/Doorman11991/smallcode/master/install.ps1 -UseBasicParsing \| iex` |

The install script downloads the correct tarball for your platform, extracts it to `~/.smallcode`, and adds it to your PATH. Run `smallcode --help` to verify.

SmallCode includes [BoneScript](https://github.com/Doorman11991/BoneScript) and [budget-aware-mcp](https://github.com/Doorman11991/budget-aware-mcp) as dependencies — everything installs in one go.

### Fresh GitHub checkout quick start

If you just cloned/pulled this repository, run it directly from the checkout first:

```bash
cd smallcode
npm install

# Start your local model server first (LM Studio, llama.cpp, Ollama, etc.)
cat > .env <<'EOF'
SMALLCODE_MODEL=your-local-model-name
SMALLCODE_BASE_URL=http://localhost:1234/v1
EOF

node bin/smallcode.js
```

Optional: make the `smallcode` and `smallcode-rag-index` commands available globally from this checkout:

```bash
npm link
smallcode --help
```

If the fullscreen UI has display issues in your terminal, start with `node bin/smallcode.js --classic`.

The fullscreen TUI enables raw mode, mouse tracking, and bracketed paste. SmallCode always restores your terminal on exit — including when you suspend it with `Ctrl+Z` (it cleans up before stopping, then redraws on `fg`), when it is terminated, or if it crashes. If a hard kill (`kill -9`) ever leaves your shell echoing raw escape sequences, run `reset` to restore it.

### RAG harness quick run

SmallCode runs as a terminal UI harness by default:

```bash
smallcode                 # fullscreen TUI
smallcode --classic       # readline UI fallback
node bin/smallcode.js     # from a repo checkout
```

To build the local GitHub RAG database, run the Python scraper/indexer with the curated starter corpus, or use the broader preset for a larger multi-language corpus:

```bash
npm run rag:index
npm run rag:index -- --preset broad
# or, after install:
smallcode-rag-index --preset broad
```

For custom repos, create `.smallcode/rag/repos.json` with `preset`, `repos`, and chunking limits.

See [docs/rag-harness.md](docs/rag-harness.md) for the full LM Studio/llama.cpp setup, UI walkthrough, RAG config, indexing, and web-fallback flow.

### Requirements

- Node.js 18+ (LTS recommended — 20.x or 22.x have prebuilt binaries for SQLite)
- Python 3 + Git for the RAG scraper/indexer (`npm run rag:index`)
- A local LLM server (LM Studio, Ollama, or any OpenAI-compatible endpoint)

**Optional** (for code graph + FTS5 memory search):
- `better-sqlite3` needs native compilation if prebuilt binaries aren't available for your Node version
- Prebuilt binaries exist for Node LTS (20.x, 22.x) on Linux/macOS/Windows. no build tools needed
- If you're on a non-LTS Node (23+, 25+), you'll need:
  - **Linux**: `python3`, `make`, `gcc`/`g++` (`sudo apt install build-essential python3` or `pacman -S base-devel python`)
  - **macOS**: Xcode Command Line Tools (`xcode-select --install`)
  - **Windows**: Visual Studio Build Tools with "Desktop development with C++" workload, or `npm install -g windows-bu