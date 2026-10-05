# ReSkate

play it offline, host your own lobbies and dedicated servers, and mod it.
the launcher, the runtime that loads into the game, and the dedicated server.

> ReSkate is a fan project. It is not affiliated with or endorsed by Electronic Arts or Full Circle.
> You need your own copy of skate. on Steam.

## Features

- **Offline play.** No EA servers needed. Your skater, outfits, unlocks and progress are saved on your PC,
  and the game runs even with Steam closed.
- **Multiplayer.**
  - Host a Steam lobby for up to 32 players: public, or joined with a code, with an optional password.
  - Join dedicated servers from the in-game server browser.
  - Proximity voice chat, and text chat with emotes and an optional bad-word filter.
  - Parties in lobbies and on dedicated servers: invite, join, leave, promote.
  - Throwdowns with other players (Jam, Spot Battle and S.K.A.T.E.), and co-op challenges.
- **In-game menu and console.**
  - Map and fast travel.
  - World: time of day, population, district levels, rotating parks.
  - The **Park Editor**: place, move and save objects with freecam, snapping and undo.
  - Skater options: first person, movement, boosts, noclip.
  - Progression, controls, graphics and multiplayer settings.
- **Mods.**
  - Drop a mod in `Mods/` and it is merged into the game at launch. Mods can add custom maps, loading
    screens, cosmetics and scripts.
  - Browse and install mods from the [Thunderstore community](https://thunderstore.io/c/reskate/) in the
    launcher.
  - Most mod changes apply in game without a restart.
- **Launcher.**
  - Checks that you have the supported game build, and can download exactly that build with your Steam
    account.
  - Keeps ReSkate itself up to date.

## Getting started

1. Download the latest `ReSkate-<version>.zip` from
   [Releases](https://github.com/Dingo-Shenanigans/ReSkate/releases).
2. Extract `ReSkateLauncher.exe` and `ReSkate.dll` into either folder:
   - **your skate. folder**, beside `Skate.exe` (Steam → skate. → Manage → Browse local files); or
   - **an empty folder**, where the launcher installs the game for you (about 14 GB).
3. Run `ReSkateLauncher.exe`.
   - It checks for ReSkate updates, then checks the game files against the supported build.
   - If the game is missing, or Steam has updated it past the supported build, sign in when asked. You
     can scan a QR code with the Steam app, or use your username and password with Steam Guard. It then
     downloads only the files it needs.
4. Press **PLAY**.

ReSkate supports one game build at a time (Steam build `25414733`).
### Controls

| Key | Opens |
|---|---|
| **Insert** | the ReSkate menu |
| **~** (grave/tilde) | the command console (`help` lists the commands) |
| **T** | chat, in multiplayer |

The menu and console keys can be changed in the launcher's Settings.

### Where things are

| What | Where |
|---|---|
| Mods | `Mods\<mod name>\` beside `Skate.exe`, ordered by `Mods\mods.json` |
| Logs | `logs\ReSkate.log` beside `Skate.exe` |
| Profile (skater, progress, parks) | `%LOCALAPPDATA%\ReSkate\profiles\offline\` |
| The game's own settings and saves | `%LOCALAPPDATA%\ReSkate\Game\` (kept apart from the normal game) |
| Launcher settings | `ReSkateLauncher.settings.json` beside the launcher |

## Mods

- Install mods from the launcher's **MODS** page: browse Thunderstore, or drag a `.zip` or folder onto the
  window.
- In game, the **MODS** tab of the ReSkate menu (**Insert**) turns mods on and off and applies the changes.
- Mods are checked against the game build they were made for. Outdated mods, or mods that can't be merged
  cleanly, are left out with a message naming them, and the rest still load.
- A mod that adds songs can give them their own playlist in the game's music screen with a
  `reskate-music.json` in its folder:

  ```json
  {"schema": 1, "playlists": [{"name": "My Playlist", "songs": ["Artist - Title", "Artist - Other Title"]}]}
  ```

  Each entry is the song's artist and title exactly as the mod registers them, joined by ` - `. Entries that
  match no song are ignored, and a playlist with no matching songs is not shown. A file that does not follow
  this shape is skipped and logged. The songs themselves still have to be added by the mod.

Only install mods you trust. Mods change game data, and custom scripts can run code.

## Dedicated servers

`ReSkateServer.exe` is a headless lobby that needs neither the game nor Steam installed. It is in the
`ReSkateServer-<version>.zip` of each release. See [Server/README.txt](Server/README.txt) for setup,
`ReSkateServer.json`, admin commands, votes and the anti-cheat checks.

### Linux servers

Each release also ships `ReSkateServer-Linux-<version>.zip`: the same headless lobby as a native
x86_64 Linux binary (no Wine, no game install). Setup in short:

```sh
unzip ReSkateServer-Linux-<version>.zip -d reskate-server && cd reskate-server
./setup-linux-server-libs.sh
./ReSkateServer            # writes ReSkateServer.