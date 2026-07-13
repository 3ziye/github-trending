<div align="center">

# CS2FOW

### Server-side anti-wallhack for Counter-Strike 2 community servers

[![Version](https://img.shields.io/github/v/release/karola3vax/CS2FOW?style=for-the-badge&label=version)](https://github.com/karola3vax/CS2FOW/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/karola3vax/CS2FOW/total?style=for-the-badge&label=downloads)](https://github.com/karola3vax/CS2FOW/releases)
[![Issues](https://img.shields.io/github/issues/karola3vax/CS2FOW?style=for-the-badge&label=issues)](https://github.com/karola3vax/CS2FOW/issues)
[![License](https://img.shields.io/github/license/karola3vax/CS2FOW?style=for-the-badge&label=license)](LICENSE)

![CS2FOW demonstration](docs/CS2FOW.gif)

</div>

CS2FOW is a server-side anti-wallhack plugin for Counter-Strike 2 community servers. It withholds a living enemy's visual entities when solid map walls fully block that enemy from a living opponent.

## FAQ

### What is CS2FOW?

CS2FOW is a server-side anti-wallhack plugin for Counter-Strike 2 community servers. When solid map walls completely hide a living enemy, it can stop sending that enemy's visual entities to one opposing player.

It is not a screen filter and does not run on the player's computer.

### Does it work in Premier or Valve matchmaking?

No. It requires a community or dedicated server running Metamod:Source. Valve would need to add a similar system for official matchmaking.

### Do players install anything or risk a VAC ban?

Players install nothing. CS2FOW runs only on the server and does not modify or inject into the CS2 client.

### Can a cheat bypass it?

A cheat cannot recover an exact live enemy position that the server never sent. It can still use sound, teammate information, last-known positions, common prefire spots, and other game clues. CS2FOW reduces the main wallhack data source; it does not make all cheating impossible.

### What exactly gets hidden?

For a living enemy, CS2FOW treats only the pawn, known carried weapons, wearables, and a currently carried hostage prop as one visual group. Unknown and independent gameplay entities stay visible.

Self, dead players, spectators, and HLTV remain unfiltered. Teammates remain unfiltered by default; an optional setting applies the same visibility gate to living teammates.

### Can players still wallbang a hidden enemy?

Yes. The enemy remains fully present on the server. Movement, hit registration, penetration, damage, and game rules continue normally.

### Does it block radar cheats or sound ESP?

It reduces radar cheats that depend on live enemy entity positions. It does not remove footsteps, gunshots, teammate information, bomb information, or every other clue.

### What about smokes, doors, breakables, and moving props?

Smokes are visibility blockers. CS2FOW copies CS2's live smoke voxel grid and checks wall-clear rays against it, including changing edges, overlap, growth, fade, and grenade-made holes. Doors, breakables, and moving props are not blockers in the current preview because the baked map contains only static geometry.

### How does it avoid enemies appearing too late around corners?

The worker checks body points, bounding-box corners, and the held weapon muzzle. Movement prediction starts gradually above 75 units per second and is fully active at 100. It looks ahead by 75 ms plus 1.5 times the recipient's current round-trip latency, capped at 375 ms and 96 movement units per player. Left/right shoulder origins also grow with recipient RTT from 24 to 128 units by default. A 16 ms hold reduces one-tick corner flicker.

When the worker sees an enemy again, CS2FOW stops removing that enemy from normal snapshots immediately.

### Does it run expensive engine traces every tick?

No. Map collision is baked into a compact BVH8 file. A background worker casts rays against that data, while `CheckTransmit` only reads the finished answer.

### Do custom and Workshop maps work?

Yes, when their physics can be baked. The server can bake a mounted map automatically, and the separate Bake Service can prepare downloadable `.bvh8` and `.json` files from a public Workshop item.

### What happens when a map changes?

CS2FOW compares the current source CRC and size with the stored bake. A mismatched or outdated bake is rejected, the plugin shows players normally, and an automatic rebake can create current data.

### What does “fail open” mean?

If CS2FOW is missing information or is not sure that filtering is safe, it sends players normally instead of hiding them.

## Quickstart

1. Install [Metamod:Source](https://www.sourcemm.net/) on the CS2 server.
2. Download the Windows or Linux `0.2.1-preview` core ZIP from the [CS2FOW releases page](https://github.com/karola3vax/CS2FOW/releases).
3. Extract the ZIP into the server's `game/csgo` folder. Keep the folders inside the ZIP unchanged.
4. Start the server and load a map.
5. Run `cs2fow_status` in the server console.

The first load may say that an automatic bake is