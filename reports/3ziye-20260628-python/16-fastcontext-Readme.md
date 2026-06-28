# FastContext: Training Efficient Repository Explorer for Coding Agents

<p align="center">
  <a href="https://arxiv.org/abs/2606.14066"><img src="https://img.shields.io/badge/arXiv-2606.14066-b31b1b.svg" alt="arXiv"></a>
  <a href="https://github.com/microsoft/fastcontext"><img src="https://img.shields.io/badge/Code-GitHub-181717.svg" alt="Code"></a>
  <img src="https://img.shields.io/badge/Python-3.12%2B-blue.svg" alt="Python 3.12+">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
</p>

<p align="center">
  <a href="#news">📰 News</a> |
  <a href="#overview">🔎 Overview</a> |
  <a href="#results">📊 Results</a> |
  <a href="#quick-start">⚡ Quick Start</a> |
  <a href="#reproduction">🧪 Reproduction</a> |
  <a href="#citation">📚 Citation</a>
</p>

FastContext is a lightweight repository-exploration subagent for coding agents. Instead of letting the main
coding agent spend its own context window on broad file reads and code searches, the main agent delegates
a natural-language context query to FastContext. FastContext explores the repository with read-only tools,
issues independent tool calls in parallel, and returns compact file-line citations as focused evidence for the
main agent.

<p align="center">
  <img src="figures/overview.png" alt="FastContext overview" width="95%">
</p>

## News

- 🚀 **2026-06-15**: We released the arXiv paper [[📄 arXiv](https://arxiv.org/abs/2606.14066)] and the model weights [[🤗 Model](https://huggingface.co/collections/microsoft/swe-fastcontext)].


## Overview

Modern coding agents often use the same model to explore a repository and solve the task. This makes
exploration expensive: exploratory reads and searches consume tokens, stay in the solver's history, and can
pollute later reasoning with irrelevant snippets.

FastContext separates repository exploration from solving:

- 🧭 **Delegated exploration**: the main agent asks FastContext for repository context before editing or answering.
- 🔒 **Read-only tools**: FastContext uses `Read`, `Glob`, and `Grep`; it does not modify files.
- ⚙️ **Parallel tool calling**: independent reads and searches can be issued in the same exploration turn.
- 📌 **Compact evidence**: the final response is a short `<final_answer>` block with file paths and line ranges.
- 🧠 **Trainable explorers**: the paper trains 4B-30B exploration models with SFT and task-grounded RL.

The intended contract is simple: FastContext finds the relevant code; the main coding agent uses that focused
evidence to edit, test, or answer.

```text
<final_answer>
/path/to/repo/src/router.py:42-58
/path/to/repo/tests/test_router.py:101-119
</final_answer>
```

## Results

Across SWE-bench Multilingual, SWE-bench Pro, and SWE-QA, FastContext improves the score-token tradeoff of
Mini-SWE-Agent style coding agents.

| Result | Finding |
| --- | --- |
| 📈 End-to-end success | Up to **+5.5** score improvement with delegated repository exploration. |
| 💸 Main-agent token use | Up to **60.3%** fewer main-agent tokens. |
| 🧠 Compact trained explorer | FC-4B-RL improves or ties FC-4B-SFT across all reported end-to-end settings. |
| 🎯 Standalone exploration | Trained FastContext models recover patch-relevant files and symbols more accurately than non-FastContext small-model baselines. |

<p align="center">
  <img src="figures/main-result.png" alt="FastContext main results" width="95%">
</p>

## Token Efficiency

FastContext reduces the main agent's context burden by moving broad repository exploration outside the
solver trajectory. The reduction is especially visible in file-reading and code-search tokens.

<p align="center">
  <img src="figures/breakdown.png" alt="FastContext token breakdown" width="95%">
</p>

## Installation

FastContext requires Python 3.12 or newer. The repository uses [`uv`](https://docs.astral.sh/uv/) for package
and environment management.

Install the CLI from the repository root:

```bash
uv tool install .
```

For development:

```bash
uv sync --all-groups
```

Build a local wheel:

```bash
uv build
```

The built wheel is written under `dist/`, for example:

```text
dist/fastcontext-0.1.0-py3-none-any.whl
```

## Model Configuration

FastContext expects an OpenAI-compatible chat completions endpoint. For direct CLI usage, configure:

```bash
export FC_BASE_URL="https://your-endpoint.example/v1"
export FC_MODEL="your-model-name"

# optional: only needed when your endpoint requires authentication
export FC_API_KEY="your-api-key"

# optional: override default FastContext parameters
export FC_MAX_TOKENS=4096
export FC_TEMPERATURE=0.7
```

Benchmark runners may also pass separate FastContext credentials through `FASTCONTEXT_*` variables in
`benchmark/evaluation/configs/example.env`.

## Quick Start

### Local Ollama endpoint

The easiest local setup on macOS is to run an OpenAI-compatible endpoint with
[Ollama](https://ollama.com/). Install Ollama, start the service, and pull a quantized FastContext model:

```bas