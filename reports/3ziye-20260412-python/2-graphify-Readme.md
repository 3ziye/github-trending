# graphify

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja-JP.md) | [한국어](README.ko-KR.md)

[![CI](https://github.com/safishamsi/graphify/actions/workflows/ci.yml/badge.svg?branch=v4)](https://github.com/safishamsi/graphify/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/graphifyy)](https://pypi.org/project/graphifyy/)
[![Downloads](https://static.pepy.tech/badge/graphifyy/month)](https://pepy.tech/project/graphifyy)
[![Sponsor](https://img.shields.io/badge/sponsor-safishamsi-ea4aaa?logo=github-sponsors)](https://github.com/sponsors/safishamsi)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Safi%20Shamsi-0077B5?logo=linkedin)](https://www.linkedin.com/in/safi-shamsi)

**An AI coding assistant skill.** Type `/graphify` in Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, Aider, OpenClaw, Factory Droid, or Trae - it reads your files, builds a knowledge graph, and gives you back structure you didn't know was there. Understand a codebase faster. Find the "why" behind architectural decisions.

Fully multimodal. Drop in code, PDFs, markdown, screenshots, diagrams, whiteboard photos, images in other languages, or video and audio files - graphify extracts concepts and relationships from all of it and connects them into one graph. Videos are transcribed with Whisper using a domain-aware prompt derived from your corpus. 20 languages supported via tree-sitter AST (Python, JS, TS, Go, Rust, Java, C, C++, Ruby, C#, Kotlin, Scala, PHP, Swift, Lua, Zig, PowerShell, Elixir, Objective-C, Julia).

> Andrej Karpathy keeps a `/raw` folder where he drops papers, tweets, screenshots, and notes. graphify is the answer to that problem - 71.5x fewer tokens per query vs reading the raw files, persistent across sessions, honest about what it found vs guessed.

```
/graphify .                        # works on any folder - your codebase, notes, papers, anything
```

```
graphify-out/
├── graph.html       interactive graph - click nodes, search, filter by community
├── GRAPH_REPORT.md  god nodes, surprising connections, suggested questions
├── graph.json       persistent graph - query weeks later without re-reading
└── cache/           SHA256 cache - re-runs only process changed files
```

Add a `.graphifyignore` file to exclude folders you don't want in the graph:

```
# .graphifyignore
vendor/
node_modules/
dist/
*.generated.py
```

Same syntax as `.gitignore`. Patterns match against file paths relative to the folder you run graphify on.

## How it works

graphify runs in three passes. First, a deterministic AST pass extracts structure from code files (classes, functions, imports, call graphs, docstrings, rationale comments) with no LLM needed. Second, video and audio files are transcribed locally with faster-whisper using a domain-aware prompt derived from corpus god nodes — transcripts are cached so re-runs are instant. Third, Claude subagents run in parallel over docs, papers, images, and transcripts to extract concepts, relationships, and design rationale. The results are merged into a NetworkX graph, clustered with Leiden community detection, and exported as interactive HTML, queryable JSON, and a plain-language audit report.

**Clustering is graph-topology-based — no embeddings.** Leiden finds communities by edge density. The semantic similarity edges that Claude extracts (`semantically_similar_to`, marked INFERRED) are already in the graph, so they influence community detection directly. The graph structure is the similarity signal — no separate embedding step or vector database needed.

Every relationship is tagged `EXTRACTED` (found directly in source), `INFERRED` (reasonable inference, with a confidence score), or `AMBIGUOUS` (flagged for review). You always know what was found vs guessed.

## Install

**Requires:** Python 3.10+ and one of: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli), [Aider](https://aider.chat), [OpenClaw](https://openclaw.ai), [Factory Droid](https://factory.ai), or [Trae](https://trae.ai)

```bash
pip install graphifyy && graphify install
```

> **Official package:** The PyPI package is named `graphifyy` (install with `pip install graphifyy`). Other packages named `graphify*` on PyPI are not affiliated with this project. The only official repository is [safishamsi/graphify](https://github.com/safishamsi/graphify). The CLI and skill command are still `graphify`.

### Platform support

| Platform | Install command |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (auto-detected) or `graphify install --platform windows` |
| Codex | `graphify install --platform codex` |
| OpenCode | `graphify install --platform opencode` |
| GitHub Copilot CLI | `grap