# Uncharted: The Nathan Drake Collection — PC port

Run the PS4 **Uncharted: The Nathan Drake Collection** (CUSA02344: *Drake's Fortune*, *Among
Thieves* and *Drake's Deception*) natively on Windows. The game's own x86-64 code runs directly
on the PC; a runtime supplies the PS4 system libraries, and a Vulkan renderer executes the PS4 GPU
work.

By **BilalReloaded** ([YouTube](https://www.youtube.com/@BilalReloaded/videos),
[GitHub](https://github.com/bc160201983)), October 2026. What changed and when:
[CHANGELOG.md](CHANGELOG.md).

> **No game files are in this repository or its builds.** You need your own copy of the game
> (the dumped CUSA02344 folder). This project is not affiliated with Sony, Naughty Dog or
> Bluepoint Games.

## Status

| Game | Plays | Notes |
|---|---|---|
| Uncharted: Drake's Fortune | Yes | 60 FPS in the tested areas. Native rendering up to 2880x1620 (4K output upscaled from it, the HUD at 4K). |
| Uncharted 2: Among Thieves | Yes | Played at 1440p and 4K. 60 FPS and more; the heaviest view 99 FPS at 4K on an RTX 5080 (frame limit 120). |
| Uncharted 3: Drake's Deception | Yes | Played at 1080p and 1440p, 4K tested: the Cartagena crowd 90 FPS at 4K on an RTX 5080 (frame limit 120). |

The Collection menu, switching between the three games, saves, audio (music, speech, effects),
cutscene movies and controllers work. Details and open issues: [analysis/STATUS.md](analysis/STATUS.md);
plan and test list: [analysis/PLAN.md](analysis/PLAN.md).

## System requirements and the lowest PC that plays

- **Needs:** Windows 10 or 11 (64-bit); a CPU from **Intel's 4th-generation Core (Haswell, 2013)
  or newer, or any AMD Ryzen** (the games need AVX, F16C, BMI1, MOVBE and LZCNT); a graphics card
  or integrated GPU with **Vulkan 1.3** and a current driver; about **6 GB of free RAM** for the
  game (16 GB in the PC recommended).
- **Weakest GPU tested: the integrated AMD Radeon graphics of a Ryzen 7000/9000 desktop CPU**
  (2 compute units, about a quarter of a PS4's GPU). At **720p**: Uncharted 3 27-39 FPS,
  Uncharted 2 27 FPS, Drake's Fortune 24 FPS; at **540p** Uncharted 3 33 FPS. Playable, not
  smooth. Settings: preset **Low**, or resolution **1080p** with upscaling **FSR 1** at
  **Performance** (the game draws 960x540) or **Ultra Performance**, anti-aliasing off.
- **4 CPU cores:** 60 FPS in Drake's Fortune and Uncharted 3 (title screen and in play; a 4-core
  test with a fast GPU), with **Idle game threads: Sleep** (the default). On a 4-6 core CPU also
  try **Multithreaded rendering** (per game) and keep **Frames queued at 1**.
- **Players report:** Core i5-10400F + RTX 3050 6 GB plays Uncharted 2 and 3.

## Features

**Launcher** (`Uncharted Launcher.exe`)
- A card per game; settings are kept **per game**.
- Quality presets:

  | Preset | Resolution | Frame rate | For |
  |---|---|---|---|
  | Low | 1080p, FSR 1 Performance (draws 960x540) | 60 | weak GPUs |
  | Medium | 1080p (as on PS4) | 60 | most PCs |
  | High | 1440p | 60 | fast GPUs |
  | Ultra | 4K (Drake's Fortune draws 1620p, upscaled) | up to 120 (experimental) | very fast GPUs |

  Every preset queues 1 frame. 2 frames queued is faster in heavy scenes, but GPU results
  reach the game a frame later: keep it at 1.

  **Low-end PCs and laptops:** keep **Idle game threads** (launcher, **Performance** tab) on
  **Sleep** (the default). With **Spin** the games' six job threads keep their cores busy while
  they wait for work, as on the PS4 where each has its own core; on a 4-6 core CPU that took
  nearly all of it (a 4-core test: 19-27 FPS on the title screen, 60 with Sleep). Also turn on **Multithreaded rendering** (per game) and keep **Frames queued at 1**. The PS4's
  GPU commands are otherwise processed on one CPU core, which limits slower CPUs; with this option
  the Vulkan command recording runs on a second core. On fast desktop CPUs it makes no difference.
  If a game hangs while loading, turn that option off again. With a weak GPU also pick the **Low**
  preset (FSR 1 Performance at 1080p); integrated GPUs: FSR 1 **Ultra Performance**.

- **Display:** windowed, borderless or exclusive fullscreen; resolution 540p, 720p, 900p, 1080p,
  1440p, 1620p or 4K; aspect ratio 16:10, 16:9, 21:9, 32:9; **upscaling** FSR 1, FSR 3.1, FSR 4
  or NVIDIA DLSS: the game draws below the resolution (Quality 1/1.5, Balanced 1/1.7, Performance
  1/2, Ultra Performance 1/3 of its width and height) and each frame is upscaled to it before the
  HUD and menus, which stay sharp; FSR 3.1, FSR 4 and DLSS also at the resolution (Native AA,
  DLAA); anti-aliasing TAA (with upscaling off or FSR 1); RCAS sharpening; FPS counter. Upscaling
  saves GPU time only: where the CPU limits the frame rate (most PCs at 1080p and 1440p, Steam
  Deck) it changes little.
- **Performance:** frame rate limit 30 / 40 / 45 / 50 / 55 / 60 / 75 / 90 / 100 / 120 (60 is the
  PS4's; above 60 is experimental, and faster than 120 breaks the games' movement, so it is not
  off