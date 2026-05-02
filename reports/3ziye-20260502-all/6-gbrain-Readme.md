# GBrain

Your AI agent is smart but forgetful. GBrain gives it a brain.

Built by the President and CEO of Y Combinator to run his actual AI agents. The production brain powering his OpenClaw and Hermes deployments: **17,888 pages, 4,383 people, 723 companies**, 21 cron jobs running autonomously, built in 12 days. The agent ingests meetings, emails, tweets, voice calls, and original ideas while you sleep. It enriches every person and company it encounters. It fixes its own citations and consolidates memory overnight. You wake up and the brain is smarter than when you went to bed.

The brain wires itself. Every page write extracts entity references and creates typed links (`attended`, `works_at`, `invested_in`, `founded`, `advises`) with zero LLM calls. Hybrid search. Self-wiring knowledge graph. Structured timeline. Backlink-boosted ranking. Ask "who works at Acme AI?" or "what did Bob invest in this quarter?" and get answers vector search alone can't reach. Benchmarked side-by-side against the category: gbrain lands **P@5 49.1%, R@5 97.9%** on a 240-page Opus-generated rich-prose corpus, beating its own graph-disabled variant by **+31.4 points P@5** and ripgrep-BM25 + vector-only RAG by a similar margin. The graph layer plus v0.12 extract quality together carry the gap. Full BrainBench scorecards + corpus live in the sibling [gbrain-evals](https://github.com/garrytan/gbrain-evals) repo.

GBrain is those patterns, generalized. 29 skills. Install in 30 minutes. Your agent does the work. As Garry's personal agent gets smarter, so does yours.

**New in v0.25.0 — BrainBench-Real (session capture, contributor opt-in):** with `GBRAIN_CONTRIBUTOR_MODE=1` set in your shell, every real `query` + `search` call through MCP, CLI, or the subagent tool-bridge gets captured (PII-scrubbed) into an `eval_candidates` table. Snapshot with `gbrain eval export`, replay against your code change with `gbrain eval replay`. Three numbers come back: mean Jaccard@k between captured and current retrieved slugs, top-1 stability, and latency Δ. **Off by default** for production users — no surprise data accumulation. Walkthrough: [docs/eval-bench.md](docs/eval-bench.md). NDJSON wire format: [docs/eval-capture.md](docs/eval-capture.md).

> **~30 minutes to a fully working brain.** Database ready in 2 seconds (PGLite, no server). You just answer questions about API keys.

> **LLMs:** fetch [`llms.txt`](llms.txt) for the documentation map, or [`llms-full.txt`](llms-full.txt) for the same map with core docs inlined in one fetch. **Agents:** start with [`AGENTS.md`](AGENTS.md) (or [`CLAUDE.md`](CLAUDE.md) if you're Claude Code).

## Install

### On an agent platform (recommended)

GBrain is designed to be installed and operated by an AI agent. If you don't have one running yet:

- **[OpenClaw](https://openclaw.ai)** ... Deploy [AlphaClaw on Render](https://render.com/deploy?repo=https://github.com/chrysb/alphaclaw) (one click, 8GB+ RAM)
- **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** ... Deploy on [Railway](https://github.com/praveen-ks-2001/hermes-agent-template) (one click)

Paste this into your agent:

```
Retrieve and follow the instructions at:
https://raw.githubusercontent.com/garrytan/gbrain/master/INSTALL_FOR_AGENTS.md
```

That's it. The agent clones the repo, installs GBrain, sets up the brain, loads 29 skills, and configures recurring jobs. You answer a few questions about API keys. ~30 minutes.

If your agent doesn't auto-read `AGENTS.md`, point it at that file first:
`https://raw.githubusercontent.com/garrytan/gbrain/master/AGENTS.md` is the non-Claude
agent operating protocol (install, read order, trust boundary, common tasks). For
the full doc map, use `llms.txt` at the same URL root.

### Standalone CLI (no agent)

```bash
git clone https://github.com/garrytan/gbrain.git && cd gbrain && bun install && bun link
gbrain init                     # local brain, ready in 2 seconds
gbrain import ~/notes/          # index your markdown
gbrain query "what themes show up across my notes?"
```

**Do NOT use `bun install -g github:garrytan/gbrain`.** Bun blocks the top-level
postinstall hook on global installs, so schema migrations never run and the CLI
aborts with `Aborted()` the first time it opens PGLite. Use `git clone + bun install
&& bun link` as shown above. See [#218](https://github.com/garrytan/gbrain/issues/218).

```
3 results (hybrid search, 0.12s):

1. concepts/do-things-that-dont-scale (score: 0.94)
   PG's argument that unscalable effort teaches you what users want.
   [Source: paulgraham.com, 2013-07-01]

2. originals/founder-mode-observation (score: 0.87)
   Deep involvement isn't micromanagement if it expands the team's thinking.

3. concepts/build-something-people-want (score: 0.81)
   The YC motto. Connected to 12 other brain pages.
```

### MCP server (Claude Code, Cursor, Windsurf)

GBrain exposes 30+ MCP tools via stdio:

```json
{
  "mcpServers": {
    "gbrain": { "command": "gbrain", "args": ["