## Free Humanize Text: Open-source toolkit to rewrite AI-generated content into natural
<p align="center">
  <img src="presentation/banner.png" alt="Humanize-Text" width="600"/>
</p>

<p align="center">
  <a href="https://github.com/lynote-ai/humanize-text/stargazers"><img src="https://img.shields.io/github/stars/lynote-ai/humanize-text?style=social" alt="Stars"></a>
  <a href="https://github.com/lynote-ai/humanize-text/network/members"><img src="https://img.shields.io/github/forks/lynote-ai/humanize-text?style=social" alt="Forks"></a>
  <a href="https://github.com/lynote-ai/humanize-text/blob/main/LICENSE"><img src="https://img.shields.io/github/license/lynote-ai/humanize-text" alt="License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python"></a>
  <a href="https://lynote.ai"><img src="https://img.shields.io/badge/Try-Lynote.ai-brightgreen?style=for-the-badge" alt="Lynote.ai"></a>
</p>

<p align="center">
  English | <a href="README-zh.md">中文</a>
</p>

---

## What is Humanize-Text?

An AI text humanization toolkit. This repo evolved through two stages:

- **v1.0** — Documented **4 humanization methodologies** as reference implementations (translation chain, multi-turn LLM rewriting, detection-guided feedback loop, mixed-engine translation). See [docs/techniques.md](docs/techniques.md).
- **v1.5 (current)** — Added the **Standard Pipeline**: a production-grade integration of Method 1 (Translation Chain) + Method 2 (LLM Rewriting), fixed as a 5-step chain we actually run and recommend.

### v1.5.1 — Standard Pipeline (Recommended)

The Standard Pipeline preserves the original writing style while routing text through a 4-step chain: two LLM humanization rewrites (DeepSeek or [OpenRouter](https://openrouter.ai) via OpenAI-compatible API) followed by two cross-engine translation hops.

```
Input (EN) → Chinese (LLM) → Japanese (LLM) → Finnish (Google) → English (Niutrans)
```

LLM steps use **DeepSeek** (default) or **[OpenRouter](https://openrouter.ai)** — any OpenAI-compatible chat API. Configure via `[llm]` in `config.toml`. See [Configuration Guide](docs/configuration.md).

**See [`examples/showcase/`](examples/showcase/) for 5 real samples with full intermediate-step outputs and AI-detection verdicts.**

**Characteristics:**
- Best original style preservation among all approaches
- Fast processing speed
- 100% key information retention (verified on 50 text pairs)
- Expert quality score: 9.1/10

> The 4 underlying methodologies live in `src/methodologies/` as reference implementations for research and customization. The Standard Pipeline (`src/standard/pipeline.py`) is the recommended production path.

> **Want higher bypass rates + all methods combined?**
> Lynote.ai fuses Standard + Advanced + Focus pipelines into one intelligent system — auto-selects the optimal approach for each passage.
>
> **[Try Lynote.ai Free →](https://lynote.ai)**

---

## How It Works

### Step-by-Step Pipeline

| Step | Engine | From → To | Purpose |
|------|--------|-----------|---------|
| 1 | LLM (temp 1.3) | Input → Chinese (Chinese Rewriting) | LLM humanization rewrite + language shift |
| 2 | LLM (temp 1.3) | Chinese → Japanese (Japanese Rewriting) | Second LLM humanization, carries Step 1 as history |
| 3 | Google Translate | Japanese → Finnish (First Round of Translation) | First translation hop — distant language structural disruption |
| 4 | Niutrans | Finnish → English (Second-Round Translation) | Second translation hop — cross-engine reconstruction |

### Why This Chain Works

1. **Steps 1–2 (LLM Rewrite):** Configurable LLM provider (DeepSeek default, OpenRouter optional) at temperature 1.3 rewrites while translating, breaking AI statistical fingerprints with creative variation. Step 2 carries Step 1 as conversation history for coherent humanization.
2. **Steps 3–4 (Multi-Engine Translation):** Two different NMT engines (Google → Niutrans) introduce compounding structural changes. No single-engine fingerprint survives.
3. **Distant Languages:** Chinese → Japanese → Finnish maximizes linguistic distance at each hop, ensuring thorough restructuring before reconstruction to English.

---

## Lynote.ai — Beyond Standard

<p align="center">
  <a href="https://lynote.ai">
    <img src="presentation/lynote_banner.png" alt="Lynote.ai" width="500"/>
  </a>
</p>

The Standard pipeline above is **one of three tiers** available. Each has different trade-offs:

| Tier | Style Preservation | Speed | Approach |
|------|-------------------|-------|----------|
| **Standard** (this repo) | Best | Fast | Translation chain |
| **Advanced** | Good | Medium | Translation chain + LLM multi-round rewriting |
| **Focus** | Moderate | Slower | Translation chain + Detection-guided feedback loop |

**Lynote.ai** combines all three tiers and automatically selects the optimal approach for each text passage:

- **Intelligent Tier Selection** — Analyzes text and picks Standard, Adva