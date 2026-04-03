# minutes

[![GitHub stars](https://img.shields.io/github/stars/silverstein/minutes?style=social)](https://github.com/silverstein/minutes)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Crates.io](https://img.shields.io/crates/v/minutes-cli)](https://crates.io/crates/minutes-cli)

**Open-source conversation memory.** &nbsp; [useminutes.app](https://useminutes.app)

Agents have run logs. Humans have conversations. **minutes** captures the human side — the decisions, the intent, the context that agents need but can't observe — and makes it queryable.

Record a meeting. Capture a voice memo on a walk. Ask Claude *"what did I promise Sarah?"* — and get an answer. Your AI remembers every conversation you've had.

<p align="center">
  <img src="docs/assets/demo.gif" alt="minutes demo — record, dictate, phone sync, AI recall" width="750">
</p>

### Works with

<p align="center">
  <a href="#claude-code-plugin">Claude Code</a> &bull;
  <a href="#any-mcp-client-claude-code-codex-gemini-cli-claude-desktop-or-your-own-agent">Codex</a> &bull;
  <a href="#any-mcp-client-claude-code-codex-gemini-cli-claude-desktop-or-your-own-agent">Gemini CLI</a> &bull;
  <a href="#any-mcp-client-claude-code-codex-gemini-cli-claude-desktop-or-your-own-agent">Claude Desktop</a> &bull;
  <a href="#mistral-vibe">Mistral Vibe</a> &bull;
  <a href="#vault-sync-obsidian--logseq">Obsidian</a> &bull;
  <a href="#vault-sync-obsidian--logseq">Logseq</a> &bull;
  <a href="#phone--desktop-voice-memo-pipeline">Phone Voice Memos</a> &bull;
  Any MCP client
</p>

## Quick start

```bash
# macOS — Desktop app (menu bar, recording UI, AI assistant)
brew install --cask silverstein/tap/minutes

# macOS — CLI only
brew tap silverstein/tap && brew install minutes

# Any platform — from source (requires Rust + cmake; Windows also needs LLVM)
cargo install minutes-cli                          # macOS/Linux
cargo install minutes-cli --no-default-features    # Windows (see install notes below)

# MCP server only — no Rust needed (Claude Code, Codex, Gemini CLI, Claude Desktop, etc.)
npx minutes-mcp
```

```bash
minutes setup --model small   # Download whisper model (466MB, recommended)
minutes record                # Start recording
minutes stop                  # Stop and transcribe
```

## How it works

```
Audio → Transcribe → Diarize → Summarize → Structured Markdown → Relationship Graph
         (local)     (local)     (LLM)       (decisions,            (people, commitments,
        whisper.cpp  pyannote-rs Claude/       action items,          topics, scores)
        /parakeet    (native)    Ollama/       people, entities)      SQLite index
                                Mistral/OpenAI
```

Everything runs locally. Your audio never leaves your machine (unless you opt into cloud LLM summarization). Speakers are identified via native diarization. The relationship graph indexes people, commitments, and topics across all meetings for instant queries.

## Features

### Record meetings
```bash
minutes record                                    # Record from mic
minutes record --title "Standup" --context "Sprint 4 blockers"  # With context
minutes record --language ur                      # Force Urdu (ISO 639-1 code)
minutes record --device "AirPods Pro"             # Use specific audio device
minutes stop                                      # Stop from another terminal
```

### Take notes during meetings
```bash
minutes note "Alex wants monthly billing not annual billing"          # Timestamped, feeds into summary
minutes note "Logan agreed"                       # LLM weights your notes heavily
```

### Process voice memos
```bash
minutes process ~/Downloads/voice-memo.m4a        # Any audio format
minutes watch                                     # Auto-process new files in inbox
```

### Search everything
```bash
minutes search "pricing"                          # Full-text search
minutes search "onboarding" -t memo               # Filter by type
minutes actions                                   # Open action items across all meetings
minutes actions --assignee sarah                   # Filter by person
minutes list                                      # Recent recordings
```

### Relationship intelligence

> *"What did I promise Sarah?"* — the query nobody else can answer.

```bash
minutes people                                     # Who you talk to, how often, about what
minutes people --rebuild                           # Rebuild the relationship index
minutes commitments                                # All open + overdue commitments
minutes commitments --person alex                   # What did I promise Alex?
```

Tracks people, commitments, topics, and relationship health across every meeting. Detects when you're losing touch with someone. Suggests duplicate contacts ("Sarah Chen" ↔ "Sarah"). Powered by a SQLite index rebuilt from your markdown in <50ms.

### Cross-meeting intelligence
```bash
minutes research "prici