<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/reef-logo-dark.svg">
  <img src="docs/assets/reef-logo-light.svg" alt="Reef" width="220">
</picture>

<h3>Continual learning infra for self-improving agents</h3>

[![CI](https://github.com/Human-Agent-Society/reef/actions/workflows/ci.yml/badge.svg)](https://github.com/Human-Agent-Society/reef/actions/workflows/ci.yml)
[![PyPI package: reef-infra](https://img.shields.io/pypi/v/reef-infra?label=PyPI%3A%20reef-infra&logo=pypi&logoColor=white)](https://pypi.org/project/reef-infra/)
[![Python](https://img.shields.io/badge/python-3.12%2B-3776AB?logo=python&logoColor=white)](pyproject.toml)
[![License](https://img.shields.io/badge/license-Apache--2.0-green)](LICENSE)

English | [中文](README.zh.md)

<div align="left">

Reef is the first open-source infrastructure for continual self-improving agents.
It connects agent inference, feedback, learning, and versioned delivery. Use it
to train model weights with Slime and SGLang, or improve an agent's harness, including its prompts, rules, and skills.


</div>

**🚀 [Get started](https://reefinfra.ai/docs/getting-started/quickstart/) |
🗺️ [Roadmap](https://github.com/Human-Agent-Society/reef/issues/25) |
📣 [Launch post](https://x.com/ao_qu18465/status/2094867930081337730) |
💬 [Join Discord](https://discord.gg/5y8e5f937k) |
📱 [Join WeChat Group](docs/community/wechat.md)**

</div>


## 🎯 When to use Reef

Use Reef when you want your agent to keep improving simply by learning from how you interact with your agent.

| Your goal | Learning path | What you need |
|---|---|---|
| Keep getting stronger model designed for you | Model weight training | A trainable model, a supported GPU stack, and feedback your recipe can use |
| Get your harness to self-improve | Harness optimization | A model endpoint, representative tasks, and an evaluator; no local training GPUs |
| Scientific discoveries | Test-time training | An execution environment, a correctness checker, and a measurable objective |


## 🧩 How Reef fits your stack

| Ability | Inference engine (vLLM, SGLang, …) | RL training framework (Slime, veRL, AReaL, …) | **Reef** |
|---|:---:|:---:|:---:|
| Serves live traffic | ✅ | ❌ | ✅ |
| Trains weights | ❌ | ✅ | ✅ |
| Version management | ❌ | ❌ | ✅ |
| Stays live through updates | ❌ | ❌ | ✅ |
| Evolves beyond weights (skills, harness) | ❌ | ❌ | ✅ |


## 🔄 How it works

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/loop-animation-dark.svg">
  <img src="docs/assets/loop-animation-light.svg" alt="Reef serves requests, records feedback, produces updates, and commits accepted updates to a version history." width="76%">
</picture>
</div>

Reef processes each learning cycle in four steps. The table also shows which
modules implement each step.

| Step | What happens | Where it lives |
|---|---|---|
| **1&nbsp;·&nbsp;Serve** | Serve agent requests and record interactions. | [`service/`](reef/service) — agent requests and interaction records<br>[`runtime/`](reef/runtime) — inference and artifact updates |
| **2&nbsp;·&nbsp;Observe** | Match feedback to recorded interactions. | [`storage/records.py`](reef/storage/records.py) — stored interactions and feedback<br>[`train/processors/`](reef/train/processors) — feedback matching and eligibility |
| **3&nbsp;·&nbsp;Grow** | Produce an update from eligible records. | [`recipe/`](reef/recipe) — recipe integration<br>[`train/`](reef/train) — batches and update jobs |
| **4&nbsp;·&nbsp;Commit** | Apply the configured selection policy and publish accepted updates. | [`train/evaluation/`](reef/train/evaluation) — candidate evaluation<br>[`artifact/`](reef/artifact) — version history<br>[`surface/`](reef/surface) — artifact delivery |


## 📦 Installation

> 💡 **Note**
>
> Reef's artifact and checkpoint functionality requires the `git-lfs` system
> package. Reef initializes Git LFS locally for its artifact repositories.

We recommend [uv](https://docs.astral.sh/uv/) for managing packages, and the
commands below use it.

### From PyPI

```bash
uv venv && source .venv/bin/activate
uv pip install reef-infra
python3 -c "import reef; print(reef.__version__)"
```

### From source

```bash
git lfs install
git clone https://github.com/Human-Agent-Society/reef.git
cd reef
uv venv && source .venv/bin/activate
uv pip install -e .
python3 -c "import reef; print(reef.__version__)"
```

Use the source checkout for development and for the training examples below.


## 🔧 Using Reef

Reef supports two learning surfaces: model **weights** and agent **harnesses**.
The deployment's recipe determines which surface its scenarios update.

As a minimal example, start Reef as a pure inference server:

```bash
uv run reef serve --inference.model-path Qwen/Qwen2.5-1.5B-Instruct
```

### Weight-training deployment

#### Start the deployment

The following example starts the SAO (arXiv:2607.07508) example deployment. Run it
from a