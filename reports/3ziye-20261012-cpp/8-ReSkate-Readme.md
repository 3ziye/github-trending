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
  - **Hall of Meat** (off by default): bail and see the bones you hurt, with a skate. 3 style Meat card.
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

### Linux (Proton)

1. Install skate. with Steam and put `ReSkateLauncher.exe` and `ReSkate.dll` beside `Skate.exe`
   (step 2 above, first option).
2. In Steam → skate. → Properties → Launch Options, enter:

   ```
   bash -c 'exec "${@/EAAntiCheat.GameServiceLauncher.exe/ReSkateLauncher.exe}"' -- %command%
   ```

3. Press **Play** on skate. in your Steam library.

Steam starts EA's anti-cheat launcher (`EAAntiCheat.GameServiceLauncher.exe`), not `Skate.exe`, and the
anti-cheat refuses to run under Proton (*E111000B … Wine, Proton, and Steam Deck are not supported*).
The launch option swaps it for ReSkate's launcher, which starts the game itself. Launching from the game's
own Steam entry, rather than adding the launcher as a non-Steam game, keeps skate.'s app ID and its
Proton prefix.

Tested with ReSkate 1.1.3 and Proton Experimental on CachyOS: the launcher, the server browser, joining
a public server and hosting a lobby. Steam Deck should work the same way but is untested. If you load a
custom map and then join a server on another map, the screen can stay black
([#31](https://github.com/Dingo-Shenanigans/ReSkate/issues/31)): load the server's map first.

### Controls

| Key | Opens |
|---|---|
| **Insert** | the ReSkate menu |
| **~** (grave/tilde) | the command console (`help` lists the commands) |
| **T** | chat, in multiplayer |

The menu and console keys can be changed in the launcher's Settings.

In **MAP → ROTATING PARKS** and the controller-friendly **MOD OPTIONS → PARKS** screen,
**Load Random Parks** chooses and loads one random layout for each of
San Vansterdam's three slots. Each supported layout has an equal chance; empty lots are excluded and
a roll can pick a layout already loaded. Choices save with your profile and are shared when you host.
**Randomize on Launch** is off by default. Turn it on to pick fresh layouts once on each subsequent
game launch, when the park controller is ready. Changing maps does not roll again. Guests follow the
host's layouts; a dedicated server admin can use the button to randomize the server's parks for everyone.
Both menus share the same launch preference. It only affects your own parks, including when you host
a lobby. Joining a host cancels any pending startup roll, so leaving the lobby restores your saved
l