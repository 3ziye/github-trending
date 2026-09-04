<div align="center">

# DonSeTch

**The web, for AI agents.**

<div align="center">
<a href="https://trendshift.io/repositories/163922?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-163922" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/163922/daily?language=Rust" alt="dondai44423%2Fdonsetch | Trendshift" width="250" height="55"/></a>
</div>

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/G5Y624N5RE)

[![Rust](https://img.shields.io/badge/Rust-edition%202024-ce422b?logo=rust&logoColor=white)](https://www.rust-lang.org)
[![MCP](https://img.shields.io/badge/MCP-server-7c3aed?logo=modelcontextprotocol&logoColor=white)](https://modelcontextprotocol.io)
[![License](https://img.shields.io/badge/license-AGPL%203.0-2563eb)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-766%20passed-00d4aa)](#)
[![npm](https://img.shields.io/npm/v/donsetch?color=cb3837&logo=npm)](https://www.npmjs.com/package/donsetch)
[![npm downloads](https://img.shields.io/npm/dm/donsetch?color=cb3837&logo=npm&label=downloads)](https://www.npmjs.com/package/donsetch)
[![GitHub stars](https://img.shields.io/github/stars/dondai44423/donsetch?style=flat&logo=github&color=e3b341)](https://github.com/dondai44423/donsetch/stargazers)

[Install](#-install) · [Quickstart](#-quickstart) · [The 3 tools](#-the-3-tools) · [Chrome TLS](#-chrome-tls-not-chrome-like) · [Solve & Bounce](#-solve-and-bounce) · [Search](#-keyless-search) · [PDF](#-pdf--ocr) · [Benchmark](#-wrb-web-research-benchmark) · [Comparison](#-comparison) · [Gotchas](#-gotchas) · [Limits](#-honest-limits)

</div>

---

<img src="assets/herobanner.png" alt="DonSeTch, the web, for AI agents" width="100%">

>
> **🤝 Use Bright Data? Support DonSeTch.** Get your proxy, SERP, or
> Web Unlocker plan through this partner link and part of it comes
> back to keep DonSeTch free and actively developed. You pay nothing
> extra:
>
> 💰 **https://get.brightdata.com/ivqwoicrrlbr**
>
> Bright Data is woven into the tool itself: the `bd` SERP provider,
> the Web Unlocker tier-3 bypass, and the `unlocker` key type plug
> straight into a Bright Data account.

DonSeTch gives any AI agent full web research from a single local process.
Three tools, zero API keys, zero accounts. Rust, one binary. The fetch
and crawl transport is built from scratch: no hyper, no Playwright, no
Selenium. (BYOK adapters and the opt-in CloakBrowser installer use
reqwest; the core paths that run on every fetch do not.)

Works with every MCP client (Claude Code, Cursor, OpenCode, Pi, Hermes)
and as a standalone CLI.

## ✨ What makes it different

| | What it does |
|---|---|
| 🛡️ **Real Chrome TLS** | Drives Chrome's own BoringSSL natively. Your ClientHello IS Chrome's ClientHello. The fingerprint is emergent from the real engine, not a faked table that rots. |
| ⏱️ **Temporal stealth** | TLS session resumption, conditional revalidation (304), persistent cookies, connection pooling. The loudest remaining bot tell, and nobody else fakes it. |
| 👻 **Solve-and-bounce** | Browser solves the challenge, hands cookies back to tier 1, goes to sleep. The browser almost never fetches content. |
| 🧠 **Self-improving fetch** | Learns from every fetch. Cookie lifetimes learned adaptively. Warm starts skip the browser. Converges to optimal routing per domain. |
| 🔑 **Keyless search** | 10+ backends in parallel, fused by cross-engine consensus + local semantic reranking. No API keys. $0 forever. BYOK optional. |
| 📄 **Pixel-fusion PDF** | Glyphs + rendered pixels from the same stream, fused deterministically. Per-region trust audit. Scanned PDFs auto-OCR'd. |
| 🧬 **Built from scratch** | Own HTTP/2 (HPACK, flow control), own extraction engine, own PDF parser, own search aggregator, own crawl engine. |
| 🪶 **~3.5k tokens** | Three tools, ~3.5k tokens total in the MCP context. Every token earns its place. |

## 🆕 v3, the agent-first upgrade

Context is the agent's budget. v3 saves it aggressively:

| | What it does |
|---|---|
| 🔗 **Reference handles** | Links render as `[text](L12)`, search results as `S1…Sn`, and `fetch S3` just works. URLs cost 80 tokens, handles cost 3. Raw URLs stay in `structuredContent`. |
| 🧾 **Probe mode** | `must_contain` verifies a claim against the fully fetched page but returns MATCH/NO-MATCH + up to 3 excerpts (~60 tokens instead of 4k). |
| ♻️ **Resurrection fetch** | Dead link? `archive=auto` serves the nearest Wayback snapshot, honestly labeled with its age. |
| 🕵️ **Anti-cloak check** | On decoy-prone domains, tier-1 responses are equivalence-checked against a headless render. `decoy suspected` is stamped, never silently passed as content. |
| 📌 **Page memory** | Every fetch is fingerprinted. Re-fetches report `changed` with section-level diffs; `since_last=true` collapses a re-check to one line (~30 tokens). |
| 🧠 **Domain intelligence** | Reddit, npm/PyPI/crates.io/Go/RubyGems, GitHub, Stack