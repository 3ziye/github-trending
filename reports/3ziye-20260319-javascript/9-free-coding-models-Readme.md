<p align="center">
  <img src="https://img.shields.io/npm/v/free-coding-models?color=76b900&label=npm&logo=npm" alt="npm version">
  <img src="https://img.shields.io/node/v/free-coding-models?color=76b900&logo=node.js" alt="node version">
  <img src="https://img.shields.io/npm/l/free-coding-models?color=76b900" alt="license">
  <img src="https://img.shields.io/badge/models-160-76b900?logo=nvidia" alt="models count">
  <img src="https://img.shields.io/badge/providers-20-blue" alt="providers count">
</p>

<h1 align="center">free-coding-models</h1>

<p align="center">
  <strong>Find the fastest free coding model in seconds</strong><br>
  <sub>Ping 160 models across 20 AI Free providers in real-time </sub><br><sub> Install Free API endpoints to your favorite AI coding tool: <br>OpenCode, OpenClaw, Crush, Goose, Aider, Qwen Code, OpenHands, Amp or Pi in one keystroke</sub>
</p>



<p align="center">

```bash
npm install -g free-coding-models
free-coding-models
```

create a free account on one of the [providers](#-list-of-free-ai-providers)

</p>

<p align="center">
  <a href="#-why-this-tool">Why</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-list-of-free-ai-providers">Providers</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-tui-keys">TUI Keys</a> •
  <a href="#-contributing">Contributing</a>
</p>

<p align="center">
  <img src="demo.gif" alt="free-coding-models demo" width="100%">
</p>

<p align="center">
  <sub>Made with ❤️ and ☕ by <a href="https://vanessadepraute.dev">Vanessa Depraute</a> (aka <a href="https://vavanessa.dev">Vava-Nessa</a>)</sub>
</p>

---

## 💡 Why this tool?

There are **160+ free coding models** scattered across 20 providers. Which one is fastest right now? Which one is actually stable versus just lucky on the last ping?

This CLI pings them all in parallel, shows live latency, and calculates a **live Stability Score (0-100)**. Average latency alone is misleading if a model randomly spikes to 6 seconds; the stability score measures true reliability by combining **p95 latency** (30%), **jitter/variance** (30%), **spike rate** (20%), and **uptime** (20%). 

It then writes the model you pick directly into your coding tool's config — so you go from "which model?" to "coding" in under 10 seconds.

---

## ⚡ Quick Start

### 🟢 List of Free AI Providers

Create a free account on one provider below to get started:

**160 coding models** across 20 providers, ranked by [SWE-bench Verified](https://www.swebench.com).

| Provider | Models | Tier range | Free tier | Env var |
|----------|--------|-----------|-----------|--------|
| [NVIDIA NIM](https://build.nvidia.com) | 44 | S+ → C | 40 req/min (no credit card needed) | `NVIDIA_API_KEY` |
| [iFlow](https://platform.iflow.cn) | 11 | S+ → A+ | Free for individuals (no req limits, 7-day key expiry) | `IFLOW_API_KEY` |
| [ZAI](https://z.ai) | 7 | S+ → S | Free tier (generous quota) | `ZAI_API_KEY` |
| [Alibaba DashScope](https://modelstudio.console.alibabacloud.com) | 8 | S+ → A | 1M free tokens per model (Singapore region, 90 days) | `DASHSCOPE_API_KEY` |
| [Groq](https://console.groq.com/keys) | 10 | S → B | 30‑50 RPM per model (varies by model) | `GROQ_API_KEY` |
| [Cerebras](https://cloud.cerebras.ai) | 7 | S+ → B | Generous free tier (developer tier 10× higher limits) | `CEREBRAS_API_KEY` |
| [SambaNova](https://sambanova.ai/developers) | 12 | S+ → B | Dev tier generous quota | `SAMBANOVA_API_KEY` |
| [OpenRouter](https://openrouter.ai/keys) | 11 | S+ → C | Free on :free: 50/day <$10, 1000/day ≥$10 (20 req/min) | `OPENROUTER_API_KEY` |
| [Hugging Face](https://huggingface.co/settings/tokens) | 2 | S → B | Free monthly credits (~$0.10) | `HUGGINGFACE_API_KEY` |
| [Together AI](https://api.together.ai/settings/api-keys) | 7 | S+ → A- | Credits/promos vary by account (check console) | `TOGETHER_API_KEY` |
| [DeepInfra](https://deepinfra.com/login) | 2 | A- → B+ | 200 concurrent requests (default) | `DEEPINFRA_API_KEY` |
| [Fireworks AI](https://fireworks.ai) | 2 | S | $1 credits – 10 req/min without payment | `FIREWORKS_API_KEY` |
| [Mistral Codestral](https://codestral.mistral.ai) | 1 | B+ | 30 req/min, 2000/day | `CODESTRAL_API_KEY` |
| [Hyperbolic](https://app.hyperbolic.ai/settings) | 10 | S+ → A- | $1 free trial credits | `HYPERBOLIC_API_KEY` |
| [Scaleway](https://console.scaleway.com/iam/api-keys) | 7 | S+ → B+ | 1M free tokens | `SCALEWAY_API_KEY` |
| [Google AI Studio](https://aistudio.google.com/apikey) | 3 | B → C | 14.4K req/day, 30/min | `GOOGLE_API_KEY` |
| [SiliconFlow](https://cloud.siliconflow.cn/account/ak) | 6 | S+ → A | Free models: usually 100 RPM, varies by model | `SILICONFLOW_API_KEY` |
| [Cloudflare Workers AI](https://dash.cloudflare.com) | 6 | S → B | Free: 10k neurons/day, text-gen 300 RPM | `CLOUDFLARE_API_TOKEN` + `CLOUDFLARE_ACCOUNT_ID` |
| [Perplexity API](https://www.perplexity.ai/settings/api) | 4 | A+ → B | Tiered limits by spend (default ~50 RPM) | `PERPLEXITY_API_KEY` |
| [Replicate](https://re