# bd - Beads Issue Tracker 🔗

[![Go Version](https://img.shields.io/github/go-mod/go-version/steveyegge/beads)](https://go.dev/)
[![Release](https://img.shields.io/github/v/release/steveyegge/beads)](https://github.com/steveyegge/beads/releases)
[![npm version](https://img.shields.io/npm/v/@beads/bd)](https://www.npmjs.com/package/@beads/bd)
[![CI](https://img.shields.io/github/actions/workflow/status/steveyegge/beads/ci.yml?branch=main&label=tests)](https://github.com/steveyegge/beads/actions/workflows/ci.yml)
[![Go Report Card](https://goreportcard.com/badge/github.com/steveyegge/beads)](https://goreportcard.com/report/github.com/steveyegge/beads)
[![License](https://img.shields.io/github/license/steveyegge/beads)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/beads-mcp)](https://pypi.org/project/beads-mcp/)

**Give your coding agent a memory upgrade**

> ## 🎉 **v0.20.1: Multi-Worker Support Unlocked!** 🎉
>
> **Hash-based IDs eliminate merge conflicts and collision issues!**
>
> Previous versions used sequential IDs (bd-1, bd-2, bd-3...) which caused frequent collisions when multiple agents or branches created issues concurrently. Version 0.20.1 switches to **hash-based IDs** (bd-a1b2, bd-f14c, bd-3e7a...) that are collision-resistant and merge-friendly.
>
> **What's new:** ✅ Multi-clone, multi-branch, multi-agent workflows now work reliably  
> **What changed:** Issue IDs are now short hashes instead of sequential numbers  
> **Migration:** Run `bd migrate` to upgrade existing databases (optional - old DBs still work)
>
> Hash IDs use progressive length scaling (4/5/6 characters) with birthday paradox math to keep collisions extremely rare while maintaining human readability. See "Hash-Based Issue IDs" section below for details.

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
- 🔐 **Protected branch support** - Works with GitHub/GitLab protected branches via separate sync branch
- 🏗️ **Extensible** - Add your own tables to the SQLite database
- 🔍 **Multi-pr