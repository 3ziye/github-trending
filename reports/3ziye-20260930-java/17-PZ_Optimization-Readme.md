[![Project Zomboid Build 42: stock vs all optimizations. Same PC, same save, same route; 174 fps stock, 632 fps optimized](docs/media/showcase-stock-vs-all-optimizations-thumbnail.jpg)](https://www.youtube.com/watch?v=GCjCYbTE9AQ)

# PZ_Optimization

Performance patches for **Project Zomboid Build 42**, on the Java side of the game.
Not a Lua mod: a set of drop-in `.class` files that shadow 41 game classes and remove
the worst stalls from the chunk streamer, the renderer, the weather and the loading path.
`projectzomboid.jar` is never modified, every change has a kill switch in an in-game
Options tab, and every number in this file comes from the hands-off benchmark harness in
this repo.

**Target: Build 42.21, jar revision `4a0e9546ec`, Windows, Linux and macOS** (the three
Steam depots ship the same jar). The overrides refuse to run against any other revision: they log one
line and the game behaves as stock.

| | |
|---|---|
| **Steam Workshop** | [PZ_Optimization (item 3805285544)](https://steamcommunity.com/sharedfiles/filedetails/?id=3805285544) |
| **Latest release** | [github.com/xD3I/PZ_Optimization/releases/latest](https://github.com/xD3I/PZ_Optimization/releases/latest) (`install.ps1`, `install.sh`, `pzopt-4a0e9546ec-classes.zip`) |
| **Showcase video** | [youtube.com/watch?v=GCjCYbTE9AQ](https://www.youtube.com/watch?v=GCjCYbTE9AQ), stock vs all optimizations ([See it in action](#see-it-in-action)) |
| **Live benchmark dashboard** | [pzo.diegov.dev](https://pzo.diegov.dev) (Grafana: every harness run since 2026-09-24 frame by frame, CPU / GPU use, profiler flame graphs, run-vs-run diffs, the game being benchmarked right now; the first page load after a quiet spell takes a few seconds) |
| **Every run, in order** | [`docs/results.md`](docs/results.md) (earlier runs: [`docs/archive/2026-09-24/`](docs/archive/2026-09-24/)) |

Single player is what has been measured. The files are client side only (nothing to
install on a server); read [Known limitations](#known-limitations) before installing on a
machine you play on.

> **Turn off Steam's in-game performance monitor** (Settings > In Game > "In-game
> performance monitor", the newer overlay, not the classic Shift+Tab one). It hooks every
> GL call and serialises the render thread: with it on the optimized game stops at about
> 160 fps and the headroom these patches recover is hidden (164 vs 237 fps on the 120 km/h
> route, `docs/archive/2026-09-24/results.md` 2026-09-19). Use the build's own overlay
> ([F9 / L3 + R3](#performance-overlay-f9--l3--r3)), MangoHud or RivaTuner instead.

---

## Contents

1. [See it in action](#see-it-in-action)
2. [Results at a glance](#results-at-a-glance)
   - [Weather: fog & lightning at 120 km/h](#weather-fog--lightning-at-120-kmh)
   - [Rosewood spin, uncapped](#rosewood-spin-uncapped)
   - [Downtown Louisville, 2,500 zombies](#downtown-louisville-2500-zombies)
   - [Boot and load](#boot-and-load)
   - [Windows](#windows)
   - [macOS](#macos)
   - [Handheld and old laptops](#handheld-and-old-laptops)
   - [Against the Workshop's performance mods](#against-the-workshops-performance-mods)
   - [Input latency: NVIDIA Reflex-style low latency](#input-latency-nvidia-reflex-style-low-latency)
   - [Variable refresh: G-SYNC, FreeSync, ProMotion](#variable-refresh-g-sync-freesync-promotion)
   - [Clear audio: no clipping under gunfire](#clear-audio-no-clipping-under-gunfire)
   - [Ambient occlusion at almost no cost](#ambient-occlusion-at-almost-no-cost)
3. [Install](#install)
   - [Requirements](#requirements)
   - [Method A: Steam Workshop](#method-a-steam-workshop)
   - [Method B: installer script from the GitHub release](#method-b-installer-script-from-the-github-release)
   - [Method C: unpack the zip by hand](#method-c-unpack-the-zip-by-hand)
   - [Method D: build from source (Linux)](#method-d-build-from-source-linux)
   - [Check that it loaded](#check-that-it-loaded)
   - [Uninstall](#uninstall)
   - [Updating the mod](#updating-the-mod)
   - [After a game update](#after-a-game-update)
4. [Settings](#settings)
   - [Options > Optimizations](#options--optimizations)
   - [Frame cap: Uncapped, 300 to 500 fps, menu framerate](#frame-cap-uncapped-300-to-500-fps-menu-framerate)
   - [Upscaling: FSR 1.0 and DLSS](#upscaling-fsr-10-and-dlss)
   - [Performance overlay (F9 / L3 + R3)](#performance-overlay-f9--l3--r3)
   - [`pzopt.properties` and the key table](#pzoptproperties-and-the-key-table)
5. [How the optimizations work](#how-the-optimizations-work)
   - [Chunk streaming](#1-chunk-streaming)
   - [Renderer](#2-renderer)
   - [Weather: puddles, rain, lightning, fog](#3-weather-puddles-rain-lightning-fog)
   - [Boot: launch to main menu](#4-boot-launch-to-main-menu)
   - [Load: Continue to world ready](#5-load-continue-to-world-ready)
   - [Visual fixes found on the way](#6-visual-fixes-found-on-the-way)
   - [Measured and not adopted](#measured-and-not-adopted)
6. [How the install works without touching the jar](#how-the