<div align="center">
  <img src="clawlet.png" alt="clawlet" width="500">
  <h1>Clawlet</h1>
  <h3>Ultra-lightweight and efficient personal AI assistant</h3>
</div>

**Clawlet** is a lightweight personal AI agent with hybrid semantic memory search — a single static binary with no runtime and no CGO.  
Bundled SQLite + sqlite-vec. Drop it on any machine and memory search just works.

This project is inspired by **OpenClaw** and **nanobot**.

## Install

Download from [GitHub Releases](https://github.com/mosaxiv/clawlet/releases/latest).

macOS (Apple Silicon):
```bash
curl -L https://github.com/mosaxiv/clawlet/releases/latest/download/clawlet_Darwin_arm64.tar.gz | tar xz
mv clawlet ~/.local/bin/
```

## Quick Start

```bash
# Initialize
clawlet onboard \
  --openrouter-api-key "sk-or-..." \
  --model "openrouter/anthropic/claude-sonnet-4.5"

# Check effective configuration
clawlet status

# Chat
clawlet agent -m "What is 2+2?"
```

## Configuration (`~/.clawlet/config.json`)

Config file: `~/.clawlet/config.json`

### Supported providers

clawlet currently supports these LLM providers:

- **OpenAI** (`openai/<model>`, API key: `env.OPENAI_API_KEY`)
- **OpenAI Codex (OAuth)** (`openai-codex/<model>`, no API key; login: `clawlet provider login openai-codex`)
- **OpenRouter** (`openrouter/<provider>/<model>`, API key: `env.OPENROUTER_API_KEY`)
- **Anthropic** (`anthropic/<model>`, API key: `env.ANTHROPIC_API_KEY`)
- **Gemini** (`gemini/<model>`, API key: `env.GEMINI_API_KEY` or `env.GOOGLE_API_KEY`)
- **Local (Ollama / vLLM / OpenAI-compatible local endpoint)** (`ollama/<model>` or `local/<model>`, default base URL: `http://localhost:11434/v1`, API key optional)

Minimal config (OpenRouter):

```json
{
  "env": { "OPENROUTER_API_KEY": "sk-or-..." },
  "agents": { "defaults": { "model": "openrouter/anthropic/claude-sonnet-4-5" } }
}
```

Agent generation defaults are configurable:

```json
{
  "agents": {
    "defaults": {
      "model": "openrouter/anthropic/claude-sonnet-4-5",
      "maxTokens": 8192,
      "temperature": 0.7
    }
  }
}
```

Minimal config (Local via Ollama):

```json
{
  "agents": { "defaults": { "model": "ollama/qwen2.5:14b" } }
}
```

Minimal config (Local via vLLM using the same `ollama/` route):

```json
{
  "agents": { "defaults": { "model": "ollama/meta-llama/Llama-3.1-8B-Instruct" } },
  "llm": { "baseURL": "http://localhost:8000/v1" }
}
```

OpenAI Codex (OAuth):

```bash
# one-time login
clawlet provider login openai-codex

# headless environment (SSH / container)
clawlet provider login openai-codex --device-code
```

```json
{
  "agents": { "defaults": { "model": "openai-codex/gpt-5.1-codex" } }
}
```

### Option: Memory search setup

To enable semantic memory search, add `memorySearch` to the agent defaults:

```json
{
  "env": {
    "OPENAI_API_KEY": "sk-..."
  },
  "agents": {
    "defaults": {
      "memorySearch": {
        "enabled": true,
        "provider": "openai",
        "model": "text-embedding-3-small"
      }
    }
  }
}
```

Local embedding (Ollama / OpenAI-compatible local endpoint):

```json
{
  "agents": {
    "defaults": {
      "memorySearch": {
        "enabled": true,
        "provider": "openai",
        "model": "nomic-embed-text",
        "remote": {
          "baseURL": "http://localhost:11434/v1"
        }
      }
    }
  }
}
```

When enabled:
- The agent gains `memory_search` and `memory_get` tools for retrieving past context.
- clawlet indexes `MEMORY.md`, `memory.md`, and `memory/**/*.md` for retrieval.
- The index DB is created at `{workspace}/.memory/index.sqlite`.

When disabled (default):
- `memorySearch.enabled` defaults to `false`; the search tools are not exposed to the model.
- Memory files (`memory/MEMORY.md`, `memory/YYYY-MM-DD.md`) are still injected into context as usual.
- Normal chat behavior is otherwise unchanged.


## Security

### Secure Defaults
- `tools.restrictToWorkspace` defaults to `true` (tools can only access files inside the workspace directory)
- `gateway.listen` defaults to `127.0.0.1:18790`
- `gateway.allowPublicBind` defaults to `false`

### Security Checklist

| Item | Status | Details |
| --- | --- | --- |
| Gateway not publicly exposed | ✅ | Default bind is localhost only. Public bind is rejected unless `gateway.allowPublicBind=true` is explicitly set. |
| Filesystem scoped (no `/`) | ✅ | File tools block root path, path traversal, encoded traversal, symlink escapes, and sensitive state paths. |
| Exec tool dangerous-command guard | ✅ | `exec` blocks unsafe shell constructs (command chaining, unsafe expansions, redirection/`tee`, dangerous patterns), blocks sensitive paths, and passes only allowlisted environment variables to subprocesses. |

## Tools

### Multimodal input (audio/image/attachments)

Inbound channel messages can include attachments. clawlet can:

- send images to vision-capable models,
- transcribe audio using the configured provider,
- and inline text-like file attachments into the user context.

Conf