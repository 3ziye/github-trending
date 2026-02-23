# Audio Plugin Coder (APC)
![Audio Plugin Coder Logo](https://github.com/Noizefield/audio-plugin-coder/blob/main/assets/APC_Logo.gif)

> AI-powered open-source framework for vibe-coding audio plugins from concept to shipped product

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![JUCE](https://img.shields.io/badge/JUCE-8.0-blue.svg)](https://juce.com/)
[![Platform](https://img.shields.io/badge/Platform-Windows%2011-0078D4.svg)](https://www.microsoft.com/windows)
[![Sponsor](https://img.shields.io/badge/Sponsor-Project-pink.svg?style=social&logo=heart)](https://github.com/sponsors/Noizefield) 

## About Audio Plugin Coder 

**Audio Plugin Coder (APC)** is the result of a long-standing personal obsession: building creative tools, writing music, and ultimately creating professional audio plugins.

While developing software instruments and effects has always been a dream, building real-world VSTs (with robust DSP, UI, state handling, and packaging) is notoriously complex. Over time, and especially with the rapid advancement of AI-assisted development, that barrier has finally crumbled.

Over the past 18 months, APC has been continuously designed, tested, and re-iterated as a practical **AI-first framework** for building audio plugins. This involved thousands of hours of experimentation, trial-and-error, and yes... occasionally yelling at LLMs to finally render the UI correctly.

**Midway through development, I stumbled upon the excellent work of [TÂCHES (glittercowboy)](https://github.com/glittercowboy).** His approach to context engineering was a revelation. I adopted some of his core ideas, particularly regarding meta prompting and structured agent workflows and integrated them directly into APC's DNA to create a more robust system.

APC is designed to be **Agent Agnostic**. Whether you use Google's Antigravity, Kilo, Claude Code, or Cursor, APC provides the structure they need to succeed.

## ⚠️ Development Status Disclaimer

**Audio Plugin Coder (APC) is currently in active development.** APIs may change, features may be incomplete, and bugs should be expected.

Use APC for development and experimentation purposes only until a stable release is announced.

## What is Audio Plugin Coder?

**Audio Plugin Coder (APC)** is a structured, AI-driven workflow system that guides LLM agents through the entire audio plugin development lifecycle.

It enables the creation of VST3 / AU / CLAP plugins using natural language, predefined workflows, and domain-specific skills- without constantly re-explaining context, architecture, or best practices to the AI.

Instead of manually juggling DSP architecture, UI frameworks, build systems, state tracking, and packaging, APC provides a unified framework where AI agents can operate with **long-term context, validation, and self-improving knowledge.**

## ✨ Key Features

- 🤖 **LLM-Driven Development** - Designed to work with Antigravity, Kilo, Claude Code, Cursor, or any coding agent.
- 🎯 **Structured Workflows** - Five-phase system: Dream → Plan → Design → Implement → Ship.
- 🎨 **Dual UI Frameworks** - Choose Visage (pure C++) or WebView (HTML5 Canvas).
- 📊 **State Management** - Automatic progress tracking, validation, and rollback capabilities.
- 🔧 **Self-Improving** - Auto-capture troubleshooting knowledge; the system gets smarter over time.
- 🏗️ **Production Ready** - JUCE 8 integration with CMake build system.
- 📚 **Comprehensive Skills** - Pre-built domain knowledge for DSP, UI design, testing, and packaging.
- 🎬 **Bridge Templates** - FFGL visual plugins and Max/MSP externals support.

## 🚀 Quick Start

### Prerequisites

- Windows 11 or Linux (tested with Mint Linux) (macOS not yet tested)
- PowerShell 7+
- Visual Studio 2022 (with C++ development tools)
- CMake 3.22+
- Git
- **An LLM coding agent** (Claude Code, Antigravity, Kilo, Codex, Cursor)

### Installation

1. **Clone the repository (with submodules):**
```powershell
git clone --recursive https://github.com/Noizefield/audio-plugin-coder.git
cd audio-plugin-coder
```

Or clone normally and run setup:
```powershell
git clone https://github.com/Noizefield/audio-plugin-coder.git
cd audio-plugin-coder
.\scripts\setup.ps1
```

### Bridge Templates (FFGL & Max/MSP)

If you are specifically interested in building **FFGL Visual Plugins** or **Max for Live Externals**, use the included One-Click Setup script for Windows:

```powershell
.\scripts\setup_bridges.bat
```

This script will:
1.  Check for CMake and Git.
2.  Automatically download JUCE 8 (if missing).
3.  Configure the Visual Studio solution for your chosen bridge.
4.  Open the project ready for compilation.

2. **Initialize your LLM agent:**

For **Kilo**:
```powershell
# Workflows are automatically discovered from .agent/workflows/
```

For **Claude Code**:
```powershell
# The agent will discover workflows from .agent/workflows/
```

3. **Create your first plugin:**
```
/dream MyReverb
```

The AI wi