<p align="center">
  <h1 align="center">Cortex</h1>
  <p align="center"><strong>Cognitive Harness for Language Models</strong></p>
  <p align="center">
    <a href="https://github.com/by-scott/cortex/releases"><img src="https://img.shields.io/github/v/release/by-scott/cortex?display_name=tag" alt="Release"></a>
    <a href="https://crates.io/crates/cortex-sdk"><img src="https://img.shields.io/crates/v/cortex-sdk" alt="Crates.io"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  </p>
  <p align="center">
    <a href="docs/quickstart.md">Quick Start</a> ·
    <a href="docs/safe-use.md">Safe Use</a> ·
    <a href="docs/policy-profiles.md">Policy Profiles</a> ·
    <a href="docs/local-coding-agent.md">Local Coding</a> ·
    <a href="docs/local-models.md">Local Models</a> ·
    <a href="docs/usage.md">Usage</a> ·
    <a href="docs/config.md">Configuration</a> ·
    <a href="docs/plugins.md">Plugins</a> ·
    <a href="docs/roadmap.md">Roadmap</a> ·
    <a href="README.zh.md">中文</a>
  </p>
</p>

---

Cortex is a local-first runtime surface for long-running AI model work. It gives replaceable models a user-owned operating layer for durable memory, retrieval evidence, tools, permissions, channels, journal/replay, evaluation, plugin governance, and operator control.

Cortex is a cognitive harness substrate for language-model systems. In practice, that means it is infrastructure for driving, observing, evaluating, and hardening model behavior across real interfaces instead of treating one model call as the product.

Use Cortex when you want a local coding, research, or tool-using model workflow whose state stays with you: memory, journals, policies, plugin trust, retrieval corpora, traces, and operator decisions survive model/provider changes.

Cortex does not claim biological consciousness, biological wisdom, complete prompt-injection defense, hostile multi-tenant hardening, or mature sandbox containment. Policy and risk gates improve review and control, but they are not a replacement for OS/container isolation.

## What It Provides

- Long-running sessions across CLI, HTTP, socket, Telegram, QQ, WhatsApp, MCP, and ACP bridge clients.
- Actor-scoped identity for sessions, memory, tasks, audit data, transport bindings, and channel subscriptions.
- Event-sourced runtime state with SQLite WAL, externalized blobs, replay checkpoints, compaction boundaries, side-effect substitution, and replay digests.
- Durable memory with provenance, trust, owner actor, contradiction links, validity windows, usage outcomes, and graph relationships.
- RAG evidence that is cited, scoped, taint-aware, reranked, compressed, support-checked, and kept separate from durable memory.
- Tool execution with declared effects, risk policy, confirmation, preview, verification, commit records, receipts, and rollback posture.
- Plugin governance for process-isolated JSON tools and trusted native ABI extensions.
- ACP client support through configured external processes exposed by the `acp_agent` tool.
- Operator status, journal timelines, token and provider cache read/write tokens, policy simulation, replay, release gates, and dashboard surfaces.
- Protected runtime-home governance so prompt, config, and state evolution use checked runtime paths rather than ordinary file or script tools.

Cortex is not a hosted multi-tenant service. The current distribution is a daemon and Rust workspace for controlled operation of language-model behavior.

## Safe Today

Cortex is intended for a trusted local machine, reviewed plugins, and explicit operator control.

| Use | Current guidance |
|-----|------------------|
| Personal local coding or research | Recommended, with `balanced` or `strict` permissions. |
| Reviewed process plugins | Recommended when the manifest, signature, capabilities, and effects have been inspected. |
| Trusted native plugins | Treat as trusted in-process code, not as a sandboxed extension. |
| Unreviewed plugins, shared machines, or external side effects | Use conservative policies, confirmation, and narrow tool allowlists. |
| Hostile multi-tenant deployment | Not a current target. |

See [Safe Use](docs/safe-use.md) and [Maturity and Production Notes](docs/maturity.md) before enabling broad tools, native plugins, messaging channels, or `open` permissions.

## Install

Prerequisites:

- Linux x86_64
- systemd
- one LLM provider key

```bash
curl -sSf https://raw.githubusercontent.com/by-scott/cortex/main/scripts/cortex.sh | \
  CORTEX_API_KEY="your-key" \
  CORTEX_PERMISSION_LEVEL="balanced" bash -s -- install
```

Manage the daemon:

```bash
cortex demo
cortex start
cortex status
cortex doctor
cortex restart
cortex stop
```

Use Cortex:

```bash
cortex                            # REPL
cortex "summarize this project"   # one-shot turn
echo "data" | cortex "summarize"  # pipe input
cortex --acp                      # ACP bridge for a running daemon
cortex --mcp-server            