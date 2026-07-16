<p align="center">
  <img src="docs/logo.png" width="150" alt="drawio-ai-kit logo" valign="middle">
  &nbsp;&nbsp;
  <img src="docs/wordmark.svg" width="360" alt="drawio-ai-kit — the AI draws, the kit makes it right" valign="middle">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-22D3EE?style=flat-square" alt="Version 1.0.0">
  <img src="https://img.shields.io/badge/dependencies-0-2BB3A3?style=flat-square" alt="Dependencies: 0">
  <img src="https://img.shields.io/badge/skills-5-5AA9FF?style=flat-square" alt="5 domain skills">
  <img src="https://img.shields.io/badge/node-%E2%89%A518-B98CF0?style=flat-square" alt="Node ≥18">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-F59E0B?style=flat-square" alt="License: MIT"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-ff69b4?style=flat-square" alt="PRs welcome"></a>
</p>

An orchestration and validation framework enabling AI agents to generate **structurally precise and aesthetically standardized** draw.io diagrams, optimized for AWS, Azure & GCP architectures.

It mitigates common AI agent hallucinations (such as generating non-existent stencil IDs that result in empty shapes) using three key components:

1. **Declarative Catalog** — A single source of truth mapping draw.io stencil IDs (`mxgraph.aws4.*`) to their respective taxonomies and canonical color palettes.
2. **Design Principles** — Codified architectural and layout rules (`rules/principles.md`).
3. **Structural Validator** — A static analysis engine that audits diagram XML to guarantee stencil references are valid and design principles are satisfied prior to serialization.

Exposed to the AI via the **zero-dependency `drawio-ai` CLI**.

## Showcase

One diagram per platform — all generated end-to-end by the kit: no hand-placed coordinates, real stencils, validated, vision-checked. Full set in [`examples/`](examples/).

<p align="center"><img src="docs/gallery.png" width="900" alt="Gallery — AWS Multi-AZ · Databricks Data Intelligence Platform · Azure hub-spoke landing zone · GCP Shared VPC landing zone"></p>

## Quick start

Full install — the CLI plus all 5 Domain Skills (AWS, Azure, GCP, Databricks, BPMN) — in one line:

```bash
npm i -g github:sparklabx/drawio-ai-kit && npx skills add sparklabx/drawio-ai-kit
```

Restart your agent, then try: *"draw an AWS 3-tier web app"*.

The first command puts the `drawio-ai` binary on PATH (installs straight from
GitHub — not yet on the npm registry; see [INSTALL.md](INSTALL.md) to pin a version
or install from a clone). The second registers the Domain Skills with your agent
(the `skills` CLI auto-detects Claude Code, Codex, Gemini CLI, …) — without it the
agent never picks the kit up on its own.

- Just one domain instead: `npx skills add sparklabx/drawio-ai-kit --skill drawio-aws` (`--list` previews all 5)
- Optional, for the full experience: the **draw.io desktop app** enables `drawio-ai render` (the vision self-check); **Graphviz** enables `vendor/autolayout.py` for large graphs. Details in [INSTALL.md](INSTALL.md).

## Is it safe to install?

Short answer: yes — and you don't have to take my word for it.

- **No hidden code.** No `postinstall` (or any lifecycle) hooks — nothing runs on `npm install`. Zero runtime dependencies. **No `sudo`, no `curl | bash`, no remote code.**
- **Zero runtime dependencies.** The single dependency (`@modelcontextprotocol/sdk`) was removed at 1.0.0. The package is now fully self-contained.
- **Runs locally, no telemetry.** The CLI only reads/writes local files. The single optional outbound call is icon-logo fetching from public CDNs (lobe-icons), and it's opt-in.
- **Easy to undo:**

```bash
npm uninstall -g drawio-ai-kit              # remove the CLI
npx skills remove drawio-aws              # remove a domain skill (repeat for each)
```

- **Updating** — two independent channels:

```bash
npm i -g github:sparklabx/drawio-ai-kit   # CLI/engine (icon search, workflow, validator, rules)
npx skills update                         # the Domain Skills (SKILL.md) — always pulls latest
```

The skills are thin frontends that call `drawio-ai` at runtime, so engine fixes reach you the
moment you update the CLI — no skill re-install needed. `npx skills update` only refreshes the
SKILL.md text. Pin a specific release with `github:sparklabx/drawio-ai-kit#v1.0.1`.

To report a security issue, see [`SECURITY.md`](SECURITY.md).

## Build a diagram — declarative, no hardcoded coordinates

Define a diagram **topology** (`pipeline`/`hierarchy`/`network`/`hubspoke`/`hybrid`/`mesh`/`sequence`), declare the **nested structure**, and the layout engine programmatically computes spatial coordinates (x/y/w/h) — frames auto-size to fit their children, while rows and columns auto-space. You define the logical topology, not raw pixels.

```js
import { Diagram } from "./src/builder.mjs";
import { group, icon, box, renderTree } from "./src/layout-engine.mjs";

const 