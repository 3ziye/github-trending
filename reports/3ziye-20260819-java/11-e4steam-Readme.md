<div align="center">

<img src="common/src/main/resources/assets/e4steam_minecraft/icon.png" width="180" alt="e4steam logo">

# e4steam

### Play Minecraft with friends through Steam

🇬🇧 **English** · 🇷🇺 **Русский**

<a href="https://discord.gg/k2EsPGQfMu" title="Join the Discord server"><img src="https://img.shields.io/badge/-%20-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="42" alt="Discord"></a>
<a href="https://t.me/Kamilchikm" title="Telegram channel"><img src="https://img.shields.io/badge/-%20-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" height="42" alt="Telegram"></a>
<a href="https://dalink.to/kamilchik1231" title="All project links on DAlink"><img src="docs/assets/dalink.svg" width="30" height="30" alt="DAlink"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/e4steam" title="Download on CurseForge"><img src="https://img.shields.io/badge/-%20-F16436?style=for-the-badge&logo=curseforge&logoColor=white" height="42" alt="CurseForge"></a>
<a href="https://github.com/Kamilhik/e4steam" title="GitHub repository"><img src="https://img.shields.io/badge/-%20-181717?style=for-the-badge&logo=github&logoColor=white" height="42" alt="GitHub"></a>
<a href="https://modrinth.com/project/SqqdJF90" title="View on Modrinth"><img src="https://img.shields.io/badge/-%20-00AF5C?style=for-the-badge&logo=modrinth&logoColor=white" height="42" alt="Modrinth"></a>
<a href="https://youtu.be/KJ1W_eJ2VK4" title="Watch the demonstration"><img src="https://img.shields.io/badge/-%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" height="42" alt="YouTube"></a>

[![Version](https://img.shields.io/github/v/release/Kamilhik/e4steam?display_name=tag&sort=semver&style=flat-square)](https://github.com/Kamilhik/e4steam/releases)
[![Build](https://img.shields.io/github/actions/workflow/status/Kamilhik/e4steam/build.yml?branch=main&label=build&style=flat-square)](https://github.com/Kamilhik/e4steam/actions/workflows/build.yml)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat-square)](LICENSE)

**🇷🇺 Русская версия находится ниже — [открыть](#русская-версия)**

</div>

> [!IMPORTANT]
> **e4steam 0.2.4 is the current stable release.** Windows x64 is the primary
> supported platform. Linux x64 is experimental. Dedicated servers and macOS
> are not supported. e4steam permanently uses the shared Steam test App ID 480
> (Spacewar), so unrelated App ID 480 traffic is possible and is filtered.

e4steam opens a Minecraft singleplayer world to Steam friends without port
forwarding or a public IP. Both players need the mod and a signed-in Steam
client. Minecraft TCP traffic and supported voice-chat UDP traffic travel over
Steam P2P or Valve relays.

Offline Minecraft launcher profiles are supported for Steam connections. The
host authenticates each guest through the authorized Steam bridge, while
Minecraft creates the guest profile using its normal offline-mode rules. Steam
itself must still be running and signed in on every computer.

## Which file should I download?

| Minecraft | Loader | File name contains | Extra dependency |
| --- | --- | --- | --- |
| 1.17–1.18.2 | Fabric/Quilt | `fabric-quilt-mc1.17-1.18.2` | Fabric API |
| 1.17.1–1.18.1 | Forge | `forge-mc1.17.1-1.18.1` | None |
| 1.19–1.21.x | Fabric/Quilt | `fabric-quilt-mc1.19-1.21.11` | Fabric API |
| 1.18.2–1.20.2 | Forge | `forge-mc1.18.2-1.20.2` | None |
| 1.20.2–1.21.x | NeoForge | `neoforge-mc1.20.2-26.2` | None |
| 26.1–26.2 | Fabric/Quilt or NeoForge | file containing `mc26.1-26.2` | Fabric API only for Fabric/Quilt |

Each listed JAR already contains both Windows x64 and Linux x64 Steam native
libraries. Download one file for your Minecraft version and loader; there are
no separate Windows and Linux builds.

Declared ranges are broader than the manually tested matrix. Check
[COMPATIBILITY.md](COMPATIBILITY.md); unverified combinations are experimental.

## Installation

1. Install the loader matching your Minecraft version.
2. Download the matching e4steam JAR from [GitHub Releases](https://github.com/Kamilhik/e4steam/releases), [CurseForge](https://www.curseforge.com/minecraft/mc-mods/e4steam), or [Modrinth](https://modrinth.com/mod/e4steam).
3. Put the JAR in the instance's `mods` folder. Fabric and Quilt also require Fabric API.
4. Install the same e4steam release on every player's computer.
5. Start Steam and sign in before launching Minecraft.

## Playing

1. Open a singleplayer world.
2. Select **Open to LAN → Steam friends** or **Invitation only**.
3. Press **Invite friends** and send the invitation in the Steam overlay.
4. Your friend accepts the invite and confirms joining in Minecraft.

Simple Voice Chat is detected automatically. Plasmo Voice is supported when it
shares Minecraft's port. Another UDP mod can use the `voiceChatPort` setting.

## If an invitation does not arrive

- Confirm both players are Steam friends, online, and using the same e4steam release.
- Confirm both use the same Minec