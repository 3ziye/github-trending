# Android TV Makeover

Debloat an Android TV over Wi-Fi, replace its ad-filled home screen with a clean Apple TV style
launcher, control it from your phone, and add a fast live TV app for Indian channels. Everything is
reversible.

- **Launcher:** your photos fading behind the home screen, a dock of 5 apps, a 5-column app grid,
  clock and greeting, YouTube / Instagram / Facebook follower counters, HDMI/AV switcher.
- **Phone remote:** a web page served by the TV. Trackpad, keyboard, volume, apps, inputs, sending
  photos to the TV, and Siri shortcuts. Works in Safari on iPhone and in any phone browser.
- **Live TV app:** Indian channels in categories, 1080p only, smooth on a 1 GB TV.

Built and tested on a Xiaomi MiTV-AXSO0 (Android TV 9, 1 GB RAM). It should work on most Android TV /
Google TV sets (Xiaomi, TCL, Hisense, Sony, OnePlus, Realme, Nvidia Shield). It does not work on
Samsung Tizen, LG webOS or Fire TV.

| Home screen | Inputs menu |
|---|---|
| ![Launcher home](docs/images/launcher-home.png) | ![Inputs menu](docs/images/launcher-inputs.png) |

| App grid (5 per row) | Phone remote |
|---|---|
| ![App grid](docs/images/launcher-grid.png) | <img src="docs/images/phone-remote.png" alt="Phone remote: trackpad, buttons and keyboard" width="180"> <img src="docs/images/phone-apps.png" alt="Phone remote: apps and inputs" width="180"> |

| Live TV app | Categories |
|---|---|
| ![Live TV](docs/images/live-tv-all.png) | ![News](docs/images/live-tv-news.png) |

## What's inside

| Path | What it is |
|---|---|
| `launcher/` | Native Android TV launcher (Java, AndroidX RecyclerView, minSdk 28, ~40 MB RAM). Rotating photo wallpapers (or pitch black), a dock of five apps with a colour glow sampled from the focused app, a 5-column app grid below (the number per row is a setting), one glass focus highlight, clock and greeting in Outfit, frosted Inputs / Wi-Fi / Settings pills, follower counters, HDMI/AV/Live TV input switcher, deterministic D-pad navigation. Also runs the phone remote's web server. |
| `apps/live-tv/` | Live TV app (Flutter), a modified fork of [kananinirav/Indian-IPTV-App](https://github.com/kananinirav/Indian-IPTV-App). Category sidebar, small channel logos, 1080p streams only, instant start from cache, Up/Down channel switching, automatic backup streams. See [apps/live-tv/README.md](apps/live-tv/README.md). |
| `tools/tv` | Tiny ADB client in Python (`adb-shell`): `shell`, `screenshot`, `push`, `pull`, `key`. Works when macOS Local Network privacy blocks the stock `adb` binary. |
| `profiles/` | Debloat profiles: which packages to disable for a given TV. |
| `PROMPT.md` | The prompt to give a coding assistant (e.g. Claude Code) to do all of this on your TV, step by step, with screenshots. |

## Quick start

On the TV: Settings → Device Preferences → About → press OK on **Build** 7 times, then go back →
Developer options → turn on **USB debugging** (and Network/ADB debugging if your TV shows it).

On a Mac or Linux computer on the same Wi-Fi:

```bash
./setup.sh
```

```bash
tools/find-tv.sh
```

Accept the "Allow USB debugging?" prompt on the TV (tick "Always allow"). Then back up first:

```bash
./backup.sh
```

### 1. Debloat

Profiles list packages to disable with `pm disable-user` (nothing is uninstalled). Package names differ
between brands, so for another TV copy the profile and edit it; check what a package does with
`tools/tv shell "dumpsys package <name>"`. Never disable TV input services, the remote/Bluetooth
services, the keyboard, or Play Store/Services.

```bash
./disable.sh profiles/xiaomi-mitv-axso0.txt
```

### 2. Launcher

Edit `launcher/app/src/main/res/values/config.xml` (dock apps, hidden apps, greeting name, wallpaper),
then:

```bash
./build_and_install.sh
```

Needs JDK 17 and the Android SDK (platform 34, build-tools 34): `brew install openjdk@17` and
`brew install --cask android-commandlinetools`, then
`sdkmanager "platforms;android-34" "build-tools;34.0.0"`. If several apps claim Home, the script sets
the default with `cmd package set-home-activity`.

### 3. Live TV app (optional)

Needs Flutter (`brew install --cask flutter`):

```bash
./build_live_tv.sh
```

### Undo everything

```bash
./restore.sh profiles/xiaomi-mitv-axso0.txt --uninstall
```

Or re-enable a single app: `tools/tv shell "pm enable <package>"`.

## Phone remote

The launcher serves a control page on your home Wi-Fi at `http://<TV IP>:8080` (the IP is in
`.tv-ip` after `tools/find-tv.sh`, or in the TV's Wi-Fi settings).

1. Open it in Safari (or any phone browser) on the same Wi-Fi.
2. Tap **Pair with TV**. The TV asks "Allow this phone to control the TV?" over whatever is on
   screen: press Right, then OK on the remote. Each phone pairs once.
3. On iPhone: Share → **Add to Home Screen**, and it opens full-screen like an app.

Four tabs:

- **Remote:** a trackpad (swipe to move, tap for OK), Back, Home, play/pause, volume and mute, and a
  keyboard that types live into whatever search box is op