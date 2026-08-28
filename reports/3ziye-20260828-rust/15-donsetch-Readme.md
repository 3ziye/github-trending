<div align="center">

<img src="assets/herobanner.png" width="640" alt="DonSeTch — The web, for AI agents">

**$0. No keys, no accounts. Built from scratch in Rust.**

Fetch · search · crawl · bypass bot walls · read PDFs (even scanned) · semantic reranking

One binary · Chrome's own TLS · headless browser escalation · zero Python

Works with **Claude Code**, **Cursor**, **OpenCode**, **Pi**, **Windsurf**, and any MCP client.

</div>

<br>

<div align="center">

[![npm](https://img.shields.io/npm/v/donsetch?color=cb3837&logo=npm)](https://www.npmjs.com/package/donsetch)
[![npm downloads](https://img.shields.io/npm/dm/donsetch?color=cb3837&logo=npm&label=downloads)](https://www.npmjs.com/package/donsetch)
[![GitHub stars](https://img.shields.io/github/stars/dondai44423/donsetch?style=flat&logo=github&color=e3b341)](https://github.com/dondai44423/donsetch/stargazers)
[![CI](https://img.shields.io/github/actions/workflow/status/dondai44423/donsetch/ci.yml?branch=master&logo=github&label=CI)](https://github.com/dondai44423/donsetch/actions/workflows/ci.yml)
[![Rust](https://img.shields.io/badge/Rust-edition%202024-ce422b?logo=rust&logoColor=white)](https://www.rust-lang.org)
[![MCP](https://img.shields.io/badge/MCP-server-7c3aed?logo=modelcontextprotocol&logoColor=white)](https://modelcontextprotocol.io)
[![License](https://img.shields.io/badge/license-AGPL%203.0-2563eb)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-695%20passed-00d4aa)](#)

</div>

<br>

```bash
npm install -g donsetch
```

<div align="center">

[Install](#-install) · [Two ways to use it](#-two-ways-to-use-it) · [The 3 tools](#-the-3-tools) · [Chrome TLS](#-chrome-tls-not-chrome-like) · [Solve & Bounce](#-solve-and-bounce) · [Search](#-keyless-search) · [PDF](#-pdf--ocr) · [Benchmark](#-wrb-web-research-benchmark) · [Comparison](#-comparison) · [Gotchas](#-gotchas) · [Limits](#-honest-limits)

### 🔥 [DonSeTch vs Firecrawl — live head-to-head](#-donsetch-vs-firecrawl-live-head-to-head)

</div>

---

DonSeTch gives any AI agent full web research from a single local process. Three tools, zero API keys, zero accounts. Built in Rust — one binary, no Python, no Playwright, no Selenium, no `reqwest`, no `hyper`. Every layer built from scratch.

Works with every MCP client: Claude Code, Cursor, OpenCode, Pi, anything that speaks MCP. Also works as a standalone CLI.

## ✨ What makes it different

| | What it does |
|---|---|
| 🛡️ **Real Chrome TLS** | Drives Chrome's own BoringSSL natively. Your ClientHello IS Chrome's ClientHello — fingerprint is emergent from the real engine, not a faked table that rots. |
| ⏱️ **Temporal stealth** | TLS session resumption, conditional revalidation (304), persistent cookies, connection pooling. The loudest remaining bot tell — and nobody else fakes it. |
| 👻 **Solve-and-bounce** | Browser solves the challenge, hands cookies to tier 1, goes to sleep. Tier 1 fetches at full speed. The browser almost never fetches content. |
| 🧠 **Self-improving fetch** | Learns from every fetch. Cookie lifetimes learned adaptively. Warm starts skip the browser entirely. Converges to optimal routing per domain. |
| 🔎 **Semantic reranking** | Local ONNX cross-encoder reads query + result through full attention. Pushes out generic articles that keyword-match but aren't about the topic. |
| 🔑 **Keyless search** | 10+ backends in parallel, fused by cross-engine consensus. No API keys, no accounts, no billing. $0 forever. BYOK optional. |
| 📄 **Pixel-fusion PDF** | Glyphs + rendered pixels from the same stream, fused deterministically. No hallucination. Per-region trust audit. Scanned PDFs auto-OCR'd. |
| 🧬 **Built from scratch** | Own HTTP/2 (HPACK, flow control), own extraction engine, own PDF parser, own search aggregator, own crawl engine. Zero dependency on existing OSS web tooling. |
| 🪶 **~3.5k tokens** | Three tools, ~3.5k tokens total in the MCP context. No bloat, no redundancy, every token earns its place. |

---

## 🆕 v3 — the agent-first upgrade

Four things no free (or paid) competitor has, plus a stack of agent-first mechanics:

| | What it does |
|---|---|
| 🔗 **Reference handles** | Fetched-page links render as `[text](L12)`, search results as `S1…Sn` — and `fetch S3` just works. URLs cost 80 tokens a piece; handles cost 3. Raw URLs stay in `structuredContent` for citation. |
| 🧾 **Probe mode** | `must_contain: "CVE-2026-1234"` verifies a claim against the FULLY-fetched page but returns MATCH/NO-MATCH + ≤3 excerpts (~60 tokens instead of 4k). Verification questions stop paying reading prices. |
| ♻️ **Resurrection fetch** | Dead link? `archive=auto` transparently serves the nearest Wayback snapshot, labeled `ARCHIVED COPY — 2021-04-03 (5 years old)`. Dead ends become honest answers. |
| 🕵️ **Anti-cloak check** | On domains known to serve decoys, tier-1 responses are equivalence-checked against a headless render — `decoy suspected` is stamped, never silently passed off as content. |
| 📌 **Page memory** | Every fetch i