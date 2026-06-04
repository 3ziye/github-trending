<h1 align="center">autopreso</h1>

<p align="center">
  <a href="https://github.com/kunchenguid/autopreso/actions/workflows/ci.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/kunchenguid/autopreso/ci.yml?style=flat-square&label=ci" /></a>
  <a href="https://github.com/kunchenguid/autopreso/actions/workflows/release-please.yml"><img alt="Release" src="https://img.shields.io/github/actions/workflow/status/kunchenguid/autopreso/release-please.yml?style=flat-square&label=release" /></a>
  <a href="https://www.npmjs.com/package/autopreso"><img alt="npm" src="https://img.shields.io/npm/v/autopreso?style=flat-square" /></a>
  <a href="https://img.shields.io/badge/platform-macOS-blue?style=flat-square"><img alt="Platform" src="https://img.shields.io/badge/platform-macOS-blue?style=flat-square" /></a>
  <a href="https://x.com/kunchenguid"><img alt="X" src="https://img.shields.io/badge/X-@kunchenguid-black?style=flat-square" /></a>
  <a href="https://discord.gg/Wsy2NpnZDu"><img alt="Discord" src="https://img.shields.io/discord/1439901831038763092?style=flat-square&label=discord" /></a>
</p>

<h3 align="center">Let the whiteboard whiteboard itself.</h3>

<p align="center">
  <img src="https://raw.githubusercontent.com/kunchenguid/autopreso/main/assets/autopreso.png" alt="autopreso whiteboard hero screenshot" width="960" />
</p>

> [!WARNING]
> autopreso is in **alpha** and under active development. Expect rough edges, breaking changes, and the occasional weird drawing. Bug reports welcome.

You wanted to give the talk, not build the deck.

autopreso runs a local web app with a live Excalidraw canvas and a listening agent.
You speak; transcripts stream to a model; the model draws, labels, and rearranges the whiteboard in real time.
Stage a few seed elements, hit start, and present.

- **Hands free** - your speech drives an agent that edits an Excalidraw scene as you talk, no clicking required.
- **Bring your own model** - use your OpenAI API key or Codex subscription. Auto Preso itself is completely free and open source.
- **Can run locally** - use Moonshine for transcription and Ollama for the agent and you get a fully local setup.

## Quick Start

```sh
$ npx autopreso              # boots the server, opens the browser
autopreso listening at http://127.0.0.1:3210

# In the browser:
# 1. Drop reference materials onto the staging canvas (title, agenda, etc).
# 2. Pick your microphone, transcription model, agent model, and optional Agent instructions.
# 3. Click "Start Preso" and start talking.
```

## Install

**npm (recommended)**

```sh
npm install -g autopreso
autopreso
```

**npx (no install)**

```sh
npx autopreso
```

**From source**

```sh
git clone https://github.com/kunchenguid/autopreso.git
cd autopreso
npm install
npm start
```

## How It Works

```
  ┌──────────┐   audio    ┌──────────────┐   text   ┌──────────────┐
  │   mic    │──────────► │     STT      │────────► │  whiteboard  │
  │ (browser)│   24kHz    │ Moonshine /  │ chunks   │    agent     │
  └──────────┘            │ OpenAI WS    │          │ (OpenAI /    │
                          └──────────────┘          │  Codex /     │
                                                    │  Ollama)     │
                                                    └──────┬───────┘
                                                           │ tool calls
                                                           ▼
                                                  ┌────────────────┐
                                                  │   Excalidraw   │
                                                  │  scene (live)  │
                                                  └────────────────┘
```

- **Two modes** - "staging" lets you sketch seed content client-side; "live" hands the canvas over to the agent, biases OpenAI Realtime transcription toward staging text and labels, and starts streaming transcripts.
- **Local server, local network only** - the Express + WebSocket server binds to 127.0.0.1; nothing is exposed beyond your machine.
- **Persistent settings** - models, API keys, STT engine choices, and Agent instructions live in `~/.config/autopreso/settings.json` and survive restarts.
- **Warmup loop** - after you hit start the agent primes itself against your staging content and Agent instructions so the first sentence you say doesn't get a cold model.

## CLI Reference

| Command        | Description                                  |
| -------------- | -------------------------------------------- |
| `autopreso`    | Start the local server and open the browser. |
| `autopreso -h` | Show help.                                   |

### Flags

| Flag         | Description                                   |
| ------------ | --------------------------------------------- |
| `--no-open`  | Start the server without opening the browser. |
| `-h, --help` | Show help.                                    |

## Configuration

Settings persist at `~/.c