# WoWee - World Of Warcraft Engine Experiment

<p align="center">
  <img src="assets/Wowee.png" alt="Wowee Logo" width="240" />
</p>

A native C++ World of Warcraft client with a custom Vulkan renderer.

[![Sponsor](https://img.shields.io/github/sponsors/Kelsidavis?label=Sponsor&logo=GitHub)](https://github.com/sponsors/Kelsidavis)
[![Discord](https://img.shields.io/discord/1?label=Discord&logo=discord)](https://discord.gg/SDqjA79B)

[![Watch the video](https://img.youtube.com/vi/B-jtpPmiXGM/maxresdefault.jpg)](https://youtu.be/B-jtpPmiXGM)

[![Watch the video](https://img.youtube.com/vi/Pd9JuYYxu0o/maxresdefault.jpg)](https://youtu.be/Pd9JuYYxu0o)

[![Watch the video](https://img.youtube.com/vi/J4NXegzqWSQ/maxresdefault.jpg)](https://youtu.be/J4NXegzqWSQ)

Protocol Compatible with **Vanilla (Classic) 1.12 + TBC 2.4.3 + WotLK 3.3.5a**.

> **Legal Disclaimer**: This is an educational/research project. It does not include any Blizzard Entertainment assets, data files, or proprietary code. World of Warcraft and all related assets are the property of Blizzard Entertainment, Inc. This project is not affiliated with or endorsed by Blizzard Entertainment. Users are responsible for supplying their own legally obtained game data files and for ensuring compliance with all applicable laws in their jurisdiction.

## Status & Direction (2026-02-18)

- **Compatibility**: **Vanilla (Classic) 1.12 + TBC 2.4.3 + WotLK 3.3.5a** are all supported via expansion profiles and per-expansion packet parsers (`src/game/packet_parsers_classic.cpp`, `src/game/packet_parsers_tbc.cpp`). All three expansions are roughly on par — no single one is significantly more complete than the others.
- **Tested against**: AzerothCore, TrinityCore, and Mangos.
- **Current focus**: protocol correctness across server variants, visual accuracy (M2/WMO edge cases, equipment textures), and multi-expansion coverage.
- **Warden**: Full module execution via Unicorn Engine CPU emulation. Decrypts (RC4→RSA→zlib), parses and relocates the PE module, executes via x86 emulation with Windows API interception. Module cache at `~/.local/share/wowee/warden_cache/`.

## Features

### Rendering Engine
- **Terrain** -- Multi-tile streaming with async loading, texture splatting (4 layers), frustum culling
- **Atmosphere** -- Procedural clouds (FBM noise), lens flare with chromatic aberration, cloud/fog star occlusion
- **Characters** -- Skeletal animation with GPU vertex skinning (256 bones), race-aware textures
- **Buildings** -- WMO renderer with multi-material batches, frustum culling, 160-unit distance culling
- **Particles** -- M2 particle emitters with WotLK struct parsing, billboarded glow effects

### Asset Pipeline
- Extracted loose-file **`Data/`** tree indexed by **`manifest.json`** (fast lookup + caching)
- Optional **overlay layers** for multi-expansion asset deduplication
- `asset_extract` + `extract_assets.sh` (Linux/macOS) / `extract_assets.ps1` (Windows) for MPQ extraction (StormLib tooling)
- File formats: **BLP** (DXT1/3/5), **ADT**, **M2**, **WMO**, **DBC** (Spell/Item/Faction/etc.)

### Gameplay Systems
- **Authentication** -- Full SRP6a implementation with RC4 header encryption
- **Character System** -- Creation (with nonbinary gender option), selection, 3D preview, stats panel, race/class support
- **Movement** -- WASD movement, camera orbit, spline path following
- **Combat** -- Auto-attack, spell casting with cooldowns, damage calculation, death handling
- **Targeting** -- Tab-cycling, click-to-target, faction-based hostility (using Faction.dbc)
- **Inventory** -- 23 equipment slots, 16 backpack slots, drag-drop, auto-equip
- **Spells** -- Spellbook with class specialty tabs, drag-drop to action bar, spell icons
- **Action Bar** -- 12 slots, drag-drop from spellbook/inventory, click-to-cast, keybindings
- **Trainers** -- Spell trainer UI, buy spells, known/available/unavailable states
- **Quests** -- Quest markers (! and ?) on NPCs and minimap, quest log, quest details, turn-in flow
- **Vendors** -- Buy, sell, and buyback (most recent sold item), gold tracking, inventory sync
- **Loot** -- Loot window, gold looting, item pickup
- **Gossip** -- NPC interaction, dialogue options
- **Chat** -- Tabs/channels, emotes, chat bubbles, clickable URLs, clickable item links with tooltips
- **Party** -- Group invites, party list
- **Warden** -- Warden anti-cheat module execution via Unicorn Engine x86 emulation (cross-platform, no Wine)
- **UI** -- Loading screens with progress bar, settings window, minimap with zoom/rotation/square mode, top-right minimap mute speaker, separate bag windows with compact-empty mode (aggregate view)

## Building

### Prerequisites

```bash
# Ubuntu/Debian
sudo apt install libsdl2-dev libglm-dev libssl-dev \
                 libvulkan-dev vulkan-tools glslc \
                 libavformat-dev libavcodec-dev libswscale-dev libavutil-dev \
                 zlib1g-dev cmake build-essential libx11-dev \
                 libunicorn-