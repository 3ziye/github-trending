<p align="center">
  <img src="docs/home.jpg" width="900" alt="Luma's Home by day: Hello, Alex with the date, five round scene buttons, a 3D model of the home floating on pale silver silk and a row of favourite apps">
</p>

<h1 align="center">Luma</h1>

<p align="center">
  A calm, tvOS-inspired home screen for Android TV and Google TV.<br>
  Your favourite apps over living wallpapers, with no ads, no sponsored rows and no tracking.
</p>

<p align="center">
  <a href="#install"><b>Install</b></a> &nbsp;·&nbsp;
  <a href="#make-luma-your-home-screen"><b>Make it your home screen</b></a> &nbsp;·&nbsp;
  <a href="#support-the-project"><b>Support the project</b></a>
</p>

<p align="center">
  Made by <a href="https://x.com/0xProbabillity">@0xProbabillity</a>
</p>

## What it does

Luma works on its own: it needs no smart home, account or other app. Everything below except the scene block
works on any Android TV.

- **A quiet Home.** A greeting with today's date, your favourite apps as large cards, and nothing you did not put
  there. Moving to an app shows its name and a line about it; hold OK on any app to show it on Home, move it or
  hide it.
- **Home widgets, page by page.** Above your apps, Home can show *Up Next* (the shows and videos you were
  watching, from the Continue watching list that YouTube, Netflix and other apps share with Android TV: OK
  resumes where you stopped), *Weather* (now, the next hours or the coming days), *Now Playing* (music playing on
  the TV, with play, pause and skip), *Inputs* (on a TV: its HDMI ports and live TV; a PlayStation, Xbox, Nintendo
  Switch, Apple TV, Chromecast, Fire TV, soundbar and more are recognised over HDMI-CEC and shown under their own
  name and colour; OK switches to it and Home comes back) and *Control* (Wi-Fi, picture and sound,
  accessories, settings). Left and Right turn the pages; your apps stay underneath.
- **Every app, one tab away.** *Apps* lists everything installed on the TV, hidden apps included.
- **Light by day, dark at night.** The default wallpaper, *Silver*, is pale silver silk from sunrise to sunset and
  graphite silk after dark, and the whole interface turns light or dark with it. Sunrise and sunset are worked out
  for your TV's time zone, with no location permission and no network.
- **Living wallpapers.** Eight of them, from silver silk and a Norwegian fjord at dusk to the Milky Way. On the
  fjord, clouds drift and the water moves very slowly, with real depth: the sky and the mountains travel at
  different speeds as you move. Everything pauses while an app is open.
- **Feels like a TV, not a phone.** Springy focus, cards that tilt toward the direction you move, a pill that
  slides along the tab bar, and soft, quiet navigation sounds. *Fluid motion* and *Navigation sounds* turn off
  in Settings, and Android's own animation settings are respected.
- **Your smart home, if you have one.** The scene block appears only when
  [House Control TV](https://github.com/0xProbabillity/house-control-tv) is installed: Home then also shows five
  round scene buttons and a live 3D model of your home floating on the wallpaper, and a scene can open an app as
  the lights go down (*Movie* starts Netflix). Without it, Home is just your greeting and favourites over the wallpaper, and Luma picks House
  Control up as soon as you install it.
- **Easy to leave.** Settings → *Home screen* hands Home back to your TV's own launcher, and
  `./luma.sh restore` undoes everything the installer changed.

<p align="center">
  <img src="docs/scenes.jpg" width="49%" alt="At night: the Cozy scene button in focus, with its description in the greeting, on graphite silk">
  <img src="docs/wallpapers.jpg" width="49%" alt="The wallpaper picker previewing the Milky Way">
  <img src="docs/settings.jpg" width="49%" alt="Settings in the light look: wallpaper, your name, clock, motion and sound">
  <img src="docs/support.jpg" width="49%" alt="Settings → Support the author: four QR codes for tips in crypto">
</p>

<p align="center">
  <img src="docs/widgets.jpg" width="100%" alt="Home widgets: Up Next with three videos and their progress, and the weather in Miami for the next hours">
  <img src="docs/inputs.jpg" width="49%" alt="Inputs with a recognised PlayStation 5, Xbox Series X and Apple TV on HDMI 1 to 3, next to Now Playing">
  <img src="docs/widget-editor.jpg" width="49%" alt="Settings → Home widgets: switches for each widget and miniature pages of Home">
</p>
<p align="center"><sub>Shown with Luma's promo demo (<code>--es luma.demo promo</code>): the videos, the song and the consoles are made up.</sub></p>

## Requirements

| | You need |
| --- | --- |
| TV | Android TV or Google TV, Android 8.0 or newer, with **USB / network debugging** turned on (Settings → Device Preferences → About: press *Build* 7 times, then Developer options) |
| Computer | macOS or Linux with [ADB](https://developer.android.com/tools/releases/platform-tools) (`brew install --cask android-plat