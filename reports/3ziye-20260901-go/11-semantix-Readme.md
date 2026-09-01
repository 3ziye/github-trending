<div align="center">

# Semantix

### Cross-session memory for AI coding agents — and a much smaller bill.

**Semantic Caching · Adaptive Scheduling · Speculative Prefetch · Cross-Session Learning**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](./LICENSE)
[![Version](https://img.shields.io/badge/release-0.7.3-blue?style=flat-square)](https://github.com/Gnosil/semantix/releases)
[![GitHub stars](https://img.shields.io/github/stars/Gnosil/semantix?style=flat-square&logo=github)](https://github.com/Gnosil/semantix/stargazers)
[![GitHub contributors](https://img.shields.io/github/contributors/Gnosil/semantix?style=flat-square&logo=github)](https://github.com/Gnosil/semantix/graphs/contributors)
[![Website](https://img.shields.io/badge/website-semantix.ensureok.ai-168b6d?style=flat-square)](https://semantix.ensureok.ai)

**English** · [简体中文](./README.zh-CN.md) · [Quickstart](./docs/QUICKSTART.md) · [Technical Overview](./docs/TECHNICAL-OVERVIEW.md) · [Website](https://semantix.ensureok.ai)

</div>

<br/>

> **A coding agent loses its entire context when a session ends, and a provider's prefix cache hits only on byte-identical prompts — a single edit near the head invalidates everything after it.**
>
> Semantix addresses both: a complete coding agent with the memory kernel built in, and a standalone kernel that attaches to an agent already in use.

## Quick start

**Install** — one line, macOS / Linux (arm64 / amd64):

```bash
curl -fsSL https://raw.githubusercontent.com/Gnosil/semantix/main/agent-skill/scripts/install.sh | sh
```

This drops `semantix` + `semantix-agent` into `~/.local/bin` and turns on cross-session memory. **Use it** — start the agent inside any project; that folder becomes the workspace:

```bash
cd ~/your-project
semantix                 # bare command → launch the coding agent here (first run sets up provider / API key)
semantix search "..."    # any subcommand → the memory kernel (search / extract / inject / verify / usage)
```

Pin a version or arch with `... | sh -s -- v0.7.2 arm64`. Other install methods and the full command reference live in [docs/QUICKSTART.md](./docs/QUICKSTART.md).

## Two ways to run it

**`semantix-agent` — the complete agent.** A CLI coding agent shipping with the memory kernel built in: extraction, retrieval, injection and the evolution loop are wired at boot, with provider presets for ~50 endpoints.

**The kernel — attached to an existing agent.** Harness-independent by design; the integration surface is a small set of hooks (tool registration, message interception, session export / event bypass). Three ways in:

| Path | Integration cost | Applies to |
| --- | --- | --- |
| **Agent skill** | `semantix install --target claude-code` | Claude Code |
| **Tool registration** | two tool schemas (`semantix_lookup` / `semantix_inject`) | custom / self-hosted agents |
| **Gateway** | one base URL, no code change | any OpenAI-compatible client |

Fail-open throughout: on kernel error the agent falls back to its normal execution path.

## Cross-session memory

A project's build conventions, test layout and service flags have to be re-established in every new session. Semantix extracts reusable **slices** from finished sessions — task patterns, project knowledge, tool sequences, verified results — into a local scored library, and reinjects the relevant ones when a similar task appears. Each hit carries its retrieval zone (🟢 hit · 🟡 grey · ⚪ miss) and its source session — real `semantix search` / `dashboard` / `verify` output lives in the [reuse visualization walkthrough](./docs/TECHNICAL-OVERVIEW.md#reuse-visualization).

Hits, misses and manual corrections all feed back into slice scores and retrieval thresholds, so precision improves with use rather than volume alone. Type-aware eviction discards stale results first and retains project knowledge.

## Cache hit rate and cost

Provider prefix caches match byte-exactly: a hit requires the prompt to be identical to the previous one byte for byte, and a single differing character near the head invalidates everything after it.

The impact of that failure mode is routinely underestimated. Claude Code writes a per-request billing marker into the head of the system prompt. First-party endpoints strip it server-side; third-party endpoints do not, so there the line invalidates the cache from the first token. The spec behind the prefix-hygiene middleware attributes a **133× difference in hit rate** to that single header, and records cache spend rising **4–5×** when stripping is disabled. `semantix-gateway` strips it by default.

The design goal is to make the provider cache hittable rather than to work around it:

- **Byte-stable injection** — retrieved slices are ordered by ID rather than by score, so semantically similar requests produce byte-identical prefixes.
- **Prefix hygiene** — per-request attribution markers are stripped and the tool array is canonicalized by name, removing clien