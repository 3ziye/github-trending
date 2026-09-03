<div align="center">

# unlazy

**Completion discipline for substantial AI-agent work, backed by runnable gates.**

Write the acceptance ledger first. Execute reviewed checks. Reverify returned work. Report only what the evidence supports.

[Quick start](#quick-start) | [Gate contract](#the-gate-contract) | [Orchestration](#orchestration-and-parallel-work) | [Security](#security-boundary) | [Research](#research-basis)

</div>

## Version status

The current source targets `2.1.0`. It is not identified here as a tagged GitHub release. Pin an exact commit when you need an immutable installation. See [CHANGELOG.md](CHANGELOG.md) for the unreleased change set.

## Install

Use the [skills CLI](https://github.com/vercel-labs/skills) for supported agents:

```text
npx skills add Leonxlnx/unlazy
```

Add `-g` for a user-level install or `--all` for every detected agent.

Manual locations:

```text
Claude Code:  ~/.claude/skills/unlazy
Codex CLI:    ~/.codex/skills/unlazy
```

Clone the repository into the relevant directory. Invoke it as `/unlazy` where slash skills are supported, `$unlazy` in Codex, or by a natural-language trigger from the skill description.

The core is [SKILL.md](SKILL.md). The checker and optional hook require Node 16 or newer and use no third-party runtime packages.

## Quick start

Ask for substantial work with an explicit trigger:

```text
/unlazy tree 5 refactor the payment module and verify every migration path
```

For a solo task, copy [templates/gates-leaf.md](templates/gates-leaf.md) to `GATES.md`, replace every placeholder, and inspect it without executing commands:

```text
node <path-to-skill>/scripts/gate-check.mjs --status GATES.md
```

`--status` is the only mode that is always non-executing. On a new oracle with no exact approval record, a normal run prints its resolved command, expectation, working directory, shell, and `PATH` without executing it:

```text
node <path-to-skill>/scripts/gate-check.mjs GATES.md
```

Do not treat normal mode as a permanent dry run: once the exact oracle is approved, normal mode can execute it.

`CHECK:` lines are shell code. After reading every command and called script, approve and run the ledger:

```text
node <path-to-skill>/scripts/gate-check.mjs --approve GATES.md
```

Re-run all runnable gates, including gates already marked complete:

```text
node <path-to-skill>/scripts/gate-check.mjs --reverify GATES.md
```

Use `--help` for the complete current CLI.

## The gate contract

```markdown
# Gates: pricing behavior

- [ ] G1: pricing fixtures render the expected tiers
  CHECK: node scripts/verify-pricing.mjs
  EXPECT: pricing verification passed
  EVIDENCE: pending

- [ ] G2: checkout integration succeeds from its package
  CHECK: node scripts/verify-checkout.mjs
  EXPECT: checkout verification passed
  CWD: packages/checkout
  EVIDENCE: pending
```

A runnable gate passes only when its process exits `0` and `EXPECT:` matches combined output. Evidence records the resolved shell, resolved working directory, exit status, a short `PATH` fingerprint, the match result, and a SHA-256/byte-count fingerprint of successful output. Raw successful output is neither echoed nor persisted. The pre-execution transcript shows the resolved `PATH`, capped for display. Old evidence is not re-execution; parent verification uses `--reverify`.

The parser rejects zero-gate ledgers, duplicate ids, incomplete runnable gates, invalid expectations, and abandonment with a missing reason or unknown gate id. It ignores fenced examples, preserves CRLF or LF when updating, and inserts a missing evidence line when needed. A valid abandonment is terminal handoff rather than success: the checker exits `1` with `HANDOFF REQUIRED`, and Stop allows exit while reporting qualified ids.

The checker can prove only the command oracle you declare. It cannot infer that an English title and arbitrary shell code mean the same thing. Good gates therefore:

- read the artifact or service named by the outcome
- print a success-only marker after all assertions pass
- test an absence check against a known positive control
- measure supplied figures instead of copying them into `EXPECT:`
- review consequential manual outcomes with evidence proportional to risk

Use the advisory, non-executing `scripts/gate-lint.mjs` to catch mechanically weak ledger patterns; add `--strict` when warnings should fail. Full specification: [references/gates.md](references/gates.md).

## Shell and PATH

The checker uses `--shell` first, then `UNLAZY_SHELL`, then Node's platform default shell. That default is `/bin/sh` on Unix and `process.env.ComSpec` on Windows with the platform fallback. Checks inherit the launch environment, including `PATH`.

This matters on Windows: a checker launched from Git Bash can see Unix-like tools that the same checker launched from PowerShell does not. `--shell` changes the interpreter; it does not install `grep`, `tail`, `tr`, or other external programs. Portable examples call rep