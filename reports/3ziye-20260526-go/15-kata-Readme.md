# kata カタ

Local-first issue tracking for humans and coding agents.

kata gives agents a structured place to record tasks, decisions, links,
comments, and state changes without turning GitHub Issues, markdown plans, or
chat transcripts into the source of truth.

The CLI is built for agents and automation: stable commands, JSON output, and
predictable failure modes. The TUI is built for people: browse, triage, edit,
and supervise agent-written work without reading raw JSON. Both talk to the
same local daemon and SQLite database.

Status: early public preview. The CLI, daemon, and TUI are usable, but command
contracts and UI details may still change before a stable release.

## Quick Start

```sh
go install go.kenn.io/kata/cmd/kata@latest   # or see Install for other options

cd your-repo
kata init                                         # bind this workspace to a kata project
kata create "fix login race"                      # returns the issue's short_id, e.g. abc4
kata list                                         # list open issues
kata show abc4                                    # inspect by short_id
kata close abc4 --done --message "Fixed the issue and verified the relevant tests pass." --commit <sha>
kata tui                                          # browse and triage interactively
```

See [Install](#install) for `go install`, build-from-source, and Windows
instructions; see [Working with kata](#working-with-kata) for a longer
walkthrough.

## What kata does today

What you can do:

- Track issues separately per project, with short IDs derived from each
  issue's ULID (`kata#abc4`).
- Create, list, edit, close, reopen, comment, label, assign, and link issues.
- Search, idempotent-create, soft-delete, restore, and irreversibly purge.
- Browse and triage in a TUI (`kata tui`) over the same data.
- Stream state changes as durable events for polling, live tailing, hooks, and
  TUI updates.

How it's built:

- Workspace-to-project binding lives in `.kata.toml`, falling back to a git
  remote URL when no binding file exists.
- Data lives locally in SQLite under `KATA_HOME` behind a long-running daemon.
- Issues have stable ULID `uid` values; `short_id` (the lowercased last 4+
  chars of the ULID) is the display label, qualified as `kata#abc4` across
  projects.
- `kata export` and `kata import` provide a git-friendly JSONL backup and
  schema cutover path.
- Successful commands emit JSON for reliable parsing by agents and scripts.

## Goals

Three priorities:

- Agent ergonomics: stable commands, JSON-first workflows, explicit workspace
  binding, search-before-create, idempotency keys, and predictable exit codes.
- Human oversight: a TUI that helps people browse, triage, edit, and supervise
  agent activity without reading raw JSON.
- Auditability: append-only comments, event history, actor attribution, and
  explicit destructive operations.

Longer term, kata is intended to support a shared server mode for teams, CI,
and multiple agents. That mode should be a real authenticated deployment, not
the local daemon exposed on a public interface.

## Why kata, and how is it different from Beads or git-bug?

kata is intentionally small. It is not a project-management suite, a git
workflow engine, or an agent worker pool. It is a durable task ledger that
humans and agents can both understand.

[Beads](https://github.com/gastownhall/beads) is a substantial tool in the
same space: a Dolt-powered distributed graph issue tracker for AI agents. Its
default shape is project-local: `bd init` creates a `.beads/` Dolt database
alongside the code, with native Dolt history, branching, merging, push/pull,
and optional server mode for concurrent writers. That does not mean Beads
requires git; it also supports git-free workflows.

kata makes a different architectural bet: the issue ledger should be a local
service adjacent to workspaces, not a database owned by each repository. A
repository that uses kata gets only a small, secret-free `.kata.toml` binding;
the canonical state lives in `KATA_HOME` behind a daemon API. That keeps task
state out of code history while still giving agents a structured coordination
layer and giving humans a TUI over the same event stream.

It also has a different complexity budget. Beads is a large, capable system
with distributed database semantics, merge behavior, federation, MCP
integration, and agent workflow machinery. kata is deliberately smaller: one
daemon, one local store, one HTTP API, one TUI, and a narrow issue model that
should stay easy to understand, operate, and teach to agents.

[git-bug](https://github.com/git-bug/git-bug) takes the most git-native
approach of the three: it stores issues, comments, and identities as git
objects under custom refs in the repository itself, and distributes them
through ordinary `git push` / `git pull`. Every clone carries the full issue
history offline, and bridges sync with GitHub, GitLab, and Jira. kata sits at
the other end of that spectrum — iss