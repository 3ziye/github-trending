# OpenPlanter

A recursive-language-model investigation agent with a desktop GUI and terminal interface. OpenPlanter ingests heterogeneous datasets — corporate registries, campaign finance records, lobbying disclosures, government contracts, and more — resolves entities across them, and surfaces non-obvious connections through evidence-backed analysis. It operates autonomously with file I/O, shell execution, web search, and recursive sub-agent delegation.

![OpenPlanter Desktop](screenshot.png)

## Download

Pre-built binaries are available on the [Releases page](https://github.com/ShinMegamiBoson/OpenPlanter/releases/latest):

- **macOS** — `.dmg`
- **Windows** — `.msi`
- **Linux** — `.AppImage`

## Desktop App

The desktop app (`openplanter-desktop/`) is a Tauri 2 application with a three-pane layout:

- **Sidebar** — Session management, provider/model settings, and API credential status
- **Chat pane** — Conversational interface showing the agent's objectives, reasoning steps, tool calls, and findings with syntax-highlighted code blocks
- **Knowledge graph** — Interactive Cytoscape.js visualization of entities and relationships discovered during investigation. Nodes are color-coded by category (corporate, campaign-finance, lobbying, contracts, sanctions, etc.). Click a source node to open a slide-out drawer with the full rendered wiki document.

### Features

- **Live knowledge graph** — Entities and connections render in real time as the agent works. Switch between force-directed, hierarchical, and circular layouts. Search and filter by category.
- **Wiki source drawer** — Click any source node to read the full markdown document in a slide-out panel. Internal wiki links navigate between documents and focus the corresponding graph node.
- **Session persistence** — Investigations are saved automatically. Resume previous sessions or start new ones from the sidebar.
- **Background wiki curator** — A lightweight agent runs in the background to keep wiki documents consistent and cross-linked.
- **Multi-provider support** — Switch between OpenAI, Anthropic, OpenRouter, Cerebras, and Ollama (local) from the sidebar.

### Building from Source

```bash
cd openplanter-desktop

# Install frontend dependencies
cd frontend && npm install && cd ..

# Run in development mode
cargo tauri dev

# Build distributable binary
cargo tauri build
```

Requires: Rust stable, Node.js 20+, and platform-specific Tauri dependencies ([see Tauri prerequisites](https://v2.tauri.app/start/prerequisites/)).

## CLI Agent

The Python CLI agent can be used independently of the desktop app.

### Quickstart

```bash
# Install
pip install -e .

# Configure API keys (interactive prompt)
openplanter-agent --configure-keys

# Launch the TUI
openplanter-agent --workspace /path/to/your/project
```

Or run a single task headlessly:

```bash
openplanter-agent --task "Cross-reference vendor payments against lobbying disclosures and flag overlaps" --workspace ./data
```

### Docker

```bash
# Add your API keys to .env, then:
docker compose up
```

The container mounts `./workspace` as the agent's working directory.

## Supported Providers

| Provider | Default Model | Env Var |
|----------|---------------|---------|
| OpenAI | `gpt-5.2` | `OPENAI_API_KEY` |
| Anthropic | `claude-opus-4-6` | `ANTHROPIC_API_KEY` |
| OpenRouter | `anthropic/claude-sonnet-4-5` | `OPENROUTER_API_KEY` |
| Cerebras | `qwen-3-235b-a22b-instruct-2507` | `CEREBRAS_API_KEY` |
| Ollama | `llama3.2` | (none — local) |

### Local Models (Ollama)

[Ollama](https://ollama.com) runs models locally with no API key. Install Ollama, pull a model (`ollama pull llama3.2`), then:

```bash
openplanter-agent --provider ollama
openplanter-agent --provider ollama --model mistral
openplanter-agent --provider ollama --list-models
```

The base URL defaults to `http://localhost:11434/v1` and can be overridden with `OPENPLANTER_OLLAMA_BASE_URL` or `--base-url`. The first request may be slow while Ollama loads the model into memory; a 120-second first-byte timeout is used automatically.

Additional service keys: `EXA_API_KEY` (web search), `VOYAGE_API_KEY` (embeddings).

All keys can also be set with an `OPENPLANTER_` prefix (e.g. `OPENPLANTER_OPENAI_API_KEY`), via `.env` files in the workspace, or via CLI flags.

## Agent Tools

The agent has access to 19 tools, organized around its investigation workflow:

**Dataset ingestion & workspace** — `list_files`, `search_files`, `repo_map`, `read_file`, `write_file`, `edit_file`, `hashline_edit`, `apply_patch` — load, inspect, and transform source datasets; write structured findings.

**Shell execution** — `run_shell`, `run_shell_bg`, `check_shell_bg`, `kill_shell_bg` — run analysis scripts, data pipelines, and validation checks.

**Web** — `web_search` (Exa), `fetch_url` — pull public records, verify entities, and retrieve supplementary data.

**Planning & delegation** — `think`, `subtask`, `execute`, `list_artifacts`, `read_artifact` — decompose investi