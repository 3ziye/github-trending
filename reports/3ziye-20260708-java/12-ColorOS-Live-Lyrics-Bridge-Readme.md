# ColorOS Live Lyrics Bridge

[![Build Debug APK](https://github.com/Andrea-lyz/ColorOS-Live-Lyrics-Bridge/actions/workflows/build-debug.yml/badge.svg)](https://github.com/Andrea-lyz/ColorOS-Live-Lyrics-Bridge/actions/workflows/build-debug.yml)

Languages: [English](README.md) | [简体中文](README.zh-CN.md)

<p align="center">
  <img src="GIF.gif" alt="ColorOS Live Lyrics Bridge demo" width="360">
</p>

An LSPosed/libxposed API 102 module that bridges timed lyrics from supported Android music players into the ColorOS/OPlus lock-screen lyric pipeline.

The module currently ships DexKit-based compatibility adapters for Salt Player and ConePlayer plus SystemUI renderer hooks. Other players should integrate by publishing the `lyricInfo` contract themselves.

Release assets also include optional LyricProvider APKs for QQ Music, NetEase Cloud Music, Apple Music, Poweramp, Spotify, QiShui Music, and KuGou Music/Concept. They are separate LSPosed modules that forward complete lyric data to ColorOS Live Lyrics Bridge and Lyricon/词幕.

A player-independent transaction layer associates lyric callbacks with media metadata. Events with media IDs, URIs, or complete title/artist hints bind directly; anonymous passive callbacks wait for the next stable metadata observation so preloads and instrumentals cannot shift lyrics across tracks.

## What It Hooks

Player process:

```text
android.media.session.MediaSession#setMetadata(android.media.MediaMetadata)
```

For built-in compatibility adapters, a valid lyric captured for the current track takes priority over a simple player-provided `MediaMetadata["lyricInfo"]` payload. The simple payload remains a fallback until capture succeeds. A player payload containing `rawLyric` or timed translation data is treated as an explicit enhanced integration and is kept. Self-integrating players should publish the same payload themselves.

```json
{
  "songName": "...",
  "artist": "...",
  "songId": "lockscreen-lyrics-...",
  "lyric": "[00:00.00]...",
  "rawLyric": "[00:00.000]word[00:00.120]..."
}
```

SystemUI process:

- Reads `lyricInfo` from OPlus media data.
- Normalizes the official line-level LRC so each timestamp produces one primary OPlus list item, while translations and word timing remain in the complete model.
- Builds a word-level timeline from `rawLyric` when available.
- Merges timed translation lines from the original `lyricInfo` into the word-level model.
- Resolves private OPlus media and lyric targets through DexKit, with legacy class-name fallback.
- Draws inside the official lock-screen lyric `TextView.onDraw(Canvas)` path.
- Maps official items by timestamp, normalized text, and occurrence order so repeated lyrics and pre-roll lines remain stable.
- Uses compact dynamic lyric slots with a `56dp` floor and about `12dp` vertical padding, keeps official `6dp` line spacing, uses a moving two-line window for long main lyrics, and places the active line about `48dp` below the viewport center.
- Recovers lyric rendering after transient visibility changes without changing item geometry during playback.
- Dynamically recognizes player-provided `lyricInfo` without a hard-coded package name.
- Keeps the screen from timing out while the recognized provider's lock-screen lyric UI is actively visible.

## Screen Timeout Keep-Awake

The keep-awake logic runs only in the SystemUI process. It is intentionally tied to the official OPlus lock-screen lyric UI, not to playback alone.

SystemUI hooks used by this feature:

- `android.util.Log.i(String, String)`
- `android.util.Log.println(int, String, String)`
- OPlus Seedling media playback position/state hooks
- Visible official lyric `TextView` tracking
- `ACTION_SCREEN_OFF`, `ACTION_SCREEN_ON`, and `ACTION_USER_PRESENT` broadcasts inside SystemUI

The module watches OPlus `PluginSeedling--Template` logs for supported player packages and checks fields such as:

```text
lyricUiMode=true
lockImmersiveMode: true
containerView.isShown=true
hasLyric=false
```

It holds a 15-second `SCREEN_BRIGHT_WAKE_LOCK` lease only when all of these are true:

- The current package is either a built-in compatibility adapter or the active provider of a valid `lyricInfo` payload.
- OPlus lyric UI mode is active.
- Playback is playing.
- There is lyric evidence from a recently visible official lyric view, with only a short grace window from fresh lyric metadata.
- The screen is interactive and the keyguard is still showing.

While active, the module renews the wake-lock lease and pulses `PowerManager.userActivity(...)` about every 8 seconds so the system treats the lock-screen lyric view as user-visible activity. The wake lock is released on screen off, true keyguard dismissal, playback stop, missing visible lyric evidence, unsupported package, or any condition change. `ACTION_USER_PRESENT` is followed by a short keyguard recheck so face unlock can keep the lock-screen lyric UI awake when the keyguard remains visible.

Self-integrating players are recognized from