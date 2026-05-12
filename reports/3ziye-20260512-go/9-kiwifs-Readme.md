<p align="center">
  <img src="kiwifs.png" alt="KiwiFS" width="200" />
</p>

<h1 align="center">KiwiFS</h1>

<p align="center">
  <strong>Markdown filesystem for agents and teams.</strong>
</p>

<p align="center">
  Searchable. Structured. Versioned. One binary, zero config.
</p>

<p align="center">
  <a href="https://github.com/kiwifs/kiwifs/actions/workflows/ci.yml"><img src="https://github.com/kiwifs/kiwifs/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-BSL--1.1-blue" alt="License: BSL 1.1"></a>
  <a href="https://github.com/kiwifs/kiwifs"><img src="https://img.shields.io/badge/go-1.25-00ADD8?logo=go&logoColor=white" alt="Go 1.25"></a>
  <a href="https://github.com/kiwifs/kiwifs"><img src="https://img.shields.io/badge/single_binary-yes-green" alt="Single Binary"></a>
  <a href="https://github.com/kiwifs/kiwifs"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen" alt="PRs Welcome"></a>
</p>

<p align="center">
  <a href="https://kiwifs.mintlify.app">Docs</a> · <a href="FAQ.md">FAQ</a> · <a href="ROADMAP.md">Roadmap</a> · <a href="CONTRIBUTING.md">Contributing</a>
</p>

```bash
curl -fsSL https://raw.githubusercontent.com/kiwifs/kiwifs/main/install.sh | sh
kiwifs init --root ./knowledge && kiwifs serve --root ./knowledge
# Open http://localhost:3333
```

**Or with Docker:**

```bash
docker run -p 3333:3333 -v ./knowledge:/data ameliaanhlam/kiwifs
```

---

## The problem

Markdown is the lingua franca of agents and developers — but raw `.md` files are just files. Or are they?

Current solutions fall into one of these camps:

- **Database tables pretending to be files** — no search, no versioning, no human interface. You get `read()` and `write()`, nothing else.
- **Read-only retrieval layers** — agents can search but can't write. The filesystem is a one-way mirror.
- **Flat markdown logs** — no structure, no queries, no importance scoring. The naive approach everyone outgrows.
- **Ephemeral sandboxes** — agent dies, files die. No persistence across sessions.
- **Proprietary SaaS** — locked to a vendor's ecosystem. Can't self-host, can't extend.

A real markdown filesystem needs to be all of these at once:

- **Writable** — agents write with `cat`, `echo`, `curl`, or MCP tools. Not read-only, not API-only.
- **Searchable** — full-text (BM25) and semantic (vector) over the same files.
- **Queryable** — structured queries over typed metadata, not just keyword matching.
- **Trustworthy** — every write is a Git commit. Immutable audit trail. Crash recovery. Blame.
- **Human-readable** — a web UI with wiki links, backlinks, and graph view. Not pgAdmin.

KiwiFS is all five.

```
AGENT                              HUMAN
─────                              ─────
cat /kiwi/pages/auth.md            Web UI (like Obsidian Publish
grep -r "timeout" /kiwi/             + Notion's block editor)
echo "# Report" > /kiwi/r.md      wiki links, graph view, search

       ↕                                ↕
     ┌──────────────────────────────────────┐
     │         Markdown files in folders    │
     │         (the single source of truth) │
     └──────────────────────────────────────┘
       ↕                ↕              ↕
    Git versioning   FTS5 + vector   SSE events
    (audit trail)    (search index)  (live updates)
```

## Why files, not a database

This is the core design decision. Every other choice follows from it.

**Files are the only format that is simultaneously human-readable, agent-native, and tool-agnostic.** `cat file.md` works in every shell, every container, every sandbox, every CI pipeline. No driver. No connection string. No SDK. The agent doesn't need to learn your API — it already knows the filesystem from training data.

A Postgres table is invisible to both agents and humans without custom tooling. A JSON blob requires parsing. A proprietary format requires a client library. Markdown files require nothing.

But raw files alone aren't enough. You need versioning, search, concurrency control, a web UI. KiwiFS layers database-like guarantees **on top of** files:

| Need | How KiwiFS solves it |
|---|---|
| **Versioning** | Git — every write is an atomic commit. Crash recovery, blame, diff, point-in-time restore. |
| **Search** | SQLite FTS5 (BM25 ranked) + pluggable vector search. Rebuildable from files anytime. |
| **Concurrency** | Optimistic locking via ETags (git blob hash). Standard HTTP `If-Match` / `409 Conflict`. |
| **Structured queries** | Frontmatter → SQLite `file_meta` table. Query by field, sort, filter. |
| **Audit trail** | Git commit log. SHA-1 hash chain. Tamper = broken chain. |
| **Real-time sync** | SSE broadcast on every write/delete. UI updates live. |

The files are the truth. Everything else is a derivative index you can rebuild.

> **"I already have this in Postgres."**
>
> Postgres stores your data. KiwiFS makes it *accessible* — to agents via `cat`/`grep`/NFS/S3, to humans via a web UI with wiki 