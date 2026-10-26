THIS PROJECT IS NOT RELATED TO SHADPS4. ALL QUESTIONS RELATED TO THIS PROJECT SHOULD BE SENT TO THE DISCORD SERVER https://discord.gg/KYZRKk9CB, NOT TO THE SHADPS4 SERVER.


# bbport — a native Linux port of Bloodborne

**English** · [Русский](README.ru.md)

bbport is the counterpart of Wine + DXVK for a single game: *Bloodborne* for PlayStation 4
(CUSA03173, game version 1.09) on an x86-64 Linux PC. The game's original executable runs
directly on the PC:

- **as in Wine**, the game's x86-64 code runs on the CPU directly, and a runtime written for
  this one game replaces the PS4 system libraries;
- **as in DXVK**, the game's graphics are translated to Vulkan — by the port's own renderer and
  shader translator (they started from [shadPS4](https://github.com/shadps4-emu/shadPS4)'s and were
  rewritten), including temporal upscaling with AMD FSR 3.1, FSR 4, FSR 4.1.1 and NVIDIA DLSS;
- memory and the GPU's work follow the PC model on every GPU by default (the new memory and
  translation model, since 0.6); the old memory model of 0.3 stays as a launcher option
  (*Memory model → Old*).

What remains to the full Wine + DXVK model: removing the old memory model once the new one is
confirmed on NVIDIA and Intel (see below).

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
  is the new one on every GPU):
  - **The new memory and translation model — the default on every GPU (0.6).** The game's memory lives
    in system RAM and the GPU reads it where it is, as a PC game's buffers; data it reads often
    is kept in VRAM and given back when unused (textures after 20 s, buffers after 60 s). The
    layer's memory module tracks CPU writes to mirrored blocks to keep those copies coherent;
    it does not copy the whole GPU-visible memory. The PS4 command processor's work
    is translated into Vulkan commands rather than emulated on the CPU: memory writes
    (`WRITE_DATA`, DMA) are done by the GPU in command-stream order, and fences are written by the
    GPU itself at the end of the pipeline, at the same point of the stream as the PS4's command
    processor writes them. On every GPU the game's memory goes through the layer's memory module:
    bound in place, VRAM copies as separate buffers, no sparse binding (NVIDIA's sparse binding
    froze the GPU for seconds; on AMD the module is faster than the former sparse arena too);
    `BB_LAYER_MEMORY=0` gives AMD's sparse arena. Tested thoroughly on an RX 7800 XT; on NVIDIA
    by testers. A driver that fails the startup checks falls back to VRAM copies by itself.
    Without the launcher: `BB_PC_MODEL=1/0` (unset: the new one, as *Auto*).
  - **The old memory model, as in 0.3** (*Old*). VRAM copies of the game's memory, writes
    tracked through page protection, with every fix made since 0.3.

  [Changes in 0.6](docs/CHANGES_0.6.md), [0.6-pre1](docs/CHANGES_0.6-pre1.md),
  [0.51](docs/CHANGES_0.51.md), [0.5](docs/CHANGES_0.5.md).

  Unused textures are freed in both modes, so VRAM no longer grows with every area visited.
- **Unlocked frame rate.** Hooks in the game's code make the simulation use the real frame time
  (the community patches in `patches/Bloodborne.xml` remain for comparison, `BB_FRAME_HOOKS=0`);
  ~90 FPS at 4K with FSR 4 Balanced on an RX 7800 XT, ~150 FPS at 1440p with FSR 4 Quality.
  Also 30/60/90 FPS modes; **F3** switches a 30 FPS limit on and off while playing (some
  cinematics, e.g. Laurence's, are safest at 30).
- **Any aspect ratio, live.** 4:3, 16:10, 16:9, 21:9 and 32:9 with the HUD at the screen's edges,
  through hooks (the game's code is not patched); cinematics are wide too.
- **Keyboard and mouse.** Mouse look turns the game's camera directly; a mouse pointer in the
  game's menus (F1 releases the mouse); a layout close to Dark Souls III's (Space dodge, Left
  Shift run, Shift+Space jump); movement keys ramp up like a stick; button prompts show the bound
  key, or the buttons of the gamepad in use (Xbox and others), PlayStation icons only with a
  PlayStation pad.
- **Online play and seamless co-op.** Two pools on shadPS4 0.2