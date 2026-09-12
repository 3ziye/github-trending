# dsh-anchored-standard

[中文说明](./README.zh-CN.md)

Experimental DeepSeek Harness agent presets — a base mode, two live-anchor
variants, and one seeded prefab mode — that anchor a session's model trajectory
on the Minimal condition
(real Minimal tool schema, no auto-injected context), then promote to a small
resident catalog once the session is durable, unlocking heavier Standard tools
on demand.

This is a community project. It is not an official DeepSeek preset and is not
affiliated with or endorsed by DeepSeek.

The project is frozen — new issues and pull requests are no longer accepted (see
[Project status](#project-status-frozen-2026-09-10)). For ideas for new plugins or useful
findings, please submit them under the
[repository](https://github.com/0liveiraaa/DeepseekCotexplorations).

## Project status (frozen 2026-09-10)

**This project is frozen.** On 2026-09-10 DeepSeek released V4.1 Flash and announced that
V4 Pro — the model these presets were measured on and tuned for — is retired on
2026-09-14 12:00, with its traffic routed to V4.1 Flash. The presets exist to re-anchor a
trajectory that the successor does not appear to need patched: the flash family anchored
under every condition in our first-round dose-response probes (32/32), which is why the
project never tuned for it. V4.1 Flash's own first-round trajectory has NOT been measured
(no API budget in maintenance mode), so treat that as an inference from the earlier
flash data, not a result. The model the work was built around is going away, so the
maintenance period ends here. **New issues and pull requests are no longer accepted or
handled.** The repository stays online with its history, data and acknowledgement record
intact.

This is the ending [`FAREWELL.md`](./FAREWELL.md) asked for: "let the next model eat more
diverse harness environments during training, so that patch engineering like this is no
longer necessary." That file now ends with a closing note written by the successor model
itself, V4.1 Flash. What stays valid is the model-agnostic part — the `context-gate`
unified injection control, the prefab pipeline, the discovery-tool dose-response data, and
the general observation that the API-visible surface conditions the trajectory. Research
material remains open in
[DeepseekCotexplorations](https://github.com/0liveiraaa/DeepseekCotexplorations).

Earlier status (2026-08-17, kept for the record): following the price increases on both the
DeepSeek official API and the opencode go subscription, active development had already
stopped — the evaluation loops these presets depend on (Project2-class runs and multi-trial
roll/probe experiments) were no longer affordable, leaving the repository in **maintenance
only** mode (bug fixes and harness-compatibility updates when feasible). A personal note
from the maintainer: [FAREWELL.md](./FAREWELL.md) (Chinese). Contributors and collaborators
are listed in [ACKNOWLEDGEMENTS.md](./ACKNOWLEDGEMENTS.md).

Community projects that users report perform better in some scenarios, plus
ecosystem tooling built around these presets:

- [dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) — a runtime injector
  plus task-aware thinking-mode routing presets (the router-standard family).
- [J-Space Cognition Suite](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.6)
  — a model-agnostic inference-time cognitive control layer packaged as a Skill.
- [both-anchored (auto-b7n)](https://github.com/0liveiraaa/DeepseekCotexplorations/tree/main/contributions/andyzheng0715-v4pro-anchored-both/) —
  an independently developed two-phase anchored preset: no first-request output
  cap, no promotion gate, promotion on the first durable `tool/call` or
  `assistant/message`, with the full PTC SDK kept intact via post-promotion wire
  trimming (the #85 feedback and experiment data live in the research repository,
  with sample sizes and boundary caveats stated in the original contribution).
- [dsh-recovery](https://github.com/AndyZHENG0715/dsh-recovery) — a zero-dependency
  self-healing CLI plus watchdog plugin: broken-preset quarantine/rollback,
  safe-mode whitelists, and boot probes.

## Modes at a glance

| Mode | Directory | First model request | Anchor mechanism | Promotion signal | Cost |
|---|---|---|---|---|---|
| Anchored Standard | `preset/` | 2 tools (the Minimal pair) | Minimal tool schema | first durable `tool/call` **or** `assistant/message` (`promoteOn: either`) | none |
| Zero-Anchored Standard | `zero-anchored-standard/` | 0 tools | one fixed anchor turn | the anchor reply (`assistant/message`) | +1 model call |
| Whoami Standard | `whoami-standard/` | 0 tools | one "你是谁" self-introduction turn | the self-introduction reply (`assistant/message`) | +1 model call |
| Prefab Anchored Standard | `prefab/` | seeded rolled history | bundled successful trajectory | already promoted in the seed | no model call to instantiate |
| Eternal Minimal | `eternal-minimal/` | 2 tools, forever | the v