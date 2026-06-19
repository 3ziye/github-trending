# CodeSeek

**Code intelligence CLI tool for Claude Code.** AST-based call graph analysis + semantic search — right from your terminal.

## Quick Start

```bash
# Install via npm (handles setup wizard + binary download automatically)
npm install -g codeseek

# First run — interactive setup wizard configures your embedding model
codeseek

# Index your project
codeseek init

# Search code by symbol name
codeseek search main --limit 10

# Query call graph
codeseek callers main
codeseek callees process_data

# Register with Claude Code / Codex as MCP tools
codeseek install

# Check status
codeseek status

# Auto-index on git commits
codeseek install-hooks
```

## Install

### npm

```bash
npm install -g codeseek
```

The npm package ships a lightweight JS wrapper that handles:

| Step | Description |
|------|-------------|
| **First-run wizard** | Interactive CLI prompts for embedding API token, model, and base URL |
| **Binary download** | Automatically pulls the correct Rust binary for your platform from GitHub Releases |
| **Pass-through** | All commands (`init`, `search`, `callers`, etc.) are forwarded to the native binary |

Supported platforms:

| Platform | Architecture |
|----------|-------------|
| macOS | arm64 (Apple Silicon), x64 (Intel) |
| Linux | x64 |

### Homebrew

```bash
brew tap CodeBendKit/codeseek git@github.com:CodeBendKit/codeseek.git
brew install codeseek
```

### From source

```bash
git clone https://github.com/CodeBendKit/codeseek.git
cd codeseek
./build.sh --release
```

`build.sh` compiles both the TypeScript wrapper (`dist/`) and the Rust binary, then installs to `~/.codeseek/bin/`.

## Commands

| Command | Description |
|---------|-------------|
| `codeseek` | First-time setup wizard (configures embedding model interactively) |
| `codeseek init` | Build/update code index (full on first run, MD5-incremental thereafter) |
| `codeseek status` | Index statistics: functions, files, last update |
| `codeseek search <query>` | Symbol name search (falls back from vector → graph name match) |
| `codeseek callers <symbol>` | Find functions that call this symbol |
| `codeseek callees <symbol>` | Find functions this symbol calls |
| `codeseek list` | List all indexed projects with paths |
| `codeseek install` | Register codeseek as MCP tools in Claude Code / Codex |
| `codeseek uninstall` | Remove MCP integration |
| `codeseek uninit` | Delete the current project index |
| `codeseek install-hooks` | Install git hooks (post-commit/post-merge → `codeseek init`) |
| `codeseek serve --mcp` | Start MCP server (stdio JSON-RPC, used by Claude Code internally) |

All query commands support `--json` for machine-readable output.

## Claude Code / Codex Integration

```bash
codeseek install
```

Writes MCP server config to:

| Agent | Config file |
|-------|------------|
| **Claude Code** | `~/.claude.json` (global, all projects) or `./.mcp.json` (project-local) |
| **Codex CLI** | `~/.codex/config.toml` |

Claude Code auto-discovers these tools after restart:

| Tool | Capability |
|------|-----------|
| `codeseek_search` | Find symbols by name |
| `codeseek_callers` | Trace upstream callers |
| `codeseek_callees` | Trace downstream callees |
| `codeseek_status` | Check index health |

Remove integration:

```bash
codeseek uninstall
```

## How It Works

### Index Building (`codeseek init`)

```
Source files
  → Tree-sitter AST parse (7 languages)
  → Extract functions / classes / methods
  → Batch embed via API (20 texts per call, SQLite cache)
  → Store vectors in LanceDB
  → Build BM25 index in Tantivy
  → Serialize call graph (PetCodeGraph)
  → Save to ~/.codeseek/<project_hash>/
```

**Idempotent**: first run is full build, subsequent runs compare MD5 hashes — only changed files are re-processed. Use `codeseek install-hooks` for automatic re-index on git commit/merge.

### Hybrid Search Pipeline (`codeseek search`)

```
                        ┌─────────────────────┐
User query ────────────→│  Embedding Model     │──→ Query vector
                        └─────────────────────┘
                                  │
          ┌───────────────────────┼───────────────────────┐
          ▼                       ▼                       ▼
   ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
   │ Dense Search │       │ Sparse Search│       │ Graph Search │
   │ (LanceDB ANN)│       │ (Tantivy BM25)│      │ (PetCodeGraph)│
   └──────┬───────┘       └──────┬──────┘       └──────┬──────┘
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 ▼
                        ┌─────────────────┐
                        │   RRF Fusion    │  ← Reciprocal Rank Fusion
                        │  (Top-20 candidates)│
                        └────────┬────────┘
                                 │
                                 ▼
                        ┌─────────────────┐
                        │    Reranker     │  ← C