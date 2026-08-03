<div align="center">

<img src="docs/cs2ac-logo.png" width="760" alt="CS2AC">

### Open-source server-side anti-cheat for Counter-Strike 2.

[![Modules](https://img.shields.io/badge/modules-18-6f42c1?style=for-the-badge)](#detection-modules)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-5c7cfa?style=for-the-badge)](#quickstart)
[![License](https://img.shields.io/badge/license-AGPL--3.0-2ea44f?style=for-the-badge)](LICENSE)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy_Me_a_Coffee-Support_Development-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=000000)](https://buymeacoffee.com/karola3vax)

**A good Counter-Strike match should be decided by the players, not by who brought the better cheat.**

CS2AC watches the aim, shots, movement, button presses, and game settings that players send to the server. When it finds enough strong evidence, it reports the player and can ask the server to punish them.

[Watch it work](#showcase) · [Install](#quickstart) · [Read the detection modules](#detection-modules) · [Pair it with CS2FOW](#cs2ac-and-cs2fow)

</div>

## Showcase

<table>
<tr>
<td width="50%" align="center">
<img src="docs/showcase/aimbot.gif" width="100%" alt="CS2AC detecting a blatant snap-hit aimbot">
<br><strong>AIMBOT</strong><br>
<sub>A damaging shot follows a blatant snap onto the target.</sub>
</td>
<td width="50%" align="center">
<img src="docs/showcase/aimlock.gif" width="100%" alt="CS2AC detecting inhumanly precise target tracking">
<br><strong>AIMLOCK</strong><br>
<sub>The aim follows a moving enemy with machine-like precision.</sub>
</td>
</tr>
<tr>
<td width="50%" align="center">
<img src="docs/showcase/antiaim.gif" width="100%" alt="CS2AC detecting impossible anti-aim angles">
<br><strong>ANTIAIM</strong><br>
<sub>The view produces impossible angles, spin, jitter, or attack-return patterns.</sub>
</td>
<td width="50%" align="center">
<img src="docs/showcase/bhop.gif" width="100%" alt="CS2AC detecting automated bunny hopping">
<br><strong>BHOP</strong><br>
<sub>Landings and jump inputs repeat with automated timing.</sub>
</td>
</tr>
<tr>
<td width="50%" align="center">
<img src="docs/showcase/irregular-behavior.gif" width="100%" alt="CS2AC detecting repeated irregular airborne and no-scope results">
<br><strong>IRREGULAR BEHAVIOR</strong><br>
<sub>Rage-level airborne and no-scope results keep adding up.</sub>
</td>
<td width="50%" align="center">
<img src="docs/showcase/silentaim.gif" width="100%" alt="CS2AC detecting a firing angle that disagrees with visible aim">
<br><strong>SILENTAIM</strong><br>
<sub>The damaging firing angle does not follow the visible aim path.</sub>
</td>
</tr>
</table>

### CS2AC and CS2FOW

<div align="center">

<a href="https://github.com/karola3vax/CS2FOW">
<img src="docs/showcase/cs2fow-wallhack.gif" width="100%" alt="CS2FOW operating across Dust II long sightlines">
</a>

**CS2AC catches cheating behavior. CS2FOW stops hidden enemy positions from reaching the wallhack.**

<sub>They solve different problems, run entirely on the server, and can protect the same CS2 community server together.</sub>

</div>

## Quickstart

You need a Windows x64 or Linux x64 CS2 dedicated server running [Metamod:Source](https://www.sourcemm.net/) 2.x.

1. Open this repository's **Releases** tab and choose the matching Windows or Linux package.
2. Extract it into the CS2 server root without rearranging anything. The package begins with the `game` folder.
3. Edit `game/csgo/cfg/cs2ac.cfg`.
4. Start the server.
5. Run `meta list`, then `cs2ac_status`.

That is it. Players install nothing.

The default punishment commands are made for [CS2-SimpleAdmin](https://github.com/daffyyyy/CS2-SimpleAdmin). If your server uses another admin plugin, replace the two commands in `cs2ac.cfg` with commands that plugin understands.

CS2AC checks for stable updates after startup and every six hours. A verified update is prepared in the background and installed on the next full server restart. Set `cs2ac_auto_update 0` in `cs2ac.cfg` and run `cs2ac_reload` to disable future automatic checks and downloads. An update already prepared before this was disabled may still install on the next restart. Existing settings are copied into the new configuration layout, and the previous configuration and plugin binary are kept as backups.

## Detection output

When a detector finds enough evidence, CS2AC can report the result wherever the server owner needs it:

1. Announce it in public chat.
2. Hold a center-screen alert for five seconds.
3. Write the detector evidence to the server console.
4. Submit the configured ban or kick command to the server.
5. Send a detailed Discord webhook report.

Chat and center-screen announcements can be turned on or off separately. CS2AC sends the chosen ban or kick command to the server. The installed admin plugin must understand and run that command.

```text
[CS2AC] detected AIMBOT on Player and punished.
```

<div align="center">

<img sr