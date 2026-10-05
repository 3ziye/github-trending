THIS PROJECT IS NOT RELATED TO SHADPS4. ALL QUESTIONS RELATED TO THIS PROJECT SHOULD BE SENT TO THE DISCORD SERVER https://discord.gg/KYZRKk9CB, NOT TO THE SHADPS4 SERVER.


# bbport — a native Linux port of Bloodborne

**English** · [Русский](README.ru.md)

bbport runs the original PlayStation 4 executable of *Bloodborne* (CUSA03173, game version
1.09) directly on an x86-64 Linux PC. It is not a general emulator. The game's own x86-64 code
executes natively; a small runtime written for this one game replaces the PS4 system libraries;
the GPU work is translated to Vulkan by a renderer derived from
[shadPS4](https://github.com/shadps4-emu/shadPS4) and heavily extended for this game, including
temporal upscaling with AMD FSR 3.1, FSR 4 and FSR 4.1.1.

> **No game files are included.** You need your own dump of Bloodborne (CUSA03173, v1.09).
> This project is not affiliated with Sony Interactive Entertainment, FromSoftware or AMD.

**Status: experimental, playable.** The game boots, loads saves and plays (the Hunter's Dream
and several areas of Yharnam were played with it) with sound, gamepad and saving.
A full play-through has not been verified, and only one machine (Linux, AMD Radeon RX 7800 XT,
Mesa/RADV) has been tested thoroughly.

## Highlights

- **Native execution.** The eboot is converted offline into a flat memory image; PS4 libc and
  libSceFios2 are linked into it as native code. No CPU emulation and no per-instruction
  translation: the game code runs at full speed.
- **Unlocked frame rate.** Community patches (`patches/Bloodborne.xml`) make the simulation
  use the real frame time; ~90 FPS at 4K with FSR 4 Balanced on an RX 7800 XT, ~150 FPS at
  1440p with FSR 4 Quality. Also 30/60/90 FPS modes.
- **Temporal upscaling built for this game.** Bloodborne has no velocity buffer, so bbport
  computes motion vectors itself: camera motion from depth and the scene matrices, and object
  motion (characters, cloth, weapons) from the vertex positions of the previous frame. The
  scene is jittered sub-pixel (Halton) and rendered at a reduced resolution; the upscaler fills
  the output (720p for the Steam Deck, 1080p, 1440p or 2160p) and the UI is drawn natively at the output resolution.
  - **FSR 3.1** (FireBurn/FSR-Vulkan).
  - **FSR 4 (INT8, model v07)** on GPUs exposing the required Vulkan shader features —
    RDNA2/3 included (see Requirements).
  - **FSR 4.1.1 (INT8)**: AMD's 4.1.1 DLL is recorded once under vkd3d-proton and its passes
    are replayed natively on Vulkan; the output is **bit-exact** with the DLL. The assets are
    built on your machine from your own DLLs (`tools/fsr4cap`).
  - Faster than AMD's own shaders on RDNA3: the final passes of FSR 4 and 4.1.1 were rewritten
    to store through workgroup memory (3.5× and 2.3× faster, bit-exact); FSR 4 costs ~4 ms at
    4K on an RX 7800 XT instead of ~6 ms.
- **Multi-threaded GPU command processing.** The PS4 command stream is decoded on one thread
  and draws are bound and recorded on another (two-stage pipeline), with a Vulkan recording
  thread and helper threads for memory copies. Early on the single GPU thread capped the game
  at ~26 FPS; now it runs at 90–150 FPS depending on resolution and scene.
- **In-game menu** (Insert or L3+R3): upscaler, preset, sharpness, output resolution, game
  effects (chromatic aberration, DoF, motion blur, SSAO, the game's own AA, SSR, model LOD).
- **GTK4 launcher** and an **AppImage** for the Steam Deck.

## How it differs from shadPS4

| | shadPS4 | bbport |
|---|---|---|
| Scope | General PS4 emulator, many games | One game: Bloodborne v1.09 |
| Loading | Its own ELF loader and kernel emulation at run time | The eboot is converted offline (`scripts/`) into an image with PS4 libc/Fios2 linked in; a C loader maps it and jumps into the game (loader and runtime: ~5k lines) |
| System libraries | Broad HLE of the PS4 OS | A small runtime (`src/runtime_*.c`) that implements exactly what Bloodborne calls: memory, threads, sync, files, audio (incl. ATRAC9), pad, saves, AppContent |
| GPU | shadPS4 video core and shader recompiler | The same core (vendored, GPL) with ~200 marked changes (`bbport:`) plus new modules: two-stage draw pipeline, render-state and texture-set memoization, render-scale proxies, motion vectors, FSR 3.1/4/4.1.1, frame capture and GPU profiler |
| GPU thread | One thread processes the whole command stream (the bottleneck in Bloodborne) | Decode and draw recording run on separate threads; the work scales with the hardware threads (Steam Deck included) |
| Upscaling | — | Temporal (FSR 3.1, FSR 4, FSR 4.1.1) with the game's own motion vectors and jitter |
| Game patches | Patch files applied by the emulator | The same community patches, compiled at start (`scripts/patches.py`); render resolution, effects and FPS from the launcher |

Without shadPS4 there would be no bbport: its renderer and shader recompiler are the base of
the graphics side.

## Requirements

- Linux x86-64, a Vulkan 1.3