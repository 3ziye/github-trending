# gograph

[![Go Report Card](https://goreportcard.com/badge/github.com/ozgurcd/gograph)](https://goreportcard.com/report/github.com/ozgurcd/gograph)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`gograph` is a local AST/type-aware Go repository context indexer for AI coding agents.

![Gograph Demo](gograph-demo.gif)

It builds a compact graph of packages, symbols, calls, routes, config reads, tests, and code-quality signals so agents can navigate Go repositories with fewer raw file reads.

> **Note on Language Support:** I originally built `gograph` specifically for **Golang** because that is what I needed for my own workflows. It currently only parses and maps Go codebases. However, the architecture is extensible! If you want to add support for other languages (Python, TypeScript, Rust, etc.), **contributions are more than welcome.** Please see the [Contributing Guide](CONTRIBUTING.md) to get started.

## Why not use a Language Server (`gopls`)?

While `gopls` has access to similar AST and type data, connecting an AI coding agent to a Language Server is notoriously difficult and inefficient:

1. **Protocol Mismatch:** AI agents operate inside terminal environments. `gopls` communicates via JSON-RPC over `stdin/stdout`. While you can invoke some `gopls` CLI commands, it usually returns raw file coordinates (`file:line:col`). This forces the agent to burn tokens running `cat` or `sed` to actually read the referenced code.
2. **LLM-Optimized Output:** `gograph` doesn't just find coordinates; it physically extracts the exact structural slice (the struct body, the interface, the method) and formats it natively in Markdown. The AI reads exactly what it needs in one shot with zero surrounding file noise.
3. **Graph-Level Diagnostics:** Language servers are built for point-in-time human IDE features (like hover or go-to-definition). `gograph` is built for systemic graph traversal. For example, `gograph trace "parse failed"` performs a reverse-BFS from an error string all the way up the call stack to the HTTP entry point. `gograph impact` calculates the full blast radius of a code change. `gopls` doesn't natively perform graph-traversal diagnostics like this out of the box.

In short: `gopls` is optimized for human IDEs. `gograph` is optimized for terminal-based LLMs trying to save context tokens.

## Features
- **Local Only:** Graph building performs no network calls and sends no source code to external APIs. MCP integration is local stdio-based.
- **Go Focused:** Maps Go project structures, packages, and dependencies using the standard AST.
- **Targeted Focus:** Extract incredibly targeted context for a single package using `focus` to save LLM tokens.
- **Token-Saving Context Bundle:** `context <symbol>` replaces 4–5 separate tool calls — returns node, source, callers, callees, and tests in one response.
- **Hotspot Ranking:** `hotspot` ranks functions by incoming call count so agents know which functions to study first.
- **Code Quality Analysis:** Cyclomatic complexity (`complexity`), god-object detection (`godobj`), and package coupling/instability (`coupling`).
- **Change Detection:** `changes` surfaces new/modified/deleted symbols since the last build without re-reading source files. `changes --git <ref>` scopes the same output to files changed since any git ref (branch, tag, or commit).
- **Dependency Trees:** `deps <pkg> [--transitive]` shows direct or full transitive import closures for any package.
- **Tech Stack Extraction:** Automatically parses `go.mod` to summarize your external dependencies (like `gin` or `pgx`) so agents instantly understand your stack.
- **Concurrency Mapping:** Detects goroutine spawns, channel sends, mutex locks, WaitGroup usage, and `sync.Once.Do` calls across the entire codebase.
- **Interface Satisfaction:** Best-effort duck-typing analysis that tells you which interfaces any struct satisfies — without running the compiler.
- **Test Coverage Map:** Best-effort mapping that links `Test*` functions to the production symbols they likely exercise.
- **Environment Config:** Surfaces every `os.Getenv` / `viper.Get*` read with file, line, and enclosing function.
- **Pathfinding:** `path <from> <to>` finds the shortest call chain between any two symbols via BFS.
- **Dead Code Detection:** `orphans` uses full reachability analysis from entry points — stricter than simple 0-call-count checks.
- **Clean Graph (No Generated Files):** Uses strict line-based detection to automatically exclude generated files like mocks or protobufs.
- **Fast:** Written in Go for high performance.

## Non-goals
- No multi-language parsing.
- No AI/model API calls.
- No embeddings.
- No SaaS backend.
- No telemetry.
- No replacement for compiler/type-checker correctness.
- No guarantee that heuristic extractors find every route, SQL query, test relation, or dynamic call.

## Correctness model
- **Default mode** uses Go AST parsing and best-effor