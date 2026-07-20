<div align="center">

# CS2FOW

### Server-side anti-wallhack for Counter-Strike 2 community servers

[![Version](https://img.shields.io/github/v/release/karola3vax/CS2FOW?style=for-the-badge&label=version)](https://github.com/karola3vax/CS2FOW/releases/latest) [![Downloads](https://img.shields.io/github/downloads/karola3vax/CS2FOW/total?style=for-the-badge&label=downloads)](https://github.com/karola3vax/CS2FOW/releases) [![Issues](https://img.shields.io/github/issues/karola3vax/CS2FOW?style=for-the-badge&label=issues)](https://github.com/karola3vax/CS2FOW/issues) [![License](https://img.shields.io/github/license/karola3vax/CS2FOW?style=for-the-badge&label=license)](LICENSE)

<img src="docs/ancient.gif" width="800" alt="CS2FOW hiding players behind solid map geometry on Ancient">

<img src="docs/smokeandhegrenade.gif" width="800" alt="CS2FOW hiding players behind smoke and revealing them through an HE-cleared opening">

</div>

CS2FOW stops your server from sending an enemy's live position when walls or smoke completely hide them. A wallhack cannot draw a player your server never sent.

- **It stays on your server:** CS2FOW never runs on your players' computers.
- **Players install nothing:** they join and play normally. There is no client injection or extra download.
- **When in doubt, show the player:** if data is missing, too old, or unsafe, CS2FOW steps aside instead of hiding someone by mistake. This is called failing open.

## Across different maps

Every map gets a lightweight 3D copy of its solid walls. CS2FOW uses that copy to check who can actually see whom.

<table>
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

## FAQ

<details>
<summary><strong>What is CS2FOW?</strong></summary>

CS2FOW is an anti-wallhack plugin for Counter-Strike 2 community servers. If walls or live smoke completely hide a living player, your server can stop sending that player's live visuals to the opponent who cannot see them.

It is not a filter drawn over the screen. Everything happens on your server.

</details>

<details>
<summary><strong>Does it work in Premier or Valve matchmaking?</strong></summary>

No. You need a community or dedicated server running Metamod:Source. Only Valve could add something similar to official matchmaking.

</details>

<details>
<summary><strong>Do players install anything or risk a VAC ban?</strong></summary>

Nothing. Players join your server like normal. CS2FOW does not modify, inject into, or even run inside their CS2 client.

</details>

<details>
<summary><strong>Can a cheat bypass it?</strong></summary>

A cheat cannot unpack an exact live enemy position if your server never put it in the package. It can still listen for sounds, use teammate information, remember the last known position, or guess a common prefire spot. CS2FOW cuts off the main source used by wallhacks; it does not make every kind of cheating impossible.

</details>

<details>
<summary><strong>What exactly gets hidden?</strong></summary>

CS2FOW hides only the known visuals that travel with a living player: the player model, carried weapons, wearables, and a hostage they are currently carrying. Anything unknown or independent stays visible.

You always receive yourself, dead players, spectators, and HLTV. Teammates also stay visible by default, but you can choose to apply the same visibility check to living teammates.

</details>

<details>
<summary><strong>Can players still wallbang a hidden enemy?</strong></summary>

Yes. Hidden does not mean deleted. The player is still fully present on your server, so movement, hit registration, bullet penetration, damage, and game rules keep working normally.

</details>

<details>
<summary><strong>Does it block radar cheats or sound ESP?</strong></summary>

It helps against radar cheats that need live enemy positions. It does not silence footsteps or gunshots, hide bomb information, remove teammate knowledge, or erase every other clue the game provides.

</details>

<details>
<summary><strong>What about smokes, doors, breakables, and moving props?</strong></summary>

Smoke blocks sight too. CS2FOW copies the game's live smoke shape, which is stored as a 3D grid of tiny boxes called voxels. That lets it follow changing edges, overlapping smokes, growth, fading, and holes opened by grenades.

Doors, breakable objects, and moving 