# bbhost

bbhost is a translation layer that runs Bloodborne on Windows and Linux. The
game's own 1.09 executable runs unmodified on the PC's x86-64 CPU; bbhost
answers its calls into the PS4's system libraries with PC implementations, and
recompiles its GPU work, GCN shaders and the engine's draw calls, for Vulkan.
The aim is a definitive PC version of the game - the original, intact, with
what a PC release would add: any resolution and aspect ratio, 60 fps and
beyond, keyboard and mouse, proper settings, mods and online play.

![Cainhurst Castle](docs/images/cainhurst.jpg)

bbhost contains no game code or data. You need your own copy of the game: a
dump with the 1.09 update and its decrypted executable.

## Why not emulation

The PS4 has an x86-64 CPU, so the game's code does not need to be translated
to run on a PC - it needs a place to live. bbhost provides that place:

- **The CPU side runs natively.** bbhost loads the game's ELF executable,
  relocates it, links its imports to its own implementations and starts it.
  The game's code runs at full speed on the host CPU, with no interpreter or
  recompiler involved.
- **The PS4's system libraries are reimplemented** for the PC: files and
  saves, threads and memory, input, audio, movies, networking and the
  PlayStation Network calls the online features use - every one of the 660
  named functions the game imports.
- **Graphics are being moved from emulation to native code.** The game's
  renderer was written for the PS4's GPU: it builds command buffers for an AMD
  GCN GPU and ships GCN shader programs. bbhost hooks FromSoftware's own
  graphics layer instead, so draws are built directly from the engine's objects,
  and decompiles the shaders to typed, structured SPIR-V. The
  status table below shows what is native today and what still goes through
  the emulated GPU command processor.
- **Game functions are being rewritten as source**, one at a time, each checked
  against the original, so the game can be fixed and extended where a patch
  would not reach.

## Features

| | |
|---|---|
| ![Yharnam in 21:9](docs/images/yharnam-ultrawide.jpg) | **Any resolution, ultrawide included.** 21:9 and 32:9 with a wider field of view and the HUD where it belongs, and the resolution can be changed while playing. FSR 1 upscaling for slower GPUs. |
| ![PC Graphics settings](docs/images/pc-graphics.jpg) | **Settings in the game's own menus.** The System menu gains PC Settings, PC Graphics, PC Effects, PC Controls, PC Camera and Key Bindings, drawn in the game's style: anti-aliasing, ambient occlusion, shadow distance, fog, motion blur, field of view, frame cap and more. |

- **60 fps**, with the game's timing corrected so physics, animation and
  cutscenes run at the right speed. Higher frame caps keep the game's logic at
  60.
- **Keyboard and mouse**: mouse camera, a pointer in every menu, rebindable
  keys, and button prompts that show the keys.
- **PC enhancements** that can be switched off for the game as it shipped: the
  Hunter's Dream mirror opens the character appearance editor (a feature cut
  from the release), "Rebirth in the Nightmare" at the Altar of
  Despair lets you redistribute your levels, and the late areas allow two
  invaders, as the chalice dungeons do.
- **Online play** through a private server: co-op, invasions, messages,
  bloodstains and summon signs between bbhost players.
- **Mods** without touching the game files: replacement files, param tables
  edited by field name, byte patches as data, and native plugins - a
  randomizer (items, shops and enemies), a boss rush, gameplay mutators and
  the developers' own debug menu ship with it.
- **A setup window** that finds and checks your game files, and the Steam Deck
  as a supported device.

![The setup window](docs/images/setup-window.png)

## Status

The game is playable on Windows and Linux: the world, its bosses and online
sessions. What runs on native code and what is still emulated:

| Part | State |
|---|---|
| Game logic (CPU) | the game's own code, running natively |
| System libraries | reimplemented by bbhost: all 660 named imports the game binds |
| Window, input, audio, movies, saves | native (SDL3, Vulkan, FFmpeg, LibAtrac9) |
| Online | native sockets and HTTP against a private server; peer-to-peer UDP with NAT traversal |
| Draws | native: each draw is built from the engine's graphics objects; the command buffer only marks its place in the stream |
| Post-processing (YEBIS) | native: every stage's resources built by bbhost |
| Tessellation | native: the host GPU's own tessellation stages, all three stages lifted; the game's mesh hulls draw as one native pipeline, without the PS4's on-chip ring |
| Shaders | decompiled ("lifted") from GCN to typed, structured SPIR-V when the game creates them: every shader the game ships except compute (3,206 of 3,209 pixel shader programs, all vertex and tessellation programs; 100% of draws at the 12 measured places, see [docs/rendering.md](do