<h1 align="center">
  <img src="docs/assets/logo.svg" width="52" alt="the waggle mark: a figure-eight dance with the waggle run as an arrow" align="center"> waggle
</h1>

<p align="center">
  <strong>Not a path. Not a URL. A handoff that answers back.</strong>
</p>

<p align="center">
  Locations are dumb — no per-agent shaping, no receipts, no way to fix them
  once sent. waggle's 30-byte <strong>token</strong> resolves into each
  agent's own view, <strong>counts every read</strong>, and propagates a
  correction to every holder. A path can't do that; a URL needs a server;
  this needs neither.
</p>

<p align="center">
  <a href="#the-problem">The problem</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#install">Install</a> ·
  <a href="#wire-it-into-your-harness">Harness setup</a> ·
  <a href="#by-file-type">By file type</a> ·
  <a href="#reach-local--machines--the-edge">Reach</a> ·
  <a href="#the-tmux-switchboard">Switchboard</a> ·
  <a href="docs/design/essay.md">The essay</a> ·
  <a href="paper/">The paper</a>
</p>

<p align="center">
  <img src="docs/assets/hero.svg" alt="The handoff, before and after: pasting the whole artifact to every subagent, versus handing off a 30-byte token that each consumer resolves into its own projection" width="940">
</p>

## The problem

We are entering the world of agent harnesses: Claude Code orchestrators
fanning out subagents, Codex sessions delegating in parallel, cross-vendor
agents discovering each other over open protocols. And every one of these
handoffs, today, works the same way: **forward the context and hope.**

The costs are measured, not hypothetical. Multi-agent systems consume ~15×
the tokens of a chat session — the overhead attributed by the vendor itself
to *"duplicating context across agents… and summarizing results for
handoffs,"* whose one-line summary is **"each handoff loses context."**
Roughly 37% of multi-agent failures trace to exactly this seam.

Waggle's competitor is not another protocol. It is
`"Here's /tmp/analysis.md. Use it."` — and that instinct is *correct*: a
path is a 30-byte reference, which is exactly the right size for a handoff.
But a raw path has **no attribution** (who made this, from what), **no
adaptation** (the small-context model gets the same 9,000 tokens as the
frontier model), **no lifecycle** (a stale path silently serves wrong data
forever), **no telemetry** (which subagent actually read its input? which
stalled?), and **no reach** (it dies at the machine boundary).

<p align="center">
  <img src="docs/assets/context.svg" alt="Three context windows compared: a full handoff fills the window with the artifact again; a raw path is cheap but blind; a waggle token stays small and pulls back only budgeted slices through resolve, search, and read" width="940">
</p>

Only the *string* enters the consumer's context — the artifact behind it
never travels unless something fetches it. Waggle standardizes that third
pattern and enforces its one hard rule **by type**: the token travels; the
artifact never auto-expands; `resolve`, `read`, and `search` return only the
projection or slice the consumer asked for, under byte budgets. Cheap like a
path — but the reference answers back.

## "But my subagents share a filesystem — that's already share-by-reference"

It is, and that's the smartest thing you can do without waggle. A path isn't a
copy; both agents point at the same bytes. Our benchmark's `reference` arm is
*exactly* this — a local path plus `ls`, `grep`, `open`, `pdftotext` — and with a
fair toolset it scores **90%**, competitive with waggle's 96%. If your agents are
local, the task is short, and you never need to audit anything, **use the path** —
waggle is overhead.

The distinction isn't copy-vs-reference. It's that a path is a *location*, and a
location can't answer three questions a handoff eventually has to:

- **Was it read — and which parts?** `cat` and `grep` leave no trace you can query.
  The entire "did your subagent actually read it?" check is *impossible* with a bare
  path, not just inconvenient — reading a file records nothing. Our sharpest result
  (regions read → 99% correct; skipped → 20%) exists only because reads go through
  the token.
- **Which version?** A path names *mutable* bytes. Correct the file mid-task and
  agent A read the old copy, B the new, with nothing to tell them apart — the
  divergent-copy failure, happening *with* a shared filesystem. Waggle snapshots at
  mint (content-addressed, immutable) and gives `supersede`/`revoke` with lineage.
- **Reachable from where?** `file:///…` means nothing to an agent in another
  container or at the edge. The same token resolves unchanged across all three radii.

The case for waggle is **accountability, versioning, and reach** — never that the
filesystem duplicates bytes. The moment you need to *prove* what an agent read,
survive the file changing, or hand off to something not on this box, a path runs out
and a name doesn't.

## How it w