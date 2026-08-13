# Claude of Duty

Get updates [here](https://shumer.dev/newsletter).

A first-person shooter built in the browser with Three.js r180 and WebGL2. Roughly
55k lines across 11 subsystems, written by a fleet of AI agents under orchestration.

**There are no art assets.** Every texture, mesh, animation and sound is generated
procedurally at load time from code. No models, no HDRIs, no image files, no audio
files. The only runtime dependency is `three`.

```bash
npm install
npm run dev          # http://127.0.0.1:5173
```

Click the canvas to lock the cursor. WASD move, mouse aim, LMB fire, RMB ADS,
R reload, Shift sprint, Ctrl crouch, Space jump, Q/E lean, Esc release.

## What's in it

| subsystem | what it does |
|---|---|
| `render` | HDR pipeline, cascaded shadow maps in a `sampler2DArray` with texel snapping and PCSS contact hardening, MRT depth/normal/velocity prepass, GTAO, TAA with YCoCg variance clipping, tile-dilated motion blur, Karis bloom pyramid, GPU EV100 metering, procedural 33³ grade LUT, AgX composite |
| `materials` | GPU texture forge: 19 procedural surfaces (concrete, brick, plaster, asphalt, sand, rusted/painted/brushed metal, wood, fabric, burlap, glass…), periodic noise so everything tiles seamlessly, Sobel height→normal, parallax occlusion mapping, triplanar projection, curvature-driven edge wear |
| `sky` | Atmospheric scattering, time of day, PMREM environment generation, volumetric fog and light shafts |
| `world` | ~120×120 m market street: modular building kit with real wall thickness, enterable interiors, several hundred instanced props |
| `physics` | Written from scratch, no library. Binned-SAH BVH (29k tris → 14k nodes in 22 ms, 0.25 µs/raycast), swept-capsule character controller with a 5-plane crease stack, impulse rigid bodies with CCD, PBD ragdolls, multi-layer bullet penetration |
| `player` | Movement state machine, slide/mantle/lean, camera feel |
| `weapons` | Procedural weapon geometry, viewmodel rig, ADS, spring recoil, procedural reloads, ballistics with travel time and drop |
| `fx` | GPU particles, decals, tracers, muzzle flash, explosions |
| `ai` | Skinned soldiers, navmesh pathing, perception, cover behaviour, ragdoll death |
| `ui` | DOM/CSS HUD: crosshair, hitmarkers, minimap, compass, killfeed |
| `audio` | Web Audio synthesis — no sound files. Layered weapon fire, convolution reverb, HRTF spatialisation, occlusion |

`ARCHITECTURE.md` is the contract the agents worked against: subsystem interface,
directory ownership, the cross-subsystem event vocabulary, and shared surface types.

## Tooling

The interesting part of this repo is arguably the harness, not the game.

| tool | purpose |
|---|---|
| `tools/capture.mjs` | Screenshot one named shot via GPU-backed headless Chromium |
| `tools/shotset.mjs` | All 11 shots in one session — fast review set |
| `tools/baseline.mjs` | **Reproducible** capture: each shot in an isolated page, fixed frame budget. Bit-identical across runs |
| `tools/imagediff.mjs` | Per-pixel gate. Exits non-zero if any pixel moved |
| `tools/profile.mjs` | Gameplay profiler at real device pixel ratio. Frame-time *distribution* and hitch attribution via per-frame WebGL program counts |
| `tools/playtest.mjs` | Scripted movement/fire smoke test |

Two findings worth recording, because both invalidated earlier measurements:

**Median frame time hides the actual problem.** A static-camera benchmark reported
94 fps while the game was unplayable. Real gameplay at Retina DPR (internal 3.34 MP,
not 2.07) ran 12–17 fps with **728–1236 ms stalls** caused by 34+ WebGL programs
compiling lazily mid-frame. `profile.mjs` reports p50/p95/p99 and attributes each
hitch, which is what surfaced it.

**Captures were not reproducible.** `shotset.mjs` reuses one page across all 11
shots, so particle age, decal buffers and exposure state leak forward — two identical
runs differed on 10 of 11 shots. `baseline.mjs` isolates each shot in a fresh page,
which is bit-identical and is what makes `imagediff.mjs` a usable gate.

## Performance

Measured on an Apple silicon laptop at 1512×982, DPR 2 (3.34 MP internal), `ultra` preset,
3 runs, gameplay in motion with AI and firing active:

| | before optimization | after |
|---|---|---|
| fps p50 | 12–17 | **28–30** |
| fps p99 | 4–9 | **14–17** |
| worst frame | 728–1236 ms | **66–82 ms** |
| shader compiles during play | 34–35 | **0** |
| boot | ~9–12 s | **3.7–4.6 s** |

The optimization pass was constrained to produce **zero visual change**, enforced by
`imagediff.mjs` rather than by assertion — the shipped build is bit-identical to its
pre-optimization reference across all 11 shots.

Shader pre-warm (`src/core/prewarm.js`) is what removed the stalls. Making it
*provably* pixel-neutral required first fixing subsystems that animated off
`performance.now()` instead of the engine clock, since any change to boot duration
otherwise shifted output.

## Honest assessment

The goal was to match a modern Call of Duty. **It does