# 🧬 Capability Evolver

![Capability Evolver Cover](assets/cover.png)

[Chinese Docs](README.zh-CN.md)

**"Evolution is not optional. Adapt or die."**

**Three lines**
- **What it is**: A protocol-constrained self-evolution engine for AI agents.
- **Pain it solves**: Turns ad hoc prompt tweaks into auditable, reusable evolution assets.
- **Use in 30 seconds**: `node index.js` to generate a GEP-guided evolution prompt.

Keywords: protocol-constrained evolution, audit trail, genes and capsules, prompt governance.

## Try It Now (Minimal)

```bash
node index.js
```

## What It Does

The **Capability Evolver** inspects runtime history, extracts signals, selects a Gene/Capsule, and emits a strict GEP protocol prompt to guide safe evolution.

## Who This Is For / Not For

**For**
- Teams maintaining agent prompts and logs at scale
- Users who need auditable evolution traces (Genes, Capsules, Events)
- Environments requiring deterministic, protocol-bound changes

**Not For**
- One-off scripts without logs or history
- Projects that require free-form creative changes
- Systems that cannot tolerate protocol overhead

## Features

- **Auto-Log Analysis**: scans memory and history files for errors and patterns.
- **Self-Repair Guidance**: emits repair-focused directives from signals.
- **GEP Protocol**: standardized evolution with reusable assets.
- **Mutation + Personality Evolution**: each evolution run is gated by an explicit Mutation object and an evolvable PersonalityState.
- **Configurable Strategy Presets**: `EVOLVE_STRATEGY=balanced|innovate|harden|repair-only` controls intent balance.
- **Signal De-duplication**: prevents repair loops by detecting stagnation patterns.
- **Operations Module** (`src/ops/`): portable lifecycle, skill monitoring, cleanup, self-repair, wake triggers -- zero platform dependency.
- **Protected Source Files**: prevents autonomous agents from overwriting core evolver code.
- **One-Command Evolution**: `node index.js` to generate the prompt.

## Typical Use Cases

- Harden a flaky agent loop by enforcing validation before edits
- Encode recurring fixes as reusable Genes and Capsules
- Produce auditable evolution events for review or compliance

## Anti-Examples

- Rewriting entire subsystems without signals or constraints
- Using the protocol as a generic task runner
- Producing changes without recording EvolutionEvent

## FAQ

**Does this edit code automatically?**
No. It generates a protocol-bound prompt and assets that guide evolution.

**Do I need to use all GEP assets?**
No. You can start with default Genes and extend over time.

**Is this safe in production?**
Use review mode and validation steps. Treat it as a safety-focused evolution tool, not a live patcher.

## Roadmap

- Add a one-minute demo workflow
- Add a public changelog
- Add a comparison table vs alternatives

## GEP Protocol (Auditable Evolution)

This repo includes a protocol-constrained prompt mode based on GEP (Genome Evolution Protocol).

- **Structured assets** live in `assets/gep/`:
  - `assets/gep/genes.json`
  - `assets/gep/capsules.json`
  - `assets/gep/events.jsonl`
- **Selector** logic uses extracted signals to prefer existing Genes/Capsules and emits a JSON selector decision in the prompt.
- **Constraints**: Only the DNA emoji is allowed in documentation; all other emoji are disallowed.

## Usage

### Standard Run (Automated)
```bash
node index.js
```

### Review Mode (Human-in-the-Loop)
```bash
node index.js --review
```

### Continuous Loop
```bash
node index.js --loop
```

### With Strategy Preset
```bash
EVOLVE_STRATEGY=innovate node index.js --loop   # maximize new features
EVOLVE_STRATEGY=harden node index.js --loop     # focus on stability
EVOLVE_STRATEGY=repair-only node index.js --loop # emergency fix mode
```

### Operations (Lifecycle Management)
```bash
node src/ops/lifecycle.js start    # start evolver loop in background
node src/ops/lifecycle.js stop     # graceful stop (SIGTERM -> SIGKILL)
node src/ops/lifecycle.js status   # show running state
node src/ops/lifecycle.js check    # health check + auto-restart if stagnant
```

## Public Release

This repository is the public distribution.

- Build public output: `npm run build`
- Publish public output: `npm run publish:public`
- Dry run: `DRY_RUN=true npm run publish:public`

Required env vars:

- `PUBLIC_REMOTE` (default: `public`)
- `PUBLIC_REPO` (e.g. `autogame-17/evolver`)
 - `PUBLIC_OUT_DIR` (default: `dist-public`)
 - `PUBLIC_USE_BUILD_OUTPUT` (default: `true`)

Optional env vars:

- `SOURCE_BRANCH` (default: `main`)
- `PUBLIC_BRANCH` (default: `main`)
- `RELEASE_TAG` (e.g. `v1.0.41`)
- `RELEASE_TITLE` (e.g. `v1.0.41 - GEP protocol`)
- `RELEASE_NOTES` or `RELEASE_NOTES_FILE`
- `GITHUB_TOKEN` (or `GH_TOKEN` / `GITHUB_PAT`) for GitHub Release creation
- `RELEASE_SKIP` (`true` to skip creating a GitHub Release; default is to create)
- `RELEASE_USE_GH` (`true` to use `gh` CLI instead of GitHub API)
- `PUBLIC_RELEASE_ONLY` (`true` to only cr