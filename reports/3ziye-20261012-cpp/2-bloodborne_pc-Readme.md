THIS PROJECT IS NOT RELATED TO SHADPS4. ALL QUESTIONS RELATED TO THIS PROJECT SHOULD BE SENT TO THE DISCORD SERVER https://discord.gg/KYZRKk9CB, NOT TO THE SHADPS4 SERVER.


# bbport — a native Linux port of Bloodborne

**English** · [Русский](README.ru.md)

bbport is the counterpart of Wine + DXVK for a single game: *Bloodborne* for PlayStation 4
(CUSA03173, game version 1.09) on an x86-64 Linux PC. The game's original executable runs
directly on the PC:

- **as in Wine**, the game's x86-64 code runs on the CPU directly, and a runtime written for
  this one game replaces the PS4 system libraries;
- **as in DXVK**, the game's graphics are translated to Vulkan — by a renderer derived from
  [shadPS4](https://github.com/shadps4-emu/shadPS4) and heavily extended for this game, including
  temporal upscaling with AMD FSR 3.1, FSR 4 and FSR 4.1.1;
- memory and the GPU's work follow the PC model on AMD GPUs by default (the new memory and
  translation model); NVIDIA and other GPUs keep the old memory model of 0.3 for now. The
  launcher's *Memory model* switches either way.

One step remains to the full Wine + DXVK model: the new model on NVIDIA as well, then removing the
old memory model (see below).

> **No game files are included.** You need your own dump of Bloodborne with update 1.09: any retail
> release (CUSA00900 in the US, CUSA03173 for the European Game of the Year edition, ...), as they
> share the same executable.
> This project is not affiliated with Sony Interactive Entertainment, FromSoftware or AMD.

**Status: experimental, playable.** The game boots, loads saves and plays (the Hunter's Dream
and several areas of Yharnam were played with it) with sound, gamepad and saving.
A full play-through has not been verified, and only one machine (Linux, AMD Radeon RX 7800 XT,
Mesa/RADV) has been tested thoroughly.

## Highlights

- **Native execution.** The eboot is converted offline into a flat memory image; PS4 libc and
  libSceFios2 are linked into it as native code. No CPU emulation and no per-instruction
  translation: the game code runs at full speed.
- **Two memory models** (launcher → *Mode → Memory and translation model*; *Auto*, the default,
  picks by GPU):
  - **The old memory model, as in 0.3 — the default on NVIDIA, Intel and others.** VRAM copies
    of the game's memory, writes tracked through page protection. With every fix made since 0.3
    (motion vectors and the upscaler, flicker with DoF on, a damaged shader cache).
  - **The new memory and translation model — the default on AMD.** The game's memory lives
    in system RAM and the GPU reads it where it is, as a PC game's buffers; data it reads often
    is kept in VRAM and given back when unused (textures after 20 s, buffers after 60 s). The
    layer's memory module tracks CPU writes to mirrored blocks to keep those copies coherent;
    it does not copy the whole GPU-visible memory. The PS4 command processor's work
    is translated into Vulkan commands rather than emulated on the CPU: memory writes
    (`WRITE_DATA`, DMA) are done by the GPU in command-stream order, and fences are written by the
    GPU itself at the end of the pipeline, at the same point of the stream as the PS4's command
    processor writes them. On AMD the game's memory is kept in a sparse buffer (the arena); on
    NVIDIA, Intel and others it goes through the layer's memory module: bound in place, VRAM
    copies as separate buffers, no sparse rebinding (NVIDIA's sparse binding froze the GPU for
    seconds); `BB_LAYER_MEMORY=1/0` chooses by hand. Tested on an RX 7800 XT. On NVIDIA it can be chosen by hand (*New*); testers' results differ by scene,
    some scenes are slower than with the old model, so it is not the default there yet. Not
    tested on Intel. Without the launcher: `BB_PC_MODEL=1/0` (unset: by GPU, as *Auto*).

  [Changes in 0.5](docs/CHANGES_0.5.md); the prereleases: [pre4](docs/CHANGES_0.5-pre4.md),
  [pre3](docs/CHANGES_0.5-pre3.md), [pre2](docs/CHANGES_0.5-pre2.md).

  Unused textures are freed in both modes, so VRAM no longer grows with every area visited.
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
  - **FSR 