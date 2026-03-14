**Official website:** [nullclaw.io](https://nullclaw.io)

<p align="center">
  <img src="nullclaw.png" alt="nullclaw" width="200" />
</p>

<h1 align="center">NullClaw</h1>

<p align="center">
  <strong>Null overhead. Null compromise. 100% Zig. 100% Agnostic.</strong><br>
  <strong>678 KB binary. ~1 MB RAM. Boots in <2 ms. Runs on anything with a CPU.</strong>
</p>

<p align="center">
  <a href="https://github.com/nullclaw/nullclaw/actions/workflows/ci.yml"><img src="https://github.com/nullclaw/nullclaw/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://nullclaw.github.io"><img src="https://img.shields.io/badge/docs-nullclaw.github.io-informational" alt="Documentation" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT" /></a>
</p>

The smallest fully autonomous AI assistant infrastructure — a static Zig binary that fits on any $5 board, boots in milliseconds, and requires nothing but libc.

Docs: [English](docs/en/README.md) · [中文](docs/zh/README.md) · [Contributing](CONTRIBUTING.md)

```
678 KB binary · <2 ms startup · 5,300+ tests · 50+ providers · 19 channels · Pluggable everything
```

### Features

- **Impossibly Small:** 678 KB static binary — no runtime, no VM, no framework overhead.
- **Near-Zero Memory:** ~1 MB peak RSS. Runs comfortably on the cheapest ARM SBCs and microcontrollers.
- **Instant Startup:** <2 ms on Apple Silicon, <8 ms on a 0.8 GHz edge core.
- **True Portability:** Single self-contained binary across ARM, x86, and RISC-V. Drop it anywhere, it just runs.
- **Feature-Complete:** 50+ providers, 19 channels, 35+ tools, 10 memory engines, multi-layer sandbox, tunnels, hardware peripherals, MCP, subagents, streaming, voice — the full stack.

### Why nullclaw

- **Lean by default:** Zig compiles to a tiny static binary. No allocator overhead, no garbage collector, no runtime.
- **Secure by design:** pairing, strict sandboxing (landlock, firejail, bubblewrap, docker), explicit allowlists, workspace scoping, encrypted secrets.
- **Fully swappable:** core systems are vtable interfaces (providers, channels, tools, memory, tunnels, peripherals, observers, runtimes).
- **No lock-in:** OpenAI-compatible provider support + pluggable custom endpoints.

## Benchmark Snapshot

Local machine benchmark (macOS arm64, Feb 2026), normalized for 0.8 GHz edge hardware.

| | [OpenClaw](https://github.com/openclaw/openclaw) | [NanoBot](https://github.com/HKUDS/nanobot) | [PicoClaw](https://github.com/sipeed/picoclaw) | [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) | **[🦞 NullClaw](https://github.com/nullclaw/nullclaw)** |
|---|---|---|---|---|---|
| **Language** | TypeScript | Python | Go | Rust | **Zig** |
| **RAM** | > 1 GB | > 100 MB | < 10 MB | < 5 MB | **~1 MB** |
| **Startup (0.8 GHz)** | > 500 s | > 30 s | < 1 s | < 10 ms | **< 8 ms** |
| **Binary Size** | ~28 MB (dist) | N/A (Scripts) | ~8 MB | 3.4 MB | **678 KB** |
| **Tests** | — | — | — | 1,017 | **5,300+** |
| **Source Files** | ~400+ | — | — | ~120 | **~230** |
| **Cost** | Mac Mini $599 | Linux SBC ~$50 | Linux Board $10 | Any $10 hardware | **Any $5 hardware** |

> Measured with `/usr/bin/time -l` on ReleaseSmall builds. nullclaw is a static binary with zero runtime dependencies.

Reproduce locally:

```bash
zig build -Doptimize=ReleaseSmall
ls -lh zig-out/bin/nullclaw

/usr/bin/time -l zig-out/bin/nullclaw --help
/usr/bin/time -l zig-out/bin/nullclaw status
```

## Documentation

Start here if you want the shortest path to install, configure, operate, or extend nullclaw.

Localized documentation lives under `docs/en/` and `docs/zh/`. Use the links below to jump straight to the page you need.

| Need | English | 中文 |
|---|---|---|
| Start here | [`docs/en/README.md`](docs/en/README.md) | [`docs/zh/README.md`](docs/zh/README.md) |
| Install | [`docs/en/installation.md`](docs/en/installation.md) | [`docs/zh/installation.md`](docs/zh/installation.md) |
| Configure | [`docs/en/configuration.md`](docs/en/configuration.md) | [`docs/zh/configuration.md`](docs/zh/configuration.md) |
| Commands | [`docs/en/commands.md`](docs/en/commands.md) | [`docs/zh/commands.md`](docs/zh/commands.md) |
| Development | [`docs/en/development.md`](docs/en/development.md) | [`docs/zh/development.md`](docs/zh/development.md) |
| Operations | [`docs/en/usage.md`](docs/en/usage.md) | [`docs/zh/usage.md`](docs/zh/usage.md) |
| Architecture | [`docs/en/architecture.md`](docs/en/architecture.md) | [`docs/zh/architecture.md`](docs/zh/architecture.md) |
| Security | [`docs/en/security.md`](docs/en/security.md) | [`docs/zh/security.md`](docs/zh/security.md) |
| Gateway API | [`docs/en/gateway-api.md`](docs/en/gateway-api.md) | [`docs/zh/gateway-api.md`](docs/zh/gateway-api.md) |

- Specialized guides: [`CONTRIBUTING.md`](CONTRIBUTING.md), [`SECURITY.md`](SECURITY.md), [`SIGNAL.md`](SIGNAL.md)

## Choose Your Path

| Goal | Open this first | Then go to |
|---|---|---|
| First run in English | [`do