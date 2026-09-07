# Star Fox Enhanced

A native Windows PC port of the open-source
[UltraStarFox](https://github.com/Sunlitspace542/ultrastarfox) codebase. It
presents at a selectable 20, 30, 60, 90, 120, 240, 360, or 480 frames per
second while preserving the original game's intended NTSC simulation speed
and assembled model data. The default is 60 FPS.

> You do not need to build this yourself. Prebuilt alpha downloads are
> available under GitHub Releases, and the current Windows x64 nightly is also
> kept in `dist/StarFoxEnhanced`.

This repository is an early playable fidelity pass. It does not track a game
executable, retail ROM, reconstructed ROM, or generated asset companion. The
Windows executable embeds source-built BPS deltas and symbol data. The
complete optional compressed MSU-1 music set is distributed separately as
`Starfox-MSU1.PAK` beside the executable. On its
first launch it validates the user's own unmodified Star Fox USA v1.2 (Rev 2)
ROM, reconstructs the Original and Star Fox EX runtime data locally, and writes
one version-bound `Starfox-Assets.BIN` companion beside the executable. Later
launches use that validated companion without requiring the retail ROM to stay
present. `v0.0.4` is the current public alpha release.

This project utilizes Codex GPT 5.6 Sol at Ex-High thought.

## What is preserved

- Gameplay, PATH/map bytecode, strategies, collision, damage, RNG, animation,
  bosses, and stage progression update at the original deterministic 20 Hz.
- Camera and object transforms are presentation-only interpolations, producing
  smooth motion at the selected render FPS without changing game state.
- All rendered 3D geometry is decoded from the assembled UltraStarFox ROM:
  integer vertices, faces, BSP order, animation frames, LODs, shadows, texture
  coordinates, colors, and collision metadata.
- Original BG tilemaps, palettes, OBJ graphics, HUD, text, route-map sprites,
  textured planet maps, particles, dust, and SPC700 music/effects are used.
- Title, attract intro, control selection, training, route selection, all
  three routes, game over, continue, credits, pause, and stage transitions are
  connected in the native flow.

The cleaned pre-game setup starts with an `EXPERIENCE` selector. `ORIGINAL` is
the default; `STARFOX EX` selects the embedded 1.11.03 source build, including
its native title/intro, three-page configuration menu, shipped `PLANETS` and
`PLANETS2` campaigns, custom stages, ships, models, palettes, music, and source
mechanics. EX's real 64 KiB cartridge SRAM is persisted byte-for-byte at
`Documents/Star Fox Enhanced/starfox-ex.srm`; its source `SFEX` validation,
defaults, loading, START GAME commit, and L+R+DOWN+B intro reset paths all run
unchanged.

The setup also independently selects game pace, render FPS, display mode,
presentation renderer, MSU-1 music, rumble, controller remapping, and a
separate Options page. `RENDERER` defaults to GPU and can be changed to
SOFTWARE to use SDL's portable CPU presentation backend; this is an actual
backend switch and is saved with the other setup choices.
MSU-1 music is off by default and, when enabled for Original, replaces the
SPC music stem with the companion orchestral set while leaving sound effects
on their own channel. If `Starfox-MSU1.PAK` is not beside the executable, the
option reads `NOT FOUND` and cannot be enabled. Rumble is on by default for
Original and plays the authored
UltraStarFox sequences on compatible SDL, XInput, and Steam Input controllers.
The Options page also provides independent MUSIC and SFX volume controls.
Left/right changes them in 10% steps; the mouse can drag either bar to any
whole percentage from 0 through 100. The first option is the
Star Fox EX-style God Mode: player collision is disabled,
regular Nova Bombs remain infinite, and holding R while pressing A fires a
God Nuke. The Options page can also enable a live on-screen FPS counter which
reports completed presentations in 250 ms samples so lag spots remain visible,
and select green (the default), white, blue, red, yellow, cyan, magenta, or
orange crosshair art. The selected hue applies to both the original four-piece
OBJ reticle and its Super FX cockpit triangles while damaged-wing indicators
remain red.

`RENDER UPSCALE` replaces the old Upscaled Polys option and rasterizes the
Super FX world layer from 1x up to 10x the source raster. Face visibility and
BSP order remain tied to the original grid while high-resolution projection
retains fractional endpoints across interpolated and completed source frames.
This resolves polygon edges and lines with finer, temporally stable steps.
Cartridge HUD, sprites, backgrounds, and text keep their authored resolution.
Scan conversion and presentation run on the CPU, so higher scales cost frame
time and memory and the usable ceiling depends on the machine.

`ANTI-ALIASING` and the surface-driven effects (`ENHANCED TEXTURES` and
`RTX LIGHTING`) run on the scaled raster as well, so they
resolve polygon edges at the