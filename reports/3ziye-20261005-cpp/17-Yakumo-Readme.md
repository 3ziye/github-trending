<p align="center"><img src="docs/images/logo.svg" alt="Yakumo" width="720"></p>

<p align="center"><b>English</b> · <a href="README.ru.md">Русский</a> · <a href="README.es.md">Español</a></p>

<p align="center">
  <a href="https://github.com/TeamGDB/Yakumo/releases/latest"><img src="https://img.shields.io/github/v/release/TeamGDB/Yakumo?style=flat-square&amp;label=release&amp;labelColor=2a1a22&amp;color=b98335" alt="Latest stable release"></a>
  <a href="https://github.com/TeamGDB/Yakumo/actions/workflows/tests.yml?query=branch%3Amain"><img src="https://img.shields.io/github/actions/workflow/status/TeamGDB/Yakumo/tests.yml?branch=main&amp;event=push&amp;style=flat-square&amp;label=tests&amp;labelColor=2a1a22" alt="Unit tests on main"></a>
  <a href="docs/COVERAGE.md"><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FTeamGDB%2FYakumo%2Fcoverage-badges%2Fcoverage.json&amp;style=flat-square&amp;cacheSeconds=300" alt="Coverage of measured source lines on main; see scope and unmeasured files"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-b98335?style=flat-square&amp;labelColor=2a1a22" alt="License: MIT"></a>
  <a href="docs/COMPATIBILITY.md"><img src="https://img.shields.io/badge/platforms-Windows%20%C2%B7%20Linux%20%C2%B7%20macOS%20%C2%B7%20Android-b98335?style=flat-square&amp;labelColor=2a1a22" alt="Platforms: Windows, Linux, macOS and Android"></a>
  <a href="https://github.com/TeamGDB/Yakumo/stargazers"><img src="https://img.shields.io/github/stars/TeamGDB/Yakumo?style=flat-square&amp;label=stars&amp;labelColor=2a1a22&amp;color=b98335" alt="GitHub stars"></a>
  <a href="https://github.com/TeamGDB/Yakumo/releases"><img src="https://img.shields.io/github/downloads/TeamGDB/Yakumo/total?style=flat-square&amp;label=downloads&amp;labelColor=2a1a22&amp;color=b98335" alt="GitHub release asset downloads across all releases"></a>
</p>

<p align="center">
  <a href="https://discord.gg/XbQSE3b4m"><img src="https://img.shields.io/badge/Discord-Join%20community-b98335?style=flat-square&amp;logo=discord&amp;logoColor=white&amp;labelColor=2a1a22" alt="Join the TeamGDB Discord community"></a>
</p>

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

You can load a save copied from a PSP or start a new game, hunt, play with other hunters and save your progress, with music, movies and lighting. The game simulation stays at the PSP's 30 frames per second; optional frame interpolation presents it at 45, 60, 90, 120 or the display's refresh rate without changing game speed. Loads are shorter than on a PSP: while the game loads in silence, it runs ahead of rea