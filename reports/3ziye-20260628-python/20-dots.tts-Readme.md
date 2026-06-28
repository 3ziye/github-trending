<p align="center">
  <img src="assets/logo.png" alt="dots.tts" width="280">
</p>

<p align="center">
  <a href="https://github.com/rednote-hilab/dots.tts"><img src="https://img.shields.io/badge/GitHub-rednote--hilab%2Fdots.tts-blue?logo=github" alt="GitHub"></a>
  <a href="https://huggingface.co/collections/rednote-hilab/dotstts"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-dots.tts%20collection-yellow" alt="Hugging Face"></a>
  <a href="https://arxiv.org/abs/2606.07080"><img src="https://img.shields.io/badge/arXiv-Report-b31b1b?logo=arxiv&logoColor=white" alt="arXiv"></a>
  <a href="https://huggingface.co/spaces/rednote-hilab/dots.tts"><img src="https://img.shields.io/badge/Playground-Live-orange" alt="Playground"></a>
  <a href="https://rednote-hilab.github.io/dots.tts-demo/"><img src="https://img.shields.io/badge/Demo%20Page-Live-red" alt="Demo Page"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-green" alt="License"></a>
</p>

**dots.tts** is a **2B-parameter fully continuous, end-to-end autoregressive (AR) text-to-speech system**. The backbone pairs a semantic encoder, an LLM, and an autoregressive flow-matching acoustic head over a **48 kHz** AudioVAE, with no discrete tokens anywhere in the pipeline.

dots.tts achieves the best average performance on **Seed-TTS-Eval**, with WERs of **0.94% / 1.30% / 6.60%** and SIM scores of **81.0 / 77.1 / 79.5** on the zh / en / zh-hard test sets, respectively. It further attains the **highest average speaker similarity (83.9)** on the 24-language **MiniMax multilingual** benchmark. Across other benchmarks, dots.tts also consistently demonstrates **open-source state-of-the-art performance**, exhibiting strong generation stability, voice cloning ability, and emotional expressiveness.

### News

* **[2026.06]** 🔥 We have released **dots.tts** — 2B fully continuous AR TTS, with pretrained / self-corrective-aligned / MeanFlow-distilled checkpoints and full inference & fine-tuning code under Apache-2.0.

---

## Contents

- [Quick Start](#-quick-start)
  - [Installation](#installation)
  - [Checkpoints](#checkpoints)
  - [CLI](#cli)
  - [Python API](#python-api)
  - [Web Demo (Gradio)](#web-demo-gradio)
  - [Fine-tuning](#fine-tuning)
  - [MeanFlow Distillation](#meanflow-distillation)
- [Usage Tips](#-usage-tips)
- [Architecture](#-architecture)
- [Performance](#-performance)
  - [Seed-TTS-Eval](#seed-tts-eval)
  - [MiniMax Multilingual](#minimax-multilingual-24-languages)
  - [CV3-Eval](#cv3-eval)
  - [EmergentTTS-Eval](#emergenttts-eval)
- [Community Projects](#-community-projects)
- [Risks and Limitations](#%EF%B8%8F-risks-and-limitations)
- [Citation](#-citation)
- [License](#-license)

---

## 🚀 Quick Start

### Installation

We recommend creating a fresh conda environment first (Python 3.10–3.12):

```bash
conda create -n dots_tts python=3.10 -y
conda activate dots_tts
```

Then install from source:

```bash
python -m pip install --upgrade pip
python -m pip install -e . -c constraints/recommended.txt
```

For training / linting extras:

```bash
python -m pip install -e .[full] -c constraints/recommended.txt
```

The constraints file pins the recommended versions. To use other compatible
versions, omit `-c constraints/recommended.txt`; the compatibility ranges are
declared in `pyproject.toml`.

### Checkpoints

Three pretrained checkpoints are released on Hugging Face. All three share the same backbone — choose by the quality / inference-cost tradeoff:

| Model | Description | Recommended `--num-steps` |
|---|---|:---:|
| [`rednote-hilab/dots.tts-base`](https://huggingface.co/rednote-hilab/dots.tts-base) | Pretrained checkpoint. | `10`–`32` (default `10`) |
| [`rednote-hilab/dots.tts-soar`](https://huggingface.co/rednote-hilab/dots.tts-soar) | Self-corrective-aligned (SCA) checkpoint on top of `dots.tts-base`. Best voice cloning performance. | `10`–`32` (default `10`) |
| [`rednote-hilab/dots.tts-mf`](https://huggingface.co/rednote-hilab/dots.tts-mf) | MeanFlow-distilled student from `dots.tts-soar`. Recommended if you care about inference speed. | `4` |

Pass the repo id directly to `--model-name-or-path` (or `DotsTtsRuntime.from_pretrained`) — the snapshot is fetched on first use and cached locally.

### CLI

The package installs a `dots.tts` entry point:

```bash
# Continuation voice cloning (reference audio + transcript) — recommended, best SIM
dots.tts \
  --model-name-or-path rednote-hilab/dots.tts-soar \
  --text "Hello, this is a zero-shot voice cloning demonstration." \
  --prompt-audio /path/to/reference.wav \
  --prompt-text "The exact transcript of the reference audio." \
  --num-steps 10 \
  --output clone.wav

# X-vector-only voice cloning (reference audio only — timbre from speaker x-vector)
dots.tts \
  --model-name-or-path rednote-hilab/dots.tts-soar \
  --text "Hello, this is a zero-shot voice cloning demonstration." \
  --prompt-audio /path/to/reference.wav \
  --num-steps 10 \
  --ou