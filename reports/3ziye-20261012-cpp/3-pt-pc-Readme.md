# P.T. for PC

![Lisa in the hallway](docs/media/lisa.gif)

If the port is worth something to you, you can buy me a coffee: [patreon.com/loreanxavier](https://www.patreon.com/loreanxavier). It keeps the testing hardware and the releases coming.

This is a native PC port of P.T., the 2014 PS4 teaser by Kojima Productions. It is not an emulator. The game logic was
rebuilt in C++ from the original's behaviour and the renderer is written on Vulkan; every level, model, texture, sound,
script and cutscene is read at run time from your own copy of the PS4 game. There is no game data in this repository
and none in the installer.

I made this in my spare time, with AI tools (see AI Disclosure at the end), because P.T. deserved to keep existing
somewhere other than on consoles that still have it installed. It plays the whole teaser from the first wake-up to
the street, with the voice part included.

## What you need

- Your own copy of P.T. The port is built and tested with the US release, CUSA01127, as a dump folder from your console
  or a fake PKG made from that dump. The European and Japanese releases install too, with a note, but I have not seen
  their data myself. A store PKG cannot be used: it is encrypted for the console that owns it, and nothing here
  decrypts it.
- Windows 10 or 11 (x64), Linux x86-64 with glibc 2.38 or newer (Ubuntu 24.04, Debian 13, Fedora 39, current Arch
  and SteamOS), or macOS 14 or newer on an Apple silicon or Intel Mac.
- A GPU and driver with Vulkan 1.3; on macOS the port brings MoltenVK, which runs Vulkan on Metal. The optional
  ray-traced shadows, ambient occlusion and reflections need a GPU with Vulkan ray queries (not on macOS). DLSS needs a
  GeForce RTX card; FSR and XeSS run on any recent GPU (Windows only). The settings page greys out what your machine
  cannot run and says why.
- A microphone for one part of the game, as on the PS4 (saying "Jack"). **No microphone? No problem, and no file to
  edit:** open **PC settings > Sound**, turn on **Assign J / L2 + R2 for the microphone trigger**, then press **J** on
  the keyboard or **both triggers together** on a controller when the game is listening.

## Installing

Download the installer from the Releases page: `P.T.PC.Port.Setup.exe` on Windows, the Linux setup binary on Linux.
Point it at your dump folder or fake PKG and at a destination folder (the default on Windows is
`%LocalAppData%\Programs\P.T. PC Port`). It copies the three game archives it needs (`chunk1.psarc`,
`texture.qar`, `pathid_list_ps4.bin`) next to the port and makes a desktop shortcut if you want one. The shortcut
uses `icon0.png` from your own copy, the icon the PS4 shows for the game. This repository does not contain the
package or that image: the installer reads it from the PKG or dump you select. The eboot, modules and the rest of
`sce_sys` are not used.

Linux: `chmod +x` the setup and run it, from a terminal or from the file manager (it uses zenity or kdialog for its windows). The game needs only glibc and the system's Vulkan driver. On a Steam Deck
install from desktop mode and add `pt` as a non-Steam game; it runs on SteamOS as it is.

macOS: download `P.T.PC.Port-macOS-arm64.zip` (M1 and later) or `P.T.PC.Port-macOS-x64.zip` (Intel), unzip `P.T. PC Port.app`,
open it once and allow it under System Settings > Privacy & Security (it is not signed with a Developer ID), then pick your
dump folder when it asks. A fake PKG has to be extracted on Windows or Linux first. Intel Macs need a GPU that MoltenVK can
run the renderer on; the port was written without a Mac at hand and the Intel app has not been run on one yet. More in
docs/macos.md.

Portable downloads: `P.T.PC.Port-portable-windows.zip` and `P.T.PC.Port-portable-linux.zip` hold the same files the
setups install. Unpack one anywhere you can write to, then either put your extracted `CUSA01127` folder next to `pt.exe`
(`pt` on Linux) or pick the folder when the game asks at the first start. The macOS app zips work the same way. Game
archives are never included; the setups also accept a fake PKG, the portable zips need the extracted folder.

Settings, saves, logs and caches live in `data/` beside the executable on Windows and Linux, so a whole game folder can
be moved or copied; an older profile is migrated once without overwriting newer files. On macOS they stay in
`~/Library/Application Support/pt-port/pt/`. The game checks GitHub Releases for a newer version at startup;
`[network] check_updates = 0` disables that check.

Thanks to ahm3texe for the Apple silicon port(even though he is an easy ragebaitted dumbass), totsu0jv for Czech translation, GrzybDev for Polish translation, and yewhochen for the Linux library-loading
and startup-focus fixes. Their contributions are incorporated here, with platform and release changes adapted for 1.0.2.

## Playing

Mouse and WASD, right mouse button to zoom, left button, Enter or E to interact, Esc for the pause menu, Alt+Enter for
fullscreen, F10 for the PC