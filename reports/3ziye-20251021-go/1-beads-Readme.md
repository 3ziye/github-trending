# bd - Beads Issue Tracker 🔗

**Give your coding agent a memory upgrade**

> **🚨 CRITICAL WARNING - Do Not Use for Multiple Workstreams**
>
> **v0.9.x has data duplication and data loss bugs when handling multiple workstreams.** This creates a mess that's difficult even for agents to clean up. Until further notice, **use only for single-workstream projects**. A fix is in progress.

> **🚨 MCP SERVER WARNING - Single Project Only**
>
> **Do NOT use the MCP server if you have multiple beads repositories/projects.** The MCP server currently routes issues to the wrong database when working across multiple repos. **The beads binary (bd command, v0.9.9+) works fine for multi-workstream scenarios** - instruct your agents to use the binary directly via shell commands instead of the MCP server. A fix for the MCP server is in progress.

> **⚠️ Alpha Status**: This project is in active development. The core features work well, but expect API changes before 1.0. Use for development/internal projects first.

Beads is a lightweight memory system for coding agents, using a graph-based issue tracker. Four kinds of dependencies work to chain your issues together like beads, making them easy for agents to follow for long distances, and reliably perform complex task streams in the right order.

Drop Beads into any project where you're using a coding agent, and you'll enjoy an instant upgrade in organization, focus, and your agent's ability to handle long-horizon tasks over multiple compaction sessions. Your agents will use issue tracking with proper epics, rather than creating a swamp of rotten half-implemented markdown plans.

Instant start:

```bash
curl -fsSL https://raw.githubusercontent.com/steveyegge/beads/main/scripts/install.sh | bash
```

Then tell your coding agent to start using the `bd` tool instead of markdown for all new work, somewhere in your `AGENTS.md` or `CLAUDE.md`. That's all there is to it!

You don't use Beads directly as a human. Your coding agent will file and manage issues on your behalf. They'll file things they notice automatically, and you can ask them at any time to add or update issues for you.

Beads gives agents unprecedented long-term planning capability, solving their amnesia when dealing with complex nested plans. They can trivially query the ready work, orient themselves, and land on their feet as soon as they boot up.

Agents using Beads will no longer silently pass over problems they notice due to lack of context space -- instead, they will automatically file issues for newly-discovered work as they go. No more lost work, ever.

Beads issues are backed by git, but through a clever design it manages to act like a managed, centrally hosted SQL database shared by all of the agents working on a project (repo), even across machines.

Beads even improves work auditability. The issue tracker has a sophisticated audit trail, which agents can use to reconstruct complex operations that may have spanned multiple sessions.

Agents report that they enjoy working with Beads, and they will use it spontaneously for both recording new work and reasoning about your project in novel ways. Whether you are a human or an AI, Beads lets you have more fun and less stress with agentic coding.

![AI Agent using Beads](https://raw.githubusercontent.com/steveyegge/beads/main/.github/images/agent-using-beads.jpg)

## Features

- ✨ **Zero setup** - `bd init` creates project-local database (and your agent will do it)
- 🔗 **Dependency tracking** - Four dependency types (blocks, related, parent-child, discovered-from)
- 📋 **Ready work detection** - Automatically finds issues with no open blockers
- 🤖 **Agent-friendly** - `--json` flags for programmatic integration
- 📦 **Git-versioned** - JSONL records stored in git, synced across machines
- 🌍 **Distributed by design** - Agents on multiple machines share one logical database via git
- 🏗️ **Extensible** - Add your own tables to the SQLite database
- 🔍 **Multi-project isolation** - Each project gets its own database, auto-discovered by directory
- 🌲 **Dependency trees** - Visualize full dependency graphs
- 🎨 **Beautiful CLI** - Colored output for humans, JSON for bots
- 💾 **Full audit trail** - Every change is logged
- ⚡ **High performance** - Batch operations for bulk imports (1000 issues in ~950ms)
- 🗜️ **Memory decay** - Semantic compaction gracefully reduces old closed issues

## Installation

### Homebrew (macOS/Linux)

```bash
brew tap steveyegge/beads
brew install bd
```

**Why Homebrew?**
- ✅ Simple one-command install
- ✅ Automatic updates via `brew upgrade`
- ✅ No need to install Go
- ✅ Handles PATH setup automatically

### Quick Install Script (All Platforms)

```bash
curl -fsSL https://raw.githubusercontent.com/steveyegge/beads/main/scripts/install.sh | bash
```

The installer will:
- Detect your platform (macOS/Linux, amd64/arm64)
- Install via `go install` if Go is available
- Fall back to building from source if needed
- Guide you through PATH setup if necess