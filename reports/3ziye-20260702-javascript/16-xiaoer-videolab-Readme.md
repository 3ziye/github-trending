<div align="center">

# 🎬 Xiaoer VideoLab

### One click. Any video. Local.

Press one toolbar button and the video on the current page lands in your `~/Downloads`.
Powered by a tiny local [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) daemon — **1800+ sites** out of the box
(YouTube · Bilibili · X/Twitter · TikTok · Vimeo · Twitch · Weibo …).

[![CI](https://github.com/Jane-xiaoer/xiaoer-videolab/actions/workflows/ci.yml/badge.svg)](https://github.com/Jane-xiaoer/xiaoer-videolab/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)
![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows-lightgrey)
![Manifest V3](https://img.shields.io/badge/Chrome-MV3-4285F4?logo=googlechrome&logoColor=white)
![Python stdlib only](https://img.shields.io/badge/Python-stdlib%20only-3776AB?logo=python&logoColor=white)
![No tracking](https://img.shields.io/badge/network-localhost%20only-27ae60)

[![English](https://img.shields.io/badge/lang-English-2563eb)](README.md)&nbsp;
[![简体中文](https://img.shields.io/badge/lang-简体中文-lightgrey)](README.zh-CN.md)

</div>

---

## 🙏 Thanks to our contributors / 致谢贡献者

**This project is better because of these people — thank you! / 本项目因他们而更好,衷心感谢!**

- [**@ttmouse**](https://github.com/ttmouse) — popup history panel, **cancel a stuck download**, play / open-folder, one-click daemon start ([#4](https://github.com/Jane-xiaoer/xiaoer-videolab/pull/4))
  <br>弹出历史面板、**取消卡住的下载**、播放 / 打开文件夹、一键启动服务
- [**@jzq1212 (林以恒)**](https://github.com/jzq1212) — **Windows support**: cross-platform daemon + PowerShell install scripts ([#1](https://github.com/Jane-xiaoer/xiaoer-videolab/pull/1))
  <br>**Windows 支持**:跨平台 daemon + PowerShell 安装脚本
- [**@alick-zhang**](https://github.com/alick-zhang) — raised the Windows request that kicked it off ([#3](https://github.com/Jane-xiaoer/xiaoer-videolab/issues/3))
  <br>提出 Windows 需求,促成了上面的 Windows 支持

> Issues & PRs welcome — your name goes here too. / 欢迎提 issue 和 PR,你的名字也会出现在这里。

---

## Why

Browser video downloaders are a swamp of sketchy extensions that beg for "read everything on every site"
permissions and phone home. Xiaoer VideoLab takes the opposite bet:

- **The extension does almost nothing.** It only reads the *current tab's URL* when you click it, and POSTs
  that one string to `127.0.0.1`. No page scraping, no content scripts, no remote servers.
- **The download happens locally.** A small Python daemon hands the URL to `yt-dlp`, the
  battle-tested open-source downloader. All the smarts live in a tool you can audit.
- **Nothing leaves your machine** except the request `yt-dlp` makes to fetch the video you asked for.

## How it works

```
 ┌─────────────────────┐   click    ┌──────────────────────────┐         ┌──────────┐
 │  Browser toolbar     │ ─────────► │  daemon @ 127.0.0.1:7788 │ ──────► │  yt-dlp  │ ──► ~/Downloads
 │  (Chrome MV3 ext.)   │  POST url  │  (Python stdlib, launchd)│  spawn  └──────────┘        │
 └─────────────────────┘            └──────────────────────────┘                              ▼
        ▲   badge: … ✓ ✕ !                       │                                   macOS notification
        └───────────────────────────────────────┘                                     "✅ <filename>"
```

- **daemon** — Python standard-library `http.server`, listens on `127.0.0.1:7788`, started at login by `launchd`.
- **extension** — Chrome MV3, a single toolbar button, grabs `tab.url` and POSTs it to the daemon.
- **output** — `~/Downloads/<platform>_<title>_<date>.mp4` (≤1080p mp4 by default; configurable).
- **log** — `~/Library/Logs/xiaoer-videolab.log`

## ✅ What you can download

Powered by yt-dlp's **1872 extractors** — most video sites work. A practical map:

| | Sites |
|---|---|
| **✅ Tested & confirmed** | **YouTube · Vimeo · Bilibili (B站) · Douyin (抖音) · Xiaohongshu (小红书)** |
| **✅ Supported** (yt-dlp extractor, same path) | X/Twitter · Ixigua (西瓜) · Instagram · Reddit · Dailymotion · Facebook · TikTok\* · …and ~1860 more |
| **⚠️ Free content only** | Youku (优酷) · iQiyi (爱奇艺) — VIP / DRM-protected episodes can't be downloaded |
| **🚫 Not recommended** | **Weibo (微博) · Zhihu (知乎)** — see note below |
| **❌ Not supported** | Kuaishou (快手) & Tencent Video (腾讯视频) — no extractor; **WeChat Channels (视频号)** — in-app & encrypted |

> 🚫 **Weibo / Zhihu — not recommended.** Their web pages are combined SPA feeds (much like TikTok): the video is just one small part of a big page, and you usually **can't open a single video on its own URL**. With no clean per-video address to grab, the button has nothing reliable to work with — so we suggest skipping them.
>
> \* **TikTok / overseas sites** need a network that can reach them (a proxy in mainland China; note some datacenter IPs are blocked by TikTok's API).
>
> 🎯 **视频号 / 快手 / 小程序 / 直播流?** Those live inside apps and need packet-sniffing — use [**res-downloader**](https://github.com/putyy/res-downloader) for them. This tool focuses 