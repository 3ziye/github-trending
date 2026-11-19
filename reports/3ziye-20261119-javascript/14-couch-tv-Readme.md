<p align="center"><img src="docs/screens/banner.png" alt="couch-tv on a TV: the Night home screen with the glass clock, Keep watching and the app dock" width="100%"></p>

<p align="center">
  <b>Your own home screen and phone remote for the TV.</b><br>
  Scenes with a glass clock, your apps in your order, Keep watching across apps,
  and a phone remote that finds a show and starts it. No ads on the home screen. Open source.
</p>

<p align="center">
  <a href="https://github.com/Seagey/couch-tv/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/Seagey/couch-tv?style=flat-square&label=release&color=5b5bd6"></a>
  <a href="LICENSE"><img alt="MIT licence" src="https://img.shields.io/badge/licence-MIT-3a3a40?style=flat-square"></a>
  <a href="#will-it-work-on-my-tv"><img alt="Google TV, Android TV, Fire TV, Samsung, LG, Roku, Apple TV and more" src="https://img.shields.io/badge/TVs-Google%20TV%20%C2%B7%20Android%20TV%20%C2%B7%20Fire%20TV%20%C2%B7%20Samsung%20%C2%B7%20LG%20%C2%B7%20Roku%20%C2%B7%20more-3a3a40?style=flat-square"></a>
</p>

<p align="center"><b>
  <a href="#get-started">Set it up</a>
  &nbsp;·&nbsp; <a href="#will-it-work-on-my-tv">Which TVs</a>
  &nbsp;·&nbsp; <a href="docs/README.md">Docs</a>
  &nbsp;·&nbsp; <a href="docs/UPDATES.md">What's new</a>
</b></p>

## Get started

1. **With your AI agent, the easiest way.** Open this folder in Claude Code (or any coding agent)
   and say "set this up on my TV". It reads [AGENTS.md](AGENTS.md), finds your TV, asks which option
   you want and a few questions (who watches, the look, your apps), reads the plan back, and changes
   nothing on the TV until you say yes.
2. **From your phone or a computer:** [couchtv.sites.underseage.studio](https://couchtv.sites.underseage.studio),
   with the free Setup app on a Mac or Windows computer. It also checks whether your TV will work.
3. **By hand:** [docs/SETUP.md](docs/SETUP.md) has every step, from developer mode to the TV home,
   and how to [undo it](docs/SETUP.md#undo-put-the-google-home-screen-back).

**Pick the way for your TV before you start.** Not every way does the whole job on every TV:

| Way | What you need | Google TV | Android TV | Fire TV | Samsung or LG |
|---|---|---|---|---|---|
| **AI agent** ([AGENTS.md](AGENTS.md)) | A computer on the TV's Wi-Fi with Claude Code or another coding agent | Yes, Home button included | Yes | Yes, Home button included (Amazon's home flashes up first). The full phone remote keeps a computer on at home | Yes, as an app that a computer at home that stays on opens. Their own Home button still opens their own menu |
| **From your phone** ([website](https://couchtv.sites.underseage.studio/phone)) | The TV remote and a phone on the same Wi-Fi. No computer | Only part: the app and the phone remote, but Google keeps the Home button. AI or the Setup app adds the Home button once, even afterwards | Yes. On Android TV 10 and newer the app asks Android to make it the home | Only part: Home needs three one off grants from a computer, and on current Fire OS the phone remote can't press keys or type | No |
| **Setup app** ([website](https://couchtv.sites.underseage.studio/computer)) | A Mac or Windows computer on the same Wi-Fi, once | Yes, Home button included | Yes, Android TV 7.1 and newer | Yes on Fire OS 6, 7 and 8 (Amazon's home flashes up first) | No |
| **By hand** ([docs/SETUP.md](docs/SETUP.md)) | A Mac or Linux computer with Python 3.11 or newer | Yes | Yes | [on-tv/README.md, Fire TV](on-tv/README.md#fire-tv-fire-os) | [docs/SAMSUNG.md](docs/SAMSUNG.md), [docs/LG.md](docs/LG.md), with a computer at home that stays on |

Other TVs: [Will it work on my TV?](#will-it-work-on-my-tv)

> [!NOTE]
> Set couch-tv up with 0.10 or older on a Google TV? 0.11 and newer leave the Google home and setup
> apps switched on. Read [If your TV loops after a restart](docs/TROUBLESHOOTING.md#if-your-tv-loops-after-a-restart)
> before you next restart your TV.

<a name="setup"></a><a name="setting-it-up-with-an-ai-agent"></a><a name="what-you-need"></a><a name="step-1-developer-mode-on-the-tv-every-option"></a><a name="step-2-get-the-code-and-set-up-python-every-option"></a><a name="step-3-pair-the-tv-with-the-bridge-option-b"></a><a name="step-4-build-the-phone-remote-option-b"></a><a name="step-5-run-the-bridge-option-b"></a><a name="step-6-put-the-tv-home-on-the-tv-options-a-and-b-it-becomes-the-home-the-google-home-stays-on"></a><a name="building-the-app-instead-of-downloading-it"></a><a name="undo-put-the-google-home-screen-back"></a><a name="if-your-tv-loops-after-a-restart"></a><a name="troubleshooting"></a><a name="tcl-home-goes-back-to-google-tv-after-every-restart"></a><a name="if-disney-or-another-app-signs-you-out-after-the-tv-turns-off"></a><a name="seeing-every-app"></a>

## Updates

The newest release is **0.13.5**, on [the Releases page](https://github.com/Seagey/couch-tv/releases): fixes from a real beginner on a TCL (Use as home screen