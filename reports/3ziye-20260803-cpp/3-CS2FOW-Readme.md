<div align="center">

<img src="docs/cs2fow-logo.png" width="760" alt="CS2FOW">

### Server-side anti-wallhack for Counter-Strike 2 community servers

[![Protection](https://img.shields.io/badge/protection-Walls%20%7C%20Smoke-6f42c1?style=for-the-badge)](#the-protection-boundary)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-5c7cfa?style=for-the-badge)](#quickstart)
[![License](https://img.shields.io/badge/license-MIT-2ea44f?style=for-the-badge)](LICENSE)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy_Me_a_Coffee-Support_Development-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=000000)](https://buymeacoffee.com/karola3vax)

**A wallhack cannot draw a player your server never sent.**

CS2FOW stops your server from sending an enemy's live position when walls or smoke completely hide them. It runs entirely on the server, players install nothing, and uncertain visibility stays visible.

[Watch it work](#showcase) · [Install](#quickstart) · [Learn how it works](#how-it-works) · [Pair it with CS2AC](#cs2fow-and-cs2ac)

</div>

## Showcase

Every map gets a lightweight 3D copy of its solid walls. CS2FOW uses that copy to check who can actually see whom.

<table>
<tr>
<td width="50%" align="center">
<img src="docs/ancient.gif" width="100%" alt="CS2FOW hiding players behind solid map geometry on Ancient"><br>
<strong>Ancient &mdash; A site</strong>
</td>
<td width="50%" align="center">
<img src="docs/smokeandhegrenade.gif" width="100%" alt="CS2FOW hiding players behind smoke and revealing them through an HE-cleared opening"><br>
<strong>Smoke &mdash; HE-cleared opening</strong>
</td>
</tr>
<tr>
<td width="50%" align="center">
<img src="docs/cache.gif" width="100%" alt="CS2FOW operating around the Cache A site"><br>
<strong>Cache &mdash; A site</strong>
</td>
<td width="50%" align="center">
<img src="docs/dust2b.gif" width="100%" alt="CS2FOW operating around the Dust II B site"><br>
<strong>Dust II — B site</strong>
</td>
</tr>
<tr>
<td width="50%" align="center">
<img src="docs/dust2long.gif" width="100%" alt="CS2FOW operating across Dust II long sightlines"><br>
<strong>Dust II — Long</strong>
</td>
<td width="50%" align="center">
<img src="docs/mirageaside.gif" width="100%" alt="CS2FOW operating around the Mirage A site"><br>
<strong>Mirage &mdash; A site</strong>
</td>
</tr>
</table>

### CS2FOW and CS2AC

<div align="center">

<a href="https://github.com/karola3vax/CS2AC">
<img src="docs/cs2ac-logo.png" width="760" alt="CS2AC">
</a>

**CS2FOW hides unseen positions. CS2AC detects cheating behavior.**

<sub>They solve different problems, run entirely on the server, and can protect the same CS2 community server together.</sub>

</div>

## Quickstart

You need a Windows x64 or Linux x64 CS2 dedicated server running [Metamod:Source](https://www.sourcemm.net/) 2.x, the plugin loader that lets CS2 load server extensions. Your CPU must support AVX, a common instruction set CS2FOW uses for fast geometry calculations.

1. Open this repository's **Releases** tab and choose the matching Windows or Linux package.
2. Extract it into the server root, the top-level CS2 server folder, without rearranging anything. The package begins with the `game` folder.
3. Start the server and load a map.
4. Run `meta list`, then `cs2fow_status`.

That is it. Players install nothing.

The first time you load a map, `cs2fow_status` may say that an automatic bake is running. A bake is the one-time step that turns the map's solid walls into fast visibility data. Everyone stays visible until it finishes and passes its checks. The optional official-maps ZIP includes ready-made data, so those maps skip this first wait.

CS2FOW uses a compatibility file called gamedata to locate the exact parts of the CS2 server program it needs. Before using it, the plugin confirms the program by file size and CRC32, a checksum that acts like a digital fingerprint. If Valve ships an unknown update, CS2FOW stays off until matching gamedata is installed rather than guessing inside server memory.

## The protection boundary

CS2FOW keeps its hands off as much of the game as possible. It hides only this small visual group:

- the player pawn, which is the in-game entity representing a living player;
- active, last, and carried weapons, including the carried C4 bomb;
- wearable items, such as gloves and equipment attached to the model;
- the visible hostage model currently carried by the player.

Everything that matters on its own stays on its own. A planted C4 bomb, dropped objective, dropped weapon, flying grenade, burning Molotov fire, sound, or unknown game object does not disappear just because the player who once owned it is hidden. Your server still controls movement, collisions, whether bullets hit, damage through walls, and game rules exactly as before.

CS2FOW does not filter HLTV, Valve's built-in match broadcast system, or spectators, dead players, and your own player. Teammates stay visible by default. Free-for-