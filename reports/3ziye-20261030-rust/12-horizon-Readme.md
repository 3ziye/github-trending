<p align="center">
  <img src="docs/media/banner.webp" alt="Horizon: Minecraft: Java Edition 26.3, rewritten in Rust and checked against vanilla by more than 300 differential harnesses" width="100%">
</p>

<p align="center">
  <a href="https://github.com/horizon-rust/horizon/actions/workflows/ci.yml"><img src="https://github.com/horizon-rust/horizon/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI"></a>
  <img src="https://img.shields.io/badge/Minecraft-Java%2026.3-5D9C3F" alt="Minecraft Java 26.3">
  <img src="https://img.shields.io/badge/Rust-stable-B7410E?logo=rust&logoColor=white" alt="Rust">
  <img src="https://img.shields.io/badge/vanilla%20parity-100%25-F0795A" alt="Vanilla parity 100%">
  <a href="#project-status"><img src="https://img.shields.io/badge/player--visible%20gaps-833%20open-F0795A" alt="Player-visible gaps open"></a>
  <img src="https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-2A2470" alt="Linux, macOS and Windows">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-3B2F7E" alt="MIT license"></a>
</p>

<p align="center">
  <a href="https://playhorizon.dev"><b>Website</b></a> ·
  <a href="#download"><b>Download</b></a> ·
  <a href="https://playhorizon.dev/docs/"><b>Documentation</b></a> ·
  <a href="https://github.com/horizon-rust/horizon/releases"><b>Release notes</b></a> ·
  <a href="ROADMAP.md"><b>Roadmap</b></a> ·
  <a href="#project-status"><b>Project status</b></a> ·
  <a href="#contributing"><b>Contributing</b></a>
</p>

# Horizon

Horizon is Minecraft: Java Edition 26.3 rewritten in Rust: a native game that reads the same worlds, follows the same rules and generates the same terrain as the Java game, and is checked against it by more than 300 differential harnesses. You play it through a small launcher, on the files from your own copy of Minecraft. It is free, open source and unofficial.

> Not an official Minecraft product. Not approved by or associated with Mojang or Microsoft. Horizon contains no Minecraft code, assets or data: you need your own legally obtained copy of Minecraft: Java Edition 26.3.

## Download

Horizon is installed through **the Horizon launcher**. Get it from [playhorizon.dev](https://playhorizon.dev) (the Download button picks your system) or from [the launcher releases](https://github.com/horizon-rust/horizon/releases?q=launcher-v&expanded=true), for Linux x86-64, macOS on Apple Silicon or Windows x64. The launcher installs the game and keeps it up to date with each new build (Horizon ships on one channel, the Nightly), prepares its files from your copy of Minecraft (your own install, or downloaded from Mojang for your account), and updates itself.

**You need** a Microsoft account that owns Minecraft: Java Edition (the launcher signs in with it, as other launchers do; see [Microsoft account](docs/microsoft-account.md)) and a GPU with Vulkan or OpenGL 3.3 on Linux, Vulkan or DirectX 12 on Windows, or any Apple Silicon Mac. Nothing else: with no Minecraft on your computer, Play downloads 26.3 and the Java it needs from Mojang for your account, as the official launcher does, then prepares it once. An install you already have (the official launcher, Prism, MultiMC and other launchers all work) is used instead. Step by step, with macOS's first-open prompt and the first launch: [Install and first launch](https://playhorizon.dev/docs/install).

<table>
  <tr>
    <td width="50%"><img src="docs/media/launcher-play.webp" alt="The launcher's Play page: a version ready to play, its summary, Client and Server, the version picker and Play"></td>
    <td width="50%"><img src="docs/media/launcher-patch-notes.webp" alt="The launcher's Patch notes page"></td>
  </tr>
</table>

## What works today

The [documentation](https://playhorizon.dev/docs/) covers each of these.

- **The game:** singleplayer with vanilla's world generation, mobs, villagers, raids, redstone, every command, the HUD and the recipe book, on saves in vanilla's format. Worlds from 1.8 to 26.2 are upgraded as vanilla does. [Status table](#project-status).
- **Horizon's own extras:** new menus (vanilla's are one setting away), graphics presets, distant terrain up to 1024 chunks, controller support, optional zoom, minimap and more, all off by default where they would change the vanilla look. See [Settings](https://playhorizon.dev/docs/settings).
- **Resource packs and data packs:** resource packs work, and data packs load functions, predicates, item modifiers and world generation (vanilla's heights and biomes for now).
- **Playing with others:** invite friends from the pause menu's Friends button with a code, Open to LAN, and joining servers, online-mode ones with the Microsoft account the launcher signs in with. See [Multiplayer](https://playhorizon.dev/docs/multiplayer).
- **Mods:** content mods add blocks, items and data, and native mods change the game's own Rust code, built by the launcher on your copy, with no Rust to install. Horizon's own (Zoom, FP