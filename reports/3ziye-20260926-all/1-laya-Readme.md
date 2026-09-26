<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/NandhaKishorM/laya/main/assets/logo-lockup-dark.png" />
    <img src="https://raw.githubusercontent.com/NandhaKishorM/laya/main/assets/logo-lockup.png" alt="Laya" width="330" />
  </picture>
</p>

**Multilingual, non-autoregressive System 1 decision engine.** Typed decisions over 100+ languages in a single forward pass — 33 ms — trained with reinforcement learning against strictly proper scoring rules (RLCD), with a router that picks the right checkpoint per request.

<div align="center">

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/15d4Yv__KHeHjshVb-6PRTfqVllxih2S3?usp=sharing)
[![PyPI version](https://img.shields.io/pypi/v/laya.svg)](https://pypi.org/project/laya/)
[![Docs](https://img.shields.io/badge/docs-online-2ea44f)](https://nandhakishorm.github.io/laya/)
[![Hugging Face Model](https://img.shields.io/badge/%F0%9F%A4%97%20Model-convaiinnovations%2Flaya-blue)](https://huggingface.co/convaiinnovations/laya)
[![Multilingual](https://img.shields.io/badge/%F0%9F%A4%97%20Model-laya--multilingual-blue)](https://huggingface.co/convaiinnovations/laya-multilingual)
[![Hugging Face Space](https://img.shields.io/badge/%F0%9F%A4%97%20Space-laya--demo-orange)](https://huggingface.co/spaces/convaiinnovations/laya-demo)
[![Dev.to Article](https://img.shields.io/badge/dev.to-Read%20Article-0A0A0A?logo=devdotto&logoColor=white)](https://dev.to/nandakishor_m_6cc0adfde9f/i-built-non-autoregressive-decision-models-a-year-ago-then-a-frontier-lab-called-it-a-18me)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-nandakishorm-FFDD00?logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/nandakishorm)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)

</div>

## Installation

```bash
python -m pip install laya
```

Python 3.10 or newer. Optional extras: `laya[serve]` (HTTP server), `laya[mcp]` (MCP server), `laya[langchain]` (LangChain and LangGraph), `laya[onnx]` (ONNX Runtime), `laya[fast]` (TileLang GPU fast path). Step-by-step setup for each platform, CPU-only or GPU PyTorch builds, and troubleshooting are in [Installation details](#installation-details).

**Long documents.** `laya-multilingual` reads up to 8,192 tokens with `max_len=8192`. Measured accuracy and time by document length, reproducible with [`research/scripts/bench_long_context.py`](https://github.com/NandhaKishorM/laya/blob/main/research/scripts/bench_long_context.py):

<p align="center">
  <img src="https://raw.githubusercontent.com/NandhaKishorM/laya/main/assets/long_context_8192.png" alt="laya-multilingual with max_len=8192: 16 to 18 of 20 requests correct with up to about 4,000 tokens of text before them, more variable beyond" width="100%" />
</p>

## Quickstart

> **Long documents: `laya-multilingual` reads up to 8,192 tokens.** It ships with a 1,024-token limit that cuts long documents off, so pass `max_len=8192` for them:
>
> ```python
> result = router.predict(long_document, questions, model="multilingual", max_len=8192)
> ```
>
> In the table above, 16 to 18 of 20 requests were answered correctly with up to about 4,000 tokens of text before them; beyond that results vary (8 to 17 of 20), so check long-document accuracy on your own data. Short inputs give identical answers with `max_len=8192`, and speed follows the input's real length, not the limit: short inputs are unchanged, and a 4,000-token input takes about 1.7 s on an Apple GPU. Name the checkpoint with `model="multilingual"`, since long mostly-English text would otherwise route to the English checkpoint.

```python
from laya import Router

router = Router()  # downloads a checkpoint on first use; Router(preload=True) loads all three up front

state = "Hi, we were billed twice for March. Please refund the duplicate today or we will cancel our plan."
questions = {
    "department": {"type": "choice", "instructions": "Which department should handle this?",
                   "criteria": {"billing": "invoices, payments, refunds",
                                "technical": "bugs, outages, system errors",
                                "other": "everything else"}},
    "urgency": {"type": "score", "instructions": "How urgent is this?",
                "criteria": ["not urgent", "soon", "blocking"]},
    "churn_risk": {"type": "noul", "instructions": "Does the user threaten to cancel or leave?"},
}

result = router.predict(state, questions)
print(result["answers"]["department"]["choice"])  # billing
print(result["answers"]["churn_risk"]["noul"])    # probability the answer is yes
print(result["routing"]["model"])                 # english
```

The same call works in any of 100+ languages. The `Router` detects the script and language and sends non-English text to `laya-multilingual`:

```python
for text