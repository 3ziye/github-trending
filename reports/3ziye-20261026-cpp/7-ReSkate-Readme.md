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
  - Throwdowns with other players (Jam, Spot Battle and S.K.A.T.E.), and co-op challenges. Plugins add
    throwdown modes of their own to the Throwdowns page ([contrib/throwdown-kit.md](contrib/throwdown-kit.md)).
- **In-game menu and console.**
  - Map and fast travel.
  - World: time of day, population, district levels, rotating parks.
  - The **Park Editor**: place, move and save objects with freecam, snapping and undo. Save a selection as a
    set and place it again anywhere, on any map.
  - Skater options: first person, movement, boosts, noclip.
  - Hall of Meat, grind exit triggers, Board Break, Road Rash and the FPV drone are plugin mods now,
    installed like any other mod. Board Break and Road Rash ship inside their asset mods.
  - Progression, controls, graphics and multiplayer settings.
- **Mods.**
  - Drop a mod in `Mods/` and it is merged into the game at launch. Mods can add custom maps, loading
    screens, cosmetics and scripts.
  - Browse and install mods from the [Thunderstore community](https://thunderstore.io/c/reskate/) in the
    launcher. A mod that needs others (a mod pack) brings them with it.
  - Save sets of mods as profiles, switch between them, and share one as a code or a file.
  - Most mod changes apply in game without a restart.
- **Launcher.**
  - Checks that you have the supported game build, and can download exactly that build with your Steam
    account.
  - Keeps ReSkate itself up to date.

## Getting started

1. Download the latest `ReSkate-<version>.zip` from
   [Releases](https://github.com/Dingo-Shenanigans/ReSkate/releases).
2. Extract `ReSkateLauncher.exe` and `ReSkate.dll` into **a new, empty folder of their own**, for
   example `C:\Games\ReSkate`. Do **not** put them in Steam's skate. folder: ReSkate keeps its own
   copy of the game there, so Steam updating skate. cannot break it.
3. Run `ReSkateLauncher.exe`.
   - It checks for ReSkate updates, then installs the supported build of the game into that folder
     (about 14 GB of free space).
   - Sign in to Steam when asked, with the account that owns skate. You can scan a QR code with the
     Steam app, or use your username and password with Steam Guard.
   - On later runs it checks the game files and downloads only what is missing.
4. Press **PLAY**.

ReSkate supports one game build at a time (Steam build `25414733`).

### Linux (Proton)

1. Install skate. with Steam, and put `ReSkateLauncher.exe` and `ReSkate.dll` in a new, empty folder
   of their own, for example `~/Games/ReSkate` (not Steam's skate. folder: the launcher refuses to
   run from there).
2. In Steam → skate. → Properties → Launch Options, enter this with your own folder's path:

   ```
   bash -c 'exec "${@/*EAAntiCheat.GameServiceLauncher.exe//home/you/Games/ReSkate/ReSkateLauncher.exe}"' -- %command%
   ```

3. Press **Play** on skate. in your Steam library. The launcher installs its own copy of the game
   into that folder the first time.

Steam starts EA's anti-cheat launcher (`EAAntiCheat.GameServiceLauncher.exe`), not `Skate.exe`, and the
anti-cheat refuses to run under Proton (*E111000B … Wine, Proton, and Steam Deck are not supported*).
The launch option swaps it for ReSkate's launcher, which starts the game itself. Launching from the game's
own Steam entry, rather than adding the launcher as a non-Steam game, keeps skate.'s app ID and its
Proton prefix.

The launcher in a folder of its own is new and has not been tested on Proton yet. With the launcher
beside `Skate.exe`, as it was set up before, ReSkate 1.1.3 was tested with Proton Experimental on
CachyOS: the launcher, the server browser, joining a public server and hosting a lobby. Steam Deck should work the same way but is untested. If you load a
custom map and then join a server on another map, the screen can stay black
([#31](https://github.com/Dingo-Shenanigans/ReSkate/issues/31)): load the server's map first.

### macOS (NotProton / CrossOver)

Steam for Mac with a Wine-based compatibility tool works much the same way; see
[macOS](https://docs.reskate.dev/macos) in the docs for its launch option.

### Multiplayer map downloads

Missing multiplayer custom maps can be d