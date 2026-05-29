# harness-experimental

Turn any software repo into an agent-ready workspace.

`harness-experimental` is a repository-level operating harness for Claude Code,
Codex, Cursor, and other coding agents. It gives agents the missing project
context they need before they change code: where to start, what the product
contract says, how risky the work is, what proof is required, and which
decisions future agents should inherit.

The app is what users touch. The harness is what agents touch.

## Why Star This Repo

Star this repo if you want practical, reusable patterns for making AI-assisted
software development more reliable, inspectable, and easier for humans to steer.

This project is exploring a simple idea:

> Coding agents do not only need better prompts. They need better repositories.

## The Problem

Most repos are built for humans reading code in a familiar codebase. Coding
agents usually enter with only a chat prompt and a shallow snapshot of files.
That leads to common failure modes:

- The agent edits code before understanding product intent.
- Important constraints live only in chat history or in someone's head.
- Validation expectations are vague or discovered too late.
- Architecture tradeoffs are repeated instead of inherited.
- Large requests do not get broken into reviewable story-sized work.

## The Harness Approach

A repository starts to have a harness when it helps an agent answer practical
engineering questions without relying only on chat history:

- What should I read first?
- What type of work is this?
- Which product contract does it affect?
- How risky is the change?
- What proof will show the work is done?
- What decision or lesson should future agents inherit?

In this repo, those answers live in:

- `AGENTS.md` — the stable agent shim with local project notes and Harness
  doc links.
- `docs/HARNESS.md` — the human-agent collaboration model.
- `docs/FEATURE_INTAKE.md` — tiny, normal, and high-risk work classification.
- `docs/ARCHITECTURE.md` — architecture discovery and boundary rules.
- `docs/TEST_MATRIX.md` — behavior-to-proof validation expectations.
- `docs/stories/` — story packets and backlog items.
- `docs/decisions/` — durable decisions and tradeoffs.
- `docs/templates/` — reusable spec, story, decision, and validation templates.

OpenAI describes this shift as an agent-first world where humans steer and
agents execute:

https://openai.com/index/harness-engineering/

## Install Harness Into A Project

From a target project directory, run:

```bash
curl -fsSL "https://raw.githubusercontent.com/hoangnb24/harness-experimental/main/scripts/install-harness.sh?$(date +%s)" | bash -s -- --yes
```

If the target already has `AGENTS.md`, `docs/`, or `scripts/`, choose one:

```bash
# Update an existing Harness repo without moving existing files
curl -fsSL "https://raw.githubusercontent.com/hoangnb24/harness-experimental/main/scripts/install-harness.sh?$(date +%s)" | bash -s -- --merge --yes

# Back up and replace AGENTS.md, docs/, and scripts/
curl -fsSL "https://raw.githubusercontent.com/hoangnb24/harness-experimental/main/scripts/install-harness.sh?$(date +%s)" | bash -s -- --override --yes
```

Use `--merge` when a project already has Harness and you want to append newly
added Harness files without moving the existing `AGENTS.md`, `docs/`, or
`scripts/` paths into backup. Existing files stay untouched; only missing
Harness files are created.

For older Harness installs whose `AGENTS.md` still contains the full generated
operating guide, refresh it into the small stable shim:

```bash
curl -fsSL "https://raw.githubusercontent.com/hoangnb24/harness-experimental/main/scripts/install-harness.sh?$(date +%s)" | bash -s -- --merge --refresh-agent-shim --yes
```

The refresh backs up the existing file. If it detects the old
Harness-generated guide, it replaces it with the shim. If the file appears
custom, it appends or updates a marked Harness block instead of overwriting the
project's local instructions.

Or install into a specific path:

```bash
curl -fsSL "https://raw.githubusercontent.com/hoangnb24/harness-experimental/main/scripts/install-harness.sh?$(date +%s)" | bash -s -- --directory /path/to/project --yes
```

Use `--dry-run` to preview changes before writing files.

The installer also downloads the prebuilt Harness CLI for the current platform,
verifies its `.sha256` checksum, and installs it at
`scripts/bin/harness-cli`. The Rust CLI is the main Harness tool. Installed
projects keep `scripts/harness` as the stable command path, and that entrypoint
uses the Rust binary for normal Harness work.

Harness CLI release assets are published from tags by the
`Harness CLI Release` GitHub Actions workflow. The installer expects each
release to include `harness-cli-<platform>` and
`harness-cli-<platform>.sha256` assets for macOS arm64, macOS x64, Linux x64,
and Linux arm64.

## Try The Flow

The fastest way to understand the harness is to inspect the tiny demo:

- `docs/demo/README.md`: sho