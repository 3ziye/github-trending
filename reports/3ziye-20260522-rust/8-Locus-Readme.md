# Locus for Unity - Open Source Unity Dev Agent

> Scale game development efficiency and free creators from tedious, repetitive work.

[![Docs](https://img.shields.io/badge/DOCS-unity.farlocus.com-f2c230?style=for-the-badge&labelColor=4a4a4a)](https://unity.farlocus.com/en)
[![Release](https://img.shields.io/badge/RELEASE-GitHub-5d7285?style=for-the-badge&labelColor=4a4a4a)](https://github.com/r1n7aro/Locus/releases)
[![License](https://img.shields.io/badge/LICENSE-GPL--3.0--or--later-88b000?style=for-the-badge&labelColor=4a4a4a)](LICENSE)
[![Roadmap](https://img.shields.io/badge/ROADMAP-View-2d6cdf?style=for-the-badge&labelColor=4a4a4a)](https://unity.farlocus.com/en/overview/roadmap)
[![YouTube](https://img.shields.io/badge/YOUTUBE-Watch-ff0000?style=for-the-badge&labelColor=4a4a4a)](https://www.youtube.com/watch?v=xoApXZMon9M)
[![X](https://img.shields.io/badge/X-@farlocus-000000?style=for-the-badge&labelColor=4a4a4a)](https://x.com/farlocus)
![QQ Group](https://img.shields.io/badge/QQ_Group-1104932978-12b7f5?style=for-the-badge&labelColor=4a4a4a)

English | [简体中文](README.zh-CN.md)

[![Watch the demo on YouTube](https://img.youtube.com/vi/xoApXZMon9M/maxresdefault.jpg)](https://www.youtube.com/watch?v=xoApXZMon9M)

## Overview

`Locus for Unity` is an open-source AI Agent for Unity projects.

- **In-editor operations**: write C# code, read and modify Unity objects and assets, and complete the full feature development workflow
- **Runtime analysis and debugging**: autonomously operate and capture runtime state to help fix bugs and optimize performance
- **Automated knowledge system**: automatically summarize conversation requirements into design documents and preserve project understanding in long-term memory
- **Visual version control**: provide a visual version control interface with semantic diff analysis and conflict handling for Unity YAML assets
- **Multiple model support**: support subscription account sign-in and compatibility with multiple LLM API capabilities

Locus is currently in early testing (`v0.2.8`). We welcome you to try it and share feedback through Issues. Your input is highly valuable to us.

## What Makes Locus Technically Different?

Locus is a standalone Rust + Tauri + Vue.js application that runs as an independent process.

- We designed a proprietary intermediate representation that lets agents progressively read large scenes and assets, along with retrieval tools that help agents quickly locate target objects
- With Roslyn, Locus can JIT-compile and execute C# code inside the Unity Editor to make semantic asset edits. Locus also includes agent-side version management handling so users can review and revert asset and code changes the agent makes during a conversation
- Built on Rust's parallel ecosystem, Locus performs highly parallel asset database scans, enabling fast semantic parsing for large scenes and reference queries for arbitrary assets. The Unity Editor API only provides dependency queries
- Locus includes an automated knowledge system. The agent summarizes fragmented conversation requests into design documents and saves working understanding into memory, reducing repeated project exploration
- Documents in the knowledge system support configurable AI maintenance modes and maintenance rules, plus L0/L1/L2 injection control inside context. Users can customize progressive expansion behavior, use native lexical and syntactic retrieval across large document sets, and choose and download embedding runtimes
- We built C# state-machine tools so the agent can sample internal state through reflection at specific frames or events during runtime, output frame-by-frame tables, and dynamically debug multi-frame behavior
- Locus provides a graphical version control interface and supports semantic diff review and conflict resolution for Unity YAML files
- Locus uses Vue.js to deliver a modern frontend experience with better UX than the limited controls provided by the Unity Editor API, then embeds it into the Unity window through Windows APIs

If Locus were implemented inside the Unity Editor, or designed as an MCP server, most of these capabilities would be difficult to deliver and some would be nearly impossible technically.

## Installation

Windows is currently the only supported platform. We plan to add macOS support soon.

We recommend installing from the Releases build. For the post-installation setup flow, see [Quick Start](https://unity.farlocus.com/en/overview/install-and-setup).

## Compatibility

Locus currently supports Unity 2021 or later on Windows.

If you encounter compatibility issues on older Unity versions, please report them through Issues. We will try to fix them where practical; compatibility fixes that require substantial changes may be handled as branch-specific solutions.

## Build from Source

This repository uses `bun` + `Tauri 2`, with Windows as the primary development and build platform.

### Run in Development

```powershell
bun tauri dev
```

This comm