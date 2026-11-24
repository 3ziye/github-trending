<p align="center"><img src="https://github.com/MatinSenPai/Gemini-Config-Checker/raw/main/assets/banner.png" alt="Gemini/Check" width="100%"></p>

<p align="center">
  <b>English</b> · <a href="README.fa.md">فارسی</a>
</p>

<p align="center">
   <a href="https://www.dropbox.com/scl/fi/l80rdcm1o9gnqcpdsw1gi/GeminiConfigChecker.rar?rlkey=dv7oxsttd2j8kvr5zu7uyx1tm&st=l2vaozdz&dl=1">
    <img alt="Download the Gemini app" src="https://img.shields.io/badge/Download-%20Gemeni%20app-0969DA?style=for-the-badge&logo=github&logoColor=white">
  </a>
</p>

# Gemini Config Checker

Find proxy configs that actually get you into **Google AI Studio and Gemini**, by testing each one the way a person would: in a
*signed-in* browser, through the route you will really use.

> **Version 0.1.0, early pre-release.** It works end to end on Windows (the only platform it has been run on so far). The macOS,
> Linux and Android builds come from the CI pipeline and have not been exercised on real devices yet. Please report what you find.

## Two modes, one switch

The big **Simple / Advanced** switch in the header decides what is tested. The route diagram under the title morphs to show it.

| | **Simple** | **Advanced** |
|---|---|---|
| Question it answers | *Which of my configs work?* | *Which free configs work through my config?* |
| Route | you → **config** → AI Studio / Gemini | you → **base config** → **free config** → AI Studio / Gemini |
| You provide | your configs (links, a subscription URL or base64), or pick a ready-made free list | one working base config, plus a free list or pasted configs |
| Anti-DPI profile is applied to | every config under test (each one connects from your machine) | the base config's first hop (free configs run inside its tunnel) |
| Typical use | check a pile of configs you already have; test a config before you rely on it | your Cloudflare config works, but you need a *different exit* that Google accepts |
| Export | links, base64, a full Xray config of one config | links, base64, a chain Xray config (`base → free`) |

## Contents
[Credits](#credits-and-references) · [Why a signed-in browser](#why-a-signed-in-browser) · [Download and install](#download-and-install) ·
[User guide](#user-guide) · [Troubleshooting](#troubleshooting-and-faq) · [Privacy and security](#privacy-and-security) ·
[Build from source](#build-from-source) · [Releases and CI](#releases-and-ci)

## Credits and references

This project exists because of other people's work. Please go and use and star them.

| Project | What it gave us |
|---|---|
| [**0xRadikal/Free-v2ray-Configs**](https://github.com/0xRadikal/Free-v2ray-Configs) | The auto-updated lists of free configs (`verified`, `fast`, `secure`, ...) that this tool scans |
| [**patterniha**](https://github.com/patterniha) | [PattN](https://github.com/patterniha/PattN) (Windows / Linux / macOS client) and [PattNG](https://github.com/patterniha/PattNG) (Android): the anti-DPI recipe, plus the fragment `finalmask` semantics from his [Xray-core fork](https://github.com/patterniha/Xray-core) that our fragmenting forwarder reproduces |
| [**bia-pain-bache/BPB-Worker-Panel**](https://github.com/bia-pain-bache/BPB-Worker-Panel) | The Cloudflare Worker panel that produces many of the base configs this tool chains behind (patterniha maintains a [fork](https://github.com/patterniha/BPB-Worker-Panel)) |
| [**Anti-DPI recipe post**](https://t.me/MatinSenPaii/5469) | The exact Finalmask / fingerprint / ALPN / cipher values used as defaults |
| [**MatinSenPai/SenPaiScanner**](https://github.com/MatinSenPai/SenPaiScanner) | Companion tool for finding clean Cloudflare IPs to use as a config's address |
| [XTLS/Xray-core](https://github.com/XTLS/Xray-core) | The proxy engine embedded in the app |
| [2dust/v2rayN](https://github.com/2dust/v2rayN) | The config layout the "Copy with chain" export follows (PattN is a fork of it) |
| [Wails](https://wails.io) | The native desktop shell |
| [Vazirmatn](https://github.com/rastikerdar/vazirmatn) and [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono) | The fonts used in the UI (SIL Open Font License) |

## Why a signed-in browser?

Google decides region availability **per signed-in account, after the page has loaded**. A plain HTTP request (even to the Gemini API
with a dummy key) answers "fine" from every country, so connectivity probes mark every live config as healthy. Measured while building
this tool: exits geolocated to the US, HK and SG were blocked, and the same exit can flip over time. The only reliable signal is what
Google shows a signed-in user, so that is what this tool reads:

| Product | "Blocked" looks like |
|---|---|
| AI Studio | redirect to `/docs/available-regions` |
| Gemini | "Gemini isn't currently supported in your country" |

## Download and install

Get the build for your system from the [Releases](../../releases) page. Every release ships `SHA256SUMS.txt`.

| Platform | Desktop app (native window) | Web server (U