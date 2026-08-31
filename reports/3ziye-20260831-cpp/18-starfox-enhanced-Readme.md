# Star Fox Enhanced

A native Windows PC port of the open-source
[UltraStarFox](https://github.com/Sunlitspace542/ultrastarfox) codebase. It
presents at a selectable 20, 30, 60, 90, 120, 240, 360, or 480 frames per
second while preserving the original game's intended NTSC simulation speed
and assembled model data. The default is 60 FPS.

# NOTE: YOU DO NOT HAVE TO BUILD THIS, THE NIGHTLY IS IN THE REPO AT dist/StarFoxEnhanced

This repository is an early playable fidelity pass. It does not track a game
executable, retail ROM, reconstructed ROM, or generated asset companion. The
Windows executable embeds source-built BPS deltas and symbol data. The
complete optional compressed MSU-1 music set is distributed separately as
`Starfox-MSU1.PAK` beside the executable. On its
first launch it validates the user's own unmodified Star Fox USA v1.2 (Rev 2)
ROM, reconstructs the Original and Star Fox EX runtime data locally, and writes
one version-bound `Starfox-Assets.BIN` companion beside the executable. Later
launches use that validated companion without requiring the retail ROM to stay
present. No GitHub release has been published yet.

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
MSU-1 music, rumble, controller remapping, and a separate Options page.
MSU-1 music is off by default and, when enabled for Original, replaces the
SPC music stem with the companion orchestral set while leaving sound effects
on their own channel. If `Starfox-MSU1.PAK` is not beside the executable, the
option reads `NOT FOUND` and cannot be enabled. Rumble is on by default for
Original and plays the authored
UltraStarFox sequences on compatible SDL, XInput, and Steam Input controllers.
The Options page's first option is the
Star Fox EX-style God Mode: player collision is disabled,
regular Nova Bombs remain infinite, and holding R while pressing A fires a
God Nuke. The Options page can also enable a live on-screen FPS counter which
reports completed presentations in 250 ms samples so lag spots remain visible,
and select green (the default), white, blue, red, yellow, cyan, magenta, or
orange crosshair art. The selected hue applies to both the original four-piece
OBJ reticle and its Super FX cockpit triangles while damaged-wing indicators
remain red.

`CUSTOMIZE SCREEN` opens a mouse-driven captured native-gameplay HUD preview
using the game's actual HUD artwork. Lives, Shield, Bombs/Boost, Comms, and the
Boss Health bar can each be dragged independently; `RESET` (or Y) restores the
current display mode's defaults. Layouts are independent for 4:3,
16:9, 16:10, 21:9, and 32:9, with separate Original and Star Fox EX layouts
for every size. They save automatically to
`Documents/Star Fox Enhanced/hud-layout.cfg`.
Game pace, render FPS, display mode, MSU-1 music, rumble, God Mode, the FPS
counter, and crosshair colour also persist in
`Documents/Star Fox Enhanced/pregame.cfg`. Keyboard and
controller remaps are saved automatically when the remapping screen closes.
Standard display uses the complete 256x224 raster; Widescreen 16:9,
Widescreen 16:10, Ultrawide 21:9, and Super Ultrawide 32:9 expand the intro
and gameplay scene to 400x224, 360x224, 520x224, and 800x224 respectively
while keeping cartridge-authored HUD, dialogue, title, map, and control-screen
artwork centred in their original safe area. All modes use nearest-neighbor scaling
in a resizable window. It is a hybrid source port: a pinned 65C816 core
executes bounded original routines while timing, asset decoding, simulation
orchestration, rendering, audio output, and 