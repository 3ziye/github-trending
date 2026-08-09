<div align="center">

<br />

<!-- Absolute URLs, not repo-relative paths: this README is also the PyPI
     long_description, and PyPI renders it standalone with no assets/
     directory alongside it, so relative paths 404 there. -->
<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="https://raw.githubusercontent.com/NVIDIA-NeMo/labs-OO-Agents/main/assets/nvidia-labs-object-oriented-agents-dark.svg"
  >
  <source
    media="(prefers-color-scheme: light)"
    srcset="https://raw.githubusercontent.com/NVIDIA-NeMo/labs-OO-Agents/main/assets/nvidia-labs-object-oriented-agents-light.svg"
  >
  <img
    alt="NVIDIA-labs Object Oriented Agents"
    src="https://raw.githubusercontent.com/NVIDIA-NeMo/labs-OO-Agents/main/assets/nvidia-labs-object-oriented-agents-light.svg"
    width="820"
  >
</picture>

<p align="center"><b>A Pythonic way to build AI agents.</b></p>

[![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?logo=nvidia&logoColor=white)](https://www.nvidia.com/)
[![Paper](https://img.shields.io/badge/paper-arXiv-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2607.20709)
[![Blog](https://img.shields.io/badge/blog-NVIDIA-76B900?logo=nvidia&logoColor=white)](https://developer.nvidia.com/blog/six-agent-harness-capabilities-for-higher-model-performance/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](https://github.com/NVIDIA-NeMo/labs-OO-Agents/blob/main/LICENSE)

**[Quick Start](#quick-start)** &nbsp;·&nbsp; **[Examples](https://github.com/NVIDIA-NeMo/labs-OO-Agents/blob/main/examples/README.md)** &nbsp;·&nbsp; **[Paper](https://arxiv.org/abs/2607.20709)** &nbsp;·&nbsp; **[Blog](https://developer.nvidia.com/blog/six-agent-harness-capabilities-for-higher-model-performance/)**

<br />

</div>


NVIDIA-labs OO Agents (NOOA) is a model-agnostic Python framework designed to support reliable AI agent development. Many agent frameworks represent prompts, tools, callbacks, and workflows as separate abstractions. NOOA offers an alternative object-oriented interface that brings these concepts together in a Python class. NOOA lets developers express an agent’s state, capabilities, prompts, and typed interfaces through a single Python class:

```python
from nooa import Agent

# The agent is a Python object.
class SupportAgent(Agent):
    """You are a support agent."""

    # State lives on the object. Fields are typed.
    order_db: OrderDB

    # Ordinary method. Just Python.
    def is_refund_eligible(self, order: Order) -> bool:
        return order.delivered and order.days_since_delivery <= 30

    # Agentic method: the runtime hands this to an LLM.
    async def triage(self, message: str, order: Order) -> Ticket:
        """Create a typed support ticket."""
        ...
```

**What's happening here:**

- **Agents are Python objects.** Fields are state, methods are capabilities, docstrings are prompts, type annotations are contracts.
- **`...` bodies are LLM-driven.** A method with `...` becomes an agentic loop; a real body stays deterministic Python.
- **Code as action.** The model acts by writing Python in a Jupyter-style REPL with access to `self`, imports, and helpers — Python methods and type annotations supply the callable interfaces, reducing the need to write separate tool-schema definitions.
- **Pythonic and agent-ready.** Typed I/O with auto-retry, live-object arguments passed by reference, and model-callable context and event APIs — designed around agent-oriented Python workflows.

This design supports familiar Python testing, tracing, refactoring, and version-control workflows — **just like the rest of your software**. Read the paper for the design principles and evaluation results: [NVIDIA OO Agents: Native Python Object-Oriented Agents](https://arxiv.org/abs/2607.20709).

## Installation

Add the **core** framework to a new (or existing) Python project with [uv](https://docs.astral.sh/uv/getting-started/installation/):

```bash
uv init my-agent-project
cd my-agent-project

uv add nooa
```

Or with pip: `pip install nooa`.

<details>
<summary><b>Optional sub-packages</b> — CLI, memory, benchmarks, evaluation pipeline</summary>

<br />

The CLI, memory, and benchmark packages are separate distributions. Install
them by name, or pull them in as extras of the core package:

```bash
uv add nooa-cli                 # or: uv add "nooa[cli]"
uv add nooa-memory              # or: uv add "nooa[memory]"
uv add nooa-bench               # or: uv add "nooa[bench]"

uv add "nooa[cli,memory]"       # several at once
```

| Package | Extra | What it adds |
|---|---|---|
| `nooa-cli` | `nooa[cli]` | the `nooa` command, trace viewer, eval runner |
| `nooa-memory` | `nooa[memory]` | long-term memory subsystem (`MemoryManager`) |
| `nooa-bench` | `nooa[bench]` | `BenchAgent` and the Harbor benchmark runner |

`eval_pipeline` is not published to PyPI — install it from the repo:

```bash
uv add "eval_pipeline @ git+https://github.com/NVIDIA-NeMo/labs-OO-Agents.git@main