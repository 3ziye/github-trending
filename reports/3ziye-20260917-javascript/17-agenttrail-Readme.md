<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/brand/agenttrail-mark-dark.svg">
  <img src="assets/brand/agenttrail-mark-black.svg" alt="agenttrail" width="96">
</picture>

# agenttrail

**Local observability for AI coding agents.**

[![Kitchen on npm](https://img.shields.io/npm/v/agenttrail-kitchen?color=e9a23b&label=kitchen%20on%20npm)](https://www.npmjs.com/package/agenttrail-kitchen)
[![Map on npm](https://img.shields.io/npm/v/agenttrail?color=e9a23b&label=map%20on%20npm)](https://www.npmjs.com/package/agenttrail)
[![Kitchen checks](https://github.com/sodiumsun/agenttrail/actions/workflows/kitchen.yml/badge.svg)](https://github.com/sodiumsun/agenttrail/actions/workflows/kitchen.yml)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

</div>

Agenttrail watches your coding agents' available activity and turns it into a live view of their work. See which part of a project is changing, what tasks an agent has reported, and where it needs your attention—without piecing together several terminal windows.

Your agents keep running in tools such as Codex and Claude Code. Agenttrail observes local files, plans and supported agent events; it visualizes that evidence for you. It does not run the agents, assign their work or decide that a task is finished.

## One project, two views

**Agenttrail** is the open-source project. **Map** and **Kitchen** are its two views:

| | Agenttrail Map | Agenttrail Kitchen |
| --- | --- | --- |
| Helps you follow | Project structure, progress and which components are changing | Current tasks, role contributions and completed work |
| Visualizes work as | Components, dependencies, file activity and session trails | Chefs, order tickets, cooking and deliveries |
| Main sources | `PLAN.md`, file changes and optional Claude Code hooks | Available native todos, local Codex/Claude activity and optional Claude/Cursor hooks |
| Start in your repo | `npx agenttrail` | `npx agenttrail-kitchen .` |
| Plan needed? | Optional for file activity; needed for the component map | Optional; native todos supply order tickets when available |

Choose Map for the project overview and Kitchen to follow the work as a shared cooking scene. Each runs independently in your browser. They currently have separate local services and provider adapters; Kitchen can also read a running Map's context. Their activity coverage and history are not identical. [How observability works](docs/OBSERVABILITY.md)

## Agenttrail Kitchen

[![Agenttrail Kitchen overview: six project responsibilities working together, with shared dishes and a delivery conveyor](docs/kitchen/overview.jpg)](docs/kitchen/README.md)

*Recorded while real Codex and Claude sessions built a small 3D maze game. Chefs represent responsibilities, not necessarily separate agent processes.*

## Run Kitchen in your repo

You need **Node.js 20+**, a browser with WebGL, and a local project folder. Run this in the repo you want to watch:

```bash
npx agenttrail-kitchen .
```

The browser opens at **localhost:4780** (or the next free port). Keep this terminal open and keep working in your coding agent. Codex and Claude Code activity is discovered from available local logs. No `PLAN.md`, Agenttrail Map installation, copied files, API key or new agent session is required for basic observation. The watcher does not launch agents or edit your repo.

**Want to see it before connecting an agent?** Add `--example` to the command, then click **Next example step**. This is a labeled, scripted example. Click **Live** to return to your real repo.

**This is a public experimental preview.** The npm package includes the graphics and fonts, so users do not need a build step. To pin this release, use `npx agenttrail-kitchen@0.1.0-alpha.3 .`. The separate `npx agenttrail` command opens the Map.

[Kitchen guide](docs/kitchen/README.md) · [Connect agents and troubleshoot](docs/kitchen/CONNECTING.md) · [Release and verification](docs/kitchen/RELEASE.md)

## Watch the work become dishes

![Real recorded cooking and handoffs, with camera close-ups to show the agents working together](docs/kitchen/cooking.gif)

| In the kitchen | In your project |
| --- | --- |
| Chef | A project responsibility; the actual provider and session remain inspectable |
| Ticket / dish | An available native todo, with its own wording and status |
| Cooking | Observed work associated with that responsibility |
| Several chefs on one ticket | Contributions from roles or sessions associated with the same todo |
| Plate transfer | Explicit artifact revision and receipt metadata |
| Delivery conveyor | A native todo reported complete |

One session can move between several chefs as its work changes. Roles adapt to the project; you can refine them with an optional [workflow configuration](examples/kitchen-workflow). Multiple kitchens organize larger workflows. Click a chef or ticket to inspect its evidence.

**What happens automatically:** lo