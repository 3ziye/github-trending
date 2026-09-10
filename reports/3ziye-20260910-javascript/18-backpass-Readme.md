<h1 align="center">backpass</h1>
<p align="center">
  <a href="https://github.com/kunchenguid/backpass/actions/workflows/ci.yml"
    ><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/kunchenguid/backpass/ci.yml?style=flat-square&label=ci"
  /></a>
  <a href="https://github.com/kunchenguid/backpass/actions/workflows/release-please.yml"
    ><img alt="Release" src="https://img.shields.io/github/actions/workflow/status/kunchenguid/backpass/release-please.yml?style=flat-square&label=release"
  /></a>
  <a href="https://www.npmjs.com/package/backpass"
    ><img alt="npm" src="https://img.shields.io/npm/v/backpass?style=flat-square"
  /></a>
  <a href="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-blue?style=flat-square"
    ><img alt="Platform" src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-blue?style=flat-square"
  /></a>
  <a href="https://x.com/kunchenguid"
    ><img alt="X" src="https://img.shields.io/badge/X-@kunchenguid-black?style=flat-square"
  /></a>
  <a href="https://discord.gg/Wsy2NpnZDu"
    ><img
      alt="Discord"
      src="https://img.shields.io/discord/1439901831038763092?style=flat-square&label=discord"
  /></a>
</p>

<h3 align="center">Gradient descent for your agent memory.</h3>

Your `AGENTS.md` is a set of weights. Every agent session is a forward pass. The
transcript that session leaves on disk is the loss signal - and today nothing reads it.
The loop only closes when a human happens to remember a failure and edits the file by hand.

`backpass` closes it. It finds the agent sessions that actually ran in your repo, reads
what happened in them, and proposes evidence-backed edits to your memory surface - the
memory file and project skills - under a token budget, gated by you.

- **Local-first** - Reads the transcript stores of seven agent harnesses directly from disk.
  No API, no upload; transcripts never leave your machine except into an agent you already
  authenticated, and obvious secrets are redacted before they do.
- **Evidence-gated** - Every proposed edit carries verbatim quotes from real sessions,
  and every `add`, `rewrite`, or `remove` edit needs evidence from at least two distinct
  sessions. Small, noisy, bounded steps - not a rewrite.
- **Human in the loop** - Analysis never writes. `backpass apply` is the only writing
  command, and it shows each edit with its evidence for you to accept or reject.

```
AGENTS.md / CLAUDE.md + skills (the weights)
  → agent session               (forward pass)
  → transcript on disk          (loss signal)
  → backpass: collect samples, distill, calculate loss, aggregate gradients
  → backpass: gradient descent  (diffs + skill extractions)
  → you accept or reject        (the human gate)
  → back to the weights
```

One run is one bounded gradient step.

## Quick Start

```sh
npm install -g backpass
# or run it without installing
npx backpass
```

Requires **Node >= 22.5** and [`acpx`](https://github.com/openclaw/acpx) on your PATH.

backpass has **no API keys of its own**. Every model call goes through acpx to a harness
you have already authenticated.

```sh
cd your-repo
backpass init      # write .backpassrc.json, exclude .backpass/ via .git/info/exclude
backpass           # collect samples → calculate loss → aggregate gradients → gradient descent (never writes)
backpass apply     # review each edit, accept or reject, then write
```

### User-level memory

A run is one scope. The default is the checkout you are in. `backpass --scope user`
trains the always-loaded user file and user-level skills from Claude Code and Codex
sessions across projects, and writes only those files. A project-scoped run never
writes a user-level file.

Canonical user memory is the first existing file in this order: `~/.agents/AGENTS.md`,
`$CLAUDE_CONFIG_DIR/CLAUDE.md` (default `~/.claude/CLAUDE.md`), and
`$CODEX_HOME/AGENTS.md` (default `~/.codex/AGENTS.md`). User-level skill extractions
default to `~/.agents/skills`, with a warning if Claude's active `skills` path is a
real directory rather than the usual symlink. See [Configuration](#configuration) for
using an existing harness-loaded directory instead.

In user scope every `add`, `rewrite`, or `remove` edit also clears `minGapProjects`
(default `1`): the distinct projects behind its own quotes, counted from the gap
clusters it cites and from the session-to-project map behind the instruction evidence
rows. `extract` and `move` edits remain exempt.

State lives in `$XDG_CONFIG_HOME/backpass/user/` (default
`~/.config/backpass/user/`) with mode 0700, isolated from every project's
`.backpass/`. User-scope evidence, ledgers, proposals, and apply surfaces stay in
that one directory.

Harness load paths, verified for v1:

- **Claude Code** loads `CLAUDE.md` from `CLAUDE_CONFIG_DIR` (default `~/.claude`)
  and inlines `@` imports, including `~/` and absolute paths. A CLAUDE.md containing
  only an import that resolves to the canonical user memory is a valid pointer, su