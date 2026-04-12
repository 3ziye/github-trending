<div align="center">

<img src="assets/osai.png" alt="Awesome Open Source AI" width="120" />

# Awesome Open Source AI

*A curated list of **battle-tested, production-proven** open-source AI models, libraries, infrastructure, and developer tools. Only elite-tier projects make this list.*

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](./CONTRIBUTING.md)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-blue.svg?style=flat-square)](./LICENSE)

<sub>by **Boring Dystopia Development**</sub>

<p align="center">
  <a href="https://boringdystopia.ai/">
    <img src="https://img.shields.io/badge/boringdystopia.ai-111111?style=for-the-badge&logo=vercel&logoColor=white" alt="boringdystopia.ai" />
  </a>&nbsp;
  <a href="https://x.com/alvinunreal">
    <img src="https://img.shields.io/badge/X-@alvinunreal-000000?style=for-the-badge&logo=x&logoColor=white" alt="X @alvinunreal" />
  </a>&nbsp;
  <a href="https://t.me/boringdystopiadevelopment">
    <img src="https://img.shields.io/badge/Telegram-Join%20channel-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Join channel" />
  </a>
</p>

</div>

---
<div align="center">

**[ 🌱 Emerging ](./EMERGING.md)** • **[ Explore the List ](#-contents)** • **[ Submission Guidelines ](#contributing)** • **[ License ](#license)**

</div>

## 📋 Contents

- [🧬 1. Core Frameworks & Libraries](#-1-core-frameworks--libraries)
- [🧠 2. Open Foundation Models](#-2-open-foundation-models)
- [⚡ 3. Inference Engines & Serving](#-3-inference-engines--serving)
- [🤖 4. Agentic AI & Multi-Agent Systems](#-4-agentic-ai--multi-agent-systems)
- [🔍 5. Retrieval-Augmented Generation (RAG) & Knowledge](#-5-retrieval-augmented-generation-rag--knowledge)
- [🎨 6. Generative Media Tools](#-6-generative-media-tools)
- [🛠️ 7. Training & Fine-tuning Ecosystem](#section-7)
- [📊 8. MLOps / LLMOps & Production](#-8-mlops--llmops--production)
- [📈 9. Evaluation, Benchmarks & Datasets](#-9-evaluation-benchmarks--datasets)
- [🛡️ 10. AI Safety, Alignment & Interpretability](#section-10)
- [🧩 11. Specialized Domains](#-11-specialized-domains)
- [🖥️ 12. User Interfaces & Self-hosted Platforms](#section-12)
- [🧪 13. Developer Tools & Integrations](#-13-developer-tools--integrations)
- [📚 14. Resources & Learning](#-14-resources--learning)

---

### 🧬 1. Core Frameworks & Libraries

> Core libraries and frameworks used to build, train, and run AI and machine learning systems.

#### Deep Learning Frameworks

- **[PyTorch](https://github.com/pytorch/pytorch)** ![GitHub stars](https://img.shields.io/github/stars/pytorch/pytorch?style=social) - Dynamic computation graphs, Pythonic API, dominant in research and production. The current standard for most frontier AI work.
- **[TensorFlow](https://github.com/tensorflow/tensorflow)** ![GitHub stars](https://img.shields.io/github/stars/tensorflow/tensorflow?style=social) - End-to-end platform with excellent production deployment, TPU support, and large-scale serving tools.
- **[JAX](https://github.com/jax-ml/jax)** ![GitHub stars](https://img.shields.io/github/stars/jax-ml/jax?style=social) + **[Flax](https://github.com/google/flax)** ![GitHub stars](https://img.shields.io/github/stars/google/flax?style=social) - High-performance numerical computing with composable transformations (JIT, vmap, grad). Rising favorite for research and scientific ML.
- **[NumPyro](https://github.com/pyro-ppl/numpyro)** ![GitHub stars](https://img.shields.io/github/stars/pyro-ppl/numpyro?style=social) - Probabilistic programming with NumPy powered by JAX for autograd and JIT compilation. Bayesian modeling and inference at scale.
- **[Keras](https://github.com/keras-team/keras)** ![GitHub stars](https://img.shields.io/github/stars/keras-team/keras?style=social) - High-level, beginner-friendly API that now runs on multiple backends (TensorFlow, JAX, PyTorch). Perfect for rapid experimentation.
- **[tinygrad](https://github.com/tinygrad/tinygrad)** ![GitHub stars](https://img.shields.io/github/stars/tinygrad/tinygrad?style=social) - Minimalist deep learning framework with tiny code footprint. The "you like pytorch? you like micrograd? you love tinygrad!" philosophy - simple yet powerful.
- **[PaddlePaddle](https://github.com/PaddlePaddle/Paddle)** ![GitHub stars](https://img.shields.io/github/stars/PaddlePaddle/Paddle?style=social) - Industrial deep learning platform from Baidu serving 23+ million developers and 760,000+ companies. China's first independent R&D framework with advanced distributed training and deployment capabilities.
- **[PyTorch Geometric](https://github.com/pyg-team/pytorch_geometric)** ![GitHub stars](https://img.shields.io/github/stars/pyg-team/pytorch_geometric?style=social) - Library for deep learning on irregular input data such as graphs, point clouds, and manifolds. Part of the PyTorch ecosystem.

#### Rust ML Frameworks

- **[Burn](