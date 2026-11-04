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
- **Trending, not sponsored.** Three fresh picks every hour (up to six, in Home Settings) from what's trending this week and the latest releases, only from apps you already have, and from the services you choose. The focused one opens wide and the others show their posters. Movies and Shows get their own tabs, and on Google TV your own [Plex library](#your-plex-library-optional) can join in.
- **Continue Watching** (Google TV and Android TV). *Home Settings* → *Top of the screen* puts what you left halfway in your apps on top, with its progress, and OK picks it up in its app. Or a big clock, or the picks.
- **Your TMDB key from your phone.** *Home Settings* → *TMDB key* shows a QR code: scan it and paste the key. On LG and Samsung, type it with the remote.
- **Weather and markets, one press away.** The hour-by-hour forecast (or the next 5 days), sunrise and sunset, and live crypto prices.
- **What's playing.** Music, a podcast or the radio going on in the background shows on the home screen and the screensaver: the title, the artist and the app, from any app that tells Android what it plays (*Home Settings*, off until you turn it on).
- **The status at a glance, and a mouse** (Google TV and Android TV). *Home Settings* → *Status icons* puts Wi-Fi or Ethernet, Bluetooth audio and a USB drive at the top of the home screen; off, nothing listens for them. A mouse or an air-mouse remote works too: hover moves the focus, the wheel scrolls, a click picks.
- **Light by day, dark by night.** It follows your city's real sunset, the way your phone does.
- **A screensaver to match.** Full-screen photos of the picks with a big glass clock. On LG and Samsung, *Home Settings* → *Screensaver* can make it a large clock with the weather instead, drifting slowly so it doesn't burn into OLED screens. Optionally (*Watch from the screensaver*, in Home Settings), OK opens the title on screen in its app, and any other button just closes it.
- **Dimming for a dark room** (LG and Samsung). *Home Settings* → *Dim* darkens Free My TV's own screens, not the apps you open: low, medium, high, or automatic (medium from 22:00 to 07:00). Off until you pick it.
- **Your own photos** (Google TV and Android TV). Send them from your computer (up to 100): the screensaver shows them, and without picks one is the home screen's background each hour.
- **Fast.** 60 fps, every frame in 16.6 ms, on the TV's own chip. The home screen uses 96 MB of memory instead of 242 MB (−60%).<br><sub>Measured on a 98″ TCL Google TV running Android 14.</sub>
- **Set up on the TV.** Language, your city, temperature, theme, how many picks and which streaming services they come from, the weather and prices cards, the forecast's hours or days, which coins, and the apps on the shelf, in Free My TV's own settings.
- **Safe.** No root. Nothing is uninstalled. One button brings back the factory home screen.

## Install

About ten minutes. You need a Google TV or Android TV (Android 8 or newer) and a computer on the same Wi-Fi. The APK goes on the TV, not on your phone (on a phone, the settings say so and nothing switches).

### The easy way: an AI assistant

1. **On the TV**, turn on developer mode: Settings → System → About → press *Android TV OS build* 7 times. Then Settings → System → Developer options → turn on **USB debugging**. Write down the TV's IP address (Settings → Network & Internet).
2. **On your computer**, open an AI coding assistant ([Claude Code](https://claude.com/claude-code), Codex or Antigravity) and say:
   > Install Free My TV (github.com/simbasjungles/free-my-tv) on my TV at 192.168.1.50. I live in Lisbon.

   It downloads the code, installs the tools it needs, builds the app and puts it on your TV, and asks before anything important. Swap in your TV's IP and your city.
3. **On the TV**, open *Free My TV* → *Home Screen* → *Free My TV*. That's when the TV asks *Allow USB debugging?* for Free My TV: tick *Always allow* and accept.

### The ready APK

No tools to install besides adb. The APK on the [latest release](https://github.com/simbasjungles/free-my-tv/releases/latest) 