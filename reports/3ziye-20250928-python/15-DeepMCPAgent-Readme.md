<!-- Banner / Title -->
<div align="center">
  <img src="docs/images/icon.png" width="120" alt="DeepMCPAgent Logo"/>

  <h1>🤖 DeepMCPAgent</h1>
  <p><strong>Model-agnostic LangChain/LangGraph agents powered entirely by <a href="https://modelcontextprotocol.io/">MCP</a> tools over HTTP/SSE.</strong></p>

  <!-- Badges -->
  <p>
    <a href="https://cryxnet.github.io/DeepMCPAgent">
      <img alt="Docs" src="https://img.shields.io/badge/docs-latest-brightgreen.svg">
    </a>
    <a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue.svg"></a>
    <a href="#"><img alt="License" src="https://img.shields.io/badge/License-Apache%202.0-blue.svg"></a>
    <a href="#"><img alt="Status" src="https://img.shields.io/badge/status-beta-orange.svg"></a>

<p>
  <a href="https://www.producthunt.com/products/deep-mcp-agents?utm_source=badge-featured&utm_medium=badge&utm_source=badge-deep-mcp-agents" target="_blank">
    <img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1011071&theme=light" alt="Deep MCP Agents on Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" />
  </a>
</p> 
  </p>

  <p>
    <em>Discover MCP tools dynamically. Bring your own LangChain model. Build production-ready agents—fast.</em>
  </p>

  <p>
    📚 <a href="https://cryxnet.github.io/deepmcpagent/">Documentation</a> • 🛠 <a href="https://github.com/cryxnet/deepmcpagent/issues">Issues</a>
  </p>
</div>

<hr/>

## ✨ Why DeepMCPAgent?

- 🔌 **Zero manual tool wiring** — tools are discovered dynamically from MCP servers (HTTP/SSE)
- 🌐 **External APIs welcome** — connect to remote MCP servers (with headers/auth)
- 🧠 **Model-agnostic** — pass any LangChain chat model instance (OpenAI, Anthropic, Ollama, Groq, local, …)
- ⚡ **DeepAgents (optional)** — if installed, you get a deep agent loop; otherwise robust LangGraph ReAct fallback
- 🛠️ **Typed tool args** — JSON-Schema → Pydantic → LangChain `BaseTool` (typed, validated calls)
- 🧪 **Quality bar** — mypy (strict), ruff, pytest, GitHub Actions, docs

> **MCP first.** Agents shouldn’t hardcode tools — they should **discover** and **call** them. DeepMCPAgent builds that bridge.

---

## 🚀 Installation

Install from [PyPI](https://pypi.org/project/deepmcpagent/):

```bash
pip install "deepmcpagent[deep]"
```

This installs DeepMCPAgent with **DeepAgents support (recommended)** for the best agent loop.
Other optional extras:

- `dev` → linting, typing, tests
- `docs` → MkDocs + Material + mkdocstrings
- `examples` → dependencies used by bundled examples

```bash
# install with deepagents + dev tooling
pip install "deepmcpagent[deep,dev]"
```

⚠️ If you’re using **zsh**, remember to quote extras:

```bash
pip install "deepmcpagent[deep,dev]"
```

---

## 🚀 Quickstart

### 1) Start a sample MCP server (HTTP)

```bash
python examples/servers/math_server.py
```

This serves an MCP endpoint at: **[http://127.0.0.1:8000/mcp](http://127.0.0.1:8000/mcp)**

### 2) Run the example agent (with fancy console output)

```bash
python examples/use_agent.py
```

**What you’ll see:**

![screenshot](/docs/images/screenshot_output.png)

---

## 🧑‍💻 Bring-Your-Own Model (BYOM)

DeepMCPAgent lets you pass **any LangChain chat model instance** (or a provider id string if you prefer `init_chat_model`):

```python
import asyncio
from deepmcpagent import HTTPServerSpec, build_deep_agent

# choose your model:
# from langchain_openai import ChatOpenAI
# model = ChatOpenAI(model="gpt-4.1")

# from langchain_anthropic import ChatAnthropic
# model = ChatAnthropic(model="claude-3-5-sonnet-latest")

# from langchain_community.chat_models import ChatOllama
# model = ChatOllama(model="llama3.1")

async def main():
    servers = {
        "math": HTTPServerSpec(
            url="http://127.0.0.1:8000/mcp",
            transport="http",    # or "sse"
            # headers={"Authorization": "Bearer <token>"},
        ),
    }

    graph, _ = await build_deep_agent(
        servers=servers,
        model=model,
        instructions="Use MCP tools precisely."
    )

    out = await graph.ainvoke({"messages":[{"role":"user","content":"add 21 and 21 with tools"}]})
    print(out)

asyncio.run(main())
```

> Tip: If you pass a **string** like `"openai:gpt-4.1"`, we’ll call LangChain’s `init_chat_model()` for you (and it will read env vars like `OPENAI_API_KEY`). Passing a **model instance** gives you full control.

---

## 🖥️ CLI (no Python required)

```bash
# list tools from one or more HTTP servers
deepmcpagent list-tools \
  --http name=math url=http://127.0.0.1:8000/mcp transport=http \
  --model-id "openai:gpt-4.1"

# interactive agent chat (HTTP/SSE servers only)
deepmcpagent run \
  --http name=math url=http://127.0.0.1:8000/mcp transport=http \
  --model-id "openai:gpt-4.1"
```

> The CLI accepts **repeated** `--http` blocks; add `header.X=Y` pairs for auth:
>
> ```
> --http name=ext url=https://api.example.com/mcp transport=http header.Authorization="Bearer TOKEN