# ccglass

**See exactly what your coding agent sends to the model.** A lightweight
local logging reverse-proxy + web dashboard for **Claude Code, Codex,
OpenCode, DeepSeek-TUI, Reasonix, Kimi, Ollama, OpenRouter, and more**.
One command, like `ollama`:

```bash
npm install -g ccglass
ccglass
```

<p align="center">
  <img src="https://raw.githubusercontent.com/jianshuo/ccglass/main/docs/demo.gif" alt="ccglass dashboard — live request capture, token/cache/cost, message history with tool calls, the agent-loop flow view, and a turn-to-turn diff" width="100%">
</p>

Run with no arguments and `ccglass` asks which client to inspect:

```
  Which client do you want to inspect?

    1) Claude Code
    2) Codex (OpenAI)
    3) DeepSeek-TUI
    4) Reasonix
    5) Kimi (Moonshot, via Claude Code)
    6) OpenCode

  >
```

Or name it directly: `ccglass claude`, `ccglass codex`, `ccglass deepseek`,
`ccglass deepseek-tui`, `ccglass reasonix`, `ccglass dsnix`, or `ccglass kimi`.

`ccglass` starts a proxy, points the client at it via the right base-URL env var,
launches it for you, and opens a dashboard where you watch every request in real
time — the full system prompt, every tool schema, the message history,
token/cache/cost numbers, and a turn-to-turn diff.

```
  ● ccglass watching Codex (OpenAI) → https://api.openai.com
    dashboard: http://127.0.0.1:57633
```

## Why

These CLIs are Node/native apps that **ignore `HTTP_PROXY`/`HTTPS_PROXY`** — so
Charles/mitmproxy never see the traffic, and `fetch`-patching tools break across
updates. `ccglass` sidesteps all of it: the client does the HTTPS to the real API
itself; you only intercept the plain HTTP hop to localhost. No CA certs, no TLS
pinning.

## Providers

| `ccglass <provider>` or `--provider` | Wraps | Env var | Upstream | Format |
|---|---|---|---|---|
| `claude` | Claude Code | `ANTHROPIC_BASE_URL` | api.anthropic.com | Anthropic Messages |
| `codex` | Codex | `OPENAI_BASE_URL` | api.openai.com | OpenAI Responses / Chat |
| `deepseek` | DeepSeek-TUI dispatcher | `DEEPSEEK_BASE_URL` | api.deepseek.com | OpenAI Chat |
| `deepseek-tui` | DeepSeek-TUI runtime | `DEEPSEEK_BASE_URL` | api.deepseek.com | OpenAI Chat |
| `reasonix` | Reasonix | `DEEPSEEK_BASE_URL` | api.deepseek.com | OpenAI Chat |
| `dsnix` | Reasonix (`dsnix` alias) | `DEEPSEEK_BASE_URL` | api.deepseek.com | OpenAI Chat |
| `kimi` | Claude Code → Moonshot | `ANTHROPIC_BASE_URL` | api.moonshot.ai/anthropic | Anthropic Messages |
| `opencode` | OpenCode | `OPENAI_BASE_URL` | auto (from env) | OpenAI Chat |
| `ollama` | any Ollama-backed client | `OPENAI_BASE_URL` | 127.0.0.1:11434 | OpenAI Chat |
| `lmstudio` | any LM Studio-backed client | `OPENAI_BASE_URL` | 127.0.0.1:1234 | OpenAI Chat |
| `openrouter` | any OpenRouter-backed client | `OPENAI_BASE_URL` | openrouter.ai/api | OpenAI Chat |
| `glm` | any GLM/Zhipu-backed client | `OPENAI_BASE_URL` | auto (from env) | OpenAI Chat |
| `bedrock` | Claude Code → AWS Bedrock | `ANTHROPIC_BEDROCK_BASE_URL` | auto (from env) | Anthropic Messages |
| `vertex` | Claude Code → Google Vertex AI | `ANTHROPIC_BASE_URL` | auto (from env) | Anthropic Messages |
| `run --provider <p> -- <cmd>` | any client | per provider | per provider | per provider |

**Notes by provider:**

- **Codex** — captures traffic when Codex is in **API-key mode** (`OPENAI_API_KEY`). If Codex is authenticated via **ChatGPT login**, it uses a WebSocket transport (`wss://chatgpt.com/...`) that bypasses `OPENAI_BASE_URL` — the dashboard will be empty. Run `codex doctor` to check your auth mode; if it shows `auth mode: chatgpt`, switch to API-key mode to use ccglass.
- **Kimi** — runs through Claude Code against Moonshot's Anthropic-compatible endpoint; set `ANTHROPIC_AUTH_TOKEN` to your Moonshot key.
- **DeepSeek-TUI** — OpenAI-compatible Chat Completions; set `DEEPSEEK_API_KEY`.
- **Reasonix** — OpenAI-compatible Chat Completions; set `DEEPSEEK_API_KEY`.
- **OpenCode** — auto-detects upstream from `OPENAI_BASE_URL`; set it before running. Use `--env-var` if your OpenCode provider uses a different env var name.
- **Ollama / LM Studio** — no key needed for local models; pass `--upstream` if your server runs on a non-default address.
- **OpenRouter** — set `OPENAI_API_KEY` to your OpenRouter key.
- **GLM/Zhipu** — set `OPENAI_BASE_URL` to your Zhipu endpoint (e.g. `https://open.bigmodel.cn/api/paas/v4`) and `OPENAI_API_KEY` to your Zhipu key.
- **AWS Bedrock** — set `ANTHROPIC_BEDROCK_BASE_URL` to your Bedrock endpoint before running. Claude Code in Bedrock mode reads its endpoint from this var (not `ANTHROPIC_BASE_URL`). Works against Bedrock-compat gateways (bearer / mTLS auth). Direct AWS endpoints (`*.amazonaws.com`) will fail through the proxy because SigV4 signs the Host header — ccglass prints a warning if it detects this.
- **Google Vertex AI** — set `ANTHROPIC_BASE_URL` to your Vertex AI endpoint (e.g. `https://us-east5-aiplatform.googleapis.com`) before running; GCP credentials are fo