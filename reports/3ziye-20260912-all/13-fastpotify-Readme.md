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
  Stalled Spotify connections time out after five seconds per attempt so
  playback can try another endpoint.
- **Controls other devices.** Move playback to a speaker, a phone, or
  another computer from the device picker, and keep controlling it: play,
  pause, skip, seek, shuffle, repeat, volume. Long device lists scroll.
- **Finds speakers on your network.** Fastpotify finds librespot, spotifyd,
  and supported hardware receivers over mDNS. Once connected, they appear as
  Spotify Connect devices. The picker uses responding receivers' names and
  combines entries with the same device ID.
- **Library.** Browse playlists, Liked Songs, saved albums, followed artists,
  podcasts, and saved episodes. Filter, pin, and reorder sidebar items.
  On `main`, after 0.7.1, choose name, recent plays, or saved-date order where
  available. Follow Spotify’s playlist order or keep a separate local arrangement.
  Move Liked Songs among your pins or unpin it and choose its local position;
  the placement survives restarts.
  Liked Songs reopens from an account-specific metadata cache. Older rows
  refresh in the background while Like and Unlike take effect immediately.
  Right-click album, artist, and podcast cards for their actions (on `main`,
  after 0.7.1).
- **Search** across songs, artists, albums, playlists, podcasts, and episodes,
  with a top result and per-type views. Right-click results and cards for their actions.
- **Home** with Made for you, Recently played, your top artists and songs, and
  recommendations. Right-click playlist shortcuts and shelf cards for their actions.
- **Artist pages** with popular songs, a filterable discography, and related
  artists. **Album**, **playlist**, and **podcast** pages support playback
  from any row.
  Discography and related-artist cards also have right-click menus (on `main`,
  after 0.7.1).
  Artist names in the player bar open their pages, including during local
  playback before Web API metadata arrives (on `main`, after 0.7.1).
- **Edit your playlists.** Create, rename, describe, reorder, and delete them.
  On `main`, after 0.7.1, hold a dragged song near the playlist's top or bottom
  edge to scroll to rows beyond the screen. The Library sidebar scrolls while
  dragging toward offscreen playlists too.
  Add songs from a row menu, or drag a row or the currently playing song to a
  playlist in the sidebar. On `main`, after 0.7.1, drop a song from the player
  bar, queue, or another list between rows of an open editable playlist to
  insert it there. This adds a copy and leaves playback and the queue unchanged.
  Clear the playlist’s filter and sort to choose an insertion position.
  Drop it on an empty playlist to add its first song.
  A playlist a friend shared with you takes songs too,
  as Spotify's own apps allow. Filter the **Add to playlist** menu by name to
  find the destination quickly.
- **Opens Spotify links.** Fastpotify registers for `spotify:` links, so a
  song, album, artist, playlist, or podcast shared from another app opens
  in it, whether it is running or not. `open.spotify.com` addresses go
  through the browser, which hands them to the same handler.
- **Queue** as a side panel or a page; it names what is playing from, and
  anything can be added to it from a row menu. **Add to queue** places songs
  after those already queued and before the context continues.
- **Resumes the last session.** On startup, the last song is paused where it
  stopped. Play resumes it, and the other playback controls work before it
  starts.
- **Album-art colour.** Pages and the player bar take a tint from the cover
  of what you are looking at or listening to. Turn it off in Settings.
- **Light and dark**, or follow the system.
- **Winamp mini player.** `Ctrl+M` opens a small player for classic `.wsz`
  skins, drawn at 1x to 4x scale. It includes a spectrum analyser, playlist,
  and equalizer. It keeps its shade mode and, where the d