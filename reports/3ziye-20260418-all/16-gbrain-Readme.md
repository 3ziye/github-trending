# GBrain

Your AI agent is smart but forgetful. GBrain gives it a brain.

Built by the President and CEO of Y Combinator to run his actual AI agents. The production brain powering his OpenClaw and Hermes deployments: **17,888 pages, 4,383 people, 723 companies**, 21 cron jobs running autonomously, built in 12 days. The agent ingests meetings, emails, tweets, voice calls, and original ideas while you sleep. It enriches every person and company it encounters. It fixes its own citations and consolidates memory overnight. You wake up and the brain is smarter than when you went to bed.

GBrain is those patterns, generalized. 25 skills. Install in 30 minutes. Your agent does the work. As Garry's personal agent gets smarter, so does yours.

> **~30 minutes to a fully working brain.** Database ready in 2 seconds (PGLite, no server). You just answer questions about API keys.

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

That's it. The agent clones the repo, installs GBrain, sets up the brain, loads 25 skills, and configures recurring jobs. You answer a few questions about API keys. ~30 minutes.

### Standalone CLI (no agent)

```bash
git clone https://github.com/garrytan/gbrain.git && cd gbrain && bun install && bun link
gbrain init                     # local brain, ready in 2 seconds
gbrain import ~/notes/          # index your markdown
gbrain query "what themes show up across my notes?"
```

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
    "gbrain": { "command": "gbrain", "args": ["serve"] }
  }
}
```

Add to `~/.claude/server.json` (Claude Code), Settings > MCP Servers (Cursor), or your client's MCP config.

### Remote MCP (Claude Desktop, Cowork, Perplexity)

```bash
ngrok http 8787 --url your-brain.ngrok.app
bun run src/commands/auth.ts create "claude-desktop"
claude mcp add gbrain -t http https://your-brain.ngrok.app/mcp -H "Authorization: Bearer TOKEN"
```

Per-client guides: [`docs/mcp/`](docs/mcp/DEPLOY.md). ChatGPT requires OAuth 2.1 (not yet implemented).

## The 25 Skills

GBrain ships 25 skills organized by `skills/RESOLVER.md`. The resolver tells your agent which skill to read for any task.

[Skill files are code.](https://x.com/garrytan/status/2042925773300908103) They're the most powerful way to get knowledge work done. A skill file is a fat markdown document that encodes an entire workflow: when to fire, what to check, how to chain with other skills, what quality bar to enforce. The agent reads the skill and executes it. Skills can also call deterministic TypeScript code bundled in GBrain (search, import, embed, sync) for the parts that shouldn't be left to LLM judgment. [Thin harness, fat skills](docs/ethos/THIN_HARNESS_FAT_SKILLS.md): the intelligence lives in the skills, not the runtime.

### Always-on

| Skill | What it does |
|-------|-------------|
| **signal-detector** | Fires on every message. Spawns a cheap model in parallel to capture original thinking and entity mentions. The brain compounds on autopilot. |
| **brain-ops** | Brain-first lookup before any external API. The read-enrich-write loop that makes every response smarter. |

### Content ingestion

| Skill | What it does |
|-------|-------------|
| **ingest** | Thin router. Detects input type and delegates to the right ingestion skill. |
| **idea-ingest** | Links, articles, tweets become brain pages with analysis, author people pages, and cross-linking. |
| **media-ingest** | Video, audio, PDF, books, screenshots, GitHub repos. Transcripts, entity extraction, backlink propagation. |
| **meeting-ingestion** | Transcripts become brain pages. Every attendee gets enriched. Every company gets a timeline entry. |

### Brain operations

| Skill | What it does |
|-------|-------------|
| **enrich** | Tiered enrichment (Tier 1/2/3). Creates and updates person/company pages with compiled truth and timelines. |
| **query** | 3-layer search with synthesis and cit