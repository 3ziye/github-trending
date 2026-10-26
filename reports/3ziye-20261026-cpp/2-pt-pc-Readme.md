<div align="center">

# P.T. for PC

**A native PC port of P.T., the 2014 PS4 teaser by Kojima Productions. Windows, Linux and macOS.**

<a href="https://www.patreon.com/loreanxavier"><img src="https://img.shields.io/badge/Support%20the%20port%20on%20Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white" alt="Support the port on Patreon" height="48"></a>

<a href="https://github.com/LoreanXavier/pt-pc/releases/latest"><img src="https://img.shields.io/github/v/release/LoreanXavier/pt-pc?style=for-the-badge&label=Download&color=2b2b2b" alt="Download the latest release"></a>
<a href="https://github.com/LoreanXavier/pt-pc/releases"><img src="https://img.shields.io/github/downloads/LoreanXavier/pt-pc/total?style=for-the-badge&color=2b2b2b" alt="Downloads"></a>
<a href="https://discord.gg/3vKwUf2eTb"><img src="https://img.shields.io/badge/Discord-Join-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>

![Lisa in the hallway](docs/media/lisa.gif)

</div>

> [!IMPORTANT]
> **This port is made by one person in their spare time.** If it gave you a good scare, please consider supporting it on [**Patreon**](https://www.patreon.com/loreanxavier). It pays for the testing hardware and keeps the updates coming.

> [!NOTE]
> **Bug reports:** I've closed GitHub Issues because of ongoing spam attacks. Please join the [Discord server](https://discord.gg/3vKwUf2eTb) to report bugs.

This is a native PC port of P.T., the 2014 PS4 teaser by Kojima Productions. It is not an emulator. The game logic was
rebuilt in C++ from the original's behaviour, with Vulkan and DirectX 12 renderers; every level, model, texture, sound,
script and cutscene is read at run time from your own copy of the PS4 game. There is no game data in this repository
and none in the installer.

The port runs on its own engine, Hallway Engine.

I made this in my spare time, with AI tools (see AI Disclosure at the end), because P.T. deserved to keep existing
somewhere other than on consoles that still have it installed. It plays the whole teaser from the first wake-up to
the street, with the voice part included.

## What you need

- Your own copy of P.T. The port is built and tested with the US release, CUSA01127, as a dump folder from your console
  or a fake PKG made from that dump. The folder can have any name: the game recognises it by its files. Other releases,
  such as the European CUSA01114, are accepted the same way, but I have not seen their data myself; the game logs at its
  start what differs from the US data. A store PKG cannot be used: it is encrypted for the console that owns it, and nothing here
  decrypts it.
- Windows 10 or 11 (x64), Linux x86-64 with glibc 2.38 or newer (Ubuntu 24.04, Debian 13, Fedora 39, current Arch
  and SteamOS), or macOS 14 or newer on an Apple silicon or Intel Mac.
- A GPU and driver with Vulkan 1.3; on macOS the port brings MoltenVK, which runs Vulkan on Metal. The optional
  ray-traced shadows, ambient occlusion and reflections need a GPU with Vulkan ray queries (not on macOS). DLSS needs a
  GeForce RTX card. Available upscalers depend on the platform and renderer; see docs/upscaling.md. The settings page greys out what your machine
  cannot run and says why.
- A microphone for one part of the game, as on the PS4. If you have none, `key = J` under `[voice]` in `pt.ini` lets a
  key stand in for the spoken word.

## Installing

Download the installer from the Releases page: `P.T.PC.Port.Setup.exe` on Windows, the Linux setup binary on Linux.
Point it at your dump folder or fake PKG and at a destination folder (the default on Windows is
`%LocalAppData%\Programs\P.T. PC Port`). It copies the three game archives it needs (`chunk1.psarc`,
`texture.qar`, `pathid_list_ps4.bin`) next to the port and makes a shortcut if you want one. The eboot, modules and
system files are not used.

Linux: `chmod +x` the setup and run it from a terminal. The game needs only glibc and the system's Vulkan driver. On a Steam Deck
install from desktop mode and add `pt` as a non-Steam game; it runs on SteamOS as it is.

macOS: download `P.T.PC.Port-macOS-arm64.zip` (M1 and later) or `P.T.PC.Port-macOS-x64.zip` (Intel), unzip `P.T. PC Port.app`,
open it once and allow it under System Settings > Privacy & Security (it is not signed with a Developer ID), then pick your
dump folder when it asks. A fake PKG has to be extracted on Windows or Linux first. Intel Macs need a GPU that MoltenVK can
run the renderer on; the port was written without a Mac at hand and the Intel app has not been run on one yet. More in
docs/macos.md.

Windows and Linux releases include installers and portable ZIPs. To update an existing installation, use the game's update
button or run the new installer over it. Your game archives, settings, saves and mods stay.

On Windows and Linux, settings, saves, logs and cache live in `data/` beside the executable. The game migrates
existing user data without overwriting newer files. On macOS, these stay i