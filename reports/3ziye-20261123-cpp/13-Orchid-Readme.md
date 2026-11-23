<!--
# SPDX-FileCopyrightText: Copyright 2025 Eden Emulator Project
# SPDX-License-Identifier: GPL-3.0-or-later

# SPDX-FileCopyrightText: 2018 yuzu Emulator Project
# SPDX-License-Identifier: GPL-2.0-or-later
-->
<!-- lang: en-GB -->

<h1 align="center">
  <br>
  <img src="dist/Orchid.png" alt="Orchid" width="200">
  <br>
  <b>Orchid</b>
  <br>
</h1>

<h4 align="center">A very experimental Switch 2 emulator. Orchid started from
<a href="https://github.com/zortos293/Eglantine">Eglantine</a> and has grown into its own project, with fixes aimed at
Mario Tennis Fever first, plus the shader, kernel and graphics work other games need.</h4>

> [!NOTE]
> Orchid is an independent project. Problems with these builds are not caused by the Eglantine
> or Eden developers, so please do not report them there.

<p align="center">
  <a href="#project-scope">Project scope</a> |
  <a href="#branches-and-builds">Branches and builds</a> |
  <a href="#what-orchid-adds">What Orchid adds</a> |
  <a href="#performance-and-compatibility">Performance</a> |
  <a href="#download">Download</a> |
  <a href="#build-the-newest-commit-yourself">Build it yourself</a> |
  <a href="#documentation">Documentation</a> |
  <a href="#license">License</a>
</p>

Orchid opens NXFormat (`.nx`) game archives directly from the file picker or a game directory.
The reader comes from [nxformat](https://github.com/fab918/nxformat), with the loader adapted
from [Lichii](https://github.com/sheepbun/Lichii/tree/2f0c8df47af2a4de0477839ed54c80b260377ea8).

## Project scope

Orchid's support and development focus is on demonstrably improving these games:

- Mario Tennis Fever
- Hyrule Warriors: Age of Imprisonment
- Pokémon Pokopia
- Star Fox
- Super Mario Bros. Wonder
- Yoshi and the Mysterious Book
- Donkey Kong Bananza
- Kirby Air Riders
- Kirby and the Forgotten Land
- Xenoblade Chronicles: Definitive Edition, 2 and X: Definitive Edition (Switch 1 and Switch 2
  Editions)
- Orbitals

These are the project's target games; inclusion here does not mean a game is already fully
playable or free of issues. See [Performance and compatibility](#performance-and-compatibility)
for the currently reported results and their test conditions.

## Branches and builds

| Branch | Channel | Release name |
|---|---|---|
| `main` | stable | `v0.<minor>.<patch>`, regular release |

`.github/version` sets the minor version; CI counts the patch up. In 0.5 all branches were merged
into `main` (formerly `mario-tennis-fever`), including the experimental `mario-tennis-fever-perf`.

Commits land often, but they do not start a build. Release builds are started by hand
(Actions > release-binaries > Run workflow), so the newest release can be several commits behind
its branch. To run the newest commit, [build it yourself](#build-the-newest-commit-yourself).

## What Orchid adds

Compared with the Eglantine it started from:

- **Mario Tennis Fever:** startup crash fixed, the NVIDIA crash at match start fixed, and per-game
  defaults (low GPU accuracy, balanced fences).
- **Shaders:** many more Ampere instructions lowered (IMAD.WIDE, IADD3 carries, LEA.HI, F2I.U64,
  I2F from 64-bit pairs, bindless TEX modes and others), mainly from the Fire Emblem: Fortune's
  Weave bring-up.
- **System:** Switch 2 built-in fonts served from their own shared memory; kernel thread start and
  finalize races fixed.
- **Graphics:** query reports flushed before MME DMA reads, layered cross-format texture copies,
  separate surface and texture descriptor buffers, geometry shaders and framebuffers kept within
  device limits.
- **Experimental branch only:** a performance pass (buffer cache, puller, memory trap and kernel
  locking changes). Faster on some systems, less tested.
- **Updates:** release builds check this repository for updates and only offer builds of their
  own channel.

## Performance and compatibility

> [!NOTE]
> Measured by hand on Version 0.9.5 on one PC: AMD Ryzen 7 5800X3D, AMD Radeon RX 9070 XT,
> 32 GB RAM, CachyOS (Linux 7.x, Mesa RADV from git), 1x resolution scaling. Other hardware
> will differ.

| Game | FPS | Notes |
|---|---|---|
| Hyrule Warriors: Age of Imprisonment | 60 | drops to 20-40 in Combat |
| Donkey Kong Bananza | 30-40, 15-25 in heavy areas | 30FPS Mod recommended (Built in) |
| Mario Tennis Fever | 60 | runs flawlessly |
| Yoshi and the Mysterious Book | 60 | First Level tested; optional fixed-resolution patch, 1080p/1440p/4K (Built in) |
| Super Mario Bros. Wonder | 160 | custom FPS targets (only set what you can hit) |
| Star Fox | 60 |  |
| Pokémon Pokopia | 60 | |
| Orbitals | 30 | Background Texture flickering |
| Kirby Air Riders |DO NOT PLAY MOST LIKELY CRASHES YOUR PC 30 SECONDS IN A RACE|

## Download

Releases are on the [releases page](https://github.com/MythosOfs/Orchid/releases). Each one has:

| File | For |
|---|---|
| `orchid-<version>-linux-x86_64-pgo.AppImage` | Linux, profile-guided build (preferred) |
| `orchid-<version>-linux-x86_64.AppImage` | Linu