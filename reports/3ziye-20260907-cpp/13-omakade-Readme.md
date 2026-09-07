# Omakade

[![CI](https://github.com/btsouth/omakade/actions/workflows/ci.yml/badge.svg)](https://github.com/btsouth/omakade/actions/workflows/ci.yml)
[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-8cd3cb.svg)](COPYRIGHT)

**Your games, beautifully together.**

[![Omakade library showing installed games from multiple launchers](docs/assets/library-preview.webp)](https://btsouth.github.io/omakade/assets/omakade-demo.mp4)

[Watch the 18-second demo](https://btsouth.github.io/omakade/assets/omakade-demo.mp4)

Omakade is a Linux game library built for Omarchy. It brings
installed Steam, Lutris, Heroic, Faugus, RetroArch, Battle.net, Epic, GOG, and Amazon games
into one quiet, cover-focused home that follows the active Omarchy theme.

[Project homepage](https://btsouth.github.io/omakade/) ·
[Roadmap](PLAN.md) · [Support](SUPPORT.md)

> Omakade is an independent community project. It is not an official Omarchy
> application.

## Features

Omakade 1.7.0 includes:

- Native and Flatpak Steam, Lutris, Heroic, Faugus, RetroArch, PCSX2,
  Ryujinx, Cemu, shadPS4, and Dolphin discovery, plus direct GOG installation
  discovery, including Steam non-Steam shortcuts and games sideloaded into
  Heroic, plus Battle.net games from Wine, Proton, and Bottles prefixes
- Console cards for cartridge and disc systems, with a per-system choice
  between cards and library tiles, per-game pinning, and ROM folder scanning
  for EmuDeck-style layouts
- One-click details and delegated launching through the owning platform
- Omarchy palette, font, transparency, and live theme updates
- Search, favorites, hidden games, sorting, and source filters that combine,
  including one chip for every emulator
- Runtime source controls with scan status and detected locations
- Optional close-after-launch behavior
- Collections, tags, completion states, and smart organization filters
- Local Steam achievements plus optional Web API enrichment
- Optional RetroAchievements progress for supported RetroArch systems
- Optional Steam owned-library sync with installed and ready-to-install views
- Optional IGDB ratings, popularity sorting, and game-length estimates
- SteamGridDB portrait covers with per-game identification and artwork choices
- Adjustable cover size and per-console grouping preferences
- Local, downloaded, and user-selected cover, hero, and logo artwork
- Manual games, preferred installations, extra GOG folders, bulk organization,
  saved filters, a random pick, and personal backup and restore
- Explicit linking for games installed through multiple sources
- ProtonDB and PCGamingWiki shortcuts with actionable launch errors
- Keyboard, mouse, and controller navigation
- Controller-first Couch Mode with Detail and Grid views, on-screen search,
  and controller input that stays with your game after launch
- x86_64 and ARM64 packages, with checksums, SBOMs, and signed provenance
- Optional Sunshine app export so Moonlight can start Omakade or any installed
  game, plus `--play` and `--quit` commands

![Omakade game details showing playtime, IGDB insights, and Steam achievements](docs/assets/game-details.webp)

Omakade reads launcher data without modifying it. Core discovery, browsing,
artwork, and launching work offline. Run `omakade --demo` to explore the UI
with a deterministic fictional library.

Direct GOG discovery checks `~/GOG Games`, `~/Games/GOG`, `~/Games/Heroic`,
and immediate game folders under `~/Games`. In Settings, use **Extra GOG Folders**
to add library folders by path or through the desktop folder picker. Saved folders
are scanned alongside the standard locations. `OMAKADE_GOG_LIBRARY_PATHS` remains
an additive, colon-separated list of extra roots. Missing folders keep their
cached games while available folders refresh. Removing a saved folder does not
delete its game files or personal library choices. Native Linux builds
launch directly; Windows game builds run on Linux through `umu-run` with an
isolated per-game prefix. Omakade itself does not run on Windows.
GOG games installed through Heroic continue to launch through Heroic.

ARM64 packages pass automated build and lifecycle checks; testing on an Omarchy
ARM64 device is still open in [issue #13](https://github.com/btsouth/omakade/issues/13).
On Apple Silicon with Asahi Linux, Omakade installs and discovers Steam games,
but the `fex-steam` wrapper that provides `/usr/bin/steam` can fail to start
games from any `steam://` request, including Steam's own client. That is a
wrapper limitation, not something Omakade can work around; see issue #13 for
the details and workarounds reported so far.

## Install on Omarchy or Arch

### Install or upgrade from the Omarchy Package Repository

On Omarchy, install Omakade from OPR with:

```bash
sudo pacman -S omarchy/omakade
```

After that, Omakade updates with normal Omarchy system updates.

### Install or upgrade from the terminal

These commands are for x86_64. For ARM64, replace `x86_64` with `a