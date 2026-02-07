[![Discord](https://img.shields.io/badge/discord-join-5865F2?logo=discord&logoColor=white)](https://discord.gg/VEhNQXxYMB)

# OpenWork
> Make your company feel 1000× more productive.

We give AI agents the tools your team already uses and let them learn from your behavior. The more you use OpenWork, the more connected your tools become, the more knowledge accumulates, and the bigger the chunks of work you can automate.

OpenWork is the simplest interface to OpenCode: a desktop app for running agentic workflows across your tools without living in the terminal.
Double-click, pick a folder, and you get three things instantly:
1. Zero-friction setup — your existing opencode configuration just works, no migration needed
2. Chat access — WhatsApp and Telegram ready to go (one token, done)
3. Cloud-ready — every app doubles as a client; deploy to the cloud and access from anywhere
> **The easiest way to create safe agentic workflows and share them with your team**

It's an **extensible, open-source alternative** to “Claude Work”.


<video src="https://github.com/different-ai/openwork/releases/download/v0.11.16/app-demo-compressed.mp4" width="1292" autoplay loop muted playsinline></video>


<img width="1292" height="932" alt="Screenshot 2026-01-31 at 13 43 30" src="https://github.com/user-attachments/assets/6639d1ef-c831-406e-a812-87fde403e6d5" />


OpenWork is designed around the idea that you can easily ship your agentic workflows as a repeatable, productized process.

It’s a native desktop app that runs **OpenCode** under the hood, but presents it as a clean, guided workflow:
- pick a workspace
- start a run
- watch progress + plan updates
- approve permissions when needed
- reuse what works (commands + skills)

The goal: make “agentic work” feel like a product, not a terminal.


## Alternate UIs

- **Owpenbot (WhatsApp bot)**: a lightweight WhatsApp bridge for a running OpenCode server. Install with:
  - `curl -fsSL https://raw.githubusercontent.com/different-ai/owpenbot/dev/install.sh | bash`
  - run `owpenbot setup`, then `owpenbot whatsapp login`, then `owpenbot start`
  - full setup: https://github.com/different-ai/owpenbot/blob/dev/README.md
- **Openwrk (CLI host)**: run OpenCode + OpenWork server without the desktop UI. Install with `npm install -g openwrk`.
  - docs: [packages/headless/README.md](./packages/headless/README.md)


## Quick start
Download the dmg here https://github.com/different-ai/openwork/releases (or install from source below)

## Why

Current CLI and GUIs for opencode are anchored around developers. That means a focus on file diffs, tool names, and hard to extend capabilities without relying on exposing some form of cli.

OpenWork is designed to be:
- **Extensible**: skill and opencode plugins are installable modules.
- **Auditable**: show what happened, when, and why.
- **Permissioned**: access to privileged flows.
- **Local/Remote**: OpenWork works locally as well as can connect to remote servers.

## What’s Included 

- **Host mode**: runs opencode locally on your computer
- **Client mode**: connect to an existing OpenCode server by URL.
- **Sessions**: create/select sessions and send prompts.
- **Live streaming**: SSE `/event` subscription for realtime updates.
- **Execution plan**: render OpenCode todos as a timeline.
- **Permissions**: surface permission requests and reply (allow once / always / deny).
- **Templates**: save and re-run common workflows (stored locally).
- **Skills manager**:
  - list installed `.opencode/skills` folders
  - install from OpenPackage (`opkg install ...`)
  - import a local skill folder into `.opencode/skills/<skill-name>`
 

## Skill Manager    
<img width="1292" height="932" alt="image" src="https://github.com/user-attachments/assets/b500c1c6-a218-42ce-8a11-52787f5642b6" />


## Works on local computer or servers
<img width="1292" height="932" alt="Screenshot 2026-01-13 at 7 05 16 PM" src="https://github.com/user-attachments/assets/9c864390-de69-48f2-82c1-93b328dd60c3" />


## Quick Start

### Requirements

- Node.js + `pnpm`
- Rust toolchain (for Tauri): install via `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
- Tauri CLI: `cargo install tauri-cli`
- OpenCode CLI installed and available on PATH: `opencode`

### Install

```bash
pnpm install
```

OpenWork now lives in `packages/app` (UI) and `packages/desktop` (desktop shell).

### Run (Desktop)

```bash
pnpm dev
```

### Run (Web UI only)

```bash
pnpm dev:ui
```

### Arch Users:

```bash
yay -s opencode # Releases version
```

## Architecture (high-level)

- In **Host mode**, OpenWork spawns:
  - `opencode serve --hostname 127.0.0.1 --port <free-port>`
  - with your selected project folder as the process working directory.
In Host mode, OpenWork starts an OpenCode server directly on your own computer in the background.
When you select a project folder, OpenWork runs OpenCode locally using that folder and connects the desktop UI to it.
This allows you to run agentic workflows, 