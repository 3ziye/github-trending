<p align="center">
  <img src=".github/Ball.png" alt="Spacebot" width="120" height="120" />
</p>

<h1 align="center">Spacebot</h1>

<p align="center">
  <strong>An AI agent for teams, communities, and multi-user environments.</strong><br/>
  Thinks, executes, and responds — concurrently, not sequentially.<br/>
  Never blocks. Never forgets.
</p>

<p align="center">
  <a href="https://fsl.software/">
    <img src="https://img.shields.io/static/v1?label=License&message=FSL-1.1-ALv2&color=000" />
  </a>
  <a href="https://github.com/spacedriveapp/spacebot">
    <img src="https://img.shields.io/static/v1?label=Core&message=Rust&color=DEA584" />
  </a>
  <a href="https://discord.gg/gTaF2Z44f5">
    <img src="https://img.shields.io/discord/949090953497567312?label=Discord&color=5865F2" />
  </a>
</p>

<p align="center">
  <a href="https://spacebot.sh"><strong>spacebot.sh</strong></a> •
  <a href="#how-it-works">How It Works</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#tech-stack">Tech Stack</a> •
  <a href="https://docs.spacebot.sh">Docs</a>
</p>

> **One-click deploy with [spacebot.sh](https://spacebot.sh)** — connect your Discord, Slack, Telegram, or Twitch, configure your agent, and go. No self-hosting required.

<p align="center">
  <img src=".github/spacebot-ui.jpg" alt="Spacebot UI" />
</p>

---

## The Problem

Most AI agent frameworks run everything in a single session. One LLM thread handles conversation, thinking, tool execution, memory retrieval, and context compaction — all in one loop. When it's doing work, it can't talk to you. When it's compacting, it goes dark. When it retrieves memories, raw results pollute the context with noise.

[OpenClaw](https://github.com/anomalyco/openclaw) _does_ have subagents, but handles them poorly and there's no enforcement to their use. The session is the bottleneck for everything.

Spacebot splits the monolith into specialized processes that only do one thing, and delegate everything else.

---

## Built for Teams and Communities

Most AI agents are built for one person in one conversation. Spacebot is built for many people working together — a Discord community with hundreds of active members, a Slack workspace with teams running parallel workstreams, a Telegram group coordinating across time zones.

This is why the architecture exists. A single-threaded agent breaks the moment two people talk at once. Spacebot's delegation model means it can think about User A's question, execute a task for User B, and respond to User C's small talk — all at the same time, without any of them waiting on each other.

**For communities** — drop Spacebot into a Discord server. It handles concurrent conversations across channels and threads, remembers context about every member, and does real work (code, research, file operations) without going dark. Fifty people can interact with it simultaneously.

**For fast-moving channels** — when messages are flying in, Spacebot doesn't try to respond to every single one. A message coalescing system detects rapid-fire bursts, batches them into a single turn, and lets the LLM read the room — it picks the most interesting thing to engage with, or stays quiet if there's nothing to add. Configurable debounce timing, automatic DM bypass, and the LLM always knows which messages arrived together.

**For teams** — connect it to Slack. Each channel gets a dedicated conversation with shared memory. Spacebot can run long coding sessions for one engineer while answering quick questions from another. Workers handle the heavy lifting in the background while the channel stays responsive.

**For multi-agent setups** — run multiple agents on one instance. A community bot with a friendly personality on Discord, a no-nonsense dev assistant on Slack, and a research agent handling background tasks. Each with its own identity, memory, and security permissions. One binary, one deploy.

### Deploy Your Way

| Method                                 | What You Get                                                                                |
| -------------------------------------- | ------------------------------------------------------------------------------------------- |
| **[spacebot.sh](https://spacebot.sh)** | One-click hosted deploy. Connect your platforms, configure your agent, done.                |
| **Self-hosted**                        | Single Rust binary. No Docker, no server dependencies, no microservices. Clone, build, run. |
| **Docker**                             | Container image with everything included. Mount a volume for persistent data.               |

---

## Capabilities

### Task Execution

Workers come loaded with tools for real work:

- **Shell** — run arbitrary commands with configurable timeouts
- **File** — read, write, and list files with auto-created directories
- **Exec** — run specific programs with arguments and environment variables
- **[OpenCode](https://opencode.ai