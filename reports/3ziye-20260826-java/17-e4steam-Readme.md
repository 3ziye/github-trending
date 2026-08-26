<div align="center">

<img src="common/src/main/resources/assets/e4steam_minecraft/icon.png" width="180" alt="e4steam logo">

# e4steam

### Play Minecraft with friends through Steam

### Играйте с друзьями в Minecraft через Steam

🇬🇧 **English** · [🇷🇺 **Русский**](#русская-версия)

<a href="https://discord.gg/zFvrHz2ys7" title="Join the K2 Studio Discord"><img src="https://img.shields.io/badge/-%20-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="42" alt="Discord"></a>
<a href="https://t.me/K2Studio_Dev" title="K2 Studio Telegram channel"><img src="https://img.shields.io/badge/-%20-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" height="42" alt="Telegram"></a>
<a href="https://dalink.to/kamilchik1231" title="All project links on DAlink"><img src="docs/assets/dalink.svg" width="42" height="42" alt="DAlink"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/e4steam" title="Download on CurseForge"><img src="https://img.shields.io/badge/-%20-F16436?style=for-the-badge&logo=curseforge&logoColor=white" height="42" alt="CurseForge"></a>
<a href="https://github.com/Kamilhik/e4steam" title="GitHub repository"><img src="https://img.shields.io/badge/-%20-181717?style=for-the-badge&logo=github&logoColor=white" height="42" alt="GitHub"></a>
<a href="https://modrinth.com/project/SqqdJF90" title="View on Modrinth"><img src="https://img.shields.io/badge/-%20-00AF5C?style=for-the-badge&logo=modrinth&logoColor=white" height="42" alt="Modrinth"></a>
<a href="https://youtu.be/KJ1W_eJ2VK4" title="Watch the demonstration"><img src="https://img.shields.io/badge/-%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" height="42" alt="YouTube"></a>

[![Version](https://img.shields.io/github/v/release/Kamilhik/e4steam?display_name=tag&sort=semver&style=flat-square)](https://github.com/Kamilhik/e4steam/releases)
[![Build](https://img.shields.io/github/actions/workflow/status/Kamilhik/e4steam/ci.yml?branch=main&label=build&style=flat-square)](https://github.com/Kamilhik/e4steam/actions/workflows/ci.yml)
[![Addon API](https://img.shields.io/maven-central/v/io.github.kamilhik/e4steam-api?label=Addon%20API&style=flat-square)](https://central.sonatype.com/artifact/io.github.kamilhik/e4steam-api/1.0.0)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat-square)](LICENSE)

**🇷🇺 Русская версия находится ниже — [открыть](#русская-версия)**

</div>

> [!IMPORTANT]
> **e4steam 0.3.0 is the current full release, not an alpha, beta or
> prerelease.** Windows x64 is the primary supported platform. Linux x64,
> macOS and dedicated servers are experimental. e4steam permanently uses the
> shared Steam test App ID 480 (Spacewar), so unrelated App ID 480 traffic is
> possible and is filtered.

> [!NOTE]
> 0.3.0 includes Addon API 1.0, loader-native addon discovery, macOS natives,
> an experimental fail-closed dedicated server and retro release artifacts.
> A Windows x64 NeoForge 1.21.1 dedicated server with one authenticated Steam
> client was manually verified on August 24, 2026. The two-client, macOS and
> remaining cross-platform matrices are not complete, so Linux, macOS and
> dedicated-server support remain experimental.

e4steam opens a Minecraft singleplayer world to Steam friends without port
forwarding or a public IP. Both players need the mod and a signed-in Steam
client. Minecraft TCP traffic and supported voice-chat UDP traffic travel over
Steam P2P or Valve relays.

Offline Minecraft launcher profiles are supported for Steam connections. In
0.3.0, the host derives each Steam guest's stable Minecraft
UUID and safe profile name from the authenticated SteamID rather than trusting
the name supplied by the client. Steam itself must still be running and signed
in on every computer.

## What's new in 0.3.0

The repository now contains a separate loader-independent Java 8 API artifact,
an addon testkit and a neutral compile-checked example. API 1.0 includes scoped
identity, session, dedicated, access, lobby, negotiated network, UDP, UI,
command, config, storage, world-settings, modpack, skin, diagnostics,
localization and logging contracts. Addons are discovered only through the
installed mod loader or Java service metadata; core never scans or downloads
arbitrary JAR files. See the [Addon API guide](docs/ADDON_API.md) and the
[compatibility matrix](COMPATIBILITY.md).

### Addon API for developers

The stable **e4steam Addon API 1.0.0** is published on
[Maven Central](https://central.sonatype.com/artifact/io.github.kamilhik/e4steam-api/1.0.0).
No custom Maven repository is required:

```groovy
dependencies {
    compileOnly("io.github.kamilhik:e4steam-api:1.0.0")
}
```

[Full Addon API documentation](docs/ADDON_API.md)

This API is not a sandbox: an installed addon is ordinary code in the same JVM
and must come from a trusted source. Core does not expose Steam passwords,
auth tickets, invite tokens, GSLT, native handles or raw protocol hooks.
Public Worlds, Modpack Sync, Offline Sk