<div align="center">

![XMASJS LOGO](./Xmas.JS.svg)
> **above logo does not represent any religious affiliation** , it is simply a stylized representation of "Xmas" as in "ECMAScript".

# Xmas.JS

**A Modern System Scripting Runtime for the JavaScript Era**

[![License: Apache-2.0 OR GPL-3.0](https://img.shields.io/badge/License-Apache%202.0%20OR%20GPL%203.0-blue.svg)](LICENSE)
[![WinterTC Compatible](https://img.shields.io/badge/WinterTC-Compatible-green.svg)](https://wintertc.org/)
[![Built with QuickJS](https://img.shields.io/badge/Built%20with-QuickJS-orange.svg)](https://bellard.org/quickjs/)
[![Powered by Tokio](https://img.shields.io/badge/Powered%20by-Tokio-red.svg)](https://tokio.rs/)

[Features](#-features) • [Installation](#-installation) • [Quick Start](#-quick-start) • [Benchmarks](#-benchmarks) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 🎯 What is Xmas.JS?

Xmas.JS is a **lightweight, high-performance JavaScript/TypeScript runtime** designed to replace traditional system scripting languages like **Lua, Perl, and Python** for system administration, automation, and glue code tasks.

Unlike Node.js, Deno, or Bun which target web applications and server-side development, **Xmas.JS is purpose-built for:**

- 🔧 **System scripting and automation** - Replace Bash, PowerShell, Python scripts
- ⚡ **Serverless and edge computing** - Cold start in milliseconds, not seconds
- 🪶 **Embedded scripting** - Minimal memory footprint (<5MB)
- 🔌 **CLI tools and utilities** - Fast startup for command-line applications
- 🧩 **System integration** - Native Rust modules for deep system access

> **Note:** The word "Xmas" is pronounced like "ECMAS" (ECMAScript), not a religious reference. "JavaScript" in this context refers to ECMAScript/TypeScript, not Oracle's JavaScript™ trademark.

---

## 🚀 Why Xmas.JS?

### The Problem with Existing Runtimes

**QuickJS does not use any sort of JIT compilation**, making it ideal for fast startup and low memory usage, but less suited for long-running web servers.

Modern JavaScript runtimes like Node.js, Deno, and Bun are excellent for **web servers and applications**, but they're **overkill for scripting**:

| Runtime     | Cold Start  | Memory (Idle) | Best Use Case                             |
| ----------- | ----------- | ------------- | ----------------------------------------- |
| **Node.js** | ~100-200ms  | ~30-50MB      | Web servers, long-running apps            |
| **Deno**    | ~150-300ms  | ~40-60MB      | Secure web apps, TypeScript projects      |
| **Bun**     | ~50-100ms   | ~25-35MB      | Fast web development                      |
| **Xmas.JS** | **~5-15ms** | **~3-8MB**    | **System scripts, CLI tools, serverless** |

### The Xmas.JS Difference

```
Traditional System Scripts          Modern System Scripts with Xmas.JS
┌─────────────────────────┐        ┌─────────────────────────┐
│  Python + libraries     │        │  Xmas.JS + TypeScript   │
│  Slow startup           │   →    │  Instant startup        │
│  Heavy dependencies     │        │  Zero dependencies      │
│  Version hell           │        │  Single binary          │
│  Limited async          │        │  Native async/await     │
└─────────────────────────┘        └─────────────────────────┘
```

**Performance Targets:**
- ⚡ **10x faster startup** than Node.js/Deno
- 💰 **2x lower cost** on serverless platforms
- 🪶 **5x smaller memory footprint** than traditional runtimes
- 🔥 **Native performance** via Rust integration

---

## ✨ Features

### Core Capabilities
- ✅ **[WinterTC](https://wintertc.org/) Compatible APIs** - Standard Web APIs (fetch, crypto, streams, etc.)
- ✅ **Modern JavaScript/TypeScript** - Full ES2023+ support including async/await, modules, decorators
- ✅ **Ultra-Fast Startup** - Cold start in ~5-15ms, perfect for CLI and serverless
- ✅ **Minimal Memory Footprint** - Runs comfortably in <5MB RAM
- ✅ **Async I/O** - Powered by Tokio for high-performance concurrent operations
- ✅ **Rust Extensions** - Native module system for system-level access
- ✅ **Interactive REPL** - Built-in read-eval-print loop for rapid prototyping

### In Development
- 🚧 **Package Manager** - Built-in dependency management (no need for npm/pnpm)
- 🚧 **Cross-Platform Shell** - Execute package.json scripts anywhere
- 🚧 **Built-in Toolchain** - Bundler, minifier, TypeScript compiler, linter (powered by [OXC](https://oxc-project.github.io/))
- 🚧 **Bytecode Compilation** - Bundle scripts as bytecode for security and performance
- 🚧 **Full WinterTC Coverage** - Complete Web API compatibility

---

## 🏗️ Virtual System Layer

Xmas.JS uses a **pluggable virtual system layer** called `vsys` to abstract all system-level operations. This enables:

- 🔒 **Sandboxed execution** for serverless/edge computing
- 💾 **Custom filesystem** implementations (in-memory, virtual, restricted)
- 🌐 **Custom network** implementations (proxied, restricted, mocked)
- � **Custom module loading** (load 