<div align="center">

<img src="docs/assets/icon-512.png" width="96" alt="">

# Free My TV

**A fast, ad-free home screen for Google TV, LG and Samsung TVs.**

Trending picks from your own apps, the weather at a glance, and a look that follows the sunset.<br>
Open source. Built with Claude Code. One button to undo.

[**freemytv.io**](https://freemytv.io) · [Install](#install) · [LG TVs](#lg-tvs-webos) · [Samsung TVs](#samsung-tvs-tizen) · [Any TV](#any-tv) · [Make it yours](#make-it-yours)

<img src=".github/preview.webp" width="880" alt="The Free My TV home screen: a glass shelf of apps, trending picks, and a drawer with the weather and crypto prices">

</div>

## What you get

- **No ads.** No sponsored rows, banners or autoplaying promos. Not one.
- **Your apps, front and center.** The streaming apps you actually use, on a glass shelf. Pick them and their order right on the TV.
- **Trending, not sponsored.** Three fresh picks every hour (up to six, in Home Settings) from what's trending this week and the latest releases, only from apps you already have. Movies and Shows get their own tabs.
- **Weather and markets, one press away.** The hour-by-hour forecast (or the next 5 days), sunrise and sunset, and live crypto prices.
- **What's playing.** Music, a podcast or the radio going on in the background shows on the home screen and the screensaver: the title, the artist and the app, from any app that tells Android what it plays (*Home Settings*, off until you turn it on).
- **Light by day, dark by night.** It follows your city's real sunset, the way your phone does.
- **A screensaver to match.** Full-screen photos of the picks with a big glass clock. Optionally (*Watch from the screensaver*, in Home Settings), OK opens the title on screen in its app, and any other button just closes it.
- **Your own photos** (Google TV and Android TV). Send them from your computer (up to 100): the screensaver shows them, and without picks one is the home screen's background each hour.
- **Fast.** 60 fps, every frame in 16.6 ms, on the TV's own chip. The home screen uses 96 MB of memory instead of 242 MB (−60%).<br><sub>Measured on a 98″ TCL Google TV running Android 14.</sub>
- **Set up on the TV.** Language, your city, temperature, theme, how many picks and which streaming services they come from, the weather and prices cards, the forecast's hours or days, which coins, and the apps on the shelf, in Free My TV's own settings.
- **Safe.** No root. Nothing is uninstalled. One button brings back the factory home screen.

## Install

About ten minutes. You need a Google TV or Android TV (Android 8 or newer) and a computer on the same Wi-Fi.

### The easy way: an AI assistant

1. **On the TV**, turn on developer mode: Settings → System → About → press *Android TV OS build* 7 times. Then Settings → System → Developer options → turn on **USB debugging**. Write down the TV's IP address (Settings → Network & Internet).
2. **On your computer**, open an AI coding assistant ([Claude Code](https://claude.com/claude-code), Codex or Antigravity) and say:
   > Install Free My TV (github.com/simbasjungles/free-my-tv) on my TV at 192.168.1.50. I live in Lisbon.

   It downloads the code, installs the tools it needs, builds the app and puts it on your TV, and asks before anything important. Swap in your TV's IP and your city.
3. **On the TV**, open *Free My TV* → *Home Screen* → *Free My TV*. That's when the TV asks *Allow USB debugging?* for Free My TV: tick *Always allow* and accept.

### The ready APK

No tools to install besides adb. The APK on the [latest release](https://github.com/simbasjungles/free-my-tv/releases/latest) has no TMDB key: add yours on the TV for the picks (*Home Settings* → *TMDB key*, [below](#the-tmdb-key)). It takes your city from the TV's time zone (change it in *Home Settings* → *City*).

1. **On the TV**, do step 1 above.
2. **On your computer**, download `FreeMyTV.apk` from the release and install it:
   ```bash
   adb connect 192.168.1.50:5555
   adb install -r FreeMyTV.apk
   ```
   On Android 14, Google Play Protect may hold the install with *Risky app blocked*: choose *More details* → *Install anyway*.
3. **On the TV**, do step 3 above.

If you built Free My TV yourself before, switch back to *Original* and uninstall it first: your build and the release are signed with different keys. For the picks, add your TMDB key in *Home Settings* → *TMDB key* (below).

**Updates come to the TV.** Once a week the APK from the release looks for a newer release and downloads it; the home screen then says so once, and *Home Settings* → *Updates* (the last row) installs it through Android's installer, which asks first (and, the first time, asks to allow Free My TV to install apps). OK on *Updates* also checks right away. The download must come from this repository's releases, match the size and SHA-256 GitHub lists, be newer, and be signed with the project's key. A build you made yourself checks only when you press *Updates*