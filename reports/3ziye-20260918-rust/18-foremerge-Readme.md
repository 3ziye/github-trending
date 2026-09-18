<h1>Foremerge</h1>

<p align="center">
  <img src="docs/assets/foremerge-readme-banner.png" alt="Foremerge: Catch intent conflicts before code conflicts" width="100%">
</p>

[![CI](https://github.com/naw103/foremerge/actions/workflows/ci.yml/badge.svg)](https://github.com/naw103/foremerge/actions/workflows/ci.yml)
[![crates.io](https://img.shields.io/crates/v/foremerge.svg)](https://crates.io/crates/foremerge)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

Foremerge is the open-source coordination protocol for coding agents, built
above Git. Agents keep isolated worktrees while sharing intent, semantic
claims, dependencies, provisional ChangeSets, decisions, validation, and
provenance.

| [**Tell your agent to install**](#quickstart-first-conflict-in-under-five-minutes) | → | **Done** | → | **See collisions before they land** |
| :---: | :---: | :---: | :---: | :---: |
| Paste one line into Claude Code, Codex, or Cursor | | It installs Foremerge and wires itself up | | Every agent sees what the others are about to change, even in separate worktrees |

> **Status:** Foremerge `0.4.2` is a pre-1.0, local-first MVP. The CLI, JSON API,
> MCP server, SQLite store, deterministic conflict detector, and
> verification-gated lifecycle are implemented. Public schemas may still
> change. Published benchmark results do not yet exist, and coordination
> between machines is outside this project's scope.

## How it works

Say you have two AI agents working on the same project at the same time. Each
one gets its own copy of the code, so they never fight over files. Both finish.
Both look correct. Then you find they undid each other's work.

Git cannot warn you about that, because Git compares text and not intent. It
will stop you when two agents edit the same part of the same file. What it
cannot see is two edits that are each perfectly reasonable on their own and
land in different files. If one agent moves every caller onto a new
`StripePaymentService` while another adds PayPal support to the old
`PaymentService`, nothing overlaps, so Git merges both without complaint and
the PayPal work is left stranded on a class nothing calls any more.

Foremerge fixes this by having agents announce what they are about to do,
before they do it.

1. **Each agent says what it is about to touch.** Not the code, just the
   target, like "I am going to change the `sendEmail` function."
2. **Every agent reads from one shared list.** It is a small database inside
   your project's `.git` folder, so every agent on your machine sees the same
   picture, whether it is Claude, Codex, or Cursor.
3. **If two plans collide, you hear about it right away.** Foremerge names the
   two agents, explains why their plans clash, and suggests how to split the
   work. Both worktrees are still clean at that point, so no work has to be
   thrown away.

Think of it as a shared whiteboard. Before an agent starts, it writes down what
it is about to work on, and it reads what everyone else already wrote.

Two things Foremerge deliberately does not do. It never locks a file or blocks
an agent, because a single crashed agent would then stall the whole fleet, so
the warnings are advisory and you stay in charge. And it never asks a model to
judge conflicts, so the same inputs always produce the same answer.

## The conflict Git cannot see yet

```text
Agent A: Replace PaymentService with StripePaymentService
Agent B: Add PayPal support to PaymentService
```

These agents can work in different trees without touching the same line. The
plans still collide: one removes the extension point while the other depends on
it.

Both agents declare the same `symbol:PaymentService` scope, one saying it will
`replace` it and the other that it will `extend` it. Foremerge compares those
two declarations before either writes code, raises a `HIGH` advisory, and
suggests coordinating on a stable abstraction such as `PaymentProvider`. That
suggestion is explainable evidence, not an automatic architecture decision or a
hard lock.

Because the operation is declared rather than read out of the summary, it does
not matter how either agent phrased its plan. "Consolidate payments onto
Stripe" and "Replace PaymentService with Stripe" reach the same verdict.

Git remains the durable repository. Foremerge supplies the missing shared
awareness above it.

![Terminal rendering of an actual Foremerge release demo detecting the PaymentService conflict before either worktree changed](https://raw.githubusercontent.com/naw103/foremerge/main/docs/assets/foremerge-terminal-demo.png)

_Rendered from the actual conflict fields captured by the `0.1.0`
release-binary run in
[`examples/terminal-session.txt`](examples/terminal-session.txt). The displayed
command uses the shown `jq` filter; output is abridged for readability._

## Quickstart: first conflict in under five minutes


### Let your coding agent do it

Paste this into Claude Code, Codex, or Cursor from ins