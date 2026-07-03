<p align="center">
  <img src="https://github.com/modiqo/skillspec/raw/main/assets/skillspec-wordmark.svg" alt="SkillSpec" width="520">
</p>

# Skills that agents can actually follow

[![CI](https://github.com/modiqo/skillspec/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/modiqo/skillspec/actions/workflows/ci.yml)

You wrote a good `SKILL.md`. But did the agent actually follow it, or skip the
late safety rule, grab an undeclared tool, and report "done" with no proof?

**SkillSpec tells you.** Run one command and get a risk report. Then turn any
skill into a contract the agent has to follow, with a record you can inspect at
the end.

No new agent runtime. No orchestration platform. Just a CLI and a small
`skill.spec.yml` that lives next to your `SKILL.md`.

<p align="center">
  <a href="https://github.com/modiqo/skillspec/blob/main/assets/skillspec-layer-stack.svg">
    <img src="https://raw.githubusercontent.com/modiqo/skillspec/main/assets/skillspec-layer-stack.svg" alt="SkillSpec sits inside the skills layer" width="1100">
  </a>
</p>

## See It In 30 Seconds

Point Doctor at any skill, a local folder or a public GitHub URL:

```bash
skillspec doctor ./my-skill
```

```text
SkillSpec Doctor
================
Target: ./my-skill        Shape: simple_skill

Agent follow-through risk: HIGH (74/100)

Findings
- description is short and generic -> automatic discovery may be unreliable
- active skill load is 8,482 tokens -> above the balanced target
- 14 must/never obligations appear after 60% of the body -> easy to miss
- tools and commands are used, but dependencies are never declared
- no tests and no progress/trace surface -> "done" can't be checked

Likely consequence
An agent may follow the broad task but skip a late safety gate, use an
undeclared tool, or claim completion without evidence.

Next step
Ask your agent: /skillspec import ./my-skill, compile it, test it, install it,
and print the alignment summary.
```

No install required to try it. Paste a public skill URL into the hosted page:

**<https://skillspec.sh/>**

## Why This Exists

A `SKILL.md` is just text. The harness loads it and hopes the model reads the
right part. For a throwaway skill, that can be fine. For a skill you rely on,
"hope" is not a plan:

- **Buried rules get skipped.** The important "never do X" sits at line 400,
  and models are most reliable at the start and end of context, not the middle.
- **Every miss grows the prose.** Each failure becomes another paragraph, which
  makes the next miss more likely.
- **You only see the final answer.** There is no durable record of which route
  ran, which steps happened, or what was skipped.

SkillSpec moves the load-bearing parts out of prose and into a small structured
contract:

- when to use the skill
- which route to take
- what is forbidden
- what dependencies must exist
- what checks must pass
- what proof should exist at the end

## Install

Install the CLI:

```bash
curl -fsSL https://skillspec.sh/install.sh | sh
skillspec --version
```

Or with Cargo:

```bash
cargo install skillspec
skillspec --version
```

Then add the plugin to your harness.

Claude Code:

```bash
claude plugin marketplace add modiqo/skillspec --sparse .claude-plugin plugins/skillspec
claude plugin install skillspec@skillspec
claude plugin list
```

Codex:

```bash
codex plugin marketplace add modiqo/skillspec --ref main --sparse .agents --sparse plugins/skillspec
codex plugin add skillspec@skillspec
```

<details>
<summary>Other platforms, pinned releases, direct downloads, and local development</summary>

Prebuilt binaries are available on the
[releases page](https://github.com/modiqo/skillspec/releases):

- `skillspec-macos.tar.gz`
- `skillspec-linux-x86_64.tar.gz`
- `skillspec-windows-x86_64.zip`

Release artifacts include `.sha256` checksums. The installer verifies the
checksum and writes to `~/.local/bin` by default.

Pin a version or choose an install directory:

```bash
curl -fsSL https://skillspec.sh/install.sh \
  | SKILLSPEC_VERSION=v0.1.0 SKILLSPEC_INSTALL_DIR="$HOME/.local/bin" sh
```

Install unreleased `main`:

```bash
cargo install --git https://github.com/modiqo/skillspec --package skillspec --force
skillspec --version
```

Install from a local checkout:

```bash
cargo install --path crates/skillspec-cli --force
skillspec --version
```

Local development can also install the skill folder directly:

```bash
# Codex
skillspec install skill skills/skillspec --target codex --retire-existing

# Agents
skillspec install skill skills/skillspec --target agents --retire-existing

# Claude local project
skillspec install skill skills/skillspec --target claude-local --retire-existing
```

For day-to-day development, the repository includes a `Justfile` that keeps the
crate split and local harness install flow in one place:

```bash
# Show the local crate hierarchy and dependency direction.
just packages

# Build every workspace package.
just build-debug
just build-release

# Instal