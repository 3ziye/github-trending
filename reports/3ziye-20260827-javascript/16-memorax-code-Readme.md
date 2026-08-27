<h1 align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/memorax-code-lockup-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="docs/assets/memorax-code-lockup-light.svg">
    <img src="docs/assets/memorax-code-lockup-light.svg" alt="MemoraX Code" width="420">
  </picture>
</h1>

<p align="center">
  <a href="https://trendshift.io/repositories/105791?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-105791" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/105791/daily?language=JavaScript" alt="memorax-ai/memorax-code | Trendshift" width="250" height="55" /></a>
</p>

<h2 align="center">Never lose context. Never start over.</h2>

<p align="center">
  <sub>
    Beyond code, it remembers how your architecture evolves and how your engineering unfolds.
  </sub>
</p>

<p align="center">
  <a href="https://code.memorax.net/"><img src="https://img.shields.io/badge/website-code.memorax.net-2563eb" alt="MemoraX Code website"></a>
  <a href="https://www.npmjs.com/package/@memorax/memorax-code"><img src="https://img.shields.io/npm/v/@memorax/memorax-code.svg" alt="npm version"></a>
  <img src="https://img.shields.io/npm/v/@memorax/memorax-code.svg?label=version&color=f59e0b" alt="npm package version">
  <img src="https://img.shields.io/badge/node-%3E%3D20-339933?logo=node.js&logoColor=white" alt="Node.js 20 or newer">
</p>

<p align="center">
  <a href="https://discord.gg/eCUS8PpjG"><img src="https://img.shields.io/badge/Discord-Join%20Chat-5865F2?logo=discord&logoColor=white" alt="Join the MemoraX Code Discord community"></a>
  <a href="docs/assets/wechat-group-qr.jpg"><img src="https://img.shields.io/badge/WeChat-Join%20Group-07C160?logo=wechat&logoColor=white" alt="Join the MemoraX Code WeChat group"></a>
</p>

<p align="center">
  <strong>English</strong> · <a href="README.zh.md">简体中文</a>
</p>

## Make Every Interaction the Starting Point for the Next

Coding agents are good at the task in front of them, but a new session often
starts without the architecture, failed attempts, repository rules, or working
preferences established before it.

MemoraX Code gives Codex, Claude Code, DeepSeek Harness, and OpenCode a shared
memory layer for that context.
It can recall prior engineering knowledge, capture reusable lessons from
completed work, maintain repository knowledge, and carry your procedures and
preferences into future sessions.

The goal is not to remember everything. It is to bring back the small amount of
memory relevant to the current task so the agent can reach useful investigation
and validation sooner.

## Quick Start

Prepare Node.js 20+ (Node.js 24 LTS recommended) and at least one of Codex,
Claude Code, DeepSeek Harness, or OpenCode. Python 3 is required for Repo
Memory operations. Each coding-agent harness retains its own runtime
requirements; current DeepSeek Harness releases require Node.js
`^22.19.0 || >=24.0.0`. DSH may be installed globally or initialized
beforehand through its official `npx` workflow.

### Install and Connect

#### 1. Install the Package

```bash
npm install -g @memorax/memorax-code
```

#### 2. Connect a MemoraX Account (Recommended)

[Create a MemoraX account](https://platform.memorax.net/) or use an existing
one, then run:

```bash
memorax-code setup --existing-account
```

> [!TIP]
> Using MemoraX Code across devices? Find the MemoraX username and API key
> needed by setup in the MemoraX Code configuration file on a configured device
> (normally `~/.memorax-code/config.toml`), then enter them locally during setup
> on another device. This file contains your API key—keep it private and never
> paste it into chats or public issues.

#### Or Try Without an Account (90-Day Guest Mode)

To start immediately and connect an account later, run:

```bash
memorax-code setup
```

To activate your guest account, first run this command directly in your local
terminal:

```bash
memorax-code account --show-mark-id
```

After obtaining the Mark ID, create your MemoraX account. The platform does
not currently support attaching a Mark ID to an account that has already been
registered.

Both setup paths automatically detect supported coding agents. Restart or
refresh every detected coding agent after setup.

### Installation Troubleshooting

If the initial setup does not work as expected, check these common cases:

| Symptom | Recommended fix |
| --- | --- |
| Installation fails with an unsupported Node.js version | Run `node --version` and upgrade to Node.js 20 or later before reinstalling MemoraX Code. |
| The package installed but setup did not start | This is expected. Run the appropriate setup command above from a normal interactive terminal. |
| Search, retrieval, or writeback is unavailable after setup | Run `memorax-code status` and `memorax-cli status`, then follow the detailed troubleshooting guide. |

See [Configuration](docs/configur