<p align="center"><img src="docs/images/logo.svg" alt="Yakumo" width="720"></p>

<p align="center"><b>English</b> · <a href="README.ru.md">Русский</a> · <a href="README.es.md">Español</a></p>

# Yakumo

A native port of **Monster Hunter Portable 3rd HD Ver.** made by static recompilation: the game's PSP code is translated ahead of time into C++ and compiled for your machine, then run on a reimplementation of the PSP system software. It is not an emulator — there is no interpreter or JIT at the heart of it — and it is not a decompilation.

> **This project does not include any game assets.** You must provide the files from your own legally obtained copy of Monster Hunter Portable 3rd HD Ver. (`NPJB-40001`) to install or build Yakumo.

## Legal disclaimer

**Yakumo** is an independent, open-source project and is not affiliated with, authorized by, sponsored by, or endorsed by CAPCOM, Sony, or any of their affiliates.

Monster Hunter, Monster Hunter Portable 3rd HD Ver., CAPCOM, PlayStation, PSP, and all related trademarks, game assets, artwork, audio, characters, and other intellectual property belong to their respective owners.

**Yakumo** does not include any game assets or original game files: no disc image, no copy of the game's executable or data, and no textures, models, audio or video from the game. You must provide the files from your own legally obtained copy of Monster Hunter Portable 3rd HD Ver. to install or build **Yakumo**; the installer checks that copy and accepts only the original release.

To use **Yakumo**, users must provide the required files from their own legally obtained copy of Monster Hunter Portable 3rd HD Ver. for PlayStation 3.

Users are solely responsible for obtaining, dumping, extracting, and using their game copy in accordance with the laws applicable in their jurisdiction.

**Yakumo** does not support, provide, link to, or encourage the use of unauthorized or pirated copies of the game.

Any references to the original game or its trademarks are made solely for identification, compatibility, and interoperability purposes.

Screenshots and other depictions of the original game may be used solely to document or demonstrate **Yakumo's** functionality. All depicted third-party game content remains the property of its respective rights holders.

The license covering **Yakumo** applies only to the project's own original code and materials and does not grant any rights to third-party intellectual property.

**Yakumo** provides the software, not the game. You must provide your own legally obtained copy.

## Status: playable

You can load a save copied from a PSP or start a new game, hunt, play with other hunters and save your progress, with music, movies and lighting. The game simulation stays at the PSP's 30 frames per second; optional frame interpolation presents it at 45, 60, 90, 120 or the display's refresh rate without changing game speed. Loads are shorter than on a PSP: while the game loads in silence, it runs ahead of real time (*Fast loading*, on by default).

| Works | Missing or rough |
| --- | --- |
| Booting, menus, character creation, the village and hunting areas | |
| Saves in the PSP's own format, including saves and downloaded quests copied from a PSP; import, export and backups from the menu | Curved surfaces (#10); the save-data dialogs draw nothing yet (#33) |
| Vulkan graphics: models, animation, textures, transparency, lighting and fog; adjustable internal resolution, arbitrary window shapes and frame interpolation | |
| PPSSPP-compatible HD texture packs, installed from the menu or copied into the data directory | |
| Mods in the community's mhp3reload format: file replacements and patches, managed from the menu (see the [profile README](profiles/mhp3rd/README.md#mods)) | Code mods (#81) |
| Sound effects, streamed music and cutscene movies | |
| Fully rebindable keyboard and mouse controls; gamepads with an analog right-stick camera and aim, control presets and button-combination binds | |
| Yakumo's in-game menu, first-run setup, file browser and on-screen keyboard, all usable with a gamepad, keyboard or mouse | |
| All 355 code overlays recompiled | |
| Multiplayer: through the ad hoc servers PSP players use, or hosted from the game on a LAN or VPN | |

Tested on macOS (Apple Silicon, Vulkan through MoltenVK), on a Steam Deck in Game Mode with native Vulkan and the built-in controls, and on Windows 11 with MSVC.

The state of each part of the game on each platform is in [`docs/COMPATIBILITY.md`](docs/COMPATIBILITY.md).

## Play

A prebuilt release needs nothing but your disc image. Download one from the [releases page](https://github.com/TeamGDB/Yakumo/releases), start it, and point the first-run setup at your image: it checks the image, prepares the game from it and keeps everything in a per-user directory.

- **Linux and Steam Deck:** a Flatpak bundle and a portable tarball. [`docs/LINUX.md`](docs/LINUX.md) covers installing, the first start, Game Mode, w