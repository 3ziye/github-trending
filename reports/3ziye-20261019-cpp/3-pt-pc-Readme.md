# P.T. for PC

![Lisa in the hallway](docs/media/lisa.gif)

If the port is worth something to you, you can buy me a coffee: [ko-fi.com/loreanxavier](https://ko-fi.com/loreanxavier). It keeps the testing hardware and the releases coming.

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
  or a fake PKG made from that dump. The European and Japanese releases install too, with a note, but I have not seen
  their data myself. A store PKG cannot be used: it is encrypted for the console that owns it, and nothing here
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
existing user data without overwriting newer files. On macOS, these stay in `~/Library/Application Support/pt-port/pt/`.
The game checks GitHub Releases for a newer version at startup; `[network] check_updates = 0` disables that check.

Thanks to ahm3texe for the Apple silicon port, totsu0jv for Czech translation, and yewhochen for the Linux library-loading
and startup-focus fixes.

## Playing

Mouse and WASD, right mouse button to zoom, left button, Enter or E to interact, Esc for the pause menu, Alt+Enter for
fullscreen, F10 for the PC settings. Any gamepad works as the PS4 pad; the button prompts follow whatever you used
last (keyboard, PlayStation, Xbox or Switch). Vibration follows the original's patterns. The in-game options
(brightness, subtitles, camera inversion) are the original ones, and as on the PS4 the option screen and the preface
only play on a first start.

## What the port adds

The Original preset keeps the PS4 look. The port also includes the following features.

Display and image
- Windowed, borderless or exclusive fullscreen, with a selectable render resolution and v-sync on or off. Exclusive
  fullscreen lists supported display modes; borderless keeps the desktop window and can render at another selected size.
- Upscalers: AMD FSR 3.1 and FSR 4, NVIDIA DLSS (with a choice of model) and Intel XeSS, in the usual quality steps or a
  custom scale, plus na