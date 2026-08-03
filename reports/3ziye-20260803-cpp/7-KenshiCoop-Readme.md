# KenshiCoop

Setup + Demo: [https://www.youtube.com/watch?v=OqwVRRZEYGM](https://www.youtube.com/watch?v=OqwVRRZEYGM)

Experimental **co-op multiplayer for [Kenshi](https://lofigames.com/)**, built as an
[RE_Kenshi](https://github.com/BFrizzleFoShizzle/RE_Kenshi) /
[KenshiLib](https://github.com/BFrizzleFoShizzle/KenshiLib) plugin.

One player hosts their world; a friend connects (LAN, direct UDP, or Steam P2P)
and plays their own squad inside it. The plugin replicates squads, NPCs, combat,
inventory and equipment, direct trades between the players' squads, items
dropped on the ground (both directions), base building and container contents,
money, game speed, and more - and saves are coordinated: any save either player
makes becomes one shared save, streamed to both machines automatically.

> **Status: work in progress.** This is a hobby project under active
> development. Expect rough edges, desyncs, and crashes. Two players is the
> current design target.

## How it works

- `KenshiCoop.dll` is loaded into the game by RE_Kenshi. It hooks the engine via
  KenshiLib and drives all game mutation on the main thread.
- Networking is [ENet](https://github.com/lsalzman/enet) over UDP, with an
  optional Steam P2P tunnel (no port forwarding needed).
- The host is authoritative for the world; each client is authoritative for its
  own squad. See `docs/API_REFERENCE.md` for the full engine-control surface and
  wire protocol.

```
src/plugin/       The KenshiCoop plugin (net, sync/replication, engine facade, scenarios)
src/netproto/     Shared wire-protocol headers (plain C++03, compiled by everything)
src/nettest/      Standalone ENet console app (transport de-risking)
src/netsim/       Protocol simulator
src/prototest/    Wire-protocol unit tests
src/tunneltest/   Steam-tunnel socket-hook tests
scripts/          Build, deploy, session, and automated-test tooling (PowerShell)
docs/             Build guide, engine/API reference, replication pitfalls
third_party/      ENet patches, VC10 compat shim (deps are fetched, not committed)
```

## Try it (play with a friend)

Two players, two machines. You configure the session **inside the game** with
an in-game panel (press **F2**) - you swap Steam IDs by clipboard right in the
panel, so there's no config file to edit and no launcher scripts to run. (A tiny
`coop_config.json` is only needed for LAN / direct-UDP games.)

### Before you start (both players)

1. **Kenshi 1.0.65 (Steam)**, set to windowed mode: launch Kenshi once, then
   Options > Video > un-check **Full Screen**.
2. **[RE_Kenshi 0.3.1+](https://www.nexusmods.com/kenshi/mods/847)** installed
   (free Nexus mod - it loads the co-op plugin into the game).
3. **Steam running and online** on both machines. That's the whole network
   setup: the connection is Steam P2P, so there's no port forwarding, no
   router configuration, and no IP addresses. (A direct-UDP mode is also
   available for LAN / port-forwarded games.)

### 1. Install the mod

Grab `KenshiCoop-kit.zip` from the
[latest release](https://github.com/nhoral/KenshiCoop/releases/latest) and
unzip it anywhere (both players). You do not need to clone this repository -
but if you did, the same kit is in [dist/mod-kit](dist/mod-kit).

The zip contains a single **`KenshiCoop`** folder. Copy that folder into your
Kenshi `mods` directory so you end up with
`<Kenshi>\mods\KenshiCoop\KenshiCoop.dll` (default Steam path:
`C:\Program Files (x86)\Steam\steamapps\common\Kenshi\mods\`). Then launch
Kenshi and enable **KenshiCoop** in the Mods menu.

### 2. Connect in-game (press F2)

The Co-op panel works at the **main menu** (before you load a game) as well as
in-game, so the joining player doesn't need to load anything first.

1. Press **F2** to open the Co-op panel.
2. **Swap Steam IDs.** Each player clicks **"Copy my Steam ID"** and sends it to
   the other (Steam chat, Discord, ...). When you receive your friend's ID, copy
   it, then click **"Paste friend's Steam ID"** - the panel shows the ID it
   captured. This is per-session (nothing is written to disk), so re-paste it if
   you relaunch Kenshi.
3. Leave **Transport** on **STEAM**.
4. **Host:** load the save you want to play, or start a new game - pick
   **Multiplayer (Wanderer x2)** from the start list for a ready-made two-squad
   co-op start (see below). Then set **Role: HOST** and toggle **Connection** to
   **ONLINE**.
5. **Join:** straight from the **main menu** - no save needed - set
   **Role: JOIN** and toggle **Connection** to **ONLINE**. The host streams its
   world to you on connect and you load right into it. (If you already have an
   identical copy of the host's save on disk, it's used as-is instead of
   transferring.)
6. The white status line shows live state (and a banner over your leader shows
   it too, in-game). Toggle **Connection** to **OFFLINE** to leave.

**LAN / direct-UDP (advanced):** skip the Steam ID swap. Open
`<Kenshi>\mods\KenshiCoop\coop_config.json`, set `"transport":