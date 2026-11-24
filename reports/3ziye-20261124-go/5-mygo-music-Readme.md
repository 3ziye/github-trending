# MyGo Music

A native desktop music player written in Go with [MyGo](https://github.com/egoist/mygo), no WebView. It plays your local files out of the box, and everything else comes from plugins.

## Features

- Local files (MP3, FLAC, Ogg Vorbis, WAV, and ALAC, FLAC or AAC in .m4a and .aac) with tags, covers and `.lrc` lyrics
- Playlists, liked songs, search, albums and artists
- Now Playing with lyric stage styles, cover wall, queue, shuffle and repeat
- Notch player on macOS, tray, media keys
- Audio cache, fades on pause and seek, loudness normalization
- Session restore
- Podcast captions, written down on the device as episodes play
- English and Simplified Chinese
- Plugins can add accounts, catalogs, podcasts, stations, comments and pages of their own

## Build

```bash
go tool mygo dev     # run in development
go tool mygo build   # package into build/
go test ./internal/...
```

## Podcast captions

Episodes are written down on the device as they play, with [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) and Qwen3-ASR, which the app downloads when the listener asks for them. The libraries come from this repository's `sherpa-onnx-<version>` prerelease, which only changes with that version:

```bash
go run ./scripts/sherpa -sign "Developer ID Application: …"
gh release create sherpa-onnx-2.0.1 --prerelease --latest=false build/sherpa/*
```

## Plugins

A plugin is a folder in the app's `plugins` directory (Settings > Plugins > + > Show Plugins Folder) with a `plugin.json` and one JavaScript or TypeScript file. Install one with the + in Settings > Plugins from GitHub, by its repository or its address, or from its folder or a zip of it on this computer, or drop the folder in by hand. Remove one from its ⋯ menu there. There's nothing to build, and the same plugin runs on every platform. [`examples/demo-plugin`](examples/demo-plugin) does everything a plugin can with made-up data: copy it to start.

```json
{
  "id": "example",
  "name": "Example",
  "version": "1.0.0",
  "minAppVersion": "0.1.8",
  "main": "index.js",
  "playback": "stream",
  "permissions": { "network": ["api.example.com"] },
  "settings": [{ "key": "apiKey", "label": "API Key", "help": "From your account page", "link": "https://example.com/keys" }],
  "navigation": [
    { "builtin": "home" },
    { "title": "Charts", "page": "charts", "icon": "chart" },
    { "title": "Stations", "builtin": "stations" }
  ]
}
```

```js
export async function search({ query, kind, offset }) {
  const res = await fetch(`https://api.example.com/search?q=${encodeURIComponent(query)}&type=${kind}&offset=${offset}`, {
    headers: { authorization: `Bearer ${host.setting("apiKey")}` },
  });
  return { tracks: (await res.json()).items.map(toTrack), more: false };
}

export function stream({ id, quality }) {
  return { url: `https://api.example.com/audio/${id}.mp3`, type: "mp3" };
}
```

Export a function for each thing the plugin does. Each takes one object of parameters and returns a value or a promise. What it doesn't export, the app leaves out of its pages.

| Export | Parameters | Returns |
| --- | --- | --- |
| `signIn`, `signOut`, `account` | | `{id, name, imageUrl, page}`; `account` returns `null` when signed out. `page` is a `browse` page of the listener's own, which the account menu opens as My Page |
| `setSetting` | `{key, value}` | |
| `home` | | `Browse` |
| `browse` | `{page}` | `Browse` |
| `search` | `{query, kind, offset}`, where `kind` is `tracks`, `albums`, `artists`, `playlists` or `shows` | `{tracks or albums or ..., more}` |
| `suggest` | `{query}` | `[string]` |
| `recent` | | `[Track]` |
| `played` | `{id}` | |
| `liked` | `{offset}` | `{tracks, more}` |
| `isLiked` | `{ids}` | `{id: bool}` |
| `like`, `likeEpisode` | `{id, on}` | `like` likes a song, and `likeEpisode` an episode: without it, episodes show no heart |
| `album` | `{id}` | `{album, tracks}` |
| `artist` | `{id}` | `{artist, tracks, albums}` |
| `saveAlbum`, `followArtist`, `savePlaylist`, `subscribeShow` | `{id, on}` | |
| `savedAlbums` | `{offset}` | `{albums, more}` |
| `playlists` | | `[Playlist]` |
| `playlist` | `{id}` | `Playlist` with `tracks` |
| `createPlaylist` | `{name}` | `Playlist` |
| `renamePlaylist` | `{id, name}` | |
| `deletePlaylist` | `{id}` | |
| `addToPlaylist`, `removeFromPlaylist` | `{id, trackIds}` | |
| `movePlaylistTrack` | `{id, from, to}` | |
| `shows` | | `[Show]` |
| `show` | `{id, offset}` | `{show, episodes, more}` |
| `stations` | | `[Station]` |
| `stationNext` | `{id}` | `[Track]` |
| `comments` | `{trackId, offset}` | `{comments, total, more}` |
| `likeComment` | `{trackId, commentId, on}` | |
| `postComment` | `{trackId, text}` | `Comment` |
| `lyrics` | `{id}` | `{lrc, translation}`, or `{lines}` with timed `words` |
| `stream` | `{id, quality}` | `{url, type, headers, size, gain, peak}`, where `type` is `mp3`, `flac`, `ogg`, `wav`, `m4a` (ALAC, FLAC or AAC-LC, whole or in fragments as a DASH stream serves it) or `aac` (AAC-