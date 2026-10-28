<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/logo-dark.svg">
    <img src="docs/assets/logo-light.svg" alt="dumbtv" width="300">
  </picture>
</p>

<p align="center"><b>Your TV should do what you paid for.</b><br>
Ads, tracking and clutter out of your Fire TV. Your apps and HDMI inputs stay.</p>

<p align="center">
  <a href="https://dumbtv.org"><b>dumbtv.org</b></a> ·
  <a href="https://dumbtv.org/start">Get started</a> ·
  <a href="https://dumbtv.org/blocked">What it blocks</a> ·
  <a href="https://dumbtv.org/tv">Devices</a> ·
  <a href="https://dumbtv.org/help">Get help</a>
</p>

<p align="center">
  <a href="https://github.com/humblemuzzu/dumbtv/stargazers"><img src="https://img.shields.io/github/stars/humblemuzzu/dumbtv?style=flat&color=4C8DFF" alt="Stars"></a>
  <a href="https://github.com/humblemuzzu/dumbtv/releases/latest"><img src="https://img.shields.io/github/v/release/humblemuzzu/dumbtv?label=dumbtv%20home&color=4C8DFF" alt="Latest launcher release"></a>
  <a href="https://github.com/humblemuzzu/dumbtv/actions/workflows/validate.yml"><img src="https://github.com/humblemuzzu/dumbtv/actions/workflows/validate.yml/badge.svg" alt="CI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-4C8DFF" alt="MIT licence"></a>
  <a href="#thanks"><img src="https://img.shields.io/github/contributors/humblemuzzu/dumbtv?color=4C8DFF" alt="Contributors"></a>
</p>

<p align="center">
  <img src="docs/assets/hero.png" alt="dumbtv home on a television: a clock, an Apps row and an Inputs row" width="880">
</p>

<p align="center"><sub>As seen in
<a href="https://techcrunch.com/2026/10/19/people-are-using-ai-to-make-their-smart-tvs-dumb-again/">TechCrunch</a> ·
<a href="https://www.techradar.com/entertainment/streaming/your-tv-should-do-what-you-paid-for-people-are-vibe-coding-apps-to-banish-ads-from-their-smart-tvs-and-android-tv-and-its-catching-on">TechRadar</a> ·
<a href="https://www.tomsguide.com/ai/people-are-using-ai-to-turn-their-smart-tvs-into-dumb-tvs-and-you-might-want-to-do-the-same">Tom's Guide</a> ·
<a href="https://gizmodo.com/people-using-ai-to-make-smart-tvs-dumb-again-is-the-most-2026-thing-ever-2000828213">Gizmodo</a> ·
<a href="https://www.xda-developers.com/people-are-now-vibe-coding-their-smart-tvs-to-strip-them-of-ads-and-unwanted-features/">XDA</a> ·
<a href="https://itsfoss.com/news/debloat-smart-tv/">It's FOSS</a> ·
<a href="docs/PRESS.md">and more than 100 others</a></sub></p>

---

## The story

I had a Fire TV Edition television that had become painful to use. Menus lagged,
apps took ages to open, and the home screen was mostly ads. When I looked, it had
129 MB of free memory, and much of the rest went to apps that started on their own
and to Amazon services that report what you watch.

So I asked a coding agent to clean it up over ADB, and
[posted what happened](https://x.com/DevMuzzammil/status/2111595814099591535). People
asked for the scripts, so I put them here and
[shared them](https://x.com/DevMuzzammil/status/2111912547318395338). Since then,
owners of about twenty other TVs and sticks have run it and sent back what they
found.

dumbtv is that cleanup, made safe to run on someone else's TV.

## What it does

On a Fire TV stick, Cube or Fire TV Edition television, from your computer, with
no root:

- **Removes the ads and tracking.** Disables Amazon's sponsored rows, ad
  services, screen fingerprinting (ACR), telemetry and experiments, and turns off
  ad tracking and usage reporting.
- **Blocks what cannot be disabled.** A small open-source DNS filter on the TV
  stops Amazon's telemetry and automatic updates from reaching their servers.
  Everything else, including your streaming apps, works as before.
- **Replaces the home screen** with [dumbtv home](launcher/README.md): your apps,
  your inputs and a clock. 54 KB, open source, no internet access, no permissions.
- **Leaves your apps alone.** Nothing you watch is removed unless you name it.
- **Can all be undone** with one command.

## Quick start

You need a computer with [`adb`](https://developer.android.com/tools/releases/platform-tools)
and about ten minutes. On the TV, turn on ADB: **Settings → My Fire TV → About**,
press OK on the device name 7 times, then **Developer Options → ADB debugging**.
The TV's IP address is under **Settings → My Fire TV → About → Network** (on a
Fire TV Edition television: **Settings → Network**, then the connected network).

**With a coding agent** (Claude Code, Codex, Cursor, Gemini and others): clone this
repository, open the agent in it, and say:

> Clean up my Fire TV. Its IP address is _(the address from the Network screen)_.

It reads [AGENTS.md](AGENTS.md), asks you a few questions, and runs the steps
below.

**By hand:**

```sh
git clone https://github.com/humblemuzzu/dumbtv && cd dumbtv
adb connect <tv-ip>:5555        # press Allow on the TV
./scripts/preflight.sh          # what the TV is and what would change;