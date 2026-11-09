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
- **Optional controller shell** (Settings -> System -> **Controller only mode**; off by default, the
  classic launcher stays as it was): a PlayStation 5-style home screen with a full-screen background
  and logo per game, and the three games on a carousel along the bottom. It opens on the game you
  played last, and moving between games dissolves one game's art into the next (the artwork is not
  shipped: see `launcher/assets/ps5/NOTICE.md` to add your own). The wordmark is
  top left; the **Games**, **Gallery** and **Display** capsules are across the top, with Settings and
  Quit as the gear and the power button top right.
- **Gallery:** your photo-mode pictures, in a grid with a filter per game and a full-screen viewer.
  It reads `Pictures\Uncharted Launcher` (or a folder you choose) and its `1 Drake's Fortune`,
  `2 Among Thieves` and `3 Drake's Deception` subfolders; anything you drop in appears on the next
  visit, newest first. Thumbnails are cached, so opening it again is instant.
- **Display:** resolution, upscaling and its quality, the frame rate limit, the display mode, VSync
  and the launcher animations in one panel, with **All settings** going to the full page. Left/Right
  changes a value; the settings pages and the config always agree.
- **Controller first:** the D-pad or left stick moves, Cross chooses, Circle goes back, Options
  opens the settings, L1 and R1 switch games (or filter the Gallery). Up from a screen reaches the
  capsules. **Hold L3 + R3** for two seconds to close a running game: the ring along the bottom
  fills while you hold, and the first five seconds after a launch are ignored so a controller
  resting on a desk cannot close anything. Settings -> System turns that shortcut and the on-screen
  hints off, and sets the hold time (1-3 s).
- **Controller only mode** (Settings -> System, off by default) picks the shell: on is the
  PlayStation 5 hub; off is the classic layout, with the game cards, the tab strip and the footer Play button, in the same
  window and with the same settings. It switches without restarting; both layouts work from the
  controller, and the keyboard still moves and chooses.
- **Settings** keeps every option below, as a category list on the left and the same rows on the
  right