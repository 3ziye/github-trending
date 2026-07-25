<div align="center">

<img src="assets/logo.svg" width="112" height="112" alt="img2threejs logo" />

# img2threejs

**Rebuild the object in a reference image as a code-only, procedural Three.js model.**

Quality-gated, animation-ready, and deliberately token-efficient — reconstruction-by-code, not photogrammetry, mesh extraction, or downloaded art packs.

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.2.0-green.svg)](SKILL.md)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Runtime](https://img.shields.io/badge/runtime-Three.js-000000.svg)](https://threejs.org)
[![Tooling](https://img.shields.io/badge/tooling-Python%203.10%2B%20stdlib-3776ab.svg)](scripts)

<a href="https://trendshift.io/repositories/83608?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-83608" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/83608/daily?language=Python" alt="hoainho%2Fimg2threejs | Trendshift" width="250" height="55"/></a>

![img2threejs demo — a reference loot-chest image reconstructed as a procedural Three.js model](assets/demo.gif)

</div>

*A single reference image reconstructed in code — correct proportions, colours, bevels, gold trim, and an emissive emblem — running live in the browser.*

### [→ Open the Live Demo Gallery](https://hoainho.github.io/img2threejs-showcase/)

Every model in the gallery is generated code, running in your browser. No mesh files, no downloads.

---

## Live demos

Reconstructions built entirely from primitives, procedural shaders, and generated geometry. The clips below are the live models running in-browser — open each one to orbit it and read the generated source.

| Demo | Preview | Subject | View | Source |
| --- | --- | --- | --- | --- |
| Sony WF-1000XM3 Earbuds + Case | <img src="assets/sony-wf1000xm3.gif" width="260" alt="Sony WF-1000XM3 live demo" /> | hard-surface object | [Live](https://hoainho.github.io/img2threejs-showcase/#/demo/sony-wf1000xm3) | [code](https://github.com/hoainho/img2threejs-showcase/blob/main/src/demos/sony-wf1000xm3/createSonyWf1000xm3Model.ts) |
| ISSACA 12 Gauge Shotgun | <img src="assets/issaca-shotgun.gif" width="260" alt="ISSACA 12 Gauge Shotgun live demo" /> | hard-surface object | [Live](https://hoainho.github.io/img2threejs-showcase/#/demo/issaca-shotgun) | [code](https://github.com/hoainho/img2threejs-showcase/blob/main/src/demos/issaca-shotgun/createIssacaShotgunModel.ts) |
| Gerber Paracord Knife | <img src="assets/gerber-knife.gif" width="260" alt="Gerber Paracord Knife live demo" /> | hard-surface object | [Live](https://hoainho.github.io/img2threejs-showcase/#/demo/gerber-knife) | [code](https://github.com/hoainho/img2threejs-showcase/blob/main/src/demos/gerber-knife/createGerberKnifeModel.ts) |
| Doraemon House (isometric diorama) | <img src="assets/doraemon-house.gif" width="260" alt="Doraemon House live demo" /> | hard-surface object | [Live](https://hoainho.github.io/img2threejs-showcase/#/demo/doraemon-house) | [code](https://github.com/hoainho/img2threejs-showcase/blob/main/src/demos/doraemon-house/createDoraemonHouseModel.ts) |
| War-Hauler "SECTOR 07" | <img src="assets/warhauler.gif" width="260" alt="War-Hauler SECTOR 07 live demo" /> | hard-surface object | [Live](https://hoainho.github.io/img2threejs-showcase/#/demo/warhauler) | [code](https://github.com/hoainho/img2threejs-showcase/blob/main/src/demos/warhauler/createWarHaulerModel.ts) |
| Crowned Loot Chest | <img src="assets/crown-chest.gif" width="260" alt="Crowned Loot Chest live demo" /> | hard-surface object | [Live](https://hoainho.github.io/img2threejs-showcase/#/demo/crown-chest) | [code](https://github.com/hoainho/img2threejs-showcase/blob/main/src/demos/crown-chest/createCrownChestModel.ts) |

The gallery source lives in [hoainho/img2threejs-showcase](https://github.com/hoainho/img2threejs-showcase). If this project is useful, a star on this repo helps others find it.

---

## What it does

You give it one reference image of an object. It produces a `THREE.Group` factory written in TypeScript that recreates that object from primitives, procedural shaders, and generated geometry — with a runtime hierarchy (pivots, sockets, colliders) so the result is ready to animate, not an inert lump.

It runs under Claude Code, Codex, or OpenCode. It is agent-agnostic: wherever the docs say "agent vision" or "agent browser tool", it uses whatever the host provides — native image reading, a browser MCP, the project preview, or a user-supplied screenshot.

### Subjects and detail accuracy

- **Objects and characters.** Each subject is classified `object`, `character`, or `hybrid`. Objects follow the hard-surface pipeline; characters route through an anatomy-aware track (head-unit proportions, facial landmarks, pose) documented in `grimoire/character/recons