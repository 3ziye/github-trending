# agentic-stack

**Keep one portable memory-and-skills layer across coding-agent harnesses, so switching tools doesn't reset how your agent works.**

A portable `.agent/` folder (memory + skills + protocols) that plugs into Claude Code, Cursor, Windsurf, OpenCode, OpenClaw, Hermes, Pi Coding Agent, Codex, Antigravity, or a DIY Python loop — and keeps its knowledge when you switch.

It also includes a local data layer so you can monitor the whole suite of
agents from one place: harness activity, cron runs, active agents, token/cost
estimates, KPI summaries, user-defined resource categories, and
screenshot-ready daily dashboards.

<p align="center">
  <img src="docs/data-layer.svg" alt="agentic-stack data layer dashboard flow" width="880"/>
</p>

And it can turn approved, redacted runs into local flywheel artifacts:
trace records, context cards, eval cases, training-ready JSONL, and readiness
metrics without training a model or sending telemetry.

<p align="center">
  <img src="docs/demo.gif" alt="agentic-stack demo" width="880"/>
</p>

<p align="center">
  <img src="docs/diagram.svg" alt="agentic-stack architecture" width="880"/>
</p>

### New in v0.16.1 — getting-started refresh

Patch release. Ships the production-ready getting-started guide from PR #49
and fixes onboarding version drift in the first-run banner.

- **Accurate install paths.** The getting-started guide now separates
  Homebrew, source checkout, and PowerShell flows so users do not expect a
  global `agentic-stack` command from a plain clone.
- **Current management commands.** The guide documents `dashboard`, `status`,
  `doctor`, `upgrade`, `sync-manifest`, `add`, `remove`, and `manage` for both
  Homebrew and source-checkout users.
- **Correct onboarding version.** The setup banner now reads the package
  version from `harness_manager.__version__` instead of showing stale release
  text.

See [CHANGELOG.md](CHANGELOG.md) for the full list.

### v0.16.0 — safe project upgrades

Minor release. Adds `agentic-stack upgrade` and `agentic-stack sync-manifest`
so installed projects can pick up new `.agent` infrastructure and skill
metadata without clobbering adapter settings or user memory.

- **Safe upgrade command.** Run `agentic-stack upgrade --dry-run` to preview
  skeleton-owned `.agent` file updates, then `agentic-stack upgrade --yes` to
  apply them.
- **Manifest repair.** Run `agentic-stack sync-manifest` to rebuild
  `.agent/skills/_manifest.jsonl` from installed `SKILL.md` frontmatter.
- **No config overwrite.** Upgrade leaves `CLAUDE.md`, `.claude/settings.json`,
  personal/semantic/episodic/working memory, candidates, and existing skill
  directories untouched.
- **Stricter doctor.** `agentic-stack doctor` now warns when Claude Code hook
  commands point to missing `.agent` files or hook scripts are present but
  unwired.

### v0.12.0 — tldraw visual canvas

Minor release. Adds an opt-in `tldraw` seed skill for live canvas diagrams and
a skill-local snapshot store. It is beta and off by default.

- **`tldraw` seed skill.** Draw, diagram, sketch, wireframe, flowchart, and
  whiteboard on a live canvas at `http://localhost:3030` through an MCP server.
- **Skill-local snapshots.** Save worthwhile canvases with
  `.agent/skills/tldraw/store.py snapshot`; list, load, and archive them later
  without treating them as a fifth memory layer.
- **Opt-in beta.** Onboarding writes `tldraw.enabled: false` by default. After
  enabling it, users manually merge `adapters/_shared/tldraw-mcp.json` into
  their harness MCP config.

### v0.11.0 — data layer + data flywheel

Added two local-first data capabilities for teams running multiple agent
harnesses against the same `.agent/` brain.

- **`data-layer` seed skill.** Generate local dashboard exports across Claude
  Code, Hermes, OpenClaw, Codex, Cursor, OpenCode, and custom loops:
  harness events, cron timelines, KPI summaries, token/cost estimates,
  categories, `dashboard.html`, and `daily-report.md`. The skill also acts as
  the injected natural-language surface for showing the terminal dashboard.
- **`data-flywheel` seed skill.** Export approved, redacted runs into trace
  records, context cards, eval cases, training-ready JSONL, and flywheel
  metrics. It is local-only and model-agnostic; it prepares artifacts but
  does not train models or call external APIs.

### v0.10.0 — design-md skill + Python 3.9 fix

Added the `design-md` seed skill for root `DESIGN.md` / Google Stitch
workflows, and fixed the Python 3.9 crash that hit macOS-default brew users
on first run.

### v0.9.1 — pi adapter fixes + tz correctness

Closed the gap between v0.9.0 and a working pi adapter, plus a timezone
sweep across every Python writer/reader so the dream cycle stops drifting
against the UTC decay window.

### v0.9.0 — harness manager

<p align="center">
  <img src="docs/harness-manager.svg" alt="harness manager v0.9.0" width="880"/>
</p>

Manifest-driven adapter system: every harness is now declared by an
`adapter