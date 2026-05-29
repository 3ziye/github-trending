<div align="center">

<a href="https://rmux.io">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://rmux.io/rmux-header-dark.svg">
    <img src="https://rmux.io/rmux-header.svg" alt="RMUX" width="500">
  </picture>
</a>


**Universal Rust multiplexer for the agentic era: detachable, scriptable, and inspectable, with a tmux-compatible CLI, daemon-backed SDK, and native [Ratatui](https://ratatui.rs) integration.**

English · [Français](README.fr.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

[![License: MIT OR Apache-2.0](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue.svg)](LICENSE-MIT)
[![Release validation](https://github.com/Helvesec/rmux/actions/workflows/ci.yml/badge.svg)](https://github.com/Helvesec/rmux/actions/workflows/ci.yml)
[![rmux 0.3.1](https://img.shields.io/badge/rmux-0.3.1-informational.svg)](#install)
[![Platform: Linux | macOS | Windows](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)](#platform-support)
[![Unsafe policy](https://img.shields.io/badge/unsafe-restricted-success.svg)](#verification)

<br />
<a href="https://rmux.io">
  <img src="https://rmux.io/rmux-terminal-demo.gif" width="500" alt="RMUX terminal session demo" />
</a>

</div>

> [!IMPORTANT]
> Current release: **v0.3.1**, published on **25 May 2026**. All 90 tmux-compatible commands are implemented, but bugs are expected — this is a fresh public preview. Please [file issues](https://github.com/helvesec/rmux/issues) if you hit one.

## Why RMUX

RMUX exists because I believe the tmux use case has only been partially explored. My own starting point was simple: I wanted to run long-lived agents over SSH without losing their terminals, while still being able to inspect, script, and orchestrate everything around them.

So I rebuilt that idea from scratch in Rust: a blazing-fast, tmux-compatible multiplexer with a typed SDK, persistent sessions, structured snapshots, and native local transports on Linux, macOS, and Windows, including Windows Named Pipes.

RMUX is usable by agents, headless CLI workflows, and humans alike: you can give terminal apps detachable execution, reconnect later, inspect their state, drive them from code, or simply use it for normal tmux-style terminal work.

## Demos

Short, real examples of what RMUX can be used for.

<table>
  <tr>
    <td align="center" width="20%"><a href="https://rmux.io/#demo-orchestration"><img src="https://rmux.io/demos/demo-orchestration.png" width="150" alt="Multi Agents Orchestration demo preview"></a><br><sub><a href="https://github.com/Helvesec/rmux-demos/tree/main/demo-orchestration"><strong>Multi Agents Orchestration</strong></a></sub><br><sub>≃ 514 lines</sub></td>
    <td align="center" width="20%"><a href="https://rmux.io/#demo-broadcast"><img src="https://rmux.io/demos/demo-broadcast.png" width="150" alt="Agent Broadcast Arena demo preview"></a><br><sub><a href="https://github.com/Helvesec/rmux-demos/tree/main/broadcast-demo"><strong>Agent Broadcast Arena</strong></a></sub><br><sub>≃ 2,171 lines</sub></td>
    <td align="center" width="20%"><a href="https://rmux.io/#demo-zellij"><img src="https://rmux.io/demos/demo-zellij.png" width="150" alt="Mini-Zellij demo preview"></a><br><sub><a href="https://github.com/Helvesec/rmux-demos/tree/main/mini-zellij"><strong>Mini-Zellij</strong></a></sub><br><sub>≃ 944 lines</sub></td>
    <td align="center" width="20%"><a href="https://rmux.io/#demo-mirroring"><img src="https://rmux.io/demos/demo-mirroring.png" width="150" alt="Terminal browser mirroring demo preview"></a><br><sub><a href="https://rmux.io/#demo-mirroring"><strong>Terminal &lt;&gt; Browser Mirroring</strong></a></sub><br><sub>≃ 649 lines</sub></td>
    <td align="center" width="20%"><a href="https://rmux.io/#demo-playwright"><img src="https://rmux.io/demos/demo-playwright.png" width="150" alt="Playwright Testing demo preview"></a><br><sub><a href="https://github.com/Helvesec/rmux-demos/tree/main/terminal-playwright-demo"><strong>Playwright Testing</strong></a></sub><br><sub>≃ 1,495 lines</sub></td>
  </tr>
</table>

## Install

Prebuilt binary for macOS and Linux:

```sh
curl -fsSL https://rmux.io/install.sh | sh
```

Prebuilt binary for Windows PowerShell:

```powershell
irm https://rmux.io/install.ps1 | iex
```

Direct downloads and SHA256 checksums are available from the [v0.3.1 GitHub Release](https://github.com/helvesec/rmux/releases/tag/v0.3.1).

From crates.io with Cargo:

```sh
cargo install rmux --locked
```

From a local checkout:

```sh
cargo install --path . --locked
```

For Rust applications:

```sh
cargo add rmux-sdk
cargo add ratatui-rmux
```

## Documentation

The full RMUX documentation is available at [rmux.io/docs](https://rmux.io/docs/).

It includes [installation guides](https://rmux.io/docs/get-started/), [CLI references](https://rmux.io/docs/cli/), [SDK examples](https://rmux.io/docs/examples/), [terminal automation examples](https://rmux.io/docs/examples/#