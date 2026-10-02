<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="site/public/static/logo-white.svg">
    <img src="site/public/static/logo.svg" alt="" width="88">
  </picture>
</p>

<h1 align="center">ollaya</h1>

<p align="center"><strong>Run open decision models locally, the way Ollama runs LLMs.</strong></p>

<p align="center">
  <a href="https://ollaya.dev">Website</a> ·
  <a href="https://ollaya.dev/search">Models</a> ·
  <a href="https://ollaya.dev/results">Results</a> ·
  <a href="https://ollaya.dev/docs">Docs</a> ·
  <a href="https://github.com/ollaya-dev/ollaya/releases">Releases</a> ·
  <a href="https://huggingface.co/ollaya-dev">Hugging Face</a>
</p>

<p align="center">Created and maintained by <a href="https://github.com/cobanov">Mert Cobanov</a> (<a href="https://x.com/mertcobanov">@mertcobanov</a>).</p>

A decision model reads a *state* (a message, an email, a ticket, any JSON) plus typed questions
(`choice`, `score`, `noul`) and returns calibrated probabilities in a single forward pass, in
milliseconds. It never generates text. Ollaya pulls these models by name, serves them from a
local daemon, and speaks TypeSafe's `/v1/systemone` wire format, so existing Jev clients work by
changing one environment variable.

```sh
curl -fsSL https://ollaya.dev/install.sh | sh
ollaya run winnow:e4b --preset triage "Third time this year you've double-charged me. Refund it today or I'm cancelling and moving to a competitor."
```

```
intent            refund                                ███████████████░ 0.91
is_urgent         yes                                   ███████████████░ 0.92
frustration       2.89 / 3  very angry or using stron…  ██████████████░░ 0.86
refund_requested  yes                                   ████████████████ 0.99
churn_risk        yes                                   ████████████████ 0.99
```

`winnow:e4b` is the recommended model: 0.722 accuracy on typed decisions (TypeSafe's Jev: 0.738)
and 89 ms for these five questions on an RTX 4090. It is a 4B-class language model, so without an
NVIDIA GPU start with `laya`, which answers in a fraction of a second on a CPU. All models and their
numbers: [ollaya.dev/search](https://ollaya.dev/search).

## Features

- **One binary.** `ollaya serve` runs the daemon; `ollaya run`, `pull`, `list`, `ps`, `show`, `rm`,
  `cp`, `stop` and `create` work the way they do in Ollama. If the daemon isn't running, the CLI
  starts it.
- **TypeSafe-compatible.** `POST /v1/systemone`, `/v1/decisions` and `GET /v1/models` are
  wire-identical to TypeSafe. The official SDK works unchanged when you set
  `TYPESAFE_BASE_URL=http://localhost:11435`.
- **Native API.** `/api/decide` adds routing information and timings. `/api/pull` streams
  NDJSON progress, and there are `/api/tags`, `/api/show`, `/api/ps` and more. See
  [docs/api.md](docs/api.md).
- **Weights come from their authors.** Ollaya publishes only small ONNX graphs, about 3 MB each.
  These graphs read the original weight files (usually `model.safetensors`) from the author's
  Hugging Face repository, pinned to a commit and verified by sha256. Models whose authors publish
  GGUF files (`winnow`, `jevk5`, `jeb`) run that file itself on llama.cpp. Ollaya never re-hosts weights.
- **For agents.** `ollaya mcp` serves the models to Claude Code, Claude Desktop, Cursor and other
  MCP clients (`claude mcp add ollaya -- ollaya mcp`), and the
  [`ollaya-decisions` skill](skills/ollaya-decisions/SKILL.md) teaches agents when and how to use
  them (`npx skills add ollaya-dev/ollaya --skill ollaya-decisions`).
- **Routers.** `laya` detects the script and language of each request, then answers with
  `laya:en` or `laya:multilingual`.
- **Modelfiles.** You can bake a question set into your own model:
  ```
  FROM laya
  QUESTIONS ./triage.json
  PARAMETER precision fp32
  ```
  Then run `ollaya create triage -f Modelfile` and `ollaya run triage "…"`.
- **Fast and exact.**
  - **Hardware:** ONNX Runtime on CPU, and CUDA on NVIDIA GPUs. GGUF models run on llama.cpp:
    CPU, CUDA, and Metal on Apple silicon.
  - **Precision:** fp16 on GPU and fp32 on CPU, chosen when the model loads.
  - **Accuracy:** fp32 exports give the same decision as the PyTorch reference on 100% of 2,383
    questions per checkpoint.

## Models

| Model | What it is |
|---|---|
| `winnow:e4b` | **Recommended.** EldanRing's Winnow-E4B, a Gemma 4 fine-tune run from the author's Q8_0 GGUF on llama.cpp: 0.722 on typed-decisions (Jev: 0.738), 89 ms for five questions on an RTX 4090 |
| `laya` | Router: picks `laya:en` or `laya:multilingual` by language |
| `laya:en` | English decision model (ModernBERT-large, 421M). The fastest: 8–10 ms for five questions on an RTX 4090 |
| `laya:multilingual` | 100+ languages (mmBERT-base, 322M) |
| `laya:typed-decisions` | Fine-tuned on the typed-decisions workflows |
| `decider`, `decider:4b`, `decider:0.8b` | Mapika's Qwen3.5 decoders, 2B (the default), 4B and 0.8B: 0.680 on typed-decisions