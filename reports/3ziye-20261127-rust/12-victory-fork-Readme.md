# VIctory fork (work in progress)

A work-in-progress fork of [VIctory](https://github.com/Marvisak/VIctory), a
compatibility layer that runs an Xbox Series title natively on Windows from
files the user supplies. This fork follows upstream
`main` and adds fixes aimed at one goal: getting the game's world to render
correctly and playably on one particular PC.

**This repository contains no game files, code or assets.** You need your own
copy of the game. It is not affiliated with or endorsed by the game's
developer or publisher.

## Credits

- **[VIctory](https://github.com/Marvisak/VIctory)** by Marvisak and its
  contributors is the base of everything here: the loader, the runtime
  services, the Direct3D 12 back end and the shader recompiler. Licensed
  GPL-3.0-or-later; so is this fork. Upstream's history is kept intact below
  the single commit that carries this fork's changes.
- **[XCL](https://github.com/ivall/xcl)** by ivall and its contributors
  (GPL-2.0-only) was used as a reference for how the same title behaves under
  another layer. Fixes inspired by it were written anew in VIctory's code.
- The guard over every view of a memory page is code by **myokex**
  ([victory-amd](https://github.com/myokex/victory-amd), commit `c6dc4d8`), which
  adapts pull request #115 here by Spexivus, its correction by joroyt and a part of
  VIctory #1122 by tightfall. The read-beside fix for kernel reads into title
  memory is by **Joshua Odom** (commit `10ea38e` of the same fork family). Both
  are carried here unchanged apart from one merge conflict.
- This fork's changes were developed with [Claude Code](https://claude.com/claude-code).

## Status of this fork (2026-11-27, 06:30 UTC)

**Playable, slowly: about 11 world frames per second at the first boat mission at 1,500 to 3,300
draws (usual frame 88 ms), 8.5 at 3,300 and more (115 to 120 ms); the console runs 30. The card is no
longer the limit (53 to 66 ms a frame, the submitting thread waits for it about 0 ms); the thread that
prepares submissions is (65 to 87 ms a frame at work). The
open water now shows waves and the sun's path with no black patches. The tester has played from the opening through the prologue and past
the first boat mission. The graphics card is still lost now and then 30 to 50 minutes into a session,
before the title's next save point; cause not known yet. **New: with the ray-tracing structure builder on
(the default) the title's ray-traced shadows and light now show once a scene has streamed in (tester,
2026-11-27), but the frame rate falls to about 0.2 to 3 a second while it runs; set
`VICTORY_BVH_BUILDER=0` to play at the speeds above.**
Tested on one machine: Windows 11, Intel i7-14700KF, NVIDIA RTX 4070 12 GB,
32 GB RAM. The Series X profile is used throughout.

| Stage | State in this fork |
|-------|--------------------|
| Boot, menus, start screen | works, 30 fps (as upstream) |
| Opening cutscene | plays from start to finish, in order, lit: title cards, credits cards, night and dusk shots |
| Saves | the game autosaves a checkpoint and loads it again; test runs continue from the last checkpoint |
| The prologue and the first missions | play: characters, textures, sky, sunlit exteriors, vehicles and boats; HUD, pause menu and pad input work. Played past the first boat mission (2026-11-25) |
| Water | **2026-11-27: no black or grey patches on open water** once the two 64-lane water programs (5dc3b25986622949, 6f225b641c5b0708) are no longer forced into the wave-wide form (leave them out of `VICTORY_WAVE_WIDE_ONLY`). Before: right since `VICTORY_TEXTURE_BACK=1` (pull request #999): boats float, the surface is lit (blue, waves, the sun's path). Without it boats sink and the mission fails |
| Light in shadow | **2026-11-27: ray-traced shadows and light show with the builder on, after a scene has streamed in (minutes at the low frame rate; the first minutes still show stand-in models and black faces).** Without the builder (`VICTORY_BVH_BUILDER=0`) anything the sun does not hit directly is black |
| Frame rate in the world | **2026-11-26 evening: usual world frame 131 ms at 3,300 to 4,100 draws with the card at 80 ms a frame (card hashing a group of 64 threads a piece, now the default; 149 ms and 108 ms of card without it, run 349).** Earlier: 8.2 to 8.6 world frames a second at the first boat mission at 3,000 to 5,000 draws, 9.5 over a whole standing run** (runs 311, 312, 315, 316: frames counted only where every frame is a world frame, not fades or loading screens), with the texture pass on its own thread (`VICTORY_HEAP_WORKER=1`; 6.2 to 6.7 without it). 10 to 14 fps at 500 to 1,500 draws. The thread that prepares submissions is the limit (about 70 ms of a usual frame); the card is at work about 9 ms. It started at 3 to 6 seconds a frame. Measured with the switch set in `diagnostics/README.md`; the defaults are slower |
| Stability | **the card is lost after 30 to 50 minutes of play**: Windows reports the device removed (0x887A0005) 