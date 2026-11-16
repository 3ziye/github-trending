# Oblivion Remastered Performance Fix

[![Build](https://github.com/LTSharpe/OblivionRemasteredPerformanceFix/actions/workflows/build.yml/badge.svg)](https://github.com/LTSharpe/OblivionRemasteredPerformanceFix/actions/workflows/build.yml)
[![Latest release](https://img.shields.io/github/v/release/LTSharpe/OblivionRemasteredPerformanceFix?include_prereleases)](https://github.com/LTSharpe/OblivionRemasteredPerformanceFix/releases)

Higher frame rates in towns and crowds, far fewer hitches while you travel, no long frame when you step out of a door,
quicker menus, and a few crash fixes, for *The Elder Scrolls IV: Oblivion Remastered*. **The game looks and plays the
same**: no lowered settings, no shorter view distance, ray-traced lighting stays on its highest setting. The fix changes
*how* the engine does its work, never *what* it draws.

**It works on any PC that runs the game**, not just ours: it has no per-PC settings or paths, it finds the code it
changes in the game itself, and its helper threads adapt to your CPU. It is not tied to AMD: players report it working
with NVIDIA and AMD graphics cards, DLSS and FSR, Intel and AMD CPUs, on Steam and Game Pass, and through OBSE64
([Compatibility](#compatibility)). How much it gains depends on your hardware: most where the CPU is the limit
([Results](#results)).

> **Built by Claude.** The profiling, the reverse engineering, the fixes, the benchmark and these docs were done by Claude,
> Anthropic's AI model, working in Claude Code. [LTSharpe](https://github.com/LTSharpe) set the goal and the rules (never
> change the look), made every decision and played every build. All of the source is here for you to read.
>
> Free and open source. If it makes your game better and you'd like to say thanks, you can
> [support the work on GitHub Sponsors](https://github.com/sponsors/LTSharpe). Entirely optional.

> **Beta.** Every build is measured in depth on our test PC (AMD Ryzen 7 5800X, AMD Radeon RX 9070 XT, Windows 11,
> Steam), and players report it working on theirs: since the first release more than 40 have reported back, on NVIDIA
> RTX 20 to 50 series, AMD Radeon RX 7000 and 9000, Ryzen and Intel Core CPUs, the Game Pass version, a handheld, VR and
> one Linux PC. Most say it runs better, a few reported problems ([Compatibility](#compatibility)). Please keep
> [telling us how it went](https://github.com/LTSharpe/OblivionRemasteredPerformanceFix/issues/new/choose), especially on
> Intel Arc, CPUs with fewer cores, Steam Deck and Windows 10.

[Results](#results) · [Install](#install-two-minutes) · [AMD ML frame generation](#optional-amd-ml-frame-generation-radeon-rx-9000) ·
[What it does](#what-it-does) · [Check it on your PC](#check-it-on-your-pc-before--after) · [Graphics settings](#find-good-graphics-settings) ·
[Uninstall](#uninstall) · [Is it safe?](#is-it-safe) · [Compatibility](#compatibility) · [FAQ](#faq) · [Help improve it](#help-improve-it)

## Results

| Measured on our test PC (yours will differ: see below) | Stock game | With the fix | Measured on |
|---|---|---|---|
| **Flight round the Imperial City** at 4K with frame generation, frame rate capped at 60 before frame generation | 72 fps, 1% low 33, 19.5 hitches of 50 ms or more per flight, worst frame 135 ms | **102 fps** (+41%), 1% low 45, **4.8 hitches**, worst frame 66 ms | 1.0.0-beta |
| **Flight through Cheydinhal** at 4K, no frame generation | 55 fps, 1% low 26, 4-6 hitches of 50 ms or more | **63 fps**, 1% low **43**, **no hitch** | 0.16.2 (before the first public release) |
| **Cheydinhal streets** at 4K with frame generation (3 views) | 64 fps (1% low 50) | **91 fps** (1% low 68), +43% | 0.11.0 |
| **Cheydinhal when the CPU is the limit** (720p, no frame generation) | 45 fps | **57 fps**, +25% | 0.11.0 |
| **Stepping out of a door** at 4K: the worst frame as the picture comes back | 187 ms | **95 ms** | 0.11.0 |
| **Opening the menu** on the Graphics page at 4K | 0.74 s freeze | **0.43 s** | 0.11.0 |
| **Opening the pause menu or the inventory** at 4K | 0.36 s freeze | **0.20 s** | 0.11.0 |
| **Alt-tab** after using the inventory or the map | FSR and frame generation stay off | back on at once | 0.11.0 |
| **Pause menu, first open after a while** (game bug, issue #5) | one bright wrong frame, every time in our test | **never** | 1.2.3-beta |

**New in 1.2.3** (the main thread's work per frame, which decides the frame rate where the CPU is the limit; 4K, FSR
Performance, frame generation, frame rate capped at 60; public scenes in `bench/scenarios/`):

| Where (scenario, scene) | Switch off | Switch on (the 1.2.3-beta default) | Fixes |
|---|---|---|---|
| Brindle Home horse corral (`playlog-spots`, `brindle-corral-hold`) | 10.6 ms | **9.2 ms**: time over 16.7 ms per frame -87% | `PhysAnimNoEmptyLock`, `RigTraceReuse` |
| Skingrad forest (`skingrad-spots`, `sk-d`) | 9.7 ms (tick work) | **8.5 ms**: time over 16.7 ms -50% | `ChaosMaxPayloadSize` |
| Vilverin, Imperial City flight (`ic-spots`, `ic