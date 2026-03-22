<div align="center">
  <h1 align="center">
    <img src="assets/spacer.png" alt="" width="23" height="40" align="absmiddle" />
    OpenClaw-RL<!--
--><sup>
    <img src="assets/clawistool.png" alt="Claw-RL logo" width="23" height="40" align="absmiddle" />
    <sup>
  </h1>

  <p><b>Empowering OpenClaw with RL — Train a personalized agent simply by talking to it.</b></p>
  <p><b>Scalable RL in real-world settings — Agentic RL for terminal, GUI, SWE, and tool-call settings.</b></p>
</div>


<p align="center">
  <img src="https://img.shields.io/badge/⚡_Fully_Async-yellow?style=for-the-badge" alt="Fully Async" />
  <img src="https://img.shields.io/badge/💰_Zero_API_or_Zero_GPU-blue?style=for-the-badge" alt="Zero API or Zero GPU" />
  <img src="https://img.shields.io/badge/🤖_Personalized-success?style=for-the-badge" alt="Personalized" />
  <img src="https://img.shields.io/badge/🛠️_Auto_Optimization-orange?style=for-the-badge" alt="Auto" />
  <img src="https://img.shields.io/badge/💬_Language_Feedback-purple?style=for-the-badge" alt="Language Feedback" />
  <img src="https://img.shields.io/badge/🧠_Hybrid_RL-red?style=for-the-badge" alt="Hybrid RL" />
  <img src="https://img.shields.io/badge/🌍_Real_World_Agentic_RL-green?style=for-the-badge" alt="General Agentic RL" />
  <br><br>
  <a href="https://arxiv.org/abs/2603.10165"><img src="https://img.shields.io/badge/📄_Tech_Report-red?style=flat-square" alt="Tech Report" /></a>
  <a href="https://yinjjiew.github.io/projects/openclawrl1"><img src="https://img.shields.io/badge/Blog-Page-blue?style=flat-square" alt="OpenClaw-RL Blog" /></a>
  <a href="https://openclaw.ai"><img src="https://img.shields.io/badge/OpenClaw-Plugin-orange?style=flat-square" alt="OpenClaw Plugin" /></a>
  <a href="https://github.com/THUDM/slime"><img src="https://img.shields.io/badge/Slime-Supported-purple?style=flat-square" alt="Slime Based" /></a>
  <a href="https://thinkingmachines.ai/tinker/"><img src="https://img.shields.io/badge/Tinker-Supported-yellow?style=flat-square" alt="Tinker Supported" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-green?style=flat-square" alt="License Apache 2.0" /></a>
</p>

<p align="center">
  <video src="https://github.com/user-attachments/assets/a58aacad-3c1d-47aa-bbd1-cf8c5f36de6f" controls width="200"></video>
</p>









## 📰 News

- **[2026/3/20]** 🔥 You can use your own openclaw now, simply install [this extension](https://github.com/Gen-Verse/OpenClaw-RL/tree/main/extensions/rl-training-headers).
- **[2026/3/13]** 🚀 OpenClaw-RL now supports both local GPU and cloud ([Tinker](https://thinkingmachines.ai/tinker/)) deployment. Launch with [**one line of code**](#combinemethod) — Hybrid RL, OPD, and Binary RL all supported!
- **[2026/3/12]** 🔥 We support LoRA training now!
- **[2026/3/10]** 🔥 We have released our [**Technical Report**](https://arxiv.org/abs/2603.10165)! 🏆 Ranked **#1** on [HuggingFace Daily Papers](https://huggingface.co/papers/2603.10165)!
- **[2026/3/10]** 🔥 Huge updates today! We released a [new combination method](./openclaw-combine), along with an [interesting evaluation](./openclaw-test) of these OpenClaw-RL methods. Track 2 is released too, featuring scalable RL implementations for general agent settings across [terminal](./terminal-rl), [GUI](./gui-rl), [SWE](./swe-rl), and [tool-call](./toolcall-rl) scenarios. We only focus on real-world settings!
- **[2026/3/3]** 🙌 Working with the authors of [SDFT](https://arxiv.org/abs/2601.19897) and [SDPO](https://arxiv.org/abs/2601.20802), we have integrated their methods into [openclaw-opd](./openclaw-opd). We welcome the integration of novel and effective methods!
- **[2026/3/3]** 📺 Check out these community tutorial videos on OpenClaw-RL: [Video 1](https://www.youtube.com/watch?v=5xnm1vB7G64) | [Video 2](https://www.youtube.com/watch?v=ZtN6Gg_bdJE)
- **[2026/2/26]** 🔥 We release **OpenClaw-RL v1** — a fully asynchronous RL framework for training personalized AI agents from natural conversation feedback. 

---

## 💡 TL;DR

> **OpenClaw-RL** is a fully asynchronous reinforcement learning framework that turns everyday conversations into training signals for personalized AI agents, and supports training general agents with large-scale environment parallelization.

Most RL-for-LLM systems assume centralized, batch-mode training with pre-collected datasets. **OpenClaw-RL** takes a fundamentally different approach: it wraps your self-hosted model in [OpenClaw](https://openclaw.ai) as an OpenAI-compatible API, intercepts live multi-turn conversations, and continuously optimizes the policy in the background — all without interrupting your usage.


<p align="center">
  <img src="assets/framework.png"  alt="Overview"  width="600">
</p>



> **Highlights:** Fully async 4-component loop · Self-hosted & private · Zero manual labeling · Three learning paradigms (Binary RL / OPD / Combine) · Personal + General agent support

<details>
<summary><b>🌈 Features</b></summa