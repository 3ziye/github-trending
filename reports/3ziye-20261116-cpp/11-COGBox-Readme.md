# Gears of War Native - PC ports of Gears of War, Gears of War 2, Gears of War 3 and Gears of War: Judgment

Hello all, I'm Shagg. These are my personal **native Windows versions** of the four Xbox 360 Gears of War games, made by static
recompilation, with a launcher called **COGBox** that sets up your own copy of each game and starts it. This franchise
is one of my favourites, so the project is near and dear to my heart.

**Fully playable** with a few hiccups - if you hit one, please send a problem report (see below).

**COGBox is back on GitHub!** This is our home again, and we're keeping [GitLab](https://gitlab.com/shagg88/cogbox) as a full backup
with the same releases.

**[Download the latest release](https://github.com/Shagg88/COGBox/releases)** · You need your own copy of each game
and its title update. No game files are included, ever.

**Online multiplayer is here (0.6.0):** play Gears of War online with friends again, peer to peer through COGBox's own
matchmaking - no Xbox Live needed. Off until you turn it on in the launcher's Social tab.

**[Join the COGBox Discord](https://discord.gg/Y6qGbzBKQZ)** - find people to play with, get help, share feedback.

<a href="https://recomplauncher.com/game/cogbox"><img src="https://recomplauncher.com/assets/press/launcher/badge-dark.svg" alt="Get it on RecompLauncher" height="56"></a>

COGBox is on RecompLauncher, the free home for recompiled PC games. Get it straight from its developer:
https://recomplauncher.com/game/cogbox

> An unofficial fan project, not affiliated with Microsoft, Epic Games or The Coalition. "Gears of War", "Xbox" and
> "Xbox 360" are trademarks of Microsoft.

---

## The games

| Game | Tested disc | Tested title update | Status |
|---|---|---|---|
| Gears of War | Game version 0.0.0.1 | Title Update 5 (version 0.0.5.1) | Playable |
| Gears of War 2 | US disc, game version 0.0.0.5 | Title Update 6 (version 0.0.6.5) | Every chapter plays in testing |
| Gears of War 3 | Game version 0.0.0.11 | Title Update 6 (version 0.0.6.11) | Playable |
| Gears of War: Judgment | Game version 0.0.0.9 | Title Update 4 (version 0.0.4.9) | Playable |

Title updates are required; disc-only copies aren't supported. The versions are the ones the game itself reports
(with the title update applied, the third number is the update's).

Players have also reported other copies working, most likely other regions' releases: Gears of War, 2 copies of the
disc; Gears of War 2, 1 of the title update; Gears of War 3, 5 of the title update; Judgment, 1 of the disc and 4 of
the title update. COGBox checks your copy when you add it: a tested or reported copy is accepted as it is, any other
copy is marked "untested" - it may work, but please try a tested one before reporting a problem. Each game's page in
the launcher shows the same versions.

## Features

The games' Xbox 360 code is translated ahead of time into ordinary Windows programs - no emulator runs while you play -
and our own renderer draws every frame on Direct3D 12 (or Vulkan).

- **Any resolution** up to 5K, or matched to your monitor, with real extra detail; **ultrawide** up to 48:9 (three
  screens) and **HDR10**.
- **Modern lighting extras** (experimental, off by default): XeGTAO or CACAO ambient occlusion, PCSS soft shadows
  (Gears 3 and Judgment) and screen-space indirect lighting.
- **Upscaling and anti-aliasing:** SMAA, AMD FSR, NVIDIA DLSS and Intel XeSS (experimental).
- **High frame rates:** the 30 fps limit lifted, frame-rate caps from 30 to 180 (and 40 / 45 for the Steam Deck), and
  frame generation (AMD FSR, NVIDIA DLSS on RTX 40/50; experimental).
- **Lower input lag:** NVIDIA Reflex and AMD Anti-Lag 2 where your GPU has them.
- **Keyboard and mouse** or **Xbox / PlayStation controllers**, with button prompts that follow what you use, and
  DualSense adaptive triggers in all four games (experimental, off by default).
- **Split-screen co-op** in all four games, and **System Link** LAN co-op (experimental).
- **Online multiplayer** (0.6.0, off by default): peer to peer through COGBox's own matchmaking.
- **Insane from the start**, **achievements** in all four games, chapter select, and an **in-game menu**
  (Back + Start, or F1) to change settings or quit.
- **DLC and mods**, every language your copy has, and screenshots with **\\**.

## What you need

- **Windows 10 or 11, 64-bit** (or Linux / Steam Deck through Proton, or a Mac with Apple Silicon through CrossOver -
  both experimental).
- **A CPU with AVX2** (roughly 2013 or newer) and **a DirectX 12 graphics card** (under Proton: a graphics driver with
  Vulkan 1.3, such as a recent Mesa or NVIDIA driver).
- **Your own copy of each game** - a disc image (.iso), a Games on Demand copy or the disc's extracted files - and its
  **title update**, copied from your console's `Content\0000000000000000\<title ID>\000B0000\` folder
  (Gears of War `4D5307D5`, Gears 2 `4D53082D`, Gears 3 `4D5308AB`, Judgment `4D530A26`).
- About 8-16 GB of free space p