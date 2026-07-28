<div align="center">

# PAXM

### Stop re-explaining your project to every new coding-agent session.

[![CI](https://github.com/pax-beehive/paxm/actions/workflows/ci.yml/badge.svg)](https://github.com/pax-beehive/paxm/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/pax-beehive/paxm)](https://github.com/pax-beehive/paxm/releases/latest)
[![Go](https://img.shields.io/github/go-mod/go-version/pax-beehive/paxm)](go.mod)
[![Platforms](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-6f42c1)](https://github.com/pax-beehive/paxm/releases/latest)

PAXM carries decisions, conventions, and working context into later Codex,
Claude Code, OpenCode, Pi, Cursor, TRAE, Kimi Code, ZCode, Kiro, Cline, and MCP
sessions. Start locally with SQLite and no account, API key, embeddings, or
extra memory-layer model calls. Change memory providers later without rewiring
every agent.

[Install for Codex](#codex-plugin) · [Install the CLI](#opencode-pi-cli-or-mcp) · [See the result](#what-changes-after-installation) · [Docs](#documentation) · [中文](docs/README.zh-CN.md)

</div>

## What changes after installation

In one session, record a decision:

```bash
paxm remember --profile ltm --text \
  "Production deploys run through GitHub Actions; never deploy from a laptop"
```

In a later session, Codex, Claude Code, OpenCode, Pi, or an MCP client can
recover it:

```bash
paxm recall --query "how do we deploy production?"
```

With passive integration enabled, paxm recalls relevant context before the
agent responds and durably captures completed turns afterward. Provider delays
or failures do not block the coding session.

The practical result:

- **New sessions resume with project context** instead of making you restate
  architecture decisions, conventions, and operational constraints.
- **One memory path works across agents.** A decision captured from Codex can
  be recalled from Claude Code, OpenCode, Pi, or any MCP client.
- **Your storage stays your choice.** Start with local SQLite, connect Zep,
  Mem0, MemOS, or OpenViking, or bring a private provider through JSON-RPC.
- **You retain control.** Credentials, hook trust, routing, data location,
  disable, uninstall, and rollback remain user-owned.

## Quick start

Choose the agent you already use. The Codex plugin is the shortest path to a
complete active-and-passive memory loop.

### Codex plugin

```bash
codex plugin marketplace add pax-beehive/paxm --ref paxm-memory-v0.1.4
codex plugin add paxm-memory@pax-agent-nexus
curl -fsSL https://github.com/pax-beehive/paxm/releases/latest/download/install.sh | bash
paxm setup --integration codex-plugin
```

Start a new Codex task and trust the Pax Agent neXus hooks when `/hooks` asks.
The explicit installer downloads the latest published paxm binary. The plugin
registers active-memory skills and owns the passive Codex hooks after setup;
it never installs a binary, writes credentials, or bypasses hook trust on its
own.

Verify the first successful loop before relying on passive memory:

```bash
paxm config doctor
paxm remember --profile stm --text "PAXM_FIRST_RECALL_OK"
paxm recall --query "PAXM_FIRST_RECALL_OK"
paxm history --days 1
```

Set `PAXM_VERSION` before installation for a reproducible version or rollback.
Provider credentials remain user-managed. Team Memory can derive a scoped
agent credential from a paxl device connection; paxm never writes that secret
to `config.yaml`.

### Claude Code plugin

Install the paxm CLI, then install the Claude Code plugin:

```bash
curl -fsSL https://github.com/pax-beehive/paxm/releases/latest/download/install.sh | bash
claude plugin marketplace add pax-beehive/paxm
claude plugin install paxm-claude@pax-memory
paxm setup --integration claude-plugin
```

The Claude plugin includes active-memory skills, the paxm MCP server, and five
lifecycle hooks: `SessionStart`, `UserPromptSubmit`, `PostToolUse`,
`PostToolUseFailure`, and `Stop`.

Session bootstrap injects the configured user, agent, and session identity
together with the current local time and time zone. Codex, Claude Code, and Pi
use their session-start events; OpenCode performs the same bootstrap before the
first message in a session. If a later user input arrives more than 12 hours
after the preceding turn activity, paxm refreshes the local-time context before
the agent handles that input.

### OpenCode, Pi, CLI, or MCP

Install the latest release and run interactive setup. The default SQLite
provider makes the adaptor usable without first creating an account or API
key.

```bash
curl -fsSL https://github.com/pax-beehive/paxm/releases/latest/download/install.sh | bash
paxm setup
paxm config doctor
```

`paxm setup` asks only two questions: which providers to enable and which
agents get passive memory. Agents found on the machine are pre-selected and
marked `(detected)`, and cloud provider API keys are masked as they are typed.
Everything else uses the tuned defaults. When Team Memory is sel