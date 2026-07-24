<div align="center">

# MovieBox-Tui

A terminal client for finding and streaming movies, TV shows, and anime from your keyboard.

[![Crates.io](https://img.shields.io/crates/v/moviebox-tui.svg?logo=rust)](https://crates.io/crates/moviebox-tui)
[![Downloads](https://img.shields.io/crates/d/moviebox-tui.svg)](https://crates.io/crates/moviebox-tui)
[![License](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue.svg)](#license)
[![Rust](https://img.shields.io/badge/rust-1.85%2B-orange.svg?logo=rust)](#requirements)
[![Support](https://img.shields.io/badge/Support-Crypto-gold.svg)](#support)

<br>

<p align="center">
  <img src="https://raw.githubusercontent.com/mesamirh/MovieBox-Tui/main/assets/screenshots/01-home.jpg" alt="MovieBox-Tui home screen" width="88%"/>
</p>

</div>

---

## What is this?

**MovieBox-Tui** is a terminal UI I built to search MovieBox's public catalog and stream the results in my favorite video player, without leaving the terminal. It talks to the MovieBox API directly, resolves the video URLs it returns, and hands them off to `mpv`, `IINA`, or `VLC`.

No browsers, no ads, no login walls, no configuration. Type a title, pick a quality, watch.

> **Note:** This project is a client for a third-party service. It does not host, store, or redistribute any media. It only resolves the links the upstream API returns. It is intended strictly for educational and personal use. You are responsible for complying with copyright law in your jurisdiction.

---

## Demo

A short walkthrough of the app in action:

<div align="center">

**[Watch the demo on YouTube](https://youtu.be/0L1Wc3cwMCc)**

</div>

---

## Contents

- [What it can do](#what-it-can-do)
- [Screenshots](#screenshots)
- [Platform support](#platform-support)
- [Requirements](#requirements)
- [Install](#install)
- [Getting started](#getting-started)
- [Keybindings](#keybindings)
- [How it works](#how-it-works)
- [Project layout](#project-layout)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [License](#license)

---

## What it can do

**Search and discovery**
- Type-to-search with live, debounced suggestions.
- Slash commands to browse curated feeds: `/movies`, `/shows`, `/anime`, `/discover`.
- Each result shows a poster, release year, and (when highlighted) IMDb rating and genres.

**Playback**
- Detects `mpv`, `IINA`, and `VLC` at startup. You get a picker for whatever you have installed.
- Full season and episode browsing for TV series and anime, with per-episode stream resolution.
- Multiple resolutions (1080p, 720p, 480p, 360p) are fetched in parallel and listed by quality.
- Attach external subtitle tracks, and switch between available audio dubs before playing.
- If a stream fails or expires, hit <kbd>R</kbd> to re-resolve it.

**Downloading and sharing**
- Built-in multi-connection downloader. Uses up to 16 parallel connections when the source allows range requests, with live speed, ETA, progress bar, and cancel.
- Copy any direct stream URL to your clipboard with a single keystroke.
- Downloads go to your system Downloads folder.

**The interface**
- Real poster art rendered inline in terminals that support graphics (Kitty, WezTerm, iTerm2, Ghostty, foot, etc.).
- In-app notification when a newer version is published to crates.io.
- The details view shows the poster, IMDb rating, year, genres, duration, country, and full description alongside the season, episode, and stream panels.

---

## Screenshots

<details open>
<summary><b>Home and search</b></summary>
<br>

| Home | Search results |
| :---: | :---: |
| <img src="https://raw.githubusercontent.com/mesamirh/MovieBox-Tui/main/assets/screenshots/01-home.jpg" alt="Home screen" width="480"> | <img src="https://raw.githubusercontent.com/mesamirh/MovieBox-Tui/main/assets/screenshots/02-search-results.jpg" alt="Search results" width="480"> |

</details>

<details>
<summary><b>Details view</b></summary>
<br>

| Movie | TV series |
| :---: | :---: |
| <img src="https://raw.githubusercontent.com/mesamirh/MovieBox-Tui/main/assets/screenshots/03-movie-details.jpg" alt="Movie details" width="480"> | <img src="https://raw.githubusercontent.com/mesamirh/MovieBox-Tui/main/assets/screenshots/04-series-details.jpg" alt="Series details" width="480"> |

</details>

<details>
<summary><b>Discover feeds</b></summary>
<br>

| Movies | Series | Anime |
| :---: | :---: | :---: |
| <img src="https://raw.githubusercontent.com/mesamirh/MovieBox-Tui/main/assets/screenshots/05-discover-movies.jpg" alt="Discover movies" width="320"> | <img src="https://raw.githubusercontent.com/mesamirh/MovieBox-Tui/main/assets/screenshots/06-discover-series.jpg" alt="Discover series" width="320"> | <img src="https://raw.githubusercontent.com/mesamirh/MovieBox-Tui/main/assets/screenshots/07-discover-anime.jpg" alt="Discover anime" width="320"> |

</details>

<details>
<summary><b>Help overlay</b></summary>
<br>

<p align="center">
  <img sr