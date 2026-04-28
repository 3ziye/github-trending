<div align="center">
  <img width="1500" height="276" alt="graymatter-banner" src=".github/assets/graymatter-banner-1.jpg" />
</div>

<h1 align="center"> GrayMatter </h1>


<p align="center">
  <a href="https://github.com/angelnicolasc/graymatter/actions/workflows/ci.yml"><img src="https://github.com/angelnicolasc/graymatter/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://pkg.go.dev/github.com/angelnicolasc/graymatter"><img src="https://pkg.go.dev/badge/github.com/angelnicolasc/graymatter.svg" alt="Go Reference"></a>
  <a href="https://github.com/angelnicolasc/graymatter/releases/tag/v0.5.1"><img src="https://img.shields.io/github/v/release/angelnicolasc/graymatter" alt="Latest Release"></a>
  <img src="https://img.shields.io/badge/coverage-73.5%25-brightgreen" alt="Coverage 73.5%">
  <img src="https://img.shields.io/badge/platforms-linux%20%7C%20macOS%20%7C%20windows-blue" alt="Platforms">
  <img src="https://goreportcard.com/badge/github.com/angelnicolasc/graymatter" alt="Go Report Card">
  <img src="https://img.shields.io/github/license/angelnicolasc/graymatter" alt="License">
<div align="center">
<br />

<strong>Three lines of code to give your AI agents persistent memory and cut token usage by 90%.</strong>
<br /><br />
One binary. Drop it in. Run it. No Docker, no databases, no config files, no cloud accounts, no bullshit.
<br /><br />
<strong>General-purpose MCP server. Zero vendor lock-in.</strong>
<br />
Works with Claude Code, Cursor, Codex, OpenCode, Antigravity — and any MCP-compatible client.
<br />
Also a plain Go library if you don't use MCP.
<br /><br />
Free. Offline. No account required.

<br />
</div>

```go
ctx := context.Background()
mem := graymatter.New(".graymatter")
mem.Remember(ctx, "agent", "user prefers bullet points, hates long intros")
facts, _ := mem.Recall(ctx, "agent", "how should I format this response?")
// ["user prefers bullet points, hates long intros"]
```

---

## Why

Every AI agent is **stateless by default**. Each run re-injects the full
conversation history — and that history grows linearly. Two prompts in and you've already burned half of your daily quota.

That's not just a memory problem. That's a money and performance problem.


**Mem0, Zep, Supermemory** solve this — but they're Python/TypeScript-only
and require a running server. The Go ecosystem has no production-ready,
embeddable, zero-dependency memory layer for agents.

That gap is GrayMatter.

<p align="center">
  <img src=".github/assets/token-reduction-chart1.jpg" alt="GrayMatter-Chart1" width="800px" style="max-width: 900px;">
</p>


<p align="center">
<strong>~97% reduction in context tokens</strong> — versus full-history injection.<br>
Context quality <em>improves</em> over time as consolidation surfaces only what matters.<br>
No Docker. No Redis. No API key required for storage.<br><br>
Drop it in once. It auto-connects to <strong>Claude Code, Cursor, Codex, OpenCode, Antigravity</strong> — any MCP-compatible client picks it up automatically.
</p>

---

## Observability

You can't improve what you can't see.

`graymatter tui` opens a live terminal dashboard with everything your
agent memory is doing — no extra setup required.

<p align="center">
  <img src=".github/assets/tui-graymatter.jpg" alt="GrayMatter-TUI" width="900px" style="max-width: 900px;">
</p>

**What you get at a glance:**

- **Facts** — total stored, distributed across agents
- **Memory cost** — KB on disk (text + embeddings), not tokens
- **Recalls** — cumulative access count across all sessions
- **Health** — percentage of facts above relevance threshold (weight > 0.5)
- **Token cost (30d)** — real spend breakdown by model, with cache hit rate
- **Agent activity** — facts vs recalls per agent, side by side
- **Weight distribution** — how consolidated your memory is over time
- **Activity timeline** — facts created per day, last 30 days

The dashboard auto-refreshes every 5 seconds. Press `1–4` to switch tabs,
`r` to force refresh, `q` to quit.

---


## Install

**Binary (recommended):**

```bash
# Linux (x86_64)
curl -sSL -o graymatter.tar.gz https://github.com/angelnicolasc/graymatter/releases/download/v0.5.1/graymatter_0.5.1_linux_amd64.tar.gz
tar -xzf graymatter.tar.gz
sudo mv graymatter /usr/local/bin/

# Linux (ARM64)
curl -sSL -o graymatter.tar.gz https://github.com/angelnicolasc/graymatter/releases/download/v0.5.1/graymatter_0.5.1_linux_arm64.tar.gz
tar -xzf graymatter.tar.gz
sudo mv graymatter /usr/local/bin/

# macOS (Apple Silicon)
curl -sSL -o graymatter.tar.gz https://github.com/angelnicolasc/graymatter/releases/download/v0.5.1/graymatter_0.5.1_darwin_arm64.tar.gz
tar -xzf graymatter.tar.gz
sudo mv graymatter /usr/local/bin/

# Windows (PowerShell)
iwr https://github.com/angelnicolasc/graymatter/releases/download/v0.5.1/graymatter_0.5.1_windows_amd64.zip -OutFile graymatter.zip
Expand-Archive graymatter.zip -DestinationPath .\graymatter_cli
```

**Go install:**

```bash
go install github.com/ange