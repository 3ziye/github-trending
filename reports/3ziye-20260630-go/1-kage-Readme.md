# kage

[![ci](https://github.com/tamnd/kage/actions/workflows/ci.yml/badge.svg)](https://github.com/tamnd/kage/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/tamnd/kage)](https://github.com/tamnd/kage/releases/latest)
[![Go Reference](https://pkg.go.dev/badge/github.com/tamnd/kage.svg)](https://pkg.go.dev/github.com/tamnd/kage)
[![Go Report Card](https://goreportcard.com/badge/github.com/tamnd/kage)](https://goreportcard.com/report/github.com/tamnd/kage)
[![License](https://img.shields.io/github/license/tamnd/kage)](./LICENSE)

**kage** (影, "shadow") clones a website into a folder you can browse offline, with every script stripped out. It opens each page in real headless Chrome, waits for the page to settle, snapshots the DOM a human would have seen, then deletes all the JavaScript and pulls the CSS, images, and fonts down to local paths. What lands on disk looks like the live site and runs no code.

[Install](#install) • [Quick start](#quick-start) • [Commands](#commands) • [Clone](#clone) • [Pack](#pack-it-into-one-file) • [Double-click app](#a-double-click-app) • [Native window](#a-real-window-not-a-browser-tab) • [How it works](#how-it-works)

![kage cloning paulgraham.com, packing it into one file, and serving it back offline](docs/static/demo.gif)

You already know the problem. You hit "Save As" on a page you want to keep, and six months later you open it to find a blank screen, a spinner that never stops, or a copy that still tries to phone home to an analytics server that no longer exists. The page was never really yours. It was a thin client for someone else's JavaScript.

kage takes the other road. It drives a real browser, lets the page finish doing whatever it does, grabs the finished result, and then rips every script out of it. No tracking, no network calls, no surprises. Just `.html` files you can open straight off disk, hand to a friend, or pack into a single file and forget about for a decade.

Full docs and guides live at **[kage.tamnd.com](https://kage.tamnd.com)**.

## Install

```bash
go install github.com/tamnd/kage/cmd/kage@latest
```

Prefer a prebuilt binary? Grab an archive, a `.deb`/`.rpm`/`.apk`, or a checksum from [releases](https://github.com/tamnd/kage/releases). Or let a package manager handle it:

```bash
# Homebrew (macOS)
brew install --cask tamnd/tap/kage

# Scoop (Windows)
scoop bucket add tamnd https://github.com/tamnd/scoop-bucket
scoop install kage

# apt (Debian, Ubuntu)
curl -fsSL https://tamnd.github.io/linux-repo/gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/tamnd.gpg
echo "deb [signed-by=/usr/share/keyrings/tamnd.gpg] https://tamnd.github.io/linux-repo/apt stable main" | sudo tee /etc/apt/sources.list.d/tamnd.list
sudo apt update && sudo apt install kage

# dnf (Fedora, RHEL)
sudo dnf config-manager --add-repo https://tamnd.github.io/linux-repo/dnf/tamnd.repo
sudo dnf install kage
```

Or skip installing Chrome yourself and use the container image, which bundles Chromium:

```bash
docker run --rm -v "$PWD/out:/out" ghcr.io/tamnd/kage clone paulgraham.com
```

kage drives a real browser, so it needs Chrome or Chromium on the host. It finds a system install on its own; point it somewhere specific with `--chrome` or the `KAGE_CHROME` environment variable. The container needs nothing extra.

Shell completion ships in the box: `kage completion bash|zsh|fish|powershell`.

## Quick start

Let's mirror Paul Graham's essays so you can read them on a plane, on a laptop with no wifi, or in the year 2050 after the site has finally changed its design:

```bash
# 1. Clone the site into $HOME/data/kage/paulgraham.com/
kage clone paulgraham.com

# 2. Read it back offline in your browser
kage serve $HOME/data/kage/paulgraham.com
# open http://127.0.0.1:8800
```

That's the whole loop. Every essay, every image, every stylesheet, frozen on your disk and runnable with zero network. The next two steps are optional but nice: collapse the whole thing into one file, and pop it open in its own window.

```bash
# 3. Squeeze the mirror into a single shareable file
kage pack paulgraham.com               # -> paulgraham.com.zim
kage open paulgraham.com.zim

# 4. Or into one executable that *is* the site
kage pack paulgraham.com --format binary -o paulgraham
./paulgraham                           # serves itself, needs nothing installed
```

## Commands

| Command | What it does |
| --- | --- |
| `kage clone <url>` | render a site in headless Chrome and write a browsable, script-free mirror |
| `kage serve [dir]` | preview a cloned folder over a local HTTP server |
| `kage pack <mirror-dir>` | collapse a mirror into one ZIM archive, a self-contained viewer binary, or a double-click app |
| `kage open <file.zim>` | serve a packed ZIM back for offline reading |

## Clone

```bash
# The whole site, into $HOME/data/kage/<host>/
kage clone https://paulgraham.com

# Just the first 50 pages, two links deep, for a quick taste
kage clone paulgraham.com --max-pages