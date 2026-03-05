<p align="center">
  <img src="https://img.shields.io/npm/v/free-coding-models?color=76b900&label=npm&logo=npm" alt="npm version">
  <img src="https://img.shields.io/node/v/free-coding-models?color=76b900&logo=node.js" alt="node version">
  <img src="https://img.shields.io/npm/l/free-coding-models?color=76b900" alt="license">
  <img src="https://img.shields.io/badge/models-158-76b900?logo=nvidia" alt="models count">
  <img src="https://img.shields.io/badge/providers-20-blue" alt="providers count">
</p>

<h1 align="center">free-coding-models</h1>

<p align="center">
  <strong>Contributors</strong><br>
  <a href="https://github.com/vava-nessa"><img src="https://avatars.githubusercontent.com/u/5466264?v=4&s=60" width="60" height="60" style="border-radius:50%" alt="vava-nessa"></a>
  <a href="https://github.com/erwinh22"><img src="https://avatars.githubusercontent.com/u/6641858?v=4&s=60" width="60" height="60" style="border-radius:50%" alt="erwinh22"></a>
  <a href="https://github.com/whit3rabbit"><img src="https://avatars.githubusercontent.com/u/12357518?v=4&s=60" width="60" height="60" style="border-radius:50%" alt="whit3rabbit"></a>
  <a href="https://github.com/skylaweber"><img src="https://avatars.githubusercontent.com/u/172871734?v=4&s=60" width="60" height="60" style="border-radius:50%" alt="skylaweber"></a>
  <a href="https://github.com/PhucTruong-ctrl"><img src="https://github.com/PhucTruong-ctrl.png?s=60" width="60" height="60" style="border-radius:50%" alt="PhucTruong-ctrl"></a>
  <br>
  <sub>
    <a href="https://github.com/vava-nessa">vava-nessa</a> &middot;
    <a href="https://github.com/erwinh22">erwinh22</a> &middot;
    <a href="https://github.com/whit3rabbit">whit3rabbit</a> &middot;
    <a href="https://github.com/skylaweber">skylaweber</a> &middot;
    <a href="https://github.com/PhucTruong-ctrl">PhucTruong-ctrl</a>
  </sub>
</p>

<p align="center">
  💬 <a href="https://discord.gg/5MbTnDC3Md">Let's talk about the project on Discord</a>
</p>

<p align="center">

```
1. Create a free API key (NVIDIA, OpenRouter, Hugging Face, etc.)
2. npm i -g free-coding-models
3. free-coding-models
```

</p>

<p align="center">
  <strong>Find the fastest coding LLM models in seconds</strong><br>
  <sub>Ping free coding models from 20 providers in real-time — pick the best one for OpenCode, OpenClaw, or any AI coding assistant</sub>
</p>

<p align="center">
  <img src="demo.gif" alt="free-coding-models demo" width="100%">
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-requirements">Requirements</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-tui-columns">Columns</a> •
  <a href="#-stability-score">Stability</a> •
  <a href="#-coding-models">Models</a> •
  <a href="#-opencode-integration">OpenCode</a> •
  <a href="#-openclaw-integration">OpenClaw</a> •
  <a href="#-how-it-works">How it works</a>
</p>

---

## ✨ Features

- **🎯 Coding-focused** — Only LLM models optimized for code generation, not chat or vision
- **🌐 Multi-provider** — Models from NVIDIA NIM, Groq, Cerebras, SambaNova, OpenRouter, Hugging Face Inference, Replicate, DeepInfra, Fireworks AI, Codestral, Hyperbolic, Scaleway, Google AI, SiliconFlow, Together AI, Cloudflare Workers AI, Perplexity API, Alibaba Cloud (DashScope), ZAI, and iFlow
- **⚙️ Settings screen** — Press `P` to manage provider API keys, enable/disable providers, test keys live, and manually check/install updates
- **🔀 Multi-account Proxy (`fcm-proxy`)** — Automatically starts a local reverse proxy that groups all your accounts into a single provider in OpenCode; supports multi-account rotation and auto-detects usage limits to swap between providers.
- **🚀 Parallel pings** — All models tested simultaneously via native `fetch`
- **📊 Real-time animation** — Watch latency appear live in alternate screen buffer
- **🏆 Smart ranking** — Top 3 fastest models highlighted with medals 🥇🥈🥉
- **⏱ Continuous monitoring** — Pings all models every 3 seconds forever, never stops
- **📈 Rolling averages** — Avg calculated from ALL successful pings since start
- **📊 Uptime tracking** — Percentage of successful pings shown in real-time
- **📐 Stability score** — Composite 0–100 score measuring consistency (p95, jitter, spikes, uptime)
- **📊 Usage tracking** — Monitor remaining quota percentage for each model directly in the TUI; persists across sessions via `token-stats.json`.
- **📜 Live Log Viewer** — Press `X` to view real-time activity and error logs in a focused TUI overlay.
- **🛠 MODEL_NOT_FOUND Rotation** — If a specific provider returns a 404 for a model, the TUI intelligently rotates through other available providers for the same model.
- **🔄 Auto-retry** — Timeout models keep getting retried, nothing is ever "given up on"
- **🎮 Interactive selection** — Navigate with arrow keys directly in the table, press Enter to act
- **🔀 Startup mode menu** — Choose between OpenCode and OpenClaw before the TUI launches
- **💻 O