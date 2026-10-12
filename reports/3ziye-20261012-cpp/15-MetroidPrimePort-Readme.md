# Metroid Prime — native port

A native build of **Metroid Prime** (GameCube, USA v1.00, v1.01 or v1.02 `GM8E01`, or PAL `GM8P01` as experimental) for Linux,
Windows and Android. The game is compiled natively from the
[PrimeDecomp](https://github.com/PrimeDecomp/prime) decompiled source and renders
through Aurora (SDL3 and WebGPU), with no emulator involved.

**No game content is included.** You need your own copy of the game: the port
reads it from a disc image and never ships any of its assets. This repository
ships no disc image, and neither does any package or release built from it.

## What it adds over the console release

- Widescreen rendering — 4:3, 16:9 or following the window — with the HUD spread
  to the edges and the menus, pause and map screens aspect-corrected
- An uncapped presentation rate over a fixed-rate simulation, so physics and
  animation stay console-accurate at any frame rate
- Graphics options: first-person FOV, MSAA and anisotropic filtering, HUD scale,
  and toggles to hide the helmet and the visor effects
- Mouse aim and twin-stick aiming, with sensitivity, inversion and crosshair size
- A Controls page for rebinding keyboard, mouse and controller, with a second key
  per action, conflict warnings, controller presets (GameCube, Modern,
  Southpaw), deadzones and gyro aim
- Optional gameplay tweaks, all off by default: Fast Morph (quick morph and
  unmorph that keep momentum), Spring Ball (optionally on a gyro flick), Toggle
  Lock-On and Sticky Charge
- Skippable cutscenes: Start skips cutscenes the console release forces you to
  watch
- Save states (eight slots plus undo, F5/F9) and a reveal-whole-map option with
  an item, scan and room tracker
- An on-screen in-game timer and a LiveSplit Server client that starts, splits
  on upgrades and stops at the credits
- Hard mode, the Fusion Suit and the image galleries can be unlocked without
  beating the game
- Memory card import and export as `.gci` files or raw card images, including
  straight from and to Dolphin
- A mods folder that replaces loose disc files or single resources inside PAKs (or adds new ones),
  user texture packs, HD texture replacements, and in-game button prompts that
  follow the input bound to each action
- Discord Rich Presence on desktop (bring your own Discord application id)
- The common options sit in pause > Options beside the game's own; the F1
  overlay holds everything, in pages for Game, Controls, Video, Remastered,
  Mods, Archipelago, Tracker, Save states, System and Debug (cheats sit behind
  a "Show cheats" box)
- A touch overlay on Android, with a virtual controller for the sticks, triggers,
  shoulders and face buttons

## Randomizer and Archipelago

Both are supported, on all three platforms.

- **Randomizer** — item placement is driven by a seed file. `tools/rando_seed.py`
  generates one and `docs/RANDOMIZER.md` covers the format.
- **Archipelago multiworld** — the Metroid Prime AP world's item and location
  tables are built in. Open F1 > Archipelago, enter the server (`host:port`), your
  slot name and the password if any, and connect; no seed file is needed. The
  seed's options are applied and a new game starts at the Landing Site with
  the intro skipped. Each seed and slot gets its own memory card, checks made
  offline are sent on the next connect, Recent games resumes an earlier seed,
  and the Chat sub-tab shows the server log and sends messages such as `!hint`.
  DeathLink is supported.

  `wss://` needs no extra setup on any platform: OpenSSL is vendored and linked
  statically on Android, and the trust store is enumerated by hand, so the
  system CA bundle is not required. See `docs/ARCHIPELAGO.md`.

Cutscenes are always skippable in randomizer and Archipelago games.

## Downloads

Releases are published on the
[GitHub releases page](https://github.com/Odrannnn/MetroidPrimePort/releases).
Every build needs your own disc image; none of them contains one.

| Platform | Artefact | Notes |
| --- | --- | --- |
| Linux | AppImage | Self-contained, no install. `chmod +x` and run. |
| Linux | Flatpak | `io.github.odrannnn.metroidprimeport` |
| Linux | `.tar.gz` | The bare binary, its textures and the licences |
| Windows | `.zip` | Unzip anywhere; needs a Visual C++ redistributable |
| Android | `.apk` | Sideload; enable install from unknown sources |

Android APKs are signed with a project release key. An app signed with one key
cannot be updated by one signed with another, so keep the key — see
`docs/RELEASING.md`.

## Building

Needs CMake 3.25+, Ninja and a C++20 toolchain. Aurora and MusyX are vendored, so
a normal clone is enough; Aurora fetches its pinned dependencies on the first
configure.

```sh
cmake -S . -B build/native -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DAURORA_ENABLE_TESTS=OFF -DMP_BUILD_TESTS=ON
cmake --build build/native -j 4
ctest --test-dir build/native -L port --output-on-failure
```

On Windows, run from an MSVC developer shell and add
`-DCMAKE_C_CO