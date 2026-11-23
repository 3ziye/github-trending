# Project ReLink

<a href="https://recomplauncher.com"><picture><source media="(prefers-color-scheme: dark)" srcset="https://recomplauncher.com/assets/press/launcher/badge-light.svg"><img alt="Get it on RecompLauncher" src="https://recomplauncher.com/assets/press/launcher/badge-dark.svg" height="48"></picture></a>

**Zelda OOT Remake Recomp.** An unofficial static recompilation of *The Legend of Zelda: Ocarina of Time* (the Switch 2
remake) into a native Windows game: the game's code is translated to PC code and compiled on your machine, with no emulator.

[Français plus bas](#français)

**Discord:** [join the Project ReLink server](https://discord.gg/RFNUtCQk8j) to ask questions, get help and follow new
versions. Bugs are still best reported as [issues](https://github.com/pixl27/ProjectReLink/issues) with `relink_log.txt`
attached, so they don't get lost.

![The Project ReLink launcher](docs/launcher.png)

**No game files are in this repository.** ReLink builds the game on your PC from your own copy.

## The game version you need

ReLink works with **one version of the game**: the Switch 2 remake with its update installed.

| | |
|---|---|
| Program | `0400486024DEC000` |
| Update | v131072 |
| Build | `e0f3ccfa` |

Other versions do not work: the launcher checks your copy and says so before it installs anything. Your copy is either a
`.nup` file, or the game's `romfs` and `exefs` folders.

## Install and play

1. Download `ReLink-Setup.exe` from the [latest release](https://github.com/pixl27/ProjectReLink/releases/latest).
2. Run it. It downloads ReLink and its tools (about 310 MB), checks them and opens the launcher. Nothing else to install:
   ReLink brings its own compiler and Python.
3. Pick your copy of the game. The launcher looks for `.nup` files in Downloads, Desktop and Documents; you can also choose
   one, drop it on the window, or give the `romfs` and `exefs` folders.
4. Press **Install**. It takes 10 to 45 minutes depending on your CPU; you can keep using the PC.
5. Press **Play**. The desktop and Start menu shortcuts open the launcher from then on.

**With RecompLauncher.** Each release also has `ProjectReLink-<version>-Windows-x64.zip`, the same tools in one file, with a
`recomplauncher.json` that lets [RecompLauncher](https://recomplauncher.com) install ReLink, ask for your copy (the same
version as above), build the game in the same way and start it. Its settings page writes the game's own
`relink_options.ini`; the frame rate goes in `relink_env.txt` beside it.

The first start is long, once (about 16 minutes on our PC): the game prepares its shaders, builds its graphics pipelines
for your driver's cache and makes the compute pipelines play is known to use, with a progress screen. It does that part
again after a graphics driver update, so that the first visit of a place does not stutter while the driver compiles, and
after an update of ReLink that changes the renderer's shader code or state (0.6.3 is one). Since 0.7.6 every PC starts the
same way, whatever its RAM. A PC that ran an earlier version with 20 GB of RAM or more has a pipeline cache file in the game
folder, `mkw_vk_pipelines.bin` (800 MB and more), that nothing reads any more: since 0.7.8 the game deletes it at its first
start, unless `RX_VK_LEAN_PIPELINES=0` in `relink_env.txt` brings back the older start, which uses it.

![Installing](docs/install.png)

![The first start: the night ends as the game gets ready](docs/loading.png)

### What your PC needs

- 64-bit Windows 10 or 11, and a CPU with AVX2.
- A graphics card with Vulkan 1.3 and mesh shaders, with an up-to-date driver: NVIDIA GeForce RTX 20 series or newer, AMD
  Radeon RX 6000 series or newer, Intel Arc. We only tested on NVIDIA. Since 0.7.9 a card without mesh shaders (GeForce GTX
  10 series) gets a picture too, as an experiment: about half the frame rate, and some large rocks missing.
- 8 GB of video memory recommended, 16 GB of RAM or more.
- About 60 GB free while it installs, and an internet connection for the download.

### Updating

The launcher says when a new release is out. **Update** downloads only what changed and builds the game again in the same
folder, from the game files the folder keeps: your `.nup` is not needed again. Saves (`user`), settings and mods are kept.

### Where the files go

- The game: the folder you choose (`Games\ReLink` in your user folder by default). Your copy is never changed.
- ReLink itself: `%LOCALAPPDATA%\ReLink`. The build files (about 4 GB) are deleted once the game is ready.
- To uninstall: delete the game folder, `%LOCALAPPDATA%\ReLink` and the shortcuts.

## Settings

The launcher sets the display (full screen, 3D render resolution, upscaling, sharpness, ultrawide), the smoothness (60
frames a second or unlocked, frame generation), the game's language and the controls. It can put the display at 60 Hz while
you play, so that every frame lasts the same time on a 100 or 144 Hz display, and puts the display's own rate back
a