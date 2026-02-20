<p align="center">
  <img src=".github/media/banner.png" alt="Sandbox Agent SDK" />
</p>

<h3 align="center">Run Coding Agents in Sandboxes. Control Them Over HTTP.</h3>

<p align="center">
  A server that runs inside your sandbox. Your app connects remotely to control Claude Code, Codex, OpenCode, Cursor, Amp, or Pi — streaming events, handling permissions, managing sessions.
</p>

<p align="center">
  <a href="https://sandboxagent.dev/docs">Documentation</a> — <a href="https://sandboxagent.dev/docs/api-reference">API Reference</a> — <a href="https://rivet.dev/discord">Discord</a>
</p>

<p align="center">
  <em><strong>Experimental:</strong> <a href="./gigacode/">Gigacode</a> — use OpenCode's TUI with any coding agent.</em>
</p>

## Why Sandbox Agent?

Running coding agents remotely is hard. Existing SDKs assume local execution, SSH breaks TTY handling and streaming, and every agent has a different API. Building from scratch means reimplementing everything for each coding agent.

Sandbox Agent solves three problems:

1. **Coding agents need sandboxes** — You can't let AI execute arbitrary code on your production servers. Coding agents need isolated environments, but existing SDKs assume local execution. Sandbox Agent is a server that runs inside the sandbox and exposes HTTP/SSE.

2. **Every coding agent is different** — Claude Code, Codex, OpenCode, Cursor, Amp, and Pi each have proprietary APIs, event formats, and behaviors. Swapping agents means rewriting your integration. Sandbox Agent provides one HTTP API — write your code once, swap agents with a config change.

3. **Sessions are ephemeral** — Agent transcripts live in the sandbox. When the process ends, you lose everything. Sandbox Agent streams events in a universal schema to your storage. Persist to Postgres, ClickHouse, or [Rivet](https://rivet.dev). Replay later, audit everything.

## Features

- **Universal Agent API**: Single interface to control Claude Code, Codex, OpenCode, Cursor, Amp, and Pi with full feature coverage
- **Universal Session Schema**: Standardized schema that normalizes all agent event formats for storage and replay
- **Runs Inside Any Sandbox**: Lightweight static Rust binary. One curl command to install inside E2B, Daytona, Vercel Sandboxes, or Docker
- **Server or SDK Mode**: Run as an HTTP server or embed with the TypeScript SDK
- **OpenAPI Spec**: [Well documented](https://sandboxagent.dev/docs/api-reference) and easy to integrate from any language
- **OpenCode SDK & UI Support** *(Experimental)*: [Connect OpenCode CLI, SDK, or web UI](https://sandboxagent.dev/docs/opencode-compatibility) to control agents through familiar OpenCode tooling

## Architecture

![Agent Architecture Diagram](./.github/media/agent-diagram.gif)

The Sandbox Agent acts as a universal adapter between your client application and various coding agents. Each agent has its own adapter that handles the translation between the universal API and the agent-specific interface.

- **Embedded Mode**: Runs agents locally as subprocesses
- **Server Mode**: Runs as HTTP server from any sandbox provider

[Architecture documentation](https://sandboxagent.dev/docs)

## Components

| Component | Description |
|-----------|-------------|
| **Server** | Rust daemon (`sandbox-agent server`) exposing the HTTP + SSE API |
| **SDK** | TypeScript client with embedded and server modes |
| **Inspector** | Built-in UI at inspecting sessions and events |
| **CLI** | `sandbox-agent` (same binary, plus npm wrapper) mirrors the HTTP endpoints |

## Get Started

Choose the installation method that works best for your use case.

### Skill

Install skill with:

```bash
npx skills add rivet-dev/skills -s sandbox-agent
```

```bash
bunx skills add rivet-dev/skills -s sandbox-agent
```

### TypeScript SDK

Import the SDK directly into your Node or browser application. Full type safety and streaming support.

**Install**

```bash
npm install sandbox-agent@0.2.x
```

```bash
bun add sandbox-agent@0.2.x
# Optional: allow Bun to run postinstall scripts for native binaries (required for SandboxAgent.start()).
bun pm trust @sandbox-agent/cli-linux-x64 @sandbox-agent/cli-linux-arm64 @sandbox-agent/cli-darwin-arm64 @sandbox-agent/cli-darwin-x64 @sandbox-agent/cli-win32-x64
```

**Setup**

Local (embedded mode):

```ts
import { SandboxAgent } from "sandbox-agent";

const client = await SandboxAgent.start();
```

Remote (server mode):

```ts
import { SandboxAgent } from "sandbox-agent";

const client = await SandboxAgent.connect({
  baseUrl: "http://127.0.0.1:2468",
  token: process.env.SANDBOX_TOKEN,
});
```

**API Overview**

```ts
const agents = await client.listAgents();

await client.createSession("demo", {
  agent: "codex",
  agentMode: "default",
  permissionMode: "plan",
});

await client.postMessage("demo", { message: "Hello from the SDK." });

for await (const event of client.streamEvents("demo", { offset: 0 })) {
  console.log(event.type, event.data);
}
```

`permissionMode: "accep