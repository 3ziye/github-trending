<p align="center">
  <img src="assets/logo.svg" alt="Atlas Inference Engine" width="640" />
</p>
<p align="center">
  <h1 align="center">Atlas Inference Engine</h1>
  <p align="center">
    <strong>Pure Rust LLM Inference</strong><br>
    <em>Universal Inference At Unimaginable Speeds</em>
  </p>
  <p align="center">
    <img alt="NVIDIA" src="https://img.shields.io/badge/NVIDIA-76B900?style=flat-square&logo=nvidia&logoColor=white">
    <img alt="AMD" src="https://img.shields.io/badge/AMD-ED1C24?style=flat-square&logo=amd&logoColor=white">
    <img alt="Intel" src="https://img.shields.io/badge/Intel-0071C5?style=flat-square&logo=intel&logoColor=white">
  </p>
  <p align="center">
    <a href="LICENSE"><img alt="License: AGPLv3" src="https://img.shields.io/badge/license-AGPLv3-yellow?style=flat-square"></a>
    <a href="#build"><img alt="Pure Rust" src="https://img.shields.io/badge/runtime-pure%20Rust-orange?style=flat-square"></a>
    <a href="https://hub.docker.com/r/avarok/atlas-gb10"><img alt="Docker Hub" src="https://img.shields.io/badge/Docker%20Hub-avarok%2Fatlas--gb10-2496ED?style=flat-square&logo=docker&logoColor=white"></a>
    <a href="https://discord.gg/DwF3brBMpw"><img alt="Discord" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fdiscord.com%2Fapi%2Fv10%2Finvites%2FDwF3brBMpw%3Fwith_counts%3Dtrue&query=%24.approximate_member_count&label=discord&suffix=%20members&style=flat-square&logo=discord&logoColor=white&color=5865F2"></a>
  </p>
</p>

<p align="center">
  <a href="assets/atlas-demo.mp4"><img alt="Atlas demo — click for full-quality MP4" src="assets/atlas-demo.gif" width="820" /></a>
</p>

<p align="center">
  <a href="#run-atlas"><img alt="Quick Start — under 2 minutes" src="https://img.shields.io/badge/%E2%9A%A1%20Quick%20Start%20%E2%80%94%20%3C%202%20min-2EA44F?style=for-the-badge&logo=docker&logoColor=white"></a>
  <a href="https://atlasinference.io"><img alt="atlasinference.io" src="https://img.shields.io/badge/%F0%9F%8C%90%20atlasinference.io-F48C06?style=for-the-badge"></a>
  <a href="https://x.com/AIshaqui81766/status/2052121270506930276"><img alt="Launch announcement on X" src="https://img.shields.io/badge/%F0%9D%95%8F%20Launch%20Announcement-000000?style=for-the-badge&logo=x&logoColor=white"></a>
</p>

## Philosophy

The foundation of any given field of science is philosophy. It is that which inspires direction, structure, and mission.

Atlas began as a solution to widely known problem in using other (python) inference engines built by data scientists: the code was steeped in a poly codebase with an ever shifting ecosystem of dependencies, patches, and cross-dependencies. One day your workaround for running a model works, the next day you have to update to a nightly branch of several dependencies and inject a new workaround. This is not how you build a software ecosystem; that's how you build a proof of concept. We thank the great and hard work data scientists made in proving LLMs can revolutionize our world, its economy, and how it challenges us to higher epochs. Now, the software engineers take the torch to turn a proof of concept into something that is designed to withstand the test of time.

### Main Objective

Similar to how llama.cpp was built with the intent to prove you don't need $10000-$100000 GPUs to run LLMs, Atlas is built with the intent to consistently force the narrative that as hardware continues to advance, we should not have to pay premium Cloud API prices for inference. Atlas, by virtue of its philosophy, maximizes speed for each hardware/model combination, thus paving the way for meaningfully powerful and intelligent LLMs to be run locally in such a way the model is truly useful.

### Design Choices

#### Free and Open Source, Always

We promised this since the beginning. We believe great software comes from opening the source, not from just keeping it closed. The more eyes, the better. And therein brings us to the next point.

#### Community-First

For those who've followed us this far since the inception of our Discord, you know the extent to which our commitment to the community is, according to one user humourously put, "cracked". We want to build something incredible, and that means we not only build for you, but you, now having access to the source code, can now build for others in ways that triumph over existing solutions. This is the only way we all win. We are the Pirates of the inference space.

#### Monorepo

We chose a monorepo design to ensure that, as we head further into the agentic age of coding, the average data scientist or engineer can contribute meaningful PRs to any part of the system. Eventually, since this is a monorepo, there will be a day where the repo is autonomously self-improving and self-patching. This is most efficient and most effective when all the code is in one place, not many.

#### Hardware+Model Specific Kernels

We make no compromises or generalizations. Each hardware and model combination has its own uniq