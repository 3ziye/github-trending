<p align="center"><img src="docs/images/icon.png" alt="Playden icon" width="128"></p>

# Playden for PS5

**Play your Steam library's Windows games on a jailbroken PS5.**

[![Discord](https://img.shields.io/discord/1562443095629373590?label=Discord&logo=discord&logoColor=white)](https://discord.gg/wd8UjExpPA)
[![Reddit](https://img.shields.io/badge/Reddit-r%2FPlayden__PS5-FF4500?logo=reddit&logoColor=white)](https://www.reddit.com/r/Playden_PS5/)

Playden is a launcher that runs on the PS5, adapted from [Playden for macOS](https://github.com/leolobato/playden).
You sign in to Steam with a QR code or your account name and password, browse your library, download games, and play them. The Windows games run through
[prospero-win](https://github.com/mpereiraesaa/prospero-win), a port of Wine to the PS5. Each game gets its own
private Windows environment and its own tile on the PS5 Home screen.

> [!WARNING]
> **Alpha software.** Playden is an early, experimental project. It signs in to **your real Steam account**, downloads
> games with your licenses, and reads and writes your **Steam Cloud saves**. Read [Before you use it](#before-you-use-it).
> If you are not comfortable with these risks, do not use it.

![Playden's library on the PS5: Steam games as cover art, with Installed, All, Favorites and Hidden on the side](docs/images/library.jpg)

## Features

- **Steam sign-in with a QR code** (approve it in the Steam mobile app), **or with your account name and password.**
  Steam Guard email codes, Steam Mobile app codes and approval in the app are supported. The sign-in screen opens on
  the method you used last.
- **Your whole Steam library.** Search, sort, favorites, collections, ratings and notes, with cover art and store
  details. The library works offline from a cache.
- **Downloads from Steam.** Queue games and watch progress. The Queue screen also lists the games being prepared, in
  the order they start; Prepare next moves a waiting game to the front.
- **Storage at a glance.** Settings › Storage shows how much space is used and lists installed games by size or
  last played. Select several games and uninstall them together; saves are kept unless you choose otherwise.
- **Each game is its own PS5 app.** It gets a tile on the Home screen, so you can start it without Playden.
- **A private Windows environment per game** ("bottle"), so games do not share settings or files.
- **Steam Cloud saves.** Playden checks your Cloud saves before a game starts and syncs them after it ends. If the
  console and the Cloud disagree, you choose which one to keep. You can turn the automatic sync off in Settings and
  sync by hand from the Saves tab.
- **Per-game settings.** Graphics, frame rate, resolution, controller mapping, and how the game starts: pick any
  program from the game folder, edit its arguments and library overrides, or try a game Playden flagged anyway. A
  game's settings can be exported as a recipe ([format](docs/community-recipes.md)).
- **Graphics.** Direct3D 8–11 through [DXVK](https://github.com/doitsujin/dxvk), Direct3D 12 through
  [vkd3d-proton](https://github.com/HansKristian-Work/vkd3d-proton) (kit 0.11 and later), OpenGL through Mesa's Zink, and
  Vulkan, all on the PS5 GPU's Vulkan driver.
- **Gamepad support.** XInput, DirectInput, Raw Input, Windows.Gaming.Input and the Windows multimedia joystick API,
  with rumble. Games see the DualSense as an Xbox controller.
- **Mouse and keyboard.** Plug a USB mouse and keyboard into the PS5, or use a controller preset: the left stick as a
  mouse, or the D-pad as the arrow keys.
- **Import Windows games.** Add game folders you already have, from a USB drive, an M.2 SSD or over FTP. No Steam
  account is needed. See [Import Windows games](#import-windows-games).
- **Install to internal or external disks.** Console storage, or an exFAT USB drive formatted on a Mac or PC.

See the [compatibility list](COMPATIBILITY.md) for the games we have tested.

### Planned

- Steam game updates
- Other stores (GOG, Epic)
- Support for game launches (Rockstar, EA, Ubisoft)
- Community recipes in the preset chooser

## Before you use it

Playden is alpha software. It is not affiliated with, endorsed by, or supported by Valve. Know these points before
you sign in:

- **It is an unofficial Steam client.** Playden talks to Steam's servers directly, the way the Steam client does. Valve
  does not support third-party clients. We know of no account problems from this, but the risk is yours to accept.
- **Your Steam session stays on the console.** Playden stores a Steam sign-in token on the PS5, **without encryption**.
  On a jailbroken console, anyone with file access (for example through FTP) can read it. To keep it off the console, turn off "Stay
  signed in", then sign in again each time Playden starts.
- **It replaces a game's Steam API.** When Playden prepares a game, it puts
  [gbe_fork](https://github.com/Detanup01/gbe_fork), a Steamworks emulator, in place of the ga