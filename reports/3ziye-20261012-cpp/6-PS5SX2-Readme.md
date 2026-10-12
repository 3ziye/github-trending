<p align="center">
  <img src="ps5/docs/banner.png" alt="PS5SX2" width="100%">
</p>

<h3 align="center">PCSX2, the PS2 emulator, running natively on a jailbroken PS5.</h3>

<p align="center">
  <img alt="Platform: jailbroken PS5" src="https://img.shields.io/badge/platform-jailbroken%20PS5-8c6bff">
  <img alt="Renderer: Vulkan" src="https://img.shields.io/badge/renderer-Vulkan-6f55d9">
  <img alt="Based on PCSX2" src="https://img.shields.io/badge/based%20on-PCSX2-5a45c8">
  <img alt="Licence: GPL-3.0-or-later" src="https://img.shields.io/badge/licence-GPL--3.0--or--later-3d3a8c">
</p>

---

## What is PS5SX2?

PS5SX2 is a port of [PCSX2](https://github.com/PCSX2/pcsx2) to the PS5. It runs as a native app on a jailbroken console:

- PCSX2's recompilers run straight on the PS5's CPU.
- Its Vulkan renderer draws through a modified version of ps5vk, [Mihawk-99](https://github.com/mihawk-99)'s native Vulkan driver for the PS5's GPU ([PS5_Vulkan](https://github.com/mihawk-99/PS5_Vulkan)), tweaked specifically for PS5SX2.
- You pick a game from a cover-flow shelf and play it upscaled on a 4K TV.
- You change its settings from your phone while you play.

## A passion project

PS5SX2 is a passion project. It started as a "can this even work?" experiment, done in spare time out of love for the PS2's library and the fun of seeing those games on new hardware. There's no company or schedule behind it, and nothing is for sale.

Expect rough edges. Bug reports with logs are very welcome, and so is patience.

## Highlights

- **Native, not streamed.** The emulator, its recompilers and its renderer all run on the console itself.
- **Up to 6x native resolution.** PCSX2's hardware renderer runs on Vulkan with 4K output, and FSR is one of the display filters.
- **A shelf for your games.** A 3D cover flow of your library. Covers download automatically the first time you start it. Games play from `.iso`, `.chd`, `.cso` and `.zso` files, and each is titled from its serial in PCSX2's game database, whatever the file is called.
- **Settings from your phone.** The shelf shows a QR code: scan it, or type the address under it (`http://<PS5 IP>:<port>/`) into any browser on the same network, and a settings page opens. Triangle on the shelf shows the QR code large.
  - Change the resolution, aspect ratio, filters, patches and more, for all games or one game.
  - Most changes apply while you play.
  - In a game, hold L2 + D-pad Down for 2 seconds to open the page in the PS5's own web browser. The game keeps running.
- **Widescreen and 60 FPS patches.** Put PCSX2 patch files (`.pnach`) in `/data/PCSX2/patches/` and switch them on per game from the settings page.
- **RetroAchievements.** Sign in on the shelf and earn [RetroAchievements](https://retroachievements.org) as you play (softcore). Unlocks pop up like PS5 trophies, with the badge and the trophy sound, and every game's list is in its Square menu. [RetroAchievements](#retroachievements) has the details.
- **Online play.** PCSX2's emulated network adapter is on for every game and goes out through the PS5's own connection. SOCOM II has played online matches on [PS Rewired](https://psrewired.com)'s revival servers.
- **Recommended settings** for the games played during development, one tap away on the settings page.
- **Bigger memory cards.** Make blank 8, 16, 32 or 64 MB cards on the settings page and pick the card in each slot, for all games or for one.
- **HD texture packs in one button.** Press Square on a game to download its HD texture pack from archive.org's [PCSX2 HD Texture Packs](https://archive.org/details/pcsx2-hd-texture-packs) collection (about 340 games). It installs itself. Your own PNG or DDS packs work too, kept on the console, on a USB drive or in any folder you name.
- **Rumble and an FPS graph.** The game's vibration goes to the controller, at the strength you choose, and a blue frame-rate graph can sit in the corner of the picture. The settings page switches them on and off, and chooses what the info box shows.
- **Up to 4 players** with a multitap: the other PS5 users logged in when the game starts play on their own controllers.
- **Fast forward** (experimental) on a button combo you choose, to skip videos.
- **Games, BIOS and textures on a USB drive.** Games are found in the drive's top folder, `games/`, `PCSX2/games/` and `PS5SX2/games/`; a BIOS in `bios/`, `PCSX2/bios/` or `PS5SX2/bios/`.
- **USB keyboard and mouse** play as the PS2 controller, with PCSX2's own keys. This doesn't work on firmware 11.x and 12.00 yet: see [Known limitations](#known-limitations).
- **Logs that survive.** The last sessions' boot, emulator and settings logs stay on the console, so a problem can be tracked down afterwards. When a game runs slow, a built-in profiler notes in the log which part of the emulator the time went to: logs from slow games are the most useful ones to send.

## What you need

- **A jailbroken PS5.** Development happens on a PS5 Pro on firmware 11.40. Testers ha