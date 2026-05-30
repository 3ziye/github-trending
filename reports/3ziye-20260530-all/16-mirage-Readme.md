<p align="center">
  <img src="assets/mirage-og-light@2x.png" alt="Mirage: A Unified Virtual File System for AI Agents" width="900">
</p>

<p align="center">
    <a href="https://docs.mirage.strukto.ai" alt="Documentation">
        <img src="https://img.shields.io/badge/mirage-docs-0C0C0C?labelColor=FAFAFA" /></a>
    <a href="https://www.strukto.ai" alt="Website">
        <img src="https://img.shields.io/badge/made by-strukto.ai-0C0C0C?labelColor=FAFAFA" /></a>
    <a href="https://github.com/strukto-ai/mirage/blob/main/LICENSE" alt="License">
        <img src="https://img.shields.io/github/license/strukto-ai/mirage?color=0C0C0C&labelColor=FAFAFA" /></a>
    <a href="https://discord.gg/u8BPQ65KsS" alt="Discord">
        <img src="https://img.shields.io/badge/discord-join-0C0C0C?labelColor=FAFAFA&logo=discord&logoColor=0C0C0C" /></a>
    <br/>
    <a href="https://docs.mirage.strukto.ai/python/quickstart" alt="Python docs">
        <img src="https://img.shields.io/badge/python-docs-0C0C0C?labelColor=FAFAFA&logo=python&logoColor=0C0C0C" alt="Python docs"></a>
    <a href="https://pypi.org/project/mirage-ai/" alt="PyPI Version">
        <img src="https://img.shields.io/pypi/v/mirage-ai.svg?color=0C0C0C&labelColor=FAFAFA"/></a>
    <br/>
    <a href="https://docs.mirage.strukto.ai/typescript/quickstart" alt="TypeScript docs">
        <img src="https://img.shields.io/badge/typescript-docs-0C0C0C?labelColor=FAFAFA&logo=typescript&logoColor=0C0C0C" alt="TypeScript docs"></a>
    <a href="https://www.npmjs.com/package/@struktoai/mirage-node" alt="NPM Version">
        <img src="https://img.shields.io/npm/v/@struktoai/mirage-node.svg?color=0C0C0C&labelColor=FAFAFA"/></a>
</p>

Mirage is **a Unified Virtual File System for AI Agents**: a single tree that mounts services and data sources like S3, Google Drive, Slack, Gmail, and Redis side-by-side as one filesystem.

AI agents reach every backend with the same handful of Unix-like tools, and pipelines compose across services as naturally as on a local disk. It's a simulated environment, agents see one filesystem underneath. Any LLM that already knows bash can use Mirage out of the box, with zero new vocabulary.

```ts
const ws = new Workspace({
  '/data':   new RAMResource(),
  '/s3':     new S3Resource({ bucket: 'logs' }),
  '/slack':  new SlackResource({}),
  '/github': new GitHubResource({}),
})

await ws.execute('grep alert /slack/general/*.json | wc -l')
await ws.execute('cat /github/mirage/README.md')
await ws.execute('cp /s3/report.csv /data/local.csv')

// Register a new command, available across every mount.
ws.command('summarize', ...)

// Override a command for a specific resource + filetype —
// `cat` on a Parquet file in /s3 renders rows as JSON instead of raw bytes.
ws.command('cat', { resource: 's3', filetype: 'parquet' }, ...)

await ws.execute('summarize /github/mirage/README.md')
await ws.execute('cat /s3/events/2026-05-06.parquet | jq .user')
```

## About

- **One filesystem, every backend.** Every service speaks the same filesystem semantics, so agents reason about one abstraction instead of N SDKs and M MCPs, leaning on the filesystem and bash vocabulary LLMs are most fluent in.
- **Multiple resources, one filesystem:** RAM, Disk, Redis, S3 / R2 / OCI / Supabase / GCS, Gmail / GDrive / GDocs / GSheets / GSlides, GitHub / Linear / Notion / Trello, Slack / Discord / Telegram / Email, MongoDB, SSH, and more, mounted side-by-side under a single root.
- **Familiar bash tools across every mount.** Agents reuse the same handful of Unix-like tools instead of learning a new API per service, and pipelines compose across services as naturally as on a local disk, the exact corpus modern LLMs are most heavily trained on.
- **Portable workspaces:** clone, snapshot, and version your environment. Move agent runs between machines without restarting or reconfiguring the system.
- **Embed in your apps and services:** Python and TypeScript SDKs let you give your AI agents a virtual filesystem directly inside FastAPI, Express, browser apps, or any async runtime, no separate process required. Clone, snapshot, and version the workspace from inside your code.
- **Works with major agent application frameworks:** OpenAI Agents SDK, Vercel AI SDK (TypeScript), LangChain, Pydantic AI, CAMEL, and OpenHands.
- **Lightweight CLI + daemon:** plugs into coding agents like Claude Code and Codex so they reach every mounted resource through familiar bash, getting more useful work done per turn.

## Architecture

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/mirage-arch-dark.svg">
    <img src="assets/mirage-arch-light.svg" alt="Mirage architecture: AI Agent and Application → Mirage Bash and VFS → Dispatcher &amp; Cache → Infrastructure and Remote" width="900">
  </picture>
</p>

## Installation

### Prerequisites

- **Python** ≥ 3.12 for the `mirage-ai` package and the `mirage` CLI
- **Node.js** ≥ 20 for the TypeScript SDK
- **macOS*