# notPipe
**English** / [русский](README.ru.md) 

A working YouTube client for **Android 1.5+** utilizing [YtAPILegacy](http://yt.modyleprojects.ru), [Invidious](https://invidious.io) and [yt2009](https://github.com/ftde0/yt2009) APIs. Made with ❤ and longevity in mind. Instead of using a single instance, the app uses multiple instances at the same time for reliability.
* **Telegram channel with updates**: [@AppDataApps](https://t.me/AppDataApps)
* **[Retro Android Group](https://t.me/retroandroidgroup)** on Telegram

![notPipe](img/logo.png "Working YouTube for legacy Android devices")

<img src="img/scr1.png" alt="Screenshot" width="200"/> <img src="img/scr2.png" alt="Screenshot" width="200"/> <img src="img/scr3.png" alt="Screenshot" width="200"/> <img src="img/scr4.png" alt="Screenshot" width="200"/> <img src="img/scr5.png" alt="Screenshot" width="200"/> <img src="img/scr6.png" alt="Screenshot" width="200"/>

## 📥 Download
* [GitHub Releases](https://github.com/gohoski/notPipe/releases)
* [OldMarket](http://oldmarket.store/app.php?id=536)
* [Market Reborn](http://market.lyano.ovh/details/?id=io.github.gohoski.notpipe)
* Telegram (link at the top of the README)

## Features
> [!NOTE]  
> Due to various limitations, the app does not connect to YouTube directly. Instead it connects to various instances of YtAPILegacy, Invidious and yt2009. See ["Why and how"](#why-and-how) for more information.
* Trending, search
* Videos, related videos, comments
* Video playback
* Video conversion for devices that do not support H.264
* Automatic updates of the list of instances from a URL
### TODO
* Landscape, tablet layout (it works on tablets but doesn't look usable)
* Channels
* Playlists
* Authorization via YtAPILegacy

## Solving issues on Android ≤2.3
*(videos lag or do not play at all)*

If videos do not play, first try typical diagnostics:
1. **Switch an instance.** Click the "Playback via … >" button. Some instances might be temporarily unavailable.
2. Make sure your **network is stable.** notPipe may not work properly on a slow Internet connection.

If this does not help, then your device does not support the H.264 codec. Its support depends heavily on the device. There are two ways to solve this problem in notPipe:
1. **Use [MX Player](https://archive.org/details/mx-player-1.7.39)** (Android 2.1+) and switch to the **external player** in settings. However, on unpowerful devices, it's likely that the player will lag on most videos. You can only try.
2. **Enable conversion** in settings. This converts the video to the MPEG-4 Visual codec server-side while using the system player. Requires an SD card. This will unfortunately make a delay when playing a video, but it should last no more than 3–5 minutes.

## Why and how
Existing methods for watching YouTube on legacy Android suffer from two fatal flaws—poor usability and an inability to survive YouTube’s current anti-bot measures. Current workarounds generally have the following issues:
* **Single point of failure.** Current *(and previous)* ways of watching YouTube rely on a single specific API instance. The moment an instance gets a noticeable amount of traffic, YouTube automatically bans its IP address. A single instance may also be heavily overloaded, rendering it unusable.
* **Poor usability.** Web wrappers like S60Tube lack a native feel and require constantly switching between a browser and a video player. yt2009 patched APKs require tedious, per-instance patching—furthermore, they often suffer from heavy server-side video transcoding overhead, crippling in endless buffering. The old mobile YouTube design also isn't always practical. Everything feels clunky.

This project was built from the ground up to solve these exact issues. Instead of relying on a single point of failure, this client **utilizes multiple APIs and instances** simultaneously, randomly selecting a new instance for each activity. This decentralized approach provides critical advantages:
1. **Ban evasion.** Requests are distributed across a big enough pool of servers. Because no single server generates massive traffic, the chances of YouTube triggering an IP ban are drastically reduced.
2. **Performance.** Server bandwidth is load-balanced naturally, preventing the crippling slowdowns seen in single-instance patched APKs.
3. **It just works.** You get a native Android interface without needing to patch your own APKs or configure private servers.
4. **No single point of failure.** Because this is exactly how previous YouTube clients died, everything is decentralized and open for anyone to contribute.
5. **Automatic updates of the instances.** The list of the instances is automatically updated and by default loads from http://144.31.189.129/notPipe.json, requiring as less actions from the user as possible.

## Reporting bugs
**Report bugs in the [Issues](https://github.com/gohoski/numAi/issues) tab!** Don't forget to specify which version of Android you encountered the bug on.

## Build
The pr