<h1 align="center" id="title">📻 FH6 Universal Radio</h1>

<p align="center">
  <a href="https://discord.gg/NyZUcATqWZ"><img src="https://img.shields.io/badge/Discord-Join%20Us-5865F2?style=flat-square&logo=discord&logoColor=white" /></a>
</p>

<p align="center"><img src="assets/banner.png" alt="FH6 Universal Radio" /></p>

An open-source radio mod for **Forza Horizon 6**. Adds a new in-game radio station fed from your **local music**, **online radio** stations, **Spotify**, **YouTube Music**, **Jellyfin** server, or **any Windows app** (Deezer, a browser tab...), controlled from a browser dashboard.

<p align="center">
  <img src="assets/ingame.png" alt="In-game radio station" width="49%" />
  <img src="assets/webui.png" alt="Web dashboard" width="49%" />
</p>

## Features

- **Local files**: build named **stations** from one or more folders, exclude subfolders you don't want, and pick a play order (shuffle / albums / name / folder) with repeat modes and a searchable queue. MP3 / FLAC / WAV / OGG / M4A / AAC / OPUS / WMA / M3U / M3U8 etc.
- **Online radio**: search a directory of thousands of internet stations by name, genre, or country (via [radio-browser.info](https://www.radio-browser.info)) or paste any stream URL; save favourites with logos and genre/bitrate badges, with live track info.
- **YouTube Music**: paste any video, playlist, or YT Music URL from the dashboard. Tracks are added to a searchable queue, with support for saving playlists as reusable stations.
- **Spotify Connect**: cast from the Spotify app to an "FH6 Universal Radio" device (requires Spotify Premium).
- **Jellyfin**: stream playlists from your own Jellyfin server, view queued tracks, and save playlists as stations for quick access later.
- **External audio**: capture any Windows app (Deezer, a browser tab...) and pipe it into the radio through a virtual audio cable.
- **In-game radio integration**: audio is routed through FH6's radio bus, fades with menus and reacts to in-game volume like every other station.
- **Live dashboard** at `http://localhost:8420`: switch source, transport controls, volume, settings.
- **Race start action**: on race begin, advance to next track, restart the current one, turn radio off on race begin, or leave it alone.
- **Quick station skip**: tune the radio knob away and back within 1s to skip the current track.
- **Loudness normalization**: For consistent volume across tracks.
- **5-band equalizer**: 60 Hz / 250 Hz / 1 kHz / 4 kHz / 12 kHz peaking biquads, ±6 dB per band, applied producer-side at 48 kHz before audio hits the game.
- **Vanilla radio passthrough**: broadcast FH6's built-in radio stations through the mod. Requires **Streamer Mode = Off** while in use.
- **Media hotkeys**: Play/Pause and Next Track/Source media keys continue to work while FH6 is focused.

## Install

> 📺 Prefer a video? Watch the [installation guide on YouTube](https://www.youtube.com/watch?v=9Uwy3pDf4SQ).

1. Download the latest `fh6-universal-radio.zip` from [Nexus Mods](https://www.nexusmods.com/forzahorizon6/mods/215).
2. Close FH6.
3. Extract the ZIP into your Forza Horizon 6 install folder (next to `forzahorizon6.exe`). Overwrite when prompted.
4. Launch the game. In **Audio settings**, set **Radio DJ = Off**.
   - For custom stations (local files, Spotify, YouTube Music, Jellyfin, etc.), enable **Streamer Mode**.
   - For **Vanilla Radio passthrough**, disable **Streamer Mode**.
5. Cycle through radio stations until you land on the new one.
6. Open <http://localhost:8420> in any browser on the same machine. From another device on the same network, use your PC's local IP (e.g. `http://192.168.1.42:8420`), run `ipconfig` in a Command Prompt to find it.

### Dependencies

Online radio, YouTube Music, Spotify, Jellyfin, and non-native local formats rely on external binaries: `yt-dlp`, `ffmpeg`, and `librespot`. The mod **downloads them automatically** on first launch into `fh6-radio\bin`, so there's nothing to install by hand.

To manage them yourself instead, set the paths in the dashboard (**Settings > YouTube Music** for yt-dlp, **Settings > General > ffmpeg path**, **Settings > Spotify Connect** for librespot).

### YouTube Music

Private/age-restricted content needs a Netscape `cookies.txt` exported from your browser. Use an extension like **Get cookies.txt LOCALLY** to export it.

### Spotify Connect

Enable Spotify under **Settings**, then open the Spotify app on a device on the same Wi-Fi network, tap the **Devices** icon, and pick **FH6 Universal Radio**. Requires an old Spotify Premium account (a Spotify Connect limitation).

### External audio

External Audio is a loopback capture of a Windows playback device, so the app has to play onto a device you don't otherwise hear, or it reaches your speakers directly instead of through the radio. Route it through a virtual audio cable:

1. Install a virtual audio cable, e.g. [VB-Audio Virtual Cable](https://vb-audio.com/Cable/).
2. Send the app's audio to the cable. A