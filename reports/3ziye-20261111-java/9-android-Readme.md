<p align="center">
  <img src="docs/banner.png" alt="FMHYPlay" width="560">
</p>

<p align="center">
  <b>Any streaming site, a real player.</b><br>
  A TV-first Android app that opens the sites you choose, finds the video they play, and plays it in a native hardware-accelerated player.
</p>

<p align="center">
  <a href="https://github.com/fmhyplay/android/releases/latest"><img alt="Release" src="https://img.shields.io/github/v/release/fmhyplay/android?color=ff3b5c"></a>
  <a href="https://github.com/fmhyplay/android/actions/workflows/build.yml"><img alt="Build" src="https://img.shields.io/github/actions/workflow/status/fmhyplay/android/build.yml?branch=main"></a>
  <img alt="Android 8.0+" src="https://img.shields.io/badge/Android-8.0%2B-3ddc84">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue">
</p>

<p align="center">
  <a href="https://fmhyplay.github.io/android/">Documentation</a> ·
  <a href="https://github.com/fmhyplay/android/releases/latest">Download</a> ·
  <a href="https://fmhyplay.github.io/android/guide.html">User guide</a> ·
  <a href="https://fmhyplay.github.io/android/build.html">Build from source</a> ·
  <a href="https://buymeacoffee.com/rohit267">Support</a>
</p>

<p align="center">
  <img src="docs/screenshots/player.jpg" alt="FMHYPlayer" width="760">
</p>

## Why

Streaming sites are built for a desktop browser with a mouse. On a TV remote they are painful, they are full of pop-ups, and their embedded players stutter on weak hardware. FMHYPlay keeps the site (so you keep every title and server it offers) but takes over the part that goes wrong:

- It **finds the video stream** the page starts and plays it in **FMHYPlayer** (ExoPlayer with the hardware decoder), with nothing painted over the picture.
- It **drives the site for you**: pick a title and it opens that title's page (or the exact episode); the player's Episodes, Sub / Dub, Servers and Quality buttons press the site's own buttons, so you do not go back to the page.
- It **blocks ads and pop-ups**, **tunnels the app's own traffic** through Cloudflare WARP when you want it, and works with a **TV remote** and with **touch**.

## Features

**Cast to TV**
- The **Cast** button in the phone's player sends the video to a TV on the same Wi-Fi, from the same spot. The phone becomes the remote: play, pause, seek, ±10 s and TV volume (the phone's volume keys work too)
- **TV with FMHYPlay (recommended)**: the TV plays the stream itself, with the site's headers and cookie, WARP, ad blocking and subtitles. It opens even when FMHYPlay is closed on the TV
- **Chromecast, Google TV and TVs with Cast built in**: no app needed on the TV; the phone relays the stream so sites still accept it
- **DLNA / UPnP smart TVs** (Samsung, LG, Sony, Kodi and others): same relay; works best with MP4 and TS streams, since not every TV plays HLS

<p align="center"><img src="docs/cast.svg" alt="Cast from the phone to a TV on the same Wi-Fi" width="760"></p>

**Series and anime**
- **Episodes** strip in the player (stills and names along the bottom while the video plays), **Previous** and **Next**, and the next episode starts by itself
- **Skip intro, recap and credits** (times from TheIntroDB and AniSkip), with a Next episode button at the credits; *Settings, Skip intros* skips them for you
- **Sub / Dub** button for anime, remembered per site
- Opens the exact episode directly on 34 TV sites and 22 anime sites; elsewhere it presses the episode in the site's own list or menus

**FMHYPlayer**
- Hands off automatically when a page starts an HLS, DASH or live FLV stream; falls back to the page if the stream cannot be played
- Icon buttons in two groups: Previous, Next, Episodes on the left; Quality, Audio, Sub / Dub, Servers, Subtitles, More, Cast, Full screen on the right; menus open as a side panel; what is picked shows under the title, and on a TV the button the remote is on shows its name
- Replays the page's Referer, Origin and cookies, so streams that check them still play
- **Resumes where you stopped on any site or server**, with a Restart button; the place is saved every 10 seconds while you watch, and the subtitles you had on come back
- Quality list with frame rate (for example 1080p60), audio and subtitle tracks, speed and zoom modes
- **Servers and Quality buttons that control the site's own player**, including players inside cross-origin iframes
- **Volume boost** (up to +12 dB) and **Dialog boost** (clearer voices, off until you turn it on in Settings or in the player)
- **Debug overlay** (*More, Debug overlay*, off by default): a panel down the right edge with resolution, frame rate, codec and decoder (hardware or software), video and audio bitrate, network speed, buffer, frames shown and dropped, stream type, host, how long the video took to open, and memory, refreshed every second
- **Subtitles in any language** from OpenSubtitles, converted so every script shows right, remembered per title, optional auto subtitles in your l