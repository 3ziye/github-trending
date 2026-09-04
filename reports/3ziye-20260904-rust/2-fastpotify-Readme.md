# Fastpotify

**Spotify, native and fast.** Fastpotify is a Spotify client written in
Rust with [egui](https://github.com/emilk/egui). It plays music through
[librespot](https://github.com/librespot-org/librespot). It typically uses
100–250 MB of RAM, while Spotify's desktop app often uses 600 MB to over 1 GB.
It runs on Linux, macOS, and Windows, starts in well under a second, and has no
browser engine.

**Playback needs Spotify Premium.** Free accounts can browse and search, but
cannot play music through Fastpotify on this computer or another device.

![Fastpotify Home with the playlist library, recommendations, queue, and player visible](docs/screenshot.png)

See [fastpotify.rocks](https://fastpotify.rocks/) for installation, setup,
everyday use, and connection details.

## What it does

- **Plays music on this computer.** Fastpotify appears as a Spotify Connect
  device. Select it from your phone or play music in the app. Playback is
  gapless and supports up to 320 kbps, with
  optional volume normalisation and an on-disk audio cache.
- **Controls other devices.** Move playback to a speaker, a phone, or
  another computer from the device picker, and keep controlling it: play,
  pause, skip, seek, shuffle, repeat, volume.
- **Finds speakers on your network.** Fastpotify finds librespot, spotifyd,
  and supported hardware receivers over mDNS. Once connected, they appear as
  Spotify Connect devices.
- **Library.** Browse playlists, Liked Songs, saved albums, followed artists,
  podcasts, and saved episodes. Filter, pin, and reorder sidebar items.
- **Search** across songs, artists, albums, playlists, podcasts, and episodes,
  with a top result and per-type views.
- **Home** with Made for you, Recently played, your top artists and songs, and
  recommendations.
- **Artist pages** with popular songs, a filterable discography, and related
  artists. **Album**, **playlist**, and **podcast** pages support playback
  from any row.
- **Edit your playlists.** Create, rename, describe, reorder, and delete them.
  Add songs from a row menu, or drag a row or the currently playing song to a
  playlist in the sidebar. A playlist a friend shared with you takes songs too,
  as Spotify's own apps allow.
- **Opens Spotify links.** Fastpotify registers for `spotify:` links, so a
  song, album, artist, playlist, or podcast shared from another app opens
  in it, whether it is running or not. `open.spotify.com` addresses go
  through the browser, which hands them to the same handler.
- **Queue** as a side panel or a page; add anything to it from a row menu.
- **Resumes the last session.** On startup, the last song is paused where it
  stopped. Play resumes it, and the other playback controls work before it
  starts.
- **Album-art colour.** Pages and the player bar take a tint from the cover
  of what you are looking at or listening to. Turn it off in Settings.
- **Light and dark**, or follow the system.
- **Winamp mini player.** `Ctrl+M` opens a small player for classic `.wsz`
  skins, drawn at 1x to 4x scale. It includes a spectrum analyser, playlist,
  and equalizer. Drop a skin from the
  [Winamp Skin Museum](https://skins.webamp.org) on either window to add it.

  ![The mini player wearing the built-in skin](docs/assets/images/winamp.png)
- **Equalizer.** Winamp's ten bands and presets over the music played on
  this computer, in Settings and in the skin.
- **MilkDrop.** The visualiser, powered by
  [projectM](https://github.com/projectM-visualizer/projectm), runs in its own
  window and process. It supports fullscreen and automatically downloads more
  than 10,000 `.milk` presets on first use (about 26 MB).

  https://github.com/user-attachments/assets/12b31312-0e0c-4b34-9383-e8c66aabc58d
- **Keyboard-first.** Every common action has a shortcut (`Ctrl+/` or `?` lists
  them).
- **Keeps playing when you close the window.** Fastpotify stays in the system
  tray. Use the tray icon or media controls to reopen it, and quit from the
  tray menu or with `Ctrl+Q`. You can make the close button quit in Settings.
  On macOS, the Dock icon also reopens the window.
- **Visible network activity.** Pages show a spinner while loading. The top
  bar also shows slow or rate-limited Spotify requests.
- **One instance.** Launching it again brings the existing window forward
  instead of starting a second copy, on every platform.
- **Desktop integration.** MPRIS on Linux, so media keys, the shell, and
  `playerctl` see Fastpotify like any other player. On macOS and Windows,
  `fastpotify next` and its siblings drive the running app from a terminal,
  a launcher, or a hotkey.

## Install

On Arch Linux, Fastpotify is in the AUR:

```bash
yay -S fastpotify-bin      # the released build, ready made
yay -S fastpotify          # the release, built from source
yay -S fastpotify-git      # built from the latest commit
```

On macOS, with [Homebrew](https://brew.sh):

```sh
brew install --cask crmne/tap/fastpotify
```

Everywhere else, build the si