<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="branding/mediarium-lockup-dark.svg" />
    <img src="branding/mediarium-lockup-light.svg" alt="Mediarium" height="64" />
  </picture>
</p>

<p align="center"><b>Your movies, TV, music and books, from search to library, in one app.</b></p>

<p align="center">
  <a href="docs/INSTALL.md">Install</a> ·
  <a href="docs/README.md">Documentation</a> ·
  <a href="docs/FEATURES.md">Features</a> ·
  <a href="CHANGELOG.md">Changelog</a> ·
  <a href="https://github.com/rdborg/Mediarium/issues">Report a bug</a> ·
  <a href="https://github.com/rdborg/Mediarium/discussions">Ideas and questions</a> ·
  <a href="https://www.reddit.com/r/Mediarium/">Reddit</a>
</p>

# Mediarium

Mediarium is a self-hosted media manager. Find a movie or show, and it searches your Usenet and torrent indexers, downloads the best release, unpacks it, names it and puts it in your library, ready for Plex, Jellyfin or Emby.

It does the jobs of Radarr, Sonarr, Prowlarr, SABnzbd, a torrent client and Bazarr in **one app**: one container, one web page, one search bar, one thing to update and back up.

- **Movies and TV** (anime, daily shows and specials included), plus **music**, **ebooks** and **audiobooks** if you switch them on.
- **Mediarium Books**, a built-in reader and audiobook player that opens as an app of its own and remembers your place on every device. It reads Kindle books too, jumps between audiobook chapters, and follows book series.
- **Tags** such as Kids or 4K, which also show up as collections in Plex, Jellyfin and Emby.
- **Discover and search** everything from one place, across all your indexers.
- **Built-in downloaders** for Usenet and torrents, with repair and unpacking.
- **Built-in VPN** for torrents (WireGuard), with no special container permissions.
- **Quality profiles** with upgrades and fallbacks, automatic searching and retries.
- **Family accounts with permissions and requests**: choose what each person can do, and anyone who can't add titles sends a request for you to approve.
- **Subtitles** picked to match your exact file, with a timing fix when one is out of sync.
- **What's been watched**, read from Plex, Jellyfin and Emby, with watch statistics and optional cleanup rules (all off until you switch them on).
- Notifications, media-server refresh (Plex, Jellyfin, Emby, Audiobookshelf, Kavita), download hours, backups, and your own script after each import.
- **Move over from Radarr, Sonarr, Prowlarr, SABnzbd** and eight other apps without redoing your setup. They are only read, never changed.
- Runs on **Synology, Unraid, QNAP, any Linux server** and 64-bit Raspberry Pi.

**Privacy:** there are no ads, and Mediarium sends nothing about you or your library anywhere. It asks once whether you want to share a small anonymous message a day (a random ID, the version and rough device sizes) so the project can see which devices are popular: it is off until you say Yes, the numbers are public at [mediarium.app/stats](https://mediarium.app/stats/), and the code is open. [What exactly is sent](docs/usage-stats.md).

Mediarium is new. Movies and TV work end to end, and so do music, ebooks and audiobooks once you switch them on. It's used daily, but expect some rough edges. [FEATURES.md](docs/FEATURES.md) says what works and what doesn't yet.

## Screenshots

| | |
|---|---|
| ![Dashboard with a card for each kind of media and a Server card](docs/images/dashboard.png) | ![Discover with rows of movies and shows like the ones in your library](docs/images/discover.png) |
| **Dashboard**: what needs attention, a card per kind of media and the Server card | **Discover**: more like your library, trending, popular and coming soon |
| ![Library of movies with a status badge on each poster](docs/images/library.png) | ![Activity page with downloads in progress, waiting in line and failed](docs/images/activity.png) |
| **Library**: every title with its status, and Select to change many at once | **Activity**: what is downloading, waiting in line or failed, plus history and blocklist |
| ![Upcoming calendar for the month](docs/images/upcoming-calendar.png) | ![An artist page in the music library](docs/images/music-artist.png) |
| **Upcoming**: the calendar of releases and episodes, and what is still wanted | **Music**: artists and albums, off until you switch it on |
| ![Discover on the eBooks and Audiobooks tab, with a corner banner on each cover saying eBook, Audiobook or both](docs/images/discover-books.png) | ![The Mediarium Books shelf with the books you are reading or listening to at the top](docs/images/bookshelf.png) |
| **Books**: trending and classic books, each marked eBook, Audiobook or both | **Mediarium Books**: your shelf, with the reader and the audiobook player |
| ![The Media types page with cards for movies, TV shows, music, audiobooks and ebooks](docs/images/settings-modules.png) | ![The Quality page with the quality profiles table